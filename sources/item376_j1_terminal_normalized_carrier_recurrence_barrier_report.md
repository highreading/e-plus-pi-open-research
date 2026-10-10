> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 376 — terminal-normalized $j=1$ carriers and a recurrence–height barrier

Checked: 2026-09-01 (Beijing time)

## 1. Verdict and admission check

Retain the actual fixed-$j=1$ family



$$
p=4h+6s+3,
 \qquad
 M=3h+4s+2,
 \qquad
 h,s\geq1,
 \qquad
 3\nmid h.
\tag{1.1}
$$



Item 372 proved characteristic-zero nonvanishing of the two first
boundary coordinates $X_h$ and $U_h$.  The present item normalizes by
the unique lowest $3$-adic terminal summands and obtains exact primitive
integer carriers for their possible vanishing modulo the selected prime.

> **PROVED — terminal-normalized carrier theorem.**  Put
> 

$$
> x_h={X_h\over T_h},
> \qquad
> u_h={U_h\over S_{h+2}},
>
$$


> where $T_h$ and $S_{h+2}$ are the terminal summands from Item 372.
> Then
> 

$$
> x_h,u_h\in1+3\mathbb Z_3.
>
$$


> Explicit finite sums give reduced fractions
> 

$$
> x_h={N_x(h)\over E_x(h)},
> \qquad
> u_h={N_u(h)\over E_u(h)}
>
$$


> with primitive integer numerator–denominator pairs.  On every actual
> row, $T_h,S_{h+2},E_x(h),E_u(h)$ are $p$-units.  Consequently
> 

$$
> X_h\equiv0\pmod p\iff p\mid N_x(h),
> \qquad
> U_h\equiv0\pmod p\iff p\mid N_u(h).
> \tag{1.2}
>
$$



The unreduced cleared sums are proper-hypergeometric finite sums on each
class $h\bmod3$, and hence are holonomic.  This does **not** give a
recurrence for the primitive numerators after nonlinear gcd reduction.
More importantly, even primitive integrality, congruence to $1$ modulo
$3$, fixed-order polynomial recurrence, and pointwise
$O(h\log h)$ height do not imply selector-weighted zero density.  An
explicit comparison sequence with all these properties is divisible by
the actual selected primes on a bulk of Chebyshev mass
$M/8+o(M)$, or capacity $1/48$ per $6M$.

Thus this item proves a usable exact overcarrier and a scoped no-go for a
broad recurrence/unit/height method class, but no asymptotic theorem for
the genuine paired gates.  The admission ledger is



$$
\boxed{\text{new booking}=0},
 \qquad
 \boxed{\text{new capacity reduction}=0},
 \qquad
 \boxed{\text{shared fixed-}j=1\text{ ceiling}=1/36}.
\tag{1.3}
$$



## 2. Exact reverse terminal-normalized sums

Write



$$
\sigma_h=-{4h+3\over6},
 \qquad
 K_0(z)=(1-z)^{2h}(1+z)=\sum_j k^{(0)}_jz^j,
\tag{2.1}
$$



and



$$
K_1(z)=(1-z)^{2h}(1+z)^4=\sum_j k^{(1)}_jz^j.
\tag{2.2}
$$



Both kernels are palindromic.  The terminal summands used in Item 372 are



$$
T_h=(-1)^h{(\sigma_h+1)_h\over(3\sigma_h+2)_h},
 \qquad
 S_{h+2}=(-1)^{h+2}{(\sigma_h)_{h+2}\over(3\sigma_h)_{h+2}}.
\tag{2.3}
$$



Reverse the original sums by writing $r=h-t$ for $X_h$ and
$r=h+2-t$ for $U_h$.  Palindromy changes the kernel coefficients to
$k^{(0)}_{2r}$ and $k^{(1)}_{2r}$.  The identity



$$
(a-r)_r=(-1)^r(1-a)_r
\tag{2.4}
$$



then gives the exact formulas



$$
\boxed{
 x_h=
 \sum_{r=0}^{h}(-1)^r k^{(0)}_{2r}
 {\left(h+\frac12\right)_r\over
  \left(\frac12-\frac h3\right)_r}}
\tag{2.5}
$$



and



$$
\boxed{
 u_h=
 \sum_{r=0}^{h+2}(-1)^r k^{(1)}_{2r}
 {\left(h+\frac12\right)_r\over
  \left(-\frac12-\frac h3\right)_r}.}
\tag{2.6}
$$



The $r=0$ term in each formula is $1$.  Item 372's factor-by-factor
valuation argument, read in reverse order, says every $r$-th correction
has $3$-adic valuation at least $r$.  Hence



$$
\boxed{x_h,u_h\in1+3\mathbb Z_3.}
\tag{2.7}
$$



This is stronger than mere characteristic-zero nonvanishing, but it is
not nonvanishing modulo an arbitrary actual prime $p\ne3$.

## 3. Exact primitive integer clearing

For the first normalized value define



$$
D_x(h)=\prod_{j=0}^{h-1}(3-2h+6j)
\tag{3.1}
$$



and



