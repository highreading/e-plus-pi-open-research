> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact endpoint remainder for the constrained raw-arctangent family

Date: 2026-08-26

This note continues `raw_arctan_bordered_rank_proof.md`.  It derives exact
real-integral and contour representations for the endpoint remainder and keeps
three normalizations separate:

1. arbitrary rational scaling of the polynomial triple;
2. a primitive integral polynomial triple;
3. the primitive integral *endpoint pair* obtained after removing the gcd of
   only the two endpoint coefficients.

The distinction is essential.  An arbitrarily rescaled analytic remainder has
no Diophantine meaning.  Only the last normalization gives an integer linear
form in $1$ and $e+\pi$.

This note proves an all-degree nonvanishing theorem for the endpoint
*coefficient* $B_n(1)$, but it does **not** prove that the endpoint remainder is
nonzero for every $n$ and does not prove that the endpoint-primitive remainders
tend to zero or infinity.  Those are genuinely additional Archimedean
questions.

## 1. The family and its exact order conditions

Fix $n\geq0$, put

$$
m=n+1,\qquad M=3n+1=3m-2,
$$

and let $A,B,C\in\mathbb Q[z]$ have degree at most $n$.  Consider

$$
R(z)=A(z)+B(z)e^z+C(z)\arctan z.                 \tag{1}
$$

The constrained family is defined by

$$
R(z)=O(z^M),\qquad C(1)=4B(1).                  \tag{2}
$$

The first condition comprises the $M=3n+1$ coefficient equations with
indices $0,\ldots,M-1$.  Together with the endpoint equation, this gives
$3n+2$ rational homogeneous equations on $3n+3$ coefficients.

The all-degree rank theorem in `raw_arctan_bordered_rank_proof.md` shows that
the solution space of (2) is exactly one-dimensional over $\mathbb Q$.  That
rank proof and its link to the defining Taylor system were independently
audited in the archive on 2026-08-26.

Write

$$
B(z)=\sum_{j=0}^n b_jz^j,\qquad
C(z)=\sum_{j=0}^n c_jz^j.                       \tag{3}
$$

## 2. An all-degree endpoint-coefficient theorem

**Proposition 2.1.**  Every nonzero solution of (2) satisfies

$$
B(1)\ne0,\qquad C(1)=4B(1)\ne0.                 \tag{4}
$$

**Proof.**  For $n=0$, the equations give $(A,B,C)=(-b,b,4b)$, so a nonzero
solution has $B(1)=b\ne0$.  Now suppose $n\geq1$ and $B(1)=0$.  The endpoint
equation gives $C(1)=0$, so

$$
B=(z-1)\widetilde B,\qquad C=(z-1)\widetilde C,
\qquad \deg\widetilde B,\deg\widetilde C<n.
$$

For coefficient indices $k=n+1,\ldots,3n$, condition (2) says

$$
[z^k]\bigl(B(z)e^z+C(z)\arctan z\bigr)=0.
$$

These are exactly the $2n\times2n$ square system denoted $T_n$ in Section 1
of the bordered-rank note.  Sections 2--4 of that note prove
$\det T_n\ne0$.  Hence $\widetilde B=\widetilde C=0$, and then the low-order
conditions in (2) give $A=0$, contrary to the solution being nonzero.  This
proves (4).  $\square$

This proposition is about the coefficient functional $B\mapsto B(1)$; it is
not a nonvanishing theorem for the real number $R(1)$.

## 3. Exact tail formula

For an integer $L\geq1$, define

$$
E_L=\sum_{r=L}^{\infty}\frac1{r!},              \tag{5}
$$

and let $o(L)$ be the least odd integer not smaller than $L$.  Define

$$
T_L=\sum_{\substack{r\geq L\\ r\text{ odd}}}
       \frac{(-1)^{(r-1)/2}}r.                  \tag{6}
$$

**Proposition 3.1 (exact endpoint tail).**  Every solution of (2) satisfies

$$
R(1)=\sum_{j=0}^n b_jE_{M-j}+\sum_{j=0}^n c_jT_{M-j}. \tag{7}
$$

Moreover, both tails have exact real-integral representations

$$
E_L=\frac1{(L-1)!}\int_0^1e^t(1-t)^{L-1}\,dt,  \tag{8}
$$

$$
T_L=(-1)^{(o(L)-1)/2}
     \int_0^1\frac{t^{o(L)-1}}{1+t^2}\,dt.      \tag{9}
$$

Consequently

$$
R(1)=\int_0^1e^tP_n(t)\,dt+
     \int_0^1\frac{Q_n(t)}{1+t^2}\,dt,          \tag{10}
$$

where the two explicitly rational polynomials are

$$
P_n(t)=\sum_{j=0}^n
\frac{b_j(1-t)^{M-j-1}}{(M-j-1)!},              \tag{11}
$$

