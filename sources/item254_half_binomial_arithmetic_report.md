> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 254 — arithmetic forms of the half-binomial prefix

Checked: 2026-08-31 (Beijing time)

## 1. Scope and verdict

On an actual ordinary-(j=2) row put



$$
p=2r+6s+3,\qquad r\geq1\text{ odd},\qquad 3\nmid r,\qquad
 m=s-1,
 \tag{1.1}
$$



and write



$$
n={p-1\over2}=3m+d,\qquad d=r+4,\qquad
 h_j={\binom{2j}{j}\over8^j},\qquad
 H_m=\sum_{j=0}^m h_j,
 \tag{1.2}
$$



with $\varepsilon=(2/p)\in\{\pm1\}$.  Item 252 showed that this
prefix is the remaining universal period in the ordinary-(j=2) diagonal.
This item tests character sums, reflection, and valuations at the actual
phase



$$
6m=p-(2r+9).                    \tag{1.3}
$$



The outcome is as follows.

> **PROVED — one exact finite-field Mellin period.**  Define in
> $\mathbf F_p[z]$
> 

$$
> C_p(z)=\sum_{k=0}^n H_kz^k.
>
$$


> Then
> 

$$
> (1-z)C_p(z)=(1-z/2)^n-\varepsilon z^{n+1},\qquad C_p(1)=0, \tag{1.4}
>
$$


> and
> 

$$
> \boxed{H_m=-\sum_{x\in\mathbf F_p^*}x^{-m}C_p(x).}     \tag{1.5}
>
$$


> Pointwise, with the value at $x=1$ defined as zero,
> 

$$
> C_p(x)={\chi(1-x/2)-\varepsilon x\chi(x)\over1-x}.     \tag{1.6}
>
$$



> **PROVED — Jacobi/Greene split.**  The Mellin period is the difference
> of one three-point Greene sum and one explicit Jacobi unit.  In the
> notation of Section 3,
> 

$$
> \boxed{H_m\equiv-\mathcal T_p+\varepsilon\mathcal J_p,
> \qquad \mathcal J_p\equiv n-m+1\not\equiv0\pmod p.}    \tag{1.7}
>
$$


> The character $\theta=\omega^{-m}$ in $\mathcal T_p$ satisfies
> 

$$
> \theta^6=\omega^{2r+8},\qquad
> \operatorname {ord}(\theta)
> ={p-1\over\gcd(m,2r+8)}\ge {p-1\over2r+8}.             \tag{1.8}
>
$$


> Moreover $\omega^{-1}(1-x)$, which encodes the incomplete cutoff,
> has order $p-1$.  Splitting $p\equiv1,5\pmod6$ does localize the
> *unweighted character factor* to a fixed genus-one Kummer cover, but the
> cutoff survives as a field-valued rational weight with a puncture.  Thus
> the prefix is not reduced to an unweighted Jacobi/elliptic trace.

> **PROVED — algebraic incomplete-beta form with all units audited.**
> If formal integration means coefficientwise antidifferentiation in
> $\mathbf F_p[u]$, then
> 

$$
> \boxed{
> H_m=2^{-m}(2m+d)\binom{3m+d}{m}
>       \int_0^1u^{2m+d-1}(1-2u)^m\,du\pmod p.}           \tag{1.9}
>
$$


> Every denominator in the integral lies between $2m+d$ and
> $3m+d=n<p$, and the prefactor is a $p$-unit.  This is an
> *incomplete* beta value, not a complete Jacobi sum.

> **PROVED — fixed-cutoff boundary compression.**  With
> $q=\lfloor p/6\rfloor$, the actual $H_m$ differs from $H_q$ by
> a fixed number of explicit $p$-unit endpoint terms when $r$ is
> fixed.  The exact formulas are in Section 5.

> **PROVED — universal nonvanishing of the prefix is false.**  Two exact
> actual rows are
> 

$$
> H_2={43\over32}\equiv0\pmod {43},\quad (p,r,s)=(43,11,3),
> \tag{1.10}
>
$$


> and
> 

$$
> H_4={2867\over2048}={47\cdot61\over2048}\equiv0\pmod {47},
> \quad (p,r,s)=(47,7,5).                                  \tag{1.11}
>
$$



