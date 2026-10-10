> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Varying-order factorial-digit rays: exact local content and a Roth barrier

Checked: 2026-08-26 UTC

## 1. Scope and conclusions

Let



$$
s=e+\pi,\qquad
 C_n=\lfloor n!e\rfloor+\lfloor n!\pi\rfloor,\qquad
 x_n=n!s-C_n,
\tag{1}
$$



and, for $a\geq1$, $b\geq0$, $b\leq a+1$, put



$$
W_{a,b}=\Delta^b(a!),\qquad
 Z_{a,b}=\Delta^bC_a,\qquad
 H_{a,b}=\gcd(W_{a,b},Z_{a,b}).
\tag{2}
$$



The endpoint-matched Hermite--Padé construction in the companion fixed-ray
note gives the fully primitive linear form



$$
L_{a,b}=\frac{W_{a,b}s-Z_{a,b}}{H_{a,b}}
 =\frac{\Delta^b x_a}{H_{a,b}}.
\tag{3}
$$



This note analyzes (3) when $b$ varies with $a$, including
$b=o(a)$, $b/a\to\lambda$, $b=a-h$, $b=a$, and $b=a+1$.
The main new exact decomposition is



$$
W_{a,b}=a!D_{a,b},\qquad
 Z_{a,b}=D_{a,b}C_a+K_{a,b},
\tag{4}
$$



where $K_{a,b}$ is a positive integer combination of only the next
$b$ canonical digits.  If



$$
g_{a,b}=\gcd(D_{a,b},K_{a,b}),\qquad
 D'=D_{a,b}/g_{a,b},\qquad K'=K_{a,b}/g_{a,b},
\tag{5}
$$



then the full endpoint gcd factors exactly as



$$
\boxed{H_{a,b}=g_{a,b}J_{a,b},\qquad
 J_{a,b}=\gcd(a!,D'C_a+K').}
\tag{6}
$$



Thus $g$ is the content visible in the local future-digit block, while
$J$ is a separate residual divisor of the past factorial numerator.
This distinction is essential.  Uniformly over every admissible varying
order,



$$
\limsup_{a\to\infty}\frac{\log g_{a,b}}{\log W_{a,b}}\leq\frac12.
\tag{7}
$$



If $b/a\to\lambda\in[0,1]$, the sharper upper exponent is
$\lambda/(1+\lambda)$.  Consequently, using only the universal
finite-difference bound, local content alone cannot meet any fixed
Roth-strength exponent.  Even on the diagonal it reaches at most the
critical square-root exponent up to $W^{o(1)}$.  A Roth argument must
therefore obtain a positive power of $W$ from $J$, or prove a separate
exceptional upper bound for $|\Delta^b x_a|$.

No such theorem follows from the allowed digit ranges.  The exact modular
identities below show what would have to be controlled, while an adversarial
canonical-digit construction proves that range information alone cannot
control $J$.  These are rigorous barriers, not a proof that the route is
impossible for the specific digits of $\pi$.

## 2. Canonical digits and the target recurrence

For any real $y$, its terminating-convention canonical factorial digits
are



$$
d_n(y)=\lfloor n!y\rfloor-n\lfloor(n-1)!y\rfloor,\qquad
 0\leq d_n(y)\leq n-1.
\tag{8}
$$



For $y=\pi$, write $d_n=d_n(\pi)$ and set



$$
c_0=4,\qquad c_1=1,\qquad c_n=d_n+1\quad(n\geq2).
\tag{9}
$$



Then



$$
s=\sum_{n=0}^{\infty}\frac{c_n}{n!},\qquad
 C_n=n!\sum_{k=0}^n\frac{c_k}{k!},
\tag{10}
$$



and hence



$$
C_{n+1}=(n+1)C_n+c_{n+1},\qquad
 x_{n+1}=(n+1)x_n-c_{n+1}.
\tag{11}
$$



The digit bounds give $1\leq c_m\leq m$ for $m\geq2$.  The exact
tail formula



$$
x_n=\sum_{m>n}c_m\frac{n!}{m!}
\tag{12}
$$



therefore implies the useful strict interval



