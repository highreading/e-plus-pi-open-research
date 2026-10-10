> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Endpoint tails, arithmetic height, and degree regimes for the Machin family

Date: 2026-08-26

This note studies the endpoint-matched Hermite--Padé construction based on

$$
G(z)=16\arctan(z/5)-4\arctan(z/239),\qquad G(1)=\pi. \tag{1}
$$

It is important to separate three scopes.

* The exact tail, integral, contour, and coefficient-height inequalities in
  Sections 1--4 hold for arbitrary degree bounds $(a,b,c)$ and any rational
  solution satisfying the stated order and endpoint conditions.  The
  coefficient-tail formulas additionally assume $M>\max\{a,b,c\}$, as
  stated where they are used; the Peano and contour formulas need only
  $M>a$.
* The all-degree rank theorem and the cofactor height bound in Section 5 are
  for the diagonal family $a=b=c=n$.
* Section 6 proves an independent all-degree no-decay result for one explicit
  non-diagonal ray, $(a,b,c)=(N-1,1,1)$ with odd $N$.  It is not a no-go
  theorem for all non-diagonal slopes.

The principal new analytic fact is that the *combined* Machin tail has a
known sign and sharp first-omitted-term scale $5^{-L}/L$.  The principal
arithmetic obstruction remains endpoint normalization: in the diagonal
family, an additional determinant/gcd must be controlled before polynomial
coefficient heights can be compared with that analytic scale.

## 1. Exact combined tails

Write

$$
G(z)=\sum_{r\geq0}g_rz^r,                         \tag{2}
$$

where $g_r=0$ for even $r$ and, for positive odd $r$,

$$
g_r=\frac{(-1)^{(r-1)/2}}r
\left(\frac{16}{5^r}-\frac4{239^r}\right).       \tag{3}
$$

For $L\geq1$, let $o(L)$ be the least odd integer not smaller than $L$, and
put

$$
E_L=\sum_{r=L}^{\infty}\frac1{r!},                \tag{4}
$$

$$
T_L(x)=\sum_{\substack{r\geq L\\r\text{ odd}}}
\frac{(-1)^{(r-1)/2}}{r x^r},\qquad x>1,          \tag{5}
$$

$$
U_L=16T_L(5)-4T_L(239).                           \tag{6}
$$

Thus $U_L$ is exactly the tail of $G(1)=\pi$ beginning at index $L$.

Let $o=o(L)=2h+1$.  Termwise integration of the absolutely convergent
geometric series gives

$$
T_L(x)=(-1)^h x^{-o}
\int_0^1\frac{t^{o-1}}{1+t^2/x^2}\,dt.            \tag{7}
$$

Define

$$
I_o(x)=\int_0^1\frac{t^{o-1}}{1+t^2/x^2}\,dt.    \tag{8}
$$

Then

$$
\frac{x^2}{x^2+1}\frac1o\leq I_o(x)\leq\frac1o. \tag{9}
$$

Consequently the two terms in (6) have the same alternating sign before
their fixed subtraction, and the $x=5$ term strictly dominates.

**Theorem 1.1 (sharp signed Machin tail).**  For every $L\geq1$, with
$o=o(L)=2h+1$,

$$
(-1)^hU_L>0,                                      \tag{10}
$$

and

$$
\boxed{
\frac1o\left(\frac{200}{13}\,5^{-o}-4\,239^{-o}\right)
\leq |U_L|\leq\frac{16}{o5^o}.}                  \tag{11}
$$

Moreover, as $o\to\infty$,

$$
\boxed{
U_L=(-1)^h\frac{200}{13}\frac{5^{-o}}o
\left(1+O\!\left(\frac1o\right)
        +O\!\left((5/239)^o\right)\right).}     \tag{12}
$$

**Proof.**  Substitute (7) into (6).  The lower bound for the first term
and the upper bound for the second in (9) give the left side of (11); it is
positive already at $o=1$, and its dominance only increases with $o$.  The
upper bound in (11) follows by discarding the positive subtracted
$239$-term and using $I_o(5)\leq1/o$.

