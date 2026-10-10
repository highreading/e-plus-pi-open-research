> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 289 — exact Archimedean balancing in the fixed-$j=1$ CRT norm class

Checked: 2026-08-31 (Beijing time)

## 1. Scope, admission audit, and verdict

Fix $M$ and retain Item 284's complete candidate product



$$
B=B_M=\prod_{p\in\mathcal S_M}p,
 \qquad
 \mathcal S_M=\left\{p\text{ prime}:{4M+3\over3}\le p\le{3M-1\over2}\right\}.
                                                                    \tag{1.1}
$$



Let $d_0$ be any **fixed** CRT class which is a quadratic nonresidue modulo
every $p\mid B$, and put



$$
x=\overline C_0(M),\qquad y=\overline C_1(M),\qquad
 d=d_0+kB\quad(k\in\mathbf Z).                              \tag{1.2}
$$



Every representative preserves the exact gate recognition



$$
p\mid x^2-dy^2\quad\Longleftrightarrow\quad p\mid x,y
 \quad(p\mid B).                                           \tag{1.3}
$$



This item permits arbitrary positive or negative representatives and chooses
the optimal one by exact Archimedean balancing.  It does not factor a norm or
use the unknown collision subset.

The class $d_0\bmod B$ is frozen before this optimization.  The theorem
closes representative choice inside that one arithmetic progression.  It
does not optimize across the many different simultaneous-nonresidue CRT
classes obtained by changing the local nonresidue at one or more candidate
primes.

The main theorem below assumes the nonempty-candidate case $B>1$.  The
zero-capacity boundary $B=1$, where a representative norm may vanish, is
retained separately in Section 2.

> **PROVED — exact global minimum over the CRT class.**  If $B>1$ and
> $y\ne0$, set
> 
> 

$$
>  t=x^2-d_0y^2,\qquad q=By^2,
> \qquad r=t\bmod q\quad(0\le r<q).                         \tag{1.4}
>
$$


> 
> Then
> 
> 

$$
>  \boxed{\min_{k\in\mathbf Z}|x^2-(d_0+kB)y^2|
>  =\min(r,q-r)=\operatorname{dist}(t,q\mathbf Z).}        \tag{1.5}
>
$$


> 
> The minimizing $k$ is obtained by one nearest-integer division.  For a
> nonzero pair with $y\ne0$, the minimum is positive and the minimizer is
> unique.  When $y=0$, every $k$ gives the same value $x^2$.

> **PROVED — exact primitive factorization and all-representative ideal.**
> Put $c=\gcd(|x|,|y|)$, $x=cX$, and $y=cY$.  If
> $(x,y)\ne(0,0)$, then
> 
> 

$$
>  \gcd(X^2-d_0Y^2,BY^2)=1.                                \tag{1.6}
>
$$


> 
> Consequently every representative norm has the exact form
> 
> 

$$
>  x^2-(d_0+kB)y^2
>  =c^2\{X^2-d_0Y^2-kBY^2\},                               \tag{1.7}
>
$$


> 
> with the braced cofactor coprime to $B$.  In particular,
> 
> 

$$
>  \boxed{v_p(x^2-dy^2)=2v_p(c)\quad(p\mid B)}             \tag{1.8}
>
$$


> 
> for every representative, and
> 
> 

$$
>  \boxed{\gcd\bigl(x^2-d_0y^2,\ x^2-(d_0+B)y^2\bigr)=c^2.}
>                                                                    \tag{1.9}
>
$$



Thus changing the representative never changes a candidate-prime
valuation.  It only balances a cofactor supported away from $B$.
Unrestricted Bezout recombination of two adjacent norms recovers exactly
$c^2$, which is Item 281's original Fitting/gcd target squared; this is an
exact localization, not a new small-height invariant.

The valuation theorem and the Archimedean theorem are distinct.  Equation
(1.8) identifies the candidate part exactly as $c^2$, but supplies no
uniform upper bound on $c$.  Equation (1.5) computes the nearest-lattice
distance exactly, but supplies no useful uniform upper bound on that distance
for the actual coefficient sequence beyond (1.10).