> **PROVED — a weighted numerator-container bound, but not zero rate.**
> If $s_2(m)$ is the binary digit sum and $\mathcal Z_m$ is any set
> of distinct odd primes for which $H_m=0\pmod p$, then
> 

$$
> \boxed{
> \sum_{p\in\mathcal Z_m}\log p
> <\bigl(3m-s_2(m)+\tfrac12\bigr)\log2.}                  \tag{1.12}
>
$$


> The right side divided by $6m$ tends to
> $\log2/2=0.34657359\ldots$, not zero.  Hence this height argument
> supplies a rigorous weighted bound but not the weighted zero-rate theorem
> required by the Route-1 ledger.

The exact character and beta representations therefore sharpen the remaining
arithmetic problem, but they do not prove a usable all-prime exclusion or a
zero weighted-rate theorem for the full gate.  This item books no rate.

## 2. Prefix polynomial and coefficient orthogonality

For $0\leq j\leq n=(p-1)/2$,



$$
\binom nj\equiv(-1)^j{\binom{2j}{j}\over4^j}\pmod p,
$$



so



$$
h_j\equiv\binom nj\left(-{1\over2}\right)^j\pmod p.     \tag{2.1}
$$



Consequently



$$
Q_p(z):=(1-z/2)^n=\sum_{j=0}^nh_jz^j,
 \qquad Q_p(1)=2^{-n}=\varepsilon.                         \tag{2.2}
$$



For $C_p(z)=\sum_{k=0}^nH_kz^k$, taking first differences of the
prefixes gives



$$
(1-z)C_p(z)=Q_p(z)-H_nz^{n+1}
             =Q_p(z)-\varepsilon z^{n+1},                 \tag{2.3}
$$



which proves the first identity in (1.4).  At $z=1$, differentiate
(2.3).  Since



$$
Q_p'(1)=-n\varepsilon,
$$



we get



$$
C_p(1)=-Q_p'(1)+\varepsilon(n+1)
       =(2n+1)\varepsilon=p\varepsilon=0\quad\text{in }\mathbf F_p.
 \tag{2.4}
$$



Now $\deg C_p=n<p-1$.  Multiplicative power orthogonality gives, for
every actual $0\leq m<n$,



$$
\sum_{x\in\mathbf F_p^*}x^{-m}C_p(x)=-[z^m]C_p(z)=-H_m, \tag{2.5}
$$



including $m=0$, where the constant coefficient is the unique surviving
power.  This proves (1.5).

Euler's criterion applied pointwise to (2.3) gives



$$
Q_p(x)=\chi(1-x/2),\qquad x^{n+1}=x\chi(x).               \tag{2.6}
$$



For $x\ne1$, division in (2.3) proves (1.6); (2.4) supplies its regular
value $C_p(1)=0$.  No singular endpoint is discarded.

## 3. Exact Jacobi/Greene decomposition and its limitation

Let $\omega:\mathbf F_p^*\to\mu_{p-1}$ be the Teichmuller character,
let $\phi=\omega^n$ be the quadratic character, and extend every
multiplicative character by zero at zero.  Fix the prime above $p$ for
which reduction of $\omega(x)$ is $x$.  Put



$$
\theta=\omega^{-m},\qquad \bar\omega=\omega^{-1},        \tag{3.1}
$$



and define the algebraic-integer character sums



$$
\begin{aligned}
 \mathcal T_p&=\sum_{x\in\mathbf F_p}
   \theta(x)\phi(1-x/2)\bar\omega(1-x),\\
 \mathcal J_p&=J(\theta\omega^{n+1},\bar\omega)
   =\sum_{x\in\mathbf F_p}
   \theta(x)\omega^{n+1}(x)\bar\omega(1-x).
\end{aligned}                                               \tag{3.2}
$$



The first is the usual unnormalized three-point finite-field beta integral
underlying a Greene ${}_2F_1$ value at $1/2$.  The second is an ordinary
Jacobi sum.  Reducing (3.2) at the chosen prime and using (1.6) gives



$$
H_m\equiv-\mathcal T_p+\varepsilon\mathcal J_p.           \tag{3.3}
$$



The endpoint $x=1$ contributes zero to both sums, exactly matching
$C_p(1)=0$.

Set



$$
a=n-m+1=2m+d+1.
$$



Then $1\leq a\leq p-2$, and reduction of the Jacobi sum is



