> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 426 — exact cellwise first-Witt gate and the actual-step period recurrence

Date: 2026-09-01  
Status: **WORK-ONLY, UNAUDITED, EXACT RECURRENCE AND CAPACITY LOCALIZATION, NO BOOKING**

## 1. Capacity-first verdict

Retain Item 424's ordinary rank-zero first-Witt gate.  For an odd prime
$p\in\mathcal P_m$ satisfying



$$
p^2>4m+1,                                                \tag{1.1}
$$



put



$$
\kappa_{m,p}=\frac{A_m}{p}\pmod p.                      \tag{1.2}
$$



Item 424 proves



$$
v_p(c_m)\ge b_{m,p}+1
 \quad\Longleftrightarrow\quad \kappa_{m,p}=0,           \tag{1.3}
$$



where $b_{m,p}=v_p(K_m)\in\{0,1\}$.  Every such row has unique
parameters



$$
4m+1=(2j+1)p-2s,
 \qquad1\le s\le\frac{p-3}{6},                           \tag{1.4}
$$



and



$$
6m=(3j+1)p+r,
 \qquad r=\frac{p-6s-3}{2}.                              \tag{1.5}
$$



This item gives two uniform advances.

First, it turns $\kappa$ into an exact cellwise determinant.  Define
the two zero-constant primitives



$$
T_\nu'(x)=P_{\nu,s}(x),
 \qquad
 P_{\nu,s}=u^rQ^{2s-\nu},
 \qquad \nu=0,1,                                        \tag{1.6}
$$



where $u=x(1-x)$ and $Q=(1+x)(1+x^2)$.  A four-section map followed
by one fixed Hermite recurrence gives four-dimensional vectors
$H_{\nu,j,s,p}$, and exact linear functionals $R_j,L_j$ satisfy



$$
\boxed{
 \kappa_{m,p}
 =L_j(H_1)R_j(H_0)-L_j(H_0)R_j(H_1)\pmod p.}            \tag{1.7}
$$



No characteristic-zero endpoint coordinate or precomputed content gcd is
needed once the cell data are supplied.

Second, away from the terminal band $r<24$, all four special endpoint
periods entering (1.7) satisfy a nonzero recurrence of order at most four
in the **actual row step**



$$
s\longmapsto s+2,
 \qquad m\longmapsto m-1                               \tag{1.8}
$$



at fixed $(p,j)$.  The recurrence is produced by a $49\times50$
exact linear system over $\mathbb F_p$, and Section 5 proves that its
five recurrence coefficients cannot all vanish.

The terminal band lost by this recurrence has zero linear capacity:



$$
\boxed{
 \sum_{\substack{p\in\mathcal P_m\\0\le r<24}}\log p
 =O(\log m)=o(m).}                                      \tag{1.9}
$$



However, the recurrence does **not** prove weighted zero density for
$\kappa$.  A bounded-order recurrence controls long zero runs only after
a unit audit; it does not control isolated zeros, which may occupy a
positive fraction of a finite-field sequence.  Therefore the rigorous
component ceilings remain



$$
\frac{\mathfrak C_F}{6}
 =0.3895079179997942811851475804\ldots                  \tag{1.10}
$$



for the whole first-Witt radical layer, and



$$
\frac{\mathfrak C_F-2}{6}
 =0.0561745846664609478518142471\ldots                  \tag{1.11}
$$



for the already booked Item-149 overlap.  No smaller ceiling, positive
mass, or new booking is proved.

## 2. Booking and overlap before the recurrence

The three layers must remain separate.

1. Every $p\in\mathcal P_m$ supplies the ordinary squarefree factor in
   $F_m=G_m$.  That factor was already removed in the normalized
   carrier and is not new Item-426 credit.
2. The $j=0$ cell is
   $4m+1<p\le6m$.  It is not in Item 149.  Here $b_{m,p}=0$, so a
   zero of $\kappa$ is the first actual content copy after the frozen
   normalization.
3. Every $j\ge1$ row under (1.1) lies in the Item-149 rank-one overlap.
   Here $b_{m,p}=1$, and Item 149 has already booked that first
   post-$G_m$ copy.  A zero of $\kappa$ is a further post-booking
   depth, not a second label for the booked copy.

Thus the support of (1.7) is arithmetically meaningful in both parts, but
its interpretation differs.  Multiplying the ordinary $F_m$ factor,
the Item-149 factor, and a $\kappa$-zero radical without this partition
would double count.

