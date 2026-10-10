from pathlib import Path
from math import factorial
import json
import sympy as s
import mpmath as mp
mp.mp.dps=1200;ROOT=Path('work/session_20261002_codex_continuation/main')
D=[1]
for n in range(1,100):D.append(n*D[-1]+(-1)**n)
rows=[]
for M in [4,12,48]:
 X=2*M;t=X+1;A=t*t+t+1;B=t*t+1;d=D[X];f=factorial(X)
 ell=4*sum((s.Rational((-1)**(M-a),2*a-1)for a in range(1,M+1)),s.Integer(0))
 r=(s.Integer(B*f)+s.Rational(4*(d-1),t))/(A*d-t);c=r-ell;q=int(c.q)
 v=s.Rational(B)/(A*r-s.Rational(4,t))
 assert v==s.Rational(d,f)-(t*r-s.Rational(4,t))/(f*(A*r-s.Rational(4,t)))
 assert int(v.q)<=8*t**3*int(ell.q)*q
 C=s.Matrix([[d-1,D[X+2]+1]])
 rr=lambda j:-s.Integer(factorial(2*j))+4*sum((s.Rational((-1)**(j-a),2*a-1)for a in range(1,j+1)),s.Integer(0))
 R=s.Matrix([[rr(M),rr(M+1)]]);V=s.Matrix([[1,-1]]);b0=C.col_join(R).det();b1=C.col_join(R+V).det()-b0
 assert -b0/b1==c
 vm=mp.mpf(int(v.p))/int(v.q);cm=mp.mpf(int(c.p))/q
 err=vm-1/mp.e;assert abs(err)<=mp.mpf(6)/(X*f)
 rows.append({'M':M,'X':X,'actual_center':str(c),'actual_q':str(q),'old_atan_denominator':str(ell.q),'extracted_rational':str(v),'extracted_actual_denominator':str(v.q),'exact_full_endpoint_and_extraction':True,'diagnostic_complete_error':mp.nstr(cm-mp.e-mp.pi,40),'diagnostic_inverse_e_error':mp.nstr(err,40),'diagnostic_scaled_full_error':mp.nstr(X*(cm-mp.e-mp.pi),30)})
 print('K1_EXTRACT',M,'qbits',q.bit_length(),'scalederror',mp.nstr(X*(cm-mp.e-mp.pi),12),flush=True)
(ROOT/'SHIFTED_SHORT_K1_EXTRACTION_CERTIFICATE.json').write_text(json.dumps({'status':'PASS_NEW_K1_FULL_PRIMITIVE_MOBIUS_EXTRACTION','rows':rows,'scope':'Exact endpoint/extraction/finaldenominator identities and diagnostic errorbounds; author infinite obstruction is proved separately.'},indent=2)+'\n')
