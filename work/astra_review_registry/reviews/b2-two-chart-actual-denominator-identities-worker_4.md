> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review: Exact two-chart ideals and reduced-denominator valuations for the b=2 endpoint pair

Reviewer: worker_4
Verdict: approved
Candidate SHA256: ace0c8602da8ebb959a140d0a8e4dd9caf532014dc653f5328e909389ca4280d

I independently reviewed the assigned immutable payload and compared it with the completed reconstruction and checks preserved in work/astra_20260929/worker_4/note_000011.md through note_000014.md. No mathematical defect was identified within its stated scope.

The original endpoint formulas checked were those in work/session_20260913/hp_b2_contiguous_endpoint_arithmetic.md, equations (1)–(13): the Legendre moment functional, endpoint and partial-exponential contractions, cross-product reconstruction, and H_m scalar identities. The candidate additionally cites hp_b2_endpoint_attempt.md for projection and endpoint definitions; I do not claim a complete independent reading of that additional file. The required projection, polynomial order conditions, and endpoint identification were instead independently reconstructed from the stated F and Legendre definitions using the reproducing kernel, as recorded in note_000013.md.

The complete numerator is retained: X=2P*S−kU*C−2fηW, including both partial-exponential contractions and the correction −2fηW. Determinant expansion and Rodrigues' identity give Y_raw=αD and X_raw=αX with the same nonzero α=gf/(Gk). Consequently the rational ratio is unchanged by this scaling or by any subsequent common primitive normalization. Approval does not identify separate primitive endpoint valuations without the appropriate coefficient-content correction, and the ratio identity does not require the separate normalization claim.

For p>2n+2, the stated moment and factorial denominators ensure p-integrality, and G is a unit. The Wronskian aw_U−bw_P=G therefore proves that at least one of a,b is a unit. Direct expansion gives bX+U*D=2(VS−bfηW) and aX+P*D=kVC−2afηW. The corresponding changes of generators have determinants b/2 and a, respectively, which are units on their stated charts. Thus both ideal equalities hold at every prime-power depth, with compatible results where the charts overlap.

For D≠0, the reduced-denominator identity v_p(q)=v_p(D)−min(v_p(D),v_p(X)) follows directly from rational reduction. Substitution of either equal ideal proves the claimed chart formulas. The convention v_p(0)=+∞ handles X=0 and zero chart generators; D=0 remains excluded from every ratio statement.

Independent exact symbolic checks verified reconstruction, common scaling, both chart identities, and compatibility. Five exact examples n=2 through 6 also verified polynomial order conditions and endpoints, obtaining reduced denominators 502, 414090, 1579037328, 6908572362600, and 260737140696321600. These are finite supporting checks, not growth estimates.

Approval certifies only the stated exact identities and conditional implications. It does not certify eventual normality or denominator nonvanishing, any extension to excluded small primes, a quantitative cancellation or denominator bound, or irrationality of e+π.