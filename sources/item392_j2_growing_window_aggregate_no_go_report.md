> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 392 — ordinary-$j=2$ growing-window aggregate propagation theorem

Checked: 2026-09-01 (Beijing time)

## 1. Scope and outcome

Item 385 proved that every fixed finite collection of target-retaining
same-ray returns has zero logarithmic prime-pair mass.  This item makes the
offset set move with $M$, treats the degenerate and nondegenerate charts
before either chart is selected, and identifies the transition scale
visible to an unconditional two-dimensional upper-bound sieve.

For the ordinary fixed-$j=2$ family, put



$$
I_M=\left[\frac{4M+3}{5},\frac{6M-1}{7}\right],
 \qquad
 \theta(I_M)=\sum_{\substack{p\in I_M\\p\ \text{prime}}}\log p.
\tag{1.1}
$$



The exact fixed-$M$ return from Item 385 is



$$
(r,s,p)\longmapsto(r-42k,s+15k,p+6k).
\tag{1.2}
$$



Let $H_M\subset\mathbb Z\setminus\{0\}$ be any finite offset set and
define



$$
\mathfrak s(k)=
 \prod_{\substack{q\mid k\\q\geq5\ \text{prime}}}\frac{q-1}{q-2},
 \qquad
 \Sigma(H_M)=\sum_{k\in H_M}\mathfrak s(|k|).
\tag{1.3}
$$



The empty product is one.  A candidate prime is $H_M$-paired if
$p+6k\in I_M$ is prime for at least one $k\in H_M$.  Write its
logarithmic mass as $W_{\rm pair}(M;H_M)$, and write the mass of the
complement in $I_M$ as $W_{\rm iso}(M;H_M)$.

> **PROVED — uniform moving-offset theorem.**  With an absolute implied
> constant,
> 

$$
>  \boxed{
>  W_{\rm pair}(M;H_M)
>  \ll \frac{M}{\log M}\Sigma(H_M).}
> \tag{1.4}
>
$$


> Offsets for which both endpoints lie in $I_M$ automatically satisfy
> $|k|\ll M$, so the estimate is uniform over every relevant set.

> **PROVED — strongest complete-window zero-rate regime supplied by this
> theorem.**  Uniformly for
> 

$$
> H_M(K)=\{k\in\mathbb Z:0<|k|\leq K(M)\},
>
$$


> one has
> 

$$
>  \boxed{W_{\rm pair}(M;K)\ll MK/\log M.}
> \tag{1.5}
>
$$


> Consequently every $K(M)=o(\log M)$ gives
> $W_{\rm pair}=o(M)$, while
> 

$$
>  \boxed{W_{\rm iso}(M;K)=\frac{2}{35}M+o(M).}
> \tag{1.6}
>
$$


> Thus the whole sublogarithmic same-ray window still leaves the complete
> raw normalized ordinary-$j=2$ capacity $1/105$ isolated.

> **PROVED — complementary packing theorem.**  For a complete symmetric
> window,
> 

$$
>  \boxed{W_{\rm iso}(M;K)\ll
>       \frac{M\log M}{K}+\log M.}
> \tag{1.7}
>
$$


> Hence if $K/\log M\to\infty$, the isolated raw mass is $o(M)$
> and the paired raw mass is $(2/35)M+o(M)$.

Equations (1.5) and (1.7) give a rigorous phase diagram.
Sublogarithmic complete windows pair only zero-rate mass;
superlogarithmic complete windows leave only zero-rate isolated mass.
The critical scale $K\asymp\log M$ is the exact barrier of these
unconditional inputs.  Nothing here asserts that this is a barrier for
the primes themselves.

This is a global no-go for every proposed **sublogarithmic-window**
propagation mechanism requiring a second actual prime row.  It is not a
bound on the actual incomplete-beta collision sets and therefore makes
no ledger booking:



$$
\boxed{\Delta r_1=0},\qquad
 \boxed{\Delta\text{ booked capacity}=0},\qquad
 \boxed{\text{raw ordinary-}j=2\text{ ceiling}=1/105}.
