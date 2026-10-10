> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 348 — the actual first-Hasse polynomial and the trivial terminating Dwork-dash tower for fixed $j=1$

Date: 2026-09-01

## 1. Outcome and capacity first

Keep the actual fixed-$j=1$ row



$$
n=2h,\qquad r=2s+1,\qquad
 p=2n+3r=4h+6s+3,\qquad
 2M=3n+4r.                                                \tag{1.1}
$$



Items 339 and 342 reduced the factor selected by the ordinary collision
to



$$
a_{r,n}=[u^n]G(u)^{-r},\qquad
 G(u)=1-4u+6u^2-4u^3,                                    \tag{1.2}
$$



and proved the one-way gate



$$
\boxed{\text{ordinary fixed-}j=1\text{ collision}
 \Longrightarrow p\mid a_{r,n}.}                         \tag{1.3}
$$



The converse in (1.3) is not asserted.  The selected-factor condition
itself is equivalent to $p\mid a_{r,n}$, but a zero of the selected
factor need not reconstruct the full original collision.

Item 342 gave an exact four-Kummer realization at the chosen prime, while
Item 345 proved that ordinary Galois descent does not lower its global
height.  This item takes the genuinely $p$-adic next step.  It builds
the *actual first-Hasse truncation polynomial* on both carry charts and
applies Dwork's dash to its terminating parameter.

Let $\ell(r,n)$ be the exact number of $p$-unit terms from Item 339.
Outside the already closed forced-zero ray, there is a polynomial
$H_{r,n,p}(z)\in\mathbb F_p[z]$ such that



$$
\boxed{
 p\mid a_{r,n}\Longleftrightarrow H_{r,n,p}(1)=0,\qquad
 \deg H_{r,n,p}=\ell(r,n)-1.}                            \tag{1.4}
$$



It is a normalized terminating ${}_4F_3$ on the left chart
$r\leq n$, and a forward-shifted terminating ${}_5F_4$
tail on the right chart $r>n$.

On either chart the term ratio contains a top parameter $-J$, where



$$
J=\deg H_{r,n,p}<p.                                     \tag{1.5}
$$



For the standard Dwork dash



$$
\mathfrak D_p(x)={x+\lambda_p(x)\over p},\qquad
 0\leq\lambda_p(x)<p,\quad x+\lambda_p(x)\in p\mathbb Z_p, \tag{1.6}
$$



one has



$$
\boxed{\mathfrak D_p(-J)=0.}                            \tag{1.7}
$$



Thus the formal hypergeometric dash tower of the actual terminating
chart is trivial after its first step: the dashed coefficient sequence
has top parameter $0$, hence all positive-index coefficients vanish.
There is no second nontrivial native Hasse factor waiting higher in this
dash tower.

The capacity consequence is negative but global.  Item 339 proved that
fixed-$M$ rows with $\ell(r,n)=o(M)$ have logarithmic prime mass
$o(M)$.  By (1.4), exactly the same is true of rows with
$\deg H_{r,n,p}=o(M)$.  Therefore:



$$
\boxed{
 \begin{gathered}
 \text{bounded- or sublinear-degree use of the native first-Hasse}\\
 \text{criterion reaches only zero-rate fixed-}j=1\text{ support};\\
 \text{any positive-rate use must control linearly growing }H.
 \end{gathered}}                                         \tag{1.8}
$$



This closes the natural bounded-degree first-Hasse and higher-dash
subroutes.  It does **not** prove that no different geometric
$F$-crystal exists, nor that an unknown global identity cannot produce
a bounded-degree divisor.  Such a new identity is precisely additional
input not furnished by the actual terminating dash tower.

No weighted nonconcentration theorem is obtained.  Hence



$$
\boxed{
 \text{new linear log rate}=0,\qquad
 \text{new fixed-}j=1\text{ ceiling reduction}=0.}       \tag{1.9}
$$



The retained ceiling is $1/36$ per $6M$, and $W_b(M)=o(M)$
remains open.

## 2. The exact tied prefix and its one-way gate

Item 339 proved



