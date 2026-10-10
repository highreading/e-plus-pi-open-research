> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 305 — exact small-residue continuant classification and multiplier no-go

Checked: 2026-08-31 (Beijing time)

## 1. Capacity-first verdict

Use the continuant convention



$$
K(\varnothing)=1,
\qquad
K(z_1,\ldots,z_j)
=z_jK(z_1,\ldots,z_{j-1})+K(z_1,\ldots,z_{j-2}).
\tag{1.1}
$$



Put



$$
w_1=7,
\qquad
w_j=4j+2\quad(j\ge2),
\qquad
m=n-2,
\tag{1.2}
$$



and define



$$
a=K(w_1,\ldots,w_m),\qquad
c=K(w_1,\ldots,w_{m-1}),\qquad
S=K(w_2,\ldots,w_m).
\tag{1.3}
$$



For $1\le k<m$, let



$$
Q_k=K(w_1,\ldots,w_k),\qquad
P_k=K(w_2,\ldots,w_k),\qquad
D_k=K(w_{k+2},\ldots,w_m),
\tag{1.4}
$$



where $P_1=K(\varnothing)=1$.

Item 305 proves the exact classification behind the proposed
continued-fraction window.  If



$$
1\le R<\frac{a}{2c}
\tag{1.5}
$$



and, for a sign $\sigma\in\{\pm1\}$, the positive residue



$$
\kappa\equiv \sigma RS\pmod a,
\qquad 0<\kappa<c,
\tag{1.6}
$$



exists, then for a unique convergent index $1\le k<m$ and an integer
$g\ge1$,



$$
\boxed{
R=gQ_k,
\qquad
\kappa=gD_k,
\qquad
\sigma=(-1)^k.}
\tag{1.7}
$$



Conversely, every pair $g,k$ satisfying



$$
gQ_k<\frac{a}{2c},
\qquad
gD_k<c
\tag{1.8}
$$



produces (1.6) with $\sigma=(-1)^k$.

The multiplier $g$ is essential.  There are two explicit infinite
families proving that neither of the shortcuts



$$
R\text{ must itself equal some }Q_k,
\qquad
Q_k<\frac{a}{2c}\Longrightarrow D_k\ge c
\tag{1.9}
$$



is true.  Thus Legendre's convergent criterion does not prove the desired
centered half-bound.  New information fixing the actual nearest quotient,
or otherwise excluding the multipliers $g$, is required.

This result closes one proposed modular-square/Ostrowski shortcut, not the
entire modular-square or Ostrowski branch.  It proves neither the actual
half-bound nor a proper-target construction.  Therefore



$$
\boxed{
\text{new Route-1 rate}=0,
\qquad
\text{new beta capacity reduction}=0.}
\tag{1.10}
$$



## 2. Euler continuant identity

The rational number



$$
\frac Sa=[0;w_1,w_2,\ldots,w_m]
\tag{2.1}
$$



has convergents $P_k/Q_k$.  Splitting the continuant word at $k$, or
equivalently taking the determinant of the corresponding two matrix
products, gives



$$
\boxed{
Q_kS-P_ka=(-1)^kD_k.}
\tag{2.2}
$$



This is Euler's continuant identity in the exact orientation needed here.
All coefficients are positive.  Moreover



$$
S=K(w_2,\ldots,w_m)>K(w_1,\ldots,w_{m-1})=c,
\tag{2.3}
$$



because the two words have the same length and every coefficient in the
first is strictly larger than the corresponding coefficient in the second.

## 3. Exact dual-window classification

Assume (1.5)--(1.6), and write



$$
\sigma RS=pa+\kappa,
\qquad
\widetilde p=\sigma p.
\tag{3.1}
$$



Then



$$
\left|\frac Sa-\frac{\widetilde p}{R}\right|
=\frac{\kappa}{aR}
<\frac{c}{aR}
<\frac1{2R^2}.
\tag{3.2}
$$



The residue cannot vanish: since $\gcd(S,a)=1$, the divisibility
$a\mid RS$ with $R<a$ is impossible.  The numerator
$\widetilde p$ also cannot be zero, because that would give
$\kappa=RS\ge S>c$.

Let



$$
g=\gcd(\widetilde p,R),
\qquad
\frac{\widetilde p}{R}=\frac PQ
\tag{3.3}
$$



in lowest terms.  Since $Q\le R$, (3.2) is stronger than



$$
\left|\frac Sa-\frac PQ\right|<\frac1{2Q^2}.
\tag{3.4}
$$



