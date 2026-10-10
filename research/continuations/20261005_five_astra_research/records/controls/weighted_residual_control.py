"""New n=17 local audit, with exact primitive ray retained from reconstruction."""
import json
import math
import resource
from pathlib import Path
import sympy as s
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
OUT=Path(__file__).resolve().parent
case=next(a for a in json.loads((OUT/'weighted_control.json').read_text()) if a['n']==17)
n=17;r=8;k=9
coeff=case['Q_coefficients'];ell=s.ilcm(*range(1,4*n-2,2))
assert math.gcd(*coeff)==1 and coeff[-1]>0
der=[1]
for j in range(1,4*n):der.append(j*der[-1]+(-1)**j)
assert all(sum(coeff[a]*(der[2*(i+a)]-(-1)**(i+a)) for a in range(n+1))==0 for i in range(n))
Ls=[s.Integer(0)]
for v in range(1,2*n):Ls.append(4*sum(s.Rational((-1)**a,2*v-1-2*a) for a in range(v)))
R=s.Matrix(k,k,lambda i,j:sum(coeff[a]*(-math.factorial(2*(i+j+a))+Ls[i+j+a]) for a in range(n+1)))
basis=s.eye(k)
for j in range(1,k):basis[0,j]=-(-1)**j
Rend=basis.T*R*basis;T=ell*Rend
assert all(a.q==1 for a in T)
def rankmod(matrix,p):
    rows=[[int(a)%p for a in matrix.row(i)] for i in range(matrix.rows)];rank=0
    for col in range(matrix.cols):
        piv=next((i for i in range(rank,len(rows)) if rows[i][col]),None)
        if piv is None:continue
        rows[rank],rows[piv]=rows[piv],rows[rank]
        inv=pow(rows[rank][col],-1,p)
        for i in range(rank+1,len(rows)):
            f=rows[i][col]*inv%p
            rows[i]=[(a-f*b)%p for a,b in zip(rows[i],rows[rank])]
        rank+=1
    return rank
def detmod(matrix,p):
    return int(s.Matrix(matrix).det(method='domain-ge'))%p
records=[]
for p in (53,59,61):
    def residue(a):
        a=s.Rational(a);assert a.q%p
        return int(a.p)%p*pow(int(a.q),-1,p)%p
    degree=max(j for j,a in enumerate(coeff) if a%p)
    h=max(0,n+degree-(p+1)//2);size=k-h
    actualrank=rankmod(T,p);assert actualrank==h
    assert all(int(T[i,j])%p==0 for i in range(k) for j in range(k) if i<size or j<size)
    Efirst=[[int(T[i,j])//p%p for j in range(size)] for i in range(size)]
    unitell=int(ell)//p%p
    residual=Rend[:size,:size].applyfunc(residue)
    assert Efirst==[[unitell*int(a)%p for a in residual.row(i)] for i in range(size)]
    # Evaluate the pole-free formula using the native Q reduction, if allowed.
    window=degree>(p-1)//4
    def convolution(a,b):
        out=[0]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):out[i+j]+=x*y
        return out
    endpoints=[[1]]
    for i in range(1,size):endpoints.append([-(-1)**i]+[0]*(i-1)+[1])
    predicted=[]
    t=(p+1)//2
    for i in range(size):
        row=[]
        for j in range(size):
            f=convolution(convolution(coeff,endpoints[i]),endpoints[j])
            if window:
                assert len(f)-1<t
                value=sum((a%p)*residue(-math.factorial(2*v)+Ls[v]) for v,a in enumerate(f))%p
            else:
                f0=convolution(convolution([a%p for a in coeff[:degree+1]],endpoints[i]),endpoints[j])
                f1=convolution(convolution([(a-a%p)//p for a in coeff],endpoints[i]),endpoints[j])
                value=0
                for v,a in enumerate(f0):
                    regularL=4*sum(s.Rational((-1)**b,2*v-1-2*b) for b in range(v) if 2*v-1-2*b!=p)
                    value+=a*residue(-math.factorial(2*v)+regularL)
                value+=sum(a*4*(-1)**(v-t) for v,a in enumerate(f1) if v>=t)
                value%=p
            row.append(value)
        predicted.append(row)
    assert predicted==[[int(a) for a in residual.row(i)] for i in range(size)]
    Ndet=detmod(predicted,p)
    N0det=detmod([row[1:] for row in predicted[1:]],p) if size>1 else 1
    w=sum(a*(-1)**i for i,a in enumerate(coeff))%p
    record={'n':n,'prime':p,'native_primitive_ray_verified':True,'degree_mod_p':degree,
        'highest_pole_rank':h,'actual_pole_rank':actualrank,'residual_dimension':size,
        'pole_free_window':window,'Q_minus_one_mod_p':w,'det_N_mod_p':Ndet,
        'det_N0_mod_p':N0det,'residual_matrix_mod_p':predicted,
        'native_ray_coefficients_mod_p2':[a%(p*p) for a in coeff],
        'formula_agrees_with_exact_residual':True,
        'first_layer_both_units':bool(Ndet and w*N0det%p),
        'finite_only':True}
    records.append(record)
(OUT/'weighted_residual_control.json').write_text(json.dumps(records,indent=2)+'\n')
print(json.dumps([{a:v for a,v in rec.items() if a not in ('residual_matrix_mod_p','native_ray_coefficients_mod_p2')} for rec in records],indent=2))
