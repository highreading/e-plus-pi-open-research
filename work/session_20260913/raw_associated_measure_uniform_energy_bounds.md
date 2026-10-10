> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Uniform interior and edge bounds for the actual associated Legendre measure

Date: 2026-09-13. Original continuation by audit_computations; independent review passed in `raw_associated_measure_uniform_independent_review.md`.

This note proves uniform, all-index density bounds for the actual associated
measure in `raw_coupled_pencil_exact_legendre_square.md`. No degree scan or
uniform asymptotic expansion is used. The argument is a two-solution energy
estimate for the Legendre equation, followed by its exact Wronskian identity.
The two-boundary forcing factors of the original coupled system remain in
place; none of the estimates proves the missing mixed zero-count assertion.

## 1. Normalization and statements

Let a>=1, m=a-1, l=2m, k=l+1/2, and

    c_m=alpha_(2m+1) alpha_(2m+2),
    alpha_j=j/sqrt(4j^2-1).

Write P_l for the ordinary Legendre polynomial normalized by P_l(1)=1,
and Q_l^F for its real Ferrers second-kind solution on (-1,1). The
root continuation `raw_associated_measure_legendre_second_kind.md`
(independently reviewed in `raw_associated_measure_second_kind_independent_review.md`)
gives

    w_a(y)=sqrt(y)/{2 c_m^2 (4m+1)
                    [Q_l^F(sqrt(y))^2+(pi^2/4)P_l(sqrt(y))^2]},
    0<y<1.                                                        (1)

This is the density of the probability measure for the infinite Jacobi
tail beginning at index a. In particular the polynomial degree in (1)
is 2(a-1), not 2a. The complex function in the corresponding boundary
formula is Q_l(s+i0)=Q_l^F(s)-i*pi*P_l(s)/2.

Put

    w_free(y)=(8/pi)sqrt(y(1-y)).

The following explicit conclusions hold.

**Interior theorem.** For every m>=1 and 0<y<1,

    |log(w_a(y)/w_free(y))|
       <= 1/(4m^2) + sqrt(y)/(4k sqrt(1-y)).                        (2)

Thus if 1-y>=C^2/k^2, the density ratio is bounded above and below by
exp(1/(4m^2)+1/(4C)) and its reciprocal. This is uniform all the way
to y=0, where both densities vanish. If k*sqrt(1-y) tends to infinity,
the ratio tends to one uniformly on the specified sets.

**Edge theorem.** For m>=1, 0<delta<=k^(-2), and

    L_delta=(1/2)log(1/(k^2 delta)),

one has

    1/[64 k (1+L_delta)^2]
       <= w_a(1-delta)
       <= 576/[k (1+L_delta)^2].                                  (3)

Consequently

    delta/[512 k (1+L_delta)^2]
       <= mu_a([1-delta,1])
       <= 576 delta/[k (1+L_delta)^2].                            (4)

In particular the mass of the width-k^(-2) endpoint layer is bounded
above and below by fixed positive constants times k^(-3). The
logarithm contains k^2 delta. Replacing it by a fixed-index endpoint
logarithm with constants independent of a would lose this shift.

**Integrated theorem.** For every m>=1,

    integral_0^1 |w_a(y)-w_free(y)| dy <= 4/k.                      (5)

All constants are deliberately loose. The m=0 density is given
explicitly in (1), with P_0=1 and Q_0^F=atanh(sqrt(y)); the growing-index
statements (2)-(5) are stated only for m>=1.

## 2. The exact two-solution energy estimate

Set y=cos(theta)^2, 0<theta<=pi/2, and define

    u(theta)=sqrt(sin(theta)) P_l(cos(theta)),
    v(theta)=(2/pi)sqrt(sin(theta)) Q_l^F(cos(theta)).

Substitution in the Legendre equation gives, for both w=u and w=v,

    w''+[k^2+1/(4 sin(theta)^2)]w=0.                               (6)

