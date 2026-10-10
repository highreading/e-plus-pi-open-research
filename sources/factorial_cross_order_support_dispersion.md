> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Cross-order factorial-digit support dispersion

Date: 2026-08-28

## 1. Status

This note records new deductions from the exact factorial-digit formulas in
the archive.  It does **not** prove that $e+\pi$ is irrational or
transcendental.  It proves three theorem-level statements:

1. an exact determinant identity for two arbitrary primitive
   finite-difference forms, possibly with different bases and orders;
2. an unconditional lower bound for the combined outside-prime parts of
   their denominators, generalizing the untouched-truncation dispersion law
   to all orders;
3. a no-go theorem for moving-support blocks lying in a bounded
   multiplicative base window and a genuinely subdiagonal order region.

It also gives a harmonic-support phase diagram.  On a ray
$b/a\to\lambda<1$, algebraicity of $e+\pi$ forces the primitive
denominator to have harmonic prime-support mass at least
$((1-\lambda)/2-o(1))\log a$.  Any fixed positive saving below that
threshold proves transcendence.

The surviving regimes are correspondingly sharp: a successful moving block
must use very widely separated base scales, orders with $b/a\to1$, or new
arithmetic information that is not captured by the present determinant
bound.

## 2. Exact primitive coordinates

Put



$$
\alpha=e+\pi,
 \qquad
 C_n=\lfloor n!e\rfloor+\lfloor n!\pi\rfloor,
 \qquad
 x_n=n!\alpha-C_n.
$$



For an admissible $(a,b)$, write



$$
W_{a,b}=\Delta^b(a!)=a!D_{a,b},
 \qquad
 Z_{a,b}=\Delta^bC_a=D_{a,b}C_a+K_{a,b}.
$$



The archive proves



$$
g_{a,b}=\gcd(D_{a,b},K_{a,b}),
 \quad
 \bar D_{a,b}=D_{a,b}/g_{a,b},
 \quad
 \bar K_{a,b}=K_{a,b}/g_{a,b},
$$





$$
J_{a,b}=\gcd\bigl(a!,\bar D_{a,b}C_a+\bar K_{a,b}\bigr),
 \qquad
 H_{a,b}=g_{a,b}J_{a,b},
 \qquad
 \gcd(J_{a,b},\bar D_{a,b})=1.
$$



Consequently the fully primitive pair has the particularly useful form



$$
\boxed{
 P_{a,b}=\frac{\bar D_{a,b}C_a+\bar K_{a,b}}{J_{a,b}},
 \qquad
 Q_{a,b}=\frac{a!\bar D_{a,b}}{J_{a,b}}.}
 \tag{2.1}
$$



For $b=0$, use



$$
D_{a,0}=\bar D_{a,0}=1,
 \qquad K_{a,0}=\bar K_{a,0}=0,
 \qquad g_{a,0}=1.
$$



Let



$$
X_{a,b}=\Delta^b x_a.
$$



Then



$$
\frac{X_{a,b}}{g_{a,b}}
 =\bar D_{a,b}x_a-\bar K_{a,b}.             \tag{2.2}
$$



The archived digit bounds give, uniformly for $0\le b\le B$,



$$
|X_{a,b}|<2^{B+1}.                                  \tag{2.3}
$$



Also



$$
D_{a,b}\le \frac{(a+b)!}{a!}\le(a+B)^B             \tag{2.4}
$$



when $b\le B$; the first inequality is harmlessly non-strict here.

## 3. The cross-order determinant theorem

Let $(a,b)$ and $(m,c)$ be admissible, with $a\le m$.  Define



$$
R_{a,m}=\frac{m!}{a!},
 \qquad
 T_{a,m}=C_m-R_{a,m}C_a.
 \tag{3.1}
$$



Iteration of the canonical recurrence gives



$$
T_{a,m}=\sum_{j=a+1}^{m}\frac{m!}{j!}c_j\in\mathbb Z_{\ge0},
 \qquad
 x_m=R_{a,m}x_a-T_{a,m}.                             \tag{3.2}
