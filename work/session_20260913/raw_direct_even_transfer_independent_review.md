> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the direct even-degree transfer

Date: 2026-09-13. Reviewer: audit_sources.

Reviewed all of `raw_direct_even_degree_transfer.md` against the exact
gauge factorization, the original factorial-polynomial normalization,
the audited one-degree integral identities, and the now-proved even
cubic-degree gate. The substantive claims pass. Equation (12) needs
an explicit plus sign before `V_0(t)`; this transcription correction
has been reported to its author.

## 1. Direct rational transfer and infinity data

The factorization `Psi_n=K_n S G`, with S G independent of n, proves
the direct identity `T^[2]=K_(n+2) K_n^-1`. Its mixed Cramer
determinants have a common origin factor `z^(3n-1)`: the two old
remainder rows have that minimum order, while the new remainder jets
vanish even more deeply. Thus only Q_n remains in the denominator.
Replacing old row two leaves old derivative rows zero and one, whose
minimum remainder order is 3n, giving the extra z in the last numerator
column.

Increasing the new polynomial degree from n+1 to n+2 adds one to the
old mixed-degree bounds. The bottom-right bound needs, and correctly
uses, cancellation of the leading minor of the two old A,C rows zero
and one. This gives the displayed degree table `(6,7,7;5,6,6;4,5,5)`.
The determinant and differential compatibility identities follow with
the stated powers `z^6` and `Q_n^2`; no intermediate-degree matrix
or denominator enters.

On the current cubic stratum, the old Laurent plane contains a
degree-n branch. Its potentially excessive numerator degree n+6
gives `N_(0,6)+n N_(1,7)=0`. The exponential numerator has two
excessive degrees, n+7 and n+6. The possible first lower B coefficient
in the second equation multiplies the coefficient already set to zero
by the first. This verifies all three relations (7), and hence the
equivalent a,b,c relations (8), without an asymptotic coefficient ratio.

## 2. Factorial indexing, differentiation, and the exact operator

The common reversed-factorial reference is n+7. On the output side
the index difference is `n+7-(n+2+d)=5-d`, while on an input
coefficient B_k the denominator is `(n+7-d-k+j)!`. This gives exactly
`J^(7+j-d)(n-theta)_(underline j)` on the input side. The input
degree in this falling-factorial operator remains n.

There is no J^0 contribution after a_7=0. The only first-derivative
boundary terms are a_6 J and b_7 J(n-theta); evaluated at zero they
cancel as `(-n gamma+n gamma)P(0)`. Therefore precisely two
derivatives may be applied without losing constants. No unproved
boundary condition on the actual selected input is needed.

For the c terms, after these two derivatives the generic integral
power is `r=7-d`. The exact integration identity contributes

    (n+r)(n+r-1)J^r,
    -2(n+r-1)t J^(r-1),
    t^2 J^(r-2).

Reindexing these three pieces verifies respectively the c_(7-k),
c_(6-k), and c_(5-k) terms in (10). The a and b terms similarly
give their stated shifted indices. The r=0 and r=1 boundary cases
yield the displayed second-order differential operator; after the
three infinity cancellations it is exactly

    gamma L + delta t(t-1)D + V_0 + sum_(k=1)^6 V_k J^k.

The vanished constant c_0 follows from the last-column z factor and
eliminates V_7. The centered identity follows by inserting
`b_6=delta-2n gamma` into V_0; its constant and linear coupled terms
are `-n(n+1)gamma+n(1-2t)delta`, with the remaining quadratic W_0.

## 3. Norm criterion and the even subsequence

The inverse on the left is precisely the same cubic Volterra inverse
as in the audited one-degree note. Its norm bound remains a separate
hypothesis. For inputs in degree at most n, the Legendre spectral
bound, weighted derivative energy bound, multiplication norms and
`||J^k||<=1/k!` prove inequality (14) directly.

Under (16), each term is bounded by its stated constant times
`(n+1)(n+2)`. In particular
`(n+1)sqrt(n(n+1)) <= (n+1)(n+2)` and
`(n+1)^2 <= (n+1)(n+2)`. Thus the proposed uniform constant
`L(G+D/2+V)` is valid. Iterating directly over even n produces the
factor `(2m)!/2!`, multiplied by a constant to the m-1 power and the
fixed initial norm. This proves the conditional factorial estimate;
no unavailable odd transfer estimate has entered.

For the actual broad-band inputs, spectral projection yields
`||(L-n(n+1))P_n||=O(n^2/log n)||P_n||`: the top window has that
spectral width and the lower block is exponentially small. The
centered delta operator has norm O(n). Consequently the stated
relaxation `bar gamma=O(log n)` is valid under its remaining explicit
bounds. It applies to the selected family, rather than all degree-n
polynomials, as the source specifies.

## 4. Exact leading-minor quotients

Let the old and new algebraic Laurent top jets be `(a,a_1-c)` and
`(d,d_1-f)`. In `H C_new-C H_new`, the top two coefficients are
exactly m_0 and m_1: the two cross terms `-cf` and `+cf` cancel.
The next coefficient of `(B+B')` contributes n b m_0, and the
separate old-derivative term subtracts exactly that amount. Hence
the numerator's first two coefficients are `b m_0` and
`b m_1+B_(n,n-1)m_0`.

The term involving B_new and the old algebraic Wronskian begins two
degrees below the leading degree. Also D^2 has no relative inverse
linear term. Dividing by the exact current coefficient `Q_3=b Xi`
therefore proves (18), including its signs and normalization. The
quotients are defined at every even current index by the proved Xi
theorem. Their absolute-value bounds are not consequences of those
dyadic nonvanishing results.

This audit uses no new canonical samples or numerical scan. It proves
no unconditional transfer norm bound, no bound on accessory roots,
and no conclusion about the arithmetic nature of e+pi.
