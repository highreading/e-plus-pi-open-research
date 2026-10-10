"""Author examples for the exponential-gauged primitive endpoint and mod-p carry cancellation."""
from pathlib import Path
from fractions import Fraction as Q
from math import factorial,comb,gcd,lcm
import json,hashlib
SESSION=Path('work/session_20261002_codex_continuation')
certpath=SESSION/'main/EXPLICIT_DEGREE61_RADIUS198_CERTIFICATE.json'
raw=certpath.read_bytes();K=json.loads(raw)['endpoint_basis_integers']
d=len(K)+1
P=[Q(0)]*(d+1);P[1]=Q(1)
for k,v in enumerate(K,1):P[k]+=Q(v,factorial(k));P[k+1]-=Q(v,factorial(k))
pj=[int(v*factorial(k)) for k,v in enumerate(P)]
Qjets=[2]+[sum(comb(j,k)*pj[k]*pj[j-k] for k in range(max(0,j-d),min(d,j)+1))-(2*pj[j] if j<=d else 0) for j in range(1,2*d+1)]
N=420;G=[0];u=[0];D=[1];B=[1]
for n in range(1,N+1):
 num=(4*pj[n] if n<=d else 0)-sum(comb(n-1,k)*Qjets[k]*G[n-k] for k in range(1,min(2*d,n-1)+1))
 assert num%2==0
 G.append(num//2);assert G[-1]%2==0
 u.append(sum(comb(n,j)*(-1)**(n-j)*G[j] for j in range(n+1)))
 D.append(n*D[-1]+(-1)**n);B.append(n*B[-1]+u[-1])
 assert B[-1]==factorial(n)+sum(comb(n,j)*G[j]*D[n-j] for j in range(n+1))
 if n%2==0:assert D[-1]%2==1 and B[-1]%2==0
supportden=lcm(*(v.denominator for v in P))
ps=[]
for p in range(61,200):
 if any(p%q==0 for q in range(2,int(p**.5)+1)):continue
 assert supportden%p
 assert all(v%p==0 for v in G[p+1:])
 roots=[]
 for r in range(p):
  if D[r]%p==0:roots.append({'r':r,'residue':(B[r]-factorial(r))%p})
 for n in range(p,N+1):
  a,r=divmod(n,p)
  assert D[n]%p==(-1)**a*D[r]%p
  expected=((-1)**a*(B[r]-factorial(r))+a*(-1)**(a-1)*G[p]*D[r])%p
  assert B[n]%p==expected
  if r==1:assert B[n]%p==(-1)**a*2%p
 ps.append({'p':p,'derangement_roots':roots,'p_jet_residue':G[p]%p,'checks_n':[p,N]})
rows=[]
for n in (20,40,61,80,120,180,240,320,420):
 h=gcd(D[n],B[n]);q=D[n]//h
 rows.append({'n':n,'D_n':str(D[n]),'B_n':str(B[n]),'actual_gcd':str(h),'actual_q':str(q),'q_digits':len(str(q)),'v2_q':0 if q%2 else None})
out={'status':'PASS_EXACT_NEW_GAUGED_ENDPOINT_AND_CARRY_IDENTITIES','scope':'New arithmetic identities for fixed degree61; no new analytic-radius audit and no uniform gcd-rate theorem','source_sha256':hashlib.sha256(raw).hexdigest(),'N':N,'degree':d,'records':rows,'good_prime_rows':ps}
(SESSION/'main/GAUGED_PULLBACK_ENDPOINT_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS n1..420, primes61..199; records',[(r['n'],r['q_digits']) for r in rows])
