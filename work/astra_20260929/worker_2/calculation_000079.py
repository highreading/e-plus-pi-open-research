from pathlib import Path
import hashlib, json, sys
sys.path.insert(0, '[private local path removed]')
import sympy as s

root = Path('[private local path removed]')
path = root / 'work/astra_review_registry/candidates/worker3-microscopic-reference-and-sharp-cofactor-bound-v1.md'
raw = path.read_bytes()
payload = raw.split(b'\n\n', 2)[2]
expected = '48241943005ab30cb868e89f6e9927046c2fa5a6f81ea94e10f38e5155682718'
actual = hashlib.sha256(payload).hexdigest()
assert actual == expected, {'payload_sha256': actual, 'expected': expected}

t, T = s.symbols('t T')
p = [s.Integer(1), t-s.Rational(1,2)]
for m in range(1, 7):
    beta = s.Rational(m*m, 4*(4*m*m-1))
    p.append(s.expand((t-s.Rational(1,2))*p[-1] + beta*p[-2]))

def moment(r):
    return sum(s.Rational(2, 2*k+1)*s.binomial(r,2*k)*(-1)**k for k in range(r//2+1))/2**r

def functional(poly):
    return s.expand(sum(coeff*moment(power[0]) for power,coeff in s.Poly(s.expand(poly),t).terms()))

def zero(expr):
    assert s.cancel(s.expand(expr)) == 0

normalization_checks = 0
for m in range(8):
    original = s.I**m*s.legendre(m,-s.I*(2*t-1))/s.binomial(2*m,m)
    zero(original-p[m])
    normalization_checks += 1

h = [s.Rational(2*(-1)**m, (2*m+1)*int(s.binomial(2*m,m))**2) for m in range(8)]
chi = []
for m in range(8):
    quotient, remainder = s.div(p[m]-p[m].subs(t,1), 1-t, t)
    zero(remainder)
    chi.append(s.expand(p[m].subs(t,1)*T + functional(quotient)))

kernel_checks = 0
for n in range(6):
    zero(functional(p[n]**2)-h[n])
    V = s.expand(sum(p[k]*p[k].subs(t,1)/h[k] for k in range(n+1)))
    H = s.expand(sum(chi[k]*p[k]/h[k] for k in range(n+1)))
    b = p[n+1].subs(t,1)/p[n].subs(t,1)
    zero((t-1)*V-p[n].subs(t,1)*(p[n+1]-b*p[n])/h[n])
    zero(1-(1-t)*H-(chi[n]*p[n+1]-chi[n+1]*p[n])/h[n])
    zero(p[n+1].subs(t,1)*chi[n]-p[n].subs(t,1)*chi[n+1]-h[n])
    V0 = V.subs(t,0)
    W0 = 1-H.subs(t,0)
    zero(V0+2*p[n].subs(t,1)*p[n+1].subs(t,0)/h[n])
    eps = (-1)**n*chi[n]/p[n].subs(t,1)
    alpha = chi[n+1]/chi[n]
    zero(W0/V0-(-1)**(n+1)*eps*(1+alpha/b)/2)
    kernel_checks += 6

symbolic_vandermonde_checks = 0
for d in range(1,5):
    X = s.symbols('x0:'+str(d))
    matrix = s.Matrix([[s.prod(X[i]-k for k in range(j)) for j in range(d)] for i in range(d)])
    vand = s.prod(X[j]-X[i] for i in range(d) for j in range(i+1,d))
    zero(matrix.det(method='domain-ge')-vand)
    symbolic_vandermonde_checks += 1

factorial_checks = 0
for d in range(1,6):
    n = d+2
    samples = [list(range(d)), list(reversed(range(d))), [2*i+1 for i in range(d)], [0]*d]
    for xs in samples:
        matrix = s.Matrix([[s.Rational(1,s.factorial(n+xs[i]+1-j)) for j in range(d)] for i in range(d)])
        rhs = s.prod(xs[j]-xs[i] for i in range(d) for j in range(i+1,d))/s.prod(s.factorial(n+x+1) for x in xs)
        zero(matrix.det()-rhs)
        factorial_checks += 1

cofactor_checks = 0
for b in range(1,6):
    high = [[s.Integer(j+2)**(i+1) for j in range(b+1)] for i in range(b-1)]
    e = [s.Integer(1)]*(b+1)
    v = [s.Integer(j+2)**b for j in range(b+1)]
    w = [s.Integer(j+2)**(b+1) for j in range(b+1)]
    DV = s.Matrix(high+[e,v]).det()
    DW = s.Matrix(high+[e,w]).det()
    N = s.Matrix(high+[v,w]).det()
    assert DV != 0 and N != 0
    remaining = high+[v]
    difference = s.Matrix([[row[j+1]-row[j] for j in range(b)] for row in remaining])
    zero(DV-(-1)**(b+1)*difference.det())
    M = s.Matrix(high+[[e[j]+v[j] for j in range(b+1)]])
    B = []
    for j in range(b+1):
        minor = M.copy()
        minor.col_del(j)
        B.append((-1)**(b+j)*minor.det())
    zero(sum(B[j]*e[j] for j in range(b+1))+DV)
    zero(sum(B[j]*w[j] for j in range(b+1))-DW-N)
    cofactor_checks += 3

print(json.dumps({'payload_sha256':actual,'payload_byte_start':len(raw)-len(payload),'file_bytes':len(raw),'whole_file_sha256':hashlib.sha256(raw).hexdigest(),'polynomial_normalization_checks':normalization_checks,'norm_kernel_and_endpoint_checks':kernel_checks,'symbolic_vandermonde_checks':symbolic_vandermonde_checks,'exact_factorial_checks':factorial_checks,'cofactor_sign_checks':cofactor_checks,'all_passed':True,'scope':'Exact finite consistency checks supplement the general audit; they do not verify a leading-term refinement or an arithmetic denominator estimate.'},sort_keys=True))