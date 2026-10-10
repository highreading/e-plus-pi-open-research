> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 397 — ordinary-$j=2$ matched-aggregate factor localization

Checked: 2026-09-01 (Beijing time)

## 1. Scope and outcome

Item 394 constructed the exact target-retaining fixed-$M$ aggregate



$$
\mathfrak A_M^\sharp
 =\prod_{\substack{p\in I_M\\p\text{ an actual collision}}}p,
\qquad
 I_M=\left[\frac{4M+3}{5},\frac{6M-1}{7}\right],
\tag{1.1}
$$



from the matched factors



$$
d_{M,q}=\operatorname{rad}
 \gcd(q,\widehat{\mathfrak G}_{M,q}).
\tag{1.2}
$$



This item attacks the height of (1.1).  No strict saving is obtained.
Instead, the complete factor localization proves exactly why the
unsaturated $0.124449\ldots$ envelope collapses to, and only to, the
raw $2/35$ ceiling under the presently available operations.

> **PROVED — exact envelope decomposition.**  Item 394's constant is
> 

$$
> C_6=\frac{2}{35}+C_{\rm comp},
> \tag{1.3}
>
$$


> where
> 

$$
> \boxed{
> C_{\rm comp}
> =\frac{3774576680099633199868}
> {56080510212831201972875}
> =0.06730638979165371\ldots .}
> \tag{1.4}
>
$$


> The first term is exactly the $u=1$ prime-row component.  Every
> $u\geq5$ component is supported below the row interval and is
> removed by Item 394's safe $(L_M-1)!$-saturation.

> **PROVED — atomic high-prime localization.**  If
> 

$$
> d_{M,q}^\sharp=(d_{M,q})_{((L_M-1)!)},
> \tag{1.5}
>
$$


> then
> 

$$
> \boxed{
> d_{M,q}^\sharp=
> \begin{cases}
> q,&q\text{ is prime and its actual row collides},\\
> 1,&\text{otherwise}.
> \end{cases}}
> \tag{1.6}
>
$$


> For distinct rows $q\ne q'$,
> 

