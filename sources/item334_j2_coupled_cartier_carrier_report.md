> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 334 - the target-coupled Cartier carrier on fixed-$M$ slices

Checked: 2026-09-01 (Beijing time)

## 1. Admission and capacity audit first

Retain the actual ordinary-$j=2$ rows



$$
p=2r+6s+3,\qquad r\ge1\text{ odd},\qquad3\nmid r,
 \qquad s\ge1,                                      \tag{1.1}
$$



with



$$
m=s-1,\qquad d=r+4,\qquad n=3m+d=\frac{p-1}{2},
 \qquad q=2m+d,\qquad p=6m+2d+1.                    \tag{1.2}
$$



Let



$$
\mathcal F_{m,d}(x)=(1-x)^n(1+x)^{n+q}
 =\sum_kc_kx^k,qquad \epsilon=\left(\frac2p\right). \tag{1.3}
$$



Item 328 identified $c_p$ as the actual Cartier digit.  Item 331 then
showed why its marginal distribution cannot close the branch: on fixed
horizontal rays it is maximally concentrated.  The present item therefore
retains all of the data that may not be dropped:

1. the old determinant gate
   

$$
D=9c\ell-11\mu,qquad c=2^{2s};                 \tag{1.4}
$$


2. the moving affine target coming from
   $B_s,\kappa_r,\tau_{r,s},h_m,P_{r+2}(m)$; and
3. every nondegenerate and degenerate connection chart.

Here



$$
f=\binom{f_0}{f_1},\quad b=\binom{b_0}{b_1},\quad
 v=\binom{v_0}{v_1},\qquad
 \ell=\det(f,b),\quad\mu=\det(f,v),\quad C=\det(b,v). \tag{1.5}
$$



The letter $v$ is used for Item 318's former column $d$, so it cannot
be confused with the tied exponent $d=r+4$.

This remains a Closer branch internal to the already retained determinant
support.  Its raw ceiling is



$$
\boxed{\mathcal C_{\max}=1/105\text{ per }6M}.      \tag{1.6}
$$



The target-coupled carrier derived below is exact, but its proved height is
only



$$
\log |\text{row carrier numerator}|=O(M\log M),    \tag{1.7}
$$



and the corresponding direct aggregate bound is



$$
O(M^2\log M).           \tag{1.8}
$$



This is weaker than the existing $O(M)$ raw cell ceiling.  No
sublinear aggregate-height or average-gcd theorem is proved.  Therefore



$$
\boxed{\text{new booking}=0},\qquad
 \boxed{\text{new capacity reduction}=0},\qquad
 \boxed{\text{ordinary-}j=2\text{ ceiling}=1/105\text{ per }6M}.
                                                               \tag{1.9}
$$



## 2. Verdict

Put



$$
h_m=\frac1{8^m}\binom{2m}{m},\qquad
 P=P_{r+2}(m),\qquad
 \Phi_{r,s}=c_p+\epsilon h_mP.                     \tag{2.1}
$$



Define the target-retaining Cartier representative



$$
\boxed{
 W^{\rm C}_{r,s}=B_s\left[
 (-1)^{m+1}\frac{9\kappa_r}{2}\Phi_{r,s}
 -\tau_{r,s}\right].}                              \tag{2.2}
$$



> **PROVED - exact actual-family target substitution.**  On every actual
> row,
> 

$$
> \boxed{W^{\rm C}_{r,s}\equiv Z_{\rm act}\pmod p}, \tag{2.3}
>
$$


> with only certified $p$-unit denominators.  Thus (2.2) retains, rather
> than replaces, the moving affine target.

Define two coordinate residuals



$$
\boxed{
 \begin{aligned}
 T_\nu={}&\frac{9\kappa_r}{2}f_\nu B_s\Phi_{r,s}\\
 &+(-1)^m\left(f_\nu B_s\tau_{r,s}-9cb_\nu+11v_\nu\right),
 \qquad \nu=0,1.
 \end{aligned}}                                    \tag{2.4}
$$



> **PROVED - chart-free coordinate equivalence.**  Over $\mathbf Q$,
> 

$$
> \boxed{T_\nu=(-1)^{m+1}
> \left(f_\nu W^{\rm C}_{r,s}+9cb_\nu-11v_\nu\right).} \tag{2.5}
>
$$


