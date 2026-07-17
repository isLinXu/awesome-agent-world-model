#!/usr/bin/env python3
"""
Auto-update script for Awesome Agent World Model.

Fetches latest papers from multiple sources:
  1. arXiv API (keyword search)
  2. HuggingFace Papers (https://huggingface.co/api/papers)
  3. Papers with Code (https://paperswithcode.com/search)

Papers are classified into README sections and inserted with cross-source
deduplication based on arXiv ID.
"""

import argparse
import json
import re
import sys
import time
import html as html_mod
from datetime import datetime, timedelta
from typing import List, Dict, Set, Optional
import requests
import xml.etree.ElementTree as ET

# ─── Configuration ───────────────────────────────────────────────────────────

# arXiv API endpoint
ARXIV_API = "http://export.arxiv.org/api/query"

# HuggingFace Papers API
HF_PAPERS_API = "https://huggingface.co/api/papers"

# Papers with Code search URL
PWC_SEARCH_URL = "https://paperswithcode.com/search"

# World model related search queries (OR combined for arXiv)
SEARCH_QUERIES = [
    "world model",
    "world models",
    "embodied AI",
    "VLA vision language action",
    "robot manipulation world model",
    "physical AI simulation",
    "dreamer RSSM",
    "JEPA predictive architecture",
    "genie interactive world",
    "gaia autonomous driving",
    "cosmos NVIDIA world",
]

# Keywords for filtering HF / PwC papers (case-insensitive substring match)
# Broader than arXiv queries to catch trending papers that don't use exact terms
SOURCE_FILTER_KEYWORDS = [
    "world model", "world models", "embodied", "physical ai",
    "vla", "vision language action", "robot", "manipulation",
    "simulation", "digital twin", "predictive model", "dreamer",
    "jepa", "genie", "gaia", "cosmos", "video generation",
    "autonomous driving", "reinforcement learning", "model-based",
    "agent", "planning", "interactive", "generative simulation",
]

# Valid paper sections in README (only these have paper tables)
PAPER_SECTIONS = {
    "物理 AI 元年 (2025-2026)",
    "快速突破期 (2023-2024)",
    "奠基性工作 (2018-2022)",
    "世界模型综述专区",
    "世界模型六大流派",
    "Agent 系统范式论文",
    "安全与对齐论文",
}

# Section mapping: (keyword_pattern, section_title_in_readme)
# Patterns are checked IN ORDER - first match wins
SECTION_MAP = [
    # Specific 2026 papers
    ("(versecrafter|neoverse|videoworld 2|geoworld|drivelaw|rynnworld|lingbot|foresight governance|worldscore|worldarena 2)",
     "物理 AI 元年 (2025-2026)"),
    # Survey papers
    ("(survey|review|comprehensive|tutorial).*world model",
     "世界模型综述专区"),
    # Foundational works (before year check)
    ("(world models ha schmidhuber|planet deep planning|dreamer|rssm|predrnn|muzero|world models.*2018|world models.*2019|world models.*2020|world models.*2021)",
     "奠基性工作 (2018-2022)"),
    # JEPA specifically
    ("(jepa|joint embedding predictive|lecun.*jepa)",
     "奠基性工作 (2018-2022)"),
    # VLA papers
    (r"(π0|openvla|neurovla|rynnvla|gr-3|smolvla|vla.*robot|vision language action|physical intelligence|π0\.5)",
     "物理 AI 元年 (2025-2026)"),
    # World model frameworks (new ones)
    ("(genie.*2|genie.*3|gaia.*2|cosmos.*predict|cosmos.*transfer|wvm|lewm|awm|qwen.*agentworld|cosmos 3|marble)",
     "物理 AI 元年 (2025-2026)"),
    # General world models (recent)
    ("(world model|physical ai|embodied intelligence|simulation.*robot|digital twin)",
     "物理 AI 元年 (2025-2026)"),
]

# Source badges for README entries
SOURCE_BADGES = {
    "arxiv": "arXiv",
    "huggingface": "🤗 HF",
    "paperswithcode": "PwC",
}

# ─── Data Source 1: arXiv API ────────────────────────────────────────────────

