> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Universality of the factor-endpoint positive cone, and why shrinking is equivalent to irrationality

Checked: 2026-08-27 UTC.

## 1. Main theorem

Put



$$
s=e+\pi,\qquad
 W(x)=e^x+\frac4{1+x^2}>0\quad(0\leq x\leq1),
 \tag{1}
$$



and define



$$
A(F)=\sum_{j\geq0}(-1)^jF^{(j)}(1),\qquad
 B(F)=\sum_{j\geq0}(-1)^jF^{(j)}(0).
 \tag{2}
$$



Consider all real polynomials of the form



$$
F=(1-x)^2H,\qquad H\geq0\quad\hbox{on }[0,1],
 \tag{3}
$$



which satisfy



$$
A(F)=F(i)=F(-i)=a\in\mathbb R.
 \tag{4}
$$



For such a polynomial,



$$
G=\frac{F-a}{1+x^2}
 \tag{5}
$$



is a polynomial, and its output point is



$$
T(F)=(a,c),\qquad
 c=-B(F)+4\int_0^1G(x)\,dx.
 \tag{6}
$$



Let $\mathcal C_{\mathbb R}\subset\mathbb R^2$ be the cone of all output
points (6).

### Theorem 1: exact real cone



$$
\boxed{
 \mathcal C_{\mathbb R}
 =\{(0,0)\}\ \cup\
 \{(a,c)\in\mathbb R^2:sa+c>0\}.}
 \tag{7}
$$



Thus the only supporting functional of the full positive common-kernel
cone is the original positive integral



$$
sa+c=\int_0^1F(x)W(x)\,dx.
 \tag{8}
$$



There is no additional real convex-geometric obstruction.

### Theorem 2: exact rational and primitive realization

If $a,c\in\mathbb Q$ and



$$
sa+c>0,
 \tag{9}
$$



then there is a rational polynomial $H>0$ on $[0,1]$ satisfying the
common equations and having output exactly $(a,c)$.

Consequently, if $(q,k)\in\mathbb Z^2$ is primitive and



$$
qs+k>0,
 \tag{10}
$$



there is a primitive integer polynomial



$$
F=(1-x)^2H\geq0
 \tag{11}
$$



whose **fully primitive output pair** is exactly



$$
\boxed{(q,k).}
 \tag{12}
$$



In particular, for every pair of coprime integers $q>0,p$ with



$$
\frac pq<e+\pi,
 \tag{13}
$$



there is a primitive positive integer polynomial in this factor class whose
fully primitive form is



$$
\boxed{q(e+\pi)-p.}
 \tag{14}
$$



No irrationality assumption is made in either theorem.

### Corollary: exact circularity of the shrinking question

There is an infinite sequence of primitive positive forms from this cone
which tends to zero if and only if $e+\pi$ is irrational.

Therefore this positive-cone route is universal at the level of
realizability, but universality alone cannot decide irrationality. If
$e+\pi$ were rational, its exact boundary ray would be the unique missing
rational boundary ray and every nonzero primitive positive value would
have a fixed arithmetic gap. If it is irrational, its lower continued
fraction convergents are all realized and give a shrinking sequence.

This note proves a cone classification and an equivalence theorem. It does
not choose between the rational and irrational alternatives, and it does
not prove transcendence.

## 2. Extending all coordinates off the common plane

It is useful to work with $H$, not $F$. For an arbitrary real
polynomial $H$, put



$$
F=(1-x)^2H,\qquad
 r(H)=\Re H(i),\qquad
 a(H)=2\Im H(i).
 \tag{15}
$$



Since



$$
F(i)=(1-i)^2H(i)=-2iH(i)=a(H)-2ir(H),
 \tag{16}
$$



Euclidean division gives a unique polynomial $Q_H$ satisfying



$$
\boxed{
 F-a(H)=(1+x^2)Q_H-2r(H)x.}
 \tag{17}
$$



Indeed, the right remainder has the correct values $-2ir(H)$ and
$2ir(H)$ at $i$ and $-i$.

Define the second common-plane constraint



$$
\alpha(H)=A(F)-a(H)
 \tag{18}
$$



and extend the rational output coordinate to every real polynomial by



