> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 266 — global stable off-ray layers and the weighted-radical barrier

Date: 2026-08-31

## 1. Scope and verdict

This item returns to the rank-one common moving content of Items 211--216.
Write the fixed global row parameter as $M$, and put



$$
2M+1=(j+1)p-s,\qquad j\ge1,\qquad
 k=3s+2<p.                                             \tag{1.1}
$$



For an odd prime $p$, set



$$
q=\begin{cases}1,&p\ge5s+4,\\2,&p<5s+4,\end{cases}
 \qquad b=qp-5s-4,\qquad r\equiv3s+2\pmod4,
 \quad0\le r<4.                                      \tag{1.2}
$$



The stable band is $b\le k+2=3s+4$.  The conclusions are:

> **PROVED — exact stable-row globalization.**  Apart from the fixed primes
> $p<11$, which have zero logarithmic rate, the stable rows are exactly
> the two disjoint interval families
> 

$$
> \begin{array}{ll}
> q=1:&(8j+7)p\ge16M,\quad(5j+4)p\le10M+1,\\[2mm]
> q=2:&(4j+3)p\ge8M,\quad(3j+2)p\le6M.
> \end{array}                                         \tag{1.3}
>
$$


> On every row
> 

$$
> 10M+1-b=(5j+5-q)p,\qquad0\le b<p,\qquad
> b\le{6M\over7}+1.                                  \tag{1.4}
>
$$



> **PROVED — exact raw stable capacity.**  The prime number theorem gives
> total stable-row log weight
> 

$$
> C_{\rm st}M+o(M),\qquad
> C_{\rm st}=\sum_{j\ge1}\left{
> {6\over(5j+4)(8j+7)}+{2\over(3j+2)(4j+3)}\right}
> =0.239111014698\ldots .                             \tag{1.5}
>
$$


> Thus the entire stable candidate for one additional copy has raw ceiling
> $C_{\rm st}/6=0.039851835783\ldots$ per $6M$.

> **PROVED — a decisive far-subcell comparison.**  Already the subcell
> $b\ge M/5$ has exact raw coefficient
> 

$$
> C_{\rm far}={1139587\over9085230}
> =0.125432927950\ldots\quad\hbox{per }M,              \tag{1.6}
>
$$


> or $0.020905487992\ldots$ per $6M$.  This is larger than the
> presently missing
> 

$$
> 0.117797902016590763\ldots\quad\hbox{per }M          \tag{1.7}
>
$$


> by $0.007635025933\ldots$.  Merely deleting slowly growing $b$-layers
> therefore cannot decide the branch.

> **PROVED — exact stable eliminant container and mandatory witness.**  The
> Item 212 rational sums give fixed integers
> $N_{g_1}(b,r),N_{g_0}(b,r)$ such that, outside the classified support
> gap,
> 

$$
> p\mid g_0(s),g_1(s)
> \iff p\mid N_{g_1}(b,r),N_{g_0}(b,r).               \tag{1.8}
>
$$


> The row $(M,s,p,j,q,b,r)=(2249,299,2399,1,1,900,3)$
> is retained, its terminal state is $(7,-7,0,0)$, and
> 

$$
> \gcd(N_{g_1}(900,3),N_{g_0}(900,3))
> =2^{449}\!\prod_{\ell\in L}\ell,                  \tag{1.9}
>
$$


> where
> 

$$
> L=\{911,971,991,1031,1051,1091,1151,1171,1231,1291,2399\}.
>
$$



> **PROVED, SHARPLY SCOPED INFORMATION/HEIGHT BARRIER.**  Multiplying the
> per-layer divisors $10M+1-b$ costs $O(M\log M)$; summing the available
> Item 214 numerator-height bound costs $O(M^2\log M)$.  Neither estimate
> sharpens (1.5).  More strongly, the phase identity, fixed-layer
> integrality, and those inherited height envelopes alone admit a mock
> fixed sequence that saturates every actual row in the far subcell along
> a geometric subsequence.  Its limsup coefficient is (1.6), still above
> (1.7).  This is an obstruction only to those containers.  The mock
> sequence does not satisfy the actual hypergeometric identities, and no
> impossibility theorem is claimed for a new cancellation-aware recurrence
> in $b$, a sharper gcd factorization, or another arithmetic invariant.

