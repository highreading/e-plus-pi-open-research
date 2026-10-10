> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of mixed $E$-function, $G$-function, and
# logarithm-value theorems for $e+\pi$

Date: 2026-08-27 (UTC)

## 1. Scope and verdict

Put


$$
({\rm H})\qquad s=e+\pi\in\overline{\mathbb Q}.
$$


This note asks a specific question: can one combine the strongest
currently available theorems on values and logarithms of
$E$-functions, functional or value algebraic independence of
$E$- and $G$-functions, or interpolation by $E$-functions, with
a choice of functions and algebraic points that contradicts
$({\rm H})$?

The audited results do **not** presently give such a contradiction.
There is, however, an exact explanation stronger than a generic
failure of hypotheses:

> **Forced-collision principle.** If $({\rm H})$ holds and
> $F(x)=e,\ G(y)=\pi$ for $E$-functions $F,G$ and nonzero
> algebraic $x,y$, then the scaled Borel singularity sets of $F$
> and $G$ must intersect. In particular, if $F(z)=e^z$ and $x=1$,
> then
> 

$$
> y\in\mathfrak S(G).
>
$$



Thus no exact $E$-function interpolation of $\pi$ can be chosen
with Borel support separated from that of the exponential: the
hypothetical algebraic relation itself forces the precise obstruction
to Delaygue's Lindemann--Weierstrass theorem for $E$-functions.

Likewise, if an $E$-function assumes an algebraic exponential value
$F(x)=e^\eta$ at a nonzero algebraic point, then


$$
\frac{x}{\eta}\in\mathfrak S(F).
$$


This puts every such construction in exactly the exceptional branch
of Fischler--Rivoal's logarithm theorem. Polynomial perturbations,
interpolation theorems, and regularity of minimal differential
equations cannot remove this obstruction.

The mixed $E/G$ route reaches a different exact frontier. Under
$({\rm H})$, both $e$ and $\pi$ would belong to the value-ring
intersection


$$
\mathbf E\cap\mathbf G
$$


and would be transcendental. The conjectural identity
$\mathbf E\cap\mathbf G=\overline{\mathbb Q}$ would therefore
contradict $({\rm H})$, but this identity is not a theorem.
Functional independence results, including recent $p$-adic results
mixing $E$- and $G$-functions, do not specialize to the required
complex values.

No proof of either algebraicity or transcendence of $e+\pi$ is
claimed here.

## 2. Conventions that must not be conflated

An $E$-function is written


$$
F(z)=\sum_{n\geq0}\frac{a_n}{n!}z^n
$$


with algebraic coefficients satisfying the usual Siegel growth and
holonomy conditions. Its inverse Borel transform is the $G$-series


$$
\psi(F)(t)=\sum_{n\geq0}a_nt^n.
$$


Following Delaygue and Fischler--Rivoal, let
$\mathfrak S(F)$ denote the finite set of finite singularities of
the analytic continuation of $\psi(F)$.

Three notions play different roles:

1. $\mathfrak S(F)$ is a set of singularities in the **Borel
   variable** $t$.
2. A singularity of the minimal homogeneous or inhomogeneous
   differential equation of $F(z)$ is a singularity in the
   **original variable** $z$.
3. A $G$-value is an analytically continued value of a $G$-function
   at an algebraic point; it is not in general a finite algebraic-point
   value of the associated $E$-function.

For $\lambda\in\overline{\mathbb Q}^{\,*}$,


$$
\psi(F(\lambda z))(t)=\psi(F)(\lambda t),
\qquad
\mathfrak S(F(\lambda z))
=\{\rho/\lambda:\rho\in\mathfrak S(F)\}.             \tag{2.1}
$$


For the exponential,


$$
\psi(e^z)(t)=\frac1{1-t},
\qquad
\mathfrak S(e^z)=\{1\}.                              \tag{2.2}
$$



The distinction above is essential below. In particular, regularity of
a minimal differential equation at $z=1$ says nothing by itself
about whether $1\in\mathfrak S(F)$.

## 3. The primary results used in this audit

### 3.1 Delaygue's $E$-function Lindemann--Weierstrass theorem

For $E$-functions $F_1,\ldots,F_r$ whose sets
$\mathfrak S(F_i)$ are pairwise disjoint, and an algebraic point
$a$ at which every $F_i(a)$ is transcendental, Delaygue's
Theorem 2.1 states that


$$
1,F_1(a),\ldots,F_r(a)
$$


are linearly independent over $\overline{\mathbb Q}$.

The theorem is stated in the strict $E$-function setting in the
preprint audited here. Fischler--Rivoal's later logarithm paper
explicitly explains why the same argument and the required structural
inputs extend to Siegel $E$-functions. Nothing below needs a broader
version than the strict case when the chosen functions are strict.

The same-point theorem immediately gives the following different-point
form, which is the precise form needed here.

**Lemma 3.1 (scaled-support criterion).** Let $F_1,\ldots,F_r$ be
$E$-functions, let $x_1,\ldots,x_r$ be nonzero algebraic numbers,
and assume every $F_i(x_i)$ is transcendental. If