$$
c(H)=-B(F)+4\int_0^1Q_H(x)\,dx.
 \tag{19}
$$



All four maps



$$
r,\quad \alpha,\quad a,\quad c
 \tag{20}
$$



are real linear. They have rational coefficients on $\mathbb Q[x]$.
The common plane in the $H$-coordinate is



$$
\mathcal S=\ker r\cap\ker\alpha.
 \tag{21}
$$



On this plane, (17) becomes $F-a=(1+x^2)Q_H$, so (19) is exactly the
coordinate in (6).

Repeated integration by parts gives



$$
\int_0^1e^xF(x)\,dx=eA(F)-B(F).
 \tag{22}
$$



Equation (17) also gives



$$
\begin{aligned}
4\int_0^1\frac{F(x)}{1+x^2}\,dx
&=\pi a(H)+4\int_0^1Q_H(x)\,dx
 -8r(H)\int_0^1\frac{x}{1+x^2}\,dx\\
&=\pi a(H)+4\int_0^1Q_H(x)\,dx-4\log2\,r(H).
\end{aligned}
\tag{23}
$$



Let



$$
J(H)=\int_0^1(1-x)^2H(x)W(x)\,dx.
 \tag{24}
$$



Combining (18), (19), and (22)--(23) gives the central extension identity



$$
\boxed{
 J(H)=s\,a(H)+c(H)+e\,\alpha(H)-4\log2\,r(H).}
 \tag{25}
$$



On $\mathcal S$, this reduces to (8).

The two constraints are independent. On the two polynomials $1,x$, their
matrix is



$$
\begin{pmatrix}
 r(1)&r(x)\\
 \alpha(1)&\alpha(x)
 \end{pmatrix}
 =
 \begin{pmatrix}
 1&0\\
 2&-6
 \end{pmatrix},
 \tag{26}
$$



whose determinant is $-6$.

## 3. A strictly positive order unit

The polynomial



$$
H_*=3+8x+3x^2
 \tag{27}
$$



satisfies



$$
H_*\geq3\quad(0\leq x\leq1)
 \tag{28}
$$



and exact calculation gives



$$
r(H_*)=\alpha(H_*)=0,\qquad
 (a(H_*),c(H_*))=(16,-85).
 \tag{29}
$$



Thus $H_*\in\mathcal S$ is an order unit: for every polynomial $P$
there is $M>0$ such that



$$
-MH_*\leq P\leq MH_*
 \quad\hbox{on }[0,1].
 \tag{30}
$$



This elementary fact is what allows a positive functional on the common
plane to be extended to the full polynomial algebra.

For reference, there is also a strictly positive target-zero direction:



$$
H_0=(1+x^2)(68+16x)>0,
 \tag{31}
$$



with



$$
r(H_0)=\alpha(H_0)=a(H_0)=0,\qquad c(H_0)=132.
 \tag{32}
$$



Adding positive multiples of $H_0$ already shows that normalized output
slopes are unbounded in one direction. The dual proof below determines the
other boundary exactly.

## 4. Positive extension lemma

Let $\mathcal P$ be the cone of real polynomials nonnegative on
$[0,1]$.

### Lemma 3

Every linear functional $\ell:\mathcal S\to\mathbb R$ satisfying



$$
\ell(H)\geq0\qquad(H\in\mathcal S\cap\mathcal P)
 \tag{33}
$$



has an extension $\widetilde\ell:\mathbb R[x]\to\mathbb R$ satisfying



$$
\widetilde\ell(H)\geq0\qquad(H\in\mathcal P).
 \tag{34}
$$



### Proof

For a polynomial $P$, define



$$
p(P)=\inf\{\ell(S):S\in\mathcal S,\ S\geq P\text{ on }[0,1]\}.
 \tag{35}
$$



The set in (35) is nonempty by (30). It is bounded below: if
$P\geq-MH_*$ and $S\geq P$, then



$$
S+MH_*\in\mathcal S\cap\mathcal P,
$$



so



$$
\ell(S)\geq-M\ell(H_*).
 \tag{36}
$$



The map $p$ is sublinear. If $S\in\mathcal S$, positivity on
$\mathcal S$ shows



