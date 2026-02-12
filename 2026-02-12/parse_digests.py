#!/usr/bin/env python3
"""
Parse podcast digest markdown files into JSON for the dashboard.
v2.0 - Inclui TODAS as secções
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime

DIGESTS_DIR = Path("/root/clawd/memory/podcast-research/digests")
OUTPUT_FILE = Path("/root/clawd/overnight/2026-02-12/digests.json")


def extract_section(content: str, header_pattern: str, end_pattern: str = r"\n---|\n## ") -> str:
    """Extract content between a header and the next section."""
    match = re.search(f"{header_pattern}.*?\n\n(.*?)(?={end_pattern})", content, re.DOTALL)
    return match.group(1).strip() if match else ""


def parse_subsections(section_text: str) -> dict:
    """Parse subsections with ### headers into a dict."""
    subsections = {}
    current_key = None
    current_content = []
    
    for line in section_text.split("\n"):
        if line.startswith("### "):
            if current_key:
                subsections[current_key] = "\n".join(current_content).strip()
            current_key = line[4:].strip()
            current_content = []
        elif current_key:
            current_content.append(line)
    
    if current_key:
        subsections[current_key] = "\n".join(current_content).strip()
    
    return subsections


def parse_bullet_list(text: str) -> list:
    """Extract bullet points from text."""
    items = re.findall(r"^[-*]\s+(.+)$", text, re.MULTILINE)
    return [item.strip() for item in items]


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
        "theme": "",
        "tldr": "",
        "sections_summary": {},  # Resumo por Secções
        "insights": [],
        "actions": {
            "immediate": [],
            "week": [],
            "longterm": []
        },
        "context_application": {},  # Aplicação ao Contexto
        "frameworks": [],  # Frameworks & Modelos Mentais
        "stories": [],  # Histórias & Exemplos
        "resources": [],  # Recursos Mencionados
        "reflection_questions": [],  # Perguntas para Reflexão
        "quotes": [],
        "rating": 0,
        "rating_breakdown": {},  # Rating detalhado
        "tags": [],
        "verdict": ""
    }
    
    # Extract date from filename
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
        elif "tema" in key or "theme" in key:
            digest["theme"] = value
    
    # Extract TL;DR
    tldr_match = re.search(r"## 🎯 TL;DR.*?\n\n(.+?)(?=\n\n---|\n\n##)", content, re.DOTALL)
    if tldr_match:
        digest["tldr"] = tldr_match.group(1).strip()
    
    # Extract Resumo por Secções
    sections_text = extract_section(content, r"## 📚 Resumo por Secções")
    if sections_text:
        digest["sections_summary"] = parse_subsections(sections_text)
    
    # Extract Top 10 Insights
    insights_section = re.search(r"## 💡 Top 10 Insights.*?\n\n(.*?)(?=\n---|\n## )", content, re.DOTALL)
    if insights_section:
        rows = re.findall(r"\|\s*\d+\s*\|\s*\*\*([^*]+)\*\*\s*\|\s*([^|]+)\s*\|", insights_section.group(1))
        digest["insights"] = [{"insight": r[0].strip(), "why": r[1].strip()} for r in rows]
    
    # Extract Actions
    actions_section = re.search(r"## 🛠️ Acções Práticas.*?\n\n(.*?)(?=\n---|\n## )", content, re.DOTALL)
    if actions_section:
        action_text = actions_section.group(1)
        
        immediate = re.findall(r"- \[ \] (.+)", action_text.split("### Esta Semana")[0] if "### Esta Semana" in action_text else action_text)
        digest["actions"]["immediate"] = immediate[:5]
        
        if "### Esta Semana" in action_text:
            week_section = action_text.split("### Esta Semana")[1].split("### Longo Prazo")[0] if "### Longo Prazo" in action_text else action_text.split("### Esta Semana")[1]
            week = re.findall(r"- \[ \] (.+)", week_section)
            digest["actions"]["week"] = week[:5]
        
        if "### Longo Prazo" in action_text:
            longterm_section = action_text.split("### Longo Prazo")[1]
            longterm = re.findall(r"- \[ \] (.+)", longterm_section)
            digest["actions"]["longterm"] = longterm[:5]
    
    # Extract Aplicação ao Contexto
    context_text = extract_section(content, r"## 🎯 Aplicação ao Contexto")
    if context_text:
        digest["context_application"] = parse_subsections(context_text)
    
    # Extract Frameworks & Modelos Mentais
    frameworks_text = extract_section(content, r"## 🧠 Frameworks")
    if frameworks_text:
        frameworks = parse_subsections(frameworks_text)
        digest["frameworks"] = [{"name": k, "content": v} for k, v in frameworks.items()]
    
    # Extract Histórias & Exemplos
    stories_text = extract_section(content, r"## 📖 Histórias")
    if stories_text:
        stories = parse_subsections(stories_text)
        digest["stories"] = [{"title": k, "content": v} for k, v in stories.items()]
    
    # Extract Recursos Mencionados
    resources_text = extract_section(content, r"## 🔗 Recursos")
    if resources_text:
        resources = re.findall(r"[-*]\s+\*\*([^*]+)\*\*[:\s]+(.+)", resources_text)
        if resources:
            digest["resources"] = [{"type": r[0].strip(), "description": r[1].strip()} for r in resources]
        else:
            # Fallback: simple bullet list
            digest["resources"] = [{"type": "item", "description": r} for r in parse_bullet_list(resources_text)]
    
    # Extract Perguntas para Reflexão
    questions_text = extract_section(content, r"## ❓ Perguntas")
    if questions_text:
        questions = re.findall(r"\d+\.\s+(.+)", questions_text)
        digest["reflection_questions"] = questions
    
    # Extract Quotes
    quotes_section = re.search(r"## 💬 Quotes.*?\n\n(.*?)(?=\n---|\n## )", content, re.DOTALL)
    if quotes_section:
        quotes = re.findall(r"> \"(.+?)\"", quotes_section.group(1))
        digest["quotes"] = quotes[:8]
    
    # Extract Rating breakdown
    rating_section = re.search(r"## 📊 Rating.*?\n\n(.*?)(?=\n\n\*\*Veredicto|\Z)", content, re.DOTALL)
    if rating_section:
        ratings = re.findall(r"\|\s*([^|]+)\s*\|\s*(⭐+)\s*\|", rating_section.group(1))
        digest["rating_breakdown"] = {r[0].strip(): r[1].count("⭐") for r in ratings}
        # Calculate average
        if digest["rating_breakdown"]:
            digest["rating"] = round(sum(digest["rating_breakdown"].values()) / len(digest["rating_breakdown"]), 1)
    
    # Extract Verdict
    verdict_match = re.search(r"\*\*Veredicto:\*\*\s*(.+?)(?=\n|$)", content)
    if verdict_match:
        digest["verdict"] = verdict_match.group(1).strip()
    
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
