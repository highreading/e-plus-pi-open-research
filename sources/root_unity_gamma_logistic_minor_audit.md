> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The logistic-moment minor behind the root-of-unity correction

## Positive contour models, all-parameter endpoint normality, and the exact
## augmented-Chebyshev obstruction for Γ

Checked: 2026-08-27 UTC

## 1. Verdict

Put



$$
f(z)=\frac{1}{1+e^z},\qquad
 \mathcal L(p)=p(d/dz)f(z)\big|_{z=0},                        \tag{1}
$$



and



$$
\Phi_{m,n}(X)=\prod_{j=0}^{m-1}(X-j)^{n+1},\qquad
 M=m(n+1).                                                     \tag{2}
$$



The natural two-dimensional endpoint space in the constrained
root-of-unity construction is the kernel of



$$
K_{q,a}=\mathcal L\!\left((X^q\Phi_{m,n})^{(a)}\right),
 \quad 0\le q\le D-2,\quad 0\le a\le D.                       \tag{3}
$$



The previous audit verified the expected rank in finite grids but did not
prove it for all parameters.  This note proves the following
all-parameter theorem.

> **Endpoint normality theorem.**  For every
> $m\ge1$ and $n\ge D\ge2$, the matrix in (3) has rank $D-1$.
> Its kernel has parity dimensions
> 

$$
>  (\dim E_2^{\rm even},\dim E_2^{\rm odd})=
>  \begin{cases}
>   (2,0),&mn\text{ odd and }D\text{ even},\\
>   (1,1),&\text{otherwise}.
>  \end{cases}                                                  \tag{4}
>
$$



The proof is not a finite-rank extrapolation.  After centering the row
polynomials, (3) splits into two bi-moment matrices.  For even $m$, the
positive measure contains $\operatorname {sech}(\pi t)$; for odd $m$,
it contains $1/\sinh(\pi t)$ on $t>0$.  The two polynomial systems in
each block are ordinary powers of $t^2$ and degree-graded derivative
polynomials in $\tanh^2(\pi t)$ or $\coth^2(\pi t)$.  Andréief's
identity makes an initial maximal minor a strictly signed integral of two
Vandermonde determinants.

This note also gives the requested exact minor representation of the
two-column correction



$$
\Gamma_{C,D}(z)=C(z)\beta_D(z)-D(z)\beta_C(z).                \tag{5}
$$



Let $\Lambda_b$ be the Hermite-cardinal polynomial determined by



$$
\Lambda_b^{(a)}(j)=(-1)^j\delta_{a,b},qquad
 0\le j<m,\quad0\le a,b\le n.                                 \tag{6}
$$



Then the coefficient row of the endpoint specialization is



$$
E_{b,a}:=[z^b]\beta_{z^a}=-\mathcal L(\Lambda_b^{(a)}).       \tag{7}
$$



If $N=(c\ d)$ is a basis matrix for $\ker K$, then, up to one
nonzero scalar independent of $\ell$,



$$
\boxed{
 [z^\ell]\Gamma_{C,D}
 \ \doteq\!
 \sum_{a+b=\ell}
 \det\!\begin{pmatrix}K\\ e_a^T\\ E_b\end{pmatrix}.}       \tag{8}
$$



Here $C(z)=\sum c_a z^a$, $D(z)=\sum d_a z^a$, and
$\doteq$ means equality up to the fixed Plücker normalization of
$N$.  Formula (8) is exact over $\mathbb Q$.

The normality theorem does **not** by itself prove $\Gamma\ne0$.  It
does, however, isolate the missing statement much more sharply.  The gauge



$$
\widehat\beta_C=\beta_C+\frac m2C             \tag{9}
$$



reverses endpoint parity.  Consequently:

* outside the defect in (4), $\Gamma$ is even and its constant
  coefficient is the bordered minor
  

$$
\det\!\begin{pmatrix}K\\ e_0^T\\ E_0\end{pmatrix};    \tag{10}
$$


* in the defect case, both endpoints are even, $\Gamma$ is odd, and
  its linear coefficient is the bordered minor
  

$$
\det\!\begin{pmatrix}K\\ e_0^T\\ E_1\end{pmatrix}.    \tag{11}
$$



