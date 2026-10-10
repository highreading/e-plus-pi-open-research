> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Quotient output minor: one exact hypothesis test

2026-10-02. Author symbolic evidence for the NEW quotient-output-minor hypothesis, not a repetition of the archived 15 certificate values and not a proof for unbounded n.

The explicit target is whether the three consecutive actual W-output rows have rank three on the moment-state quotient by the known U solution. Let B_m be the 3×4 matrix of output rows at m,m+1,m+2, all pulled back to the common state (I_m,…,I_(m+3)). Its signed 3×3 cofactor vector is necessarily proportional to v_m=(U_m,…,U_(m+3)), since B_m v_m=0. Write it as τ_n(m)v_m, where defined over Q(m); this determines τ_n uniquely because v_m is not the zero rational vector.

For n=4, `derive_weighted_observability.py` generated the actual U polynomial and all moment transition rows through the n+3 support index, formed the actual order-five weighted finite differences, and obtained τ_4 by a signed minor divided by U_m. The rational expression and its full factorization are saved in `weighted_observability_n4.json` and `.log`.

Its numerator has degree 22 and mixed coefficient signs. Its denominator factors into m+5,…,m+8, 2m+9,…,2m+15, 4m+17,…,4m+31 and a positive-coefficient sextic. Thus every denominator factor is strictly positive for m≥0.

An exact Sturm root count of the numerator returned zero roots on [0,∞). Its eight real roots were all isolated in negative rational intervals; the other roots are nonreal. This checks the mathematically meaningful hypothesis τ_4(m)≠0 on the whole nonnegative real axis, rather than sampling W at individual m. It proves the n=4 instance of rank three; no general-n inference is made. A follow-up n=8 derivation is in progress.

Canonical transition implication: if M_m is the moment companion matrix, the pulled-back next cofactor vector equals det(M_m) τ_n(m+1)v_m, since M_m v_m=v_(m+1). Therefore the determinant of the induced three-output state transition, wherever the quotient is observable, is

    det(M_m) τ_n(m+1)/τ_n(m),
    det(M_m)=c_0(n,m)/c_4(n,m)≠0.

This keeps the regular moment recurrence and the transformed apparent singularities separate. The general O(1)-shift theorem is reduced to a concrete nonvanishing problem for τ_n at actual integer m in the required regime. Neither its sign nor its zero count is presently proved for an infinite n-family.

Follow-up n=8 completed. Its τ_8 numerator has degree 38 and mixed coefficient signs, including negative high-degree coefficients. Its denominator again factors completely into positive linear factors and a positive-coefficient sextic on m≥0. An exact Sturm calculation finds zero nonnegative real roots; all 18 real roots are negative, with saved exact rational isolating intervals. The complete data are in `weighted_observability_n8.json`, `.log`, and `weighted_observability_root_counts.json`.

These two exact whole-axis tests support, but do not prove, the following sharply formulated target: for every n=4k, the canonical quotient-output scalar τ_n(m) is nonzero for real m≥0 (or at least for integers m in the large-selector regime). A coefficient-positivity proof is not available because both observed numerators have negative coefficients. A structural positive integral, sum of squares, or controlled recurrence in n would be needed. No further small-n grid is proposed merely to accumulate evidence.

A structural positivity attempt was tested on the same two derived numerator polynomials, without any new W point scan: expand p_n(m)=Σ_k Δ^k p_n(0) binom(m,k). All Newton coefficients are strictly positive for n=4. For n=8, coefficients k=29,30,31,32 are negative. The simple all-positive Newton-coefficient hypothesis is therefore false already at n=8 and cannot be promoted to a general proof. Exact coefficient arrays are saved in `weighted_observability_newton_coefficients.json`.

The observed denominator has a simpler combined pattern after ignoring constant powers of two: P_6(m,n) times ∏_(j=n+13)^(5n+12)(4m+j); the numerator degree is 4n+6 in both derived cases. This is a structural pattern, not a proved identity for all n. It identifies a concrete possible recurrence-in-n object for a future positivity argument.
