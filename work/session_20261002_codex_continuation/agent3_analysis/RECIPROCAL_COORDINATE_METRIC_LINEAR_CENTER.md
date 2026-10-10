> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# An actual positive rational metric that makes the center linear

Agent 3, 2026-10-02. Original author deduction, not independently reviewed. This is a new metric on the same complete B lift. It does not alter the original canonical factorial metric, and no comparison of the two actual reduced denominators is claimed.

Fix 0<c<1/1000 and b/n->c. The complete actual lift Psi=[u,v], its least common denominator d_B, and primitive integer columns U,V are exactly those of PROPORTIONAL_PRIMITIVE_CENTER_INTERFACE.md:

    u=U/d_B, v=V/d_B, gcd(all entries of [U,V])=1,
    u(1)=0, v(1)=1.

All coordinate errors, including the full exponential companion and the coefficient-zero endpoint term, are governed by PROPORTIONAL_ACTUAL_CENTER_SIGNED_RATE.md and PROPORTIONAL_METRIC_LEADING_EQUIVALENCE.md.

## 1. Target and source checks

Pre-target archive queries included reciprocal coordinate weights, negative polynomial evaluations, B(-1), u(-1), v(-1), metric linearization and signs with weights. They were run first across the October 1 and current sessions and then across archive Markdown, excluding repetitive historical author notes. The closest papers are agent2/PRECONDITIONED_RECONSTRUCTION_REPORT.md (compatible factorial norms), agent4/RATIONAL_CENTER_ARITHMETIC.md (exact Gram content), the current relative-coordinate theorem and root's GRAM_RESULTANT_CROSS_PRODUCT_REDUCTION.md. None of the searched material supplies this reciprocal-coordinate positive metric and its exact linear reduced-denominator formula. This is a bounded overlap assessment, not a global novelty claim.

Primary queries included `Hermite Pade positive weights rational denominator`, `rational approximation Gram reciprocal weights`, `Toeplitz determinant characteristic polynomial saddle asymptotics varying weight 2024`, `Hankel Smith normal form factorial`, and `Hermite Pade factorial common divisor`. Opened the full primary papers https://arxiv.org/html/1502.06695 and https://arxiv.org/pdf/1704.03539, the current structured modular Smith paper https://arxiv.org/pdf/2607.05800, and Blackstone--Charlier--Lenells' Toeplitz paper at https://doi.org/10.1017/prm.2023.73 . Their determinant, structured-content and rational weight methods are related background. The last Toeplitz theorem assumes equilibrium supported on the whole circle and is not imported into our short-arc oscillatory model. The deduction below is elementary once the already established actual coordinate signs are available.

## 2. Exact positive rational construction

The complete proportional saddle result gives, uniformly in 0<=j<=b,

    sign(u_j)=epsilon_n(-1)^j, epsilon_n=(-1)^(n+b),
    u_j != 0,                                             (1)

eventually. This follows from u_j=(-1)^n P_j/D, D>0, and sign(P_j)=(-1)^(b-j). In particular it is a sign statement for the ACTUAL coordinates, rather than just for the highest-coefficient reconstruction model.

Set the rational positive diagonal metric

    W*_jj=1/|U_j|.                                        (2)

It is determined entirely by the rational lift, without using S=e+pi or its approximation error. Multiplication of all weights by a common scalar has no effect on the center. Direct substitution gives

    u^T W* u=d_B^(-2) sum_j |U_j|,
    u^T W* v=d_B^(-2) epsilon_n sum_j (-1)^j V_j.

Since sum_j |U_j|=epsilon_n U(-1), the center is EXACTLY

    c*=v(-1)/u(-1)=V(-1)/U(-1).                           (3)

Both the exponential companion and the v_0 endpoint term occur in V(-1). The alternating signs ensure U(-1)!=0 and prevent any real cancellation in its value.

More generally, for any positive rational t the metric

    W*(t)_jj=t^j/|U_j|

is positive and yields the exact center V(-t)/U(-t). The parameter may depend arbitrarily on n. Integer t>=1 introduces no evaluation denominator; a rational t=a/h must retain the homogeneous evaluation scale h^b before primitive reduction.

