> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A rectangular rank criterion and an optimal physical source flag

Parent proof, 9 October 2026. DIFFERENT review is pending. The new
joint kernel is being independently audited in A4turn21; the new
mixed-compound theorem of A2turn13 also awaits DIFFERENT review.
No original-sized array, determinant or source calculation is run.

Before this continuation, scoped current/previous/Desktop English
MD/TEX searches for this specific rectangular root-multiplicity
criterion and linear physical attaining flag find no proved earlier
statement. A2turn13's submask CONTACT-JET flags, rising divisor and
mixed window are REUSE. They explicitly leave the optimal consecutive
physical source flag open. A2turn14 is already researching that
question; this parent derivation is a new proposed input to that
ongoing work, not a new claim for an already closed result.

Classical finite-field conjugation, polynomial root multiplicity,
finite rank/basis extension and irrational-rotation density are
reuse. The archived qualitative CRT/rotation gate already records
the latter at its proper scope. No new external theorem is adopted.

Keep the original d=9^(18+32u)-1, d=2 mod3 and v2(d)=4.
Let U_(j,r) be the additionally normalized contact parity with the
FULL integer row divisor2^j(d+1)_j. Its value is independent of the
physical starting row at this parity precision. Every use below
has actual r<d and actual top jets n+j<d.

## 1. The finite rectangular cross block

Use the exact joint-kernel column convolution C(Y)=(1+Y+Y^2)^d
on the first2L contact columns. This is an invertible binary
triangular operation on the normalized PARITY matrix, not a
claimed whole integer-pencil operation. Reorder its first2m rows
and first2L columns by parity. The transformed rectangle is

    [[C_(m,L,d), A_(m,L,d)], [A_(m,L,d), 0]],          (1)

where, for0<=h<m and0<=l<L,

    A(h,l)=[Y^l] Tr(omega^(h+2)
                  (1+omega^2 Y)^d/(1+omega Y)^(h+1)). (2)

The two cross blocks coincide by Lucas on the least binary digit;
the odd/odd block is zero. Equation(2) follows by expanding the
joint numerator and R(X+Y). In particular the internal phase is
omega^(h+l+v+2), after squaring inside the trace. The opposite phase
would be incorrect. The corrected parent block note records this
phase correction and8192 NEW independent finite comparisons.

## 2. An evaluated full-row-rank criterion

Let L=2^a be a power of2, put rho=d mod L, and assume

    2L<=d, m>=1, rho+2m<=L.                          (3)

Then A_(m,L,d) has binary row rank EXACTLYm.

Proof. Suppose a binary row vector c=(c_0,...,c_(m-1)) annihilates
all L columns. Set

    Q(Y)=sum_(h=0)^(m-1) c_h omega^(h+2)
                         (1+omega Y)^(m-h-1).

Thus deg Q<=m-1. Let sigma denote coefficientwise field conjugation.
The annihilation says that, modulo Y^L,

    F+F^sigma=0,
    F=(1+omega^2 Y)^d Q(Y)/(1+omega Y)^m.

Both denominators have constant1. Multiplying by their product
therefore gives

    (1+omega^2 Y)^(d+m) Q(Y)
       +(1+omega Y)^(d+m) Q^sigma(Y)=0 mod Y^L.

Since L is a power of2, (1+alpha Y)^L=1 mod Y^L. By(3),
d+m mod L=rho+m, with no wrap. The congruence becomes the polynomial

    P(Y)=(1+omega^2 Y)^(rho+m) Q(Y)
             +(1+omega Y)^(rho+m) Q^sigma(Y).

Its degree is at most rho+2m-1<=L-1. The congruence therefore
implies P=0 EXACTLY. At the root of1+omega Y, the other linear
factor is a unit. Consequently Q is divisible by
(1+omega Y)^(rho+m). This divisor has degree at leastm, whereas
deg Q<m. Hence Q=0. The powers(1+omega Y)^(m-h-1) are a basis,
and every omega^(h+2) is nonzero, so all c_h vanish. This proves
the rank statement without evaluating a growing determinant.

Equation(1) now has row rank EXACTLY2m: a row relation in its
odd-column block first annihilates A and kills the even-row
coefficients; the even-column block then kills the odd-row
coefficients. Undoing the finite unit column convolution preserves
rank. Thus the ACTUAL normalized contact rectangle on rows
0,...,2m-1 and original returns r=0,...,2L-1 has rank2m.

The condition2L<=d pays all selected original return indices. This
does not prove row rank at arbitrary parameters violating(3).

## 3. Transfer to the minimizing physical top rows

