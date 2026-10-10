> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact ternary reduced-denominator valuation for the b=2 endpoint pair on n congruent to two modulo three

Status: Independently reviewed research result (AI review; not formal verification)
Author: worker_2
Reviewer: worker_1
Content SHA256: ba51fc9529c4fe1ea78ad46225229d224dc4c5ac36b4b80e067017230642ce38
Review: work/astra_review_registry/reviews/worker2-b2-ternary-residue-two-exact-denominator-v1-worker_1.md

STATUS: Unverified author derivation submitted for independent review. This claim concerns the specified rational endpoint pair and its exact ternary valuation. It does not prove irrationality of e+pi.

STATEMENT AND DEFINITIONS

Fix n≥5 with n≡2 modulo 3. Put m=n+1, t=v_3(m), r=v_3(n!), and f=2^n/(n!)². Let P_j denote the ordinary Legendre polynomial and define L_j(z)=2^j i^j P_j(−i(2z−1))∈Z[z]. Set a=L_n(1), b=L_m(1).

Define the moment functional ℒ(Q)=∫_{−1}^1 Q((1+iu)/2)du, and set
w_P=ℒ((L_n(z)−a)/(z−1)),
w_U=ℒ((L_m(z)−b)/(z−1)).
Write E_j=Σ_{v=0}^j1/v!, and, for a polynomial Q, T_0(Q)=Σ_d[z^d]Q(z)E_{n+d}. Put P*=w_P+T_0(L_n) and U*=w_U+T_0(L_m).

Let H_j(x)=j![s^j]e^(xs)(1−s+s²/2)^j, and define
h_j=H_j(1),
J_j=jH_j(1)+H′_j(1),
K_j=j(j−1)H_j(1)+2jH′_j(1)+H″_j(1).
Set η=h_m and
S=J_m²−h_mK_m,
C=(J_m−h_m)J_n−(K_m−J_m)h_n,
W=J_mJ_n−K_mh_n.
The complete endpoint pair is
D=m²bC−2aS,
X=2P*S−m²U*C−2fηW.
In particular, the last term of X is retained. Write N=X/f.

Then D and X are nonzero, and
v_3(D)=v_3(N)=t.
More precisely, D/m≡2a and N/m≡2 modulo 3. If q is the positive reduced denominator of X/D, then
v_3(q)=2r.
The same denominator belongs to −X/D. Identification with the reconstructed b=2 endpoint ratio is the published source dependency specified below.

PROOF

1. Auxiliary estimates near indices divisible by three.

For j≥0, direct expansion of the definition gives
H_m^(j)(1)=Σ_{B,C≥0; B+2C+j≤m} (−1)^B (m)_(B+2C+j)(m)_(B+C)/(2^C B!C!),
where (m)_k=m(m−1)…(m−k+1). The term B=C=0 is (m)_j.

Consider a nonleading term, and put l=B+C≥1 and k=B+2C=l+C. The identity
(m)_l/(B!C!)=binom(m,l)binom(l,B)
shows that its valuation is at least
2t+floor((k+j−1)/3)−v_3(l).
Indeed, binom(m,l)=(m/l)binom(m−1,l−1) has valuation at least t−v_3(l). The other falling factorial contains m, together with floor((k+j−1)/3) further factors divisible by 3. Powers of two are units. The imposed range ensures these falling factorials are nonzero; omitted terms vanish exactly.

For j=1,2, floor((k+j−1)/3)≥floor(l/3)≥v_3(l). For j=0, floor((k−1)/3)≥floor((l−1)/3)≥v_3(l)−1. These elementary inequalities hold for every positive integer l: if v_3(l)=v≥1, use l≥3^v; the case v=0 is immediate.

Summing the finite expansions proves
h_m−1∈3^(2t−1)Z_3,
H′_m(1)−m∈3^(2t)Z_3,
H″_m(1)−m(m−1)∈3^(2t)Z_3.
Since t≥1, substitution into the definitions yields
J_m≡2m mod3^(2t),
K_m≡2m(m−1) mod3^(2t).
Consequently h_m≡1, J_m/m≡2, and K_m/m≡1 modulo 3.

2. Auxiliary residues at n≡2 modulo three.

The coefficient of x^j in H_n(x) is
(n!/j!)[s^(n−j)](1−s+s²/2)^n.
The bracketed coefficient belongs to Z_3. For j≤n−3 the factorial ratio contains n−2, which is divisible by 3. The remaining three coefficients therefore give
H_n(x)≡x^n−x^(n−1)+x^(n−2) mod3.
Here the unreduced top coefficients are 1, −n², and n³(n−1)/2. Evaluation and differentiation imply h_n≡1 and J_n≡0 modulo 3.

It follows that C∈3Z_3. Moreover, J_m² has valuation 2t while h_mK_m has valuation t, so
v_3(S)=t, S/m≡2 mod3.
Likewise J_mJ_n has valuation at least t+1, whereas K_mh_n has valuation t, giving
v_3(W)=t, W/m≡2 mod3.

3. Legendre endpoint units.

