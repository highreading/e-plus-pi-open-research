> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A concrete finite-depth closure proposal for the actual weighted core

This is a coordinator proof proposal to audit. Fix an integer r>=6. A deliberately
conservative possible sufficient domain is
v3(j)>=r-2, H>128(r+1)^2*3^(r-1)*D, h>=r+2.
The claim to prove is actual normalized radical Schur form Rrad in3^r,
not an unrestricted inverse valuation or an exact reduced denominator.
A1turn24's precision lemma, if retained, transfers a core proof at this depth
because the actual polynomial error has depth tau=v3(j)+2>=r.

Use common covering grid G=H/3^(r-1), odd. At a smaller effective precision
one may use coarser grids, all odd multiples of G. The proposed support modules
include local shifts of width w, where an explicit induction should keep
w<=4(r+1)(D+2), strictly less than G/8 on the proposed domain.

- Half-grid coefficient vectors: bands near ((2k+1)G-1)/2 with local shifts
  bounded by w, all intersected with finite HIGH[d,m].
- Integer-grid polynomial vectors: complete polynomials
  y^(kG+s)*(y-1)^D supported wholly inside HIGH, |s|<=w.
- Upper edge vectors: last w+1 HIGH coordinates.
- Lower edge vectors: first w+1 HIGH coordinates.

Do not infer closure just from these names. Prove the following operations
entrywise with coefficient valuations and finite truncations:

1. V is half-grid plus upper-edge. The explicit all-pole formula for V
   proves this at each effective precision. Its lower-edge entries vanish
   by extended direct annihilation, not merely by a macroscopic picture.
2. R maps a half-grid vector to sums of COMPLETE integer-grid polynomial
   vectors plus lower-edge vectors. For a single basis input e_b, the inverse
   series coefficients give, before intersection with HIGH, shifted copies
   y^(r1-b-kG)*(y-1)^D. Track each coefficient's precision. Centers strictly
   inside HIGH give complete copies. The only possible truncations are near
   integer center zero, since the upper boundary has half-grid center H/2;
   put these low truncations in the lower-edge module explicitly.
3. Actual F maps an internal integer-grid polynomial to half-grid plus
   upper-edge. Multiplication by B_A converts it to B_H times an integer-grid
   monomial. Every lower extraction then has a half-grid position, as does
   the top extraction after subtracting the integer-grid exponent.
   Prove X_U applied to such a polynomial is zero at the needed precision:
   its selected coefficient is a half-grid point, separated from integer
   support by at least G/2-w-D. This is what eliminates the actual LOW-unit
   projection, rather than omitting that projection by definition.
4. Actual F maps a lower-edge vector to half-grid plus upper-edge. Monic
   division of y^(d+s) by(y-1)^D produces quotient degree nu+s. Extended
   direct annihilation identifies the actual LOW projection with its degree
   <D remainder. The explicit Fe_d formula generalizes with that quotient.
   Quantify the shift-width increase at this operation.
5. R maps upper-edge to lower-edge exactly by its anti-triangular structure.
   R's integer-grid expansion cannot send an upper-edge input to a new
   interior half-grid band. Recheck the finite upper/lower boundary widths.

Then each retained Neumann walk
R, RFR, RF R F R, ... in (E0+3F)^-1 sends the right V^T into
integer-grid plus lower-edge modules. The left V annihilates those modules
by the grid gap, including all edge exceptions. Each closed contraction
vanishes modulo the required remaining precision. At most r-2 F factors
are needed because of the explicit3 cost in the inverse series.

Finally derive direct Z^TLZ,Z^TLU precision from the same half-grid gap,
and eliminate the LOW-force correction only after its exact depth is proved.
Give a complete inequality for all local shifts through these walks, and
retain every original cutoff pole: deleting a pole cannot create a new band,
but this observation does not replace endpoint subtraction or LOW projection.

If some stated operation is false, isolate the exact truncated polynomial
or projection that fails and derive the corrected module. A schematic grid
parity argument is insufficient; this note specifies the finite boundary
step whose previous absence blocked the induction.
