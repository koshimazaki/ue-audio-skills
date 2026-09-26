"""Copy the skills from a UE-AUDIO-MCP checkout into skills/.

The skills are maintained in UE-AUDIO-MCP (.claude/skills/) in Claude Code's
format. This adapts their frontmatter to the Agent Skills spec:
allowed-tools becomes space-separated, and Claude Code's argument-hint moves
under metadata, since the spec allows no other top-level fields.

Usage: python scripts/sync_from_ue_audio_mcp.py <path-to-UE-AUDIO-MCP>
Then check with: agentskills validate skills/<name>   (pip install skills-ref)
"""
from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path


def adapt_frontmatter(skill_md: Path) -> None:
    text = skill_md.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise SystemExit(f"{skill_md}: no frontmatter")
    _, frontmatter, body = text.split("---", 2)
    lines, hint = [], None
    for line in frontmatter.strip("\n").split("\n"):
        key, _, value = line.partition(":")
        if key == "metadata":
            raise SystemExit(f"{skill_md}: already has metadata, merge argument-hint by hand")
        if key == "allowed-tools":
            line = "allowed-tools: " + " ".join(t for t in re.split(r"[,\s]+", value) if t)
        elif key == "argument-hint":
            hint = value.strip()
            continue
        lines.append(line)
    if hint:
        lines += ["metadata:", f"  argument-hint: {hint}"]
    skill_md.write_text("---\n" + "\n".join(lines) + "\n---" + body, encoding="utf-8")


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    src = Path(sys.argv[1]) / ".claude" / "skills"
    dest = Path(__file__).resolve().parent.parent / "skills"
    skills = sorted(p for p in src.iterdir() if (p / "SKILL.md").is_file()) if src.is_dir() else []
    if not skills:
        raise SystemExit(f"No skills found in {src}")
    for skill in skills:
        target = dest / skill.name
        shutil.rmtree(target, ignore_errors=True)
        shutil.copytree(skill, target, ignore=shutil.ignore_patterns(".DS_Store"))
        adapt_frontmatter(target / "SKILL.md")
        print(f"synced {skill.name}")


if __name__ == "__main__":
    main()