Thus proving the appropriate determinant in (10) or (11) nonzero would
settle the high-$m$ survivor for every parameter.

There is a real obstruction to applying total positivity mechanically.
Even after every entry of a natural parity block is made positive by row
and column signs, its arbitrary minors need not be positive.  At
$(m,n,D)=(2,4,5)$, the normalized odd block is



$$
\begin{pmatrix}
 304&3000&29640\\
 4644&45834&452310
 \end{pmatrix},                                                \tag{12}
$$



and the minor in columns $1,3$ is



$$
304\cdot452310-29640\cdot4644=-145920.      \tag{13}
$$



Only the **initial** maximal minors used in the rank proof have a direct
positive Andréief representation.  The extra row in (10) or (11) is a
rational Hermite-cardinal function, not another ordinary monomial row.
The remaining theorem is therefore an augmented Chebyshev statement, not
ordinary total positivity of the full confluent matrix.

No conclusion about the arithmetic nature of $e+\pi$ is claimed here.

The replayable files are

* `scripts/root_unity_gamma_logistic_minor_certificate.py`;
* `results/root_unity_gamma_logistic_minor_certificate.json`.

## 2. Two exact contour representations of the logistic functional

Two elementary Fourier transforms give the positive models needed below:



$$
\int_{-\infty}^{\infty}e^{iut}\operatorname {sech}(\pi t)\,dt
       =\operatorname {sech}(u/2),                             \tag{14}
$$



and, in the principal-value sense,



$$
\operatorname {pv}\!\int_{-\infty}^{\infty}
       \frac{e^{iut}}{\sinh(\pi t)}\,dt
       =i\tanh(u/2).                                           \tag{15}
$$



Equation (14), first for exponentials and then coefficientwise, gives



$$
\boxed{
 \mathcal L(p)=\frac12\int_{-\infty}^{\infty}
 p\!\left(-\frac12+it\right)\operatorname {sech}(\pi t)\,dt.} \tag{16}
$$



Indeed, the right side applied to $p(X)=e^{uX}$ is



$$
\frac12e^{-u/2}\operatorname {sech}(u/2)=\frac1{1+e^u}.
$$



Similarly, (15) gives



$$
\boxed{
 \mathcal L(p)=\frac12p(0)+\frac i2\operatorname {pv}
 \int_{-\infty}^{\infty}\frac{p(it)}{\sinh(\pi t)}\,dt.}      \tag{17}
$$



The sign in (17) is worth checking: multiplying the right side of (15) by
$i/2$ produces $-\tfrac12\tanh(u/2)$, and



$$
\frac12-\frac12\tanh(u/2)=\frac1{1+e^u}.
$$



The shift identity



$$
\mathcal L(p(X+1))+\mathcal L(p(X))=p(0)                     \tag{18}
$$



implies, whenever $p(0)=\cdots=p(k-1)=0$,



$$
\mathcal L(p(X+k))=(-1)^k\mathcal L(p).     \tag{19}
$$



All later contour shifts use (19), so no unproved displacement of a
complex contour is involved.

## 3. Centering the endpoint matrix

Put



$$
c=\frac{m-1}{2}.                       \tag{20}
$$



Replacing the row basis $1,X,\ldots,X^{D-2}$ by
$1,X-c,\ldots,(X-c)^{D-2}$ is an invertible triangular row operation.
Thus (3) has the same rank as



$$
\widetilde K_{q,a}=
 \mathcal L\!\left(\bigl((X-c)^q\Phi_{m,n}(X)\bigr)^{(a)}\right).
                                                                    \tag{21}
$$



Since $a\le D\le n$, the polynomial being evaluated in (21) still
vanishes at every integer $0,\ldots,m-1$.  This is exactly the
hypothesis needed to use (19).

## 4. Even $m$: a positive sech bi-moment matrix

Let $m=2k$, so $c=k-\tfrac12$, and define



$$
V(t)=\prod_{r=1}^{k}
 \left(t^2+\left(r-\frac12\right)^2\right)^{n+1}>0.            \tag{22}
$$



Shifting (16) by $k$ with (19) gives, for the polynomial in (21),



