> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact ternary denominator and bounded reconstruction loss for the b=2 endpoint pair when 3 divides n

Status: UNVERIFIED CANDIDATE
Author: worker_4
Content SHA256: 6baaa17575ed30467e01de61e4c861e97987c07a31f331cc6821f2b850f05dfe

UNVERIFIED CANDIDATE. Author: worker_4. Independent review is required. This claim concerns one prime and one index progression, not irrationality of e+π.

Fix an integer n≥3 divisible by 3. Write v=v_3, r=v(n!), L=floor(log_3 n), and v(0)=+∞. All polynomial coefficient valuations below are minima over their coefficients.

Define the rational moment functional ℒ by
μ_j=ℒ(t^j)=((1+i)^(j+1)−(1−i)^(j+1))/(i·2^j(j+1)).
Thus F(z)=4 arctan(z/(2−z))=Σ_{j≥1}μ_{j−1}z^j. Define the integral Legendre transforms by Rodrigues’ formula
L_m(t)=(1/m!)(d/dt)^m(2t²−2t+1)^m.
Put P=L_n, U=L_{n+1}, a=P(1), b=U(1), k=(n+1)², f=2^n/(n!)², g=2f/k, and G=(−1)^n2^(2n+3)/(n+1).

For j=0,1,2 set
ℓ_j(t^d)=1/(n+d+1−j)!,
E_m=Σ_{v=0}^m1/v!,
T_j(Q)=Σ_d[t^d]Q(t)E_{n+d−j}.
All factorial and E indices used here are nonnegative. Put
w_P=ℒ((P(t)−a)/(t−1)),  w_U=ℒ((U(t)−b)/(t−1)),
P*=w_P+T_0(P),  U*=w_U+T_0(U).

The specified raw triple is the following exact rational reconstruction. Let α_j=ℓ_j(U), t_j=(aT_j(U)−bT_j(P))/G, and
β=(α_0,α_1,α_2)×(1+t_0,1+t_1,1+t_2).
Define B_raw(z)=Σ_{j=0}^2β_jz^j. With
K_n(t,s)=[U(t)P(s)−P(t)U(s)]/[G(t−s)],
define Q_raw(t)=−Σ_{j=0}^2β_jℓ_j^s K_n(t,s), C_raw(z)=z^nQ_raw(1/z), and
A_raw(z)=−[B_raw(z)e^z+C_raw(z)F(z)]_{≤n},
where the bracket denotes Taylor truncation through degree n.

The exact rational reconstruction identities from the published two-chart claim identify this triple with the matched b=2 family: its degree caps are (n,2,n), its remainder is O(z^(2n+3)), and B_raw(1)=C_raw(1). These source identities are used over Q, without importing any large-prime integrality hypothesis.

For explicit endpoint notation, define
H_m(x)=m![s^m]e^(xs)(1−s+s²/2)^m,
h_m=H_m(1),
J_m=mH_m(1)+H′_m(1),
K_m=m(m−1)H_m(1)+2mH′_m(1)+H″_m(1).
Set η=h_{n+1} and
S=J_{n+1}²−ηK_{n+1},
C=(J_{n+1}−η)J_n−(K_{n+1}−J_{n+1})h_n,
W=J_{n+1}J_n−K_{n+1}h_n.
The scalar C in these formulas is distinct from the polynomial C_raw. Define the COMPLETE endpoint contractions
D=kbC−2aS,
X=2P*S−kU*C−2fηW.
The cited exact endpoint identities are
B_raw(1)=C_raw(1)=γD,  A_raw(1)=γX,
γ=gf/(Gk)=(−1)^n/[4(n+1)^3(n!)^4].

The claims are:

(1) D is a ternary unit, and X/f is a ternary unit congruent to 2 modulo 3. Consequently D and both raw endpoints are nonzero, and the positive reduced denominator q_n of A_raw(1)/B_raw(1)=X/D satisfies
v_3(q_n)=2r=n−s_3(n),
where s_3(n) is the sum of the base-3 digits of n.

(2) The raw coefficient contents satisfy
c_3(B_raw)=−4r,
c_3(C_raw)≥−6r,
c_3(A_raw)≥−6r−L.
For ν=min(c_3(A_raw),c_3(B_raw),c_3(C_raw)), one has
−6r−L≤ν≤−6r.
Thus the full coefficient loss relative to B_raw lies between 2r and 2r+L.

