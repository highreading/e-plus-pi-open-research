"""Interior saddle pairing from the unchanged certified odd witness vectors."""
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
def conj(a):
    return iv.mpc(a.real,-a.imag)
def widen(a,e):
    rad=iv.mpf([-1,1])*e
    return iv.mpc(a.real+rad,a.imag+rad)
f=[[z(a) for a in col] for col in raw["solutions"][:2]]
errors=[iv.mpf(4)/10**13,iv.mpf(3)/10**12]
ii=iv.mpc(0,1)
vv=[iv.sqrt(iv.mpf(2)/3)*(ii/iv.sqrt(3))**r for r in range(L)]
ww=[iv.sqrt(iv.mpf(2)/3)*(-ii/iv.sqrt(3))**r for r in range(L)]
pv=[widen(sum(conj(vv[r])*f[j][2*r] for r in range(L)),errors[j])
    for j in range(2)]
pw=[widen(sum(conj(ww[r])*f[j][2*r+1] for r in range(L)),errors[j])
    for j in range(2)]
assert pw[0].real > iv.mpf(1)/2
alpha=pw[1]/pw[0]
g=iv.sqrt(2)*(pv[1]-pv[0]*alpha)
rho=(iv.sqrt(5)-1)/2
ell=[iv.sqrt(iv.mpf(2)/5)*(ii*iv.sqrt(iv.mpf(3)/5))**r
     for r in range(L)]
lf=[widen(sum(conj(ell[r])*(f[j][2*r]+rho*f[j][2*r+1])
              for r in range(L)),2*errors[j]) for j in range(2)]
# The full test has norm sqrt(1+rho^2)<2. The full-space solved-vector
# bounds already include every infinite tail of the finite approximants.
numerator=iv.sqrt(2)*(lf[1]-lf[0]*alpha)
base_pair=2/(iv.sqrt(15)*(1-1/iv.sqrt(5)))
amplitude=numerator/(g*base_pair)
assert amplitude.real > iv.mpf(604)/1000
assert amplitude.real < iv.mpf(605)/1000
assert abs(amplitude.imag) < iv.mpf(1)/10**8
out={"status":"PASS","new_linear_solves":0,"new_canonical_degrees":0,
     "uses":"unchanged raw_odd_limit_certificate_vectors.json",
     "limiting_projection_coefficient":str(alpha),
     "saddle_test_pairings":[str(a) for a in lf],
     "numerator":str(numerator),"base_pair":str(base_pair),
     "g_even":str(g),"saddle_amplitude":str(amplitude),
     "rational_real_bounds":["0.604","0.605"],
     "phase":"R_(2m)(rho) tends to this positive amplitude, without alternating phase"}
(BASE/"raw_even_interior_multiplier_certificate.json").write_text(
    json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))
