> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Large-selector block noncancellation report

New author mathematics; no independent review, numerical scan, or repeated check. Earlier endpoint-enclosure results are preserved. The two main selection and complete-exponential drafts were read as author inputs.

The endpoint enclosure extends uniformly to

    m=rho n log n+O(n log n/log log n)

with a common truncation depth K=O_rho(n log n). Its normalized remainder is at most exp(-2n log n) on eligible nodes. Exact adjusted m values remain in every coefficient and phase.

A new selection theorem strengthens the main U-maximizer. For n=2^s, take the same dyadic h of size log n/log log n and 8h complete parity-eligible runs, contained in an interval of length at most 4nh+n/2. Divided differences imply that each residue class modulo h has at most n/2 nodes below T=(2h)^(n/2). Counting consecutive integer edges then proves that at least

    h(n-8)

pairs (m,m+1) have BOTH |U|>=T. Their two forcing values therefore satisfy log|U|=(1/2+o(1))n log log n. No search was performed.

For the upper endpoint contribution J_m, the new exact adjacent identity is

    J_(m+1)=-2i J_m+E_m.

A direct segment bound proves

    |E_m|<=4*2^m*(n+1)!/(7m/8)^(n+2).

It yields an adjacent lower bound in terms of |J_m|, but its error is small relative only to an explicit absolute-integral majorant. No relative bound for the actual oscillatory J_m is inferred.

A more general block test uses the finite endpoint sums. On a high-high edge set

    p0=Z_m/U_m, p1=Z_(m+1)/U_(m+1),
    S_e=|p0|^2+|p1|^2,
    W_e=Im(conjugate(p0)p1),
    d_e=|W_e|/sqrt(2S_e),

with d_e=0 when S_e=0. These are explicit rational/algebraic data independent of e and pi. The determinant inequality gives

    max(|Im p0|,|Im p1|)>=d_e.

Consequently the COMPLETE error satisfies

    max(|c_m-(e+pi)|,|c_(m+1)-(e+pi)|)
      >=[2^(n+2)d_e-eta_star-Bstar]_+.

Here eta_star<=exp(-2n log n), and Bstar bounds the entire exponential residual uniformly on the high-forcing nodes:

    log Bstar<=-n log n+(1/2+o(1))n log log n.

The report does not assert positivity of the bracket. The missing phase theorem is a quantitative lower bound for W_e on at least one of the many high-high edges. Large U alone supplies none. The dyadic h-grid has a real endpoint multiplier (-2i)^h=2^h, so the new use of consecutive integer nodes avoids that aliasing but does not control the analytic correction.

Using the provisional ACTUAL dyadic denominator law, the research note proves a block primitive-form lower bound

    max q_m|c_m-(e+pi)|
      >=Qmin[2^(n+2)d_block-eta_star-Bstar]_+,

where d_block=max_e d_e and log Qmin=2rho log 2 n log n+O_rho(n). A phase lower rate exp(-sigma n log n) with sigma<min(1,2rho log 2) would imply selected-subsequence divergence. That phase bound is not established.

Strongest outcome: uniform enlarged-range control, guaranteed adjacent large-forcing pairs, and explicit signed adjacent/block inequalities with a precisely identified remaining phase obstruction. No enclosure is presented as dominance and no unbounded complete-error lower bound is claimed.

Full proofs: LARGE_SELECTOR_BLOCK_NONCANCELLATION.md. Both new files require read-back before completion is reported.
