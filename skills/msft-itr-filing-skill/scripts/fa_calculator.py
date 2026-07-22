#!/usr/bin/env python3
"""
Schedule FA calculator for Microsoft RSU/ESPP held via Fidelity.

Computes, per acquisition lot (Table A3) and for the whole account (Table A2):
- Initial value  = shares x FMV-at-acquisition x SBI TT-buy rate on the ACQUISITION date
- Closing value  = shares x (31-Dec close price) x SBI TT-buy rate on 31-Dec
- Account PEAK   = max over the calendar year of (cumulative shares held x monthly-high
                   price) x SBI TT-buy rate on that month's peak date

Reporting period = CALENDAR YEAR (1 Jan - 31 Dec) for Schedule FA.

Edit the CONFIG block below for the assessment year you are filing, then run:
    python fa_calculator.py SBI_REFERENCE_RATES_USD.csv

IMPORTANT: report the dividend ONCE (A2 or A3, not both). Sale proceeds = 0 if not sold.
"""
import sys
from datetime import datetime, timedelta

# ----------------------------- CONFIG (edit per year) -----------------------------
YEAR_END = "2025-12-31"
CLOSE_PRICE = 483.62        # MSFT close on YEAR_END (USD)

# Every acquisition lot HELD during the calendar year: (label, acq_date, shares, fmv_usd)
# Include ALL lots from the FIRST acquisition through 31-Dec of this calendar year
# (prior-year lots still held are reported too).
LOTS = [
    # ("30-Sep-2024 ESPP", "2024-09-30", 1.7364, 387.27),
    # ("15-Jul-2025 RSU",  "2025-07-15", 13.0720, 503.02),
]

# MSFT monthly HIGH price + a representative peak date each month (USD) for peak calc.
# (month_label, high_price, high_date)  -- see references/msft-monthly-prices.md
MONTHLY_HIGH = [
    # ("Oct", 538.66, "2025-10-28"),
]
CORE_MMF_CLOSE = 0.0        # core money-market cash on YEAR_END (USD), for A2 closing
# ---------------------------------------------------------------------------------

import csv


def load_rates(path):
    rates = {}
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            try:
                d = datetime.strptime(row["DATE"].split()[0], "%Y-%m-%d").date()
                tt = float(row["TT BUY"])
            except (ValueError, KeyError):
                continue
            if tt > 0:
                rates[d] = tt
    return rates


def rate_on(rates, datestr, max_back=10):
    d = datetime.strptime(datestr, "%Y-%m-%d").date()
    for back in range(max_back + 1):
        dd = d - timedelta(days=back)
        if dd in rates:
            return rates[dd]
    return None


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 1
    rates = load_rates(argv[1])
    close_tt = rate_on(rates, YEAR_END)

    print("=== Table A3 (per lot) ===")
    print(f"{'Lot':20}{'shares':>9}{'init$':>10}{'initRs':>11}{'closeRs':>11}")
    tot_init = tot_close = tot_sh = 0.0
    for label, ad, sh, fmv in LOTS:
        r = rate_on(rates, ad)
        init = sh * fmv * r
        close = sh * CLOSE_PRICE * close_tt
        tot_init += init; tot_close += close; tot_sh += sh
        print(f"{label:20}{sh:9.4f}{sh*fmv:10.2f}{init:11,.0f}{close:11,.0f}")
    print(f"{'TOTAL':20}{tot_sh:9.4f}{'':10}{tot_init:11,.0f}{tot_close:11,.0f}")

    # Peak: cumulative shares up to each month, x monthly high, x rate on peak date
    print("\n=== Account PEAK (A2) ===")
    events = sorted((datetime.strptime(ad, "%Y-%m-%d").date(), sh) for _, ad, sh, _ in LOTS)
    best = None
    for mon, hi, hidate in MONTHLY_HIGH:
        hd = datetime.strptime(hidate, "%Y-%m-%d").date()
        held = sum(sh for d, sh in events if d <= hd)
        val = held * hi * rate_on(rates, hidate)
        if best is None or val > best[1]:
            best = (mon, val, held, hi)
    if best:
        print(f"Peak month {best[0]}: {best[2]:.4f} sh x ${best[3]} -> Rs {best[1]:,.0f}")
    acct_close = (tot_close / (CLOSE_PRICE * close_tt) + CORE_MMF_CLOSE) * CLOSE_PRICE * close_tt \
        if close_tt else 0
    print(f"A2 closing (shares + MMF ${CORE_MMF_CLOSE}): Rs {acct_close:,.0f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
