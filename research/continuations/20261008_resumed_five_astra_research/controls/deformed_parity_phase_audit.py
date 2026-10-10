"""Parent-authored NEW bounded cross-check after an unsent phase defect.

No keys, network, original-length arrays, previous scans or code supplied
by an external model. Integers/field operations only; writes controls.
"""
from pathlib import Path
import hashlib, json, math

C=Path(__file__).resolve().parent
d=464
q=128

def fm(a,b):
    v=0
    for i in range(2):
        for j in range(2):
            if (a>>i)&1 and (b>>j)&1:
                v^=1<<(i+j)
    if v&4:
        v^=7
    return v

def wp(k):
    return (1,2,3)[k%3]

def tr(a):
    b=a^fm(a,a)
    assert b in (0,1)
    return b

def field_det(rows):
    a=[list(r) for r in rows]
    n=len(a)
    det=1
    for j in range(n):
        p=next((i for i in range(j,n) if a[i][j]),None)
        if p is None:
            return 0
        a[j],a[p]=a[p],a[j]
        v=a[j][j]
        det=fm(det,v)
        iv=fm(v,v)
        a[j]=[fm(iv,x) for x in a[j]]
        for i in range(j+1,n):
            v=a[i][j]
            if v:
                a[i]=[x^fm(v,y) for x,y in zip(a[i],a[j])]
    return det

def binary_rank(rows,width):
    piv={}
    for row in rows:
        v=sum(x<<j for j,x in enumerate(row))
        while v:
            j=v.bit_length()-1
            if j not in piv:
                piv[j]=v
                break
            v^=piv[j]
    return len(piv)

# The direct side uses exact INTEGER binomials in the new rising
# source sum. This does not call the previous J digit-filter code.
theta=[1,0]
for i in range(d+2*q+2):
    theta.append((theta[-1]+theta[-2])%2)
eta=[(theta[i]+((i+1)%2)*theta[i+1])%2
     for i in range(d+2*q)]
support=[t for t in range(d+1) if math.comb(d,t)%2]
bc=[[math.comb(n,r)%2 if r<=n else 0 for r in range(q)]
    for n in range(d+2*q)]
u=[]
for j in range(q):
    row=[]
    for r in range(q):
        v=0
        for t in support:
            v^=bc[t+j+r][r]&eta[t+j+r]
        row.append(v)
    u.append(row)

# Independently construct the finite binary COLUMN convolution.
c=[1]+[0]*(q-1)
for b in range(d.bit_length()):
    if not (d>>b)&1:
        continue
    shift=1<<b
    nxt=c[:]
    for t in (shift,2*shift):
        for j in range(t,q):
            nxt[j]^=c[j-t]
    c=nxt
upr=[[sum(c[r-s]*u[j][s] for s in range(r+1))%2
      for r in range(q)] for j in range(q)]

matches=0
wrong_mismatches=0
for h in range(q//2):
    for l in range(q//2):
        right=0
        wrong=0
        for v in range(l+1):
            if math.comb(d,v)%2 and math.comb(h+l-v,l-v)%2:
                right^=wp(h+l+v+2)
                wrong^=wp(h+l-v+2)
        a=tr(right)
        bad=tr(wrong)
        for direct in (upr[2*h][2*l+1],upr[2*h+1][2*l]):
            assert direct==a
            matches+=1
            wrong_mismatches+=direct!=bad
        assert upr[2*h+1][2*l+1]==0

d2=[[0,1],[1,2]]
d4=[[2,2,0,0],[3,3,2,0],[3,1,2,2],[3,2,2,3]]
assert field_det(d2)==1
assert field_det(d4)==2
r64=binary_rank([row[:64] for row in u[:64]],64)
r128=binary_rank(u,128)
assert (r64,r128)==(64,128)
assert wrong_mismatches>0

receipt={
    'status':'PASS',
    'scope':'NEW auxiliary d464 contact parity and exact small field phase checks; not an original-index coefficient or gcd theorem.',
    'd':d,'largest_parity_block':q,'integer_binomial_upper_max':d+2*q-2,
    'direct_integer_source_sum_support_size':len(support),
    'cross_block_entry_comparisons':matches,
    'reversed_phase_discrepancies':wrong_mismatches,
    'direct_binary_ranks':{'64':r64,'128':r128},
    'reduced_field_determinants':{'2':1,'4':'omega'},
    'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'corrected_note_sha256':hashlib.sha256((C/'COORDINATOR_DEFORMED_PARITY_BLOCK_REDUCTION.md').read_bytes()).hexdigest(),
    'no_original_length_solve':True,'no_previous_scan_rerun':True,
    'different_full_proof_review':'pending',
}
(C/'DEFORMED_PARITY_PHASE_AUDIT_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt))
