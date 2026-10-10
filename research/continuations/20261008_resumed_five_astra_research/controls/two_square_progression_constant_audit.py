from pathlib import Path
from math import prod
import hashlib,json
R=Path(__file__).resolve().parents[1]
primes=[3,5,7,11,13,17]
exponents=[120,60,40,24,20,15]
assert all(e*(p-1)==240 for p,e in zip(primes,exponents))
P=prod(p**e for p,e in zip(primes,exponents))
left=P*2**240
right=13**240
assert left>right
M=prod(primes)
assert M==255255
cert={'scope':'Exact fixed constants for the analytic progression bound; no original large-index computation.',
      'primes':primes,'lcm_prime_minus_one':240,'exponents':exponents,
      'progression_modulus':M,'prime_product_power':str(P),
      'lhs':str(left),'rhs':str(right),'positive_difference':str(left-right),
      'inequality':'2^240 * product(p^(240/(p-1))) > 13^240',
      'implication':'exp(sum(log(p)/(p-1))) > 13/2 > 6'}
cert['code_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
(R/'controls/two_square_progression_constant_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
print(json.dumps({'progression_modulus':M,'integer_inequality_pass':True,'positive_difference_digits':len(str(left-right))}))