> **PROVED — scoped one-dimensional spacing barrier.**  For $B>1$ and
> $y\ne0$, the norm values are one affine lattice $t+q\mathbf Z$.
> Nearest-integer balancing is already
> globally optimal and gives
> 
> 

$$
>  0<\min_k|x^2-(d_0+kB)y^2|<{B|y|^2\over2}.               \tag{1.10}
>
$$


> 
> The factor $1/2$ is the covering-radius constant of this one fixed-class
> lattice.
> Improving (1.10) exponentially requires new arithmetic information on
> the actual residue phase $t/q$; no geometry-of-numbers refinement of the
> same one-dimensional lattice can do so.

With the frozen componentwise bounds, (1.10) reproduces exactly Item 284's
normalized ratio $H-\kappa+1/12$ and raw ratio $H/2+1/24$.  Therefore
allowing every representative proves no exponential height improvement and
no retained-ceiling reduction.

Item 149 already books the first post-Cartier copy.  The decision is



$$
\boxed{\text{new fixed-\(j=1\) capacity reduction}=0,\qquad
        \text{new unconditional Route-1 rate}=0.}           \tag{1.11}
$$



The raw ceiling remains $1/36$ per $6M$.  No collision census is used.

## 2. Boundary branches and exact recognition

Assume first that $B>1$.  It is odd and squarefree.  Since $d_0$ is a
nonresidue modulo every prime factor of $B$,



$$
\gcd(d_0,B)=1.                                            \tag{2.1}
$$



For $p\mid B$, reduction of a representative norm gives



$$
x^2-dy^2\equiv x^2-d_0y^2\pmod p.                         \tag{2.2}
$$



If $y\not\equiv0\pmod p$, a zero in (2.2) would make $d_0$ a square.
If $y\equiv0\pmod p$, a zero forces $x\equiv0\pmod p$.
This proves (1.3) without division by $y$ and retains every branch.

The zero-coordinate cases are exact.

* If $y=0$ and $x\ne0$, every norm equals $x^2=c^2$; there is
  nothing to balance.
* If $x=0$ and $y\ne0$, the minimum is
  $|y|^2\min_k|d_0+kB|$, and (1.6)--(1.9) still hold.
* If $x=y=0$, every representative norm is zero and every candidate
  prime collides.  Absolute-height arguments are degenerate, so the raw
  ceiling is retained.
* If $B=1$, the candidate set is empty and this cell has zero prime-log
  mass.  A representative can make the norm zero when, for example,
  $Y=\pm1$.  The positivity, uniqueness, and strict covering bound in the
  main theorem concern $B>1$.

No prime, zero-coordinate, or integer-zero branch is silently divided away.

## 3. Nearest-lattice proof and unique minimizer

For $y\ne0$, equation (1.2) gives



$$
N_k=x^2-(d_0+kB)y^2=t-kq.                                 \tag{3.1}
$$



Write $t=aq+r$ with $0\le r<q$.  The two closest lattice points are
$aq$ and $(a+1)q$, at distances $r$ and $q-r$.  This proves
(1.5).  Explicitly,



$$
k_*=
 \begin{cases}
  (t-r)/q,&r<q-r,\\
  (t+q-r)/q,&r>q-r.
 \end{cases}                                                \tag{3.2}
$$



Section 4 proves that after removing $c^2$, the residue is a unit modulo
$Q=BY^2$.  Since $B\ge3$ is odd, this rules out both $r=0$ and a tie
$r=q/2$.  Thus $N_{k_*}\ne0$ and the minimizer is unique whenever the
pair is nonzero and $y\ne0$.

The algorithm uses only multiplication, Euclidean division, and comparison.
It neither factors $N_k$ nor asks which candidate primes collide.

## 4. Primitive cofactor theorem

Let $c,X,Y$ be as in (1.6), so $\gcd(X,Y)=1$.  Put



$$
T=X^2-d_0Y^2,\qquad Q=BY^2.                              \tag{4.1}
$$



First,



