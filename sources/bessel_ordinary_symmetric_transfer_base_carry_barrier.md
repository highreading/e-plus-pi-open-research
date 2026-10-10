> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Ordinary Bessel lifts: symmetric transfer separation and the unavoidable base carry

Checked: 2026-08-27 UTC.

## 1. Verdict

Let



$$
q_0=q_1=1,\qquad q_n=(4n-2)q_{n-1}+q_{n-2}.
\tag{1}
$$



Fix a prime $p\geq5$, let



$$
0\leq r\leq {p-1\over2},\qquad s=p-1-r,
\tag{2}
$$



and suppose $p\mid q_r$.  Write



$$
c={q_r\over p}\pmod p,\qquad
 \delta={q_r-q_s\over p}\pmod p.
\tag{3}
$$



Because $q_0=1$, the root hypothesis forces $r\geq1$, so every
occurrence of $q_{r-1}$ below is defined.

The second expression agrees with the ordinary index slope used in the
four-point theorem.

This note proves two exact separations.

First, outside the central point, put



$$
h={p-3\over2}-r\geq0,
\tag{4}
$$



and let ${\cal K}_h(X)$ be the continuant of the odd symmetric list



$$
X-4h,X-4h+4,\ldots,X-4,X,X+4,\ldots,X+4h.
\tag{5}
$$



Then



