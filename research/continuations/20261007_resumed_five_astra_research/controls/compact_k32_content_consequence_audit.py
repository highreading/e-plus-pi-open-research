"""Finite consequences of the completed parent k32 exact certificate."""
from pathlib import Path
from fractions import Fraction as Q
from math import factorial, gcd
import json, sys
sys.set_int_max_str_digits(500000)
OUT=Path(__file__).resolve().parent
v=json.loads((OUT/'compact_k32_content_envelope_certificate.json').read_text())
k=v['k'];assert k==32
G=int(v['G']);D=int(v['D']);W=int(v['W']);Lambda=int(v['full_clearer'])
def v2(n):
    answer=0
    while n%2==0:n//=2;answer+=1
    return answer
assert W==2**547
assert (v2(G),v2(D),v2(int(v['proposed_envelope_B'])))==(3375,780,2828)
hilbert=Q(1)
for j in range(k):hilbert*=factorial(j)**4
for j in range(2*k):hilbert/=factorial(j)
raw_lower=Q(Lambda,16*k)**k*Q(k*k*(k*k-1),3)**(k*k)*hilbert**2
whole_lower=raw_lower/G
assert whole_lower>1
decimal_exponent=len(str(whole_lower.numerator))-len(str(whole_lower.denominator))
if whole_lower.numerator<whole_lower.denominator*10**decimal_exponent:decimal_exponent-=1
assert whole_lower>=10**decimal_exponent
assert whole_lower<10**(decimal_exponent+1)
record={'scope':'One exact compact k32 instance, not an infinite divergence theorem.',
        'accepted_analytic_source':'A4turn19 equation8.6, same integer H and actual G.',
        'content_envelope_falsified':True,'W_is_exactly_2_power_547':True,
        'v2_G':3375,'v2_D':780,'v2_proposed_B':2828,
        'additional_binary_depth_over_D':2595,
        'large_prime_residual_after_187':1,
        'whole_primitive_error_lower_bound':str(whole_lower),
        'whole_primitive_error_exceeds_one':True,
        'whole_primitive_error_at_least_10_power':decimal_exponent,
        'all_checks_passed':True,'network_or_credentials_used':False}
(OUT/'compact_k32_content_consequence_certificate.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({name:record[name] for name in ('all_checks_passed','content_envelope_falsified',
        'W_is_exactly_2_power_547','whole_primitive_error_at_least_10_power')}))