Legendre's theorem therefore makes $P/Q$ a convergent of $S/a$.
The initial $0/1$ convergent was excluded above, and the terminal
convergent has denominator $a>R\ge Q$.  Hence



$$
\frac PQ=\frac{P_k}{Q_k}
\quad\text{for a unique }1\le k<m.
\tag{3.5}
$$



It follows that



$$
R=gQ_k,
\qquad
\widetilde p=gP_k.
\tag{3.6}
$$



Combining (3.1), (3.6), and (2.2) yields



$$
\sigma\kappa
=RS-\widetilde p\,a
=g(Q_kS-P_ka)
=(-1)^kgD_k.
\tag{3.7}
$$



Since $\kappa,D_k>0$, this proves (1.7).  Reversing the calculation proves
the converse (1.8).  In the Item-302 centered-residue notation, where
$\sigma=(-1)^n\operatorname{sgn}(r)$, the compatible sign is equivalently



$$
\operatorname{sgn}(r)=(-1)^{n+k}.
\tag{3.8}
$$



## 4. Infinite multiplier counterfamily

Fix any $k\ge1$, and choose



$$
n=Q_k+2,
\qquad
m=Q_k.
\tag{4.1}
$$



The terminal coefficient is



$$
B=w_m=4Q_k+2.
\tag{4.2}
$$



Set



$$
E=K(w_{k+2},\ldots,w_{m-1}).
\tag{4.3}
$$



The right recurrence and the word-concatenation identity give



$$
D_k
=BE+K(w_{k+2},\ldots,w_{m-2})
<(B+1)E,
\tag{4.4}
$$



and



$$
c
=Q_{k+1}E+Q_kK(w_{k+3},\ldots,w_{m-1})
>Q_{k+1}E.
\tag{4.5}
$$



Because



$$
Q_{k+1}=w_{k+1}Q_k+Q_{k-1}
>8Q_k+6
=2(B+1),
\tag{4.6}
$$



one has



$$
2D_k<c.
\tag{4.7}
$$



Also $a=Bc+K(w_1,\ldots,w_{m-2})>Bc$, so



$$
\frac{a}{2c}>\frac B2=2Q_k+1.
\tag{4.8}
$$



Consequently



$$
R=2Q_k<\frac{a}{2c},
\qquad
\kappa=2D_k<c
\tag{4.9}
$$



is compatible.  Yet every prefix denominator is odd: $Q_0=1,Q_1=7$,
and thereafter the recurrence has an even coefficient.  Thus $2Q_k$ is
not any $Q_j$.  This disproves the denominator-only classification for
infinitely many $n$.

The first instance is



$$
k=1,quad n=9,quad
a=312129649,quad c=10391023,quad D_1=4365570.
\tag{4.10}
$$



Here



$$
R=14<\frac{a}{2c}=15.019\ldots,
\qquad
\kappa=8731140<c.
\tag{4.11}
$$



## 5. Infinite tail-bound counterfamily

Again fix $k\ge1$, but now choose



$$
n=\frac{Q_k+3}{2},
\qquad
m=\frac{Q_k-1}{2}.
\tag{5.1}
$$



This is integral because $Q_k$ is odd, and $m>k+1$.  The terminal
coefficient is



$$
B=w_m=2Q_k.
\tag{5.2}
$$



As before,



$$
\frac{a}{2c}>\frac B2=Q_k,
\tag{5.3}
$$



whereas



$$
D_k<(B+1)E=(2Q_k+1)E<Q_{k+1}E<c.
\tag{5.4}
$$



Thus the condition $Q_k<a/(2c)$ holds while $D_k<c$, for every
$k\ge1$.  The proposed implication $D_k\ge c$ is therefore false in an
infinite exact family.

## 6. Scope and admission

The theorem is structural and uses no finite scan.  Bounded rows in the
checker replay (2.2), the exact classification, the two infinite-family
inequalities at initial indices, and the concrete $k=1$ instance.  Those
rows are labelled EXACT FINITE ONLY; the infinite statements themselves are
proved symbolically in Sections 3--5.

What is closed:

1. Legendre's theorem cannot delete the multiplier $g$.
2. The small-$R$ threshold does not force $D_k\ge c$.
3. Those two claims cannot establish the centered half-bound.

What remains open:

1. a seed-specific restriction on the actual nearest quotient or multiplier;
2. a different modular-square or Ostrowski invariant;
3. the actual half-bound and the stronger Item-295 window;
4. transfer to proper de-overlapped targets; and
5. the Item-282 product baseline.

No new positive linear exponent enters the Route-1 ledger.