def fetch_arxiv_papers(start_date: str, end_date: str, max_results: int = 50) -> List[Dict]:
    """Fetch papers from arXiv API with retry logic."""
    query = " OR ".join([f'"{q}"' for q in SEARCH_QUERIES])

    params = {
        "search_query": f"all:({query})",
        "start": 0,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }

    max_retries = 3
    for attempt in range(max_retries):
        try:
            if attempt > 0:
                wait = 2 ** attempt
                print(f"  [arXiv] Retrying in {wait}s... (attempt {attempt + 1}/{max_retries})")
                time.sleep(wait)

            response = requests.get(ARXIV_API, params=params, timeout=30)
            response.raise_for_status()
            break
        except requests.RequestException as e:
            print(f"  [arXiv] Error (attempt {attempt + 1}): {e}", file=sys.stderr)
            if attempt == max_retries - 1:
                return []

    try:
        root = ET.fromstring(response.content)
    except ET.ParseError as e:
        print(f"  [arXiv] XML parse error: {e}", file=sys.stderr)
        return []

    ns = {
        "atom": "http://www.w3.org/2005/Atom",
        "arxiv": "http://arxiv.org/schemas/atom",
    }

    papers = []
    for entry in root.findall("atom:entry", ns):
        title_elem = entry.find("atom:title", ns)
        published_elem = entry.find("atom:published", ns)
        summary_elem = entry.find("atom:summary", ns)
        id_elem = entry.find("atom:id", ns)

        title = title_elem.text.strip() if title_elem is not None and title_elem.text else ""
        published = published_elem.text[:10] if published_elem is not None and published_elem.text else ""
        summary = summary_elem.text.strip() if summary_elem is not None and summary_elem.text else ""
        entry_id = id_elem.text if id_elem is not None and id_elem.text else ""

        # Extract arXiv ID
        arxiv_id = ""
        arxiv_match = re.search(r'arXiv:(\d+\.\d+)', entry_id)
        if arxiv_match:
            arxiv_id = arxiv_match.group(1)
        else:
            url_match = re.search(r'/(\d+\.\d+)', entry_id)
            arxiv_id = url_match.group(1) if url_match else ""

        # Categories
        categories = []
        primary_category = ""
        for cat in entry.findall("atom:category", ns):
            term = cat.get("term", "")
            categories.append(term)
            if not primary_category:
                primary_category = term

        # Authors
        authors = []
        for author in entry.findall("atom:author", ns):
            name_elem = author.find("atom:name", ns)
            if name_elem is not None and name_elem.text:
                authors.append(name_elem.text)

        # Filter by date
        if start_date <= published <= end_date:
            papers.append({
                "title": title,
                "authors": authors,
                "published": published,
                "summary": summary,
                "arxiv_id": arxiv_id,
                "primary_category": primary_category,
                "categories": categories,
                "source": "arxiv",
                "upvotes": 0,
                "github_repo": "",
                "github_stars": 0,
            })

    print(f"  [arXiv] Fetched {len(papers)} papers")
    return papers


# ─── Data Source 2: HuggingFace Papers API ───────────────────────────────────

