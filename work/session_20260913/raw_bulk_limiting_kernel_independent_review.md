> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the many-node limiting bulk-kernel bounds

Date: 2026-09-13. Reviewer: audit_results.
Source: raw_bulk_limiting_kernel_eigenvalue_bounds.md by audit_computations.

The complete proof passes. I checked the actual spectral spacing,
the two parity-vector constants, the exact Cauchy inverse diagonal,
the factorial trace estimate, both eigenvalue and determinant scales,
the actual high-column normalization, and the perturbation and sparse
selection conditions. No substantive correction is required.

The source proves bounds for the limiting matrix and gives precise
sufficient hypotheses for transfer to the actual one. This review
does not replace its conditional entrywise-rate hypothesis with an
unproved rate, nor does it assert a full growing high-matrix inverse
bound.

## 1. Actual-node spacing and vector constants

For l_j>l_i the reviewed enclosures give

    xi_(l_j)−xi_(l_i)
      >= (l_j−l_i)(l_i+l_j+1)−1/4
      >= 2 alpha n (l_j−l_i).

The last inequality holds because l_i>=alpha n and the extra
(l_j−l_i)(l_j−l_i+1)−1/4 is positive. Thus it needs neither
consecutive selection nor an unproved spectral-gap formula.
Dividing by 4n² and using

    −q'(c)=q(c)/sqrt(c(c+1))

gives precisely tau|i−j|/n in the stated compact interval.
The lower and upper c bounds also hold for the allowed integer
rounding of the original indices.

For the first component of each parity vector, all three factors
have the stated positive compact-interval lower bounds. The minimum
used in a_* therefore bounds both parities. For A_*, use
sqrt(cosh² eta+sinh² eta)<=exp(eta), maximum parity prefactor sqrt2,
and q^(±1/4)<=q_-^(-1/4). This bounds the whole vector norm rather
than just its individual coordinates.

Writing the two component diagonals as D_0,D_1 gives exactly
L=D_0 K D_0+D_1 K D_1. Its first term implies
lambda_min(L)>=a_*²lambda_min(K), because
||D_0v||>=a_*||v||. This is an eigenvalue estimate from a
congruence; it does not assume D_0 K D_0>=a_*²K in Loewner order.
The source makes the correct, weaker assertion.

## 2. Exact Cauchy inverse and the factorial gain

The determinant formula is

    det K = (product_i q_i²)
            (product_(i<j)(q_i−q_j)²)
            / product_(i,j)(1−q_i q_j).

Taking its principal cofactor ratio cancels all pairs avoiding i
and leaves exactly

    (K^-1)_ii = q_i^-2(1−q_i²)
      product_(j!=i) [(1−q_i q_j)/(q_i−q_j)]².

In particular the factor is 1−q_i², not its reciprocal. The one-node
case agrees with K_ii=q_i²/(1−q_i²), which fixes that orientation.

With r=m−1, actual spacing gives the denominator product at least
(tau/n)^r(i−1)!(m−i)!. Dropping the numerator factors, each of
which is at most1, and summing the inverse diagonal yields

    tr K^-1 <= q_-^-2(n/tau)^(2r)
       binom(2r,r)/(r!)².

The finite combinatorial identity follows by multiplying the sum
of reciprocal squared factorials by (r!)²; it becomes
sum_j binom(r,j)²=binom(2r,r). Thus lambda_min(K)>=1/tr K^-1
gives exactly equations (11)–(13) of the source. There is no
unaccounted factor m and no use of an entrywise bound for the
operator norm of a nonpositive inverse. The inverse is positive
definite, so its trace does control its largest eigenvalue.

For r>=1, r!>=(r/e)^r and binom(2r,r)<=4^r produce the source's
simplified lower bound. For m=1 the empty product gives q_-²,
which is a valid lower bound directly.

## 3. Feature ranks and the two different exponential scales

The expansion of L has exactly two scalar features for each
power s>=1. Keeping s<=h therefore has rank at most2h, regardless
of the selected parity pattern. Its positive semidefinite tail
has trace bounded by

    m A_*² q_+^(2(h+1))/(1−q_+²).

Choosing h=floor((m−1)/2) makes the rank strictly less than m.
The exponent 2(h+1) is m for even m and m+1 for odd m; replacing
it by m gives the valid common upper bound in (16).

More generally, h=floor((j−1)/2) has rank below j and gives
lambda_j<=C_*m q_+^(2 ceil(j/2)), with eigenvalues in decreasing
order. This justifies the product bound for the determinant,
including both odd and even j. The initial j=1,2 cases simply
use the full positive tail with h=0.

