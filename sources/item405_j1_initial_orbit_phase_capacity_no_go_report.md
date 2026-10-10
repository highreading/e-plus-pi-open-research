> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 405 — exact initial orbit for the fixed-$j=1$ columns and the bounded-depth capacity no-go

Date: 2026-09-01

## 1. Outcome and capacity decision first

Retain the actual fixed-$j=1$ family



$$
p=4h+6s+3,\qquad M=3h+4s+2,\qquad h,s\geq1,
 \tag{1.1}
$$



and Item 363's joint Hasse--transverse necessary gate



$$
Q_0(h,s)=0,\qquad E_h^*=0\pmod p.                  \tag{1.2}
$$



Here $E_h^*$ is Item 293's phase residual for the selected-Hasse
carrier.  Items 293 and 360 identify its reduction with the selected
Hasse gate up to $p$-units on every actual row.  Item 401 proves that a
fixed prime gives a consecutive same-characteristic column, with motion



$$
(M,h,s,p)\longmapsto(M+1,h+3,s-2,p).                \tag{1.3}
$$



At $D\sim\log M$, Item 395's strict admission target is



$$
\log\mathcal C_{M,D}<\left({1\over12}-\varepsilon\right)M.
 \tag{1.4}
$$



This item evaluates the missing initial Hasse orbit and gives its sharp
capacity consequence.

1. **PROVED — the first three points of every column miss the actual
   joint gate.**  The two possible initial Hasse states are
   

$$
(E_1^*,E_4^*,E_7^*),\qquad(E_2^*,E_5^*,E_8^*).
   \tag{1.5}
$$


   Factoring their six reduced numerators leaves exactly seven
   phase-compatible rows on which the Hasse coordinate can vanish.  Exact
   evaluation of $Q_0$ is nonzero on all seven.  Thus the first
   $\min(3,\lfloor p/12\rfloor)$ points of every fixed-$p$ candidate
   column are absent from the joint selector.

2. **PROVED — the strongest capacity gain from this theorem is zero.**
   At fixed $M$, at most two candidate primes lie in those first three
   column levels.  Their total logarithmic weight is at most
   $2\log U_M=O(\log M)=o(M)$.  The retained fixed-$j=1$ ceiling
   therefore remains $1/36$ per $6M$.

3. **PROVED — exact bounded-depth initials plus recurrence existence still
   saturate (1.4).**  Remove the depth-three primes from the full candidate
   set.  The remaining selector still has logarithmic-window cluster
   radical at least
   

$$
{1\over12}M+o(M)                              \tag{1.6}
$$


   at $D=\lfloor\log M\rfloor$.  For every fixed horizontal slice,
   degree-three interpolation over the independent prime columns matches
   all exact depth-three initial-coordinate values and realizes precisely
   this selector under the one common homogeneous recurrence
   

$$
X_{t+4}-4X_{t+3}+6X_{t+2}-4X_{t+1}+X_t=0.         \tag{1.7}
$$



The interpolation model is not the actual Item 401 operator and is not the
actual orbit.  It closes only the inference from recurrence existence plus
bounded-depth initial data.  An operator-specific theorem for the actual
distinguished orbit or a genuine cross-prime reciprocity law remains live.
No such law is proved here.  Therefore



$$
\boxed{
 \text{new booking}=0,\qquad
 \text{new whole-cell capacity reduction}=0,\qquad
 \text{retained fixed-}j=1\text{ ceiling}=1/36.}
 \tag{1.8}
$$



## 2. Exact beginning of every fixed-prime column

Item 401 gives



$$
I_p=\left[\left\lceil{2p+1\over3}\right\rceil,
            \left\lfloor{3p-3\over4}\right\rfloor\right]\cap\mathbb Z,
 \qquad |I_p|=\left\lfloor{p\over12}\right\rfloor. \tag{2.1}
$$



Write $p=12k+r$, $r\in\{1,5,7,11\}$.  At the lower endpoint of
$I_p$, direct substitution gives



$$
\begin{array}{c|c|c|c}
r&M_{p,0}&h_{p,0}&s_{p,0}\\ \hline
1&8k+1&1&2k-1\\
5&8k+4&2&2k-1\\
7&8k+5&1&2k\\
11&8k+8&2&2k.
\end{array}                                             \tag{2.2}
$$



If $t=M-M_{p,0}$ is the column age, then



$$
h=h_{p,0}+3t,\qquad s=s_{p,0}-2t.                    \tag{2.3}
$$



Thus the first three Hasse indices are exactly



$$
1,4,7\quad(p\equiv1,7\bmod12),\qquad
 2,5,8\quad(p\equiv5,11\bmod12).                    \tag{2.4}
