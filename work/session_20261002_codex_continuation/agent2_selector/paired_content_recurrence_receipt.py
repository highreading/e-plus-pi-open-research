"""Bounded exact normalization checks for the all-degree recurrence/carry proof."""
from fractions import Fraction as F
from math import factorial,comb,gcd,lcm
from pathlib import Path
import json
ROOT=Path(__file__).parent

def v2(x):
 if not x:return 10**9
 z=0
 while x%2==0:z+=1;x//=2
 return z

def vf(m):return m-m.bit_count()
def md(a):
 m=0
 while vf(2*m)<a:m+=1
 d=0
 while 2+d+vf(d)<a:d+=1
 return m,d

def beta(r):return -F(factorial(2*r))+4*sum((F((-1)**j,2*r-2*j-1) for j in range(r)),F(0))

def poly_mul(x,y):
 z=[0]*(len(x)+len(y)-1)
 for i,a in enumerate(x):
  for j,b in enumerate(y):z[i+j]+=a*b
 return z

def shiftpoly(m,d,plus):
 z=[0]*m+[1]
 for _ in range(d):z=poly_mul(z,[-1,1])
 if plus:z=poly_mul(z,[1,1])
 return z

def val(x):return v2(x.numerator)-v2(x.denominator)
rec=[]
for a in range(1,11):
 m,d=md(a)
 for isD in [False,True]:
  annih=shiftpoly(m,0 if a<=2 else d,False if a<=2 else not isD)
  for q in [[1],[1,-3,2],[2,0,-1,5]]:
   qp=poly_mul(q,[1,2,1]) if isD else q
   full=poly_mul(annih,qp)
   for s in range(15):
    z=sum((c*beta(s+i) for i,c in enumerate(full)),F(0))
    assert val(z)>=a,(a,isD,q,s,z)
  rec.append({'a':a,'D_moment':isD,'m':m,'d':d,'annihilator_coefficients':annih,'starts_verified':15,'integer_weight_polynomials_verified':3})
carry=[]
n=9;M=4*n-3;L=lcm(*(j for j in range(1,M+1,2)))
for p in [3,5,7]:
 a=0;P=1
 while L%(P*p)==0:a+=1;P*=p
 ell=(L//P)%p
 for r in range(2*n):
  K=sum(((-1)**(r-(P*u+1)//2)*pow(u,-1,p) for u in range(1,p,2) if P*u<=2*r-1),0)%p
  actual=L*beta(r);assert actual.denominator==1
  assert actual.numerator%p==4*ell*K%p,(p,a,r,actual,K)
 carry.append({'n':n,'prime':p,'highest_denominator_depth':a,'all_beta_indices_verified':list(range(2*n))})
out={'status':'PASS_EXACT_RECURRENCE_AND_CARRIED_SIGN_NORMALIZATION','scope':'Bounded formula receipt; all-degree claims are proved in the authored theorem. No new degree or prime atlas.','recurrences':rec,'odd_top_carries':carry}
(ROOT/'PAIRED_CONTENT_RECURRENCE_RECEIPT.json').write_text(json.dumps(out,indent=2)+'\n')
print(out['status'],len(rec),'recurrence interfaces',len(carry),'carry interfaces')
