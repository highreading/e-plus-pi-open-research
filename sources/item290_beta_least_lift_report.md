> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 290 — exact least-lift reduction for the full beta target

Checked: 2026-08-31 (Beijing time)

## 1. Verdict

Retain



$$
q_0=q_1=1,\qquad q_{n+2}=(4n+6)q_{n+1}+q_n.            \tag{1.1}
$$



For the full beta target define



$$
\rho_n:=\min_{k\in\mathbb Z}
\left|q_{n+1}^{\,2}-kq_n\right|.                       \tag{1.2}
$$



This is exactly the minimum absolute coefficient of a monic linear
annihilator for the Item-285 boundary unit



$$
u_n=-q_{n+1}^{\,2}\pmod {q_n}.                         \tag{1.3}
$$



The all-$n$ Euclidean and continuant description is exact.
For $n\ge2$, put



$$
a=q_{n-1},\qquad b=q_n,\qquad c=q_{n-2},\qquad
A=4n-2.                                                \tag{1.4}
$$



Then



$$
q_{n+1}\equiv a\pmod b,\qquad b=Aa+c.                 \tag{1.5}
$$



Because every $q_n$ is odd, there is a unique centered quotient



$$
\boxed{
\kappa_n=
\left\lfloor{2a^2+b\over2b}\right\rfloor}              \tag{1.6}
$$



and signed centered remainder



$$
\boxed{
r_n=a^2-\kappa_nb,\qquad
-{b\over2}<r_n<{b\over2},\qquad
\rho_n=|r_n|.}}                                        \tag{1.7}
$$



Equivalently, $r_n$ is the unique centered representative and



$$
\rho_n=\min_{\ell\in\mathbb Z}|r_n-\ell b|=|r_n|.       \tag{1.8}
$$



Define



$$
h_n=a-A\kappa_n.                                       \tag{1.9}
$$



One Euclidean step gives the exact determinant



$$
\boxed{
r_n=ah_n-c\kappa_n.}                                   \tag{1.10}
$$



The same identity in the original modulus coordinates is



$$
\boxed{
A r_n=bh_n-ac.}                                        \tag{1.10a}
$$



Since $\kappa_n\in\mathbb Z$ is equivalent to
$h_n\equiv a\pmod A$, this gives the exact constrained minimum



$$
\boxed{
\rho_n={1\over A}
\min_{\substack{h\in\mathbb Z\\h\equiv a\;(\mathrm{mod}\ A)}}
|bh-ac|.}                                              \tag{1.10b}
$$



For $\kappa_n>0$,



$$
\boxed{
\rho_n
=a\kappa_n
\left|{h_n\over\kappa_n}-{c\over a}\right|.}           \tag{1.11}
$$



The continuant word is also explicit:

Here and below there is one boundary convention: for $n=2$, the
ascending word is $(7)$ and the descending word is also $(7)$.
Thus (1.12) means $q_2=K(7)$, and (1.13) means
$q_1/q_2=[0;7]$.  For $n\ge3$, the arithmetic lists displayed in
(1.12)--(1.13) are literal.



$$
\boxed{
q_n=K(7,10,14,\ldots,4n-2),}                           \tag{1.12}
$$





$$
\boxed{
{q_{n-1}\over q_n}
=[0;4n-2,4n-6,\ldots,10,7].}                          \tag{1.13}
$$



Thus the degree-one question is reduced exactly to the centered
determinant (1.10) for one descending arithmetic-progression word.

No valid all-$n$ estimate of either required kind was found:

* an admissible lift would require
  

$$
\log\rho_n=O(n);                                     \tag{1.14}
$$


* exclusion of every $O(n)$-height linear lift would follow, for
  example, from
  

$$
{\log\rho_n\over n}\longrightarrow\infty,            \tag{1.15}
$$


  and in particular from a bound
  $\rho_n\ge\exp(cn\log n)$.

The exact reduction alone proves only



$$
1\le\rho_n\le{q_n-1\over2}.                            \tag{1.16}
$$



Moreover, generic continuant size arguments cannot improve the lower
bound $1$: palindromic positive continued-fraction words of arbitrary
length and arbitrarily large entries have numerator square congruent to
$\pm1$ modulo their denominator.

The beta word in (1.13) is not palindromic.  A stronger result may still
follow from its exact arithmetic-progression asymmetry.  That specific
step remains open and is not replaced by finite extrapolation.

For a proper de-overlapped target $Q\mid q_n$, the least lift is the
centered reduction of $r_n$ modulo $Q$.  Hence a full-target upper
bound transfers to every proper target, while a full-target lower bound
does not.  The Item-282 product baseline remains separate.  Booking is
zero.

## 2. Continuant and continued-fraction formula

