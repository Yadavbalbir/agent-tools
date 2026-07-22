# Tax Rules — verify every Assessment Year

> ⚠️ Rates, slabs, surcharge, cess, and limits change annually. Confirm each against the
> official return/utility for the filing AY before computing. The values below are a
> starting reference for **AY 2026-27 (FY 2025-26), New Regime** and must be re-verified.

## New Regime slabs — AY 2026-27 (verify)
| Slab (₹) | Rate |
|---|---|
| 0 – 4,00,000 | Nil |
| 4,00,001 – 8,00,000 | 5% |
| 8,00,001 – 12,00,000 | 10% |
| 12,00,001 – 16,00,000 | 15% |
| 16,00,001 – 20,00,000 | 20% |
| 20,00,001 – 24,00,000 | 25% |
| Above 24,00,000 | 30% |

- Standard deduction (salary): ₹75,000.
- Health & Education Cess: 4% on (tax + surcharge).
- Surcharge: applies above ₹50L (verify thresholds/rates; new-regime cap 25%).
- Rebate 87A: income up to ₹12,00,000 in New Regime (not available on special-rate income like STCG 111A).
- Sanity check: tax on a salary-only Total Income should exactly match the Form 16 computation — use it to confirm the slabs.

## Capital gains
- **STCG u/s 111A** (listed equity / equity MF, STT paid): **20%** for transfers on/after 23-Jul-2024; **15%** before. Verify the AY.
- **LTCG u/s 112A** (equity): 12.5% beyond the exempt threshold (verify threshold), for transfers on/after 23-Jul-2024.
- STCG/LTCG special rates are **not** eligible for 87A rebate.

## Chapter VI-A in New Regime
- Generally **nil**: 80C, 80CCD(1B), 80D, 80G, 80TTA/80TTB, HRA, LTA all disallowed.
- Allowed: **80CCD(2)** (employer NPS), 80CCH (Agnipath) — only if applicable.

## Foreign dividend + Foreign Tax Credit
- Foreign dividend is taxable under **Other Sources** at slab rate (resident = global income).
- Convert income and foreign tax at the **SBI TT-buying rate** on the **last day of the month before** the receipt/withholding (Rule 115 / Rule 128).
- **FTC = lower of** (foreign tax paid) vs (Indian tax on that income = income × marginal rate incl. cess).
- India–US dividends: DTAA **Article 10**, treaty rate 25%. Relief under **Section 90**.
- **Form 67 must be filed before the ITR.**
- Effective foreign-tax rate = foreign tax ÷ foreign income (may be slightly under 25% due to per-lot rounding). Use it where the form validates `amount = income × rate`.

## Schedule FA (foreign assets)
- Reporting period = **calendar year (1 Jan–31 Dec)**, not the financial year.
- Convert initial/peak/closing values at the SBI TT-buying rate on the relevant date (closing → 31 Dec).
- Report even if nothing is sold. Disclosure-only — no tax impact — but mandatory (Black Money Act).
- RSU/ESPP shares → **Table A3 (Foreign Equity & Debt Interest)**.

## Other
- **Interest on income-tax refund (Sec 244A)** received during the FY is taxable under Other Sources (the refund principal is not).
- **234B/234C**: no advance-tax interest if assessed shortfall (tax − TDS − FTC) is below ₹10,000.
- Refund principal is never taxable; only its 244A interest is.

## FX rate source
- Use the **SBI TT-buying ("TT Buy") rate** — not TT Sell or Bill rates.
- If a date is a holiday/weekend, use the previous working day's rate.
