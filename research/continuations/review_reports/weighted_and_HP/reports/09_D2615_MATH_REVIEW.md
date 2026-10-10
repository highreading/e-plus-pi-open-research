> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

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

- [Complete results](../OWN_EXACT_INTERFACE_EXAMPLES.json#/single_jet_N4_exact_denominator_example); pointer `/single_jet_N4_exact_denominator_example`。

Program written by the reviewer：[check_interface_examples_owned.py](../check_interface_examples_owned.py)。
