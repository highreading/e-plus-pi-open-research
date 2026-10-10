> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 295 — the sharp nearest window and the Turán defect in beta descent

Checked: 2026-08-31 (Beijing time)

## 1. Verdict

Let



$$
q_0=q_1=1,\qquad
q_n=(4n-2)q_{n-1}+q_{n-2}\quad(n\ge2),                 \tag{1.1}
$$



so, in the classical Bessel normalization,



$$
q_n=(-1)^ny_n(-2)=|y_n(-2)|.                           \tag{1.2}
$$



For $n\ge2$, put



$$
a=q_{n-1},\qquad b=q_n,\qquad c=q_{n-2},\qquad
A=4n-2.                                                \tag{1.3}
$$



Then



$$
b=Aa+c.                                                \tag{1.4}
$$



Let



$$
r_n=a^2-\kappa_nb,\qquad
-\frac b2<r_n<\frac b2,\qquad
\rho_n=|r_n|,                                          \tag{1.5}
$$



where $\kappa_n$ is the nearest integer to $a^2/b$.

The conjectural half-bound is



$$
\rho_n\ge\frac a2.                                     \tag{1.6}
$$



The exact nearest-integer criterion needs a sharp window.  If



$$
H_n=\operatorname{nint}\!\left(\frac{ac}{b}\right),    \tag{1.7}
$$



then



$$
\boxed{
\rho_n<\frac a2
\iff
\begin{cases}
H_n\equiv a\pmod A,\\
\displaystyle
\left|H_n-\frac{ac}{b}\right|
<
\frac{Aa}{2b}
=\frac12-\frac{c}{2b}.
\end{cases}}                                           \tag{1.8}
$$



The bare congruence is only a relaxation.  Its exact threshold is



$$
\boxed{
H_n\equiv a\pmod A
\iff
\rho_n<
\frac{b}{2A}
=\frac a2+\frac{c}{2A}.}                               \tag{1.9}
$$



Thus deleting the second line of (1.8) widens the allowed lift window
by $c/A$.  It is not an equivalent reformulation of half-bound
failure.

The natural one-step minimal-counterexample descent can also be
written exactly.  Put



$$
B=A-4,\qquad d=q_{n-3},\qquad a=Bc+d                  \tag{1.10}
$$



for $n\ge3$, and define



$$
h=a-A\kappa_n,\qquad K=\kappa_n-Bh.                   \tag{1.11}
$$



Then



$$
\boxed{
r_n=ah-c\kappa_n=dh-cK.}                               \tag{1.12}
$$



The determinant is preserved, but the transformed point misses the
previous square-residue affine slice from (n=4) onward:



$$
\boxed{
K+Bh=\kappa_n,\qquad (K+Bh)-c=-t_n.}                    \tag{1.13}
$$



The exact defect is



$$
t_n:=c-\kappa_n.                                       \tag{1.14}
$$



It is itself a seed-specific Turán quotient.  With



$$
T_n:=bc-a^2,                                           \tag{1.15}
$$



one has



$$
\boxed{
t_n=
\operatorname{nint}\!\left(\frac{T_n}{b}\right),\qquad
T_n+T_{n-1}=4ac.}                                      \tag{1.16}
$$



Projecting to the previous affine slice replaces $K$ by $K+t_n$
and gives



$$
\boxed{
c^2-ah=ct_n-r_n.}                                      \tag{1.17}
$$



After centering modulo $a$, the right side is exactly the previous
beta residue:



$$
\boxed{
\operatorname{cent}_a(ct_n-r_n)=r_{n-1}.}              \tag{1.18}
$$



Consequently a minimal-counterexample argument gives only the already
known inequality



$$
\left|\operatorname{cent}_a(ct_n-r_n)\right|
=\rho_{n-1}\ge\frac c2.                                \tag{1.19}
$$



It does not bound $|r_n|$: the projection has introduced the moving
term $ct_n$.

This is a sharply scoped obstruction to the natural one-dimensional
descent.  It is not an impossibility theorem for a coupled descent
which controls $t_n$, $T_n$, or further Bessel data.

No proof of (1.6) and no exact counterexample is obtained.  Proper
de-overlapped targets and the Item-282 product baseline remain
separate.  Booking is zero.

## 2. Nearest integers are unique

All $q_j$ are odd, and adjacent terms are coprime.  Hence