$$
p(S)=\ell(S).
 \tag{37}
$$



The algebraic Hahn--Banach theorem therefore extends $\ell$ to a linear
functional $\widetilde\ell$ on all polynomials with



$$
\widetilde\ell(P)\leq p(P).
 \tag{38}
$$



If $P\geq0$, then $0\geq-P$, hence $p(-P)\leq0$. Equation (38) gives



$$
-\widetilde\ell(P)=\widetilde\ell(-P)\leq0.
$$



This is (34). $\square$

## 5. Exact dual cone

Suppose $(u,v)\in\mathbb R^2$ is nonnegative on the output cone:



$$
u\,a(H)+v\,c(H)\geq0
 \quad
 (H\in\mathcal S,\ H\geq0).
 \tag{39}
$$



Apply Lemma 3 to the functional on the left. Its positive extension differs
from $ua+vc$ by a functional which vanishes on $\mathcal S$.
Because (26) proves that $r,\alpha$ are independent and
$\mathcal S=\ker(r,\alpha)$, there are real $\lambda,\mu$ such that



$$
\widetilde\ell
 =u\,a+v\,c+\lambda r+\mu\alpha.
 \tag{40}
$$



Use (25) to rewrite this as



$$
\boxed{
\widetilde\ell
=vJ+(u-sv)a+(\mu-ev)\alpha
  +(\lambda+4v\log2)r.}
\tag{41}
$$



We now use only the moments



$$
m_n=\widetilde\ell(x^n).
 \tag{42}
$$



Since $\widetilde\ell$ is positive and



$$
0\leq x^{n+1}\leq x^n\leq1
 \quad(0\leq x\leq1),
 \tag{43}
$$



the sequence $m_n$ is nonnegative, bounded, and nonincreasing. In
particular, it converges.

### 5.1 Factorial growth forces the coefficient $e$

Put



$$
f_n=x^n(1-x)^2.
 \tag{44}
$$



If $!n$ denotes the derangement number, then



$$
A(x^n)=(-1)^n!n
 \tag{45}
$$



and the recurrence for derangements gives



$$
A(f_n)
 =(n^2+5n+5)(-1)^n!n-(n+3).
 \tag{46}
$$



Also



$$
a(x^n)=2\Im(i^n)\in\{0,2,0,-2\}.
 \tag{47}
$$



Consequently



$$
\alpha(x^n)=A(f_n)-a(x^n)
 \tag{48}
$$



has factorially growing absolute value. For example, the alternating
formula for derangements gives $!n\geq n!/3$ for $n\geq2$, so the
factorial term in (46) dominates the two linear terms in (46)--(48). In
contrast,



$$
a(x^n),\quad r(x^n)
 \tag{49}
$$



are bounded, and



$$
J(x^n)=\int_0^1x^n(1-x)^2W(x)\,dx\longrightarrow0.
 \tag{50}
$$



Indeed, the continuous function $(1-x)^2W(x)$ is bounded, so the last
integral is at most a constant times $1/(n+1)$.

If $\mu-ev\ne0$, equation (41) makes $m_n$ unbounded along the
monomials. This contradicts (43). Therefore



$$
\boxed{\mu=ev.}
 \tag{51}
$$



This is the unique cancellation of the factorial exterior functional. The
constant $e$ is forced by positivity; it is not inserted as an
approximation.

### 5.2 Moment convergence kills the exterior four-cycle

After (51), equation (41) gives



$$
m_n=vJ(x^n)+\beta\,a(x^n)+\gamma\,r(x^n),
 \tag{52}
$$



where



$$
\beta=u-sv,\qquad
 \gamma=\lambda+4v\log2.
 \tag{53}
$$



For $n=0,1,2,3\pmod4$, the periodic part in (52) is



$$
\gamma,\quad2\beta,\quad-\gamma,\quad-2\beta.
 \tag{54}
$$



Because $J(x^n)\to0$ and $m_n$ converges, the four values in (54) must
be equal. Hence



$$
\boxed{\beta=\gamma=0.}
 \tag{55}
$$



Equations (51), (53), and (55) reduce the positive extension to



$$
\widetilde\ell=vJ.
 \tag{56}
