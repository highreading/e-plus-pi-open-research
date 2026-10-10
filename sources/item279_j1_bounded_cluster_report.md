> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 279 — bounded fixed-$M$ $j=1$ clusters and the CRT transversality barrier

Checked: 2026-08-31 (Beijing time)

## 1. Quantifiers, admission, and verdict

Stay in the fixed common-log cell



$$
p=4h+6s+3,\qquad h,s\ge1,\qquad M=3h+4s+2.             \tag{1.1}
$$



Fix integers $D\ge1$ and $2\le t\le D+1$ **before** letting
$M\to\infty$.  A bounded cluster pattern is a set



$$
J\subseteq\{0,1,\ldots,D\},\qquad 0\in J,\qquad |J|=t. \tag{1.2}
$$



Anchoring the least parameter point at zero loses no cluster.  Allowing
all patterns in (1.2) means diameter at most $D$; requiring
$\max J=D$ gives exact diameter $D$.

The fixed-$M$ parameter tower is



$$
(h_j,s_j,p_j,M)=(h-4j,s+3j,p+2j,M),\qquad 0\le j\le D. \tag{1.3}
$$



The full simultaneous collision gate is imposed at every prime $p_j$
with $j\in J$.  The conclusions are uniform over all
$\binom D{t-1}$ patterns in (1.2), with constants allowed to depend on
the fixed pair $(D,t)$.

> **PROVED — exact multi-prime module.**  On every unit transport chart,
> if $A_j$ is the pulled-back two-row gate modulo $p_j$ and
> $r_j=\operatorname{rank}A_j\in\{0,1,2\}$, then the complete CRT
> solution module is
>
> 

$$
> \boxed{\mathcal S_J\cong\prod_{j\in J}\ker A_j,
> \qquad |\mathcal S_J|=\prod_{j\in J}p_j^{\,4-r_j}.}     \tag{1.4}
>
$$


>
> Thus every rank-one and rank-zero branch is retained.

> **PROVED — bounded rational transversality gives no product
> valuation.**  Even if any four rational gate rows from different
> parameter points are transverse, their CRT row blocks have no unit
> $4\times4$ minor.  Different prime blocks are killed by orthogonal
> idempotents.  Hence the natural mixed-minor construction cannot force
> product divisibility of the four-state coordinates.

> **PROVED — all bounded non-singleton prime clusters have zero linear
> mass.**  The classical Selberg upper-bound sieve gives, simultaneously
> for all fixed patterns (1.2),
>
> 

$$
> \#\{p\le X:p+2j\text{ prime for every }j\in J\}
> =O_{D,t}\!\left({X\over(\log X)^t}\right).               \tag{1.5}
>
$$


>
> Their endpoint prime-log weight at fixed $M$ is
> $O_{D,t}(M/(\log M)^{t-1})=o(M)$.  The union over every
> non-singleton pattern of diameter at most $D$ is
> $O_D(M/\log M)=o(M)$.

The denominator-free consequence of a cluster is only



$$
\left(\prod_{j\in J}p_j\right)^2
 \mid\gcd(C_0(M),C_1(M)),                                  \tag{1.6}
$$



already contained in Item 197/264's square radical and Item 149's first
post-Cartier copy.  Repeated enumeration of overlapping patterns does not
raise any prime valuation.

The isolated-prime collision problem remains open.  Consequently the
full raw fixed-$j=1$ ceiling stays $1/36$ per $6M$, and



$$
\boxed{\text{new capacity reduction}=0,\qquad
        \text{new unconditional Route-1 rate}=0.}           \tag{1.7}
$$



No assertion here is uniform when $D=D(M)$ grows.

## 2. Exact phase tower and boundary rows

Equation (1.3) follows directly from



$$
\begin{aligned}
 4(h-4j)+6(s+3j)+3&=p+2j,\\
 3(h-4j)+4(s+3j)+2&=M.
\end{aligned}                                               \tag{2.1}
$$



