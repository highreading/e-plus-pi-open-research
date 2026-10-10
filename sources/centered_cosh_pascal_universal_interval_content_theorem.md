> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The universal prime interval in the centered-cosh Pascal content

## An Euler-periodicity and Lucas reduction theorem

Checked: 2026-08-27 UTC

## 1. Statement

Put



$$
H(y)=\sec\sqrt y
     =\sum_{n\geq0}U_n\frac{y^n}{(2n)!},
 \qquad
 H(y)^2=\sum_{n\geq0}T_n\frac{y^n}{(2n)!}.
                                                        \tag{1}
$$



Thus $U_n=|E_{2n}|$, and



$$
T_n=\sum_{a=0}^n\binom{2n}{2a}U_aU_{n-a}.              \tag{2}
$$



For $q\geq1$, let $d=(d_0,\ldots,d_q)$ be the positive
primitive kernel vector of the signed even-Pascal matrix



$$
\sum_{i=0}^q(-1)^i\binom{2(q+r)}{2i}d_i=0
 \qquad(1\leq r\leq q),                                 \tag{3}
$$



and put



$$
e_k=\sum_{i=0}^k(-1)^{k-i}\binom{2k}{2i}d_i.           \tag{4}
$$



Define



$$
\begin{split}
 w_m={}&2\sum_{i=0}^q\binom{2m}{2i}d_iU_{m-i}\\
 &-\sum_{k=0}^q\binom{2m}{2k}e_kT_{m-k},                \tag{5}\\
 G_q={}&\gcd\bigl((8q+2)(8q+1)w_{4q},\,w_{4q+1}\bigr). \tag{6}
 \end{split}
$$



The convention is that a binomial coefficient is zero when its lower
index exceeds its upper index.  The content (6) is exactly
$G_q^{\rm Pascal}$ in the normalization theorem.

Then every prime in the upper half of the endpoint factorial range is
a forced divisor:



$$
\boxed{
   \prod_{\substack{\ell\ \text{prime}\\4q<\ell\leq8q+2}}\ell
   \ \mid\ G_q.}                                       \tag{7}
$$



The product in (7) is squarefree.  The theorem asserts one forced copy
of each prime; it does not assert that the displayed primes occur with
valuation exactly one.

In particular, when studying the conjectural support and lcm-square
bound for $G_q$, the quotient



$$
G_q^{\rm exc}:=
 \frac{G_q}{\displaystyle
   \prod_{4q<\ell\leq8q+2,\ \ell\ \text{prime}}\ell}   \tag{8}
$$



is an integer.  It is the appropriate exceptional-content quotient.

## 2. Two Euler congruences

Let $\ell$ be an odd prime, and put



$$
h=\frac{\ell-1}{2},\qquad \chi=(-1)^h.                 \tag{9}
$$



The congruences needed below are



$$
\boxed{
 \begin{aligned}
 U_{n+h}&\equiv\chi U_n\pmod\ell &&(n\geq1),\\
 U_h&\equiv\chi-1\pmod\ell,\\
 T_{n+h}&\equiv\chi T_n\pmod\ell &&(n\geq0).
 \end{aligned}}                                         \tag{10}
$$



We include the proof because the exceptional value at $n=0$ in the
first line is important.

Let the Euler polynomials be normalized by



$$
\frac{2e^{xt}}{e^t+1}
 =\sum_{n\geq0}E_n(x)\frac{t^n}{n!}.                    \tag{11}
$$



The finite geometric sum gives



$$
\sum_{a=0}^{\ell-1}(-1)^a(x+a)^n
 =\frac{E_n(x)+E_n(x+\ell)}2
 \equiv E_n(x)\pmod\ell.                               \tag{12}
$$



At $x=1/2$, using



$$
2^{2n}E_{2n}(1/2)=(-1)^nU_n,
$$



equation (12) becomes



$$
(-1)^nU_n\equiv
 \sum_{a=0}^{\ell-1}(-1)^a(2a+1)^{2n}\pmod\ell.        \tag{13}
$$



For $n\geq1$, Fermat's theorem may be applied termwise; the unique
zero base $2a+1\equiv0\pmod\ell$ contributes zero before and after
the shift.  This proves the first line of (10).  At $n=0$, that one
base contributes $(-1)^h=\chi$ before the shift but zero after it.
Since $\sum_{a=0}^{\ell-1}(-1)^a=1$, equation (13) gives
$U_h\equiv\chi-1$.

The tangent-number identity



$$
T_n=(-1)^{n+1}2^{2n+1}E_{2n+1}(0)                     \tag{14}
$$



and (12) at $x=0$ give



$$
T_n\equiv(-1)^{n+1}2^{2n+1}
 \sum_{a=0}^{\ell-1}(-1)^aa^{2n+1}\pmod\ell.           \tag{15}
$$



Here the zero base contributes zero for every $n\geq0$.  Shifting
$n$ by $h$, Fermat's theorem and $2^{\ell-1}\equiv1$ therefore
multiply the right side by exactly $(-1)^h=\chi$.  This proves the
last line of (10).

