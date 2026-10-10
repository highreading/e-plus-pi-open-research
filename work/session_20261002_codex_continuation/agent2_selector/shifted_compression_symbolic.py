from pathlib import Path
import sympy as sp
import json
ROOT=Path(__file__).parent
X,d=sp.symbols('X d')
P=[sp.Integer(1)];Q=[sp.Integer(0)]
for j in range(1,11):
 P.append(sp.expand((X+j)*P[-1]))
 Q.append(sp.expand((X+j)*Q[-1]+(-1)**j))
n=3
rho=[sp.expand(P[2*r]*d+Q[2*r]-(-1)**r) for r in range(6)]
C=sp.Matrix(n,n+1,lambda i,j:rho[i+j])
v=[sp.expand((-1)**(n+j)*C[:,[t for t in range(n+1) if t!=j]].det(method='domain-ge')) for j in range(n+1)]
g=v[0]
for t in v[1:]:g=sp.gcd(g,t)
z=[sp.cancel(t/g) for t in v]
print('GENERIC_COFACTOR_GCD',sp.factor(g),flush=True)
print('REDUCED_D_DEGREES',[sp.degree(t,d) for t in z],flush=True)
qminus=sp.factor(sum((-1)**j*t for j,t in enumerate(z)))
print('QMINUS_FACTORED',qminus,flush=True)
bez=sp.gcdex(sp.Poly(z[-1],d,domain=sp.QQ.frac_field(X)),sp.Poly(z[0],d,domain=sp.QQ.frac_field(X)))
print('TWO_COFACTOR_GCD_IN_QX_D',bez[-1].as_expr(),flush=True)
out={'n':n,'scope':'One symbolic compression hypothesis, not a degree/prime atlas.','generic_cofactor_gcd':str(sp.factor(g)),'reduced_cofactor_polynomials':list(map(str,z)),'q_minus_one_factored':str(qminus),'d_degrees':[sp.degree(t,d) for t in z],'leading_constant_cofactor_gcd_over_QX':str(bez[-1].as_expr())}
(ROOT/'SHIFTED_COMPRESSION_SYMBOLIC_RECEIPT.json').write_text(json.dumps(out,indent=2,default=int)+'\n')
R=sp.factor(sp.resultant(z[0],z[-1],d))
print('SPECIALIZATION_CONTENT_RESULTANT',R,flush=True)
out['specialization_content_resultant']=str(R)
out['specialization_content_resultant_degree_X']=sp.degree(R,X)
(ROOT/'SHIFTED_COMPRESSION_SYMBOLIC_RECEIPT.json').write_text(json.dumps(out,indent=2,default=int)+'\n')
