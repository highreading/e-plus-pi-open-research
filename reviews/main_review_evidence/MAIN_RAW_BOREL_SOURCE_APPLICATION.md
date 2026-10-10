> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Verification of original-source conditions for the actual Borel–Legendre structure

Primary agent, October 4, 2026. This record supports the primary review of `work/session_20260913/raw_borel_legendre_literature.md`. It does not claim independent reproving of every complete source below.

The actual object is the coefficientwise transform F_k=Σ_d [t^d]Q_k·x^d/d! of the Rodrigues polynomial Q_k. The primary reviewer checked the two terminating hypergeometric expressions, generating function, fourth-order differential equation, and complete Green boundary form formula by formula. New exact controls begin from Rodrigues and cover orders 0–9 and 100 complete Green identities; they are finite supplementary evidence. The arbitrary-order root-preservation argument depends on the correct source conditions below.

## Root preservation and strict interlacing

[Specified Borcea–Brändén v6 original](https://arxiv.org/pdf/math/0606360v6), SHA-256 `25e17f5a41fa00306bc40836c00f395a4c03bdc0d032eece56d6799f3b9975f4`, 31 pages. The primary reviewer read complete §1 and viewed original PDF pages 4 and 5. Theorem 1.7(iv) requires T[(1+x)^N] to have real roots of the same sign for every nonnegative integer N. For multiplier 1/d!, this polynomial is exactly L_N(-x). Integration by parts in Laguerre Rodrigues gives orthogonality with positive weight on the positive half-line, so its N roots are positive and simple, satisfying the criterion.

Theorem 1.5 equates real-rootedness of all real linear combinations with interlacing. It applies to rotated consecutive Legendre polynomials and their Borel transforms. Strictness additionally uses the source's inverse-polynomial differential representation: each factor D-r has nonzero real r, and noninherited roots are determined by the strictly decreasing f'/f=r. A consecutive real pencil has root multiplicity at most 1 at zero, so every nonzero transformed pencil has no repeated roots. A common root would produce a nonzero pencil with a repeated root, which is impossible. The conclusion is strict interlacing on the imaginary axis.

This does not imply Chebyshev behavior of the actual high block on (0,1). The primary reviewer recomputed two complete collocation determinants at n4, two complete Wronskians at n5, and two interior-node configurations at n5, each pair with opposite signs. Continuity gives counterexamples to ordinary Chebyshev behavior; they close only shortcuts asserting all-index or all-odd-index validity.

## Scalar orthogonality and total positivity

The introduction of the [official Kwon–Littlejohn–Yoon research report](https://mathsci.kaist.ac.kr/bk21/morgue/research_report_pdf/04-21.pdf), PDF pages 1–5, was checked through a complete consecutive transcript from online reading of the official PDF. Direct original download with ordinary TLS remained unsuccessful; the transcript SHA is not represented as the PDF SHA. Theorems 1.1/1.2 explicitly begin with a quasi-definite orthogonal moment functional and its orthogonal polynomial sequence. A differential eigenvalue equation is not a sufficient hypothesis. The externally paraphrased proof is not adopted here.

The actual individual monic sequence already violates the three-term Favard recurrence at low order. Coefficient matching requires b3=-234/35, which would make the constant term of R4 equal to 156/35, while its actual value is 72/35. Thus no quasi-definite scalar moment functional makes the complete sequence orthogonal. A positive diagonal Sobolev construction is also excluded by strictly positive <F0,F2>. This argument does not classify nondiagonal or indefinite pairings.

[Published Díaz–Mainar–Rubio 2023 original](https://link.springer.com/content/pdf/10.1007/s10915-023-02323-1.pdf), SHA-256 `369216f128ad47f9099392a0cffbc83d9a4eb9b3351729234b6107d231222db5`, 27 pages. The primary reviewer read complete §4 and §5.3. The ordinary Bessel basis in §5.3 is Σ_j(i+j)!·t^j/[2^j(i-j)!j!], distinct from actual F_i. The actual coefficient matrix ordered by increasing degree and power has a -1/3 minor, so total nonnegativity of that Bessel coefficient matrix cannot be transferred directly.

Retain a weaker accurate fact: the general Theorem 4 allows any finite basis of increasing-degree polynomials with positive leading coefficients to be strictly totally positive on some sufficiently far-right interval. It is therefore inaccurate to say no total-positivity theorem applies. The interval threshold may depend on the entire finite basis, however. The theorem supplies neither the n-uniform threshold needed here nor an interval shifted to (0,1). Both finite actual high-block counterexamples remain consistent with that theorem.

## Multiple-Bessel moments agree, but the parameters are inadmissible

[Specified Mañas v2 original](https://arxiv.org/pdf/2608.00781v2), SHA-256 `a10f8698bc774351735afdd97a68c74270122800ffb50d940520d85156dd0f53`, 70 pages. The primary reviewer read complete §§3 and 6, all pairing/degree/weak-strong-normality definitions in §2.1, and the introduction's explicit limitation to algebraic decomposition without a positivity claim. Original PDF pages 7 and 45 were viewed. The latest version was not mixed with specified v2, and complete reproving of 70 pages is not claimed.

Definition 3.1 on PDF page 7 requires differences between distinct row parameters and between distinct column parameters to be nonintegral. The immediately following formula-admissibility convention excludes Gamma poles within this regular parameter domain; it does not revoke the noninteger-difference hypothesis.

Proposition 6.3 on PDF page 45 and its complete proof give, at q=1, moments L_j[z^d]=1/Γ(d+α_j+2). These match the actual factorial functionals with α_j=n-j, but actual parameter differences are integers and violate regularity. Orthogonality conditions in §2.1 use initial monomial blocks; this project additionally needs a bridge to the specified high Legendre block. Agreement of moments alone does not supply that bridge.

A resonant limit may retain some formulas, but a complete proof of rank, normalization, and high-block identification for this project is currently absent. General normality or positivity conclusions are therefore not transferred. The source also explicitly does not claim irrationality from these auxiliary identities.

## Complete quantities that continued research must retain

The primary reviewer checked arbitrary-order full rank, nonzero B(1), and actual reduced-denominator formula v2(q_n)=n+2floor((n+2)/4) for the original arctangent family. Distinct dyadic depths give distinct rational endpoints, so at most one remainder is zero. The positive kernel's uniform exponent is log(sqrt2-1), but the actual primitive form still satisfies

`log|L_n| = log q_n + n log(sqrt2-1) + log M_n + log theta_n + o(n)`。

M_n is the absolute integral mass of the specified normalized polynomial, and theta_n is its complete signed-cancellation ratio. Neither quantity nor the odd-prime part of q_n is controlled by the kernel estimate, imaginary-axis interlacing, or finite total positivity. They must remain in subsequent proofs and computations.
