> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 177 — actual constrained $B_0$ on the first two fixed bands

Date: 2026-08-29

## 1. Scope and verdict

This item goes beyond Item 175's ambient functional noncollapse.  It
specializes the actual Item 172 primitive to the two smallest
parity-compatible slices



$$
(j,s)=(1,1),\qquad(2,0),          \tag{1.1}
$$



and evaluates the resulting $B_0$ digit for every admissible prime.

The conclusions are exact.

**PROVED — actual constrained nonvanishing on $j=1,s=1$.**  Here
$m=p-1$.  For every prime $p\ge7$,



$$
\boxed{
 B_0\equiv
 \begin{cases}
  2735/4,&p\equiv1\pmod4,\\
 -5295/4,&p\equiv3\pmod4,
 \end{cases}
 \pmod p,}                                               \tag{1.2}
$$



and neither value can vanish in its indicated prime class.  Thus



$$
\boxed{B_0\ne0\quad(p\ge7).}     \tag{1.3}
$$



This is a theorem on the actual constrained $\bar T$-locus, not merely
on the ambient five-value space.

**PROVED — complete actual classification on $j=2,s=0$.**  Here
$m=(3p-1)/2$.  For every prime $p\ge7$,



$$
\boxed{
 B_0\equiv
 \begin{cases}
 -918897/128,&p\equiv1\pmod4,\\
   59829/128,&p\equiv3\pmod4,
 \end{cases}
 \pmod p.}                                               \tag{1.4}
$$



The only zeros are



$$
\boxed{p=7,11.}                  \tag{1.5}
$$



In particular $B_0\ne0$ for every prime $p\ge13$ on this slice.

**PROVED — circular-sign erratum.**  Under the archive convention
$E=-4\operatorname {Im}\operatorname {Res}_i$, the five-divisor formula
for $B_0$ carries an overall factor



$$
\chi_4(p)=(-1)^{(p-1)/2}.             \tag{1.6}
$$



The prior version of Item 172 equation (4.11), and the inherited display
in Item 175, suppressed this sign; the correction is now integrated into
both reports.  It changes no zero condition, finite count, survivor list,
or stored Hasse digit.  It only negates the old displayed contraction when
$p\equiv3\pmod4$.  Section 7 records the exact scope.

**NO POSITIVE-MASS CLAIM.**  The slices (1.1) are fixed rays in the
$(m,p)$-plane.  Although they contain every prime above the stated
thresholds as the parameter $p$ varies, they do not give positive
log-prime mass for a fixed $m$.  They yield no improved Route-1 content
constant and no conclusion about $e+\pi$.

## 2. The two actual cell slices

On the $\kappa=1$ cell, Item 172 gives



$$
2m+1=(j+1)p-s,\qquad
 0\le s\le{p-3\over3},\qquad s\equiv j\pmod2.           \tag{2.1}
$$



For $j=1$, the smallest compatible value is $s=1$, and (2.1) gives



$$
m=p-1.                          \tag{2.2}
$$



For $j=2$, the smallest compatible value is $s=0$, and



$$
m={3p-1\over2}.                 \tag{2.3}
$$



Every prime $p\ge7$ satisfies all cell inequalities in both cases,
including



$$
p\le4m+1<p^2.                   \tag{2.4}
$$



Thus these are genuine $e=1$ rows of the original mixed-cubic problem,
not formal parameter specializations.

Put



$$
P_0=u^{p-3s-3}Q^{2s+1},\qquad
 P_1=u^{p-3s-3}Q^{2s},                                  \tag{2.5}
$$



and retain the repaired exact convention



$$
\widetilde\gamma_\nu=[x^{p-1}]P_\nu\in\mathbb Z,
 \qquad
 \bar\gamma_\nu=\widetilde\gamma_\nu\pmod p.          \tag{2.6}
$$



The exact primitive is formed before reduction.  All calculations below
start from that convention.

## 3. Closed characteristic-$p$ primitives

### 3.1 The slice $j=2,s=0$

The exact coefficients are



$$
\widetilde\gamma_0={(p-4)(p-5)\over2},\qquad
 \widetilde\gamma_1={(p-3)(p-4)\over2},                 \tag{3.1}
$$



so



$$
(\bar\gamma_0,\bar\gamma_1)=(10,6). \tag{3.2}
$$



Hence the reduced determinant polynomial is



$$
\bar\Theta=u^{p-3}(6Q-10).                             \tag{3.3}
$$



Set



$$
B_2(x)=2+2x+3x^2.               \tag{3.4}
$$



The exact rational identity



$$
uB_2'-2u'B_2=6Q-10                         \tag{3.5}
$$



gives the convenient characteristic-$p$ primitive representative



$$
\widehat T_2=u^{p-2}B_2.        \tag{3.6}
$$



Indeed $\widehat T_2'=\bar\Theta$ in characteristic $p$.