$$



This is the order-three initial state aligned with Item 296's selected-
Hasse recurrence.  No finite sample or guessed recurrence is used in
(2.1)--(2.4).

## 3. Exact Hasse initials and phase-compatible divisors

Item 293 gives the six reduced rational values



$$
\begin{array}{c|r|r}
h&\operatorname{num}(E_h^*)&\operatorname{den}(E_h^*)\\ \hline
1&-104&21\\
4&-7104750016&761805\\
7&-49133396574985216&2147198787\\
2&13744&231\\
5&169877825152&1380483\\
8&5832403476713133056&18259427025.
\end{array}                                             \tag{3.1}
$$



Their numerator factorizations are



$$
\begin{array}{c|l}
h&|\operatorname{num}(E_h^*)|\\ \hline
1&2^3\cdot13\\
4&2^6\cdot7\cdot13\cdot1219909\\
7&2^{10}\cdot13\cdot73\cdot1103\cdot1409\cdot32533\\
2&2^4\cdot859\\
5&2^7\cdot7\cdot53\cdot1033\cdot3463\\
8&2^{10}\cdot11\cdot47\cdot1314127\cdot8383391.
\end{array}                                             \tag{3.2}
$$



Every prime factor of the corresponding denominator is at most $4h+3$.
An actual row prime satisfies $p=4h+6s+3>4h+3$, so the denominator is a
$p$-unit.  Hence $E_h^*=0\pmod p$ forces $p$ to be one of the
numerator primes in (3.2).

Impose the exact phase condition



$$
s={p-4h-3\over6}\in\mathbb Z_{\ge1}.                \tag{3.3}
$$



All numerator factors but the following seven are eliminated:



$$
\begin{array}{r|r|r}
p&h&s\\ \hline
13&1&1\\
1219909&4&203315\\
53&5&5\\
73&7&7\\
32533&7&5417\\
47&8&2\\
8383391&8&1397226.
\end{array}                                             \tag{3.4}
$$



This is an exhaustive divisor reduction, not a prime scan.  For example,
the numerator prime $859$ at $h=2$ is phase-incompatible because
$(859-11)/6\notin\mathbb Z$.

## 4. Exact transverse audit of the seven Hasse-zero rows

Item 218's rational-tail formula gives $Q_0,Q_1\pmod p$, with every
denominator a $p$-unit.  Exact evaluation on (3.4) gives



$$
\begin{array}{r|r|r|r|r}
p&h&s&Q_0&Q_1\\ \hline
13&1&1&9&4\\
1219909&4&203315&833864&86967\\
53&5&5&36&14\\
73&7&7&32&58\\
32533&7&5417&20350&11902\\
47&8&2&30&41\\
8383391&8&1397226&6424621&1596119.
\end{array}                                             \tag{4.1}
$$



In particular, $Q_0\ne0\pmod p$ in every row.  Combining (2.4), the
exhaustive Hasse divisor list (3.4), and (4.1) proves



$$
\boxed{
 0\le t<\min(3,|I_p|)
 \quad\Longrightarrow\quad
 \neg\bigl(Q_0(h_{p,0}+3t,s_{p,0}-2t)
 =E_{h_{p,0}+3t}^*=0\bmod p\bigr).}
 \tag{4.2}
$$



Equation (4.2) is the requested actual initial-orbit arithmetic.  It
strictly strengthens Item 401's statement that the all-zero recurrence
orbit is merely a nonactual countermodel: the actual distinguished orbit
misses the joint gate throughout its complete three-state Hasse initial
window.

It is not a cross-prime reciprocity theorem.  The calculation separates
the columns by exact phase and checks their only possible initial Hasse
divisors.  It supplies no equation containing two residue characteristics.

## 5. Sharp direct capacity gain: at most $2\log U_M$

Let



$$
\mathcal J_M^{(3)}=
 \{p\in\mathcal P_M:0\le M-M_{p,0}<3\}.              \tag{5.1}
$$



At fixed $M$, (2.3) and parity show that the three possible Hasse
indices are



$$
\{1,5,7\}\quad(M\text{ odd}),\qquad
 \{2,4,8\}\quad(M\text{ even}).                     \tag{5.2}
$$



If $M$ is odd, the corresponding possible primes are



$$
A,\quad A-2,\quad A-3,
 \qquad A={3M-1\over2}.                               \tag{5.3}
$$



If $A$ is odd, the last is even; if $A$ is even, the first two are
even.  If $M$ is even, the possible primes are



$$
B-1,\quad B-2,\quad B-4,
 \qquad B={3M\over2}.                                 \tag{5.4}
$$



