> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 252 — Frobenius normalization of the final diagonal and a scalar fixed-degree barrier

Checked: 2026-08-31 (Beijing time)

## 1. Scope and verdict

Let



$$
p=2r+6s+3,\qquad s\geq1,\qquad r\geq1\text{ odd},\qquad 3\nmid r,
 \tag{1.1}
$$



be an actual ordinary-$j=2$ row, and put



$$
A_s=\sum_{j=0}^{2s-1}\binom{3s-1}{s+j}\binom{s+j-1}{j}
     =[x^{s-1}]\frac{(2+x)^{3s-1}-1}{1+x}.          \tag{1.2}
$$



The exact recurrence and representations of $A_s$ were established in
Item 251.  This item asks whether the special relation (1.1) removes the
moving diagonal period modulo $p$.

Set



$$
m=s-1,\qquad d=r+2,\qquad
 h_j=\frac{(1/2)_j}{j!2^j},\qquad H_m=\sum_{j=0}^m h_j,               \tag{1.3}
$$



and define the fixed-$r$ boundary polynomial



$$
P_d(m)=\sum_{k=1}^{d}\frac1{2^k}
                 \frac{(m+1/2)_k}{(1/2)_k}.                         \tag{1.4}
$$



> **PROVED — exact one-period Frobenius normal form.** On every row
> (1.1), with $\varepsilon_2=(2/p)=2^{(p-1)/2}\pmod p$,
> 

$$
> \boxed{
> A_s=(-1)^m\left\{
> \varepsilon_2\bigl(H_m-h_mP_d(m)\bigr)-1
> \right\}\pmod p.}                                                \tag{1.5}
>
$$


> Thus all parameter shifts depending on $r$ reduce to a boundary
> polynomial of degree $d$, but the single universal truncated
> half-binomial period $H_m$ remains.

> **PROVED — all denominators in (1.5) are $p$-units.** No factor
> crossing $p$ is canceled or inverted.  The precise bounds are in
> Section 5.

> **PROVED — scalar fixed-degree barrier.** A scalar Gosper
> removal of $H_m$ would require
> 

$$
> \frac{2x+1}{4x+4}R(x+1)-R(x)=1.                                  \tag{1.6}
>
$$


> There is no solution $R\in K(x)$ over any characteristic-zero
> constant field $K$ (in particular $K=\mathbf Q(r)$).  More strongly, for every
> prime $p\ge5$, every solution in
> $\overline{\mathbf F}_p(x)$, if one exists, has denominator degree
> at least $(p-1)/2$, where numerator and denominator are reduced over
> $\overline{\mathbf F}_p$.  Hence no scalar rational telescoper of uniformly
> fixed degree can remove this period in characteristic $p$.

> **OPEN.** The barrier concerns the scalar contiguous/Gosper ansatz
> (1.6).  It does not rule out a phase-only identity at the single index
> $m=(p-2r-9)/6$, a higher-rank Cartier relation, or a nonlinear
> relation involving another period.  No all-prime nonvanishing or
> weighted zero theorem for $A_s$ is proved.  This item books zero rate.

## 2. Exact coefficient and Frobenius reduction

Write



$$
N=3s-1=\frac{p-1}{2}-d.                                           \tag{2.1}
$$



Expanding the geometric denominator in (1.2) only through degree
$m=s-1$ gives the exact integer identity



$$
A_s=(-1)^m\left(
 2^N\sum_{j=0}^m\binom Nj\left(-\frac12\right)^j-1
 \right).                                                          \tag{2.2}
$$



Every $j$ in (2.2) satisfies $0\le j\le m<p$.  In
$\mathbf F_p$,



$$
N\equiv-d-\frac12,\qquad
 \binom Nj=(-1)^j\frac{(d+1/2)_j}{j!},\qquad
 2^N=\varepsilon_2\,2^{-d}.                                      \tag{2.3}
$$



Consequently, if



$$
S_m(a)=\sum_{j=0}^m\frac{(a)_j}{j!2^j},                           \tag{2.4}
$$



then



$$
A_s=(-1)^m\left(\varepsilon_2\,2^{-d}S_m(d+1/2)-1\right)\pmod p. \tag{2.5}
$$



This is an exact Frobenius/Lucas step.  It has not replaced a moving
sum by finite evidence.

## 3. Contiguous descent to one universal period

For every rational or formal parameter $a$, truncating the elementary
identity $(1-z)(1-z)^{-a-1}=(1-z)^{-a}$ at degree $m$ gives



$$
S_m(a+1)=2S_m(a)-\frac{(a+1)_m}{m!2^m}.                            \tag{3.1}
$$



There is no endpoint at infinity in (3.1): the displayed last term is
exactly the omitted coefficient of degree $m+1$.  Iterating (3.1)
from $a=1/2$ through $a=d+1/2$ yields



$$
2^{-d}S_m(d+1/2)
 =H_m-\sum_{k=1}^d\frac1{2^k}
            \frac{(k+1/2)_m}{m!2^m}.                               \tag{3.2}
$$



The Pochhammer rectangle identity



$$
\frac{(k+1/2)_m}{m!2^m}
 =h_m\frac{(m+1/2)_k}{(1/2)_k}                                    \tag{3.3}
$$



turns (3.2) into



$$
2^{-d}S_m(d+1/2)=H_m-h_mP_d(m).                                  \tag{3.4}
$$



