# Let's Humanize

**A craft system for work that feels considered, specific, and trustworthy.**

Let's Humanize helps an agent improve writing, code, research, strategy, and design by fixing the thinking before polishing the surface. It is built for real readers and real constraints—not for detector games, synthetic quirks, or generic “professional” filler.

## Why this skill is different

- **Diagnose, then edit.** Find the structural, evidential, or usability problem before touching the wording.
- **Specific without fabrication.** Ground details in the user's context and sources; narrow claims when evidence is missing.
- **Works across disciplines.** Focused playbooks cover writing, design, software, research, and strategy.
- **Protects voice and provenance.** Preserve intent and authorship; never promise detector evasion or impersonate someone deceptively.
- **Verifiable by design.** Practical checklists and regression examples make the quality bar reusable.

## Install

Copy the `lets-humanize/` directory into your agent's supported skills directory. For Hermes, a common user-local location is `~/.hermes/skills/creative/lets-humanize/`. Confirm the exact install mechanism for your runtime; package creation does not install or activate the skill automatically.

## Package map

- `SKILL.md` — the core operating system and quality gates.
- `references/` — domain playbooks and anti-pattern repairs.
- `templates/` — reusable briefs and review rubrics.
- `evals/evals.json` — behavior checks for future revisions.
- `scripts/validate_package.py` — offline package validator using Python's standard library.
- `SOURCE-NOTES.md` — snapshot provenance and license cautions.

## Validate

From the skill directory, run:

```bash
python3 scripts/validate_package.py
```

The validator reports errors and warnings separately and returns non-zero if any issue is found. It requires Python 3.9+ and has no third-party dependencies.

## Scope

This package improves the quality of an artifact. It does not certify factual accuracy automatically, replace subject-matter or legal review, guarantee audience response, claim human authorship, or help evade AI-detection systems.

## Language

All authored documentation and prompt guidance in this package are in English. Preserve another language when the user explicitly asks for a multilingual artifact or supplies source material that must remain unchanged.

## Provenance

The source repository and snapshot details are documented in `SOURCE-NOTES.md`. The upstream repository did not declare a license at the reviewed revision; no upstream code, assets, or substantive prose is redistributed here.
