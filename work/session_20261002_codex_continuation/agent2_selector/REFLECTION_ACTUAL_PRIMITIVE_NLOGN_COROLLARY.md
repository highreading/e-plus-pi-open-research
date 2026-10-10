> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Actual primitive consequence for the reflected nlogn regime

2026-10-02. Original author corollary combining two separately authored results; this is not an audit. No theorem about all rational constructions or about rationality of e+pi is asserted.

The family, target gate, normalization and exact final numerator are `REFLECTION_DISTRIBUTED_POLE_REPAIR.md`. Let n=4k tend to infinity, h>=1 with

    h/(n log n)→kappa, 0<kappa<infinity,
    N=n+h.

Let c be the ACTUAL complete projected rational center and q its reduced positive denominator.

The original analytic theorem `../agent3_analysis/REFLECTED_KERNEL_NLOGN_SIGNED_DIVERGENCE.md` proves, with the full exponential/vertical errors, that

    c−(e+pi)>0 eventually,
    log(c−(e+pi))~n/sqrt(N/n),
    c−(e+pi)→infinity.                             (1)

That theorem owns the signed saddle/covariance analysis. The exact all-h arithmetic proof in the repair note proves

    v2(q)=v2(N!)+v2(U)>=N−s2(N)+1, U>0.            (2)

Here s2(N)<=1+log2(N), so s2(N)=o(nlogn), while N/(nlogn)→kappa. Equations (1),(2) yield

    liminf log(q |c−(e+pi)|)/(n log n)
       >= kappa log2 >0.                           (3)

The normalized logarithm of the error in (1) tends to zero but the unnormalized error itself diverges; no cancellation is lost by passing to its absolute value after the eventual sign is proved. Thus the ACTUAL primitive forms q(e+pi−c) diverge exponentially at the nlogn scale throughout this intended regime, without a binary eligibility restriction or an odd-prime denominator hypothesis.

This is a scoped exclusion of the stated reflected two-row family and depth regime. Finite h/n, h=o(n), h of order n², and different target-preserving projections are not covered by (1), and (3) is not transferred to them.
