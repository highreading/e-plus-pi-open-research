> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 222 — an all-$h$ phase resultant for the $j=1$ common-log cell

Date: 2026-08-31

## 1. Scope and verdict

Item 218 reduced every admissible $j=1$ row to



$$
p=6s+4h+3,\qquad h,s\geq1,\qquad 3\nmid h,                 \tag{1.1}
$$



and proved that a simultaneous zero of the two original coordinates must
annihilate a rational eliminant $E_h(s)$.  Its fixed-$h$ resultants
exclude $h\leq8$, but their construction grows with $h$.

This item gives a single exact specialization valid for every
$h\geq1$, $3\nmid h$.

**PROVED — all-$h$ phase localization.**  The phase equation in (1.1)
allows $s$ to be replaced modulo $p$ by



$$
s_*=-{4h+3\over6}.                                      \tag{1.2}
$$



At (1.2), the eliminant has an explicit integer numerator $A_h$,
depending only on $h$, and every simultaneous zero necessarily satisfies



$$
\boxed{p\mid A_h}.                \tag{1.3}
$$



All clearing factors are audited as $p$-units for every actual row.
Thus (1.3) is an all-prime theorem, not a scan or a fixed-line
interpolation.

**PROVED — a scoped recurrence obstruction.**  Neither residue subsequence
$E^*_{3n+1}$ nor $E^*_{3n+2}$ obeys a polynomial-coefficient recurrence
of order at most 8 and coefficient degree at most 8.  Two nonzero
$81\times81$ determinants give exact finite-field certificates.  This
rules out that bounded ansatz only; recurrences of larger order or degree
remain open.

**PROVED — exact diagonal reduction.**  On $s=h$, $p=10h+3$, the
eliminant obstruction is equivalent, subject only to one explicitly stated
unit, to a $p^2$-coefficient supercongruence.  This exposes why the
integer eliminant can have systematic false positives without proving a
collision of the original coordinate pair.

**FINITE.**  For all 77 diagonal primes $p\leq2000$, the eliminant
vanishes exactly on the 40 rows with odd $h$, while neither original
coordinate ever vanishes.  This parity pattern is not extrapolated.

**OPEN.**  No all-prime proof of the apparent odd-diagonal
supercongruence, no uniform nonvanishing theorem for the original
coordinates, and no weighted exceptional-prime bound for unbounded $h$
is obtained.  The actual Route-1 rate gain is therefore zero.

## 2. The Item 218 eliminant and its phase

Let



$$
K_0=(1-z)^{2h}(1+z),\qquad
 K_1=(1-z)^{2h}(1+z)^4.                              \tag{2.1}
$$



For an integer polynomial $K=\sum K_nz^n$, write



$$
\operatorname{Odd}(K;a,q)
 =\sum_{t\geq0}(-1)^t{(a+1)_t\over(q+a+2)_t}K_{2t+1},            \tag{2.2}
$$




$$
\operatorname{Even}(K;a,q)
 =\sum_{t\geq0}(-1)^t{(a)_t\over(q+a+1)_t}K_{2t}.               \tag{2.3}
$$



The sums terminate at $\deg K$.  Item 218 defines



$$
\begin{aligned}
x&=\operatorname{Odd}(K_0;s,2s),&
y&=\operatorname{Odd}(K_0;h,2s),\\
u&=\operatorname{Even}(K_1;s,2s-1),&
v&=\operatorname{Odd}(K_1;h,2s-1),
\end{aligned}                                                   \tag{2.4}
$$



and proves the necessary condition



$$
E_h(s)={2s+h+1\over2s}xv+{3(3s+1)\over2s}uy=0\pmod p.          \tag{2.5}
$$



From (1.1),



$$
6s\equiv-(4h+3)\pmod p.                    \tag{2.6}
$$



Every denominator in (2.2)--(2.5) is a $p$-unit on an actual row, as
proved in Item 218.  Therefore rational evaluation respects (2.6): the
reduction of $E_h(s)$ equals that of $E_h(s_*)$.  Denote the latter by
$E_h^*$.

At $s=s_*$, retain the letters $x,y,u,v$ for the four specialized
sums.  Direct substitution in (2.5) gives



$$
\boxed{E_h^*={h\over4h+3}xv
       +{9(4h+1)\over2(4h+3)}uy.}                  \tag{2.7}
$$



## 3. Integer clearing uniform in $h$

The four successive hypergeometric ratios at the phase are



$$
{6i+3-4h\over3(2i+1-4h)},\qquad
 {3(h+1+i)\over3i+3-h},                            \tag{3.1}
$$



for $x,y$, respectively, and



$$
{6i-4h-3\over3(2i-4h-3)},\qquad
 {3(h+1+i)\over3i-h},                              \tag{3.2}
$$



for $u,v$, respectively.  Define



$$
\begin{aligned}
D_x&=3^h\prod_{i=0}^{h-1}(2i+1-4h),&
D_y&=\prod_{i=0}^{h-1}(3i+3-h),\\
D_u&=3^{h+2}\prod_{i=0}^{h+1}(2i-4h-3),&
D_v&=\prod_{i=0}^{h}(3i-h),                         \tag{3.3}
\end{aligned}
$$



