> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Complete logarithmic forcing vector: cancellation on a deformed arc

Status: new author paper deduction. No numerical checks or audits were performed. SIGNED_ADJOINT_REMAINDER and its conditional log(2) envelope remain unchanged. Child 3's RATIONAL_CENTER_ASYMPTOTICS.md was read as author data. Its arc construction motivates the derivation below, but no normalized-center theorem is assumed for arbitrary vectors.

## 1. Definitions and result

Write R=sqrt(2), chi=R-1, Q0(z)=1-z+z^2/2, and F(z)=4 arctan(z/(2-z)). For integers n>=16 and 2<=b<=n, define

    eF_i=[z^(n+i)] Q0(z)^n D_z^n((F(z)-pi)/(1-z)),
    0<=i<b,
    D_R=diag((-R)^i).

The new bound is

    ||D_R eF||_2 <= 2 sqrt(pi b/n) n! chi^n.             (1)

It holds throughout this domain, without the additional slow-growth condition or any inverse estimate. In particular it proves the proposed n! chi^n exp(O(b log n+log n)) upper bound on n>=512 b^4 log n, with a much smaller displayed prefactor.

This is a bound on the complete forcing vector, not merely the particular adjoint contraction defining a center. It results from integration cancellation before absolute values. No assertion about the sign of every entry or the actual rate of a full center error is needed.

## 2. Deriving the arbitrary-polynomial identity

Let tau=(1+iy)/2, -1<=y<=1. The complete logarithmic difference quotient gives

    eF_i=-n! integral_-1^1 tau^n/(1-tau)
                  [z^(n+i)] Q0(z)^n/(1-tau z)^(n+1) dy.    (2)

All coefficient extractions and integrals can be interchanged: near z=0 the series converge uniformly on the compact y interval.

Set V(t)=t^2-t+1/2=t^(2)Q0(1/t). For any polynomial L(t)=sum_i lambda_i t^i, coefficient comparison gives

    sum_i lambda_i eF_i
      =-integral_-1^1 P_L(tau)/(1-tau) dy,
    P_L(t)=t^n D_t^n[V(t)^n L(t)].                       (3)

Here lambda is arbitrary, real or complex. There is NO condition lambda^T fP=1.

For completeness write Q0(z)^n=sum_s q_s z^s. For L=t^i, both sides of the polynomial identity underlying (3) equal

    sum_(s<=n+i) q_s (2n+i-s)!/(n+i-s)! t^(2n+i-s).

On the coefficient side this follows from the binomial series for (1-tz)^(-n-1). On the derivative side it follows from V(t)^n=t^(2n)Q0(1/t). Terms whose initial degree is below n differentiate to zero. Thus every factorial displayed has a nonnegative argument. Linearity proves (3) for every L.

The normalization used by Child 3 is relevant to interpreting rational companions and endpoint constants, but is unnecessary for (3). This explicitly establishes the required specialization rather than importing a full-center conclusion.

## 3. Integration by parts and both conjugate endpoints

The roots of V are alpha=(1+i)/2 and its conjugate. V^n L has a zero of order at least n at each endpoint of the integration segment. Therefore all boundary terms in n integrations by parts vanish. Since

    D_t^n[t^n/(1-t)]=n!/(1-t)^(n+1),

and dy=2dt/i, equation (3) becomes

    sum_i lambda_i eF_i
      =(-1)^(n+1)n! integral_-1^1
              V(tau)^n L(tau)/(1-tau)^(n+1) dy.          (4)

There is no endpoint contribution suppressed here: all derivatives of V^n L of orders 0 through n-1 vanish at BOTH endpoints. The pole t=1 is outside the deformation region used next.

Deform the segment to the left arc

    t(theta)=1-R^(-1)exp(i theta), -pi/4<=theta<=pi/4.

The region between the segment and this arc excludes 1. The arc in this theta order runs from the upper endpoint to the lower endpoint, opposite to the original segment. This reversal, together with dy=2dt/i, gives exactly

    sum_i lambda_i eF_i
      =(-1)^(n+1)2n! integral_(-pi/4)^(pi/4)
              h(theta)^n L(t(theta)) dtheta,
    h(theta)=R cos(theta)-1.                            (5)

Indeed V(t)/(1-t)=h(theta), and dt/(1-t)=-i dtheta. These facts account for the factor 2 and orientation in (5).

For real lambda, the values at opposite theta are conjugates. The integral is real and L can be replaced by its real part. Neither endpoint nor conjugate half of the arc is discarded. On the entire arc h>=0 and |t(theta)|<=R^(-1).

Equation (5) holds for arbitrary polynomials. In particular, taking L=t^i gives every individual forcing entry:

    eF_i=(-1)^(n+1)2n! integral h(theta)^n t(theta)^i dtheta.  (6)

## 4. Uniform vector bound

For |theta|<=pi/4, the elementary Taylor bound yields

    1-cos(theta)>=theta^2/2-theta^4/24>=theta^2/3.

Since R/chi=2+R>3,

    h(theta)/chi
      =1-(R/chi)(1-cos(theta))<=1-theta^2<=exp(-theta^2).

The left side is nonnegative. Combining this inequality with |t(theta)|<=R^(-1) in (6) gives

    R^i |eF_i|
      <=2n! chi^n integral_(-pi/4)^(pi/4) exp(-n theta^2)dtheta
      <=2 sqrt(pi/n)n! chi^n.                          (7)

Summing squares proves (1). Signs in D_R do not affect its Euclidean norm.

The improvement is not a pointwise improvement of the old radius kernel. Integration by parts and contour deformation have first combined its signed contributions. Only afterward is the nonnegative arc weight bounded. The old sharp pointwise radius-kernel bound therefore does not obstruct (1).

