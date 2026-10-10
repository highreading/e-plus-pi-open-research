> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 394 — actual ordinary-$j=2$ matched-modulus aggregate and saturation collapse

Checked: 2026-09-01 (Beijing time)

## 1. Scope and verdict

Items 334 and 349 give the target-retaining primitive carrier and the
triple-minor degenerate carrier on one actual row.  Items 355, 359, and
361 show why within-prime moments, a common coefficient kernel, and the
old endpoint norm do not by themselves control the fixed-$M$ selector.
This item asks the remaining one-row question globally: can all selected
row carriers be packaged into one prime-independent integer of small
height?

The answer has two parts.

> **PROVED — exact prime-independent matched aggregate.**  There is an
> explicit integer $\mathfrak A_M^\sharp$, constructed from the actual
> Item-334 carrier on every integer row, matched gcds with the row modulus,
> one lcm, and a safe low-prime saturation, such that
> 

$$
>  \boxed{\mathfrak A_M^\sharp
>   =\prod_{\substack{p\in I_M\\
>       p\ \text{is an actual ordinary-}j=2\text{ collision}}}p.}
> \tag{1.1}
>
$$


> The construction does not enumerate primes and retains the moving
> incomplete-beta target.

> **PROVED — exact chart factorization.**  Item 349's safely saturated
> triple-minor carrier splits (1.1) into disjoint nondegenerate and
> degenerate factors
> 

$$
>  \boxed{\mathfrak A_M^\sharp
>   =\mathfrak A_{M,\rm nd}^\sharp
>    \mathfrak A_{M,\rm deg}^\sharp,\qquad
>    \gcd(\mathfrak A_{M,\rm nd}^\sharp,
>         \mathfrak A_{M,\rm deg}^\sharp)=1.}
> \tag{1.2}
>
$$


> Thus the degenerate carrier refines the aggregate but cannot shrink
> the union: the two charts recombine to the original exact support.

> **PROVED — best available height constant and collapse.**
> 

$$
>  \boxed{\log\mathfrak A_M^\sharp
>  \leq\frac{2}{35}M+o(M).}
> \tag{1.3}
>
$$


> After division by $6M$, this is exactly $1/105$.  It does not
> strictly reduce the shared ceiling.

Before the final low-prime saturation, the same matched construction has
a completely explicit linear height bound



$$
\log\mathfrak A_M\leq C_6M+o(M),\qquad
 C_6=0.12444924693451084\ldots .
\tag{1.4}
$$



The exact constant $C_6$ is proved below from the lcm of the
$6$-coprime integer rows.  The saturation improves (1.4) to (1.3),
but then (1.1) shows that the aggregate is literally the desired
collision product.  Proving any strict saving in its height is therefore
equivalent to the open weighted-density theorem, not a consequence of
packaging.

Items 361 and 349 make the obstruction formula-specific: target-free
phase elimination gives exactly the old norm $N_r$, whose selected
support contains (and may strictly exceed) (1.1), while the triple-minor
carrier only partitions (1.1).  No known actual resultant or norm yields
a smaller aggregate.

Consequently



$$
\boxed{\Delta r_1=0},\qquad
 \boxed{\Delta\text{ booked capacity}=0},\qquad
 \boxed{\text{ordinary-}j=2\text{ ceiling}=1/105}.
\tag{1.5}
$$



## 2. Integer rows and a canonical extension of the actual carrier

Put



$$
L_M=\left\lceil\frac{4M+3}{5}\right\rceil,\qquad
 U_M=\left\lfloor\frac{6M-1}{7}\right\rfloor,
\qquad
 \mathcal Q_M=\{q:L_M\leq q\leq U_M,\ (q,6)=1\}.
\tag{2.1}
$$



For $q\in\mathcal Q_M$, define



$$
r=6M-7q,\qquad
 s=\frac{5q-4M-1}{2},\qquad m=s-1.
\tag{2.2}
$$



These are exactly the positive ordinary integer rows.  If $q=p$ is
prime, (2.2) is the actual fixed-$M$ selector.

Item 334's target-retaining carrier contains



