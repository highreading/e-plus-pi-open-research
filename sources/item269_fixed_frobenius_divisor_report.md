> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 269 — fixed-Frobenius-divisor admission for the moving $j=2$ gate

Checked: 2026-08-31 (Beijing time)

## 1. Verdict and capacity-first admission test

Retain the fixed punctured elliptic curve and odd Picard 1-motive from
Item 267:



$$
E:\quad Y^2=X^3-\frac12,\qquad
U=E\setminus\{X^3=1\},\qquad
M_U^-=[L^-\longrightarrow E].                              \tag{1.1}
$$



For a good prime $p=6q+e$, $e\in\{1,5\}$, the sealed crystalline
frame supplies



$$
x_p=(1,H_q,h_q)^{\mathsf T}.                                \tag{1.2}
$$



On an admissible ordinary-$j=2$ row, let $\delta$ and $D_\delta$
be the phase-dependent boundary data recalled in Section 3.  Item 267
gives



$$
A_s=(-1)^m\{\epsilon(H_q-D_\delta h_q)-1\},                  \tag{1.3}
$$



and Item 251 gives the two actual affine gates



$$
G_\nu=f_\nu Z+U_\nu\qquad(\nu=0,1).                          \tag{1.4}
$$



For this item, a **qualifying fixed-Frobenius-divisor formulation**
means more than a fixed ambient cohomology group.  It requires:

1. a bounded-rank realization over a fixed finite-type base indexing
   the actual $(p,r)$ rows;
2. conductor bounded independently of $r$;
3. nontrivial geometric monodromy in the row direction;
4. one fixed proper conjugacy-stable algebraic subvariety of the
   monodromy realization whose Frobenius membership contains, or
   exactly detects, the full two-coordinate collision; and
5. a uniform local-density estimate strong enough to sum over the
   positive-mass moving-$r$ cell.

This is the minimum package needed before a Chebotarev or large-sieve
zero-density argument can affect capacity.

> **PROVED — exact fixed universal incidence, but with moving external
> row state.**  There is a fixed bilinear incidence variety
> 

$$
> \mathcal I=
> \{(R,x)\in\operatorname{Mat}_{2\times3}\times\mathbb A^3:
> Rx=0,\ x_0=1\}                                             \tag{1.5}
>
$$


> such that the full collision is exactly
> 

$$
> (R_{r,s},x_p)\in\mathcal I.                                \tag{1.6}
>
$$


> This retains both $G_0$ and $G_1$, including the separate
> $f_0=f_1=0$ branch.  The matrix $R_{r,s}$, however, is external
> row data; it is not Frobenius data of the fixed motive (1.1).

> **PROVED — exact reduced $3$-adic slope theorem.**  Put
> 

$$
> L_\delta^{(5)}=3\delta,\qquad
> L_\delta^{(1)}=3\delta-2.
>
$$


> If $D_\delta=A_\delta/B_\delta$ in lowest terms with $B_\delta>0$,
> then
> 

$$
> \boxed{
> \begin{aligned}
> v_3(A_\delta)&=0,\\
> v_3(B_\delta)&=
> L_\delta^{(e)}
> +v_3\!\left((2L_\delta^{(e)}-1)!!\right).
> \end{aligned}}                                             \tag{1.7}
>
$$


> Hence the actual odd-$\delta$ slopes are pairwise distinct in each
> phase, with strictly decreasing $v_3(D_\delta)$.

> **PROVED, SHARPLY SCOPED ALGEBRAIC-CORRESPONDENCE NO-GO.**  In either
> phase there is no nonzero
> 

$$
> P(T,V)\in\mathbb Q[T,V]
>
$$


> for which
> 

$$
> P(\delta,D_\delta)=0                                       \tag{1.8}
>
$$


> for all sufficiently large actual odd $\delta$; in fact it cannot
> hold on any unbounded infinite set of actual $\delta$'s.  Thus the
> moving slope is not a branch of a fixed finite-degree algebraic
> correspondence over the naive $\delta$-line.