$$



Since $J(1)>0$ and $\widetilde\ell(1)\geq0$, we have $v\geq0$.
Therefore every dual vector is of the form



$$
(u,v)=v(s,1),\qquad v\geq0.
 \tag{57}
$$



Conversely, (8) shows immediately that every vector in (57) is nonnegative
on the cone. We have proved the exact dual identity



$$
\boxed{
 \mathcal C_{\mathbb R}^*
 =\mathbb R_{\geq0}(s,1).}
 \tag{58}
$$



## 6. From the dual to the exact real cone

The bipolar theorem for convex cones in the finite-dimensional output
space gives



$$
\overline{\mathcal C_{\mathbb R}}
=\mathcal C_{\mathbb R}^{**}
=\{(a,c):sa+c\geq0\}.
\tag{59}
$$



We need slightly more than the closure. A standard elementary convex fact
is



$$
\operatorname {ri}(C)=\operatorname {ri}(\overline C)
 \tag{60}
$$



for every nonempty convex set in finite-dimensional space. In this
two-dimensional situation it can be seen directly: place a small triangle
around an interior point of $\overline C$, approximate its three vertices
by points of $C$, and make the approximations small enough that the
original point remains in their convex hull. Convexity then puts the point
in $C$.

Applying (60) to (59) proves



$$
\{(a,c):sa+c>0\}\subset\mathcal C_{\mathbb R}.
 \tag{61}
$$



The reverse inclusion follows from (8). Moreover, if $H\geq0$ is
nonzero, then $(1-x)^2H$ is positive on a nonempty subinterval and
$W>0$, so



$$
J(H)>0.
 \tag{62}
$$



Thus no nonzero output lies on the boundary $sa+c=0$. The zero polynomial
gives $(0,0)$. Equations (61)--(62) prove Theorem 1.

## 7. Rational lifting with strict positivity

Let



$$
y=(a,c)\in\mathbb Q^2,\qquad sa+c>0.
 \tag{63}
$$



Write



$$
y_*=(16,-85)=T((1-x)^2H_*).
 \tag{64}
$$



Since $sy_{*,1}+y_{*,2}=J(H_*)>0$, choose a sufficiently small rational
$\varepsilon>0$ such that



$$
y-\varepsilon y_*
 \tag{65}
$$



still lies in the open half-plane. By Theorem 1, there is a real polynomial
$K\geq0$ in the common plane with output (65). Then



$$
H=K+\varepsilon H_*
 \tag{66}
$$



has output exactly $y$ and satisfies



$$
H\geq3\varepsilon>0
 \quad(0\leq x\leq1).
 \tag{67}
$$



Fix a degree containing $H$. The equations



$$
r=0,\qquad\alpha=0,\qquad a=y_1,\qquad c=y_2
 \tag{68}
$$



are an affine linear system with rational coefficients and rational
right-hand side. A rational affine system which has a real solution has a
rational particular solution and a nullspace basis over $\mathbb Q$.
Consequently its rational points are dense in its real solution space.

Approximate the coefficients of $H$ within this exact affine fiber by a
rational solution $H_{\mathbb Q}$. The approximation can be made so
small in coefficient $\ell^1$-norm that (67) remains strict. Thus



$$
H_{\mathbb Q}>0,\qquad
 r(H_{\mathbb Q})=\alpha(H_{\mathbb Q})=0,\qquad
 (a(H_{\mathbb Q}),c(H_{\mathbb Q}))=y.
 \tag{69}
$$



This proves the rational assertion in Theorem 2.

Clear the coefficients of $H_{\mathbb Q}$ by a positive common
denominator, then divide their integer content. The resulting polynomial
$H_{\mathbb Z}$ is primitive and positive. Since $(1-x)^2$ is primitive,
Gauss's lemma shows that



$$
F_{\mathbb Z}=(1-x)^2H_{\mathbb Z}
 \tag{70}
$$



is primitive as well. Its output is a positive rational multiple of $y$.
Therefore its fully primitive integer output is the primitive lattice
vector on the ray through $y$.

Taking $y=(q,k)$ proves (12). Taking $k=-p$ proves the lower-approximant
realizability statement (14).