$$
\Phi_{r,s}=c_p+\epsilon_p h_mP_{r+2}(m),
\qquad \epsilon_p=\left(\frac2p\right).
\tag{2.3}
$$



It has a canonical extension to all $q\in\mathcal Q_M$: replace the
selected coefficient $c_p$ by



$$
c_q=[x^q](1-x)^n(1+x)^{n+Q},
\tag{2.4}
$$



with the same tied $n,Q$, and replace $\epsilon_p$ by the
Dirichlet character



$$
\chi_8(q)=(-1)^{(q^2-1)/8}.
\tag{2.5}
$$



For prime $q=p$, (2.5) equals $(2/p)$, so this extension agrees
exactly with the actual formula.  Use (2.4)-(2.5) in Item 334's
$D,T_0,T_1$, and set



$$
\mathfrak G_{M,q}
 =\gcd\bigl(|\operatorname{num}D|,
            |\operatorname{num}T_0|,
            |\operatorname{num}T_1|\bigr).
\tag{2.6}
$$



Let $S^G_{r,s}$ be the established Item-338 safe product of ingredient
denominators, the central-binomial factor, and already removed foreign
support.  If $N_{(S)}$ denotes the largest divisor of $N$ coprime to
$S$, define



$$
\widehat{\mathfrak G}_{M,q}
   =(\mathfrak G_{M,q})_{(S^G_{r,s})}.
\tag{2.7}
$$



Every actual selected prime is coprime to $S^G_{r,s}$.  Therefore
Item 334 gives the exact equivalence



$$
\boxed{p\text{ is an actual collision}
 \iff p\mid\widehat{\mathfrak G}_{M,p}.}
\tag{2.8}
$$



Likewise, let



$$
\widehat\Pi_{M,q}=(\Pi_r)_{(S^\Pi_{r,s})}
\tag{2.9}
$$



be Item 349's safely saturated triple-minor carrier.  On an actual prime
row,



$$
\boxed{p\mid\widehat\Pi_{M,p}
 \iff \ell_r=\mu_r=C_r=0\pmod p.}
\tag{2.10}
$$



No prime assumption enters the definitions (2.1)-(2.7) and (2.9);
primality is used only when interpreting their large prime divisors.

## 3. The matched aggregate

For each integer row put



$$
d_{M,q}=\operatorname{rad}
          \gcd(q,\widehat{\mathfrak G}_{M,q}),
\qquad
 e_{M,q}=\operatorname{rad}
          \gcd(q,\widehat\Pi_{M,q}).
\tag{3.1}
$$



Define



$$
\mathfrak A_M=\operatorname{lcm}_{q\in\mathcal Q_M}d_{M,q}.
\tag{3.2}
$$



This is one prime-independent integer.  It already has linear height
because $d_{M,q}\mid q$.  To remove support coming only from composite
integer rows, put $B_M=L_M-1$ and safely saturate



$$
\boxed{\mathfrak A_M^\sharp=(\mathfrak A_M)_{(B_M!)}.}
\tag{3.3}
$$



Every actual candidate prime is greater than $B_M$, so (3.3) cannot
remove it.

### Theorem 3.1 (exact support identity)

Equation (1.1) holds.

#### Proof

First note that



$$
U_M<2L_M
\tag{3.4}
$$



for every relevant $M$.  If a prime $\lambda>B_M$ divides some
$q\in\mathcal Q_M$, then $q=\lambda$: otherwise
$q\geq2\lambda\geq2L_M>U_M$.  Thus every prime surviving (3.3)
comes from its own prime row and from no composite row.

For that row, $d_{M,p}=p$ exactly when
$p\mid\widehat{\mathfrak G}_{M,p}$.  Apply (2.8).  Conversely every
actual collision prime makes $d_{M,p}=p$, survives (3.3), and hence
divides $\mathfrak A_M^\sharp$.  The radical in (3.1) makes the
product squarefree.  This proves (1.1).  $\square$

The construction is not merely a necessary aggregate: after the
low-prime saturation it has exactly the selected collision support.

## 4. Exact nondegenerate/degenerate recombination

