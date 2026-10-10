> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 423 — polynomial-in-$m$ Bezout combinations do not lower the normalized mixed-cubic base

Date: 2026-09-01  
Status: **ROOT-AUDITED CANONICAL SHARPLY SCOPED BEZOUT-HEIGHT NO-GO, NO BOOKING**

## 1. Capacity-first verdict

Retain the canonical exact residue pair



$$
\lambda_{0,m}=[y^{4m}]
 \frac{(1-y)^{6m}(1+y)}{(1+y^2)^{4m+1}},
 \qquad
 \lambda_{1,m}=[y^{4m+1}]
 \frac{(1-y)^{6m}(1+y)^4}{(1+y^2)^{4m+2}}.       \tag{1.1}
$$



Canonical Items 415 and 418 put



$$
\mu_{s,m}=\lambda_{s,m}/F_m\in\mathbb Z,
 \qquad
 \log F_m=\mathfrak C_Fm+o(m),                         \tag{1.2}
$$



where



$$
\mathfrak C_F=-4\log2+\frac{\pi}{\sqrt3}+3\log3,
$$



and prove the complete strictly-large carrier identity



$$
c_m^>=
 \bigl(\gcd(|\mu_{0,m}|,|\mu_{1,m}|)\bigr)_{p>6m}.     \tag{1.3}
$$



Item 418's current component ceiling is



$$
C_>=\frac{\log\rho_*-\mathfrak C_F}{6}
 =0.4287738853386578689457603829\ldots,                \tag{1.4}
$$



with



$$
\rho_*=135.5974839008548212502259703306\ldots .       \tag{1.5}
$$



Item 420 proved that every fixed rational coordinate combination retains
root base $\rho_*$.  The present item attacks the next natural Bezout
class: coefficients that vary with the row but have fixed algebraic
complexity and logarithmic height.

> **Polynomial Bezout no-go.**  For every
> $(A,B)\in\mathbb Q[m]^2\setminus\{(0,0)\}$,
> 

$$
> \boxed{
>  \limsup_{m\to\infty}
>  |A(m)\lambda_{0,m}+B(m)\lambda_{1,m}|^{1/m}
>  =\rho_*.}                                             \tag{1.6}
>
$$



After clearing one fixed denominator, the corresponding integer
combination of the normalized pair satisfies



$$
\boxed{
 \limsup_{m\to\infty}
 |A(m)\mu_{0,m}+B(m)\mu_{1,m}|^{1/m}
 =\rho_*e^{-\mathfrak C_F}
 =13.1004071782333102143382142797\ldots .}              \tag{1.7}
$$



Thus ordinary absolute height of **one same-index, fixed-degree
polynomial Bezout combination** cannot improve (1.4).  The first saddle
cancellation from Item 420 is the only cancellation available over the
reals: at the next order the required coefficient is nonreal.

This is a sharply scoped no-go, not a theorem about the gcd itself.  It
does not exclude growing-degree or adaptive coefficients, combinations
using shifted rows, a joint resultant of two combinations, or arithmetic
nonconcentration.  Its ledger delta is exactly zero.

## 2. Common phase and the first exact cancellation

Use Item 420's constant-term model



$$
H(y)=\frac{(1-y)^6}{y^4(1+y^2)^4},
 \qquad
 f_0(y)=\frac{1+y}{1+y^2},
 \qquad
 f_1(y)=\frac{(1+y)^4}{y(1+y^2)^2},                     \tag{2.1}
$$



so that



$$
\lambda_{0,m}=\operatorname{CT}(f_0H^m),
 \qquad
 \lambda_{1,m}=\operatorname{CT}(f_1H^m).              \tag{2.2}
$$



The critical polynomial is



