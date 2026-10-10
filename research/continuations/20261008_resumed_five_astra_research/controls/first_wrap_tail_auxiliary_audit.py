"""ONE new bounded first-wrap diagnostic, beyond the CLOSED q<=L receipt.

Coordinator authored. No network, credentials, external code or original
indices. Old lower-window profiles are not rerun or imported. The only rank
targets are q=129..134 on all272 columns, with both parity cases fixed before
execution. New columns and new rows are checked by independent exact paths.
"""
from pathlib import Path
import hashlib, json, math

HERE=Path(__file__).resolve().parent
TARGET=HERE/'FIRST_WRAP_TAIL_AUXILIARY_RECEIPT.json'
assert not TARGET.exists(), 'A closed diagnostic must not be rerun.'
D,L,RHO=272,128,16
PS=(67,68)
QS=tuple(range(129,135))
ETA=(1,0,0,1,1,1)
assert D==2*L+RHO and D%3==2

def om(n):return (1,2,3)[n%3]
def trace(x):return x>>1
def direct(e,z):
    ts=[t for t in range(e+1) if math.comb(e,t)&1]
    return [sum(math.comb(r+z+t,r)*ETA[(r+z+t)%6] for t in ts)&1
            for r in range(D)]

def rational(p,z):
    v=z//2
    if p&1:
        numerator=p-1
        denominator=p+2*v+(3 if z&1 else 0)
        phase=2*p+2*v
    else:
        numerator=p+(0 if z&1 else 1)
        denominator=p+2*v+2
        phase=2*p+2*v+(0 if z&1 else 1)
    ts=[t for t in range(numerator+1) if not(t&~numerator)]
    raw=[]
    for r in range(D):
        x=0
        for t in ts:
            if t>r:break
            j=r-t
            if not(j&(denominator-1)):x^=om(phase+2*t+j)
        raw.append(x)
    if p&1 and z&1:
        raw=[(raw[r-1] if r else 0)^(raw[r-2] if r>=2 else 0)
             for r in range(D)]
    return [trace(x) for x in raw]

def bits(row):return sum(x<<i for i,x in enumerate(row))
def rank(rows,width):
    mask=(1<<width)-1
    basis={}
    for row in rows:
        row &= mask
        while row:
            i=row.bit_length()-1
            if i in basis:row^=basis[i]
            else:
                basis[i]=row
                break
    return len(basis)

def bitpoly_product(a,b):
    value=0
    while b:
        low=b&-b
        value^=a<<(low.bit_length()-1)
        b^=low
    return value

# Exact binary convolution C_d=(1+Y+Y^2)^d moduloY^d.
conv=1
for bit in range(D.bit_length()):
    if D>>bit&1:
        power=1<<bit
        conv^=(conv<<power)^(conv<<(2*power))
conv &= (1<<D)-1

def reduced_mixed(p,z):
    v=z//2
    if p&1:
        bp=RHO+p-1
        ap=p+2*v+(3 if z&1 else 0)-RHO
        phase=2*p+2*v
    else:
        bp=RHO+p+(0 if z&1 else 1)
        ap=p+2*v+2-RHO
        phase=2*p+2*v+(0 if z&1 else 1)
    assert ap>0
    ts=[t for t in range(bp+1) if not(t&~bp)]
    raw=[]
    for r in range(D):
        x=0
        for t in ts:
            if t>r:break
            j=r-t
            if not(j&(ap-1)):x^=om(phase+2*t+j)
        raw.append(x)
    if p&1 and z&1:
        raw=[(raw[r-1] if r else 0)^(raw[r-2] if r>=2 else 0)
             for r in range(D)]
    return bits([trace(x) for x in raw])

top=[bits(direct(D,j)) for j in range(max(PS)+1)]
records=[]
new_coeffs=0
wrap_tail_coeffs=0
for p in PS:
    assert p>=RHO+1 and p+RHO<=L
    rp=top[:p-1] if p&1 else top[:p-2]+[top[p-2]^top[p-1]]
    extra=top[p-1]^top[p] if p&1 else top[p-1]
    rq=rp+[extra]
    values=[]
    for z in range(max(QS)-p):
        row=direct(p,z)
        other=rational(p,z)
        # The CLOSED first256 coefficients are reused for old rows.
        first_new=0 if z>=L-p else 2*L
        assert row[first_new:]==other[first_new:],('new_kernel_tail',p,z)
        new_coeffs+=D-first_new
        value=bits(row)
        values.append(value)
        reduced=reduced_mixed(p,z)
        expected=(reduced^(reduced<<(2*L)))&((1<<D)-1)
        actual=bitpoly_product(conv,value)&((1<<D)-1)
        # These16 previously unchecked original tail columns detect g.
        assert actual>>(2*L)==expected>>(2*L),('common_wrap_tail',p,z)
        wrap_tail_coeffs+=RHO
    for q in QS:
        h=q-p
        # Pay the precise expanded degree cut; no terminal assertion.
        poles=[p+2*(z//2)+(3 if p&1 and z&1 else
                0 if p&1 else 2)-RHO for z in range(h)]
        m=max([p]+poles)
        assert m+RHO==max(p+RHO,q+(q&1))<=D//2
        v=values[:h]
        strict=rp+v
        tied=rp+[v[-1]^extra]+[v[j]^v[j+1] for j in range(h-1)]
        strong=rank(rq+v,D)
        rstrict=rank(strict,D)
        rtied=rank(tied,D)
        records.append({'p':p,'q':q,'h':h,'M':m,
                        'strong_rank_all272':strong,'strong_expected':q,
                        'strict_rank_all272':rstrict,'tied_rank_all272':rtied,
                        'strict_tied_expected':q-1,
                        'strong_rank_first256':rank(rq+v,2*L),
                        'strong_full':strong==q,
                        'strict_tied_full':rstrict==q-1 and rtied==q-1})

receipt={'state':'EXACT_DIAGNOSTIC_COMPLETE','auxiliary_d':D,'dyadic_L':L,
         'rho':RHO,'original_research_index':False,'p_parameters':PS,
         'q_parameters':QS,'new_kernel_coefficient_comparisons':new_coeffs,
         'new_common_wrap_tail_comparisons':wrap_tail_coeffs,
         'profiles':records,
         'all_new_strong_profiles_full':all(x['strong_full'] for x in records),
         'all_new_strict_tied_profiles_full':all(x['strict_tied_full'] for x in records),
         'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'interface_sha256':hashlib.sha256((HERE/'COORDINATOR_FIRST_DYADIC_WRAP_MIXED_INTERFACE.md').read_bytes()).hexdigest(),
         'scope':'Only fixed auxiliary NEW beyond-L ranks and previously unchecked tail/kernel identities. This does not prove a universal or original-index rank, complete cofactor prefactor, terminal joint valuation, all-prime saving or any e+pi theorem.'}
TARGET.write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt))
