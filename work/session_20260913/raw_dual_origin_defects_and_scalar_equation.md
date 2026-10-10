> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact dual origin defects and a bounded-degree scalar equation

Date: 2026-09-13. Original continuation by root. Independent review pending.

This note uses the actual simultaneous integer triple, not the selected
type-I triple. The new quadratic certificate gives a small, exact defect
ledger for the two simultaneous errors and a differential equation with
degrees independent of n. These facts do not estimate an endpoint error.

## 1. Inputs and notation

Write Q=Qhat_n, P=Pe_n, T=Pa_n, D=1+z^2, M=3n+1. Thus each polynomial
has degree at most 2n and

    Re=Q exp(z)-P=O(z^M),   Ra=Q atan(z)-T=O(z^M).

The independently reviewed dual quadratic theorem gives

    D^2 exp(z) W(Q,P exp(-z),T-Q atan(z))=z^(6n) K(z),
    0 != K in Z[z],   v:=ord_0 K <= deg K=:k <=2.             (1)

The new deleted-last-row dyadic lemma in
raw_adjacent_dual_cross_and_fixed_gcd.md proves Q_n(0)!=0 for every n.
Its independent reviewer has separately confirmed this lemma. Its exact
valuation and factorial normalization should be read there rather than
inferred from a generic normality assumption.

The earlier raw_hp_homogeneous_ode.md concerns the three-dimensional
space {R,Be^z,C} of a selected type-I triple and its cubic. It does not
give the equation below for the simultaneous triple and its quadratic.

## 2. Origin defects of the two errors

Put g=-exp(-z)Re and h=-Ra. Subtracting Q from the second column of (1)
changes the three functions to Q,g,h without changing their Wronskian.
They are linearly independent, since that Wronskian is nonzero.

Choose an echelon basis of span(g,h) with distinct orders a<b. Then
a>=M, b>=M+1. Since ord Q=0, the leading Wronskian coefficient is a
nonzero Vandermonde in the distinct integer orders 0,a,b. In particular

    ord W(Q,g,h)=a+b-3=6n+v.                                (2)

The two first omitted coefficients of Re and Ra cannot both vanish.
Otherwise z^2(Q,P,T) would satisfy all the simultaneous equations at
index n+1: its degree is at most 2n+2 and its two errors have order at
least M+3=3(n+1)+1. Uniqueness of that next simultaneous denominator
would make Q_(n+1) proportional to z^2 Q_n. This contradicts the proved
Q_(n+1)(0)!=0. Thus a=M. Equation (2) now gives the exact ledger

    a=M,                  b=M+1+v,       0<=v<=2.           (3)

Every nonzero CONSTANT linear combination of exp(-z)Re and Ra therefore
has order at most M+3=3n+4. Exactly one projective combination cancels
the first omitted coefficient, and its order is exactly M+1+v.
This assertion concerns the specified gauged errors. It must not be
silently applied to Re+4Ra, whose exponential coefficient in this basis
is not constant.

There is a version independent of the newly proved Q(0) lemma. If
ell=ord Q and a=M+t, b=M+t+1+s, then the distinct orders ell,a,b give

    ell+2t+s=ord_0 K<=2.                                    (4)

Here ell<=2n<M, so the orders are indeed distinct. In particular that
older information alone would have bounded ell by 2; it would not have
proved ell=0 or t=0. Equation (3) uses the additional exact dyadic input.

## 3. The actual scalar equation

