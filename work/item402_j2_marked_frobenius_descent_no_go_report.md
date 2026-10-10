> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 402 — marked-Frobenius descent obstruction on the ordinary-$j=2$ rays

Checked: 2026-09-01 (Beijing time)

## 1. Capacity first and verdict

Item 399 isolates the actual nondegenerate collision as the selected-prime
ideal



$$
p\mid E_{p,r,s},\qquad \mathfrak P_p\mid\Xi_{p,r,s},
\tag{1.1}
$$



where $\mathfrak P_p$ is the Teichmuller-selected prime of
$K_p=\mathbb Q(\mu_{p-1})$, and $\Xi_{p,r,s}$ retains the ordered
incomplete-beta cutoff.  Item 349 separately isolates the degenerate chart.

The two prime rays each have Chebyshev mass



$$
\frac1{35}M+o(M).
\tag{1.2}
$$



Thus a theorem making the **whole** collision mass on one ray $o(M)$
would improve the normalized ordinary-$j=2$ ceiling by



$$
\boxed{\frac1{210}}.
\tag{1.3}
$$



No such theorem is proved here.  Instead this item closes a precise and
larger information class than the ordinary norm treated in Item 399.

> **PROVED — trivial stabilizer of the actual ordered cutoff.**  On every
> positive-rate row with $m\geq1$, the subset
> $S_m=\{0,1,\ldots,m\}\subset\mathbb Z/(p-1)\mathbb Z$ has trivial
> stabilizer under $(\mathbb Z/(p-1)\mathbb Z)^\times$.

> **PROVED — no proper formal Kummer-mode descent preserving the cutoff.**
> In the exact mode-labelled category of Items 347 and 399, any descent to
> a proper subfield identifies at least two distinct multiplicatively
> permuted cutoffs.  An exact descent retaining the formal ordered-cutoff
> support therefore has field of definition $K_p$ itself.  This does not
> rule out an accidental formula-specific equality among evaluated
> conjugates.

> **PROVED — complete invariant-information no-go.**  Relative trace,
> relative norm, every collection of elementary symmetric functions,
> Frobenius characteristic polynomials, Newton-slope multisets, and in
> fact the entire ring of unmarked Galois-invariant functions fail to
> determine whether the **selected** coordinate vanishes.  This is proved
> by exact split-cyclotomic Chinese-remainder countermodels, not by a
> finite search.

> **PROVED — unit-root dichotomy.**  An unmarked unit-root or Frobenius
> packet falls under the preceding no-go.  A coordinate marked at
> $\mathfrak P_p$ does retain the selector, but then it is exactly the
> chosen-prime object still requiring the open nonconcentration theorem;
> it is not a rational or proper-subfield compression.

The result does not show that the actual values $\Xi_{p,r,s}$ realize
the abstract countermodels.  Its conclusion is the logically correct
one: no theorem using only the stated invariant information can prove the
selected-prime condition without an additional formula-specific relation
among conjugate cutoffs.

The degenerate Item-349 chart is independent of this obstruction and is
not bounded here.  Consequently



$$
\boxed{\eta=0},\qquad
 \boxed{\Delta\text{ capacity}=0},\qquad
 \boxed{\text{ordinary-}j=2\text{ ceiling}=1/105}.
\tag{1.4}
$$



No prime census is used.

## 2. The cutoff has trivial multiplicative stabilizer

Put



$$
N=p-1=6m+2r+8,
 \qquad S_m=\{0,1,\ldots,m\}\subset\mathbb Z/N\mathbb Z.
\tag{2.1}
$$



The actual phase gives



$$
N>6(m+1)>2m.
\tag{2.2}
$$



### Theorem 2.1

If $m\geq1$, $N>2m$, and
$aS_m=S_m$ for a unit $a\pmod N$, then $a=1\pmod N$.

#### Proof

Let $A\in\{1,\ldots,N-1\}$ be the least positive residue of $a$.
Since $1\in S_m$ and $aS_m=S_m$, one has $1\leq A\leq m$.
If $A\geq2$, put



$$
k=\left\lfloor\frac mA\right\rfloor+1.
\tag{2.3}
$$



Then $1\leq k\leq m$, while



$$
m<Ak\leq m+A\leq2m<N.
\tag{2.4}
$$



