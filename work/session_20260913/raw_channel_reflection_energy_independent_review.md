> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the reflection and boundary-energy angle theorem

Date: 2026-09-13. Reviewer: audit_results.
Source: raw_channel_reflection_energy_angle.md by audit_computations.

The complete theorem passes. I independently checked the actual
Borel–Legendre reflection normalization, the uniform subexponential
norm proof and its constants, the component-angle identity, the
energy conjugation, the rank-two commutator orientation, and the
boundary-residue Hilbert–Schmidt formula including repeated eigenvalues.
The elementary exponential estimate for the remaining weighted sum
also checks. No substantive correction is needed.

The proved conclusion is a subexponential bound for the unweighted
channel angle and an exact positive scalar target for the additional
energy loss. The source does not claim that target has the needed
subexponential bound; neither does this review.

## 1. Actual basis, translation and reflection

The raw monic Legendre formula
Q_k(t)=i^k P_k(−it)/c_k and the product
k!/(a_1...a_k)=c_k sqrt(2k+1) give exactly the E_k normalization
in equations (1)–(2). No factorial or leading Legendre coefficient
is omitted.

The map from a Euclidean coefficient vector c to

    p(t)=sum_(k<N)c_k sqrt(2k+1)i^k P_k(t)

is an isometry in complex L²([-1,1],dt/2). Its phases have unit
modulus and the normalized Legendre polynomials are orthonormal.
The actual polynomial represented by c is B[p(−ix)]. If
T p=(p−p(0))/t, direct coefficient differentiation gives

    D_x B[p(−ix)]=B[−i(Tp)(−ix)].

Thus translation by1 corresponds to exp(−iT). Reflection
f(x)->f(1−x) is parity after that translation; ordinary parity
is unitary in this coefficient norm. This establishes the norm
reduction without replacing the actual raw coordinate norm by
an unrelated monomial norm.

The branch identity (4) has the correct initial functions
1 and sqrt3(x−1/2). Its five-term induction is valid because
the outer coefficient is nonzero. Reflection commutes with the
actual differential operator Tcal and has opposite signs on
these initial functions. Hence the component involution is
exactly C_N, including the offset in v_1=e_1−sqrt3 e_0/2.

For the vectors in (5), the polynomial power is at most n−1.
Every intermediate degree is at most2(n−1)+sigma<=N−1.
Therefore truncating K to K_N causes no path to leave the
finite space. These actual vanishing spaces have the respective
pointwise eigenvalues +1 and −1 for C_N. No assumption that their
raw coordinate bases are orthogonal is used.

## 2. Resolvent-generating bound and contour constants

On each monomial t^k the finite geometric identity is

    sum_(j=0)^k s^j t^(k−j)
       =(t^(k+1)−s^(k+1))/(t−s).

By linearity this gives the exact removable divided difference
G_s p=(tp(t)−sp(s))/(t−s). The Legendre integral formula gives
|P_k(z)|<=exp(k|z|): its integrand is bounded by
(|z|+sqrt(1+|z|²))^k, and asinh(|z|)<=|z|. The stated
geometric-generating derivation justifies that integral formula
for complex z without an unresolved square-root choice.

Cauchy–Schwarz therefore yields
|p(z)|<=N exp(N|z|)||p||. For |s|=r<=1/4 and real |t|>=2r,
the divided difference is bounded by 2|p(t)|+|p(s)|. Its L²
contribution is at most (2+N exp(Nr))||p||.

For |t|<=2r, the entire segment from s to t is inside the disk
of radius2r. Cauchy's bound on disks of radius r centered there
uses only |z|<=3r and gives
|p'(z)|<=(N/r)exp(3Nr)||p||. Consequently the derivative of
z p(z) is bounded by3N exp(3Nr)||p|| on the segment. The
contribution of this second region is at most that bound.
Adding the two region norms gives at most

    (4N+2)exp(3Nr)||p|| <=6N exp(3Nr)||p||.

This verifies equation (8) with room in its constant.

The contour formula (9) has the correct ds/s factor. Expanding
exp(−i/s) and the finite G_s polynomial, its residue is exactly
sum_j (−i)^j T^j/j!. The essential singularity introduces no
uncontrolled series tail: T is nilpotent, and only its finitely
many coefficients contribute. On the circle, the exponential
has modulus at most exp(1/r). Thus the operator norm is bounded
by6N exp(1/r+3Nr). Taking r=(3N)^(-1/2) is admissible for
every N>=6 and gives precisely6N exp(2sqrt(3N)).

## 3. Unweighted angle and exact energy conjugation

For a principal pair of unit vectors u,v from the positive and
negative involution subspaces, choose their inner product c>=0.
In the orthonormal coordinates u,(v−cu)/sqrt(1−c²), the
involution is

    [[1,−2c/sqrt(1−c²)],[0,−1]].

Its largest singular value is sqrt((1+c)/(1−c)). Principal
pairs decompose the direct sum, with unmatched directions
contributing norm1. This proves the claimed relation on that
sum and the juxtaposed-basis value delta=sqrt(1−c). In the
application N=2n>=6 both channels have positive dimension;
the one-empty-channel convention elsewhere gives delta=1.

