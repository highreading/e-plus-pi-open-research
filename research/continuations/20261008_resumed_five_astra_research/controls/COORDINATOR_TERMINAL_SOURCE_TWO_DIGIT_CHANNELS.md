> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Actual terminal source: two low-digit channels, with the size bill retained

9 October 2026, ongoing funded research. Parent proof from the current
original source formulas; an external DIFFERENT audit is not yet obtained.
This is a source constraint, not an inverse representation or an endpoint
evaluation. No computation is commissioned by this note.

## Reused hypotheses and checked overlap

Use A1turn15 Sections1,3 and7 at their original scope, in particular
H=3^(h-1), h>=63, D=H-A, nu=D/2-1, d=3D/2-1,
m+nu=(H-1)/2, and beta=1 mod3. The actual HIGH interval is d<=s<=m.
All parameters remain linked to the original j family and RangeIII;
P and chi are not independently selected.

The formula to reuse is

    upsilon_T[s] = -3^(h-1) [beta B(H,nu-1+s) + 3 B(H,nu+s)] mod3^28,

where B(N,q)=4^N N!(N+q)!(2q)!/(q!(2N+2q+1)!). Its exact valuation is

    v3 B(N,q) = -sum_(e=1)^h 1_(N mod3^e >= j_e(q)),
    j_e(q) = ((3^e-1)/2 - q) mod3^e.

The complete factorial source is paid at depth h-1>=62, so it contributes
zero at the precisions below. The physical3H terminal pole remains in
the formula. The all-prime producer and its actual denominator are not
altered by this local reduction.

Scoped overlap searches in the current/previous reports and the
October5/6 continuation found existing pole-grid and carry constructions,
including October7 A4turn3 Section7 and A1turn4 Section7. Those constructions
are established reuse. No exact two-channel statement for this CURRENT
terminal source was recovered. The following is an elementary corollary
of the supplied valuation identity, not a claim of a new general
automatic-sequence theorem or a universal novelty finding.

## Exact trailing-one valuation in the actual q range

Write r_e=(3^e-1)/2. Both terminal arguments satisfy

    0 <= q <= r_(h-1),

and q=r_(h-1) occurs ONLY for s=m in the3y channel. For e<=h-1,
H mod3^e=0, so the indicator is1 exactly when q=r_e mod3^e.
Let ell(q) be the number of initial ternary digits equal to1, reading
from the least significant end, capped at h-1. These are exactly the
successful indicators e<=h-1.

At e=h, j_h(q)=r_h-q>=H, with equality only at q=r_(h-1).
Consequently

    C(H,q)=ell(q)                         if q<r_(h-1),
    C(H,r_(h-1))=h.

The normalized beta contribution has depth h-1-ell(q) for every one
of its actual arguments, because its largest argument is r_(h-1)-1.
An ordinary3y contribution has depth h-ell(q); its terminal argument
has depth0. In particular, that exceptional3H unit is not assigned
the ordinary depth formula.

## Two exact low-digit support classes

Fix 2<=K<=28 and put L=h-K, B0=3^L. Ordinary beta entries visible
mod3^K require and suffice that

    nu-1+s = r_L modB0.

Ordinary3y entries visible mod3^K require and suffice that

    nu+s = r_(L+1) mod3^(L+1),

and the terminal s=m is also present. At the common low-digit split L,
the full terminal source can therefore be written

    s=b+B0*a, 0<=b<B0,
    upsilon_T[s] = 1_(b=b_beta) F_beta(a) + 1_(b=b_3y) F_3y(a) mod3^K,
    b_beta = (r_L-nu+1) modB0,
    b_3y   = (r_L-nu) modB0.

The two residues are distinct. F_beta retains the actual beta values and
the original finite range mask. F_3y retains the finer ordinary congruence,
the original range mask, the actual values, and the exceptional terminal
unit. Hence the low-digit/high-digit unfolding has rank AT MOST2 over
Z/3^K, in the precise sense of the displayed sum of two products. This
statement does not rely on a rank algorithm over a field.

There is no cancellation between the two source channels at a visible
ordinary coordinate: their low residues differ by1. The beta and3y unit
parts are units after their displayed valuation powers are removed.
This justifies the stated support tests at this local modulus.

## Why this does not authorize enumeration or solve the inverse

Ignoring the original lower q cutoff only enlarges the counts. There are
at most (3^(K-1)-1)/2 visible beta positions and at most
(3^(K-2)-1)/2 ordinary3y positions, plus the terminal. The resulting
upper bound is

    2*3^(K-2).

At K=27 this is 1,694,577,218,886 positions. A two-term tensor expression
at ONE digit split is therefore not a usable full precision-sized value
algorithm. It says nothing yet about state sizes inside F_beta,F_3y,
or about intermediate states after applying a matrix.

The true inverse is still

    M_H = (E_Y-3 X^T M_L X)^(-1)

on BOTH original finite HIGH ends. The LOW MATRIX return remains.
Neither M_H nor its action is shown to preserve the two low-digit
classes; the claimed source rank must not be promoted to inverse rank.
The normalized Omega source retains ALL14 terms and both beta/3y
channels and has not been reduced to two classes here.

The useful next obligation is to prove a small representation for the
actual directional inverse action, or for the final contracted pairing,
using this exact terminal seed together with the known finite mod3
inverse and paid higher lifts. A bound on reachable intermediate states
and every range mask must precede execution. The precise target remains
w_H^T f_H mod3^26, with w_H=(M_H upsilon_T-e_d)/3 and f_H=upsilon_0/3.
One extra precision digit for the coordinate quotient is still required.
