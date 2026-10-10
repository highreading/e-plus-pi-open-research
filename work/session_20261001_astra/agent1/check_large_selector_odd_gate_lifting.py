from fractions import Fraction as Q
from math import factorial, comb
import json
from pathlib import Path

def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def power(a,e):
    ans=[1]
    for _ in range(e): ans=mul(ans,a)
    return ans

def residue(x,mod):
    x=Q(x)
    return (x.numerator*pow(x.denominator,-1,mod))%mod

def val(x,p):
    x=Q(x)
    if not x: return None
    a,b=x.numerator,x.denominator
    v=0
    while a%p==0: a//=p; v+=1
    while b%p==0: b//=p; v-=1
    return v

# One newly derived witness; no parameter or prime search.
n,m,p=4,37,151
N=2*n+4*m; J=N-n
assert J==p+1 and n<p and N<2*p
assert m%2==1
B=mul(power([1,-2,2],n),power([1,-4,2],2*m))
D=[1]
for j in range(1,N+1): D.append(j*D[-1]+1)
fd=[0,2]
for j in range(1,N): fd.append(j*fd[j]-comb(j,2)*fd[j-1])
mu=[Q(fd[h+1],factorial(h+1)) for h in range(N)]
prefix=[Q(0)]
for v in mu: prefix.append(prefix[-1]+v)
K=[comb(j,n)*B[j] if j>=n else 0 for j in range(N+1)]
U=sum(K)
L=sum((K[j]*prefix[j] for j in range(n,N+1)),Q(0))
Vexp=sum(B[j]*(factorial(J)//factorial(j-n))*D[j] for j in range(n,N+1))
W=Vexp+factorial(n)*factorial(J)*L
q=(W/Q(factorial(n)*factorial(J)*U)).denominator
btop=2**(N//2)
Fn=n*D[n]+2*n*factorial(n)+1
Uhigh=sum(K[p:])
H1=(Uhigh-n*btop)//p
assert (Uhigh-n*btop)%p==0
wp=(factorial(p-1)+1)//p
assert (factorial(p-1)+1)%p==0
Mp=p*mu[p-1]
mp1=(Mp+2)/p
En=factorial(n)*(Q(D[p-1])+sum((Q(D[v-1],factorial(v)) for v in range(1,n+1)),Q(0)))
Slow=sum((Q(B[j]*D[j],factorial(j-n)) for j in range(n,p+n)),Q(0))
Lreg=L-mu[p-1]*Uhigh
Xi=btop*(n*En-D[n])+factorial(n)*(2*H1+n*btop*(2-2*wp-mp1))-Slow-factorial(n)*Lreg
assert residue(W-btop*Fn-p*Xi,p*p)==0
assert Fn%p==0
Theta=residue(btop*(Fn//p)+Xi,p)
assert residue(W/p,p)==Theta
# Low-degree endpoint expansion, separate from the full K contraction.
Apoly=power([1,2,2],n)
e0=Q(1-n,2)
Cseries=[Q(0)]*(n+1)
bc=Q(1)
for h in range(n//2+1):
    if h: bc*=Q(e0-h+1,h)
    Cseries[2*h]=bc*(-2)**h
T=mul(Apoly,Cseries)[:n+1]
a_n=T[n]
logC=[Q(0)]*(n+1)
for h in range(1,n//2+1): logC[2*h]=-Q(2**h,h)
b_n=mul(T,logC)[n]/2
assert a_n==Q(479,2) and b_n==-36
assert U==6204 and residue(U,p)==13
assert residue(U-a_n-p*b_n,p*p)==0
assert Fn==453 and val(q,p)==0
result={
 'status':'PASS_SINGLE_NEW_GATE_AND_FIRST_LIFT_WITNESS',
 'parameters':{'n':n,'m':m,'p':p,'N':N,'J':J},
 'F_n':Fn,'F_n_mod_p':Fn%p,
 'U':U,'U_mod_p':U%p,'v_p_U':val(U,p),
 'endpoint_a_n':str(a_n),'endpoint_b_n':str(b_n),
 'first_lift_Theta_mod_p':Theta,'v_p_W':val(W,p),'v_p_actual_q':val(q,p),
 'checks':['complete numerator modulo p squared','normalized first lift','independent low-degree endpoint expansion','actual reduced denominator cancellation'],
 'scope':'One exact example only. The all-index conclusions require the written proof; no prime scan or prior checker replay.'
}
Path('work/session_20261001_astra/agent1/large_selector_odd_gate_lifting_check.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
