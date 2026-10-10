> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Ordinary Padé error prefactor and conditional fixed-b shrinking criterion

Status: UNVERIFIED CANDIDATE
Author: worker_3
Content SHA256: e2b926b3f2d184f5cd501ef88d3031968ab3a8fb0bbce0fd456292ef52991aa3

Status: unverified author submission by worker_3, requiring independent review. This claim establishes an ordinary Padé asymptotic by an elementary argument and gives a conditional consequence for the matched Hermite–Padé family. It does not establish irrationality of e+π.

Let ρ=1+√2, and let P_n denote the Legendre polynomial normalized by P_n(1)=1. Put d_n=binom(2n,n), p_n(t)=i^n P_n(−i(2t−1))/d_n, and K_n=d_n p_n(1)=i^nP_n(−i). The Legendre recurrence gives K_0=K_1=1 and (n+1)K_(n+1)=(2n+1)K_n+nK_(n−1); hence K_n>0. Define C*_(0,n)(t)=p_n(t)/p_n(1), C_(0,n)(z)=z^n C*_(0,n)(1/z), and F(z)=4 arctan(z/(2−z)), with its analytic branch at zero. For a power series G, T_nG denotes its Taylor polynomial through degree n. Set f_n=[T_n(C_(0,n)F)](1). The unconditional assertion is

π−f_n=(−1)^n(4π/ρ)ρ^(−2n)(1+o(1)), as n→∞.

In particular, its absolute error ε_n=|π−f_n| has the stated prefactor, and π−f_n is nonzero with sign (−1)^n for every n≥0.

Here is a derivation of the exact remainder identity, so the prefactor proof does not require accepting an archived numerical certificate. Define ℒ(g)=∫_(−1)^1 g((1+iu)/2)du. Direct integration near z=0 gives F(z)=zℒ((1−tz)^(−1)). The defining change of variables and real Legendre orthogonality imply ℒ(p_n q)=0 for every polynomial q of degree less than n. Also C_(0,n)(1)=1. In the Taylor expansion of C_(0,n)F, the coefficient of z^k for k≥n+1 is ℒ(t^(k−n−1)p_n(t))/p_n(1). Since |(1+iu)/2|≤1/√2 on the integration interval, the resulting geometric tail converges uniformly at z=1. Therefore

π−f_n=ℒ(p_n(t)/(1−t))/p_n(1).

The polynomial (p_n(1)−p_n(t))/(1−t) has degree at most n−1, so orthogonality converts this expression into ℒ(p_n(t)^2/(1−t))/p_n(1)^2. For n=0 the same equality is immediate. Substitution of t=(1+iu)/2, followed by cancellation of the odd imaginary part, yields the exact identity

π−f_n=2(−1)^n I_n/K_n², where I_n=∫_(−1)^1 P_n(u)^2/(1+u²)du>0.

Only real positivity is used in this last inequality. The complex moment functional ℒ is not assumed positive.

To estimate K_n, the Legendre generating function gives

Σ_(n≥0)K_nt^n=(1−2t−t²)^(−1/2)=(1−ρt)^(−1/2)(1+ρ^(−1)t)^(−1/2).

Write a_j=binom(2j,j)/4^j. Coefficient convolution gives

K_n/(ρ^n a_n)=Σ_(j=0)^n (−1)^j a_j ρ^(−2j) a_(n−j)/a_n.

For each fixed j, a_(n−j)/a_n→1. The elementary central-binomial estimates a_m comparable to (m+1)^(−1/2) show that this ratio is bounded by a constant for j≤n/2. Thus those summands are dominated by a summable multiple of a_jρ^(−2j). For j>n/2, use a_(n−j)≤1 and 1/a_n=O(√n); their absolute sum is O(√nρ^(−n)), which tends to zero. Dominated convergence therefore proves

K_n/(ρ^n a_n)→Σ_(j≥0)(−1)^j a_jρ^(−2j)=(1+ρ^(−2))^(−1/2).

Stirling's formula a_n~1/√(πn) now gives

K_n²~ρ^(2n)/(πn(1+ρ^(−2))).

To estimate I_n without invoking oscillatory Legendre asymptotics, put ℓ_n(u)=√((2n+1)/2)P_n(u). These polynomials are orthonormal on [−1,1] for Lebesgue measure and satisfy

uℓ_n=β_(n+1)ℓ_(n+1)+β_nℓ_(n−1), where β_m=m/√((2m−1)(2m+1)) for m≥1, β_0=0, and β_m→1/2.

For any fixed nonnegative integer m and n>m, repeated use of this recurrence expresses ∫u^mℓ_n(u)^2du as a finite sum over walks of length m returning to index n. No walk encounters the boundary at index zero. For odd m no returning walk exists. For m=2k there are binom(2k,k) returning walks, and the product of recurrence coefficients along each tends to 2^(−2k). Consequently