$$
\frac{\rho_i}{x_i}\ne\frac{\rho_j}{x_j}
\quad
(i\ne j,\ \rho_i\in\mathfrak S(F_i),\
\rho_j\in\mathfrak S(F_j)),                          \tag{3.1}
$$


then $1,F_1(x_1),\ldots,F_r(x_r)$ are linearly independent over
$\overline{\mathbb Q}$.

**Proof.** Apply Delaygue's theorem at the common point $1$ to
$\widetilde F_i(z)=F_i(x_i z)$. Equation (2.1) identifies the
singularity set of $\widetilde F_i$ with
$\mathfrak S(F_i)/x_i$, so (3.1) is exactly pairwise disjointness.
$\square$

The contrapositive of Lemma 3.1 is unconditional and will be the main
tool in Section 4.

### 3.2 Fischler--Rivoal on logarithms of $E$-functions

The final published paper is:

S. Fischler and T. Rivoal, *Transcendence of values of logarithms of
$E$-functions*, Math. Ann. **394** (2026), article 12,
DOI [10.1007/s00208-026-03374-z](https://doi.org/10.1007/s00208-026-03374-z);
preprint [arXiv:2409.18537](https://arxiv.org/abs/2409.18537).

The results relevant to this problem are:

* If transcendental $E$-functions $f,g$ are not related by
  $f(z)=g(\beta z)$ for an algebraic $\beta$, then only finitely
  many pairs of nonzero algebraic points can satisfy
  $f(\xi)=g(\eta)$ (Theorem 1).
* In particular, for a transcendental $E$-function $f$ not equal
  to $e^{\beta z}$, only finitely many algebraic points can have an
  algebraic determination of $\log f(\xi)$ (Corollary 1).
* More precisely, their proof and Proposition 1 show that a
  transcendental equality $f(\xi)=g(\eta)$ at nonzero algebraic
  points forces
  

$$
\frac{\xi}{\eta}
  =
  \frac{\rho_f}{\rho_g}
  \quad\text{for some}\quad
  \rho_f\in\mathfrak S(f),\
  \rho_g\in\mathfrak S(g).                           \tag{3.2}
$$


* Consequently, an algebraic determination of $\log f(\xi)$ occurs
  only in the trivial branch $f(\xi)=1$, or in the Borel-exceptional
  branch
  

$$
f(\xi)=\exp(\xi/\rho)
  \quad\text{for some }\rho\in\mathfrak S(f).         \tag{3.3}
$$



Their quantitative Theorem 2 assumes that $f\in\mathbb Q[[z]]$ is a
strict $E$-function, $\xi\in\mathbb Q^*$, $f(\xi)>0$, and
$\log f(\xi)\notin\mathbb Q$. It gives effectively computable
constants $c,d>0$ such that


$$
\left|\log f(\xi)-\frac ab\right|
\ge \exp(-c b^d)
\qquad(a\in\mathbb Z,\ b\ge1).                       \tag{3.4}
$$


The theorem presupposes that the chosen logarithm is outside the
rational branch; it does not prove that (3.3) fails, and it does not
give algebraic independence of two logarithms or forbid an algebraic
sum of logarithms.

### 3.3 Beukers' specialization theorem

Let $Y=(F_1,\ldots,F_r)^T$ be a vector of $E$-functions satisfying


$$
Y'=A(z)Y,\qquad A(z)\in M_r(\overline{\mathbb Q}(z)),
$$


and let $T$ be a common denominator of the entries of $A$. At an
algebraic $\alpha$ with $\alpha T(\alpha)\ne0$, Beukers'
refinement of Siegel--Shidlovskii says:

* the transcendence degree of the values equals the functional
  transcendence degree; and
* every homogeneous algebraic relation among the values is the
  specialization of a homogeneous functional relation (Theorem 1.3
  and Corollary 1.4 in the cited paper; adjoining the constant function
  $1$ treats inhomogeneous relations).

This is a powerful **functional-to-value** transfer theorem. It is not
a theorem that arbitrary separately interpolated $E$-functions are
functionally independent, nor is it a mixed $E/G$ specialization
theorem.

Primary source:

F. Beukers, *A refined version of the Siegel--Shidlovskii theorem*,
Ann. of Math. (2) **163** (2006), 369--379,
[arXiv:math/0405549](https://arxiv.org/abs/math/0405549).

### 3.4 Interpolation by $E$-functions

Fischler--Rivoal's current interpolation theorem says, in particular,
that every $\xi$ in the ring $\mathbf E$ of $E$-values has a
representation $F(1)=\xi$ for which $1$ is not a singularity of
either the minimal homogeneous or minimal inhomogeneous differential
equation of $F$. Their general theorem prescribes finitely many jets
at finitely many nonzero algebraic points and describes exactly when
those points are singularities of the two minimal equations.

Primary source:

S. Fischler and T. Rivoal, *On the singularities of differential
equations satisfied by $E$-functions*,
[arXiv:2604.20332](https://arxiv.org/abs/2604.20332), Theorems 3--4.

Again, these are singularities of equations in the original
$z$-plane, not the Borel singularities $\mathfrak S(F)$.

## 4. The exact forced collision under $e+\pi\in\overline{\mathbb Q}$

The next theorem is a direct, rigorous reduction of the proposed
strategy.

**Theorem 4.1 (forced Borel collision).** Assume $({\rm H})$. Let
$F,G$ be $E$-functions and let $x,y\in\overline{\mathbb Q}^{\,*}$
satisfy


$$
F(x)=e,\qquad G(y)=\pi.                              \tag{4.1}
$$


Then there exist $\rho_F\in\mathfrak S(F)$ and
$\rho_G\in\mathfrak S(G)$ such that


$$
\boxed{\frac{\rho_F}{x}=\frac{\rho_G}{y}}.           \tag{4.2}
$$



**Proof.** Both $e$ and $\pi$ are transcendental. Under
$({\rm H})$,


$$
F(x)+G(y)-s=0                                        \tag{4.3}
$$


is a nontrivial $\overline{\mathbb Q}$-linear relation among
$1,F(x),G(y)$. If the two scaled singularity sets were disjoint,
Lemma 3.1 would make those three numbers linearly independent. Hence
the scaled sets intersect, which is precisely (4.2). $\square$

**Corollary 4.2 (canonical exponential).** Assume $({\rm H})$. If
$G$ is any $E$-function and


$$
G(y)=\pi,\qquad y\in\overline{\mathbb Q}^{\,*},
$$


then


$$
\boxed{y\in\mathfrak S(G)}.                          \tag{4.4}
$$



**Proof.** Take $F(z)=e^z$, $x=1$, and use
$\mathfrak S(F)=\{1\}$ in (4.2): $1=\rho_G/y$.
$\square$

This statement rules out an entire family of attempted applications,
not just one convenient representation. For example, the elementary
conditional interpolant


$$
G_y(z)=s-e^{z/y}
$$


satisfies $G_y(y)=\pi$, and indeed
$\mathfrak S(G_y)=\{y\}$. More elaborate exact interpolants cannot
move all Borel singularities away from $y$, because Corollary 4.2
forbids it.

There is also a useful compatibility check with the 2026 interpolation
theorem. Under $({\rm H})$, $\pi=s-e$ lies in $\mathbf E$, so
Fischler--Rivoal produce an $E$-function $G$ with $G(1)=\pi$ and
with $1$ regular for both minimal differential equations. Yet
Corollary 4.2 forces


$$
1\in\mathfrak S(G).                                  \tag{4.5}
$$


There is no contradiction: (4.5) is a Borel-plane singularity, while
the interpolation theorem controls original-variable differential
singularities. This gives an exact conditional example showing why
the two notions cannot be substituted for one another.

## 5. Every exact algebraic logarithm is forced into the exceptional set

**Theorem 5.1 (forced logarithmic exception).** Let $F$ be an
$E$-function and let $x,\eta\in\overline{\mathbb Q}^{\,*}$. If


$$
F(x)=e^\eta,                                         \tag{5.1}
$$


then


$$
\boxed{\frac{x}{\eta}\in\mathfrak S(F)}.             \tag{5.2}
$$



**Proof.** The value $e^\eta$ is transcendental by
Hermite--Lindemann. Apply Fischler--Rivoal's equality transfer (3.2)
to $F(x)=\exp(\eta)$. Since $\mathfrak S(\exp)=\{1\}$, equation
(3.2) gives $x/\eta=\rho_F$ for some
$\rho_F\in\mathfrak S(F)$. $\square$

Thus (5.1) is exactly of the exceptional form (3.3):


$$
F(x)=\exp(x/\rho_F).
$$


The logarithm theorem is internally consistent with every exact
interpolation; it does not contradict it.

Two consequences dispose of common perturbative attempts.

1. If
   

$$
F(z)=e^{\beta z}+(z-x)H(z)
$$


   is an $E$-function and $F(x)=e^{\beta x}$, then, provided the
   value is nontrivial,
   

$$
\beta^{-1}\in\mathfrak S(F).
$$


   Adding a vanishing correction cannot remove the singularity
   responsible for the logarithmic exception.

2. Under $({\rm H})$, any $E$-function $F$ with
   $F(1)=e^s$ necessarily has $s^{-1}\in\mathfrak S(F)$. A regular
   interpolant in the sense of the minimal differential equation may
   exist, but it remains Borel-exceptional.

The sign cannot be used to manufacture a second algebraic logarithm.
If $\alpha,\beta\in\overline{\mathbb Q}$, $\beta\ne0$, and
$e^\alpha=-e^\beta$, then $e^{\alpha-\beta}=-1$ would be
algebraic, contradicting Hermite--Lindemann because
$\alpha-\beta\ne0$; equality $\alpha-\beta=0$ would give
$1=-1$. Hence $-e^\beta$ has no algebraic logarithm.

Finally, the quantitative one-logarithm theorem cannot be iterated into
the needed conclusion. Under $({\rm H})$ one would need a theorem
that forbids an algebraic relation between two logarithms, or their
sum. A lower bound for rational approximation to one already-known
irrational logarithm has no such consequence.

### 5.1 The direct logarithm of an algebraic number is still mixed

Choose the standard determination


$$
\log(-1)=i\pi.
$$


Then $({\rm H})$ is equivalently


$$
e-i\log(-1)=s\in\overline{\mathbb Q}.                \tag{5.3}
$$


This does not fall under Baker's theorem on linear forms in logarithms:
that theorem requires every variable in the linear form to be a
logarithm of a nonzero algebraic number, whereas $e$ is an
$E$-value and is not supplied as such a logarithm. Rewriting
$e=\log(e^e)$ is only formal for this purpose, because $e^e$ is
not an algebraic input to Baker's theorem. Fischler--Rivoal's theorem
also does not combine an $E$-value with $\log(-1)$; it concerns
the logarithm of a single $E$-function value and, in its quantitative
part, rational approximation to that one logarithm. Thus (5.3)
isolates another exact missing theorem: linear independence between a
nonalgebraic $E$-value and logarithms of algebraic numbers.

## 6. Why $\pi$ as a $G$-value does not become a finite
$E$-function value

The elementary representation $\pi=4\arctan(1)$ makes $\pi$ a
$G$-value. Its exact inverse-Borel partner is


$$
\operatorname{Si}(z)
=\sum_{n\ge0}
\frac{(-1)^n z^{2n+1}}{(2n+1)(2n+1)!}.
$$


This is an $E$-function, and


$$
\psi(\operatorname{Si})(t)=\arctan t,
\qquad
\mathfrak S(\operatorname{Si})=\{i,-i\}.             \tag{6.1}
$$


But


$$
\pi=4\,\psi(\operatorname{Si})(1),                   \tag{6.2}
$$


not $4\operatorname{Si}(1)$. The Borel transform is not
evaluation-preserving, so Delaygue's and Fischler--Rivoal's finite
algebraic-point value theorems do not apply to (6.2).

There is an equivalent infinity representation:


$$
\lim_{x\to+\infty}2\operatorname{Si}(x)=\pi.          \tag{6.3}
$$


Fischler--Rivoal prove that the ring of $G$-values is exactly the
ring of finite directional limits at infinity of $E$-functions (and
also of corresponding convergent $E$-integrals). This is a precise
bridge between $\mathbf G$ and $E$-functions, but its endpoint is
infinity rather than a nonzero algebraic point. Beukers' and
Delaygue's value theorems do not specialize at infinity.

Under $({\rm H})$, this bridge gives the transparent conditional
example


$$
L_s(z)=s(1-e^{-z})-2\operatorname{Si}(z),
$$


which is an $E$-function and satisfies


$$
\lim_{x\to+\infty}L_s(x)=s-\pi=e.                    \tag{6.4}
$$


Equation (6.4) recovers the conditional fact $e\in\mathbf G$, but it
does not turn that limit into a finite-point $E$-value theorem.

Primary source for this bridge:

S. Fischler and T. Rivoal, *Relations between values of arithmetic
Gevrey series, and applications to values of the Gamma function*,
J. Number Theory **261** (2024), 36--54,
[DOI 10.1016/j.jnt.2024.02.016](https://doi.org/10.1016/j.jnt.2024.02.016),
[arXiv:2301.13518](https://arxiv.org/abs/2301.13518) (the archived
source version states the same theorem).

## 7. The exact $E/G$ value-ring frontier

Let $\mathbf E$ and $\mathbf G$ be the rings of $E$-values and
$G$-values. Unconditionally,


$$
e=e^1\in\mathbf E,\qquad
\pi=4\arctan(1)\in\mathbf G.
$$


Under $({\rm H})$, closure under algebraic constants and subtraction
gives


$$
\pi=s-e\in\mathbf E,\qquad
e=s-\pi\in\mathbf G.
$$


Therefore


$$
e,\pi\in\mathbf E\cap\mathbf G                      \tag{7.1}
$$


and both elements of the intersection are transcendental.

Consequently, the conjecture


$$
\mathbf E\cap\mathbf G=\overline{\mathbb Q}           \tag{7.2}
$$


would disprove $({\rm H})$. But (7.2) is not among the theorems in
the audited sources. Fischler--Rivoal explicitly describe it as a
natural conjecture whose proof is out of reach. Their proved
functional statement that an entire $G$-function must be a
polynomial, or the corresponding intersection statement for
**function classes**, does not imply (7.2) for value rings: the two
representations of a number need not arise from the same function.

The following exact division obstruction shows why a naive attempt to
force them into one function fails.

**Proposition 7.1 (mixed zero cannot be divided out).** For every
$\alpha\in\overline{\mathbb Q}$, define


$$
H_\alpha(z)=\alpha-e^z-4\arctan z,\qquad
Q_\alpha(z)=\frac{H_\alpha(z)}{z-1}.
$$


Then


$$
Q_\alpha\notin\mathcal E+\mathcal G,                 \tag{7.3}
$$


where $\mathcal E,\mathcal G$ denote the $E$- and $G$-function
classes.

**Proof.** Suppose $Q_\alpha=E+G$ with
$E\in\mathcal E,\ G\in\mathcal G$. Then


$$
R(z):=(\alpha-e^z)-(z-1)E(z)
      =(z-1)G(z)+4\arctan z.
$$


The left side belongs to $\mathcal E$, and the right side to
$\mathcal G$. Hence $R\in\mathcal E\cap\mathcal G$.

For completeness, a $G$-function that is entire is a polynomial.
Indeed, put all its coefficients $a_n$ in a fixed number field
$K$. The $G$-growth conditions give $C>1$ and integers
$D_n\le C^n$ such that $D_na_j$ is integral for $j\le n$ and
$|\sigma(a_n)|\le C^n$ for every embedding 

$$
\sigma:K\hookrightarrow
\mathbb C
$$

. If $a_n\ne0$, the product formula applied to the
nonzero algebraic integer $D_na_n$ gives, at the distinguished
embedding,


$$
|a_n|
\ge D_n^{-1}
    \prod_{\sigma\ne{\rm id}}|D_n\sigma(a_n)|^{-1}
\ge C^{-c_K n}                                      \tag{7.4}
$$


for a constant $c_K$. Infinitely many nonzero coefficients would
therefore give finite radius of convergence. Hence an entire
$G$-function has only finitely many nonzero coefficients. Since
every $E$-function is entire,
$\mathcal E\cap\mathcal G=\overline{\mathbb Q}[z]$. But


$$
R(1)=\alpha-e
$$


is transcendental, whereas a polynomial with algebraic coefficients
has an algebraic value at $1$, a contradiction. $\square$

If $\alpha=s$ under $({\rm H})$, then $H_s(1)=0$, so
$Q_s$ is holomorphic at $1$; nevertheless (7.3) says that the
zero-removal operation leaves the mixed class. This is an exact
functional obstruction to converting the hypothetical value relation
into a forbidden common functional identity.

## 8. What Beukers' specialization theorem does and does not transfer

Suppose one found $E$-functions $F,G$ with
$F(x)=e,\ G(y)=\pi$, rescaled them to a common point $1$, put


$$
1,\quad F(xz),\quad G(yz)
$$


in a first-order $E$-system regular at $1$, and proved the three
functions linearly independent over $\overline{\mathbb Q}(z)$.
Beukers' theorem would then make their values linearly independent,
contradicting $({\rm H})$.

The 2026 interpolation theorem can in fact supply the regular-system
part. Apply it separately to $e$ and, conditionally under
$({\rm H})$, to $\pi$. The two resulting minimal homogeneous
equations are regular at $1$. Their companion systems, together with
the equation $1'=0$, have a direct sum that is a common first-order
system regular at $1$.

What interpolation does **not** supply is independence of all
components of this joint first-order system. Indeed, under
$({\rm H})$, the value relation


$$
-s\cdot1+F(1)+G(1)=0
$$


and Beukers' theorem force a degree-one functional relation over
$\overline{\mathbb Q}(z)$ among the components of the direct-sum
system. Those components include $1,F,G$ and, in general,
derivatives needed to close the two equations. The lifted relation can
involve those derivative components, even though its specialization at
$1$ involves only $1,F(1),G(1)$. Therefore Beukers' lifting theorem
alone does **not** imply that $1,F,G$ themselves are functionally
linearly dependent. The exact conclusion is:

> **Conditional regular-interpolation no-go.** Under $({\rm H})$,
> for every pair of exact $E$-interpolants for $e,\pi$ whose
> minimal homogeneous equations are regular at the evaluation point,
> the components of the associated common direct-sum first-order
> system are functionally linearly dependent.

For the obvious interpolants $e^z,\ s-e^z$, the lifted relation is
already the constant-coefficient identity


$$
e^z+(s-e^z)-s=0.                                    \tag{8.1}
$$


Thus their value relation is precisely in Beukers' lifted/zero branch,
not in conflict with the theorem.

Accordingly, the genuinely missing input is not a specialization
theorem or regular interpolation, but one of:

* an exact pair of regular interpolants for which a closed common
  first-order vector containing $1,F,G$ can be proved componentwise
  linearly independent over $\overline{\mathbb Q}(z)$; or
* an independent theorem excluding the functional relation that
  Beukers would lift.

The forced Borel collision of Theorem 4.1 shows an additional,
system-independent obstruction before one even reaches this route.

No analogous archimedean specialization theorem for a vector
consisting of an $E$-function and a $G$-function at $z=1$ was
found in the audited primary sources.

### 8.1 Current algebraic-independence measures keep an exact zero branch

The 2025 preprint of B. Adamczewski and C. Faverjon,
*Algebraic independence measures for values of $E$-functions and
$M$-functions*,
[arXiv:2502.09999](https://arxiv.org/abs/2502.09999), proves a
Liouville-type alternative for arbitrary Siegel $E$-functions. In
its system-free $E$-case, let
$f_1,\ldots,f_r$ be $E$-functions and let
$\alpha\ne0$ be algebraic. Put


$$
\tau=\operatorname {trdeg}_{\overline{\mathbb Q}(z)}
\overline{\mathbb Q}(z)
\bigl(f_i^{(\ell)}:1\le i\le r,\ \ell\ge0\bigr).
$$


There are positive constants $C_1,C_2$ (with the dependencies
specified in the paper) such that, for every integer polynomial $P$,
either


$$
P(f_1(\alpha),\ldots,f_r(\alpha))=0,                 \tag{8.2}
$$


or


$$
|P(f_1(\alpha),\ldots,f_r(\alpha))|
\ge C_1 H(P)^{-C_2\deg(P)^\tau}.                    \tag{8.3}
$$


Their system theorem has the analogous alternative with the
functional transcendence degree of the system components.

This result is deliberately formulated so that it does not claim
nonvanishing. Under $({\rm H})$, use


$$
f_1(z)=e^z,\qquad f_2(z)=s-e^z,\qquad\alpha=1.
$$


If $m_s\in\mathbb Z[X]$ is a nonzero integer multiple of the minimal
polynomial of $s$, then


$$
P(X,Y)=m_s(X+Y)
$$


is a nonzero integer polynomial and


$$
P(f_1(1),f_2(1))=m_s(e+\pi)=m_s(s)=0.                \tag{8.4}
$$


Thus the hypothetical relation lands exactly in branch (8.2);
the lower bound (8.3) never activates. The stronger conclusion that no
transcendental $E$-value is a Liouville number is likewise
compatible with $({\rm H})$.

## 9. Recent functional $E/G$ independence does not fill the value gap

Recent work of D. Vargas--Montoya proves algebraic independence for
certain collections mixing $E$- and $G$-functions. The hypotheses
and conclusion are $p$-adic and functional:

* one fixes a finite totally ramified extension $K/\mathbb Q_p$;
* the functions belong to a class satisfying a
  maximal-order-multiplicity condition and a strong Frobenius
  structure;
* algebraic independence is over the field $E_p$ of $p$-adic
  analytic elements, with a criterion involving products and
  logarithmic derivatives.

The concrete examples mix $J_0(\pi_3z)$, with
$\pi_3^2=-3$ a Dwork $3$-adic element, and Apéry-type
$G$-functions. These are rigorous functional results. They do not:

1. specialize at a complex algebraic point to a theorem about complex
   values;
2. identify the ordinary complex constant $\pi$ with the Dwork
   $p$-adic element $\pi_p$;
3. provide the exact values $e$ and $\pi$ in one admissible
   family; or
4. yield an archimedean relation-lifting theorem for mixed $E/G$
   values.

Thus these results cannot be transferred to (7.1) without a new
specialization principle.

Primary sources audited:

* D. Vargas--Montoya, *On the algebraic independence of
  $E$-functions and $G$-functions, I*,
  [arXiv:2502.00768](https://arxiv.org/abs/2502.00768).
* D. Vargas--Montoya, *On the algebraic independence of
  $E$-functions and $G$-functions, II*,
  [arXiv:2507.20429](https://arxiv.org/abs/2507.20429).

Functional algebraic independence by itself never implies algebraic
independence at a specified value point unless a valid specialization
theorem and all of its regularity hypotheses are supplied.

### 9.1 The August 2026 $E$-period construction

The current version of B. Snodgrass, *Periods of $E$-operators*,
[arXiv:2608.06005v2](https://arxiv.org/abs/2608.06005), was also
audited because it postdates the logarithm and interpolation papers.
Its principal theorem gives a cyclotomic rational structure on rapid
decay cohomology for pullbacks of suitable connections of exponential
type. This permits the definition of $E$-periods as matrix entries of
the de Rham/rapid-decay comparison isomorphism, and realizes certain
absolutely convergent integrals involving $E$-functions in that
framework.

This is a structural period-realization theorem. It supplies no
injectivity statement for a formal period algebra, no criterion that a
specified matrix coefficient is nonzero, and no algebraic-independence
or transcendence theorem for those coefficients. The paper itself
places transcendence of periods in the context of period conjectures.
Moreover, both exponential periods and $E$-values lie in the larger
$E$-period setting described there. Hence placing $e$, $\pi$, or
their integral representations in a common $E$-period algebra is
fully compatible with the hypothetical algebraic relation
$e+\pi=s$; an injectivity or period-conjecture input would still be
needed. The construction therefore does not change the forced-support
or value-ring reductions above.

## 10. Why direct exponentiation is outside the $E$-class

One may try to turn $s=e+\pi$ into relations involving
$e^e$, $e^\pi$, or logarithms of $E$-values. The natural
functional candidates already leave the class. For example,


$$
\exp(e^z+z-1)
$$


takes the value $e^e$ at $z=1$, while under $({\rm H})$


$$
\exp((s-1)z-e^z+1)
$$


takes the value $e^\pi$ at $z=1$. Their Taylor coefficients are
algebraic under the stated hypotheses, but neither function is an
$E$-function.

Every $E$-function has exponential type, hence entire order at most
$1$. If $h$ is a transcendental entire function, then $e^h$ has
infinite order. Indeed, if $e^h$ had finite order, then
$\Re h(z)=\log|e^{h(z)}|$ would have a polynomial growth bound
outside a fixed disk. Borel--Carathéodory would give a polynomial
growth bound for $h$, forcing $h$ to be a polynomial. If $h$ is
a polynomial of degree $d$, then $e^h$ has order $d$. In the
examples above the exponent contains $e^z$ and is transcendental
entire, so the exponentials have infinite order.

The value ring $\mathbf E$ is a ring, but it is not asserted to be
closed under arbitrary exponentiation or division. Even a separate
construction representing $e^e$ and $e^\pi$ as $E$-values
would not suffice: Fischler--Rivoal's theorem controls individual
logarithms and exceptional points, not an algebraic sum of two
logarithms.

## 11. Current theorem-by-theorem decision table

| Candidate theorem | Exact useful conclusion | Hypothesis forced to fail or missing under $({\rm H})$ |
|---|---|---|
| Delaygue, Theorem 2.1 | Linear independence of $1$ and transcendental $E$-values with disjoint Borel supports | Exact representations of $e,\pi$ force a scaled-support collision by Theorem 4.1 |
| Fischler--Rivoal 2026, Theorem 1 / Corollary 1 / Proposition 1 | Finiteness and classification of algebraic logarithmic exceptions | Every exact value $F(x)=e^\eta$ forces $x/\eta\in\mathfrak S(F)$, exactly the exceptional branch |
| Fischler--Rivoal quantitative Theorem 2 | One-logarithm rational approximation lower bound | Assumes nonrationality and does not prohibit algebraic relations among two logarithms |
| Beukers refinement | Functional relations and value relations coincide at a regular algebraic specialization | Interpolation supplies a common regular direct-sum system, but under $({\rm H})$ Beukers forces dependence among all of its components; the missing input is an independent proof that a closed common vector is componentwise independent |
| Fischler--Rivoal interpolation | Exact $E$-value interpolation with regular minimal equations | Differential regularity does not imply Borel-support separation; (4.5) proves the distinction conditionally |
| Adamczewski--Faverjon value measures | Effective lower bound for a polynomial in arbitrary $E$-values, unless it is exactly zero | Under $({\rm H})$, $m_s(e+\pi)=0$ is precisely the allowed zero branch |
| $G$-value as directional $E$-limit | Represents $\pi$ by an $E$-function at infinity | Available $E$-value specialization theorems are for finite algebraic points |
| Functional $\mathcal E\cap\mathcal G=\overline{\mathbb Q}[z]$ | Separates the function classes | Does not imply the value-ring statement $\mathbf E\cap\mathbf G=\overline{\mathbb Q}$ |
| Vargas--Montoya mixed $E/G$ independence | $p$-adic functional algebraic independence for strong-Frobenius/MOM families | No complex-value specialization and no admissible exact $e,\pi$ family |
| Snodgrass $E$-periods (2026) | Cyclotomic rational structures and period realizations for rapid-decay pairings | No injectivity, nonvanishing, or algebraic-independence theorem for the matrix coefficients |

## 12. Sharp surviving reductions

### 12.1 A Delaygue target

Find $E$-functions $F,G$ and nonzero algebraic $x,y$ with


$$
F(x)=e,\qquad G(y)=\pi,
$$


and prove


$$
\mathfrak S(F)/x\ \cap\ \mathfrak S(G)/y=\varnothing.
$$


Delaygue would immediately disprove $({\rm H})$. Theorem 4.1 shows
that this is not a flexible representation problem: under
$({\rm H})$, such separation is impossible. Proving it for any exact
pair would itself be the decisive new arithmetic input.

### 12.2 A value-ring target

It is enough to prove any one of


$$
\mathbf E\cap\mathbf G=\overline{\mathbb Q},\qquad
e\notin\mathbf G,\qquad
\pi\notin\mathbf E.
$$


Each contradicts (7.1). None is supplied by the audited functional
intersection results.

### 12.3 A Beukers target

Construct exact regular $E$-interpolants for $e,\pi$, embed them
with $1$ in a closed common first-order vector, and prove all
components of that vector linearly independent over
$\overline{\mathbb Q}(z)$. The 2026 interpolation theorem can supply
the regularity and a direct-sum common system; Beukers then specializes
the componentwise independence. Interpolation alone does not give that
decisive independence and, conditionally under $({\rm H})$, Beukers
forces a functional relation somewhere among the direct-sum
components.

### 12.4 A multi-logarithm target

Construct appropriate $E$-values whose logarithms are $e$ and
$\pi$, and prove a theorem excluding a nonzero algebraic linear
combination of those logarithms. Existing logarithm results prove
transcendence or measures for one logarithm and explicitly admit the
forced exceptional branch; they do not supply this joint theorem.

These are reductions, not proved routes to the final problem.

## 13. Primary-source provenance and exact local hashes

Primary artifacts were downloaded and inspected on 2026-08-27. The
hashes below identify the exact local source or PDF used for this
audit.

| Source artifact | URL | SHA-256 |
|---|---|---|
| Fischler--Rivoal, *Transcendence of values of logarithms of $E$-functions*, final PDF | [DOI](https://doi.org/10.1007/s00208-026-03374-z) | `86669c0103d2a589c9a45970734a9ebac47c737382c015fa026b546960c0301d` |
| Delaygue, *A Lindemann--Weierstrass theorem for $E$-functions*, arXiv source v2 | [arXiv:2210.12046](https://arxiv.org/abs/2210.12046) | `900362b1c9a2682cf3362504061e5524fbe5d390a8836e633e42772b67a9eeb4` |
| Fischler--Rivoal, *On the singularities of differential equations satisfied by $E$-functions*, arXiv source v1 | [arXiv:2604.20332](https://arxiv.org/abs/2604.20332) | `d338d11051d85dad237b0b3aa17953c140fe5e19015c970516620a92bb96ccf2` |
| Fischler--Rivoal, arithmetic-Gevrey relations, arXiv source | [arXiv:2301.13518](https://arxiv.org/abs/2301.13518) | `304cd713f3488b89768a3bca26858b6197725133ba05d51c7ec19cb48bd67d1b` |
| Beukers, refined Siegel--Shidlovskii theorem, arXiv source | [arXiv:math/0405549](https://arxiv.org/abs/math/0405549) | `3023c4190ccb9b1640b668d0d7ca975cd4d1551e7ba70531bfde1efa97642ad2` |
| Fischler--Rivoal, zeros of $E$-functions, arXiv source v1 | [arXiv:2503.20345](https://arxiv.org/abs/2503.20345) | `5a134dfc6dd21f129fb921dde3b3789063998862bb738970952f45195c1fd505` |
| Adamczewski--Faverjon, algebraic-independence measures for $E/M$-values, arXiv source v1 | [arXiv:2502.09999](https://arxiv.org/abs/2502.09999) | `7f30da6c5903fbff27197140aa3dd8b71b39178fcd616ff8ea627e62318a1c44` |
| Vargas--Montoya I, arXiv source v2 | [arXiv:2502.00768](https://arxiv.org/abs/2502.00768) | `68ea90e94209119b5a85300c1d10381b51a5c6d6f3eeb9cbd0dd7ae1cc24d813` |
| Vargas--Montoya II, arXiv source v1 | [arXiv:2507.20429](https://arxiv.org/abs/2507.20429) | `189a1264a62a026a473987df78303c1bc7fde5177b1a3cccb69628791d1199b5` |
| Snodgrass, *Periods of $E$-operators*, arXiv source v2 | [arXiv:2608.06005](https://arxiv.org/abs/2608.06005) | `65b4c87421674293c6bc8984eecb52894dddc76f0d1ced70dcad8056daa6e3b5` |

The 2025 Fischler--Rivoal zero paper was checked because its title and
scope might suggest a route through common zeros. Its unconditional
results concern special quotient/zero configurations; the broad
statements connecting zeros with $\pi$, logarithms, or
exponential-polynomial configurations are conditional on Schanuel-type
or explicit $E$-function conjectures. They therefore do not alter
the verdict above.

The arXiv current-results query was also checked through 2026-08-27.
No later theorem in the queried $E/G$-function and logarithm-value
literature supplied an archimedean mixed-value specialization or the
intersection theorem (7.2). This bibliographic observation is not used
as a mathematical premise: every no-go statement above is tied to the
exact hypotheses of the cited theorem.

## 14. Final audit conclusion

The strongest exact conclusion is not merely that current theorems
“seem inapplicable.” It is this dichotomy:



$$
\boxed{
\begin{array}{c}
e+\pi\in\overline{\mathbb Q}
\\[2mm]\Longrightarrow\\[2mm]
\text{every exact \(E/E\) representation of \(e,\pi\)
has the Borel-support collision}\\
\text{that prevents Delaygue's linear-independence conclusion,}
\\[1mm]
\text{and every exact \(E\)-representation of an algebraic
exponential lies in}\\
\text{the exceptional branch of Fischler--Rivoal's logarithm theorem.}
\end{array}}
$$



On the mixed $E/G$ side, $({\rm H})$ is exactly a source of
transcendental elements in $\mathbf E\cap\mathbf G$. Excluding those
elements requires a value-ring theorem, not the available functional
intersection or $p$-adic functional-independence theorems.

Accordingly, no audited existing theorem contradicts $({\rm H})$
after all hypotheses are checked. The sharp missing inputs are Borel
support separation for an exact pair, a complex mixed-value
specialization theorem, the $E/G$ value-ring intersection
conjecture, or a genuinely joint algebraic-independence theorem for
logarithms of $E$-values.
