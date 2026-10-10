> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Route 1 targeted literature note after Items 259--265

Checked: 2026-08-31 (Beijing time)

## 1. Scope and strict conclusion

This is a targeted, primary-source literature check for the two live closer
questions:

1. weighted zero density for the moving incomplete-beta / punctured elliptic
   gate in the fixed $j=2$ cell; and
2. a high-singleton squarefull bound for the fixed beta denominator.

It is not an exhaustive bibliography and makes no novelty claim.  The search
found close frameworks for incomplete hypergeometric systems, Dwork
Frobenius, Picard 1-motives, finite-field hypergeometric distributions, and
large sieves.  It did not locate a theorem whose hypotheses directly imply
either Route-1 closer target for the actual moving family.  Absence from this
targeted search is not evidence that no such theorem exists.

## 2. Adjacent results and exact applicability

### Incomplete hypergeometric structure

Nishiyama and Takayama,
[Incomplete A-Hypergeometric Systems](https://arxiv.org/abs/0907.0745),
prove holonomicity and contiguity relations for incomplete beta and related
integrals.  This supports the archive's endpoint-retaining affine viewpoint:
an incomplete integral has an inhomogeneous boundary term and is not merely a
complete cycle period.  It supplies no mod-$p$ weighted zero-density theorem
for a cutoff and character that move with $p$.

Adolphson and Sperber,
[The Dwork-Frobenius operator on hypergeometric series](https://arxiv.org/abs/2204.09814),
construct Frobenius actions on hypergeometric and $A$-hypergeometric series
and prove integrality/eigenvector-type results.  This is the right broad
language for a Frobenius lift, but the archived target is an incomplete
endpoint functional on an open curve.  Before this theory can affect the
ledger, one must exhibit the actual full affine gate as a coordinate of the
relevant fixed filtered $F$-crystal or 1-motive and then prove a horizontal
zero-density theorem for that coordinate.

### Central-binomial and finite-field identities

Mattarei,
[Asymptotics of partial sums of central binomial coefficients and Catalan numbers](https://arxiv.org/abs/0906.4290),
gives closed forms over finite fields for full truncated generating
polynomials.  Mattarei and Tauraso,
[Congruences for central binomial sums and finite polylogarithms](https://arxiv.org/abs/1012.1308),
derive polynomial identities and congruences for several complete
central-binomial sums.  These identities are useful for independent
normalization checks, but they do not remove the moving cutoff
$k=s-1$ or the second affine condition of Item 251.

Z.-H. Sun,
[Congruences concerning Legendre polynomials III](https://arxiv.org/abs/1012.4234),
relates certain $\lfloor p/6\rfloor$-truncated *product-weighted*
hypergeometric sums to elliptic character sums.  The archived $H_m$ is the
plain incomplete central-binomial prefix, and Items 254 and 260--263 prove
that the unweighted compact elliptic trace omits the nonzero-residue
logarithmic coordinate.  The cited theorem therefore cannot be substituted
for the actual gate.

Ono, Saad, and Saikia,
[Distribution of values of Gaussian hypergeometric functions](https://arxiv.org/abs/2108.09560),
prove value-distribution theorems for natural finite-field hypergeometric
families as the field parameter varies.  Their setting does not directly
cover one prime-tied cutoff with a character of growing order and an
endpoint rational weight.  A usable transfer would require an explicit
sheaf/family identification and a theorem uniform in this horizontal
specialization.

### Open curves and 1-motives

Andreatta and Barbieri Viale,
[Crystalline realizations of 1-motives](https://arxiv.org/abs/math/0302161),
identify one-dimensional crystalline cohomology with the crystalline
realization of the cohomological Picard 1-motive and compare it with de Rham
realizations.  This supports treating the punctured logarithmic coordinate as
a mixed extension rather than as an ordinary compact trace.

Mohajer and Sebbar,
[P-adic Period Conjectures for 1-motives: Integration and Linear Relations](https://arxiv.org/abs/2507.15020),
develop $p$-adic integration and period structures for 1-motives.  Their
linear-relation framework is conceptually adjacent, but it does not state the
prime-by-prime weighted zero-density theorem required here.  The immediate
archive task is therefore exact recognition of the divisor, extension
coordinate, and endpoint functional before any distribution claim.

### Sieve and Wieferich-type warnings

Kowalski,
[The principle of the large sieve](https://arxiv.org/abs/math/0610021),
gives an abstract large-sieve framework with applications to Frobenius
families and divisibility sequences.  The applications require a suitable
family, monodromy/independence input, and a large-sieve constant.  None of
those inputs has yet been proved for the actual moving punctured coordinate
or for the high-singleton beta denominator.

Silverman's
[Wieferich's criterion and the abc-conjecture](https://doi.org/10.1016/0022-314X(88)90019-4)
shows that non-Wieferich questions for infinite-order points on $j=0$ and
$j=1728$ elliptic curves are naturally deep and, in that result,
$abc$-conditional.  This is a warning about the likely arithmetic depth of
an elliptic-logarithmic interpretation.  It is **not** evidence that the
Item-251 gate is equivalent to an elliptic Wieferich condition; such an
equivalence remains to be proved or rejected.

### Padé denominators and the beta high-singleton barrier

Cullinan and Scheel,
[On the arithmetic of Padé approximants to the exponential
function](https://arxiv.org/abs/2007.01329), identify exponential Padé
polynomials with generalized Laguerre polynomials and prove
irreducibility/Galois-group results by Newton polygons.  This confirms that
the beta continuants belong to a well-developed arithmetic Padé family, but
their theorems concern the polynomial in its argument.  They do not bound
the vertical valuation of the distinguished integer specialization
$q_N=A_N(-1)$, and a simple root modulo $p$ does not prevent
$p^2\mid A_N(-1)$.

Mezzarobba and Salvy,
[Effective Bounds for P-Recursive
Sequences](https://arxiv.org/abs/0904.2452), give effective complex-size
bounds for sequences satisfying polynomial-coefficient recurrences.  In the
present recurrence those methods recover the correct factorial/exponential
height scale, but they do not give a uniform $p$-adic valuation bound.
Likewise, Medina, Moll, and Rowland,
[The valuation of polynomial
sequences](https://www.math.tulane.edu/~vhm/papers_html/valpol.pdf), analyze
$v_p(Q(n))$ for one fixed polynomial $Q$.  Here the reverse-Bessel
polynomial $A_N$ changes with $N$, so that theorem cannot be applied as a
uniform high-singleton estimate.

Thus the targeted literature check supplies no implication of
$\log\operatorname{sqfull}(q_N)=o(N\log N)$.  This is an applicability
statement, not a claim that no relevant theorem exists.

## 3. Research decision

The literature check supports the following order.

1. Prove the exact Picard-1-motive/generalized-Jacobian realization of
   $(H_q,h_q)$, including the non-descending endpoint functional.
2. Determine whether the *full actual affine gate*, not merely the prefix,
   is a fixed Frobenius extension condition or still uses a vector/function
   moving with $r$.
3. Only if a fixed arithmetic condition results, identify the precise
   monodromy or Galois representation needed by a horizontal sieve.
4. Keep the beta high-singleton problem separate: support or pairwise-gcd
   theorems do not control singleton multiplicity.

No cited result changes the booked rate, the retained common-log ceilings, or
the Route-1 decision.  Route 1 remains ACTIVE and Route 2 remains QUEUED.

## 4. Strict labels

- **PROVED FROM CITED SOURCES:** only the general frameworks and results
  explicitly attributed above.
- **PROVED IN THE ARCHIVE:** the applicability/non-applicability statements
  that follow from the exact forms in Items 251, 254, and 259--265.
- **OPEN:** any horizontal weighted zero-density theorem, any actual
  elliptic-Wieferich equivalence, and the beta high-singleton squarefull
  bound.
- **BOOKING:** zero new rate and zero capacity reduction.

## 5. Addendum after Items 281--284 (2026-08-31)

Hanson, Vaughan, and Zhang,
[The Least Number with Prescribed Legendre
Symbols](https://arxiv.org/abs/1605.05584), study how small an integer can
be while realizing a prescribed vector of Legendre symbols at all primes
dividing a squarefree modulus.  Their theorems are average/eligibility results
with explicit local obstructions; they do not state a uniform bound for every
deterministic moving product



$$
B_M=\prod_{p\in\mathcal S_M}p
$$



arising in Item 284.  Consequently they do not presently imply
$\log\lambda_M=o(M)$ for the least simultaneous nonresidue in that item.
More importantly, Item 284 proves that even such a subexponential coefficient
would leave the inherited absolute-height ratio at $H/2>1/6$.  The cited
paper may sharpen coefficient construction, but it cannot by itself change
the fixed-$j=1$ capacity ledger.

Kowalski,
[The large sieve, monodromy and zeta functions of
curves](https://arxiv.org/abs/math/0503714), proves a Frobenius large sieve
for algebraic families under compatible-sheaf, monodromy/linear-disjointness,
and uniform cohomological-complexity hypotheses.  This is the right kind of
framework for a weighted exceptional-set theorem, but the archive has not
constructed those inputs for the actual tied $(M,p)$ gate.  In particular,
the gate changes characteristic with the row, retains an external arithmetic
state/endpoint functional, and Items 267, 269, and 271 do not produce one
fixed bounded-conductor lisse family with the required monodromy.  Therefore
the Frobenius sieve is not currently applicable merely from the exact CRT norm
or the translation-difference module.

The next literature-sensitive task is precise rather than heuristic: either
construct the compatible sheaf and prove its monodromy and conductor bounds,
or prove that the currently available finite module cannot supply those data.
No cited theorem changes the booking or retained ceiling.
