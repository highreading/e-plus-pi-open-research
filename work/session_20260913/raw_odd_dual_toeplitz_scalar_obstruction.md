> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Odd dual degrees: uniform signed Toeplitz structure and one scalar obstruction

Date: 2026-09-13. Original bounded continuation by audit_results.
Independent review: PASS by audit_sources; see raw_odd_dual_toeplitz_independent_review.md.

This continues the passed raw_joint_dual_hankel_and_even_root_product.md and its root review. It retains the actual matrix dimension n+1, the actual primitive polynomial, and the actual linear endpoint functional. It does not assume that a signed Toeplitz or Hankel matrix is positive.

For odd n=2m+1, m>=0, there is an exact real scalar s_m, defined below using a compression which is proved invertible, such that

    V_n(1)/[t^n]V_n = B_m^odd s_m,
    B_m^odd = (4m+2)! m! (3m+2)! / ((2m+1)!)^3.            (1)

The normalization of s_m has no growing operator-norm cost: the full normalized Toeplitz matrix has norm at most e sqrt(5/4), and its Hermitian part has a uniform spectral gap around zero, with equally many positive and negative eigenvalues.

The separately passed added-column theorem raw_dual_endpoint_added_column_dyadic.md, reviewed in raw_dual_added_column_independent_review.md, proves s_m!=0 for every m. The norm estimates do not control its magnitude. The exact remaining scalar estimate is

    log|s_m|=o(m).                                         (2)

If (2) holds, the absolute odd-degree root-product limit is the same 3sqrt(3)/e as for even degrees. A sign for s_m is not inferred from the single available odd-degree control.

## 1. The actual odd matrix

Retain q_n(z)=z^n U_n(1/z), with coefficient vector q, and

    a_k=[z^k] e^z(1+z^2)^n,
    A=(a_(n+i-j))_(i,j=0)^n.

The exact reviewed identity is

    A q=n! V_n(1) e_0.                                     (3)

Its symbol is e^(e^(i theta))(2cos theta)^n. The first n high rows, namely rows 1,...,n after reversal, have rank n. The independently proved deleted-last-row theorem gives

    q(0)=u_n=(2n)![t^n]V_n !=0.                             (4)

These are all-index facts. No full determinant of A is assumed nonzero.

Put L=m+1. After ordering even coefficients before odd coefficients, a polynomial of degree at most 2m+1 is

    p(z)=u(z^2)+z v(z^2),   degree u,degree v<=m.

Use the positive comparison weight

    w_(m+1)(theta)=|1+e^(2i theta)|^(2m+2)
                 =(2cos theta)^(2m+2).

Its full Gram matrix G is block diagonal with two copies of

    C_(m+1)=(binom(2m+2,m+1+i-j))_(i,j=0)^m.                (5)

All references to square roots of G mean its positive definite real square root.

## 2. A uniform comparison for the two required positive weights

For a polynomial u of degree at most m, let

    I_a(u)=integral_|t|=1 |1+t|^(2a)|u(t)|^2 dtheta/(2pi).

The following bounds hold for every m>=0:

    I_m(u)<= (5/4) I_(m+1)(u),
    I_(m+1)(u)<= (5/4) I_(m+2)(u).                         (6)

Here is an elementary proof, including the degree dependence. With
t=(1+iy)/(1-iy), write u(t)=P(y)/(1-iy)^m, where degree P<=m.
The change of variables gives

    I_a(u)=4^a/pi integral_R |P(y)|^2(1+y^2)^(-a-m-1)dy.

Thus I_a/I_(a+1) is one quarter of the mean of 1+y^2 under the polynomial weight |P|^2(1+y^2)^(-beta), where beta=a+m+2.

For the even positive weight (1+y^2)^(-beta), the monic orthogonal polynomials through degree m+1 have squared norms

    h_j = j!/(2beta-2j)_j
          integral_R (1+y^2)^(j-beta)dy,

