> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Signed error of the fixed b=3 factorial B-only Gram center

Status: main-agent author proof, not independently reviewed. This document preserves and develops the latest automatically recorded derivation. It uses the retained exact Toeplitz representation, forcing identities and canonical reconstruction. Their existing scopes remain attached. No numerical computation, old audit or seed calculation is repeated. The conclusion concerns one specified approximation family; the rationality or irrationality of e+pi remains OPEN.

## 1. Construction and theorem

Let n tend to infinity through even integers. Fix b=3 and factorial-weight parameter m_w=1. Let T_n be the actual three-by-three contact Toeplitz matrix and f=fP, fQ its two forcing columns. Set

    M0=1+sqrt(2), sigma=sqrt(2),
    Dsc=diag(1,-sigma,2),
    Aplus=1+1/sigma, Aminus=1-1/sigma.

On coefficient polynomials of degree at most two, let Dpol differentiate and let Z multiply by t-1. Define

    Krec=Z(I+Dpol)^(-n),
    w_j=(n-1)!/(n+2-j)!, 0<=j<=3,
    W=diag(w_j^2), G_n=Krec^T W Krec,
    xi=T_n^(-1)f, u=Krec xi,
    a_n=xi^T G_n xi=u^T W u,
    lambda=T_n^(-T)G_n xi/a_n,
    kappa=u^T W e0/a_n.

The center in question is exactly

    c_n=kappa+lambda^T fQ,
    lambda^T f=1.

It is the factorial B-only Gram center, not a coordinate center or a full-coefficient norm center. Its endpoint correction kappa is part of the definition.

The author theorem proved below is

    c_n-(e+pi)=-4pi M0^(-2n-3)(1+o(1)).            (1)

In particular this complete error is negative and nonzero eventually. If q_n=den(c_n) is its actual reduced denominator, then

    log(q_n |c_n-(e+pi)|)
        =log q_n-2n log M0+O(1).                  (2)

No upper or lower global estimate for q_n crossing this rate is supplied here.

## 2. Exact scaled Toeplitz integral

For even n the retained representation is

    H_n=Dsc T_n Dsc^(-1),
    (H_n)_(i,j)=(1/(2pi)) integral_(-pi)^pi
          w_n(t) exp(i(j-i)t) dt, 0<=i,j<=2,

where

    w_n(t)=(1+sigma cos t)^n exp(-sigma exp(it)).

The weight is complex. The arguments below use its local limit and absolute tail bounds, not positivity of that weight.

Put

    a0=sigma/(2M0)>0.

For fixed x,

    M0^(-n) w_n(x/sqrt(n))
          -> exp(-sigma) exp(-a0 x^2).             (3)

This convergence is uniform on compact x-sets. The expansion follows from cos t=1-t^2/2+O(t^4), while exp(-sigma exp(it)) tends to exp(-sigma).

For every fixed small epsilon>0, there is eta>0 such that

    |1+sigma cos t|<=M0(1-eta),
        epsilon<=|t|<=pi.

On |t|<=epsilon one has

    |1+sigma cos t|^n<=M0^n exp(-c n t^2)

for some c>0. The remaining exponential factor has bounded modulus on the whole contour. These estimates justify localization at t=0.

## 3. Determinants and cofactors before inversion

For ordered row indices I and column indices J of size r, the integration identity obtained by expanding determinants gives

    det H_n[I,J]
      =1/(r!(2pi)^r) integral
          product_(l=1)^r w_n(t_l)
          det[exp(-i i_a t_l)]_(a,l)
          det[exp(i j_b t_l)]_(l,b)
          dt_1 ... dt_r.                          (4)

This is an algebraic identity for the complex integrals. For r=3 and indices 0,1,2, the two alternating factors have leading product

    n^(-3) product_(a<b)(x_b-x_a)^2

after t_l=x_l/sqrt(n). Indeed each exponential alternant contributes its index Vandermonde divided by 0!1!2!; for indices 0,1,2 that ratio equals one. The conjugate phases multiply to one.

