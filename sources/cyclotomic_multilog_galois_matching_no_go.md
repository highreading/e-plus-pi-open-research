> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Full-orbit cyclotomic multi-log matching and the monodromy obstruction

Date: 2026-08-27.

## 1. Scope and theorem

Fix an odd prime $p\ge5$, put



$$
G=(\mathbb Z/p\mathbb Z)^\times,qquad \zeta=e^{2\pi i/p},
$$



and use the complementary algebraic units



$$
x_a={1\over1+\zeta^a},\qquad y_a=1-x_a=x_{-a}
\quad(a\in G).                                             \tag{1}
$$



This note asks whether several logarithmic branches, algebraic weights, or
Dirichlet-character projectors can repair the Galois mismatch of the
fixed-$p$, $c=f=0$ paired Rivoal form.  The coefficient system may use
any fixed finite number of copies of the full primitive orbit, arbitrary
fixed algebraic weights, and arbitrary fixed logarithm sheets.

The answer is no.

> **Full-orbit multi-log obstruction.**  Suppose a scalar algebraic form
> has coefficient $u$ on $s=e+\pi$, and at every cyclotomic embedding
> its analytic logarithmic coefficient matches the corresponding conjugate
> of $u$.  Then:
>
> 1. with centered logarithm lifts, necessarily $u=0$;
> 2. if $u\ne0$ and the total centered coefficient vector is not even,
>    at least one conjugate remainder grows like $\rho_*^d/d$, where
>    $\rho_*>1$;
> 3. if the centered coefficient vector is even, all centered remainders
>    cancel, but a nonzero target can then come only from monodromy, and
>    every conjugate remainder tends to
>    $(\pi/e)\sigma(u)\ne0$.

Thus no such nonzero scalar form tends to zero at every Galois branch.
The proof covers fixed systems, and also fixed-field coefficient sequences
of subexponential projective height.  It does not cover exponentially
fine-tuned coefficients, different Padé degree allocations in different
orbit components, or mixtures of unrelated conductors.  Nothing here
classifies $e+\pi$.

## 2. Centered branches and the unique maximal pair

Let $\widetilde a$ be the representative of $a$ in
$(-p/2,p/2)$.  Then $\widetilde{-a}=-\widetilde a$, and the centered
logarithm difference is



$$
L_a^0=\operatorname {Log}(y_a)-\operatorname {Log}(x_a)
={2\pi i\over p}\widetilde a.                             \tag{2}
$$



On the corrected-Rivoal edge write



$$
P_{d,a}=A_d(x_a)A_d(y_a),                                 \tag{3}
$$



and



$$
D^0_{d,a}=A_d(y_a)R_{\log,d}(x_a)
           -A_d(x_a)R_{\log,d}(y_a).                     \tag{4}
$$



The exact symmetries are



$$
P_{d,-a}=P_{d,a},\qquad D^0_{d,-a}=-D^0_{d,a},             \tag{5}
$$



and the fixed-orbit endpoint theorem gives



$$
P_{d,a}\longrightarrow e^{-1},                            \tag{6}
$$



uniformly in $a$, together with



$$
D^0_{d,a}={2ie^{-3/2}\over d}\rho_a^d
\left\{
\sin\left({(d+2)\pi\widetilde a\over p}
 +{1\over2}\tan{\pi\widetilde a\over p}\right)
+O_p(d^{-1})\right\},                                    \tag{7}
$$



where



$$
\rho_a={1\over2\cos(\pi\widetilde a/p)}.                 \tag{8}
$$



Modulo the pair $a\leftrightarrow-a$, the unique maximum occurs at



$$
a_*={p-1\over2},\qquad
\rho_*={1\over2\sin(\pi/(2p))}>1.                         \tag{9}
$$



The leading sine at this pair is uniformly bounded away from zero as
$d$ varies.  Its rational multiple of $\pi$ cannot cancel the
nonzero algebraic number
$\tfrac12\tan(\pi\widetilde a_*/p)$.  Hence



$$
|D^0_{d,a_*}|\asymp_p{\rho_*^d\over d},                   \tag{10}
$$



and every other pair has strictly smaller exponential base.

## 3. General finite sheets and exact compatibility

Take copies $j=1,\ldots,J$.  In copy $j$, choose fixed algebraic
weights $C_{j,a}$ and an integer sheet function
$m_j:G\to\mathbb Z$.  The lifted logarithm difference is



$$
L_{j,a}={2\pi i\over p}\{\widetilde a+pm_j(a)\},          \tag{11}
$$



and changing the sheet adds exactly



$$
D^{(j)}_{d,a}=D^0_{d,a}+2\pi i\,m_j(a)P_{d,a}.            \tag{12}
$$



At $\sigma_k:\zeta\mapsto\zeta^k$, exact matching of one scalar
coefficient $u$ requires



