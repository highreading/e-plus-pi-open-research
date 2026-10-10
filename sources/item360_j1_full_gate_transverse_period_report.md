> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 360 — reconstruction of the full fixed-$j=1$ gate and its transverse parameter-derivative period

Date: 2026-09-01

## 1. Outcome and capacity first

The actual fixed common-log cell is



$$
p=4h+6s+3,\qquad M=3h+4s+2,\qquad h,s\geq1,              \tag{1.1}
$$



and its original ordinary collision is the simultaneous pair



$$
Q_0(h,s)=Q_1(h,s)=0\pmod p.                              \tag{1.2}
$$



Items 222–357 retained only the necessary Hasse/eliminant coordinate



$$
a_{r,n}=0\pmod p,qquad n=2h,\quad r=2s+1.               \tag{1.3}
$$



This item reconstructs (1.2) before that selection and computes its exact
period-coordinate elimination ideal.

The main result is that two different ideals have been conflated in the
one-coordinate route.

1. If the moving factorial ratio is forgotten and eliminated as an
   unspecified variable, the elimination ideal is exactly the principal
   Hasse ideal.
2. On the actual tied family, that factorial ratio has one fixed explicit
   value.  The full gate is then a prime codimension-two ideal.

Thus the unused original equation does force a genuinely transverse
period.  It is not an arbitrary numerator moment: it is exactly the first
original common-log coordinate and has the parameter-derivative form



$$
\boxed{
\mathscr T_{h,s}
=\left.\partial_\tau
\bigl(2[z^{T}]-[z^{L_0}]\bigr)
(1-z)^{2h}(1+z)(1+z^2)^{2s+\tau}
\right|_{\tau=0},}                                      \tag{1.4}
$$



where



$$
T=2h+6s+2,\qquad L_0=4h+4s+2.                           \tag{1.5}
$$



Every denominator in (1.4) is a $p$-unit, and



$$
\boxed{\mathscr T_{h,s}=Q_0(h,s).}                       \tag{1.6}
$$



Therefore



$$
\boxed{
\text{full ordinary collision}
\Longrightarrow a_{r,n}=0,\quad\mathscr T_{h,s}=0.}     \tag{1.7}
$$



The transverse condition is independent of selected Hasse vanishing.  On
the two predeclared selected-zero rows,



$$
(p,h,s)=(13,1,1),\ (47,8,2),                             \tag{1.8}
$$



one has respectively



$$
(a_{r,n},\mathscr T_{h,s})=(0,9),\ (0,30)\pmod p.        \tag{1.9}
$$



Neither row is asserted to be a full collision.

This is a real codimension gain in the exact full-gate information, but no
weighted joint-zero theorem is proved.  Hence



$$
\boxed{
\text{new collision-forced algebraic condition}=1,\quad
\text{new linear log rate}=0,\quad
\text{new fixed-}j=1\text{ capacity reduction}=0.}       \tag{1.10}
$$



Booking remains $0$, the $1/36$ ceiling per $6M$ is retained, and
Route 1 remains ACTIVE.

## 2. The original two coordinates before elimination

Retain Item 218's terminating periods



$$
\begin{aligned}
x&=\operatorname {Odd}(K_0;s,2s),&
y&=\operatorname {Odd}(K_0;h,2s),\\
u&=\operatorname {Even}(K_1;s,2s-1),&
v&=\operatorname {Odd}(K_1;h,2s-1),
\end{aligned}                                             \tag{2.1}
$$



where



$$
K_0=(1-z)^{2h}(1+z),\qquad
K_1=(1-z)^{2h}(1+z)^4.                                   \tag{2.2}
$$



The four factorial prefactors are denoted



$$
\mathsf A,\quad\mathsf B,\quad\mathsf C,\quad\mathsf D. \tag{2.3}
$$



They are all $p$-units on every actual row.  The two original divided
coordinates are exactly



