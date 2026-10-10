> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Literature status and theorem audit

Checked: 2026-08-31 UTC

## Current status

The 2026-08-31 targeted recheck found no accepted proof of irrationality or
transcendence of $e+\pi$.  The current primary sources below still describe
the problem as open; the claimed solutions listed later remain unusable for
the stated proof defects.

- Runlong Yu, *Tail Criteria, No-Go Audits, and Apéry-Type Certificate
  Obstructions for the Irrationality of e+pi*, arXiv:2606.17303v1 (2026),
  explicitly states that even irrationality remains open and audits several
  bounded low-complexity methods.
  - Abstract: https://arxiv.org/abs/2606.17303
  - HTML: https://arxiv.org/html/2606.17303
- Michel Waldschmidt's survey *Transcendence of Periods: The State of the Art*
  explicitly lists $e+\pi$ and $e\pi$ as not known (PDF page 79, with the
  surrounding discussion repeated on pages 80--82):
  https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/TNT2013.pdf.
- Runlong Yu, *Computer-Assisted Diagonal Hermite--Padé Normality via
  239-Adic Discrete Convexity* (University of Alabama repository, July 2026),
  reports a computer-assisted proof of sharp diagonal type-I normality through
  degree 1,087,602,879 for $1,e^z,G(z)$, where
  $G(z)=16\arctan(z/5)-4\arctan(z/239)$ and $G(1)=\pi$. It expressly does
  not prove an arithmetic statement about $1,e,\pi$: denominator and height
  control, plus small provably nonzero evaluated forms, remain untreated. This
  archive checked the preprint's theorem statement and scope but did not rerun
  its roughly 36-billion-inequality external certificate.
  https://ir.ua.edu/items/[session identifier removed]

## Unconditional tools and their limits

1. **Hermite--Lindemann / Lindemann--Weierstrass.** If distinct algebraic
   numbers alpha_j are used as exponents, their exponentials are linearly
   independent over the algebraic numbers. It does not apply when the needed
   exponent is e or pi.
2. **Gelfond--Schneider.** If alpha is algebraic, alpha != 0,1, and beta is
   algebraic irrational, every value of alpha^beta is transcendental. It proves
   e^pi = (-1)^(-i) transcendental but does not apply to e+pi.
3. **Baker's theorem.** Controls nonzero linear forms in logarithms of algebraic
   numbers. The number e is not known to be a logarithm of an algebraic number,
   so the relation e+pi=s cannot be put wholly inside its hypotheses.
4. **Nesterenko's modular theorem.** In particular, pi and e^pi are
   algebraically independent. If s=e+pi were algebraic, this would imply that e
   and e^pi are algebraically independent after the algebraic translation
   e=s-pi; it gives no contradiction.
5. **Six exponentials theorem.** Its conclusion that at least one exponential
   in a suitable 2-by-3 array is transcendental is too weak here: the natural
   arrays already contain known transcendental entries such as e.
6. **Schanuel's conjecture.** Applied to 1 and i*pi, it predicts algebraic
   independence of e and pi and therefore transcendence of e+pi. This is
   conditional and points opposite to algebraicity.

## The mixed E-value/G-value frontier

Let **E** be the ring of values of Siegel E-functions at algebraic points and
**G** the corresponding ring for analytic continuations of G-functions.  The
standard conjecture



$$
\mathbf E\cap\mathbf G=\overline{\mathbb Q}
$$



is explicitly described as currently out of reach by Fischler and Rivoal,
*Relations between values of arithmetic Gevrey series, and applications to
values of the Gamma function*, J. Number Theory 261 (2024), 36--54,
https://doi.org/10.1016/j.jnt.2024.02.016 (preprint:
https://arxiv.org/abs/2301.13518).  An Oberwolfach report records that only the
trivial inclusion from right to left is known:
https://ems.press/content/serial-article-files/46625?nt=1.

This conjecture would settle the present problem in the transcendental
direction. Indeed, $e\in\mathbf E$, $\pi\in\mathbf G$, and both rings
contain the algebraic numbers. If $s=e+\pi$ were algebraic, then
$\pi=s-e\in\mathbf E$ and $e=s-\pi\in\mathbf G$, placing the known
transcendental numbers $e$ and $\pi$ in the intersection.

