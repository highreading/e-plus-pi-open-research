> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 292 — the beta least lift is an inhomogeneous $e$-Padé determinant

Checked: 2026-08-31 (Beijing time)

## 1. Verdict

Retain



$$
q_0=q_1=1,\qquad
q_n=(4n-2)q_{n-1}+q_{n-2}\quad(n\ge2),                 \tag{1.1}
$$



and, for $n\ge2$,



$$
\rho_n=\min_{k\in\mathbb Z}|q_{n-1}^2-kq_n|.           \tag{1.2}
$$



Item 290 reduced the full-target degree-one problem to (1.2).
This item uses the exact reverse-Bessel seed, rather than a generic
continuant estimate.

Define its companion



$$
p_0=1,\qquad p_1=3,\qquad
p_n=(4n-2)p_{n-1}+p_{n-2}.                             \tag{1.3}
$$



Then $p_n/q_n$ is exactly the regular continued-fraction convergent
to $e$ of zero-based index $3n-2$, and



$$
p_nq_{n-1}-p_{n-1}q_n=2(-1)^{n-1}.                    \tag{1.4}
$$



Put



$$
a=q_{n-1},\qquad b=q_n,\qquad s_n=(-1)^{n-1}.          \tag{1.5}
$$



The first all-$n$, seed-specific conclusion is the exact
minimization identity



$$
\boxed{
\rho_n=
\min_{\substack{\beta,J\in\mathbb Z\\
p_n\beta-Jb=2s_na}}|\beta|.}                           \tag{1.6}
$$



Every solution has



$$
\beta=r_n+\ell b\qquad(\ell\in\mathbb Z),              \tag{1.7}
$$



where $r_n$ is Item 290's signed centered representative of
$a^2\bmod b$.  Thus (1.6) is not a relaxation or a one-way
necessary condition: it is an exact recognition of the actual least
lift.

Let



$$
\eta_n:=(-1)^n\left(e-\frac{p_n}{b}\right)>0.           \tag{1.8}
$$



For every solution in (1.6),



$$
\boxed{
s_n(\beta e-J)=\frac{2a}{b}-\beta\eta_n.}              \tag{1.9}
$$



If the desired half-bound failed, so that



$$
0<|\beta|=\rho_n<\frac a2,                             \tag{1.10}
$$



then (1.9) would place $\beta e-J$ in an explicitly tiny
neighborhood of the moving inhomogeneous target $2a/b$:



$$
\left|
s_n(\beta e-J)-\frac{2a}{b}
\right|
<
\frac{a}{2bQ_{3n-1}},                                  \tag{1.11}
$$



where $Q_j$ is the denominator of the $j$-th regular convergent
to $e$, and



$$
Q_{3n-1}=2nb+Q_{3n-3}.                                 \tag{1.12}
$$



In relative form,



$$
\left|
\frac{s_n(\beta e-J)}{2a/b}-1
\right|
<
\frac1{4Q_{3n-1}}.                                    \tag{1.13}
$$



This yields a rigorous, sharply scoped obstruction.  A fixed-power
*homogeneous* irrationality estimate



$$
|\beta e-J|\ge C(1+|\beta|)^{-\lambda}
\quad(C>0,\ \lambda>0\text{ fixed})                    \tag{1.14}
$$



combined only with the size consequence
$|\beta e-J|<1/n$ of (1.11), gives only



$$
\boxed{
1+\rho_n>(Cn)^{1/\lambda}.}                            \tag{1.15}
$$



That is a polynomial scale.  It is far below the required



$$
\log\rho_n\ge n\log n-O(n).                            \tag{1.16}
$$



The standard continued-fraction lower bound for $e$,



$$
|\beta e-J|
\gg\frac1{|\beta|\log(2|\beta|)},                      \tag{1.17}
$$



similarly gives only



$$
\rho_n\log(2\rho_n)\gg n.                              \tag{1.18}
$$



Equations (1.15) and (1.18) are method ceilings for the declared
homogeneous comparison.  They do **not** rule out an inhomogeneous
shrinking-target theorem, an exact Ostrowski argument using the center
of (1.11), or a new seed-specific congruence.

No proof of



$$
2\rho_n\ge q_{n-1}                                    \tag{1.19}
$$



