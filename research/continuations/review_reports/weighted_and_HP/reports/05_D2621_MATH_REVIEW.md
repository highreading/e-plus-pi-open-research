> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

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
