> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the diagonal Machin free-coefficient theorem and measure comparison

Date: 2026-08-26

## Verdict

**ACCEPT.** I independently rederived the determinant decomposition, the
unique least-valuation term in both residue classes, the competing
determinant bounds, the edge case $n=1$, and the quantitative
$E$-function specializations. I found no mathematical defect in the
frozen source.

The accepted source is
sources/diagonal_machin_free_coefficient_and_measure.md, with SHA-256

22ebb6d23ae62d2c833d3a054456b4c9d52726230af73764e6f8f9b5992f8edd.

The reported supporting hashes were also verified exactly:

* scripts/machin_diagonal_free_coefficient.py:
  7bab16eb94428900484390731f35ea363e491396c2f263a20aae66177f0aca30;
* results/machin_diagonal_free_coefficient.json:
  7dbabc0aea7271a9a724799735efc58007e9a029bc805de484a172e60afca2bf.

A fresh execution of the reported script produced a byte-identical result
file. In addition, I wrote a separate implementation using only Python's
Fraction class, independent row-denominator clearing, and a local Bareiss
determinant routine. It imports neither SymPy nor the reported script. Its
artifacts are

* scripts/independent_diagonal_machin_audit.py;
* results/independent_diagonal_machin_audit.json.

That implementation reproduced every archived determinant digest and every
archived valuation at $n=1,4,5,8,9,12,13,16$. It also exhaustively
enumerated all $D_E$ Laplace summands for $n=1,4,5$.

## 1. Reduction and the exact determinant identity

Let $G=4\Gamma$, where the odd Taylor coefficients of $\Gamma$ are



$$
\gamma_r=(-1)^{(r-1)/2}
\frac{4\,5^{-r}-239^{-r}}{r}
\qquad(r>0\text{ odd}),
$$



and all other coefficients used here are zero. On $B(1)=C(1)$, write



$$
B=x+(z-1)\widetilde B,\qquad
C=x+(z-1)\widetilde C,
$$



with $\deg\widetilde B,\deg\widetilde C<n$. For rows
$k=n+1,\ldots,3n+1$, direct coefficient extraction gives



$$
E_{k,j}=\frac1{(k-j)!},\qquad
P_{k,a}=\frac{k-a-1}{(k-a)!},
$$





$$
\Gamma_{k,j}=\gamma_{k-j},\qquad
Q_{k,a}=\gamma_{k-a-1}-\gamma_{k-a}.
$$



All occurring kernel indices are positive: the smallest is
$n+1-(n-1)-1=1$. Thus no negative-index convention enters the
argument.

Columnwise,



$$
P_a=E_{a+1}-E_a,\qquad
Q_a=\Gamma_{a+1}-\Gamma_a.
$$



The square matrix of the $2n+1$ high rows, in the coordinate order
$(x,\widetilde B,\widetilde C)$, is



$$
\mathcal T_n=(E_0+4\Gamma_0\mid P\mid4Q).
$$



Expanding in the first column gives two terms. In the $E_0$ term,
factoring $4$ from each of the $n$ $Q$-columns and undoing
successive differences changes $(E_0,P)$ into $E$, with determinant
one. This gives $4^nD_E$, where $D_E=\det(E\mid Q)$. In the
$\Gamma_0$ term, one obtains a further factor $4$, moves
$\Gamma_0$ across the $n$ columns of $P$, and then changes
$(\Gamma_0,Q)$ into $\Gamma$. Therefore



$$
\det\mathcal T_n
=4^nD_E+4^{n+1}(-1)^nD_G
=4^n\bigl(D_E+4(-1)^nD_G\bigr),
$$



where $D_G=\det(P\mid\Gamma)$. This independently checks both the
extra factor $4$ and the sign $(-1)^n$.

