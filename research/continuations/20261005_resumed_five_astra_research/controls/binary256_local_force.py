from pathlib import Path
from math import comb,factorial
from fractions import Fraction as F
import json,hashlib
MOD=256;ROOT=Path(__file__).resolve().parent
U={1:-1,2:2,3:-3,4:3};square={}
for i,a in U.items():
 for j,b in U.items():square[i+j]=square.get(i+j,0)+comb(i+j,i)*a*b
assert all(v%2==0 for v in square.values())
V=[square[i]//2 for i in range(2,9)];assert V==[1,-6,24,-75,180,-315,315]
f=[1]
for a in range(1,10):f.append(f[-1]*(209+a)%MOD)
assert f==[1,210,22,56,152,16,112,128,128,0]
B=[sum(f[u]*comb(644,u-a) for u in range(a,9))%MOD for a in range(9)]
beta=[sum((-1)**a*B[a]*comb(a,k-1) for a in range(k-1,9))%MOD for k in range(1,10)]
assert B==[197,234,54,56,248,208,112,128,128]
assert beta==[113,202,78,200,248,80,240,128,128]
negative=[]
for s in range(-10,0):
 k=-s;c=beta[k-1] if 1<=k<=9 else 0
 slope=(c+(beta[k-2] if 2<=k<=10 else 0))%MOD
 negative.append({'s':s,'constant':c,'x_coefficient_except_xZ0_at_minus1':slope,'plus_xZ0':s==-1})
def fall(a,k):
 v=1
 for i in range(k):v*=a-i
 return v
def odd_mod(x):
 assert x.denominator%2==1
 return x.numerator*pow(x.denominator,-1,MOD)%MOD
states=[]
for z in range(8):
 h=161+256*z;n=2*h;central=[]
 for ell in range(11):
  j=ell//2
  if ell%2:
   pref=fall(h,j+1)
   for t in range(j+1):pref*=2*h+2*t+1
   val=sum((F(2**s*factorial(s)**2,factorial(2*s+1))*comb(h-j-1,s)*comb(h+j,s) for s in range(10)),F(0))*pref
  else:
   pref=fall(h,j)
   for t in range(1,j+1):pref*=2*h+2*t-1
   val=sum((F(2**s*factorial(s)**2,factorial(2*s))*comb(h-j,s)*comb(h+j,s) for s in range(10)),F(0))*pref
  central.append(odd_mod(val))
 force=[]
 for i in range(18):
  val=0
  for ell in range(min(i,10)+1):
   prod=1
   for t in range(ell+1,i+1):prod*=n+t
   val+=comb(i,ell)*prod*central[ell]
  force.append(val%MOD)
 assert [v%64 for v in force[:8]]==[2,9,51,57,12,36,48,16]
 assert all(v%64==0 for v in force[8:])
 states.append({'h0':h,'n0':n,'central_mod256':central,'forcing_mod256':force,'signed_Newton_mod256':[((-1)**i*v)%MOD for i,v in enumerate(force)]})
rec={'status':'EXACT_BOUNDED_PASS','scope':'Complete bounded central and first forcing inputs at8 auxiliary h states, plus local exterior and contact-polynomial prerequisites. Infinite tail and original transfer rely on A5 turn1 proofs, not this finite arithmetic. No finite contact inverse, joint norm-mixed sum, higher-binomial contraction or denominator claim.','source':'A5 resumed turn1 sections3-10; exact central formula A5 prior turn20 equations2.1/2.2 and3.1','modulus':MOD,'U_square_div2':V,'exterior_factorial':f,'exterior_B':B,'exterior_beta':beta,'negative_coefficients':negative,'states':states,'old_mod64_reduction_pass':True,'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(ROOT/'binary256_local_force_certificate.json').write_text(json.dumps(rec,indent=2)+'\n')
print(json.dumps({'status':rec['status'],'states':states,'negative':negative},indent=2))
