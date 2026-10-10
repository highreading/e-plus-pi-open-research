"""Fixed rational polynomial contractions; coordinator-authored, exact fractions."""
from fractions import Fraction as F
from pathlib import Path
import math,json,resource
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
OUT=Path(__file__).resolve().parent
def trim(p):
    while len(p)>1 and not p[-1]:p.pop()
    return p
def add(a,b):
    c=[F(0)]*max(len(a),len(b))
    for i,v in enumerate(a):c[i]+=v
    for i,v in enumerate(b):c[i]+=v
    return trim(c)
def scale(a,s):return trim([v*s for v in a])
def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):c[i+j]+=v*w
    return trim(c)
def compose(a,b):
    c=[F(0)]
    for v in reversed(a):c=add(mul(c,b),[v])
    return c
def evaluation(p,x):
    c=F(0)
    for v in reversed(p):c=c*x+v
    return c
def vp(k):
    if not k:return 100000
    z=0
    while k%3==0:k//=3;z+=1
    return z
def residue(v,mod):
    assert v.denominator%3
    return v.numerator*pow(v.denominator,-1,mod)%mod
f=[F(0)]
for ell in range(9):
    product=[F(1)]
    for r in range(ell):product=mul(product,[-F(r),F(1)])
    for r in range(1,ell+1):product=mul(product,[F(r),F(1)])
    f=add(f,scale(product,F((-1)**ell,2**ell*math.factorial(ell))))
t=[F(0),F(1)]
f0=compose(f,[F(0),F(3)]);f1=compose(f,[F(1),F(3)]);f2=compose(f,[F(2),F(3)])
base=add(add(scale(f0,4),scale(mul([F(1),F(3)],f1),-8)),
         scale(mul(mul([F(1),F(3)],[F(2),F(3)]),f2),4))
eps=scale(mul([F(1),F(-9)],base),F(1,3))
degree=len(eps)-1
fall=[[F(1)]]
for h in range(1,degree+4):fall.append(mul(fall[-1],[F(1-h),F(1)]))
stirling=[[0]*(degree+4) for _ in range(degree+4)];stirling[0][0]=1
for a in range(1,degree+4):
    for h in range(1,a+1):stirling[a][h]=stirling[a-1][h-1]+h*stirling[a-1][h]
C={}
for a in range(degree+4):
    for t0 in range(a+1):
        c0=[F(0)]
        for h in range(t0,a+1):c0=add(c0,scale(fall[h],stirling[a][h]*math.comb(h,t0)))
        C[a,t0]=c0
I={}
def inner(a,b):
    key=(a,b)
    if key not in I:
        c0=[F(0)]
        for t0 in range(min(a,b)+1):c0=add(c0,mul(C[a,t0],C[b,t0]))
        I[key]=c0
    return I[key]
H=[F(0)]
for h,e in enumerate(eps):
    for a in range(h+1):H=add(H,scale(inner(a,h-a),e*math.comb(h,a)))
H3=compose(H,[F(0),F(3)])
coefficients_integral=all(v.denominator%3 for v in H3)
coeffsmod9=[residue(v,9) for v in H3] if coefficients_integral else None
vals=[residue(evaluation(H3,k),9) for k in range(len(H3))]
delta=[];row=vals.copy()
while row:
    delta.append(row[0]);row=[(row[i+1]-row[i])%9 for i in range(len(row)-1)]
assert residue(evaluation(H,21),9)==4
common=math.lcm(*(v.denominator for v in H))

f3=compose(f,[F(3),F(3)])
F1=add(add(scale(f1,-8),scale(mul([F(2),F(3)],f2),16)),
       scale(mul(mul([F(2),F(3)],[F(3),F(3)]),f3),-8))
e1=mul(mul([F(1),F(3,2)],[F(1),F(-9)]),F1)
G=[F(0)]
for h,e in enumerate(e1):
    for a in range(h+1):G=add(G,scale(inner(a,h-a),e*math.comb(h,a)))
G3=compose(G,[F(0),F(3)])
assert all(v.denominator%3 for v in H3+G3)
H3m=[residue(v,27) for v in H3];G3m=[residue(v,27) for v in G3]
Theta3=mul([F(7),F(-36)],G3)
Theta3m=[residue(v,27) for v in Theta3]
assert residue(evaluation(G,21),27)==11
assert all(v%9==0 for v in G3m[1:]) and G3m[0]%9==2
commonG=math.lcm(*(v.denominator for v in G))
report={'G_degree':len(G)-1,'G_coefficients_ascending':[str(v) for v in G],
 'G_common_denominator':str(commonG),'G_common_denominator_v3':vp(commonG),
 'H3_coefficients_mod27':H3m,'G3_coefficients_ascending':[str(v) for v in G3],
 'G3_coefficients_mod27':G3m,'Theta3_coefficients_mod27':Theta3m,
 'G21_mod27':residue(evaluation(G,21),27),'Theta_at_T7_mod27':residue(evaluation(Theta3,7),27),
 'scope':'fixed symbolic contraction valid all nonnegative M by A1turn11 identity; Q rule conditional on that audited proof',
 'finite_degree_symbolic_certificate':True}
(OUT/'weighted_mod27_residue_control.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if 'ascending' not in k and 'denominator' not in k}))
