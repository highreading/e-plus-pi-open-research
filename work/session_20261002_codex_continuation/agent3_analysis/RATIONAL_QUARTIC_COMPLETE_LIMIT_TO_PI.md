> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Complete limit of the actual rational quartic two-row projection

Agent 3, 2026-10-02. Original analytic author theorem, not an independent audit. Selector owns the construction's primitive arithmetic. This theorem concerns its EXACT F,wF projection and complete e+pi error, and does not concern rationality of e+pi.

## 1. Outcome and actual construction

Let n=4k->infinity, h>=1 an integer with h/n->infinity. Use precisely the construction of selector's RATIONAL_MULTIPLIER_PERIOD_GATE.md:

    V(w)=w^2-w+1/2,
    G(w)=(1-2w^2)(1+4w^4),
    F_i(w)=w^i (2V(w))^n G(w)^h/[w^(n+1)(1-w)^(4h)], i=0,1.

Define the ACTUAL responses

    r_(j,i)=Res_(w=j) F_i, j=0,1,
    R_i=r_(0,i)-r_(1,i),
    A_i=Res_1(e^(w-1) F_i), B_i=Res_0(e^w F_i),
    L_i=A_i-R_i, T=(4h-1)!,
    F=T(L_1 F_0-L_0 F_1),
    U=T(A_1 R_0-A_0 R_1).

The complete rational approximants are alpha=-B(F)/U and beta=-4 Im P(a)/U, with a=(1+i)/2 and the actual rational Hermite primitive P. Then

    U>0 eventually,
    alpha -> 0, beta -> pi,
    c=alpha+beta -> pi,
    (e+pi)-c -> e>0.                                     (1)

Thus this projection is normal eventually in the large-h regime, but its complete e+pi error does NOT shrink. Its exact coefficient-one e+pi identity is preserved; the exponential contour term, divided by U, tends to e rather than zero.

For h=kappa n log n+O(n), kappa>0, the stronger error statement below is

    c-(e+pi)=-e+O(exp[-kappa log(29/16)n log n
                                      +o(n log n)]).     (2)

Both pole responses, the full exponential companion, and the full vertical segment with BOTH endpoint contributions are retained. The theorem is independent of the selector's dyadic binomial gate. Its final denominator remains the selector's exact reduced denominator; no raw projection clearer is substituted for it.

## 2. Archive and fresh primary-source checks

Before deriving this target, archive searches covered period-preserving rational quartic kernels, F,wF, the 4h pole, the old polynomial quartic kernel and its complete exponential error. The actual source RATIONAL_MULTIPLIER_PERIOD_GATE.md Sections 2--4 and QUARTIC_ENDPOINT_MULTIPLIER_TARGET.md were read. The latter has a polynomial kernel and cannot supply the exponential normalization for the rational two-pole projection. The former leaves its determinant and complete errors open. Other archive hits use polynomial selectors or different contour weights. This is a bounded overlap assessment, not a global novelty claim.

Fresh primary queries included `site:arxiv.org Hermite Pade rational kernel arctangent exponential contour saddle endpoint`, `site:arxiv.org rational quartic weight orthogonal polynomials saddle point beta integrals`, and `site:arxiv.org Toeplitz Hankel saddle determinants endpoint asymptotics 2024 2025`. Opened the full Gharakhloo--Its 2025 structured-determinant paper https://arxiv.org/pdf/2509.12345, the full Hermite--Pade paper https://arxiv.org/html/1502.06695, the current fixed-parameter saddle record https://arxiv.org/abs/2407.04852, and the full rational-reduction primary papers https://arxiv.org/pdf/1805.03445 and https://arxiv.org/pdf/1404.5069. Their determinant, saddle and Hermite-reduction methods are credited background. No determinant theorem for a different symbol is imported. The proof here is a direct scalar saddle calculation and an exact two-variable covariance identity for the actual responses.

## 3. A full contour with one real saddle

Put s=w-1. An exact expansion gives

    G(1+s)=-P_6(s),
    P_6(s)=5+36s+98s^2+144s^3+116s^4+48s^5+8s^6,
    H(s)=(1+2s+2s^2)/(1+s).

