> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 196 — the all-moving first-gate map on the rank-one cell

Date: 2026-08-30

## 1. Scope and verdict

This item returns to the positive-mass $\kappa=1$ cell of Item 172 and
allows the residual coordinate $s$ to move through its full range.  It
does not assume digit independence and it does not replace the separate
second-lift digit $A_1$.

The conclusions are deliberately scoped.

**PROVED — a prime-independent all-moving rational primitive.**  Put



$$
k=3s+2.
$$



Two explicit positive integers $g_0(s),g_1(s)$, followed by one rational
primitive $G_s$, determine the moving primitive for every admissible
prime and the two first gates whenever $p\ge2j+3$.  The primitive has
poles only at $0,1$, is normalized by
$G_s(\infty)=0$, and is independent of $p$.  Its polynomial numerator
$B_s=u^kG_s$ satisfies



$$
\deg B_s=2k-2=6s+2,
 \qquad [x^{2k-2}]B_s={g_1(s)\over2},
 \qquad M_kB_s\in\mathbb Z[x],                         \tag{1.1}
$$



where $M_k=\operatorname{lcm}(1,\ldots,k)$.  Since every cell prime has
$p>k$, all denominators in this primitive are automatically $p$-units.

**PROVED — exact separated formulas for $A_0$ and $B_0$.**  For
$p\ge2j+3$, the two gates are rational contractions



$$
A_0\equiv C^A_{j,s,\rho}\pmod p,
 \qquad B_0\equiv C^B_{j,s,\rho}\pmod p,
 \qquad \rho=p\bmod4,                                  \tag{1.2}
$$



in which the moving vector depends only on $(s,\rho)$, while the Cartier
weight vector depends only on $j$.  Equations (4.5)--(4.6) give the map
explicitly.  This is an all-moving version of the fixed-$s$ formulas used
in Items 177, 178, and 181.

**PROVED — scoped obstruction to the existing sign method.**  A Cayley
sign proof can establish that the rational number
$C^B_{j,s,\rho}$ is nonzero.  When $s$ is fixed, this leaves only
finitely many exceptional primes.  When $s=s(p)$ moves, it gives no
uniform information about



$$
p\mid\operatorname{num}C^B_{j,s,\rho}. \tag{1.3}
$$



This is not merely a logical possibility.  On the exact cell row



$$
(m,p,j,s)=(11,13,1,3),
$$



one has



$$
C^A_{1,3,1}={2607104\over99}\equiv4\pmod {13},
 \qquad
 C^B_{1,3,1}=-{2213120\over33}\ne0\quad\hbox{over }\mathbb Q,
 \qquad C^B_{1,3,1}\equiv0\pmod {13}.                 \tag{1.4}
$$



This row lies inside Item 181's proved nonzero Cayley-sign family for
$s=3$; the obstruction is rationally nonzero, yet the actual prime
divides the gate numerator.

Thus even an all-$(j,s)$ rational sign theorem would not, by itself,
give the required modular zero count.  This is a no-go only for that
inference; it is not a no-go for Route 1 or for a stronger arithmetic
argument controlling the numerators in (1.3).

**PROVED — fixed and slowly growing residual layers have zero rate.**  If
$0\le s\le S(m)$, the total log-prime weight of all such rank-one rows is



$$
O\bigl((S(m)+1)\log m\bigr).   \tag{1.5}
$$



Consequently $S(m)=o(m/\log m)$ has zero Route-1 capacity.  The first
four frozen layers $s=0,1,2,3$ therefore cannot address the positive-mass
part of the cell.

**OPEN.**  No uniform sublinear zero count for the moving map is proved.
The $A_0$ zero set, the second digit $A_1$, and their joint
synchronization with $B_0$ remain separate.  No content exponent is
improved and no conclusion about $e+\pi$ is claimed.

## 2. The moving cell and its two scalar sequences

On the $\kappa=1$ cell,



$$
2m+1=(j+1)p-s,
 \qquad 0\le s\le{p-3\over3},
 \qquad s\equiv j\pmod2,                               \tag{2.1}
$$



and



$$
F_j={u^{3j+2}\over Q^{2j+2}},
 \qquad
 P_0=u^{p-3s-3}Q^{2s+1},
 \qquad
 P_1=u^{p-3s-3}Q^{2s},                                 \tag{2.2}