> **PROVED, SHARPLY SCOPED CONJUGACY NO-GO.**  In the sealed Item-267
> Cartier realization, the coefficient $H_q-D_\delta h_q$ is not an
> isomorphism or conjugacy invariant.  On $p\equiv5\pmod6$, all
> matrices with $h_q\ne0$ and fixed $\epsilon$ have the same normal
> form.  On $p\equiv1\pmod6$, the corresponding extension coefficient
> is removable on the nonresonant locus $h_q\ne\epsilon$.  Therefore
> no conjugacy-stable divisor in this fixed realization detects even the
> framed period hyperplane, much less the full moving two-gate
> collision.  Any conjugacy-stable container that contains one such
> collision matrix contains the entire relevant normal-form orbit, so it
> supplies no row-selective local-density saving.

The fixed 1-motive can be pulled back to an $r$-line, but that pullback
is constant and has trivial geometric monodromy in $r$.  The universal
incidence (1.5) is a useful exact bookkeeping object, not a qualifying
large-sieve object.  A new auxiliary lisse/crystalline family or a
dynamical realization could in principle encode $R_{r,s}$; this item
does **not** prove that every such future construction is impossible.

The admission test therefore fails:



$$
\boxed{
\text{new unconditional Route-1 rate}=0,\qquad
\text{new ordinary-\(j=2\) capacity reduction}=0.}           \tag{1.9}
$$



The raw cell remains



$$
\frac{2}{35}M+o(M)                                          \tag{1.10}
$$



in log-prime mass.  Every bounded replay below is
**EXACT FINITE ONLY** and contains no exceptional-prime search.

## 2. The full two-coordinate gate is one fixed incidence with a moving matrix

Write



$$
\sigma=(-1)^m,\qquad
\alpha_r=\frac{9\kappa_r}{2}.
$$



Equation (1.3) is



$$
A_s=a_r x_p,\qquad
a_r=\sigma(-1,\epsilon,-\epsilon D_\delta).                  \tag{2.1}
$$



Since



$$
Z=B_s(\alpha_rA_s-\tau_{r,s}),
$$



one has



$$
Z=z_{r,s}x_p,                                                \tag{2.2}
$$



where



$$
z_{r,s}=B_s
\left(
-\alpha_r\sigma-\tau_{r,s},
\alpha_r\sigma\epsilon,
-\alpha_r\sigma\epsilon D_\delta
\right).                                                     \tag{2.3}
$$



Consequently define the two rows



$$
R_{\nu,r,s}
=f_\nu z_{r,s}+(U_\nu,0,0),\qquad \nu=0,1.                   \tag{2.4}
$$



Then, without division and without discarding a rank branch,



$$
\boxed{
G_\nu=R_{\nu,r,s}x_p,\qquad
G_0=G_1=0
\Longleftrightarrow
(R_{r,s},x_p)\in\mathcal I.}                                 \tag{2.5}
$$



If $f_0=f_1=0$, the two rows in (2.4) reduce to
$(U_0,0,0)$ and $(U_1,0,0)$, so (2.5) gives exactly the separate
$U_0=U_1=0$ branch.  This is why replacing the full gate by only the
period line loses information.

The contemporaneous Item-268 adjacent-fiber calculation is used here
only as contextual support: its transported common zero supplies one
linear equation at the next fiber, not another common zero, and its
exact nonpropagation witness shows that a transported line cannot replace
both rows of (2.4).  It is not a frozen dependency of this package unless
a final Item-268 hash is added to the manifest.

The incidence variety $\mathcal I$ is fixed and of bounded degree, but
the points $R_{r,s}$ do not come from (1.1).  Treating
$R_{r,s}$ as an extra coordinate merely restates the collision.  No
uniform conductor, geometric monodromy, or Frobenius equidistribution
theorem for this row-matrix sequence is currently available.

## 3. Exact arithmetic of the full slopes

For $p\equiv5\pmod6$, actual rows have odd $\delta\ge1$ and



$$
\begin{aligned}
c_0&=1,&
\frac{c_{j+1}}{c_j}&=\frac{6j+5}{3j+4},&
K_\delta&=\sum_{j=0}^{\delta-1}c_j,\\
\Pi_\delta&=\sum_{k=1}^{3\delta}
2^{-k}\frac{(-\delta-1/3)_k}{(1/2)_k},&
D_\delta&=K_\delta+c_\delta\Pi_\delta.
\end{aligned}                                                \tag{3.1}
$$