$$
a_{r,n}=
 \sum_{k=0}^{K}
 {r+k-1\choose k}{4r+n-1\choose n-4k},
 \qquad K=\left\lfloor{n\over4}\right\rfloor.            \tag{2.1}
$$



Write



$$
T_k={r+k-1\choose k}{4r+n-1\choose n-4k},\qquad
 \delta=n-4K\in\{0,2\},\qquad d=r-n-1.                  \tag{2.2}
$$



Every actual $p$ is odd.  The integral rescaling in Item 339 gives



$$
p\mid\operatorname{num}(b_h)
 \Longleftrightarrow p\mid a_{r,n}.                      \tag{2.3}
$$



Combining (1.3) and (2.3), all conclusions below retain the correct
logical direction:



$$
\text{ordinary collision}\Longrightarrow
 \text{selected-factor zero}\Longleftrightarrow
 \text{first-Hasse value zero}.                          \tag{2.4}
$$



Nothing below promotes the last condition back to a full original
collision.

## 3. Left chart: the actual terminating ${}_4F_3$

Assume $r\leq n$.  Then $4r+n-1<p$, so every $T_k$ in
(2.1) is a $p$-unit.  In particular,



$$
T_0={4r+n-1\choose n}\not\equiv0\pmod p.                \tag{3.1}
$$



Define



$$
H_L(z)=\sum_{k=0}^{K}{T_k\over T_0}z^k
 \in\mathbb F_p[z].                                      \tag{3.2}
$$



The exact ratio is



$$
{T_{k+1}\over T_k}
 =
 {\prod_{q=0}^{3}\left(k+{q-n\over4}\right)
  \over
  (k+1)(k+r+\tfrac14)(k+r+\tfrac12)(k+r+\tfrac34)}.      \tag{3.3}
$$



Consequently



$$
H_L(z)=
 {}_4F_3\!\left(
 \begin{matrix}
 -n/4,\ (1-n)/4,\ (2-n)/4,\ (3-n)/4\\
 r+1/4,\ r+1/2,\ r+3/4
 \end{matrix};z\right),                                  \tag{3.4}
$$



with the series terminating at $K$.  Indeed the numerator parameter
with index $q=\delta$ is



$$
{\delta-n\over4}=-K.                                    \tag{3.5}
$$



Every coefficient in (3.2) is nonzero, so



$$
\deg H_L=K=\ell(r,n)-1.                                 \tag{3.6}
$$



Finally,



$$
a_{r,n}\equiv T_0H_L(1)\pmod p,                         \tag{3.7}
$$



and the prefactor $T_0$ is a unit.  Thus (1.4) holds on
the left chart.

This is the direct $p$-integral form of the same chosen-prime value
isolated by Item 342's four Kummer sums.  It is not an additional
independent condition: it is an exact repackaging of the selected
coefficient.

## 4. Right chart: the exact forward-shifted Hasse tail

Assume $r>n$.  Since



$$
4r+n-1=p+d,\qquad d=r-n-1,                              \tag{4.1}
$$



Lucas's theorem gives



$$
{4r+n-1\choose n-4k}
 \equiv {d\choose n-4k}\pmod p.                          \tag{4.2}
$$



The unique all-term forced-zero case is



$$
d=0,\qquad\delta=2
 \quad\Longleftrightarrow\quad h=s\text{ odd}.           \tag{4.3}
$$



It has at most one row at fixed $M$, hence weighted mass
$O(\log M)=o(M)$; it is kept separate below.

Outside (4.3), put



$$
J=\min\!\left(K,\left\lfloor{d-\delta\over4}\right\rfloor\right).
                                                                    \tag{4.4}
$$



The first surviving original index is



$$
k_0=K-J.                                                   \tag{4.5}
$$



Keep the original forward order $k=k_0+i$, and define



$$
V_i={r+k_0+i-1\choose k_0+i}{d\choose n-4(k_0+i)},
 \qquad
 H_R(z)=\sum_{i=0}^{J}V_iz^i.                            \tag{4.6}
$$



Every $V_i$ in (4.6) is a $p$-unit.  Equation (4.2) gives