When rho n<=m<=n, the exact inverse bound gives
lambda_min>=exp(−C n): one has r>=rho n/2 eventually, and the
base tau r/(2en) is bounded below by a fixed positive constant.
The feature bound gives lambda_min<=exp(−c n), after absorbing
the polynomial prefactor. The diagonal entries are bounded below
by a positive constant, so the asserted exponential order of the
ordinary condition number follows as well, together with the
O(m) trace upper bound.

For determinants, the first Gram congruence yields
det L>=a_*^(2m)det K by determinant monotonicity for positive
definite matrices. The spacing-product identity
product_(i<j)(j−i)=product_(j=1)^(m−1)j! gives (18).
Alternatively the already proved exp(−C n) bound for every
eigenvalue yields the exp(−C n²) lower scale immediately.
Multiplying the feature eigenvalue bounds gives an exponent
2 sum_j ceil(j/2) of order m²; its positive m log(C_*m) term
is lower order. Hence the stated exp(−Theta(n²)) determinant
scale is distinct from the exp(−Theta(n)) least-eigenvalue scale.

## 4. Actual column normalization and stability

I compared Section6 against raw_actual_branch_column_asymptotics.md.
The prescribed high interval is n+1,...,2n−1 and its upper cut
is 2n, so the limiting vectors are the even-cut a_0,a_1 and the
column powers are x^(3/2),x, independently of the lower-cut parity.
The actual selected parameter is c_i=xi_(l_i)/(2n)².

Thus the source's exact scale

    d_i=g_(l_i) s_(2n)(xi_(l_i)) xi_(l_i)^(p_(sigma_i))

contains precisely the amplitude, retained scalar product, and
correct parity-selected column power. These are positive real
numbers in the reviewed spectral phase. The actual Gram satisfies
G_actual=D hat(G) D, with this exact diagonal D; no amplitude
asymptotic or common-power substitution is used.

An entrywise error epsilon_n has operator norm at most m epsilon_n.
Since L>=b_(m,n)I, Weyl's inequality gives the stated sufficient
rank threshold epsilon_n<=b_(m,n)/(2m). For
eta_n=m epsilon_n/b_(m,n)<1, the error bound also implies

    (1−eta_n)L <= hat(G) <= (1+eta_n)L.

This proves the determinant ratios and the logarithmic bound
2m²epsilon_n/b_(m,n) for eta_n<=1/2. Restoring D costs at
least min_i d_i in a safe feature singular-value lower bound,
as the source explicitly retains. A bare o(1) error supplies
none of these exponentially small comparisons for m~n.

The positive-semidefinite rank-loss example is correctly used
only to show a norm-stability limitation. Subtracting the least
eigenvalue projector creates a singular PSD matrix at exactly
that operator distance; it is not claimed to be the actual HP
matrix or a counterexample to an additional structured theorem.

## 5. Sparse equally spaced selections and the conditional logarithmic regime

Let a=ceil(alpha n), b=floor(beta n), and choose the actual integer
indices in (26). When (b−a)/(m−1)>=2, subtracting floors gives

    l_j−l_i >= (j−i)[(b−a)/(m−1)−1]
             >= (j−i)(b−a)/(2(m−1)).

For large n, b−a>=(beta−alpha)n/2. This implies the source's
slightly weaker but convenient bound with denominator4m and
hence spacing tau_s|i−j|/m in q. Thus the construction preserves
distinct actual nodes with no assumed spectral interpolation.

Repeating the inverse proof with n/tau replaced by m/tau_s gives
the first inequality in (28). Since (m−1)/m>=1/2, the simplified
base is at least tau_s/(4e); replacing exponent2(m−1) by2m makes
the bound weaker because that base lies strictly between0 and1.
The definitions indeed make it less than1: c_+>=1/4 gives
tau<1, and tau_s=tau(beta−alpha)/4<1/4.

For m=floor(kappa log n) and kappa<1/C_s, the least-eigenvalue
lower bound is c n^(-C_s kappa). Under the explicitly conditional
entrywise rate O(log n/n),

    m² epsilon_n/lambda_min(L)
      =O((log n)³ n^(-1+C_s kappa)) -> 0.

The rank and relative-determinant transfer then follow. A
consecutive cluster of the same size would not meet this improved
spacing bound, and the source correctly excludes that inference.
Likewise this logarithmic selection does not prove the full-density
rank or conditioning assertion.

## 6. Review conclusion

All claimed exact identities, constants and asymptotic scales pass.
The retained distinction is essential: the limiting kernel is
quantitatively positive definite for a growing bulk selection,
but transfer requires a compatible quantitative error in the
actual normalization. The source identifies that requirement
and does not silently derive it from convergence alone.
