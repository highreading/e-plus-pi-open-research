> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 328 - the actual ordinary-$j=2$ Cartier digit and its Frobenius break

Checked: 2026-09-01 (Beijing time)

## 1. Scope and verdict

Retain the actual ordinary-$j=2$ row



$$
p=2r+6s+3,\qquad r\ge1\text{ odd},\qquad3\nmid r,\qquad s\ge1,
 \tag{1.1}
$$



and put



$$
m=s-1,\qquad d=r+4,\qquad n=3m+d=\frac{p-1}{2},
 \qquad q=2m+d=n-m.                                  \tag{1.2}
$$



Thus the actual tied phase and fixed-$M$ phase are



$$
p=6m+2d+1=2n+1,qquad
 2M=14m+5d+1,qquad q=2(M-p)+1,                       \tag{1.3}
$$



and



$$
q\text{ is odd},\qquad
                         \frac p3<q\le\frac{p-1}{2}.  \tag{1.4}
$$



Item 325 proves



$$
H_m=\epsilon\left\{1-(-1)^nS_{n,q}\right\}\pmod p,
 \qquad
 S_{n,q}=\sum_{j=0}^{(q-1)/2}(-1)^j
             \binom q{2j+1}\binom nj,                \tag{1.5}
$$



where $\epsilon=(2/p)$.  The present item asks whether the exact sum can
be promoted from a representation into arithmetic at the tied prime.

Define



$$
\mathcal F_{m,d}(x)
 =(1-x)^n(1+x)^{n+q}
 =\sum_{k=0}^{D}c_kx^k,qquad D=2n+q=p+q-1.          \tag{1.6}
$$



> **PROVED - the remaining period is one exact Cartier digit.**
> 

$$
> \boxed{S_{n,q}=(-1)^nc_p=c_{q-1},}
> \qquad
> \boxed{H_m=\epsilon(1-c_p)\pmod p.}                \tag{1.7}
>
$$


> Hence, after the old determinant gate and on the
> $\ell_r\ne0\pmod p$ chart, the original collision is exactly
> 

$$
> \boxed{c_p=1-\epsilon\Theta_{r,s}\pmod p.}          \tag{1.8}
>
$$


> This is an actual-family affine Cartier-digit condition, not a new
> auxiliary period.

> **PROVED - exact Frobenius break.**  The coefficients in (1.6) satisfy
> over $\mathbf Z$
> 

$$
> \boxed{(k+1)c_{k+1}=q c_k+(k-p-q)c_{k-1}.}           \tag{1.9}
>
$$


> Modulo $p$, the recurrence has exactly one singular step before the
> polynomial endpoint, at $k=p-1$:
> 

$$
> \boxed{q c_{p-1}=(q+1)c_{p-2}.}                     \tag{1.10}
>
$$


> Equation (1.10) contains no $c_p$.  The Cartier digit is a genuinely
> free continuation parameter for the local reduced recurrence.

> **PROVED - self-similar Frobenius impulse.**  If two reduced recurrence
> continuations agree through $c_{p-1}$ and their $p$-th digits differ
> by $\lambda$, then
> 

$$
> \boxed{\delta_{p+t}=\lambda c_t\qquad(0\le t\le q).} \tag{1.11}
>
$$


> The endpoint $c_{D+1}=0$ lies exactly $q>p/3$ steps after $c_p$,
> and its impulse multiplier is
> 

$$
> \boxed{
> c_q\equiv2^{-q}\binom{2q}{q}\not\equiv0\pmod p.}   \tag{1.12}
>
$$


> Thus the endpoint fixes the free digit uniquely, but only after linear
> depth.

> **PROVED - scoped local-recurrence no-go.**  For every $J<q$, there
> are $p$ recurrence-consistent continuations through index $p+J$
> with identical pre-$p$ coefficients and arbitrary $c_p$.  Therefore
> every bounded-depth, and more generally every $o(p)$-depth, method
> using only (1.9) and a not-yet-reached endpoint is eventually blind to
> the actual Cartier digit.

