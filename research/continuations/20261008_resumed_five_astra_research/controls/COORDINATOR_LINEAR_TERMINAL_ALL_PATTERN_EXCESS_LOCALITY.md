> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# All-pattern excess localization for the actual linear terminal coefficient

Coordinator derivation, 9 October 2026. NEW parent proof; DIFFERENT audit
pending. The target is the exact linear determinant from FULL A2turn14,
not the differently normalized constant border. A nonzero next aggregate
digit and a valuation upper remain OPEN.

Scoped current/Desktop MD/TEX searches before this derivation recover the
first-layer exclusion, complete THETA cancellation and general mixed
payment, but no all-p/all-v excess-localization statement in that scope.
Those passed finite Cauchy/Newton and factorial identities are REUSE. No
unread external theorem, probabilistic claim or original-sized calculation
is adopted.

## 1. Exact retained object

Keep original k=9^(18+32u), d=k-1, n=d+2, physical terminal3d+1 and the
literal paired linear coefficient

    I1=-c_k det[w_*,v^(0),...,v^(d)].

The factor c_k is retained. Write alpha=v_2((2d)!)=2d-s_2(d),
m=1+floor(log_2 d), L_d=alpha-12, lambda_j=j+v_2(j!). The exact nominal
L_p and its strictly convex difference are as in the separate coordinator
terminal-convexity note. Let L_* be its minimum, attained at p_*=d/4+O(m),
with at most the adjacent equality tie.

All product columns arise from the exact RN source, and R=R^C-2^(alpha-2)V.
A term has p product columns and v factorial-forcing columns, 0<=v<=p<=d;
put a=p-v and h=n-p. Both forcing/source index sets and the full atom are
retained. Scalar gamma, Cauchy, adjugate and odd source factors are not
assigned to1. This note only books binary lower payments.

## 2. The factorial-pattern comparison holds before its positivity test

For1<=p<=d, the source minor pays B_p(d). If the atom is a product column,
the full atom-containing integer divisor proves this. If it is a bottom
column, ALL top sources are u-jets and pay the stronger

    B_p(d)+v_2((d+1)_(p-1)).                      (1)

Indeed every source row of jet orderj has its full rising divisor; the
maximum selected order is>=p-1. The atom is absent from these top minors.
The missing bottom factorial is covered by its explicit2^A_d, with
A_d=v_2(d!)=v_2((d+1)!) since d+1=k is odd.

The FULL mixed Cauchy jet payment with a=p-v Cauchy columns is

    c_a+sum_{j=a}^{n-v-1}lambda_j.

At a=0 this is the ordinary normalized bottom jet payment, with c_0=0;
no fictitious Cauchy minor or nonunit division is introduced. Empty source
and forcing index sets retain determinant1. The full source/adjoin bill
from turn14 gives

    E_p+E_a+v(2d-m-6),

and each factorial forcing contributes its exact2^(alpha-2) scalar.
Subtract the nominal L_p. The resulting additional lower payment is at
least

    v(alpha-2)+E_a-E_p+v(2d-m-6)+c_a-c_p
      +sum_{j=a}^{n-v-1}lambda_j-sum_{j=p}^{n-1}lambda_j.       (2)

The endpoint ranges are literal: a>=0,h>=2,n-v-1=a+h-1. Use

    E_p-E_a<=v(2p+m),
    c_p-c_a<=4pv,
    lambda_(b+h)-lambda_b<=2h+m.

The last follows from lambda_j=2j-s_2(j); every j involved is<=d+1<2^m
at the original indices, including the last physical jet. The first two
are the same full finite factorial/Cauchy inequalities as in turn14,
valid for0<=a<=p<=d. They do not require p<=d/3. No positivity is used
when deriving them. Summing the last inequality for the v removed upper
and added lower indices makes (2) at least

    v M_p,  M_p=alpha-4p-3m-12.                  (3)

This extends the comparison itself to ALL product counts. The earlier
p<=d/3 restriction made M_p positive; it was not required for(2)--(3).
The complete atom-bottom sector has the additional payment(1).

