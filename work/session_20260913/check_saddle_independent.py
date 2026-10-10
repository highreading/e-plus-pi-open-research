"""Independent exact saddle checks; no imports from archived certificates.

All signs use outward-rounded dyadic intervals, not floating point.
Polynomial identities use fractions modulo the defining sextic.
Run with Python >=3.10. Writes only this session's result file.
"""
from fractions import Fraction as F
from pathlib import Path
import json

BITS = 192
SCALE = 1 << BITS


class I:
    def __init__(self, lo, hi=None, raw=False):
        hi = lo if hi is None else hi
        if raw:
            self.lo, self.hi = lo, hi
        else:
            lo, hi = F(lo), F(hi)
            self.lo = lo.numerator * SCALE // lo.denominator
            self.hi = -((-hi.numerator * SCALE) // hi.denominator)
        assert self.lo <= self.hi

    @staticmethod
    def cast(a):
        return a if isinstance(a, I) else I(a)

    def __add__(self, other):
        other = I.cast(other)
        return I(self.lo + other.lo, self.hi + other.hi, True)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo, True)

    def __sub__(self, other):
        return self + -I.cast(other)

    def __rsub__(self, other):
        return I.cast(other) + -self

    def __mul__(self, other):
        other = I.cast(other)
        endpoints = [a*b for a in (self.lo,self.hi) for b in (other.lo,other.hi)]
        return I(min(endpoints)//SCALE, -((-max(endpoints))//SCALE), True)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = I.cast(other)
        assert other.lo > 0 or other.hi < 0, 'interval divisor crosses zero'
        return self * I(F(SCALE,other.hi), F(SCALE,other.lo))

    def __pow__(self, n):
        assert isinstance(n,int) and n >= 0
        out = I(1)
        for _ in range(n):
            out = out * self
        return out

    def sign(self):
        assert self.lo > 0 or self.hi < 0, 'sign unresolved'
        return 1 if self.lo > 0 else -1

    def record(self):
        return {'lower_numerator':str(self.lo), 'upper_numerator':str(self.hi),
                'denominator':str(SCALE)}


def add(a,b):
    return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
            for i in range(max(len(a),len(b)))]


def scale(a,c):
    return [x*c for x in a]


def mul(a,b):
    out = [0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j] = out[i+j]+x*y
    return out


def derivative(a):
    return [a[i]*i for i in range(1,len(a))]


def evaluate(a,x):
    out = 0
    for c in reversed(a):
        out = out*x+c
    return out


def remainder(a,b):
    out = a[:]
    while len(out)>=len(b):
        factor = out[-1]/b[-1]
        offset = len(out)-len(b)
        for j in range(len(b)-1):
            out[offset+j] = out[offset+j]-factor*b[j]
        # Leading cancellation is exact algebra, so discard that coefficient.
        out.pop()
    return out


G = list(map(F,[2,1,-55,-20,280,-384,128]))


def red(a):
    out = remainder(list(map(F,a)),G)
    return out+[F(0)]*(6-len(out))


def pmul(a,b):
    return red(mul(a,b))


def cmul(a,b):
    return (red(add(pmul(a[0],b[0]),scale(pmul(a[1],b[1]),-1))),
            red(add(pmul(a[0],b[1]),pmul(a[1],b[0]))))


def cadd(a,b):
    return red(add(a[0],b[0])),red(add(a[1],b[1]))


def cscale(a,c):
    return red(scale(a[0],c)),red(scale(a[1],c))


def ci_mul(a,b):
    return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]


def ci_div(a,b):
    norm=b[0]*b[0]+b[1]*b[1]
    return ((a[0]*b[0]+a[1]*b[1])/norm,
            (a[1]*b[0]-a[0]*b[1])/norm)


def ci_add(a,b):
    return a[0]+b[0],a[1]+b[1]


def ci_scale(a,c):
    return a[0]*c,a[1]*c


def variations(signs):
    return sum(a!=b for a,b in zip(signs,signs[1:]))


