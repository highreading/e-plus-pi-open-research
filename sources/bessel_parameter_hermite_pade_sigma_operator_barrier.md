> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The Bessel parameter zero: a $\Sigma$-operator exclusion and a shift Hermite--Padé determinant barrier

Checked: 2026-08-27 UTC.

## 1. Verdict

Let



$$
q_0=q_1=1,\qquad q_n=(4n-2)q_{n-1}+q_{n-2},
\tag{1}
$$



and let $f_p:\mathbb Z_p\to\mathbb Z_p$ be the canonical interpolation
of



$$
f(n)=(-1)^nq_n.
\tag{2}
$$



It satisfies



$$
f_p(x+1)+(4x+2)f_p(x)-f_p(x-1)=0.
\tag{3}
$$



If $\rho=\rho_{p,r}$ is an ordinary zero, then



$$
v_p(q_n)=v_p(n-\rho)
\tag{4}
$$



for every nonnegative integer $n\equiv r\pmod p$.

This note tests two genuinely non-raw-looking routes to a height bound
for $\rho$: the 2026 theory of $\Sigma$-operators and determinants or
Hermite--Padé forms made from parameter shifts of $f_p$.

The conclusions are exact but negative.

1. The Bessel recurrence operator

   

$$
R=1+(4n-2)\sigma-\sigma^2
   \tag{5}
$$



   is not a $\Sigma$-operator.  Its image under Rivoal's
   difference-to-differential morphism is irregular at $z=0$.
   More strongly, the sequence $f(n)$ cannot satisfy *any*
   $\Sigma$-operator eventually, because its ordinary generating series
   has radius zero, whereas a rational solution of a $\Sigma$-operator
   generates a $G$-function.
2. Every finite integral-polynomial shift form has an exact reduction

   

$$
\sum_{j\in J}P_j(x)f_p(x+j)
   =A(x)f_p(x)+B(x)f_p(x+1),
   \qquad A,B\in\mathbb Z[x].
   \tag{6}
$$



   On every ordinary branch,

   

$$
\boxed{
   v_p\!\left(\sum_{j\in J}P_j(\rho)f_p(\rho+j)\right)
   =v_p(B(\rho)).}
   \tag{7}
$$



   Thus a linear shift Hermite--Padé form gains no unexplained
   $p$-adic order: all of it is exactly the order of an ordinary
   integer polynomial at the unknown zero.
3. The same reduction gives a determinant dichotomy.  For a determinant
   of linear shift forms, let $\mathcal B(x)$ be the matrix of the
   corresponding $B$-polynomials.  At the root,

   

$$
v_p D(\rho)=v_p\det\mathcal B(\rho).
   \tag{8}
$$



   If $\det\mathcal B$ is not identically zero, the entire root problem
   has merely been transferred to the polynomial
   $\det\mathcal B$.  If $\det\mathcal B\equiv0$, so that the
   determinant vanishes formally whenever $f_p(x)=0$, then its
   evaluation at an integer $n$ is divisible in $\mathbb Z$ by
   $f(n)=(-1)^nq_n$.  Unless the auxiliary is zero, its archimedean
   height is therefore at least

   

$$
\log q_n=n\log n+O(n).
   \tag{9}
$$



These statements rule out the direct application of
$\Sigma$-operator theory and every determinant whose vanishing is
forced *formally* by finitely many parameter shifts, the recurrence, and
the equation $f_p(\rho)=0$.  They do **not** rule out a shift
determinant whose residual polynomial happens to vanish or be very small
at this particular $\rho$; that is exactly the still-open polynomial
approximation problem.  Nor do they rule out a Hermite--Padé construction
that introduces genuinely new functions, controlled arithmetic local
Taylor data, integral transforms, or nontrivial hypergeometric tails.

No estimate



$$
v_p(n-\rho)\log p=o(n\log n)
\tag{10}
$$



