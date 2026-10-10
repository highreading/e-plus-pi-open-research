> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Obstruction to the current growing-degree bounding criterion

Status: main-agent paper deduction, pending independent audit. This corrects the interpretation of GROWING_CONTENT_CRITERION_DRAFT.md and the residual target in GROWING_FACTORIAL_CONTENT_DRAFT.md. It does not exclude the actual growing-degree construction.

## 1. The chosen upper bounds cannot certify shrinking

Use b=floor(n/2), the monic cofactor normalization Y=-D_V, and the explicit positive bounds in agent3/GAUSSIAN_VANDERMONDE_BOUND.md. The actual endpoint determinants satisfy |D_V|<=B_V, |D_W|<=B_W, and |T|<=B_T.

Put A_n=(20/9)^(n+1). The chosen special-row bounds are

    M_V=A_n (n+1)^2 64^n/2,
    M_W=A_n [20/19+2(n+1)^2 64^n].

Therefore, exactly,

    M_W=4M_V+(20/19)A_n>4M_V.

The expressions B_V and B_W have identical remaining positive factors: the same dimension b, high-row product, divided-difference factor, contour radius, reference polynomial, Gaussian factor, and integration factorial. Consequently

    B_W/B_V=M_W/M_V>4.

On the domain D_V!=0, the actual positive reduced denominator q is an integer and q>=1. Thus

    q(B_W+B_T)/|D_V|
      >=q B_W/B_V
      >4q>=4.

This expression cannot tend to zero on any unbounded nonzero-endpoint set. The argument requires no estimate of the endpoint gcd and no assertion about its growth.

The actual primitive form only satisfies an upper inequality involving this expression. A lower bound on the upper-bound expression is not a lower bound on the actual form. The conclusion is confined to these chosen bounding expressions.

## 2. The strict leading content target is unattainable

Retain the proposed exact clearer

    F=(2n+1)!,
    rho_plus=product_{l=1}^{b-1}(2n+2l)!,
    M=2^(2n+3) F^2 rho_plus.

The integrality and precise scale of MX,MY are under independent review. Assuming that proposed clearing statement is valid, define

    g=gcd(|MX|,|MY|)

on Y!=0. Since MY is a nonzero integer,

    1<=g<=|MY|=M|D_V|<=M B_V.

The explicit estimates proposed in the combined criterion give

    log M=(5/4)n^2 log n+O(n^2),
    log B_V=-(1/2)n^2 log n+O(n^2).

These estimates concern one fixed positive contour parameter lambda and R=lambda n. Hence

    log g<=(3/4)n^2 log n+O(n^2),
    limsup log g/(n^2 log n)<=3/4.

The earlier strict sufficient hypothesis liminf log g/(n^2 log n)>3/4 therefore cannot hold on an unbounded nonzero-endpoint set. Its logical implication remains sufficient but is vacuous under these same endpoint bounds.

Similarly, put A_b=product_{j=0}^{b-2}j!, with the empty product equal to one. Since

    log(A_b^2)=(1/4)n^2 log n+O(n^2),

one obtains

    limsup log(g/A_b^2)/(n^2 log n)<=1/2.

Thus the proposed strict residual target above 1/2 is also unattainable. Interpreting g/A_b^2 as an integer still requires the separate divisibility audit. This correction does not refute the proposed automatic divisor A_b^2 or Agent 1's exact minor identities.

If the proposed clearer is found incorrect, the original content criterion requires a separate normalization repair; that would not affect the obstruction in Section 1.

## 3. A useful replacement formulation

Whenever the proposed exact clearing identity is valid, define the nonnegative endpoint-normalization loss

    delta_n=log(M B_V/g)
           =log(q B_V/|D_V|)>=log q>=0.

For any genuinely improved nonnegative bounds Bhat_W and Bhat_T on the complete remainder determinants, the exact primitive-form identity gives

    |L_n|<=exp(delta_n) (Bhat_W+Bhat_T)/B_V.

A sufficient quantitative target is therefore

    delta_n+log((Bhat_W+Bhat_T)/B_V)->-infinity,

together with endpoint and full-remainder nonvanishing on the same unbounded index set. If the improved numerator bound is zero, it cannot establish a nonzero remainder and that case must be handled separately.

The current choices have (B_W+B_T)/B_V>4 and cannot meet this target. Productive continuation requires sharper control of the actual projection remainder, cancellation between the complete remainder determinants, or another approximation construction. Increasing an endpoint gcd alone cannot rescue the current bounds.

No replacement shrinking estimate, growing-degree nonvanishing theorem, or rationality/irrationality proof is established here.

## 4. Required review and record correction

The combined review should check the exact equality of the common positive factors in B_V and B_W, the direction of every inequality, the scale-specific definition of g, and the uniformity of the logarithmic estimates. The arithmetic review should continue to assess valid divisibility claims independently of the now-unattainable strict target. The endpoint-nonvanishing work remains relevant.

Earlier drafts are preserved as research history. Their strict content thresholds must not be treated as viable remaining objectives without addressing this obstruction.
