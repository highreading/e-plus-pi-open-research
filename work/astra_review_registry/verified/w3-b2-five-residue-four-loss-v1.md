> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact five-adic numerator loss for the b=2 endpoint on indices congruent to four modulo five beyond n=9

Status: Independently reviewed research result (AI review; not formal verification)
Author: worker_3
Reviewer: worker_2
Content SHA256: e08cc00ef7c40a2bdfda278145fa8330dbac4fbc58b3723fe44b76131acf8e43
Review: work/astra_review_registry/reviews/w3-b2-five-residue-four-loss-v1-worker_2.md

Status: unverified author candidate submitted for independent review. This claim concerns the exact b=2 endpoint numerator and reduced denominator. It proves no rationality or irrationality statement about e+pi.

For every integer n≥14 with n≡4 modulo five, put m=n+1, r=v_5(n!), s=v_5(m), and f=2^n/(n!)². Define X,D and Z_n=X/(fm) below. Then

Z_n≡20 (mod 25),
Z_n/5≡4 (mod 5),
v_5(Z_n)=1,
v_5(X)=s−2r+1,
v_5(q_n)=2r−1,

where q_n is the positive reduced denominator of −X/D. In particular X and D are nonzero on this domain.

The complete normalized exponential contribution is already 20 modulo 25 for every n≥9 in the progression. The conclusion about the full Z_n starts at n=14 because the moment contribution requires separate treatment at n=9. No assertion about v_5(Z_9) is part of this claim.

Exact definitions and published inputs.

Let

L_a(t)=(1/a!)(d/dt)^a(1−2t+2t²)^a,
P=L_n, U=L_m, a=P(1), b=U(1).

Define ℒ(Q)=∫_(−1)^1 Q((1+ix)/2)dx and

w_P=ℒ((P(t)−a)/(t−1)),
w_U=ℒ((U(t)−b)/(t−1)).

For k≥0 put E_k=Σ_(v=0)^k 1/v!, e_k=k!E_k. The transform used for both P and U has the SAME index n:

T_0(Q)=Σ_d [t^d]Q(t) E_(n+d).

Write P*=w_P+T_0(P) and U*=w_U+T_0(U). Set

Q(z)=1−z+z²/2,
c_(a,t)=[z^t]Q(z)^a,
H_a(x)=a![z^a]exp(xz)Q(z)^a,
h_a=H_a(1),
J_a=ah_a+H'_a(1),
K_a=a(a−1)h_a+2aH'_a(1)+H''_a(1).

Finally define

S=J_m²−h_mK_m,
C=(J_m−h_m)J_n−(K_m−J_m)h_n,
W=J_mJ_n−K_mh_n,
D=m²bC−2aS,
X=2P*S−m²U*C−2fh_mW.

The published endpoint identification establishes that −X/D is the actual rational approximant, including every endpoint cancellation. The published residue-four theorem establishes v_5(D)=s and

v_5(q_n)=max(0,2r−v_5(Z_n)).

It also establishes v_5(w_P),v_5(w_U)≥−L, where L=floor(log_5(n+1)). These are the only arithmetic conclusions imported below. The new numerator congruence is proved explicitly.

1. Exact formulas retaining normalization and the boundary term.

For a nonnegative integer a, write (a)_t=a(a−1)…(a−t+1), with (a)_0=1. Coefficient extraction gives

H_a^(d)(1)=Σ_t (a)_(t+d)c_(a,t).

All these sums terminate. Put h=h_m, j=J_m/m, and k=K_m/m. Cancelling m algebraically before any modular reduction gives

h=Σ_t (m)_t c_(m,t),
j=h+Σ_t (m−1)_t c_(m,t),
k=(m−1)h+2H'_m(1)+Σ_t (m−1)_(t+1)c_(m,t).

Their right sides belong to Z[1/2], so these expressions do not lose precision when v_5(m) is large.

Set A=T_0(P)/f and B=mT_0(U)/f. Rodrigues coefficient reversal gives the exact formulas

A=Σ_(t=0)^n (n)_t c_(n,t)e_(2n−t),
B=4e_(2m−1)+2Σ_(t=1)^m (m−1)_(t−1)c_(m,t)(2m−t)e_(2m−1−t).

For clarity, if u_(m,k)=[t^k](1−2t+2t²)^m, then u_(m,2m−t)=2^m c_(m,t). Substitution into Rodrigues' formula gives

B=2^(1−m)Σ_(d=0)^m ((m−1)!/d!)(m+d)u_(m,m+d)e_(m−1+d).

