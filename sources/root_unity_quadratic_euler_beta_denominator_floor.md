> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The quadratic Euler ratio has exponential reduced-denominator floors

## Exact beta tails, adjacent determinants, and the published $\pi^2$ measure used here

Checked: 2026-08-27 UTC

## 1. Statement

Let



$$
A_N=(2N+2)(2N+1),\qquad
 G_N=\gcd(A_N|E_{2N}|,|E_{2N+2}|),                         \tag{1}
$$



and define the reduced positive integers



$$
P_N=\frac {|E_{2N+2}|}{G_N},\qquad
 Q_N=\frac {A_N|E_{2N}|}{G_N}.                             \tag{2}
$$



Then $\gcd(P_N,Q_N)=1$.  Put



$$
\alpha=\frac4{\pi^2},\qquad s=2N+1.       \tag{3}
$$



**Theorem 1.1.**  For every $N\geq1$,



$$
\frac {P_N}{Q_N}
   =\alpha\,\frac{\beta(s+2)}{\beta(s)}>\alpha,             \tag{4}
$$



where



$$
\beta(u)=\sum_{k\geq0}
                         \frac {(-1)^k}{(2k+1)^u}.           \tag{5}
$$



More precisely,



$$
\boxed{
 \alpha\left(\frac8{3^{s+2}}-\frac {24}{5^{s+2}}\right)
 <
 \frac {P_N}{Q_N}-\alpha
 <
 \alpha\,
 \frac {8/3^{s+2}}{1-3^{-s}}.}                             \tag{6}
$$



Consequently,



$$
\boxed{
 \frac {P_N}{Q_N}-\frac4{\pi^2}
   =\frac {32}{\pi^2\,3^{2N+3}}
      \left(1+O\left((3/5)^{2N+1}\right)\right).}           \tag{7}
$$



Let the safe decimal upper bound



$$
\overline\mu=5.095412                     \tag{8}
$$



be chosen just above Zudilin's proved bound
$5.09541178\ldots$ for the irrationality exponent of
$\zeta(2)=\pi^2/6$.  For every $\varepsilon>0$,



$$
\boxed{
 \log Q_N\geq
 \frac {2\log3}{\overline\mu+\varepsilon}\,N
       +O_\varepsilon(1).}                                  \tag{9}
$$



In particular,



$$
\boxed{
 \liminf_{N\to\infty}\frac{\log Q_N}{N}
 \geq\frac {2\log3}{\overline\mu}
 =0.4312162740\ldots .}                                    \tag{10}
$$



Equivalently,



$$
G_N\leq A_N|E_{2N}|
 \exp\left(-(0.4312162740\ldots-o(1))N\right).         \tag{11}
$$



There is a stronger unconditional statement for every *adjacent pair*,
which does not use an irrationality measure.  Put



$$
D_N=P_NQ_{N+1}-P_{N+1}Q_N.
$$



**Theorem 1.2 (adjacent integral determinant).**  The reduced ratios
$P_N/Q_N$ are strictly decreasing, and for every $N\geq1$,



$$
D_N>0,\qquad v_2(D_N)=1.                 \tag{11a}
$$



In particular,



$$
\boxed{
 Q_NQ_{N+1}>
       \frac {13\pi^2}{216}\,3^{2N+3}.}                   \tag{11b}
$$



Consequently,



$$
\boxed{
 \liminf_{N\to\infty}
 \frac{\log Q_N+\log Q_{N+1}}{N}\geq2\log3,\qquad
 \limsup_{N\to\infty}\frac{\log Q_N}{N}\geq\log3.}    \tag{11c}
$$



This is an unconditional exponential lower bound for the reduced
denominator, with the sharper statement (11b) for adjacent products.  It
is not strong enough to determine the primitive-height asymptotic: the
full Euler scale is
$\log(A_N|E_{2N}|)=2N\log N+O(N)$, whereas (10) removes only a
linear-in-$N$ term.  Thus (9)--(11) do not prove
$\log G_N=o(N\log N)$, do not bound the isolated factor $J_N$ at the
needed leading scale, and do not classify $e+\pi$.

## 2. Exact beta-ratio identity

The classical beta-value formula for the secant Euler numbers is



