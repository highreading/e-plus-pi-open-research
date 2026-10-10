> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 224 — Inhomogeneous Cartier terminals in the fixed $j=2$ cell

Checked: 2026-08-31 (Beijing time)

## 1. Scope and verdict

Retain the normalized Item 219/221 cell



$$
4m+1=5p-2s,\qquad 1\le s\le\frac{p-3}{6},\qquad
 s\equiv\frac{p-1}{2}\pmod 2,\qquad p\ge 11,                 \tag{1.1}
$$



where $p$ is prime, and put



$$
r=\frac{p-6s-3}{2},\qquad
 f_0(z)=z^r(1-z)^r(1+z)(1+z^2)^{2s}.                       \tag{1.2}
$$



This item develops the moment recurrence suggested after Item 221.  It
does not combine $j=2$ with another fixed cell.

> **PROVED — exact inhomogeneous terminal theorem.**  For the shifted
> $f_0$-periods $T_k$, the boundary-free interior recurrence is
> 

$$
> \begin{aligned}
> &(k+r+1)T_k+(1-r)T_{k+1}+(4s-r-1)T_{k+2}\\
> &\hspace{19mm} +(1-r)T_{k+3}
> -(k+2r+4s+6)T_{k+4}=0.                              \tag{1.3}
> \end{aligned}
>
$$


> At its first upper and lower resonances it is not homogeneous.  The
> exact regularized terminal equations are
> 

$$
>       \tau(T)=7(-1)^r,\qquad \beta(T)=11.            \tag{1.4}
>
$$


> In particular, reducing the coefficient $-p$ at the upper terminal
> before regularizing loses the nonzero constant $7(-1)^r$.

> **PROVED — a necessary scalar compatibility for $s\ge2$.**  An exact
> $z^3$-reduction shows that every common-log collision must have
> 

$$
> (T_0,T_1,T_2,T_3)=
> \lambda\left(
> 0,\ 4s-2,\ 2s-5,\
> -\frac{52s^2-36s-27}{4(s-1)}
> \right).                                             \tag{1.5}
>
$$


> Let $U$ denote the recurrence solution with $\lambda=1$, propagated
> through all unit pivots, and define
> 

$$
> \tau=\tau(U),\qquad \beta=\beta(U),\qquad
> \Omega_{p,s}=7(-1)^r\beta-11\tau.                    \tag{1.6}
>
$$


> Then an actual common-log collision with $s\ge2$ requires
> 

$$
>                 \boxed{\beta\ne0,\quad\tau\ne0,\quad
>                        \Omega_{p,s}=0\pmod p.}        \tag{1.7}
>
$$


> This condition is necessary only.

> **EXACT FINITE ONLY.**  Among the 1,115 admissible $s\ge2$ rows with
> $p\le401$, (1.7) excludes 1,108 by $\Omega_{p,s}\ne0$.  Exactly
> seven rows are formally compatible:
> 

$$
> (23,3),(157,4),(193,26),(241,4),(311,47),(349,50),(397,44). \tag{1.8}
>
$$


> Direct evaluation of the original two common-log periods shows that
> none of these seven rows is a collision.  Thus they are explicit
> counterexamples to the stronger assertion that this terminal
> recurrence alone always yields a contradiction; they are **not**
> counterexamples to the desired common-log exclusion.

> **OPEN.**  No all-prime classification or density bound for the zeros
> of $\Omega_{p,s}$ is proved.  The $s=1$ family is outside the
> $z^3$-reduction and remains open.  Item 224 therefore books no
> capacity reduction and proves nothing about $e+\pi$.

## 2. Period normalization and the common gate

Work in $\mathbb F_p[i]$, with $i^2=-1$, and let



$$
\chi=(-1)^{(p-1)/2},\qquad
 \mathcal L_\chi(V)=9V(1)+(-10+\chi i)V(i)
                            +(-10-\chi i)V(-i).        \tag{2.1}
$$



For every shift with a nonsingular polynomial primitive, set



$$
F_k(x)=\int_0^x z^k f_0(z)\,dz,\qquad
 T_k=\mathcal L_\chi(F_k).                            \tag{2.2}
$$



