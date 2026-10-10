> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Mano–Tsuda: applicability to the actual raw family

Date: 2026-09-13. Focused primary-source review and independent
fixed-degree confluence calculation. No asymptotic theorem is imported.

## 1. Primary-source facts

Toshiyuki Mano and Teruhisa Tsuda, *Hermite–Padé approximation,
isomonodromic deformation and hypergeometric integral*,
[arXiv:1502.06695v2](https://arxiv.org/pdf/1502.06695v2), revised final
version dated March 29, 2016; arXiv v2 posted April 30, 2016.
Read Sections 1–3, especially equations (1.1)–(1.2), Theorems 1.3 and
1.6, Proposition 2.1, and Theorem 3.2.

Theorem 1.6 constructs an exponent-shifting polynomial gauge for a
Fuchsian system. Section 1.4 assumes no integer exponent differences
at zero and infinity. The underlying dual approximation identity is
algebraic. Section 2.1 explicitly assumes full rank of its modified
neighboring approximation matrices. Determinant formulas use their
normalizing minors. Section 3.1 divides by current nonzero constant
terms. Theorem 3.2 asserts formal approximation order, not an endpoint
error or arithmetic-height estimate. The reviewed statements provide
no large-degree bound for these minors.

## 2. Exact comparison with the project equation

The following calculation is independent of the cited theorem. Put
D=1+z^2, F=arctan z, and

    G(z) = [[1,0,0], [exp(z),exp(z),0], [F(z),0,1]].

Direct multiplication gives

    G' G^(-1) = diag(0,1,0) + E_(3,1)/D.

The actual scalar fundamental matrix is a rational left gauge of this
base matrix, as proved in the degree-transfer note. Its exponential
branch at infinity is explicit. The other two branches form a Laurent
plane. At the origin the scalar equation has integer exponents, and
at the logarithmic points it has the resonances already handled by the
finite-jet proof. Thus the literal hypotheses of the cited Fuchsian
theorem are not the hypotheses of the actual scalar family.

This does not invalidate its algebraic method. Formal-series
elimination and determinant identities can still be derived directly.
What must be checked afresh is the actual index pattern, normalization,
and nonvanishing of every divisor used by an algorithm. Our raw degree-n
Taylor space has dimension two before endpoint normalization. A unique
row normalized by B_n(1)=1, C_n(1)=4 is selected from that space. It is
not automatically one of the differently indexed neighboring rows in
the cited construction.

Likewise F(0)=0 obstructs the unmodified first constant-term division.
Replacing F by 1+F removes that first obstruction by an invertible
constant change of basis, but says nothing about later pivots. The
proved rank of the actual endpoint-matched system does not imply full
rank of every other neighboring approximation matrix.

The existing unconditional scalar-state construction already proves
existence of the actual next normalized row without those extra pivot
assumptions. A new coordinate system is useful only if it gives a
quantitative bound, a simpler proved recurrence, or an exact arithmetic
factorization absent from that construction.

## 3. A proved fixed-degree Fuchsian confluence

For a complex parameter epsilon near zero define the analytic germ

    g_epsilon(z) = (1-epsilon z)^(-1/epsilon),
    g_0(z) = exp(z),

using its power series at zero. Its coefficients are exactly

    [z^k] g_epsilon(z)
       = (1/k!) product_(j=0)^(k-1) (1+j epsilon).

They are polynomials in epsilon. Moreover

    g_epsilon'/g_epsilon = 1/(1-epsilon z).

Replacing both exponential entries of G by g_epsilon gives

    G_epsilon' G_epsilon^(-1)
       = diag(0,1/(1-epsilon z),0)+E_(3,1)/D.

For epsilon nonzero, this matrix has only simple finite poles and is
O(1/z) at infinity. Thus it is a Fuchsian system, with repeated zero
exponents still present; this observation alone does not remove the
separate nonresonance qualification in the cited theorem.

Fix n. Form the square system for the polynomial triple
(A_(n,epsilon),B_(n,epsilon),C_(n,epsilon)) of degrees at most n by
requiring

    A_(n,epsilon)+B_(n,epsilon) g_epsilon
       +C_(n,epsilon) arctan z = O(z^(3n+1)),
    B_(n,epsilon)(1)=1,  C_(n,epsilon)(1)=4.

There are 3n+3 coefficients and 3n+3 equations. Its matrix M_n(epsilon)
has entries polynomial in epsilon, by the displayed coefficient
formula. The actual all-index rank theorem says det M_n(0) is nonzero.
Consequently M_n(epsilon)^(-1) is analytic in some neighborhood of
epsilon=0, and all normalized coefficients are analytic there. They
converge to the actual raw coefficients as epsilon tends to zero.

The neighborhood may depend on n. This is a proved fixed-n
continuation, with no claimed uniform neighborhood and no interchange
of n tending to infinity with epsilon tending to zero. At epsilon=1/m
with integer m, g_epsilon is rational; such a specialization is not an
exact linear form in 1,e,pi and cannot replace the epsilon=0 arithmetic
problem.

## 4. One concrete quantitative target

Let M_n be the exact square matrix just defined, including the actual
two endpoint rows. A precise sufficient conditioning lemma would be
an explicit sequence eta_n>0, with a useful polynomial lower scale,
for which

    sup_(|epsilon|<=eta_n)
      ||M_n(0)^(-1)(M_n(epsilon)-M_n(0))|| <= 1/2.

It would imply a zero-free determinant disk and a controlled inverse
there by the geometric-series identity. This is an honest missing
lemma, not a consequence of constant monodromy or a determinant
representation. It must be combined with an independently proved
uniform estimate in the perturbed system to transfer asymptotics.

Even the input coefficient scale illustrates the issue. For k<=3n,

    |product_j(1+j epsilon)-1|
       <= exp(|epsilon| k(k-1)/2)-1.

Thus epsilon=o(n^(-2)) makes those finitely many relative coefficient
perturbations small. That entrywise observation does not control the
displayed inverse-weighted perturbation: cancellation in M_n(0) may
amplify it. The needed inverse estimate is closely related to the
existing actual constrained-polynomial norm problem, rather than a
known bypass of it.

## 5. Priority and scope

The primary paper supplies a useful structural precedent and possible
alternative coordinates. The direct fixed-degree confluence above is
rigorous. At present neither supplies determinant lower bounds,
primitive denominator control, or a uniform estimate for the actual
endpoint remainder. The immediate priority remains a quantitative
estimate on the already proved actual finite-state orbit or its
equivalent constrained polynomial system; a confluent reformulation
should be promoted only after it provides one of those estimates.
