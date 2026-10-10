"""Odd saddle multipliers from the unchanged three certified witness vectors.

No new inverse solve or quadrature. Fixed rational D2/c boxes are checked
against the already certified boundary-matrix output before use.
"""
import json
import re
import sys
from fractions import Fraction
from pathlib import Path

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE/"math_packages"))
from mpmath import iv
iv.dps = 100

raw = json.loads((BASE/"raw_odd_limit_certificate_vectors.json").read_text())
old = json.loads((BASE/"raw_odd_limit_interval_certificate.json").read_text())
assert raw["L"] == 64 and old["status"] == "PASS"
assert old["fixed_parameters"]["interval_decimal_precision"] == 100
L = raw["L"]


def exact_complex(pair):
    return iv.mpc(iv.mpf(pair[0][0])/pair[0][1],
                  iv.mpf(pair[1][0])/pair[1][1])


def conj(z):
    return iv.mpc(z.real, -z.imag)


def widen(z, error):
    radius = iv.mpf([-1, 1])*error
    return iv.mpc(z.real+radius, z.imag+radius)


def certified_box(old_text, lower, upper):
    parts = re.findall(r"\[([^,\]]+),\s*([^\]]+)\]", old_text)
    assert len(parts) == 2
    endpoints = [[Fraction(z.strip()) for z in part] for part in parts]
    scale = 10**12
    lo, hi = Fraction(lower, scale), Fraction(upper, scale)
    imaginary_radius = Fraction(1, 10**10)
    # Generous allowance for serializing the existing 100-digit intervals.
    serialization_margin = Fraction(1, 10**90)
    assert lo+serialization_margin < endpoints[0][0]
    assert endpoints[0][1]+serialization_margin < hi
    assert -imaginary_radius+serialization_margin < endpoints[1][0]
    assert endpoints[1][1]+serialization_margin < imaginary_radius
    real = iv.mpf([lower, upper])/scale
    imaginary = iv.mpf([-1, 1])/10**10
    return iv.mpc(real, imaginary)


boxes = [
    [(743784742762, 743784742765), (76149347069, 76149347087)],
    [(493103175444, 493103175447), (889138775516, 889138775534)],
]
D2 = [[certified_box(old["D2"][i][j], *boxes[i][j])
       for j in range(2)] for i in range(2)]
c = [
    certified_box(old["D3"][0][2], -512209298805, -512209298703),
    certified_box(old["D3"][1][2], 1006345884897, 1006345884999),
]
det = D2[0][0]*D2[1][1]-D2[0][1]*D2[1][0]
assert det.real > iv.mpf(62)/100
coefficients = [
    (D2[1][1]*c[0]-D2[0][1]*c[1])/det,
    (-D2[1][0]*c[0]+D2[0][0]*c[1])/det,
]

f = [[exact_complex(z) for z in col] for col in raw["solutions"]]
error_rationals = [(4, 10**13), (3, 10**12), (2, 10**11)]
for saved, (numerator, denominator) in zip(
        old["solution_error_intervals"], error_rationals):
    match = re.fullmatch(r"\[([^,\]]+),\s*([^\]]+)\]", saved)
    assert match is not None
    upper = Fraction(match.group(2).strip())
    assert upper+Fraction(1, 10**90) < Fraction(numerator, denominator)
errors = [iv.mpf(numerator)/denominator for numerator, denominator in error_rationals]
ii = iv.mpc(0, 1)
v = [iv.sqrt(iv.mpf(2)/3)*(ii/iv.sqrt(3))**r for r in range(L)]
vpair = [
    widen(sum(conj(v[r])*f[j][2*r] for r in range(L)), errors[j])
    for j in range(3)
]
g = vpair[2]-vpair[0]*coefficients[0]-vpair[1]*coefficients[1]
assert g.real < -2 and g.real > -3

rho = (iv.sqrt(5)-1)/2
phi = 1/rho
ell_plus = [
    iv.sqrt(iv.mpf(2)/5)*(ii*iv.sqrt(iv.mpf(3)/5))**r for r in range(L)
]
ell_minus = [conj(z) for z in ell_plus]


def solution_test(ell, z):
    # ||ell*(f1+z f2)||=sqrt(1+z²)<2 for z=rho or -phi.
    pairings = [
        widen(sum(conj(ell[r])*(f[j][2*r]+z*f[j][2*r+1])
                  for r in range(L)), 2*errors[j])
        for j in range(3)
    ]
    value = pairings[2]-pairings[0]*coefficients[0]-pairings[1]*coefficients[1]
    return value, pairings


interior_numerator, interior_tests = solution_test(ell_plus, rho)
exterior_numerator, exterior_tests = solution_test(ell_minus, -phi)
base = 2/(iv.sqrt(15)*(1-1/iv.sqrt(5)))
interior = interior_numerator/(g*base)
# The odd monic reference lies in channel two, contributing z=-phi.
exterior = exterior_numerator/(g*(-phi)*base)
assert interior.real > iv.mpf(282)/1000
assert interior.real < iv.mpf(283)/1000
assert exterior.real > -iv.mpf(1193)/1000
assert exterior.real < -iv.mpf(1192)/1000
assert abs(interior.imag) < iv.mpf(1)/10**7
assert abs(exterior.imag) < iv.mpf(1)/10**7

payload = {
    "status": "PASS",
    "uses": ["raw_odd_limit_certificate_vectors.json",
             "raw_odd_limit_interval_certificate.json"],
    "new_linear_solves": 0,
    "new_quadrature": 0,
    "new_canonical_degrees": 0,
    "old_D2_and_c_coarse_boxes_checked": True,
    "old_solution_error_bounds_checked": True,
    "woodbury_coefficients": [str(z) for z in coefficients],
    "g_odd": str(g),
    "interior_tests": [str(z) for z in interior_tests],
    "exterior_tests": [str(z) for z in exterior_tests],
    "interior_numerator": str(interior_numerator),
    "exterior_numerator": str(exterior_numerator),
    "base_pair": str(base),
    "interior_amplitude": str(interior),
    "exterior_amplitude": str(exterior),
    "rational_real_bounds": {
        "interior": ["0.282", "0.283"],
        "exterior": ["-1.193", "-1.192"],
    },
    "phase": {
        "interior": "R_(2m+1)(rho) tends to B_odd without alternating phase",
        "exterior": "(-1)^m Rtilde_(2m+1)(-rho) tends to A_odd",
    },
}
(BASE/"raw_odd_saddle_multiplier_certificate.json").write_text(
    json.dumps(payload, indent=2)+"\n")
print(json.dumps(payload, indent=2))
