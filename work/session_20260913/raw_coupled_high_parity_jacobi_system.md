> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The actual mixed high block as a symmetric system with two boundary functions

Date: 2026-09-13. Original continuation by audit_computations.

This derives an exact finite matrix differential system for the ACTUAL
high span. It preserves the two parity branches and their boundary
members, unlike an arbitrary-forcing resolvent argument. Its symmetric
pencil has explicitly controlled frequencies. These facts do not yet
prove the mixed zero bound or an additional high-row rank estimate.

## 1. An exact second-derivative recurrence

Use E_m=F_(2m)/Q_(2m)(0), and the normalized odd O_m from
`raw_mixed_parity_volterra_and_darboux.md`. The proved identities are

    E_(m+1)-E_m=(4m+3) I O_m,
    (2m+1)^2 O'_m=(4m+1)E_m+4m^2 O'_(m-1).

Eliminating O'_m gives, for every m>=1,

    E_(m+1)''-(1+gamma_m)E_m''+gamma_m E_(m-1)''
       =delta_m E_m,                                        (1)

where the constants simplify exactly to

    gamma_m=4m^2(4m+3)/[(2m+1)^2(4m-1)]
           =1+1/[(2m+1)^2(4m-1)],
    delta_m=(4m+3)(4m+1)/(2m+1)^2
           =4-1/(2m+1)^2.                                  (2)

Thus the departure from the constant discrete Laplacian is O(m^-3),
while the mass coefficient differs from 4 by O(m^-2). No asymptotic
fit or new degree construction is involved.

## 2. Symmetrization with the actual two boundary functions

Fix integers 1<=a<=b, put r=b-a+1 and

    Evec=(E_a,...,E_b)^T,
    rho_a=1, rho_(m+1)=rho_m/gamma_(m+1).

Let H have diagonal rho_m(1+gamma_m) and off-diagonal
H_(m,m+1)=H_(m+1,m)=-rho_m. Let M=diag(rho_m delta_m), and

    B=[gamma_a e_1, rho_b e_r],
    beta(x)=(E_(a-1)(x), E_(b+1)(x))^T.

Equation (1) is exactly

    H Evec''+M Evec=B beta'',
    Evec(0)=1vec, Evec'(0)=0.                               (3)

Both H and M are symmetric positive definite. In fact, with endpoint
values z_(a-1)=z_(b+1)=0,

    z^T H z=gamma_a z_a^2
          +sum_(m=a)^(b-1) rho_m(z_(m+1)-z_m)^2
          +rho_b z_b^2.                                    (4)

Only the two displayed neighboring even polynomials occur as forcing
functions. There is no replacement of their actual values by arbitrary
positive data. The system size r grows with the original degree.

## 3. Exact embedding of the mixed high span and its constraints

The odd identity

    O_m=(E_(m+1)'-E_m')/(4m+3)                              (5)

makes the embedding particularly small at its boundaries. Positive
normalizations relating E_m,O_m to F_k do not change their spans.

