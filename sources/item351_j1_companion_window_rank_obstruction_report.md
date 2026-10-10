> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 351 — all-window Hasse–Taylor rank and the scoped companion-transfer no-go for fixed $j=1$

Date: 2026-09-01

## 1. Outcome and capacity first

Retain the actual tied family



$$
n=2h,\qquad r=2s+1,\qquad
p=2n+3r,\qquad 2M=3n+4r,                                \tag{1.1}
$$



and the selected integral carrier



$$
a_{r,n}=[u^n]G(u)^{-r},\qquad
G(u)=1-4u+6u^2-4u^3.                                    \tag{1.2}
$$



Items 339, 342, and 348 give the exact one-way chain



$$
\boxed{
\text{ordinary fixed-}j=1\text{ collision}
\Longrightarrow p\mid a_{r,n}
\Longleftrightarrow H_{r,n,p}(1)=0.}                     \tag{1.3}
$$



The first arrow is not reversed.  In particular, a selected-coordinate
zero used below is not silently promoted to a full original collision.

This item asks whether the existing selected zero, together with its
exact Hasse, Frobenius, or contiguous transfers, automatically supplies
a second independent condition.

The answer is a rigorously scoped **no**:

1. for every $0\leq w\leq J=\deg H<p$, the first $w+1$
   Hasse–Taylor coordinates at $z=1$ have rank $w+1$;
2. $H(1)=0$ kills only the zeroth coordinate;
3. a derivative companion vanishes only when the actual root at $1$
   has extra multiplicity, which is an additional arithmetic condition;
4. the sub-$p$ Frobenius transfer copies the entire coefficient window
   exactly and therefore adds no equation; and
5. the contiguous coefficient transfer lies in one nonsingular
   order-three local state module, so a transfer identity changes
   coordinates but does not manufacture another zero condition.

Equivalently, the module of conditions *formally forced by the one
selected equation* remains rank one.  The ambient companion-coordinate
space can have larger rank; those independent coordinates are precisely
why their vanishing is not implied.

The actual predeclared selected-zero row



$$
(h,s,p)=(8,2,47),\qquad (n,r)=(16,5),                    \tag{1.4}
$$



has a simple Hasse root:



$$
H(1)=0,\qquad H^{[1]}(1)=16\ne0\pmod{47}.                \tag{1.5}
$$



Moreover every declared $n$-shift from $-6$ through $6$, and
every declared $r$-shift from $-4$ through $4$, is nonzero except
the central selected coordinate.  This is an exact counterexample to
the most natural universal companion implications, not a density
sample and not a full-collision example.

There is also a capacity obstruction for using a neighboring *actual*
fixed-$M$ row.  Such rows satisfy



$$
(h,s,p)\longmapsto(h+4q,s-3q,p-2q).                     \tag{1.6}
$$



For every fixed nonzero $q$, simultaneous primality of $p$ and
$p-2q$ has logarithmic mass $O(M/\log M)=o(M)$ by the
two-linear-form upper-bound sieve.  A bounded collection of such
neighbors is therefore zero-rate and cannot control isolated rows.

No actual-family codimension-two gate and no weighted-density theorem
is proved.  Hence



$$
\boxed{
\text{new independent forced condition}=0,\quad
\text{new linear log rate}=0,\quad
\text{new fixed-}j=1\text{ capacity reduction}=0.}       \tag{1.7}
$$



The retained fixed-$j=1$ ceiling remains $1/36$ per $6M$.
Route 1 remains ACTIVE.

## 2. The all-window Hasse–Taylor theorem

Write the actual Item 348 polynomial as



$$
H(z)=\sum_{k=0}^{J}c_kz^k\in\mathbb F_p[z],
\qquad J<p.                                              \tag{2.1}
$$



For $0\leq m\leq J$, define the Hasse derivative coordinate



$$
D_m(H)=H^{[m]}(1)
=\sum_{k=m}^{J}{k\choose m}c_k.                          \tag{2.2}
$$



Taylor's formula is exact in every characteristic:



$$
\boxed{
H(z)=\sum_{m=0}^{J}D_m(H)(z-1)^m.}                       \tag{2.3}
$$



For a window $0\leq m\leq w$, take the columns
$0\leq k\leq w$ of the coordinate matrix in (2.2).  The resulting
Pascal minor is



