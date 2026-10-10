> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 407 — ordinary-$j=2$ target-rejection density boundary on one full ray

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



On either complete ray, Item 399 gives the raw Chebyshev mass



$$
R_e(M)=\frac1{35}M+o(M).
\tag{1.2}
$$



Thus one full ray has normalized capacity $1/210$, and both ordinary-
$j=2$ rays have the shared normalized ceiling $1/105$.

Item 404 isolates the exact degenerate target carrier



$$
\Gamma_{r,s}=\gcd\!\left(
  \Pi_r,
  |\operatorname {num}T_0|,
  |\operatorname {num}T_1|
 \right),
 \qquad
 \Gamma^{\rm sat}_{r,s}=(\Gamma_{r,s})_{(S_{r,s})},
\tag{1.3}
$$



with



$$
p\mid\Pi^{\rm sat}_{r,s}
 \quad\Longleftrightarrow\quad
 \ell_r=\mu_r=C_r=0\pmod p,
\tag{1.4}
$$



and



$$
p\mid\Gamma^{\rm sat}_{r,s}
 \quad\Longleftrightarrow\quad
 p\text{ is an original collision in the degenerate chart}.
\tag{1.5}
$$



This item attacks the support difference in (1.4)–(1.5), not the rarity
of either support separately.  Write $A_{(B)}$ for the largest divisor
of $A$ coprime to $B$, and define the actual rowwise rejection
carrier



$$
\boxed{
 \mathcal J_{r,s}
 =\bigl(\Pi^{\rm sat}_{r,s}\bigr)_{(\Gamma^{\rm sat}_{r,s})}.}
\tag{1.6}
$$



The results are:

> **PROVED — exact degenerate target-rejection carrier.**  On every
> actual row,
> 

$$
> \boxed{
> p\mid\mathcal J_{r,s}
> \quad\Longleftrightarrow\quad
> p\mid\Pi^{\rm sat}_{r,s}
> \text{ and }
> p\nmid\Gamma^{\rm sat}_{r,s}.}
> \tag{1.7}
>
$$


> These, and only these, are degenerate rows rejected by the surviving
> target gate.

> **PROVED — exact union accounting.**  If $D_e,G_e,N_e$ denote,
> respectively, the degenerate-gate mass, the degenerate-collision mass,
> and Item 399's nondegenerate selected-prime collision mass, then the
> full collision mass is
> 

$$
> \boxed{W_e(M)=G_e(M)+N_e(M),}
> \tag{1.8}
>
$$


> while the degenerate target-rejection mass is
> 

$$
> \boxed{F_e^{\rm deg}(M)=D_e(M)-G_e(M)
> =\sum_{p\mid\mathcal J_{r,s}}\log p.}
> \tag{1.9}
>
$$


> The sum in (1.9) is over the actual tied-prime rows on the fixed ray.

> **PROVED — sharp joint density criterion.**  Put $R=1/35$.  If
> actual theorems on one ray give
> 

$$
> D_e(M)\ge dM+o(M),\qquad
> G_e(M)\le gM+o(M),\qquad
> N_e(M)\le nM+o(M),
> \tag{1.10}
>
$$


> then the excluded ray mass is at least
> 

$$
> \boxed{
> \sigma(d,g,n)M+o(M),\qquad
> \sigma(d,g,n)=
> \max\!\left\{0,d-g,\frac1{35}-g-n\right\}.}
> \tag{1.11}
>
$$


> Hence the normalized capacity reduction is at least
> 

$$
> \boxed{\Delta\mathcal C_e\ge\sigma(d,g,n)/6.}
> \tag{1.12}
>
$$



> **PROVED — sharp information boundary.**  Formula (1.11) is best
> possible from only the aggregate facts in (1.10), the exact chart
> inclusions, and disjointness.  Abstract weighted-ray models attain the
> bound.  They are information-theoretic mass models, not actual prime
> rows, connection values, or selected-prime residuals.

