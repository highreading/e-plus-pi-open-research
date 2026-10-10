> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 163 — a scalar-free determinant digit tower through the fifth content layer

Date: 2026-08-29

## 1. Scope and verdict

This note first gives the valuation ledger for an arbitrary forced
prime-power layer



$$
q_p=p^e\le 4m+1<p^{e+1}.
$$



It then specializes the digit formulas and finite certificate to the
asymptotically relevant prime-number-theorem scale $e=1$.  The primes
with $e\ge2$ lie below $O(\sqrt m)$ and have $o(m)$ radical
logarithm.  Let $p$ be a forced rank-one or vanishing rank-two prime
from $\mathcal H_m\cup\mathcal Z_m$, and put



$$
\delta=\mathbf 1_{p\in\mathcal P_m},\qquad D=1+\delta.
$$



The conclusions are separated as follows.

**PROVED — exact two-minor gate.**  Define



$$
X_s=q_pR_s,\qquad
 \mathscr A=L_1X_0-L_0X_1=q_pA_m,\qquad
 \mathscr B=L_1E_0-L_0E_1=8B_m.
$$



The forced Cartier theorem gives



$$
p^D\mid\mathscr A,\mathscr B.
$$



Write their normalized $p$-adic expansions as



$$
{\mathscr A\over p^D}=\sum_{j\ge0}a_jp^j,\qquad
 {\mathscr B\over p^D}=\sum_{j\ge0}b_jp^j,\qquad
 0\le a_j,b_j<p.                                      \tag{1.1}
$$



On the positive-mass $e=1$ scale, the content layers have the exact
gates



$$
\begin{array}{c|l}
p^2\mid c_m&a_0=0,\\
p^3\mid c_m&a_0=a_1=b_0=0,\\
p^4\mid c_m&a_0=a_1=a_2=b_0=b_1=0,\\
p^5\mid c_m&a_0=a_1=a_2=a_3=b_0=b_1=b_2=0.
\end{array}                                                \tag{1.2}
$$



The old lifted digit is exactly $a_0=\eta_{m,p}$.  Starting at the
third content layer when $e=1$, an $A$-digit alone is insufficient:
one must lift the period determinant $\mathscr B$ as well.  For general
$e$, the $B$-minor first enters at layer $p^{e+2}$, as (2.5)
records.

**PROVED — scalar-free determinant digit/carry tower seeded by the first
Bockstein.**  Every digit
in (1.1), and hence every gate in (1.2), is obtained by a finite
convolution-and-carry recurrence.  It divides only by powers of $p$
after verified divisibility.  It never divides by either Cartier scalar,
so zero Cartier images and rank-zero rows cause no singular branch.

**PROVED — deterministic arbitrary-precision coordinate recurrence.**
The item-162 first-order Hasse recurrence computes
$(X_s,L_s,E_s)\pmod {p^M}$ for arbitrary fixed $M$, with the exact
factorial-valuation reserve.  For the gates through $p^5$, $M=7$
works uniformly for both $\delta=0$ and $\delta=1$.

**PROVED NO-GO — four complete support layers still cannot close the
arithmetic threshold.**  Even the optimistic certification of four full
valuation layers on every available forced radical has capacity at most



$$
1.1396325196868866572818193116\ldots
 <1.1561471519642446123307302239\ldots .                \tag{1.3}
$$



Five complete layers are the first count not excluded by this support
ceiling.  This is not a five-layer divisor theorem.

**EXPERIMENTAL — exact finite audit only.**  On all 784 $e=1$ forced
rows with $m\le100$, the Hasse recurrence agrees with the frozen
$U_m,V_m$ modulo $p^6$, all carry digits agree with direct
determinants, and all gates through $p^5$ agree with the actual content
valuation.  The survival counts are $784,58,5,0,0$ for layers one
through five.  These counts have no asserted density or asymptotic
meaning.

**OPEN.**  No positive-mass vanishing theorem is known for the
simultaneous digit systems in (1.2).  In particular, this item does not
improve the proved content exponent and does not decide $e+\pi$.

## 2. Exact normalization and proof of the gates

