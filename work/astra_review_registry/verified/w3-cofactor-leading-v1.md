> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Leading term of the full factorial determinant and conditional endpoint cofactor constant

Status: Independently reviewed research result (AI review; not formal verification)
Author: worker_3
Reviewer: worker_2
Content SHA256: bd4dd231d066a28039e75fa399678b6eb7f2c6f1f431ca3771acddfe23f86c9b
Review: work/astra_review_registry/reviews/w3-cofactor-leading-v1-worker_2.md

STATUS: UNVERIFIED AUTHOR CANDIDATE. Independent review is required.

SCOPE

This claim proves a full-factorial determinant asymptotic and specializes it to explicitly stated endpoint normalization hypotheses. It is distinct from worker3-microscopic-reference-and-sharp-cofactor-bound-v1: that candidate supplies application estimates and an upper bound; this claim supplies the first nonzero term. The endpoint specialization below remains conditional on the reference and analytic-factor hypotheses, whose application verification is contained in that separately pending candidate. No reduced arithmetic denominator estimate, growing-degree assertion, or irrationality conclusion is made.

1. ABSTRACT STATEMENT

Fix d≥1 and put S=d(d−1)/2. Let n tend to infinity through integers n≥d. Let F_n be polynomials with F_n(0)=1, satisfying, for a fixed C,

|[t^k]F_n|≤(Cn)^k/k!,
F_n(z/n)→exp(−cz) locally uniformly in complex z.

Let G_(i,n), 1≤i≤d, be analytic and uniformly bounded on a common fixed disk. Suppose their coefficients in degrees 0,...,d−1 converge, and write

E=lim det([t^r]G_(i,n))_(i=1,...,d;r=0,...,d−1).

For nonzero amplitudes a_(i,n), set P_(i,n)=a_(i,n)F_nG_(i,n). Define

T_(n,j)(P)=Σ_(m≥0)[t^m]P/(n+m+1−j)!, 0≤j≤d−1.

Then

(n!)^d n^(d+S) det(T_(n,j)(P_(i,n)))/∏_i a_(i,n)
→exp(−dc)(∏_(j=0)^(d−1)j!)E.                                      (1)

More precisely, with

κ_(n,d)=(n!)^d n^(d+S)det(T_(n,j)(t^rF_n))_(r,j=0,...,d−1),
E_n=det([t^r]G_(i,n)),

the normalized determinant equals κ_(n,d)E_n+O(1/n), and κ_(n,d)→exp(−dc)∏j!. The O(1/n) is the Taylor-shift remainder; no convergence rate for κ_(n,d) or E_n is asserted.

2. EXACT KERNEL AND DOMINATION

Write F_n=Σ_k u_(n,k)t^k and extend u_(n,k)=0 beyond its degree. The microscopic convergence implies u_(n,k)/n^k→(−c)^k/k! for each fixed k, by Cauchy's coefficient formula.

For nonnegative integers x_1,...,x_d,

det(1/(n+x_i+1−j)!)_(i=1,...,d;j=0,...,d−1)
=V(x_1,...,x_d)/∏_i(n+x_i+1)!,                                  (2)

where V(x)=∏_(i<h)(x_h−x_i). To prove (2), extract the displayed denominator from each row. Column j becomes the monic falling-factorial polynomial (n+x_i+1)_j of degree j; its determinant is V(x), with precisely this sign.

Fix shifts r_i≥0. Expanding the F_n factors row by row and putting x_i=r_i+k_i gives the exact shift kernel. Since

n!/(n+k+r+1)!≤n^(−k−r−1),
|V(x)|≤∏_i(1+x_i)^(d−1),
1+r+k≤(1+r)(1+k),

its normalized summands satisfy

|(n!)^d n^(d+Σr_i) ∏_i u_(n,k_i) V(r+k)/∏_i(n+r_i+k_i+1)!|
≤∏_i[C^(k_i)(1+k_i)^(d−1)/k_i!] ∏_i(1+r_i)^(d−1).               (3)

The right side is summable in all k_i. This proves both dominated convergence for every fixed shift tuple and the uniform bound

|(n!)^d n^(d+Σr_i)det(T_(n,j)(t^(r_i)F_n))|
≤K_d∏_i(1+r_i)^(d−1).                                         (4)

For fixed k,r, the remaining factorial ratios tend to one after their displayed powers of n are extracted. Thus the fixed-shift limit equals

