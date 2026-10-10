> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 234 — first $p^2$/Witt lift of the corrected $j=1$ common-log system

Checked: 2026-08-31 (Beijing time)

## 1. Scope and verdict

Work on the actual $j=1$ row


$$
p=4h+6s+3=2r+6s+3,\qquad r=2h,\qquad h,s\geq1,
 \tag{1.1}
$$


and retain both endpoint indices $\nu=0,1$.

This item produces the first coefficient-level second digit of the
corrected common-log system.

**PROVED — exact all-row Witt expansion.**  If $C_\nu$ is the original
integer coefficient of Item 197, then $p\mid C_\nu$, and $C_\nu/p$
is computed modulo $p^2$ by an explicit linear-plus-quadratic Frobenius
defect.  The quadratic term is the square


$$
6U^2V^{-5}(VA-UB)^2.                                           \tag{1.2}
$$


All signs and both harmonic-number correction terms are derived below.

**PROVED — unreduced rational-moment lift.**  Let $M_\nu$ be the exact
Item 223 boundary moment, before reduction modulo $p$.  There are
explicit $p$-integral carries $R_\nu,J_\nu,E_\nu$ such that


$$
\begin{aligned}
 H_{1,\nu}&=Q_\nu+2pR_\nu,\\
 H_{1,\nu}&=-\epsilon M_\nu+pJ_\nu,\\
 {C_\nu\over p}&\equiv
 6Q_\nu+p(12R_\nu+E_\nu)\pmod {p^2}.              \tag{1.3}
\end{aligned}
$$


Here $\epsilon=(-1)^{(p-1)/2}$.  On the first common-log gate,
$Q_\nu\in p\mathbb Z_{(p)}$, equation (1.3) proves explicitly that
$M_\nu\in p\mathbb Z_{(p)}$ before $M_\nu/p$ is written.

**PROVED — a genuine branch-specific second-digit invariant.**  On that
gate put $Q_\nu^{(1)}=Q_\nu/p$ and
$M_\nu^{(1)}=M_\nu/p$ in $\mathbb F_p$.  Then


$$
\boxed{\;
 \Omega_\nu
 =6Q_\nu^{(1)}+12R_\nu+E_\nu
 =-6\epsilon M_\nu^{(1)}+6J_\nu+E_\nu
 \equiv {C_\nu\over p^2}\pmod p .\;}              \tag{1.4}
$$


Consequently $p^3\mid C_\nu$ if and only if
$\Omega_\nu=0$.  This is a per-coordinate equivalence, but it is only a
necessary invariant for any larger Route-1 collision problem.
Throughout this report $\Omega_\nu$ means the **Item 234 $j=1$ Witt
digit** in (1.4).  It is unrelated to the $j=2$ quantity denoted
$\Omega$ in Item 224.

**PROVED — terminal multiplicities and a separate antiperiod carry.**
At the four terminal phases $a=2,3,4,5$, the exact leading multiplier
is $ap$, not $p$.  After pole deletion the exact terminal equation is


$$
B_t\widehat u_t-C_t\widehat u_{t+1}
 +D_t\widehat u_{t+2}-ap\,\widehat u_{t+3}
 =\ell_{ap-1}.                                                   \tag{1.5}
$$


The first lift of antiperiodicity introduces a new squared-denominator
coordinate $v_t$:


$$
\begin{aligned}
 \widehat u_{t+2p}+\widehat u_t&\equiv2p\,v_t\pmod {p^2},\\
 \widehat u_{t+4p}-\widehat u_t&\equiv-4p\,v_t\pmod {p^2}.
                                                                  \tag{1.6}
\end{aligned}
$$


This theorem is logically separate from $\Omega_\nu$.

**PROVED — sharply scoped terminal no-go.**  Once a first-digit terminal
compatibility holds, division of (1.5) by $p$ gives


$$
{B_t\widehat u_t-C_t\widehat u_{t+1}
 +D_t\widehat u_{t+2}-\ell_{ap-1}\over p}
 =a\,\widehat u_{t+3}.                                          \tag{1.7}