$$



Define the integral cross residual



$$
\boxed{
 \begin{aligned}
 \mathcal R_{a,b;m,c}
 &={}
 R_{a,m}\bar D_{m,c}\bar K_{a,b}\notag\\
 &\quad-
 \bar D_{a,b}
 \bigl(\bar D_{m,c}T_{a,m}+\bar K_{m,c}\bigr).
 \end{aligned}}
 \tag{3.3}
$$



### Theorem 3.1

The primitive determinant is exactly



$$
\boxed{
 P_{a,b}Q_{m,c}-P_{m,c}Q_{a,b}
 =\frac{a!\mathcal R_{a,b;m,c}}
 {J_{a,b}J_{m,c}}.}
 \tag{3.4}
$$



In particular,



$$
J_{a,b}J_{m,c}\mid a!\mathcal R_{a,b;m,c}.          \tag{3.5}
$$



The two primitive pairs are distinct if and only if
$\mathcal R_{a,b;m,c}\ne0$.

There is also the cancellation identity



$$
\boxed{
 \mathcal R_{a,b;m,c}
 =\bar D_{a,b}\frac{X_{m,c}}{g_{m,c}}
 -R_{a,m}\bar D_{m,c}\frac{X_{a,b}}{g_{a,b}}.}
 \tag{3.6}
$$



#### Proof

Substitute (2.1) into the left side of (3.4).  Its numerator is



$$
\begin{aligned}
 &m!\bar D_{m,c}
   (\bar D_{a,b}C_a+\bar K_{a,b})\\
 &\quad-a!\bar D_{a,b}
   (\bar D_{m,c}C_m+\bar K_{m,c}).
 \end{aligned}
$$



Use $m!=a!R_{a,m}$ and
$C_m=R_{a,m}C_a+T_{a,m}$.  The terms containing $C_a$
cancel, and the result is $a!\mathcal R_{a,b;m,c}$.  This proves
(3.4).  The left side is an integer, proving (3.5).  Two primitive pairs
with positive second coordinate have zero determinant exactly when they are
equal, which proves the distinctness assertion.

Finally, substitute (2.2) and (3.2) into the right side of (3.6).  The
coefficient of $x_a$ cancels, leaving exactly (3.3).  $\square$

### Uniform residual bound

If $b,c\le B$, equations (2.3), (2.4), and (3.6) give



$$
\begin{aligned}
 |\mathcal R_{a,b;m,c}|
 &\le
 D_{a,b}|X_{m,c}|+R_{a,m}D_{m,c}|X_{a,b}|\\
 &\le
 \boxed{2^{B+2}R_{a,m}(m+B)^B}.
 \end{aligned}                                      \tag{3.7}
$$



The important point is that the bound contains one finite-difference
factor $D$, not a product $D_{a,b}D_{m,c}$.  This saving comes from
the exact cancellation in (3.6).

## 4. All-order outside-prime dispersion

For a finite prime set $\mathcal S$, let $N_{\mathcal S^c}$ denote
the part of $|N|$ supported outside $\mathcal S$.

### Theorem 4.1

Suppose the two primitive pairs in Theorem 3.1 are distinct.  Then



$$
\boxed{
 (Q_{a,b})_{\mathcal S^c}(Q_{m,c})_{\mathcal S^c}
 \ge
 \frac{(m!)_{\mathcal S^c}}
 {|\mathcal R_{a,b;m,c}|_{\mathcal S^c}}.}
 \tag{4.1}
$$



Consequently, if $b,c\le B$,



$$
\boxed{
 (Q_{a,b})_{\mathcal S^c}(Q_{m,c})_{\mathcal S^c}
 \ge
 \frac{a!}
 {2^{B+2}(m+B)^B(m!)_{\mathcal S}}.}
 \tag{4.2}
$$



#### Proof

Because $J_{a,b}\mid a!$ and
$\gcd(J_{a,b},\bar D_{a,b})=1$, equation (2.1) gives