$$
|E_{2N}|=
 \frac {4^{N+1}(2N)!}{\pi^{2N+1}}\,\beta(2N+1).             \tag{12}
$$



Applying (12) at $N$ and $N+1$, and cancelling
$(2N+2)! = A_N(2N)!$, gives



$$
\frac {|E_{2N+2}|}{A_N|E_{2N}|}
 =\frac4{\pi^2}
  \frac{\beta(2N+3)}{\beta(2N+1)}.                         \tag{13}
$$



Dividing numerator and denominator by their gcd $G_N$ does not change
the ratio, proving (4) except for its sign.

## 3. Signed nearest-pole tail

For $s>0$,



$$
\begin{aligned}
 \beta(s+2)-\beta(s)
 &=\sum_{k\geq1}(-1)^{k+1}d_k(s),\\
 d_k(s)&=(2k+1)^{-s}-(2k+1)^{-s-2}.                        \tag{14}
 \end{aligned}
$$



The function



$$
x^{-s}(1-x^{-2})                     \tag{15}
$$



is strictly decreasing for $x\geq3$ when $s\geq1$.  Hence the terms
$d_k(s)$ are positive and strictly decreasing.  The alternating-series
bounds give



$$
0<
 \frac8{3^{s+2}}-\frac {24}{5^{s+2}}
 <
 \beta(s+2)-\beta(s)
 <
 \frac8{3^{s+2}}.                                          \tag{16}
$$



The same alternating-series argument gives



$$
1-3^{-s}<\beta(s)<1.               \tag{17}
$$



Since



$$
\frac {P_N}{Q_N}-\alpha
 =\alpha\,
  \frac{\beta(s+2)-\beta(s)}{\beta(s)},                    \tag{18}
$$



equations (16)--(17) prove (6), including strict positivity.  Dividing
the second term in (16) by the first gives



$$
\frac{24/5^{s+2}}{8/3^{s+2}}
   =3(3/5)^{s+2},                                           \tag{19}
$$



and $1/\beta(s)=1+O(3^{-s})$.  This proves (7).

For later use, (6) also supplies the uniform upper bound



$$
0<\frac {P_N}{Q_N}-\alpha
 <
 \frac {432}{13\pi^2}\,3^{-(2N+3)}
 \qquad(N\geq1),                                           \tag{20}
$$



because $1-3^{-s}\geq1-3^{-3}=26/27$.

## 4. The adjacent determinant and its exact 2-part

Write $e_N=P_N/Q_N-\alpha$, and let



$$
T_N=\alpha\frac8{3^{s+2}}.
$$



The lower bound in (6), divided by $T_N$, is



$$
1-3(3/5)^{s+2}\geq1-3(3/5)^5>\frac34.                  \tag{20a}
$$



The upper bound at $N+1$, divided by the *same* $T_N$, is at most



$$
\frac1{9(1-3^{-(s+2)})}
 \leq\frac {27}{242}<\frac18.                            \tag{20b}
$$



Thus $e_N>e_{N+1}>0$, so the reduced fractions $P_N/Q_N$ are
strictly decreasing and $D_N$ is a positive integer.  Moreover, (20)
gives



$$
1\leq D_N
   =Q_NQ_{N+1}(e_N-e_{N+1})
   <\frac {432}{13\pi^2}\,
       Q_NQ_{N+1}3^{-(2N+3)}.                             \tag{20c}
$$



The integral determinant has a useful exact parity refinement.  Every
secant Euler number $E_{2j}$ is odd.  For completeness, this follows
inductively modulo 2 from



$$
\sum_{j=0}^{n}\binom{2n}{2j}E_{2j}=0,
 \qquad
 \sum_{j=0}^{n-1}\binom{2n}{2j}=2^{2n-1}-1.              \tag{20d}
$$



It follows from (1) that $G_N$ and $P_N$ are odd, whereas



$$
v_2(Q_N)=v_2(A_N)=1+v_2(N+1).           \tag{20e}
$$



Exactly one of $N+1,N+2$ is odd.  Hence one of $Q_N,Q_{N+1}$ has
2-adic valuation 1 and the other has valuation at least 2.  Since both
$P_N,P_{N+1}$ are odd, the two terms defining $D_N$ have distinct
2-adic valuations, proving $v_2(D_N)=1$.  Replacing the first inequality
in (20c) by $2\leq D_N$ proves (11b).