Use the ordinary continuant normalization



$$
K(\varnothing)=1,\qquad K(x_1)=x_1,                   \tag{2.1}
$$





$$
K(x_1,\ldots,x_t)
=x_tK(x_1,\ldots,x_{t-1})
+K(x_1,\ldots,x_{t-2}).                               \tag{2.2}
$$



Starting with $q_1=1$ and $q_2=7$, recurrence (1.1) gives



$$
q_3=10q_2+q_1,\qquad
q_4=14q_3+q_2,
$$



and generally



$$
q_n=(4n-2)q_{n-1}+q_{n-2}.                            \tag{2.3}
$$



For $n=2$, define the continuant word to be $W_2=(7)$.  For
$n\ge3$, define



$$
W_n=(7,10,14,\ldots,4n-2).
$$



Equations (2.1)–(2.3) prove by induction



$$
q_n=K(7,10,14,\ldots,4n-2),                           \tag{2.4}
$$



which is (1.12).

For a positive word $w=(x_1,\ldots,x_t)$,



$$
\begin{pmatrix}x_1&1\\1&0\end{pmatrix}
\cdots
\begin{pmatrix}x_t&1\\1&0\end{pmatrix}
=
\begin{pmatrix}
K(x_1,\ldots,x_t)&K(x_1,\ldots,x_{t-1})\\
K(x_2,\ldots,x_t)&K(x_2,\ldots,x_{t-1})
\end{pmatrix}.                                        \tag{2.5}
$$



Apply (2.5) to the reversed word



$$
w_n=(4n-2,4n-6,\ldots,10,7).                          \tag{2.6}
$$



At the boundary $n=2$, (2.6) means $w_2=(7)$, the reversal of
$W_2$; for $n\ge3$ it is the literal descending list shown.

Continuant reversal symmetry gives



$$
K(w_n)=q_n,\qquad K(4n-6,\ldots,10,7)=q_{n-1}.         \tag{2.7}
$$



The standard numerator/denominator formula for a finite continued
fraction now gives (1.13).

This is an all-$n$ identity, not a fitted recurrence or a finite
pattern.

## 3. Centered remainder and degree-one equivalence

From (1.1),



$$
q_{n+1}=(4n+2)q_n+q_{n-1}.                            \tag{3.1}
$$



Therefore



$$
q_{n+1}^2\equiv q_{n-1}^2=a^2\pmod b.                 \tag{3.2}
$$



All $q_n$ are odd: the recurrence coefficient is even and the two
initial values are odd.  Hence no residue class modulo $b$ has two
representatives of absolute value $b/2$.  The nearest integer to
$a^2/b$ is exactly (1.6), and (1.7) follows.

Adjacent recurrence terms are coprime:



$$
\gcd(q_n,q_{n-1})
=\gcd(q_{n-1},q_{n-2})
=\cdots=1.                                             \tag{3.3}
$$



Consequently,



$$
\gcd(r_n,b)=\gcd(a^2,b)=1,                             \tag{3.4}
$$



so $r_n\ne0$.  This proves (1.16).

Every integer lift of the boundary unit (1.3) has the form



$$
v=-r_n+\ell b,\qquad \ell\in\mathbb Z.                 \tag{3.5}
$$



The centered choice $v=-r_n$ has minimum absolute value
$\rho_n$.

A monic linear polynomial



$$
M(U)=U+\alpha                                          \tag{3.6}
$$



annihilates $u_n$ modulo $b$ if and only if



$$
\alpha\equiv q_{n+1}^2\equiv r_n\pmod b.               \tag{3.7}
$$



Thus its minimum possible coefficient magnitude is also $\rho_n$.
Equivalently,



$$
\boxed{
\min_M\log\max(1,|\alpha|)
=\log\rho_n,}                                         \tag{3.8}
$$



where the minimum is over all monic linear annihilators modulo $q_n$.
This is the exact Item-285 admission equivalence.

## 4. One-step Euclidean determinant

Equation (2.3) is



$$
b=Aa+c,\qquad 0<c<a.                                  \tag{4.1}
$$



It immediately gives



$$
{a\over A+1}
<{a^2\over b}
<{a\over A}.                                          \tag{4.2}
$$



Let $\kappa_n$ be the nearest integer in (1.6), and put



$$
h_n=a-A\kappa_n.
$$



Then



$$
\begin{aligned}
r_n
&=a^2-\kappa_n(Aa+c)\\
&=a(a-A\kappa_n)-c\kappa_n\\
&=ah_n-c\kappa_n,
\end{aligned}                                          \tag{4.3}
$$



proving (1.10).

Multiplying (4.3) by $A$, and using
$A\kappa_n=a-h_n$, gives