$$



where



$$
u=x(1-x),\qquad Q=(1+x)(1+x^2)=1+x+x^2+x^3.           \tag{2.3}
$$



Let $k=3s+2$.  Item 172's four-section formulas, reduced only after the
exact resonant coefficients have been formed, give



$$
\begin{aligned}
 g_0(s)&=[x^k]{Q^{2s+1}\over(1-x)^{k+1}},\\
 g_1(s)&=[x^k]{Q^{2s}\over(1-x)^{k+1}}.                \tag{2.4}
\end{aligned}
$$



These are ordinary positive integers.  They satisfy, for every cell prime,



$$
\widetilde\gamma_0\equiv g_0(s)\pmod p,
 \qquad
 \widetilde\gamma_1\equiv g_1(s)\pmod p.              \tag{2.5}
$$



For example, the first congruence follows from



$$
\begin{aligned}
 \widetilde\gamma_0
 &=[x^k](1-x)^{p-5s-4}(1-x^4)^{2s+1}\\
 &\equiv[x^k](1-x)^{-5s-4}(1-x^4)^{2s+1}
 =[x^k]{Q^{2s+1}\over(1-x)^{3s+3}}\pmod p.             \tag{2.6}
\end{aligned}
$$



Here $k<p$, so the term $-x^p$ in $(1-x)^p$ cannot enter the
coefficient.  The proof for $g_1$ is identical.

Define



$$
H_s(x)=Q(x)^{2s}\bigl(g_1(s)Q(x)-g_0(s)\bigr).        \tag{2.7}
$$



Then the reduced determinant polynomial is exactly



$$
\bar\Theta
 =\bar\gamma_1P_0-\bar\gamma_0P_1
 =u^{p-k-1}H_s.                                        \tag{2.8}
$$



## 3. A normalized rational primitive valid for every moving $s$

Consider the rational differential



$$
{H_s(x)\over u(x)^{k+1}}\,dx. \tag{3.1}
$$



Its residue at $0$ is



$$
[x^k]{H_s\over(1-x)^{k+1}}
 =g_1(s)g_0(s)-g_0(s)g_1(s)=0.                         \tag{3.2}
$$



Moreover $\deg H_s=2k-1$, so (3.1) is $O(x^{-3})dx$ at
infinity.  Its residue at infinity is zero, and the residue theorem makes
the residue at $1$ zero as well.  Hence (3.1) is rationally exact.

Write its principal parts as



$$
{H_s\over u^{k+1}}
 =\sum_{r=1}^{k+1}a_{s,r}x^{-r}+O(1)\quad(x=0),         \tag{3.3}
$$





$$
{H_s\over u^{k+1}}
 =\sum_{r=1}^{k+1}b_{s,r}(1-x)^{-r}+O(1)\quad(x=1).    \tag{3.4}
$$



Every $a_{s,r},b_{s,r}$ is an integer, since explicitly



$$
\begin{aligned}
 a_{s,r}
 &=[x^{k+1-r}]{H_s(x)\over(1-x)^{k+1}},\\
 b_{s,r}
 &=[y^{k+1-r}]{H_s(1-y)\over(1-y)^{k+1}}.              \tag{3.5}
\end{aligned}
$$



Equation (3.2) and the residue theorem say $a_{s,1}=b_{s,1}=0$.
The unique primitive vanishing at infinity is therefore



$$
\boxed{
 G_s(x)=
 -\sum_{r=2}^{k+1}{a_{s,r}\over r-1}x^{1-r}
 +\sum_{r=2}^{k+1}{b_{s,r}\over r-1}(1-x)^{1-r}.}     \tag{3.6}
$$



It satisfies



$$
G_s'={H_s\over u^{k+1}},
 \qquad G_s(\infty)=0.                                 \tag{3.7}
$$



Put



$$
B_s=u^kG_s.                   \tag{3.8}
$$



The only poles of $G_s$ have order at most $k$, so $B_s$ is a
polynomial.  The decay at infinity gives $\deg B_s\le2k-2$, and
(3.7) gives the exact identity



$$
uB_s'-ku'B_s=H_s.             \tag{3.9}
$$



Since the leading coefficient of $H_s$ is $g_1(s)>0$, comparison in
(3.9) proves equality in the degree bound and the leading-coefficient
claim in (1.1).  Finally, every denominator in (3.6) divides
$M_k$, proving $M_kB_s\in\mathbb Z[x]$.