$$
\frac1{n+1}<x_n<1+\frac1n\qquad(n\geq1).
\tag{13}
$$



For the lower bound, keep only the first positive tail term.  For the
upper bound, replace $c_m$ by $m$:



$$
\sum_{m>n}m\frac{n!}{m!}
 =n!\sum_{k\geq n}\frac1{k!}<1+\frac1n.
\tag{14}
$$



## 3. Exact local-digit decomposition

Iteration of (11) gives, for $r\geq0$,



$$
C_{a+r}=\frac{(a+r)!}{a!}C_a
 +\sum_{j=1}^r\frac{(a+r)!}{(a+j)!}c_{a+j}.
\tag{15}
$$



Taking the $b$-th forward difference yields (4), with



$$
D_{a,b}
 =\sum_{r=0}^b(-1)^{b-r}\binom br\frac{(a+r)!}{a!},
\tag{16}
$$



and



$$
K_{a,b}=\sum_{j=1}^bE_{a,b,j}c_{a+j},
\tag{17}
$$



where



$$
\begin{aligned}
 E_{a,b,j}
 &=\sum_{r=j}^b(-1)^{b-r}\binom br
     \frac{(a+r)!}{(a+j)!}\\
 &=\frac{b!a!}{(a+j)!}
   \sum_{t=0}^{b-j}\frac{(-1)^t}{t!}
      \binom{a+b-t}{a}.
\end{aligned}
\tag{18}
$$



In each alternating sum in (18), the positive term magnitudes strictly
decrease.  Therefore



$$
E_{a,b,j}>0,\qquad E_{a,b,b}=1,
\tag{19}
$$



and $K_{a,b}>0$ for $b\geq1$.  The same calculation gives



$$
D_{a,0}=1,\qquad D_{a,1}=a,\qquad
 D_{a,b}=(a+b-1)D_{a,b-1}+(b-1)D_{a,b-2}.
\tag{20}
$$



Finally, substituting $x_a=a!s-C_a$ into (4) gives the exact cancellation
identity



$$
\boxed{\Delta^b x_a=D_{a,b}x_a-K_{a,b}.}
\tag{21}
$$



Thus numerical smallness of a finite difference is closeness of
$D_{a,b}x_a$ to the specific local-digit integer $K_{a,b}$; it is not
automatically explained by endpoint gcd.

## 4. Sharp factorial scale of $W_{a,b}$

Let



$$
R_{a,b}=\frac{(a+b)!}{a!},\qquad
 S_{a,b}=\frac{D_{a,b}}{R_{a,b}}.
\tag{22}
$$



Changing variables $t=b-r$ in (16) gives



$$
S_{a,b}=\sum_{t=0}^b\frac{(-1)^t}{t!}
 \prod_{q=0}^{t-1}\frac{b-q}{a+b-q}.
\tag{23}
$$



The terms again decrease.  For $b\geq1$, alternating-series bounds give



$$
\frac{a}{a+b}\leq S_{a,b}<1,
\tag{24}
$$



where the lower equality occurs at $b=1$.  Keeping the next term gives
the exact refinement



$$
0\leq S_{a,b}-\frac{a}{a+b}
 \leq\frac{b(b-1)}{2(a+b)(a+b-1)}.
\tag{25}
$$



Consequently



$$
\frac{a}{a+b}(a+b)!\leq W_{a,b}<(a+b)!
 \qquad(b\geq1).
\tag{26}
$$



In particular, if $b=o(a)$, then uniformly



$$
S_{a,b}=1-\frac{b}{a+b}+O\!\left(\frac{b^2}{a^2}\right),
 \qquad
 W_{a,b}=(a+b)!S_{a,b}.
\tag{27}
$$



There is also an exact proportional-ray limit.  If
$b/a\to\lambda\in[0,1]$, then each fixed product in (23) tends to
$(\lambda/(1+\lambda))^t$.  It is dominated by
$(b/(a+b))^t/t!$, so dominated convergence proves



$$
S_{a,b}\longrightarrow
 \exp\!\left(-\frac{\lambda}{1+\lambda}\right).
\tag{28}
$$



Therefore Stirling's formula gives



