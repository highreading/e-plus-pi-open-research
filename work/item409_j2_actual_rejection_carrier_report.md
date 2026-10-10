> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 409 — actual formulas and the moving-row obstruction for the ordinary-$j=2$ rejection carrier

Checked: 2026-09-01 (Beijing time)

## 1. Capacity first and verdict

Retain one ordinary-$j=2$ ray



$$
p=2r+6s+3,\qquad r=6M-7p,\qquad
 s=\frac{5p-4M-1}{2},\qquad
 r\equiv e\pmod 6,\quad e\in\{1,5\}.
\tag{1.1}
$$



Its raw Chebyshev mass is



$$
R_e(M)=\frac1{35}M+o(M),
\tag{1.2}
$$



so its normalized capacity is $1/210$. The two rays share the
ordinary-$j=2$ ceiling $1/105$.

Items 349, 404, and 407 define



$$
\Pi_r=\gcd\bigl(
 |\operatorname{num}\mathfrak a_r|,
 |\operatorname{num}\mathfrak b_r|,
 |\operatorname{num}K_r|
 \bigr),
\tag{1.3}
$$





$$
\Gamma_{r,s}=\gcd\bigl(
 \Pi_r,|\operatorname{num}T_0|,|\operatorname{num}T_1|
 \bigr),
\tag{1.4}
$$



and, after Item 338's tied-prime-safe saturation,



$$
\boxed{
 \mathcal J_{r,s}
 =\bigl(\Pi^{\rm sat}_{r,s}\bigr)_{(\Gamma^{\rm sat}_{r,s})}.}
\tag{1.5}
$$



The present item goes inside these integers. It reconstructs the actual
algebraic coefficient sequences, the canonical $K_r$-chain, the global
Cartier diagonal, and the actual incomplete period. The outcome is a
formula-specific obstruction, not a positive-density theorem.

> **PROVED — actual tied-support normal form.** On every actual row,
>
> 

$$
> \boxed{
> p\mid\mathcal J_{r,s}
> \Longleftrightarrow
> p\mid\operatorname{num}\mathfrak a_r,\
> p\mid\operatorname{num}\mathfrak b_r,\
> p\mid\operatorname{num}K_r,\
> (T_0,T_1)\not\equiv(0,0)\pmod p.}
> \tag{1.6}
>
$$


>
> Every denominator displayed below is a $p$-unit. Thus (1.6) is an
> exact statement about the actual sequences, not an ambient rank-one
> packet.

> **PROVED — actual target branch split.** The Cartier residual has the
> tied-prime replacement
>
> 

$$
> T_\nu\equiv(-1)^{m+1}
> \bigl(f_\nu Z_{r,s}+9\,4^s b_\nu-11v_\nu\bigr)\pmod p,
> \tag{1.7}
>
$$


>
> where $m=s-1$ and $Z_{r,s}$ is the actual incomplete period. On
> $p\mid\Pi_r$, if $f\ne0$, one scalar residual containing that
> incomplete period survives. If $f=0$, the period disappears and the
> surviving test is $9\,4^s b-11v=0$.

> **PROVED — two proposed all-row good-reduction identities are false.**
> On the actual prime row
>
> 

$$
> (p,r,s,M)=(709,347,2,885),
> \tag{1.8}
>
$$


>
> exact reconstruction gives
>
> 

$$
> \boxed{
> \Pi_r=\Pi^{\rm sat}_{r,s}=79,\qquad
> \Gamma_{r,s}=\Gamma^{\rm sat}_{r,s}=1,\qquad
> \mathcal J_{r,s}=79.}
> \tag{1.9}
>
$$


>
> Thus neither $\Pi^{\rm sat}\equiv1$ nor
> $\mathcal J\equiv1$ is an all-row integer identity. The factor $79$
> is foreign to the tied characteristic $709$, so (1.9) does **not**
> refute the still-open tied-prime statement
> $p\nmid\Pi^{\rm sat}_{r,s}$, and it gives no density information.

> **PROVED — scoped actual-sequence resultant/recurrence no-go.**
> The two algebraic minor sequences $\mathfrak a_r,\mathfrak b_r$
> share the known order-three ray operator. The actual $K_r$-chain
> fails that operator in each of five natural gauges, by exact nonzero
> first-window residuals on both rays. The actual period sequence has an
> order-two recurrence, but a unit shift in its index changes the tied
> characteristic from $p$ to $p+6$. Finally, safely matched
> $\mathcal J$-row factors are high-prime atoms with pairwise gcd one.
> Therefore the known common operator, same-characteristic bounded
> propagation, and common-divisor resultants of matched factors supply no
> positive lower bound for $\mathcal J$-support.

