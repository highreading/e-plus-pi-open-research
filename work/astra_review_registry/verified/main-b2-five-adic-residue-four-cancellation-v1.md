> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Five-adic denominator valuation and forced numerator cancellation for the b=2 endpoint on indices congruent to four modulo five

Status: Independently reviewed research result (AI review; not formal verification)
Author: main
Reviewer: worker_2
Content SHA256: b123168c159b9a62d863ee40ffdae485533f2229e99c368b6cd671e04f321519
Review: work/astra_review_registry/reviews/main-b2-five-adic-residue-four-cancellation-v1-worker_2.md

STATUS AND SCOPE

Unverified lead candidate for independent review. This concerns the exact b=2 rational endpoint pair. It proves no rationality or irrationality statement about e+pi.

Write v=v_5 and v(0)=+∞. For every integer n≥4 with n≡4 (mod 5), put m=n+1, r=v(n!), s=v(m), and f=2^n/(n!)². With the definitions below,

v(D)=s, so D≠0.

For n≥9 in this progression, define Z_n=X/(fm). Then

Z_n∈5Z_5,
v(q_n)=max(0,2r−v(Z_n))≤2r−1,

where q_n is the positive reduced denominator of −X/D. If X=0, the denominator is 1 and the displayed maximum is interpreted as zero. Equivalently, the nonnegative loss max(0,2r−v(q_n)) equals min(2r,v(Z_n)). No upper bound on v(Z_n) is asserted.

EXACT DEFINITIONS

Let
L_j(t)=(1/j!)(d/dt)^j(1−2t+2t²)^j,
P=L_n, U=L_m, a=P(1), b=U(1).

These are the integral Legendre normalizations used in the published endpoint identities. Define ℒ(Q)=∫_{−1}^1 Q((1+iu)/2)du and
w_P=ℒ((P(t)−a)/(t−1)),
w_U=ℒ((U(t)−b)/(t−1)).

Put E_j=Σ_{h=0}^j1/h!, e_j=j!E_j,
T_0(Q)=Σ_d[t^d]Q(t)E_{n+d},
P*=w_P+T_0(P), U*=w_U+T_0(U).

For every nonnegative integer j define
H_j(x)=j![z^j]e^{xz}(1−z+z²/2)^j,
h_j=H_j(1),
J_j=jh_j+H'_j(1),
K_j=j(j−1)h_j+2jH'_j(1)+H''_j(1).

Set
S=J_m²−h_mK_m,
C=(J_m−h_m)J_n−(K_m−J_m)h_n,
W=J_mJ_n−K_mh_n,
D=m²bC−2aS,
X=2P*S−m²U*C−2fh_mW.

The published rational endpoint identification gives A_raw(1)=γX and B_raw(1)=γD, where γ=(−1)^n/[4m³(n!)⁴]. Thus reduction of −X/D includes all endpoint cancellation independently of primitive polynomial coefficient normalization. In particular, the denominator conclusion also gives v(B_raw(1))=−4r−2s.

PROOF

1. Auxiliary estimates at arbitrary depth s.

Using falling factorials, direct coefficient expansion gives, for j=0,1,2,
H_m^(j)(1)=Σ_{u,w≥0}(−1)^u(m)_{u+2w+j}(m)_{u+w}/(2^w u!w!).
Only finitely many terms are nonzero. The u=w=0 term is respectively 1, m, m(m−1).

For every other nonzero term let R=u+2w and t=u+w>0. Remove the initial factor m from both falling factorials. The remaining term has valuation at least
floor((R+j−1)/5)+floor((t−1)/5)−v(u!w!).
Indeed, each residual product of length k−1 contains at least floor((k−1)/5) multiples of five.

Set q=floor(t/5) and ε=1 if 5 divides t, otherwise ε=0. Binomial integrality and Legendre’s formula give
v(u!w!)≤v(t!)=q+v(q!).
Since R≥t, the lower bound is at least q−2ε−v(q!) for j=0 and q−ε−v(q!) for j=1,2. These are respectively ≥−1 and ≥0: for q=0, ε=0; for q≥1 use v(q!)≤q−1.

Consequently
h_m=1+m²A,
H'_m(1)=m+m²B,
H''_m(1)=m(m−1)+m²E,
with v(A)≥−1 and B,E∈Z_5. Expanding the definitions,
J_m=2m+m²(mA+B),
K_m=−2m+m²[4+m(m−1)A+2mB+E].
Since 5 divides m, both bracketed corrections are integral. Therefore
h_m≡1, J_m/m≡2, K_m/m≡−2 (mod 5).

2. Residue-four values and the denominator.

Let c_{j,t}=[z^t](1−z+z²/2)^j. Then
H_j^(h)(1)=Σ_t(j)_{t+h}c_{j,t}.
For j=5u+d, 0≤d≤4, all terms with t+h>d vanish modulo five. In the remaining terms t<5, Frobenius gives c_{j,t}≡c_{d,t}. Hence H_j^(h)(1)≡H_d^(h)(1) for h=0,1,2.

