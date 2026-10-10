> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 355 - target-residual Parseval and the fixed-$M$ selector obstruction

Checked: 2026-09-01 (Beijing time)

## 1. Scope, capacity, and verdict

Retain the actual ordinary-$j=2$ nondegenerate collision from Items
341 and 352,



$$
p=2r+6s+3,
 \qquad L=s=m+1,
 \qquad
 \boxed{4^L=c_r^*,\quad H_{L-1}=\Theta_{r,L}\pmod p}.
\tag{1.1}
$$



Item 347 proved that the exact Kummer lift has rank at least $L$, and
Item 352 proved the complementary rank-pole tradeoff for exact
nonsemisimple companions.  On the positive-rate bulk $L\asymp M$, so
the remaining natural possibility is a second-moment or large-sieve
theorem for this linearly growing-conductor family.

This item derives the exact second moments.  They expose a sharp
selector obstruction rather than a weighted-density gain.

> **PROVED - exact target-retaining residual Parseval identity.**  For
> a fixed prime $p$, let $\mathcal A_p^{\rm nd}$ be the admissible
> nondegenerate $L$-values, and put
> 

$$
> \Delta_p(L)=
> \bigl(4^L-c_{r(L)}^*,\ H_{L-1}-\Theta_{r(L),L}\bigr)
> \in\mathbf F_p^2.
>
$$


> For arbitrary complex weights $\alpha_L$,
> 

$$
> \boxed{
> \frac1{p^2}\sum_{a,b\in\mathbf F_p}
> \left|\sum_{L\in\mathcal A_p^{\rm nd}}
> \alpha_L\,e_p\!\left(a\Delta_{p,1}(L)+b\Delta_{p,2}(L)\right)
> \right|^2
> =\sum_{y\in\mathbf F_p^2}
> \left|\sum_{\Delta_p(L)=y}\alpha_L\right|^2.}
>
$$


> No target has been frozen or discarded: both actual moving target
> coordinates occur inside $\Delta_p(L)$.

> **PROVED - exact fixed-$M$ selector saturation.**  For fixed $M$
> and $p$, the tied equations select at most one row,
> 

$$
> L_{M,p}=\frac{5p-4M-1}{2}.
>
$$


> On this singleton the Fourier summand has modulus one for every
> $(a,b)$, whether or not the collision occurs.  Therefore its
> normalized second moment is identically $1$.  Summing with
> $\log p$ over the raw interval gives exactly the raw prime mass,
> potentially $(2/35)M+o(M)$.  The magnitude-square large sieve is
> literally blind to the selected collision indicator.

> **PROVED - even minimal transverse energy can leave a full selected
> diagonal.**  The residual collision energy
> 

$$
> E_p=\sum_yN_p(y)^2,
> \qquad N_p(y)=\#\{L:\Delta_p(L)=y\},
>
$$


> has the minimum $|\mathcal A_p^{\rm nd}|$ when all residuals are
> distinct.  Nevertheless one may place the unique zero residual at
> the prescribed selector $L_{M,p}$ for every $p$.  Thus an optimal
> within-prime energy bound alone does not imply a uniform theorem for
> a specified fixed-$M$ diagonal.  This is a method-class example, not
> a claim that the actual targets are arbitrary.

> **PROVED - exact Kummer/Jacobi second moment.**  With
> $N=p-1$, Teichmuller character $\omega$, quadratic character
> $\varphi=\omega^{N/2}$, and
> 

$$
> j_u=-\omega^{-u}(2)J(\omega^{-u},\varphi),
>
$$


> one has
> 

$$
> \sum_{u=0}^{N-1}|j_u|^2=N(N-1).
>
$$


> For every actual $L<N/2$, the Kummer translates
> 

$$
> P_L(a)=\sum_{u=0}^{L-1}\zeta^{au}j_u
>
$$


> satisfy
> 

$$
> \boxed{
> \sum_{a\bmod N}|P_L(a)-\theta|^2
> =N\bigl((L-1)p+|1-\theta|^2\bigr)}
>
$$


