"""Main-authored bounded controls; the infinite counterexample has a separate proof."""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import hashlib
import json

def e_lower(m): return sum((Q(1,factorial(k)) for k in range(m+1)),Q(0))
def atan_interval(den,m):
    s=sum((Q((-1)**k,(2*k+1)*den**(2*k+1)) for k in range(m)),Q(0))
    nxt=Q((-1)**m,(2*m+1)*den**(2*m+1))
    return min(s,s+nxt),max(s,s+nxt)
ea=e_lower(200)
eb=ea+Q(2,factorial(201))
a,b=atan_interval(5,80)
c,d=atan_interval(239,80)
pa,pb=16*a-4*d,16*b-4*c
assert 3<pa<pb<4
lo,hi=ea+pa,eb+pb
partial=[]; convergents=[]
p0,p1,q0,q1=0,1,1,0
for _ in range(4):
    z=lo.numerator//lo.denominator
    assert z==hi.numerator//hi.denominator
    partial.append(z)
    p0,p1=p1,z*p1+p0
    q0,q1=q1,z*q1+q0
    convergents.append([p1,q1])
    lo,hi=1/(hi-z),1/(lo-z)
assert partial==[5,1,6,7]
assert convergents[-1]==[293,50]
v=[]; controls=[]
for n in range(1,7):
    em=e_lower(20*n+20)
    rhat=1-sum((vk*em**k for k,vk in enumerate(v,1)),Q(0))
    vn=(rhat-Q(1,2*factorial(n)))/em**n
    assert 0<vn<=Q(1,2**n*factorial(n-1))
    v.append(vn)
    ra=1-sum((vk*eb**k for k,vk in enumerate(v,1)),Q(0))
    rb=1-sum((vk*ea**k for k,vk in enumerate(v,1)),Q(0))
    assert Q(1,3*factorial(n))<ra<=rb<Q(1,2*factorial(n))
    encoded=f'{vn.numerator}/{vn.denominator}'.encode()
    controls.append({'n':n,'coefficient_sha256':hashlib.sha256(encoded).hexdigest(),
                     'positive':True,'entire_majorant_bound':True,'residual_interval_inside_1_over_3n_factorial_and_1_over_2n_factorial':True})
out={'author':'main Codex','arithmetic':'exact Fraction; e Taylor and alternating Machin intervals',
     'scope':'First six construction coefficients and four e+pi continued-fraction entries only; all-n validity is established in the separate main proof',
     'e_plus_pi_first_four_partial_quotients':partial,'convergents':convergents,
     'foukzon_recursive_counterexample_controls':controls,
     'carella_2_4_sqrt2_bounds': {'alpha_lower_7_over_5_square_below_2':Q(7,5)**2<2,
                               'alpha_upper_3_over_2_square_above_2':Q(3,2)**2>2,
                               'beta_upper_5_over_3_equivalent':Q(27,20)**2<2,
                               'product_9_over_4_equals_two_3_over_2_convergents':Q(3,2)**2==Q(9,4)},
     'carella_15_4_golden_ratio_control':{'sqrt5_greater_than_20_over_9':Q(20,9)**2<5,
                                       'sqrt5_less_than_7_over_3':5<Q(7,3)**2}}
Path(__file__).with_name('EXTERNAL_CLAIM_MAIN_CONTROLS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'continued_fraction':partial,'fourth_convergent':convergents[-1],'recursive_coefficients_checked':len(controls)}))
