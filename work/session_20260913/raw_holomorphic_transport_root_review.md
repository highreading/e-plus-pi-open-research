> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of holomorphic normalized transport

Date: 2026-09-13. Root verification of
`raw_holomorphic_normalized_transport.md`.

**Verdict: the complex extension, ordered-product bounds, and
uniform parameter derivative estimates pass.**

The principal roots of c and c+1 lie in the sector with arguments
between -pi/4 and pi/4 on Re c>0. Their sum is nonzero in that
sector, and the product of their sum and difference is one.
Thus q,m,lambda and the displayed logarithm are holomorphic with
the stated branches. The equation q+q^(-1)=4c+2 excludes any
unit-circle crossing in this connected domain; comparison with
the positive axis proves |q|<1 everywhere in it.

The geometric vector solves the half-line resolvent equation in
the complex domain and is square summable there. On a compact
set, its weighted Hilbert norm is bounded using absolute squares
of q and m. The finite parity-block coefficient error and the
resolvent distance bound therefore give a locally uniform complex
O(1/N) estimate. No identification of a complex bilinear square
with a norm is made. The opposite-parity perturbation is bounded
by the ordinary complex resolvent identity.

The resulting boundary matrix equals m(c)I/16+O(1/N).
The positive minimum of |m(c)| on the compact set justifies
inversion by a norm estimate. This is the required replacement
for a real quadratic-form lower bound. Alternatively its Hermitian
real part is positive to the right of the finite real spectrum.
The normalization of the transfer by the nonzero lambda(c) and
the stated error constant are correct.

Enlarging the compact parameter set by a fixed positive distance
and by scale factors in [1/4,1] retains a compact subset of the
right half-plane. Hence the same estimates hold at every cut
from n to m<=2n, not only at the final cut. Summation of the
step-two reciprocal bounds controls the ordered product and its
inverse. In particular no commutation of factors and no vanishing
of the accumulated error is assumed.

Matrix-valued Cauchy estimates on the fixed larger domain give
exactly the first and second derivative bounds stated. The
relative-change estimate follows by integrating the derivative
along a segment and multiplying by the inverse bound. The second
derivative factorial cancels the Taylor remainder factor 1/2.
The conversion from chi derivatives to x derivatives correctly
supplies n^(-2r).

The logarithm of the exact scalar product and the continuum
integral use the same holomorphic branches. A step-two Riemann
sum leaves a bounded holomorphic error on the larger compact
set, so its derivatives are controlled by the same Cauchy
argument. Exponentiating retains bounded norm and inverse.

The branch matrices used in the exact quotient are invertible
because Re(chi n^2) exceeds the finite row spectral upper bound
for all cuts under consideration and sufficiently large n.
The theorem correctly leaves the separate initial matrix
P_n(chi n^2), its parameter dependence, and the selected high-row
multi-node determinant unresolved.