$$
\gcd(T,Y)=\gcd(X^2,Y)=1.                                 \tag{4.2}
$$



Now let $p\mid B$.  If $p\mid T$ and $p\nmid Y$, then
$d_0\equiv(X/Y)^2\pmod p$, contradicting nonresiduosity.  If
$p\mid Y$, then $p\mid T$ forces $p\mid X$, contradicting
$\gcd(X,Y)=1$.  Hence



$$
\gcd(T,B)=1.                                              \tag{4.3}
$$



Equations (4.2)--(4.3) prove (1.6).  Moreover,



$$
\gcd(T-kQ,Q)=\gcd(T,Q)=1                                 \tag{4.4}
$$



for every $k$.  Multiplying by $c^2$ proves (1.7)--(1.8).

Finally,



$$
\begin{aligned}
 \gcd(N_0,N_1)
 &=c^2\gcd(T,T-Q)\\
 &=c^2\gcd(T,Q)=c^2,
 \end{aligned}                                             \tag{4.5}
$$



which proves (1.9).  Equivalently, the ideal generated by *all*
representative norms is



$$
(N_k:k\in\mathbf Z)=c^2\mathbf Z.                         \tag{4.6}
$$



Thus a Euclidean algorithm on adjacent representatives produces no object
beyond the original specialized Fitting generator.

## 5. What Archimedean balancing can and cannot change

Define the reduced balanced cofactor



$$
\mu'=\min_{k\in\mathbf Z}|T-kQ|.                         \tag{5.1}
$$



Then the exact optimum is