Thus $ak\pmod N=Ak\notin S_m$, a contradiction.  Hence $A=1$.
$\square$

The $m=0$ edge has no ordered-prefix content to distinguish.  Item 344
already proves that every sublinear-$m$ edge has zero logarithmic rate,
so it cannot carry the positive mass at issue here.

By Item 347, the modes indexed by $S_m$ are distinct Kummer
constituents.  Therefore Theorem 2.1 implies that the formal
ordered-cutoff **support** has Galois orbit of exact size



$$
\boxed{\varphi(N)}.
\tag{2.5}
$$



The rational moving target is fixed by Galois and does not enlarge the
support stabilizer.  The evaluated residual itself could have a smaller
orbit only through an additional formula-specific coincidence; no such
coincidence is asserted or excluded here.

## 3. Exact proper-subfield descent theorem

Let



$$
G=\operatorname{Gal}(K_p/\mathbb Q)
 \cong(\mathbb Z/N\mathbb Z)^\times,
\tag{3.1}
$$



and let $H\leq G$.  Write $L=K_p^H$.  For $h\in H$, Item 399's
exact action sends the cutoff $S_m$ to $hS_m$.  If $H\ne\{1\}$,
Theorem 2.1 supplies an $h$ for which $hS_m\ne S_m$.

Consequently the usual descents are orbit aggregates:



$$
\operatorname{Tr}_{K_p/L}(\Xi)=\sum_{h\in H}\sigma_h(\Xi),
 \qquad
 \operatorname{N}_{K_p/L}(\Xi)=\prod_{h\in H}\sigma_h(\Xi).
\tag{3.2}
$$



The same is true of the coefficients of the relative characteristic
polynomial.  They are symmetric functions of the distinct cutoff
coordinates.  Thus every proper descent mixes the actual cutoff with at
least one different cutoff.

Equivalently, an exact mode-preserving descent retains $S_m$ only if



$$
H\subseteq\operatorname{Stab}_G(S_m)=\{1\}.
\tag{3.3}
$$



Hence the field of definition of the formal mode-labelled object is the
full $K_p$.  This is stronger than the statement that one displayed
rational norm is too large: no proper intermediate field preserves the
formal ordered prefix at all.  It is not an absolute field-of-definition
claim for a numerical specialization that might satisfy extra identities.

## 4. Split-cyclotomic local theorem

Because $N=p-1$, the prime $p$ splits completely in $K_p$.  Thus



$$
\mathcal O_{K_p}/p\mathcal O_{K_p}
 \cong\prod_{a\in G}\mathbb F_p.
\tag{4.1}
$$



Index the coordinates so that $a=1$ is reduction at the selected
prime $\mathfrak P_p$.  If $x_a$ denotes the coordinate of an
algebraic integer $x$, then for the prime of $L=K_p^H$ below
$\mathfrak P_p$,



$$
\operatorname{N}_{K_p/L}(x)\equiv\prod_{h\in H}x_h,
 \qquad
 \operatorname{Tr}_{K_p/L}(x)\equiv\sum_{h\in H}x_h.
\tag{4.2}
$$



Therefore



$$
x_1=0\Longrightarrow \operatorname{N}_{K_p/L}(x)=0,
\tag{4.3}
$$



but the converse says only that $x_h=0$ for **some** $h\in H$.
Trace has not even this one-way zero implication.

The loss is unavoidable for the whole invariant information class.
Choose $1\ne h_0\in H$.  By the Chinese remainder theorem there is
an algebraic integer $\alpha$ whose residue tuple has



$$
\alpha_1=0,\qquad \alpha_{h_0}=1,
\tag{4.4}
$$



with arbitrary fixed unit values in the other coordinates.  Put
$\beta=\sigma_{h_0}(\alpha)$.  Then



$$
\alpha_1=0,\qquad \beta_1=1,
\tag{4.5}
$$



while $\alpha$ and $\beta$ lie in the same $H$-orbit.  Hence



$$
F(\alpha)=F(\beta)
\tag{4.6}
$$



for **every** $H$-invariant function $F$.  This includes the entire
invariant ring, not merely trace and norm.  Taking the same rational
integer $E$, even with $p\mid E$, for both models proves that adjoining
Item 399's first rational coordinate does not restore the lost selector.

