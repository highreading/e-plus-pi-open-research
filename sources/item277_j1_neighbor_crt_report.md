> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 277 — neighboring $j=1$ collisions, CRT, and zero cluster mass

Checked: 2026-08-31 (Beijing time)

## 1. Scope, phase relocation, and verdict

Stay in the fixed $j=1$ family



$$
p=4h+6s+3,\qquad h,s\ge1,\qquad M=3h+4s+2.                 \tag{1.1}
$$



Adjacent fixed-$M$ parameter points satisfy



$$
(h,s,p,M)\longmapsto(h-4,s+3,p+2,M),\qquad h\ge5.          \tag{1.2}
$$



Indeed,



$$
4(h-4)+6(s+3)+3=p+2,\qquad
 3(h-4)+4(s+3)+2=M.                                         \tag{1.3}
$$



This item asks what follows if both $p$ and $q=p+2$ are prime and both
rows satisfy the full simultaneous gate.

> **PROVED — strongest fixed-integer CRT consequence.**  If both rows
> collide, then
>
> 

$$
> \boxed{[p(p+2)]^2\mid\gcd(C_0(M),C_1(M)).}                 \tag{1.4}
>
$$


>
> This is exactly the distinct-prime square divisibility already contained
> in Item 197/264.  It is not a third valuation copy and does not improve
> the exponent at either prime.

> **PROVED — cross-field transversality obstruction.**  Even if the two
> pulled-back gate planes are transverse over $\mathbb Q$, the mixed
> congruences live in $\mathbb F_p$ and $\mathbb F_{p+2}$.  CRT splits
> their solution module as a product of the two kernels.  The rational
> stacked determinant does not become an invertible determinant modulo
> $p(p+2)$, and it forces no $p(p+2)$-divisibility of the state.

> **PROVED — neighboring clusters have zero linear mass.**  Such adjacent
> prime rows are twin-prime positions.  The classical Brun/Selberg
> upper-bound sieve gives $O(M/\log^2M)$ possible edges and
> $O(M/\log M)=o(M)$ endpoint prime-log weight at fixed $M$.

Thus even a perfect all-prime exclusion of simultaneous neighboring
collisions could remove only zero normalized mass.  Item 149 already books
the first post-Cartier copy, so



$$
\boxed{\text{new fixed-\(j=1\) capacity reduction}=0,\qquad
        \text{new unconditional Route-1 rate}=0.}            \tag{1.5}
$$



The full raw ceiling remains $1/36$ per $6M$.

## 2. The denominator-free square CRT theorem

Recall the fixed integers



$$
C_\nu(M)=[z^{4M+\nu}]
 { (1-z)^{6M}(1+z)^{1+3\nu}
  \over(1+z^2)^{4M+1+\nu}}\in\mathbb Z,\qquad \nu=0,1.       \tag{2.1}
$$



On every actual row, the divided full gate is equivalent to



$$
p^2\mid C_0(M),\qquad p^2\mid C_1(M).                      \tag{2.2}
$$



For $q=p+2$, one has $\gcd(p,q)=1$.  Therefore, for either coordinate,



$$
p^2\mid C_\nu,\quad q^2\mid C_\nu
 \quad\Longleftrightarrow\quad
 (pq)^2\mid C_\nu.                                          \tag{2.3}
$$



This proves (1.4) without local denominators, transport matrices, or rank
assumptions.

If $\mathcal E_M$ is any set of neighboring collision edges and
$\mathcal V_M$ its set of endpoint primes, then



$$
\left(\prod_{r\in\mathcal V_M}r\right)^2
 \mid\gcd(C_0(M),C_1(M)).                                   \tag{2.4}
$$



Equation (2.4) is already a subproduct of Item 197/264's
$R_M^2\mid\gcd(C_0,C_1)$, where $R_M$ contains every collision prime.
No endpoint receives exponent four merely because it belongs to a pair.

In fact, the neighboring edges do not overlap in the actual range.  If
$p>5$ and $p,p+2$ are both prime, then $p\equiv2\pmod3$, so



$$
3\mid p-2,\qquad 3\mid p+4.                                \tag{2.5}
$$



Both adjacent outside parameter points are composite.  Thus there is not
even a combinatorial source of repeated edge multiplicity.

