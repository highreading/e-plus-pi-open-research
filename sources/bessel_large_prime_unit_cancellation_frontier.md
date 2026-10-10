> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Large primes in the Bessel denominator: a unit-cancellation frontier

Checked: 2026-08-27 UTC.

## 1. Verdict

Let



$$
q_0=q_1=1,
 \qquad q_n=(4n-2)q_{n-1}+q_{n-2}\quad(n\geq2).
\tag{1}
$$



This note isolates the range of odd primes $p>2n$, and more generally
$p>n/2$, in the unresolved valuation problem for $q_n$.

There is one unconditional bound:



$$
\boxed{p>2n\quad\Longrightarrow\quad v_p(q_n)\leq n-1.}
\tag{2}
$$



It is uniform and elementary, but it is not on the needed scale.  Since
$\log p\asymp\log n$ at the lower edge $p>2n$, the desired estimate



$$
v_p(q_n)\log p=o(n\log n)
\tag{3}
$$



requires $v_p(q_n)=o(n)$, whereas (2) remains linear.

The standard structural inputs do not improve (2).

1. In the terminating factorial formula, every summand is a $p$-adic
   unit when $p>2n$.  Divisibility is therefore pure cancellation;
   every termwise minimum-valuation argument gives only zero.
2. The exponential-Padé Wronskian proves that the polynomial-argument
   root at $x=1$ is simple, but simple Hensel roots can have arbitrary
   distance exponent.  In the present family the Wronskian restates the
   depth exactly and supplies no upper bound.
3. The boundary subfamily

   

$$
p=2n+1
   \tag{4}
$$



   already lies in $p>2n$.  Here reflection forces the index slope to
   vanish whenever $p\mid q_n$.  Thus ordinary index-Hensel simplicity
   is unavailable precisely at this large-prime boundary.

For (4) there is an exact all-power cancellation tower.  Put
$m=(p-1)/2$.  Define



$$
c_j=\frac{(1/2)_j^2}{j!},
 \qquad
 S_{m,\ell}
 =\sum_{j=\ell}^{m}c_j\,
 e_\ell\left(1,\frac1{3^2},\ldots,
                    \frac1{(2j-1)^2}\right),
\tag{5}
$$



where $e_\ell$ is the elementary symmetric polynomial and the empty
alphabet for $j=0$ has $e_0=1$.  Every denominator in (5) is prime
to $p$, and



$$
\boxed{
 (-1)^m q_m
 =\sum_{\ell=0}^{m}(-p^2)^\ell S_{m,\ell}.}
\tag{6}
$$



Consequently, for every $A\geq1$,



$$
\boxed{
 v_p(q_m)\geq A
 \iff
 \sum_{\ell=0}^{\min\{m,\lfloor(A-1)/2\rfloor\}}
       (-p^2)^\ell S_{m,\ell}
 \equiv0\pmod {p^A}.}
\tag{7}
$$



For $A=1,2$, condition (7) is the familiar truncated
${}_2F_0$ congruence $S_{m,0}\equiv0\pmod {p^A}$.  Higher depth
introduces a new symmetric harmonic layer every two powers.  Formula
(7) is exact, but no nonvanishing law for this tower is proved here.

Thus a uniform large-prime theorem cannot be obtained merely by declaring
the factorial terms to be units, invoking the Padé Wronskian, or using
first-order shift/reflection congruences.  It must control cancellation in
the special Bessel sum, including the central tower (7).  This is a
sharply scoped no-go, not a proof that such a cancellation theorem is
impossible.

The broader range $n/2<p$ is not even squarefree in general:



$$
q_8=312129649=13^2\cdot1846921,
 \qquad v_{13}(q_8)=2,
\tag{8}
$$



and $13>8/2$.  Hence any proposed uniform exponent-one statement for
the range in the task is false.

No little-oh valuation bound, irrationality result, or statement about
$e+\pi$ is proved.

## 2. The elementary large-prime exponent bound

