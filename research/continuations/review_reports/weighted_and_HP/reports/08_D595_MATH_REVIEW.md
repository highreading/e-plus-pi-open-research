> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

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

- [Complete results](../OWN_EXACT_INTERFACE_EXAMPLES.json#/n1_actual_HP_endpoint_counterexample); pointer `/n1_actual_HP_endpoint_counterexample`。

Program written by the reviewer：[check_interface_examples_owned.py](../check_interface_examples_owned.py)。
