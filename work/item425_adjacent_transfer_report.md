> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 425 — adjacent transfer saturates the normalized mixed-cubic base

Date: 2026-09-01  
Status: **WORK-ONLY, PROVED ADJACENT-DETERMINANT SATURATION AND SCOPED HOLONOMIC NO-GO, ZERO LEDGER**

## 1. Capacity verdict first

Retain the actual Item-390 residues



$$
\lambda_{0,m}=\operatorname {CT}(f_0H^m),\qquad
 \lambda_{1,m}=\operatorname {CT}(f_1H^m),                 \tag{1.1}
$$



where



$$
H(y)=\frac{(1-y)^6}{y^4(1+y^2)^4},\qquad
 f_0(y)=\frac{1+y}{1+y^2},\qquad
 f_1(y)=\frac{(1+y)^4}{y(1+y^2)^2}.                       \tag{1.2}
$$



Canonical Item 200 and Items 390, 415 give



$$
F_m\mid\lambda_{0,m},\lambda_{1,m},\qquad
 \mu_{s,m}:=\frac{\lambda_{s,m}}{F_m}\in\mathbb Z,\qquad
 \log F_m=\mathfrak C_Fm+o(m),                            \tag{1.3}
$$



and, for the strictly-large component,



$$
c_m^>=\left(\gcd(|\mu_{0,m}|,|\mu_{1,m}|)\right)_{p>6m}.
                                                               \tag{1.4}
$$



Put



$$
g_m=\gcd(|\mu_{0,m}|,|\mu_{1,m}|),\qquad
 R_*=\rho_*e^{-\mathfrak C_F}
 =13.1004071782333102143382142797\ldots .                 \tag{1.5}
$$



The current pointwise component ceiling is



$$
C_>:=\frac{\log R_*}{6}
 =0.4287738853386578689457603829\ldots .                  \tag{1.6}
$$



For the adjacent exterior carrier



$$
W_m^\lambda=
 \lambda_{0,m}\lambda_{1,m+1}
 -\lambda_{1,m}\lambda_{0,m+1},\qquad
 W_m^\mu=\frac{W_m^\lambda}{F_mF_{m+1}},                  \tag{1.7}
$$



this item proves



$$
W_m^\mu\in\mathbb Z,\qquad
 g_mg_{m+1}\mid W_m^\mu,                                  \tag{1.8}
$$



and the exact exponential size



$$
\lim_{m\to\infty}|W_m^\lambda|^{1/m}=\rho_*^2,\qquad
 \lim_{m\to\infty}|W_m^\mu|^{1/m}=R_*^2.                  \tag{1.9}
$$



Thus a direct use of the determinant to bound only one row has ceiling



$$
\frac{\log R_*^2}{6}=2C_>
 =0.8575477706773157378915207658\ldots,                   \tag{1.10}
$$



which is worse.  If its size is shared across the two row gcds in (1.8),
the mean cost per contained row is



$$
\frac{\log R_*^2}{12}=C_>.                               \tag{1.11}
$$



Therefore the natural adjacent determinant gives **no strict exponential
gain** over Item 418.  It books no lower-bound mass and reduces no live
capacity.  This is a zero-ledger result.

The conclusion is deliberately scoped.  It closes the adjacent $2\times2$
exterior carrier and the first natural degree-two shifted critical-value
reduction below.  It does not close growing windows, adaptive
$m$-dependent coefficients of unbounded degree, or an arithmetic modular
resultant that contains fewer row gcds than its analytic height suggests.

## 2. Exact adjacent exterior identity

Item 420 proved the unique fixed-coordinate leading cancellation



$$
D_m:=2\lambda_{1,m}-5\lambda_{0,m}
 =\frac1m\operatorname {CT}(qH^m),\qquad
 q(y)=\frac{y^4-4y^2-1}{2y(1+y^2)^2}.                    \tag{2.1}
$$



Substitute $2\lambda_{1,n}=5\lambda_{0,n}+D_n$ into the determinant.
For every $m\ge1$,



