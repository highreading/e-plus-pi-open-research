> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the fixed exponential-degree error theorem

Date: 2026-09-27. Reviewer: audit_results.
Source: fixed_exponential_degree_error_theorem.md.
Verdict: FULL PASS. No mathematical repair requested.

Scope: each one fixed integer b>=1, n tending to infinity.
No growing-b inference and no reduced-denominator bound are accepted
or claimed by the source. No additional degree scan was performed.

## 1. Exact equations, dimensions, and signs

For caps (n,b,n) and order 2n+b+1, there are n+b high logarithmic
moment equations. The first n+1 reconstruct C by the nondegenerate
degree-n kernel, leaving exactly b-1 orthogonal tests
p_(n+1),...,p_(n+b-1). The remaining endpoint row is 1+ell(V).
Taylor reconstruction then determines A. Thus the b-by-(b+1)
matrix in (2) is the actual remaining system.

The evaluated remainder uses both complete tails:
R(1)=ell_B(W). This identity is independent of b; it follows from
the polynomial projection and factorial summation, not from a
first omitted coefficient. For the maximal-cofactor vector,
Y=det[U;e+v;e]=-det[U;e;v] and
R=det[U;e;w]+det[U;v;w].
I checked the common orientation cancellation and the negative
sign preceding the first determinant ratio.

## 2. The determinant lemma retains its full cancellation order

For a shifted monomial t^r U/U(0), the source's difference
D_j=ell_(j+1)-ell_j has numerator
P_j(X)=(X)_(j+1)-(X)_j, X=n+k+r+1.
The polynomial P_j is monic of degree j+1.
The determinant of these polynomials has Vandermonde degree
S=d(d-1)/2; its symmetric quotient has degree d and top term
the product of the X_i. Hence its division by n^d tends to
Vandermonde(k_i+r_i), with the asserted orientation.

The n! factorial ratios supply n^(-k_i-r_i-1) in each row.
Together with u_k/n^k -> (-c)^k/k! and the n^d polynomial factor,
the remaining power is exactly n^(-sum r_i).
Summing the Vandermonde over the independent k_i weights gives
exp(-dc)Vandermonde(r_i): the sum is alternating of degree at most
S, and its top-degree scalar is the product of the exponential
sums. This argument is valid for the signed or complex weights.

I checked the required dominated bound separately. The reciprocal
root bound gives |u_k|/n^k <= (2L)^k/k! for every relevant k and
n>=1. The normalized polynomial determinant is bounded by a
fixed polynomial in the k_i+r_i+1, uniformly in n. Factorial
summation therefore gives precisely a fixed polynomial bound in
the r_i, as required by (6).

Uniform Cauchy bounds for the G_i coefficients then justify the
infinite multilinear expansion. Repeated r_i give identical rows
and vanish exactly. The least distinct index sum is S, with
indices 0,...,d-1. The remaining sum, multiplied by n^S, is O(1/n)
once n exceeds the reciprocal disk radius by a fixed factor.
This avoids an invalid entrywise-error estimate for a small
determinant. The leading Vandermonde is product_(j=0)^(d-1) j!,
so both the factorial and the n^S normalization in (4) are correct.

## 3. Actual local ratios and the two limiting functions

On the disk |t|<=1/20, the recurrence ratios stay in Re z<=-9/20:
the initial ratio has that property, as does every positive
beta_k times its reciprocal added to t-1/2.
The map has Lipschitz constant at most
(1/12)/(9/20)^2<1 on this half-plane. Its images are bounded.
The same contraction for constant beta=1/16 has the unique fixed
point equal to the displayed square-root branch at t=0.
The perturbation beta_k->beta thus proves uniform local ratio
convergence; Cauchy supplies fixed derivative convergence.

The actual U reference has the already proved reciprocal-root
bound 2 and scaled limit exp(-sqrt(2)z). Fixed products of adjacent
ratios give the high-row limits 1,h,...,h^(b-2).
The two exact normalized V,W quotients have value 1 at zero and
uniformly nonzero local denominators. I independently simplified
their limits using lambda=-a h, alpha_infinity/a=-s, and
1-t=a(h+1)(h-s)/h. This gives
G_V=(1-s)/(h-s), G_W=2/(h+1),
with h'(0)=-sqrt(2), exactly as stated.

## 4. Jet determinants and rank

Successive column differences, understood as multiplication by
the triangular matrix retaining the original adjacent differences,
have determinant 1. Expanding along the e row gives the same
cofactor sign for V and W. The factorial determinant lemma applies
with d=b.

After replacing t by h-1 in the fixed jets, the common nonzero
Jacobian power cancels in the ratio. The polynomial rows
1,h,...,h^(b-2) span every polynomial of degree at most b-2.
The last-row quotient is therefore the quotient of its derivatives
of order b-1:
((1-s)/2)^(b-1)=(sqrt(2)-1)^(b-1).
Both derivatives are nonzero. The empty polynomial-row case b=1
uses order zero and also checks.

The same lemma with d=b-1 verifies the stated b-column minor of
[U;e]. The additional v row is bounded by
C n^M |V(0)|/n! relative to this nonzero leading minor.
Since |V(0)|=exp(O(n)), it vanishes. This proves eventual rank b,
and the nonzero endpoint determinant proves Y!=0.
These facts concern the actual HP system, so Taylor reconstruction
gives the asserted projective uniqueness.

## 5. Whole-tail comparison and final sign

The entry bound for a fixed ell_j on every normalized reference
is at most C n^j |P(0)|/n!. It follows from the same root and
Cauchy estimates used above and also applies to the rational W
through its locally analytic normalized factor.
An extra factorially small row in det[U;v;w] therefore gives
the relative bound in (11), after the denominator asymptotic
loses only a fixed power of n. The factors W(0) and V(0) have
been retained; no positivity of the complex moment functional
is used.

The complete determinant quotient is consequently
R/Y ~ -(W(0)/V(0)) kappa^(b-1).
The prior exact reference identity has the factor
(-1)^(n+1) epsilon_n (1+alpha_n^*/b_n)/2,
whose final real factor tends to kappa. Hence
(-1)^n R/(Y epsilon_n) -> kappa^b.
This verifies the sign, nonzero limiting constant, and eventual
nonvanishing of the full evaluated remainder.

The actual primitive logarithmic form retains log q in (12).
No estimate for that q follows from the analytic result, and the
proof's constants depend on the fixed b. Those limitations are
stated correctly throughout the source.