$$
P(y)=3y^3-6y^2-y-2,
 \qquad
 \frac{H'}H=\frac{2P(y)}{y(1-y)(1+y^2)}.                \tag{2.3}
$$



Item 420's exact identity is



$$
D_m:=2\lambda_{1,m}-5\lambda_{0,m}
 =\frac1m\operatorname{CT}(qH^m),                       \tag{2.4}
$$



where



$$
q(y)=\frac{y^4-4y^2-1}{2y(1+y^2)^2}.                  \tag{2.5}
$$



Equation (2.4) is an exact integration-by-parts identity, not an
asymptotic cancellation.  It saves one power of $m$, but Item 420 also
proved that $q$ is nonzero at every critical point.  Consequently it
cannot change an exponential rate by itself.

For arbitrary polynomial coefficients, put



$$
S(m)=A(m)+\frac52B(m).                                  \tag{2.6}
$$



Then the candidate Bezout combination has the exact decomposition



$$
\boxed{
 A(m)\lambda_{0,m}+B(m)\lambda_{1,m}
 =S(m)\lambda_{0,m}+\frac{B(m)}2D_m.}                   \tag{2.7}
$$



Thus all polynomially moving cancellations reduce to a competition
between the original amplitude and the single integrated amplitude.

## 3. The exact obstruction to a second real cancellation

Let $\alpha,\bar\alpha$ be the two dominant nonreal roots of $P$.
At a critical point define



$$
t(y)=\frac{q(y)}{f_0(y)}
 =\frac{y^4-4y^2-1}{2y(1+y^2)(1+y)}.                    \tag{3.1}
$$



Exact elimination gives



$$
\boxed{
 \operatorname{Res}_y\!\left(
 P(y),\,y^4-4y^2-1-2t\,y(1+y^2)(1+y)
 \right)
 =-16(320t^3-400t^2+220t-11).}                         \tag{3.2}
$$



The cubic on the right has discriminant



$$
-3,460,300,800<0.                                   \tag{3.3}
$$



Moreover,



$$
\operatorname{Res}(P,y^4-4y^2-1)=176,
 \qquad
 \operatorname{Res}(P,2y(1+y^2)(1+y))=5120.            \tag{3.4}
$$



Hence all three critical ratios are finite and nonzero.  The real critical
point gives the unique real root of the cubic in (3.2), while conjugation
maps the other two ratios to one another.  Therefore



$$
\boxed{t(\alpha)\notin\mathbb R,
 \qquad t(\bar\alpha)=\overline{t(\alpha)}.}            \tag{3.5}
$$



Numerically, only as a check,



$$
t(\alpha)=0.597341269672512\mp
 0.514389544198388,i.
$$



The exact negative discriminant (3.3), rather than this decimal, is the
proof of nonreality.

## 4. Proof of the polynomial Bezout theorem

Item 420's two-saddle lemma gives nonzero constants $C_0,C_q$ and a
nonreal number $\tau$, with $|\tau|=\rho_*$, such that



$$
\lambda_{0,m}=m^{-1/2}
 \left(C_0\tau^m+\overline{C_0}\,\overline\tau^m
 +O(\rho_*^m/m)\right),                                 \tag{4.1}
$$





$$
D_m=m^{-3/2}
 \left(C_q\tau^m+\overline{C_q}\,\overline\tau^m
 +O(\rho_*^m/m)\right).                                 \tag{4.2}
$$



The two local Gaussian factors are identical, so (2.1), (2.5), and the
local saddle calculation give the exact amplitude ratio



$$
\frac{C_q}{C_0}=\frac{q(\alpha)}{f_0(\alpha)}=t(\alpha).
                                                               \tag{4.3}
$$



Let $s=\deg S$ and $b=\deg B$, with the degree of the zero
polynomial interpreted as $-\infty$.  Equation (2.7) gives exactly
three cases.

1. If $s>b-1$, the $S\lambda_0$ term dominates.  Its leading saddle
   amplitude is the nonzero product of the leading coefficient of $S$
   and $C_0$.
2. If $s<b-1$, the $BD/2$ term dominates.  Its leading saddle
   amplitude is the nonzero product of the leading coefficient of $B$
   and $C_q/2$.
3. If $s=b-1$, the two terms have the same polynomial scale.  If
   $s_*$ and $b_*$ are their real rational leading coefficients, the
   leading amplitude at $\alpha$ is
   

$$
C_0\left(s_*+\frac{b_*}{2}t(\alpha)\right).          \tag{4.4}
$$


   Here $b_*\ne0$, and (3.5) makes (4.4) nonzero.

Thus every nonzero pair $(A,B)$ has an expansion



$$
m^e\left(C\tau^m+\bar C\bar\tau^m
 +O(\rho_*^m/m)\right),
 \qquad C\ne0,                                         \tag{4.5}
$$



for a half-integer $e$.  Writing
$\tau=\rho_*e^{i\phi}$ and $C=|C|e^{i\delta}$, the leading
conjugate sum is



$$
2|C|\rho_*^m\cos(m\phi+\delta).                        \tag{4.6}
$$



Since $\tau$ is nonreal, $e^{2i\phi}\ne1$, and therefore



$$
\frac1N\sum_{m=1}^N\cos^2(m\phi+\delta)\longrightarrow\frac12.
                                                               \tag{4.7}
$$



The cosine is bounded away from zero on an infinite subsequence.  The
upper bound follows directly from (4.5), and polynomial powers do not
affect $m$-th roots.  This proves (1.6).

Finally, after a fixed denominator is cleared,



$$
A(m)\mu_{0,m}+B(m)\mu_{1,m}
 =\frac{A(m)\lambda_{0,m}+B(m)\lambda_{1,m}}{F_m}.      \tag{4.8}
$$



Equation (1.2) turns (1.6) into (1.7).

## 5. Meaning for the genuinely joint gcd

Let



$$
g_m^>=\bigl(\gcd(|\mu_{0,m}|,|\mu_{1,m}|)\bigr)_{p>6m}.
$$



For integral $A,B$, one always has



$$
g_m^>\mid A(m)\mu_{0,m}+B(m)\mu_{1,m}.                 \tag{5.1}
$$



Thus a natural joint attack is to search for low-height Bezout
coefficients making the right side exponentially smaller.  Theorem (1.6)
closes the complete fixed-degree polynomial version of that attack:
no such single combination has exponential base below the already known
normalized base.

The word **single** is essential.  A true gcd theorem could still arise
from a pair of combinations and their determinant, a subresultant, a
finite-field common-zero theorem, or an adaptive coefficient choice.  In
particular, (1.6) does not imply that $g_m^>$ itself has exponential
size; all available exact scans are compatible with it being one.

The admission consequence is nonetheless useful.  Further searches of the
form



$$
(a_dm^d+\cdots+a_0)\mu_{0,m}
 +(b_dm^d+\cdots+b_0)\mu_{1,m}
$$



cannot lower the current component ceiling by ordinary height, regardless
of the fixed degree $d$.  The next admissible attack must introduce
genuinely new joint arithmetic information.

## 6. Ledger and de-overlap

All factors of $F_m$ are at most $6m$.  Dividing by $F_m$ therefore
preserves every valuation in (1.3), and no divisor is rebooked.

The exact ledger effect is



$$
\boxed{
 \Delta C_>=0,
 \quad \Delta r_{\rm booked}=0,
 \quad \Delta C_{\rm global}=0,
 \quad \Delta(T-r_1)=0.}                                \tag{6.1}
$$



The strictly-large component ceiling remains (1.4).  As in Items 415 and
418, that component ceiling is not an additive subtraction from a global
total-content ceiling.

## 7. Strict claim ledger

### PROVED

* The exact critical-ratio resultant (3.2) and negative discriminant
  (3.3).
* Nonreality of the next cancellation ratio at the two dominant saddles.
* The root-size theorem (1.6) for every nonzero pair in
  $\mathbb Q[m]^2$.
* The normalized theorem (1.7), preserving all $p>6m$ valuation depths.
* Zero change to every capacity and booking quantity.

### SHARPLY SCOPED NO-GO

* A same-index, fixed-degree polynomial-in-$m$ Bezout combination,
  bounded by its ordinary absolute height, cannot improve Item 418's
  exponential component ceiling.

### OPEN

* A direct bound for the actual gcd in (1.3), including
  $\log g_m^>=o(m)$ or $g_m^>=1$.
* Growing-degree, adaptive, or modularly selected coefficients.
* Shifted-row recurrences and joint resultants/subresultants.
* Weighted zero density for the actual normalized pair.
* Route-1 completion and irrationality of $e+\pi$.

### NOT CLAIMED

* That the normalized gcd has root base
  $\rho_*e^{-\mathfrak C_F}$.
* That a finite noncollision census proves support.
* That all possible Bezout or resultant methods are excluded.
* Any new booked divisor or irrationality proof.

## 8. Deterministic replay

Run

```text
python scripts/item423_polynomial_bezout_no_go_certificate.py \
  --output results/item423_polynomial_bezout_no_go_certificate_replay.json \
  --replay results/item423_polynomial_bezout_no_go_certificate.json
```

The standard-library replay:

1. pins canonical Items 415, 418, and 420 by SHA-256;
2. verifies (3.2) by exact Sylvester determinants;
3. verifies the exact discriminant and both nonvanishing resultants;
4. checks (2.4) and (2.7) on twenty-four exact integer rows and five
   polynomial-combination normalizations; and
5. reproduces the unchanged normalized base and component ceiling.

The saddle argument is a uniform proof in Sections 3--4.  The finite rows
only check exact normalization; they are not used to infer the theorem.
The canonical package is stored under `sources/`, `scripts/`, `results/`,
and `manifests/`.
