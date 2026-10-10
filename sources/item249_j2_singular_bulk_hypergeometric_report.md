> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 249 — Hypergeometric reduction of the singular $j=2$ bulk family

Checked: 2026-08-31 (Beijing time)

## 1. Scope and verdict

Item 247 isolated the singular locus of its symbolic elimination.  In
the Item 244 fixed $j=2$ parameterization, it is



$$
r_{(j=2)}=1,\qquad p=6s+5\text{ prime},\qquad s\ge2.              \tag{1.1}
$$



This $r$ is unrelated to the parameter with the same letter in the
separate $j=1$ branch.  The inherited Item 244 lower index is exactly



$$
L=\left\lceil\frac r2\right\rceil=1.                            \tag{1.2}
$$



Put



$$
M=2s+1=\frac{p-2}{3},\qquad
 n=2s-1=M-2=\frac{p-8}{3}.                         \tag{1.3}
$$



The nonempty coordinate is



$$
D_1(t)=(1-t)(1+t)^n(3+t)
       =(3-2t-t^2)(1+t)^n.                           \tag{1.4}
$$



> **PROVED — closed exact rational expression.**  Define
> 

$$
> d_v=3\binom{n}{v}-2\binom{n}{v-1}-\binom{n}{v-2},
> \qquad
> h_v=\sum_{k=0}^{v-1}\frac{(-1)^k}{2k+3},           \tag{1.5}
>
$$


> with out-of-range binomial coefficients zero and $h_0=0$.  Then
> 

$$
> \boxed{
> \mathsf B_1=\mathcal B_{L=1}[D_1]
> =\sum_{v=1}^{M}
> \frac{(-1)^{v-1}d_vh_v}{2v+3}.}                   \tag{1.6}
>
$$


> This is an equality over $\mathbb Q$, before reduction modulo
> $p$.

> **PROVED — exact coefficient recurrence.**  The coefficients in
> (1.5) satisfy
> 

$$
> \boxed{
> 3(v+1)d_{v+1}
> =(3n-v-2)d_v+(3v-2n-7)d_{v-1}
> +(v-n-4)d_{v-2},}                                  \tag{1.7}
>
$$


> with $d_{-2}=d_{-1}=0$, $d_0=3$.  Thus (1.5)--(1.7) give an
> exact linear-time rational recurrence for every singular row.

> **PROVED — fixed algebraic-hypergeometric reduction.**  Let
> 

$$
> \mathscr D(t)=(1-t)(3+t)(1+t)^{-8/3}
> =\sum_{v\ge0}c_vt^v.                               \tag{1.8}
>
$$


> Define the universal rational sequence
> 

$$
> \Theta_m=\sum_{v=1}^{m}
> \frac{(-1)^{v-1}c_vh_v}{2v+3}.                    \tag{1.9}
>
$$


> Then, for every admissible prime in (1.1),
> 

$$
> \boxed{
> \mathsf B_1\equiv\Theta_{(p-2)/3}\pmod p.}        \tag{1.10}
>
$$


> All row dependence has moved to the terminal index and the moving
> modulus; the coefficient recurrence itself is independent of $p$.

> **PROVED — exact moving-prime criterion.**  Every denominator in
> (1.8)--(1.10) is a $p$-unit, and hence
> 

$$
> \boxed{
> \mathsf B_1=0\pmod p
> \iff
> p\mid\operatorname{num}\!\left(\Theta_{(p-2)/3}\right).}       \tag{1.11}
>
$$



> **SCOPED OBSTRUCTION.**  The universal recurrence permits genuine
> moving-prime cancellation: at the excluded boundary $s=1,p=11$,
> 

$$
> \mathsf B_1=\frac{88}{945}
> \equiv\Theta_3=-\frac{49676}{25515}
> \equiv0\pmod {11}.                                 \tag{1.12}
>
$$


> Thus a theorem for every prime $p\equiv5\pmod6$ is false; the
> admissibility condition $s\ge2$ is essential.  No cancellation is
> found on admissible rows through $p\le20000$, but an all-prime
> nonvanishing proof or admissible counterexample remains open.

> **GLOBAL INTERFACE / BOOKING.**  This scalar occurs only in the
> stronger Item 239 $p^3$ carry.  Item 249 does not strengthen the
> ordinary $p^2$ common-log gate and books no rate or capacity.

## 2. The exact coefficient sum

Expanding (1.4) immediately gives (1.5).  The Item 246 triangular
formula at $L=1$ is



$$
\mathcal B_1[D_1]
 =\sum_{0\le k<v\le M}
 \frac{(-1)^{v-k-1}d_v}{(2k+3)(2v+3)}.              \tag{2.1}
$$



For fixed $v$,



$$
\sum_{k=0}^{v-1}\frac{(-1)^{v-k-1}}{2k+3}
 =(-1)^{v-1}h_v.                                    \tag{2.2}
$$



Substitution of (2.2) into (2.1) proves (1.6).  Thus the closed
expression is not inferred from a bounded scan.

## 3. The exact row recurrence

The logarithmic derivative of (1.4) gives



$$
(3+t-3t^2-t^3)D_1'
 =[3n-2-(2n+4)t-(n+2)t^2]D_1.                       \tag{3.1}
$$



Equating the coefficient of $t^v$ proves (1.7).  Together with



$$
h_{v+1}=h_v+\frac{(-1)^v}{2v+3},\qquad h_0=0,       \tag{3.2}
$$



and the running sum in (1.6), this is a finite first-order state in
$(d_v,d_{v-1},d_{v-2},h_v,\Theta_v)$.

## 4. The universal hypergeometric sequence

Write



$$
a_v=\binom{-8/3}{v}
 =(-1)^v\frac{(8/3)_v}{v!}.                         \tag{4.1}
