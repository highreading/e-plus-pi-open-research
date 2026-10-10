> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 344 - quadratic Frobenius carrier and maximal moving-cutoff obstruction

Checked: 2026-09-01 (Beijing time)

## 1. Scope, capacity audit, and verdict

Retain the actual ordinary-$j=2$ family



$$
p=2r+6s+3=6m+2d+1,
 \qquad m=s-1,
 \qquad d=r+4,
\tag{1.1}
$$



and the tied-prime-safe saturated carrier of Item 338.  On Item 341's
nondegenerate chart, a collision is exactly the **joint** condition



$$
\boxed{4^{m+1}=c_r^*,\qquad H_m=\Theta_{r,s}\pmod p},
 \qquad
 H_m=\sum_{j=0}^m\frac1{8^j}\binom{2j}{j}.
\tag{1.2}
$$



Neither coordinate in (1.2) is discarded below.  The degenerate chart
remains localized to Item 341's primitive triple-minor carrier and is
not reclassified here.

At fixed $M$,



$$
2M=5r+14s+7,
 \qquad
 5p=4M+2m+3,
 \qquad
 r=6M-7p.
\tag{1.3}
$$



Thus the raw prime interval has Chebyshev length



$$
\left(\frac67-\frac45\right)M+o(M)
 =\frac{2}{35}M+o(M),
\tag{1.4}
$$



and the current ceiling is still $1/105$ per $6M$.

This item tests the exact recurrence and Frobenius structure of the
actual state.  The result is a global, sharply scoped obstruction.

> **PROVED - fixed Frobenius degree, maximal extraction complexity.**
> The generating function of $H_m$ has algebraic degree two, and
> $H_m$ obeys an invertible order-two polynomial recurrence modulo
> every actual tied prime.  Nevertheless, its moving prefix functional
> has maximal reduced finite-field degree $p-1$.  Its exact
> semisimple additive-character completion has all $p$ character
> modes nonzero and carries a normalization by $1/p$.

> **PROVED - positive-rate bulk theorem.**  For any
> $u(M)=o(M)$, the total logarithmic mass of fixed-$M$ rows with
> $m\leq u(M)$ or $r\leq u(M)$ is $o(M)$.  Hence direct
> bounded/sublinear-prefix methods and bounded/sublinear boundary-degree
> methods can see only a zero-rate edge.  On every fixed positive-rate
> bulk, both $m$ and $r$ are linear in $M$.

> **PROVED - scoped method-class no-go.**  A method that first replaces
> the sharp prefix by either a uniformly bounded-degree polynomial over
> $\mathbf F_p$, or a uniformly bounded number of additive-character
> modes, cannot give an exact formula for the actual $H_m$.  The
> quadratic Frobenius carrier does not change this: it reproduces the
> same moving coefficient and supplies no second condition on (1.2).

> **OPEN.**  A target-specific cancellation among all character modes,
> a bounded-conductor sheaf that retains the moving coefficient
> functional without expanding its cutoff, or a joint distribution
> theorem for $(4^{m+1},H_m)$ against
> $(c_r^*,\Theta_{r,s})$ is not ruled out.

Consequently



$$
\boxed{\text{new booking}=0},\qquad
 \boxed{\text{new capacity reduction}=0},\qquad
 \boxed{\text{ceiling remains }1/105\text{ per }6M}.
\tag{1.5}
$$



No finite zero census is used or promoted.

## 2. The exact reversible recurrence

Put



$$
h_m=\frac1{8^m}\binom{2m}{m}.
\tag{2.1}
$$



Then



$$
\frac{h_{m+1}}{h_m}=\frac{2m+1}{4m+4},
 \qquad H_{m+1}=H_m+h_{m+1}.
\tag{2.2}
$$



The generating function is



$$
F(z)=\sum_{m\geq0}H_mz^m
 =\frac1{(1-z)\sqrt{1-z/2}}.
\tag{2.3}
$$



Its first-order differential equation



$$
2(1-z)(2-z)F'(z)=(5-3z)F(z)
\tag{2.4}
$$



gives, for $m\geq1$,



$$
\boxed{
 4(m+1)H_{m+1}-(6m+5)H_m+(2m+1)H_{m-1}=0.}
\tag{2.5}
$$



Equivalently,



$$
\binom{H_{m+1}}{H_m}
 =
 \begin{pmatrix}
 \dfrac{6m+5}{4(m+1)}&-\dfrac{2m+1}{4(m+1)}\\[4pt]
 1&0
 \end{pmatrix}
 \binom{H_m}{H_{m-1}}.
\tag{2.6}
$$



On an actual row, $p=6m+2r+9$, so



$$
0<m+1<p,
 \qquad 0<2m+1<p,
 \qquad 0<6m+5<p.
\tag{2.7}
$$



The determinant $(2m+1)/(4m+4)$ is therefore a $p$-unit.  The
rank-two recurrence is reversible; it has no singular actual endpoint
that could force $H_m$ onto the moving target.

