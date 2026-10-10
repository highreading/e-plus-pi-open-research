> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 226 — Four-phase Cartier closure in the fixed $j=2$ cell

Checked: 2026-08-31 (Beijing time)

## 1. Scope and verdict

Retain the Item 219--225 cell



$$
4m+1=5p-2s,\qquad 1\le s\le\frac{p-3}{6},\qquad
 s\equiv\frac{p-1}{2}\pmod2,\qquad p\ge11,              \tag{1.1}
$$



and, for $s\ge2$,



$$
r=\frac{p-6s-3}{2},\qquad
 f_0=z^r(1-z)^r(1+z)(1+z^2)^{2s}.                     \tag{1.2}
$$



This item attacks the all-prime simultaneous-zero problem left by
Item 225.  Its main result is structural rather than a larger scan.

> **PROVED — exact phase transfer and $4p$-closure.**  Put
> 

$$
> k_q=(q-1)p+2s-3,\qquad
> Y_q=(\widehat T_{k_q},\widehat T_{k_q+1},
>                \widehat T_{k_q+2},\widehat T_{k_q+3})^t.            \tag{1.3}
>
$$


> There are an exact matrix $M=M_{p,s}$, column $b=b_{p,s}$, and
> terminal row $a=a_{p,s}$ such that
> 

$$
> Y_{q+1}=MY_q+b\,w_q,\qquad
> aY_q=(-1)^r w_q,\qquad w_q=W_{\mathcal L}(qp).       \tag{1.4}
>
$$


> The integer weights have period four:
> 

$$
>                     (w_1,w_2,w_3,w_4)=(7,29,11,-11).               \tag{1.5}
>
$$


> Coefficientwise,
> 

$$
>                         \widehat T_{k+4p}=\widehat T_k,              \tag{1.6}
>
$$


> and therefore
> 

$$
> (I-M^4)Y_1=M^3bw_1+M^2bw_2+Mbw_3+bw_4.             \tag{1.7}
>
$$



> **PROVED — exact affine solvability criterion.**  Let $v$ be the
> Item 224 common-line state at the first terminal, so a collision has
> $Y_1=\lambda v$.  Combine Item 224's bottom equation, all four
> terminal equations in (1.4), and all four coordinates of (1.7).
> They form nine equations
> 

$$
>                         c_i\lambda=d_i\qquad(1\le i\le9).            \tag{1.8}
>
$$


> The formal multi-phase system is solvable exactly when
> 

$$
> \operatorname{rank}[c\mid d]=\operatorname{rank}c=1,               \tag{1.9}
>
$$


> equivalently, at least one $c_i$ is nonzero and all 36 augmented
> $2\times2$ minors
> 

$$
>                         c_i d_j-c_jd_i                              \tag{1.10}
>
$$


> vanish.  Every actual common-log collision with $s\ge2$ must pass
> this criterion.  Item 224's $\Omega$ and Item 225's $\Psi$ are,
> up to harmless signs, the first two terminal minors of (1.10).

> **PROVED — regular fixed-point completeness.**  Define
> 

$$
>                         \Delta_{p,s}=\det(I-M^4).                    \tag{1.11}
>
$$


> If $\Delta_{p,s}\ne0$, then closure solvability with
> $Y_1=\lambda v$ is equivalent to the original $j=2$ common-log
> collision.  Thus on every regular row, (1.7) is not merely another
> necessary condition: it exactly recovers the original gate.

> **EXACT FINITE ONLY.**  Through $p\le401$, the nine-equation system
> is inconsistent on all 1,115 admissible $s\ge2$ rows.  Of these,
> 1,100 have $\Delta\ne0$.  The remaining 15 rows with $\Delta=0$
> are listed in Section 8 and are also formally inconsistent.  This is
> a finite classification, not an all-prime theorem.

> **OPEN / METHOD BARRIER.**  No all-prime augmented-minor
> nonvanishing theorem or density bound is proved.  Each of the six
> closure-only minors has explicit zeros in the finite census, so no
> one of those minors is a uniform unit.  The determinant-zero rows do
> not yet have an all-prime factorization or zero-rate bound.  Item 226
> therefore books no capacity reduction and proves nothing about
> $e+\pi$.

