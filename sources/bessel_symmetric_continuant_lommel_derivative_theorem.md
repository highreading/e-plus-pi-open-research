> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The symmetric Bessel continuant derivative: an exact Lommel-square formula

Checked: 2026-08-27 UTC.

## 1. Scope and verdict

For a finite list, write



$$
[a_1,\ldots,a_n]
 =a_n[a_1,\ldots,a_{n-1}]+[a_1,\ldots,a_{n-2}],
 \qquad []=1,
\tag{1}
$$



for its continuant.  Thus (1) uses a plus sign in the second term.  Put



$$
{\cal K}_h(X)=[X-4h,X-4h+4,\ldots,X+4h]
 \qquad(h\geq0).
\tag{2}
$$



For $0\leq j\leq h$, define the positive tail continuants



$$
P_{h,j}=[4(j+1),4(j+2),\ldots,4h],
 \qquad P_{h,h}=1,
\tag{3}
$$



and put $P_{h,h+1}=0$ when using recurrences.

This note proves the all-$h$ formula



$$
\boxed{
 {\cal K}'_h(0)=(-1)^h\left\{
 P_{h,0}^{2}+2\sum_{j=1}^h(-1)^jP_{h,j}^{2}
 \right\}.}
\tag{4}
$$



Every tail in (4) has the explicit factorial sum



$$
\boxed{
 P_{h,j}=\sum_{\ell=0}^{\lfloor(h-j)/2\rfloor}
 4^{h-j-2\ell}
 \frac{(h-j-\ell)!(h-\ell)!}
 {\ell!(h-j-2\ell)!(j+\ell)!}.}
\tag{5}
$$



The derivative itself also has the single terminating sum



$$
\boxed{
 {\cal K}'_h(0)=
 \sum_{a=0}^h(-16)^a(a!)^2
 \binom{h+a+1}{2a+1}.}
\tag{5a}
$$



Equivalently, as an identity of formal power series,



$$
\boxed{
 \sum_{h\geq0}{\cal K}'_h(0)z^h
 ={1\over(1-z)^2}
 \sum_{a\geq0}(a!)^2
 \left({-16z\over(1-z)^2}\right)^a.}
\tag{5b}
$$



Moreover,



$$
\boxed{
 {13\over15}P_{h,0}^{2}
 <(-1)^h{\cal K}'_h(0)
 <{17\over15}P_{h,0}^{2}.}
\tag{6}
$$



In particular, ${\cal K}'_h(0)$ is a nonzero integer of sign
$(-1)^h$.  Formula (4) is also a Cauchy--Binet expansion of one explicit
pentadiagonal determinant; see Theorem 2 below.

The arithmetic limitation is essential.  Integer nonvanishing does **not**
imply nonvanishing modulo a prime.  For example,



$$
{\cal K}'_2(0)=963=3^2\cdot107.
\tag{7}
$$



Consequently this theorem does not prove the missing Charlier congruence
from the frozen ordinary-lift analysis, and it does not prove
large-prime squarefreeness of the Bessel denominator.

## 2. The factorial formula for a tail

We first prove (5) without invoking a special-function identity.  For
integers $n\geq0$ and $\nu\geq1$, let



$$
D_n(\nu)=[4\nu,4(\nu+1),\ldots,4(\nu+n-1)].
\tag{8}
$$



The determinant model for a continuant is the tridiagonal matrix with the
listed diagonal, upper diagonal $1$, and lower diagonal $-1$.  Expanding
its determinant as matchings of a path, a matching with $\ell$ edges
removes $2\ell$ diagonal factors.  The elementary weighted-matching
identity



$$
\sum_{\substack{M\text{ a matching of }\{0,\ldots,n-1\}\\|M|=\ell}}
 \prod_{a\notin V(M)}(\nu+a)
 =\frac{(n-\ell)!}{\ell!(n-2\ell)!}
   (\nu+\ell)_{n-2\ell}
\tag{9}
$$



follows by induction on $n$: separate matchings according as the last
vertex is unmatched or is joined to its predecessor.  The two resulting
terms obey the same recurrence and initial values as the right side of
(9).  Here $(x)_m=x(x+1)\cdots(x+m-1)$, with $(x)_0=1$.
Restoring the factor $4$ at every unmatched vertex gives



$$
D_n(\nu)=
 \sum_{\ell=0}^{\lfloor n/2\rfloor}
 4^{n-2\ell}\frac{(n-\ell)!}{\ell!(n-2\ell)!}
 (\nu+\ell)_{n-2\ell}.
\tag{10}
$$



This is the terminating Lommel sum for the arithmetic continuant, derived
here directly.  Set $n=h-j$ and $\nu=j+1$.  Since



$$
(j+1+\ell)_{h-j-2\ell}
 ={(h-\ell)!\over(j+\ell)!},
\tag{11}
$$



equation (10) becomes exactly (5).

Because both sides of (10) are polynomials in $\nu$, that identity also
holds for an indeterminate $\nu$.  Taking $n=2h+1$ and
$\nu=X/4-h$ gives



