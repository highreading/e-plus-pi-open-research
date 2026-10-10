> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Two-dimensional remainder report

New paper result, with no numerical sweep or frozen-control recomputation. The superseded factorial-kernel audit remains unfinished and its materials are preserved.

For contact M=2n+b and caps (n,b,n), the exact reduced constraints are

    ell_x(p_(n+l))=0, 1<=l<=b-2,
    (evec+ell(V_n)) dot x=0.

The missing row is l=b-1. The solution space has dimension at least two; exact dimension and normality remain Child 3's responsibility. The complete remainder is the linear functional R(1)=ell_x(W_n). Every retained high row can be subtracted exactly: ell_x(W_d)=R(1) and ell_x(V_d)=-Y for n<=d<=n+b-2.

For every vector and every n+1<=k<=n+b-1,

    R(1)=[ell_x(p_k/(1-t))+v_k Y]/p_k(1).

For Y!=0 this decomposes R/Y into an actual exponential companion E_k=e-T(p_k) dot x/[p_k(1)Y] and the fixed pi error v_k/p_k(1). The latter has sign (-1)^k. In particular,

    (-1)^n E_(n+1)=epsilon_(n+1)+(-1)^n R/Y.

This specifies the sign and amplitude required for cancellation, rather than assuming that the two errors cannot cancel.

The new quantitative gain uses the first TWO retained high rows, so b>=4. Put k=n+1, L_k=||p_k||_1, b_k=p_(k+1)(1)/p_k(1), and delta_k=p_(k+1)'(1)/p_(k+1)(1)-p_k'(1)/p_k(1). A recurrence proof gives 1<=delta_k<=2 and 1/2<=b_k<=2/3. The explicit positive rational subtraction coefficients

    c_1=1+1/delta_k, c_2=1/(b_k delta_k)

make p_k-(1-t)(c_1p_k+c_2p_(k+1)) divisible by t^2. The quotient has coefficient norm at most (101/9)L_k. Therefore

    |ell_x(p_(n+1)/(1-t))|
       <=(101e/9)L_(n+1) sum_j |x_j|/(n+3-j)!.

The first high row alone gives the same coefficient estimate with constant e and denominator (n+2-j)!. The new bound is at most 101/[9(n+3-b)] times that one-row bound. It is strictly smaller for b=floor(n/2), n>=18, with an additional O(1/n) saving and no extra conditioning factor. This comparison does not divide upper bounds to estimate an actual quotient. No comparison with an independently optimized G_lambda norm is asserted.

For an integer triple, divide its own endpoint pair by g=gcd(|X|,|Y|), and put q=|Y|/g and lambda_j=x_j/Y. The full primitive estimate is

    |R(1)|/g <= q {epsilon_(n+1)
       +(101e/9)[L_(n+1)/p_(n+1)(1)]
                       sum_j |lambda_j|/(n+3-j)!}.

The normalized coefficients are explicit rational conditioning data. No coefficient clearer is identified with q. Child 4's endpoint-lattice research and report have now been read. Under its normality hypothesis, a primitive direction u=(P,Q) has rational-lift B coefficients beta_j(u); its minimal integral lift multiplies all coefficients and its endpoint gcd by the same radial factor m(u). That factor cancels exactly. Our resulting directional estimate is

    |P+Q(e+pi)| <= |Q| epsilon_(n+1)
       +(101e/9)[L_(n+1)/p_(n+1)(1)]
                       sum_j |beta_j(u)|/(n+3-j)!.

This formula remains valid for Q=0 without dividing by Q. It applies separately to any two independent primitive directions, which need not lift to a lattice basis. Neither the lift denominator nor the endpoint index supplies an additional primitive saving.

What remains unresolved: the sizes of q and normalized coefficients for two independent useful lattice vectors; sufficient cancellation or smallness of both primitive remainders; and controlled subtraction using an unbounded number of high rows. The new polynomial saving does not settle those obligations. No normality proof, independent audit, or irrationality claim is made.

Full proofs and hypotheses: TWO_DIMENSIONAL_REMAINDER_RESEARCH.md. Both new deliverables require read-back verification before completion is reported.