$$
\mathcal J_p\equiv
 \sum_{x\in\mathbf F_p\setminus\{0,1\}}{x^a\over1-x}=a
 \pmod p.                                                   \tag{3.4}
$$



For completeness, the last identity follows from the finite-field power
sums (or inductively from the difference of the cases $a$ and $a-1$);
the case $a=1$ is one directly evaluated inverse sum.  In particular,
$\mathcal J_p$ is a $p$-adic unit.

The phase (1.3) does impose a Kummer relation:



$$
\theta^6=\omega^{-6m}=\omega^{2r+8}.                      \tag{3.5}
$$



It does **not** make $\theta$ a character of bounded order.  Indeed



$$
\gcd(m,p-1)=\gcd(m,6m+2r+8)=\gcd(m,2r+8),                \tag{3.6}
$$



which proves (1.8).  For fixed $r$, its order therefore grows at least
linearly with $p$.  Independently, the character $\bar\omega(1-x)$
introduced by the incomplete denominator has full order $p-1$.

This explains one precise difference from familiar fixed-order Jacobi
evaluations: in the direct Teichmuller lift the incomplete cutoff has not
disappeared.  The residue-class substitutions below expose a fixed-order
genus-one character factor, but retain a rational puncture and a
field-valued weight.  Equation (3.3) is therefore a useful exact
localization, while standard unit formulas for *unweighted* Jacobi sums do
not force the difference in (3.3) to be a unit.  The exact cancellations
(1.10)--(1.11) show that such a force cannot hold for $H_m$ on all actual
rows.

There is also a direct termwise Jacobi expansion.  For $0\leq j\leq m$,



$$
J(\omega^{-j},\phi)\equiv-(-1)^j\binom nj\not\equiv0\pmod p,
 \tag{3.7}
$$



and hence



$$
H_m\equiv-\sum_{j=0}^m2^{-j}J(\omega^{-j},\phi)\pmod p.  \tag{3.8}
$$



Every summand in (3.8) is a $p$-adic unit.  Thus there is no unique
lowest-valuation term; termwise Jacobi valuations alone cannot prevent
cancellation.

### 3.1 The two residue classes and a fixed genus-one factor

The phase can be sharpened without pretending that the rational cutoff is
gone.

If $p\equiv1\pmod6$, put



$$
q={p-1\over6},\qquad \delta={r+4\over3},\qquad
 \rho(x)=x^q.
$$



Then $\rho$ has order six and $m=q-\delta$, so



$$
x^{-m}=x^\delta\rho^{-1}(x).                              \tag{3.9}
$$



The three-point term becomes



$$
\mathcal T_p\equiv
 \sum_{x\in\mathbf F_p\setminus\{0,1\}}
 {x^\delta\rho^{-1}(x)\chi(1-x/2)\over1-x}\pmod p.       \tag{3.10}
$$



Without the rational weight $x^\delta/(1-x)$, the character factor in
(3.10) is the usual sextic/quadratic Jacobi factor.  Equivalently it is the
trace factor of the fixed Kummer cover



$$
Y^6={(1-x/2)^3\over x},            \tag{3.11}
$$



which has genus one: the ramification contributions at $0,2,\infty$ are
$5,3,4$, giving $-12+5+3+4=0=2g-2$.  Formula (3.10), however, is a
rationally weighted moment on the curve punctured at $x=1$, not its
unweighted Frobenius trace.

If $p\equiv5\pmod6$, the cube map is a permutation of $\mathbf F_p$.
Since



$$
3m=n-(r+4),
$$



substitution $y=x^3$ in (1.5) gives



$$
H_m=-\sum_{x\in\mathbf F_p^*}x^{r+4}\chi(x)C_p(x^3).     \tag{3.12}
$$



Splitting the explicit Jacobi term, with $a=n-m+1=2m+r+5$, yields



$$
\boxed{
 H_m=\varepsilon a-
 \sum_{x\in\mathbf F_p\setminus\{0,1\}}
 {x^{r+4}\chi\!\left(x(1-x^3/2)\right)\over1-x^3}
 \pmod p.}                                                 \tag{3.13}
$$



Indeed $3a-(r+7)=p-1$, so the cube permutation and (3.4) give



