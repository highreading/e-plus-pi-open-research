> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 293 — integral recurrence and density barrier for the sole $j=1$ gate

Date: 2026-08-31

## 1. Outcome

After Item 288, the endpoint scalar $K_h$ is redundant at every actual
moving prime.  The sole surviving fixed-$j=1$ arithmetic gate is



$$
E_h^*\equiv0\pmod p,        \tag{1.1}
$$



where



$$
p=4h+6s+3,\qquad h,s\geq1,\qquad3\nmid h.          \tag{1.2}
$$



This item proves three exact statements.

First, $E_h^*$ satisfies a primitive integral order-three, step-three
recurrence



$$
\boxed{\sum_{k=0}^{3}Q_k(h)E_{h+3k}^*=0},\qquad Q_k\in\mathbb Z[h],
                                                               \tag{1.3}
$$



in both nonzero residue classes modulo $3$.  Every $Q_k$ has degree
22, their individual integer contents are
$(4096,512,4,27)$, whose gcd is one, their common polynomial gcd is
one, and



$$
Q_0(h),Q_1(h),Q_2(h)<0<Q_3(h)\qquad(h\geq1).       \tag{1.4}
$$



The recurrence is derived symbolically from Item 237's proved recurrence
and Item 243's proved gauge; it is not reconstructed from values.

Second, the signs propagate:



$$
\boxed{E_h^*<0\quad(h\equiv1\pmod3),\qquad
        E_h^*>0\quad(h\equiv2\pmod3).}              \tag{1.5}
$$



Thus the rational gate is never identically zero at an admissible index.
This does not imply nonvanishing after reduction modulo the moving prime.

Third, remove every prime-power factor at primes at most $4h+3$ from the
reduced numerator $N_E(h)$, and call the resulting positive integer
$M_h$.  Item 288's localization and Item 243's gauge prove that $M_h$
is exactly the $>4h+3$ part of the numerator of



$$
c_h=[x^{2h}]C(x),           \tag{1.6}
$$



where $C(x)$ is Item 237's fixed algebraic series.  This is an all-$h$
algebraic generating-function description of the primitive large-prime
gate.

The recurrence and algebraicity give only



$$
\log\operatorname {rad}(M_h)=O(h),\qquad
 \sum_{\substack{h\leq H\\3\nmid h}}
       \log\operatorname {rad}(M_h)=O(H^2).         \tag{1.7}
$$



They do not give the required $o(H)$ weighted actual-prime bound.  A
rigorous comparison sequence proves the following narrowly scoped no-go:

> Algebraicity or rationality, a fixed-order integral recurrence,
> integrality, and exponential height alone cannot imply an
> $o(H)$ bound for primes tied to the actual row $p=4h+6s+3$.

This does not obstruct a sequence-specific congruence, monodromy,
fixed-diagonal, or auxiliary-local argument for the exact $E_h^*$
sequence.

The conditional $j=1$ ceiling remains $1/6$ per $m$, equivalently
$1/36$ per $6m$.  The new booked rate, exponent, and capacity
reduction are all zero.

## 2. Symbolic derivation of the integral recurrence

Item 237 proves



$$
\sum_{k=0}^{3}p_k(h)c_{h+3k}=0.                   \tag{2.1}
$$



Item 243 proves



$$
c_h=\mathcal G_hE_h^*,\qquad
 \frac{\mathcal G_{h+3}}{\mathcal G_h}=\rho(h),    \tag{2.2}
$$



where



$$
\rho(h)=
\frac{h(4h+1)(4h+5)(4h+7)(4h+9)(4h+11)(4h+15)^2}
{864(h+1)(h+2)(2h+1)^2(2h+3)(2h+5)^2(4h+3)}.      \tag{2.3}
$$



Substitution of (2.2) into (2.1), followed only by division by the nonzero
$\mathcal G_h$, gives



$$
\sum_{k=0}^{3}p_k(h)
 \left(\prod_{j=0}^{k-1}\rho(h+3j)\right)E_{h+3k}^*=0.        \tag{2.4}
$$



