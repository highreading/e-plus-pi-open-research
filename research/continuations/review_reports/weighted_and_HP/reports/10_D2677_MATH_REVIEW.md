> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

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
