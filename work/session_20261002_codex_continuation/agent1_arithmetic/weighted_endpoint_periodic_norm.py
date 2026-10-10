"""L24 exact periodic binary response and quadratic/linear separation.

No full new center nodes are computed. Existing residue states support the
all-degree coupled identities, with every linear correction retained.
"""
from pathlib import Path
import json
from weighted_endpoint_binary_inverse import inputs,matvec
from weighted_regular_dyadic_subfamily import eo_residues
from weighted_endpoint_coupled_symmetry import check as coupled_check

BASE=Path(__file__).resolve().parent


def check(m):
    B,C,w,t,L=inputs(m)
    x=matvec(C,w)
    x0=[a for d in range(m) for a in ((1,1),(0,0),(1,0))[d%3]]
    assert [a%2 for a in x]==x0
    x1=[((a-b)%4)//2 for a,b in zip(x,x0)]
    H=[[((B[2*d+1][2*e+1]-B[2*d][2*e])%4)//2 for e in range(m)]
       for d in range(m)]
    ell=[]
    for d in range(m):
        for s in range(2):
            ell.append((w[2*d+(s^1)]+sum(H[d][e]*x0[2*e+(s^1)]
                          for e in range(m))+(d==0))%2)
    k=[((w[i^1]-t[i])%8)//2 for i in range(2*m)]
    b=matvec(C,k,2)
    v=coupled_check(m)['v_vector_mod2']
    bv=[a^c for a,c in zip(b,v)]
    predicted=[int(s==1 and d%6 in (1,3)) for d in range(m) for s in range(2)]
    predicted[-2]^=1;predicted[-1]^=1
    assert bv==predicted
    Bx=matvec(B,x)
    E=[((a-c)%8)//2 for a,c in zip(Bx,w)]
    q0=sum(x0[i^1]*y for i,y in enumerate(matvec(B,x0)))%8
    S1=sum(a*c for a,c in zip(t,x))%8
    S2=sum(a*c for a,c in zip(matvec(C,t),Bx))%8
    reconstructed=(q0+4*sum(a*c for a,c in zip(ell,x1))
                      -2*sum(a*c for a,c in zip(k,x))
                      -4*sum(a*c for a,c in zip(b,E)))%8
    assert S2==reconstructed
    U=(q0-2*S1-2*sum(a*c for a,c in zip(ell,x0))
          +2*sum((a-c)*y for a,c,y in zip(ell,k,x))
          -2*sum(a*(y-z) for a,y,z in zip(bv,Bx,w)))%8
    assert U==coupled_check(m)['one_binomial_layer_normalized_endpoint_U_mod8']
    return {'m':m,'periodic_binary_response_valid':True,
            'period6_b_plus_v_valid_including_last_boundary':True,
            'periodic_quadratic_norm_q0_mod8':q0,
            'complete_reconstructed_U_mod8':U,
            'ell_vector_mod2':ell,'k_vector_mod4':k,
            'no_all_degree_residue4_inferred':True}


def run():
    e,o=eo_residues(15);table=[]
    for p in (2,8):
        for d in range(4):
            pairs=[]
            for a in range(2):
                z=0
                for s in range(d+1):
                    if s&~d:continue
                    j=(p-1-s)%15;r=(2*p-1-d+s)%15
                    z^=(e[j]*e[r]+o[j]*o[r])%2 if a==0 else (e[j]*o[r]+o[j]*e[r])%2
                pairs.append(z)
            table.append({'m_mod15':p,'index':d,'binary_response_P_E':pairs})
    out={'status':'AUTHOR periodic binary-response norm reduction',
         'fixed_field_binary_response_table':table,
         'existing_state_receipts':[check(m) for m in (2,8,32)],
         'full_actual_endpoint_U_digit_remains_unproved':True}
    (BASE/'WEIGHTED_ENDPOINT_PERIODIC_NORM_RECEIPT.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps([{k:r[k] for k in ('m','periodic_quadratic_norm_q0_mod8',
                'complete_reconstructed_U_mod8')} for r in out['existing_state_receipts']],indent=2))


if __name__=='__main__':run()
