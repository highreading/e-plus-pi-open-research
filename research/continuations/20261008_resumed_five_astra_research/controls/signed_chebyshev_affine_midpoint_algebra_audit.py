"""Parent-authored bounded symbolic audit of the NEW12-step affine evaluator.

No child code executes. Degree<=22 fixed polynomials and formal Bezout
identities are checked; no source normalization, gcd, determinant or q is
recomputed at a numeric research index. This does not prove RRE.
"""
from pathlib import Path
import hashlib,json,time
import sympy as s
OUT=Path(__file__).resolve().parent
started=time.monotonic()
n=s.Symbol('n');alpha,beta,delta,X,Y=s.symbols('alpha beta delta X Y')
w=[1,8,58,168,399,-176,-916,-176,399,168,58,8,1]
r=[s.Integer(1),s.Integer(0)];v=[s.Integer(0),s.Integer(1)];e=[s.Integer(0),s.Integer(0)]
for k in range(1,12):
    r.append(s.expand(r[k-1]+4*(n-k)*r[k]))
    v.append(s.expand(v[k-1]+4*(n-k)*v[k]))
    e.append(s.cancel(e[k-1]+4*(n-k)*e[k]+2/((n-k)**2-1)))
A=s.expand(sum(w[k]*(n-k)*r[k] for k in range(13)))
B=s.expand(sum(w[k]*(n-k)*v[k] for k in range(13)))
E=s.cancel(1359872+sum(w[k]*(n-k)*e[k] for k in range(13)))
Ql=s.prod(n-k for k in range(13))
QE=s.cancel(Ql*E)
PA,PB,PE=s.Poly(A,n,domain=s.ZZ),s.Poly(B,n,domain=s.ZZ),s.Poly(QE,n,domain=s.ZZ)
assert PA.degree()==11 and PB.degree()==12 and PE.degree()<=22
assert PA.LC()==4**10 and PB.LC()==4**11
P=n*alpha**2+(n-2)*beta**2
Q=4*(n-1)*(n-2)*beta**2-2*(n-1)*alpha*beta
T=(alpha+beta)**2-2*delta**2+2*beta**2/n
Delta=s.expand(A*Q-B*P)
expected=-n*B*alpha**2-2*(n-1)*A*alpha*beta-(n-2)*(B-4*(n-1)*A)*beta**2
assert s.expand(Delta-expected)==0
u_scaled=A*X+B*Y+E;v_scaled=P*X+Q*Y+T
res1=s.cancel(Q*u_scaled-B*v_scaled-Delta*X-(Q*E-B*T))
res2=s.cancel(A*v_scaled-P*u_scaled-Delta*Y-(A*T-P*E))
assert res1==0 and res2==0
cleared_T=s.expand(Ql*((alpha+beta)**2-2*delta**2)+2*s.cancel(Ql/n)*beta**2)
assert s.cancel(cleared_T-Ql*T)==0
# Independent fixed polynomial/source check: actual H and its gamma expansion.
t=s.Symbol('t');C=[s.Integer(1),2*t-1]
for j in range(1,6):C.append(s.expand(2*(2*t-1)*C[-1]-C[-2]))
gam=[458,176,-399,-168,-58,-8,-1]
H=t*(1-t)*(1+t*t)**2
assert s.expand(sum(gam[j]*C[j] for j in range(7))-2048*H)==0
mom=[1]
for j in range(1,7):mom.append(1-j*mom[-1])
etaC=[sum(s.Poly(c,t).nth(j)*mom[j] for j in range(7)) for c in C]
assert -2*sum(gam[j]*etaC[j] for j in range(7))==1359872
assert sum(s.Poly(H,t).nth(j)*mom[j] for j in range(7))==-332
def arr(poly):return [int(c) for c in reversed(poly.all_coeffs())]
obj={'all_checks_passed':True,'scope':'Fixed12-step NEW affine source evaluator, exact local denominator and formal Bezout identities only. Does NOT establish determinant sign, midpoint gcd bound, RRE, primitive q or irrationality.',
     'network_or_keys_used':False,'numeric_h_lambda_G_q_recomputed':False,
     'A_coefficients_low_first':arr(PA),'B_coefficients_low_first':arr(PB),
     'Q_local_E_coefficients_low_first':arr(PE),
     'degrees':{'A':PA.degree(),'B':PB.degree(),'Q_local_E':PE.degree()},
     'leading_coefficients':{'A':int(PA.LC()),'B':int(PB.LC())},
     'Q_local_factored':'product(n-k,k=0..12)',
     'exact_zero_Bezout_residuals':[str(res1),str(res2)],
     'determinant_quadratic_identity_verified':True,
     'complete_affine_T_clearer_verified':True,'H_Chebyshev_expansion_verified':True,
     'eta_H':-332,'complete_U_constant':1359872,
     'corrected_source_weights_context':'Positive r! in x=1-t; direct-t moments1-j*mom[j-1] used here.',
     'seconds':round(time.monotonic()-started,3),
     'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(OUT/'signed_chebyshev_affine_midpoint_algebra_certificate.json').write_text(json.dumps(obj,indent=2)+'\n')
print(json.dumps({'checks':True,'degrees':obj['degrees'],'leading':obj['leading_coefficients'],'seconds':obj['seconds']}),flush=True)
