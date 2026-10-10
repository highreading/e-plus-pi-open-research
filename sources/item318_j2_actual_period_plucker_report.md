> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 318 - actual-period incidence after the ordinary $j=2$ determinant gate

Checked: 2026-08-31 (Beijing time)

## 1. Scope and verdict

Retain the actual ordinary row



$$
p=2r+6s+3,\qquad r=2h+1,\qquad c=2^{2s},
 \tag{1.1}
$$



and the Items 250/291 connection-plane form



$$
G_\nu=f_\nu Z+9c b_\nu-11d_\nu,\qquad \nu=0,1.
 \tag{1.2}
$$



Item 314 controls the earlier endpoint determinant branch.  This item does
not repeat its resultant, its two endpoint branches, or either cubic-character
factor.  It asks the logically later question: after the determinant has
vanished, when does the formal common value of $Z$ equal the actual
incomplete-beta/logarithmic period?

Put



$$
f=\binom{f_0}{f_1},\quad b=\binom{b_0}{b_1},\quad
 d=\binom{d_0}{d_1},\quad
 g=fZ+9cb-11d,
 \tag{1.3}
$$



and define the three connection-plane minors



$$
\ell=\det(f,b),\qquad m=\det(f,d),\qquad C=\det(b,d).
 \tag{1.4}
$$



The old determinant and two transverse exterior residuals are



$$
\begin{aligned}
 D&=\det(f,g)=9c\ell-11m,\\
 E_b&=\det(g,b)=\ell Z+11C,\\
 E_d&=\det(g,d)=mZ+9cC.
 \end{aligned}
 \tag{1.5}
$$



They satisfy the exact syzygy



$$
\boxed{11E_d-9cE_b=-DZ.}
 \tag{1.6}
$$



> **PROVED - exact actual-period condition on every nondegenerate chart.**
> On $D=0$ and $\ell\ne0$, the formal value is
> 

$$
> Z_{\rm form}=-\frac{11C}{\ell},
> \tag{1.7}
>
$$


> and the original simultaneous collision is equivalent to the single,
> division-free condition
> 

$$
> \boxed{
> \ell B_s\left(\frac{9\kappa_r}{2}A_s-\tau_{r,s}\right)+11C=0.}
> \tag{1.8}
>
$$


> On $D=0$ and $m\ne0$, the corresponding formula is
> 

$$
> Z_{\rm form}=-\frac{9cC}{m},\qquad
> \boxed{
> mB_s\left(\frac{9\kappa_r}{2}A_s-\tau_{r,s}\right)+9cC=0.}
> \tag{1.9}
>
$$



Here $B_s,A_s,\tau_{r,s}$ are exactly those of Item 251:



$$
Z_{\rm act}=B_s\left(\frac{9\kappa_r}{2}A_s-\tau_{r,s}\right).
 \tag{1.10}
$$



> **PROVED - exterior codimension and scoped no-go.**  If
> $\operatorname{span}(f,b,d)$ has rank two, then
> 

$$
> g=0\quad\Longleftrightarrow\quad D=E_b=E_d=0.
> \tag{1.11}
>
$$


> On $D=0$, equation (1.6) leaves at most one independent transverse
> exterior condition.  If the span has rank at most one, every pairwise
> exterior minor vanishes for every $Z,c$.  Therefore no tower made only
> from determinants of $f,b,d,g$ can distinguish a nonzero collinear
> residual from the zero residual on that chart.

This is a global structural reduction, not a weighted prime theorem.  It
books no Route-1 gain and does not reduce the retained ordinary-$j=2$
ceiling $1/105$ per $6M$.

## 2. Admission and capacity audit

The relevant fixed-family relation is



$$
2M=5r+14s+7.
 \tag{2.1}
$$



The new residual is admitted only as a **Closer target** internal to the
already retained determinant branch:

1. An original collision forces it exactly, because $g=0$ forces every
   determinant in (1.5) to vanish.
