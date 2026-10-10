> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The quadratic tangent survivor cannot have subexponential denominators

## An exact odd-zeta tail, an adjacent determinant, and the irregular-pair barrier

Checked: 2026-08-27 UTC

## 1. Statement

Let the positive tangent numbers $\tau_r$ be defined by



$$
\tan z=\sum_{r\geq1}\tau_r\frac{z^{2r-1}}{(2r-1)!}.       \tag{1}
$$



For $r\geq1$, put



$$
\begin{aligned}
 G_r&=\gcd\!\left(\tau_{r+1},8r(2r+1)\tau_r\right),\\
 P_r&=\frac{8r(2r+1)\tau_r}{G_r},\qquad
 Q_r=\frac{\tau_{r+1}}{G_r}.
 \end{aligned}                                             \tag{2}
$$



Thus $P_r,Q_r$ are positive and coprime.  The integer $Q_r$ is
exactly the denominator survivor in the $D=2$ root-of-unity constrained
Hermite--Padé endpoint; there is no auxiliary-vector normalization in
(2).

Define



$$
A_r=\sum_{j\geq0}(2j+1)^{-2r}
     =(1-2^{-2r})\zeta(2r).                                \tag{3}
$$



**Theorem 1 (individual exponential floor).**  For every $r\geq1$,



$$
\boxed{\frac{P_r}{Q_r}=\pi^2\frac{A_r}{A_{r+1}}>\pi^2}    \tag{4}
$$



and



$$
0<\frac{P_r}{Q_r}-\pi^2
   <\frac{5\pi^2}{2}\,9^{-r}.                             \tag{5}
$$



More precisely,



$$
\boxed{
 \frac{P_r}{Q_r}-\pi^2
  =\frac{8\pi^2}{9}\,9^{-r}
    \left(1+O\!\left((9/25)^r\right)\right).}             \tag{6}
$$



Let



$$
\overline\mu=5.095412                  \tag{7}
$$



be a safe decimal strictly above Zudilin's proved upper bound
$5.09541178\ldots$ for the irrationality exponent of
$\zeta(2)=\pi^2/6$.  For every $\varepsilon>0$,



$$
\boxed{
 \log Q_r\geq
 \frac{\log9}{\overline\mu+\varepsilon}\,r
       +O_\varepsilon(1).}                                  \tag{8}
$$



Consequently,



$$
\boxed{
 \liminf_{r\to\infty}\frac{\log Q_r}{r}
 \geq\frac{\log9}{\overline\mu}
 =0.4312162740\ldots .}                                    \tag{9}
$$



In particular, **there is no infinite subsequence on which**
$\log Q_r=o(r)$.  This unconditionally rules out the small-survivor
condition proposed for activating the archived $D=2$ endpoint criterion.

There is also a measure-free adjacent statement.

**Theorem 2 (adjacent integral determinant).**  The fractions
$P_r/Q_r$ are strictly decreasing.  If



$$
D_r=P_rQ_{r+1}-P_{r+1}Q_r,                    \tag{10}
$$



then, for every $r\geq1$,



$$
D_r>0,\qquad v_2(D_r)=1,                  \tag{11}
$$



and hence



$$
\boxed{Q_rQ_{r+1}>\frac{4}{5\pi^2}\,9^r.}               \tag{12}
$$



It follows that



$$
\liminf_{r\to\infty}
 \frac{\log Q_r+\log Q_{r+1}}r\geq2\log3,
 \qquad
 \limsup_{r\to\infty}\frac{\log Q_r}{r}\geq\log3.     \tag{13}
$$



Theorems 1--2 are only exponential-scale statements.  Since



$$
\log\tau_{r+1}=2r\log r+O(r),            \tag{14}
$$



they do not prove a factorial-scale lower bound for $Q_r$, or an
$o(r\log r)$ upper bound for $\log G_r$.  They do, however, settle
the precise alternative $\log Q_r=o(r)$ in the negative.

## 2. Exact odd-zeta ratio

The Bernoulli formula for the tangent numbers is



$$
\tau_r=(-1)^{r-1}
 \frac{2^{2r}(2^{2r}-1)}{2r}B_{2r}.                        \tag{15}
$$



The Euler evaluation of $\zeta(2r)$ therefore gives



$$
u_r:=\frac{\tau_r}{2^{2r}(2r-1)!}
 =\frac{(2^{2r}-1)|B_{2r}|}{(2r)!}
 =2\pi^{-2r}A_r.                                           \tag{16}
$$



On the other hand,



$$
\frac{u_r}{u_{r+1}}
 =\frac{8r(2r+1)\tau_r}{\tau_{r+1}}
 =\frac{P_r}{Q_r}.                                         \tag{17}
$$



Combining (16)--(17) proves the identity in (4).

Subtracting consecutive odd-zeta tails gives



