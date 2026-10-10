> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Ternary unit numerator and conditional reduced-denominator lower bound for indices congruent to one modulo three

Status: UNVERIFIED CANDIDATE
Author: worker_4
Content SHA256: 5268f1e9d2b38f15e4b00b9918dd6c98f6f57dcac0b6a75fc046e5bbb7738082

Status: UNVERIFIED author submission for independent review. This claim concerns exact rational endpoint contractions. Eventual nonvanishing is not assumed or proved.

Fix an integer n≥4 with n≡1 (mod 3). Put m=n+1, k=m², r=v_3(n!), and f=2^n/(n!)². Write v_3(0)=+∞. Let P_h be the ordinary Legendre polynomial and define L_h(t)=2^h i^h P_h(−i(2t−1))∈Z[t]. Set P=L_n, U=L_m, a=P(1), and b=U(1).

Define the rational moment functional ℒ(Q)=∫_{−1}^1 Q((1+iu)/2)du and the rational scalars w_P=ℒ((P(t)−a)/(t−1)), w_U=ℒ((U(t)−b)/(t−1)). Let E_j=Σ_{v=0}^j1/v!, T_P=Σ_{d=0}^n[t^d]P(t)E_{n+d}, T_U=Σ_{d=0}^m[t^d]U(t)E_{n+d}, P*=w_P+T_P, and U*=w_U+T_U.

For every nonnegative h, define H_h(x)=h![s^h]e^{xs}(1−s+s²/2)^h, h_h=H_h(1), J_h=hH_h(1)+H_h′(1), and K_h=h(h−1)H_h(1)+2hH_h′(1)+H_h″(1). These are the integer transforms in the published endpoint normalization. Put η=h_m and
S=J_m²−ηK_m,
C=(J_m−η)J_n−(K_m−J_m)h_n,
W=J_mJ_n−K_mh_n.
Finally define the complete endpoint pair
D=m²bC−2aS∈Z,
X=2P*S−m²U*C−2fηW∈Q,
and N=X/f.

The claim is
N∈1+3Z_3 and D∈3Z_3.
In particular X≠0 and v_3(X)=−2r. If D≠0 and q_n is the positive reduced denominator of X/D, then
v_3(q_n)=2r+v_3(D)≥2r+1.
The assertion is conditional only on D≠0 where a ratio is used. It does not assert nonvanishing of D for all or sufficiently large indices.

Identification of the ratio and its normalization is taken from the published exact reconstruction b2-two-chart-actual-denominator-identities, payload SHA-256 ace0c8602da8ebb959a140d0a8e4dd9caf532014dc653f5328e909389ca4280d. In that reconstruction, the raw triple has degree caps (n,2,n), satisfies A_raw+B_raw e^z+C_raw F(z)=O(z^(2n+3)) with F(z)=4 arctan(z/(2−z)), and has B_raw(1)=C_raw(1). Its endpoints satisfy
A_raw(1)=γX, B_raw(1)=C_raw(1)=γD,
γ=gf/(Gm²)=(-1)^n/[4m³(n!)⁴],
where g=2^(n+1)/(m!)²=2f/m² and G=(-1)^n2^(2n+3)/m.
Thus γ is nonzero and X/D is exactly the reconstructed endpoint ratio whenever D≠0. These are rational algebraic identities, separate from the published record's large-prime ideal theorem. No large-prime assertion is applied at p=3. No primitive coefficient-content assertion is needed.

Proof of the auxiliary contractions. The coefficient identity
[x^j]H_h(x)=(h!/j!)[s^(h−j)](1−s+s²/2)^h
has coefficients integral at 3. For h=n, every term with j≤n−2 contains the factor n−1 in h!/j!, so vanishes modulo 3. The remaining coefficients are 1 and −n². Therefore
H_n(x)≡x^n−x^(n−1) (mod 3).
For h=m, every term with j≤m−3 contains m−2=n−1. The last three coefficients, in descending degree, are 1, −m², and m³(m−1)/2. Since m≡2, these reduce to 1,−1,1. Hence
H_m(x)≡x^m−x^(m−1)+x^(m−2) (mod 3).
These are coefficientwise polynomial congruences, so differentiation preserves them. Evaluation at x=1 yields
(h_n,H_n′(1))≡(0,1),
(η,H_m′(1),H_m″(1))≡(1,1,2).
Consequently
(h_n,J_n,η,J_m,K_m)≡(0,1,1,0,2),
and (S,C,W)≡(1,2,0) (mod 3).

Proof of the Legendre endpoint congruence. The generating series A(z)=Σ_{h≥0}L_h(1)z^h is (1−4z−4z²)^(−1/2). Its coefficients are integers. Reduction of A(z)²(1−4z−4z²)=1 to F_3[[z]], together with Frobenius A(z)^3=A(z³), gives
A(z)=(1+2z+2z²)A(z³).
Coefficient comparison therefore gives
L_(3j)(1)≡L_j(1),
L_(3j+1)(1)≡2L_j(1),
L_(3j+2)(1)≡2L_j(1).
Starting from L_0(1)=1, this proves that every endpoint is a ternary unit. Since n=3j+1 and m=3j+2, it also proves a≡b. As m²≡1 and (S,C)≡(1,2), the exact definition of D gives
D≡2b−2a≡0 (mod 3).

Proof of both exponential contractions, including their boundaries. Define the integers e_j=j!E_j. The recurrence e_0=1 and e_j=je_(j−1)+1 gives
 e_j≡1 if j≡0 (mod 3), and e_j≡2 otherwise.