$$
\gcd(a,b)=1,\qquad b\text{ is odd}.                    \tag{2.1}
$$



The ratio $a^2/b$ cannot be a half-integer: if



$$
2a^2=(2m+1)b,
$$



then $b\mid a^2$, contradicting (2.1).  Thus
$\kappa_n$ in (1.5) is unique.

The ratio $ac/b$ also cannot be a half-integer.  Indeed,



$$
2ac=(2m+1)b
$$



would imply $b\mid ac$.  Since $\gcd(a,b)=1$, this would force
$b\mid c$, impossible because $0<c<b$.  Therefore $H_n$ in
(1.7) is unique, and



$$
\left|H_n-\frac{ac}{b}\right|<\frac12.                 \tag{2.2}
$$



No tie convention is hidden in (1.8) or (1.9).

## 3. Proof of the sharp-window equivalence

Starting from the centered quotient $\kappa_n$, set



$$
h=a-A\kappa_n.                                         \tag{3.1}
$$



Using $b=Aa+c$,



$$
\begin{aligned}
b(a-A\kappa_n)-ac
&=ab-Ab\kappa_n-ac\\
&=A(a^2-\kappa_nb),
\end{aligned}
$$



so



$$
\boxed{
A r_n=bh-ac.}                                          \tag{3.2}
$$



Suppose first that $\rho_n<a/2$.  Equation (3.2) gives



$$
\left|h-\frac{ac}{b}\right|
=\frac{A\rho_n}{b}
<
\frac{Aa}{2b}
<\frac12.                                              \tag{3.3}
$$



By uniqueness of the nearest integer,



$$
h=H_n.                                                 \tag{3.4}
$$



Equation (3.1) gives $H_n\equiv a\pmod A$, and (3.3)
is the sharp window in (1.8).

Conversely, suppose $H_n\equiv a\pmod A$ and the sharp window
holds.  Define



$$
\kappa=\frac{a-H_n}{A}\in\mathbb Z,\qquad
r=a^2-\kappa b.                                        \tag{3.5}
$$



The same algebra as in (3.2) gives



$$
A r=bH_n-ac.                                           \tag{3.6}
$$



The sharp window implies



$$
|r|<\frac a2<\frac b2.                                 \tag{3.7}
$$



Thus $r$ is already the centered representative of $a^2\bmod b$.
It equals $r_n$, proving the reverse implication and (1.8).

The strict threshold matters:



$$
\frac{Aa}{2b}
=\frac{b-c}{2b}
=\frac12-\frac{c}{2b}.                                 \tag{3.8}
$$



Nearestness alone supplies only $<1/2$.

## 4. The congruence-only relaxation

If $H_n\equiv a\pmod A$, define $\kappa,r$ by (3.5).
Nearestness (2.2) and (3.6) give



$$
|r|<\frac{b}{2A}<\frac b2.                             \tag{4.1}
$$



Hence $r=r_n$, and



$$
\rho_n<\frac{b}{2A}.                                   \tag{4.2}
$$



Conversely, if $\rho_n<b/(2A)$, equation (3.2) gives



$$
\left|h-\frac{ac}{b}\right|<\frac12.
$$



Therefore $h=H_n$, and (3.1) gives
$H_n\equiv a\pmod A$.  This proves (1.9).

Using $b=Aa+c$,



$$
\frac{b}{2A}
=\frac a2+\frac{c}{2A}.                                \tag{4.3}
$$



The half-bound failure interval ends at $a/2$; the bare congruence
interval ends at $a/2+c/(2A)$.  The missing sharp-window band is
therefore genuine at the level of the exact inequalities, whether or
not an actual beta index ever enters it.

## 5. Exact base cases for a minimal counterexample

The first three allowed rows are



$$
\begin{array}{c|c|c|c|c}
n&a&b&\kappa_n&r_n\\ \hline
2&1&7&0&1\\
3&7&71&1&-22\\
4&71&1001&5&36.
\end{array}                                             \tag{5.1}
$$



Thus



$$
2\rho_n\ge a\qquad(n=2,3,4).                           \tag{5.2}
$$



Any minimal counterexample to (1.6) would have



$$
n\ge5.                                                 \tag{5.3}
$$



These are exact base cases only, not a finite extrapolation.

## 6. Seed-specific Turán arithmetic

For $n\ge3$, put



