> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of complex neighborhoods and local jet inversion

Date: 2026-09-13. Reviewer: audit_results.

Reviewed raw_intermediate_holomorphic_jet_bounds.md in full, including
the new Section 5 block-Toeplitz inverse. The real-center theorem was
previously checked in raw_intermediate_parameter_independent_review.md.

**Verdict: PASS.** The analytic and local-module estimates are correct.
One minor scope clarification was sent to the author: the unqualified
phrase "subexponentially conditioned" in Section 5 should refer to
the actual even cut N=2n, or the bounded quadratic parameter range.
For arbitrary odd N and unbounded x the explicit seed factor remains.
No estimate or proof requires modification.

## 1. Exact complex relative-resolvent identity

For H=xI-K_j>0, Y=H^(-1/2)iota and h=z-x, the identity

    B_j(z)-B_j(x)=Y*[(I+hH^(-1))^(-1)-I]Y

is exact. Only the two outer factors are evaluated at the real
center. Since B_j(x)=Y*Y, the matrix V=Y B_j(x)^(-1/2) is an
isometry. Compressing the middle operator by V therefore gives
the claimed relative norm bound.

The eigenvalues of H are at least d=x-lambda_max(K_j); the
middle operator has norm at most |h|/(d-|h|). This argument is
valid for complex h and does not treat B_j(z) as a positive matrix.
For all preceding cuts d>=x-j-3/4>=x/3, for large N and x>=2N.
On the stated radius the relative perturbation is consequently
O(log(N)/sqrt(x)), with an absolute constant.

At late cuts this bound combines with the proved scalar real
boundary estimate without amplification by an unbounded condition
number. The exact transfer order remains Gamma^(-1) B_j(z)^(-1).
At early cuts, the real transfer and Gamma estimates imply a
scalar relative estimate for B_j(x) before (6) is applied. Thus
the early-cut error does not acquire a missing x/j^2 factor.
Both sums in Section 3 have the asserted uniform sizes.

## 2. Holomorphic disk and determinant normalization

The ratio rho_N(x)/x is at most log(N)/sqrt(2N), tending to
zero uniformly for x>=2N. The whole closed disk therefore lies
strictly in Re z>N+3/4 for all sufficiently large N. This places
it beyond the spectra of every preceding real symmetric K_j.

The determinant det(zI-K_N) is nonvanishing on that simply
connected half-plane, so the holomorphic square root chosen
positive on the real axis exists. The exact Casoratian has
det P_N=(-1)^N d_N^2; hence the normalized determinant is
(-1)^N, with magnitude one even at complex z.

For a two-by-two matrix of determinant magnitude one, the operator
norm of its inverse equals its own norm. The fixed-seed estimate
retains the half power (1+x)^((N mod 2)/2). Combining condition
bounds for the exact ordered product and dividing by the exact
determinant cancels the scalar factors without requiring them
to be holomorphic functions of the complex parameter. This proves
the uniform normalized matrix and inverse bounds in (3).

## 3. All derivative orders and the physical determinant scale

The functions and their inverses are holomorphic on a neighborhood
of the closed radius-rho disk. Operator-valued Cauchy estimates
give r! rho^(-r), with no dimension or derivative-order-dependent
constant. The same reasoning applies to the inverse matrix.

The determinant logarithm is the sum of the scalar logarithms
centered at the real point, with the branch fixed there. Each
relative eigenvalue displacement has modulus at most one half
for large N. Summing |log(1+u)|<=2|u| gives exactly the stated
3N log(N)/sqrt(x) upper bound and its reciprocal counterpart.

Applying Cauchy directly to P_N(z)/d_N(x) and
d_N(x) P_N(z)^(-1), with the real-center determinant scale held
constant, proves (5). This avoids an unaccounted Leibniz sum or
extra radius loss. The exact logarithmic-derivative formula (12)
and its factorial factor (r-1)!/2 also check.

## 4. The finite local jet multiplication inverse

The coordinate t=2(z-x)/rho maps |t|<=2 to exactly the original
disk. Both A_x=P_N(x+rho t/2)/d_N(x) and its actual inverse
are bounded by E_N there. Their coefficients are therefore
bounded by E_N 2^(-k).

Multiplication modulo t^nu is a lower block-Toeplitz operator.
Its coefficient-space Euclidean norm is at most the sum of
the block coefficient norms: write it as a sum of truncated
shift powers tensored with the coefficient matrices. Each shift
has norm at most one. Thus the norm is at most 2E_N, uniformly
in nu.

The formal identities A_x A_x^(-1)=A_x^(-1) A_x=I show that
the truncated Toeplitz matrix for the inverse series is the exact
two-sided matrix inverse at every multiplicity. Its norm has the
same bound. Noncommuting matrix coefficients cause no difficulty
because the product orders are preserved in these identities.

Direct sums have the maximum of their component operator norms.
They introduce no factor depending on the number of nodes or
their multiplicities. The determinant scale and radius at each
node define the coefficient norms and must remain in that direct
sum; the author explicitly retains them.

The resulting local isomorphism multiplies an already supplied
Taylor jet by the branch matrix. It is not the global Hermite
evaluation map from a polynomial space to all those jets, and
is not identified with the exceptional Schur block. The final
section correctly keeps both remaining distinctions.

## 5. Minor wording scope

At N=2n the odd seed factor is absent, so these local maps have
subexponential bounds uniformly on the actual denominator nodes.
The same conclusion follows on a bounded quadratic x-range for
either parity. For arbitrary odd N with x allowed to be arbitrarily
large, the proved bounds retain (1+x)^(1/2) for each norm, and
one must not silently absorb it into an N-subexponential constant.
This qualification was communicated to the author; all displayed
estimates already retain the correct factor.
The author has now applied the qualification to Section 5.