$$
\sum_{x\in\mathbf F_p\setminus\{0,1\}}{x^{r+7}\over1-x^3}
 =\sum_{y\in\mathbf F_p\setminus\{0,1\}}{y^a\over1-y}=a. \tag{3.14}
$$



The quadratic character in (3.13) belongs to the genus-one curve



$$
y^2=x(1-x^3/2).                                           \tag{3.15}
$$



Under $X=1/x$, $Y=y/x^2$, this is birational to the fixed
$j=0$ curve



$$
Y^2=X^3-1/2.                       \tag{3.16}
$$



For $p\equiv5\pmod6$, its unweighted quadratic trace is zero: the cube
map is bijective and
$\sum_X\chi(X^3-1/2)=\sum_t\chi(t-1/2)=0$.  This does not evaluate
(3.13), whose factor $x^{r+4}/(1-x^3)$ and puncture at $x=1$ remain.
Thus the fixed CM curve localization supplies no all-prime nonvanishing or
zero-density theorem by itself.

## 4. Incomplete beta integral and unit audit

For integers $0\leq m<n$, the elementary incomplete-beta identity is



$$
\sum_{j=0}^m\binom njx^j
 =(1+x)^n I_{1/(1+x)}(n-m,m+1),                             \tag{4.1}
$$



where



$$
I_z(a,b)={(a+b-1)!\over(a-1)!(b-1)!}
              \int_0^z t^{a-1}(1-t)^{b-1}\,dt.            \tag{4.2}
$$



For integral $a,b$, this is a polynomial identity over $\mathbf Q$;
it follows equally by expanding the integrand and differentiating.  Put
$x=-1/2$, so that $1/(1+x)=2$, and substitute $t=2u$.  Equations
(2.1), (4.1), and $n=3m+d$ yield (1.9).

Explicitly, the finite-field integral in (1.9) is



$$
\int_0^1u^{2m+d-1}(1-2u)^m\,du
 =\sum_{k=0}^m{\binom mk(-2)^k\over2m+d+k}.                \tag{4.3}
$$



Its denominator range is



$$
0<2m+d\leq2m+d+k\leq3m+d=n={p-1\over2}<p.                \tag{4.4}
$$



Also $2m+d=n-m$ and $\binom nm$ are $p$-units.  Therefore



$$
H_m=0\pmod p
 \quad\Longleftrightarrow\quad
 \int_0^1u^{2m+d-1}(1-2u)^m\,du=0\pmod p.                 \tag{4.5}
$$



This reformulates the problem without any hidden denominator or omitted
endpoint.  It does not evaluate the incomplete beta value.  Replacing (4.3)
by a complete finite-field character sum would change the object and is not
justified.

## 5. Reflection to the natural $\lfloor p/6\rfloor$ cutoff

Let $q=\lfloor p/6\rfloor$.  The actual index is a fixed backward shift
from $q$:



$$
\begin{array}{c|c|c}
 p\bmod6&r\bmod3&\delta=q-m\\ \hline
 1&2&(r+4)/3\\
 5&1&(r+2)/3.
\end{array}                                                  \tag{5.1}
$$



The backward quotient of consecutive terms is



$$
{h_{q-k}\over h_q}=\prod_{i=0}^{k-1}{4(q-i)\over2(q-i)-1}. \tag{5.2}
$$



Reducing $q=(p-1)/6$ or $(p-5)/6$ in (5.2) gives the fixed rational
boundary sums



$$
\begin{aligned}
 B^{(1)}_\delta
 &=\sum_{k=0}^{\delta-1}\prod_{i=0}^{k-1}{6i+1\over3i+2}
   =\sum_{k=0}^{\delta-1}2^k{(1/6)_k\over(2/3)_k},\\
 B^{(5)}_\delta
 &=\sum_{k=0}^{\delta-1}\prod_{i=0}^{k-1}{6i+5\over3i+4}
   =\sum_{k=0}^{\delta-1}2^k{(5/6)_k\over(4/3)_k}.
\end{aligned}                                               \tag{5.3}
$$



Thus



$$
\boxed{
 H_m=H_q-h_qB^{(p\bmod6)}_\delta\pmod p.}                  \tag{5.4}
$$



All factors in (5.2)--(5.3) are units.  For the ratios actually used,
their integer denominators are at most $r<p$, and their numerators are
at most $2r-3<p$.  Also $2q<p$, so
$h_q=\binom{2q}{q}/8^q$ is a unit.