## 3. Exact cellwise construction of $\kappa$

Put



$$
a=3j+1,
 \qquad c=2j+1,
 \qquad F_j=\frac{u^a}{Q^c}.                            \tag{3.1}
$$



Then the original rows factor as



$$
\omega_\nu=F_j^pP_{\nu,s}\,dx.                        \tag{3.2}
$$



The degree bounds are



$$
\deg P_{0,s}=p-3,
 \qquad \deg P_{1,s}=p-6,                               \tag{3.3}
$$



so the primitive in (1.6) exists uniquely over $\mathbb F_p$.
Differentiate $F_j$ and define



$$
D_j=a u'Q-cQ'u
 =(3j+1)-(5j+2)(x+x^2+x^3)+x^4.                        \tag{3.4}
$$



Set $N_\nu=T_\nu D_j$.  For $0\le n\le4$, define the exact
four-sections



$$
h_{\nu,n}
 =\sum_{z=0}^{p-1}[x^{pn-4z}]N_\nu,
 \qquad
 H_\nu(x)=\sum_{n=0}^4h_{\nu,n}x^n.                    \tag{3.5}
$$



Terms with a negative exponent in (3.5) are zero.  In particular
$H_\nu(0)=0$.  At every fourth root of unity $\zeta$,



$$
H_\nu(\zeta^p)=D_j(\zeta)T_\nu(\zeta).                \tag{3.6}
$$



The leading Cartier/Bockstein differential is



$$
\Phi_\nu
 =\frac{u^{3j}H_\nu}{Q^{2j+2}}\,dx.                   \tag{3.7}
$$



Let



$$
\mathcal E_j(H)=(R_j(H),L_j(H),E_j(H))                 \tag{3.8}
$$



be the exact mixed-cubic endpoint map of (3.7).  Combining the
four-section leading-gate theorem of Item 194 with Item 424's integral
bridge identifies the rational-log minor without a unit ambiguity and
proves (1.7).

This is an actual-family formula.  The parameters in (1.4)--(1.6) are the
ones forced by $(m,p)$; no ambient period has been added.

## 4. A deterministic Hermite recurrence for $\mathcal E_j$

Formula (1.7) is finite and exact because $\mathcal E_j$ has the
following recurrence.  Put



