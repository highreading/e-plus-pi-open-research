> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact two-chart ideals and reduced-denominator valuations for the b=2 endpoint pair

Status: UNVERIFIED CANDIDATE
Author: worker_1
Content SHA256: ace0c8602da8ebb959a140d0a8e4dd9caf532014dc653f5328e909389ca4280d

Status: unverified candidate submitted by worker_1 for independent review. This claim concerns exact algebra and local valuations only.

STATEMENT AND DEFINITIONS

Fix an integer n≥2. Let P_k denote the ordinary Legendre polynomial and define L_k(t)=2^k i^k P_k(−i(2t−1))∈Z[t]. Write P=L_n, U=L_{n+1}, a=P(1), b=U(1), and k=(n+1)². Define the rational moment functional ℒ(Q)=∫_{−1}^1 Q((1+iu)/2)du and the rational numbers
w_P=ℒ((P(t)−a)/(t−1)),  w_U=ℒ((U(t)−b)/(t−1)).
Put E_m=Σ_{v=0}^m1/v! and T_j(Q)=Σ_d[t^d]Q(t)E_{n+d−j}, for j=0,1,2. All indices here are nonnegative. Set T_P=T_0(P), T_U=T_0(U), P*=w_P+T_P, and U*=w_U+T_U.

Define H_m(x)=m![s^m]e^{xs}(1−s+s²/2)^m and the scalar transforms
h_m=H_m(1),
J_m=mH_m(1)+H′_m(1),
K_m=m(m−1)H_m(1)+2mH′_m(1)+H″_m(1).
These scalars are integers. Set η=h_{n+1}, f=2^n/(n!)², g=2^{n+1}/((n+1)!)²=2f/k, and
S=J_{n+1}²−h_{n+1}K_{n+1},
C=(J_{n+1}−h_{n+1})J_n−(K_{n+1}−J_{n+1})h_n,
W=J_{n+1}J_n−K_{n+1}h_n.
The endpoint pair under consideration is
D=kbC−2aS∈Z,
X=2P*S−kU*C−2fηW∈Q.
Define G=(−1)^n2^{2n+3}/(n+1) and V=bP*−aU*.

For every prime p>2n+2, all the displayed scalar data are p-integral. The numbers 2,n+1,k,f,g,G and α=gf/(Gk) are p-adic units. At least one of a,b is a p-adic unit. Moreover,
V=bT_P−aT_U−G.
If b is a unit, then the following ideals in Z_p are equal:
(D,X)=(D,VS−bfηW).
If a is a unit, then
(D,X)=(D,kVC−2afηW).
Both identities are valid at every prime-power depth, including when one generator is zero.

Assume additionally D≠0, and let q be the positive reduced denominator of X/D. With v_p(0)=+∞, the b-unit chart gives
v_p(q)=v_p(D)−min(v_p(D),v_p(VS−bfηW)).
The a-unit chart gives
v_p(q)=v_p(D)−min(v_p(D),v_p(kVC−2afηW)).
When both charts are available their results agree. These are exact formulas, with no bound on any displayed valuation asserted.

IDENTIFICATION WITH THE ACTUAL ENDPOINT RATIO

For clarity, the endpoint reconstruction used here can be specified entirely in scalar notation. Define ℓ_j(t^d)=1/(n+d+1−j)!, a_j=ℓ_j(U), and r_j=ℓ_j(P). Let
 t_j=(aT_j(U)−bT_j(P))/G,
 x_j=(w_PT_j(U)−w_UT_j(P))/G.
Let β=(a_0,a_1,a_2)×(1+t_0,1+t_1,1+t_2), Y_raw=Σ_jβ_j, and X_raw=Σ_jβ_jx_j. The original endpoint reconstruction identifies these as B(1)=C(1)=Y_raw and A(1)=X_raw for the raw b=2 triple with degree caps (n,2,n), R=A+Be^z+CF=O(z^{2n+3}), and F(z)=4 arctan(z/(2−z)). This identification is a stated source dependency, independently audited by the author; the present claim does not assert eventual normality.

Here are the exact scaling details. Rodrigues’ formula gives
Σ_d[t^d]L_m(t)x^{m+d}/(m+d)!=2^m x^mH_m(x)/(m!)².
Consequently (r_1,r_2)=f(h_n,J_n) and (a_0,a_1,a_2)=g(η,J_{n+1},K_{n+1}). Define
𝒮=a_1²−a_0a_2=g²S,
𝒞=(a_1−a_0)r_2−(a_2−a_1)r_1=gfC,
𝒲=a_1r_2−a_2r_1=gfW.
Using T_0(Q)−T_1(Q)=ℓ_1(Q) and T_1(Q)−T_2(Q)=ℓ_2(Q), determinant expansion yields
Y_raw=(b𝒞−a𝒮)/G,
X_raw=(P*𝒮−U*𝒞−a_0𝒲)/G.
Since g=2f/k and a_0=gη, both scale by the SAME nonzero factor:
Y_raw=αD,  X_raw=αX,  α=gf/(Gk).
Thus D≠0 is equivalent to Y_raw≠0, and q is exactly the reduced denominator of A(1)/B(1) for this reconstructed triple. It includes every cancellation in that rational ratio; no assumption about primitive polynomial normalization is necessary. The term −2fηW is part of the actual numerator and must be retained.

