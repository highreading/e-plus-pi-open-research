> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the base ODE asymptotic and its two saddle sheets

Date: 2026-09-13. Reviewer: audit_computations.
Status: PASS on all substantive claims.
Target: raw_base_polynomial_uniform_asymptotic.md, in full.

The finite coefficient formula from the circular-binomial note gives
(-m)_j(m)_j/[(-2m)_j j!] through j=m. The denominator does not vanish
in that finite range. Comparing consecutive coefficients proves the
displayed ODE, including the coefficient -2m-w and f_m'(0)=m/2.
There is no use of a nonterminating hypergeometric definition with
an invalid lower parameter.

The previous positive-measure extremal argument excludes all zeros
from the closed unit disk. The reciprocal root sum therefore bounds
f_m'/(mf_m) by 1/(1-|w|). Cauchy estimates give uniform derivative
bounds on smaller disks. Subsequence compactness, the limiting
quadratic equation, and the value 1/2 at zero select exactly
r=1/(1+sqrt(1-w+w^2)). The discriminant has no disk zeros, and its
chosen square root cannot equal -1 there. Analytic continuation
therefore selects the same branch on the entire open disk.

I checked the subtraction identity (4) and its sign independently.
The denominator converges to -2sqrt(Delta), uniformly separated
from zero on every compact subdisk. This yields delta_m=O(1/m).
Applying Cauchy to that already uniform estimate gives
delta_m'=O(1/m) on smaller compact sets. Expanding the same equation
then gives

    h=(A r'-w r)/(2sqrt(Delta)),
    r_m=r+h/m+O(1/m^2).

Thus the transport correction is justified with the correct sign,
and is not a formal coefficient match without a remainder estimate.
Integration of the normalized analytic logarithm and exponentiation
give the claimed uniform relative O(1/m) error for the explicit
base factor. Derivative expansions follow on smaller compacts.

The actual factor R_n has a uniformly bounded analytic logarithm
only on the previously proved zero-free subdisks below cos(1).
The target keeps that restriction in its normalized logarithmic
limit. Its multiplicative formula on larger compact subdisks is
still exact in scope: the relative error belongs to the base factor,
so the formula does not divide by a potentially zero R_n. The
exterior formula correctly uses formal reversal of degree n,
including degree defects, and only evaluates its Hardy multiplier
inside the unit disk.

For the interior saddle, the rational part of H_in' is
-(z^3+3z-2)/[z(1+z^2)(z-1)]. Eliminating the square root gives
the stated factor -2z(1+z^2)(z^2+z-1), after excluding the
denominator zeros. Direct substitution retains the positive golden
candidate and rejects the negative one on this sheet. A path through
the positive candidate is in a different homology class from the
left contour unless the residue at zero is included.

The exterior derivative is different because formal reversal adds
the factor z^n. Its displayed square-root term and sign are correct.
At z=-phi, substitution using rho=1/phi and rho^2+rho=1 gives
an exact zero. The target correctly leaves contour dominance,
endpoint estimates, and the nonzero actual multiplier unproved.

For further exact checks, my companion saddle note derives

    H_out''(-phi)=(25-11sqrt(5))/4>0,
    exp(2H_out(-phi))=27rho^5/4,

using the same branch normalization. These are consistent with
the target's formulas. No new canonical degree or root scan was
used in this review.

No correction was required.