## 3. Complete mixed-state CRT description

Work first on the unit chart from Item 273/275.  Pull the $q=p+2$ state
back to the $p$-row rational frame by the exact fixed-$M$ transport
$W_{h,s}$.  After clearing denominators which are units in the relevant
field, write



$$
A=G_{h,s}\pmod p,\qquad
 B=G_{h-4,s+3}W_{h,s}\pmod q.                               \tag{3.1}
$$



Let their ranks be



$$
r_p=\operatorname{rank}_{\mathbb F_p}A,\qquad
 r_q=\operatorname{rank}_{\mathbb F_q}B,\qquad
 r_p,r_q\in\{0,1,2\}.                                       \tag{3.2}
$$



The two collision conditions on an integral clearing $X$ are simply



$$
AX_p=0\quad\text{in }\mathbb F_p^2,\qquad
 BX_q=0\quad\text{in }\mathbb F_q^2.                        \tag{3.3}
$$



CRT gives the exact solution-module isomorphism



$$
\boxed{
 \mathcal S_{p,q}\cong
 \ker(A:\mathbb F_p^4\to\mathbb F_p^2)
 \times
 \ker(B:\mathbb F_q^4\to\mathbb F_q^2).}                    \tag{3.4}
$$



Consequently



$$
|\mathcal S_{p,q}|=p^{\,4-r_p}q^{\,4-r_q}.                 \tag{3.5}
$$



This retains all nine rank pairs.  Rank drops make the mixed condition
weaker, never stronger.

For the generic pair $r_p=r_q=2$, (3.5) still leaves $p^2q^2$
solutions modulo $pq$.  Thus two transverse planes over a common field
would have zero intersection, but two planes imposed in different CRT
components leave a large product kernel.

## 4. Why the stacked determinant vanishes over CRT

Let $N=pq$, and let $e_p,e_q\in\mathbb Z/N\mathbb Z$ be the CRT
idempotents



$$
e_p=(1,0),\qquad e_q=(0,1)
 \quad\text{under}\quad
 \mathbb Z/N\mathbb Z\cong\mathbb F_p\times\mathbb F_q.      \tag{4.1}
$$



Then



$$
e_p^2=e_p,\quad e_q^2=e_q,\quad e_pe_q=0.                  \tag{4.2}
$$



The one-ring version of (3.3) is



$$
\mathcal M X=0,\qquad
 \mathcal M=
 \begin{pmatrix}
 e_pA\\ e_qB
 \end{pmatrix}.                                             \tag{4.3}
$$



Regardless of the ordinary stacked determinant of $\binom AB$,



$$
\det\mathcal M=e_p^2e_q^2\det\begin{pmatrix}A\\B\end{pmatrix}
 =0\quad\text{in }\mathbb Z/N\mathbb Z.                     \tag{4.4}
$$



Equivalently, using integer row scalings $qA$ and $pB$, the determinant
contains the tautological factor



$$
\det\begin{pmatrix}qA\\pB\end{pmatrix}
 =p^2q^2\det\begin{pmatrix}A\\B\end{pmatrix}.                \tag{4.5}
$$



Thus the mixed matrix is never invertible modulo $N$, even when the
rational row planes are transverse.

An exact model shows that no hidden coordinate divisibility survives.
Take



$$
A=\begin{pmatrix}1&0&0&0\\0&1&0&0\end{pmatrix},\qquad
 B=\begin{pmatrix}0&0&1&0\\0&0&0&1\end{pmatrix}.             \tag{4.6}
$$



The ordinary stacked determinant is one.  Nevertheless



$$
X=(p,0,q,0)^{\mathsf T}                                    \tag{4.7}
$$



satisfies $AX=0\pmod p$ and $BX=0\pmod q$, while
$X\not\equiv0\pmod{pq}$.  Hence cross-field transversality does not force
the state coordinates to acquire a product divisor.

The direct scalar consequence



$$
p q\mid (a_i\cdot X)(b_j\cdot X)                           \tag{4.8}
$$



for one $A$-row $a_i$ and one $B$-row $b_j$ is merely the product
of the two original congruences.  It is edge-dependent and supplies no
new fixed integer or valuation beyond (2.3).

