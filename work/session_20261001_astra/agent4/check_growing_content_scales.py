"""Independent formal arithmetic checks; no HP index or prime scan."""
from pathlib import Path
import json
import sympy as s

OUT=Path('work/session_20261001_astra/agent4')
t,F,rhop,f,G,A,B,wp,wu,ac,bc,sg,c,k=s.symbols('t F rhop f G A B wp wu ac bc sg c k', nonzero=True)
checks={}
J=s.Matrix([[0,-sg,-c],[sg,0,k],[c,-k,0]])
e=s.Matrix([1,0,0]); u=s.Matrix([0,1,0]); p=s.Matrix([0,0,1])
br=lambda v,w:(v.T*J*w)[0]
TP=f*ac*e-f*p
TU=2*f*bc*e/t-2*f*u/t
tr=(A*TU-B*TP)/G
xr=(wp*TU-wu*TP)/G
D=t*B*c-2*A*sg
N=2*wp*sg-t*wu*c+2*f*(sg*ac-c*bc-k)
checks['endpoint_Y']=s.cancel(br(e+tr,e)-f*D/(t*G))==0
checks['endpoint_X']=s.cancel((br(e+tr,xr)-f*N/(t*G)).subs(G,A*wu-B*wp))==0
DP,DU,E=s.symbols('DP DU E')
# Direct endpoint formulas after replacing high rows by integers.
checks['partial_row_Y']=s.cancel((B*br(e,TP)-A*br(e,TU))/G-f*D/(t*G))==0
checks['partial_row_X']=s.cancel((wp*br(e,TU)-wu*br(e,TP)-br(TU,TP))/G-f*N/(t*G))==0
n=s.symbols('n',integer=True,positive=True)
Factual=s.factorial(2*n+1)
Lambda=2**(n+1)*s.factorial(n+2)*Factual*s.factorial(n)**2
M=2**(2*n+3)*Factual**2*rhop
Gactual=(-1)**n*2**(2*n+3)/(n+1)
factual=2**n/s.factorial(n)**2
scale=s.simplify(M/rhop*factual/((n+1)*Gactual))
checks['monic_cleared_scale']=s.simplify(scale-(-1)**n*2**n*Factual**2/s.factorial(n)**2)==0
checks['gcd_rational_scale']=s.simplify((-1)**n*scale/Lambda-Factual/(2*s.factorial(n+2)*s.factorial(n)**4))==0
# Clearing requires t F w integral, F TP and F TU integral.
W1,W2,P1,U1,EP,EU,EE=s.symbols('W1 W2 P1 U1 EP EU EE',integer=True)
cleared_X=t*F**2*(wp*DU-wu*DP-E)
cleared_Y=t*F**2*(B*DP-A*DU)
checks['endpoint_clearer_X']=s.expand(cleared_X.subs({wp:W1/(t*F),wu:W2/(t*F),DU:EU/F,DP:EP/F,E:EE/F**2})-(W1*EU-W2*EP-t*EE))==0
checks['endpoint_clearer_Y']=s.expand(cleared_Y.subs({DP:EP/F,DU:EU/F})-t*F*(B*EP-A*EU))==0
# Formal b=1 and b=2 compatibility; no evaluated degrees.
a,h,j,ka,el=s.symbols('a h j ka el')
high=[a,t*ka,t*el]; ev=[1,1,1]; uv=[0,ka,ka+el]; pv=[0,h,h+j]
checks['b2_sigma']=s.expand(-s.det(s.Matrix([high,ev,uv]))-(t*ka**2-a*el))==0
checks['b2_c']=s.expand(-s.det(s.Matrix([high,ev,pv]))-((t*ka-a)*j-t*(el-ka)*h))==0
checks['b2_kappa']=s.expand(s.det(s.Matrix([high,uv,pv]))-a*(ka*j-el*h))==0
checks['b1_empty_minor']=(-s.det(s.Matrix([[1,1],[0,ka]])),-s.det(s.Matrix([[1,1],[0,h]])),s.det(s.Matrix([[0,ka],[0,h]])))==(-ka,-h,0)
assert all(checks.values()),checks
result={'status':'PASS_FORMAL_ARITHMETIC','checks':checks,'positive_gcd_scale':'(2n+1)!/[2(n+2)!(n!)^4]','scope':'Formal endpoint and scale identities only. All-size integrality and divisibility require the written proof. No rank or asymptotic claim.'}
(OUT/'growing_content_scale_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
