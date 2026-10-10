"""NEW exact divided-contact/Laguerre coordinate diagnostic.

Classical Laguerre moments and OLD integral T lattice are reuse.
This bounded question concerns factorial-divided y^r, y=t(t-2)/2.
No all-r integrality or primitive determinant upper is inferred.
"""
from pathlib import Path
from fractions import Fraction
import hashlib,json,math,time
H=Path(__file__).resolve().parent
OUT=H/'THETA_DIVIDED_LAGUERRE_COORDINATE_RECEIPT.json'
assert not OUT.exists()
start=time.monotonic();limit=32
rows=[];nonintegral=[]
for r in range(limit+1):
    row=[]
    for m in range(2*r+1):
        num=sum(math.comb(r,s)*(-2)**(r-s)*math.factorial(r+s)*
                (math.comb(r+s,m) if m<=r+s else 0)
                for s in range(r+1))*(-1)**m
        c=Fraction(num,(1<<r)*math.factorial(r))
        row.append(c)
        if c.denominator!=1:nonintegral.append([r,m,c.numerator,c.denominator])
    rows.append(row)
    odddouble=math.prod(range(1,2*r,2))
    assert row[-1]==odddouble
    if r:assert row[-2]==-(2*r-1)*odddouble
theta=[1,0]
for j in range(1,2*limit+1):theta.append((2*j+1)*theta[-1]+theta[-2])
assert all(rows[r][0]==theta[r] for r in range(limit+1))
gram=[]
for r in range(limit+1):
    for s in range(r,limit+1):
        got=sum(a*b for a,b in zip(rows[r],rows[s]))
        expected=math.comb(r+s,r)*theta[r+s]
        assert got==expected
        gram.append([r,s,got.numerator,got.denominator])
receipt={'time':time.strftime('%Y-%m-%d %H:%M:%S'),
 'scope':'NEW bounded r0..32 exact divided-contact coordinates only; not all-degree integrality or filtered/paired upper',
 'variable':'y=t(t-2)/2; standard orthonormal Laguerre L_m(t)',
 'coordinate_formula':'(-1)^m/(2^r*r!)*sum_s binom(r,s)*(-2)^(r-s)*(r+s)!*binom(r+s,m)',
 'network_and_credentials_denied_by_sandbox':True,'coordinator_authored':True,
 'r_limit':limit,'all_checked_coordinates_integral':not nonintegral,
 'nonintegral_coordinates':nonintegral,
 'all_checked_Gram_binomial_theta_identities_pass':True,
 'Gram_pair_count':len(gram),'leading_two_coordinate_identities_pass':True,
 'coordinate_rows':[[[c.numerator,c.denominator] for c in row] for row in rows],
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'seconds':round(time.monotonic()-start,3)}
OUT.write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({k:v for k,v in receipt.items() if k!='coordinate_rows'}))
