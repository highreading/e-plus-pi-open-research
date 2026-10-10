> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact five-adic reduced-denominator valuation for the b=2 endpoint pair when five divides the index

Status: Independently reviewed research result (AI review; not formal verification)
Author: worker_4
Reviewer: worker_1
Content SHA256: 01a6d34706170e9b0b193c720e8ef0827f198102e1feba308852028cdeb51b81
Review: work/astra_review_registry/reviews/b2-five-adic-endpoint-denominator-v1-worker_1.md

UNVERIFIED CANDIDATE. Author: worker_4. Independent review is required. This claim concerns the actual rational endpoint pair at one prime on one progression.

STATEMENT AND DEFINITIONS

Fix an integer n≥5 divisible by 5. Write v=v_5, r=v(n!), L=floor(log_5 n), and v(0)=+∞. Define the rational moment functional ℒ by
ℒ(t^j)=μ_j=((1+i)^(j+1)−(1−i)^(j+1))/(i·2^j(j+1)).
Thus F(z)=4 arctan(z/(2−z))=Σ_{j≥1}μ_{j−1}z^j. Define
L_m(t)=(1/m!)(d/dt)^m(2t²−2t+1)^m,
P=L_n, U=L_{n+1}, a=P(1), b=U(1), k=(n+1)²,
f=2^n/(n!)², g=2f/k, G=(−1)^n2^(2n+3)/(n+1).
The polynomials L_m have integral coefficients.

For j=0,1,2 put
ℓ_j(t^d)=1/(n+d+1−j)!,
E_m=Σ_{h=0}^m1/h!,
T_j(Q)=Σ_d[t^d]Q(t)E_{n+d−j}.
All indices occurring here are nonnegative. Set
w_P=ℒ((P(t)−a)/(t−1)), w_U=ℒ((U(t)−b)/(t−1)),
P*=w_P+T_0(P), U*=w_U+T_0(U).

To specify the raw normalization completely, let
α_j=ℓ_j(U), τ_j=(aT_j(U)−bT_j(P))/G,
(β_0,β_1,β_2)=(α_0,α_1,α_2)×(1+τ_0,1+τ_1,1+τ_2),
B_raw(z)=Σ_{j=0}^2β_jz^j.
Define
K_n(t,s)=[U(t)P(s)−P(t)U(s)]/[G(t−s)],
Q_raw(t)=−Σ_{j=0}^2β_jℓ_j^sK_n(t,s),
C_raw(z)=z^nQ_raw(1/z),
A_raw(z)=−[B_raw(z)e^z+C_raw(z)F(z)]_{≤n}.

For the endpoint contractions define
H_m(x)=m![s^m]e^(xs)(1−s+s²/2)^m,
h_m=H_m(1),
J_m=mh_m+H′_m(1),
K_m=m(m−1)h_m+2mH′_m(1)+H″_m(1),
η=h_{n+1},
S=J_{n+1}²−ηK_{n+1},
C=(J_{n+1}−η)J_n−(K_{n+1}−J_{n+1})h_n,
W=J_{n+1}J_n−K_{n+1}h_n.
Here the scalar C is distinct from C_raw, and K_m is distinct from the two-variable kernel. Put
D=kbC−2aS,
X=2P*S−kU*C−2fηW.

The published exact rational reconstruction identities give
B_raw(1)=C_raw(1)=γD, A_raw(1)=γX,
γ=gf/(Gk)=(−1)^n/[4(n+1)^3(n!)^4].
They also give the degree caps (n,2,n) and remainder order O(z^(2n+3)). Only their rational identities are used here, without a large-prime hypothesis.

The claimed conclusions are
v(D)=0, X/f≡3 mod 5, v(X)=−2r.
In particular both endpoints are nonzero. If q_n is the positive reduced denominator of A_raw(1)/B_raw(1)=X/D, then
v_5(q_n)=2v_5(n!)=(n−s_5(n))/2,
where s_5(n) is the base-5 digit sum. In the specified raw normalization,
v_5(A_raw(1))=−6r and v_5(B_raw(1))=−4r.
These endpoint valuations are not assertions about full polynomial coefficient content.

PROOF

1. Auxiliary derivative congruences on the entire index disk.

The falling-factorial interpolation of H_m^(j)(1) is
𝓗_j(X)=Σ_{u,v≥0}(−1)^u (X)_(u+2v+j)(X)_(u+v)/(2^v u!v!),
where (X)_a=X(X−1)⋯(X−a+1), with (X)_0=1. At nonnegative integer X=m this equals H_m^(j)(1), by expanding the defining generating polynomial.

For completeness, on X=a+5Y every falling factorial of length M has coefficientwise valuation at least floor(M/5): among any M consecutive integer constants at least that many are divisible by 5, and their corresponding linear factors have every coefficient divisible by 5. Put h=floor((u+2v)/5) and ℓ=floor((u+v)/5). Since
v_5(u!v!)≤v_5((u+v)!)=ℓ+v_5(ℓ!),
the displayed summand has coefficientwise valuation at least
h−v_5(ℓ!)≥h−v_5(h!).
For h≥1 this is at least 1 and tends to infinity with h. Thus all terms with u+2v≥5 form a convergent sum in 5Z_5⟨Y⟩.

The retained terms have denominators prime to 5, so their reductions on X=a+5Y equal their values at a. At a=0 and a=1 they give, respectively,
(𝓗_0,𝓗_1,𝓗_2)≡(1,0,0), (0,1,0) mod 5.
Indeed every positive-length falling factorial at zero vanishes; at one, only the terms with relevant lengths at most one survive. Therefore, for 5|n,
(h_n,J_n,η,J_{n+1},K_{n+1})≡(1,0,0,1,2) mod 5.
Consequently
(S,C,W,k)≡(1,−1,−2,1) mod 5.
This calculation is coefficientwise on the auxiliary disks, rather than an inference from finitely many sampled indices.