$$
\begin{split}
 A_x(h)=\sum_{r=0}^{h}&(-1)^r k^{(0)}_{2r}3^r
 \prod_{i=0}^{r-1}(2h+1+2i)\\
 &\mathrel{}\times
 \prod_{j=r}^{h-1}(3-2h+6j).
\end{split}
\tag{3.2}
$$



Empty products are $1$.  Directly clearing the prefix denominator in
each summand of (2.5) gives



$$
\boxed{x_h={A_x(h)\over D_x(h)}.}
\tag{3.3}
$$



Similarly put



$$
D_u(h)=\prod_{j=0}^{h+1}(-3-2h+6j)
\tag{3.4}
$$



and



$$
\begin{split}
 A_u(h)=\sum_{r=0}^{h+2}&(-1)^r k^{(1)}_{2r}3^r
 \prod_{i=0}^{r-1}(2h+1+2i)\\
 &\mathrel{}\times
 \prod_{j=r}^{h+1}(-3-2h+6j).
\end{split}
\tag{3.5}
$$



Then



$$
\boxed{u_h={A_u(h)\over D_u(h)}.}
\tag{3.6}
$$



None of the displayed denominator factors is zero.  Because
$k^{(0)}_0=k^{(1)}_0=1$, only the $r=0$ term survives modulo $3$,
so



$$
A_x(h)\equiv D_x(h)\not\equiv0\pmod3,
 \qquad
 A_u(h)\equiv D_u(h)\not\equiv0\pmod3.
\tag{3.7}
$$



Now take the exact primitive reductions



$$
g_x(h)=\gcd(A_x(h),D_x(h)),
 \quad
 N_x(h)={A_x(h)\over g_x(h)},
 \quad
 E_x(h)={D_x(h)\over g_x(h)},
\tag{3.8}
$$



and analogously $g_u,N_u,E_u$, normalizing both denominators to be
positive.  These are the minimal reduced numerator–denominator pairs.
Equation (3.7) also proves that all four primitive integers are
$3$-units and recovers (2.7).

The elementary binomial bound on the kernel coefficients and the
$O(h)$-size of every linear factor give



$$
\log\max\bigl(
 |N_x(h)|,E_x(h),|N_u(h)|,E_u(h)
 \bigr)=O(h\log(h+2)).
\tag{3.9}
$$



## 4. Actual-family modular bridge

Every factor in $D_x(h)$ has absolute value at most $4h-3$, and every
factor in $D_u(h)$ has absolute value at most $4h+3$.  Expanding
(2.3) shows that the integer linear factors in its numerators and
denominators also have absolute value at most $4h+3$.  On an actual row,



$$
p=4h+6s+3\geq4h+9.
\tag{4.1}
$$



Therefore $D_x,D_u,T_h,S_{h+2}$, and hence $E_x,E_u$, are all
$p$-units.  This proves the equivalences (1.2).  In particular, for the
two boundary events of Items 364 and 368,



$$
\boxed{
 \mathcal B_{xy}(h,s)\Longrightarrow p\mid N_x(h),
 \qquad
 \mathcal B_{uv}(h,s)\Longrightarrow p\mid N_u(h).}
\tag{4.2}
$$



These are exact actual-family one-coordinate **overcarriers**.  They are
weaker than the paired gcd carriers, since (4.2) forgets the simultaneous
$Y_h$ or $V_h$ congruence.  They must not be booked independently or
added to the capacity of those paired gates.

## 5. What holonomicity does and does not prove

The kernel coefficients have the explicit forms



$$
k^{(0)}_{2r}
 =\binom{2h}{2r}-\binom{2h}{2r-1}
\tag{5.1}
$$



and



$$
k^{(1)}_{2r}
 =\sum_{a=0}^{4}(-1)^a\binom4a\binom{2h}{2r-a}.
\tag{5.2}
$$



After fixing $h\bmod3$, every summand in (3.2) is proper
hypergeometric in the remaining row parameter and $r$; (3.5) is a
fixed sum of five such terms.  Standard creative telescoping therefore
proves:

> **PROVED.**  On each residue class $h\bmod3$, the unreduced sequences
> $A_x(h)$, $D_x(h)$, $A_u(h)$, and $D_u(h)$ satisfy fixed-order
> recurrences with polynomial coefficients.

This is an existence theorem; no guessed recurrence is promoted.  It does
not imply the same statement for



$$
N_x(h)={A_x(h)\over\gcd(A_x(h),D_x(h))},
 \qquad
 N_u(h)={A_u(h)\over\gcd(A_u(h),D_u(h))},
\tag{5.3}
$$



because primitive reduction is nonlinear.  A fixed-order polynomial
recurrence for either primitive numerator remains **OPEN**.

Even such a recurrence would propagate divisibility modulo one fixed
prime, whereas the actual fixed-$M$ selector is



$$
p_h={3M-h\over2}.
\tag{5.4}
$$



Consecutive actual parameters satisfy $h\mapsto h+4$,
$s\mapsto s-3$, and $p_h\mapsto p_h-2$.  Thus ordinary recurrence
propagation does not couple the relevant events at their moving moduli.
A useful resultant would need target-specific information relating these
different primes; neither (3.9) nor holonomicity supplies it.