is proved here.  The exact remaining task is to construct a controlled
algebraic relation for $\rho$, small-height integer polynomials taking
exceptionally small nonzero values there, or an auxiliary outside the
finite-shift algebra that implies the same estimate.

## 2. Why the recurrence is not a $\Sigma$-operator

Rivoal writes $\sigma u_n=u_{n-1}$ and defines an algebra isomorphism



$$
\mathcal M:\overline{\mathbb Q}[n,\sigma]
 \longrightarrow\overline{\mathbb Q}[z,\delta],
 \qquad n\longmapsto\delta=z\frac d{dz},
 \quad \sigma\longmapsto z.
\tag{11}
$$



A difference operator is a $\Sigma$-operator when its image is a
$G$-operator.  Applying (11) to (5) and using
$\delta z=z\delta+z$ gives



$$
\begin{aligned}
 \mathcal M(R)
 &=1+(4\delta-2)z-z^2\\
 &=4z\delta+1+2z-z^2\\
 &=4z^2\frac d{dz}+1+2z-z^2.
\end{aligned}
\tag{12}
$$



The coefficient quotient of this first-order differential operator is



$$
\frac{1+2z-z^2}{4z^2},
\tag{13}
$$



which has a double pole at $z=0$.  Hence (12) is irregular there and
cannot be a $G$-operator.  Equivalently, a local homogeneous solution
is



$$
z^{-1/2}\exp\left(\frac z4+\frac1{4z}\right),
\tag{14}
$$



which displays the irregular exponential factor at $0$.  Therefore
$R$ is not a $\Sigma$-operator.

There is also a stronger exclusion that does not depend on choosing the
minimal recurrence.  Positivity in (1) gives



$$
q_n>\prod_{j=2}^{n}(4j-2)
 \qquad(n\geq2).
\tag{15}
$$



Consequently



$$
\lim_{n\to\infty}|f(n)|^{1/n}=+\infty,
\tag{16}
$$



so $\sum_{n\geq0}f(n)z^n$ has radius of convergence zero.  Theorem
1(ii) of Rivoal's paper says that a rational forward solution of a
$\Sigma$-operator has a $G$-function as its ordinary generating
series.  A $G$-function has coefficients of at most exponential
archimedean growth.  Thus no $\Sigma$-operator can annihilate
$(f(n))$ eventually.

