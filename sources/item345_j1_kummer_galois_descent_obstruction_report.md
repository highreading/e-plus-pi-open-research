> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 345 — split-prime descent dichotomy for the fixed-$j=1$ Kummer lift

Date: 2026-09-01

## 1. Outcome and capacity first

Item 342 attached to every actual selected fixed-$j=1$ row an algebraic
integer



$$
\mathcal T=\mathcal T_{p,r,n}\in
 K_p:=\mathbb Q(\zeta_{p-1})                               \tag{1.1}
$$



and a chosen Teichmüller prime $\mathfrak P\mid p$ such that



$$
\mathcal T\equiv a_{r,n}\pmod{\mathfrak P},\qquad
 |\sigma(\mathcal T)|\leq B_p:=21\sqrt p                  \tag{1.2}
$$



for every complex embedding $\sigma$.  The original collision implies
$a_{r,n}=0\pmod p$, hence $\mathcal T\in\mathfrak P$.

This item determines whether ordinary Galois descent can convert that
chosen-prime condition into a useful rational or bounded-degree obstruction.
The answer is a precise dichotomy.

1. **Additive descent is not gate-forced.** Since

   

$$
p\equiv1\pmod{p-1},
$$



   $p$ splits completely in $K_p$, and the decomposition group of
   $\mathfrak P$ is trivial.  Membership in one split prime does not force
   any nontrivial trace, character projection, or Galois average to vanish
   modulo the prime below it.

2. **Multiplicative descent preserves the gate but not the useful height.**
   For every subgroup $H\subseteq\operatorname{Gal}(K_p/\mathbb Q)$,

   

$$
\mathcal T\in\mathfrak P
   \Longrightarrow
   N_{K_p/K_p^H}(\mathcal T)
   \in\mathfrak P\cap K_p^H.                              \tag{1.3}
$$



   If $d=[K_p:\mathbb Q]=\varphi(p-1)$ and $h=|H|$, then each conjugate
   of the relative norm is bounded by $B_p^h$, while
   $[K_p^H:\mathbb Q]=d/h$.  Its absolute norm bound is therefore

   

$$
(B_p^h)^{d/h}=B_p^d
   =(21\sqrt p)^{\varphi(p-1)},                            \tag{1.4}
$$



   exactly the original Item 342 bound.  Passing through a bounded-index,
   bounded-degree, or any intermediate subfield gives no black-box norm
   improvement.

Thus no subexponential fixed-$M$ carrier, no strict fixed-$j=1$ constant,
and no proof of $W_b(M)=o(M)$ follows from formal Galois descent.

The only way a descent could still succeed is through new arithmetic:

- a large stabilizer of $\mathcal T$ specifically on almost all
  selected-zero rows;
- exceptional cancellation making an actual relative norm far smaller
  than its conjugate bound;
- or a chosen-prime $p$-adic theorem which does not descend by ordinary
  Galois averaging.

No such theorem is proved here.  Consequently



$$
\boxed{
 \text{new linear log rate}=0,\qquad
 \text{new fixed-}j=1\text{ capacity reduction}=0,\qquad
 \text{retained ceiling}={1\over36}.}                     \tag{1.5}
$$



The result reaches every Item 342 row.  Its zero ledger gain is caused by
the split-prime geometry and norm height, not by thin support.

## 2. The chosen coordinate in the completely split fiber

Let



$$
m=p-1,\qquad K=\mathbb Q(\zeta_m),\qquad
 \mathcal G=\operatorname{Gal}(K/\mathbb Q)
 \cong(\mathbb Z/m\mathbb Z)^\times.                      \tag{2.1}
$$



Choose a primitive root $g\in\mathbb F_p^\times$.  The Teichmüller
prime used by Item 342 is the prime $\mathfrak P_g$ for which



$$
\zeta_m\longmapsto g\pmod{\mathfrak P_g}.                \tag{2.2}
$$



Because $p\nmid m$ and the order of $p$ modulo $m$ is one, $p$
splits completely.  In particular,



$$
D(\mathfrak P_g/p)=\{1\}.                                \tag{2.3}
$$



Equivalently,



$$
\mathcal O_K/p\mathcal O_K
 \cong\prod_{j\in\mathcal G}\mathbb F_p,                  \tag{2.4}
$$



where the $j$-th coordinate evaluates $\zeta_m$ at $g^j$.

Item 342's lift can be written



$$
\mathcal T=P_{p,r,n}(\zeta_m)                            \tag{2.5}
$$



for an explicit integral group-ring polynomial.  Its chosen-prime
reduction is



$$
P_{p,r,n}(g)=a_{r,n}\pmod p.                             \tag{2.6}
$$



The conjugate $\sigma_j(\mathcal T)$ has reduction



$$
P_{p,r,n}(g^j)                                           \tag{2.7}
$$



at the same chosen prime.  Hence the selected gate (2.6) kills one
coordinate in the product (2.4); it imposes no formal condition on the
other coordinates.

This simple observation governs every descent considered below.