Consequently, if



$$
Z_p={H_q\over h_q},                                       \tag{5.5}
$$



then an actual zero is exactly the fixed-rational collision



$$
Z_p=B^{(p\bmod6)}_\delta.                                 \tag{5.6}
$$



This is a useful phase normalization.  It does not evaluate the base period
$Z_p$.  Classical complete central-binomial congruences determine the sum
through $(p-1)/2$, and the known $\lfloor p/6\rfloor$ Legendre-polynomial
trace formulas involve additional $\binom{3k}{k}\binom{6k}{3k}$ factors.
Neither operation may be substituted for the incomplete plain prefix in
(5.5).

## 6. Exact zeros and the numerator-container theorem

Put



$$
U_m=8^mH_m=\sum_{j=0}^m\binom{2j}{j}8^{m-j}\in\mathbf Z.  \tag{6.1}
$$



The standard binary valuation is



$$
v_2\binom{2j}{j}=s_2(j).                                  \tag{6.2}
$$



The final term $j=m$ in (6.1) has valuation $s_2(m)$.  If
$j=m-k<m$, binary subadditivity gives



$$
s_2(m)\leq s_2(m-k)+s_2(k)\leq s_2(m-k)+k,
$$



and hence



$$
v_2\!\left(\binom{2(m-k)}{m-k}8^k\right)
 =s_2(m-k)+3k>s_2(m).                                     \tag{6.3}
$$



The minimum valuation in (6.1) is therefore unique, so



$$
v_2(U_m)=s_2(m),\qquad
 H_m={N_m\over2^{3m-s_2(m)}}                               \tag{6.4}
$$



in lowest terms, where $N_m=U_m/2^{s_2(m)}$ is odd.

Because the infinite positive series is $\sqrt2$,



$$
0<N_m<2^{3m-s_2(m)+1/2}.                                  \tag{6.5}
$$



Every odd prime with $H_m=0\pmod p$ divides $N_m$.  Taking the
product over distinct primes proves (1.12).  On an actual row one also has
$p\geq6m+11$, so



$$
\#\mathcal Z_m^{\rm actual}
 <{(3m-s_2(m)+1/2)\log2\over\log(6m+11)}.                 \tag{6.6}
$$



This proves finiteness and an $O(m/\log m)$ count for each fixed $m$,
but not zero logarithmic weight.  Indeed $H_m\to\sqrt2$ and
$s_2(m)=O(\log m)$, so



$$
{\log N_m\over6m}\longrightarrow{\log2\over2}.          \tag{6.7}
$$



The exact identities



$$
U_2=86=2\cdot43,qquad U_4=5734=2\cdot47\cdot61          \tag{6.8}
$$



give (1.10)--(1.11) and disprove universal nonvanishing on actual rows.
These are zeros of the isolated prefix; they are not asserted to be common
zeros of both original Item 250 gates.

## 7. Reproducibility and strict labels

The companion standard-library checker verifies:

1. coefficient identity (2.1), prefix polynomial (2.3), and $C_p(1)=0$;
2. the pointwise character formula, Mellin extraction, Greene split, explicit
   Jacobi unit, sixth-power relation, and character-order bound;
3. the incomplete-beta formula and every denominator range;
4. the fixed-cutoff boundary formulas for both prime residues;
5. the exact binary valuation, reduced denominator, height inequality, and
   the two symbolic zero witnesses.

Its row and character censuses are **EXACT FINITE ONLY**.  They are regression
tests for the proved identities and are not extrapolated.

Classification:

* **PROVED:** (1.4)--(1.9), (5.1)--(5.6), the exact actual zeros
  (1.10)--(1.11), and the weighted numerator-container theorem
  (1.12)/(6.6).
* **EXACT FINITE ONLY:** all counts and extra witnesses in the JSON output.
* **OPEN:** a transformation of the moving high-order three-point period to
  a bounded-order invariant; a zero weighted-rate theorem for actual moving
  rows; all-prime or zero-rate control of the full Item 251 gate; and any
  resulting Route-1 capacity reduction.

Accordingly,



$$
\boxed{\text{new unconditional rate}=0,\qquad
        \text{capacity reduction}=0.}                       \tag{7.1}
$$


