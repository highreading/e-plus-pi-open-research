"""New maximal Taylor-order inverse-Apery arithmetic, exact rational only."""
from fractions import Fraction as Q
from math import factorial,gcd,lcm
from pathlib import Path
import json
SESSION=Path('work/session_20261002_codex_continuation')
N=100
f=[1,-1]
for k in range(2,N+1):f.append((-1)**k-k*(k-1)*f[k-2])
u=[0]
for k in range(1,N+1):u.append(4*f[k-1]-u[-1])
rows=[]
for n in range(2,N+1):
    E=sum((Q((-1)**k,factorial(k)) for k in range(n+1)),Q(0))
    V=sum((Q(u[k],factorial(k)) for k in range(n+1)),Q(0))
    D=int(E*factorial(n));B=int((1+V)*factorial(n))
    c=Q(B,D)
    normalized=[Q((-1)**k,factorial(k))*(c-(-1)**k*u[k]) for k in range(n+1)]
    A=lcm(*(x.denominator for x in normalized))
    coeff=[int(A*x) for x in normalized]
    C=coeff[0]
    assert sum(coeff)==A
    assert gcd(*coeff)==1
    assert 4*A%factorial(n-1)==0
    # Coefficients of (R+R')exp x+4A/(1+x²) vanish through x^(n-1).
    pol=[coeff[k]+((k+1)*coeff[k+1] if k<n else 0) for k in range(n+1)]
    for j in range(n):
        kernel=sum((Q(pol[k],factorial(j-k)) for k in range(min(j,n)+1)),Q(0))
        if j%2==0:kernel+=4*A*(-1)**(j//2)
        assert kernel==0
    endpoint_gcd=gcd(A,C);q=A//endpoint_gcd
    assert 4*endpoint_gcd%factorial(n-1)==0
    assert factorial(n)%endpoint_gcd==0
    assert q==D//gcd(D,B)
    rows.append({'n':n,'D_n':D,'B_n':B,'primitive_coefficient_A':A,'primitive_coefficient_C':C,'endpoint_gcd':endpoint_gcd,'actual_endpoint_denominator':q,'coefficient_ray':coeff if n<=12 else None,'q_log_factorial_ratio_diagnostic':None})
out={'status':'PASS_EXACT_NEW_MAXIMAL_ORDER_IDENTITIES','n_range':[2,N],'f_initial':f[:12],'u_initial':u[:12],'rows':rows,'scope':'Exact family identities and raw factorial divisibility; no uniform endpoint gcd estimate or main irrationality claim.'}
(SESSION/'main/INVERSE_APERY_MAXIMAL_ORDER_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n')
for r in rows[:12]:print(r['n'],r['primitive_coefficient_A'],r['endpoint_gcd'],r['actual_endpoint_denominator'])
print('PASS exact n=2..100')