Put q=2m+1<=d. The full rank above gives2m DISTINCT actual return
indices in0,...,2L-1 with unit normalized contact determinant.
Choose those columns and the atom-contact column. Use the original
consecutive physical top rows

    T_q={d-q,...,d-1}.

Their forward-difference transformation has determinant1. Extract
the exact contact row factors2^j(d+1)_j. In the atom-column
expansion, omitting the largest contact rising payment is uniquely
cheapest: the final jet order2m has a strictly larger rising
valuation than order2m-1 because d+2m is even. The atom has exact
jet depthj with an odd normalized value. The unique lowest term
therefore uses the atom in row2m and the proved unit contact minor
in rows0,...,2m-1. Its EXACT binary depth is

    B_q(d)=binom(q,2)+sum_(j=0)^(q-2) v2((d+1)_j).   (4)

This attains the stronger universal source divisor. All full rising
integers and their odd factors are retained before the parity
argument. There is no claim that the parity convolution is a
simultaneous integer operation on the complete corrected pencil.
Full rank guarantees a subset of ORIGINAL columns; it does not
require importing transformed columns into that pencil.

These optimal source minors can be nested over the odd sizes
q=5,7,...,2m+1. The existing four return columns1,0,5,4 have a unit
normalized contact minor on the first4 jet rows by the established
source5 theorem. Their independence persists when further rows are
added. Rank2m allows ordinary basis extension by two further actual
return columns at each step. Choosing the least available extending
indices makes this a definite finite selection rule. This is a
rank/existence theorem, not a compact O(log d) execution claim for
the entire selection algorithm. No original-sized selection is run.

## 4. A linear-size family at infinitely many ORIGINAL indices

Write k=d+1=9^(18+32u), a=floor(log2 k), L=2^(a-1). Consider only
the original indices with

    (9/8)2^a < k < (5/4)2^a.                         (5)

Then2L<=d, and

    L/4-1 < rho=d-2L < L/2-1.

Choose m=L/8 and q=2m+1=L/4+1. Every original L is sufficiently
large that q<=d/8. Also rho+2m<L/2-1+L/4<L, so(3) holds.
The optimal physical source flag therefore extends to a rank
q with q/d bounded below by a fixed positive constant (asymptotically
at least1/10) on the subfamily(5). Its contact columns stay below2L<=d.

This subfamily is infinite. Indeed, log2 9 is irrational: a rational
value would imply an equality between a positive power of9 and a
power of2, contradicting prime factorization. The fractional parts
of18 log2 9+32u log2 9 are therefore dense by the established
irrational-rotation result. They hit the nonempty interval
(log2(9/8),log2(5/4)) infinitely often. This gives(5) in the SAME
original index family. No conjecture about binary digits is used.

More sharply, one need not stop at q=L/4+1. Define q_star as the
largest odd integer satisfying the exact mixed-compound hypotheses

    10q_star+3m_d<L_d, 4q_star<alpha_d-2,
    m_d=1+floor(log2 d), L_d=2d-s2(d)-12.

Then q_star=d/5-O(log d). Since q_star<d/5 and rho<L/2-1,

    rho+q_star-1 < rho+(2L+rho)/5-1 < L.

Thus(3) also holds for m=(q_star-1)/2, and for every smaller odd
source rank. The optimal nested physical source flag reaches the
END of the proved mixed-compound comparison window, asymptotically
one fifth of d, on this same original subfamily. The simple d/8
window is therefore not the endpoint of this argument. The exact
strict inequalities remain necessary; correction terms are not
removed beyond them. This refinement is algebraic, with no new
source or determinant calculation.

## 5. Complete corrected comparison and remaining scope

CONDITIONAL on the new A2turn13 mixed-compound theorem, which still
awaits a DIFFERENT audit, its two strict comparison inequalities
(in particular q<=d/8) and(4) give the exact complete common
cofactor depth

    Theta_q(d)=c_q+2E_q+B_q(d),

with the original firstq residual physical rows attaining it and
normalized Vandermonde row residue1. Every bottom correction and
factorial part is paid by that theorem, not deleted by entrywise
congruence. The full odd pivot quotient remains; it is not set to1.

The NEW parent result solves the OPTIMAL CONSECUTIVE source-unit
existence problem at linear rank on the explicit infinite subfamily.
It does not solve it at ALL original indices, at all even ranks or
through all d+1 common directions. Nor does it upper-bound either
terminal coefficient or their joint all-prime gcd. No final nu^[5]
bound, other odd-prime descent, primitive whole-error decay, producer
retirement or e+pi conclusion is proved. In particular, a divergence
proved only on this subfamily would not retire every other index of
the producer. Further mixed corrections and both terminal borders
must be controlled before any such implication.
