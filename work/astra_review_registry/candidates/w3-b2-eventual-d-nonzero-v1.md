> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact identification of the two-chart denominator with the matched b=2 endpoint and eventual nonvanishing

Status: UNVERIFIED CANDIDATE
Author: worker_3
Content SHA256: 66273b26045bf283eff8b3b503e2c51141e05c2c3f0bf128a8412e1fdec6817f

Status: UNVERIFIED submission by worker_3 for independent review.

STATEMENT.
For n≥2, use the exact endpoint definitions in the published record b2-two-chart-actual-denominator-identities. Let P=L_n and U=L_{n+1}, where L_m(t)=2^m i^m P_m(−i(2t−1)) and P_m is the ordinary Legendre polynomial. Set a=P(1), b=U(1), and k=(n+1)^2. Here b denotes an endpoint value; the exponential degree throughout this claim is fixed at 2.

Define H_m(x)=m![s^m]e^{xs}(1−s+s^2/2)^m, h_m=H_m(1), J_m=mh_m+H'_m(1), and K_m=m(m−1)h_m+2mH'_m(1)+H''_m(1). Put
S=J_{n+1}^2−h_{n+1}K_{n+1},
C=(J_{n+1}−h_{n+1})J_n−(K_{n+1}−J_{n+1})h_n,
D=kbC−2aS.

Let Y_cof be the endpoint of the signed maximal-cofactor solution used in the published matched-family theorem, specialized to exponential degree 2 and the SAME index n. Then the exact identity is

Y_cof=α_n D/d_{n+1},
α_n=(−1)^n/[4(n+1)^3(n!)^4],
d_{n+1}=2^{n+1}binom(2n+2,n+1).

Both scalars are nonzero. Consequently the published matched endpoint theorem, together with its published factorial-determinant dependency, implies D≠0 for all sufficiently large n. No effective threshold or all-index assertion is made.

PROOF OF THE FAMILY IDENTIFICATION.
Use the common moment functional ℒ(Q)=∫_{−1}^1Q((1+iu)/2)du. Write d_m=2^m binom(2m,m), so the monic polynomials in the matched theorem are exactly p_m=L_m/d_m. Define its reproducing kernel V_n(t)=Σ_{m=0}^n p_m(t)p_m(1)/ℒ(p_m^2). Christoffel–Darboux in the L normalization gives

V_n(t)=[bP(t)−aU(t)]/[G(1−t)],
G=(−1)^n2^{2n+3}/(n+1).

For j=0,1,2 let ℓ_j(t^r)=1/(n+r+1−j)!, E_m=Σ_{v=0}^m1/v!, and T_j(Q)=Σ_r[t^r]Q(t)E_{n+r−j}. All factorial and E indices here are nonnegative. Absolute convergence of the factorial series gives

ℓ_j(Q/(1−t))=eQ(1)−T_j(Q).

Therefore

ℓ_j(V_n)=[aT_j(U)−bT_j(P)]/G=t_j,

exactly the t_j in the two-chart reconstruction. The two terms containing e cancel. Thus this comparison is an exact rational identity, not an asymptotic approximation.

Set u=(ℓ_0(p_{n+1}),ℓ_1(p_{n+1}),ℓ_2(p_{n+1})), v=(ℓ_0(V_n),ℓ_1(V_n),ℓ_2(V_n)), and e_vec=(1,1,1). The b=2 reduced matrix in the matched theorem has rows u and e_vec+v. With its stated sign convention, the coefficient vector B_cof is u×(e_vec+v), since B_cof·z=det[u;e_vec+v;z].

The raw vector in the two-chart record is β=(a_0,a_1,a_2)×(e_vec+t), where a_j=ℓ_j(U). We have a_j=d_{n+1}u_j and t=v, hence

β=d_{n+1}B_cof,
Y_raw=Σ_jβ_j=d_{n+1}Y_cof.

