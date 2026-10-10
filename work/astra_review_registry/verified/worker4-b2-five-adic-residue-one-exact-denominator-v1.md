> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact five-adic reduced-denominator valuation for the b=2 endpoint pair on indices congruent to one modulo five

Status: Independently reviewed research result (AI review; not formal verification)
Author: worker_4
Reviewer: worker_1
Content SHA256: cbf4838dfb7531fb17145053d4180baeed90ce8d9214d4f57197b1022eb790d3
Review: work/astra_review_registry/reviews/worker4-b2-five-adic-residue-one-exact-denominator-v1-worker_1.md

UNVERIFIED CANDIDATE. Author: worker_4. Independent review is required. This claim concerns the complete rational endpoint pair at the prime five on one index progression.

STATEMENT AND DEFINITIONS

Fix an integer n≥6 with n≡1 (mod 5). Write v=v_5, r=v(n!), L=floor(log_5 n), and v(0)=+∞. Define the rational moment functional by
ℒ(t^j)=μ_j=((1+i)^(j+1)−(1−i)^(j+1))/(i·2^j(j+1)).
Define the integral polynomials
L_m(t)=(1/m!)(d/dt)^m(2t²−2t+1)^m,
and put P=L_n, U=L_{n+1}, a=P(1), b=U(1), k=(n+1)², f=2^n/(n!)², g=2f/k, G=(−1)^n2^(2n+3)/(n+1).
For j=0,1,2 define
ℓ_j(t^d)=1/(n+d+1−j)!, E_m=Σ_{h=0}^m1/h!, T_j(Q)=Σ_d[t^d]Q(t)E_{n+d−j}.
All indices occurring here are nonnegative. Put
w_P=ℒ((P(t)−a)/(t−1)), w_U=ℒ((U(t)−b)/(t−1)),
P*=w_P+T_0(P), U*=w_U+T_0(U).

Define
H_m(x)=m![s^m]e^(xs)(1−s+s²/2)^m,
h_m=H_m(1), J_m=mh_m+H′_m(1),
K_m=m(m−1)h_m+2mH′_m(1)+H″_m(1).
Set
η=h_{n+1}, S=J_{n+1}²−ηK_{n+1},
C=(J_{n+1}−η)J_n−(K_{n+1}−J_{n+1})h_n,
W=J_{n+1}J_n−K_{n+1}h_n,
D=kbC−2aS, X=2P*S−kU*C−2fηW.
Here C is a scalar, distinct from the polynomial C_raw below.

To specify the raw normalization, let
α_j=ℓ_j(U), τ_j=(aT_j(U)−bT_j(P))/G,
(β_0,β_1,β_2)=(α_0,α_1,α_2)×(1+τ_0,1+τ_1,1+τ_2),
B_raw(z)=Σ_{j=0}^2β_jz^j.
With
K_n(t,s)=[U(t)P(s)−P(t)U(s)]/[G(t−s)],
define
Q_raw(t)=−Σ_{j=0}^2β_jℓ_j^sK_n(t,s),
C_raw(z)=z^nQ_raw(1/z),
A_raw(z)=−[B_raw(z)e^z+C_raw(z)F(z)]_{≤n},
where F(z)=4 arctan(z/(2−z)). The kernel K_n(t,s) is distinct from the scalar K_m.

The published exact rational reconstruction identities give
B_raw(1)=C_raw(1)=γD, A_raw(1)=γX,
γ=gf/(Gk)=(−1)^n/[4(n+1)^3(n!)^4].
Only these rational identities are imported; the large-prime local ideal theorem is not applied at five.

The conclusions are
D≡a≠0 (mod 5), X/f≡4 (mod 5), v(D)=0, v(X)=−2r.
In particular both endpoints are nonzero. If q_n denotes the positive reduced denominator of A_raw(1)/B_raw(1)=X/D, then
v_5(q_n)=2v_5(n!)=(n−s_5(n))/2,
where s_5(n) is the base-five digit sum. In the specified raw normalization,
v_5(A_raw(1))=−6r and v_5(B_raw(1))=−4r.
These last valuations concern endpoints, not full polynomial coefficient content. There is no loss involving v_5(n−1).

PROOF

1. Auxiliary contractions.