def main():
    # Independently form the coordinate polynomials from the report formulas.
    X=scale(mul([1,4],[1,-18,49,-52,16]),F(-1,5))
    Y=scale([5,-11,-67,196,-208,64],F(1,5))
    tau=(red(X),red(Y))
    tau2=cmul(tau,tau)
    tau3=cmul(tau2,tau)
    assert red(add(add(pmul(X,X),pmul(Y,Y)),[0,-1])) == [0]*6
    saddle=cadd(cadd(cscale(tau3,4),cmul((red([6]),red([-1])),tau2)),
                cadd(cmul((red([0]),red([-1])),tau),(red([-1]),red([-1]))))
    assert saddle==([0]*6,[0]*6)

    lo=F(458133387942745,10**15)
    hi=F(458133387942746,10**15)
    assert evaluate(G,lo*lo)>0>evaluate(G,hi*hi)
    alpha=I(lo*lo,hi*hi)
    assert evaluate(derivative(G),alpha).sign()==-1
    radius=I(lo,hi)
    tx,ty=evaluate(X,alpha),evaluate(Y,alpha)
    assert tx.sign()==ty.sign()==1

    # Angular derivative numerator, derived directly from |Psi|^2.
    # q=tan(theta/2), D=-2 R P/(1+q^2)^3.
    R=radius
    A=[(1+2*R)**2,I(0),(1-2*R)**2]
    B=[1+2*R+2*R**2,4*R,1-2*R+2*R**2]
    C=[(1+R)**2,I(0),(1-R)**2]
    P=add(add(mul([0,12],mul(B,C)),
              mul([-3,6,3],mul(A,C))),mul([0,-4],mul(A,B)))
    assert len(P)==7
    chain=[P,derivative(P)]
    while len(chain[-1])>1:
        nxt=scale(remainder(chain[-2],chain[-1]),-1)
        # Positive rational normalization prevents interval-size blowup.
        sign=nxt[-1].sign()
        middle=F(nxt[-1].lo+nxt[-1].hi,2*SCALE)
        nxt=scale(nxt,1/abs(middle))
        assert nxt[-1].sign()==sign
        chain.append(nxt)
    positive=[poly[-1].sign() for poly in chain]
    negative=[s*(-1)**(len(poly)-1) for s,poly in zip(positive,chain)]
    root_count=variations(negative)-variations(positive)
    assert root_count==2
    points=[F(-282),F(-281),F(11,40),F(69,250)]
    point_signs=[evaluate(P,I(q)).sign() for q in points]
    assert point_signs==[1,-1,-1,1]
    half_angle=ty/(radius+tx)
    assert half_angle.lo*SCALE**0 > F(11,40)*SCALE
    assert half_angle.hi < F(69,250)*SCALE

    # Evaluate curvature from the differentiated saddle identity at tau.
    t=(tx,ty)
    t2=ci_mul(t,t)
    sp=ci_add(ci_add(ci_scale(t2,12),ci_mul((12,-2),t)),(0,-1))
    numerator=ci_mul(ci_mul((2,-2),t),sp)
    denominator=ci_mul(ci_mul(ci_add((1,0),t),ci_add((1,0),ci_scale(t,2))),
                       ci_add((1,0),ci_mul((1,-1),t)))
    curvature=ci_div(numerator,denominator)
    assert curvature[0].lo>2*SCALE

    # Direct rational b2/b0, with no use of the report's reduced amplitude.
    t3=ci_mul(t2,t)
    t4=ci_mul(t2,t2)
    polynomial=ci_add(ci_add(ci_scale(t4,4),ci_scale(t3,8)),
                      ci_add(ci_scale(t2,2),ci_add(ci_scale(t,-2),(-1,0))))
    numerator=ci_mul((1,-1),polynomial)
    denominator=ci_scale(ci_mul(ci_mul(t,ci_add((1,0),t)),
                                ci_add((1,0),ci_mul((1,1),t))),32)
    amplitude=ci_div(numerator,denominator)[1]
    assert amplitude.sign()==1
    result={
        'status':'exact_checks_passed',
        'scope':'sextic coordinate/saddle identities, uniform interval Sturm, curvature and amplitude signs',
        'not_checked_here':'Cartier integrality, beta matching, asymptotic proof logic; see separate mathematical audit',
        'precision_bits':BITS,
        'independent_of_archive_code':True,
        'norm_and_saddle_polynomial_remainders_zero':True,
        'selected_radius_bounds':[str(lo),str(hi)],
        'selected_sextic_root_unique_in_interval':True,
        'sturm_degrees':[len(a)-1 for a in chain],
        'sturm_negative_infinity_signs':negative,
        'sturm_positive_infinity_signs':positive,
        'angular_real_root_count':root_count,
        'angular_test_points':[str(q) for q in points],
        'angular_point_signs':point_signs,
        'half_angle':half_angle.record(),
        'curvature_real':curvature[0].record(),
        'amplitude_imaginary':amplitude.record(),
    }
    target=Path(__file__).with_name('saddle_independent_checks.json')
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if not isinstance(v,dict)},indent=2))


if __name__=='__main__':
    main()
