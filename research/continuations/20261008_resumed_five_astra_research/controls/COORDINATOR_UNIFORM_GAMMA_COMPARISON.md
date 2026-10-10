> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Uniform Gamma comparison and the compact rational-error rate

Coordinator derivation, 8 October 2026. Status: a complete proposed proof for
independent mathematical review. It is not a proof deciding e+pi. The actual
primitive gcd and denominator remain unchanged and uncontrolled.

## 1. Reused objects and the scoped overlap gate

Use the EXACT compact H_k, moments, clearers, negative atom, and primitive p_k,q_k
defined in A4turn20. Put s0=e+pi. Its accepted identities are

    (-1)^k H_k(s0) = Lambda_k^k J_k^nu D_k,
    (-1)^k H_(1,k) = Lambda_k^k J_(k-1)^+ S_k,
    eps_k = s0-p_k/q_k = R_k D_k/S_k,
    R_k = J_k^nu/J_(k-1)^+ = 1/K_(k-1)^nu(-1,-1).

Here D_k is the FULL conditioned determinant, including overlap and negative
atom; S_k is the FULL extracted slope, including overlap. Neither is a new
integer normalization. Set

    Z_k = det((2k+2i+2j)!)_(0<=i,j<k),
    M_0 = ((2k+2i+2j)!),
    M_-1 = ((2k-2+2i+2j)!).

The old proof compares the exterior contribution by shifting every Gamma
variable by1, losing an extra e^(-k). It also uses2^k in the slope upper bound.
The present application instead controls M_-1 RELATIVELY to M_0. A scoped
archive search found the old scaled-interval comparison, classical Laguerre
and Gershgorin/positive-quadrature arguments, but no completed constant-factor
comparison for these same two compact determinants. Reuse of those classical
tools is explicit; global novelty is not asserted.

