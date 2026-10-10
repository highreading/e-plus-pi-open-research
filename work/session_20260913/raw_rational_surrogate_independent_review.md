> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the rational-surrogate rank improvement

Date: 2026-09-13. Reviewer: audit_computations.

Reviewed `raw_rational_surrogate_rank_improvement.md` in full.
The proof passes. No correction is requested. I checked the bin
endpoints, exact remainder, numerator and denominator degrees,
absence of a denominator-conditioning loss, actual polynomial
embedding, supported-angle estimate, exact good count, completion
to the full energy image, and the smaller Schur and physical maps.

The accepted result is an actual rank bound
n−O(sqrt(n)log(n)) and a correspondingly smaller exact exceptional
problem. It does not assert a full old-cutoff channel-angle bound.

## 1. Bins, normalization and exact scalar error

The actual high roots satisfy 2n<=a_i=beta_i−M_n<=n².
With g=2n, the largest possible a_i/g is n/2. Thus

    J=1+floor(log_2(n/2)),
    j=floor(log_2(a_i/g))

always has 0<=j<J. In particular if n/2 is a power of two
and a_i=n², its bin index is the last included index, not
one beyond the list. At an internal dyadic boundary the root
is assigned to the next bin, as required by the half-open bins.

For a in [g2^j,g2^(j+1)), rho=(3/2)g2^j satisfies
|a−rho|<=rho/3. Since x>=0, this gives
|(rho−a)/(rho+x)|<=1/3. The exact finite geometric identity is

    a/(a+x)
      =a sum_(r=0)^(nu−1)(rho−a)^r/(rho+x)^(r+1)
        +[a/(a+x)] [(rho−a)/(rho+x)]^nu.

Multiplying the ordinary geometric-series identity by a/(rho+x)
verifies both the sign and the factor in the remainder. Its absolute
value is at most3^(−nu), because a/(a+x)<=1. Summation with
the actual positive normalized omega_i costs at most their sum,
which is less than one. Hence the scalar approximation error has
no factor J, nu, or the number of roots.

Every denominator power appearing in the truncated expression is
at most nu and belongs to one of the retained bins. Therefore the
common denominator Q in source (4) clears every term exactly.
Its factors are strictly positive on the row spectrum. Each
correction to1 has numerator degree at most D−1 after clearing Q,
so P has degree exactly D and the same leading coefficient as Q.
There is no possible leading-degree cancellation. Empty bins can
introduce common factors but do not invalidate these degree claims
or the subsequent polynomial embedding.

Functional calculus gives the stated operator error, and commuting
with F gives the identical F-energy error. The choice
nu=ceil(4sqrt(6n)/log3) gives epsilon<=exp(−4sqrt(6n)).
Consequently D=nu J=O(sqrt(n)log(n)) is eventually smaller than
both original multiplier dimensions, which are asymptotic to n/2.

## 2. The actual restricted embedding and its support

Multiplication by the nonzero Q maps polynomials of degree below
d_a−D injectively into polynomials of degree below d_a. Its image
therefore has codimension exactly D in the original first-channel
domain. Since the original full unprojected vanishing map is
injective, this is also an actual p'=n−1−D dimensional subfamily.
The second channel and its original offset seed are unchanged.

The first surrogate component has degree at most

    deg(P)+ell_a+(d_a−D−1)=ell_a+d_a−1.

Thus the added denominator degree has been exactly offset by the
restriction on v; it has not been added to the coordinate support.
The surrogate support is no larger than that of the original low-
factor W spaces. In particular s=n+O(sqrt n), whereas the positive
weight has degree h<=n/2+1, so s+h<2n eventually.

All branch coefficient identities are consequently exact inside
the finite matrix. Since P is nonzero and has degree D, both
surrogate channel maps are injective. Their opposite pure component
polynomials cannot cancel each other. The C-eigenvalue statement
uses the actual v_0=e_0 and v_1=e_1−(sqrt3/2)e_0; it is not
an assumption of coordinate parity orthogonality.

The original cutoff supplies beta_i−M_n>=2n. With the positive-
power lemma's M=2n+1, beta_i−M>=2n−1/4>0. Hence the
coefficients in the expansion of F_b(K) in powers of H=MI−K
are positive, and the previously reviewed support lemma applies
with exactly the source's A_n.

## 3. There is no hidden condition-number loss from Q

For a restricted first-channel input set

    w=L_a(K)Q(K)v.

Because every factor is a function of K and Q(K)>0, the difference
between the actual and surrogate images is exactly

    R(K)w−P(K)L_a(K)v=(R−P/Q)(K)w.

The F-energy error is at most epsilon||w||_F. At the same time
the actual norm is ||R(K)w||_F>=(2/n)||w||_F. This is an
inequality on the entire restricted first-channel space. Therefore,
after its *actual* Gram normalization, the operator error is at
most n epsilon/2. Neither v nor Qv is compared in Euclidean norm;
no norm of Q, inverse of Q, or multiplication-coordinate matrix is
required. This verifies the main normalization issue in (10).

