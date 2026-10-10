"""Independent original-system control n=3 -> 4 and local exceptional controls."""
import sys, json
from pathlib import Path
from math import factorial, comb
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'math_packages'))
import sympy as s
z=s.symbols('z');D=1+z*z
def clean(a):return s.cancel(a)
def ff(k):return s.Rational(1,factorial(k)) if k>=0 else s.S.Zero
def tau(k):return s.Rational((-1)**((k-1)//2),k) if k>0 and k%2 else s.S.Zero
def original(n):
    rows=[[ff(k-j) for j in range(n+1)]+[tau(k-j) for j in range(n+1)]
          for k in range(n+1,3*n+1)]
    rows += [[-4]*(n+1)+[1]*(n+1),[1]*(n+1)+[0]*(n+1)]
    sol=s.Matrix(rows).inv()*s.Matrix([0]*(2*n+1)+[1])
    B=sum(sol[j]*z**j for j in range(n+1))
    C=sum(sol[n+1+j]*z**j for j in range(n+1))
    A=-sum(sum(sol[j]*ff(k-j)+sol[n+1+j]*tau(k-j)
               for j in range(n+1))*z**k for k in range(n+1))
    return list(map(s.expand,(A,B,C)))
def gauge(A,B,C):
    return s.Matrix([[D**2*A,B,C],
        [D**2*s.diff(A,z)+D*C,B+s.diff(B,z),s.diff(C,z)],
        [D**2*s.diff(A,z,2)+2*D*s.diff(C,z)-s.diff(D,z)*C,
         B+2*s.diff(B,z)+s.diff(B,z,2),s.diff(C,z,2)]])
n=3;old=original(n);new=original(n+1)
K=gauge(*old);Kn=gauge(*new)
Q=clean(K.det()/z**(3*n-1))
assert s.degree(Q,z)==3 and s.degree(s.gcd(Q,z*D*s.diff(Q,z)),z)==0
base=s.Matrix([[-2*s.diff(D,z)/D,0,0],[0,1,0],[D,0,0]])
comp=((K.diff(z)+K*base)*K.inv()).applyfunc(clean)
A3=z*D*Q
aco=[clean(-comp[2,j]*A3) for j in range(3)]+[A3]
A0,A1,A2,A3=aco
# Derive the origin series in Euler form, independently of the author's
# polynomial residual recurrence and without copying the actual high series.
bc=[clean(z*A2/A3),clean(z*z*A1/A3),clean(z**3*A0/A3)]
bc=[[s.series(f,z,0,8).removeO().expand().coeff(z,j) for j in range(8)] for f in bc]
M=3*n+1;u=[s.S.One]
for r in range(1,8):
    num=sum(((M+r-j)*(M+r-j-1)*bc[0][j]+(M+r-j)*bc[1][j]+bc[2][j])*u[r-j]
            for j in range(1,r+1))
    u.append(clean(-num/((M+r)*(M+r-1)*r)))
A,B,C=old
def rc(k):
    return A.coeff(z,k)+sum(B.coeff(z,j)*ff(k-j)+C.coeff(z,j)*tau(k-j) for j in range(n+1))
assert all(clean(u[r]-rc(M+r)/rc(M))==0 for r in range(8))
variables=s.symbols('v:20')
N=[sum(variables[j]*z**j for j in range(6)),
   sum(variables[6+j]*z**j for j in range(7)),
   sum(variables[13+j]*z**j for j in range(7))]
eq=[]
for f in (s.diff(A3,z)*N[0]+A0*N[2],s.diff(A3,z)*N[1]+A1*N[2]):
    rem=s.rem(f,Q,z).expand()
    eq.extend(rem.coeff(z,k) for k in range(3))
for f in (N[2],N[1]-s.diff(N[2],z)):
    rem=s.rem(f,D,z).expand()
    eq.extend(rem.coeff(z,k) for k in range(2))
f=sum(u[r]*z**(M+r) for r in range(5))
nf=s.expand(sum(N[j]*s.diff(f,z,j) for j in range(3)))
eq.extend(nf.coeff(z,k) for k in range(M-2,M+3))
eq += [N[0].coeff(z,5)+n*N[1].coeff(z,6),
       N[1].coeff(z,6)+N[2].coeff(z,6),
       N[0].coeff(z,5)+N[1].coeff(z,5)+N[2].coeff(z,5)+n*N[1].coeff(z,6)+2*n*N[2].coeff(z,6)]
H,_=s.linear_eq_to_matrix(eq,variables)
assert H.shape==(18,20) and H.rank()==18
uj=[sum(comb(j,r)*s.diff(B,z,r).subs(z,1) for r in range(j+1)) for j in range(6)]
cj=[s.diff(C,z,j).subs(z,1) for j in range(6)]
assert Q.subs(z,1)!=0
eq += [sum(N[j].subs(z,1)*uj[j] for j in range(3))-Q.subs(z,1),
       sum(N[j].subs(z,1)*cj[j] for j in range(3))-4*Q.subs(z,1)]
mat,rhs=s.linear_eq_to_matrix(eq,variables)
sol=mat.inv()*rhs
Ns=[s.expand(f.subs(dict(zip(variables,sol)))) for f in N]
true=(Kn*K.inv()).applyfunc(clean)
assert all(clean(Ns[j]/Q-true[0,j])==0 for j in range(3))
# The two-dimensional homogeneous nullspace really consists of unmatched
# next Taylor triples, checked directly rather than by comparing one solution.
for v in H.nullspace():
    ns=[s.expand(f.subs(dict(zip(variables,v)))) for f in N]
    chat=clean(sum(ns[j]*s.diff(C,z,j) for j in range(3))/Q)
    bhat=clean(sum(ns[j]*sum(comb(j,r)*s.diff(B,z,r) for r in range(j+1)) for j in range(3))/Q)
    ahat=clean((ns[0]*D**2*A+ns[1]*(D**2*s.diff(A,z)+D*C)+ns[2]*(D**2*s.diff(A,z,2)+2*D*s.diff(C,z)-s.diff(D,z)*C))/(D**2*Q))
    assert all(not s.denom(f).has(z) and s.degree(f,z)<=n+1 for f in (ahat,bhat,chat))
    assert all(ahat.coeff(z,k)+sum(bhat.coeff(z,j)*ff(k-j)+chat.coeff(z,j)*tau(k-j) for j in range(n+2))==0 for k in range(3*n+4))
# Synthetic regular-singular exceptional-origin germ: orders 1,3,M,
# whose Wronskian defect is h=3. This checks only the local identities,
# and is not presented as an exceptional member of the actual raw family.
ys=[z,z**3,z**M*s.exp(z)]
wm=s.Matrix([[s.diff(y,z,j) for y in ys] for j in range(3)])
co=(-(s.Matrix([[s.diff(y,z,3) for y in ys]]))*wm.inv()).applyfunc(clean)
bb=[clean(z*co[0,2]),clean(z*z*co[0,1]),clean(z**3*co[0,0])]
const=[s.limit(f,z,0) for f in bb]
t=s.symbols('t')
ind=s.expand(t*(t-1)*(t-2)+const[0]*t*(t-1)+const[1]*t+const[2])
assert s.factor(ind)==(t-1)*(t-3)*(t-M)
wj=clean(wm.det()/s.exp(z))
assert min(k[0] for k,v in s.Poly(wj,z).terms())==3*n+2
v=[s.S.One]
series=[[s.series(f,z,0,8).removeO().expand().coeff(z,j) for j in range(8)] for f in bb]
for r in range(1,8):
    num=sum(((M+r-j)*(M+r-j-1)*series[0][j]+(M+r-j)*series[1][j]+series[2][j])*v[r-j] for j in range(1,r+1))
    v.append(clean(-num/((M+r-1)*(M+r-3)*r)))
assert v==[ff(j) for j in range(8)]
# Synthetic simple apparent point: local columns exp(x),1,x^3,
# N=(0,-1,1), Q=x. The quotient endpoint derivative formula agrees
# with direct analytic continuation for U=exp(x), C=1+2x^3.
x=s.symbols('x')
for y in (s.exp(x),1+2*x**3):
    num=s.diff(y,x,2)-s.diff(y,x)
    assert num.subs(x,0)==0
    assert s.limit(num/x,x,0)==s.diff(num,x).subs(x,0)
result={'status':'PASS','actual_control':'n3 -> n4 from two original Taylor/endpoint solves',
 'origin_relative_coefficients_checked':8,'homogeneous_rank':18,'square_rank':20,
 'matches_original_next_triple':True,'both_homogeneous_basis_images_checked':True,
 'synthetic_exceptional_origin_orders':[1,3,M],'synthetic_origin_defect':3,
 'synthetic_simple_endpoint_quotient_identity':True,
 'scope':'Synthetic local controls are not asserted to be actual exceptional raw-family degrees.'}
(HERE/'raw_generic_independent_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
