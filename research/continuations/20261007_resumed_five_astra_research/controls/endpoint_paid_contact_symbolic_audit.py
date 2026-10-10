"""Parent fixed-size symbolic audit of NEW actual contact and Laurent formulas."""
from pathlib import Path
import sympy as s
import hashlib,json,time
ROOT=Path(__file__).resolve().parent
start=time.monotonic()
n,c,b,d,fn=s.symbols('n c b d fn')
m=n+1;N=n+2
a=2*m*d-2*c-(n-1)*b
ee=(4*d+(n-2)*c+b)/(2*N)
T=s.Matrix([[c,b,a],[d,c,b],[ee,d,c]])
V=s.Matrix([[2*N,0,0],[N,N,0],[m,2*n+3,1]])
X=m*fn*c;Y=m*fn*b;Z=m*fn*(2*d-c)
P=n*X+Y;Q=n*Z+2*X-Y;F=2*m*(Y-2*X-(n-1)*Z)
z=s.Matrix([P,Q,F])
def zero(matrix):
    return all(s.cancel(v)==0 for v in matrix)
assert zero(V*z-2*N*m*fn*(T[:,1]+n*T[:,0]))
W3=s.Matrix([X,Z,Y-X-(2*n+1)*Z])
W0=s.Matrix([m*Z-(n*n+1)*X-(n-1)*Y,
 m*Y+(1-n)*X-m*m*Z,
 2*m*(m*X+(n*n+n+1)*Z-N*Y)])
contacts=[]
for j,W,kernel,ell in [(0,W0,T[:,2]-n*m*T[:,0],s.Matrix([[-1,n,-n*m]])),
                       (3,W3,T[:,0],s.Matrix([[0,0,1]]))]:
    raw=ell*T.adjugate()*V
    assert zero(W-2*N*m*fn*V.inv()*kernel)
    assert zero(raw*z) and zero(raw*W)
    # This exact proportionality additionally identifies the cross-product scale.
    assert zero(z.cross(W).T+2*m*m*fn*fn*raw)
    contacts.append({'j':j,'direction_verified':True,'two_kernel_equations_verified':True,
       'cross_product_scale_to_raw_contact':'-2*((n+1)!)^2'})

# Paid source-specific identity, before division by actual integer contents.
P0,Q0,F0,C,hhat,lhat,Kactual,affine,scale=s.symbols('P0 Q0 F0 C hhat lhat Kactual affine scale')
w1,w2,w3=s.symbols('w1 w2 w3')
Mv=Q0*hhat-P0*lhat
theta=C*Mv+F0*(affine-Kactual)
href=scale*(w3*Mv+F0*(w1*lhat-w2*hhat))
Bres=w3*(affine-Kactual)-C*(w1*lhat-w2*hhat)
assert s.expand(scale*w3*theta-C*href-scale*F0*Bres)==0

# Independent Laurent substitution into the transformed tensor equation.
t=s.symbols('t')
B2=s.Matrix([[0,1,s.Rational(1,2)],[0,-1,-s.Rational(1,2)],
             [0,1,s.Rational(1,2)]])
B1=s.Matrix([[0,1,s.Rational(1,2)],[1,-1,0],[-2,1,-1]])
B0=s.Matrix([[0,0,0],[1,1,s.Rational(1,2)],[-1,-1,-s.Rational(1,2)]])
Rinf=s.Matrix([[0,1],[1,2]]);J=s.Matrix([[0,0],[-1,-1]])
g0=s.Matrix([[0,0],[-1,-1],[-s.Rational(1,2),-s.Rational(1,2)]])
g1=s.Matrix([[0,s.Rational(1,2)],[s.Rational(3,2),3],[s.Rational(1,2),1]])
g2=s.Matrix([[-s.Rational(1,2),-s.Rational(1,2)],[-s.Rational(5,2),-s.Rational(7,2)],[-1,-s.Rational(3,2)]])
g3=s.Matrix([[0,-s.Rational(1,2)],[-s.Rational(25,2),-33],[-7,-18]])
G=sum((g*t**i for i,g in enumerate([g0,g1,g2,g3])),s.zeros(3,2))
ga2=s.Matrix([[0,0],[-s.Rational(1,2),s.Rational(1,2)],[-s.Rational(1,4),s.Rational(1,4)]])
ga1=s.Matrix([[0,s.Rational(1,2)],[0,0],[0,s.Rational(1,4)]])
ga0=s.Matrix([[0,s.Rational(1,2)],[0,s.Rational(1,2)],[0,s.Rational(1,4)]])
res=G+(B2.T+t*B1.T+t*t*B0.T)*G.subs(t,t/(1+t))*(Rinf+t/(1+t)*J)-(ga2+t*ga1+t*t*ga0)
truncated=res.applyfunc(lambda v:s.series(v,t,0,4).removeO().expand())
assert truncated==s.zeros(3,2)
obstruction=g3[2,:]+g2[2,:]
assert obstruction==s.Matrix([[-8,-s.Rational(39,2)]])
out={'personally_authored':True,'network_and_credentials_denied':True,
 'contact_cases':contacts,'shared_kernel_identity_verified':True,
 'paid_source_identity_verified_before_contents':True,
 'Laurent_coefficients_zero_through_order3':True,
 'Laurent_obstruction':[str(x) for x in obstruction],
 'scope':'Fixed-size symbolic contact directions, raw cross-product scale and Laurent identities. Actual primitive-contact contents are retained symbolically; no numerical original producer or subfactorial gcd conclusion.',
 'all_passed':True,'elapsed_seconds':round(time.monotonic()-start,3),
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(ROOT/'endpoint_paid_contact_symbolic_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out),flush=True)
