> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Shifted proportional saddles: exact algebra and remaining integration step

Agent 3, 2026-10-02, original author work. Saved before the short root-requested integral-jet interface review. The actual characteristic zero-free theorem is in SMALL_RATIO_ACTUAL_CHARACTERISTIC_ZERO_FREE.md; no complete center-rate claim is made by this progress note.

For fixed 0<c<10^(-10), define L_c(q)=integral log(z(x)^(-1)+q) dmu_c(x), with the exact principal equilibrium in PROPORTIONAL_B_EXACT_SELBERG_PROGRESS.md. The positive-real branch is used. The two limiting forcing phases are

    Phi_+(zeta)=log(1+(sigma/2)(zeta+zeta^(-1)))+c L_c(sigma+zeta),
    Phi_-(zeta)=log((sigma/2)(zeta+zeta^(-1))-1)+c L_c(sigma-zeta).

Exact radical/rational algebra gives the stationary points

    zeta_+=2/(2+c), zeta_-=2M/(2M-c), M=1+sqrt(2),

and the phase difference

    Phi_+(zeta_+)-Phi_-(zeta_-)=(2+c)log M.

The symbolic receipt proportional_saddle_algebra.json has both stationary residuals zero, both radical-square residuals zero, and the factors determining the logarithmic difference exactly M^2 and M^4. This is algebra for the equilibrium phases, separate from an actual scalar-integral theorem.

The next integration argument uses the proved actual A_j(q) zero-free bounds on fixed complex domains around q=M and q=M^(-1). A bounded-loggas empirical law plus the strongly convex variance bound should give log[A_j(q)/(s_j B_j Z_d(0))]/n -> c L_c(q), uniformly in EVERY coordinate j. The real part follows from absolute partition ratios; a holomorphic logarithm anchored at a positive real q then recovers the complex phase and all local derivatives. This retains the oscillatory expectation, rather than replacing it by its modulus.

The remaining work is to deform the scalar plus circle and minus arc to the moving radial saddles, use exact finite-n stationary points for the local Gaussian estimate, control remote arcs and the minus endpoint connectors, and bound the complete E_j and D/P_0 terms. Only then can the exact positive-weight coordinate convexity turn a coordinate result into a complete Gram-center result.

Additional primary-source queries on empirical beta-ensemble laws opened Alice Guionnet's full primary lecture notes, https://perso.ens-lyon.fr/aguionne/ColumbiaCBMS.pdf. A DOI opening for the Borot/Guionnet multi-cut paper, https://doi.org/10.1017/fms.2023.129, returned an internal error. No asymptotic is imported without checking its hypotheses. An elementary compact-energy truncation proof may be more suitable because the present field diverges at the fixed principal boundaries.

The archive query proportional/double-scaling/shifted-saddle/(2+c) across work found the previous b^4 log n normality, high-row proportional bounds, varying Toeplitz hypotheses, and this team's current reduction. It did not locate the complete actual-center target in that bounded check; no global novelty claim follows.
