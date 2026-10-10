"""L24 coupled-member elimination of the second internal binomial layer.

Checks the new symbolic identity at existing states only. The all-degree
residue4 evaluation is still a separate carry-sum problem.
"""
from pathlib import Path
import json
from weighted_endpoint_binary_inverse import inputs,matvec
from weighted_regular_dyadic_subfamily import eo_residues

BASE=Path(__file__).resolve().parent


def check(m):
    B,C,w,t,L=inputs(m)
    H=[[((B[2*d+1][2*e+1]-B[2*d][2*e])%4)//2
        for e in range(m)] for d in range(m)]
    Hrev=[[H[m-1-d][m-1-e] for e in range(m)] for d in range(m)]
    def diag_Hrev_mv(v):
        out=[0]*(2*m)
        for d in range(m):
            for s in range(2):
                out[2*d+s]=sum(Hrev[d][e]*v[2*e+s] for e in range(m))%2
        return out
    # E=(BC-I)/2. Here only its action on w is needed modulo4.
    x=matvec(C,w)
    Bx=matvec(B,x)
    Ew=[((a-b)%8)//2 for a,b in zip(Bx,w)]
    CEw=matvec(C,Ew)
    E2w=[((a-b)%4)//2 for a,b in zip(matvec(B,CEw,4),Ew)]
    CE2w=matvec(C,E2w,2)
    oldQ=sum(a*b for a,b in zip(t,CE2w))%2
    hw=diag_Hrev_mv(w)
    v=[hw[i^1] for i in range(2*m)]
    v[-2]^=1;v[-1]^=1
    periodic={2:{1:(0,1),3:(1,0),5:(1,1)},
              8:{1:(1,0),3:(1,1),5:(1,1)}}
    predicted=[0]*(2*m)
    for d in range(1,m,2):
        predicted[2*d:2*d+2]=periodic[m%15][d%6]
    predicted[2]^=1
    predicted[-2]^=1;predicted[-1]^=1
    assert v==predicted
    newQ=sum(a*b for a,b in zip(v,Ew))%2
    assert oldQ==newQ
    S1=sum(a*b for a,b in zip(t,x))%8
    S2=sum(a*b for a,b in zip(t,matvec(C,Bx)))%8
    U=(S2-2*S1-2*sum(a*(b-c) for a,b,c in zip(v,Bx,w)))%8
    original=(L-S1+2*sum(a*b for a,b in zip(t,CEw))-4*oldQ)%8
    assert L==0 and U==original
    return {'m':m,'n':2*m+1,'quadratic_second_carry_old_and_new_mod2':[oldQ,newQ],
            'one_binomial_layer_normalized_endpoint_U_mod8':U,
            'remaining_all_degree_residue4_not_inferred':True,
            'v_vector_mod2':v}


def run():
    e,o=eo_residues(15)
    finite_table=[]
    for p in (2,8):
        for d in (1,3,5,7):
            action=[sum(e[(p-1-s)%15]*f[(2*p-d+s)%15]
                        for s in range(d) if not(s & ~(d-1)))%2
                    for f in (e,o)]
            finite_table.append({'m_mod15':p,'odd_degree':d,
                                 'H_reversed_omega_P_E':action})
    out={'status':'AUTHOR coupled-symmetry removal of second binomial layer',
         'receipts':[check(m) for m in (2,8,32)],
         'fixed_field_periodic_vector_boundary_table':finite_table,
         'one_internal_B_layer_suffices_at_all_regular_degrees':True,
         'exact_q2_n_plus2_still_unproved':True}
    (BASE/'WEIGHTED_ENDPOINT_COUPLED_SYMMETRY_RECEIPT.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps([{k:r[k] for k in ('m','quadratic_second_carry_old_and_new_mod2',
                'one_binomial_layer_normalized_endpoint_U_mod8')} for r in out['receipts']],indent=2))


if __name__=='__main__':run()
