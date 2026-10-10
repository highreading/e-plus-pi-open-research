> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 329 — a fixed-$M$ cubic Cartier carrier for the actually selected fixed-$j=1$ factor

Date: 2026-09-01

## 1. Outcome and capacity first

This item replaces the step-12, two-row viewpoint of Item 326 by a genuinely
single-row theorem.  It retains the exact factor selected by the original
ordinary collision and its actual Item-308 initial data.

On an actual fixed-$M$ row, put



$$
M=3h+4s+2,\qquad p=4h+6s+3,\qquad n=2h=6M-4p.             \tag{1.1}
$$



Define the fixed cubic



$$
P(t)=(1-t)(t^2-2t+2)=2-4t+3t^2-t^3                       \tag{1.2}
$$



and the integer coefficient



$$
K_{M,n}=[t^n]P(t)^{4M}.            \tag{1.3}
$$



Let $c^+_{h,s}=X_s+Y_{s,\epsilon}w_h$ be the exact
Item-308 linear form forced to vanish by an ordinary fixed-$j=1$
collision.  The main theorem is



$$
\boxed{
 c^+_{h,s}\equiv(4M+1)2^{1-4M}K_{M,2h}\pmod p.}          \tag{1.4}
$$



Every factor in front of $K_{M,2h}$ is a $p$-unit.  Therefore



$$
\boxed{
 \text{ordinary fixed-}j=1\text{ collision at }(M,s,p)
 \Longrightarrow p\mid K_{M,6M-4p}.}                    \tag{1.5}
$$



This is a coefficient of one fixed cubic power, not a generic recurrence
state, an unused parity, a norm-only condition, or a collision at a second
row.

The theorem also identifies a second explicit integer carrier $L_{M,p}$
for the opposite factor and proves the exact selected-container union



$$
\boxed{
 p\mid D_{s,\epsilon}
 \quad\Longleftrightarrow\quad
 p\mid K_{M,2h}\ \text{or}\ p\mid L_{M,p}.}              \tag{1.6}
$$



Thus a weighted zero-density theorem for $K$ alone closes the original
fixed-$j=1$ gate, while weighted zero density for both $K$ and $L$
closes the full Item-308 container envelope.

No such density theorem is proved here.  A comparison construction shows
that one shared polynomial carrier, degree $O(M)$, integrality, strict
alternating signs, and even logarithmic $\ell^1$-height $O(M)$ do not
by themselves reduce the raw capacity.  The specific cubic power, its
fixed rational Cartier model, and its arithmetic recurrence remain live.

Consequently



$$
\boxed{\text{new linear log rate}=0,\qquad
        \text{new fixed-}j=1\text{ capacity reduction}=0.}             \tag{1.7}
$$



The fixed-$j=1$ ceiling remains $1/36$ per $6M$.

## 2. Actual-family implication and the two rational factors

Item 308 gives, on every actual row,



$$
c_h^*\equiv X_s+Y_{s,\epsilon}w_h\pmod p,\qquad
 w_h=(-1)^{\lfloor h/2\rfloor}2^h,\qquad \epsilon=h\bmod2,              \tag{2.1}
$$



and



$$
2^{3s+1}w_h^2\equiv\delta_{s,\epsilon}\pmod p.          \tag{2.2}
$$



Set



$$
c^+_{h,s}=X_s+Y_{s,\epsilon}w_h,\qquad
 c^-_{h,s}=X_s-Y_{s,\epsilon}w_h.                         \tag{2.3}
$$



With Item 308's integers $a_s=\Lambda_sX_s$ and
$b_{s,\epsilon}=\Lambda_sY_{s,\epsilon}$, equations (2.2)--(2.3)
give



$$
\boxed{
 D_{s,\epsilon}\equiv
 \Lambda_s^2\,2^{3s+1}c^+_{h,s}c^-_{h,s}\pmod p.}         \tag{2.4}
$$



The scale is a $p$-unit.  Unlike the algebraic factorization used in
Item 321, (2.4) lives directly in $\mathbb F_p$ and the original gate
selects the plus sign in (2.3).  There is no ambiguity about a prime above
$p$.

The pinned bridge from the ordinary collision is



$$
\text{ordinary collision}\Longrightarrow E_h^*=0
 \Longleftrightarrow c_h^*=c^+_{h,s}=0.                   \tag{2.5}
$$



Only this necessary implication is used.

## 3. A first fixed-$M$ polynomial carrier

Retain Item 308's rational source



$$
G_s(t)={N_s(t)\over(1-t)^{2s+6}D(t)^{2s+1}},\qquad
 D(t)=t^2-2t+2,                                           \tag{3.1}
$$



with



$$
c_h^*\equiv2^{2s}[t^{2h}]G_s(t)\pmod p.                 \tag{3.2}
$$



