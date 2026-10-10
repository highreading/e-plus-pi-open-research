> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 286 — Frobenius-large-sieve applicability for the isolated fixed-$j=1$ gate

Checked: 2026-08-31 (Beijing time)

## 1. Scope, admission audit, and verdict

Retain the actual fixed common-log cell



$$
p=4h+6s+3,\qquad M=3h+4s+2,\qquad h,s\ge1,             \tag{1.1}
$$



and Item 281's normalized integral pair



$$
\overline C(M)=\bigl(\overline C_0(M),\overline C_1(M)\bigr).
                                                                    \tag{1.2}
$$



For every actual candidate prime,



$$
\boxed{\text{full divided gate collides at }p
 \iff p\mid\overline C_0(M),\ \ p\mid\overline C_1(M).} \tag{1.3}
$$



The gcd and the CRT norm are used below only as exact recognition of
(1.3).  No new scalar is designed.

> **PROVED IN THE ARCHIVE — scoped Frobenius-sieve applicability
> obstruction.**  The fixed-$j=1$ data currently sealed in the archive do
> not satisfy the hypotheses needed to apply Kowalski's Frobenius large
> sieve to (1.3).  The available object is a rational translation-difference
> module with fixed singular support.  The archive has not constructed a
> fixed finite-field base, a compatible system of lisse auxiliary-$\ell$
> sheaves, uniform cohomological complexity, geometric/arithmetic monodromy,
> cross-$\ell$ linear disjointness, or conjugacy-stable local sets which
> contain every actual collision.

> **PROVED IN THE ARCHIVE — diagonal-modulus obstruction.**  More
> decisively, (1.3) is a congruence modulo the same prime $p$ which is the
> varying residue characteristic.  It does not formally imply any condition
> modulo an auxiliary prime $\ell\ne p$.  Thus even a realization of
> $\overline C(M)\bmod p$ as a characteristic-$p$ matrix coefficient
> would not, by itself, provide the simultaneous auxiliary-$\ell$ local
> conditions on which the Frobenius large sieve operates.

> **PROVED, CONDITIONAL BRIDGE.**  If a future construction upgrades the
> gate to two conjugacy-invariant integer-valued compatible Frobenius
> coefficients (or supplies an equally rigorous framed replacement) and
> proves that a collision forces both coefficients to vanish as integers,
> then the target lies in their zero locus modulo every auxiliary $\ell$.  Under
> Kowalski's remaining hypotheses and a positive-density complement in each
> monodromy coset, Proposition 3.3 gives a power-saving exceptional-point
> bound.  A horizontal analogue giving
> $N(M)=o(M/\log M)$ collision primes would imply collision log weight
> $o(M)$, remove the full isolated $M/6+o(M)$ raw mass, and hence remove
> the remaining $1/36$ ceiling per $6M$.  Neither the exact-zero bridge
> nor such a horizontal theorem is currently proved.

This result is deliberately scoped.  It does not prove that no enlarged
sheaf, arithmetic $D$-module, compatible system over an arithmetic base,
or horizontal Chebotarev theorem can encode the gate.  It proves that the
present finite module, Pluecker incidence, gcd recognition, and CRT
recognition do not supply the missing hypotheses or the auxiliary-local
bridge.

Item 149 already books the first post-Cartier copy.  Therefore



$$
\boxed{\text{new fixed-\(j=1\) capacity reduction}=0,\qquad
        \text{new unconditional Route-1 rate}=0.}           \tag{1.4}
$$



No finite collision census is used.

## 2. Exact tied family and raw capacity

Eliminating $h$ from (1.1) gives



$$
4M+1=3p-2s,
 \qquad
 p={4M+2s+1\over3}.                                      \tag{2.1}
$$



The endpoint inequalities $h,s\ge1$ put every candidate prime in



$$
{4M+3\over3}\le p\le {3M-1\over2}.                       \tag{2.2}
$$



The interval length is exactly



$$
{3M-1\over2}-{4M+3\over3}={M-9\over6}.                   \tag{2.3}
$$



Consequently the prime number theorem gives total candidate log weight



$$
\sum_{p\text{ in }(2.2)}\log p={M\over6}+o(M).            \tag{2.4}
$$



This is $1/36$ after normalization by $6M$.  Item 279 shows that every
fixed-diameter cluster subfamily has weight $o(M)$; therefore all linear
capacity may be concentrated on isolated primes.  Item 286 addresses that
remaining mass directly, not by another bounded-cluster argument.

