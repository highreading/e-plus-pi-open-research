> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent adversarial review of the fixed-prime Roth argument

2026-09-13. Reviewer: delegated source/mathematics auditor. This review checks the new argument independently from its outline. It accepts the separately audited Item237/309/314 recurrence and branch bridges, and the all-zero-three-state bound from `fixed_prime_stepanov_attempt.md`, as explicit dependencies. It does not independently reprove every archived certificate. No conclusion about the rationality of e+pi follows from this upper estimate alone.

**Conclusion:** the proposed qualitative bound Z(p)=o(p) is valid under those inputs. The finite-field reduction, dependence of the initial combination on p, and order of the density/block-size/prime quantifiers do not introduce a gap. The argument below supplies precise versions of those steps.

## 1. Input and the transfer determinant

For each sufficiently large prime p outside a fixed finite exceptional set, let N=p/12+O(1), h_n=e/2+3n with e in {1,5}, and let u_0,...,u_(N-1) be the actual determinant sequence. The inputs are:

1. Whenever all four indices are actual,
   sum_(j=0)^3 P_j(h_n) u_(n+j)=0 modulo p, for fixed degree-16 polynomials P_j in Q[h].
2. There are at most five n for which the three-state vector w_n=(u_n,u_(n+1),u_(n+2))^t is zero.
3. The forward transfer matrix has a finite rational limit C at h=infinity, with the characteristic polynomial computed below.

Use column states and

    T(h) = [[0,1,0],[0,0,1],[-P_0/P_3,-P_1/P_3,-P_2/P_3]].

For an integer d>=1 define

    M_d(h)=T(h+3(d-1)) ... T(h+3) T(h),
    F_d(h)=det([e_1; e_1 M_d(h); e_1 M_(2d)(h)]).

The brackets describe three rows, not columns. These are fixed rational functions over Q. Products are ordered as displayed because states are columns. Away from the shifted zeros of P_3,

    (u_n,u_(n+d),u_(n+2d))^t = H_d(h_n) w_n,

where H_d is the matrix whose determinant is F_d. The recurrence equations needed by the transfer remain inside the actual index interval after requiring n+2d+2<N. Discarding the last 2d+2 possible starting indices costs O_d(1); this removes any endpoint ambiguity.

## 2. Independent proof that every F_d is nonzero

The characteristic polynomial of C is

    x^3 -(413233/729)x^2 -(9856/19683)x -64/531441.

Its primitive integer multiple is

    H(x)=531441x^3-301246857x^2-266112x-64.

Modulo7 this is x^3-2x^2-1. Its values at x=0,...,6 are respectively

    6,5,6,1,3,4,3 (mod7).

There is no root, so this cubic is irreducible over Q. Its exact discriminant is

    -572058527163885303300000000
    =-2^8 * 3^21 * 5^8 * 11^3 * 641^2.

Its square class is -33, so the splitting field L has Galois group S_3 and its unique quadratic subfield is Q(sqrt(-33)). Every root of unity zeta in L generates an abelian Galois extension Q(zeta)/Q; its Galois group is an abelian quotient of S_3, hence has order at most2. The only potential nonreal quadratic cyclotomic fields are Q(i) and Q(sqrt(-3)), neither equal to Q(sqrt(-33)). Consequently the roots of unity in L are exactly +/-1.

The distinct roots lambda_1,lambda_2,lambda_3 of H are nonzero. No ratio lambda_i/lambda_j is1. No ratio is -1 either: opposite roots would leave the third root equal to the rational sum 413233/729, contradicting irreducibility. Thus no ratio of distinct roots is a root of unity.

The companion matrix C has eigenvector matrix

    V = [[1,1,1],[lambda_1,lambda_2,lambda_3],
         [lambda_1^2,lambda_2^2,lambda_3^2]].

It is invertible. Since T(h+3j) tends to C for fixed j, M_d(h) tends to C^d. Multiplying the limiting H_d by V shows

    lim_(h->infinity) F_d(h)
      = product_(i<j)(lambda_j^d-lambda_i^d)
        /product_(i<j)(lambda_j-lambda_i) != 0.

Therefore F_d is not the zero rational function for every fixed positive d. This argument proves all d at once; checking finitely many small d would not have sufficed.

