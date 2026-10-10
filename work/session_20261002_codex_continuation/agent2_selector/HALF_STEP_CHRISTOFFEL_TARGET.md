> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Structural positivity target for the half-step output determinant

2026-10-02. Original research continuation, following the completed uniform half-step block theorem. The remaining stronger target is an exact Casoratian or positive Christoffel/Gram representation of det O_n(h), or a regular recurrence which selects from a constant number of shifts uniformly in n=4k. No all-n representation has yet been identified.

## Search before pursuing this representation

Archive search: `Christoffel`, `Darboux`, `Gram determinant`, `sum of squares`, `conjugate.*Casorat`, and `Casorat.*conjugate` over `sources` and the preceding session. Read `agent1/FIXED_WEIGHT_CHRISTOFFEL_RESEARCH.md` §§1–3. It establishes a different fixed-weight t transform of complex-segment Legendre polynomials, signed norms and second-kind formulas. Its warning that complex bilinear norms are not positive is relevant. Its actual contact and center quantities are different from the present half-step output; no direct transfer is made. Other archive hits concern unrelated Bessel/Darboux exclusion and coupled Gram identities.

Online paper searches: `orthogonal polynomials Christoffel transformation complex conjugate roots determinant positivity Casorati paper`; `Darboux transformation discrete orthogonal polynomials Casorati determinant positivity complex conjugate Christoffel`; `Christoffel transform complex conjugate zeros positive measure orthogonal polynomials arxiv`; `Christoffel transformations complex parameters orthogonal polynomials sum squares`.

Opened relevant primary full texts:

- G. Ariznabarreta and M. Mañas, *Darboux transformations for multivariate orthogonal polynomials*, https://arxiv.org/pdf/1503.04786, §2, especially Definition 2.1 and the subsequent requirement that the transformed polynomial be positive on the original support, with nonsingular moment matrices. The browser's metadata title was different, but the PDF's actual first-page title identifies the paper.
- R. Kozhan and M. Vaktnäs, *Christoffel Transform and Multiple Orthogonal Polynomials*, https://arxiv.org/pdf/2407.13946, introduction and its discussion of positivity and normality. These hypotheses must be established for an actual measure before a determinant formula can prove this target.
- S. Odake, *New finite-type multi-indexed orthogonal polynomials obtained from state-adding Darboux transformations*, opened publisher full text https://academic.oup.com/ptep/article/2023/7/073A01/7218584. The displayed multi-step Casoratian identities are structural background, not a present nonvanishing theorem.
- NIST DLMF §18.2(v), https://dlmf.nist.gov/18.2, opened the Christoffel–Darboux kernel and sum-of-products formula. With a positive measure, evaluation at conjugate points makes a kernel sum of absolute squares; the positive-measure identification is exactly the missing obligation here.

Overlap is the classical Christoffel/Darboux determinant mechanism. New work would be an identity for the ACTUAL polynomial kernel -2^(-n-1)wV^(n/2)R_n and output O_n(h), with every endpoint term retained. Merely placing two complex-conjugate symbols in a determinant does not prove a positive measure or a positive Gram determinant. No novelty beyond the eventual actual-family identity is asserted.

## Current structural data and next exact derivation

The three-output det is regular and nonzero for all h≥0 at n=4,8 by exact Sturm calculations. Its numerator degrees are 2n in those cases; this remains a pattern rather than a uniform theorem. The positive complete-period output supplies one column but leaves two coupled endpoint columns. The positive-root mesh of u_n(h) gives no generic binomial-transform real-rootedness conclusion.

The next exact derivation uses the all-integer-selector moment recurrence. In the polynomial-total-derivative reduction, replacing the old exponent 2m by h and selector square q² by z=−q halves the polynomial shift degree. This may expose a simpler quotient or Darboux identity. Every claimed recurrence must have zero full-contour endpoint flux, a regular leading coefficient, and actual U as its killed mode; a generic holonomic closure alone will not settle det O_n.