If n=2s+1>=3, choose a=s+1,b=2s+1,r=s+1. Then

    H_n={p^T Evec+q^T Evec' : p_b=0, sum_m q_m=0}.            (6)

Indeed the even members are E_a,...,E_(b-1), while the odd members
are the r-1 consecutive differences in (5). Those differences span
exactly the coefficient hyperplane with sum q=0. The dimension is
2r-2=n-1.

If n=2s>=2, choose a=s,b=2s,r=s+1. Then

    H_n={p^T Evec+q^T Evec' : p_a=p_b=0, sum_m q_m=0}.        (7)

The even members now run from E_(a+1) to E_(b-1), with the same consecutive
derivative differences. The dimension is 2r-3=n-1. The two summands
in (6),(7) have opposite parity and are independent. Thus no additional
unwritten relation or boundary function is being discarded.

Equations (3),(6),(7) turn the original all-index zero problem into a
precise coupled matrix problem with two actual forcing polynomials and
two or three coefficient constraints. The earlier scalar Darboux
non-selfadjointness does not apply to this different, vector-valued
formulation.

## 4. Every frequency has a uniform explicit comparison

Let L_r be the ordinary r-by-r Dirichlet discrete Laplacian with diagonal
2 and off-diagonal -1, and put

    S_a=sum_(m=a)^infinity 1/[(2m+1)^2(4m-1)] <=1/(8a^2).

The inequality follows from the summand bound 1/(12m^3), separating
the first term and bounding the rest by an integral. Every edge weight
in (4), and every rho_m, lies between exp(-S_a) and exp(S_a). Therefore

    exp(-S_a)L_r <= H <=exp(S_a)L_r,
    exp(-S_a)[4-(2a+1)^(-2)]I <= M <=4exp(S_a)I.              (8)

Let omega_1>...>omega_r>0 be the frequencies defined by

    M v_j=omega_j^2 H v_j.

They are distinct: M^(-1/2)H M^(-1/2) is an irreducible symmetric
tridiagonal matrix. The eigenvalues of L_r are
`4sin^2(j*pi/[2(r+1)])`, in increasing j order. The min--max principle
and (8) give the exact bounds

    exp(-S_a) sqrt[1-1/(4(2a+1)^2)]
      <=omega_j sin(j*pi/[2(r+1)])<=exp(S_a),                (9)

simultaneously for EVERY 1<=j<=r and every b>=a. In particular,

    omega_j sin(j*pi/[2(r+1)])=1+O(a^-2)                    (10)

with an absolute implied constant, independent of r and j. For the
actual high blocks a and r are both of order n, so this is a uniform
all-mode comparison, including the largest frequency of order n.
There is no fixed-index asymptotic assumption in (9).

## 5. Two-boundary forcing does not remove the growing number of modes

The exact endpoint transfer in a formal derivative parameter tau is

    B^T(M+tau H)^(-1)B
       =sum_(j=1)^r z_j z_j^T/(tau+omega_j^2),
    z_j=B^T v_j,   v_i^T H v_j=delta_ij.                    (11)

This is a positive matrix Stieltjes representation with r simple poles.
Both entries of every z_j are nonzero. To see this, use the equivalent
irreducible tridiagonal problem for M^(-1/2)H M^(-1/2): an eigenvector
with first or last coordinate zero would be zero everywhere by the
three-term recurrence.

Moreover the sign of the product of its two endpoint coordinates is
(-1)^(j-1), in the ordering of (9). Here the off-diagonal entries are
negative, so the lowest tridiagonal eigenvector has one sign; successive
eigenvectors have the usual alternating endpoint product. This sign
can also be obtained without a nodal theorem: the endpoint inverse
entry is the positive product of the magnitudes of the off-diagonals,
divided by det(J-tI); residues at its ordered simple roots alternate.
Positive diagonal rescalings do not change those signs. Thus the
off-diagonal residues in (11) alternate. The diagonal measures are
positive. For r>=2 the cross residues have both signs, so there is no
single positive scalar measure for the cross entry. When r=1, the two
forcing columns are collinear and the sole cross residue is positive;
all actual high blocks in (6),(7) have r>=2.

Consequently the universal two-input/two-output transfer has all r
poles, with no endpoint-unobservable modes. A bounded number of forcing
FUNCTIONS is not a bounded-dimensional homogeneous dynamics. This is
an exact property of the actual coefficients (2), not a generic matrix
counterexample.

The particular forcing beta in (3) is polynomial, so it selects the
special solution in which the oscillatory homogeneous terms cancel.
One exact way to retain that cancellation is

    Evec=sum_(j=0)^b (-M^(-1)H)^j M^(-1)B beta^(2j+2).       (12)

This follows by iterating (3), with zero remainder because each E_m
has degree at most 2b. The last possible derivative of E_(b+1) is
2b+2, so the upper limit b is necessary in general. Formula (12)
uses growing derivative order and alternating matrix powers; it must
not be replaced by independent freely oscillating modes or by an
arbitrary positive forcing.

## 6. The precise next zero-count lemma

A sufficient theorem is the following statement for the actual data
(2)--(7): every nonzero observable p^T Evec+q^T Evec' has at most n
zeros in (0,1). This would prove full high spectral row rank by the
independently reviewed singular-endpoint Sturm bridge.

The new formulation supplies a positive symmetric pencil, exact two
boundary functions, explicit boundary coefficient constraints, and
uniform frequency information. What it does NOT yet supply is control
of the cancellations in (12) for arbitrary admissible p,q. The
alternating cross residues and the r distinct active modes in (11)
identify what a proposed two-channel variation theorem must preserve.
A theorem depending only on the rank of B, the positivity of H,M, or
the positive scalar resolvent of the original Volterra operator would
omit essential information. No new rank improvement is claimed here.