PROOF OF LOCAL ASSERTIONS

The Legendre leading coefficient is c_m=2^m binom(2m,m), and ℒ(L_n²)=(−1)^n2^{2n+1}/(2n+1). Hence the Christoffel–Darboux normalizing constant is
(c_{n+1}/c_n)ℒ(L_n²)=G.
The corresponding kernel identity is K_n(1,t)=(bP(t)−aU(t))/(G(1−t)). Integrating and using reproduction of the constant polynomial gives the exact Wronskian
aw_U−bw_P=G.
This proves the formula for V.

For completeness, a monomial moment is
ℒ(t^d)=((1+i)^{d+1}−(1−i)^{d+1})/(i2^d(d+1)).
Its numerator divided by i is an integer. The polynomial quotients defining w_P,w_U have integer coefficients and degree at most n. Thus their moment denominators have no prime factor exceeding n+1, apart from 2. The largest factorial in T_P,T_U is (2n+1)!. Therefore w_P,w_U,T_P,T_U are p-integral for p>2n+2, as are X,D,V and all their displayed factors. The factorials in f,g and all numerator/denominator factors in G,k,α are p-units. The integer-coefficient assertion for H_m also follows directly from its coefficient expansion: each term is binom(m,b+c)binom(b+c,c)(m)_{b+2c}x^{m−b−2c}/2^c with sign (−1)^b, and the consecutive product (m)_{b+2c} contains at least c even factors whenever the term is nonzero.

If both a and b were nonunits, p-integrality of w_P,w_U would force G=aw_U−bw_P to be a nonunit. This contradicts the explicit unit formula for G and proves chart coverage.

Direct expansion, with no division, gives
bX+U*D=2(VS−bfηW),
aX+P*D=kVC−2afηW.
On the b-unit chart, replacing X by bX+U*D preserves the generated ideal, and removing the factor 2 also preserves it because p is odd. On the a-unit chart, replacing X by aX+P*D preserves the ideal. These prove both ideal identities.

For any p-integral rational pair X,D with D≠0, reduction of X/D gives
v_p(q)=max(0,v_p(D)−v_p(X))=v_p(D)−min(v_p(D),v_p(X)).
The valuation of a two-generator ideal equals the minimum of its generator valuations. Substitution of either equal ideal proves the claimed formulas, also for X=0 or a zero chart generator.

One may alternatively use Λ=2^{n+1}(2n+2)!(n!)². The denominator observations above imply ΛX∈Z; ΛD∈Z and Λ is a p-unit throughout the stated range. Hence q=|ΛD|/gcd(|ΛD|,|ΛX|), giving the same valuations. No minimality of Λ is needed.

DEPENDENCIES, EVIDENCE, AND LIMITS

Original sources: work/session_20260913/hp_b2_contiguous_endpoint_arithmetic.md (SHA-256 5be62d46800cccae5cea266853b33e2cbac6880dba158565518cbfdd3682d84a), especially equations (1)–(13); work/session_20260913/hp_b2_endpoint_attempt.md (SHA-256 ba2b0e2c74e72892488ae9fea6a1f3b7483afa5e9f4cb622ddbe317af907cd05), exact projection and endpoint definitions only. The two-chart reformulation originates in work/astra_20260929/main/note_000059.md (SHA-256 296ae9a544011b2841f484018f10769d74f2ab41ce5d8502bd5cebe9059480cf).

Author audit evidence: work/astra_20260929/worker_1/note_000004.md records the reconstruction audit; work/astra_20260929/worker_1/note_000007.md (SHA-256 27026569223138f1bd79140282b449443d654f0190694c22ff2b2fd2723c1fa9) records the fresh successful symbolic verification of reconstructed X,Y, both common-factor scaling identities, and both chart identities. These computations support the exact algebra only and are not independent registry approval. The earlier failed SymPy import supplies no computational evidence.

Self-audit: the proof requires p>2n+2; no claim is made at p=2 or p=3. Ratios and denominator formulas require D≠0. No unconditional nonvanishing theorem, asymptotic prefactor, estimate for V or either contraction, upper bound on q, or irrationality result is part of this claim. Independent review remains required.