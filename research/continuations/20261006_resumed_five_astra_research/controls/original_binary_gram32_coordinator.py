#!/usr/bin/env python3
"""New complete physical32-bit columns and maximal certified Gram dividend.

Uses newly checked short orders63/62, universal fixed divisors, and inspected
factorial transport. No old producer or Gram target is regenerated.
"""
from pathlib import Path
from math import comb
import hashlib
import importlib.util
import json
import time

ROOT = Path(__file__).resolve().parent

def multiply(a,b,modulus):
    result = [0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            result[i+j] = (result[i+j]+x*y) % modulus
    return result

def numerator_polynomial(A,a,b,R,bits):
    modulus = 1 << bits
    falling, rising = [[1]], [[1]]
    for r in range(1,R+1):
        falling.append(multiply(falling[-1],[b-r+1,-1],modulus))
        rising.append(multiply(rising[-1],[a+b+r-1,-1],modulus))
    result = [0]*(R+1)
    for r,c in enumerate(A):
        if c:
            term = multiply(falling[r],rising[R-r],modulus)
            for j,x in enumerate(term):
                result[j] = (result[j]+c*x) % modulus
    return result

def fixed_divisor(R):
    factorial_val = R-R.bit_count()
    maximum = max((comb(R,r) & -comb(R,r)).bit_length()-1 for r in range(R+1))
    t = factorial_val-maximum
    assert t == min((r-r.bit_count())+(R-r-(R-r).bit_count()) for r in range(R+1))
    return t

def normalized_newton(U,t,R,bits,tr):
    modulus = 1 << bits
    large = 1 << (bits+t)
    values = []
    for j in range(R+1):
        value = 0
        for c in reversed(U):
            value = (value*j+c) % large
        assert value % (1 << t) == 0
        values.append(value >> t)
    return tr.differences(values,modulus)

def main():
    started = time.monotonic()
    transport = ROOT/'original_binary_gram_transport_coordinator.py'
    spec = importlib.util.spec_from_file_location('accepted_transport',transport)
    tr = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(tr)
    source = ROOT/'original_binary_numerators32_certificate.json'
    data = json.loads(source.read_text())
    assert data['status'] == 'PASS' and data['precision_bits'] == 32
    assert data['full_principal_parts_verified'] and data['exterior_plus_one_verified']
    records = data['new_branch_and_factor_tests']
    assert all(z['n_branch_zero'] and z['contact_z_factor_verified'] for z in records)
    Rf,Re = [z['short_denominator_order'] for z in records]
    assert (Rf,Re) == (63,62)
    af,ae = [z['short_numerator'] for z in records]
    assert all(len(A) <= R+1 for A,R in zip((af,ae),(Rf,Re)))
    n,b = int(data['n']),int(data['b'])
    a = 2*n
    tf,te = fixed_divisor(Rf),fixed_divisor(Re)
    assert (tf,te) == (57,52)
    df,vf = tr.odd_product(a,Rf,42)
    de,ve = tr.odd_product(a,Re,42)
    assert (vf,ve) == (63,62)
    norm_loss,mixed_loss = 2*(vf-tf),vf+ve-tf-te
    assert (norm_loss,mixed_loss) == (12,16)
    norm_bits,mixed_bits = min(32+9+1,64),min(32+9,64)
    kernel_bits = max(norm_bits+norm_loss,mixed_bits+mixed_loss)
    assert (norm_bits,mixed_bits,kernel_bits) == (42,41,57)
    Uf = numerator_polynomial(af,a,b,Rf,400)
    Ue = numerator_polynomial(ae,a,b,Re,400)
    Pf = normalized_newton(Uf,tf,Rf,kernel_bits,tr)
    Pe = normalized_newton(Ue,te,Re,kernel_bits,tr)
    modulus = 1 << kernel_bits
    fv = tr.consecutive_values(Pf,2*Rf+1,modulus)
    ev = tr.consecutive_values(Pe,2*Rf+1,modulus)
    ff = tr.differences([x*x % modulus for x in fv],modulus)
    fe = tr.differences([x*y % modulus for x,y in zip(fv,ev)][:Rf+Re+1],modulus)
    assert len(ff) <= 2*Rf+1 and len(fe) <= Rf+Re+1
    results,trace = tr.contraction(n+2,b,2*n-1,[ff,fe],[2*Rf,Rf+Re],kernel_bits,True)
    sf = results[0] % (1 << (norm_bits+norm_loss))
    sm = results[1] % (1 << (mixed_bits+mixed_loss))
    assert sf % (1 << norm_loss) == 0 and sm % (1 << mixed_loss) == 0
    norm = (sf >> norm_loss)*pow(df*df % (1 << norm_bits),-1,1 << norm_bits) % (1 << norm_bits)
    mixed = (sm >> mixed_loss)*pow(df*de % (1 << mixed_bits),-1,1 << mixed_bits) % (1 << mixed_bits)
    previous_path = ROOT/'binary_quadratic_precision45_certificate.json'
    previous = json.loads(previous_path.read_text())
    assert norm % (1 << 30) == previous['D_raw_mod2_30']
    assert mixed % (1 << 29) == previous['E_raw_mod2_29']
    d,e = tr.val2(norm,norm_bits),tr.val2(mixed,mixed_bits)
    ratio = {'available':False,'reason':'No upper norm depth without a nonzero norm residue'}
    if norm:
        s = min(mixed_bits-d-1,norm_bits-2*d-1+e)
        if s > 0:
            ratio = {'available':True,'absolute_precision_bits':s,'norm_depth':d,'mixed_depth_value_or_lower_bound':e}
            if mixed:
                order = e-d-1
                unit_bits = s-order
                assert unit_bits > 0 and unit_bits <= norm_bits-d and unit_bits <= mixed_bits-e
                unit = (mixed >> e)*pow(norm >> d,-1,1 << unit_bits) % (1 << unit_bits)
                ratio.update({'valuation':order,'unit_residue':unit,'unit_precision_bits':unit_bits})
            else:
                ratio.update({'zero_mod2_s':True,'valuation_lower_bound':mixed_bits-d-1})
            ratio['logarithmic_guard_lower_bound'] = str(2000*b-138+9-d-1)
            assert int(ratio['logarithmic_guard_lower_bound']) >= s
        else:
            ratio = {'available':False,'reason':'Current absolute Gram precision does not give a positive ratio guard','maximum_guard_bits':s}
    artifact = {
        'status':'PASS','scope':'NEW complete original u0 physical32-bit columns with certified norm42/mixed41 comparison; all-prime arithmetic remains open',
        'n':str(n),'b':str(b),'physical_column_bits':32,'physical_content_lower_bounds':[9,9],
        'short_orders':[Rf,Re],'universal_fixed_divisors':[tf,te],'denominator_valuations':[vf,ve],
        'normalization_losses':[norm_loss,mixed_loss],'shared_kernel_bits':kernel_bits,
        'payload_degrees':[2*Rf,Rf+Re], 'Uf_mod400':list(map(str,Uf)), 'Ue_mod400':list(map(str,Ue)),
        'D_raw_mod2_42':norm,'E_raw_mod2_41':mixed,
        'valuation_D_raw':{'value_or_lower_bound':d,'exact':bool(norm)},
        'valuation_E_raw':{'value_or_lower_bound':e,'exact':bool(mixed)},
        'primitive_norm_loss_if_first_content9':{'value_or_lower_bound':d-18,'exact_if_content_verified':bool(norm)},
        'ratio_E_over_2D':ratio,'transport':trace,'old30_29_bit_reduction_passed':True,
        'complete_exterior_retained':True,'finite_range_inclusive':'0<=j<=b',
        'all_prime_gcd_evaluated':False,'irrationality_proved':False,
        'dependencies':[{'name':p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in (transport,source,previous_path,ROOT/'binary_kernel_content_certificate.json')]
    }
    target = ROOT/'original_binary_gram32_certificate.json'
    target.write_text(json.dumps(artifact,indent=2)+'\n')
    receipt = {k:v for k,v in artifact.items() if k not in ('Uf_mod400','Ue_mod400','transport')}
    receipt['transport'] = {k:v for k,v in trace.items() if k != 'trace'}
    receipt['source_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    receipt['artifact_sha256'] = hashlib.sha256(target.read_bytes()).hexdigest()
    receipt['elapsed_seconds'] = round(time.monotonic()-started,3)
    (ROOT/'original_binary_gram32_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt))

if __name__ == '__main__':
    main()