$$
B=A-4,\qquad d=q_{n-3}.
$$



Then



$$
a=Bc+d,\qquad 0<d<c.                                  \tag{6.1}
$$



The two adjacent ratios satisfy



$$
\frac ba=A+\frac ca>A,
$$



while



$$
\frac ac=B+\frac dc<A-3.
$$



Therefore



$$
\frac ba>\frac ac,
$$



which proves



$$
\boxed{T_n=bc-a^2>0.}                                  \tag{6.2}
$$



Similarly,



$$
T_{n-1}=ad-c^2>0.                                     \tag{6.3}
$$



Direct substitution of $b=Aa+c$ and $a=(A-4)c+d$
gives



$$
\begin{aligned}
T_n+T_{n-1}
&=(bc-a^2)+(ad-c^2)\\
&=a(Ac-a+d)\\
&=4ac,
\end{aligned}                                          \tag{6.4}
$$



proving the Turán recurrence in (1.16).

Since



$$
\frac{T_n}{b}=c-\frac{a^2}{b},                         \tag{6.5}
$$



translation invariance and uniqueness of the nearest integer give



$$
t_n=c-\kappa_n
=\operatorname{nint}\!\left(\frac{T_n}{b}\right).      \tag{6.6}
$$



The elementary bounds



$$
\frac{a}{A+1}<\frac{a^2}{b}<\frac aA                  \tag{6.7}
$$



give the seed-specific interval



$$
\boxed{
\frac{4c-d}{A}
<
\frac{T_n}{b}
<
\frac{5c-d}{A+1}.}                                    \tag{6.8}
$$



For $n\ge4$, this implies



$$
1\le t_n<c.                                           \tag{6.9}
$$



For the lower bound, $(4c-d)/A>3c/A>1/2$;
$6c>A$ at $n=4$ and persists because $c$ increases while
$A$ increases by only $4$.  For the upper bound,
$a^2/b>1/2$, so (6.5) is $<c-1/2$.

Thus a hypothetical minimal counterexample has a nonzero, moving
defect.  The descent cannot silently discard it.

## 7. The natural descent and its exact failure to close

Retain



$$
h=a-A\kappa_n,\qquad K=\kappa_n-Bh.                   \tag{7.1}
$$



Item 290's determinant is



$$
r_n=ah-c\kappa_n.                                     \tag{7.2}
$$



Using $a=Bc+d$,



$$
\begin{aligned}
r_n
&=(Bc+d)h-c\kappa_n\\
&=dh-c(\kappa_n-Bh)\\
&=dh-cK.
\end{aligned}                                          \tag{7.3}
$$



This is the exact unimodular Euclidean descent.  It preserves the
determinant $r_n$.

At level $n-1$, a square-residue candidate with quotient $h$
would have the affine coordinate



$$
K_{\mathrm{sq}}=c-Bh,                                 \tag{7.4}
$$



because



$$
c^2-ha=c(c-Bh)-dh.                                    \tag{7.5}
$$



But the transformed coordinate in (7.1) satisfies



$$
K+Bh=\kappa_n,                                        \tag{7.6}
$$



which equals $c$ at the exceptional base row $n=3$, and differs
from $c$ for every $n\ge4$ by (6.9).  In general,



$$
K_{\mathrm{sq}}-K=c-\kappa_n=t_n.                    \tag{7.7}
$$



Projecting onto the previous square slice gives



$$
\begin{aligned}
c^2-ha
&=c(K+t_n)-dh\\
&=ct_n-(dh-cK)\\
&=ct_n-r_n,
\end{aligned}                                          \tag{7.8}
$$



which is (1.17).

Let



$$
r_{n-1}=\operatorname{cent}_a(c^2).                   \tag{7.9}
$$



Because $c^2-ha\equiv c^2\pmod a$, (7.8) gives



$$
\operatorname{cent}_a(ct_n-r_n)=r_{n-1}.              \tag{7.10}
$$



Now assume $n$ were a minimal counterexample.  Minimality gives



$$
|r_{n-1}|\ge\frac c2.                                  \tag{7.11}
$$



Equations (7.10)–(7.11) say only



$$
\left|\operatorname{cent}_a(ct_n-r_n)\right|
\ge\frac c2.                                           \tag{7.12}
$$



There is no contradiction with $|r_n|<a/2$, because $ct_n$ is a
nonzero moving translation before centering.

