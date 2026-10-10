"""Coordinator-authored exact raw polynomial contractions, not a projected ray."""
import math,json,resource,time
from pathlib import Path
from fractions import Fraction as F
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
OUT=Path(__file__).resolve().parent;start=time.monotonic()
def trim(a):
    while len(a)>1 and not a[-1]:a.pop()
    return a
def add(a,b):
    c=[F(0)]*max(len(a),len(b))
    for i,v in enumerate(a):c[i]+=v
    for i,v in enumerate(b):c[i]+=v
    return trim(c)
def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):c[i+j]+=v*w
    return trim(c)
def scale(a,s):return trim([v*s for v in a])
def compose(a,b):
    c=[F(0)]
    for v in reversed(a):c=add(mul(c,b),[v])
    return c
def vp(k):
    if not k:return 100000
    z=0
    while k%3==0:k//=3;z+=1
    return z
def residue(v,mod):
    assert v.denominator%3,(v,mod)
    return v.numerator*pow(v.denominator,-1,mod)%mod
f=[F(0)]
for ell in range(12):
    term=[F(1)]
    for r in range(ell):term=mul(term,[-F(r),F(1)])
    for r in range(1,ell+1):term=mul(term,[F(r),F(1)])
    f=add(f,scale(term,F((-1)**ell,2**ell*math.factorial(ell))))
f0,f1,f2,f3=[compose(f,[F(k),F(3)]) for k in range(4)]
F0=add(add(scale(f0,4),scale(mul([F(1),F(3)],f1),-8)),
       scale(mul(mul([F(1),F(3)],[F(2),F(3)]),f2),4))
F1=add(add(scale(f1,-8),scale(mul([F(2),F(3)],f2),16)),
       scale(mul(mul([F(2),F(3)],[F(3),F(3)]),f3),-8))
A2=[F(1),F(-99,2),F(81,2)]
e0=scale(mul(A2,F0),F(1,3));e1=mul(A2,F1)
degree=30
fall=[[F(1)]]
for h in range(1,degree+1):fall.append(mul(fall[-1],[F(1-h),F(1)]))
stirling=[[0]*(degree+1) for _ in range(degree+1)];stirling[0][0]=1
for a in range(1,degree+1):
    for h in range(1,a+1):stirling[a][h]=stirling[a-1][h-1]+h*stirling[a-1][h]
C={}
for a in range(degree+1):
    for t in range(a+1):
        c=[F(0)]
        for h in range(t,a+1):c=add(c,scale(fall[h],stirling[a][h]*math.comb(h,t)))
        C[a,t]=c
I={}
def inner(a,b):
    key=tuple(sorted((a,b)))
    if key not in I:
        c=[F(0)]
        for t in range(min(a,b)+1):c=add(c,mul(C[a,t],C[b,t]))
        I[key]=c
    return I[key]
def contraction(poly,terms):
    # Each term is coefficient * D^a * E^b * (D+E)^extra.
    out=[F(0)]
    for a,b,extra,factor in terms:
        for h,v in enumerate(poly):
            if v:
                for k in range(h+extra+1):
                    out=add(out,scale(inner(a+k,b+h+extra-k),
                                     factor*v*math.comb(h+extra,k)))
    return out
H=contraction(e0,[(0,0,0,F(1)),(1,1,1,F(9,2))])
G=contraction(e1,[(0,0,0,F(1)),(1,0,0,F(3)),(1,1,0,F(-9)),
                 (1,2,0,F(27)),(1,1,1,F(9,2)),(2,1,1,F(27,2))])
H9=compose(H,[F(0),F(9)]);G9=compose(G,[F(0),F(9)])
H9_integral=all(v.denominator%3 for v in H9)
G9_integral=all(v.denominator%3 for v in G9)
report={
 'scope':'Raw norm and mixed contractions only; projection and factorial tail are separate',
 'moment_terms':12,'H_degree':len(H)-1,'G_degree':len(G)-1,
 'H_coefficients':[str(v) for v in H],'G_coefficients':[str(v) for v in G],
 'H_common_denominator':str(math.lcm(*(v.denominator for v in H))),
 'G_common_denominator':str(math.lcm(*(v.denominator for v in G))),
 'H_coefficient_max_denominator_v3':max(vp(v.denominator) for v in H),
 'G_coefficient_max_denominator_v3':max(vp(v.denominator) for v in G),
 'H9_coefficients_individually_integral':H9_integral,
 'G9_coefficients_individually_integral':G9_integral,
 'H9_coefficients_mod81':[residue(v,81) for v in H9] if H9_integral else None,
 'G9_coefficients_mod81':[residue(v,81) for v in G9] if G9_integral else None,
 'seconds':round(time.monotonic()-start,3)}
(OUT/'weighted_raw_mod81_control.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ('H_coefficients','G_coefficients')}))