For r=2, retained row indices i1<i2 and column indices j1<j2 give leading product

    (i2-i1)(j2-j1) n^(-1)(x2-x1)^2.

Define positive finite Gaussian integrals

    I_r=integral_(R^r) exp(-a0 sum x_l^2)
                     product_(a<b)(x_b-x_a)^2 dx,

and constants

    C3=exp(-3sigma) I_3/[3!(2pi)^3]>0,
    C2=exp(-2sigma) I_2/[2!(2pi)^2]>0.

Equations (3)-(4) yield

    det H_n=C3 M0^(3n)n^(-9/2)(1+o(1)).            (5)

For the adjugate, the gaps remaining after deleting indices 0,1,2 are 1,2,1. Incorporating cofactor signs, put

    v=(1,-2,1)^T.

Then entrywise, hence in any matrix norm in dimension three,

    adj H_n=C2 M0^(2n)n^(-2)(v v^T+o(1)).          (6)

To justify these limits globally, configurations with at least one |t_l|>=epsilon have an exponentially small weight and bounded alternants. On the remaining cube the alternants vanish on coincident points and obey a constant times the corresponding product of pairwise distances. For the finite integer frequencies used here this follows directly from factoring the Vandermonde in exp(it_l), with the remaining symmetric polynomial bounded. After rescaling, a polynomial times exp(-c sum x_l^2) dominates the integrand. Dominated convergence proves both limits. This also explains why an entrywise rank-one approximation to H_n itself is not being inverted.

In particular det H_n is nonzero eventually. Dividing (6) by (5) gives the rigorous inverse asymptotic

    H_n^(-1)=k_n(v v^T+o(1)),
    k_n=(C2/C3)M0^(-n)n^(5/2)>0.                  (7)

The determinant has a positive real leading constant; its nonvanishing follows without asserting pointwise positivity of the original complex weight.

## 4. The actual reconstruction metric

Direct finite multiplication gives

    (I+Dpol)^(-n)=
      [[1,-n,n(n+1)], [0,1,-2n], [0,0,1]],

and

    Krec=
      [[-1,n,-n(n+1)],
       [1,-n-1,n(n+3)],
       [0,1,-2n-1],
       [0,0,1]].

The positive weights are

    (w0,w1,w2,w3)
       =(1/[n(n+1)(n+2)],1/[n(n+1)],1/n,1).

The first two columns of diag(w_j)Krec tend to zero. Its final column is

    (-1/(n+2), (n+3)/(n+1), -2-1/n, 1)^T

and tends to (0,1,-2,1)^T. Consequently

    G_n -> 6 e2 e2^T.                             (8)

Here e2 is coordinate two in a length-three vector. This limit uses exactly the stated weights and reconstruction.

## 5. Forcing direction and limiting normalized selector

The retained positive forcing-circle identities give

    f0=(n!/(2pi)) integral_(-pi)^pi
                            (1+sigma cos t)^n dt,

and for i=0,1,2 the corresponding polynomial factor is (1+exp(it)/sigma)^i. The same Laplace argument gives

    f0=Cf n! M0^n n^(-1/2)(1+o(1)),
    Cf=1/[2sqrt(pi a0)]>0,
    f/f0 -> fstar=(1,Aplus,Aplus^2)^T.             (9)

The nonsymmetric inverse follows from (7). Define

    r=Dsc^(-1)v=(1,sigma,1/2)^T,
    l=Dsc v=(1,2sigma,2)^T.

Then

    T_n^(-1)=k_n(r l^T+o(1)).                     (10)

The scalar

    B0=l^T fstar=(1+sigma Aplus)^2=(2+sigma)^2

is strictly positive. Equations (9)-(10) give

    xi/(k_n f0) -> B0 r.                          (11)

Thus xi is of order n! n^2, and its final coordinate has a nonzero leading constant. From (8),

    r^T(6e2e2^T)r=3/2>0.

Inserting (8), (10) and (11) into the defining quotient for lambda gives

    f0 lambda -> l/B0.                            (12)

