> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 256 — the first beta jet and persistence of the phase resonance

Checked: 2026-08-31 (Beijing time)

## 1. Scope and verdict

Keep the Item-255 phase



$$
p=6m+2d+1,\qquad d=r+4\geq5,
 \qquad L=m+1,qquad a=2m+d,qquad b=3m+d+1.         \tag{1.1}
$$



For a $p$-unit $c$, define the value and first denominator jet



$$
\begin{aligned}
 M_q(c)&=\sum_{k=0}^m\binom mk{c^k\over a+q+k},\\
 N_q(c)&=\sum_{k=0}^m\binom mk{c^k\over(a+q+k)^2}.
 \end{aligned}                                                     \tag{1.2}
$$



The target is $M_0(-2)=I_{m,d}$, which vanishes modulo $p$ exactly
when the universal Item-252 prefix $H_m$ vanishes.  Item 255 proved that
the reciprocal value orbit $c=-2$, $c^{-1}=-1/2$ has rank one.  This
item takes that orbit through its first Hasse/jet level.

> **PROVED — exact mod-$p^2$ reflection with the first jet retained.**
> Denominator complementation gives
> 

$$
> \boxed{
> M_L(c)\equiv-c^m\{M_0(c^{-1})+pN_0(c^{-1})\}\pmod {p^2},}       \tag{1.3}
>
$$


> and
> 

$$
> \boxed{N_L(c)\equiv c^mN_0(c^{-1})\pmod p.}                    \tag{1.4}
>
$$


> Thus the next digit genuinely introduces the squared-denominator
> companion; it is not legitimate to reuse the value-only reflection.

> **PROVED — exact endpoint-retaining jet recurrence.**  The Item-255
> value recurrence is
> 

$$
> (a+q)M_q(c)+c(b+q)M_{q+1}(c)=(1+c)^L.            \tag{1.5}
>
$$


> Its differentiated recurrence is
> 

$$
> \boxed{
> (a+q)N_q(c)+c(b+q)N_{q+1}(c)=M_q(c)+cM_{q+1}(c).}               \tag{1.6}
>
$$


> The derivative of the endpoint is zero because the endpoint does not
> depend on $a$.  The original endpoint $(1+c)^L$, in particular
> $(-1)^L$ for $c=-2$, remains in (1.5).

> **PROVED — exact mod-$p^2$ determinant expansion.**  Put
> 

$$
> \mathcal H_{m,d}=\sum_{t=0}^m{1\over a+t}.                       \tag{1.7}
>
$$


> If $A_c$ is the homogeneous value-orbit multiplier, then
> 

$$
> \boxed{A_c\equiv c^{-L}(1+p\mathcal H_{m,d})\pmod {p^2},}       \tag{1.8}
>
$$


> and the reciprocal value matrix has determinant
> 

$$
> \boxed{A_cA_{c^{-1}}-1\equiv2p\mathcal H_{m,d}\pmod {p^2}.}    \tag{1.9}
>
$$


> This is the exact first-Hasse term, with no omitted endpoint.

> **PROVED, SHARPLY SCOPED NO-GO — adjoining the first jet still gives
> no independent condition.**  Iterating (1.5)--(1.6) gives
> 

$$
> \binom{M_L(c)}{N_L(c)}=
> \begin{pmatrix}A_c&0\\B_c&A_c\end{pmatrix}
> \binom{M_0(c)}{N_0(c)}+\binom{E_c}{F_c},         \tag{1.10}
>
$$


> where
> 

$$
> B_c=-LA_c\sum_{q=0}^{L-1}{1\over(a+q)(b+q)}.     \tag{1.11}
>
$$


> Combining the two reciprocal iterations with (1.3)--(1.4), and reducing
> the first-jet system modulo $p$, yields the four-by-four matrix
> 

$$
> \boxed{
> \mathcal J_c=
> \begin{pmatrix}
> c^{-L}&c^m&0&0\\
> c^{-m}&c^L&0&0\\
> B_c&0&c^{-L}&-c^m\\
> 0&B_{c^{-1}}&-c^{-m}&c^L
> \end{pmatrix}.}                                  \tag{1.12}
>
$$


> On every actual phase row,
> 