$$
Q_0=2\mathsf A x-\mathsf B y,\qquad
Q_1=2\mathsf C u-\mathsf D v.                            \tag{2.4}
$$



Define the three actual scalar ratios



$$
\lambda={\mathsf B\over\mathsf A},\qquad
\alpha={\mathsf C\over\mathsf A}
=-{3(3s+1)\over2s},\qquad
\beta={\mathsf D\over\mathsf B}
={2s+h+1\over2s}.                                       \tag{2.5}
$$



The first ratio is the explicit moving factorial value



$$
\boxed{
\lambda_{h,s}
=(-1)^{h-s}{h!\binom{3s+1}{s}\over(2s+2)_h}.}           \tag{2.6}
$$



Normalize by the unit $\mathsf A$:



$$
f_0={Q_0\over\mathsf A}=2x-\lambda y,qquad
f_1={Q_1\over\mathsf A}=2\alpha u-\beta\lambda v.      \tag{2.7}
$$



The full gate is precisely



$$
f_0=f_1=0.                                                \tag{2.8}
$$



## 3. Why forgetting the factorial ratio gives one principal Hasse ideal

Work first over a coefficient field containing $\alpha,\beta$, and
treat $\lambda$ as an unspecified variable.  Put



$$
I_{\rm univ}
=\langle2x-\lambda y,\ 2\alpha u-\beta\lambda v\rangle
\subset K[x,y,u,v,\lambda].                              \tag{3.1}
$$



The exact resultant is



$$
\boxed{
\operatorname {Res}_\lambda
(2x-\lambda y,2\alpha u-\beta\lambda v)
=2H,}                                                     \tag{3.2}
$$



where



$$
\boxed{H=\beta xv-\alpha uy.}                            \tag{3.3}
$$



Moreover



$$
K[x,y,u,v,\lambda]/I_{\rm univ}
\cong K[y,v,\lambda],                                    \tag{3.4}
$$



through



$$
x={\lambda y\over2},\qquad
u={\beta\lambda v\over2\alpha}.                         \tag{3.5}
$$



The kernel on the four period coordinates is the single rank-one minor
(3.3).  Hence the exact elimination ideal is



$$
\boxed{
I_{\rm univ}\cap K[x,y,u,v]=\langle H\rangle.}           \tag{3.6}
$$



This proves globally why the earlier elimination produced one Hasse
coordinate: it projected away the actual value of $\lambda$.

On an actual row, Item 218's eliminant is exactly



$$
E_h(s)=H.                                                 \tag{3.7}
$$



Items 243, 332, and 339 give a unit $\kappa_{h,s}\in\mathbb F_p^\times$
such that



$$
\boxed{a_{r,n}=\kappa_{h,s}H\pmod p.}                    \tag{3.8}
$$



Explicitly, if $\mathcal R_h$ is Item 243's unit gauge, one may take



$$
\kappa_{h,s}={3\,2^{2h-1}\mathcal R_h\over4h+3}.       \tag{3.9}
$$



Every factor in (3.9) is a $p$-unit on the actual family.

## 4. The actual tied fiber has codimension two

Now specialize $\lambda$ to its actual value (2.6).  In the exact
period-coordinate ring put



$$
I_{h,s}=\langle f_0,f_1\rangle.                           \tag{4.1}
$$



The quotient solves uniquely for $x,u$ in terms of $y,v$.  Therefore



$$
\boxed{
I_{h,s}\text{ is prime of codimension }2.}               \tag{4.2}
$$



The Hasse period belongs to this ideal through the exact syzygy



$$
\boxed{\beta v f_0-yf_1=2H.}                              \tag{4.3}
$$



But $f_0\notin\langle H\rangle$.  For example,



$$
(x,y,u,v)=(1,0,0,0)                                      \tag{4.4}
$$



has $H=0$ and $f_0=2$.  Thus the actual full gate is strictly
stronger than the principal Hasse hypersurface.