\tag{1.8}
$$



## 2. The chart-aggregate carrier space

The fixed-$M$ equations are



$$
p=2r+6s+3,\qquad 2M=5r+14s+7,
\tag{2.1}
$$



so $r=6M-7p$ and $s=(5p-4M-3)/2$.  Positivity is equivalent
to $p\in I_M$.  Apart from irrelevant small characteristics, every
prime in this interval is one actual row, and the prime number theorem
gives



$$
\theta(I_M)=\left(\frac67-\frac45\right)M+o(M)
 =\frac{2}{35}M+o(M).
\tag{2.2}
$$



Items 334 and 349 partition possible target-retaining collisions into
nondegenerate and degenerate primitive-carrier charts.  They do not make
two copies of (2.2).  Pairing is tested before the chart label or carrier
value is read.  Therefore any propagation argument on either chart, or on
their union, that requires a second actual row is contained in the single
prime-pair support bounded below.

## 3. A self-contained uniform prime-pair upper bound

We record and prove exactly the sieve input used here.

### Lemma 3.1 (uniform two-linear-form upper bound)

Let $J$ be an interval contained in $[cX,CX]$, of length at most
$(C-c)X$, where $0<c<C<\infty$ are fixed.  If $0<|h|\leq CX$,
then



$$
\#\{n\in J:n\text{ and }n+h\text{ are prime}\}
 \ll_{c,C}\frac{X}{(\log X)^2}
 \prod_{\substack{q\mid h\\q>2}}\frac{q-1}{q-2}.
\tag{3.1}
$$



The estimate is unconditional and the constant does not depend on $h$.

#### Proof

Put $z=X^{1/4}$ and sift the polynomial $F_h(n)=n(n+h)$ by
primes below $z$.  If one of the two prime values is itself below
$z$, there are only $O(z)$ exceptional $n$, which is harmless.
For a squarefree $d$, the number of roots of $F_h$ modulo $d$
is multiplicative, with



$$
\nu_h(q)=
 \begin{cases}
 1,&q\mid h,\\
 2,&q\nmid h.
 \end{cases}
\tag{3.2}
$$



Interval counting gives



$$
\#\{n\in J:d\mid F_h(n)\}
 =\frac{|J|\nu_h(d)}d+O(\nu_h(d)).
\tag{3.3}
$$



Apply the Selberg square majorant
$\bigl(\sum_{d\mid F_h(n)}\lambda_d\bigr)^2$, with
$\lambda_1=1$ and $\lambda_d=0$ for $d\geq z$.
Expanding the square, inserting (3.3), and minimizing the resulting
positive quadratic form gives



$$
S(J,z)\leq \frac{|J|}{G_h(z)}
       +O\bigl(z^2(\log z)^4\bigr),
\qquad
 G_h(z)=\sum_{\substack{d<z\\d\ \text{squarefree}}}
 \prod_{q\mid d}\frac{\nu_h(q)}{q-\nu_h(q)}.
\tag{3.4}
$$



For completeness, the minimizer follows by completing the square after
the change of variables
$y_d=\sum_{d\mid m}\lambda_m\nu_h(m)/m$.  The coefficient of
$y_d^2$ is
$\prod_{q\mid d}\nu_h(q)/(q-\nu_h(q))$, and
$\lambda_1=1$ becomes one linear constraint.  Cauchy--Schwarz gives
the first term in (3.4).  The displayed remainder follows from
$\nu_h(d)\leq2^{\omega(d)}$ and
$\sum_{d<z^2}3^{\omega(d)}\ll z^2(\log z)^2$.

It remains to bound $G_h$ uniformly.  Put
$b_h(q)=\nu_h(q)/(q-\nu_h(q))$ and $y=z^{1/4}$.  Give squarefree
products of primes below $y$ probability proportional to
$b_h(d)=\prod_{q\mid d}b_h(q)$.  Their total unnormalized mass is