Let



$$
D_m^\sharp=2^{9m+5}K_m,\qquad
 G_m=\prod_{r\in\mathcal P_m}r,
$$



and write



$$
D_m^\sharp=p^ed,\qquad G_m=p^\delta g,\qquad
 d,g\in\mathbb Z_p^\times.                               \tag{2.1}
$$



The equality $v_p(D_m^\sharp)=e$ uses the definition of $q_p$, while
$p<2m$ keeps $p$ out of the removed middle product.  From the exact
primitive normalization,



$$
U_m={d\over g}{\mathscr A\over p^\delta},\qquad
 V_m={d\over8g}p^{e-\delta}\mathscr B.                  \tag{2.2}
$$



The forced rank-one theorem, and the rank-two theorem on
$\Delta_{p,s}=0$, give proportional endpoint triples modulo $p$ when
$\delta=0$.  Hence both minors are divisible by $p$.  When
$\delta=1$, both endpoint triples vanish separately modulo $p$, so
both minors are divisible by $p^2$.  Uniformly,



$$
p^D\mid\mathscr A,\mathscr B.          \tag{2.3}
$$



Substituting (1.1) into (2.2) gives the exact valuation ledger



$$
\boxed{
 v_p(U_m)=1+v_p\!\left({\mathscr A\over p^D}\right),\qquad
 v_p(V_m)=e+1+v_p\!\left({\mathscr B\over p^D}\right).}   \tag{2.4}
$$



For $e=1$, taking the minimum proves every equivalence in (1.2).
Notice that no nonvanishing hypothesis on $L_s,E_s$, or on a Cartier
scalar, appears.

More generally, for every $r\ge2$, as far as the two normalized series
are known,



$$
p^r\mid c_m
 \quad\Longleftrightarrow\quad
 a_0=\cdots=a_{r-2}=0
 \quad\hbox{and}\quad
 b_0=\cdots=b_{r-e-2}=0.                                \tag{2.5}
$$



The second string is empty when $r\le e+1$.  Formula (2.5) is an exact
all-depth statement, not merely a fifth-order truncation.  It recovers the
item-160 one-coordinate bridge for $r\le e+1$.

## 3. Arbitrary-precision Hasse coordinate evaluator

For $K_s=4m+1+s$, and for a root
$\alpha\in\{-1,i,-i\}$ of $Q$, put



$$
C_{s,\alpha}(r)
 =[t^r]{u(\alpha+t)^{6m}\over Q_\alpha(\alpha+t)^{K_s}}.
                                                               \tag{3.1}
$$



The exact period coordinates are



$$
\begin{aligned}
L_s&=4C_{s,-1}(K_s-1)
   +2C_{s,i}(K_s-1)+2C_{s,-i}(K_s-1),\\
E_s&=2i\bigl(C_{s,i}(K_s-1)-C_{s,-i}(K_s-1)\bigr).
\end{aligned}                                                \tag{3.2}
$$



For the conjugate implementation this is simply
$E_s=-4\operatorname {Im}C_{s,i}(K_s-1)$.

With the item-161 band notation, the exact top-layer endpoint coordinate
is



$$
X_s=q_pR_s=\sum_{h=0}^ep^h\mathcal B_{s,h}
 \quad\hbox{in }\mathbb Z_p.                              \tag{3.3}
$$



For the $e=1$ certificate this is
$X_s=\mathcal B_{s,0}+p\mathcal B_{s,1}$.  Thus
(3.1)--(3.3) compute both determinants to any requested precision.  No
unrecorded lower band is discarded.

For completeness, write locally



$$
F(t)={A(t)^{6m}\over B(t)^{K_s}}=\sum_{n\ge0}C_nt^n,
$$



and set



$$
P(t)=A(t)B(t)=\sum_jP_jt^j,\qquad
 S(t)=6mA'(t)B(t)-K_sA(t)B'(t)=\sum_jS_jt^j.
$$



Coefficient comparison in $PF'=SF$ gives



