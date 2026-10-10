"""ONE NEW fixed auxiliary audit of higher rows, critical poles and larger ranks.

Coordinator-authored; no third-party code/input, network or credential access.
Auxiliary d272 is not an original research index. Previous closed first-row
receipt is not executed/imported/replaced. This checks a genuinely larger
higher-row range and coupled stack; no terminal coefficient is evaluated.
"""
from pathlib import Path
import math,hashlib,json

HERE=Path(__file__).resolve().parent
TARGET=HERE/'HIGHER_MIXED_POLE_WINDOW_AUXILIARY_RECEIPT.json'
assert not TARGET.exists(), 'Do not rerun a closed higher-row audit.'
D,L,RHO,WIDTH=272,128,16,256
PARAMETERS=(17,18,67,68,111,112)
ETA=(1,0,0,1,1,1)
assert D==2*L+RHO and D%3==2 and WIDTH==2*L

def direct(e,z):
    ts=[t for t in range(e+1) if math.comb(e,t)%2]
    return [sum(math.comb(r+z+t,r)*ETA[(r+z+t)%6] for t in ts)%2
            for r in range(WIDTH)]

def omega(n):
    return (1,2,3)[n%3]

def trace(x):
    # F4 trace: 0->0,1->0,omega->1,omega^2->1.
    assert 0<=x<=3
    return x>>1

def rational_row(p,z):
    v=z//2
    if p%2:
        numerator=p-1
        denominator=p+2*v+(3 if z%2 else 0)
        phase=2*p+2*v
    else:
        numerator=p+(0 if z%2 else 1)
        denominator=p+2*v+2
        phase=2*p+2*v+(0 if z%2 else 1)
    # Independent rational-series coefficient path uses Lucas bits, not comb.
    terms=[t for t in range(numerator+1) if not(t&~numerator)]
    raw=[]
    for r in range(WIDTH):
        value=0
        for t in terms:
            if t>r: break
            j=r-t
            if not(j&(denominator-1)):
                value^=omega(phase+2*t+j)
        raw.append(value)
    if p%2 and z%2:
        raw=[(raw[r-1] if r>=1 else 0)^(raw[r-2] if r>=2 else 0)
             for r in range(WIDTH)]
    return [trace(x) for x in raw]

def bits(row):
    return sum(x<<i for i,x in enumerate(row))

def extend(basis,value):
    while value:
        i=value.bit_length()-1
        if i in basis: value^=basis[i]
        else:
            basis[i]=value
            return True
    return False

def rank(rows):
    basis={}
    for row in rows: extend(basis,row)
    return len(basis)

top=[bits(direct(D,j)) for j in range(max(PARAMETERS)+1)]
comparisons=0
records=[]
for p in PARAMETERS:
    assert p>=RHO+1 and p+RHO<=L
    rp=top[:p-1] if p%2 else top[:p-2]+[top[p-2]^top[p-1]]
    extra=top[p-1]^top[p] if p%2 else top[p-1]
    rq=rp+[extra]
    assert rank(rp)==p-1 and rank(rq)==p
    basis={}
    for row in rq: assert extend(basis,row)
    mixed=[]
    profile=[]
    for z in range(L-p):
        row=direct(p,z)
        if z>=1:
            assert row==rational_row(p,z), ('higher_kernel',p,z)
            comparisons+=WIDTH
        value=bits(row)
        mixed.append(value)
        assert extend(basis,value), ('coupled_independence',p,z)
        h=z+1
        assert len(basis)==p+h
        strict_rank=rank(rp+mixed)
        tied_rows=rp+[mixed[-1]^extra]+[mixed[j]^mixed[j+1] for j in range(h-1)]
        tied_rank=rank(tied_rows)
        assert strict_rank==p+h-1 and tied_rank==p+h-1, ('full_stack',p,h)
        profile.append({'h':h,'q':p+h,'rank_source_plus_mixed':len(basis),
                        'rank_strict_stack':strict_rank,'rank_tied_stack':tied_rank})
    records.append({'p':p,'parity':'odd' if p%2 else 'even','new_higher_rows':L-p-1,
                    'q_endpoint':L,'profile':profile})

assert comparisons==94464
receipt={'state':'PASS','auxiliary_d':D,'dyadic_L':L,'rho':RHO,
         'return_columns':WIDTH,'original_research_index':False,
         'parameters':PARAMETERS,'new_higher_row_coefficient_comparisons':comparisons,
         'new_higher_rows':369,'all_q_to_L_rank_profiles':375,
         'kernel_paths':['Exact integer binomial sums with eta period',
                         'Independent full both-parity F4 rational-series Lucas path'],
         'rank_path':'Exact-binomial source and mixed rows; incremental binary elimination; full strict/tied stacks',
         'critical_scope':'Includes odd z=rho-1/rho and all higher distinct poles, even higher pole pairs, and every q<=L for the fixed six cases.',
         'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'proof_note_sha256':hashlib.sha256((HERE/'COORDINATOR_MIXED_WINDOW_TO_DYADIC_L.md').read_bytes()).hexdigest(),
         'scope':'Auxiliary higher-row/rank audit only. No complete Cauchy-Binet relative unit, original continuation, terminal border, gcd or e+pi theorem is proved by this receipt.',
         'records':records}
TARGET.write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({k:v for k,v in receipt.items() if k!='records'}))
