> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the high-factor ratio localization

Date: 2026-09-13. Reviewer: audit_sources.

Reviewed `raw_high_ratio_quasilocal_approximation.md`, including
the reciprocal, coordinate-sign, and cross-block numerical-rank
extensions, against the actual factor and Krylov conventions in
`raw_high_factor_split_and_parity_rank.md` and
`raw_high_multipoint_complementary_reduction.md`.

**Verdict: all stated claims pass this independent audit.** No
mathematical repair is requested. This is an analytic and algebraic
review; no new degree, node, or numerical matrix scan was performed.
The remaining combined-channel angle is a hypothesis in the final
rank conversion, not a proved estimate.

## 1. The actual roots, gap, and positive weights

For a nonempty high list, its first retained index exceeds
ceil(2 sqrt(n)), so l(l+1)>4n. Combining the actual lower node
bound with M_n=2n+3/4 gives the stated gap at least 2n. Moving
the last root of a longer parity list leaves an alternating pair
of equal lists and changes at most one low-factor degree. If no
list survives, the identity-ratio convention covers every claim.

The telescoping interlacing estimate gives

    (alpha_1-t)/(beta_h-t) <= R(t) <= 1.

The left ratio decreases in t. Its numerator at M_n is at least
2n and its denominator at most n^2, establishing 2/n <= R <= 1
on the entire spectral interval, including n=2 in the empty case.

At t=beta_i the residue of R is positive in the convention
R=1-sum c_i/(beta_i-t): multiplying by t-beta_i gives c_i.
Every paired factor in the product for c_i is positive. The
reciprocal has the opposite residue sign in the t-variable and
the stated representation 1+sum d_i/(alpha_i-t), with d_i>0.
The coefficients at infinity and at M_n therefore have exactly
the signs and normalized sums used in equations (6)-(8), (16b).

The symmetric row matrix has first off-diagonal -a_(k+1) and
second off-diagonal a_(k+1)a_(k+2), with all a_j positive.
Conjugation by diag((-1)^k) makes both bands positive. After a
scalar shift its resolvent above the spectrum is represented by
a convergent nonnegative Neumann series; the connected first
band makes every resolvent entry strictly positive. Thus the
negative off-diagonal entries in D R(K) D and the entrywise
positive reciprocal are exact. Positive definiteness follows
separately from scalar spectral calculus. No assertion about a
common cone for arbitrary Krylov coefficients follows or is used.

## 2. Chebyshev approximation and numerical rank

The numerator in equation (9) vanishes at the actual pole beta,
so division gives a polynomial of degree at most m. Multiplying
its residual by beta-M_n bounds the residual uniformly by
1/T_(m+1)(z_beta), with no denominator factor left unaccounted
for. The interval length is at most 6n^2 and the pole gap is at
least 2n, so z_beta>=1+2/(3n).

For u=sqrt(2/(3n))<=1, cosh(u)<=1+u^2. Monotonicity of cosh
therefore gives arcosh(z_beta)>=sqrt(2/(3n)). The inequality
1/cosh(v)<=2 exp(-v) yields exactly epsilon_(m,n) in (13).
The positive weights sum to less than one, so the sum of the
individual approximation errors has no factor depending on the
number of poles. For the reciprocal their sum is at most n/2-1,
which is safely bounded by n/2 in (16b).

Functional calculus gives the operator norm estimate. A degree-m
polynomial of a bandwidth-two matrix has bandwidth at most 2m.
Its distant coordinate tail is exactly zero, and its cross block
at any prefix cut has rank at most 2m. Compression of the norm
error and the singular-value rank-approximation inequality prove
(16) and (16a), including cuts near the finite endpoints. These
claims concern numerical rank at the specified tolerance, and do
not contradict the previous large exact cross-cut rank.

## 3. Actual support indices and the energy normalization

For even n, the two domain dimensions are d_0=n/2-1 and d_1=n/2;
the maximal indices before multiplication by p_m are respectively
n-4+2 ell_0 and n-1+2 ell_1. For odd n they are n-3+2 ell_0 and
n-2+2 ell_1. Multiplication of the selected channel by p_m adds
at most 2m. Thus r=min(n-1,2(m+max ell_sigma)) is a valid common
enlargement beyond coordinates 0,...,n in every parity. For the
specified logarithmic approximation degree it is o(n), and all
maximal indices eventually lie below 2n.

Within that degree range the finite coefficient transform has no
boundary error. The two nonzero component polynomials p_m L_a u_a
and L_b u_b belong to different vector-polynomial components;
their independence follows from the original triangular basis,
not from any positivity statement. Positivity of p_m follows
whenever the approximation error is at most 1/n, as stated.

F_b(K), R(K), and p_m(K) commute. Conjugation by F_b(K)^(1/2)
therefore preserves the norm of R-p_m and proves (17) without a
condition number of F_b. The note explicitly uses ordinary
orthogonal projection onto F_b^(1/2) of the coordinate subspace;
it never contracts an ordinary coordinate projection in the F_b
energy norm.

For each channel the Gram matrix is positive definite. Since
R>=2I/n and commutes with F_b,

    W_a^T F_b W_a <= (n^2/4) W_a^T R F_b R W_a.

Consequently the error in the individually normalized first
channel is at most (n/2) epsilon, exactly as in (23). The enlarged
energy subspace contains the approximate columns, and the
orthogonal complement of the retained energy subspace inside it
has dimension r. This gives the rank-r approximation used in (24).

## 4. The combined angle and actual projected matrix

Writing E=[E_a,E_b], the separate channel normalizations give

    E^T E = [[I,C],[C^T,I]], C=E_a^T E_b.

When both channels are nonempty its smallest eigenvalue is
1-||C||. Full rank of the original unprojected vanishing module
implies this is positive but supplies no quantitative lower bound.
The empty-channel convention delta_n=1 is correct.

The final normalization E(E^T E)^(-1/2) has operator factor
1/delta_n. Applying it to the proved rank-r approximation gives
(27), with that loss retained. The principal-angle identity then
gives at least n-1-r retained singular values >=sqrt(1-eta^2)
when eta<1; a negative count is merely a vacuous statement.

The orthonormal retained energy basis is
F_b^(1/2) P_L^T (F_b[L,L])^(-1/2). Pairing it with the normalized
combined image gives exactly the matrix in (28), with the stated
column Gram factors and the actual projected Z_L. All factors
are invertible, so its rank is the actual rank. Returning to an
unweighted singular value requires those factors; returning to
the physical spectral kernel requires the separately retained
amplitude-weighted cardinal matrix as well.

Thus a polynomial lower bound for delta_n would produce the
stated O(sqrt(n) log(n)) rank-defect reduction, but neither that
lower bound nor a growing mixed-kernel determinant estimate is
proved in this note. The unconditional content is the explicit
resolvent approximation, localization, coordinate sign, and
individually normalized energy-defect bounds.