This is an ambient period-coordinate statement specialized to the exact
actual scalar (2.6), not a claim that the four periods are arbitrary on
the binomial orbit.  The actual rows in (1.9) independently rule out a
universal implication from selected Hasse zero to $f_0=0$ on that orbit.

## 5. Exact chart decomposition and the boundary that must not be lost

Replacing $f_1$ by $H$ is legitimate only after a chart saturation.
Indeed, (4.3) gives



$$
\langle f_0,H\rangle=\langle f_0,yf_1\rangle.            \tag{5.1}
$$



Because $y$ and $f_1$ are relatively prime modulo $f_0$,



$$
\boxed{
\langle f_0,H\rangle
=I_{h,s}\cap\langle x,y\rangle.}                         \tag{5.2}
$$



Equivalently,



$$
\boxed{I_{h,s}=\langle f_0,H\rangle:y^\infty.}           \tag{5.3}
$$



The symmetric chart is



$$
\boxed{
\langle f_1,H\rangle
=I_{h,s}\cap\langle u,v\rangle,qquad
I_{h,s}=\langle f_1,H\rangle:v^\infty.}                  \tag{5.4}
$$



Thus $H=0$ plus the transverse equation $f_0=0$ recovers the full
gate away from $y=0$.  Without saturation it also contains the explicit
spurious boundary $x=y=0$, where the second original coordinate remains
unconstrained.  The same warning applies to the $v$-chart.

This boundary is retained in every capacity statement below.  No
nonvanishing or zero-density theorem for it is assumed.

## 6. The transverse period is forced by the actual collision

Define



$$
P_0(z;\tau)
=(1-z)^{2h}(1+z)(1+z^2)^{2s+\tau}.                       \tag{6.1}
$$



Then



$$
\left.\partial_\tau P_0(z;\tau)\right|_{\tau=0}
=(1-z)^{2h}(1+z)(1+z^2)^{2s}\log(1+z^2).                \tag{6.2}
$$



Item 218's exact palindromic reduction therefore gives (1.4)–(1.6).
In the terminating-tail coordinates,



$$
\boxed{
{\mathscr T_{h,s}\over\mathsf A}
=2x-\lambda_{h,s}y=f_0.}                                \tag{6.3}
$$



Thus $\mathscr T$ is a transverse deformation of the actual common-log
period in the $(1+z^2)$-exponent direction.  It is not introduced after
the fact: it is the first original divided coordinate.

The denominator audit is inherited exactly from Item 218.  Every
logarithmic denominator is an integer strictly between $0$ and $p$,
and all factorials in $\mathsf A$ are below $p$.  Hence (6.3) is valid
on every actual row with no exceptional prime.

## 7. Declared exact controls

Only the five rows already predeclared in Items 339–357 are used.

| $(h,s,p)$ | $(Q_0,Q_1)$ | $H=E_h(s)$ | selected $a_{r,n}$ | transverse $\mathscr T$ |
|---|---|---:|---:|---:|
| $(1,1,13)$ | $(9,4)$ | $0$ | $0$ | $9$ |
| $(2,1,17)$ | $(14,14)$ | $11$ | $8$ | $14$ |
| $(8,2,47)$ | $(30,41)$ | $0$ | $0$ | $30$ |
| $(4,4,43)$ | $(25,27)$ | $34$ | $2$ | $25$ |
| $(2,6,47)$ | $(17,23)$ | $42$ | $36$ | $17$ |

The exact rational values of $\mathscr T$ before reduction are



$$
{7\over60},\quad {76\over105},\quad
-{140347\over5819814},\quad {257\over437580},\quad
{25607\over10581480}.                                    \tag{7.1}
$$



The certificate independently extracts these parameter derivatives and
reduces them to the displayed $Q_0$ values.  It also reconstructs all
four periods, all four factorial prefactors, $\lambda,\alpha,\beta$,
both normalized gate equations, the syzygy, and the positive-prefix Hasse
coefficient.

