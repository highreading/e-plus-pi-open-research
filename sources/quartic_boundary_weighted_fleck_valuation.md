> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The boundary quartic weighted-Fleck valuation

Checked: 2026-08-27 UTC.

## 1. Statement and scope

For $m\ge1$, define the rational number



$$
S_m=\sum_{h=0}^{m-1}\binom{4m}{4h+1}
\frac{(2m-2h)!(2m+2h)!}
{(m-h)!(m+h)!(2m)!}.
\tag{1}
$$



This is the terminating sum which occurs in the first odd Hermite
coordinate of the boundary quartic kernel:



$$
b_{4m,\,2m+1}=-\frac{S_m}{4^{2m}}.
\tag{2}
$$



The earlier fixed-slope note proved (1)--(2) and checked the following
valuation through $m=30$, but left its all-$m$ proof open.

**Theorem 1.1.** For every integer $m\ge1$,



$$
\boxed{v_2(S_m)=m+s_2(m)+v_2(m)+1.}
\tag{3}
$$



Consequently,



$$
\boxed{
v_2\!\left(\operatorname {den} b_{4m,\,2m+1}\right)
=3m-s_2(m)-v_2(m)-1.}
\tag{4}
$$



The proof has two independent finite-difference components.  An odd
hypergeometric weight has exact Newton-coefficient valuation $j$.  A
four-state binomial transfer matrix supplies the complementary
residue-class valuation $m-j$.  Their unique top-order intersection
proves (3), with no unproved congruence or asymptotic input.

Equation (3) settles only the weighted-Fleck congruence isolated in the
earlier note.  It does not control the other two odd coordinates, the odd
part of the rational endpoint, or the final determinant gcd.  In
particular, it does not classify $e+\pi$.

## 2. Removing the factorial and the visible factor $4m$

Write



$$
(2r-1)!!=1\cdot3\cdots(2r-1),\qquad (-1)!!=1.
$$



Since



$$
\frac{(2r)!}{r!}=2^r(2r-1)!!,
$$



equation (1) becomes



$$
S_m=\frac{2^{2m}}{(2m)!}A_m,
\tag{5}
$$



where



$$
A_m=\sum_{h=0}^{m-1}\binom{4m}{4h+1}
(2m-2h-1)!!(2m+2h-1)!!.
\tag{6}
$$



For $0\le h\le m-1$, the odd number $4h+1$ occurs among the factors
of $(2m+2h-1)!!$, because



$$
4h+1\le2m+2h-1.
$$



Thus



$$
w_h=
\frac{(2m-2h-1)!!(2m+2h-1)!!}{4h+1}
\tag{7}
$$



is an odd integer.  The elementary identity



$$
\binom{4m}{4h+1}
=\frac{4m}{4h+1}\binom{4m-1}{4h}
$$



gives



$$
A_m=4m\,C_m,\qquad
C_m=\sum_{h=0}^{m-1}\binom{4m-1}{4h}w_h.
\tag{8}
$$



It remains to prove



$$
v_2(C_m)=m-1.
\tag{9}
$$



## 3. Exact Newton valuations of the odd weight

Let $\Delta f_h=f_{h+1}-f_h$.

**Lemma 3.1.** For $0\le j\le m-1$,



$$
\boxed{v_2(\Delta^j w_0)=j.}
\tag{10}
$$



**Proof.** Since $w_0$ is odd, it is enough to prove (10) for
$f_h=w_h/w_0$.  Direct cancellation in (7) gives, for
$0\le h\le m-2$,



$$
\frac{f_{h+1}}{f_h}
=\frac{(2m+2h+1)(4h+1)}
{(2m-2h-1)(4h+5)}
=1+2a_h,
\tag{11}
$$



where



$$
a_h=
\frac{8h^2+10h-4m+3}
{(2m-2h-1)(4h+5)}.
\tag{12}
$$



Both the numerator and denominator in (12) are odd, so $a_h$ is a
$2$-adic unit.  A second direct subtraction yields



$$
a_{h+1}-a_h=4B_m(2h),
\tag{13}
$$



where



$$
B_m(Y)=
\frac{4Y^2m-2Y^2+20Ym-8Y+8m^2+17m-6}
{(2Y+5)(2Y+9)(Y-2m+1)(Y-2m+3)}.
\tag{14}
$$



Every denominator in (14) is odd when $Y=2h$.  More generally, if
$G(Y)=P(Y)/Q(Y)$ has $2$-integral polynomial coefficients and
$Q(2h)$ is odd on the integer range under consideration, then



$$
G(2h+2)-G(2h)
$$



is twice another rational function with $2$-integral numerator and odd
denominator.  This follows after putting the two fractions over a common
denominator: the numerator



$$
P(Y+2)Q(Y)-P(Y)Q(Y+2)
$$



is coefficientwise divisible by $2$.  Iteration therefore gives



$$
\Delta^rG(2h)\in2^r\mathbb Z_{(2)}.
\tag{15}
$$



Applying (15) to (13)--(14) proves



$$
\Delta^r a_h\in2^{r+1}\mathbb Z_{(2)}
\qquad(r\ge1).
\tag{16}
$$



Equation (11) is



$$
\Delta f_h=2a_hf_h.
\tag{17}
$$



We now induct on $j$, simultaneously for every admissible $h$.
For $j=0$, $f_h$ is odd.  Suppose
$v_2(\Delta^j f_h)=j$.  The discrete Leibniz rule gives