> for every fixed complex target $\theta$.  This clean identity is
> transverse to the actual row: the actual prefix is $a=0$, while
> the target is a selected-prime residue.  It does not control
> divisibility at that prime.

> **PROVED - moving-target Fourier obstruction.**  If the target is
> allowed to vary with the Kummer translate, Parseval remains exact but
> contains the complete Fourier transform of the target.  The cross
> term can align perfectly with $P_L(a)$; no target-independent lower
> bound survives.  If instead one averages over the actual admissible
> parameter $L$, the residual identity above retains the target but
> fixed $M$ extracts one deterministic point from each different
> finite field.

> **OPEN.**  A selector-aware cross-prime theorem for the actual
> residuals could still succeed.  Likewise, a power-saving bound for
> $E_p$ could give an almost-all-$M$ exceptional-set estimate after
> averaging in $M$.  Neither theorem follows from the exact identities
> here.

Consequently



$$
\boxed{\text{new booking}=0},
 \qquad
 \boxed{\text{new capacity reduction}=0},
 \qquad
 \boxed{\text{ordinary-}j=2\text{ ceiling remains }1/105}.
\tag{1.2}
$$



No finite prime census is used.

## 2. The admissible parameter family and the fixed-$M$ selector

For a fixed odd prime $p$, define



$$
r_p(L)=\frac{p-6L-3}{2}.
\tag{2.1}
$$



Let $\mathcal A_p$ consist of positive integers $L$ for which
$r_p(L)\ge1$ is odd and $3\nmid r_p(L)$.  On the nondegenerate
chart also require



$$
\ell_{r_p(L)}\ne0\pmod p,
\tag{2.2}
$$



and call the resulting set $\mathcal A_p^{\rm nd}$.  Every displayed
target denominator is a $p$-unit by the audits in Item 341, so the
residual map



$$
\boxed{
 \Delta_p(L)=
 \left(
 4^L-c_{r_p(L)}^*,
 H_{L-1}-\Theta_{r_p(L),L}
 \right)\in\mathbf F_p^2}
\tag{2.3}
$$



is well-defined.  The actual collision is exactly



$$
\Delta_p(L)=(0,0).
\tag{2.4}
$$



In Item 352's complete-matrix notation this is precisely



$$
\left(
 \det(A_{1/4}^L)-c_{r_p(L)}^*,
 (\mathscr M_L)_{12}+\Theta_{r_p(L),L}
 \right)
 =\bigl(\Delta_{p,1}(L),-\Delta_{p,2}(L)\bigr).
\tag{2.5}
$$



Thus the residual Parseval identity below is an identity for the two
actual target-shifted matrix coordinates, not merely for an auxiliary
state sequence.

The fixed-$M$ relation is



$$
2M=5r+14L+7.
\tag{2.6}
$$



Substituting (2.1) gives the mutually inverse formulas



$$
\boxed{
 M=\frac{5p-2L-1}{4},
 \qquad
 L=L_{M,p}=\frac{5p-4M-1}{2}.}
\tag{2.7}
$$



Thus fixing $p$ and varying $L$ is a transverse average over many
different $M$-values.  Fixing $M$ returns to at most one admissible
$L$ for each prime.  This change in geometry is the source of the
large-sieve obstruction below.

## 3. Exact target-retaining residual Parseval

Let



$$
e_p(t)=\exp(2\pi i t/p).
\tag{3.1}
$$



For arbitrary coefficients $\alpha_L\in\mathbf C$, put



$$
S_p(a,b;\alpha)
 =\sum_{L\in\mathcal A_p^{\rm nd}}
 \alpha_L e_p\!\left(
 a\Delta_{p,1}(L)+b\Delta_{p,2}(L)
 \right).
\tag{3.2}
$$



Expanding the square and using additive orthogonality in both
coordinates gives



