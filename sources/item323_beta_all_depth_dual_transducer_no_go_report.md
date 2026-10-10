> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 323 — the all-depth beta dual transducer and literal-inheritance no-go

Checked: 2026-08-31 (Beijing time)

## 1. Strict verdict

Retain



$$
q_0=q_1=1,
\qquad
q_n=(4n-2)q_{n-1}+q_{n-2}\quad(n\ge2),
\tag{1.1}
$$



and, for $n\ge5$, put



$$
A=4n-2,
\qquad
a=q_{n-1},\quad b=q_n,\quad c=q_{n-2},
\qquad m=n-2.
\tag{1.2}
$$



Item 316 proves that a centered half-bound failure is equivalent to the
exact canonical target



$$
\frac{a}{2c}\le R<\frac a2,
\qquad
0<|E_m|<c,
\qquad
E_{m+1}=\operatorname{sgn}(E_m)Q_m.
\tag{1.3}
$$



Item 320 carried (1.3) backward through every fixed sub-half-linear
truncation depth.  Its comparison used the crude deviation estimate
$|z_{m-r}|<(4n)^{r+1}$, which loses its force near depth $n/2$.

Item 323 removes that loss exactly.

> **PROVED — ALL-DEPTH DUAL-TRANSDUCER THEOREM.**  For every canonical
> Ostrowski word representing $0\le R<Q_m$, there is an exact reversed
> suffix transducer $s_j$, defined in Section 3, such that
>
> 

$$
> \boxed{-1<s_j<1\qquad(0\le j\le m).}
> \tag{1.4}
>
$$


>
> If the word also satisfies the actual Item-316 boundary (1.3), then at
> every depth
>
> 

$$
> \boxed{
> \left|\operatorname{sgn}(E_m)E_j-
> \frac{aQ_j}{b}\right|<1
> \qquad(0\le j\le m+1).}
> \tag{1.5}
>
$$



Thus every signed prefix determinant lies in one of the two integer cells
adjacent to the exact continuous center $aQ_j/b$.  There is no
factorial-versus-exponential transition at depth $n/2$: the exact
deviation is uniformly less than one through the whole tower.

This proves the global scoped closure requested after Item 320.

> **PROVED — ALL-DEPTH LITERAL-INHERITANCE NO-GO.**  For every $n\ge5$,
> if an actual Item-316 target existed, then no literal prefix truncation
> at any depth could itself inherit an exact earlier Item-316 appended
> target.  More precisely, for every $1\le j\le m$,
>
> 

$$
> \boxed{\left|\mathscr U_{j-1}\right|\ne Q_{j-1}.}
> \tag{1.6}
>
$$



The proof is division-free for every $j\ge3$.  The two bottom indices
$j=1,2$ are handled symbolically from the exact Markov carry, not by a
scan.  The single structural base $n=5$, at which the general
$j\ge3$ inequality is not needed, has no Item-316 target by an exact
calculation.

Equation (1.6) closes the complete literal prefix/inherited-target descent,
including critical depth $L\sim n/2$, supercritical linear depth, and
base-reaching depth.  It does **not** exclude the original all-digit target
(1.3).  It also does not cover canonical redigitization of a complement,
a nonlinear invariant, an odd-modulus or growing-precision square
condition, or a different descent endpoint.

No full-target half-bound, proper-target theorem, or capacity reduction is
proved.  Booking is zero.

## 2. Coordinates and the exact target boundary

Set



$$
w_1=7,
\qquad
w_j=4j+2\quad(2\le j\le m),
\qquad
w_{m+1}=A.
\tag{2.1}
$$



Define



$$
Q_{-1}=0,\quad Q_0=1,
\qquad
P_{-1}=1,\quad P_0=0,
\tag{2.2}
$$





$$
Q_j=w_jQ_{j-1}+Q_{j-2},
\qquad
P_j=w_jP_{j-1}+P_{j-2}.
\tag{2.3}
$$



Then



$$
Q_j=q_{j+1},
\qquad
Q_m=a,
\qquad
Q_{m+1}=b.
\tag{2.4}
$$