Every cell prime satisfies $p\ge k+1$.  Thus reduction modulo $p$ is
legitimate, and



$$
\widehat T_{p,s}=u^{p-k}B_s    \tag{3.10}
$$



satisfies $\widehat T_{p,s}'=\bar\Theta$ in characteristic $p$.
The literal reduction of Item 172's zero-constant exact primitive and
$\widehat T_{p,s}$ have degree at most $2p-2$, the same derivative,
and the same constant term.  Their difference is therefore $cx^p$.

As in Item 177,



$$
\mathcal C\left(x^p{dF_j\over F_j}\right)
 =x{dF_j\over F_j},
 \qquad xF_j'\,dx=d(xF_j)-F_j\,dx.                     \tag{3.11}
$$



The relative boundary of $xF_j$ vanishes, and the remaining term is a
multiple of the base vector.  It drops from both determinant wedges.
Consequently $\widehat T_{p,s}$, or equivalently $G_s$, gives the
actual $A_0$ and $B_0$ digits.

## 4. The all-moving rational map

Let $\sigma_1$ be the identity on $\mathbb Q(i)$, and let
$\sigma_3$ be complex conjugation.  For



$$
a\in\{-1,i,-i\},              \tag{4.1}
$$



define the moving value



$$
\boxed{V_{s,\rho}(a)=u(a)G_s\bigl(\sigma_\rho(a)\bigr).}       \tag{4.2}
$$



This is precisely the inverse-Frobenius value needed by Cartier.  Indeed,
$a^p=\sigma_\rho(a)$, and therefore



$$
\begin{aligned}
 \tau_p\bigl(\widehat T_{p,s}(a)\bigr)
 &=\tau_p\bigl(u(a)^{p-k}B_s(a)\bigr)\\
 &=u(a)u(\sigma_\rho(a))^{-k}B_s(\sigma_\rho(a))
 =V_{s,\rho}(a).                                      \tag{4.3}
\end{aligned}
$$



Let



$$
w^A_{j,a}=R_jL_{j,a}-L_jR_{j,a},
 \qquad
 w^B_{j,a}=E_jL_{j,a}-L_jE_{j,a}                      \tag{4.4}
$$



be Item 172's fixed weights, and put $K=2j+2$.  Because the normalized
representative vanishes at $0,1$, the exact all-moving gates are



$$
\boxed{C^A_{j,s,\rho}
 =-K\sum_{a\in\{-1,i,-i\}}V_{s,\rho}(a)w^A_{j,a},}     \tag{4.5}
$$





$$
\boxed{C^B_{j,s,\rho}
 =\chi_4(\rho)(-K)
 \sum_{a\in\{-1,i,-i\}}V_{s,\rho}(a)w^B_{j,a},}        \tag{4.6}
$$



where $\chi_4(1)=1$ and $\chi_4(3)=-1$.  The paired Gaussian terms
make both constants rational.  For every cell prime with $p\ge2j+3$,
their denominators are $p$-units and



$$
A_0\equiv C^A_{j,s,\rho},
 \qquad B_0\equiv C^B_{j,s,\rho}\pmod p.              \tag{4.7}
$$



Equations (2.4), (3.5)--(3.6), and (4.2), (4.5)--(4.6) are the promised
finite rational map.  Its dimensions are fixed at the final Cartier
stage, even though $\deg B_s=6s+2$ grows.

## 5. Cayley form and what its obstruction detects

Assemble the three moving values into



$$
h_{s,\rho}(x)
 ={V_{s,\rho}(-1)\over x+1}
 +{V_{s,\rho}(i)\over x-i}
 +{V_{s,\rho}(-i)\over x+i}
 ={N_{s,\rho}(x)\over Q(x)},                           \tag{5.1}
$$



where



$$
\begin{aligned}
 N_{s,\rho}(x)={}&V_{s,\rho}(-1)(x^2+1)\\
 &+V_{s,\rho}(i)(x+1)(x+i)
 +V_{s,\rho}(-i)(x+1)(x-i).                           \tag{5.2}
\end{aligned}
$$



Thus $N_{s,\rho}\in\mathbb Q[x]$ has degree at most two for every
moving $s$.  Under



