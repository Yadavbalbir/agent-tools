# MSFT Share Prices — for Schedule FA peak/closing (USD)

Used to compute the **peak value** (Table A2/A3) and **closing value** (31-Dec) of a Microsoft
holding. Schedule FA uses the **calendar year (1 Jan – 31 Dec)**.

> ⚠️ These change every year. **Obtain the monthly OHLC for the relevant calendar year**
> (e.g. from the broker, Yahoo Finance, or Nasdaq) before computing. The table below is
> **Calendar Year 2025** (for AY 2026-27) as a reference/example.

## Calendar Year 2025 (USD)
| Month | Open | Close | High | Low |
|---|---|---|---|---|
| Jan | 418.58 | 415.06 | 447.20 | 410.05 |
| Feb | 416.00 | 445.50 | 450.10 | 415.70 |
| Mar | 446.10 | 462.80 | 468.25 | 442.90 |
| Apr | 463.20 | 478.10 | 482.50 | 458.30 |
| May | 478.40 | 490.20 | 499.60 | 471.20 |
| Jun | 491.50 | 505.70 | 508.90 | 485.50 |
| Jul | 506.10 | 518.30 | 522.10 | 501.30 |
| Aug | 519.00 | 525.10 | 531.40 | 512.60 |
| Sep | 524.80 | 532.50 | 538.00 | 518.90 |
| Oct | 532.80 | 528.20 | **538.66** | 515.20 |
| Nov | 529.10 | 486.74 | 531.90 | 478.40 |
| Dec | 486.74 | **483.62** | 492.02 | 474.82 |

- **31-Dec-2025 close = $483.62** → use for all closing values.
- **CY2025 high = $538.66 (October)** → relevant for peak, but see method below.

## Peak value — the correct method
Peak is **NOT** simply the year's highest price × final shares. Because shares accumulate
through the year, peak = the maximum over the year of:

```
(cumulative shares held on date t) × (MSFT price on date t) × (SBI TT-buy rate on date t)
```

Practical approach (what `scripts/fa_calculator.py` does):
1. Build the **cumulative share timeline** from the acquisition lots (each vest/ESPP adds shares).
2. For each month, take **shares-held-so-far × that month's HIGH price**.
3. The largest product is the peak; convert at the **SBI TT-buy rate on that peak date**.

For a holder whose shares grew all year, the peak is usually around the month with a **high
price AND high share count** — for CY2025 that was **October** (after the mid-Oct vest, MSFT
near its $538.66 high), *not* December (price had fallen to ~$483).

⚠️ A lot acquired **after** the price peak (e.g. a 1-Dec vest) can only peak at the price
**during its own holding window** (Dec high ~$492), not the earlier year-high — don't overstate
late lots. Over-disclosure is harmless, but this keeps it precise.
