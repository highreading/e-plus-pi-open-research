"""Certified even inverse corner from the already certified odd witnesses."""
import json
import sys
from pathlib import Path
BASE=Path(__file__).resolve().parent
sys.path.insert(0,str(BASE/"math_packages"))
from mpmath import iv
iv.dps=100
raw=json.loads((BASE/"raw_odd_limit_certificate_vectors.json").read_text())
L=raw["L"]
assert L==64

def z(pair):
    return iv.mpc(iv.mpf(pair[0][0])/pair[0][1],
                  iv.mpf(pair[1][0])/pair[1][1])
f=[[z(a) for a in col] for col in raw["solutions"][:2]]
errors=[iv.mpf(4)/10**13,iv.mpf(3)/10**12]
# These are larger than the independently certified errors:
# 3.508e-13 and 2.827e-12 for the unchanged exact dyadic vectors.

def conj(a):
    return iv.mpc(a.real,-a.imag)
def widen(a,e):
    rad=iv.mpf([-1,1])*e
    return iv.mpc(a.real+rad,a.imag+rad)

ii=iv.mpc(0,1)
vv=[iv.sqrt(iv.mpf(2)/3)*(ii/iv.sqrt(3))**r for r in range(L)]
ww=[iv.sqrt(iv.mpf(2)/3)*(-ii/iv.sqrt(3))**r for r in range(L)]
pv=[widen(sum(conj(vv[r])*f[j][2*r] for r in range(L)),errors[j])
    for j in range(2)]
pw=[widen(sum(conj(ww[r])*f[j][2*r+1] for r in range(L)),errors[j])
    for j in range(2)]
assert pw[0].real > iv.mpf(1)/2
g=iv.sqrt(2)*(pv[1]-pv[0]*pw[1]/pw[0])
assert g.real > iv.mpf(91149)/10**5
assert g.real < iv.mpf(91150)/10**5
assert abs(g.imag) < iv.mpf(1)/10**8
inverse=1/g
error_constant=iv.sqrt(3)*iv.exp(iv.mpf(1)/2)/(4*g)
assert error_constant.real > iv.mpf(783)/1000
assert error_constant.real < iv.mpf(784)/1000
out={"status":"PASS","uses":"unchanged raw_odd_limit_certificate_vectors.json",
     "new_linear_solves":0,"new_canonical_degrees":0,
     "v_pairings":[str(a) for a in pv],"w_pairings":[str(a) for a in pw],
     "g_even":str(g),"inverse_g_even":str(inverse),
     "exponential_error_constant":str(error_constant),
     "rational_real_bounds":{"g_even":["0.91149","0.91150"],
                             "exponential_error_constant":["0.783","0.784"]}}
(BASE/"raw_even_limit_from_odd_witnesses.json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))
