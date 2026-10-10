> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Factorial-ceiling recurrence: exact structure, a Roth obstruction, and no-go boundaries

Checked: 2026-08-26 UTC

## Scope and verdict

This note investigates the eventual ceiling recurrence introduced by Runlong
Yu,



$$
A_n(\pi)=\lceil n!\pi\rceil,\qquad
 A_{n+1}(\pi)=(n+1)A_n(\pi)-1.
$$



It does **not** prove that $e+\pi$ is algebraic or transcendental.  It gives
two rigorous additions to the audit:

1. a block version of the recurrence, combined with Roth's theorem, gives a
   genuine all-index restriction under the hypothesis that $e+\pi$ is
   algebraic irrational;
2. the complete set of real numbers having an eventual recurrence is a
   countable dense set consisting entirely of transcendental numbers.  In
   particular, generic distribution results, transcendence of $\pi$ by
   itself, and finite modular tests cannot rule out the recurrence.

The primary sources used are:

- R. Yu, *Tail Criteria, No-Go Audits, and Apéry-Type Certificate
  Obstructions for the Irrationality of $e+\pi$*, Theorems 3.1--3.4,
  [arXiv:2606.17303](https://arxiv.org/abs/2606.17303).
- K. F. Roth, *Rational approximations to algebraic numbers*,
  *Mathematika* **2** (1955), 1--20,
  [doi:10.1112/S0025579300000644](https://doi.org/10.1112/S0025579300000644).

## 1. Universal identities

The algebra is clearer if $\pi$ is initially replaced by an arbitrary real
number $x$.  Put



$$
E_n=\sum_{k=0}^n\frac1{k!},\qquad
 \rho_n=n!(e-E_n),\qquad
 B_n=n!E_n,
$$



and



$$
A_n(x)=\lceil n!x\rceil,\qquad
 \delta_n(x)=A_n(x)-n!x,\qquad
 C_n(x)=A_n(x)+B_n.
$$



For $n\geq1$, the elementary factorial tail estimate gives



$$
0<\rho_n<1,\qquad B_n=\lfloor n!e\rfloor,
 \qquad B_{n+1}=(n+1)B_n+1.                            \tag{1}
$$



Also $0\leq\delta_n(x)<1$, with strict positivity when $x$ is
irrational.  If



$$
s=e+x,
$$



then the following approximation is valid for every $n\geq1$:



$$
\frac{C_n(x)}{n!}-s
 =\frac{\delta_n(x)-\rho_n}{n!},
 \qquad
 \left|\frac{C_n(x)}{n!}-s\right|<\frac1{n!}.          \tag{2}
$$



For $n\geq1$, define the recurrence event at index $n$ by



$$
\mathcal R_n(x):\quad
 A_{n+1}(x)=(n+1)A_n(x)-1.                             \tag{3}
$$



Using (1), this is exactly



$$
\mathcal R_n(x)
 \quad\Longleftrightarrow\quad
 C_{n+1}(x)=(n+1)C_n(x)
 \quad\Longleftrightarrow\quad
 \frac{C_{n+1}(x)}{(n+1)!}=\frac{C_n(x)}{n!}.           \tag{4}
$$



Thus the recurrence says that two consecutive rational approximants in (2)
are literally the same rational number.  This observation is the basis of
the block theorem below.

## 2. Complete classification of eventual recurrence

### Theorem 1 (exceptional-set classification)

For a real number $x$, the following are equivalent:

1. $\mathcal R_n(x)$ holds for every sufficiently large $n$;
2. $e+x\in\mathbb Q$;
3. $x\in\mathbb Q-e$.

Consequently, the set of all real $x$ with an eventual recurrence is
$\mathbb Q-e$.  It is countable, dense, of Lebesgue measure zero and
Hausdorff dimension zero, and every one of its elements is transcendental.

#### Proof

If (3) holds for all $n\geq n_0$, (4) shows that



$$
\frac{C_n(x)}{n!}=\frac{C_{n_0}(x)}{n_0!}=:c\in\mathbb Q
 \qquad(n\geq n_0).
$$



Letting $n\to\infty$ in (2) gives $s=e+x=c$, so $s$ is rational.

Conversely, suppose $s=a/b\in\mathbb Q$, with $b>0$.  If $b\mid n!$,
then both $C_n(x)$ and $n!s$ are integers.  Equation (2), before division
by $n!$, gives



$$
C_n(x)-n!s=\delta_n(x)-\rho_n,
 \qquad |C_n(x)-n!s|<1.
$$



The integer on the left must therefore vanish.  Hence



$$
C_n(x)=n!s
$$



for every $n$ such that $b\mid n!$, and (4) holds from that point onward.
This proves the equivalence.

The description as $\mathbb Q-e$ makes countability and density immediate.
If $q-e$ were algebraic for some rational $q$, then
$e=q-(q-e)$ would be algebraic, a contradiction.  Thus every member of the
set is transcendental.  A countable subset of the line has measure and
Hausdorff dimension zero. $\square$

For $x=\pi$, Theorem 1 is Yu's ceiling-recurrence criterion.  The more
general formulation exposes an important limitation: **transcendence of
$\pi$ cannot itself be an obstruction**, because every real number with the
eventual recurrence is already transcendental.

If $s=a/b$ is in lowest terms, the proof also shows that the recurrence is
guaranteed once $b\mid n!$.  Therefore an exactly certified failure of
$\mathcal R_n(\pi)$ excludes rational denominators $b$ dividing $n!$,
but any finite set of failures still leaves infinitely many possible
denominators.

## 3. The modular criterion is pointwise equivalent, not independent

Suppose now that $x$ is irrational and let



$$
F_m(x)=\lfloor m!x\rfloor,
 \qquad
 d_m(x)=F_m(x)-mF_{m-1}(x).
$$



Then $0\leq d_m(x)\leq m-1$, and $A_m(x)=F_m(x)+1$.  Direct subtraction
gives



$$
C_m(x)-mC_{m-1}(x)=d_m(x)-(m-2).                     \tag{5}
$$



The right side lies in $[-(m-2),1]$.  Since this interval contains no
nonzero multiple of $m$, for every $m\geq2$ one has the exact chain



$$
\begin{aligned}
 \mathcal R_{m-1}(x)
 &\Longleftrightarrow d_m(x)=m-2\\
 &\Longleftrightarrow m\mid C_m(x)\\
 &\Longleftrightarrow A_m(x)\equiv-1\pmod m.           \tag{6}
 \end{aligned}
$$



The last equivalence uses $B_m=mB_{m-1}+1$, hence $B_m\equiv1\pmod m$.
Thus the tempting modular test



$$
\lceil m!\pi\rceil\equiv-1\pmod m
$$



is exactly the same event as the ceiling recurrence; it supplies no new
independent obstruction.

There is likewise no internal $p$-adic inconsistency.  If
$s=a/b\in\mathbb Q$ and $b\mid n!$, then



$$
C_n(x)=\frac{a}{b}n!.                                 \tag{7}
$$



For every fixed prime $p$, the $p$-adic valuation of the right side tends
to infinity with $n$ (apart from the harmless case $a=0$, where the value
is zero and its valuation is conventionally infinite).  The explicit
transcendental examples $x=a/b-e$ realize
all these congruences.  A successful $p$-adic argument would therefore
need genuinely new information specific to $\pi$; consequences of the
recurrence alone cannot contradict one another.

## 4. Finite-prefix universality

The next statement makes precise why no finite computation of factorial
digits, ceilings, or their residue classes can determine the algebraic class
of $e+\pi$.

### Theorem 2 (three-way finite-prefix compatibility)

Fix an irrational real number $x_0$ and an integer $K\geq1$.  There are
transcendental real numbers 

$$
x_{\mathrm{rat}},x_{\mathrm{alg}},
x_{\mathrm{tr}}
$$

 such that



$$
A_n(x_*)=A_n(x_0)\qquad(1\leq n\leq K)                \tag{8}
$$



for all three choices, while



$$
\begin{array}{c|c}
 x_* & e+x_*\\ \hline
 x_{\mathrm{rat}} & \text{rational},\\
 x_{\mathrm{alg}} & \text{algebraic irrational},\\
 x_{\mathrm{tr}} & \text{transcendental}.
 \end{array}                                           \tag{9}
$$



#### Proof

For each $n\leq K$, the irrationality of $x_0$ implies
$n!x_0\notin\mathbb Z$.  Hence the finitely many functions
$x\mapsto\lceil n!x\rceil$ are all locally constant at $x_0$.  There is
an open interval $I$ containing $x_0$ on which all the equalities in (8)
hold.

Choose a rational number $r\in e+I$, and set
$x_{\mathrm{rat}}=r-e$.  Then $x_{\mathrm{rat}}\in I$, its sum with
$e$ is rational, and it is transcendental because otherwise $e$ would be
algebraic.

Next choose an algebraic irrational $\alpha\in e+I$, and set
$x_{\mathrm{alg}}=\alpha-e$.  Again $x_{\mathrm{alg}}\in I$, and it is
transcendental: if it were algebraic, then $e=\alpha-x_{\mathrm{alg}}$
would be algebraic.

Finally choose a rational $q\in I-e$, and set
$x_{\mathrm{tr}}=e+q$.  This lies in $I$ and is transcendental.  Its sum
with $e$ is $2e+q$, which is also transcendental, since algebraicity of
$2e+q$ would imply algebraicity of $e$. $\square$

Applied with $x_0=\pi$, this theorem concerns only the **finite prefix
information** extracted from $\pi$; it does not replace $\pi$ in the
original problem and does not show that any of the three alternatives holds
for $e+\pi$.  It proves the narrower no-go statement that finite prefix
information alone cannot decide among them.

## 5. Recurrence blocks produce unusually strong rational approximations

The eventual criterion is all-or-nothing.  Finite but long blocks contain
more quantitative information.

### Lemma 3 (block approximation)

Let $1\leq u<v$, and suppose



$$
\mathcal R_n(x)\quad\text{holds for every }n=u,u+1,\ldots,v-1.  \tag{10}
$$



Then the single rational number



$$
c_{u,v}=\frac{C_u(x)}{u!}=\frac{C_v(x)}{v!}            \tag{11}
$$



has reduced denominator at most $u!$ and satisfies



$$
|(e+x)-c_{u,v}|<\frac1{v!}.                            \tag{12}
$$



#### Proof

Iterating (4) through precisely the indices in (10) gives (11).  Before
reduction, the first expression in (11) has denominator $u!$, so its
reduced denominator is at most $u!$.  Applying (2) at the endpoint $v$
gives (12). $\square$

The indexing matters: a block of recurrence events from $u$ through
$v-1$ freezes the approximants at the integer levels
$u,u+1,\ldots,v$, and the final error is $1/v!$, not $1/(v-1)!$.

### Theorem 4 (Roth obstruction to very long blocks)

Assume that $s=e+x$ is algebraic irrational.  For every $\varepsilon>0$,
there are only finitely many pairs $(u,v)$ satisfying (10) and



$$
v!>(u!)^{2+\varepsilon}.                               \tag{13}
$$



Consequently, for every infinite sequence of recurrence blocks with
$u_j\to\infty$,



$$
\limsup_{j\to\infty}
 \frac{\log(v_j!)}{\log(u_j!)}\leq2.                   \tag{14}
$$



In particular, for every $\eta>0$, only finitely many such blocks can
satisfy $v\geq(2+\eta)u$.

#### Proof

Write the rational in (11) in lowest terms as $c_{u,v}=p/q$.  Lemma 3
gives $q\leq u!$.  Under (13),



$$
\left|s-\frac pq\right|
 <\frac1{v!}
 <\frac1{(u!)^{2+\varepsilon}}
 \leq\frac1{q^{2+\varepsilon}}.                        \tag{15}
$$



Roth's theorem says that a fixed real algebraic irrational $s$ has only
finitely many reduced rational approximations satisfying (15).

For completeness, infinitely many qualifying blocks cannot evade Roth's
finiteness by repeatedly producing the same rational.  If a fixed rational
$c\ne s$ occurred for blocks with unbounded endpoints $v$, (12) would
force $|s-c|=0$, a contradiction.  Blocks with bounded $v$ give only
finitely many integer pairs $(u,v)$.  Thus an infinite family of qualifying
blocks would contain infinitely many distinct reduced rationals, contradicting
Roth's theorem.

Statement (14) is an immediate reformulation of the finiteness assertion for
each $\varepsilon>0$.  Finally, Stirling's formula shows that, uniformly for
$v\geq(2+\eta)u$ and sufficiently large $u$,



$$
\frac{\log(v!)}{\log(u!)}>2+\frac\eta2.
$$



Apply the first part with $\varepsilon=\eta/2$. $\square$

There is also an elementary degree-dependent form.  If $s$ is algebraic of
degree $d\geq2$, Liouville's polynomial argument supplies a constant
$K_s>0$ such that



$$
\left|s-\frac pq\right|\geq\frac{K_s}{q^d}             \tag{16}
$$



for every reduced rational $p/q$.  To see this directly, let
$P\in\mathbb Z[X]$ be the minimal polynomial of $s$.  The nonzero integer
$q^dP(p/q)$ has absolute value at least one; factor $P$ over $\mathbb C$
and bound all factors other than $p/q-s$ when $|p/q-s|<1$.  The remaining
case $|p/q-s|\geq1$ is harmless after decreasing the constant.

Combining (12), (16), and $q\leq u!$ gives the all-block bound



$$
v!<K_s^{-1}(u!)^d.                                    \tag{17}
$$



Roth improves the asymptotic exponent $d$ in (17) to $2+\varepsilon$, at
the cost of ineffectivity and finitely many exceptions.

For the original number, (10) is equivalently the factorial-digit block



$$
d_m(\pi)=m-2\qquad(m=u+1,\ldots,v).                   \tag{18}
$$



Thus Theorem 4 is a genuine obstruction that would hold if $e+\pi$ were
algebraic irrational.  It is not presently a resolution: no theorem is known
that forces $\pi$'s factorial digits to contain infinitely many blocks
violating (14).

### Corollary 5 (a conditional transcendence criterion)

Suppose the following two statements are proved for the fixed number
$x=\pi$:

1. $\mathcal R_n(\pi)$ fails for infinitely many $n$;
2. there are infinitely many recurrence blocks $[u_j,v_j)$, with
   $u_j\to\infty$, for which
   

$$
\limsup_{j\to\infty}
   \frac{\log(v_j!)}{\log(u_j!)}>2.                    \tag{19}
$$



Then $e+\pi$ is transcendental.

#### Proof

The first statement and Theorem 1 exclude $e+\pi\in\mathbb Q$, because a
rational value would force every sufficiently late recurrence event.  The
strict inequality in (19) supplies some $\varepsilon>0$ and infinitely many
blocks with $v_j!>(u_j!)^{2+\varepsilon}$.  Theorem 4 therefore excludes
algebraic irrationality.  A real algebraic number is either rational or
algebraic irrational, so both algebraic cases have been excluded. $\square$

Equivalently, it would be enough to prove both

1. infinitely many recurrence failures (excluding the rational case), and
2. infinitely many blocks with factorial span exponent strictly greater than
   two,

for the fixed factorial digits of $\pi$.  Corollary 5 is a criterion, not a
verification: neither required all-index statement is currently established
for $\pi$.

## 6. Distributional and computational no-go audit

Theorem 1 implies that eventual recurrence is a measure-zero phenomenon, but
also that its exceptional set is dense.  Therefore:

- an almost-everywhere equidistribution theorem for $\{n!x\}$ cannot be
  specialized to the fixed value $x=\pi$ without an additional theorem;
- probabilistic heuristics for factorial digits cannot certify a single digit
  of the infinite tail;
- checking any finite number of failures cannot rule out a later onset;
- finite congruences derived through (6) are just finite digit information and
  are covered by Theorem 2;
- a contradiction must use special analytic or arithmetic information about
  $\pi$, not just the abstract recurrence and not just the already-known
  transcendence of $\pi$.

The countable dense family $q-e$ is a concrete consistency model for every
formal consequence of the eventual recurrence.  This does not prove that
$\pi=q-e$ for some rational $q$; it proves why a purely formal modular or
$p$-adic manipulation of the recurrence cannot disprove that possibility.

## Conclusion

Yu's tail recurrence remains a correct exact route to a proof of rationality:
proving it for all sufficiently large indices would rigorously prove that
$e+\pi$ is rational.  The research here did not establish that tail.

The new positive result is the block obstruction: under algebraic
irrationality of $e+\pi$, Roth's theorem forbids recurrence blocks whose
endpoint factorial has exponent greater than $2+\varepsilon$ relative to
the starting factorial, apart from finitely many exceptions.  The new no-go
result is finite-prefix universality: every finite ceiling/digit record is
compatible, after replacing the fixed number $\pi$ by a transcendental
number with that same finite record, with each of the three possible classes
for the sum with $e$.  Neither statement settles the fixed special value
$e+\pi$, but both sharply identify what an all-index proof would have to add.