No displayed row is a full collision.  In particular, the two Hasse-zero
rows are separation witnesses, not collision witnesses and not density
evidence.

## 8. Capacity audit and the new joint target

At fixed $M$, the actual candidate primes have logarithmic mass



$$
{M\over6}+o(M),                                           \tag{8.1}
$$



or $1/36$ per $6M$.  The transverse condition reaches every row, so
its raw support is large enough to matter.

Define the joint Hasse/transverse envelope



$$
\mathcal W_{H,\mathscr T}(M)
=\sum_{\substack{s\in\mathcal S_M,\ p_s\ {\rm prime}\\
                  a_{2s+1,2h_s}=0\ ({\rm mod}\ p_s)\\
                  \mathscr T_{h_s,s}=0\ ({\rm mod}\ p_s)}}
 \log p_s.                                                \tag{8.2}
$$



Every full ordinary collision is counted in (8.2), including every chart
boundary.  Therefore



$$
\boxed{\mathcal W_{\rm full}(M)\leq
       \mathcal W_{H,\mathscr T}(M).}                     \tag{8.3}
$$



A theorem



$$
\boxed{\mathcal W_{H,\mathscr T}(M)=o(M)}                \tag{8.4}
$$



would remove the entire fixed-$j=1$ ceiling and book $1/36$ per
$6M$.  Any strict constant below $M/6$ would already book a partial
saving.

But algebraic codimension two is not a weighted zero-density theorem.
The period $\mathscr T$ still has moving hypergeometric length and no
fixed-$M$ sublinear-height common target is proved.  The boundary
$x=y=0$ also has no weighted upper bound.  Consequently (8.4) remains
OPEN and no capacity is booked.

The new admissible Builder directions are now exact rather than ambient:

1. a finite-field hypergeometric or Frobenius representation of the pair
   $(a_{r,n},\mathscr T_{h,s})$;
2. an average-gcd theorem between the selected Hasse numerator and the
   cleared parameter-derivative period; or
3. a monodromy/nonconcentration theorem for their joint zero divisor on
   the tied family.

## 9. Strict decision

### PROVED

- exact reconstruction of the full two-coordinate Item 218 gate;
- the principal elimination ideal $\langle H\rangle$ after forgetting
  the factorial ratio;
- the prime codimension-two actual-fiber ideal $\langle f_0,f_1\rangle$;
- the exact syzygy and both primary chart decompositions;
- the first original coordinate as the transverse parameter-derivative
  period (1.4);
- one additional collision-forced algebraic condition;
- zero booking.

### EXACT FINITE ONLY

- five predeclared rows;
- two selected-Hasse zeros with nonzero transverse period;
- no prime scan, full-collision claim, or density inference.

### OPEN

- weighted joint-zero density (8.4);
- weighted control of the two chart boundaries;
- a fixed-M average gcd or sublinear-height common target;
- any strict fixed-$j=1$ ceiling reduction, Route 1, and every conclusion
  about $e+\pi$.

## 10. Ledger and self-audit



$$
\begin{array}{c|c}
\text{quantity}&\text{Item 360 value}\\ \hline
\text{forgotten-ratio Hasse codimension}&1\\
\text{actual full-gate codimension}&2\\
\text{new collision-forced algebraic condition}&1\\
\text{new proved linear log rate}&0\\
\text{new fixed-}j=1\text{ capacity reduction}&0\\
\text{retained fixed-}j=1\text{ ceiling per }6M&1/36
\end{array}                                               \tag{10.1}
$$



The self-audit records:

1. the original full collision is never replaced by a selected-factor
   converse;
2. Hasse-zero separation controls are not called full collisions;
3. the actual factorial ratio is fixed before the codimension-two claim;
4. saturation boundaries are retained explicitly;
5. algebraic codimension receives no density weight;
6. no capacity is booked without an asymptotic actual-family theorem.
