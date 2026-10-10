> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Bounded origin data from the actual homogeneous equation

Date: 2026-09-13. Root continuation of the homogeneous ODE and rational
degree transfer. This removes the growing index of the origin Taylor
conditions from the data needed for the next transfer. It does not
remove the endpoint connection problem or prove an asymptotic estimate.

Use the notation of `raw_hp_homogeneous_ode.md`. In particular n>=1,
R=A+B exp(z)+C atan(z) has order at least 3n+1, and



$$
W(R,B e^z,C)=e^z z^{3n-1}Q(z)/(1+z^2)^2,
 \qquad 0\ne Q\in\mathbb Q[z],\quad \deg Q\le3.
$$



The scalar equation is written in monic form



$$
y'''+a_2(z)y''+a_1(z)y'+a_0(z)y=0.
\tag{1}
$$



## 1. The exceptional origin is still regular singular

Let l0<l1 be the echelon vanishing orders of the two-dimensional
analytic solution space spanned by B exp(z),C. Write M=ord_0 R.
The established two-function multiplicity bound gives l1<=2n+1<M.
The leading Wronskian of three analytic germs with distinct orders is
their nonzero leading-coefficient product times the Vandermonde in
those orders. Its vanishing order is therefore l0+l1+M-3. Thus, with
h=ord_0 Q,



$$
M+l_0+l_1=3n+2+h,\qquad 0\le h\le3.
\tag{2}
$$



Since l0>=0,l1>=1 and M>=3n+1, this strengthens the individual bounds to



$$
\boxed{3n+1\le M\le3n+4,\qquad l_0+l_1\le4.}
\tag{3}
$$



In particular the entire low-order analytic space is visible in its
first five jets, even when Q has a zero at the origin.

For any derivative row set I, the corresponding determinant of these
echelon germs has valuation at least l0+l1+M-sum(I). This remains true
when a derivative kills a leading monomial: it only increases the
valuation of that entry. Comparing the cofactors W013,W023,W123 with
W012 proves that a2,a1,a0 have poles of order at most1,2,3 respectively
at zero. Consequently



$$
b(z)=z a_2(z),\qquad c(z)=z^2 a_1(z),\qquad d(z)=z^3a_0(z)
\tag{4}
$$



are analytic at zero, including every exceptional Q(0)=0 case. They
are rational functions whose degrees are bounded independently of n.
The Euler form of (1), with theta=z d/dz, is



$$
[\theta(\theta-1)(\theta-2)
   +b(z)\theta(\theta-1)+c(z)\theta+d(z)]y=0.
\tag{5}
$$



Each actual echelon leading order is a root of the monic indicial
polynomial



$$
I(s)=s(s-1)(s-2)+b_0s(s-1)+c_0s+d_0.
$$



There are three distinct such orders, so



$$
\boxed{I(s)=(s-l_0)(s-l_1)(s-M).}
\tag{6}
$$



The high root M is determined from the ODE alone: it is the unique
root at least 3n+1, and can be found by testing the four integers in
(3). This is a bounded computation in the accessory coefficients and
n. It does not require computing a Taylor series through order 3n.

## 2. The first eight relative coefficients

Normalize the high solution locally by



$$
R_*(z)=z^M\sum_{r\ge0}u_r z^r,\qquad u_0=1.
$$



Expand b,c,d from (4) at zero. Substitution in (5) gives, for r>=1,



$$
\boxed{
 u_r=-\frac{
 \displaystyle\sum_{j=1}^r
  \left[(M+r-j)(M+r-j-1)b_j
             +(M+r-j)c_j+d_j\right]u_{r-j}}
 {(M+r-l_0)(M+r-l_1)r}.}
\tag{7}
$$



Every denominator is nonzero. The actual R divided by its leading
coefficient obeys this recurrence, so neither an existence theorem
nor an unproved formal convergence assumption is needed to identify
these coefficients. For any fixed r, the needed coefficients of the
rational functions (4) are obtained by bounded formal division after
removing their common origin powers. In particular u0,...,u7 use only
bounded accessory data and seven recurrence steps.

When Q(0)!=0, (2) forces l0=0,l1=1,M=3n+1. Equation (7) reduces to the
usual high Frobenius recurrence with denominator
(M+r)(M+r-1)r. This generic simplification must not be imposed in the
exceptional cases; (7) already handles them.

## 3. Consequence for the rational degree transfer

The first row of the transfer is (N0,N1,N2)/Q with deg Nj<=6.
Its required origin condition is



$$
N_0R+N_1R'+N_2R''=O(z^{3n+4+h}).
\tag{8}
$$



The largest coefficient of R that can occur in the coefficients being
set to zero is at degree 3n+5+h<=3n+8. Since M>=3n+1, these are among
the first eight coefficients u0,...,u7 above, with earlier coefficients
zero. Multiplying R by a nonzero common scalar does not change (8).
Hence **all origin-raise equations in the fixed-size next-degree
construction can be formed from n and the scalar ODE alone**. The
polynomial coefficient arrays of the current triple are unnecessary
for this part of the construction.

This conclusion is unconditional for the actual family, including
multiple Q roots and Q(0)=0. Replacing the other polynomiality, infinity,
and endpoint conditions by bounded data is a separate task. The
endpoint normalization B(1)=1,C(1)=4 fixes a global connection which
does not follow from the origin exponents by themselves.

## 4. Verification scope

`check_raw_hp_origin_jets.py` compares the eight coefficients from (7)
against the original Taylor/endpoint construction in independently
chosen degrees. These finite controls check signs and indexing. The
all-degree argument, including the exceptional-origin case, is the
Wronskian valuation and recurrence derivation above; no exceptional
case is inferred from a sample of generic rows.