$$
y={x+1\over1-x},\qquad t=y-1,\qquad
 \Delta(t)=2+4t+3t^2+t^3,                              \tag{5.3}
$$



put



$$
M_{s,\rho}(y)=(1+y)^3N_{s,\rho}\left({y-1\over y+1}\right),
 \qquad
 M_{s,\rho}(1+t)=\sum_{q=0}^3m_q(s,\rho)t^q.           \tag{5.4}
$$



This gives a four-coordinate rational map



$$
(s,\rho)\longmapsto
                         m_{s,\rho}\in\mathbb Q^4.    \tag{5.5}
$$



Items 178 and 181 used fixed instances of exactly this map.  Their
exactness argument applies to arbitrary $m_{s,\rho}$.  Namely, put



$$
A=3j+2,\qquad K=2j+2,\qquad
 p_r=[t^{A+r}]\Delta(t)^K\quad(r=2,3,4),               \tag{5.6}
$$





$$
q_j=\begin{pmatrix}
 2(A+1)\\4(A+1-K)\\3(A+1-2K)\\A+1-3K
 \end{pmatrix},
 \qquad d=\begin{pmatrix}2\\4\\3\\1\end{pmatrix},      \tag{5.7}
$$





$$
c_j=\begin{pmatrix}
 0\\
 -2(A+2)p_2\\
 -4(A+2-K)p_2-2(A+3)p_3\\
 -3(A+2-2K)p_2-4(A+3-K)p_3-2(A+4)p_4
 \end{pmatrix}.                                        \tag{5.8}
$$



Then



$$
\boxed{C^B_{j,s,\rho}=0\text{ over }\mathbb Q
 \quad\Longrightarrow\quad
 \Omega_{j,s,\rho}:=\det[q_j\ c_j\ d\ m_{s,\rho}]=0.}  \tag{5.9}
$$



This is a useful characteristic-zero nonidentity certificate.  It does
not turn a congruence $C^B_{j,s,\rho}\equiv0\pmod p$ into rational
exactness, so it does not give a modular root count.

## 6. The precise fixed-$s$ barrier

For fixed $(j,s,\rho)$, equation (4.6) is a fixed rational number.
Proving it nonzero leaves only the primes dividing its numerator.  This is
why the sign arguments of Items 178 and 181 prove eventual nonvanishing on
each fixed slice.

On a moving slice, the numerator changes with $s$.  The exact witness
(1.4) shows that rational nonzero and even a definite sign are compatible
with an actual modular zero.  Therefore a uniform extension of the old
sign calculation would still require a new arithmetic theorem controlling
the prime divisors of the moving numerator.

There is also a direct rate obstruction to treating more fixed layers.
From (2.1), every row with a given $s$ satisfies



$$
p\mid 2m+1+s.                 \tag{6.1}
$$



For fixed $s$, $j+1=(2m+1+s)/p$ is then determined by $p$, so there
is no hidden band multiplicity.  Hence



$$
\begin{aligned}
 \sum_{\substack{\kappa=1\text{ rows}\\0\le s\le S(m)}}\log p
 &\le\sum_{s=0}^{S(m)}\log(2m+1+s)\\
 &=O\bigl((S(m)+1)\log m\bigr),                       \tag{6.2}
\end{aligned}
$$



which proves (1.5).  In particular, any bounded collection of residual
layers has zero capacity, and even $S(m)=o(m/\log m)$ remains too small.

The all-moving data are also outside the fixed-support primitive class:
$\deg B_s=6s+2$, while



$$
g_1(s)\ge[x^k](1-x)^{-k-1}={2k\choose k}.             \tag{6.3}
$$



Thus neither the polynomial support nor its coefficient height stays
fixed as $s$ grows.  Equation (6.3) does not prove that the final gate
has many zeros; it records why Item 172's fixed-polynomial thinness theorem
does not automatically apply to this map.

## 7. PNT-scale capacity and the three separate gates

The full $\kappa=1$ cell has log-prime coefficient



$$
C_1=-1-{\pi\over\sqrt3}+3\log3
 =0.4820375017701112\ldots\quad\text{per }m.            \tag{7.1}
$$



To display the scale genuinely missed by fixed $s$, split at
$s/p=1/6$.  In the $j$-th PNT band this split is



$$
{2\over j+1}<{p\over m}<{12\over6j+5}
 \quad\hbox{and}\quad
 {12\over6j+5}\le {p\over m}<{6\over3j+2}.            \tag{7.2}