$$



Then



$$
c_v=3a_v-2a_{v-1}-a_{v-2},\qquad
 3(v+1)a_{v+1}=-(3v+8)a_v.                          \tag{4.2}
$$



Equivalently, the fixed coefficients obey



$$
\boxed{
9(v+1)c_{v+1}
=-3(v+10)c_v+(9v-5)c_{v-1}+(3v-4)c_{v-2},}          \tag{4.3}
$$



with negative-index coefficients zero and $c_0=3$.  Equations
(3.2), (4.2), and



$$
\Theta_0=0,\qquad
 \Theta_v=\Theta_{v-1}
 +\frac{(-1)^{v-1}c_vh_v}{2v+3}\quad(v\ge1)         \tag{4.4}
$$



are the promised $p$-independent recurrence.

To prove (1.10), note that $n=(p-8)/3\equiv-8/3\pmod p$.  For
$0\le v\le M<p$, the map $x\mapsto\binom{x}{v}$ is a polynomial
over $\mathbb F_p$, because $v!$ is a unit.  Therefore



$$
\binom{n}{v}\equiv\binom{-8/3}{v}\pmod p,         \tag{4.5}
$$



and (1.5), (4.2) give $d_v\equiv c_v\pmod p$ term by term.  Applying
(1.6) proves (1.10).

## 5. Unit and endpoint audit

For $s\ge2$, $M=2s+1\ge5$, and



$$
M<p,\qquad 2M+3<p=3M+2.                            \tag{5.1}
$$



The denominators of $a_v$ divide $3^vv!$, hence are $p$-units
for $v\le M$.  Every denominator inside $h_v$ is at most
$2M+1$, and the largest outer denominator in (1.9) is $2M+3$.
This proves the complete unit assertion and (1.11).

The two terminal coefficients also provide a useful independent check.
Since $D_1$ has degree $M=n+2$, its leading terms give



$$
d_M=-1,\qquad d_{M-1}=-M.                           \tag{5.2}
$$



Thus (4.5) implies $c_M=-1$ and $c_{M-1}=-M\pmod p$.  The checker
verifies these endpoint values on every finite row.

## 6. What remains of nonvanishing

Equation (1.11) is now a single universal moving-index numerator
problem:



$$
p=3M+2\text{ prime},\quad M\ge5\text{ odd},\qquad
 p\nmid\operatorname{num}(\Theta_M) ?              \tag{6.1}
$$



The boundary value (1.12) is exact: $11\mid88$, $11\nmid945$,
$11\mid49676$, and $11\nmid25515$.  It shows that neither the
algebraic-series recurrence nor its terminal relation is, by itself, a
unit invariant for every moving prime.  It does not disprove (6.1),
because $M=3$ corresponds to the forbidden value $s=1$.

No fixed-prime scan can prove (6.1), and no factorization, interlacing,
or finite-state invariant excluding its numerator divisibility has
been obtained.  This is an OPEN arithmetic condition, not a declared
impossibility.

## 7. Exact witnesses and finite evidence

The first two admissible values are



$$
\Theta_5\equiv9\pmod {17},\qquad
 \Theta_7\equiv3\pmod {23}.                         \tag{7.1}
$$



Three independent finite layers are recorded:



$$
\begin{array}{c|r|r}
\text{replay}&\text{rows}&\text{zeros}\\ \hline
\text{direct actual polynomial, }p\le401&38&0\\
\text{exact rational comparison, }p\le101&11&0\\
\text{universal recurrence, }p\le20000&1134&0.
\end{array}                                           \tag{7.2}
$$



The last line is an independent recurrence scan, not an extrapolation
or an all-prime theorem.

## 8. Replay, status, and booking

The standard-library checker
`item249_j2_singular_bulk_hypergeometric_certificate.py`:

1. reconstructs the exact integer coefficients and proves the
   coefficient recurrence by direct identity replay;
2. checks the exact character-prefix sum against the Item 246
   triangular functional;
3. verifies the fixed algebraic-series recurrence and termwise
   finite-field reduction;
4. audits every denominator and the two terminal coefficients;
5. verifies the excluded boundary zero and admissible witnesses; and
6. produces separately labelled direct, rational, and extended finite
   scans.

From the archive root, run:

    python scripts/item249_j2_singular_bulk_hypergeometric_certificate.py --output results/item249_j2_singular_bulk_hypergeometric_certificate.json
    python scripts/item249_j2_singular_bulk_hypergeometric_certificate.py --output results/item249_j2_singular_bulk_hypergeometric_certificate_replay.json

Canonical and replay outputs are byte-identical and contain no host path,
timestamp, random seed, or elapsed time.

### Status ledger

**PROVED**

- the inherited value $L=1$, exact coefficient formula, and exact
  character-prefix sum;
- the exact row-coefficient ODE recurrence;
- the fixed algebraic-hypergeometric sequence and universal recurrence;
- the termwise finite-field reduction and complete denominator audit;
- the terminal coefficients and moving-prime numerator criterion; and
- the exact excluded-boundary zero (1.12).

**EXACT FINITE ONLY**

- the 38-row direct replay through $p\le401$;
- the 11-row rational replay through $p\le101$; and
- the 1,134-row universal recurrence scan through $p\le20000$.

**OPEN**

- prove (6.1) for every admissible prime, or find an admissible exact
  counterexample;
- factor or control the moving-prime numerator of $\Theta_M$; and
- obtain any Route-1 rate or capacity improvement.

The booking is



$$
\boxed{
\text{new unconditional log rate}=0,\qquad
\text{new divisibility exponent}=0,\qquad
\text{capacity reduction}=0.}                        \tag{8.1}
$$



Item 249 proves no statement about the arithmetic nature of $e+\pi$.
