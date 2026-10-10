"""Independent b=2 audit at exactly 3, 7, 11; no canonical HP solve.

Writes only a new certificate in Agent 4's directory. Original programs
are inspected as sources, never imported or executed by this checker.
"""
from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha256
from math import comb, factorial
from pathlib import Path
import json
import sympy as sp

BASE = Path('work/session_20261001_astra')
OUT = BASE / 'agent4'
PRIMES = (3, 7, 11)
LAST_SEED = 10
FIELDS = ('h', 'u', 'v', 'J', 'Acal', 'Bcal', 'a', 'k', 'ell',
          'sigma', 'C', 'omega', 'Vtilde')


def normalized_formula(n, h, u, v, ac, bc):
    t = n + 1
    j = n*h + u
    a = -n*h + n*u + F(1, 2)*v
    k = (1-n)*h + (n-1)*u + v
    ell = (-n*n+3*n+2)*h + (n*n-2*n-1)*u + n*v
    sigma = t*k*k - a*ell
    omega = k*j - ell*h
    c = (t*k-a)*j - t*(ell-k)*h
    vt = sigma*ac - c*bc - a*omega
    return dict(zip(FIELDS, (h, u, v, j, ac, bc, a, k, ell,
                             sigma, c, omega, vt)))


def formal_checks():
    n,h,u,v,ac,bc,wp,wu,pn,pu,f = sp.symbols(
        'n h u v ac bc wp wu pn pu f')
    t = n + 1
    state = normalized_formula(n,h,u,v,ac,bc)
    a,j = state['a'],state['J']
    up = t*(h-u+v/2)
    vp = t*(n*h+u-(n+2)*v/2)
    jp = t*a+up
    kp = t*(t-1)*a+2*t*up+vp
    old_s = jp**2-a*kp
    old_w = jp*j-kp*h
    old_c = (jp-a)*j-(kp-jp)*h
    old_v = old_s*ac-t*old_c*bc-a*old_w
    qt = 2*wp*state['sigma']-t*wu*state['C']
    dt = t*pu*state['C']-2*pn*state['sigma']
    old_x = (2*(wp+f*ac)*old_s
             -t*t*(wu+2*f*bc/t)*old_c-2*f*a*old_w)
    old_d = t*t*pu*old_c-2*pn*old_s
    differences = {
        'J_factor': jp-t*state['k'],
        'K_factor': kp-t*state['ell'],
        'S_factor': old_s-t*state['sigma'],
        'W_factor': old_w-t*state['omega'],
        'C_identity': old_c-state['C'],
        'V_factor': old_v-t*state['Vtilde'],
        'complete_numerator_factor': old_x-t*(qt+2*f*state['Vtilde']),
        'denominator_factor': old_d-t*dt,
    }
    transition = sp.Matrix([
        [-n,n,sp.Rational(1,2)],
        [t,-t,t/2],
        [n*t,t,-t*(n+2)/2],
    ])
    differences['transition_determinant_identity_only'] = (
        transition.det()-t**4/2)
    x = sp.symbols('x')
    hx = sp.Function('H')(x)
    adjacent_first = t*(hx-sp.diff(hx,x)+sp.diff(hx,x,2)/2)
    adjacent_zero = (x*sp.diff(hx,x,2)/2
                     +(t-x)*(sp.diff(hx,x)-hx))
    ode = (x*sp.diff(hx,x,3)+(n+2-2*x)*sp.diff(hx,x,2)
           +2*(x-1)*sp.diff(hx,x)-2*n*hx)
    differences['ODE_from_adjacent_identities'] = (
        2*(sp.diff(adjacent_zero,x)-adjacent_first)-ode)

    # Reconstruct the original endpoint determinants with independent scalars.
    a0,a1,a2,r1,r2,tp,tu = sp.symbols('a0 a1 a2 r1 r2 tp tu')
    gdet = pn*wu-pu*wp
    avec = [a0,a1,a2]
    tuvec = [tu,tu-a1,tu-a1-a2]
    tpvec = [tp,tp-r1,tp-r1-r2]
    tvec = [(pn*z-pu*w)/gdet for z,w in zip(tuvec,tpvec)]
    xvec = [(wp*z-wu*w)/gdet for z,w in zip(tuvec,tpvec)]
    yraw = sp.Matrix([avec,[1+z for z in tvec],[1,1,1]]).det()
    xraw = sp.Matrix([avec,[1+z for z in tvec],xvec]).det()
    sm = a1*a1-a0*a2
    cm = (a1-a0)*r2-(a2-a1)*r1
    wm = a1*r2-a2*r1
    differences['original_endpoint_Y_determinant'] = (
        yraw-(pu*cm-pn*sm)/gdet)
    differences['original_endpoint_X_determinant'] = (
        xraw-((wp+tp)*sm-(wu+tu)*cm-a0*wm)/gdet)

    # Check the exact scale between rational minors and integer transforms.
    g = 2*f/t**2
    small_s,small_c,small_w = g*g*old_s,g*f*old_c,g*f*old_w
    scaled_y = (pu*small_c-pn*small_s)/gdet
    scaled_x = ((wp+f*ac)*small_s-(wu+2*f*bc/t)*small_c
                -g*a*small_w)/gdet
    prefactor = g*f/(gdet*t*t)
    differences['original_endpoint_Y_scale'] = scaled_y-prefactor*old_d
    differences['original_endpoint_X_scale'] = scaled_x-prefactor*old_x
    results = {key:sp.cancel(value)==0 for key,value in differences.items()}
    assert all(results.values()), ('formal identity failure',results)
    return results