This retains both $p\bmod4$ phases.  Equivalently, if
$(1-z)^r(1+z)(1+z^2)^{2s}=\sum_\ell a_\ell z^\ell$, then



$$
T_k=\sum_\ell a_\ell\,
 \frac{W_\chi(r+\ell+k+1)}{r+\ell+k+1},               \tag{2.3}
$$



where



$$
\begin{array}{c|rrrr}
 n\bmod4&0&1&2&3\\ \hline
 W_\chi(n)&-11&9-2\chi&29&9+2\chi .
\end{array}                                            \tag{2.4}
$$



At a zero denominator, Section 4 uses the unreduced characteristic-zero
primitive and takes the finite product forced by (1.3); it never assigns
an inverse to $0\pmod p$.

Item 221 proved that the original two $j=2$ common-log periods
$S_0,S_1$ obey



$$
S_0=T_0,\qquad
 S_0=S_1=0
 \iff
 T_0=0,\quad(5-2s)T_1+2(2s-1)T_2=0.                 \tag{2.5}
$$



## 3. Derivation of the five-term recurrence

Put



$$
K_k(z)=z^{k+1}(1-z^4)f_0(z).                        \tag{3.1}
$$



Logarithmic differentiation of $f_0$ gives



$$
\frac{f'_0}{f_0}
 =\frac rz-\frac r{1-z}+\frac1{1+z}
       +\frac{4sz}{1+z^2}.                           \tag{3.2}
$$



Using



$$
\frac{1-z^4}{z-1}=-(1+z+z^2+z^3),\quad
 \frac{1-z^4}{z+1}=1-z+z^2-z^3,\quad
 \frac{1-z^4}{1+z^2}=1-z^2,                         \tag{3.3}
$$



and collecting powers of $z$ in $K'_k$ yields exactly



$$
\begin{aligned}
 K'_k={}&(k+r+1)z^kf_0+(1-r)z^{k+1}f_0
 +(4s-r-1)z^{k+2}f_0\\
 &+(1-r)z^{k+3}f_0
 -(k+2r+4s+6)z^{k+4}f_0.                            \tag{3.4}
\end{aligned}
$$



For $-r\le k\le2s-4$, $K_k$ vanishes at
$0,1,i,-i$, and all five required primitives are nonsingular.
Applying $\mathcal L_\chi$ proves (1.3).

The forward pivots, for $0\le k\le2s-4$, are



$$
-(k+2r+4s+6)
 =-\bigl(p-(2s-k-3)\bigr),                           \tag{3.5}
$$



where $2s-k-3$ runs through $2s-3,\ldots,1$.
The backward pivots, for $-1\ge k\ge-r$, are
$k+r+1=r,\ldots,1$.  Because



$$
1\le r<p,\qquad 1\le2s-3<p,                         \tag{3.6}
$$



every propagation pivot is a $p$-unit.

## 4. The two inhomogeneous Cartier terminals

### 4.1 Upper terminal

At $k=2s-3$, the last coefficient in (3.4) is



$$
-(k+2r+4s+6)=-p.                                    \tag{4.1}
$$



The degree of $f_0$ is $p-2s-2$, and its leading coefficient is
$(-1)^r$.  Hence the coefficient of $z^{p-1}$ in
$z^{2s+1}f_0$ is $(-1)^r$.  In the characteristic-zero primitive,
the resonant part is $(-1)^rz^p/p$.  Item 221's exact phase
calculation gives



$$
\mathcal L_\chi(z^p)=7.                             \tag{4.2}
$$



Therefore $pT_{2s+1}$, rather than $T_{2s+1}$, has the well-defined
reduction $7(-1)^r$.  Moving the term $-pT_{2s+1}$ in (1.3) to the
other side gives



$$
\begin{aligned}
\tau(T):={}&(r+2s-2)T_{2s-3}
 +(1-r)T_{2s-2}\\
& +(4s-r-1)T_{2s-1}
 +(1-r)T_{2s}
=7(-1)^r.                                            \tag{4.3}
\end{aligned}
$$



This is the top Cartier residue.  Simply replacing $-p$ by zero
would incorrectly replace (4.3) by a homogeneous equation.

### 4.2 Lower terminal

At $k=-r-1$, the coefficient $k+r+1$ of the logarithmic moment
$T_{-r-1}$ is zero.  Meanwhile



$$
K_{-r-1}(z)
 =(1-z^4)(1-z)^r(1+z)(1+z^2)^{2s}                  \tag{4.4}
$$



has value $1$ at $0$ and value $0$ at $1,i,-i$.  Each path
integral of $K'_{-r-1}$ is therefore $-1$, while the sum of the
three coefficients in (2.1) is $-11$.  Consequently



$$
\begin{aligned}
\beta(T):={}&(1-r)T_{-r}
 +(4s-r-1)T_{-r+1}\\
& +(1-r)T_{-r+2}
 -(r+4s+5)T_{-r+3}
=11.                                                  \tag{4.5}
\end{aligned}
$$



No logarithmic period is introduced: its coefficient vanishes before
the boundary value is evaluated.

## 5. Exact $z^3$-reduction and the initial line

For $s\ge2$, direct rational differentiation proves



$$
z^3f_0(z)\,dz=d(H_3f_0)+Q_3(z)f_0(z)\,dz,             \tag{5.1}
$$



where



$$
H_3(z)=
 \frac{(10s-5)z+4z^2-4z^3+4z^4-(10s-1)z^5}
      {2(s-1)(10s-1)(1+z)},                           \tag{5.2}
$$



and



$$
Q_3(z)=
 \frac{60s^2-20s-5+4(-30s^2+11s+4)z-(20s^2+52s+1)z^2}
      {4(s-1)(10s-1)}.                                \tag{5.3}
$$



After clearing denominators, (5.1) is a zero polynomial identity in
$z,s$.  The factor $H_3f_0$ is regular and vanishes at all four
path endpoints.  Thus (5.1) expresses $T_3$ in terms of
$T_0,T_1,T_2$.  Substituting the common gate (2.5) gives precisely
(1.5).

All denominators have been audited.  For $s\ge2$, $s-1$ is a
$p$-unit.  Item 221 proved that $10s-1$ is a unit: the cell bound
gives $0<10s-1<2p$; if $p\mid10s-1$, then $p=10s-1$, but



$$
\frac{p-1}{2}=5s-1\equiv s-1\pmod2
$$



contradicts (1.1).  The constants $2,4,7,11$ are units because
$p\ge11$, except that $11=0$ only at $p=11$; the only admissible
row at $p=11$ has $s=1$ and is outside the $s\ge2$ theorem.

The factor $s-1$ in (5.2)--(5.3) is a genuine exceptional
specialization.  When $s=1$,
$\deg(z^3f_0)=p-1$, with nonzero leading coefficient, whereas
$\deg(Q_2f_0)\le p-2$, and a polynomial derivative in
$\mathbb F_p[z]$ has zero $z^{p-1}$-coefficient.  Hence no
sub-Frobenius polynomial exact reduction with a quadratic remainder can
specialize (5.1) to $s=1$.  This is a scoped obstruction, not an
all-mechanism exclusion of the $s=1$ family.

## 6. Compatibility theorem

Normalize the vector in (1.5) by setting $\lambda=1$, and call it
$(U_0,U_1,U_2,U_3)$.  Use the unit pivots (3.5)--(3.6) to propagate
forward through $U_{2s}$ and backward through $U_{-r}$.  Define
$\tau=\tau(U)$ and $\beta=\beta(U)$ by (4.3) and (4.5).

If an actual common-log collision exists, its moments equal
$T_k=\lambda U_k$ throughout the propagated interval.  Equations
(4.3) and (4.5) then require



$$
\lambda\tau=7(-1)^r,\qquad
             \lambda\beta=11.                         \tag{6.1}
$$



Thus neither $\tau$ nor $\beta$ can vanish, and eliminating
$\lambda$ gives (1.7).

The converse is not asserted.  The five-term recurrence plus its two
terminal values does not characterize the original path periods.
Accordingly, a row with $\Omega_{p,s}=0$ is called
*formal-compatible*, not a collision.

There is also a canonical characteristic-zero numerator.  The integer



$$
D_{p,s}=4(s-1)\,r!\prod_{d=1}^{2s-3}(p-d)            \tag{6.2}
$$



is a $p$-unit and clears every denominator in
$\beta,\tau,\Omega_{p,s}$.  This follows inductively from the initial
denominator $4(s-1)$, the forward pivots $p-d$, and the backward
pivots $1,\ldots,r$.  Hence



$$
N_{p,s}=D_{p,s}\Omega_{p,s}\in\mathbb Z,\qquad
 \Omega_{p,s}=0\pmod p\iff p\mid N_{p,s}.             \tag{6.3}
$$



The same induction gives
$\log(1+|N_{p,s}|)=O(p\log p)$.  This is far too large to turn
nonzero characteristic-zero values into $p$-nondivisibility, and the
seven rows below actually have $p\mid N_{p,s}$.  Thus this height
bound supplies neither an all-prime theorem nor a zero-rate theorem.

## 7. Exact finite classification and its limitation

The deterministic replay enumerates every admissible row through
$p\le401$.  Its counts are



$$
\begin{array}{lr}
\text{all rows}&1153\\
s=1\text{ rows}&38\\
s\ge2\text{ rows}&1115\\
\Omega\ne0\text{ exclusions}&1108\\
\Omega=0\text{ formal-compatible rows}&7.
\end{array}                                            \tag{7.1}
$$



For the seven formal-compatible rows, the exact modular data are:



$$
\begin{array}{c|r|r|r|r|r|r}
p&s&r&\beta&\tau&T_0^{\rm actual}&S_1^{\rm actual}\\ \hline
23&3&1&5&1&4&13\\
157&4&65&84&75&146&36\\
193&26&17&116&49&133&161\\
241&4&107&64&25&212&124\\
311&47&13&272&251&126&152\\
349&50&23&270&82&240&198\\
397&44&65&166&147&314&123
\end{array}                                            \tag{7.2}
$$



Every entry is reduced modulo its row prime.  Both original common-log
periods are nonzero on every listed row, so all seven are actual
non-collisions.  The complete row transcript has SHA-256

f26052349a6471f532a8de0a16c02fb7c3f7b8e4d54c9b74c281515d908d27e6.

The checker also re-evaluates the top constant $7(-1)^r$, the bottom
constant $11$, and the rational-to-modular propagation on all 74
admissible $s\ge2$ rows through $p\le101$.  These finite checks
replay the formulas; the all-row proofs are Sections 3--6.

## 8. Capacity bookkeeping

The fixed $j=2$ common-log cell has capacity $2/35$ per $m$.
Item 224 does not exclude it, so the booked reduction here is exactly
zero.  Excluding $j=2$ in the future would be useful only together
with the independent $j=1$ branch: excluding both would leave



$$
0.1132379841892420\ldots\ \text{per }m
 =0.0188729973648737\ldots\ \text{per }6m,            \tag{8.1}
$$



below $G=0.01963298367\ldots$ per $6m$.  This comparison is
conditional; neither exclusion is supplied by Item 224.

## 9. Reproduction and status ledger

From the portable archive root:

~~~
python scripts/item224_j2_cartier_terminal_certificate.py \
  --output results/item224_j2_cartier_terminal_certificate.json
python scripts/item224_j2_cartier_terminal_certificate.py \
  --output results/item224_j2_cartier_terminal_certificate_replay.json
~~~

The checker uses only Python's standard library and the frozen Item 219
and Item 221 helper certificates stored beside it.  It symbolically
replays (3.4) and (5.1), audits the recurrence pivots and rational
clearings, evaluates both terminal regularizations from the original
periods, and performs the finite classification.

**PROVED**

- the exact five-term recurrence and every propagation pivot;
- the top Cartier constant $7(-1)^r$ and bottom boundary constant
  $11$;
- the $z^3$-reduction and common initial line for every $s\ge2$;
- necessity of (1.7);
- integrality and $p$-unit status of the canonical clearing (6.2).

**EXACT FINITE**

- the complete classification through $p\le401$;
- the seven formal-compatible rows in (1.8);
- direct proof within this finite range that all seven are
  non-collisions.

**OPEN**

- an all-prime classification of $\Omega_{p,s}=0$;
- the exceptional $s=1$ family;
- a sublinear or zero-rate theorem for formal-compatible rows;
- any capacity reduction or conclusion about $e+\pi$.

