> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 284 — parameter-dependent anisotropic norms for the fixed-$j=1$ gate

Checked: 2026-08-31 (Beijing time)

## 1. Scope, admission audit, and verdict

Retain the actual fixed common-log cell



$$
p=4h+6s+3,\qquad h,s\ge1,\qquad M=3h+4s+2,              \tag{1.1}
$$



and its simultaneous divided collision gate.  At fixed $M$, let



$$
\mathcal S_M=
 \left\{p\text{ prime}:{4M+3\over3}\le p\le{3M-1\over2}\right\},
 \qquad B_M=\prod_{p\in\mathcal S_M}p.                     \tag{1.2}
$$



Item 264 proves



$$
\log B_M={M\over6}+o(M).                                  \tag{1.3}
$$



This item allows one integral norm coefficient $d_M$ to depend on the
known candidate set $\mathcal S_M$, but not on the unknown subset of
collision primes.

> **PROVED — exact admissible CRT construction.**  There is an explicitly
> computable integer
>
> 

$$
> 1\le d_M<B_M                                             \tag{1.4}
>
$$


>
> which is a quadratic nonresidue modulo every
> $p\in\mathcal S_M$.  It is obtained by choosing a local nonresidue at
> every candidate prime and applying CRT.  No collision information is
> used.

> **PROVED — one scalar recognizes the full gate exactly.**  With Item
> 200's normalized integers
> $\overline C_\nu=C_\nu/F_M$, put
>
> 

$$
> \mathcal N_M=\overline C_0(M)^2-d_M\overline C_1(M)^2.   \tag{1.5}
>
$$


>
> Then, for every actual candidate prime,
>
> 

$$
> \boxed{p\mid\mathcal N_M
> \iff p^2\mid C_0(M),C_1(M)
> \iff \text{the full gate collides at }p.}                 \tag{1.6}
>
$$


>
> A collision actually gives $p^2\mid\mathcal N_M$.

> **PROVED — the absolute-height route still fails.**  The direct CRT
> coefficient satisfies $\log d_M\le M/6+o(M)$.  The best inherited
> raw-coordinate divisor-to-height ratio is
>
> 

$$
> {H\over2}+{1\over24}
> =3.20548043938709\ldots,                                  \tag{1.7}
>
$$


>
> and even a hypothetical subexponential $d_M$ only returns Item 264's
> $H/2=3.16381377272042\ldots$.  Both are far above the raw
> $1/6$ log mass per $M$.

> **PROVED — scoped bounded-height norm barrier.**  For any rational or
> integral coefficient family of exponential height
> $\delta M+o(M)$, $\delta\ge0$, an anisotropic quadratic norm,
> estimated only from the two componentwise Cauchy bounds, gives no better
> than $H/2+\delta/4$.  Thus no bounded-height parameter-dependent norm
> can prove a useful weighted bound by divisibility plus absolute size
> alone.

This is not a lower bound for the actual height of a specially cancelling
norm.  A cancellation theorem or a theorem localizing the prime factors
of $\mathcal N_M$ could still be useful.

No such theorem is proved.  Item 149 de-overlap gives



$$
\boxed{\text{new fixed-\(j=1\) capacity reduction}=0,\qquad
        \text{new unconditional Route-1 rate}=0.}           \tag{1.8}
$$



The raw ceiling remains $1/36$ per $6M$.

## 2. Exact simultaneous-nonresidue CRT coefficient

For every $p\in\mathcal S_M$, choose the least positive quadratic
nonresidue $n_p$.  Set



$$
E_p={B_M\over p}
 \left({B_M\over p}\right)^{-1}\pmod p,                   \tag{2.1}
$$



where $E_p$ is viewed as the standard CRT idempotent modulo $B_M$.
Define $d_M$ to be the least positive residue of



$$
d_M\equiv\sum_{p\in\mathcal S_M}n_pE_p\pmod{B_M}.         \tag{2.2}
$$



Then



$$
d_M\equiv n_p\pmod p,\qquad
 \left({d_M\over p}\right)=-1
 \quad(p\in\mathcal S_M).                                 \tag{2.3}
$$



In particular, $d_M\not\equiv0\pmod p$, so (2.2) is nonzero modulo
$B_M$ and has a representative satisfying (1.4).  The input to (2.2)
is the complete prime interval (1.2), which is known from $M$; the
construction never tests whether a gate collides.

If $\mathcal S_M$ is empty, one may set $d_M=2$.  This finite boundary
case has no asymptotic role.

For example, at $M=100$,



$$
\mathcal S_{100}=\{137,139,149\},\qquad
 (n_{137},n_{139},n_{149})=(3,2,2),                         \tag{2.4}
$$



and the checker obtains



$$
B_{100}=2837407,\qquad d_{100}=828442.                     \tag{2.5}
$$



All identities in (2.4)--(2.5) are exact.

## 3. Exact raw and normalized norm bridges

Every $p\in\mathcal S_M$ belongs to Item 200's forced Cartier product,
so



$$
p\mid C_0(M),C_1(M).                                      \tag{3.1}
$$



