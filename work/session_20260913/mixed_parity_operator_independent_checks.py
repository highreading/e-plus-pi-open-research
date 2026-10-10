"""All-parameter operator checks; no polynomial-degree or prime scan."""
from pathlib import Path
import sys,json
sys.path.insert(0,str(Path(__file__).parent/"math_packages"))
import sympy as S
x,z,m,lam=S.symbols("x z m lambda")
a=S.Function("a")(x)
def compose(p,q):
    out={}
    for i,pi in p.items():
        for j,qj in q.items():
            for k in range(i+1):
                out[i+j-k]=out.get(i+j-k,0)+pi*S.binomial(i,k)*S.diff(qj,x,k)
    return {j:S.expand(v) for j,v in out.items()}
L={4:x*x,3:4*x,2:x*x+2,1:2*x}
A={1:S.Integer(1),0:a}
left=compose(A,L)
ta2=x*x+6-2*a*x-4*x*x*S.diff(a,x)
ta1=4*x-4*a+2*a*a*x+4*x*x*a*S.diff(a,x)-18*x*S.diff(a,x)-6*x*x*S.diff(a,x,2)
right=compose({4:x*x,3:6*x,2:ta2,1:ta1},A)
for j in (5,4,3,2):
    assert S.simplify(left.get(j,0)-right.get(j,0))==0
required=S.diff(ta2,x)+ta2/x-6/x
defect=x+2*a*a*x+4*x*x*a*S.diff(a,x)-4*x*S.diff(a,x)-2*x*x*S.diff(a,x,2)
assert S.simplify(ta1-required-defect)==0
assert S.expand(defect.subs(a,-lam*x/2).doit()).coeff(x,1)==1+2*lam

ss=S.sin(x)/x
factor={1:S.Integer(1)}
for p in ({0:1/ss},{1:S.Integer(1)},{0:x*x*ss*ss},
          {1:S.Integer(1)},{0:1/ss},{1:S.Integer(1)}):
    factor=compose(factor,p)
for j in range(5):
    assert S.simplify(S.trigsimp(factor.get(j,0)-L.get(j,0)))==0

Ak=lambda k:k*k*(k-1)**2/(2*(2*k-1))
mass=4*m*m*(12*m*m-1)/(16*m*m-1)
assert S.factor(Ak(2*m+1)-Ak(2*m)-mass)==0

# Formal all-r indicial identities, after the telescoping product quotient.
r=S.symbols("r",integer=True,positive=True)
t=z+r
indicial=[]
for sig in (0,1):
    p=S.cancel((t-sig-2*r)/(t-sig)*t*t*(t-1)**2)
    expected=(z-r)*(z+r)*(z+r-1)**2 if sig==0 else (z-r-1)*(z+r)**2*(z+r-1)
    assert S.factor(p-expected)==0
    indicial.append(str(S.factor(p)))
out={"scope":"symbolic all-parameter operator identities; no new degree controls",
     "r1_intertwiner_coefficients":"pass","r1_formal_weight_defect":"pass",
     "positive_factorization":"pass","stieltjes_first_moment":"pass",
     "indicial_polynomials":indicial,"status":"pass"}
Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))