## 5. A signed vector identity with an explicit bounded remainder

A useful additive statement avoids invoking any unverified relative saddle asymptotic. Define the exact positive scalar

    J_n=integral_(-pi/4)^(pi/4) h(theta)^n dtheta,
    tstar=1-R^(-1),
    vstar=(tstar^i)_(i=0)^(b-1).

Then

    eF=(-1)^(n+1)2n! J_n vstar + rvec.                 (8)

The error has an explicit bound

    ||D_R rvec||_2
      <=[sqrt(pi)/(2 n^(3/2))] n! chi^n
                        sqrt(sum_(i=0)^(b-1) i^4).    (9)

To prove this, differentiate g_i(theta)=t(theta)^i twice. Since |t|,|t'|,|t''|<=R^(-1),

    |g_i''(theta)|<=i^2 R^(-i).

At zero g_i'(0) is purely imaginary. Taylor's theorem applied to the real part therefore gives

    |Re g_i(theta)-tstar^i|<=i^2 R^(-i) theta^2/2.

Insert this in (6), use the Gaussian bound of Section 4, and use

    integral_R theta^2 exp(-n theta^2)dtheta
      =sqrt(pi)/(2 n^(3/2)).

This proves (9), including the factor 2 in (6).

The leading vector is explicit and its coefficient J_n is a known positive scalar integral independent of the center and its adjoint. It is not an unknown error norm. For n>=16 one also has

    J_n>=chi^n/(2 sqrt(n)).                            (10)

Indeed on |theta|<=1/(2sqrt(n)),

    h/chi>=1-c theta^2, c=R/(2chi)<2,

so Bernoulli's inequality gives (h/chi)^n>=1-c/4>1/2. The interval has length 1/sqrt(n) and lies within the arc. In particular eF_0 has sign (-1)^(n+1) and never vanishes.

Equations (8)-(10) are an additive vector approximation. The coarse bound sqrt(sum i^4)<=sqrt(b)(b-1)^2 need not supply a useful relative approximation for every coordinate near the maximum permitted b. No such stronger relative claim is made. The direct norm bound (1) has no such limitation.

## 6. Arbitrary adjoints, exponential forcing, and endpoint constants

For any real adjoint lambda, put

    Jlambda=||D_R^(-1)lambda||_2.

Equation (1) gives the genuine arbitrary-vector estimate

    |lambda^T eF|<=2 sqrt(pi b/n)n! chi^n Jlambda.      (11)

This is a consequence of the newly established vector theorem. It does not assume that lambda arises from a center, and contains no unspecified adjoint norm in place of a forcing estimate.

For the actual fixed weighted B center, retain precisely the earlier notation

    u=K T^(-1)fP,
    v=e0+K T^(-1)fQ,
    a=u^T W u,
    lambda=T^(-T)K^T W u/a,
    c0=u^T W e0/a,
    lambda^T fP=1.

Then the COMPLETE signed center identity remains

    t-(e+pi)=c0+lambda^T eE+lambda^T eF.              (12)

The exponential forcing is still the complete function

    eE_i=-[z^(n+i)] Q0(z)^n
                  integral_0^1 s^n exp(1-s+sz)ds.

Its previously established radius-R contraction bound is retained:

    |lambda^T eE|<=9(1+R)^n Jlambda/(n+1).             (13)

Thus the new complete upper bound at the adjoint level is

    |t-(e+pi)|<=|c0|+
       [2 sqrt(pi b/n)n! chi^n+9(1+R)^n/(n+1)]Jlambda. (14)

Both signs in (12) remain relevant; no assertion of same-sign contributions is made. The endpoint term c0 is not absorbed into the logarithmic integral. No estimate of fP is developed here, since that task belongs to the main agent.

If one uses only the separate author inverse input already recorded in SIGNED_ADJOINT_REMAINDER, namely

    Jlambda<=2Hminus K0/[(1+R)^n sqrt(a)],
    |c0|<=w0/sqrt(a),

then (14) implies

    |t-(e+pi)| <= [w0
       +4 sqrt(pi b/n) Hminus K0 n! (chi/(1+R))^n
       +18Hminus K0/(n+1)]/sqrt(a).                   (15)

These are explicitly conditional propagation statements. They retain the entire exponential forcing and endpoint constant, and use no newly asserted inverse theorem. Formula (15) is not claimed to give a nonzero signed leading term.

## 7. Scope and remaining questions

The proposed logarithmic forcing-vector rate is established by (1), through an entrywise specialization derived from the complete integral and polynomial differentiation identities. It is independent of the choice between a full-coefficient center and a B-only center. That distinction enters only when selecting the actual adjoint in (12).

The new signed identity (8) has the bounded remainder (9), with both conjugate arc halves included. A scalar signed asymptotic for the actual center still requires control of the adjoint evaluation at tstar relative to its remainder, and possible cancellation against the exponential and endpoint terms. No such separation is inferred from lambda^T fP=1.

No reduced-center denominator estimate or rational-center recurrence is attempted. For any complete bound B on |t-(e+pi)|, the primitive center pair still requires both qB and 1/q+qB/2, with q the actual reduced denominator. Each integral lifting multiplier cancels against its own endpoint gcd.

The earlier log(2) envelope remains preserved as a separate result. This note establishes a stronger forcing theorem rather than altering that record. No scans, successful-check replays, or independent reviews were used. No irrationality conclusion follows from the vector theorem alone.

This file and LOGARITHMIC_FORCING_VECTOR_REPORT.md require read-back before completion is reported.