Let $\delta_1,\ldots,\delta_m$ be the canonical digits of $R$:



$$
R=\sum_{i=0}^{m-1}\delta_{i+1}Q_i,
\tag{2.5}
$$





$$
0\le\delta_1\le6,
\qquad
0\le\delta_j\le w_j\quad(2\le j\le m),
\tag{2.6}
$$





$$
\delta_j=w_j\Longrightarrow\delta_{j-1}=0.
\tag{2.7}
$$



Extend the word by $\delta_{m+1}=0$.  For $0\le j\le m+1$, put



$$
R_j=\sum_{i=0}^{j-1}\delta_{i+1}Q_i,
\qquad
Z_j=\sum_{i=0}^{j-1}\delta_{i+1}P_i,
\tag{2.8}
$$



and



$$
E_j=R_jP_j-Z_jQ_j.
\tag{2.9}
$$



Every canonical prefix satisfies



$$
0\le R_j<Q_j.
\tag{2.10}
$$



The universal determinant recurrence from Item 320 is



$$
E_{j+1}=w_{j+1}E_j+E_{j-1}+(-1)^j\delta_{j+1},
\qquad
E_0=0,\quad E_1=\delta_1.
\tag{2.11}
$$



Assume only when explicitly stated that the actual Item-316 target holds.
Write



$$
\sigma=\operatorname{sgn}(E_m),
\qquad
\epsilon=(-1)^n\sigma,
\qquad
k_j=\sigma E_j.
\tag{2.12}
$$



Then its exact two-point boundary is



$$
k_m=\kappa,
\qquad
k_{m+1}=Q_m=a,
\tag{2.13}
$$



where



$$
a^2=b\kappa+\epsilon R.
\tag{2.14}
$$



The continuous homogeneous center and its deviation are



$$
x_j=\frac{aQ_j}{b},
\qquad
z_j=k_j-x_j.
\tag{2.15}
$$



Consequently



$$
z_{m+1}=0,
\qquad
z_m=-\epsilon\frac Rb.
\tag{2.16}
$$



For arbitrary canonical words, (2.11) is universal, but (2.13)-(2.16)
are not.  Every use of $z_j$ below is conditional on the actual target.

## 3. The reversed suffix transducer

Define appended suffix continuants by



$$
H_j=K(w_{j+2},w_{j+3},\ldots,w_{m+1})
\qquad(0\le j\le m),
\tag{3.1}
$$



with $K(\varnothing)=1$, and declare the one-step boundary



$$
H_{m+1}=0.
\tag{3.2}
$$



Thus



$$
H_m=1,
\qquad
H_{m-1}=A,
\qquad
H_{j-1}=w_{j+1}H_j+H_{j+1}.
\tag{3.3}
$$



Define integer suffix loads by



$$
N_m=N_{m+1}=0,
\tag{3.4}
$$





$$
N_{j-1}=w_{j+1}N_j+N_{j+1}+\delta_{j+1}
\qquad(1\le j\le m).
\tag{3.5}
$$



The exact dual-transducer state is



$$
\boxed{s_j=\frac{RH_j-bN_j}{b}.}
\tag{3.6}
$$



It starts at



$$
s_m=\frac Rb,
\qquad
s_{m+1}=0,
\tag{3.7}
$$



and (3.3)-(3.5) give the exact backward recurrence



$$
\boxed{
s_{j-1}=w_{j+1}s_j+s_{j+1}-\delta_{j+1}.}
\tag{3.8}
$$



No target hypothesis is present in (3.1)-(3.8).  The state is a genuine
dual transducer attached to every canonical digit word.

## 4. Exact continuant split

For $j+1\le h\le m-1$, put



$$
C_{j,h}=K(w_{j+2},\ldots,w_h),
\tag{4.1}
$$



so $C_{j,j+1}=1$.  Splitting the full continuant at $j$ gives



$$
\boxed{
b=H_jQ_{j+1}+H_{j+1}Q_j.}
\tag{4.2}
$$



The corresponding cross-determinant is