The same parity argument applies.  Since every candidate prime is greater
than two,



$$
\boxed{|\mathcal J_M^{(3)}|\le2.}                   \tag{5.5}
$$



By (4.2), the actual joint-gate set is contained in
$\mathcal P_M\setminus\mathcal J_M^{(3)}$.  The maximum direct
logarithmic saving relative to the full candidate product is



$$
\sum_{p\in\mathcal J_M^{(3)}}\log p
 \le2\log U_M=O(\log M)=o(M).                        \tag{5.6}
$$



Consequently



$$
\limsup {W_{H\mathscr T}(M)\over6M}\le{1\over36}    \tag{5.7}
$$



with no smaller coefficient proved.  The exact initial theorem removes
real candidate rows, but its strongest possible normalized gain is zero.

## 6. The depth-three-excluded selector still saturates Item 395

Define the abstract selector



$$
\mathcal A_M=\mathcal P_M\setminus\mathcal J_M^{(3)}. \tag{6.1}
$$



The prime number theorem in the tied interval and (5.6) give



$$
\sum_{p\in\mathcal A_M}\log p={M\over6}+o(M).       \tag{6.2}
$$



Let $D\sim c\log M$, $c>1/2$, and let
$\mathcal I_{M,D}(\mathcal A)$ be the members of $\mathcal A_M$
having no second member within numerical distance $2D$.  Distinct
members of this isolated set are more than $2D$ apart in an interval of
length $H_M=(M-9)/6$.  Hence



$$
|\mathcal I_{M,D}(\mathcal A)|
 \le1+\left\lfloor{H_M\over2D}\right\rfloor,        \tag{6.3}
$$



and



$$
\sum_{p\in\mathcal I_{M,D}(\mathcal A)}\log p
 \le {M\over12c}+o(M).                               \tag{6.4}
$$



Subtracting (6.4) from (6.2), the positive-degree vertex radical of
$\mathcal A_M$ satisfies



$$
\boxed{
 \log\mathcal C_{M,D}(\mathcal A)
 \ge\left({1\over6}-{1\over12c}\right)M+o(M)
 ={2c-1\over12c}M+o(M).}                             \tag{6.5}
$$



The coefficient is exactly Item 395's admission coefficient and Item
400's ambient lower coefficient.  At $c=1$,



$$
\boxed{
 \liminf_{M\to\infty}{1\over M}
 \log\mathcal C_{M,\lfloor\log M\rfloor}(\mathcal A)
 \ge{1\over12}.}                                     \tag{6.6}
$$



Thus even a selector which respects the proved depth-three actual initial
exclusion still saturates the strict threshold (1.4).

The same proof applies after deleting any fixed number $B$ of initial
levels: at fixed $M$ this removes at most $B$ candidates and only
$O_B(\log M)$ weight.  Bounded-depth improvements cannot change a
linear coefficient.

## 7. A common bounded-order recurrence matching all exact initials

The preceding support witness can also be placed inside a recurrence
information class without reverting to Item 401's all-zero initial orbit.
Fix a sufficiently large target $M_0$, so every candidate column has at
least three points.  For each $p\in\mathcal P_{M_0}$, let



$$
a_p=M_0-M_{p,0},\qquad0\le a_p<|I_p|<p.             \tag{7.1}
$$



For $t=0,1,2$, let



$$
q_{p,t}=Q_0(h_{p,0}+3t,s_{p,0}-2t),\qquad
 e_{p,t}=E_{h_{p,0}+3t}^*\quad\hbox{in }\mathbb F_p. \tag{7.2}
$$



For $a_p\ge3$, the four nodes $0,1,2,a_p$ are distinct in
$\mathbb F_p$.  There are unique polynomials $q_p(T),e_p(T)$ of
degree at most three satisfying



$$
q_p(t)=q_{p,t},\quad e_p(t)=e_{p,t}\quad(0\le t\le2),
 \qquad q_p(a_p)=e_p(a_p)=0.                          \tag{7.3}
$$



For $a_p<3$, use the degree-at-most-two interpolants through the three
actual initial values.  By (4.2), their values at $a_p$ do not satisfy
the joint gate.

Every polynomial sequence of degree at most three satisfies the same
homogeneous fourth-difference recurrence (1.7), over every
$\mathbb F_p$.  Therefore the columnwise assignments



$$
Q_{0,p}^{\rm model}(M_{p,0}+t)=q_p(t),\qquad
 E_p^{\rm model}(M_{p,0}+t)=e_p(t)                   \tag{7.4}
$$



have all of the following properties:

1. they use one prime-independent homogeneous recurrence of order four;
2. they match every exact $Q_0,E^*$ value in the actual depth-three
   initial orbit;
