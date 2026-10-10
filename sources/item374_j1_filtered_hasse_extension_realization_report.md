> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 374 — exact filtered-Hasse realization of the fixed-$j=1$ transverse coordinate

Date: 2026-09-01

## 1. Outcome and capacity first

The actual selector is



$$
p=4h+6s+3,\qquad M=3h+4s+2,\qquad
n=2h,\qquad r=2s+1.                                    \tag{1.1}
$$



Items 360 and 369 give the one-way gate



$$
\text{full ordinary collision}
\Longrightarrow a_{r,n}=0,\qquad Q_0(h,s)=0\pmod p.      \tag{1.2}
$$



Item 371 showed that $Q_0$ cannot be the *full determinant* of the
direct lisse or fixed-normalization crystalline architectures considered
there.  This item asks whether it can instead be a graded Hasse invariant
or filtered extension coordinate while full Frobenius remains invertible
after $p$ is inverted.

The answer is yes, exactly and in minimal rank.

For any lift $\widetilde Q\in W(\mathbb F_p)=\mathbb Z_p$ of
$Q_0\in\mathbb F_p$, there is a rank-two strongly generated filtered
Frobenius module



$$
M=W e_1\oplus W e_2,\qquad
\operatorname {Fil}^1M=W e_1,                            \tag{1.3}
$$



with divided and full Frobenius



$$
\varphi_1(e_1)=e_1+\widetilde Qe_2,\qquad
\varphi_0(e_1)=p\varphi_1(e_1),\qquad
\varphi_0(e_2)=e_2.                                      \tag{1.4}
$$



Its full Frobenius matrix is



$$
\Phi_{\widetilde Q}
=\begin{bmatrix}p&0\\p\widetilde Q&1\end{bmatrix},
\qquad \det\Phi_{\widetilde Q}=p.                        \tag{1.5}
$$



Thus it is an isogeny after inverting $p$, with fixed Hodge weights
$(0,1)$.  But the graded Hasse map



$$
\operatorname {Fil}^1M/p
\xrightarrow{\ \overline{\varphi}_1\ }M/p
\longrightarrow M/(\operatorname {Fil}^1M+pM)            \tag{1.6}
$$



is multiplication by



$$
\boxed{\operatorname {Ha}(\Phi_{\widetilde Q})=Q_0.}     \tag{1.7}
$$



Hence $Q_0=0$ is an exact target-forced Hasse divisor while the full
Frobenius isocrystal stays invertible.

There is also an exact residue-level multiplicative realization.  Put



$$
U(t)=\begin{bmatrix}1&0\\t&1\end{bmatrix}.               \tag{1.8}
$$



Then



$$
U(x)U(y)=U(x+y),\qquad\det U(t)=1.                       \tag{1.9}
$$



Item 369's additive local transverse moment therefore becomes a product
of invertible unipotent extension factors.  This is the precise way in
which the Hasse-extension route escapes Item 371's determinant-product
obstruction.

However, the construction is horizontally information-neutral.  Every
residue $q$ can be inserted in (1.4), the full Frobenius polynomial is



$$
\chi_{\Phi}(X)=(X-p)(X-1)                                \tag{1.10}
$$



for every $q$, and the pointwise product has quadratically many
nonidentity factors.  No prime-independent geometric family,
bounded-support compression, or horizontal distribution theorem is
obtained.

Thus



$$
\boxed{
\text{new target-forced Hasse realization}=1,\quad
\text{new independent collision condition}=0,\quad
\text{booking}=0.}                                       \tag{1.11}
$$



The raw reach is the full



$$
{M\over6}+o(M),\qquad {1\over36}\text{ per }6M,           \tag{1.12}
$$



but the $1/36$ ceiling is retained and Route 1 remains ACTIVE.

## 2. A minimal strongly generated filtered Frobenius module

Let $k=\mathbb F_p$ and $W=W(k)=\mathbb Z_p$.  Witt Frobenius is the
identity on $W$, and choose any lift
$\widetilde Q\in\mathbb Z_p$ of $Q_0$.

Define



$$
\operatorname {Fil}^0M=M,\qquad
\operatorname {Fil}^1M=We_1,\qquad
\operatorname {Fil}^2M=0.                               \tag{2.1}
$$



The maps in (1.4) are $\sigma$-semilinear and satisfy the exact
Fontaine--Laffaille relation



$$
\varphi_0|_{\operatorname {Fil}^1}=p\varphi_1.           \tag{2.2}
$$



Moreover,