def fetch_huggingface_papers(start_date: str, end_date: str, max_results: int = 100) -> List[Dict]:
    """Fetch trending papers from HuggingFace Papers API.

    The API returns daily paper lists. We fetch multiple days to cover
    the requested date range, then filter by keywords.
    """
    papers = []
    seen_ids: Set[str] = set()

    # Parse dates and iterate day by day
    try:
        d_start = datetime.strptime(start_date, "%Y-%m-%d")
        d_end = datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        print(f"  [HF] Invalid date format, skipping", file=sys.stderr)
        return []

    # HF API uses the paper's publishedAt date (not submission date)
    # We iterate from end_date backwards to start_date
    current = d_end
    while current >= d_start and len(papers) < max_results:
        date_str = current.strftime("%Y-%m-%d")
        url = f"{HF_PAPERS_API}?date={date_str}"

        max_retries = 3
        for attempt in range(max_retries):
            try:
                if attempt > 0:
                    wait = 2 ** attempt
                    print(f"  [HF] Retrying {date_str} in {wait}s...")
                    time.sleep(wait)

                response = requests.get(url, timeout=30)
                response.raise_for_status()
                break
            except requests.RequestException as e:
                print(f"  [HF] Error fetching {date_str} (attempt {attempt + 1}): {e}",
                      file=sys.stderr)
                if attempt == max_retries - 1:
                    response = None

        if response is None:
            current -= timedelta(days=1)
            continue

        try:
            daily_papers = response.json()
        except json.JSONDecodeError:
            print(f"  [HF] JSON decode error for {date_str}", file=sys.stderr)
            current -= timedelta(days=1)
            continue

        for entry in daily_papers:
            paper_info = entry.get("paper", entry)
            arxiv_id = paper_info.get("id", "")

            # Deduplicate across days
            if arxiv_id in seen_ids:
                continue
            seen_ids.add(arxiv_id)

            published = paper_info.get("publishedAt", "")[:10]
            title = paper_info.get("title", "")
            summary = paper_info.get("summary", "")
            upvotes = entry.get("upvotes", paper_info.get("upvotes", 0))
            github_repo = paper_info.get("githubRepo", "")
            github_stars = paper_info.get("githubStars", 0)

            # AI-generated keywords (if available)
            ai_keywords = paper_info.get("ai_keywords", [])

            # Filter by keyword relevance
            combined_text = f"{title} {summary} {' '.join(ai_keywords)}".lower()
            if not any(kw in combined_text for kw in SOURCE_FILTER_KEYWORDS):
                continue

            # Filter by date range
            if published and not (start_date <= published <= end_date):
                continue

            papers.append({
                "title": title,
                "authors": [a.get("name", "") for a in paper_info.get("authors", [])],
                "published": published or date_str,
                "summary": summary,
                "arxiv_id": arxiv_id,
                "primary_category": "",
                "categories": [],
                "source": "huggingface",
                "upvotes": upvotes,
                "github_repo": github_repo,
                "github_stars": github_stars,
            })

        current -= timedelta(days=1)

    print(f"  [HF] Fetched {len(papers)} relevant papers")
    return papers


# ─── Data Source 3: Papers with Code ─────────────────────────────────────────

def fetch_paperswithcode_papers(start_date: str, end_date: str,
                                max_results: int = 50) -> List[Dict]:
    """Fetch papers from Papers with Code by scraping search results.

    PwC's API has been merged with HuggingFace, but the web search page
    still returns structured data embedded in SVELTE_HYDRATER attributes.
    We extract paper data from the HTML and filter by keywords.
    """
    papers = []

    # Build search queries (PwC search supports space-separated keywords)
    search_terms = ["world model", "embodied AI", "physical AI",
                    "VLA robot", "video generation world"]

    seen_ids: Set[str] = set()

    for term in search_terms:
        if len(papers) >= max_results:
            break

        params = {"q": term}
        headers = {"User-Agent": "Mozilla/5.0 (compatible; AutoUpdateBot/1.0)"}

        max_retries = 3
        response = None
        for attempt in range(max_retries):
            try:
                if attempt > 0:
                    wait = 2 ** attempt
                    print(f"  [PwC] Retrying '{term}' in {wait}s...")
                    time.sleep(wait)

                response = requests.get(PWC_SEARCH_URL, params=params,
                                        headers=headers, timeout=30,
                                        allow_redirects=True)
                response.raise_for_status()
                break
            except requests.RequestException as e:
                print(f"  [PwC] Error fetching '{term}' (attempt {attempt + 1}): {e}",
                      file=sys.stderr)
                if attempt == max_retries - 1:
                    response = None

        if response is None or response.status_code != 200:
            continue

        html_content = response.text

        # Extract SVELTE_HYDRATER data-props JSON
        # Pattern: data-target="DailyPapers" data-props="{...JSON...}"
        match = re.search(
            r'data-target="DailyPapers"[^>]*data-props="([^"]+)"',
            html_content
        )

        if not match:
            # Try alternative pattern (SearchResults)
            match = re.search(
                r'data-target="SearchResults"[^>]*data-props="([^"]+)"',
                html_content
            )

        if not match:
            print(f"  [PwC] No structured data found for '{term}'")
            continue

        # Unescape HTML entities and parse JSON
        try:
            raw_json = html_mod.unescape(match.group(1))
            data = json.loads(raw_json)
        except (json.JSONDecodeError, ValueError) as e:
            print(f"  [PwC] JSON parse error for '{term}': {e}", file=sys.stderr)
            continue

        # Extract papers from dailyPapers or results
        daily_papers = data.get("dailyPapers", data.get("results", []))

        for entry in daily_papers:
            paper_info = entry.get("paper", entry)
            arxiv_id = paper_info.get("id", "")

            if not arxiv_id or arxiv_id in seen_ids:
                continue
            seen_ids.add(arxiv_id)

            title = paper_info.get("title", "")
            summary = paper_info.get("summary", "")
            published = paper_info.get("publishedAt", "")[:10]
            upvotes = entry.get("upvotes", paper_info.get("upvotes", 0))
            github_repo = paper_info.get("githubRepo", "")
            github_stars = paper_info.get("githubStars", 0)

            # Filter by keyword relevance
            combined_text = f"{title} {summary}".lower()
            if not any(kw in combined_text for kw in SOURCE_FILTER_KEYWORDS):
                continue

            # Filter by date range (PwC may have older papers)
            if published and not (start_date <= published <= end_date):
                continue

            papers.append({
                "title": title,
                "authors": [a.get("name", "") for a in paper_info.get("authors", [])],
                "published": published,
                "summary": summary,
                "arxiv_id": arxiv_id,
                "primary_category": "",
                "categories": [],
                "source": "paperswithcode",
                "upvotes": upvotes,
                "github_repo": github_repo,
                "github_stars": github_stars,
            })

            if len(papers) >= max_results:
                break

    print(f"  [PwC] Fetched {len(papers)} relevant papers")
    return papers