For (12), integration by parts gives, for
$f_x(t)=(1+t^2/x^2)^{-1}$,

$$
I_o(x)=\frac{f_x(1)}o-\frac1o\int_0^1t^of_x'(t)\,dt
=\frac{x^2}{x^2+1}\frac1o+O_x(o^{-2}).           \tag{13}
$$

Since $16\cdot25/26=200/13$, substitution in (6) proves (12). $\square$

This improves the earlier coefficientwise estimate with constant $25$:
the exact combined alternating tail has the uniform bound $16/(o5^o)$ and
a nonzero leading constant.  There is no hidden cancellation between the
$5$- and $239$-parts of a *single* tail.

## 2. Arbitrary degree triples: tail and integral formulas

Let

$$
\deg A\leq a,\qquad \deg B\leq b,\qquad\deg C\leq c, \tag{14}
$$

and suppose $M>a$ and

$$
R(z)=A(z)+B(z)e^z+C(z)G(z)=O(z^M),\qquad C(1)=B(1). \tag{15}
$$

Write

$$
B(z)=\sum_{j=0}^b b_jz^j,\qquad
C(z)=\sum_{j=0}^c c_jz^j.                         \tag{16}
$$

Because $G$ has radius of convergence $5$, all endpoint series below are
absolutely convergent.  The low coefficients of $Be^z+CG$ are canceled by
$A$, and those from $a+1$ through $M-1$ vanish.

For the coefficient-tail formulas in the rest of this section, assume in
addition that

$$
M>\max\{a,b,c\}.                                  \tag{16a}
$$

Hence

**Proposition 2.1 (exact endpoint tail).**

$$
\boxed{
R(1)=\sum_{j=0}^b b_jE_{M-j}
    +\sum_{j=0}^c c_jU_{M-j}.}                    \tag{17}
$$

Using Taylor's integral remainder for $e^z$ and (7), this is equivalently

$$
R(1)=\int_0^1e^tP(t)\,dt
+16\int_0^1\frac{Q_5(t)}{1+t^2/25}\,dt
-4\int_0^1\frac{Q_{239}(t)}{1+t^2/239^2}\,dt,   \tag{18}
$$

where

$$
P(t)=\sum_{j=0}^b
\frac{b_j(1-t)^{M-j-1}}{(M-j-1)!},               \tag{19}
$$

$$
Q_x(t)=\sum_{j=0}^c c_j
(-1)^{(o(M-j)-1)/2}x^{-o(M-j)}t^{o(M-j)-1}.      \tag{20}
$$

These are exact identities, not estimates.

For the diagonal family $a=b=c=n$, $M=3n+1$, equation (19) factors as

$$
P_n(t)=(1-t)^{2n}\sum_{j=0}^n
\frac{b_j(1-t)^{n-j}}{(3n-j)!}.                  \tag{21}
$$

The Machin polynomials contain the opposite endpoint factor.  With
$c_{-1}=0$,

$$
\begin{aligned}
Q_{x,n}(t)={}&(-1)^nc_nx^{-(2n+1)}t^{2n}\\
&+\sum_{\substack{0\leq j\leq n\\j\equiv M\pmod2}}
(-1)^{(M-j)/2}(c_{j-1}+c_j)
x^{-(M-j+1)}t^{M-j}.
\end{aligned}                                    \tag{22}
$$

In particular,

$$
Q_{x,n}(t)=t^{2n}\widetilde Q_{x,n}(t^2).         \tag{23}
$$

Equation (22) also displays an exact cancellation mechanism: adjacent
coefficients enter through $c_{j-1}+c_j$.  Therefore even a large lower
bound for individual coefficient heights cannot by itself give a lower
bound for the endpoint tail.  This is why a $239$-adic coefficient-height
lower bound is not an Archimedean no-go theorem.

There is also a Peano-kernel representation, valid for all degrees in
(14)--(15):

$$
R(1)=\frac1{(M-1)!}\int_0^1(1-t)^{M-1}
\frac{d^M}{dt^M}\bigl(B(t)e^t+C(t)G(t)\bigr)\,dt. \tag{24}
$$

