from pathlib import Path
import hashlib, sys
sys.path.insert(0, '[private local path removed]')
import sympy as sp
root=Path('[private local path removed]')
p=root/'work/astra_review_registry/candidates/w3-b2-five-residue-four-loss-v1.md'
data=p.read_bytes()
marker=b'Status: unverified author candidate submitted for independent review.'
start=data.index(marker)
expected='e08cc00ef7c40a2bdfda278145fa8330dbac4fbc58b3723fe44b76131acf8e43'
actual=hashlib.sha256(data[start:]).hexdigest()
assert actual==expected, (start,actual)
u=sp.symbols('u'); m=5*u

def fall(a,t):
    return sp.prod(a-j for j in range(t))
def coeff(a,t):
    return sp.expand(sum((-1)**(t-2*j)*fall(a,t-j)/(2**j*sp.factorial(j)*sp.factorial(t-2*j)) for j in range(t//2+1)))
def zero_mod(expr,mod):
    for c in sp.Poly(sp.expand(expr),u).all_coeffs():
        num,den=map(int,sp.fraction(c))
        assert den%5!=0, (expr,c)
        assert num*pow(den,-1,mod)%mod==0, (expr,c,mod)
checks=0
for a,expected_row in [(m,[1,-m,0,m/6,m/8]),(m-1,[1,1-m,sp.Rational(1,2)-m,-m/3,-sp.Rational(1,4)+7*m/24])]:
    for t,value in enumerate(expected_row):
        zero_mod(coeff(a,t)-value,25); checks+=1
for a,row in [(m,[-u,0,0,0,0]),(m-1,[1-u,3-u,2*u,1,1-u])]:
    for t,value in enumerate(row,5):
        zero_mod(coeff(a,t)-value,5); checks+=1
for t,value in enumerate([1,m-1,2-3*m,-6+11*m,24]):
    zero_mod(fall(m-1,t)-value,25); checks+=1
for t,value in enumerate([4,1,3,1,1],5):
    zero_mod(fall(m-1,t)-(m-5)*value,25); checks+=1
zero_mod(sum(fall(m-1,t)*coeff(m,t) for t in range(10))-(1+3*m+5*u*(u-1)),25); checks+=1
zero_mod(sum(fall(m-1,t+1)*coeff(m,t) for t in range(9))-(3*m-1-5*u*(u-1)),25); checks+=1
print({'payload_start':start,'payload_sha256':actual,'whole_file_sha256':hashlib.sha256(data).hexdigest(),'finite_table_checks':checks,'status':'passed'})