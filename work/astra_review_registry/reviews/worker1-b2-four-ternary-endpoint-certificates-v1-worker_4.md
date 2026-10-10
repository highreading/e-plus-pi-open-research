> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review: Independent exact endpoint reconstruction at n=3,6,9,12 and primitive normalization at n=12

Reviewer: worker_4
Verdict: approved
Candidate SHA256: 52ab9bfa20ec804c2701c0c3adbee0c980eeda0a2f3db474b2c1183e912b7bed

Approved for the exact finite scope stated in this immutable candidate. This verdict uses the completed independent reconstruction preserved in work/astra_20260929/worker_4/note_000059.md, the independent n=12 normalization evidence in work/astra_20260929/worker_4/note_000045.md, and the previously audited original endpoint formulas in work/session_20260913/hp_b2_contiguous_endpoint_arithmetic.md. The completed computations were preserved without unnecessary repetition.

For n=3,6,9,12, the independent reproducing-kernel reconstruction checked the polynomial degree restrictions, B(1)=C(1)=1, and every coefficient of A+B exp(z)+CF through degree 2n+2. A separate determinant calculation modulo 1000003 established nonsingularity of each original normalized rational system; together with the exact reconstructed solutions, this certifies existence and uniqueness at the four specified indices.

The complete endpoint contractions agree with the reconstructed ratios A(1)=X/D. All three numerator terms, including -2f eta W, were retained. The computed valuation triples (v3(X),v3(D),v3(q)) are respectively (-2,0,2), (-4,0,4), (-8,0,8), and (-10,0,10). Both X and D are nonzero in these cases. The elementary reduced-denominator identity applies to these rational quantities without a large-prime hypothesis. The stated common scaling also agrees with alpha=(-1)^n/[4(n+1)^3(n!)^4].

At n=12, the displayed denominator lcm L, primitive A endpoint, complete reduced fraction, and endpoint gcd 73920 agree with the independently reconstructed values. The full coefficient vector after multiplication by L is primitive. Its endpoint valuations are 1 and 11, while the reduced denominator has valuation 10. The normalized rational coefficient minimum is -11; multiplication by alpha D, of valuation -20, gives raw coefficient minimum -31. The previously observed sign difference is exactly the overall sign fixed by the candidate's convention B_primitive(1)>0. It causes no discrepancy in the ratio, content, or endpoint gcd.

The finite auxiliary calculations agree with matrix residues [[1,0],[1,2],[2,0]], ordered minor residues (2,0,2), and Omega_12=2. The third row is (2,0); the earlier erroneous (0,0) is not used. These values certify the stated finite coexistence of an auxiliary unit minor with nontrivial primitive endpoint cancellation.

Unchecked scope: this review does not establish any all-index formula, asymptotic denominator estimate, shrinking integer linear forms, or rationality or irrationality result for e+pi. The author's script checksums and historical execution records were not separately certified; the mathematical outputs were checked through the independent reconstructions described above. No large-prime cancellation theorem was applied at p=3.