The 2025 papers by Daniel Vargas-Montoya (arXiv:2502.00768 and
arXiv:2507.20429) do not supply the missing specialization theorem.  They give
functional p-adic algebraic-independence criteria over a field of analytic
elements, under strong Frobenius and maximal-order-multiplicity hypotheses.
Their exponential example is $\exp(\pi_p z)$ with a Dwork constant $\pi_p$,
not the complex E-function $e^z$, and no result transfers mixed functional
independence of $e^z$ and $\arctan z$ to algebraic independence of their
complex values at $z=1$.

## Higher-prime-power Cartier/Dwork literature checked for item 160

The following primary sources provide relevant candidate machinery:

- Anton Mellit and Masha Vlasenko, *Dwork's congruences for the constant
  terms of powers of a Laurent polynomial*, proves congruences modulo prime
  powers for a specific constant-term sequence:
  https://arxiv.org/abs/1306.5811.
- Masha Vlasenko, *Higher Hasse--Witt matrices*, develops higher matrices and
  $p$-adic limit formulas; the advertised Frobenius/unit-root limit
  construction uses an invertible Hasse--Witt operation:
  https://arxiv.org/abs/1605.06440.
- Alexander Varchenko and Wadim Zudilin, *Congruences for Hasse--Witt matrices
  and solutions of $p$-adic KZ equations*, proves Dwork-type congruences for
  tuples of Laurent polynomials:
  https://arxiv.org/abs/2108.12679.
- Éric Delaygue, Tanguy Rivoal, and Julien Roques, *On Dwork's $p$-adic
  formal congruences theorem and hypergeometric mirror maps*, generalizes
  formal congruences for globally bounded hypergeometric series:
  https://arxiv.org/abs/1309.5902.

These results do not directly supply item 160's missing lift.  The matrix
selected by the present rank-two endpoint comparison is singular precisely on
the content locus where a second digit is sought, so an inversion-based
application is unavailable there.  More importantly, the archive has no
theorem identifying that selected comparison matrix with the ambient
Hasse--Witt operator of a smooth proper family or with an integral
Frobenius-stable lattice.  The separable pole polynomial
$\operatorname{disc}Q=-16$ does not itself degenerate at the relevant odd
primes.

Accordingly, higher Hasse--Witt, Dwork, or Witt-vector machinery remains an
**OPEN candidate**, not an applied theorem and not a route-wide no-go.
No source in this targeted search supplied the specific lifted relative
endpoint digit formula needed here; this is a scope statement, not a claim of
novelty.

## Finite-logarithm and incomplete-beta literature checked for Items 217--221

The fixed $j=1,2$ common-log cells reduce to moving weighted finite-logarithm
or incomplete-beta periods.  A targeted primary-source check found useful
machinery but no theorem that proves the required simultaneous nonvanishing:

- Amnon Besser, *Finite and p-adic polylogarithms*, proves the finite
  polylogarithm framework and functional equations used by the archive.  It
  does not give nonvanishing for coefficient functionals whose polynomial
  weight and extraction index both move with $(p,s)$:
  https://arxiv.org/abs/math/0006051.
- Björn Grohmann, *On the Zeros of Fermat Quotients and Mirimanoff
  Polynomials*, studies zeros of the ordinary finite logarithm and relates them
  to Fermat quotients.  The paper illustrates that even much more specialized
  simultaneous Fermat-quotient zero questions are delicate; it supplies no
  exclusion for the present weighted periods:
  https://arxiv.org/abs/math/0604427.
- Kenta Nishiyama and Nobuki Takayama, *Incomplete A-Hypergeometric Systems*,
  proves holonomicity and inhomogeneous contiguity machinery for incomplete
  beta integrals.  Holonomicity alone is not a finite-field nonvanishing
  theorem, and the boundary term is exactly the feature retained by the
  present fixed-cell obstruction:
  https://arxiv.org/abs/0907.0745.
- Frits Beukers, Henri Cohen, and Anton Mellit, *Finite hypergeometric
  functions*, develops complete finite-field hypergeometric sums as Frobenius
  traces.  The Item-219 sums are incomplete moving endpoint periods, so no
  direct trace nonvanishing consequence was found:
  https://arxiv.org/abs/1505.02900.