$$
\mathcal P_w=\left({k\choose m}\right)_{0\leq m,k\leq w}.
                                                                    \tag{2.4}
$$



It is upper triangular with diagonal entries $1$, so



$$
\boxed{\det\mathcal P_w=1,\qquad
\operatorname{rank}(D_0,\ldots,D_w)=w+1.}                \tag{2.5}
$$



This is the requested all-window rank theorem.  It applies uniformly
for every actual Hasse degree and does not rely on a finite scan.

The selected gate is only



$$
D_0(H)=H(1)=0.                                           \tag{2.6}
$$



For $w\geq1$, the additional equations



$$
D_1(H)=\cdots=D_w(H)=0                                   \tag{2.7}
$$



are equivalent to



$$
(z-1)^{w+1}\mid H(z).                                    \tag{2.8}
$$



Thus the natural derivative/resultant companion is a genuine
multiple-root condition, of codimension $w+1$ in coefficient space.
It is not a second copy of (2.6), and the old gate contains no statement
that forces it.

For $w=1$, the local resultant statement is especially transparent:



$$
H(1)=H^{[1]}(1)=0
\Longleftrightarrow (z-1)^2\mid H(z).                    \tag{2.9}
$$



The exact row (1.4)--(1.5) shows that even this first multiplicity
condition fails for an actual selected-factor zero.

## 3. The rank-one forced-condition lemma

Let $V=\mathbb F_p^{J+1}$ be the coefficient space and let
$E_0(c)=\sum_k c_k$.  A linear companion $L\in V^\ast$ is
formally forced to vanish by the selected equation exactly when



$$
\ker E_0\subseteq\ker L.                                 \tag{3.1}
$$



Elementary duality gives



$$
(\ker E_0)^\perp=\langle E_0\rangle,                     \tag{3.2}
$$



and hence



$$
\boxed{
\ker E_0\subseteq\ker L
\Longleftrightarrow L=\lambda E_0
\text{ for some }\lambda\in\mathbb F_p.}                 \tag{3.3}
$$



This yields the exact dichotomy for every finite linear companion
window:

- if its row is proportional to $E_0$, it is a duplicate and adds
  no codimension;
- if its row is independent of $E_0$, its vanishing is not implied
  by the selected equation.

The Hasse–Taylor theorem proves that all nonzero derivative rows fall
in the second case.  More general rationally weighted term moments obey
the same dichotomy whenever their weights are regular on the terminating
support.

Equation (3.3) is deliberately a theorem about what follows from the
existing linear gate and transfer identities alone.  The actual
hypergeometric coefficient vectors occupy a special arithmetic subset
of $V$.  A new theorem showing that this subset meets
$\ker E_0$ only inside some second hyperplane would be substantive
new arithmetic input; (3.3) does not rule it out.  No such identity is
present in Items 342, 345, or 348.

## 4. Frobenius copies the whole sub-$p$ window

In $\mathbb F_p[[u]]$,



$$
G(u)^{p-r}=G(u)^pG(u)^{-r}
=G(u^p)G(u)^{-r}.                                       \tag{4.1}
$$



Since $G(u^p)=1+O(u^p)$, one has the exact all-window identity



$$
\boxed{
[u^m]G(u)^{p-r}=a_{r,m}
\quad(0\leq m<p).}                                      \tag{4.2}
$$



Item 342 uses the coordinate $m=n$.  Equation (4.2) shows that
passing to neighboring sub-$p$ Frobenius coefficients does not add
a relation: it simply copies the neighboring reciprocal coefficients.
In particular,



$$
a_{r,n}=0
\quad\not\Longrightarrow\quad
a_{r,n+j}=0                                              \tag{4.3}
$$



by Frobenius transfer alone.

The exact control (1.4) makes (4.3) concrete for every declared
$-6\leq j\leq6$, $j\ne0$.  The logical theorem, however, is
the identity (4.2); the finite row is used only to refute proposed
universal small-shift implications.

## 5. The exact contiguous state and the three-zero theorem

Put



$$
A_r(u)=G(u)^{-r}=\sum_{m\geq0}a_{r,m}u^m.                \tag{5.1}
$$



Differentiating $G^rA_r=1$ gives