At d=m the apparent factor 1/m cancels exactly, producing 4e_(2m−1). For d≤m−1, substitution t=m−d produces the displayed finite sum. Thus the singular boundary term has been retained exactly.

Define

T=S/m=mj²−hk,
V=W/m=jJ_n−kh_n.

Then

C=(mj−h)J_n−m(k−j)h_n,
Z_n=F_n+M_n,
F_n=2AT−BC−2hV,
M_n=2(w_P/f)T−(mw_U/f)C.

These identities include every term of the actual numerator.

2. Uniform truncation modulo 25.

Every c_(a,t) belongs to Z[1/2]. Any product of ten consecutive integers is divisible by 25. Consequently h,h_n,A and the additional sum in j may be truncated at t=9; H'_m,H'_n and the additional sum in k may be truncated at t=8; B may be truncated at t=10 together with its separate boundary term. These are termwise bounds, valid without any restriction on s=v_5(m).

For n≥9, all exponential indices in these retained sums are nonnegative, and all retained ranges lie within the appropriate original sums. No extension to undefined e indices is used.

3. Coefficient and falling-factorial reductions.

Write m=5u. All congruences until the moment estimate are in Z_5. Direct expansion of Q(z)^a gives the following coefficients for t=0,…,4, modulo 25:

(c_(m,t)) = (1,−m,0,m/6,m/8),
(c_(n,t)) = (1,1−m,1/2−m,−m/3,−1/4+7m/24).

For example, the exact degree-two, degree-three, and degree-four coefficients of Q(z)^a are a²/2, −(a³−a)/6, and (a⁴−4a²+3a)/24. Thus the displayed reductions involve only denominators prime to five.

Frobenius gives Q(z)^m≡Q(z^5)^u modulo five. Hence c_(m,5)≡−u and c_(m,t)≡0 for 6≤t≤9. From Q(z)^(m−1)=Q(z)^m/Q(z), or direct coefficient multiplication, it follows that

(c_(n,5),…,c_(n,9))≡(1−u,3−u,2u,1,1−u) (mod 5).

For verification of this last multiplication, the coefficients of 1/Q(z) through degree nine are

1,1,1/2,0,−1/4,−1/4,−1/8,0,1/16,1/16.

Put P_t=(m−1)_t. Multiplication of consecutive factors gives

(P_0,…,P_4)≡(1,m−1,2−3m,−6+11m,24) (mod 25),
(P_5,…,P_9)≡(m−5)(4,1,3,1,1) (mod 25).

In the second identity, m−5 already supplies a factor five, so the other factors need only be reduced modulo five. These identities remain valid when m−5 has greater valuation or is zero.

4. Auxiliary scalar reductions.

In h_m, the t=1,…,4 terms vanish modulo 25 because both their falling factorial and their coefficient contain a factor m. The t=5 term is 5u² modulo 25. Terms t=6,…,9 contain both m and m−5. Similarly H'_m≡m. Thus

h≡1+5u²,
H'_m(1)≡m (mod 25).

The coefficient tables give

Σ_(t=0)^9 P_t c_(m,t)≡1+3m+5u(u−1),
Σ_(t=0)^8 P_(t+1)c_(m,t)≡3m−1−5u(u−1).

Substitution into the division-free formulas yields

j≡2+10u+10u²,
k≡−2+10u−10u² (mod 25).

For h_n, the t=0,…,4 terms sum to −5 modulo 25. The remaining t=5,…,9 terms sum to 4(m−5). Therefore h_n≡4m=20u.

For H'_n, the t=0,…,3 terms sum to −2+(9/2)m modulo 25, and the t=4,…,8 terms sum to 3u(m−5). Hence

H'_n(1)≡−2+20u+15u²,
J_n=nh_n+H'_n(1)≡−2+15u² (mod 25).

This proves all required auxiliary reductions using finite sums with no division by m.

5. Complete exponential reductions.

The exact recurrence e_0=1, e_j=je_(j−1)+1 gives, for every integer v≥0,

(e_(5v),…,e_(5v+4))
≡(1,5v+2,5(4v+1),10v+16,5(4v+3)) (mod 25).

Indeed the recurrence gives these four successors from e_(5v)≡1, and then e_(5v+5)≡1 because e_(5v+4) is divisible by five. This proves the formula by induction from v=0.

For A, the e factors at t=0,…,4 are therefore

(6+20u,10+15u,−3+10u,1,15u) (mod 25).

At t=5,…,9 their reductions modulo five are (1,0,2,1,0). Multiplying by the coefficient and falling-factorial tables in part 3, the first five contributions sum to 18 modulo 25 and the last five sum to 3u(m−5)=15u(u−1). Consequently

