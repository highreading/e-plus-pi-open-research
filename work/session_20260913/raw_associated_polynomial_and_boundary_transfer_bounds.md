> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Actual associated polynomial norms, endpoint weights, and two-boundary transfer

Date: 2026-09-13. Original continuation by audit_computations; independent review passed in `raw_associated_polynomial_transfer_independent_review.md`.

This note continues the independently reviewed exact Legendre-square and
uniform-measure results. It controls a growing polynomial subspace, the
actual endpoint polynomial of degree comparable to the block length, and
the signed two-boundary resolvent at positive Laplace parameters. The
alternating spectral weights are retained throughout. These estimates do
not establish the mixed interval zero bound or the high spectral row rank.

## 1. Actual matrices and coefficient bounds

Use a>=2, b>=a, r=b-a+1, and the notation of
`raw_coupled_pencil_exact_legendre_square.md`. Thus J_+ is the r-by-r
positive-off-diagonal Jacobi matrix with entries

    d_t=alpha_(2t)^2+alpha_(2t+1)^2,
    c_t=alpha_(2t+1)alpha_(2t+2),
    alpha_j=j/sqrt(4j^2-1),

at t=a,...,b. Let J_0 be the r-by-r matrix with diagonal 1/2 and
off-diagonals 1/4. Both matrices have spectrum strictly in (0,1).
Set m=a-1 and k=2m+1/2, as in the density note.

For t>=1, direct rational inequalities give

    0<d_t-1/2<=1/(30t^2),
    0<c_t-1/4<=1/(60t^2).                                     (1)

Indeed alpha_j^2=(1/4)[1+1/(4j^2-1)]. For d_t each denominator
is at least 15t^2. For c_t apply
sqrt((1+x)(1+y))<=1+(x+y)/2 to its two factors, whose
denominators are again at least 15t^2. The symmetric row-sum bound
therefore proves

    ||J_+-J_0||_2<=1/(15a^2)=:eta_a.                           (2)

There is no asymptotic coefficient substitution in these estimates.

## 2. A growing actual Krylov subspace with a controlled Gram matrix

Let mu_a be the associated probability measure, and let

    dmu_free(y)=(8/pi)sqrt(y(1-y))dy.

The proof in `raw_associated_measure_uniform_energy_bounds.md` in fact
implies the stronger pointwise absolute bound

    |w_a(y)-w_free(y)|<=8/k,   0<y<1.                          (3)

To check it, outside 1-y<k^(-2), apply the logarithmic ratio bound
and |exp(t)-1|<=exp(1/2)|t|. Since w_free<=4/pi and
w_free*sqrt(y)/sqrt(1-y)=(8/pi)y, the result is at most

    exp(1/2)[1/(pi m^2)+2/(pi k)]< 3/k.

Here k/m^2<=5/2. Inside the edge layer, the previously proved
w_a<=64/(pi^2 k) and w_free<=8/(pi k), together with positivity,
give (3). An absolute difference is bounded by the larger of these
two positive upper bounds, so no sum is needed.

For every complex polynomial q of degree at most d, put h=d+1.
Then the elementary free-measure inequality is

    integral_0^1 |q(y)|^2dy <=(3h/2)||q||_free^2.               (4)

Here is a proof retaining the endpoint cost. The orthonormal basis
is U_j(2y-1), j>=0, where U_j is the Chebyshev polynomial of the
second kind. Its endpoint bound is |U_j|<=j+1. Thus

    ||q||_infinity^2 <=[sum_(j=0)^d(j+1)^2]||q||_free^2
                     <=h^3||q||_free^2.

On [epsilon,1-epsilon], epsilon=1/(4h^2), the free density is at
least 2sqrt(3)/(pi h)>1/h. The interior integral is consequently
at most h||q||_free^2. The two omitted intervals have total length
1/(2h^2), contributing at most h||q||_free^2/2. This proves (4).

Combining (3)-(4) gives the all-degree quadratic-form estimate

    | ||q||_(mu_a)^2-||q||_free^2 |
       <=epsilon_d ||q||_free^2,
    epsilon_d=12(d+1)/k.                                      (5)

In particular every d=o(a) has a Gram matrix tending to the identity
in the free orthonormal basis. Every d+1<=k/24 has a Gram matrix
between I/2 and 3I/2. This improves the degree-o(a^(1/3)) conclusion
that would follow from the L1 estimate and the endpoint supremum
bound alone; the improvement uses the actual pointwise density bound.

For d<=r-1 this is an exact statement about an actual finite matrix.
Define

    Phi_d=[U_0(2J_+-I)e_1, ..., U_d(2J_+-I)e_1].

The Gaussian quadrature exactness through degree 2r-1 gives

    (1-epsilon_d)I <= Phi_d^T Phi_d <=(1+epsilon_d)I.             (6)

The columns have degrees 0,...,d and nonzero leading coefficients;
the tridiagonal nonzero off-diagonals imply

    range(Phi_d)=span(e_1,...,e_(d+1)).                          (7)

