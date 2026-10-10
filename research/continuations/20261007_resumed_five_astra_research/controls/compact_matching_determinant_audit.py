"""Parent-authored exact finite audit; no numerical oracle or external code."""
from fractions import Fraction as F
from math import factorial,gcd
from pathlib import Path
import json

# A monomial exponential integral is a_d*e+(-1)^(d+1)*d!, from integration by parts.
def exponential(d):
    a=1
    for m in range(1,d+1):a=1-m*a
    independent=sum((-1)**j*factorial(d)//factorial(d-j) for j in range(d+1))
    assert a==independent
    return F(a),F((-1)**(d+1)*factorial(d))

# Four times the arctangent integral obeys J_d=4/(d-1)-J_(d-2).
def arctangent(d):
    assert d%2==0
    pi_part,rational_part=F(1),F(0)
    for m in range(2,d+1,2):
        pi_part,rational_part=-pi_part,F(4,m-1)-rational_part
    return pi_part,rational_part

rows=[{0:-117,2:-4,4:1},{0:-6884,2:-133,6:1}]
matrix=[]
for row in rows:
    values=[]
    for j in range(2):
        e_part=pi_part=rational=F(0)
        for d,c in row.items():
            ae,re=exponential(d+2*j);ap,rp=arctangent(d+2*j)
            e_part+=c*ae;pi_part+=c*ap;rational+=c*(re+rp)
        assert e_part==pi_part
        values.append((rational,e_part))
    matrix.append(values)

def product(a,b):return [a[0]*b[0],a[0]*b[1]+a[1]*b[0],a[1]*b[1]]
left=product(matrix[0][0],matrix[1][1]);right=product(matrix[0][1],matrix[1][0])
coeff=[a-b for a,b in zip(left,right)]
assert coeff==[F(1289257492,1575),F(-223466880,1575),F(0)]
raw=(1289257492,223466880);content=gcd(*raw)
assert content==4
primitive=(raw[0]//content,raw[1]//content)
assert primitive==(322314373,55866720)
lower_e=F(65,24);lower_pi=4*(F(1,2)-F(1,24)+F(1,3)-F(1,81))
assert lower_pi==F(505,162)
assert lower_e+lower_pi>F(29,5)>F(raw[0],raw[1])
def pair(x):return [x.numerator,x.denominator]
data={"scope":"One finite compact determinant only; no infinite sequence or irrationality proof.",
      "parent_authored":True,"period_matching_all_four_entries":True,
      "matrix":[[[pair(x) for x in v] for v in row] for row in matrix],
      "determinant_coefficients_constant_s_s_squared":[pair(x) for x in coeff],
      "raw_integer_pair":raw,"content":content,"primitive_integer_pair":primitive,
      "nonzero_sign":"negative, by exact elementary lower bounds",
      "e_lower_bound":pair(lower_e),"pi_lower_bound":pair(lower_pi),"all_checks_passed":True}
out=Path(__file__).with_name('compact_matching_determinant_certificate.json')
out.write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps({"all_checks_passed":True,"primitive_integer_pair":primitive,"scope":data["scope"]}))
