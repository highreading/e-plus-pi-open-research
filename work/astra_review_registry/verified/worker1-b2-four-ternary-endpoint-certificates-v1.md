> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent exact endpoint reconstruction at n=3,6,9,12 and primitive normalization at n=12

Status: Independently reviewed research result (AI review; not formal verification)
Author: worker_1
Reviewer: worker_4
Content SHA256: 52ab9bfa20ec804c2701c0c3adbee0c980eeda0a2f3db474b2c1183e912b7bed
Review: work/astra_review_registry/reviews/worker1-b2-four-ternary-endpoint-certificates-v1-worker_4.md

Verification status: author-checked finite exact-computation claim, submitted for independent review. No assertion about all multiples of three or irrationality of e+pi is included.

1. Definitions and independent approximation system

Write v3 for the rational 3-adic valuation, with v3(3)=1. Define rational moments
mu_d = 2^(1-d) sum_{0<=j<=d, j even} binom(d,j)(-1)^(j/2)/(j+1),
and the formal series F(z)=sum_{d>=0} mu_d z^(d+1). For each n in {3,6,9,12}, seek rational polynomials A,B,C satisfying
 deg A<=n, deg B<=2, deg C<=n,
 A(z)+B(z)e^z+C(z)F(z)=O(z^(2n+3)),
 B(1)=C(1)=1.

Here is an explicit square rational system determining B and C. Put e_k=1/k! for k>=0 and e_k=0 otherwise; put f_k=mu_(k-1) for k>=1 and f_k=0 otherwise. With B(z)=sum_{j=0}^2 b_j z^j and C(z)=sum_{j=0}^n c_j z^j, impose
 sum_j b_j e_(d-j)+sum_j c_j f_(d-j)=0 for d=n+1,...,2n+2,
 sum_j b_j=1, sum_j c_j=1.
These are n+4 equations in n+4 unknowns. Set
 A_d=-sum_j b_j e_(d-j)-sum_j c_j f_(d-j), 0<=d<=n.
For all four specified indices, exact rational elimination found a pivot in every column, checked the solution against the original equations, and checked every residual coefficient through degree 2n+2. Thus the normalized triple exists uniquely at these four indices. This construction uses no endpoint determinant formula.

2. Independently reconstructed complete endpoint pair

Define integer polynomials L_0(t)=1, L_1(t)=4t-2 and
 (m+1)L_(m+1)(t)=(2m+1)(4t-2)L_m(t)+4mL_(m-1)(t).
Let ell be the linear functional ell(t^d)=mu_d. For P=L_n and U=L_(n+1), put
 a=P(1), b=U(1),
 w_P=ell((P(t)-P(1))/(t-1)), w_U=ell((U(t)-U(1))/(t-1)).
Let E_r=sum_{k=0}^r 1/k! and T_n(Q)=sum_d Q_d E_(n+d), where Q_d is the coefficient of t^d in Q.

Define H_m(x) by the finite coefficient formula
 H_m(x)=(m!/2^m) sum_{r=0}^m ([t^(m-r)](t^2-2t+2)^m) x^r/r!.
Write h_m,J_m,K_m,M_m for the derivatives of orders 0,1,2,3 of x^m H_m(x), evaluated at x=1. Set
 eta=h_(n+1),
 S=J_(n+1)^2-eta K_(n+1),
 Cstar=(J_(n+1)-eta)J_n-(K_(n+1)-J_(n+1))h_n,
 W=J_(n+1)J_n-K_(n+1)h_n,
 k=(n+1)^2, f=2^n/(n!)^2.
The source's scaled pair is
 D=k b Cstar-2a S,
 X=2(w_P+T_n(P))S-k(w_U+T_n(U))Cstar-2f eta W.
All THREE displayed terms of X were retained in the executed calculation.

For every n in {3,6,9,12}, X and D are nonzero and the independently solved system in section 1 satisfies A(1)=X/D. With q the positive denominator of X/D in lowest terms, the exact results are:

 n | v3(X) | v3(D) | v3(q)
 3 | -2 | 0 | 2
 6 | -4 | 0 | 4
 9 | -8 | 0 | 8
12 | -10 | 0 | 10

The rational identity v3(q)=max(0,v3(D)-v3(X)) was checked directly. In addition, with Lambda=2^(n+1)(2n+2)!(n!)^2, both Lambda X and Lambda D are integers, and integer gcd reduction produced the same q. The calculation checked the exact Wronskian
 a w_U-b w_P=(-1)^n 2^(2n+3)/(n+1)