The fixed-$M$ identities are



$$
2s+1=3p-4M,\qquad 2s+6=3p-4M+5,\qquad 2h=6M-4p<p.        \tag{3.3}
$$



Modulo $p$, one has



$$
(1-t)^{3p}=(1-t^p)^3,\qquad D(t)^{3p}=D(t^p)^3.          \tag{3.4}
$$



Because the target degree $2h$ is below $p$, only the constant
coefficient $D(0)^{-3}=2^{-3}$ of the two Frobenius factors can reach it.
Also



$$
s\equiv-{4M+1\over2}\pmod p.                            \tag{3.5}
$$



Define the integer quintic



$$
\begin{aligned}
R_M(t)={}&12-(160M+44)t+(448M+104)t^2-(512M+112)t^3\\
         &\quad +(276M+60)t^4-(60M+12)t^5.
\end{aligned}                                             \tag{3.6}
$$



It is exactly



$$
R_M(t)=3N_{-(4M+1)/2}(t).         \tag{3.7}
$$



Equations (3.1)--(3.7), together with
$2^{2s}=2^{3p-4M-1}\equiv2^{2-4M}\pmod p$, prove



$$
\boxed{
 c_h^*\equiv {C_{M,2h}\over3\,2^{4M+1}}\pmod p,}         \tag{3.8}
$$



where



$$
C_{M,n}=[t^n]R_M(t)(1-t)^{4M-5}D(t)^{4M}\in\mathbb Z.  \tag{3.9}
$$



This is already one fixed polynomial coefficient array for the entire
fixed-$M$ slice.  The next section removes the quintic and the extra
endpoint pole completely.

## 4. Exact Hermite collapse to the pure cubic power

Let $\vartheta=t\,d/dt$ and retain $P=(1-t)D$.  Direct rational
differentiation proves the all-$M$ identity



$$
\boxed{
{R_M(t)\over(1-t)^5}P(t)^{4M}
=
(\vartheta-6M)
\left({2D(t)^2\over(1-t)^4}P(t)^{4M}\right)
+12(4M+1)P(t)^{4M}.}                                     \tag{4.1}
$$



Every term in parentheses becomes an integer polynomial for $M\geq1$:



$$
{2D(t)^2\over(1-t)^4}P(t)^{4M}
 =2(1-t)^{4M-4}D(t)^{4M+2}.                              \tag{4.2}
$$



Taking the coefficient of $t^n$ in (4.1) gives the exact integer
identity



$$
C_{M,n}=(n-6M)S_{M,n}+12(4M+1)K_{M,n},                 \tag{4.3}
$$



where $S_{M,n}$ is the corresponding coefficient of (4.2).  At the
actual index $n=2h=6M-4p$,



$$
C_{M,2h}=-4pS_{M,2h}+12(4M+1)K_{M,2h}.                 \tag{4.4}
$$



Moreover



$$
4M+1=3p-2s.                     \tag{4.5}
$$



Since $0<2s<p$, equation (4.5) proves $p\nmid4M+1$.
Substitution of (4.4) into (3.8) now gives exactly (1.4).

The same coefficient is also the Frobenius digit



$$
\boxed{
 K_{M,2h}\equiv8[t^{2h}]P(t)^{-2s-1}\pmod p,}           \tag{4.6}
$$



because



$$
4M=3p-2s-1                      \tag{4.7}
$$



and only the constant $P(0)^3=8$ of $P(t^p)^3$ reaches a degree
below $p$.  Thus the selected factor is a genuine single-row Cartier
digit of a fixed cubic.

## 5. The opposite factor and the full container envelope

To retain the complete Item-308 envelope, one needs $c^-$ as well as the
factor selected by the original collision.  Put



$$
m=2s+5=3p-4M+4<p.                \tag{5.1}
$$



Define the second integer coefficient



$$
J_{M,m}=[x^m]
 R_M(1+x)(1+x^2)^{4M}(1+x)^{-6M-1}.                      \tag{5.2}
$$



The last factor is interpreted as its integer formal power series.  The
same below-$p$ Frobenius extraction applied directly to Item 308's exact
formula for $A_s$ proves



$$
X_s\equiv-{2^{2-4M}\over3}J_{M,2s+5}\pmod p. \tag{5.3}
$$



Since $c^-=2X_s-c^+$, define



$$
\boxed{
 L_{M,p}=4J_{M,2s+5}+3(4M+1)K_{M,2h}\in\mathbb Z.}       \tag{5.4}
$$



Equations (1.4), (5.3), and (5.4) give



$$
\boxed{
 c^-_{h,s}\equiv-{2^{1-4M}\over3}L_{M,p}\pmod p.}       \tag{5.5}
$$



Combining (2.4), (1.4), and (5.5) proves the exact zero union (1.6).
Accordingly, define