## 2. Regularized periods and the $q p$ multiplicity audit

Write $f_0=\sum_nc_nz^n$, and retain Item 225's finite part



$$
\widehat F_k(x)=
 \sum_{\substack{n\\p\nmid n+k+1}}
 \frac{c_nx^{n+k+1}}{n+k+1},\qquad
 \widehat T_k=\mathcal L(\widehat F_k).                \tag{2.1}
$$



For



$$
K_k=z^{k+1}(1-z^4)f_0
$$



and Item 224's five coefficients $A_j(k)$, Item 225 proved



$$
\sum_{j=0}^4A_j(k)\widehat T_{k+j}
 =-\sum_{a\ge1}[z^{ap}]K_k\,W_{\mathcal L}(ap).        \tag{2.2}
$$



At the $q$-th terminal $k=k_q$, the last recurrence coefficient is
exactly



$$
\begin{aligned}
 A_4(k_q)
 &=-\bigl(k_q+2r+4s+6\bigr)\\
 &=-q p.                                               \tag{2.3}
\end{aligned}
$$



The leading resonant primitive term is



$$
\frac{(-1)^r z^{qp}}{qp}.                \tag{2.4}
$$



Thus the product of (2.3) and (2.4) cancels $q$ exactly.  The
terminal right-hand side is



$$
(-1)^rW_{\mathcal L}(qp),     \tag{2.5}
$$



with neither a missing factor $q$ nor an extra division by $q$.
This audit is performed before reduction modulo $p$.

For $k=k_q+t$, $1\le t\le p-1$,



$$
A_4(k)=-(q p+t)\equiv-t\not\equiv0\pmod p.           \tag{2.6}
$$



Hence every intervening propagation pivot is a unit.

## 3. The phase weights

In endpoint coordinates



$$
E=F(1),\qquad C=\frac{F(i)+F(-i)}2,\qquad
 S=\frac{F(i)-F(-i)}{2i},
$$



the functional is



$$
\mathcal L=(9,-20,-2\chi),
 \qquad \chi=(-1)^{(p-1)/2}.                           \tag{3.1}
$$



Its monomial weight has period four:



$$
\begin{array}{c|rrrr}
n\bmod4&0&1&2&3\\ \hline
W_{\mathcal L}(n)&-11&9-2\chi&29&9+2\chi .
\end{array}                                            \tag{3.2}
$$



If $p\equiv1\pmod4$, substitute $\chi=1$; if
$p\equiv3\pmod4$, substitute $\chi=-1$ and reverse the odd
residues.  Both cases give the phase-independent integer cycle



$$
W_{\mathcal L}(p)=7,\quad
 W_{\mathcal L}(2p)=29,\quad
 W_{\mathcal L}(3p)=11,\quad
 W_{\mathcal L}(4p)=-11.                              \tag{3.3}
$$



The value $29$ may vanish when $p=29$; no unit assumption on an
individual phase weight is used.

## 4. Construction of the one-phase transfer

Set $k_1=2s-3$ and



$$
h=(1-z^4)f_0.                \tag{4.1}
$$



At relative offset $t$, $1\le t\le p-1$, the only Cartier source in
the interval from phase $q$ to phase $q+1$ is



$$
-w_q\,[z^{\,p-2s+2-t}]h.                             \tag{4.2}
$$



The recurrence coefficients modulo $p$ depend only on $t$, not on
$q$.  Propagating the four input coordinates of $Y_q$ and the
normalized source (4.2) therefore defines a fixed matrix and column



$$
Y_{q+1}=MY_q+bw_q.            \tag{4.3}
$$



The value $\widehat T_{k_q+4}$, which is free at the terminal, gives a
sixth propagation column.  Item 225 proved that this homogeneous
response has generating polynomial



$$
g=(1-z)^r(1+z)(1+z^2)^{2s},
$$



of degree strictly below $p-4$.  The four output positions correspond
to coefficients $p-4,p-3,p-2,p-1$, so this entire free column is
identically zero.  This proves that (4.3) loses no hidden resonant
parameter.

Finally, the terminal row is



