> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the spectral route: actual Gram matrices, projection, and primitive approximation interfaces

Reviewer: `/root/proof_inventory`. October 4, 2026. This is an independent assistant-review report for integration by the primary agent. It neither writes to the primary review database nor modifies the source manuscripts.

**Decisive scope on the first page.** For the same actual original raw approximation, changing the basis, cutoff, spectral decomposition, row/column normalization, or expression while retaining the same reduced rational number `p_n/q_n` changes neither `q_n` nor `e+π−p_n/q_n`. Manuscript 1999, formally accepted in primary review 204, proves `|q_n(e+π)−p_n|→∞` for this fixed family. A spectral route that still produces this original raw approximation is therefore covered by the exclusion theorem in 1999; supplying a spectral Gram lower bound cannot change that arithmetic conclusion. No different weighted, b=1, b=2, or other approximation family is excluded here. A new object needs an independent proof of its actual integer normalization, common factors, and complete-error interface.

**Judgment standard.** Only conclusions actually asserted in the source are reviewed. A source that proves identities without claiming a residual lower bound is judged to have a valid stated claim. A theorem with explicit additional conditions is judged valid conditionally when the deduction under those conditions is correct. Unproved conditions and unasserted stronger conclusions are listed only as route follow-up tasks. No definite error in the actual mathematical assertions of these ten core manuscripts was found, so no source errata are proposed. The general projection, physical-scale, and primitive-error counterexamples below test possible inference rules. **They are not counterexamples to these manuscripts**, nor are they counterexamples to an actual `K_N`.

**Reading and adopted scope.** Ten core manuscripts were read in full and their original-byte SHAs checked individually. Manuscript 2326 on node spacing was also read in full as reviewed support. Entry points, complete line scopes, and the machine-readable register are in independent_math_review_register.jsonl (historical reference; see the publication coverage notes). Three complete primary continuation notes were consulted. The assembly in 1999 uses all actual arithmetic and parity-specific analytic inputs accepted in primary review 204. This report independently rederives the assembly, matrix identities, single-channel tests, and exact rate gap; it does not review again the 718 prime classes or four infinite saddle amplitudes. Other inherited inputs remain strictly within their preserved primary scopes; see [inherited_support_exact_documents_and_main_scopes.json](inherited_support_exact_documents_and_main_scopes.json).

## 1. Exclusion of the original raw family and invariance of the object

Lines 7–20 of manuscript 1999 specify the actual object:



$$
Z_n=\widehat Q_n(1),\quad N_n=\widehat P_{e,n}(1)+4\widehat P_{a,n}(1),\quad
g_n=\gcd(|N_n|,|Z_n|),\quad
q_n=|Z_n|/g_n,\quad p_n=\operatorname{sign}(Z_n)N_n/g_n.
$$



The coefficient 4 comes from the arctangent endpoint `π/4` and cannot be omitted. The assembly's `A_e,B_e` are the actual exterior and interior even limits explicitly clarified in primary review 204, namely `A_s,B_s` in the original input. Amplitudes are not replaced merely because labels look similar.

Primary-reviewed inputs give factorial depths at ten primes and an exact dyadic depth for the same **final reduced denominator**. Their combination in lines 38–75 of manuscript 1999 is correct:



$$
q_n\ge\frac{e^{Ln}}{\sqrt2 C_Pn^{10}},\quad
L=\tfrac32\log2+\sum_{p\in P}\frac{\log p}{p-1},\quad
P=\{3,7,23,43,71,83,101,109,127,151\},\quad
C_P=25839289479611181.
$$



The complete asymptotics for both parities and actual nonzero amplitudes give, for all sufficiently large `n`,



$$
|e+\pi-p_n/q_n|\ge\rho^{5n}/4,\qquad \rho=\phi^{-1},\quad \phi=(1+\sqrt5)/2.
$$



Multiplication in lines 119–131 of manuscript 1999 therefore yields