> Consequently, on every actual row and on every chart,
> 

$$
> \boxed{\text{original simultaneous collision}
> \quad\Longleftrightarrow\quad T_0=T_1=0\pmod p.}  \tag{2.6}
>
$$



For a rational number $x$, let $\operatorname {num}(x)$ be its
reduced integer numerator.  Define



$$
\boxed{
 \mathfrak G_{r,s}
 =\gcd\left(
  |\operatorname {num}(D)|,
  |\operatorname {num}(T_0)|,
  |\operatorname {num}(T_1)|
 \right).}                                         \tag{2.7}
$$



Item 315's sign theorem makes $D\ne0$ over $\mathbf Q$, so
$\mathfrak G_{r,s}$ is a well-defined positive integer.

> **PROVED - smallest primitive row carrier.**  Every displayed
> denominator is a $p$-unit, and therefore
> 

$$
> \boxed{
> p\text{ is an original collision on }(r,s)
> \quad\Longleftrightarrow\quad p\mid\mathfrak G_{r,s}.} \tag{2.8}
>
$$


> Its squarefree kernel $\operatorname {rad}(\mathfrak G_{r,s})$ is the
> canonical smallest squarefree integer with the same rowwise prime
> support.

Equation (2.8) is the requested fully cleared, actual-family,
target-retaining localization.  What remains open is not the clearing but
the size of the gcd after the determinant and period numerators meet.

## 3. Derivation from the exact Cartier digit

Item 252's finite-contiguous formula uses the correction length $r+2$:



$$
A_s=(-1)^m\left\{
 \epsilon\left[H_m-h_mP_{r+2}(m)\right]-1
 \right\}\pmod p.                                  \tag{3.1}
$$



Item 328 gives



$$
H_m=\epsilon(1-c_p)\pmod p. \tag{3.2}
$$



Since $\epsilon^2=1$, substitution in (3.1) yields, in one line,



$$
\begin{aligned}
 A_s
 &\equiv(-1)^m\{(1-c_p)-\epsilon h_mP-1\}\\
 &=(-1)^{m+1}(c_p+\epsilon h_mP)
 =(-1)^{m+1}\Phi_{r,s}\pmod p.                    \tag{3.3}
\end{aligned}
$$



The exact actual period from Item 251 is



$$
Z_{\rm act}=B_s\left(\frac{9\kappa_r}{2}A_s-\tau_{r,s}\right). \tag{3.4}
$$



Equations (3.3)-(3.4) prove (2.3).  Substitution in the original two
coordinate equations



$$
G_\nu=f_\nu Z_{\rm act}+9cb_\nu-11v_\nu          \tag{3.5}
$$



and multiplication by the harmless sign $(-1)^{m+1}$ gives (2.4)-(2.5).
No connection minor is divided out, so zero-minor rows remain present.

This also proves that the target-retaining use of Item 331 is a Cartier
reparametrization of the existing actual period, not a second independent
condition.  The arithmetic content resides in the coupled gcd (2.7).

## 4. The fixed-$M$ slice

The fixed-family relation is



$$
2M=5r+14s+7.               \tag{4.1}
$$



Together with (1.1), it gives the exact maps



$$
\boxed{p=\frac{6M-r}{7}},\qquad
 \boxed{p=\frac{4M+2m+3}{5}},                      \tag{4.2}
$$



and hence



$$
\frac{4M}{5}<p<\frac{6M}{7}. \tag{4.3}
$$



Thus every relevant prime is of order $M$.  The integer solutions of
(4.1) advance by



$$
(r,s)\longmapsto(r+14,s-5), \tag{4.4}
$$



so there are $O(M)$ possible rows on one slice.

Let $\mathcal R_M$ be the actual prime rows satisfying (4.1), and put



$$
\mathfrak C_M
 =\operatorname {rad}\left(
   \prod_{(r,s)\in\mathcal R_M}\mathfrak G_{r,s}
  \right).                                         \tag{4.5}
$$



Every collision prime on the slice divides (4.5), although a prime may
also enter through the carrier of a different row.  Therefore