and no construction with $\log\rho_n=O(n)$ is obtained.  The
proper-target asymmetry and the Item-282 product baseline remain.
Booking is zero.

## 2. Exact reverse-Bessel and factorial seed

Define the monic reverse-Bessel polynomial



$$
A_n(X)=
\sum_{k=0}^n
\frac{(2n-k)!}{k!(n-k)!}X^k.                           \tag{2.1}
$$



Its coefficient formula gives



$$
A_0(X)=1,\qquad A_1(X)=2+X,                            \tag{2.2}
$$



and direct coefficient comparison gives



$$
A_n(X)=(4n-2)A_{n-1}(X)+X^2A_{n-2}(X).                \tag{2.3}
$$



Consequently,



$$
\boxed{
q_n=A_n(-1),\qquad p_n=A_n(1).}                        \tag{2.4}
$$



In particular,



$$
q_n=
\sum_{k=0}^n(-1)^k
\frac{(2n-k)!}{k!(n-k)!},\qquad
p_n=
\sum_{k=0}^n
\frac{(2n-k)!}{k!(n-k)!}.                              \tag{2.5}
$$



For the classical normalization



$$
y_n(z):={}_2F_0\!\left(-n,n+1;\,\,;-\frac z2\right)
=
\sum_{j=0}^n
\frac{(n+j)!}{j!(n-j)!}\left(\frac z2\right)^j,         \tag{2.6}
$$



reindexing $j=n-k$ in (2.5) gives



$$
\boxed{
p_n=y_n(2),\qquad
q_n=(-1)^ny_n(-2)=|y_n(-2)|.}                          \tag{2.7}
$$



Thus the companion used in (1.6) is not an auxiliary fitted to finite
data.  Both $p_n$ and $q_n$ are the two signed fixed-argument
Bessel specializations of the same exact factorial polynomial.

## 3. The every-third convergents to $e$

Euler's regular continued fraction is



$$
e=[2;1,2,1,1,4,1,1,6,1,1,8,\ldots].                  \tag{3.1}
$$



Write $P_j/Q_j$ for its $j$-th convergent, with the initial
$2$ carrying index $0$.  Thus



$$
a_{3t-2}=1,\qquad a_{3t-1}=2t,\qquad a_{3t}=1
\quad(t\ge1).                                         \tag{3.2}
$$



The ordinary convergent recurrence, applied three times to one block,
shows for $n\ge3$ that



$$
P_{3n-2}=(4n-2)P_{3n-5}+P_{3n-8},                    \tag{3.3}
$$





$$
Q_{3n-2}=(4n-2)Q_{3n-5}+Q_{3n-8}.                    \tag{3.4}
$$



The boundary values are



$$
\frac{P_1}{Q_1}=\frac31,\qquad
\frac{P_4}{Q_4}=\frac{19}{7}.                          \tag{3.5}
$$



Comparing (3.3)–(3.5) with (1.1) and (1.3) proves



$$
\boxed{
\frac{p_n}{q_n}=\frac{P_{3n-2}}{Q_{3n-2}}
\quad(n\ge1).}                                        \tag{3.6}
$$



The determinant formula for adjacent convergents, or directly the
recurrence in (1.1)–(1.3), gives



$$
D_n:=p_nq_{n-1}-p_{n-1}q_n,\qquad
D_n=-D_{n-1},\qquad D_1=2.                            \tag{3.7}
$$



This proves (1.4).  It also proves



$$
\gcd(p_n,q_n)=1,\qquad \gcd(q_n,q_{n-1})=1.           \tag{3.8}
$$



The $n=2$ boundary is literal:



$$
(p_2,q_2)=(19,7),\qquad 3n-2=4,\qquad
p_2q_1-p_1q_2=-2.                                     \tag{3.9}
$$



## 4. Proof of the fixed-RHS minimization theorem

From (1.4),



$$
p_na-p_{n-1}b=2s_n.                                   \tag{4.1}
$$



Multiplying by $a$ gives



$$
p_na^2-(ap_{n-1})b=2s_na.                             \tag{4.2}
$$



Thus $(\beta,J)=(a^2,ap_{n-1})$ is one integer
solution of



$$
p_n\beta-Jb=2s_na.                                    \tag{4.3}
$$



