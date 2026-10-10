"""One symbolic d=2 example; p=751 is selected from its exact discriminant."""
from pathlib import Path
import json
import sympy as S

z,b,g=S.symbols("z beta gamma")
d=2; p=751; D=1+z*z; ss=3*d+2
Lco=[-d*(d-1)*z+2*d*d*(d-1)-d*b,
     (2*d-2)*z*z+b*z+g,
     -((z+ss)*D-4*z*z),z*D]
def L(f):
    return S.expand(sum(Lco[j]*S.diff(f,z,j) for j in range(4)))
def P(f):
    return S.expand(sum(Lco[j]*sum(S.binomial(j,k)*S.diff(f,z,k)
                                   for k in range(j+1)) for j in range(4)))
B=z**d
for r in range(1,d+1):
    B=S.expand(B+P(B).coeff(z,d+2-r)/r*z**(d-r))
E=S.Matrix([S.factorial(d)*P(B).coeff(z,j) for j in (1,0)])
Jac=E.jacobian([b,g])
Jdet=S.factor(Jac.det())
Wpol=[P(z**j) for j in range(d-1,-1,-1)]
Wpol += [z*(S.diff(B,z)+B)-d*B,S.diff(B,z)+B]
W=S.Matrix([[f.coeff(z,k) for f in map(S.expand,Wpol)]
            for k in range(d+1,-1,-1)])
assert S.simplify(Jdet-(-1)**d*S.factorial(d)*W.det())==0

GB=S.groebner(list(E),g,b)
elim=S.Poly(list(GB)[-1],b).monic().as_expr()
disc=int(S.discriminant(elim,b))
common=S.gcd(S.Poly(elim,b,modulus=p),S.Poly(S.diff(elim,b),b,modulus=p))
assert common.monic().as_expr()==b-30
subs={b:30,g:15}
def modpoly(f):
    return S.Poly.from_dict({
        powers:int(coef.p)*pow(int(coef.q),-1,p)%p
        for powers,coef in S.Poly(S.expand(f),z,domain=S.QQ).terms()
    },z,modulus=p)

U=S.Matrix([[L(z**j).coeff(z,k) for j in range(d+1)] for k in range(d)])
C=sum((-1)**j*U[:,[a for a in range(d+1) if a!=j]].det()*z**j
      for j in range(d+1))
Bm=modpoly(B.subs(subs)).as_expr()
Cm=modpoly(C.subs(subs)).as_expr()
Jm=modpoly(Cm*(S.diff(Bm,z)+Bm)-S.diff(Cm,z)*Bm).as_expr()
Rm=S.rem(modpoly(2*S.diff(Cm,z)-((30+14)*z+15-4)*Cm),
         S.Poly(D,z,modulus=p)).as_expr()
ec=[int(v)%p for v in E.subs(subs)]
jac=[[int(Jac.subs(subs)[i,j])%p for j in range(2)] for i in range(2)]
rc=int(S.resultant(D,Cm,z))%p
rj=int(S.resultant(D,Jm,z))%p
assert ec==[0,0]
assert int(Jdet.subs(subs))%p==0
assert (rc,rj)==(53,124)
assert Rm==193*z+257
assert pow(4*rc*rj%p,(p-1)//2,p)==p-1
dotB=modpoly(72*S.diff(B,b).subs(subs)-55*S.diff(B,g).subs(subs)).as_expr()
forcing=modpoly(P(dotB).subs(subs)+72*(z*(S.diff(Bm,z)+Bm)-d*Bm)
                -55*(S.diff(Bm,z)+Bm))
assert forcing.is_zero
out={
  "scope":"one symbolic degree and one discriminant-selected prime; not an actual four-equation root",
  "d":d,"prime":p,"beta_gamma":[30,15],
  "E1_E0":[str(S.expand(v)) for v in E],
  "eliminant":str(elim),"discriminant":disc,
  "discriminant_factorization":{str(k):int(v) for k,v in S.factorint(disc).items()},
  "Jacobian_matrix_mod_p":jac,
  "B_mod_p":str(Bm),"Cstar_mod_p":str(Cm),"Jstar_mod_p":str(Jm),
  "pole_resultants_mod_p":[rc,rj],"residue_remainder_mod_p":str(Rm),
  "four_times_resultant_product_mod_p":4*rc*rj%p,
  "resultant_product_is_nonsquare":True,
  "tangent_parameters":[72,-55],"tangent_B_mod_p":str(dotB),
  "augmented_Jacobian_identity":"pass","tangent_identity":"pass",
  "status":"pass"
}
Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))
