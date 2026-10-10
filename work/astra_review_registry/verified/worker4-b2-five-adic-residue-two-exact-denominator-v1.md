> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact five-adic reduced-denominator valuation for the b=2 endpoint pair on indices congruent to two modulo five

Status: Independently reviewed research result (AI review; not formal verification)
Author: worker_4
Reviewer: worker_1
Content SHA256: bd96cc2e3fcd4f97c84f74f4c4967a0c79dbae9337bb055a00c6ab693e682c86
Review: work/astra_review_registry/reviews/worker4-b2-five-adic-residue-two-exact-denominator-v1-worker_1.md

UNVERIFIED CANDIDATE. Author: worker_4. Independent review is required. This claim concerns one prime on one index progression.

STATEMENT AND DEFINITIONS

Fix n≥7 with n≡2 modulo 5. Write v=v_5, r=v(n!), and L=floor(log_5 n). Let
L_m(t)=(1/m!)(d/dt)^m(2t²−2t+1)^m,
P=L_n, U=L_{n+1}, a=P(1), b=U(1), k=(n+1)², f=2^n/(n!)².
These polynomials have integer coefficients. Define the rational linear functional ℒ by
ℒ(t^j)=μ_j=((1+i)^(j+1)−(1−i)^(j+1))/(i·2^j(j+1)).
Put E_j=Σ_{h=0}^j1/h!, T_0(Q)=Σ_d[t^d]Q(t)E_{n+d},
w_P=ℒ((P−a)/(t−1)), w_U=ℒ((U−b)/(t−1)),
P*=w_P+T_0(P), U*=w_U+T_0(U).
Define
H_m(x)=m![s^m]e^(xs)(1−s+s²/2)^m,
h_m=H_m(1), J_m=mh_m+H′_m(1),
K_m=m(m−1)h_m+2mH′_m(1)+H″_m(1),
η=h_{n+1}, S=J_{n+1}²−ηK_{n+1},
C=(J_{n+1}−η)J_n−(K_{n+1}−J_{n+1})h_n,
W=J_{n+1}J_n−K_{n+1}h_n,
D=kbC−2aS,
X=2P*S−kU*C−2fηW.
The letter C here denotes a scalar contraction.

Then a is a five-adic unit and
D≡4a mod 5, X/f≡2 mod 5.
In particular D and X are nonzero. If q_n is the positive reduced denominator of X/D, then
v_5(q_n)=2v_5(n!)=(n−s_5(n))/2.

The published exact rational reconstruction identifies X/D with the b=2 endpoint ratio A_raw(1)/B_raw(1), with
A_raw(1)=γX, B_raw(1)=γD,
γ=(−1)^n/[4(n+1)^3(n!)^4].
Thus in this specified raw normalization the endpoint valuations are −6r and −4r, respectively. No full polynomial coefficient-content assertion is made.

PROOF

1. Auxiliary reductions uniformly on the index progression.

For j=0,1,2 the interpolation of H_m^(j)(1) is
𝓗_j(Z)=Σ_{u,v≥0}(−1)^u(Z)_(u+2v+j)(Z)_(u+v)/(2^v u!v!),
where falling factorials have their usual meaning and (Z)_0=1. At nonnegative integers this is the defining finite expansion of H_m^(j)(1).

On Z=c+5Y, a falling factorial of length M has coefficientwise valuation at least floor(M/5). Set h=floor((u+2v)/5), ℓ=floor((u+v)/5). Since
v_5(u!v!)≤v_5((u+v)!)=ℓ+v_5(ℓ!),
each summand has coefficientwise valuation at least h−v_5(ℓ!)≥h−v_5(h!). For h≥1 this is positive and tends to infinity with h. The omitted sum with u+2v≥5 therefore converges in 5Z_5⟨Y⟩. Retained terms have unit denominators and reduce to their evaluations at c.

Use H_2=x²−4x+4 and H_3=x³−9x²+27x−24. Their derivative triples at one are (1,−2,2) and (−5,12,−12). Because n≡2 and n+1≡3, this gives
(h_n,J_n,η,J_{n+1},K_{n+1})≡(1,0,0,2,0),
(S,C,W,k)≡(4,2,0,4) modulo 5.
These reductions apply throughout the disks; they are not inferred from sampled indices.

2. Legendre endpoint units and D.

Writing A_m=L_m(1), Rodrigues' formula yields
A_m=[x^m](1+2x+2x²)^m,
A(z)=Σ_m A_mz^m=(1−4z−4z²)^(−1/2).
For Q(z)=1−4z−4z², the identity QA²=1 and Frobenius give, in F_5[[z]],
A(z)=Q(z)²A(z^5)=(1+2z+3z²+2z³+z⁴)A(z^5).
Hence A_{5j+d}≡c_dA_j, where c=(1,2,3,2,1). Every factor is nonzero and A_0=1, so every A_m is a unit. At n=5j+2, a≡3A_j and b≡2A_j, whence b≡4a. Consequently
D≡3(b−a)≡4a≠0 modulo 5.

3. Every surviving exponential-contraction term.

