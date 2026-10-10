> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 401 — algebraic cross-$M$ transport and the vertical-column no-go for fixed $j=1$

Date: 2026-09-01

## 1. Outcome and capacity decision first

Retain the actual fixed-$j=1$ family



$$
p=4h+6s+3,\qquad M=3h+4s+2,\qquad h,s\geq1,
 \tag{1.1}
$$



and Item 363's joint Hasse--transverse necessary gate.  At the
logarithmic window $D\sim\log M$, Items 395 and 400 show that a useful
new theorem must prove



$$
\log \mathcal C_{M,D}<(1/12-\varepsilon)M
 \tag{1.2}
$$



for some fixed $\varepsilon>0$, or otherwise lower the retained
$1/36$ ceiling per $6M$.  This admission threshold is applied before
the recurrence construction.

This item proves two exact cross-$M$ statements and one sharply scoped
no-go.

1. **PROVED -- each fixed prime gives a long same-characteristic
   column.**  A prime $p>3$ is an actual candidate for exactly
   $\lfloor p/12\rfloor$ consecutive values of $M$.  Consecutive
   points obey
   

$$
(M,h,s,p)\longmapsto(M+1,h+3,s-2,p).             \tag{1.3}
$$


   Thus cross-$M$ transport really does remain in one field
   $\mathbb F_p$, unlike fixed-$M$ transport between neighboring
   primes.

2. **PROVED -- the two original transverse coordinates have bounded
   algebraic cross-$M$ complexity.**  Item 197's integers
   $C_0(M),C_1(M)$ have algebraic ordinary generating functions.  An
   exact degree-twelve residue presentation gives an algebraic degree at
   most
   

$$
\binom{12}{4}=495.                               \tag{1.4}
$$


   Consequently each sequence satisfies a nonzero polynomial-coefficient
   recurrence whose order and coefficient degrees are absolute constants,
   independent of $p$.  On every fixed-$p$ candidate column, division
   by the compulsory first copy of $p$ transports the actual divided
   coordinates modulo the *same* prime.  Item 296 already supplies an
   exact order-three same-characteristic recurrence for the selected
   Hasse carrier.  Hence both sides of the Item 363 gate have genuine
   finite-rank vertical transport.

3. **PROVED -- homogeneous vertical transport alone cannot beat (1.2).**
   The columns for distinct primes are independent CRT components.  Every
   homogeneous recurrence admits the zero output orbit.  Taking the two
   divided original coordinates to be zero on every prime column is
   compatible with every such recurrence, and it lies in the full-gate
   branch of Item 363, hence also in the joint Hasse--transverse gate.
   It realizes the full candidate set at each fixed $M$.  Item 400 proves
   that this countermodel has logarithmic-window cluster mass at least
   $M/12+o(M)$, exactly saturating the admission coefficient.

The last statement is an information-class no-go, not a theorem about the
actual initial orbit.  An explicit arithmetic evaluation of the actual
initial state, a reciprocity law between two different prime columns, or a
common cross-prime carrier may still distinguish the actual selector.  The
mere existence, order, regularity, or finite rank of the same-prime
recurrences does not.

Therefore



$$
\boxed{
 \text{new booking}=0,\qquad
 \text{new whole-cell capacity reduction}=0,\qquad
 \text{retained fixed-}j=1\text{ ceiling}=1/36.}
 \tag{1.5}
$$



## 2. Exact fixed-prime candidate columns

Eliminating $h,s$ from (1.1) gives



$$
h=3M-2p,\qquad s={3p-4M-1\over2}.                     \tag{2.1}
$$



For every odd $p$, the second expression is integral.  The inequalities
$h,s\geq1$ are equivalent to



$$
\left\lceil{2p+1\over3}\right\rceil
 \leq M\leq
 \left\lfloor{3p-3\over4}\right\rfloor.              \tag{2.2}
$$



Call this interval $I_p$.  If $p>3$ is prime, write
$p=12k+r$ with $r\in\{1,5,7,11\}$.  Direct substitution in (2.2)
gives respectively



$$
\begin{array}{c|c}
r&I_p\\ \hline
1 &[8k+1,9k]\\
5 &[8k+4,9k+3]\\
7 &[8k+5,9k+4]\\
11&[8k+8,9k+7].
\end{array}                                               \tag{2.3}
$$



Thus



$$
\boxed{|I_p|=k=\lfloor p/12\rfloor.}                  \tag{2.4}
$$



Increasing $M$ by one in (2.1) gives (1.3).  In particular, the shift
preserves $p$, preserves $h\bmod3$, and moves through one consecutive
same-characteristic column until it reaches the boundary $s=1$.

