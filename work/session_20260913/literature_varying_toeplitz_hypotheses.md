> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Primary Toeplitz asymptotic theorems and the actual varying symbol

Date: 2026-09-13. Targeted literature continuation by root.
This is a hypothesis audit, not an imported asymptotic theorem.

The actual even symbol is exp(z)|1+z^2|^(2m), with matrix size 2m+1.
Its two root exponents grow proportionally to the matrix size. The odd
symbol additionally changes sign. These features must be retained when
using literature on Fisher-Hartwig singularities.

[B. Fahs, Uniform Asymptotics of Toeplitz Determinants with
Fisher-Hartwig Singularities (2021)](https://link.springer.com/article/10.1007/s00220-021-03943-0):
read Introduction conditions (a)-(c), Theorem 1.1 and its preceding
discussion. The theorem treats nonnegative symbols with real analytic
background and controls moving singularity LOCATIONS. It does not
state uniformity for root exponents tending to infinity. Our exp(z)
background is complex on the circle, and our exponents grow. The
published location uniformity is therefore insufficient here.
Useful precedent: a Riemann-Hilbert treatment of the actual circle
polynomials and a determinant differential identity.

[Deift, Its and Krasovsky, Asymptotics of Toeplitz, Hankel, and
Toeplitz+Hankel determinants with Fisher-Hartwig singularities,
Annals of Mathematics 174 (2011)](https://annals.math.princeton.edu/wp-content/uploads/annals-v174-n2-p12-p.pdf):
read the introductory theorem discussion, Remark 1.6 on page 1246,
Remark 1.9, and the opening of the circle-polynomial section.
Complex weights are included, but the stated parameter uniformity
keeps alpha and beta in specified COMPACT sets. Alpha=m does not
remain in such a set. Eventual determinant nonvanishing for a fixed
symbol likewise does not prove nonvanishing along our changing symbols.
The project's all-index nonvanishing and sector bounds were proved
directly and do not depend on this unsupported substitution.

[Blackstone, Charlier and Lenells, Toeplitz determinants with a
one-cut regular potential and Fisher-Hartwig singularities I
(online 2023; volume 2024)](https://doi.org/10.1017/prm.2023.73):
read equations (1.2)-(1.10), Theorem 1.1 and its explicit uniformity
statement. The potential and background must be analytic near the
circle; the equilibrium density is required to be strictly positive
on the whole circle. Parameter uniformity is again on compact sets.
Absorbing our growing zeros into the potential produces a logarithmic
singularity at plus/minus i, violating that analytic hypothesis.
Leaving them as root exponents instead returns to the unbounded-
parameter issue. No equilibrium-density assertion for our symbol
has been established from this paper.

These are precise applicability obstructions, not claims that the
methods cannot be extended. A direct route remains the project's
explicit binomial base kernel, its complex perturbation and finite
boundary matrices. A literature extension would need quantitative
control for linearly growing root exponents, the actual complex or
signed background, and the particular endpoint/partial contour.
Ordinary fixed-parameter formulas do not supply that missing lemma.

Searches also returned varying Jacobi and circular singularity papers.
They have not been used as theorems here without a checked matching
specialization. No quoted passage or claimed review of their full
proofs is included.