$$
\begin{aligned}
 {\cal K}_h(X)
 =\sum_{\ell=0}^h&
 4^{2h+1-2\ell}
 { (2h+1-\ell)!\over
   \ell!(2h+1-2\ell)!}\\
 &\mathrel{}\times
 \left({X\over4}-h+\ell\right)_{2h+1-2\ell}.
\end{aligned}
\tag{11a}
$$



Put $a=h-\ell$.  The final rising factorial in (11a) is



$$
\prod_{u=-a}^{a}\left({X\over4}+u\right),
\qquad
 \left.{d\over dX}\right|_{X=0}
 \prod_{u=-a}^{a}\left({X\over4}+u\right)
 ={(-1)^a(a!)^2\over4}.
\tag{11b}
$$



Termwise differentiation of the finite sum (11a), followed by
$\ell=h-a$, therefore gives



$$
\begin{aligned}
 {\cal K}'_h(0)
 &=\sum_{a=0}^h
 (-1)^a16^a(a!)^2
 { (h+a+1)!\over(h-a)!(2a+1)!}\\
 &=\sum_{a=0}^h(-16)^a(a!)^2
 \binom{h+a+1}{2a+1},
\end{aligned}
\tag{11c}
$$



which proves (5a).  Finally, setting $h=a+n$, interchanging two formal
sums coefficientwise, and using the binomial series gives



$$
\begin{aligned}
 \sum_{h\geq0}{\cal K}'_h(0)z^h
 &=\sum_{a\geq0}(-16)^a(a!)^2z^a
   \sum_{n\geq0}\binom{n+2a+1}{2a+1}z^n\\
 &={1\over(1-z)^2}
 \sum_{a\geq0}(a!)^2
 \left({-16z\over(1-z)^2}\right)^a,
\end{aligned}
\tag{11d}
$$



proving (5b).  No analytic convergence is asserted or needed in (11d).

## 3. Cofactors give the alternating squares

For $-h\leq a\leq h$, let



$$
L_a=[-4h,-4h+4,\ldots,4(a-1)].
\tag{12}
$$



The list is empty when $a=-h$.  For $0\leq j\leq h$, reflection of
the negative half and the continuant recurrence give



$$
\boxed{L_j=(-1)^{h-j}P_{h,j}.}
\tag{13}
$$



Here is a complete induction.  At $j=0$, reflection and negation of all
$h$ entries give $L_0=(-1)^hP_{h,0}$.  At $j=1$, the terminal zero
in $L_1$ removes the last two entries in the continuant recurrence, so
$L_1=(-1)^{h-1}P_{h,1}$.  For $j\geq1$,



$$
L_{j+1}=4jL_j+L_{j-1},
 \qquad
 P_{h,j-1}=4jP_{h,j}+P_{h,j+1};
\tag{14}
$$



substitution of the two induction hypotheses into (14) proves (13).

Differentiate the determinant defining (2).  The diagonal cofactor at
position $j\geq0$ is the product of its left and right continuants, hence
by (13) it is



$$
(-1)^{h-j}P_{h,j}^{2}.
\tag{15}
$$



Reflection identifies the cofactor at $-j$ with the cofactor at $j$:
the two complementary lists are exchanged and the total number of retained
diagonal entries is $2h$, so the total sign from negation is positive.
There is one central cofactor and two of every cofactor with $j\geq1$.
Summing (15) proves (4).

The edge cases are literal.  For $h=0$, (4) says
${\cal K}'_0(0)=1$.  For $h=1$, it says



$$
{\cal K}'_1(0)=-\{4^2-2\}=-14.
\tag{16}
$$



## 4. A uniform sign and size bound

Prepending the first entry in (3) gives, for $0\leq j<h$,



$$
P_{h,j}=4(j+1)P_{h,j+1}+P_{h,j+2}.
\tag{17}
$$



All terms are nonnegative.  Thus



$$
P_{h,j}\geq4(j+1)P_{h,j+1}.
\tag{18}
$$



Equality occurs precisely at the terminal step $j=h-1$, where
$P_{h,h+1}=0$; it is strict at every earlier step.  Iteration yields



$$
0<P_{h,j}\leq{P_{h,0}\over4^j j!}
 \qquad(1\leq j\leq h).
\tag{19}
$$



Let the expression in braces in (4) be $S_h$.  Equations (19) and the
triangle inequality give



$$
\left|S_h-P_{h,0}^{2}\right|
 \leq2P_{h,0}^{2}
 \sum_{j=1}^h{1\over16^j(j!)^2}
 <2P_{h,0}^{2}\sum_{j=1}^{\infty}{1\over16^j}
 ={2\over15}P_{h,0}^{2}.
\tag{20}
$$



The strict inequality holds also when $h=1$, since $1/16<1/15$.
Equation (20) proves (6), including positivity of $S_h$.

## 5. The pentadiagonal determinant

**Theorem 2.**  For $h\geq1$, let $G_h=(g_{jk})_{1\leq j,k\leq h}$.
For $h=1$, put $G_1=(14)$.  For $h\geq2$, its nonzero entries are