$$
a_{r,n}\equiv H_R(1)\pmod p,\qquad
 \deg H_R=J=\ell(r,n)-1.                                 \tag{4.7}
$$



Modulo $p$, its exact term ratio is the left ${}_4F_3$ ratio
shifted by $k_0$.  Equivalently,



$$
{H_R(z)\over V_0}
 =
 {}_5F_4\!\left(
 \begin{matrix}
 1,\ k_0-n/4,\ k_0+(1-n)/4,\ k_0+(2-n)/4,\ k_0+(3-n)/4\\
 k_0+1,\ r+k_0+1/4,\ r+k_0+1/2,\ r+k_0+3/4
 \end{matrix};z\right).                                  \tag{4.8}
$$



The numerator parameter in (4.8) with $q=\delta$ is



$$
k_0+{\delta-n\over4}=k_0-K=-J.                          \tag{4.9}
$$



Thus the shifted ${}_5F_4$ terminates exactly at $J$.  This
forward presentation is important for the dash calculation: all four
displayed bottom parameters are positive $p$-integral rationals.
In particular, none has first Dwork dash $0$.  Reversing the tail
would introduce a negative-integral bottom parameter and obscure this
fact with a formal $0/0$; no such reversal is used here.

This proves (1.4)--(1.5) on the right chart without importing the
unselected parity factor or an abstract state.

## 5. What Dwork's dash does—and does not do

For $0\leq J<p$, the least residue required in (1.6) for $x=-J$
is $\lambda_p(-J)=J$.  Therefore



$$
\mathfrak D_p(-J)={-J+J\over p}=0.                      \tag{5.1}
$$



On the left chart all three bottom parameters are positive nonintegral
$p$-integral rationals.  On the right chart, Section 4 gives the
positive bottom parameters



$$
k_0+1,\quad r+k_0+\tfrac14,\quad
r+k_0+\tfrac12,\quad r+k_0+\tfrac34.                    \tag{5.2}
$$



Their first dashes are nonzero: a dash can be $0$ only when the
original parameter is a nonpositive integer.  Thus no dashed bottom
parameter creates a $0/0$.

A generalized hypergeometric coefficient sequence with a top parameter
$0$ and nonzero positive dashed bottom parameters is



$$
c_0=1,\qquad c_m=0\quad(m\geq1),                        \tag{5.3}
$$



because $(0)_m=0$.  All later dashes of that top parameter remain
$0$.  Hence the formal Dwork-dash tower attached to the actual
terminating chart has only one nontrivial Hasse layer: the first
polynomial $H_L$ or $H_R$.

The scope is important.  This proves a statement about the explicit
terminating hypergeometric coefficient system in Sections 3--4.  It
does not:

1. construct a smooth geometric family whose unit root equals
   $a_{r,n}$;
2. identify the four Kummer sums with a bounded-rank geometric
   $F$-crystal;
3. prove ordinary or unit-root nonvanishing at $z=1$; or
4. rule out a new geometric realization carrying additional structure.

Accordingly, the phrase “trivial dash tower” is not a universal no-go
for $p$-adic cohomology.  It is the exact obstruction for the native
terminating chart produced by the selected factor itself.

## 6. Degree and fixed-$M$ capacity

Define the selected-factor envelope



$$
W_b(M)=
 \sum_{\substack{h,s\geq1,\ M=3h+4s+2\\
                  p=4h+6s+3\ {\rm prime}\\
                  p\mid\operatorname{num}(b_h)}}\log p. \tag{6.1}
$$



The desired theorem remains



$$
W_b(M)=o(M).                                            \tag{6.2}
$$



The full raw fixed-$j=1$ candidate mass is $M/6+o(M)$, whose
ledger ceiling is $1/36$ per $6M$.  The forced ray (4.3) has only
$O(\log M)$ mass.

Away from that ray, Sections 3--4 prove the identity



$$
\deg H_{r,n,p}=\ell(r,n)-1.                             \tag{6.3}
$$



Item 339's weighted short-interval theorem proves that any fixed-$M$
support on which



$$
\ell(r,n)=o(M)                                          \tag{6.4}
$$



has logarithmic prime mass $o(M)$.  Equations (6.3)--(6.4) yield:

> **Native first-Hasse degree theorem.** Rows on which
> $\deg H_{r,n,p}=o(M)$ have weighted prime mass $o(M)$.
> Hence no positive-rate support can be confined to bounded or
> sublinear native first-Hasse degree.  Any positive-rate mechanism
> based on this criterion must treat rows of degree $\gg M$ along
> a positive-mass subfamily.

Thus an “ordinary bounded-degree Hasse divisor” does not emerge from
the exact chart or its dash tower.  Producing one would require a new
global factorization or geometric identity proving that the selected
zero set is contained in a bounded-degree divisor.  Degree growth alone
does not prove that no such unknown identity exists, so that possibility
is left OPEN.

The dash calculation adds a second obstruction: after the first
linearly growing Hasse polynomial, there is no nontrivial later
polynomial in the native formal dash tower that could supply an
independent bounded-degree condition.

Neither obstruction proves (6.2), so no capacity is booked.

## 7. Five exact controls

The deterministic certificate replays five rows fixed in Item 339.
It performs no prime census.

| $(h,s,p)$ | chart | coefficients of $H$ in $\mathbb F_p$ | $\deg H$ | $H(1)$ | $a_{r,n}\bmod p$ |
|---|---|---|---:|---:|---:|
| $(1,1,13)$ | forced ray | empty | -- | $0$ | $0$ |
| $(2,1,17)$ | left | $1,4$ | $1$ | $5$ | $8$ |
| $(8,2,47)$ | left | $1,4,43,23,23$ | $4$ | $0$ | $0$ |
| $(4,4,43)$ | right | $2$ | $0$ | $2$ | $2$ |
| $(2,6,47)$ | right | $23,13$ | $1$ | $36$ | $36$ |

For the left row $(2,1,17)$, the unit prefactor is $T_0=5$,
so $a_{r,n}\equiv5H(1)\equiv8\pmod{17}$.  The row
$(8,2,47)$ remains the exact all-unit cancellation witness.
It is not a density statement and not a full original collision.

## 8. Scoped decision

### PROVED

- the exact left normalized terminating ${}_4F_3$;
- the exact right surviving-tail Hasse polynomial;
- $p\mid a_{r,n}\Longleftrightarrow H_{r,n,p}(1)=0$
  outside the separately classified forced ray;
- $\deg H_{r,n,p}=\ell(r,n)-1$;
- the presence of the actual terminating top parameter
  $-\deg H$;
- one-step trivialization of the formal Dwork dash tower;
- zero-rate weighted support of bounded or sublinear native
  first-Hasse degree;
- the scoped bounded-degree/native-higher-dash no-go;
- zero ledger booking.

### EXACT FINITE ONLY

- the five preselected controls in Section 7;
- no scan, density extrapolation, or universal nonvanishing claim.

### OPEN

- a $p$-adic nonconcentration theorem for
  $H_{r,n,p}(1)$ on its linearly growing-degree bulk;
- a global monodromy, average-gcd, or factor-localization theorem for
  the complete first-Hasse polynomial;
- a new geometric $F$-crystal with structure not present in the
  formal terminating dash tower;
- any new identity forcing selected zeros into a bounded-degree divisor;
- $W_b(M)=o(M)$, any strict fixed-$j=1$ ceiling reduction,
  Route 1, and every conclusion about $e+\pi$.

## 9. Ledger consequence



$$
\begin{array}{c|c}
\text{quantity}&\text{Item 348 value}\\ \hline
\text{new independent condition}&0\\
\text{new proved linear log rate}&0\\
\text{new fixed-}j=1\text{ capacity reduction}&0\\
\text{sublinear native Hasse-degree mass}&o(M)\\
\text{native higher-dash factors after the first}&\text{trivial}\\
\text{retained fixed-}j=1\text{ ceiling per }6M&1/36
\end{array}                                               \tag{9.1}
$$



The missing input has now been localized sharply: it must control the
single, linearly growing first-Hasse value globally.  Repeating the
native dash does not create another condition, and restricting to
bounded-degree Hasse charts can reach only zero-rate edges.