$$
\left[\varphi_1(e_1),\varphi_0(e_2)\right]
=\begin{bmatrix}1&0\\\widetilde Q&1\end{bmatrix},        \tag{2.3}
$$



whose determinant is one.  Hence the divided Frobenius images generate
$M$.  This is the strong-generation condition, not merely an arbitrary
matrix with one selected entry.

The full map has determinant $p$, so



$$
\varphi_0:\sigma^*M[1/p]\xrightarrow{\sim}M[1/p].        \tag{2.4}
$$



The filtration dimensions and determinant valuation are independent of
$h,s,p$; the Hodge polygon has weights $0,1$ on every row.

Reducing (2.3) modulo $p$ and projecting the first column to
$M/(\operatorname {Fil}^1+pM)$ gives $Q_0\bar e_2$.  This proves
(1.7).

Rank two is minimal for this graded-Hasse architecture.  In rank one,
either $\operatorname {Fil}^1=0$ or
$\operatorname {Fil}^1=M$; one of the source and target of (1.6) is
zero.  Rank two is the first rank in which the graded map can have a
nontrivial scalar vanishing divisor.

## 3. Principal-minor and extension formulations

At the purely algebraic level,



$$
P(q)=\begin{bmatrix}q&-1\\1&0\end{bmatrix}\in
\operatorname {SL}_2                                      \tag{3.1}
$$



has principal $1\times1$ minor $q$.  Thus even a principal-minor
realization with invertible full matrix is possible in rank two.

But (3.1) is basis-dependent packaging.  The filtered construction is
stronger: the zero of $q$ is the zero of the canonical graded map (1.6)
relative to the fixed filtration.

There is also an extension interpretation.  The residue unipotent matrix



$$
U(q)=\begin{bmatrix}1&0\\q&1\end{bmatrix}                \tag{3.2}
$$



is an extension of two trivial graded factors.  It is the identity exactly
when $q=0$.  For $q\ne0$, its semisimplification is still
$\mathbf1\oplus\mathbf1$, but the extension is nontrivial relative to
the chosen flag.  Thus the Hasse condition is extension splitting, not an
eigenvalue or determinant condition.

The full filtered Frobenius makes this distinction even sharper.  Put



$$
D=\operatorname {diag}(p,1),\qquad
\Phi_{\widetilde Q}=U(\widetilde Q)D.                    \tag{3.3}
$$



With



$$
b={p\widetilde Q\over p-1},                              \tag{3.4}
$$



one checks over the isocrystal that



$$
U(b)^{-1}\Phi_{\widetilde Q}U(b)=D.                      \tag{3.5}
$$



So the unfiltered isocrystal and its characteristic polynomial are the
same for every $Q_0$.  The parameter survives only in the relative
filtered/divided-Frobenius position.  Standard semisimple compatible-system
data cannot see it.

## 4. The additive moment becomes a unipotent product

Retain Item 369's exact local entry



$$
R(x)=2x^{-T}F_Q(x)-x^{-L}F_Q(x),                         \tag{4.1}
$$



over $\mathbb F_{p^2}^{\times}$, for which



$$
\sum_x R(x)=-Q_0.                                        \tag{4.2}
$$



Because all matrices $U(t)$ lie in the same one-parameter unipotent
root group, they commute and (1.9) iterates:



$$
\boxed{
\prod_{x\in\mathbb F_{p^2}^{\times}}U(-R(x))
=U\!\left(-\sum_xR(x)\right)=U(Q_0).}                   \tag{4.3}
$$



Every factor and the product have determinant one.  Thus the transverse
additive cancellation really can be a multiplicative *extension class*,
even though it cannot be a multiplicative full determinant.

Grouping the two extracted coefficients gives the shorter identity



$$
U(2c_T)U(-c_L)=U(2c_T-c_L)=U(Q_0).                      \tag{4.4}
$$



But (4.4) is not a bounded-support local construction: $c_T$ and
$c_L$ are already global complete-moment coefficients.  The genuinely
pointwise product (4.3) has $p^2-1$ factors.  Compressing it to one factor
$U(Q_0)$ computes the target globally and is information-neutral.

In fact almost all pointwise factors are nonidentity.  For $x\ne0$,



$$
R(x)=x^{-L}P_0(x)\mathscr L_p(x^2)
\bigl(2x^{L-T}-1\bigr).                                  \tag{4.5}
$$



The three factors on the right have at most



$$
4,\qquad 2(p-1),\qquad |L-T|=2|h-s|                     \tag{4.6}
$$



