#!/usr/bin/env python3
"""New complete originalu0 force head and finite exterior loads at32bits.

Reuses accepted central formulas and archived operator coefficients. No matrix
or previous producer is regenerated and no original-length vector is formed.
"""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import hashlib
import json
import resource

resource.setrlimit(resource.RLIMIT_CPU,(120,120))
ROOT = Path(__file__).resolve().parent
OLD = ROOT.parents[1]/'astra_pro5_resume_20261005'/'controls'
PREC = 32
Q = 1<<PREC
b = 9**18
n = 4002*b
h = n//2

def depth(x):
    x %= Q
    return PREC if x==0 else (x&-x).bit_length()-1

def residue(x):
    assert x.denominator%2
    return x.numerator*pow(x.denominator,-1,Q)%Q

def central(ell):
    j,odd = divmod(ell,2)
    pref = 1
    if odd:
        for t in range(j+1):
            pref *= 2*h+2*t+1
    else:
        for t in range(1,j+1):
            pref *= 2*h+2*t-1
    for t in range(j+odd):
        pref *= h-t
    total = 0
    # L(36)=34; all s>=36 are killed modulo2^32 by the tail theorem.
    for s in range(36):
        frac = F((1<<s)*factorial(s)**2,factorial(2*s+odd))
        total += residue(frac)*comb(h-j-odd,s)*comb(h+j,s)
    return pref*total%Q

def main():
    operator = ROOT/'original_binary_operator_schur32_certificate.json'
    op = json.loads(operator.read_text())
    assert (int(op['b']),int(op['n']),op['precision_bits'])==(b,n,PREC)
    lam,cc = op['symbol_coefficients'],op['inverse_coefficients']
    m = op['operator_degree']
    B = [central(ell) for ell in range(96)]
    f = []
    for i in range(96):
        total = 0
        for ell in range(i+1):
            prod = 1
            for t in range(ell+1,i+1):
                prod = prod*(n+t)%Q
            total += comb(i,ell)*prod*B[ell]
        f.append(total%Q)
    assert all(z==0 for z in f[72:])
    old = json.loads((ROOT/'original_binary_head20_certificate.json').read_text())
    assert [z % (1<<20) for z in f[:48]] == old['first_force_0_47']
    assert all(z % (1<<20) == 0 for z in f[48:])
    v = [1]
    for t in range(1,37):
        v.append(v[-1]*(b+t)%Q)
    assert v[36]==0 and factorial(36)%(1<<32)==0
    v = v[:36]
    uout = [sum(comb(n,t-r)*v[t] for t in range(r,36))%Q for r in range(36)]
    hout = [sum(lam[s]*comb(b+r,s)*uout[r-s]
                for s in range(m+1) if 0<=r-s<36)%Q for r in range(160)]
    assert [z % (1<<20) for z in hout[:100]] == old['complete_exterior_load_0_99']
    assert all(z % (1<<20) == 0 for z in hout[100:])
    log_bound = 1+(h-h.bit_count())-((2*n+b-1).bit_length()-1)-(b-b.bit_count())
    assert log_bound>=PREC
    cert = {'status':'PASS','scope':'NEW complete original u0 physical32-bit first force head and exponential exterior load under A5turn4 tail proof; no Gram or norm-relative omission',
            'u':0,'b':str(b),'n':str(n),'precision_bits':PREC,'operator_degree':m,
            'operator_artifact_sha256':hashlib.sha256(operator.read_bytes()).hexdigest(),
            'central_coefficients_0_95':B,'first_force_0_71':f[:72],
            'first_force_72_95_zero':True,'central_tail_s_ge36_depth_at_least34':True,
            'first_force_tail_i_ge72_proved_bound_at_least34':True,
            'factorial_tail_v_0_35':v,'upper_exterior_load_0_35':uout,
            'complete_exterior_load_0_159':hout,
            'symbol_coefficients':lam,'inverse_coefficients':cc,
            'absolute_logarithmic_omission_bound':str(log_bound),
            'relative_logarithmic_omission_proved':False,'original_Gram_pair_computed':False}
    target = ROOT/'original_binary_head32_certificate.json'
    target.write_text(json.dumps(cert,indent=2)+'\n')
    receipt = {'status':'PASS','scope':cert['scope'],
               'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               'artifact_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),
               'b':str(b),'n':str(n),'precision_bits':PREC,
               'first_force_head_length':72,'complete_exterior_load_length':160,
               'first_force_head_nonzero_count':sum(z!=0 for z in f[:72]),
               'first_force_initial_pair':f[:2],'archived20_bit_complete_head_reduction_passed':True,
               'first_force_head_minimum_depth':min(map(depth,f[:72])),
               'tail_proof_report_sha256':hashlib.sha256((ROOT.parent/'responses/A5_turn4.md').read_bytes()).hexdigest(),
               'relative_logarithmic_omission_proved':False,'original_Gram_pair_computed':False}
    (ROOT/'original_binary_head32_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))

if __name__=='__main__':
    main()