Put u_{m,j}=[t^j](1−2t+2t²)^m and e_j=j!E_j. Rodrigues' formula gives
[t^d]L_m(t)=(m+d)!u_{m,m+d}/(m!d!).
Substitution gives the exact sums
T_0(P)/f=2^(−n)Σ_{d=0}^n(n!/d!)u_{n,n+d}e_{n+d},
T_0(U)/f=[2^n(n+1)]^(−1)Σ_{d=0}^{n+1}(n!/d!)(n+1+d)u_{n+1,n+1+d}e_{n+d}.
All summands are five-adically integral. The sole nonintegral factorial quotient over Z, at d=n+1, is 1/(n+1), a five-adic unit. When d≤n−3 the quotient contains n−2, so that summand vanishes modulo 5. Retain d=n−2,n−1,n for P and d=n−2,n−1,n,n+1 for U.

The highest coefficients are
u_{m,2m}=2^m,
u_{m,2m−1}=−m2^m,
u_{m,2m−2}=m²2^(m−1),
u_{m,2m−3}=−m(m−1)(m+1)2^(m−1)/3,
where the symbol on each left side denotes the coefficient u. For the last expression, three linear selections or one linear and one constant selection contribute −2^m[binom(m,3)+m(m−1)/2]. The other formulas follow from zero, one, or two degrees of deficit from the leading term.

Thus the complete reductions are
T_0(P)/f≡[n³(n−1)/2]e_{2n−2}−n²e_{2n−1}+e_{2n},
T_0(U)/f≡−[n²(n−1)(n+2)(2n−1)/3]e_{2n−2}+2n²(n+1)e_{2n−1}−2(2n+1)e_{2n}+[4/(n+1)]e_{2n+1} modulo 5.

The recurrence e_0=1, e_j=je_{j−1}+1 gives residues (1,2,0,1,0) at indices congruent to (0,1,2,3,4) modulo 5. Since n≡2,
(e_{2n−2},e_{2n−1},e_{2n},e_{2n+1})≡(0,1,0,1).
The three P contributions are (0,1,0), and the four U contributions are (0,4,0,3). Therefore
T_0(P)/f≡1, T_0(U)/f≡2 modulo 5.
The U boundary contributes 3 and has been retained.

4. Moment bound and complete numerator.

The polynomial quotients defining w_P,w_U have integer coefficients and degree at most n. The displayed moment formula gives v_5(μ_j)≥−v_5(j+1), since its numerator divided by i is an integer. Also floor(log_5(n+1))=L: a change from floor(log_5 n) could occur only if n+1 were a power of five, excluded by n+1≡3. Hence
v_5(w_P),v_5(w_U)≥−L.
Since n≥7, L≥1; the integer 5^L is a factor in n!, giving r≥L. Therefore
v_5(w_P/f),v_5(w_U/f)≥2r−L≥1.
This also holds at n=7, where r=L=1. Only now may the moments be discarded modulo 5. We obtain P*/f≡1 and U*/f≡2. Retaining the complete correction term,
X/f=2(P*/f)S−k(U*/f)C−2ηW
≡2·1·4−4·2·2−2·0·0≡2 modulo 5.
Thus v_5(X)=−2r and X≠0.

5. Reduction, normalization, and arbitrary nearby valuations.

For rational X,D with D≠0, the reduced denominator of X/D satisfies v_5(q)=max(0,v_5(D)−v_5(X)). This does not require five-adic integrality of X. The proved valuations yield v_5(q_n)=2r. Legendre's factorial formula gives 2r=(n−s_5(n))/2.

Because n+1 is a unit, v_5(γ)=−4r, proving the stated raw endpoint valuations. Common rational normalization cancels from X/D; this observation alone does not replace the two unit arguments.

There is no restriction on v_5(n−2). All omitted summands have valuation at least v_5(n−2)≥1; larger valuations strengthen their vanishing. The retained expressions divide only by 2,3,n+1 and powers of 2, all units on this progression. Higher valuations of nearby index factors appearing in numerators cannot introduce denominators or invalidate the reductions. The argument therefore covers the entire stated progression without an exceptional-index hypothesis.

DEPENDENCIES, EVIDENCE, AND SCOPE

The exact rational endpoint reconstruction and common scaling are used from work/astra_review_registry/verified/b2-two-chart-actual-denominator-identities.md, payload SHA-256 ace0c8602da8ebb959a140d0a8e4dd9caf532014dc653f5328e909389ca4280d. Its large-prime local ideal theorem is not applied at five. The interpolation, Legendre recurrence, and factorial-sum framework also appear in work/astra_review_registry/verified/b2-five-adic-endpoint-denominator-v1.md, payload SHA-256 01a6d34706170e9b0b193c720e8ef0827f198102e1feba308852028cdeb51b81; the needed arguments are supplied above. The unapproved residue-one candidate is comparison material only, not a premise.

Author derivation: work/astra_20260929/worker_4/note_000084.md. Completed exact reconstructions: work/astra_20260929/worker_4/note_000085.md. At n=7,12,27 the full polynomial order conditions and endpoint-scaling checks passed, with (v_5(D),v_5(X),v_5(q_n)) respectively (0,−2,2), (0,−4,4), (0,−12,12). Each gave D/a≡4 and (T_0(P)/f,T_0(U)/f,X/f)≡(1,2,2). These are finite author checks, not independent approval or the proof of uniformity. No additional reconstruction was performed after those three.

Self-audit found no unresolved mathematical dependency beyond the published rational endpoint identification. Independent review remains required. The claim proves neither primitive coefficient content, other prime valuations, a full denominator upper bound, a shrinking sequence of integer forms, nor rationality or irrationality of e+pi.