## 6. A sharp comparison for the proposed method class

The preceding limitation is not merely a failure to find a recurrence.
Define



$$
P_h=\prod_{\substack{4h<k\leq18h\\3\nmid k}}k,
 \qquad
 C_h=P_h^2.
\tag{6.1}
$$



Then $C_h$ has all the generic features just obtained for a primitive
normalized carrier:



$$
C_h\in\mathbb Z,
 \qquad
 C_h\equiv1\pmod3,
 \qquad
 \log C_h=O(h\log(h+2)).
\tag{6.2}
$$



It also satisfies a first-order polynomial recurrence on each class
$h\bmod3$.  Indeed, let



$$
E_h=\prod_{\substack{4h<k\leq4h+12\\3\nmid k}}k,
 \qquad
 R_h=\prod_{\substack{18h<k\leq18h+54\\3\nmid k}}k.
\tag{6.3}
$$



There are exactly $8$ and $36$ factors, respectively, and interval
cancellation gives



$$
\boxed{E_h^2C_{h+3}=R_h^2C_h.}
\tag{6.4}
$$



On a fixed residue class the two coefficients in (6.4) are fixed-degree
polynomials in $h$.  Thus $C_h$ has a stronger recurrence than the
mere holonomic existence obtained in Section 5.

Nevertheless, in the actual bulk



$$
{M\over12}\leq h\leq {M\over3},
\tag{6.5}
$$



the selected prime satisfies



$$
4h+3<p_h={3M-h\over2}<18h.
\tag{6.6}
$$



Apart from endpoint effects of $O(\log M)$, every prime in



$$
{4M\over3}<p\leq {35M\over24}
\tag{6.7}
$$



corresponds to an actual $(h,s)$ in (6.5), and it divides $C_h$.
The prime number theorem therefore gives the exact asymptotic obstruction



$$
\sum_{\substack{p\text{ represented in the bulk}}}
 (\log p)\,1_{p\mid C_{3M-2p}}
 ={M\over8}+o(M).
\tag{6.8}
$$



After division by $6M$, this is capacity



$$
\boxed{{1\over48}.}
\tag{6.9}
$$



Hence no theorem whose hypotheses use only primitive integrality,
membership in $1+3\mathbb Z_3$, fixed-order polynomial recurrence, and
pointwise $O(h\log h)$ height can force selector-weighted zero density.
The comparison already has positive linear selector mass.  This is a
scoped method-class obstruction, not a theorem that the genuine carriers
have positive mass.

## 7. Capacity and strategic consequence

The full fixed-$j=1$ gate has raw mass $M/6+o(M)$, hence shared ceiling
$1/36$ per $6M$.  The two saturation boundaries partition/overlap the
same full gate with its nonboundary chart; their one-coordinate
overcarriers are not additive ledger cells.

The comparison in Section 6 shows that the normalized recurrence–height
package alone cannot prove the required $o(M)$ exceptional mass.  It
does not prove any lower bound for the actual carrier, so $1/48$ is not
booked.  The correct delta is



$$
\boxed{
 \Delta r_1=0,
 \qquad
 \Delta\text{capacity}=0,
 \qquad
 \text{retained shared ceiling}=1/36.}
\tag{7.1}
$$



The first missing arithmetic input is selector-aware cross-prime
information: for example an average-gcd theorem or a reciprocity/resultant
identity that relates $N_x(3M-2p)$ and $N_u(3M-2p)$ to the moving prime
$p$, while retaining the second coordinate of the relevant paired gate.

## 8. Strict labels

### PROVED

- the exact reverse sums (2.5) and (2.6);
- $x_h,u_h\in1+3\mathbb Z_3$ for every $3\nmid h$;
- the exact cleared formulas (3.1)–(3.6) and their primitive reductions;
- the actual-prime equivalences (1.2) and boundary overcarriers (4.2);
- $O(h\log h)$ pointwise height;
- holonomicity of the unreduced cleared sequences on each $h\bmod3$
  class;
- the explicit first-order comparison recurrence (6.4);
- the comparison's $M/8+o(M)$ selector mass and $1/48$ capacity;
- the scoped recurrence/unit/height no-go;
- zero booking, zero capacity reduction, and retention of the shared
  $1/36$ ceiling.

### EXACT FINITE ONLY

- eight declared normalized symbolic controls, four actual-row bridge
  controls, six recurrence controls, and three comparison controls in the
  deterministic replay;
- no prime scan, collision census, recurrence guessing, or extrapolation.

### OPEN

- a fixed-order polynomial recurrence for either primitive reduced
  numerator sequence;
- a target-specific small-height resultant, cross-prime average gcd, or
  weighted zero-density theorem for the actual paired gates;
- any strict reduction of the shared fixed-$j=1$ ceiling;
- Route 1 and every conclusion about $e+\pi$.

Characteristic-zero nonvanishing and $3$-adic unit normalization must
not be confused with nonvanishing modulo the selected prime.