$$


Since $a=2,3,4,5$ is a $p$-unit for every actual row, one lifted
terminal merely determines the free post-terminal digit.  It supplies no
new compatibility by itself.

**EXACT FINITE ONLY.**  Direct integer/rational replay covers all 184
actual rows through $p\leq151$, hence 368 coordinates.  The larger
exact census covers all 22,934 actual rows through $p\leq2000$.  It
finds 46 individual first-gate zeros, no joint first-gate zero, and no
individual $M_\nu^{(1)}=0$ or $\Omega_\nu=0$ among those 46.  These
statements are not extrapolated.

**OPEN.**  No simultaneous first-gate row is excluded for all primes; no
all-row theorem controls $\Omega_0,\Omega_1$ on a hypothetical common
row; and the squared-denominator coordinate $v_t$ is not closed
arithmetically.  No Route-1 rate or exponent is booked.

## 2. Exact coefficient and support window

Put


$$
\begin{aligned}
 m&=3h+4s+2,&q_\nu&=2s-\nu,\\
 N_\nu&=3p-q_\nu-1=4m+\nu,\\
 P_\nu(z)&=(1-z)^r(1+z)^{1+3\nu}(1+z^2)^{q_\nu},\\
 G(z)&={(1-z)^4\over(1+z^2)^3}.
                                                               \tag{2.1}
\end{aligned}
$$


Then the original Item 197 integer is exactly


$$
C_\nu=[z^{N_\nu}]G(z)^pP_\nu(z).                              \tag{2.2}
$$


The degree


$$
d_\nu=\deg P_\nu=r+4s+1+\nu                                  \tag{2.3}
$$


satisfies


$$
p-q_\nu-1-d_\nu=r+1>0.                                       \tag{2.4}
$$



Set


$$
U=1-z^p,\qquad V=1+z^{2p}.                                   \tag{2.5}
$$


The series $U^4V^{-3}$ has support only at nonnegative multiples
$kp$.  For $k=0,1,2$,


$$
N_\nu-kp\geq N_\nu-2p=p-q_\nu-1>d_\nu,                        \tag{2.6}
$$


whereas for $k\geq3$,


$$
N_\nu-kp\leq-q_\nu-1<0.                                      \tag{2.7}
$$


Therefore


$$
[z^{N_\nu}]U^4V^{-3}P_\nu=0                                  \tag{2.8}
$$


as an exact integer coefficient.  This support zero, rather than a
division argument, proves $p\mid C_\nu$ in the expansion below.

## 3. The exact Witt expansion

Define the integer polynomials


$$
A={(1-z)^p-U\over p},\qquad
 B={(1+z^2)^p-V\over p}.                                      \tag{3.1}
$$


Thus $(1-z)^p=U+pA$ and $(1+z^2)^p=V+pB$.  In
$\mathbb Z_{(p)}[[z]]$, expansion through order $p^2$ gives


$$
\begin{aligned}
 &(U+pA)^4(V+pB)^{-3}\\
 &\quad=U^4V^{-3}
 +p\,L(A,B)+p^2K(A,B)\pmod {p^3},                 \tag{3.2}\\
 L(A,B)&=4U^3V^{-3}A-3U^4V^{-4}B,\\
 K(A,B)&=6U^2V^{-3}A^2-12U^3V^{-4}AB+6U^4V^{-5}B^2\\
       &=6U^2V^{-5}(VA-UB)^2.                     \tag{3.3}
\end{aligned}
$$


The use of modulus $p^3$ in (3.2) is essential: after the exact support
zero (2.8) is subtracted and one factor $p$ is divided out, it yields
the quotient modulo $p^2$:


$$
{C_\nu\over p}\equiv
 [z^{N_\nu}]\{L(A,B)+pK(A,B)\}P_\nu\pmod {p^2}.                 \tag{3.4}
$$



