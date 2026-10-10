> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the uniform true/artificial node gap and factor jets

Date: 2026-09-13. Reviewer: audit_results.

Reviewed raw_uniform_true_artificial_node_gap.md in full.
**Verdict: PASS.** The operator compression, uniform 1/21 offset,
reciprocal-distance sum and local factor-jet estimates all check.
No correction is required.

## 1. Self-adjoint compression and the Schur identity

The Legendre operator L0 is self-adjoint with eigenbasis e_l,
eigenvalues E_l=l(l+1) and compact resolvent. Multiplication
by (x-1/2)^2 is bounded self-adjoint, with 0<=W<=I/4.
Thus L0+W is self-adjoint on D(L0), has compact resolvent,
and min-max puts lambda_l=xi_l-3/4 in [E_l,E_l+1/4].

For Q=I-e_l e_l*, the projection preserves D(L0) and reduces
L0, since e_l is an eigenvector. The compressed operator is
the self-adjoint restriction of L0 to QH plus the bounded
perturbation QWQ, on D(L0) intersect QH=Q D(L0). It has
compact resolvent. Its unperturbed eigenvalues are exactly
the original increasing list with E_l removed.

Min-max applies to this entire compressed operator and places
each of its eigenvalues in [E_m,E_m+1/4], m!=l, in that order.
The nearest possible unperturbed gap is two, so every such
interval is at distance at least 7/4 from lambda_l. This
justifies the bounded compressed resolvent on the full infinite
complement, not merely a finite matrix approximation.

The e_l component of an actual eigenvector cannot vanish, or
the compressed equation and this invertibility would make
the whole eigenvector zero. Solving its complementary component
therefore yields the exact Schur identity. The resolvent is
not assumed positive: the correction is bounded in absolute
value by ||QWe_l||^2 times its operator norm, at most 1/28.

The stated W diagonal follows from the normalized Legendre
multiplication coefficients. At l=0 it equals 1/12. At l>=1
each of its two terms exceeds 1/16, so it exceeds 1/8.
Therefore the uniform lower bound is

    lambda_l-E_l>=1/12-1/28=1/21.

This proof neither invokes an asymptotic perturbation expansion
nor transfers a finite-compression eigenvalue claim to an
unbounded operator without a domain argument.

## 2. Every integer-plus-3/4 node is uniformly separated

Write xi_l=E_l+3/4+delta_l, with 1/21<=delta_l<=1/4.
At the lattice point E_l+3/4 the distance is delta_l. At
every other lattice point it is at least 1-delta_l>=3/4.
This proves the claimed 1/21 separation uniformly in both
indices. Actual denominator nodes belong to this lattice.

The statement concerns the true column nodes. It does not
assert a gap between them and any finite row-matrix spectrum.
If the nodes are divided by N^2, the corresponding separation
is 1/(21N^2); the unscaled gap should not be copied unchanged
into a scaled coordinate.

## 3. Uniform reciprocal-distance sum

There are at most two indices with |k-E_l|<2; their contribution
is bounded using the gap. For the other indices,
|x-xi_l|>=(7/8)|k-E_l| follows from delta_l<=1/4.

With t(t+1)=k, factor |k-E_l|=|t-l|(t+l+1). For t>=2,
the ranges l<t/2 and l>2t+2 each contribute O(1/t), by
respectively counting O(t) terms of size O(t^-2) and summing
a quadratic tail. In the middle, remove the at most two
closest indices to t and use the uniform gap for them. The
remaining distances grow at least like consecutive half-integers,
giving O(log(t+2)/t). This is uniformly bounded. If t<2,
only finitely many initial indices require the gap, and the
remaining tail is O(sum l^-2). Thus (3) is uniform in every
nonnegative integer k and in every finite or parity subset.

## 4. Factor ratios and exact finite jet multiplication

On |z-x|<=1/42, each relative factor differs from one by
at most one half. The local logarithms are analytic there,
and |log(1+u)|<=2|u| bounds their total by the uniform
reciprocal-distance sum times 2|z-x|. Both the normalized
polynomial and its reciprocal consequently have a bound
independent of its degree and of the chosen true-node subset.

Cauchy's coefficient estimate on that fixed disk gives
C1(42h)^r after substitution z=x+hu. There is no missing
factorial, because these are Taylor coefficients. The inverse
series is used locally; no analyticity on the larger unit
u-disk is claimed when h is large.

The truncated lower Toeplitz operator and its exact inverse
have norm at most the sums of the respective first nu
coefficient bounds. This yields

    C1 nu max(1,42h)^(nu-1)

for each, uniformly in multiplicity. At the actual radii
h=O(n log n) and nu=O(sqrt n), the logarithm is
O(sqrt n log n). This applies equally to low, high and full
parity factors, since constant signs cancel in their normalized
ratios.

The scalar values V(x_j) at distinct nodes remain separate
and can vary substantially. The uniform normalized jet bound
does not equate them, and it does not remove the energy or
retained-space projections from the exceptional Schur problem.
