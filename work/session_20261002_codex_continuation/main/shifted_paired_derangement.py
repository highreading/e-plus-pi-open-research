"""Fresh shifted matching moments: roots, full determinant and final gcd."""
from pathlib import Path
from math import factorial,gcd,lcm
import sys,json
import sympy as sp
import mpmath as mp
sys.set_int_max_str_digits(1000000)
SROOT=Path('work/session_20261002_codex_continuation')
D=[1]
for n in range(1,400):D.append(n*D[-1]+(-1)**n)
def rat(j):return -sp.Integer(factorial(2*j))+4*sum((sp.Rational((-1)**(j-r),2*r-1) for r in range(1,j+1)),sp.Integer(0))
rows=[];y=sp.Symbol('y');mp.mp.dps=1000
for k in (2,3,4):
 for MM in (8,32,128):
  n=2*k-1
  def rho(j):return D[2*(MM+j)]-(-1)**(MM+j)
  C=sp.Matrix(n,n,lambda i,j:rho(i+j));assert C.det()!=0
  cc=list(C.inv()*sp.Matrix([-rho(i+n) for i in range(n)]))+[sp.Integer(1)]
  cd=lcm(*(int(a.q) for a in cc));qq=[int(a*cd) for a in cc];gc=gcd(*qq);qq=[a//gc for a in qq]
  assert all(sum(qq[j]*rho(j+s) for j in range(n+1))==0 for s in range(n))
  poly=sp.Poly(sum(a*y**j for j,a in enumerate(qq)),y)
  roots_le_one=int(poly.count_roots(-sp.oo,1));real_roots=int(poly.count_roots(-sp.oo,sp.oo))
  qm=sum(a*(-1)**j for j,a in enumerate(qq));assert qm!=0
  R=sp.Matrix(k,k,lambda i,j:sum(qq[t]*rat(MM+i+j+t) for t in range(n+1)))
  W=sp.Matrix(k,k,lambda i,j:qm*(-1)**(MM+i+j))
  for s in range(2*k-1):assert sum(qq[j]*D[2*(MM+j+s)] for j in range(n+1))==(-1)**(MM+s)*qm
  c0=R.det();c1=(R+W).det()-c0;assert c1!=0
  assert all((R+t*W).det()==c0+t*c1 for t in (-1,2))
  clear=lcm(int(c0.q),int(c1.q));pair=[int(c0*clear),int(c1*clear)];g=gcd(*pair);pair=[a//g for a in pair]
  center=mp.mpf(-pair[0])/pair[1];err=mp.e+mp.pi-center
  expected=(mp.e+2)*factorial(k-1)**2/2**(2*k-1)
  rows.append({'k':k,'M':MM,'n':n,'primitive_integer_polynomial':list(map(str,qq)),
   'exact_real_root_count':real_roots,'exact_root_count_at_or_below_one':roots_le_one,
   'all_roots_above_one_exact':real_roots==n and roots_le_one==0,'q_minus_one':str(qm),
   'complete_rational_determinant_pair':list(map(str,[c0,c1])),
   'formal_clearer':str(clear),'full_output_content':str(g),
   'primitive_constant_S_pair':list(map(str,pair)),'actual_q':str(abs(pair[1])),
   'diagnostic_complete_positive_error':mp.nstr(err,40),
   'diagnostic_error_times_M_power':mp.nstr(err*MM**(2*k-1),40),
   'fixed_k_predicted_limit':mp.nstr(expected,40),'diagnostic_precision_digits':mp.mp.dps})
  print('NEW_SHIFTED_EXACT',k,MM,'allrootsabove1',real_roots==n and roots_le_one==0,'qbits',abs(pair[1]).bit_length(),'scalederror',mp.nstr(err*MM**(2*k-1),14),flush=True)
out={'status':'PASS_NEW_SHIFTED_PAIRED_FULL_DETERMINANTS','rows':rows,
 'scope':'Fresh exact matching/full determinant/final gcd/Sturm root receipts; real errors are diagnostics. Fixed-degree theorem separate, no growing-degree uniform bound or main proof.'}
(SROOT/'main/SHIFTED_PAIRED_DERANGEMENT_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n')
