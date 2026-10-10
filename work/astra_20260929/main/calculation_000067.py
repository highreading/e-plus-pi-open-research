from fractions import Fraction as F
from math import factorial
import json

def plus(*polys):
    out={}
    for p in polys:
        for i,x in p.items(): out[i]=out.get(i,F(0))+x
    return {i:x for i,x in out.items() if x}

def times(p,q):
    out={}
    for i,x in p.items():
        for j,y in q.items(): out[i+j]=out.get(i+j,F(0))+x*y
    return {i:x for i,x in out.items() if x}

def scaled(p,x): return {i:v*x for i,v in p.items() if v*x}

def falling(a,d,k):
    p={0:F(1)}
    for j in range(k): p=times(p,{0:F(a-j),1:F(d)})
    return p

def contraction(a): return plus(*(falling(a,6,r) for r in range(9)))

H={}; A={}; KP={}; BP={}
# Enumerate by total falling-factorial length, independently of the source loops.
for R in range(12):
    for c in range(R//2+1):
        b=R-2*c
        s=b+c
        weight=F((-1)**b,2**c*factorial(b)*factorial(c))
        h=scaled(times(falling(1,3,R),falling(1,3,s)),weight)
        k=scaled(times(times(falling(2,3,R),falling(2,3,s)),{0:F(4-R),1:F(6)}),weight)
        H=plus(H,h)
        A=plus(A,times(h,contraction(2-R)))
        KP=plus(KP,k)
        BP=plus(BP,times(k,contraction(3-R)))
inv={j:F((-3)**j,2**(j+1)) for j in range(3)}
K=times(KP,inv)
B=times(BP,inv)
C=plus(times(K,A),scaled(times(H,B),-1))

def modpoly(p,m):
    result=[0]*(max(p,default=0)+1)
    for i,x in p.items():
        assert x.denominator%3 != 0, (i,str(x))
        result[i]=x.numerator*pow(x.denominator,-1,m)%m
    while len(result)>1 and result[-1]==0: result.pop()
    return result

checks=[('H_mod9',H,9,[0]),('H_mod27',H,27,[0,9,9]),('K_mod9',K,9,[0,3]),('A_mod3',A,3,[0]),('A_mod9',A,9,[3,6]),('B_mod3',B,3,[1]),('C_mod27',C,27,[0,0,9])]
results={}
for name,p,m,expected in checks:
    actual=modpoly(p,m)
    results[name]={'actual':actual,'expected':expected,'match':actual==expected}
print(json.dumps({'checks':results,'all_match':all(v['match'] for v in results.values()),'exact_truncated_C_degree':max(C,default=0),'scope':'All coefficients of finite truncations; infinite tails require the separately audited bounds.'},indent=2))