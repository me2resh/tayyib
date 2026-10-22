# Tayyib (طيّب)

**A hard halal gate for everything money touches.** Stocks, funds, cash products, the holdings inside an ISA or pension, and employers or clients. One verdict to the AAOIFI standard, the ratios behind it, two independent sources that must agree, the purification owed, and the date to check again. Arabic by default, English on request.

Site: https://me2resh.github.io/tayyib/

Tayyib is an add-on for Claude Code, Codex and Cursor (and anything else that reads the Agent Skills format, with a rule file for GitHub Copilot). The name means pure and wholesome, the word the Quran pairs with halal; it is the bar a BORDERLINE verdict exists to protect.

## What it does

1. **Classifies** the product: stock, fund, cash, wrapper, employer.
2. **Core-business test first.** Banking, insurance, gambling, alcohol, defence and the rest; a fail here is a FAIL whatever the ratios. For a job, the unit and the work, not just the group.
3. **Three ratios** on the AAOIFI thresholds: non-compliant income below 5% of revenue, debt below 33% of market capitalisation, cash and interest-bearing securities below 33%.
4. **Two sources must agree.** Screener pages fetched and dated; a split is BORDERLINE at best; a page that cannot be read is "unverified" and does not count.
5. **One verdict** in a fixed layout: CLEAN, BORDERLINE or FAIL, with the reasoning, the purification arithmetic and a re-screen date. A checker fails any verdict that drifts from the layout.

## Install

Claude Code, one line:

```
/plugin install tayyib --marketplace me2resh/tayyib
```

Older Claude Code: `/plugin marketplace add me2resh/tayyib`, then `/plugin install tayyib@tayyib`. Shell: `claude plugin install tayyib --marketplace me2resh/tayyib`. The skill answers to `/tayyib`.

Codex and other Agent-Skills agents: clone and run `./install.sh codex` or `./install.sh /path/to/skills`. Cursor: copy `.cursor/rules/tayyib.mdc`. Copilot: copy `.github/copilot-instructions.md`.

Then ask, in Arabic or English: "Is Acme halal?", "Screen this fund before I put it in my ISA", "Can I take this role?", "Purification owed on 500 shares held all year".

## The output is deterministic

Every verdict has a language-neutral front block (type, date, verdict, sources read, agreement, re-screen), a fixed header, eight numbered sections in a fixed order with fixed names in Arabic and in English, fixed table columns, a mark on every fact, and footnoted sources. `skills/tayyib/references/outputs.md` is the specification; `skills/tayyib/scripts/check_verdict.py` enforces it and the skill runs it before finishing. The eight sample verdicts (four in Arabic, four in English) pass it.

## Rules the skill enforces

- The gate is hard: pay, yield, convenience and urgency never move a verdict.
- Core business first, then ratios, then two agreeing sources.
- BORDERLINE means BORDERLINE. Fail safe: unverified means BORDERLINE, never CLEAN.
- Ratings drift: every verdict carries a re-screen date or trigger.
- A verdict is about the product, never about the person's holdings.

## Repository

```
.claude-plugin/                      plugin manifest and marketplace
skills/tayyib/SKILL.md               the skill (Agent Skills format)
skills/tayyib/references/standard.md the gate: exclusions, ratios, per-type screens, purification
skills/tayyib/references/sources.md  screeners, filings, procedure
skills/tayyib/references/outputs.md  the fixed verdict layout, Arabic and English
skills/tayyib/scripts/check_verdict.py
skills/tayyib/examples/ar, en        eight sample verdicts
docs/                                the website and sample PDFs
install.sh
```

## Licence

MIT. Tayyib gives evidence to a standard; it is not a fatwa, and the decision and any question of scholarship are the person's own.
