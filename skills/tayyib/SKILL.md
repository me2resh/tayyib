---
name: tayyib
description: Halal screening as a hard gate for any financial product or employer, to the AAOIFI standard, with one verdict (CLEAN, BORDERLINE or FAIL), the ratios, two independent sources that must agree, the purification amount and a re-screen date. Use it before recommending, buying, holding or taking any stock, ETF or fund, savings or cash product, ISA or pension holding, or a job or client. Trigger on "is X halal", "halal stock", "shariah compliant", "can I invest in", "is this fund ok", "purification", "AAOIFI", "riba", "halal job", "should I take this role", and on any request to recommend a financial product or employer even when halal is not mentioned, because the gate runs first.
tools: Read, Grep, Glob, Bash, WebSearch, WebFetch
keywords: [halal, shariah, AAOIFI, screening, stocks, ETF, funds, savings, riba, purification, employer, job, Islamic finance]
---

# Tayyib

A hard halal gate for everything money touches: stocks, funds, cash products, the holdings inside an ISA or pension, and employers or clients. One verdict, the ratios behind it, two sources that agree, the purification owed, and the date to check again. The name means more than permitted: pure and wholesome, which is the bar a BORDERLINE verdict exists to protect.

## The idea in one paragraph

Most mistakes in halal investing are not about hard cases. They are a bond fund inside a tax wrapper nobody screened, a savings account chosen for its rate, a clean company whose job is in its defence unit, or a single screener's green tick taken on trust. Tayyib runs the same procedure every time, in the same order, and writes the same document: the core-business test first, then the three AAOIFI ratios, then two independent screeners that must agree, then the verdict, the purification and the re-screen date. A missing source makes the verdict BORDERLINE, never CLEAN. Nothing is softened because the return, the salary or the convenience is good.

## Rules

- **The gate is hard.** Pay, equity, yield, convenience or urgency never move a verdict. The screen gives evidence; the person decides; the screen never softens a FAIL.
- **Core business first.** A failed core-business test is a FAIL regardless of ratios. The test applies to the company and, for a job, to the specific unit and role.
- **Two sources must agree.** A single screener's verdict is never CLEAN on its own. A split verdict is BORDERLINE at best, with the failing ratio named. An unreadable or login-walled page is "unverified", and a search snippet is not a source.
- **BORDERLINE means BORDERLINE.** It is never "mostly clean". The verdict says the exact concern and what would resolve it.
- **Ratings drift.** Ratios move with price and with each quarterly filing. Every verdict carries a re-screen date or trigger, and a verdict older than its re-screen date is not a verdict.
- **Fail safe.** When sources cannot be read, when the product cannot be classified, or when the methodology of a fund is not stated, the answer is BORDERLINE with the reason, not CLEAN with a caveat.
- **Privacy.** Never record a person's holdings, balances or employer in the skill's own files; a verdict is about the product, not the person.

## Step 0: classify

Decide the product type before anything else, because the screen differs: `stock`, `fund` (ETF, index fund, active fund, multi-asset), `cash` (savings, current account, bonds, premium bonds, money market), `wrapper` (ISA, pension, platform: neutral in itself, screen the holdings), `employer` (company, client, role, unit), `other`. State the type in the front block. A request to recommend anything financial runs the gate first on every candidate.

## Step 1: run the standard

`references/standard.md` is the gate: the core-business exclusions, the three ratios and their thresholds, the per-type screens, and the purification method. Read it before every screen; do not work from memory, because the thresholds and the exclusions are the whole point.

## Step 2: verify from sources

`references/sources.md` names the primary screeners, the tiebreaker, the filings and factsheets to read for ratios, and the exact procedure for fetching and recording each one. Fetch the screener pages directly; record the date read and whether the page was readable. Two independent sources must agree for CLEAN.

## Step 3: write the verdict, to the fixed layout

`references/outputs.md` is the specification: a machine-readable front block, a fixed header, numbered sections in a fixed order with fixed names, fixed table columns, and a sources section the verdict can be rebuilt from. Run `python3 scripts/check_verdict.py <file.md>` before finishing and fix every failure. For a batch, one file or one block per name, in the order given, each passing the checker.

## After a FAIL

Tell the caller to add the name to whatever exclusion list they keep, to note the purification owed on anything held so far, and, for a held position, that the question of whether to sell is theirs and is answered by the standard's guidance on holding non-compliant stock, which the verdict quotes.