$$
\boxed{
Q_hH_j-bC_{j,h}=(-1)^{h-j}Q_jH_h.}
\tag{4.3}
$$



At $h=j+1$, (4.3) is exactly



$$
Q_{j+1}H_j-b=-Q_jH_{j+1}.
\tag{4.4}
$$



Appending one coefficient to $h$ proves (4.3) by the continuant
recurrence.  Thus its sign and its empty-word endpoint are fixed without
a finite fit.

Unrolling (3.5) gives



$$
\boxed{
N_j=\sum_{h=j+1}^{m-1}\delta_{h+1}C_{j,h}.}
\tag{4.5}
$$



Also



$$
R=R_{j+1}+
\sum_{h=j+1}^{m-1}\delta_{h+1}Q_h.
\tag{4.6}
$$



Multiplying (4.6) by $H_j$, subtracting $bN_j$, and using
(4.3) yields the exact split



$$
\boxed{
RH_j-bN_j=H_jR_{j+1}+Q_j\mathcal A_j,}
\tag{4.7}
$$



where



$$
\mathcal A_j=
\sum_{h=j+1}^{m-1}
(-1)^{h-j}\delta_{h+1}H_h.
\tag{4.8}
$$



This is the central all-depth identity.  It keeps the lower prefix
$R_{j+1}$, every upper digit, and the appended coefficient $A$.

## 5. The alternating tail bound and uniform unit strip

The suffix recurrence gives



$$
w_{h+1}H_h=H_{h-1}-H_{h+1}.
\tag{5.1}
$$



The positive terms of (4.8) occur at
$h=j+2,j+4,\ldots$.  Using $\delta_{h+1}\le w_{h+1}$, their total
is at most



$$
\sum_{
\substack{j+2\le h\le m-1\\h\equiv j\pmod2}}
w_{h+1}H_h
\le H_{j+1}.
\tag{5.2}
$$



The magnitude of the negative terms, at
$h=j+1,j+3,\ldots$, is at most



$$
\sum_{
\substack{j+1\le h\le m-1\\h\not\equiv j\pmod2}}
w_{h+1}H_h
\le H_j.
\tag{5.3}
$$



Both sums telescope by (5.1).  Therefore



$$
\boxed{-H_j\le\mathcal A_j\le H_{j+1}.}
\tag{5.4}
$$



Canonicality gives $0\le R_{j+1}<Q_{j+1}$.  Combining (4.2),
(4.7), and (5.4),



$$
-Q_jH_j
\le RH_j-bN_j
<H_jQ_{j+1}+Q_jH_{j+1}=b.
\tag{5.5}
$$



Since $Q_j<Q_{j+1}$ and every $H_j>0$, (4.2) also gives



$$
Q_jH_j<b.
\tag{5.6}
$$



Hence



$$
\boxed{-b<RH_j-bN_j<b,}
\tag{5.7}
$$



which proves (1.4).  This proof is exact for every depth.  It uses no
asymptotic comparison and no observation bound.

## 6. Identification with the target deviation

Under the actual target, subtracting the homogeneous recurrence for
$x_j$ from (2.11) gives



$$
z_{j-1}=z_{j+1}-w_{j+1}z_j
-\sigma(-1)^j\delta_{j+1}.
\tag{6.1}
$$



Because $m=n-2$ has the same parity as $n$, equations (2.16) and
(3.7)-(3.8) show that the two sequences are exactly related by



$$
\boxed{
s_j=-\epsilon(-1)^{m-j}z_j
=-\sigma(-1)^jz_j.}
\tag{6.2}
$$



The top two values agree, and (3.8) is precisely the sign-normalized
version of (6.1), so (6.2) holds at every index by backward induction.

Equations (5.7) and (6.2) prove



$$
\boxed{|z_j|<1\qquad(0\le j\le m+1),}
\tag{6.3}
$$



where $z_{m+1}=0$.  Equivalently,



$$
\boxed{
\sigma E_j\in
\left(
\frac{aQ_j}{b}-1,
\frac{aQ_j}{b}+1
\right)\cap\mathbb Z.}
\tag{6.4}
$$



