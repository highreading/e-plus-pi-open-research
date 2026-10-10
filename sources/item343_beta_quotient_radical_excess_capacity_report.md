> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 343 — quotient-lift saturation and the radical/excess beta split

Checked: 2026-09-01 (Beijing time)

## 1. Strict verdict

Assume the actual Item-316 target.  Retain Item 340's notation



$$
T+\epsilon R=bt,
\qquad
Q\mid b,
\tag{1.1}
$$



where $Q$ is a declared target divisor after all previously booked
denominator factors have been removed.  Retain Item 337's primitive
cofactor lcm $\Lambda$ and put



$$
G_Q=\gcd(Q,\Lambda),
\qquad
H_Q=\gcd(G_Q,t),
\qquad
K_Q=G_Q/H_Q.
\tag{1.2}
$$



Thus



$$
\Gamma_Q=\log G_Q=\log H_Q+\log K_Q.
\tag{1.3}
$$



Item 343 gives the requested global valuation-excess theorem for $K_Q$.
It treats $\Lambda$ as one overlap-normalized integer and does not return
to individual local cofactors.

For a positive integer $N$, define



$$
E(N)=\frac{N}{\operatorname{rad}(N)},
\qquad
\operatorname{sqfull}(N)
=\prod_{v_p(N)\ge2}p^{v_p(N)}.
\tag{1.4}
$$



When $Q>1$, put



$$
M_Q=\left\lceil\log_2Q\right\rceil,
\qquad
G_Q^\perp
=\frac{G_Q}{\gcd(G_Q,t^{M_Q})},
\qquad
R_Q^\perp=\operatorname{rad}(G_Q^\perp).
\tag{1.5}
$$



The case $Q=1$ is trivial and has zero mass.

> **PROVED — QUOTIENT RADICAL/EXCESS THEOREM.**  There is an exact
> integer $J_Q$ such that
>
> 

$$
> \boxed{
> K_Q=R_Q^\perp J_Q,
> \qquad
> J_Q\mid E(Q).}
> \tag{1.6}
>
$$


>
> Moreover
>
> 

$$
> \boxed{
> R_Q^\perp
> =\prod_{\substack{p\mid Q,\ p\mid\Lambda\\p\nmid t}}p.}
> \tag{1.7}
>
$$



Consequently, with



$$
\Xi_Q:=\log R_Q^\perp
=\sum_{\substack{p\mid Q,\ p\mid\Lambda\\p\nmid t}}\log p,
\tag{1.8}
$$



one has the global capacity bound



$$
\boxed{
\log K_Q
\le\Xi_Q+\log E(Q)
\le\Xi_Q+\log\operatorname{sqfull}(Q)
\le\Xi_Q+\log\operatorname{sqfull}(b).}
\tag{1.9}
$$



This separates two fundamentally different mechanisms.

1. Every repeated valuation in $K_Q$, including all $K_Q$-mass on
   primes which divide the quotient $t$, lies in the already identified
   squarefull/excess barrier $E(Q)$.
2. The only possible new squarefree layer is $R_Q^\perp$.  Its primes
   divide the target and the global cofactor lcm but explicitly do **not**
   divide $t$.

The quotient lift saturates completely at every precision.  For every
integer $s\ge1$ and every integer $\ell$,



$$
\boxed{
t\equiv\ell\pmod{Q^s}
\iff
T+\epsilon R\equiv b\ell\pmod{bQ^s}.}
\tag{1.10}
$$



Thus the entire tower of $bQ^s$-lifts is exactly the one scalar
$t\in\mathbb Z_Q$.  It cannot see a new vanishing layer on the primes in
$R_Q^\perp$, because $t$ is a unit at every one of those primes.

Equation (1.9) is a rigorous capacity reduction of the **form** of the
open problem, but not a numerical beta reduction.  Item 265 leaves
$\log\operatorname{sqfull}(Q)=o(\log b)$ open, and no theorem here
proves $\Xi_Q=o(\log b)$.  Both terms can retain full theoretical
one-target scale under the current bounds.

The exact three-part ledger is



$$
\boxed{
\Gamma_Q
=\log H_Q+\Xi_Q+\log J_Q,
\qquad
J_Q\mid E(Q).}
\tag{1.11}
$$



The quotient-covered part $H_Q$ is already a subfactor of
$G_Q$; it is not an additional copy.  The genuinely new target-specific
question left by the quotient analysis is the weighted zero density of the
$t$-avoiding radical hits $\Xi_Q$, together with the old squarefull
barrier.

No new capacity is booked.

## 2. Primewise form of $H_Q$ and $K_Q$

For a prime $p$, write



$$
q_p=v_p(Q),
\qquad
g_p=v_p(G_Q)
=\min\{v_p(Q),v_p(\Lambda)\},
\qquad
\tau_p=v_p(t).
\tag{2.1}
$$



Then exactly



