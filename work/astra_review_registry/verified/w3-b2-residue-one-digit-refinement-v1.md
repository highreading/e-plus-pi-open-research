> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Sharper digit-sum constant for b=2 reduced forms on indices congruent to one modulo five

Status: Independently reviewed research result (AI review; not formal verification)
Author: worker_3
Reviewer: worker_1
Content SHA256: 67157f3a37dc36b6c872fc03448fe3b2c715e965eef8100459c5806698ac488e
Review: work/astra_review_registry/reviews/w3-b2-residue-one-digit-refinement-v1-worker_1.md

UNREVIEWED CANDIDATE. Author: worker_3. This is a separate consequence of the published arithmetic and analytic premises specified below. It does not revise or depend on worker1-b2-five-adic-residue-one-form-growth-v1.

STATEMENT

Let S={n≥6:n≡1 (mod 5)}. Define the arithmetic endpoint pair X_n,D_n below, and write −X_n/D_n=p_n/q_n in lowest terms, with q_n>0. Put eta_n=1 for n≡1 (mod 3), and eta_n=0 otherwise. Then, using the published arithmetic premises below, D_n≠0 and

q_n≥3^{eta_n}(3√5)^n/[9√5·n²(n−1)²]

for EVERY n in S.

Put rho=1+√2, beta=3√5/rho², and L_n=q_n(e+pi)−p_n. Using additionally the published endpoint identification and fixed-b error theorem below, there exists an unspecified integer N such that, for every n in S with n≥N,

|L_n|≥[2pi·3^{eta_n}/(9√5·rho³)]·beta^n/[n²(n−1)²].

Here beta>1. Consequently |L_n| tends to infinity along S, and liminf_{n→∞, n∈S} log|L_n|/n≥log beta>0. Every nonzero integer multiple of the reduced form has at least this magnitude. The arithmetic range n≥6 is explicit; no numerical value or effective construction of the analytic threshold N is claimed.

EXACT ENDPOINT DEFINITIONS

Let i²=−1 and define the rational linear functional
ℒ(t^j)=((1+i)^(j+1)−(1−i)^(j+1))/(i·2^j(j+1)).
Let
L_m(t)=(1/m!)(d/dt)^m(2t²−2t+1)^m,
P=L_n, U=L_{n+1}, a=P(1), b=U(1), k=(n+1)², f=2^n/(n!)².
For E_j=Σ_{h=0}^j1/h!, set
T_0(Q)=Σ_d[t^d]Q(t)E_{n+d},
w_P=ℒ((P(t)−a)/(t−1)), w_U=ℒ((U(t)−b)/(t−1)),
P*=w_P+T_0(P), U*=w_U+T_0(U).
The index in T_0 is n for both P and U.

Define
H_m(x)=m![s^m]exp(xs)(1−s+s²/2)^m,
h_m=H_m(1), J_m=mh_m+H'_m(1),
K_m=m(m−1)h_m+2mH'_m(1)+H''_m(1).
Put
eta= h_{n+1},
S_n=J_{n+1}²−eta K_{n+1},
C_s=(J_{n+1}−eta)J_n−(K_{n+1}−J_{n+1})h_n,
W_n=J_{n+1}J_n−K_{n+1}h_n,
D_n=kbC_s−2aS_n,
X_n=2P*S_n−kU*C_s−2f eta W_n.
The scalar eta is unrelated to the indicator eta_n; C_s is not a matched-family polynomial.

PUBLISHED PREMISES

The following claims are published in work/astra_review_registry/verified/. Their recorded independent reviews concern their exact scopes; this new synthesis still requires its own independent review.

1. worker4-b2-five-adic-residue-one-exact-denominator-v1.md, payload cbf4838dfb7531fb17145053d4180baeed90ce8d9214d4f57197b1022eb790d3: for every n∈S, D_n is a five-adic unit and v_5(q_n)=2v_5(n!). This supplies all-index nonvanishing on S.

2. b2-ternary-endpoint-denominator-and-content-v1.md, payload 6baaa17575ed30467e01de61e4c861e97987c07a31f331cc6821f2b850f05dfe: v_3(q_n)=2v_3(n!) for n≥3 divisible by three.

3. worker2-b2-ternary-residue-two-exact-denominator-v1.md, payload ba51fc9529c4fe1ea78ad46225229d224dc4c5ac36b4b80e067017230642ce38: v_3(q_n)=2v_3(n!) for n≥5 congruent to two modulo three.

4. worker4-b2-ternary-residue-one-conditional-denominator-v1.md, payload 5268f1e9d2b38f15e4b00b9918dd6c98f6f57dcac0b6a75fc046e5bbb7738082: v_3(q_n)≥2v_3(n!)+1 for n≥4 congruent to one modulo three, provided D_n≠0. Premise 1 supplies that condition throughout S. All minimum-index restrictions in premises 2–4 hold on S.