For $p\equiv1\pmod6$, actual rows have odd $\delta\ge3$ and



$$
\begin{aligned}
c_0&=1,&
\frac{c_{j+1}}{c_j}&=\frac{6j+1}{3j+2},&
K_\delta&=\sum_{j=0}^{\delta-1}c_j,\\
\Pi_\delta&=\sum_{k=1}^{3\delta-2}
2^{-k}\frac{(1/3-\delta)_k}{(1/2)_k},&
D_\delta&=K_\delta+c_\delta\Pi_\delta.
\end{aligned}                                                \tag{3.2}
$$



Unify the upper limit by writing $L=L_\delta^{(e)}$.  The $k$-th
term of $\Pi_\delta$ is



$$
t_k=
\frac{\prod_{i=0}^{k-1}(3i-3\delta+\mu_e)}
{3^k(2k-1)!!},
\qquad
\mu_5=-1,\quad\mu_1=1.                                      \tag{3.3}
$$



Every numerator factor in (3.3) is a $3$-adic unit.  Therefore



$$
v_3(t_k)=-k-v_3((2k-1)!!).                                  \tag{3.4}
$$



This valuation is strictly decreasing with $k$, so the final term is
the unique term of lowest valuation.  There can be no cancellation at
that level:



$$
v_3(\Pi_\delta)
=-L-v_3((2L-1)!!).                                          \tag{3.5}
$$



All factors defining $c_\delta$ are $3$-adic units, and every term
of $K_\delta$ is $3$-integral.  Hence



$$
v_3(c_\delta)=0,\qquad v_3(K_\delta)\ge0.                    \tag{3.6}
$$



The negative valuation in (3.5) dominates in
$D_\delta=K_\delta+c_\delta\Pi_\delta$.  Thus



$$
v_3(D_\delta)=-L-v_3((2L-1)!!),                              \tag{3.7}
$$



which proves (1.7), including the statement after reduction to lowest
terms.  Increasing actual $\delta$ by two increases $L$ by six, so
the right side of (3.7) decreases strictly.  This proves pairwise
distinctness without a finite scan.

For orientation, the first exact reduced values are



$$
\begin{array}{c|c|c|c}
e&\delta&D_\delta&v_3(D_\delta)\\ \hline
5&1&-37/81&-4\\
5&3&-65034611/145083393&-13\\
1&3&1995557/3247695&-10\\
1&5&5118998158267/8331477615945&-18.
\end{array}                                                  \tag{3.8}
$$



The table is **EXACT FINITE ONLY**; the theorem is (3.3)–(3.7).

## 4. No fixed algebraic correspondence over the cutoff line

Fix one phase and suppose, for contradiction, that a nonzero



$$
P(T,V)=\sum_{i=0}^d a_i(T)V^i\in\mathbb Q[T,V]               \tag{4.1}
$$



vanishes at $(\delta,D_\delta)$ for an unbounded set of actual odd
$\delta$'s.  Clear a fixed rational denominator so that all
$a_i$ lie in $\mathbb Z[T]$.  Remove the largest common power of
$V$; this is legal because $D_\delta\ne0$.  Then both the leading
coefficient $a_d(T)$ and the constant coefficient $a_0(T)$ are
nonzero polynomials.

The exceptional integers at which either coefficient vanishes are
finite.  For every remaining $\delta$, write



$$
D_\delta=A_\delta/B_\delta,\qquad
\gcd(A_\delta,B_\delta)=1,\quad B_\delta>0.
$$



Multiplying (4.1) by $B_\delta^d$ and reducing modulo
$B_\delta$ gives



$$
B_\delta\mid a_d(\delta).                                   \tag{4.2}
$$



Because $a_d$ is fixed,



$$
\log B_\delta\le\log|a_d(\delta)|=O(\log\delta).              \tag{4.3}
$$



But (1.7) gives



$$
\log B_\delta\ge v_3(B_\delta)\log3
\ge(3\delta-2)\log3.                                        \tag{4.4}
$$



Equations (4.3) and (4.4) contradict each other on every unbounded
set.  This proves (1.8), while explicitly handling the finitely many
leading-coefficient exceptions.

