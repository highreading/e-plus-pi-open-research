"""Independent exact audit. Actual approximation controls: n=4,6,8,10 only.
Reference polynomials through degree 17 support the saved shifted-minor
transitions; they are not additional canonical approximants.
No author program is imported or executed. Writes remain in agent4.
"""
import hashlib
import itertools
import json
import math
from collections import Counter
from functools import lru_cache
from pathlib import Path
import re
import sympy as s

BASE = Path('work/session_20261001_astra')
OUT = BASE / 'agent4'
OUTPUT_NAMES = {'two_scalar_quotient_independent_checks.json',
                'two_scalar_quotient_independent_stdout.txt'}
COUNTS = Counter()

def check(category, condition):
    COUNTS[category] += 1
    if not bool(condition):
        raise AssertionError(category)

def digest(path):
    if path.is_symlink():
        raise RuntimeError('Symbolic links are outside this audit')
    return hashlib.sha256(path.read_bytes()).hexdigest()

source_names = [
    'agent2/TWO_SCALAR_DETERMINANT_QUOTIENT.md',
    'agent2/TWO_SCALAR_DETERMINANT_QUOTIENT_REPORT.md',
    'agent2/REPORT.md',
    'agent2/check_two_scalar_quotient.py',
    'agent2/two_scalar_quotient_evidence.json',
    'agent2/growing_regime_certificates.json',
    'agent2/ACTUAL_PROJECTION_REMAINDER.md',
    'agent3/BERNSTEIN_DIFFERENCE_CONTINUATION.md',
    'PRIMITIVE_CONDITIONING_LIMITATION.md',
]
protected = {str(BASE / name): digest(BASE / name) for name in source_names}
for path in OUT.iterdir():
    if path.is_file() and path.name not in OUTPUT_NAMES:
        protected[str(path)] = digest(path)

author = json.loads((BASE / 'agent2/two_scalar_quotient_evidence.json').read_text())
frozen = json.loads((BASE / 'agent2/growing_regime_certificates.json').read_text())
check('frozen index domain', [r['n'] for r in author['records']] == [4, 6, 8, 10])
check('frozen index domain', [r['n'] for r in frozen['records']] == [4, 6, 8, 10])
check('source certificate provenance', author['source_sha256'] ==
      digest(BASE / 'agent2/growing_regime_certificates.json'))
check('source certificate provenance', author['checker_sha256'] ==
      digest(BASE / 'agent2/check_two_scalar_quotient.py'))
R = s.Rational

def beta(k):
    return R(k*k, 4*(4*k*k-1)) if k else R(0)

def add(a, b):
    result = [R(0)] * max(len(a), len(b))
    for j, v in enumerate(a):
        result[j] += v
    for j, v in enumerate(b):
        result[j] += v
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result

def scale(a, c):
    return [c*v for v in a]

def multiply(a, b):
    result = [R(0)] * (len(a)+len(b)-1)
    for j, v in enumerate(a):
        for k, w in enumerate(b):
            result[j+k] += v*w
    return result

polys = [[R(1)], [-R(1,2), R(1)]]
for k in range(1, 17):
    polys.append(add(multiply([-R(1,2), R(1)], polys[k]),
                     scale(polys[k-1], beta(k))))

