> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The augmented root-of-unity determinant after endpoint normality

## A shifted-coordinate theorem, exact completely-monotone reductions, and
## the remaining confluent-Newton positivity lemma

Checked: 2026-08-27 UTC

## 1. Verdict

This note continues, in new files, the frozen audit
`sources/root_unity_gamma_logistic_minor_audit.md`.  None of the frozen source,
script, or result is modified here.

Put



$$
h=n+1,\qquad
 \Phi(X)=\prod_{j=0}^{m-1}(X-j)^h,\qquad
 c=\frac{m-1}{2},                                           \tag{1}
$$



and let



$$
K_{q,a}=\mathcal L\!\left(((X-c)^q\Phi)^{(a)}\right),
 \quad 0\le q\le D-2,\quad0\le a\le D.                    \tag{2}
$$



The preceding audit proved $\operatorname {rank}K=D-1$ and reduced
nonvanishing of the two-column correction $\Gamma$ to one bordered minor.
The present continuation gives three additional exact results.

1.  The coordinate row in that border is never redundant.  More precisely,
    the submatrix of (2) on

    

$$
q\equiv mn\pmod2,\qquad a=2,4,\ldots                 \tag{3}
$$



    has full possible row rank for every $m\ge1$ and
    $n\ge D\ge2$.  Consequently evaluation $C\mapsto C(0)$ is nonzero
    on the even endpoint kernel.  This is an all-parameter theorem, proved
    below by a totally nonnegative coefficient Toeplitz matrix and
    Andreief's identity.

2.  Outside the parity defect, the other factor of the bordered determinant
    is exactly a divided-difference determinant for a rational function
    $\rho_{m,n}$.  Strict complete monotonicity of $\rho_{m,n}$ on
    $(0,\infty)$ proves the border nonzero.  The central-pole issue for odd
    $m$ disappears after subtracting the known central cardinal value before
    integrating by parts.

3.  Complete monotonicity has an entirely algebraic sufficient certificate.
    Write

    

$$
\rho(x)=\frac{N(x)}{\prod_{j=1}^{p}(x+\lambda_j)},
      \qquad0<\lambda_1\le\cdots\le\lambda_p.               \tag{4}
$$



    If

    

$$
N(x)=\sum_{d=0}^{p-1}\gamma_d
      \prod_{j=1}^{d}(x+\lambda_j),\qquad \gamma_d>0,        \tag{5}
$$



    then

    

$$
\rho(x)=\sum_{d=0}^{p-1}
      \frac{\gamma_d}{\prod_{j=d+1}^{p}(x+\lambda_j)}       \tag{6}
$$



    is the Laplace transform of a strictly positive sum of convolutions of
    exponential kernels.  Thus $\rho$ is strictly completely monotone.

The exact certificate proves (5), coefficient by coefficient over
$\mathbb Q$, for all generic tuples



$$
2\le m\le10,\qquad2\le n\le7,                              \tag{7}
$$



and for every parity-defect $\Lambda_1$ tuple in that range.  This is an
exact finite theorem, not a positivity sample.

The all-parameter statement still missing is now particularly clean:

> **Confluent-Newton positivity lemma needed.**  The three explicit cardinal
> numerators in Sections 4 and 7 have strictly positive coefficients in the
> ordered Newton bases with repeated square nodes described there, for all
> $m,n$ in their stated parity ranges.

This lemma would prove $\Gamma\ne0$ for every $m\ge2$.  It is not proved
here.  A tempting stronger pointwise-integrand argument is false: at
$(m,n)=(8,3)$, one natural simple-pole quotient already has a negative
residue.  The full integrated rational function nevertheless has a positive
Newton/Coxian certificate.  Hence cancellations in the integral cannot be
discarded.

For $m=1$, the exact classification from the preceding module audit is:



$$
\boxed{\Gamma=0\quad\Longleftrightarrow\quad
        n\text{ is even and }D\text{ is odd}.}               \tag{8}
$$



Those are polynomial-multiple degeneracies, not genuine two-column
inheritance.

No conclusion about the arithmetic nature of $e+\pi$ is claimed here.

The replayable files are

* `scripts/root_unity_gamma_augmented_newton_certificate.py`;
* `results/root_unity_gamma_augmented_newton_certificate.json`.