(3) For any common rational scaling to a primitive integral full triple (A_0,B_0,C_0), put c=−6r−ν. Then c is an integer with 0≤c≤L and
v_3(A_0(1))=c,
v_3(B_0(1))=2r+c,
v_3(gcd(A_0(1),B_0(1)))=c.
This does not assert c=0.

Proof of (1). The published corrected ternary certificate supplies the following coefficientwise derivative consequences for every integer n divisible by 3:
(h_n,J_n,η,J_{n+1},K_{n+1})≡(1,0,0,1,2) mod 3.
Therefore S≡1, C≡2, W≡1, and k≡1.

Let A_m=L_m(1). Its integral generating series A(z)=Σ_{m≥0}A_mz^m satisfies
(1−4z−4z²)A(z)²=1.
Reducing modulo 3 and multiplying by A(z) gives
A(z)=(1+2z+2z²)A(z³).
Thus A_{3m}≡A_m, A_{3m+1}≡2A_m, and A_{3m+2}≡2A_m. Starting with A_0=1 proves that every A_m is a ternary unit. Since 3|n, b≡2a. Hence
D≡2b−2a≡2a≠0 mod 3.

It remains to estimate the actual numerator, including its partial-exponential contractions. Write
(2t²−2t+1)^m=Σ_j u_{m,j}t^j.
Rodrigues’ formula gives
[t^d]L_m(t)=(m+d)!u_{m,m+d}/(m!d!).
Set e_j=j!E_j. These integers satisfy e_0=1 and e_j=j e_{j−1}+1. Consequently e_{3j}≡1 and e_{3j+1}≡e_{3j+2}≡2 mod 3.

Direct substitution gives the exact expressions
T_0(P)/f=2^(−n)Σ_{d=0}^n(n!/d!)u_{n,n+d}e_{n+d},
T_0(U)/f=[2^n(n+1)]^(−1)Σ_{d=0}^{n+1}(n!/d!)(n+1+d)u_{n+1,n+1+d}e_{n+d}.
Every d<n summand vanishes modulo 3, since n!/d! contains n. In the first expression the d=n summand equals e_{2n}, because u_{n,2n}=2^n. Therefore T_0(P)/f≡1.

In the second expression the remaining coefficients are
u_{n+1,2n+1}=−(n+1)2^(n+1),
u_{n+1,2n+2}=2^(n+1),
where the displayed ν symbols denote the same coefficients u, not coefficient content. Equivalently, using u throughout,
u_{n+1,2n+1}=u_{n+1,2n+1}, and ν_{n+1,2n+2}=u_{n+1,2n+2}.
Their contributions give
T_0(U)/f=−2(2n+1)e_{2n}+[4/(n+1)]e_{2n+1} modulo 3,
so T_0(U)/f≡−2+8≡0. All divisions by n+1 are ternary-unit divisions.

The quotients defining w_P,w_U have integral coefficients and degree at most n. The moment formula gives v(μ_j)≥−v(j+1). Among j+1≤n+1 the possible loss is at most L, because n+1 is a ternary unit. Hence v(w_P),v(w_U)≥−L. Also L≤r: n! contains the factor 3^L. Thus
v(w_P/f),v(w_U/f)≥2r−L≥1.
It follows that P*/f≡1 and U*/f≡0. The COMPLETE normalized numerator therefore satisfies
X/f=2(P*/f)S−k(U*/f)C−2ηW≡2 mod 3.
Consequently v(X)=−2r. Since v(D)=0, reduction of the rational number X/D gives v(q_n)=max(0,v(D)−v(X))=2r. Legendre’s formula gives 2v_3(n!)=n−s_3(n).

This proves actual contraction valuations. Cancellation of γ alone would not prove them. Since v(γ)=−4r, it also proves
v(A_raw(1))=−6r,
v(B_raw(1))=−4r.

Proof of (2). First, T_j(P)/f and T_j(U)/f are ternary integral for all j=0,1,2. Indeed their summands, after introducing e_{n+d−j}, have the form
2^(−n)·[(n!)²/(m!d!)]·[(m+d)!/(n+d−j)!]·u_{m,m+d}e_{n+d−j},
where m=n or n+1 and 0≤d≤m. The second factorial quotient is integral. The first bracket is ternary integral: for m=n it is n!/d!, while for m=n+1 the only additional denominators are powers of the unit n+1.