$$
\begin{aligned}
 g_{11}&=13,\\
 g_{jj}&=16j^2-2 &&(2\leq j<h),\\
 g_{hh}&=16h^2-1,\\
 g_{j,j+1}&=8j+4,
 &g_{j+1,j}&=-(8j+4) &&(1\leq j<h),\\
 g_{j,j+2}&=g_{j+2,j}=1 &&(1\leq j<h-1).
\end{aligned}
\tag{21}
$$



Then



$$
\boxed{
 \det G_h=(-1)^h{\cal K}'_h(0)=S_h.}
\tag{22}
$$



To prove this, index rows and columns by $-h,\ldots,h$, and let $T_h$
have diagonal $4j$, upper diagonal $1$, and lower diagonal $-1$.
Then



$$
{\cal K}_h(X)=\det(XI+T_h).
\tag{23}
$$



Reflection anti-commutes with $T_h$.  In the even basis



$$
e_0=\delta_0,\qquad e_j=\delta_j+\delta_{-j},
\tag{24}
$$



and odd basis



$$
o_j=\delta_j-\delta_{-j},
\tag{25}
$$



the matrix in (23) has block form



$$
\begin{pmatrix}XI_{h+1}&A\\ B&XI_h\end{pmatrix}.
\tag{26}
$$



More explicitly, with rows of $A$ indexed by $0\leq a\leq h$, its
columns by $1\leq k\leq h$, rows of $B$ by $1\leq j\leq h$, and
columns by $0\leq b\leq h$, the nonzero entries are



$$
\begin{aligned}
 A_{0,1}&=2,
 &A_{j,j}&=4j,
 &A_{j,j+1}&=1,
 &A_{j,j-1}&=-1,\\
 B_{j,j-1}&=-1,
 &B_{j,j}&=4j,
 &B_{j,j+1}&=1,
\end{aligned}
\tag{26a}
$$



whenever the displayed indices lie in their stated ranges.  Direct
multiplication of (26a) gives $BA=G_h$, including both exceptional
boundary diagonal entries in (21).  The Schur determinant identity, first for
indeterminate nonzero $X$ and then as a polynomial identity, gives



$$
{\cal K}_h(X)=X\det(X^2I_h-G_h).
\tag{27}
$$



Taking the coefficient of $X$ proves (22).  Cauchy--Binet applied to
$BA$ gives exactly the central term and the paired tail terms in (4).
More explicitly, the product of maximal minors obtained by omitting even
index $0$ is $P_{h,0}^2$, while omission of even index $j\geq1$
gives $2(-1)^jP_{h,j}^2$.  These minor evaluations follow from the same
triangular continuant recurrence used in (13)--(14); the replay also
checks every individual maximal-minor product through its stated cutoff.

## 6. Exact translation to the remaining Charlier condition

Retain the notation of the frozen ordinary-lift analysis.  Thus $p\geq5$
is prime,



$$
1\leq r<{p-1\over2},\qquad
 s=p-1-r,\qquad h={p-3\over2}-r,
\tag{28}
$$



and $p\mid q_r$.  Let ${\mathfrak L}_n$ and
${\mathfrak A}_{p,r}$ be its Charlier lift derivative and positive
partial-injection count.  The already proved transfer and Charlier
identities, combined with (4) and (22), give



$$
\boxed{
 {\mathfrak L}_s-{\mathfrak L}_r
 \equiv(-1)^{r+h+1}2q_{r-1}\det G_h\pmod p.}
\tag{29}
$$



Since $q_{r-1}$ is a unit modulo $p$, the root is ordinary precisely
when



$$
p\nmid\det G_h.
\tag{30}
$$



The distinct base-square condition remains



$$
{\mathfrak A_{p,r}\over p}
 \equiv{\mathfrak L}_r\pmod p.
\tag{31}
$$



Equations (29)--(31) are an exact, explicit reformulation, but there is no
deduction from (30) to the negation of (31) in this note.  The real
inequalities (6) do not survive reduction modulo $p$, and (7) shows that
even a prime much larger than $2h+1$ can divide the nonzero determinant.
For the tied value $p=107,h=2,r=50$, one has 

$$
q_{50}\equiv26\pmod
{107}
$$

, so this particular determinant zero is not a Bessel root; that is
only an exact diagnostic, not an all-prime argument.

Accordingly, this package proves the requested all-parameter
continuant/Lommel formula and sign theorem.  It does **not** prove (31)
impossible under (30), does **not** prove $p^2\nmid q_r$, and has no
direct implication for $e+\pi$.

## 7. Replay and frozen dependency

The transfer and Charlier identities used only in Section 6 are proved in

    sources/bessel_ordinary_symmetric_transfer_base_carry_barrier.md

with frozen SHA-256

    769c886c1c8e5a6e406bd2018c71846e2831170359c2e97b43939e200a108c6e.

The deterministic replay

    scripts/bessel_symmetric_continuant_lommel_derivative_certificate.py

independently checks the factorial formula, the cofactor-square identity,
the strict rational bounds, the block matrices, the pentadiagonal
determinants, the edge cases, and the diagnostic in (7) and Section 6.
Finite replay cutoffs are regression checks only; every theorem above is
proved for all $h$.