where the denominator is rising factorial. This follows by differentiating (1+y^2)^(j-beta) j times, multiplying by (1+y^2)^beta, and integrating by parts. Its leading coefficient before monic normalization is (-1)^j(2beta-2j)_j. All boundary terms vanish for beta=2m+2 or 2m+3 and j<=m+1.

The three-term recurrence therefore has zero diagonal and positive squared off-diagonal coefficients

    alpha_j=h_j/h_(j-1)
       =j(2beta-j)/[(2beta-2j)^2-1].                        (7)

These increase with j in the stated range. At j=m+1 and beta=2m+2, the value is 3(m+1)^2/[4(m+1)^2-1]<=1. At beta=2m+3 it is smaller than 1 as well. Hence multiplication by y from degree at most m to degree at most m+1 has norm at most 2, by its tridiagonal matrix with off-diagonal entries at most 1. Consequently the mean of 1+y^2 is at most 5, proving (6). This includes m=0 and complex coefficient polynomials.

## 3. The normalized odd matrix has uniformly bounded norm

For two polynomials p,r of degree at most n, the symbol and Cauchy–Schwarz give

    |p* A r|
      <=e [integral |2cos theta|^(2m)|p|^2]^(1/2)
           [integral |2cos theta|^(2m+2)|r|^2]^(1/2).

Each even weight is pi-periodic, so the mixed terms between u(z^2) and z v(z^2) integrate to zero. Applying the first inequality of (6) to both parity components proves

    Atilde=G^(-1/2) A G^(-1/2),
    ||Atilde||<=C0:=e sqrt(5/4).                            (8)

The comparison retains the dimension 2m+2. In particular the normalization does not hide factorial or exponential losses in an unspecified matrix norm.

## 4. Exact positive and negative subspaces of the Hermitian part

Consider the two explicit L-dimensional subspaces

    P_+={(1+z)u(z^2): degree u<=m},
    P_-={(1-z)u(z^2): degree u<=m}.

They are orthogonal for the G inner product, and the squared G norm of either displayed polynomial is 2 I_(m+1)(u).

Pair theta and theta+pi in the original signed symbol. Write x=cos theta and y=sin theta. The exact real quadratic forms are

    Re <(1+z)u,A(1+z)u>
       = integral 2(2x)^(2m+1) cos(y)
                     [sinh(x)+x cosh(x)] |u(z^2)|^2,

    Re <(1-z)u,A(1-z)u>
       = integral 2(2x)^(2m+1) cos(y)
                     [sinh(x)-x cosh(x)] |u(z^2)|^2.        (9)

The normalized circle measure is understood. These paired integrands are even under (x,y)->(-x,-y). For x>=0,

    sinh x+x cosh x>=2x,
    x cosh x-sinh x>=x^3/3,
    cos y>=cos(1)>0.

The first inequality in (9) is consequently at least 2cos(1)I_(m+1)(u). The negative of the second is at least cos(1)I_(m+2)(u)/12. Applying the second inequality of (6) proves

    Re <p,Ap> >= a ||p||_G^2 on P_+,       a=cos(1),
    Re <p,Ap> <=-b ||p||_G^2 on P_-,       b=cos(1)/30.     (10)

Thus H=Re(Atilde) has exactly L positive and L negative eigenvalues. In fact it has a uniform spectral gap. In the orthogonal P_+,P_- decomposition its diagonal blocks are >=aI and <=-bI, and its off-diagonal norm is at most C0. A block Schur factorization gives

    ||H^(-1)|| <= (1+C0/a)^2/b.                             (11)

The negative Schur block is -H_- - X*H_+^(-1)X and has inverse norm at most 1/b. This proves (11) without any control on roots of V.

The conclusion concerns the Hermitian part. It does not prove invertibility of Atilde: a nonsymmetric real matrix can be singular while its Hermitian part is invertible with both signs. The missing scalar below preserves that distinction.

## 5. An always-defined one-scalar Schur complement

The exact binomial determinant formula from the even-degree note gives

    c_m=(G^(-1))_(0,0)
       =((2m+1)!)^2/[m!(3m+2)!] >0.                        (12)

