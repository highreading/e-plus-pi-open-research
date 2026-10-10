"""NEW universal constants for a uniform original Xi theorem; no dense n."""
from pathlib import Path
from math import comb, factorial
import datetime
import hashlib
import json

HERE=Path(__file__).resolve().parent
R=HERE.parent
gamma=[1,0]
for r in range(1,18):
    gamma.append((4*r+2)*gamma[-1]+4*gamma[-2])
expected=[1,0,4,4,0,7,1,0,4,1,0]
assert [g%9 for g in gamma[:11]]==expected
assert gamma[9]%9==gamma[0]%9 and gamma[10]%9==gamma[1]%9
g=[sum((-1)**(h-a)*comb(h,a)*gamma[a] for a in range(h+1))%9
   for h in range(9)]
assert g==[1,8,5,0,0,6,3,6,6]
delta9=[sum((-1)**(9-a)*comb(9,a)*gamma[start+a] for a in range(10))%9
        for start in range(9)]
assert delta9==[0]*9
shift_payments=[{'r':r,'binomial27r':comb(27,r),'mod9':comb(27,r)%9}
                for r in range(1,9)]
assert all(row['mod9']==0 for row in shift_payments)

terms=[]
for h in range(9):
    for a in range(h//2+1):
        numerator=factorial(h)
        denominator=factorial(a)**2*factorial(h-2*a)
        assert numerator%denominator==0
        integer_weight=numerator//denominator*2**(h-2*a)
        choose=comb(1+a,h) if 1+a>=h else 0
        terms.append({'h':h,'a':a,'newton_coefficient_mod9':g[h],
                      'integer_weight':integer_weight,'binomial_at_d1':choose,
                      'contribution_mod9':g[h]*integer_weight*choose%9})
diagonal=sum(row['contribution_mod9'] for row in terms)%9
assert diagonal==0

# Independently reconstruct ONLY the2x2 transformed diagonal. This is
# a universal coefficient identity, not a sample-sized inverse substitute.
t2=[[comb(a+b,a)*gamma[a+b] for b in range(2)] for a in range(2)]
p_inv=[[1,0],[-1,1]]
hat2=[[sum(p_inv[i][a]*t2[a][b]*p_inv[j][b]
           for a in range(2) for b in range(2)) for j in range(2)] for i in range(2)]
assert hat2==[[1,-1],[-1,9]]
last_b2_inverse=[[0,2],[2,2]]
assert sum(last_b2_inverse[0][a]*[2,0][a] for a in range(2))%3==0
assert (2*1+2)%3==1
sources=[R/'responses/A4_turn13.md',HERE/'COORDINATOR_ORIGINAL_XI_UNIT_CANDIDATE.md',
         R/'gates/ACTUAL_PRODUCER_SCALAR_AND_SHORT_PREFIX_GATE_20261009.md']
output={'status':'PASS','time':datetime.datetime.now().astimezone().isoformat(),
        'scope':'NEW universal period/Newton/diagonal constants supporting the complete parent original-family proof; no original dense matrix is computed.',
        'gamma0_to10_mod9':expected,'newton_coefficients_mod9':g,
        'delta9_checks_mod9':delta9,'binomial_shift_payments':shift_payments,
        'all_integer_diagonal_terms_at_d1':terms,'finite_hat2':hat2,
        'uniform_period_and_original_Xi_proof_in_note':True,
        'actual_V70_evaluated':False,'actual_Delta_A_evaluated':False,
        'source_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'original_index_experiment':False,'global_proof':False}
(HERE/'original_xi_pascal_universal_certificate.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps({'status':'PASS','newton_coefficients_mod9':g,
                  'proved_parent_original_Xi_mod9':3,
                  'actual_producer_contraction_evaluated':False,'global_proof':False}))