and



$$
X=D_xx,\quad Y=D_yy,\quad
                    U=D_uu,\quad V=D_vv.            \tag{3.4}
$$



Every summand denominator in (3.1)--(3.2) divides the corresponding
product in (3.3).  Hence $X,Y,U,V\in\mathbb Z$.  Now set



$$
\boxed{A_h=2hXV D_uD_y+9(4h+1)UY D_xD_v.}          \tag{3.5}
$$



Equations (2.7) and (3.3)--(3.5) give the exact rational identity



$$
E_h^*={A_h\over2(4h+3)D_xD_yD_uD_v}.              \tag{3.6}
$$



This is an identity over $\mathbb Q$ for every $h\geq1$ with
$3\nmid h$; no finite computation is used in its proof.

## 4. Complete denominator and unit audit

Let $(h,s,p)$ be an actual row.  The factors of $D_x$ lie between
$1-4h$ and $-2h-1$, and those of $D_u$ lie between
$-4h-3$ and $-2h-1$.  Their absolute values are at most $4h+3<p$.
The factors of $D_y,D_v$ have absolute value at most $2h<p$.

A zero factor in either $D_y$ or $D_v$ would force $3\mid h$.
But then (1.1) makes $p>3$ divisible by 3, contradicting primality.
The factors $D_x,D_u$ are visibly nonzero.  Finally,
$2,3,4h+3$ are $p$-units because $p=6s+4h+3>4h+3$.

Thus the denominator in (3.6) is a $p$-unit on every actual row.
Combining (2.5)--(2.7) with (3.6) proves (1.3).

The checker evaluates (2.2)--(2.7) exactly over $\mathbb Q$ for all
54 values $1\leq h\leq80$, $3\nmid h$, and independently verifies
that (3.3)--(3.6) hold term by term.  This is a replay check of the symbolic
derivation, not the logical basis for the all-$h$ theorem.

## 5. Height ledger and its exact limitation

Put



$$
M_h=(h+3)2^{2h+4}(21h)^{h+2}.                    \tag{5.1}
$$



The coefficient $\ell^1$-norms of $K_0,K_1$ are at most
$2^{2h+1},2^{2h+4}$, respectively.  There are at most $h+3$ terms
in each sum.  After applying the clearing products, every linear factor
appearing in a numerator or an unused denominator factor has absolute
value at most $21h$.  Consequently each of



$$
|X|,|Y|,|U|,|V|,|D_x|,|D_y|,|D_u|,|D_v|
$$



is at most $M_h$.  Equation (3.5) therefore yields the explicit bound



$$
|A_h|\leq47hM_h^4,         \tag{5.2}
$$



and in particular, whenever $A_h\ne0$,



$$
\log|A_h|=O(h\log h).      \tag{5.3}
$$



Even if all relevant $A_h$ are nonzero, this height is too large for the
required global sum.  Summing the individual bound (5.3) over the $O(m)$
possible moving values of $h$ is superlinear in $m$, so (1.3) alone
gives no $o(m)$ common-prime log-mass bound.  If some $A_h$ vanishes
identically as an integer, the individual-height method is weaker still.
Independently, the strip
$h=o(m/\log m)$ contains only $o(m/\log m)$ rows, each of log weight
$O(\log m)$, and hence has zero linear rate.  This is a scoped no-go for
the individual-height method, not an obstruction to a collective gcd or
primitive-divisor argument.

## 6. A bounded recurrence no-go

The factors in (3.3) are nonzero precisely on the two residue classes
$h\equiv1,2\pmod3$.  Split the rational sequence accordingly.  For
$c\in\{1,2\}$, consider the ansatz



$$
\sum_{k=0}^{r}P_k(n)E^*_{3(n+k)+c}=0,
 \qquad r\leq8,\quad \deg P_k\leq8,                \tag{6.1}
$$



with $P_k\in\mathbb Q[n]$.  It suffices to test the maximal 81
coefficients.  Over $\mathbb F_{1000000007}$, form the square matrix



$$
\mathcal M_c(n;(k,d))=n^dE^*_{3(n+k)+c},
 \quad 0\leq n\leq80,\quad0\leq k,d\leq8.         \tag{6.2}
$$



Exact Gaussian elimination gives



$$
\det\mathcal M_1=501978340\ne0,
 \qquad
 \det\mathcal M_2=365649200\ne0                  \tag{6.3}
$$



modulo 1000000007.  All phase denominators used in these rows are nonzero
modulo that prime.  If a rational identity (6.1) existed, clearing its
coefficient denominators and dividing by the coefficient gcd would give a
primitive integer null vector.  Its reduction modulo 1000000007 would be
nonzero and would contradict (6.3).  Lower order or degree embeds in the
same matrix by zero padding.  Thus (6.3) proves the declared no-go.

This statement says nothing about order or degree above 8, rational
coefficients depending on additional parameters, or non-polynomial
recurrences.  Those branches remain open.