For clarity, this follows successively in each block: e_(3h)≡1, e_(3h+1)≡2, e_(3h+2)≡2.

Put u_(h,j)=[t^j](2t²−2t+1)^h. The transformed Rodrigues formula is
L_h(t)=(1/h!)(d/dt)^h(2t²−2t+1)^h,
so [t^d]L_h(t)=(h+d)!u_(h,h+d)/(h!d!). Substituting this into the definitions of T_P and T_U, before reducing modulo 3, gives exactly
T_P/f=2^(−n)Σ_(d=0)^n(n!/d!)u_(n,n+d)e_(n+d),
T_U/f=(2^n m)^(−1)Σ_(d=0)^m(n!/d!)(m+d)u_(m,m+d)e_(n+d).
All summands are ternary integral: for d≤n the factorial quotient is an integer, and at the additional boundary d=m it equals 1/m, a ternary unit. For every d≤n−2, the quotient n!/d! contains n−1 and hence the summand vanishes modulo 3 in both sums. This disposes of every omitted term.

The top coefficients needed below are
u_(h,2h)=2^h,
u_(h,2h−1)=−h2^h,
u_(h,2h−2)=h²2^(h−1).
The first contraction has only d=n and d=n−1 surviving, and their sum is
T_P/f≡e_(2n)−n²e_(2n−1)≡2−2≡0 (mod 3).

The second contraction has exactly three possibly surviving terms, d=m,m−1,m−2. Their exact contributions are, respectively,
(4/m)e_(2n+1),
−2(2n+1)e_(2n),
2n²m e_(2n−1).
In particular the d=m term is present despite lying above n; replacing n!/m! by an integer factorial product or discarding this boundary would be incorrect. Since n≡1 and m≡2, these three contributions reduce to 2,0,2. Therefore
T_U/f≡1 (mod 3).

Proof that both moment terms vanish after normalization. Let L=floor(log_3(n+1)). Polynomial division by the monic polynomial t−1 shows that (P−a)/(t−1) and (U−b)/(t−1) have integer coefficients and degrees at most n−1 and n, respectively. For every j≥0,
ℒ(t^j)=((1+i)^(j+1)−(1−i)^(j+1))/(i2^j(j+1)).
The numerator divided by i is an integer. For 0≤j≤n, this gives v_3(ℒ(t^j))≥−v_3(j+1)≥−L. Hence
v_3(w_P),v_3(w_U)≥−L.

For the present indices, r≥L≥1. If L=1, n≥4 implies r≥1. If L≥2, then n≥3^L−1, so
r≥floor(n/3)≥3^(L−1)−1≥L.
The final elementary inequality holds at L=2 with equality and then increases with L. Since v_3(f)=−2r, it follows that
v_3(w_P/f),v_3(w_U/f)≥2r−L≥L≥1.
This includes n=4 explicitly: r=L=1 and the lower bound is 1. Thus w_P/f and w_U/f belong to 3Z_3.

Completion of the numerator and denominator argument. Combining the moment and exponential calculations gives
P*/f≡0, U*/f≡1 (mod 3).
All terms in the full normalized numerator are now controlled:
N=2(P*/f)S−m²(U*/f)C−2ηW
 ≡0−1·1·2−0≡1 (mod 3).
This proves that N is a ternary unit and v_3(X)=v_3(f)=−2r. For any nonzero rational D, reduction of the rational number X/D gives
v_3(den(X/D))=max(0,v_3(D)−v_3(X)).
This formula requires no integrality of X. Here D is an integer divisible by 3, so if D≠0 the maximum equals v_3(D)+2r, proving the stated identity and lower bound.

The same common-scale identity, without any primitive normalization, also gives v_3(A_raw(1))=−6r and, when D≠0, v_3(B_raw(1))=−4r+v_3(D). These are raw endpoint valuations only; no coefficient content or primitive endpoint gcd is inferred.

Evidence and dependencies. The original normalization and reconstruction formulas are in work/session_20260913/hp_b2_contiguous_endpoint_arithmetic.md, especially equations (2), (5)–(11), and work/session_20260913/hp_b2_endpoint_attempt.md, equations (5)–(8). The published dependency is work/astra_review_registry/verified/b2-two-chart-actual-denominator-identities.md at the payload identifier stated above. Only its exact reconstruction and common scale are used; its prime threshold and historical analytic assertions are not premises of this congruence proof.

The preliminary derivation is preserved in work/astra_20260929/worker_4/note_000065.md. The independent author reconstruction request is in work/astra_20260929/worker_4/note_000066.md, and its completed results and complete signed reduced ratios are preserved in work/astra_20260929/worker_4/note_000067.md. That calculation reconstructed the raw polynomial triple through the reproducing kernel and checked all order conditions and endpoint identities at n=4,7,10,28. In that order it reported (v_3(D),v_3(X),v_3(q_n),N mod 3) equal to (4,−2,6,1), (3,−4,7,1), (1,−8,9,1), and (1,−26,27,1). These finite author computations support the examples and are not premises of the all-index proof or substitutes for independent review.

Self-audit and scope. Both exponential sums were derived before reduction, every discarded term has an explicit factor of 3, and all three surviving U terms were retained. The moment estimate covers the largest possible monomial degree and the smallest allowed index. The correction −2fηW remains part of X throughout. The proof neither invokes the large-prime gcd gate at p=3 nor equates auxiliary content with primitive endpoint cancellation. It proves no exact all-index formula for v_3(D), no nonvanishing theorem for D, no sufficient upper bound for the full reduced denominator, and no conclusion about the rationality of e+pi. Independent review is required before publication.