The construction can be made modulo $p^2$, with one coordinate of
valuation exactly one and all others units.  Its conjugate has the same
valuation multiset and the same Newton polygon, but the positive-valuation
coordinate is no longer the selected one.  Thus unmarked slope and
unit-root data have the same defect.

This is an information-class theorem.  It does not assert that arbitrary
CRT tuples arise from the actual $\Xi_{p,r,s}$.  A successful theorem
must add precisely such an actual-formula restriction.

## 5. Consequence for trace, norm, and unit-root proposals

The preceding theorem gives the following exact screening rule.

1. A rational trace can cancel even when the selected coordinate
   vanishes, so it is not a necessary divisor.
2. A relative or rational norm gives a necessary divisor, but replaces
   the selected condition by an existential union over conjugate cutoffs.
3. A Frobenius characteristic polynomial or Newton polygon retains only
   an unordered packet.  It records how many coordinates are nonunits,
   not whether $\mathfrak P_p$ is one of them.
4. A unit-root coordinate marked at $\mathfrak P_p$ does retain the
   condition.  Such a marked object is not a descent: it is the live
   chosen-prime invariant of Item 399, and it still needs a uniform
   nonconcentration theorem.

Accordingly, no further unmarked trace/norm/symmetric/unit-root
compression should be admitted as a Builder branch unless it proves an
actual relation making all conjugate cutoffs equivalent or proves that
the selected prime is intrinsically characterized inside the packet.

## 6. The degenerate chart prevents a full-ray booking

The selected residual $\Xi_{p,r,s}$ belongs to Item 341's
$\ell_r\ne0$ chart.  Item 349 shows that the complementary chart is
controlled by the independent triple-minor carrier



$$
p\mid\Pi^{\rm sat}_{r,s},
\tag{6.1}
$$



together with the surviving target coordinate.  Nothing in Sections
2–5 bounds (6.1).

Let $W_e^{\rm nd}(M)$ and $W_e^{\rm deg}(M)$ be the collision masses
on one ray.  Even a hypothetical proof



$$
W_e^{\rm nd}(M)=o(M)
\tag{6.2}
$$



would leave



$$
W_e^{\rm deg}(M)\leq\frac1{35}M+o(M).
\tag{6.3}
$$



Thus it would yield no fixed full-ray saving without a complementary
degenerate bound.  Conversely, a degenerate-only theorem has the same
problem with the nondegenerate chart.  The exact $1/210$ gain requires
control of their union.

## 7. Admission decision and remaining live inputs

**Closed as sufficient by itself:**

- rational or proper-subfield trace/norm of the chosen-prime residual;
- any finite or complete collection of unmarked symmetric conjugacy
  invariants;
- an unmarked Frobenius polynomial, Newton polygon, or unit-root packet;
- proper-field descent claimed to preserve the actual ordered cutoff; and
- a theorem on only the nondegenerate chart with no degenerate estimate.

**Still live:**

- a marked $\mathfrak P_p$-adic Frobenius coordinate with a genuine
  weighted nonconcentration theorem;
- an actual formula tying all conjugate cutoffs to the selected one;
- a direct one-ray theorem for Item 399's selected ideal;
- an exact good-reduction or moving-divisor upper bound for the Item-349
  degenerate carrier; and
- a theorem controlling the union of both charts on one complete ray.

The strongest numerical reward available from the last item is still
$1/210$ per $6M$.  This report proves no positive fraction of it.

## 8. Deterministic certificate and strict labels

The deterministic certificate verifies the frozen Items 349, 397, and
399 dependencies, the exact capacity arithmetic, the cutoff-stabilizer
argument on declared algebraic identity instances, and split-algebra
countermodels for relative symmetric and valuation-multiset data.  These
instances replay the symbolic constructions; they are not a prime or
collision census.

**PROVED:** Theorems 2.1, (3.3), the split-cyclotomic invariant-ring
countermodel, the marked/unmarked unit-root dichotomy, and the capacity
zero conclusion for this information class.

**EXACT FINITE ONLY / DIAGNOSTIC:** declared group and split-algebra
replays in the certificate.

**OPEN:** every actual weighted exclusion, the degenerate moving-divisor
theorem, a positive $\eta$, Route 1, and every conclusion about
$e+\pi$.