DIFFERENT audit must check all these finite source and empty-Cauchy cases;
this new extension is not silently declared covered by the first-layer
turn14 audit.

## 3. Negative M_p counts have a quadratic gap

If M_p>=0, every pattern has payment>=L_p. If M_p<0, use v<=p in(3):

    pattern payment >=L_p+p M_p.

The established uniform factorial/Legendre estimates give

    L_p=3d^2-2dp+4p^2+O(dm), 0<=p<=d,
    L_p+p M_p=3d^2+O(dm).

These are uniform finite estimates with constants independent of p,u.
Since L_*=11d^2/4+O(dm), the second branch is separated by

    d^2/4+O(dm).

It cannot appear within extra precision B=O(dm) at sufficiently large
ORIGINAL indices. This excludes every negative-M_p factorial pattern,
including patterns with a=0, without deleting them entrywise.

For p=0, the complete all-bottom determinant pays

    n L_d+sum_{j=0}^{n-1}lambda_j=3d^2+O(dm).

The explicit atom factor exactly covers the possible missing
v_2((n-1)!)=v_2((d+1)!)=A_d. Thus p0 has the same quadratic separation.
The bounded p1,p2 endpoints also lie away from the actual minimum.

This use of a lower payment is only exclusion of terms at a fixed
precision. It is not attainment or an upper bound for the complete sum.

## 4. ALL remaining counts and factorial orders at precision B

Suppose B=O(dm). Every remaining pattern has M_p>=0 and L_p<=L_*+B.
By the exact convexity note,

    |p-p_*|<=T_B,  T_B=(1+sqrt(1+2B))/2.

Together with |p_*-d/4|<=m+2 and alpha>=2d-m, this gives

    M_p>=d-8m-20-4T_B=d-O(sqrt(dm)+m)>0.         (4)

For every actual factorial-pattern competitor,

    v <= (B-(L_p-L_*))/M_p.                     (5)

Therefore only O(log d) factorial forcing columns can enter an
O(d log d) excess theorem, and only O(sqrt(d log d)) product counts can
enter. ALL ties and both parities are retained. The two near-minimal
factorial-adjugate index sets and every odd relative prefactor still
must be evaluated; their number is not bounded merely by(5).

## 5. A fully paid first linear-width precision window

Set B=floor(d/8). At sufficiently large original indices, (4) gives
M_p>B for every admitted competitor. Thus every v>=1 term is beyond
L_*+B. If the atom is a bottom correction, (1) gives the extra payment

    v_2((d+1)_(p-1))
        =p-1+s_2(d)-s_2(d+p-1)
        >=p-1-m
        >=d/4-2m-3-T_B > B.

Therefore the ENTIRE linear determinant through this precision comes
only from pure-Cauchy patterns with the atom as a product column and
the complete localized p range. This assertion includes all large-p
factorial patterns by the preceding quadratic-gap argument. It does
not assume that the unique first-layer forcing/source pair remains
the only near-minimal I,J pair at higher precision.

The complete leading THETA layer remains zero, as proved in turn14.
The next full aggregate residue is not evaluated by this note. A
single selected nonzero minor or a rank-one P5 perturbation cannot
replace that evaluation. Other-prime arithmetic and the actual
primitive normalization also remain necessary.

## 6. Remaining audit and research obligations

The NEW all-p/all-v comparison, empty-Cauchy/p0 cases, uniform gap and
first linear-width exclusions await DIFFERENT proof audit. They do
not change an admitted request or any saved exchange. No numerical
matrix, original source table, solve or prime scan is requested.

The useful next task is now a complete noncancellation/excess theorem
for the retained pure-Cauchy, product-atom near-minimal sector, or for
the small factorial order allowed by(5) at O(d log d) precision.
The actual coefficient I1 and the exact constant coefficient I0,
odd interpolation factors, both full borders and scalar transfer
remain literal. All-prime G, least clearers, primitive q, full
nonzero error and the e+pi objective remain OPEN.
