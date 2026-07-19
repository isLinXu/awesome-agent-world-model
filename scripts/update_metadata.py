#!/usr/bin/env python3
"""
Update metadata in README.md: version badge, entry count, last update date.
"""

import re
from datetime import datetime

README_PATH = "README.md"
# After v8.0 split, paper tables live in sub-documents
SUB_DOCS = {
    "papers": "docs/papers.md",
    "frameworks": "docs/frameworks.md",
    "industry": "docs/industry.md",
    "technical": "docs/technical.md",
    "references": "docs/references.md",
}


def count_entries(content: str) -> int:
    """Count total entries (table rows with links)."""
    # Count table rows with links
    rows = [l for l in content.split('\n') if l.strip().startswith('|') and 'http' in l]
    return len(rows)


def count_papers(content: str) -> int:
    """Count paper entries in research paper sections."""
    # Look for paper table rows with Year column
    count = 0
    for line in content.split('\n'):
        if line.strip().startswith('|') and re.search(r'\|\s*\d{4}\s*\|.*\|\s*\[.*arXiv', line):
            count += 1
    return count


def update_metadata():
    with open(README_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    # After v8.0 split: count entries and papers across all sub-documents
    total_entries = 0
    total_papers = 0
    for doc_name, doc_path in SUB_DOCS.items():
        try:
            with open(doc_path, 'r', encoding='utf-8') as f:
                doc_content = f.read()
            total_entries += count_entries(doc_content)
            total_papers += count_papers(doc_content)
        except FileNotFoundError:
            print(f"Warning: {doc_path} not found, skipping")

    # Update entry count badge (match any existing number + optional trailing link)
    content = re.sub(
        r'\[!\[Entries\]\(https://img\.shields\.io/badge/Entries-\d+%2B-orange\)\]\([^)]*\)',
        f'[![Entries](https://img.shields.io/badge/Entries-{total_entries}%2B-orange)]()',
        content
    )

    # Update last update date
    today = datetime.now().strftime("%Y-%m-%d")
    old_date = re.search(r'Last%20Update-\d{4}--\d{2}--\d{2}', content)
    if old_date:
        new_date = f"Last%20Update-{today}"
        content = content.replace(old_date.group(), new_date)

    # Update last updated in footer
    old_footer = re.search(r'> \*\*最后更新\*\*：\d{4}-\d{2}-\d{2}', content)
    if old_footer:
        new_footer = f"> **最后更新**：{today}"
        content = content.replace(old_footer.group(), new_footer)

    # Update paper count and total in coverage matrix (now in docs/technical.md)
    tech_path = SUB_DOCS["technical"]
    try:
        with open(tech_path, 'r', encoding='utf-8') as f:
            tech_content = f.read()
        old_papers = re.search(r'\| 研究论文 \| \d+ \| \d+% \|', tech_content)
        if old_papers:
            new_papers = f"| 研究论文 | {total_papers} | 99% |"
            tech_content = tech_content.replace(old_papers.group(), new_papers)
        old_total = re.search(r'\| \*\*总计\*\* \| \*\*\d+\+\*\* \|', tech_content)
        if old_total:
            new_total = f"| **总计** | **{total_entries}+** |"
            tech_content = tech_content.replace(old_total.group(), new_total)
        with open(tech_path, 'w', encoding='utf-8') as f:
            f.write(tech_content)
    except FileNotFoundError:
        print(f"Warning: {tech_path} not found, skipping coverage matrix update")

    with open(README_PATH, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Updated: {total_entries} total entries, {total_papers} papers, date: {today}")


if __name__ == "__main__":
    update_metadata()
