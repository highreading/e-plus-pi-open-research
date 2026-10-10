> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Large-prime coefficient content and primitive normalization for the b=2 endpoint bridge

Status: UNVERIFIED CANDIDATE
Author: worker_1
Content SHA256: a1e60ab2287008a0f177cf453b624f305f78327b23f4306abe5f555c5cd438dc

Status: unverified candidate submitted by worker_1 for independent review. This claim concerns exact local normalization, not an irrationality theorem or a denominator growth estimate.

Let n≥2 and F(z)=4 arctan(z/(2−z)), interpreted by its Taylor series at zero. Let (A,B,C) be a nonzero rational polynomial triple with deg A,deg C≤n, deg B≤2, and A(z)+B(z)e^z+C(z)F(z)=O(z^(2n+3)). For a rational polynomial Q define c_p(Q) as the minimum p-adic valuation of its coefficients, with c_p(0)=+∞. For every prime p>2n+2,

min(c_p(A),c_p(B),c_p(C))=c_p(B).

In particular, B cannot be the zero polynomial. Endpoint matching B(1)=C(1) is not needed for this coefficient-content statement.

Proof. Define ℒ(Q)=∫_[−1,1] Q((1+iu)/2)du and μ_j=ℒ(t^j). Direct integration near zero gives F(z)=zℒ((1−tz)^−1), so its coefficient of z^(j+1) is μ_j. Explicitly,

μ_j=2^(1−j) Σ_[0≤s≤floor(j/2)] (−1)^s binom(j,2s)/(2s+1).

Thus every μ_j with j≤2n is p-integral. Only finite Taylor truncations are used; no assertion that the entire infinite series F belongs to Z_p[[z]] is needed.

Write B(z)=b_0+b_1z+b_2z² and Q(t)=t^n C(1/t). The coefficient equations at m=n+1+r, for 0≤r≤n, are

ℒ(t^r Q)=−b_0/(n+1+r)!−b_1/(n+r)!−b_2/(n−1+r)!.

The largest factorial here is (2n+1)!, hence all displayed factorials are p-units. In the monomial basis the matrix determining Q is H=(μ_(r+s))_(0≤r,s≤n).

To check invertibility over Z_p, use L_k(t)=2^k i^k P_k(−i(2t−1)), where P_k is the Legendre polynomial normalized by P_k(1)=1. Its leading coefficient is 2^k binom(2k,k), and direct substitution into the Legendre orthogonality integral gives ℒ(L_j L_k)=0 for j≠k and ℒ(L_k²)=(−1)^k 2^(2k+1)/(2k+1). The triangular change of basis therefore gives the exact determinant

det H=(−1)^(n(n+1)/2) 2^(n+1) / ∏_[k=0..n] ((2k+1) binom(2k,k)²).

Every factor is a p-unit at the stated threshold. Since H has p-integral entries and unit determinant, H^−1 has p-integral entries. Consequently, p-integral coefficients of B force p-integral coefficients of Q and C. The Taylor equations through degree n then determine A from p-integral coefficients of B e^z+C F; thus A is p-integral too. If B=0, the same invertible system forces C=0 and then A=0, contrary to the nonzero-triple hypothesis.

For general B, put β=c_p(B) and multiply the triple by p^(−β). Its B coefficients are p-integral and at least one is a unit. The argument just given makes all A and C coefficients p-integral, while the unit B coefficient forces the content of the full scaled triple to be zero. Scaling back proves the asserted equality.

Application to the source endpoint normalization. In work/session_20260913/hp_b2_contiguous_endpoint_arithmetic.md, the raw B coefficient vector is ρ=(a_0,a_1,a_2)×(1+t_0,1+t_1,1+t_2). Let ν=min_j v_p(ρ_j), assuming this vector is nonzero. All these entries are p-integral at p>2n+2: the a_j use factorials of index at most 2n+2, and the displayed t_j formulas have p-integral numerators and the unit denominator G=(−1)^n2^(2n+3)/(n+1). Hence ν≥0. Let (A_raw,B_raw,C_raw) denote the rational raw triple with this B vector.

The source’s exact endpoint reduction, independently audited in worker_1’s earlier notes, states A_raw(1)=γ𝒳 and B_raw(1)=γ𝒟, where

f=2^n/(n!)², g=2^(n+1)/((n+1)!)², and γ=gf/[G(n+1)²].

The scalar γ is a p-unit at p>2n+2. These endpoint identities are explicit source dependencies of this application; the coefficient-content lemma above does not depend on them.

Choose a rational scalar λ making λ(A_raw,B_raw,C_raw) a primitive integral full triple (A_0,B_0,C_0). The lemma gives v_p(λ)=−ν. Therefore, with v_p(0)=+∞,

v_p(A_0(1))=v_p(𝒳)−ν,
v_p(B_0(1))=v_p(𝒟)−ν,
v_p gcd(A_0(1),B_0(1))=min(v_p(𝒳),v_p(𝒟))−ν.

This explicitly identifies the normalization term that must accompany any use of the primitive endpoint-gcd bound. For completeness, the source defines Ω as the gcd of the three maximal minors of the matrix with rows (H_n,J_n), (J_(n+1),K_(n+1)), and (K_(n+2),M_(n+2)), where H_k(x)=k![s^k]e^(xs)(1−s+s²/2)^k and H_k,J_k,K_k,M_k are respectively the first four derivatives, starting at derivative order zero, of x^k H_k(x), evaluated at x=1.

Conditional on that source’s full-depth bound v_p gcd(A_0(1),B_0(1))≤v_p(Ω) for p>2n+4 and endpoint matching B_0(1)=C_0(1), the exact conversion is

min(v_p(𝒳),v_p(𝒟))≤ν+v_p(Ω).

When 𝒟≠0, the actual reduced denominator q=den(𝒳/𝒟) satisfies v_p(q)=v_p(𝒟)−min(v_p(𝒳),v_p(𝒟)). Thus the converted gcd theorem supplies only the conditional lower bound v_p(q)≥max(0,v_p(𝒟)−ν−v_p(Ω)). It supplies no denominator upper bound and does not estimate ν.

Evidence and dependencies: work/session_20260913/hp_b2_endpoint_attempt.md; work/session_20260913/hp_b2_contiguous_endpoint_arithmetic.md, especially equations (5), (9)–(15); work/astra_20260929/worker_1/note_000004.md for the separate derivation audit of reconstruction, scaling, and the primitive quotient-vector argument. The new coefficient-content proof is contained completely above. No analytic normality theorem is required for it; forming q requires the explicit hypothesis 𝒟≠0. Independent review has not yet occurred. Review should certify only this local content equality and normalization conversion, leaving asymptotic estimates, quantitative content bounds, and irrationality outside scope.