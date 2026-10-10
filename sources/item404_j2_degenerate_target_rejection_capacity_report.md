> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 404 — the ordinary-$j=2$ degenerate target gate and sharp ray-capacity criterion

Checked: 2026-09-01 (Beijing time)

## 1. Capacity first and verdict

Retain the actual ordinary-$j=2$ rows



$$
p=2r+6s+3,
 \qquad r=6M-7p,
 \qquad s=\frac{5p-4M-1}{2},
 \qquad r\equiv e\pmod 6,
 \quad e\in\{1,5\}.
\tag{1.1}
$$



For either ray, Item 399 gives the raw Chebyshev mass



$$
R_e(M)=\frac1{35}M+o(M).
\tag{1.2}
$$



Thus one complete ray has normalized capacity



$$
\boxed{\frac1{6}\frac1{35}=\frac1{210}}.
\tag{1.3}
$$



Item 397 proves that the safely saturated prime-row factors are atomic,
so a strict improvement must exclude actual prime rows rather than reuse
high-prime gcd overlap.  Item 402 proves that unmarked descent of Item
399's selected nondegenerate coordinate supplies no such exclusion.  In
particular, there is no pre-existing complementary chart saving which
can silently be added to a degenerate-only statement.

Item 349 isolates the degenerate connection chart by the safely
saturated primitive triple-minor carrier



$$
p\mid\Pi^{\rm sat}_{r,s}
 \quad\Longleftrightarrow\quad
 \ell_r=\mu_r=C_r=0\pmod p.
\tag{1.4}
$$



That gate is necessary but not sufficient for an original collision.
The surviving target coordinate must still vanish.  This item couples
the two pieces exactly.

Let Item 334's chart-free target residuals be



$$
T_\nu=(-1)^{m+1}
 \bigl(f_\nu W^{\rm C}_{r,s}+9\,4^s b_\nu-11v_\nu\bigr),
 \qquad \nu=0,1,
 \qquad m=s-1,
\tag{1.5}
$$



with every displayed denominator a tied-$p$ unit.  Define



$$
\boxed{
 \Gamma_{r,s}
 =\gcd\!\left(
  \Pi_r,
  |\operatorname {num}T_0|,
  |\operatorname {num}T_1|
 \right),}
\tag{1.6}
$$



and, using Item 338's tied-prime-safe saturation product $S_{r,s}$,



$$
\boxed{\Gamma^{\rm sat}_{r,s}=(\Gamma_{r,s})_{(S_{r,s})}.}
\tag{1.7}
$$



The principal results are as follows.

> **PROVED — exact target-retaining degenerate carrier.**  On every
> actual row,
> 

$$
> \boxed{
> p\text{ is an original collision in the triple-minor chart}
> \quad\Longleftrightarrow\quad
> p\mid\Gamma_{r,s}
> \quad\Longleftrightarrow\quad
> p\mid\Gamma^{\rm sat}_{r,s}.}
> \tag{1.8}
>
$$


> Moreover $\Gamma^{\rm sat}_{r,s}\mid\Pi^{\rm sat}_{r,s}$.

> **PROVED — exact rejected-degenerate mass.**  On a fixed ray put
> 

$$
> F_e^{\rm deg}(M)=
> \sum_{\substack{p\text{ on the }e\text{-ray}\\
> p\mid\Pi^{\rm sat}_{r,s}\\
> p\nmid\Gamma^{\rm sat}_{r,s}}}\log p.
> \tag{1.9}
>
$$


> These and only these are the raw ray primes which enter the degenerate
> triple-minor chart and are rejected by its surviving target gate.

> **PROVED — sharp capacity criterion.**  A lower bound
> 

$$
> F_e^{\rm deg}(M)\geq\delta M+o(M)
> \tag{1.10}
>
$$


> removes at least $\delta/6$ from the normalized ordinary-$j=2$
> ceiling, even before any further nondegenerate rejection is used.  In
> particular, the maximum one-ray reward is $1/210$.

> **PROVED — chart-only zero-booking warning.**  Neither
> 

$$
> \sum_{p\mid\Pi^{\rm sat}_{r,s}}\log p=o(M)
> \tag{1.11}
>
$$


> nor
> 

$$
> \sum_{p\mid\Gamma^{\rm sat}_{r,s}}\log p=o(M)
> \tag{1.12}
>
$$