The full forward window exists when



$$
h\ge4D+1.                                                  \tag{2.2}
$$



If (2.2) fails, the anchor lies among at most $4D$ boundary parameter
rows.  Their total prime-log weight is $O_D(\log M)$.  A backward or
two-sided cluster is handled by translating its least offset to zero;
the same boundary count applies at the other endpoint.

At fixed $M$, the actual prime rows lie in Item 264's interval



$$
{4M+3\over3}\le p\le {3M-1\over2},                        \tag{2.3}
$$



whose total raw prime-log weight is $M/6+o(M)$, or $1/36$ after
normalization by $6M$.

## 3. The exact multi-prime CRT module

Let $J$ satisfy (1.2), suppose the distinct integers
$p_j=p+2j$ are prime, and put



$$
N_J=\prod_{j\in J}p_j.                                    \tag{3.1}
$$



On a unit chart, compose Item 273/275's exact fixed-$M$ rational
transports to identify each local graph state with a common four-state
$X$.  After clearing only denominators that are $p_j$-units, write



$$
A_jX=0\quad\text{in }\mathbb F_{p_j}^{\,2},\qquad
 r_j=\operatorname{rank}_{\mathbb F_{p_j}}A_j\in\{0,1,2\}.
                                                                    \tag{3.2}
$$



CRT gives



$$
\mathbb Z/N_J\mathbb Z\cong
 \prod_{j\in J}\mathbb F_{p_j}.                           \tag{3.3}
$$



Taking the kernel component by component proves the exact isomorphism
(1.4).  In particular, a rank-two component contributes $p_j^2$
solutions, a rank-one component $p_j^3$, and a rank-zero component
$p_j^4$.  Rank drop weakens the incidence; it never supplies a missing
cross-prime equation.

If a transport denominator is not a unit, the common-state chart is not
used.  The original local gate remains valid, while the denominator-free
fixed-coefficient implication in Section 5 remains unconditional.  For
fixed $D$, every such chart failure lies in the exceptional container
of Section 6.

## 4. All mixed maximal minors vanish over CRT

For $j\in J$, let $e_j\in\mathbb Z/N_J\mathbb Z$ be the CRT
idempotent which equals one in the $p_j$-component and zero in every
other component.  Then



$$
e_j^2=e_j,\qquad e_je_k=0\quad(j\ne k),\qquad
 \sum_{j\in J}e_j=1.                                       \tag{4.1}
$$



The one-ring mixed gate is the $2t$-row matrix



$$
\mathcal M_J=
 \begin{pmatrix}
  e_{j_1}A_{j_1}\\
  e_{j_2}A_{j_2}\\
  \vdots\\
  e_{j_t}A_{j_t}
 \end{pmatrix}.                                             \tag{4.2}
$$



Every block has only two rows.  Therefore any choice of four rows uses at
least two distinct blocks.  By multilinearity, its determinant contains
$e_j^ae_k^b$ with $j\ne k$ and positive $a,b$, hence



$$
\boxed{I_4(\mathcal M_J)=0
 \quad\text{in }\mathbb Z/N_J\mathbb Z.}                  \tag{4.3}
$$



This holds for every $t\ge2$, every pattern, every set of rational
pulled-back planes, and every rank profile.  A nonzero determinant of a
rational four-row substack does not survive as a unit CRT minor.

The componentwise reason is even more direct: in the $p_j$-component,
only the two rows of $A_j$ remain, so the map from a four-state has a
kernel of dimension at least two.  Thus no mixed system of this natural
form is injective over $\mathbb Z/N_J\mathbb Z$, and it cannot imply
$X\equiv0\pmod{N_J}$.

An exact transverse model makes the obstruction concrete.  Take



$$
J=\{0,1,4\},\qquad(p_0,p_1,p_4)=(29,31,37),               \tag{4.4}
$$



with