2. In the universal rank-two connection plane it is not a consequence of
   $D=0$.  Thus it is a genuinely transverse formal condition.
3. On the actual arithmetic family, no theorem here bounds the weighted set
   of primes dividing its cleared numerator on the fixed-$M$ slices.
4. Height, diagonality, or a fitted recurrence alone cannot affect the
   $1/105$ ceiling.  Such expansions are therefore not undertaken.

Consequently



$$
\boxed{\text{new capacity reduction}=0},\qquad
 \boxed{\text{new booking}=0}.
 \tag{2.2}
$$



## 3. The exterior identities

Expanding determinants in (1.5) gives



$$
\begin{aligned}
 \det(f,g)
 &=\det(f,9cb-11d)=9c\ell-11m,\\
 \det(g,b)
 &=Z\det(f,b)-11\det(d,b)=\ell Z+11C,\\
 \det(g,d)
 &=Z\det(f,d)+9c\det(b,d)=mZ+9cC.
 \end{aligned}
 \tag{3.1}
$$



Therefore



$$
\begin{aligned}
 11E_d-9cE_b
 &=11mZ+99cC-9c\ell Z-99cC\\
 &=(11m-9c\ell)Z=-DZ,
 \end{aligned}
 \tag{3.2}
$$



which proves (1.6) over any commutative ring.  No modular division is used.
The rank and chart equivalences below are field statements, applied to the
actual residue field $\mathbb F_p$.

If $D=0$, then $g$ is collinear with $f$.  On the $\ell\ne0$
chart, $f,b$ are a basis.  A vector collinear with both is zero, so



$$
D=0,\ \ell\ne0:\qquad g=0\Longleftrightarrow E_b=0.
 \tag{3.3}
$$



The same argument with the basis $f,d$ proves the $m\ne0$ chart.
Substitution of (1.10) yields (1.8) and (1.9).  These displayed residuals,
not the divided values in (1.7) and (1.9), are the certified modular tests.

## 4. Independence and resonance are different statements

The coefficient $C$ is not a formal function of $(\ell,m)$ in the
universal $2$-by-$3$ connection plane.  For example, take



$$
f=(1,0),\quad b=(x,2),\quad d=(y,3).
 \tag{4.1}
$$



Then $(\ell,m)=(2,3)$ is fixed while



$$
C=3x-2y
 \tag{4.2}
$$



varies.  More directly, over characteristic different from $11$, take



$$
f=(1,0),\quad b=(0,1),\quad d=(0,9/11),\quad c=1.
 \tag{4.3}
$$



Then $D=0$ identically and $E_b=Z$.  Hence $E_b$ is not in the
universal ideal generated by $D$.

This proves formal independence on the determinant-zero locus.  It does
**not** prove arithmetic independence along the tied family (2.1), nor any
positive or zero weighted density.

Equation (1.6) proves the complementary resonance statement: once $D=0$,
the two exterior residuals cannot provide two new conditions.  For
$p\ne11$, $E_b$ and $E_d$ are scalar-equivalent.  At $p=11$,
$D=0$ forces $\ell=0$, because $9c$ is a unit; $E_b$ is then
automatic and $E_d$ is the surviving exterior test.  Thus the second
chart covers this finite coefficient characteristic without discarding it.

## 5. Every degenerate chart

There are two genuinely degenerate possibilities.

### 5.1 The columns span a line

If $f,b,d$ all lie on one line, then



$$
\ell=m=C=0.
 \tag{5.1}
$$



All exterior residuals in (1.5) vanish for every $Z,c$, although the
collinear vector $g$ need not be zero.  One original coordinate equation
$G_\nu=0$, with a certified nonzero coordinate on that chart, is
unavoidable.  Adding further determinants cannot repair this loss.

### 5.2 The period column vanishes

If $f=0$, then $Z$ is irrelevant and



$$
g=9cb-11d.
 \tag{5.2}
$$



