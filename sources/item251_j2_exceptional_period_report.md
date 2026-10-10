> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 251 — the surviving period on the ordinary $j=2$ exceptional locus

Checked: 2026-08-31 (Beijing time)

## 1. Scope and verdict

Retain the ordinary Item-219/250 cell



$$
p=2r+6s+3,\qquad r=2h+1\ge1,\qquad Q=2s,
 \tag{1.1}
$$



and Item 250's exact rank-one gate



$$
G_\nu=f_\nu Z+U_\nu,
 \qquad U_\nu=P_\nu^\flat c+H_\nu^\flat,
 \qquad c=2^Q,                                      \tag{1.2}
$$



where



$$
Z=9\kappa_r e-\mathfrak f,\qquad e=J_0.           \tag{1.3}
$$



This item does not repeat the fixed-$r$ derivation of
$(f_\nu,P_\nu^\flat,H_\nu^\flat)$.  It determines the remaining period
$Z$ exactly and asks what that determination supplies on



$$
f_0U_1-f_1U_0=L_rc+M_r=0.                         \tag{1.4}
$$



> **PROVED — exact integer normalization of the surviving period.**  Put
> 

$$
> B_s=\frac{(2s-1)!(s-1)!}{(3s-1)!},               \tag{1.5}
>
$$


> and
> 

$$
> A_s=\sum_{j=0}^{2s-1}
>       \binom{3s-1}{s+j}\binom{s+j-1}{j}\in\mathbb Z. \tag{1.6}
>
$$


> Then
> 

$$
> e=\frac{B_s}{2}A_s,\qquad
> \mathfrak f=B_s\tau_{r,s},                       \tag{1.7}
>
$$


> where
> 

$$
> \tau_{r,s}=(-1)^{s+h}\frac23
>       \frac{(s)_{h+1}}{(3s+1)_{h+1}}.            \tag{1.8}
>
$$


> Consequently
> 

$$
> \boxed{
> Z=B_s\left(\frac{9\kappa_r}{2}A_s-\tau_{r,s}\right).} \tag{1.9}
>
$$


> Every denominator in (1.5), (1.8), and (1.9) is a $p$-unit on every
> actual row.

> **PROVED — algebraic diagonal and order-two recurrence.**  If
> $w=t(2+w)^3$ is the unique series in $t\mathbb Z[[t]]$, then
> 

$$
> \sum_{s\ge1}A_st^{s-1}
>   =\frac{(2+w)^3}{2(1-w^2)}-\frac1{1+t}.          \tag{1.10}
>
$$


> With $A_1=3,A_2=49$, the exact recurrence is
> 

$$
> \begin{aligned}
> &(s+1)(2s+3)(28s+11)A_{s+2}\\
> &\quad-(1456s^3+3456s^2+2303s+435)A_{s+1}\\
> &\quad-6(3s+1)(3s+2)(28s+39)A_s=0.               \tag{1.11}
> \end{aligned}
>
$$



> **PROVED — the residual is an incomplete hypergeometric endpoint.**  Set
> $\Delta_s=A_{s+1}+A_s$.  Equation (1.11) factors exactly as
> 

$$
> \frac{\Delta_{s+1}}{\Delta_s}
>  =\frac{6(3s+1)(3s+2)(28s+39)}
>         {(s+1)(2s+3)(28s+11)},\qquad \Delta_1=52, \tag{1.12}
>
$$


> over $\mathbb Q$, while
> 

$$
> A_s=(-1)^{s-1}\left(3+
>       \sum_{j=1}^{s-1}(-1)^j\Delta_j\right).     \tag{1.13}
>
$$


> Thus the rank-one eliminant removes the product mode but leaves its
> alternating incomplete sum.  The order-two recurrence does not turn the
> exceptional locus into a fixed-$r$ product obstruction.

> **PROVED — rank-aware second condition.**  On (1.4), if
> $(f_0,f_1)\ne(0,0)\pmod p$, a simultaneous collision is equivalent to
> 

$$
> f_\nu B_s\left(\frac{9\kappa_r}{2}A_s-\tau_{r,s}\right)
>       +U_\nu=0\pmod p                             \tag{1.14}
>
$$


> for one (hence every) index with $f_\nu\ne0$.  No division is needed:
> both displayed residuals are exactly $G_0,G_1$.  If
> $f_0=f_1=0\pmod p$, the separate branch is $U_0=U_1=0$, and $Z$
> is irrelevant.