# ─── Cross-source Deduplication ──────────────────────────────────────────────

def deduplicate_papers(papers: List[Dict]) -> List[Dict]:
    """Deduplicate papers across sources based on arXiv ID.

    Priority: arXiv > HuggingFace > Papers with Code
    (arXiv has the richest metadata; HF/PwC add social signals like upvotes)
    If a paper appears in multiple sources, merge metadata from all sources
    but keep the highest-priority source as primary.
    """
    source_priority = {"arxiv": 0, "huggingface": 1, "paperswithcode": 2}
    seen: Dict[str, Dict] = {}

    # Sort by source priority so highest-priority source is processed first
    sorted_papers = sorted(papers, key=lambda p: source_priority.get(p.get("source", ""), 3))

    for paper in sorted_papers:
        arxiv_id = paper.get("arxiv_id", "")
        if not arxiv_id:
            continue

        if arxiv_id not in seen:
            seen[arxiv_id] = paper
        else:
            # Merge: fill in missing fields from lower-priority source
            existing = seen[arxiv_id]
            if not existing.get("github_repo") and paper.get("github_repo"):
                existing["github_repo"] = paper["github_repo"]
            if not existing.get("github_stars") and paper.get("github_stars"):
                existing["github_stars"] = paper["github_stars"]
            if not existing.get("upvotes") and paper.get("upvotes"):
                existing["upvotes"] = paper["upvotes"]
            # Track all sources
            all_sources = existing.get("all_sources", [existing.get("source", "")])
            if paper.get("source") and paper["source"] not in all_sources:
                all_sources.append(paper["source"])
            existing["all_sources"] = all_sources

    deduped = list(seen.values())
    removed = len(papers) - len(deduped)
    print(f"  [Dedup] Removed {removed} duplicates, {len(deduped)} unique papers")
    return deduped


# ─── Classification ──────────────────────────────────────────────────────────

def classify_paper(paper: Dict) -> str:
    """Classify paper into README section.

    Logic: Pattern matching first (specific keywords), then year-based fallback.
    """
    text = f"{paper['title']} {paper['summary']}".lower()

    # Step 1: Try specific pattern matching first
    for pattern, section in SECTION_MAP:
        if re.search(pattern, text):
            if section in PAPER_SECTIONS:
                return section
            # Fallback if mapped to non-paper section
            year = int(paper["published"][:4]) if paper["published"] else 2026
            if year >= 2025:
                return "物理 AI 元年 (2025-2026)"
            elif year >= 2023:
                return "快速突破期 (2023-2024)"
            return "奠基性工作 (2018-2022)"

    # Step 2: Year-based fallback
    year_str = paper.get("published", "2026")[:4]
    try:
        year = int(year_str)
    except ValueError:
        year = 2026

    if year >= 2025:
        return "物理 AI 元年 (2025-2026)"
    elif year >= 2023:
        return "快速突破期 (2023-2024)"
    elif year >= 2018:
        return "奠基性工作 (2018-2022)"

    return "物理 AI 元年 (2025-2026)"


