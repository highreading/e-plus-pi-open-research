> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Quantitative irrationality-measure transfer for rational companions

Status: new main-agent author deduction. The transfer argument below is proved from explicitly stated inputs. Its application to pi requires a sourced quantitative irrationality-measure theorem; that source has not yet been checked in this continuation. No numerical experiment or independent review is claimed. This is a possible branch exclusion, not a solution of the rationality of e+pi.

## 1. An exact transfer inequality

Let alpha and beta be rational, c=alpha+beta, q=den(c), and B=den(beta), with positive reduced denominators. Suppose an explicit positive E satisfies

    |e-alpha|<=E.

Assume constants nu>0, mu>0, C_e>0, C_pi>0 such that every reduced rational a/b satisfies

    |e-a/b|>=C_e b^(-nu),
    |pi-a/b|>=C_pi b^(-mu).

For e, the retained elementary project proof permits nu=2+epsilon for any fixed epsilon>0. The pi inequality is a separate input; irrationality alone does not supply it with a finite exponent.

Since alpha=c-beta, its reduced denominator is at most qB. Therefore

    E>=C_e(qB)^(-nu),
    q>=C_e^(1/nu) E^(-1/nu)/B.                    (1)

The pi input gives

    |beta-pi|>=C_pi B^(-mu).

If

    E <= (C_pi/2) B^(-mu),                         (2)

then the reverse triangle inequality, retaining both components, gives

    |c-(e+pi)|>= (C_pi/2) B^(-mu).

Combining this with (1) proves

    q|c-(e+pi)| >= (C_pi/2) C_e^(1/nu)
                          E^(-1/nu) B^(-(mu+1)).  (3)

The denominator B is the actual denominator of beta. A valid upper bound for B can be substituted on the right. No exact dyadic law or nonvanishing of an oscillatory contour sum is required once (2) follows from the stated approximation bounds.

## 2. Rate form

Let X tend to infinity along any sequence of rational companions. Suppose

    liminf (-log E)/X >= a>0,
    limsup log B/X <= b>=0.

If a>mu b, condition (2) holds eventually. Formula (3) then gives

    liminf log(q|c-(e+pi)|)/X >= a/nu-(mu+1)b.      (4)

For the retained e theorem take nu=2+epsilon and then let epsilon decrease to zero. In particular, the strict condition

    a/2>(mu+1)b                                   (5)

implies (2) and divergence of the primitive errors. The strict inequality is essential; no conclusion at its boundary is asserted.

All rate bounds concern the same indices and the same rational companions. This argument does not interchange coordinate, Gram, and direct-selector centers.

## 3. Application to the saved large-selector formulas

Let n=4k tend to infinity, fix rho>0, and take nonnegative integers

    m=rho n log n+o(n log n).

Define

    Bpoly(t)=(1-2t+2t^2)^n(1-4t+2t^2)^(2m),
    K(t)=t^n Bpoly^(n)(t)/n!, U=K(1),
    T=calL((K-U)/(t-1)), beta=T/U,
    N=2n+4m, Lambda=2n+8m.

Only indices with U!=0 are admitted. Let alpha be the complete rational exponential companion defined in LARGE_SELECTOR_EXPONENTIAL_REMAINDER_DRAFT.md, and c=alpha+beta.

The saved author exponential estimate supplies

    E=3 Lambda^n exp(Lambda/(n+1))
                     /((n+1)(n!)^2 |U|).          (6)

The saved coefficient argument gives 2^(n/2)|U. On nonzero nodes this is a lower bound for |U|. Its Cauchy upper bound is

    |U|<=(4m/n)^(n/2) exp(n+n sqrt(n/m)).

Consequently log|U|=o(n log n), uniformly under the displayed asymptotic allocation, and with X=n log n,

    (-log E)/X -> 1.                              (7)

The moment argument in LARGE_SELECTOR_WEIGHTED_DIFFERENCE_DRAFT.md extends the logarithmic denominator bound to every nonzero U in this domain:

    O_N T belongs to 2 Z,
    den(beta) divides O_N |U|/2,                   (8)

where O_N is the lcm of odd positive integers at most N. This extension is an author deduction, not a claimed independent PASS. Its proof uses v_2(T)>=1 and that every odd moment denominator divides O_N; it does not require the special parity allocation.

Using O_N<=4^N, equations (8) and the bound for U imply

    limsup log den(beta)/(n log n)<=4rho log 4.    (9)

Thus (4), with the pi approximation input retained explicitly, gives

    liminf log(q|c-(e+pi)|)/(n log n)
       >=1/2-4rho(mu+1)log 4,                     (10)

provided the strict dominance condition is satisfied. In particular,

    0<rho<1/[8(mu+1)log 4]                        (11)

implies divergence on every such nonzero-node sequence.

This conclusion, if all inputs are established, covers all nonzero choices in the stated small-rho regime. It does not require selecting a nonzero weighted-difference certificate. It does not cover arbitrary rho, nor establish anything about reconstructed centers with different rational corrections.

## 4. Input status and remaining work

The transfer inequalities (1)-(5) are elementary author proofs given the two rational-approximation inequalities. The exponential estimate, coefficient divisibility, Cauchy bound, and moment-denominator extension are saved author inputs. No new calculation has been performed here.

A finite irrationality measure for pi is a classical external result, but this note deliberately supplies no unchecked numerical exponent or bibliographic detail. Locate an appropriate source in the existing offline materials and verify the exact theorem and its quantifiers before marking (10)-(11) as an established application to pi. For a published upper bound on the irrationality measure, generally use any strictly larger exponent to obtain the uniform constant required here; do not silently substitute the boundary exponent.

If the source is unavailable offline, retain the application as explicitly dependent on that external theorem and continue other authorized research. Do not manufacture a citation or treat ordinary irrationality of pi as sufficient.

Even a completed exclusion of this selector regime would leave the actual irrationality or rationality of e+pi unresolved.
