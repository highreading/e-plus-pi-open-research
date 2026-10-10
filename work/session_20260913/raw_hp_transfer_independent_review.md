> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the rational degree transfer, and bounded local reconstruction

Date: 2026-09-13. Reviewed `raw_hp_rational_degree_transfer.md` against
the original Taylor conditions and `raw_hp_homogeneous_ode.md`.

**Review result:** the rational transfer, degree bounds, at-most29-row
construction, and six-jet endpoint regularization pass. The additional
lemmas below distinguish unique global determination by the accessory
equation from a bounded rational procedure. They prove bounded local
reconstruction at infinity and at a generic logarithmic pole, and an
unconditional bounded update of endpoint jets once the transfer is
known. They do not claim that accessory coefficients alone already give
the normalized endpoint directions by a bounded rational formula.

## 1. Universal gauge and mixed determinants

The reviewed factorization Psi_n=K_n S G is exact: multiplying each row
of K_n by S removes its D² factor in the first coordinate, and then G
adds e^z times its second coordinate and F times its third coordinate.
The first column becomes R and its derivatives, with all F' and F''
terms present. The other columns become U=Be^z and C.

Since S,G are independent of n, the transfer is exactly
T_n=K_(n+1)K_n^(-1). A mixed row determinant has the same universal
factor D²e^(-z) as an unmixed determinant; D³ is neither needed nor
appropriate for this rows0,1,2 calculation.

For each mixed determinant the first analytic column contains old
remainder jets of orders at least3n-1 and new jets of orders at least
3n+2. Thus its polynomial numerator has the asserted factor z^(3n-1).
The two smallest derivative orders among its three rows give the
displayed numerator-degree matrix



$$
\begin{pmatrix}5&6&6\\4&5&5\\3&4&4\end{pmatrix}.
$$



For the lower-right entry, the first-and-third-column minor on the old
rows0,1 has the leading equal-degree cancellation, supplying the extra
one-degree improvement. Replacing old row2 leaves only old remainder
jets of orders0,1, so every last-column numerator has an extra factor z.
These arguments remain valid when individual polynomial degrees drop.

Taking the determinant yields
det(T_n)=z³Q_(n+1)/Q_n and det(N_n)=z³Q_n²Q_(n+1), with the same cubic
normalization as the homogeneous ODE. Differentiation then gives exactly
T'=C_(n+1)T-T C_n. The companion signs and the cleared identity in the
reviewed note agree with the cofactor equation.

## 2. The at-most29 equations in21 unknowns are sufficient and necessary

For the trial numerator row (N0,N1,N2), each polynomial of degree at
most6, the three quotient expressions in the reviewed formula(11)
are exactly the coefficients of