$$
> B_{c^{-1}}=c^{2L}B_c,\qquad
> \boxed{\operatorname{rank}_{\mathbf F_p}\mathcal J_c=2.}      \tag{1.13}
>
$$


> The affine terms obey the corresponding two compatibilities.  Hence the
> value plus first squared-denominator jet still supplies no polynomial
> obstruction for $M_0(-2)=0$, for $H_m=0$, or for an affine target
> value arising in the Item-251 gate.

> **PROVED — the first-Hasse unit shortcut is false.**  On the admissible
> row $(p,r,s,m,d)=(23,1,3,2,5)$,
> $\mathcal H_{m,d}=1/9+1/10+1/11=299/990\equiv0\pmod {23}$.
> The exact characteristic-zero value determinant has numerator valuation
> two at $23$.  Thus (1.9) cannot be promoted to a universal unit or
> resultant theorem.

> **OPEN / zero booking.**  A second denominator jet appears at order
> $p^3$, but the first-jet rank theorem already proves that the proposed
> two-moment Hasse closure fails.  This item does not claim that every
> higher jet is impossible.  No zero-density theorem or Route-1 rate is
> obtained.

All bounded counts in the checker are **EXACT FINITE ONLY**.

## 2. Reflection to the next Hasse digit

Put $q_k=a+k$.  Reversing $k$ in $M_L(c)$ gives the exact identity



$$
M_L(c)=\sum_{k=0}^m\binom mk{c^{m-k}\over p-q_k}.                 \tag{2.1}
$$



Since every $q_k$ is a $p$-unit,



$$
{1\over p-q_k}\equiv-{1\over q_k}-{p\over q_k^2}\pmod {p^2}.   \tag{2.2}
$$



Substitution in (2.1) proves (1.3).  Squaring the denominator gives



$$
{1\over(p-q_k)^2}\equiv{1\over q_k^2}\pmod p,                  \tag{2.3}
$$



which proves (1.4).  Equations (2.2)--(2.3) explicitly distinguish the
value and jet levels.

For completeness, the next term would be
$-p^2/q_k^3$ in (2.2).  It is not used: mod $p^2$ already suffices
to test the requested first-jet closure.

## 3. Exact coupled recurrence

Equation (1.5) is obtained by integrating the derivative of



$$
u^{a+q}(1+cu)^{m+1}.                            \tag{3.1}
$$



Equivalently it follows termwise from (1.2).  Formally differentiating
(1.5) with respect to $a$, using



$$
-{\partial\over\partial a}M_q(c)=N_q(c),          \tag{3.2}
$$



gives (1.6).  Solving for the next state yields



$$
\begin{aligned}
 M_{q+1}&=\lambda_qM_q+\mu_q,\\
 N_{q+1}&=\lambda_qN_q+\eta_qM_q+\nu_q,           \tag{3.3}
 \end{aligned}
$$



where



$$
\begin{aligned}
 \lambda_q&=-{a+q\over c(b+q)},
 &\mu_q&={(1+c)^L\over c(b+q)},\\
 \eta_q&={L\over c(b+q)^2},
 &\nu_q&={(1+c)^L\over c(b+q)^2}.                 \tag{3.4}
 \end{aligned}
$$



The homogeneous transfer matrices are scalar Jordan matrices, so their
product has the form displayed in (1.10).  Because all diagonal factors
commute,



$$
{B_c\over A_c}=\sum_{q=0}^{L-1}{\eta_q\over\lambda_q}
 =-L\sum_{q=0}^{L-1}{1\over(a+q)(b+q)},            \tag{3.5}
$$



which proves (1.11).  The affine constants $E_c,F_c$ are generated by
the same exact recursion (3.3); the checker retains them as rational
numbers.

## 4. Mod-$p^2$ multiplier and determinant

The denominator factors satisfy, exactly,



$$
(b)_L=\prod_{t=0}^m(p-(a+t))
 =(-1)^L(a)_L\prod_{t=0}^m\left(1-{p\over a+t}\right).            \tag{4.1}
$$



Therefore



$$
{ (a)_L\over(b)_L}
 =(-1)^L\prod_{t=0}^m\left(1-{p\over a+t}\right)^{-1}
 \equiv(-1)^L(1+p\mathcal H_{m,d})\pmod {p^2}.   \tag{4.2}
$$



Since



