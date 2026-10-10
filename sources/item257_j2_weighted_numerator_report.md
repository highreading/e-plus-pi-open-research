> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 257 — actual-row half-binomial weights and the height/residue ceiling

Checked: 2026-08-31 (Beijing time)

## 1. Scope and verdict

Write $M$ for the **global** index in the ordinary $j=2$ cell and
$k=s-1$ for the half-binomial prefix index.  Thus



$$
4M+1=5p-2s,\qquad 1\le s\le {p-3\over6},\qquad
 H_k=\sum_{j=0}^k{\binom{2j}{j}\over8^j}.             \tag{1.1}
$$



This distinction is essential: for fixed $M$, different row primes use
different numerators $N_k$.

> **PROVED — exact global reindexing.**  The integral candidate rows are
> parameterized by
> 

$$
> \begin{aligned}
> \mathcal S_M={}&\left\{s\ge1:
> 14s\le2M-7,\quad s\equiv3(M-1)\pmod5\right\},\\
> p_s={}&{4M+2s+1\over5},\qquad
> r_s={2M-14s-7\over5}=6M-7p_s.                    \tag{1.2}
> \end{aligned}
>
$$


> The actual prime rows are exactly
> 

$$
>             {4M+3\over5}\le p\le {6M\over7},      \tag{1.3}
>
$$


> with $p>7$ prime.  The map between these primes and
> $s\in\mathcal S_M$ is bijective.

> **PROVED — numerator container.**  Put
> 

$$
> U_k=8^kH_k,\qquad
> N_k={U_k\over2^{s_2(k)}}.                          \tag{1.4}
>
$$


> Then $v_2(U_k)=s_2(k)$, $N_k$ is odd, and
> 

$$
> 2^{3k-s_2(k)}\le N_k<2^{3k-s_2(k)+1/2}.            \tag{1.5}
>
$$


> If $R_M^H$ is the product of the distinct actual row primes for which
> $H_{s-1}=0\pmod p$, then
> 

$$
> \boxed{R_M^H\mid\mathcal P_M,\qquad
> \mathcal P_M=\prod_{s\in\mathcal S_M}N_{s-1}.}     \tag{1.6}
>
$$



> **PROVED, SHARPLY SCOPED NO-GO — individual numerator height and the
> automatic residue restrictions cannot reduce the $j=2$ mass.**  One has
> 

$$
> \boxed{
> \log\mathcal P_M={3\log2\over490}M^2+O(M\log M).} \tag{1.7}
>
$$


> Even the unfiltered lcm container contains its largest factor and hence
> has logarithm at least
> 

$$
> {3\log2\over7}M-O(\log M)
> =0.297063077\ldots M-O(\log M),                   \tag{1.8}
>
$$


> whereas the whole raw cell has log-prime mass only
> 

$$
> \boxed{{2\over35}M+o(M)=0.057142857\ldots M+o(M).} \tag{1.9}
>
$$


> Thus the raw support bound is strictly stronger than every available
> *unfiltered* numerator-height container.  This is a no-go for height plus
> congruence filtering, not a theorem about the actual factor distribution
> of $N_k$.

> **PROVED — no hidden residue-density gain.**  On an actual row
> 

$$
> p=6k+2d+1,\qquad d=r+4\equiv3,5\pmod6,\qquad
> p\equiv2k+3\pmod4.                                \tag{1.10}
>
$$


> But (1.10), and the congruence $s\pmod5$ in (1.2), are automatic
> consequences of the global cell.  They do not select a half or a fifth
> of the primes in (1.3).

> **PROVED, SCOPED JOINT CEILING.**  Item 251's rank-one gate prescribes an
> affine value of $H_k$; it does not require $H_k=0$.  The fixed-$M$
> square-divisor container of Item 197 remains the only available common
> integer height bound for the full gate.  Its Cauchy constant gives
> 

$$
> {\log R_M^{\rm gate}\over M}\le {H\over2}+o(1)
> =3.163813772\ldots+o(1),                           \tag{1.11}
>
$$


> whenever a nonzero coefficient is used, with the raw bound retained in
> every degenerate case.  This is again far above $2/35$.  Combining
> (1.6) with that square container adds the quadratic height (1.7) and is
> weaker still.

> **BOOKING DECISION.**  No $o(M)$ theorem and no constant below
> $2/35$ is obtained.  Therefore
> 

$$
> \boxed{\text{new unconditional Route-1 rate}=0,\qquad
>        \text{ordinary-}j=2\text{ capacity reduction}=0.}      \tag{1.12}
>
$$



The finite scan in the certificate is **EXACT FINITE ONLY**.

## 2. Exact row arithmetic

Solving (1.1) for $p$ gives



$$
5p=4M+2s+1.                  \tag{2.1}
$$



Integrality is equivalent to