$$
\begin{aligned}
A r_n
&=Aah_n-Ac\kappa_n\\
&=(Aa+c)h_n-ac\\
&=bh_n-ac.
\end{aligned}                                          \tag{4.3a}
$$



Conversely, every $h\equiv a\pmod A$ has the form
$h=a-A\kappa$ for a unique $\kappa\in\mathbb Z$.
Minimizing (4.3a) over that arithmetic progression proves (1.10b).

There are two equivalent rational-approximation forms:



$$
\boxed{
\left|{a\over b}-{\kappa_n\over a}\right|
={\rho_n\over ab},}                                    \tag{4.4}
$$



and, when $\kappa_n>0$,



$$
\boxed{
\left|{c\over a}-{h_n\over\kappa_n}\right|
={\rho_n\over a\kappa_n}.}                             \tag{4.5}
$$



Thus $\rho_n$ is an exact cross-determinant between two rational
approximants tied by the new leading partial quotient $A=4n-2$.

Ordinary rational separation applied to either equation gives only



$$
\rho_n\ge1.                                           \tag{4.6}
$$



Legendre's convergent criterion is also too weak for the desired
scale: its standard $1/(2a^2)$ threshold does not control the
$1/b$-scale interval relevant to (4.4).  A proof of (1.14) or (1.15)
must use more than the generic fact that (1.13) is a continued
fraction.

Equations (4.1)–(4.5) are the exact centered Euclidean description
requested in this item.  Iterating the Euclidean algorithm evaluates
$r_n$ deterministically, but no uniform height estimate follows
merely from executing that finite algorithm.

## 5. A sharp barrier for generic continuant bounds

For an integer $x$, write



$$
T(x)=
\begin{pmatrix}x&1\\1&0\end{pmatrix}.                 \tag{5.1}
$$



Every $T(x)$ is symmetric and has determinant $-1$.
Let



$$
w=(x_1,\ldots,x_t)                                    \tag{5.2}
$$



be a palindrome.  Then



$$
T(x_1)\cdots T(x_t)
$$



is symmetric, because its transpose reverses the word and the reversed
word equals $w$.  Write



$$
T(x_1)\cdots T(x_t)
=
\begin{pmatrix}B&P\\P&C\end{pmatrix}.                 \tag{5.3}
$$



Taking determinants gives



$$
BC-P^2=(-1)^t.                                        \tag{5.4}
$$



Therefore



$$
\boxed{
P^2\equiv(-1)^{t+1}\pmod B.}                           \tag{5.5}
$$



For the rational $[0;w]=P/B$, the least absolute square residue is
exactly $1$.

Palindromic positive words can have arbitrary length and arbitrarily
large partial quotients.  Hence no growing lower bound for a numerator
square residue can follow from:

* positivity of the word;
* its length;
* upper or lower size bounds on its partial quotients; or
* generic continuant product estimates alone.

This is a sharply scoped method barrier.  It does not apply the
palindromic conclusion to the beta word.  The beta word



$$
(4n-2,4n-6,\ldots,10,7)                               \tag{5.6}
$$



has a specific nonpalindromic arithmetic progression, and a theorem
exploiting that exact structure remains possible.

## 6. The observed half-bound is finite only

The deterministic checker includes the exact rows $2\le n\le160$.
On those rows it verifies



$$
2\rho_n\ge q_{n-1}.                                   \tag{6.1}
$$



The smallest checked ratio occurs at $n=4$:



$$
q_3=71,\qquad \rho_4=36,\qquad
2\rho_4-q_3=1.                                        \tag{6.2}
$$



> **EXACT FINITE ONLY.**
> Equations (6.1)–(6.2) are a bounded replay observation.  No all-$n$
> proof is known, and they are not used to infer an asymptotic.

If (6.1) were proved for all sufficiently large $n$, then



$$
\log\rho_n
\ge\log q_{n-1}-\log2
=n\log n+O(n),                                        \tag{6.3}
$$



which would exclude every $O(n)$-height full-target linear lift.
Equation (6.3) is therefore a precise possible target, not a booked
theorem.

## 7. Proper de-overlapped targets

Let



$$
Q\mid\overline q_{m,n}
={q_n\over\gcd(q_n,D_m)}.                              \tag{7.1}
$$



Assume $Q>1$.  Because $q_n$ is odd, $Q$ is odd.  Let



$$
r_{n,Q}
$$



be the unique centered residue of $q_{n+1}^2$ modulo $Q$, and put



$$
\rho_{n,Q}=|r_{n,Q}|.                                  \tag{7.2}
$$



Since



$$
q_{n+1}^2\equiv r_n\pmod {q_n},
$$



and $Q\mid q_n$,



