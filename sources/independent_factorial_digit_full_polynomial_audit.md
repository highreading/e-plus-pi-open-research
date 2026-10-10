> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the full polynomial-$C$ factorial-digit family

## 1. Verdict and scope

Let



$$
d_n=\lfloor n!\pi\rfloor-n\lfloor (n-1)!\pi\rfloor\quad(n\geq2),
 \qquad
 G(z)=3+\sum_{n\geq2}d_n\frac{z^n}{n!}.
\tag{1}
$$



For nonnegative $a,b,c$, put $M=a+b+c+1$ and consider



$$
\deg A\leq a,\quad \deg B\leq b,\quad \deg C\leq c,
 \qquad
 A+Be^z+CG=O(z^M),\quad B(1)=C(1).
\tag{2}
$$



An implementation independent of the exploratory scan reconstructed all



$$
\sum_{T=0}^{18}\binom{T+2}{2}=\binom{21}{3}=1330
\tag{3}
$$



systems with $a+b+c\leq18$.  The exact verdict is:

* every bordered jet matrix has full row rank and nullity one;
* exactly five kernel lines have the entire endpoint pair
  $(A(1),B(1))=(0,0)$;
* the smallest nonzero reduced endpoint in the full box occurs at
  $(8,2,0)$, and the smallest one with $c>0$ occurs at $(8,3,1)$;
* a separate high-jet block and tail formula reproduces the endpoint pair
  exactly for every nonsingular high block;
* 597 stable-range Schur-complement identities were checked exactly.

This is an exact finite certificate and an all-degree structural reduction.
It is **not** an all-degree nonvanishing theorem.  In fact, an all-degree
full-rank theorem for this family would imply the presently unknown
irrationality of $e+\pi$; see Section 8.

## 2. Integral jet matrix

Write



$$
g_0=3,\qquad g_1=0,\qquad g_n=d_n\ (n\geq2),
 \qquad q_n=1+g_n.
\tag{4}
$$



Thus $g_n=G^{(n)}(0)$, while $q_n$ is the $n$-th jet of
$e^z+G(z)$.  Use ordinary monomial coefficients



$$
A=\sum_{j=0}^a A_jz^j,\qquad
 B=\sum_{j=0}^b B_jz^j,\qquad
 C=\sum_{j=0}^c C_jz^j.
\tag{5}
$$



After multiplying the $k$-th Taylor equation by $k!$, its entries are



$$
k!\,[z^k]A=k!A_k,\qquad
 k!\,[z^k](Be^z)=\sum_{j\leq\min(b,k)}k^{\underline j}B_j,
\tag{6}
$$



and



$$
k!\,[z^k](CG)
 =\sum_{j\leq\min(c,k)}k^{\underline j}g_{k-j}C_j.
\tag{7}
$$



Together with the integral endpoint row



$$
\sum_{j=0}^bB_j-\sum_{j=0}^cC_j=0,
\tag{8}
$$



these give an $(a+b+c+2)\times(a+b+c+3)$ integer matrix.  No
floating-point rank decision is involved.

The independent implementation computes the exact rational nullspace,
clears denominators, and divides the ordinary integer content of the full
coefficient vector.  If



$$
\alpha=A(1),\qquad \beta=B(1)=C(1),
\tag{9}
$$



it separately divides $(\alpha,\beta)$ by its endpoint gcd.  Thus the
reported form is the primitive integer form



$$
\alpha+\beta(e+\pi).
\tag{10}
$$



## 3. The square high-jet block

Suppose first that the common target coefficient $\beta\neq0$, and scale
the kernel line so that $\beta=1$.  There are unique polynomials



$$
T(z)=\sum_{j=0}^{b-1}t_jz^j,\qquad
 S(z)=\sum_{j=0}^{c-1}s_jz^j
\tag{11}
$$



such that



$$
B(z)=1+(z-1)T(z),\qquad
 C(z)=1+(z-1)S(z).
\tag{12}
$$



Empty sums cover $b=0$ or $c=0$.  Define



$$
u_j(k)=k^{\underline j}(k-j-1)\qquad(0\leq j<b)
\tag{13}
$$



and



$$
v_j(k)=k^{\underline j}
 \bigl((k-j)g_{k-j-1}-g_{k-j}\bigr)
 \qquad(0\leq j<c).
\tag{14}
$$



When $k<j$, the falling factorial makes the entry zero.  For $k=j$,
the parenthesis in (14) means $-g_0$.  These are the jets of



$$
z^j(z-1)e^z\quad\hbox{and}\quad z^j(z-1)G(z),
\tag{15}
$$



respectively.  Put $N=b+c$, let the rows be indexed by
$k=a+1,\ldots,a+N$, and define



$$
\mathcal H_{a,b,c}
 =\bigl(u_0,\ldots,u_{b-1},v_0,\ldots,v_{c-1}\bigr),
 \qquad
 y=(q_{a+1},\ldots,q_{a+N})^{\mathsf T}.