The accepted all-degree rank theorem leaves a one-dimensional solution
line after imposing rows through $3n$, and every nonzero vector on that
line has $B(1)=C(1)\ne0$. Adding row $3n+1$ is exactly adding the
first free coefficient equation because $A$ has degree at most $n$.
Thus $\det\mathcal T_n\ne0$ is equivalent to nonvanishing of the first
free coefficient on that line.

## 2. Kernel bounds, orientations, and equality cases

Write



$$
\phi(k)=v_2(k!),\qquad
A(q)=\sum_{j=0}^{q-1}\phi(j),\qquad
g_2(q)=\frac{q(q-1)}2+A(q).
$$



For distinct integers of one parity, every difference contains a factor
$2$. Division by these factors reduces the estimate to the ordinary
integral Vandermonde bound. Hence a $q$-point row or pole Vandermonde
has valuation at least $g_2(q)$, with equality for consecutive points
in that parity class.

The accepted Machin stability theorem compares the odd kernel



$$
K_d=\frac{4\,5^{-d}-239^{-d}}d
$$



with a $2$-adic-unit multiple of $1/d$, modulo $16$ after removal
of the universal square or bordered Vandermonde factor. It preserves the
exact valuation of square Cauchy blocks, all bordered lower bounds, and
the bordered equality cases whose normalized raw quotient has valuation
zero or one.

For a bordered block with $s$ ordinary rows and $s+1$ consecutive
pole points, the lower bound is



$$
v_2(V(\text{ordinary rows}))+\beta(s+1),
$$



where, for $q=s+1$ and $z=q-1=s$,



$$
\beta(q)=\frac{z(z-1)}2+A(z)+
\begin{cases}
z,&z\text{ even},\\
z+1,&z\text{ odd}.
\end{cases}
$$



Equality holds for consecutive ordinary rows whenever $s$ is even.
If $s$ is odd, equality holds when the first row-to-pole difference is
$3\pmod4$. These facts are stated for arbitrary row coordinates, so
they apply on the shifted interval $\{n+1,\ldots,3n+1\}$ without an
extra translation-invariance assumption.

For $n=2R$, the pole indices $0,\ldots,n$ have $R+1$ even members
and $R$ odd members. A nonzero $n$-row $Q$-minor has one of the
two lower bounds



$$
L_A=2g_2(R)+g_2(R)+\beta(R+1)
=3g_2(R)+\beta(R+1)
$$



or



$$
L_B=2g_2(R+1)+g_2(R-1)+\beta(R).
$$



Using $g_2(q+1)-g_2(q)=q+\phi(q)$ and the two parity branches of
$\beta$, direct subtraction yields



$$
L_B-L_A=
\begin{cases}
0,&R\text{ odd},\\
2+2v_2(R),&R\text{ even}.
\end{cases}
$$



For $n=2R-1$, both pole parity classes have size $R$. A nonzero
minor has one square block of size $R$ and one bordered block with
$R-1$ ordinary rows, so its common lower bound is



$$
L_C=2g_2(R)+g_2(R-1)+\beta(R).
$$



These are exactly the three kernel bounds used in the frozen source.

## 3. The class $n\equiv0\pmod4$: the unique least term of $D_E$

Let $n=4r$ and $R=n/2=2r$. In the Laplace expansion of $D_E$, an
$(n+1)$-row set $S$ contributes, up to sign,



