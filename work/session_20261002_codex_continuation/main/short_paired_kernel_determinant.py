"""New shorter paired right family from the full rectangular matching kernel."""
from pathlib import Path
from math import factorial,gcd,lcm
import json,sys
import sympy as sp
import mpmath as mp
sys.set_int_max_str_digits(1000000)
SROOT=Path('work/session_20261002_codex_continuation')
D=[1]
for n in range(1,100):D.append(n*D[-1]+(-1)**n)
def rho(j):return D[2*j]-(-1)**j
def rat(j):return -sp.Integer(factorial(2*j))+4*sum((sp.Rational((-1)**(j-r),2*r-1) for r in range(1,j+1)),sp.Integer(0))
mp.mp.dps=1000;rows=[]
for k in range(1,10):
 C=sp.Matrix(k,2*k,lambda i,j:rho(i+j));assert C.rank()==k
 R=sp.Matrix(k,2*k,lambda i,j:rat(i+j))
 V=sp.Matrix(k,2*k,lambda i,j:(-1)**(i+j))
 A0=C.col_join(R);A1=C.col_join(R+V)
 b0=A0.det();b1=A1.det()-b0;assert b1!=0
 assert C.col_join(R+2*V).det()==b0+2*b1
 ns=C.nullspace();assert len(ns)==k
 basis=[]
 for v in ns:
  d=lcm(*(int(z.q) for z in v));aa=[int(z*d) for z in v];g=gcd(*aa);basis.append(sp.Matrix([a//g for a in aa]))
 Q=sp.Matrix.hstack(*basis);assert C*Q==sp.zeros(k,k)
 h0=(R*Q).det();h1=((R+V)*Q).det()-h0
 assert h0*b1==h1*b0
 T=sp.eye(k)
 if k>1:T[0,1]=1
 assert (R*Q*T).det()==h0 and ((R+V)*Q*T).det()-h0==h1
 clear=lcm(int(b0.q),int(b1.q));pair=[int(b0*clear),int(b1*clear)];g=gcd(*pair);pair=[a//g for a in pair]
 center=mp.mpf(-pair[0])/pair[1];full=mp.mpf(pair[0])+mp.mpf(pair[1])*(mp.e+mp.pi)
 rows.append({'k':k,'right_degree_bound':2*k-1,'integer_kernel_columns':[[str(z) for z in v] for v in basis],
  'stacked_rational_coefficient_pair':list(map(str,[b0,b1])),'formal_clearer':str(clear),'full_content':str(g),
  'primitive_constant_S_pair':list(map(str,pair)),'actual_q':str(abs(pair[1])),
  'diagnostic_center':mp.nstr(center,60),'diagnostic_complete_error':mp.nstr(center-mp.e-mp.pi,35),
  'diagnostic_log_abs_primitive_form':mp.nstr(mp.log(abs(full)),30),
  'exact_kernel_and_stack_center_match':True,'basis_change_invariance_checked':True})
 print('NEW_SHORT_KERNEL',k,'qbits',abs(pair[1]).bit_length(),'error',mp.nstr(center-mp.e-mp.pi,12),flush=True)
out={'status':'PASS_NEW_SHORT_RECTANGULAR_KERNEL_LINEAR_S_DETERMINANTS','rows':rows,
 'scope':'New exact stacked/full-kernel primitive pairs and basis invariance; diagnostics do not prove all-degree convergence/nonzero or smallness.'}
(SROOT/'main/SHORT_PAIRED_KERNEL_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n')
