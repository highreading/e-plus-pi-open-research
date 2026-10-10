"""Bounded independent controls: universal monomial identity and the stated d=2 example."""
from pathlib import Path
import sys, json
sys.path.insert(0, str(Path(__file__).parent / "math_packages"))
import sympy as S

z,d,m,b,g=S.symbols('z d m beta gamma')
D=1+z*z
L=[-d*(d-1)*z+2*d*d*(d-1)-d*b,
   (2*d-2)*z*z+b*z+g,-((z+3*d+2)*D-4*z*z),z*D]
actual={j:S.Integer(0) for j in range(-3,4)}
for order,coef in enumerate(L):
    for (power,),v in S.Poly(coef,z).terms():
        for deriv in range(order+1):
            actual[power-deriv]+=v*S.binomial(order,deriv)*S.prod(m-a for a in range(deriv))
expected={2:m-d,1:2*m*(m-2*d)+b-d*(d-1),
          0:m*(m-1)*(m-3*d)+(m-d)*b+m+g+2*d*d*(d-1)-3*d-2,
          -1:m*(g+2*m-6*d-6),-2:m*(m-1)*(m-3*d-4)}
assert all(S.expand(v-expected.get(j,0))==0 for j,v in actual.items())

Lc=[S.expand(v.subs(d,2)) for v in L]
def op(f,gauged=False):
    return S.expand(sum(c*sum(S.binomial(j,k)*S.diff(f,z,k)
                    for k in (range(j+1) if gauged else [j]))
                    for j,c in enumerate(Lc)))
u,v=S.symbols('u v')
candidate=z*z+u*z+v
sol=S.solve([op(candidate,True).coeff(z,3),op(candidate,True).coeff(z,2)],(u,v))
B=S.expand(candidate.subs(sol))
E=S.Matrix([2*op(B,True).coeff(z,j) for j in (1,0)])
jac=E.jacobian([b,g])
W=S.Matrix([[f.coeff(z,k) for f in
             map(S.expand,[op(z,True),op(1,True),z*(S.diff(B,z)+B)-2*B,S.diff(B,z)+B])]
            for k in (3,2,1,0)])
assert S.expand(jac.det()-2*W.det())==0
f=b**6-38*b**5+589*b**4-4714*b**3+20344*b*b-44304*b+37120
gamma=(b**5-32*b**4+397*b**3-2336*b*b+6416*b-6336)/12
assert all(S.rem(S.together(e.subs(g,gamma)),f,b)==0 for e in E)
assert list(S.groebner(list(E),g,b,domain=S.QQ))==list(S.groebner([f,g-gamma],g,b,domain=S.QQ))
assert S.discriminant(f,b)==2**19*3**6*751*318737
p=751
assert S.isprime(p)
assert S.gcd(S.Poly(f,b,modulus=p),S.Poly(S.diff(f,b),b,modulus=p)).monic().as_expr()==b-30
point={b:30,g:15}
def red(poly):
    raw=S.Poly(S.expand(poly),z)
    return S.Poly.from_dict({k:int(q.p)*pow(int(q.q),-1,p)%p for k,q in raw.terms()},z,modulus=p)
Bp=red(B.subs(point)).as_expr()
U=S.Matrix([[op(z**j).coeff(z,k) for j in range(3)] for k in range(2)])
Cs=sum((-1)**j*U[:,[k for k in range(3) if k!=j]].det()*z**j for j in range(3))
Cp=red(Cs.subs(point)).as_expr()
Jp=red(Cp*(S.diff(Bp,z)+Bp)-S.diff(Cp,z)*Bp).as_expr()
jacp=[[int(jac[i,j].subs(point))%p for j in range(2)] for i in range(2)]
assert jacp==[[55,72],[214,444]]
assert [int(e.subs(point))%p for e in E]==[0,0]
assert red(Bp-(z*z+20*z-151)).is_zero
assert red(Cp-(-328*z*z-14*z+68)).is_zero
res=[int(S.resultant(D,Q,z))%p for Q in (Cp,Jp)]
assert res==[53,124]
rem=S.rem(red(2*S.diff(Cp,z)-(44*z+11)*Cp),red(D)).as_expr()
assert rem==193*z+257
assert 4*res[0]*res[1]%p==3 and pow(3,(p-1)//2,p)==p-1
dot=72*z+358
assert red(op(dot,True).subs(point)+72*(z*(S.diff(Bp,z)+Bp)-2*Bp)-55*(S.diff(Bp,z)+Bp)).is_zero
out={'status':'pass','scope':'all-index monomial coefficient identity; only stated d=2 and p=751 certificate',
     'universal_recurrence':'pass','symbolic_Jacobian_factor':'pass','discriminant':'pass',
     'prime':p,'Jacobian_mod_p':jacp,'resultants':res,'residue_remainder':str(rem),
     'tangent_witness':'pass','not_an_actual_four_equation_root':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