$$
(Q_{a,b})_{\mathcal S^c}
 = (\bar D_{a,b})_{\mathcal S^c}
   \frac{(a!)_{\mathcal S^c}}{(J_{a,b})_{\mathcal S^c}},
$$



and similarly at $(m,c)$.  Dropping the two $\bar D$-parts gives



$$
(Q_{a,b})_{\mathcal S^c}(Q_{m,c})_{\mathcal S^c}
 \ge
 \frac{(a!)_{\mathcal S^c}(m!)_{\mathcal S^c}}
 {(J_{a,b}J_{m,c})_{\mathcal S^c}}.
$$



Divisibility (3.5) bounds the denominator by
$(a!)_{\mathcal S^c}|\mathcal R|_{\mathcal S^c}$, proving
(4.1).  Use (3.7),
$(m!)_{\mathcal S^c}=m!/(m!)_{\mathcal S}$, and
$m!/R_{a,m}=a!$ to obtain (4.2).  $\square$

For $b=c=0$, this recovers the scale of the archived
untouched-truncation dispersion theorem.  The new statement permits
arbitrary orders, different orders, and different bases.

## 5. Fixed-support lacunarity for every bounded order

Define



$$
\mathcal A(\mathcal S)
 =\sum_{p\in\mathcal S}\frac{\log p}{p-1}.
 \tag{5.1}
$$



Legendre's formula gives



$$
\log(m!)_{\mathcal S}\le m\mathcal A(\mathcal S).  \tag{5.2}
$$



If both denominators in Theorem 4.1 are $\mathcal S$-units, (4.2)
implies the exact necessary inequality



$$
\boxed{
 \log a!
 \le
 m\mathcal A(\mathcal S)
 +B\log(m+B)+(B+2)\log2.}
 \tag{5.3}
$$



Therefore, for fixed $B$ and fixed nonempty $\mathcal S$, any
infinite sequence of distinct primitive pairs of orders at most $B$,
whose denominators are $\mathcal S$-units, must satisfy between
successive base indices $a<m$



$$
\boxed{
 m\ge(1-o(1))\frac{\log a!}{\mathcal A(\mathcal S)}
 \sim\frac{a\log a}{\mathcal A(\mathcal S)}.}
 \tag{5.4}
$$



Indeed, if $m$ is already larger than the right side there is nothing to
prove; otherwise $m=O(a\log a)$, so the $B\log(m+B)$ term is
$o(\log a!)$, and (5.3) gives (5.4).

This extends the archived $b=0$ S-unit gap law to every bounded family of
finite-difference orders.

## 6. No-go theorem for natural moving blocks

The next statement concerns the full union of denominator supports, so it
also applies when the union is enlarged by all numerator primes as in the
moving-support Subspace-Theorem criterion.

### Theorem 6.1

Fix constants $\kappa>1$ and $\theta\ge0$ such that



$$
\theta\kappa<1.                                     \tag{6.1}
$$



For each large $A$, let $\mathcal B_A$ be a set of at least two
distinct primitive factorial-digit pairs with



$$
A\le a\le\kappa A,
 \qquad
 0\le b\le\theta a.                                 \tag{6.2}
$$



Let $\mathcal S_A$ contain every prime dividing a denominator in the
block.  Then



$$
\boxed{
 \mathcal A(\mathcal S_A)
 \ge
 \left(\frac{1-\theta\kappa}{\kappa}-o(1)\right)
 \log A.}
 \tag{6.3}
$$



Moreover,



$$
\boxed{
 |\mathcal S_A|
 \ge A^{(1-\theta\kappa)/\kappa-o(1)}.}
 \tag{6.4}
$$



#### Proof

Choose any two distinct points and order their bases as $a\le m$.
All orders are at most



$$
B=\lfloor\theta\kappa A\rfloor.
$$



The denominators are $\mathcal S_A$-units, so (5.3), Stirling's
formula, $a\ge A$, and $m\le\kappa A$ give



