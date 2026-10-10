from pathlib import Path
from math import comb
from functools import lru_cache
import json
p=29; out=Path(__file__).resolve().parent
small=[[comb(a,k)%p if k<=a else 0 for k in range(p)] for a in range(p)]
@lru_cache(None)
def matrix(a,r,weighted=False):
 M=[[0]*6 for _ in range(6)]
 for borrow in range(2):
  for carry in range(3):
   for k in range(p):
    raw=r-k-borrow; j=raw%p; nxt_b=int(raw<0)
    nraw=2*a+j+carry; n=nraw%p; nxt_c=nraw//p
    w=small[a][k]**2*small[n][j]**2
    if weighted:w*=k
    row=3*borrow+carry; col=3*nxt_b+nxt_c
    M[row][col]=(M[row][col]+w)%p
 return M

def mul(v,M):return [sum(v[i]*M[i][j] for i in range(6))%p for j in range(6)]
def digit_sum(H,d):
 A=2001*H+69*d+67; v=[1,0,0,0,0,0]; u=v.copy(); first=True
 while A or H or first:
  a,r=A%p,H%p
  if first:u=mul(u,matrix(a,r,True))
  else:u=mul(u,matrix(a,r))
  v=mul(v,matrix(a,r)); A//=p;H//=p;first=False
 return sum(v[:3])%p,sum(u[:3])%p

def exact_sum(H,d):
 A=2001*H+69*d+67; X=comb(2*A+H,H); T=0;U=0
 for k in range(H+1):
  T=(T+X*X)%(p*p);U=(U+k*X*X)%p
  if k<H:
   num=X*(A-k)*(H-k);den=(k+1)*(2*A+H-k)
   assert num%den==0;X=num//den
 return T,U
checks=0
for H in range(101):
 for d in range(25):
  T,U=exact_sum(H,d);assert digit_sum(H,d)==(T%p,U)
  a=(11*d+9)%p
  if 1<=a<=14 and H%p>=p-a:
   assert T==0 and U==0
  checks+=1
L=p**4; mod=p**6;a0=432827;period=682892;b0=687936
base=pow(3,a0,mod);g=pow(3,period,mod)
assert base%L==b0;assert (g-1)%L==0
z=(g-1)//L;assert z%p!=0
h0=(base-b0)//L;slope=(base*z)%(p*p)
assert slope%p!=0
cells=[]
for d in range(25):
 a=(11*d+9)%p
 if not 1<=a<=14:continue
 for r in range(p-a,p):
  h=d+p*r;t=((h-h0)*pow(slope,-1,p*p))%(p*p)
  b=pow(3,a0+period*t,mod)
  assert (b-b0)//L==h
  cells.append({'d':d,'A_low':a,'H_low':r,'t_mod841':t})
assert len(cells)==100
assert len({v['t_mod841'] for v in cells})==100
receipt={'status':'FINITE_RECURRENCE_AND_REACHABILITY_CHECK_PASS','scope':'The six-state recursion was proved separately by Lucas and checked at the listed finite auxiliary indices. The 100 original exponent classes are exact modulo29^6. Infinite conclusions require the elementary Lucas and order proof in the accompanying coordinator note. No relative-depth or global denominator theorem.','p':p,'recurrence_checks':checks,'auxiliary_H':[0,100],'eligible_d':[0,24],'exponent_base':a0,'exponent_period':period,'h0_mod841':h0,'h_slope_mod841':slope,'g_lift_quotient_mod841':z,'cells':cells}
(out/'residual29_population_certificate.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({k:v for k,v in receipt.items() if k!='cells'},indent=2));print('first cells',cells[:5])