$$
P_h(y)=\prod_{2<q<y}(1+b_h(q)).
\tag{3.5}
$$



Under this product measure,



$$
\mathbb E(\log d)
 =\sum_{2<q<y}\frac{b_h(q)}{1+b_h(q)}\log q
 =\sum_{2<q<y}\frac{\nu_h(q)\log q}{q}
 \leq 2\log y+O(1)=\frac12\log z+O(1).
\tag{3.6}
$$



The elementary Mertens estimates used here are
$\sum_{q<y}\log q/q=\log y+O(1)$ and
$\prod_{2<q<y}(1-2/q)^{-1}\asymp(\log y)^2$.
The second follows by taking logarithms, using
$\sum_{q<y}1/q=\log\log y+O(1)$, and absorbing the convergent
$\sum_qO(q^{-2})$ tail.  Markov's inequality in (3.6) shows that,
for all sufficiently large $z$, a fixed positive proportion of the
$P_h(y)$-mass has $d<z$, hence is included in $G_h(z)$.
Finally,



$$
P_h(y)\asymp(\log y)^2
 \prod_{\substack{q\mid h\\2<q<y}}\frac{q-2}{q-1}.
\tag{3.7}
$$



Adding the factors with $y\leq q<z$, all at most one, only decreases
the right-hand side.  We have therefore proved, uniformly in $h$,



$$
G_h(z)\gg(\log z)^2
 \prod_{\substack{q\mid h\\2<q<z}}\frac{q-2}{q-1}.
\tag{3.8}
$$



Primes $q\mid h$ with $q\geq z$ only enlarge the product on the
right of (3.1).  Since the error in (3.4) is
$O(X^{1/2}(\log X)^4)$, (3.1) follows.  $\square$

Apply Lemma 3.1 with $h=6k$.  The fixed factors at 2 and 3 are
absorbed in the absolute constant, giving



$$
\#\{p\in I_M:p,\ p+6k\in I_M\text{ prime}\}
 \ll \frac{M}{(\log M)^2}\mathfrak s(|k|).
\tag{3.9}
$$



Since $\log p\ll\log M$, summing (3.9) over $H_M$ proves
(1.4).  Overlaps only improve this union bound.

## 4. Averaging the moving singular factor

For $k\geq1$, expand the finite Euler product exactly:



$$
\mathfrak s(k)
 =\sum_{\substack{d\mid k\\d\ \text{squarefree}\\(d,6)=1}}
       \prod_{q\mid d}\frac1{q-2}.
\tag{4.1}
$$



All terms are nonnegative.  Therefore



$$
\begin{aligned}
 \sum_{k\leq K}\mathfrak s(k)
 &\leq K\sum_{\substack{d\geq1\\d\ \text{squarefree}\\(d,6)=1}}
       \frac1d\prod_{q\mid d}\frac1{q-2}\\
 &=K\prod_{q\geq5}\left(1+\frac1{q(q-2)}\right)
 =:A K.
\tag{4.2}
\end{aligned}
$$



The product $A$ converges because its logarithm is bounded by
$\sum_{q\geq5}1/(q(q-2))<\infty$.  Hence
$\Sigma(H_M(K))\leq2AK$, and (1.5) follows.

More generally, (1.4) proves zero rate for every sparse moving family
satisfying



$$
\boxed{\Sigma(H_M)=o(\log M).}
\tag{4.3}
$$



Such a family may contain offsets much larger than $\log M$; it is the
weighted cardinality, not the largest displacement, that matters.

Subtracting (1.4) from (2.2) gives the quantitative raw
isolated-capacity remainder



$$
\boxed{
 W_{\rm iso}(M;H_M)\geq
 \frac{2}{35}M
 -O\left(\frac{M\Sigma(H_M)}{\log M}\right)+o(M).}
\tag{4.4}
$$



For a complete window this becomes



$$
\frac{W_{\rm iso}(M;K)}{6M}
 \geq\frac1{105}-O\left(\frac K{\log M}\right)+o(1).