distinct zeros, respectively.  Hence



$$
\#\{x\in\mathbb F_{p^2}^{\times}:R(x)\ne0\}
\ge p^2-1-\bigl(4+2(p-1)+2|h-s|\bigr).                  \tag{4.7}
$$



Since $2|h-s|<p$, the lower bound is $p^2-O(p)$.
Thus (4.3) is a genuinely growing-support product, not merely a notation
with many identity factors.

This precisely locates the remaining problem.  Rank is bounded, but
geometric support or horizontal complexity is not.

## 5. A genuine rowwise filtered object is not yet a compatible family

For every $q\in\mathbb F_p$, equations (1.3)--(1.7) produce a valid
rank-two filtered Frobenius object with the same Hodge polygon and full
isocrystal polynomial.  Therefore fixed rank and fixed Hodge polygon alone
place no restriction on the Hasse coordinate:



$$
\boxed{
\text{the fixed-Hodge moduli contains an affine coordinate }q
\text{ whose Hasse divisor is }q=0.}                    \tag{5.1}
$$



Given any finite set of rows and any prescribed residue values, the
rowwise construction simply inserts those values as $q$.  Consequently
no universal nonvanishing or zero-density theorem can follow from rank,
Hodge numbers, strong generation, or full Frobenius invertibility alone.

For the actual family, the selector map into this affine Hasse coordinate
is



$$
(h,s,p)\longmapsto q=Q_0(h,s)\pmod p.                    \tag{5.2}
$$



Bounding the pullback of $q=0$ along (5.2) is exactly the original
weighted-zero problem.  The rowwise module has not simplified that map.

A genuine horizontal advance would require one prime-independent
geometric filtered $F$-crystal or compatible nonsemisimple extension,
with:

1. a bounded-complexity base and connection;
2. a uniform construction of (5.2), rather than insertion of its value;
3. controlled conductor or monodromy; and
4. a nonconcentration theorem for its Hasse divisor.

None is constructed here.  In particular, the constant full polynomial
$(X-p)(X-1)$ gives no Chebotarev statistic for $Q_0$: every value has
the same semisimplification.

The fixed graded pieces are Tate-type pieces with Frobenius eigenvalues
$p$ and $1$.  Thus a genuine compatible lift would have to be a
nonsemisimple extension of those pieces whose local
Fontaine--Laffaille class is exactly $Q_0$.  The condition $Q_0=0$
would then be local splitting of the extension.  Ordinary Chebotarev
applied to the semisimplification cannot count those splitting primes,
because its characteristic polynomial is constant.  The needed input is
an extension-class, Selmer/Kummer, or framed-monodromy distribution
theorem together with an exact global bridge to the actual period.

## 6. The residue product has no canonical naive Teichmüller lift

The exact product (4.3) lives in characteristic $p$.  A naive attempt to
lift each residue entry by its Teichmüller representative fails because
Teichmüller representatives are multiplicative, not additive:



$$
[x]+[y]\ne[x+y]\pmod {p^2}                               \tag{6.1}
$$



in general.  Thus



$$
U([x])U([y])=U([x]+[y])
\ne U([x+y])                                              \tag{6.2}
$$



without a Witt carry.

This failure occurs on the declared actual rows.  At
$(h,s,p)=(1,1,13)$,



$$
2c_T=5,\qquad -c_L=4,\qquad Q_0=9\pmod {13}.             \tag{6.3}
$$



Modulo $13^2$, their Teichmüller lifts are



$$
[5]=70,\qquad[4]=147,\qquad[9]=22,                       \tag{6.4}
$$



so



$$
[5]+[4]-[9]=26=2p\pmod {p^2}.                            \tag{6.5}
$$



The certificate records the corresponding carry digits on all four
predeclared rows.  This is not a no-go for all crystalline lifts: one may
choose another lift $\widetilde Q$, or incorporate the Witt carry in a
more structured extension.  It proves only that the residue-level local
product does not automatically supply a canonical Teichmüller-compatible
horizontal lift.

## 7. Literal Kummer and Artin--Schreier cases remain separate

This item does not reopen the literal constructions closed in Items 366
and 371:

- literal full-order Kummerization of
  $\mathscr L_p(z^2)$ has at least $p-2$ ramification points;
- the literal Artin--Schreier polynomial has Swan conductor $2(p-1)$.

