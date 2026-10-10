"""Independent fixed-size closure audit; original finite C_s operators.
No remote code. Finite checks do not substitute for the support proof.
"""
import math,json,resource
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
OUT=Path(__file__).resolve().parent;n=2;b=81;mod=16
def choose(x,k):
    if k<0:return 0
    if x>=0:return math.comb(x,k) if k<=x else 0
    return (-1)**k*math.comb(k-x-1,k)
cs=(-1,2,-3,3)
E=[[sum(cs[s-1]*sum(choose(i,s-v)*choose(n,v)*choose(-v,j-i+s-v)
     for v in range(min(s,n)+1)) for s in range(1,5))%mod
    for j in range(b)] for i in range(b)]
def apply(v):return [sum(x*y for x,y in zip(row,v))%mod for row in E]
g=[((-1)**i)*(2-i+3*choose(i,2)-choose(i,3)+4*choose(i,4)-4*choose(i,5))%mod for i in range(b)]
t=[((-1)**i)*(-6-6*i+15*choose(i,3))%mod for i in range(b)]
eg=apply(g);eeg=apply(eg);et=apply(t);eet=apply(et)
pv=[((-1)**i)*(g[i]-2*eg[i]+4*eeg[i])%8 for i in range(b)]
qv=[((-1)**i)*(2*t[i]-4*et[i]+8*eet[i])%16 for i in range(b)]
def newton(values,m):
    row=values.copy();coeff=[]
    while row:
        coeff.append(row[0]%m);row=[(row[j+1]-row[j])%m for j in range(len(row)-1)]
    return coeff
pc=newton(pv,8);qc=newton(qv,16)
assert all(x==0 for x in pc[14:]) and all(x==0 for x in qc[12:])
d=[(qc[i]-2*pc[i])%16 for i in range(14)]
assert d[0]==0 and d[4]%4==d[8]%4==0 and d[12]%8==0
kappa=(d[4]//4+d[8]//4+d[12]//8)%2
B=[5,10,6,8,8]
sample=[]
for m in range(16):
    L=16*m
    value=(sum((-1)**a*B[a]*choose(L+a+4,3) for a in range(5))+
           sum(d[r]*choose(r+3,3)*choose(L+4,r+4) for r in range(14)))%16
    assert value==8*kappa*m%16;sample.append(value)
old=json.loads((OUT/'proportional_even_729_control.json').read_text())['records'][0]
actual=[((old['X_mod8192'][j]-old['Y_mod4096'][j])//2)%2 for j in (0,64)]
assert actual==[kappa,kappa]
report={'reference_n':n,'reference_b':b,'modulus':mod,
    'P_newton_mod8':pc[:14],'Q_newton_mod16':qc[:12],'d_newton_mod16':d,
    'kappa_mod2':kappa,'H_16m_mod16_for_m0to15':sample,
    'full_finite_operator_support_degree_checks_pass':True,
    'original_b81_pair_discrepancies_mod2':actual,
    'all_requested_checks_pass':True,'finite_certificate_only':True}
(OUT/'binary_fixed_polynomial_control.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