$$
A\log A-\theta\kappa A\log A-O(A)
 \le\kappa A\mathcal A(\mathcal S_A),
$$



which is (6.3).

For a set of $s$ primes, the sum in (5.1) is maximized by the first
$s$ primes.  The classical estimates



$$
\sum_{p\le y}\frac{\log p}{p-1}=\log y+O(1),
 \qquad p_s=s^{1+o(1)},
$$



therefore turn (6.3) into (6.4).  $\square$

### Corollary 6.2

No sequence of blocks satisfying (6.2) can verify the archived
moving-support condition



$$
s_A^6\log(s_A+2)=o(\log M_A),
 \qquad
 s_A=1+|\mathcal S_A|,
 \quad M_A=|\mathcal B_A|.
 \tag{6.5}
$$



Indeed, the entire region (6.2) contains only $O(A^2)$ indexed forms, so
$\log M_A=O(\log A)$, whereas (6.4) makes the left side of (6.5) a
positive power of $A$.

Thus moving blocks contained in a fixed multiplicative base window are
rigorously excluded whenever their orders stay genuinely below the
diagonal.  For every fixed relative margin $\delta>0$, forms with
$b\le(1-\delta)a$ are covered by choosing $\kappa>1$ sufficiently
close to one.

## 7. Harmonic-support phase diagram along a ray

For an integer $Q>0$, define



$$
\mathcal A(Q)=\sum_{p\mid Q}\frac{\log p}{p-1}.
 \tag{7.1}
$$



From (2.1), put $F_{a,b}=a!/J_{a,b}$.  Since $F_{a,b}\mid a!$
and every prime of $F_{a,b}$ divides $Q_{a,b}$, Legendre's formula
gives



$$
\log F_{a,b}\le a\mathcal A(Q_{a,b}).
$$



Consequently,



$$
\boxed{
 \log Q_{a,b}
 \le a\mathcal A(Q_{a,b})+\log D_{a,b}.}
 \tag{7.2}
$$



### Theorem 7.1

Let $(a_j,b_j)$ be an infinite sequence with



$$
a_j\to\infty,
 \qquad
 \frac{b_j}{a_j}\to\lambda\in[0,1),
$$



whose primitive points are distinct, have $Q_{a_j,b_j}\to\infty$, and
have nonzero errors.  If $\alpha=e+\pi$ is algebraic irrational, then



$$
\boxed{
 \liminf_{j\to\infty}
 \frac{\mathcal A(Q_{a_j,b_j})}{\log a_j}
 \ge\frac{1-\lambda}{2}.}
 \tag{7.3}
$$



Equivalently, if for some fixed $\varepsilon>0$



$$
\mathcal A(Q_{a_j,b_j})
 \le\left(\frac{1-\lambda}{2}-\varepsilon\right)
 \log a_j                                             \tag{7.4}
$$



holds infinitely often under the stated height/nonzero conditions, then
$e+\pi$ is transcendental.

Under algebraicity, (7.3) also implies



$$
\boxed{
 \omega(Q_{a_j,b_j})
 \ge a_j^{(1-\lambda)/2-o(1)}.}
 \tag{7.5}
$$



#### Proof

For every fixed $\eta>0$, Roth's theorem gives eventually



$$
\left|\alpha-\frac{P_{a,b}}{Q_{a,b}}\right|
 \ge Q_{a,b}^{-2-\eta}.                              \tag{7.6}
$$



On the other hand, the exact factorial form and the digit bound give



$$
\left|\alpha-\frac{P_{a,b}}{Q_{a,b}}\right|
 =\frac{|X_{a,b}|}{W_{a,b}}
 \le\frac{2^{b+1}}{W_{a,b}}.                         \tag{7.7}
$$



Combining (7.2), (7.6), and (7.7) yields



$$
(2+\eta)
 \bigl(a\mathcal A(Q_{a,b})+\log D_{a,b}\bigr)
 \ge\log W_{a,b}-(b+1)\log2.                        \tag{7.8}
