"""One existing actual pair: nonmonic compact diagonal and exact index factors."""
from math import factorial,gcd,lcm,prod
from pathlib import Path
import json
import sympy as sp
OUT=Path(__file__).resolve().parent
k=5;y=sp.symbols('y')
def d(r):
    n=2*r
    return sum((-1)**j*factorial(n)//factorial(j) for j in range(n+1))
def f(r):return factorial(2*r)
def gg(r):return d(r)+d(r+1)
def kk(r):return -f(r)-f(r+1)+sp.Rational(4,2*r+1)
def cc(r):return d(r)-(-1)**r
def rr(r):return -f(r)+sum((sp.Rational(4*(-1)**(r-a),2*a-1) for a in range(1,r+1)),sp.Integer(0))
def ell(i):
    return sum((-1)**(i-r)*sp.binomial(2*i,i-r)*sp.binomial(2*i+2*r,2*i)*y**r for r in range(i+1))
def basis(n):return sp.Matrix(n,n,lambda i,j:ell(i).coeff(y,j))
def delta(n):return prod(int(sp.binomial(4*i,2*i)) for i in range(n))
def moment(P,fn):
    return sum((c*fn(int(r[0])) for r,c in sp.Poly(P,y).terms()),sp.Integer(0))
def mgcd(v):
    ans=0
    for x in v:ans=gcd(ans,int(x))
    return abs(ans)
L=lcm(*range(1,6*k-4,2))
C=sp.Matrix(k,2*k,lambda i,j:cc(i+j))
R=sp.Matrix(k,2*k,lambda i,j:rr(i+j))
V=sp.Matrix(k,2*k,lambda i,j:(-1)**(i+j))
N=sp.Matrix(k,2*k-1,lambda i,j:gg(i+j)).col_join(sp.Matrix(k,2*k-1,lambda i,j:L*kk(i+j)))
W=C.col_join(sp.Matrix(k-1,2*k,lambda i,j:L*kk(i+j)))
Tk,Tkm,Tn,Tw=basis(k),basis(k-1),basis(2*k-1),basis(2*k)
AN=sp.diag(Tk,Tk);BN=Tn.T
AW=sp.diag(Tk,Tkm);BW=Tw.T
Np=AN*N*BN;Wp=AW*W*BW
assert all(T.det()==delta(T.rows) for T in [Tk,Tkm,Tn,Tw])
checks=0
for i in range(k):
    for j in range(2*k-1):
        poly=ell(i)*ell(j)
        om=sp.Rational(4*16**i,4*i+1) if i==j else 0
        assert moment(poly,lambda r:sp.Rational(4,2*r+1))==om
        assert Np[i,j]==moment((y+1)*poly,d)
        assert Np[k+i,j]==L*(-moment((y+1)*poly,f)+om)
        checks+=3
for i in range(k):
    for j in range(2*k):
        assert Wp[i,j]==moment(ell(i)*ell(j),d)-ell(i).subs(y,-1)*ell(j).subs(y,-1)
        checks+=1
for i in range(k-1):
    for j in range(2*k):
        om=sp.Rational(4*16**i,4*i+1) if i==j else 0
        assert Wp[k+i,j]==L*(-moment((y+1)*ell(i)*ell(j),f)+om)
        checks+=1
old=json.loads((OUT/'SHORT_STACK_JOINT_CONTENT_RECEIPT.json').read_text())
hn,hw=int(old['h_N']),int(old['h_W'])
w=sp.Matrix([(-1)**i*int(N.extract([r for r in range(2*k) if r!=i],range(2*k-1)).det())//hn for i in range(2*k)])
z=sp.Matrix([(-1)**j*int(W.extract(range(2*k-1),[c for c in range(2*k) if c!=j]).det())//hw for j in range(2*k)])
assert mgcd(w)==mgcd(z)==1
assert N.T*w==sp.zeros(2*k-1,1) and W*z==sp.zeros(2*k-1,1)
thetaN=mgcd(AN.adjugate().T*w)
thetaW=mgcd(BW.adjugate()*z)
assert delta(k)**2%thetaN==0 and delta(2*k)%thetaW==0
hnp=mgcd([Np.extract([r for r in range(2*k) if r!=i],range(2*k-1)).det() for i in range(2*k)])
hwp=mgcd([Wp.extract(range(2*k-1),[c for c in range(2*k) if c!=j]).det() for j in range(2*k)])
assert hnp==delta(2*k-1)*hn*thetaN
assert hwp==delta(k)*delta(k-1)*hw*thetaW
M=C.col_join(L*R)
I0=int(M.det());I1=int(C.col_join(L*(R+V)).det())-I0
Dpair=delta(k)**2*delta(2*k)
assert int((AN*M*BW).det())==Dpair*I0
assert int((AN*C.col_join(L*(R+V))*BW).det())-Dpair*I0==Dpair*I1
q=abs(Dpair*I1)//gcd(Dpair*I0,Dpair*I1)
assert str(q)==old['actual_q']
out={
 'purpose':'new complete compact/index identities at one existing pair; no atlas or content growth claim',
 'k':k,'complete_entry_and_compact_checks':checks,
 'Delta_k':str(delta(k)),'Delta_2k_minus_1':str(delta(2*k-1)),'Delta_2k':str(delta(2*k)),
 'theta_N':str(thetaN),'theta_W':str(thetaW),
 'h_N_transformed':str(hnp),'h_W_transformed':str(hwp),
 'full_pair_basis_factor':str(Dpair),'actual_q_bits':q.bit_length(),
 'exact_content_index_identities_checked':True,'full_physical_primitive_pair_invariant':True,
 'all_assertions_passed':True,
}
(OUT/'SHORT_STACK_COMPACT_DIAGONAL_RECEIPT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({key:out[key] for key in ['k','complete_entry_and_compact_checks','theta_N','theta_W','actual_q_bits','all_assertions_passed']}))