The common moment projection reconstructs C linearly from B, and Taylor truncation reconstructs A linearly under the convention R=A+Be^z+CF. Therefore the complete raw triple is also d_{n+1} times the matched cofactor triple. Both constructions have degree caps (n,2,n), order requirement O(z^{2n+3}), and matching B(1)=C(1). The auxiliary appearance of n+1 agrees with the single high row p_{n+1}; it introduces no index shift.

INDEPENDENT ENDPOINT-SCALAR EXPANSION.
Let r_j=ℓ_j(P), f=2^n/(n!)^2, and g=2^{n+1}/((n+1)!)^2=2f/k. The Rodrigues identity recorded in the two-chart source gives

(r_1,r_2)=f(h_n,J_n),
(a_0,a_1,a_2)=g(h_{n+1},J_{n+1},K_{n+1}).

Put S_scr=a_1^2−a_0a_2 and C_scr=(a_1−a_0)r_2−(a_2−a_1)r_1. Then S_scr=g^2S and C_scr=gfC.

For an explicit check of orientation, expand the endpoint of β:

Y_raw=(a_2−a_1)t_0+(a_0−a_2)t_1+(a_1−a_0)t_2
=(a_2−a_1)(t_0−t_1)+(a_0−a_1)(t_1−t_2).

Since T_0(Q)−T_1(Q)=ℓ_1(Q) and T_1(Q)−T_2(Q)=ℓ_2(Q), we have

t_0−t_1=(aa_1−br_1)/G,
t_1−t_2=(aa_2−br_2)/G.

Substitution yields

Y_raw=(bC_scr−aS_scr)/G
=[gf/(Gk)](kbC−2aS)=α_nD.

Finally gf/(Gk)=(−1)^n/[4(n+1)^3(n!)^4], proving the asserted exact scalar and its nonvanishing over Q. No p-adic unit assumption is used in this identification.

EVENTUAL NONVANISHING AND NUMERATOR CONVENTION.
The published matched-family theorem, with its separately published factorial-determinant hypothesis discharged, establishes Y_cof≠0 for every sufficiently large n at fixed exponential degree 2. The exact identity just proved transfers this assertion to D. This uses neither the pending leading-cofactor refinement nor any ternary congruence.

For the X defined in the two-chart record, its published exact reconstruction gives A_raw(1)=α_nX alongside B_raw(1)=α_nD. Hence the rational approximant to e+π is −A_raw(1)/B_raw(1)=−X/D under R=A+Be^z+CF. Its positive reduced denominator equals that of X/D. Changing consistently to R=Be^z+CF−A changes A’s sign and preserves this approximant and its signed error. No primitiveness normalization is required.

SOURCE DEPENDENCIES.
1. work/astra_review_registry/verified/b2-two-chart-actual-denominator-identities.md, payload ace0c8602da8ebb959a140d0a8e4dd9caf532014dc653f5328e909389ca4280d: exact L normalization, kernel constant, Rodrigues transforms, and numerator reconstruction. Read completely in the current ledger. The endpoint-scalar expansion and comparison of the two reduced matrices are explicitly checked above.
2. work/astra_review_registry/verified/worker3-fixed-b-matched-endpoint-transfer-conditional-v1.md, payload 48ed273001a125bce2ec58f5ce053cf10340c71cd64373fde3fc356852bc6601: exact projection/cofactor convention and eventual endpoint nonvanishing conditional on FD. Read completely.
3. work/astra_review_registry/verified/fixed-size-factorial-determinant-finite-jet-factorization-v1.md, payload 6eecc758557e4295ac85093753ee77245492520ce6c0cc0539bc68886a0732f3: the published FD dependency. Read completely. Its application hypotheses are supplied by dependency 2.

SCOPE AND SELF-AUDIT.
This is a new source-identification argument awaiting independent review. Its proof uses exact algebra and published analytic results; no numerical check is presented as proof. Eventual nonvanishing does not imply nonvanishing at every index. No exact ternary valuation, residue-one numerator congruence, denominator growth estimate, growing-degree uniformity, or conclusion about the rationality of e+π is certified.