The pinned dependencies give neither a positive lower density for
$D_e-G_e$ nor upper constants $g,n$ with $g+n<1/35$.  No actual
good-reduction, moving-divisor, average-gcd, or selected-prime weighted
theorem is proved here.  Therefore



$$
\boxed{\eta_{\rm proved}=0},\qquad
 \boxed{\Delta\mathcal C=0},\qquad
 \boxed{\text{ordinary-}j=2\text{ ceiling remains }1/105}.
\tag{1.13}
$$



There is no prime or collision census and no extrapolation from finite
rows.

## 2. The exact support-difference carrier

Item 349 defines



$$
\Pi_r=\gcd\left(
 |\operatorname {num}\mathfrak a_r|,
 |\operatorname {num}\mathfrak b_r|,
 |\operatorname {num}K_r|
 \right)
\tag{2.1}
$$



and proves $\Pi_r\ge1$ on every admissible ray row.  Item 338's safe
saturation product satisfies $p\nmid S_{r,s}$, so



$$
p\mid\Pi_r
 \quad\Longleftrightarrow\quad
 p\mid\Pi^{\rm sat}_{r,s}=(\Pi_r)_{(S_{r,s})}.
\tag{2.2}
$$



Item 404 proves



$$
\Gamma^{\rm sat}_{r,s}\mid\Pi^{\rm sat}_{r,s}
\tag{2.3}
$$



and the exact target equivalence (1.5).  For positive integers $A,B$,
the defining property of $A_{(B)}$ is



$$
q\mid A_{(B)}
 \quad\Longleftrightarrow\quad
 q\mid A\text{ and }q\nmid B
\tag{2.4}
$$



for every prime $q$.  Applying (2.4) to (1.6) proves (1.7).

Equivalently, because of (2.3), the radical support is



$$
\operatorname {rad}(\mathcal J_{r,s})
 =\frac{\operatorname {rad}(\Pi^{\rm sat}_{r,s})}
 {\operatorname {rad}(\Gamma^{\rm sat}_{r,s})}.
\tag{2.5}
$$



Formula (1.6) is preferable for replay because it is integral without
introducing a quotient convention.  Formula (2.5) makes the support
difference transparent.

Since $\mathcal J_{r,s}\mid\Pi^{\rm sat}_{r,s}\mid\Pi_r$, Item 349's
height bound gives only



$$
\log^+\mathcal J_{r,s}
 \le \log^+\Pi_r
 =O(r\log r).
\tag{2.6}
$$



This is an upper bound for one row.  The required theorem is a positive
lower bound for the tied-prime support of $\mathcal J$ along a
fixed-$M$ ray.  An upper height bound cannot supply that lower bound.

## 3. The actual full-ray union

Let $\mathcal P_e(M)$ be the raw prime rows on the $e$-ray in



$$
I_M=\left[\frac{4M+3}{5},\frac{6M-1}{7}\right].
\tag{3.1}
$$



Suppress the finitely many primes $p\le11$, which have zero
asymptotic logarithmic mass.  Use Item 404's disjoint partition



$$
\mathcal P_e
 =\mathcal D_e\ \dot\cup\ \mathcal A_e\ \dot\cup\ \mathcal O_e,
\tag{3.2}
$$



where



$$
\begin{aligned}
 \mathcal D_e&=\{p:\ell_r=\mu_r=C_r=0\}
              =\{p:p\mid\Pi^{\rm sat}_{r,s}\},\\
 \mathcal A_e&=\{p:\ell_r\ne0\},
\end{aligned}
\tag{3.3}
$$



and $\mathcal O_e$ is the leftover automatic obstruction chart.  No
row in $\mathcal O_e$ is an original collision.

The actual collision subsets are



$$
\mathcal C_e^{\rm deg}
 =\{p:p\mid\Gamma^{\rm sat}_{r,s}\}
 \subseteq\mathcal D_e
\tag{3.4}
$$



and, by Item 399,



$$
\mathcal C_e^{\rm nd}
 =\{p\in\mathcal A_e:
 p\mid E_{p,r,s},\ \mathfrak P_p\mid\Xi_{p,r,s}\}
 \subseteq\mathcal A_e.
