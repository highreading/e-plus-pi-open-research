"""New fixed polynomial amplitude endpoint and carry checks."""
from pathlib import Path
from fractions import Fraction as Q
from math import factorial,comb,gcd
import json,hashlib
S=Path('work/session_20261002_codex_continuation')
raw=(S/'main/EXPLICIT_DEGREE81_RADIUS2005_CERTIFICATE.json').read_bytes()
ks=json.loads(raw)['endpoint_basis_integers'];P=[Q(0)]*82;P[1]=Q(1)
for j,v in enumerate(ks,1):P[j]+=Q(v,factorial(j));P[j+1]-=Q(v,factorial(j))
pj=[int(v*factorial(j)) for j,v in enumerate(P)];d=len(pj)-1;M=420
qq=[2]+[sum(comb(j,a)*pj[a]*pj[j-a] for a in range(max(0,j-d),min(d,j)+1))-(2*pj[j] if j<=d else 0) for j in range(1,2*d+1)]
G,u,D,B,CC=[0],[0],[1],[1],[0]
for n in range(1,M+1):
 val=(4*pj[n] if n<=d else 0)-sum(comb(n-1,a)*qq[a]*G[n-a] for a in range(1,min(2*d,n-1)+1))
 assert val%4==0;G.append(val//2)
 u.append(sum(comb(n,j)*(-1)**(n-j)*G[j] for j in range(n+1)))
 D.append(n*D[-1]+(-1)**n);B.append(n*B[-1]+u[-1]);CC.append(-n*CC[-1]+(-1)**n*G[-1])

rows=[]
for m in range(1,5):
 aa=[(-1)**j*comb(m,j) for j in range(m+1)]
 checked=[]
 for n in range(m,141):
  da=sum(comb(n,j)*factorial(j)*aa[j]*D[n-j] for j in range(m+1))
  ba=sum(comb(n,j)*factorial(j)*aa[j]*B[n-j] for j in range(m+1))
  remainder=sum(comb(m-1,j)*fall for j in range(m) for fall in [factorial(n)//factorial(n-j)])
  jet=sum((-1)**j*comb(m-1,j)*(factorial(n)//factorial(n-j))*u[n-j] for j in range(m))
  assert da==(-1)**n*remainder and ba==jet
  determinant=jet*D[n]-da*B[n]
  for ell in (1,2**n,3**n):
   dd=D[n]+ell*da;bb=B[n]+ell*ba;content=gcd(dd,bb)
   assert determinant%content==0
   if n in (10,50,140):
    checked.append({'N':n,'L_kind': 'one' if ell==1 else ('2_power_N' if ell==2**n else '3_power_N'),'actual_q':str(abs(dd)//content),'actual_content':str(content),'integer_D_remainder':str(remainder),'complete_B_remainder':str(jet)})
 rows.append({'m':m,'new_full_endpoint_checks_to':140,'new_content_checks':3*(141-m),'records':checked})
out={'status':'PASS_ENDPOINT_ZERO_REMAINDER_AND_VARIABLE_WEIGHT_CONTENT','source_sha256':hashlib.sha256(raw).hexdigest(),'rows':rows,'scope':'New exact finite endpoint-zero and varying amplitude receipts, complete final gcd. No uniform primitive denominator gain or main proof.'}
(S/'main/ENDPOINT_ZERO_AMPLITUDE_TRANSITION_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n')
print(out['status'])
