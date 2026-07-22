#!/usr/bin/env python3
"""
SBI TT-Buy rate lookup for ITR foreign-currency conversion (Rule 115 / 128 / Schedule FA).

Uses an SBI reference-rate CSV (columns include DATE and 'TT BUY'), e.g. the
sahilgupta/sbi_forex_rates dataset exported as SBI_REFERENCE_RATES_USD.csv.

Rules implemented:
- Returns the 'TT BUY' rate for a given date.
- If the date is a weekend/holiday (no row, or TT BUY = 0), falls back to the most
  recent PREVIOUS working day (up to 10 days back).

Usage:
    python sbi_fx_rate.py SBI_REFERENCE_RATES_USD.csv 2025-07-15 2025-12-31 2024-09-30
    # prints the TT-buy rate (and the actual rate date used) for each date.
"""
import csv
import sys
from datetime import datetime, timedelta


def load_rates(csv_path: str) -> dict:
    rates = {}
    with open(csv_path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            try:
                d = datetime.strptime(row["DATE"].split()[0], "%Y-%m-%d").date()
                tt = float(row["TT BUY"])
            except (ValueError, KeyError):
                continue
            if tt > 0:
                rates[d] = tt
    return rates


def rate_on(rates: dict, datestr: str, max_back: int = 10):
    """Return (rate, rate_date) for datestr; fall back to previous working day."""
    d = datetime.strptime(datestr, "%Y-%m-%d").date()
    for back in range(max_back + 1):
        dd = d - timedelta(days=back)
        if dd in rates:
            return rates[dd], dd
    return None, None


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 1
    rates = load_rates(argv[1])
    for datestr in argv[2:]:
        rt, rd = rate_on(rates, datestr)
        if rt is None:
            print(f"{datestr}: NO RATE FOUND")
        else:
            note = "" if str(rd) == datestr else f"  (fallback from {datestr})"
            print(f"{datestr}: TT-Buy = {rt}  [rate date {rd}]{note}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
