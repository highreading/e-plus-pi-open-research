"""One fixed n15,p17,b6 full-center and local-metric audit."""
import itertools,json,math,resource
from pathlib import Path
import sympy as s
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
OUT=Path(__file__).resolve().parent
n=15;p=17;b=6;ell=17;tail=2
x=s.Symbol('x')
phi=[s.Integer(1)];F={}
for k in range(n+b):
    F[k]=[int(math.prod(range(k-j+1,k+1))*phi[j]) for j in range(k+1)]
    nxt=[s.Integer(0)]*(len(phi)+2)
    for j,a in enumerate(phi):nxt[j]+=a;nxt[j+1]-=a;nxt[j+2]+=a/2
    phi=nxt

def fall(k,j):return math.prod(range(k-j+1,k+1))
def E(k,j):return sum(a*fall(2*k-t,j) for t,a in enumerate(F[k]))
def residue(z,mod=p):
    z=s.Rational(z);assert int(z.q)%p
    return int(z.p)%mod*pow(int(z.q),-1,mod)%mod
def rankmod(M):
    rows=[[residue(a) for a in M.row(i)] for i in range(M.rows)];rank=0
    for col in range(M.cols):
        pivot=next((i for i in range(rank,len(rows)) if rows[i][col]),None)
        if pivot is None:continue
        rows[rank],rows[pivot]=rows[pivot],rows[rank];inv=pow(rows[rank][col],-1,p)
        for i in range(rank+1,len(rows)):
            factor=rows[i][col]*inv%p;rows[i]=[(a-factor*c)%p for a,c in zip(rows[i],rows[rank])]
        rank+=1
    return rank

def vp(z):
    z=s.Rational(z)
    if not z:return None
    def vi(v):
        v=abs(int(v));a=0
        while v%p==0:v//=p;a+=1
        return a
    return vi(z.p)-vi(z.q)