Thus (6) is an explicitly identified growing Krylov prefix, not an
abstract well-conditioned polynomial space. The same support fact
also states its limitation: if d<r-1, every q of degree <=d satisfies

    e_r^T q(J_+)e_1=0.                                        (8)

Low-degree moment control alone is exactly blind to the cross-boundary
entry. No estimate on that entry may be inferred from (6).

## 3. A uniform bound for the actual high-degree endpoint polynomial

Let p_j^(a) be the orthonormal polynomial of degree j for mu_a with
positive leading coefficient, p_(-1)=0 and p_0=1. Its exact recurrence is

    c_(a+j)p_(j+1)=(y-d_(a+j))p_j-c_(a+j-1)p_(j-1).             (9)

For the absent j=0 last term the value of c_(a-1) is immaterial.
On 0<=y<=1 write this as the free recurrence plus a forcing:

    p_(j+1)=2(2y-1)p_j-p_(j-1)+A_j(y)p_j+B_j p_(j-1),
    |A_j(y)|, |B_j| <=4/[15(a+j)^2].                           (10)

For A_j use (1), c>=1/4 and |y-1/2|<=1/2. For B_j use
|c_(t-1)-c_t|<=c_(t-1)-1/4<=1/[60(t-1)^2], and
t-1>=t/2. This also covers j=0 if desired, since a>=2.

Variation of constants for the free recurrence gives exactly

    p_j=U_j(2y-1)
       +sum_(h=0)^(j-1) U_(j-h-1)(2y-1)
                      [A_h p_h+B_h p_(h-1)].                  (11)

Define M_j=max_(0<=h<=j) ||p_h||_infinity/(h+1). Since
|U_s|<=s+1, equation (11) implies

    M_j<=1+(8/15)sum_(h=0)^(j-1)
                         [(h+1)/(a+h)^2] M_h.

The discrete Gronwall product and the bound
sum_(h=0)^(j-1)(h+1)/(a+h)^2<=j(j+1)/(2a^2) prove

    ||p_j^(a)||_[0,1]
       <=(j+1)exp[4j(j+1)/(15a^2)].                            (12)

This is linear growth with an absolute multiplicative constant when
j=O(a). In particular the actual endpoint polynomial p_(r-1) has
an explicit, polynomial supremum bound when r=O(a); its L2(mu_a)
norm remains exactly one. No leading coefficient or endpoint
normalization is discarded.

For clarity, the same bound holds for the endpoint polynomials of
the reversed finite r-by-r matrix, through degree r-1. Every diagonal
and off-diagonal of that matrix still satisfies (1) with t>=a.
For the reversed recurrence the coefficient errors are bounded by
4/(15a^2), because two off-diagonals lie in the same interval
[1/4,1/4+1/(60a^2)]. Repeating (11) with this uniform bound gives
exactly the exponent in (12). This finite reversal does not assert
that the reversed matrix is another infinite associated tail.

## 4. No exponentially missing endpoint quadrature modes

Let theta_i be the r eigenvalues of J_+ and v_i normalized real
eigenvectors. The recurrence gives

    (v_i)_(j+1)=p_j^(a)(theta_i)(v_i)_1,
    |(v_i)_1|^2=1/[sum_(j=0)^(r-1) p_j^(a)(theta_i)^2].         (13)

Apply (12) and sum (j+1)^2<=r^3. Applying the reversed finite
argument to the other endpoint proves both bounds

    |(v_i)_1|^2, |(v_i)_r|^2
       >= r^(-3)exp[-8r(r-1)/(15a^2)],   1<=i<=r.              (14)

Therefore every cross weight satisfies

    |(v_i)_1(v_i)_r|
       >= r^(-3)exp[-8r(r-1)/(15a^2)].                         (15)

These weights alternate in sign for r>=2, as already proved by the
irreducible Jacobi recurrence. Bound (15) does not change their
signs. When r=O(a), it says quantitatively that all r endpoint
modes remain active with at least polynomial weight. Their
cancellation in the cross sum remains a separate problem.

## 5. Exact relative control of the signed positive-parameter cross entry

Set R(tau)=(I+tau J_+)^(-1) and R_0(tau)=(I+tau J_0)^(-1).
For tau>=0 both inverses have operator norm at most one, so (2)
and the resolvent identity give

    ||R(tau)-R_0(tau)||<=tau/(15a^2).                          (16)

There is also relative, rather than merely absolute, control of the
exponentially small corner entry. The exact tridiagonal cofactor is

    R_(1,r)(tau)
       =(-tau)^(r-1)prod_(t=a)^(b-1)c_t / det(I+tau J_+).
                                                                    (17)

For tau>0 this has the same nonzero sign as the corresponding free
entry. Weyl's eigenvalue inequality, (2), and the derivative bound
|d log(1+tau x)/dx|<=tau on 0<=x<=1 give

    |log[det(I+tau J_+)/det(I+tau J_0)]|
       <=r tau/(15a^2).