The endpoint generating function is
A(z)=Σ_{j≥0}L_j(1)z^j=(1−4z−4z²)^(−1/2).
Reduce its integral coefficients modulo 3 and put Q(z)=1+2z+2z². Since A²Q=1 and A(z)^3=A(z³), one has
A(z)=Q(z)A(z³) in F_3[[z]].
Thus L_(3k)(1)≡L_k(1), while L_(3k+1)(1)≡L_(3k+2)(1)≡2L_k(1). Starting with L_0(1)=1, induction proves that every endpoint L_j(1) is a ternary unit. In particular, a and b are units.

The first summand of D=m²bC−2aS has valuation at least 2t+1, whereas the second has valuation t. Hence D≠0, v_3(D)=t, and D/m≡−2a·2≡2a modulo 3.

4. The normalized exponential contractions.

Write e_j=j!E_j∈Z and u_(h,j)=[z^j](2z²−2z+1)^h. Rodrigues’ identity gives the exact finite sums
T_0(L_n)/f=2^(−n)Σ_(d=0)^n (n!/d!)u_(n,n+d)e_(n+d),
T_0(L_m)/f=[2^n m]^(−1)Σ_(d=0)^m (n!/d!)(m+d)u_(m,m+d)e_(n+d).
For completeness, these follow by writing
L_h(z)=(1/h!)(d/dz)^h(2z²−2z+1)^h,
so [z^d]L_h=(h+d)!u_(h,h+d)/(h!d!), and then using E_j=e_j/j!.

The recurrence e_j=je_(j−1)+1 gives e_j≡1 when j≡0 modulo 3 and e_j≡2 otherwise. In the first sum, terms d≤n−3 vanish modulo 3. The leading coefficients
u_(n,2n)=2^n,
u_(n,2n−1)=−n2^n,
u_(n,2n−2)=n²2^(n−1)
give
T_0(L_n)/f≡e_(2n)−n²e_(2n−1)+[n³(n−1)/2]e_(2n−2)≡2−1+2≡0 mod3.
In these three displayed coefficient identities, the symbol u_(n,j) is intended; the identities are coefficients of the polynomial defined above.

Multiplying the second sum by m² shows that every term with d≤n belongs to mZ_3, because n!/d! is integral and the outside factor is m/2^n. The remaining d=m term is exactly 4m e_(2n+1). Therefore
m²T_0(L_m)/f∈mZ_3.

5. The normalized moment contractions.

The quotient polynomials in w_P and w_U have integral coefficients and degrees at most n−1 and n, respectively. A monomial moment is
ℒ(z^d)=((1+i)^(d+1)−(1−i)^(d+1))/(i2^d(d+1)).
Its numerator after division by i is integral. Thus, with L=floor(log_3(n+1)), both moment valuations are at least −L.

For n≥5, r=v_3(n!)≥L≥1. To check this, L=1 is immediate; if L≥2, n≥3^L−1 implies r≥floor(n/3)≥3^(L−1)−1≥L. Since v_3(f)=−2r, it follows that
v_3(w_P/f)≥2r−L≥1,
v_3(m²w_U/f)≥2t+2r−L≥2t+1.
Combining these estimates with the exact exponential contractions proves
P*/f∈3Z_3,
m²U*/f∈mZ_3.

6. The complete numerator and reduction.

In
N=2(P*/f)S−(m²U*/f)C−2h_mW,
the first two summands have valuation at least t+1. The last summand has valuation exactly t, and after division by m is congruent to −2·1·2≡2 modulo 3. Therefore N≠0, v_3(N)=t, and N/m≡2 modulo 3.

Finally, X=fN has valuation t−2r. Exact rational reduction, with no local-integrality hypothesis on X, gives
v_3(q)=max(0,v_3(D)−v_3(X))=2r.
This completes the proof for the displayed rational pair.

DEPENDENCIES AND EVIDENCE

Identification of X/D with the raw b=2 endpoint ratio uses work/astra_review_registry/verified/b2-two-chart-actual-denominator-identities.md, published payload SHA-256 ace0c8602da8ebb959a140d0a8e4dd9caf532014dc653f5328e909389ca4280d. Its common scaling is Y_raw=αD and X_raw=αX with α≠0. Only its exact rational reconstruction is imported; its p>2n+2 local ideal theorem is not applied at p=3.

Related original definitions and the divisible-by-three comparison are in work/astra_review_registry/verified/b2-ternary-endpoint-denominator-and-content-v1.md, published payload SHA-256 6baaa17575ed30467e01de61e4c861e97987c07a31f331cc6821f2b850f05dfe. Both published records were read completely in this worker’s ledger before this derivation.

Earlier author evidence: work/astra_20260929/worker_2/note_000073.md records the complementary residue calculations; note_000076.md records six completed exact endpoint reconstructions. The three relevant samples n=5,8,11 gave (v_3(D),v_3(N),v_3(q))=(1,1,2),(2,2,4),(1,1,8). Those calculations motivated this proof but are not used to establish its universal statement and were not repeated for this submission.

SELF-AUDIT AND SCOPE

All estimates concern finite sums and exact rational quantities. The moment bound is used only for n≥5. The valuation comparison explicitly retains all three complete numerator terms. Nonvanishing of D on this progression follows from unequal valuations and is not assumed. The proof needs independent review, especially the auxiliary falling-factorial bound and Rodrigues normalization. It establishes no conclusion for n=2, no denominator upper bound, no control at other primes, and no irrationality result.