Let $N(M)$ be the number of collision primes in (2.2), and let $W(M)$
be their log weight.  Since $p<3M/2$,



$$
W(M)\le N(M)\log(3M/2).                                  \tag{2.5}
$$



Hence



$$
N(M)=o(M/\log M)\quad\Longrightarrow\quad W(M)=o(M).     \tag{2.6}
$$



Equation (2.6) is the exact count-to-capacity threshold for a prospective
horizontal density theorem.

## 3. The primary-source theorem and its actual hypotheses

This section records a **LITERATURE THEOREM**, not a theorem proved by this
archive.

Kowalski's paper
[The large sieve, monodromy and zeta functions of curves](https://arxiv.org/abs/math/0503714)
starts with a smooth affine geometrically connected variety
$U/\mathbf F_q$.  For auxiliary primes 

$$
\ell\ne\operatorname{char}
\mathbf F_q
$$

, it takes lisse fixed-rank sheaves, equivalently
representations



$$
\rho_\ell:\pi_1(U)\longrightarrow G_\ell\subseteq
 \operatorname{GL}_r(\mathbf F_{\lambda}).                 \tag{3.1}
$$



In the compatible-system branch, the characteristic polynomial of
Frobenius at every point over every finite extension has coefficients
independent of $\ell$.  Theorem 3.1 assumes the appropriate uniform
cohomological bounds, bounded twist stabilizers, and pairwise linear
disjointness of the geometric monodromy representations.  The latter means
that for distinct auxiliary primes the product map to the two geometric
monodromy groups is surjective.

For conjugacy-invariant sets $\Omega(\ell)$ in the correct arithmetic
monodromy coset, define



$$
P(L)=\sum_{\substack{\ell\le L\\\ell\in\Lambda}}
 {\lvert\Omega(\ell)\rvert\over\lvert G_\ell^g\rvert}.
                                                                    \tag{3.2}
$$



Proposition 3.3 then gives, for $d=\dim U$,



$$
\lvert S(U,\Omega;L)\rvert
 \le {\kappa q^d+Cq^{d-1/2}L^A\over P(L)},                \tag{3.3}
$$



where the sifted set consists of points whose Frobenius avoids every
$\Omega(\ell)$.  The proof uses uniform Frobenius trace estimates and
cross-$\ell$ independence; a recurrence matrix with fixed poles is not one
of the inputs to (3.3).

The following sources are also primary and clarify the scope.

* Kowalski's
  [The principle of the large sieve](https://arxiv.org/abs/math/0610021)
  treats the general sieve framework and compatible Frobenius families.
* Kowalski's survey notes
  [Some aspects and applications of the Riemann hypothesis over finite fields](https://people.math.ethz.ch/~kowalski/exponential-sums-rism.pdf)
  explicitly distinguish vertical finite-field equidistribution from the
  much subtler horizontal variation of Frobenius as the characteristic
  changes.

These literature results are not being extended here.  Item 286 only audits
their hypotheses against the exact archive objects.

## 4. Hypothesis-by-hypothesis archive audit

The following table separates what is sealed from what is missing.

| Frobenius-sieve datum | Exact archive status for fixed $j=1$ |
|---|---|
| One smooth affine geometrically connected $U/\mathbf F_q$ indexing all tied rows | **MISSING.**  At fixed $M$, the candidate rows live in different characteristics $\mathbf F_p$. |
| Lisse fixed-rank auxiliary-$\ell$ sheaves on $U$ | **MISSING.**  Item 273 gives coefficient-index difference equations, not representations of $\pi_1(U)$. |
| Compatible integral system with $\ell$-independent Frobenius polynomials | **MISSING.**  No such polynomials are attached to the fixed-$j=1$ endpoint state. |
| Controlled cohomological complexity / conductor | **MISSING.**  Fixed rational singular support is not an $\ell$-adic conductor theorem. |
| Geometric and arithmetic monodromy groups | **MISSING.**  No monodromy group has been computed for the endpoint state. |
| Pairwise linear disjointness across auxiliary $\ell$ | **MISSING.**  No product-surjectivity theorem is available. |
| One fixed conjugacy-stable local condition containing the full gate | **MISSING.**  Item 275 supplies a fixed stratified incidence, but its natural kernel Pluecker line is non-horizontal and no Frobenius conjugacy class is attached. |
| Collision implies avoidance of $\Omega(\ell)$ for every auxiliary $\ell\le L$ | **MISSING.**  Recognition gives only divisibility modulo the varying characteristic $p$. |
| Uniform local density making $P(L)\to\infty$ | **MISSING.**  Algebraic codimension two is not a distribution theorem for the arithmetic section. |

The positive archive statements remain useful but strictly weaker:

* Item 273 proves a rank-at-most-eight rational parameter module with fixed
  finite singular support and retains every affine/rank-drop branch.
* Item 275 proves a rank-six exterior-square module and an exact fixed flag
  incidence, but the natural kernel line is non-horizontal under both
  parameter generators and under the actual fixed-$M$ step.
* Item 281 proves the all-branch Fitting/gcd recognition (1.3).
* Item 284 gives an exact CRT recognition, but neither compatibility nor
  auxiliary-$\ell$ localization follows from it.

Thus bounded rational rank is a recognition theorem, not a bounded-conductor
Frobenius theorem.

## 5. Exact fixed-field and diagonal-modulus obstructions

### 5.1 Fixed-field mismatch

For a fixed $M$, equation (2.1) determines at most one tied parameter
$s$ for each candidate prime $p$.  Varying $p$ therefore changes the
base characteristic.  In contrast, (3.3) averages many points
$u\in U(\mathbf F_q)$ for one fixed $q$, with auxiliary primes
$\ell\ne\operatorname{char}\mathbf F_q$.

Applying a vertical theorem separately at $q=p$ does not average the tied
rows over $p$.  A theorem over an arithmetic base such as an open part of
$\operatorname{Spec}\mathbf Z$, or a genuinely horizontal large sieve
uniform in $p$, would be new input not contained in (3.3).

### 5.2 Diagonal-modulus lemma

Let $p$ and $\ell$ be distinct primes.  The implication



$$
p\mid a,b\quad\Longrightarrow\quad \ell\mid a,b           \tag{5.1}
$$



is false: take $(a,b)=(p,p)$.  More strongly, for every finite set
$\Lambda$ of primes not containing $p$, this same pair is nonzero modulo
every $\ell\in\Lambda$.

Therefore the exact logical content of (1.3) alone cannot put a collision
inside a zero locus modulo all auxiliary $\ell$.  The same observation
applies to a CRT norm: divisibility by $p$ is not simultaneous divisibility
by the auxiliary sieve primes.

This lemma is not a counterexample to a special identity for the actual
sequence $\overline C(M)$.  It proves the narrower point required for the
applicability audit: no auxiliary-local implication follows formally from
the normalized gate/gcd or norm recognition.  A new arithmetic theorem about
the actual sequence is necessary.

### 5.3 A mod-$p$ trace is still insufficient

Suppose only that a future sheaf supplied two matrix coefficients
$t_{0,p},t_{1,p}\in\mathbf F_p$ equal to the divided gate.  Then collision
would say $t_{0,p}=t_{1,p}=0$ in characteristic $p$.  It would still not
say that compatible reductions at auxiliary $\ell$'s vanish.

Two sufficient bridges would be:

1. integral lifts $T_0,T_1$ for which collision implies
   $T_0=T_1=0$ as integers; or
2. a direct horizontal theorem for the diagonal congruences
   $T_0(p)\equiv T_1(p)\equiv0\pmod p$.

No Weil bound or small-height theorem currently turns $p\mid T_i$ into
integer equality, and no direct horizontal diagonal theorem is sealed.  If
one instead uses a framed matrix coefficient, the construction must also
provide a geometric rigidification and an applicable framed equidistribution
theorem; ordinary Frobenius is available only up to conjugacy.

## 6. Conditional bridge and quantitative payoff

This section is a proved conditional calculation, not an assertion that its
hypotheses hold.

Assume a compatible system satisfying Theorem 3.1 has two integral,
conjugacy-invariant Frobenius coefficients $T_0,T_1$, and assume the
actual target implies



$$
T_0=T_1=0.                                                 \tag{6.1}
$$



For each auxiliary $\ell$, let $Z(\ell)$ be their simultaneous zero
locus in the correct monodromy coset and put
$\Omega(\ell)=G_\ell^{\rm arith}\setminus Z(\ell)$ inside
that coset.  If



$$
{\lvert\Omega(\ell)\rvert\over\lvert G_\ell^g\rvert}
 \ge c>0                                                   \tag{6.2}
$$



on a positive-density set of auxiliary primes, then



$$
P(L)\gg {L\over\log L}.                                  \tag{6.3}
$$



Choosing $L=q^{1/(2A)}$ in (3.3) gives



$$
\lvert S(U,\Omega;L)\rvert
 \ll q^{d-1/(2A)}\log q.                                  \tag{6.4}
$$



Thus an exact-zero bridge would convert the compatible-system hypotheses
into a power-saving exceptional-point estimate in Kowalski's fixed-field
setting.

For the actual tied family, the required analogue is any horizontal bound



$$
N(M)=O(M^{1-\delta})\qquad(\delta>0),                     \tag{6.5}
$$



or, more generally, $N(M)=o(M/\log M)$.  By (2.5), either bound yields



$$
W(M)=o(M).                                                \tag{6.6}
$$



After Item 149 de-overlap, (6.6) would remove the complete remaining
isolated fixed-$j=1$ ceiling $1/36$ per $6M$.  This quantifies the
payoff without claiming that (6.4) transfers to (6.5).

## 7. Why codimension and finite rank do not prove density

On the generic chart the fixed-$j=1$ gate is two independent linear
conditions on a four-dimensional graph state.  Item 275 expresses this as a
fixed flag incidence of codimension two.  That geometric fact alone does not
show probability $p^{-2}$, because the arithmetic state is one special
section and no equidistribution theorem is known for it.

Potential reduced ranks zero and one and the affine consistency branches
remain part of the all-branch recognition.  A sheaf-theoretic container would
have to include them or prove their total weighted mass negligible.  The
fixed-window singular factors have only $O(\log M)$ weight, but that result
does not control the nonsingular isolated rows.

Likewise, a rational shift matrix is not a Frobenius matrix merely because
both are finite dimensional.  Translation by $(h,s)$ acts on coefficient
indices in characteristic zero; geometric Frobenius acts through an
arithmetic fundamental group in fixed positive characteristic.  The archive
contains no functor identifying these two actions.

## 8. Admission, de-overlap, and booking

The master admission test has the following exact outcome.

1. **Actual-family implication.**  The normalized pair and its gcd recognize
   every full collision, including every retained affine/rank branch.
2. **De-overlap.**  Item 149 already books the first post-Cartier copy.  A
   large-sieve theorem would control the residual collision set rather than
   create another valuation copy, so its potential saving would be genuine.
3. **Capacity.**  A horizontal count $o(M/\log M)$ would reduce the full
   $M/6+o(M)$ residual log mass to $o(M)$.
4. **Missing input.**  Neither the compatible bounded-complexity Frobenius
   family nor the diagonal-to-auxiliary bridge nor the horizontal density
   theorem is proved.

Consequently no positive capacity reduction is admitted.  The full
$1/36$ per $6M$ ceiling and zero booking remain.

## 9. Reproduction and strict proof labels

The standard-library certificate verifies the phase elimination, endpoint
interval, exact interval length, count-to-log-weight inequality, the
all-distinct-prime diagonal-modulus witness constructor, the conditional
large-sieve exponent calculation, and the complete hypothesis-status table.
It performs no collision scan.

### LITERATURE THEOREM

* Kowalski's Theorem 3.1 and Proposition 3.3 under their stated
  fixed-finite-field compatible-sheaf, independence, and uniform-complexity
  hypotheses.

### PROVED IN THE ARCHIVE

* The exact tied-family interval and $M/6+o(M)$ raw log capacity.
* The fixed-field mismatch between the actual prime-tied rows and the cited
  vertical Frobenius sieve.
* The diagonal-modulus lemma and the failure of recognition alone to supply
  auxiliary-$\ell$ conditions.
* The conditional exact-zero bridge and its power-saving calculation.
* The threshold $N(M)=o(M/\log M)\Rightarrow W(M)=o(M)$.
* The hypothesis-by-hypothesis insufficiency of the currently sealed finite
  translation/Pluecker modules.
* Item 149 de-overlap, unchanged $1/36$ ceiling, and zero booking.

### OPEN

* A compatible bounded-complexity lisse or crystalline system realizing the
  actual normalized fixed-$j=1$ pair.
* Monodromy, cross-$\ell$ independence, and a fixed conjugacy-stable local
  condition retaining all gate branches.
* An exact-zero or other auxiliary-local bridge for the diagonal congruence.
* A horizontal weighted theorem giving $N(M)=o(M/\log M)$.
* Every positive fixed-$j=1$ capacity reduction and every new Route-1 rate.