## 7. The exact diagonal mechanism

Take



$$
s=h,\qquad p=10h+3.      \tag{7.1}
$$



Then $s_*\equiv h\pmod p$, $x=y$, and the factorial prefactors of
Item 218 satisfy $A=B$.  Hence the first original coordinate and the
eliminant simplify to



$$
Q_0=Ax,\qquad
 E_h(h)={3h+1\over2h}x(v+3u).                      \tag{7.2}
$$



All displayed scalar and factorial factors are $p$-units.  Define the
integer



$$
S_{p,h}=[z^{8h+3}](1-z)^{2h+1}(1+z)^4
                    (1+z^2)^{2h-1+p}.             \tag{7.3}
$$



Let $H_1(N)=[z^N]P_1(z)\log(1+z^2)$, with the Item 218 diagonal weight
$P_1=(1-z)^{2h}(1+z)^4(1+z^2)^{2h-1}$.  Since
$8h+3<p$, and since $(1-z)P_1$ has degree $6h+3<8h+3$, the standard
binomial congruence



$$
{1\over p}\binom pk\equiv{(-1)^{k-1}\over k}\pmod p
 \quad(1\leq k<p)                                  \tag{7.4}
$$



gives both $p\mid S_{p,h}$ and the exact bridge



$$
{S_{p,h}\over p}\equiv
 H_1(8h+3)-H_1(8h+2)\pmod p.                       \tag{7.5}
$$



The closed tails of Item 218 give



$$
H_1(8h+2)=Cu,\qquad H_1(8h+3)=Dv,
 \qquad {D\over C}=-{1\over3}.                    \tag{7.6}
$$



Thus the right side of (7.5) is the $p$-unit multiple
$-C(v+3u)/3$.  Equations (7.2), (7.5), and (7.6) prove



$$
p^2\mid S_{p,h}\ \Longrightarrow\ E_h(h)=0,       \tag{7.7}
$$



and, if $x\not\equiv0\pmod p$, the implication in (7.7) is an
equivalence.  The remaining unit is substantive: $x\ne0$ is exactly
the nonvanishing of $Q_0$ up to the known unit $A$.

This gives a rigorous mechanism for eliminant false positives.  It does
not turn them into original common-coordinate zeros.

## 8. Declared finite diagonal evidence

The checker enumerates every prime $p=10h+3\leq2000$.  It finds



$$
\begin{array}{c|r}
\text{diagonal primes}&77\\
h\text{ odd}&40\\
h\text{ even}&37\\
E_h(h)=0&40\\
p^2\mid S_{p,h}&40\\
Q_0=0&0\\
Q_1=0&0.
\end{array}                                                     \tag{8.1}
$$



All 40 eliminant zeros are exactly the odd-$h$ rows; none occurs for
even $h$.  The complete row stream has SHA-256
`7247d97b266a41f9fb6b7157090a6e668310801ce2d8b840f795eed249bd406e`.

The following two statements remain **OPEN**:

1. For every prime $p=10h+3$ with odd $h$, prove
   $p^2\mid S_{p,h}$.
2. For every diagonal prime, prove $x\not\equiv0\pmod p$, or otherwise
   prove directly that at least one original coordinate is nonzero.

The data in (8.1) are **FINITE** and establish neither statement.

## 9. Route-1 rate ledger

The conditional capacity of the complete $j=1$ cell is



$$
{1\over6}\text{ per }m={1\over36}\text{ per }6m.               \tag{9.1}
$$



Item 222 does not exclude the unbounded-$h$ part of that cell and proves
no positive-density exceptional-prime estimate.  Its actual new usable
coefficient is



$$
\boxed{0}.            \tag{9.2}
$$



The all-$h$ divisibility (1.3) localizes the remaining arithmetic to a
one-parameter integer sequence, while Sections 5 and 6 rigorously show why
two natural bounded-complexity approaches do not yet convert that
localization into a rate gain.

## 10. Reproducibility and labels

From the archive root, run

```text
python scripts/item222_j1_phase_resultant_certificate.py --output results/item222_j1_phase_resultant_certificate.json
python scripts/item222_j1_phase_resultant_certificate.py --output results/item222_j1_phase_resultant_certificate.replay.json
```

The checker uses only Python 3.11+ standard-library integer, `Fraction`,
polynomial, and finite-field arithmetic.  It embeds no host path and has
no external data dependency.

**PROVED:** the phase reduction (1.2), formulas (2.7) and (3.1)--(3.6),
the complete $p$-unit audit and necessary condition (1.3), the height
bound (5.2), the recurrence no-go in the exact domain (6.1), and the
diagonal coefficient bridge (7.3)--(7.7).

**FINITE:** exact rational replay through $h\leq80$, and the complete
diagonal prime check through $p\leq2000$, with no extrapolation.

**OPEN:** all-prime odd-diagonal supercongruence; uniform original-coordinate
nonvanishing; any higher-order or higher-degree recurrence; a weighted
exceptional-prime bound for unbounded $h$; any positive Route-1 rate
gain from $j=1$; and the separate $j=2$ classification.