$$
\widetilde K_{q,a}=\frac{(-1)^k}{2}
 \int_{-\infty}^{\infty}
 \bigl((X-c)^q\Phi(X)\bigr)^{(a)}\big|_{X=c+it}
 \operatorname {sech}(\pi t)\,dt.                             \tag{23}
$$



On this line,



$$
\Phi(c+it)=(-1)^{k(n+1)}V(t).                                \tag{24}
$$



Since $d/dX=-i\,d/dt$ on $X=c+it$, integration by parts gives



$$
\widetilde K_{q,a}\ \doteq\
 i^{q-a}\int_{-\infty}^{\infty}
 t^qV(t)(-1)^a\frac{d^a}{dt^a}\operatorname {sech}(\pi t)\,dt.
                                                                    \tag{25}
$$



Here and in (35), the omitted factor is a nonzero global factor times a
row factor $i^q$ and a column factor $(\pi/i)^a$.  Removing it therefore
does not change the rank or the sign of a minor after fixed row and column
normalizations.

There are no boundary terms because the hyperbolic secant decays
exponentially.

Define derivative polynomials $P_a$ by



$$
(-1)^a\frac{d^a}{dt^a}\operatorname {sech}(\pi t)
 =\pi^aP_a(\tanh(\pi t))\operatorname {sech}(\pi t).          \tag{26}
$$



They satisfy



$$
P_0=1,\qquad
 P_{a+1}(x)=xP_a(x)-(1-x^2)P_a'(x).                            \tag{27}
$$



Therefore $P_a$ has parity $a$, exact degree $a$, and leading
coefficient $a!$.  In particular,



$$
P_{\epsilon+2v}(x)=x^\epsilon Q_v^{(\epsilon)}(x^2),
 \qquad \deg Q_v^{(\epsilon)}=v,                              \tag{28}
$$



with nonzero leading coefficient.

Equation (25) vanishes unless $q\equiv a\pmod2$.  In a fixed parity
block, put $q=\epsilon+2u$ and $a=\epsilon+2v$.  After removing row
and column phases, its entries have the form



$$
M_{u,v}=\int_0^\infty
 (t^2)^uQ_v^{(\epsilon)}(\tanh^2(\pi t))\,d\mu_\epsilon(t),    \tag{29}
$$



where



$$
d\mu_\epsilon(t)=
 2t^\epsilon\tanh^\epsilon(\pi t)V(t)
 \operatorname {sech}(\pi t)\,dt                             \tag{30}
$$



is strictly positive on $(0,\infty)$.

Take the first $r$ rows and first $r$ columns in (29).  Andréief's
identity expresses their determinant as a nonzero constant times



$$
\int_{0<t_1<\cdots<t_r}
 \det\bigl((t_j^2)^u\bigr)_{u=0}^{r-1}
 \det\bigl(Q_v^{(\epsilon)}(y_j)\bigr)_{v=0}^{r-1}
 \prod_{j=1}^r d\mu_\epsilon(t_j),                             \tag{31}
$$



where $y_j=\tanh^2(\pi t_j)$.  Both determinants in (31) are a nonzero
constant times a Vandermonde determinant.  Since both $t^2$ and
$\tanh^2(\pi t)$ are strictly increasing, the integrand has one strict
sign.  Thus every initial square minor in (29) is nonzero.

## 5. Odd $m$: a positive csch bi-moment matrix

Let $m=2k+1$, so $c=k$, and put



$$
V(t)=\prod_{r=1}^{k}(t^2+r^2)^{n+1}>0.                       \tag{32}
$$



The polynomial in (21), and all derivatives used there, vanish at the
central point $X=k$.  Hence the point mass in (17) is zero after shifting
by $k$.  Equations (17) and (19) give



$$
\widetilde K_{q,a}=\frac{(-1)^ki}{2}
 \operatorname {pv}\!\int_{-\infty}^{\infty}
 \frac{\bigl((X-c)^q\Phi(X)\bigr)^{(a)}|_{X=c+it}}
      {\sinh(\pi t)}\,dt.                                     \tag{33}
$$



Now



$$
\Phi(c+it)=i^{n+1}(-1)^{k(n+1)}t^{n+1}V(t).                  \tag{34}
$$



