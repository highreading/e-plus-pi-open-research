"""New exact three-integral-jet obstruction; rational interval arithmetic only."""
from fractions import Fraction as Q
from pathlib import Path
import json

SESSION=Path('work/session_20261002_codex_continuation')
source=json.loads((SESSION/'main/SECOND_JET_RADIUS_CERTIFICATE.json').read_text())
def read(name):return tuple(Q(v['numerator'],v['denominator']) for v in source[name])
def mul(x,y):
    z=[a*b for a in x for b in y];return min(z),max(z)
def add(x,y):return x[0]+y[0],x[1]+y[1]
def sub(x,y):return x[0]-y[1],x[1]-y[0]
def div(x,y):
    assert y[0]>0
    return mul(x,(1/y[1],1/y[0]))
def scale(x,y):return mul(x,(y,y))
def rec(x):
    out=[]
    for j,v in enumerate(x):
        z=v*10**30;k=z.numerator//z.denominator
        if j and z.denominator!=1:k+=1
        v=Q(k,10**30);out.append(dict(numerator=v.numerator,denominator=v.denominator))
    return out
one=(Q(1),Q(1));a=read('a_interval');t=read('t_interval');ell=read('ell_interval')
R=Q(2809621359339520,10**15);s=1/R
# The first-jet piecewise bound makes j=1 the only candidate.
assert a[0]*t[0]>1 and a[1]*t[1]<2
assert R*R>1/t[0]
assert R*R>1/(2*(1+t[1])/a[1]-t[1])
x=div((R,R),a);y=scale(t,R)
one_x=sub(one,mul(x,x))
factor=div((R*R,R*R),scale(mul(a,one_x),2))
cap=(1/factor[1],1/factor[0])
# The coefficient constraint leaves k=-2,-1,0.
assert 1+ell[0]>cap[1] and 3-ell[1]>cap[1]
Z=div(sub(y,x),scale(sub(one,mul(x,y)),s))
second={}
for k in [-2,-1]:
    B=mul(factor,add(ell,(Q(k),Q(k))))
    assert -1<B[0]<=B[1]<1
    upper=div(add(B,(s,s)),add(one,scale(B,s)))
    assert Z[0]>upper[1]
    second[str(k)]={'B':rec(B),'upper_capacity':rec(upper),'strict_rejection':True}
B=mul(factor,ell);assert 0<B[0]<=B[1]<1
eta=add((Q(-1,4),Q(-1,4)),scale(mul(ell,ell),Q(3,2)))
one_B=sub(one,mul(B,B))
Cfactor=div((R**3,R**3),scale(mul(mul(a,one_x),one_B),6))
C0=add(mul(Cfactor,eta),div(mul(x,mul(B,B)),one_B))
# C_l=C0+l*Cfactor. Unit-disk coefficients leave only l=-1,0.
assert add(C0,Cfactor)[0]>1
assert sub(C0,scale(Cfactor,2))[1]<-1
T=div(sub(Z,B),scale(sub(one,mul(B,Z)),s))
third={}
for l in [-1,0]:
    C=add(C0,scale(Cfactor,l));assert -1<C[0]<=C[1]<1
    pseudodistance=div(sub(T,C),sub(one,mul(C,T)))
    assert pseudodistance[0]>s if l==-1 else pseudodistance[1]<-s
    third[str(l)]={'C':rec(C),'signed_pseudodistance':rec(pseudodistance),'strict_rejection':True}
record={'status':'PASS_NEW_EXACT_THIRD_JET_RADIUS_CERTIFICATE','scope':'One rational test radius rejected; restriction excludes every larger disk','strict_radius_upper':{'numerator':R.numerator,'denominator':R.denominator},'strict_radius_upper_decimal':'2.809621359339520','input_certificate':'SECOND_JET_RADIUS_CERTIFICATE.json','a':rec(a),'t':rec(t),'ell':rec(ell),'Schwarzian_at_origin':{'numerator':-1,'denominator':4},'eta':rec(eta),'forced_first_derivative':1,'second_candidates':[-2,-1,0],'second_rejections':second,'forced_second_derivative':0,'third_candidates':[-1,0],'third_target':rec(T),'third_rejections':third}
(SESSION/'main/THIRD_JET_RADIUS_CERTIFICATE.json').write_text(json.dumps(record,indent=2)+'\n')
print(record['status'],record['strict_radius_upper_decimal'])
