> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 352 - chosen-prime transition and formal sublinear-window no-go

Checked: 2026-09-01 (Beijing time)

## 1. Scope, capacity, and verdict

Retain the actual ordinary-$j=2$ phase



$$
p=2r+6s+3=6m+2d+1,
 \qquad m=s-1,
 \qquad d=r+4,
\tag{1.1}
$$



and put



$$
L=m+1=s,
 \qquad
 h_u=\frac1{8^u}\binom{2u}{u},
 \qquad
 H_{L-1}=\sum_{u=0}^{L-1}h_u.
\tag{1.2}
$$



Items 344 and 347 gave the exact quadratic complete-sum model and
proved that its canonical semisimple Kummer lift has rank at least
$L$.  The remaining possibility addressed here is whether the same
chosen-prime arithmetic has a bounded nonsemisimple compression whose
Jordan or $p$-curvature data adds a companion condition to the actual
collision.

The answer is exact for the natural transition category.

> **PROVED - exact rank-two transition and complete matrix moment.**
> For $x\in\mathbf F_p^*$, let
> 

$$
> A_x=\begin{pmatrix}x^{-1}&1\\0&1\end{pmatrix}.
>
$$


> Then
> 

$$
> A_x^L=
> \begin{pmatrix}
> x^{-L}&\displaystyle\sum_{u=0}^{L-1}x^{-u}\\0&1
> \end{pmatrix},
>
$$


> and, for the quadratic character $\chi$,
> 

$$
> \boxed{
> \mathscr M_L:=\sum_{x\ne0}\chi(1-x/2)A_x^L
> =\begin{pmatrix}-h_L&-H_{L-1}\\0&-1\end{pmatrix}.}
>
$$



> **PROVED - the actual nondegenerate collision uses exactly the old
> two coordinates.**  At $x=1/4$,
> 

$$
> \det(A_{1/4}^L)=4^L.
>
$$


> Hence Item 341's collision gate is precisely
> 

$$
> \boxed{
> \det(A_{1/4}^L)=c_r^*,
> \qquad
> (\mathscr M_L)_{12}=-\Theta_{r,s}.}
>
$$


> The first equation is the existing $4^L=c_r^*$ condition and the
> second is the existing $H_{L-1}=\Theta_{r,s}$ condition.  No third
> condition appears.

> **PROVED - exact chosen-prime Jordan data.**  For $x\ne1$,
> $A_x^p=A_x$ and $A_x^{p-1}=I$.  At the unique nonsemisimple
> fiber $x=1$, if $N=E_{12}$, then
> 

$$
> A_1=I+N,
> \qquad A_1^p=I,
> \qquad A_1^L=I+LN.
>
$$


> Its exact weighted contribution to the extension coordinate is
> $L\chi(1/2)=L(2/p)$.  This is one summand of the already present
> $-H_{L-1}$, not an independent companion digit.

> **PROVED - global Jordan codimension does not increase.**  If
> $h_L\ne1$, then $\mathscr M_L$ is conjugate to
> $\operatorname {diag}(-h_L,-1)$; its extension coordinate is not a
> conjugacy invariant.  If $h_L=1$, then
> 

$$
> \mathscr M_L=-I-H_{L-1}E_{12},
>
$$


> so the entire nonsemisimple part is the single coordinate already
> targeted by $H_{L-1}=\Theta_{r,s}$.  Traces, determinants, powers,
> and polynomial matrix invariants add no codimension on either stratum.

> **PROVED - zero $p$-curvature of the fixed quadratic line.**  The
> generating function
> 

$$
> F(z)=\frac1{(1-z)\sqrt{1-z/2}}
>
$$


> defines the rank-one connection $d-d\log F$.  The tame quadratic
> cover $y^2=1-z/2$ makes $F=1/[y(2y^2-1)]$ rational, hence gauges
> the connection to the trivial one.  Its $p$-curvature is therefore
> zero for every odd good prime.  There is no nonzero curvature
> coordinate to append to the gate.

> **PROVED - scoped bounded/sublinear-window no-go.**  The rank-two
> compression retains linear complexity: the conjugacy invariants
> 

$$
> \operatorname {tr}(A_x^L)=1+x^{-L},
> \qquad \det(A_x^L)=x^{-L}
>
$$