> **PROVED SCOPED DESCENT OBSTRUCTION.**
> The determinant-preserving Euclidean step does not map the
> level-$n$ affine square slice to the level-$(n-1)$ affine
> square slice for $n\ge4$.  Its exact defect is $t_n$.
> Correcting the defect
> returns the previous residue only after adding $ct_n$ and
> centering.  Therefore minimality alone does not close this
> one-dimensional descent.

This does not exclude a coupled induction in



$$
(r_n,t_n,T_n)
$$



or a stronger factorial/hypergeometric identity.

## 8. A stronger sufficient target

One possible stronger theorem would be



$$
\boxed{
A(2\rho_n-a)\ge2c.}                                   \tag{8.1}
$$



It implies



$$
\rho_n\ge\frac a2+\frac cA.                            \tag{8.2}
$$



But the bare congruence in (1.9) would imply



$$
\rho_n<
\frac a2+\frac{c}{2A},                                \tag{8.3}
$$



which is incompatible with (8.2).  Thus (8.1) would exclude even the
relaxed nearest-integer congruence and would prove the half-bound.

At the exact base row $n=4$,



$$
A(2\rho_4-a)=14=2c.                                   \tag{8.4}
$$



No all-$n$ proof of (8.1) is supplied here.  Equation (8.1) is an
explicit open induction target, not a conclusion drawn from bounded
data.

## 9. Proper targets, product baseline, and admission

For a proper target



$$
Q\mid
\frac{q_n}{\gcd(q_n,D_m)},\qquad Q>1,                 \tag{9.1}
$$



the least residue is



$$
r_{n,Q}=\operatorname{cent}_Q(r_n),\qquad
\rho_{n,Q}=|r_{n,Q}|
\le\min\!\left\{\rho_n,\frac{Q-1}{2}\right\}.          \tag{9.2}
$$



Thus even a proof of the full-target half-bound would not transfer as
a lower bound to a proper $Q$.  A full-target upper construction
would transfer, exactly as in Item 290.

Item 282's common coefficient/product baseline remains a separate
factor.  The nearest-window and Turán descent address only the
additive full-target least lift.

Item 295 proves no retained-capacity ceiling and no positive mass.
Therefore



$$
\boxed{
\text{new Route-1 rate}=0,\qquad
\text{new beta capacity reduction}=0.}                \tag{9.3}
$$



## 10. Strict labels

### PROVED

* Unique nearest integers for $a^2/b$ and $ac/b$.
* The sharp-window iff (1.8).
* The congruence-only relaxation (1.9).
* The determinant identity and unimodular descent (1.12).
* Positivity, recurrence, and quotient description of $T_n,t_n$.
* The affine defect $t_n=c-\kappa_n$.
* The projection identity (1.17) and centered return (1.18).
* The exact base cases $n=2,3,4$.
* Proper-target asymmetry and separation from the Item-282 baseline.

### PROVED SCOPED DESCENT OBSTRUCTION

* The natural determinant-preserving step misses the previous
  square-residue slice by $t_n$.
* Projecting to that slice introduces $ct_n$; minimality returns
  only the already-known previous centered residue.
* This does not exclude a coupled descent or a new Bessel identity.

### EXACT FINITE ONLY

* The checker replays bounded instances of the universal window,
  Turán, determinant, defect, and projection identities.
* It performs no counterexample search, no larger half-bound scan,
  and no exceptional-prime search.
* Bounded rows are regression checks only.

### OPEN

* The all-$n$ half-bound $\rho_n\ge a/2$.
* The stronger target (8.1).
* Exclusion of the bare nearest-integer congruence.
* A coupled descent controlling $t_n$ or $T_n$.
* An exact counterexample, if the half-bound is false.
* A large proper de-overlapped target residue theorem.
* The Item-282 common product baseline and weighted-return cover.
* Route 1 and every conclusion about $e+\pi$.

### BOOKING



$$
\boxed{
\text{new Route-1 rate}=0,\qquad
\text{new beta capacity reduction}=0.}                \tag{10.1}
$$



## 11. Deterministic replay

From the archive root:

~~~text
python scripts/item295_beta_nearest_window_descent_certificate.py ^
  --output results/item295_beta_nearest_window_descent_certificate_replay.json
~~~

The checker uses only the Python standard library and exact integer
comparisons.  The canonical result and replay must be byte-identical.