Accordingly, finite-polylogarithm functional equations, incomplete
hypergeometric contiguity, and finite hypergeometric trace theory remain
**OPEN candidate machinery**.  The statement above records the scope of the
targeted search; it is not a novelty claim and not a proof that no applicable
theorem exists under another formulation.

## Exponential periods

Fresán and Jossen's exponential period conjecture would also settle the
problem in the transcendental direction. If $\mathcal P$ is the field generated by
ordinary periods, then $\pi$ belongs to $\mathcal P$. Their Proposition 12.1.4 says,
conditionally on the conjecture, that the exponential of every nonzero
algebraic number is transcendental over $\mathcal P$. In particular,
$e=\exp(1)$ would be transcendental over $\mathcal P$. But algebraicity of
$e+\pi$ would put $e=(e+\pi)-\pi$ inside $\mathcal P$, a contradiction.

- Javier Fresán and Peter Jossen, *Exponential motives*, Conjectures 1.3.2
  and 8.2.6 and Proposition 12.1.4:
  https://javier.fresan.perso.math.cnrs.fr/expmot.pdf
- Johan Commelin, Philipp Habegger, and Annette Huber, *Exponential periods
  and o-minimality*, arXiv:2007.08280.  Their comparison results do not prove
  the exponential period conjecture:
  https://arxiv.org/abs/2007.08280

Ben Snodgrass, *Periods of E-operators*, arXiv:2608.06005 (6 August 2026),
introduces a larger ring of $E$-periods using rapid-decay cohomology.  It
places both $E$-values and exponential periods inside that common framework,
but proves no injectivity or transcendence theorem for the associated period
pairing.  Its conclusion explicitly leaves the relation among $E$-values,
exponential periods, and the new ring as a topic for future work.  Thus the
paper supplies a useful categorical setting for the mixed $e$--$\pi$
question, not the missing arithmetic separation:
https://arxiv.org/abs/2608.06005

## Rejected claimed solutions

### Carella, arXiv:1706.08394

This manuscript claims that $e\pi$ is irrational and explicitly leaves
$e+\pi$ open. It is not an accepted resolution of even the product claim. The
central denominator-synchronization Lemma 3.1 is not proved:

- it assumes, without justification, a subsequence of partial quotients of pi
  satisfying a prescribed asymptotic size;
- it infers infinitely many denominator correlations from the existence of a
  single denominator in an interval;
- its cases impose polynomial-in-index growth conditions on the partial
  quotients of pi that are not known and are not exhaustive.

Consequently the choice required in equation (4.5) is unsupported, so the
contradiction in (4.8) does not follow.

### Carella, arXiv:2007.15000v3 (revised 14 April 2026)

This manuscript claims that $1,e,\pi$ are linearly independent and that
$e+\pi$ is transcendental. It contains several immediate fatal errors.

1. Theorem 4.1 says that $\alpha+\pi$ is irrational for every positive
   irrational $\alpha$. Taking $\alpha=4-\pi>0$ gives the rational sum 4.
2. Inside the contradiction hypothesis $\alpha+\pi=A/B$, the paper states
   that $|\sin(A-B\alpha)|>0$.  But the same hypothesis gives
   $A-B\alpha=B\pi$, so this sine is exactly zero. The asserted inequality
   therefore starts from a false premise.
3. In its purported transcendence argument, it invokes a “minimal polynomial”
   of a number it has assumed to be transcendental and then treats the
   resulting nonexistent polynomial as a contradiction.

The HTML title page is dated 24 August 2026, although the arXiv submission
history lists 14 April 2026 as the latest revision. The current HTML text
exposes all three errors directly:
https://arxiv.org/html/2007.15000.  This manuscript is not evidence that the
problem has been solved.

### Foukzon, arXiv:0907.0467

This manuscript claims irrationality of e+pi and e*pi using a proposed
nonstandard extension of transcendence theory. The claimed conclusions remain
listed as open in current specialist sources, and no accepted independent
verification of the paper's new transfer/generalization principles was found.
It cannot be used as a theorem without first proving those principles in an
accepted foundational system.

### Web/database claims

Several web databases propagate Carella's result as a theorem. An arXiv posting
or database entry is not a verification channel; the actual proof hypotheses
must be audited.
