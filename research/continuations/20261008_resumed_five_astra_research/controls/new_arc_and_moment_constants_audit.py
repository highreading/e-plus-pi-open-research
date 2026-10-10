from pathlib import Path
from math import comb, factorial, gcd
from collections import Counter
import hashlib, json, datetime

HERE=Path(__file__).resolve().parent
R=HERE.parent

def valuation(n,p):
    assert n != 0
    v=0
    while n%p==0:
        n//=p
        v+=1
    return v

fact_data=[]
for n,expected_v,expected_unit in [(2451,1223,1),(1084,539,2),(1367,678,1)]:
    f=factorial(n)
    v=valuation(f,3)
    unit=(f//3**v)%3
    assert (v,unit)==(expected_v,expected_unit)
    fact_data.append({'n':n,'v3_factorial':v,'normalized_unit_mod3':unit})
b=comb(2451,1084)
assert valuation(b,3)==6 and b%2187==1458
pole_cases=[]
for d in range(1,1036,2):
    vd=valuation(d,3)
    for layer in (1,2,3):
        a=(3*d-7)//2-243*layer
        if 0<=a<=816:
            vc=valuation(comb(816,a),3)
            bound=1 if vd<=1 else 3 if vd<=3 else 5
            assert vc>=bound
            pole_cases.append({'d':d,'layer':layer,'a':a,'v3_d':vd,
                               'v3_binomial_816_a':vc,'required_lower_bound':bound})
exception=[x for x in pole_cases if x['v3_d']==6]
assert [(x['layer'],x['a'],x['v3_binomial_816_a']) for x in exception]==[(2,604,5),(3,361,5)]

def arc_values(x):
    L=(x-1)*(x-9)*(x-25)
    A=13*x**3-455*x**2+3502*x-5850
    assert A==13*L+45*(3*x-65)
    assert 27*L==(3*x-65)*(9*x*x-120*x-269)-23560
    return A,L

rows=[]
profile=Counter()
for u in range(45):
    exponent=18+32*u
    assert exponent<=1426
    N=9**exponent
    x=4*(N-3)**2
    A,L=arc_values(x)
    raw_den=30*L
    g=gcd(A,raw_den)
    e5=int(u%5==1)
    e19=int(u%9==3)
    e31=int(u%15 in (5,7))
    expected=90*5**e5*19**e19*31**e31
    assert g==expected
    expected_v=[1,2,1+e5,e19,e31]
    actual_v=[valuation(g,p) for p in (2,3,5,19,31)]
    assert actual_v==expected_v
    assert not(e31 and(e5 or e19))
    aK=A//g
    dK=raw_den//g
    divisor=3*5**e5*19**e19*31**e31
    assert dK==L//divisor and L%divisor==0
    assert gcd(aK,dK)==1 and dK*285>=L
    assert valuation(dK,2)==0 and valuation(dK,3)==2
    assert 265050%g==0 and g<=8550
    rows.append({'u':u,'original_N_exponent_base9':exponent,
                 'N_mod_16':N%16,'N_mod_81':N%81,
                 'N_mod_25':N%25,'N_mod_19':N%19,'N_mod_31':N%31,
                 'actual_arc_gcd':g,'gcd_valuations_2_3_5_19_31':actual_v,
                 'reduced_denominator_divisor_of_L':divisor,
                 'v2_dK':0,'v3_dK':2,'reduced_pair_coprime':True})
    profile[g]+=1
assert dict(profile)=={90:26,450:8,1710:4,2790:6,8550:1}

sources={}
for p in [R/'responses/A1_turn8.md',R/'responses/A3_turn10.md',
          HERE/'NEW_ARC_AND_MOMENT_CONSTANTS_RECEIPT_GATE.md']:
    sources[str(p)]=hashlib.sha256(p.read_bytes()).hexdigest()
out={'status':'PASS','time':datetime.datetime.now().astimezone().isoformat(),
     'scope':'Two NEW bounded arithmetic checks; no global normalization or proof.',
     'source_sha256':sources,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'moment_constant':{'factorials':fact_data,'binomial_2451_1084_v3':6,
        'binomial_mod_2187':1458,'pole_cases':pole_cases,'sole_depth6_d':729},
     'original_arc':{'domain':'N=9^(18+32u), u=0..44',
        'exponent_bound':1426,'profile':dict(profile),'rows':rows,
        'uniform_conclusion_from_proof_not_finite_extrapolation':True}}
(HERE/'new_arc_and_moment_constants_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','arc_original_indices':len(rows),
        'arc_gcd_profile':dict(profile),'pole_cases':len(pole_cases),
        'binomial_mod_2187':1458,'global_proof':False}))
