"""NEW fourth digits of defined complete prefix constants; not a source jet."""
from pathlib import Path
from math import factorial, prod
from fractions import Fraction
from collections import Counter
import datetime
import hashlib
import json

HERE = Path(__file__).resolve().parent
R = HERE.parent
old_path = HERE/'prefix_mod27_constants_certificate.json'
old = json.loads(old_path.read_text())
assert old['status'] == 'PASS' and len(old['rows']) == 122
old_rows = {r['j']: r for r in old['rows']}


def remove_threes(n):
    assert n
    v = 0
    while n % 3 == 0:
        n //= 3
        v += 1
    return v, n


common = 81*2**270*factorial(270)
rows, failures = [], []
new_digit_profile, newly_nonzero = Counter(), []
for j in range(1,123):
    high = prod(243+2*j+2*a for a in range(271))
    low = prod(81+2*j+2*a for a in range(271))
    # Combine the two exact rational summands BEFORE any integrality claim.
    complete = Fraction(common, high)+Fraction(3*common, low)
    vn, un = remove_threes(complete.numerator)
    vd, ud = remove_threes(complete.denominator)
    v = vn-vd
    assert vd == 0 and v >= 0
    residue = complete.numerator % 81*pow(complete.denominator % 81,-1,81) % 81
    # Independent unreduced integer expression, with all cancellation paid.
    raw_numerator = common*(low+3*high)
    raw_denominator = high*low
    rn_v, rn_u = remove_threes(raw_numerator)
    rd_v, rd_u = remove_threes(raw_denominator)
    raw_v = rn_v-rd_v
    independently_reduced = (pow(3,raw_v,81)*(rn_u % 81)
                            *pow(rd_u % 81,-1,81)) % 81
    saved = old_rows[j]
    if (independently_reduced != residue or raw_v != v
            or residue % 27 != saved['D_j_mod27']
            or v != saved['v3_combined_constant']):
        failures.append({'j':j, 'issue':'new digit/reused receipt disagreement'})
    digit = (residue-saved['D_j_mod27'])//27
    assert 0 <= digit <= 2
    new_digit_profile[digit] += 1
    if saved['D_j_mod27'] == 0 and residue != 0:
        newly_nonzero.append(j)
    rows.append({'j':j,'D_j_mod81':residue,'fourth_ternary_digit':digit,
                 'reused_D_j_mod27':saved['D_j_mod27'],
                 'reused_exact_v3':v,'independent_unreduced_residue':independently_reduced,
                 'largest_odd_factor':243+2*j+540})

if len(newly_nonzero) != 82 or any(rows[j-1]['reused_exact_v3'] != 3 for j in newly_nonzero):
    failures.append({'issue':'expected82 old zeros acquire the fourth digit'})
sources = [old_path,R/'responses/A1_turn9.md',
           HERE/'PREFIX_MOD81_CONSTANTS_AND_CLASSICAL_SCALE_GATE.md',
           HERE/'COORDINATOR_CLASSICAL_270P_SCALE_REUSE.md']
out = {'status':'FAIL' if failures else 'PASS',
       'time':datetime.datetime.now().astimezone().isoformat(),
       'scope':'Only NEW modulo81 arithmetic of122 defined macro constants; complete source residual modulo81 is NOT established.',
       'source_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
       'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       'rows':rows,'fourth_digit_profile':dict(new_digit_profile),
       'newly_nonzero_constant_indices':newly_nonzero,
       'old_mod27_zero_count':82,'all122_agree_with_reused_mod27_receipt':not failures,
       'source_non_P_layers_revalidated':False,'actual_Delta_A_evaluated':False,
       'global_proof':False,'failures':failures}
(HERE/'prefix_mod81_constants_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'newly_nonzero':len(newly_nonzero),
                  'fourth_digit_profile':dict(new_digit_profile),
                  'outer_edges':rows[-2:],'failures':failures,'global_proof':False}))
if failures:
    raise SystemExit(1)
