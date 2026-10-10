"""New general-pole exact moments and complete primitive polynomial receipt."""
from pathlib import Path
from math import factorial,comb,prod,lcm,gcd
import sympy as sp
import mpmath as mp
import json

ROOT=Path(__file__).resolve().parent
y,w,T=sp.symbols('y w T')
D=[1]
for n in range(1,90):D.append(n*D[-1]+(-1)**n)
df=lambda d:prod(range(1,2*d,2))
cm=lambda m:sp.Rational(2**(m+1)*factorial(m-1),df(m-1))
def jets(m):
 d=m-1
 return [sp.Rational(2**j*comb(d,j)*df(d-j),df(d)) for j in range(m)]
def nu(m,r):return (-1)**r*sp.rf(sp.Rational(1,2)-r,m-1)/sp.rf(sp.Rational(1,2),m-1)
def oldmass(m):return sum((sp.Rational(2*factorial(h-2),df(h-1)) for h in range(2,m+1)),sp.Integer(0))
def moment(m,r):
 q,rem=sp.div(y**r,(1+y)**m)
 remw=sp.expand(rem.subs(y,w-1))
 coeff=[remw.coeff(w,m-h) for h in range(1,m+1)]
 ratpoly=sum((q.coeff(y,j)/sp.Integer(2*j+1) for j in range(int(sp.degree(q,y))+1)),sp.Integer(0)) if q else 0
 aa=cm(m)*(ratpoly+sum((coeff[h-1]*oldmass(h)/cm(h) for h in range(1,m+1)),sp.Integer(0)))
 vv=cm(m)*sum((coeff[h-1]/cm(h) for h in range(1,m+1)),sp.Integer(0))
 assert vv==nu(m,r)
 return aa
mp.mp.dps=1000
rows=[]
cases=[(3,3),(3,6),(3,8),(4,4),(4,7),(5,5),(5,7),(6,6),(7,7)]
for m,k in cases:
 d=m-1;dd=df(d);cs=jets(m)
 for j,c in enumerate(cs):assert sp.Rational(1,factorial(j))<=c<=sp.Rational(2**j,factorial(j))
 alpha=[moment(m,r) for r in range(3*k-1)]
 for r in range(len(alpha)-m):
  assert sum(comb(m,j)*alpha[r+j] for j in range(m+1))==cm(m)/sp.Integer(2*r+1)
 for r in range(3*k-1):
  assert sum((cs[j]*sp.ff(r,j)*(-1)**(r-j) for j in range(min(r,d)+1)),sp.Integer(0))==nu(m,r)
 A=lcm(*(int(nu(m,r).q) for r in range(m)))
 assert A==int(cm(m).q)
 bound=lcm(*range(1,2*d+1))
 assert bound%A==0
 C=sp.Matrix(k,2*k,lambda i,j:D[2*(i+j)]-nu(m,i+j))
 R=sp.Matrix(k,2*k,lambda i,j:alpha[i+j]-factorial(2*(i+j)))
 V=sp.Matrix(k,2*k,lambda i,j:nu(m,i+j))
 assert C.rank()==k and V.rank()==m
 vals=[C.col_join(R+t*V).det() for t in range(m+2)]
 polynomial=sp.Poly(sp.interpolate(list(enumerate(vals[:m+1])),T),T)
 assert polynomial.eval(m+1)==vals[m+1] and polynomial.degree()==m
 bs=[polynomial.nth(j) for j in range(m+1)]
 top=max(1,6*k-2*m-3);L=lcm(*range(1,top+1,2));clear=dd**(2*k)*L**k
 ints=[int(clear*b) for b in bs];assert all(sp.Integer(a)==clear*b for a,b in zip(ints,bs))
 F=lambda n:prod(factorial(j) for j in range(n))
 divs=[2**(k*(k-1))*dd**(k-m+j)*L**j*F(k-m+j)**2 for j in range(m+1)]
 assert all(a%v==0 for a,v in zip(ints,divs))
 g=gcd(*ints);pp=[a//g for a in ints]
 if pp[-1]<0:pp=[-a for a in pp]
 B=A;Lm=lcm(*range(1,m+1));L6=lcm(*range(1,6*k+1))
 E=B*2**(3*m+2)*Lm*L6;compact_clear=B**k*E**k
 assert all(E*z==sp.Integer(E*z) for z in alpha)
 alternative=[int(compact_clear*b) for b in bs]
 assert all(compact_clear*b==a for a,b in zip(alternative,bs))
 ag=gcd(*alternative);ap=[a//ag for a in alternative]
 if ap[-1]<0:ap=[-a for a in ap]
 assert ap==pp
 altdivs=[2**(k*(k-1))*B**(k-m+j)*(E//B)**j*F(k-m+j)**2 for j in range(m+1)]
 assert all(a%v==0 for a,v in zip(alternative,altdivs))
 J=sp.Matrix(m,m,lambda i,j:comb(i+j,i)*cs[i+j] if i+j<=d else 0)
 kap=sp.Rational(2**d*factorial(d),dd)
 assert J.det()==(-1)**(m*(m-1)//2)*kap**m/sp.Integer(F(m)**2)
 full=sum(mp.mpf(a)*(mp.e+mp.pi)**j for j,a in enumerate(pp))
 rows.append({'m':m,'k':k,'normalized_weight':str(cm(m)),'jet_coefficients':list(map(str,cs)),
 'least_universal_period_clearer':str(A),'jet_matrix_determinant':str(J.det()),'actual_degree':polynomial.degree(),
 'formal_stack_clearer':str(clear),'full_content':str(g),'primitive_coefficients':list(map(str,pp)),
 'exponential_cost_moment_clearer':str(E),'exponential_cost_stack_clearer':str(compact_clear),
 'alternative_full_content':str(ag),'exact_alternative_primitive_polynomial_match':True,
 'primitive_height_bits':max(abs(a).bit_length() for a in pp),'coefficient_forced_divisors':list(map(str,divs)),
 'diagnostic_log_abs_primitive_evaluation':mp.nstr(mp.log(abs(full)),35),'exact_moment_rank_jet_clearer_content_checks':True})
 print('GENERAL_POLE',m,k,'heightbits',rows[-1]['primitive_height_bits'],'log_form',mp.nstr(mp.log(abs(full)),12),flush=True)
(ROOT/'GENERAL_POLE_SHORT_STACK_CERTIFICATE.json').write_text(json.dumps({'status':'PASS_NEW_GENERAL_RANK_M_PERIOD_INTERFACE','rows':rows,'scope':'Bounded exact general-pole moments/ranks/jet determinants/response clearers/complete primitive content. Finite evaluations are diagnostics, not main proof or an infinite rate.'},indent=2)+'\n')