## 3. Exact contour representation and the singularity barrier

The function $G$ is analytic in $|z|<5$.  If $\Gamma$ is a positively
oriented contour in that disk enclosing $0$ and $1$, the residue theorem
gives

$$
\boxed{
R(1)=\frac1{2\pi i}\int_\Gamma
\frac{B(z)e^z+C(z)G(z)}{z^M(z-1)}\,dz.}           \tag{25}
$$

Indeed, the residues at $1$ and $0$ are respectively the endpoint value of
$Be^z+CG$ and the negative sum of its first $M$ Taylor coefficients.

For $1<\rho<5$, put

$$
S_d(\rho)=\sum_{j=0}^d\rho^j,\qquad
\mathcal G(\rho)=16\operatorname{arctanh}(\rho/5)
                 +4\operatorname{arctanh}(\rho/239).         \tag{26}
$$

On $|z|=\rho$, the absolutely convergent arctangent series gives
$|G(z)|\leq\mathcal G(\rho)$.  Therefore

$$
\boxed{
|R(1)|\leq
\frac{\rho^{1-M}}{\rho-1}
\left(e^\rho H_BS_b(\rho)
      +\mathcal G(\rho)H_CS_c(\rho)\right),}      \tag{27}
$$

where $H_B=\max|b_j|$ and $H_C=\max|c_j|$.

The restriction $\rho<5$ is intrinsic to this contour argument: the nearest
logarithmic branch points are $z=\pm5i$.  Faster convergence of a Machin
formula improves the analytic base, but it does not remove the separate
arithmetic-height obligation.

## 4. Endpoint-gcd normalization and the sharp sufficient threshold

Choose a primitive integral polynomial triple on a rational solution line
whose endpoint pair $(A(1),B(1))$ is not $(0,0)$, and write

$$
a_*=A(1),\qquad b_*=B(1)=C(1),\qquad
g=\gcd(|a_*|,|b_*|).                              \tag{28}
$$

The endpoint-primitive form is

$$
\ell=\alpha+\beta(e+\pi)=\frac{R(1)}g,qquad
\alpha=\frac{a_*}g,\quad\beta=\frac{b_*}g.        \tag{29}
$$

Define the effective, endpoint-normalized polynomial heights

$$
H_B^*=\frac{\max|b_j|}g,qquad
H_C^*=\frac{\max|c_j|}g.                          \tag{30}
$$

These may be rational because the endpoint gcd need not divide every
polynomial coefficient.  Applying (17) after division by $g$, the standard
factorial-tail bound

$$
E_K\leq\frac{K+1}{K K!},                          \tag{31}
$$

and Theorem 1.1 gives the following arbitrary-degree result, under the
tail-index hypothesis $M>\max\{a,b,c\}$ from (16a).

**Theorem 4.1 (normalized tail threshold).**  Put

$$
K_E=M-b,qquad K_G=M-c,qquad O_G=o(K_G).          \tag{32}
$$

Then

$$
\boxed{
|\ell|\leq
H_B^*(b+1)\frac{K_E+1}{K_EK_E!}
+H_C^*(c+1)\frac{16}{O_G5^{O_G}}.}                \tag{33}
$$

In particular, along any sequence of degree triples, the two conditions

$$
H_B^*(b+1)\frac{K_E+1}{K_EK_E!}\longrightarrow0, \tag{34}
$$

$$
\boxed{
\frac{16H_C^*(c+1)}{O_G5^{O_G}}\longrightarrow0} \tag{35}
$$

are sufficient for $\ell\to0$.  If the forms are also nonzero eventually,
this would prove irrationality of $e+\pi$.

For the dimension-balanced choice

$$
M=a+b+c+1,                                        \tag{36}
$$

the minimum tail indices are exactly

$$
K_E=a+c+1,qquad K_G=a+b+1.                       \tag{37}
$$

Thus increasing the degree of $C$ alone does not improve the Machin-tail
exponent.  A non-diagonal search must make $a+b$ grow and must prove that
the *effective* height after endpoint-gcd removal is