### 3.2 The slice $j=1,s=1$

The four-section formulas reduce to



$$
\begin{aligned}
 \widetilde\gamma_0
   &=-\binom{p-9}{5}+3(p-9)\equiv1260\pmod p,\\
 \widetilde\gamma_1
   &=-\binom{p-8}{5}+2(p-8)\equiv 776\pmod p.
\end{aligned}                                           \tag{3.7}
$$



Thus



$$
\bar\Theta=u^{p-6}Q^2(776Q-1260).                     \tag{3.8}
$$



Put



$$
\begin{aligned}
 B_1(x)={}&{484\over5}+290x+578x^2+952x^3+1132x^4\\
          &+1106x^5+970x^6+388x^7+388x^8.
\end{aligned}                                           \tag{3.9}
$$



Direct multiplication proves



$$
uB_1'-5u'B_1=Q^2(776Q-1260).            \tag{3.10}
$$



Since $p\ge7$, the denominator $5$ is a unit, and



$$
\widehat T_1=u^{p-5}B_1         \tag{3.11}
$$



satisfies $\widehat T_1'=\bar\Theta$.

### 3.3 Why the hat is harmless but necessary

The literal reduction $\bar T$ of Item 172's exact-integer primitive has
zero $x^p$ coefficient.  A characteristic-$p$ primitive is only unique
up to a polynomial in $x^p$.  In fact,



$$
\bar T=\widehat T-c_jx^p,\qquad
 c_1={368864\over5},\qquad c_2=13.                       \tag{3.12}
$$



This distinction is not optional: (3.6) and (3.11) generally do contain an
$x^p$ term.  Nevertheless the determinant wedges may use either
representative.  Indeed



$$
\mathcal C\left(x^p{dF_j\over F_j}\right)
 =x{dF_j\over F_j},                                     \tag{3.13}
$$



and after multiplying by $F_j$,



$$
xF_j'\,dx=d(xF_j)-F_jdx.                              \tag{3.14}
$$



The boundary of $xF_j$ vanishes at $0,1$.  Therefore (3.14) changes
the Cartier output only by a scalar multiple of $v_j$, which disappears
from both wedges.  The certificate also checks directly that



$$
\sum_a n_a\tau_p(a^p)w^B_{j,a}=0                      \tag{3.15}
$$



for $j=1,2$.  Thus using $\widehat T_j$ is exact for the $B_0$ digit,
while (3.12) preserves the exact-$\widetilde\gamma$ convention.

## 4. Actual constrained values

The zero and one evaluations of $\widehat T_j$ vanish.  At the three pole
divisors, Fermat and Gaussian Frobenius give the following exact values.

For $j=1,s=1$,



$$
\widehat T_1(-1)={134\over5},                          \tag{4.1}
$$



and



$$
\widehat T_1(i)=
 \begin{cases}
 -86/5-14i,&p\equiv1\pmod4,\\
 -14+(86/5)i,&p\equiv3\pmod4.
 \end{cases}                                           \tag{4.2}
$$



The value at $-i$ is the conjugate.  For $j=2,s=0$,



$$
\widehat T_2(-1)=-{3\over2},                          \tag{4.3}
$$



and



$$
\widehat T_2(i)=
 \begin{cases}
 (1+3i)/2,&p\equiv1\pmod4,\\
 (3-i)/2,&p\equiv3\pmod4.
 \end{cases}                                           \tag{4.4}
$$



Inverse Frobenius $\tau_p$ is the identity in the first residue class and
Gaussian conjugation in the second.

The exact Item 175 circular weights needed here are



$$
\begin{array}{c|c|c}
j&w^B_{j,-1}&w^B_{j,i}\\ \hline
1&1825/32&1025/64-(2625/64)i\\
2&163121/128&22883/64-(117355/128)i.
\end{array}                                             \tag{4.5}
$$



Again the $-i$ weight is the conjugate.

With $K=2j+2$, the correctly signed contraction is



$$
B_0=\chi_4(p)(-K)
 \left\{
 \widehat T_j(-1)w^B_{j,-1}
 +\tau_p(\widehat T_j(i))w^B_{j,i}
 +\tau_p(\widehat T_j(-i))w^B_{j,-i}
 \right\}.                                             \tag{4.6}
$$



Substitution of (4.1)--(4.5) proves the four constants in (1.2) and
(1.4).  This is a symbolic evaluation of the actual constrained
Bockstein class; no finite interpolation is used.

## 5. Exact thresholds and exceptions

All denominators in (1.2) and (1.4) are powers of $2$, hence units for
the primes in scope.

For $j=1,s=1$,



$$
2735=5\cdot547,\qquad
 5295=3\cdot5\cdot353.                                  \tag{5.1}
$$



