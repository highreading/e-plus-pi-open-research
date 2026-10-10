"""Exact algebraic rate comparisons and CRT count, no degree/prime scan."""
from pathlib import Path
from math import prod
import json

HERE=Path(__file__).resolve().parent

def pell(k):
    a,b=1,0
    for _ in range(k):a,b=a+2*b,a+b
    return a,b

def compare_integer_pell(left,k):
    a,b=pell(k)
    d=left-a
    if d<=0:sign=-1
    else:sign=(d*d>2*b*b)-(d*d<2*b*b)
    assert sign!=0
    return dict(left_integer=left,pell_exponent=k,pell_a=a,pell_b=b,
                sign=sign,squared_comparison_margin=d*d-2*b*b)

checks={
    # Six times [1.5log2 + .5log5 + log13/6] versus six times threshold.
    'all_even':compare_integer_pell(2**9*5**3*13,12),
    # Six times base+weight7 versus six times threshold.
    'odd_7_good':compare_integer_pell(5**3*13*7**2,12),
    # Seventy-two times base+the two smallest optional weights.
    'odd_smallest_two_good':compare_integer_pell(5**36*13**12*17**9*19**8,144),
    # Thirty times base+the largest single optional weight.
    'odd_largest_single_good_insufficient':compare_integer_pell(5**15*13**5*11**6,60),
}
assert checks['all_even']['sign']==1
assert checks['odd_7_good']['sign']==1
assert checks['odd_smallest_two_good']['sign']==1
assert checks['odd_largest_single_good_insufficient']['sign']==-1

component_counts={'bad11_bad17_good19':1*2*18,
                  'bad11_good17_bad19':1*15*1,
                  'good11_bad17_bad19':10*2*1,
                  'all_three_bad':1*2*1}
exceptional_other=sum(component_counts.values())
assert exceptional_other==73
odd_unexcluded=2*exceptional_other
modulus=7*11*17*19
assert (odd_unexcluded,modulus)==(146,24871)
out=dict(scope='Exact finite closed-prime comparison, contingent on reviewed actual divisor inputs.',
         all_checks_pass=True,rate_checks=checks,
         crt_component_counts=component_counts,
         unexcluded_residue_count=odd_unexcluded,odd_modulus=modulus,
         density_among_odd=f'{odd_unexcluded}/{modulus}',
         density_among_all=f'{odd_unexcluded}/{2*modulus}',
         warning='Unexcluded means the mandatory divisor is insufficient; it is not an upper bound for actual q.')
(HERE/'hp_b1_closed_prime_rate_and_crt_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='rate_checks'},indent=2))
