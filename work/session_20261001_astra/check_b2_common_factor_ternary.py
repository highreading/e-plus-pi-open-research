"""Exact symbolic and scalar checks for the main-agent b=2 draft.
These checks supplement, rather than replace, the all-index proof.
"""
import json
from hashlib import sha256
from pathlib import Path
import sympy as sp

n,h,u,v,Ac,Bc,wp,wu,pn,pu,f = sp.symbols('n h u v Ac Bc wp wu pn pu f')
t=n+1
J=n*h+u
a=-n*h+n*u+v/2
up=t*(h-u+v/2)
vp=t*(n*h+u-(n+2)*v/2)
k=(1-n)*h+(n-1)*u+v
ell=(-n**2+3*n+2)*h+(n**2-2*n-1)*u+n*v
jp=t*a+up
kp=n*t*a+2*t*up+vp
sigma=t*k**2-a*ell
omega=k*J-ell*h
C=(t*k-a)*J-t*(ell-k)*h
S=jp**2-a*kp
W=jp*J-kp*h
Cold=(jp-a)*J-(kp-jp)*h
Vtilde=sigma*Ac-C*Bc-a*omega
Qtilde=2*wp*sigma-t*wu*C
Dtilde=t*pu*C-2*pn*sigma
Xold=2*(wp+f*Ac)*S-t**2*(wu+2*f*Bc/t)*Cold-2*f*a*W
Dold=t**2*pu*Cold-2*pn*S
identities={
 'J_factor':sp.expand(jp-t*k)==0,
 'K_factor':sp.expand(kp-t*ell)==0,
 'S_factor':sp.expand(S-t*sigma)==0,
 'W_factor':sp.expand(W-t*omega)==0,
 'C_identity':sp.expand(Cold-C)==0,
 'complete_numerator_factor':sp.cancel(Xold-t*(Qtilde+2*f*Vtilde))==0,
 'denominator_factor':sp.expand(Dold-t*Dtilde)==0,
}
assert all(identities.values()), identities

z,x,y=sp.symbols('z x y')
def Hpoly(r):
    coeff=sp.Poly((1-z+z*z/2)**r,z)
    return sp.expand(sum(sp.factorial(r)*coeff.nth(s)*x**(r-s)/sp.factorial(r-s) for s in range(r+1)))
def Lpoly(r):
    return sp.Poly(sp.expand(sum(sp.factorial(2*r-2*j)*(2*y-1)**(r-2*j)/(sp.factorial(j)*sp.factorial(r-j)*sp.factorial(r-2*j)) for j in range(r//2+1))),y)
def E(d):
    return sum(sp.Rational(1,sp.factorial(j)) for j in range(d+1))
def contractions(r):
    lp,lu=Lpoly(r),Lpoly(r+1)
    scale=sp.factorial(r)**2/sp.Integer(2)**r
    aa=sp.cancel(scale*sum(lp.nth(j)*E(r+j) for j in range(r+1)))
    bb=sp.cancel(scale*(r+1)/2*sum(lu.nth(j)*E(r+j) for j in range(r+2)))
    return aa,bb
fields=['h','u','v','Acal','Bcal','a','k','ell','sigma','C','omega','Vtilde']
expected=[
 [1,0,0,1,3,0,1,2,1,-1,-2,4],
 [0,1,0,3,10,1,0,-2,2,-1,0,16],
 [1,-2,2,21,133,-5,-1,10,53,-33,-10,5452],
]
rows=[]
for r in range(3):
    hp=Hpoly(r)
    hh=hp.subs(x,1)
    uu=sp.diff(hp,x).subs(x,1)
    vv=sp.diff(hp,x,2).subs(x,1)
    aa,bb=contractions(r)
    sub={n:r,h:hh,u:uu,v:vv,Ac:aa,Bc:bb}
    vals=[hh,uu,vv,aa,bb]+[sp.cancel(expr.subs(sub)) for expr in [a,k,ell,sigma,C,omega,Vtilde]]
    assert vals==expected[r], (r,vals)
    assert all(value.is_Integer for value in vals)
    assert int(vals[-1])%3==1
    assert sp.expand(Hpoly(r+1).subs(x,1)-a.subs(sub))==0
    assert int((t*Vtilde).subs(sub))==(r+1)*int(vals[-1])
    rows.append({'r':r,**dict(zip(fields,map(int,vals))), 'unnormalized_V':int((t*Vtilde).subs(sub))})

# Given the proved Legendre digit recursion, check denominator residues
# with the common unit P_m kept as a formal variable.
pm=sp.symbols('P_m')
endpoint_pairs=[(pm,2*pm),(2*pm,2*pm),(2*pm,sp.symbols('P_next'))]
denominator_residues=[]
for r,row in enumerate(rows):
    p0,p1=endpoint_pairs[r]
    expr=(r+1)*p1*row['C']-2*p0*row['sigma']
    reduced=sp.Poly(expr,pm,sp.symbols('P_next'),modulus=3).as_expr()
    target=[2*pm,0,pm][r]
    assert sp.Poly(expr-target,pm,sp.symbols('P_next'),modulus=3).is_zero
    denominator_residues.append(str(reduced))

result={
 'status':'PASS_EXACT_ALGEBRA_AND_THREE_SCALAR_SEEDS',
 'independent_researcher_review':False,
 'scope':'Formal identities and complete ternary scalar seeds; infinite conclusions require the separately written transfer and valuation proofs.',
 'formal_identities':identities,
 'seed_fields':fields,
 'seed_rows':rows,
 'Vtilde_mod_3':[row['Vtilde']%3 for row in rows],
 'Dtilde_mod_3_in_terms_of_P_m':denominator_residues,
 'actual_HP_degree_scan':False,
 'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
}
output=Path('work/session_20261001_astra/B2_COMMON_FACTOR_TERNARY_CHECKS.json')
output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
assert json.loads(output.read_text(encoding='utf-8'))==result
print(json.dumps({'status':result['status'],'formal_identity_count':len(identities),'Vtilde_seeds':[row['Vtilde'] for row in rows],'certificate':str(output)}))
