"""Fixed exact controls, not an extension of the modular root search."""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import json

def add(a,b):
    return [(a[k] if k<len(a) else Q())+(b[k] if k<len(b) else Q()) for k in range(max(len(a),len(b)))]
def mul(a,b):
    ans=[Q()]*(len(a)+len(b)-1)
    for j,x in enumerate(a):
        for k,y in enumerate(b):ans[j+k]+=x*y
    return ans
def scale(a,c):return [x*c for x in a]
def deriv(a):return [k*a[k] for k in range(1,len(a))] or [Q()]
def H(n):
    a=[Q(1)]
    for _ in range(n):a=mul(a,[Q(1),Q(-1),Q(1,2)])
    return [factorial(n)*a[n-j]/factorial(j) for j in range(n+1)]

rows=[]
for n in (1,2,4,8):
    hn=H(n);d=deriv(hn);dd=deriv(d);ddd=deriv(dd)
    ode=add(add(mul([0,1],ddd),mul([n+2,-2],dd)),add(mul([-2,2],d),scale(hn,-2*n)))
    assert all(x==0 for x in ode)
    jets=[];a=hn
    for k in range(n+4):
        jets.append(sum(a,Q()))
        a=deriv(a)
    for j in range(n+1):
        assert jets[j+3]+(n+j)*jets[j+2]-2*j*jets[j+1]+2*(j-n)*jets[j]==0
    aa=hn+[Q()]*3
    for k in range(n+1):
        assert 2*(n-k)*aa[k]==(k+2)*(k+1)*(n+k+2)*aa[k+2]-2*(k+1)**2*aa[k+1]
    rows.append({'n':n,'ODE_and_derivative_and_coefficient_recurrences':True})

for p in (3,5,7,13):
    def aq(x,y):return ((x[0]+y[0])%p,(x[1]+y[1])%p)
    def nq(x):return ((-x[0])%p,(-x[1])%p)
    def sq(x,c):return (x[0]*c%p,x[1]*c%p)
    def mq(x,y):return ((x[0]*y[0]-x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p)
    def pq(x,n):
        ans=(1,0)
        for _ in range(n):ans=mq(ans,x)
        return ans
    def ffun(x):
        ans=(0,0);xp=(1,0);ff=1
        for r in range(p):
            if r:ff=ff*r%p
            ans=aq(ans,sq(xp,ff));xp=mq(xp,x)
        return ans
    def efun(x):
        ans=(0,0);xp=(1,0);ff=1
        for r in range(p):
            if r:ff=ff*r%p
            ans=aq(ans,sq(xp,pow(ff,-1,p)));xp=mq(xp,x)
        return ans
    half=pow(2,-1,p);alpha=(half,half);beta=(half,-half%p);inv_i=(0,p-1)
    # Direct weighted factorial sum.
    cs=[1,1]
    for r in range(2,p):cs.append((cs[-1]-half*cs[-2])%p)
    val=sum((-1)**r*factorial(r)*cs[r] for r in range(p))%p
    h=H(p-1);hp=sum(h,Q());assert hp.denominator==1 and hp.numerator%p==val
    euler=mq(inv_i,aq(mq(alpha,ffun(nq(alpha))),nq(mq(beta,ffun(nq(beta))))))
    trunc=nq(mq(inv_i,aq(mq(pq(alpha,p),efun((1,p-1))),nq(mq(pq(beta,p),efun((1,1)))))))
    assert euler==trunc==(val,0)
    assert pq(alpha,p)==(alpha if p%4==1 else beta)
    rows.append({'p':p,'C_mod_p':val,'Gaussian_Euler_and_Wilson_truncated_exponential_formulas':True})

out={'status':'PASS; fixed exact controls only','checks':rows}
Path(__file__).with_name('hp_two_branch_identity_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
