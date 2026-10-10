> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

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

- [Complete results](../OWN_EXACT_INTERFACE_EXAMPLES.json#/n1_actual_HP_endpoint_counterexample); pointer `/n1_actual_HP_endpoint_counterexample`。

Program written by the reviewer：[check_interface_examples_owned.py](../check_interface_examples_owned.py)。
