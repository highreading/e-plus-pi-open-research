> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# e + π Research Report: Closeout on September 27, 2026

**Conclusion: this session proved neither that e+π is rational nor that it is irrational.** It established analytic theorems for several specific approximation constructions, arithmetic theorems for their actual denominators in lowest terms, and rigorous exclusions of some routes. These results must not be presented as a solution of the main problem.

The session ended early under the user's final instruction: “First finish what is already in progress, then organize the files, then stop.” That new instruction caused the closeout; neither the original 40% quota threshold nor a proof of the main problem triggered it. Computations and independent verifications already running have been concluded, without starting new research directions. All three subagents have finished.

Current project location: `[private local path removed]`. Earlier desktop paths in historical materials are historical references only. All new materials are saved in `work/session_20260927/`. “New” in this report means new relative to this project's previous records; it does not assert priority over the entire mathematical literature.

## 1. Most Important Verified Progress

### 1.1 All Even Indices of the Degree-One Construction Have Been Excluded

Let q_n be the **positive denominator in completely reduced form** of the actual endpoint rational number in this project's (n,1,n) Hermite–Padé construction, rather than a common denominator chosen when clearing coefficients. For sufficiently large even n, this session proved and independently verified:



$$
v_2(q_n)\ge2v_2(n!)-\frac n2,\qquad
 v_5(q_n)\ge2v_5(n!),\qquad
 v_{13}(q_n)\ge2v_{13}(n!).
$$



The last two inequalities hold for all sufficiently large n. The proofs include genuine cancellation in the numerator, final reduction to lowest terms, and every lifting depth of the exceptional residue classes; an unreduced height was not substituted for q_n. Another agent recomputed the finite seed data from independent formulas, checking all scalars in 72 rows for six predeclared primes.

Combining this with the previously verified complete endpoint error, the primitive integer linear form L_n for this construction satisfies



$$
\liminf_{\substack{n\to\infty\\2\mid n}}
 \frac{\log|L_n|}{n}\ge
 \frac32\log2+\frac12\log5+\frac16\log13
 -2\log(1+\sqrt2)>0.
$$



Thus, **no subsequence of even indices in this construction can provide primitive integer linear forms tending to zero**. This rigorously excludes one specific proof route and helps avoid repeating that work. It is not a proof of the irrationality of e+π, and it does not exclude all odd indices or other constructions.

Proof: [exclusion of all even indices](../../work/session_20260927/hp_b1_uniform_five_thirteen_and_even_exclusion.md). Independent verification: [FULL PASS](../../work/session_20260927/hp_b1_uniform_5_13_independent_review.md).

### 1.2 Analytic Error Theorem for Fixed Exponential Degree b

For every fixed integer b≥1, this project's (n,b,n) matched-endpoint construction eventually has a unique projective solution, its endpoint Y is nonzero, and



$$
(-1)^n\frac{R(1)}{Y\epsilon_n}\longrightarrow(\sqrt2-1)^b,
$$



where ε_n is the positive logarithmic Padé error under the fixed normalization in the records. The proof passed independent verification, including the remainders, limit after determinant elimination, and nonvanishing.

This means that raising b to any particular **fixed** value changes the asymptotic constant, but not the exponential error rate −2log(1+√2) here. The theorem supplies no uniform estimate when b grows with n, and does not control the actual reduced q_n. The arithmetic remains to be resolved; this analytic result cannot be treated as a proof of shrinking integer forms.

Proof: [fixed-b theorem](../../work/session_20260927/fixed_exponential_degree_error_theorem.md). Verification: [FULL PASS](../../work/session_20260927/fixed_exponential_degree_error_independent_review.md).

### 1.3 Two Local Cancellation Obstacles at Odd Indices Have Been Precisely Identified

This session reduced certain cancellation questions for the actual normalized numerator C_n to specific p-adic analytic roots and proved the reductions using complete coefficient certificates, rather than extrapolating from a few integer samples.

On the 2-adic side, there is a uniquely specified ν∈15+16Z₂ such that



