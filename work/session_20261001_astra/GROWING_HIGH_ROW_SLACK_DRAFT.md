> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# High-row slack in the revised projection-remainder bounds

Status: main-agent proof draft. The source normalization has now been inspected directly. Independent review of this deduction and the revised remainder estimate is pending. This concerns specified bounding expressions, not growth or failure of the actual approximants.

## 1. Definitions actually present in the revised source

Source: agent2/ACTUAL_PROJECTION_REMAINDER.md, especially Sections 3–7. Its report has also been read.

Let n>=2 and 1<=b<=n. Use the monic cofactor normalization Y=-D_V and the positive reduced endpoint denominator q. Put

    rho=1/20,
    N_b=(b-1)(b-2)/2,
    H_b=(3/4)^N_b.

The source explicitly retains this H_b. Its revised positive expressions are

    B_V^sharp=K_b(R) M_V^sharp,
    B_W^sharp=K_b(R) M_W^sharp,

where K_b includes H_b, and all other common factors are identical. For every common R>20, it states

    |D_V|<=B_V^sharp,
    |D_W|<=B_W^sharp,
    |T|<=B_T^sharp,
    B_W^sharp/B_V^sharp=(37/67)epsilon_n.

The scalar estimates in Section 4 are

    epsilon_n>=2 exp(-s)s^n,
    s=(sqrt(2)-1)^2,
    tau=-log s=2log(1+sqrt(2)).

These source claims are under separate independent audit. Unlike the earlier unsaved observations, the presence of H_b is no longer an assumption about an unread document.

## 2. A smaller valid endpoint majorant

On the same disk, the established recurrence estimates give

    |p_(k+1)/p_k|
      <=11/20+(1/12)/(9/20)
      =397/540
      <3/4.

For the high function p_(n+l)/p_(n+1), the product contains l-1 adjacent ratios. Thus its row majorant can be replaced by

    (397/540)^(l-1).

There are high rows l=1,...,b-1. Their product is

    Hhat_b=(397/540)^N_b
          =(397/405)^N_b H_b.

The determinant bound depends multiplicatively on these row majorants. Keeping its reference polynomial, disk, contour, special V row, divided-difference factors, Gaussian factor, and integration factorial unchanged therefore proves

    |D_V|<=Bhat_V,
    Bhat_V=(397/405)^N_b B_V^sharp.

This is another upper bound for the actual endpoint determinant. It does not infer a determinant lower bound from row estimates. The empty products at b=1 and b=2 are harmless.

## 3. Consequence for the source's normalization loss

On D_V!=0, define exactly as in the source

    delta_n^sharp=log(q B_V^sharp/|D_V|).

Since q>=1 and the smaller endpoint majorant is valid,

    delta_n^sharp>=log q+N_b c,
    c=log(405/397)>0.

For b=floor(n/2), N_b=n^2/8+O(n). Hence this particular delta_n^sharp has an unavoidable positive quadratic lower bound. The source's proposed condition delta_n^sharp-tau n -> -infinity cannot hold in that regime.

This corrects the interpretation of the remaining loss in the revised source. The scalar-preserving remainder identity can still be correct and useful. Its removal of the earlier factor-four obstruction does not remove accumulated slack in the common high-row majorants.

## 4. Direct lower bound for the revised bounding expression

Let

    S_bound=q(B_W^sharp+B_T^sharp)/|D_V|.

Every quantity used in the following denominator comparison is positive. Therefore

    S_bound>=q B_W^sharp/Bhat_V
           =q (405/397)^N_b (37/67)epsilon_n
           >=(74/67)exp(-s) q exp(c N_b-tau n).

In particular,

    log S_bound>=log q+c N_b-tau n+log(74/67)-s.

For b=floor(n/2), this tends to positive infinity on every unbounded nonzero-endpoint set. The companion term was not dropped from the actual remainder: its positive upper bound was simply unnecessary for this lower bound on S_bound. No asymptotic estimate for B_T^sharp/B_W^sharp is needed.

More generally, for an integer sequence 1<=b(n)<=n, the same expressions cannot certify shrinking if

    liminf b(n)^2/n > 2tau/c.

Indeed b tends to infinity under this hypothesis and N_b=(b^2/2)(1-3/b+2/b^2). It includes every regime sqrt(n)<<b(n)<=n. The argument permits any common radius R>20 at each index because the factors compared above cancel exactly.

No conclusion is drawn for the complementary parameter regimes from this inequality alone.

## 5. Exact arithmetic interpretation and limits

The previously reviewed endpoint clearer gives delta_n^sharp=log(M B_V^sharp/g). Thus the same argument gives the stronger, scale-specific ceiling

    g<=M Bhat_V=M B_V^sharp exp(-c N_b).

An endpoint gcd cannot overcome this gap while these exact bounding expressions are retained. The already rejected strict leading content target above 3/4 remains rejected.

However, S_bound is an upper-bound expression for the primitive form, not the primitive form itself. A lower bound for S_bound proves neither divergence nor nonvanishing of the actual form. This note does not exclude the actual growing-degree construction.

Nor does it prove failure of a newly rebuilt estimate using different high-row normalization or joint determinant information. Merely substituting the smaller constant removes the particular factor identified here; it does not establish adequate determinant conditioning or a successful shrinking estimate.

A productive continuation should cancel the common high-row contribution in an exact determinant quotient, or estimate that quotient directly, while retaining the complete companion determinant and actual reduced denominator.

## 6. Verification requirements

Check the source's precise definitions, the valid recurrence domain, the multiplicative dependence on row bounds, the scalar lower estimate, and every inequality direction. The rational constants can be checked exactly. Such a check does not independently verify the analytic source or prove a nonvanishing theorem.