$$
\boxed{\;
 2W_m^\lambda
 =\lambda_{0,m}D_{m+1}-D_m\lambda_{0,m+1}.
 \;}                                                       \tag{2.2}
$$



More generally, for every fixed $h\ge1$, if



$$
W_{m,h}^\lambda=
 \lambda_{0,m}\lambda_{1,m+h}
 -\lambda_{1,m}\lambda_{0,m+h},                           \tag{2.3}
$$



then the exact transfer is



$$
2W_{m,h}^\lambda
 =\lambda_{0,m}D_{m+h}-D_m\lambda_{0,m+h}.                \tag{2.4}
$$



Equation (2.2) is therefore not an experimental recurrence; it is an exact
identity in the actual family.

Since $F_n$ divides both coordinates at row $n$, (1.7) is the determinant
of the two normalized integer rows:



$$
W_m^\mu=
 \det\begin{pmatrix}
 \mu_{0,m}&\mu_{1,m}\\
 \mu_{0,m+1}&\mu_{1,m+1}
 \end{pmatrix}\in\mathbb Z.                               \tag{2.5}
$$



Every prime power dividing $g_mg_{m+1}$ divides both terms in (2.5), with
the valuations adding even when the same prime occurs in both rows.
Consequently



$$
g_mg_{m+1}\mid W_m^\mu.                                  \tag{2.6}
$$



This is an all-depth integer divisibility.  It is stronger than a statement
only about the $p>6m$ part, but its carrier height is correspondingly the
product height of two rows.

## 3. The determinant has the full squared saddle base

Let $\alpha,\bar\alpha$ be the dominant critical points from Item 420,
put



$$
\tau=H(\alpha),\qquad |\tau|=\rho_*,
 \qquad t=\frac{q(\alpha)}{f_0(\alpha)}.                   \tag{3.1}
$$



Items 420 and 423 prove



$$
\tau\notin\mathbb R,\qquad t\notin\mathbb R,              \tag{3.2}
$$



and give a nonzero saddle constant $C$ for which



$$
\lambda_{0,m}
 =m^{-1/2}\left(
 C\tau^m+\bar C\bar\tau^{\,m}
 +O(\rho_*^m/m)\right),                                   \tag{3.3}
$$





$$
D_m
 =m^{-3/2}\left(
 Ct\tau^m+\bar C\bar t\bar\tau^{\,m}
 +O(\rho_*^m/m)\right).                                   \tag{3.4}
$$



Insert (3.3)--(3.4) into (2.2).  At order
$m^{-2}\rho_*^{2m}$, the two same-saddle products cancel:



$$
C\tau^m\cdot Ct\tau^{m+1}
 -Ct\tau^m\cdot C\tau^{m+1}=0,                            \tag{3.5}
$$



and likewise at the conjugate saddle.  The two cross-saddle products do
not cancel.  Their coefficient after the factor $2$ in (2.2) is removed
is



$$
K=\frac{|C|^2}{2}(t-\bar t)(\tau-\bar\tau).              \tag{3.6}
$$



Both factors in parentheses are nonzero by (3.2); hence $K\ne0$.  Uniform
use of the inherited saddle remainders gives



$$
W_m^\lambda
 =K\,m^{-2}\rho_*^{2m}\left(1+O(1/m)\right).              \tag{3.7}
$$



This proves the first limit in (1.9).  From (1.3),



$$
\log(F_mF_{m+1})=\mathfrak C_F(2m+1)+o(m),               \tag{3.8}
$$



so division by the two compulsory Cartier factors proves the normalized
limit in (1.9).

For a general fixed shift $h$, the analogous leading cross coefficient
is proportional to



$$
(t-\bar t)(\tau^h-\bar\tau^{\,h}).                       \tag{3.9}
$$



The adjacent case $h=1$ is unconditionally nonzero by (3.2) and already
saturates the squared base.  No claim is made here that (3.9) is nonzero
for every $h$.

## 4. Exact degree-two shifted critical-value reduction