3. their joint-gate set at $M_0$ is exactly
   $\mathcal P_{M_0}\setminus\mathcal J_{M_0}^{(3)}$; and
4. by (6.6), these horizontal slices saturate the $M/12$ threshold.

This proves the scoped information-class obstruction



$$
\boxed{
 \text{bounded recurrence existence + exact bounded-depth initials}
 \not\Longrightarrow
 \text{a strict fixed-}M\text{ cluster saving}.}      \tag{7.5}
$$



The construction deliberately changes the recurrence operator.  It does
not say that Item 401's actual algebraic operator admits these interpolated
orbits.  Once an explicit actual operator and a complete determining state
are used, the orbit is fixed; proving its horizontal nonconcentration is
precisely the sequence-specific arithmetic still missing.  Equation (7.5)
only prevents recurrence existence, order, rank, and a bounded initial
strip from being counted as mass.

## 8. What remains live

A successful continuation must introduce at least one of the following.

1. **Actual operator-specific orbit arithmetic.**  Use the explicit
   recurrence coefficients and a complete determining state to prove that
   later simultaneous zeros are sparse.
2. **Cross-prime reciprocity.**  Couple the $p$- and $q$-columns when
   $0<|p-q|\le2\log M$.  The phase factorization in Sections 3--4
   contains only one prime at a time.
3. **A subthreshold common carrier.**  Produce an actual-moment integer
   containing the clustered endpoint radical with logarithmic height
   $<(1/12-\varepsilon)M$.
4. **A growing-depth theorem.**  Excluding $B(M)$ initial levels becomes
   capacity-relevant only if its horizontal weighted consequence is
   linear and passes Item 395's coefficient test.  Every fixed $B$ is
   closed by Section 6.

No cross-prime resultant, reciprocity law, or actual cluster upper bound is
claimed in this item.

## 9. Deterministic replay and finite-data policy

The standard-library checker pins canonical Items 218, 293, 360, 363,
391, 395, 398, 400, and the audited canonical Item 401 theorem.  It
verifies:

1. the six exact Hasse initials and both numerator and denominator
   factorizations;
2. the exhaustive phase-compatible divisor list (3.4);
3. the exact $Q_0,Q_1$ residues in (4.1) from the rational-tail formulas;
4. fixed-prime block ages and the depth-three initial indices;
5. on the declared slice $M_0=861$, exact interpolation of every actual
   depth-three $Q_0,E^*$ value, the common fourth-difference recurrence,
   and the resulting model selector and cluster radical; and
6. the exact coefficients $1/12$ and $1/36$.

The seven phase checks are a finite consequence of complete factorizations,
not a bounded prime search.  The declared $M_0=861$ model is an algebraic
control only.  No collision census, unbounded gate scan, operator guess, or
finite-to-infinite inference is performed.

From the archive root run

```powershell
python scripts/item405_j1_initial_orbit_phase_capacity_no_go_certificate.py `
  --output results/item405_j1_initial_orbit_phase_capacity_no_go_certificate_replay.json
```

The replay must be byte-identical to the shipped certificate.

## 10. Strict decision and ledger

### PROVED

- the exact two three-term Hasse initial states of every fixed-prime column;
- the complete phase-compatible Hasse-zero divisor list;
- exact transverse nonvanishing on every row in that list;
- joint-gate exclusion throughout the first three column levels;
- the fixed-$M$ bound of at most two excluded candidate primes;
- the maximal direct saving $2\log U_M=o(M)$;
- threshold saturation after removing the complete depth-three strip;
- the common order-four interpolation countermodel matching all exact
  depth-three coordinate values;
- failure of bounded-order recurrence existence plus bounded-depth exact
  initials to beat Item 395's $M/12$ threshold;
- zero booking and retention of the $1/36$ ceiling.

### DECLARED EXACT CONTROL ONLY

- the $M_0=861$ interpolation and cluster graph;
- no density inference from this control.

### OUTSIDE THE CLOSED CLASS

- the explicit actual Item 401 recurrence operator together with a
  complete determining state;
- sequence-specific congruence or monodromy for that distinguished orbit;
- a cross-prime reciprocity law or subthreshold actual-moment carrier.

### OPEN

- the actual logarithmic-window cluster-radical upper bound;
- $W_{H\mathscr T}(M)=o(M)$ or any strict fixed-$j=1$ retained
  constant;
- any new Route-1 booking and every conclusion about $e+\pi$.



$$
\boxed{
 \text{new proved linear log rate}=0,\quad
 \text{new booked mass}=0,\quad
 \text{new whole-cell capacity reduction}=0.}        \tag{10.1}
$$