$$



The archived factorial-scale theorem and Stirling's formula give, when
$b/a\to\lambda$,



$$
\frac{\log W_{a,b}}{a\log a}\longrightarrow1+\lambda,
 \qquad
 \frac{\log D_{a,b}}{a\log a}\longrightarrow\lambda,
 \qquad
 \frac{b}{a\log a}\longrightarrow0.                 \tag{7.9}
$$



Divide (7.8) by $a\log a$, take the lower limit, and then let
$\eta\downarrow0$.  This proves (7.3).  Condition (7.4) contradicts
(7.3).

It remains to exclude rational $\alpha$.  If $\alpha=A/D$, then for all
sufficiently large $n$, $n!\alpha$ is integral and



$$
x_n=\{n!e\}+\{n!\pi\}\in(0,2)\cap\mathbb Z=\{1\}.
$$



Hence every positive-order difference has zero error eventually, contrary to
the nonzero-error hypothesis.  An infinite surviving sequence must therefore
have $b=0$ eventually.  Once $D^2\mid a!$, the corresponding primitive
denominator is $Q=a!$, whose harmonic support mass is
$(1+o(1))\log a$, so it cannot satisfy (7.4).  Thus (7.4) excludes rational
and algebraic-irrational $\alpha$, and proves transcendence.

Finally, maximize $\mathcal A(Q)$ among integers with $s$ distinct
prime divisors by using the first $s$ primes, and apply the same Mertens
and prime-number estimates used in Theorem 6.1.  This proves (7.5).
$\square$

The threshold tends to zero as $\lambda\to1$.  This is not a proof
artifact: near the diagonal, the local factor $D_{a,b}$ itself consumes
asymptotically half of the available factorial height.

## 8. Exact diagnostics and a distinctness counterexample

The companion program

`work/factorial_cross_order_support_diagnostic_sources_audit.py`

imports the archive's certified Machin interval helpers and performs only
integer calculations.  With maximum base $100$ and maximum order $10$,
it checked:

- 1,061 primitive forms;
- 562,330 indexed pairs;
- all 562,330 determinant identities and divisibilities;
- all 562,329 nonzero-residual coarse bounds;
- the exact support inequality for three selected prime sets.

It found one repeated primitive pair:



$$
(a,b)=(14,1),\qquad(m,c)=(16,0),
$$



with



$$
(P,Q)=(1021707687983,174356582400).                 \tag{8.1}
$$



The exact normalized records are



$$
\begin{array}{c|ccccc}
 (a,b)&D&K&g&\bar D&J\\ \hline
 (14,1)&14&7&7&2&1\\
 (16,0)&1&0&1&1&120.
 \end{array}
$$



Thus distinct indices do not imply distinct primitive points.  Any moving
block must deduplicate actual $(P,Q)$, exactly as required in the
Subspace-Theorem statement.  The equality (8.1) is an exact finite
counterexample; the absence of further coincidences in the scan is only a
diagnostic.

## 9. Exact remaining gap

The new theorems rule out two large classes of shortcuts:

1. fixed-support denominators of bounded-order forms cannot occur at
   comparable or merely linearly separated bases; they require at least
   $a\log a$-scale lacunarity;
2. moving blocks of polynomial size inside a bounded multiplicative base
   window cannot have sufficiently small cumulative support anywhere in a
   genuinely subdiagonal order region.

They do not rule out:

- one exceptionally supported point in each highly lacunary base scale;
- blocks spread across an enormous range of base indices;
- the near-diagonal regime $b/a\to1$, where the determinant residual can
  have factorial scale;
- a new theorem using special arithmetic of the actual factorial digits of
  $\pi$ to control $J_{a,b}$ or $\bar D_{a,b}$.

Accordingly, no fixed-support or moving-block hypothesis needed by the
Subspace-Theorem criterion has been verified.  The progress is an exact
support-dispersion theorem and a sharper classification of where any
successful support theorem would have to live.
