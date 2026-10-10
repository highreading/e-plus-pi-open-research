"""Independent root certificate, only primes127,151; all residues.
Rebuilds Toeplitz Jacobi-Trudi matrices, solves first column, verifies
residuals, reconstructs positive Q and negative Taylor endpoint.
Imports no author or agent checker. Integer modular arithmetic only.
"""
from pathlib import Path
from math import comb,factorial
import json,hashlib
base=Path(__file__).parent
src=base/'raw_third_predeclared_uniform_seed_certificate.json'
data=src.read_bytes(); source={r['p']:r for r in json.loads(data)['results']}

def detsolve(A,p):
 n=len(A); R=[row[:]+[int(i==0)] for i,row in enumerate(A)]
 det=1
 for j in range(n):
  t=next((i for i in range(j,n) if R[i][j]),None)
  assert t is not None,'singular expected-good seed'
  if t!=j:R[j],R[t]=R[t],R[j];det=-det
  pivot=R[j][j];det=det*pivot%p;ip=pow(pivot,-1,p)
  for i in range(j+1,n):
   c=R[i][j]*ip%p
   if c:
    R[i][j:]=[(v-c*w)%p for v,w in zip(R[i][j:],R[j][j:])]
 x=[0]*n
 for j in range(n-1,-1,-1):
  x[j]=(R[j][-1]-sum(R[j][l]*x[l] for l in range(j+1,n)))*pow(R[j][j],-1,p)%p
 assert [sum(row[j]*x[j] for j in range(n))%p for row in A]==[1]+[0]*(n-1)
 return det%p,x

def matrix_seed(k,b,p,fac,invfac):
 h=[]
 # Recurrence from (1+z²)h'=(1+z²+2bz)h at x=1.
 for d in range(2*k+1):
  if d==0:h.append(1);continue
  h.append(((h[d-1] if d>=1 else 0)+(2*b-d+2)*(h[d-2] if d>=2 else 0)+(h[d-3] if d>=3 else 0))*pow(d,-1,p)%p)
 A=[[h[k+i-j] if k+i-j>=0 else 0 for j in range(k+1)] for i in range(k+1)]
 det,x=detsolve(A,p)
 HD=1
 for j in range(k+1):HD=HD*fac[k+j]*invfac[j]%p
 D=HD*det%p
 M=[]
 for j in range(k+1):
  rj=fac[2*k-j]*invfac[j]*invfac[k-j]%p
  M.append(D*(-1)**j*x[j]*pow(rj,-1,p)%p)
 return D,M[::-1],hashlib.sha256(json.dumps(A).encode()).hexdigest()

def convolution(a,b,p):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%p
 return c

def rise(a,h,p):
 v=1
 for j in range(h):v=v*(a+j)%p
 return v

def border(n,r,p):
 # Actual original finite endpoint, not negative-background formula.
 falling=1;v=1
 for j in range(1,n+r+1):
  falling=falling*(n+r-j+1)%p
  v=(v+comb(n+j,j)*falling)%p
 return v

answers=[]
for p in (127,151):
 expected={c['residue']:c for c in source[p]['complete_classes']}
 assert set(expected)==set(range(p)) and source[p]['all_residues_good']
 fac=[1]
 for j in range(1,p):fac.append(fac[-1]*j%p)
 invfac=[pow(x,-1,p) for x in fac]
 exponential=[sum(invfac[:j+1])%p for j in range(p)]
 rows=[]
 for residue in range(p):
  positive=residue<=(p-1)//2
  k=residue if positive else p-1-residue
  old=expected[residue]
  assert old['k']==k and old['branch']==('positive' if positive else 'negative')
  if k==0:
   D,E=1,1;C=[1];mh=None;jets=None
  else:
   D,C,mh=matrix_seed(k,k if positive else -k-1,p,fac,invfac)
   assert D
   assert D==old['D']
   assert C==old['matrix_certificate']['cofactor_values_gamma_i']
   if positive:
    B=[(-1)**(k-j)*comb(k,j)*C[j]%p for j in range(k+1)]
    U=[fac[k+j]*B[j]%p for j in range(k+1)]
    S=convolution(U,[comb(k,j//2)%p if j%2==0 else 0 for j in range(2*k+1)],p)
    Q=[0]*(2*k+1)
    for d in range(k,3*k+1):Q[3*k-d]=comb(d,k)*S[d]%p
    E=sum(Q[j]*exponential[2*k-j] for j in range(2*k+1))%p
    assert B==old['scaled_B']
    jets=None
   else:
    r=p-k-1
    low=[(-1)**(r-i)*comb(r,i)*C[i]%p for i in range(k+1)]
    high=[sum(comb(r,u)*rise(r+i+1,2*u,p)*low[i+2*u] for u in range((k-i)//2+1))%p for i in range(k+1)]
    jets=[fac[h]*sum(comb(r+i,r+h)*high[i] for i in range(h,k+1))%p for h in range(k+1)]
    assert jets[0]==D and jets==old['J']
    poly=[sum(jets[h]*invfac[h]*comb(h,j)*(-1)**(h-j) for h in range(j,k+1))%p for j in range(k+1)]
    E=sum(poly[j]*border(r,j,p) for j in range(k+1))%p
  assert D==old['D'] and E==old['E'] and D and E
  ratio=E*pow(D,-1,p)%p
  assert ratio==old['endpoint_over_V1']
  rows.append(dict(residue=residue,k=k,branch=old['branch'],D=D,C=C,E=E,ratio=ratio,J=jets,JT_hash=mh,all_values_match=True))
 answers.append(dict(p=p,all_residues_good=True,count=len(rows),rows=rows))
 print('Independent PASS',p,'all',len(rows),'residues',flush=True)
out=base/'uniform_127_151_root_certificate.json'
out.write_text(json.dumps(dict(scope='Only all residues for127and151, independent root JT recurrence/solve and original endpoints',source_sha256=hashlib.sha256(data).hexdigest(),all_checks_pass=True,results=answers),indent=2)+'\n')
print('Saved',out)
