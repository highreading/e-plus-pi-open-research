"""Main-authored outward binary fixed-point intervals, standard library only.

Every endpoint is an integer divided by SCALE. No floating operation is
used in any enclosure. This module contains no filesystem or network I/O.
"""
from fractions import Fraction
from math import factorial, isqrt

BITS = 192
SCALE = 1 << BITS


def ceildiv(n, d):
    return -((-n) // d)


class I:
    __slots__ = ('lo', 'hi')

    def __init__(self, lo, hi=None):
        self.lo = lo
        self.hi = lo if hi is None else hi
        assert isinstance(self.lo, int) and isinstance(self.hi, int)
        assert self.lo <= self.hi

    @classmethod
    def integer(cls, n):
        return cls(n * SCALE)

    @classmethod
    def rational(cls, n, d=1):
        assert d > 0
        return cls(n * SCALE // d, ceildiv(n * SCALE, d))

    def __add__(self, other):
        other = as_i(other)
        return I(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-as_i(other))

    def __rsub__(self, other):
        return as_i(other) + (-self)

    def __mul__(self, other):
        other = as_i(other)
        products = [a * b for a in (self.lo, self.hi) for b in (other.lo, other.hi)]
        return I(min(products) // SCALE, ceildiv(max(products), SCALE))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = as_i(other)
        assert other.lo > 0 or other.hi < 0, 'Denominator enclosure includes zero'
        endpoints = [(a * SCALE, b) for a in (self.lo, self.hi) for b in (other.lo, other.hi)]
        return I(min(n // d for n, d in endpoints), max(ceildiv(n, d) for n, d in endpoints))

    def __rtruediv__(self, other):
        return as_i(other) / self

    def __pow__(self, n):
        assert isinstance(n, int)
        if n < 0:
            return I.integer(1) / (self ** (-n))
        result, base = I.integer(1), self
        while n:
            if n & 1:
                result = result * base
            n >>= 1
            if n:
                base = base * base
        return result

    def sqrt(self):
        assert self.lo >= 0
        low = isqrt(self.lo * SCALE)
        high = isqrt(self.hi * SCALE)
        if high * high < self.hi * SCALE:
            high += 1
        return I(low, high)

    def abs_upper(self):
        return I(max(abs(self.lo), abs(self.hi)))

    def upper(self):
        return I(self.hi)

    def widen(self, error):
        error = as_i(error)
        assert error.lo >= 0
        return I(self.lo - error.hi, self.hi + error.hi)

    def exact_json(self):
        return {'lower': str(Fraction(self.lo, SCALE)), 'upper': str(Fraction(self.hi, SCALE))}


def as_i(value):
    if isinstance(value, I):
        return value
    assert isinstance(value, int)
    return I.integer(value)


class C:
    __slots__ = ('real', 'imag')

    def __init__(self, real=0, imag=0):
        self.real, self.imag = as_i(real), as_i(imag)

    def __add__(self, other):
        other = as_c(other)
        return C(self.real + other.real, self.imag + other.imag)

    __radd__ = __add__

    def __neg__(self):
        return C(-self.real, -self.imag)

    def __sub__(self, other):
        return self + (-as_c(other))

    def __rsub__(self, other):
        return as_c(other) + (-self)

    def __mul__(self, other):
        other = as_c(other)
        return C(self.real * other.real - self.imag * other.imag,
                 self.real * other.imag + self.imag * other.real)

    __rmul__ = __mul__

    def __truediv__(self, scalar):
        scalar = as_i(scalar)
        return C(self.real / scalar, self.imag / scalar)

    def conjugate(self):
        return C(self.real, -self.imag)

    def abs_upper(self):
        # The componentwise sum bounds the modulus without a square root.
        return self.real.abs_upper() + self.imag.abs_upper()

    def widen(self, error):
        return C(self.real.widen(error), self.imag.widen(error))

    def exact_json(self):
        return {'real': self.real.exact_json(), 'imag': self.imag.exact_json()}


def as_c(value):
    return value if isinstance(value, C) else C(value)


def atan_rational(q, terms=80):
    """Exact alternating-series enclosure for atan(1/q), q>1."""
    assert q > 1 and terms % 2 == 0
    lower = sum((Fraction((-1) ** j, (2 * j + 1) * q ** (2 * j + 1))
                 for j in range(terms)), Fraction(0))
    upper = lower + Fraction(1, (2 * terms + 1) * q ** (2 * terms + 1))
    return I(I.rational(lower.numerator, lower.denominator).lo,
             I.rational(upper.numerator, upper.denominator).hi)


def pi_interval():
    # Machin identity: pi=16 atan(1/5)-4 atan(1/239).
    return 16 * atan_rational(5) - 4 * atan_rational(239)


def cosine_small(angle, terms=64):
    """Cosine enclosure at |angle|<4 by Taylor and a Lagrange remainder."""
    assert max(abs(angle.lo), abs(angle.hi)) < 4 * SCALE
    square = angle * angle
    term, result = I.integer(1), I.integer(1)
    for j in range(1, terms):
        term = -term * square / ((2 * j - 1) * (2 * j))
        result = result + term
    error = I.rational(4 ** (2 * terms), factorial(2 * terms))
    return result.widen(error)
