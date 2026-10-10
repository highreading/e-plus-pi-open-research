> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Saddle certificates and all-parity exclusion for the original diagonal approximation

Reviewer: main Codex. Date: October 4, 2026. This note collects personally checked original proofs and independent integer-interval controls. Exact fingerprints, conditions, and reasons are in the manuscript-by-manuscript Main review register. It does not claim review of the entire historical archive.

## Confirmed conclusion

For the original raw diagonal family, first normalize primitively using the true common factor of all maximal minors. Set Z=Q̂(1), N=Pe(1)+4Pa(1), and g=gcd(N,Z), and take positive denominator q=|Z|/g with the corresponding sign for p. For every sufficiently large integer n,



$$
|q_n(e+\pi)-p_n|\ge
 \frac{\exp(3n/200)}{4\sqrt2\,25839289479611181\,n^{10}}
 \longrightarrow\infty.
$$



Thus this fixed family and its nonzero integer multiples cannot supply vanishing integer linear forms. Only this family is excluded; rationality or irrationality of e+π is not proved. Other weighted, b=1, b=2, and spectral constructions require separate checks of normalization, indices, and error. The analytic convergence still supplies no numerical first index; arithmetic threshold n≥302 is not an effective start for the full theorem.

## Four actual amplitudes

Three original witness vectors serve as exact dyadic rational inputs. Independent half-line residual certificates retain the complete infinite tails and inverse-norm bound 12, bounding the distance of each true solution from its witness. Even order retains the actual codimension-one evaluation constraint; odd order retains the actual three-column Woodbury correction and extra z. Reference-polynomial amplitudes do not replace actual amplitudes.

The primary postprocessing imports only reviewed primary integer-interval and residual-verification modules, without executing the original research library. Every pairing retains full solution error, and interval endpoints use outward rounding. The resulting strict bounds are:

| Object | Strict interval | Independent control |
|---|---|---|
| Even exterior A_s | (49/1000, 1/20) | RAW_EVEN_SADDLE_AMPLITUDES_MAIN_CONTROL.json |
| Even interior B_s | (604/1000, 605/1000) | Same as above |
| Odd exterior A_o | (−1193/1000, −1192/1000) | RAW_ODD_SADDLE_AMPLITUDES_MAIN_CONTROL.json |
| Odd interior B_o | (282/1000, 283/1000) | Same as above |

Reality of the actual amplitudes and corner constants follows from the original finite real polynomials, phase transformations, and true limits. An imaginary-part interval containing zero is not proof of reality. The strict bounds above also support the tighter rational decimal enclosures printed in the sources; screen decimals do not replace complete rational endpoints in JSON.

## Complete phase and contours

The exterior upper arc is parametrized by z(u)=−1/2−(√5/2)cos u+i(√5/2)sin u. The primary integer-interval program recomputes every derivative and takes only covering-interval endpoints from the original certificate. All 128 rational leaf intervals cover [0,1913/1000] without gaps. It verifies G″<−1/10 on [0,1/100], G′<0 on [1/100,1913/1000], and terminal −Re z<1/8. Branch validity, G′(0)=0 at the saddle, and reflection are checked analytically; terminal overlap connects the small endpoint remainder.

The complete deformation crosses neither the pole at 0 nor that at 1. The πZ term between the original left error and right arctan error is retained. Small endpoints use the complete root product and Hardy bound, with base √5/8 strictly below the main exterior saddle height. A strict maximum on the intervening compact arc gives a fixed exponential gap. Actual multipliers converge locally uniformly and holomorphically near the saddle; quadratic phase and uniform derivative bounds give varying-amplitude Gaussian asymptotics. No convergence rate is inferred from convergence without a rate.

Complete residues on the positively oriented interior circle, actual phases for both parities, and exponential-error tails were also checked. The odd reference uses λ=1; transport for the literal absolute symbol λ=1/2 is distinguished separately. Extra z, contour signs, and the common transport factor are retained.

## Combination with the actual denominator

Set φ=(1+√5)/2 and ρ=φ⁻¹. The actual even relative-error constant is C_e=4πρ A_s/B_s, and the odd constant is C_o=−4πρ A_o/B_o. The intervals above with π>3 and ρ>3/5 give C_e>1764/3025>1/2 and C_o>36/5>1/2. Hence for every sufficiently large n,



$$
|e+\pi-p_n/q_n|\ge\tfrac14\rho^{5n}.
$$



The overall assembly uses A_e,B_e, whereas the actual even-multiplier manuscript uses A_s,B_s without explicitly printing the renaming. This primary review defines A_e=A_s and B_e=B_s through the actual exterior/interior even limits. This is a notation clarification, not another amplitude input.

All 718 required finite residue classes for ten fixed primes were independently reconstructed. Arbitrary-order positive, negative, and empty-seed transfers and the final gcd bridge were reviewed by hand separately. Every contribution acts on the same actual reduced q. Combined with the exact dyadic formula, they give



$$
q_n\ge\frac{\exp(Ln)}{\sqrt2\,C\,n^{10}},\qquad
 L=\tfrac32\log2+\sum_{p\in P}\frac{\log p}{p-1},
$$



Here P={3,7,23,43,71,83,101,109,127,151}, and C=∏P=25839289479611181. An independent rational-log certificate verifies L−5logφ>3/200. Multiplying the two estimates gives the exclusion lower bound. The complete proof uses no unverified prime-density assumption, floating-point sign, arbitrary large clearer, or finite-index extrapolation.

## Reading order for the decisive sources

1. raw_all_parity_raw_exclusion.md: the overall object and complete exclusion conclusion.
2. raw_even_endpoint_residue_asymptotic.md and raw_odd_reference_and_contour_asymptotic.md: actual parity-specific relative errors and gcd interface.
3. raw_even_dual_saddle_assembly.md, raw_dual_exterior_saddle_and_endpoint_control.md, and raw_exterior_phase_strict_maximum.md: complete contours and remainders.
4. raw_even_saddle_multiplier_limit.md, raw_even_interior_multiplier_limit.md, and raw_odd_saddle_multiplier_limits.md: four actual nonzero amplitudes.
5. MAIN_FIXED_OPERATOR_INTERVAL_APPLICATION.md and MAIN_RAW_ARITHMETIC_AND_ANALYTIC_INPUT_CHAIN.md: independent primary verification and arithmetic sources.

These manuscripts are all in work/session_20260913. Before formally adopting a step, consult its file SHA, conditions, and cited parent proofs in the Main review register. The current exclusion chain is complete; unreviewed obligations in other large-prime/Smith routes remain separate and must not be written as gaps in this chain.