The exact falling-factorial interpolation is
𝓗_j(Z)=Σ_{u,v≥0}(−1)^u(Z)_(u+2v+j)(Z)_(u+v)/(2^v u!v!),
where (Z)_a=Z(Z−1)⋯(Z−a+1) and (Z)_0=1. At a nonnegative integer Z=m it equals H_m^(j)(1), by expansion of its defining polynomial.

On a disk Z=c+5Y, a falling factorial of length M has coefficientwise valuation at least floor(M/5). Put h=floor((u+2v)/5) and ℓ=floor((u+v)/5). Since
v_5(u!v!)≤v_5((u+v)!)=ℓ+v_5(ℓ!),
each interpolation summand has coefficientwise valuation at least
h−v_5(ℓ!)≥h−v_5(h!).
For h≥1 this is at least one and tends to infinity with h. There are only finitely many summands for each fixed h. Thus all terms with u+2v≥5 form a convergent sum in 5Z_5⟨Y⟩. Every retained denominator is a unit, so reduction of the retained polynomial on a disk is its value at the residue c.

At residues one and two, respectively, the derivative triples reduce to
(H_m(1),H′_m(1),H″_m(1))≡(0,1,0), (1,−2,2).
These values also follow directly from H_1(x)=x−1 and H_2(x)=x²−4x+4. Consequently, for the progression in the statement,
(h_n,J_n,η,J_{n+1},K_{n+1})≡(0,1,1,0,1),
(S,C,W,k)≡(4,4,0,4) (mod 5).
These reductions hold on the full auxiliary index disks, not merely at sampled indices.

2. Legendre endpoint units and denominator nonvanishing.

Write A_m=L_m(1). Rodrigues’ formula yields
A_m=[x^m](1+2x+2x²)^m,
Σ_{m≥0}A_mz^m=(1−4z−4z²)^(−1/2).
For example, expanding the central coefficient gives
A_m=Σ_{v=0}^{floor(m/2)}m!·2^(m−v)/(v!²(m−2v)!),
which gives the displayed generating function.

Let A(z)=ΣA_mz^m and Q(z)=1−4z−4z². In F_5[[z]], QA²=1 and A(z)^5=A(z^5); hence
A(z)=Q(z)²A(z^5)=(1+2z+3z²+2z³+z⁴)A(z^5).
It follows that A_{5m+d}≡c_dA_m, with c=(1,2,3,2,1). All digit factors are nonzero and A_0=1, so every A_m is a five-adic unit. Writing n=5m+1 gives a≡2A_m and b≡3A_m, hence b≡4a. Therefore
D=kbC−2aS≡b+2a≡a≠0 (mod 5).
This proves D≠0 directly.

3. Complete exponential contractions, including the boundary.

Put u_{m,j}=[t^j](1−2t+2t²)^m and e_j=j!E_j. Rodrigues’ formula gives
[t^d]L_m(t)=(m+d)!u_{m,m+d}/(m!d!).
Substitution into T_0 yields the exact expressions
T_0(P)/f=2^(−n)Σ_{d=0}^n(n!/d!)u_{n,n+d}e_{n+d},
T_0(U)/f=[2^n(n+1)]^(−1)Σ_{d=0}^{n+1}(n!/d!)(n+1+d)u_{n+1,n+1+d}e_{n+d}.
Every summand is five-adically integral. In the second expression the sole factorial quotient with a denominator occurs at d=n+1 and equals 1/(n+1), a unit.

For d≤n−2, the integer n!/d! contains n−1 and is divisible by five. Thus only d=n−1,n can survive in the first sum, and only d=n−1,n,n+1 in the second. The required coefficients are
u_{m,2m}=2^m, u_{m,2m−1}=−m2^m, u_{m,2m−2}=m²2^(m−1),
where the first left-hand symbol also denotes u with the indicated subscripts. The last formula follows by selecting either one constant term or two linear terms from the m factors.

