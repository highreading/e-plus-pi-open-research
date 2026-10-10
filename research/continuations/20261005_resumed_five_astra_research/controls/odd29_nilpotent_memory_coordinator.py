"""Exhaustive fixed-field identity proving uniform original recurrence memory.

No original index is enumerated: polynomial coefficient reduction is identical
for every n divisible by29. All29 starting phases are checked exactly.
"""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parent
p=29
def mm(A,B,q):return [[sum(x*y for x,y in zip(row,col))%q for col in zip(*B)] for row in A]
def eye():return [[int(i==j) for j in range(3)] for i in range(3)]
def T(n,i,q):
    return [[(2*n+2*i+1)%q,(-(n+i)*(n+3*i-1)//2)%q,
             (-(n+i)*(n+i-1)*(1-i)//2)%q],[1,0,0],[0,1,0]]
def product(n,a,length,q):
    out=eye()
    for i in range(a,a+length):out=mm(T(n,i,q),out,q)
    return out
def one(a):
    B=product(0,a,p,p)
    rank_one=all((B[i][j]*B[k][l]-B[i][l]*B[k][j])%p==0
                for i in range(3) for k in range(i+1,3) for j in range(3) for l in range(j+1,3))
    power=eye();index=None
    for i in range(1,4):
        power=mm(B,power,p)
        if power==[[0]*3 for _ in range(3)]:index=i;break
    assert index is not None
    short=eye();length=None
    for i in range(3*p):
        short=mm(T(0,a+i,p),short,p)
        if short==[[0]*3 for _ in range(3)]:length=i+1;break
    assert length is not None
    return {'phase':a,'block_matrix_mod29':B,'rank_at_most_one':rank_one,'nilpotent_index':index,'first_zero_word_length':length}
if __name__=='__main__':
    phases=[one(a) for a in range(p)]
    memory=max(row['first_zero_word_length'] for row in phases)
    # Higher-precision finite corroboration of the all-index grouping proof.
    high=[]
    for n in (29,203,191110):
        for k in (1,2,3,4):
            for a in (2,28,29,30,57):
                assert product(n,a,memory*k,p**k)==[[0]*3 for _ in range(3)]
                high.append({'n_prefix':n,'precision':k,'phase':a,'length':memory*k,'zero':True})
    out={'status':'PASS','scope':'Uniform fixed-prime recurrence propagation identity for every integer n divisible by29; not a Gram-alignment theorem',
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'exhaustive_phases':phases,'higher_precision_corrob_checks':len(high),'higher_precision_cases':high,
         'memory_step_constant':memory,
         'uniform_consequence':f'Every actual homogeneous propagator over at least{memory}K consecutive steps is zero modulo29^K. Proof: coefficient reduction is29-periodic independent of n when29|n; each{memory}-step segment is zero modulo29 by the exhaustive phase identities; grouping K such integral segments supplies29^K.',
         'forced_consequence':f'A particular recurrence value modulo29^K depends only on its last{memory}K source terms (or all sources if the original interval is shorter). The initial step and original source/endpoint bounds must be retained.'}
    dest=ROOT/'odd29_nilpotent_memory_certificate.json';dest.write_text(json.dumps(out,indent=2)+'\n')
    receipt={k:v for k,v in out.items() if k not in ('exhaustive_phases','higher_precision_cases')}
    receipt['exhaustive_phase_count']=len(phases)
    receipt['artifact_sha256']=hashlib.sha256(dest.read_bytes()).hexdigest()
    (ROOT/'odd29_nilpotent_memory_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt),flush=True)