Equivalently, the graph



$$
\{(\delta,D_\delta):\delta\text{ actual}\}\subset\mathbb A^2
$$



is Zariski dense.  In particular, $D_\delta$ is not the value of a
fixed rational function of $\delta$, nor a rational branch of a fixed
finite-degree algebraic cover of the naive cutoff line.

This is a theorem about algebraic sections and finite-degree algebraic
correspondences.  A trace function of a new lisse sheaf, or a coordinate
of a new rational dynamical orbit, need not be algebraic in $\delta$.
Those possibilities are not ruled out; they would require new
uniform-conductor and monodromy theorems.

## 5. Why conjugacy-stable Frobenius divisors lose the gate

Use the fixed frame



$$
(\omega_0,\omega_1,\omega_2,\eta,\xi).
$$



For $p\equiv5\pmod6$, the Cartier matrix has columns



$$
\begin{aligned}
\mathcal C\omega_0&=\epsilon\omega_1,&
\mathcal C\omega_1&=\epsilon\omega_0+H_q\eta,\\
\mathcal C\omega_2&=\epsilon\omega_2,&
\mathcal C\eta&=0,&
\mathcal C\xi&=-h_q\eta.
\end{aligned}                                                \tag{5.1}
$$



The exact frame change



$$
\widetilde\omega_0=\omega_0+\frac{H_q}{\epsilon}\eta,
\qquad
\widetilde\xi=-h_q^{-1}\xi                                  \tag{5.2}
$$



puts (5.1) into a normal form independent of $H_q$ and $h_q$.
For any fixed $D$ and $h\ne0$, the two choices



$$
H=Dh+\epsilon,\qquad H=Dh+\epsilon+1                         \tag{5.3}
$$



give conjugate Cartier modules, while exactly one lies on the period
hyperplane



$$
H-Dh-\epsilon=0.                                            \tag{5.4}
$$



Thus no proper conjugacy-stable subvariety of this abstract Cartier
module detects (5.4).

More generally, a conjugacy-stable set may contain the whole normal-form
orbit and hence give a one-way collision implication.  Such a container
also contains every noncollision matrix in (5.3).  It therefore has no
strict local-density advantage for the gate and fails the admission test.

For $p\equiv1\pmod6$, put $\lambda=H_q-h_q$.  On
$h_q\ne\epsilon$,



$$
\widetilde\omega_0
=\omega_0-\frac{\lambda}{h_q-\epsilon}\eta                   \tag{5.5}
$$



removes $\lambda$.  Holding $h_q$ fixed and varying $H_q$ again
changes (5.4) without changing the conjugacy class.  On the resonant
locus only a zero/nonzero Jordan-extension status remains; the actual
gate still uses $H_q-D_\delta h_q-\epsilon$, so resonance does not
produce the desired fixed divisor.

Frobenius in an unframed lisse realization is naturally a conjugacy
class.  Equations (5.2)–(5.5) therefore rule out a conjugacy-stable
collision divisor in the sealed realization itself.  Keeping the
canonical de Rham frame preserves the actual endpoint value, but then
the test vector and its hyperplane move with $D_\delta$.

There is a complementary framed obstruction.  The lines



$$
\ell_\delta^{(5)}
=\mathbb Q(\omega_1+D_\delta\xi),\qquad
\ell_\delta^{(1)}
=\mathbb Q(\omega_0+(1-D_\delta)\eta)                        \tag{5.6}
$$



are pairwise distinct by (1.7).  A polynomial vanishing identically on
all corresponding affine period hyperplanes would have infinitely many
distinct linear factors and hence would be zero.  Also, a projective
linear transformation fixing three distinct lines in either displayed
two-plane is the identity.  Thus marking all row lines as fixed tensors
would kill projective monodromy on that period plane rather than supply
the required nontrivial row monodromy.

These are scoped obstructions to constructions using the sealed motive,
its conjugacy class, and finitely many fixed frame tensors.  They are not
an impossibility theorem for an entirely new auxiliary compatible
system.

## 6. The row parameter cannot be forgotten

The same good prime supports several admissible rows but only one fixed
Cartier/Frobenius object.  The already known exact $p=47$ cutoff
example is



