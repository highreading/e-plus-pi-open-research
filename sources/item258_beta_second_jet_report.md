> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 258 — the second beta jet and the mod-$p^3$ resonance

Checked: 2026-08-31 (Beijing time)

## 1. Scope and verdict

Retain the actual Route-1 phase



$$
p=6m+2d+1,\qquad d=r+4\geq5,\qquad
 L=m+1,\quad a=2m+d,\quad b=3m+d+1=a+L.          \tag{1.1}
$$



For a $p$-unit $c$, introduce the first three denominator moments



$$
\begin{aligned}
 M_q(c)&=\sum_{k=0}^m\binom mk{c^k\over a+q+k},\\
 N_q(c)&=\sum_{k=0}^m\binom mk{c^k\over(a+q+k)^2},\\
 P_q(c)&=\sum_{k=0}^m\binom mk{c^k\over(a+q+k)^3}.
 \end{aligned}                                                     \tag{1.2}
$$



The target remains $M_0(-2)=I_{m,d}$; by Item 255 it vanishes modulo
$p$ exactly when the universal half-binomial prefix $H_m$ vanishes.
Item 256 found rank two after adjoining $N$. This item retains $P$ and
the complete next digit.

> **PROVED — exact second-jet reflection.** Complementing the denominator
> gives
> 

$$
> \boxed{M_L(c)\equiv-c^m\{M_0(c^{-1})+pN_0(c^{-1})
>                  +p^2P_0(c^{-1})\}\pmod {p^3},}                 \tag{1.3}
>
$$


> 

$$
> \boxed{N_L(c)\equiv c^m\{N_0(c^{-1})+2pP_0(c^{-1})\}
>                  \pmod {p^2},}                                  \tag{1.4}
>
$$


> and
> 

$$
> \boxed{P_L(c)\equiv-c^mP_0(c^{-1})\pmod p.}                    \tag{1.5}
>
$$



> **PROVED — exact endpoint-retaining three-state transfer.** Besides the
> value and first-jet recurrences of Item 256,
> 

$$
> \boxed{(a+q)P_q(c)+c(b+q)P_{q+1}(c)=N_q(c)+cN_{q+1}(c).}        \tag{1.6}
>
$$


> Iteration has homogeneous part
> 

$$
> \boxed{
> \begin{pmatrix}A_c&0&0\\B_c&A_c&0\\C_c&B_c&A_c\end{pmatrix}.}   \tag{1.7}
>
$$


> The original value endpoint $(1+c)^L$ is retained. Its first and
> second formal $a$-derivatives are exactly zero; they are not omitted
> boundary terms.

Define



$$
\Delta_j=\sum_{q=0}^{L-1}
 \left({1\over(a+q)^j}-{1\over(b+q)^j}\right).                    \tag{1.8}
$$



> **PROVED — closed second-jet coefficients.**
> 

$$
> \boxed{B_c=-A_c\Delta_1,\qquad
> C_c={A_c\over2}(\Delta_1^2-\Delta_2),\qquad
> B_c^2-2A_cC_c=A_c^2\Delta_2.}                                  \tag{1.9}
>
$$



Put the moving terminal harmonic intervals



$$
\mathcal H_j=\sum_{t=0}^m{1\over(a+t)^j}.                        \tag{1.10}
$$



> **PROVED — mod-$p^3$ multiplier and second Hasse term.**
> 

$$
> \boxed{A_c\equiv c^{-L}\left\{1+p\mathcal H_1+
> {p^2\over2}(\mathcal H_2+\mathcal H_1^2)\right\}\pmod {p^3},}   \tag{1.11}
>
$$


> and hence
> 

$$
> \boxed{A_cA_{c^{-1}}-1\equiv
> 2p\mathcal H_1+p^2(\mathcal H_2+2\mathcal H_1^2)
> \pmod {p^3}.}                                                    \tag{1.12}
>
$$


> Thus the leading new value-determinant Hasse expression is
> $\mathcal H_2+2\mathcal H_1^2$.

> **PROVED — exact rank-three phase collapse.** On every actual phase row,
> 

