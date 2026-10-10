> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A common-kernel lattice for $e+\pi$: exact identity, saturated arithmetic, and the rank-two capacity barrier

Checked: 2026-08-27 UTC.

## 1. Verdict

There is a valid and unusually direct common-kernel identity. For
$H\in\mathbb Z[x]$ and $a\in\mathbb Z$, put



$$
f(x)=a+(1+x^2)H'(x),
$$



and, for a polynomial $g$, define



$$
A(g)=\sum_{k\geq 0}(-1)^k g^{(k)}(1),
 \qquad
 B(g)=\sum_{k\geq 0}(-1)^k g^{(k)}(0).
$$



If



$$
A\bigl((1+x^2)H'\bigr)=0,
\tag{1}
$$



then



$$
\boxed{
 \int_0^1 f(x)\left(e^x+\frac{4}{1+x^2}\right)\,dx
 =
 a(e+\pi)-B(f)+4\bigl(H(1)-H(0)\bigr).}
\tag{2}
$$



Thus the right side is an integer linear form in $e+\pi$. The additional
conditions $f(0)=f(1)=0$ leave a large integer lattice in which small
polynomials can be sought.

The original temporary search contained an important arithmetic defect:
making each rational nullspace ray primitive did **not** produce a saturated
$\mathbb Z$-kernel. At search parameter $40$, the old basis had index



$$
278628139008
$$



in the full integer kernel. The corrected calculation uses a saturated
kernel.

The most important exact structural result is that the map from a kernel
polynomial to its integer form has rank only two:



$$
\boxed{\Phi(K_D)=8\mathbb Z\times 2\mathbb Z.}
\tag{3}
$$



Most very short full-lattice vectors therefore lie in the exact zero-form
kernel $\ker\Phi$. After quotienting them out, the natural
potential-theoretic metric is two-dimensional. The exact finite quotient
data have the capacity scale predicted by evaluation at $i$.
Ordinary determinant/Minkowski balancing at that scale supplies
linear-form exponent $1$, equivalently rational-approximation exponent
$2$; it does not by itself supply a Roth-breaking exponent greater than
$1$.

This is a limitation of the generic determinant argument. It is **not** an
upper bound for every vector and does not rule out exceptional arithmetic
vectors. Proving such a sequence, together with uniform nonvanishing,
remains a genuinely live but open task.

Nothing here proves that $e+\pi$ is irrational, algebraic, or
transcendental.

## 2. Proof of the common-kernel identity

Repeated integration by parts terminates for a polynomial and gives



$$
\int_0^1 g(x)e^x\,dx=eA(g)-B(g).
\tag{4}
$$



Since $A(1)=1$, condition (1) gives $A(f)=a$. Also,



$$
\begin{aligned}
 4\int_0^1\frac{f(x)}{1+x^2}\,dx
 &=
 4a\int_0^1\frac{dx}{1+x^2}
 +4\int_0^1 H'(x)\,dx\\
 &=a\pi+4\bigl(H(1)-H(0)\bigr).
 \end{aligned}
\tag{5}
$$



Adding (4) and (5) proves (2). Two further exact coincidences are



$$
f(i)=f(-i)=a,
\tag{6}
$$



because $1+i^2=0$. Thus (1) may equivalently be written $A(f)=f(i)$.

The weight



$$
w(x)=e^x+\frac{4}{1+x^2}
$$



is positive on $[0,1]$, but the lattice polynomials found below
oscillate. Consequently (2) has no fixed sign, and positivity of the
weight does not supply uniform nonvanishing.

## 3. Exact lattice and the saturation correction

Let the search parameter be $g$, let



$$
H(x)=\sum_{r=1}^{g+1}h_rx^r,
$$



where the irrelevant constant term of $H$ has been normalized to zero,
and put $D=g+2$, so that $\deg f\leq D$. The integer variable vector is



$$
(a,h_1,\ldots,h_{g+1})\in\mathbb Z^D.
$$



The three imposed equations are



$$
A\bigl((1+x^2)H'\bigr)=0,
 \qquad
 f(0)=0,
 \qquad
 f(1)=0.
\tag{7}
$$



They have rank three in the range considered here, so the kernel $K_D$
has rank $D-3$.

For a monomial,



$$
A(x^n)=(-1)^n\,!n,
\tag{8}
$$



where $!n$ is the derangement number. Therefore the coefficient of
$h_r$ in the first equation of (7) is



$$
c_r=r\left(A(x^{r-1})+A(x^{r+1})\right).
\tag{9}
$$



The endpoint equations give



$$
h_1=-\sum_{r=2}^{g+1}2r h_r,
 \qquad
 a=-h_1=\sum_{r=2}^{g+1}2r h_r.
\tag{10}
$$



After substitution, the remaining equation is



$$
\sum_{r=2}^{g+1}(c_r-4r)h_r=0.
\tag{11}
$$



Every coefficient in (11) is even. After division by $2$, the first
three coefficients, for $r=2,3,4$, are respectively



$$
-6,\quad 9,\quad -100,
$$



whose gcd is $1$. Hence the reduced row is primitive for every
$g\geq 3$.

A recorded sequence of extended-gcd column operations sends this primitive
row to $(1,0,\ldots,0)$. The remaining columns are consequently a
saturated $\mathbb Z$-basis of its kernel, and (10) lifts them
bijectively to a saturated basis of $K_D$. This is equivalent to taking
the zero rows of the transformation matrix in a Hermite-normal-form
computation of the transpose of the original constraint matrix.

By contrast, clearing denominators and making each vector of a rational
nullspace basis primitive need not saturate their joint span. The exact
indices of that old sublattice are



$$
\begin{array}{c|ccccc}
g&8&16&24&32&40\\ \hline
\text{index}&24&10368&4478976&644972544&278628139008.
\end{array}
\tag{12}
$$



These are determinantal-divisor, equivalently Smith-normal-form,
computations, not floating-point diagnostics.

## 4. Exact image of the integer-form map

Define



$$
\Phi:K_D\longrightarrow\mathbb Z^2,
 \qquad
 \Phi(f)=(a,b),
$$



where



$$
b=-B(f)+4\bigl(H(1)-H(0)\bigr).
\tag{13}
$$



### Theorem 4.1

For every $g\geq 5$, equivalently $D\geq 7$,



$$
\boxed{\Phi(K_D)=8\mathbb Z\times 2\mathbb Z.}
\tag{14}
$$



### Proof

First, $b$ is even. In



$$
B(f)=\sum_{k\geq 0}(-1)^k k! f_k,
$$



the constant coefficient $f_0$ is zero, the coefficient $f_1$ is
$2h_2$, and every term with $k\geq 2$ contains the even factor $k!$.
Thus $B(f)$ is even, while the second term of (13) is divisible by four.

Next, $a$ is divisible by eight. The recurrence for derangements gives



$$
!n\equiv
 \begin{cases}
 1\pmod 8,&n\ \text{even},\\
 n-1\pmod 8,&n\ \text{odd}.
 \end{cases}
\tag{15}
$$



This follows directly by induction from
$!n=n\,!(n-1)+(-1)^n$: for even $n$, the product
$n(n-2)$ is divisible by eight, and the odd case then follows
immediately. Substitution in (9) gives



$$
c_r\equiv 2r\pmod 8
\tag{16}
$$



for every $r$. Put $z_r=(c_r-4r)/2$. Then



$$
z_r\equiv-r\pmod 4.
$$



Dividing (11) by two and reducing modulo four yields



$$
\sum_{r=2}^{g+1}r h_r\equiv0\pmod 4.
$$



Equation (10) now gives $8\mid a$. We have proved



$$
\Phi(K_D)\subseteq 8\mathbb Z\times 2\mathbb Z.
$$



For $g=5$, the two variable vectors



$$
(8,-8,57626,-102668,38706,7590,-3)
\tag{17}
$$



and



$$
(0,0,-57301,102118,-38505,-7550,3)
\tag{18}
$$



satisfy all three equations (7), and their images are respectively
$(8,0)$ and $(0,2)$. Padding them with zero higher coefficients proves
the reverse inclusion for every $g\geq 5$. This proves (14).
$\square$

The certificate also computes independently, for every integer
$5\leq g\leq 40$, Smith invariants $(2,8)$, coordinate gcds $(8,2)$,
and image index $16$ in $\mathbb Z^2$.

It follows that



$$
\operatorname{rank}\ker\Phi=D-5.
\tag{19}
$$



This large zero-form lattice is essential. An LLL reduction of the full
lattice primarily finds exact representations of
$0\cdot(e+\pi)+0$, not rational approximations to $e+\pi$.
Filtering reduced-basis rows by $a\neq0$ does not turn LLL into a
shortest-vector computation in the rank-two quotient.

## 5. Corrected finite candidates

Write



$$
f(x)=\sum_{k=0}^{D}d_kT_k(2x-1).
$$



Since $\lvert T_k(2x-1)\rvert\leq1$ on $[0,1]$,



$$
\lVert f\rVert_{[0,1]}\leq\sum_k\lvert d_k\rvert.
\tag{20}
$$



Using the saturated kernel gives the following exact finite records. Thus
the probe's search parameters $g=32,40$ correspond to polynomial degrees
$D=34,42$. The last column is certified using rational enclosures from
the exponential series and Machin's arctangent formula; it is not an
uncertified floating-point evaluation.



$$
\begin{array}{c|c|r|r|c|c|c}
g&D&a&b&\sum\lvert d_k\rvert&\gcd(a,b)&a(e+\pi)+b\\ \hline
32&34&-52439838563088&307290871838600&
\dfrac{342075143692469}{36893488147419103232}&8&
-10^{-5}<\cdot<-10^{-6}\\[6pt]
40&42&461515305521655600&-2704421761901323052&
\dfrac{1672003183159179573}{4835703278458516698824704}&4&
10^{-7}<\cdot<10^{-6}
\end{array}
\tag{21}
$$



Thus both displayed forms are rigorously nonzero, but this is only a
finite fact. Dividing by the common gcd is legitimate and materially
improves the finite height normalization. No infinite nonvanishing theorem
is known.

The corrected $D=42$ unnormalized Chebyshev-bound exponent is
approximately $0.366$, where the exponent means



$$
-\frac{\log\left(\sum\lvert d_k\rvert\right)}{\log\lvert a\rvert}.
$$



This decimal is merely a display of an expression in the exact integers
and rationals in (21); it is not an uncertified numerical assertion about
$e+\pi$.

## 6. Exact rank-two quotient metric

The quotient can be audited without LLL. Let $v_1,\ldots,v_r$ be any
saturated basis of $K_D$, where $r=D-3$. Let $E$ be the
$r\times(D+1)$ matrix whose rows are their shifted-Chebyshev coefficient
vectors, and put



$$
G=EE^T.
$$



Let $M$ be the $2\times r$ matrix whose $j$-th column is
$\Phi(v_j)$. The covariance matrix of the two output functionals in this
Euclidean coefficient norm is



$$
S=MG^{-1}M^T.
\tag{22}
$$



Consequently the minimum squared coefficient norm among real vectors
mapping to an output $y\in\mathbb R^2$ is



$$
y^TS^{-1}y.
$$



Using the exact image coordinates $(a,b)=(8u,2v)$, the quotient metric on
$(u,v)\in\mathbb Z^2$ is



$$
\boxed{
 R_D=
 \begin{pmatrix}8&0\\0&2\end{pmatrix}^{\!T}
 S^{-1}
 \begin{pmatrix}8&0\\0&2\end{pmatrix}.}
\tag{23}
$$



Every entry of $R_D$ stored in the certificate is an exact rational
number.

Let



$$
z=2i-1=-1+2i,
 \qquad
 \rho=\left|z-\sqrt{z^2-1}\right|>1,
\tag{24}
$$



where the square-root branch is chosen to make the modulus greater than
one. Eliminating the square root gives



$$
\rho^8-20\rho^6-26\rho^4-20\rho^2+1=0.
\tag{25}
$$



Exact rational sign checks, together with monotonicity of the polynomial
on this interval, certify



$$
\frac{1152895447327}{250000000000}
 <
 \rho
 <
 \frac{4611581789309}{1000000000000}.
\tag{26}
$$



For fixed $u$, the real minimizer of
$(u,v)R_D(u,v)^T$ has slope



$$
\frac vu=-\frac{(R_D)_{01}}{(R_D)_{11}}.
\tag{27}
$$



The following table contains only certified finite comparisons. The middle
column encloses $\det(R_D)\rho^{2D}$ between consecutive integers. The
last column gives the sign and a power-of-ten enclosure for the difference
between (27) and $-4(e+\pi)$, using an exact rational enclosure of
$e+\pi$.



$$
\begin{array}{c|c|c}
D&\det(R_D)\rho^{2D}&-R_{01}/R_{11}+4(e+\pi)\\ \hline
10&(14299,14300)&(10^{-5},10^{-4})\\
18&(6873,6874)&(-10^{-10},-10^{-11})\\
26&(2436,2437)&(10^{-17},10^{-16})\\
34&(901,902)&(-10^{-22},-10^{-23})\\
42&(2450,2451)&(-10^{-27},-10^{-28})
\end{array}
\tag{28}
$$



For the negative intervals, the endpoints indicate sign and absolute
magnitude; the JSON certificate stores the exact ordered rational
endpoints. Formula (28) is strong finite evidence for the quotient
geometry, but it is not an all-$D$ asymptotic theorem.

## 7. Potential-theoretic interpretation and the exponent-one barrier

This section carefully separates exact facts from asymptotic inference.
For the full shifted-Chebyshev coefficient space, evaluation at $i$ has
exponential rate $\rho^D$, because



$$
T_k(2i-1)=\frac12\left(\omega^k+\omega^{-k}\right),
 \qquad
 \lvert\omega\rvert=\rho.
\tag{29}
$$



On the common-kernel subspace, $a=f(i)$. The integration functional



$$
L(f)=\int_0^1w(x)f(x)\,dx=a(e+\pi)+b
\tag{30}
$$



has only subexponential operator-norm growth in the same coefficient
model. Since $b=L-(e+\pi)a$, the two output functionals become nearly
collinear. The exact data in (28) support, but do not prove for all $D$,
the quotient model



$$
\lVert(u,v)\rVert_D^2
 \asymp
 \rho^{-2D}u^2+
 \bigl(4(e+\pi)u+v\bigr)^2,
\tag{31}
$$



up to subexponential factors. Equivalently, this model predicts quotient
covolume of order $\rho^{-D}$ up to subexponential factors.

Under (31), ordinary two-dimensional Minkowski/Dirichlet balancing uses a
denominator cutoff $Q$. It supplies



$$
|u|\lesssim Q,
 \qquad
 |4(e+\pi)u+v|\lesssim Q^{-1}.
$$



The two terms of (31) balance at $Q\asymp\rho^{D/2}$, giving



$$
|u|\asymp\rho^{D/2},
 \qquad
 |4(e+\pi)u+v|\asymp\rho^{-D/2}.
\tag{32}
$$



Since $a=8u$ and



$$
a(e+\pi)+b=2\bigl(4(e+\pi)u+v\bigr),
$$



this generic determinant argument reaches



$$
|a(e+\pi)+b|\asymp |a|^{-1}.
\tag{33}
$$



That is linear-form exponent $1$, equivalently rational-approximation
exponent $2$. The exponential gain in the cheap quotient direction is
spent in allowing the denominator to grow in that same direction.

The logical limitation is exact and important:

- determinant/Minkowski supplies an existence guarantee at exponent $1$
  under the quotient scale (31);
- it supplies no universal lower bound for individual lattice points;
- it therefore does **not** prove that exceptional vectors of exponent
  greater than $1$ are impossible.

To obtain a Roth-breaking sequence one would need, for some fixed
$\varepsilon>0$, infinitely many nonproportional pairs satisfying



$$
0<
 \left|4(e+\pi)u+v\right|
 <
 |u|^{-1-\varepsilon},
\tag{34}
$$



together with integer polynomial representatives whose norms retain that
gain. The strict inequality on the left is the missing uniform
nonvanishing. Neither the full-lattice determinant, LLL, nor positivity of
the kernel proves (34).

## 8. Exact certificate and scope

The companion program

    scripts/common_kernel_lattice_exact_certificate.py

checks with exact integer or rational arithmetic:

1. the constraint matrix and a saturated integer-kernel construction;
2. the old unsaturated-basis indices in (12);
3. the image theorem (14), including every $5\leq g\leq40$ and the two
   all-degree generators (17)--(18);
4. the corrected candidates in (21), including rational enclosures proving
   their finite nonvanishing;
5. the quotient matrices $R_D$ at $D=10,18,26,34,42$;
6. exact determinant hashes, rational slope data, the algebraic enclosure
   (26), and all certified finite comparisons in (28).

Its frozen output is

    results/common_kernel_lattice_exact_certificate.json

The identity, saturation construction, and image statement are
all-degree theorems proved above. The quotient tables are exact finite
records used to diagnose a potential-theoretic model; they are not
substitutes for an unproved asymptotic theorem.