$$
> \boxed{\gcd(d_{M,q}^\sharp,d_{M,q'}^\sharp)=1.}
> \tag{1.7}
>
$$



> **PROVED — pairwise matched-gcd no-go.**  Before saturation,
> 

$$
> \gcd(d_{M,q},d_{M,q'})
> \mid\gcd(q,q')\mid |q-q'|<L_M.
> \tag{1.8}
>
$$


> Hence every shared factor of two different matched rows is low-prime
> support and is annihilated by (1.5).  Inclusion-exclusion, pairwise
> gcd reuse, or a resultant whose only arithmetic input is a shared
> matched divisor has zero high-prime overlap to exploit.

> **PROVED — no reciprocity-only ray saving.**  The actual endpoint
> phase equation is locally admissible on both prime rays.  For
> $r\equiv1\pmod6$, cubing is bijective and the selected phase is the
> unique cube root of $1/2$.  For $r\equiv5\pmod6$, the selected
> phase is one of the three cube roots of unity.  Thus the known cubic
> reciprocity data exclude neither ray and supply no positive
> Chebyshev-mass saving without using the moving coefficients and
> target residual.

The numerical effect is



$$
\begin{array}{c|c|c}
\text{support}&\text{per }M&\text{per }6M\\ \hline
\text{unsaturated envelope}&
0.12444924693451084\ldots&
0.020741541155751806\ldots\\
\text{composite-row support removed}&
0.06730638979165371\ldots&
0.011217731631942283\ldots\\
\text{atomic prime-row remainder}&
2/35&1/105.
\end{array}
\tag{1.9}
$$



The removed $C_{\rm comp}$ was never bookable collision capacity.
The remaining prime-row atoms are exactly (1.1).  Therefore the strict
saving proved here is



$$
\boxed{\eta=0},\qquad
 \boxed{\Delta\text{ capacity}=0},\qquad
 \boxed{\text{retained ceiling}=1/105}.
\tag{1.10}
$$



This is a precise obstruction for factor-overlap and reciprocity-only
attacks on the exact matched aggregate.  It does not rule out a new
cross-row congruence involving unmatched carrier values, nor direct
nonconcentration of the moving target.

## 2. The narrow interval forces large factors to be row labels

Retain Item 394's integer-row set



$$
\mathcal Q_M=\{q:L_M\leq q\leq U_M,\ (q,6)=1\},
\tag{2.1}
$$



where



$$
L_M=\left\lceil\frac{4M+3}{5}\right\rceil,\qquad
 U_M=\left\lfloor\frac{6M-1}{7}\right\rfloor.
\tag{2.2}
$$



The interval satisfies



$$
U_M<2L_M.
\tag{2.3}
$$



Let $\lambda\geq L_M$ be prime and suppose
$\lambda\mid q\in\mathcal Q_M$.  If $q\ne\lambda$, then
$q\geq2\lambda\geq2L_M>U_M$, a contradiction.  Thus



$$
\boxed{\lambda\mid q,\ \lambda\geq L_M
 \Longrightarrow q=\lambda.}
\tag{2.4}
$$



Since $d_{M,q}\mid q$, every factor surviving (1.5) is its row label,
and that row label is prime.  Item 394's exact carrier equivalence then
gives (1.6).

For distinct $q,q'$, (1.2) gives



$$
\gcd(d_{M,q},d_{M,q'})\mid\gcd(q,q').
\tag{2.5}
$$



Moreover, $\gcd(q,q')\mid |q-q'|$, while



$$
|q-q'|\leq U_M-L_M<L_M.
\tag{2.6}
$$



Equations (2.5)-(2.6) prove (1.8); saturation by all primes below
$L_M$ proves (1.7).

This is stronger than saying that the aggregate is squarefree.  It says
the high-prime part has no cross-row common factor at all:



$$
\mathfrak A_M^\sharp
 =\prod_{q\in\mathcal Q_M}d_{M,q}^\sharp
 =\operatorname{lcm}_{q\in\mathcal Q_M}d_{M,q}^\sharp.
\tag{2.7}
$$



Consequently the usual inequality



$$
\log\operatorname{lcm}(d_q)
 \leq\sum_q\log d_q
\tag{2.8}
$$



becomes equality after high-prime saturation.  There is no pairwise
overlap term left from which to obtain a strict constant saving.

## 3. Where the $0.124449\ldots$ envelope goes

Item 394 bounded the unsaturated aggregate by



$$
\Lambda_M=\operatorname{rad}
 \operatorname{lcm}\{q:q\in\mathcal Q_M\},
\qquad
\log\Lambda_M=C_6M+o(M).
\tag{3.1}
$$



A prime $\lambda$ belongs to this envelope when



$$
\lambda u\in[\alpha M+O(1),\beta M+O(1)],
\qquad
\alpha=\frac45,\quad\beta=\frac67,\quad(u,6)=1.
\tag{3.2}
$$



The cofactor $u=1$ gives precisely the candidate prime interval



$$
\lambda/M\in(\alpha,\beta],
\tag{3.3}
$$



of measure



$$
\beta-\alpha=\frac2{35}.
\tag{3.4}
$$



Every other allowed cofactor satisfies $u\geq5$, hence



$$
\lambda\leq\frac{\beta M+O(1)}5
 =\frac6{35}M+O(1)<L_M.
\tag{3.5}
$$



Thus all $u\geq5$ components lie in the support of
$(L_M-1)!$ and are removed.  Conversely no $u=1$ prime in
$I_M$ is removed.  The component union in Item 394 therefore
decomposes disjointly as



$$
\mathcal U=(\alpha,\beta]\ \dot\cup\ \mathcal U_{\rm comp},
\tag{3.6}
$$



and



$$
|\mathcal U_{\rm comp}|=C_6-\frac2{35}=C_{\rm comp}.
\tag{3.7}
$$



Substitution of Item 394's exact rational $C_6$ gives (1.4).
This accounts for every bit of the envelope constant: about
$54.0834\%$ is composite-row small-prime support, and the remaining
$45.9166\%$ is the prime-row interval itself.

## 4. Exact obstruction to pairwise-resultant reuse

Suppose a proposed pairwise construction uses two actual matched row
factors and can retain a prime only when that prime divides both factors.
By (1.8), every such prime is below $L_M$, so its contribution is
removed by the same saturation that defines the collision aggregate.
This includes:

1. pairwise gcd or radical-gcd corrections to (2.8);
2. common-divisor resultants formed from the two integer matched factors;
3. reuse of a prime factor across any finite graph of distinct matched
   rows; and
4. higher intersections, since every higher common divisor is already a
   pairwise common divisor.

The statement is deliberately scoped to **matched** factors.  A
resultant involving the full unmatched values
$\widehat{\mathfrak G}_{M,q}$ and
$\widehat{\mathfrak G}_{M,q'}$ could contain the selected prime of
only one row.  To affect (1.1), however, one would need a new theorem
showing that an actual collision at $q=p$ forces such an unmatched
divisibility at another row.  Items 385 and 392 show that this is not
supplied by bounded or sublogarithmic prime-row propagation.  It remains
an open cross-characteristic arithmetic input.

Thus pairwise resultants are not ruled out by name; the exact missing
bridge is identified.

## 5. The known cubic reciprocity data do not remove a ray

On an actual row put



$$
p=2r+6s+3.
\tag{5.1}
$$



Item 315's selected endpoint phase has the following two exact forms.

### 5.1 The $r\equiv1\pmod6$ ray

Let



$$
k=\frac{2r+1}{3},\qquad t=2^{k+2s}.
\tag{5.2}
$$



Then $p\equiv5\pmod6$ and



$$
t^3=\frac12\pmod p.
\tag{5.3}
$$



Since $\gcd(3,p-1)=1$, cubing is bijective on
$\mathbb F_p^\times$.  Equation (5.3) has exactly one solution for
every prime on this ray, and the actual power of $2$ is that solution.

### 5.2 The $r\equiv5\pmod6$ ray

Let



$$
k=\frac{2r+2}{3},\qquad t=2^{k+2s}.
\tag{5.4}
$$



Now $p\equiv1\pmod6$ and



$$
t^3=1\pmod p.
\tag{5.5}
$$



Thus the actual phase always lies in $\mu_3(\mathbb F_p)$.  The value
of the cubic character of $2$ selects a component but never makes the
phase equation insoluble.

The two rays each have prime mass



$$
\frac1{35}M+o(M)
\tag{5.6}
$$



by the prime number theorem in progressions.  Excluding one entire ray
would give $\eta=1/35$ per $M$, or a normalized improvement
$1/210$.  Equations (5.3) and (5.5) prove that the known endpoint
reciprocity does not do so.  Item 315's exact selected-component examples
on both rays also rule out declaring one displayed norm component
universally foreign.

A reciprocity theorem correlated with the moving coefficients
$(a_r,b_r)$ or with Item 334's second target could still succeed.
The phase relation alone cannot.

## 6. Capacity and admission decision

The exact aggregate factorization is



$$
\log\mathfrak A_M^\sharp
 =\sum_{q\in\mathcal Q_M}\log d_{M,q}^\sharp.
\tag{6.1}
$$



Every nontrivial summand is a different candidate prime.  Hence a strict
bound



$$
\log\mathfrak A_M^\sharp
 \leq\left(\frac2{35}-\eta\right)M+o(M)
\tag{6.2}
$$



requires an actual theorem proving that a subset of candidate prime rows
of logarithmic mass at least $\eta M$ has
$d_{M,p}^\sharp=1$.  Factor overlap cannot supply $\eta$, and the
known local phase relation supplies no excluded congruence class.

Therefore this item records



$$
\boxed{\eta_{\rm proved}=0.}
\tag{6.3}
$$



The smallest live inputs are now sharply separated:

- a one-row nonvanishing theorem on a positive-mass subfamily;
- a genuine cross-row implication using unmatched actual carrier values;
- a reciprocity law involving the moving coefficient component, not only
  the automatically soluble phase equation; or
- a direct weighted-density estimate for (6.1).

## 7. Deterministic certificate and evidence labels

The certificate verifies:

- the frozen Item 394 construction and dependencies;
- the exact rational decomposition $C_6=2/35+C_{\rm comp}$;
- the $u=1$ versus $u\geq5$ support separation;
- atomic row factors, pairwise gcd localization, and exact lcm/product
  equality on declared actual-formula slices;
- the two endpoint phase identities on declared rows from both rays; and
- byte-identical replay.

All enumerated rows, carrier values, and phase examples are labelled
**EXACT FINITE ONLY / DIAGNOSTIC**.  The all-$M$ localization,
constant decomposition, and phase-solvability statements are proved in
Sections 2-5 and are not extrapolated from those data.

## 8. Ledger delta

- proved $\eta$: $0$;
- booked lower bound: unchanged;
- ordinary-$j=2$ shared ceiling: unchanged at $1/105$;
- closed mechanism: strict saving from overlap among pairwise matched
  factors, including higher common-divisor reuse;
- closed local mechanism: excluding a whole ray from the known endpoint
  cubic phase equation alone;
- exact explanation of the envelope collapse: $C_{\rm comp}$ is
  entirely low-prime composite-row support, while $2/35$ is the atomic
  prime-row support;
- remaining work: arithmetic nonvanishing or cross-row correlation of
  the actual moving target-retaining carrier.

