> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# File-by-file mathematical review: weighted / b=1,b=2 / jet-Hurwitz


---

Attribution: /root/organization_evidence. Recorded at: 2026-10-04T07:02:14.278086+00:00.


---

The user explicitly authorized mathematical review for this task. Full-source reading and mathematical review scope are recorded separately. The following ten manuscripts are the priority objects. Exact primary-reviewed proof/certificate inputs are reused without rerunning the original programs. Verdicts on the manuscripts are distinguished from proof obligations for the main research goal; unasserted results are not treated as manuscript errors. The main database, source texts, formal register, and graph were not modified.


---

# D39：WEIGHTED_DETERMINANT_DYADIC_GATEWAY.md

Attribution：/root/organization_evidence

Mathematical verdict：**valid local and conditional theorems; the source does not claim completion of the general all-degree route**。

Original path：`work/session_20261002_codex_continuation/agent1_arithmetic/WEIGHTED_DETERMINANT_DYADIC_GATEWAY.md`

Original SHA-256: `6a665f2626bb6fbf4eec246d94d55e46a428d3e0fd429f240dc0dd53a09bc942`

Actual reading: complete source textL1–L205，13250characters，13533bytes; including status and dependencies, scope, and correction sections.

Copy of the original bytes：`[private local path removed]`

Existing primary review: review 5。

inherited primaryscope：Sections 1-7 checked, section 8 read as a reference to a separate proof, not certified here

Specific source-text basis：

- L44–54: the integer recurrence and oddness of b_r are valid, so v2(B_r)=r. This is a symbolic proof for every r, rather than an extrapolation from a finite scan.
- L68–76: the equivalence of three monic/cofactor integrality conditions is valid; rank<=2 mod2 proves none of them by itself.
- L82–110: the complete pair theorem is valid, provided q(0) is odd, w!=0, and every V gate in the same y basis holds simultaneously.
- L114–129: the author correctly distinguishes the shifted basis from the y basis; the manuscript explicitly does not infer the gate from the old lower bound.
- L151–153, 201–205: an integer symmetric operator and an integral block basis alone do not guarantee primitive pivots. The subsequent subfamily result is a separate dependency.

Rederivation and valid usable conclusions：

Set E_i=2^i i!. After dividing the factorial terms by E_iE_j, every term with t>=1 is even, and the t=0 term is -q(0)binom(i+j,i) mod2. The complete V gate also makes the arctangent correction even. Every northwestern principal minor of the Pascal Gram matrix P P^T equals 1, so M=E^-1 R E^-1 is a 2-adic unit matrix. The depths of z_i=(-1)^i/E_i strictly decrease with i, and the final diagonal entry of the inverse is a unit. Thus, the square of the last coordinate gives the unique lowest valuation in z^T M^-1 z. The identity beta=w alpha v^T R^-1 v gives source formula (6); after complete gcd cancellation, the formula is independent of the denominator-clearing scale.

The reviewer's synthetic example uses q(y)=(y+1)^9+512. It satisfies q(2z-1)/2^9=z^9+1, odd q(0), and w=512!=0, but V8=-1356704742505472/902522205585 has v2(V8)=10, whereas the gate at i=j=4 requires 15. This is not an actual orthogonal ray; it only excludes the additional inference that normalization integrality alone implies the gate. The source never asserts that inference, so this is not a source error. The source's own integer-symmetric-operator example was also checked independently: the monic polynomial z^2-(3/2)z-2 is indeed not 2-integral.

Conditions of use and limits relative to the main goal：

- Applying this conditional theorem requires proving every premise for the actual orthogonal q. The rational arctangent term cannot be omitted.
- The general all-n cofactor inequality and same-y-basis gate are not completed by this manuscript alone. The regular subfamily separately uses D2621/D2623.

Definite errors in the text: none were found in this object's actual assertions in this batch. The counterexamples or proof obligations above are not registered as errors in this document.

Coordinates of independent exact small examples：

