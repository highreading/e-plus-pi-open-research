> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Agent 2 report: b=floor(n/2)

The actual (n,b,n) matched system admits the same exact b-row reduction and complete-tail cofactor identities for every 1<=b<=n. A new multiple-contour representation yields an explicit uniform absolute determinant bound, with all dimension-dependent factors displayed. It retains the growing cancellation order b(b-1)/2=n^2/8+O(n), rather than extrapolating the fixed-b theorem.

See PROOF_DRAFT.md for the statements and proofs. The determinant bound follows from divided differences, reciprocal-root bounds, and a Gaussian integral on the product contour. It applies separately to both complete-tail terms, including the extra companion determinant.

The domain correction requested in ../agent3/GROWING_DEGREE_INDEPENDENT_REVIEW.md is incorporated in PROOF_DRAFT.md and recorded in GROWING_DOMAIN_CORRECTION.md. With the original functionals ell_0 through ell_b, difference determinants allow 1<=d<=b and ordinary determinants allow 1<=d<=b+1. The intended applications d=b and d=b+1 retain all accepted bounds; their largest functional index is b and their factorial arguments are at least n+1-b>=1.

This does not yet produce nonzero shrinking primitive integer forms. The missing inputs are a quantitative lower bound/nonvanishing result for the actual endpoint determinant, control of cancellation between the two remainder determinants, and the actual reduced denominator q including the final endpoint gcd. The exact sufficient inequality is q(B_W+B_T)/|D_V| ->0 together with D_V!=0 and D_W+T!=0. No favorable bound for this expression is proved.

The inherited raw-family exclusion does not automatically cover this independent unequal-degree allocation. Neither the b=0 obstruction nor the b=1 companion theorem transfers to it. No decisive obstruction to the growing regime has been established here.

The only diagnostics were n=4,6,8,10. All four matrices have the required rank and nonzero endpoints; exact intervals certify nonzero integer forms. Their reduced denominators have 10,23,43,68 digits. Their forms are large at these indices, but this is not an asymptotic conclusion. Full primitive triples, reduced endpoints, endpoint gcds, and rational interval certificates are retained in growing_regime_certificates.json. Reproduce from the workspace root with check_growing_regime.py using Python, sympy and mpmath.

Sources read: the September 27 fixed-degree theorem and independent review; the located September 13 unequal_degree_hp_attempt.md; and E_PI_RESEARCH_REPORT_20260913.md. No EQUIVALENT-named file was found in the bounded session listing. No network, installation, raw-family scan, shared-file edit, or additional agent was used.

Deliverables: PROOF_DRAFT.md, REPORT.md, GROWING_DOMAIN_CORRECTION.md, check_growing_regime.py, growing_regime_certificates.json, all under work/session_20261001_astra/agent2/.