If the implementation requires each rational metric coefficient to be a sum of squares of rational reconstruction weights, (2) admits that form without approximation. Write |U_j|=a_j1^2+...+a_j4^2 by the four-square theorem. Then W*_jj=sum_l(a_jl/|U_j|)^2. Thus at most four rational copies of each coefficient row realize exactly the same positive rational Gram metric. Zero copies may be omitted. A demand for a SINGLE rational square on every diagonal would be an additional restriction not satisfied automatically by (2).

## 3. Exact forced Gram gcd and primitive denominator

Put R=lcm_(0<=j<=b)|U_j|. Clearing the new metric gives integer coefficients C_j=R/|U_j|, with

    A*=sum_j C_j U_j^2=R epsilon_n U(-1),
    H*=sum_j C_j U_j V_j=R epsilon_n V(-1).

Therefore the ENTIRE metric clearer R is a forced Gram factor:

    gcd(A*,|H*|)=R gcd(|U(-1)|,|V(-1)|).

After it cancels, the ACTUAL reduced denominator is

    q*=|U(-1)|/g*,
    g*=gcd(|U(-1)|,|V(-1)|).                              (4)

This is a structural linearization of a quadratic contraction on the same lift. It does not credit a raw clearer as arithmetic gain: the very large R is removed exactly from numerator and denominator. It changes the remaining contraction from quadratic to linear. It also does not assert g*=1 or substitute d_B for q*.

## 4. Complete actual error and reduced content budget

Equation (3) is a positive convex average of the coordinate centers:

    c*=sum_j |u_j| c_j / sum_j |u_j|.

The all-coordinate relative theorem therefore yields

    (c*-S)/(c_b-S)->1,
    sign(c*-S)=(-1)^(n+1),
    -log|c*-S|/n -> tau_c=(2+c)log(1+sqrt2).               (5)

The same statements hold for ANY n-dependent positive rational t in Section 2, since the convex weights are t^j|u_j|. No complex ensemble has been replaced by its modulus in this deduction; (5) uses the complete actual error theorem as proved.

At t=1 the intrinsic numerator height in (4) has the smaller scale

    log|U(-1)|=log d_B+(n+b-1)log n+O(n).                  (6)

Indeed the established uniform coordinate formula gives |u_j|=C_n B_j times a uniformly bounded positive factor, with log C_n=log n!+O(n). Here B_0=sigma^(-d)(n)_d, d=b-1. The sum of the reference B_j has the exact identity

    sum_j B_j=2 sigma^(-d) E_(X~Gamma(n,1))(X+1)^d.

This is obtained by evaluating (t-1)(1+D)^(-n)t^d at t=-1 and using its known alternating coefficient signs. Expansion of (X+1)^d gives

    2B_0 <= sum B_j <= 2B_0(1+1/n)^d <= 2e^(d/n)B_0.

Thus log|u(-1)|=log n!+log B_0+O(n)=(n+b-1)log n+O(n), proving (6). The canonical factorial Gram height was 2log d_B+2(n+b)log n+O(n); the new remaining scalar height is linear rather than quadratic. This statement compares proved intrinsic scales, not the as-yet-unknown final gcds.

For this new primitive form, a sufficient arithmetic target is

    limsup log q*/n < tau_c.

Equivalently one needs g* to cancel log d_B+(n+b-1)log n down to that linear n budget. Under that unproved hypothesis, q*|c*-S|->0, and the same explicit Bezout pair from the primitive interface has both complete primitive forms shrinking. The required cancellation has not been established, so neither an irrationality proof nor a favorable final denominator rate is claimed.

## 5. The next denominator mechanism to examine

The negative-evaluation metric supplies an actual arithmetic parameter t, preserving the complete signed exponential rate for every positive rational choice. The next question is whether common roots of the two INTEGER polynomials U and V modulo prime powers can force g*(t), with the evaluation-height cost and ALL column contents retained. The parameter's effect must be studied on the actual companion V, whose endpoint value is V(1)=d_B. A congruence for a pure logarithmic companion alone is insufficient. No generic short positive lattice-vector assumption is used.