Because $\gcd(p_n,b)=1$, every solution of (4.3) has



$$
\beta=a^2+\ell b\qquad(\ell\in\mathbb Z),             \tag{4.4}
$$



and then



$$
J=ap_{n-1}+\ell p_n.                                  \tag{4.5}
$$



Let



$$
r_n=a^2-\kappa_nb,\qquad -\frac b2<r_n<\frac b2        \tag{4.6}
$$



be the unique centered representative.  Equations (4.4)–(4.6)
prove



$$
\min|\beta|=|r_n|=\rho_n.                              \tag{4.7}
$$



There is no zero solution.  Indeed, $\beta=0$ in (4.3) would imply
$b\mid2a$, while (3.8), the oddness of $b$, and $b>2$ make that
impossible.  Hence



$$
\rho_n\ge1.                                           \tag{4.8}
$$



At $n=2$,



$$
a=1,\quad b=7,\quad r_2=1,\quad J_2=3,
$$



and



$$
19\cdot1-3\cdot7=-2=2(-1)^1\cdot1.                   \tag{4.9}
$$



This checks the sign and the first allowed lift index without an
ellipsis convention.

## 5. Exact inhomogeneous $e$-coordinate

The sign of the error of a regular convergent alternates.  Since
$3n-2$ has the same parity as $n$,



$$
\eta_n=(-1)^n\left(e-\frac{p_n}{b}\right)>0.           \tag{5.1}
$$



Divide (4.3) by $b$:



$$
\beta\frac{p_n}{b}-J=2s_n\frac ab.                    \tag{5.2}
$$



Because



$$
e-\frac{p_n}{b}=(-1)^n\eta_n=-s_n\eta_n,              \tag{5.3}
$$



adding $\beta(e-p_n/b)$ to (5.2) and multiplying by
$s_n$ proves



$$
s_n(\beta e-J)=\frac{2a}{b}-\beta\eta_n,              \tag{5.4}
$$



which is (1.9).

The next regular partial quotient after index $3n-2$ is $2n$.
Therefore



$$
Q_{3n-1}=2nQ_{3n-2}+Q_{3n-3}
=2nb+Q_{3n-3}.                                        \tag{5.5}
$$



The standard exact convergent inequalities give



$$
\frac1{b(Q_{3n-1}+b)}
<
\eta_n
<
\frac1{bQ_{3n-1}}.                                    \tag{5.6}
$$



If (1.10) held, equations (5.4) and (5.6) would give



$$
\left|
s_n(\beta e-J)-\frac{2a}{b}
\right|
=|\beta|\eta_n
<
\frac{a}{2bQ_{3n-1}},                                 \tag{5.7}
$$



and division by $2a/b$ gives (1.13).

There is also an exact elementary scale bound.  Since



$$
b=(4n-2)a+q_{n-2},                                    \tag{5.8}
$$



and $0<q_{n-2}<a$ for $n\ge3$,



$$
\frac{2}{4n-1}<\frac{2a}{b}<\frac{2}{4n-2}
\quad(n\ge3).                                         \tag{5.9}
$$



At $n=2$, the left side is equality:



$$
\frac{2a}{b}=\frac27=\frac{2}{4n-1}.                  \tag{5.10}
$$



Because $Q_{3n-1}\ge1$, (1.13) and (5.9)–(5.10)
imply, uniformly for $n\ge2$,



$$
0<s_n(\beta e-J)<\frac1n.                             \tag{5.11}
$$



This is an all-$n$ implication under the explicitly stated
hypothesis (1.10).  It is not a finite pattern.

## 6. A scoped no-go for homogeneous irrationality measures

Fix constants $C>0$ and $\lambda>0$.  Declare the method class
$\mathcal H(C,\lambda)$ to consist of arguments which use the
inhomogeneous identity (5.4) only through the magnitude estimate
(5.11), and then insert a homogeneous estimate



$$
|\beta e-J|\ge C(1+|\beta|)^{-\lambda}.               \tag{6.1}
$$



If (1.10) held, (5.11) and (6.1) would imply exactly



$$
C(1+\rho_n)^{-\lambda}<\frac1n,
$$



hence



$$
1+\rho_n>(Cn)^{1/\lambda}.                            \tag{6.2}
$$



