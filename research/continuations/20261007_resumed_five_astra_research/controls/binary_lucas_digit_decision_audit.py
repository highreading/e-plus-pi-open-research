"""Parent-authored bounded automaton for the proposed complete Lucas mask.

Candidate formula is separately compared with the checked finite Schur
algorithm on supplied original rows. Decision on all mask rows remains
conditional on a symbolic formula audit. No infinite-index theorem inferred.
"""
from pathlib import Path
from math import comb
import hashlib,json,time
from binary_actual_contact_mod4_audit import choose4
ROOT=Path(__file__).resolve().parent

def decide(b):
    h=2001*b;H0=(h+1)//2;target=(b+3)//4
    assert b%64==17 and h%32==1
    length=max(h.bit_length(),target.bit_length())+2
    states={(0,False):(0,0)}
    receipt=[]
    for i in range(length):
        output={}
        for (carry,positive),(k,ell) in states.items():
            for kb in (0,1):
                if kb and not ((H0>>i)&1):continue
                if i==0 and not kb:continue
                for eb in (0,1):
                    if eb and ((h>>i)&1):continue
                    total=kb+eb+carry
                    if total%2!=((target>>i)&1):continue
                    key=(total//2,positive or bool(eb))
                    output.setdefault(key,(k+(kb<<i),ell+(eb<<i)))
        states=output
        assert len(states)<=4
        receipt.append({'bit':i,'reachable_states':[[c,int(p)] for c,p in states]})
    witness=states.get((0,True))
    if witness:
        k,ell=witness
        assert k+ell==target and k%2 and ell>0 and k<=(b-1)//4
        assert k&H0==k and not (ell&h)
        j=4*k
        assert choose4(4002*b+2,j)%2
        assert choose4(8004*b+b+3-j,b+3-j)%2
    return {'b':b,'bits':length,'reachable_state_receipt':receipt,
            'mask_accepts':bool(witness),
            'candidate_a_zero_witness':None if not witness else 4*witness[0],
            'scope':'Complete finite digit decision under the proposed inverse formula.'}

def main():
    started=time.monotonic();checks=0;failures=[]
    for name in ('binary_actual_contact_mod4_certificate.json',
                 'binary_actual_sparse_lucas_mask_certificate.json'):
        saved=json.loads((ROOT/name).read_text())
        for case in saved['cases']:
            u=case['original_u'];b=9**(18+32*u);n=4002*b;N=n+2
            residues=case.get('selected_contact_residues',case.get('contact_residues'))
            for row,value in residues.items():
                j=int(row)
                if not choose4(N,j)%2:continue
                assert j%64 in (0,4)
                expected=0 if j%64==0 else 2*choose4(2*n+b+3-j,b+3-j)%4
                checks+=1
                if value!=expected:failures.append({'u':u,'j':j,'got':value,'candidate':expected})
    # Independent literal enumeration checks only the elementary digit DP.
    # These auxiliary h are deliberately unrelated to the research family.
    dp_small=[]
    for b in (17,81,145,209):
        h=2001*b;H0=(h+1)//2;target=(b+3)//4
        literal=[4*k for k in range((b-1)//4+1)
                 if k%2 and (k&H0)==k and not ((target-k)&h)]
        dd=decide(b)
        assert dd['mask_accepts']==bool(literal)
        dp_small.append({'auxiliary_b':b,'literal_witness_count':len(literal),
                         'decision_matches':True})
    cases=[]
    for u in range(10):
        case=decide(9**(18+32*u));case['original_u']=u;cases.append(case)
    out={'personally_authored':True,'network_and_credentials_denied':True,
         'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'candidate_profile_comparisons':checks,'candidate_profile_failures':failures,
         'literal_digit_dp_checks':dp_small,'cases':cases,
         'elapsed_seconds':round(time.monotonic()-started,4),
         'scope':'Finite original u0..9 complete mask DECISIONS conditional on '
                 'the proposed inverse formula; comparisons validate only '
                 'saved rows. No infinite-family content theorem.'}
    (ROOT/'binary_lucas_digit_decision_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'profile_comparisons':checks,'formula_failures':failures,
          'decisions':[{'u':c['original_u'],'bits':c['bits'],'accepts':c['mask_accepts'],
                        'witness':c['candidate_a_zero_witness']} for c in cases],
          'seconds':out['elapsed_seconds']}),flush=True)

if __name__=='__main__':main()
