> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 421 — post-booking small-prime primitive layer: normalized-carrier escape and the Cartier-tower method boundary

Date: 2026-09-01  
Status: **ROOT-AUDITED CANONICAL SCOPED METHOD NO-GO, NO BOOKING**

## 1. Verdict and capacity first

Retain Item 393's exact post-booking valuation, for (p\leq 6m),



$$
w_{m,p}=v_p(c_m)-\mathbf 1_{p=2}-\mathbf 1_{p\in\mathcal H_m},
 \tag{1.1}
$$



and Item 415's fully Cartier-normalized residue pair



$$
\mu_{s,m}=\lambda_{s,m}/F_m\in\mathbb Z,
 \qquad s=0,1,
 \tag{1.2}
$$



where (F_m=G_m) is canonical Item 200's squarefree rank-zero
Cartier product.  Put



$$
\tau_{m,p}=\min\{v_p(\mu_{0,m}),v_p(\mu_{1,m})\}.
 \tag{1.3}
$$



Item 415 and Item 418 use ((\mu_0,\mu_1)) as an exact all-depth carrier
only for (p>6m).  The most natural attempt on the complementary branch
would be to prove



$$
w_{m,p}\leq\tau_{m,p}
                         \qquad(p\leq6m),                \tag{1.4}
$$



or at least to divide an exact post-booking small-prime carrier by (F_m).
This item proves that both exact extensions are false in the actual family.

The decisive post-booking witness is



$$
(m,p)=(13,11).                  \tag{1.5}
$$



Here (11\in\mathcal P_{13}\cap\mathcal H_{13}), while



$$
v_{11}(c_{13})=2,
 \qquad
 v_{11}(\lambda_{0,13})=v_{11}(\lambda_{1,13})=1.
 \tag{1.6}
$$



Because (F_m) is squarefree, (1.6) gives



$$
w_{13,11}=1,
                    \qquad \tau_{13,11}=0.              \tag{1.7}
$$



Thus even the **second digit at a booked Item-149 prime** can lie outside
the normalized Item-415 residue carrier.  A second witness in the upper
small-prime strip is



$$
(m,p)=(9,47),\qquad
 47\in\mathcal P_9\setminus\mathcal H_9,
 \qquad w_{9,47}=1>0=\tau_{9,47}.                       \tag{1.8}
$$



There is an even more elementary de-overlap obstruction:



$$
F_2=11,\qquad c_2=288,\qquad 11\nmid c_2.              \tag{1.9}
$$



Hence the positive-rate Item-200 factor is a factor of the residue
coordinates, not an additional divisor of the already post-(G_m) content.
It cannot be subtracted from the small-prime remainder as it was from the
large auxiliary carrier.

Combining (1.7)--(1.9) with Item 417 gives a sharp scoped no-go:

> The package consisting only of exact (F_m)-normalization, arbitrary
> degree-zero Cartier iteration in characteristic (p), and multiplicity
> inferred from those mod-(p) rank data cannot lower Item 393's safe
> small-prime component ceiling.  The normalized pair misses actual
> post-booking digits; the de-overlapped higher-level Cartier support has
> zero linear mass; and mod-(p) rank data do not bound lift valuation.

This closes a method class, not the small-prime branch.  A genuine integral
Witt/Dwork endpoint carrier, a weighted support theorem, or another
cancellation-aware global argument remains possible.

The capacity screen is already restrictive.  After crediting Item 418's
strictly-large component at its entire ceiling, the admission residual is



$$
R_{\rm out}=0.590859098330773924934546018290\ldots .     \tag{1.10}
$$



A bare squarefree support ceiling (p\leq\alpha m) has prime-number-theorem
capacity $\alpha/6$.  Therefore it can fit below (1.10) only if



$$
\boxed{\alpha<6R_{\rm out}
 =3.545154589984643549607276109742\ldots .}              \tag{1.11}
$$



In particular, one full radical/lcm layer through (4m+O(1)) has ceiling