> by itself gives a fixed ray saving.  The first says that the
> degenerate chart is rare, so the nondegenerate chart may occupy almost
> the whole ray.  The second bounds degenerate collisions but supplies
> no positive lower bound for the mass of degenerate rows on which that
> bound acts.

> **PROVED — scoped information-class no-go.**  Triple-minor residues,
> the branch label $f=0$ or $f\ne0$, tied-prime unit-denominator
> facts, safe saturation, and pointwise carrier height do not determine
> the surviving target gate.  Exact rank-one finite-field countermodels
> have identical data in that information class and opposite target
> vanishing.  These are ambient linear-algebra models, not asserted
> values of the actual connection sequences.

No actual good-reduction or moving-divisor density theorem is obtained.
Therefore



$$
\boxed{\eta_{\rm proved}=0},\qquad
 \boxed{\Delta\mathcal C=0},\qquad
 \boxed{\text{ordinary-}j=2\text{ ceiling remains }1/105}.
\tag{1.13}
$$



No prime or collision census is used.

## 2. Exact construction of the coupled degenerate carrier

Write



$$
f=(f_0,f_1),\qquad b=(b_0,b_1),\qquad v=(v_0,v_1),
\tag{2.1}
$$



and



$$
\ell=\det(f,b),\qquad
 \mu=\det(f,v),\qquad
 C=\det(b,v).
\tag{2.2}
$$



Item 349 proves, with reduced rational representatives and unit
denominators,



$$
\ell=\mu=C=0\pmod p
 \quad\Longleftrightarrow\quad
 p\mid\Pi_r,
\tag{2.3}
$$



where



$$
\Pi_r=\gcd\left(
 |\operatorname {num}\mathfrak a_r|,
 |\operatorname {num}\mathfrak b_r|,
 |\operatorname {num}K_r|
 \right).
\tag{2.4}
$$



Item 334 proves on every chart that



$$
p\text{ is an original collision}
 \quad\Longleftrightarrow\quad
 T_0=T_1=0\pmod p.
\tag{2.5}
$$



Because all reduced denominators in (2.3)-(2.5) are $p$-units,
vanishing is equivalent to divisibility of the reduced numerator.
Combining (2.3) and (2.5) gives



$$
\begin{aligned}
 p\mid\Gamma_{r,s}
 &\Longleftrightarrow
 p\mid\Pi_r,
 \ p\mid\operatorname {num}T_0,
 \ p\mid\operatorname {num}T_1\\
 &\Longleftrightarrow
 \ell=\mu=C=0\pmod p
 \text{ and the original collision holds}.
\end{aligned}
\tag{2.6}
$$



Item 349's all-ray sign theorem gives $\Pi_r\geq1$, so (1.6) is a
positive integer on every admissible row.  Also



$$
\Gamma_{r,s}\mid\Pi_r.
\tag{2.7}
$$



Item 338 proves $p\nmid S_{r,s}$.  Hence removing every prime power
supported by $S_{r,s}$ preserves divisibility by the tied prime in
both $\Pi_r$ and $\Gamma_{r,s}$.  It also preserves (2.7), giving



$$
\boxed{
 p\mid\Gamma_{r,s}
 \Longleftrightarrow p\mid\Gamma^{\rm sat}_{r,s},
 \qquad
 \Gamma^{\rm sat}_{r,s}\mid\Pi^{\rm sat}_{r,s}.}
\tag{2.8}
$$



This proves (1.8).  Unlike the Item-349 carrier by itself, (1.6) is an
exact collision carrier on the degenerate chart, not merely a Closer
upper gate.

## 3. The surviving target on both internal branches

The unified two-coordinate definition (1.6) avoids every unsafe division.
Its branchwise meaning is nevertheless useful.

### 3.1 The branch $f\ne0\pmod p$

When all three minors vanish and $f\ne0$, both $b$ and $v$ lie on
the line spanned by $f$.  Choose any index $\nu$ with
$f_\nu\ne0$.  The two target residuals are proportional on this
rank-one line, and the original collision is equivalent to the single
surviving scalar condition



$$
T_\nu=0\pmod p.
\tag{3.1}
$$



The other coordinate is redundant after localization, but keeping both
in (1.6) is division-free and remains valid when the nonzero index
changes.