For $n=1$, conclusion (2) is immediate from $q_1=1$.  Hence assume
$n\geq2$.  Positivity in (1) gives



$$
q_n<4nq_{n-1}<\prod_{j=2}^{n}4j=4^{n-1}n!.
\tag{9}
$$



By arithmetic--geometric mean applied to $1,\ldots,n$,



$$
n!\leq\left(\frac{n+1}{2}\right)^n.
\tag{10}
$$



Therefore



$$
q_n<4^{n-1}\left(\frac{n+1}{2}\right)^n
     =\frac{(2n+2)^n}{4}<(2n+1)^n.
\tag{11}
$$



Indeed, the ratio in the last inequality is
$(1+1/(2n+1))^n/4<e^{1/2}/4<1$.

If $p>2n$, then $p\geq2n+1$.  If
$a=v_p(q_n)$, equations (11) and $p^a\leq q_n$ give $a<n$,
which proves (2).

Stirling's formula makes the remaining scale gap explicit:



$$
\log q_n\leq n\log n+(\log4-1)n+O(\log n).
\tag{12}
$$



At $p=2n+O(1)$, the quotient of (12) by $\log p$ is



$$
n-(1-\log2)\frac n{\log n}
 +O\left(\frac n{(\log n)^2}\right).
\tag{13}
$$



So even the sharpened archimedean estimate is $n-o(n)$, not
$o(n)$.

For comparison, if only $p>n/2$ is assumed, (9) gives uniformly



$$
v_p(q_n)
 \leq\frac{n\log n+O(n)}{\log(n/2)}
 =n+O\left(\frac n{\log n}\right).
\tag{14}
$$



Again this is linear.

## 3. Every terminating term is a unit

The exact terminating formula is



$$
(-1)^nq_n
 =\sum_{k=0}^{n}(-1)^k
   \frac{(n+k)!}{k!(n-k)!}.
\tag{15}
$$



If $p>2n$, all factorial arguments in (15) are strictly below $p$.
Hence



$$
v_p\left(\frac{(n+k)!}{k!(n-k)!}\right)=0
 \qquad(0\leq k\leq n).
\tag{16}
$$



The same observation applies to every nonzero coefficient in the displayed
factorial normalization of the Padé
denominator



$$
Q_n(x)=\sum_{k=0}^{n}(-1)^k
 \frac{(2n-k)!}{k!(n-k)!}x^k:
\tag{17}
$$



all coefficients are $p$-adic units.  Thus neither factorial
divisibility nor a Newton-polygon lower edge singles out the high order of
$Q_n(1)$.  It comes only from cancellation among unit coefficients at
$x=1$.

This statement is deliberately limited to termwise methods.  A new
identity controlling the cancellation among the terms of (15) could
still prove (3).

## 4. What the Padé Wronskian says—and does not say

Let $P_n(x)=Q_n(-x)$.  The diagonal Padé identity gives the exact
Wronskian



$$
P_n'(x)Q_n(x)-P_n(x)Q_n'(x)-P_n(x)Q_n(x)
 =(-1)^{n+1}x^{2n}.
\tag{18}
$$



At $x=1$, reduction modulo $q_n=Q_n(1)$ gives



$$
P_n(1)Q_n'(1)\equiv(-1)^n\pmod {q_n}.
\tag{19}
$$



Thus for every prime divisor $p\mid q_n$, both factors on the left of
(19) are $p$-adic units.  If $a=v_p(q_n)$, the unique root
$\xi_{n,p}$ of $Q_n$ in $1+p\mathbb Z_p$ satisfies



$$
\boxed{v_p(1-\xi_{n,p})=a.}
\tag{20}
$$



Equation (20) records the valuation but does not bound it.  This is an
intrinsic limitation of the *local consequence* (19): for arbitrary
$A\geq1$, the integral polynomial



$$
\widetilde Q_A(x)=x-1+p^A
\tag{21}
$$