$$
A_r-A_{r+1}
 =\sum_{\substack{k\geq3\\k\ \text{odd}}}
     (1-k^{-2})k^{-2r}>0.                                  \tag{18}
$$



Since $A_{r+1}>1$,



$$
0<\frac{P_r}{Q_r}-\pi^2
 =\pi^2\frac{A_r-A_{r+1}}{A_{r+1}}
 <\pi^2\sum_{\substack{k\geq3\\k\ \text{odd}}}k^{-2r}.  \tag{19}
$$



For every decreasing positive function $f$, comparison on intervals
of length two gives



$$
\sum_{\substack{k\geq3\\k\ \text{odd}}}f(k)
 \leq f(3)+\frac12\int_3^\infty f(x)\,dx.                 \tag{20}
$$



Taking $f(x)=x^{-2r}$ yields



$$
\sum_{\substack{k\geq3\\k\ \text{odd}}}k^{-2r}
 \leq9^{-r}\left(1+\frac3{2(2r-1)}\right)
 \leq\frac52\,9^{-r},                                    \tag{21}
$$



which proves (5).

The $k=3$ term in (18) is exactly



$$
\frac89\,9^{-r}.                    \tag{22}
$$



The remaining terms are $O(25^{-r})$, while
$A_{r+1}=1+O(9^{-r-1})$.  Division in (19) proves (6).

## 3. Transfer of the published irrationality measure

Zudilin proved



$$
\mu(\zeta(2))\leq5.09541178\ldots
                    <\overline\mu.                          \tag{23}
$$



Since $\pi^2=6\zeta(2)$, the same upper bound applies to the
irrationality exponent of $\pi^2$.  Directly, if $p/q$ is reduced,
then $p/(6q)$, after reduction, has denominator at most $6q$, and



$$
\left|\pi^2-\frac pq\right|
 =6\left|\zeta(2)-\frac p{6q}\right|.                     \tag{24}
$$



Thus, for every $\varepsilon>0$, there is a
$c_\varepsilon>0$ such that all sufficiently large reduced
denominators obey



$$
\left|\pi^2-\frac pq\right|
 \geq c_\varepsilon q^{-(\overline\mu+\varepsilon)}.      \tag{25}
$$



The denominators $Q_r$ tend to infinity.  Otherwise a bounded-denominator
subsequence of the reduced fractions in (4) would contain a constant
rational subsequence tending, by (6), to the irrational number $\pi^2$.
Apply (25) to $P_r/Q_r$, and combine it with (5):



$$
c_\varepsilon Q_r^{-(\overline\mu+\varepsilon)}
 <\frac{5\pi^2}{2}\,9^{-r}.                               \tag{26}
$$



Taking logarithms proves (8), and then letting
$\varepsilon\downarrow0$ proves (9).

## 4. Strict decrease and the exact two-part

The sequence $A_r$ is a strict Stieltjes moment sequence:



$$
A_r=\sum_{j\geq0}x_j^r,\qquad x_j=(2j+1)^{-2}.            \tag{27}
$$



Cauchy--Schwarz is strict because the support contains more than one
point, so



$$
A_rA_{r+2}>A_{r+1}^2.                    \tag{28}
$$



Therefore $A_r/A_{r+1}>A_{r+1}/A_{r+2}$, proving that the
ratios in (4) strictly decrease.  Hence $D_r$ in (10) is a positive
integer.

Von Staudt--Clausen gives $v_2(B_{2n})=-1$.  Formula (15) then gives
the exact valuation



$$
v_2(\tau_n)=2n-2-v_2(n).                 \tag{29}
$$



In the two entries of the gcd in (2),



$$
\begin{aligned}
 v_2(\tau_{r+1})&=2r-v_2(r+1),\\
 v_2\!\left(8r(2r+1)\tau_r\right)&=2r+1.
 \end{aligned}                                             \tag{30}
$$



Thus



$$
v_2(Q_r)=0,\qquad
                 v_2(P_r)=1+v_2(r+1).                      \tag{31}
$$



Both $Q_r,Q_{r+1}$ are odd, while the two products in (10) have
2-adic valuations $1+v_2(r+1)$ and $1+v_2(r+2)$.  Exactly one of
$r+1,r+2$ is odd, so the two valuations are distinct, their minimum
is one, and (11) follows.

Finally, (5) and strict decrease give



$$
2\leq D_r
 =Q_rQ_{r+1}\left(\frac{P_r}{Q_r}
                    -\frac{P_{r+1}}{Q_{r+1}}\right)
 <\frac{5\pi^2}{2}Q_rQ_{r+1}9^{-r}.                       \tag{32}
$$



This proves (12); taking logarithms proves (13).

## 5. What von Staudt--Clausen and Kummer do not cancel

For an odd prime $p$, formula (15) gives the exact rational valuation



$$
v_p(\tau_n)=v_p(2^{2n}-1)+v_p(B_{2n})-v_p(n),             \tag{33}
$$



and hence