### 3.2 The branch $f=0\pmod p$

Here the period term disappears from (1.5).  The surviving condition is



$$
9\,4^s b-11v=0\pmod p,
\tag{3.2}
$$



or equivalently $T_0=T_1=0$.  The two coordinates must both be kept:
triple-minor vanishing says only that $b$ and $v$ are collinear, not
that their proportionality constant is $9\,4^s/11$.

Thus the Item-349 internal split



$$
f\ne0:\ \mathfrak a_r=\mathfrak b_r=0,
 \qquad
 f=0:\ K_r=0
\tag{3.3}
$$



does not remove the target test in either branch.

## 4. Exact ray partition and the mass which is actually bookable

Let $\mathcal P_e(M)$ be the raw candidate primes on the $e$-ray in



$$
I_M=\left[\frac{4M+3}{5},\frac{6M-1}{7}\right],
\tag{4.1}
$$



with the actual integrality restrictions from (1.1).  The finitely many
rows with $p\leq11$ have zero asymptotic mass and will be suppressed.

Partition $\mathcal P_e(M)$ into



$$
\begin{aligned}
 \mathcal D_e(M)&=\{p:\ell=\mu=C=0\},\\
 \mathcal N_e(M)&=\{p:\ell\ne0\},\\
 \mathcal O_e(M)&=\mathcal P_e(M)
 \setminus(\mathcal D_e(M)\cup\mathcal N_e(M)).
\end{aligned}
\tag{4.2}
$$



The set $\mathcal O_e$ contains no original collision.  Indeed, an
original collision satisfies Item 334's old gate



$$
D=9\,4^s\ell-11\mu=0.
\tag{4.3}
$$



If $\ell=0$ and $p>11$, then (4.3) forces $\mu=0$.  If
$C\ne0$, Item 334's independent-$(b,v)$ obstruction rules out the
collision; if $C=0$, the row lies in $\mathcal D_e$.

By (1.4) and (1.8),



$$
\mathcal D_e(M)
 =\{p:p\mid\Pi^{\rm sat}_{r,s}\},
\tag{4.4}
$$



and its actual collision subset is



$$
\mathcal C_e^{\rm deg}(M)
 =\{p:p\mid\Gamma^{\rm sat}_{r,s}\}.
\tag{4.5}
$$



On $\mathcal N_e$, Item 399 gives the exact collision subset



$$
\mathcal C_e^{\rm nd}(M)
 =\{p:p\mid E_{p,r,s},\ \mathfrak P_p\mid\Xi_{p,r,s}\}.
\tag{4.6}
$$



Define the rejected subsets



$$
\mathcal X_e^{\rm deg}=\mathcal D_e\setminus\mathcal C_e^{\rm deg},
 \qquad
 \mathcal X_e^{\rm nd}=\mathcal N_e\setminus\mathcal C_e^{\rm nd}.
\tag{4.7}
$$



Then the actual collision set and its complement have the exact disjoint
decompositions



$$
\boxed{
 \mathcal C_e
 =\mathcal C_e^{\rm deg}\ \dot\cup\ \mathcal C_e^{\rm nd},}
\tag{4.8}
$$





$$
\boxed{
 \mathcal P_e\setminus\mathcal C_e
 =\mathcal X_e^{\rm deg}
 \ \dot\cup\ \mathcal X_e^{\rm nd}
 \ \dot\cup\ \mathcal O_e.}
\tag{4.9}
$$



Taking logarithmic weights proves the exact capacity identity



$$
\boxed{
 R_e(M)-W_e(M)
 =F_e^{\rm deg}(M)+F_e^{\rm nd}(M)+O_e(M),}
\tag{4.10}
$$



where the three terms on the right are the Chebyshev masses of the three
sets in (4.9).  Formula (1.9) is exactly the first term.

Equation (4.10), not the size of either chart in isolation, is the
quantity that lowers the ledger.

## 5. Sharp capacity consequences

Let



$$
D_e(M)=\sum_{p\in\mathcal D_e(M)}\log p,
 \qquad
 G_e(M)=\sum_{p\in\mathcal C_e^{\rm deg}(M)}\log p.
\tag{5.1}
$$



Since $\mathcal C_e^{\rm deg}\subseteq\mathcal D_e$,