$$
Q_n(t)=\sum_{j=0}^n c_j
(-1)^{(o(M-j)-1)/2}t^{o(M-j)-1}.                 \tag{12}
$$

These polynomials have two useful exact factorizations.  First,

$$
P_n(t)=(1-t)^{2n}\sum_{j=0}^n
       \frac{b_j(1-t)^{n-j}}{(3n-j)!}.           \tag{12a}
$$

Second, put $c_{-1}=0$.  Pairing the two indices that produce the same
arctangent-tail monomial gives

$$
Q_n(t)=(-1)^n c_nt^{2n}+
\sum_{\substack{0\leq j\leq n\\j\equiv M\pmod2}}
(-1)^{(M-j)/2}(c_{j-1}+c_j)t^{M-j}.              \tag{12b}
$$

In particular,

$$
Q_n(t)=t^{2n}\widetilde Q_n(t^2)                 \tag{12c}
$$

for a rational polynomial $\widetilde Q_n$.  Thus the exponential integral
in (10) contains the endpoint weight $(1-t)^{2n}$, while the arctangent
integral contains the opposite endpoint weight $t^{2n}$.  This separation is
potentially useful for a future saddle-point analysis, but it supplies no
sign information because the remaining polynomials vary with $n$.

**Proof.**  Put $F=B e^z+C\arctan z$.  Since $\deg A\leq n<M$, the
conditions in (2) say that the coefficients of $F$ with indices
$n+1,\ldots,M-1$ vanish and that $A$ cancels the coefficients with indices
$0,\ldots,n$.  Hence, at the boundary point $z=1$,

$$
R(1)=\sum_{k=M}^{\infty}[z^k]F(z).
$$

The exponential series is absolutely convergent.  The arctangent series at
$1$ is convergent by the alternating-series test, and there are only finitely
many shifts $j$, so separating the finite sums gives (7).

Formula (8) is Taylor's integral remainder for $e^t$.  If
$o(L)=2h+1$, expansion of $(1+t^2)^{-1}$ followed by the alternating-series
limit gives

$$
(-1)^h\int_0^1\frac{t^{2h}}{1+t^2}\,dt
=\sum_{q=h}^{\infty}\frac{(-1)^q}{2q+1}=T_L.
$$

This proves (9), and substituting (8)--(9) in (7) proves (10)--(12).
Equation (12a) follows from $M-j-1=3n-j$.  For (12b), if
$j\equiv M\pmod2$, then the terms with indices $j-1$ and $j$ both have
tail exponent $M-j$ and the same sign $(-1)^{(M-j)/2}$.  The convention
$c_{-1}=0$ handles the lower boundary, while $j=n$ is always the single
unpaired upper-boundary index and contributes $(-1)^nc_nt^{2n}$.
This also proves (12c).
$\square$

There is also a compact Peano-kernel form.  Since $R^{(k)}(0)=0$ for
$0\leq k<M$ and $M>n$,

$$
R(1)=\frac1{(M-1)!}\int_0^1(1-t)^{M-1}
\frac{d^M}{dt^M}\bigl(B(t)e^t+C(t)\arctan t\bigr)\,dt. \tag{13}
$$

Finally, let $U$ be a thin simply connected complex neighborhood of
$[0,1]$ that excludes $i$ and $-i$, choose the branch of $\arctan z$ analytic
on $U$, and let $\Gamma\subset U$ be a positively oriented contour enclosing
$0$ and $1$.  The residue theorem gives the exact contour representation

$$
R(1)=\frac1{2\pi i}\int_\Gamma
\frac{B(z)e^z+C(z)\arctan z}{z^M(z-1)}\,dz.      \tag{14}
$$

Indeed, the residue at $1$ is $F(1)$ and the residue at $0$ is the negative
of the sum of the first $M$ Taylor coefficients of $F$; their sum is (7).

## 4. The three normalizations

Choose the unique solution line from (2).  Clearing denominators and then
dividing by the gcd of **all** polynomial coefficients produces, up to an
overall sign, a primitive integral polynomial triple

$$
(A_n^{\rm pol},B_n^{\rm pol},C_n^{\rm pol})\in\mathbb Z[z]^3. \tag{15}
$$

Define its raw endpoint integers

$$
a_n=A_n^{\rm pol}(1),\qquad b_n=B_n^{\rm pol}(1),\qquad
c_n=C_n^{\rm pol}(1)=4b_n.                       \tag{16}
$$

Proposition 2.1 gives $b_n\ne0$.  Put

$$
g_n=\gcd(|a_n|,|b_n|),\qquad
\alpha_n=\frac{a_n}{g_n},\qquad
\beta_n=\frac{b_n}{g_n}.                         \tag{17}
$$

Then $\gcd(|\alpha_n|,|\beta_n|)=1$, and the canonical endpoint-primitive
linear form is