\tag{16}
$$



The high equations in (2) are exactly



$$
\mathcal H_{a,b,c}\theta=-y,\qquad
 \theta=(t_0,\ldots,t_{b-1},s_0,\ldots,s_{c-1})^{\mathsf T}.
\tag{17}
$$



If



$$
D_{a,b,c}=\det\mathcal H_{a,b,c}\neq0,
\tag{18}
$$



then



$$
\theta=-\mathcal H_{a,b,c}^{-1}y.
\tag{19}
$$



There is an important logical distinction.  Provided the full bordered
matrix has nullity one, $D_{a,b,c}=0$ is equivalent to
$\beta=B(1)=C(1)=0$: a null vector of the homogeneous high block gives a
kernel with zero common target coefficient, and conversely.  It does
**not** in general imply $A(1)=0$.  The finite scan has six singular high
blocks but only five zero endpoint pairs; Section 6 gives the exception.

## 4. Exact tail and adjugate endpoint formula

Define the integral Taylor numerator



$$
P_a=a!\sum_{n=0}^a\frac{q_n}{n!}
\tag{20}
$$



and



$$
x_a=a!(e+\pi)-P_a.
\tag{21}
$$



For $a\geq1$,
$P_a=\lfloor a!e\rfloor+\lfloor a!\pi\rfloor$; at $a=0$, the
required Taylor numerator is $P_0=4$.

The columns in (15) telescope at $z=1$:



$$
a!\sum_{k>a}\frac{u_j(k)}{k!}
 =\begin{cases}a^{\underline j},&j\leq a,\\0,&j>a,\end{cases}
\tag{22}
$$



and



$$
a!\sum_{k>a}\frac{v_j(k)}{k!}
 =\begin{cases}a^{\underline j}g_{a-j},&j\leq a,\\0,&j>a.\end{cases}
\tag{23}
$$



Indeed, after division by $k!$, (14) is



$$
\frac{g_{k-j-1}}{(k-j-1)!}-\frac{g_{k-j}}{(k-j)!},
\tag{24}
$$



so (23) telescopes.  Let $w$ be the row vector formed by the right sides
of (22), followed by the right sides of (23).

The low equations say that $-A$ is the Taylor truncation through degree
$a$ of $Be^z+CG$.  Since the latter has value $e+\pi$ at one,
(19), (22), and (23) give



$$
e+\pi+A(1)
 =\frac{x_a+w\theta}{a!}
 =\frac{x_a-w\mathcal H_{a,b,c}^{-1}y}{a!}.
\tag{25}
$$



Writing



$$
R_{a,b,c}=-A(1)
\tag{26}
$$



therefore gives the exact rational approximant



$$
\boxed{
 R_{a,b,c}
 =\frac{P_a+w\mathcal H_{a,b,c}^{-1}y}{a!}.}
\tag{27}
$$



Equivalently, set



$$
W_{a,b,c}=a!D_{a,b,c},\qquad
 Z_{a,b,c}=P_aD_{a,b,c}
       +w\operatorname{adj}(\mathcal H_{a,b,c})y.
\tag{28}
$$



Both are integers and $R=Z/W$.  If



$$
h_{a,b,c}=\gcd(W_{a,b,c},Z_{a,b,c}),
\tag{29}
$$



then, up to overall sign, the reduced endpoint form is



$$
\boxed{
 -\frac{Z_{a,b,c}}{h_{a,b,c}}
 +\frac{W_{a,b,c}}{h_{a,b,c}}(e+\pi).}
\tag{30}
$$



The script checked (30) against the independently generated full polynomial
kernel for every nonsingular block in the $T\leq18$ box.

## 5. Schur reduction to a $c$ by $c$ digit determinant

Assume



$$
b\geq1,\qquad a\geq\max(1,b-1).
\tag{31}
$$



Partition the first $b$ and last $c$ rows, and the $u$- and
$v$-columns, as



$$
\mathcal H_{a,b,c}
 =\begin{pmatrix}U_0&V_0\\U_1&V_1\end{pmatrix}.
\tag{32}
$$



The fixed-$b$ determinant identity gives



$$
\det U_0=\kappa_bD_{a,b},\qquad
 \kappa_b=\prod_{j=0}^{b-1}j!,\qquad
 D_{a,b}=\frac{\Delta^b(a!)}{a!}>0.
\tag{33}
$$



Consequently



$$
\boxed{
 \det\mathcal H_{a,b,c}
 =\kappa_bD_{a,b}\,
  \det\bigl(V_1-U_1U_0^{-1}V_0\bigr).}
\tag{34}
$$



The remaining determinant is only $c$ by $c$.  It consists of the
residuals obtained by interpolating each factorial-digit column by the
fixed $u$-space on the first $b$ nodes and evaluating at the last
$c$ nodes.  Formula (34) separates the positive fixed-$b$ factor from
the genuinely arithmetic digit determinant.  This explains why $c=0$
has a uniform rank proof whereas $c>0$ introduces digit-dependent
cancellations.

