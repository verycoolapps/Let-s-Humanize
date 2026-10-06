#!/usr/bin/env python3
"""Validate structure and basic hygiene of the Let's Humanize skill package."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = (
    "SKILL.md",
    "README.md",
    "SOURCE-NOTES.md",
    "LICENSE-NOTES.md",
    "references/writing.md",
    "references/design.md",
    "references/coding.md",
    "references/research-and-strategy.md",
    "references/anti-patterns.md",
    "templates/humanization-brief.md",
    "templates/editorial-review.md",
    "evals/evals.json",
)
REQUIRED_SECTIONS = (
    "## Mission",
    "## When to Use",
    "## Non-Negotiable Boundaries",
    "## The Operating Method",
    "## Domain Playbooks",
    "## Verification Checklist",
    "## Common Failure Modes",
)
HYGIENE_SKIP = {"scripts/validate_package.py"}


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def strip_code_fences(text: str) -> str:
    return re.sub(r"```.*?```", "", text, flags=re.DOTALL)


def frontmatter(content: str, errors: list[str]) -> tuple[str, str]:
    if not content.startswith("---\n"):
        fail("SKILL.md must start with a YAML frontmatter delimiter at byte 0", errors)
        return "", ""
    parts = content[4:].split("\n---\n", 1)
    if len(parts) != 2:
        fail("SKILL.md is missing the closing frontmatter delimiter", errors)
        return "", ""
    return parts[0], parts[1]


def scalar(fm: str, key: str) -> str:
    match = re.search(rf"^{re.escape(key)}:\s*(.*?)\s*$", fm, re.MULTILINE)
    if not match:
        return ""
    value = match.group(1)
    if value in (">", ">-", "|", "|-"):
        block = re.search(rf"^{re.escape(key)}:\s*[|>]\-?\s*\n((?:[ \t]+.*(?:\n|$))*)", fm, re.MULTILINE)
        return " ".join(line.strip() for line in block.group(1).splitlines()) if block else ""
    return value.strip("\"'")


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    skill_path = ROOT / "SKILL.md"
    if not skill_path.is_file():
        print(f"ERROR: missing {skill_path}")
        return 1

    content = skill_path.read_text(encoding="utf-8")
    fm, body = frontmatter(content, errors)
    name = scalar(fm, "name")
    description = scalar(fm, "description")
    if not name:
        fail("frontmatter name is missing", errors)
    elif len(name) > 64 or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        fail("frontmatter name must be lowercase kebab-case and at most 64 characters", errors)
    elif ROOT.name != name:
        fail(f"directory name {ROOT.name!r} does not match frontmatter name {name!r}", errors)
    if not description:
        fail("frontmatter description is missing or empty", errors)
    elif len(description) > 1024:
        fail(f"description is {len(description)} characters; maximum is 1024", errors)
    elif not description.startswith("Use when "):
        fail("description must begin with 'Use when '", errors)
    for key in ("version", "author", "license"):
        if not scalar(fm, key):
            fail(f"frontmatter {key} is missing", errors)
    if "metadata:" not in fm or "tags:" not in fm or "related_skills:" not in fm:
        fail("frontmatter must include metadata.hermes tags and related_skills", errors)

    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            fail(f"missing required file: {relative}", errors)

    clean_body = strip_code_fences(body)
    for heading in REQUIRED_SECTIONS:
        if heading not in clean_body:
            fail(f"missing required section: {heading}", errors)
    if len(content) > 100_000:
        fail("SKILL.md exceeds 100,000 characters", errors)

    eval_path = ROOT / "evals/evals.json"
    if eval_path.is_file():
        try:
            evaluation = json.loads(eval_path.read_text(encoding="utf-8"))
            if not isinstance(evaluation.get("cases"), list) or not evaluation["cases"]:
                fail("evals/evals.json must contain a non-empty cases array", errors)
            else:
                ids = [case.get("id") for case in evaluation["cases"]]
                if any(not item for item in ids) or len(set(ids)) != len(ids):
                    fail("evaluation case IDs must be present and unique", errors)
                for case in evaluation["cases"]:
                    if not isinstance(case.get("expect"), list) or not case["expect"]:
                        fail(f"evaluation {case.get('id', '<unnamed>')} needs expected behaviors", errors)
        except (json.JSONDecodeError, OSError) as exc:
            fail(f"invalid evals/evals.json: {exc}", errors)

    forbidden = ("/home/ubuntu/", "/Users/adhithyasoemitro/", "ghp_")
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(ROOT).as_posix()
        if relative in HYGIENE_SKIP or "__pycache__" in path.parts or path.suffix == ".pyc":
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            warnings.append(f"skipped non-text file: {relative}")
            continue
        for marker in forbidden:
            if marker in text:
                fail(f"sensitive or machine-specific string {marker!r} found in {relative}", errors)
        if re.search(r"(?m)^\s*(?:TODO|FIXME):", text):
            fail(f"unfinished TODO/FIXME marker in {relative}", errors)

    print(f"Package: {ROOT.name}")
    print(f"Required files: {len(REQUIRED_FILES)}")
    print(f"Evaluation cases: {len(json.loads(eval_path.read_text(encoding='utf-8')).get('cases', [])) if eval_path.is_file() else 0}")
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")
    for item in errors:
        print(f"ERROR: {item}")
    for item in warnings:
        print(f"WARNING: {item}")
    if not errors and not warnings:
        print("PASS: zero errors and zero warnings")
    return 1 if errors or warnings else 0


if __name__ == "__main__":
    sys.exit(main())