\tag{3.5}
$$



Consequently



$$
\boxed{
 \mathcal C_e
 =\mathcal C_e^{\rm deg}\ \dot\cup\
  \mathcal C_e^{\rm nd}.}
\tag{3.6}
$$



The rejected subsets are



$$
\mathcal X_e^{\rm deg}
 =\mathcal D_e\setminus\mathcal C_e^{\rm deg}
 =\{p:p\mid\mathcal J_{r,s}\},
\tag{3.7}
$$





$$
\mathcal X_e^{\rm nd}
 =\mathcal A_e\setminus\mathcal C_e^{\rm nd}.
\tag{3.8}
$$



Thus the complement of the **union** collision set is



$$
\boxed{
 \mathcal P_e\setminus\mathcal C_e
 =\mathcal X_e^{\rm deg}\ \dot\cup\
  \mathcal X_e^{\rm nd}\ \dot\cup\mathcal O_e.}
\tag{3.9}
$$



Taking logarithmic weights gives



$$
\boxed{
 R_e-W_e
 =F_e^{\rm deg}+F_e^{\rm nd}+O_e,}
\tag{3.10}
$$



where $F_e^{\rm deg}=D_e-G_e$, proving (1.8)–(1.9).  Every saving
claimed below is a lower bound for the left side of (3.10), so no chart
mass is counted twice and no complementary chart is silently omitted.

## 4. Sharp joint threshold

Write



$$
R=\frac1{35}.
\tag{4.1}
$$



Ignore the common $o(M)$ terms while deriving the leading constants.
If $D,G,N$ are the leading masses per $M$, chart inclusion and
disjointness give



$$
0\le G\le D\le R,
 \qquad
 0\le N\le R-D.
\tag{4.2}
$$



Assume the information (1.10): $D\ge d$, $G\le g$, $N\le n$.
Two independent bounds follow immediately:



$$
R-(G+N)\ge R-g-n,
\tag{4.3}
$$



and



$$
R-(G+N)
 \ge D-G
 \ge d-g.
\tag{4.4}
$$



Together with nonnegativity, (4.3)–(4.4) prove (1.11).

The same statement can be written as the exact aggregate linear
program



$$
\max(G+N)
 =\min\{R,\ g+n,\ R-d+g\},
\tag{4.5}
$$



over (4.2) and (1.10).  Subtracting (4.5) from $R$ is exactly (1.11).

### 4.1 Degenerate rejection route

If there is no usable nondegenerate bound, take the trivial $n=R$.
Then (1.11) becomes



$$
\boxed{\sigma=(d-g)_+.}
\tag{4.6}
$$



Therefore an actual theorem



$$
D_e\ge dM+o(M),\qquad G_e\le gM+o(M),\qquad d>g,
\tag{4.7}
$$



does book a full-union saving: the rows in
$\mathcal X_e^{\rm deg}$ are absent from the collision union regardless
of what happens in the nondegenerate chart.  The normalized reward is
$(d-g)/6$.

This is the exact $d-g$ threshold.  An upper bound for $G_e$ without
a positive lower bound for $D_e$ has $d=0$ and books nothing by this
route.

### 4.2 Two-chart collision-upper-bound route

If no positive degenerate occupancy is known, take $d=0$.  Then



$$
\boxed{
 \sigma=\left(\frac1{35}-g-n\right)_+.}
\tag{4.8}
$$



Thus separate actual upper bounds for the exact Item-404 degenerate
collision carrier and the exact Item-399 selected-prime chart save a
positive part of a full ray exactly when



$$
\boxed{g+n<\frac1{35}.}
\tag{4.9}
$$



This is the exact $1/35-g-n$ threshold.  It explicitly controls the
union (3.6).

### 4.3 Gate rarity requires a complementary theorem

Suppose instead that a theorem gives an upper bound



$$
D_e(M)\le qM+o(M).
\tag{4.10}
$$



Because $G_e\le D_e$, combining (4.10) with
$N_e\le nM+o(M)$ gives