This is the correct cross-$M$ direction.  It differs from the fixed-$M$
motion



$$
(h,s,p)\longmapsto(h-4,s+3,p+2),                       \tag{2.5}
$$



which changes the residue characteristic.

## 3. One fixed rational map generates both integer coordinates

For $\nu=0,1$, retain Item 197's exact integers



$$
C_\nu(M)=[z^{4M+\nu}]
 { (1-z)^{6M}(1+z)^{1+3\nu}
  \over(1+z^2)^{4M+1+\nu}}.                            \tag{3.1}
$$



Define



$$
K(z)={(1-z)^6\over z^4(1+z^2)^4},\qquad
 w_\nu(z)={(1+z)^{1+3\nu}
       \over z^\nu(1+z^2)^{1+\nu}}.                   \tag{3.2}
$$



Then coefficient extraction is the exact constant-term identity



$$
\boxed{C_\nu(M)=\operatorname {CT}_z w_\nu(z)K(z)^M.}
 \tag{3.3}
$$



Therefore the ordinary generating function is



$$
\mathcal G_\nu(t)=\sum_{M\geq0}C_\nu(M)t^M
 =\operatorname {CT}_z{w_\nu(z)\over1-tK(z)}.          \tag{3.4}
$$



Put



$$
\Delta(z,t)=z^4(1+z^2)^4-t(1-z)^6                    \tag{3.5}
$$



and



$$
N_\nu(z)=z^{3-\nu}(1+z)^{1+3\nu}(1+z^2)^{3-\nu}.
 \tag{3.6}
$$



After multiplying (3.4) by $dz/z$, the integrand becomes exactly



$$
{w_\nu(z)\over1-tK(z)}{dz\over z}
 ={N_\nu(z)\over\Delta(z,t)},dz.                     \tag{3.7}
$$



No asymptotic expansion or modular reduction occurs in (3.3)--(3.7).

## 4. Exact algebraicity and bounded recurrence rank

The polynomial $\Delta$ has degree twelve in $z$.  For small nonzero
$t$, precisely four of its roots tend to zero, because its Newton edge
at zero is $z^4-t$.  Denote these four roots by
$z_1(t),\ldots,z_4(t)$.  Residue extraction in (3.7) gives



$$
\boxed{
 \mathcal G_\nu(t)
 =\sum_{i=1}^{4}{N_\nu(z_i(t))
          \over\partial_z\Delta(z_i(t),t)}.}           \tag{4.1}
$$



This immediately proves algebraicity, but it is useful to record a
quantitative annihilator.  Over the splitting field, let



$$
\rho_{\nu,i}={N_\nu(z_i)\over\partial_z\Delta(z_i,t)}
 \qquad(1\leq i\leq12),                                \tag{4.2}
$$



where now all twelve roots are included, and define



$$
\mathscr A_\nu(t,Y)=
 \prod_{\substack{S\subseteq\{1,\ldots,12\}\\|S|=4}}
 \left(Y-\sum_{i\in S}\rho_{\nu,i}\right).          \tag{4.3}
$$



The expression (4.3) is invariant under every permutation of the roots.
Its coefficients are therefore rational functions of the elementary
symmetric functions of the roots and hence belong to $\mathbb Q(t)$.
Equation (4.1) selects one of its factors, so



$$
\boxed{
 \mathscr A_\nu(t,\mathcal G_\nu(t))=0,\qquad
 \deg_Y\mathscr A_\nu\leq\binom{12}{4}=495.}          \tag{4.4}
$$



Repeated roots occur only on the discriminant locus and do not affect the
identity in $\mathbb Q(t)$; one may prove (4.4) first over the generic
splitting field and then clear denominators.

In characteristic zero, the derivatives of an algebraic function stay in
its finite function field.  Hence $1,\mathcal G_\nu,\mathcal G_\nu',\ldots$
are linearly dependent over $\mathbb Q(t)$.  Clearing denominators and
comparing Taylor coefficients yields



$$
\boxed{
 \sum_{j=0}^{r_\nu}A_{\nu,j}(M)C_\nu(M+j)=0}           \tag{4.5}
$$



for some fixed $r_\nu$ and nonzero
$A_{\nu,j}\in\mathbb Z[M]$, outside only the finite initial/singular
set inherent in the chosen forward form.  Both $r_\nu$ and all
coefficient degrees are absolute constants: they do not depend on $M$
or on the selected prime $p$.

Equation (4.5) is an existence theorem, not a guessed finite recurrence.
It follows from the explicit algebraic annihilator (4.3).  No prime scan
or finite holdout promotion is used.

## 5. Exact transport of the divided gate on $I_p$

