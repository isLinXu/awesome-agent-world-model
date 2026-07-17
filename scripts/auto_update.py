#!/usr/bin/env python3
"""
Auto-update script for Awesome Agent World Model.
Fetches latest arXiv papers related to world models, classifies them,
and inserts into the appropriate README.md sections.
"""

import argparse
import re
import sys
import time
from datetime import datetime
from typing import List, Dict
import requests
import xml.etree.ElementTree as ET

# arXiv API endpoint
ARXIV_API = "http://export.arxiv.org/api/query"

# World model related search queries (OR combined)
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
    ("(π0|openvla|neurovla|rynnvla|gr-3|smolvla|vla.*robot|vision language action|physical intelligence|π0\.5)",
     "物理 AI 元年 (2025-2026)"),
    # World model frameworks (new ones)
    ("(genie.*2|genie.*3|gaia.*2|cosmos.*predict|cosmos.*transfer|wvm|lewm|awm|qwen.*agentworld|cosmos 3|marble)",
     "物理 AI 元年 (2025-2026)"),
    # General world models (recent)
    ("(world model|physical ai|embodied intelligence|simulation.*robot|digital twin)",
     "物理 AI 元年 (2025-2026)"),
]


def fetch_arxiv_papers(start_date: str, end_date: str, max_results: int = 50) -> List[Dict]:
    """Fetch papers from arXiv API with retry logic."""
    # Build search query
    query = " OR ".join([f'"{q}"' for q in SEARCH_QUERIES])
    
    params = {
        "search_query": f"all:({query})",
        "start": 0,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    
    # Retry with exponential backoff
    max_retries = 3
    for attempt in range(max_retries):
        try:
            if attempt > 0:
                wait = 2 ** attempt
                print(f"Retrying in {wait}s... (attempt {attempt + 1}/{max_retries})")
                time.sleep(wait)
            
            response = requests.get(ARXIV_API, params=params, timeout=30)
            response.raise_for_status()
            break
        except requests.RequestException as e:
            print(f"Error fetching from arXiv (attempt {attempt + 1}): {e}", file=sys.stderr)
            if attempt == max_retries - 1:
                return []
    
    # Parse XML
    try:
        root = ET.fromstring(response.content)
    except ET.ParseError as e:
        print(f"Error parsing arXiv XML: {e}", file=sys.stderr)
        return []
    
    # Namespace
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
        
        paper = {
            "title": title_elem.text.strip() if title_elem is not None and title_elem.text else "",
            "authors": [author.find("atom:name", ns).text for author in entry.findall("atom:author", ns) 
                       if author.find("atom:name", ns) is not None and author.find("atom:name", ns).text],
            "published": published_elem.text[:10] if published_elem is not None and published_elem.text else "",
            "summary": summary_elem.text.strip() if summary_elem is not None and summary_elem.text else "",
            "id": id_elem.text if id_elem is not None and id_elem.text else "",
            "primary_category": "",
            "categories": [],
        }
        
        # Get categories
        for cat in entry.findall("atom:category", ns):
            term = cat.get("term", "")
            paper["categories"].append(term)
            if not paper["primary_category"]:
                paper["primary_category"] = term
        
        # Extract arXiv ID from URL
        arxiv_match = re.search(r'arXiv:(\d+\.\d+)', paper["id"])
        if arxiv_match:
            paper["arxiv_id"] = arxiv_match.group(1)
        else:
            # Try URL format
            url_match = re.search(r'/(\d+\.\d+)', paper["id"])
            paper["arxiv_id"] = url_match.group(1) if url_match else ""
        
        # Filter by date
        if start_date <= paper["published"] <= end_date:
            papers.append(paper)
    
    return papers


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
            year = int(paper["published"][:4])
            if year >= 2025:
                return "物理 AI 元年 (2025-2026)"
            elif year >= 2023:
                return "快速突破期 (2023-2024)"
            return "奠基性工作 (2018-2022)"
    
    # Step 2: Year-based fallback
    year = int(paper["published"][:4])
    if year >= 2025:
        return "物理 AI 元年 (2025-2026)"
    elif year >= 2023:
        return "快速突破期 (2023-2024)"
    elif year >= 2018:
        return "奠基性工作 (2018-2022)"
    
    return "物理 AI 元年 (2025-2026)"


def format_paper_entry(paper: Dict) -> str:
    """Format paper as README table row."""
    year = paper["published"][:4]
    title = paper["title"].replace("|", "\\|")  # Escape pipe in title
    
    # Truncate summary to ~80 chars
    summary = paper["summary"]
    if len(summary) > 80:
        # Try to break at sentence or comma
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
    authors = ", ".join(paper["authors"][:2])
    if len(paper["authors"]) > 2:
        authors += " et al."
    
    # arXiv link
    arxiv_link = f"https://arxiv.org/abs/{paper['arxiv_id']}"
    
    # Venue badge
    venue = paper["primary_category"].upper()
    if venue in ["CS.CV", "CS.RO", "CS.LG", "CS.AI"]:
        venue_badge = f"arXiv:{venue}"
    else:
        venue_badge = f"arXiv:{venue}"
    
    entry = f"| {year} | **{title}** | {authors} | {summary} | [📄 {venue_badge}]({arxiv_link}) |"
    return entry


def insert_papers_into_readme(readme_path: str, papers: List[Dict], dry_run: bool = False) -> str:
    """Insert papers into appropriate README sections."""
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Group papers by section
    section_papers = {}
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
            print(f"Warning: Section '{section}' not found in README", file=sys.stderr)
            continue
        
        # Find the table under this section
        section_idx = content.find(section_pattern)
        
        # Try Chinese header first, then English
        table_start = content.find("| 年份 |", section_idx)
        if table_start == -1:
            table_start = content.find("| Year |", section_idx)
        
        if table_start == -1:
            print(f"Warning: No table found in section '{section}'", file=sys.stderr)
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
            elif found_separator and line.startswith("##"):
                break
            else:
                break
        
        # Calculate insert position (after header + separator)
        insert_offset = 0
        for line in table_lines[:2]:  # header + separator
            insert_offset += len(line) + 1  # +1 for newline
        
        insert_position = table_start + insert_offset
        
        # Check for duplicates before inserting
        existing_content = content[table_start:table_start + insert_offset + 5000]
        
        # Format and insert entries
        entries = []
        for paper in section_paper_list:
            entry = format_paper_entry(paper)
            # Skip if paper already exists (check by arXiv ID)
            if paper.get("arxiv_id") and paper["arxiv_id"] in existing_content:
                print(f"  Skipping duplicate: {paper['title'][:50]}...")
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
    
    return f"Inserted {inserted} papers across {len(section_papers)} sections"


def main():
    parser = argparse.ArgumentParser(description="Auto-update world model papers in README.md")
    parser.add_argument("--start_date", type=str, required=True, help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end_date", type=str, required=True, help="End date (YYYY-MM-DD)")
    parser.add_argument("--readme", type=str, default="README.md", help="Path to README.md")
    parser.add_argument("--max_results", type=int, default=50, help="Max papers to fetch")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without writing")
    args = parser.parse_args()
    
    print(f"Fetching papers from {args.start_date} to {args.end_date}...")
    papers = fetch_arxiv_papers(args.start_date, args.end_date, args.max_results)
    print(f"Found {len(papers)} papers")
    
    if not papers:
        print("No papers found in date range")
        return
    
    print("Classifying papers...")
    for paper in papers:
        section = classify_paper(paper)
        print(f"  [{section}] {paper['title'][:60]}...")
    
    print(f"\nInserting into {args.readme}...")
    result = insert_papers_into_readme(args.readme, papers, args.dry_run)
    print(result)


if __name__ == "__main__":
    main()