> **OPEN.**  Neither (1.11) nor (1.12) proves all-prime nonvanishing or a
> zero-density theorem for (1.14).  Item 251 books no capacity reduction.

The first scalar shortcuts are actually false.  On the admissible row
$(p,s,r)=(31,3,5)$, $A_3=1023=33p$.  On
$(p,s,r)=(41,4,7)$,
$\Delta_4=577280=14080p$.  These exact counterexamples do not produce
common-gate collisions; they show that neither $A_s\ne0$ nor
$\Delta_s\ne0$ can be used as a universal substitute for (1.14).

## 2. The affine odd chain, independently localized

For context, define



$$
J_k=\sum_{t=0}^{Q-1}\binom{Q-1}{t}\frac1{Q+k+2t},
 \qquad c=2^Q.                                      \tag{2.1}
$$



Termwise differentiation of
$x^{Q+k}(1+x^2)^Q$ gives



$$
(Q+k)J_k+(3Q+k)J_{k+2}=c.                         \tag{2.2}
$$



At $k_*=2r+3$, the coefficient of $x^p$ is one and its derivative
vanishes modulo $p$.  Therefore the terminal is affine, not homogeneous:



$$
J_{k_*}=\frac{c-1}{Q+k_*}.                        \tag{2.3}
$$



Descending by two from (2.3) gives



$$
J_1=\alpha_rc+\beta_r,                             \tag{2.4}
$$



while the even chain starts from the independent coordinate $J_0=e$.
This is precisely why the Item-250 compression retains $Z$.  Equations
(1.7)--(1.13) identify that coordinate without discarding the Frobenius
$-1$ in (2.3).

## 3. Beta normalization

Substitute $u=x^2$ in $J_0$:



$$
e=\frac12\int_0^1u^{s-1}(1+u)^{2s-1}\,du
   =\frac12\sum_{j=0}^{2s-1}\binom{2s-1}{j}\frac1{s+j}. \tag{3.1}
$$



Here and below the integral is finite polynomial shorthand.  Dividing a
summand in (3.1) by $B_s$ gives



$$
\frac1{B_s}\binom{2s-1}{j}\frac1{s+j}
 =\binom{3s-1}{s+j}\binom{s+j-1}{j}.               \tag{3.2}
$$



Summing proves the first identity in (1.7), including the integrality in
(1.6).

For $r=2h+1$, Item 250's common upper-tail factor is



$$
\mathfrak f=(-1)^{s+h}
       \frac{(2s)!(s+h)!}{(3s+h+1)!}.               \tag{3.3}
$$



Thus



$$
\frac{\mathfrak f}{B_s}
 =(-1)^{s+h}\frac{2s(s)_{h+1}}{(3s)_{h+2}}
 =(-1)^{s+h}\frac23
       \frac{(s)_{h+1}}{(3s+1)_{h+1}},             \tag{3.4}
$$



which proves (1.8)--(1.9).

The unit bounds are direct.  The largest factorial argument in $B_s$ is
$3s-1<p$; the largest one in (3.3) is $3s+h+1<p$.  Every factor
$3s+j$ in (1.8) satisfies
$1\le3s+j\le3s+h+1<p$.  Constants $2,3$ are units.

## 4. Coefficient and algebraic generating function

Put $k=s+j$ in (1.6).  Since



$$
\binom{k-1}{s-1}=[x^{s-1}](1+x)^{k-1},            \tag{4.1}
$$



the $k=0$ term must be removed, and the binomial theorem gives



$$
A_s=[x^{s-1}]\frac{(2+x)^{3s-1}-1}{1+x}.          \tag{4.2}
$$



For $n=s-1$, the first part is the diagonal



$$
[x^n]\frac{(2+x)^2}{1+x}\{(2+x)^3\}^{n}.         \tag{4.3}
$$



The formal Lagrange diagonal identity



