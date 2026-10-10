"""L24 first contraction: exact 225-state all-degree transfer.

The terminal table is a finite residue certificate, not a degree atlas.
The two internal-binomial contractions remain separate unresolved objects.
"""
from pathlib import Path
from math import comb
import json
from weighted_endpoint_binary_inverse import inputs, rho, matvec
from weighted_branch_mod8_lift import series
from weighted_regular_dyadic_subfamily import eo_residues

BASE=Path(__file__).resolve().parent
KAPPA=[1,5,7,3]


def index(a,b):return 15*a+b


def step(v):
    out=[0]*225
    for a in range(15):
        for b in range(15):
            w=v[index(a,b)]
            for x,y in ((0,1),(1,0),(1,1)):
                j=index((2*a+x)%15,(2*b+y)%15)
                out[j]=(out[j]+w)%8
    return out


def initial():
    v=[0]*225
    for a in range(4):
        for b in range(4):
            if a|b==3:v[index(a,b)]=KAPPA[a]*KAPPA[b]%8
    return v


def terminal(m_mod480):
    saved=json.loads((BASE/'WEIGHTED_BRANCH_MOD8_LIFT_RECEIPT.json').read_text())
    O,E=[series(num,saved['common_denominator_D_power5'],963)
         for num in saved['numerators_O_E_mod8']]
    # Every index here is positive, so take its representative in1..480.
    def rr(start,d):
        d=(d-1)%480+1
        return rho(O if start%2 else E,d,start//2)
    e,o=eo_residues(15)
    table=[]
    for a in range(15):
        for b in range(15):
            total=0
            for ell in range(32):
                for u in range(32):
                    if ell|u != 31:continue
                    d=32*a+ell;f=32*b+u
                    j=(2*(m_mod480-1)-d-f)%15
                    for s in range(2):
                        for t in range(2):
                            cc=e[j] if s==t else o[j]
                            total+=cc*rr(1+s,m_mod480+d)*rr(2+t,m_mod480+f)
            table.append(total%8)
    return table


def run():
    # Exact entire state equality closes the orbit, rather than merely
    # spotting repetition in the scalar outputs.
    v=initial();states=[];seen={}
    while tuple(v) not in seen:
        seen[tuple(v)]=len(states)
        states.append(v)
        v=step(v)
        assert len(states)<2000
    pre=seen[tuple(v)];period=len(states)-pre
    terminals={str(p):terminal(p) for p in (32,128)}
    state_outputs=[{'step':i,'S1_h_phase1':sum(x*y for x,y in zip(w,terminals['32']))%8,
                    'S1_h_phase3':sum(x*y for x,y in zip(w,terminals['128']))%8}
                   for i,w in enumerate(states)]
    # Single independent contraction check. No complete new q is computed.
    B,C,w,t,L=inputs(128)
    direct=sum(a*b for a,b in zip(t,matvec(C,w)))%8
    transfer=sum(a*b for a,b in zip(states[0],terminals['128']))%8
    assert direct==transfer
    quartile_checks=0
    for h in (3,5):
        m=2**h
        for d in range(m):
            assert comb(m+d,m)%8==KAPPA[(4*d)//m]
            quartile_checks+=1
    out={'status':'AUTHOR exact 225-state first-contraction transfer',
         'dimension':225,'alphabet_pairs':[[0,1],[1,0],[1,1]],
         'top_quarter_weights':KAPPA,'initial_vector':states[0],
         'terminal_tables_m_mod480':terminals,
         'entire_state_orbit_preperiod':pre,'entire_state_orbit_period':period,
         'entire_orbit_vectors':states,
         'scalar_outputs':state_outputs,
         'independent_single_contraction_check_h7':direct,
         'bounded_binomial_weight_checks':quartile_checks,
         'longer_contractions_S2_S3_not_settled':True,
         'full_q2_n_plus2_not_proved':True}
    (BASE/'WEIGHTED_ENDPOINT_FIRST_TRANSFER_RECEIPT.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ('dimension','entire_state_orbit_preperiod',
                   'entire_state_orbit_period','independent_single_contraction_check_h7')},indent=2))
    print(json.dumps(state_outputs,indent=2))


if __name__=='__main__':run()
