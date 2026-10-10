> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact Legendre-square identification of the coupled parity pencil

Date: 2026-09-13. Original root continuation; independent review pending.

The symmetric pencil in `raw_coupled_high_parity_jacobi_system.md`
is exactly an associated Jacobi matrix for the ordinary Legendre
measure after the substitution y=u². This identifies its positive
measure and finite quadrature without a perturbation argument. In
particular every frequency is strictly greater than one, and all its
nodes interlace a specified set of squared Legendre zeros. The actual
two-boundary forcing and its coefficient constraints are still needed
for the mixed zero problem; no zero-count conclusion is claimed here.

## 1. Exact entries, including the gauge

Use the prior note's a≥1, b≥a, r=b−a+1, rho_m, gamma_m, delta_m,
H and M. Set

    J=M^(-1/2) H M^(-1/2),
    alpha_k=k/sqrt(4k²−1)  (k≥1), alpha_0=0.

Direct substitution gives

    J_(m,m)=(1+gamma_m)/delta_m
            =alpha_(2m)²+alpha_(2m+1)²,
    J_(m,m+1)=−sqrt(gamma_(m+1)/(delta_m delta_(m+1)))
              =−alpha_(2m+1)alpha_(2m+2).                 (1)

For example the two terms of the diagonal are

    (2m+1)²/[(4m+1)(4m+3)]
       +4m²/[(4m−1)(4m+1)].

The squared magnitude of the off-diagonal is

    4(m+1)²(2m+1)²/[(4m+3)²(4m+1)(4m+5)].

Let D be the diagonal matrix with entries (−1)^(m−a). Then
J_+=D J D has positive off-diagonals. This gauge is essential for the
ordinary Jacobi interpretation; it does not change eigenvalues.

Take the normalized Legendre polynomials

    ell_k(u)=sqrt(2k+1) P_k(u)

in L²([-1,1],du/2). Their exact multiplication recurrence is

    u ell_k=alpha_(k+1)ell_(k+1)+alpha_k ell_(k−1).

Applying this recurrence twice and restricting to even indices proves
that J_+ is exactly the compression of multiplication by u² to

    span{ell_(2a),ell_(2a+2),...,ell_(2b)}.                (2)

All terms at the two boundaries are retained in the diagonal in (1).
In particular this is not the square of multiplication by u compressed
to that even space (which would be zero).

## 2. Strict bounds and specified Legendre interlacing

For every nonzero polynomial q in the space (2),

    0 < integral u²|q|² du/2 < integral |q|² du/2.

Thus 0<J_+<I as quadratic forms. Its eigenvalues
theta_1<...<theta_r are simple, by its nonzero tridiagonal off-diagonals.
The pencil frequencies in the prior note satisfy

    omega_j=theta_j^(-1/2)>1,  j=1,...,r.                 (3)

The indexing agrees with the descending frequency order there.

For a specified comparison, let 0<x_1<...<x_(b+1)<1 be the positive
zeros of P_(2b+2). The even-index matrix for indices 0,...,2b has
eigenvalues x_j². To verify this normalization, square the ordinary
Legendre Jacobi matrix on indices 0,...,2b+1. Its even block is exactly
that matrix; its odd block has the same positive eigenvalues. The
original Jacobi matrix has the symmetric zeros of P_(2b+2) as its
eigenvalues, as follows from its determinant three-term recurrence.

Deleting the first a rows and columns gives exactly J_+. Successive
principal truncations of an irreducible tridiagonal matrix strictly
interlace. Therefore, for a≥1,

    x_j² < theta_j < x_(j+a)²,
    1/x_(j+a) < omega_j < 1/x_j,   1≤j≤r.                (4)

For a=0 the identification extends with equality theta_j=x_j².
The strict interlacing can be proved by the determinant recurrence:
consecutive characteristic polynomials have no common root, and
Cauchy interlacing then has no equality. Iterating a times gives (4).
These are all-index statements, not asymptotic zero locations.

## 3. A fixed positive measure behind every starting index

Under y=u² the even Legendre basis becomes

    p_m(y)=sqrt(4m+1) P_(2m)(sqrt y),
    dmu_0(y)=dy/(2sqrt y),  0<y<1.                       (5)

These are real polynomials and are orthonormal for the probability
measure mu_0. Their infinite Jacobi matrix has diagonal
d_m=alpha_(2m)²+alpha_(2m+1)² and off-diagonal
c_m=alpha_(2m+1)alpha_(2m+2)>0.