Σ_(k_1,...,k_d≥0) ∏_i[(−c)^(k_i)/k_i!] V(r_1+k_1,...,r_d+k_d).    (5)

For j≥0 put

M_j(r)=exp(c)Σ_(k≥0)(−c)^k(r+k)^j/k!.

This is a monic polynomial in r of degree j: expansion of (r+k)^j leaves finitely many absolutely convergent scalar sums, and its leading coefficient is exp(c)exp(−c)=1. Multilinearity of the Vandermonde determinant, justified by (3), evaluates (5) as

exp(−dc)det(M_j(r_i))_(i=1,...,d;j=0,...,d−1)
=exp(−dc)V(r).

At r_i=i−1 this is exp(−dc)∏_(j=0)^(d−1)j!, proving the asserted limit of κ_(n,d).

3. CANCELLATION AND THE SUMMABLE SHIFT TAIL

Choose a fixed radius R inside the common analytic disk, and M such that |[t^r]G_(i,n)|≤MR^(−r). Expand the determinant multilinearly in these Taylor coefficients. The factorial bounds ensure entrywise absolute convergence and justify the expansion. A repeated shift produces identical kernel rows and contributes zero.

The least sum of d distinct nonnegative shifts is S. The tuples with that sum are exactly the permutations of 0,...,d−1. Their combined contribution is κ_(n,d)E_n, with the sign given by the ordinary determinant expansion.

For all remaining tuples, m=Σr_i≥S+1. Bound their number by binom(m+d−1,d−1) and use (4). The total absolute remainder in the normalization of (1) is at most a constant times

n^S Σ_(m≥S+1) binom(m+d−1,d−1)(1+m)^(d(d−1))(nR)^(−m).

For nR≥2 this is O(1/n). The constants depend only on d,C,R,M. This proves the precise factorization and (1), including the required summation after cancellation. It also works when E=0; asymptotic equivalence to a nonzero leading term requires E≠0.

4. COMPARISON WITH THE PUBLISHED DIFFERENCE LEMMA

The published claim fixed-size-factorial-determinant-finite-jet-factorization-v1, payload SHA-256 6eecc758557e4295ac85093753ee77245492520ce6c0cc0539bc68886a0732f3, treats Δ_(n,j)=T_(n,j+1)−T_(n,j), j=0,...,d−1. Its normalization is (n!)^d n^S, and its limiting constant is the same exp(−dc)∏j! times E.

Thus the full determinant in (1) has an additional n^(−d), not a changed microscopic constant. The distinction follows exactly from the evaluation polynomials: full columns have degrees 0,...,d−1, whereas difference columns are (y)_(j+1)−(y)_j. Their determinant equals V(y)H_d(y), where H_d has degree d and highest homogeneous part ∏y_i. Consequently H_d(n+x_i+1)/n^d→1 for fixed x. A uniform bound by K_d∏_i(1+x_i)^d combines with the Vandermonde bound to give a summable weight C^k(1+k)^(2d−1)/k! in each variable. This is consistent with, and explicitly checks, the published domination argument. No new proof of its project-specific hypotheses is inferred from this comparison.

5. PRECISE CONDITIONAL ENDPOINT SPECIALIZATION

Fix b≥1. Put ρ=1+sqrt(2), s=ρ^(−2), A=1−s, and

f(t)=[1−2t+sqrt((1−2t)^2+1)]/ρ,

using the branch positive at zero. Hence f(0)=1 and f′(0)=−sqrt(2).

Here are the required application hypotheses. The common reference is F_n=p_(n+1)/p_(n+1)(0), where

p_0=1, p_1=t−1/2,
p_(m+1)=(t−1/2)p_m + m²/[4(4m²−1)]p_(m−1).

Assume the reference has degree n+1, reciprocal roots bounded by 2, coefficient bound |[t^k]F_n|≤(4n)^k/k!, and microscopic limit exp(−sqrt(2)z). Assume the row amplitudes below are nonzero eventually and that their normalized factors, after division by their value at zero and F_n, are uniformly bounded analytic functions on one fixed disk, converging there as follows:

P_l=p_(n+l), 1≤l≤b−1: factor limit f^(l−1);
V: factor limit A/(f−s);
W: factor limit 2/(f+1).

The high-row list is empty when b=1. These are explicit hypotheses, not independent approvals of the pending application claim.

For identification with the original endpoint system, its V and W are

