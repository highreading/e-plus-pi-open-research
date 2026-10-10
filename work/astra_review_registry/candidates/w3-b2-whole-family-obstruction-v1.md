> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Conditional eventual divergence of the complete matched b=2 integer-form family

Status: UNVERIFIED CANDIDATE
Author: worker_3
Content SHA256: 11539d8ac13528b29c5f4b8eda1eecfaa7e9ccad01860739b3f506d8de26a0d5

UNVERIFIED SYNTHESIS submitted by worker_3 for independent review. The residue-four hypothesis H4 below is an explicitly unapproved dependency. All other imported results are published. This claim concerns one fixed approximation family and its nonzero integer multiples.

DEFINITIONS

Put ξ=e+π and ρ=1+√2. For n≥2 define
L_m(t)=(1/m!)(d/dt)^m(2t²−2t+1)^m,
P=L_n, U=L_{n+1}, a=P(1), b=U(1), k=(n+1)², f_n=2^n/(n!)².
Here b is an endpoint value; the exponential degree is fixed at two throughout.

Let ℒ(Q)=∫_{−1}^1 Q((1+iu)/2)du, E_j=Σ_{h=0}^j1/h!, T_n(Q)=Σ_d[t^d]Q(t)E_{n+d}, and w(Q)=ℒ((Q(t)−Q(1))/(t−1)). Define P*=w(P)+T_n(P) and U*=w(U)+T_n(U). These are rational quantities.

Define H_m(x)=m![s^m]e^{xs}(1−s+s²/2)^m,
h_m=H_m(1), J_m=mh_m+H'_m(1),
K_m=m(m−1)h_m+2mH'_m(1)+H''_m(1).
Set
S_n=J_{n+1}²−h_{n+1}K_{n+1},
C_n=(J_{n+1}−h_{n+1})J_n−(K_{n+1}−J_{n+1})h_n,
W_n=J_{n+1}J_n−K_{n+1}h_n,
D_n=kbC_n−2aS_n,
X_n=2P*S_n−kU*C_n−2f_nh_{n+1}W_n.
Here C_n is a scalar, distinct from the polynomial C_raw below. Whenever D_n≠0, write p_n/q_n=−X_n/D_n in lowest terms with p_n∈Z and q_n>0.

EXPLICIT PENDING HYPOTHESIS

(H4) For every n≥14 with n≡4 modulo five, Z_n=X_n/[f_n(n+1)] satisfies Z_n≡20 modulo 25 in Z_5.

H4 is the precise conclusion submitted in work/astra_review_registry/candidates/w3-b2-five-residue-four-loss-v1.md, payload SHA256 e08cc00ef7c40a2bdfda278145fa8330dbac4fbc58b3723fe44b76131acf8e43. It is under independent review at this submission. This synthesis assumes H4 and does not certify its proof. In particular no assertion at n=9 is imported.

STATEMENT

There exists an integer N_D such that D_n≠0 for all n≥N_D, by the published endpoint identification and analytic nonvanishing theorem. Conditional on H4, for every n≥N_A=max(14,N_D),
q_n≥3^{2v_3(n!)}5^{2v_5(n!)−1}≥(3√5)^n/(1125n^4).

There is a separate unspecified integer N_E such that, for all n≥max(N_A,N_E),
|q_nξ−p_n|≥[2π/(1125ρ³)]n^{−4}[3√5/ρ²]^n.
Thus |q_nξ−p_n| tends to infinity. Every sequence of nonzero integer multiples of these forms also tends to infinity in absolute value. No unbounded subsequence of these forms tends to zero.

IDENTIFICATION AND ANALYTIC INPUT

The published two-chart reconstruction gives rational polynomials (A_raw,B_raw,C_raw), with degree caps (n,2,n), satisfying
R_raw(z)=A_raw(z)+B_raw(z)e^z+C_raw(z)F(z)=O(z^{2n+3}),
F(z)=4 arctan(z/(2−z)),
A_raw(1)=γ_nX_n,
B_raw(1)=C_raw(1)=γ_nD_n,
γ_n=(−1)^n/[4(n+1)^3(n!)^4]≠0.

The published exact identification gives Y_cof=γ_nD_n/d_{n+1}, with d_{n+1}=2^{n+1}binom(2n+2,n+1)≠0, and identifies the complete raw triple with d_{n+1} times the matched cofactor triple. Every formula uses the same index n; the auxiliary polynomial L_{n+1} introduces no shift. Published eventual Y_cof≠0 therefore supplies N_D.

At the endpoint, F(1)=π and
R_raw(1)/B_raw(1)=ξ+X_n/D_n=ξ−p_n/q_n.
Converting to the transfer-v2 convention requires A_minus=−A_raw, so R_raw=B_raw e^z+C_raw F−A_minus. Its approximant A_minus(1)/B_raw(1) remains −X_n/D_n. Consequently the published transfer-v2 theorem, including its ordinary Padé prefactor dependency, gives
|ξ−p_n/q_n|=(4π/ρ³)ρ^{−2n}(1+o(1)).
This is a fixed-degree statement. Its positive leading constant supplies eventual nonzero error and a threshold N_E for the lower bound with constant 2π/ρ³. N_E need not equal N_D, and neither threshold is made effective here.

