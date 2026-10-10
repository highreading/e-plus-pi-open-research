#!/usr/bin/env python3
"""Bounded exact corroboration of a finite pole identity; no network or credentials."""
from fractions import Fraction
from math import comb
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent


def valuation(n):
    if not n:
        return None
    v = 0
    while n % 3 == 0:
        n //= 3
        v += 1
    return v


def pole(poly, h, ell, cutoff):
    step = 3 ** (h - ell)
    value = Fraction(0)
    for c in range(1, (2 * cutoff + 1) // step + 1, 2):
        if c % 3:
            j = (c * step - 1) // 2
            if 0 <= j < len(poly):
                value += Fraction(3 ** ell * poly[j], c)
    return value


def main():
    layer_checks = 0
    binomial_checks = 0
    sparse_checks = 0
    boundary_checks = 0
    cases = []
    for h in range(4, 8):
        H = 3 ** (h - 1)
        for B in sorted(set((0, 3, 11, H // 3, H - 8))):
            F = [((j*j + 7*j + 3) % 13) - 6 for j in range(B+1)]
            shifted = [-x for x in F] + [0] * (H - len(F)) + F
            cutoff = H + B
            for ell in range(2, h+1):
                step = 3 ** (h-ell)
                shift = 2 * 3 ** (ell-1)
                expected = Fraction(0)
                for c in range(1, (2*B+1)//step+1, 2):
                    if c % 3:
                        j = (c*step-1)//2
                        if 0 <= j <= B:
                            expected -= Fraction(2 * 3**(2*ell-1) * F[j], c*(c+shift))
                assert pole(shifted,h,ell,cutoff) == expected
                if expected:
                    assert valuation(expected.numerator) >= 2*ell-1
                    assert expected.denominator % 3 != 0
                layer_checks += 1
            cases.append({"h":h,"H":H,"degree":B,"cutoff":cutoff})
        for r in range(1,H):
            v = valuation(comb(H,r))
            assert v == h-1-valuation(r)
            binomial_checks += 1
            for q in range(1,h+1):
                if v < q:
                    assert r % (3**max(0,h-q)) == 0
                sparse_checks += 1
        F = [0,0,1]
        shifted = [0,0,-1] + [0]*(H-3) + F
        full = pole(shifted,h,h,H+2)
        cut = pole(shifted,h,h,H+1)
        assert cut-full == -Fraction(3**h,2*(H+2)+1)
        boundary_checks += 1
    receipt = {
        "status":"PASS",
        "scope":"Exact finite layer pairing and binomial-valuation corroboration; no original Schur or Gram output",
        "source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "exact_layer_checks":layer_checks,
        "binomial_valuation_checks":binomial_checks,
        "sparse_precision_checks":sparse_checks,
        "deliberately_truncated_boundary_defect_checks":boundary_checks,
        "cases":cases,
        "original_residual_layer_computed":False,
    }
    (ROOT/"finite_pole_pair_receipt.json").write_text(json.dumps(receipt,indent=2)+"\n")
    print(json.dumps({k:v for k,v in receipt.items() if k!="cases"},indent=2))


if __name__=="__main__":
    main()