One might hope to combine $D_m$ with a few shifted values of
$\lambda_{0,\bullet}$ so that the dominant saddle value vanishes, then
use the result as a smaller carrier.  The first exact attempt can be
completed symbolically.

The critical polynomial is



$$
P(y)=3y^3-6y^2-y-2.                                     \tag{4.1}
$$



In the cubic algebra $\mathbb Q[y]/(P)$, exact reduction gives



$$
\frac{q}{f_0}=a+bH+cH^2,                                 \tag{4.2}
$$



where



$$
a=\frac{195029}{3525500},\qquad
 b=-\frac{1339328}{71391375},\qquad
 c=-\frac{237568}{1927567125}.                            \tag{4.3}
$$



Define the rational residual and its integration-by-parts antiderivative by



$$
R_2=q-f_0(a+bH+cH^2),\qquad
 A_2=-\frac{R_2}{H'/H},\qquad
 q_2=y\left(\frac{A_2}{y}\right)'.                        \tag{4.4}
$$



The congruence (4.2) is exactly what makes $A_2$ regular at every critical
point of $H$.  The constant term of
$y((A_2/y)H^m)'$ is zero.  Therefore



$$
\boxed{\;
 mD_m-a\lambda_{0,m}-b\lambda_{0,m+1}-c\lambda_{0,m+2}
 =\frac1m\operatorname {CT}(q_2H^m).
 \;}                                                       \tag{4.5}
$$



For a compact exact specification, write



$$
q_2(y)=\frac{\sum_{j=0}^{25}n_jy^j}
 {15420537000\,y^8(1+y^2)^9},                             \tag{4.6}
$$



with the coefficient vector in ascending degree



$$
\begin{aligned}
(n_0,\ldots,n_{25})={}&(
-3801088,\ 41574400,\ -205971456,\ 619161600,\\
&-1586297344,\ 3456708288,\ -6253518656,\ 12447250341,\\
&-17002039104,\ 40590677491,\ -34510619944,\ 116864052888,\\
&-69541566360,\ 257666823352,\ -128134405320,\ 374285602250,\\
&-162511549560,\ 335484606006,\ -129182415480,\ 174669454224,\\
&-62286636744,\ 44447571936,\ -16889613912,\ 1416301929,\\
&-2001384936,\ -1142868609).
\end{aligned}                                             \tag{4.7}
$$



The exact resultants are



$$
\operatorname {Res}(P,\operatorname {num}q_2)
 =-181207723609599379275366250837463531520000000,         \tag{4.8}
$$





$$
\operatorname {Res}(P,\operatorname {den}q_2)
 =33028455344443562055745346250291019776000000000.        \tag{4.9}
$$



Thus $q_2$ is finite and nonzero at every critical point, including both
dominant saddles.  Applying the same saddle lemma as Item 420 to the right
side of (4.5) saves only a power of $m$; its root base remains $\rho_*$.

There is also a basic carrier obstruction: the shifted terms
$\lambda_{0,m+1}$ and $\lambda_{0,m+2}$ need not be divisible by the
single-row gcd $g_m$.  Hence (4.5) is not itself a one-row Bezout carrier.
If one clears this by using gcds from all involved rows, the analytic height
also pays for those rows.  No strict base reduction follows.

## 5. Capacity and admission screen

The adjacent carrier passes support and actual-family tests but fails the
strict-gain test:

1. It is an exact identity for the original mixed-cubic residues.
2. It contains the complete normalized row gcds at $m$ and $m+1$.
3. Its normalized root base is exactly $R_*^2$, not a number below $R_*^2$.
4. Per contained row, its exponential cost is exactly $R_*$.
5. The degree-two shifted reduction has root base $\rho_*$ and no
   single-row divisibility bridge.

Accordingly,



$$
\Delta r_1=0,\qquad
 \Delta(\hbox{proved lower bound})=0,\qquad
 \Delta(\hbox{strictly-large capacity ceiling})=0.         \tag{5.1}
$$



The smallest still-open useful lemma is no longer an adjacent determinant
identity.  It is:

> Construct genuinely arithmetic cross-index information whose normalized
> carrier root base, after charging every row gcd it contains, is strictly
> below $R_*$; or prove weighted nonconcentration of the strictly-large
> common divisors directly.

## 6. Exact scope of the no-go

**Proved**

- The exact fixed-shift exterior transfer (2.4).
- The adjacent integer determinant and all-depth divisibility (2.5)--(2.6).
- The nonzero adjacent cross-saddle coefficient (3.6).
- The exact bases $\rho_*^2$ and $R_*^2$.
- The degree-two shifted identity (4.5), including exact coefficients and
  nonzero critical resultants.
- Zero booking and zero capacity reduction.

**Scoped no-go**

- The adjacent $2\times2$ determinant is worse as a one-row bound and
  exactly matches the existing cost after its two row gcds are charged.
- The first natural degree-two critical-value reduction saves only a
  polynomial factor and is not a one-row gcd carrier.

**Open**

- Larger fixed windows for which a genuinely new arithmetic divisibility
  appears.
- Growing windows, adaptive recurrences, and modular resultants.
- Any carrier with a strict per-contained-gcd base below $R_*$.
- The theorem $\log c_m^>=o(m)$, Route 1, and every claim about
  irrationality of $e+\pi$.

## 7. Deterministic replay

The standard-library checker verifies all pinned dependency hashes, the
exact rational reduction, the two exact resultants, Item 200's full
$F_m$, and rows $1\le m\le24$ of (2.1), (2.2), (2.5), (2.6), and
(4.5).  Those finite rows normalize the formulas only; the asymptotic
statement is the symbolic saddle proof in Section 3.

From the research root:

~~~text
python work/item425_adjacent_transfer_certificate.py --output work/item425_adjacent_transfer_certificate.json
python work/item425_adjacent_transfer_certificate.py --replay work/item425_adjacent_transfer_certificate.json --output work/item425_adjacent_transfer_certificate_replay.json
~~~

## 8. Pinned dependencies

| Dependency | SHA-256 |
|---|---|
| sources/item390_mixed_cubic_fresh_primitive_saturation_report.md | 5bfb3c871b12524f672df515e920236f2470145d4f68bdcd7b47f29408692f46 |
| results/item390_mixed_cubic_fresh_primitive_saturation_certificate.json | 45b61f683a29305e4fcfd8810f146068f950070496e8e88a2a6b800f9dc1ada6 |
| sources/item415_marked_selector_compulsory_strip_report.md | da79ea786471a6abb35288f242a0b0b2307a695bd9352eaa3c4e2033fc701777 |
| results/item415_marked_selector_compulsory_strip_certificate.json | af731cf70e9a6d40cab380d38d5b404786cefef196eb42f743634b8d390cb29e |
| sources/item418_normalized_large_carrier_report.md | 5b490e38d127deec51cac34a80c6856ed824534daad8fc3a387fe6cbb7f7db68 |
| results/item418_normalized_large_carrier_certificate.json | bcea1e6be723e48e3d1ca63bc5644b208059e5138799108ea403b0ba5d789075 |
| sources/item420_normalized_contour_extension_report.md | eebbcd02c654d6be1ca6ae50e427931abc16aae773300b4d1f32dc8f2291a414 |
| results/item420_normalized_contour_extension_certificate.json | ddac30da2c3c7ebca84cce7c412f99c05b6d6281a5598c2346f33b50efe18095 |
| work/item423_polynomial_bezout_no_go_report.md | fddb0af24dd970dd3835aad6688a02d3da277cf854781c822875698d2d2350a6 |
| work/item423_polynomial_bezout_no_go_certificate.json | 3ccb1fadac9f770cc999af24cb1781dd4c875bcaea3d01c252de94c725ad08aa |

## 9. Ledger label

This item is work-only and carries



$$
\boxed{\text{PROVED SCOPED NO-GO; ZERO LEDGER; NO IRRATIONALITY CLAIM}.}
                                                               \tag{9.1}
$$


