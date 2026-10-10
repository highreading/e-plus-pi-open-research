from pathlib import Path
from math import gcd,lcm,factorial
import json
import sympy as sp
ROOT=Path(__file__).parent
X,d,F=sp.symbols('X d F')
z=list(map(sp.sympify,json.loads((ROOT/'SHIFTED_COMPRESSION_SYMBOLIC_RECEIPT.json').read_text())['reduced_cofactor_polynomials']))
P=[sp.Integer(1)];QQ=[sp.Integer(0)]
for j in range(1,11):
 P.append(sp.expand((X+j)*P[-1]));QQ.append(sp.expand((X+j)*QQ[-1]+(-1)**j))
Gamma=[sp.expand(sum(z[t]*P[2*(s+t)] for t in range(4))) for s in range(3)]
assert all(sp.degree(t,d)<=2 for t in Gamma)
qminus=sp.expand(sum((-1)**j*z[j] for j in range(4)))
delta=sp.prod(X+2*a+1 for a in range(5))
h=[4*sum((sp.Rational((-1)**(r-1-a),1)/(X+2*a+1) for a in range(r)),sp.Integer(0)) for r in range(6)]
R0=[sp.cancel(-F*Gamma[s]+sum(z[t]*h[s+t] for t in range(4))) for s in range(3)]
T=[sp.expand(sp.cancel(delta*t)) for t in R0]
a0=sp.expand(T[0]*T[2]-T[1]**2)
b0=sp.expand(delta*qminus*(T[0]+2*T[1]+T[2]))
deg=lambda t:max(i+j for i,j,l in sp.Poly(t,F,d,X).monoms())
assert deg(a0)<=6 and deg(b0)<=6
print('EXACT_GAMMA_D_DEGREES',[sp.degree(t,d) for t in Gamma],flush=True)
print('PAIR_FD_DEGREES',deg(a0),deg(b0),flush=True)
gform=sp.factor(sp.gcd(a0,b0))
print('GENERIC_CLEARED_PAIR_GCD',gform,flush=True)
M=8;xx=2*M;dd=1
for j in range(1,xx+1):dd=j*dd+(-1)**j
ff=factorial(xx);sub={X:xx,d:dd,F:ff}
vv=list(map(int,[t.subs(sub) for t in z]));gg=gcd(*vv);primitive=[t//gg for t in vv]
row=next(t for t in json.loads((ROOT.parent/'main/SHIFTED_PAIRED_DERANGEMENT_CERTIFICATE.json').read_text())['rows'] if t['k']==2 and t['M']==M)
assert primitive==list(map(int,row['primitive_integer_polynomial']))
l=-sp.Integer(factorial(2*M))+4*sum((sp.Rational((-1)**a,2*M-2*a-1) for a in range(M)),sp.Integer(0))
# beta_M includes the large factorial.  Formula(1)'s old logarithmic mass
# must be L_M = beta_M + X!, which the exact normalization below retains.
logmass=l+ff
p=int(logmass.p);a=int(logmass.q)
av=int(a0.subs(sub));bv=int(b0.subs(sub))
actualq=abs(a*bv)//gcd(a*av+p*bv,a*bv)
assert actualq==int(row['actual_q'])
record={'status':'PASS_NEW_COMPRESSED_FULL_PAIR','n':3,'Gamma_d_degrees':[sp.degree(t,d) for t in Gamma],'pair_Fd_degrees':[deg(a0),deg(b0)],'generic_cleared_pair_gcd':str(gform),'cofactor_numerical_gcd_at_M8':gg,'normalization_reference_M':M,'actual_q_matches_complete_root_receipt':True,'scope':'One symbolic actual-pair content identity and one exact existing normalization interface; no finite degree/prime atlas.'}
(ROOT/'SHIFTED_COMPRESSION_PAIR_RECEIPT.json').write_text(json.dumps(record,indent=2,default=int)+'\n')
