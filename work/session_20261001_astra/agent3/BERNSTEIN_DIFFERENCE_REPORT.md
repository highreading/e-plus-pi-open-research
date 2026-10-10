> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Agent 3: Bernstein-difference continuation

All 126 successive signed Bernstein differences in the saved n=6,b=3 vectors are strictly negative. No positive-difference witness exists. The original 133 signed coefficients remain strictly positive. These checks used the saved vectors directly and preserved their certificate.

The symbolic continuation derives explicit difference sums in the actual ordered high-row minors, and a Volterra recurrence with the required Bernstein degree elevation. Its shift contribution need not be nonpositive. The first exact counterexample to that shortcut is

    tau_(1,0)=12152941/7064347530240>0.

The inherited contribution is -984229/144170357760, leaving the actual complete difference

    delta_(2,0)=-27329/5351778432<0.

All 95 checked shift differences are positive. The shortcut is closed; this does not refute full monotonicity or the original coefficient-sign conjecture. The correct sufficient recurrence inequality bounds the positive shift by the inherited negative allowance, with explicit nonnegative margins if available.

A separate proved conditional endpoint lemma reduces the target to two explicit ordered-minor sums E_n,E_(n+1). For even n, b=n/2,

    D_V=[p_(n+1)(1)E_n+p_n(1)E_(n+1)]/[h_n(n!)^b].

Therefore E_n,E_(n+1)>=0, not both zero, prove D_V>0 and Y<0, with a quantitative lower bound when positive margins are supplied. Their definitions retain the actual high-row minors. The inequalities remain unproved uniformly.

The polynomial bridge to the new two-scalar draft is

    z0=-E_(n+1)/(n!)^b, z1=E_n/(n!)^b.

Only this bridge is supplied; Agent 2's quotient and companion audit is not duplicated. At the same saved n=6 control,

    E_6=1355870278086451/73150524144312975360000>0,
    E_7=181648924564193/70441245472301383680000>0.

These are contractions of saved polynomial vectors, not new degree controls.

The most focused next lemma is positivity of these two aggregate ordered-minor sums on an explicitly described unbounded even-index set. The stronger recurrence route instead requires a bound on its positive shift contributions. Neither task has been completed uniformly; full-remainder nonvanishing and actual reduced-denominator control remain separate.

Files under work/session_20261001_astra/agent3/:

- BERNSTEIN_DIFFERENCE_CONTINUATION.md — identities, proofs, counterexample, and precise remaining inequalities.
- bernstein_difference_saved_data_checks.json — all 126 exact differences and source preservation.
- bernstein_difference_recurrence_checks.json — degree-elevation checks, shift witness, and polynomial endpoint bridge.
- check_bernstein_difference_identities.py — verifier using the saved coefficient vectors and ordered high-row minors.
- BERNSTEIN_DIFFERENCE_REPORT.md — this report.

No additional HP indices or primes were tested. The existing certificate is preserved. The chosen absolute-bound shrinking obstruction remains; endpoint gcd improvements do not rescue those bounds.