A≡18+10u+15u² (mod 25).

For B, the boundary contributes

4e_(2m−1)≡5+10u (mod 25).

The t=1,…,4 contributions in its remaining sum are respectively 2m,0,−4m,6m modulo 25, summing to 4m. At t=5, both 2m−5 and e_(2m−6) are divisible by five. At t=6,…,9, both c_(m,t) and the falling factorial are divisible by five. At t=10, both 2m−10 and the falling factorial are divisible by five. All these terms therefore vanish modulo 25; t≥11 was already covered by uniform truncation. It follows that

B≡5+10u+4m≡5(u+1) (mod 25).

This calculation retains the singular boundary and every other potentially surviving exponential term.

6. Universal exponential cancellation at the next digit.

Collecting the proved reductions,

h≡1+5u²,
j≡2+10u+10u²,
k≡−2+10u−10u²,
h_n≡20u,
J_n≡−2+15u²,
A≡18+10u+15u²,
B≡5(u+1) (mod 25).

Direct multiplication now gives

T=mj²−hk≡2+10u+20u²,
V=jJ_n−kh_n≡−4+20u+10u²,
C=(mj−h)J_n−m(k−j)h_n≡2+5u−5u² (mod 25).

In particular,

2AT≡22+5u²,
2hV≡17+15u+5u²,
BC≡10u+10 (mod 25).

Therefore

F_n=2AT−BC−2hV≡−5−25u≡20 (mod 25).

This proves the exponential congruence for every n≥9 in the progression. The component formulas depend only on u modulo five, equivalently n modulo 25, and their final combination is constant. No finite-sample inference or assumption of finite residue dependence is involved.

7. Moments and the stated threshold.

The published moment estimate gives v_5(w_P),v_5(w_U)≥−L, with L=floor(log_5(m)). Since v_5(f)=−2r and T,C are integral by the division-free formulas,

v_5(M_n)≥2r−L.

For n≥14 in the progression, r≥L+1. If L=1, n≥14 gives r≥2. If L≥2, m≥5^L gives

r≥floor(n/5)≥5^(L−1)−1≥L+1.

Thus 2r−L≥L+2≥3, and M_n belongs to 125Z_5. Combining this with F_n≡20 modulo 25 gives Z_n≡20 modulo 25 and v_5(Z_n)=1.

The exact identity X=fmZ_n gives v_5(X)=−2r+s+1. The published v_5(D)=s and ordinary rational reduction then give

v_5(q_n)=max(0,s−(−2r+s+1))=2r−1,

because r≥2 on the stated domain. This also proves X≠0; D≠0 is already supplied by its published valuation.

At n=9, r=L=1 and the bound gives only v_5(M_9)≥1. The exponential congruence therefore cannot be transferred to Z_9 by this omission argument. The stated threshold preserves that exception.

Dependencies and evidence.

The exact endpoint definitions and identification are from work/astra_review_registry/verified/b2-two-chart-actual-denominator-identities.md, reviewed payload SHA-256 ace0c8602da8ebb959a140d0a8e4dd9caf532014dc653f5328e909389ca4280d. Its large-prime ideal theorem is not applied at five.

The imported valuation v_5(D)=v_5(n+1), rational denominator identity, and moment bound are from work/astra_review_registry/verified/main-b2-five-adic-residue-four-cancellation-v1.md, reviewed payload SHA-256 b123168c159b9a62d863ee40ffdae485533f2229e99c368b6cd671e04f321519.

Earlier author evidence is preserved in work/astra_20260929/worker_3/note_000125.md, note_000127.md, calculation_000125.py, and calculation_000127.py. The completed exact representative calculation at n=14,19,24,29,34 returned F_n≡20 in every case. Those checks support the calculation but are not used to infer the universal theorem: parts 3–6 supply a symbolic proof. Historical successful calculations and this author audit are not independent approval.

Self-audit and limits.

The T_0 index remains n for both polynomials. Division by m is performed exactly before reduction; no precision depending on v_5(m) is silently discarded. The singular boundary term in B is included. Every discarded exponential summand has an explicit termwise valuation bound. The moment argument includes indices immediately below powers of five. The exponential statement starts at n=9, while the full numerator and denominator conclusions start at n=14. The result supplies exact local denominator information, not polynomial coefficient content, other-prime valuations, a sufficient global denominator upper bound, or a rationality conclusion. No unresolved mathematical premise remains within the scoped proof beyond the cited published inputs; independent review of this candidate remains required.