import sys,json
sys.path.insert(0,'[private local path removed]')
import sympy as s
from pathlib import Path
out=Path(__file__).resolve().parent
w,u=s.symbols('w u'); a=(1+s.I)/2
n,h=4,1
V=w*w-w+s.Rational(1,2); G=1-2*w*w+4*w**4-8*w**6
base=(2*V)**n*G**h/(w**(n+1)*(1-w)**(4*h))

def exact_parts(F):
    F=s.cancel(F)
    c0=s.series(s.cancel(F*w**(n+1)),w,0,n+1).removeO().expand()
    c1=s.series(s.cancel(F.subs(w,1+u)*u**(4*h)),u,0,4*h).removeO().expand()
    p0={j:s.expand(c0).coeff(w,n+1-j) for j in range(1,n+2)}
    p1={j:s.expand(c1).coeff(u,4*h-j) for j in range(1,4*h+1)}
    num,den=s.fraction(F)
    q,r=s.div(num,den,w)
    reconstruction=q+sum(c*w**(-j) for j,c in p0.items())+sum(c*(w-1)**(-j) for j,c in p1.items())
    assert s.cancel(F-reconstruction)==0
    P=s.integrate(q,w)+sum(c*w**(1-j)/(1-j) for j,c in p0.items() if j>1)+sum(c*(w-1)**(1-j)/(1-j) for j,c in p1.items() if j>1)
    E0=sum(c/s.factorial(j-1) for j,c in p0.items()); E1=sum(c/s.factorial(j-1) for j,c in p1.items())
    R=p0[1]-p1[1]
    ImP=s.simplify((P.subs(w,a)-P.subs(w,s.conjugate(a)))/(2*s.I))
    return {'E0':s.factor(E0),'E1':s.factor(E1),'R':s.factor(R),'ImP':ImP,'pole0':p0,'pole1':p1,'polynomial':q}

d0=exact_parts(base);d1=exact_parts(w*base)
T=s.factorial(4*h-1)
m0=s.factor(T*(d0['E1']-d0['R']));m1=s.factor(T*(d1['E1']-d1['R']))
matched=s.cancel(m1*base-m0*w*base)
dm=exact_parts(matched)
assert dm['E1']==dm['R']!=0
c=s.factor((-dm['E0']-4*dm['ImP'])/dm['R'])
raw=s.factor(-d0['E0']/d0['E1']-4*d0['ImP']/d0['R'])
payload={'parameters':{'n':n,'h':h},'target':'one new exact test of the period-compatible F,wF projection; not a uniform claim',
'F0':{k:str(v) for k,v in d0.items()},'F1':{k:str(v) for k,v in d1.items()},
'integer_projection_coefficients':[str(m0),str(m1)],'matched':{k:str(v) for k,v in dm.items()},
'actual_center':str(c),'actual_q':str(s.denom(c)),'raw_same_kernel_center':str(raw),'raw_actual_q':str(s.denom(raw)),
'conclusion':'The period-compatible projection is nonzero in this new exact example and changes the actual center. No asymptotic denominator gain is proved.'}
(out/'rational_period_projection_n4_h1.json').write_text(json.dumps(payload,indent=2)+'\n')
print(json.dumps(payload,indent=2))