Substitution in (2.5) proves (1.5).  Notice the separation:
$P_d$ has fixed length and degree when $r$ is fixed, while
$H_m$ is independent of $r$ but still has moving length.

For comparison with Item 251, its first-order factor is also exactly



$$
A_{s+1}+A_s
 =4^s\frac{28s+11}{2s+1}\binom{3s-1}{s-1}.                       \tag{3.5}
$$



Indeed the apparent factor
$(28s+39)/(28s+11)$ in the ratio telescopes.  Formula (3.5) is
consistent with (1.5), but it does not evaluate the surviving partial
sum $H_m$.

## 4. No scalar rational telescoper

The summand in (1.3) satisfies



$$
\frac{h_{j+1}}{h_j}=q(j),\qquad q(x)=\frac{2x+1}{4x+4}.            \tag{4.1}
$$



A scalar hypergeometric antidifference
$h_j=R(j+1)h_{j+1}-R(j)h_j$ is therefore equivalent to (1.6).
Adding an arbitrary constant to a proposed boundary expression for
$H_m$ does not change this necessary equation.

### 4.1 Characteristic zero

Suppose $R\in K(x)$, with $K$ of characteristic zero, solves (1.6).
After extending the constant field algebraically, follow a finite chain of
poles modulo integer translation.  A right endpoint can occur only at
the pole $-1$ of $q$; a left endpoint can occur only one step to the
right of the zero $-1/2$, namely at $1/2$.  These two points are not
congruent modulo $\mathbf Z$.  Hence $R$ has no finite pole and is a
polynomial.

If $R$ has positive degree, the leading coefficient on the left of
(1.6) is multiplied by $1/2-1=-1/2$, which cannot disappear.  Thus
$R$ would be constant.  At infinity a constant must be $-2$, while
evaluation at the zero $x=-1/2$ forces it to be $-1$.  This is a
contradiction.

### 4.2 Characteristic $p$

Let $p\ge5$ and suppose (1.6) has a rational solution over
$\overline{\mathbf F}_p$, written with reduced denominator.
Translation by one has orbits of length
$p$.  On an orbit not containing the zero and pole of $q$, any pole
propagates with equal order around all $p$ points.

On the exceptional orbit, label



$$
z=-\frac12,\qquad w=-1=z+\frac{p-1}{2}.                           \tag{4.2}
$$



Away from $z,w$, cancellation in (1.6) forces equal neighboring pole
orders.  Thus the pole order is a constant $A$ on



$$
z+1,z+2,\ldots,w
$$



and a constant $B$ on the complementary arc.  The simple zero at
$z$ and simple pole at $w$ force



$$
A=B+1.                                                            \tag{4.3}
$$



If there is a pole, the least possible profile is $B=0,A=1$, already
containing $(p-1)/2$ simple poles.  If there is no finite pole, $R$
is polynomial; after clearing $4(x+1)$, the same leading-term argument
rules out every polynomial (the constant equations are inconsistent for
$p\ge5$).  Therefore



$$
\deg\operatorname{den}(R)\ge\frac{p-1}{2}.                        \tag{4.4}
$$



In particular, a denominator-degree bound $D$ fails for every
$p>2D+1$.  This is an all-prime structural theorem, not a finite scan.

## 5. Denominator and boundary audit

All divisions above are legitimate on an actual row.

First, for every truncated index,



$$
0\le m=s-1<p,\qquad
 1\le j\le m\Longrightarrow j\in\{1,\ldots,p-1\}.                 \tag{5.1}
$$



Powers of two are units because $p$ is
odd.  In (1.4), the denominator factors after clearing halves are



$$
1,3,\ldots,2d-1,\qquad 2d-1=2r+3=p-6s<p.                         \tag{5.2}
$$



The numerator factors in the same rectangle are positive and at most



$$
2m+2d-1=2s+2r+1=p-4s-2<p.                                       \tag{5.3}
$$



Thus neither side of (3.3) crosses a multiple of $p$.  The direct
Frobenius sum (2.4) has denominator factors $j!2^j$, again units by
(5.1).  The unique finite endpoint in the contiguous descent is retained
explicitly in (3.1), not discarded.

The assumptions $r$ odd and $3\nmid r$ describe the ordinary cell;
the algebraic identity (1.5) itself only needs (1.1), primality, and the
unit inequalities above.

## 6. Exact finite replay and strict limits

The companion checker performs, with Python's standard library only:

1. exact integer checks of the two representations of $A_s$, the
   first-order factor (3.5), and the contiguous identity;
2. row-by-row modular checks of (2.2), (2.5), and (1.5);
3. separate unit inequalities (5.1)--(5.3);
4. the characteristic-$p$ pole-orbit length and minimal valuation
   profile underlying (4.4).

Any counts or zero witnesses emitted by that checker are labeled
**EXACT FINITE ONLY**.  They prove nothing outside the stated bound.

## 7. Booking and remaining work

This item supplies a clean normal form and rules out one natural scalar
fixed-degree strategy.  It does not prove that $A_s$ is nonzero on any
positive-density set of actual rows, nor that the Item 250/251 exceptional
locus is empty.

Accordingly:



$$
\boxed{\text{new unconditional rate}=0,\qquad
        \text{capacity reduction}=0.}                              \tag{7.1}
$$



Promising routes left open are a second Cartier coordinate for $H_m$,
a phase-specific relation using $6m=p-(2r+9)$, or a joint invariant
with the Item 250 factorial period.  None is asserted here.
