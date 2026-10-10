> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Small-saddle phase correction

This separate record corrects the reported constant in LARGE_DEGREE_SADDLE_SELECTOR.md without modifying or replaying its retained derivation.

For kappa=m/n tending to infinity, at either small stationary point,

    Re Psi_kappa(w)=0.5 log(2kappa)+0.5+O(kappa^(-1/2)).

The constant is +1/2, not -1/2. The contribution 2kappa log|1-2w^2| is +1/2+O(kappa^(-1/2)). The correction does not alter the previously stated leading n log n budgets, whose O(n) terms already absorb this constant.

This correction establishes neither contour dominance nor noncancellation. Those remain distinct analytic obligations.