$$
\boxed{F_e^{\rm deg}(M)=D_e(M)-G_e(M).}
\tag{5.2}
$$



Consequently, if an actual theorem gives



$$
D_e(M)\geq dM+o(M),
 \qquad
 G_e(M)\leq gM+o(M),
\tag{5.3}
$$



then



$$
\boxed{
 \Delta\mathcal C_e
 \geq\frac{(d-g)_+}{6}.}
\tag{5.4}
$$



This is the exact admission rule for a degenerate-chart theorem.  Some
important special cases are:

1. A good-reduction theorem $\Pi^{\rm sat}_{r,s}=1$ makes
   $D_e=0$.  By itself it books zero: it moves the whole worst case to
   the complementary chart.
2. A moving-divisor theorem $G_e=o(M)$ books zero unless accompanied
   by a positive lower bound for $D_e$.
3. If $G_e=o(M)$ and $D_e\geq\delta M+o(M)$, the normalized saving
   is at least $\delta/6$.
4. If almost every prime on one ray enters the degenerate gate and fails
   its target, then $F_e^{\rm deg}=M/35+o(M)$ and the full
   $1/210$ ray is removed.

There is an equivalent chartwise-upper-bound criterion.  If



$$
G_e(M)\leq gM+o(M),
 \qquad
 W_e^{\rm nd}(M)\leq nM+o(M),
\tag{5.5}
$$



then



$$
\boxed{
 W_e(M)\leq
 \min\!\left(\frac1{35},g+n\right)M+o(M),}
\tag{5.6}
$$



and the normalized saving is at least



$$
\boxed{
 \frac1{6}
 \left(\frac1{35}-g-n\right)_+.}
\tag{5.7}
$$



These criteria are sharp from the stated mass information alone: the
degenerate and nondegenerate collision sets are disjoint subsets of one
ray, and arbitrary disjoint subsets can attain every total allowed by
the bounds.  Any stronger conclusion requires arithmetic information
about the actual carriers or their chart occupancy.

## 6. A precise information class and its no-go theorem

Define $\mathscr I_{\rm minor}$ to consist of arguments which use only
the following rowwise information:

1. the actual ray and tied-prime parametrization;
2. the values $\ell=\mu=C=0$ or, equivalently, tied divisibility of
   $\Pi^{\rm sat}_{r,s}$;
3. the branch label $f=0$ or $f\ne0$;
4. tied-prime unit-denominator and safe-saturation facts; and
5. pointwise height bounds for the primitive carrier;

but which do **not** use a formula-specific relation between the actual
connection vectors and the actual value $W^{\rm C}_{r,s}$ or
$4^s$.

### Theorem 6.1 — minor information does not determine the target gate

For every field $\mathbf F_p$ with $p>11$ and every
$c\in\mathbf F_p^\times$, the information in
$\mathscr I_{\rm minor}$ admits exact rank-one models with opposite
target vanishing.

On the $f\ne0$ branch, take



$$
f=b=(1,0),\qquad v=(0,0).
\tag{6.1}
$$



All three minors vanish.  With the harmless global sign suppressed,



$$
T=fW+9cb-11v=(W+9c,0).
\tag{6.2}
$$



Thus $W=-9c$ gives $T=0$, while $W=-9c+1$ gives
$T=(1,0)$.  The connection vectors, all minors, and the branch label
are identical.

On the $f=0$ branch, take



$$
f=(0,0),\qquad b=(1,0).
\tag{6.3}
$$



Both



$$
v=\left(\frac{9c}{11},0\right)
 \quad\text{and}\quad
 v=(0,0)
\tag{6.4}
$$



give $\ell=\mu=C=0$ and the same branch label.  The first satisfies
$9cb-11v=0$; the second does not.

This proves the information-class no-go.  It does not claim that either
ambient model is attained by the actual Item-334 connection formulas.
A formula-specific identity or distribution theorem for the actual
values lies outside $\mathscr I_{\rm minor}$ and can evade the result.

### Theorem 6.2 — support and height alone have the full capacity range

The same sharpness is visible at the primitive-integer level.  For a
tied prime $p$, take a formal safely saturated packet



$$
S=1,\qquad \Pi=p.
\tag{6.5}
$$



The target-hit packet



$$
\operatorname {num}T_0=p,qquad
 \operatorname {num}T_1=p