$$
|q_n(e+\pi)-p_n|\ge
\frac{e^{(L-5\log\phi)n}}{4\sqrt2 C_Pn^{10}}
>\frac{e^{3n/200}}{4\sqrt2 C_Pn^{10}}\longrightarrow\infty.
$$



A rational interval program written for this review additionally verifies `L−5logφ>3/200`, with an interval near `0.015628796017592803`. It uses 40 positive terms of the logarithm series, a strict geometric tail bound, and integer-square-root enclosures; no floating-point sign is used. Complete rational endpoints are in [independent_exact_raw_exclusion_rate_margin.json](independent_exact_raw_exclusion_rate_margin.json). This check does not replace the other primary-reviewed parent inputs.

Every integer representation `(P,Q)` of the same reduced `p/q` satisfies `(P,Q)=m(p,q)` for `m∈Z`. From `Pq=Qp` and `gcd(p,q)=1`, first `q|Q`, then `P=mp`. A nonzero integer form satisfies `|Q(e+π)−P|=|m||q(e+π)−p|` and cannot be smaller than the primitive form. Changing representations, choosing any unbounded index subsequence, or multiplying by a nonzero integer cannot restore vanishing for this family. If a linear combination of forms at different indices creates a different rational number, it is a new object and this invariance argument does not automatically apply.

The arithmetic bound starts at `n≥302`, but the analytic asymptotics leave a finite initial segment without a numerical threshold. **The effective first index of the overall exclusion is therefore not established as 302.** Excluding this family proves neither rationality nor irrationality of `e+π`.

## 2. Correct relation between the full-space resolvent Gram matrix and the actual residual Gram matrix

The full-space argument in lines 14–183 of manuscript 2051 is an actual finite-matrix proof. The boundary block Krylov basis has inverse-norm control. The specified confluent partial-fraction basis and positive `q(K/N²)` retain every factor and give `σ_min(W)≥exp(−CD log N)`. This is not a theorem about the selected projection.

Local scales must agree. Set `a_j=x_j/N², η_j=r_j/N²`; then



$$
\frac{r_j^r}{r!}\frac{d^r}{dx^r}(xI-K)^{-1}\Gamma_N
=(-1)^r\eta_j^r(a_jI-K/N^2)^{-r-1}(\Gamma_N/N^2).
$$



This agrees with lines 67–105 of manuscript 2060. The version without `Γ_N` in lines 159–183 of manuscript 2051 retains an explicit `N²`. No missing scale was found here. Branch jets are also related by local upper-triangular Toeplitz multiplication. The lower bound first holds in the **complete row space**.

The actual energy object in lines 234–284 of manuscript 2060 is



$$
Y=F^{-1/2}Z,\quad H=Y^TY>0,\quad
\Pi_W=YH^{-1}Y^T,\quad C=F^{1/2}U_a,\quad
J=C^TY=U_a^TZ,\quad G=JH^{-1}J^T=C^T\Pi_W C.
$$



Here `G>0` follows from full row rank of the actual `J`; it cannot be inferred merely from `U_a^TU_a>0`. The standard frame for its D-dimensional energy-orthogonal complement is



$$
O_D=YH^{-1}J^TG^{-1/2}.
$$



Let `O_g` be the controlled orthogonal frame in the same energy metric, and let `Π_L=U_LU_L^T` be the actual retained energy projection. Set



$$
R_g=(O_g^T\Pi_LO_g)^{1/2},\quad U_g=U_L^TO_gR_g^{-1},\quad
T_D=U_e^TU_L^TO_D.
$$



The residual Gram matrix in lines 286–401 of manuscript 2060 is then



$$
T_D^TT_D=O_D^T U_L(I-U_gU_g^T)U_L^T O_D,
$$



It is neither `U_a^TU_a` nor `G`. The second projection after removing good directions cannot be omitted. The source retains these operations, and its stated claim is valid.

