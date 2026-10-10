"""New finite divisor-target tuning of the complete gauged endpoint."""
from pathlib import Path
from fractions import Fraction as Q
from math import factorial,comb,gcd,lcm
import json,hashlib
S=Path('work/session_20261002_codex_continuation')
raw=(S/'main/EXPLICIT_DEGREE81_RADIUS2005_CERTIFICATE.json').read_bytes()
ks=json.loads(raw)['endpoint_basis_integers'];P0=[Q(0)]*82;P0[1]=Q(1)
for j,v in enumerate(ks,1):P0[j]+=Q(v,factorial(j));P0[j+1]-=Q(v,factorial(j))
def full(poly,N):
 d=len(poly)-1;pj=[int(v*factorial(j)) for j,v in enumerate(poly)]
 qq=[2]+[sum(comb(j,a)*pj[a]*pj[j-a] for a in range(max(0,j-d),min(d,j)+1))-(2*pj[j] if j<=d else 0) for j in range(1,min(2*d,N)+1)]
 G=[0];D=[1];B=[1]
 for n in range(1,N+1):
  val=(4*pj[n] if n<=d else 0)-sum(comb(n-1,a)*qq[a]*G[n-a] for a in range(1,min(len(qq)-1,n-1)+1))
  assert val%4==0;G.append(val//2)
  u=sum(comb(n,j)*(-1)**(n-j)*G[j] for j in range(n+1))
  D.append(n*D[-1]+(-1)**n);B.append(n*B[-1]+u)
 return G,D,B
G0,D0,B0=full(P0,322);rows=[]
for N,H in [(160,159),(180,179),(200,199),(320,319),(322,163)]:
 assert N%2==0 and D0[N]%H==0 and H%2==1 and B0[N]%2==0
 K=(-B0[N]//2)%H
 if K>H//2:K-=H
 pp=P0+[Q(0)]*(N+2-len(P0));pp[N]+=Q(K,factorial(N));pp[N+1]-=Q(K,factorial(N))
 G,D,B=full(pp,N)
 assert G[:N]==G0[:N] and G[N]-G0[N]==2*K and B[N]-B0[N]==2*K
 assert sum(pp)==1 and pp[0]==0 and pp[1]==1
 assert abs(K)*3*2**N*401**81<factorial(N)
 A=B0[N]//2;m=(A+K)//H;Qg=D0[N]//H
 assert A+K==m*H and B[N]==2*m*H
 q=Qg//gcd(Qg,m)
 assert q==D[N]//gcd(D[N],B[N])
 beforeden=lcm(*(v.denominator for v in P0));afterden=lcm(*(v.denominator for v in pp))
 rows.append({'N':N,'target_divisor_H':H,'centered_K':K,'grid_denominator_Q':str(Qg),'even_grid_half_numerator_m':str(m),'remaining_grid_content':str(gcd(Qg,m)),
  'old_actual_q':str(D0[N]//gcd(D0[N],B0[N])),'new_actual_q':str(q),'new_actual_gcd':str(gcd(D[N],B[N])),
  'old_good_for_H':gcd(beforeden,H)==1,'new_good_for_H':gcd(afterden,H)==1,'strict_radius_lower':2,'exact_center_shift':{'numerator':str(2*K),'denominator':str(D[N])}})
out={'status':'PASS_EXACT_NEW_GAUGED_DIVISOR_QUANTIZATION','source_sha256':hashlib.sha256(raw).hexdigest(),'rows':rows,'scope':'Full finite endpoint tuning and explicit primitive/grid formula. No global divisor supply, small residue, infinite nonvanishing, or e+pi proof.'}
(S/'main/GAUGED_DIVISOR_QUANTIZATION_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n')
print(out['status'],[(r['N'],r['target_divisor_H'],r['centered_K'],r['old_good_for_H'],r['new_good_for_H']) for r in rows])