$$
\Delta^j(a_hf_h)
=\sum_{r=0}^j\binom jr
(\Delta^r a_h)(\Delta^{j-r}f_{h+r}).
\tag{18}
$$



The term $r=0$ has valuation exactly $j$.  By (16) and the induction
hypothesis, every term with $r\ge1$ has valuation at least



$$
(r+1)+(j-r)=j+1.
$$



Hence the right side of (18) has valuation exactly $j$.  Applying
$\Delta^j$ to (17) proves



$$
v_2(\Delta^{j+1}f_h)=j+1.
$$



This completes the induction and proves (10). $\square$

## 4. A four-state transfer congruence

Define



$$
T_{m,j}=
\sum_{h=j}^{m-1}\binom{4m-1}{4h}\binom hj
\qquad(0\le j\le m-1).
\tag{19}
$$



**Lemma 4.1.** One has



$$
\boxed{
v_2(T_{m,j})\ge m-j\quad(0\le j\le m-2),
\qquad T_{m,m-1}\equiv1\pmod2.}
\tag{20}
$$



**Proof.** Introduce four residue polynomials by



$$
(1+z)^{4m-1}
=\sum_{r=0}^3z^rR_r^{(m)}(z^4).
\tag{21}
$$



Thus



$$
R_0^{(m)}(y)
=\sum_{h=0}^{m-1}\binom{4m-1}{4h}y^h.
\tag{22}
$$



Multiplication by



$$
(1+z)^4=1+4z+6z^2+4z^3+z^4
$$



gives



$$
\begin{pmatrix}
R_0^{(m+1)}\\R_1^{(m+1)}\\R_2^{(m+1)}\\R_3^{(m+1)}
\end{pmatrix}
=M(y)
\begin{pmatrix}
R_0^{(m)}\\R_1^{(m)}\\R_2^{(m)}\\R_3^{(m)}
\end{pmatrix},
\tag{23}
$$



with



$$
M(y)=
\begin{pmatrix}
1+y&4y&6y&4y\\
4&1+y&4y&6y\\
6&4&1+y&4y\\
4&6&4&1+y
\end{pmatrix}.
\tag{24}
$$



Set $y=1+2x$.  Every entry of $M(1+2x)$ is divisible by $2$.
Modulo $2$,



$$
\frac12M(1+2x)
\equiv
\begin{pmatrix}
1+x&0&1&0\\
0&1+x&0&1\\
1&0&1+x&0\\
0&1&0&1+x
\end{pmatrix}
=(1+x)I+P,
\tag{25}
$$



where $P$ swaps residues $0,2$ and $1,3$.  At $m=1$,



$$
(R_0^{(1)},R_1^{(1)},R_2^{(1)},R_3^{(1)})
=(1,3,3,1),
$$



which is the all-ones vector modulo $2$.  Since $P\mathbf1=\mathbf1$,
equation (25) sends $\mathbf1$ to $x\mathbf1$.  Iterating (23) gives
the polynomial congruence



$$
\boxed{
R_0^{(m)}(1+2x)
\equiv2^{m-1}x^{m-1}\pmod{2^m\mathbb Z[x]}.}
\tag{26}
$$



On the other hand, the binomial theorem and (19) give



$$
R_0^{(m)}(1+2x)
=\sum_{j=0}^{m-1}2^jT_{m,j}x^j.
\tag{27}
$$



Comparison of coefficients in (26)--(27) proves (20). $\square$

## 5. Completion of the valuation

Newton interpolation on the $m$ values $w_0,\ldots,w_{m-1}$ is



$$
w_h=\sum_{j=0}^h(\Delta^jw_0)\binom hj.
\tag{28}
$$



Substitution into (8), followed by reversal of the two finite sums, gives



$$
C_m=\sum_{j=0}^{m-1}(\Delta^jw_0)T_{m,j}.
\tag{29}
$$



For $j\le m-2$, Lemmas 3.1 and 4.1 imply



$$
v_2\bigl((\Delta^jw_0)T_{m,j}\bigr)\ge j+(m-j)=m.
\tag{30}
$$



The unique final term has valuation



$$
v_2\bigl((\Delta^{m-1}w_0)T_{m,m-1}\bigr)=m-1.
\tag{31}
$$



It cannot be cancelled by the terms in (30).  Hence



$$
v_2(C_m)=m-1,
$$



which is (9).  Equations (8), (5), and Legendre's formula now give



$$
v_2(A_m)=2+v_2(m)+(m-1)
=m+v_2(m)+1,
\tag{32}
$$



and



$$
\begin{aligned}
v_2(S_m)
&=2m-v_2((2m)!)+v_2(A_m)\\
&=s_2(2m)+m+v_2(m)+1\\
&=m+s_2(m)+v_2(m)+1.
\end{aligned}
\tag{33}
$$



This proves Theorem 1.1.  Finally, (2) and (33) give (4).

## 6. Certificate boundary

The companion certificate checks, in exact integer arithmetic:

1. the identities (5), (8), (11), and (13);
2. the transfer matrix (23) and congruence (26);
3. the exact Newton valuations (10) and the bounds (20);
4. the resulting valuation (3) through a configurable finite range.

Those checks guard against transcription, residue-carry, and endpoint
errors.  The all-$m$ proof is the argument above, not extrapolation from
the finite records.