Because $0<Q_j<b$ for $j\le m$ and $\gcd(a,b)=1$, the center
$aQ_j/b$ is not an integer.  Thus (6.4) contains exactly the floor and
ceiling cells of that center.

This is the promised global replacement for Item 320's
$(4n)^{r+1}$ estimate.  The old $1/2$ depth threshold came from an
upper bound that ignored the canonical cancellation encoded by
$N_j$; it is not a genuine transition of the exact target dynamics.

## 7. Division-free exclusion for every $j\ge3$

For the literal lower prefix $\delta_1,\ldots,\delta_{j-1}$ with
$w_j$ appended, Item 320's exact boundary formula is



$$
\boxed{
\mathscr U_{j-1}=(-1)^{j+1}E_j-\delta_j.}
\tag{7.1}
$$



An inherited earlier Item-316 target would require



$$
|\mathscr U_{j-1}|=Q_{j-1}.
\tag{7.2}
$$



Under the original target, (6.3), $a/b<1/A$, and
$\delta_j\le w_j$ give



$$
|\mathscr U_{j-1}|
\le |E_j|+\delta_j
<\frac{aQ_j}{b}+1+w_j
<\frac{(w_j+1)Q_{j-1}}{A}+w_j+1.
\tag{7.3}
$$



For $n\ge6$ and $3\le j\le n-2$, the exact division-free inequality



$$
\boxed{
\bigl(A-w_j-1\bigr)Q_{j-1}>A(w_j+1)}
\tag{7.4}
$$



holds.  In beta notation it is



$$
\boxed{
\bigl(4(n-j)-5\bigr)q_j
>(4n-2)(4j+3).}
\tag{7.5}
$$



Here is an all-index proof.  For fixed $j$, the difference between the
left and right sides of (7.5) increases by



$$
4(q_j-4j-3)>0
\tag{7.6}
$$



when $n$ is replaced by $n+1$.  At $j=3$, the smallest relevant
row is $n=6$, where



$$
7q_3-22\cdot15=7\cdot71-330=167>0.
\tag{7.7}
$$



For $j\ge4$, the smallest row is $n=j+2$, and (7.5) reduces to



$$
3q_j>(4j+6)(4j+3).
\tag{7.8}
$$



It holds at $j=4$:



$$
3q_4-22\cdot19=3003-418=2585>0.
\tag{7.9}
$$



The beta recurrence gives $q_{j+1}>(4j+2)q_j$, while, for $j\ge4$,



$$
(4j+2)(4j+6)(4j+3)>(4j+10)(4j+7).
\tag{7.10}
$$



Thus (7.8) propagates by induction.  This proves (7.4) without dividing
by any moving integer.

Combining (7.3) and (7.4),



$$
\boxed{
|\mathscr U_{j-1}|<Q_{j-1}
\qquad(n\ge6,\ 3\le j\le m).}
\tag{7.11}
$$



In particular, the exact inherited endpoint (7.2) is impossible at
critical, supercritical, and near-base depths alike.

## 8. Exact bottom-index closure

The bottom index $j=1$ is an identity:



$$
\mathscr U_0=E_1-\delta_1=0,
\tag{8.1}
$$



so it cannot equal $\pm Q_0=\pm1$.

For $j=2$, first observe that



$$
0<x_1=\frac{7a}{b}<\frac7A<1.
\tag{8.2}
$$



By (6.4),



$$
k_1=\sigma E_1=\sigma\delta_1\in\{0,1\}.
\tag{8.3}
$$



Also $x_2>0$, so (6.4) implies



$$
k_2=\sigma E_2\ge0.
\tag{8.4}
$$



The exact bottom recurrence is



$$
E_2=10\delta_1-\delta_2.
\tag{8.5}
$$



If $\sigma=1$, then $\delta_1\in\{0,1\}$.  When
$\delta_1=0$, (8.4) forces $\delta_2=0$, and
$\mathscr U_1=0$.  When $\delta_1=1$, the Markov rule excludes
$\delta_2=10$, and every remaining nonnegative case has



