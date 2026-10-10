#!/usr/bin/env python3
"""New finite min-plus and parity audit of A5's original kernel lattice.

No Gram sums are regenerated. All82 shifts and both complete parity lifts
are checked with the actual original binary word and finite terminal state.
"""
from pathlib import Path
from math import comb
import hashlib
import json
import resource

resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
ROOT = Path(__file__).resolve().parent
b, n = 9**18, 4002*9**18
N, a = n+2, 2*n

def atom_minimum(N, B, C, start=0):
    S = B+C
    flags = {(0,0,0):0} if start == 0 else {(0,0,0):0,(1,0,0):0,(1,0,1):0,(1,1,1):0}
    trace = {}
    for t in range(start,max(N,B,C,S).bit_length()):
        bits = [(x >> t) & 1 for x in (N,B,S)]
        kappa = (S >> (t+1))-(B >> (t+1))-(C >> (t+1))
        out = {}
        for state,cost in flags.items():
            for digit in (0,1):
                new = tuple(int(digit+borrow > bit) for borrow,bit in zip(state,bits))
                increment = kappa+new[0]+new[1]-new[2]
                assert increment in (0,1,2)
                out[new] = min(out.get(new,10**9),cost+increment)
        flags = out
        if t+1 in (8,16,24,32,38,41,48,52,58):
            trace[str(t+1)] = {str(4*f[0]+2*f[1]+f[2]):v for f,v in sorted(flags.items())}
    return flags[(0,0,0)],trace

def choose_valuation(top,bottom):
    if bottom < 0 or bottom > top:
        return None
    return bottom.bit_count()+(top-bottom).bit_count()-top.bit_count()

shift_minima = []
for r in range(82):
    val, _ = atom_minimum(N,b-r,a+80)
    assert val >= 8
    shift_minima.append(val)
upper, trace = atom_minimum(N,b-81,a+80,8)
assert upper == 7
assert trace['38'] == {'0':4,'2':5,'6':6,'7':5}
assert trace['41'] == {'0':4,'2':6,'6':6,'7':8}
jstar = sum(1 << k for k in (9,10,23,27,31,43,48,50))
k = b-81-jstar
assert 0 <= jstar <= b-81
witness = choose_valuation(N,jstar)+choose_valuation(a+80+k,k)
assert witness == 8 and min(shift_minima) == 8
first_parity_min, _ = atom_minimum(N,b-3,a+2)
second_parity_min, _ = atom_minimum(N,b,a-1)
assert first_parity_min >= 11 and second_parity_min >= 10
source = ROOT/'binary_short_moment_certificate.json'
data = json.loads(source.read_text())
af, ae = data['short_first_numerator'],data['short_exponential_numerator']
common_e = [sum(ae[j]*(-1)**(r-j)*comb(4,r-j) for j in range(max(0,r-4),min(r,len(ae)-1)+1)) % 4 for r in range(82)]
first_lift = [(-1)**(r-3)*comb(78,r-3) % 4 if 3 <= r <= 81 else 0 for r in range(82)]
second_lift = [(-1)**r*comb(81,r) % 4 for r in range(82)]
diff_f = [(x-y) % 4 for x,y in zip(af,first_lift)]
diff_e = [(x-y) % 4 for x,y in zip(common_e,second_lift)]
assert all(x % 2 == 0 for x in diff_f+diff_e)
bf, be = [x//2 for x in diff_f],[x//2 for x in diff_e]
sets = {0:list(range(38,42))+list(range(46,50))+list(range(70,74))+list(range(78,82)),
        4:list(range(34,38))+list(range(42,46))+list(range(66,70))+list(range(74,78)),
        64:list(range(6,10))+list(range(14,18)),
        68:list(range(2,6))+list(range(10,14))}
for J,ss in sets.items():
    expected = [r for r in range(82) if ((81-r) & 16) == 0 and ((81-r) & 68) == J]
    assert sorted(ss) == expected
chi_f = [sum(bf[r] for r in sets[J]) % 2 for J in (0,4,64,68)]
chi_e = [sum(be[r] for r in sets[J]) % 2 for J in (0,4,64,68)]
artifact = {
    'status':'PASS','scope':'NEW original-word pointwise min-plus and short-numerator parity audit; no Gram evaluation',
    'n':str(n),'b':str(b),'shift_minima_0_to81':shift_minima,'sharp_kernel_content':8,
    'upper_minimum':upper,'upper_trace':trace,'attaining_j':str(jstar),'attaining_shift':81,
    'attaining_valuation':witness,'parity_lift_content_minima':[first_parity_min,second_parity_min],
    'chi_order':[0,4,64,68],'chi_first':chi_f,'chi_second':chi_e,
    'physical_first_content':{'value_or_lower_bound':9 if any(chi_f) else 10,'exact':any(chi_f)},
    'physical_second_content':{'value_or_lower_bound':9 if any(chi_e) else 10,'exact':any(chi_e)},
    'four_parity_support_theorem_independently_reviewed':False,
    'parity_content_interpretation':'A5 theorem11; min-plus, witness and parity sums independently checked here',
    'physical_bits_retained':20,'all_prime_gcd_evaluated':False,'irrationality_proved':False,
    'short_payload_sha256':hashlib.sha256(source.read_bytes()).hexdigest()
}
target = ROOT/'binary_kernel_content_certificate.json'
target.write_text(json.dumps(artifact,indent=2)+'\n')
receipt = {k:v for k,v in artifact.items() if k not in ('shift_minima_0_to81','upper_trace')}
receipt['source_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
receipt['artifact_sha256'] = hashlib.sha256(target.read_bytes()).hexdigest()
(ROOT/'binary_kernel_content_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt))
