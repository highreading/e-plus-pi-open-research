"""Coordinator-authored finite operator audit, not an infinite theorem."""
import math,json,resource
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
out=Path(__file__).resolve().parent
def choose(x,k):
    if k<0:return 0
    if x>=0:return math.comb(x,k) if k<=x else 0
    return (-1)**k*math.comb(k-x-1,k)
n,b,mod=2,81,32
cs=(-1,2,-3,3)
E=[[sum(cs[s-1]*sum(choose(i,s-v)*choose(n,v)*choose(-v,j-i+s-v)
    for v in range(min(s,n)+1)) for s in range(1,5))%mod
    for j in range(b)] for i in range(b)]
def apply(v):return [sum(x*y for x,y in zip(row,v))%mod for row in E]
def poly(coeff,i):return sum(c*choose(i,r) for r,c in enumerate(coeff))
def inverse_poly(coeff,weight,precision):
    term=[(-1)**i*poly(coeff,i)%mod for i in range(b)]
    result=[0]*b
    for depth in range(4):
        for i in range(b):result[i]=(result[i]+weight*(-2)**depth*term[i])%precision
        term=apply(term)
    values=[(-1)**i*result[i]%precision for i in range(b)]
    nc=[]
    while values:
        nc.append(values[0]);values=[(values[i+1]-values[i])%precision for i in range(len(values)-1)]
    return nc
p=inverse_poly((2,-9,3,-9,12,-4),1,16)
q=inverse_poly((10,2,8,15),2,32)
old=json.loads((out/'binary_fixed_polynomial_control.json').read_text())
assert all(x==0 for x in p[18:]) and all(x==0 for x in q[16:])
assert [x%8 for x in p[:14]]==old['P_newton_mod8']
assert [x%16 for x in q[:12]]==old['Q_newton_mod16']
assert all(x%8==0 for x in p[14:]) and all(x%16==0 for x in q[12:])
report={'reference_n':n,'reference_b':b,'P_newton_mod16':p[:18],
    'Q_newton_mod32':q[:16],'bounded_degree_checks_pass':True,
    'reductions_match_prior_complete_control':True,'finite_certificate_only':True}
(out/'binary_fixed_lift_control.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