Clear the common rational-function denominator in (2.4), then divide the
four coefficients by their common polynomial gcd and their common integer
content.  The result is (1.3).  The checker verifies, in
$\mathbb Q(h)$, that



$$
\frac{Q_k(h)}
 {p_k(h)\prod_{j=0}^{k-1}\rho(h+3j)}               \tag{2.5}
$$



is independent of $k$.  Thus the displayed $Q_k$ below are an exact
symbolic clearing of the pinned recurrence, not a guessed operator.

## 3. Complete factor record

Write



$$
Q_k(h)=\kappa_kF_k(h)q_k(h).           \tag{3.1}
$$



The four scalars are



$$
(\kappa_0,\kappa_1,\kappa_2,\kappa_3)
                    =(-4096,-512,-4,27).             \tag{3.2}
$$



The linear-factor products are



$$
\begin{aligned}
F_0={}&(h+1)(h+3)(h+5)(h+6)(2h+1)^2(2h+3)^2(2h+5)^2\\
 &\cdot(2h+7)(2h+9)^2(2h+11)(2h+13)(2h+17)(4h+3),\\
F_1={}&h(h+6)(2h+7)(2h+9)^2(2h+11)(2h+13)(2h+17)\\
 &\cdot(4h+1)(4h+5)(4h+7)(4h+11)(4h+15),\\
F_2={}&h(h+3)(2h+13)(2h+17)(4h+1)(4h+5)(4h+7)(4h+11)\\
 &\cdot(4h+13)(4h+17)(4h+19)(4h+23)(4h+27),\\
F_3={}&h(h+3)(h+6)(h+9)(4h+1)(4h+5)(4h+7)(4h+11)\\
 &\cdot(4h+13)(4h+17)(4h+19)(4h+23)(4h+25)(4h+29)\\
 &\cdot(4h+31)(4h+35)(4h+39).
\end{aligned}                                                \tag{3.3}
$$



The positive-core coefficient lists, low-to-high, are



$$
\begin{array}{c|l}
0&
[6414233265,5112300033,1603835736,247582992,18819760,564080]\\
1&
[402660529612416,1002494068911927,1039962332216826,
596405304955566,209971952382012,47325249956016,
6857541598288,618060903584,31525303040,694946560]\\
2&
[1090010738003273316,2470146696629963712,
2354075629101513405,1243406090403290781,
403775302745693160,84106392952710132,11294493697293648,
946720367971824,45093571774720,932385882560]\\
3&
[214443126,369944721,239554248,72513072,10358560,564080].
\end{array}                                                  \tag{3.4}
$$



Every factor and every core coefficient in (3.3)--(3.4) is positive for
$h\geq1$.  Equations (3.1)--(3.4) prove (1.4), and $Q_3(h)>0$ proves
ordinary rational forward propagation at every admissible index.

There is deliberately no uniform modular forward-unit claim.  The factor
$4h+39$ occurs in $Q_3$, while on the actual subline $s=6$,



$$
p=4h+39.                  \tag{3.5}
$$



Thus $Q_3(h)\equiv0\pmod p$ whenever this subline is a prime row.  It
is genuinely attained: $(h,s,p)=(1,6,43)$ is admissible and prime, and
$43\mid Q_3(1)$.  This exact structural singularity blocks the most
naive attempt to propagate moving-prime nonzeros using (1.3).

The checker expands the four factorizations, runs the Euclidean algorithm
over $\mathbb Q[h]$, and obtains



$$
\gcd_{\mathbb Q[h]}(Q_0,Q_1,Q_2,Q_3)=1,\qquad
 (\operatorname {cont}Q_0,\ldots,\operatorname {cont}Q_3)
 =(4096,512,4,27),\qquad \gcd(4096,512,4,27)=1.      \tag{3.6}
$$



Primitivity of the operator is not a gcd theorem for its values.

## 4. Exact sign theorem

The six initial values are



$$
\begin{array}{c|c}
h&E_h^*\\ \hline
1&-104/21\\
4&-7104750016/761805\\
7&-49133396574985216/2147198787\\
2&13744/231\\
5&169877825152/1380483\\
8&5832403476713133056/18259427025.
\end{array}                                                  \tag{4.1}
$$