## 3. The reduced border is a Padé error coefficient

Introduce the factorial-basis Padé pair



$$
p(y)=\sum_{i=0}^q d_i\frac{y^i}{(2i)!},
 \qquad
 B(y)=\sum_{k=0}^q e_k\frac{y^k}{(2k)!}.                \tag{16}
$$



The Pascal equations (3) and the transform (4) give the standard
Padé-order identity



$$
E(y):=B(y)H(y)-p(y)=O(y^{2q+1}).                        \tag{17}
$$



For $r\geq1$, define the odd-top border



$$
J_r=
 2\sum_{i=0}^q\binom{2r-1}{2i}d_iU_{r-i}
 -\sum_{k=0}^q\binom{2r-1}{2k}e_kT_{r-k}.               \tag{18}
$$



Because



$$
\binom{2r-1}{2i}
 =\frac{r-i}{r}\binom{2r}{2i},                          \tag{19}
$$



differentiating (1) in the divided-power basis gives



$$
\begin{split}
 rJ_r
  &=(2r)![y^r]\bigl(2p\,yH'-B\,y(H^2)'\bigr)\\
  &=(2r)![y^r]\,2(p-BH)yH'\\
  &=-(2r)![y^r]\,2E(y)yH'(y).                           \tag{20}
 \end{split}
$$



Since $yH'(y)=O(y)$, (17) and (20) imply the slightly stronger
vanishing range



$$
\boxed{J_r=0\qquad(1\leq r\leq2q+1).}                 \tag{21}
$$



Only $r\leq2q$ is needed below.

## 4. Lucas reduction of the odd endpoint

Fix a prime $\ell$ with



$$
4q+1<\ell\leq8q+2.              \tag{22}
$$



The upper endpoint $8q+2$ is even, so in fact $\ell\leq8q+1$.
Write



$$
8q+2=\ell+s,\qquad s=2r-1.                              \tag{23}
$$



Then $1\leq r\leq2q$.  Since $2i<\ell$, Lucas's theorem gives



$$
\binom{8q+2}{2i}\equiv\binom{2r-1}{2i}\pmod\ell.      \tag{24}
$$



The right side is zero unless $i\leq r-1$.  In that range,



$$
4q+1-i=h+(r-i),\qquad r-i\geq1.                         \tag{25}
$$



Applying (10) to every surviving term in (5), and doing the same for
the $T$-sum, gives



$$
w_{4q+1}\equiv\chi J_r\equiv0\pmod\ell.               \tag{26}
$$



There is one midpoint case not covered by (23): suppose
$\ell=4q+1$ is prime.  Lucas's theorem applied to the base-$\ell$
digits of $2\ell$ gives



$$
\binom{2\ell}{2i}\equiv0\pmod\ell\quad(1\leq i\leq q).
                                                                    \tag{27}
$$



Also $\ell=1+2h$.  Applying (10) twice from $n=1$ yields



$$
U_\ell\equiv U_1=1,
 \qquad T_\ell\equiv T_1=2\pmod\ell.                  \tag{28}
$$



As $e_0=d_0$, equations (5), (27), and (28) give



$$
w_{4q+1}\equiv2d_0U_\ell-e_0T_\ell=0\pmod\ell.       \tag{29}
$$



Thus every prime in (7) divides the odd endpoint coordinate.

## 5. Lucas reduction of the even endpoint

Now let



$$
4q<\ell\leq8q.                  \tag{30}
$$



Write



$$
8q=\ell+s,\qquad s=2r-1.                                \tag{31}
$$



Again $1\leq r\leq2q$, and the same Lucas calculation gives



$$
\binom{8q}{2i}\equiv\binom{2r-1}{2i}\pmod\ell,
 \qquad
 4q-i=h+(r-i).                                           \tag{32}
$$



Only $i\leq r-1$ survives.  Equations (10), (18), and (21) now
give



$$
w_{4q}\equiv\chi J_r=0\pmod\ell.\tag{33}
$$



The only possible prime in the interval (7) that is larger than
$8q$ is $\ell=8q+1$.  It divides the explicit prefactor
$(8q+2)(8q+1)$ in (6).  Combining this observation with
(26), (29), and (33) proves (7).

## 6. Scope and remaining arithmetic questions

The proof separates a universal squarefree layer from the endpoint
content.  It does **not** prove any of the following stronger claims:

1. that no prime $\ell>8q+2$ divides $G_q$;
2. that the valuation of a prime in (7) is at most two;
3. that $G_q\mid\operatorname {lcm}(1,\ldots,8q+2)^C$ for a fixed
   $C$;
4. a height conclusion or a classification of $e+\pi$.

The exact replay verifies the Euler congruences, the reduced-border
identity, every edge case, and (7) on a declared finite grid.  Those
checks are diagnostics for the symbolic proof, not extrapolations.

Companion files:

* `scripts/centered_cosh_pascal_universal_interval_content_certificate.py`;
* `results/centered_cosh_pascal_universal_interval_content_certificate.json`;
* `results/centered_cosh_pascal_universal_interval_content_hashes.sha256`.
