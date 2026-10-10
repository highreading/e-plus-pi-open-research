import sympy as s
import json
from pathlib import Path
from functools import lru_cache

BASE = Path('work/session_20261001_astra/agent1')
x = s.symbols('x')

@lru_cache(None)
def coefficients(k):
    poly = s.Poly(s.expand((1-x+x*x/2)**k), x)
    return [poly.nth(j) for j in range(2*k+1)]

def falling(n, j):
    return s.factorial(n)/s.factorial(n-j)

def D(j):
    return s.factorial(j)*sum(1/s.factorial(i) for i in range(j+1))

def state(k):
    a = coefficients(k)
    derivatives = [sum(falling(k,j+d)*a[j] for j in range(k-d+1)) for d in range(3)]
    h,u,v = derivatives
    return h, k*h+u, k*(k-1)*h+2*k*u+v

def objects(n):
    h,j,_ = state(n)
    H,J,K = state(n+1)
    A = sum(falling(n,i)*coefficients(n)[i]*D(2*n-i) for i in range(n+1))
    B = 2*D(2*n+1)+sum(falling(n,i-1)*(2*n+2-i)*coefficients(n+1)[i]*D(2*n+1-i) for i in range(1,n+2))
    S = J*J-H*K
    C = (J-H)*j-(K-J)*h
    W = J*j-K*h
    V = S*A-(n+1)*C*B-H*W
    return list(map(s.simplify,[h,j,H,J,K,A,B,S,C,W,V]))

@lru_cache(None)
def L(k):
    if k == 0: return s.Integer(1)
    if k == 1: return 4*x-2
    return s.expand((2*(2*k-1)*(2*x-1)*L(k-1)+4*(k-1)*L(k-2))/k)

def moment(j):
    return sum(s.binomial(j,h)*(-1)**(h//2)*s.Rational(2,h+1) for h in range(0,j+1,2))/2**j

def w(k):
    poly = s.Poly(s.cancel((L(k)-L(k).subs(x,1))/(x-1)),x)
    return sum(poly.nth(j)*moment(j) for j in range(max(0,k)))

def T(n,k):
    poly = s.Poly(L(k),x)
    return sum(poly.nth(j)*D(n+j)/s.factorial(n+j) for j in range(k+1))

def mod(a,p):
    a = s.Rational(a)
    return int(a.p % p)*pow(int(a.q % p),-1,p)%p

result = {'scope':'Formal substitution; direct rational checks at n=2,8; complete seed transfer for predeclared primes 3,5 only. No HP construction or degree search.'}
N,F,SS,CC,HH,WW,AA,BB,wp,wu = s.symbols('N F S C H W A B wp wu')
original = 2*(wp+F*AA)*SS-(N+1)**2*(wu+2*F*BB/(N+1))*CC-2*F*HH*WW
normalized = 2*wp*SS-(N+1)**2*wu*CC+2*F*(SS*AA-(N+1)*CC*BB-HH*WW)
assert s.cancel(original-normalized)==0
result['formal_identity'] = 'PASS'
result['direct_checks'] = []
for n in [2,8]:
    h,j,H,J,K,A,B,S,C,W,V = objects(n)
    f = s.Rational(2**n,s.factorial(n)**2)
    tp,tu = T(n,n),T(n,n+1)
    assert tp == f*A and tu == 2*f*B/(n+1)
    for k in [n,n+1]:
        poly = s.Poly(L(k),x)
        Hk,Jk,Kk = state(k)
        fk = s.Rational(2**k,s.factorial(k)**2)
        for d,target in enumerate([Hk,Jk,Kk]):
            direct = sum(poly.nth(i)/s.factorial(k+i-d) for i in range(k+1) if k+i>=d)
            assert direct == fk*target
    X = 2*(w(n)+tp)*S-(n+1)**2*(w(n+1)+tu)*C-2*f*H*W
    Q = 2*w(n)*S-(n+1)**2*w(n+1)*C
    assert s.simplify(X-Q-2*f*V)==0
    denominator = (n+1)**2*L(n+1).subs(x,1)*C-2*L(n).subs(x,1)*S
    assert denominator != 0
    ratio = s.cancel(X/denominator)
    result['direct_checks'].append({'n':n,'V':str(V),'Dcal':str(denominator),'Xcal':str(X),'actual_q':str(s.denom(ratio)),'status':'PASS'})
result['small_seeds'] = {str(n):str(objects(n)[-1]) for n in [0,1]}
assert objects(0)[-1]==4 and objects(1)[-1]==32
result['seed_certificates'] = []
for p in [3,5]:
    residues = []
    for r in range(p):
        seed = [mod(a,p) for a in objects(r)]
        transferred = [mod(a,p) for a in objects(p+r)]
        assert seed == transferred
        residues.append(seed[-1])
    assert residues[-1]==0
    result['seed_certificates'].append({'p':p,'V_residues':residues,'zero_residues':[r for r,v in enumerate(residues) if v==0],'tuple_transfer':'PASS'})
result['status']='PASS'
(BASE/'certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