$$
\begin{aligned}
\mathcal W_K(M)
 &=\sum_{\substack{s\in\mathcal S_M\setminus\{2,4,6\}\\
                    p_s\text{ prime},\ p_s\mid K_{M,2h_s}}}\log p_s,\\
\mathcal W_L(M)
 &=\sum_{\substack{s\in\mathcal S_M\setminus\{2,4,6\}\\
                    p_s\text{ prime},\ p_s\mid L_{M,p_s}}}\log p_s.
\end{aligned}                                             \tag{5.6}
$$



Then



$$
\boxed{
 \mathcal W_{\rm off}(M)\leq\mathcal W_K(M),\qquad
 \mathcal W_D(M)\leq\mathcal W_K(M)+\mathcal W_L(M).}    \tag{5.7}
$$



The first inequality is the direct route relevant to the original gate;
the second is a route to the larger sufficient container target.

## 6. A fixed rational Cartier object and an exact coefficient recurrence

The entire $K$-array is generated by one rational function independent
of $M$ and $p$:



$$
\boxed{
 \sum_{M\geq0}\sum_{n\geq0}K_{M,n}z^Mt^n
 ={1\over1-zP(t)^4}.}                                    \tag{6.1}
$$



Let



$$
P^*(u)=u^3P(u^{-1})=2u^3-4u^2+3u-1                     \tag{6.2}
$$



and define the fixed Laurent-rational function



$$
\Phi(z,u)={u^6\over u^6-zP^*(u)^4}.                     \tag{6.3}
$$



Expansion in $z$, followed by coefficient reversal, gives



$$
\boxed{
 K_{M,6M-4p}=[z^Mu^{4p}]\Phi(z,u).}                      \tag{6.4}
$$



If $\Lambda_p^{(u)}$ denotes Cartier extraction in the $u$-exponent,
then equivalently



$$
K_{M,6M-4p}=[z^Mu^4]\Lambda_p^{(u)}\Phi(z,u).           \tag{6.5}
$$



This places the weighted-zero problem inside the Frobenius orbit of one
fixed rational function.  A monodromy, $p$-curvature, or Frobenius
non-concentration theorem for the particular matrix coefficient (6.5)
would be an admissible next attack.

There is also an elementary exact recurrence.  From



$$
P(t){d\over dt}P(t)^{4M}
 =4MP'(t)P(t)^{4M},                                      \tag{6.6}
$$



one obtains, with $K_n=K_{M,n}$,



$$
\boxed{
2(n+1)K_{n+1}
+(16M-4n)K_n
+(3n-3-24M)K_{n-1}
+(-n+2+12M)K_{n-2}=0,}                                   \tag{6.7}
$$



where $K_0=2^{4M}$ and $K_n=0$ for $n<0$.  Equation (6.7) is a
single-row arithmetic recurrence inside the fixed carrier; it is not used
as a bounded-gap collision propagation argument.

The $J$-array is also fixed-rational.  Writing



$$
R_M=R_0+MR_1,\qquad
 Q(x)={(1+x^2)^4\over(1+x)^6},                            \tag{6.8}
$$



one has



$$
\sum_{M\geq0}J_M(x)z^M
={1\over1+x}
\left(
 {R_0(1+x)\over1-zQ(x)}
 +{R_1(1+x)zQ(x)\over(1-zQ(x))^2}
\right),                                                  \tag{6.9}
$$



where $J_M(x)=\sum_mJ_{M,m}x^m$.  Hence both sides of the full container
union (1.6) have fixed rational generating models.

## 7. Capacity audit and the shared-height no-go

The cubic has a particularly clean characteristic-zero size audit:



$$
P(-t)=2+4t+3t^2+t^3.             \tag{7.1}
$$



Therefore every coefficient is nonzero with strict alternating sign,



$$
(-1)^nK_{M,n}>0,                 \tag{7.2}
$$



the degree is exactly $12M$, and



$$
\boxed{
 \sum_{n=0}^{12M}|K_{M,n}|=10^{4M}.}                     \tag{7.3}
$$



Thus every individual coefficient has logarithmic height at most
$4M\log10$.  The tied coefficients $J$ and $L$ also have
$\log\max(1,|J|,|L|)=O(M)$, by their finite coefficient formulas.
Multiplying these bounds over $O(M)$ rows gives only $O(M^2)$, so
direct absolute height remains inadmissible.

The limitation persists even after adding the fact that all rows are
coefficients of one shared polynomial.  Let $\mathcal P_M$ be the actual
candidate primes, and assign



$$
a_{M,j}=
 \begin{cases}
 p,&j=6M-4p\text{ for }p\in\mathcal P_M,\\
 1,&\text{otherwise}.
 \end{cases}                                              \tag{7.4}
$$



Define