Thus the explicit lower conclusion of this declared comparison is only



$$
\log(1+\rho_n)>
\frac1\lambda\log n+\frac1\lambda\log C,              \tag{6.3}
$$



not the main-scale lower bound (1.16).

For completeness, Euler's continued fraction proves the familiar
uniform estimate



$$
\left|e-\frac uv\right|
\gg\frac1{v^2\log(2v)}
\quad(v\ge1,\ \gcd(u,v)=1).                            \tag{6.4}
$$



Indeed, outside the Legendre range the weaker $1/(2v^2)$ bound
already suffices.  Inside it, $u/v$ is a convergent; the next
partial quotient is $O(j)$, while its denominator is at least the
$j$-th Fibonacci number, so $j=O(\log(2v))$.  The usual lower
convergent inequality then gives (6.4).

The fixed-RHS pair $(J,\beta)$ need not be primitive.  Put



$$
d=\gcd(J,\beta),\qquad
u=\frac{J}{d},\qquad v=\frac{|\beta|}{d}.              \tag{6.4a}
$$



After changing the sign of $u$ if $\beta<0$, the fraction $u/v$
is reduced.  Apply (6.4), multiply first by $v$ and then by $d$,
and use $dv=|\beta|$:



$$
\begin{aligned}
|\beta e-J|
&=d\,|ve-u|\\
&\gg \frac{d}{v\log(2v)}
=\frac{d^2}{|\beta|\log(2v)}
\ge \frac1{|\beta|\log(2|\beta|)}.
\end{aligned}                                         \tag{6.4b}
$$



Thus, with no primitivity assumption on $(J,\beta)$,



$$
|\beta e-J|
\gg\frac1{|\beta|\log(2|\beta|)}.                     \tag{6.5}
$$



Combining (6.5) only with (5.11) gives



$$
\rho_n\log(2\rho_n)\gg n,                             \tag{6.6}
$$



again a polynomial scale.

> **PROVED SCOPED METHOD BARRIER.**
> No argument in $\mathcal H(C,\lambda)$, nor the standard
> homogeneous continued-fraction estimate (6.5) combined only with
> the target magnitude, proves (1.16).  The proof is the explicit
> quantitative implication (6.2) or (6.6).

This statement does not claim that every use of $e$, Padé
approximants, or continued fractions fails.  In particular, it leaves
open an argument that retains:

* the exact moving center $2a/b$;
* the correction sign and width in (5.7);
* the restricted indices $3n-2$; or
* the exact Ostrowski digits of the endpoint.

Those are precisely the data discarded by the homogeneous method
class.

## 7. What the regular-CF descent does and does not add

The immediate regular convergent denominators satisfy



$$
2Q_{3n-3}=b+a,\qquad
2Q_{3n-4}=b-a.                                        \tag{7.1}
$$



Consequently



$$
2aQ_{3n-3}=a(b+a)\equiv a^2\pmod b.                   \tag{7.2}
$$



This checks the modular inverse calculation behind (4.2), but
centering (7.2) is exactly the original problem



$$
\operatorname{cent}_b(a^2).                           \tag{7.3}
$$



Likewise, expanding a candidate vector in the adjacent-convergent
unimodular basis makes its coefficient equal to the same signed
remainder $r_n$.  The regular-CF basis therefore recognizes the
endpoint but does not, by itself, prove
$|r_n|\ge a/2$.

This is a reduction identity, not an impossibility theorem for an
Ostrowski analysis.  A useful next lemma would be an inhomogeneous
avoidance statement:



$$
\boxed{
\text{no }0<|\beta|<a/2\text{ solves }
p_n\beta-Jb=2s_na.}                                   \tag{7.4}
$$



By Section 4, (7.4) is exactly equivalent to (1.19).

## 8. Proper de-overlapped targets

Let



$$
Q\mid
\overline q_{m,n}
=\frac{q_n}{\gcd(q_n,D_m)},\qquad Q>1.                \tag{8.1}
$$



Let $r_{n,Q}$ be the centered residue of $a^2$ modulo $Q$, and
put



$$
\rho_{n,Q}=|r_{n,Q}|.                                 \tag{8.2}
$$



Because $Q\mid b$,