Those are conductor-growth theorems for specific realizations.  The
filtered module (1.3)--(1.7) is a different, nonliteral extension
packaging.  Its open problem is to construct a prime-independent geometric
origin for $Q_0$, not to repeat the closed literal calculations.

## 8. Declared exact controls

Only the four rows predeclared before Item 374 are used.  No prime or
collision scan is performed.

| $(h,s,p)$ | $M$ | $(a_{r,n},Q_0)$ | $(2c_T,-c_L)$ | Teichmüller carry digit |
|---|---:|---:|---:|---:|
| $(1,1,13)$ | $9$ | $(0,9)$ | $(5,4)$ | $2$ |
| $(2,1,17)$ | $12$ | $(8,14)$ | $(4,10)$ | $11$ |
| $(8,2,47)$ | $34$ | $(0,30)$ | $(25,5)$ | $17$ |
| $(10,11,109)$ | $76$ | $(70,0)$ | $(11,98)$ | $0$ |

For each row the certificate independently verifies:

1. $Q_0=2c_T-c_L$;
2. $U(2c_T)U(-c_L)=U(Q_0)$;
3. the filtered module relation and strong-generation determinant;
4. the full determinant $p$;
5. the graded Hasse coordinate $Q_0$; and
6. the first Teichmüller carry modulo $p^2$.

The controls are exact algebra only.  No row is promoted to a full
collision or a density statement.

## 9. Capacity audit and the remaining theorem

Let $\operatorname {Ha}_{h,s}=Q_0(h,s)$ be the Hasse coordinate in
(1.7), and define



$$
\mathcal W_{\rm filt}(M)
=\sum_{\substack{s\in\mathcal S_M,\ p_s\ \mathrm{prime}\\
a_{2s+1,2h_s}=0\ (\mathrm{mod}\ p_s)\\
\operatorname {Ha}_{h_s,s}=0\ (\mathrm{mod}\ p_s)}}
\log p_s.                                                \tag{9.1}
$$



This is exactly the previous joint envelope:



$$
\mathcal W_{\rm filt}(M)=\mathcal W_{H,Q}(M),\qquad
\mathcal W_{\rm full}(M)\leq\mathcal W_{\rm filt}(M).     \tag{9.2}
$$



The desired theorem remains



$$
\boxed{\mathcal W_{\rm filt}(M)=o(M).}                   \tag{9.3}
$$



It would remove the full $1/36$ ceiling.  A strict constant below
$M/6$ would yield a partial saving.

The exact filtered realization passes the rank and fixed-Hodge admission
tests, but it does not pass the horizontal-compatibility test: its Hasse
coordinate was inserted from the target itself.  Therefore it receives no
mass credit.

## 10. Strict decision

### PROVED

- the exact minimal rank-two strongly generated filtered Frobenius module
  with graded Hasse invariant $Q_0$;
- full Frobenius determinant $p$, fixed Hodge weights $(0,1)$, and
  invertibility after $p$ is inverted;
- the exact residue-level unipotent local-product realization (4.3);
- the quadratic lower bound (4.7) for its nonidentity factors;
- full characteristic-polynomial and semisimplification blindness to
  $Q_0$;
- fixed-rank/fixed-Hodge information-neutrality;
- nontrivial naive Teichmüller lift carries on declared actual rows;
- zero booking.

### EXACT FINITE ONLY

- four predeclared filtered-module and Witt-carry controls;
- no prime scan, full-collision claim, or density inference.

### OPEN

- a prime-independent geometric filtered/crystalline compatible extension
  realizing $Q_0$;
- a nonliteral bounded-conductor unipotent or cohomological compression;
- horizontal distribution of the filtered extension/Hasse coordinate;
- weighted joint-zero density, any strict fixed-$j=1$ ceiling reduction,
  Route 1, and every conclusion about $e+\pi$.

## 11. Ledger consequence



$$
\begin{array}{c|c}
\text{quantity}&\text{Item 374 value}\\ \hline
\text{actual rows reached}&\text{all}\\
\text{new exact Hasse realization}&1\\
\text{new independent collision condition}&0\\
\text{new proved excluded log mass}&0\\
\text{new fixed-}j=1\text{ capacity reduction}&0\\
\text{retained fixed-}j=1\text{ ceiling per }6M&1/36
\end{array}                                               \tag{11.1}
$$



Item 374 proves that the Hasse-subdeterminant route is algebraically viable
and escapes the full-determinant obstruction.  It also shows why this is
not yet ledger progress: fixed Hodge data can carry an arbitrary extension
coordinate, while standard compatible-system polynomials forget it.
