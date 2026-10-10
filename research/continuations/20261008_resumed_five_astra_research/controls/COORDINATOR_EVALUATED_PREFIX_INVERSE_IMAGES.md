> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Evaluated leading finite prefix inverse images

Status: exact bounded constant evaluation and elementary coefficient
deduction from A1turn9 Section7.2. The full source-specific prefix theorem
is still awaiting a DIFFERENT external independent proof audit. The parent
has read the entire report and its new122-constant receipt PASSES.
No physical7 source jet or global primitive content is evaluated here.

## 1. Reuse and constant provenance

The newly checked D_j have ternary valuation0 ONLY at
j27,54,108. Their complete modulo27 residues are respectively5,1,23,
so their reductions modulo3 are2,1,2. All other j1..122 constants
have positive ternary valuation. The full exact-rational receipt combines
the high and3-weighted low products before reduction. This is new coefficient
arithmetic, with maximum odd factor1027, not an original dense matrix or
a repetition of the earlier source-moment/sector checks.

The finite inverse-image formula in A1turn9 is
C_r=sum_(j=1)^13 a_(9j) [Y^(r+9j-122)](1-Y)^(-25), 0<=r<=121.
The formula is source-specific; it is quoted here pending its separate
full proof audit. The following evaluation, GIVEN that formula, is exact.

## 2. Evaluate all finite coefficients

In F3[[Y]], (1-Y)^(-25)=(1-Y)^2/(1-Y^27).
Its coefficient at n>=0 is1 precisely when n mod27 is0,1,2, and zero
otherwise. A negative index has coefficient0.
Only the three stated a_j therefore enter:

C_r=2 f_(r-95)+ f_(r-68)+2 f_(r-14),
f_n=[Y^n](1-Y)^2/(1-Y^27).

Restricting to the ACTUAL finite range0<=r<=121 gives

 C_r=2 for r in{14,15,16,41,42,43,95,96,97},
 C_r=0 for every other r in0..121.

At r68..70 the two admitted coefficients1+2 cancel. The nonexistent
r122..124 block is not introduced by an infinite-series substitution.
Consequently the actual finite polynomial is explicitly

 C(Y)=2Y^14(1-Y)^2(1+Y^27+Y^81) in F3[Y].

Its degree97 is strictly below121. Its endpoint is C(-1)=1 in F3.
This endpoint refers to the prefix inverse-image polynomial, not the
endpoint of the whole retained amplitude or final force.

## 3. Consequence for the precise next prefix transport obligation

In A1turn9 notation the actual leading finite inverse-image column is

 Z_(0,H_i)(y)=y^i(1-y)^eta C(y^P),

with eta0 in RangesI--II, eta=t=Pi-2chi in RangeIII, and all coefficients
under the admitted original degree/prefix bounds. Thus its large-grid
support now consists of NINE explicitly evaluated blocks, with all
small integer binomial coefficients reduced at their correctly leading
precision. This does not replace the higher integer digits needed for
a physical6/7 numerator calculation.

The proven formal prefix transport identity remains

 P_(7,act)-P_(7,core)=-Z_(0,H)^T Delta_A Z_(0,H) mod3,
 Delta_A=(A_act-A_core)/27 mod3.

The unknown actual producer jet Delta_A is still essential. This note
evaluates the inverse images on which it must be tested; it does not
assign that jet or its contraction zero. Physical5 complementary returns,
higher endpoint adaptation and source34 requirements for OTHER terms
remain distinct. No final-q or whole-error improvement is claimed.