$$
\det E_S\det Q_{\mathcal X'\setminus S}.
$$



Since $1/(s-j)!=(s)_j/s!$ and the falling factorials are monic,



$$
\det E_S=\pm\frac{V(S)}{\prod_{s\in S}s!},\qquad
v_2(\det E_S)\ge
A(n+1)-\sum_{s\in S}\phi(s).
$$



The sequence $\phi(k)$ is nondecreasing, and its only consecutive
plateaus are $(2m,2m+1)$. The selection boundary is the plateau
$(2n,2n+1)$. Therefore the only two subsets maximizing the factorial
sum are



$$
S_0=\{2n+1,\ldots,3n+1\}
$$



and



$$
S_*=\{2n\}\cup\{2n+2,\ldots,3n+1\}.
$$



For $S_0$, the complement is



$$
U_0=\{n+1,\ldots,2n\}
=\{2R+1,\ldots,4R\}.
$$



It has $R$ rows of each parity. The even rows face the $R$ odd poles
in a square block, while the $R$ odd rows face the $R+1$ even poles
in a bordered block. Both row sets are consecutive in their parity
classes. The bordered ordinary-row count is $s=R$, which is even here.
Thus equality holds:



$$
v_2(\det Q_{U_0})=L_A.
$$



The $E$-rows in $S_0$ are consecutive, so the full summand has
valuation



$$
v_0=A(n+1)-\sum_{k=2n+1}^{3n+1}\phi(k)
+3g_2(R)+\beta(R+1).
$$



Replacing $2n+1$ by $2n$ changes the Vandermonde by the exact factor



$$
\frac{|V(S_*)|}{|V(S_0)|}=n+1.
$$



Here $n+1$ is odd, so the $E$-minor valuation is unchanged. The
complement of $S_*$ has $R-1$ even rows and $R+1$ odd rows, so it
has the other kernel orientation $L_B$. Since $R$ is even, this costs
at least $2+2v_2(R)>0$ beyond $L_A$. Every remaining $S$ loses at
least one in the factorial sum while retaining the universal Vandermonde
and kernel lower bounds. Consequently $S_0$ is the unique
least-valuation summand:



$$
D_E\ne0,\qquad v_2(D_E)=v_0.
$$



A unique least-valuation summand cannot be cancelled in a non-Archimedean
valuation.

## 4. The competing determinant for $n\equiv0\pmod4$

For every $n$-row set $S$, the exponential-difference minor satisfies



$$
v_2(\det P_S)\ge A(n)-\sum_{s\in S}\phi(s).
$$



Among $n$-subsets of $\mathcal X'$, the factorial sum is maximized at



$$
S_G=\{2n+2,\ldots,3n+1\}.
$$



The boundary is strict because
$\phi(2n+2)>\phi(2n+1)$. A structurally nonzero complementary
$(n+1)$-row $\Gamma$-minor contains $R+1$ odd rows and $R$ even
rows, and factors into square Machin blocks of sizes $R+1$ and $R$.
Every Laplace summand of $D_G$ therefore has valuation at least



$$
A(n)-\sum_{k=2n+2}^{3n+1}\phi(k)
+2g_2(R+1)+2g_2(R).
$$



Subtracting $v_0$ leaves



$$
\phi(2n+1)-\phi(n)
+2g_2(R+1)-g_2(R)-\beta(R+1).
$$



For even $R$, direct use of the definitions gives



$$
2g_2(R+1)-g_2(R)-\beta(R+1)=R+2\phi(R).
$$



Hence



$$
v_2(D_G)-v_0\ge
\eta_n:=\phi(2n+1)-\phi(n)+R+2\phi(R)>0.
$$



The convention $v_2(0)=+\infty$ includes a zero $D_G$. Multiplication
by $4$ adds two more to the valuation, so $4D_G$ cannot cancel
$D_E$. Factoring $4^n$ gives



$$
v_2(\det\mathcal T_n)=2n+v_0.
$$



## 5. The class $n\equiv1\pmod4$, including $n=1$

Let $n=4r+1=2R-1$, so $R=2r+1$ is odd. The same two
factorial-maximal sets $S_0,S_*$ occur. For $S_0$,



$$
U_0=\{2R,2R+1,\ldots,4R-2\}
$$



has $R$ even rows and $R-1$ odd rows. The former make a square
block of size $R$, while the latter make a bordered block with
$s=R-1$ ordinary rows. Since $R-1$ is even, the bordered equality
case applies:



$$
v_2(\det Q_{U_0})=L_C.
$$



The $S_0$ summand therefore has valuation



$$
v_1=A(n+1)-\sum_{k=2n+1}^{3n+1}\phi(k)
+2g_2(R)+g_2(R-1)+\beta(R).
$$



For $S_*$, the factorial sum is unchanged but the exact Vandermonde
factor is $n+1=2R$. Because $R$ is odd, $v_2(n+1)=1$. Every
$Q$-minor still has valuation at least $L_C$, so $S_*$ costs at
least one. Every other set loses at least one in the factorial sum. Thus



$$
D_E\ne0,\qquad v_2(D_E)=v_1.
$$



A nonzero complementary $\Gamma$-minor now has $R$ rows of each
parity and splits into two square blocks of size $R$. Hence



$$
v_2(D_G)\ge
A(n)-\sum_{k=2n+2}^{3n+1}\phi(k)+4g_2(R).
$$



For odd $R$,



$$
2g_2(R)-g_2(R-1)-\beta(R)
=(R-1)+2\phi(R-1).
$$



It follows that



$$
v_2(D_G)-v_1\ge
\eta_n^{(1)}:=\phi(2n+1)-\phi(n)
+(R-1)+2\phi(R-1)>0,
$$



and again



$$
v_2(\det\mathcal T_n)=2n+v_1.
$$



For the edge case $n=1$, one has $R=1$. The bordered block has zero
ordinary rows and is the $1\times1$ appended-row determinant $1$, so
$\beta(1)=0$. Also $g_2(0)=A(0)=0$. Directly,
$S_0=\{3,4\}$, $U_0=\{2\}$, and
$Q_{2,0}=\gamma_1$ is a $2$-adic unit. The formulas give



$$
v_1=-4,\qquad
\eta_1^{(1)}=1,\qquad
v_2(\det\mathcal T_1)=-2.
$$



Thus no unspoken positive-block-size assumption excludes $n=1$.

## 6. Independent exact computations

Running the frozen script afresh generated a result with SHA-256

7dbabc0aea7271a9a724799735efc58007e9a029bc805de484a172e60afca2bf,

byte for byte identical to the archived JSON.

The independent Fraction/Bareiss implementation reproduced:

| $n$ | $v_2(D_E)$ | $v_2(D_G)$ | $v_2(\det\mathcal T_n)$ |
|---:|---:|---:|---:|
| 1 | -4 | -3 | -2 |
| 4 | -32 | -24 | -24 |
| 5 | -45 | -36 | -35 |
| 8 | -106 | -88 | -90 |
| 9 | -125 | -106 | -107 |
| 12 | -210 | -184 | -186 |
| 13 | -243 | -216 | -217 |
| 16 | -358 | -320 | -326 |

For every row, the independently computed reduced rational values of
$D_E,D_G,\det\mathcal T_n$ had exactly the same three SHA-256 digests
as the corresponding archived record. The determinant identity held as
an exact rational equality, not only after applying $v_2$.

Exhaustive $D_E$ Laplace enumeration gave:

| $n$ | total terms | zero terms | least valuation | next distinct valuation | unique minimizing actual row set |
|---:|---:|---:|---:|---:|---|
| 1 | 3 | 0 | -4 | -3 | $\{3,4\}$ |
| 4 | 126 | 26 | -32 | -29 | $\{9,10,11,12,13\}$ |
| 5 | 462 | 112 | -45 | -44 | $\{11,12,13,14,15,16\}$ |

These finite checks validate the implementation; the proof above is
all-degree in the two residue classes.

## 7. The nested Padé form

Under the temporary hypothesis



$$
s=e+\pi\in\overline{\mathbb Q},\qquad
d=[\mathbb Q(s):\mathbb Q],
$$



the field $K=\mathbb Q(i,s)$ has degree $h=2d$: the embedded field
$\mathbb Q(s)$ is real and cannot contain $i$.

For



$$
P_n(z)=\sum_{k=0}^n
\frac{(2n-k)!}{k!(n-k)!}z^k,\qquad
Q_n(z)=P_n(-z),
$$



the classical Padé identity is



$$
Q_n(z)e^z-P_n(z)
=\frac{(-1)^nz^{2n+1}}{n!}
\int_0^1t^n(1-t)^ne^{tz}\,dt.
$$



Because $e^{is}=e^{i(e+\pi)}=-e^{ie}$, the frozen form



$$
\Lambda_n=-Q_n(ie)e^{is}-P_n(ie)
$$



is $Q_n(ie)e^{ie}-P_n(ie)$. Rotating the integral by $e^{-ie/2}$,
its real part has integrand
$t^n(1-t)^n\cos(e(t-1/2))$. This cosine is at least
$\cos(e/2)>0$ on $[0,1]$, proving nonvanishing and the stated
two-sided beta-integral bound.

Let



$$
a_{n,k}=\frac{(2n-k)!}{k!(n-k)!}.
$$



These are positive integers, and



$$
\frac{a_{n,k+1}}{a_{n,k}}
=\frac{n-k}{(k+1)(2n-k)}<1.
$$



Therefore



$$
\widetilde F_n(X,Y)=-Q_n(X)Y-P_n(X)
$$



has integer coefficients, exact total degree $D_n=n+1$, and exact
height



$$
H_n=a_{n,0}=\frac{(2n)!}{n!}.
$$



## 8. Adamczewski--Faverjon specialization

I checked Theorem A and equation (6.1) in the cited primary paper.

The functions



$$
f_1(z)=ie^z,\qquad f_2(z)=e^{isz}
$$



are $E$-functions over $K$ and form a solution of



$$
Y'=\operatorname{diag}(1,is)Y.
$$



The matrix is constant, so $z=1$ is regular. The functions are
algebraically independent over $\overline{\mathbb Q}(z)$. Expanding a
hypothetical polynomial relation gives exponential parts with exponents
$m+nis$. Distinct pairs $(m,n)$ give distinct exponents because a
real rational number cannot cancel a nonzero purely imaginary rational
multiple of $s$. Exponentials with distinct constant exponents are
linearly independent over $\overline{\mathbb Q}(z)$. One direct proof
takes a relation with the fewest terms, clears denominators, and applies
a first-order differential operator annihilating one term. Minimality
would force the logarithmic derivative of a ratio of two rational
coefficients to equal a nonzero constant, which is impossible.

Theorem A therefore applies directly to
$\widetilde F_n(f_1(1),f_2(1))$. Equation (6.1) gives, for $m$
functions and total polynomial degree $D$,



$$
C_1(D)=\exp\!\left(
-\exp\!\left(C_3D^{2m}\log(D+1)\right)\right),
\qquad
C_2=\sqrt m\,4^m h^{m+1}.
$$



Here $C_3$ depends on the fixed functions and evaluation point, not on
$D$. Substituting $m=2$, $h=2d$, and $D=n+1$ gives



$$
C_2=\sqrt2\,4^2(2d)^3=128\sqrt2\,d^3.
$$



Theorem A has height factor $H^{-C_2D^m}$. Taking logarithms yields
exactly



$$
\log|\Lambda_n|\ge
-\exp\!\left(C_3(n+1)^4\log(n+2)\right)
-128\sqrt2\,d^3(n+1)^2\log H_n.
$$



Thus the total-degree power, field-degree power, double exponential in
$C_1$, and numerical coefficient are all correct. The pair of
functions is fixed once the conditional algebraic number $s$ is fixed,
so this bound is uniform in $n$. Its scale is still too weak: the
height term alone is of order $-n^3\log n$, whereas the actual Padé
logarithm is of order $-n\log n$.

The source's Stirling expansions also check:



$$
\log H_n=n\log n+(2\log2-1)n+O(\log n),
$$





$$
-\log|\Lambda_n|
=n\log n-(3-2\log2)n+O(\log n),
$$



so their quotient tends to one.

## 9. Fischler--Rivoal specialization and nonuniformity

Fischler--Rivoal's published Theorem 1 states that for a number field of
degree $h$, a vector of $N$ $E$-functions over that field satisfying
a first-order system, and a nonzero algebraic-integer linear form of
coefficient house at most $H$,



$$
|\Lambda|>cH^{-hN^h+1-\varepsilon}.
$$



The theorem explicitly writes
$c=c(\varepsilon,K,z_0,f_1,\ldots,f_N)$. No linear independence or
regular-point assumption is required once the evaluated linear form is
separately known to be nonzero.

Writing $a_{n,k}$ as above gives the exact expansion



$$
\Lambda_n
=-\sum_{k=0}^na_{n,k}i^ke^k
-\sum_{k=0}^na_{n,k}(-i)^ke^{k+is}.
$$



It uses $N_n=2n+2$ functions



$$
e^{kz}\quad(0\le k\le n),\qquad
e^{(k+is)z}\quad(0\le k\le n).
$$



They satisfy a diagonal first-order system over $K$. Their coefficients
in the linear form are Gaussian integers. Every embedding of $K$ sends
$i$ to $\pm i$, so their house is at most $H_n$. With $h=2d$,
Theorem 1 gives exactly



$$
|\Lambda_n|>
c_{n,\varepsilon}
H_n^{-2d(2n+2)^{2d}+1-\varepsilon}.
$$



The subscript $n$ on the constant is essential. Both the dimension and
the full function list change with $n$, and these objects are explicit
dependencies of $c$ in the primary theorem. The theorem supplies no
uniform positive lower control on $c_{n,\varepsilon}$ along this
sequence. Even deleting the constant would leave a height exponent of
order $n^{2d}$, far larger than the limiting exponent one of the actual
Padé forms.

If $s\in\mathbb Q$, the coefficient field is the imaginary quadratic
field $\mathbb Q(i)$. The Shidlovskii theorem quoted in the introduction
of the same Fischler--Rivoal paper gives exponent
$N_n-1+\varepsilon=2n+1+\varepsilon$. Its constant still depends on the
varying function vector, and even without that issue the permitted
logarithmic size is of order $-n^2\log n$.

Finally, the cited 2025 Fischler--Rivoal theorem is a one-value measure
for $P(e^\alpha)$. Its v1 statement permits coefficients in the ring
of integers of a number field, a slightly broader class than
$P\in\mathbb Z[X]$, but this does not change the nonapplication.
Freezing $e^{is}$ leaves coefficients involving the transcendental
number $e$, while freezing $e$ leaves coefficients involving the
transcendental number $e^{is}$. Neither gives an algebraic-coefficient
polynomial in one exponential value.

## 10. Primary sources checked

* B. Adamczewski and C. Faverjon, Algebraic Independence Measures for
  Values of E-functions and M-functions, arXiv:2502.09999v1, Theorem A
  and Section 6.1.1, equation (6.1):
  <https://arxiv.org/abs/2502.09999>.
* S. Fischler and T. Rivoal, Values of E-functions are not Liouville
  numbers, Journal de l'Ecole polytechnique -- Mathematiques 11 (2024),
  Theorem 1 and the introductory Theorem A:
  <https://www.numdam.org/articles/10.5802/jep.249/>.
* S. Fischler and T. Rivoal, A new transcendence measure for the values
  of the exponential function at algebraic arguments,
  arXiv:2502.17992v1, Theorem 1:
  <https://arxiv.org/abs/2502.17992>.

## 11. Exact limitation

The accepted theorem proves exact Taylor order $3n+1$ for
$n\equiv0,1\pmod4$. It does not prove endpoint nonvanishing, endpoint
smallness, or the needed primitive-height/content estimate. The measure
comparisons likewise show that the cited quantitative theorems do not
contradict the constructed Padé forms. Nothing in this audit proves that
$e+\pi$ is algebraic or transcendental.