ARITHMETIC COMBINATION

Write r_p=v_p(n!). The following are scoped conclusions of the published local records, except for the explicitly marked use of H4. All concern the complete X_n,D_n above and hence the same reduced denominator q_n.

For ternary residues: if n≥3 and n≡0 modulo three, v_3(q_n)=2r_3; if n≥4 and n≡1 modulo three, D_n≠0 implies v_3(q_n)=2r_3+v_3(D_n)≥2r_3+1; if n≥5 and n≡2 modulo three, v_3(q_n)=2r_3. These sufficient ranges cover all n≥14 once D_n≠0 is supplied.

For five-adic residues zero, one, and two, the respective published ranges n≥5, n≥6, and n≥7 give v_5(q_n)=2r_5. For residue three, n≥8 and D_n≠0 give v_5(q_n)=2r_5+v_5(D_n)≥2r_5+1. The latter is not asserted equal to 2r_5.

For residue four, the published cancellation identity gives v_5(D_n)=v_5(n+1) and, for n≥9,
v_5(q_n)=max(0,2r_5−v_5(Z_n)).
H4 gives v_5(Z_n)=1 for n≥14 on this progression. Here r_5≥2, so v_5(q_n)=2r_5−1. The separate numerator-nonvanishing supplement is unnecessary: H4 itself implies Z_n≠0 in this range.

It follows for n≥N_A that v_3(q_n)≥2r_3 and v_5(q_n)≥2r_5−1. Both exponents are nonnegative. Unique prime factorization therefore gives
3^{2r_3}5^{2r_5−1} divides q_n.
No coefficient-content or auxiliary maximal-minor estimate is used.

DIGIT BOUND AND GROWTH

Let s_p(n) be the base-p digit sum. Legendre's formula gives
3^{2r_3}5^{2r_5−1}=(3√5)^n/[5·3^{s_3(n)}·5^{s_5(n)/2}].
For n≥1, s_p(n)≤(p−1)(floor(log_p n)+1). Thus
3^{s_3(n)}≤9n²,
5^{s_5(n)/2}≤25n².
Their product with five is at most 1125n^4, proving the stated denominator bound.

Multiplying by the independently supplied eventual error lower bound proves the form inequality. Its exponential base exceeds one because √5>2 and 2√2<3 give
3√5>6>3+2√2=ρ².
An exponential with base greater than one dominates n^4, proving divergence.

Finally, if integers u_n,v_n with v_n≠0 satisfy u_n/v_n=p_n/q_n, reducedness implies (u_n,v_n)=j_n(p_n,q_n) for a nonzero integer j_n. Hence
|v_nξ−u_n|=|j_n|·|q_nξ−p_n|≥|q_nξ−p_n|.
An integer polynomial normalization of the matched triple has this property at the endpoint, after using u_n=−A(1) and v_n=B(1). Polynomial primitiveness does not require endpoint coprimality and is not needed for the argument.

PUBLISHED DEPENDENCIES

All paths below are under work/astra_review_registry/verified/:
1. b2-two-chart-actual-denominator-identities.md: exact rational reconstruction and common scaling only; no large-prime local ideal is applied at three or five.
2. w3-b2-eventual-d-nonzero-v1.md: exact same-index identification and eventual D_n≠0; its published determinant dependencies remain included.
3. worker2-fixed-b-projection-and-error-transfer-v2.md: fixed-degree error transfer, including its published ordinary Padé prefactor dependency.
4. b2-ternary-endpoint-denominator-and-content-v1.md: ternary residue zero.
5. worker4-b2-ternary-residue-one-conditional-denominator-v1.md: conditional ternary residue one.
6. worker2-b2-ternary-residue-two-exact-denominator-v1.md: ternary residue two.
7. b2-five-adic-endpoint-denominator-v1.md: five-adic residue zero.
8. worker4-b2-five-adic-residue-one-exact-denominator-v1.md: five-adic residue one.
9. worker4-b2-five-adic-residue-two-exact-denominator-v1.md: five-adic residue two.
10. w3-b2-five-residue-three-loss-v1.md: five-adic residue three, conditional on D_n≠0.
11. main-b2-five-adic-residue-four-cancellation-v1.md: residue-four denominator valuation and cancellation identity.

Supporting synthesis provenance, not additional assumed theorems: work/astra_20260929/worker_4/note_000119.md and work/astra_20260929/main/note_000189.md and note_000194.md. Their historical status statements are superseded by the registry at submission. No finite numerical calculation is used as proof here.

SELF-AUDIT AND LIMITS

H4 remains an unapproved hypothesis, and this synthesis itself awaits independent review. Arithmetic applicability begins at max(14,N_D); the nonzero-error lower bound has a separate eventual threshold. Sign conversion preserves the approximant, and the identification introduces no index shift. The conclusion covers these matched rational approximants and their nonzero integer multiples. It covers neither combinations of different approximants nor other approximation families nor growing exponential degree. It proves no rationality or irrationality assertion about e+π.