def falling(n,j):
    assert n >= 0 and j >= 0
    return 0 if j > n else factorial(n)//factorial(n-j)


@lru_cache(None)
def phi_coefficient(k,s):
    # Trinomial coefficient formula, with all divisions performed over Q.
    if s < 0 or s > 2*k:
        return F(0)
    total = F(0)
    for c in range(max(0,s-k),s//2+1):
        b = s-2*c
        total += F((-1)**b*comb(k,c)*comb(k-c,b),2**c)
    return total


@lru_cache(None)
def h_polynomial(k):
    coefficients = [F(0)]*(k+1)
    for s in range(k+1):
        coefficients[k-s] = falling(k,s)*phi_coefficient(k,s)
    assert all(c.denominator == 1 for c in coefficients)
    return tuple(coefficients)


def h_derivative(k,d):
    return sum((falling(j,d)*c for j,c in enumerate(h_polynomial(k))),F(0))


@lru_cache(None)
def partial_exponential(d):
    assert d >= 0
    return sum((F(1,factorial(j)) for j in range(d+1)),F(0))


@lru_cache(None)
def d_integer(d):
    # Direct finite sum, independent of the author's D recurrence.
    return sum(factorial(d)//factorial(j) for j in range(d+1))


def coefficient_construction(n):
    h,u,v = [h_derivative(n,d) for d in range(3)]
    ac = sum((falling(n,s)*phi_coefficient(n,s)*d_integer(2*n-s)
              for s in range(n+1)),F(0))
    bc = 2*d_integer(2*n+1)+sum((
        falling(n,s-1)*(2*n+2-s)*phi_coefficient(n+1,s)
        *d_integer(2*n+1-s) for s in range(1,n+2)),F(0))
    return normalized_formula(n,h,u,v,ac,bc)


@lru_cache(None)
def legendre_coefficients(k):
    # Explicit transformed ordinary Legendre expansion, not its recurrence.
    coefficients = [0]*(k+1)
    for j in range(k//2+1):
        degree = k-2*j
        denominator = factorial(j)*factorial(k-j)*factorial(degree)
        multiplier,remainder = divmod(factorial(2*k-2*j),denominator)
        assert remainder == 0
        for i in range(degree+1):
            coefficients[i] += (multiplier*comb(degree,i)*2**i
                                *(-1)**(degree-i))
    return tuple(coefficients)


def fscale(k):
    return F(2**k,factorial(k)**2)


def transformed_derivative(k,d):
    return sum((F(c,factorial(k+j-d))
                for j,c in enumerate(legendre_coefficients(k))
                if k+j >= d),F(0))/fscale(k)


def t_functional(n,k,j=0):
    return sum((c*partial_exponential(n+i-j)
                for i,c in enumerate(legendre_coefficients(k))),F(0))


def ell_functional(n,k,j):
    return sum((F(c,factorial(n+i+1-j))
                for i,c in enumerate(legendre_coefficients(k))),F(0))


@lru_cache(None)
def moment(j):
    # Integrate the binomial expansion along (1+i*u)/2, u in [-1,1].
    return sum((F(2*comb(j,a)*(-1)**(a//2),2**j*(a+1))
                for a in range(0,j+1,2)),F(0))


@lru_cache(None)
def second_kind(k):
    coefficients = legendre_coefficients(k)
    # (L_k(t)-L_k(1))/(t-1) has coefficient sum_{j>i} [t^j] L_k.
    return sum((sum(coefficients[i+1:])*moment(i)
                for i in range(k)),F(0))


def cross(a,b):
    return [a[1]*b[2]-a[2]*b[1],
            a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0]]


def direct_construction(n):
    t,f = n+1,fscale(n)
    h,j,kk = [transformed_derivative(n,d) for d in range(3)]
    u = j-n*h
    v = kk-n*(n-1)*h-2*n*u
    a,jp,kp = [transformed_derivative(n+1,d) for d in range(3)]
    tp,tu = t_functional(n,n),t_functional(n,n+1)
    ac,bc = tp/f,t*tu/(2*f)
    old_s = jp*jp-a*kp
    old_w = jp*j-kp*h
    c = (jp-a)*j-(kp-jp)*h
    old_v = old_s*ac-t*c*bc-a*old_w
    # These divisions are over Q, including every boundary seed n=p-1.
    sigma,omega,vt = old_s/t,old_w/t,old_v/t
    state = dict(zip(FIELDS,(h,u,v,j,ac,bc,a,jp/t,kp/t,
                             sigma,c,omega,vt)))
    pn,pu = sum(legendre_coefficients(n)),sum(legendre_coefficients(n+1))
    wp,wu = second_kind(n),second_kind(n+1)
    gdet = F((-1)**n*2**(2*n+3),t)
    assert pn*wu-pu*wp == gdet, ('Wronskian',n)
    qt = 2*wp*sigma-t*wu*c
    dt = t*pu*c-2*pn*sigma
    xnorm = qt+2*f*vt
    old_x = 2*(wp+tp)*old_s-t*t*(wu+tu)*c-2*f*a*old_w
    old_d = t*t*pu*c-2*pn*old_s
    assert old_x == t*xnorm and old_d == t*dt
    assert old_v == t*vt
    extras = {'V_original':old_v,'P_n':F(pn),'P_next':F(pu),
              'Qtilde':qt,'Dtilde':dt,'Xcal_original':old_x,
              'Dcal_original':old_d}
    control = None
    if n >= 2:
        avec = [ell_functional(n,n+1,d) for d in range(3)]
        tvec,xvec = [],[]
        for d in range(3):
            tud,tpd = t_functional(n,n+1,d),t_functional(n,n,d)
            tvec.append((pn*tud-pu*tpd)/gdet)
            xvec.append((wp*tud-wu*tpd)/gdet)
        bvec = cross(avec,[1+z for z in tvec])
        raw_y = sum(bvec,F(0))
        raw_x = sum((b*z for b,z in zip(bvec,xvec)),F(0))
        assert raw_y == F((-1)**n,4*t*t*factorial(n)**4)*dt, ('Y scale',n)
        assert raw_x*dt == raw_y*xnorm, ('full raw quotient',n)
        if dt:
            quotient = xnorm/dt
            assert raw_y != 0 and raw_x/raw_y == quotient
            control = {'n':n,'raw_Y':str(raw_y),'rational_endpoint':str(quotient),
                       'reduced_q':str(quotient.denominator)}
    return state,extras,control


def valuation(value,p):
    value = F(value)
    assert value != 0, ('valuation of zero requested',p)
    def integer_value(k):
        k = abs(k)
        answer = 0
        while k%p == 0:
            k //= p
            answer += 1
        return answer
    return integer_value(value.numerator)-integer_value(value.denominator)


def floor_log(value,p):
    power,answer = 1,0
    while power*p <= value:
        power *= p
        answer += 1
    return answer


def reduce_mod(value,p):
    value = F(value)
    assert value.denominator%p != 0
    return value.numerator*pow(value.denominator,-1,p)%p


def serialize(mapping):
    return {key:str(F(value)) for key,value in mapping.items()}


def main():
    root_path = BASE/'B2_COMMON_FACTOR_TERNARY_CHECKS.json'
    author_path = BASE/'agent1/normalized_prime_seed_certificate.json'
    protected = [root_path,author_path,BASE/'check_b2_common_factor_ternary.py',
                 BASE/'agent1/check_normalized_prime_seeds.py']
    protected += [OUT/name for name in (
        'B1_WHOLE_FAMILY_REVIEW.md','INHERITED_SYNTHESIS_REVIEW.md',
        'DRAFT_OBSERVATIONS_REVIEW.md','check_whole_family.py',
        'whole_family_checks.json','whole_family_check_stdout.txt',
        'check_inherited_rates_counts.py','audit_rate_count_certificate.json',
        'audit_rate_count_stdout.txt')]
    hashes = {str(path):sha256(path.read_bytes()).hexdigest() for path in protected}
    root = json.loads(root_path.read_text())
    author = json.loads(author_path.read_text())
    assert root['checker_sha256'] == hashes[str(BASE/'check_b2_common_factor_ternary.py')]
    formal = formal_checks()
    author_exact = {row['r']:row for row in author['exact_seed_rows']}
    root_exact = {row['r']:row for row in root['seed_rows']}
    author_primes = {row['p']:row for row in author['prime_certificates']}
    states,extras,controls = [],[],[]
    exact_output = []
    for n in range(LAST_SEED+1):
        tail = coefficient_construction(n)
        direct,extra,control = direct_construction(n)
        assert tail == direct, ('independent constructions',n,tail,direct)
        for key,value in direct.items():
            assert value == F(author_exact[n]['state'][key]), ('saved state',n,key)
            denominator = F(value).denominator
            assert denominator > 0 and denominator & (denominator-1) == 0
        for key,value in extra.items():
            assert value == F(author_exact[n]['endpoint_scalars'][key]), ('saved endpoint',n,key)
        assert direct['v'].denominator == 1 and direct['v'].numerator%2 == 0
        assert direct['a'] == h_derivative(n+1,0)
        assert F(n+1)*(direct['h']-direct['u']+direct['v']/2) == h_derivative(n+1,1)
        assert F(n+1)*(n*direct['h']+direct['u']-(n+2)*direct['v']/2) == h_derivative(n+1,2)
        if n < 3:
            for key in root['seed_fields']:
                assert direct[key] == F(root_exact[n][key]), ('main ternary state',n,key)
            assert extra['V_original'] == root_exact[n]['unnormalized_V']
        states.append(direct)
        extras.append(extra)
        if control is not None:
            controls.append(control)
        exact_output.append({'r':n,'state':serialize(direct),
                             'endpoint_scalars':serialize(extra)})

    # Independent finite confirmation of the second-kind normalization.
    for k in range(LAST_SEED+2):
        convolution = 8*sum((F(sum(legendre_coefficients(j-1))
                                 *sum(legendre_coefficients(k-j)),j)
                             for j in range(1,k+1)),F(0))
        assert convolution == second_kind(k), ('second-kind convolution',k)

    residue_records = []
    for p in PRIMES:
        rows = []
        for r in range(p):
            row = {'r':r,**{key:reduce_mod(value,p) for key,value in states[r].items()}}
            row.update({
                'Dtilde_P_next_coefficient':(r+1)*row['C']%p,
                'Dtilde_P_n_coefficient':-2*row['sigma']%p,
                'P_n_seed':reduce_mod(extras[r]['P_n'],p),
                'P_next_seed':reduce_mod(extras[r]['P_next'],p),
            })
            if p in (7,11):
                assert row == author_primes[p]['rows'][r], ('saved modular row',p,r)
            rows.append(row)
        vector = [row['Vtilde'] for row in rows]
        assert all(vector), ('normalized zero seed',p,vector)
        if p in (7,11):
            assert vector == author_primes[p]['Vtilde_residues']
            assert author_primes[p]['zero_residues'] == []
        else:
            assert vector == [1,1,1] == root['Vtilde_mod_3']
        residue_records.append({'p':p,'Vtilde_residues':vector,'zero_residues':[],
                                'rows':rows})

    pm,pnext = sp.symbols('P_m P_next')
    endpoint_pairs = [(pm,2*pm),(2*pm,2*pm),(2*pm,pnext)]
    ternary_targets = [2*pm,sp.Integer(0),pm]
    for r,((p0,p1),target) in enumerate(zip(endpoint_pairs,ternary_targets)):
        expr = (r+1)*p1*int(states[r]['C'])-2*p0*int(states[r]['sigma'])
        assert sp.Poly(expr-target,pm,pnext,modulus=3).is_zero
    assert [sum(legendre_coefficients(k))%3 for k in range(3)] == [1,2,2]

    finite_valuations = []
    boundary_controls = []
    for p in PRIMES:
        for n in range(p,LAST_SEED+1):
            fvp = valuation(factorial(n),p)
            ell = floor_log(n+1,p)
            assert 2*fvp > ell
            qt,dt = extras[n]['Qtilde'],extras[n]['Dtilde']
            if qt:
                assert valuation(qt,p) >= -ell
            xnorm = qt+2*fscale(n)*states[n]['Vtilde']
            assert valuation(xnorm,p) == -2*fvp
            if dt:
                q = (xnorm/dt).denominator
                observed = valuation(q,p)
                predicted = 2*fvp+valuation(dt,p)
                assert observed == predicted >= 2*fvp
                finite_valuations.append({'p':p,'n':n,'v_p_q':observed,
                                          'formula_value':predicted})
        n = p-1
        xnorm = extras[n]['Qtilde']+2*fscale(n)*states[n]['Vtilde']
        assert extras[n]['Dtilde'] != 0
        q = (xnorm/extras[n]['Dtilde']).denominator
        assert valuation(q,p) == 0, ('inherited n=p-1 consistency',p)
        boundary_controls.append({'p':p,'scalar_seed':n,'v_p_q':0,
                                  'factorial_separation_not_assumed':True})

    rate_source = json.loads((BASE/'B2_RATE_COMPARISONS.json').read_text())
    r = F(3,2)
    comparisons = {
        'seven_exceeds_three_halves_cubed':F(7)>r**3,
        'eleven_exceeds_three_halves_fifth':F(11)>r**5,
        'sqrt_two_below_three_halves_by_squaring':F(2)<r*r,
        'ratio_is_27_over_25':(3*r*r)/(1+r)**2 == F(27,25),
    }
    assert all(comparisons.values())
    assert comparisons == rate_source['comparisons']
    assert rate_source['finite_prime_set'] == list(PRIMES)
    assert [F(2,p-1) for p in PRIMES] == [F(1),F(1,3),F(1,5)]
    assert F(27-25,27) == F(2,27)
    assert F(1,25) > F(1,27)
    rate = {
        'exact_comparisons':comparisons,
        'seven_power_margin':str(F(7)-r**3),
        'eleven_power_margin':str(F(11)-r**5),
        'square_root_squared_margin':str(r*r-2),
        'lower_W_comparison_base':str(3*r*r),
        'upper_tau_comparison_base':str((1+r)**2),
        'ratio':str(F(27,25)),
        'integral_interval':[25,27],
        'integral_constant_lower_bound':str(F(2,27)),
        'strictness_proof':'On [25,27), 1/x > 1/27; integration gives log(27/25) > 2/27.',
        'numerical_logarithms_used':False,
    }
    assert all(sha256(Path(path).read_bytes()).hexdigest()==digest
               for path,digest in hashes.items()), 'An input or b=1 artifact changed.'
    result = {
        'status':'PASS_INDEPENDENT_EXACT_CHECKS',
        'scope':'Only complete scalar seeds at p=3,7,11 and their existing endpoint controls. Infinite conclusions require the separate proof audit.',
        'formal_identities':formal,
        'distinct_scalar_seeds':LAST_SEED+1,
        'complete_residue_row_count':sum(PRIMES),
        'state_coordinate_count_per_row':len(FIELDS),
        'author_7_11_modular_rows_matched':18,
        'ternary_exact_Vtilde':[int(states[r]['Vtilde']) for r in range(3)],
        'exact_seed_rows':exact_output,
        'prime_certificates':residue_records,
        'ternary_Dtilde_residues':['2 P_m','0','P_m'],
        'raw_endpoint_controls':controls,
        'finite_actual_denominator_checks':finite_valuations,
        'prime_boundary_consistency_controls':boundary_controls,
        'rate_argument':rate,
        'input_and_preserved_b1_sha256':hashes,
        'input_and_b1_artifacts_unchanged':True,
        'prime_5_lifting_audited':False,
        'prime_13_certified':False,
        'new_canonical_HP_solve':False,
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    destination = OUT/'b2_whole_family_checks.json'
    destination.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    summary = {
        'status':result['status'],
        'formal_identity_count':len(formal),
        'distinct_scalar_seeds':result['distinct_scalar_seeds'],
        'complete_residue_row_count':result['complete_residue_row_count'],
        'ternary_exact_Vtilde':result['ternary_exact_Vtilde'],
        'vectors':{str(row['p']):row['Vtilde_residues'] for row in residue_records},
        'finite_actual_denominator_checks':len(finite_valuations),
        'raw_endpoint_controls':len(controls),
        'rate_inputs_verified':all(comparisons.values()),
        'input_and_b1_artifacts_unchanged':True,
        'prime_13_certified':False,
        'certificate':str(destination),
    }
    print(json.dumps(summary,indent=2))


if __name__ == '__main__':
    main()
