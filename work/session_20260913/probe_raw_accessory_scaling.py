"""Predeclared degrees 2,4,8 and inexpensive conditional16; numerical roots are not limits."""
import json
import sys
import time
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'math_packages'))
sys.path.insert(0,str(HERE))
import sympy as s
from check_raw_hp_homogeneous_ode import raw_row
z=s.symbols('z');D=s.Poly(1+z*z,z)
def poly(f):return s.Poly(f,z)
def det3(rows):
    a,b,c=rows
    return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])
def quotient(p,k):
    q,r=s.div(p,poly(z**k));assert r.is_zero;return q
def decimals(p):return [str(s.N(a,30)) for a in p.all_coeffs()]
def exacts(p):return list(map(str,p.all_coeffs()))
out={'scope':'Exact predeclared n=2,4,8 and inexpensive conditional n=16; roots at80 digits are numerical evidence only',
     'normalization':'Q made monic; A1,A0 divided by the same original leading coefficient; z=n*zeta scaling',
     'cases':[]}
saved_path=HERE/'raw_accessory_scaling_probe.json'
if saved_path.exists():
    out['cases']=json.loads(saved_path.read_text())['cases']
for n in (2,4,8,16):
    if any(case['n']==n for case in out['cases']):
        continue
    started=time.monotonic();A,B,C=map(poly,raw_row(n))
    E=[sum((poly(s.binomial(r,j))*B.diff((z,j)) for j in range(r+1)),poly(0)) for r in range(4)]
    Cj=[C.diff((z,r)) for r in range(4)]
    AA=[A.diff((z,r)) for r in range(4)]
    f2=[D**2*A,D**2*AA[1]+D*C,D**2*AA[2]+2*D*Cj[1]-D.diff()*C]
    Q=quotient(det3([[f2[r],E[r],Cj[r]] for r in range(3)]),3*n-1)
    f3=[D**3*A,D**3*AA[1]+D**2*C,
        D**3*AA[2]+2*D**2*Cj[1]-D*D.diff()*C,
        D**3*AA[3]+3*D**2*Cj[2]-3*D*D.diff()*Cj[1]+(2*D.diff()**2-D*D.diff((z,2)))*C]
    a1=quotient(det3([[f3[r],E[r],Cj[r]] for r in (0,2,3)]),3*n-2)
    a0=-quotient(det3([[f3[r],E[r],Cj[r]] for r in (1,2,3)]),3*n-2)
    assert Q.degree()==3 and a1.degree()<=5 and a0.degree()<=4
    lead=Q.LC();qm=poly(Q.as_expr()/lead);p1=poly(a1.as_expr()/lead);p0=poly(a0.as_expr()/lead)
    qscaled=poly(qm.as_expr().subs(z,n*z)/n**3)
    a1scaled=poly(p1.as_expr().subs(z,n*z)/n**6)
    a0scaled=poly(p0.as_expr().subs(z,n*z)/n**6)
    roots=s.nroots(qm,n=80,maxsteps=200)
    intervals=s.polys.polytools.intervals(qm,eps=s.Rational(1,10**35))
    beta=B.nth(n-1)/B.nth(n)
    if C.degree()==n:
        ac=A.nth(n)/C.nth(n)
        V0=A.nth(n-1)-ac*C.nth(n-1)-C.nth(n)
        V1=A.nth(n-2)-ac*C.nth(n-2)-C.nth(n-1)
        assert V0!=0
        gamma=V1/V0
    else:
        assert C.degree()==n-1
        gamma=C.nth(n-2)/C.nth(n-1)
    q2=qm.nth(2)
    assert q2==beta+2*gamma+2
    assert p1.nth(4)==beta+3*n*n-n+(2*n-3)*q2
    assert p0.nth(3)==-n*beta-n**3-n*n-n*(n-2)*q2
    bp_roots=s.nroots(poly(B.as_expr()/B.LC()),n=60,maxsteps=300)
    cp_roots=s.nroots(poly(C.as_expr()/C.LC()),n=60,maxsteps=300)
    rec={'n':n,'elapsed_seconds':time.monotonic()-started,
         'monic_Q_exact':exacts(qm),'monic_Q_decimal':decimals(qm),
         'scaled_Q_exact':exacts(qscaled),'scaled_Q_decimal':decimals(qscaled),
         'scaled_A1_exact':exacts(a1scaled),'scaled_A1_decimal':decimals(a1scaled),
         'scaled_A0_exact':exacts(a0scaled),'scaled_A0_decimal':decimals(a0scaled),
         'Q_roots_80digits':list(map(str,roots)),'Q_roots_divided_by_n':[str(s.N(r/n,50)) for r in roots],
         'real_root_isolating_intervals':[[list(map(str,pair)),mult] for pair,mult in intervals],
         'Q_discriminant_sign':int(s.sign(s.discriminant(qm.as_expr(),z))),
         'B_max_root_modulus_divided_by_n':str(s.N(max(abs(r) for r in bp_roots)/n,30)),
         'C_max_root_modulus_divided_by_n':str(s.N(max(abs(r) for r in cp_roots)/n,30)),
         'beta_exact':str(beta),'gamma_exact':str(gamma),'beta_over_n_squared':str(s.N(beta/n**2,30)),
         'gamma_over_n_squared':str(s.N(gamma/n**2,30)),
         'root_sum_and_subleading_identities':True,
         'exact_polynomial_input':{'A':exacts(A),'B':exacts(B),'C':exacts(C)}}
    out['cases'].append(rec)
    (HERE/'raw_accessory_scaling_probe.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'n':n,'seconds':rec['elapsed_seconds'],'scaled_Q':rec['scaled_Q_decimal'],
         'scaled_A1':rec['scaled_A1_decimal'],'scaled_A0':rec['scaled_A0_decimal'],
         'Q_roots_over_n':[str(s.N(r/n,12)) for r in roots],
         'max_B_root_over_n':rec['B_max_root_modulus_divided_by_n'],
         'max_C_root_over_n':rec['C_max_root_modulus_divided_by_n']},indent=2),flush=True)
out['status']='passed'
(HERE/'raw_accessory_scaling_probe.json').write_text(json.dumps(out,indent=2)+'\n')