> **PROVED — exact Item 149 overlap, and zero booking.**  The first
> post-Cartier rank-one copy at every row in scope is already booked by
> Item 149.  A common factor $p\mid g_0,g_1$ can support only the candidate
> additional first-gate copy; it is not a new prime reservoir, and it gives
> no implication for the $A_1$ digit or a third copy.  No lower bound for
> the common-prime mass and no improved upper bound below the relevant
> threshold is proved.  The new Route-1 rate credit is therefore zero.

## 2. Exact global row map

Equation (1.1) gives



$$
s=(j+1)p-(2M+1).                                    \tag{2.1}
$$



Multiplying (1.1) by five and using $5s=qp-b-4$ gives the exact identity



$$
\boxed{10M+1-b=(5j+5-q)p.}                         \tag{2.2}
$$



Thus the quotient is $5j+4$ in the $q=1$ phase and $5j+3$ in the
$q=2$ phase.  In particular $p\mid10M+1-b$.  Also $b\ge0$, and
$b<p$: this is immediate for $q=1$, while for $q=2$ it follows from
$p<5s+4$.

For $q=1$, the phase inequality and stability become



$$
(5j+4)p\le10M+1,\qquad (8j+7)p\ge16M.              \tag{2.3}
$$



For $q=2$, stability and rank one become



$$
(4j+3)p\ge8M,\qquad (3j+2)p\le6M.                 \tag{2.4}
$$



Conversely, for $p\ge11$, (2.3) implies $s\ge0$, the $q=1$ phase,
rank one, and stability; (2.4) implies the same statements in the $q=2$
phase.  Indeed, the lower inequality in (2.3) gives
$8(j+1)p\ge16M+p\ge16M+8$, while its upper inequality gives


$$
5(3j+2)p=3(5j+4)p-2p\le30M+3-2p\le30M.
$$


For (2.4), its lower inequality gives
$4(j+1)p\ge8M+p\ge8M+4$, and


$$
4(5j+4)p=5(4j+3)p+p\ge40M+p>40M+4,
$$


which is the strict $q=2$ phase inequality.  Stability is algebraically
equivalent to the corresponding lower inequality, and rank one is the upper
inequality in (2.4).  The primes $3,5,7$ are a fixed finite set and have
zero asymptotic log weight.  This proves (1.3).

Finally, in the $q=1$ family,



$$
b=10M+1-(5j+4)p\le{6M\over8j+7}+1\le{2M\over5}+1, \tag{2.5}
$$



and in the $q=2$ family,



$$
b=10M+1-(5j+3)p\le{6M\over4j+3}+1\le{6M\over7}+1. \tag{2.6}
$$



This proves the last bound in (1.4).  The deterministic replay verifies the
forward and inverse maps on a declared bounded range, but the proof above is
all-parameter.

## 3. Raw stable and far capacities

For fixed $j$, (1.3) gives the asymptotic intervals



$$
{16\over8j+7}\le{p\over M}\le{10\over5j+4}\quad(q=1),
 \qquad
 {8\over4j+3}\le{p\over M}\le{6\over3j+2}\quad(q=2). \tag{3.1}
$$



Their lengths are



$$
{10\over5j+4}-{16\over8j+7}
 ={6\over(5j+4)(8j+7)},                              \tag{3.2}
$$





$$
{6\over3j+2}-{8\over4j+3}
 ={2\over(3j+2)(4j+3)}.                              \tag{3.3}
$$



The intervals sit inside the disjoint rank-one $j$-bands.  Applying the
prime number theorem to finitely many bands and then using the convergent
$O(j^{-2})$ tail proves (1.5).  If the sum is stopped at $J$, its tail is
strictly less than



$$
{19\over60J},                                       \tag{3.4}
$$



because the two summands are bounded by
$3/(20j^2)$ and $1/(6j^2)$.

Now impose $b\ge M/5$.  By (2.2), this adds



$$
{p\over M}\le {49\over5(5j+4)}\quad(q=1),\qquad
 {p\over M}\le {49\over5(5j+3)}\quad(q=2).          \tag{3.5}
$$



Only $j=1,2$ survive in the first phase and only $j=1,\ldots,6$ in the
second.  The nonzero interval lengths are exactly