$$
2s\equiv-4M-1\equiv M-1\pmod5,\qquad
                         s\equiv3(M-1)\pmod5.       \tag{2.2}
$$



The upper cell inequality is



$$
6s\le p-3
 \iff30s\le4M+2s-14
 \iff14s\le2M-7.                                   \tag{2.3}
$$



Substitution gives $r$ in (1.2).  It is an odd integer, and



$$
p=2r+6s+3=6k+2(r+4)+1.                             \tag{2.4}
$$



Conversely, an odd prime in (1.3) gives



$$
s={5p-4M-1\over2}\ge1,\qquad 6s\le p-3,          \tag{2.5}
$$



and hence one actual row.  Primality and $p>3$ make $3\nmid r$
automatic from $p\equiv2r\pmod3$.

The Item-219 parity condition is also automatic.  Reducing (2.1) modulo
four gives



$$
p\equiv2s+1\equiv2k+3\pmod4.                      \tag{2.6}
$$



Thus it would be incorrect to multiply the cell mass by an additional
$1/2$ for (2.6), or by $1/5$ for (2.2).  They are coordinate
descriptions of all primes in (1.3), not extra sieves.

By the prime number theorem,



$$
\sum_{\substack{p\ {\rm prime}\\(4M+3)/5\le p\le6M/7}}\log p
 =\left({6\over7}-{4\over5}\right)M+o(M)
 ={2M\over35}+o(M),                                \tag{2.7}
$$



which recovers the frozen ordinary-$j=2$ capacity.

## 3. The reduced numerator and its exact size

The integer



$$
U_k=\sum_{j=0}^k\binom{2j}{j}8^{k-j}              \tag{3.1}
$$



has one summand of uniquely least 2-adic valuation.  Legendre's formula
gives



$$
v_2\binom{2j}{j}=s_2(j),\qquad
 v_2\left(\binom{2j}{j}8^{k-j}\right)
 =s_2(j)+3(k-j).                                    \tag{3.2}
$$



For (j<k), writing (a=k-j>0) and using
$s_2(k)\le s_2(j)+s_2(a)\le s_2(j)+a$ gives



$$
s_2(j)+3a>s_2(k).                                  \tag{3.3}
$$



Hence $v_2(U_k)=s_2(k)$, proving the reduced form



$$
H_k={N_k\over D_k},\qquad D_k=2^{3k-s_2(k)}.      \tag{3.4}
$$



All summands are positive and the complete binomial series equals
$\sqrt2$, so



$$
1\le H_k<\sqrt2.           \tag{3.5}
$$



Equations (3.4)--(3.5) prove (1.5), including both endpoints and the
oddness of $N_k$.

For each actual zero, $p\mid N_{s-1}$, because $D_{s-1}$ is a
$p$-unit.  Different $s$'s give different $p_s$'s, so multiplying
these divisibilities proves (1.6).

## 4. Sharp ceiling for the height/residue route

The progression $\mathcal S_M$ has



$$
\#\mathcal S_M={M\over35}+O(1),\qquad
 \sum_{s\in\mathcal S_M}(s-1)={M^2\over490}+O(M). \tag{4.1}
$$



Also



$$
\sum_{s\in\mathcal S_M}s_2(s-1)=O(M\log M).       \tag{4.2}
$$



Using (3.4)--(3.5) termwise in $\log\mathcal P_M$ proves (1.7).
If $k_{\max}=\max_{s\in\mathcal S_M}(s-1)$, then



$$
k_{\max}={M\over7}+O(1),\qquad
 \log N_{k_{\max}}
 \ge(3k_{\max}-s_2(k_{\max}))\log2,              \tag{4.3}
$$



which proves (1.8) for the unfiltered lcm as well.

There is one valid but zero-rate exclusion.  Since



$$
N_k<2^{3k+1/2},                                    \tag{4.4}
$$



the divisibility $p_s\mid N_k$, with $p_s\asymp M$, is impossible
for $k\le(\log_2M)/3+O(1)$.  This removes only $O(\log M)$ possible
$s$-values.  Their total prime log weight is at most
$O((\log M)^2)=o(M)$, so it removes no positive fraction of (2.7).

The ceiling is information-theoretically sharp for the stated data.
Away from that $O(\log M)$ edge, the interval



$$
[D_k,\sqrt2D_k)
$$



has length greater than (2p_s).  It therefore contains an odd multiple
of $p_s$.  Consequently a family of odd integers can simultaneously
satisfy every scalar size window (1.5), every actual residue restriction,
and contain every candidate prime outside the edge.  This model is not the
actual sequence $N_k$; it proves precisely that size, parity, and
arithmetic-progression information alone cannot force a positive-mass
reduction.  A theorem about the factor distribution or a new independent
period is indispensable.

## 5. Why the affine gate does not repair this container