$$
(n+1)P_0C_{n+1}
 =\sum_{j=0}^{\min(n,\deg S)}S_jC_{n-j}
 -\sum_{j=1}^{\min(n,\deg P)}(n-j+1)P_jC_{n-j+1}.       \tag{3.4}
$$



The constant $P_0$ is a unit at every odd prime.  The only loss in step
$n$ is $v_p(n+1)$.  Starting with the reserve



$$
M+v_p((K_s-1)!)                              \tag{3.5}
$$



therefore returns every
$C_0,\ldots,C_{K_s-1}\pmod {p^M}$.  Every division by
$p^{v_p(n+1)}$ is checked for exactness before the remaining unit is
inverted.

## 4. Scalar-free Bockstein and determinant carries on $e=1$ bands

### 4.1 The differential syzygy

On a rank-one band write



$$
\omega_s=F^pP_s\,dx,\qquad \gamma_s=[x^{p-1}]P_s.
$$



The polynomial



$$
\Theta=\gamma_1P_0-\gamma_0P_1
$$



has zero $x^{p-1}$-coefficient.  Its $p$-integral primitive $T$
satisfies the exact identity



$$
\gamma_1\omega_0-\gamma_0\omega_1
 =d(F^pT)-pF^{p-1}F'T\,dx.                              \tag{4.1}
$$



This is the first determinant Bockstein.  It uses the scalars only by
multiplication.

The same construction covers a vanishing rank-two row.  If the two
resonant coefficient vectors are



$$
(a_s,b_s)=([x^{p-1}]P_s,[x^{2p-1}]P_s),
$$



their determinant is zero.  If $(a_0,a_1)\ne(0,0)$, take
$(\gamma_0,\gamma_1)=(a_0,a_1)$; otherwise take
$(\gamma_0,\gamma_1)=(b_0,b_1)$.  Both resonant coefficients of
$\gamma_1P_0-\gamma_0P_1$ then vanish.  If both rows vanish, both
Cartier images are already zero.  This is a zero test and a
multiplication, not a scalar inversion.

At coordinate level, let $z_s\in\mathbb Z_p^2$ be either relevant pair
of coordinates and suppose



$$
z_s=\Gamma_sv+pw_s
$$



for any integral lifts of the common reduction.  Then



$$
\boxed{
 {z_0\wedge z_1\over p}
 =\Gamma_0v\wedge w_1-\Gamma_1v\wedge w_0
  +p\,w_0\wedge w_1.}                                    \tag{4.2}
$$



Equation (4.2) is exact.  The final quadratic term, invisible in the first
digit, enters the next digit.  When both Cartier scalars vanish, take
$z_s=pw_s$; then



$$
{z_0\wedge z_1\over p^2}=w_0\wedge w_1.  \tag{4.3}
$$



Thus neither (4.2) nor (4.3) divides by a scalar that may be zero.

### 4.2 The all-depth carry recurrence

For any determinant



$$
\mathscr D=AB-CD,
$$



write $A=\sum A_ip^i$, and similarly for $B,C,D$, using digits in
$\{0,\ldots,p-1\}$.  Put



$$
S_n=\sum_{i=0}^n(A_iB_{n-i}-C_iD_{n-i}),\qquad c_{-1}=0, \tag{4.4}
$$



and recursively



$$
\tau_n\equiv S_n+c_{n-1}\pmod p,\quad0\le\tau_n<p,\qquad
 c_n={S_n+c_{n-1}-\tau_n\over p}.                         \tag{4.5}
$$



Then



$$
\mathscr D=\sum_{n\ge0}\tau_np^n.       \tag{4.6}
$$



The quotient in (4.5) is divisible by $p$ by the definition of
$\tau_n$.  Applying (4.4)--(4.6) to



$$
(A,B,C,D)=(L_1,X_0,L_0,X_1)
$$



produces the $a_j$, after dropping the $D$ forced zero digits.
Applying it to



$$
(A,B,C,D)=(L_1,E_0,L_0,E_1)
$$



similarly produces the $b_j$.  Equations (4.4)--(4.6) are the
deterministic determinant digit/carry tower seeded by the first Bockstein and
used by the certificate.

## 5. Why the first lift alone cannot be iterated formally