Direct expansion yields
H_4(x)=x⁴−16x³+96x²−240x+204,
(H_4(1),H'_4(1),H''_4(1))=(45,−92,108)≡(0,3,3).
Thus h_n≡0 and J_n≡3. The definitions and step 1 give
S/m≡2, C≡2, W/m≡1 (mod 5).

Every Legendre endpoint A_j=L_j(1) is a five-adic unit. To see this directly, Rodrigues’ formula gives
A_j=CT(z^(−1)+2+2z)^j.
For j=5u+d with 0≤d≤4, Frobenius and the exponent range [−d,d] imply A_j≡A_uA_d (mod 5). The initial residues A_0,…,A_4 are (1,2,3,2,1). Induction on base-five digits proves the unit assertion.

In particular a is a unit, and
D/m=mbC−2a(S/m)≡−4a≡a (mod 5).
This proves v(D)=s and D≠0. The stated raw endpoint valuation follows from γ.

3. Complete exponential contractions.

The recurrence e_0=1, e_j=je_{j−1}+1 gives e_j≡(1,2,0,1,0) according to j modulo five. Rodrigues’ formula and coefficient reversal give the exact identity
T_0(P)/f=Σ_{t=0}^n(n)_t c_{n,t}e_{2n−t}.
Every t≥5 term vanishes modulo five. For t=0,…,4, the coefficients c_{n,t} reduce to those at n=4, namely (1,−4,8,−10,17/2). Including the falling factorials and e residues, the five contributions are (1,0,2,0,0). Therefore T_0(P)/f≡3 (mod 5).

For U put u_{m,j}=[t^j](1−2t+2t²)^m. Direct substitution of its Rodrigues coefficients gives
mT_0(U)/f=2^(1−m)Σ_{d=0}^m[(m−1)!/d!](m+d)u_{m,m+d}e_{m−1+d}.
For d≤m−1 the factorial quotient is integral. Since 5 divides m, Frobenius makes u_{m,m+d} divisible by five unless 5 divides m+d; in that remaining case the explicit factor m+d supplies divisibility.

At d=m the factorial quotient is 1/m and must be cancelled exactly. Since u_{m,2m}=2^m, this boundary contribution is 4e_{2m−1}. It vanishes modulo five because 2m−1≡4. Hence mT_0(U)/f∈5Z_5. No inversion of m modulo five has been used.

4. Moments and the full numerator.

The polynomials (P−a)/(t−1) and (U−b)/(t−1) have integral coefficients and degrees at most n. The exact monomial moment is
ℒ(t^j)=((1+i)^(j+1)−(1−i)^(j+1))/(i2^j(j+1)),
so v(ℒ(t^j))≥−v(j+1).

Let L=floor(log_5(n+1)). Then v(w_P),v(w_U)≥−L. For n≥9, r≥L≥1. If L=1 this is immediate; if L≥2, n≥5^L−1 gives r≥floor(n/5)≥5^(L−1)−1≥L. Thus this estimate includes n+1=5^L.

Since v(f)=−2r, both normalized moments have valuation at least 2r−L≥1. Consequently P*/f≡3 and mU*/f≡0 (mod 5).

Retaining every term of the exact numerator,
Z_n=2(P*/f)(S/m)−(mU*/f)C−2h_m(W/m)
≡2·3·2−0−2·1·1=10≡0 (mod 5).
All terms are integral, so Z_n∈5Z_5, allowing zero.

Finally v(X)=−2r+s+v(Z_n), with the extended valuation convention. Since D≠0, ordinary rational reduction gives
v(q_n)=max(0,v(D)−v(X))=max(0,2r−v(Z_n)).
The claimed inequality and exact loss identity follow.

DEPENDENCIES, EVIDENCE, AND SELF-AUDIT

The rational endpoint identification and common raw scaling are imported from work/astra_review_registry/verified/b2-two-chart-actual-denominator-identities.md, reviewed payload SHA-256 ace0c8602da8ebb959a140d0a8e4dd9caf532014dc653f5328e909389ca4280d. Its large-prime local-ideal theorem is not applied at five. The small-prime calculations used here are derived explicitly above.

The original lead derivation is work/astra_20260929/main/note_000169.md, file SHA-256 37498ff4a566349b3182b0a854facadbd187dc1dd90ec9cfb8ae3d03ab212b22. Worker_2’s preparatory independent derivation audit is recorded in work/astra_20260929/worker_2/note_000120.md. That report is supporting evidence, not approval of this immutable candidate. Worker_4’s separate finite reconstruction is still pending and is not used as proof.

The denominator assertion starts at n=4; the numerator and loss assertions start at n=9. The proof handles arbitrary v_5(n+1), the nonintegral factorial quotient in the boundary term, the power-of-five moment boundary, and possible X=0. It does not determine polynomial coefficient content, other-prime factors, an upper bound on v(Z_n), or a useful global upper bound on q_n. Independent review remains required.