G is a ternary unit. Hence every t_j has valuation at least −2r. The exact factorial-transform identity gives
(α_0,α_1,α_2)=g(η,J_{n+1},K_{n+1}),
and v(g)=−2r. Both cross-product rows therefore have coefficient valuations at least −2r, so every β_j has valuation at least −4r. Since their sum B_raw(1) has valuation exactly −4r, c_3(B_raw)=−4r.

The kernel itself has no odd-prime denominators. Orthogonality gives
K_n(t,s)=Σ_{m=0}^n(−1)^m(2m+1)L_m(t)L_m(s)/2^(2m+1)∈Z[1/2][t,s].
The relevant denominator loss arises when applying ℓ_j. A sharper bound than the maximum individual factorial denominator follows from the Christoffel–Darboux expression
K_n(t,s)=[P(t)ΔU(t,s)−U(t)ΔP(t,s)]/G,
where ΔQ(t,s)=(Q(t)−Q(s))/(t−s).

A term of ΔL_m is [t^d]L_m times t^(d−1−e)s^e, with m=n or n+1 and 0≤e<d≤m. Applying ℓ_j to s^e and multiplying by (n!)² gives the scalar
[(n!)²/(m!d!)]·[(m+d)!/(n+e+1−j)!]·u_{m,m+d}.
The second quotient is integral because n+e+1−j≤m+d. The first bracket is ternary integral by the same argument as above. Since P,U have integral coefficients and G is a ternary unit, every coefficient of (n!)²ℓ_j^sK_n(t,s) is ternary integral.

Thus the projection B_raw↦Q_raw loses at most 2r in coefficient valuation. The established β bound gives c_3(C_raw)=c_3(Q_raw)≥−6r.

Finally, through degree n, the exponential coefficients lose at most r, while the coefficients of F lose at most L. Therefore the coefficients of B_raw e^z through degree n have valuation at least −5r, and those of C_raw F have valuation at least −6r−L. By the defining Taylor reconstruction, c_3(A_raw)≥−6r−L. These inequalities give ν≥−6r−L. Conversely, v(A_raw(1))=−6r forces ν≤−6r. This proves (2).

Proof of (3). A common rational scalar λ making the full triple primitive integral satisfies v(λ)=−ν. The already established raw endpoint valuations therefore become −6r−ν=c and −4r−ν=2r+c. Their minimum is c. This proves the primitive gcd formula and bounds. In particular c_3(B_raw)−ν=2r+c, quantifying the failure of the large-prime coefficient-content equality on this progression.

Dependencies and scope. The rational endpoint reconstruction and common scaling are used exactly as stated in work/astra_review_registry/verified/b2-two-chart-actual-denominator-identities.md, payload ace0c8602da8ebb959a140d0a8e4dd9caf532014dc653f5328e909389ca4280d. Original definitions are in work/session_20260913/hp_b2_contiguous_endpoint_arithmetic.md and work/session_20260913/hp_b2_endpoint_attempt.md. The derivative congruences are taken from work/astra_review_registry/verified/b2-ternary-zero-diredacted_historical_name.md, payload 627b84db31ceb70a32d19d4ed78056281b5ae9e2bcc79510cfc396a8bc76364c. Its corrected matrix is not being re-audited here.

The published auxiliary result v_3(Ω_n)=0 is not an endpoint-gcd transfer theorem at p=3. This proof uses its derivative congruences together with additional Legendre and partial-exponential calculations. The resulting primitive gcd bound is c≤L, not c=0. The common normalization cancels from the ratio, but the essential new input is the proved unit congruence X/f≡2 and the independent unit calculation for D.

Author evidence is preserved in work/astra_20260929/worker_4/note_000040.md and note_000041.md. Exact author computations at n=3,6,9,12 checked the reconstructed order conditions, endpoint scaling, and the stated bounds. These finite checks are supporting evidence only. The n=12 primitive gcd valuation reported as 1 awaits the separately assigned independent reconstruction; no finite-example assertion is needed for the general proof above.

Self-audit and unresolved limits. The hypothesis 3|n is essential to the unit n+1, the endpoint residues, and the partial-exponential reductions. All factorial indices are nonnegative for n≥3. D≠0 and nonzero raw B are proved rather than assumed. The full coefficient content is retained throughout. No bound for other prime factors of q_n, exact general formula for c, full-denominator growth estimate, or irrationality theorem is asserted. Independent review remains outstanding.