$$
GA_r'=-rG'A_r.                                           \tag{5.2}
$$



Taking the coefficient of $u^{m-1}$ yields



$$
\boxed{
\begin{aligned}
m\,a_{r,m}
={}&4(m+r-1)a_{r,m-1}\\
&-6(m+2r-2)a_{r,m-2}\\
&+4(m+3r-3)a_{r,m-3}.
\end{aligned}}                                           \tag{5.3}
$$



Thus the local state



$$
S_m=(a_{r,m},a_{r,m-1},a_{r,m-2})^{\mathsf T}            \tag{5.4}
$$



has transfer



$$
S_{m+1}=
\begin{pmatrix}
{4(m+r)\over m+1}&{-6(m+2r-1)\over m+1}
                 &{4(m+3r-2)\over m+1}\\
1&0&0\\
0&1&0
\end{pmatrix}S_m.                                        \tag{5.5}
$$



Its determinant is



$$
\det T_m={4(m+3r-2)\over m+1}.                           \tag{5.6}
$$



For



$$
0\leq m\leq2n+1,                                        \tag{5.7}
$$



both numerator and denominator in (5.6) are nonzero modulo
$p=2n+3r$.  Therefore the transfer is invertible throughout the
entire target-centered local range.

There is an exact actual-sequence consequence:

> **Three-zero theorem.** No three consecutive coefficients
> $a_{r,q},a_{r,q+1},a_{r,q+2}$ with $q+2\leq2n+2$
> can all vanish modulo $p$.

For $q=0$ this is immediate from $a_{r,0}=1$.  If $q\geq1$,
the three ending at $t=q+2$ vanish, and (5.3) gives



$$
4(t+3r-3)a_{r,t-3}=0.                                   \tag{5.8}
$$



The coefficient is a unit because



$$
1\leq t+3r-3\leq2n+3r-1=p-1.                            \tag{5.9}
$$



Repeating backwards forces $a_{r,0}=0$, contradicting
$a_{r,0}=1$.

For a target-centered window of width $Y(M)=o(M)$, the condition
$Y<n+2$ fails only on the edge $n=o(M)$, which Item 339 already
proved has weighted mass $o(M)$.  Hence every sublinear local
coefficient window on the positive-rate bulk lies in the nonsingular
three-state transfer module.

This does not mean that the actual initial-value orbit is an arbitrary
three-state solution.  Its initial values select one special orbit.
The point is narrower: the local transfer itself supplies no extra zero
equation.  Any congruence special to that orbit requires a new global
evaluation, nonconcentration theorem, or factor localization.

## 6. Contiguous shifts in $r$

The exact exponent shift is



$$
A_{r-q}(u)=G(u)^qA_r(u)\qquad(q\geq0).                   \tag{6.1}
$$



For $q=1$,



$$
a_{r-1,n}
=a_{r,n}-4a_{r,n-1}+6a_{r,n-2}-4a_{r,n-3}.              \tag{6.2}
$$



More generally, every bounded downward $r$-shift is a finite linear
functional of the neighboring $n$-coefficients.  Using (5.3), it
lies in the same local three-state module away from the zero-rate
endpoints.

Equation (6.2) plainly does not turn $a_{r,n}=0$ into
$a_{r-1,n}=0$; it retains three other coordinates.  In the declared
actual row, all shifts $r-4,\ldots,r+4$ except $r$ itself are
nonzero modulo $47$.  Again this refutes the elementary universal
companion proposal but is not an asymptotic statement.

A parameter derivative introduces $-\log G\cdot G^{-r}$, hence a
new global convolution rather than a zero forced by (1.3).  No
parameter-derivative gate is booked without a theorem connecting that
convolution to the full original collision.

## 7. Neighboring actual rows have zero-rate bounded-tuple reach

At fixed $M=3h+4s+2$, every other integral row is



$$
h'=h+4q,\qquad s'=s-3q.                                  \tag{7.1}
$$



Its candidate prime is



$$
p'=4h'+6s'+3=p-2q.                                      \tag{7.2}
$$



For fixed $q\ne0$, requiring both the original row and its companion
to be prime asks for two distinct affine linear forms to be prime.
The standard upper-bound sieve gives



$$
\#\{\,\text{such paired rows}\,\}
=O_q\!\left({M\over(\log M)^2}\right).                   \tag{7.3}
$$



