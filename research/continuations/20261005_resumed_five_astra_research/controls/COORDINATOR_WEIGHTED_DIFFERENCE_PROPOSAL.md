> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Weighted first-difference proposal — unproved research target

The accepted all-coefficient parameter estimate discarded the available word weight to obtain a uniform gain of3. Retaining that weight may avoid higher divided differences altogether.

Let w_i=v2(floor(i/2)!), and let W be w_i plus the total expansion order of a complete contact word. The accepted filtration gives output degree r<=4W+3. A telescoping difference of endpoint binomials costs at most floor(log2(4W+3)); changing h or n has increment depth ell+5 or ell+6. All unchanged factors retain their weight. Thus the candidate bound for a differentiated word is

    ell+5+W-floor(log2(4W+3)), ell=v2(k-k').

This requires a NEW weighted bound for the complete force difference. One possible derivation uses

    (h)_falling_m = m! binom(h,m),

whose parameter difference has depth at least ell+5+v2(m!)-floor(log2 m). The scalar depth v2(s!) in each central sum pays the binomial parameter loss there. The affine odd prefactors and the remaining n-falling products must be checked at the same precision; their difference cannot be treated as preserving weight automatically. The factorial/binomial proof of the undifferentiated w_i bound suggests that a single largest binomial loss suffices.

If the complete force difference and full finite contact inverse satisfy the word bound, define W_r=max(0,ceil((r-3)/4)) and

    beta_r=5+W_r-floor(log2(4W_r+3)).

Since W-floor(log2(4W+3)) is nondecreasing for W>=0, one would obtain

    v2(p_r(k)-p_r(k')) >= ell+beta_r.

This is a PROPOSAL, not an accepted theorem. Uniform tails, every endpoint term, parameter changes at every position in a Neumann word, and any initial-force loss must be audited.

Combining a valid bound with the exact roots -1,...,-J_r and the proved consecutive-product lemma would give

    v2(p_r(k)/product_(c=1)^L(k+c))
      >= beta_r-v2((L-1)!), 1<=L<=J_r.

For positive reconstruction shifts s and r>=s, beta_r is nondecreasing, while L=floor((s+4)/128). The resulting lower bound grows approximately as s/4-s/128-log2 s. This would remove unbounded root contacts and make the normalized high-shift tail decay at growing precision. It would still not evaluate the extra scalar norm cancellation or the complete mixed contraction.

The decisive task is to prove or correct the WEIGHTED complete-force difference, rather than adding absolute and unweighted local bounds, which is invalid.
