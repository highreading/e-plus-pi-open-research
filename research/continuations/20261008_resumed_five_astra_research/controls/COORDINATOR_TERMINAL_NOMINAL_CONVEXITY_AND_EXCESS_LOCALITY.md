> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact convexity and excess locality for the terminal nominal payment

Coordinator derivation, 9 October 2026. NEW parent proof; DIFFERENT audit
pending. It concerns the explicit terminal THETA nominal cost from FULL
A2turn14. It does not evaluate a surviving terminal digit or claim an
upper bound for either complete coefficient or their gcd.

Before deriving it, scoped current/Desktop MD/TEX searches for terminal
convexity, the exact second difference, and nominal minimizer monotonicity
recover no earlier terminal-specific theorem in that scope. The DIFFERENT
passed first-mixed ETA cost monotonicity is REUSE, with its own distinct
shifted indices. Standard binary digit/Legendre identities are REUSE; no
external result beyond those elementary identities is imported. The new
consequence is for the already fully read actual terminal cost and its
complete near-minimum product-count bookkeeping.

## 1. Retained domain and input

Keep ORIGINAL k=9^(18+32u), d=k-1, physical terminal3d+1, both complete
coefficient borders, and A2turn14's exact paired coefficient identities.
Write s(n)=s_2(n), and let L_p be the actual nominal terminal payment
defined there by

    L_p=(d+2-p)L_d+c_p+2E_p+B_p(d)
                       +sum_{j=p}^{d+1}(j+v_2(j!)).

This is a lower payment with odd Cauchy, factorial-adjugate, source and
jet prefactors retained. FULL A2turn14 gives the exact difference

    Delta_p=L_(p+1)-L_p
           =8p-2d+5-s(p)+2s(d-p-1)-s(d+p-1).       (1)

Its complete first-layer THETA cancellation is established at the stated
scope3<=p<=floor(d/3), subject to DIFFERENT A4turn24 audit. No inference
below turns that zero leading layer into an attained valuation.

## 2. Exact second difference

For1<=p<=d-2, all integer arguments of the following valuations are
positive. Use the exact digit identities

    s(n+1)-s(n)=1-v_2(n+1),
    s(n-1)-s(n)=-1+v_2(n).

Subtract (1) at p from (1) at p+1. This gives

    Delta_(p+1)-Delta_p
       =4+v_2(p+1)+2v_2(d-p-1)+v_2(d+p) >=4.       (2)

Every sign and shift is essential. In particular the argument d-p-1
belongs to the terminal cost; replacing it by d-p would import the
different earlier ETA first-mixed problem. Formula(2) is exact and proves
strict discrete convexity of this nominal terminal sequence.

## 3. All nominal minimizers and every equality tie

In any interval containing a negative and a nonnegative Delta, let

    p_* = min{p:Delta_p>=0}.

Then Delta_(p_*-1)<0 and Delta_p is strictly increasing. Consequently the
COMPLETE nominal minimizer set is

    {p_*}                         if Delta_(p_*)>0,
    {p_*,p_*+1}                   if Delta_(p_*)=0.             (3)

There is no third tied count. The full original logarithmic strip around
d/4 already proved in A2turn14 lies within3<=p<=floor(d/3) with linear
slack. Thus these are actual admitted product counts at sufficiently
large original indices, without a parity or equality distribution claim.

The root can be found by bisection of the monotone Delta with O(log d)
digit evaluations; ordinary bit cost is O((log d)^2) for this direct
implementation. This is an optional compressed count evaluation, not an
instruction to run any original factorial matrix or enumerate all counts.
No new numerical receipt is needed for formulas(1)--(3).

## 4. Complete near-minimum count localization

Let L_*=L_(p_*), and let t>=1 with p_*+t in the payment interval. Since
Delta_(p_*+r)>=4r for r>=0, summing gives

    L_(p_*+t)-L_* >= 2t(t-1).                      (4)

On the left, integrality and Delta_(p_*-1)<0 give
Delta_(p_*-r)<=-1-4(r-1). Hence

    L_(p_*-t)-L_* >= 2t(t-1)+t.                    (5)

The weaker uniform bound2t(t-1) therefore holds on both sides. At any
extra precision B>=0, EVERY product count with

    L_p<=L_*+B

must satisfy

    |p-p_*| <= (1+sqrt(1+2B))/2.                   (6)

There are consequently O(sqrt(B)+1) eligible product counts. This is a
quantified localization of ALL nominal competitors, including the adjacent
equality tie and both parities; it is not a selected-summand argument.

For a prospective upper-excess theorem at B=O(d log d), the product-count
range is therefore O(sqrt(d log d)), rather than an unbounded full count
range. At B=1, only p_*-1,p_*,p_*+1 can compete (some are excluded by their
actual Delta values). At B=0, (3) gives the exact complete set.

## 5. Precise limit of the new result

To apply(6) to a COMPLETE coefficient at that precision, each included
sector must actually have the nominal lower paymentL_p, and every excluded
correction pattern must be paid beyond that precision. The turn14 factorial
and bottom-atom exclusion at the first layer does not automatically extend
to arbitrary B. Its relevant positive margins must be compared to B, with
all source and forcing index sets and relative odd factors retained.

Likewise, localization of p does not localize the two near-minimal factorial-
adjugate index sets I,J or determine the higher integer source/THETA jets.
Their complete aggregate residue and every tied sector must still be
evaluated. For counts outside the proved paid interval, an independent
full-pattern lower payment is needed before discarding them from a global
coefficient calculation. No factorial forcing pattern is deleted merely
because its uncorrected nominal p cost is large.

The sufficient next theorem remains an actual nonzero complete I0 or I1
residue within O(d log d) extra layers, or any other proved joint binary
upper strong enough for the original arithmetic/analytic ledger. This note
supplies only the exact count convexity and excess locality part of that
bookkeeping. Other odd-prime control, actual all-prime G, least clearers,
primitive q, complete nonzero error and e+pi rationality remain OPEN.