$$
\mathscr U_1=-E_2-\delta_2=-10.
\tag{8.6}
$$



If $\sigma=-1$, (8.3) forces $\delta_1=0$.  Then



$$
k_2=\delta_2,
\qquad
\mathscr U_1=-E_2-\delta_2=0.
\tag{8.7}
$$



Therefore



$$
\boxed{\mathscr U_1\in\{0,-10\}\ne\{\pm7\}.}
\tag{8.8}
$$



This is a symbolic two-cell argument.  It is not a bounded digit scan.

The only row not covered by (7.11) when $j\ge3$ is the structural base
$n=5$.  Its exact actual values are



$$
(a,b,\kappa,R)=(1001,18089,55,7106),
\qquad
2R-a=13211>0.
\tag{8.9}
$$



Hence it has no Item-316 target at all.  Equations (7.11), (8.1),
(8.8), and (8.9) prove the all-depth no-go (1.6) for every $n\ge5$.

## 9. Scope, Item 320, Item 282, and capacity

Item 323 supersedes only Item 320's depth restriction.  The exact logical
statement is



$$
\boxed{
\text{original Item-316 target}
\Longrightarrow
\text{no literal truncated prefix inherits an earlier target}.}
\tag{9.1}
$$



It is not the converse, and the failure of every inherited target is not a
contradiction to the original target.  A hypothetical original word can
remain globally resonant while every literal prefix misses the earlier
endpoint.  That is exactly the method closure proved here.

The theorem does not apply after redigitizing the Item-295 defect or any
later complement in a new canonical basis.  It does not control a
nonlinear function of $s_j$, an odd-modulus condition, growing
$2$-adic precision, or a coupled Bessel/Turán state.  Those remain
possible attacks on the original equality.

The suffix continuants in Section 4 are exact coordinate changes, not new
common factors.  No declared proper de-overlapped target $Q\mid b$ is
bounded, and no Item-282 return or product contribution is rebooked.

### PROVED

* The exact suffix-load recurrence (3.5) and transducer (3.6)-(3.8).
* The continuant split and cross-determinant (4.2)-(4.3), with every
  empty-word boundary and sign fixed.
* The alternating tail bound (5.4).
* The universal all-depth unit strip $-1<s_j<1$.
* Conditional on the actual target, the global nearest-center confinement
  (6.3)-(6.4).
* The division-free inequality (7.4) for every declared index.
* The symbolic bottom-index classification (8.1)-(8.8).

### PROVED SCOPED NO-GO

* The entire literal canonical prefix/inherited-target descent is closed
  at every depth, including $L\sim n/2$, every supercritical linear
  depth, and base-reaching depth.
* This does not exclude the original all-digit equality, redigitized or
  nonlinear descents, or a new arithmetic invariant.

### EXACT FINITE ONLY

* The deterministic replay's declared continuant, transducer, sign,
  bottom-state, inequality, and $n=5$ control rows.
* Bounded control rows verify the symbolic formulas and are not promoted
  into an original-target exclusion or half-bound theorem.

### OPEN

* The original all-digit exclusion (1.3) and the centered half-bound.
* A redigitized complement or nonlinear invariant using the exact
  transducer state.
* Growing/full $2$-adic or odd-modulus square information.
* Every proper-target consequence and beta capacity reduction.
* Item 282's weighted return cover, Route 1, and every conclusion about
  $e+\pi$.

### BOOKING



$$
\boxed{
\text{new beta capacity reduction}=0,
\qquad
\text{new Route-1 rate}=0.}
\tag{9.2}
$$



No canonical, master, status, or research-log file is edited by this work
package.

## 10. Deterministic replay

From the archive root:

~~~text
python work/item323_beta_all_depth_dual_transducer_no_go_certificate.py ^
  --output work/item323_beta_all_depth_dual_transducer_no_go_certificate.replay.json
~~~

The checker uses only the Python standard library and exact integer or
rational arithmetic.  It performs no half-bound scan and promotes no
bounded row.