$$
\frac23
 =R_{\rm out}+0.075807568335892741732120648376\ldots,    \tag{1.12}
$$



and is not admission-decisive.  The full (p\leq6m) layer has ceiling
(1).  Consequently a useful Closer theorem must do more than show bounded
multiplicity or localization to the full clearing range: it must shrink the
weighted support below (1.11), couple it to an already bounded carrier, or
exploit cancellation between layers.

No ceiling is lowered here:



$$
\boxed{
 \Delta C_{\leq}=\Delta r_{\rm booked}
 =\Delta C_{\rm global}=\Delta(T-r_1)=0.}                \tag{1.13}
$$



## 2. Exact de-overlap

The three products in play have different roles.

1. Canonical Item 200 proves
   
   

$$
F_m=G_m\mid\lambda_{0,m},\lambda_{1,m}.
   \tag{2.1}
$$



2. The same (G_m) was already divided from the raw mixed-cubic
   determinants before (c_m=\gcd(U_m,V_m)) was defined.  It is therefore
   not a second content divisor.

3. Item 149 proves the genuinely post-(G_m) divisor

   

$$
\prod_{p\in\mathcal H_m}p\mid c_m,
   \tag{2.2}
$$



   and this one surviving copy, together with the deterministic dyadic
   copy, is precisely the baseline removed in (1.1).

Equation (1.9) makes the distinction concrete.  At (m=2), Item 200's
factor (11) divides both residue integers exactly once:



$$
(\lambda_{0,2},\lambda_{1,2})=(2475,6952),
 \qquad(v_{11}\lambda_{0,2},v_{11}\lambda_{1,2})=(1,1),
 \tag{2.3}
$$



but (11\nmid c_2).  Thus no exact inequality for the small remainder may
subtract $\log F_m$ merely because the same subtraction is valid for the
auxiliary large-prime residue carrier.

The failure is not repaired by passing to (\mu_s=\lambda_s/F_m).  For an
odd prime, (1.1) reads



$$
w_{m,p}=v_p(c_m)-\mathbf1_{p\in\mathcal H_m}.           \tag{2.4}
$$



At (1.5), the ordinary defects are



$$
d_{11}(78,53)=8,
 \qquad d_{11}(78,54)=5.                                \tag{2.5}
$$



They are at most (11-2), so (11\in\mathcal P_{13}); they are also at
most (2\cdot11-2), and (11<26), so
(11\in\mathcal H_{13}).  Exact arithmetic gives



$$
c_{13}=281943773540352,\qquad v_{11}(c_{13})=2,          \tag{2.6}
$$



while



$$
\begin{aligned}
 \mu_{0,13}&=1013436056682644,\\
 \mu_{1,13}&=2589444692394888,
\end{aligned}
\qquad
11\nmid\mu_{0,13}\mu_{1,13}.                            \tag{2.7}
$$



Equations (2.4)--(2.7) prove (1.7).  This is exactly the relevant
post-booking comparison: one Item-149 copy has already been credited, and
the surviving second copy is still invisible to the normalized pair.

For (1.8), the ordinary defects are



$$
d_{47}(54,37)=44,
 \qquad d_{47}(54,38)=41.                               \tag{2.8}
$$



Thus (47\in\mathcal P_9), but (47\notin\mathcal H_9) because
(47\not<18).  One has



$$
v_{47}(c_9)=1,\qquad
 (v_{47}\lambda_{0,9},v_{47}\lambda_{1,9})=(1,1),      \tag{2.9}
$$



so division by the one (F_9)-copy again yields (1.8).

These are exact actual-family counterexamples.  They refute the universal
carrier inequality (1.4), the divisibility



$$
c_{m,\leq}^{\rm rem}\mid\gcd(\mu_{0,m},\mu_{1,m}),      \tag{2.10}
$$



and every proposed small-prime height proof whose only bridge to (c_m) is
(2.10).  They do not refute an asymptotic comparison with a separately
proved exceptional-set estimate.

## 3. Why the all-level degree-zero tower does not repair the bridge