$$
H_C^*(c+1)=o\!\left(O_G5^{O_G}\right).            \tag{38}
$$

For the diagonal family, $O_G=2n+1$, so (38) is, up to polynomial factors,

$$
H_C^*=o(5^{2n}).                                  \tag{39}
$$

Failure to establish (34)--(35), or proof that the right side of (33) grows,
does **not** prove that the actual form grows: (22) permits cancellation.
Equations (33)--(39) identify the exact sufficient target and the limitation
of the absolute-tail method; they are not converses.

The contour estimate gives the parallel balanced-degree criterion.  Since
$S_d(\rho)<\rho^{d+1}/(\rho-1)$, equation (27), after division by $g$,
implies

$$
|\ell|<\frac1{(\rho-1)^2}
\left(e^\rho H_B^*\rho^{1-a-c}
      +\mathcal G(\rho)H_C^*\rho^{1-a-b}\right). \tag{40}
$$

For every fixed $\rho<5$, subcritical effective heights relative to
$\rho^{a+c}$ and $\rho^{a+b}$ suffice.  The sharp tail theorem recovers the
limiting analytic base $5$.

## 5. What is diagonal-specific: rank, denominators, and a coarse height bound

Now specialize to

$$
a=b=c=n,qquad M=3n+1.                            \tag{41}
$$

The theorem in `machin_bordered_rank_proof.md` proves for every $n$ that the
high Taylor equations and $C(1)=B(1)$ have a one-dimensional rational
solution space and that every nonzero solution has

$$
B(1)=C(1)\ne0.                                    \tag{42}
$$

No corresponding all-degree rank assertion is being made here for arbitrary
$(a,b,c)$.

There is an explicit universal denominator/height bound.  Put

$$
q=5\cdot239=1195,qquad L_n=n!q^n,qquad m=n+1.    \tag{43}
$$

Multiply the high coefficient row with index $k$, $n+1\leq k\leq3n$, by

$$
s_k=k!q^k.                                        \tag{44}
$$

The exponential entries become $(k)_jq^k$.  For $r=k-j$ odd, the Machin
entry is integral because

$$
s_kg_r=
4(-1)^{(r-1)/2}\frac{k!}{r}q^j(4\,239^r-5^r),   \tag{45}
$$

and $r\mid k!$.  Together with the integral endpoint row, this defines an
integer matrix $J_n$ of full row rank.

Let $w$ be its primitive integral cofactor kernel vector in the $B,C$
coordinates.  The row bounds

$$
|(k)_j q^k|\leq k^nq^k,qquad
|s_kg_{k-j}|\leq20k!q^k                          \tag{46}
$$

and Hadamard's inequality give

$$
\max_j|w_j|\leq W_n,                              \tag{47}
$$

where

$$
W_n=(2m)^{n+1/2}q^{n(4n+1)}
\prod_{k=n+1}^{3n}\max\{k^n,20k!\}.             \tag{48}
$$

The multiplier $L_n$ clears all low coefficients of $A$: for $r\leq n$,
$r\mid n!$ and $q^r\mid q^n$.  Since $|g_r|<4$ for every $r\geq1$, one
obtains a nonzero integral polynomial triple of height at most

$$
\boxed{
H_n^{\rm pol}\leq5mL_nW_n.}                     \tag{49}
$$

Making the triple primitive or removing the endpoint gcd can only reduce
this upper bound.  It is therefore an unconditional all-degree height bound,
but it is of size $\exp(O(n^2\log n))$, far above the required scale
$5^{2n}$ in (39).  A large universal upper bound does not prove that the
actual primitive height is large; it only shows that this elementary
denominator estimate cannot establish decay.

The exact missing normalization can again be expressed by cofactors.  Let

$$
u_B=(1,\ldots,1\mid0,\ldots,0),                  \tag{50}
$$

let $u_A$ be the integral row $L_nA(1)$ as a functional of $B,C$, and put