The polynomial, modular values and discriminant were independently recomputed with exact symbolic arithmetic. Approximate root values were inspected only diagnostically and are not an input to the proof.

## 3. Fixed d gives only boundedly many zero arithmetic progressions

Fix d. Write F_d=A_d/B_d with nonzero integer polynomials after clearing rational coefficient denominators. Exclude the finitely many primes dividing their contents and all fixed rational denominators used in the transfer. For the remaining primes, A_d and B_d reduce to nonzero polynomials.

There are O_d(1) possible starts at which a denominator of some T(h_n+3j), 0<=j<2d, vanishes, or B_d(h_n)=0, or A_d(h_n)=0. This follows from the elementary polynomial root bound, since n->h_n is injective modulo p on the actual interval (p>3 and N<p). Repeated factors and coincidences only lower the bound. The number and degrees of these fixed polynomials depend on d, not on p or on the state w_n.

At any remaining start, a zero arithmetic progression

    u_n=u_(n+d)=u_(n+2d)=0

forces H_d(h_n)w_n=0 with H_d(h_n) invertible, hence w_n=0. There are at most five such starts by the independent zero-three-state input. Including the bounded endpoint loss yields

    #{n: u_n=u_(n+d)=u_(n+2d)=0} <= C_d,

for a constant C_d and all sufficiently large p. The estimate is uniform over every admissible p-dependent initial linear combination. It does not require that combination to reduce from one fixed rational initial vector.

## 4. Finite Roth, with the quantifiers made explicit

The combinatorial theorem required here is Roth's theorem on three-term arithmetic progressions, not Roth's Diophantine approximation theorem. Its finite form is: for each rho>0 there is an integer K such that every subset of {0,...,K-1} with at least rho K elements contains a nonconstant three-term arithmetic progression.

Primary bibliographic source: K. F. Roth, *On Certain Sets of Integers*, Journal of the London Mathematical Society s1-28 (1953), 104-109, [publisher record](https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/jlms/s1-28.1.104). The publisher record was checked in this review; its original full proof was not reread. The theorem is used as a known theorem.

Suppose for contradiction there is delta>0 and an unbounded sequence of primes with at least delta N zero positions. Choose K once using finite Roth at density delta/2. Partition [0,N) into full disjoint blocks of length K and a remainder of fewer than K positions.

Call a full block dense if it contains at least delta K/2 zero positions, and let B be the number of dense blocks. The total number of zeros is at most

    B K + (delta/2) N + K.

Hence B >= delta N/(2K)-1, which tends to infinity. Each dense block contains a nonconstant three-term progression of zero positions, with integer difference 1<=d<K/2. Choose one such progression from each dense block. These have distinct starting indices because the blocks are disjoint.

For the already fixed K, Section3 bounds the total number of such progressions by the finite constant sum_(1<=d<K/2) C_d, once p exceeds the finite union of the exceptional-prime sets for these d. This contradicts B tending to infinity. Therefore

    #{0<=n<N:u_n=0}=o(N)=o(p).

The correct quantifier order is delta, then K(delta), then the finite union of bad primes and constants, then p tending to infinity. No uniform control of C_d as d tends to infinity is needed for this qualitative conclusion.

## 5. What this proves and what it does not

The estimate controls all zeros of the actual fixed-prime determinant gate, hence its simultaneous-collision subset through the all-row Item314 implication. It improves the completed bounded-run result to a qualitative density-zero theorem within a fixed-prime row family.

It can be summed to give an averaged o(X^2) weighted contribution over construction indices M in a dyadic interval, using the explicit affine row map and the prime number theorem or a suitable elementary bound for sum p log p. A Markov argument then gives a density-one o(M) statement for this component in the usual epsilon formulation. The independent aggregate derivation should keep the fixed-prime estimate uniform and handle fixed exceptional primes, as above.

It does not by itself produce positive divisor gains, a favorable subsequence meeting the main matching threshold, or a pointwise o(M) bound at every construction index. These remain separate mathematical questions.

The archived recurrence identities and the five-zero-state result remain indispensable proof dependencies. If either were merely fitted to finite data, the present conclusion would be conditional on their global validity. The existing notes describe them as exact identities with replayable certificates; this review does not replace the separate certificate audit.

## 6. Review of the full written quantitative strengthening

