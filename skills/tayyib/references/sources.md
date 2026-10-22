# Sources and procedure

## Primary screeners

| Source | Use | Read | Record |
|---|---|---|---|
| Zoya (zoya.finance) | Stock and ETF verdicts with ratios and purification | Fetch the ticker page directly | Verdict, each ratio, basis, date read, readable or login-walled |
| Musaffa (musaffa.com) | Stock and ETF verdicts with ratios and a compliance score | Fetch the ticker page directly | Same |
| IslamicFinanceGuru (islamicfinanceguru.com) | Tiebreaker for stocks; UK product reviews for cash, ISA and pension | Fetch the review or the screener page | Verdict and date |

Two of the three must be readable and must agree for CLEAN. A page that cannot be fetched, needs a login, or shows no ratio is recorded as "unverified"; it does not count. A search-engine snippet of a screener page is not a source.

## Ratios from the record

When a screener's ratios are missing or stale, compute from the latest annual report or quarterly filing: revenue, interest and other non-compliant income (finance income, interest on deposits, income from excluded activities), total interest-bearing debt, cash and interest-bearing securities, shares outstanding; market capitalisation from the exchange on the date read. Show the arithmetic in the verdict.

## Funds

Read the fund's own documents: the factsheet, the prospectus or key information document, the index methodology, the Shariah board or certificate, the purification policy, the top holdings. A fund whose documents do not name a Shariah methodology cannot be CLEAN.

## Cash products

Read the bank's product page and terms: the basis of return (interest rate, or expected profit rate under a Shariah board), the deposit protection, any prize draw. Islamic banks publish their Shariah board and the product's structure (commodity murabaha, wakala); record which.

## Employers and clients

Read the company's own description of its business lines, its annual report segment note where listed, the unit's page, the job description, and press for the main customers. For a role, the unit and the work matter more than the group.

## Procedure

1. Classify the product type.
2. Core-business test from the company's or product's own documents.
3. Fetch each primary screener; record verdict, ratios, basis, date, readability.
4. If fewer than two readable and agreeing sources, compute the ratios from the record and mark the verdict BORDERLINE unless the computed ratios and one readable screener agree.
5. Purification from the screener or the filing.
6. Re-screen date or trigger.
7. Write to the layout in `outputs.md`; run `scripts/check_verdict.py`.
