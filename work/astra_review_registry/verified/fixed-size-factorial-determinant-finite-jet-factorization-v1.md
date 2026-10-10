> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Finite Taylor coefficient factorization and common-factor cancellation for fixed-size factorial determinants

Status: Independently reviewed research result (AI review; not formal verification)
Author: main
Reviewer: worker_2
Content SHA256: 6eecc758557e4295ac85093753ee77245492520ce6c0cc0539bc68886a0732f3
Review: work/astra_review_registry/reviews/fixed-size-factorial-determinant-finite-jet-factorization-v1-worker_2.md

STATUS AND SCOPE

Unverified candidate submitted by main for independent review. This is an analytic determinant lemma. It asserts no irrationality result, endpoint reconstruction theorem, or reduced-denominator estimate.

STATEMENT

Fix an integer d≥1 and set S=d(d−1)/2. For integers n≥d, let U_n be a complex polynomial of degree at most n+1 with U_n(0)≠0. Suppose every reciprocal root of U_n has modulus at most a fixed L. Write F_n(t)=U_n(t)/U_n(0), and assume

F_n(z/n)→exp(−cz)

locally uniformly in z, for a fixed complex number c.

For an analytic germ P at zero define

ℓ_{n,j}(P)=Σ_{k≥0}[t^k]P/(n+k+1−j)!,  0≤j≤d,
Δ_{n,j}=ℓ_{n,j+1}−ℓ_{n,j},  0≤j≤d−1.

These sums converge absolutely. Let G_{i,n}, 1≤i≤d, be analytic on |t|<ρ and bounded there by M, where ρ>0 and M are independent of n and i. Let a_{i,n}≠0 and P_{i,n}=a_{i,n}F_nG_{i,n}. Define

E_n=det([t^r]G_{i,n})_{1≤i≤d,0≤r≤d−1},
χ_{n,d}=(n!)^d n^S det(Δ_{n,j}(t^rF_n))_{0≤r,j≤d−1}.

Then

(n!)^d n^S det(Δ_{n,j}(P_{i,n}))/∏_i a_{i,n}
=χ_{n,d}E_n+O(1/n),                                      (A)

where the remainder constant depends only on d,L,ρ,M. Moreover,

χ_{n,d}→exp(−dc)∏_{j=0}^{d−1}j!≠0.                     (B)

If the G_{i,n} converge locally uniformly to G_i, then the left side of (A) converges to exp(−dc)∏j! times det([t^r]G_i). No rate for this full convergence is asserted.

For two families, indexed by Q=V,W, satisfying these hypotheses with the same F_n and d, suppose liminf_n|E_{V,n}|>0. Their denominator determinant is eventually nonzero, and

det(ΔP_i^W)/det(ΔP_i^V)
=(∏_i a_i^W/∏_i a_i^V)·(E_{W,n}/E_{V,n}+O(1/n)).       (C)

The remainder in parentheses is an absolute O(1/n); no lower bound on E_{W,n} is required.

PROOF

Write F_n(t)=Σ_k u_{n,k}t^k, extending u_{n,k}=0 beyond its degree. The root hypothesis gives

|u_{n,k}|≤binom(n+1,k)L^k,
|u_{n,k}|/n^k≤(2L)^k/k!.

Local uniform convergence of F_n(z/n) gives u_{n,k}/n^k→(−c)^k/k! for each fixed k.

Let (X)_j be the falling factorial, with (X)_0=1, and put P_j(X)=(X)_{j+1}−(X)_j. For a nonnegative integer r,

Δ_{n,j}(t^rF_n)=Σ_k u_{n,k}P_j(n+k+r+1)/(n+k+r+1)!.

All factorial arguments in the original functionals are nonnegative because n≥d. Each P_j is monic of degree j+1. Consequently

det(P_j(X_i))=Vandermonde(X_1,…,X_d)Q(X_1,…,X_d),

where Q is a polynomial of total degree d whose highest homogeneous part is ∏_i X_i. Here Vandermonde(X)=∏_{i<j}(X_j−X_i).

For a fixed shift tuple r=(r_1,…,r_d), multilinear expansion in k_i therefore gives