## 2. The shifted coordinate minor

The row $e_0^T$ in the generic border is independent of $K$ exactly when
the even-column block remains full row rank after column $a=0$ is deleted.
In the defect case the even kernel has dimension two; the same deletion must
still leave the original even-column block with full row rank.  Both claims
follow from one shifted-minor theorem.

> **Shifted-coordinate theorem.**  Let $n\ge D\ge2$.  Select the rows
> $q\equiv mn\pmod2$ of (2), and select the first equally many columns from
> $a=2,4,\ldots,D$.  The resulting square determinant is nonzero.

### 2.1 Even number of frequencies

Let $m=2k$, and put



$$
W(x)=\prod_{r=1}^{k}
 \left(x+\left(r-\frac12\right)^2\right)^h
      =\sum_{j=0}^{p}w_jx^j.                                 \tag{9}
$$



On the centered contour $X=c+it$, an even selected row has, up to a fixed
nonzero phase,



$$
p_u(t)=t^{2u}W(t^2).                     \tag{10}
$$



For column $a=2+2v$, integrate only $a-2=2v$ times.  The derivative of
the hyperbolic kernel is then the initial degree-$v$ polynomial in
$\tanh^2(\pi t)$, while the row function is $p_u''(t)$.  Writing
$x=t^2$,



$$
[x^j]p_u''(\sqrt x)
   =(2j+2)(2j+1)w_{j+1-u}.                                   \tag{11}
$$



Thus, after a positive column scaling, the coefficient matrix is a submatrix
of the Toeplitz matrix



$$
T_{u,j}=w_{j-u}.                     \tag{12}
$$



### 2.2 Odd number of frequencies

Let $m=2k+1$.  For an even column, the selected row parity is
$q\equiv n\pmod2$.  If $q=q_0+2u$, $q_0\in\{0,1\}$, then on the
centered contour



$$
p_u(t)=t^{2u+1}W(t^2),                                      \tag{13}
$$



where



$$
W(x)=x^{(n+q_0)/2}\prod_{r=1}^{k}(x+r^2)^h.                \tag{14}
$$



After the same partial integration, divide the odd function $p_u''(t)$ by
the common positive factor $t$.  Its coefficient formula is



$$
[x^j]\frac{p_u''(\sqrt x)}{\sqrt x}
   =(2j+3)(2j+2)w_{j+1-u}.                                   \tag{15}
$$



This is again a positive column scaling of the Toeplitz matrix (12).
Integration by parts at zero is legitimate: stopping two integrations early
only improves the boundary exponent in the estimate from the frozen csch
proof.  In particular, every intermediate boundary term tends to zero since
$a\le n$.

### 2.3 Total nonnegativity and strictness

The polynomial $W$ in (9) or (14) is a product of factors $x$ and
$x+\alpha$ with $\alpha>0$.  Its coefficient Toeplitz matrix is a product
of shift matrices and nonnegative bidiagonal Toeplitz matrices.  Cauchy--Binet
therefore proves that (12) is totally nonnegative.  This is the elementary
finite Pólya-frequency argument; no unproved global total-positivity assertion
about the logistic matrix is used.

For consecutive rows $u=0,\ldots,r-1$, the maximal coefficient minor on the
top $r$ available degrees is triangular with positive diagonal $w_p$.
It is therefore strictly positive.  The generalized monomial collocation
matrix



$$
(x_j^{\ell})_{\ell,j},qquad
          0<x_1<\cdots<x_r,                                  \tag{16}
$$



is strictly totally positive.  A second Cauchy--Binet expansion now shows
that the collocation determinant of the row functions in (11) or (15) has
one strict sign.

The column functions after partial integration have degrees
$0,1,\ldots,r-1$ in $\tanh^2(\pi t)$ or
$\coth^2(\pi t)$.  Their determinant is a nonzero leading-coefficient
factor times a Vandermonde.  Andreief's identity therefore gives a strictly
signed integral.  This proves the shifted-coordinate theorem.

It follows immediately that $e_0^T$ is nonzero on the even endpoint kernel,
both in the ordinary one-dimensional even line and in the two-dimensional
even defect kernel.

## 3. Hermite-cardinal polynomials via CRT