## 3. Why traces and character projections are not forced

Let $H\neq\{1\}$ be a subgroup of $\mathcal G$, and put $L=K^H$.
The relative trace is



$$
\operatorname{Tr}_{K/L}(\mathcal T)
 =\sum_{\sigma\in H}\sigma(\mathcal T).                   \tag{3.1}
$$



Reducing at $\mathfrak q=\mathfrak P_g\cap L$, the summands in (3.1)
sample distinct split-prime coordinates.  Knowing that the identity
coordinate is zero does not force their sum to vanish.

This is not merely a warning about the particular formula.  Complete
splitting gives the ideal-theoretic statement



$$
\boxed{
 \operatorname{Tr}_{K/L}(\mathfrak P_g)
 \nsubseteq\mathfrak q\qquad(H\neq\{1\}).}                \tag{3.2}
$$



Indeed, modulo $p$, membership in $\mathfrak P_g$ means that one
coordinate in (2.4) is zero.  The remaining coordinates are arbitrary.
Choosing one other coordinate equal to one makes the orbit sum nonzero.

The same argument applies to every nontrivial additive group-algebra
projection



$$
\sum_{\sigma\in H}\lambda_\sigma\,\sigma(\mathcal T)     \tag{3.3}
$$



whose support contains a conjugate besides the identity.  In particular,
bounded-order character projections and Galois idempotents are not
target-forced by $\mathcal T\in\mathfrak P_g$.

A chosen-coordinate projector does exist modulo the split algebra
(2.4), but it is not Galois descent: it singles out $\mathfrak P_g$
and is precisely the $p$-adic information one was trying to control.

## 4. Norms preserve the gate

The relative norm is different:



$$
\mathcal N_H:=
 N_{K/L}(\mathcal T)
 =\prod_{\sigma\in H}\sigma(\mathcal T).                  \tag{4.1}
$$



The product contains the identity factor.  Therefore



$$
\mathcal T\in\mathfrak P_g
 \Longrightarrow
 \mathcal N_H\in\mathfrak P_g\cap L,                      \tag{4.2}
$$



which proves (1.3).  This implication is exact and holds for every row.

It is only one-way.  A different conjugate coordinate may vanish even when
$P_{p,r,n}(g)\neq0$.  In that case $p$ divides the absolute norm although
the selected carrier is a $p$-unit.  Two preselected controls in Section 8
exhibit this phenomenon exactly.

Thus norms introduce false positives.  False positives are acceptable for
an upper-bound carrier only if its height is small enough.  The next section
shows that the available height is unchanged.

## 5. Subfields do not improve the norm-height ledger

Let



$$
d=[K:\mathbb Q]=\varphi(p-1),\qquad h=|H|,\qquad
 [L:\mathbb Q]={d\over h}.                                \tag{5.1}
$$



Item 342 proves



$$
|\tau(\mathcal T)|\leq B_p=21\sqrt p                    \tag{5.2}
$$



for every embedding $\tau$.  Consequently every embedding of the
relative norm satisfies



$$
|\rho(\mathcal N_H)|\leq B_p^h.                          \tag{5.3}
$$



Taking the norm from $L$ to $\mathbb Q$ gives



$$
\left|N_{L/\mathbb Q}(\mathcal N_H)\right|
 \leq(B_p^h)^{d/h}=B_p^d.                                \tag{5.4}
$$



But transitivity of the norm gives the exact identity



$$
N_{L/\mathbb Q}(\mathcal N_H)
 =N_{K/\mathbb Q}(\mathcal T).                            \tag{5.5}
$$



Therefore every route through an intermediate field ends with exactly the
same absolute integer and the same black-box bound.

This handles both extremes.

- If $h$ is bounded, the relative norm has controlled per-embedding
  growth, but it remains in a field of degree $d/h\to\infty$, and one
  split-prime condition gives no Archimedean contradiction.
- If $[L:\mathbb Q]$ is bounded, then $h\geq d/[L:\mathbb Q]$ grows,
  and the per-embedding bound $B_p^h$ absorbs the entire apparent descent.

At fixed $M$, multiplying the generic absolute-norm carriers over the
candidate primes yields at best a quadratic-scale logarithmic height from
these bounds, far above the $o(M)$ target.  This is a capacity audit of
the method, not a lower bound for a specially cancelled norm.

## 6. Stabilizer criterion for a genuine descent

Let



$$
\operatorname{Stab}(\mathcal T)
 =\{\sigma\in\mathcal G:\sigma(\mathcal T)=\mathcal T\}.  \tag{6.1}
$$



The actual field generated by the lift has degree



$$
[\mathbb Q(\mathcal T):\mathbb Q]
 ={|\mathcal G|\over|\operatorname{Stab}(\mathcal T)|}.  \tag{6.2}
$$



Hence descent to degree at most $D$ requires



$$
|\operatorname{Stab}(\mathcal T)|
 \geq{\varphi(p-1)\over D}.                               \tag{6.3}
$$



