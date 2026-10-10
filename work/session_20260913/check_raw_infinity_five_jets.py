"""Fixed-size infinity matrices and all-q five-coefficient cutoff controls."""
import json
import sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'math_packages'))
import sympy as s
z,x=s.symbols('z x');D=1+z*z
def Kmat(A,B,C):
    return s.Matrix([[D*D*A,B,C],
        [D*D*s.diff(A,z)+D*C,B+s.diff(B,z),s.diff(C,z)],
        [D*D*s.diff(A,z,2)+2*D*s.diff(C,z)-s.diff(D,z)*C,
         B+2*s.diff(B,z)+s.diff(B,z,2),s.diff(C,z,2)]])
def falling(a,j):return s.prod(a-r for r in range(j))
def jets(poly):return s.Matrix([s.expand(poly).coeff(x,r) for r in range(5)])
def matrix(coeff,n,shift):
    return s.Matrix(5,5,lambda r,t:sum(
        s.expand(a).coeff(z,shift+j-(r-t))*falling(n-t,j)
        if shift+j-(r-t)>=0 else 0 for j,a in enumerate(coeff)) if t<=r else 0)
saved=json.loads((HERE/'raw_rational_transfer_checks.json').read_text())['steps']
triples={1:[7-s.Rational(19,2)*z,-7+8*z,s.Rational(17,2)-s.Rational(9,2)*z],
         3:[s.sympify(p) for p in saved[1]['next_triple']]}
out={'scope':'Two original-family infinity controls plus all-q cutoff identities','actual_cases':[]}
for n,(A,B,C) in triples.items():
    K=Kmat(A,B,C);Q=s.cancel(K.det()/z**(3*n-1));q=s.degree(Q,z)
    base=s.Matrix([[-2*s.diff(D,z)/D,0,0],[0,1,0],[D,0,0]])
    conn=((K.diff(z)+K*base)*K.inv()).applyfunc(s.cancel)
    A3=s.expand(z*D*Q)
    coeff=[s.cancel(-conn[2,j]*A3) for j in range(3)]+[A3]
    expcoeff=[s.expand(sum(s.binomial(j,k)*coeff[j] for j in range(k,4))) for k in range(4)]
    Ma=matrix(coeff,n,q+1);Me=matrix(expcoeff,n,q+2)
    assert len(Ma.nullspace())==2 and len(Me.nullspace())==1
    F=s.expand(x**n*C.subs(z,1/x))
    H=s.series(x**n*A.subs(z,1/x)-F*s.atan(x),x,0,5).removeO()
    G=s.expand(x**n*B.subs(z,1/x))
    assert Ma*jets(F)==s.zeros(5,1) and Ma*jets(H)==s.zeros(5,1)
    assert s.Matrix.hstack(jets(F),jets(H)).rank()==2
    assert Me*jets(G)==s.zeros(5,1)
    trial=sum((r+1)*x**r for r in range(5));y=s.expand(z**n*trial.subs(x,1/z))
    La=s.expand(sum(coeff[j]*s.diff(y,z,j) for j in range(4))/z**(n+q+1))
    Le=s.expand(sum(expcoeff[j]*s.diff(y,z,j) for j in range(4))/z**(n+q+2))
    assert jets(s.expand(La.subs(z,1/x)))==Ma*jets(trial)
    assert jets(s.expand(Le.subs(z,1/x)))==Me*jets(trial)
    out['actual_cases'].append({'n':n,'q':int(q),'algebraic_rank':3,'exponential_rank':4,
        'actual_Laurent_plane_matches':True,'actual_exponential_line_matches':True,
        'operator_conjugations_match':True})

# Symbolic leading-polynomial factorizations do not depend on q.
nn,ss,bb,cc,dd,lead=s.symbols('n s b c d lead')
Ia=-lead*(nn-ss)*(nn-ss-1)+(cc+dd-1)*lead*(nn-ss)-cc*dd*lead
assert s.expand(Ia+lead*(ss-(nn-cc))*(ss-(nn-dd)))==0
assert s.expand(lead*(nn-ss)-bb*lead-lead*(nn-bb-ss))==0

# For each allowed q, compare a true germ and its first five coefficients.
n=7
Ns=[1+2*z**5+3*z**6,-2+z**4-z**6,z+z**6]
Nexp=[s.expand(sum(s.binomial(j,k)*Ns[j] for j in range(k,3))) for k in range(3)]
cutoff=[]
for q in range(4):
    for germ,op in [(1/(1-x),Ns),(x**4/(1+x),Ns),(x**3/(1-x),Nexp)]:
        trunc=s.series(germ,x,0,5).removeO()
        full=z**n*germ.subs(x,1/z);short=z**n*trunc.subs(x,1/z)
        diff=s.cancel(sum(op[j]*s.diff(full-short,z,j) for j in range(3))/z**(n+6))
        coeffs=s.series(diff.subs(z,1/x),x,0,5).removeO().expand()
        assert all(coeffs.coeff(x,r)==0 for r in range(5-q))
    cutoff.append({'q':q,'tested_excess_coefficient_count':5-q,'passed':True})
out['all_q_cutoff_controls']=cutoff;out['status']='passed'
(HERE/'raw_infinity_five_jet_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print('Five-jet infinity kernels n=1,3; symbolic indicial identities; and all-q cutoff controls passed.')
