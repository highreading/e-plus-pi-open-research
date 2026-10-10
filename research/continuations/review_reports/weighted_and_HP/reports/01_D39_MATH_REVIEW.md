> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

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

- [Complete results](../OWN_EXACT_INTERFACE_EXAMPLES.json#/synthetic_normalized_weighted_polynomial_without_orthogonality); pointer `/synthetic_normalized_weighted_polynomial_without_orthogonality`。
- [Complete results](../OWN_EXACT_INTERFACE_EXAMPLES.json#/integer_symmetric_operator_counterexample); pointer `/integer_symmetric_operator_counterexample`。

Program written by the reviewer：[check_interface_examples_owned.py](../check_interface_examples_owned.py)。