This is a useful compression for evaluation, but not a distribution
theorem.  In particular, a recurrence for the state alone gives no
bound for intersections with a target that also moves with $(r,s,p)$.

## 3. Exact tied-prime Frobenius carrier

Let



$$
n=\frac{p-1}{2}=3m+d.
\tag{3.1}
$$



For $0\leq j\leq m$,



$$
\binom nj\left(-\frac12\right)^j
 \equiv\frac1{8^j}\binom{2j}{j}\pmod p.
\tag{3.2}
$$



Hence



$$
\boxed{
 H_m\equiv[z^m]\frac{(1-z/2)^n}{1-z}\pmod p.}
\tag{3.3}
$$



The denominators are $p$-units because $m<p$.  Now work in
$\mathbf F_p[[z]]$, and let $U(z)$ be the branch satisfying



$$
U(z)^2=1-z/2,
 \qquad U(0)=1.
\tag{3.4}
$$



Frobenius gives $U(z)^p=U(z^p)$, and therefore



$$
(1-z/2)^n=U(z)^{p-1}=\frac{U(z^p)}{U(z)}.
\tag{3.5}
$$



Since $m<p$, the factor $U(z^p)$ contributes only its constant
term to the coefficient in (3.3).  Thus



$$
\boxed{
 H_m=[z^m]\frac1{(1-z)U(z)}\pmod p.}
\tag{3.6}
$$



Formula (3.6) is the complete quadratic Frobenius reduction.  It does
not eliminate the moving coefficient index $m$; it recovers exactly
the original algebraic generating function (2.3).  Thus increasing the
formal sophistication of the same quadratic carrier does not by itself
produce nonconcentration.

## 4. Exact character completion uses every mode

The obstruction can be made exact.  Define, in
$\mathbf Z[1/2]$,



$$
g_{p,j}=\binom nj\left(-\frac12\right)^j
 \quad(0\leq j\leq p-1),
 \qquad
 G_{p,m}=\sum_{j=0}^m g_{p,j}.
\tag{4.1}
$$



Here $g_{p,j}=0$ for $j>n$, and (3.2) gives
$G_{p,m}\equiv H_m\pmod p$.

Let $\zeta$ be a primitive complex $p$-th root of unity.  For
$a\in\mathbf F_p$, set



$$
\widehat I_m(a)=\sum_{u=0}^m\zeta^{-au},
 \qquad
 S_p(a)=\sum_{j=0}^{p-1}g_{p,j}\zeta^{aj}
       =\left(1-\frac{\zeta^a}{2}\right)^n.
\tag{4.2}
$$



Additive orthogonality gives the exact identity



$$
\boxed{
 pG_{p,m}=\sum_{a=0}^{p-1}
 \widehat I_m(a)\left(1-\frac{\zeta^a}{2}\right)^n.}
\tag{4.3}
$$



Every mode in (4.3) is present.  Indeed,



$$
\widehat I_m(0)=m+1\ne0,
\tag{4.4}
$$



while for $a\ne0$,



$$
\widehat I_m(a)
 =\frac{1-\zeta^{-a(m+1)}}{1-\zeta^{-a}}\ne0,
\tag{4.5}
$$



because $1\leq m+1<p$.  Fourier expansion on the additive group is
unique, so any exact completion that expands the cutoff before using
special identities of the summand necessarily has all $p$ modes.

There is also a precision cost.  After clearing powers of two, the
right side of (4.3) is the rational quantity $pG_{p,m}$.  Recovering
$G_{p,m}\bmod p$ from that completed numerator requires its rational
value modulo $p^2$, not merely modulo $p$.  Therefore an ordinary
mod-$p$ estimate for the completed modes cannot be credited as an
ordinary collision exclusion.  This is a method obstruction, not an
extra-digit booking.

## 5. The finite-field cutoff has maximal degree

There is an entirely characteristic-$p$ version that avoids roots of
unity.  Let $I_{p,m}:\mathbf F_p\to\mathbf F_p$ be the sharp prefix
indicator



$$
I_{p,m}(x)=
 \begin{cases}
 1,&x\in\{0,1,\ldots,m\},\\
 0,&x\in\{m+1,\ldots,p-1\}.
 \end{cases}
\tag{5.1}
$$



Its unique reduced interpolation polynomial is



$$
\boxed{
 \mathcal I_{p,m}(X)
 =\sum_{u=0}^m\left(1-(X-u)^{p-1}\right).}
\tag{5.2}
$$



Fermat's theorem proves the values in (5.1).  The coefficient of
$X^{p-1}$ in (5.2) is



$$
-(m+1)\ne0\pmod p,
\tag{5.3}
$$



so



$$
\boxed{\deg\mathcal I_{p,m}=p-1.}
\tag{5.4}
$$



Uniqueness follows because a polynomial of degree at most $p-1$
vanishing at all $p$ field elements is zero.  Thus the exact cutoff
has the maximum possible reduced degree on every actual row.  In
particular, no bounded-degree or $o(p)$-degree polynomial
interpolation of the cutoff is exact.

The scope is important: (5.4) closes methods that replace the cutoff
as a function before exploiting the particular summand.  It does not
exclude a target-specific identity in which the summand and cutoff
cancel together.

