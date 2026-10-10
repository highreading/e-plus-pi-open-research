# New finite criterion verification for the October 2 candidate only.
import json, math
from fractions import Fraction
from pathlib import Path
root=Path('work/session_20261002_codex_continuation')
src=json.loads((root/'agent1_arithmetic/ODD_PRIME_ATLAS_CERTIFICATE.json').read_text())
ps=src['selected']
def matmul(A,B,p):
    return [[sum(x*y for x,y in zip(row,col))%p for col in zip(*B)] for row in A]
def mv(A,x,p): return [sum(a*b for a,b in zip(row,x))%p for row in A]
def tr(A): return list(map(list,zip(*A)))
def det(A,p):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])-A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])+A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))%p
def adj(A,p):
    C=[]
    for j in range(3):
        row=[]
        for i in range(3):
            rows=[k for k in range(3) if k!=i]; cols=[k for k in range(3) if k!=j]
            row.append(((-1)**(i+j)*(A[rows[0]][cols[0]]*A[rows[1]][cols[1]]-A[rows[0]][cols[1]]*A[rows[1]][cols[0]]))%p)
        C.append(row)
    return C
def conv(A,B,p):
    C=[0]*(len(A)+len(B)-1)
    for i,a in enumerate(A):
        for j,b in enumerate(B): C[i+j]=(C[i+j]+a*b)%p
    return C
def ppow(A,n,p):
    B=[1]
    for _ in range(n): B=conv(B,A,p)
    return B
out=[]
for p in ps:
    assert all(p%q for q in range(2,math.isqrt(p)+1))
    inv2=pow(2,-1,p)
    P=ppow([1,-4,-4],(p-1)//2,p)
    assert len(P)==p
    getP=lambda n:P[n%p]*([1,2][n//p] if n//p<=1 else 0)%p
    dc=[1]
    for j in range(1,2*p+2): dc.append((j*dc[-1]+1)%p)
    C=sum((-1)**j*math.factorial(j) for j in range(p))%p
    Q=[1]
    vals=[]
    for r in range(p):
        ff=[]
        for i in range(3):
            ffrow=[1]
            for j in range(1,r+i+3):
                ffrow.append(ffrow[-1]*(r+i-j+1)%p)
            ff.append(ffrow)
        N=[[sum(Q[s]*ff[i][s+j] for s in range(min(len(Q)-1,r+i-j)+1))%p for j in range(3)] for i in range(3)]
        A=[sum(Q[s]*ff[i][s]*dc[2*r+i-s] for s in range(min(len(Q)-1,r+i)+1))%p for i in range(3)]
        K=[[-1,r,-r*(r+1)],[1,-r-1,r*(r+3)],[0,1,-2*r-1],[0,0,1]]
        om=[1,(r+2)**2,((r+1)*(r+2))**2,((r+1)*(r+2)*r)**2]
        H=matmul(tr(K),[[om[i]*x%p for x in K[i]] for i in range(4)],p)
        J=[getP(r),(getP(r)*inv2+getP(r+1)*pow(4,-1,p))%p,getP(r+2)*pow(8,-1,p)%p]
        DJ=[J[0],(r+1)*J[1]%p,(r+1)*(r+2)*J[2]%p]
        adjN=adj(N,p); Y=mv(adjN,DJ,p)
        ha=mv(H,mv(adjN,A,p),p)
        W=[(ha[i]+det(N,p)*K[0][i])%p for i in range(3)]
        V=sum(y*w for y,w in zip(Y,W))%p
        vals.append(V)
        Q=conv(Q,[1,-1,inv2],p)
    source=next(x for x in src['residues'] if x['p']==p)
    row=dict(p=p,seeds=p,all_P_units=all(P),only_origin_V_zero=vals[0]==0 and all(vals[1:]),origin_coefficient_unit=(3*C+4)%p!=0,C=C,P_matches_author=P==source['P_residues'],V_matches_author=vals==source['V_residues'])
    assert all(row[k] for k in ['all_P_units','only_origin_V_zero','origin_coefficient_unit','P_matches_author','V_matches_author'])
    out.append(row)
gap_ok=Fraction(src['rho_lower'])>Fraction(src['tau_upper'])
assert gap_ok
report=dict(status='PASS finite criterion and stored exact gap comparison',scope='17 selected odd primes; no high-index scan or analytic infrastructure replay',rows=out,seeds=sum(ps),exact_gap_positive=gap_ok)
Path(__file__).with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))