R=s.Matrix(b-2,b+1,lambda i,j:E(n+i+1,i+j))
Rnormalized=R.copy();assert all(int(z)%p==0 for z in R.row(1))
Rnormalized[1,:]=Rnormalized[1,:]/p
P=s.Poly(s.expand(2**n*s.I**n*s.legendre(n,-s.I*(2*x-1))),x)
U=s.Poly(s.expand(2**(n+1)*s.I**(n+1)*s.legendre(n+1,-s.I*(2*x-1))),x)
assert all(a.is_Integer for a in P.all_coeffs()+U.all_coeffs())
def moment(j):return 2*sum(s.Rational(math.comb(j,h)*(-1)**(h//2),h+1) for h in range(0,j+1,2))/2**j
def second(poly):
    q,rem=s.div(poly-s.Poly(poly.eval(1),x),s.Poly(x-1,x));assert rem.is_zero
    return sum(q.nth(j)*moment(j) for j in range(q.degree()+1))
wP=second(P);wU=second(U);G=P.eval(1)*wU-U.eval(1)*wP
assert G==s.Rational((-1)**n*2**(2*n+3),n+1)
partials=[s.Integer(1)]
for j in range(1,2*n+3):partials.append(partials[-1]+s.Rational(1,math.factorial(j)))
def Tj(poly,j):return sum(poly.nth(t)*partials[n+t-j] for t in range(poly.degree()+1))
TP=[Tj(P,j) for j in range(b+1)];TU=[Tj(U,j) for j in range(b+1)]
t=s.Matrix(1,b+1,lambda i,j:s.cancel((P.eval(1)*TU[j]-U.eval(1)*TP[j])/G))
aendpoint=s.Matrix(1,b+1,lambda i,j:s.cancel((wP*TU[j]-wU*TP[j])/G))
erow=s.ones(1,b+1);matching=erow+t
assert all(s.Rational(z).q%p for z in list(t)+list(aendpoint))
full=Rnormalized.col_join(matching);assert rankmod(Rnormalized)==4
rankM=rankmod(full);rankE=rankmod(full.col_join(erow));rankX=rankmod(full.col_join(aendpoint))
assert rankM==5
# Actual p-unit pivot chart for the complete matching lattice.
pivots=next(cols for cols in itertools.combinations(range(b+1),5) if residue(full.extract(range(5),cols).det(method='domain-ge')))
free=[j for j in range(b+1) if j not in pivots]
BP=full.extract(range(5),pivots);CP=full.extract(range(5),free);upper=-BP.inv(method='DM')*CP
K=s.zeros(b+1,2)
for i,j in enumerate(pivots):K[j,:]=upper[i,:]
for i,j in enumerate(free):K[j,i]=1
assert full*K==s.zeros(5,2)
C=(aendpoint*K).col_join(erow*K);assert C.det()!=0
Psi=K*C.inv();uu=Psi[:,0];vv=Psi[:,1]
assert aendpoint*uu==s.Matrix([1]) and erow*uu==s.Matrix([0])
assert aendpoint*vv==s.Matrix([0]) and erow*vv==s.Matrix([1])
weights=[math.factorial(ell)//math.factorial(ell-j) for j in range(b+1)]
Omega=s.diag(*[w*w for w in weights])
A=(uu.T*Omega*uu)[0];H=(uu.T*Omega*vv)[0];center=s.cancel(H/A)
# Primitive local zero-B direction uses the endpoint row, retaining the full chart.
e0,e1=(erow*K)[0,0],(erow*K)[0,1]
z0=e1*K[:,0]-e0*K[:,1]
assert erow*z0==s.Matrix([0])
assert min(vp(z) for z in z0 if z)==0
norm=(z0.T*Omega*z0)[0]
D=[residue(s.Rational((-1)**(j-1)*math.factorial(j-1))*z0[j]) for j in range(tail,b+1)]
metric_prediction=(sum(d*d for d in D)+sum((j+2)*D[j-tail] for j in range(tail,b+1))**2)%p
assert residue(norm/p**2)==metric_prediction
c_s=(-1)**tail*math.factorial(tail)
Evalues=[E(p-1,tail+r)%p for r in range(5)]
de=[(-1)**r*math.prod(range(tail+1,tail+r+1))%p for r in range(5)]
e=[v*pow(c_s,-1,p)%p for v in Evalues]
f=[sum(de[1:r+1])%p for r in range(5)]
grow=[sum(e[1:r+1])%p for r in range(5)]
Ws=TP[tail]+TU[tail]/2;epsilon=pow(-1,(p-1)//2,p)
Theta=(2*epsilon-residue(Ws)-Evalues[0])*pow(c_s,-1,p)%p
Dpoly=(tail*tail+5*tail+8)%p
fit=s.Matrix([[1,de[r],f[r]] for r in range(3)]).inv()*s.Matrix(e[:3])
fitvals=[residue(z) for z in fit]
record={'n':n,'prime':p,'b':b,'metric':'diag((17!/(17-j)!)^2), j0..6','high_normalized_rank':rankmod(Rnormalized),
 'matching_rank':rankM,'appended_endpoint_sum_rank':rankE,'appended_A_endpoint_rank':rankX,
 'complete_matching_unit_pivot_columns':list(pivots),'endpoint_rows_p_integral':True,
 'tail_system':{'s':tail,'d':de,'e':e,'f':f,'g':grow,'Theta':Theta,'H_s':Dpoly,'fit_A_B_C':fitvals,
 'obstruction_residues':[(Dpoly*fitvals[0]-2*(tail+1)*(tail+3))%p,(Dpoly*fitvals[2]-2*(Dpoly-1))%p]},
 'zero_endpoint_metric':{'valuation':vp(norm),'norm_div_p2_mod_p':residue(norm/p**2),'five_tail_plus_rank_one_prediction':metric_prediction,'rank_one_term_retained':True},
 'actual_center':{'numerator':str(center.p),'denominator':str(center.q),'v_p_actual_q':vp(center.q),'actual_normalized_Psi_endpoint_tests_pass':True},
 'finite_only':True}
(OUT/'proportional_five_tail_control.json').write_text(json.dumps(record,indent=2)+'\n')
brief={key:value for key,value in record.items() if key!='actual_center'}
brief['actual_center_v_p_q']=vp(center.q)
print(json.dumps(brief,indent=2))
