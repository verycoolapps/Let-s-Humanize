# Let's Humanize

**A craft system for AI agents that makes work feel considered, specific, credible, and unmistakably human — not generic, not templated, not "AI-sounding."**

## What It Does

Let's Humanize is a quality framework that forces AI output through the lens of an experienced practitioner. It doesn't just polish surface text — it diagnoses structural problems, grounds claims in real evidence, respects real constraints, and preserves the user's voice and intent.

## Why It Exists

Most "humanize" tools are synonym-swappers or detector-evasion tricks. This is different:
- **Fix the thinking, not just the words** — broken arguments can't be rescued by better vocabulary
- **Preserve truth, don't fabricate it** — never invent evidence, credentials, or lived experience
- **Work across disciplines** — focused playbooks for writing, design, code, research, and strategy
- **Protect authorship** — never impersonate, never claim detector scores, never hide provenance

## Package Contents

```
lets-humanize/
├── SKILL.md                           # Core operating system + quality gates
├── README.md                          # This file
├── SOURCE-NOTES.md                    # Provenance and licensing
├── LICENSE-NOTES.md                   # License status
├── references/
│   ├── writing.md                     # Prose, copy, editorial playbook
│   ├── design.md                      # Visual and product design playbook
│   ├── coding.md                      # Software craft playbook
│   ├── research-and-strategy.md       # Evidence and recommendation playbook
│   └── anti-patterns.md              # Recognizable generic patterns + repairs
├── templates/
│   ├── humanization-brief.md          # Compact preflight template
│   └── editorial-review.md           # Reusable review rubric
├── evals/
│   └── evals.json                     # 6 behavioral regression cases
└── scripts/
    └── validate_package.py            # Deterministic package validator (stdlib only)
```

## Install

Copy `lets-humanize/` into your agent's supported skills directory. For Hermes Agent, a common location is `~/.hermes/skills/creative/lets-humanize/`. For other runtimes, consult their skill/plugin documentation. Package creation does not install or activate the skill automatically.

## Validate

From the skill directory:

```bash
python3 scripts/validate_package.py
```

No third-party dependencies. Validator reports errors and warnings separately; returns non-zero if any issue is found.

## Ethical Boundaries

This skill improves quality. It does NOT:
- Optimize text to evade AI detectors
- Fabricate human drafting histories
- Impersonate real people without authorization
- Certify factual accuracy without verification
- Guarantee audience response or "virality"

## License

See `LICENSE-NOTES.md`. The reviewed upstream repository did not declare a license. No upstream code or substantive prose is redistributed in this package.