Let y_1=Q, y_2=P exp(-z), y_3=T-Q atan(z), and write W_ijk for their
three-by-three determinant with derivative rows i,j,k. Define

    A3=z^2 D K,
    A2=-z{[(6n-z)D-2zD']K+zD K'},
    A1=D^3 exp(z) W_023 / z^(6n-2),
    A0=-D^3 exp(z) W_123 / z^(6n-2).                       (5)

All four are polynomials over Q. To clear the logarithm, add atan(z)
times the first column to the third column AFTER differentiating. In
row r its resulting entry is T^(r) minus the sum of the terms involving
Q^(r-j) atan^(j), j>=1. For r<=3 their denominators divide D^3. Factoring
exp(-z) from the second column leaves (partial-1)^r P. Thus D^3 exp(z)
clears the determinant coefficients.

To justify the origin divisions, use columns Q,g,h with g,h of orders
at least M and with their leading terms echelon-reduced to distinct
orders at least M,M+1. In both row sets 023 and 123, the smallest
possible order from the error columns is M+(M+1)-2-3=6n-2.
Derivatives of Q are analytic and add no negative order. This proves
the required monomial divisibility. Passing from exp(z) times an
analytic determinant to its polynomial numerator does not change that
order because exp(0)=1.

Expansion of a four-by-four Wronskian gives

    A3 y''' + A2 y'' + A1 y' + A0 y=0                     (6)

for all three functions and exactly their local constant span where
A3 is nonzero. In deriving A2, use W_013=W_012' and (1). The monic
coefficient is especially simple:

    A2/A3=1-6n/z+2D'/D-K'/K.                               (7)

The exponential sign in (7) differs from the older type-I equation.

## 4. Infinity types and degree bounds

At infinity take a local Laurent branch of atan(z)-atan(infinity).
The two-dimensional Laurent space spanned by Q and
T-Q[atan(z)-atan(infinity)] has a basis with distinct highest powers
c,d. One can take c=deg Q; cancel the power c from the other member
when necessary. The second member cannot disappear: atan is not a
rational function. Put b=deg P. The exponential member has form
exp(-z) z^b times a nonzero Laurent unit. All b,c,d are at most 2n.

The leading Wronskian has a nonzero factor d-c and power
exp(-z) z^(b+c+d-1). Comparing with (1), including D^2, gives

    b+c+d=6n+k-3,
    (2n-b)+(2n-c)+(2n-d)=3-k.                              (8)

Thus every one of the three infinity defects is at most 3. In particular
deg P and deg Q are at least 2n-3. When k=2, b=2n and the unordered pair
{c,d} is {2n,2n-1}. Full degree of Q is not separately inferred in the
other cases.

The same leading cofactor computation gives

    A1/A3=-(c+d-1)/z+O(z^-2),
    A0/A3=cd/z^2+O(z^-3).                                 (9)

For example the highest W_023 term uses derivative rows 0 and 2 of
the Laurent columns and derivative 3 of the exponential column;
comparison with W_012 gives the first minus sign in (9). The analogous
rows 1 and 2 give the second formula after the minus in A0.

Consequently

    deg A3<=k+4<=6,  deg A2<=k+4<=6,
    deg A1<=k+3<=5,  deg A0<=k+2<=4.                       (10)

If K has leading coefficient k_k, the coefficients of z^(k+3) in A1
and z^(k+2) in A0 are -(c+d-1)k_k and cd k_k. These can be zero. No
asymptotic convergence of these bounded-degree coefficients follows.

## 5. Local implications and limitations

If K(0)!=0, the three exact origin orders are 0,M,M+1. The regular
singular indicial polynomial of (6) is therefore r(r-M)(r-M-1).
Equivalently A1(0)=3n(3n+1)K(0). This follows either by the leading
Wronskian coefficients or by substitution into (6); A0 enters at a
higher order in the indicial calculation. For K(0)=0, use (3), not
these generic coefficients without cancellation of common powers.

At a simple root of K outside {0,i,-i}, all three functions are analytic
and their Wronskian has one zero. Their echelon orders are then 0,1,3.
This is an apparent singularity. More generally, at an ordinary point
a with aD(a)!=0, any nonzero member of this three-dimensional function
space has vanishing order at most 2+ord_a K<=4. The proof is the same
Wronskian order sum: the other two distinct nonnegative orders have
sum at least 1. This is a LOCAL multiplicity bound, not a bound for
the number of distinct real zeros on an interval.

The equation is still irregular at infinity because it contains the
actual exponential solution. Its origin resonance grows with n, even
though the polynomial coefficient degrees do not. The statements above
therefore supply neither uniform connection estimates nor a shrinking
primitive endpoint form. They retain the exact dual normalization and
identify which further coefficient or zero-location estimates would
be needed. A useful next step is a quantitative relation between this
quadratic system and the finite Hankel/Toeplitz representation of the
same dual polynomial, with the endpoint gcd restored afterwards.