$$
v_p(H_Q)=\min\{g_p,\tau_p\},
\tag{2.2}
$$



and



$$
\boxed{
v_p(K_Q)
=g_p-\min\{g_p,\tau_p\}
=\max\{0,g_p-\tau_p\}.}
\tag{2.3}
$$



This identity already prevents a common accounting error.  The raw
quotient overlap



$$
C_Q:=\log\gcd(Q,t)
\tag{2.4}
$$



is not an independent gain.  Only $H_Q$ is shared simultaneously with
the cofactor target, and



$$
H_Q\mid\gcd(Q,t),
\qquad
H_Q\mid G_Q.
\tag{2.5}
$$



Primes or valuations in $C_Q$ which are absent from $G_Q$ have no
logical connection to the original cofactor collision.  Adding $C_Q$
to $\Gamma_Q$ would double-count $H_Q$ and count irrelevant quotient
content.

## 3. Exact saturation of quotient support

Suppose $Q>1$.  If $p^{q_p}\mid Q$, then



$$
q_p\le\log_2Q\le M_Q.
\tag{3.1}
$$



If $p\mid t$, then



$$
v_p(t^{M_Q})=M_Q\tau_p\ge M_Q\ge q_p\ge g_p.
\tag{3.2}
$$



If $p\nmid t$, the same valuation is zero.  Therefore



$$
v_p\!\left(\gcd(G_Q,t^{M_Q})\right)
=
\begin{cases}
g_p,&p\mid t,\\
0,&p\nmid t.
\end{cases}
\tag{3.3}
$$



It follows that



$$
\boxed{
G_Q^\perp
=\prod_{\substack{p\mid G_Q\\p\nmid t}}p^{g_p},
\qquad
\gcd(G_Q^\perp,t)=1.}
\tag{3.4}
$$



Taking the radical proves (1.7).  The exponent $M_Q$ is used only to
write the support projection without factoring; no artificial power of
$t$ is booked as a new arithmetic object.

## 4. Proof of the radical/excess theorem

Define



$$
J_Q:=K_Q/R_Q^\perp.
\tag{4.1}
$$



This is an integer.  Indeed, if $p\mid R_Q^\perp$, then
$g_p\ge1$ and $\tau_p=0$, so (2.3) gives
$v_p(K_Q)=g_p\ge1$.

It remains to bound the exponent of $J_Q$.  There are two cases.

* If $\tau_p=0$ and $g_p>0$, then one radical copy is removed and
  
  

$$
v_p(J_Q)=g_p-1\le q_p-1.
  \tag{4.2}
$$



* If $\tau_p>0$, then $R_Q^\perp$ has no $p$-factor and
  
  

$$
v_p(J_Q)
  =\max\{0,g_p-\tau_p\}
  \le\max\{0,g_p-1\}
  \le\max\{0,q_p-1\}.
  \tag{4.3}
$$



But



$$
v_p(E(Q))=\max\{0,q_p-1\}.
\tag{4.4}
$$



Equations (4.2)-(4.4) prove



$$
J_Q\mid E(Q),
\tag{4.5}
$$



and hence (1.6).

Item 265 proves primewise



$$
E(Q)\mid\operatorname{sqfull}(Q).
\tag{4.6}
$$



Since $Q\mid b$, one also has



$$
\operatorname{sqfull}(Q)
\mid\operatorname{sqfull}(b).
\tag{4.7}
$$



Taking logarithms proves (1.9).

## 5. Exact all-precision quotient-lift saturation

Put



$$
N=T+\epsilon R=bt.
\tag{5.1}
$$



For every $s\ge1$ and integer $\ell$,



$$
\begin{aligned}
N\equiv b\ell\pmod{bQ^s}
&\iff b(t-\ell)\equiv0\pmod{bQ^s}\\
&\iff Q^s\mid t-\ell.
\end{aligned}
\tag{5.2}
$$



This proves (1.10).  Passing through all $s$ gives no tower of
independent target conditions: it gives the single $Q$-adic integer
$t$.

At a prime contributing to $R_Q^\perp$, one has $v_p(t)=0$.
Every quotient lift therefore sees a unit.  It supplies no divisibility
layer which could cover the one radical copy in (1.7).  Conversely, at a
prime dividing $t$, any $K_Q$-valuation beyond the available
$v_p(t)$ is bounded by the repeated-prime factor $E(Q)$ through
(4.3).

This proves the scoped information statement:



$$
\boxed{
\begin{array}{c}
\text{all }bQ^s\text{ quotient lifts}\\
\Downarrow\\
\text{the exact scalar }t\\
\Downarrow\\
\text{no new }K_Q\text{ radical support;}\\
\text{supported excess lies in }E(Q).
\end{array}}
\tag{5.3}
$$



The theorem does not say that $R_Q^\perp=1$.  It says that proving
otherwise, or bounding it, is a genuinely transverse cofactor/quotient
support problem rather than another digit of the same quotient lift.

