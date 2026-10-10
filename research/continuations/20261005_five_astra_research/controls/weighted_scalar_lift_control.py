"""Coordinator-authored prescribed n65 third lift, retaining all needed poles."""
import math,json,resource
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
OUT=Path(__file__).resolve().parent
n=65;size=33;d=26;rank=18
receipt=json.loads((OUT/'weighted_next_three_lift_control.json').read_text())
c=int(receipt['values']['c']['residue']);xi=int(receipt['values']['xi_last']['residue'])
eta3=(xi%27)*pow((c//3)%27,-1,27)%27
assert eta3==5 and c%81==39 and xi%27==11
def mul(a,b,mod):
    z=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):z[i+j]=(z[i+j]+x*y)%mod
    return z
def basis(i):return [1] if i==0 else [0]*(i-1)+[1,1]
delta=[(-1)**(63-k)*math.comb(63,k)%27 for k in range(64)]
core=mul(delta,[1,3],27)
def coeff(i,j,k,mod):
    poly=mul(mul(core,basis(i),mod),basis(j),mod)
    return poly[k]%mod if 0<=k<len(poly) else 0
def inv(A,mod):
    k=len(A);rows=[list(row)+[int(i==j) for j in range(k)] for i,row in enumerate(A)]
    for j in range(k):
        pivot=next(i for i in range(j,k) if rows[i][j]%3)
        rows[j],rows[pivot]=rows[pivot],rows[j]
        unit=pow(rows[j][j],-1,mod);rows[j]=[x*unit%mod for x in rows[j]]
        for i in range(k):
            if i!=j:
                f=rows[i][j]
                if f:rows[i]=[(x-f*y)%mod for x,y in zip(rows[i],rows[j])]
    return [row[k:] for row in rows]
def trans(A):return [list(x) for x in zip(*A)]
def prod(A,B,mod):return [[sum(x*y for x,y in zip(row,col))%mod for col in zip(*B)] for row in A]
E=[[(coeff(i,j,121,9)+3*coeff(i,j,40,3))%9 for j in range(d,size)] for i in range(d,size)]
Ei=inv(E,9)
X=[[(int(i==25 and j==32)+coeff(i,j,40,9)+3*sum(pow(a,-1,3)*coeff(i,j,(27*a-1)//2,3) for a in (1,5,7)))%9
    for j in range(d,size)] for i in range(d)]
cross=prod(prod(X,Ei,9),trans(X),9)
oddunits=(1,5,7,11,13,17,19,23,25)
S=[[(coeff(i,j,40,27)+3*sum(pow(a,-1,9)*coeff(i,j,(27*a-1)//2,9) for a in (1,5,7))
      +9*sum(pow(a,-1,3)*coeff(i,j,(9*a-1)//2,3) for a in oddunits)-3*cross[i][j])%27
    for j in range(d)] for i in range(d)]
old=json.loads((OUT/'weighted_next_low_lift_control.json').read_text())
assert [[x%9 for x in row] for row in S]==old['first_low_S_divided_global_unit_mod9']
E1=[row[:rank] for row in S[:rank]];F=[row[rank:] for row in S[:rank]];D1=[row[rank:] for row in S[rank:]]
E1i=inv(E1,27);corr=prod(prod(trans(F),E1i,27),F,27)
schur=[[(D1[i][j]-corr[i][j])%27 for j in range(8)] for i in range(8)]
assert all(x%3==0 for row in schur for x in row)
W=[[x//3 for x in row] for row in schur]
assert [[x%3 for x in row] for row in W]==old['next_radical_matrix_mod3']
k=[1,2,1,2,1,2,0,0]
Wk=[sum(row[j]*k[j] for j in range(8))%9 for row in W]
ksWk=sum(k[i]*Wk[i] for i in range(8))%9
assert all(x%3==0 for x in Wk) and ksWk%3==0
J=[row[1:] for row in W[1:]];Ji=inv(J,9)
v=Wk[1:]
correction=sum(v[i]*Ji[i][j]*v[j] for i in range(7) for j in range(7))%9
tau_scalar=(ksWk-correction)%9
assert tau_scalar%3==0 and tau_scalar//3==ksWk//3
endpoint=prod(E1i,[[int(i==0)] for i in range(rank)],27)
projection=[-sum(F[i][j]*endpoint[i][0] for i in range(rank))%3 for j in range(8)]
endpoint_scalar=sum(x*y for x,y in zip(projection,k))%3
assert endpoint_scalar==1
tau=tau_scalar//3
report={'n':65,'three_eta_last_mod27':eta3,'polynomial_mod27_assumption_paper_audited':True,
 'first_low_S_divided_global_unit_mod27':S,'next_radical_W_mod9':W,
 'previous_lift_reductions_pass':True,'last_radical_mod3':k,'Wk_mod9':Wk,
 'k_W_k_mod9':ksWk,'tau_mod3_from_full_scalar_Schur':tau,
 'tau_mod3_from_direct_radical':ksWk//3,'endpoint_projection_mod3':projection,
 'last_endpoint_scalar_mod3':endpoint_scalar,'tau_is_unit':bool(tau),
 'finite_A_depth_if_unit':35 if tau else None,'finite_B_depth':97,
 'finite_actual_q3_depth_if_unit':62 if tau else None,'finite_only':True}
(OUT/'weighted_scalar_lift_control.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if 'matrix' not in k and 'mod27' not in k and 'W_mod9' not in k}))