This does not rule out a new unmatched resultant, a different common
module containing $K_r$, or a cross-characteristic reciprocity law.
No weighted lower bound is proved. Hence



$$
\boxed{\eta_{\rm proved}=0},\qquad
 \boxed{\Delta\mathcal C=0},\qquad
 \boxed{\text{ordinary-}j=2\text{ ceiling remains }1/105}.
\tag{1.10}
$$



There is no prime census and no extrapolation from the declared rows.

## 2. The actual $r$-sequences inside $\Pi_r$

The first two normalized minors are coefficients of the algebraic
branches retained by Items 314, 315, and 349. Put



$$
E_-(z)=2z^3+z^2+6z-3,\qquad
 E_+(y)=2y^3+7y^2+14y+6,
\tag{2.1}
$$





$$
\begin{aligned}
P_-(z)&=16z^6+55z^5-199z^4+278z^3-42z^2-33z+45,\\
P_+(y)&=16y^6+151y^5+316y^4+352y^3
       +388y^2+292y+120,
\end{aligned}
\tag{2.2}
$$



and $Q(y)=1+y+y^2/2$. Lagrange inversion gives



$$
\boxed{
\begin{aligned}
\mathfrak a_r={-12\over r}[z^{r-1}]\;&
 { (z+1)(z^2+1)P_-(z)\over E_-(z)^4}
 { (1+z^2)^{2r/3}\over(1-z)^r},\\
\mathfrak b_r={-12\over r}[y^{r-1}]\;&
 { (y+2)(y^2+2y+2)P_+(y)\over E_+(y)^4}
 { Q(y)^{2r/3}\over(1+y)^r}.
\end{aligned}}
\tag{2.3}
$$



Thus both are algebraic-coefficient, D-finite sequences. On each ray
$r=6n+e$, they satisfy the same exact order-three step-$6$ operator:



$$
\sum_{j=0}^3p_j(r/2)\mathfrak b_{r+6j}=0,\qquad
 \sum_{j=0}^3p_j(r/2)16^{-j}\mathfrak a_{r+6j}=0.
\tag{2.4}
$$



The third sequence is the canonical inhomogeneous determinant from Item
349. With



$$
\bar q=-{2r+3\over3},\qquad
 P_0(z)=(1-z)^r(1+z),\qquad
 P_1(z)=(1-z)^r(1+z)^4,
\tag{2.5}
$$



define



$$
\eta_{2t}=0,\qquad \eta_1=1,\qquad
 \eta_{k+2}=-{\bar q+k\over3\bar q+k}\eta_k
 \quad(k\text{ odd}),
\tag{2.6}
$$



and



$$
(\bar q+k)y_k+(3\bar q+k)y_{k+2}=1,\qquad
 y_0=0,\qquad y_{2r+3}=0.
\tag{2.7}
$$



If $P_{\nu,j}=[z^j]P_\nu(z)$, put



$$
\begin{aligned}
S_0&=\sum_jP_{0,j}(y_{j+1}+y_{j+3}),&
S_1&=\sum_jP_{1,j}y_j,\\
\Delta_0&=\sum_jP_{0,j}(\eta_{j+1}+\eta_{j+3}),&
\Delta_1&=\sum_jP_{1,j}\eta_j,
\end{aligned}
\tag{2.8}
$$



so that



$$
\boxed{K_r=S_0\Delta_1-S_1\Delta_0.}
\tag{2.9}
$$



Equations (2.6)–(2.9) are terminating hypergeometric/rational chains,
not a black-box carrier. They give the established height and holonomy
candidates for $K_r$, but they do not put $K_r$ in the known module
(2.4).

The certificate reconstructs the five exact nonzero residuals used in
the operator-reuse test: the old connection operator on $C_r$, on
$16^nC_r$, the Item-315 operator on $C_r/\sigma_r$, its
$16^{-n}$-scaled version, and the Item-315 operator directly on
$K_r$. A single exact failure disproves an all-$r$ operator identity.
The failures on both rays therefore close these five Casoratian
constructions. They do not exclude a different higher-order recurrence.

## 3. The actual two-parameter target

Let $m=s-1$, $d=r+4$, and



$$
n=3m+d,\qquad q=2m+d,\qquad p=6m+2d+1.
\tag{3.1}
$$



The global Cartier digit in Item 334 is



$$
c_{m,d}=[x^{6m+2d+1}]
 (1-x)^{3m+d}(1+x)^{5m+2d}.
\tag{3.2}
$$



It has the exact bivariate rational constant-term generating function