$$
\ell_n=\alpha_n+\beta_n(e+\pi)
=\frac{R_n^{\rm pol}(1)}{g_n}.                   \tag{18}
$$

The rational approximant and its scale-free analytic error are

$$
r_n=-\frac{\alpha_n}{\beta_n}=-\frac{a_n}{b_n},
\qquad
\varepsilon_n=(e+\pi)-r_n=\frac{R_n^{\rm pol}(1)}{b_n}. \tag{19}
$$

Thus the exact factorization is

$$
|\ell_n|=|\beta_n|\,|\varepsilon_n|.             \tag{20}
$$

Multiplying (15) by a nonzero rational number changes the raw analytic
remainder and may make it arbitrarily small.  It does not change $r_n$ or
$\varepsilon_n$, and after returning to a primitive integral endpoint pair it
does not change $(\alpha_n,\beta_n)$ except for a common sign.  Therefore a
claim that the "remainder tends to zero" has Diophantine content only after
the endpoint-primitive normalization (17).

Removing $g_n$ in (17) is legitimate even when $g_n$ does not divide every
coefficient in (15).  The irrationality criterion uses only the two endpoint
integers, not integrality of the rescaled polynomials.

## 5. What endpoint nonvanishing means

Equation (19) gives the exact equivalence

$$
\ell_n=0
\quad\Longleftrightarrow\quad
e+\pi=r_n\in\mathbb Q.                            \tag{21}
$$

The all-degree rank theorem proves $\beta_n\ne0$, but it does not decide
(21).  A proof that $\ell_n\ne0$ for every $n$ would amount to proving that
$e+\pi$ avoids this particular explicitly defined sequence of rationals.  It
would not, by itself, prove irrationality, because the sequence is not known
to contain every rational number.

On the other hand, a nonzero sequence tending to zero would prove
irrationality:

**Proposition 5.1.**  If $\ell_n\ne0$ for all sufficiently large $n$ and
$\ell_n\to0$, then $e+\pi$ is irrational.

**Proof.**  If $e+\pi=p/q$ in lowest terms, then

$$
\ell_n=\frac{q\alpha_n+p\beta_n}{q}.
$$

Whenever this number is nonzero, its absolute value is at least $1/q$,
contradicting convergence to zero.  $\square$

Conversely, if $e+\pi=p/q$ and no $\ell_n$ is zero, then
$|\ell_n|\geq1/q$ for every $n$.  This is a useful exact obstruction, but it
does not decide which alternative holds for the actual constant.

## 6. A rigorous general upper bound, and why it is not enough

For the primitive integral polynomial triple (15), put

$$
H_{B,n}=\max_j|b_j|,\qquad H_{C,n}=\max_j|c_j|,
$$

where here $b_j,c_j$ denote its polynomial coefficients as in (3).  Since
$M-j\geq2n+1$, (8)--(9) imply

$$
0<E_{M-j}\leq\frac{2}{(2n+1)!},\qquad
|T_{M-j}|\leq\frac1{2n+1}.
$$

Therefore

$$
|\ell_n|\leq
\frac{n+1}{g_n}
\left(\frac{2H_{B,n}}{(2n+1)!}
      +\frac{H_{C,n}}{2n+1}\right).              \tag{22}
$$

This is an all-degree theorem, but it is only an upper bound.  In this mixed
system the arctangent singularities at $\pm i$ lie on the unit circle, so the
second tail is only algebraically small before cancellations.  To deduce
$\ell_n\to0$ from (22), one would need an upper bound on
$H_{C,n}/g_n$ that is far smaller than what the exact finite solutions show.
To prove a no-go theorem such as $|\ell_n|\to\infty$, one instead needs a
uniform *lower* bound after the cancellations in (10), together with control
of $g_n$.  Neither follows from the rank determinant.

The exact calculations for $1\leq n\leq18$ in
`results/mixed_hermite_pade_n18.json` certify that the endpoint-primitive
forms in that finite range are nonzero and have absolute value greater than
$1$; their sizes grow very rapidly over that range.  This is a finite theorem
only.  It is not evidence that may be extrapolated into the missing lower
bound or an asymptotic theorem.

## 7. Conclusion of this branch

The constrained raw-arctangent family has now been reduced to the exact
Archimedean problem (10) and the exact arithmetic factorization (20).  The
rank theorem supplies uniqueness and $B_n(1)\ne0$ for every $n$.  What remains
is one of the following genuinely new ingredients:

* an all-$n$ sign or lower-bound theorem for the two integrals in (10), plus
  a bound for the endpoint gcd $g_n$; or
* an asymptotic theorem for both $\varepsilon_n$ and $|\beta_n|$ strong enough
  to decide their product in (20).

No such ingredient is proved here.  In particular, arbitrary rational
rescaling cannot substitute for endpoint-primitive decay, and finite growth
cannot be promoted to an all-degree no-go theorem.