For clarity, the numerator T^(-T)G_n xi divided by k_n^2 f0 tends to B0 l (r^T G_infty r), whereas a_n divided by k_n^2 f0^2 tends to B0^2(r^T G_infty r). Both normalizing constants are nonzero. Thus the small error matrices in (10) are harmless even though their leading matrix has rank one.

All three entries of l/B0 are positive. Therefore the actual rational selector lambda has positive entries eventually. No assertion about primitive coefficient content is needed for this limiting direction.

## 6. Complete logarithmic residual

Retain the exact decomposition

    fQ=(e+pi)fP+eE+eF.

For even n the exact logarithmic integral is

    eF_i=-2n! integral_(-pi/4)^(pi/4)
       (sigma cos t-1)^n
       (1-exp(it)/sigma)^i dt, 0<=i<=2.            (13)

The base sigma cos t-1 is nonnegative on this interval, with unique maximum M0^(-1) at zero. Put

    b0=sigma M0/2>0.

Laplace localization gives

    eF0=-2n! M0^(-n) sqrt(pi/(b0 n))(1+o(1)),
    eF_i/eF0 -> Aminus^i.                         (14)

Combining (9) and (14), using sqrt(a0/b0)=M0^(-1), proves

    eF0/f0=-4pi M0^(-2n-1)(1+o(1)).               (15)

By (12),

    lambda^T eF/(eF0/f0)
       ->(1+sigma Aminus)^2/(2+sigma)^2
       =M0^(-2).                                 (16)

All components here are the complete logarithmic residual, including both conjugate endpoints. Equations (15)-(16) give the leading term in (1).

## 7. Exponential and endpoint terms are retained

The retained complete exponential forcing bound is

    |eE_i|<=27 M0^n sigma^(-i)/(n+1), 0<=i<=2.

Since (12) bounds f0 lambda and (9) supplies f0, it follows that

    |lambda^T eE|=O(1/(n! sqrt(n))).               (17)

For the endpoint term, Cauchy–Schwarz in the positive metric W gives

    |kappa|<=w0/sqrt(a_n).

Equations (8)-(11) imply sqrt(a_n) is asymptotic to a positive constant times n! n^2. Since w0=O(n^(-3)),

    |kappa|=O(1/(n! n^5)).                        (18)

Both bounds are o(M0^(-2n)). The exact identity

    c_n-(e+pi)=kappa+lambda^T eE+lambda^T eF

and (15)-(18) prove (1). In particular no omitted rational correction is being assumed negligible without a bound.

## 8. Arithmetic consequences and limitations

The center is rational by its exact finite construction. Put p_n=q_n c_n, with q_n positive and reduced. Equation (1) implies

    |p_n-q_n(e+pi)|
       =4pi M0^(-3)q_n M0^(-2n)(1+o(1)).

Thus the exact remaining arithmetic quantity is q_n M0^(-2n). In particular:

* A strict upper rate limsup log q_n/n<2log M0 would give nonzero primitive forms tending to zero and would prove irrationality, if established with this theorem and the necessary independent examination.
* A strict lower rate liminf log q_n/n>2log M0 would force divergence for this center.
* Merely log q_n=O(n), or equality of a limiting rate with 2log M0, does not decide the primitive-error behavior.

The previously derived qhigh and normalized S_eff identities remain relevant to q_n. They currently supply necessary content conditions and local gates, not either global rate comparison above. Establishing positivity of the limiting selector is not an arithmetic denominator estimate.

## 9. Verification status

This is a coherent author proof of the new fixed-b=3 signed-error asymptotic. It requires a narrow independent examination of the determinant/cofactor limits, the actual metric normalization, and the complete residual constants before being promoted to the project's independently examined scope. Only Child 4 is designated for such an examination; its currently accepted joint-coordinate research should be preserved. No examination is claimed in this document.

The theorem covers sufficiently large even n for this fixed factorial Gram construction. It does not transfer to growing b, coordinate centers, arbitrary selector combinations or the isolated phase problem of the large-selector family. No unconditional solution of the e+pi problem is claimed.