$$
\Delta_B=\det\begin{pmatrix}J_n\\u_B\end{pmatrix},\qquad
\Delta_A=\det\begin{pmatrix}J_n\\u_A\end{pmatrix}.           \tag{51}
$$

The cofactor lemma gives

$$
\frac{A(1)}{B(1)}=\frac{\Delta_A}{L_n\Delta_B}.  \tag{52}
$$

Hence, up to common sign, the primitive endpoint pair is

$$
\alpha_n=\frac{\Delta_A}{h_n},\qquad
\beta_n=\frac{L_n\Delta_B}{h_n},\qquad
h_n=\gcd(|\Delta_A|,L_n|\Delta_B|).              \tag{53}
$$

For every prime $p$, with the convention $v_p(0)=+\infty$ and with the
right side interpreted as $0$ when $\Delta_A=0$,

$$
v_p(\beta_n)=
\max\{0,v_p(L_n\Delta_B)-v_p(\Delta_A)\}.        \tag{54}
$$

Thus the exact unresolved diagonal arithmetic term is $\Delta_A$, or
equivalently the endpoint gcd $h_n$ and the effective heights in (30).  The
all-degree rank theorem proves $\Delta_B\ne0$ but supplies no asymptotic for
(53).  The degree-$65$ counterexample in `machin_239_endpoint_audit.md`
shows why a finite $239$-adic pattern cannot be substituted for such an
asymptotic.

## 6. A rigorous non-diagonal no-decay ray

The arbitrary-degree threshold does not itself decide whether a particular
non-diagonal family succeeds.  The following ray can be solved completely
enough to prove that it does not.

Let $N\geq1$ be odd and choose

$$
(a,b,c)=(N-1,1,1),\qquad M=N+2.                  \tag{55}
$$

Put

$$
D=N^2+N-1,qquad X=N!g_N.                         \tag{56}
$$

The two high Taylor equations have indices $N,N+1$.  Together with the
endpoint equation, they have the following kernel vector:

$$
b_0=X(N+1)(X+N+1),                                \tag{57}
$$

$$
b_1=-X^2(N+1)-X(N+2),                             \tag{58}
$$

$$
c_0=X(N^2-1)-1,\qquad c_1=XN+1.                  \tag{59}
$$

Direct substitution gives

$$
b_0+b_1=c_0+c_1=XD\ne0.                          \tag{60}
$$

This is the unique line.  Indeed, after multiplying the two Taylor rows by
$N!$ and $(N+1)!$, the minor in columns $b_0,b_1,c_0$ is

$$
1+NX.                                             \tag{61}
$$

It cannot vanish: if $X=-1/N$, their $239$-adic valuations would give
$v_{239}(N!)=N$, whereas Legendre's formula gives $v_{239}(N!)<N$.

Let

$$
\varepsilon_N=(e+\pi)+\frac{A(1)}{B(1)}.         \tag{62}
$$

This is the scale-free endpoint error.  Since $N+1$ is even,
$U_{N+1}=U_{N+2}$.  Also
$E_{N+1}=1/(N+1)!+E_{N+2}$.  Substitution of (57)--(60) in the exact tail
formula yields

$$
\boxed{
\varepsilon_N=E_{N+2}+U_{N+2}
-\frac{g_N}{D}
-\frac{N+2}{D(N+1)!}.}                           \tag{63}
$$

The signs of $U_{N+2}$ and $-g_N/D$ agree.  Theorem 1.1, while the
factorial terms are negligible, therefore gives the nonzero asymptotic

$$
\boxed{
\varepsilon_N=(-1)^{(N+1)/2}
\frac{200}{13}\frac{5^{-(N+2)}}{N+2}
\left(1+O\!\left(\frac1N\right)\right).}         \tag{64}
$$

Now put $p=239$ and take the infinite subsequence

$$
N_k=1+2p^k\qquad(k\geq1).                        \tag{65}
$$

For every positive odd $r$,

$$
v_p(g_r)=-r-v_p(r),                               \tag{66}
$$

because $4p^r-5^r$ is a $p$-adic unit.  From (63), or by subtracting
$e+\pi$, the rational endpoint ratio is

