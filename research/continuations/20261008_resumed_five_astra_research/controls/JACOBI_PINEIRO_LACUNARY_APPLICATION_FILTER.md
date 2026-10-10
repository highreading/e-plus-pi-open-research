> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Jacobi--Pineiro formula: exact application filter

9 October 2026. Primary source inspected: Branquinho, Diaz,
Foulquie-Moreno and Manas, arXiv2310.18294v1.
[Primary HTML](https://arxiv.org/html/2310.18294v1).
Reading scope: definitions(1)--(3), Theorem1/Lemma1 and their displayed
reversal derivation, all Section2 including Theorem2(8) and its proof,
and the displayed Section3 discussion. The nine-page PDF was located
but no additional PDF-specific claim is made. This is not an audit of
every theorem/reference in the paper.

The source gives terminating hypergeometric type-I polynomials for
weights x^alpha_i(1-x)^beta. Its stated AT condition excludes integer
differences among the alpha_i. Type-I conditions test consecutive
ordinary monomials and normalize the last moment. Type-II conditions
use a single ordinary polynomial against several weight families.
These source facts do not establish an inverse for our finite Gram
matrix. [Definitions and Theorem2](https://arxiv.org/html/2310.18294v1#S2).

Scoped current/previous/Desktop English MD/TEX searches, including
the Desktop work archive, find no earlier use of this precise paper
or an evaluated Jacobi--Pineiro transfer for the current gap matrix.
The previously archived FULL A4turn4 Jacobi/Christoffel and Selberg
interface is REUSE, not a new discovery. No original source or
inverse is recomputed here.

## Parent hypothesis analysis in the actual gap space

The old exact interface has

    I={0,...,D-1} union {d,...,m},
    d=D+nu,
    W=span(y^i:i in I), N=dim W=D+m-d+1=m-nu+1,
    w(y)=y^(-1/2)(1-y)^A(z-y), z=(A+71)/3.

The original inverse vector is a polynomial Q in W whose moments
against ALL the same exponents I have prescribed values. An inverse
last-column vector must vanish against I without its last exponent.
Its full finite Gram inverse is not automatically a classical
multiple-orthogonal polynomial.

A tempting two-weight substitution is

    alpha1=-1/2, alpha2=d-1/2, beta=A,
    n1=D, n2=m-d+1.

The integer difference d violates the source's uniform AT hypothesis.
This alone does NOT show that every displayed finite formula fails.
For these particular lengths D<d, the prefactor(-d)_D is nonzero;
the negative-integer hypergeometric denominator(1-d)_l in the first
component is used only through l=D-1<d-1. The other component has
positive denominator(d+1)_l. Consequently, these local terminating
expressions have no pole at this parameter difference. If the
published identity is imported at nearby noninteger parameters,
continuity gives its consecutive-moment identity at the present
finite lengths. This is a parent inference at the stated lengths,
not a claim of AT normality for all multi-indices.

The actual mismatch persists even after this possible continuation.
The resulting type-I combination lies in the gap space, but it is
tested against exponents0,...,N-2. Our last inverse column is tested
against exponents I without m. These two sets have the same size
and DIFFERENT entries: the former fills the gap D,...,d-1 while
omitting some of the highest required exponents. Type-II has the
opposite problem: its testing weights may encode the gap, but its
ordinary polynomial is not constrained to lie in W. Neither direct
substitution solves the required W-by-W finite system.

Also, the source formula has no factor(z-y). A Christoffel transfer
would require explicit finite support, changed multi-indices,
normalization and every ternary divisor before application. It
cannot be silently appended to the formula.

## Usable scope

The source may help a NEW mixed-type or explicit finite transform
construction, but no such construction, compact actual inverse,
uniform ternary valuation, HIGH lift closure, physical endpoint or
primitive denominator bound is established here. A generic
Gauss--Borel factorization or a named multiple polynomial would
still leave the original finite gap and return constraints unpaid.

Continue the current exact source/lift route. Do not assign the
already known Jacobi Gram interface again or import this type-I
formula as an actual inverse without paying the above mismatches.