$$
\boxed{\delta\equiv-2{\cal K}'_h(0)q_{r-1}\pmod p.}
\tag{6}
$$



Thus the ordinary slope is controlled by a symmetric-continuant derivative
factor and is independent of the base quotient $c$ in the
reflection-transfer formula.  Since $q_{r-1}$ is a unit at a root,



$$
\delta\ne0\quad\Longleftrightarrow\quad
 p\nmid {\cal K}'_h(0).
\tag{7}
$$



This does **not** prove that $c\ne0$.  It identifies the additional
common-divisor theorem that would be needed to turn ordinary simplicity
into base squarefreeness.

Second, let $Z_0\in\{0,-1,1,-2\}$ be an ordinary endpoint surviving to
the square threshold.  The carried digit from the frozen first-three-layer
formula has the form



$$
\boxed{{F_{p,r}(Z_0)\over p^2}\equiv d+\Psi_{p,r}(Z_0)\pmod p,}
\tag{8}
$$



where



$$
{q_r\over p}=c+pd\pmod {p^2}.
\tag{9}
$$



The coefficient of the next base digit $d$ in (8) is exactly one.  An
explicit expression for $\Psi$ is given in (43).  Consequently a
resultant or character sum formed only from the raw finite-field layers
cannot exclude the cube threshold: the next digit of the fixed integer
$q_r$ remains as an additive datum.

These are all-parameter theorems and a sharply scoped barrier.  They do not
prove that an ordinary base square or an ordinary cube exists for the
original initial values in (1), nor do they prove that one is impossible.
In particular, no valuation bound and no implication for $e+\pi$ is
claimed.

## 2. Continuants and the reflection transfer

For a list $t_1,\ldots,t_j$, define the plus continuant by



$$
[\,]=1,\qquad [t_1]=t_1,\qquad
 [t_1,\ldots,t_j]=t_j[t_1,\ldots,t_{j-1}]
                    +[t_1,\ldots,t_{j-2}].
\tag{10}
$$



It is invariant under reversal.  Put



$$
C(t)=\begin{pmatrix}t&1\\1&0\end{pmatrix}.
\tag{11}
$$



The transfer from $(q_r,q_{r-1})^{\mathsf T}$ to
$(q_s,q_{s-1})^{\mathsf T}$ is



$$
M_{p,r}=C(4s-2)C(4s-6)\cdots C(4r+2).
\tag{12}
$$



### Theorem 1 (exact mod-$p$ reflection transfer)

For every $p,r$ in (2) with $r<s$,



$$
\boxed{
 M_{p,r}\equiv
 \begin{pmatrix}1&0\\4r+2&1\end{pmatrix}\pmod p.}
\tag{13}
$$



To prove it, write $p=2m+1$ and $r=m-h-1$.  Modulo $p$, the
coefficients in (12), in product order, are



$$
4h,4h-4,\ldots,4,0,-4,-8,\ldots,-4h-4.
\tag{14}
$$



From this point through (20), all transfer matrices and the matrix $V$
are regarded in $M_2(\mathbb F_p)$; equation (19) is the corresponding
exact two-by-two identity over $\mathbb F_p$.

Let



$$
D=\operatorname {diag}(1,-1),\qquad
 J=C(0),\qquad S=JD=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\tag{15}
$$



and



$$
V=C(4)C(8)\cdots C(4h),
\tag{16}
$$



with $V=I$ when $h=0$.  Since



$$
C(-t)=-DC(t)D,
\tag{17}
$$



equation (14) gives, modulo $p$,



$$
M_{p,r}\equiv(-1)^{h+1}V^{\mathsf T}JDVC(4h+4)D\pmod p.
\tag{18}
$$



Every $C(t)$ has determinant $-1$, and every two-by-two matrix obeys



$$
V^{\mathsf T}SV=(\det V)S=(-1)^hS.
\tag{19}
$$



Therefore



$$
M_{p,r}\equiv-SC(4h+4)D
 =\begin{pmatrix}1&0\\-4h-4&1\end{pmatrix}\pmod p.
\tag{20}
$$



Finally $-4h-4\equiv4r+2\pmod p$, proving (13).

## 3. The symmetric derivative formula for the slope

Write



$$
M_{p,r}=\begin{pmatrix}A&B\\C&D_0\end{pmatrix}.
\tag{21}
$$



The upper-right entry is the continuant of the interior coefficient list:



$$
B=[4(r+2)-2,4(r+3)-2,\ldots,4s-2].
\tag{22}
$$



The indices in (22) run from $m-h+1$ to $m+h+1$.  Hence, as an exact
integer identity,



$$
\boxed{B={\cal K}_h(2p).}
\tag{23}
$$



The list defining ${\cal K}_h(-X)$ is the reversed list defining
${\cal K}_h(X)$, with all $2h+1$ entries negated.  Every continuant
monomial has degree congruent to the list length modulo two.  Reversal
invariance therefore gives



$$
{\cal K}_h(-X)=-{\cal K}_h(X).
\tag{24}
$$



Consequently there is a polynomial $R_h\in\mathbb Z[X]$ such that



$$
{\cal K}_h(X)=X{\cal K}'_h(0)+X^3R_h(X^2),
\tag{25}
$$



and (23) gives



$$
\boxed{{B\over p}\equiv2{\cal K}'_h(0)\pmod p.}
\tag{26}
$$



Now assume $p\mid q_r$.  The first row of (21) says



$$
q_s=Aq_r+Bq_{r-1}.
\tag{27}
$$



Equation (13) gives $A\equiv1\pmod p$, so



$$
{q_s-q_r\over p}
 \equiv {B\over p}q_{r-1}\pmod p.
\tag{28}
$$



Adjacent terms are coprime, because the recurrence run backwards preserves
their gcd and $\gcd(q_1,q_0)=1$.  Thus $q_{r-1}$ is a unit modulo $p$.
Equations (3), (26), and (28) prove (6)--(7).

The central case $r=s=(p-1)/2$ has no positive-length reflection
transfer and is already known to have $\delta=0$.  Theorem 1 and (6) are
deliberately stated only for $r<s$.

## 4. A positive Charlier lift, and the residual Wieferich datum

Define the monic Charlier-type polynomial



$$
{\mathfrak F}_n(a)=\sum_{j=0}^n\binom nj(a)_{\underline j},
\qquad
 (a)_{\underline j}=a(a-1)\cdots(a-j+1).
\tag{29}
$$



Its exponential generating function is



$$
\sum_{n\geq0}{\mathfrak F}_n(a){z^n\over n!}
 =e^z(1+z)^a.
\tag{30}
$$



The terminating Bessel formula and a change of index give



$$
\boxed{{\mathfrak F}_r(-r-1)=(-1)^rq_r.}
\tag{31}
$$



At the positive shifted argument $s=p-1-r$, put



$$
{\mathfrak A}_{p,r}={\mathfrak F}_r(s)
 =\sum_{j=0}^r j!\binom rj\binom sj.
\tag{32}
$$



This is the number of partial injections between sets of sizes $r,s$,
and the displayed sum proves the exact symmetry



$$
{\mathfrak A}_{p,r}={\mathfrak F}_s(r).
\tag{33}
$$



Multiplication of (30) by $(1+z)^p$ proves the exact connection formula



$$
{\mathfrak F}_n(a+p)
 =\sum_{j=0}^n\binom pj(n)_{\underline j}
 {\mathfrak F}_{n-j}(a).
\tag{34}
$$



For $1\leq j<p$,



$$
\binom pj\equiv p{(-1)^{j-1}\over j}\pmod {p^2}.
\tag{35}
$$



Define the integer



$$
{\mathfrak L}_n=
 \sum_{j=1}^n(-1)^{j-1}{(n)_{\underline j}\over j}
 {\mathfrak F}_{n-j}(-n-1)
 ={\mathfrak F}'_n(-n-1).
\tag{36}
$$



The quotient $(n)_{\underline j}/j$ is integral because a product of
$j$ consecutive integers is divisible by $j$.  Applying (34)--(35)
first with $n=r$ and then, using (33), with $n=s$, proves



$$
\boxed{
 {\mathfrak A}_{p,r}\equiv
 (-1)^rq_r+p{\mathfrak L}_r
 \equiv(-1)^rq_s+p{\mathfrak L}_s
 \pmod {p^2}.}
\tag{37}
$$



Here $r,s$ have the same parity.  Conditional on $p\mid q_r$, (37)
gives two exact reductions:



$$
\boxed{
 \delta\equiv(-1)^r({\mathfrak L}_s-{\mathfrak L}_r)\pmod p,}
\tag{38}
$$



and



$$
\boxed{
 p^2\mid q_r
 \quad\Longleftrightarrow\quad
 {{\mathfrak A}_{p,r}\over p}\equiv{\mathfrak L}_r\pmod p.}
\tag{39}
$$



Thus ordinary simplicity says that the two Charlier lift derivatives in
(38) differ.  The base square asks whether the positive partial-injection
quotient in (39) equals one of them.  Equation (38) alone does not decide
(39); the missing congruence is a genuine extra, Wieferich-type digit.

## 5. The carried digit is affine in the next base digit

We now use the notation and the proved Wilson-carry formula from the frozen
dependency in Section 8.  Let



$$
\widehat P=A_1^\sharp+B_0^\sharp\in\mathbb Z_{(p)},
 \qquad \widehat P\equiv\delta\pmod p,
\tag{40}
$$



and let $R_r\in\mathbb F_p$ and
${\cal C}_{p,r,2}(Z)\in\mathbb F_p[Z]$ be the explicit Wilson correction
and raw second layer there.  Choose representatives and define



$$
{q_r\over p}=c+pd\pmod {p^2},\qquad
 \widehat P=\delta+p\rho\pmod {p^2}.
\tag{41}
$$



Suppose $Z_0\in\{0,-1,1,-2\}$ satisfies the square-threshold condition



$$
c+Z_0\delta\equiv0\pmod p,
\tag{42}
$$



and put $\lambda_{Z_0}=(c+Z_0\delta)/p$ in $\mathbb Z_{(p)}/p$, using
the same chosen least nonnegative representatives for $c,\delta$.
Substitution of (41) into the frozen
carry formula gives



$$
\boxed{
 \begin{aligned}
 {F_{p,r}(Z_0)\over p^2}
 &\equiv d+\Psi_{p,r}(Z_0)\pmod p,\\
 \Psi_{p,r}(Z_0)
 &=\lambda_{Z_0}+Z_0\rho
   +Z_0(Z_0+1)(c+R_r)
   +{\cal C}_{p,r,2}(Z_0).
 \end{aligned}}
\tag{43}
$$



Indeed, the numerator before the final division by $p$ is



$$
{q_r\over p}+Z_0\widehat P+Z_0(Z_0+1)q_r,
\tag{44}
$$



which becomes



$$
c+Z_0\delta+p\{d+Z_0\rho+Z_0(Z_0+1)c\}
 \pmod {p^2}.
\tag{45}
$$



The remaining Wilson and raw-layer terms give (43).  Changing the chosen
representatives of $c$ or $\delta$ changes $d,\rho,\lambda$ in
compensating ways, so the total in (43) is intrinsic.

At $Z_0=0$, condition (42) is $c=0$ and (43) reduces to



$$
{F_{p,r}(0)\over p^2}\equiv d\pmod p,
\tag{46}
$$



as it must.  At every nonzero endpoint the same digit $d$ remains with
coefficient one.  Equivalently, the resultant of the first affine digit
$c+\delta Z$ and the carried second digit is affine in $d$, with unit
leading coefficient after the ordinary specialization.  No identity among
the raw layers alone can remove this term.

## 6. Exact recurrence countermodels delimit the conclusion

Let



$$
u_0=1,\quad u_1=3,\qquad
 u_n=(4n-2)u_{n-1}+u_{n-2}.
\tag{47}
$$



The discrete Wronskian is



$$
u_nq_{n-1}-u_{n-1}q_n=2(-1)^{n-1}.
\tag{48}
$$



Hence $u_n$ is a unit modulo every odd prime dividing $q_n$.

For any integer $a$,



$$
\widetilde q_j=q_j+p^2a u_j
\tag{49}
$$



satisfies the **same exact recurrence** as (1) and agrees with $q_j$
modulo $p^2$ at every index.  If $p^2\mid q_n$, then



$$
{\widetilde q_n\over p^2}
 \equiv {q_n\over p^2}+a u_n\pmod p.
\tag{50}
$$



Since $u_n$ is a unit, a unique $a\pmod p$ makes the right side zero.
Therefore the recurrence and the complete sequence modulo $p^2$, by
themselves, cannot exclude a cube at the exceptional endpoint.  The exact
initial normalization—or an equivalent next-digit theorem for the special
factorial sum—is indispensable.

For a concrete exact witness, take the genuine square



$$
p=13,\qquad n=8,qquad
 q_8=312129649,qquad u_8=848456353.
\tag{51}
$$



Here $q_8/13^2\equiv11$ and $u_8\equiv4\pmod {13}$.  Choosing
$a=7$ in (49) gives



$$
\widetilde q_8
 =q_8+13^2\cdot7u_8
 =1004035995248
 =13^3\cdot457003184.
\tag{52}
$$



There is an equally explicit warning for the base square.  At
$(p,r)=(11,4)$, the original data are



$$
q_4=1001,\qquad u_4=2721,qquad c=3,qquad\delta=1
 \quad\hbox{in }\mathbb F_{11}.
\tag{53}
$$



The solution



$$
\widetilde q_j=q_j+22u_j
\tag{54}
$$



obeys the same recurrence, and



$$
\widetilde q_4=60863=11^2\cdot503,
\qquad
 {-\widetilde q_{15}-\widetilde q_4\over11}\equiv7\pmod {11}.
\tag{55}
$$



Thus an ordinary base square is fully compatible with the recurrence law
and its nonzero index slope once the exact initial pair is allowed to vary
inside its fixed residue class modulo $p$.  This is not a counterexample
for (1): (54) changes its integer initial values.  It proves only that a
successful exclusion must use those exact initial values through the
special factorial/Charlier quotient, not recurrence simplicity alone.

## 7. What remains open

The first requested positive statement would require an all-prime theorem
excluding



$$
{{\mathfrak A}_{p,r}\over p}\equiv{\mathfrak L}_r\pmod p
\quad\hbox{when}\quad
 {\mathfrak L}_s\ne{\mathfrak L}_r\pmod p.
\tag{56}
$$



Neither the symmetric transfer (6) nor the Charlier connection formula
(37) supplies such a theorem.

For the second gap, (43) shows exactly what a noncancellation theorem must
control: the next base digit $d$, together with the explicit Wilson and
raw-layer expression $\Psi$.  A resultant in $Z$ that omits $d$
cannot prove nonvanishing.  A genuine advance would need a new congruence
for $q_r\bmod p^3$, or a global identity coupling that digit to the
finite-field harmonic blocks.

## 8. Replay and frozen dependency

The carried formula used in Section 5 is proved in

    sources/bessel_ordinary_first_three_layer_wilson_carry.md

with frozen SHA-256

    af171d428ac26019c3d98af3cd46a72cfa64db5a305857f369b05a6cfd5fa44f.

The companion certificate

    scripts/bessel_ordinary_symmetric_transfer_base_carry_certificate.py

independently checks the exact transfer identity (23), the matrix formula
(13), the slope formula (6), the Charlier identities (31)--(39), the affine
carry decomposition (43) at both frozen square witnesses, and the exact
countermodels (52), (55).  All finite grids are regression checks for the
symbolic proofs above, not extrapolations.