\tag{4.5}
$$



This lower bound is a statement about unused raw support, not a claim
that any isolated candidate is an actual collision.

## 5. The complementary packing theorem and logarithmic barrier

All primes in $I_M$ are, for large $M$, in one of the two residue
classes $\pm1\pmod6$.  Two primes on the same residue ray differ by
$6k$.  If both are isolated for the complete window
$0<|k|\leq K$, their distance is strictly greater than $6K$.
The interval length is $(2/35)M+O(1)$, so each ray contains at most



$$
1+\frac{(2/35)M+O(1)}{6K}
\tag{5.1}
$$



isolated primes.  Multiplying the two-ray count by $O(\log M)$
proves (1.7).

Combining (1.5), (2.2), and (1.7) gives



$$
\begin{array}{c|c|c}
 \text{window scale}&W_{\rm pair}&W_{\rm iso}\\ \hline
 K=o(\log M)&o(M)&(2/35)M+o(M)\\
 K\asymp\log M&\text{not decided}&\text{not decided}\\
 K/\log M\to\infty&(2/35)M+o(M)&o(M).
\end{array}
\tag{5.2}
$$



The first line is the maximal complete-window growth regime for which
the uniform sieve/union theorem (1.4) proves paired support $o(M)$:
indeed $\mathfrak s(k)\geq1$, so its controlling quantity is already
at least $2K$.  At $K\asymp\log M$, (1.5) gives only $O(M)$
and (1.7) gives only $O(M)$.  Passing the critical scale would require
additional distribution information about short same-residue prime gaps
or an actual carrier implication; it cannot be obtained by merely
reusing the present two-form upper bound.

## 6. Consequence for Route 1

Any fixed-$M$ propagation rule whose visible return offsets form
$H_M$, and whose use requires both endpoints to be actual prime rows,
can touch at most the mass in (1.4).  Consequently:

1. every complete same-ray operator window of order
   $J(M)=o(\log M)$, equivalently
   $K=\lfloor J/7\rfloor=o(\log M)$, touches only zero-rate raw support;
2. every sparse offset family with $\Sigma(H_M)=o(\log M)$ has the
   same no-go, even when its maximum offset grows rapidly;
3. a complete superlogarithmic window is not dismissed by this argument:
   it pairs essentially all raw candidate mass, but no theorem here makes
   an actual collision propagate across any one of those pairs; and
4. the statements apply to the union of the degenerate and nondegenerate
   target-retaining charts because prime-pair support precedes chart
   evaluation.

Thus Item 392 materially enlarges Item 385 from every fixed bounded
window to the full sublogarithmic tower, and proves the elementary packing
converse.  It does **not** reduce
$W_{\rm nd}(M)+W_{\rm deg}(M)$, because an actual collision can still
sit on any isolated row and no cross-prime implication has been proved.

## 7. Certificate and evidence labels

The deterministic certificate verifies:

- the frozen Item 385 dependencies;
- exact equality between the Euler-product and divisor expansions in
  (4.1) for all declared $k$;
- bounded averages in (4.2) on declared finite ranges;
- exact partition of candidate primes into paired and isolated support;
- the $6K$-separation and packing inequality for isolated primes; and
- replay equality of all serialized theorem and diagnostic fields.

All prime counts, ratios, singular-factor averages, and finite window
partitions in the JSON are labelled **EXACT FINITE ONLY / DIAGNOSTIC**.
The asymptotic assertions are proved in Sections 3--5 and are not inferred
from the finite data.

## 8. Ledger delta

- proved lower bound: unchanged;
- booked upper bound: unchanged;
- ordinary-$j=2$ raw aggregate ceiling: unchanged at $1/105$;
- new closed mechanism: every target-retaining propagation scheme needing
  a second actual row in a complete $o(\log M)$ same-ray window, and
  every sparse moving family satisfying (4.3);
- newly exposed threshold: $K\asymp\log M$; and
- finite diagnostics: not booked and not extrapolated.

