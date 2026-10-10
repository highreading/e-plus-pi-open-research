"""Parent exact new response recurrence and bounded rational-gauge audit."""
from pathlib import Path
from math import comb, factorial
from fractions import Fraction as Q
import sympy as s
import hashlib,json,time
ROOT=Path(__file__).resolve().parent;start=time.monotonic()
n=s.symbols('n');D=n*(n+1)*(n+2)
U=s.Matrix([[0,(n+1)*(n+2),(n+2)/2],
 [n+2,-(n*n+3*n+1),-n*(n+2)/(2*(n+1))],
 [-(n+2)*(2*n+3),(n+2)*(n*n+3*n+1),(n+2)*(n*n-2)/(2*(n+1))]])
RR=s.Matrix([[0,1],[(n+1)/(n+2),(2*n+3)/(n+2)]])
K=s.kronecker_product(U,RR)
gamma=s.Matrix([[0,(n+2)/2,-(n+1)**2/2,((n+1)**2+1)/2,
                 -(n+1)/4,(n*n+3*n+3)/(4*(n+1))]])
clear=4*(n+1)*(n+2)*D*D.subs(n,n+1)
columns=[];maxdeg=0
for i in range(6):
    for j in range(7):
        polys=[]
        for k in range(6):
            value=clear*((n+1)**j/D.subs(n,n+1)*K[i,k]+
                         ((n+1)**2*n**j/D if i==k else 0))
            p=s.Poly(s.cancel(value),n);polys.append(p)
            if not p.is_zero:maxdeg=max(maxdeg,p.degree())
        columns.append(polys)
rhs=[s.Poly(s.cancel(clear*gamma[k]),n) for k in range(6)]
maxdeg=max(maxdeg,max(p.degree() for p in rhs if not p.is_zero))
assert maxdeg<=14
labels=[];rows=[];bb=[]
for k in range(6):
    for degree in range(maxdeg+1):
        row=[ps[k].nth(degree) for ps in columns];val=rhs[k].nth(degree)
        if any(row) or val:
            rows.append(row);bb.append(val);labels.append({'component':k,'degree':degree})
seed=[0,0,20,40,-132,-264]
rows.append([s.Rational(seed[i]*2**j,24) for i in range(6) for j in range(7)])
bb.append(14);labels.append({'seed':2})
A=s.Matrix(rows);rhscol=s.Matrix(bb)
aug=A.row_join(rhscol);reduced,piv=aug.rref()
rank_aug=len(piv);rank_A=sum(j<42 for j in piv)
result={'unknowns':42,'equations':A.rows,'max_cleared_degree':maxdeg,
        'denominator_class':'n(n+1)(n+2)','numerator_degree_at_most':6,
        'rank_A':rank_A,'rank_augmented':rank_aug}
if rank_aug>rank_A:
    witness=None
    for v in A.T.nullspace():
        value=(v.T*rhscol)[0]
        if value:
            witness=v/value;break
    assert witness is not None and witness.T*A==s.zeros(1,42) and (witness.T*rhscol)[0]==1
    result.update({'decision':'inconsistent in this specified degree and denominator class',
                   'exact_left_null_witness':[{'equation':i,'label':labels[i],'weight':str(v)}
                     for i,v in enumerate(witness) if v],
                   'witness_times_A_zero':True,'witness_times_rhs':1})
else:
    variables=s.symbols('c0:42')
    solution=s.linsolve((A,rhscol),variables)
    result.update({'decision':'solution exists in the specified class','solution':str(solution)})

# Independent exact construction of the source and moments at small auxiliary n.
tau={2:Q(2),3:Q(4)}
for r in range(2,24):tau[r+2]=((2*r+3)*tau[r+1]+(r+1)*tau[r])/(r+2)
states={};response={};transverse={}
for r in range(2,24):
    cap=r+1;lam=[1]+[0]*cap
    for _ in range(r):
        lam=[lam[j]-(j*lam[j-1] if j else 0)+(comb(j,2)*lam[j-2] if j>=2 else 0)
             for j in range(cap+1)]
    aa=[sum(comb(j,t)*lam[t] for t in range(j+1)) for j in range(cap+1)]
    us=[0]
    for j in range(cap):us.append((r+j+1)*us[-1]+1)
    vv=[sum(comb(j,t)*lam[t]*us[j-t] for t in range(j+1)) for j in range(cap+1)]
    bn=vv[r]-aa[r];bn1=vv[r+1]-aa[r+1]
    X=(r+1)*aa[r];Ym=(r+1)*r*aa[r-1];Z=2*aa[r+1]-(r+1)*aa[r]
    P=r*X+Ym;QQ=r*Z+2*X-Ym;F=2*(r+1)*(Z-QQ)
    states[r]=(P,QQ,F);response[r]=(Q(vv[r],factorial(r)),Q(vv[r+1],factorial(r+1)))
    transverse[r]=tau[r]*bn1-Q(r+1,2)*(tau[r]+tau[r+1])*bn
assert states[2]==(0,10,-66) and transverse[2]==14 and transverse[3]==-203
checks=[]
for r in range(2,23):
    z=s.Matrix(states[r]);nxt=U.subs(n,r)*z
    assert list(nxt)==list(states[r+1])
    tensor=s.Matrix([a*b for a in states[r] for b in (tau[r],tau[r+1])])
    forcing=(gamma.subs(n,r)*tensor)[0]
    assert s.Rational(transverse[r+1])==-(r+1)**2*s.Rational(transverse[r])+forcing
    v,w=response[r];vp,wp=response[r+1]
    # d_(r+1) reconstructed from the verified moment state at parameter r.
    P,QQ,F=states[r];X=(P-(r-1)*QQ-Q(r*F,2*(r+1)))/(r+2)
    Z=QQ+Q(F,2*(r+1))
    anext=Q(P+Z-(r+1)*X,2)
    assert vp==-(r+1)*v+2*(r+1)*w+anext/factorial(r+1)-tau[r+1]
    checks.append({'n':r,'transverse':str(transverse[r]),'next':str(transverse[r+1]),
                   'forcing':str(forcing),'residual':0})
out={'scope':'Exact bounded rational certificate class and21 auxiliary exact seeded recurrence checks. No unrestricted gauge nonexistence, original-contact gcd growth, geometric-subsequence primitive denominator or whole-error proof.',
     'gauge':result,'recurrence_cases':checks,'all_finite_recurrence_checks_passed':True,
     'elapsed_seconds':round(time.monotonic()-start,3),
     'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(ROOT/'endpoint_seeded_gauge_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'gauge':result['decision'],'rank_A':rank_A,'rank_augmented':rank_aug,
                  'recurrence_cases':len(checks),'seconds':out['elapsed_seconds']}),flush=True)