Suppose three consecutive terms in one step-three residue subsequence
have the same sign.  Solving (1.3) for the fourth term and using (1.4)
shows that the fourth has that same sign.  The first three values in
$h\equiv1\pmod3$ are negative, and the first three in
$h\equiv2\pmod3$ are positive.  Induction proves (1.5).

This is a characteristic-zero sign theorem only.  A nonzero rational
numerator may still be divisible by its tied moving prime.

## 5. Removing all small-prime content

For a nonzero integer $n$ and $B\geq2$, define



$$
n_{>B}=\frac{|n|}
 {\prod_{\substack{\ell\leq B\\\ell\ {\rm prime}}}
       \ell^{v_\ell(n)}}.                          \tag{5.1}
$$



By (1.5), $N_E(h)\ne0$ for every admissible $h$, so



$$
M_h=N_E(h)_{>4h+3}         \tag{5.2}
$$



is well defined and positive.  Item 243 gives $c_h=\mathcal G_hE_h^*$,
and Item 288 proves



$$
\mathcal G_h\in
 \mathbb Z\left[\frac1\ell:\ell\leq4h+3\text{ prime}\right]^\times.     \tag{5.3}
$$



Therefore, for every prime $q>4h+3$,



$$
v_q(N_E(h))=v_q(\operatorname {num}(c_h)),          \tag{5.4}
$$



and hence



$$
\boxed{M_h=\operatorname {num}(c_h)_{>4h+3}.}       \tag{5.5}
$$



The threshold extraction in (5.1) is nonlinear, so no linear recurrence
for $M_h$ itself is claimed.  Equations (1.3) and (5.5) instead give an
integral localized recurrence and a fixed algebraic coefficient source
for exactly the prime part relevant to actual rows.

## 6. Fixed algebraic generating function and height

Item 237 proves



$$
c_h=[x^{2h}]C(x),           \tag{6.1}
$$



with the rational parametrization



$$
x=\frac{y(1+y)}{(1+y+y^2/2)^{2/3}},\qquad
 C(x(y))=\frac{N(y)}{D(y)^3},                       \tag{6.2}
$$



where



$$
\begin{aligned}
N(y)={}&432+2064y+4440y^2+5376y^3+4044y^4\\
 &+1860y^5+486y^6+48y^7,\\
D(y)={}&6+14y+7y^2+2y^3.
\end{aligned}                                      \tag{6.3}
$$



Equivalently, $C(x)$ satisfies a fixed polynomial equation over
$\mathbb Z[x]$.  Eisenstein's denominator theorem for algebraic power
series gives constants $A\geq1$ and $n_0$ such that



$$
A^n[x^n]C(x)\in\mathbb Z\qquad(n\geq n_0).         \tag{6.4}
$$



The branch in (6.2) is analytic in a fixed disk about zero, so Cauchy's
coefficient estimate gives $|[x^n]C(x)|\leq BR^{-n}$ for fixed
$B,R>0$.  Combining this with (6.4) proves



$$
\log|\operatorname {num}(c_h)|=O(h).      \tag{6.5}
$$



Equations (5.5) and (6.5) prove (1.7).  This improves the earlier crude
factorial clearing, but it remains far above the needed collective
$o(H)$ scale.

## 7. The weighted actual-prime target

For each admissible $h$, let



$$
\mathcal P_h=\left\{p:
\begin{array}{l}
p\text{ prime},\ p=4h+6s+3\text{ for some }s\geq1,\\
p\mid M_h
\end{array}\right\}.                               \tag{7.1}
$$



The desired density input would be



$$
\mathcal W(H)=
 \sum_{\substack{h\leq H\\3\nmid h}}
 \ \sum_{p\in\mathcal P_h}\log p=o(H).              \tag{7.2}
$$



The generic height consequence is only



$$
\mathcal W(H)
 \leq\sum_{\substack{h\leq H\\3\nmid h}}
      \log\operatorname {rad}(M_h)=O(H^2).          \tag{7.3}