V(t)=Σ_(k=0)^n p_k(t)p_k(1)/h_k,
W(t)=1/(1−t)−Σ_(k=0)^n χ_kp_k(t)/h_k,
h_k=2(−1)^k/[(2k+1)binom(2k,k)^2],
χ_k=∫_(−1)^1 p_k((1+iu)/2)/(1−(1+iu)/2)du.

Let ℓ_j=T_(n,j), 0≤j≤b, and use that exact column order. Define

D_V=det[(ℓ_j(P_l))_(l=1,...,b−1); (1)_(j=0,...,b); (ℓ_j(V))_(j=0,...,b)],
N=det[(ℓ_j(P_l))_(l=1,...,b−1); (ℓ_j(V))_(j=0,...,b); (ℓ_j(W))_(j=0,...,b)].

Subtracting each previous column from its successor, performed from right to left, and expanding along the row of ones gives

D_V=(−1)^(b+1)det(Δ_j(P_1),...,Δ_j(P_(b−1)),Δ_j(V)),

where the notation denotes those rows in that order, with columns j=0,...,b−1.

6. FIRST NONZERO COEFFICIENT DETERMINANTS

Set S_b=b(b−1)/2. In the coordinate x=f−1, the limiting high rows are (1+x)^j, j=0,...,b−2. Their coefficient block in degrees 0,...,b−2 is triangular with diagonal one. For the denominator, the remaining coefficient of A/(A+x) gives

E_V=(−sqrt(2))^(S_b)(−1)^(b−1)/A^(b−1)≠0.

For N, the two remaining columns have degrees b−1,b, and the remaining rows are A/(A+x), 2/(2+x). Their 2 by 2 determinant is

(−1)^(b−1)A^(−b+1)·(−1)^b2^(−b)
−(−1)^bA^(−b)·(−1)^(b−1)2^(−b+1)
=(2−A)/(2^b A^b)=(1+s)/(2^b A^b).

The change from x to t has triangular coefficient transformation with diagonal 1,f′(0),...,f′(0)^b. Therefore

E_N=(−sqrt(2))^(b(b+1)/2)(1+s)/(2^b A^b)≠0.

These formulas include b=1, when E_V=1 and E_N=−1. Using (1+s)/(1−s)=sqrt(2), they give

E_N/E_V=−2^((1−b)/2).                                           (6)

7. FACTORIAL SCALE AND SIGN

Apply (1) to N with d=b+1 and amplitudes P_1(0),...,P_(b−1)(0),V(0),W(0). Apply the published difference lemma to D_V with d=b and amplitudes P_1(0),...,P_(b−1)(0),V(0). Its hypotheses are expressly included above. Since E_V≠0, D_V is eventually nonzero.

The amplitude quotient is W(0). The factorial quotient is 1/n!. The power difference is

(b+1)(b+2)/2−b(b−1)/2=2b+1.

The microscopic quotient is exp(−sqrt(2)), and the products of factorials contribute b!. Finally the denominator row sign is (−1)^(b+1). Combining these with (6) proves

n! n^(2b+1) N/[D_V W(0)]
→(−1)^b b!2^((1−b)/2)exp(−sqrt(2)).                             (7)

The limit is nonzero. Accordingly the polynomial exponent in the corresponding upper bound is attained under these hypotheses. The first three constants are −exp(−sqrt(2)), sqrt(2)exp(−sqrt(2)), and −3exp(−sqrt(2)).

DEPENDENCIES, EVIDENCE, AND SELF-AUDIT

The proof of (1) is self-contained. The denominator specialization invokes the published factorial-determinant lemma at work/astra_review_registry/verified/fixed-size-factorial-determinant-finite-jet-factorization-v1.md with the payload hash stated above. The original endpoint definitions and proposed constants were recovered from work/astra_20260929/worker_3/note_000064.md and the domination supplement in note_000066.md. The separate application-hypothesis derivation is work/astra_review_registry/candidates/worker3-microscopic-reference-and-sharp-cofactor-bound-v1.md, payload SHA-256 48241943005ab30cb868e89f6e9927046c2fa5a6f81ea94e10f38e5155682718; that claim remains independently unapproved in the supplied registry. Thus (7) is explicitly conditional here on the listed application hypotheses, rather than silently promoting that candidate.

The proof retains the original row and column orders, covers b=1, proves a summable bound before exchanging limits, and distinguishes the O(1/n) shift tail from unquantified convergence of leading factors. Earlier finite numerical ratios are not used as proof. All constants may depend on fixed d or b. No assertion is made about actual reduced denominators, growing b, or the rationality of e+pi.