$$
A_c=(-1/c)^L{(a)_L\over(b)_L},                   \tag{4.3}
$$



equations (1.8)--(1.9) follow.  This calculation is over the localization
of $\mathbf Z$ at $p$; every denominator in (4.1)--(4.3) is a unit.

At $(p,m,d)=(23,2,5)$, the exact ratio is



$$
R={(9)_3\over(12)_3}={165\over364},\qquad
 R^2-1={-105271\over132496}.                      \tag{4.4}
$$



Here $-105271=-199\cdot23^2$, proving the stated first-Hasse-unit
counterexample without relying on a finite scan.

## 5. Rank of the augmented first-jet system

Write



$$
X=M_0(c),\quad Y=M_0(c^{-1}),\quad
 U=N_0(c),\quad V=N_0(c^{-1}).                    \tag{5.1}
$$



The two value equations modulo $p$, followed by the two jet equations,
have homogeneous matrix (1.12).  The first two rows satisfy



$$
R_2=cR_1,                                         \tag{5.2}
$$



because $L=m+1$.  Formula (1.11) gives the exact characteristic-zero
relation



$$
B_{c^{-1}}=c^{2L}B_c.                             \tag{5.3}
$$



Consequently the fourth row satisfies



$$
R_4=-cR_3+{cB_c\over A_c}R_1                    \tag{5.4}
$$



after reduction modulo $p$.  The first and third rows are independent:
the first has zero jet block, while the third has the nonzero row
$(c^{-L},-c^m)$ in that block.  Thus the rank is exactly two for every
actual row, proving (1.13).

The affine identities are



$$
E_{c^{-1}}=cE_c,\qquad
 F_{c^{-1}}=-cF_c+{cB_c\over A_c}E_c\pmod p.       \tag{5.5}
$$



They are verified directly by the exact endpoint recursion (3.3), and they
match the row relations (5.2), (5.4).  Therefore the endpoint terms do not
create a hidden compatibility condition.

The full mod-$p^2$ value equations are, from (1.3),



$$
\begin{aligned}
 A_cX+c^mY+E_c+p c^mV&\equiv0\pmod {p^2},\\
 c^{-m}X+A_{c^{-1}}Y+E_{c^{-1}}+p c^{-m}U
   &\equiv0\pmod {p^2}.                           \tag{5.6}
 \end{aligned}
$$



Although the value determinant has first digit $2\mathcal H_{m,d}$,
the new residues $U,V$ occur in exactly that next digit.  Equations
(5.4)--(5.5) show that adjoining their own mod-$p$ recurrences still
does not produce a second condition on $X$.

## 6. Denominator, endpoint, and scope audit

For $0\leq q,k\leq m$,



$$
0<a+q+k\leq4m+d<p,
 \qquad 0<b+q\leq4m+d+1<p.                       \tag{6.1}
$$



The reflected denominators $p-(a+k)$ lie in the same positive unit
range.  Their squares are units as well.  The beta-localization factorials
remain below $n=(p-1)/2$.  Constants $2,-2,-1/2$ are units.

The endpoint $(1+c)^L$ is retained in $M$'s affine recurrence.  Its
formal $a$-derivative is exactly zero in the jet recurrence; this is not
an omitted endpoint.  At $u=0$, the positive exponent makes the boundary
zero.

### PROVED

* mod-$p^2$ value reflection (1.3) and mod-$p$ jet reflection (1.4);
* the exact coupled recurrence (1.5)--(1.6), including endpoints;
* multiplier and determinant expansions (1.8)--(1.9);
* the all-row rank-two theorem (1.12)--(1.13) and affine compatibility;
* the exact $p=23$ counterexample to a universal first-Hasse unit.

### EXACT FINITE ONLY

* all bounded rank, zero, and joint-zero counts emitted by the checker.

### OPEN

* a second or higher jet that is genuinely independent of the reciprocal
  tower;
* all-prime or weighted control of $\mathcal H_{m,d}$;
* any independent obstruction for the actual Item-251 collision;
* any new divisibility exponent, rate, capacity reduction, or conclusion
  about $e+\pi$.

Accordingly,



$$
\boxed{\text{new unconditional linear-log rate}=0,\qquad
        \text{capacity reduction}=0.}                            \tag{6.2}
$$