The primary source used here is T. Rivoal,
[*A class of arithmetic difference operators*](https://rivoal.perso.math.cnrs.fr/articles/sigmaop.pdf),
preprint dated February 26, 2026; see Definition 1, Theorem 1(ii), and
the recalled Fuchsian property of $G$-operators.  That paper develops
complex asymptotics, $G$-arithmetic, and meromorphic interpolation of
solutions.  It contains no $p$-adic irrationality measure that could
override the preceding nonmembership.

Factorial renormalization does not make (5) an application of the
theorem: such a gauge is not the morphism (11) and changes both the
operator and the sequence whose interpolation is being studied.  A
separately normalized recurrence would require a fresh $G$-function
audit and, even if useful for complex asymptotics, would not by itself
give a $p$-adic height theorem for the zero of the original $f_p$.
The factorial-growth slope is precisely what distinguishes (1) from the
Apéry-type $\Sigma$-operator examples in the paper.

## 3. The exact two-generator shift module

Define polynomials $U_j,V_j\in\mathbb Z[x]$, for $j\in\mathbb Z$,
by



$$
U_0=1,\quad V_0=0,\qquad
 U_1=0,\quad V_1=1,
\tag{17}
$$



and the recurrence



$$
\begin{aligned}
 U_{j+1}&=-(4x+4j+2)U_j+U_{j-1},\\
 V_{j+1}&=-(4x+4j+2)V_j+V_{j-1}.
\end{aligned}
\tag{18}
$$



For negative $j$, equation (18) is read backwards.  Equation (3)
then proves, by induction in both directions, that



$$
\boxed{
 f_p(x+j)=U_j(x)f_p(x)+V_j(x)f_p(x+1)
 \qquad(j\in\mathbb Z).}
\tag{19}
$$



The adjacent coefficient pairs are unimodular:



$$
\boxed{
 U_jV_{j+1}-U_{j+1}V_j=(-1)^j.}
\tag{20}
$$



Indeed, the transfer matrix in (18) has determinant $-1$, and the
identity is $1$ at $j=0$.

Now let $J\subset\mathbb Z$ be finite and $P_j\in\mathbb Z[x]$.
Substitution of (19) gives (6) with the explicit coefficients



$$
A=\sum_{j\in J}P_jU_j,\qquad
 B=\sum_{j\in J}P_jV_j.
\tag{21}
$$



The map from shift forms to the second coefficient is already
surjective, since $V_1=1$.  Therefore the recurrence alone imposes no
hidden divisibility or Padé order on $B$.

## 4. The unit boundary value on an ordinary branch

Let $r\in\{0,\ldots,p-1\}$ be an ordinary root class and
$\rho\in r+p\mathbb Z_p$ its zero.  Consecutive Bessel denominators
are coprime:



$$
\gcd(q_m,q_{m+1})
 =\gcd(q_{m-1},q_m)=\cdots=\gcd(q_0,q_1)=1.
\tag{22}
$$



Since $p\mid q_r$, equation (22) gives $p\nmid q_{r+1}$.
The $1$-Lipschitz interpolation and
$\rho+1\equiv r+1\pmod p$ therefore give



$$
\boxed{f_p(\rho+1)\in\mathbb Z_p^\times.}
\tag{23}
$$



Evaluating (6) at $\rho$ and using $f_p(\rho)=0$ proves



$$
\sum_{j\in J}P_j(\rho)f_p(\rho+j)
 =B(\rho)f_p(\rho+1),
\tag{24}
$$



and (7) follows.

This yields a sharp linear dichotomy.

- If $B=0$ identically, the form is $A(x)f_p(x)$.  At an integer
  $n$, either it is zero or

  

$$
\left|A(n)f(n)\right|\geq q_n.
  \tag{25}
$$



- If $B\ne0$, exact vanishing at $\rho$ means $B(\rho)=0$, which
  is already an algebraicity certificate for $\rho$.  High but finite
  $p$-adic order is exactly the polynomial-approximation problem
  $v_p(B(\rho))$, with no additional gain supplied by the shifts.

Thus a recurrence syzygy pays the full Bessel height, while a
non-syzygy succeeds only if its residual polynomial $B$ supplies the
missing arithmetic theorem.

## 5. Determinants of linear shift forms

Let an $s\times s$ matrix have entries



$$
H_{ab}(x)=\sum_{j\in J_{ab}}P_{ab,j}(x)f_p(x+j),
 \qquad P_{ab,j}\in\mathbb Z[x].
\tag{26}
$$



Use (21) entrywise and write



$$
H_{ab}(x)=A_{ab}(x)F+B_{ab}(x)G,
\qquad F=f_p(x),\quad G=f_p(x+1).
\tag{27}
$$



Let



$$
\mathscr D(x;F,G)
 =\det\bigl(A_{ab}(x)F+B_{ab}(x)G\bigr)
 \in\mathbb Z[x,F,G],
\tag{28}
$$



and let $\mathcal B=(B_{ab})$.  Setting $F=0$ gives



$$
\mathscr D(x;0,G)=\det\mathcal B(x)\,G^s.
\tag{29}
$$



At $x=\rho$, equation (23) makes $G$ a unit.  Therefore



$$
\boxed{
 v_p\det(H_{ab}(\rho))
 =v_p\det\mathcal B(\rho),}
\tag{30}
$$



which proves (8).

If $\det\mathcal B\equiv0$, equation (29) says that the polynomial
$\mathscr D$ is divisible by $F$:



$$
\mathscr D(x;F,G)=F\,\mathscr C(x;F,G),
 \qquad\mathscr C\in\mathbb Z[x,F,G].
\tag{31}
$$



At every nonnegative integer $n$,



$$
\det(H_{ab}(n))
 =(-1)^nq_n\,
 \mathscr C\bigl(n,(-1)^nq_n,(-1)^{n+1}q_{n+1}\bigr).
\tag{32}
$$



If this integer is nonzero, (9) follows.  Each division by a $q_n$
factor corresponds to removing one formal $F$-factor and one order of
the recurrence-forced zero at $\rho$.  After all such factors are
removed, no vanishing forced solely by $f_p(\rho)=0$ remains.

A canonical $2\times2$ Hankel determinant illustrates the other
branch:



$$
D_2(x)=
 \det\begin{pmatrix}
 f_p(x)&f_p(x+1)\\
 f_p(x+1)&f_p(x+2)
 \end{pmatrix}.
\tag{33}
$$



At a zero $\rho$,



$$
D_2(\rho)=-f_p(\rho+1)^2\in\mathbb Z_p^\times.
\tag{34}
$$



So this simplest nontrivial determinant has no root order at all.

Equations (30)--(32) cover determinants and linear
Hermite--Padé systems whose entries are finite parameter-shift forms.
They do not cover determinants involving new integral transforms,
derivatives supplied with independent arithmetic data, or infinite
tails with a separately proved height theorem.

### 5.1 Jet data already contain an open Euler-factorial value

Adding parameter derivatives does not preserve the terminating arithmetic
at integer indices.  For



$$
T_k(x)=\frac{(-x)_k(x+1)_k}{k!}
 =\frac{(-1)^k}{k!}\prod_{h=-k+1}^{k}(x+h),
\tag{J1}
$$



the factor $x-n$ is simple when $k\geq n+1$, and exact
differentiation gives



$$
\boxed{
 T_k'(n)=(-1)^{n+1}
 \frac{(k-n-1)!(n+k)!}{k!}\ne0
 \qquad(k\geq n+1).}
\tag{J2}
$$



In particular, termwise differentiation is $p$-adically convergent at
$x=0$ and yields



$$
\boxed{
 f_p'(0)=-\sum_{m=0}^{\infty}m!.}
\tag{J3}
$$



Thus the first jet already introduces Euler's $p$-adic factorial
constant.  Its irrationality for any specified prime is itself a
longstanding conjecture.  The primary Padé/determinant reference
T. Matala-aho and W. Zudilin,
[*Euler's factorial series and global relations*](https://arxiv.org/abs/1703.02633),
*J. Number Theory* **186** (2018), 202--210, proves global alternatives
across sets of primes; it does not prove the required fixed-$p$
irrationality or a uniform height theorem for (J3).

The scale of that paper's explicit Padé family also explains the
fixed-prime gap.  At the specialization giving $\sum m!$, its integral
coefficients and remainder satisfy



$$
\begin{aligned}
 \log\max\{|P_M|,|Q_M|\}
 &\leq M\log M+O(M),\\
 v_p(Q_M\textstyle\sum_{m\geq0}m!-P_M)
 &\geq2v_p(M!)
 =\frac{2M}{p-1}+O(\log M).
\end{aligned}
\tag{J4}
$$



The certified fixed-$p$ order in (J4) is only linear in the Padé
index, while the coefficient height is on the $M\log M$ scale.
Their successful product argument multiplies over a set of primes,
using the global factorial product formula.  For one fixed prime, any
extra remainder order beyond (J4) is precisely additional arithmetic
cancellation not controlled by those estimates.  Thus this known
non-raw Padé family does not provide the missing fixed-$p$ input.

More generally, differentiating (19) $\ell$ times gives



$$
\begin{aligned}
 f_p^{(\ell)}(x+j)
 =\sum_{t=0}^{\ell}\binom{\ell}{t}
 \bigl(
 U_j^{(\ell-t)}(x)f_p^{(t)}(x)
 +V_j^{(\ell-t)}(x)f_p^{(t)}(x+1)
 \bigr).
\end{aligned}
\tag{J5}
$$



So finite shifted jets reduce to finitely many boundary jets, but the
recurrence supplies no rationality or archimedean heights for those
boundary constants.  A local Hermite--Padé system over $\mathbb Q_p$
can certainly be formed; turning it into a rational-integer auxiliary
requires a new arithmetic theorem for these jet values.  Replacing the
jets by finite rational truncations returns to the tail threshold (40).

## 6. The residual polynomial problem

For clarity, the exact height requirement on the residual polynomial is
elementary.  Let $C\in\mathbb Z[x]$ have degree $d$, coefficient
height $H(C)$, and let



$$
a=v_p(n-\rho),\qquad b=v_p(C(\rho)).
\tag{35}
$$



Integral polynomials are $1$-Lipschitz on $\mathbb Z_p$, so



$$
v_p(C(n))\geq\min(a,b).
\tag{36}
$$



If $C(n)\ne0$, the archimedean product estimate gives



$$
\boxed{
 \min(a,b)\log p
 \leq\log(d+1)+\log H(C)+d\log\max(1,n).}
\tag{37}
$$



Consequently a useful Padé construction would have to provide, uniformly
in the relevant $p,r,n$, a polynomial $C$ with



$$
\begin{aligned}
 C(n)&\ne0,\\
 v_p(C(\rho))&\geq v_p(n-\rho),\\
 \log H(C)+\deg(C)\log(n+1)&=o(n\log n).
\end{aligned}
\tag{38}
$$



An exact nonzero polynomial relation $C(\rho)=0$ of uniformly
controlled degree and height would be more than enough, but no such
algebraicity result is known.  Solving a local Hermite--Padé system over
$\mathbb Q_p$ does not provide (38): its coefficients are $p$-adic
numbers with no rational archimedean height until a separate arithmetic
theorem is supplied.

The parameter-hypergeometric series



$$
f_p(x)=\sum_{k\geq0}\frac{(-x)_k(x+1)_k}{k!}
\tag{39}
$$



does supply rational polynomial truncations.  However, the companion
audit

    sources/bessel_padic_hypergeometric_zero_pade_barrier.md

proves that the factor $x-n$ first occurs at $k=n+1$, while the
preceding integer value is already


$$
\sum_{k=0}^{n}\frac{(-n)_k(n+1)_k}{k!}
 =(-1)^nq_n.
\tag{40}
$$



Thus finite truncation data recover the same main-scale height.  The
combination of (30)--(32) and (40) isolates the remaining opening
precisely: a successful parameter Padé construction must use arithmetic
structure not generated by finite shifts and must import the relevant
tail factor without importing $q_n$.

Nothing in this note proves irrationality or transcendence of a Bessel
zero, or of $e+\pi$.

## 7. Exact certificate

The companion script

    scripts/bessel_parameter_hermite_pade_sigma_certificate.py

checks the forward and backward coefficient recurrences (18), the
unimodular identity (20), and the shift reduction (19) over finite exact
boxes.  It checks mod-$p$ root classes for many primes (hence the
boundary-unit condition needed on ordinary classes), the boundary unit
(23), and the Hankel identity (34).  It also verifies the
factorial-growth lower bound (15), the algebraic irregular-solution
identity (14), the nonterminating derivative formula (J2), and finite
instances of the residual polynomial estimate (37).

Run

    python -m py_compile scripts/bessel_parameter_hermite_pade_sigma_certificate.py
    python scripts/bessel_parameter_hermite_pade_sigma_certificate.py

For byte-identical replay, use

    python scripts/bessel_parameter_hermite_pade_sigma_certificate.py \
      --output /tmp/bessel_parameter_hermite_pade_sigma_certificate.json
    cmp results/bessel_parameter_hermite_pade_sigma_certificate.json \
      /tmp/bessel_parameter_hermite_pade_sigma_certificate.json