After writing Sections1-5 independently, I read the complete `fixed_prime_roth_density.md`, including the new growing-spacing argument. I checked the matrix multiplication order, common integer clearing, polynomial degrees and coefficient norms, reduction modulo p, the final two-state boundary issue, the deletion argument, and the summation consequence. No mathematical correction is required in that version, subject to the same archived proof dependencies.

In detail, after clearing all P_j by a common integer, put L_d=H(6d+1)^16. Every entry of M(h+3t), for 0<=t<2d, has coefficient l1 norm at most L_d. An entry of its k-factor product has norm at most 3^(k-1)L_d^k, which is bounded by (3L_d)^k. Because the first row of J_d is e_1, its determinant has just two possibly nonzero summands. Hence

    deg J_d <=48d,
    ||J_d||_1 <=2[3H(6d+1)^16]^(3d).

These bounds concern the actual nonzero integer numerator obtained by clearing transfer denominators. They do not assume that a reduced numerator has small height. For K_p=floor(log p/(100 log log p)), the logarithm of the bound is at most (48/100+o(1))log p, uniformly for 1<=d<=K_p. Thus no such J_d reduces to the zero polynomial for large p. The shifted denominator product D_(2d) has degree32d and remains a nonzero polynomial after excluding the fixed divisors of leading(P_3).

If a zero progression ends at n+2d, the full transfer through 2d steps uses values through n+2d+2. Of the allowed progression starts, exactly at most the last two fail this stricter condition. Adding2 to the 48d+32d+5 count is sufficient. This supports the written safe bound80d+7; no loss of order d at each endpoint is required.

Deleting every start of every zero progression with gap<=K_p deletes at most sum_(d<=K_p)(80d+7)=O(K_p^2) indices. Any progression remaining after deletion would have existed before deletion and its start would have been deleted, a contradiction. Every interval of length K_p in the remaining zero set is consequently three-term-progression-free. Thus the written estimate

    Z(p) <=(N_p/K_p)r_3(K_p)+O(K_p^2)

is valid. It gives the qualitative result already proved above, and any known bound on r_3 gives the corresponding quantitative conclusion.

I independently opened the primary [Bloom–Sisask arXiv PDF](https://arxiv.org/pdf/2309.02353), version1 of 5 September2023, and checked Theorem1 on PDF p.1: its stated bound is r_3(K)<=K exp(-c(log K)^(1/9)) for an absolute positive constant c. Only the theorem statement was checked in this pass; its full proof is an imported literature theorem. Since log K_p~log log p and K_p^2 is negligible compared with p exp(-c(log log p)^(1/9)), this gives the quantitative result in the root note. The arXiv record contains no journal reference, so this review does not describe that particular source as a verified journal publication.

Two presentation corrections were sent to the root: call the displayed leading coefficients the ratios normalized by leading(P_3), and avoid implying a separately verified journal publication for the 2023 arXiv source. Neither changes the mathematical argument.

## 7. Review of the later leading-coefficient simplification

The root subsequently proposed using only the leading coefficient of J_d. This simplification is valid. Let L be the degree16 coefficient matrix of M(h)=P_3(h)T(h), after common integer clearing, and let l_3 be the nonzero leading coefficient of P_3. Then L=l_3 C. Translations do not change a polynomial matrix's highest coefficient, so the degree16k coefficient of A_k is L^k. The coefficient of degree48d in J_d is therefore

    j_d=det([e_1; e_1 L^d; e_1 L^(2d)])
       =l_3^(3d) det([e_1; e_1 C^d; e_1 C^(2d)]) !=0.

Thus deg J_d is exactly48d. The integer coefficient j_d is nonzero by the same all-d Vandermonde argument. For B=max(2, maximum absolute row-sum of L), the matrix row-sum norm gives |j_d|<=2B^(3d). Choosing K_p=floor(log p/(6 log B)) gives |j_d|<=2sqrt(p)<p for p>4 and1<=d<=K_p. Hence every J_d retains its nonzero leading coefficient modulo p throughout this longer spacing range. The old full-coefficient height estimate may be replaced by this shorter argument, and K_p is now of order log p. The final exp(-c(log log p)^(1/9)) shape is unchanged.

This argument applies without change to the ordinary j=1 extension in `roth_extension_actual_cells.md`, because its operator is identical. It uses no assumption on numerical root sizes or on a residue-field eigenvalue ratio.