## 6. Six singular blocks but only five zero endpoint pairs

The exact singular high blocks through total degree $18$ are



$$
(0,1,0),\ (1,0,1),\ (1,0,2),\ (1,1,1),\
 (2,0,1),\ (2,0,2).
\tag{35}
$$



At $(0,1,0)$, the kernel is



$$
A=1,\qquad B=z-1,\qquad C=0.
\tag{36}
$$



Indeed, $1+(z-1)e^z=O(z^2)$.  Here $\beta=0$, as block singularity
predicts, but the endpoint pair is $(A(1),\beta)=(1,0)$, not zero.

The other five singular blocks have zero endpoint pair.  Their exact origin
is the initial factorial-digit gap



$$
G(z)-3=O(z^4),
\tag{37}
$$



because $d_2=d_3=0$.  For $r=0,1$,



$$
-3z^r(z-1)+z^r(z-1)G(z)
 =z^r(z-1)(G(z)-3)=O(z^{r+4}).
\tag{38}
$$



For $r=0$, the minimal box is $(1,0,1)$, whose required order is
three.  One unit of degree slack is allowed before the required order
exceeds four, giving



$$
(1,0,1),\ (2,0,1),\ (1,1,1),\ (1,0,2).
\tag{39}
$$



For $r=1$, the minimal box $(2,0,2)$ already requires order five,
exactly the order supplied by (38).  These are the five zero endpoint
records.  Their primitive coefficient vectors are in the JSON result.

## 7. Exact finite minima

After excluding the five zero endpoint pairs, the global winner is



$$
(a,b,c)=(8,2,0),\qquad
 (\alpha,\beta)=(-20533,3504),
\tag{40}
$$



with



$$
\bigl|-20533+3504(e+\pi)\bigr|
 =0.000185099130012275549714631107498368\ldots.
\tag{41}
$$



Its exact rational enclosure is strictly separated from every other
nonzero record; the runner-up by exact lower bound is $(6,8,0)$.

Among records with $c>0$, the winner is



$$
(a,b,c)=(8,3,1),\qquad
 (\alpha,\beta)=(-74239453,12669120),
\tag{42}
$$



and



$$
\bigl|-74239453+12669120(e+\pi)\bigr|
 =0.00198541951452043025096254091617366\ldots.
\tag{43}
$$



Its exact interval is strictly separated from every other $c>0$ record;
the runner-up by exact lower bound is $(14,3,1)$.

The enclosures use the independent identity



$$
\pi=4\bigl(\arctan(1/2)+\arctan(1/3)\bigr)
\tag{44}
$$



with exact alternating-series remainders, together with a positive rational
tail bound for $e$.  The same rational interval certifies every required
factorial floor, every nonzero sign, and both minimum comparisons.

## 8. Why an all-degree theorem is difficult

The determinant in (34) is built from actual factorial digits of $\pi$.
There is no known positivity mechanism for it.  More sharply, this family
encodes the open rationality problem for the target.

If $e+\pi$ were rational, its canonical combined factorial expansion
would imply



$$
d_n=n-2
\tag{45}
$$



for all sufficiently large $n$.  But the $n$-th jet of
$(z-2)e^z$ is $n-2$.  Hence



$$
P(z)=G(z)-(z-2)e^z
\tag{46}
$$



would be a polynomial.  The exact identity



$$
-P(z)+(2-z)e^z+G(z)=0
\tag{47}
$$



satisfies endpoint matching because $2-1=1$.  Multiplying (47) by any
polynomial $R(z)$ preserves both the identity and endpoint matching:



$$
-R(z)P(z)+R(z)(2-z)e^z+R(z)G(z)=0.
\tag{48}
$$



For degree boxes large enough to contain every $R$ of degree at most
$r$, these give $r+1$ independent kernel vectors.  Thus a claim that
every bordered matrix in all degrees has nullity one would itself prove
$e+\pi\notin\mathbb Q$.  Even the weaker claim that every sufficiently
large endpoint pair is nonzero would rule out rationality.

Accordingly, the $T\leq18$ scan gives useful exact data and
(27)--(34) give a reusable structural reduction, but neither can be
extrapolated into an unconditional all-degree rank or nonvanishing theorem.

## 9. Reproducibility

The independent implementation and complete record are

* <scripts/independent_factorial_digit_full_polynomial_audit.py>;
* <results/independent_factorial_digit_full_polynomial_T18.json>.

The JSON contains all 1330 matrix and kernel hashes, exact endpoint pairs,
every high-block determinant, the six singular-block records, the five
explicit zero-endpoint kernels, exact minimum enclosures, and the 597
Schur-complement checks.  Re-running the script reproduces the result
byte-for-byte.