The first Bockstein data do not determine the next digit in the abstract
coordinate category.  For example, over $\mathbb Z_p^2$, fix



$$
v=(1,0),\qquad z_0=v,\qquad
 z_1=v+pav_2+p^2bv_2,\qquad v_2=(0,1).
$$



Then



$$
z_0\wedge z_1=pa+p^2b.                 \tag{5.1}
$$



Keeping the characteristic-$p$ Cartier data and the first digit $a$
fixed leaves $b\pmod p$ arbitrary.  In particular, after setting
$a=0$, the next normalized digit is still unrestricted.  Therefore a
deeper theorem must use new $p$-adic information, such as the complete
Hasse recurrence; it cannot be a formal reapplication of the old
mod-$p$ proportionality.  This abstract obstruction does not exclude a
special identity in the actual mixed-cubic family.

## 6. Support capacity through five layers

The optimistic radical capacity per $6m$ is



$$
C_{\rm rad}=r_1+{C_2\over6}
 =0.2849081299217216643204548279\ldots .                 \tag{6.1}
$$



If every forced prime carried $k$ complete certified layers, the support
mechanism could certify at most $kC_{\rm rad}$.  The exact ledger is



$$
\begin{array}{c|c|c}
k&kC_{\rm rad}&kC_{\rm rad}-T_{\rm req}\\ \hline
2&0.5698162598434433286409096558&-0.5863308921208012836898205681\\
3&0.8547243897651649929613644837&-0.3014227621990796193693657402\\
4&1.1396325196868866572818193116&-0.0165146322773579550489109123\\
5&1.4245406496086083216022741395&\phantom{-}0.2683934976443637092715439156.
\end{array}                                                  \tag{6.2}
$$



The rank-two term $C_2$ is itself only a radical ceiling.
Consequently the positive fifth-row margin in (6.2) says only that five
layers are the first number not ruled out by support capacity.  It
supplies neither the rank-two radical mass nor any required digit
vanishing.

## 7. Exact finite replay

The standard-library certificate

work/item163_deeper_digits_certificate.py

reuses the archived item-162 local recurrence but takes the prime and
precision explicitly.  It performs the following checks on all 784 unique
forced $e=1$ rows through $m=100$:



$$
\begin{array}{l|r}
\text{check}&\text{failures}\\ \hline
p^D\mid\mathscr A,\mathscr B&0\\
a_0=\eta_{m,p}&0\\
\text{carry recurrence versus direct determinant}&0\\
U_m,V_m\text{ versus frozen coordinates modulo }p^6&0\\
\text{content gates through }p^5&0.
\end{array}                                                  \tag{7.1}
$$



The finite survival counts are



$$
\begin{array}{c|rrrrr}
\text{source}&p^1&p^2&p^3&p^4&p^5\\ \hline
\text{rank one, }\delta=0&453&35&4&0&0\\
\text{rank one, }\delta=1&285&15&1&0&0\\
\text{rank-two zero, }\delta=0&46&8&0&0&0\\ \hline
\text{all}&784&58&5&0&0.
\end{array}                                                  \tag{7.2}
$$



The five $p^3$-survivors are



$$
(m,p)=(36,19),(67,17),(74,19),(89,19),(100,23).          \tag{7.3}
$$



No statement in (7.2)--(7.3) is extrapolated.  Two canonical executions
produce byte-identical JSON with SHA-256

c3234900f80abb0ff2ee4c96e82d8c19fd5734b58135d16c5090e397dcebc9d1.

## 8. Remaining constructive target

For a fifth-layer theorem on a positive-mass $e=1$ family, the exact
target is now the simultaneous congruence system



$$
a_0=a_1=a_2=a_3=b_0=b_1=b_2=0.                         \tag{8.1}
$$



The direct recurrence (3.4) and carries (4.5) make (8.1) a deterministic
finite certificate at every $(m,p)$.  What is missing is a uniform
arithmetic identity forcing (8.1) on enough prime bands.  The first-lift
five-divisor evaluation collapse controls only $a_0$; no corresponding
fixed-support collapse for the later $a_j,b_j$ is proved here.
