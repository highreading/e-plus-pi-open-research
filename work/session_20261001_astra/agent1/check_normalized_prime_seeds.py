"""Complete normalized b=2 seeds for exactly 5,7,11,13.
Two exact constructions; no HP nullspace construction or degree search.
Finite checks supplement the separately written transfer proof.
"""
import json
from functools import lru_cache
from pathlib import Path
import sympy as s

BASE = Path('work/session_20261001_astra/agent1')
PRIMES = (5, 7, 11, 13)
x = s.symbols('x')

@lru_cache(None)
def coeffs(n):
    poly = s.Poly(s.expand((1-x+x*x/2)**n), x)
    return tuple(poly.nth(j) for j in range(2*n+1))

def falling(n, j):
    if j > n:
        return s.Integer(0)
    return s.factorial(n)/s.factorial(n-j)

@lru_cache(None)
def exp_integer(j):
    if j == 0:
        return s.Integer(1)
    return j*exp_integer(j-1)+1

def normalize(n, h, u, v, A, B):
    t = n+1
    J = n*h+u
    a = -n*h+n*u+v/2
    k = (1-n)*h+(n-1)*u+v
    ell = (-n*n+3*n+2)*h+(n*n-2*n-1)*u+n*v
    sigma = t*k*k-a*ell
    omega = k*J-ell*h
    C = (t*k-a)*J-t*(ell-k)*h
    Vtilde = sigma*A-C*B-a*omega
    fields = ('h','u','v','J','Acal','Bcal','a','k','ell','sigma','C','omega','Vtilde')
    values = (h,u,v,J,A,B,a,k,ell,sigma,C,omega,Vtilde)
    return {key:s.cancel(value) for key,value in zip(fields,values)}

@lru_cache(None)
def tail_construction(n):
    co = coeffs(n)
    h,u,v = [sum((falling(n,j+d)*co[j] for j in range(max(0,n-d+1))),s.Integer(0)) for d in range(3)]
    A = sum((falling(n,j)*co[j]*exp_integer(2*n-j) for j in range(n+1)),s.Integer(0))
    B = 2*exp_integer(2*n+1)+sum((falling(n,j-1)*(2*n+2-j)*coeffs(n+1)[j]*exp_integer(2*n+1-j) for j in range(1,n+2)),s.Integer(0))
    return normalize(n,h,u,v,A,B)

@lru_cache(None)
def legendre(n):
    if n == 0:
        return s.Poly(1,x)
    if n == 1:
        return s.Poly(4*x-2,x)
    expr = (2*(2*n-1)*(2*x-1)*legendre(n-1).as_expr()+4*(n-1)*legendre(n-2).as_expr())/n
    poly = s.Poly(s.expand(expr),x)
    assert all(c.is_Integer for c in poly.all_coeffs())
    return poly

def fscale(n):
    return s.Rational(2**n,s.factorial(n)**2)

def factorial_functional(k,d):
    poly = legendre(k)
    return sum((poly.nth(j)/s.factorial(k+j-d) for j in range(k+1) if k+j>=d),s.Integer(0))

def T(n,k):
    poly = legendre(k)
    return sum((poly.nth(j)*exp_integer(n+j)/s.factorial(n+j) for j in range(k+1)),s.Integer(0))