has $\widetilde Q_A(1)=p^A$, unit derivative, and a simple root at
distance exactly $p^{-A}$ from $1$.  The comparison (21) is not a
Bessel polynomial; it proves only that simplicity and the unit inverse in
(19), by themselves, cannot imply an exponent bound.

## 5. Exact central cancellation tower

Let $p=2m+1$ be prime.  In the $j$-th term of (15), pair the factors
around the center:



$$
(m+t)(m+1-t)=\frac{p^2-(2t-1)^2}{4}
 \qquad(1\leq t\leq j).
\tag{22}
$$



This gives the exact identity



$$
\frac{(m+j)!}{j!(m-j)!}
 =\frac1{4^jj!}
   \prod_{t=1}^{j}\bigl(p^2-(2t-1)^2\bigr).
\tag{23}
$$



After the alternating sign in (15) is included,



$$
\begin{aligned}
 (-1)^m q_m
 &=\sum_{j=0}^{m}
   \frac1{4^jj!}
   \prod_{t=1}^{j}\bigl((2t-1)^2-p^2\bigr)\\
 &=\sum_{j=0}^{m}c_j
   \prod_{t=1}^{j}
   \left(1-\frac{p^2}{(2t-1)^2}\right).
\end{aligned}
\tag{24}
$$



Expand the last product by elementary symmetric polynomials and interchange
the two finite sums.  This proves (6).  Because
$1,3,\ldots,2m-1$, $j!$, and the powers of $2$ are all prime to
$p$, every $S_{m,\ell}$ belongs to the localization
$\mathbb Z_{(p)}$.

Modulo $p^A$, every term in (6) with $2\ell\geq A$ vanishes.
Deleting exactly those terms proves (7).

At a central root, reflection of the canonical interpolation about
$-1/2$ forces the index derivative, and hence the first index slope,
to vanish modulo $p$.  Thus the first lift either dies or admits all
$p$ children.  Formula (7) identifies the arithmetic decision at every
subsequent precision; reflection itself makes none of those decisions.

This last limitation also has a clean comparison family.  For every
$A\geq1$,



$$
H_A(x)=(2x+1)^{2A}
\tag{25}
$$



is an integral, reflection-symmetric, $1$-Lipschitz function on
$\mathbb Z_p$, and at $m=(p-1)/2$,



$$
H_A(m)=p^{2A}.
\tag{26}
$$



It also has zero derivative at the fixed point $-1/2$.  Therefore
reflection, local analyticity, central slope vanishing, and ordinary
shift-Lipschitz congruences are collectively compatible with arbitrarily
large central valuation.  The polynomials (25) do not satisfy the Bessel
difference equation; the conclusion is precisely that these general
structural properties, without the special cancellation arithmetic of
(24), cannot prove (3).

## 6. Scope and certificate

The proved positive result is (2), and the exact Bessel reduction is
(6)--(7).  The no-go statements have the following strict scope.

- Equation (16) rules out only termwise factorial-valuation bounds.
- Equation (21) rules out only a bound deduced from argument-root
  simplicity and the unit Wronskian congruence alone.
- Equations (25)--(26) rule out only a bound deduced from reflection,
  analyticity, central slope, and shift-Lipschitz structure alone.

None of these comparisons rules out a theorem exploiting new cancellation
inside (15) or (24).  That cancellation is the exact surviving large-prime
problem.

The companion script

    scripts/bessel_large_prime_unit_cancellation_frontier_certificate.py

checks with exact integer and rational arithmetic:

1. (9)--(11), the term-unit statement (16), and the coefficient-unit
   statement following (17) on finite grids;
2. the Padé Wronskian (18) in bounded degrees;
3. the exact central identities (23)--(24), the symmetric expansion (6),
   and the truncated congruence criterion (7);
4. the counterexample (8); and
5. the comparison families (21) and (25)--(26).

The finite checks are regression tests.  The all-parameter proofs are
Sections 2--5.