Write $C_\nu=pu_\nu$.  Since $d_M$ is a nonresidue,



$$
u_0^2-d_Mu_1^2\equiv0\pmod p
 \iff u_0=u_1=0\pmod p.                                   \tag{3.2}
$$



For the raw norm



$$
\mathcal R_M=C_0(M)^2-d_MC_1(M)^2,                        \tag{3.3}
$$



equations (3.1)--(3.2) give the exact valuation dichotomy



$$
\begin{array}{c|c}
\text{row status}&v_p(\mathcal R_M)\\ \hline
\text{not a collision}&2\\
\text{collision}&\ge4.
\end{array}                                                 \tag{3.4}
$$



Thus



$$
\boxed{p^4\mid\mathcal R_M
 \iff \text{the full gate collides at }p.}                 \tag{3.5}
$$



Now write $F_M=p(F_M/p)$.  The factor $F_M/p$ is a $p$-unit, so
the normalized pair $(\overline C_0,\overline C_1)$ is a common unit
multiple of $(u_0,u_1)$ modulo $p$.  This proves (1.6) and the square
valuation following it.

If $R_M^{(1)}$ is the full collision radical, then



$$
(R_M^{(1)})^4\mid\mathcal R_M,\qquad
 (R_M^{(1)})^2\mid\mathcal N_M.                            \tag{3.6}
$$



Moreover, whenever the specialized pair is not zero as an integer pair,



$$
R_M^{(1)}=\gcd(\operatorname{rad}|\mathcal N_M|,B_M).      \tag{3.7}
$$



The norm itself is then nonzero.  Indeed, $d_M$ cannot be a perfect
square integer because it is a nonresidue modulo every candidate prime;
an identity $C_0^2=d_MC_1^2$ with a nonzero pair would make $d_M$ a
rational square.  If both coordinates vanish as integers, the height
argument is degenerate and the raw support bound is retained.

## 4. Least simultaneous nonresidue: what is proved and open

Define



$$
\lambda_M=\min\left\{d\ge1:
 \left({d\over p}\right)=-1\text{ for every }p\in\mathcal S_M\right\}.
                                                                    \tag{4.1}
$$



The CRT construction proves the unconditional bound



$$
\lambda_M<B_M,qquad
 \log\lambda_M\le{M\over6}+o(M).                           \tag{4.2}
$$



No theorem here proves



$$
\log\lambda_M=o(M),                                      \tag{4.3}
$$



or any sharper uniform estimate.  Standard one-character least
quadratic-nonresidue bounds do not directly solve (4.3), because (4.1)
prescribes the negative character value simultaneously for
$\asymp M/\log M$ different prime moduli.

The checker determines $\lambda_M$ exactly for $9\le M\le300$.  The
largest value in that bounded replay is $881$, at $M=259$ with eight
candidate primes.  This statement is **EXACT FINITE ONLY** and supports
no asymptotic inference.

Crucially, even a proof of (4.3) would not make the absolute-height method
pass: Section 7 shows that the limiting certified ratio would still be
$H/2$.

## 5. Bounded-complexity rational row rules

Suppose a proposed rule gives a rational coefficient



$$
d_{p,M}={a(h,s,M)\over b(h,s,M)}\pmod p                    \tag{5.1}
$$



on the actual row.  It is usable only after proving



$$
p\nmid b(h,s,M),\qquad
 \left({a(h,s,M)b(h,s,M)^{-1}\over p}\right)=-1           \tag{5.2}
$$



on every row in scope.  A denominator-zero row is not silently removed;
without a separate weighted theorem it retains raw capacity.

There are two natural ways to aggregate (5.1).

1. **Separate local norms.**  Divisibility of one row-specific integer at
   each different prime does not combine into a single absolute-height
   bound.  Multiplying all $\asymp M/\log M$ norms loses exactness: a
   noncollision prime can divide one of the other split norms.  Even if
   the product is used only as a necessary divisor, both its inherited
   height and its collision valuation are multiplied by the number of
   factors, so their ratio remains the same $H/2$ or
   $H-\kappa$ barrier rather than improving it.
2. **One CRT norm.**  Interpolate the residues (5.1) to one coefficient
   modulo $B_M$.  This returns exactly to Sections 2--4, with an
   integral representative of height at most $B_M$.

Thus a row-dependent rational rule needs more than pointwise
nonresiduosity.  It needs either a common low-height interpolation plus a
new factor-distribution theorem, or a different global invariant.

This item proves no universal nonexistence theorem for bounded-complexity
rational functions.  It closes only the divisibility-plus-componentwise-
height route after such a function or its CRT interpolation has been
supplied.

## 6. Exact false positives for simple parameter rules

The following table uses



$$
U_\nu=C_\nu(M)/p\pmod p.                                  \tag{6.1}
$$



Every displayed row is actual, $(U_0,U_1)\ne(0,0)$, and
$U_0^2-dU_1^2=0\pmod p$:



