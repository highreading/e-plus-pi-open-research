"""Parent-authored exact consequences; finite scope only, no network or keys."""
from pathlib import Path
from fractions import Fraction as Q
from math import factorial, gcd
import json, sys
sys.set_int_max_str_digits(500000)
OUT=Path(__file__).resolve().parent
OLD=OUT.parents[1]/'astra_pro5_resume_20261007'/'controls'
c32=json.loads((OLD/'compact_k32_content_envelope_certificate.json').read_text())
c33=json.loads((OUT/'compact_k33_content_envelope_certificate.json').read_text())
assert c32['k']==32 and c33['k']==33

def v2(n):
    assert n>0
    return (n&-n).bit_length()-1

def decade(value):
    assert value>0
    n,d=value.numerator,value.denominator
    e=len(str(n))-len(str(d))
    target=Q(10**e) if e>=0 else Q(1,10**(-e))
    if value<target:e-=1
    target=Q(10**e) if e>=0 else Q(1,10**(-e))
    assert target<=value<10*target
    return e

p32,q32=int(c32['primitive_p']),int(c32['primitive_q'])
p33,q33=int(c33['primitive_p']),int(c33['primitive_q'])
assert gcd(p32,q32)==gcd(p33,q33)==1
delta=p33*q32-p32*q33
gap=Q(delta,q32*q33)

# Classical rigorous Taylor/Machin bounds, reused to enclose the fixed constant.
en=300
elo=sum((Q(1,factorial(j)) for j in range(en+1)),Q(0))
ehi=elo+Q(2,factorial(en+1))
def atan_even_enclosure(a,N=128):
    assert N%2==0
    lower=sum((Q((-1)**j,(2*j+1)*a**(2*j+1)) for j in range(N)),Q(0))
    upper=lower+Q(1,(2*N+1)*a**(2*N+1))
    return lower,upper
a5l,a5u=atan_even_enclosure(5)
a239l,a239u=atan_even_enclosure(239)
sl=elo+16*a5l-4*a239u
su=ehi+16*a5u-4*a239l
assert sl<su
eps32l,eps32u=sl-Q(p32,q32),su-Q(p32,q32)
eps33l,eps33u=sl-Q(p33,q33),su-Q(p33,q33)
assert eps32l>0 and eps33l>0
assert gap>0 and gap==eps32l-eps33l==eps32u-eps33u
ratio_l,ratio_u=eps33l/eps32u,eps33u/eps32l
contraction_l=gap/eps32u

rows=[]
for c in [c32,c33]:
    k=c['k'];G=int(c['G']);D=int(c['D']);W=int(c['W']);Lambda=int(c['full_clearer'])
    hilbert=Q(1)
    for j in range(k):hilbert*=factorial(j)**4
    for j in range(2*k):hilbert/=factorial(j)
    raw_lower=Q(Lambda,16*k)**k*Q(k*k*(k*k-1),3)**(k*k)*hilbert**2
    whole_lower=raw_lower/G
    e=decade(whole_lower)
    row={'k':k,'v2_G':v2(G),'v2_D':v2(D),'additional_binary_depth_over_D':v2(G)-v2(D),
         'v2_proposed_B':v2(int(c['proposed_envelope_B'])),'W_is_power_of_two':W>0 and W&(W-1)==0,
         'W_binary_exponent':v2(W) if W>0 and W&(W-1)==0 else None,
         'primitive_q_digits':len(str(int(c['primitive_q']))),
         'whole_lower_accepted_source':'A4turn19 equation8.6, original H, k>=32.',
         'whole_primitive_error_lower_bound':str(whole_lower),'whole_error_at_least_10_power':e}
    rows.append(row)

record={'parent_authored':True,'scope':'Only exact compact indices32 and33; no eventual theorem and no original binary instance.',
        'all_checks_passed':True,'network_or_credentials_used':False,
        'constant_enclosure':{'e_Taylor_terms_through':en,'atan_terms_each':128,'lower':str(sl),'upper':str(su),
                              'width_decimal_exponent':decade(su-sl)},
        'primitive_delta':str(delta),'delta_positive':delta>0,'delta_decimal_digits':len(str(abs(delta))),
        'exact_adjacent_rational_gap':str(gap),'gap_decimal_exponent':decade(gap),
        'error32_lower':str(eps32l),'error32_upper':str(eps32u),
        'error33_lower':str(eps33l),'error33_upper':str(eps33u),
        'error_ratio_lower':str(ratio_l),'error_ratio_upper':str(ratio_u),
        'error_ratio_below_one_half':ratio_u<Q(1,2),
        'contraction_lower':str(contraction_l),'contraction_exceeds_one_half':contraction_l>Q(1,2),
        'denominator_ratio_decimal_exponent':decade(Q(q33,q32)),
        'indices':rows}
(OUT/'compact_k32_k33_adjacent_certificate.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'all_checks_passed':True,'delta_positive':delta>0,'delta_digits':len(str(abs(delta))),
      'gap_decimal_exponent':record['gap_decimal_exponent'],
      'error_ratio_below_half':record['error_ratio_below_one_half'],
      'q33_over_q32_decimal_exponent':record['denominator_ratio_decimal_exponent'],
      'indices':[{k:r[k] for k in ['k','v2_G','v2_D','W_binary_exponent','primitive_q_digits','whole_error_at_least_10_power']} for r in rows]},indent=2))