Each actual channel of E_D is orthonormal. The surrogate blocks
retain the same normalization, so their individual smallest singular
values are at least1−t_n. Separately orthonormalizing the surrogate
blocks and using the supported angle bound gives

    sigma_min(Etilde_D)>=(1−t_n)/A_n.

Weyl's inequality then yields (11). Since
A_n t_n=O(n³exp(−2sqrt(6n))) tends to zero, the final lower
bound1/(2A_n) follows for all sufficiently large n. This applies
only to E_D, not the full old-cutoff channel juxtaposition.

The final combined restricted orthonormalization has norm cost
at most1/sigma_min(E_D)<=2A_n. Thus

    ||O_D−Otilde_D||<=2A_n t_n

is exactly the source's (12), with all Gram factors retained.

## 4. The good count includes the D sacrificed directions correctly

The retained raw coordinate prefix corresponds to channel-degree
caps q_sigma=floor((n−sigma)/2). Since deg P=D, no tail
coordinate is present precisely when

    deg v<=q_a−ell_a−D,
    deg u_b<=q_b−ell_b.

For large n these bounds are nonnegative and strictly inside the
relevant multiplier ranges. The sum q_0+q_1=n−1 gives exactly

    g_good=n+1−ell_0−ell_1−D.

The restricted family has dimension p'=n−1−D, so only
ell_0+ell_1−2 of its directions lie outside this good subspace.
Relative to the *full* family there are D additional sacrificed
directions. The total exceptional count is therefore

    k=(n−1)−g_good=D+ell_0+ell_1−2.

The original cutoff and optional one-root transfer give
ell_0+ell_1=b+1 or b+2, hence k=D+b−1 or D+b. This is
the claimed O(sqrt(n)log(n)) count; the D loss is neither
omitted nor counted twice.

In actual restricted orthonormal coordinates the good space is
T_D^(−1)ran(I_good). Its orthonormal frame Q_good maps under
Otilde_D into the retained energy space. The norm comparison from
(12) then proves (15). The actual columns O_D Q_good are
orthonormal, so their retained least singular value is at least
sqrt(1−eta_n²), establishing the full-matrix rank lower bound.

## 5. Completion to the full energy image is legitimate

The good frame belongs to the full image F^(1/2)ran(X). That
image has dimension n−1 by the reviewed unprojected independence.
It can therefore be extended to an orthonormal frame O_full with
the good columns first. No lower bound for the angle between the
original full channels is needed for the existence of this frame.

Because F^(1/2)X is injective and has this same range, O_full
equals F^(1/2)X times an invertible coefficient matrix. This matrix
may be poorly conditioned; the source explicitly does not bound it.
The asserted orthogonal block transformations act on the resulting
energy-orthonormal coordinates, not on the original unnormalized
multiplier coefficients.

For A_full equal to the retained projection of O_full, its first
g_good columns have defect norm at most eta_n. Completing their
retained images orthogonally gives the exact rectangular block form
in source (17). The good Gram lies between (1−eta_n²)I and I;
the good/exceptional cross block is bounded by
eta_n/sqrt(1−eta_n²), using A_full^T A_full=I−D_full^T D_full.
Thus the same controlled Schur elimination applies with the smaller
k, regardless of how the remaining full-image columns were completed.

This proves rank Z_L=n−1−k+rank T_n and the stated number of
near-unit retained energy singular values. The exact complementary
identity transfers rank to the prescribed actual high block.

## 6. The physical map and the omitted directions

Write O_full=F^(1/2)X T_full with T_full invertible. Then

    A_full=F[L,L]^(−1/2) Z_L T_full,
    Z_L^T=T_full^(−T) A_full^T F[L,L]^(1/2).

In H_high=−Z_H^(−T)Z_L^T S, both leading factors are invertible.
The upper triangular retained block forces every vector of
ker A_full^T into U_e ker T_n^T. Hence the physical map is
exactly the source's

    ker H_high=S^(−1)F[L,L]^(−1/2)U_e ker T_n^T.

This derivation does not require a norm bound on T_full. The
positive metric M_e=J_e^T J_e retains every actual g_l and
cardinal factor in S. Its dimension is k+2, but its conditioning
and endpoint action remain unproved.

Finally, the source correctly refuses to reuse the previous all-
exceptional polynomial-surrogate tail test. The D omitted directions
were not included in X_D or its error estimate. Completion to the
full image proves the exact block form and rank count, but does not
create an approximation theorem for those omitted columns. This
scope limitation is necessary and is stated explicitly.

## 7. Review conclusion

All substantive claims pass: the rational approximation has its
stated uniform error, the exact divisor restriction offsets the
polynomial numerator's degree, no Q conditioning enters the actual
Gram-normalized estimate, and the resulting restricted good frame
gives an O(sqrt(n)log(n)) exceptional full-family problem.

Complete rank, the remaining small Schur block, the physical
two-plane angle, primitive denominator bounds, and irrationality
remain separate. No new computation or degree scan was used in
this review.