The raw target in this factor class is always divisible by four, as proved
in the companion lattice note. This does not restrict primitive output
rays: denominator clearing and output cross-content absorb the required
raw scaling.

## 8. Exact primitive-output classification

Let $\mathscr P$ denote the set of fully primitive output pairs of
primitive integer polynomials in the factor-endpoint positive cone.
Theorems 1--2 give the exact classification



$$
\boxed{
 \mathscr P
 =
 \{(q,k)\in\mathbb Z^2:
 \gcd(q,k)=1,\ q(e+\pi)+k>0\}.}
 \tag{71}
$$



The phrase “closure of the primitive cone” needs care. The literal set of
primitive lattice points is discrete in $\mathbb R^2$, so its ordinary
Euclidean closure is itself. The precise statements are:

1. the real output cone is exactly (7);
2. every rational ray in its open half-plane is represented by a primitive
   integer polynomial;
3. the projective directions of primitive outputs are therefore all
   rational directions in the open half-plane and are dense in its
   projectivization;
4. the closure of the real cone is the closed half-plane in (59).

These formulations separate Euclidean closure, conical closure, and
primitive-ray density.

## 9. Why universality does not prove irrationality

Suppose first that



$$
s=\frac PQ
 \tag{72}
$$



is rational in lowest terms. For all integers $q,k$,



$$
qs+k=\frac{qP+kQ}{Q}.
 \tag{73}
$$



If this value is positive, its numerator is a positive integer, so



$$
qs+k\geq\frac1Q.
 \tag{74}
$$



The boundary primitive ray $(Q,-P)$ has value zero and is excluded by
positivity. Thus no sequence of primitive positive values can tend to zero.

If $s$ is irrational, its continued-fraction convergents contain
infinitely many lower convergents $p_n/q_n$ with



$$
0<q_ns-p_n<\frac1{q_n}\longrightarrow0.
 \tag{75}
$$



Theorem 2 realizes every ray $(q_n,-p_n)$ by a primitive positive integer
polynomial. Hence a shrinking family exists.

Combining (74)--(75),



$$
\boxed{
\begin{aligned}
e+\pi\text{ irrational}
\quad\Longleftrightarrow\quad&
\text{there are primitive positive factor-endpoint}\\
&\text{common-kernel forms tending to zero.}
\end{aligned}}
\tag{76}
$$



This equivalence explains the finite Bernstein experiments. Their many
small changing rays are manifestations of a universal cone, not evidence
that the decisive infinite arithmetic step has already occurred. Any proof
that extracts a shrinking sequence must add information which rules out the
rational boundary case; continuous optimization or cone density alone
cannot do so.

## 10. Scope and relation to the finite construction

The companion finite package constructs fourteen explicit primitive
degree-66 witnesses, ending with



$$
1246188493618(e+\pi)-7302508153575
=3.273998315\ldots\times10^{-13}.
\tag{77}
$$



The present theorem explains why every strict rational lower ray is
realizable, not merely those fourteen. Its proof is existential: the
positive-extension and bipolar arguments do not give useful degree,
coefficient-height, denominator, or cross-content bounds for a requested
ray. The prior Bernstein construction remains valuable as an explicit,
deterministically checkable realization with quantitative positivity
margins.

Nothing here proves irrationality, algebraicity, or transcendence of
$e+\pi$.

## 11. Deterministic algebraic certificate

Run

    python -m py_compile scripts/factor_endpoint_positive_cone_universality_certificate.py
    python scripts/factor_endpoint_positive_cone_universality_certificate.py

The script writes

    results/factor_endpoint_positive_cone_universality_certificate.json

using only the Python standard library. It verifies:

- the extended Euclidean-division identity (17) on the monomial basis
  through degree 256;
- the exact formulas (46) and the corresponding $B(f_n)$ formula;
- the independence matrix (26);
- the order-unit data (27)--(29);
- the positive target-zero direction (31)--(32);
- the four-cycle (54);
- all concrete integer and rational identities used in the dual proof.

The positive-extension lemma, the all-degree factorial-growth argument,
the convex bipolar step, and the rational-density lifting are proofs in
this note, not finite-computation inferences.
