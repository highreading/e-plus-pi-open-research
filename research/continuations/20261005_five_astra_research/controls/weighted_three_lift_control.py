"""One coordinator-authored n17 exact lift audit; finite evidence only."""
import json,math,resource
from pathlib import Path
import sympy as s
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
OUT=Path(__file__).resolve().parent
case=next(a for a in json.loads((OUT/'weighted_control.json').read_text()) if a['n']==17)
n=17;p=3;coeff=case['Q_coefficients']
der=[1]
for j in range(1,4*n+3):der.append(j*der[-1]+(-1)**j)
mu=[der[2*j] for j in range(2*n+2)]
def h(d):
    if d==0:return [1]
    poly=[math.comb(d-1,i)*(-1)**(d-1-i) for i in range(d)]
    ans=[0]*(d+1)
    for i,c in enumerate(poly):ans[i]+=c;ans[i+1]+=c
    return ans
def product(a,b):
    ans=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):ans[i+j]+=x*y
    return ans
def pairing(a,b):
    poly=product(a,b);return sum(c*(mu[i]-(-1)**i) for i,c in enumerate(poly))
basis=[h(i) for i in range(n+1)];div=[1]+[math.factorial(i-1) for i in range(1,n+1)]
G=s.Matrix(n,n,lambda i,j:s.Rational(pairing(basis[i],basis[j]),div[i]*div[j]))
assert all(a.q==1 for a in G)
for d in range(n-1):
    assert int(G[0,d+1])%3==2
    for e in range(n-1):assert int(G[d+1,e+1])%3==(-(d+e)*math.comb(d+e,d))%3
assert G[0,0]==0
I=list(range(1,n-1));Widx=[0,n-1]
E=G.extract(I,I);U=G.extract(I,Widx);W=G.extract(Widx,Widx)
assert int(E.det(method='domain-ge'))%3
Einv=E.inv(method='DM');Schur=W-U.T*Einv*U
omega=s.Matrix([s.Rational(pairing(basis[i],basis[n]),div[i]*div[n]) for i in range(n)])
xi=omega.extract(Widx,[0])-U.T*Einv*omega.extract(I,[0])
a,b,c=Schur[0,0],Schur[0,1],Schur[1,1]
delta=c-b*b/a
eta_last=s.cancel((xi[1]-b*xi[0]/a)/delta)
eta_const=s.cancel((xi[0]-b*eta_last)/a)
endpoint=-math.factorial(n-1)*eta_const
native=s.Rational(case['Q_minus_one'],coeff[-1]);assert endpoint==native

def vp(z):
    z=s.Rational(z)
    if z==0:return None
    def vi(k):
        k=abs(int(k));out=0
        while k%p==0:out+=1;k//=p
        return out
    return vi(z.p)-vi(z.q)
def unit(z):
    z=s.Rational(z);v=vp(z)
    if v is None:return None
    z=z/p**v if v>=0 else z*p**(-v)
    return int(z.p)%9*pow(int(z.q),-1,9)%9
record={'n':n,'prime':p,'all_divided_Gram_entries_integral':True,'all_residue_formulas_pass':True,
 'E_size':len(I),'E_unit':True,'scalar_lifts':{},'monic_endpoint_matches_native_primitive_Q':True,'finite_only':True}
for label,z in [('a',a),('b',b),('c',c),('delta',delta),('xi_const',xi[0]),('xi_last',xi[1]),('mixed_last_numerator',xi[1]-b*xi[0]/a),('eta_last',eta_last),('eta_const',eta_const),('monic_endpoint',endpoint)]:
 record['scalar_lifts'][label]={'valuation':vp(z),'first_unit_mod_9':unit(z),'exact':str(z)}
assert [[unit(z)%3 if vp(z)==0 else 0 for z in Schur.row(i)] for i in range(2)]==[[2,0],[0,0]]
print(json.dumps({'phase':'radical lift','valuations':{k:v['valuation'] for k,v in record['scalar_lifts'].items()} }),flush=True)
k=9;Ls=[s.Integer(0)]
for j in range(1,2*n):Ls.append(4*sum(s.Rational((-1)**v,2*j-1-2*v) for v in range(j)))
R=s.Matrix(k,k,lambda i,j:sum(coeff[t]*(-math.factorial(2*(i+j+t))+Ls[i+j+t]) for t in range(n+1)))
change=s.eye(k)
for j in range(1,k):change[0,j]=-(-1)**j
Rend=change.T*R*change;ell=int(s.ilcm(*range(1,4*n-2,2)));T=ell*Rend
assert all(z.q==1 for z in T)
A=int(T.det(method='domain-ge'));B=int(ell*case['Q_minus_one']*T[1:,1:].det(method='domain-ge'))
g=math.gcd(A,B);q=abs(B)//g
assert q==int(case['center_denominator'])
record['complete_endpoint_pair']={'ell':str(ell),'v_A':vp(A),'v_B':vp(B),'v_g':vp(g),'v_actual_q':vp(q),'actual_q_matches_previous_exact_reconstruction':True}
(OUT/'weighted_three_lift_control.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':'finite normalization and exact lift check passes','scalar_valuations':{k:v['valuation'] for k,v in record['scalar_lifts'].items()},'complete_endpoint_pair':record['complete_endpoint_pair']},indent=2))
