> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# An integral-jet pullback whose Taylor radius exceeds $3/2$

## Scope

Put



$$
F(w)=4\arctan\frac{w}{2-w}
    =4\int_0^w\frac{dt}{t^2-2t+2},
\qquad
\phi(z)=z+\frac{z^7-z^8}{140},
\qquad
G(z)=F(\phi(z)).
\tag{1}
$$



This note proves exactly that



$$
G(1)=\pi,\qquad G^{(n)}(0)\in\mathbb Z\quad(n\geq0),
\qquad \rho(G)>\frac32,
\tag{2}
$$



where $\rho(G)$ is the radius of the Taylor series at the origin.
The radius statement is certified by eight rational Schur--Cohn
inequalities.  Numerical roots are reported only as a diagnostic.

This substantially improves the previously certified lower bound
$\rho(G)>\sqrt2$ for a degree-five composition.  It still does not decide
whether $e+\pi$ is algebraic or transcendental: in the standard diagonal
endpoint-matched Hermite--Padé construction, the primitive endpoint forms
again grow rapidly.

## 1. Endpoint and all-order derivative-jet integrality

The endpoint identities are immediate:



$$
\phi(0)=0,\qquad
\phi(1)=1,\qquad
G(1)=F(1)=4\arctan(1)=\pi.
\tag{3}
$$



The only nonzero derivative jets of $\phi$ at zero are



$$
\phi'(0)=1,\qquad
\phi^{(7)}(0)=\frac{7!}{140}=36,\qquad
\phi^{(8)}(0)=-\frac{8!}{140}=-288.
\tag{4}
$$



Thus $\phi$ is an integral Hurwitz polynomial.  The base function has the
already derived jets



$$
F^{(k)}(0)
=4(k-1)!2^{-k/2}\sin\frac{k\pi}{4}\in\mathbb Z
\qquad(k\geq1),
\tag{5}
$$



and $F(0)=0$.  Faà di Bruno's formula gives



$$
G^{(n)}(0)
=\sum_{k=1}^n F^{(k)}(0)
B_{n,k}\!\left(\phi'(0),\phi''(0),\ldots,
\phi^{(n-k+1)}(0)\right),
\tag{6}
$$



where every exponential partial Bell polynomial $B_{n,k}$ has integer
coefficients.  Equations (4)--(6) prove



$$
\boxed{G^{(n)}(0)\in\mathbb Z\quad(n\geq0).}
\tag{7}
$$



This is an all-order proof; the archived finite jet computation is only an
independent consistency check.

## 2. Every preimage of $1\pm i$ is a genuine singularity

Differentiation of (1) gives



