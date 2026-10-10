"""Numerical candidate generator only: Schur interpolation, series inversion,
then rounding in the endpoint-fixed integral-Hurwitz basis. Proof is separate."""
from pathlib import Path
from math import factorial
import mpmath as mp,numpy as np,json
mp.mp.dps=160
SESSION=Path('work/session_20261002_codex_continuation')
R=mp.mpf('2.65');N=60
z=mp.mpc(.5,.5);H=lambda z:2*mp.ellipk(z)/mp.pi
h=H(z);a=2*mp.pi*(h.real**2-h.imag**2);t=h.imag/h.real
ell=1-(h*mp.diff(H,z)).imag/(h.real**2-h.imag**2)
def smul(c,d,N):return [sum(c[j]*d[k-j] for j in range(max(0,k-len(d)+1),min(k+1,len(c)))) for k in range(N+1)]
def sinv(c,N):
    out=[1/c[0]]
    for k in range(1,N+1):out.append(-sum(c[j]*out[k-j] for j in range(1,min(len(c),k+1)))/c[0])
    return out
def strip(c):
    b=c[0];M=len(c)-2;return smul(c[1:],sinv([1-b*b]+[-b*v for v in c[1:]],M),M)
def compose(c,d,N):
    out=[mp.mpf(0)]*(N+1);power=[mp.mpf(1)]+[mp.mpf(0)]*N
    for k in range(len(c)):
        if k:power=smul(power,d,N)
        for j in range(N+1):out[j]+=c[k]*power[j]
    return out
S=smul([-mp.mpf(1),-mp.mpf(1),mp.mpf('.5')],sinv([mp.mpf(4),mp.mpf(-8),mp.mpf(8),mp.mpf(-4),mp.mpf(1)],N),N)
r=[ell]
for k in range(N):r.append((S[k]+sum(r[j]*r[k-j] for j in range(k+1))/2)/(k+1))
v=[1/a]
for k in range(N):v.append(sum(r[j]*v[k-j] for j in range(k+1))/(k+1))
xi=[mp.mpf(0)]+[v[k]/(k+1) for k in range(N)]
raw=json.loads((SESSION/'main/JET_TREE_265_PREFIX_DIAGNOSTIC.json').read_text())
paths=[]
for jets in raw['surviving_prefixes']:
    M=len(jets);phi=[mp.mpf(0)]+[mp.mpf(j)/factorial(k+1) for k,j in enumerate(jets)]
    fc=compose(xi[:M+1],phi,M);g=[fc[k]*R**k for k in range(1,M+1)]
    target=R*t;params=[]
    while g:
        b=g[0];params.append(b);target=(target-b)*R/(1-b*target)
        g=strip(g) if len(g)>1 else []
    paths.append((max([abs(v) for v in params]+[abs(target)]),jets,params,target))
paths.sort(key=lambda x:x[0])
score,jets,params,target=paths[0]
g=[target]+[mp.mpf(0)]*N
for b in reversed(params):
    shifted=[mp.mpf(0)]+g[:-1]
    numerator=[b]+shifted[1:];denominator=[mp.mpf(1)]+[b*v for v in shifted[1:]]
    g=smul(numerator,sinv(denominator,N),N)
f=[mp.mpf(0)]+[g[k-1]/R**k for k in range(1,N+1)]
# Formal Newton inversion of xi(phi)=f, retaining all coefficients each pass.
phi=[mp.mpf(0),mp.mpf(1)]+[mp.mpf(0)]*(N-1)
dxi=[(k+1)*xi[k+1] for k in range(N)]
for _ in range(7):
    residual=[v-w for v,w in zip(compose(xi,phi,N),f)]
    correction=smul(residual,sinv(compose(dxi,phi,N),N),N)
    phi=[v-w for v,w in zip(phi,correction)]
cum=mp.mpf(-1);basis=[]
for k in range(1,N+1):
    cum+=phi[k];basis.append(int(mp.nint(cum*factorial(k))))
records=[]
for last in [12,16,20,24,30,40,50,60]:
    coeff=[mp.mpf(0),mp.mpf(1)]+[mp.mpf(0)]*last
    for k,c in enumerate(basis[:last],1):coeff[k]+=mp.mpf(c)/factorial(k);coeff[k+1]-=mp.mpf(c)/factorial(k)
    ar=np.array([complex(v) for v in coeff]);ar[0]-=1+1j
    roots=np.roots(ar[::-1]);radius=float(min(abs(v) for v in roots))
    records.append({'last_basis_index':last,'diagnostic_radius':radius,'basis':basis[:last]})
    print(last,radius)
record={'status':'NUMERICAL_CANDIDATE_ONLY','chosen_integral_prefix':jets,'construction_disk':str(R),'schur_slack_score':str(score),'basis_candidates':records,'precision':mp.mp.dps,'formal_order':N}
(SESSION/'main/SCHUR_INTERPOLATED_POLYNOMIAL_CANDIDATES.json').write_text(json.dumps(record,indent=2)+'\n')
print('Chosen prefix',jets,'Schur slack score',mp.nstr(score,12))
