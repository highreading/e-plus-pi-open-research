"""Independent fixed receipt-transition checks; imported files are data only."""
import functools,hashlib,json,resource
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
OUT=Path(__file__).resolve().parent
SRC=Path('work/session_20261002_codex_continuation/agent1_arithmetic')
N=json.loads((SRC/'WEIGHTED_ENDPOINT_RATIONAL_NORM_RECEIPT.json').read_text())
L=json.loads((SRC/'WEIGHTED_ENDPOINT_COMPLETE_LINEAR_RECEIPT.json').read_text())
M=json.loads((SRC/'WEIGHTED_ENDPOINT_MOMENT_POLYNOMIAL_RECEIPT.json').read_text())
def coeff(v):return sum((x%8)<<(4*i) for i,x in enumerate(v))
def digits(a):return [(a>>(4*i))&7 for i in range(4)]
def add(a,b):return coeff([x+y for x,y in zip(digits(a),digits(b))])
@functools.lru_cache(maxsize=65536)
def mul(a,b):
    aa=digits(a);bb=digits(b);v=[0]*7
    for i,x in enumerate(aa):
        for j,y in enumerate(bb):v[i+j]+=x*y
    for i in range(6,3,-1):
        v[i-4]-=v[i];v[i-3]-=v[i]
    return coeff(v[:4])
def power(a,k):
    out=1
    for _ in range(k):out=mul(out,a)
    return out

def pp(a,b,odd=False):
    out={}
    for (i,j),c in a.items():
        for (u,v),d in b.items():
            x=i+u;y=j+v
            if odd:
                if x%2!=1 or y%2!=1:continue
                x//=2;y//=2
            t=mul(c,d)
            if t:out[x,y]=add(out.get((x,y),0),t)
    return {key:c for key,c in out.items() if c}
def ppower(a,k):
    out={(0,0):1}
    for _ in range(k):out=pp(out,a)
    return out
zeta=coeff(M['zeta_coefficients']);eta=power(zeta,5)
xy={(0,0):1,(1,0):7,(0,1):7,(1,1):1}
qs={}
for term,(a,b) in enumerate(N['unordered_root3_terms']):
    for phase in range(4):
        z=power(zeta,2**phase);et=power(eta,2**phase)
        pole={(0,0):1,(1,0):mul(7,mul(z,power(et,a))),(0,1):mul(7,mul(z,power(et,b)))}
        qs[term,phase]=ppower(pp(xy,ppower(pole,5)),4)
def unserialize(a):return {(i,j):c for i,j,c in a}
def serialize(a):return [[i,j,c] for (i,j),c in sorted(a.items())]
orbit=N['initial_and_orbit_states'];assert len(orbit)==7
checks=[]
for h in range(7):
    current=[unserialize(a) for a in orbit[h]]
    nxt=[serialize(pp(a,qs[i,h%4],odd=True)) for i,a in enumerate(current)]
    expected=orbit[h+1] if h<6 else orbit[3]
    assert nxt==expected,('norm transition',h)
    checks.append({'from_h':h,'to_h':h+1,'equals_saved_h':h+1 if h<6 else 3,'source_phase':h%4,'target_phase':(h+1)%4,'all_six_full_polynomials_equal':True})
assert (6+1)%4==3%4

def vector_step(v):
    assert len(v)==225
    out=[0]*225
    for a in range(15):
        for b in range(15):
            for x,y in ((0,1),(1,0),(1,1)):
                j=15*((2*a+x)%15)+(2*b+y)%15
                out[j]=(out[j]+v[15*a+b])%8
    return out
vo=L['full_vector_orbit'];assert len(vo)==11
for t in range(11):
    assert len(vo[t])==4
    nxt=[vector_step(v) for v in vo[t]]
    assert nxt==(vo[t+1] if t<10 else vo[3]),('linear',t)
summary={'status':'coefficientwise checks of EXISTING fixed closure receipts pass; initial representation and full scalar reconstruction remain paper dependencies',
 'norm_full_polynomial_transition_checks':checks,'norm_preperiod':3,'norm_period':4,'phase_included':True,
 'linear_all_four_225_coordinate_transitions_verified':11,'linear_preperiod':3,'linear_period':8,
 'source_sha256':{name:hashlib.sha256((SRC/name).read_bytes()).hexdigest() for name in ('WEIGHTED_ENDPOINT_RATIONAL_NORM_RECEIPT.json','WEIGHTED_ENDPOINT_COMPLETE_LINEAR_RECEIPT.json')},
 'no_archive_program_executed':True}
(OUT/'weighted_closure_audit.json').write_text(json.dumps(summary,indent=2)+'\n')
excerpt={'source_archive_path':str(SRC/'WEIGHTED_ENDPOINT_RATIONAL_NORM_RECEIPT.json'),
 'source_sha256':summary['source_sha256']['WEIGHTED_ENDPOINT_RATIONAL_NORM_RECEIPT.json'],
 'coefficient_ring':N['coefficient_ring'],'unordered_root3_terms':N['unordered_root3_terms'],
 'packed_coefficient_convention':'sum c_i*2^(4i), c_i in 0..7, basis 1,x,x^2,x^3; x^4=-x-1',
 'full_state_preperiod':3,'full_state_period':4,'source_phase_h3':3,'source_phase_h6':2,
 'complete_six_polynomial_state_h3':orbit[3],'complete_six_polynomial_state_h6':orbit[6],
 'h7_computed_coefficientwise_equals_h3':True,'all_transition_checks':checks,'outputs':N['outputs']}
(OUT/'weighted_norm_closure_excerpt.json').write_text(json.dumps(excerpt)+'\n')
print(json.dumps(summary,indent=2))
