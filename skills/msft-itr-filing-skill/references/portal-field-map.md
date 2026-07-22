# Portal Field Map — ITR-2 (Microsoft employee, New Regime)

Schedule-by-schedule field mapping. Values are placeholders — fill from the user's reconciled figures.

## Filing Status (Part A-General)
- Filed u/s: **139(1)** (on/before due date) or **139(5)** if revising
- Opting out of new regime 115BAC(6): **No** (stay in New Regime)
- Residential status: **Resident**; condition **182+ days [6(1)(a)]** → ROR
- FPI: **No** · Held unlisted equity shares: **No** (MSFT is listed)
- Reason for filing: **"Taxable income more than basic exemption limit"** (not the Seventh Proviso option)

## Schedule S — Salary
- 17(1) salary; 17(2) perquisites (RSU vest + ESPP + others); 17(3) = 0 (delete empty row)
- Nature of employer: **Others** (private sector)
- Any perquisite typed "Any Other" needs a **Description**; or use "Other benefits or amenities"
- Allowances exempt u/s 10: **0** (New Regime) · Standard deduction 16(ia): **75,000**

## Schedule CG — Capital Gains
- STCG u/s **111A** (equity, STT paid): Full consideration − (cost + improvement + transfer exp) = STCG
- Consideration must match AIS "Sale of securities"
- **Section F (accrual)**: split STCG by **sell date** across the five 234C periods (must total STCG)

## Schedule OS — Other Sources
- **1ai Dividend** = Indian + **foreign (MSFT) dividend** (foreign has no separate box here)
- Interest: savings bank (all accounts) + **income-tax refund (244A)**
- Everything else (56(2)(x), family pension, 89A, machinery rent) = 0
- Dividend quarterly breakup only matters for 234C (nil for small balances)

## Schedule FSI — Foreign Source Income
- Country: **United States (2)** · TIN: **PAN** (if no US TIN)
- Head: **Other Sources** · Income; Tax paid abroad; Tax payable in India; Relief (lower of); DTAA **Article 10**
- Must equal Form 67

## Schedule TR — Tax Relief
- Country **US (2)**; tax paid = relief; Section **90**; DTAA total = relief
- "Foreign tax refunded later?" → **No**
- Total FTC must equal Form 67 and FSI

## Schedule FA — Table A3 (Foreign Equity & Debt Interest)
- Country **US (2)** · Entity **Microsoft Corporation** · Address **One Microsoft Way, Redmond, Washington** · ZIP **98052** · Nature **Listed Company**
- Date of acquiring interest = **first RSU vest date**
- Initial value (cost) / Peak / Closing — converted at SBI TT-buy rate (closing → 31 Dec)
- Gross amount paid = **dividend during the calendar year** · Gross proceeds = **0** if not sold

## Part B-TTI
- Rebate 87A: 0 (income > ₹12L) · Surcharge: 0 (income < ₹50L) · Cess: 4%
- Tax relief (Sec 90) = FTC
- **Foreign-asset question → YES** (ensures Schedule FA is filed)

## Schedule IT — Tax Paid
- Self-assessment challan: BSR code, date, challan serial no., amount (minor head **300**)
- Confirm **Balance payable = ₹0**

## Nil / skip schedules
- HP (no property), VDA (no crypto), 5A (Portuguese), AL (only if income > ₹50L), CFL/BFLA (no losses), AMTC (no AMT), VI-A (nil deductions)

## Validate final JSON
- Salary/CG/OS totals match computation
- FSI = TR = Form 67 (same FTC)
- `AssetOutIndiaFlag = YES`, Schedule FA A3 present
- Schedule IT challan present, balance = 0