$$
\begin{array}{c|c|c|c|c}
\delta&r&s&m&H_m\pmod{47}\\ \hline
1&1&7&6&33\\
3&7&5&4&0\\
5&13&3&2&41\\
7&19&1&0&1.
\end{array}                                                  \tag{6.1}
$$



This is not a new exceptional-prime search and is not a full-gate
density claim.  It proves only the exact factor-through-prime
obstruction: a condition depending on the fixed motive at $p$ alone
cannot distinguish the row-labelled cutoff events.

Pulling $M_U^-$ back to a row parameter base repeats the same
Frobenius class at all these rows.  That pullback is geometrically
constant.  To make (1.6) a Frobenius condition, a new realization must
encode $R_{r,s}$, preserve both rows, and prove nontrivial geometric
monodromy plus uniform conductor.  No such realization is currently in
the archive.

## 7. Capacity verdict

For each fixed $r$, one may retain the row vector and regard the
collision as a fixed framed incidence.  Its total log-prime weight along
one ray is only $O(\log M)=o(M)$, exactly as in the previously known
fixed-ray geometry.

The ordinary-$j=2$ cell contains linearly many moving $r$'s.  Item
269 proves neither:

* a fixed conjugacy-stable divisor with uniform local density;
* a bounded-conductor sheaf realizing the moving row matrices;
* a recurrence-orbit equidistribution theorem for $D_\delta$ or
  $R_{r,s}$; nor
* a strict retained ceiling below the raw $2/35$ mass.

The exact valuation theorem shows why a naive finite-degree algebraic
parameterization cannot repair the issue, but it is not itself a zero
container.  Therefore no positive linear mass can be removed and the
booking is zero.

## 8. Strict proof labels

### PROVED

* The full collision is exactly the two-row incidence (2.5), including
  the rank-zero branch.
* The reduced valuation formula (1.7), strict slope distinctness, and
  the algebraic-correspondence theorem (1.8).
* The conjugacy-stable no-go for the sealed Cartier realization.
* The constant-pullback/trivial-row-monodromy obstruction.
* Failure of the current positive-linear-capacity admission test.

### PROVED, SCOPED NO-GO

* No nonzero fixed $P(\delta,D_\delta)$ describes the slopes.
* No conjugacy-stable divisor in the Item-267 abstract Cartier module
  detects the actual framed coefficient.
* Finitely many fixed tensors from that realization cannot absorb the
  pairwise distinct moving lines while retaining nontrivial projective
  monodromy on their two-plane.

These statements do not rule out a new auxiliary sheaf or dynamical
realization.

### EXACT FINITE ONLY

The standard-library checker verifies:

* 1,503 individual tail-term valuations through actual odd
  $\delta\le31$;
* 29 strict adjacent slope-valuation comparisons;
* 397 exact Cartier normal-form changes through $p\le97$;
* 23 same-conjugacy-class gate separations;
* 12 exact full two-row incidence identities; and
* the inherited four-row $p=47$ factor-through-prime witness.

It performs no exceptional collision-prime search.

### OPEN

* A fixed bounded-conductor sheaf or crystalline family whose Frobenius
  data encodes $R_{r,s}$.
* Nontrivial geometric monodromy and a fixed proper collision divisor
  for the actual $(p,r)$ family.
* Any uniform local-density or weighted large-sieve theorem for the
  moving full gate.
* Any elliptic-Wieferich equivalence; Item 267's warning remains in
  force.
* Route 1 and every conclusion about $e+\pi$.

### BOOKING

No new Route-1 rate and no new ordinary-$j=2$ capacity reduction are
booked.

## 9. Portable package

~~~text
sources/item269_fixed_frobenius_divisor_report.md
scripts/item269_fixed_frobenius_divisor_certificate.py
results/item269_fixed_frobenius_divisor_certificate.json
results/item269_fixed_frobenius_divisor_certificate_replay.json
results/item269_fixed_frobenius_divisor_ledger.json
manifests/item269_fixed_frobenius_divisor_manifest.json
results/item269_fixed_frobenius_divisor_hashes.sha256
~~~

The frozen dependencies are Items 251, 262, 263, and 267.