\tag{6.6}
$$



has $\Gamma=p$, while the target-miss packet



$$
\operatorname {num}T_0=1,qquad
 \operatorname {num}T_1=p
\tag{6.7}
$$



has $\Gamma=1$.  They have the same triple carrier, safe saturation,
and pointwise logarithmic size $O(\log p)$, yet opposite collision
status.  Applying either choice row by row on a fixed-$M$ slice fills
or empties any selected ambient subset of that ray without violating
those rowwise data.  This construction deliberately does not model an
additional cross-$M$ recurrence relation.

Again, (6.5)-(6.7) are information-theoretic countermodels, not actual
sequence values.  They prove only that a density conclusion cannot be a
formal consequence of support, saturation, and pointwise height alone.

## 7. Height and moving-divisor status

Because $\Gamma_{r,s}\mid\Pi_r$, Item 349's bound immediately gives



$$
\log^+\Gamma_{r,s}
 \leq\log^+\Pi_r
 =O(r\log r).
\tag{7.1}
$$



On a fixed-$M$ slice there are $O(M)$ candidate rows and
$r=O(M)$.  Therefore the direct product estimate is only



$$
\sum_{(r,s)}\log^+\Gamma_{r,s}
 =O(M^2\log M).
\tag{7.2}
$$



Safe saturation can only decrease the left side, but no certified
average saving is available.  The raw ray mass is already $O(M)$, so
(7.2) is noncompetitive.  The scoped countermodels in Section 6 show
why the order of the pointwise height bound alone cannot repair this.

The following remain **OPEN**:



$$
\sum_{p\mid\Gamma^{\rm sat}_{r,s}}\log p=o(M),
\tag{7.3}
$$



a positive lower bound for $F_e^{\rm deg}(M)$, an average gcd theorem
for (1.6), and an all-row good-reduction theorem for either
$\Pi^{\rm sat}$ or $\Gamma^{\rm sat}$.

## 8. Conditional admission targets

The following statements are deliberately labelled **CONDITIONAL**.

> **CONDITIONAL A.**  If, on one ray,
> $D_e(M)\geq dM+o(M)$ and
> $G_e(M)\leq gM+o(M)$ with $d>g$, then the ordinary-$j=2$
> normalized ceiling falls by at least $(d-g)/6$.

> **CONDITIONAL B.**  If the Item-399 nondegenerate collision mass is
> at most $nM+o(M)$ and the Item-404 degenerate collision mass is at
> most $gM+o(M)$, with $g+n<1/35$, then one ray contributes at
> most $(g+n)/6$ to the normalized ceiling and the saving from that
> ray is at least $(1/35-g-n)/6$.

> **CONDITIONAL C.**  A full $o(M)$ theorem for both actual chart
> collision masses on one ray removes exactly its complete normalized
> capacity $1/210$.

None of the antecedents with a positive numerical margin is proved here.

## 9. Deterministic certificate and strict labels

The companion certificate verifies:

- frozen canonical hashes for Items 334, 338, 349, 397, 399, and 402;
- the gcd and tied-prime-safe saturation implications in (2.6)-(2.8);
- exact rank-one target-hit and target-miss models on both internal
  branches;
- the sharp ray-capacity arithmetic (5.4) and (5.7); and
- byte-identical replay.

Canonical replay:

```powershell
python scripts/item404_j2_degenerate_target_rejection_capacity_certificate.py `
  --replay results/item404_j2_degenerate_target_rejection_capacity_certificate.json `
  --output results/item404_j2_degenerate_target_rejection_capacity_certificate_replay.json
```

The declared finite-field and integer packets are labelled
**EXACT ALGEBRAIC COUNTERMODELS / NOT ACTUAL VALUES / NO CENSUS**.

**PROVED:** the exact target-retaining degenerate carrier, its safe
saturation, the internal surviving-target split, the exact ray
partition, the rejected-mass capacity identity, the sharp capacity
criteria, the scoped minor-information no-go, and $\eta=0$.

**CONDITIONAL:** only the implications in Section 8.  No antecedent with
a positive saving is promoted to a theorem.

**OPEN:** every actual moving-divisor, good-reduction, average-gcd, or
positive rejected-mass theorem; a positive full-ray saving; Route 1; and
every conclusion about $e+\pi$.
