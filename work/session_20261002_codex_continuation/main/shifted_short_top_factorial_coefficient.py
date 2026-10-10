from pathlib import Path
import sympy as s,json
X=s.symbols('X');rows=[]
for k in range(1,4):
 P=[s.Integer(1)];Q=[s.Integer(0)]
 for j in range(1,6*k):P.append(s.expand(P[-1]*(X+j)));Q.append(s.expand(Q[-1]*(X+j)+(-1)**j))
 PM=s.Matrix(k,2*k,lambda i,j:P[2*(i+j)]);CM=s.Matrix(k,2*k,lambda i,j:Q[2*(i+j)]-(-1)**(i+j))
 Z=s.Poly(CM.col_join(-PM).det(method='domain-ge'),X);factor=s.factor(Z.as_expr());sg=(-1)**(k+1)
 coeffs=Z.all_coeffs();allsame=all(c*sg>0 for c in coeffs)
 print('TOP_FACTORIAL',k,Z.degree(),allsame,factor,flush=True)
 rows.append({'k':k,'polynomial':str(Z.as_expr()),'factorization':str(factor),'degree':Z.degree(),'all_coefficients_have_expected_nonzero_sign':allsame,'coefficient_sign':sg})
Path('work/session_20261002_codex_continuation/main/SHIFTED_SHORT_TOP_FACTORIAL_COEFFICIENT_CERTIFICATE.json').write_text(json.dumps({'status':'EXACT_NEW_LEADING_FACTORIAL_POLYNOMIALS','rows':rows,'scope':'Exact symbolic all-X polynomials k1..3; no all-k nonzero or main irrationality conclusion inferred.'},indent=2)+'\n')
