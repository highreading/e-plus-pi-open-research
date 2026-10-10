"""Exact fixed-seed arithmetic for the proved candidate residue transfer.
Only degrees 0..6. These are finite theorem inputs, not extrapolations.
"""
from pathlib import Path
from math import factorial,comb,gcd
from functools import reduce
import json
import sympy as s
z=s.symbols('z')
rows=[]
for k in range(7):
 if k==0:
  rows.append(dict(k=0,MD=1,M=[1],b=[1],V=[1],V1=1,Pe1=1,MD_factors={},Pe_factors={}))
  continue
 def a(r):
  if r<0:return s.Integer(0)
  return sum(s.Rational(comb(k,h),factorial(r-2*h)) for h in range(min(k,r//2)+1))
 A=s.Matrix(k+1,k+1,lambda i,j:a(k+i-j))
 HD=reduce(lambda x,j:x*s.Rational(factorial(k+j),factorial(j)),range(k+1),s.Integer(1))
 MD=s.cancel(HD*A.det())
 assert MD.q==1
 Ms=[]
 for j in range(k+1):
  rj=s.Rational(factorial(2*k-j),factorial(j)*factorial(k-j))
  Mj=s.cancel((HD/rj)*A.minor_submatrix(0,j).det())
  assert Mj.q==1
  Ms.append(int(Mj))
 B=[(-1)**(k-j)*comb(k,j)*Ms[k-j] for j in range(k+1)]
 G=reduce(gcd,map(abs,B))
 bc=[b//G for b in B]
 b=sum(c*z**j for j,c in enumerate(bc))
 R=sum(comb(k,h)*s.diff(z**k*b,z,2*h) for h in range(k+1))
 V,rem=s.div(R,(z-1)**k,z)
 assert rem==0
 vc=[int(s.Poly(V,z).nth(j)) for j in range(k+1)]
 assert all(s.Poly(V,z).nth(j).q==1 for j in range(k+1))
 V1=sum(vc)
 assert V1==MD/G
 def D(r):return sum(comb(k+j,j)*factorial(k+r)//factorial(k+r-j) for j in range(k+r+1))
 Pe=sum(c*D(j) for j,c in enumerate(vc))
 # Independent integral reconstruction for Pe, using exact monomial moments.
 integ=s.Poly(s.expand(z**k*(1+z)**k*V.subs(z,1+z)),z)
 Pe2=sum(c*factorial(mon[0]) for mon,c in integ.terms())/factorial(k)
 assert Pe2==Pe
 rows.append(dict(k=k,MD=int(MD),M=Ms,b=bc,V=vc,V1=V1,Pe1=int(Pe),MD_factors={str(p):int(v) for p,v in s.factorint(abs(int(MD))).items()},Pe_factors={str(p):int(v) for p,v in s.factorint(abs(Pe)).items()}))
 print(k,'MD',MD,'V1',V1,'Pe',Pe,flush=True)
p=Path(__file__).with_name('small_residue_exact_seeds.json')
p.write_text(json.dumps({'scope':'Fixed degrees 0..6 as inputs to residue-transfer theorem; all arithmetic exact; every identity asserted.', 'seeds':rows},indent=2)+'\n')
print('Saved',p)