$$
\boxed{
 \sum_{m,d\ge0}c_{m,d}t^mu^d
 =\operatorname{CT}_x
 {x^{-1}\over
 \left(1-t{(1-x)^3(1+x)^5\over x^6}\right)
 \left(1-u{(1-x)(1+x)^2\over x^2}\right)}.}
\tag{3.3}
$$



Indeed the coefficient of $t^mu^d$ on the right is (3.2) after
multiplication by $x^{-(6m+2d+1)}$. Thus the raw Cartier digit is a
rational diagonal and is holonomic. This is stronger structural
information than a pointwise height estimate, but it is still not a
modular anti-gcd theorem.

Write



$$
h_m={1\over8^m}\binom{2m}{m},\qquad
 \Phi_{r,s}=c_{m,d}+\epsilon_ph_mP_{r+2}(m).
\tag{3.4}
$$



The exact Item-334 residuals are



$$
\boxed{
\begin{aligned}
T_\nu={}&{9\kappa_r\over2}f_\nu B_s\Phi_{r,s}\\
&+(-1)^m\bigl(f_\nu B_s\tau_{r,s}
               -9\,4^sb_\nu+11v_\nu\bigr),
\qquad \nu=0,1.
\end{aligned}}
\tag{3.5}
$$



Here



$$
B_s={(2s-1)!(s-1)!\over(3s-1)!},\qquad
 \tau_{r,s}=(-1)^{s+(r-1)/2}{2\over3}
 { (s)_{(r+1)/2}\over(3s+1)_{(r+1)/2}}.
\tag{3.6}
$$



Equations (2.3), (2.6)–(2.9), and (3.2)–(3.6) are a complete actual
formula for $\Pi_r,\Gamma_{r,s}$, and $\mathcal J_{r,s}$. The only
nonalgebraic operations in the three integer carriers are primitive
numerator extraction, gcd, and support saturation.

For tied-prime analysis, Item 251 supplies the more transparent actual
period. Put



$$
A_s=\sum_{j=0}^{2s-1}
 \binom{3s-1}{s+j}\binom{s+j-1}{j}\in\mathbb Z.
\tag{3.7}
$$



Then



$$
\boxed{Z_{r,s}=B_s\left({9\kappa_r\over2}A_s-\tau_{r,s}\right).}
\tag{3.8}
$$



If $w=t(2+w)^3$, its generating function is



$$
\sum_{s\ge1}A_st^{s-1}
 ={(2+w)^3\over2(1-w^2)}-{1\over1+t}.
\tag{3.9}
$$



With $A_1=3,A_2=49$, it satisfies



$$
\begin{aligned}
&(s+1)(2s+3)(28s+11)A_{s+2}\\
&\quad-(1456s^3+3456s^2+2303s+435)A_{s+1}\\
&\quad-6(3s+1)(3s+2)(28s+39)A_s=0.
\end{aligned}
\tag{3.10}
$$



Item 334's Cartier substitution gives (1.7). This is only a tied-$p$
support replacement: the integers defined by the two sides can have
different foreign-prime factors. Item 409 does not identify their full
foreign support.

## 4. The two actual degenerate target problems

Suppose $p\mid\Pi_r$. Then all three connection minors vanish modulo
$p$.

### 4.1 $f\ne0\pmod p$

Both $b$ and $v$ lie on the line spanned by $f$. Choose
$\nu$ with $f_\nu\ne0$. The two residuals in (1.7) are proportional,
and target rejection is exactly



$$
f_\nu Z_{r,s}+9\,4^sb_\nu-11v_\nu\ne0\pmod p.
\tag{4.1}
$$



Thus this branch is a genuine incomplete-period nonvanishing problem for
the algebraic sequence $A_s$, against moving $r$-dependent
coefficients. Triple-minor vanishing does not remove it.

### 4.2 $f=0\pmod p$

The period term is zero and the exact target rejection is



$$
\boxed{9\,4^sb-11v\ne(0,0)\pmod p.}
\tag{4.2}
$$



The gate still includes $K_r=0\pmod p$, while the target is now an
exponential proportionality problem. It is not legitimate to impose
the incomplete-period condition from the other branch.

Equations (4.1)–(4.2) are the actual formula-specific content absent
from the abstract support packets in Items 404 and 407.

## 5. Why the available recurrences do not give a moving-row resultant

There are three separate obstructions.

### 5.1 The known gate operator does not contain $K_r$

The recurrence (2.4) controls the first two normalized minors. The exact
counterexamples described after (2.9) prove that it does not control the
third in any of the five natural gauges. Hence no proved Abel identity or
Casoratian from that operator bounds