$$
\begin{array}{c|c|c|c}
\text{rule for }d&(p,h,s,M)&(U_0,U_1)&d\pmod p\\ \hline
h&(13,1,1,9)&(2,11)&1\\
s&(13,1,1,9)&(2,11)&1\\
h+s&(139,7,18,95)&(107,62)&25\\
2h+3s&(31,1,4,21)&(13,1)&14\\
M&(71,8,6,50)&(46,30)&50\\
M-1&(283,34,24,200)&(154,100)&199\\
M+1&(443,74,24,320)&(195,44)&321.
\end{array}                                                 \tag{6.2}
$$



Hence none of these natural low-height rules is anisotropic on every
actual row, and each has an actual arithmetic false positive.  These are
declared witnesses, not evidence for a universal rational-function
no-go.

## 7. Exact divisor-to-height ledger

Let



$$
H=6.327627545440858\ldots                                  \tag{7.1}
$$



be Item 264's componentwise Cauchy constant, and write



$$
\log\max(1,|d_M|)=\delta M+o(M),\qquad\delta\ge0.          \tag{7.2}
$$



The raw norm satisfies



$$
\log|\mathcal R_M|\le(2H+\delta)M+o(M).                   \tag{7.3}
$$



Combining (7.3) with the fourth-power divisor in (3.6) gives



$$
{\log R_M^{(1)}\over M}
 \le{H\over2}+{\delta\over4}+o(1).                         \tag{7.4}
$$



This is the strongest inherited-height ratio in the norm class.  For the
direct CRT construction, $\delta\le1/6$, so (7.4) becomes (1.7).  If
$d_M$ has subexponential, polynomial, or bounded height, then
$\delta=0$ and (7.4) is exactly Item 264's $H/2$ barrier.

For comparison, Item 281 gives



$$
H-\kappa=3.99058003744209\ldots,                           \tag{7.5}
$$



for one normalized component.  The normalized norm has height at most



$$
\{2(H-\kappa)+\delta\}M+o(M)                              \tag{7.6}
$$



and only the square divisor in (3.6), hence ratio



$$
H-\kappa+{\delta\over2}.                                  \tag{7.7}
$$



At the direct CRT value $\delta=1/6$, this is
$4.07391337077542\ldots$, worse than (1.7).

The same ledger covers a rational coefficient $a_M/b_M$: after
clearing, use $b_MC_0^2-a_MC_1^2$ and put the exponential height of
$(a_M,b_M)$ into $\delta$.  Denominators cannot create a negative
height contribution.

Since the raw support is only $1/6$ per $M$, neither (7.4) nor (7.7)
passes admission.  This is an upper-bound-method obstruction, not a
matching lower bound on the actual norm height.

## 8. De-overlap and the missing theorem

The scalar (1.5) is forced by the actual two-coordinate gate and is exact
on every candidate prime.  It therefore passes the logical
actual-family test.  It fails the remaining tests:

1. **Item 149 de-overlap.**  Squaring the two already known gate
   coordinates and forming their norm does not create an independent
   post-Cartier valuation copy.  The powers in (3.6) are algebraic powers
   of the same collision ideal already audited in Items 264 and 281.
2. **Height.**  Even the best possible subexponential coefficient leaves
   the inherited ratio at $H/2>1/6$.
3. **Density.**  No theorem proves that the prime divisors of
   $\mathcal N_M$ lying in (1.2) have log weight $cM+o(M)$ with
   $c<1/6$.  By (1.6), that statement is exactly the original weighted
   collision problem in scalar form.

A useful continuation would need a separately proved cancellation bound
for $\mathcal R_M$ or $\mathcal N_M$, or an arithmetic theorem on
their prime factors in the moving interval.  Neither follows from CRT or
least-nonresidue existence.

Therefore the isolated-prime mass remains open and the booking is zero.

## 9. Replay and proof labels

The standard-library checker verifies:

* the exact CRT coefficient, nonresidue symbols, forced divisibility, and
  both norm equivalences on 708 actual candidate rows through
  $M\le220$;
* the exact example (2.4)--(2.5);
* every least simultaneous nonresidue through $M\le300$;
* all seven actual parameter-rule false positives in (6.2);
* the displayed height constants and comparisons.

The bounded CRT and least-coefficient replays are **EXACT FINITE ONLY**.
No asymptotic inference about $\lambda_M$, collisions, or density is
made from them.

### PROVED

* The all-candidate-prime CRT nonresidue construction without collision
  presupposition.
* The exact raw fourth-power and normalized scalar gate equivalences.
* The coefficient bound $d_M<B_M$ and its $M/6+o(M)$ height.
* The bounded-height norm divisor-to-height barrier.
* The aggregation dichotomy for row-dependent rational rules.
* The seven exact actual false positives for simple rules.
* Item 149 de-overlap, unchanged $1/36$ ceiling, and zero booking.

### EXACT FINITE ONLY

* The bounded CRT, least-simultaneous-nonresidue, and witness replays.

### OPEN

* A subexponential theorem for $\lambda_M$.
* A bounded-complexity rational rule satisfying the nonresidue and unit
  conditions on every actual row.
* Exponential cancellation in the exact norm or a useful prime-factor
  localization theorem.
* Any $c<1/6$ weighted collision bound, positive fixed-$j=1$ capacity
  reduction, or new Route-1 rate.
