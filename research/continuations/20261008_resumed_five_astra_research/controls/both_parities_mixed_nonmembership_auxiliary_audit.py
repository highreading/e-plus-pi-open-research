"""ONE bounded auxiliary audit: direct integer sums versus F4 series and ranks.

d=272 is NOT an original research index. No terminal border, original-sized
matrix, external input, network access or credential access is used.
"""
from pathlib import Path
import hashlib
import json
import math

HERE=Path(__file__).resolve().parent
D,L,RHO=272,128,16
WIDTH=2*L
ETA=(1,0,0,1,1,1)
assert D==2*L+RHO and D%3==2 and D%32==16

def direct_row(e,j):
    ts=[t for t in range(e+1) if math.comb(e,t)%2]
    return [sum(math.comb(r+j+t,r)*ETA[(r+j+t)%6] for t in ts)%2
            for r in range(WIDTH)]

def wp(n):
    return (1,2,3)[n%3]

def mul(a,b):
    out=0
    while b:
        if b&1: out^=a
        b>>=1
        a<<=1
        if a&4: a^=7
    return out

def trace(a):
    t=a^mul(a,a)
    assert t in (0,1)
    return t

def closed_first_row(p):
    numerator=p-1 if p%2 else p+1
    denominator=p if p%2 else p+2
    phase=2*p if p%2 else 2*p+1
    out=[]
    for r in range(WIDTH):
        value=0
        for t in range(min(numerator,r)+1):
            # Lucas parity, separate from the exact-comb direct array.
            if t&~numerator: continue
            j=r-t
            if j&(denominator-1): continue
            value^=wp(phase+2*t+j)
        out.append(trace(value))
    return out

def bits(row):
    return sum(x<<r for r,x in enumerate(row))

def rank(rows):
    pivots={}
    for value in rows:
        while value:
            pivot=value.bit_length()-1
            if pivot in pivots: value^=pivots[pivot]
            else:
                pivots[pivot]=value
                break
    return len(pivots)

top=[bits(direct_row(D,j)) for j in range(L-RHO+1)]
records=[]
coefficient_comparisons=0
for p in range(RHO+1,L-RHO+1):
    direct=direct_row(p,0)
    assert direct==closed_first_row(p), ('kernel',p)
    coefficient_comparisons+=WIDTH
    s=bits(direct)
    rp=top[:p-1] if p%2 else top[:p-2]+[top[p-2]^top[p-1]]
    rq=top[:p-1]+[top[p-1]^top[p]] if p%2 else top[:p]
    v=top[p-1]^top[p] if p%2 else top[p-1]
    observed=(rank(rp),rank(rq),rank(rq+[s]),rank(rp+[v^s]))
    assert observed==(p-1,p,p+1,p), ('rank',p,observed)
    assert rank(rq+rp)==p
    records.append({'p':p,'parity':'odd' if p%2 else 'even',
                    'rank_R_p':p-1,'rank_R_p_plus_1':p,
                    'rank_with_S_p':p+1,'rank_tied_stack':p})

receipt={
    'state':'PASS','auxiliary_d':D,'dyadic_L':L,'rho':RHO,
    'original_research_index':False,'return_columns':WIDTH,
    'p_range':[RHO+1,L-RHO],'parameter_cases':len(records),
    'independent_kernel_coefficient_comparisons':coefficient_comparisons,
    'kernel_paths':['Exact integer binomial sums and eta period',
                    'Independent F4 rational-series formula with Lucas parity'],
    'source_rank_path':'Exact integer source sum, finite binary row elimination',
    'records':records,
    'scope':'Auxiliary both-parity kernel and finite row nonmembership/tied-stack audit only; not a proof of original-index continuation, complete relative Cauchy--Binet units, terminal borders, gcd or e+pi.',
    'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'proof_note_sha256':hashlib.sha256((HERE/'COORDINATOR_EVEN_AND_TIED_FIRST_MIXED_TRANSITION_EXTENSION.md').read_bytes()).hexdigest()
}
target=HERE/'BOTH_PARITIES_MIXED_NONMEMBERSHIP_AUXILIARY_RECEIPT.json'
assert not target.exists(), 'Do not rerun a closed auxiliary check.'
target.write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({k:v for k,v in receipt.items() if k!='records'}))