## 5. The exact Item 275 transverse witness

Item 275's actual fixed-$M$ pair is



$$
(h,s,p,M)=(5,1,29,21)
 \longmapsto(1,4,31,21),                                    \tag{5.1}
$$



with



$$
\det\begin{pmatrix}
 G_{5,1}\\G_{1,4}W_{5,1}
 \end{pmatrix}
 =-{585482135072\over1165539375}\ne0.                       \tag{5.2}
$$



This is the strongest possible rational transversality: the two row
planes span the full four-dimensional dual state space.  Nevertheless,
the first collision would be modulo $29$ and the second modulo $31$.
Equations (3.4) and (4.4) apply exactly, so (5.2) gives no additional
product divisibility.

If a transport denominator meets one of Item 273's fixed singular
factors, that row belongs to the already proved fixed-window
$O(\log M)$ exceptional container.  The obstruction above holds on the
unit chart; the exceptional branches are weaker and have zero normalized
mass.

## 6. Cluster spacing and logarithmic capacity

At fixed $M$, all actual $j=1$ primes lie in



$$
{4M+3\over3}\le p\le {3M-1\over2}.                         \tag{6.1}
$$



A neighboring edge requires both $p$ and $p+2$ prime.  The classical
Brun/Selberg upper-bound sieve states



$$
\#\{p\le X:p,\ p+2\text{ prime}\}
 =O\!\left({X\over(\log X)^2}\right).                        \tag{6.2}
$$



Apply (6.2) with $X=2M$.  The total log weight of both endpoints of all
neighboring prime edges in (6.1) is at most



$$
\begin{aligned}
 \sum_{\substack{p\text{ in }(6.1)\\p,p+2\text{ prime}}}
 \bigl(\log p+\log(p+2)\bigr)
 &\ll \log(2M){M\over(\log M)^2}\\
 &=O\!\left({M\over\log M}\right)=o(M).
\end{aligned}                                               \tag{6.3}
$$



The simultaneous collision edges form a subset, so they have the same
$o(M)$ upper bound.

This is an unconditional weighted theorem, but it affects zero linear
mass.  Even proving that no neighboring pair ever collides would leave
the isolated collision primes completely uncontrolled and would not
lower the raw $M/6+o(M)$, or $1/36$ per $6M$, ceiling.

## 7. Admission and de-overlap

The master admission test now has an exact answer.

1. **Actual-family implication:** a neighboring double collision implies
   (2.3), and the mixed local states satisfy the product-kernel
   description (3.4).
2. **De-overlap:** (2.3) is already part of Item 197/264's square radical
   and Item 149's booked post-Cartier copy; no new exponent appears.
3. **Capacity:** all neighboring prime endpoints have only $o(M)$
   log weight by (6.3).

Therefore the mechanism has zero maximum linear capacity before any
collision theorem is applied.  No retained ceiling below $1/36$ and no
new Route-1 rate result.

## 8. Replay and proof labels

The standard-library checker verifies:

* the exact phase relocation (1.2) on a deterministic integer grid;
* the square CRT identity (2.3);
* the full CRT idempotent obstruction (4.1)--(4.7);
* Item 275's exact actual transverse witness (5.1)--(5.2);
* twin-edge isolation through a bounded replay.

The bounded twin replay is **EXACT FINITE ONLY**.  The asymptotic estimate
(6.2) is the classical unconditional Brun/Selberg upper-bound theorem,
not an extrapolation from that replay.

### PROVED

* The exact neighboring phase map and all boundary conditions.
* The denominator-free square CRT divisibility and zero extra valuation.
* The complete mixed-state CRT solution module for every rank pair.
* The failure of rational transversality to produce a product-field
  determinant or state-coordinate divisor.
* Twin-edge isolation and $o(M)$ endpoint log weight.
* Item 149 de-overlap, unchanged $1/36$ ceiling, and zero booking.

### EXACT FINITE ONLY

* The bounded phase and twin-isolation replays.

### OPEN

* A genuinely cross-prime fixed integer beyond $C_0(M),C_1(M)$ with a
  useful independent valuation.
* Any weighted theorem for isolated full-gate collision primes.
* Any positive $j=1$ capacity reduction or new Route-1 rate.