The integer recurrence e_0=1, e_j=je_{j−1}+1 gives, for every h≥0,
(e_{5h},e_{5h+1},e_{5h+2},e_{5h+3},e_{5h+4})≡(1,2,0,1,0).
Since n≡1 (mod 5),
(e_{2n−1},e_{2n},e_{2n+1})≡(2,0,1).
The two surviving P terms yield
T_0(P)/f≡−n²e_{2n−1}+e_{2n}≡3 (mod 5).
The three surviving U terms yield
T_0(U)/f≡2n²(n+1)e_{2n−1}−2(2n+1)e_{2n}+[4/(n+1)]e_{2n+1}.
Their respective residues are 3,0,2, whose sum is zero modulo five. The third term is the d=n+1 boundary; omitting it would change the conclusion.

4. Moment-denominator losses and the complete numerator.

The quotient polynomials defining w_P,w_U have integral coefficients and degree at most n. The moment formula gives v_5(μ_j)≥−v_5(j+1), because its numerator divided by i is an integer and 2 is a unit. For 1≤j+1≤n+1 the largest possible valuation of j+1 is at most floor(log_5(n+1)). Since n+1≡2 (mod 5), n+1 is not a power of five, and this floor equals L=floor(log_5 n). Thus
v_5(w_P),v_5(w_U)≥−L.
Since n≥6, we have L≥1; the integer 5^L occurs among the factors of n!, so r≥L. Therefore
v_5(w_P/f),v_5(w_U/f)≥2r−L≥1.
This includes the smallest index n=6, where r=L=1. Combining with the exponential contractions gives
P*/f≡3, U*/f≡0 (mod 5).
Keeping the complete numerator, including its correction, now gives
X/f=2(P*/f)S−k(U*/f)C−2ηW≡2·3·4≡4 (mod 5).
Hence X≠0 and v_5(X)=v_5(f)=−2r.

5. Actual reduction and normalization.

For any nonzero rational pair X,D, the positive reduced denominator of X/D satisfies
v_5(q)=max(0,v_5(D)−v_5(X)).
This identity requires no integrality assumption. The valuations proved above give v_5(q_n)=2r. Legendre’s factorial formula gives 2r=(n−s_5(n))/2.

Since 5∤4(n+1)^3, v_5(γ)=−4r. The exact endpoint identities therefore give raw endpoint valuations −6r and −4r. Common nonzero rational normalization cancels from the ratio. No polynomial coefficient-content bound is used.

The factor n−1 enters only to make lower exponential-contraction terms vanish modulo five. Its higher valuation creates no denominator in either normalized contraction. The complete normalized numerator is a unit, so no term involving v_5(n−1) is lost in the resulting denominator formula.

DEPENDENCIES, EVIDENCE, AND SELF-AUDIT

The actual endpoint identification and common scaling are the exact rational identities in work/astra_review_registry/verified/b2-two-chart-actual-denominator-identities.md, payload SHA-256 ace0c8602da8ebb959a140d0a8e4dd9caf532014dc653f5328e909389ca4280d. The raw reconstruction is also explicitly specified above. The interpolation bound, Legendre digit argument, and contraction framework agree with work/astra_review_registry/verified/b2-five-adic-endpoint-denominator-v1.md, payload SHA-256 01a6d34706170e9b0b193c720e8ef0827f198102e1feba308852028cdeb51b81; the progression-specific calculations are supplied here. Neither the large-prime ideal theorem nor an analytic eventual-nonvanishing theorem is used at five.

The initial derivation is preserved in work/astra_20260929/worker_4/note_000074.md. Bounded exact reconstructions are preserved in work/astra_20260929/worker_4/note_000075.md. At n=6,11,16,21,26 they checked the complete polynomial order conditions and endpoint scaling. The respective triples (v_5(D),v_5(X),v_5(q_n)) were (0,−2,2), (0,−4,4), (0,−6,6), (0,−8,8), (0,−12,12). Every example gave (T_0(P)/f,T_0(U)/f,X/f)≡(3,0,4). The n=6 reduced denominator agreed with the previously preserved value 260737140696321600. These are finite author checks, not independent approval or proof of the general statement.

The hypotheses ensure that n+1 is a unit, the specified factorial-sum truncation is valid modulo five, and normalized moments vanish. Both D and X are proved nonzero. This claim makes no assertion about full coefficient content, primitive endpoint gcds, other index residues, other prime factors, analytic error rates, or the rationality of e+pi. Independent review remains outstanding.