## 6. Exact corollaries and admission decision

### 6.1 Squarefree target

If $Q$ is squarefree, then $E(Q)=1$, so (1.6) becomes



$$
\boxed{K_Q=R_Q^\perp,
\qquad
\log K_Q=\Xi_Q.}
\tag{6.1}
$$



Thus the full valuation-excess problem on a squarefree target is exactly a
weighted support-avoidance problem.

### 6.2 Complete quotient support

If every prime dividing $G_Q$ also divides $t$, then
$R_Q^\perp=1$ and



$$
\boxed{K_Q\mid E(Q).}
\tag{6.2}
$$



If $Q$ is additionally squarefree, then



$$
\boxed{K_Q=1.}
\tag{6.3}
$$



### 6.3 Conditional zero-rate closure

If an actual-family theorem proves both



$$
\Xi_Q=o(\log b)
\tag{6.4}
$$



and



$$
\log\operatorname{sqfull}(Q)=o(\log b),
\tag{6.5}
$$



then (1.9) gives



$$
\boxed{\log K_Q=o(\log b).}
\tag{6.6}
$$



Equation (6.5) is the existing Item-265 high-singleton/squarefull barrier,
not a new Item-343 obligation.  After that old branch is removed, the only
new lemma needed for $K_Q$ is (6.4).

The raw upper bounds remain



$$
0\le\Xi_Q\le\log\operatorname{rad}(Q)\le\log Q,
\tag{6.7}
$$



and



$$
0\le\log E(Q)\le\log Q.
\tag{6.8}
$$



Thus Item 343 does not prove a numerical strict fraction.  It proves that
positive-linear $K_Q$-mass must enter through one of two already explicit
doors: the old squarefull barrier or the new $t$-avoiding radical
correlation.  No third quotient-lift reservoir remains.

## 7. Ledger and non-duplication

Combining (1.3) and (1.6) gives the exact ledger



$$
\Gamma_Q
=\log H_Q+\Xi_Q+\log J_Q,
\qquad
J_Q\mid E(Q).
\tag{7.1}
$$



Its interpretation is rigid.

* $H_Q$ is the quotient-covered portion of the already admitted
  cofactor mass.  It is not additive to $\Gamma_Q$.
* $\log J_Q$ is repeated-prime-power mass already governed by the
  Item-265 squarefull branch.  It cannot be booked again.
* $\Xi_Q$ is the only new squarefree support question.  Every prime it
  counts avoids $t$, so it is not carried by the quotient lift.

Therefore the quotient lift can still have positive raw overlap
$\log\gcd(Q,t)$, but after exact cross-mechanism de-overlap it supplies
no independent positive-linear copy.  Its strategic value is diagnostic:
it removes all but $\Xi_Q$ and the old squarefull barrier from the
$K_Q$ decision.

## 8. Strict labels

### PROVED

* The primewise identities (2.2)-(2.3).
* The exact support saturation (3.3)-(3.4).
* The radical/excess factorization
  $K_Q=R_Q^\perp J_Q$ with $J_Q\mid E(Q)$.
* The global capacity bound (1.9).
* The all-precision quotient equivalence (1.10).
* The exact three-part ledger (1.11).
* The squarefree, complete-support, and conditional zero-rate corollaries.

### PROVED SCOPED NO-GO

* Repeating the same quotient lift through arbitrary $bQ^s$ precision
  yields only the one scalar $t$, not independent target conditions.
* Quotient-supported $K_Q$-excess lies in the old squarefull branch.
* The only new squarefree $K_Q$-support explicitly avoids $t$ and
  cannot be credited to the quotient lift.
* This does not prove that the avoiding support has zero density.

### EXACT FINITE ONLY

* The deterministic replay's declared integer valuation tuples and seed
  control rows for support saturation, radical/excess factorization, and
  all-precision quotient congruences.
* No bounded row is promoted to an actual-family density or capacity
  theorem.

### OPEN

* The actual sizes of $H_Q$, $\Xi_Q$, $J_Q$, and $\Gamma_Q$.
* The weighted zero-density theorem $\Xi_Q=o(\log b)$.
* Item 265's squarefull/high-singleton theorem.
* The Item-316 centered half-bound and original all-digit exclusion.
* Every numerical beta capacity reduction, Route 1, and every conclusion
  about $e+\pi$.

### BOOKING



$$
\boxed{
\text{new beta capacity reduction}=0,
\qquad
\text{new Route-1 rate}=0.}
\tag{8.1}
$$



No canonical, master, status, checkpoint, or research-log file is edited
by this work package.

## 9. Deterministic replay

From the archive root:

~~~text
python work/item343_beta_quotient_radical_excess_capacity_certificate.py ^
  --output work/item343_beta_quotient_radical_excess_capacity_certificate.replay.json
~~~

The checker uses only the Python standard library and exact integer
arithmetic.  It performs no half-bound, prime, or target census and
promotes no bounded row.