The underlying Legendre equation and the Wronskian normalization are
recorded in [DLMF 14.2.1](https://dlmf.nist.gov/14.2.E1) and
[DLMF 14.2.4](https://dlmf.nist.gov/14.2.E4), specialized to order zero.
The transformation (6) and all inequalities below are derived here.

Let p_m=P_(2m)(0)=(-1)^m binom(2m,m)/4^m. Parity and the Wronskian

    P_l(x)(Q_l^F)'(x)-P_l'(x)Q_l^F(x)=1/(1-x^2)

give the exact initial data

    u(pi/2)=p_m,      u'(pi/2)=0,
    v(pi/2)=0,        v'(pi/2)=-2/(pi p_m).                         (7)

The signs of p_m and the second initial derivative are retained.
Only their squares enter the singular-value bounds.

For a solution w put z=(w,w'/k)^T. Its coefficient matrix is

    k [[0,1],[-1,0]] + [[0,0],[-q(theta)/k,0]],
    q(theta)=1/(4 sin(theta)^2).

The symmetric part of this matrix has norm q(theta)/(2k).
For any nonzero solution vector,

    |d log ||z||/dtheta| <= q(theta)/(2k).

Integrating backwards from pi/2 shows that the two singular values
of its fundamental transfer matrix are between exp(-I) and exp(I),
where

    I=integral_theta^(pi/2) q(t)/(2k) dt=cot(theta)/(8k).           (8)

Apply this to the initial diagonal matrix in (7), in coordinates
(w,w'/k). If E=u^2+v^2, its value is the squared norm of the first
row of the transferred fundamental matrix. Consequently, with

    A_m=k p_m^2,       B_m=4/(pi^2 A_m),

one obtains

    min(A_m,B_m) exp[-cot(theta)/(4k)]
       <= k E(theta)
       <= max(A_m,B_m) exp[cot(theta)/(4k)].                       (9)

This estimate does not select a phase or discard the second solution.
It is essential to bound the sum P^2+(2Q/pi)^2 rather than either
oscillatory solution separately.

## 3. Exact initial amplitudes and the interior ratio

The elementary factorial formula gives

    A_(m+1)/A_m
      =1+1/[(4m+1)(2m+2)^2].                                    (10)

Thus A_m increases from 1/2 to 2/pi. The limit also follows directly
from Wallis integrals: if I_j=integral_0^(pi/2)sin(t)^j dt, then
I_(2m)=(pi/2)|p_m|, I_(2m+1)=1/[(2m+1)|p_m|], and
I_(2m+2)/I_(2m)=(2m+1)/(2m+2) bounds
I_(2m+1)/I_(2m) between that ratio and one.

For m>=1 let epsilon_m=log[(2/pi)/A_m]. Using log(1+t)<=t in (10),

    0<=epsilon_m
       <= sum_(j=m)^infinity 1/(16j^3)
       <= 3/(32m^2).                                             (11)

The last bound uses the first term and the integral from m to infinity.
Since B_m=(2/pi)exp(epsilon_m), (9) becomes

    exp[-epsilon_m-cot(theta)/(4k)]
       <= (pi k/2) E(theta)
       <= exp[epsilon_m+cot(theta)/(4k)].                         (12)

Also, directly from the two alpha factors,

    1/16<c_m^2<=4/45,
    0<log(16c_m^2)
      <=1/[4(2m+1)^2-1]+1/[4(2m+2)^2-1]
      <=1/(8m^2),  m>=1.                                        (13)

The density normalization (1) gives exactly

    w_a(y)/w_free(y)=1/[8 pi c_m^2 k E(theta)].                   (14)

Combining (11)-(14), using 3/32+1/8=7/32<1/4, proves (2).
This computation also verifies the limiting density's factor 8/pi.

For later edge estimates a slightly looser version, valid even at m=0,
is convenient. Since 1/2<=A_m<=2/pi and
2/pi<=B_m<=8/pi^2, (9) implies

    (1/2)exp[-cot(theta)/(4k)]
       <= k E(theta)
       <= (8/pi^2)exp[cot(theta)/(4k)].                            (15)

## 4. The moving endpoint layer and its logarithmic mass

Assume m>=1, so k>=5/2. Put theta_0=arcsin(1/k) and
x_0=cos(theta_0). On 0<=theta<=theta_0 one has

    1/2<=P_l(cos(theta))<=1.                                     (16)

Here is an elementary uniform justification. The integral formula

    P_l(x)=(1/pi)integral_0^pi
                   (x+i sqrt(1-x^2) cos(phi))^l dphi

gives |P_l(x)|<=1 on [-1,1]. The telescoping Legendre derivative
identity expresses P_l' as the sum of (2j+1)P_j over
j=l-1,l-3,..., so |P_l'|<=l(l+1)/2. Hence

    P_l(x)>=1-[l(l+1)/2](1-x)
           >=1-[k^2/2](1-x)>=1/2,

because 1-x<=1-x_0=k^(-2)/(1+x_0). These identities can also be
obtained from the Legendre generating function in
[DLMF 14.7(iv)](https://dlmf.nist.gov/14.7.iv) by differentiation.

Define T(theta)=Q_l^F(cos(theta))/P_l(cos(theta)). Equation (16)
makes this well defined throughout the layer. At theta_0, (15) and
sin(theta_0)=1/k give

    |Q_l^F(cos(theta_0))|^2<=2 exp(1/4),
    |T(theta_0)|^2<=8 exp(1/4)<16.                               (17)

The Wronskian fixes both the sign and the exact integral:

    T(theta)=T(theta_0)
             +integral_theta^theta_0 dt/[sin(t)P_l(cos(t))^2].     (18)

Let delta=sin(theta)^2 and L=(1/2)log[1/(k^2 delta)], so L>=0.
Since P lies between 1/2 and one, and

    L <= integral_theta^theta_0 csc(t) dt <= L+log(2),

equations (17)-(18) imply

    T(theta)>=L-4,
    |T(theta)|<=4+4(L+log(2))<7+4L.                             (19)

The displayed csc bounds follow from its primitive log(tan(t/2)):
the extra ratio of 1+cos(theta) and 1+cos(theta_0) lies in [1,2].
In particular,

    (1+L)^2/36 <= T(theta)^2+pi^2/4 <=64(1+L)^2.                 (20)

For the lower bound, use pi^2/4 when 0<=L<=8 and
(L-4)^2>=L^2/4 when L>=8. For the upper bound use
(7+4L)^2+pi^2/4<=52(1+L)^2<64(1+L)^2.

Multiplication by P_l^2 in (16) now bounds the denominator in (1)
between (1+L)^2/144 and 64(1+L)^2. Since sqrt(y)>=1/2,
c_m^2<=1/9, and c_m^2>=1/16, equation (1), with 4m+1=2k,
proves the deliberately loose constants in (3).

To integrate the upper bound, L_t>=L_delta for 0<t<=delta.
For a lower bound integrate only over delta/2<=t<=delta; there
L_t<=L_delta+(log 2)/2<(3/2)(1+L_delta). This gives the stronger
lower constant 1/288 in (4), and hence the stated 1/512.

A simpler edge upper bound, useful for integration over the whole
interval, follows immediately from (16):

    w_a(1-delta)<=64/(pi^2 k), 0<delta<=k^(-2).                  (21)

The logarithmic upper estimate (3) improves it deep inside the layer.
The fixed-index failure of comparison with a semicircle at y=1 is
therefore compatible with uniform comparison outside the moving
layer and with a uniformly small total mass of that layer.

## 5. Integrated comparison and exact finite quadrature consequence

On the interior 1-y>=k^(-2), the right side of (2) is at most 1/2.
Thus |exp(t)-1|<=exp(1/2)|t| and

    integral_interior |w_a-w_free|
      <=exp(1/2)[1/(4m^2)+1/(pi k)].                            (22)

Here integral w_free=1 and
integral_0^1 w_free(y)*sqrt(y)/sqrt(1-y) dy=4/pi.
On the omitted layer, (21) and w_free(1-t)<=(8/pi)sqrt(t) give

    integral_edge |w_a-w_free|
       <=[64/pi^2+16/(3pi)]/k^3.                               (23)

For m>=1, k/m^2<=5/2 and k^2>=25/4. Equations (22)-(23) are
bounded by 4/k. For example exp(1/2)<5/3 and pi>3 already give a
coefficient less than 4. This proves (5), including the moving edges.

Consequently, for every bounded measurable test function f,

    |integral f dmu_a - integral f w_free dy|
       <=(4/k)||f||_infinity.                                  (24)

Let theta_j,w_j be the actual r-node Gaussian quadrature in the
Legendre-square note, with its original starting index a. For every
polynomial q of degree at most 2r-1, exactness gives

    |sum_(j=1)^r w_j q(theta_j)
        - integral_0^1 q(y)w_free(y)dy|
       <=(4/k)||q||_[0,1].                                    (25)

This is uniform in the quadrature length r. It is a statement with
the displayed supremum norm; it does not bound high-degree tests
whose own norm grows. Nor does it replace finite quadrature by an
integral for arbitrary rational tests without a further error bound.

## 6. What this does and does not control

The actual associated measure, rather than only an entrywise limit
of the Jacobi coefficients, now has explicit uniform bounds and a
total-variation convergence rate. The boundary logarithmic shift and
mass are controlled even when the starting index grows with the high
block. These conclusions can be used for scalar diagonal quadrature
estimates and for bounded polynomial tests.

The original transfer is still

    B_tilde^T (I+tau J_+)^(-1) B_tilde,
    B_tilde=D M^(-1/2) B.

Both endpoint factors are retained. Its off-diagonal quadrature
weights contain the product of the first and last eigenvector
components and alternate in sign for r>=2. Passing from (25) to
those tests must keep the actual degree-(r-1) endpoint polynomial,
its normalization, and any growth of its supremum norm. No
constant-sign cross measure, mixed zero bound, high-row rank theorem,
primitive shrinking estimate, or irrationality conclusion is inferred.

The next concrete analytic question is a bound on that actual endpoint
polynomial observable, or on the exact polynomial cancellation of
the coupled forcing, using (2)-(4) with both boundary factors present.