The new localization is exact, but it does not control primes for which
(1.8) holds.  The strict ledger effect remains



$$
\boxed{\text{new capacity reduction}=0},\qquad
 \boxed{\text{new booking}=0},\qquad
 \boxed{\text{ordinary-}j=2\text{ ceiling}=1/105\text{ per }6M}.
 \tag{1.13}
$$



## 2. Admission, raw capacity, and actual implication

Item 322 gives, after $D_{r,s}=0$ and on $\ell_r\ne0\pmod p$,



$$
\mathcal E_{r,s}=
 \ell_rB_s\frac{9\kappa_r}{2}(-1)^m\epsilon
 (H_m-\Theta_{r,s})\pmod p,                            \tag{2.1}
$$



with a certified unit multiplier.  Combining (2.1) with (1.7) gives
(1.8) and proves that the new Cartier equation is forced by the original
collision.  It is not a freely chosen extra moment.

The condition is also internal to the already retained determinant branch.
It can only remove capacity; it cannot be added to the booked lower bound.
Item 322 already makes the adjacent $p,p+6$ transfer subfamily zero-rate.
The isolated complement retains the full raw ceiling



$$
\mathcal C_{\max}=\frac1{105}
 =0.009523809523809523\ldots\quad\text{per }6M.        \tag{2.2}
$$



Even perfect target avoidance in (1.8) would only close (2.2), far less
than the current Route-1 deficit.  It would nevertheless be useful in a
Route-1 no-go ledger.  No target avoidance or weighted prime bound is
proved here.

The $\ell_r=0$ and rank-at-most-one charts remain present.  Equation
(1.8) is not applied there; those rows retain the division-free residual or
an individual connection coordinate from Items 318 and 322.

## 3. From the Item-325 convolution to the $p$-th coefficient

Let



$$
A_q(z)=\sum_{j=0}^{(q-1)/2}\binom q{2j+1}z^j.
 \tag{3.1}
$$



Coefficient reversal in $(1-z)^n$ gives



$$
S_{n,q}=(-1)^n[z^n](1-z)^nA_q(z).                    \tag{3.2}
$$



The odd part of $(1+x)^q$ is



$$
A_q(x^2)=\frac{(1+x)^q-(1-x)^q}{2x}.                 \tag{3.3}
$$



Substituting $z=x^2$ into (3.2) therefore yields



$$
\begin{aligned}
 S_{n,q}
 &=\frac{(-1)^n}{2}[x^{2n+1}](1-x^2)^n
       \bigl((1+x)^q-(1-x)^q\bigr).                  \tag{3.4}
\end{aligned}
$$



The first product in (3.4) is $\mathcal F_{m,d}(x)$; the second is
$\mathcal F_{m,d}(-x)$.  Since $2n+1=p$ is odd, their coefficients at
$x^p$ are $c_p$ and $-c_p$.  This proves



$$
S_{n,q}=(-1)^nc_p.             \tag{3.5}
$$



There is also exact reciprocity.  From (1.6),



$$
x^D\mathcal F_{m,d}(1/x)=(-1)^n\mathcal F_{m,d}(x),  \tag{3.6}
$$



so



$$
c_{D-k}=(-1)^nc_k.                                    \tag{3.7}
$$



Because $D-p=q-1$, equations (3.5)-(3.7) give



$$
S_{n,q}=c_{q-1}.               \tag{3.8}
$$



Finally (1.5) and (3.5) prove the Cartier-digit formula in (1.7).  No
finite scan, interpolation, or division by a connection minor occurs in
this derivation.

Reciprocity does determine $c_p$ from $c_{q-1}$, but (3.8) shows that
the latter is exactly the original unevaluated binomial period.  Thus it is
not an arithmetic elimination of the target.

## 4. The coefficient recurrence and the unique break

Logarithmic differentiation of (1.6) gives



$$
(1-x^2)\mathcal F'_{m,d}(x)
 =\bigl(q-Dx\bigr)\mathcal F_{m,d}(x).                \tag{4.1}