$$
\gcd(\operatorname{num}\mathfrak a_r,
      \operatorname{num}\mathfrak b_r,
      \operatorname{num}K_r).
\tag{5.1}
$$



This closes those five resultants, not every possible recurrence for
$K_r$.

### 5.2 The target recurrence changes characteristic

At fixed $r$, the shift $s\mapsto s+1$ in (3.10) changes



$$
p=2r+6s+3\quad\longmapsto\quad p+6.
\tag{5.2}
$$



Reducing an integer recurrence modulo $p$ relates neighboring values
inside $\mathbf F_p$. The selected test at the neighboring row lies in
$\mathbf F_{p+6}$. There is no unital field homomorphism between
fields of different characteristic. Consequently (3.10), including a
unit leading coefficient when one is available, is not a
cross-characteristic propagation theorem.

The fixed-$M$ geometry makes the mismatch sharper. A same-ray shift
$r\mapsto r+6j$ returns to the fixed-$M$ lattice only when
$7\mid j$. The first return is



$$
(r,s,p)\longmapsto(r+42,s-15,p-6).
\tag{5.3}
$$



The order-three window $r,r+6,r+12,r+18$ therefore contains no second
fixed-$M$ row. At the first possible return the selected modulus has
again changed.

### 5.3 Matched rejection factors are already atomic

Let



$$
L_M=\left\lceil{4M+3\over5}\right\rceil,\qquad
 U_M=\left\lfloor{6M-1\over7}\right\rfloor.
\tag{5.4}
$$



For every integer row $q\in[L_M,U_M]$, define



$$
j_{M,q}^{\sharp}
 =\left(
 \operatorname{rad}\gcd\left(
 q,\mathcal J_{6M-7q,(5q-4M-1)/2}
 \right)
 \right)_{((L_M-1)!)}.
\tag{5.5}
$$



Since $U_M<2L_M$, a prime $\lambda\ge L_M$ dividing such a $q$
forces $q=\lambda$. Therefore



$$
\boxed{
 j_{M,q}^{\sharp}=
 \begin{cases}
 q,&q\text{ is prime and its actual row is degenerate-target-rejected},\\
 1,&\text{otherwise},
 \end{cases}}
\tag{5.6}
$$



and, for $q\ne q'$,