$$
\boxed{
r_{n,Q}=\operatorname{cent}_Q(r_n),\qquad
\rho_{n,Q}
=\min_{\ell\in\mathbb Z}|r_n-\ell Q|.}                 \tag{7.3}
$$



In particular,



$$
\boxed{
1\le\rho_{n,Q}
\le\min\!\left\{\rho_n,{Q-1\over2}\right\}.}            \tag{7.4}
$$



The lower bound follows because



$$
\gcd(q_{n+1},Q)=1,
$$



so the square residue is nonzero.

Equation (7.4) gives the asymmetric transfer:

* if $\log\rho_n=O(n)$ for the full target, then
  $\log\rho_{n,Q}=O(n)$ for every proper target;
* a large lower bound for $\rho_n$ does not imply a lower bound for
  $\rho_{n,Q}$, because centering modulo the smaller $Q$ can reduce
  $r_n$ again.

If



$$
\log Q=O(n),
$$



then (7.4) already supplies an $O(n)$-height lift, but such a target
has zero beta-saddle rate before any new argument.  For a proper target
with



$$
\log Q\asymp n\log n,
$$



an independent estimate for (7.3) is still required.

Thus a full-target lower-bound theorem would close only the full
degree-one route.  It would not rule out useful small lifts on proper
de-overlapped factors.

## 8. Item-282 baseline and capacity

For the nonhomogeneous scalar residual from Item 285, write



$$
\gcd(Q,\mathcal S_n)=G_0X,\qquad
G_0=\gcd(Q,B_n),                                      \tag{8.1}
$$



where $B_n$ is the original common coefficient/product baseline.

The least-lift problem concerns only the additive quotient $X$.
Even an admissible degree-one lift would leave $G_0$ in the Item-282
weighted-return channel.

Item 290 proves neither (1.14) nor (1.15), for the full target or for a
large proper target.  Therefore it gives no actual retained-capacity
ceiling.  The exact reduction identifies the missing arithmetic object
but does not book it.

## 9. Strict labels

### PROVED

* The continuant formula (1.12) and continued fraction (1.13).
* The unique centered quotient/remainder (1.6)–(1.7).
* The identity $q_{n+1}^2\equiv q_{n-1}^2\pmod {q_n}$.
* The degree-one annihilator/lift equivalence and minimum height
  $\log\rho_n$.
* The one-step Euclidean determinant (1.10), the constrained
  progression form (1.10b), and approximation formulas (4.4)–(4.5).
* Coprimality and the exact bounds $1\le\rho_n\le(q_n-1)/2$.
* The palindromic continuant theorem (5.5).
* The proper-target reduction (7.3), asymmetric transfer, and Item-265
  de-overlap.
* Separation from the Item-282 common product baseline.

### PROVED SCOPED METHOD BARRIER

* Generic continued-fraction separation proves only
  $\rho_n\ge1$.
* Positivity, word length, partial-quotient size, and generic
  continuant product estimates cannot yield a growing lower bound,
  because palindromic positive words of arbitrary size have least
  square residue $1$.
* This does not exclude a theorem using the exact beta
  arithmetic-progression word.

### EXACT FINITE ONLY

* The checker replays $2\le n\le160$, including the observed
  $2\rho_n\ge q_{n-1}$ pattern.
* It also checks centered Euclidean determinants, proper-target
  reductions, and explicit palindromic counterfamily rows.
* No exceptional-prime search or asymptotic extrapolation is performed.

### OPEN

* An all-$n$ bound $\log\rho_n=O(n)$.
* Or a lower bound with $\log\rho_n/n\to\infty$, including the
  unproved half-bound suggested by the finite rows.
* An estimate exploiting the exact word
  $(4n-2,4n-6,\ldots,10,7)$.
* The already pinned Item-265 dependency records the equivalent exact
  reverse-Bessel specialization and factorial sum; in the classical
  normalization $q_n=|y_n(-2)|$.  This seed-specific arithmetic,
  absent from the palindromic generic-continuant counterfamily, is the
  natural next input for the progression-word determinant.
* A large proper de-overlapped target residue theorem.
* The Item-282 common product baseline and weighted-return cover.
* Route 1 and every conclusion about $e+\pi$.

### BOOKING



$$
\boxed{
\text{new Route-1 rate}=0,\qquad
\text{new beta capacity reduction}=0.}                 \tag{9.1}
$$



## 10. Deterministic replay

From the archive root:

~~~text
python scripts/item290_beta_least_lift_certificate.py ^
  --output results/item290_beta_least_lift_certificate_replay.json
~~~

The checker is Python-standard-library only, deterministic, and uses
exact integer and continuant-matrix arithmetic.  The canonical result
and replay must be byte-identical.