$$
\sum_{\substack{(r,s)\in\mathcal R_M\\
                  p\text{ is a collision}}}\log p
 \le\log\mathfrak C_M
 \le\sum_{(r,s)\in\mathcal R_M}\log\mathfrak G_{r,s}. \tag{4.6}
$$



The precise sufficient Closer theorem is now



$$
\boxed{
 \sum_{(r,s)\in\mathcal R_M}
       \log\operatorname {rad}(\mathfrak G_{r,s})=o(M).} \tag{4.7}
$$



This is a target-retaining average-gcd problem on the actual fixed-$M$
line.  It is **OPEN**.

## 5. Exterior targets and every chart

The two exterior versions of (2.4) are



$$
\boxed{
 \begin{aligned}
 T_\ell={}&\frac{9\kappa_r}{2}\ell B_s\Phi_{r,s}
 +(-1)^m(\ell B_s\tau_{r,s}-11C),\\
 T_\mu={}&\frac{9\kappa_r}{2}\mu B_s\Phi_{r,s}
 +(-1)^m(\mu B_s\tau_{r,s}-9cC).
 \end{aligned}}                                    \tag{5.1}
$$



Direct determinant expansion gives the exact rational identities



$$
\boxed{
 T_\ell=\det(T,b),\qquad T_\mu=\det(T,v),\qquad
 \det(f,T)=(-1)^{m+1}D.}                           \tag{5.2}
$$



They are the signed Item-318 exterior residuals evaluated at $W^{\rm C}$.
The syzygy becomes



$$
11T_\mu-9cT_\ell=-(-1)^{m+1}DW^{\rm C}.          \tag{5.3}
$$



The complete chart stratification is therefore as follows.

### 5.1 $\ell\ne0\pmod p$

On $D=0$, the original collision is equivalent to the one extra
condition



$$
T_\ell=0\pmod p.       \tag{5.4}
$$



The chart-specific primitive carrier is



$$
\gcd\bigl(|\operatorname {num}(D)|,
            |\operatorname {num}(T_\ell)|\bigr).  \tag{5.5}
$$



### 5.2 $\ell=0$, $\mu\ne0\pmod p$

On $D=0$, the corresponding single condition is



$$
T_\mu=0\pmod p,        \tag{5.6}
$$



with the analogous primitive gcd carrier.  This chart includes the
surviving exterior test in the special characteristic $p=11$; no
division by $11$, $\ell$, or $\mu$ is used.

### 5.3 $\ell=\mu=0$, $C\ne0\pmod p$

Then $b,v$ are independent and necessarily $f=0$.  The vector
$9cb-11v$ cannot vanish, so an original collision is impossible.  This
is a certified obstruction chart, not a discarded denominator case.

### 5.4 $\ell=\mu=C=0$, $f\ne0\pmod p$

All connection columns lie on one line and exterior tests are automatic.
Choose an index $\nu$ with $f_\nu\ne0$.  On $D=0$, the necessary
and sufficient remaining condition is the individual coordinate



$$
T_\nu=0\pmod p.        \tag{5.7}
$$



### 5.5 $\ell=\mu=C=0$, $f=0\pmod p$

The period is irrelevant.  Both original affine coordinates must vanish;
equivalently one retains $T_0=T_1=0$.  Formula (2.7) remains safe and
complete on this final chart.

Thus the coordinate carrier (2.7) is uniform, while (5.5)-(5.7) are the
smallest chartwise tests after the old gate.

## 6. Primitive clearing and the height ledger

Items 250, 251, 252, and 318 prove that the reduced denominators of



$$
f_\nu,b_\nu,v_\nu,B_s,\kappa_r,\tau_{r,s},h_m,
 P_{r+2}(m)                                          \tag{6.1}
$$



are $p$-units on every actual row.  The coefficient $c_p$ is an
integer.  Hence reducing each rational in (1.4), (2.4), and (5.1) to its
primitive numerator loses and adds no actual prime.  This proves the
clearing assertion in (2.8) without an oversized common denominator.

A safe uniform clearer can also be displayed.  Let $Q^{\rm C}_{r,s}$
be six times the product of the reduced denominators in (6.1).  Then