For $1\leq k\leq p-1$, let


$$
H_{k-1}=\sum_{j=1}^{k-1}{1\over j}\in\mathbb Z_{(p)}.
$$


The exact product for $\binom pk/p$ gives


$$
{1\over p}\binom pk
 \equiv {(-1)^{k-1}\over k}(1-pH_{k-1})\pmod {p^2}.             \tag{3.5}
$$


Consequently


$$
\begin{aligned}
 A&\equiv A_0+pA_1\pmod {p^2},&
 A_0&=-\sum_{k=1}^{p-1}{z^k\over k},&
 A_1&=\sum_{k=1}^{p-1}{H_{k-1}z^k\over k},\\
 B&\equiv B_0+pB_1\pmod {p^2},&
 B_0&=\sum_{k=1}^{p-1}{(-1)^{k-1}z^{2k}\over k},&
 B_1&=-\sum_{k=1}^{p-1}{(-1)^{k-1}H_{k-1}z^{2k}\over k}.
                                                               \tag{3.6}
\end{aligned}
$$


Every displayed denominator is one of $1,\ldots,p-1$, hence a
$p$-unit.

Define


$$
\begin{aligned}
 D_\nu&=[z^{N_\nu}]L(A_0,B_0)P_\nu,\\
 E_\nu&=[z^{N_\nu}]
 \{L(A_1,B_1)+K(A_0,B_0)\}P_\nu\pmod p.            \tag{3.7}
\end{aligned}
$$


Then


$$
{C_\nu\over p}\equiv D_\nu+pE_\nu\pmod {p^2}.                  \tag{3.8}
$$



## 4. Exact reflection carry

Let


$$
\lambda_\nu=p-q_\nu-1,\qquad
 T=r+6s+2,\qquad
 H_\nu(n)=[z^n]P_\nu\log(1+z^2),                               \tag{4.1}
$$


and put


$$
\begin{aligned}
 Y_\nu&=[z^{\lambda_\nu}]B_0P_\nu,\\
 Y'_\nu&=[z^{2p-q_\nu-1}]B_0P_\nu,\\
 Q_\nu&=2H_\nu(T)-H_\nu(\lambda_\nu).                          \tag{4.2}
\end{aligned}
$$



Direct section extraction in (3.7) is exact over $\mathbb Q$.  In the
$A_0$-factor, the coefficient of $z^{2p}$ in
$U^3V^{-3}$ is $3-3=0$.  In the $B_0$-factor, the coefficients of
$z^p,z^{2p}$ in $U^4V^{-4}$ are $-4,2$.  All other sections miss
the support.  Hence


$$
D_\nu=12Y'_\nu-6Y_\nu=6(2Y'_\nu-Y_\nu).                       \tag{4.3}
$$



The polynomial $P_\nu$ is self-reciprocal and


$$
d_\nu+q_\nu+1=T,\qquad p-T=r+1>0.                             \tag{4.4}
$$


Writing $j=p-k$ in $Y'_\nu$, then using self-reciprocity, gives


$$
\begin{aligned}
 Y'_\nu
 &=\sum_{j=1}^{p-1}{(-1)^j\over p-j}P_{\nu,T-2j}\\
 &=H_\nu(T)+pR_\nu,                                            \tag{4.5}\\
 R_\nu
 &=\sum_{j=1}^{p-1}
 {(-1)^jP_{\nu,T-2j}\over j(p-j)}.
                                                               \tag{4.6}
\end{aligned}
$$


Coefficients outside the support are zero.  Also
$Y_\nu=H_\nu(\lambda_\nu)$ exactly, since
$\lambda_\nu<p$, so the finite logarithm has not yet truncated.
Equations (4.2)--(4.6) prove


$$
D_\nu=6Q_\nu+12pR_\nu.                                       \tag{4.7}
$$


Every denominator in $R_\nu$ is a $p$-unit.

## 5. Exact unreduced endpoint moment and the Hermite carry

Let