- [Complete results](OWN_EXACT_INTERFACE_EXAMPLES.json#/synthetic_normalized_weighted_polynomial_without_orthogonality); pointer `/synthetic_normalized_weighted_polynomial_without_orthogonality`。
- [Complete results](OWN_EXACT_INTERFACE_EXAMPLES.json#/integer_symmetric_operator_counterexample); pointer `/integer_symmetric_operator_counterexample`。

Program written by the reviewer：[check_interface_examples_owned.py](check_interface_examples_owned.py)。


---

# D1903：hp_b1_endpoint_attempt.md

Attribution：/root/organization_evidence

Mathematical verdict：**valid eventual analytic conclusions with an accurately identified unresolved arithmetic interface**。

Original path：`work/session_20260913/hp_b1_endpoint_attempt.md`

Original SHA-256: `3f3c874e30661f8f4f82f4341b5a1e3dec118b33e2e671003731b82cb00496cb`

Actual reading: complete source textL1–L522，16417characters，16450bytes; including status and dependencies, scope, and correction sections.

Copy of the original bytes：`[private local path removed]`

Existing primary review: review 31。

inherited primaryscope：Uniform proofs and exact denominator ledger, n>=64/n>=512 as stated; old finite checks are not the proof

Specific source-text basis：

- L19–45: Y>0 for n>=64 and the nonzero error/rate for n>=512. The main goal requires q; the real size of Y is not a bound on q.
- L109–127, 267–291: projection and endpoint matching give delta=t1-t0 and Y=delta/(1+t1), while correctly retaining the n=1 exception.
- L321–406: the complete endpoint remainder is ell_B(Psi), rather than just the first free jet. Its eventual nonvanishing follows from a complete tail estimate.
- L434–492: X/Y and den(X/Y) constitute the actual endpoint pair. Any redundant clearer cancels simultaneously through the gcd.

Rederivation and valid usable conclusions：

For the raw representative B=(1+t1)-(1+t0)z, Y=delta and X=(1+t1)a0-(1+t0)a1. Exactly, R(1)=X+delta S, c=-X/delta, and hence R(1)/delta=S-c. Reducing with q=den(c) gives |qS-p|=q|R(1)/delta|, independently of how the full triple was initially normalized. Reusing the root-location/polarization and complete remainder estimates confirmed in primary review 31 gives log|qS-p|=log q-2n log(1+sqrt(2))+o(n).

The complete analytic proof scope of primary review 31 is reused without rechecking hundreds of finite inputs or external papers. The source explicitly leaves the arithmetic question open; this does not make the manuscript incorrect. A usable next task is the minimum rational height of X/delta. A positive route requires an infinite subsequence with q<=exp((2log(1+sqrt(2))-eta)n); excluding this family requires a sufficiently strong uniform lower bound on q together with the proved nonzero error. The primary reviewer already corrected D1906's n=1 prime-scope error; it is retained only as inherited errata.

Conditions of use and limits relative to the main goal：

- Retain n>=64/n>=512 in the analytic comparison. An n=1 counterexample does not refute an eventual theorem.
- No favorable upper bound on total q, route-excluding lower bound, or complete gcd rate is proved.

Definite errors in the text: none were found in this object's actual assertions in this batch. The counterexamples or proof obligations above are not registered as errors in this document.

Coordinates of independent exact small examples：

- [Complete results](OWN_EXACT_INTERFACE_EXAMPLES.json#/n1_actual_HP_endpoint_counterexample); pointer `/n1_actual_HP_endpoint_counterexample`。

Program written by the reviewer：[check_interface_examples_owned.py](check_interface_examples_owned.py)。


---

# D1910：hp_b2_endpoint_attempt.md

Attribution：/root/organization_evidence

Mathematical verdict：**valid eventual b=2 theorems and local prime exclusion; the total denominator remains unresolved**。

Original path：`work/session_20260913/hp_b2_endpoint_attempt.md`

Original SHA-256: `ba2b0e2c74e72892488ae9fea6a1f3b7483afa5e9f4bb622ddbe317af907cd05`

Actual reading: complete source textL1–L522，16114characters，16129bytes; including status and dependencies, scope, and correction sections.

Copy of the original bytes：`[private local path removed]`

Existing primary review: review 33。

inherited primaryscope：All proof sections including covariance domination and prime-family argument; historical small-degree fractions are not independently rerun here

Specific source-text basis：

- L25–45, 95–148: the signs in the two-row cross product and Y=-S(U,V) are correct.
- L155–231: the covariance lemma has a uniform-in-m O(n^-2) tail majorant; it does not interchange an infinite sum using only pointwise convergence for fixed m.
- L321–381: eventual Y<0 is under the normalization B(0)=1. The positive constant for R/Y is (sqrt(2)-1)^2; the sign of Y is not the sign of the error quotient.
- L383–424: the minimum endpoint q and complete error are retained. Positive Y at n=2,3 does not refute eventual negativity.
- L446–521: for each odd prime p, the local statement p does not divide q at n=p-1 is valid. It is not an all-n total-height theorem.

Rederivation and valid usable conclusions：

Set Delta=ell1-ell0, Theta=ell2-ell1, and S(P,Q)=Theta(P)Delta(Q)-Delta(P)Theta(Q). Expanding det(a,1+t,1) gives Y=-S(U,V); expanding det(a,1+t,w) gives R=S(U,W)+det(a,t,w). Primary review 33 checked uniform domination for the covariance. Consequently, S(U,V)~- (dV/n)U(0)V(0)e^(-2sqrt(2))/(n!)^2; the analogous formula for the other S uses dW. The third determinant has an additional factorial factor and vanishes asymptotically. Therefore R/Y~-(dW/dV)W(0)/V(0). The identities dW/dV=sqrt(2)-1 and (1+lambda_-/lambda_+)/2=sqrt(2)-1 yield the complete quotient constant (sqrt(2)-1)^2.

The fixed-half-plane root/resolvent proof and local boundary kernel confirmed in primary review 33 are reused. The complex-segment moment functional L is not assumed to be a positive measure; its h_k alternate in sign. Positivity in the source concerns the transformed symbol/covariance and actual eventual quotient. It must not be confused with raw even/odd objects or a different positive-energy metric.

Conditions of use and limits relative to the main goal：

- The conclusion holds for sufficiently large n; the source supplies no explicit uniform threshold.
- The fact that p does not divide q_(p-1) removes only one prime factor. Other primes and every prime-power/gcd cost remain relevant.
- The primitive error still equals q|R/Y| exactly. The stated analytic constant improvement does not control log q.

Definite errors in the text: none were found in this object's actual assertions in this batch. The counterexamples or proof obligations above are not registered as errors in this document.


---

# D2366：hp_b2_cubic_maximal_minor_gate.md

Attribution：/root/organization_evidence

Mathematical verdict：**a valid all-depth local ideal theorem for large primes; no uniform bound on actual gcd depth is supplied**。

Original path：`work/session_20260927/hp_b2_cubic_maximal_minor_gate.md`

Original SHA-256: `7736790e3894ce58b43cc2810fca914c1e6a0f1e51029921ef4469817fe062b1`

Actual reading: complete source textL1–L279，9608characters，9608bytes; including status and dependencies, scope, and correction sections.

Copy of the original bytes：`[private local path removed]`

Existing primary review: review 27。

inherited primaryscope：All sections; p>2n+4 for valuation and endpoint assertions; polynomial identities themselves are universal; finite diagnostic claims not used

Specific source-text basis：

- L44–91: the equality for v_p(Omega) requires p>2n+4; actual endpoint depth only satisfies d_p<=v_p(Omega).
- L95–129: the raising/ODE/transition determinant is (n+1)^4/2; primitivity of the state is a local premise.
- L153–210: actual homogeneous elimination of the two minors and the unit-ideal conversion are correct.
- L222–270: the actual exceptional factor n^2+4n+1 in P(1) and the cutoff are retained. Simple Hensel lifting supplies no upper bound on depth.

Rederivation and valid usable conclusions：

Collecting cubic monomials directly gives uE+(nu+(n+2)h)D=-(n+1)C. The coefficients of h^3, h^2u, hu^2, and u^3 are respectively 2(n+1)(n+2), -4(n+1), -(n+1)(n-2), and -(n+1); every term containing v cancels. If h is a unit, subtracting (n+u/h) times the first column from the second reduces the minor ideal to (D,E). If u is a unit, this identity replaces it with (D,C); if u is not a unit, both are units. If h is not a unit, the primitive state and the values of the two minors/third minor ensure at least one unit. The all-depth formula therefore holds within the stated large-prime scope only.

The 11 formal-identity controls in B2_MAIN_FORMAL_CONTROL_RESULT.json and the actual primitive-kernel handoff in primary review 27 are reused. An additional local model takes n=2, p=11, h=1: f(u)=u^3+4u-8 has a simple root at u=7. Successive Hensel lifting to 11^6 and v=(6-2u-u^2)/u give D=0 with arbitrarily deep C. This model only shows that the local equations and separability cannot bound depth by themselves; it neither constructs an actual H_n nor refutes the source. Source lines 255–263 explicitly state this limitation.

Conditions of use and limits relative to the main goal：

- Every unit prefactor uses p>2n+4. A universal polynomial identity does not make its valuation conclusion universal at small primes.
- Large Omega does not imply a large actual endpoint gcd. A necessary condition cannot be reversed into a sufficient condition.
- A q rate still requires quantitative control of how closely the actual state approaches the cubic root, the depth of D, small primes, and complete endpoint content.

Definite errors in the text: none were found in this object's actual assertions in this batch. The counterexamples or proof obligations above are not registered as errors in this document.

Coordinates of independent exact small examples：

- [Complete results](OWN_EXACT_INTERFACE_EXAMPLES.json#/b2_arbitrary_depth_synthetic_equation_states); pointer `/b2_arbitrary_depth_synthetic_equation_states`。

Program written by the reviewer：[check_interface_examples_owned.py](check_interface_examples_owned.py)。


---

# D2621：WEIGHTED_REGULAR_DYADIC_SUBFAMILY.md

Attribution：/root/organization_evidence

Mathematical verdict：**valid integrality for an infinite regular subfamily and complete dyadic pair transfer**。

Original path：`work/session_20261002_codex_continuation/agent1_arithmetic/WEIGHTED_REGULAR_DYADIC_SUBFAMILY.md`

Original SHA-256: `f8fec8c888185dc0f14157e37df54176e72e8102cfe4fd0a4f370424b89024be`

Actual reading: complete source textL1–L272，14468characters，14801bytes; including status and dependencies, scope, and correction sections.

Copy of the original bytes：`[private local path removed]`

Existing primary review: review 8。

inherited primaryscope：Sections 1-8, coupled recurrence, coefficientwise 2-adic convergence, normalized differences, Gram residue, common arctangent filtration and complete-pair valuation; literature novelty not certified

Specific source-text basis：

- L66–113: value convergence and coefficientwise convergence of the coupled contraction have explicit depths, so every Delta^2 difference is valid.
- L115–179: period 15 of the F2 recurrence/state is an inductive certificate. Lucas anti-triangularity gives a unit Gram matrix at n=4^j+1.
- L183–201: the actual Gram solution is gamma_i=(D_n/D_i)(G^-1 w)_i, rather than a direct basis change without row scaling.
- L203–248: arctangent uses the same filtration in the h_i basis for every monomial multiplier, followed by transfer back to the actual y basis.
- L250–264: after complete gcd cancellation, q2=2+v2(η), with η nonzero. This manuscript does not claim the final exact next digit.

Rederivation and valid usable conclusions：

Each contraction of length a contains u(u−2)…(u−2a+2), so a fixed-degree coefficient has depth at least max(0,a−ℓ), while its value has depth at least a+v2(a!). The residue of the difference divided by 2^d d! is the dth Taylor coefficient. The common Gram scale for h_i and the mixed row give the γ_i filtration. The depth of R_at(z^a(z²−1)^d) is at least 1+d+v2(d!), so every term of P_n(z)·(2z−1)^s has depth at least σ+1. Multiplying by the actual q factor λ2^n gives V_s≥n+σ+1, sufficient to cover the same-y-basis gate 2σ+1 when i,j≤m. The D39 complete-pair theorem then gives the actual v2(q)=v2(w)−2σ.

The all-degree conclusion in this manuscript has a valid symbolic proof. Its use of a fixed F2 state does not make it an extrapolation from a finite scan. The full proof scope of primary review 8 is reused. This batch rederives transfer of the actual q normalization, the common arctangent filtration, and final gcd cancellation, without regenerating the historical n5/n17 values.

Conditions of use and limits relative to the main goal：

- The scope is n=4^j+1, j≥1. No all-n regularity or odd-content theorem is supplied.
- This manuscript gives only q2=2+v2η. The final depth of η uses D2623 and the finite-state input reviewed by the primary agent.
- Positivity is used only in A(zW²)>0 to prove P_n(0)≠0. The signed functional ℒ=A−eval is not itself positive definite.

Definite errors in the text: none were found in this object's actual assertions in this batch. The counterexamples or proof obligations above are not registered as errors in this document.


---

# D2623：WEIGHTED_REGULAR_EXACT_DYADIC_ENDPOINT_THEOREM.md

Attribution：/root/organization_evidence

Mathematical verdict：**a valid primary-reviewed regular exact-endpoint theorem; this review checks the transfer and explicitly reuses the finite-state proof**。

Original path：`work/session_20261002_codex_continuation/agent1_arithmetic/WEIGHTED_REGULAR_EXACT_DYADIC_ENDPOINT_THEOREM.md`

Original SHA-256: `8473e67123a188590fa1ebb6ac4be0ee3a514e5440a28332679ed619f464df56`

Actual reading: complete source textL1–L294，15502characters，15766bytes; including status and dependencies, scope, and correction sections.

Copy of the original bytes：`[private local path removed]`

Existing primary review: review 23。

inherited primaryscope：Sections 1-8; n=4^j+1,j>=1 only; all nine inspected certificate programs and two imported helper modules; original files preserved

Specific source-text basis：

- L7–45: the scope is only n=4^j+1; the theorem gives v2(w)=3n−2 and final q2=n+2.
- L49–87: U=P_n(0)/D_m² and q2=n+v2(U) are the actual complete-pair transfer.
- L123–186: the degree-10 to degree-4 identity and closure of the full state including phase justify the uniform conclusion. A scalar pattern alone is insufficient.
- L190–278: linear/carry boundaries and withdrawn residues are explicitly retained. Primary review 23 covers the closed inputs h1/3/5 and every odd h.
- L24–30, 294: choosing a positive denominator for the center requires choosing the numerator's sign consistently. No conclusion about odd content, total height, or irrationality is inferred.

Rederivation and valid usable conclusions：

The filtration and nine state receipts confirmed in primary reviews 8, 18, and 20–23 are reused. The primary replay closes complete polynomials/vectors together with phase; it does not merely observe a few U outputs equal to 4. This batch checks that Q²−σ(Q)(X²,Y²) is 2-divisible and that every correction in its fourth power is 8-divisible, which legitimately yields the Cartier transition. U=4 mod8 gives v2U=2. Since σ=n−2, v2P(0)=2σ+2=2n−2, v2w=n+v2P(0)=3n−2, and final q2=v2w−2σ=n+2.

The actual q2 gives q≥2^(n+2), which is still insufficient for comparison with the unknown weighted-center error and supplies no upper bound on odd factors. The three floating-point records at n8/16/32 in MAIN_WEIGHTED_REFLECTION_EXPLORATION_READING_RECEIPT.json were explicitly not accepted as proof evidence. This batch derives no positivity or error claim from those floating-point values.

Conditions of use and limits relative to the main goal：

- This batch does not rerun the nine original programs or claim independent recomputation of all their numerical states. It cites WEIGHTED_CERTIFICATE_REPLAY_RESULT.json and primary review 23 precisely.
- Computational inputs and the primary review's original scope are inherited unchanged. No all-n statement, odd-factor bound, or upper bound on total q is added.
- In general notation, set A=Dα, B=Dβ, and g=gcd(|A|,|B|): p=−sgn(B)A/g and q=|B|/g. Taking an absolute value only for q without adjusting p consistently gives the wrong center. Source line 30 already requires a common sign choice; this is a notation clarification, not a newly registered error.

Definite errors in the text: none were found in this object's actual assertions in this batch. The counterexamples or proof obligations above are not registered as errors in this document.


---

# D596：nonpolynomial_integral_hurwitz_pullback.md

Attribution：/root/organization_evidence

Mathematical verdict：**a valid specified analytic pullback and all-order Hurwitz integrality; the finite root-certificate scope is not expanded into an HP height theorem**。

Original path：`sources/nonpolynomial_integral_hurwitz_pullback.md`

Original SHA-256: `3ae2fb397de460360a589eec2c25bd30d96b7319cea501012763b7c9761dab56`

Actual reading: complete source textL1–L619，14323characters，14331bytes; including status and dependencies, scope, and correction sections.

Copy of the original bytes：`[private local path removed]`

Existing primary review: review 39。

inherited primaryscope：Complete analytic proof and finite exact root-exclusion certificate; numerical nearest roots, winding samples and search counts remain historical diagnostics

Specific source-text basis：

- L54–188: endpoint fixing, complete jet formulas for the exponential terms, the integer recurrence for F, and Bell-combinatorial closure are valid.
- L239–309: the finite degree-65 Cohn descent is correct and proves zero-freeness on the entire specified closed disk; this is not sampling-based exclusion.
- L311–459: the Schur boundary product retains the leading modulus √2; 2B²>T² supplies a strict Rouché margin.
- L493–520: puncture-preimage multiplicity still gives residue −2si. Compactness of the closed disk supplies a strict radius greater than r0.
- L524–619: nearest numerical roots and the single-term search are explicitly diagnostic only. No primitive HP height conclusion is supplied.

Rederivation and valid usable conclusions：

The equation (2−2w+w²)F′=4 gives f_(n+1)=n f_n−n(n−1)f_(n−1)/2. With f0=0 and f1=2, every f is an even integer. The jet of φ's exponential perturbation is k binom(n,m)(r a^(r−1)−a^r), hence integral. Bell partition coefficients are integers, so every jet of G is an even integer. The finite stages of the root certificate give a conclusion for every point of the specified disk through strict Cohn comparison and Rouché induction. This is neither an infinite HP-degree scan nor an integrality inference from only 121 jets.

The real endpoint branch of φ on [0,1] can be integrated directly using F′=4/((w−1)²+1), yielding π. The arctangent-coordinate expression at w=2 introduces no actual new singularity. The primary reviewer's strict zero-free margin is reused; uncertified nearest-root numbers are not treated as upper bounds or optimality theorems.

Conditions of use and limits relative to the main goal：

- Primary review 39 and the two finite root certificates/121 jets independently reconstructed in HURWITZ_MAIN_CERTIFICATE_RECONSTRUCTION.json are reused. The original research code is not rerun.
- Radius>1.7679119 concerns this specific φ; it cannot replace the original F or be generalized to an arbitrary pullback.
- All-order integrality follows from recurrence/Bell arguments, not from the 121-jet data. Primitive endpoint heights remain unbounded by this result.

Definite errors in the text: none were found in this object's actual assertions in this batch. The counterexamples or proof obligations above are not registered as errors in this document.

Coordinates of independent exact small examples：

- [Complete results](OWN_EXACT_INTERFACE_EXAMPLES.json#/F_jets_0_through_8); pointer `/F_jets_0_through_8`。

Program written by the reviewer：[check_interface_examples_owned.py](check_interface_examples_owned.py)。


---

# D595：nonpolynomial_integral_hurwitz_hp_diagnostic.md

Attribution：/root/organization_evidence

Mathematical verdict：**the finite diagnostics are correct and explicitly yield no all-degree conclusion; no mathematical error was found in the source**。

Original path：`sources/nonpolynomial_integral_hurwitz_hp_diagnostic.md`

Original SHA-256: `aa93d76dea21a3d7ab24bd40362d6948c8586df11fc7e7138866247e6b79f78b`

Actual reading: complete source textL1–L119，4150characters，4163bytes; including status and dependencies, scope, and correction sections.

Copy of the original bytes：`[private local path removed]`

Existing primary review: review 42。

inherited primaryscope：Complete diagnostic manuscript, integer-jet generation, high system and table; main uses independently chosen exact endpoint intervals rather than comparing the historical interval endpoint hashes

Specific source-text basis：

- L13–16: the source explicitly covers only n1..15 and asserts no uniform rank, nonvanishing, content/height, or asymptotic result.
- L58–90: the finite table retains the n1 endpoint (0,0) alongside full row rank and a nonzero first free jet; no implication between these is claimed.
- L94–119: JSON and program references are historical proof-evidence coordinates. The primary reviewer independently reconstructed 15 systems; this batch does not turn an old PASS into a new review.

Rederivation and valid usable conclusions：

Primary review 42 and the 15 exact system reconstructions in HURWITZ_MAIN_HP_RECONSTRUCTION.json are reused. This batch only adds the minimum interface rederivation: φ=z+O(z^7), so G=F through z^4. The high-row matrix is [[1/2,1,1,2],[1/6,1/2,1/3,1],[1,1,−1,−1]], with rank 3 and kernel (B0,B1,C0,C1)=(2,−2,−1,1). The low row gives A=−2+2z. Its R=z^4/12+O(z^5), but A(1)=B(1)=C(1)=0. The stored version may choose the overall negative ray and thus free coefficient −1/12, which is fully consistent.

This manuscript belongs in the category of valid finite diagnostics. Failure to prove an all-degree result that it never asserts is not an error. The small example helps choose the correct proof obligation for continuation; database review statuses are neither upgraded nor merged.

Conditions of use and limits relative to the main goal：

- The n1 example only excludes the extra universal implication that full rank or a nonzero first jet implies a nonzero endpoint. It does not refute an eventual result or a specified subfamily.
- Actual growth at n2..15 concerns those 15 finite records only. It is neither all-n divergence nor route exclusion.

Definite errors in the text: none were found in this object's actual assertions in this batch. The counterexamples or proof obligations above are not registered as errors in this document.

Coordinates of independent exact small examples：

- [Complete results](OWN_EXACT_INTERFACE_EXAMPLES.json#/n1_actual_HP_endpoint_counterexample); pointer `/n1_actual_HP_endpoint_counterexample`。

Program written by the reviewer：[check_interface_examples_owned.py](check_interface_examples_owned.py)。


---

# D2615：SINGLE_JET_ACTUAL_DENOMINATOR_CANCELLATION.md

Attribution：/root/organization_evidence

Mathematical verdict：**a valid exact denominator-cancellation construction and conditional error interface; a useful residue remains unproved**。

Original path：`work/session_20261002_codex_continuation/agent1_arithmetic/SINGLE_JET_ACTUAL_DENOMINATOR_CANCELLATION.md`

Original SHA-256: `023a5576cd1834095c05169c9beb790bc86200aa11aac9731bab4b0faec26d30`

Actual reading: complete source textL1–L103，7980characters，8000bytes; including status and dependencies, scope, and correction sections.

Copy of the original bytes：`[private local path removed]`

Existing primary review: review 38。

inherited primaryscope：All generic polynomial-family proofs; eventual analyticity for r<min(2,Rbase), and stronger conclusions only under the stated small-residue condition; bounded author receipt not rerun

Specific source-text basis：

- L5–40: Z_N is odd for even N. The chosen K makes the final denominator exactly 2^f, with the complete e+G response retained.
- L44–62: the exact disk-norm equality contains 2^s2(N), and the worst-case threshold is 2. This is not a radius ceiling for every construction.
- L64–85: a small residue is equivalent to a restricted dyadic approximation of the target S, which the source explicitly does not derive.
- L87–103: partial cancellation gives only a denominator divisor, retaining the remaining odd gcd. The four finite modified maps have no new radius certificate.

Rederivation and valid usable conclusions：

All jets of G are even and all jets of H=e^z+G are odd. For even N, N!/j! is even when j<N, so Z_N is odd. Choosing 2K≡−Z modO_N makes L=(Z+2K)/O_N odd, with final denominator exactly 2^f_N. The only new first jet in P_N−P changes the Taylor sum by exactly 2K/N!, using F′(0)=2. At z=−r, both |z|^N=r^N and |1−z|=1+r are attained, giving norm=(1+r)α_N2^s2(N)(r/2)^N. If the fixed base radius is greater than 2, Cauchy's estimate gives 2^f_N|S−c_N|→0, and this tail controls the difference between the actual scaled error and 2α_N.

The complete generic proof scope of primary review 38 is reused. The reviewer's finite N4, P=z example gives c4=145/24, K=1, and c4new=49/8; it only checks final gcd cancellation and does not claim radius>2 for P=z. For fixed r>2, the norm condition is stronger than α_N→0. Exact odd cancellation is valid; failure to meet the error budget does not make the manuscript incorrect.

Conditions of use and limits relative to the main goal：

- Retain the fixed base omitted-value disk and branch conditions. For arbitrary r>2, α_N needs an exponentially small bound, which a general center congruence does not supply.
- α_N→0 is equivalent to this restricted dyadic approximation and remains unproved in the current material. Integral jets cannot replace it.
- An irrationality contradiction also requires nonvanishing. Odd L_N excludes eventual equality of rational S with L_N/2^f_N.

Definite errors in the text: none were found in this object's actual assertions in this batch. The counterexamples or proof obligations above are not registered as errors in this document.

Coordinates of independent exact small examples：

- [Complete results](OWN_EXACT_INTERFACE_EXAMPLES.json#/single_jet_N4_exact_denominator_example); pointer `/single_jet_N4_exact_denominator_example`。

Program written by the reviewer：[check_interface_examples_owned.py](check_interface_examples_owned.py)。


---

# D2677：WEIGHTED_DIFFERENCE_BLOCK_NONVANISHING.md

Attribution：/root/organization_evidence

Mathematical verdict：**the explicitly conditional theorem is valid; two foundational lemmas were independently confirmed, while parent inputs needed for application remain usage obligations**。

Original path：`work/session_20261002_codex_continuation/agent2_selector/WEIGHTED_DIFFERENCE_BLOCK_NONVANISHING.md`

Original SHA-256: `5c6182ae48f06523eb047811ab185aa40858a435fef2062ae3d8a41a1f52215b`

Actual reading: complete source textL1–L244，16409characters，16844bytes; including status and dependencies, scope, and correction sections.

Copy of the original bytes：`[private local path removed]`

Existing primary review: absent at the snapshot date; this report does not write to the database.

Inherited primary scope: none; this report supplies its own explicitly conditional review only.

Specific source-text basis：

- L3, 55–81: the phase and interpolation lemmas have independent proofs. The author explicitly retains the relative-saddle parent inputs.
- L85–111: the ratio phase gives a nonzero certificate in one nearby block, rather than nonvanishing for every start.
- L113–198: the primitive bound retains the complete β and α errors, both odd LCMs, and the H³ cost.
- L200–244: the rational selection rule and leading-rate PNT refinement are valid under the stated parent inputs. The ρ boundary remains open.

Rederivation and valid usable conclusions：

If adjacent phase decreases for four nonzero complex numbers all lie in [2π/5,3π/5], the total decrease is at least 6π/5. They cannot all remain in a single interval of length π where sin≥0; crossing to the next such interval requires a decrease of at least π, contradicting the one-step upper bound. The same argument applies to sin≤0, so both strict signs occur. If Δ^d vanishes for N=4(d+r) samples, those samples agree with a polynomial of degree at most d−1. Divide them into d+r disjoint four-node intervals. A degree-r polynomial u can spoil at most r intervals. At least d remaining intervals exhibit strict sign changes, forcing d distinct roots in a nonzero p, a contradiction. Thus, for d=n+1 and r=n/2 in this manuscript, N=6n+4, there are 5n+3 certificate starts, and the furthest direct node is 6n+3. The counts agree with the complete support.

Recomputing the bound gives B*=1/(2^r O_L H²), q≥2(Cε/E*)^(1/(2+ε))/(O_N H), and combined q|c−S|≥(Cε/E*)^(1/(2+ε))/(2^r O_N O_L H³), retaining both 4ρ LCM costs. The leading rate is therefore 1/2−8ρ in the PNT version. Selecting rational p within B*/8 of π makes the actual β difference at least 3B*/4; E*≤B*/4 then retains complete error at least B*/2. Closure of the all-parity root argument cannot replace these parents.

Conditions of use and limits relative to the main goal：

- The actual ratio J_(m+1)/J_m and uniform domain come from D2476. It was pending at this database snapshot, and its saddle proof was not independently reviewed here.
- Actual identities, the W lattice, the β denominator, and the complete α remainder come from D2399 and its parents. The full parent chain is not expanded in this batch.
- Accepting these named inputs yields primitive divergence for the selected family: elementary ρ<1/(16log4), or PNT ρ<1/16. The conclusion does not extend to all weighted/raw/b1/b2 families.
- Unreviewed parent inputs remain obligations for use. The author states the conditions explicitly, so their unresolved status does not make the manuscript incorrect.

Definite errors in the text: none were found in this object's actual assertions in this batch. The counterexamples or proof obligations above are not registered as errors in this document.