$$
\frac{A(1)}{B(1)}=
-\sum_{r=0}^{N+1}\frac1{r!}
-\sum_{r=0}^{N+1}g_r
-\frac{g_N}{D}
-\frac{N+2}{D(N+1)!}.                            \tag{67}
$$

The signs in (67) are worth making explicit:
$E_{N+2}-e=-\sum_{r=0}^{N+1}1/r!$ and
$U_{N+2}-\pi=-\sum_{r=0}^{N+1}g_r$.  Thus (67) is not subject to a
choice of endpoint-ratio convention.

For $N=N_k$, one has

$$
N\equiv1,\quad N+1\equiv2,\quad D\equiv1\pmod p. \tag{68}
$$

The coefficient $1+1/D=N(N+1)/D$ multiplying the final $g_N$ contribution
in (67) is therefore a $p$-adic unit, and that contribution has valuation
$-N$.

Every earlier odd $r<N$ has larger valuation.  To see this, put
$v=v_p(r)$.  If $v\leq k$, then
$N-r\equiv1\pmod{p^v}$; since $N-r$ is positive and even,

$$
N-r\geq p^v+1>v.                                 \tag{69}
$$

If $v>k$, then $r\geq p^{k+1}>1+2p^k=N$, which is impossible.  Hence
$r+v_p(r)<N$, and (66) is strictly larger than $-N$.  Finally,
$v_p((N+1)!)<N$, so all exponential and remaining factorial terms in (67)
also have valuation greater than $-N$.  Thus

$$
\boxed{
v_{239}\!\left(\frac{A(1)}{B(1)}\right)=-N
\quad(N=1+2\cdot239^k).}                         \tag{70}
$$

If $(\alpha_N,\beta_N)$ is the reduced endpoint pair, equation (70) says

$$
v_{239}(\alpha_N)=0,qquad v_{239}(\beta_N)=N.   \tag{71}
$$

Combining (64) and (71), for all sufficiently large $k$,

$$
|\alpha_N+\beta_N(e+\pi)|
=|\beta_N\varepsilon_N|
\geq c\,\frac{(239/5)^N}{N}\longrightarrow\infty \tag{72}
$$

for an absolute $c>0$.  Therefore the endpoint-primitive forms on the ray
$(N-1,1,1)$ do **not** tend to zero: a sequence that diverges on the
subsequence (65) cannot converge to zero on the full odd-$N$ ray.  This
does **not** assert that the forms diverge at every odd $N$.

### 6.1 The exact obstruction for general odd $N$

The preceding $239$-adic argument extends to every odd $N$ except for an
explicit leading-residue exceptional set.  This gives a useful all-degree
statement, but it also shows exactly why the tempting unique-dominant-term
proof cannot simply be asserted for all odd $N$.

For arbitrary odd $N$, put

$$
a_N=v_p(N+1),\qquad d_N=v_p(D),\qquad
W_*(N)=N-a_N+d_N,                                \tag{73}
$$

and, for positive odd $r<N$,

$$
w(r)=r+v_p(r),\qquad
W_N=\max\left(W_*(N),\max_{\substack{1\leq r<N\\r\ {\rm odd}}}w(r)\right).
                                                               \tag{74}
$$

Write $\bar r=r/p^{v_p(r)}\pmod p$, and use a bar on the other $p$-adic
units below as well.  Define the following completely explicit residue in
$\mathbf F_p$:

$$
\begin{aligned}
\mathcal C_N={}&
\sum_{\substack{1\leq r<N,\ r\ {\rm odd}\\w(r)=W_N}}
(-1)^{(r-1)/2}\bar r^{-1}\\
&+\mathbf 1_{W_*(N)=W_N}(-1)^{(N-1)/2}
\overline{\frac{N+1}{p^{a_N}}}\,
\overline{\frac{D}{p^{d_N}}}^{\,-1}.
\end{aligned}                                    \tag{75}
$$

The harmless common factor $4$ has been suppressed in (75).

