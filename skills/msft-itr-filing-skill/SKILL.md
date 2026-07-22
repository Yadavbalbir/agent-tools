---
name: msft-itr-filing
description: "Use when helping a salaried Microsoft India employee file their Indian Income Tax Return (ITR) that involves Microsoft RSUs/ESPP held via Fidelity (foreign shares), foreign dividends, Indian broker capital gains, and the new tax regime. Covers document collection, AIS/TIS/26AS reconciliation, tax computation, Form 67 (foreign tax credit), Schedule FA, and step-by-step ITR-2/ITR-3 portal filing. Triggers: 'file ITR', 'Form 16', 'RSU ESPP tax', 'Schedule FA', 'Form 67', 'foreign tax credit', 'Fidelity 1042-S', 'AIS reconciliation'."
---

# Microsoft India ITR Filing Workflow

A repeatable, document-driven workflow to prepare and validate an Indian ITR for a **salaried Microsoft India employee** who holds **Microsoft RSUs/ESPP via Fidelity** and may trade on Indian brokers.

> **Golden rules**
> 1. Never invent a value — ask for the document. The only estimate allowed is FX conversion; flag it and use the exact SBI TT-buying rate before final filing.
> 2. You prepare and validate; the user logs in and submits. Never handle passwords/OTPs.
> 3. Schedule FA + Form 67 are mandatory when foreign shares are held.
> 4. Confirm the AY and its slab/limit rules every year — they change.
> 5. Show the formula and inputs for every number.

---

## Step 0 — Kick off

Confirm before anything else:
- **Financial Year / Assessment Year** (e.g. FY 2025-26 → AY 2026-27).
- **Regime**: Old vs New (Microsoft Form 16 shows *"Opting out of 115BAC = No"* → New regime).
- **Income sources**: salary, Indian broker trades (delivery / intraday / F&O), RSU/ESPP, foreign dividends, bank interest, rental, crypto.
- Whether the user has **last year's ITR** (for a year-over-year baseline).

Then present the **Document Checklist** below and collect files into the workspace.

---

## Step 1 — Document Checklist

### A. Salary (Microsoft)
- Form 16 **Part A** and **Part B**
- **Form 12BA** (perquisites breakup — RSU vest + ESPP discount)
- Payslips (Apr–Mar), especially March (cross-check YTD)

### B. Indian broker capital gains (Groww / Zerodha / etc.)
- **Tax P&L / Capital Gains statement** (stocks + mutual funds) for the FY
- Confirm segments traded: **delivery (STCG/LTCG), intraday (speculative), F&O** → this decides the ITR form
- F&O / intraday: contract notes / ledger for turnover

### C. Foreign shares — Microsoft RSU/ESPP (Fidelity)
- **Fidelity Year-End Investment Report** (1 Jan–31 Dec — calendar year, for Schedule FA)
- **Form 1042-S** (US tax withheld on dividends — for Form 67 / FTC)
- Holdings on **31 Dec**, peak value, cost basis, RSU vest dates + ESPP purchase dates
- First acquisition date (earliest vest) — needed for Schedule FA

### D. Other income
- **Bank interest certificates** (savings + FD) — all banks
- **Dividend statements** — Indian shares
- Rental income (if any)

### E. Validation (download from portal)
- **AIS** (Annual Information Statement) + **TIS** + **Form 26AS** for the AY

### F. Not needed in New Regime
- 80C / 80D / HRA / LTA / 80TTA proofs (disallowed). Exception: **80CCD(2)** employer NPS, if the CTC includes it (Microsoft usually contributes to PF, not NPS).

### Common PDF passwords
- **Form 16 (TRACES / employer)**: often the **full PAN** (e.g. `ABCDE1234F`); sometimes PAN(5) + DOB(DDMMYYYY).
- **AIS / TIS**: PAN in **lowercase** + DOB(DDMMYYYY), e.g. `abcde1234f01012000`.
- **Form 26AS / intimation**: DOB(DDMMYYYY).

Use `scripts/extract_pdf.py` to read PDFs (handles encryption with candidate passwords). See `references/document-checklist.md` for a printable list.

---

## Step 2 — Read & reconcile

1. Extract every PDF/CSV with the helper script.
2. Build the income picture per head.
3. **Reconcile against AIS/TIS/26AS** and flag every mismatch:
   - Extra **savings accounts** the user forgot (AIS lists all)
   - Dividends from shares held but not traded
   - **Sale of securities** value must match the broker capital-gains statement
   - Salary + TDS must match Form 16 and 26AS exactly
   - No VDA (crypto) rows unless the user traded crypto
