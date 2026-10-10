"""Outward interval certificate for one fixed analytic contour phase.

No canonical approximating degree or guessed numerical maximum is used.
The interval leaves cover a rational angular interval exactly. All sign
decisions are made on outward enclosures; bisection only refines a proof.
"""
from fractions import Fraction
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / 'math_packages'))
from mpmath import iv

iv.dps = 60

def exact(q):
    q = Fraction(q)
    return iv.mpf(q.numerator) / q.denominator

def interval(lo, hi):
    left, right = exact(lo), exact(hi)
    return iv.mpf([left.a, right.b])

def complex_sqrt_positive_real(z):
    # On this contour the chosen square root has positive real part.
    # If a wide box does not establish its positive denominator, refine.
    mag = iv.sqrt(z.real**2 + z.imag**2)
    rad = (mag + z.real) / 2
    if not rad.a > 0:
        raise ValueError('Refine square-root box')
    real = iv.sqrt(rad)
    return iv.mpc(real, z.imag/(2*real))

def phase_derivatives(lo, hi):
    u = interval(lo, hi)
    radius = iv.sqrt(iv.mpf(5))/2
    z = iv.mpc(-iv.mpf(1)/2-radius*iv.cos(u), radius*iv.sin(u))
    D = 1+z*z
    w = -1/(z*z)
    S = complex_sqrt_positive_real(1-w+w*w)
    r = 1/(1+S)
    rp = (1-2*w)/(2*S*(1+S)**2)
    hp = 2*z/D-1/z-1/(z-1)+r/z**3
    hpp = 2*(1-z*z)/D**2+1/z**2+1/(z-1)**2-3*r/z**4+2*rp/z**6
    zp = -iv.j*(z+iv.mpf(1)/2)
    zpp = -(z+iv.mpf(1)/2)
    return (hp*zp).real, (hpp*zp*zp+hp*zpp).real

def rational_string(q):
    return f'{q.numerator}/{q.denominator}'

def cover(lo, hi, which, upper, depth=0):
    try:
        enclosure = phase_derivatives(lo, hi)[which]
        passed = bool(enclosure.b < exact(upper).a)
    except (ValueError, ZeroDivisionError):
        passed = False
    if passed:
        leaves.append({
            'lo': rational_string(lo), 'hi': rational_string(hi),
            'derivative_order': which+1,
            'enclosure': str(enclosure),
            'strict_upper_bound': rational_string(Fraction(upper)),
        })
        return
    if depth >= 30:
        raise RuntimeError(f'Certificate failed on {lo}, {hi}')
    middle = (lo+hi)/2
    cover(lo,middle,which,upper,depth+1)
    cover(middle,hi,which,upper,depth+1)

leaves=[]
# The exact symbolic calculation gives F'(0)=0. Negative second
# derivative proves strict descent on this first interval.
cover(Fraction(0),Fraction(1,100),1,Fraction(-1,10))
# The remainder is certified directly by its first derivative.
cover(Fraction(1,100),Fraction(1913,1000),0,Fraction(0))

endpoint_a=iv.mpf(1)/2+iv.sqrt(iv.mpf(5))/2*iv.cos(exact(Fraction(1913,1000)))
assert endpoint_a.a>0 and endpoint_a.b<exact(Fraction(1,8)).a

out={
    'status':'PASS', 'interval_decimal_precision':60,
    'contour':'z(u)=-1/2-(sqrt(5)/2)cos(u)+i(sqrt(5)/2)sin(u)',
    'phase':'log(1+z^2)-log(z)-log(z-1)+(1/2)L(-1/z^2)',
    'certified_middle_angular_interval':['0','1913/1000'],
    'second_derivative_bound_near_saddle':'Fpp < -1/10 on [0,1/100]',
    'first_derivative_bound':'Fp < 0 on [1/100,1913/1000]',
    'endpoint_minus_real_z':str(endpoint_a),
    'endpoint_overlap':'0 < -Re z(1913/1000) < 1/8',
    'leaf_count':len(leaves), 'leaves':leaves,
    'new_canonical_degrees_solved':0,
}
(HERE/'exterior_phase_monotonicity_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='leaves'},indent=2))