$$
\boxed{
\sigma_k(u)={2i\over p}
\sum_{j,a}\sigma_k(C_{j,a})
\{\widetilde{ka}+pm_j(ka)\}
\quad(k\in G).}                                           \tag{13}
$$



The logarithmic-remainder part at the same embedding is



$$
\boxed{
F^{\log}_{k,d}=\sum_{j,a}\sigma_k(C_{j,a})
\{D^0_{d,ka}+2\pi i\,m_j(ka)P_{d,ka}\}.}                \tag{14}
$$



The exponential remainder on a fixed orbit is factorially small.  It
cannot cancel either the exponential term or the nonzero constant isolated
below.

## 4. Centered averaging forces a zero target

Suppose first that every $m_j$ is zero, and put
$C_a=\sum_jC_{j,a}$.  Applying $\sigma_k^{-1}$ to (13) gives



$$
u={2i\over p}\sum_a C_a\widetilde{ka}
\quad(k\in G).                                             \tag{15}
$$



For each fixed $a$, multiplication by $a$ permutes $G$, while
centered residues cancel in opposite pairs.  Therefore



$$
{1\over|G|}\sum_{k\in G}\widetilde{ka}=0.                \tag{16}
$$



Averaging (15) over $k$ proves



$$
\boxed{u=0.}                                               \tag{17}
$$



This is the compatibility condition missed by a purely formal character
projection.  A Dirichlet-character or Gauss-sum vector may transform
formally by a character, but it is not the conjugate vector of one scalar
algebraic form unless (13) holds.  For centered branches, (13) and (16)
force its target coefficient to vanish.

## 5. A noneven vector has a growing conjugate

Let $C_a=\sum_jC_{j,a}$ be the total coefficient of the centered
remainder.  Suppose that



$$
C_b\ne C_{-b}                                             \tag{18}
$$



for some $b$.  Choose $k$ with $kb=a_*$.  The two unique maximal
terms in (14) are



$$
\sigma_k(C_b)D^0_{d,a_*}
+\sigma_k(C_{-b})D^0_{d,-a_*}
=\sigma_k(C_b-C_{-b})D^0_{d,a_*}.                         \tag{19}
$$



Its fixed algebraic coefficient is nonzero.  All other centered terms have
smaller exponential base, and the sheet terms are bounded by (6).  Thus



$$
\boxed{|F^{\log}_{k,d}|\asymp_{p,C,m}\rho_*^d/d.}         \tag{20}
$$



For coefficients in a fixed field with projective height $e^{o(d)}$,
the same argument applies unless the difference in (18) is eventually
zero: the elementary height/product lower bound prevents a nonzero
algebraic difference from being as small as $\rho_*^{-d}$.

## 6. Evenness leaves a nonzero monodromy limit

The only way to remove every unique-maximal pair is



$$
C_a=C_{-a}\quad(a\in G).                                  \tag{21}
$$



By (5), this cancels the entire centered remainder and also the centered
target multiplier at every embedding.  Put



$$
M_k=\sum_{j,a}\sigma_k(C_{j,a})m_j(ka).                   \tag{22}
$$



Equations (13)--(14) become



$$
\sigma_k(u)=2iM_k                                         \tag{23}
$$



and



$$
F^{\log}_{k,d}=2\pi i
\sum_{j,a}\sigma_k(C_{j,a})m_j(ka)P_{d,ka}.               \tag{24}
$$



Using (6) in (24) gives



$$
\boxed{
F^{\log}_{k,d}+F^{\exp}_{k,d}
={\pi\over e}\sigma_k(u)+o_{p,C,m}(1).}                  \tag{25}
$$



If $u\ne0$, none of its conjugates vanishes, so every branch is
eventually bounded away from zero.

Noncentered matching itself is possible.  For example, take one copy,
all weights equal to one, and the least-positive representatives
$r(a)\in\{1,\ldots,p-1\}$.  Since



$$
\sum_{a\in G}r(ka)={p(p-1)\over2},                         \tag{26}
$$



equation (13) holds with $u=i(p-1)$.  But (25) then tends to
$i\pi(p-1)/e$, independently of $k$.  Its nonzero coefficient comes
entirely from trivial-character monodromy, and precisely that monodromy
prevents smallness.

## 7. Character interpretation and boundary

The centered multiplier is an odd mean-zero function on $G$.  Odd
character pieces see the unique pair $\pm a_*$ with addition rather than
cancellation and therefore grow like $\rho_*^d/d$.  Even and trivial
pieces kill the centered target; obtaining a target through sheet shifts
leaves the limit (25).  In short,



$$
\boxed{
\text{odd characters: exponential growth};\qquad
\text{even/trivial characters: zero target or nonzero monodromy limit}.}
$$



The theorem is confined to a fixed prime conductor, a fixed finite number
of full-orbit copies, and the common edge $c=f=0$.  It leaves open
different degree allocations, multiple conductors, and new simultaneous
Padé conditions imposed before evaluation.  It supplies no proof of
algebraicity or transcendence of $e+\pi$.
