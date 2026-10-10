"""Generic local determinant identities and the single n=1 boundary control."""
import sys, json
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE/'math_packages'))
import sympy as s

rows = [s.Matrix(1,3,s.symbols(f'j{i}_0:3')) for i in range(5)]
def det(i,j,k):
    return rows[i].col_join(rows[j]).col_join(rows[k]).det()
V=det(1,2,3); w0=det(0,1,2); w1=det(0,1,3)
w2=det(0,2,3)+det(0,1,4)
cramer=V*rows[0]-det(0,2,3)*rows[1]+w1*rows[2]-w0*rows[3]
assert all(s.expand(v)==0 for v in cramer)
plucker=V*det(0,1,4)-w1*det(1,2,4)+w0*det(1,3,4)
assert s.expand(plucker)==0
bezout=V**2*rows[0]-(V*w2-w1*det(1,2,4)+w0*det(1,3,4))*rows[1]+V*w1*rows[2]-V*w0*rows[3]
assert all(s.expand(v)==0 for v in bezout)

z=s.symbols('z');D=1+z*z
A=14-19*z;B=-14+16*z;C=17-9*z
N=s.Matrix([[D*D*A,B,C],
 [D*D*s.diff(A,z)+D*C,B+s.diff(B,z),s.diff(C,z)],
 [D*D*s.diff(A,z,2)+2*D*s.diff(C,z)-s.diff(D,z)*C,
  B+2*s.diff(B,z)+s.diff(B,z,2),s.diff(C,z,2)]]).det()
Q=s.cancel(N/z**2).expand()
fder={r:s.diff(1/D,z,r-1).subs(z,1) for r in range(1,6)}
J=[]
for r in range(6):
    aa=s.diff(A,z,r).subs(z,1)+sum(s.binomial(r,j)*s.diff(C,z,r-j).subs(z,1)*fder[j] for j in range(1,r+1))
    bb=sum(s.binomial(r,j)*s.diff(B,z,j).subs(z,1) for j in range(r+1))
    J.append([aa,bb,s.diff(C,z,r).subs(z,1)])
E=-8*s.Matrix(J[1:4]).det()
assert E.is_Integer
carrier=[Q.subs(z,1),s.diff(Q,z).subs(z,1),s.diff(Q,z,2).subs(z,1)/2]
assert s.gcd_list(carrier)==12
q3=Q.coeff(z,3)
full=carrier+[E+12*q3]
out={'scope':'Universal symbolic five-row identities and exactly the n=1 endpoint-matched line; no prime or degree scan.',
     'status':'pass','generic_Cramer':'pass','generic_Plucker':'pass',
     'generic_quadratic_Bezout':'pass',
     'n1':{'Q':str(Q),'E':str(E),'carrier':[str(v) for v in carrier],
           'carrier_gcd':str(s.gcd_list(carrier)),'fourth_entry':str(full[-1]),
           'four_entry_gcd':str(s.gcd_list(full))}}
(HERE/'raw_endpoint_local_classification_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