$$
> b+q=p-(a+m-q),\qquad
> \Delta_2\equiv-2p\mathcal H_3\pmod {p^2}.                       \tag{1.13}
>
$$


> Consequently $B_c^2-2A_cC_c\equiv0\pmod p$. The reciprocal
> value/first-jet/second-jet matrix has
> 

$$
> \boxed{\operatorname {rank}_{\mathbf F_p}=3}                    \tag{1.14}
>
$$


> for every admissible row, not merely generically. The three independent
> rows solve successively for the reciprocal value and jets while leaving
> $M_0(c)$ arbitrary. The affine endpoint rows satisfy the same three
> dependencies.

> **PROVED, SHARPLY SCOPED NO-GO.** The reciprocal closure through
> mod $p^3$, including both denominator jets and every endpoint term,
> supplies no necessary congruence for $M_0(-2)=0$, for $H_m=0$, or
> for prescribing the affine value required by the Item-251 gate. This is
> a rank theorem about this three-moment ansatz, not a proof that every
> higher jet or every Route-1 method is impossible.

> **PROVED — both natural universal-unit shortcuts fail.**
> On $(p,r,s,m,d)=(89,19,8,7,23)$, the interval is $37,\ldots,44$ and
> $\mathcal H_1\equiv\mathcal H_2\equiv44\pmod {89}$, so
> $\mathcal H_2+2\mathcal H_1^2=44\cdot89\equiv0\pmod {89}$.
> On $(157,59,6,5,63)$, the interval is $73,\ldots,78$ and
> $\mathcal H_3\equiv0\pmod {157}$; the exact numerator of
> $B_c^2-2A_cC_c$ has $157$-adic valuation two. Thus neither the
> second determinant coefficient nor the divided curvature is an all-row
> unit.

> **OPEN / zero booking.** No all-prime resultant for simultaneous
> harmonic vanishing, no weighted zero theorem, and no Item-251 collision
> restriction follows. No rate or capacity is booked.

Every bounded count in the checker is **EXACT FINITE ONLY**.

## 2. Complementary-denominator reflection

Write $x_k=a+k$. Reversing $k$ at $q=L$ gives



$$
M_L(c)=\sum_{k=0}^m\binom mk{c^{m-k}\over p-x_k}.                \tag{2.1}
$$



All $x_k$ are $p$-units, and



$$
{1\over p-x}=-{1\over x}\left(1+{p\over x}+{p^2\over x^2}\right)
       \pmod {p^3},                                               \tag{2.2}
$$




$$
{1\over(p-x)^2}={1\over x^2}\left(1+{2p\over x}\right)
       \pmod {p^2},\qquad
 {1\over(p-x)^3}=-{1\over x^3}\pmod p.                            \tag{2.3}
$$



Substitution proves (1.3)–(1.5), including the alternating signs and the
coefficient $2$ in (1.4).

## 3. Exact contiguous recurrences and transfer

Integrating the derivative of
$u^{a+q}(1+cu)^{m+1}$ gives



$$
(a+q)M_q+c(b+q)M_{q+1}=(1+c)^L.                                \tag{3.1}
$$



With $N_q=-\partial_aM_q$ and
$P_q=\tfrac12\partial_a^2M_q$, differentiating (3.1) once and twice
gives



$$
\begin{aligned}
 (a+q)N_q+c(b+q)N_{q+1}&=M_q+cM_{q+1},\\
 (a+q)P_q+c(b+q)P_{q+1}&=N_q+cN_{q+1}.
 \end{aligned}                                                    \tag{3.2}
$$



The endpoint is independent of $a$, so its differentiated terms vanish
exactly. Solving one step, with $\alpha=a+q,\ \beta=b+q$, gives the
homogeneous matrix



$$
\begin{pmatrix}
 \lambda&0&0\\ \eta&\lambda&0\\ \theta&\eta&\lambda
 \end{pmatrix},\qquad
 \lambda=-{\alpha\over c\beta},\quad
 \eta={L\over c\beta^2},\quad
 \theta={L\over c\beta^3}.                                      \tag{3.3}