$$
\frac{\log D_{a,b}}{\log W_{a,b}}\longrightarrow
 \frac{\lambda}{1+\lambda}.
\tag{29}
$$



In the near-diagonal regimes, for each fixed admissible offset,



$$
\begin{aligned}
 b=a-h &: \quad W_{a,b}\sim e^{-1/2}(2a-h)!,\\
 b=a &: \quad W_{a,a}\sim e^{-1/2}(2a)!,\\
 b=a+1 &: \quad W_{a,a+1}\sim e^{-1/2}(2a+1)!.
\end{aligned}
\tag{30}
$$



The last line is the only fixed positive offset beyond the diagonal allowed
by $b\leq a+1$.

## 5. Exact gcd factorization and the Roth calibration

Let $g,D',K'$ be as in (5).  From (4),



$$
\begin{aligned}
 H_{a,b}
 &=\gcd(a!gD',g(D'C_a+K'))\\
 &=g\,\gcd(a!D',D'C_a+K').
\end{aligned}
\tag{31}
$$



Because $\gcd(D',K')=1$, one has
$\gcd(D',D'C_a+K')=1$.  This proves (6), and also



$$
J_{a,b}\mid a!,\qquad \gcd(J_{a,b},D')=1.
\tag{32}
$$



The reduced rational approximant has denominator $Q=W/H$ and error



$$
\left|s-\frac{Z/H}{W/H}\right|
 =\frac{|\Delta^b x_a|}{W}.
\tag{33}
$$



For $b\geq1$, all $x_a,\ldots,x_{a+b}$ lie in the interval
$(1/(a+b+1),1+1/a)$.  The positive and negative coefficient masses in
a $b$-th difference are both $2^{b-1}$.  Hence (13) improves the
digit-free bound to



$$
|\Delta^b x_a|<2^{b-1}
 \left(1+\frac1a-\frac1{a+b+1}\right).
\tag{34}
$$



For a fixed $\varepsilon>0$, the exact Roth-strength condition is



$$
|\Delta^b x_a|W^{1+\varepsilon}<H^{2+\varepsilon}.
\tag{35}
$$



Using (34) supplies a sufficient condition by replacing the first factor
with its displayed upper bound.  An application of Roth's theorem would
also have to prove that the reduced denominators $Q=W/H$ are unbounded
and yield infinitely many distinct approximants.

The local factor cannot by itself force that sufficient condition.  Indeed,
$g\leq D$, and for every admissible sequence



$$
\frac{\log D}{\log W}
 =\frac{\log D}{\log(a!)+\log D}
 \leq
 \frac{\log((2a+1)!/a!)}{\log(2a+1)!}
 =\frac12+o(1).
\tag{36}
$$



Also $b\log2=o(\log W)$, uniformly for $b\leq a+1$.  Therefore, if
$\log J=o(\log W)$, the digit-free sufficient condition in (35) fails
eventually for every fixed $\varepsilon>0$.  More precisely, when
$b/a\to\lambda$, that route requires



$$
\limsup\frac{\log J}{\log W}\geq
 \frac{1+\varepsilon}{2+\varepsilon}
 -\frac{\lambda}{1+\lambda},
\tag{37}
$$



whenever the right side is positive.  On the diagonal this lower exponent
is $\varepsilon/(2(2+\varepsilon))$; for $b=o(a)$, it is the full
$(1+\varepsilon)/(2+\varepsilon)$.  A separately proved exceptional
upper bound for $|\Delta^b x_a|$ could change this calibration, and no
such bound is ruled out here.

## 6. Modular identities and near-diagonal cases

Let $!m$ denote the number of derangements of $m$ objects, with
$!0=1$, $!1=0$.  Reducing (16) modulo $a$ gives



$$
\boxed{D_{a,b}\equiv !b\pmod a.}
\tag{38}
$$



Similarly, reducing (18) gives



$$
E_{a,b,j}\equiv\binom bj\,!(b-j)\pmod a,
\tag{39}
$$



and therefore



$$
\boxed{K_{a,b}\equiv
 \sum_{j=1}^b\binom bj\,!(b-j)c_{a+j}\pmod a.}
\tag{40}
$$



The recurrence $!n=n\,!(n-1)+(-1)^n$ proves, for fixed $k\geq0$,



$$
!(a+k)\equiv(-1)^a!k\pmod a.
\tag{41}
$$



Combining (38) and (41) yields the two admissible nonnegative offsets:



$$
\gcd(a,D_{a,a})=1,
 \qquad a\mid D_{a,a+1}.
\tag{42}
$$



For a fixed subdiagonal offset $h\geq1$, the exact assertion is instead



$$
D_{a,a-h}\equiv !(a-h)\pmod a;
\tag{43}
$$



there is no bounded fixed residue analogous to (41).  These congruences do
not by themselves control $g$, because $K$ contains the actual future
digits.  Since $E_{a,b,b}=1$, no prime divisor of $D$ is a forced
coefficientwise divisor of every possible local digit block.

## 7. Why digit-range information cannot control $J$

The factor $J$ in (6) depends on the residue of $C_a$ modulo $a!$.
The allowed canonical-digit ranges impose no useful restriction on that
residue.  To see this rigorously, replace $\pi$ temporarily by an
arbitrary $y\in[3,4)$.  The integer



$$
P_a=\lfloor a!y\rfloor
\tag{44}
$$



can be any of the $a!$ consecutive integers from $3a!$ through
$4a!-1$.  Thus $C_a=\lfloor a!e\rfloor+P_a$ runs through every
residue class modulo $a!$.  After fixing $P_a$, every finite allowed
future digit block may still be chosen arbitrarily: append that block and
then, for example, an all-zero tail.  This avoids the unique
terminating/maximal-tail ambiguity.

In particular, if $M\mid a!$ and $\gcd(M,D')=1$, one can choose
$C_a$ so that



$$
D'C_a+K'\equiv0\pmod M,
\tag{45}
$$



forcing $M\mid J$.  Other choices avoid any prescribed residue.  This
does not describe the fixed digits of $\pi$; it proves that a theorem
about $J$ must use arithmetic information beyond the inequalities
$0\leq d_n\leq n-1$.

Even transcendence of the source number alone is insufficient.  Choose a
rational $q$ with $e+3<q<e+4$ and put $y=q-e$.  Then
$3<y<4$, the number $y$ is transcendental, all of its canonical
factorial digits obey (8), but $e+y=q$ is rational.  Its sequence
$x_n$ is eventually equal to one, so every varying-order difference
with $b\geq1$ is eventually zero.

For the actual target this gives the exact logical dichotomy:



$$
\begin{array}{ll}
 s\notin\mathbb Q &: \Delta^b x_a\ne0
   \text{ for every admissible }(a,b),\\
 s\in\mathbb Q &: \Delta^b x_a=0
   \text{ for all sufficiently large }a\text{ and every }b\geq1.
\end{array}
\tag{46}
$$



The first line follows because one zero makes $s=Z/W$ rational.  The
second follows because $x_n=1$ once the denominator of $s$ divides
$n!$.  Thus any all-degree nonvanishing or positive lower-bound theorem
already contains at least the irrationality problem for $e+\pi$.

## 8. Minimal exponential type of the entire interpolant

There is also a clean analytic limitation.  If



$$
F(z)=\sum_{n\geq0}a_n\frac{z^n}{n!},\qquad a_n\in\mathbb Z,
\tag{47}
$$



is nonpolynomial and entire of exponential type, then its type is at least
one.  Indeed, infinitely many $|a_n|\geq1$, and Cauchy's estimate at
radius $n$ gives



$$
M_F(n)\geq\frac{n^n}{n!}=\exp(n+O(\log n)).
\tag{48}
$$



For the canonical interpolant



$$
G(z)=3+\sum_{n\geq2}d_n\frac{z^n}{n!},
\tag{49}
$$



the bound $d_n\leq n-1$ gives $M_G(r)\leq3+re^r$, so its type is at
most one.  Since $\pi$ is irrational, $G$ is not a polynomial.
Therefore its exponential type is exactly one.  The integral-Hurwitz
interpolant cannot be replaced, within this coefficient class, by a
nonpolynomial entire function of smaller exponential type.

## 9. Exact finite certificate

The companion program certifies all factorial floors with rational Machin
and exponential-tail intervals, then checks every admissible pair with



$$
a+b\leq530,\qquad a\geq\max(1,b-1).
\tag{50}
$$



There are exactly $71{,}019$ such pairs.  On every one, the program
independently verifies (4), (6), (24)--(25), and the modular identities
(38) and (40).  Directed rational intervals exclude zero at all
$71{,}019$ endpoints: $35{,}716$ are positive and $35{,}303$ are
negative.  This is a finite certificate, not an all-degree nonvanishing
theorem.

Two square-root tests are also exact throughout the triangle.  There is no
case satisfying



$$
H_{a,b}^2>2^{b+1}W_{a,b},
\tag{51}
$$



and no positive-$b$ case satisfying the stronger test obtained from
(34),



$$
H_{a,b}^2>
 2^{b-1}\left(1+\frac1a-\frac1{a+b+1}\right)W_{a,b}.
\tag{52}
$$



The maximum ratios in these two exact finite comparisons are respectively
$1/2$ at $(a,b)=(1,0)$ and $3/5$ at $(1,1)$.  Thus neither test
comes close to producing a large-degree subsequence in this range.

The largest computed value of $\log H/\log W$ is
$0.4520559724\ldots$ at $(8,2)$.  The largest computed actual
approximation exponent is



$$
\mu_{a,b}=
 \frac{-\log|s-(Z/H)/(W/H)|}{\log(W/H)}
\tag{53}
$$



with value $2.2962701804\ldots$ at $(5,1)$; the next is
$2.0530478558\ldots$ at $(8,2)$.  These logarithmic orderings are
diagnostic floating renderings.  The underlying $W,Z,H,g,J$ are exact,
and the displayed endpoint sizes have directed rational certificates.

The factor split and cancellation size are visible in representative
records:

| $(a,b)$ | $H$ | $g$ | $J$ | $|\Delta^b x_a|$ | $|L_{a,b}|$ |
|---:|---:|---:|---:|---:|---:|
| $(5,1)$ | 12 | 1 | 12 | $0.07531077070$ | $0.006275897558$ |
| $(8,2)$ | 840 | 1 | 840 | $0.1554832692$ | $1.850991300\times10^{-4}$ |
| $(346,3)$ | 2,875,602,586,336 | 8 | 359,450,323,292 | $0.08461987202$ | $2.942683124\times10^{-14}$ |
| $(100,100)$ | 65 | 1 | 65 | $9.788710496\times10^{28}$ | $1.505955461\times10^{27}$ |
| $(200,200)$ | 1 | 1 | 1 | $1.203055913\times10^{59}$ | $1.203055913\times10^{59}$ |
| $(264,265)$ | 341,475 | 3 | 113,825 | $4.124593609\times10^{78}$ | $1.207875718\times10^{73}$ |
| $(265,265)$ | 94 | 1 | 94 | $3.896271754\times10^{78}$ | $4.144969951\times10^{76}$ |

In particular, the small primitive values at $(8,2)$ and $(346,3)$
come predominantly from $J$, not from the local factor $g$ or an
exceptionally small finite difference.  The sampled near-diagonal finite
differences are instead enormous.  Neither observation is extrapolated
beyond the certified triangle.

Frozen companion artifacts:

* `scripts/factorial_digit_entire_varying_b_probe.py`, SHA-256
  `003ed11dea46976e31c07e7eacac47c5c8b72c4eb802b45e768165fbb7955cac`;
* `results/factorial_digit_entire_varying_b_total530.json`.

The JSON embeds the exact source and script hashes.  Its own hash is
reported alongside the frozen snapshot; it is intentionally not inserted
here, which would create a circular source/result hash dependency.

The exact identities, asymptotics, gcd factorization, modular congruences,
Roth calibration, adversarial digit-range barrier, and type-one statement
in Sections 2--8 are all-degree theorems.  Finite nonvanishing, rankings,
and gcd sizes in the JSON result are diagnostics and prove nothing about
the tail of the specific digit sequence of $\pi$.