Item 251 and Item 252 give, with (d=r+2) in their boundary-polynomial
notation,



$$
A_s=(-1)^k\{\epsilon[H_k-h_kP_d(k)]-1\}\pmod p.   \tag{5.1}
$$



On the rank-one affine locus the remaining condition is



$$
f_\nu B_s\left[
 {9\kappa_r\over2}(-1)^k
 \{\epsilon[H_k-h_kP_d(k)]-1\}-\tau_{r,s}\right]
 +U_\nu=0\pmod p.                                  \tag{5.2}
$$



Thus (5.2) asks that $H_k$ equal a row-dependent affine target.  It is
not the zero condition $p\mid N_k$, and (1.6) is not a container for
the full common gate.

The independence is visible in exact actual rows:



$$
\begin{array}{c|r|r|r|r|r|r}
p&s&r&H_k&G_0&G_1&L_rc+M_r\\ \hline
43&3&11&0&29&20&13\\
47&5&7&0&31&29&30\\
367&39&65&234&238&354&0
\end{array}                                        \tag{5.3}
$$



For the last row the cubic resultant is also zero.  Therefore neither
$H_k=0$ nor the Item-250 affine eliminant implies the other.  The last
row remains a false positive, so (5.3) does not assert a common collision.

For the actual common gate, the fixed-$M$ integer coefficients of Item
197 satisfy $p^2\mid C_0(M),C_1(M)$.  Its proved Cauchy bound has



$$
H=6.327627545440858\ldots.                         \tag{5.4}
$$



The available exponent two yields (1.11).  With the same height, an
exponent greater than



$$
{H\over2/35}=110.733\ldots                         \tag{5.5}
$$



would be needed merely to beat the raw $j=2$ mass.  No such valuation
multiplicity is present.  Item 255's reciprocal orbit and Item 256's first
jet give no second independent condition, so they cannot be counted as
extra copies.

## 6. Route-1 threshold comparison

The raw $j=2$ cell contributes



$$
{2\over35}\quad\hbox{per global }M,\qquad
 {1\over105}\quad\hbox{per }6M.                    \tag{6.1}
$$



Any theorem with retained exceptional weight strictly below $2/35$
per $M$ would book a genuine partial reduction.  To close the currently
recorded common-log gap **conditional on complete removal of the $j=1$
cell**, the retained $j=2$ exception allowance is only



$$
6(0.0007599863045581\ldots)
 =0.0045599178273486\ldots\quad\hbox{per }M.         \tag{6.2}
$$



The numerator product is quadratic, the unfiltered lcm coefficient in
(1.8) is $0.297063\ldots$, and the fixed-$M$ square-height coefficient
in (1.11) is (3.163813\ldots).  After taking the minimum with raw
support, all three give exactly the old $2/35$ ceiling.  They do not
approach either the partial-booking threshold or (6.2).

## 7. Exact finite replay and strict labels

The checker verifies:

* the bijection (1.2)--(1.3) for every $M\le1000$;
* $v_2(U_k)=s_2(k)$, odd reduction, and the squared size inequalities
  through $k=257$;
* selected exact product/lcm containers;
* all 128,682 actual rows through $p\le5000$, finding 57 $H_k$-zeros;
* the three independence witnesses (5.3) against the frozen Item-250
  formulas.

In that bounded scan the 57 zeros occur at 57 distinct global indices.
The first two are



$$
(p,k,M)=(43,2,52),\qquad(47,4,56).                 \tag{7.1}
$$



Their individual observed weights exceed $2/35$ at those small $M$'s;
this has no asymptotic significance.  All zero counts, distinctness
claims, observed ratios, and nonoccurrences in the scan are
**EXACT FINITE ONLY**.

### PROVED

* the global reindex, prime interval, and automatic residue statements;
* the exact numerator container and height asymptotics;
* the zero-rate small-prefix edge;
* the sharply scoped height/residue information barrier;
* the affine-target distinction and the available joint-height comparison;
* the zero booking decision.

### EXACT FINITE ONLY

* every bounded replay count and witness census in the certificate.

### OPEN

* any theorem on admissible large prime factors of the actual $N_k$;
* any punctured-moment or higher-jet condition independent of the existing
  phase resonance;
* an $o(M)$ or $<2M/35$ theorem for the actual Item-251 gate;
* any new Route-1 capacity or conclusion about $e+\pi$.

## 8. Reproduction

From the portable archive root:

~~~
python scripts/item257_j2_weighted_numerator_certificate.py \
  --output results/item257_j2_weighted_numerator_certificate.json
python scripts/item257_j2_weighted_numerator_certificate.py \
  --output results/item257_j2_weighted_numerator_certificate_replay.json
~~~

The checker uses only Python's standard library and the frozen Item-250
checker.  It contains no timestamp, random seed, elapsed time, or host path.
