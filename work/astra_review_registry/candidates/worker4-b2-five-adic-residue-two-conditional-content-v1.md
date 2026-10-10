> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Conditional five-adic coefficient content and primitive endpoint gcd bound on the residue-two progression

Status: UNVERIFIED CANDIDATE
Author: worker_4
Content SHA256: 2c26bae0fb61072731e91f2bcb1cbca24f0ad4281c0323753d425900c5986932

UNVERIFIED CANDIDATE. Author: worker_4. Independent review is required. This claim supplies coefficient bounds and a conditional primitive endpoint-gcd bound; it makes no assertion about the rationality of e+pi.

Definitions and statement.

Fix an integer n≥7 with n≡2 modulo five. Write v=v_5, r=v(n!), L=floor(log_5 n), and v(0)=+∞. For a rational polynomial V, let c_5(V) be the minimum valuation of its coefficients, with c_5(0)=+∞.

Define
L_m(t)=(1/m!)(d/dt)^m(2t²−2t+1)^m,
P=L_n, U=L_{n+1}, a=P(1), b=U(1),
f=2^n/(n!)², G=(−1)^n2^(2n+3)/(n+1).
Both P and U have integer coefficients, and G is a five-adic unit.

For j=0,1,2 put
ℓ_j(t^d)=1/(n+d+1−j)!,
E_h=Σ_{k=0}^h1/k!,
T_j(V)=Σ_d[t^d]V(t)E_{n+d−j},
α_j=ℓ_j(U),
t_j=(aT_j(U)−bT_j(P))/G.
All factorial indices used here are nonnegative. Define
β=(α_0,α_1,α_2)×(1+t_0,1+t_1,1+t_2),
B_raw(z)=Σ_{j=0}^2β_jz^j,
K_n(t,s)=[U(t)P(s)−P(t)U(s)]/[G(t−s)],
Q_raw(t)=−Σ_{j=0}^2β_jℓ_j^sK_n(t,s),
C_raw(z)=z^nQ_raw(1/z).
The antisymmetric numerator makes K_n a polynomial of degree at most n in each variable, so C_raw is a polynomial.

Let
μ_h=((1+i)^(h+1)−(1−i)^(h+1))/(i·2^h(h+1)),
F(z)=Σ_{k≥1}μ_{k−1}z^k,
A_raw(z)=−[B_raw(z)e^z+C_raw(z)F(z)]_{≤n}.
These are the specified rational reconstruction formulas used in the published endpoint work.

Unconditionally for these definitions,
c_5(B_raw)≥−4r,
c_5(C_raw)≥−6r,
c_5(A_raw)≥−6r−L.
Consequently, for ν=min(c_5(A_raw),c_5(B_raw),c_5(C_raw)), one has ν≥−6r−L.

Assume additionally the explicit endpoint hypotheses
(H) v(A_raw(1))=−6r and v(B_raw(1))=−4r.
Then
c_5(B_raw)=−4r,
−6r−L≤ν≤−6r.
For any common rational scalar λ making the entire triple (A_0,B_0,C_0)=λ(A_raw,B_raw,C_raw) primitive integral, define c=−6r−ν. Then
0≤c≤L,
v(A_0(1))=c,
v(B_0(1))=2r+c,
v(gcd(A_0(1),B_0(1)))=c.
Thus primitive endpoint cancellation at five is at most floor(log_5 n), while the coefficient-content loss relative to B_raw is exactly 2r+c.

Proof of the unconditional bounds.

Write u_{m,h}=[t^h](1−2t+2t²)^m. Rodrigues’ formula gives
[t^d]L_m(t)=(m+d)!u_{m,m+d}/(m!d!).
In particular its coefficients are integers.

For m∈{n,n+1} and 0≤d≤m, put M_{m,d}=(n!)²/(m!d!). This is five-adically integral. Indeed, for m=n it equals n!/d!; for m=n+1 and d≤n it equals n!/((n+1)d!); and for m=n+1,d=n+1 it equals 1/(n+1)². The only additional denominator is a power of the unit n+1. This includes the boundary d=n+1 explicitly.

The factorial-functional row can be bounded directly:
(n!)²α_j=Σ_{d=0}^{n+1}M_{n+1,d}[(n+1+d)!/(n+d+1−j)!]u_{n+1,n+1+d}.
The second factorial quotient is integral for j=0,1,2. Therefore v(α_j)≥−2r. No auxiliary derivative congruence is needed for this step.