$$



Comparing coefficients of $x^k$, with $c_{-1}=c_{D+1}=0$, proves



$$
(k+1)c_{k+1}=q c_k+(k-1-D)c_{k-1}.                  \tag{4.2}
$$



Since $D=p+q-1$, this is (1.9).  Reduction modulo $p$ gives



$$
(k+1)c_{k+1}=q c_k+(k-q)c_{k-1}.                    \tag{4.3}
$$



The forward pivot $k+1$ vanishes exactly when
$k\equiv p-1\pmod p$.  But



$$
D=p+q-1<p+\frac p2<2p-1,                             \tag{4.4}
$$



so $k=p-1$ is the only such index before the endpoint.  At that index,
(4.3) becomes (1.10).  It checks compatibility of the pre-$p$ state but
does not determine $c_p$.

This is an exact Frobenius phenomenon at the actual tied coefficient:
the characteristic-zero recurrence determines every earlier coefficient,
but its pivot vanishes precisely when it reaches the coefficient that
encodes $H_m$.

## 5. The impulse is a shifted copy of the low coefficient sequence

Take two solutions of (4.3) that agree through index $p-1$, and write
their difference as $\delta_k$.  Normalize first to



$$
\delta_{p-1}=0,\qquad\delta_p=1. \tag{5.1}
$$



Put $e_t=\delta_{p+t}$.  Shifting $k=p+t$ in (4.3) gives



$$
(t+1)e_{t+1}=q e_t+(t-q)e_{t-1},qquad
 e_{-1}=0,\ e_0=1.                                    \tag{5.2}
$$



But the low coefficients $c_t$, starting from $c_{-1}=0,c_0=1$,
satisfy exactly the same recurrence.  Since $t+1$ is a unit for
$0\le t<q<p$, induction gives



$$
e_t=c_t\qquad(0\le t\le q).   \tag{5.3}
$$



Scaling (5.1) by an arbitrary $\lambda\in\mathbf F_p$ proves (1.11).
Thus there are exactly $p$ local continuations at the Frobenius break,
and their later differences are controlled by the original low
coefficient sequence.

## 6. The endpoint multiplier is an explicit unit

The endpoint lies at



$$
D+1=p+q,\qquad (D+1)-p=q>p/3.                        \tag{6.1}
$$



By (5.3), changing $c_p$ by one changes the endpoint value
$c_{D+1}$ by $c_q$.  It remains to evaluate that multiplier.

Because $n=(p-1)/2\equiv-1/2\pmod p$ and $q<p$, coefficientwise
reduction through degree $q$ gives



$$
\begin{aligned}
 c_q
 &=[x^q](1-x^2)^n(1+x)^q\\
 &\equiv[x^q](1-x^2)^{-1/2}(1+x)^q\pmod p.           \tag{6.2}
\end{aligned}
$$



The characteristic-zero coefficient identity



$$
[x^q](1-x^2)^{-1/2}(1+x)^q
 =2^{-q}\binom{2q}{q}                                \tag{6.3}
$$



follows, for example, by summing its generating function.  Indeed the
left side equals



$$
a_q=\sum_{j=0}^{\lfloor q/2\rfloor}
       \frac1{4^j}\binom{2j}{j}\binom q{2j},          \tag{6.4}
$$



and



$$
\begin{aligned}
 \sum_{q\ge0}a_qt^q
 &=\frac1{1-t}\sum_{j\ge0}\binom{2j}{j}
       \left(\frac{t^2}{4(1-t)^2}\right)^j\\
 &=\frac1{\sqrt{1-2t}}.
\end{aligned}                                         \tag{6.5}
$$



This proves (6.3) and hence (1.12).  Since $2q\le p-1$, both
$2^q$ and $\binom{2q}{q}$ are $p$-units.  Therefore the endpoint
condition $c_{D+1}=0$, once reached, fixes the free $c_p$ uniquely.

