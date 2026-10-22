# Output specification

The layout is fixed. The front block is machine-readable so the checker and any script can read a verdict without parsing prose. Section numbers, order and heading text never change.

## 1. Front block

Every verdict file starts with:

```
---
tayyib: 1
name: <product, ticker or employer and role>
type: stock | fund | cash | wrapper | employer | other
screened: YYYY-MM-DD
verdict: CLEAN | BORDERLINE | FAIL
sources_read: <N>
sources_agree: yes | no | unverified
rescreen: YYYY-MM-DD or a trigger in a few words
---
```

Then the title line and the header:

```
# <Name>: Tayyib verdict

Screened on <D Month YYYY>. Standard: AAOIFI core-business test, then the three ratios; two independent sources must agree. Sample verdict lines are marked as such.
Verdict: ✅ CLEAN | 🟡 BORDERLINE | ❌ FAIL
```

## 2. Sections, in order

| # | Heading | Content |
|---|---|---|
| 1 | The verdict in one paragraph | The verdict, the deciding fact, and what would change it |
| 2 | Core business | Pass or fail with the business lines and the non-compliant share of revenue, cited |
| 3 | Ratios | Table: `Ratio | Value | Threshold | Basis | Source | Mark`; "Not applicable" for cash and employer with one line why |
| 4 | Sources and agreement | Table: `Source | Verdict | Date read | Readable | Mark`; then one line: agree, split, or unverified |
| 5 | Reasoning | Why the verdict; for BORDERLINE the exact concern and what resolves it |
| 6 | Purification | The figure or formula with arithmetic; "Not applicable" with the reason for cash and employer |
| 7 | Re-screen | Date or trigger, and why that one |
| 8 | Sources | Footnotes `[^1]`, `[^2]`... each `[^n]: <what, date> <url>` |

## 3. Marks and citations

- Every fact sentence ends with ✅ (read from a source and linked or footnoted), 🟡 (inferred, or from a page that could not be opened) or ❔ (not found after looking).
- Every ✅ is followed on the same line by a footnote `[^n]` or an inline link. Every number carries one.
- A screener verdict is quoted as the screener states it, with the date read.
- Dates `D Month YYYY` in prose, `YYYY-MM-DD` in tables and the front block.

## 4. Batch

For a list, one file per name, or one block per name separated by a horizontal rule, in the order given, each with its own front block. The checker accepts a file with several front blocks.

## 5. Quality bar

- All eight sections present in order with the exact headings.
- The front block verdict matches the verdict line in the header and the verdict in section 1.
- `sources_read` equals the number of rows in section 4 marked readable; `sources_agree: yes` only when at least two readable rows agree with the verdict.
- A CLEAN verdict has `sources_agree: yes`; otherwise the checker fails it.
- Every footnote defined is used and every used footnote is defined.
- Section 6 shows arithmetic or cites a published purification figure for any CLEAN or BORDERLINE stock or fund.
