"""Parent-authored symbolic and finite checks of new endpoint lemmas."""
from pathlib import Path
from math import comb, factorial
import sympy as s
import json,hashlib,time
root=Path(__file__).resolve().parent;start=time.monotonic()
n,h,ll,k,q=s.symbols('n h ell k q',integer=True)
def B(kk):return s.Matrix([[2*kk+1,kk*(2*n+1-3*kk)/2,kk*(kk-1)*(kk-n-1)/2],[1,0,0],[0,1,0]])
C=s.Matrix([[1,2*n-3,(2*n-3)*(2*n-5)+(n-2)*(7-n)/2],[0,1,2*n-5],[0,0,1]])
direct=s.Matrix.hstack(s.Matrix([1,0,0]),B(n-2)*s.Matrix([1,0,0]),B(n-2)*B(n-3)*s.Matrix([1,0,0]))
assert (direct-C).applyfunc(s.simplify)==s.zeros(3)
det=s.factor((B(n)*B(n-1)*C).det())
assert s.simplify(det-n*(n-1)**2*(n-2)/2)==0
obs=s.Matrix([[h,-(n+1)*(h+ll)/2,0]])*B(n)*B(n-1)*C
assert s.simplify(obs[0]-((5*n*n-1)*h-(2*n*n+n-1)*ll)/2)==0
z=s.Matrix([1,1,1]);v=s.Matrix([1,2,0])
c0=s.Matrix([q-2,1,1-q]);c3=s.Matrix([1,0,-1])
assert c0.dot(z)==0 and c3.dot(z)==0 and c0.cross(c3)==-z
R0=c0.dot(v);R3=c3.dot(v)
Avec=0;Bvec=k-1-q;Theta=-1+(k-Bvec)
# The report's affine observations include the source response and are not
# contact rows evaluated on the three scalar symbols (A,B,kappa).
# Check its stated complete affine identity using its actual observations.
E0=k-2*q;E3=-1
assert s.simplify(Theta-q)==0
assert s.simplify(R0*E3-R3*E0-(q-k))==0
other0=s.Matrix([1,0,-1]);other3=s.Matrix([1,q,-1-q])
assert other0.cross(other3)==q*z

# Independently construct factorial-normalized phi(z)^r moments through r+1
# by exact divided-power multiplication, then the defined X,Y,Z,F,P values.
parity=[]
for r in range(2,42):
    cap=r+1;lam=[1]+[0]*cap
    for _ in range(r):
        nxt=[]
        for j in range(cap+1):
            val=lam[j]
            if j>=1:val-=j*lam[j-1]
            if j>=2:val+=comb(j,2)*lam[j-2]
            nxt.append(val)
        lam=nxt
    aa=[sum(comb(j,t)*lam[t] for t in range(j+1)) for j in range(cap+1)]
    X=(r+1)*aa[r];Y=(r+1)*r*aa[r-1];Z=2*aa[r+1]-(r+1)*aa[r]
    F=2*(r+1)*(Y-2*X-(r-1)*Z)
    P=r*(r+1)*(aa[r]+aa[r-1]);pivot=2*(2*r+3)*P+3*F
    assert F!=0 and pivot!=0
    if r%2==0:
        assert all(v%2 for v in aa) and F%4==2 and pivot%4==2
    else:assert F%r==(-2)%r
    parity.append({'r':r,'F_mod4':F%4,'P_mod4':P%4,'pivot_mod4':pivot%4,'F_nonzero':F!=0,'pivot_nonzero':pivot!=0})
out={'scope':'Exact symbolic Green response and contact identities;40 auxiliary finite moment checks support but do not replace the symbolic parity proof. No gcd growth or original approximation error is computed.',
     'symbolic_determinant':str(det),'first_green_weight':str(s.factor(obs[0])),
     'full_three_green_weights':[str(s.factor(x)) for x in obs],
     'companion_source_identity':True,'countermodels_checked':True,'parity_cases':parity,
     'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'elapsed_seconds':round(time.monotonic()-start,3)}
(root/'endpoint_green_chart_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'symbolic_identities_passed':True,'auxiliary_parity_cases':len(parity),'seconds':out['elapsed_seconds']}))