The chosen-prime condition $P(g)=0$ says nothing about the algebraic
equalities



$$
P(\zeta_m^j)=P(\zeta_m)                                  \tag{6.4}
$$



needed for (6.3).  A large stabilizer could still arise from special
arithmetic of the selected-zero rows, but proving it would be a new global
theorem, not formal descent from the gate.

The deterministic controls show that automatic stabilization is already
false at the exact finite level.  Both preselected carrier-zero rows
$(h,s,p)=(1,1,13)$ and $(8,2,47)$ have trivial stabilizer and full
cyclotomic orbit.  These are not asserted to be full original collisions,
and no density inference is made.

## 7. Capacity conclusion and scoped no-go

The split-prime theorem applies to all actual Item 342 rows, whose raw
fixed-$j=1$ mass is



$$
{M\over6}+o(M).                                          \tag{7.1}
$$



The following method classes are closed.

1. Nontrivial Galois traces, bounded-character projections, or additive
   idempotents justified only by the chosen-prime gate.
2. Relative norms through bounded-index or bounded-degree subfields,
   combined only with Item 342's conjugate bound.
3. Automatic rational descent inferred from the Teichmüller construction
   or from selected-carrier vanishing alone.

The following remain open.

1. A theorem forcing a stabilizer of size comparable to $\varphi(p-1)$
   on all but zero-rate selected-zero rows.
2. Special relative-norm cancellation which beats (5.4).
3. Chosen-prime $p$-adic nonconcentration without ordinary descent.
4. An additional condition from the full original collision that forces
   descent beyond the selected factor alone.

No selected-zero row is excluded, so



$$
\text{proved excluded weighted mass}=0,\qquad
 \text{retained ceiling}={1\over36}.                      \tag{7.2}
$$



## 8. Exact group-ring controls

For each of the five Item 342 rows, the certificate constructs the integral
group-ring polynomial $P(X)$, reduces it modulo $\Phi_{p-1}(X)$, tests
every Galois multiplier, and evaluates the resultant



$$
\left|\operatorname{Res}(\Phi_{p-1},P)\right|
 =\left|N_{K/\mathbb Q}(\mathcal T)\right|.               \tag{8.1}
$$



No prime scan is performed.

| $(h,s,p)$ | selected target | orbit degree | absolute norm | $p\mid$ norm |
|---|---:|---:|---:|---|
| $(1,1,13)$ | $0$ | $4$ | $6877$ | yes |
| $(2,1,17)$ | $8$ | $8$ | $19103121$ | yes |
| $(8,2,47)$ | $0$ | $22$ | $2075473882824195408557$ | yes |
| $(4,4,43)$ | $2$ | $12$ | $2592733605337$ | no |
| $(2,6,47)$ | $36$ | $22$ | $1905718768398368001644003$ | yes |

Every stabilizer in the table is exactly $\{1\}$.  The $p=17$ and
second $p=47$ rows are exact norm false positives: their selected targets
are nonzero, but a different split coordinate makes the absolute norm
divisible by $p$.

The two selected-zero rows verify the one-way gate to the norm and show
that selected-carrier vanishing does not by itself force nontrivial
stabilization.  They are exact controls only, not full-collision or
asymptotic claims.

## 9. Strict labels

### PROVED

- complete splitting of $p$ in $K_p$ and the trivial decomposition
  group of the chosen Teichmüller prime;
- failure of every nontrivial additive Galois projection to be forced by
  chosen-prime membership;
- preservation of the gate by every relative norm;
- invariance of the black-box absolute norm bound under all intermediate
  subfields;
- the stabilizer/orbit criterion (6.2)--(6.3);
- the scoped Galois-projection and subfield-norm no-go.

### EXACT FINITE ONLY

- the five preselected group-ring stabilizer and resultant controls;
- two carrier-zero controls have trivial stabilizer;
- two nonzero controls are norm false positives;
- no finite control is promoted to a density statement or full collision.

### OPEN

- a large-stabilizer theorem on a weighted-full set of selected-zero rows;
- special relative-norm cancellation below the Item 342 bound;
- chosen-prime $p$-adic nonconcentration;
- descent forced by an additional full-collision condition;
- $W_b(M)=o(M)$ or any strict fixed-$j=1$ ceiling reduction;
- fixed-$j=1$ closure, Route 1, and every conclusion about $e+\pi$.

## 10. Ledger consequence



$$
\begin{array}{c|c}
\text{quantity}&\text{Item 345 value}\\ \hline
\text{actual rows reached by split-prime analysis}&\text{all}\\
\text{new independent condition}&0\\
\text{new proved excluded log mass}&0\\
\text{new fixed-}j=1\text{ capacity reduction}&0\\
\text{retained fixed-}j=1\text{ ceiling per }6M&1/36
\end{array}                                                \tag{10.1}
$$



Item 345 proves that ordinary Galois descent has only two formal options:
additive projections lose the gate, while norms keep the gate and retain
the full norm-height barrier.  It is a global descent obstruction, not a
ledger gain.