Also set `D_g=(I−Π_L)O_g, D_a=(I−Π_L)O_D`. From `O_g^TO_D=0`,
`O_g^TΠ_LO_D=−D_g^TD_a`, and `R_g²=I−D_g^TD_g`. Direct elimination of the good Gram block gives the exact formula in lines 178–215 of manuscript 2059:



$$
\boxed{T_D^TT_D=I-D_a^T(I-D_gD_g^T)^{-1}D_a.}
$$



If `η=||D_g||<1, α=||D_a||`, then



$$
\max\{0,1-\alpha^2/(1-\eta^2)\}\le\gamma^2\le1-\alpha^2,
\quad \gamma=\sigma_{\min}(T_D).
$$



Thus `α²<1−η²` is a directly usable sufficient condition. Merely having `α<1` without a relative margin, or nondegeneracy of the full Gram matrix, is insufficient for a residual lower bound. Manuscripts 2059/2060 **do not assert these stronger conclusions unconditionally**.

The minimum-energy formula in lines 89–125 of manuscript 2059 is also valid. For `Ju=h`,



$$
u_h=H^{-1}J^TG^{-1}h,\qquad \min u^THu=h^TG^{-1}h.
$$



Its data norm is `G^{-1}`, rather than the Euclidean unit-data norm. The exact inf-sup and minimum-norm dual conditions in lines 224–290 follow from this formula and the actual retained test space. These are valid equivalences and conditional propositions.

## 3. Consistent changes of scale and physical scales that must be retained

A consistent constraint-coordinate change `J'=AJ`, with invertible A, gives `G'=AGA^T` and



$$
O_D'=O_D R,\quad R=G^{1/2}A^T(AGA^T)^{-1/2},\quad R^TR=I.
$$



When **data and their Gram matrix are transformed together**, node amplitudes or constraint-column scaling only change the orthogonal frame of the complement; `σ_min(T_D)` is unchanged. A large `d_j` alone does not prove a bad angle. Nor may one remove the weights from `J` while continuing to compare unit data in the old `G^{-1}` norm. Similarly, a multiplier-basis change `Z'=ZB` requires simultaneous changes `H'=B^THB, J'=JB`, which preserve `G`.

The coefficient right inverse in lines 292–351 of manuscript 2059 applies only in the specified `z/N²` coefficient norm. Its energy bound retains `H_sc` and every node weight `Λ`:



$$
G^{-1}\preceq\Lambda^{-T}\widehat R^TH_{sc}\widehat R\Lambda^{-1}.
$$



The source does not remove these costs from the coefficient right inverse. The polynomial degree `m=ceil(n/8)` used for the full angle in manuscript 2303 cannot be mistaken for the number of removed directions. Its rational good space is counted separately by `D+ell_0+ell_1−2`, and the entire comparison uses the new `b=ceil(192√n)`.

The physical endpoint metric is a different object. Lines 279–338 of manuscript 2112 explicitly give



$$
J_e=S^{-1}F[L,L]^{-1/2}U_e,\quad M_e=J_e^TJ_e,\quad
\widehat T=M_e^{-1/2}T,
$$



When `T` has full column rank, an orthogonal `V` spans `ker T^T`:



$$
\mathfrak d_n=\frac{\det((P_*J_e)V)^2}{\det(V^TM_eV)}.
$$



The formula retains the actual `S`, cardinal factors, and `g_l`. Good conditioning of the energy matrix does not replace the physical endpoint angle, and this conversion still supplies no primitive/gcd control of the actual integer coefficients. The concrete framework in 2112 uses the old `n^{3/4}` cutoff; 2303/2059/2296/2254 use the new 192√n cutoff. Only the general finite-dimensional algebra can be reused without carrying over the old `F`, good frame, or degree counts silently.

## 4. The stated claim in pending manuscript 2254 is valid: explicit scope of the single-channel strengthening

Lines 8–29 of manuscript 2254 set `dμ=F_bR²L_a²dΣ_aa`, `dχ=dμ/R`, and retain `2/n≤R≤1`, giving