Let

    v=G^(-1/2)e_0/sqrt(c_m),  ||v||=1,
    Pi=I-vv*,
    B=Pi Atilde restricted to v-perpendicular.

The compression B is invertible for EVERY m>=0. The following argument proves this directly from the high rows, before using the stronger added-column theorem that A itself is invertible. To see this, the n high rows of (3) imply that Pi Atilde has rank n and one-dimensional kernel. Its kernel is generated by x=G^(1/2)q. By (4),

    v*x=q(0)/sqrt(c_m)!=0.

The kernel thus meets v-perpendicular trivially. The restriction B, a square map of dimension n, is injective and hence invertible. This argument uses the actual high-row rank and actual constant coefficient, not generic nonsingularity of a principal minor.

Define the real scalar

    s_m=v*Atilde v-v*Atilde Pi B^(-1) Pi Atilde v.           (13)

The vector k=v-B^(-1)Pi Atilde v has v*k=1 and Pi Atilde k=0. Therefore x=(q(0)/sqrt(c_m))k. Taking the v component of (3) after normalization gives

    n! V_n(1)=q(0)s_m/c_m.

Substitution of (4) and (12) proves (1). In particular,

    V_n(1)=0 iff s_m=0 iff A is singular.                  (14)

The now independently passed added-column theorem excludes all three alternatives for the actual family in every degree. Thus s_m is always nonzero and v*Atilde^(-1)v=1/s_m. The unconditional norm estimate (8) supplies the honest upper bound

    |s_m|<=C0+C0^2 ||B^(-1)||.                              (15)

No bound on ||B^(-1)|| or a nonzero lower bound for s_m is inferred from (11).

## 6. The exact remaining odd-degree analytic target

Stirling's formula in (1) yields, with n=2m+1,

    log B_m^odd
       =n log n+[(3/2)log 3-1]n+O(log n).                  (16)

Thus (2) would imply

    (|V_n(1)/[t^n]V_n|)^(1/n)/n ->3sqrt(3)/e

along odd degrees. Conversely, that nonzero root-product limit implies log|s_m|=o(n). This is an exact scalar obstruction in a specified uniformly bounded normalization. It does not involve a growing unspecified multiplicative constant.

One sufficient, stronger pair of estimates is ||B^(-1)||=exp(o(n)) together with |s_m|>=exp(-o(n)). The first controls the upper side by (15); the second excludes the isolated scalar cancellation. Neither is presently proved.

The uniform two-sign theorem (10) shows why simply copying even accretivity is incorrect. It also provides a concrete matrix structure for future estimates of B and s_m. All cross-parity terms remain in Atilde and in (13); none has been dropped by replacing the signed symbol with its absolute value.

The added-column congruence also fixes the scalar's dyadic depth exactly. With phi(k)=v_2(k!),

    B_m^odd s_m=V_n(1)/[t^n]V_n in 1+2 Z_2,
    v_2(s_m)=-1-phi(3m+2)+phi(m).                          (17)

Indeed v_2(B_m^odd)=1+phi(3m+2)-phi(m), by phi(2k)=k+phi(k) and phi(2m+1)=m+phi(m). This dyadic valuation does not control |s_m| in the real absolute value.

## 7. Only the frozen n=1 control

For the already saved V_1(t)=2-t and q_1(z)=-2+3z (the reversal of U_1(t)=3-2t),

    A=[[1,1],[3/2,1]],   G=2I,  c_0=1/2,
    Atilde=A/2, v=e_0, B=[1/2], s_0=-1/4.

Here B_0^odd=4, so (1) gives V_1(1)/[t]V_1=-1 exactly. This confirms the sign convention and normalization. It does not establish a sign or an Archimedean size theorem at other odd degrees; nonvanishing follows separately from the added-column proof. No additional canonical degree was constructed.

The signed dual integrals and fixed-combination endpoint gcd remain separate research targets. Neither (1) nor the uniform Hermitian-part bounds prove a shrinking integer form or irrationality.