Every coefficient of P_6 is strictly positive. Define

    mu_P(s)=s P_6'(s)/P_6(s), mu_H(s)=s H'(s)/H(s).

The derivative d mu_P/d log s is the variance of a random variable on {0,...,6}, with probabilities proportional to its positive coefficients times s^j. It is strictly positive. Since mu_P(0)=0, mu_P(infinity)=6, there is a unique positive sigma satisfying mu_P(sigma)=4. Also mu_P(1)=1416/455<4 and mu_P(3)>4, so 1<sigma<3. Its defining polynomial is

    4sigma^6+12sigma^5-36sigma^3-49sigma^2-27sigma-5=0.

For lambda=n/h->0, the implicit function theorem gives a real sigma_n->sigma, uniformly separated from 1 and 3, satisfying

    mu_P(sigma_n)+lambda mu_H(sigma_n)=4.

Set

    v_n=sigma_n d/ds[mu_P(s)+lambda mu_H(s)]_(s=sigma_n)>0,
    Z_n=P_6(sigma_n)^h H(sigma_n)^n sigma_n^(-4h).

The v_n are bounded away from zero and infinity. Since the coefficient of s^4 in P_6 is 116,

    P_6(s)/s^4>=116 for every s>0.                       (3)

Moreover H(sigma_n)>1 eventually. These elementary lower bounds are sufficient; no optimized saddle constant is needed.

Use the positively oriented circle |s|=sigma_n. Because sigma_n>1, it encloses BOTH poles w=0 and w=1. There is no attempt to compute a one-pole residue on a contour crossing the other pole without adding that residue. On this full contour define

    I_i=(1/(2pi i))oint F_i(w)dw=r_(0,i)+r_(1,i),
    C_i=(1/(2pi i))oint e^(w-1)F_i(w)dw
                                      =e^(-1)B_i+A_i.  (4)

The exact conversion back to the actual selector responses is therefore

    R_i=2r_(0,i)-I_i,
    A_i=C_i-e^(-1)B_i.                                  (5)

No pole or exponential endpoint term has been discarded.

The scalar saddle calculation on this circle gives

    I_0=(-1)^h Z_n sigma_n/(1+sigma_n)
                    /sqrt(2pi h v_n) (1+o(1)),
    I_1/I_0=1+sigma_n+o(1),
    C_0/I_0=e^(sigma_n)+o(1),
    C_1/I_0=(1+sigma_n)e^(sigma_n)+o(1).                 (6)

For completeness, strict positivity of the P_6 coefficients implies |P_6(sigma_n e^(i theta))|<P_6(sigma_n) for every theta !=0 modulo 2pi. The support contains consecutive integers, so no second equality arc occurs. On a fixed neighborhood of theta=0, the real phase curvature is v_n, with h-scaled cubic terms uniformly bounded. The H factor has no zero or pole on any of these circles: its zeros have modulus 1/sqrt2 and its pole has modulus1. Its global contribution is exp(O(n)), and its local log-modulus correction is O(n theta^2). Since n/h->0, the P_6 angular gap controls the full phase uniformly. Restricting to |theta|<=h^(-2/5) makes the cubic exponent o(1); outside it the Gaussian tail is exp(-c h^(1/5)), and fixed remote arcs are exp(-c h+O(n)). The real positive saddle amplitudes in (6) follow by conjugation symmetry. These observations justify (6) uniformly for any sequence h/n->infinity, not just a fixed kappa n log n ray.

## 4. The determinant requires a covariance calculation

The first-order expressions in (6) cancel inside the determinant. They alone would NOT establish normality. Let dmu(s)=F_0(1+s) ds/(2pi i) on the same full circle. An exact symmetrization gives

    C_0 I_1-C_1 I_0
      =1/2 doubleoint (e^s-e^t)(t-s) dmu(s)dmu(t).        (7)

At the two central angles theta,phi,

    (e^s-e^t)(t-s)
      =e^(sigma_n) sigma_n^2(theta-phi)^2
                            [1+O(|theta|+|phi|)].        (8)