$$
\begin{aligned}
 \frac1{p^2}\sum_{a,b}|S_p(a,b;\alpha)|^2
 &=\sum_{L,L'}\alpha_L\overline{\alpha_{L'}}
   1_{\Delta_p(L)=\Delta_p(L')}\\
 &=\sum_{y\in\mathbf F_p^2}
   \left|\sum_{\Delta_p(L)=y}\alpha_L\right|^2.
 \end{aligned}
\tag{3.3}
$$



This proves the advertised exact identity.  It is a large-sieve
**equality**, with the collision multiplicities on the right.

Taking $\alpha_L=1$, define



$$
N_p(y)=\#\{L\in\mathcal A_p^{\rm nd}:\Delta_p(L)=y\},
 \qquad
 E_p=\sum_yN_p(y)^2.
\tag{3.4}
$$



Then



$$
\boxed{
 E_p=\#\{(L,L'):\Delta_p(L)=\Delta_p(L')\}
 =\frac1{p^2}\sum_{a,b}|S_p(a,b;1)|^2.}
\tag{3.5}
$$



The actual zero count also has exact Fourier inversion:



$$
\boxed{
 N_p(0)=\frac1{p^2}\sum_{a,b}S_p(a,b;1).}
\tag{3.6}
$$



Equations (3.5) and (3.6) must not be confused.  The second moment loses
the phases whose coherent alignment detects the zero residual.

The general inequalities are only



$$
|\mathcal A_p^{\rm nd}|\le E_p
 \le|\mathcal A_p^{\rm nd}|^2,
 \qquad
 N_p(0)^2\le E_p.
\tag{3.7}
$$



No power saving over the upper endpoint follows from orthogonality
alone.

## 4. The singleton second moment is collision-blind

Fix $M$.  For each prime in the raw interval, (2.7) selects at most
one $L_{M,p}$.  On the nondegenerate chart write



$$
\delta_{M,p}=\Delta_p(L_{M,p}),
 \qquad
 s_{M,p}(a,b)=e_p(a\delta_{M,p,1}+b\delta_{M,p,2}).
\tag{4.1}
$$



For every $(a,b)$,



$$
|s_{M,p}(a,b)|^2=1.
\tag{4.2}
$$



Therefore



$$
\boxed{
 \frac1{p^2}\sum_{a,b}|s_{M,p}(a,b)|^2=1}
\tag{4.3}
$$



both when $\delta_{M,p}=0$ and when $\delta_{M,p}\ne0$.  By
contrast,



$$
\frac1{p^2}\sum_{a,b}s_{M,p}(a,b)
 =1_{\delta_{M,p}=0}.
\tag{4.4}
$$



Thus the target-retaining first moment is exact but is precisely the
unsolved collision indicator; the magnitude-square second moment is
independent of it.

Let $\mathcal P_M^{\rm nd}$ be the selected nondegenerate primes in
the fixed-$M$ interval.  Weighting (4.3) gives



$$
\boxed{
 \mathcal Q_M
 :=\sum_{p\in\mathcal P_M^{\rm nd}}
 \frac{\log p}{p^2}\sum_{a,b}|s_{M,p}(a,b)|^2
 =\sum_{p\in\mathcal P_M^{\rm nd}}\log p.}
\tag{4.5}
$$



The right side can occupy the full raw mass



$$
\frac{2}{35}M+o(M).
\tag{4.6}
$$



This is stronger than saying that Cauchy-Schwarz is too weak: the
canonical fixed-$M$ second moment equals the available capacity
regardless of which primes collide.

## 5. Minimal transverse energy does not control a prescribed diagonal

The minimum possible value of (3.4) is



$$
E_p=|\mathcal A_p^{\rm nd}|,
\tag{5.1}
$$



attained when the residuals are pairwise distinct.  Since
$|\mathcal A_p^{\rm nd}|<p^2$, pairwise distinct residuals can include
any prescribed placement of the zero cell.  In particular, for a fixed
$M$, one can have



$$
\Delta_p(L_{M,p})=0
\tag{5.2}
$$



at every selected prime while all other residuals are distinct.  Then
(5.1) is optimal but the fixed-$M$ collision mass is still (4.6).

This construction is a formal test of what the statistic $E_p$ can
imply.  It does **not** replace the actual formulas for
$c_r^*$ and $\Theta_{r,L}$, and it is not evidence that the actual
family behaves adversarially.  It proves only the scoped statement



$$
\boxed{
 \text{within-prime residual energy alone cannot give a uniform bound
 on a prescribed fixed-}M\text{ selector}.}
\tag{5.3}
$$



An arithmetic theorem showing that the actual selector cannot align
with the zero cells would be new information, not a consequence of
Parseval.

## 6. Exact Kummer/Jacobi energy

The same obstruction appears in the chosen-prime Kummer model, even
though its Archimedean second moment can be evaluated exactly.  Put



$$
N=p-1,
 \qquad
 \varphi=\omega^{N/2},
 \qquad
 j_u=-\omega^{-u}(2)J(\omega^{-u},\varphi)
 \quad(0\le u<N).
\tag{6.1}
$$



The two exceptional Jacobi sums occur at $u=0$ and $u=N/2$:



$$
|j_0|^2=|j_{N/2}|^2=1.
\tag{6.2}
$$



For the other $N-2$ modes, the two characters and their product are
nontrivial, so



$$
|j_u|^2=p.
\tag{6.3}
$$



Consequently



$$
\boxed{
 \sum_{u=0}^{N-1}|j_u|^2
 =2+(N-2)p=N(N-1).}
\tag{6.4}
$$



Every actual $L$ satisfies $L<N/2$, so the prefix contains $u=0$
but not the second exceptional mode.  If $\zeta$ is a primitive
$N$-th root and



$$
P_L(a)=\sum_{u=0}^{L-1}\zeta^{au}j_u,
 \qquad a\in\mathbf Z/N\mathbf Z,
\tag{6.5}
$$



ordinary Fourier Parseval gives



$$
\boxed{
 \sum_{a\bmod N}|P_L(a)|^2
 =N\bigl(1+(L-1)p\bigr).}
\tag{6.6}
$$



Moreover $j_0=1$ exactly.  Hence



$$
\sum_aP_L(a)=N,
\tag{6.7}
$$



and for every fixed complex target $\theta$,



$$
\boxed{
 \sum_{a\bmod N}|P_L(a)-\theta|^2
 =N\left((L-1)p+|1-\theta|^2\right).}
\tag{6.8}
$$



At the selected prime $\mathfrak P\mid p$, Item 347 gives



$$
P_L(0)=\sum_{u=0}^{L-1}j_u
 \equiv H_{L-1}\pmod{\mathfrak P}.
\tag{6.9}
$$



Thus (6.8) is an exact second moment of the same Kummer modes, with a
fixed target retained.  Yet it averages over the artificial translate
$a$, while the actual state is the single point $a=0$.  It is also
an Archimedean identity, whereas (6.9) asks for divisibility at the
chosen prime.  No inequality from (6.8) converts those two distinct
questions.

On the positive-rate bulk $L\asymp p$, the average square in (6.6) is
$1+(L-1)p\asymp p^2$.  The exact identity exhibits the linear
conductor rather than removing it.

## 7. What happens when the target also moves

Suppose one assigns a complex target $\theta_a$ to every Kummer
translate and defines



$$
\widehat\theta_u
 =\frac1N\sum_{a\bmod N}\theta_a\zeta^{-au}.
\tag{7.1}
$$



Parseval gives the exact target-retaining formula



$$
\boxed{
 \sum_a|P_L(a)-\theta_a|^2
 =N\sum_{u\bmod N}
 \left|1_{0\le u<L}j_u-\widehat\theta_u\right|^2.}
\tag{7.2}
$$



The clean diagonal energy (6.8) is lost: every Fourier coefficient of
the moving target appears.  In the extreme case $\theta_a=P_L(a)$,
the right side is zero.  Therefore no lower bound independent of target
arithmetic is possible.

The actual target $\Theta_{r,L}$ is tied to the admissible parameter
$L$, not to a canonical Kummer translate $a$.  Extending it to all
$a$ would be arbitrary.  Averaging over the genuine parameter $L$
instead leads back to (3.3), which retains the target exactly but is
transverse to fixed $M$.

This proves the promised dichotomy:



$$
\boxed{
 \begin{array}{ll}
 \text{clean Kummer second moment} &\Longrightarrow
   \text{fixed/transverse target and selected-prime mismatch},\\
 \text{actual moving target retained} &\Longrightarrow
   \text{unknown residual energy and a singleton fixed-}M\text{ selector}.
 \end{array}}
\tag{7.3}
$$



## 8. Possible almost-all-$M$ route and its missing input

Varying $M$ as well as $p$ reassembles the transverse family.  Each
pair $(p,L)$ determines one $M$ by (2.7), so schematically



$$
\sum_M W_{\rm nd}(M)
 =\sum_p(\log p)N_p(0)
\tag{8.1}
$$



over matching dyadic ranges and congruence restrictions.  From (3.7),



$$
N_p(0)\le\sqrt{E_p}.
\tag{8.2}
$$



Therefore a genuine power-saving theorem



$$
\sum_{p\asymp X}(\log p)\sqrt{E_p}=o(X^2)
\tag{8.3}
$$



would imply an almost-all-$M$ exceptional-set gain after averaging
over $M\asymp X$.  Such a result could be strategically relevant if
the main irrationality construction is permitted to select a good
subsequence.

The exact identity alone supplies only



$$
E_p\le|\mathcal A_p^{\rm nd}|^2=O(p^2),
\tag{8.4}
$$



which makes the left side of (8.3) merely $O(X^2)$.  There is no
little-$o$ gain.  Proving (8.3), or proving a uniform fixed-$M$
selector theorem directly, requires arithmetic nonconcentration of the
actual targets.

Accordingly, the first missing inputs are either

1. a power-saving collision-energy theorem for the actual residual map
   $\Delta_p(L)$, together with a justified almost-all-$M$ use in
   the main construction; or
2. a selector-aware cross-prime estimate for
   $\Delta_p(L_{M,p})=0$ uniformly in the required $M$-family.

Neither is a bounded-conductor sheaf statement: Items 347 and 352 show
that the exact conductor/rank-pole budget grows linearly on the bulk.

## 9. Capacity and chart-overlap audit

The raw fixed-$M$ interval is



$$
\frac{4M+3}{5}\le p\le\frac{6M-1}{7},
\tag{9.1}
$$



with logarithmic prime mass



$$
\frac{2}{35}M+o(M).
\tag{9.2}
$$



Item 355 treats only the nondegenerate chart $\ell_r\ne0$.  Item
349's degenerate chart is disjoint at each selected prime but lies in
the same interval.  Hence



$$
W_{\rm nd}(M)+W_{\rm deg}(M)
 \le\frac{2}{35}M+o(M),
\tag{9.3}
$$



and their capacities are not additive.  The singleton energy (4.5)
can equal the full right side of (9.3), so no strict ceiling reduction
has been proved.  Dividing by $6M$ leaves



$$
\frac1{105}.
\tag{9.4}
$$



There is no new divisor, no new lower bound, and no weighted exceptional
set for the actual fixed-$M$ family.

## 10. Strict labels and deterministic replay

The companion certificate verifies:

- the exact fixed-$M$ selector identities on seven declared actual
  nondegenerate rows from Item 341;
- collision-independence of the singleton second moment;
- exact occupancy, pair-count, and weighted residual-energy identities
  on declared combinatorial families;
- the full and prefix Jacobi energy counts in the actual range;
- the mutually inverse $(p,L,M)$ formulas; and
- exact raw-capacity normalization.

Those rows and combinatorial instances are **EXACT FINITE ONLY**.  They
are not a prime scan, a collision census, or evidence for an asymptotic
distribution.

The orthogonality identities (3.3), (3.6), (4.3)-(4.5), the Jacobi
identities (6.4), (6.6), (6.8), the moving-target formula (7.2), and
the selector-saturation theorem are **PROVED** for their stated exact
families.

The following remain **OPEN**:

1. a power-saving bound for actual residual energy $E_p$;
2. selector-aware cross-prime cancellation on fixed-$M$ rows;
3. whether an almost-all-$M$ theorem suffices for the final
   irrationality construction; and
4. the weighted Item 349 degenerate-carrier problem.

Accordingly every ledger change remains zero.