2. Legendre endpoint units and the denominator contraction.

Write A_m=L_m(1) and A(z)=Σ_{m≥0}A_mz^m. Rodrigues’ formula gives
A_m=[x^m](1+2x+2x²)^m.
Summing its central coefficient formula yields
A(z)=(1−4z−4z²)^(−1/2).
For example, the coefficient formula is
A_m=Σ_{v=0}^{floor(m/2)} m!·2^(m−v)/(v!²(m−2v)!),
which also directly verifies the generating identity.

Let Q(z)=1−4z−4z². In F_5[[z]], Q(z)A(z)²=1 and Frobenius gives A(z)^5=A(z^5). Hence
A(z)=Q(z)²A(z^5)
=(1+2z+3z²+2z³+z⁴)A(z^5).
Thus A_{5m+d}≡c_dA_m for c=(1,2,3,2,1). All digit factors are nonzero, and A_0=1, so every A_m is a five-adic unit. If 5|n then b≡2a. Using the auxiliary residues,
D≡−b−2a≡a≠0 mod 5.
This proves v(D)=0 and D≠0. No analytic interpolation of the Legendre endpoints in the index is asserted or needed.

3. The complete numerator contraction.

Write (2t²−2t+1)^m=Σ_j u_{m,j}t^j. Rodrigues’ formula gives
[t^d]L_m(t)=(m+d)!u_{m,m+d}/(m!d!).
Set e_j=j!E_j. These integers satisfy e_0=1 and e_j=je_{j−1}+1, so
e_{5m}≡1 and e_{5m+1}≡2 mod 5.

Direct substitution into T_0 gives the exact expressions
T_0(P)/f=2^(−n)Σ_{d=0}^n(n!/d!)u_{n,n+d}e_{n+d},
T_0(U)/f=[2^n(n+1)]^(−1)Σ_{d=0}^{n+1}(n!/d!)(n+1+d)u_{n+1,n+1+d}e_{n+d}.
All terms are five-adically integral. In the second sum, the only factorial quotient with a denominator is at d=n+1, where it equals 1/(n+1), a unit.

Every term with d<n vanishes modulo 5 because n!/d! contains n. Since u_{n,2n}=2^n, the first expression reduces to e_{2n}≡1. The two surviving terms in the second expression use
u_{n+1,2n+1}=−(n+1)2^(n+1),
u_{n+1,2n+2}=2^(n+1),
where both symbols on the left are the coefficient u with the indicated subscripts. They yield
T_0(U)/f≡−2(2n+1)e_{2n}+[4/(n+1)]e_{2n+1}
≡−2+8≡1 mod 5.

The quotient polynomials defining w_P,w_U have integral coefficients and degree at most n. The moment formula implies v_5(μ_j)≥−v_5(j+1): its numerator after division by i is an integer and 2 is a five-adic unit. For 1≤j+1≤n+1, the possible loss is at most L, because n+1 is a unit. Thus
v_5(w_P),v_5(w_U)≥−L.
Since n≥5 and n! contains the factor 5^L, one has r≥L≥1. As v_5(f)=−2r,
v_5(w_P/f),v_5(w_U/f)≥2r−L≥1.
It follows that P*/f≡1 and U*/f≡1. Keeping every term of the numerator, including its correction, gives
X/f=2(P*/f)S−k(U*/f)C−2ηW
≡2+1=3 mod 5.
Hence X≠0 and v_5(X)=−2r.

4. Actual reduction and raw normalization.

For any nonzero rational X,D, the positive reduced denominator of X/D satisfies
v_5(q)=max(0,v_5(D)−v_5(X)).
This identity does not require X or D to be integral. Applying the proved contraction valuations gives v_5(q_n)=2r. Legendre’s factorial formula gives 2r=(n−s_5(n))/2.

Because 5∤4(n+1)^3, the specified γ has valuation −4r. Thus the raw endpoint valuations are −6r and −4r. Any common nonzero rational scaling, including primitive integral normalization of the full triple, cancels from the ratio. This cancellation alone would not establish the result: the separate unit calculations for D and X/f are essential.

DEPENDENCIES, EVIDENCE, AND SELF-AUDIT

The endpoint reconstruction and common scaling are the exact rational identities in work/astra_review_registry/verified/b2-two-chart-actual-denominator-identities.md, payload SHA-256 ace0c8602da8ebb959a140d0a8e4dd9caf532014dc653f5328e909389ca4280d. Original definitions appear in work/session_20260913/hp_b2_contiguous_endpoint_arithmetic.md and work/session_20260913/hp_b2_endpoint_attempt.md. The five-adic derivative, Legendre, and complete numerator arguments are supplied above; they are not consequences of the large-prime transfer theorem or the ternary unit-minor certificate.

Author derivation and exact finite evidence are preserved in work/astra_20260929/worker_4/note_000052.md and work/astra_20260929/worker_4/note_000053.md. The latter records the complete reduced endpoint ratios at n=5 and n=10. The author computations used rational moment reconstruction, checked the full order conditions through degrees 12 and 22 and the endpoint scaling, and obtained (v_5(D),v_5(X),v_5(q_n))=(0,−2,2) and (0,−4,4). Their raw full coefficient-content minima were −6 and −12, respectively. These finite calculations support the examples only and do not replace the general proof or independent review.

The hypothesis n≥5 with 5|n ensures positive factorial valuation, the unit n+1, and the stated factorial-sum reductions. Nonvanishing of D and X is proved. No general coefficient-content equality or primitive endpoint-gcd formula is asserted. No conclusion is claimed for other index disks, other prime factors of q_n, a shrinking sequence of integer linear forms, or the rationality of e+π.