$$
a=\bigl(k_1+r+1,\ 1-r,\ 4s-r-1,\ 1-r\bigr),          \tag{4.4}
$$



reduced modulo $p$.  Equations (2.5) and (4.4) give the second part of
(1.4).

## 5. Coefficientwise $4p$-periodicity

The coefficient formula for (2.1) is



$$
\widehat T_k=
 \sum_{\substack{\ell\\p\nmid r+\ell+k+1}}
 g_\ell\,
 \frac{W_{\mathcal L}(r+\ell+k+1)}
      {r+\ell+k+1}.                                   \tag{5.1}
$$



Replacing $k$ by $k+4p$ preserves all three ingredients:

- the condition that the denominator is divisible by $p$;
- the inverse of every retained denominator modulo $p$;
- the endpoint weight, because $4p\equiv0\pmod4$.

Thus (1.6) holds coefficient by coefficient, including every omitted
Cartier term.  Iterating (4.3) four times gives



$$
Y_5=M^4Y_1+M^3bw_1+M^2bw_2+Mbw_3+bw_4.              \tag{5.2}
$$



Since $Y_5=Y_1$, equation (1.7) follows.

## 6. The exact augmented-rank criterion

Let $U_k$ be Item 224's canonical common-line solution, and put



$$
v=(U_{k_1},U_{k_1+1},U_{k_1+2},U_{k_1+3})^t.        \tag{6.1}
$$



A collision has $Y_1=\lambda v$.  Define



$$
C_1=0,\quad V_1=v,\qquad
 C_{q+1}=MC_q+bw_q,\quad V_{q+1}=MV_q.                \tag{6.2}
$$



Then the exact formal equations are



$$
\begin{array}{rcl}
\beta\lambda&=&11,\\
(aV_q)\lambda&=&(-1)^rw_q-aC_q,\qquad q=1,2,3,4,\\
\bigl((I-M^4)v\bigr)_j\lambda
 &=&\bigl(M^3bw_1+M^2bw_2+Mbw_3+bw_4\bigr)_j,
 \quad j=0,1,2,3.
\end{array}                                            \tag{6.3}
$$



These are the nine rows $c_i\lambda=d_i$ of (1.8).  Because the first
terminal right-hand side is $7(-1)^r\ne0$ for $p\ge17$, the zero
coefficient-column edge case cannot be silently accepted.  Linear
algebra gives the exact criterion



$$
\operatorname{rank}[c\mid d]=\operatorname{rank}c=1
 \iff
 \left(\exists i:c_i\ne0\right)
 \ \text{and}\ 
 c_id_j-c_jd_i=0\ \text{for every }i<j.               \tag{6.4}
$$



The minor from the bottom and first-terminal rows is



$$
7(-1)^r\beta-11\tau=\Omega.                          \tag{6.5}
$$



The minor from the first and second terminals is the negative of
Item 225's $\Psi$.  Therefore Item 226 retains both earlier
conditions and adds the remaining phase and closure minors.

This formulation is important: a nonzero forcing vector by itself is
not a contradiction.  The contradiction is precisely the augmented
rank being larger than the coefficient rank.

## 7. Why $\Delta\ne0$ makes closure complete

Assume



$$
\Delta=\det(I-M^4)\ne0.       \tag{7.1}
$$



Then (1.7) has a unique solution $Y_1$.  The actual regularized moment
state satisfies (1.7) by Sections 4--5, so it is that unique solution.
If a scalar $\lambda$ makes $\lambda v$ satisfy closure, it must
therefore equal the actual state.

All moments in $Y_1$ are below the first Cartier pole.  The Item 224
recurrence can be propagated backward from $Y_1$ to
$(T_0,T_1,T_2,T_3)$: the relevant leading pivots are
$r+1,r+2,\ldots$, all $p$-units on this range.  Hence the actual
initial vector is $\lambda$ times Item 224's common line, which is
equivalent to



$$
S_0=S_1=0.                   \tag{7.2}
$$



The reverse implication is immediate.  This proves the regular
fixed-point completeness theorem.

When $\Delta=0$, fixed points need not be unique.  The nine-equation
criterion remains necessary, but closure alone is not declared
sufficient.

## 8. Exact finite classification and rank-degenerate rows