Item 417 defines the complete squarefree degree-zero Cartier tower.  After
removing the ordinary (F_m)-support, any new prime in that tower has a
witness at some level $p^e$ with $e\geq2$.  Therefore



$$
p\leq\sqrt{6m},
 \qquad
 \log E_m=O(\sqrt m\log m)=o(m).                        \tag{3.1}
$$



This has two exact consequences for the current branch.

* As a Builder divisor, the de-overlapped tower has zero linear-exponent
  capacity.
* As a Closer mechanism, it supplies divisibility of the residue pair, not
  an upper bound on the unclassified post-booking factor of (c_m).

Both escape primes in (1.7)--(1.8) already belong to $F_m$, whereas
Item 417 defines its extra product after deleting $F_m$.  Hence replacing
$\mu_s$ by the further normalized coordinates
$\lambda_s/(F_mE_m)$ leaves those two local depths equal to zero.  The
all-level squarefree normalization therefore cannot repair the failed
small-content carrier inequality.

Repeated witnessing levels do not change (3.1).  Cartier iteration is
nested:



$$
\mathcal C^{e_0}(\bar\omega)=0
 \Longrightarrow
 \mathcal C^e(\bar\omega)=0\quad(e\geq e_0).            \tag{3.2}
$$



Hence several true degree-zero statements after the first zero are not
independent (p)-adic digits.  Item 417 also supplies actual exact-one
rows, including the higher-level witness ((m,p)=(5,5)), so a level
(p^e) cannot be read as (e) copies of (p).

The information-theoretic limitation can be stated independently of any
finite scan.  Over (\mathbb Z_p^3), in coordinate order ((R,L,E)), set



$$
z_0=(1,1,1),\qquad z_1=(1+p^r,1,1+p^r).               \tag{3.3}
$$



For every (r\geq1), the two rows have the same nonzero reduction modulo
(p), but the two target minors are



$$
L_1R_0-L_0R_1=-p^r,\qquad
 L_1E_0-L_0E_1=-p^r.                                   \tag{3.4}
$$



Thus one and the same characteristic-(p) rank-one datum is compatible
with arbitrary common determinant valuation.  Since all degree-zero
Cartier iterates still live in characteristic (p), no valuation upper
bound follows from their rank record alone.

Equations (3.3)--(3.4) are an ambient information-class obstruction, not
an actual mixed-cubic counterfamily.  Their role is only to identify the
missing input: a useful theorem must incorporate an integral lift.  The
actual witnesses in Section 2 separately show that the simplest automatic
lift statements are false on the real family.

## 4. The admission threshold for a small-prime support theorem

Item 418's sharp centered-circle result gives the strictly-large component
ceiling



$$
C_>=0.428773885338657868945760382909\ldots .            \tag{4.1}
$$



The frozen deficit after the booked Item-149 mass is



$$
T-r_1=1.0196329836694317938803064012\ldots .            \tag{4.2}
$$



Their difference is the comparison residual (1.10).  This subtraction is
an admission comparison only; it is not a proved additive global ceiling.

Suppose a candidate theorem gives no information beyond squarefree support
at primes (p\leq\alpha m+O(1)).  The prime number theorem gives the raw
component ceiling



$$
\limsup\frac1{6m}\sum_{p\leq\alpha m+O(1)}\log p
 \leq\frac\alpha6.                                     \tag{4.3}
$$



For (4.3) even to fit below (R_{\rm out}), it is necessary that (1.11)
hold.  In particular:



$$
\frac{\vartheta(4m+O(1))}{6m}\longrightarrow\frac23
 >R_{\rm out},                                         \tag{4.4}
$$



and



$$
\frac{\vartheta(6m)}{6m}\longrightarrow1
 >R_{\rm out}.                                         \tag{4.5}
$$