Since $d_{M,q}$ and $e_{M,q}$ are squarefree, define the row factors



$$
d^{\rm deg}_{M,q}=\gcd(d_{M,q},e_{M,q}),\qquad
 d^{\rm nd}_{M,q}=(d_{M,q})_{(e_{M,q})}.
\tag{4.1}
$$



Their prime supports are disjoint and



$$
d_{M,q}=d^{\rm deg}_{M,q}d^{\rm nd}_{M,q}.
\tag{4.2}
$$



Take lcms over $q$ and then apply the saturation (3.3), obtaining
$\mathfrak A_{M,\rm deg}^\sharp$ and
$\mathfrak A_{M,\rm nd}^\sharp$.

For a surviving prime row, (2.10) says that $p$ enters the first
factor exactly on the triple-minor degenerate chart.  If (2.10) fails,
an actual collision enters the second factor.  Theorem 3.1 therefore
proves (1.2).

This is the precise actual-formula reason that Item 349 does not lower
the shared ceiling.  It can make either chart factor much smaller, but
their union is identically the Item-334 collision product.  Separate
weighted theorems are still useful; merely multiplying or norming the
two chart carriers is not.

## 5. Exact height of the unsaturated modulus envelope

By (3.1),



$$
\mathfrak A_M\mid
 \Lambda_M:=\operatorname{rad}
 \operatorname{lcm}\{q:q\in\mathcal Q_M\}.
\tag{5.1}
$$



We compute the leading logarithmic height of $\Lambda_M$, rather than
using the much weaker product of row heights.

Set



$$
\alpha=\frac45,\qquad \beta=\frac67.
\tag{5.2}
$$



Apart from the fixed primes $2,3$, a prime $\lambda$ divides
$\Lambda_M$ exactly when



$$
\lambda u\in[\alpha M+O(1),\beta M+O(1)]
\quad\text{for some }u\geq1,\ (u,6)=1.
\tag{5.3}
$$



Thus $\lambda/M$ belongs to the union



$$
\mathcal U=\bigcup_{\substack{u\geq1\\(u,6)=1}}
 \left(\frac{\alpha}{u},\frac{\beta}{u}\right].
\tag{5.4}
$$



Consecutive $6$-coprime multipliers have gaps $2$ or $4$.
The intervals for consecutive $u<v$ overlap exactly when



$$
\frac vu\leq\frac\beta\alpha=\frac{15}{14}.
\tag{5.5}
$$



The complete component decomposition is therefore:

- single intervals for
  $u=1,5,7,11,13,17,19,23,25$;
- overlapping pairs $(u,u+2)$ for
  $u=29,35,41,47,53$; and
- one tail component $(0,\beta/59]$.

Indeed $55\to59$ is the last non-overlapping gap $4$;
$59\to61$ overlaps, $61\to65$ overlaps, and every later gap
satisfies (5.5).

Hence the exact measure is



$$
\begin{aligned}
 C_6:=|\mathcal U|
={}&\frac{2}{35}
 \sum_{u\in\{1,5,7,11,13,17,19,23,25\}}\frac1u\\
&+\sum_{u\in\{29,35,41,47,53\}}
 \left(\frac{6}{7u}-\frac{4}{5(u+2)}\right)
 +\frac{6}{7\cdot59}\\
={}&
 \frac{6979177263689987598318}
 {56080510212831201972875}\\
={}&0.12444924693451084\ldots .
\tag{5.6}
\end{aligned}
$$



The prime number theorem applied to the finitely many components and
the tail gives



$$
\boxed{\log\Lambda_M=C_6M+o(M).}
\tag{5.7}
$$



Equations (5.1) and (5.7) prove (1.4).  This improves the old
$O(M^2\log M)$ raw carrier-product estimate to an explicit linear
bound, but $C_6>2/35$, so it is still weaker than the raw candidate
prime ceiling.

## 6. Final saturation and the exact capacity barrier

Theorem 3.1 and the prime number theorem give



