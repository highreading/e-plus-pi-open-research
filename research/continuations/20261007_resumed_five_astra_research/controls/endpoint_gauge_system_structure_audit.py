"""Parent structural exact audit of the new homogenized rational-gauge system."""
from pathlib import Path
import sympy as s
import json,hashlib,time
ROOT=Path(__file__).resolve().parent;start=time.monotonic();n=s.symbols('n')
U=s.Matrix([[0,(n+1)*(n+2),(n+2)/2],
 [n+2,-(n*n+3*n+1),-n*(n+2)/(2*(n+1))],
 [-(n+2)*(2*n+3),(n+2)*(n*n+3*n+1),(n+2)*(n*n-2)/(2*(n+1))]])
RR=s.Matrix([[0,1],[(n+1)/(n+2),(2*n+3)/(n+2)]])
K=s.kronecker_product(U,RR)
KI=s.kronecker_product(U.inv(),RR.inv()).applyfunc(s.cancel)
gamma=s.Matrix([[0,(n+2)/2,-(n+1)**2/2,((n+1)**2+1)/2,
                 -(n+1)/4,(n*n+3*n+3)/(4*(n+1))]])
N=s.zeros(7);NI=s.zeros(7)
N[:6,:6]=-(n+1)**2*KI.T;N[:6,6]=KI.T*gamma.T;N[6,6]=1
NI[:6,:6]=-K.T/(n+1)**2;NI[:6,6]=gamma.T/(n+1)**2;NI[6,6]=1
N=N.applyfunc(s.cancel);NI=NI.applyfunc(s.cancel)
assert (N*NI-s.eye(7)).applyfunc(s.cancel)==s.zeros(7)
assert (KI*K-s.eye(6)).applyfunc(s.cancel)==s.zeros(6)
def structure(M):
    denominator=s.Poly(1,n)
    for value in M:
        if value:denominator=s.lcm(denominator,s.Poly(s.denom(value),n))
    numerators=[s.Poly(s.cancel(denominator.as_expr()*value),n) for value in M if value]
    gcd=numerators[0]
    for p in numerators[1:]:gcd=s.gcd(gcd,p)
    return {'denominator_lcm':str(s.factor(denominator.monic().as_expr())),
            'matrix_content_up_to_nonzero_rational_unit':str(s.factor(gcd.as_expr()/denominator.as_expr())),
            'denominator_factors':[[str(f.as_expr()),e] for f,e in s.factor_list(denominator)[1]]}
shiftNI=NI.subs(n,n-1).applyfunc(s.cancel)
out={'scope':'Exact homogenization, inverse and polynomial denominator structure. These entry-denominator lcms are NOT yet universal solution denominator bounds or a proof of rational-gauge existence/nonexistence.',
 'equation':'ell(n+1) K(n)+(n+1)^2 ell(n)=gamma(n); Y=(ell^T,1), Y(n+1)=N(n)Y(n)',
 'det_U':str(s.factor(U.det())),'det_R':str(s.factor(RR.det())),
 'det_N':str(s.factor(N.det())), 'N_structure':structure(N),
 'N_inverse_structure':structure(NI),'shift_minus_one_inverse_structure':structure(shiftNI),
 'inverse_identities_passed':True,'elapsed_seconds':round(time.monotonic()-start,3),
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(ROOT/'endpoint_gauge_system_structure_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out),flush=True)
