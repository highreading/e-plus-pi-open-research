> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the confluent boundary-resolvent Gram

Date: 2026-09-13. Reviewer: audit_results.

Reviewed raw_confluent_boundary_resolvent_gram.md in full.
**Verdict: PASS.** The actual resolvent family has the asserted full
column rank and exp(-C D log N) lower singular-value bound at the
specified repeated dyadic nodes. No correction is needed.

The proof keeps the actual row matrix, every repeated-pole coefficient,
the physical N^2 jet factor, and the normalized boundary coupling.
It does not establish the separately needed compression or identify
this family with the exceptional Schur block.

## 1. Nodes, spectrum and growing dimensions

With N=2n, the largest dyadic multiplier obeys 2^(J-1)<=n/2.
Thus the largest x_j is at most 3n^2/2+2n+3/4, and every
a_j=x_j/N^2 is in (0,1) for sufficiently large n. The first
unscaled gap from the upper row spectral bound is exactly 3n;
the smallest consecutive node gap is also 3n. After division by
N^2, both are 3/(2N), stronger than the 1/N bounds used.

The reviewed row spectral estimates imply ||J_N||<=2 safely.
The stated multiplicity and number of nodes give
D=O(sqrt(N)log N), so D<=N/4 eventually. All arguments are
explicitly restricted to sufficiently large n, and no small-index
exception has been silently absorbed into this dimension bound.

## 2. Exact tail block recurrence and support

Let V_r select coordinates N-2-2r,N-1-2r in increasing order.
For r>=1 the connecting block is explicitly

    C_r=Gamma_(N-2r)/N^2,

where Gamma_u has entries

    [ a_(u-1)a_u,       0          ]
    [ -a_u,            a_u a_(u+1)].

Writing A_r=V_r^T J_N V_r, the exact decomposition is

    J_N V_r=V_(r-1) C_r^T+V_r A_r+V_(r+1) C_(r+1).

The absent r=-1 term is omitted. This agrees with the author's
orientation in (5), with B_r=C_r^T, and puts the inverse on
the correct right-hand side.

For every connecting block actually used, all recurrence indices
are at least N-2D+1>=N/2. The diagonal entries after division
by N^2 are bounded below by an absolute positive constant, and
the triangular off-diagonal entry is bounded. The inverses are
therefore uniformly bounded. The diagonal blocks have bounded
norm as compressions of J_N.

The coefficient recursion for expressing V_r in powers of J_N
has the bound M_(r+1)<=C(3M_r+2M_(r-1)), with one absolute
constant. Increasing C_0 gives the asserted C_0^(r+1) bound.
No factorial or cut-dependent inverse enters this recursion.

Each application of the band-two matrix extends support at most
two coordinates toward the interior. Hence J_N^s V_0, s<D,
is supported entirely in the last 2D coordinates. The identity
Y T=[V_0,...,V_(D-1)] is consequently an exact square inverse
identity after tail compression. Equivalently, its right side
has full rank and T is square, so T is invertible and Y equals
that isometry times T^(-1).

The norm estimate for the block coefficient matrix T follows
from its block row and column sums; D C_0^(D+1) is a safe
upper bound. The lower singular-value bound in (7) therefore
holds. The upper bound follows from
||J_N^s V_0||<=2^s and the norm of a concatenated block matrix.

## 3. Quantitative repeated-pole coefficient basis

The polynomials p_(j,r)=q/(a_j-t)^(r+1) are D linearly
independent polynomials of degree below D: a relation divided
by q has zero principal part at each distinct node, forcing
every coefficient to vanish. Their ordering is consistent with
the Kronecker product C_q tensor I_2 in the factorization.

For a unit Euclidean coefficient vector, |p(t)|<=sqrt(D)2^(D-1)
on each radius-1/(4N) disk. Every other denominator factor there
has modulus at least 3/(4N), so p/q_j is holomorphic throughout
that disk with the stated upper bound. The principal-part
coefficient is a Taylor coefficient of order nu-r-1; its possible
sign is immaterial for the norm estimate. Cauchy's factor is
at most (4N)^(nu-1), not a derivative factorial.

Combining these estimates and taking the Euclidean norm of the
D coefficients proves ||C_q^(-1)||<=D(8N)^D. The estimate
retains the entire multiplicity and uses actual node separation;
no unproved confluent-Vandermonde conditioning assertion enters.

## 4. Factorization and singular-value products

The matrix polynomial identity is exactly

    W=q(J_N)^(-1) Y (C_q tensor I_2).

All a_j are above the entire row spectrum, so q(J_N) is positive
definite regardless of the parity of nu. The scalar bound
|q(t)|<=3^D on the spectrum gives
sigma_min(q(J_N)^(-1))>=3^(-D). Together with the two preceding
inverse bounds, the usual lower singular-value inequality for
a square-left/tall-middle/square-right product gives the stated
lower bound. Each factor acts on the required full space.

For the upper bound, every block of W has norm at most N^(r+1)
by its spectral distance. Concatenation gives sqrt(D)N^nu.
Both estimates have the stated exp(C D log N) scale. Squaring
the lower bound gives the Gram eigenvalue statement with a
larger absolute constant. Since D log N=O(sqrt(N)log^2 N)=o(N),
the claimed subexponential exponent is correct.

## 5. Local jet radii and actual boundary factors

The local radius h_j=sqrt(x_j)log N/2 is exactly half the
holomorphic radius used in the independent branch-jet theorem.
For large N, h_j>=1 and h_j/N^2<=1, proving the two loose
bounds N^(-2)<=t_j<=1. Diagonal scaling by t_j^r therefore
loses at most N^(-2(nu-1)) in the least singular value, which
is absorbed by C D log N. The signs do not change singular
values, and the upper norm is not increased.

The conversion to unscaled resolvents is exact:

    (a_j I-J_N)^(-r-1)=N^(2r+2)(x_j I-K_N)^(-r-1),

while t_j^r=h_j^r N^(-2r). After multiplying by (-1)^r,
the result is precisely N^2 h_j^r times the r-th physical
derivative divided by r!. Thus the displayed N^2 factor in
(12) is essential and correct; neither a factorial nor a
radius factor is missing.

Finally Gamma_N/N^2 and its inverse have uniformly bounded
norm by the same triangular coefficient bounds. Right
multiplication by the repeated 2-by-2 factor preserves the
singular-value scale. Using the unnormalized Gamma_N instead
introduces the explicit common N^2 factor, as the source states.

## 6. Scope of the conclusion

This proves a lower bound for the full N-by-2D two-component
resolvent-jet family and its Gram. Removing good directions,
restricting the two channels, or inserting the earlier physical
metric can introduce a small angle. A general compression need
not preserve the lower bound just proved. The source explicitly
retains that remaining bridge and the additional low-factor
directions; no exceptional-matrix or endpoint conclusion is
inferred from the Gram bound alone.