Let J^(a) be its infinite principal tail starting at m=a, and let
mu_a be the spectral probability measure of its first coordinate.
The finite matrix J_+ above is its first r-by-r truncation. The tail
is a positive contraction: it is the compression of multiplication
by y to the closed span of p_a,p_(a+1),.... It has no eigenvector at
0 or 1, since the same integral strictness argument would force its
representing function to vanish almost everywhere. Thus mu_a has
no endpoint atoms.

This measure is explicitly determined by a finite fractional-linear
transformation of one elementary logarithm. Define

    m_a(z)=integral dmu_a(y)/(z−y),  z outside [0,1].

For real z>1, direct integration in u gives

    m_0(z)=1/(2sqrt z) log((sqrt z+1)/(sqrt z−1)).        (6)

It determines the analytic function elsewhere by continuation from
the integral, avoiding an unstated logarithm branch. Schur complementation
of the first tail coordinate gives exactly

    m_(a+1)(z)=[(z−d_a)m_a(z)−1]/[c_a² m_a(z)].        (7)

Let the polynomial matrix

    T_a(z)=[[A_a,B_a],[C_a,D_a]]
          = product from k=a−1 down to 0
               [[z−d_k,−1],[c_k²,0]],
    T_0=I.

Then

    m_a=(A_a m_0+B_a)/(C_a m_0+D_a),
    det T_a=prod_(k=0)^(a−1)c_k²>0.                    (8)

The order of multiplication in (8) follows by composing (7); it is
not interchangeable. On 0<y<1 the upper half-plane boundary value is

    m_0(y+i0)=1/(2sqrt y) log((1+sqrt y)/(1−sqrt y))
                       −i*pi/(2sqrt y).

Because T_a(y) is real with positive determinant, the denominator
C_a m_0+D_a cannot vanish there: if C_a≠0 its imaginary part is
nonzero; if C_a=0, invertibility forces D_a≠0. The elementary formula
for the imaginary part of a real fractional-linear transform gives

    dmu_a(y)/dy = [prod_(k=0)^(a−1)c_k²]
           /[2sqrt y |C_a(y)m_0(y+i0)+D_a(y)|²] >0.     (9)

For completeness, the boundary formula is analytic on each compact
subinterval of (0,1), so Stieltjes inversion gives absolute continuity
there and excludes interior singular measure. Possible residual mass
could only lie at the two endpoints, where it has already been
excluded. Thus (9) describes the entire probability measure mu_a.
The denominator is retained; no uniform bound in a is inferred.

## 4. Exact quadrature and the remaining matrix signs

Let v_j be an orthonormal eigenbasis of J_+ at theta_j and set
w_j=|(v_j)_1|². Irreducibility makes each w_j strictly positive, and
sum_j w_j=1. The quadrature identity is

    integral q(y) dmu_a(y)=sum_j w_j q(theta_j)
                        for every deg q≤2r−1.           (10)

An elementary proof compares (J^(a))^k_11 and (J_+)^k_11. A tridiagonal
walk which leaves the first r coordinates and returns to the first
requires at least 2r steps, so the moments agree through degree 2r−1.
The spectral theorem then gives (10). No limiting quadrature claim
is required.

The full two-boundary transfer must still retain its endpoint factors.
With the original B from the coupled note, set

    B_tilde=D M^(-1/2) B.

Then its exact expression is

    B^T(M+tau H)^(-1)B
       =B_tilde^T(I+tau J_+)^(-1)B_tilde.               (11)

Its two diagonal corner measures are positive. For r>=2, its off-diagonal
weights contain the product of the two endpoint components of v_j
and alternate in sign. Equations (9)–(10) therefore do not turn this
cross measure into a constant-sign scalar measure. For r=1 the two
endpoint columns are collinear and the sole cross weight is positive;
all actual high blocks have r>=2. These representations do not remove
any of the r poles at tau=−1/theta_j<−1.

The exact positive measure (9), specified quadrature (10), and
Legendre interlacing (4) provide additional structure for the actual
coupled system. A useful next step is a bound for the sign-selected
mixed observable, or for its exact polynomial cancellation formula,
using this associated measure with both boundary factors retained.
The frequency bounds alone and positivity of either diagonal measure
do not establish that bound. The original endpoint normalization,
primitive denominator and irrationality target remain unresolved.