Also 0<=log(4c_t)<=4(c_t-1/4)<=1/(15t^2). Combining these with
(17) proves

    |log[R_(1,r)(tau)/R_(0;1,r)(tau)]|
       <=r(1+tau)/(15a^2),  tau>0.                            (18)

The quotient in the logarithm is positive. For r>=2 and tau=0 both
corner entries vanish; (18) is then interpreted only by its limit,
not as a quotient of two nonzero numbers. The r=1 formula has the
usual empty product and remains valid.

This relative estimate uses an exact determinant identity. It does
not divide the absolute estimate (16) by an exponentially small
quantity. In the actual r=O(a) regime it gives relative error O(1/a)
uniformly on bounded positive tau intervals.

The free entry is explicit. Put z=1+2/tau for tau>0. Then

    det(I+tau J_0)=(tau/4)^r U_r(z),
    R_(0;1,r)=(-1)^(r-1)4/[tau U_r(z)],
    R_(0;1,1)=R_(0;r,r)=(4/tau)U_(r-1)(z)/U_r(z).              (19)

For z=cosh(t), U_r(z)=sinh((r+1)t)/sinh(t). Formula (18) thus
controls the actual cross entry relative to a specified exponentially
decaying expression, preserving all alternating-residue cancellation.

## 6. The actual boundary factors and Laplace initial data

Return to the original H,M,B of the coupled equation. With
D=diag((-1)^(j-1)),

    B_tilde=D M^(-1/2)B=[beta_L e_1, beta_R e_r],
    beta_L=gamma_a/sqrt(delta_a),
    beta_R=(-1)^(r-1)sqrt(rho_b)/sqrt(delta_b).                 (20)

For r>=2 these are distinct endpoint columns. The actual transfer is

    G(tau)=B^T(M+tau H)^(-1)B=B_tilde^T R(tau) B_tilde.

Define its free comparison with the SAME boundary factors,

    G_0(tau)=B_tilde^T R_0(tau) B_tilde.                       (21)

No approximation is made to gamma_a,rho_b,delta_a,delta_b. Since
gamma_a<=28/27, delta_a>=35/9 and rho_b<=1, one has
||B_tilde||^2<1 for r>=2. Hence

    ||G-G_0||<=tau/(15a^2).                                   (22)

The diagonal entries are relatively controlled, for example by

    |G_ii/G_(0;ii)-1|<=tau(1+tau)/(15a^2),                    (23)

since R_(0;ii)>=1/(1+tau). For the actual cross entry, the two
(-1)^(r-1) signs in (17) and (20) cancel. It is positive for tau>0
and obeys (18) relative to

    G_(0;12)(tau)
      =[gamma_a sqrt(rho_b)/sqrt(delta_a delta_b)]
           *4/[tau U_r(1+2/tau)].                             (24)

The positive value in (24) does not mean its individual spectral
residues have the same sign.

There is an exact connection to the ACTUAL polynomial forcing,
including its initial data. Write

    H Evec''+M Evec=B beta'',
    beta=(E_(a-1),E_(b+1))^T.

All components are polynomials, so their Laplace integrals on
[0,infinity) converge for every real s>0. Their initial values are
Evec(0)=1, beta(0)=(1,1)^T, and their first derivatives vanish.
The row sums of H give exactly H 1=B(1,1)^T. Consequently all
Laplace initial-data terms cancel, leaving

    Evec_hat(s)=s^2(M+s^2 H)^(-1)B beta_hat(s),
    B^T Evec_hat(s)=s^2 G(s^2) beta_hat(s).                    (25)

Thus (18),(22)-(24) apply to a genuine two-boundary Laplace transfer
of the actual polynomial family. The identity does not assume that
beta can be varied independently while retaining that family.

## 7. Remaining obstruction for the mixed observable

The polynomial comparison (5)-(7) is nontrivial on every d=o(a),
including d proportional to sqrt(a), and identifies the corresponding
actual finite Krylov prefix. The full endpoint polynomial bound
(12) and endpoint weights (14) work at r=O(a). The exact determinant
formula supplies additional relative control of the positive-parameter
cross transfer that the low-degree prefix cannot see by (8).

These controls are in their displayed norms and parameter ranges.
The oscillation question concerns constrained signed combinations
p^T Evec(x)+q^T Evec'(x) on 0<x<1. Neither positive-parameter
Laplace comparison nor lower bounds for the individual alternating
weights control zeros of that signed inverse transform. Near the
negative poles tau=-1/theta_i, no analogue of (16) follows from the
positive-axis argument, and a small matrix perturbation may move a
pole. The actual forcing also enforces exact cancellation of every
pole in its polynomial solution.

Finally, these are matrices for the coupled Legendre-square system.
No identification with a well-conditioned subspace of the separate
high spectral evaluation/Schur-complement problem has been proved.
Such a map would need its actual constraints, normalization and
projection bounds; it cannot be supplied merely by the common use
of an associated positive measure. The concrete remaining task is
to control the sign-selected combination of the two actual forcing
transforms in (25), or its exact inverse transform, while retaining
the endpoint constraints and all alternating residues.