$$
v_p(Q_r)=\max\!\left\{0,
 v_p(\tau_{r+1})-v_p\!\left(8r(2r+1)\tau_r\right)
 \right\}.                                                \tag{34}
$$



Von Staudt--Clausen determines the negative Bernoulli valuations:
the reduced denominator of $B_{2n}$ is the square-free product of
primes $p$ satisfying $p-1\mid2n$.  It does not control positive
valuations of irregular Bernoulli numerators.  Nor can the two
cyclotomic factors by themselves create a large adjacent gcd, because



$$
\gcd(2^{2r}-1,2^{2r+2}-1)
 =2^{\gcd(2r,2r+2)}-1=3.                                  \tag{35}
$$



There is nevertheless no universal odd-coprimality theorem for adjacent
tangent numbers.  Exact Bernoulli arithmetic gives



$$
\begin{array}{c|cc}
 p&v_p(\operatorname{num}B_m)&m\\ \hline
 587&1&m=90,92\\
 491&1&m=336,338.
 \end{array}                                               \tag{36}
$$



The corresponding exact tangent gcds are



$$
\boxed{
 \gcd(\tau_{45},\tau_{46})=2^{88}\cdot587,
 \qquad
 \gcd(\tau_{168},\tau_{169})=2^{331}\cdot491.}           \tag{37}
$$



These odd factors come from the Bernoulli numerators, not from (35):



$$
\begin{array}{c|cc}
 p&2^m\bmod p&m\\ \hline
 587&234,349&m=90,92\\
 491&208,341&m=336,338.
 \end{array}                                               \tag{38}
$$



This is more than an isolated finite accident.  The mod-$p$ Kummer
congruence says that for positive even $m\equiv \ell\pmod{p-1}$,
with $p-1\nmid m$ and $p\nmid m\ell$,



$$
\frac{B_m}{m}
                 \equiv\frac{B_\ell}{\ell}\pmod p.       \tag{39}
$$



It follows from the first row of (36) that



$$
587\mid\gcd(\tau_r,\tau_{r+1})
 \quad\text{if}\quad
 r=45+293k,\ k\geq0,\ 587\nmid r(r+1),                  \tag{40}
$$



and from the second row that



$$
491\mid\gcd(\tau_r,\tau_{r+1})
 \quad\text{if}\quad
 r=168+245k,\ k\geq0,\ 491\nmid r(r+1).                 \tag{41}
$$



Each condition excludes only two residue classes of $k$ modulo the
displayed prime, so (40)--(41) are infinite families.  They rigorously
refute any attempt to obtain a factorial lower bound merely by declaring
adjacent Bernoulli numerator branches incompatible.  They do **not**
show that the aggregate gcd in (2) is factorially large, and they do not
preclude some deeper factorial-scale lower bound for $Q_r$.

## 6. Scale of the remaining gap

Equation (16) can be rearranged as



$$
\tau_n=2\left(\frac2\pi\right)^{2n}(2n-1)!A_n.            \tag{42}
$$



Since $A_n=1+O(9^{-n})$, Stirling's formula gives (14).  Combining
(9), (14), and $G_r=\tau_{r+1}/Q_r$ gives only



$$
\log G_r
 \leq2r\log r+O(r)
   -\left(0.4312162740\ldots-o(1)\right)r.                 \tag{43}
$$



The leading $2r\log r$ term remains untouched.  Thus the exact outcome
is sharply scoped:

1. the desired $o(r)$ denominator subsequence is impossible;
2. every adjacent product has the stronger measure-free floor (12);
3. adjacent irregular pairs obstruct the simplest Bernoulli-coprimality
   route to a factorial floor; and
4. no factorial-scale estimate or classification of $e+\pi$ follows.

## 7. References and replay

The irrationality exponent is Theorem 1 of:

W. Zudilin, *On the irrationality measure of $\pi^2$*,
Russian Math. Surveys **68**:6 (2013), 1133--1135,
<https://doi.org/10.1070/RM2013v068n06ABEH004872>.
It states $\mu(\zeta(2))\leq5.09541178\ldots$.

The Kummer formulation and irregular-pair terminology may be found in:

B. C. Kellner, *On irregular prime power divisors of the Bernoulli
numbers*, Math. Comp. **76** (2007), 405--441,
<https://arxiv.org/abs/math/0409223>.

The deterministic companion certificate reconstructs the tangent numbers
from the differential equation $\tan'(z)=1+\tan^2(z)$, independently
checks the Bernoulli formula, reduces $P_r/Q_r$, verifies the exact
two-adic statements and adjacent determinants on the declared finite grid,
and supplies exact certificates for (36)--(38).  The finite grid is not
used to prove Theorems 1--2 or the Kummer progressions.

From the research directory run

    python3 scripts/root_unity_tangent_survivor_exponential_no_go_certificate.py
    sha256sum -c results/root_unity_tangent_survivor_exponential_no_go_hashes.sha256