$$
v_2(C_n)=
 \begin{cases}
 v_2(n-1),&n\equiv1\pmod8,\ n\ne1,\\
 2,&n\equiv3,5\pmod8,\\
 v_2(n-\nu),&n\equiv7\pmod8.
 \end{cases}
$$



All coefficients modulo 1024 on the four odd disks were computed; the infinite tails have coefficientwise bounds, and integrality was checked before every required division of a finite term. This conclusion passed independent verification.

On the 3-adic side, there is a uniquely specified ξ∈55+81Z₃ such that, for n≡1 mod3,



$$
v_3(C_n)=v_3(n-1)+v_3(n-\xi).
$$



The associated actual-denominator formulas, exceptional indices, and comparisons with the second class of terms are stated individually and passed verification. There is also a complete theorem v₃(q_n)=2v₃(n!) for n≥5, n≡2 mod3, and a lower bound when n≡0 mod3.

**No bound has been proved on how rapidly ordinary integers n can approach these p-adic roots.** Hensel's lemma supplies roots and local factorizations, not the required Diophantine upper bounds, and does not determine the rationality of ν or ξ. Both obstacles remain explicitly unresolved.

Proofs and verifications: [odd dyadic numerator](../../work/session_20260927/hp_b1_odd_dyadic_actual_numerator.md), [independent verification](../../work/session_20260927/hp_b1_odd_dyadic_germs_independent_review.md), [residue-one numerator and ternary root](../../work/session_20260927/hp_b1_residue_one_actual_numerator.md), and [ternary-root verification](../../work/session_20260927/hp_b1_ternary_root_independent_root_review.md). The transfer to q_n in Section 3 of the odd dyadic note has not yet received a separate independent verification; the PASS for the first two sections must not automatically be extended to it.

### 1.4 The Actual Gcd Obstacle at Degree Two Has Been Reduced to Small Algebraic Objects

For b=2, an exact depth formula has been obtained for the common factor Ω_n of the maximal minors of the actual three-by-two matrix at large primes, reducing its constraints to two explicit polynomials, one cubic. It was also proved that



$$
\min\{v_p(\Omega_n),v_p(\Omega_{n+1})\}=0
 \quad(p>2n+6),
$$



and Ω_n≠0 for every n≥2. Adjacent terms cannot share such a prime factor, but **deep cancellation at isolated indices remains uncontrolled**. This does not imply a sufficiently strong upper or lower bound for q_n.

Proofs: [cubic gcd constraint](../../work/session_20260927/hp_b2_cubic_maximal_minor_gate.md), [adjacent coprimality and nonvanishing](../../work/session_20260927/hp_b2_adjacent_content_coprimality.md). Verifications: [cubic-constraint verification](../../work/session_20260927/hp_b2_cubic_maximal_minor_independent_review.md), [root verification](../../work/session_20260927/two_local_lemmas_independent_root_review.md).

## 2. Closeout Materials Completed but Not Fully Independently Verified

The following materials are saved, but must be distinguished from the verified conclusions above.

- Odd-index CRT exclusion from the six-prime table: the proof text, integer inequalities, and counting certificate are complete; a dedicated independent combined verification is not. The unexcluded set consists of 146 residue classes modulo 24871 among odd n. “Unexcluded” does not mean that an effective approximation exists, and is not an upper bound for q_n. See [CRT restriction](../../work/session_20260927/hp_b1_closed_prime_odd_index_restriction.md).
- Section 3 of the odd dyadic numerator note: the transfer to actual q_n and its combination with primes 5 and 13 have been written. Independent review of the numerator germs passed, but another reviewer has not completely verified this additional transfer. See the note above. This short verification can be completed first next time, rather than repeating coefficient certificates that have already passed.

## 3. Literature Progress and Scope of Applicability

This session first restored the previously accepted conclusions and checked the integrity of files in the old manifest: all 4,765 non-AppleDouble entries existed; changes to old entries concerned caches only. No new mathematical materials beyond the previous closeout record were found that needed to be reinvented.

