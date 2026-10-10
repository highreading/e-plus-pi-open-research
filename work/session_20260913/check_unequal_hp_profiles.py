"""Predeclared exact profiles; finite checks do not assert asymptotics.

Profiles: n=4,8,12,16 and b=0,1,round(n/log(n)),n. All arithmetic is exact.
The old exact helper supplies integer jets and rational elimination only.
"""
from fractions import Fraction as Q
from pathlib import Path
from functools import reduce
import json, math, sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'scripts'))
from item179_independent_diagonal_exact import falling, tau, null_vector, primitive
sys.set_int_max_str_digits(0)

def add(a,b):
    return [(a[k] if k<len(a) else Q(0))+(b[k] if k<len(b) else Q(0)) for k in range(max(len(a),len(b)))]
def scale(a,v): return [v*x for x in a]
def mul(a,b):
    c=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c
def p_sequence(n):
    ps=[[Q(1)],[Q(-1,2),Q(1)]]
    for k in range(1,n):
        ps.append(add(mul(ps[-1],[Q(-1,2),Q(1)]),scale(ps[-2],Q(k*k,4*(4*k*k-1)))))
    return ps[:n+1]
def ell(p,n,B):
    return sum((v*sum((x/Q(math.factorial(n+k+1-j)) for j,x in enumerate(B)),Q(0)) for k,v in enumerate(p)),Q(0))
def h(k): return Q(2*(-1)**k,(2*k+1)*math.comb(2*k,k)**2)
def atan_interval(inv,m):
    t=sum((Q((-1)**k,(2*k+1)*inv**(2*k+1)) for k in range(m+1)),Q(0))
    u=Q(1,(2*m+3)*inv**(2*m+3))
    return (t,t+u) if m%2 else (t-u,t)
e0=sum((Q(1,math.factorial(k)) for k in range(601)),Q(0))
e1=e0+Q(1,600*math.factorial(600))
a0,a1=atan_interval(5,600)
t0,t1=atan_interval(239,200)
S0,S1=e0+16*a0-4*t1,e1+16*a1-4*t0
def decade(v):
    k=len(str(v.numerator))-len(str(v.denominator))
    def power(k):return Q(10**k) if k>=0 else Q(1,10**(-k))
    while v<power(k):k-=1
    while v>=power(k+1):k+=1
    return k
def bounds(X,Y):
    lo,hi=sorted([Q(X)+Y*S0,Q(X)+Y*S1])
    assert lo>0 or hi<0
    sign=1 if lo>0 else -1
    aa,bb=(lo,hi) if sign==1 else (-hi,-lo)
    assert decade(aa)==decade(bb)
    return {'sign':sign,'floor_log10_abs':decade(aa),'abs_gt_one':aa>1}
profiles=[(n,b) for n in [4,8,12,16] for b in [0,1,round(n/math.log(n)),n]]
rows=[]
for n,b in profiles:
    M=2*n+b+1
    mat=[[falling(k,j) for j in range(b+1)]+[falling(k,j)*tau(k-j) for j in range(n+1)] for k in range(n+1,M)]
    mat.append([-1]*(b+1)+[1]*(n+1))
    ns,rank=null_vector(mat)
    bc=primitive(ns); B=bc[:b+1]; C=bc[b+1:]
    A=[-sum([Q(falling(k,j)*B[j]) for j in range(min(k,b)+1)]+[Q(falling(k,j)*tau(k-j)*C[j]) for j in range(min(k,n)+1)],Q(0))/math.factorial(k) for k in range(n+1)]
    raw=primitive(A+list(map(Q,B+C)))
    A=raw[:n+1]; B=raw[n+1:n+b+2]; C=raw[n+b+2:]
    assert sum(B)==sum(C)
    assert all(sum(falling(k,j)*B[j] for j in range(b+1))+sum(falling(k,j)*tau(k-j)*C[j] for j in range(n+1))==0 for k in range(n+1,M))
    X,Y=sum(A),sum(B); assert Y
    g=math.gcd(X,Y)
    ps=p_sequence(n)
    Cstar=list(reversed(list(map(Q,C))))
    if b==0:
        U=[Q(0)]
        for k in range(n):U=add(U,scale(ps[k],-ell(ps[k],n,B)/h(k)))
        reconstructed=add(U,scale(ps[n],(Q(Y)-sum(U))/sum(ps[n])))
    else:
        reconstructed=[Q(0)]
        for k in range(n+1):reconstructed=add(reconstructed,scale(ps[k],-ell(ps[k],n,B)/h(k)))
    assert reconstructed==Cstar
    row={'n':n,'b':b,'M':M,'rank':rank,'matrix_shape':[len(mat),len(mat[0])],'A':A,'B':B,'C':C,'endpoint_gcd':g,'primitive_pair':[X//g,Y//g], 'primitive_endpoint':bounds(X//g,Y//g),'normalized_endpoint':bounds(Q(X,Y),1), 'B_height_digits':len(str(max(map(abs,B)))),'C_height_digits':len(str(max(map(abs,C)))),'primitive_Y_digits':len(str(abs(Y//g))), 'legendre_projection_exact_check':True}
    rows.append(row)
    print(n,b,row['primitive_endpoint']['floor_log10_abs'],row['normalized_endpoint']['floor_log10_abs'],flush=True)
out={'status':'finite exact profiles only; no asymptotic inference','predeclared_profiles':profiles,'constant_interval_method':'Taylor e through600; Machin arctan(1/5) through600 and arctan(1/239) through200, exact rational tail bounds','rows':rows}
(Path(__file__).with_name('unequal_hp_exact_profiles.json')).write_text(json.dumps(out,indent=2)+'\n')