The restriction norm is bounded by ||C_N||. If
M=6N exp(2sqrt(3N))>=1, then
sqrt(2/(1+M²))>=1/M, verifying the simplified last bound in (11).

The actual energy identities are

    F^(1/2)R W_a=F^(-1/2)Z_a,
    F^(1/2)W_b=F^(-1/2)Z_b.

Thus the correct transported involution is
J_F=F^(-1/2)C_NF^(1/2), not the conjugation in the other order.
Its displayed subspace S is invariant, and the principal-angle
identity applies to its restriction exactly. Equation (14)
then follows by the inequality between restriction and full
operator norms. Individual Gram normalizations merely choose
orthonormal bases of these two energy subspaces and do not
alter their angle.

## 4. Boundary commutator and its sign

The matrix C is upper triangular by polynomial degree. Therefore,
for the first-N projection P, (I−P)CP=0. On finitely supported
coefficient vectors KC=CK is the polynomial identity that the
operator Tcal commutes with reflection. Every product column
in this identity has finite support, so no infinite Hilbert-space
domain or operator convergence is needed.

The in-to-out block of K across the cut, with interior coordinates
N−2,N−1 and exterior coordinates N,N+1, is Gamma_N; hence its
out-to-in block is Gamma_N^T. Compressing KC=CK gives

    K_N C_N=C_N K_N+U_N Gamma_N^T iota_N^T.

This checks both the positive sign and every transpose in (16).
The two columns of U_N are precisely the first N coefficients
of E_N(1−x),E_(N+1)(1−x), as required. Being a subblock of
C_(N+2), their norm has the stated bound from (6). The
Gamma_N factor has order N². Finite rank alone does not remove
the F-conjugation, and the source does not claim it does.

## 5. Divided ratio and the exact positive spectral sum

For F(t)=product_i(beta_i−t)>0 on the real row spectrum,
F is decreasing if the high factor is nonempty. Therefore

    psi_F(lambda,mu)
      =(sqrt(F(mu)/F(lambda))−1)/(lambda−mu)

is positive off the diagonal. Letting mu tend to lambda gives
the exact continuous value −F'(lambda)/(2F(lambda)), also
positive. The empty product gives zero everywhere.

For distinct spectral values, the commutator block equals
(lambda−mu) Pi_lambda C_N Pi_mu. Multiplication by psi_F
therefore gives precisely the corresponding block of J_F−C_N.
For a repeated eigenvalue, the entire equal-eigenvalue block
of both operators is zero. In particular the nonzero diagonal
value of psi_F is multiplied by a zero commutator block,
not by an unproved limiting spectral gap.

The squared Hilbert–Schmidt norm of a commutator block is

    ||Pi_lambda U_N Gamma_N^T iota_N^T Pi_mu||_HS²
      =tr[(U_N^T Pi_lambda U_N)
           (Gamma_N^T iota_N^T Pi_mu iota_N Gamma_N)]
      =tr(A_lambda B_mu).

Both 2-by-2 factors are positive semidefinite, so this trace
is nonnegative. At lambda=mu the trace is zero because that
whole commutator block is zero. Summing the mutually orthogonal
spectral blocks proves the exact identity (20), including
multiple eigenspaces. The B_mu agree with the residues of
the earlier boundary Weyl matrix; its formula has exactly
Gamma_N^T iota_N^T(zI−K_N)^(-1)iota_N Gamma_N.

Finally ||J_F||<=||C_N||+||J_F−C_N||_HS gives the stated
angle lower bound with Theta_N. This uses a Hilbert–Schmidt
upper bound for an operator norm, in the valid direction.

## 6. Elementary remaining loss and final scope

Writing g=sqrt(F), the mean-value estimate for
(g(mu)−g(lambda))/(g(lambda)(lambda−mu)) gives

    sup psi_F <=(1/2)sqrt(cond F)
                        sum_i 1/(beta_i−M_n).

Indeed |g'|=(g/2)sum_i(beta_i−t)^(-1); its numerator is
bounded by the largest g and its denominator by the smallest.
For retained nodes l>b=ceil(2sqrt n), the reviewed node bounds
give beta_i−M_n>=l²/2. Thus their reciprocal sum is at most
2 sum_(l>b)l^(-2)<=2/b.

The row spectral interval has length at most6n² for the stated
large-n application, so each factor in cond(F) is bounded by
1+12n²/l². Enlarging the product to all l=1,...,n and using
1+12(n/l)²<=13(n/l)² together with n!>=(n/e)^n proves (23).
The resulting estimate for Theta_N is only exponential in n.
It does not combine with the subexponential reflection norm
to yield a subexponential energy-angle bound.

All ingredients of the remaining scalar sum are actual finite
boundary residues and the actual high factors. A sharper estimate
for that weighted sum, or for the restriction of J_F to its actual
vanishing space, is still necessary. The source keeps this
condition explicit and does not infer an irrationality statement.
