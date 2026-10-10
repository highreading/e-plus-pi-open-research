"""Coordinator implementation of the prescribed independent binomial sums."""
import math,json,resource
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
OUT=Path(__file__).resolve().parent
M=21;L=3*M
def moment(s,mod):
    total=0
    for ell in range(min(s,8)+1):
        rising=math.prod(range(s+1,s+ell+1))
        total+=math.comb(s,ell)*pow(-2,s-ell,mod)*rising
    return total%mod
def e(s,mod):
    return (4*moment(s,mod)+4*(s+1)*moment(s+1,mod)+(s+1)*(s+2)*moment(s+2,mod))%mod
tau=[(-1)**(M-d)*math.comb(M,d) for d in range(M+1)]
R=sum(tau[d]*tau[z]*math.comb(3*(d+z),3*d)*e(3*(d+z),27)
      for d in range(M+1) for z in range(M+1))%27
assert R%3==0
X=sum(tau[d]*tau[z]*math.comb(3*(d+z)+1,3*d)*e(3*(d+z)+1,9)
      for d in range(M+1) for z in range(M+1))%9
u=[]
for i in range(L):
    v=sum(tau[d]*math.comb(i+3*d,i)*e(i+3*d,9) for d in range(M+1))%9
    assert v%3==0
    u.append(v//3)
Binv=[[((-1)**(q+r))*sum(math.comb(a,q)*math.comb(a,r) for a in range(max(q,r),M))%3
       for r in range(M)] for q in range(M)]
Ainv=[[0,0,1],[0,2,2],[1,2,2]]
norm=sum(u[i]*Binv[i//3][j//3]*Ainv[i%3][j%3]*u[j] for i in range(L) for j in range(L))%3
cdiv3=(R//3-3*norm)%9
eta3=X*pow(cdiv3,-1,9)%9
assert cdiv3==4 and X==2 and eta3==5
report={'M':M,'n':65,'R_mod27':R,'R_div3_mod9':R//3,'u_mod3':u,
        'u_J_u_mod3':norm,'mixed_binomial_sum_X_mod9':X,'c_div3_mod9':cdiv3,
        'three_eta_last_mod9':eta3,'independent_sum_predictions_pass':True,'finite_only':True}
(OUT/'weighted_pascal_digit_control.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report))
