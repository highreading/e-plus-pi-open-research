"""Parent-authored exact finite decision after universal denominator/degree bounds.

No remote code is executed. This decides the displayed rational tensor gauge,
not other endpoint representations or any global irrationality criterion.
"""
from pathlib import Path
import hashlib,json,time
import sympy as s

ROOT=Path(__file__).resolve().parent
start=time.monotonic()
n=s.symbols('n')
D=(n+1)**2*(n+2)
degrees=[3,3,3,3,2,2]
U=s.Matrix([[0,(n+1)*(n+2),(n+2)/2],
 [n+2,-(n*n+3*n+1),-n*(n+2)/(2*(n+1))],
 [-(n+2)*(2*n+3),(n+2)*(n*n+3*n+1),(n+2)*(n*n-2)/(2*(n+1))]])
RR=s.Matrix([[0,1],[(n+1)/(n+2),(2*n+3)/(n+2)]])
K=s.kronecker_product(U,RR)
gamma=s.Matrix([[0,(n+2)/2,-(n+1)**2/2,((n+1)**2+1)/2,
 -(n+1)/4,(n*n+3*n+3)/(4*(n+1))]])

# Check the matrices needed in the infinity proof independently.
scale=s.diag(1,1,n)
scaled_U=scale.subs(n,n+1).inv()*U*scale
Uinf=scaled_U.applyfunc(lambda v:s.limit(v/n**2,n,s.oo))
Rinf=RR.applyfunc(lambda v:s.limit(v,n,s.oo))
leading=s.eye(6)+s.kronecker_product(Uinf,Rinf)
assert Uinf==s.Matrix([[0,1,s.Rational(1,2)],[0,-1,-s.Rational(1,2)],
                      [0,1,s.Rational(1,2)]])
assert leading.det()==-s.Rational(1,4)
scaled_gamma=gamma*s.kronecker_product(scale,s.eye(2))
gamma_degrees=[None if not v else s.degree(s.fraction(s.cancel(v))[0],n)
                -s.degree(s.fraction(s.cancel(v))[1],n) for v in scaled_gamma]
assert all(d is None or d<=2 for d in gamma_degrees)

clear=4*(n+1)*(n+2)*D*D.subs(n,n+1)
unknown_labels=[]
columns=[]
max_degree=0
for i,bound in enumerate(degrees):
    for j in range(bound+1):
        unknown_labels.append({'component':i,'degree':j})
        ps=[]
        for k in range(6):
            expr=clear*((n+1)**j/D.subs(n,n+1)*K[i,k]
                +((n+1)**2*n**j/D if i==k else 0))
            p=s.Poly(s.cancel(expr),n)
            ps.append(p)
            if not p.is_zero:max_degree=max(max_degree,p.degree())
        columns.append(ps)
rhs=[s.Poly(s.cancel(clear*gamma[k]),n) for k in range(6)]
max_degree=max(max_degree,max(p.degree() for p in rhs if not p.is_zero))
assert max_degree<=11 and len(columns)==22
rows=[];bb=[];labels=[]
for k in range(6):
    for degree in range(12):
        row=[ps[k].nth(degree) for ps in columns]
        val=rhs[k].nth(degree)
        if any(row) or val:
            rows.append(row);bb.append(val)
            labels.append({'component':k,'degree':degree})
A=s.Matrix(rows);rhscol=s.Matrix(bb)
_,piv=A.row_join(rhscol).rref()
rank_A=sum(j<22 for j in piv)
rank_aug=len(piv)
result={'unknowns':22,'equations':A.rows,'max_cleared_degree':max_degree,
 'denominator':'(n+1)^2(n+2)','numerator_degrees':degrees,
 'seed_equation_used':False,'rank_A':rank_A,'rank_augmented':rank_aug,
 'unknown_labels':unknown_labels,'equation_labels':labels,
 'coefficient_matrix':[[str(x) for x in row] for row in rows],
 'right_hand_side':[str(x) for x in bb]}
if rank_aug>rank_A:
    witness=None
    for v in A.T.nullspace():
        val=(v.T*rhscol)[0]
        if val:
            witness=v/val;break
    assert witness is not None
    assert witness.T*A==s.zeros(1,22) and (witness.T*rhscol)[0]==1
    result.update({'decision':'No rational gauge of the displayed six-component tensor type exists, using the independently established universal bounds.',
      'exact_left_null_witness':[{'equation':i,'label':labels[i],'weight':str(v)}
          for i,v in enumerate(witness) if v],
      'witness_times_A_zero':True,'witness_times_rhs':1})
else:
    coefficients=list(s.linsolve((A,rhscol)))[0]
    polys=[];idx=0
    for bound in degrees:
        polys.append(sum(coefficients[idx+j]*n**j for j in range(bound+1)))
        idx+=bound+1
    ell=s.Matrix([polys])/D
    residual=(ell.subs(n,n+1)*K+(n+1)**2*ell-gamma).applyfunc(s.cancel)
    assert residual==s.zeros(1,6)
    seed=s.Matrix([0,0,20,40,-132,-264])
    seed_residual=s.cancel((ell.subs(n,2)*seed)[0]-14)
    result.update({'decision':'Rational gauge found','numerator_polynomials':[str(p) for p in polys],
                   'residual_polynomials':[str(v) for v in residual],
                   'actual_seed_residual':str(seed_residual)})
out={'personally_authored':True,'network_and_credentials_denied':True,
 'infinity_checks':{'U_infinity':str(Uinf),'R_infinity':str(Rinf),
       'leading_determinant':str(leading.det()),'scaled_forcing_degrees':gamma_degrees},
 'gauge':result,'scope':'Exact universal rational-gauge decision after the pole-orbit and infinity degree theorems; no nonexistence statement for other representations, no original-contact gcd estimate, and no e+pi proof.',
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'elapsed_seconds':round(time.monotonic()-start,3)}
(ROOT/'endpoint_universal_gauge_certificate.json').write_text(json.dumps(out,indent=2,default=str)+'\n')
print(json.dumps({'decision':result['decision'],'rank_A':rank_A,'rank_augmented':rank_aug,
 'equations':A.rows,'seconds':out['elapsed_seconds']}),flush=True)
