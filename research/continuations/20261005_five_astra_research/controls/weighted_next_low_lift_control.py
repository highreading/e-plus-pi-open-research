"""Single first-low-block second lift using derived local Q65=3P65 modulo9."""
import json,math,resource
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
OUT=Path(__file__).resolve().parent
n=65;m=32;d=26;size=33;mod=9
receipt=json.loads((OUT/'weighted_next_three_lift_control.json').read_text())
c=int(receipt['values']['c']['residue']);xi=int(receipt['values']['xi_last']['residue'])
eta3=(xi%9)*pow((c//3)%9,-1,9)%9
assert eta3==5
def mul(a,b,modulus):
    result=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):result[i+j]=(result[i+j]+x*y)%modulus
    return result
def basis(i):
    if i==0:return [1]
    return [0]*(i-1)+[1,1]
delta=[((-1)**(63-k))*math.comb(63,k)%9 for k in range(64)]
# Tail ratios N!/e! contain63, depth2, for every e<=62. Thus locally
# 3P=(y+1)(y-1)^63[3(y-1)-64*(3eta_last)] modulo9.
core=mul(delta,[(-3-64*eta3)%9,3],9)
ray=[x%3 for x in delta]
def coefficient(poly,k):return poly[k] if 0<=k<len(poly) else 0
def coeffpair(poly,i,j,k,modulus):return coefficient(mul(mul(poly,basis(i),modulus),basis(j),modulus),k)%modulus
def inverse(matrix,modulus):
    p=3;k=len(matrix);rows=[row[:]+[int(i==j) for j in range(k)] for i,row in enumerate(matrix)]
    for j in range(k):
        pivot=next(i for i in range(j,k) if rows[i][j]%p)
        rows[j],rows[pivot]=rows[pivot],rows[j]
        inv=pow(rows[j][j],-1,modulus);rows[j]=[x*inv%modulus for x in rows[j]]
        for i in range(k):
            if i!=j:
                f=rows[i][j]
                if f:rows[i]=[(x-f*y)%modulus for x,y in zip(rows[i],rows[j])]
    return [row[k:] for row in rows]
def matmul(A,B,modulus):
    return [[sum(x*y for x,y in zip(row,col))%modulus for col in zip(*B)] for row in A]
def transpose(A):return [list(x) for x in zip(*A)]
E=[[coeffpair(ray,i,j,121,3) for j in range(d,size)] for i in range(d,size)]
Einv=inverse(E,3)
X=[[coeffpair(ray,i,j,40,3)+int(i==25 and j==32) for j in range(d,size)] for i in range(d)]
X=[[v%3 for v in row] for row in X]
cross=matmul(matmul(X,Einv,3),transpose(X),3)
S=[[(coeffpair(core,i,j,40,9)+3*sum(pow(a,-1,3)*coeffpair(ray,i,j,(27*a-1)//2,3) for a in (1,5,7))-3*cross[i][j])%9
    for j in range(d)] for i in range(d)]
M=json.loads((OUT/'weighted_first_low_rank_control.json').read_text())['matrix_mod3']
C=[[int(i==0 and j==0) if j==0 else int(i==j or i==j-1) for j in range(d)] for i in range(d)]
expected=matmul(matmul(transpose(C),M,3),C,3)
assert [[v%3 for v in row] for row in S]==expected
rank=18;E1=[row[:rank] for row in S[:rank]];F=[row[rank:] for row in S[:rank]];D1=[row[rank:] for row in S[rank:]]
E1inv=inverse(E1,9);corr=matmul(matmul(transpose(F),E1inv,9),F,9)
schur=[[(D1[i][j]-corr[i][j])%9 for j in range(d-rank)] for i in range(d-rank)]
assert all(x%3==0 for row in schur for x in row)
W=[[x//3 for x in row] for row in schur]
e0=[int(i==0) for i in range(rank)]
response=matmul(E1inv,[[x] for x in e0],9)
projected=[-sum(F[i][j]*response[i][0] for i in range(rank))%3 for j in range(d-rank)]
try:
    Winv=inverse(W,3);norm=sum(projected[i]*Winv[i][j]*projected[j] for i in range(len(W)) for j in range(len(W)))%3
    Wunit=True
except StopIteration:
    norm=None;Wunit=False
report={'n':n,'local_polynomial_normalization':'3 times actual monic P65; differs from primitive Q by a 3-unit',
 'polynomial_digit_derivation_requires_audit':True,'three_eta_last_mod9':eta3,
 'first_low_S_divided_global_unit_mod9':S,'first_low_rank_mod3':rank,
 'next_radical_dimension':d-rank,'next_radical_matrix_mod3':W,
 'distinguished_endpoint_projection_mod3':projected,'next_radical_is_unit':Wunit,
 'distinguished_inverse_pole_unit':norm,
 'actual_S_inverse_endpoint_depth_if_digit_derivation_passes':-1 if Wunit and norm else None,
 'actual_endpoint_A_depth_if_digit_derivation_passes':d+(d-rank) if Wunit else None,
 'actual_q3_depth_if_endpoint_and_digit_proofs_pass':63 if Wunit and norm else None,
 'finite_only':True}
(OUT/'weighted_next_low_lift_control.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if 'matrix' not in k and 'mod9' not in k},indent=2))
