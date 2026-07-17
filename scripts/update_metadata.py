#!/usr/bin/env python3
"""
Update metadata in README.md: version badge, entry count, last update date.
"""

import re
from datetime import datetime

README_PATH = "README.md"


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
    
    # Count entries
    total_entries = count_entries(content)
    total_papers = count_papers(content)
    
    # Update entry count badge
    old_entries = "[![Entries](https://img.shields.io/badge/Entries-380%2B-orange)]()"
    new_entries = f"[![Entries](https://img.shields.io/badge/Entries-{total_entries}%2B-orange)]()"
    if old_entries in content:
        content = content.replace(old_entries, new_entries)
    
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
    
    # Update paper count in coverage matrix
    old_papers = re.search(r'\| 研究论文 \| \d+ \| \d+% \|', content)
    if old_papers:
        new_papers = f"| 研究论文 | {total_papers} | 99% |"
        content = content.replace(old_papers.group(), new_papers)
    
    # Update total count in coverage matrix
    old_total = re.search(r'\| \*\*总计\*\* \| \*\*\d+\+\*\* \|', content)
    if old_total:
        new_total = f"| **总计** | **{total_entries}+** |"
        content = content.replace(old_total.group(), new_total)
    
    with open(README_PATH, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated: {total_entries} total entries, {total_papers} papers, date: {today}")


if __name__ == "__main__":
    update_metadata()