$$
\boxed{
r_{n,Q}=\operatorname{cent}_Q(r_n),\qquad
\rho_{n,Q}\le
\min\!\left\{\rho_n,\frac{Q-1}{2}\right\}.}            \tag{8.3}
$$



Reducing (4.2) modulo $Q$, and using
$\gcd(p_n,Q)=1$, gives another exact minimization:



$$
\boxed{
\rho_{n,Q}=
\min_{\substack{\beta,J\in\mathbb Z\\
p_n\beta-JQ=2s_na}}|\beta|.}                           \tag{8.4}
$$



However, $p_n/Q$ is not the Padé convergent $p_n/q_n$.
Dividing (8.4) by $Q$ therefore does not yield (5.4) with a small
error term.  This is the precise proper-target asymmetry:

* a full-target upper bound $\log\rho_n=O(n)$ transfers through
  (8.3);
* a full-target lower bound does not transfer;
* the $e$-Padé coordinate in Section 5 is tied to the full
  denominator $q_n$, not an arbitrary large divisor $Q$.

An independent large-$Q$ residue theorem is still required.

## 9. Product baseline and capacity admission

Item 282 separates the nonhomogeneous residual into



$$
\gcd(Q,\mathcal S_n)=G_0X,\qquad
G_0=\gcd(Q,B_n),                                      \tag{9.1}
$$



where $B_n$ is the common coefficient/product baseline.  Item 292
addresses only the additive least-lift quotient $X$.  It supplies no
new estimate for $G_0$.

If (1.19) were proved, then the established beta growth would give



$$
\log\rho_n
\ge\log q_{n-1}-\log2
=n\log n-O(n),                                        \tag{9.2}
$$



closing the full-target degree-one $O(n)$-height loophole.  But
(1.19) remains open, and even (9.2) would not close the proper-$Q$
or product-baseline channels.

Therefore the positive-linear-capacity admission test fails:



$$
\boxed{
\text{new Route-1 rate}=0,\qquad
\text{new beta capacity reduction}=0.}                \tag{9.3}
$$



## 10. Strict labels

### PROVED

* The factorial/reverse-Bessel identities (2.1)–(2.7).
* The every-third $e$-convergent identity (3.6), including the
  zero-based index $3n-2$.
* The Wronskian (1.4) and the $n=2$ sign/index boundary.
* The fixed-RHS minimum equivalence (1.6), the complete solution
  family (1.7), and the exclusion of $\beta=0$.
* The exact inhomogeneous identity (1.9).
* The next-denominator/error bounds (1.11)–(1.13).
* The proper-target identities (8.3)–(8.4).
* Separation from the Item-282 product baseline.

### PROVED SCOPED METHOD BARRIER

* In the declared class $\mathcal H(C,\lambda)$, the explicit
  consequence is only (6.2).
* The standard homogeneous continued-fraction estimate for $e$
  gives only (6.6) when the moving target center is discarded.
* No claim is made against inhomogeneous/Ostrowski, shrinking-target,
  or new seed-specific congruence methods.

### EXACT FINITE ONLY

* The checker verifies bounded coefficient, convergent, determinant,
  centered-family, correction-bound bookkeeping, and proper-target
  rows.
* Those rows are deterministic regression checks only.
* No bounded observation is used to assert (1.19), an asymptotic, or
  a prime exception theorem.

### OPEN

* The all-$n$ inequality $2\rho_n\ge q_{n-1}$.
* Any lower bound $\log\rho_n\ge n\log n-O(n)$.
* Any construction $\log\rho_n=O(n)$.
* The exact inhomogeneous avoidance lemma (7.4).
* A large proper de-overlapped target residue theorem.
* The Item-282 common product baseline and weighted-return cover.
* Route 1 and every conclusion about $e+\pi$.

### BOOKING



$$
\boxed{
\text{new Route-1 rate}=0,\qquad
\text{new beta capacity reduction}=0.}                \tag{10.1}
$$



## 11. Deterministic replay

From the archive root:

~~~text
python scripts/item292_beta_bessel_pade_lift_certificate.py ^
  --output results/item292_beta_bessel_pade_lift_certificate_replay.json
~~~

The checker uses only the Python standard library, exact integers, and
exact rational comparisons.  The canonical result and replay must be
byte-identical.