@lru_cache(None)
def moment(k):
    return R(2, 2**k) * sum(R(math.comb(k,j)*(-1)**(j//2), j+1)
                            for j in range(0, k+1, 2))

def functional(p):
    return sum(c*moment(k) for k, c in enumerate(p))

def second_kind(p):
    return sum(c*sum(moment(j) for j in range(k))
               for k, c in enumerate(p))

A = [sum(p) for p in polys]
h = [R(2*(-1)**k, (2*k+1)*math.comb(2*k,k)**2)
     for k in range(len(polys))]
w = [second_kind(p) for p in polys]
for k, p in enumerate(polys):
    check('reference polynomial norm', functional(multiply(p,p)) == h[k])
    check('reference coefficient and endpoint bounds',
          sum(abs(c) for c in p) <= 2**k and A[k] >= R(1,2**k))
    if k:
        check('reference polynomial orthogonality', functional(p) == 0)
        check('reference endpoint ratio', R(1,2) <= A[k]/A[k-1] <= R(2,3))
    if k+1 < len(polys):
        check('reference second-kind determinant',
              A[k]*w[k+1]-A[k+1]*w[k] == h[k])

@lru_cache(None)
def E(k):
    if k < 0:
        raise ValueError('Negative exponential partial-sum index')
    return sum(R(1, math.factorial(j)) for j in range(k+1))

def ell(p, n, j):
    check('factorial functional domain', n+1-j >= 1)
    return sum(c/R(math.factorial(n+k+1-j)) for k,c in enumerate(p))

def tau(p, n, b):
    check('partial-sum domain', n-b >= 0)
    return [sum(c*E(n+k-j) for k,c in enumerate(p)) for j in range(b+1)]

@lru_cache(None)
def Q(k, m):
    if k < 0 or m < 1:
        raise ValueError('Q requires k>=0,m>=1')
    return sum(c/R(math.factorial(m+r)) for r,c in enumerate(polys[k]))

def HH(k, m):
    return Q(k,m)-Q(k,m+1)

def bf(high, x, y):
    return high.col_join(s.Matrix([x,y])).det()

def qstr(x):
    return str(s.cancel(x))

def bracket(N, x, y):
    return (s.Matrix(1, len(x), x)*N*s.Matrix(y))[0]

def derivative_at_one(p, j):
    return sum(c*R(math.factorial(k),math.factorial(k-j))
               for k,c in enumerate(p) if k >= j)

def transform(p, n):
    return [c*R(math.factorial(n),math.factorial(n+k))
            for k,c in enumerate(p)]

def outward(lo, hi, digits=40):
    d = 10**digits
    return [qstr(R(s.floor(lo*d),d)), qstr(R(s.ceiling(hi*d),d))]

def atan_bounds(inv, terms=220):
    low = sum(R((-1)**j, (2*j+1)*inv**(2*j+1)) for j in range(terms))
    return low, low+R(1,(2*terms+1)*inv**(2*terms+1))

a5, b5 = atan_bounds(5)
a239, b239 = atan_bounds(239)
pi_lo, pi_hi = 16*a5-4*b239, 16*b5-4*a239
e_lo = E(300)
e_hi = e_lo+R(1,300*math.factorial(300))
check('independent constant intervals', pi_lo < pi_hi and e_lo < e_hi)

records = []
D_saved = {}
for ar, fr in zip(author['records'], frozen['records']):
    n, b = ar['n'], ar['b']
    check('frozen index domain', b == n//2 == fr['b'])
    dim = b+1
    ones = [R(1)]*dim
    P, U = polys[n], polys[n+1]
    A0, A1, hn = A[n], A[n+1], h[n]
    high = s.Matrix([[ell(polys[n+l],n,j) for j in range(dim)]
                     for l in range(1,b)])
    check('high-row rank', high.rank() == b-1)
    tu, tp = tau(U,n,b), tau(P,n,b)
    z0, z1 = -bf(high,ones,tu), -bf(high,ones,tp)
    check('rational quotient coordinates', z0.is_Rational and z1.is_Rational)

    V = [R(0)]
    Hrat = [R(0)]
    for k in range(n+1):
        V = add(V, scale(polys[k],A[k]/h[k]))
        Hrat = add(Hrat, scale(polys[k],-w[k]/h[k]))
    check('finite-kernel Christoffel-Darboux identity',
          scale(multiply([1,-1],V),hn) == add(scale(P,A1),scale(U,-A0)))
    check('projection remainder rational identity',
          scale(add([R(1)],scale(multiply([1,-1],Hrat),-1)),hn)
          == add(scale(U,-w[n]),scale(P,w[n+1])))
    vrow = [ell(V,n,j) for j in range(dim)]
    # W row = e*ones - pi*vrow + wrat, from the finite projection.
    wrat = [-E(n-j)-ell(Hrat,n,j) for j in range(dim)]
    check('kernel row from two tails',
          vrow == [(A0*tu[j]-A1*tp[j])/hn for j in range(dim)])
    check('projection row from two tails',
          wrat == [(w[n]*tu[j]-w[n+1]*tp[j])/hn for j in range(dim)])
    DV = bf(high,ones,vrow)
    DWrat = bf(high,ones,wrat)
    Trat = bf(high,vrow,wrat)
    check('D_V determinant sign and scale', DV == (A1*z1-A0*z0)/hn)
    check('D_W rational coefficient', DWrat == (-w[n]*z0+w[n+1]*z1)/hn)
    check('T rational coefficient and negative orientation',
          Trat == -bf(high,tu,tp)/hn)
    endpoint_matrix = high.col_join(s.Matrix([[1+x for x in vrow]]))
    Braw = [(-1)**(b+j)*endpoint_matrix[:,[k for k in range(dim) if k != j]].det()
            for j in range(dim)]
    check('cofactor sign and endpoint', sum(Braw) == -DV != 0)
    check('augmented rank and selected kernel',
          endpoint_matrix.rank() == b and endpoint_matrix*s.Matrix(Braw) == s.zeros(b,1))

    clearers = [math.factorial(2*n+2*l) for l in range(1,b)]
    integer_rows = [[high[l,j]*clearers[l] for j in range(dim)] for l in range(b-1)]
    check('integer high-row clearers', all(x.q == 1 for row in integer_rows for x in row))
    contents = [math.gcd(*(int(abs(x)) for x in row)) for row in integer_rows]
    check('positive row contents', all(c > 0 for c in contents))
    R0 = s.Matrix([[x/contents[l] for x in row] for l,row in enumerate(integer_rows)])
    minors = {(i,j): (-1)**(i+j+1)*R0[:,[k for k in range(dim) if k not in (i,j)]].det()
              for i in range(dim) for j in range(i+1,dim)}
    mu = math.gcd(*(int(abs(x)) for x in minors.values()))
    check('positive maximal-minor content', mu > 0)
    N = s.zeros(dim)
    for (i,j), value in minors.items():
        N[i,j], N[j,i] = value/mu, -value/mu
    gamma = R(math.prod(contents)*mu,math.prod(clearers))
    check('positive rational determinant scale', gamma > 0)
    for i,j in minors:
        fi, fj = [R(int(k==i)) for k in range(dim)], [R(int(k==j)) for k in range(dim)]
        check('all basis determinant scales', bf(high,fi,fj) == gamma*N[i,j])
    Z0, Z1 = -bracket(N,ones,tu), -bracket(N,ones,tp)
    K = bracket(N,tu,tp)
    dep = A1*Z1-A0*Z0
    check('primitive contractions and common scale',
          z0 == gamma*Z0 and z1 == gamma*Z1 and DV == gamma*dep/hn)
    check('decomposable primitive alternating form', N.rank() == 2)
    for i,j,k,l in itertools.combinations(range(dim),4):
        check('all coordinate Plucker relations',
              N[i,j]*N[k,l]-N[i,k]*N[j,l]+N[i,l]*N[j,k] == 0)
    kappas = [sum(N[i,j] for i in range(dim)) for j in range(dim)]
    row_sums = [sum(abs(N[j,k]) for k in range(dim)) for j in range(dim)]
    eligible = [j for j in range(dim) if kappas[j] != 0]
    check('conditioning eligibility', len(eligible) > 0)
    C = min(row_sums[j]/abs(kappas[j]) for j in eligible)
    check('conditioning lower bound', C >= 1)
    for j in range(dim):
        fj = [R(int(k==j)) for k in range(dim)]
        check('tail Plucker identity including zero kappa',
              kappas[j]*K == Z1*bracket(N,fj,tu)-Z0*bracket(N,fj,tp))
        check('exponential coefficient of companion Plucker identity',
              kappas[j]*dep == (Z0*A0-Z1*A1)*bracket(N,fj,ones))
    Delta = abs(A1*z1-A0*z0)/(A0*abs(z0)+A1*abs(z1))
    rpi = (w[n+1]*Z1-w[n]*Z0)/dep
    re_comp = -K/dep
    check('rational companion identities', rpi == DWrat/DV and re_comp == Trat/DV)
    quotient = -rpi-re_comp
    pp, qq = int(quotient.p), int(quotient.q)

    fields = {'z0':z0,'z1':z1,'eta':z1/z0,'pole':A0/A1,
              'projective_pole_separation':Delta,'A0':A0,'A1':A1,
              'h_n':hn,'D_V':DV,'common_high_scale_gamma':gamma,
              'rational_pi_companion':rpi,'rational_e_companion':re_comp}
    for key,value in fields.items():
        check('author exact scalar fields', R(ar[key]) == value)
    check('author second-kind fields', list(map(R,ar['second_kind_rational_parts'])) == [w[n],w[n+1]])
    check('author row and minor contents', ar['row_contents'] == contents and ar['minor_content'] == mu)
    authored_minors = {}
    for key,value in ar['primitive_high_minors'].items():
        indices = tuple(map(int,re.findall(r'\d+',key)))
        check('author minor key domain', len(indices) == 2 and indices in minors)
        authored_minors[indices] = R(value)
    check('author primitive minor coefficients', authored_minors == {(i,j):N[i,j] for i,j in minors})
    # Compare every contraction value, independent of the author's label spelling.
    check('author primitive contraction values',
          sorted(map(R,ar['primitive_contractions'].values())) == sorted([Z0,Z1,K,dep]))
    check('author exact sign evidence', z0 < 0 < z1 and Delta == 1 and
          ar['product_sign'] == -1 and ar['sign_condition'] is True)
    check('author fully reduced quotient', (ar['p'],ar['q']) == (pp,qq))

    triple = {key.upper():list(map(R,value)) for key,value in fr['primitive_full_triple'].items()}
    af, bfv, cf = triple['A'], triple['B'], triple['C']
    check('frozen polynomial degree caps', len(af) <= n+1 and len(bfv) <= b+1 and len(cf) <= n+1)
    check('frozen integral primitive triple', all(x.q == 1 for pol in triple.values() for x in pol)
          and math.gcd(*(int(abs(x)) for pol in triple.values() for x in pol)) == 1)
    Xf, Yf = sum(af), sum(bfv)
    check('frozen endpoint matching', Yf == sum(cf) != 0)
    check('frozen endpoint quotient and complete cancellation', Xf/Yf == quotient)
    check('frozen endpoint gcd', math.gcd(int(abs(Xf)),int(abs(Yf))) == fr['endpoint_gcd'])
    check('frozen saved endpoints', Xf == fr['primitive_endpoint_X'] and Yf == fr['primitive_endpoint_Y'])
    check('frozen fully reduced q', (fr['p'],fr['q']) == (pp,qq) and fr['q_digits'] == len(str(qq)))
    check('frozen determinant endpoint', R(fr['D_V']) == DV and R(fr['cofactor_Y']) == -DV)
    check('frozen companion coordinates', R(fr['rational_pi_companion']) == rpi and R(fr['rational_e_companion']) == re_comp)
    Bf = bfv + [R(0)]*(dim-len(bfv))
    check('frozen polynomial versus selected cofactor',
          all(Bf[j]*sum(Braw) == Braw[j]*Yf for j in range(dim)))
    check('frozen high equations and endpoint equation', endpoint_matrix*s.Matrix(Bf) == s.zeros(b,1))
    order = 2*n+b+1
    check('frozen order convention', fr['order_required'] == order)
    # F'(z)=2/(1-z+z^2/2), derived directly from F=4 arctan(z/(2-z)).
    deriv = [R(2),R(2)]
    for k in range(2,order):
        deriv.append(deriv[k-1]-deriv[k-2]/2)
    fseries = [R(0)]+[deriv[k-1]/k for k in range(1,order)]
    for k in range(order):
        value = (af[k] if k < len(af) else 0)
        value += sum(x/R(math.factorial(k-j)) for j,x in enumerate(bfv) if j <= k)
        value += sum(x*fseries[k-j] for j,x in enumerate(cf) if j <= k)
        check('original formal HP residual', value == 0)

    lo, hi = pi_lo+e_lo-rpi-re_comp, pi_hi+e_hi-rpi-re_comp
    check('finite complete evaluated remainder nonzero', lo > 0 or hi < 0)
    saved_interval = list(map(R,fr['integer_form_interval']))
    check('saved and independent integer-form interval consistency',
          saved_interval[0] <= qq*hi and qq*lo <= saved_interval[1])
    check('saved finite nonzero sign consistency',
          (saved_interval[0] > 0 and lo > 0) or (saved_interval[1] < 0 and hi < 0))

    bridge = {}
    rhigh = [transform(multiply([1,-1],polys[n+l]),n) for l in range(1,b)]
    for kval in (n,n+1):
        ak = transform(polys[kval],n)
        wr = s.Matrix([[derivative_at_one(p,j) for j in range(b)]
                       for p in rhigh+[ak]]).det()
        ev = (-1)**(kval+b-1)*wr
        expected_z = z1 if kval == n else z0
        check('endpoint bridge Wronskian sign and scale',
              expected_z == (-1)**(b+1)*wr/R(math.factorial(n)**b))
        bridge[str(kval)] = qstr(ev)
        if n == 6:
            total = R(0)
            coefficient_rows = [p+[R(0)]*(n+b+1-len(p)) for p in rhigh+[ak]]
            for cols in itertools.combinations(range(n+b+1),b):
                vand = math.prod(cols[j]-cols[i] for i in range(b) for j in range(i+1,b))
                inner = R(0)
                for aidx, col in enumerate(cols):
                    hm = s.Matrix([[row[c] for c in cols if c != col]
                                   for row in coefficient_rows[:-1]]).det()
                    inner += (-1)**(b-1+aidx)*hm*coefficient_rows[-1][col]
                total += vand*inner
            check('ordered-minor endpoint bridge at frozen n=6', total == wr)
    check('endpoint bridge D_V formula',
          DV == (A1*R(bridge[str(n)])+A0*R(bridge[str(n+1)]))/R(hn*math.factorial(n)**b))
    if n == 6:
        check('saved bridge E_6', R(bridge['6']) == R(1355870278086451,73150524144312975360000))
        check('saved bridge E_7', R(bridge['7']) == R(181648924564193,70441245472301383680000))

    ds = {}
    for ss in (0,1):
        mat = s.Matrix([[HH(n+l,n-j) for j in range(b)] for l in range(1,b)]
                       + [[Q(n+1-ss,n-j) for j in range(b)]])
        ds[ss] = mat.det()
        check('adjacent-difference determinant orientation',
              (z0 if ss == 0 else z1) == (-1)**(b+1)*ds[ss])
    D_saved[n] = ds
    records.append({'n':n,'b':b,'z0':qstr(z0),'z1':qstr(z1),'Delta':qstr(Delta),
        'A0':qstr(A0),'A1':qstr(A1),'h_n':qstr(hn),
        'second_kind_rational_parts':[qstr(w[n]),qstr(w[n+1])],
        'D_V':qstr(DV),'cofactor_Y':qstr(-DV),
        'row_contents':contents,'minor_content':mu,'gamma_high':qstr(gamma),
        'primitive_high_minors':{str(ij):qstr(N[ij[0],ij[1]]) for ij in minors},
        'primitive_contractions':{'Z0':qstr(Z0),'Z1':qstr(Z1),'K_tail':qstr(K),'d_endpoint':qstr(dep)},
        'author_primitive_contraction_labels':ar['primitive_contractions'],
        'kappa':[qstr(v) for v in kappas],'absolute_row_sums':[qstr(v) for v in row_sums],
        'eligible_coordinates':eligible,'C':qstr(C),
        'C_minimizers':[j for j in eligible if row_sums[j]/abs(kappas[j]) == C],
        'rational_pi_companion':qstr(rpi),'rational_e_companion':qstr(re_comp),
        'p':pp,'q':qq,'q_digits':len(str(qq)),'primitive_endpoint_gcd':fr['endpoint_gcd'],
        'complete_normalized_error_interval':outward(lo,hi),
        'integer_form_interval':outward(qq*lo,qq*hi),
        'interval_scope':'Fresh certified bounds; saved large endpoints checked for overlap and sign, not identical derivation.',
        'bridge_E':bridge,'difference_minors':{str(ss):qstr(value) for ss,value in ds.items()},
        'actual_rank':int(endpoint_matrix.rank()),'all_checks_pass':True})

# Scalar array controls exercise the boundary m=1 as well as saved-domain indices.
for m in (1,2,4,6,8):
    check('Q initial conditions', Q(0,m) == R(1,math.factorial(m)) and
          Q(1,m) == R(1,math.factorial(m+1))-R(1,2*math.factorial(m)))
    check('Q shift with omitted negative index', Q(0,m+1) == Q(1,m)+Q(0,m)/2)
    for k in range(1,16):
        check('factorial-array recurrence', Q(k+1,m) == Q(k,m+1)-Q(k,m)/2+beta(k)*Q(k-1,m))
        check('H recurrence domain k>=1', HH(k,m) == Q(k,m)/2-Q(k+1,m)+beta(k)*Q(k-1,m))
        if k >= 2:
            rhs = (Q(k+2,m)+Q(k+1,m)+(R(1,4)-beta(k+1)-beta(k))*Q(k,m)
                   -beta(k)*Q(k-1,m)+beta(k)*beta(k-1)*Q(k-2,m))
            check('two-shift array formula domain k>=2', Q(k,m+2) == rhs)

transfers = []
for n in (4,6,8):
    b = n//2
    check('enlarged factorial window domain', n-b >= 1)
    size = n+b+6
    J = s.zeros(size)
    for k in range(size):
        J[k,k] = R(1,2)
        if k+1 < size:
            J[k,k+1] = 1
        if k:
            J[k,k-1] = -beta(k)
    baseQ = s.Matrix([[Q(k,n-j) for j in range(b+1)] for k in range(size)])
    for ss in (0,1):
        F = s.zeros(b+1,size)
        for row,k in enumerate(range(n+3,n+b+3)):
            F[row,:] = (s.eye(size)-J)[k,:]
        F[b,n+3-ss] = 1
        left = F*J*J
        value = (left*baseQ).det()
        check('saved shifted-minor transition', value == D_saved[n+2][ss])
        item = {'from_n':n,'to_n':n+2,'s':ss,'determinant':qstr(value),
                'largest_reference_degree':size-1}
        if n == 4:
            support = [j for j in range(size) if any(left[i,j] != 0 for i in range(b+1))]
            total, terms = R(0), 0
            for cols in itertools.combinations(support,b+1):
                a = left[:,list(cols)].det()
                if a:
                    total += a*baseQ[list(cols),:].det()
                    terms += 1
            check('explicit finite Cauchy-Binet expansion at 4->6', total == value)
            item.update({'support':support,'nonzero_left_minor_terms':terms})
        transfers.append(item)

# Formal identities in an arbitrary two-dimensional quotient; no nonzero
# z-coordinate is assumed in these polynomial checks.
e0,e1,a0,a1,c0,c1,f0,f1 = s.symbols('e0 e1 a0 a1 c0 c1 f0 f1')
def wedge(x,y):
    return x[0]*y[1]-x[1]*y[0]
ee, aa, cc, ff = (e0,e1),(a0,a1),(c0,c1),(f0,f1)
plucker = wedge(ee,ff)*wedge(aa,cc)-wedge(ee,aa)*wedge(ff,cc)+wedge(ee,cc)*wedge(ff,aa)
check('universal quotient Plucker identity', s.expand(plucker) == 0)
check('Plucker with zero first coordinate', s.expand(plucker.subs({a0:e0,a1:e1})) == 0)
check('Plucker with zero second coordinate', s.expand(plucker.subs({c0:e0,c1:e1})) == 0)
u0,u1,v0,v1,hs = s.symbols('A0 A1 v0 v1 h', nonzero=True)
coeffdet = s.Matrix([[-u0/hs,u1/hs],[v0/hs,-v1/hs]]).det()
check('formal coefficient determinant orientation', s.expand(hs**2*coeffdet+u1*v0-u0*v1) == 0)

m = s.symbols('m', integer=True, positive=True)
NN = s.Matrix([[0,m,1-m],[-m,0,m],[m-1,-m,0]])
rr = s.Matrix([[m,m-1,m]])
x = s.symbols('x0:3')
y = s.symbols('y0:3')
check('abstract conditioning determinant orientation',
      s.expand(rr.col_join(s.Matrix([x,y])).det()-bracket(NN,x,y)) == 0)
check('abstract conditioning kappa', [sum(NN[i,j] for i in range(3)) for j in range(3)] == [-1,0,1])
check('abstract conditioning rank-two identity', NN.det() == 0 and NN[:2,:2].det() == m*m)
check('abstract conditioning companion', bracket(NN,[1,0,0],[0,0,1]) == 1-m)
abstract = {'domain':'integer m>=2','high_row':['m','m-1','m'],
            'primitivity_certificate':'m-(m-1)=1 for row entries and signed minors',
            'kappa':[-1,0,1],'absolute_row_sums':['2m-1','2m','2m-1'],
            'C':'2m-1','z0':-1,'z1':1,'Delta':1,
            'companion':'(1-m)/(A0+A1), for arbitrary fixed positive A0,A1',
            'scope':'Abstract decomposable primitive forms; not actual HP factorial-tail data.'}
for path, oldhash in protected.items():
    check('protected files unchanged', digest(Path(path)) == oldhash)

result = {'status':'PASS_INDEPENDENT_EXACT_CHECKS',
          'scope':'Actual HP controls exactly n=4,6,8,10; no new canonical solve or prime scan.',
          'construction':'Monic rational recurrence, direct moments, finite kernel and projection, direct determinants, frozen full triples.',
          'reference_polynomial_max_degree':17,
          'reference_degree_scope':'Degrees above the frozen approximation indices only support finite-support shifts and scalar identities.',
          'check_counts':dict(COUNTS),'total_checks':sum(COUNTS.values()),
          'records':records,'shifted_minor_transfers':transfers,
          'abstract_conditioning_example':abstract,
          'source_and_completed_artifact_sha256':protected,
          'all_protected_files_unchanged':True,
          'uncertified':['Unbounded opposite-sign law or quantitative projective separation',
                         'Uniform upper control of C for the actual factorial array',
                         'Adequate asymptotic growth of the fully reduced q',
                         'Full-remainder nonvanishing on an unbounded index sequence',
                         'Agent 1 detailed revised reference estimates',
                         'Bernstein recurrences outside the endpoint bridge in Sections 6-7']}
summary = {'status':result['status'],'actual_indices':[r['n'] for r in records],
           'total_checks':result['total_checks'],
           'q_digits':[r['q_digits'] for r in records],
           'conditioning_C':[r['C'] for r in records],
           'Delta':[r['Delta'] for r in records],
           'all_protected_files_unchanged':True}
(OUT/'two_scalar_quotient_independent_checks.json').write_text(json.dumps(result,indent=2)+'\n')
text = json.dumps(summary,indent=2)+'\n'
(OUT/'two_scalar_quotient_independent_stdout.txt').write_text(text)
print(text,end='')