$$
\sum_{n\ge0}t^n[x^n]A(x)\phi(x)^n
   =\frac{A(w)}{1-t\phi'(w)},\qquad w=t\phi(w),    \tag{4.4}
$$



with $A(x)=(2+x)^2/(1+x)$ and $\phi(x)=(2+x)^3$, yields



$$
\frac{(2+w)^3}{2(1-w^2)}.                         \tag{4.5}
$$



The removed coefficient $[x^n](1+x)^{-1}=(-1)^n$ contributes
$(1+t)^{-1}$.  This proves (1.10) as an identity in formal power series.

## 5. Exact telescoping certificate for the recurrence

Let



$$
E_s=\int_0^1u^{s-1}(1+u)^{2s-1}\,du=B_sA_s,
 \qquad R=u(1+u)^2.                                \tag{5.1}
$$



Write $C_0,C_1,C_2$ for the three coefficients of
$A_s,A_{s+1},A_{s+2}$ in (1.11), and put



$$
D_j=C_j\frac{B_s}{B_{s+j}}.                       \tag{5.2}
$$



Define



$$
H_s(u)=\frac{3u(3s+1)(3s+2)(u-1)(u+1)}{4s(2s+1)}P_s(u), \tag{5.3}
$$



where



$$
\begin{aligned}
P_s(u)={}&(252s^2+435s+132)u^4\\
 &+(1176s^2+2058s+627)u^3\\
 &+(2380s^2+4211s+1287)u^2\\
 &+(2016s^2+3648s+1182)u\\
 &+448s^2+848s+312.
\end{aligned}                                      \tag{5.4}
$$



Direct coefficient comparison in $\mathbb Q(s)[u]$ gives



$$
D_0+D_1R+D_2R^2
 =H_s'(u)+H_s(u)\left(\frac{s-1}{u}
                    +\frac{2s-1}{1+u}\right).     \tag{5.5}
$$



Multiplying (5.5) by $u^{s-1}(1+u)^{2s-1}$ makes the right side an
exact derivative.  Since $H_s(0)=H_s(1)=0$, integration proves (1.11)
for every integer $s\ge1$.  The checker clears $4s(2s+1)$ and verifies
the resulting bivariate integer-polynomial identity exactly; no sampling
is used for its canonical proof.

On an actual row $4s(2s+1)$ is a $p$-unit.  However, factors such as
$28s+11$ in (1.11) need not be units.  Indeed, for
$(p,s,r)=(41,4,7)$, $28s+11=3p$.  Therefore (1.11) is used as an
integer recurrence; no modular division by its leading coefficient is
claimed.

## 6. Factorization and the precise leftover

The coefficient identity



$$
C_0-C_1+C_2=0              \tag{6.1}
$$



shows that $(-1)^s$ is one solution of (1.11).  Substituting
$\Delta_s=A_{s+1}+A_s$ gives (1.12).  Equivalently,



$$
\Delta_s=52\,27^{s-1}
 \frac{(4/3)_{s-1}(5/3)_{s-1}(67/28)_{s-1}}
      {(2)_{s-1}(5/2)_{s-1}(39/28)_{s-1}}.         \tag{6.2}
$$



Discrete antidifferentiation gives (1.13).  This is a useful structural
endpoint: $A_s$ is one alternating incomplete hypergeometric sum, rather
than two unrelated beta periods.  It is not a nonvanishing theorem.

The exact counterexamples quoted after (1.14) prove a scoped no-go:

* universal nonvanishing of $A_s$ is false;
* universal nonvanishing of its hypergeometric increment $\Delta_s$ is
  false; and
* modular propagation by dividing every coefficient of (1.12) is invalid.

They do not rule out a deeper Cartier, $p$-adic, or density theorem for
the particular combination in (1.14).

### Coordinated modular specialization

Item 252 continues (4.2) one step further.  Put



$$
m=s-1,\qquad d=r+2,\qquad
 \epsilon=\left(\frac2p\right)\in\{\pm1\},\qquad
 2^{(p-1)/2}\equiv\epsilon\pmod p,                 \tag{6.3}
$$



and define



$$
h_j=\frac{(1/2)_j}{j!\,2^j},\qquad
 H_m=\sum_{j=0}^m h_j,                              \tag{6.4}
$$





$$
P_d(m)=\sum_{k=1}^d2^{-k}
          \frac{(m+1/2)_k}{(1/2)_k}.               \tag{6.5}
$$



Its exact finite-contiguous identity gives



$$
\boxed{
 A_s=(-1)^m\{\epsilon[H_m-h_mP_d(m)]-1\}\pmod p.}  \tag{6.6}
$$



The sign and normalization follow directly from
$3s-1=(p-1)/2-d$ in (4.2); they were independently cross-checked against
all 1,153 Item-251 phase rows through $p\le401$.  The proof and the
fixed-degree scalar-Gosper no-go belong to the separate Item-252 package
and are not duplicated here.

Combining (6.6) with (1.9) gives the most localized form of the second
condition:



$$
Z=B_s\left[
 \frac{9\kappa_r}{2}(-1)^m
 \{\epsilon[H_m-h_mP_d(m)]-1\}-\tau_{r,s}\right].  \tag{6.7}
$$



