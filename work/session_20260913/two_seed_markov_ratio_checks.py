"""Closed exact control: actual N=4 ratio, plus stabilization of its first five tail moments."""
from pathlib import Path
import sys,json
sys.path.insert(0,str(Path(__file__).parent/'math_packages'))
import sympy as S
z=S.symbols('z')
def a(k): return S.Integer(k)**2/S.sqrt(4*k*k-1)
def matrix(N):
    A=S.zeros(N)
    for j in range(N):
        A[j,j]=(a(j)**2 if j else 0)+a(j+1)**2-j*(j+1)
        for k in range(j+1,min(j+3,N)):
            A[j,k]=A[k,j]=a(k) if k==j+1 else a(k-1)*a(k)
    return A
K=matrix(4);A=K[1:,1:];e=S.eye(3)[:,0];v=e+a(2)*S.eye(3)[:,1]
D=S.factor((z*S.eye(3)-A).det())
Q=S.factor((v.T*(z*S.eye(3)-A).adjugate()*e)[0])
assert S.expand(D-(1323*z**3+11697*z**2+18284*z-13168)/1323)==0
assert S.expand(Q-(315*z**2+2932*z+6576)/315)==0
assert S.gcd(D,Q)==1
assert S.gcd(D,K.charpoly(z).as_expr())==1
pole_intervals=[(-7,-6),(-3,-2),(0,1)]
zero_intervals=[(-6,-5),(-4,-3)]
for f,iv in [(D,pole_intervals),(Q,zero_intervals)]:
    assert all(f.subs(z,l)*f.subs(z,r)<0 for l,r in iv)
    assert sum(S.Poly(f,z).count_roots(l,r) for l,r in iv)==S.degree(f,z)
m=[S.simplify((v.T*A**j*e)[0]) for j in range(5)]
H=S.Matrix(3,3,lambda i,j:m[i+j])
assert H.det()==-S.Rational(400592896,2701125)
# For moments through order four, all paths from index 1 to indices 1 or 2 stay below 6.
# This is one fixed formal-moment check, not a degree/prime scan.
T=matrix(6)[1:,1:]; e6=S.eye(5)[:,0];v6=e6+a(2)*S.eye(5)[:,1]
stable=[S.simplify((v6.T*T**j*e6)[0]) for j in range(5)]
stable_det=S.factor(S.Matrix(3,3,lambda i,j:stable[i+j]).det())
assert stable_det==S.Rational(117256192,471625)
out={'scope':'actual N=4 counterexample only; separate stabilized moments do not extend its sign',
     'ratio_numerator':str(Q),'ratio_denominator':str(D),
     'pole_intervals':pole_intervals,'zero_intervals':zero_intervals,
     'residue_signs':['+','-','+'],'moments_N4':[str(x) for x in m],
     'Hankel3_N4':str(H.det()),'stable_moments_N_ge_6':[str(x) for x in stable],
     'stable_Hankel3':str(stable_det),'status':'pass'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
