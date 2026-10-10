> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 268 — an exact cross-$b$ contiguous relation and its surviving line

Date: 2026-08-31

## 1. Scope and verdict

This item attacks the capacity-relevant stable off-ray subcell isolated in
Item 266.  On an actual rank-one row, write



$$
2M+1=(j+1)p-s,\qquad k=3s+2<p,                       \tag{1.1}
$$





$$
q=\begin{cases}1,&p\ge5s+4,\\2,&p<5s+4,\end{cases}
 \qquad b=qp-5s-4.                                    \tag{1.2}
$$



Let $g_0(s),g_1(s)$ be the two exact common-moving-content integers of
Items 205 and 212.  Thus an admissible prime is an extra common first-gate
prime exactly when



$$
p\mid g_0(s),g_1(s).          \tag{1.3}
$$



The conclusions are:

> **PROVED — maximum affected mass first.**  The phase-preserving step
> $s\mapsto s+1$ sends
> 

$$
> (b,r)\longmapsto(b-5,r+3\bmod4).                    \tag{1.4}
>
$$


> On the far cell $b\ge M/5$, it remains stable for all sufficiently
> large $M$.  The only possible rank failures are
> $p=3s+c$, $c=3,4,5$; their total log weight at fixed $M$ is
> $O(\log M)$.  Therefore the invariant below affects the full far-cell
> coefficient
> 

$$
> C_{\rm far}={1139587\over9085230}
> =0.125432927950\ldots\quad\hbox{per }M               \tag{1.5}
>
$$


> up to zero rate.

> **PROVED — exact adjacent-layer identity.**  Put
> 

$$
> \begin{array}{ll}
> a(s)=75s^2+100s+3,& b_0(s)=6s^2+11s+4,\\
> c(s)=575s^2+1525s+998,&d(s)=46s^2+123s+81.
> \end{array}                                         \tag{1.6}
>
$$


> Then, for every $s\ge0$,
> 

$$
> \boxed{\begin{aligned}
> &16(s+1)(2s+3)\,[a(s)g_0(s)-20b_0(s)g_1(s)]\\
> &\quad+3(3s+4)(3s+5)\,[c(s)g_0(s+1)-20d(s)g_1(s+1)]=0.
> \end{aligned}}                                      \tag{1.7}
>
$$


> This is proved by an explicit constant-term telescoping certificate, not
> guessed from a scan.

> **PROVED — exact phase form.**  On an actual phase, substitute
> $5s\equiv-(b+4)\pmod p$.  With $b'=b-5$, define
> 