Let $\Lambda_b$ be the unique polynomial of degree less than $mh$ such
that



$$
\Lambda_b^{(a)}(j)=(-1)^j\delta_{a,b},qquad
 0\le j<m,\quad0\le a\le n.                                 \tag{17}
$$



Equivalently, in the polynomial Chinese-remainder ring,



$$
\Lambda_b(X)\equiv
 \frac{(-1)^j}{b!}(X-j)^b\pmod{(X-j)^h}.                    \tag{18}
$$



Formula (18) is how the certificate constructs the cardinal rows.  It avoids
numerical inversion of a confluent Vandermonde matrix and proves every jet
identity exactly.

Reflection about $c$ gives



$$
\Lambda_0(c+U)=
 \begin{cases}
  \text{odd in }U,&m\text{ even},\\
  \text{even in }U,&m\text{ odd},
 \end{cases}                                                  \tag{19}
$$



and, when $m$ is odd,



$$
\Lambda_1(c+U)\text{ is odd in }U.   \tag{20}
$$



These parity statements are exact consequences of uniqueness in (17).

## 4. The two generic completely-monotone rational functions

### 4.1 Even $m$

Let $m=2k$.  By (19), define $N_{m,n}\in\mathbb Q[x]$ by



$$
\Lambda_0(c+U)=U N_{m,n}(-U^2).                 \tag{21}
$$



Put



$$
B_m(x)=\prod_{r=1}^{k}
 \left(x+\left(r-\frac12\right)^2\right),\qquad
 \rho_{m,n}(x)=\frac{N_{m,n}(x)}{B_m(x)^h}.                  \tag{22}
$$



A harmless global sign is chosen so that the first nonzero Newton coefficient
below is positive.  The numerator has exact degree $kh-1$, one less than
the denominator.

### 4.2 Odd $m$

Let $m=2k+1$, put



$$
q_0\equiv h\pmod2,\quad q_0\in\{0,1\},\qquad
 s=\frac{h+q_0}{2},\qquad \epsilon=(-1)^k.                  \tag{23}
$$



The cardinal conditions at the central node and parity imply



$$
\Lambda_0(c+U)-\epsilon=U^{2s}N_{m,n}(-U^2).          \tag{24}
$$



Define



$$
B_m(x)=\prod_{r=1}^{k}(x+r^2),\qquad
 \rho_{m,n}(x)=\frac{N_{m,n}(x)}{B_m(x)^h}.                  \tag{25}
$$



Here $U^{q_0}\Phi(c+U)$, not $\Phi(c+U)$ alone, is the base row in the
relevant odd-column block.  Its central factor is $U^{h+q_0}=U^{2s}$, so
(25) is exactly the ratio of the cardinal row to the first ordinary row.
Again $\deg N_{m,n}=kh-1$.

## 5. Why complete monotonicity proves the generic border

Outside the defect, the endpoint space is one even line plus one odd line.
The constant coefficient of $\Gamma$ is, up to nonzero factors, the product
of the shifted coordinate minor from Section 2 and the odd-column block
augmented by $E_0$.

For even $m$, integrate every odd column $a=1,3,\ldots$ all the way.  The
ordinary centered rows are



$$
t^{2u+1}B_m(t^2)^h,                         \tag{26}
$$



and the cardinal row is $tN_{m,n}(t^2)$, up to fixed phases.  Factoring the
positive common row weight leaves



$$
\rho_{m,n}(x),1,x,\ldots.             \tag{27}
$$



The column determinant is a Vandermonde in $\tanh^2(\pi t)$.

For odd $m$, replace $\Lambda_0$ by
$\Lambda_0-\Lambda_0(c)$.  This does not change any odd derivative in
$E_0$, and (24) shows that it vanishes to order at least $h$ at the
central pole.  Full integration by parts is therefore boundary-free.  The
same factorization gives (27), now with a Vandermonde in
$\coth^2(\pi t)$.

If $\rho$ is strictly completely monotone, then for
$0<x_1<\cdots<x_r$,



$$
\det\begin{pmatrix}
  \rho(x_1)&\cdots&\rho(x_r)\\
  1&\cdots&1\\
  x_1&\cdots&x_r\\
  \vdots&&\vdots\\
  x_1^{r-2}&\cdots&x_r^{r-2}
 \end{pmatrix}                                                \tag{28}