$$
R_e-W_e
 \ge\left(\frac1{35}-q-n\right)M+o(M).
\tag{4.11}
$$



This is sharp from those two bounds.  But gate rarity **alone** has the
trivial $n=R$ and gives zero.  In particular,
$D_e=o(M)$ simply moves the possible worst case to the nondegenerate
selected-prime chart unless that chart is also bounded.

## 5. Precise information class and no-go theorem

Define $\mathscr I_{407}(d,g,n)$ to consist of arguments which use
only:

1. the actual tied-prime parametrization and ray mass $R=1/35$;
2. the exact rowwise equivalences (1.4), (1.5), and (3.5);
3. the inclusions and disjoint partition (3.2)–(3.6);
4. the aggregate inequalities (1.10);
5. tied-prime-safe saturation and the pointwise height
   $\log^+\mathcal J=O(r\log r)$; and
6. unmarked invariant information already closed by Item 402;

but no formula-specific weighted distribution theorem for the actual
values of $\Pi^{\rm sat}$, $\Gamma^{\rm sat}$, or the selected ideal
$(E,\Xi)$, and no cross-row relation forcing additional rejection.

### Theorem 5.1 — aggregate information has exact saving $\sigma$

Within $\mathscr I_{407}(d,g,n)$, the largest universally forced
excluded mass is exactly (1.11).

The lower bound was proved in Section 4.  For sharpness, take an abstract
nonatomic ray of total mass $R$.  Choose a degenerate interval of mass
$D\in[d,R]$, put a degenerate-collision subinterval of mass



$$
G=\min(D,g),
\tag{5.1}
$$



and put a nondegenerate-collision interval of mass



$$
N=\min(R-D,n)
\tag{5.2}
$$



in the complement.  Choosing $D$ at a breakpoint of the piecewise
linear function



$$
\min(D,g)+\min(R-D,n)
\tag{5.3}
$$



attains (4.5).  The remaining mass is assigned to target rejections or
the automatic obstruction chart.  All containments and aggregate bounds
in $\mathscr I_{407}$ hold, while the excluded mass is exactly
$\sigma$.

If the unmarked invariant fields in clause 6 are required explicitly,
decorate the nondegenerate hit and miss pieces with Item 402's conjugate
split-cyclotomic packets: the full unmarked invariant data agree while
the selected coordinate vanishes on only one packet.  This decoration
does not change any mass or containment.  It remains an abstract
information packet and is not an actual value of $\Xi_{p,r,s}$.

This construction is an **ABSTRACT WEIGHTED INFORMATION MODEL / NOT
ACTUAL PRIME ROWS / NOT ACTUAL CONNECTION VALUES / NOT AN ACTUAL
SELECTED-PRIME PACKET**.  It proves only that a stronger conclusion
cannot be a formal consequence of the named information.  It neither
asserts nor suggests that the actual sequences realize the model.

### Corollary 5.2 — zero margin means zero admissible booking

If $d\le g$ and $g+n\ge1/35$, then



$$
\sigma(d,g,n)=0.
\tag{5.4}
$$



No positive full-ray saving follows inside $\mathscr I_{407}$.  An
actual formula-specific theorem outside this class can evade the no-go;
that is precisely the missing arithmetic input.

## 6. Audit of the live actual-theorem routes

### 6.1 Good reduction for the degenerate gate

An all-row theorem $\Pi^{\rm sat}_{r,s}=1$ would give



$$
D_e=G_e=F_e^{\rm deg}=0.
\tag{6.1}
$$



It would close the degenerate chart but produce no target-rejection mass
there.  With the nondegenerate chart uncontrolled, (4.8) has
$g=0,n=R$ and saves zero.  Good reduction can contribute to a union
theorem only when paired with $n<R$.

### 6.2 Moving-divisor upper bound for $\Gamma^{\rm sat}$

A theorem



$$
G_e(M)=o(M)
\tag{6.2}
$$



would give $g=0$.  It saves $d/6$ if accompanied by an actual lower
bound $D_e\ge dM+o(M)$, or combines with $n<1/35$ through (4.8).
Without either complement, $d=0,n=R$ and the bookable margin is zero.