$$



The affine one-step vector is



$$
{ (1+c)^L\over c}
 \begin{pmatrix}\beta^{-1}\\\beta^{-2}\\\beta^{-3}\end{pmatrix}. \tag{3.4}
$$



Iterating proves (1.7). Alternatively, differentiating
$M_L=A_cM_0+E_c$ gives



$$
B_c=-A_c',\qquad C_c={A_c''\over2}.                              \tag{3.5}
$$



Since



$$
{A_c'\over A_c}=\Delta_1,\qquad
 \left({A_c'\over A_c}\right)'=-\Delta_2,                         \tag{3.6}
$$



equations (1.9) follow. This fixes all signs without interpolation or
guessed recurrences.

## 4. Hasse expansion and phase curvature

The exact complementary product is



$$
(b)_L=(-1)^L(a)_L\prod_{t=0}^m\left(1-{p\over a+t}\right).      \tag{4.1}
$$



Together with $A_c=(-1/c)^L(a)_L/(b)_L$, expansion of the reciprocal
product yields (1.11). Squaring the common scalar multiplier gives
(1.12). All calculations occur in the localization $\mathbf Z_{(p)}$.

For the second transfer curvature, reindexing the $b$-interval gives



$$
\sum_{q=0}^{m}{1\over(b+q)^2}
 =\sum_{t=0}^{m}{1\over(p-(a+t))^2}
 \equiv\mathcal H_2+2p\mathcal H_3\pmod {p^2}.                   \tag{4.2}
$$



Therefore



$$
\boxed{B_c^2-2A_cC_c=A_c^2\Delta_2
       \equiv-2pA_c^2\mathcal H_3\pmod {p^2}.}                   \tag{4.3}
$$



There are two distinct next-level quantities:

* $\mathcal H_2+2\mathcal H_1^2$ is the second coefficient of the
  value determinant;
* $-2A_c^2\mathcal H_3$ is the first divided coefficient of the
  second-jet row curvature.

Neither is a universal unit, by the exact rows stated above.

## 5. The augmented matrix and its exact phase rank

Let



$$
X=M_0(c),\ Y=M_0(c^{-1}),\ U=N_0(c),\ V=N_0(c^{-1}),\qquad
 W=P_0(c),\ Z=P_0(c^{-1}),\quad t=c^m.                            \tag{5.1}
$$



Put bars on transfer coefficients for $c^{-1}$. The homogeneous
mod-$p$ system is



$$
\mathcal K_c=
 \begin{pmatrix}
 A&t&0&0&0&0\\
 t^{-1}&\bar A&0&0&0&0\\
 B&0&A&-t&0&0\\
 0&\bar B&-t^{-1}&\bar A&0&0\\
 C&0&B&0&A&t\\
 0&\bar C&0&\bar B&t^{-1}&\bar A
 \end{pmatrix}.                                                   \tag{5.2}
$$



Exactly over $\mathbf Q$,



$$
\bar A=c^{2L}A,\qquad \bar B=c^{2L}B,\qquad \bar C=c^{2L}C.      \tag{5.3}
$$



Modulo $p$, $A=c^{-L}$, $\bar A=c^L$, and $L=m+1$. If $R_i$
denotes row $i$, then



$$
\begin{aligned}
 R_2&=cR_1,\\
 R_4&=-cR_3+{cB\over A}R_1,\\
 R_6&=cR_5-{cB\over A}R_3+{cC\over A}R_1.
 \end{aligned}                                                    \tag{5.4}
$$



The last identity uses $B^2-2AC=0\pmod p$, proved for every actual row
in (4.3). Rows $R_1,R_3,R_5$ are independent because their newest
two-column blocks have the unit coefficient $A$. Hence the rank is
exactly three.

Writing the affine iterate as



$$
\begin{pmatrix}M_L\\N_L\\P_L\end{pmatrix}
 =\begin{pmatrix}A&0&0\\B&A&0\\C&B&A\end{pmatrix}
  \begin{pmatrix}M_0\\N_0\\P_0\end{pmatrix}
  +\begin{pmatrix}E\\F\\G\end{pmatrix},                           \tag{5.5}
$$



the reciprocal endpoint terms obey



$$
\bar E=cE,\quad
 \bar F=-cF+{cB\over A}E,\quad
 \bar G=cG-{cB\over A}F+{cC\over A}E\pmod p.                     \tag{5.6}
$$



Thus (5.4) creates no hidden affine compatibility condition. The three
independent equations solve for $Y,V,Z$ successively for arbitrary
$X,U,W$. In particular, $X$ is unrestricted modulo $p$.

For clarity, the complete retained precisions are



$$
\begin{aligned}
 AX+tY+E+ptV+p^2tZ&=0&&\pmod {p^3},\\
 BX+AU-tV+F-2ptZ&=0&&\pmod {p^2},\\
 CX+BU+AW+tZ+G&=0&&\pmod p,
 \end{aligned}                                                    \tag{5.7}
$$



together with their reciprocal equations. These equations explicitly
show where the second determinant digit is absorbed by the two jet
levels; deleting those moments would create a spurious condition.

## 6. Exact unit witnesses

For $(p,r,s,m,d)=(89,19,8,7,23)$, $a=37$. Direct inversion of
$37,\ldots,44$ modulo $89$ gives



$$
\mathcal H_1\equiv44,\qquad \mathcal H_2\equiv44,\qquad
 \mathcal H_2+2\mathcal H_1^2=3916=44\cdot89.                    \tag{6.1}
$$



For $(157,59,6,5,63)$, $a=73$. The inverse cubes of
$73,\ldots,78$ modulo $157$ are



$$
92,45,108,118,116,149,                                           \tag{6.2}
$$



whose sum is $628=4\cdot157$. Hence $\mathcal H_3=0\pmod {157}$.
The exact rational checker also verifies $v_{157}(B^2-2AC)=2$. These
are exact counterexamples, not statistical inferences from the scan.

## 7. Denominator, boundary, and scope audit

For $0\leq q,k\leq m$,



$$
0<a+q+k\leq4m+d<p,\qquad
 0<b+q\leq4m+d+1<p.                                                \tag{7.1}
$$



At the terminal shift $q=L$,



$$
0<a+L+k\leq4m+d+1<p.                                             \tag{7.2}
$$



Also $0<p-(a+k)<p$. Powers one, two, and three of all these
denominators remain units. Constants $2,-2,-1/2$ are units. At
$u=0$, the exponent $a+q>0$ kills the boundary; at $u=1$, the
value endpoint is exactly $(1+c)^L$.

### PROVED

* the mod-$p^3$, mod-$p^2$, and mod-$p$ reflections (1.3)–(1.5);
* the exact second-jet recurrence and three-state transfer;
* the closed transfer identities (1.9);
* the multiplier/determinant expansion (1.11)–(1.12);
* the all-row phase curvature and rank-three theorem;
* affine endpoint compatibility and freedom of $M_0(c)$;
* exact counterexamples to both natural universal-unit claims.

### EXACT FINITE ONLY

At prime bound $601$, the portable checker has $2440$ actual rows:

* all $2440$ have augmented rank exactly three;
* $12$ have vanishing second determinant Hasse expression;
* $7$ have vanishing curvature lead $\mathcal H_3$;
* $6$ have $M_0(-2)=0$;
* no joint target/Hasse or target/curvature zero occurs in this finite
  range.

The last two absences are finite observations only and imply no density,
resultant, or all-prime theorem.

### OPEN

* a third or higher jet that is genuinely independent of this reciprocal
  translation tower;
* all-prime or weighted control of the moving 

$$
\mathcal H_1,\mathcal H_2,
  \mathcal H_3
$$

 intervals;
* any independent obstruction for the actual Item-251 collision;
* any new divisibility exponent, rate, capacity reduction, or conclusion
  about $e+\pi$.

Accordingly,



$$
\boxed{\text{new unconditional linear-log rate}=0,\qquad
        \text{capacity reduction}=0.}                            \tag{7.3}
$$


