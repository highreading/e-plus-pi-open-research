import sympy as S
from pathlib import Path
sigma=S.sqrt(2); M=1+sigma; rho=1/sigma
a=sigma/(2*M); b=sigma*M/2
d=a/12-a*a/2; ff=-a/360+a*a/12-a**3/3
k=S.symbols('k', real=True); h=S.symbols('h')
simp=lambda x:S.simplify(S.expand(x))
mom=lambda j:S.factorial2(2*j-1)/(2*a)**j
c2=lambda kk:simp((sigma-(kk-sigma)**2)*mom(1)/2+d*mom(2))
c4=lambda kk:simp((-sigma/S.Integer(24)-(kk-sigma)*sigma/6+sigma**2/8-(kk-sigma)**2*sigma/4+(kk-sigma)**4/24)*mom(2)+(ff+sigma*d/2-(kk-sigma)**2*d/2)*mom(3)+d*d*mom(4)/2)
A=lambda kk:simp(c2(kk)-c2(0))
B=lambda kk:simp(c4(kk)-c4(0)-A(kk)*c2(0))
H=S.Matrix(3,3,lambda i,j:1+A(j-i)*h+B(j-i)*h*h)
adj=H.adjugate().applyfunc(S.expand)
A0=adj.applyfunc(lambda x:simp(x.coeff(h,1)))
A1=adj.applyfunc(lambda x:simp(x.coeff(h,2)))
D=S.diag(1,-sigma,2)
Q0=(D.inv()*A0*D*2*a).applyfunc(simp)
Q1=(D.inv()*A1*D*2*a).applyfunc(simp)
fstar=S.Matrix([1,1+rho,(1+rho)**2])
fm=S.Matrix([0,-rho/(4*a),(-2*rho*(1+rho)-2*rho*rho)/(4*a)]).applyfunc(simp)
gstar=S.Matrix([1,1-rho,(1-rho)**2])
gm=S.Matrix([0,rho/(4*b),(2*rho*(1-rho)-2*rho*rho)/(4*b)]).applyfunc(simp)
r=S.Matrix([1,sigma,S.Rational(1,2)]); l=S.Matrix([1,2*sigma,2])
B0=simp((l.T*fstar)[0])
X1=(Q1*fstar+Q0*fm).applyfunc(simp)
lam0=(l/B0).applyfunc(simp)
lam1=(2*Q1.row(2).T/B0-2*l*X1[2]/B0**2).applyfunc(simp)
con0=simp((lam0.T*gstar)[0])
con1=simp((lam1.T*gstar+lam0.T*gm)[0])
scalar1=simp((1/b-1/a)/16)
gamma=simp(scalar1+con1/con0)
result='\n'.join([f'a={simp(a)} b={simp(b)}', f'c2(k)={c2(k)}',f'A(k)={A(k)}',f'B(k)={B(k)}',f'A0={A0}',f'A1={A1}',f'Q0={Q0}',f'Q1={Q1}',f'f1={fm}',f'F1={gm}',f'lambda0={lam0}',f'lambda1={lam1}',f'normalization1={simp((lam1.T*fstar+lam0.T*fm)[0])}',f'con0={con0}',f'con1={con1}',f'scalar1={scalar1}',f'gamma={gamma}'])
print(result)
Path(__file__).with_suffix('.txt').write_text(result+'\n')