After integrating by parts,



$$
\widetilde K_{q,a}\ \doteq\
 i^{q+n+2-a}\operatorname {pv}\!\int_{-\infty}^{\infty}
 t^{q+n+1}V(t)(-1)^a\frac{d^a}{dt^a}\frac1{\sinh(\pi t)}\,dt.
                                                                    \tag{35}
$$



Integration by parts across zero is legitimate.  At every intermediate
step the boundary term is
$O(t^{n+1+q-a})$, which tends to zero because $a\le n$.

Define $H_a$ by



$$
(-1)^a\frac{d^a}{dt^a}\frac1{\sinh(\pi t)}
 =\pi^aH_a(\coth(\pi t))\frac1{\sinh(\pi t)}.                 \tag{36}
$$



Then



$$
H_0=1,\qquad
 H_{a+1}(x)=xH_a(x)+(x^2-1)H_a'(x).                            \tag{37}
$$



Again $H_a$ has parity $a$, exact degree $a$, and nonzero leading
coefficient.  Equation (35) vanishes unless



$$
a\equiv q+n\pmod2.                    \tag{38}
$$



Fix a row parity $q=\epsilon+2u$, put
$\delta\equiv\epsilon+n\pmod2$, and write



$$
H_{\delta+2v}(x)=x^\delta\widetilde Q_v^{(\delta)}(x^2),
 \qquad\deg\widetilde Q_v^{(\delta)}=v.                      \tag{39}
$$



After phases are removed, the block entries are



$$
\widetilde M_{u,v}=\int_0^\infty
 (t^2)^u\widetilde Q_v^{(\delta)}(\coth^2(\pi t))
 \,d\nu_{\epsilon,\delta}(t),                               \tag{40}
$$



with the strictly positive measure



$$
d\nu_{\epsilon,\delta}(t)=
 2t^{\epsilon+n+1}\coth^\delta(\pi t)V(t)
 \frac{dt}{\sinh(\pi t)}.                                    \tag{41}
$$



The same Andréief calculation applies.  This time $t^2$ increases and
$\coth^2(\pi t)$ decreases, so the second Vandermonde contributes the
fixed sign $(-1)^{r(r-1)/2}$.  The determinant is still nonzero.

## 6. Proof of the endpoint normality theorem

For even $m$, (25) gives checkerboard offset zero.  For odd $m$, (38)
gives offset $n$.  These combine into



$$
\widetilde K_{q,a}=0
 \quad\text{unless}\quad a\equiv q+mn\pmod2.                 \tag{42}
$$



Every nonzero parity block has full row rank by Sections 4--5.

If $D=2d+1$, the row parities each occur $d$ times and the endpoint
coefficient parities each occur $d+1$ times.  Each endpoint parity
therefore contributes nullity one.

If $D=2d$ and the checkerboard offset is zero, the even block is
$d$-by-$(d+1)$, and the odd block is $(d-1)$-by-$d$.  Again each
endpoint parity contributes nullity one.

If $D=2d$ and the offset is one, the even row block maps to the $d$
odd columns and is square invertible.  The $d-1$ odd rows map to the
$d+1$ even columns, leaving a two-dimensional even kernel.  Offset one
means $mn$ is odd.  This proves both rank $D-1$ and (4).

## 7. Hermite-cardinal rows and the bordered-minor formula

Let



$$
T_C(z,y)=\sum_{j=0}^{m-1}\sum_{a=0}^n b_{j,a}(C)z^ay^j       \tag{43}
$$



be the unique auxiliary polynomial whose exponential specialization
matches the first $M$ jets of $-C(z)f(z)$.  For every polynomial
$Q$,



$$
Q(d/dz)\bigl(z^ae^{jz}\bigr)\big|_{z=0}=Q^{(a)}(j).          \tag{44}
$$



Apply (44) with $Q=\Lambda_b$ from (6).  It extracts exactly the
alternating coefficient



$$
\sum_{j=0}^{m-1}(-1)^jb_{j,b}(C)=[z^b]T_C(z,-1).             \tag{45}
$$



The matched jets equal those of $-Cf$, and



$$
Q(d/dz)\bigl(z^af(z)\bigr)\big|_{z=0}
 =\mathcal L(Q^{(a)}).                                        \tag{46}