The factor $547$ is $3\pmod4$, so it cannot divide the numerator used
in the $p\equiv1\pmod4$ branch.  The factor $353$ is $1\pmod4$, so it
cannot divide the numerator used in the $p\equiv3\pmod4$ branch.  The
remaining factors are below the admissible threshold $p\ge7$.  This
proves (1.3) for every prime, not merely for primes in a checked range.

For $j=2,s=0$,



$$
918897=3\cdot7^3\cdot19\cdot47,\qquad
 59829=3\cdot7^2\cdot11\cdot37.                         \tag{5.2}
$$



Every prime factor of the first numerator is $3\pmod4$, so none can
occur on its $p\equiv1\pmod4$ branch.  On the second branch, $37$ is
$1\pmod4$; the compatible primes are exactly $7,11$.  This proves
(1.5), and proves nonvanishing for every $p\ge13$.

## 6. What this does and does not resolve

Item 175 showed that the ambient five-value $B_0$ functional does not
collapse on any fixed band.  Equations (1.2)--(1.5) now prove more: on two
actual constrained slices, the moving $\bar T$-values themselves do not
cancel, apart from the two completely classified small exceptions on the
second slice.

The theorem does **not** classify other values of $s$ inside $j=1,2$,
other bands $j\ge3$, or the gates $A_0,A_1$.  Since $B_0\ne0$ blocks
the cubic gate $A_0=A_1=B_0=0$, these two rays carry no cubic survivors
above the stated thresholds.  A fixed ray has zero log-prime mass in the
content problem, so this exclusion supplies structural information but no
asymptotic gain.

## 7. Integrated narrow circular-sign erratum

Under the archive circular-coordinate convention
$E=-4\operatorname {Im}\operatorname {Res}_i$, inverse Frobenius acts on
that coordinate with the quadratic sign
$\chi_4(p)=(-1)^{(p-1)/2}$.  Therefore Item 172 equation (4.11) reads

> 

$$
> B_0=\chi_4(p)\sum_{a\in\mathcal S}
> \tau_p(n_a\bar T(a))
> (E_jL_{j,a}-L_jE_{j,a})\pmod p.
>
$$



Item 172 equation (4.10), the $A_0$ formula, is unchanged.  Item 175
equation (4.1) inherits the same prefactor, and its signed coefficient
(4.3) is


$$
\chi_4(p)(3j+2)w^B_{j,1}.
$$


The unsigned core $(3j+2)w^B_{j,1}$ is the fixed nonzero rational used
in the exceptional-prime argument.

Consequences of the erratum are exactly scoped:

- Item 172's finite counts $2649,119,104,10,8$ do not change.
- Its ten cubic survivors do not change.
- Its displayed Hasse-control $B_0$ values do not change.
- Every theorem stated only in terms of $B_0=0$ remains valid.
- Item 175's all-$j$ nonzero theorem, exceptional-prime set, weights,
  and finite coordinate checks do not change.
- A direct numerical use of the old contraction at $p\equiv3\pmod4$
  must negate the resulting $B_0$ residue; $p\equiv1\pmod4$ is
  unchanged.

## 8. Deterministic certificate

The standard-library checker

`scripts/item177_actual_fixed_band_certificate.py`

performs the following exact tasks.

1. It verifies the integer four-section reductions (3.2) and (3.7) for all
   primes through $1000$.
2. It multiplies out the rational identities (3.5) and (3.10).
3. It computes the $x^p$-kernel coefficients in (3.12) and verifies the
   exact wedge cancellation (3.15).
4. It reconstructs all weights in (4.5) from exact
   $\mathbb Q(i)$-principal parts.
5. It evaluates the Gaussian Frobenius branches and reproduces all four
   rational constants in (1.2) and (1.4).
6. It factors all four numerators and checks every prime through $1000$
   against the closed formulas.
7. It independently replays seven representative $B_0$ digits with the
   modulo-$p^2$ local Hasse recurrence, including both exceptional zeros.

The symbolic identities and factor-class arguments prove the all-prime
statements.  The finite loops are normalization audits.  Two canonical
executions are required to be byte-identical before integration.

## 9. Status ledger

### PROVED

- Actual constrained $B_0\ne0$ for every prime $p\ge7$ on
  $(j,s)=(1,1)$.
- Actual constrained $B_0=0$ exactly at $p=7,11$, and nowhere for
  $p\ge13$, on $(j,s)=(2,0)$.
- The exact primitive-representative correction (3.12)--(3.15).
- The $\chi_4(p)$ erratum and invariance of all Item 172/175 zero and
  nonvanishing statements.

### FINITE AUDIT

- Four-section and closed-form prime checks through $p\le1000$.
- Seven independent exact Hasse replays.

### OPEN

- Other $s$-slices in $j=1,2$ and all $j\ge3$.
- Actual fixed-band classification of $A_0,A_1$.
- Any positive-mass consequence or improved content exponent.
- The rationality, irrationality, or transcendence of $e+\pi$.