$$
\widehat R=\frac{N_0R+N_1R'+N_2R''}{Q_n}
            =\widehat A+\widehat B e^z+\widehat C F.
\tag{1}
$$



In particular the A quotient includes both derivative corrections
DC and 2DC'-D'C. There is no omitted logarithmic or exponential term.

Write q=deg Q_n and h=ord_0Q_n. The B and C numerators have degree at
most n+6. For each, zero Euclidean remainder gives q linear equations,
and suppressing quotient degrees above n+1 gives at most5-q further
equations. Each therefore costs at most5. The A numerator has degree
at most n+10 and denominator degree q+4, giving (q+4)+(5-q)=9.
These counts hold also for q=0 and when leading coefficients vanish.

The numerator in (1) already has order at least3n-1. Imposing order
at least3n+4+h costs at most5+h<=8 equations and is exactly equivalent
to the next required remainder order3n+4. The largest old R coefficient
used is that of degree3n+5+h<=3n+8, because of the second derivative.
There are therefore at most eight old unconstrained coefficients, not
an unbounded Taylor prefix. Finally the quotient endpoint conditions
give two equations. Total:19+8+2=29 at most.

All equations are rational and linear in the21 numerator coefficients.
The actual next row supplies consistency. Any solution produces the
canonical next triple by the accepted rank theorem. Two representations
of that same triple would differ by an order-at-most2 rational operator
annihilating the three independent fundamental solutions; their jet
matrix is invertible over the meromorphic field, so that difference
operator is zero. Thus the claimed unique coefficient vector follows.

Using the polynomial quotients at z=1 is essential. Direct substitution
into an unregularized N/Q formula would be invalid when Q_n(1)=0.

## 3. The six-jet endpoint map is valid

Let h=ord_1Q_n<=3. Since det(Psi_n)=e^z z^(3n-1)Q_n/D², its determinant
has precisely this order at1. Its h-th derivative is a sum of minors
formed from derivative rows at most h+2<=5; at least one is nonzero.
Thus the six-by-three endpoint jet matrix has rank3.

After removal of the common invertible G(1), its matrix H_n is real
rational. Consequently H_n^T H_n is positive definite, and the displayed
rational left inverse exists. The identity



$$
H_{n+1}(H_n^TH_n)^{-1}H_n^T(H_nG(1))=H_{n+1}G(1)
$$



proves propagation of every actual fundamental column. It does not
make the six-by-six map invertible outside that three-dimensional
subspace. No assumption Q_n(1)!=0 is hidden in this argument.

## 4. What the companion equation determines globally

The companion equation uniquely determines the line spanned by C among
polynomial solutions. Indeed every solution is a constant combination
of R,U,C. A polynomial solution has zero logarithmic monodromy, forcing
its R coefficient to vanish; nonrationality of exp then forces its U
coefficient to vanish. Similarly its exponential-polynomial solution
line is exactly the line of U. The endpoint conditions C(1)=4 and
B(1)=1 fix their scales uniquely.

This is an information-theoretic uniqueness statement. A conventional
reconstruction can impose the polynomial ansatz of degree at most n,
or propagate its coefficient recurrence. Either uses data or work
growing with n. The uniqueness proof alone is not a bounded-size
rational reconstruction algorithm.

The same distinction applies to the high-order R line: its origin
condition singles out a one-dimensional local solution space, but a
connection coefficient is needed to compare its normalization with
the separately normalized U and C. The root's separate origin-Frobenius
lemma reconstructs its required finite jets up to a harmless common
scale; it should not be mistaken for a global connection formula.

## 5. Bounded reconstruction of top Laurent jets at infinity

Use q=deg Q, m=q+3, and q_q=lc(Q). The homogeneous-ODE note proves



$$
\frac{A_2}{A_3}=-1-\frac{b+c+d-1}{z}+O(z^{-2}),\quad
 \frac{A_1}{A_3}=\frac{c+d-1}{z}+O(z^{-2}),\quad
 \frac{A_0}{A_3}=-\frac{cd}{z^2}+O(z^{-3}),
$$



where b=deg B and c,d are distinct integers, each within4 of n.
The sum and product of c,d are read from the leading coefficients;
b follows from b+c+d=3n+q-4. Thus this finite list of exponents is
recoverable from accessory coefficients and n.

For the exponential branch write
$U=e^zz^b\sum_{j\ge0}u_jz^{-j}$, u0=1. In the conjugated operator
$e^{-z}Le^z$, the leading coefficient on a monomial z^r is
$q_q(r-b)z^{r+m-1}$. Consequently the recurrence coefficient on u_j
is exactly -j*q_q. It is nonzero for every j>=1. Any fixed number of
top B coefficients is therefore obtainable by a fixed number of
rational operations from the accessories; no lower polynomial array
is required.

For the two Laurent branches put h=max(c,d), l=min(c,d), Delta=h-l<=4.
The leading coefficient on z^r is
$-q_q(r-h)(r-l)z^{r+m-2}$. The high-branch recurrence coefficient
at step j is q_q*j*(Delta-j); it has just the resonance j=Delta.
The two actual Laurent germs ensure compatibility there. Choosing
that free coefficient to be zero is a basis convention. The low-branch
coefficient is -q_q*j*(Delta+j), never zero for j>=1. Thus a basis of
either fixed number of top Laurent jets is also rationally reconstructible
from bounded data.

Selecting which linear combination is the actual polynomial C is a
different issue. In the generic q=3 case the two powers are n and n-1,
and the resonant coefficient mixes those two Laurent germs. Polynomiality
selects one combination globally. A naive way to determine it requires
reaching a negative Laurent coefficient, an index growing with n.
This demonstrates a gap in that particular reconstruction method; it
is not a proof that every possible bounded rational method is impossible.

For degree tests on the transfer this selection is unnecessary: the
actual transfer maps the entire old Laurent plane to the new Laurent
plane. In the q=3 case, the independent transfer agent sharpened this
to three top-coefficient equations. Writing deg N0<=5 and deg N1,N2<=6,
they are



$$
N_{0,5}+nN_{1,6}=0,\quad N_{1,6}+N_{2,6}=0,
$$




$$
N_{0,5}+N_{1,5}+N_{2,5}+nN_{1,6}+2nN_{2,6}=0.
\tag{2}
$$



I independently checked them: the first removes the only excessive
power of the degree-n Laurent branch; the degree-(n-1) branch already
fits. The latter two remove the top two exponential-polynomial powers.
The unknown second coefficient of B cancels after imposing the second
equation. These conditions use the whole Laurent plane and assume
neither a particular degree for C nor a chosen connection coefficient.

## 6. A local accessory formula for the monodromy-image line C

At xi=i or -i suppose Q(xi)!=0. Then A3 has a simple zero there,
A2(xi)=2A3'(xi), and C(xi)!=0. The last assertion also follows directly
from N(xi)=-D'(xi)C(xi)K(xi), where
K=B C'-(B+B')C and N=z^(3n-1)Q.