def second_kind(k):
    if k == 0:
        return s.Integer(0)
    poly = legendre(k)
    quotient,remainder = s.div(poly,s.Poly(x-1,x))
    assert remainder.as_expr() == poly.eval(1)
    def moment(j):
        return sum((s.binomial(j,a)*(-1)**(a//2)*s.Rational(2,a+1) for a in range(0,j+1,2)),s.Integer(0))/2**j
    return s.cancel(sum((quotient.nth(j)*moment(j) for j in range(k)),s.Integer(0)))

@lru_cache(None)
def direct_construction(n):
    t = n+1
    f = fscale(n)
    h,J,K = [s.cancel(factorial_functional(n,d)/f) for d in range(3)]
    u = J-n*h
    v = K-n*(n-1)*h-2*n*u
    a,Jp,Kp = [s.cancel(factorial_functional(n+1,d)/fscale(n+1)) for d in range(3)]
    tp,tu = T(n,n),T(n,n+1)
    A,B = s.cancel(tp/f),s.cancel(t*tu/(2*f))
    S = Jp**2-a*Kp
    W = Jp*J-Kp*h
    C = (Jp-a)*J-(Kp-Jp)*h
    sigma,omega = s.cancel(S/t),s.cancel(W/t)
    V = S*A-t*C*B-a*W
    Vtilde = s.cancel(V/t)
    result = dict(zip(('h','u','v','J','Acal','Bcal','a','k','ell','sigma','C','omega','Vtilde'),(h,u,v,J,A,B,a,s.cancel(Jp/t),s.cancel(Kp/t),sigma,C,omega,Vtilde)))
    assert result == tail_construction(n), (n,result,tail_construction(n))
    pn,pu = legendre(n).eval(1),legendre(n+1).eval(1)
    wp,wu = second_kind(n),second_kind(n+1)
    Xoriginal = 2*(wp+tp)*S-t*t*(wu+tu)*C-2*f*a*W
    Doriginal = t*t*pu*C-2*pn*S
    Qtilde = 2*wp*sigma-t*wu*C
    Dtilde = t*pu*C-2*pn*sigma
    Xnormalized = Qtilde+2*f*Vtilde
    assert s.cancel(Xoriginal-t*Xnormalized)==0
    assert s.cancel(Doriginal-t*Dtilde)==0
    assert s.cancel(V-t*Vtilde)==0
    # Check source formula (5) independently using its rational minors.
    # The source HP domain is n>=2; smaller indices are only scalar seeds.
    if n >= 2:
        def ell(k,j):
            poly = legendre(k)
            return sum((poly.nth(i)/s.factorial(n+i+1-j) for i in range(k+1)),s.Integer(0))
        a0,a1,a2 = [ell(n+1,j) for j in range(3)]
        r1,r2 = ell(n,1),ell(n,2)
        Sm = a1*a1-a0*a2
        Cm = (a1-a0)*r2-(a2-a1)*r1
        Wm = a1*r2-a2*r1
        G = s.Rational((-1)**n*2**(2*n+3),t)
        assert s.cancel(pn*wu-pu*wp-G)==0
        Xendpoint = ((wp+tp)*Sm-(wu+tu)*Cm-a0*Wm)/G
        Yendpoint = (pu*Cm-pn*Sm)/G
        assert s.cancel(Xendpoint*Dtilde-Yendpoint*Xnormalized)==0
        if Dtilde != 0:
            assert Yendpoint != 0
            assert s.cancel(Xendpoint/Yendpoint-Xnormalized/Dtilde)==0
    extra = {'V_original':V,'P_n':pn,'P_next':pu,'Qtilde':Qtilde,'Dtilde':Dtilde,'Xcal_original':Xoriginal,'Dcal_original':Doriginal}
    return result,extra

# Formal polynomial verification does not specialize an index or a state.
n,h,u,v,A,B,wp,wu,pn,pu,f = s.symbols('n h u v A B wp wu pn pu f')
t = n+1
state = normalize(n,h,u,v,A,B)
a,J = state['a'],state['J']
up = t*(h-u+v/2)
vp = t*(n*h+u-(n+2)*v/2)
Jp = t*a+up
Kp = n*t*a+2*t*up+vp
S = Jp**2-a*Kp
W = Jp*J-Kp*h
C = (Jp-a)*J-(Kp-Jp)*h
Q = 2*wp*state['sigma']-t*wu*state['C']
Dn = t*pu*state['C']-2*pn*state['sigma']
Xold = 2*(wp+f*A)*S-t*t*(wu+2*f*B/t)*C-2*f*a*W
Dold = t*t*pu*C-2*pn*S
formal = {
    'J_factor':s.expand(Jp-t*state['k'])==0,
    'K_factor':s.expand(Kp-t*state['ell'])==0,
    'S_factor':s.expand(S-t*state['sigma'])==0,
    'W_factor':s.expand(W-t*state['omega'])==0,
    'C_identity':s.expand(C-state['C'])==0,
    'V_factor':s.expand(S*A-t*C*B-a*W-t*state['Vtilde'])==0,
    'full_numerator_factor':s.cancel(Xold-t*(Q+2*f*state['Vtilde']))==0,
    'denominator_factor':s.expand(Dold-t*Dn)==0,
}
assert all(formal.values()),formal

def mod(value,p):
    value = s.Rational(value)
    return int(value.p)%p*pow(int(value.q)%p,-1,p)%p

def serialized(mapping):
    return {key:str(s.cancel(value)) for key,value in mapping.items()}

exact_rows = []
for r in range(max(PRIMES)):
    direct,extra = direct_construction(r)
    for value in direct.values():
        denominator = int(s.denom(value))
        assert denominator > 0 and denominator & (denominator-1) == 0
    exact_rows.append({'r':r,'state':serialized(direct),'endpoint_scalars':serialized(extra),'two_exact_constructions_agree':True,'original_endpoint_identity_checked':r>=2})

prime_rows = []
for p in PRIMES:
    rows = []
    for r in range(p):
        direct,extra = direct_construction(r)
        tail = tail_construction(r)
        residues = {key:mod(value,p) for key,value in direct.items()}
        assert residues == {key:mod(value,p) for key,value in tail.items()}
        rows.append({'r':r,**residues,'Dtilde_P_next_coefficient':((r+1)*residues['C'])%p,'Dtilde_P_n_coefficient':(-2*residues['sigma'])%p,'P_n_seed':mod(extra['P_n'],p),'P_next_seed':mod(extra['P_next'],p)})
    vector = [row['Vtilde'] for row in rows]
    prime_rows.append({'p':p,'Vtilde_residues':vector,'zero_residues':[r for r,value in enumerate(vector) if value==0],'uniform_unit_seeds':all(vector),'rows':rows})

certificate = {
    'status':'PASS',
    'scope':'Exactly primes 5,7,11,13 and their 36 residue entries. Two exact constructions at the 13 distinct scalar seeds r=0,...,12; adjacent Legendre data only as needed. No HP nullspace construction, prime search, or additional degree sampling.',
    'independent_researcher_review':False,
    'formal_identities':formal,
    'exact_seed_rows':exact_rows,
    'prime_certificates':prime_rows,
    'limits':'Finite seed arithmetic does not prove lifts or endpoint nonvanishing. All-index consequences require the separate transfer and second-kind separation proofs.'
}
output = BASE/'normalized_prime_seed_certificate.json'
output.write_text(json.dumps(certificate,indent=2)+'\n')
assert json.loads(output.read_text()) == certificate
print(json.dumps({'status':'PASS','formal_identities':formal,'seeds':[{'p':item['p'],'Vtilde_residues':item['Vtilde_residues'],'zero_residues':item['zero_residues'],'uniform_unit_seeds':item['uniform_unit_seeds']} for item in prime_rows],'zero_rows':[{'p':item['p'],**row} for item in prime_rows for row in item['rows'] if row['Vtilde']==0],'certificate':str(output)},indent=2))