# ─── Formatting ──────────────────────────────────────────────────────────────

def format_paper_entry(paper: Dict) -> str:
    """Format paper as README table row.

    Columns: | Year | Title | Authors | Summary | Link+Source |
    """
    year = paper.get("published", "2026")[:4]
    title = paper["title"].replace("|", "\\|")

    # Truncate summary to ~80 chars
    summary = paper.get("summary", "")
    if len(summary) > 80:
        break_at = summary.rfind(".", 0, 80)
        if break_at == -1:
            break_at = summary.rfind(",", 0, 80)
        if break_at == -1:
            break_at = summary.rfind(" ", 70, 85)
        if break_at == -1:
            break_at = 80
        summary = summary[:break_at] + "..."

    summary = summary.replace("|", "\\|").replace("\n", " ")

    # Authors (first 2 + et al. if more)
    authors_list = paper.get("authors", [])
    authors = ", ".join(authors_list[:2]) if authors_list else "Unknown"
    if len(authors_list) > 2:
        authors += " et al."

    # arXiv link
    arxiv_id = paper.get("arxiv_id", "")
    arxiv_link = f"https://arxiv.org/abs/{arxiv_id}" if arxiv_id else ""

    # Source badge(s)
    all_sources = paper.get("all_sources", [paper.get("source", "arxiv")])
    source_labels = []
    for src in all_sources:
        label = SOURCE_BADGES.get(src, src)
        if label not in source_labels:
            source_labels.append(label)
    source_str = " + ".join(source_labels)

    # Venue / category
    venue = paper.get("primary_category", "").upper()
    if not venue:
        venue = "CS.AI"
    venue_badge = f"arXiv:{venue}"

    # Build link cell with source badge
    link_cell = f"[📄 {venue_badge}]({arxiv_link})"
    if paper.get("upvotes", 0) > 0:
        link_cell += f" ⬆{paper['upvotes']}"
    if paper.get("github_repo"):
        link_cell += f" [🐙 Repo]({paper['github_repo']})"
    link_cell += f" `{source_str}`"

    entry = f"| {year} | **{title}** | {authors} | {summary} | {link_cell} |"
    return entry


# ─── README Insertion ────────────────────────────────────────────────────────

def insert_papers_into_readme(readme_path: str, papers: List[Dict],
                              dry_run: bool = False) -> tuple:
    """Insert papers into appropriate README sections.

    Returns (summary_string, inserted_count).
    """
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Group papers by section
    section_papers: Dict[str, List[Dict]] = {}
    for paper in papers:
        section = classify_paper(paper)
        if section not in section_papers:
            section_papers[section] = []
        section_papers[section].append(paper)

    inserted = 0
    for section, section_paper_list in section_papers.items():
        # Find section in README
        section_pattern = f"### {section}"
        if section_pattern not in content:
            print(f"  Warning: Section '{section}' not found in README", file=sys.stderr)
            continue

        section_idx = content.find(section_pattern)

        # Try Chinese header first, then English
        table_start = content.find("| 年份 |", section_idx)
        if table_start == -1:
            table_start = content.find("| Year |", section_idx)

        if table_start == -1:
            print(f"  Warning: No table found in section '{section}'", file=sys.stderr)
            continue

        # Find end of table (next blank line or next section/header)
        lines_after_table = content[table_start:].split('\n')
        table_lines = []
        found_separator = False
        for i, line in enumerate(lines_after_table):
            if i == 0 and ("年份" in line or "Year" in line):
                table_lines.append(line)
                continue
            if i == 1 and line.startswith("|") and ":-" in line:
                table_lines.append(line)
                found_separator = True
                continue
            if found_separator and line.strip().startswith("|"):
                table_lines.append(line)
            elif found_separator and line.strip() == "":
                break
            elif found_separator and line.startswith("#"):
                break
            else:
                break

        # Calculate insert position (after header + separator)
        insert_offset = 0
        for line in table_lines[:2]:  # header + separator
            insert_offset += len(line) + 1  # +1 for newline

        insert_position = table_start + insert_offset

        # Check for duplicates before inserting
        existing_content = content[table_start:table_start + insert_offset + 10000]

        # Format and insert entries
        entries = []
        for paper in section_paper_list:
            entry = format_paper_entry(paper)
            # Skip if paper already exists (check by arXiv ID)
            arxiv_id = paper.get("arxiv_id", "")
            if arxiv_id and arxiv_id in existing_content:
                print(f"  Skipping duplicate (already in README): {paper['title'][:50]}...")
                continue
            entries.append(entry)
            inserted += 1

        if not entries:
            continue

        # Insert entries
        new_content = content[:insert_position] + '\n'.join(entries) + '\n' + content[insert_position:]
        content = new_content

    if not dry_run and inserted > 0:
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(content)

    return (f"Inserted {inserted} papers across {len(section_papers)} sections", inserted)


# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Auto-update world model papers in README.md from multiple sources"
    )
    parser.add_argument("--start_date", type=str, required=True,
                        help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end_date", type=str, required=True,
                        help="End date (YYYY-MM-DD)")
    parser.add_argument("--readme", type=str, default="README.md",
                        help="Path to README.md")
    parser.add_argument("--max_results", type=int, default=50,
                        help="Max papers per source")
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview changes without writing")
    parser.add_argument("--sources", type=str, default="arxiv,huggingface,paperswithcode",
                        help="Comma-separated list of sources to fetch from "
                             "(arxiv, huggingface, paperswithcode)")
    args = parser.parse_args()

    enabled_sources = [s.strip() for s in args.sources.split(",") if s.strip()]
    print(f"Fetching papers from {args.start_date} to {args.end_date}")
    print(f"Enabled sources: {enabled_sources}")
    print(f"Max results per source: {args.max_results}")
    print()

    all_papers: List[Dict] = []

    # ── Fetch from each enabled source ──
    if "arxiv" in enabled_sources:
        print("━━━ Fetching from arXiv ━━━")
        arxiv_papers = fetch_arxiv_papers(args.start_date, args.end_date,
                                          args.max_results)
        all_papers.extend(arxiv_papers)

    if "huggingface" in enabled_sources:
        print("━━━ Fetching from HuggingFace Papers ━━━")
        hf_papers = fetch_huggingface_papers(args.start_date, args.end_date,
                                             args.max_results)
        all_papers.extend(hf_papers)

    if "paperswithcode" in enabled_sources:
        print("━━━ Fetching from Papers with Code ━━━")
        pwc_papers = fetch_paperswithcode_papers(args.start_date, args.end_date,
                                                args.max_results)
        all_papers.extend(pwc_papers)

    print(f"\nTotal fetched (before dedup): {len(all_papers)}")

    if not all_papers:
        print("No papers found from any source")
        return

    # ── Cross-source deduplication ──
    print("\n━━━ Deduplicating ━━━")
    papers = deduplicate_papers(all_papers)

    # ── Classify ──
    print("\n━━━ Classifying papers ━━━")
    for paper in papers:
        section = classify_paper(paper)
        source = paper.get("source", "?")
        upvotes = paper.get("upvotes", 0)
        upvote_str = f" ⬆{upvotes}" if upvotes else ""
        print(f"  [{section}] ({source}{upvote_str}) {paper['title'][:65]}...")

    # ── Insert into README ──
    print(f"\n━━━ Inserting into {args.readme} ━━━")
    if args.dry_run:
        print("[DRY RUN] No changes will be written")

    result, count = insert_papers_into_readme(args.readme, papers, args.dry_run)
    print(result)

    # ── Summary by source ──
    print("\n━━━ Summary by source ━━━")
    source_counts: Dict[str, int] = {}
    for p in papers:
        src = p.get("source", "unknown")
        source_counts[src] = source_counts.get(src, 0) + 1
    for src, count in sorted(source_counts.items()):
        badge = SOURCE_BADGES.get(src, src)
        print(f"  {badge}: {count} papers")

    if count == 0:
        print("\nAll papers were already in the README or could not be classified.")


if __name__ == "__main__":
    main()