$$
A_0=A_4=
 \begin{pmatrix}1&0&0&0\\0&1&0&0\end{pmatrix},\qquad
 A_1=
 \begin{pmatrix}0&0&1&0\\0&0&0&1\end{pmatrix}.           \tag{4.5}
$$



The rational stack $\binom{A_0}{A_1}$ has determinant one, while all
fifteen $4\times4$ minors of (4.2) vanish modulo
$N_J=29\cdot31\cdot37=33263$.  Moreover



$$
X=(29\cdot37,0,31,0)^{\mathsf T}                          \tag{4.6}
$$



satisfies all three local gates but is not zero modulo $N_J$.

The scope of (4.3) is precise.  It excludes an independent product
valuation obtained solely by stacking the bounded-window rational gate
planes and taking their ordinary mixed minors.  It does not exclude a
new cross-prime invariant involving additional arithmetic data.

## 5. The only unconditional fixed-integer cluster consequence

Recall Item 277's fixed integers



$$
C_\nu(M)=[z^{4M+\nu}]
 { (1-z)^{6M}(1+z)^{1+3\nu}
  \over(1+z^2)^{4M+1+\nu}}\in\mathbb Z,
 \qquad\nu=0,1.                                             \tag{5.1}
$$



The actual full divided collision at $p_j$ gives



$$
p_j^2\mid C_0(M),\qquad p_j^2\mid C_1(M).                 \tag{5.2}
$$



The primes are distinct, so simultaneous collisions on $J$ give
(1.6).  This statement needs no transport chart and includes every
rank-drop and denominator branch.

Let $\mathcal P_M$ be any family of overlapping cluster patterns and
let $V_M$ be the union of their endpoint collision primes.  Then the
strongest consequence obtained by multiplying (5.2) is



$$
\left(\prod_{q\in V_M}q\right)^2
 \mid\gcd(C_0(M),C_1(M)).                                  \tag{5.3}
$$



One must take the radical union in (5.3), not multiply once for every
pattern containing $q$.  Membership in several clusters does not
upgrade $q^2$ to $q^4$, $q^6$, or any higher power.  Equation
(5.3) is exactly a subproduct of Item 197/264's already recorded square
radical.  Item 149 already books the first post-Cartier copy.  Hence this
branch produces no independent valuation copy.

## 6. Exceptional transport factors

Item 273 proves that every fixed parameter-shift window has only finitely
many translated singular factors



$$
\ell(h,s)=\alpha h+\beta s+\gamma.                         \tag{6.1}
$$



On the fixed-$M$ parametrization



$$
h=3M-2p,\qquad s={3p-4M-1\over2},                         \tag{6.2}
$$



one has



$$
2\ell(h,s)\equiv
 (6\alpha-4\beta)M+(2\gamma-\beta)\pmod p.               \tag{6.3}
$$



For a fixed diameter $D$, there are $O_D(1)$ translated factors.
None has phase-proportional slope.  Thus every exceptional prime divides
one of $O_D(1)$ nonzero integers of size $O_D(M)$, and



$$
\sum_{p\text{ exceptional in the }D\text{-window}}\log p
 =O_D(\log M).                                              \tag{6.4}
$$



Together with the $O_D(\log M)$ boundary rows from Section 2, this is
zero normalized mass.  These branches are retained through (5.2)--(5.3);
only the common rational-state description (3.2) is withheld there.

## 7. Uniform bounded-pattern sieve theorem

For one pattern $J$, define the distinct linear forms



$$
L_j(n)=n+2j,\qquad j\in J.                                \tag{7.1}
$$



If the tuple is admissible, the classical Selberg upper-bound sieve for a
fixed $t$-tuple of distinct linear forms gives



$$
\#\{n\le X:L_j(n)\text{ prime for all }j\in J\}
 \ll_J {X\over(\log X)^t}.                                 \tag{7.2}
$$



If the tuple is inadmissible, a fixed prime divides the product of the
forms for every $n$; simultaneous primality then has only the finite
exceptional possibilities in which one of the forms equals that fixed
prime.  It obeys (7.2) after enlarging the constant.

