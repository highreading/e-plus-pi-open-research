"""Verify the exceptional normalized seed using existing exact data.
No additional prime, degree, or lift calculation is performed.
The all-index digit and valuation deductions require the written proof.
"""
import json
from hashlib import sha256
from pathlib import Path
import sympy as sp

BASE = Path('work/session_20261001_astra/agent1')
source = BASE/'normalized_prime_seed_certificate.json'
certificate = json.loads(source.read_text())
assert certificate['status'] == 'PASS'
prime_rows = certificate['prime_certificates']
assert [item['p'] for item in prime_rows] == [5,7,11,13]
assert sum(len(item['rows']) for item in prime_rows) == 36
assert [item['p'] for item in prime_rows if item['uniform_unit_seeds']] == [7,11,13]
assert [(item['p'],r) for item in prime_rows for r in item['zero_residues']] == [(5,4)]

z = sp.symbols('z')
polynomial = sp.Poly(sp.expand((1-4*z-4*z*z)**2),z)
digits = [int(polynomial.nth(j)) % 5 for j in range(5)]
assert digits == [1,2,3,2,1]
assert all(digits)
exact_rows = certificate['exact_seed_rows']
assert [int(exact_rows[j]['endpoint_scalars']['P_n']) % 5 for j in range(5)] == digits

row = prime_rows[0]['rows'][4]
expected = {'h':0,'u':3,'v':3,'J':3,'Acal':3,'Bcal':0,
            'a':1,'k':2,'ell':3,'sigma':2,'C':2,'omega':1,'Vtilde':0}
assert all(row[key] == value for key,value in expected.items())
assert (row['sigma']*row['Acal']-row['C']*row['Bcal']-row['a']*row['omega']) % 5 == 0
pn,pu = sp.symbols('P_n P_next')
denominator_expression = 5*pu*row['C']-2*pn*row['sigma']
assert sp.Poly(denominator_expression-pn,pn,pu,modulus=5).is_zero
assert row['Dtilde_P_next_coefficient'] == 0
assert row['Dtilde_P_n_coefficient'] == 1

seed = exact_rows[4]
V = sp.Rational(seed['state']['Vtilde'])
D = sp.Rational(seed['endpoint_scalars']['Dtilde'])
assert D.q == 1 and int(D) % 5 == 1
assert sp.Rational(seed['endpoint_scalars']['V_original']) == 5*V

result = {
    'status':'PASS',
    'scope':'Existing 36 seed entries and the degree-four Legendre digit factor at p=5 only; no additional indices or lifts.',
    'source_certificate_sha256':sha256(source.read_bytes()).hexdigest(),
    'checker_sha256':sha256((BASE/'check_normalized_five_residual.py').read_bytes()).hexdigest(),
    'uniform_unit_seed_primes':[7,11,13],
    'only_zero_seed':{'p':5,'r':4,'state_mod_5':expected},
    'legendre_digit_factor_mod_5':digits,
    'normalized_denominator_residue':'Dtilde_n = P_n modulo 5 when n = 4 modulo 5',
    'existing_exact_seed_4':{'Vtilde':str(V),'Dtilde':str(D)},
    'paper_deductions_to_justify':[
        'The generating function gives P_(5m+r)=digit[r]*P_m modulo 5, so every P_n is a 5-adic unit.',
        'Consequently Dtilde_n is a unit on n=4 modulo 5; no common factor of positive 5-adic valuation can remove this normalized zero.',
        'The remaining depth concerns the full scaled numerator, including the second-kind term.'
    ],
    'independent_researcher_review':False
}
output = BASE/'normalized_five_residual_certificate.json'
output.write_text(json.dumps(result,indent=2),encoding='utf-8')
assert json.loads(output.read_text()) == result
print(json.dumps(result,indent=2))