$$
\begin{array}{c|cc}
j&q=1&q=2\\ \hline
1&1/45&2/35\\
2&1/230&1/44\\
3&0&1/90\\
4&0&11/2185\\
5&0&1/460\\
6&0&1/1485.
\end{array}                                          \tag{3.6}
$$



Their sum is (1.6).  Numerically,



$$
C_{\rm far}-0.117797902016590763\ldots
 =0.007635025933\ldots>0.                            \tag{3.7}
$$



Thus even a genuinely far, finite-$j$ portion retains enough raw capacity
to exceed the current gap.  This is a comparison of ceilings, not a claim
that common zeros have that mass.

## 4. Stable eliminants and unit audit

For $a\in\{0,1\}$, put



$$
E_a=2s+a,\qquad B_a=b+1-a,\qquad
 t={3s+2-r\over4}.                                   \tag{4.1}
$$



Item 212's exact coefficient normalization is



$$
D_a=(-1)^{t+r}{E_a\choose t}\Phi_a(s,b,r),          \tag{4.2}
$$





$$
\Phi_a(s,b,r)=
 \sum_{h=0}^{H_a}(-1)^h{B_a\choose r+4h}
 {t^{\underline h}\over(E_a-t+1)_h},
 \quad
 H_a=\min\!\left(t,\left\lfloor{B_a-r\over4}\right\rfloor\right).
                                                               \tag{4.3}
$$



Here $D_0=g_1$ and $D_1=g_0$ modulo $p$.  On an actual summation
range,



$$
0\le t\le E_a<p,\qquad
 1\le E_a-t+u\le E_a<p\quad(1\le u\le h).           \tag{4.4}
$$



Thus the binomial base and every displayed denominator are $p$-units.
Stability gives



$$
H_a=\left\lfloor{B_a-r\over4}\right\rfloor,        \tag{4.5}
$$



so the cutoff depends only on $(b,r)$.  Since



$$
5s\equiv-(b+4)\pmod p,                              \tag{4.6}
$$



substitute $S_b=-(b+4)/5$ into (4.3), reduce the resulting fraction, and
call its numerator $N_a(b,r)$.  For $p>5$, the reduced denominator is a
unit because it is congruent, up to powers of $2$ and $5$, to the actual
unit denominator product.  This proves (1.8), with the support gaps handled
as in Item 212.

At $(b,r)=(900,3)$, exact rational reconstruction and exact division give
(1.9).  The phase congruence requires $p\equiv19\pmod{20}$; the ten factors
from $911$ through $1291$ are $11\pmod{20}$, while $2399\equiv19$.
The latter gives $s=(2399-900-4)/5=299$, and direct recurrence yields



$$
(A_{896},A_{897},A_{898},A_{899})=(7,-7,0,0)\pmod{2399}. \tag{4.7}
$$



This is a genuine cancellation root, not a support gap.

## 5. The exact global container and why its available bounds fail

Let $G_{b,r}$ be the gcd of the two reduced eliminant numerators, with the
convention $G_{b,r}=0$ at a simultaneous support gap.  If
$R_M^{\rm st}$ is the squarefree product of stable
off-ray common-content primes, then (1.4) and (1.8) give the exact container



$$
R_M^{\rm st}\mid
 \operatorname {rad}\!\prod_{0\le b\le6M/7+1}
 \gcd\!\left(10M+1-b,\prod_{r=0}^3G_{b,r}\right).    \tag{5.1}
$$



No denominator prime is hidden in (5.1), by (4.4)--(4.6).

If one discards the eliminant and multiplies only the layer factors, then



$$
\sum_{b\le6M/7+1}\log(10M+1-b)=O(M\log M).          \tag{5.2}
$$



This does not improve the linear raw support (1.5).  Conversely, Item 214's
proved bound



$$
\log|N_a(b,r)|\le
 \log(b+2)+(b+1)\log2+{b+2\over2}\log(10(b+3))       \tag{5.3}
$$



sums to $O(M^2\log M)$ over (5.1).  The within-summand recurrence of Item
214 and the first-order Gosper obstruction of Item 216 supply no proved
cross-$b$ product bound.  Therefore these particular containers do not
produce an $o(M)$ theorem or even a ceiling below (1.7).