$$



The recurrence supplies no automatic improvement: a single congruence
$E_h^*=0\pmod p$ leaves an order-three relation among three other
values, and the forward coefficient is not uniformly a moving-prime
unit by (3.5).  No value-gcd, radical, or zero-density theorem follows
from operator primitivity (3.6).

## 8. Rigorous information-class no-go

Consider the comparison sequence



$$
a_h=4h+9.                  \tag{8.1}
$$



It has the rational generating function and integral recurrence



$$
\sum_{h\geq1}a_hz^h=\frac{z(13-9z)}{(1-z)^2},
 \qquad a_{h+2}-2a_{h+1}+a_h=0,                    \tag{8.2}
$$



and $\log a_h=O(\log h)$, which is stronger than the exponential-height
information available for $M_h$.

Every prime value $a_h$ is an actual row with $s=1$.  Moreover, if
$3\mid h$, then $4h+9>3$ is divisible by $3$; hence every prime
value automatically has the required $3\nmid h$.  Conversely, up to
finitely many initial values, primes $p\equiv1\pmod4$ have
$p=4h+9$ for an integer $h\geq1$.  The prime number theorem in the
progression $1\pmod4$ therefore gives the exact normalization



$$
\begin{aligned}
\sum_{\substack{h\leq H\\4h+9\ {\rm prime}}}\log(4h+9)
 &=\vartheta(4H+9;4,1)+O(1)\\
 &\sim\frac{4H}{\varphi(4)}=2H.                    \tag{8.3}
\end{aligned}
$$



Thus the properties

- fixed algebraic or rational generating function,
- fixed-order integral holonomy,
- integrality or bounded denominators, and
- exponential height

do not, by themselves, imply (7.2).  This proves a no-go only for that
information class.  It says nothing against exploiting the exact
coefficients in (3.3)--(3.4), a sequence-specific congruence, algebraic
monodromy, Cartier information with the prime tied to the index, or a new
auxiliary-local construction.

Fixed-characteristic automaticity or zero-set descriptions also do not
directly supply (7.2): here the characteristic changes with the row and
satisfies $p\asymp h+s$.  This is an applicability distinction, not an
additional impossibility theorem.

## 9. Capacity and strict scope

Item 288 removed $K_h$ as an independent large-moving-prime condition.
Item 293 now isolates the remaining task exactly as the moving-prime zero
set of $M_h$.  It proves an integral recurrence, sign-definiteness in
characteristic zero, an algebraic coefficient description, and a strict
generic-information no-go.  It does not prove (7.2).

Therefore the conditional $j=1$ ceiling is retained:



$$
\boxed{\text{conditional capacity}=1/6\text{ per }m
        =1/36\text{ per }6m.}                      \tag{9.1}
$$



The unconditional booking remains



$$
\boxed{\text{new linear log rate}=0,\quad
        \text{new divisibility exponent}=0,\quad
        \text{capacity booked}=0.}                 \tag{9.2}
$$



Route 1 and every conclusion about $e+\pi$ remain open.

## 10. Reproducibility

From the archive root, run

~~~text
python scripts/item293_j1_E_gate_density_no_go_certificate.py --output results/item293_j1_E_gate_density_no_go_certificate.replay.json
~~~

The checker uses exact standard-library integer, polynomial, and
Fraction arithmetic.  It pins Items 222, 229, 237, 243, and 288;
derives the $Q_k$ by exact cross multiplication from (2.4); verifies
degree, content, polynomial gcd, signs, and the $s=6$ forward
singularity; checks the six sign initials; and performs a bounded replay
of already proved identities through $h\leq8$.  It runs no prime search.

- **PROVED:** (1.3)--(1.5), the large-prime bridge (5.5), the algebraic
  height bound (6.5), and the narrowly scoped information-class no-go.
- **OPEN:** (7.2), every sequence-specific moving-prime density theorem,
  Route 1, and every conclusion about $e+\pi$.
- **NOT CLAIMED:** a recurrence for the nonlinear sequence $M_h$, a
  uniform modular forward unit, or any inference from a prime scan.
