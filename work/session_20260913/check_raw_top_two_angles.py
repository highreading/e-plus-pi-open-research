"""Closed n4,n8,n16 principal-angle diagnostic using only exact F moments."""
import sys,json
from pathlib import Path
from math import factorial,comb
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'math_packages'))
import sympy as s
def moment(k,l):
    return s.Rational(factorial(k),factorial(2*k))*sum(
        s.Rational(comb(k,(k+d)//2)*factorial(k+d),factorial(d-l)*factorial(d+l+1))
        for d in range(l,k+1) if d%2==k%2)
out=[]
for n in (4,8,16):
    M=s.Matrix([[moment(k,l) for l in range(n+1)] for k in range(n+1,2*n)])
    A=M[:,:n-1];B=M[:,n-1:]
    detA=A.det()
    if detA==0:
        out.append({'n':n,'low_minor_zero':True,'rank':M.rank()})
        continue
    Z=-A.inv()*B
    sums=s.Matrix(2,2,lambda i,j:sum(Z[l,i]*Z[l,j]/(2*l+1) for l in range(n-1)))
    top=[2*n-1,2*n+1]
    k00=top[0]*sums[0,0];k11=top[1]*sums[1,1];k01sq=top[0]*top[1]*sums[0,1]**2
    tr=s.factor(k00+k11);de=s.factor(k00*k11-k01sq)
    disc=tr**2-4*de
    assert tr>=0 and de>=0 and disc>=0
    eigen=[(tr-s.sqrt(disc))/2,(tr+s.sqrt(disc))/2]
    graph=[s.sqrt(v) for v in eigen]
    sine=[s.sqrt(v/(1+v)) for v in eigen]
    out.append({'n':n,'low_minor_zero':False,'low_minor_sign':int(s.sign(detA)),
        'graph_columns':[[str(Z[l,j]) for j in range(2)] for l in range(n-1)],
        'orthonormal_graph_gram':{'k00':str(k00),'k11':str(k11),'k01_squared':str(k01sq),'trace':str(tr),'determinant':str(de)},
        'graph_singular_values':[str(s.N(v,20)) for v in graph],
        'principal_angle_sines':[str(s.N(v,20)) for v in sine],
        'n_times_worst_sine':str(s.N(n*sine[1],20)),
        'n_times_graph_norm':str(s.N(n*graph[1],20)),
        'top_low_rows':[[l,str(s.N(Z[l,0]*s.sqrt(s.Rational(top[0],2*l+1)),15)),str(s.N(Z[l,1]*s.sqrt(s.Rational(top[1],2*l+1)),15))] for l in range(max(0,n-5),n-1)],
        'exact_kernel_check':M*s.Matrix.vstack(Z,s.eye(2))==s.zeros(n-1,2)})
    print(json.dumps({k:out[-1][k] for k in ('n','low_minor_sign','graph_singular_values','principal_angle_sines','n_times_worst_sine','n_times_graph_norm','top_low_rows')},indent=2),flush=True)
res={'status':'complete','scope':'Only the predeclared moment blocks n4,n8,n16; no canonical raw degree construction. Decimal angles derive from exact rational 2x2 Gram data.','rows':out}
(HERE/'raw_top_two_angles.json').write_text(json.dumps(res,indent=2)+'\n')