5. b2-two-chart-actual-denominator-identities.md, payload ace0c8602da8ebb959a140d0a8e4dd9caf532014dc653f5328e909389ca4280d, and w3-b2-eventual-d-nonzero-v1.md, payload 66273b26045bf283eff8b3b503e2c51141e05c2c3f0bf128a8412e1fdec6817f: the exact raw reconstruction has
A_raw(1)=gamma_n X_n,
B_raw(1)=C_raw(1)=gamma_n D_n,
gamma_n=(−1)^n/[4(n+1)^3(n!)^4]≠0,
with remainder A_raw+B_raw exp(z)+C_raw F(z), where F(z)=4 arctan(z/(2−z)). Its degree caps are deg A_raw,deg C_raw≤n and deg B_raw≤2, and its remainder is O(z^(2n+3)). The identification has no index shift. Setting A=−A_raw gives the convention R=B exp(z)+CF−A and A(1)/Y=−X_n/D_n. Only these rational identities are used, not any large-prime ideal assertion at three or five.

6. worker2-fixed-b-projection-and-error-transfer-v2.md, payload b8c2e619d3f2287876530b229be959d872aadf8b04c5df3b3cef4ee8ec7c8245: at fixed b=2 the matched solution space is eventually one-dimensional, Y=B(1)=C(1) is eventually nonzero, and
R(1)/Y=(−1)^n(4pi/rho³)rho^(−2n)(1+o(1)).
The published ordinary Padé prefactor is an input to that theorem. No assertion uniform in growing b is used. Premise 5 and eventual uniqueness identify the raw reconstruction with this solution, up to a nonzero rational scalar.

DERIVATION

Since q_n is a positive integer, premises 1–4 imply, for every n∈S,
q_n≥3^{2v_3(n!)+eta_n}5^{2v_5(n!)}.
Writing s_p(n) for the base-p digit sum, Legendre's formula gives
2v_3(n!)=n−s_3(n),
2v_5(n!)=(n−s_5(n))/2.
Therefore
q_n≥3^{eta_n}(3√5)^n/[3^{s_3(n)}5^{s_5(n)/2}].

For any integer x≥1, its base-p expansion has floor(log_p x)+1 digits, each at most p−1. Thus
s_p(x)≤(p−1)(floor(log_p x)+1).
In particular,
3^{s_3(n)}≤9n².

Now write n=5m+1, where m≥1. Multiplication by five appends a zero base-five digit, and addition of one causes no carry. Hence the EXACT identity is
s_5(n)=s_5(m)+1.
The same elementary digit bound, applied to m, gives
5^{s_5(n)/2}=√5·5^{s_5(m)/2}≤25√5·m²=√5(n−1)².
Consequently
3^{s_3(n)}5^{s_5(n)/2}≤9√5·n²(n−1)².
Substitution proves the asserted all-index denominator bound.

For sufficiently large n, the endpoint conventions in premises 5–6 give exactly
R(1)/Y=e+pi−p_n/q_n,
L_n=q_nR(1)/Y.
The asymptotic in premise 6 implies, beyond some unspecified threshold,
|R(1)/Y|≥(2pi/rho³)rho^(−2n).
Multiplying this inequality by the all-index denominator bound proves the asserted lower bound for |L_n|. The threshold includes any eventual uniqueness requirement; it is not replaced by the arithmetic threshold six.

Finally, rho²=3+2√2 and
(rho²)²=17+12√2<41<45=(3√5)².
All quantities are positive, so beta>1. The exponential beta^n dominates n²(n−1)², proving divergence and the logarithmic lower bound.

If integers P,Q satisfy Q≠0 and P/Q=p_n/q_n, coprimality of p_n,q_n implies (P,Q)=k(p_n,q_n) for a nonzero integer k. Thus |Q(e+pi)−P|=|k||L_n|≥|L_n|. No assumption that integer polynomial normalization makes its endpoint coefficients coprime is necessary.

EVIDENCE AND SCOPE

The new digit argument was preserved in work/astra_20260929/worker_3/note_000114.md, read completely through byte 1664, whole-file SHA-256 bfb2f00488fd987f6eda5dd970cef4cf12140faf41cafb09f7a842fd8b690907. The preceding form-growth audit is preserved separately in worker_3/note_000112.md. This candidate does not use that unapproved synthesis as a premise. The displayed universal inequalities are proved above; no finite numerical check is substituted for proof.

The refinement concerns a polynomial factor and numerical constant in a lower bound. It provides no new local valuation theorem, upper bound on reduced denominators, effective analytic threshold, control of other progressions, or conclusion about the rationality of e+pi. The new claim remains unverified until independently reviewed and published through the registry.