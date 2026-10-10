from fractions import Fraction as F
from math import factorial as fac
import json

def power(base,k):
    a=[F(1)]
    for _ in range(k):
        b=[F(0)]*(len(a)+len(base)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(base): b[i+j]+=x*y
        a=b
    return a

def ell(k):
    a=power([1,-2,2],k)
    return [a[k+j]*F(fac(k+j),fac(j)*fac(k)) for j in range(k+1)]

def hk(k):
    a=power([1,-1,F(1,2)],k)
    h=sum((a[s]*F(fac(k),fac(k-s)) for s in range(k+1)),F(0))
    dx=sum((a[s]*F(fac(k),fac(k-s-1)) for s in range(k)),F(0))
    return h,h+dx/k

def val(x,p):
    x=F(x)
    if not x: return 'infinity'
    a,b=abs(x.numerator),x.denominator
    v=0
    while a%p==0: a//=p; v+=1
    while b%p==0: b//=p; v-=1
    return v

with open('work/session_20260913/hp_b1_adjacent_scalar_gate_checks.json') as f:
    old=json.load(f)
for row in old['rows']:
    n=row['n']
    assert n in (2,8)
    E=[sum((F(1,fac(r)) for r in range(d+1)),F(0)) for d in range(2*n+2)]
    D=[fac(d)*E[d] for d in range(2*n+2)]
    P=[sum(ell(k),F(0)) for k in range(n+2)]
    Q=[8*sum((P[j-1]*P[k-j]/j for j in range(1,k+1)),F(0)) for k in range(n+2)]
    T={k:sum((c*E[n+j] for j,c in enumerate(ell(k))),F(0)) for k in (n,n+1)}
    h=hk(n)[0]; k=hk(n+1)[1]
    aa=power([1,-1,F(1,2)],n)
    bb=power([1,-1,F(1,2)],n+1)
    A=sum((F(fac(n),fac(n-s))*aa[s]*D[2*n-s] for s in range(n+1)),F(0))
    B=2*D[2*n+1]+sum((F(fac(n),fac(n-s+1))*(2*n+2-s)*bb[s]*D[2*n+1-s] for s in range(1,n+2)),F(0))
    assert T[n]==F(2**n,fac(n)**2)*A
    assert T[n+1]==F(2**(n+1),(n+1)*fac(n)**2)*B
    assert h.denominator==k.denominator==1
    C=k*A-h*B
    qp=2*k*Q[n]-(n+1)*h*Q[n+1]
    full=qp+F(2**(n+1),fac(n)**2)*C
    assert full==2*k*(Q[n]+T[n])-(n+1)*h*(Q[n+1]+T[n+1])
    delta=(n+1)*P[n+1]*h-2*P[n]*k
    assert delta!=0
    ratio=full/delta
    checks={'P_n':P[n]==row['P_n'],'P_next':P[n+1]==row['P_next'],'H_n':h==row['H_n'],'K_next':k==row['K_next'],'Delta':delta==row['Delta'],'ratio':ratio==F(row['endpoint_ratio']),'q':ratio.denominator==row['actual_q'],'old_N_scaling':full*row['M']==row['N']}
    assert all(checks.values()),checks
    out={'n':n,'checks':checks,'H':str(h),'K':str(k),'A':str(A),'B':str(B),'C':str(C),'Qpart':str(qp),'full':str(full),'Delta':str(delta),'ratio':str(ratio),'q':ratio.denominator,'valuations':{name:{str(p):val(x,p) for p in (2,3)} for name,x in [('C',C),('full',full),('Delta',delta),('q',ratio.denominator),('old_N',row['N']),('old_M',row['M'])]},'old_v3_delta_field':row['v3_delta'],'old_v3_delta_matches_integer_Delta':row['v3_delta']==val(delta,3)}
    print(json.dumps(out,ensure_ascii=False))