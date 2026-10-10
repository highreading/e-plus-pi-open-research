> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Nonvanishing of the b=2 endpoint numerator on indices congruent to four modulo five

Status: UNVERIFIED CANDIDATE
Author: worker_2
Content SHA256: c45a87ae1556ffd2f129849b6d56ae3d029a23a6371b52174e3add2998ec7533

UNVERIFIED SYNTHESIS CANDIDATE. Independent review is required. This claim concerns the specified rational endpoint family and establishes no rationality or irrationality statement about e+pi.

STATEMENT AND EXACT DEFINITIONS

For every integer n≥4 with n≡4 (mod 5), put m=n+1 and f=2^n/(n!)². Use the following exact rational endpoint contractions.

Define L_j(t)=(1/j!)(d/dt)^j(1−2t+2t²)^j, P=L_n, U=L_m, a=P(1), and b=U(1). Let ℒ(Q)=∫_{−1}^1 Q((1+iu)/2)du, where i²=−1. Its monomial moments are rational. Set
w_P=ℒ((P(t)−a)/(t−1)),
w_U=ℒ((U(t)−b)/(t−1)),
E_j=Σ_{h=0}^j1/h!,
T_0(Q)=Σ_d[t^d]Q(t)E_{n+d},
P*=w_P+T_0(P), and U*=w_U+T_0(U).

For j≥0 define
H_j(x)=j![z^j]exp(xz)(1−z+z²/2)^j,
h_j=H_j(1),
J_j=jh_j+H′_j(1),
K_j=j(j−1)h_j+2jH′_j(1)+H″_j(1).

Put
S=J_m²−h_mK_m,
C=(J_m−h_m)J_n−(K_m−J_m)h_n,
W=J_mJ_n−K_mh_n,
D=m²bC−2aS,
X=2P*S−m²U*C−2fh_mW,
Z_n=X/(fm).

Then D≠0, X≠0, and Z_n≠0 for every n≥4 on this progression. For n≥9 on the progression, the additional conclusion is
Z_n∈5Z_5\{0}, hence 1≤v_5(Z_n)<∞.

The proof imports the published local endpoint statements listed below with precisely these definitions. Their underlying local arithmetic proofs are dependencies of this synthesis.

PROOF

1. Establish the denominator hypothesis first.

The published residue-four theorem gives
v_5(D)=v_5(n+1)<∞
for every n≥4 with n≡4 (mod 5). Thus D≠0 at each individual index under consideration. Define q_n=den(X/D), taking the positive reduced denominator and den(0)=1. The alternative endpoint convention −X/D has exactly the same denominator.

The published common endpoint scaling is A_raw(1)=γX and B_raw(1)=γD, where γ=(−1)^n/[4(n+1)^3(n!)^4]≠0. Consequently all imported denominator statements concern this same q_n, irrespective of primitive coefficient normalization.

2. Check all ternary index restrictions and strict positivity.

Write r_3=v_3(n!). The progression n≥4, n≡4 (mod 5), splits exhaustively into the following three cases, with k≥0.

• n=4+15k. Then n≡1 (mod 3) and n≥4. The published residue-one theorem applies because D≠0 was established in step 1. It gives
v_3(q_n)=2r_3+v_3(D)≥2r_3+1>0.
This case includes n=4; no eventual threshold is used.

• n=9+15k. Then 3 divides n and n≥9, satisfying the multiples-of-three theorem's threshold n≥3. It gives
v_3(q_n)=2r_3>0.

• n=14+15k. Then n≡2 (mod 3) and n≥14, satisfying the residue-two theorem's threshold n≥5. It gives
v_3(q_n)=2r_3>0.

Strict positivity follows because n≥4 implies r_3≥1. In particular, every relevant index has v_3(q_n)≥2r_3>0. For n≥9 this also gives v_3(q_n)≥8.

3. Deduce numerator nonvanishing.

If X=0, then D≠0 implies X/D=0. Its positive reduced denominator would be q_n=1, forcing v_3(q_n)=0, contrary to step 2. Therefore X≠0. Since fm is a nonzero rational number, Z_n=X/(fm)≠0 as well.

None of the three imported denominator statements assumes X≠0. Their restrictions are the displayed index conditions and, for residue one, D≠0. The contradiction therefore has no circular nonvanishing assumption.

4. Combine with the separately published divisibility assertion.

For n≥9 with n≡4 (mod 5), the published residue-four theorem additionally gives Z_n∈5Z_5, allowing zero in that original assertion. Step 3 excludes zero, so v_5(Z_n) is a finite positive integer. No divisibility assertion at n=4 is imported or inferred.

DEPENDENCIES

All paths below are project-relative. Hashes identify reviewed payloads, not complete files with registry headers.

1. work/astra_review_registry/verified/main-b2-five-adic-residue-four-cancellation-v1.md
Payload SHA-256: b123168c159b9a62d863ee40ffdae485533f2229e99c368b6cd671e04f321519.
Used for v_5(D)=v_5(n+1) at n≥4 on the progression and Z_n∈5Z_5 only at n≥9.

2. work/astra_review_registry/verified/b2-ternary-endpoint-denominator-and-content-v1.md
Payload SHA-256: 6baaa17575ed30467e01de61e4c861e97987c07a31f331cc6821f2b850f05dfe.
Used only for the actual reduced-denominator formula when 3 divides n and n≥3.

3. work/astra_review_registry/verified/worker2-b2-ternary-residue-two-exact-denominator-v1.md
Payload SHA-256: ba51fc9529c4fe1ea78ad46225229d224dc4c5ac36b4b80e067017230642ce38.
Used for the actual reduced-denominator formula when n≡2 (mod 3) and n≥5.

4. work/astra_review_registry/verified/worker4-b2-ternary-residue-one-conditional-denominator-v1.md
Payload SHA-256: 5268f1e9d2b38f15e4b00b9918dd6c98f6f57dcac0b6a75fc046e5bbb7738082.
Used for the conditional denominator formula when n≡1 (mod 3), n≥4, and D≠0.

5. work/astra_review_registry/verified/b2-two-chart-actual-denominator-identities.md
Payload SHA-256: ace0c8602da8ebb959a140d0a8e4dd9caf532014dc653f5328e909389ca4280d.
Used for the exact rational endpoint identification and common scaling. Its large-prime local-ideal theorem is not applied at three or five.

EVIDENCE AND SCOPE

The original deduction for n≥9 appears in work/astra_20260929/main/note_000175.md. Source comparisons and the completed preparatory audit are preserved in work/astra_20260929/worker_2/note_000130.md and note_000131.md. The inclusion of n=4 is recorded in note_000132.md and proved explicitly above.

This argument uses no analytic error asymptotic, unspecified eventual-nonvanishing threshold, coefficient-content estimate, or numerical experiment. It changes no previously reviewed payload. The new synthesis requires independent approval.

The conclusion 1≤v_5(Z_n)<∞ for n≥9 is pointwise finiteness only. No numerical, logarithmic, sublinear, or other quantitative upper bound as n varies is established. The growth of v_5(Z_n), the required control of actual reduced denominators, and the rationality of e+pi remain unresolved.