$$
\mathcal L_\epsilon(f)=
 (2\epsilon-i)\int_0^{-i}f(z)\,dz+
 (2\epsilon+i)\int_0^if(z)\,dz                                \tag{5.1}
$$


and define the unreduced rational moment


$$
M_\nu=\mathcal L_\epsilon(z^{p+r}P_\nu).                      \tag{5.2}
$$


For a monomial,


$$
\mathcal L_\epsilon(z^q)={\ell_q\over q+1},\qquad
 \ell_q=(2\epsilon-i)(-i)^{q+1}+(2\epsilon+i)i^{q+1}\in\mathbb Z.
                                                               \tag{5.3}
$$



Write $P_\nu=\sum_{a=0}^{d_\nu}p_{\nu,a}z^a$, and set


$$
D_{\nu,a}=2p-q_\nu-1-a.                                      \tag{5.4}
$$


Self-reciprocity in (5.2) gives the exact sum


$$
M_\nu=\sum_{a=0}^{d_\nu}
 {p_{\nu,a}\ell_{D_{\nu,a}-1}\over D_{\nu,a}}.                 \tag{5.5}
$$


The full support inequalities are


$$
p+r+1
 =2p-q_\nu-1-d_\nu
 \leq D_{\nu,a}
 \leq2p-q_\nu-1<2p.                                           \tag{5.6}
$$


Thus every $D_{\nu,a}$ is strictly between $p$ and $2p$, so
$M_\nu\in\mathbb Z_{(p)}$.

Define


$$
J_\nu=
 \sum_{\substack{0\leq a\leq d_\nu\\D_{\nu,a}\ {\rm odd}}}
 {2\epsilon(-1)^{(D_{\nu,a}-1)/2}p_{\nu,a}
 \over D_{\nu,a}(D_{\nu,a}-p)}.                               \tag{5.7}
$$


In addition to (5.6),


$$
r+1\leq D_{\nu,a}-p\leq p-q_\nu-1<p,                          \tag{5.8}
$$


so every divided quantity in $J_\nu$ has a $p$-unit denominator.

Here is a coefficientwise proof of the sign in the second identity of
(1.3).  If $D=D_{\nu,a}$ is even, the $a$-weight in
$H_{1,\nu}=2Y'_\nu-Y_\nu$ is


$$
{4(-1)^{D/2-1}\over D}
 =-{\epsilon\ell_{D-1}\over D}.                               \tag{5.9}
$$


If $D$ is odd, its $H_{1,\nu}$-weight is


$$
{2\epsilon(-1)^{(D-1)/2}\over D-p},
                                                               \tag{5.10}
$$


while its weight in $-\epsilon M_\nu$ is


$$
{2\epsilon(-1)^{(D-1)/2}\over D}.                             \tag{5.11}
$$


The difference between (5.10) and (5.11) is exactly $p$ times
the summand in (5.7).  Therefore


$$
\boxed{H_{1,\nu}=-\epsilon M_\nu+pJ_\nu}                      \tag{5.12}
$$


over $\mathbb Q$, not just modulo $p$.

Combining (4.5) with (5.12) yields


$$
Q_\nu=-\epsilon M_\nu+p(J_\nu-2R_\nu).                        \tag{5.13}
$$



## 6. What the second digit does and does not say

Because $6$ is a unit for $p\geq13$, (3.8), (4.7), and (5.13)
give the first-gate equivalences


$$
\begin{aligned}
 p^2\mid C_\nu
 &\iff Q_\nu\in p\mathbb Z_{(p)}\\
 &\iff M_\nu\in p\mathbb Z_{(p)}.                              \tag{6.1}
\end{aligned}
$$


This proves the divisibility of $M_\nu$ before
$M_\nu^{(1)}=M_\nu/p$ is defined.  Dividing (3.8) only after (6.1)
is legitimate: on the gate, (3.8) first reads


$$
{C_\nu\over p}\equiv p\Omega_\nu\pmod {p^2}.
 \tag{6.1a}