## 6. Fixed-$M$ edges have zero logarithmic rate

Let $u(M)=o(M)$.  From (1.3), rows with $m\leq u(M)$ have their
prime in



$$
\frac{4M+3}{5}\leq p\leq\frac{4M+2u(M)+3}{5},
\tag{6.1}
$$



an interval of length $2u(M)/5+O(1)$.  Rows with $r\leq u(M)$
have



$$
\frac{6M-u(M)}7\leq p<\frac{6M}{7},
\tag{6.2}
$$



an interval of length $u(M)/7+O(1)$.  The prime number theorem in
the form $\vartheta(x)=x+o(x)$, applied at endpoints comparable with
$M$, gives



$$
\boxed{
 \sum_{\substack{\text{actual fixed-}M\text{ rows}\\
                  m\leq u(M)\ \mathrm{or}\ r\leq u(M)}}\log p
 =o(M).}
\tag{6.3}
$$



Uniformly for fixed $\delta>0$, the same argument bounds the two
edges by $O(\delta M)+o(M)$.  Therefore all possible positive-rate
mass can be confined, up to an arbitrarily small edge loss, to



$$
m\geq\delta M,
 \qquad r\geq\delta M.
\tag{6.4}
$$



The moving boundary term in the legitimate target is



$$
P_L(m)=\sum_{k=1}^{L}2^{-k}
 \frac{(m+1/2)_k}{(1/2)_k},
 \qquad L=r+2.
\tag{6.5}
$$



As a polynomial in $m$, it has exact degree $L$, with leading
coefficient



$$
\frac{2^{-L}}{(1/2)_L}
 =\frac1{1\cdot3\cdots(2L-1)}.
\tag{6.6}
$$



This coefficient is a $p$-unit because



$$
2L-1=2r+3<p=6m+2r+9.
\tag{6.7}
$$



Consequently the positive-rate bulk is exactly the regime in which
the prefix length $m+1$ and the explicit boundary degree $r+2$
are both linear.  Studying one fixed prefix, one fixed boundary degree,
or even any sublinear family can remove at most (6.3), hence cannot
reduce the $1/105$ ceiling.

## 7. What the recurrence does and does not control

On the nondegenerate chart, Item 341 gives unit multiples



$$
D=9\ell_r(4^{m+1}-c_r^*),
 \qquad
 T_\ell=-\epsilon_pK_{r,s}\ell_r(H_m-\Theta_{r,s}).
\tag{7.1}
$$



Thus an actual collision still requires both equations in (1.2).
Equations (2.5) and (3.6) constrain the left side of the second
coordinate, but they give no recurrence or Frobenius divisor for the
moving right side $\Theta_{r,s}$, and no correlation with the first
coordinate $c_r^*$.

This limitation is formal as well as computational.  An invertible
recurrence for $H_m$ alone is compatible with an arbitrary prescribed
intersection set if the target values are left unconstrained: choose
the target equal to $H_m$ on that set and different elsewhere.  Hence
no weighted nonconcentration conclusion can logically follow from the
state recurrence without using an additional arithmetic law for the
**actual** target.  The actual target is not declared arbitrary; rather,
the missing theorem must exploit its specific connection data.

The first admissible new input is therefore one of:

1. a bounded-conductor Frobenius/sheaf model for the **joint** residual
   $(4^{m+1}-c_r^*,H_m-\Theta_{r,s})$;
2. a target-specific relation among the $p$ completed modes in (4.3)
   that survives the $1/p$ precision cost; or
3. a weighted large-sieve, monodromy, or average-gcd theorem for the
   actual moving point.

The quadratic carrier, the rank-two recurrence, bounded character
completion, and bounded finite-field interpolation are now closed as
sufficient mechanisms by themselves.

## 8. Certificate and strict labels

The deterministic companion checker verifies:

1. the exact rational recurrence and its direct prefix values;
2. the tied-prime coefficient identity and all unit inequalities;
3. the Frobenius coefficient truncation on declared actual rows;
4. the orthogonality mechanism and the nonzero exponent test for all
   $p$ additive Fourier modes;
5. the unique reduced cutoff polynomial and its exact degree $p-1$;
6. the fixed-$M$ identities and the exact boundary-degree unit test.

Any declared rows in the certificate are **EXACT FINITE REPLAY ONLY**.
The all-prime theorems are the symbolic arguments in Sections 2-7, not
an extrapolation from those rows.  No collision count is emitted.

## 9. Ledger decision

**PROVED:** fixed degree-two Frobenius carrier; reversible order-two
recurrence; exact $p$-mode character completion; maximal-degree
finite-field cutoff; zero-rate sublinear edges; scoped bounded-mode and
bounded-degree no-go.

**EXACT FINITE ONLY:** deterministic checks on the declared actual rows.

**OPEN:** weighted nonconcentration for the actual joint moving target,
target-specific cancellations across all modes, and weighted control of
the degenerate triple-minor carrier.

No new factor is booked, and no capacity is removed.