$$
J(x)=(Q'(x))^{-1}\pmod Q
 =-\frac{x}{4}+\frac{x^2}{4}.                            \tag{4.1}
$$



Start with



$$
M_{2j+2}=u^{3j}H.                                      \tag{4.2}
$$



For $k=2j+2,\ldots,2$, define



$$
r_k=M_k\bmod Q,
 \qquad
 a_k=-\frac{Jr_k}{k-1}\bmod Q,                         \tag{4.3}
$$



and



$$
M_{k-1}
 =\frac{M_k-a_k'Q+(k-1)a_kQ'}{Q}.                      \tag{4.4}
$$



The numerator in (4.4) is divisible by $Q$.  Condition (1.1) implies
$2j+2<p$, so every $k-1$ and the factor four in (4.1) are units.

At each level, add



$$
\frac{a_k(1)}{4^{k-1}}-a_k(0)                         \tag{4.5}
$$



to the rational endpoint coordinate.  Finally write



$$
M_1=qQ+(b_0+b_1x+b_2x^2).                              \tag{4.6}
$$



Then



$$
\begin{aligned}
 R_j(H)&=\sum_{k=2}^{2j+2}
 \left(\frac{a_k(1)}{4^{k-1}}-a_k(0)\right)
 +\int_0^1q(x)\,dx,\\
 L_j(H)&=b_0-b_1+3b_2,\\
 E_j(H)&=b_0+b_1-b_2.
\end{aligned}                                           \tag{4.7}
$$



Equations (3.5) and (4.1)--(4.7) are the promised cellwise exact
recurrence for $\kappa$.

### The explicit $j=0$ cell

When $j=0$, write



$$
H=h_1x+h_2x^2+h_3x^3+h_4x^4.
$$



One Hermite step gives



$$
\boxed{
 R_0(H)=\frac{h_2-h_3}{4},
 \qquad
 L_0(H)=\frac{-h_1+h_3-2h_4}{2}.}                      \tag{4.8}
$$



Consequently the full positive-capacity unbooked cell has the explicit
gate



$$
\boxed{
\begin{aligned}
8\kappa_{m,p}={}&
(-h_{1,1}+h_{1,3}-2h_{1,4})(h_{0,2}-h_{0,3})\\
&-(-h_{0,1}+h_{0,3}-2h_{0,4})(h_{1,2}-h_{1,3})
\pmod p.
\end{aligned}}                                         \tag{4.9}
$$



The indices before the comma label $\nu$; those after it label the
four-section.  Formula (4.9) is exact for every $j=0$ row, including
the known zero $(m,p)=(9,47)$.  It is not a universal nonvanishing
formula.

## 5. Uniform recurrence in the actual tied step

Fix $(p,j,\nu)$ and one admissible phase of $s$.  The integrands obey



$$
P_{\nu,s+2k}
 =P_{\nu,s}\frac{Q^{4k}}{u^{6k}}.                       \tag{5.1}
$$



Assume $r\ge24$, equivalently that all five rows
$s,s+2,\ldots,s+8$ remain polynomial rows.  Put



$$
e=2s-\nu.                                               \tag{5.2}
$$



Seek $A(x)\in\mathbb F_p[x]$, $\deg A\le44$, and
$(c_0,\ldots,c_4)\in\mathbb F_p^5$ satisfying



$$
\begin{aligned}
 \sum_{k=0}^4c_kQ^{4k}u^{6(4-k)}
 ={}&uQA'\\
 &+\{u(e+1)Q'+(r-23)Qu'\}A.
\end{aligned}                                           \tag{5.3}
$$



Both sides have degree at most $48$.  Equation (5.3) therefore gives
49 homogeneous linear equations in 50 unknowns, so a nonzero solution
always exists.

Crucially, the five $c_k$'s cannot all vanish.  If they did, (5.3)
would say



$$
\frac{d}{dx}\left(Au^{r-23}Q^{e+1}\right)=0.           \tag{5.4}
$$



The polynomial inside the derivative has degree at most



$$
44+2(r-23)+3(e+1)=p-2-3\nu<p.                         \tag{5.5}
$$



In characteristic $p$, a polynomial of degree below $p$ with zero
derivative is constant.  Since $r-23\ge1$, it vanishes at $x=0$;
it is therefore zero, forcing $A=0$, a contradiction.

Divide (5.3) by $u^{24}$, multiply by $P_{\nu,s}$, and use (5.1).
This yields the exact telescoping identity



$$
\boxed{
 \sum_{k=0}^4c_kP_{\nu,s+2k}
 =\frac{d}{dx}
 \left(\frac{QA}{u^{23}}P_{\nu,s}\right).}             \tag{5.6}
$$



The primitive on the right is



$$
Au^{r-23}Q^{e+1}.                                      \tag{5.7}
$$



It vanishes at $0,1,-1,i,-i$.  Integrating (5.6) from zero to each
fourth root of unity proves



$$
\boxed{
 \sum_{k=0}^4c_kT_{\nu,s+2k}(\zeta)=0
 \qquad(\zeta^4=1).}                                   \tag{5.8}
$$



By (3.6), the same recurrence holds for the four-section values and hence
for every coordinate in (4.7).  The two values of $\nu$ have different
coefficient vectors, so $\kappa$ belongs to the resulting bilinear
finite-state system; (5.8) is not a scalar nonvanishing theorem for it.

## 6. Capacity localization

### 6.1 The recurrence boundary is zero-rate

For every terminal row $0\le r<24$, equation (1.5) gives



$$
p\mid6m-r.                                              \tag{6.1}
$$



At fixed $m$, multiply over the distinct primes arising from all cells.
For each fixed $r$, their product divides $|6m-r|$.  Therefore



$$
\sum_{\substack{p\in\mathcal P_m\\0\le r<24}}\log p
 \le\sum_{r=0}^{23}\log|6m-r|
 =O(\log m),                                             \tag{6.2}
$$



which proves (1.9).  Thus the recurrence covers the entire
positive-linear capacity; its missing terminal rows cannot affect an
exponent ledger.

### 6.2 Exact capacity of each cell

The $j$-th prime interval is



$$
\frac4{2j+1}<\frac pm<\frac6{3j+1}.                    \tag{6.3}
$$



Its normalized raw first-Witt capacity is exactly



$$
\boxed{
 C_j=\frac{1}{6}
 \left(\frac6{3j+1}-\frac4{2j+1}\right)
 =\frac1{3(3j+1)(2j+1)}.}                               \tag{6.4}
$$



Hence



$$
C_0=\frac13,                                           \tag{6.5}
$$



and



$$
\sum_{j\ge1}C_j=\frac{\mathfrak C_F-2}{6}.            \tag{6.6}
$$



For $J\ge2$,



$$
\sum_{j\ge J}C_j
 \le\frac1{18}\sum_{j\ge J}\frac1{j^2}
 \le\frac1{18(J-1)}.                                   \tag{6.7}
$$



Thus any future finite-cell theorem can be converted immediately into a
rigorous global capacity bound, with (6.7) controlling the unresolved
tail.

## 7. Why this is not yet weighted zero density

The exact recurrence removes two sources of ambiguity:

* $\kappa$ is now a determinant of four explicitly generated finite-
  field periods, not an implicit quotient of large rational endpoints;
* the parity-compatible moving family has bounded recurrence order outside
  a zero-rate terminal band.

But neither fact bounds isolated zeros.  Even a nonsingular recurrence of
order two over a finite field can have zeros on a positive proportion of
its indices.  To deduce



$$
\sum_{\substack{p\in\mathcal P_m\\\kappa_{m,p}=0}}
 \log p=o(m),                                           \tag{7.1}
$$



one still needs a nonconcentration input: for example, a Frobenius-trace
interpretation with controlled monodromy, a resultant whose prime support
is subexponential, or a cellwise zero theorem strong enough to combine
with (6.4)--(6.7).

Accordingly, Item 426 does not reduce (1.10) or (1.11).  Its strategic
result is a precise handoff: future work should study the order-four
period system or the explicit $j=0$ determinant (4.9), not recompute
global Hermite endpoints one row at a time.

## 8. Ledger effect

The exact delta is



$$
\boxed{
 \Delta C_{\le}=0,
 \quad\Delta r_{\rm booked}=0,
 \quad\Delta C_{\rm global}=0,
 \quad\Delta(T-r_1)=0.}                                 \tag{8.1}
$$



The zero-rate statement (1.9) localizes the recurrence boundary; it does
not exclude any positive-capacity interior $\kappa$-zero support.

## 9. Strict claim ledger

### PROVED

* The exact cell determinant (1.7) and finite Hermite recurrence
  (3.5), (4.1)--(4.7).
* The explicit full $j=0$ gate (4.9).
* The uniform nonzero actual-step telescoper (5.3)--(5.8) for $r\ge24$.
* Zero logarithmic capacity of the terminal $r<24$ band.
* The exact cell capacities (6.4) and tail bound (6.7).
* Correct separation of ordinary $F_m$, Item-149 overlap, and the new
  gate, with zero booking.

### EXACT FINITE ONLY

The replay checks every eligible row through $m=60$: 749 incidences,
13 $\kappa$-zeros, and exact agreement between (1.7) and Item 424.
It also constructs six exact recurrence witnesses in three actual cells.
These counts are diagnostic only.

### OPEN

* Weighted zero density or positive density for $\kappa$.
* A monodromy, resultant, or nonconcentration theorem for (5.8).
* Uniform control of deeper Witt digits after $\kappa=0$.
* Route-1 completion and irrationality of $e+\pi$.

### NOT CLAIMED

* That bounded recurrence order implies few zeros.
* A reduced first-Witt ceiling or a new divisor lower bound.
* Any extrapolation from the finite census.
* Route-1 closure or an irrationality proof.

## 10. Deterministic replay

Run

```text
python work/item426_witt_cell_recurrence_certificate.py \
  --output work/item426_witt_cell_recurrence_certificate.replay.json \
  --replay work/item426_witt_cell_recurrence_certificate.json
```

The standard-library replay:

1. pins Items 200, 418, and 424 plus the Item-149 source theorem;
2. reconstructs (3.5) and the Hermite map on every declared finite row;
3. compares (1.7) with the independently normalized Item-424 value;
4. verifies the explicit $j=0$ formula;
5. constructs the $49\times50$ systems and verifies (5.3), (5.6), and
   endpoint recurrences in representative actual cells; and
6. reproduces all capacity constants and overlap labels.

All artifacts remain under `work/item426_*`; no canonical or central file
is edited.
