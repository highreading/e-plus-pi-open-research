"""Fresh exact paired-response moment determinants and actual primitive pair."""
from pathlib import Path
from math import factorial,gcd,lcm
import json
import sympy as sp
import mpmath as mp
SROOT=Path('work/session_20261002_codex_continuation')
D=[1]
for n in range(1,100):D.append(n*D[-1]+(-1)**n)
def rho(j):return D[2*j]-(-1)**j
def rat(j):
 return -sp.Integer(factorial(2*j))+4*sum((sp.Rational((-1)**(j-r),2*r-1) for r in range(1,j+1)),sp.Integer(0))
rows=[]
mp.mp.dps=1000
for k in range(2,9):
 n=2*k-1
 C=sp.Matrix(n,n,lambda i,j:rho(i+j))
 assert C.det()!=0
 v=list(C.inv()*sp.Matrix([-rho(i+n) for i in range(n)]))+[sp.Integer(1)]
 den=lcm(*(int(a.q) for a in v));qq=[int(a*den) for a in v]
 content=gcd(*qq);qq=[a//content for a in qq]
 assert gcd(*qq)==1
 assert all(sum(qq[j]*rho(j+s) for j in range(n+1))==0 for s in range(n))
 qm=sum(a*(-1)**j for j,a in enumerate(qq));assert qm!=0
 R=sp.Matrix(k,k,lambda i,j:sum(qq[t]*rat(i+j+t) for t in range(n+1)))
 W=sp.Matrix(k,k,lambda i,j:qm*(-1)**(i+j))
 for s in range(2*k-1):
  assert sum(qq[j]*D[2*(j+s)] for j in range(n+1))==(-1)**s*qm
 c0=R.det();c1=(R+W).det()-c0
 assert c1!=0
 assert all((R+a*W).det()==c0+a*c1 for a in (-1,2,3))
 clear=lcm(int(c0.q),int(c1.q));pair=[int(c0*clear),int(c1*clear)]
 gc=gcd(*pair);primitive=[a//gc for a in pair]
 actualq=abs(primitive[1]);cc=mp.mpf(-primitive[0])/primitive[1]
 full=mp.mpf(primitive[0])+mp.mpf(primitive[1])*(mp.e+mp.pi)
 rows.append({'k':k,'orthogonal_degree_in_y':n,'primitive_integer_q_coefficients':list(map(str,qq)),
  'q_minus_one':str(qm),'constraint_matrix_determinant':str(C.det()),
  'rational_determinant_coefficients':[str(c0),str(c1)],'formal_coefficient_clearer':str(clear),
  'full_output_content':str(gc),'primitive_linear_pair_constant_S':list(map(str,primitive)),
  'actual_center_denominator':str(actualq),
  'diagnostic_center':mp.nstr(cc,60),'diagnostic_complete_error':mp.nstr(cc-mp.e-mp.pi,30),
  'diagnostic_log_abs_primitive_form':mp.nstr(mp.log(abs(full)),30),
  'diagnostic_precision_digits':mp.mp.dps,'scope':'Exact full moment/linear determinant/content; real values are diagnostics, not interval bounds.'})
 print('EXACT_NEW_PAIR',k,'qbits',actualq.bit_length(),'logform',mp.nstr(mp.log(abs(full)),12),flush=True)
out={'status':'PASS_NEW_PAIRED_DERANGEMENT_LINEAR_S_DETERMINANTS','rows':rows,
 'scope':'New exact complete determinant coefficients and final primitive gcd; no asymptotic smallness/nonzero or main proof inferred from finite diagnostics.'}
(SROOT/'main/PAIRED_DERANGEMENT_LINEAR_S_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n')