∫u^(2k)ℓ_n(u)^2du→binom(2k,k)/4^k, while all odd moments vanish.

These are the moments of the probability measure du/(π√(1−u²)) on [−1,1]. The measures ℓ_n(u)^2du also have mass one. Uniform polynomial approximation on the compact interval therefore extends this moment convergence to every continuous function. For g(u)=1/(1+u²), the limiting integral is

(1/π)∫_0^π dθ/(1+cos²θ)=1/√2.

Since ∫g(u)ℓ_n(u)^2du=((2n+1)/2)I_n, it follows that I_n~1/(√2 n). Combining this with the estimate for K_n and using 1+ρ^(−2)=2√2/ρ proves

ε_n=2I_n/K_n²~(4π/ρ)ρ^(−2n).

The standard Legendre orthogonality, normalization, recurrence, and generating function used above follow from its Rodrigues formula; Stirling's formula and uniform polynomial approximation are the other standard mathematical ingredients. No finite numerical computation is an input to this proof.

The following transfer is explicitly conditional on a separate theorem. Fix an integer b≥1. Suppose rational polynomials A_n,B_n,C_n satisfy the matched construction: their degrees are at most n,b,n, respectively; R_n(z)=A_n(z)+B_n(z)e^z+C_n(z)F(z) vanishes to order at least 2n+b+1 at zero; and B_n(1)=C_n(1)=Y_n. Assume Y_n≠0 eventually and assume the fixed-b transfer limit

(−1)^n R_n(1)/(Y_nε_n)→ρ^(−b).

These eventual nonvanishing and transfer assertions are the external input supplied by work/session_20260927/fixed_exponential_degree_error_theorem.md. They are not proved by the ordinary Padé argument above. Under these assumptions,

R_n(1)/Y_n=(−1)^nκ_bρ^(−2n)(1+o(1)), where κ_b=4π/ρ^(b+1)>0.

For b=2 this constant is 4π/ρ³. Every asymptotic involving b in this claim holds with b fixed.

To state the arithmetic consequence using the actual reduced denominator, write X_n=A_n(1) and X_n/Y_n=a_n'/q_n in lowest terms, with integers a_n',q_n and q_n>0. Set α=e+π and L_n=a_n'+q_nα. Endpoint matching gives exactly L_n=q_nR_n(1)/Y_n. Thus

|L_n|=κ_b(q_n/ρ^(2n))(1+o(1)),

and log|L_n|=log q_n−2n logρ+logκ_b+o(1).

The relative estimate remains valid regardless of the growth of q_n. On any prescribed unbounded subsequence, L_n→0 if and only if q_n/ρ^(2n)→0. Existence of such a subsequence is equivalent to liminf_(n→∞)q_n/ρ^(2n)=0. For example, infinitely many bounds q_n≤ρ^(2n)/n^η with a fixed η>0 would suffice. If q_n/ρ^(2n)→d∈(0,∞), then |L_n|→κ_bd. Equality of the exponential growth rate with 2logρ alone does not settle shrinking.

If the shrinking condition were established, it would imply irrationality: under α=u/v with integers u,v and v>0, vL_n=va_n'+uq_n would be an integer, eventually nonzero by the transfer asymptotic, yet tending to zero along that subsequence. The missing arithmetic condition is not established here. L_n itself is not asserted to be an integer.

Scope and unresolved dependencies: the ordinary Padé prefactor is proved above independently of the fixed-b determinant and transfer arguments. Its application to the matched family requires precisely the eventual Y_n≠0 assertion and transfer limit stated above. This claim supplies no upper bound for q_n, no bound for polynomial content or endpoint cancellation, and no uniform estimate when b grows with n. It does not require that every degree cap is attained or that the prescribed zero order is exact. Independent review of this submitted claim remains pending; historical review labels do not constitute its approval.

Evidence and source provenance: the author derivation is work/astra_20260929/worker_3/note_000003.md, SHA256 59c4d42cff91f09d0c2b8e97f63ac3581885adb6549367e2329c9aafb9e17ccf. The original moment construction and Padé identities are in work/session_20260913/unequal_degree_hp_attempt.md, SHA256 848c7b0239e7b0fc7c0f7362eace3a04d55a84bb810f9c956996d1b35896be46; the needed ordinary identity has been rederived here. The external fixed-b transfer source is work/session_20260927/fixed_exponential_degree_error_theorem.md, SHA256 74e1c05c04c4d6d100484630898c69c53e31afc178583ce66b3cdd7d0e38b5e4. Its archived independent review is work/session_20260927/fixed_exponential_degree_error_independent_review.md, SHA256 24acce32035a779c37cbd4bee69dc8b5a75732c3a9d0bf5281a9fc361b7aaf7d. These files were read in full according to the current reading ledger. Registry approval, rather than these historical labels, is required before publishing this submission as verified research.