For every $M\in I_p$, the rank-zero construction gives



$$
p\mid C_0(M),C_1(M).                                   \tag{5.1}
$$



Define the divided coordinates



$$
U_{\nu,p}(M)={C_\nu(M)\over p}\pmod p.               \tag{5.2}
$$



Item 363's exact bridge is



$$
\boxed{U_{\nu,p}(M)\equiv6Q_\nu(h,s)\pmod p.}        \tag{5.3}
$$



Take any recurrence window in (4.5) wholly contained in $I_p$.  Every
term is divisible by the same prime $p$.  Dividing the integral identity
by $p$ and reducing gives the exact same-characteristic transport



$$
\boxed{
 \sum_{j=0}^{r_\nu}A_{\nu,j}(M)
 U_{\nu,p}(M+j)=0\quad\hbox{in }\mathbb F_p.}          \tag{5.4}
$$



Thus the transverse condition is not merely a fixed-$M$ CRT residue: it
belongs to a bounded-rank vertical recurrence along a column of length
$p/12+O(1)$.

The selected Hasse side has an independent exact transport already sealed
in Item 296.  In its notation,



$$
\sum_{k=0}^{3}Q_k(h)E_{h+3k}^*=0.                     \tag{5.5}
$$



On a fixed prime column, the four terms in (5.5) correspond exactly to



$$
(M+k,h+3k,s-2k,p),\qquad0\leq k\leq3.                \tag{5.6}
$$



Item 296 gives the complete coefficient-singularity atlas and proves
invertible three-state transport off the stated core loci.  Equations
(5.4)--(5.6) therefore establish finite-rank vertical transport for both
the transverse and selected-Hasse coordinates.  The new content of this
item is the exact algebraic construction (3.4)--(4.5) for the original
two divided coordinates and its alignment with the same fixed-$p$
motion.

## 6. Why this does not control a fixed-$M$ logarithmic cluster

At one fixed $M$, a cluster contains distinct primes 

$$
p,q\in\mathcal
P_M
$$

.  Their vertical transports live in different fields:



$$
\mathbb F_p\quad\hbox{and}\quad\mathbb F_q.           \tag{6.1}
$$



No equation in (5.4) or (5.5) contains both columns.  Over their product
modulus, the complete recurrence-state space decomposes as



$$
\mathscr V_{p,q}=\mathscr V_p\times\mathscr V_q.      \tag{6.2}
$$



More generally, for any fixed-$M$ candidate set $S$, CRT gives the
direct product $\prod_{p\in S}\mathscr V_p$.  This is the same
orthogonal-idempotent obstruction encountered for fixed-window gate
planes, now in the vertical direction.

There is an especially sharp countermodel.  Every recurrence under
discussion is homogeneous, so on every prime column one may take