$$



The two coefficients are



$$
\begin{aligned}
 C_{1,<1/6}
 &=\sum_{j\ge1}\left({12\over6j+5}-{2\over j+1}\right)\\
 &=\log432-\sqrt3\,\pi-{2\over5}
 =0.2270274955414568\ldots,                            \tag{7.3}
\end{aligned}
$$





$$
\begin{aligned}
 C_{1,\ge1/6}
 &=\sum_{j\ge1}\left({6\over3j+2}-{12\over6j+5}\right)\\
 &=-\log16-{3\over5}+{2\pi\over\sqrt3}
 =0.2550100062286545\ldots.                            \tag{7.4}
\end{aligned}
$$



Both are positive; (7.4) alone is more than half of the rank-one cell.
One hypothetical extra valuation copy on the far subcell would have
normalized ceiling



$$
{C_{1,\ge1/6}\over6}
 =0.0425016677047757\ldots .                            \tag{7.5}
$$



The valuation gates must remain separate:

1. The first $\kappa=1$ copy is already part of the proved Item 149
   radical mass.
2. A second copy is governed by $A_0=0$.  Equation (4.5) represents this
   gate exactly, but no moving zero theorem is proved.  Its whole-cell
   ceiling is $C_1/6=0.0803395836283519\ldots$.
3. A third copy requires the joint system
   $A_0=A_1=B_0=0$.  Equation (4.6) handles only the first circular gate;
   $A_1$ remains the genuine modulo-$p^3$ Hasse lift.  Its whole-cell
   ceiling is another $C_1/6$.

Thus the new map is structurally exact but supplies no content gain by
itself.

## 8. Deterministic certificate, frozen artifacts, and status ledger

The standard-library checker

    work/item196_rankone_moving_gate_certificate.py

performs the following exact tasks.

1. It verifies the two coefficient forms of $g_0,g_1$.
2. It constructs $B_s$ and verifies (1.1), (3.5), and (3.9).
3. It evaluates $G_s$ and $B_s/u^k$ independently at all three pole
   divisors and verifies equality.
4. It builds $N_{s,\rho}$ and the four-coordinate Cayley vector.
5. It reproduces the fixed-$s$ constants of Items 177 and 181.
6. It reproduces four independent Item 172 Hasse controls for both
   $A_0$ and $B_0$, including the two $p=107,s=15$ non-scalar rows.
7. It verifies the exact witness (1.4) and the capacity split.

The canonical run uses $0\le s\le24$.  This finite range audits the
all-$s$ algebraic proof; it is not used to extrapolate a zero count.
Canonical and replay outputs are required to be byte-identical.

The checker resolves its pinned Item 175 and Item 178 helpers either beside
the checker in work/ or beside it after archival in scripts/.  Its JSON
stores only archive-relative dependency keys and hashes, never host paths.
An archive-layout replay with the checker and helpers under scripts/ and
the default output under results/ is required to be byte-identical to the
work-layout canonical JSON.

The frozen archive-relative artifact set is:

    sources/item196_rankone_moving_gate_report.md
    scripts/item196_rankone_moving_gate_certificate.py
    results/item196_rankone_moving_gate_certificate.json
    results/item196_rankone_moving_gate_certificate_replay.json
    results/item196_rankone_moving_gate_hashes.sha256

The hash manifest also pins the imported Item 175/178 helper scripts and
the Item 172, 175, 177, 178, and 181 reports/results used for normalization
and exact replay comparisons.

Status summary:

- **PROVED:** the all-moving rational primitive, denominator bound, and
  exact $A_0/B_0$ map.
- **PROVED:** the fixed/slow residual-layer zero-rate theorem (6.2).
- **PROVED:** rational sign nonzero does not imply modular nonzero on a
  moving slice, by the exact witness (1.4).
- **PROVED:** the PNT capacity split (7.3)--(7.5).
- **FINITE AUDIT:** exact replay through $s=24$ and the listed Hasse
  controls.
- **OPEN:** a uniform sublinear modular zero count for either first gate.
- **OPEN:** the joint moving system $A_0=A_1=B_0=0$.
- **OPEN:** any improved Route-1 content exponent and the rationality,
  irrationality, or transcendence of $e+\pi$.