and the Rodrigues-transform coefficient identities used in reconstruction. It also evaluated the original endpoint cross-product determinants separately and checked both their common scaling factor and their ratio.

3. Full coefficient normalization at n=12

For the uniquely normalized rational triple in section 1, the least common multiple of ALL coefficient denominators is
 L=36403805741687347841562731899445831419791586099200000.
Multiplication by L gives an integer polynomial triple whose entire coefficient vector has gcd 1. Choose this primitive triple with positive B(1). Its endpoints are
 A_primitive(1)=-213321732297551284888756637809663458680168482090637760,
 B_primitive(1)=C_primitive(1)=L.
Their endpoint gcd is exactly
 gcd(|A_primitive(1)|,B_primitive(1))=73920=2^6*3*5*7*11.
Consequently the reduced fraction is
 X/D=-2885845945583756559642270533139386616344270591053 / 492475727024991177510318342795533433709301760000.

In particular,
 v3(L)=11,
 v3(A_primitive(1))=1,
 v3(B_primitive(1))=11,
 v3(q)=10.
The minimum valuation among the coefficients of the normalized rational triple is -11. This follows also from the computed lcm and primitive coefficient gcd: at least one coefficient of the primitive integer triple is a 3-adic unit.

To specify the raw normalization unambiguously, let G=(-1)^n 2^(2n+3)/(n+1), g=2^(n+1)/((n+1)!)^2, alpha=gf/(G(n+1)^2), and define the raw triple as alpha D times the normalized triple. This is the scaling checked against the endpoint cross-product construction; its endpoints are alpha X and alpha D. At n=12, v3(alpha D)=-20, so its minimum coefficient valuation is -31. Primitive normalization therefore changes its B endpoint valuation from -20 to 11. The raw coefficient valuation, primitive endpoint valuation, endpoint gcd valuation, and reduced-denominator valuation are different quantities.

4. Auxiliary minors and precise scope

Define the auxiliary matrix with rows
 (h_n,J_n), (J_(n+1),K_(n+1)), (K_(n+2),M_(n+2)),
and let Omega_n be the positive gcd of its three ordered maximal minors. At each of the four tested indices, the matrix reduces modulo 3 to
 [[1,0],[1,2],[2,0]],
and its ordered minors reduce to (2,0,2). At n=12 the exact gcd is Omega_12=2.

Thus these finite examples demonstrate that an auxiliary unit minor can coexist with a reduced endpoint denominator divisible by 3. At n=12 it also coexists with a primitive endpoint gcd divisible by 3. This does not contradict the original endpoint-gcd theorem or the published local-chart theorem: their large-prime hypotheses exclude p=3 here. The elementary rational denominator identity used above has no such restriction.

These computations prove only the specified finite identities, subject to independent verification of the certificates. They do not establish a formula for arbitrary n divisible by 3, a denominator-growth estimate, a shrinking sequence of nonzero integer linear forms, or irrationality of e+pi.

5. Reproducible evidence and dependencies

The full exact reconstruction and independent-system implementation is work/astra_20260929/worker_1/calculation_000061.py, SHA-256 23a70be94192346b554bdd6f5606d155e7e0ddb34aeb17e2be651891334386d3. It uses Python Fraction arithmetic, prints the exact fractions and individual numerator terms, and asserts all checks described in sections 1–2 and the finite auxiliary residues. Its successful execution was reported at worker_1 step 62.

The full coefficient-content, primitive endpoint gcd, and raw-scaling calculation is work/astra_20260929/worker_1/calculation_000063.py, SHA-256 fca29b8c2e462cde7bb185679a0d082601c3f8fbfe60d3abeedd65377181e8a0. Its successful execution was reported at step 64. The exact normalization results are preserved in work/astra_20260929/worker_1/note_000064.md, SHA-256 dc5188332deea7da39f0526fea6731d94ed9bfd6a0e84472843a14861499a183.

Source definitions were checked against work/session_20260913/hp_b2_contiguous_endpoint_arithmetic.md and work/astra_review_registry/verified/b2-two-chart-actual-denominator-identities.md. Their general large-prime valuation conclusions are not invoked at p=3. Independent review of this new finite claim remains outstanding.