All denominators in (6.4)--(6.5) are units: $m<p$;
the odd denominator factors of $P_d$ are at most
$2d-1=2r+3=p-6s<p$, and its numerator rectangle is bounded by
$2m+2d-1=p-4s-2<p$.  Thus, after the exact fixed-degree correction
$h_mP_d(m)$, one moving half-binomial prefix $H_m$ remains.  Neither
Item 251 nor Item 252 currently proves its required rowwise nonvanishing
or a sufficient zero-density estimate.

## 7. Exceptional-locus implication

Let $\mathbf f=(f_0,f_1)$ and
$\mathbf U=(U_0,U_1)$.  Equation (1.2) is



$$
\mathbf G=\mathbf fZ+\mathbf U. \tag{7.1}
$$



Its determinant compatibility is (1.4).  If $\mathbf f\ne0\pmod p$,
then (1.4) says that $\mathbf U$ lies on the same line as $\mathbf f$.
There is one unique formal value of $Z$ making both coordinates zero.
Substituting (1.9) gives (1.14), with no hidden division.  This is the exact
second arithmetic condition missing from the cubic resultant.

If $\mathbf f=0\pmod p$, determinant compatibility is automatic and the
right condition is $\mathbf U=0$.  A uniform proof must retain this branch;
declaring (1.14) after dividing by $f_0$ or $f_1$ would be incomplete.

The second condition is not vacuous.  For example, all of the following
are exact affine false positives:



$$
\begin{array}{c|r|r|r|r}
p&s&r&G_0&G_1\\ \hline
953&158&1&0&374\\
2281&378&5&1645&1690\\
5711&941&31&519&4302\\
367&39&65&238&354.
\end{array}                                        \tag{7.2}
$$



In each row $L_rc+M_r=0$, but (1.14) fails.  Thus (1.14) genuinely
removes false positives; no checked row in (7.2) is a common collision.

## 8. Finite replay, separated from the theorem

The canonical checker verifies the exact telescoping identity, 100 direct
sum/diagonal/integral triples, 999 recurrence and increment steps, and the
first 30 coefficients of (1.10).

Against Item 250 it checks every 1,153 admissible row through $p\le401$:



$$
\begin{array}{l|r}
\text{period-normalization identities}&1153\\
L_rc+M_r=0&3\\
(G_0,G_1)=(0,0)&0\\
(f_0,f_1)=(0,0)&0.
\end{array}                                        \tag{8.1}
$$



A separate scalar scan through $p\le20000$ covers 1,763,142 admissible
rows.  It finds 185 rows with $A_s=0\pmod p$ and 194 with
$\Delta_s=0\pmod p$.  These counts, and the absence of a common gate in
(8.1), are **EXACT FINITE ONLY**.  They imply no density statement.

## 9. Rate and strict labels

The recurrence relates neighboring $s$-values, hence neighboring moduli
$p,p+6,p+12$ when $r$ is fixed.  It does not by itself compare their
different prime reductions.  The algebraic generating function supplies
height and holonomy information, but no theorem here bounds the primes for
which the row-specific residual (1.14) vanishes.  Therefore



$$
\boxed{\text{new unconditional Route-1 rate from Item 251}=0}. \tag{9.1}
$$



### PROVED

* the beta normalization, tail ratio, and formula (1.9) for $Z$;
* the coefficient/diagonal/generating-function descriptions of $A_s$;
* the telescoping recurrence (1.11), including endpoints;
* the factorization (1.12)--(1.13);
* the rank-aware exceptional condition (1.14);
* the stated denominator audit and the two explicit scalar
  counterexamples.

### EXACT FINITE ONLY

* the 1,153-row phase replay through $p\le401$;
* the seven selected larger affine false positives;
* the 1,763,142-row scalar-zero census through $p\le20000$.

### OPEN

* all-prime nonvanishing of (1.14);
* any zero-density theorem strong enough to reduce the $j=2$ capacity;
* all-prime classification of the rank-zero branch;
* a Cartier or $p$-adic theorem for the incomplete sum (1.13);
* any new divisibility exponent, capacity booking, or conclusion about
  $e+\pi$.

## 10. Reproduction

From the portable archive root:

~~~
python scripts/item251_j2_exceptional_period_certificate.py \
  --output results/item251_j2_exceptional_period_certificate.json
python scripts/item251_j2_exceptional_period_certificate.py \
  --output results/item251_j2_exceptional_period_certificate_replay.json
~~~

The checker uses only Python's standard library and the frozen Item-250
checker.  It contains no timestamp, elapsed time, random seed, or host path.