$$
(Q^{\rm C}_{r,s})^2D\in\mathbb Z,qquad
 (Q^{\rm C}_{r,s})^6T_\ell,
 (Q^{\rm C}_{r,s})^6T_\mu,
 (Q^{\rm C}_{r,s})^6T_0,
 (Q^{\rm C}_{r,s})^6T_1\in\mathbb Z.               \tag{6.2}
$$



The sixth power is only a safe uniform certificate.  The reduced
numerators in (2.7) are the canonical clearing and should be used for
height questions.

For completeness, the height bound is obtained as follows.

1. The absolute coefficient bound from (1.3) is
   

$$
|c_p|\le2^{2n+q},\qquad2n+q=p+q-1<\frac32p,     \tag{6.3}
$$


   so $\log(1+|c_p|)=O(M)$ by (4.3).
2. Every remaining rational is built from a bounded number of factorial
   ratios, or from $O(M)$ products and sums of rational linear factors.
   Their numerator and denominator logarithmic heights are
   $O(M\log M)$.
3. Addition and multiplication of the bounded collection in (2.4)
   preserve the $O(M\log M)$ bound.

This proves (1.7).  Since (4.1) has $O(M)$ rows, summing gives (1.8).
Taking a gcd can of course make the carrier dramatically smaller, but no
all-row or average theorem quantifies that cancellation.

The direct height ledger therefore stops at



$$
\sum_{(r,s)\in\mathcal R_M}
 \log\operatorname {rad}(\mathfrak G_{r,s})
 \le O(M^2\log M),                                  \tag{6.4}
$$



whereas Route 1 requires $o(M)$.  This is not a proof that a sublinear
carrier theorem is impossible.  It proves that primitive clearing plus
individual height supplies no such theorem; the missing input is exactly
the average-gcd estimate (4.7).

## 7. What Item 331 does and does not add after coupling

The fixed-$m$ concentration theorem from Item 331 is no longer a free
obstruction or a source of mass.  After the true affine target is restored,
its coefficient appears only in



$$
\Phi_{r,s}=c_p+\epsilon h_mP_{r+2}(m), \tag{7.1}
$$



and (3.3) identifies this combination with the old integer period $A_s$
modulo the tied prime.  Therefore:

- factorization of $c_p$ alone does not factor $T_\nu$;
- the positive fixed-value fibres of $c_p$ do not imply collisions;
- the determinant gate and $T_\nu$ cannot be counted separately; and
- the only admissible arithmetic target is the coupled carrier (2.7), or
  its chartwise versions.

This is a new target-retaining conclusion, not a repetition of Item 331's
coefficient-only no-go.

## 8. Deterministic replay

The companion certificate verifies:

- twelve exact rational identities on three generic connection planes;
- the fixed-$M$ maps and interval (4.2)-(4.3);
- (2.3), (2.5), and (5.1)-(5.3) on 334 actual rows;
- unit denominators and primitive-numerator carrier equivalence on every
  replayed row;
- all five chart rules whenever their hypotheses occur; and
- the three old determinant hits $(271,113,7)$, $(367,65,39)$, and
  $(383,109,27)$, each rejected by the coupled target.

The full census through $p\le199$, plus those three declared old hits,
contains 333 $\ell$-chart rows, one $\mu$-chart row, no actual
collision, and primitive gcd carriers of at most three bits.  These are
**EXACT FINITE REPLAY ONLY** facts.  In particular, the small observed
gcds are not promoted to (4.7).

## 9. Strict labels

### PROVED

- the target-retaining Cartier representative (2.2)-(2.3);
- the two fully coupled coordinate congruences (2.4)-(2.6);
- the primitive row carrier and exact equivalence (2.7)-(2.8);
- the fixed-$M$ parameter map and prime interval;
- the two exterior targets, syzygy, and complete chart stratification;
- all-row primitive numerator clearing and safe uniform clearing; and
- the $O(M\log M)$ pointwise and $O(M^2\log M)$ aggregate height
  bounds.

### EXACT FINITE REPLAY ONLY

- every bounded count, chart census, gcd size, and digest in Section 8.

### OPEN / NOT CLAIMED

- the target-retaining average-gcd theorem (4.7);
- sublinear logarithmic height for the fixed-$M$ aggregate carrier;
- weighted zero density for the original collisions;
- any new booking or reduction of the $1/105$ ceiling; and
- any Route-1 completion or no-go conclusion from this branch alone.