Through $p\le401$, the census is



$$
\begin{array}{lr}
\text{all admissible rows}&1153\\
s=1\text{ rows}&38\\
s\ge2\text{ rows}&1115\\
\Delta\ne0\text{ rows}&1100\\
\Delta=0\text{ rows}&15\\
\text{formally solvable nine-equation rows}&0.
\end{array}                                            \tag{8.1}
$$



The 15 exact determinant-zero pairs are



$$
\begin{aligned}
 &(41,4),(73,8),(103,15),(109,2),(191,13),\\
 &(191,19),(193,16),(197,24),(211,17),(281,18),\\
 &(337,16),(349,18),(373,38),(389,14),(401,46).
\end{aligned}                                          \tag{8.2}
$$



Each pair denotes $(p,s)$.  Every row in (8.2) still has augmented
rank strictly larger than coefficient rank, so each is formally
excluded within the finite census.

For the six closure-only minors in coordinate order
$(01,02,03,12,13,23)$, the exact zero lists are



$$
\begin{array}{c|l}
01&(47,5)\\
02&(73,4),(167,13),(241,34),(251,39),(283,15),(353,16),
    (367,53),(397,38)\\
03&(29,4),(149,2),(151,9),(401,32)\\
12&(107,15),(127,3),(191,19),(199,27),(229,24),(359,29),
    (373,34),(397,6)\\
13&(131,15),(163,23),(271,3),(383,7)\\
23&(101,14),(127,19),(163,25),(277,32),(379,5).
\end{array}                                            \tag{8.3}
$$



Thus no one of these six minors is a uniform unit.  The lists are
finite evidence only; they are not symbolic classifications of all
zeros.  The complete row transcript has SHA-256

815c4c714a8e0b4996884337248aea91f643d0f69f1279d2b212a998461627ac.

On all 74 admissible $s\ge2$ rows through $p\le101$, the checker
also evaluates the original regularized coefficient sums and verifies:

- all four exact $q p$ terminal equations;
- every one-phase state transfer;
- coefficientwise $4p$-periodicity;
- the affine closure and augmented-rank construction.

These finite replays check the formulas; Sections 2--7 contain the
all-row proofs.

## 9. Consequence and remaining obstruction

Item 226 replaces the two-scalar necessary system
$\Omega=\Psi=0$ by a complete nine-row formal compatibility test and,
when $\Delta\ne0$, an exact reformulation of the original collision.
This is a structural advance, but it is not yet a rate theorem.

An all-prime result now requires at least one of:

- a unit or controlled-zero theorem for an augmented minor;
- a factorization and density bound for $\Delta=0$;
- a direct theorem that coefficient and augmented ranks differ on all
  admissible rows.

The finite exceptions in (8.2)--(8.3) show why a claim based on one
unchecked determinant would be invalid.

The $j=2$ capacity remains $2/35$ per $m$, and Item 226 books
rate $0$.

## 10. Reproduction and status ledger

From the portable archive root:

~~~
python scripts/item226_j2_four_phase_closure_certificate.py \
  --output results/item226_j2_four_phase_closure_certificate.json
python scripts/item226_j2_four_phase_closure_certificate.py \
  --output results/item226_j2_four_phase_closure_certificate_replay.json
~~~

The checker uses only Python's standard library and the frozen Item
219, 221, 224, and 225 helpers stored beside it.

**PROVED**

- exact one-phase transfer with every $q p$ multiplicity retained;
- coefficientwise $4p$-periodicity and four-phase closure;
- exact nine-equation augmented-rank/minor solvability;
- collision implies formal solvability on every $s\ge2$ row;
- closure solvability is equivalent to the original common gate when
  $\Delta\ne0$.

**EXACT FINITE**

- formal inconsistency on every $s\ge2$ row through $p\le401$;
- the 15 determinant-zero rows in (8.2), each separately inconsistent;
- the six individual-minor zero lists in (8.3).

**OPEN**

- an all-prime augmented-rank inconsistency theorem;
- a factorization or density theorem for $\Delta=0$;
- the exceptional $s=1$ family;
- a zero-rate theorem for $j=2$;
- any capacity reduction or conclusion about $e+\pi$.

