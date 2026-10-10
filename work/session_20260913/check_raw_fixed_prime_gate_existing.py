"""Independent exact checks on the four already frozen cases only."""
import json
import math
from fractions import Fraction
from pathlib import Path
BASE=Path(__file__).resolve().parent
source=json.loads((BASE/"raw_accessory_scaling_probe.json").read_text())
cached=json.loads((BASE/"raw_fixed_prime_denominator_cached_checks.json").read_text())
indices=[2,4,8,16]
primes=[2,3,5,7,11,13,17,19]
assert cached["prime_set"]==primes
saved={row["n"]:row for row in source["cases"]}
assert all(n in saved for n in indices)
expected={row["n"]:row for row in cached["cases"]}
assert set(expected)==set(indices)
def integ(v):
    v=Fraction(v)
    assert v.denominator==1
    return v.numerator
def valuation(v,p):
    assert v!=0
    v=abs(v); a=0
    while v%p==0:
        v//=p; a+=1
    return a
results=[]
for n in indices:
    pol=saved[n]["exact_polynomial_input"]
    aa=sum(integ(x) for x in pol["A"])
    bb=sum(integ(x) for x in pol["B"])
    assert bb!=0
    gg=math.gcd(aa,bb)
    q=abs(bb)//gg
    vals={str(p):valuation(q,p) for p in primes}
    assert str(q)==expected[n]["q"]
    assert str(gg)==expected[n]["raw_endpoint_gcd"]
    assert vals==expected[n]["valuations"]
    assert vals["2"]==n+2*((n+2)//4)
    results.append({"n":n,"q":str(q),"raw_endpoint_gcd":str(gg),
                    "valuations":vals,"status":"PASS"})
def fall(a,j):
    return math.factorial(a)//math.factorial(a-j)
D=[sum(math.comb(2+j,j)*fall(2+r,j) for j in range(3+r))
   for r in range(3)]
assert D==[19,106,685]
coeff=[940,64,49]
Pe=sum((-1)**r*coeff[r]*D[r] for r in range(3))
assert Pe==44641
# Independent use of the already frozen n=2 primitive Qhat coefficients.
Qhat=[17640,-9720,13404,-5832,940]
E=lambda k:sum((Fraction(1,math.factorial(j)) for j in range(k+1)),Fraction(0))
Pe_direct=sum(Qhat[j]*E(4-j) for j in range(5))
assert Pe_direct==Pe
out={"status":"PASS","scope":"Only frozen n=2,4,8,16; no degree solve, no new indices or primes",
     "source":"raw_accessory_scaling_probe.json / cases / exact_polynomial_input",
     "cases":results,"border_n2":{"D":D,"Pe":Pe,"direct_Pe":str(Pe_direct)}}
(BASE/"raw_fixed_prime_gate_independent_checks.json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps({"status":"PASS","cases":indices,"border_n2":out["border_n2"]},indent=2))

