from pathlib import Path
from math import factorial,gcd,lcm
import json,sys
import sympy as s
import mpmath as mp
sys.set_int_max_str_digits(1000000);mp.mp.dps=1200
ROOT=Path('work/session_20261002_codex_continuation/main')
D=[1]
for j in range(1,140):D.append(j*D[-1]+(-1)**j)
def rr(m):return -s.Integer(factorial(2*m))+4*sum((s.Rational((-1)**(m-a),2*a-1)for a in range(1,m+1)),s.Integer(0))
rows=[]
for k in range(1,5):
 for M in [8,32]:
  X=2*M;d=D[X];f=factorial(X);old=rr(M)+f;p=int(old.p);a=int(old.q)
  P=[s.Integer(1)];Q=[s.Integer(0)]
  for j in range(1,6*k):P.append(P[-1]*(X+j));Q.append(Q[-1]*(X+j)+(-1)**j)
  hm=[4*sum((s.Rational((-1)**(r-1-j),X+2*j+1)for j in range(r)),s.Integer(0))for r in range(3*k)]
  PM=s.Matrix(k,2*k,lambda i,j:P[2*(i+j)]);QM=s.Matrix(k,2*k,lambda i,j:Q[2*(i+j)])
  V=s.Matrix(k,2*k,lambda i,j:(-1)**(i+j));ht=s.Matrix(k,2*k,lambda i,j:hm[i+j])
  C=d*PM+QM-V;R0=-f*PM+ht;R=R0+old*V
  assert C==s.Matrix(k,2*k,lambda i,j:D[X+2*(i+j)]-(-1)**(i+j))
  assert R==s.Matrix(k,2*k,lambda i,j:rr(M+i+j))
  A0=C.col_join(R0).det();B0=C.col_join(R0+V).det()-A0
  b0=C.col_join(R).det();b1=C.col_join(R+V).det()-b0
  assert b0==A0+old*B0 and b1==B0 and b1!=0
  delta=s.prod(X+2*j+1 for j in range(3*k-2))
  AA=int(A0*delta**k);BB=int(B0*delta**k);pair=[a*AA+p*BB,a*BB];content=gcd(*pair);prim=[v//content for v in pair]
  clear=lcm(int(b0.q),int(b1.q));raw=[int(b0*clear),int(b1*clear)];gg=gcd(*raw);assert [v//gg for v in raw]==prim or[v//gg for v in raw]==[-v for v in prim]
  center=mp.mpf(-prim[0])/prim[1]
  # Fraction-free row identity retaining the complete S response.
  assert C.col_join(d*R0+f*C).det()==d**k*A0
  assert C.col_join(d*(R0+V)+f*C).det()==d**k*(A0+B0)
  rows.append({'k':k,'M':M,'scalar_D':str(d),'scalar_factorial':str(f),'old_atan_mass':str(old),'tail_clearer':str(delta),'complete_primitive_pair':list(map(str,prim)),'actual_q':str(abs(prim[1])),'final_content':str(content),'diagnostic_complete_error':mp.nstr(center-mp.e-mp.pi,45),'exact_three_state_and_full_endpoint_match':True})
  print('SHIFTED_SHORT',k,M,'qbits',abs(prim[1]).bit_length(),'error',mp.nstr(center-mp.e-mp.pi,12),flush=True)
# New exact symbolic fixed-X models verify the all-degree structural reduction at k1..3.
symbolic=[]
ds,fs=s.symbols('d f');X=16
for k in range(1,4):
 P=[s.Integer(1)];Q=[s.Integer(0)]
 for j in range(1,6*k):P.append(P[-1]*(X+j));Q.append(Q[-1]*(X+j)+(-1)**j)
 C=s.Matrix(k,2*k,lambda i,j:ds*P[2*(i+j)]+Q[2*(i+j)]-(-1)**(i+j))
 R=s.Matrix(k,2*k,lambda i,j:-fs*P[2*(i+j)]+4*sum((s.Rational((-1)**(i+j-1-a),X+2*a+1)for a in range(i+j)),s.Integer(0)))
 V=s.Matrix(k,2*k,lambda i,j:(-1)**(i+j));b0=s.Poly(C.col_join(R).det(method='domain-ge'),ds,fs);b1=s.Poly(C.col_join(R+V).det(method='domain-ge')-b0.as_expr(),ds,fs)
 assert b0.total_degree()<=k and b1.total_degree()<=k and b1.degree(fs)<=k-1
 symbolic.append({'k':k,'X':X,'A0_total_degree':b0.total_degree(),'B0_total_degree':b1.total_degree(),'B0_factorial_degree':b1.degree(fs),'A0_polynomial':str(b0.as_expr()),'B0_polynomial':str(b1.as_expr())})
 print('SYMBOLIC_SHORT',k,b0.total_degree(),b1.total_degree(),b1.degree(fs),flush=True)
(ROOT/'SHIFTED_SHORT_RECURRENCE_CERTIFICATE.json').write_text(json.dumps({'status':'PASS_NEW_SHIFTED_SHORT_COMPLETE_PRIMITIVE_RECURRENCE','rows':rows,'symbolic_models':symbolic,'scope':'Three-state endpoint/primitivegcd/rankdegree identities; decimal errors are diagnostic, and no globalgcd or smallintegerform theorem is inferred.'},indent=2)+'\n')
