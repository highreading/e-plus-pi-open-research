> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Gamma lower-bound correction

This separate note records the previously reported correction to RATIONAL_SADDLE_SELECTOR.md without modifying or replaying its proof or computations.

In the paragraph bounding the complete exponential residual, replace the assertion Gamma(m+1/2)>=1 for integers m>=0 by

    Gamma(m+1/2)>=sqrt(pi)/2.

The minimum occurs at m=1. The displayed bound Bexp already retains the exact Gamma factor and is unchanged. The corrected positive constant changes neither its stated logarithmic upper bound nor the uniform logarithmic-degree asymptotic conclusion.

This correction provides no extension beyond the original m<=log n domain. The larger-degree selector requires a separate analysis.