$$
\mu=c^2\mu',qquad
 1\le\mu'<{Q\over2},qquad
 \gcd(\mu',Q)=1.                                          \tag{5.2}
$$



In particular, every candidate-prime factor of $\mu$ comes entirely from
$c^2$.  The balancing step changes only $\mu'$, which is coprime to the
full moving candidate product $B$.

This is both positive recognition and a barrier:

* the representative can be optimized exactly without factorization;
* no representative can remove the square $c^2$ carrying the collision
  primes;
* the worst purely metric bound on the remaining phase is the covering
  radius $Q/2$; and
* a better asymptotic bound needs a theorem about the special residues
  $T\bmod Q$, not another choice of representative.

The declared exact lattice witness



$$
B=35,\quad d_0=3,\quad X=163,\quad Y=36                  \tag{5.3}
$$



has $d_0$ nonsquare modulo both $5$ and $7$, and



$$
T=22681,qquad Q=45360,qquad \mu'=22679={Q\over2}-1.    \tag{5.4}
$$



It shows within the simultaneous-nonresidue norm class that the reduced
phase can lie essentially at the covering boundary.  This is a declared
finite witness, not an assertion about the actual coefficient sequence.

## 6. Natural bounded-degree analogues

Take $e\ge1$ representatives $d_i=d_0+k_iB$ and form the natural
product



$$
P_{\mathbf k}=\prod_{i=1}^e(x^2-d_i y^2).                 \tag{6.1}
$$



The factors can be balanced independently, so



$$
\min_{\mathbf k}|P_{\mathbf k}|=\mu^e.                   \tag{6.2}
$$



For every candidate prime,



$$
v_p(P_{\mathbf k})=2e\,v_p(c).                           \tag{6.3}
$$



Consequently the divisor-to-height ratio of the optimal product is exactly



$$
{\log\mu^e\over2e}={\log\mu\over2}.                      \tag{6.4}
$$



Powers and finite products of same-class CRT norms add no gain.  On the
other hand, unrestricted integer linear recombination reaches the ideal
generator $c^2$ by (4.6), but this is the original gcd problem and its
Bezout coefficients depend on the full state.

The adjacent difference



$$
N_k-N_{k+1}=By^2                                         \tag{6.5}
$$



is divisible by every candidate prime, including every noncollision prime,
so eliminating the phase by differences loses exact gate recognition.

These conclusions are scoped to products, powers, differences, and
unrestricted ideal recombination of the same-class quadratic norms.  A
separately proved low-height cancellation in a different bounded-degree
expression is not ruled out.

## 7. Height and capacity audit

Item 264's componentwise constant and Item 200's forced-product constant are



$$
H=6.327627545440858\ldots,
 \qquad
 \kappa=-4\log2+{\pi\over\sqrt3}+3\log3
 =2.33704750799876\ldots.                                  \tag{7.1}
$$



For either normalized component,



$$
\log\max(1,|x|,|y|)\le(H-\kappa)M+o(M),                  \tag{7.2}
$$



and



$$
\log B={M\over6}+o(M).                                   \tag{7.3}
$$



Equation (1.10) therefore gives



$$
\log\mu\le
 \{2(H-\kappa)+1/6\}M+o(M).                               \tag{7.4}
$$



If $R_M^{(1)}$ is the collision radical, then (1.8) gives



$$
(R_M^{(1)})^2\mid\mu.                                    \tag{7.5}
$$



Thus the balanced normalized ratio is still



$$
{\log R_M^{(1)}\over M}
 \le H-\kappa+{1\over12}+o(1)
 =4.07391337077542\ldots+o(1),                             \tag{7.6}
$$



far above the raw $1/6$ mass.

For the raw coordinates $C_\nu=F_M\overline C_\nu$, every representative
norm is exactly $F_M^2\mu$.  Combining (7.4) with
$\log F_M=\kappa M+o(M)$ reproduces



$$
{1\over4M}\log(F_M^2\mu)
 \le {H\over2}+{1\over24}+o(1)
 =3.20548043938709\ldots+o(1).                             \tag{7.7}
$$



The factor $F_M^2$ is forced content already covered by the existing
Cartier/post-Cartier accounting; it cannot be booked again.

A genuinely useful normalized cancellation theorem would need at least



$$
\log\mu\le(1/3-\varepsilon)M                              \tag{7.8}
$$



for some $\varepsilon>0$, because (7.5) would then put the collision
log mass below $M/6$.  Neither (1.5) nor the coprimality in (5.2) proves
(7.8).  Alternatively one could bound the moving candidate part of
$c=\gcd(x,y)$ directly, but that is precisely Item 281's open Fitting/gcd
problem.

The admission test therefore fails:

1. exact recognition is preserved for every representative;
2. balancing is globally optimal and factorization-independent;
3. candidate valuations are invariant and equal those of $c^2$;
4. the inherited exponent is unchanged; and
5. the only moving-prime localization is the tautological identity with
   $c^2$; no new bound-producing localization or small-gcd theorem is
   obtained.

The $1/36$ ceiling and zero booking remain.

## 8. Reproduction and strict labels

The standard-library checker verifies the exact nearest-representative
formula, uniqueness, primitive coprimality, candidate valuations, adjacent
gcd, product theorem, declared covering-boundary witness, frozen height
constants, and all zero-coordinate branches.  Its bounded algebra replay is
**EXACT FINITE ONLY** and contains no actual collision census.

### PROVED

* The exact optimal representative and minimum (1.5).
* The primitive cofactor theorem, candidate-valuation invariance, and
  all-representative ideal $c^2\mathbf Z$.
* The exact one-dimensional spacing/covering-radius barrier.
* No gain from natural bounded products or powers of same-class norms.
* The unchanged normalized and raw inherited height ratios.
* Item 149 de-overlap, unchanged $1/36$ ceiling, and zero booking.

### EXACT FINITE ONLY

* The portable bounded algebra replay and the declared witness (5.3)--(5.4).

### OPEN

* Any actual-family theorem placing $T\bmod Q$ exponentially closer to
  zero than the covering-radius bound.
* Optimization across the distinct simultaneous-nonresidue CRT classes;
  this report closes only representatives of the fixed class $d_0\bmod B$.
* A bound $\log\mu<(1/3-\varepsilon)M$, or a useful moving-prime bound on
  $\gcd(x,y)$.
* A different bounded-degree expression with separately proved exponential
  cancellation.
* Every positive fixed-$j=1$ capacity reduction and every new Route-1 rate.
