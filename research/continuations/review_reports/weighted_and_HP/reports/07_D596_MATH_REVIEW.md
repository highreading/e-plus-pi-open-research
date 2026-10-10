> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

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

- [Complete results](../OWN_EXACT_INTERFACE_EXAMPLES.json#/F_jets_0_through_8); pointer `/F_jets_0_through_8`。

Program written by the reviewer：[check_interface_examples_owned.py](../check_interface_examples_owned.py)。