$$


Because (6.1) gives $p^2\mid C_\nu$, division of (6.1a) by $p$
then gives $C_\nu/p^2\equiv\Omega_\nu\pmod p$, proving (1.4).

There are two possible meanings of “one extra digit,” and they must not
be conflated:

1. An extra digit of the exact endpoint moment is
   $M_\nu\in p^2\mathbb Z_{(p)}$, equivalently
   $M_\nu^{(1)}=0$.  This equivalence is merely a valuation rewrite.
2. An extra digit of the original integer-residue coordinate is
   $p^3\mid C_\nu$, equivalently $\Omega_\nu=0$.  Formula (1.4)
   is the new branch-specific transport identity relating this digit to
   the endpoint system.

If both notions of extra digit are imposed, then (1.4) reduces to the
explicit carry condition


$$
\boxed{\Xi_\nu:=6J_\nu+E_\nu=0\pmod p.}                       \tag{6.2}
$$


Thus, for two coordinates, an endpoint-extra and coefficient-extra
common lift forces


$$
M_0^{(1)}=M_1^{(1)}=\Xi_0=\Xi_1=0.                            \tag{6.3}
$$


No sufficiency for the full Route-1 problem is claimed.

## 7. Exact terminal lift with multiplicities retained

Factor


$$
W=(1-z)^r(1+z^2)^{2s-1},\qquad
 P_0=(1+z)(1+z^2)W,\qquad P_1=(1+z)^4W.                        \tag{7.1}
$$


For


$$
N_{t,k}=p+r+t+k+1
$$


define the pole-deleted moment


$$
\widehat u_t=
 \sum_{\substack{k\\p\nmid N_{t,k}}}
 {w_k\ell_{N_{t,k}-1}\over N_{t,k}},
 \qquad W=\sum_kw_kz^k.                                       \tag{7.2}
$$


All retained denominators are $p$-units by definition.  At the initial
section no pole is present, and the exact moments are


$$
\begin{aligned}
 M_0&=\widehat u_0+\widehat u_1+\widehat u_2+\widehat u_3,\\
 M_1&=\widehat u_0+4\widehat u_1+6\widehat u_2
       +4\widehat u_3+\widehat u_4.                            \tag{7.3}
\end{aligned}
$$



Let $\sigma=(1-z)(1+z^2)$.  The exact Pearson coefficients are


$$
\begin{aligned}
 A_t&=p+2r+4s+t+2,&B_t&=p+r+t+1,\\
 C_t&=p+2r+t+2,&D_t&=p+r+4s+t+1.                              \tag{7.4}
\end{aligned}
$$


At


$$
t_a=2s+1+(a-2)p,\qquad a=2,3,4,5,                            \tag{7.5}
$$


one has $A_{t_a}=ap$.  Moreover


$$
\deg(\sigma W)=r+4s+1<p,\qquad
 p-\deg(\sigma W)=r+2s+2>0.                                  \tag{7.6}
$$


Thus the support of


$$
K_{t_a}=z^{p+r+t_a+1}\sigma W
$$


contains at most one multiple of $p$.  Its top exponent is exactly
$ap$, and its top coefficient is $-1$.  Deleting that derivative
term gives the exact equality (1.5), with the displayed positive source
$\ell_{ap-1}$.

The same multiplicity is visible before deletion.  The top monomial of
the full $u_{t_a+3}$ has denominator $ap$ and coefficient one, while
all other denominators are $p$-units.  Therefore


$$
p\,u_{t_a+3}\equiv{\ell_{ap-1}\over a}\pmod p.                 \tag{7.7}
$$


Multiplication by the retained factor $a$ in $A_{t_a}=ap$
recovers the source $\ell_{ap-1}$.  Dropping $a$ before division
would give the wrong second digit.

Equation (1.7) now proves the scoped no-go: in the formal transfer
problem the second terminal digit solves for the new free coordinate
$\widehat u_{t_a+3}\bmod p$, because $a$ is invertible.  A single
terminal does not produce another scalar obstruction.