> have pole order $L$ at $x=0$.  More generally, if an exact
> $n$-state companion retains this determinant and every entry has
> pole order at most $K$, the Leibniz formula gives
> $nK\ge L$.  Thus bounded local pole order forces linear state rank.
> A $D$-step truncation leaves the
> exact tail $H_{L-1}-H_{D-1}$.  As a symbolic Laurent weight, the
> truncation is identically exact only for $D\ge L$.  Thus a
> universally/formally exact choice $D=o(M)$ reaches only the
> $L=o(M)$ edge, whose logarithmic prime mass is $o(M)$ by Item 344.
> For $D<L$, pointwise equality can still occur through accidental
> vanishing of the tail period; weighted control of those primes is new
> arithmetic and remains open.  On every positive-rate bulk, an exact
> symbolic realization has semisimple rank or transition/pole length
> $\Omega(M)$.

> **OPEN.**  This does not rule out every imaginable target-specific,
> $p$-dependent nonlinear sheaf.  Weighted nonconcentration for the
> actual moving target remains open on the nondegenerate chart, and
> weighted support of Item 349's safely saturated carrier remains open
> on the degenerate chart.

No weighted prime mass has changed.  Therefore



$$
\boxed{\text{new booking}=0},
 \qquad
 \boxed{\text{new capacity reduction}=0},
 \qquad
 \boxed{\text{ordinary-}j=2\text{ ceiling remains }1/105}.
\tag{1.3}
$$



No finite prime scan or collision census is used.

## 2. The exact nonsemisimple transition

For a scalar $a$ and $L\ge1$, direct multiplication gives



$$
\begin{pmatrix}a&1\\0&1\end{pmatrix}^{L}
 =\begin{pmatrix}
 a^L&1+a+\cdots+a^{L-1}\\0&1
 \end{pmatrix}.
\tag{2.1}
$$



Taking $a=x^{-1}$ proves



$$
\boxed{
 A_x^L=\begin{pmatrix}x^{-L}&W_L(x)\\0&1\end{pmatrix},
 \qquad
 W_L(x)=\sum_{u=0}^{L-1}x^{-u}.}
\tag{2.2}
$$



This is a genuine rank-two nonsemisimple compression of the $L$
individual Kummer modes.  It is exact over the function field, not
merely pointwise on a declared set of primes.

The compression does not make its moving length disappear.  Both trace
and determinant are invariant under rational conjugacy, and (2.2)
gives



$$
\boxed{
 \operatorname {tr}(A_x^L)=1+x^{-L},
 \qquad
 \det(A_x^L)=x^{-L}.}
\tag{2.3}
$$



Thus every rational transition conjugate to (2.2) still exposes a pole
of exact order $L$ at $x=0$.  Rank has fallen from $L$ to two, but
the exact transition order has grown to $L$.

There is a useful rank-pole form that includes larger nonsemisimple
companions.  Let $B_L(x)$ be an exact $n$-state transition whose
determinant is $x^{-L}$ times a unit at $x=0$, as required when the
canonical determinant coordinate is retained.  If every entry of
$B_L$ has pole order at most $K$, every Leibniz monomial in its
determinant has pole order at most $nK$.  Therefore



$$
\boxed{nK\ge L.}
\tag{2.4}
$$



In particular, bounded $K$ forces state rank $n=\Omega(L)$.  The
rank-two matrix (2.2) attains the other side of the tradeoff by taking
$K=L$.  This statement applies to exact companions retaining the
canonical determinant; it does not impose a determinant on an
unrelated target-specific object.

## 3. Completing all quadratic moments at once

Item 347 proved, for every integer $u$ in the actual range,



$$
\boxed{
 -\sum_{x\in\mathbf F_p^*}x^{-u}\chi(1-x/2)=h_u\pmod p.}
\tag{3.1}
$$



The tied phase gives $L<(p-1)/2$, so (3.1) applies to
$u=0,1,\ldots,L$.  Applying it entrywise to (2.2) yields