$$
\widetilde K_M(t)=\sum_{j=0}^{12M}(-1)^ja_{M,j}t^j.     \tag{7.5}
$$



The indices in (7.4) are distinct.  The comparison polynomial is primitive,
has exact degree $12M$, has the same strict alternating nonzero sign
pattern, and satisfies



$$
\log\|\widetilde K_M\|_1=O(\log M).           \tag{7.6}
$$



Nevertheless every candidate prime divides its tied coefficient, so its
retained weighted mass is



$$
{M\over6}+o(M),                  \tag{7.7}
$$



the full raw $1/36$-per-$6M$ ceiling.

This proves the scoped information-class no-go



$$
\boxed{
\begin{gathered}
\text{one shared integer carrier of degree }O(M),\text{ integrality,}\\
\text{strict alternating signs, and }\log\ell^1=O(M)\\
\text{alone imply no strict fixed-}j=1\text{ capacity reduction.}
\end{gathered}}                                           \tag{7.8}
$$



The comparison family is not a power of the actual cubic and does not
share (6.1), (6.5), or (6.7).  Those sequence-specific structures are
precisely what remains admissible.

## 8. Exact replay controls and strict scope

The certificate replays five rows already preselected in Item 308.  Two
are especially useful for separating the selected target from its envelope:



$$
\begin{array}{c|cc|cc|c}
(M,h,s,p)&c^+&c^-&K&L&D\pmod p\\ \hline
(34,8,2,47)&0&30&0&24&0\\
(30,4,4,43)&16&0&2&0&0.
\end{array}                                                \tag{8.1}
$$



The first row is a zero of the factor selected by the original eliminant;
the second is a zero only of the opposite factor.  This exactly checks the
union (1.6) and shows why $\mathcal W_D$ is a larger envelope than the
actual selected target.

Equation (8.1) is **EXACT FINITE ONLY**.  Neither row is promoted to a new
full Item-264 collision claim, and no finite zero census or prime scan is
used asymptotically.

## 9. Capacity, strict labels, and the next theorem

The strategically smallest live theorem is now



$$
\boxed{
 \mathcal W_K(M)=
 \sum_{\substack{s\in\mathcal S_M\setminus\{2,4,6\}\\
                  p_s\text{ prime},\\
                  p_s\mid[t^{2h_s}]P(t)^{4M}}}
 \log p_s=o(M).}                                          \tag{9.1}
$$



It is a weighted zero-density problem for one fixed cubic Cartier object.
Proving (9.1) closes the original fixed-$j=1$ gate.  To close the larger
container envelope, prove the analogous theorem for $L$ as well.

- **PROVED:** the fixed-$M$ Frobenius carrier (3.8); the exact Hermite
  identity (4.1); the pure cubic selected-factor formula (1.4); the
  Frobenius digit (4.6); the dual carrier (5.4)--(5.5); the exact container
  zero union (1.6); the fixed rational Cartier readout (6.5); the exact
  coefficient recurrence (6.7); and the scoped shared-height no-go (7.8).

- **SCOPED SHARED-CARRIER/HEIGHT NO-GO:** degree, integrality, sign pattern,
  a common carrier, and absolute or $\ell^1$ height alone cannot reduce
  the raw capacity.  The specific cubic, Cartier action, and recurrence are
  not closed.

- **EXACT FINITE ONLY:** the five declared Item-308 replay rows.  No scan or
  finite census is promoted.

- **OPEN:** (9.1); weighted zero density for $L$;
  $\mathcal W_{\rm off}(M)=o(M)$; $\mathcal W_D(M)=o(M)$;
  fixed-$j=1$ closure; Route 1; and every conclusion about $e+\pi$.

- **NOT CLAIMED:** universal nonvanishing; a Frobenius monodromy theorem;
  that the comparison polynomial resembles the actual cubic power; that a
  declared control is a new full collision; a prime scan; positive capacity;
  or any ledger improvement.

The ledger remains



$$
\boxed{\text{capacity booked}=0,\qquad
        \text{fixed-}j=1\text{ ceiling}={1\over36}
        \text{ per }6M.}                                  \tag{9.2}
$$



No canonical, master, or status file is edited by this research package.

## 10. Deterministic replay

From the archive root, run

~~~text
python work/item329_j1_fixedM_cubic_cartier_certificate.py --output work/item329_j1_fixedM_cubic_cartier_certificate.replay.json
~~~

The checker pins canonical Items 308 and 326.  It verifies every fixed-$M$
index identity, reconstructs $R_M$, proves the Hermite identity in
$\mathbb Q(M,t)$, derives the cubic coefficient recurrence, checks the
integer coefficient identity before reduction modulo $p$, reconstructs
the plus and minus Item-308 factors and both carriers on all five declared
rows, and verifies the exact zero union.  It performs no prime scan.