$$
U_{0,p}(M')=U_{1,p}(M')=0\qquad(M'\in I_p).           \tag{6.3}
$$



The output orbit (6.3) satisfies every recurrence coefficient, including
all singular steps.  It need not make an ambient state zero: one may
adjoin any unit coordinate invisible to the two homogeneous output
recurrences.  By (5.3), (6.3) is the full original gate
$Q_0=Q_1=0$.  Item 363's exact syzygy then forces the selected Hasse
condition as well.  Hence (6.3) realizes



$$
\mathcal Z_M^{\rm model}=\mathcal P_M                 \tag{6.4}
$$



for every fixed $M$, while respecting all homogeneous same-prime
recurrence equations and their finite-rank descriptions.

For $D\sim c\log M$, Item 400 proves



$$
\liminf {1\over M}\log\mathcal C^{\rm model}_{M,D}
 \geq {2c-1\over12c}.                                  \tag{6.5}
$$



At $c=1$, this is $1/12$, exactly the coefficient that (1.2) must
strictly beat.  Thus bounded order, fixed rank, ordinary recurrence
regularity, and same-characteristic propagation do not pass the admission
test.

The countermodel is deliberately not asserted to be the actual
$C_\nu(M)$ orbit.  The actual initial values select one distinguished
solution of (4.5).  A theorem exploiting those values could still prove
nonconcentration.  What is closed is the inference



$$
\text{``bounded cross-}M\text{ recurrence''}
 \Longrightarrow
 \text{``subthreshold fixed-}M\text{ cluster radical''.} \tag{6.6}
$$



## 7. Height and carrier audit

The recurrence theorem does not create a new small external integer.  The
existing direct coefficient height is Item 197's



$$
\log|C_\nu(M)|\leq H M+o(M),\qquad
 H=6.327627545440858\ldots.                             \tag{7.1}
$$



Removing the compulsory candidate product saves only
$M/6+o(M)$.  When the coefficient is nonzero, the resulting direct
normalized height has upper coefficient $H-1/6$, vastly larger than the
required $1/12$; if the coefficient is zero, this height route supplies
no bound at that index.
A fixed Casoratian or bounded product of adjacent recurrence values has,
without a new cancellation theorem, only the sum of these height bounds.
The recurrence identity itself supplies no such cancellation.

Likewise, multiplying a same-prime constraint along $I_p$ repeats the
same prime column; it does not create a distinct-prime carrier for a
fixed-$M$ cluster.  Multiplying over distinct columns returns to the CRT
product and the old endpoint radical.

Accordingly no new integer of height $<(1/12-\varepsilon)M$ containing
$\mathcal C_{M,\lfloor\log M\rfloor}$ is proved, and no mass can be
booked.

## 8. Minimal live input after this closure

A successful cross-$M$ continuation must use more than the recurrence
operator.  At least one of the following is necessary.

1. **Actual initial-orbit arithmetic.**  Prove that the distinguished
   solution selected by the exact initial coefficients avoids the
   codimension-two gate often enough; the zero-orbit countermodel must be
   excluded quantitatively, not just declared nonactual.
2. **Cross-prime reciprocity.**  Produce an identity coupling the
   $p$-column to the $q$-column for $0<|p-q|\leq2\log M$.  A
   same-prime recurrence never supplies such a map.
3. **A common external carrier.**  Construct from the actual moments an
   integer whose candidate part contains the clustered endpoint radical
   and whose height is strictly below $M/12$ at $c=1$.
4. **A horizontal distribution theorem.**  Prove nonconcentration for the
   actual recurrence initial states as the residue characteristic varies.
   Ordinary finite-rank state counting inside one $\mathbb F_p$ is
   vertical and is insufficient.

These targets retain the logical connection to the original gate and pass
the capacity screen in principle.  Merely writing smaller recurrence
tables, resolving more coefficient singularities, or verifying longer
finite holdouts does not.

## 9. Deterministic replay and finite-data policy

The standard-library certificate pins Items 296, 363, 395, and 400 and
checks:

1. the exact fixed-prime interval (2.2), its length (2.4), and every
   consecutive phase shift on declared structural primes;
2. the constant-term formula (3.3) by two independent coefficient
   constructions on declared small $M$ values;
3. the exact numerator identity (3.7), the degree-twelve denominator, and
   the fourfold zero at $t=0$;
4. the combinatorial algebraic-degree bound $\binom{12}{4}=495$;
5. the direct-product zero-output recurrence countermodel and the exact
   admission coefficient $1/12$.

The controls contain no actual gate-zero scan, collision census, guessed
operator promotion, or finite-to-infinite inference.  Algebraicity and the
no-go are proved in Sections 4 and 6.

From the archive root run

```powershell
python scripts/item401_j1_crossM_algebraic_transport_no_go_certificate.py `
  --output results/item401_j1_crossM_algebraic_transport_no_go_certificate_replay.json
```

The replay must be byte-identical to the shipped certificate.

## 10. Strict decision and ledger

### PROVED

- the exact fixed-prime candidate block and its $M\mapsto M+1$ phase;
- the common rational-map constant-term representation of $C_0,C_1$;
- the degree-twelve residue formula and algebraic-degree bound at most 495;
- existence of absolute bounded-order polynomial recurrences for both
  original coordinates;
- exact same-characteristic transport after division by the compulsory
  first prime copy;
- alignment with Item 296's selected-Hasse transport;
- the direct-product vertical-column and zero-output-orbit no-go;
- failure of recurrence existence/rank/regularity alone to beat the sharp
  Item 395--400 admission coefficient;
- zero booking and retention of the $1/36$ ceiling.

### DECLARED STRUCTURAL CONTROLS ONLY

- fixed-prime phase blocks and small constant-term identities;
- no actual gate scan, recurrence guess, or density extrapolation.

### OUTSIDE THE CLOSED CLASS

- arithmetic evaluation of the distinguished initial orbit;
- a reciprocity law between different prime columns;
- a subthreshold actual-moment carrier;
- a horizontal distribution theorem for the initial states.

### OPEN

- the actual logarithmic-window cluster-radical bound;
- $W(M)=o(M)$ or any strict fixed-$j=1$ retained constant;
- any new Route-1 booking and every conclusion about $e+\pi$.



$$
\boxed{
 \text{new proved linear log rate}=0,\quad
 \text{new booked mass}=0,\quad
 \text{new whole-cell capacity reduction}=0.}
 \tag{10.1}
$$