(n!)^d n^{Σr_i}det(Δ_{n,j}(t^{r_i}F_n))
→Σ_{k_1,…,k_d≥0}∏_i[(−c)^{k_i}/k_i!]·Vandermonde(k_1+r_1,…,k_d+r_d).             (D)

We justify this passage uniformly enough to control subsequent Taylor expansions. For n≥1,

n!/(n+k+r+1)!≤n^{−k−r−1}.

After substituting X_i=n+k_i+r_i+1, the quantity n^{−d}det(P_j(X_i)) is bounded by a fixed polynomial in the nonnegative variables k_i+r_i+1. Indeed, the Vandermonde is independent of the common n shift, and Q has degree at most d. Combining this bound with |u_{n,k}|/n^k≤(2L)^k/k! and summing the factorial weights yields constants C and m, depending only on d,L, such that

|(n!)^d n^{Σr_i}det(Δ_{n,j}(t^{r_i}F_n))|
≤C∏_i(1+r_i)^m.                                       (E)

This proves the domination required for (D). The sum in (D) is an alternating polynomial in r_1,…,r_d of degree at most S: alternatingness follows by simultaneously permuting the k summation variables. Its homogeneous part of degree S is exp(−dc) times Vandermonde(r). Every alternating polynomial is divisible by that Vandermonde. Hence the sum equals exp(−dc)Vandermonde(r). Choosing r_i=i−1 proves (B), since Vandermonde(0,…,d−1)=∏_{j=0}^{d−1}j!.

Now expand G_{i,n}=Σ_{r≥0}g_{i,n,r}t^r. Cauchy's estimate gives |g_{i,n,r}|≤Mρ^{−r}. For all sufficiently large n the expansions may be interchanged with the determinant: entrywise absolute convergence follows from the factorial bounds above, and determinant expansion is finite in the columns.

A tuple with repeated shifts has identical monomial-shift rows and contributes zero. The least sum of d distinct nonnegative shifts is S. The tuples attaining S are exactly the permutations of 0,…,d−1. Their contribution to the normalized determinant is exactly χ_{n,d}E_n, including its sign by the ordinary determinant expansion.

For the remaining tuples, put m_0=Σr_i≥S+1. Equation (E) bounds their total absolute contribution by a constant times

n^S Σ_{m_0≥S+1} binom(m_0+d−1,d−1)(1+m_0)^{dm}(nρ)^{−m_0}.

For nρ≥2 this is O(1/n), with constant depending only on d,L,ρ,M. This proves (A), including uniformity in the analytic factors. The arbitrary nonzero amplitudes were divided out exactly.

Local uniform convergence of the analytic factors implies convergence of their fixed Taylor coefficients, proving the stated limiting formula. It need not give an O(1/n) convergence rate for E_n or χ_{n,d}.

Finally, apply (A) to both families. By (B), χ_{n,d} is eventually bounded away from zero. Since E_{V,n} is also bounded away from zero, the normalized denominator determinant is eventually nonzero. All coefficient determinants are uniformly bounded by the Cauchy estimates. Division of the two formulas (A) therefore gives (C). This proves the claim.

DEPENDENCIES AND EVIDENCE

The starting determinant lemma and shift expansion appear in work/session_20260927/fixed_exponential_degree_error_theorem.md, Section 2, read completely in the current chain. The preserved independent lead audit is work/astra_20260929/main/note_000082.md, also recovered completely. The present claim makes the common finite-n scalar explicit and proves its cancellation in ratios. These source files motivate the statement; the proof above contains the required argument and does not rely on archived PASS assertions.

SELF-AUDIT AND APPLICATION LIMITS

The determinant size d is fixed. No uniformity as d grows is claimed. The common reference polynomial is essential to the cancellation in (C). Analytic factors must have uniform bounds on a fixed disk. Nonzero limiting coefficient determinants may justify division only after the hypotheses have been verified for the actual functions. The project-specific reciprocal-root bound, microscopic polynomial limit, projection identities, complete-tail identity, and reference endpoint normalization are not established by this abstract lemma. It also does not estimate the extra cofactor determinant occurring in the full matched remainder. No computation or formal verification is claimed; independent review is required.