This conclusion is deliberately method-scoped.  Equations (5.2)--(5.3) are
upper estimates, not lower bounds on every possible resultant.

## 6. A precise information countermodel for those estimates

The weakness of (5.2)--(5.3) can be made exact without pretending to model
the hypergeometric sequence.  Take $M_n=5^n$, with $n$ sufficiently
large.  The blocks



$$
I_n=\left[\left\lceil{M_n\over5}\right\rceil,
            \left\lfloor{6M_n\over7}+1\right\rfloor\right]     \tag{6.1}
$$



are disjoint, because the next lower endpoint is $M_n$, larger than the
previous upper endpoint.

For $b\in I_n$, define a mock fixed integer $\widetilde G_{b,r}$ to be
the product of all actual stable phase primes at global row $M_n$ having
that $(b,r)$; put it equal to one outside these blocks.  Distinct primes
at fixed $(M_n,b)$ all divide $10M_n+1-b$, hence



$$
\widetilde G_{b,r}\le10M_n+1\le50b+1.              \tag{6.2}
$$



Set both mock numerator sequences equal to $\widetilde G_{b,r}$.  Thus the
mock sequences are fixed as $M$ varies, respect the phase-layer
divisibility, and lie far below the inherited height envelope (5.3).  Yet
at every selected $M_n$ it marks every actual row with $b\ge M_n/5$ as
a common row.  The prime number theorem along this subsequence gives limsup
coefficient $C_{\rm far}$, which exceeds (1.7).

Therefore no inference using only the phase identity, fixed-layer
integrality, and (5.3) can force a smaller coefficient.  The construction is
not an actual common-content counterexample: it does not satisfy (4.3), the
common-term recurrence, or any future cross-$b$ invariant.  Those are the
precise open sources of additional information.

## 7. Item 149 overlap and the master admission test

Every row here lies in the $\kappa=1$ rank-one cell.  Item 149 already
books its first post-Cartier copy.  Items 196 and 205 identify
$p\mid g_0,g_1$ with common moving content and hence with simultaneous
vanishing of the two first gates $A_0,B_0$.  Accordingly:

1. **Actual-family implication:** (1.8) is exact on actual stable rows.
2. **De-overlap:** only one additional first-gate copy could be credited;
   the already booked Item 149 copy cannot be counted again.
3. **No third-copy implication:** common content does not force $A_1=0$.
4. **Quantitative admission:** no lower bound for the common radical is
   proved, and the best upper ceiling remains above the relevant gap.

The stable eliminant therefore supplies no new positive rate and does not
close Route 1 negatively.  Both directions remain open.

## 8. Deterministic replay and status

The standard-library checker

```text
scripts/item266_far_offray_weighted_barrier_certificate.py
```

performs the following tasks:

* independently reconstructs the stable rational sums and the complete
  $b=900$ gcd factorization;
* independently recomputes the terminal state and the row identity at
  $(2249,299,2399,1,900)$;
* verifies the exact forward/inverse global row map on a declared bounded
  range;
* verifies (1.5) with an explicit rational tail enclosure and verifies every
  rational term in (3.6);
* verifies the block and inherited-height inequalities used in Section 6.

The bounded map replay is **EXACT FINITE ONLY**.  It is not a common-zero
scan and supports no asymptotic inference.

### PROVED

* Exact all-parameter globalization (1.3)--(1.4), with fixed small primes
  separated.
* Raw stable coefficient (1.5) and exact far coefficient (1.6).
* Stable eliminant equivalence, denominator-unit audit, and mandatory
  $2399$ witness.
* Exact global container (5.1).
* Scoped information/height barrier for (5.2)--(5.3).
* Exact Item 149 overlap and zero new booking.

### EXACT FINITE ONLY

* The declared bounded row-bijection replay and exact arithmetic witness
  recomputation.

### OPEN

* An all-$b$ factorization or phase-feasible prime-localization theorem.
* A cancellation-aware cross-$b$ recurrence or low-height resultant.
* An $o(M)$ or sufficiently small explicit weighted upper bound.
* A positive weighted lower bound for the candidate extra copy.
* Any improvement of the Route-1 exponent.