Since each prime has logarithm $O(\log M)$, their total logarithmic
weight is



$$
O_q\!\left({M\over\log M}\right)=o(M).                   \tag{7.4}
$$



The same conclusion holds for any bounded collection of fixed offsets.
Thus an argument which first asks for a neighboring actual prime and
then transfers a condition can address only a zero-rate paired subset.
It cannot exclude isolated rows and receives no fixed-$j=1$ capacity
credit.

For a growing collection of offsets, a union bound gives zero rate only
within the corresponding sieve range; no claim is made that every
arbitrary $o(M)$-sized collection of prime offsets is zero-rate.

## 8. The declared exact control

For $(h,s,p)=(8,2,47)$, Item 348 gives



$$
H(z)=1+4z+43z^2+23z^3+23z^4.                            \tag{8.1}
$$



Its full Hasse–Taylor vector at $1$ is



$$
\bigl(D_0,D_1,D_2,D_3,D_4\bigr)
=(0,16,15,21,23)\pmod{47}.                               \tag{8.2}
$$



In particular, $z=1$ is a simple root.  The declared coefficient
windows are



$$
\begin{array}{c|rrrrrrrrrrrrr}
j&-6&-5&-4&-3&-2&-1&0&1&2&3&4&5&6\\ \hline
a_{5,16+j}
&2&9&9&15&39&21&0&20&8&29&12&35&3
\end{array}                                               \tag{8.3}
$$



and



$$
\begin{array}{c|rrrrrrrrr}
q&-4&-3&-2&-1&0&1&2&3&4\\ \hline
a_{5+q,16}
&15&33&14&43&0&33&33&1&2.
\end{array}                                               \tag{8.4}
$$



The certificate also verifies (4.2) and (5.3) on this declared window.
No other prime is searched.

## 9. Scoped decision and missing input

### PROVED

- the all-window Hasse–Taylor/Pascal rank theorem (2.5);
- the exact higher-multiplicity criterion (2.8);
- the rank-one forced-condition lemma (3.3);
- the full sub-$p$ Frobenius coefficient-window identity (4.2);
- the exact order-three local recurrence and invertible target transfer;
- the three-consecutive-zero theorem;
- containment of sublinear target windows in the same local module
  outside zero-rate endpoints;
- zero-rate capacity of bounded neighboring actual-prime tuples;
- the scoped no-go for obtaining a second condition from the existing
  selected equation and these transfer identities alone;
- zero booking.

### EXACT FINITE ONLY

- the single predeclared $p=47$ selected-zero row;
- its simple Hasse root and its displayed $n$- and $r$-windows;
- seven symbolic Pascal-minor replays;
- no prime scan, density extrapolation, or full-collision claim.

### OPEN

- a second condition forced by information in the *full original
  collision* but absent from the selected-coordinate gate;
- a theorem that actual full-collision rows have multiple Hasse roots;
- weighted zero density for any genuine codimension-two carrier;
- global arithmetic of the exact initial-value orbit in (5.3);
- $W_b(M)=o(M)$, any strict fixed-$j=1$ ceiling reduction,
  Route 1, and every conclusion about $e+\pi$.

The theoretical maximum reach of a genuine forced codimension-two
condition would be the entire retained fixed-$j=1$ ceiling,
$1/36$ per $6M$.  No such forced condition was found, so this
maximum is not booked.

## 10. Ledger consequence and self-audit



$$
\begin{array}{c|c}
\text{quantity}&\text{Item 351 value}\\ \hline
\text{new forced independent condition}&0\\
\text{new proved linear log rate}&0\\
\text{new fixed-}j=1\text{ capacity reduction}&0\\
\text{bounded actual-neighbor mass}&o(M)\\
\text{retained fixed-}j=1\text{ ceiling per }6M&1/36
\end{array}                                               \tag{10.1}
$$



The self-audit explicitly records:

1. (1.3) is used only in its proved direction;
2. the $p=47$ row is a selected-factor zero, not a claimed original
   collision;
3. ambient companion rank is not confused with actual-orbit
   nonvanishing;
4. paired-prime zero-rate mass is not credited against isolated rows;
5. no geometric $F$-crystal, density theorem, or ledger gain is
   asserted.