$$
H_a\preceq\widetilde H\preceq(n/2)H_a.
$$



Set `G_a=J_aH_a^{-1}J_a^T`. The original μ extremizer is
`u_h=H_a^{-1}J_a^TG_a^{-1}h`; lines 31–70 construct



$$
w_h=\widetilde H^{-1}J_a^TG_a^{-1}h,\qquad p_h=(\pm)L_aw_h.
$$



For `J_av=0`,
`<p_h,r_av>_F=w_h^T\widetilde Hv=u_h^TH_av=0`. For every single-channel extremizer,



$$
\langle p_h,f_{h'}^a\rangle_F=h^TG_a^{-1}h'.
$$



Furthermore, `J_aw_h=\widetilde G G_a^{-1}h`, which generally differs from `h`; the source explicitly retains this relabeling. Lines 72–105 use `\widetilde G≤G_a` and one additional `1/R` to obtain



$$
\|p_h\|_F^2\le(n/2)E_a(h),\qquad E_a(h)=h^TG_a^{-1}h.
$$



With the actual degree condition `deg(L_aw_h)≤q_a`, removing at most `t_a=max(0,ell_a+d_a−1−q_a)=O(√n)` data directions puts `p_h` in the retained prefix. Therefore



$$
\boxed{\|\Pi_Lf_h^a\|_F\ge\sqrt{2/n}\,\|f_h^a\|_F}
$$



The result holds on a data band of dimension `D−O(√n)` and satisfies first-channel zero-data good orthogonality. This is a valid strengthening; the source need not be changed to the weaker `2/n` bound.

The pairing with the other good channel in lines 107–140 remains
`∫F_bL_aL_bw_hv_b dΣ_ab`. Its exact cross-moment map and the positive telescoping expansion of `F_b−F_a` one degree lower are valid. The source does not claim that these properties make the cross map vanish or have small rank or norm. The mixed residual bound is therefore a **follow-up task**, not an error in this manuscript.

The full/single Schur comparison, Pythagoras identity, scalar kernel, and original `2/n` band bound in 2296 are also valid. Its conditional rank improvement in lines 227–280 explicitly requires a new scalar approximation estimate; the warning that the current conservative `η/δ` is not small is correct. An unproved premise does not invalidate a conditional theorem.

## 5. Original error and actual q: limits on the use of spectral progress

The complete manuscript 2011 proves a factorial lower bound on the absolute mass of the normalized polynomial and uses high orthogonality to obtain a factorially small cancellation ratio:
`M_n≥n!exp(−O(n))`, `vartheta_n≤exp(O(n))/n!`. The complete formula in lines 220–243 retains `q_n`:



$$
\log|L_n|=\log q_n+2n\log(\sqrt2-1)+\log M_n+\log\vartheta_n+o(n).
$$



The two opposing factorial scales do not determine the exponential rate of their product. A small normalized remainder cannot replace smallness of `q_n·error`. Lines 392–396 explicitly restrict the source's conclusion, and its stated claim is valid. Later manuscript 1999 supplies a lower bound in the opposite direction for the primitive error of this fixed original family.

The adjacent determinant/gcd argument for actual reduced rationals in 2278 is valid within the exact dyadic and even-relative-error scopes of primary-reviewed 2014 and 2098: `v_2(D_{n,m})=a_n`, and `D/gcd(q_n,q_m)` is a nonzero odd integer. The limsup statements for adjacent denominators and odd parts, and the necessary adjacent odd-factor condition for a shrinking subsequence, are correct. The statement that these estimates had not yet excluded shrinking describes the scope of those weaker estimates at that time. It neither claims that the later result 1999 is invalid nor constitutes a mathematical error requiring correction. Current continuation uses the completed exclusion in 1999, rather than presenting 2278 as the route's latest conclusion.

## 6. Exact counterexamples to general inference rules, not source errata

The reviewer's [independent_exact_interface_examples.py](independent_exact_interface_examples.py) uses only standard-library rational arithmetic and computes 15 exact examples. They test general interfaces without importing or running the original research scripts. The parameter constructions below provide complete analytic reasons; finite examples are not promoted to infinite conclusions for an actual `K_N`.

**A good full Gram matrix can have zero actual projection.** In `R^6`, take `F=I`, `Z=[e_1,w_t]`, and
`w_t=((1−t²)/(1+t²))e_2+(2t/(1+t²))e_3`. Set `U_a=w_t`, choose good frame `e_1`, and retain `span(e_1,e_3,e_4,e_5)`. The full quantities are `H=I, G=1, U_a^TU_a=1, η=0`, but the residual Gram is `(2t/(1+t²))²`. It is zero at t=0 and arbitrarily small for positive t. This refutes a direct inference of a residual lower bound from these general full-Gram properties.

**A positive retained norm can vanish after good subtraction.** Let `a²+b²=1`, `O_g=ae_1+be_2`, and `O_D=be_1−ae_2`, retaining only e_1 in this plane. Then `η=b, α=a`, and the denominator's retained norm is `b>0`, yet it becomes exactly zero after removing the retained good direction. Choose `a=(m²−1)/(m²+1), b=2m/(m²+1)` to have `η→0`. Here `α²=1−η²`, showing why a positive retained bound and a small good defect still need the correct relative margin.

**Good energy conditioning does not control the physical endpoint.** In `R^4`, take the orthogonal kernel frame
`V_1=(3e_1+4e_3)/5, V_2=(3e_2+4e_4)/5` and use its orthogonal complement as the two columns of `T`, so `T^TT=I`. Set `J_e=diag(M,M,1,1)` and let `P_*` select the final two coordinates. Formula (24) of 2112 then equals `256/(9M²+16)²→0`. Another kernel choice in the first two coordinates makes the endpoint zero. A lower bound for full T cannot remove `M_e` or the endpoint rows.

**One and two powers of a weight are not interchangeable.** On two points, take `R=(1/2,1), μ=R²`, `u=(4,−1)`, and `v=(1,1)`. Then `<u,v>_μ=0`, but the naive test pairing with one weight equals 1. The correct test in 2254, `w=Ru=(2,−1)`, restores a zero first-channel pairing. Adding a nonzero cross term from a positive matrix measure still leaves a nonzero other-channel pairing, consistent with the source's retained cross obstruction.

**Small relative error and good spectral conditioning do not prove primitive vanishing.** `A_q=[[1,1/q],[0,1]]` satisfies `det A_q=1, ||A_q||≤2, ||A_q^{-1}||≤2`, while the rational-entry denominator q is arbitrarily large. Alternatively, for rational target 1, take `q=2^n, p=q−1`. Then `gcd(p,q)=1` and relative error `2^{-n}→0`, but the primitive form `q−p=1`. This refutes a general argument that omits actual q; it makes no assertion about actual `e+π`.

## 7. Manuscript verdicts, provenance, and literature comparison

The formal manuscript-by-manuscript register is independent_math_review_register.jsonl (historical reference; see the publication coverage notes). Each of the ten core entries records complete source line scope, original SHA, actual path, actual assertion, deduction, inherited primary review IDs, and independent route follow-up tasks. Verdicts and route goals have separate fields; definite-error lists are empty. The additional full reading of 2326 and all literature/primary-context receipts are recorded separately without expanding the core review set.

The complete local texts `matrix_orthogonal_ratio_literature.md` and `literature_hp_dvr_content_and_obstruction.md` were read as historical literature guides only. The preserved original Beckermann–Labahn ISSAC2009 text was directly examined at lines 350–480 and 580–790, including (3.1), Theorem 5.3, and the associated proofs. The Mahler cofactor relation retains `d^(m−2)`, and fraction-free updates retain the previous pivot `d_k`. These are the original source's exact normalizations. This report derives no actual endpoint gcd upper bound from these identities. PDF/text SHAs, actual reading scope, and the authors' URLs are in [local_and_original_literature_and_main_context_reading_receipt.json](local_and_original_literature_and_main_context_reading_receipt.json). Neither full review of the paper or all literature nor novelty of these rederivations is claimed.

**Continuation conclusion.** The source's spectral, energy, and single-channel results remain usable under their respective conditions; this review found no definite mathematical error requiring correction. Mixed residual Gram and physical endpoint estimates remain additional research tasks beyond these matrix results. If the target is shrinking integer forms from the same original raw family, 1999 already excludes it. A new rational approximation family requires reidentification of the object and its arithmetic/complete-error interface.

## Appendix: exact fingerprints and full-reading scopes for ten core sources

Every path has prefix `work/session_20260913/`. Actual compatibility-link destinations, path aliases, primary IDs, and independent review IDs are in JSONL. Table line numbers refer to the unchanged complete source manuscripts.

| Document ID | Source manuscript | Original-byte SHA256 | Full-reading line scope | Manuscript verdict |
|---:|---|---|---|---|
| 1999 | raw_all_parity_raw_exclusion.md | `ffa55a2238c90e3e940830c497657e7e75ee961e209d67cc1efc2bf7277387c9` | 1–165 | the source's stated claim is valid (reusing actual parent inputs reviewed by the primary agent and independently rederiving the assembly) |
| 2060 | raw_denominator_exceptional_resolvent_bridge.md | `520dfb1348d87cc2a8be0071e6aaba61d467fa472747b82561c5c5e9169ce675` | 1–474 | the source's stated identities are valid; propositions with explicit additional Gram conditions are valid |
| 2059 | raw_denominator_dual_variational_interpolation.md | `6264ed9edbfb8168ceedd69ffa986358e33c3b72866bdc6fc1050697005b2aa7` | 1–434 | the source's stated claim is valid; the exact equivalence and explicitly conditional propositions are valid |
| 2296 | raw_single_channel_denominator_extremizers.md | `3edd859a631150fc80e7fe804f498e1535b8f61fc0abc02359a21edb668cad89` | 1–296 | the source's stated claim is valid; the explicitly conditional rank-improvement proposition is valid |
| 2254 | raw_polynomial_weight_denominator_dual_tests.md | `6cc937217230d36fdd4e2c1a5c56f911187b99cc87b3aa33cec2e5f54c473fa3` | 1–140 | the source's stated claim is valid (all five sections independently reviewed) |
| 2303 | raw_sqrt_cutoff_full_channel_angle.md | `365b135bb5d0e26ab22374f47154e5c24df71a9a6f0fd898aae881f450299b60` | 1–168 | the source's stated claim is valid (retaining the explicit new cutoff and the scope of the inherited supporting lemma) |
| 2051 | raw_confluent_boundary_resolvent_gram.md | `6c0b2525f6621661c83897ed20c44ab04eaf9e4a5b20b3406743677af21485d8` | 1–200 | the source's stated claim is valid (the confluent Gram matrix of the complete finite row matrix) |
| 2112 | raw_explicit_exceptional_schur_reduction.md | `04748c73ea66ef572f4530960d7dad2b9a0437a818dfd1fd35a2ce9734a583c8` | 1–363 | the source's stated claim is valid; propositions with explicit additional rank/Gram conditions are valid |
| 2011 | raw_arctan_dual_factorial_mass.md | `c9b4c8a980dcb8bc86974554e486ec084ba99d383dc5d0ccffb0a7436c90d9c0` | 1–396 | the source's stated claim is valid (inheriting the actual positive-kernel inputs reviewed by the primary agent) |
| 2278 | raw_relative_error_dyadic_denominator_growth.md | `11c3a830dca90a1312d0973365d217e6e75f7e03ced6f2180ef2e411f317601f` | 1–227 | the source's actual arithmetic assertion is valid under the explicitly reviewed dyadic and even-error inputs |