$$
\begin{aligned}
 (\mathscr M_L)_{11}
 &=\sum_{x\ne0}x^{-L}\chi(1-x/2)=-h_L,\\
 (\mathscr M_L)_{12}
 &=\sum_{u=0}^{L-1}\sum_{x\ne0}x^{-u}\chi(1-x/2)
   =-H_{L-1}.
 \end{aligned}
\tag{3.2}
$$



The complete sum of the nontrivial character along the affine linear
argument is zero when $x=0$ is included.  Its omitted $x=0$ term is
$1$, so



$$
\sum_{x\ne0}\chi(1-x/2)=-1.
\tag{3.3}
$$



Equations (3.2)-(3.3) prove the matrix identity



$$
\boxed{
 \mathscr M_L
 =\sum_{x\ne0}\chi(1-x/2)A_x^L
 =\begin{pmatrix}-h_L&-H_{L-1}\\0&-1\end{pmatrix}.}
\tag{3.4}
$$



Unlike a fixed-target surrogate, (3.4) retains the full moving cutoff
and the actual exponent $L=s$.

## 4. Exact collision coordinates and absence of a companion invariant

At the distinguished point $x=1/4$, formula (2.2) becomes



$$
A_{1/4}^L
 =\begin{pmatrix}
 4^L&(4^L-1)/3\\0&1
 \end{pmatrix}.
\tag{4.1}
$$



The denominator $3$ is a tied-prime unit.  Hence every local matrix
entry in (4.1) is already a function of the determinant $4^L$.  Item
341's nondegenerate normal form



$$
4^L=c_r^*,
 \qquad H_{L-1}=\Theta_{r,s}pmod p
\tag{4.2}
$$



is exactly



$$
\boxed{
 \det(A_{1/4}^L)-c_r^*=0,
 \qquad
 (\mathscr M_L)_{12}+\Theta_{r,s}=0.}
\tag{4.3}
$$



In particular,



$$
\mathscr M_L+\Theta_{r,s}E_{12}
 =\begin{pmatrix}-h_L&\Theta_{r,s}-H_{L-1}\\0&-1\end{pmatrix}
\tag{4.4}
$$



is diagonal precisely when the second old collision coordinate
vanishes.  This is a repackaging of that coordinate, not a new one.

There is also an exact all-polynomial statement.  For any polynomial
$Q$, the upper-right entry of $Q(\mathscr M_L)$ is



$$
-H_{L-1}
 \frac{Q(-h_L)-Q(-1)}{1-h_L}
 \quad(h_L\ne1),
\tag{4.5}
$$



with limiting value $-H_{L-1}Q'(-1)$ when $h_L=1$.  Thus every
power or polynomial readout remains in the one-dimensional extension
line generated by $H_{L-1}$.  Meanwhile



$$
\det(TI-\mathscr M_L)=(T+h_L)(T+1)
\tag{4.6}
$$



does not see the extension at all.

The same ideal statement covers the standard finite tensor operations.
Write $\delta=\Theta_{r,s}-H_{L-1}$ and



$$
B_L=\mathscr M_L+\Theta_{r,s}E_{12}
 =\begin{pmatrix}-h_L&\delta\\0&-1\end{pmatrix}.
\tag{4.7}
$$



Every entry of a fixed tensor, symmetric, exterior, or polynomial
construction on $B_L$ is a polynomial in $\delta$.  Its difference
from the diagonal specialization $\delta=0$ is divisible by
$\delta$.  Consequently every nilpotent companion readout belongs to
the old ideal $(H_{L-1}-\Theta_{r,s})$; diagonal readouts can involve
$h_L$, but the actual collision forces no value of $h_L$.  These
standard functorial companions therefore add no codimension.

If $h_L\ne1$, the upper-triangular conjugation with parameter



$$
t=\frac{H_{L-1}}{1-h_L}
\tag{4.8}
$$



diagonalizes $\mathscr M_L$.  If $h_L=1$, then



$$
\mathscr M_L=-I-H_{L-1}E_{12},
 \qquad
 (\mathscr M_L+I)^2=0.
\tag{4.9}
$$



So even on the repeated-eigenvalue locus, the only Jordan coordinate
is the already targeted $H_{L-1}$.  The collision imposes no separate
condition on $h_L$; treating $h_L=1$, or any other chosen value, as
mandatory would be an invalid strengthening of the actual gate.

