> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Uniform separation of actual prolate nodes from the artificial denominator nodes

Date: 2026-09-13. Original continuation by root. Independent review
`raw_uniform_node_gap_independent_review.md` passes the full proof and
the factor-jet corollaries without correction.

This proves a quantitative strengthening of the strict coprimality used in
`raw_denominator_exceptional_resolvent_bridge.md`. It concerns the true
column nodes and the artificial denominator nodes. It makes no assertion
about separation from the finite row spectrum of K_N.

## 1. A uniform positive offset

Work in the normalized shifted Legendre basis of L²[0,1]. Let L₀ have
eigenvectors e_l and eigenvalues E_l=l(l+1). The actual self-adjoint
prolate operator is

    T=L₀+(3/4)I+W,      Wf(x)=(x−1/2)²f(x).

It has the same operator domain as L₀ and compact resolvent, since W is
bounded and self-adjoint. In quadratic-form order 0≤W≤I/4. Thus its
ordered eigenvalues satisfy ξ_l−3/4∈[E_l,E_l+1/4].

The diagonal of W in this basis is

    w_ll=(1/4){ l²/(4l²−1)+(l+1)²/[4(l+1)²−1] },

where the first term is zero at l=0. Therefore w_00=1/12, and w_ll>1/8
for l≥1; in particular w_ll≥1/12 for every l.

Fix l, set λ=ξ_l−3/4, and let Q=I−e_l e_l*. The compression
A_Q=Q(L₀+W)Q on QL² has domain Q Dom(L₀). Its unperturbed eigenvalues
are exactly the increasing sequence (E_m) with E_l omitted. Min-max and
0≤QWQ≤I/4 place each compressed eigenvalue in the corresponding
interval [E_m,E_m+1/4]. These intervals are at distance at least 7/4
from λ∈[E_l,E_l+1/4]: the smallest unperturbed adjacent gap is 2.
Consequently

    ||(A_Q−λ)⁻¹||≤4/7.

For an eigenvector c e_l+v of L₀+W at λ, the compressed equation is

    (A_Q−λ)v=−c QWe_l.

Here c≠0, because otherwise invertibility would force v=0. Substitute
v=−c(A_Q−λ)⁻¹QWe_l into the e_l component and divide by c. The exact
Schur identity gives

    λ−E_l=w_ll−⟨QWe_l,(A_Q−λ)⁻¹QWe_l⟩.

Since ||QWe_l||≤||W||≤1/4, the absolute value of the correction is at
most (1/16)(4/7)=1/28. Hence, for every l≥0,

    ξ_l≥l(l+1)+3/4+1/21.                         (1)

No numerical eigenvalue information or perturbation-series remainder is
used here. The existing upper bound ξ_l≤l(l+1)+1 suffices below.

## 2. Uniform separation from every integer plus 3/4

Write ξ_l=E_l+3/4+δ_l, where 1/21≤δ_l≤1/4. For any integer k, if
k=E_l then |k+3/4−ξ_l|=δ_l≥1/21. If k≠E_l, the distance is at least
1−δ_l≥3/4. Thus

    |k+3/4−ξ_l|≥1/21     for every integer k and l≥0.       (2)

In particular this applies to the actual artificial nodes
x_j=2n+3/4+3n·2^j. It quantitatively proves that both actual parity node
polynomials are units modulo the artificial denominator, without an
uncontrolled approach to a true node as n grows.

## 3. A useful reciprocal-distance estimate

Let x=k+3/4>0 with k an integer, and consider any subset of the true
nodes. The complete sum obeys an absolute uniform bound

    Σ_{l≥0} 1/|x−ξ_l| ≤ C,                       (3)

where C is independent of k≥0. Here is an elementary proof. The at most
two indices with |k−E_l|<2 contribute at most 42 by (2). For all other
indices, |x−ξ_l|≥|k−E_l|−1/4≥(7/8)|k−E_l|. Put t≥0 such that
t(t+1)=k. Then |k−E_l|=|t−l|(t+l+1). If t<2, summing the tail
O(1/l²) gives an absolute bound, with finitely many initial terms handled
by (2). If t≥2, split into l<t/2, t/2≤l≤2t+2, and l>2t+2.
The outer sums are O(1/t). In the middle sum, all but the at most two
indices nearest t have |t−l| bounded below by consecutive positive
half-integers and t+l+1≥t, giving O(log(t+2)/t). Handle those nearest
indices directly using (2). This proves (3). The same bound holds for
either parity or a finite node subset.

For a finite node polynomial V(z)=∏_{l∈I}(z−ξ_l), normalize at such x:
v_x(z)=V(z)/V(x). On |z−x|≤1/42, every ratio
(z−ξ_l)/(x−ξ_l) lies within 1/2 of 1, so the convergent local logarithms
and (3) yield

    |v_x(z)|+|v_x(z)⁻¹|≤C₁.                      (4)

The constants are independent of x and of the chosen finite subset I.
Cauchy's coefficient bound therefore gives, for any radius parameter h>0,

    |[u^r] V(x+hu)/V(x)|,
    |[u^r] V(x)/V(x+hu)| ≤ C₁(42h)^r.           (5)

The inverse on the second line means its Taylor series at u=0. It is
used only through finite order; it is not asserted analytic on |u|≤1
when h is large. The associated ν-by-ν triangular Taylor multiplication
matrix and its exact inverse have norm at most

    C₁ ν max{1,42h}^{ν−1}.                       (6)

For the actual h_j=√x_j log(2n)/2=O(n log n) and ν=O(√n), this is
exp(O(√n log n)). Thus multiplication by a true low factor, high factor,
or full parity factor in local confluent coordinates has a proved
subexponential condition bound after retaining its actual scalar value
V(x_j). Separate scalar values at different nodes are not equated or
discarded. This estimate does not remove the energy projection in the
exceptional Schur problem.