$$
\begin{aligned}
 \log\mathfrak A_M^\sharp
 &=W_{\rm nd}(M)+W_{\rm deg}(M)\\
 &\leq\sum_{\substack{L_M\leq p\leq U_M\\p\ \text{prime}}}\log p\\
 &=\left(\frac67-\frac45\right)M+o(M)
 =\frac{2}{35}M+o(M).
\tag{6.1}
\end{aligned}
$$



Thus the best currently rigorous height constant for the exact
target-retaining aggregate is $2/35$ per $M$, or $1/105$ per
$6M$.  This is not a new proof of the raw ceiling; it explains why
the natural matched-modulus aggregation reaches exactly that ceiling
and stops.

More strongly, the desired theorem



$$
W_{\rm nd}(M)+W_{\rm deg}(M)=o(M)
\tag{6.2}
$$



is equivalent, term for term, to



$$
\log\mathfrak A_M^\sharp=o(M).
\tag{6.3}
$$



Accordingly, an improved height estimate for the aggregate cannot be
obtained merely from its construction.  It must use new arithmetic of
the actual carrier values.

## 7. Why the known resultants and norms do not improve (6.1)

This obstruction uses the actual formulas.

1. **Item 361 phase norm.**  Eliminating the selected phase from the
   nondegenerate old gate gives exactly
   

$$
N_r=18^3a_r^3+11^3\,2^{2r+2}b_r^3.
   \tag{7.1}
$$


   Every actual collision prime divides $N_r$, but Item 315 exhibits
   foreign cubic components.  Therefore the sharply saturated matched
   norm aggregate contains $\mathfrak A_M^\sharp$; it cannot be a
   smaller target-retaining divisor.  Retaining the phase gives the old
   selected gate, while eliminating it loses the legitimate second
   target.

2. **Item 349 triple-minor carrier.**  Equations (4.1)-(4.2) show
   exactly what adjoining $\Pi_r$ does: it partitions the collision
   product into degenerate and nondegenerate factors and recombines to
   the same $\mathfrak A_M^\sharp$.

3. **Item 359 coefficient kernel.**  The common fixed-$M$ rational
   kernel packages the old determinant coordinate.  Taking a product
   of its selected coefficient numerators has quadratic height.
   Matching each coefficient with its own modulus returns the construction
   (3.1)-(3.3); after safe saturation it is again (1.1).

4. **Item 355 second moments.**  At fixed $M$, each prime selects one
   row.  The exact aggregate identity (1.1) shows the same obstruction
   arithmetically: no within-prime energy estimate changes its selected
   large-prime factors.

Thus every already available actual-formula elimination either produces
a support superset (the old norm), partitions the same support (the
triple-minor carrier), or collapses to the exact collision product after
matched-modulus saturation.  This is not another abstract recurrence
countermodel.

## 8. Deterministic certificate and evidence labels

The certificate:

- verifies the frozen Items 334, 349, 355, 359, 361, 385, and 392
  dependencies;
- reconstructs the Item-334 and Item-349 carriers on declared rows;
- verifies the $\chi_8$ extension agrees with $(2/p)$ on declared
  actual primes;
- checks the matched gcd, lcm, low-prime saturation, exact support, and
  chart partition identities on declared fixed-$M$ slices;
- proves the interval component list in (5.6) using exact rational
  arithmetic; and
- replays finite lcm-envelope ratios as diagnostics.

Every enumerated row, prime, carrier, and numerical lcm ratio is labelled
**EXACT FINITE ONLY / DIAGNOSTIC**.  Equations (1.1)-(1.4) are proved
symbolically in Sections 2-6 and are not inferred from the finite data.

## 9. Ledger delta

- proved lower bound: unchanged;
- booked upper bound: unchanged;
- exact target-retaining aggregate: newly constructed;
- best rigorous aggregate-height constant: $2/35$ per $M$, equal to
  the existing raw ceiling;
- strict capacity reduction: none;
- actual-formula mechanism closed: obtaining a saving solely by taking
  the known phase norm, adjoining the degenerate carrier, or packaging
  the common kernel and then applying matched-modulus saturation;
- remaining theorem: a genuine arithmetic estimate for
  $\log\mathfrak A_M^\sharp$, equivalently (6.2).