**Proposition 6.1 (all odd degrees outside an exact exceptional set).**
If $\mathcal C_N\ne0$ in $\mathbf F_{239}$, then

$$
\boxed{
v_{239}\!\left(\frac{A(1)}{B(1)}\right)=-W_N,\qquad
v_{239}(\beta_N)=W_N
\geq N-\lfloor\log_{239}(N+1)\rfloor.}           \tag{76}
$$

Consequently the endpoint-primitive form has the lower bound

$$
|\alpha_N+\beta_N(e+\pi)|
\geq c\,\frac{239^{\,N-\lfloor\log_{239}(N+1)\rfloor}}
               {5^N N}                          \tag{77}
$$

for every sufficiently large odd $N$ with $\mathcal C_N\ne0$.

**Proof.**  In (67), combine the two occurrences of $g_N$.  Their
coefficient is

$$
-\left(1+\frac1D\right)=-\frac{N(N+1)}D,
$$

so their combined valuation is $-W_*(N)$.  Each earlier $-g_r$ has
valuation $-w(r)$.  After multiplication by $p^{W_N}$, reducing the terms
of least valuation modulo $p$, and using

$$
p^{r+v_p(r)}g_r
\equiv-4(-1)^{(r-1)/2}\bar r^{-1}\pmod p,
$$

and, directly,

$$
p^{W_*(N)}
\left(-\frac{N(N+1)}Dg_N\right)
\equiv4(-1)^{(N-1)/2}
\overline{\frac{N+1}{p^{a_N}}}\,
\overline{\frac D{p^{d_N}}}^{\,-1}\pmod p,
$$

one obtains exactly $4\mathcal C_N$.

The rational exponential terms cannot join this leading residue.  Indeed,
Legendre's bound and the definition of $a_N$ give

$$
v_p((N+1)!)\leq\frac{N+1}{p-1}<N-a_N.            \tag{78}
$$

For $a_N=0$, $(N+1)/(p-1)<N$ is immediate.  For $a_N\geq1$, the difference
$N-a_N-(N+1)/(p-1)$ is increasing as a function of $N$ and, at
$N=p^{a_N}-1$, equals
$p^{a_N}-1-a_N-p^{a_N}/(p-1)>0$ for $p=239$.
Thus the factorial terms in (67), including the one with denominator
$D(N+1)!$, have denominator exponent strictly less than $W_*(N)$.  If
$\mathcal C_N\ne0$, no leading cancellation occurs, proving the equality
in (76).  The lower bound follows from
$W_N\geq W_*(N)\geq N-\lfloor\log_p(N+1)\rfloor$, and (77) follows from
(64).  $\square$

Accordingly, the exceptional set

$$
\mathcal E=\{N\geq1:N\ {\rm odd},\ \mathcal C_N=0
              \text{ in }\mathbf F_{239}\}       \tag{79}
$$

is a precise finite-congruence obstruction to (76), not a numerical
heuristic.  It is nonempty.  Take

$$
u=161,\qquad r=p^2u=9\,196\,481,\qquad
N=r+2=9\,196\,483.
$$

Here $N<p^3$, $a_N=d_N=0$, and the only terms attaining $W_N=N$ are the
combined final term and $r=N-2$, for which $v_p(r)=2$.  Since

$$
u^{-1}\equiv144,\qquad
\frac{N+1}{D}\equiv\frac35\equiv144\pmod{239},
$$

their signs are opposite and

$$
\mathcal C_N\equiv144+95\equiv0\pmod{239}.       \tag{80}
$$

Thus the leading numerator congruence really can vanish.  At such an $N$
one only obtains
$v_p(A(1)/B(1))>-W_N$ from this calculation; the next $p$-adic digits must
be analyzed.  In particular, this note does not prove the desired uniform
bound $v_p(\beta_N)\geq N-O(\log N)$ on the exceptional set.

### 6.2 The $N=1$ edge

The formulas also have no hidden small-degree exception.  At $N=1$, direct
exact row reduction gives the primitive polynomial coefficient vector