$$
> \begin{aligned}
> U_b={}&5(3b^2+4b-29)g_0(s)
>       -4(6b^2-7b-24)g_1(s),\\
> V_{b'}={}&5(23b'^2+109b'+116)g_0(s+1)\\
>          &-4(46b'^2+213b'+216)g_1(s+1).
> \end{aligned}                                       \tag{1.8}
>
$$


> Then
> 

$$
> \boxed{
> 16(b-1)(2b-7)U_b
> +3(3b'+7)(3b'+2)V_{b'}\equiv0\pmod p.}             \tag{1.9}
>
$$


> This is a genuine cross-$b$ relation between adjacent stable phase
> layers.

> **PROVED — sharply scoped rank-one obstruction.**  If (1.3) holds and
> $p\nmid(3s+4)(3s+5)$, then (1.7) forces only
> 

$$
> c(s)g_0(s+1)-20d(s)g_1(s+1)=0\pmod p.              \tag{1.10}
>
$$


> The pair $(c,20d)$ is not identically zero outside the fixed primes
> $2,5,17,23$, because
> 

$$
> \operatorname {Res}_s(c,d)=1564=2^2\cdot17\cdot23. \tag{1.11}
>
$$


> Thus (1.10) is one genuine adjacent line, not two coordinates.  Moreover,
> (1.7) shows that this line is exactly proportional to the current-layer
> linear combination; it is not an independent divisor or a second
> valuation condition.

> **PROVED — uniqueness in the first natural ansatz.**  Among identities
> 

$$
> P_0(s)g_0(s)+P_1(s)g_1(s)+P_2(s)g_0(s+1)
> +P_3(s)g_1(s+1)=0,                                  \tag{1.12}
>
$$


> with $P_i\in\mathbb Q[s]$ and $\deg P_i\le4$, the solution space is
> one-dimensional and is spanned by (1.7).  Hence this natural adjacent
> degree-four module supplies no second row with which to form a nonzero
> $2\times2$ resultant.

> **PROVED — actual-family nonpropagation witness.**  At
> 

$$
> (M,s,p,j,q,b,r)=(2249,299,2399,1,1,900,3),          \tag{1.13}
>
$$


> one has $(g_0,g_1)=(0,0)\pmod{2399}$.  The adjacent stable layer has
> 

$$
> s'=300,\quad b'=895,\quad r'=2,\qquad
> (g_0(300),g_1(300))=(2105,1694)\not=(0,0)           \tag{1.14}
>
$$


> modulo $2399$, while its forced line is
> 

$$
>                         966g_0+128g_1=0\pmod{2399}. \tag{1.15}
>
$$


> It is itself an actual cross-$j$ row:
> $(M',j',s',b')=(3448,2,300,895)$, and both endpoints lie in their
> respective far cells.

> **PROVED, METHOD-SCOPED HEIGHT FAILURE.**  The integer in (1.10) has only
> the inherited exponential bound $\log|V_s|=O(s)$, not polynomial size
> in $s$.  Multiplying it over the moving $s$-layers at fixed $M$
> costs $O(M^2)$, and (1.7) makes its divisibility dependent on the
> current gate anyway.  It gives neither a polynomial-height cross-layer
> integer nor a zero weighted-rate theorem.  This does not rule out a
> higher-degree relation, a nonlinear resultant, a larger cohomological
> state, or a genuinely cancellation-aware invariant.

> **PROVED — Item 149 de-overlap and zero booking.**  Item 149 already books
> the first post-Cartier copy at every prime in scope.  Equation (1.10) is
> forced by the candidate extra common gate and is not another copy.  It
> gives no $A_1$ implication.  The new Route-1 rate credit is zero.

## 2. The common-moving sequences as two periods

Let



$$
Q(x)=1+x+x^2+x^3.            \tag{2.1}
$$



Using $1-x^4=(1-x)Q(x)$, the Item 205 coefficients become



$$
g_1(s)=[x^{3s+2}]\frac{Q(x)^{2s}}{(1-x)^{3s+3}},
 \qquad
 g_0(s)=[x^{3s+2}]\frac{Q(x)^{2s+1}}{(1-x)^{3s+3}}.  \tag{2.2}
$$



Put



$$
\Phi(x)={Q(x)^2\over x^3(1-x)^3},qquad
 w(x)={1\over x^2(1-x)^3}.                           \tag{2.3}
$$



Then



$$
g_1(s)=\operatorname {CT}(w\Phi^s),
 \qquad g_0(s)=\operatorname {CT}(Qw\Phi^s).         \tag{2.4}
$$



The two adjacent layers are therefore four period observations of the same
hyperexponential kernel.

## 3. Exact telescoping proof of the adjacent identity

Write $\theta=x\,d/dx$.  Define



$$
N_s(x)=\sum_{i=0}^7n_i(s)x^i, \tag{3.1}
$$



where



$$
\begin{array}{c|l}
i&n_i(s)\\ \hline
0&7464+16818s+12555s^2+3105s^3\\
1&14886+33549s+25065s^2+6210s^3\\
2&22140+49988s+37455s^2+9315s^3\\
3&30318+68723s+51685s^2+12900s^3\\
4&18120+41250s+31245s^2+7875s^3\\
5&16458+38439s+29775s^2+7650s^3\\
6&5364+12720s+10025s^2+2625s^3\\
7&-894-1375s-525s^2.
\end{array}                                           \tag{3.2}
$$



Set



$$
R_s(x)={N_s(x)Q(x)\over x^5(1-x)^5}.   \tag{3.3}
$$



Direct polynomial expansion gives the rational identity



$$
\begin{aligned}
 &w\{16(s+1)(2s+3)[aQ-20b_0]\\
 &\qquad\quad+3(3s+4)(3s+5)\Phi[cQ-20d]\}\\
 &=\theta R_s+sR_s\,\theta\log\Phi.                  \tag{3.4}
\end{aligned}
$$



Multiplying by $\Phi^s$, the right side is
$\theta(R_s\Phi^s)$.  The constant term of a $\theta$-derivative is
zero.  Applying $\operatorname {CT}$ and using (2.4) proves (1.7) for
every $s\ge0$.  The checker verifies (3.4) coefficient by coefficient in
$\mathbb Z[s,x]$.

## 4. Phase-preserving cross-$b$ and cross-$j$ maps

At fixed $(p,q)$, replacing $s$ by $s+1$ gives



$$
b'=qp-5(s+1)-4=b-5,qquad r'=r+3\pmod4. \tag{4.1}
$$



If the original far row has $b\ge M/5$, then $b\ge5$ for all
sufficiently large $M$.  Thus the phase is unchanged: in the $q=1$
case $b\ge5$ says $p\ge5s+9$, and the $q=2$ inequality remains true
automatically.  Stability is retained because



$$
b-5\le b\le3s+4<3(s+1)+4.    \tag{4.2}
$$



The adjacent layer remains rank one unless $p\le3s+5$.  Since the
original row has $p>3s+2$, the only failures are



$$
p=3s+c,qquad c=3,4,5.       \tag{4.3}
$$



Substitution in (1.1) gives



$$
(3j+2)p=6M+3-c.              \tag{4.4}
$$



Therefore all distinct boundary primes at fixed $M$ divide
$(6M)(6M-1)(6M-2)$, and their total log weight is $O(\log M)$.  Removing
them does not alter (1.5).

The adjacent layer is also an actual cell row.  Put



$$
j'=j+1,qquad M'=M+{p-1\over2}.          \tag{4.5}
$$



Then



$$
2M'+1=(j'+1)p-(s+1).                                 \tag{4.6}
$$



This is the advertised cross-$j$ realization.

Finally, substituting $s\equiv-(b+4)/5\pmod p$ into (1.6), clearing the
unit $5$, and writing $b'=b-5$ gives (1.8)--(1.9).  No moving
denominator is introduced.

## 5. Unit audit and the surviving adjacent line

For an actual row, $0\le s\le(p-3)/3$.  Hence, outside the fixed primes,



$$
0<s+1<p,qquad0<2s+3<p.       \tag{5.1}
$$



Also $3s+4,3s+5\le p+2$.  Either is divisible by $p$ exactly on one of
the boundary rays in (4.3); these have zero rate by (4.4).

The two reduced coefficient pairs have resultants



$$
\operatorname {Res}(a,b_0)=-3051=-3^3\cdot113,
 \qquad
 \operatorname {Res}(c,d)=1564=2^2\cdot17\cdot23.    \tag{5.2}
$$



Thus, after removing the fixed exceptional primes and the boundary rays,
both sides of (1.7) are nonzero linear observations.  If (1.3) holds, the
first observation vanishes and the second is exactly the line (1.10).  It is
not a common adjacent gate.

More importantly, define



$$
U_s=a(s)g_0(s)-20b_0(s)g_1(s),qquad
 V_s=c(s)g_0(s+1)-20d(s)g_1(s+1).                   \tag{5.3}
$$



Equation (1.7) is precisely



$$
3(3s+4)(3s+5)V_s=-16(s+1)(2s+3)U_s.                \tag{5.4}
$$



Modulo every nonexceptional actual prime, $p\mid V_s$ is therefore
equivalent to $p\mid U_s$.  The adjacent divisor is a relocation of a
current-layer linear combination.  It is not independent information from
the common gate.

## 6. Minimal adjacent ansatz and the actual counterexample

Consider the vector space of quadruples $(P_0,P_1,P_2,P_3)$ with
$\deg P_i\le4$ satisfying (1.12) for all $s\ge0$.  Evaluation at
$s=0,1,\ldots,24$ gives an exact rational matrix with twenty columns and
rank nineteen.  The coefficients in (1.7) span its one-dimensional kernel.
Every all-$s$ identity in the ansatz lies in this sampled kernel, so the
rank computation proves uniqueness; it is not an extrapolation from a
zero scan.

Consequently there is no second independent adjacent relation of the same
degree with which to eliminate both entries of $(g_0(s+1),g_1(s+1))$.
The mandatory actual row shows the remaining line is real.  Exact recurrence
arithmetic gives (1.13)--(1.15).  In particular a common gate at $b=900$
does not propagate to a common gate at $b=895$.

This is a scoped obstruction to the first adjacent linear-resultant ansatz.
It says nothing about degrees greater than four or nonlinear relations.

## 7. Height, Item 149 overlap, and admission

Item 205 gives



$$
|g_1(t)|\le4^{5t+2},qquad |g_0(t)|\le4^{5t+3}.      \tag{7.1}
$$



Therefore



$$
|V_s|\le\bigl(|c(s)|+20|d(s)|\bigr)4^{5s+8},qquad
                         \log|V_s|=O(s).              \tag{7.2}
$$



There are $O(M)$ possible moving $s$-layers with $s=O(M)$.  The
product furnished by (7.2) consequently has logarithmic height
$O(M^2)$, not $O(\log M)$ or $o(M)$.  It cannot improve Item 266's
raw ceiling.  Equation (5.4) additionally proves that its prime divisor is
not an independent condition.

The master admission test therefore gives:

1. **Actual-family implication:** a common gate forces (1.10) on every
   nonexceptional actual far row.
2. **De-overlap:** (1.10) is caused by the same candidate extra gate after
   Item 149's first copy; it cannot be booked again.
3. **Quantitative result:** the available cross-layer integer has
   exponential height and no weighted zero theorem.
4. **Decision:** zero new Route-1 rate.

## 8. Replay and status

The standard-library checker

```text
scripts/item268_cross_b_contiguous_obstruction_certificate.py
```

* verifies the telescoping identity (3.4) in exact bivariate polynomial
  arithmetic;
* verifies the exact degree-four kernel rank and its generator;
* computes both resultants by exact rational elimination;
* verifies the phase substitution, boundary divisor identity, and exact far
  coefficient;
* recomputes the $2399$ common row and its nonzero adjacent line.

No common-zero scan is performed.  The bounded recurrence/rank replay is
**EXACT FINITE ONLY** and is used only to certify the stated finite matrix
rank and declared witness.

### PROVED

* Maximum affected mass (1.5), up to a zero-rate boundary.
* Exact adjacent identity and telescoping certificate.
* Exact cross-$b$/cross-$j$ realization and unit audit.
* One-dimensional surviving adjacent line and actual nonpropagation witness.
* Uniqueness in the degree-$4$ adjacent linear ansatz.
* Scoped height/dependence failure and exact Item 149 de-overlap.
* Zero new booking.

### OPEN

* A higher-degree or nonlinear cross-layer resultant.
* A bounded-rank global transfer retaining the fixed initial state.
* A polynomial-height cross-layer integer forced by the full common gate.
* An $o(M)$ or sufficiently small weighted upper bound.
* Any positive common-content lower bound or Route-1 improvement.