## 8. The squared-denominator antiperiod carry

Define separately


$$
v_t=
 \sum_{\substack{k\\p\nmid N_{t,k}}}
 {w_k\ell_{N_{t,k}-1}\over N_{t,k}^2}\pmod p.                  \tag{8.1}
$$


Again every denominator is a $p$-unit.  Since $p$ is odd,


$$
\ell_{q+2p}=-\ell_q,\qquad \ell_{q+4p}=\ell_q.                 \tag{8.2}
$$


The deleted set in (7.2) is unchanged by either shift.  Term by term,


$$
\begin{aligned}
 {\ell_q\over N}-{\ell_q\over N+2p}
 &\equiv {2p\ell_q\over N^2}\pmod {p^2},\\
 {\ell_q\over N+4p}-{\ell_q\over N}
 &\equiv-{4p\ell_q\over N^2}\pmod {p^2}.                       \tag{8.3}
\end{aligned}
$$


After the sign changes in (8.2), summation proves (1.6).

Thus the naive lift
$\widehat u_{t+2p}=-\widehat u_t\pmod {p^2}$ is false in
general.  Any genuine second-digit phase closure must retain $v_t$.
This coordinate is not used in the coefficient invariant
$\Omega_\nu$; it records a different, terminal/antiperiod obstruction.

## 9. Deterministic replay and finite status

The standard-library checker
work/item234_j1_first_witt_certificate.py verifies:

- the exact rational identities
  $H_{1,\nu}=Q_\nu+2pR_\nu=-\epsilon M_\nu+pJ_\nu$;
- every denominator window (5.6)--(5.8);
- the harmonic Witt digit $E_\nu$;
- (1.4) against the original exact integer coefficient $C_\nu$ on
  all 368 coordinates through $p\leq151$;
- all four terminal multiplicities and unreduced pole digits on three
  representative rows;
- both congruences (1.6) over short exact ranges on those rows; and
- the complete first-gate census through $p\leq2000$.

The census contains


$$
\begin{array}{c|r}
\text{actual rows}&22934\\
Q_0=0&20\\
Q_1=0&26\\
Q_0=Q_1=0&0\\
\text{individual first-gate records}&46\\
M_\nu^{(1)}=0\text{ among those records}&0\\
\Omega_\nu=0\text{ among those records}&0.
\end{array}                                                     \tag{9.1}
$$


The first three exact second digits are


$$
\begin{array}{c|r|r|r|r}
p&h&s&\nu&\Omega_\nu\\ \hline
29&5&1&1&19\\
53&11&1&1&30\\
109&10&11&0&25.
\end{array}                                                     \tag{9.2}
$$


All of (9.1)--(9.2) is **EXACT FINITE ONLY**.

## 10. Final theorem ledger

### PROVED

- Exact support zero and all-row quotient expansion modulo $p^2$.
- Correct $A_0,A_1,B_0,B_1$ harmonic digits and quadratic square.
- Exact reflection carry $R_\nu$.
- Exact unreduced-moment carry $J_\nu$, with every divided denominator
  certified to be a $p$-unit.
- The per-coordinate second-digit identity (1.4), and condition (6.2)
  when endpoint and coefficient extra digits are both required.
- Exact terminal multiplicities $ap$, signs, and pole numerators.
- Squared-denominator antiperiod carry (1.6).
- The local one-terminal no-go (1.7).

### EXACT FINITE ONLY

- Every row count, zero count, nonoccurrence, sample value, and digest in
  the companion certificate.

### OPEN

- An all-prime exclusion of $Q_0=Q_1=0$.
- An all-row obstruction forcing at least one of
  $\Omega_0,\Omega_1$ to be nonzero on a hypothetical common row.
- Arithmetic closure of the $v_t$ phase coordinate.
- Any positive Route-1 rate, valuation exponent, or conclusion about
  $e+\pi$.