$$



Equations (45)--(46) prove (7).

Let $c,d\in\mathbb Q^{D+1}$ be the two columns of a kernel basis
$N$.  Direct convolution gives



$$
[z^\ell]\Gamma
 =\sum_{a+b=\ell}
 \det\!\begin{pmatrix}e_a^Tc&e_a^Td\\E_bc&E_bd\end{pmatrix}.
                                                                    \tag{47}
$$



The two-by-two determinant in (47) is the restriction of the alternating
form $e_a\wedge E_b$ to $\ker K$.  The standard complementary-minor
identity gives



$$
\det\!\begin{pmatrix}e_a^TN\\E_bN\end{pmatrix}
 =\chi(K,N)
 \det\!\begin{pmatrix}K\\e_a^T\\E_b\end{pmatrix},           \tag{48}
$$



where $\chi(K,N)\ne0$ is independent of $a,b$.  Summing (48) proves
(8).  This also shows that the primitive vector of all coefficients of
$\Gamma$ is intrinsic to the saturated exterior line; changing the
endpoint basis multiplies all coefficients by one nonzero scalar.

## 8. Reflection and the parity-reversing gauge

Write



$$
R_C(z,y)=C(z)+(1+y)T_C(z,y).                                  \tag{49}
$$



Reflection followed by a common frequency shift gives



$$
y^mR_C(-z,y^{-1})
 =(-1)^mC(-z)+(1+y)\left[
 y^{m-1}T_C(-z,y^{-1})+
 \frac{y^m-(-1)^m}{y+1}C(-z)\right].                          \tag{50}
$$



At $y=-1$, the quotient in (50) is $m(-1)^{m-1}$.  If
$C(-z)=\sigma C(z)$, uniqueness of origin interpolation shows that the
reflected pair is $(-1)^m\sigma$ times the original pair.  Therefore



$$
\beta_C(-z)+m\sigma C(z)=-\sigma\beta_C(z).                  \tag{51}
$$



Equation (51) is equivalent to



$$
\widehat\beta_C(-z)=-\sigma\widehat\beta_C(z),               \tag{52}
$$



which proves the parity reversal asserted after (9).  The added scalar
multiple in (9) cancels from (5), so it does not change $\Gamma$.

When the endpoint space is one even plus one odd line, (52) makes
$\Gamma$ even.  Its constant term contains only the even endpoint value
and the constant term of the correction attached to the odd endpoint;
this is (10).  In the defect case, both endpoints are even, both gauged
corrections are odd, and the coefficient of $z$ is (11).

These observations reduce global nonvanishing to one coefficient, but the
normality theorem does not determine either bordered determinant.

## 9. The top Hermite-cardinal row is explicitly rational

The polynomial $\Lambda_n$ in (6) has zeros of multiplicity $n$ at
all $j=0,\ldots,m-1$.  Hence



$$
\Lambda_n(X)=A_{m,n}(X)\prod_{j=0}^{m-1}(X-j)^n,
 \qquad\deg A_{m,n}\le m-1.                                  \tag{53}
$$



Its values at the nodes are



$$
A_{m,n}(j)=
 \frac{(-1)^{j+n(m-1-j)}}
 {n!\,[j!(m-1-j)!]^n}.                                        \tag{54}
$$



Thus $A_{m,n}$ is the ordinary Lagrange interpolant of the explicit
data (54).  Dividing (53) by $\Phi$ gives the simple-pole formula



$$
\boxed{
 \frac{\Lambda_n(X)}{\Phi_{m,n}(X)}
 =\frac1{n!}\sum_{j=0}^{m-1}
 \frac{(-1)^{j+(n+1)(m-1-j)}}
 {[j!(m-1-j)!]^{n+1}}\frac1{X-j}.}                            \tag{55}
$$



Formula (55) is a useful Christoffel/Markov boundary row for leading
coefficients of $\Gamma$.  It also displays the remaining difficulty:
depending on parity, the residues in (55) can alternate.  Pairing symmetric
poles sometimes produces a positive Stieltjes sum in $t^2$, but not in
all parity regimes.