Set e_h=h!E_h, an integer. For m=n or n+1, direct substitution gives
T_j(L_m)/f=2^(−n)Σ_{d=0}^m M_{m,d}[(m+d)!/(n+d−j)!]u_{m,m+d}e_{n+d−j}.
Every summand is five-adically integral: the factorial quotient is integral because m≥n and j≥0, and M_{m,d} was treated above. Hence v(T_j(P)),v(T_j(U))≥−2r. Since a,b are integers and G is a unit, v(t_j)≥−2r. Also r≥0, so v(1+t_j)≥−2r. Each coordinate of the cross product β is a difference of products whose valuations are at least −4r. This proves c_5(B_raw)≥−4r.

To estimate the kernel projection, write ΔV(t,s)=(V(t)−V(s))/(t−s). The exact identity
K_n(t,s)=[P(t)ΔU(t,s)−U(t)ΔP(t,s)]/G
follows by expansion.

A term of ΔL_m has coefficient [t^d]L_m and monomial t^(d−1−e)s^e, where 0≤e<d≤m. Applying ℓ_j to its s-variable and multiplying by (n!)² gives
M_{m,d}[(m+d)!/(n+e+1−j)!]u_{m,m+d}.
The second quotient is integral because n+e+1−j≤m+d. The first factor is five-adically integral by the preceding cases. Since P,U have integral coefficients and G is a unit, every coefficient of (n!)²ℓ_j^sK_n belongs to Z_5. Thus c_5(ℓ_j^sK_n)≥−2r. Multiplication by β_j and summation prove c_5(Q_raw)≥−6r. Reversing its coefficients preserves their minimum valuation, giving c_5(C_raw)≥−6r.

Finally, the coefficients of e^z through degree n have valuations at least −r. The numerator defining μ_h, after division by i, is an integer; powers of two are units at five. Therefore v(μ_h)≥−v(h+1). The coefficients of F through degree n consequently have valuations at least −L. It follows that the coefficients through degree n of B_raw e^z have valuations at least −5r, and those of C_raw F have valuations at least −6r−L. Taylor truncation and subtraction preserve the smaller lower bound. Since −6r−L≤−5r, this proves c_5(A_raw)≥−6r−L and hence ν≥−6r−L.

Proof under the endpoint hypotheses.

Evaluation at one cannot have valuation below the minimum coefficient valuation. Hypothesis (H), together with c_5(B_raw)≥−4r, therefore forces c_5(B_raw)=−4r. The other endpoint in (H) gives ν≤c_5(A_raw)≤−6r. Combining this with the unconditional lower bound yields −6r−L≤ν≤−6r.

The hypotheses ensure that the triple is nonzero. For a common scaling λ to a primitive integral full triple, the minimum coefficient valuation at five is zero, so v(λ)=−ν. The endpoint valuations become −6r−ν=c and −4r−ν=2r+c. Their minimum is c, which is the valuation of their integer gcd. The bounds on ν give 0≤c≤L. This proves every conditional assertion.

Dependencies, evidence, and verification status.

The displayed reconstruction is the one in work/astra_review_registry/verified/b2-ternary-endpoint-denominator-and-content-v1.md, payload SHA-256 6baaa17575ed30467e01de61e4c861e97987c07a31f331cc6821f2b850f05dfe. Its exact rational endpoint identification is supplied by work/astra_review_registry/verified/b2-two-chart-actual-denominator-identities.md, payload SHA-256 ace0c8602da8ebb959a140d0a8e4dd9caf532014dc653f5328e909389ca4280d. The coefficient estimates above are rederived at five; no ternary congruence or large-prime content theorem is imported.

The intended endpoint hypotheses (H) are asserted in the separate, currently unapproved candidate work/astra_review_registry/candidates/worker4-b2-five-adic-residue-two-exact-denominator-v1.md, payload SHA-256 bd96cc2e3fcd4f97c84f74f4c4967a0c79dbae9337bb055a00c6ab693e682c86. That candidate uses the common raw endpoint scale γ=(−1)^n/[4(n+1)^3(n!)^4]. Its independent approval remains outstanding. The present conditional theorem treats (H) as hypotheses and does not approve their application.

The initial supplementary derivation is preserved in work/astra_20260929/worker_4/note_000096.md. Earlier endpoint reconstructions at n=7,12,27 are preserved in work/astra_20260929/worker_4/note_000085.md. Those finite computations concern the endpoint candidate; they are not premises of this coefficient proof or independent verification of it. No additional reconstruction or index scan was performed for this extension.

Self-audit and unresolved limits.

Every factorial index is nonnegative, the d=n+1 boundary has been retained, and all divisions involving n+1 are unit divisions. No division by n−2 occurs. The unconditional bounds do not require endpoint nonvanishing; the conditional conclusions explicitly require (H). The claim gives a bounded interval for ν and the primitive gcd valuation, not an exact value of either. Independent review is required before publication. No full-denominator estimate or irrationality result follows.