When $C\ne0$, the vectors $b,d$ are independent and (5.2) cannot
vanish; at least one of $11C$ or $9cC$ detects that obstruction.
When $C=0$, all columns again span at most a line and the individual
coordinate equation is necessary.  This is exactly the rank-aware branch
already required by Item 251, now expressed without unsafe division.

## 6. All-row $p$-unit clearing

Let $Q_{r,s}$ be six times the product of the reduced denominators of



$$
f_0,f_1,b_0,b_1,d_0,d_1,B_s,\kappa_r,\tau_{r,s}.
 \tag{6.1}
$$



Items 250 and 251 proved that every denominator in (6.1) is a $p$-unit
on every actual row.  Every actual prime satisfies $p>3$, so the added
factor $6$ is also a unit.  Therefore



$$
p\nmid Q_{r,s}.
 \tag{6.2}
$$



Each basic rational multiplied by $Q_{r,s}$ is integral.  Hence



$$
Q_{r,s}^2D\in\mathbb Z,\qquad
 Q_{r,s}^4E_b(Z_{\rm act})\in\mathbb Z,\qquad
 Q_{r,s}^4E_d(Z_{\rm act})\in\mathbb Z.
 \tag{6.3}
$$



The fourth power is a safe uniform clearer, not a claim of minimality.
Because (6.2) holds, the cleared integer vanishes modulo $p$ exactly
when the rational residual does.  In particular, the test never divides
by $\ell$ or $m$; rows on either zero chart remain present.

No Item-314 hypergeometric cube, endpoint resultant, or Item-315
cubic-character factor is included in this clearer or booked again.

## 7. Deterministic finite replay

The certificate replays the exact rational identities on the nine known
Item-250 determinant-zero rows.  Every one has $\ell\ne0\pmod p$, and
the transverse residual is nonzero, so all nine remain certified false
positives for determinant sufficiency.  For example,



$$
\begin{array}{c|c|c|c|c|c}
(p,s,r)&\ell&C&E_b&G_0&G_1\\ \hline
(271,7,113)&134&46&137&173&136\\
(367,39,65)&88&330&29&238&354\\
(953,158,1)&392&96&507&0&374
\end{array}
\tag{7.1}
$$



All entries are reduced modulo $p$.  The full bounded census through
$p\le401$ contains three determinant-zero rows, no
determinant-zero/$\ell$-zero row, and no actual collision.  These are
**EXACT FINITE ONLY / DIAGNOSTIC** facts.  They are not used in any global
or weighted claim.

## 8. Strategic conclusion

Item 318 supplies the exact incidence missing between the formal
determinant gate and the actual incomplete-beta period:



$$
\boxed{D=0\quad+\quad E_{\rm actual}=0.}
 \tag{8.1}
$$



On rank-two charts, $E_{\rm actual}$ is a genuine new formal condition.
The entire exterior tower nevertheless has transverse codimension only one,
and it is blind on rank-at-most-one charts.  The next admissible theorem
would therefore have to control the fixed-$M$ weighted prime support of
the cleared numerator in (1.8) or (1.9), or provide a non-exterior
coordinate theorem on the degenerate chart.  P-recursiveness or numerator
height alone is not enough.

## 9. Strict labels

**PROVED**

- the three Plucker identities and exact syzygy (1.6);
- both nondegenerate formal values and division-free actual-period tests;
- logical necessity under the original collision;
- universal independence of the transverse residual on $D=0$;
- the rank-at-most-one determinant-only no-go;
- the all-row $p$-unit clearing; and
- zero Route-1 booking.

**EXACT FINITE ONLY / DIAGNOSTIC**

- the nine declared determinant-zero replays and the $p\le401$ chart
  census.

**OPEN**

- a fixed-$M$ weighted zero-density theorem for the cleared actual-period
  residual;
- arithmetic independence of $C$ on the actual family;
- a non-exterior coordinate theorem on the rank-at-most-one chart; and
- any reduction of the retained $1/105$ ceiling.