4. Foreign items (MSFT dividend, holdings) are **not** in AIS — capture them separately.

---

## Step 3 — Determine ITR form & regime

| Situation | Form |
|---|---|
| Salary + capital gains + foreign assets, **no business income** | **ITR-2** |
| **Any intraday (speculative) or F&O** trading | **ITR-3** |

- Intraday = speculative **business** income → forces ITR-3.
- F&O = non-speculative business income → forces ITR-3.
- Delivery-only equity = capital gains → ITR-2 is fine.
- Regime: New is usually better for Microsoft employees (few/no deductions). No Form 10-IEA needed to stay in New.

See `references/tax-rules.md` for the detailed rate rules and confirm them for the filing AY.

---

## Step 4 — Compute (show all math)

- **Salary**: Gross 17(1) + perquisites 17(2) − standard deduction = income under Salaries.
- **Capital gains**: STCG u/s 111A at the AY's rate (20% for sales on/after 23-Jul-2024; 15% before). LTCG u/s 112A as applicable.
- **Other sources**: savings interest + Indian dividend + **foreign dividend** + **interest on income-tax refund (Sec 244A) is taxable** in the year received.
- **Foreign dividend & FTC**: convert each dividend/withholding at the **SBI TT-buying rate** on the last day of the month **before** receipt (Rule 115 / Rule 128). FTC = **lower of** foreign tax paid vs Indian tax on that income.
- **Deductions**: New regime → Chapter VI-A generally 0 (80TTA, 80C, 80D, 80G all disallowed).
- **Tax**: apply the AY slabs, cess 4%, surcharge if applicable; subtract FTC and TDS to get **balance payable**.
- **234B/234C**: no advance-tax interest if the assessed shortfall is below ₹10,000.

---

## Step 5 — File on the portal (order matters)

1. **Form 67 FIRST** (before the ITR): foreign income, foreign tax paid, Indian tax on it, FTC (lower of), DTAA article (dividends = **Article 10**, rate 25% for India–US), Section **90**. Attach Form 1042-S + Fidelity statement. Bulk-upload CSV template: fill the effective foreign-tax rate so `amount = income × rate` reconciles. e-Verify and note the acknowledgement.
2. **ITR schedules** (select CG, OS, FSI, TR, FA in addition to the mandatory ones):
   - **Schedule S** (Salary) — set *Nature of employer = Others*; give a description for any "Any Other" perquisite; delete an empty 17(3) row.
   - **Schedule CG** — STCG 111A: consideration, cost, gain; fill the **quarterly accrual (section F)** by sell date.
   - **Schedule OS** — dividends (incl. foreign) in field 1ai; savings + refund interest under interest.
   - **Schedule FSI + TR** — must tie exactly to Form 67 (income, tax, FTC, Article, TIN=PAN if no foreign TIN).
   - **Schedule FA (Table A3 — Foreign Equity & Debt Interest)** — Microsoft Corporation, USA (code 2); acquisition date = first vest; initial (cost), peak, and closing values converted at the **31-Dec SBI TT-buying rate**; dividend during the **calendar year**; sale proceeds 0 if not sold.
   - **Part B-TTI** — answer the foreign-asset question **YES**.
3. **Pay self-assessment tax** (challan minor head **300**, correct AY) **before** submitting; enter it in **Schedule IT**; verify balance = ₹0.
4. **Validate → Preview → Submit → e-Verify** within 30 days.

See `references/portal-field-map.md` for the schedule-by-schedule field mapping.

---

## Step 6 — Validate the final JSON

Before upload, extract the ITR JSON and confirm:
- Salary, CG, OS totals match the computation
- FSI = TR = Form 67 (same FTC amount)
- `AssetOutIndiaFlag = YES`; Schedule FA A3 populated
- Schedule IT has the self-assessment challan; **balance payable = 0**

---

## Step 7 — Post-filing gotchas

- If the user paid the balance **after** filing (chose "Pay Later"), the return shows a **demand**. The challan (correct AY + head 300) is usually auto-credited at CPC processing, but the clean fix is a **Revised Return u/s 139(5)** adding the challan in Schedule IT.
- A revised return needs the **original acknowledgement number + filing date**. Use the portal's **"File Revised Return"** button to pre-fill original data; a fresh "File Income Tax Return" flow starts blank.

---

## Session hygiene
- Track collected vs pending documents and every computed figure in session memory, so a resumed session picks up cleanly.
- Re-state the AY and regime whenever you compute tax.