There are exactly



$$
\binom D{t-1}                                              \tag{7.3}
$$



patterns (1.2).  Because $D,t$ are fixed, summing (7.2) proves the
uniform all-pattern estimate (1.5), with one constant depending only on
$(D,t)$.  Every endpoint in (2.3) has logarithm $O(\log M)$, so all
endpoints of all size-$t$ clusters have total log weight



$$
O_{D,t}\!\left({M\over(\log M)^{t-1}}\right)=o(M).        \tag{7.4}
$$



Finally, summing over the fixed set $2\le t\le D+1$ is dominated by
$t=2$:



$$
\sum_{\substack{q\text{ prime in }(2.3)\\
       q\text{ belongs to a prime cluster of diameter }\le D}}
 \log q
 =O_D\!\left({M\over\log M}\right)=o(M).                  \tag{7.5}
$$



The collision clusters are a subset of these ambient prime clusters, so
(7.4)--(7.5) apply without any distribution assumption about the gate.
This is a genuine asymptotic theorem, not an extrapolation from the finite
replay.

## 8. Isolated primes and the unchanged capacity

Call an actual prime row $D$-isolated when no other actual prime row
lies within $D$ parameter steps.  Equation (7.5) controls the
non-isolated rows only.  It gives no estimate for the collision gate on
the $D$-isolated rows.

For fixed $D$, the ambient prime weight of non-isolated rows is already
$o(M)$; equivalently, bounded clusters cannot carry a positive fraction
of the raw $M/6+o(M)$ weight.  Thus even a perfect exclusion of every
bounded non-singleton collision cluster would leave the entire linear
ceiling on the isolated-prime rows.

The master admission test therefore gives:

1. **Actual-family implication:** (1.6) and the product-kernel module
   (1.4) hold, with the exceptional branches treated by Section 5.
2. **De-overlap:** (1.6) is already the Item 197/264 square radical and
   Item 149 first-copy mechanism; overlapping patterns are radicalized.
3. **Capacity:** all bounded non-singleton ambient clusters have only
   $o(M)$ log weight, while isolated collision primes remain
   uncontrolled at linear scale.

No retained ceiling below $1/36$ per $6M$ follows.  The booking is
strictly zero.

## 9. Replay and proof labels

The standard-library checker verifies:

* the exact phase tower (1.3) on 12,716 deterministic integer rows;
* the CRT idempotent identities and all fifteen mixed maximal minors in
  the three-prime transverse witness (4.4)--(4.6);
* the product-square divisibility witness;
* every anchored pattern for $D=6$, all sizes
  $2\le t\le7$, and all base primes up to 10,000.

The last bullet is **EXACT FINITE ONLY**.  The asymptotic estimates
(7.2)--(7.5) use the classical unconditional Selberg upper-bound sieve,
not the finite replay.

### PROVED

* The phase tower, fixed-$D$ boundary range, and exact quantifiers.
* The complete multi-prime CRT product-kernel module for every rank
  profile.
* Vanishing of all natural mixed $4\times4$ CRT minors, regardless of
  rational multi-plane transversality.
* The square-radical fixed-integer consequence and zero extra valuation.
* The $O_D(\log M)$ singular/boundary containers.
* The uniform all-pattern sieve bound and $o(M)$ log mass for every
  fixed bounded non-singleton cluster family.
* Item 149/264 de-overlap, unchanged $1/36$ ceiling, and zero booking.

### EXACT FINITE ONLY

* The bounded phase, CRT witness, and $D=6$ prime-pattern replays.

### OPEN

* Weighted control of the full gate on $D$-isolated prime rows.
* Any theorem uniform for a diameter $D=D(M)$ growing with $M$.
* A cross-prime invariant using arithmetic information beyond the natural
  bounded rational gate-plane stack.
* Any positive fixed-$j=1$ capacity reduction or new Route-1 rate.