Write x=z-xi. The logarithmic solution has the form
$v(x)\log x+w(x)$, with w analytic and v a nonzero constant multiple
of C. Since Lv=0, the remaining part of L(v log x) is



$$
A_3(3v''/x-3v'/x^2+2v/x^3)
 +A_2(2v'/x-v/x^2)+A_1v/x.
$$



The x^(-2) coefficient cancels because A2(xi)=2A3'(xi). The x^(-1)
coefficient must also vanish since Lw is analytic. It equals



$$
A_3'(\xi)v'(0)
  +[A_3''(\xi)-A_2'(\xi)+A_1(\xi)]v(0).
$$



Therefore



$$
\boxed{\frac{C'(\xi)}{C(\xi)}
 =\frac{A_2'(\xi)-A_3''(\xi)-A_1(\xi)}{A_3'(\xi)}.}
\tag{3}
$$



Normalize C(xi)=1. The equation at xi next fixes C''; coefficient
comparison fixes every further bounded jet. Its Taylor recurrence
coefficient on v_(k+2) is
$A_3'(\xi)(k+2)^2(k+1)$, nonzero for k>=0. Thus any fixed local jet
of the C line is rational over Q(i) in the accessory data. This proves
bounded local reconstruction, including its correct analytic line.

Formula(3) does not immediately give C'(1)/C(1). Moving from xi to1 is
a connection problem. At a pole where Q also vanishes, the formula's
hypotheses fail and its denominator must not be used.

## 7. Unconditional bounded closure of endpoint jet state

There is a useful stronger version of the six-jet observation. Given
the current accessory equation, six endpoint jets of any actual solution
determine every further fixed number of jets by bounded rational work.

To prove it, put t=z-1. A local analytic echelon basis has distinct
nonnegative integer orders r0<r1<r2. Its Wronskian has order
r0+r1+r2-3=ord_1Q<=3. Hence r2<=5. The cofactor order estimates give
at most simple, double, and triple poles in A2/A3,A1/A3,A0/A3. Therefore
the following Euler coefficients are analytic at t=0:



$$
b(t)=t A_2/A_3,\quad c(t)=t^2 A_1/A_3,\quad d(t)=t^3 A_0/A_3.
$$



The indicial polynomial is



$$
I(k)=k(k-1)(k-2)+b_0k(k-1)+c_0k+d_0
     =\prod_{j=0}^2(k-r_j).
\tag{4}
$$



For y=sum y_k t^k its exact coefficient recurrence is



$$
I(k)y_k=-\sum_{j=1}^k
 [b_j(k-j)(k-j-1)+c_j(k-j)+d_j]y_{k-j}.
\tag{5}
$$



In particular I(k)!=0 for every k>=6. Starting from six consistent
jets, coefficients through any fixed index follow by rational operations
on a fixed Taylor expansion of the rational accessories. No selection
between resonant solutions remains beyond index5.

For the transfer $\widehat y=(N_0y+N_1y'+N_2y'')/Q$, write
Q=t^h q(t), q(0)!=0, h<=3. Six next jets require the numerator only
through index h+5, hence old y only through index h+7<=10. Formula(5)
reconstructs these from the six stored jets using at most five further
steps. Exact series division by q then gives the next six jets. The
vanishing of numerator coefficients below h follows from the actual
transfer and can also be checked as a local pole-cancellation condition.

For U=Be^z, store U^(r)(1)/e, which is rational, together with C^(r)(1),
0<=r<=5. The same formulas propagate these twelve rational quantities.
Thus a bounded endpoint-jet state closes unconditionally once N is known,
even when Q(1)=0. This is stronger than merely replacing one finite
endpoint matrix by another whose entries still require whole polynomials.

## 8. Remaining distinction for an accessory-only update

The full transfer theorem still uses current polynomial data. The new
local reconstructions remove several reasons for that dependence: top
infinity tests, fixed origin jets (in the root's separate proof), generic
pole data, and propagation of bounded endpoint jets can all be handled
locally. The endpoint directions can be retained as a bounded rational
state instead of repeatedly reconstructing full polynomial arrays.

A proof that those endpoint directions are themselves bounded rational
functions of the scalar accessory coefficients has not been obtained
here. Unique global determination is not that proof. The generic
bounded local transfer system now proved in
`raw_hp_generic_accessory_update.md` does use the endpoint-jet state.
Its completeness and uniqueness are verified next against the original
polynomial problem, not inferred just from counting equations.

## 9. Independent review of the generic twenty-variable update

The additional note assumes deg Q=3, squarefree Q, and gcd(Q,zD)=1,
without excluding Q(1)=0. Under exactly those hypotheses its Sections2–8
pass independent review.

At a simple Q-root, the local free jets y,y' and the equation for y''
give precisely the two remainder congruences stated there. They remove
the pole of S on the entire old solution space. At each logarithmic
point the nonzero value of C makes the double- and simple-pole tests
necessary as well as sufficient; differentiating t2*C gives exactly
t1=t2' after t2=0, with no omitted C' or Q' term. This verifies its
four D-divisibility equations.

The global sufficiency argument is sound. The rational Bhat and Chat
have possible finite poles only at Q-roots, already removed. Ahat's
additional poles at +/-i are exactly the extra derivative terms in
S(C log), removed by the D tests. Removing the logarithmic coefficient
before asserting analyticity is essential and is done correctly.
The three infinity equations bound the whole Laurent plane. Thus
Chat has degree at most n+1, and
S(A+C(F-F_infinity))=Ahat+Chat(F-F_infinity) also has growth at most
z^(n+1). Its second term has growth at most z^n, which bounds Ahat's
degree as required. The exponential branch bounds Bhat separately.
The origin conditions then give the actual next Taylor order.

Conversely every unmatched next-degree triple gives the asserted
operator by mixed-row Cramer determinants, whether or not either of
its endpoint values is zero. Any nonzero such high-order triple has
B,C both nonzero by the two-function multiplicity bound. All its
local conditions and numerator degree bounds therefore apply. The
operator correspondence is injective by the old fundamental matrix.
The unmatched next space has dimension2, because imposing its one
matching condition gives the independently proved one-dimensional
canonical space while the Taylor equation count gives dimension at
least2. Hence the eighteen homogeneous equations have rank18 on the
twenty coefficients. This establishes rank by an exact isomorphism,
not by an equation count alone.

The two endpoint functionals are independent on that space: a vector
with both endpoints zero would lie in the canonical matched line but
have B(1)=0, contradicting its established nonzero endpoint. The two
regularized endpoint equations therefore make the twenty-by-twenty
system nonsingular. At Q(1)=0, the removed exponential contributes a
multiple of a numerator already known to vanish, so the derivative
endpoint formula using U^(j)(1)/e has the correct normalization.

The reconstructed next two transfer rows, the companion compatibility
formula, and Q_next=det(T)Q/z^3 then preserve the actual canonical
normalization. Section7 above proves bounded propagation of the
endpoint jets, including exceptional endpoint zeros. This supplies
a genuine finite rational state update on the stated generic locus.
The current assumptions need not hold for the output, so the claim
does not extend automatically to an infinite generic orbit.

## 10. Exact local identity controls

The original-row checker `check_raw_hp_homogeneous_ode.py` was extended
to test (3) at both logarithmic poles without numerical evaluation:
it verifies divisibility by D of
$A_3'C'-(A_2'-A_3''-A_1)C$, after checking gcd(Q,D)=1. The n=1,2,4
original Taylor rows all pass. These checks supplement the local
Laurent derivation and assert no all-degree genericity.