An lcm-power estimate is weaker still.  If a residual carrier is bounded
only by (\operatorname{lcm}(1,\ldots,\alpha m)^k), its natural
Chebyshev ceiling is (k\alpha/6).  Already (k=1,\alpha=4) misses the
admission threshold by the positive amount in (1.12).  Therefore the
following conclusions, by themselves, are not strategically sufficient:

* support at all primes in the clearing range;
* squarefreeness on that whole range;
* a fixed positive lcm power; or
* a uniform finite valuation bound without weighted support thinning.

This is a capacity no-go, not a statement that the actual support saturates
these ceilings.  A zero-density theorem could make the true mass much
smaller than (4.3), and such a theorem remains a valid target.

## 5. Exact finite normalization census

The deterministic replay reconstructs every (\lambda_{s,m}), (F_m),
and exact content row for (1\leq m\leq100).  It records:

* 1,659 Item-200 prime incidences for which (p\mid F_m) but (p\nmid c_m);
* 468 incidences for which (w_{m,p}>\tau_{m,p});
* among those 468 escapes, 11 lie in
  (\mathcal P_m\cap\mathcal H_m), 18 in
  (\mathcal P_m\setminus\mathcal H_m), 120 in
  (\mathcal H_m\setminus\mathcal P_m), and 319 in neither set;
* a maximum observed gap (w_{m,p}-\tau_{m,p}=6).

These counts are exact checks of normalization and show that the displayed
witnesses are not transcription accidents.  They are **not** used to infer
frequency, density, or an asymptotic lower bound.

## 6. Strict claim ledger

### PROVED

* The exact actual-family counterexamples (1.7)--(1.9).
* Failure of the universal small-prime normalized-carrier inequality
  (1.4), including at a booked second digit.
* Exact de-overlap: Item-200 (F_m=G_m) is not an additional divisor of
  post-(G_m) content.
* The abstract arbitrary-lift-valuation model (3.3)--(3.4).
* The admission cutoff (1.11) and the full-clearing-layer excess (1.12).
* Zero change to every booked or ceiling quantity.

### INHERITED FROM ITEM 417

* The de-overlapped all-level degree-zero tower has support
  (p\leq\sqrt{6m}) and hence zero linear mass.
* Nested Cartier zeros do not constitute independent valuation digits.
* Actual exact-one rows refute automatic multiplicity from a higher
  prime-power level.

### SCOPED NO-GO

The combination of (F_m)-normalization, all-level characteristic-(p)
degree-zero tests, and lift multiplicity inferred from those tests does not
yield a smaller rigorous ceiling for the complete post-booking
(p\leq6m) primitive remainder.

### OPEN

* An integral first-error/Witt/Dwork endpoint carrier for (w_{m,p}).
* A weighted support theorem with effective cutoff below (1.11), or a
  nontrivial zero-density substitute.
* A cancellation-aware joint carrier coupling small and large content.
* A uniform upper bound for the aggregate post-booking depths (j\geq2).
* Route 1 and the irrationality of (e+\pi).

### NOT CLAIMED

* That the finite escape census has positive density.
* That every possible integral Cartier lift fails.
* That the true small-prime component has capacity (2/3) or (1).
* A new divisor, a reduced global ceiling, Route-1 closure, or an
  irrationality proof.

## 7. Deterministic replay

Run

```text
python scripts/item421_small_prime_primitive_layer_certificate.py \
  --output results/item421_small_prime_primitive_layer_certificate_replay.json \
  --replay results/item421_small_prime_primitive_layer_certificate.json
```

The standard-library replay:

1. pins canonical Items 149, 200, 393, 415, and 418, together with the
   completed work Item 417;
2. reconstructs $F_m$ and the two exact residue integers from their
   coefficient formulas;
3. verifies all displayed memberships, valuations, and integer hashes;
4. reproduces the finite normalization census and its stream hashes;
5. checks the arbitrary-lift-valuation model; and
6. verifies the capacity arithmetic with exact decimal input from Item 418.

The canonical report, replay script, certificates, manifest, ledger delta,
root audit, and hash inventory are stored under `sources/`, `scripts/`,
`results/`, and `manifests/`.
