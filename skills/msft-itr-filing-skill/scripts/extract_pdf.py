#!/usr/bin/env python3
"""
Extract text from ITR-related PDFs (Form 16/12BA, AIS/TIS, Form 26AS, 1042-S,
Fidelity statements, broker reports). Handles password-protected TRACES/portal PDFs
by trying common password patterns derived from PAN + DOB.

Usage:
    python extract_pdf.py <file1.pdf> [file2.pdf ...] --pan ABCDE1234F --dob 01012000

If --pan/--dob are omitted, only non-encrypted PDFs are read.
Requires: pypdf   (pip install pypdf)
"""
import argparse
import sys


def candidate_passwords(pan: str | None, dob: str | None) -> list[str]:
    """Common password patterns for TRACES / income-tax portal PDFs.
    dob expected as DDMMYYYY."""
    c: list[str] = [""]
    if pan:
        c += [pan.upper(), pan.lower()]
    if pan and dob:
        c += [
            pan.upper() + dob,
            pan.lower() + dob,
            (pan[:5].upper() + dob),
            (pan[:5].lower() + dob),
        ]
    if dob:
        c += [dob]
    # de-dupe, keep order
    seen, out = set(), []
    for p in c:
        if p not in seen:
            seen.add(p)
            out.append(p)
    return out


def extract(path: str, cands: list[str]) -> None:
    from pypdf import PdfReader

    print("=" * 20, path, "=" * 20)
    try:
        r = PdfReader(path)
        if r.is_encrypted:
            ok = False
            for pw in cands:
                try:
                    if r.decrypt(pw):
                        print(f"[decrypted with password pattern: {pw!r}]")
                        ok = True
                        break
                except Exception:
                    pass
            if not ok:
                print("ERROR: could not decrypt with candidate passwords "
                      "(pass correct --pan/--dob)")
                return
        for i, page in enumerate(r.pages):
            print(f"----- page {i + 1} -----")
            print(page.extract_text())
    except Exception as e:  # noqa: BLE001
        print("ERROR:", e)
    print()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+", help="PDF file paths")
    ap.add_argument("--pan", help="PAN, e.g. ABCDE1234F")
    ap.add_argument("--dob", help="Date of birth as DDMMYYYY, e.g. 01012000")
    args = ap.parse_args()
    cands = candidate_passwords(args.pan, args.dob)
    for f in args.files:
        extract(f, cands)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