Taking logarithms in (11b) proves the first assertion in (11c).  If the
second assertion failed, there would be an $\eta>0$ such that
$\log Q_k\leq(\log3-\eta)k$ for every sufficiently large $k$.  The
sum at $k=N,N+1$ would then be at most
$2(\log3-\eta)N+O(1)$, contradicting the first assertion.  Notice that
the exact equality $v_2(D_N)=1$ rules out a growing *dyadic*
determinant divisor; it does not rule out growing odd divisors and
supplies no stronger individual liminf.

## 5. Transfer of the irrationality measure

Zudilin proved



$$
\mu(\zeta(2))\leq5.09541178\ldots<\overline\mu.            \tag{21}
$$



The irrationality exponent is invariant under a nonconstant rational
fractional-linear transformation.  Here this can also be seen directly
from



$$
\alpha=\frac2{3\zeta(2)}.               \tag{22}
$$



If $p/q$ is sufficiently close to $\alpha$, then $p\asymp q$, and


$$
\left|\zeta(2)-\frac {2q}{3p}\right|
   =\frac {2q}{3\alpha p}
      \left|\alpha-\frac pq\right|.                         \tag{23}
$$



After reduction, the denominator on the left is at most $3p\asymp q$.
Therefore (21) implies that for every $\varepsilon>0$ there is a
constant $c_\varepsilon>0$ such that



$$
\left|\alpha-\frac pq\right|
       \geq c_\varepsilon
                 q^{-(\overline\mu+\varepsilon)}            \tag{24}
$$



for all sufficiently large reduced denominators $q$.

The sequence $Q_N$ tends to infinity.  Indeed, otherwise a bounded
denominator subsequence of the reduced rationals $P_N/Q_N$ would have a
constant rational subsequence, contradicting (7) and the irrationality of
$\alpha$.  Apply (24) to (2), and combine it with (20):



$$
c_\varepsilon Q_N^{-(\overline\mu+\varepsilon)}
 <
 \frac {432}{13\pi^2}\,3^{-(2N+3)}.                        \tag{25}
$$



Taking logarithms proves (9).  Letting $\varepsilon\downarrow0$ proves
(10), and the identity $Q_N=A_N|E_{2N}|/G_N$ gives (11).

## 6. Why these bounds cannot settle the gcd obstruction

Stirling's formula and (12) give



$$
\log(A_N|E_{2N}|)
                    =2N\log N+O(N).                         \tag{26}
$$



Combining (11) and (26) still gives only



$$
\log G_N\leq2N\log N+O(N),          \tag{27}
$$



which has the same leading term as the trivial bound 

$$
G_N\leq
A_N|E_{2N}|
$$

.  The exponential beta-tail $3^{-2N}$ can force only an
exponential reduced denominator through any fixed irrationality measure.
To remove a positive proportion of the factorial logarithm would require
a qualitatively stronger input than a one-dimensional fixed-exponent
irrationality measure for $\pi^2$.

Thus the exact conclusion has three parts:

1. every adjacent denominator product has the unconditional lower bound
   (11b);
2. the published $\pi^2$ measure also gives the individual lower bound
   (9); but
3. both facts are too weak by a factor of $\log N$ in the exponent to
   control the primitive height at the item-$J_N$ threshold.

## 7. Primary reference and replay

The irrationality exponent used above is Theorem 1 of:

W. Zudilin, *On the irrationality measure of $\pi^2$*,
Russian Math. Surveys 68:6 (2013), 1133--1135,
<https://doi.org/10.1070/RM2013v068n06ABEH004872>.

Its theorem states
$\mu(\zeta(2))\leq5.09541178\ldots$.  The deterministic companion
certificate checks the exact reduction $P_N,Q_N$, the beta-tail
inequalities, the adjacent determinant and its exact 2-adic valuation on
a declared finite grid, the numerical constant in (10), and the
$N=1643$ denominator metadata.  The analytic proof above, not the finite
grid, establishes the all-$N$ theorems.

From the research directory run

    python3 scripts/root_unity_quadratic_euler_beta_denominator_certificate.py
    sha256sum -c results/root_unity_quadratic_euler_beta_denominator_hashes.sha256

No claim in this package classifies $e+\pi$.
