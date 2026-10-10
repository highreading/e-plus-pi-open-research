"""Universal determinant check; no approximant degrees or primes."""
from pathlib import Path
import json
import sys
BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE / "math_packages"))
import sympy as s

A,B,wP,wU,a0,a1,a2,r1,r2,TP,TU = s.symbols(
    "A B wP wU a0 a1 a2 r1 r2 TP TU")
G = A*wU-B*wP
a = s.Matrix([[a0,a1,a2]])
e = s.Matrix([[1,1,1]])
pu = s.Matrix([[TU,TU-a1,TU-a1-a2]])
pp = s.Matrix([[TP,TP-r1,TP-r1-r2]])
t = (A*pu-B*pp)/G
x = (wP*pu-wU*pp)/G
S = a1*a1-a0*a2
C = (a1-a0)*r2-(a2-a1)*r1
W = a1*r2-a2*r1
checks = {
    "exact_endpoint_Y": s.factor(
        s.Matrix.vstack(a,e+t,e).det()-(B*C-A*S)/G) == 0,
    "exact_endpoint_X": s.factor(
        s.Matrix.vstack(a,e+t,x).det()
        -((wP+TP)*S-(wU+TU)*C-a0*W)/G) == 0,
}
assert all(checks.values())
result = {"scope": "Universal scalar variables, no degree or prime sample",
          "checks": checks, "all_checks_pass": all(checks.values())}
(BASE / "hp_b2_contiguous_formal_identity_checks.json").write_text(
    json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
