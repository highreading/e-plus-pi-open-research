"""Parent-authored bounded actual-source calculation; no remote code execution.

Central force identities are candidate input mathematics from A5turn4.
Their modular algorithm is independently compared with literal coefficients
at auxiliary small parameters, then evaluated at original u=0.
"""
from pathlib import Path
from fractions import Fraction
from math import comb, factorial
import hashlib, json, time

ROOT = Path(__file__).resolve().parent

def valuation2(a):
    return (a & -a).bit_length()-1 if a else None

def unit_fraction_mod(value, precision):
    assert value.denominator % 2
    modulus = 1 << precision
    return value.numerator * pow(value.denominator, -1, modulus) % modulus

def seeds(h, precision):
    modulus = 1 << precision
    aa = bb = 0
    receipts = []
    for j in range(min(h, 2*precision-1)+1):
        denominator = factorial(2*j)
        denominator_v = 2*j-j.bit_count()
        odd_denominator = denominator >> denominator_v
        division = denominator_v-j
        assert division >= 0
        pre_modulus = 1 << (precision+division)
        fall = 1
        fall_v = 0
        for k in range(j):
            factor = h-k
            fall = fall * (factor % pre_modulus) % pre_modulus
            fall_v += valuation2(factor)
        numerator = fall*fall % pre_modulus
        assert numerator % (1 << division) == 0
        tj = (numerator >> division) * pow(odd_denominator, -1, modulus) % modulus
        exact_v = 2*fall_v-division
        assert exact_v >= j-j.bit_count() >= j//2
        aa = (aa+tj) % modulus
        if j < h:
            bb = (bb+(h-j)*tj*pow(2*j+1, -1, modulus)) % modulus
        receipts.append({'j':j,'removed_power':division,
                         'numerator_valuation':2*fall_v,
                         'term_valuation':exact_v,
                         'predivision_bits':precision+division,
                         'residue':tj})
    return aa, bb, receipts

def force_head(h, precision, stop):
    n = 2*h
    aa, bb, seed_receipts = seeds(h, precision)
    vals = [aa, (n+1)*(aa+bb) % (1 << precision)]
    precisions = [precision, precision]
    divisions = []
    for i in range(stop-1):
        paid_bits = min(precisions[max(0, i-1):i+2])
        modulus = 1 << paid_bits
        numerator = ((4*n+4*i+6)*vals[i+1]
                     -(3*i+n+2)*(n+i+1)*vals[i])
        if i:
            numerator += i*(n+i)*(n+i+1)*vals[i-1]
        numerator %= modulus
        assert numerator % 2 == 0
        vals.append(numerator//2)
        precisions.append(paid_bits-1)
        divisions.append({'i':i,'predivision_bits':paid_bits,
                          'paid_power':1,'numerator_is_even':True})
    return vals[:stop+1], precisions[:stop+1], seed_receipts, divisions

def auxiliary_check(h):
    precision, stop = 24, 12
    vals, bits, _, _ = force_head(h, precision, stop)
    polynomial = [1]
    for _ in range(2*h):
        output = [0]*(len(polynomial)+2)
        for k, value in enumerate(polynomial):
            output[k] += value
            output[k+1] += 2*value
            output[k+2] += 2*value
        polynomial = output
    r = (1 << h)*comb(2*h, h)
    checks = []
    for i in range(stop+1):
        coefficient = sum(comb(i,k)*polynomial[2*h-k]
                          for k in range(min(i,2*h)+1))
        literal = Fraction(factorial(2*h+i)*coefficient,
                           factorial(2*h)*r)
        expected = unit_fraction_mod(literal, bits[i])
        checks.append(vals[i] == expected)
    assert all(checks)
    return {'h':h,'literal_coefficient_checks':len(checks),'all_passed':True,
            'scope':'Auxiliary algorithm check, not an original-family theorem.'}

def main():
    started = time.monotonic()
    auxiliary = [auxiliary_check(h) for h in (1,2,5,17)]
    u, L, I, precision = 0, 8, 62, 70
    b = 9**(18+32*u)
    h = 2001*b
    n = 2*h
    assert h % 32 == 1
    vals, bits, terms, divisions = force_head(h, precision, I)
    assert min(bits) >= L
    residues = [v % (1 << L) for v in vals]
    assert residues[0] % 8 == 2 and residues[1] % 8 == 1
    assert residues[2] % 8 == 3 and residues[3] % 4 == 1
    assert all(v%2 == int(i in (1,2,3)) for i,v in enumerate(residues))
    N = n+2
    v_weights = [(b-j).bit_count()+(N-b+j).bit_count()-N.bit_count()
                 for j in (4,3)]
    out = {'personally_authored':True,'network_and_credentials_denied':True,
           'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'auxiliary_algorithm_checks':auxiliary,
           'original_index':{'u':u,'b':b,'n':n,'h':h},
           'L':L,'I':I,'seed_precision_bits':precision,
           'seed_terms':terms,'recurrence_divisions':divisions,
           'force_head_mod256':residues,'remaining_bits_by_coordinate':bits,
           'Kummer_weight_valuations_b_minus4_b_minus3':v_weights,
           'proved_candidate_content_upper_bound':min(v_weights)-1,
           'all_passed':True,'elapsed_seconds':round(time.monotonic()-started,4),
           'scope':'Finite ORIGINAL u=0 force coefficients and content upper bound only. '
                   'No actual inverse content value, infinite subsequence, primitive '
                   'relative contraction or denominator/error conclusion is inferred.'}
    (ROOT/'binary_actual_force_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'all_passed':True,'original_u':u,'seed_terms':len(terms),
                      'force_residues':residues,'content_upper_bound':min(v_weights)-1,
                      'seconds':out['elapsed_seconds']}),flush=True)

if __name__ == '__main__':
    main()