## 5. Chosen-prime $p$-step and $p$-curvature data

Write $a=x^{-1}$.  If $x\ne1$, then $a\ne1$, and



$$
1+a+\cdots+a^{p-1}=1,
\tag{5.1}
$$



because $1+a+\cdots+a^{p-2}=0$ and $a^{p-1}=1$.  Therefore



$$
\boxed{A_x^p=A_x,\qquad A_x^{p-1}=I\quad(x\ne1).}
\tag{5.2}
$$



At $x=1$, put $N=E_{12}$.  Since $N^2=0$,



$$
\boxed{
 A_1=I+N,
 \qquad A_1^p=I,
 \qquad A_1^L=I+LN.}
\tag{5.3}
$$



Thus $x=1$ is the unique nonsemisimple fiber.  Its character weight
is



$$
\chi(1-1/2)=\chi(1/2)=\chi(2),
\tag{5.4}
$$



so its exact contribution to $(\mathscr M_L)_{12}$ is



$$
\boxed{L\chi(2)=L(2/p).}
\tag{5.5}
$$



There is no implication that the other $p-2$ fibers cannot cancel
this contribution.  Equation (3.4) shows that the completed answer is
exactly $-H_{L-1}$, and the collision already supplies its legitimate
moving target.

The natural scalar connection likewise contributes no new curvature
condition.  From



$$
F(z)=\sum_{m\ge0}H_mz^m
 =\frac1{(1-z)\sqrt{1-z/2}}
\tag{5.6}
$$



one has



