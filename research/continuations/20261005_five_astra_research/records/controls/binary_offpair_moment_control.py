"""Coordinator-derived finite moment expansions and polynomial certificates."""
import math,json,resource
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
out=Path(__file__).resolve().parent
data=json.loads((out/'binary_fourth_lift_control.json').read_text())
p=data['P_newton_mod32'];q=data['Q_newton_mod64'];B=data['boundary_values_mod64']
def choose(n,k):return math.comb(n,k) if 0<=k<=n else 0
def coeffs(poly,j):
    def T(a,x):
        return choose(132+a-1,a)*sum(v*choose(x,r-a) for r,v in enumerate(poly) if r>=a)
    ans={-1:j*T(0,j-1)}
    for a in range(len(poly)):
        ans[a]=T(a,j)+j*T(a,j-1)+j*T(a+1,j-1)
    return ans
def qcoeffs(j):
    ans=coeffs(q,j)
    raw={-1-s:sum((-1)**a*B[a]*choose(a,s) for a in range(s,7)) for s in range(7)}
    for a in range(-8,1):ans[a]=ans.get(a,0)+(1+j)*raw.get(a,0)+j*raw.get(a+1,0)
    return ans
def nc(v,m):
    a=[]
    while v:
        a.append(v[0]%m);v=[(v[i+1]-v[i])%m for i in range(len(v)-1)]
    return a
spec=[('P45',p,2,8,{-1:2,0:1,2:2,3:4,4:4}),
('P53',p,1,8,{-1:2,0:7,1:2,2:2,4:4}),
('P57',p,3,8,{-1:5,0:6,1:2,2:6,3:4}),
('Q55',q,1,4,{-4:2,-3:2,-2:1,-1:2})]
report={}
for name,poly,r,m,expected in spec:
    grids=[qcoeffs(r+64*s) if name=='Q55' else coeffs(poly,r+64*s) for s in range(24)]
    errors={a:nc([(g.get(a,0)-expected.get(a,0))%m for g in grids],m) for a in range(-8,22)}
    bad={str(a):v for a,v in errors.items() if any(v)}
    report[name]={'j_residue_mod64':r,'modulus':m,'all_Newton_coefficients_zero':not bad,'nonzero_difference_certificates':bad}
g=[coeffs(p,4+64*s) for s in range(24)]
report['P_even_j4']={'every_moment_coefficient_even':all(v%2==0 for row in g for v in row.values()),
'M4_coefficient_Newton_mod8':nc([row[4]%8 for row in g],8)}
report['bounded_polynomial_certificate_only']=True
report['actual_binomial_carry_arguments_not_evaluated']=True
(out/'binary_offpair_moment_control.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