$$
G'(z)=
\frac{4\phi'(z)}
 {(\phi(z)-(1+i))(\phi(z)-(1-i))}.
\tag{8}
$$



The only finite singularities of the continued germ $F$ occur at
$1+i$ and $1-i$.  Suppose that $\phi(z)-(1+i)$ has multiplicity
$m$ at $z_0$.  In characteristic zero, $\phi'$ then has multiplicity
exactly $m-1$ there, while
$\phi(z_0)-(1-i)=2i\ne0$.  Hence (8) has a simple pole at $z_0$.
The same argument applies to a preimage of $1-i$.  Integration shows that
each such point is a genuine logarithmic singularity of $G$.

Consequently,



$$
\rho(G)=
\min\{|z|:\phi(z)=1+i\text{ or }\phi(z)=1-i\}.
\tag{9}
$$



Because $\phi$ has real coefficients, the two root sets are conjugate and
have identical modulus multisets.

## 3. The exact Schur--Cohn certificate at radius $3/2$

Let $q(z)=\phi(z)-(1+i)$, set $r=3/2$, and reverse the polynomial:



$$
\begin{aligned}
P_0(w)
&=w^8q(r/w)\\
&=-(1+i)w^8+\frac32w^7
  +\frac{(3/2)^7}{140}w-\frac{(3/2)^8}{140}.
\end{aligned}
\tag{10}
$$



The roots of $q$ are all outside $|z|=3/2$ if and only if the roots of
$P_0$ are all inside $|w|=1$.

For a degree-$d$ polynomial written in leading-to-constant order,



$$
P(w)=a_0w^d+a_1w^{d-1}+\cdots+a_d,
\tag{11}
$$



let



$$
P^*(w)=\overline{a_d}w^d+\overline{a_{d-1}}w^{d-1}
       +\cdots+\overline{a_0}.
\tag{12}
$$



After dividing $P$ by its leading coefficient, write its constant
coefficient as $c$.  If



$$
g=1-|c|^2>0,
\tag{13}
$$



Cohn's degree-reduction rule replaces $P$ by



$$
\mathcal S(P)(w)=\frac{P(w)-cP^*(w)}{w}.
\tag{14}
$$



The numerator has zero constant coefficient and leading coefficient $g$.
The rule states that $P$ has all $d$ roots in the open unit disk if and
only if $\mathcal S(P)$ has all $d-1$ roots there.  Repeated strict
positivity of (13), down to a nonzero constant, is therefore an exact
unit-disk certificate.

All coefficients in (10) lie in $\mathbb Q(i)$, so this recursion can be
performed with pairs of rational numbers and no rounding.  For degrees
$8,7,\ldots,1$, the exact gaps $g_d=N_d/D_d$ are as follows:



$$
\begin{array}{c|l|l}
d&N_d&D_d\\ \hline
8&
2525964479&
2569011200\\
7&
6317523106902195841&
6380496549169741441\\
6&
39450445465937677644152548903700839681&
39911098206243173380123161627517697281\\
5&
240551396495599056479431912924123809898616954289959041921&
243921085995014014563270043553716849801921831267879451521\\
4&
1425197321976377542680969292930773219060548589019365717409088922866968066561&
1449846708225414395046305916837484398337158131041889460615718994105991068161\\
3&
8146920681362684064892046292848997328034586336120933153202306042841556150121244026297018857601&
8327231728585194206241258262787733365923212893432712496758122636392063861681034842234684291201\\
2&
44459870044186827322831567768544620916244372663053060091952497532456189630493711788478095317643497900667485239041&
45778851110165646801672053999078965887495299164299552325737582034526966877537866652826994014883209170433889744641\\
1&
6344832614739421075321842648155146717176321871398108246371484643860044733399065089126273096673577717282891108352865025894992844445&
237375409832845050902758983163994662442399057974133180579480739995205376887080055775369104622672617183250336858889738930017728132481
\end{array}
\tag{15}
$$



Every numerator and denominator in (15) is a positive integer.  Therefore
all eight Schur--Cohn steps are strict, and every root of $P_0$ lies in
the open unit disk.  Every solution of $\phi(z)=1+i$ consequently has
$|z|>3/2$.  Conjugation gives the same conclusion for $1-i$, and (9)
proves



$$
\boxed{\rho(G)>\frac32.}
\tag{16}
$$



The exact program stores the normalized constant $c$ at each stage as
well as the gap (15), so every step can be checked by direct rational
arithmetic.

## 4. Numerical location of the first singularity

High-precision root finding, used only as a diagnostic, gives



$$
\rho(G)=
1.5598556036265734152460990842856358069875\ldots.
\tag{17}
$$



One nearest preimage of $1+i$ is



$$
1.16433155822099191225031075176119\ldots
+1.03801807628571605490782537646711\ldots\,i.
\tag{18}
$$



The strict rational theorem (16) does not depend on these decimal
approximations.

## 5. Exact finite diagonal endpoint systems

For $1\leq n\leq15$, an exact program constructs



$$
A_n(z)+B_n(z)e^z+C_n(z)G(z)=O(z^{3n+1}),
\qquad C_n(1)=B_n(1),
\tag{19}
$$



with $\deg A_n,\deg B_n,\deg C_n\leq n$.  In every case the
$(2n+1)$-by-$(2n+2)$ high-jet-plus-endpoint matrix has full row rank,
its kernel has dimension one, and the coefficient at the first
unconstrained order $3n+1$ is nonzero.

At $n=1$, the endpoint value is identically zero, so this member is
degenerate.  For $n=2,\ldots,15$, directed rational interval arithmetic
certifies the following base-ten decades for the fully reduced nonzero
endpoint forms:



$$
0,\ 7,\ 15,\ 26,\ 44,\ 64,\ 89,\ 119,\ 150,\ 191,\ 233,\
281,\ 331,\ 385.
\tag{20}
$$



The digit counts of the exact maximal-cofactor common contents, for
$n=1,\ldots,15$, are



$$
1,\ 1,\ 3,\ 6,\ 12,\ 20,\ 30,\ 42,\ 58,\ 77,\ 100,\ 125,\
155,\ 190,\ 228.
\tag{21}
$$



Thus the larger analytic radius improves the finite diagonal behavior
relative to the degree-five composition, but the primitive endpoint forms
still grow very rapidly.  The finite calculation proves no all-degree rank,
height, content, or asymptotic theorem.

## 6. Reproducible artifacts and surviving question

The exact radius/jet certificate is
scripts/high_radius_composed_pullback_certificate.py, with output
results/high_radius_composed_pullback_certificate.json.

The exact finite Hermite--Padé probe is
scripts/high_radius_composed_pullback_hp_probe.py, with output
results/high_radius_composed_pullback_hp_n15.json.

The surviving question is whether a non-diagonal degree allocation,
singularity-softening factor, or provable determinant divisor can exploit
the radius gain in (16) without losing it to primitive coefficient height.
Nothing in this note establishes that decisive arithmetic estimate.
