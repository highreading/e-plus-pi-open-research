"""Coordinator-authored bounded coefficient certificates; no remote code."""
import json, math, resource
from pathlib import Path

resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
OUT = Path(__file__).resolve().parent
P = (34,31,7,5,48,12,4,4,32,8,56,8)
Q = (52,36,24,6,112,48,64,8,32,32,64,112)
D = tuple((q-2*p) % 128 for p,q in zip(P,Q))
B = (69,106,54,56,120,80,112)
BETA = tuple(sum((-1)**s*B[s]*math.comb(s,k-1)
                 for s in range(k-1,7)) % 128 for k in range(1,8))
ROWS = ((0,4,64,68),(2,32,36,66),(1,3,16,20,34,48,52,65,67),
        (8,12,18,24,28,33,35,40,44,50,56,60))
RESIDUES = tuple(r for row in ROWS for r in row) + (96,100)

def choose(x,k):
    if k < 0: return 0
    if x >= 0: return math.comb(x,k) if k <= x else 0
    return (-1)**k * math.comb(k-x-1,k)

def fg(s,x,coeff,large_a=4):
    if not 0 <= s <= 11: return 0
    return choose(large_a+s-1,s)*sum(coeff[r]*choose(x,r-s)
                                   for r in range(s,12))

def z(s,x,large_a=4):
    if -7 <= s <= -1: return BETA[-s-1]
    return fg(s,x,D,large_a)

def u(s,x,large_a=4):
    return (fg(s,x,P,large_a)+x*fg(s,x-1,P,large_a)
            +x*fg(s+1,x-1,P,large_a))

def vv(s,x,large_a=4):
    return z(s,x,large_a)+x*z(s,x-1,large_a)+x*z(s+1,x-1,large_a)

def newton(values,mod):
    row = [v%mod for v in values]; result = []
    while row:
        result.append(row[0]); row = [(row[i+1]-row[i]) % mod
                                    for i in range(len(row)-1)]
    return result

def valuation2(n):
    return (n & -n).bit_length()-1

assert D == (112,102,10,124,16,24,56,0,96,16,80,96)
assert BETA == (113,74,78,72,120,80,112)
tables=[]; all_periodic=True
for rho in RESIDUES:
    uc={str(s):newton([u(s,128*t+rho)-u(s,rho) for t in range(13)],64)
        for s in range(-1,12)}
    vc={str(s):newton([vv(s,128*t+rho)-vv(s,rho) for t in range(13)],128)
        for s in range(-8,12)}
    ok=all(not any(a) for a in list(uc.values())+list(vc.values()))
    all_periodic &= ok
    tables.append({'rho':rho, 'U_s_minus1_to11_mod64':[u(s,rho)%64 for s in range(-1,12)],
        'V_s_minus8_to11_mod128':[vv(s,rho)%128 for s in range(-8,12)],
        'periodicity_newton_U':uc,'periodicity_newton_V':vc,'periodicity_pass':ok})

factor_u={str(s):newton([u(s,x,644)-u(s,x,4) for x in range(13)],64)
          for s in range(-1,12)}
factor_v={str(s):newton([vv(s,x,644)-vv(s,x,4) for x in range(13)],128)
          for s in range(-8,12)}
factor_pass=all(not any(a) for a in list(factor_u.values())+list(factor_v.values()))
table_pass=all(tuple(r for r in range(69) if valuation2(math.comb(68,r)) == depth)
                == row for depth,row in enumerate(ROWS))
overflow=tuple(r for r in range(69,128) if valuation2(math.comb(196,r)) <= 2)
table_pass &= overflow == (96,100)

# Independent direct finite signed Newton moment/reconstruction identity.
# Auxiliary n322,b209: these are bounded controls, not original powers.
a=644; bb=209
def sol(coeff,j):
    return sum(choose(-a,i-j)*(-1)**i*sum(coeff[r]*choose(i,r) for r in range(12))
               for i in range(max(j,0),bb)) if j < bb else 0
def theta(j): return sol(P,j) if j >= 0 else 0
def eta(j):
    if not 0 <= j < bb: return 0
    return sol(Q,j)-sum(B[s]*choose(-a,bb+s-j) for s in range(7))
def moment(j,s): return choose(a+bb-1-j,bb-1-j-s)
direct_fail=[]
for j in range(bb):
    first = j*theta(j-1)-theta(j)
    delta = j*(eta(j-1)-2*theta(j-1))-(eta(j)-2*theta(j))
    fm = (-1)**(j+1)*sum(u(s,j)*moment(j,s) for s in range(-1,12))
    gm = (-1)**(j+1)*sum(vv(s,j)*moment(j,s) for s in range(-8,12))
    if (first-fm)%64 or (delta-gm)%128: direct_fail.append(j)

receipt={'p_coeff_mod64':P,'q_coeff_mod128':Q,'d_coeff_mod128':D,
    'beta_1_to7_mod128':BETA,'residue_count':len(RESIDUES),
    'degree_bound_periodicity':12,'all_periodicity_certificates_pass':all_periodic,
    'A644_to_A4_factor_newton_U':factor_u,'A644_to_A4_factor_newton_V':factor_v,
    'bounded_factor_replacement_pass':factor_pass,'low_weight_table_pass':table_pass,
    'finite_direct_moment_indices':bb,'finite_direct_moment_failures':direct_fail,
    'tables':tables,'all_fixed_certificates_pass':all_periodic and factor_pass and table_pass and not direct_fail,
    'scope':'Exact bounded polynomial and auxiliary finite moment certificates only. '
            'No infinite fifth mixed-digit evaluation or original-family population assertion.'}
(OUT/'binary_fifth_moment_control.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({k:v for k,v in receipt.items() if k not in
    ('tables','A644_to_A4_factor_newton_U','A644_to_A4_factor_newton_V')}))
assert receipt['all_fixed_certificates_pass']