$$
\frac{F'}F=\frac1{1-z}+\frac1{2(2-z)}.
\tag{5.7}
$$



On the tame cover $y^2=1-z/2$, so that
$z=2-2y^2$,



$$
F=\frac1{y(2y^2-1)},
 \qquad
 \left(\frac{F'}F\right)\frac{dz}{dy}
 =-\frac1y-\frac{4y}{2y^2-1}
 =\frac d{dy}\log F.
\tag{5.8}
$$



Hence the pullback of $d-d\log F$ is gauge-equivalent to the trivial
connection.  The cover has degree two, prime to every actual odd
prime; faithful pullback then gives zero $p$-curvature downstairs.
This proves a structural zero, not a new Hasse digit.

All of (5.2)-(5.8) is taken at the actual selected prime $p$.  It does
not identify reductions at different tied primes through a common
complex embedding, and it supplies neither Archimedean smallness nor a
Frobenius equidistribution theorem.  Such an inference would require
new arithmetic input beyond the exact transition identities.

## 6. Exact truncation tails and the complexity dichotomy

For $0\le D\le L$, put



$$
W_D(x)=\sum_{u=0}^{D-1}x^{-u},
 \qquad H_{-1}=0.
\tag{6.1}
$$



Subtracting the two exact complete sums gives



$$
\boxed{
 H_{L-1}-H_{D-1}
 =-\sum_{x\ne0}\chi(1-x/2)
   \sum_{u=D}^{L-1}x^{-u}.}
\tag{6.2}
$$



Consequently a $D$-step companion window has only two possibilities.

1. If it discards the tail, it is identical to the full Laurent weight
   for all inputs only when $D\ge L$.
2. If $D<L$, it may agree at an individual chosen prime only when the
   additional tail period in (6.2) vanishes modulo $p$.
3. If it retains that tail, (6.2) is precisely the moving arithmetic
   period that the compression was meant to control.

The first statement is a formal identity statement: the Laurent
polynomial $W_L-W_D=\sum_{u=D}^{L-1}x^{-u}$ is nonzero for $D<L$.
It does **not** assert that its character-weighted complete sum is
nonzero at every actual prime.  Such pointwise cancellation is an open
zero-density problem, not something the transition algebra excludes.

Now fix $M$.  The actual relations are



$$
5p=4M+2m+3,
 \qquad r=6M-7p.
\tag{6.3}
$$



If $D=D(M)=o(M)$, the rows on which a discarded-tail window is
**formally and uniformly** exact satisfy $L\le D=o(M)$, hence
$m=o(M)$.  Item 344 proves that these edge rows carry only $o(M)$
logarithmic prime mass.  Every positive-rate bulk has
$m\ge\delta M$ after removal of such edges, so there $L\asymp M$.
This says nothing by itself about the exceptional rows with $D<L$
and a vanishing tail period.

This yields the exact natural-class dichotomy:



$$
\boxed{
 \begin{array}{c}
 \text{semisimple Kummer unrolling: rank at least }L,\\[2mm]
 \text{rank-two nonsemisimple compression: invariant pole/transition
 length }L,\\[2mm]
 \text{general exact bounded-pole companion: }nK\ge L.
 \end{array}}
\tag{6.4}
$$



Thus a bounded or sublinear nonsemisimple window has zero-rate
**formal/uniform** exact reach.  On a positive-rate bulk, bounded local
pole order forces linear state rank, while bounded rank forces linear
pole/transition order.  Accidental pointwise tail cancellation remains
outside this no-go and requires a weighted nonconcentration theorem.
This theorem concerns exact powers of the canonical
transition, their rational conjugates and polynomial readouts, and
their truncation windows.  It does not claim that every exotic
$p$-dependent nonlinear construction must arise in this category.

## 7. Degenerate chart and overlap audit

Item 341 and Item 349 partition the same raw tied-prime family into the
outer charts



$$
\ell_r\ne0
 \qquad\text{and}\qquad
 \ell_r=0.
\tag{7.1}
$$



On $\ell_r\ne0$, the exact implication is (4.2)-(4.3).  On
$\ell_r=0$, the affine normalization used to obtain those two
coordinates is unavailable: an original collision forces the safely
saturated triple-minor carrier of Item 349, together with its remaining
coordinate condition.  It does **not** force
$4^L=c_r^*$ or $H_{L-1}=\Theta_{r,s}$.  Imposing the matrix gate on
that chart would therefore be logically invalid.

Inside Item 349's carrier, the two cases $f\ne0$ and $f=0$ give the
exact two-sequence and $f/K$ gcd branches.  They partition the
degenerate carrier support; they are not two new additive reservoirs.

The fixed-$M$ prime interval remains



$$
\frac{4M+3}{5}\le p\le\frac{6M-1}{7},
\tag{7.2}
$$



with raw Chebyshev mass



$$
\vartheta\left(\frac{6M-1}{7}\right)
 -\vartheta\left(\frac{4M+3}{5}\right)
 =\frac{2}{35}M+o(M).
\tag{7.3}
$$



Therefore the nondegenerate and degenerate collision masses together
satisfy one bound



$$
W_{\rm nd}(M)+W_{\rm deg}(M)
 \le\frac{2}{35}M+o(M),
\tag{7.4}
$$



not two copies of it.  Normalizing by $6M$ gives the single raw
ceiling



$$
\frac1{6}\frac2{35}=\frac1{105}.
\tag{7.5}
$$



The transition/Jordan theorem neither shrinks (7.4) nor books any part
of it.

## 8. Strict labels and deterministic replay

The companion certificate verifies:

- the exact rational transition-power identity;
- the complete matrix moment on seven declared actual rows;
- every fiberwise $p$-step identity and the unique Jordan
  contribution on those rows;
- the actual determinant and moving-target extension residuals inherited
  from Item 341;
- trace/determinant independence from the extension in several powers;
- both global Jordan strata; and
- the exact truncation-tail identity for declared windows.

Those bounded rows and digests are **EXACT FINITE ONLY** and are not a
prime or collision census.  The all-$L$ matrix identities, tame-cover
trivialization, invariant pole-order theorem, sublinear-edge theorem,
and overlap audit are **PROVED** symbolically in this report.

The following remain **OPEN**:

1. weighted nonconcentration of the actual pair
   $(4^L,H_{L-1})$ against $(c_r^*,\Theta_{r,s})$;
2. $o(M)$ weighted support of Item 349's safely saturated moving
   carrier; and
3. a legitimate target-specific chosen-prime construction outside the
   exact transition/Kummer/window classes closed here; and
4. weighted control of primes for which a proper truncation tail in
   (6.2) vanishes accidentally.

These are the first missing arithmetic inputs.  A larger finite scan,
an unforced equation for $h_L$, or another polynomial readout of
$\mathscr M_L$ cannot replace them.