## 7. A global no-go for sublinear-depth recurrence closure

Fix any $J<q$.  The endpoint index $D+1=p+q$ is not visible in the
window through $p+J$.  Equations (5.1)-(5.3) show that for every
$\lambda\in\mathbf F_p$, adding



$$
\delta_{p+t}=\lambda c_t\qquad(0\le t\le J)          \tag{7.1}
$$



produces another continuation satisfying every reduced coefficient
recurrence in that window, while leaving all coefficients before $p$
unchanged and replacing $c_p$ by $c_p+\lambda$.

It follows rigorously that the data consisting of

* the complete pre-$p$ coefficient state;
* the local recurrence (4.3); and
* fewer than $q$ forward recurrence rows

contains no restriction at all on $c_p$.  Since $q>p/3$, every fixed
depth and every $J=o(p)$ eventually falls into this blind range.

This closes a broad but precisely stated method class:



$$
\boxed{\text{bounded- or sublinear-depth local differential-recurrence
 closure cannot control the actual Cartier digit}.}    \tag{7.2}
$$



The theorem does not rule out a global reciprocity identity, a nonlinear
factorization, another arithmetic period, monodromy or large-sieve input,
an average gcd theorem, or weighted zero density.  It says only that the
natural local recurrence has deliberately lost the digit at its unique
Frobenius pivot and needs linear-depth global information to recover it.

## 8. Arithmetic and capacity conclusion

Equation (1.8) is the smallest actual isolated-row arithmetic target now
available on the nondegenerate chart.  It converts the conic moment into
one affine Cartier coefficient, but neither (1.8) nor the recurrence proves



$$
\sum_{\substack{(r,s)\text{ on a fixed-}M\text{ slice}\\
 p\mid D_{r,s},\ c_p=1-\epsilon\Theta_{r,s}}}\log p=o(M). \tag{8.1}
$$



The unit (1.12) is a transfer multiplier, not a nonvanishing theorem for
the affine target in (1.8).  Likewise the $p$ free local continuations
are an information-theoretic statement about the recurrence, not evidence
that actual collision primes have positive density.

Accordingly Item 328 books zero and removes zero from the $1/105$
ceiling.  A successful continuation must bring arithmetic external to the
local coefficient recurrence: for example target-specific Frobenius
monodromy, factor localization of the cleared affine digit, or a weighted
average gcd theorem.

## 9. Deterministic replay

The standard-library checker verifies the tied geometry, polynomial
coefficients, every recurrence row, both Cartier identities, reciprocity,
the period congruence, the impulse self-similarity, and the unit endpoint
multiplier on every declared actual row through $p\le199$.  It separately
checks the characteristic-zero coefficient identity on a rectangular
family of tied integer parameters.

All counts, samples, and digests are **EXACT FINITE ONLY**.  The all-prime
results are the coefficient extraction, logarithmic derivative,
translation of the unique singular pivot, generating-function identity,
and linear-depth argument above.

## 10. Strict labels

**PROVED**

* $S_{n,q}=(-1)^nc_p=c_{q-1}$;
* $H_m=\epsilon(1-c_p)\pmod p$;
* the actual affine Cartier target (1.8) on the declared chart;
* the exact coefficient recurrence and unique Frobenius break;
* the self-similar impulse $\delta_{p+t}=\lambda c_t$;
* the unit endpoint multiplier (1.12);
* the bounded- and $o(p)$-depth local-recurrence no-go; and
* zero capacity booking and zero capacity reduction.

**EXACT FINITE ONLY / DIAGNOSTIC**

* every declared row count, sample, and digest in the certificate.

**OPEN**

* weighted zero density for the affine Cartier target (1.8);
* divisor localization or factor nonconcentration for its cleared
  numerator;
* a target-specific global Frobenius or monodromy theorem;
* arithmetic on the $\ell_r=0$ and rank-at-most-one charts;
* any reduction of the retained $1/105$ ceiling; and
* any new Route-1 booking or conclusion about $e+\pi$.