For the constant and linear rows in (10)--(11), the corresponding rational
functions $\Lambda_0/\Phi$ and $\Lambda_1/\Phi$ have confluent poles of
order up to $n+1$.  They are exact rational Hermite-cardinal transforms,
not polynomial rows of the bi-moment matrix.

## 10. Why ordinary total positivity stops short

The proof in Sections 4--6 uses only the minor formed by the first $r$
degree-graded column polynomials.  It does not show that an arbitrary set
of the derivative polynomials is a Chebyshev system.

The failure is already exact in a small case.  For $(m,n,D)=(2,4,5)$,
take centered odd rows $q=1,3$ and odd columns $a=1,3,5$.  Before sign
normalization the block is



$$
\begin{pmatrix}
 304&-3000&29640\\
 -4644&45834&-452310
 \end{pmatrix}.                                                \tag{56}
$$



Multiplying the second row and the middle column by $-1$ gives (12),
whose nonconsecutive minor (13) is negative.  Thus there is no diagonal
choice of row and column signs making this block totally positive: it is
already entrywise positive under the displayed choice, yet has minors of
both signs.

This does not contradict the normality proof.  The initial two columns in
(12) have determinant



$$
304\cdot45834-3000\cdot4644=1536>0,         \tag{57}
$$



exactly as predicted by (31).

## 11. The exact remaining augmented-Chebyshev lemma

The contour proof converts a fixed endpoint-parity block of $K$ to a pairing



$$
\int_0^\infty x(t)^uQ_v(y(t))\,d\mu(t),          \tag{58}
$$



where $x(t)=t^2$, while $y(t)$ is either
$\tanh^2(\pi t)$ or $\coth^2(\pi t)$.  In a boundary-free parity
block, adjoining $E_b$ replaces one monomial row by the rational
Hermite-cardinal function obtained from $\Lambda_b/\Phi$.  In the odd
$m$ csch model, integration by parts can also produce finite terms at
the central pole; those terms must be retained.  The bordered determinants
(10)--(11), or equivalently the exact cardinal formula (7), include them
automatically.  No boundary-free formula is assumed in this note.

Consequently, (10)--(11) would follow from the following precise type of
statement:

> **Augmented-Chebyshev lemma needed.**  In the relevant parity block, the
> row system
> 

$$
>       1,x,\ldots,x^{r-1},\rho_{m,n}(x)                       \tag{59}
>
$$


> obtained from the centered rational cardinal function, together with the
> explicit central-pole functional when present, has a strictly signed
> generalized collocation determinant in the exact size required by
> $D\le n$.

Equivalently, the appropriate divided difference of $\rho_{m,n}$ must
have one strict sign.  Complete monotonicity of $\rho_{m,n}$ would be a
sufficient condition in several blocks, but it has not been proved here.
The mixed residue signs visible in (55), and the failure of full total
positivity in (13), show why neither property may be inserted without a
separate argument.

The finite exact data continue to support the augmented lemma: every tested
$\Gamma$ with $m\ge2$ is nonzero, and its nonzero coefficients have one
sign after primitive normalization.  Those data are evidence only.  The
all-parameter result established in this note is endpoint normality (4),
not the augmented lemma (59).

## 12. Replay certificate

The exact certificate performs the following operations over $\mathbb Q$.

1. It constructs $K$, the centered version of $K$, all
   $\Lambda_b$, and all rows $E_b$.
2. On the grid
   

$$
1\le m\le4,\quad2\le n\le5,\quad2\le D\le\min(5,n),       \tag{60}
$$


   it verifies rank $D-1$, the parity dimensions (4), and parity reversal
   under (9).
3. It constructs $\Gamma$ directly on a kernel basis and verifies every
   coefficient in the bordered-minor identity (8), including the known
   zero cases at $m=1$.
4. It verifies (53)--(55) exactly.
5. It records the exact counterexample (12)--(13).

The grid contains 40 tuples.  Its deterministic exact-row digest is

    41e5b516efca487f5e54256e8dca0f21c5fb97131601b1367729c425398aa97b

The certificate is a replay of the algebraic formulas and the explicit
negative minor.  The proof of (4) is the all-parameter argument in
Sections 2--6, not an inference from (60).