The standard recurrence/orthogonality and Gaussian rule are described in
[NIST DLMF18.9](https://dlmf.nist.gov/18.9) and
[NIST DLMF3.5](https://dlmf.nist.gov/3.5). The application and inequalities below
are derived here. Fresh primary queries also located Laguerre Markov-norm
papers; those are background, not an imported theorem settling this target.

## 2. An inverse-square Gamma norm bound with the physical boundary retained

For k>=2 let alpha=2k-2 and N=2k-1. Gaussian quadrature for

    w_alpha(t) dt = t^alpha exp(-t) dt, t>0,

has N positive nodes and weights. Its nodes are eigenvalues of the Laguerre
Jacobi matrix, with diagonals2i+alpha+1 (0<=i<N) and off-diagonals
sqrt(j(j+alpha)) (1<=j<N).

We first prove every node is >=(k-1)/3. For a>0 and 0<=b<=a,

    sqrt(a^2-b^2) <= a-b^2/(2a).

For an interior Jacobi row i<=N-2=2k-3, take a_i=i+k-1 and b=k-1.
Its diagonal equals a_i+a_(i+1), and the two off-diagonal magnitudes are
sqrt(a_i^2-b^2), sqrt(a_(i+1)^2-b^2). At i=0 the first is0. The Gershgorin
lower endpoint is therefore at least

    (k-1)^2/2 * (1/a_i+1/a_(i+1))
    >= (k-1)^2/(3k-3) = (k-1)/3.

The final row has only one off-diagonal. Bounding it by i+alpha/2 gives the
larger lower endpoint3k-2. Thus all nodes t_j meet the claimed bound.

For ANY real polynomial P of degree<=2k-2=N-1, quadrature is exact for P^2.
It is also a LOWER bound for the integral of t^2 P^2, whose degree is<=2N.
To verify the latter without an analytic quadrature-error hypothesis: subtract
the nonnegative leading coefficient times the square of the monic degree-N
orthogonal polynomial. The remainder has degree<=2N-1, is exactly integrated,
and that orthogonal polynomial vanishes at every node. The error is its
positive squared norm times that leading coefficient.

Consequently,

    integral P(t)^2 t^(2k-2)e^(-t) dt
    <= 9/(k-1)^2 * integral P(t)^2 t^(2k)e^(-t) dt.       (2.1)

Apply (2.1) to P(t)=p(t^2), deg(p)<=k-1. It gives the Loewner inequality

    0 <= M_-1 <= c_k M_0, c_k=9/(k-1)^2.                (2.2)

Boundary audit: the largest weighted polynomial degree in the denominator is
(2k-2)+2N=6k-4, EXACTLY the original maximal factorial. The quadrature's exact
degree is2N-1; its required base moments end one degree earlier. The degree2N
comparison uses the SAME available maximal moment and a nonnegative norm.
No original successor moment, extra physical row, or corrected charge is added.

## 3. Constant-factor exterior comparisons

For t>=1, Bernoulli's inequality gives

    (t^2-1)^k >= t^(2k)-k t^(2k-2).

For 0<t<1 the right side is nonpositive, while an exterior-only integral has
zero contribution. Therefore, for every p of degree<=k-1,

    integral_(t>1) p(t^2)^2 (t^2-1)^k e^(-t)dt
    >= p^T(M_0-k M_-1)p.

Set gamma_k=k c_k=9k/(k-1)^2. For k>=64 it is<1. The exterior conditioned
weight prod_(j=1)^k(x-y_j), with0<=y_j<=1, is between(x-1)^k and x^k
on x>1. The EXACT exterior density becomes e^(-1)e^(-t)dt under x=t^2.
It follows, uniformly in every conditioning tuple y, that the exterior Gram
determinant is between

    e^(-k)(1-gamma_k)^k Z_k and e^(-k) Z_k.             (3.1)

The same lower bound applies to the slope exterior weight

    (x+1) prod_(j=1)^(k-1)(x-y_j) >= (x-1)^k.

Its upper weight is at most(x+1)x^(k-1), so its exterior determinant is at most

    e^(-k) det(M_0+M_-1)
    <= e^(-k)(1+c_k)^k Z_k.                            (3.2)

This replaces the previous2^k upper factor. All these are relative matrix
comparisons before determinants are taken.

For k>=64,

    k gamma_k/(1-gamma_k)
      =9k^2/(k^2-11k+1) <=11,
    gamma_k <=1/6.

The first inequality is equivalent to2k^2-121k+11>=0; at64 its value is459,
and it increases thereafter. The second follows from k^2-56k+1>=0.
Thus log(1-gamma)>=-gamma/(1-gamma) gives

    (1-gamma_k)^k >= e^(-11),
    (1+c_k)^k <= e^(gamma_k) <= e^(1/6) <3/2.          (3.3)

Integrating the uniform conditional bounds over the normalized compact
Vandermonde measures preserves them. Every density factor e^(-1) is retained:
the determinants have e^(-k), not e^(-1).

## 4. Full overlap and negative-atom payments

Let C_k=binom(4k-1,2k-2)/(2k)! be the accepted coefficient-functional bound,
z_k=(e-e^(-1))C_k, and b_k=e 8^k C_k/4. A4turn20's COMPLETE expansion gives

    |D_k-exterior_k| <= e^(-k) Z_k d_k,
    d_k = exp(z_k)(1+b_k)-1,

including the entire negative atom, and gives for the extracted slope

    |S_k-slope_exterior_k| <= e^(-k) Z_k d_k^+,
    d_k^+ = 2^k(exp(z_k)-1).

The accepted factorial cutoff proves, for every k>=64,

    e^k d_k <=2*4^(-k),
    e^k d_k^+ <=2*4^(-k).

In particular both d_k,d_k^+ are<=2*4^(-k). This is at most e^(-11)/2:
it suffices to check4*3^11<4^64, using e<3, and the left side is fixed.
Thus every overlap and atom is paid, with no appeal to unsigned substitution.

Combining Sections3 and4 gives the COMPLETE comparison

    (1/2)e^(-k-11) Z_k <= D_k <=2e^(-k) Z_k,
    (1/2)e^(-k-11) Z_k <= S_k <=2e^(-k) Z_k.            (4.1)

It uses the same original integer H and its actual slope.

## 5. Proposed uniform error theorem

The e^(-k) factors cancel between numerator and slope. Therefore (4.1) implies

    (e^(-11)/4) R_k <= eps_k <=4e^11 R_k, k>=64.       (5.1)

Use the ALREADY accepted Christoffel estimates from A4turn20, with
A=(3+2sqrt(2))^2=17+12sqrt(2):

    3/(2k^2 A^(k-1)) <= R_k <=28/A^(k-1).

They yield

    3/(8e^11 k^2 A^(k-1)) <= eps_k
       <=112e^11/A^(k-1), k>=64.                      (5.2)

In particular the exact logarithmic ordinary-error rate would be

    lim_(k->infinity) -log(eps_k)/k = log(A).           (5.3)

This would replace the previous exponential-rate window by a single rate.
The constants are deliberately conservative; optimality is not claimed.

After the ACTUAL primitive reduction, the whole error remains q_k eps_k.
A sufficient condition is now q_k=o(A^(k-1)), while a necessary condition is
q_k=o(k^2 A^(k-1)). Neither is proved. In particular q_k=o(33^(k-1)) would be
a rational-base sufficient condition because A>33. No new divisor of G_k is
provided by this analytic theorem, and the previous raw leading4 remains.

## 6. A fixed-stride ordering consequence requiring no neighboring gcd guess

The Christoffel variational formula gives R_(k+1)<=R_k/9: multiply a minimizing
polynomial p, p(-1)=1, by (1-2x)/3. Its degree increases by1, it still evaluates
to1 at-1, and its absolute factor on[0,1] is<=1/3.

Using (5.1), for EVERY k>=64,

    eps_(k+13)/eps_k
       <=16e^22/9^13 <16/81 <1/2.                    (6.1)

Thus the actual rational zeros satisfy p_(k+13)/q_(k+13)>p_k/q_k on each of
the13 infinite ladders. The primitive integer cross difference is positive.
Rational separation and (5.2) give

    q_k q_(k+13) >= A^(k-1)/(112e^11),
    limsup_(k->infinity) log(q_k)/k >= (1/2)log(A).     (6.2)

These lower bounds remain too weak to prove primitive divergence; no bounded
cross difference or bounded adjacent denominator ratio is assumed. They also
do not prove one-step ordering. The original sparse index progression retains
its previous distinct scope.

## 7. Review obligations

Independently check the Jacobi lower endpoint, the degree2N positive Gaussian
error, the Loewner and Bernoulli directions, all exterior density factors,
normalization of D_k/S_k, use of the complete accepted overlap/atom bounds,
uniform k>=64 cutoff, exact-rate deduction and fixed-stride consequence.
If any step fails, retain the valid inverse-square or exterior lemma at its
correct scope and identify the missing bridge. The final denominator/gcd
problem and the rationality of e+pi remain unresolved.

## 8. A correlated comparison: strengthening the proposed theorem

The separate constants above can be improved by correlating the SAME exterior
integrals before comparing determinants. The following avoids importing a
determinantal-process coupling theorem. Its tools are the already accepted
Christoffel variational identity, positive exterior weights and relative matrices.
No completed same-pencil adjacent contraction was located in the scoped prior
archive; that contraction is explicitly open in A5turn14. The classical identity
itself is reused.

For x_1,...,x_k>1 put P_x(y)=prod_i(x_i-y). For any positive compact measure m
whose degree-(k-1) moment matrix is positive definite,
write R_k(m)=J_k(m)/J_(k-1)((1+y)^2 m). It is the SAME degree-(k-1) normalized
polynomial minimum used above. Pointwise on[0,1],

    prod_i(x_i-1) <= P_x(y) <= prod_i x_i.

Monotonicity of the polynomial minimum therefore gives

    prod_i(x_i-1) R_k(nu) <= R_k(P_x nu)
       <= prod_i x_i R_k(nu).                          (8.1)

Let mathcal_D_ext, mathcal_S_ext be the positive exterior raw determinants,
before division by J_k(nu), J_(k-1)^+ respectively. Directly integrate the compact
variables in the EXACT two-measure formula:

    mathcal_D_ext = (1/k!) integral V(x)^2 J_k(P_x nu) dmu_ext^k(x),
    mathcal_S_ext = (1/k!) integral V(x)^2 prod_i(x_i+1)
                         J_(k-1)((1+y)^2 P_x nu) dmu_ext^k(x).      (8.2)

Their common sign is the already extracted(-1)^k. All factorial endpoint and
arctangent moments stay in nu; the actual negative atom is paid separately in
Section4, not substituted by a positive measure in the FULL determinant.

At each tuple x, the ratio of the two displayed integrands is

    R_k(P_x nu)/prod_i(x_i+1).

Thus (8.1) gives

    R_k(nu) mathcal_S_minus <= mathcal_D_ext
       <= R_k(nu) mathcal_S_ext,                       (8.3)

where mathcal_S_minus replaces prod_i(x_i+1) in the slope integral by
prod_i(x_i-1), retaining its other factors. To compare these two slope integrals,
integrate the exterior variables first instead. At each compact tuple y of
length k-1, their respective Gram weights on x>1 are

    Q_plus(x)=(x+1) prod_j(x-y_j),
    Q_minus(x)=(x-1) prod_j(x-y_j).

Write their Gram matrices B_plus(y),B_minus(y), in the monomial basis of degree
<=k-1. They obey

    B_plus >= e^(-1)(1-gamma_k) M_0,
    B_plus-B_minus =2C(y),
    0<=C(y)<=e^(-1) M_-1.

The last inequality is pointwise on x>1 because prod_j(x-y_j)<=x^(k-1).
Using (2.2) and the correct Loewner direction gives

    B_minus >=(1-delta_k) B_plus,
    delta_k=2c_k/(1-gamma_k)=18/(k^2-11k+1).            (8.4)

For k>=64, k delta_k=2gamma_k/(1-gamma_k)<=2/5. Bernoulli therefore gives

    (1-delta_k)^k >=1-k delta_k>=3/5.

The compact averaging measure is positive, so determinant comparison and
(8.3) yield

    (3/5) R_k(nu) mathcal_S_ext <= mathcal_D_ext
       <= R_k(nu) mathcal_S_ext.

Equivalently, for the NORMALIZED exterior quantities E_D,E_S,

    (3/5) E_S <= E_D <= E_S.                           (8.5)

This is a correlation of the actual two exterior integrals, stronger than
separate Gamma ceilings. In every use of (8.2), the largest compact moment is
3k-2. Both Q_plus,Q_minus have degree k; their largest Gamma factorial is6k-4.

To pay the FULL overlap and atom, put tau_k=2e^11 4^(-k). Section4 and the
slope exterior lower bound imply

    |D_k-E_D| <= tau_k E_S,
    |S_k-E_S| <= tau_k E_S.

For k>=64, tau_k<1/100: e<3 and200*3^11<4^13<=4^64 suffice. Combining with
(8.5),

    (3/5-tau_k)/(1+tau_k) <= D_k/S_k
       <=(1+tau_k)/(1-tau_k).

The lower endpoint is>=59/101>1/2 and the upper is<=101/99<9/8. Hence the
STRONGER proposed FULL theorem is

    (1/2) R_k <= eps_k <=(9/8) R_k, k>=64.             (8.6)

It implies the sharper actual rational-error bounds

    3/(4k^2 A^(k-1)) <= eps_k <=63/(2A^(k-1)).         (8.7)

The exact logarithmic rate (5.3) and the sufficient/necessary q obligations
remain as stated, now with much better constants. No actual q bound is added.

Since R_(k+1)<=R_k/9, (8.6) further proves the proposed ONE-STEP contraction

    0<eps_(k+1)<=eps_k/4, for EVERY k>=64.              (8.8)

It supersedes the weaker stride13 consequence if independently accepted.
Adjacent rational zeros would then be strictly increasing and

    q_k q_(k+1) >=2 A^(k-1)/63,
    limsup log(q_k)/k >=(1/2)log(A).                    (8.9)

The relative matrix comparison, normalization of both integrations, and full
perturbation payments in this section require particular independent scrutiny.

## 9. An elementary denominator selector removes a redundant conditional premise

Let Delta_k=p_(k+1)q_k-p_k q_(k+1)>0. By (8.8), the adjacent gap is between
(3/4)eps_k and eps_k. Therefore

    q_k q_(k+1) eps_k <=(4/3) Delta_k.

Choose i(k) in{k,k+1} whose ACTUAL reduced denominator is smaller; this uses
only the two known integers and makes no choice based on the unknown target.
Its ordinary error is<=eps_k, hence

    0<q_(i(k))eps_(i(k))
       <=sqrt((4/3) Delta_k eps_k).                    (9.1)

Consequently bounded Delta on an explicit infinite set would prove irrationality
through this explicit selector WITHOUT assuming balanced neighboring denominators.
More generally Delta_k=o(A^(k-1)) on such a set suffices by (8.7). Since i(k)>=k,
the selected indices are unbounded; any duplicates can be removed. This is an
elementary conditional implication, not a new arithmetic bound on Delta. The
finite Delta32 has13281 digits and does not verify any infinite hypothesis.

This strengthens the conditional application in A5turn14; its balanced-ratio
premise was sufficient there for a whole-tail estimate but is unnecessary for
selecting a successful infinite subsequence. The global question is still open.