$$



has one strict sign.  Indeed it is a Vandermonde times the divided difference
$\rho[x_1,\ldots,x_r]$, and the Hermite--Genocchi formula gives the sign
$(-1)^{r-1}$.  Andreief's identity applied to (28) and the column
Vandermonde proves the augmented block nonzero.

Thus strict complete monotonicity of (22) or (25), together with the proved
coordinate theorem, implies the generic bordered minor is nonzero.

## 6. Ordered Newton coefficients and a positive inverse-Laplace density

For even $m$, list



$$
\frac14\ (h\text{ times}),\quad
 \frac94\ (h\text{ times}),\quad\ldots,\quad
 \left(k-\frac12\right)^2\ (h\text{ times}).                \tag{29}
$$



For odd $m$, list



$$
1\ (h\text{ times}),\quad4\ (h\text{ times}),\quad\ldots,
 \quad k^2\ (h\text{ times}).                              \tag{30}
$$



Call the resulting nondecreasing list $\lambda_1,\ldots,\lambda_p$, where
$p=kh$.  The exact finite phenomenon is



$$
N_{m,n}(x)=\sum_{d=0}^{p-1}\gamma_d
             \prod_{j=1}^{d}(x+\lambda_j),qquad\gamma_d>0. \tag{31}
$$



Dividing (31) by the full denominator proves (6).  Each term in (6) is the
Laplace transform of the convolution



$$
e^{-\lambda_{d+1}t}*\cdots*e^{-\lambda_pt},                 \tag{32}
$$



which is strictly positive for $t>0$.  Hence (31) is a finite exact
complete-monotonicity certificate.  It also gives a positive Coxian
state-space realization; mixed ordinary partial-fraction residues do not
invalidate it.

The certificate verifies all $\gamma_d>0$ over $\mathbb Q$ throughout
(7).  The claim for arbitrary $m,n$ is precisely the missing
confluent-Newton lemma, not an inference from this grid.

## 7. The parity-defect row

In the defect, $m=2k+1$, $n$ is odd, $h=n+1$ is even, and $D$ is
even.  Both endpoint directions are even.  After expanding the linear
bordered minor along $e_0^T$, the remaining augmented row is $E_1$ on
columns $a=2,4,\ldots$.

Put $s=h/2$ and $\epsilon=(-1)^k$.  The central cardinal conditions give



$$
\Lambda_1(c+U)-\epsilon U
       =U^{h+1}N^{(1)}_{m,n}(-U^2).                           \tag{33}
$$



Define



$$
\rho^{(1)}_{m,n}(x)=
 \frac{N^{(1)}_{m,n}(x)}{\prod_{r=1}^{k}(x+r^2)^h}.          \tag{34}
$$



Integrate each even column only $a-1$ times.  The derivative-polynomial
columns are then the initial odd sequence and have a Vandermonde determinant
after the common $\coth(\pi t)$ factor is removed.  The ordinary row
functions and (33) are all first derivatives of



$$
t\,x^sB_m(x)^h x^u,qquad
 t\,x^sN^{(1)}_{m,n}(x),qquad x=t^2.                        \tag{35}
$$



Coefficientwise, differentiation multiplies column $x^j$ by the same
positive factor $2j+1$.  Therefore it is enough that the coefficient matrix
of



$$
x^sN^{(1)}_{m,n}(x),\quad
 x^sB_m(x)^h,\quad x^{s+1}B_m(x)^h,\ldots                    \tag{36}
$$



be totally nonnegative with one strict maximal minor.

There is an elementary Newton-to-Toeplitz lemma.  If $D=\prod(x+\lambda_j)$
and $N$ has the nonnegative Newton expansion (5), then the coefficient
matrix with first row $N$ and subsequent rows $D,xD,\ldots$ is totally
nonnegative.  For one Newton basis term $B_d=\prod_{j\le d}(x+\lambda_j)$,
factor $B_d$ from every row.  Its coefficient Toeplitz matrix is totally
nonnegative, while the remaining matrix has first row $1$ and shifted rows
of $D/B_d$, another coefficient Toeplitz matrix.  Cauchy--Binet proves the
claim; positive linear combination in the first row gives (5).  The highest
Newton coefficient supplies a strict triangular minor.

