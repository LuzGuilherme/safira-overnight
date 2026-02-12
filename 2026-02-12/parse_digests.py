#!/usr/bin/env python3
"""
Parse podcast digest markdown files into JSON for the dashboard.
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime

DIGESTS_DIR = Path("/root/clawd/memory/podcast-research/digests")
OUTPUT_FILE = Path("/root/clawd/projects/overnight-2026-02-12/digests.json")


def parse_markdown_digest(filepath: Path) -> dict:
    """Parse a single digest markdown file."""
    content = filepath.read_text(encoding="utf-8")
    
    digest = {
        "id": filepath.stem,
        "filename": filepath.name,
        "date": "",
        "title": "",
        "host": "",
        "guest": "",
        "duration": "",
        "link": "",
        "tldr": "",
        "insights": [],
        "actions": {
            "immediate": [],
            "week": [],
            "longterm": []
        },
        "quotes": [],
        "rating": 0,
        "tags": [],
        "sections": {}
    }
    
    # Extract date from filename (2026-02-11-sleep-michael-breus.md)
    date_match = re.match(r"(\d{4}-\d{2}-\d{2})", filepath.stem)
    if date_match:
        digest["date"] = date_match.group(1)
    
    # Parse metadata table
    metadata_pattern = r"\|\s*\*\*([^*]+)\*\*\s*\|\s*([^|]+)\s*\|"
    for match in re.finditer(metadata_pattern, content):
        key = match.group(1).strip().lower()
        value = match.group(2).strip()
        
        if "título" in key or "title" in key:
            digest["title"] = value
        elif "host" in key:
            digest["host"] = value
        elif "convidado" in key or "guest" in key:
            digest["guest"] = value
        elif "duração" in key or "duration" in key:
            digest["duration"] = value
        elif "link" in key:
            digest["link"] = value
    
    # Extract TL;DR
    tldr_match = re.search(r"## 🎯 TL;DR.*?\n\n(.+?)(?=\n\n---|\n\n##)", content, re.DOTALL)
    if tldr_match:
        digest["tldr"] = tldr_match.group(1).strip()
    
    # Extract Top 10 Insights
    insights_section = re.search(r"## 💡 Top 10 Insights.*?\n\n(.*?)(?=\n---|\n## )", content, re.DOTALL)
    if insights_section:
        # Parse table rows
        rows = re.findall(r"\|\s*\d+\s*\|\s*\*\*([^*]+)\*\*\s*\|\s*([^|]+)\s*\|", insights_section.group(1))
        digest["insights"] = [{"insight": r[0].strip(), "why": r[1].strip()} for r in rows]
    
    # Extract Actions
    actions_section = re.search(r"## 🛠️ Acções Práticas.*?\n\n(.*?)(?=\n---|\n## )", content, re.DOTALL)
    if actions_section:
        action_text = actions_section.group(1)
        
        # Immediate
        immediate = re.findall(r"- \[ \] (.+)", action_text.split("### Esta Semana")[0] if "### Esta Semana" in action_text else action_text)
        digest["actions"]["immediate"] = immediate[:5]
        
        # Week
        if "### Esta Semana" in action_text:
            week_section = action_text.split("### Esta Semana")[1].split("### Longo Prazo")[0] if "### Longo Prazo" in action_text else action_text.split("### Esta Semana")[1]
            week = re.findall(r"- \[ \] (.+)", week_section)
            digest["actions"]["week"] = week[:5]
        
        # Long term
        if "### Longo Prazo" in action_text:
            longterm_section = action_text.split("### Longo Prazo")[1]
            longterm = re.findall(r"- \[ \] (.+)", longterm_section)
            digest["actions"]["longterm"] = longterm[:5]
    
    # Extract Quotes
    quotes_section = re.search(r"## 💬 Quotes.*?\n\n(.*?)(?=\n---|\n## )", content, re.DOTALL)
    if quotes_section:
        quotes = re.findall(r"> \"(.+?)\"", quotes_section.group(1))
        digest["quotes"] = quotes[:5]
    
    # Extract Rating
    rating_match = re.search(r"Recomendo.*?⭐+", content)
    if rating_match:
        stars = rating_match.group(0).count("⭐")
        digest["rating"] = stars
    
    # Extract Tags
    tags_section = re.search(r"## 🏷️ Tags\s*\n\n(.+?)(?=\n---|\n## |\Z)", content, re.DOTALL)
    if tags_section:
        tags = re.findall(r"`#([^`]+)`", tags_section.group(1))
        digest["tags"] = tags
    
    return digest


def main():
    digests = []
    
    if DIGESTS_DIR.exists():
        for filepath in sorted(DIGESTS_DIR.glob("*.md"), reverse=True):
            try:
                digest = parse_markdown_digest(filepath)
                digests.append(digest)
                print(f"✅ Parsed: {filepath.name}")
            except Exception as e:
                print(f"❌ Error parsing {filepath.name}: {e}")
    
    # Write JSON
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump({
            "generated": datetime.utcnow().isoformat() + "Z",
            "count": len(digests),
            "digests": digests
        }, f, indent=2, ensure_ascii=False)
    
    print(f"\n📦 Generated {OUTPUT_FILE} with {len(digests)} digests")


if __name__ == "__main__":
    main()