Inherited broad literature routes include Lindemann–Weierstrass, Baker, Schanuel-type conjectures, algebraic independence, auxiliary functions, Padé approximation, irrationality measures, and matched integrals. This session made targeted literature updates only for work closest to the current obstacles, recording the scope and the actual passages read:

| Literature input | Relevance to this project and remaining obstacle |
|---|---|
| Delaygue's Lindemann–Weierstrass theorem for E-functions | The arctangent germ here has finite branch points and cannot simply be treated as an entire E-function. |
| Fischler–Rivoal's mixed-value results for arithmetic Gevrey series | The relevant mixed-lifting theorem has explicit conjectural dependencies; the required unconditional endpoint-arithmetic conclusion was not obtained. |
| Adamczewski–Faverjon's algebraic-independence measures for E/M-values | M means Mahler; these did not supply the actual gcd theorem for the present mixed exponential/logarithmic construction. |
| Arithmetic-series/GRH results for the Euler factorial series | Parameter conditions and the quantifier “there exists a prime” cannot replace the specified-prime depth estimates needed here. |
| Recent Hermite–Padé convergence results | Convergence rates do not automatically control this project's actual reduced denominators. |

Original source links, theorem numbers, and conditions are in the [literature update](../../work/session_20260927/literature_update_and_b2_analytic_certificate.md). That note also provides an independently verified local analytic/compactness certificate criterion, without claiming that all certificates succeed or giving bounds uniform as the prime grows.

No applicable theorem directly solving the main e+π problem was found. The conditional consequence of Schanuel's conjecture—that e and π are algebraically independent and their sum is therefore transcendental—remains unchanged; it is not an unconditional proof.

## 4. Priorities When Resuming

This list gives suggestions for resumption; they will not be pursued in this session.

1. **First independently verify the two deductions already written.** These are the transfer from the odd dyadic numerator to actual q_n and the six-prime CRT synthesis. Check only the steps not yet accepted, rather than rerunning every earlier route.
2. **Remaining arithmetic obstacles for b=1.** Study upper bounds on ordinary integers approaching the specified p-adic roots, or seek actual-denominator information that bypasses cancellation near those local roots. The known Hensel factorizations do not themselves solve this; do not infer root properties from finite numerical fits.
3. **Actual numerators and isolated deep cancellation for b=2.** Use the new quadratic/cubic constraints, adjacent-coprimality theorem, and actual endpoint formulas to study factorial losses at small primes and isolated depths at large primes. Adjacent coprimality cannot replace a bound on a single term.
4. **Original matched-integral route.** This session did not change the original synchronized arithmetic-gain ledger: the sufficient target remains limsup log(c_m Δ_m g_m)/(6m)>1.1561471519642446… at the same index; the recorded gain remains only 0.1365141682948128…. Genuine synchronized positive gain is needed, rather than adding gains at different indices.
5. **New degree allocations or other constructions.** The analytic rate for fixed b has been unified. Changing the growth of b or introducing new parameters requires new proofs of uniform error and the actual primitive arithmetic normalization. General transcendence-theory and conjectural routes still depend on major unresolved inputs.

Do not repeat scans of the fully excluded raw family, treat coefficient common denominators as actual q_n, expect an extra factorial-scale error suddenly to arise from the same rational companion approximation, or regard numerical/integer-relation searches as proofs.

## 5. Files and Runtime Status

Overall index: [SESSION_20260927.md](SESSION_20260927.md). Itemized verification status: [CLOSING_VERIFICATION_REGISTER_20260927.md](CLOSING_VERIFICATION_REGISTER_20260927.md). Detailed proofs, reviews, exact scripts, JSON certificates, and sources for this session are retained in `work/session_20260927/`; earlier research materials have not been rearranged or overwritten.

The quota monitor's shared state is inactive, active monitoring loops have terminated, and the application's five-minute scheduled task is PAUSED. No reset was used this session. The last recorded quota reading was **84%** (2026-09-27 12:02:08, Asia/Shanghai); it is a historical final reading, not a fresh query of the real-time balance at closeout. The session did not end because the quota was exhausted.