The factorization is uniform even when theta=phi: divide each difference by s-t and use its analytic divided difference. Both circle phase factors have the same (-1)^h sign, whose square is positive. The two Gaussian variables have variance 1/(h v_n), so their squared difference has mean 2/(h v_n). Equations (7)-(8), with the same tail bounds as above, prove

    C_0 I_1-C_1 I_0
      =e^(sigma_n) sigma_n^2 I_0^2/(h v_n) (1+o(1)).     (9)

Thus the determinant's real leading term is strictly POSITIVE. The leading size is not obtained from an absolute-value ensemble or by asserting a nonzero difference of two equal leading saddle moments.

## 5. Keeping the actual pole-zero responses

Choose a small circle |w|=r with r=n/(8h)<1/4 eventually. Since G(w)=1+O(w^2), 2V(w)=1+O(w), and (1-w)^(-4h) has log-modulus at most 8h r, Cauchy's estimate gives, for i=0,1,

    |B_i|+|r_(0,i)|
      <=exp[n log(8h/n)+O(n+n^2/h)]
      =exp[o(h)].                                       (10)

The optional e^w factor is bounded on that circle. This estimates the COMPLETE pole-zero residues rather than their first Taylor coefficients. From (3) and (6), |I_0|>=exp[h log116+o(h)], so every correction to (9) introduced by (5) is exponentially small relative to I_0^2/h. Consequently the actual response satisfies

    U/T=e^(sigma_n) sigma_n^2 I_0^2/(h v_n) (1+o(1))>0. (11)

Equivalently,

    U/T=e^(sigma_n) sigma_n^4 Z_n^2
              /[2pi h^2 v_n^2(1+sigma_n)^2] (1+o(1)).  (12)

The factorial multiplier T in the integer projection has been retained in (11)-(12); it cancels only when forming the actual center quotient.

Also L_i=O(|I_0|), by (5)-(6) and (10). Hence the ACTUAL exponential numerator obeys

    |alpha|=|L_1 B_0-L_0 B_1|/|U/T|
             <=exp[-h log116+o(h)] ->0.                 (13)

It follows exactly, without estimating e indirectly, that the projected complete exponential error is e-alpha->e. The new pole at1 has changed the normalization regime.

## 6. Complete logarithmic error, with both endpoints retained

Let C be the ENTIRE vertical segment from bar(a) to a and put J_i=-2i int_C F_i(w)dw. Hermite reduction with the specified continuous endpoint branches gives exactly

    pi-beta=(L_1 J_0-L_0 J_1)/(U/T).                    (14)

Both endpoint logs, whose increments are +i pi/2 at0 and -i pi/2 at1, are the inputs to (14). Along C, |w| and |1-w| lie between1/2 and1/sqrt2, and |2V(w)/w|<=1. Also

    |1-2w^2|<=2, |1+4w^4|<=2,
    |G(w)/(1-w)^4|<=64.

The whole segment has length1. Thus

    |J_0|<=4*64^h, |J_1|<=2*64^h.                     (15)

This elementary full-contour bound suffices; it does not remove either conjugate endpoint, and does not require repeating the old quartic Bernstein certificate. Equations (11), (14)-(15) give

    |beta-pi|<=exp[-h log(116/64)+o(h)]
              =exp[-h log(29/16)+o(h)] ->0.             (16)

Together (13),(16) prove (1)-(2), with eventual complete sign c-(e+pi)<0. An optimized logarithmic saddle or oscillatory phase is unnecessary to identify this nonshrinking complete error: the exponential component already tends to e, whereas the logarithmic component tends to zero.

## 7. Scope

The proof supplies actual determinant nonvanishing, a complete signed error limit, and an infinite large-h regime for this specified period-preserving rational quartic projection. It does not disprove the construction algebra, the selector's dyadic q identity, other rational multipliers, or the possibility of a different finite-ratio h/n regime. It says that h~kappa n log n in this exact F,wF projection approaches pi and therefore cannot provide a shrinking primitive form for e+pi, regardless of its reduced denominator. No conclusion about rationality of e+pi is drawn.