### 6.3 Gate-rarity upper bound

A theorem $D_e=o(M)$ is not a lower bound for (1.9).  It gives zero
by itself and contributes only through (4.11) after a nondegenerate
selected-prime upper bound is supplied.  No gate-rarity-only booking is
admissible.

### 6.4 Pointwise height and products

There are $O(M)$ candidate rows and $r=O(M)$.  From (2.6), the raw
fixed-$M$ product estimate is only



$$
\sum_{(r,s)}\log^+\mathcal J_{r,s}
 =O(M^2\log M).
\tag{6.3}
$$



The ray itself has only $O(M)$ mass.  More importantly, (6.3) is an
upper height bound, whereas (1.9) needs a positive lower density of tied
prime divisors.  It supplies no positive $d-g$ margin.

### 6.5 The selected-prime complement

Item 399's nondegenerate condition retains both



$$
p\mid E_{p,r,s}
 \quad\text{and}\quad
 \mathfrak P_p\mid\Xi_{p,r,s}.
\tag{6.4}
$$



Item 402 proves that unmarked trace, norm, symmetric, and Frobenius
packets do not determine the selected coordinate.  No pinned theorem
gives $N_e\le nM+o(M)$ with a useful $n<1/35$.  Replacing (6.4) by
an unmarked or unspecified-prime condition would enlarge support and is
not admitted in (1.10).

Thus none of the live routes supplies a positive numerical margin in
(1.11).

## 7. Conditional admission table

Every line in this section is **CONDITIONAL** unless its margin is zero.



$$
\begin{array}{c|c|c}
\text{actual input on one ray}&
\text{excluded mass per }M&
\text{normalized saving}\\ \hline
D\ge dM,\ G\le gM&
(d-g)_+M&(d-g)_+/6\\
G\le gM,\ N\le nM&
(1/35-g-n)_+M&(1/35-g-n)_+/6\\
\text{both input pairs}&
\sigma(d,g,n)M&\sigma(d,g,n)/6\\
D=o(M)\text{ only}&0&0\\
G=o(M)\text{ only}&0&0\\
G=o(M),\ N=o(M)&(1/35)M&1/210.
\end{array}
\tag{7.1}
$$



The last line removes one complete ray, not both ordinary-$j=2$ rays.
No positive-margin antecedent in this table is proved by Item 407.

## 8. Deterministic certificate and strict labels

The companion certificate:

- freezes canonical Items 349, 397, 399, and 402 and the complete Item
  404 work package used here;
- verifies the exact support-difference carrier (1.6) on Item 404's
  declared integer-algebra packets;
- checks the linear program (4.5), the exact threshold (1.11), and
  representative rational scenarios;
- constructs exact abstract mass models attaining the bound; and
- produces byte-identical replay.

The inherited integer packets are labelled **EXACT INTEGER ALGEBRA
REPLAY ONLY / NOT ACTUAL VALUES / NO CENSUS**.  The sharpness models are
labelled **ABSTRACT WEIGHTED INFORMATION MODELS / NOT ACTUAL ROWS**.
Neither class is used to infer an actual density statement.

**PROVED:** the exact rejection carrier $\mathcal J$, its tied-prime
equivalence, the full-union accounting, the sharp joint threshold
$\max\{0,d-g,1/35-g-n\}$, the gate-rarity coupling rule, the precise
information-class boundary, and proved $\eta=0$.

**CONDITIONAL:** only implications whose antecedents are explicit actual
weighted theorems with a positive margin.

**EXACT ALGEBRAIC REPLAY ONLY / NOT ACTUAL:** declared integer support
packets inherited from Item 404.

**ABSTRACT INFORMATION MODEL / NOT ACTUAL:** the mass constructions used
solely to prove sharpness of the information boundary.

**OPEN:** every actual good-reduction, moving-divisor, average-gcd,
positive rejected-mass, or selected-prime weighted theorem; every
positive full-ray saving; Route 1; and every conclusion about $e+\pi$.
