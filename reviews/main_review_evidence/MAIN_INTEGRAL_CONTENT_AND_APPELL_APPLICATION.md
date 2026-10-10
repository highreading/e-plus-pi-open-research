> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Primary review: integral content congruences and actual Appell normalization

Reviewer: primary agent main Codex. Date: October 4, 2026. The primary agent personally made the judgments below; the assisting agent supplied originals and coordinates only.

This record accepts the auxiliary lemmas and normalizations below. It does not approve pending prime-seed tables, infinite actual-endpoint estimates, or an entire literature file. Reading scopes for complete natural sections, typographic issues, and mathematical applicability are recorded separately.

## Original literature actually read

- C. Ryba, *Stable centres of wreath products*, Algebraic Combinatorics 6 (2023), 413–455. Original PDF fingerprint: `4f9100622a63bc9fea54dcef3e665f9523e5cb20ed7960c502cf5893de04a68e`. The primary reviewer personally read complete §3 (PDF pages 11–18, printed 422–429) and the complete bibliography. Original-page text on PDF 12–17 was also read page by page, and images on PDF 15,16,17 were visually inspected. Proposition 3.11 and Theorems 3.8,3.14 with their complete proofs are used. Remaining §§2,4–7 and the full PDF are not marked read.
- Bonneux–Hamaker–Stembridge–Stevens, *Wronskian Appell Polynomials and Symmetric Functions*, arXiv:1812.01864v2. Original PDF fingerprint: `a4e455d65179a6c9d514d4db613c4277403c08b26b37816879f911af57ff0508`. The primary reviewer personally read complete §§3,4,5.4 and the complete bibliography and visually inspected PDF 7,11. The short proof of Theorem 5.8 ends with a square at the bottom of PDF 11. Text extraction omitted that glyph; no proof page is missing. Other parts of §5, §§6–7, and the entire PDF are not marked read.

This record reuses original literature in the archive. Finding the same result again is not counted as new research.

## Content congruence for partitions of equal size

Let λ and η be partitions of the same size N whose box-content multisets agree modulo any positive integer M. Multiplicity is included; comparison of residues that merely occur is insufficient.

Ryba's coefficient ring R consists of rational polynomials integer-valued at every integer, rather than only Z[t]. Theorem 3.8 gives an integral isomorphism from R⊗Λ to the Farahat–Higman algebra. Theorem 3.14 therefore expresses the central character value of each fixed conjugacy class as a symmetric function of box contents, whose R coefficients become integers at the same integer N. Equal N is essential; coefficients evaluated at different N cannot be declared congruent directly.

There is also a direct rederivation at fixed N from Proposition 3.11. A monomial symmetric function of Jucys–Murphy elements has the corresponding class sum as leading term with coefficient 1; other terms are lower in lexicographic order by reduced cycle-type size and length. Group-ring expansion coefficients are integers, so recursively solving for each valid class sum requires subtraction only, with no division by integers. Nonexistent cycle types are zero under the source convention. Jucys–Murphy eigenvalues in the Specht basis are box contents, giving an integral symmetric-polynomial expression at fixed N.

Every central character value at λ and η is consequently congruent modM. Frobenius and hook formulas give

    H(λ)s_λ = Σ_{μ⊢N} ω^λ_μ p_μ,

Here ω^λ_μ is the central character value of the corresponding class sum. The identity-class coefficient is 1. Every ω^λ_μ is integral, as follows directly from the integral content expression. Coefficientwise subtraction gives

    H(λ)s_λ − H(η)s_η ∈ M Z[p_1,p_2,…].

This auxiliary lemma thus retains complete depth for composite moduli. It does not use membership in the same p-block to infer higher p-powers, nor expand Theorem 3.16's prime-level block conclusion. It cannot imply congruence between partitions of different sizes.

## Normalization of the actual family

For any integer background b, set a_j^(b)(x)=[z^j] exp(xz)(1+z²)^b, defining coefficients with negative j as zero. Even for b<0, this is a formal rational-coefficient power series with each fixed a_j polynomial; j!a_j is a monic Appell polynomial.

The complete-function map in Appell Theorem 4.1 is φ_b(h_j)=a_j^(b). The monic Wronskian polynomial is φ_b(H(λ)s_λ), not φ_b(s_λ). These normalizations differ by the hook product. When the modulus contains hook prime factors, one cannot divide out that product and still claim integral coefficient congruence.

Using the logarithm of exp, Proposition 4.3 gives here

    φ_b(p_1)=x,
    φ_b(p_{2h})=2b(−1)^{h+1},
    φ_b(p_{2h+1})=0  (h≥1).

These images lie in Z[x]. The integral power-sum expression for augmented Schur functions used in the proof of Theorem 5.8 applies, so every corresponding monic Wronskian polynomial is in Z[x]. The equal-size content lemma remains valid after this integral map.

For the actual background b=n≥1, every surviving monomial other than the identity class contains a factor 2n. Thus every λ satisfies

    φ_n(H(λ)s_λ) ≡ x^{|λ|}  (mod 2n in Z[x]).

For the actual full Toeplitz matrix A=(a_{n+i−j})_{0≤i,j≤n}, transposition identifies Jacobi–Trudi with λ_D=(n^{n+1}). The minor deleting row0,colj corresponds to λ_j=((n+1)^j,n^{n−j}), and the inverse-column cofactor sign is (−1)^j. With these conventions fixed, the hook ratio is

    H_D/H_j=(2n−j)!/[j!(n−j)!].

At x=1, the augmented values of the full determinant and every cofactor are 1 mod2n and hence nonzero. The actual full Toeplitz matrix is invertible for every n≥1. This does not rely on finite-degree tests, conjectured positive weights, or historical PASS labels.

## Interfaces still requiring separate review

Box-content pairing and equal-size inflation must be checked term by term in every positive/negative residue manuscript. Links between actual primitive V, factorial-normalized b, reversed U, Qhat, and final N/Z still use their respective complete construction proofs. The literature lemma does not replace those proofs.

If prime seed D or E vanishes, content congruence supplies neither unit status nor higher valuations. Congruences for actual numerator Pe+4Pa must retain Pa's factorial-versus-logarithm threshold, followed by actual removal of gcd(Z,N). This record does not infer an actual reduced denominator directly from a unit Schur cofactor.

This literature application supplies no irrationality conclusion for e+π. Finite certificates and actual parity-specific saddle amplitudes not yet personally checked remain in the review queue.
