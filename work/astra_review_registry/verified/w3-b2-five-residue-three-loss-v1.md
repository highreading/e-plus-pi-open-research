> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Five-adic unit numerator and eventual zero denominator loss for the b=2 endpoint on indices congruent to three modulo five

Status: Independently reviewed research result (AI review; not formal verification)
Author: worker_3
Reviewer: worker_2
Content SHA256: 4c6782bac2e4b40307b358ad9cb7dd30d0caaa7b00bad5bb0c608c52a001f142
Review: work/astra_review_registry/reviews/w3-b2-five-residue-three-loss-v1-worker_2.md

STATUS AND SCOPE

This is an unverified author submission for independent review. The claim concerns the exact b=2 endpoint ratio defined below. It establishes an eventual denominator lower bound, not an irrationality result.

Write v=v_5, with v(0)=+∞. For every integer n≥8 satisfying n≡3 (mod 5), set r=v(n!) and f=2^n/(n!)². Then

X/f≡1 (mod 5),   D≡0 (mod 5).

Consequently, whenever D≠0 and q_n is the positive reduced denominator of −X/D,

v(q_n)=2r+v(D)≥2r+1,
L_5(n):=max(0,2r−v(q_n))=0.

The published eventual-nonvanishing theorem identified below proves D≠0 for every sufficiently large n. Hence L_5(n)=0, and in particular L_5(n)=O(log n), for all sufficiently large n≡3 (mod 5). This submission does not prove D≠0 at every index n≥8 in the progression. The proposed equality v(q_n)=2v(n!) is false wherever this ratio is defined on the progression.

EXACT DEFINITIONS AND SOURCE DEPENDENCIES

Define the integral Rodrigues polynomials

L_m(z)=(1/m!) (d/dz)^m(1−2z+2z²)^m.

Put P=L_n, U=L_{n+1}, a=P(1), b=U(1), N=n+1, and k=N². Let E_j=Σ_{s=0}^j1/s!, e_j=j!E_j, and

T_0(Q)=Σ_d [z^d]Q(z) E_{n+d}.

Define the rational moments

μ_j=2 Im((1+i)^(j+1))/(2^j(j+1)),  j≥0,

and extend μ linearly to polynomials. For Q=P,U put

w_Q=μ((Q(z)−Q(1))/(z−1)),
P*=w_P+T_0(P),   U*=w_U+T_0(U).

Let c_{m,t}=[z^t](1−z+z²/2)^m and

H_m(x)=Σ_{t=0}^m (m)_t c_{m,t}x^{m−t},

where (m)_t=m(m−1)…(m−t+1), with (m)_0=1. Define

h=H_n(1),
J=nH_n(1)+H'_n(1),
η=H_N(1),
J_1=NH_N(1)+H'_N(1),
K_1=nNH_N(1)+2NH'_N(1)+H''_N(1),
S=J_1²−ηK_1,
C=(J_1−η)J−(K_1−J_1)h,
W=J_1J−K_1h.

The exact endpoint contractions are

D=kbC−2aS,
X=2P*S−kU*C−2fηW.

These are the definitions and identities of the published files:

1. work/astra_review_registry/verified/b2-two-chart-actual-denominator-identities.md, payload SHA-256 ace0c8602da8ebb959a140d0a8e4dd9caf532014dc653f5328e909389ca4280d.
2. work/astra_review_registry/verified/b2-five-adic-endpoint-denominator-v1.md, payload SHA-256 01a6d34706170e9b0b193c720e8ef0827f198102e1feba308852028cdeb51b81.

The rational contraction identities apply at five; no large-prime hypothesis from a separate local-ideal theorem is used. The actual approximant is −X/D, and changing its sign does not change its reduced denominator.

Eventual nonvanishing of this same D, with the same normalization and index, is supplied by:

3. work/astra_review_registry/verified/w3-b2-eventual-d-nonzero-v1.md, payload SHA-256 66273b26045bf283eff8b3b503e2c51141e05c2c3f0bf128a8412e1fdec6817f.

The proof below derives the new congruences from these exact definitions. Source 3 is needed only for the unconditional eventual conclusion.

PROOF OF THE AUXILIARY CONGRUENCES

All c_{m,t} belong to Z[1/2]. Differentiating the definition gives

H_m^(j)(1)=Σ_{t=0}^{m−j}(m)_{t+j}c_{m,t}.

Write m=5u+d with 0≤d≤4. If t+j≥d+1, the falling product contains m−d and is zero modulo five. In every remaining term t≤d−j<5. The polynomial congruence

(1−z+z²/2)^m≡(1−z^5+z^10/2)^u(1−z+z²/2)^d (mod 5)

therefore implies c_{m,t}≡c_{d,t} for every needed coefficient. It follows that H_m^(j)(1)≡H_d^(j)(1) modulo five, for j=0,1,2. If j>d, both sides are zero modulo five by the same argument.

Direct expansion gives

H_3(x)=x³−9x²+27x−24,
H_4(x)=x⁴−16x³+96x²−240x+204.

Their value/first-derivative/second-derivative triples at one reduce respectively to (0,2,3) and (0,3,3). Since n≡3 and N≡4, this yields

(h,J,η,J_1,K_1)≡(0,2,0,3,2),
(S,C,W,k)≡(4,1,1,1) (mod 5).

For completeness, the Legendre endpoint digit relation can also be proved directly. Write A_m=L_m(1). By shifting the Rodrigues polynomial,

A_m=[w^m](1+2w+2w²)^m=CT(w^(−1)+2+2w)^m.

For 0≤d≤4, reduction modulo five gives

A_{5u+d}≡A_u A_d.

