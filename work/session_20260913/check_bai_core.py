from fractions import Fraction as F
from bisect import bisect_right
from pathlib import Path
import sympy as sy, mpmath as mp, json, hashlib
out=Path(__file__).parent
# Exact verification of the full periodic set for the selected integer triple.
a,b,c=1857,3714,5570;d=3715
intervals=[]
for j in range(1,372,2):intervals.append((F(j,b),F(3*j+1,2*c)))
for j in range(2,1115,2):intervals.append((F(j,b),F(3*j,2*c)))
for j in range(373,1856,2):intervals.append((F(j,b),F(2*j+1,2*d)))
for j in range(1116,1857,2):intervals.append((F(j,b),F(2*j+1,2*d)))
for j in range(1859,3714,2):intervals.append((F(j,b),F(3*j-1,2*c)))
intervals.sort();starts=[x for x,y in intervals]
assert len(intervals)==2784 and all(x<y for x,y in intervals)
assert all(y<=u for (x,y),(u,v) in zip(intervals,intervals[1:]))
assert sum((y-x for x,y in intervals),F())==F(1724689,13797510)
frac=lambda x:x-x.numerator//x.denominator
def actual(u):return frac(a*u+F(1,2))+2*frac(b*u)<frac(c*u)
def listed(u):
 i=bisect_right(starts,u)-1
 return i>=0 and u<intervals[i][1]
breaks=sorted(set([F(0),F(1)]+[F(j,b) for j in range(1,b)]+[F(j,c) for j in range(1,c)]+[F(2*j+1,2*d) for j in range(d)]))
for u in breaks[:-1]:assert actual(u)==listed(u),('endpoint',u)
for u,v in zip(breaks,breaks[1:]):assert actual((u+v)/2)==listed((u+v)/2),('interval',u,v)
# Exact independent reconstruction of the phase-derivative numerator.
e,l,u=sy.symbols('eta l u',real=True)
D=1+e**2*(1-l)**2
Kr=25*(1-e**2)+l*(25*e**2+24*e+7);Ki=-50*e+l*(18*e+24)
H=sy.expand(Kr**2+Ki**2)
J=(25+3*l)**2+(-25*e*(1-l)-4*l)**2
alpha=sy.Rational(a,c);beta=sy.Rational(b,c)
P=sy.expand(2*alpha*(1-l)*D*H*J-2*beta*l*D*H*J+beta*l*(1-l)*D*sy.diff(H,l)*J-l*(1-l)*D*H*sy.diff(J,l)+(1-alpha-2*beta)*l*(1-l)*sy.diff(D,l)*H*J)
Q=sy.cancel(P*sy.Rational(557,125)/(1+e**2));assert sy.denom(Q)==1
pol=sy.Poly(Q,l);Cs=[sy.expand(sum(pol.nth(j)*sy.binomial(6-j,k-j) for j in range(k+1))) for k in range(7)]
expected=[1160625*(e**2+1)**3,-175*(26528*e-26529)*(e**2+1)**2,2*(e**2+1)*(2212607*e**2-3795652*e+3126443),8*(418731*e**3+420703*e**2+923835*e-500369),-128*(14851*e**2-143914*e+168053),512*(15784*e-43639),-7606272]
assert all(sy.expand(x-y)==0 for x,y in zip(Cs,expected))
# Exact Bernstein bounds on e in [9/10,1] certify every coefficient sign.
x=sy.symbols('x');signs=[]
for k,Ck in enumerate(Cs):
 p=sy.Poly(sy.expand(Ck.subs(e,sy.Rational(9,10)+x/10)),x);n=p.degree()
 bern=[sum(p.nth(j)*sy.binomial(i,j)/sy.binomial(n,j) for j in range(i+1)) for i in range(n+1)]
 if min(bern)>0:signs.append(1)
 elif max(bern)<0:signs.append(-1)
 else:raise AssertionError(('sign not certified',k,bern))
assert signs==[1,1,1,1,-1,-1,-1]
# Independent high precision reproduction; these floating evaluations are diagnostics.
mp.mp.dps=70
m=lambda f:mp.mpf(f.numerator)/f.denominator
omega=mp.fsum(mp.digamma(m(y))-mp.digamma(m(x)) for x,y in intervals)
C=(7430-4645*mp.log(2)-omega)/5570
rho=mp.findroot(lambda y:3715*y**3-232119*y**2-928475*y-1160625,66)
z=(mp.sqrt(rho)-5)/(mp.sqrt(rho)+5)
r=(mp.log(25)+3716*mp.log(2)+3714*mp.log(1+z)+3714*mp.log(2+6*z+9*z*z+6*z**3+2*z**4)-7430*mp.log(1-z)-5570*mp.log(z))/5570
my=mp.mpf(232125)/(743*rho);mA=mp.mpf(706242355200)/(552049*(rho*rho+6*rho+25));mJ=mp.mpf(22280000)/(743*(rho-25))
s=mp.mpf(a)/(2*c)*mp.log(my)+mp.mpf(b)/(2*c)*mp.log(mA)-mp.log(mJ)/2
sigma=r+C;tau=-s-C
sigold=mp.mpf('11.613890045331')/3;tauold=mp.mpf('1.90291648559998')/3
h=mp.mpf('2.3246783391437311');dd=mp.mpf('2.3370623743589730');muold=mp.mpf('7.1032053341370017');munew=1+sigma/tau
vals=dict(omega=omega,C=C,r=r,s=s,sigma=sigma,tau=tau,mu=munew,approximation_exponent=1+tau/sigma,matching_content_threshold=(sigma-tau)/2,relative_content_threshold=(sigma-tau)/(2*sigma),old_pi_content_ceiling=h-dd/muold,new_pi_content_ceiling=h-dd/munew,ceiling_improvement=dd*(1/munew-1/muold),new_safe_escape_scale=1/(mp.mpf('7.102')+1),new_safe_cancellation_scale=2/mp.mpf('7.102'))
report={'status':'bounded independent verification, not full proof certification','exact_periodic_cells':len(breaks)-1,'exact_periodic_endpoint_checks':len(breaks)-1,'interval_count':len(intervals),'exact_phase_polynomial_identity':True,'exact_uniform_Bernstein_coefficient_signs':signs,'floating_diagnostics':{k:mp.nstr(v,50) for k,v in vals.items()},'source_sha256':{name:hashlib.sha256((out/name).read_bytes()).hexdigest() for name in ['bai_2609.11276.pdf','zeilberger_zudilin_1912.06345.pdf']}}
(out/'bai_core_checks.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