Apply the lemma after prefixing the rate list by $s$ zero rates.  Equation
(36), the positive column scaling, monomial collocation, and Andreief then
prove the defect border nonzero whenever $N^{(1)}_{m,n}$ has strictly
positive Newton coefficients at the repeated nodes



$$
-1,-1,\ldots,-4,-4,\ldots,-k^2.             \tag{37}
$$



The exact certificate verifies this for all defect tuples in (7).  Universal
positivity in (37) is the third part of the missing lemma.

## 8. An exact integral formula and a false stronger shortcut

For even $m=2k$, put



$$
P(U)=\prod_{r=1}^{k}(U^2-a_r^2),\qquad a_r=r-\frac12.       \tag{38}
$$



The flat cardinal jets imply



$$
\Lambda_0'(c+U)=P(U)^nQ(U),
                  \qquad\deg Q\le2k-2.                      \tag{39}
$$



Since $\Lambda_0(c)=0$, integration on the imaginary segment gives the
exact identity



$$
\rho_{m,n}(x)\doteq
 \int_0^1
 \frac{\widetilde Q(t^2x)
       \prod_{r=1}^{k}(a_r^2+t^2x)^n}
      {\prod_{r=1}^{k}(a_r^2+x)^{n+1}}\,dt,                 \tag{40}
$$



where $\widetilde Q(x)\doteq Q(i\sqrt x)$ and $\doteq$ absorbs one
global nonzero sign.  Exact grids show that $\widetilde Q$ has positive
coefficients after this normalization.

One may rewrite the integrand as



$$
\frac{\widetilde Q(t^2x)}{\prod_r(a_r^2+t^2x)}
 \prod_r\left(
 t^2+(1-t^2)\frac{a_r^2}{a_r^2+x}
 \right)^{n+1}.                                               \tag{41}
$$



The product in (41) is completely monotone.  It would therefore suffice if
$\widetilde Q(x)/\prod_r(a_r^2+x)$ were completely monotone.  That
sufficient condition is false in general, even though the integral is
completely monotone in every certified tuple.

At $(m,n)=(8,3)$, one exact normalization is



$$
\widetilde Q(x)=
 \frac{652253888x^3+11401671120x^2+57327324516x+89430640551}
 {1519668456468750}.                                         \tag{42}
$$



The residues of
$\widetilde Q(x)/\prod_{r=1}^{4}(x+(r-\tfrac12)^2)$, in increasing pole
order, are



$$
\frac{94751528}{273540322164375},\quad
 -\frac{37276184}{422130126796875},\quad
 \frac{539717768}{6838508054109375},\quad
 \frac{450364792}{4884648610078125}.                         \tag{43}
$$



Thus a pointwise-in-$t$ proof based only on (41) cannot cover all odd
$n$.  The positive Coxian expansion of the integrated $\rho$, rather than
positivity of every integrand factor, is the exact surviving target.

## 9. Exact replay and logical scope

The certificate performs the following operations over $\mathbb Q$.

1.  It constructs $\Lambda_0$ and the required $\Lambda_1$ directly by
    polynomial CRT and verifies every jet in (17).
2.  It verifies the centered parity and divisibility factorizations
    (21), (24), and (33).
3.  It computes every confluent Newton coefficient in (31), proves it is
    strictly positive by exact rational comparison, and reconstructs the
    numerator exactly.  Cross-multiplication of (6) is exactly this Newton
    reconstruction.
4.  On a smaller determinant grid it verifies the shifted coordinate minor
    and the appropriate generic or defect bordered minor directly.

The generic Newton grid is (7); the defect grid consists of the odd $m,n$
tuples in (7).  The direct determinant grid is



$$
2\le m\le6,\qquad2\le n\le5,
 \qquad2\le D\le\min(5,n).                                  \tag{44}
$$



The shifted-coordinate theorem is proved for all parameters in Section 2.
The finite certificate does not promote (31) to an all-parameter theorem.
Closing that one confluent-Newton positivity lemma would prove all remaining
bordered determinants, but an arithmetic contradiction for $e+\pi$ would
still require the endpoint height/value comparison from the companion norm
audit.