Indeed, after applying the fifth-power congruence, the exponents from the second factor lie between −d and d; its only exponent divisible by five is zero. The initial values A_0,…,A_4 are 1,2,8,32,136, reducing to (1,2,3,2,1). Induction on base-five digits shows that every A_m is a unit modulo five. For n=5u+3 and N=5u+4,

a≡2A_u,   b≡A_u≡3a (mod 5).

Thus

D=kbC−2aS≡b−8a≡0 (mod 5).

The definitions place D in Z[1/2], so v(D)≥1 whenever D≠0. This conclusion does not require an all-index nonvanishing theorem.

COMPLETE EXPONENTIAL CONTRACTIONS

Reversing the coefficient polynomial gives

[z^{2m−t}](1−2z+2z²)^m=2^m c_{m,t}.

Substitution into the Rodrigues coefficients proves the exact finite identities

T_0(P)/f=Σ_{t=0}^n (n)_t c_{n,t}e_{2n−t},

T_0(U)/f=(2/N²)Σ_{t=0}^N (N)_t(2N−t)c_{N,t}e_{2N−1−t}.

The second sum includes its t=0 term. Its prefactor is a five-adic unit because N≡4. All other displayed coefficient denominators are powers of two.

The recurrence e_0=1 and e_j=je_{j−1}+1 gives the periodic residue list

e_j≡(1,2,0,1,0) for j≡(0,1,2,3,4) (mod 5).

For the P sum, every t≥4 term vanishes modulo five because (n)_t contains n−3. For t=0,1,2,3 the respective lists are

(n)_t:          (1,3,1,1),
c_{n,t}:        (1,2,2,1),
e_{2n−t}:       (2,1,0,1).

The four term contributions are (2,1,0,1), so T_0(P)/f≡4.

For the U sum, every t≥5 term vanishes because (N)_t contains N−4. For t=0,1,2,3,4 the lists are

(N)_t:              (1,4,2,4,4),
c_{N,t}:            (1,1,3,0,1),
2N−t:               (3,2,1,0,4),
e_{2N−1−t}:         (0,2,1,0,1).

Their products are (0,1,1,0,1). Multiplication by 2/N²≡2 gives T_0(U)/f≡1. These lists account for every potentially surviving exponential term.

NORMALIZED MOMENT ESTIMATE

Both Rodrigues polynomials have integral coefficients: differentiating a monomial z^s and dividing by m! multiplies its coefficient by binom(s,m). Division of Q(z)−Q(1) by z−1 therefore produces an integral polynomial. The resulting quotient degrees are at most n−1 for P and n for U.

The explicit moment formula implies v(μ_j)≥−v(j+1). Set L=floor(log_5 n). Since n+1≡4 modulo five, n+1 is not a positive power of five, so floor(log_5(n+1))=L. Every moment used in w_P,w_U consequently has valuation at least −L, giving

v(w_P),v(w_U)≥−L.

Because n≥8, L≥1. The factor 5^L occurs among 1,…,n, hence r=v(n!)≥L. Since v(f)=−2r,

v(w_P/f),v(w_U/f)≥2r−L≥1.

This proves that the normalized moment contributions vanish modulo five before they are discarded. Therefore

P*/f≡4,   U*/f≡1 (mod 5).

ACTUAL NUMERATOR AND REDUCED DENOMINATOR

Keeping the full correction term in the contraction gives

X/f=2(P*/f)S−k(U*/f)C−2ηW
   ≡2·4·4−1·1·1−2·0·1
   ≡1 (mod 5).

Hence X is nonzero and v(X)=v(f)=−2r. If D≠0, reduction of the rational number −X/D gives

v(q_n)=max(0,v(D)−v(X)).

This formula does not assume X is an integer. Since v(D)≥1, it becomes

v(q_n)=2r+v(D)≥2r+1,
L_5(n)=0.

Source 3 proves eventual nonvanishing for exactly this D. Applying it completes the asserted eventual result on the progression. No upper bound on v(D), higher-congruence nonvanishing, or estimate on its possible positive valuation is necessary for this lower-bound conclusion.

BOUNDED AUTHOR CHECKS AND EVIDENCE

The saved exact computation work/astra_20260929/worker_3/calculation_000102.py independently reconstructed the original endpoint polynomials only at n=8,23,28. Its reported execution passed all assertions, including the original order conditions, matching, endpoint scalar normalization, contractions, and rational denominator reduction. The output is summarized in work/astra_20260929/worker_3/note_000103.md. The preceding general derivation is preserved in work/astra_20260929/worker_3/note_000102.md.

The respective triples (v(D),v(X),v(q_n)) were

n=8:  (1,−2,3),
n=23: (2,−8,10),
n=28: (1,−12,13).

All three gave X/f≡1 and normalized exponential contractions (4,1) modulo five. Their normalized moment valuations were respectively (1,1), (8,8), and (10,10). In particular, n=8 is an exact counterexample to the proposed equality v(q_n)=2v(n!). These are finite author checks, not a proof of the progression or independent approval.

SELF-AUDIT AND UNRESOLVED SCOPE

The proof retains all surviving exponential terms and establishes the normalized moment estimate separately. The auxiliary congruences use a finite coefficient argument and do not rely on numerical interpolation or an infinite-tail assertion. The same endpoint ratio and index are retained throughout. The rational denominator formula allows the negative valuation of X and does not substitute a primitive-content valuation for the actual denominator.

The congruences hold for every n≥8 in the stated progression. The denominator identity is conditional on D≠0 there; the unconditional conclusion is eventual and uses the explicitly cited published theorem. Its threshold is not made effective. Independent review of this submission remains required. No sufficient global upper bound on q_n, shrinking linear form, or rationality or irrationality conclusion for e+pi is claimed.