$$
(A_0,b_0,b_1,c_0,c_1)
=(47\,123\,952,-47\,123\,952,42\,578\,172,
  1\,428\,025,-5\,973\,805).                     \tag{81}
$$

Thus $A(1)=47\,123\,952$, $B(1)=C(1)=-4\,545\,780$, and their gcd is
$3\,804$.  The primitive endpoint pair and ratio are

$$
(\alpha_1,\beta_1)=(12\,388,-1\,195),\qquad
\frac{A(1)}{B(1)}=-\frac{12\,388}{1\,195}.       \tag{82}
$$

In particular $v_{239}(A(1)/B(1))=-1$ and
$v_{239}(\beta_1)=1$, in agreement with Proposition 6.1
($W_1=1$ and $\mathcal C_1=2$).

## 7. Exact finite diagnostics

Three executable finite audits accompany this note.

1. `machin_endpoint_tail_probe.py` recomputes the diagonal forms through
   $n=18$, removes the endpoint gcd, and checks (33) against a certified
   rational interval for $e+\pi$.  In all 18 degrees the effective
   $C$-height exceeds $5^{2n}$, the proved upper bound is greater than one,
   and the actual form is certified nonzero and greater than one.  At
   $n=18$, the normalized $C$-height divided by $5^{36}$ already has decimal
   exponent $2067$, the tail bound has exponent $2067$, and the actual form
   has exponent $2040$.  These are finite facts only.

2. `machin_nondiagonal_probe.py` scans all 455 triples of nonnegative degrees
   with $a+b+c\leq12$ and $M=a+b+c+1$.  Every matrix in this box has nullity
   one; 454 have nonzero endpoint coefficient, while $(0,1,0)$ is the sole
   endpoint-degenerate case.  No certified endpoint form or tail upper bound
   in the scan is below one.  Among triples with all three degrees positive,
   the smallest finite bounds favor putting most available degree in $A$ and
   keeping $b=c=1$, which motivated Section 6.  This bounded observation is
   not promoted to a slope theorem.

3. `machin_fixed_bc1_ray.py` checks the closed formulas (57)--(67) against
   direct exact linear algebra for odd $N\leq13$, including the endpoint
   normalization (81)--(82).  At the first nontrivial
   subsequence point $N=479=1+2\cdot239$, it independently computes a reduced
   endpoint denominator with exactly $479$ factors of $239$, confirming
   (70)--(71) in that instance.  It also verifies the exact leading-residue
   criterion against reduced endpoint ratios at $N=15,239,477$, respectively
   exercising $239\mid D$, $239\mid N$, and $239\mid(N+1)$.  Finally, it
   verifies the exact leading-residue
   cancellation (80) using modular integer arithmetic, without constructing
   the enormous rational endpoint ratio at $N=9\,196\,483$.

The finite diagonal data, and similar behavior for other faster-converging
Machin kernels, illustrate the general lesson already made rigorous by
(33): faster analytic convergence can be completely offset by arithmetic
height.  No unarchived exploratory figures are used as evidence here.

## 8. Status and remaining route

For the diagonal Machin family, the exact endpoint problem is now reduced to
the following two quantities:

$$
\text{effective height }H_C^*
\quad\text{versus}\quad
\frac{(2n+1)5^{2n+1}}{16(n+1)},                  \tag{83}
$$

and the actual cancellation inside the two integrals in (18).  An all-degree
proof of

$$
H_C^*=o(5^{2n})                                   \tag{84}
$$

would make the absolute-tail route succeed, while a complete asymptotic with
a nonzero leading constant could decide the forms even when (84) fails.
Neither is presently known.  Rank and normality alone do not control (53),
and a coefficient-height lower bound alone does not control the cancellations
visible in (22).

The non-diagonal theorem in Section 6 eliminates one natural slope but leaves
other regimes open.  In every balanced regime, equations (37)--(38) give the
precise arithmetic target.  These results prove no irrationality or
transcendence statement about $e+\pi$; they sharpen the proof obligations and
provide one rigorous non-diagonal no-go result without extrapolating finite
data.