$$
\boxed{\gcd(j_{M,q}^{\sharp},j_{M,q'}^{\sharp})=1.}
\tag{5.7}
$$



Thus a pairwise gcd, lcm correction, or common-divisor resultant formed
only from the matched factors has no high-prime overlap to exploit. An
unmatched resultant involving full values at other rows is not excluded,
but it needs a new theorem forcing its foreign divisor back to the
selected row.

## 6. Good reduction: the direction of the implication matters

The exact witness (1.8)–(1.9) rules out the strongest proposed integer
identity. Three weaker statements must be distinguished.

1. A **tied gate good-reduction theorem**
   $p\nmid\Pi^{\rm sat}_{r,s}$ would make the degenerate chart empty.
   It would also make the $\mathcal J$-mass zero. By itself it books
   zero, because the nondegenerate chart could occupy the whole ray.
2. A **relative target good-reduction theorem**
   $\Gamma^{\rm sat}_{r,s}=1$ would make every degenerate gate row a
   target rejection, but it still needs a positive lower bound for the
   degenerate gate mass.
3. A theorem that all prime factors of $\Pi^{\rm sat}$ are smaller than
   the tied $p$ would imply the first statement, not the second. It is
   a chart-closing input, not directly a positive
   $\mathcal J$-support theorem.

No one of these actual all-row theorems is proved here. Pointwise height
does not decide any of them: it is an upper bound on available factors,
whereas positive rejection density is a lower-support statement.

## 7. Exact coupling to the nondegenerate chart

Let



$$
J_e(M)=\sum_{\substack{p\text{ on the }e\text{-ray}\\
                         p\mid\mathcal J_{r,s}}}\log p,
\tag{7.1}
$$



and retain Item 407's notation $G_e(M)$ for degenerate collisions and
$N_e(M)$ for nondegenerate selected-prime collisions. If actual
theorems give



$$
J_e(M)\ge jM+o(M),\qquad
 G_e(M)\le gM+o(M),\qquad
 N_e(M)\le nM+o(M),
\tag{7.2}
$$



then two independent exclusions are available:



$$
R_e-(G_e+N_e)\ge J_e,\qquad
 R_e-(G_e+N_e)\ge
 \left({1\over35}-g-n\right)M+o(M).
\tag{7.3}
$$



Hence



$$
\boxed{
 \Delta\mathcal C_e\ge
 {1\over6}\max\left\{0,j,{1\over35}-g-n\right\}.}
\tag{7.4}
$$



If only a gate lower bound $D_e\ge dM+o(M)$ and collision upper bound
$G_e\le gM+o(M)$ are known, then $j=d-g$, and (7.4) is precisely
Item 407's



$$
{1\over6}\max\left\{0,d-g,{1\over35}-g-n\right\}.
\tag{7.5}
$$



No positive $j$, useful $g+n<1/35$, or $d>g$ is proved. The
numerical ledger therefore stays unchanged.

## 8. Sharply scoped global no-go and the smallest missing lemma

Define the Item-409 method class to use only:

1. the actual formulae (2.3), (2.6)–(2.9), and (3.2)–(3.10);
2. the known common operator (2.4) and actual period recurrence (3.10);
3. fixed bounded same-characteristic propagation;
4. primitive clearing and tied-prime-safe saturation;
5. common-divisor resultants among matched row factors; and
6. pointwise height only as an upper bound, never as a density input.

> **PROVED — scoped screening theorem.** Inside this class, every
> proposed positive-margin mechanism fails at a certified step:
> $K_r$ is not in the known operator in any of the five tested gauges;
> the target recurrence changes the selected characteristic; matched
> high-prime factors have zero overlap; and height has the wrong
> inequality direction for a support lower bound. Thus this class
> supplies no $j>0$ in (7.4).

This theorem does not say that the actual sequences realize an ambient
countermodel. No ambient packet is used or claimed actual. It also does
not rule out a different common recurrence, an unmatched moving-row
resultant, cross-characteristic reciprocity, or a direct anti-gcd theorem.

The smallest missing statement is one formula-specific lemma.

> **OPEN — actual tied large-prime Smith anti-gcd lemma.** Prove that for
> one $e\in\{1,5\}$ and some fixed $\delta>0$,
>
> 

$$
> \boxed{
> \sum_{\substack{p\text{ on the fixed-}M\ e\text{-ray}\\
> p\mid\operatorname{num}\mathfrak a_r,\
> p\mid\operatorname{num}\mathfrak b_r,\
> p\mid\operatorname{num}K_r\\
> (T_0,T_1)\not\equiv(0,0)\ (p)}}
> \log p
> \ge\delta M+o(M).}
> \tag{8.1}
>
$$



Because every relevant denominator is a $p$-unit, (8.1) is exactly
$J_e(M)\ge\delta M+o(M)$. It would save $\delta/6$, or combine with
nondegenerate information through (7.4). Unlike a pointwise height
bound, it has the needed direction and is already stated on the selected
fixed-$M$ diagonal.

## 9. Deterministic certificate, replay, and strict claim labels

The certificate pins every canonical dependency named in Section 1 and
the audited work Item 407 package.  It then performs exact rational
reconstruction of the actual rows, saturation and support subtraction,
the target/period congruence checks, the Cartier constant-term identity,
the actual-period recurrence, the five inherited operator-obstruction
witnesses, fixed-$M$ interval atomicity, and the exact chart-coupling
formula (7.4).  Its declared Item-409 witness is
$(p,r,s,\Pi^{\rm sat},\Gamma^{\rm sat},J)=(709,347,2,79,1,79)$.

From the repository root, the deterministic replay command is:

~~~powershell
python work/item409_j2_actual_rejection_carrier_certificate.py --replay work/item409_j2_actual_rejection_carrier_certificate.json --output work/item409_j2_actual_rejection_carrier_certificate_replay.json
~~~

The replay is required to be byte-identical to the committed certificate;
the package hash file records both outputs separately.

### Strict labels

- **PROVED:** the displayed actual formulae and recurrences; the target
  congruence; the fixed-$M$ return geometry; matched-prime atomicity;
  the exact witness $J_{709,347,2}=79$; and the conditional chart
  coupling (7.4).
- **PROVED, SCOPED NO-GO:** the method class of Section 8 cannot produce
  a positive $J$-support margin from the pinned inputs.
- **CERTIFIED FINITE WITNESS, NOT A CENSUS:** the five exact reconstructed
  rows in the certificate, especially the foreign factor $79$.
- **OPEN:** the tied large-prime Smith anti-gcd lemma (8.1), or an
  equivalent formula-specific unmatched moving-row resultant theorem.
- **NOT CLAIMED:** a positive density for degenerate rejection; a
  prime-census extrapolation; a pointwise-height-to-density implication;
  realization of any ambient packet by the actual sequences; or a
  numerical improvement to the Route-1 exponent.

Accordingly this package is a rigorous structural advance with a
formula-specific obstruction and smallest missing lemma, but its booked
numerical saving is exactly zero.
