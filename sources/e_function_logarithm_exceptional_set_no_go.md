> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# E-function logarithms under the hypothesis $e+\pi\in\overline{\mathbb Q}$

## A primary-source audit and a forced-exception theorem

Date of audit: 2026-08-26.

This note uses only primary papers.  Its purpose is deliberately narrow: test the
new Fischler--Rivoal theorem on logarithms of values of $E$-functions, together
with its 2025--2026 follow-ups, against the hypothetical relation



$$
\alpha:=e+\pi\in\overline{\mathbb Q}.                                      \tag{1}
$$



The audit does **not** prove or disprove (1).  It does prove a useful no-go result:
every exact $E$-function interpolation of $e^\eta$, with both the evaluation
point and $\eta$ algebraic and nonzero, has a forced singularity in the
associated Borel/G-series.  Consequently the interpolation point is necessarily
one of the exceptional points in the logarithm theorem.  In particular, adding an
arbitrary vanishing $E$-function perturbation to an exponential cannot make the
Fischler--Rivoal theorem contradict (1).

All statements below are unconditional unless a paragraph explicitly begins by
assuming (1).

## 1. Three different notions that must not be conflated

If



$$
F(z)=\sum_{n\geq 0}a_n\frac{z^n}{n!}
$$



is an $E$-function, put



$$
\psi(F)(t)=\sum_{n\geq0}a_nt^n,
 \qquad
 \mathfrak S(F)=\{\text{finite singularities of the analytic continuation of
 }\psi(F)\}.                                                               \tag{2}
$$



Thus $\mathfrak S(F)$ is a finite subset of
$\overline{\mathbb Q}^{\,*}$.  For $\gamma\in\overline{\mathbb Q}^{\,*}$,



$$
\psi(e^{\gamma z})(t)=\frac1{1-\gamma t},
 \qquad
 \mathfrak S(e^{\gamma z})=\{\gamma^{-1}\}.                                \tag{3}
$$



There are three distinct objects in the papers under review:

1. the Borel-plane singularities $\mathfrak S(F)$ in (2);
2. singularities, in the original $z$-plane, of a minimal homogeneous or
   inhomogeneous differential equation satisfied by $F$;
3. algebraic evaluation points $\xi$ for which some determination of
   $\log F(\xi)$ is algebraic.

The 2026 interpolation theorem controls item 2.  The 2024/2026 logarithm theorem
is controlled by item 1 and characterizes item 3.  Regularity in item 2 does not
imply anything like the absence of a point from item 1.

## 2. Exact primary theorems used

### 2.1 Delaygue's Lindemann--Weierstrass theorem

In [Delaygue, *A Lindemann--Weierstrass theorem for $E$-functions*, Theorem
2.1 and Corollary 2.2](https://arxiv.org/abs/2210.12046), the relevant statements
are as follows.

* If $F_1,\ldots,F_m$ are $E$-functions whose sets
  $\mathfrak S(F_j)$ are pairwise disjoint, $x$ is algebraic, and every
  $F_j(x)$ is transcendental, then
  $1,F_1(x),\ldots,F_m(x)$ are linearly independent over
  $\overline{\mathbb Q}$.
* In the different-point form, if $F_1,F_2$ are $E$-functions,
  $x_1,x_2\in\overline{\mathbb Q}^{\,*}$, and
  $F_1(x_1)=F_2(x_2)$ is transcendental, then

  

$$
\frac{x_1}{x_2}=\frac{\rho_1}{\rho_2}
   \quad\text{for some}\quad
   \rho_j\in\mathfrak S(F_j).                                               \tag{4}
$$



Delaygue states the paper for strict $E$-functions.  Fischler--Rivoal explain
in Remark 1 following their Proposition 1 that (4), and the general theorem used
to prove it, remain valid for Siegel $E$-functions.  They list the four inputs
needed for that extension: Fuchsian behavior of G-functions at infinity; a
G-function with no finite singularity is a polynomial; annihilation of an
$E$-function by an $E$-operator without nonzero finite singularities; and
Beukers' refined Siegel--Shidlovskii theorem.

### 2.2 Fischler--Rivoal's logarithm theorem

The current primary version is Fischler--Rivoal,
[*Transcendence of values of logarithms of E-functions*](https://www.imo.universite-paris-saclay.fr/~stephane.fischler/logE.pdf),
Math. Ann. 394 (2026), article 12, revised 2025-11-11 and published online
2026-02-08.  Its relevant exact hypotheses and conclusions are:

* **Theorem 1.**  Let $F,G$ be transcendental Siegel $E$-functions.  If
  $F(z)\ne G(\beta z)$ for every
  $\beta\in\overline{\mathbb Q}$, then

  

$$
\{(x,y)\in\overline{\mathbb Q}^{\,2}:F(x)=G(y)\}
$$



  is finite.
* **Corollary 1.**  If $F$ is an $E$-function not of the form
  $e^{\beta z}$, $\beta\in\overline{\mathbb Q}$, then, for any fixed
  determination of the logarithm, $\log F(x)$ is transcendental for every
  algebraic $x$ outside a finite exceptional set.
* **Proposition 1.**  The ratio assertion (4) holds for Siegel
  $E$-functions.
* **Exact exceptional-point characterization.**  Given
  $x\in\overline{\mathbb Q}$, there exists an algebraic determination of
  $\log F(x)$ if and only if either $F(x)=1$, or

  

$$
F(x)=\exp(x/\rho)
   \quad\text{for some}\quad \rho\in\mathfrak S(F).                         \tag{5}
$$



Equivalently, if



$$
\operatorname{Exc}_{\log}(F)
 =\{x\in\overline{\mathbb Q}:\exists\eta\in\overline{\mathbb Q},
        e^\eta=F(x)\},
$$



then, when $F$ is not a pure exponential in the paper's excluded sense
$F(z)=e^{\beta z}$ with $\beta\in\overline{\mathbb Q}$,



$$
\operatorname{Exc}_{\log}(F)
 =\{x\in\overline{\mathbb Q}:F(x)=1\}
  \cup\bigcup_{\rho\in\mathfrak S(F)}
       \{x\in\overline{\mathbb Q}:F(x)=e^{x/\rho}\}.                        \tag{6}
$$



This set is finite.  Formula (6), not merely the existence of an unspecified
finite set, is decisive for the present question.

The paper also proves a quantitative theorem.  Its hypotheses are substantially
stronger: $F\in\mathbb Q[[z]]$ must be a **strict** $E$-function,
$x\in\mathbb Q^*$, $F(x)>0$, and $\ln F(x)\notin\mathbb Q$.  It then gives
effective $c,d>0$ such that



$$
\left|\ln F(x)-\frac ab\right|\geq \exp(-cb^d)
 \qquad(a\in\mathbb Z, b\geq1).                                           \tag{7}
$$



Theorem (7) does not decide whether a prescribed point is exceptional and does
not give algebraic independence between two logarithms.

## 3. The forced Borel-singularity theorem

### Proposition 1 (exact algebraic logarithms force their own singularity)

Let $F$ be a Siegel $E$-function and let
$x,\eta\in\overline{\mathbb Q}^{\,*}$.  If



$$
F(x)=e^\eta,                                                               \tag{8}
$$



then



$$
\boxed{\frac{x}{\eta}\in\mathfrak S(F).}                                 \tag{9}
$$



#### Proof

Hermite--Lindemann implies that $e^\eta$ is transcendental because
$\eta\ne0$ is algebraic.  Apply Fischler--Rivoal Proposition 1 to $F$ at
$x$ and $e^z$ at $\eta$.  By (3),
$\mathfrak S(e^z)=\{1\}$.  Equation (4) therefore gives



$$
\frac{x}{\eta}=\frac\rho1
 \quad\text{for some }\rho\in\mathfrak S(F),
$$



which is (9). $\square$

When $F$ is not a pure exponential, (5) now says that $x$ is necessarily an
exceptional evaluation point.  If $\eta=0$, then $F(x)=1$, which is the
other exceptional case in (5).  Thus **every** exact algebraic logarithm lies in
the exceptional set, with (9) specifying the responsible Borel singularity when
the logarithm is nonzero.

### Proposition 2 (rigidity of an algebraic scalar)

Let $c\in\overline{\mathbb Q}^{\,*}$ and
$\beta,x,\eta\in\overline{\mathbb Q}$.  If



$$
c e^{\beta x}=e^\eta,                                                       \tag{10}
$$



then $c=1$ and $\eta=\beta x$.

#### Proof

Equation (10) gives



$$
c=e^{\eta-\beta x}.
$$



If the algebraic number $\eta-\beta x$ were nonzero, Hermite--Lindemann
would make the right-hand side transcendental, contrary to
$c\in\overline{\mathbb Q}$.  Hence $\eta=\beta x$ and $c=1$. $\square$

This elementary lemma completely separates the plus and minus perturbations
below.

## 4. The perturbed-exponential no-go

Let $x,\beta\in\overline{\mathbb Q}^{\,*}$ and let $H$ be any
$E$-function.  Consider



$$
F_+(z)=e^{\beta z}+(z-x)H(z).                                               \tag{11}
$$



Then $F_+$ is an $E$-function and



$$
F_+(x)=e^{\beta x}.                                                         \tag{12}
$$



If $H\ne0$, $F_+$ is not a pure exponential.  Indeed, if
$F_+=e^{\gamma z}$ for an algebraic $\gamma$, evaluation at $x$ gives
$e^{(\gamma-\beta)x}=1$.  Hermite--Lindemann forces $\gamma=\beta$, and
then $(z-x)H(z)\equiv0$, a contradiction.

Apply Proposition 1 with $\eta=\beta x$.  It yields



$$
\boxed{\beta^{-1}\in\mathfrak S(F_+).}                                    \tag{13}
$$



Consequently $x\in\operatorname{Exc}_{\log}(F_+)$, because



$$
F_+(x)=\exp\!\left(\frac{x}{\beta^{-1}}\right).                            \tag{14}
$$



This remains true with $(z-x)H(z)$ replaced by **any** $E$-function
perturbation that vanishes at $x$, and it remains true for any higher-order
factor $(z-x)^mH(z)$.  The argument depends only on the exact value (12).

There is also a useful coefficient-level check.  Write



$$
H(z)=\sum_{n\geq0}b_n\frac{z^n}{n!},
 \qquad B(t)=\psi(H)(t)=\sum_{n\geq0}b_nt^n.
$$



Then



$$
\psi(F_+)(t)
  =\frac1{1-\beta t}+t^2B'(t)+(t-x)B(t).                                    \tag{15}
$$



One might hope to choose $B$ so that the remaining terms cancel the pole at
$t=\beta^{-1}$.  Equation (13) proves that complete cancellation is
impossible whenever (11) is a non-exponential $E$-function.  This is an
arithmetic obstruction, not a failure of a particular ansatz for $H$.

Now consider the apparent sign variant



$$
F_-(z)=-e^{\beta z}+(z-x)H(z),
 \qquad F_-(x)=-e^{\beta x}.                                                 \tag{16}
$$



There is **no** algebraic logarithm of $-e^{\beta x}$: equation
$e^\eta=-e^{\beta x}$ with algebraic $\eta$ would contradict Proposition
2 with $c=-1$.  Equivalently, all logarithms are
$\beta x+(2k+1)\pi i$, and all are transcendental.  Thus the minus sign is not
a second exceptional algebraic-log construction.  It simply produces a
transcendental logarithm, fully consistent with Fischler--Rivoal Corollary 1.
More generally, no nontrivial algebraic scalar multiple of $e^{\beta x}$ can
have an algebraic logarithm.  The only scalar relevant to an algebraic-log
contradiction is $c=1$, already covered by (11)--(14).

## 5. Consequences under $\alpha=e+\pi\in\overline{\mathbb Q}$

Assume (1).  Since $\alpha>0$, it is nonzero.  The most direct attempted
application is



$$
F_\alpha(z)=e^z+(z-\alpha)H(z),
 \qquad F_\alpha(\alpha)=e^\alpha.                                          \tag{17}
$$



For nonzero $H$, this is a non-exponential $E$-function defined over a
number field containing $\alpha$.  Its principal logarithm at $\alpha$ is
the algebraic number $\alpha$.  Formula (13) gives



$$
1\in\mathfrak S(F_\alpha),                                                  \tag{18}
$$



and (14) puts $\alpha$ in the exceptional set.  Hence no choice of $H$ can
both preserve (17) and prove nonexceptionality by removing the singularity at
1.  More generally, if $\beta x=\alpha$, then every exact interpolant has the
forced singularity $\beta^{-1}=x/\alpha$.

There is a second elementary obstruction to using ordinary value theorems.
Under (1), both $e$ and $\pi$ are values of $E$-functions at the algebraic
point 1:



$$
e=e^1,
 \qquad
 \pi=(\alpha-e^z)\big|_{z=1}.                                                \tag{19}
$$



But the associated functions satisfy the identity



$$
e^z+(\alpha-e^z)-\alpha\equiv0.                                             \tag{20}
$$



Thus the hypothesized value relation is already a functional relation over
$\overline{\mathbb Q}(z)$.  Siegel--Shidlovskii lifting and modern
algebraic-independence measures are designed to preserve precisely such
functional relations; (20) therefore gives them no contradiction.

To encode $e$ itself as a logarithm one would need an $E$-value equal to
$e^e$; to encode $\pi$ one would need an $E$-value equal to $e^\pi$.
No primary theorem reviewed here supplies either membership.  The hypothesis
(1) gives



$$
e^\alpha=e^e e^\pi,                                                         \tag{21}
$$



and $e^\alpha$ is an $E$-value because $\alpha$ is algebraic, but the
known $E$-value set is used here only as a **ring**.  The cited theorems do not
give closure under exponentiating an $E$-value or under taking arbitrary
quotients, so (21) does not put either factor in that ring.

Even a future construction representing $e^e$ or $e^\pi$ as an
$E$-value would need an additional theorem on algebraic relations between
several logarithms.  Corollary 1 proves individual transcendence; the
transcendence of both $e$ and $\pi$ is already known and is compatible with
their sum being algebraic.  The familiar representation
$\log(-1)=(2k+1)\pi i$, using the constant $E$-function $-1$, likewise
only recovers the known transcendence of $\pi$.

### 5.1 The direct exponentiation constructions are not $E$-functions

There are natural entire functions with algebraic Taylor coefficients that do
take the desired exponential values.  For example,



$$
U_e(z)=\exp(e^z+z-1)
 \quad\Longrightarrow\quad
 U_e(0)=1,\qquad U_e(1)=e^e.                                                  \tag{21a}
$$



Under (1), a corresponding construction for $e^\pi$ is



$$
U_\pi(z)=\exp((\alpha-1)z-e^z+1)
 \quad\Longrightarrow\quad
 U_\pi(0)=1,\qquad U_\pi(1)=e^{\alpha-e}=e^\pi.                              \tag{21b}
$$



The Taylor coefficients of $U_e$ are rational and those of $U_\pi$ lie in
$\mathbb Q(\alpha)$, so coefficient algebraicity alone is not the obstacle.
Neither function is an $E$-function.  Here is a short rigorous growth proof.

Every Siegel $E$-function has finite entire order at most 1: from
$|a_n|\leq n!^\varepsilon$ eventually, for every $\varepsilon>0$, applied
to the coefficients $a_n/n!$, the coefficient formula for entire order gives
order at most $1/(1-\varepsilon)$, hence at most 1.

On the other hand, if $Q$ is a transcendental entire function, then
$e^Q$ has infinite order.  Indeed, finite order of $e^Q$ would give a
polynomial bound for



$$
\max_{|z|=r}\Re Q(z)=\log M_{e^Q}(r).
$$



Borel--Carathéodory on concentric disks would then give a polynomial bound for
$M_Q(r)$, forcing $Q$ to be a polynomial.  Both inner functions in
(21a)--(21b) are transcendental because of the nonzero $e^z$ term, so both
outer exponentials have infinite order.

This also blocks the general recipe “interpolate $e$ or $\pi$ by an
$E$-function and exponentiate that function.”  A related tempting formula is
$e^\pi=(-1)^{-i}$ (with the principal branch).  The function
$(1-z)^{-i}$ realizes this value at $z=2$ after analytic continuation, but
it is a multivalued holonomic function with a branch singularity at $z=1$,
not an entire $E$-function.  Its formal inverse-Borel series is
$\sum_{n\geq0}(i)_n z^n/(n!)^2$; this transformation is not
evaluation-preserving, and the reviewed $E$-function criteria do not certify
the nonrational parameter $i$.  It therefore supplies no $E$-value
representation of $e^\pi$.  Thus the two most immediate constructions of
$e^e$ and
$e^\pi$ fail for precise, independently checkable reasons.

## 6. The 2026 interpolation follow-up and why it does not evade the barrier

Fischler--Rivoal,
[*On the singularities of differential equations satisfied by E-functions*,
Theorems 3 and 4](https://arxiv.org/abs/2604.20332), prove the following.

Let



$$
\mathbf E=\{F(a):F\text{ is a Siegel }E\text{-function},\ a\in\overline{\mathbb Q}\}.
$$



This is a ring.  For every $\zeta\in\mathbf E$, there is an $E$-function
$F$ with $F(1)=\zeta$ such that 1 is not a singularity of either the
minimal homogeneous or the minimal inhomogeneous differential equation of
$F$.  More generally, their Theorem 4 interpolates $T$ prescribed jets at
each of finitely many pairwise distinct nonzero algebraic points.  The minimal
homogeneous order $\mu$ is at least $T+1$; an interpolation point is singular
for that equation exactly when its prescribed jet values are linearly dependent
over $\overline{\mathbb Q}$.  For the minimal inhomogeneous equation, of order
$\mu-1$, the corresponding criterion includes the number 1 among the values.

Assume (1) and set $\zeta=e^\alpha$.  Then $\zeta\in\mathbf E$, and
Hermite--Lindemann makes $\zeta$ transcendental.  Apply Theorem 4 with
$N=T=1$, interpolation point 1, and prescribed value $\zeta$.  It produces
an $E$-function $F$ such that



$$
F(1)=e^\alpha,\qquad \mu\geq2,                                              \tag{22}
$$



and 1 is regular for both minimal differential equations: the singleton
$\{e^\alpha\}$ is linearly independent, and so is
$\{1,e^\alpha\}$.  Since $\mu\geq2$, $F$ is not a pure exponential.

Nevertheless Proposition 1 above, applied to $F(1)=e^\alpha$, gives



$$
\boxed{\alpha^{-1}\in\mathfrak S(F).}                                     \tag{23}
$$



Thus 1 is an exceptional algebraic evaluation point for the logarithm theorem,
even though 1 is regular for both minimal differential equations.  Equations
(22)--(23) are a concrete conditional consequence of combining the two papers
and a rigorous demonstration that the 2026 interpolation theorem does not close
the exceptional-set loophole.  It controls a different type of singularity.

## 7. Other 2025--2026 primary results screened

### 7.1 Rational approximations to $E$-values

Fischler--Rivoal,
[*Rational approximations to values of E-functions*, Theorem 1](https://arxiv.org/abs/2312.12043),
revised 2025-07-10, states: if $F\in\mathbb Q[[z]]$ is an $E$-function and
$r\in\mathbb Q$, then either $F(r)\in\mathbb Q$, or for every
$\varepsilon>0$,



$$
\left|F(r)-\frac pq\right|\geq c q^{-2-\varepsilon}                         \tag{24}
$$



for some $c=c(F,r,\varepsilon)>0$.  The same paper records the consequence
that if a rational-Taylor-coefficient $E$-function satisfies
$F(1)=e^\gamma$ for algebraic $\gamma$, then $\gamma\in\mathbb Q$.

This gives a complete reason why the quantitative logarithm theorem (7) misses
the conditional value $e^\alpha$:

* if $\alpha\in\mathbb Q$, then $\ln(e^\alpha)=\alpha\in\mathbb Q$,
  contrary to an explicit hypothesis of (7);
* if $\alpha\in\overline{\mathbb Q}\setminus\mathbb Q$, no
  rational-coefficient $E$-function can take the value $e^\alpha$ at 1,
  while (7) does not cover general algebraic coefficient fields.

The estimate (24) itself is a measure for a value once its irrationality is
known; it does not rule out (1).

### 7.2 Algebraic-independence measures

Adamczewski--Faverjon,
[*Algebraic Independence Measures for Values of E-functions and M-functions*,
Theorems 1.1 and 1.2](https://arxiv.org/abs/2502.09999), prove Liouville-type
lower bounds in the form of an alternative:



$$
P(F_1(a),\ldots,F_m(a))=0
 \quad\text{or}\quad
 |P(F_1(a),\ldots,F_m(a))|\geq\text{an explicit-type positive bound}.         \tag{25}
$$



Their hypotheses and exponents are formulated using a linear differential
system or, after removing that restriction, the transcendence degree of the
differential field generated by the functions.  Under (1), the relation in
(20), or the integral polynomial relation obtained by applying the minimal
polynomial of $\alpha$ to $e+\pi$, falls into the zero branch of (25).
There is therefore no nonvanishing conclusion to invoke.

The 2025 paper on a new transcendence measure for $e^\gamma$ at algebraic
$\gamma$,
[Fischler--Rivoal, arXiv:2502.17992](https://arxiv.org/abs/2502.17992),
similarly quantifies the already known nonvanishing of polynomials in
$e^\gamma$.  It contains no theorem relating the decomposition
$\gamma=e+\pi$ to such polynomials.

### 7.3 Zeros and factorization

Fischler--Rivoal,
[*Zeros of E-functions and of exponential polynomials defined over
$\overline{\mathbb Q}$*](https://arxiv.org/abs/2503.20345), contains
unconditional results on certain entire quotients and on $E$-functions all of
whose zeros have the same multiplicity.  Its results specifically involving
$\pi$, logarithms of algebraic numbers, and common-zero factorization for
exponential polynomials assume Schanuel's conjecture.  Its proposed general
zero/factorization theory for arbitrary $E$-functions assumes three stated
conjectures (factorization, uniqueness of irreducible factors sharing a zero,
and a zero/logarithm separation conjecture).  Those conditional statements
cannot be imported into the present unconditional problem.

The August 2026 preprint
[*Periods of E-operators*](https://arxiv.org/abs/2608.06005) develops a period
realization for integrals involving $E$-functions.  It does not state a
Diophantine nonvanishing or algebraic-log theorem capable of deciding the
exceptional point in (17) or (22).

## 8. Precisely what remains open in this route

The following implication is now rigorous:



$$
\begin{array}{c}
 x,\eta\in\overline{\mathbb Q}^{\,*},\quad F(x)=e^\eta,
 \quad F\text{ an }E\text{-function}
 \end{array}
 \quad\Longrightarrow\quad
 \frac{x}{\eta}\in\mathfrak S(F).                                           \tag{26}
$$



Therefore any successful use of the logarithm theorem against (1) would need
substantially different input.  For example, one would need a fixed
$E$-function whose Borel singularities are independently known, together with
a consequence of (1) forcing an exponential value at an incompatible algebraic
point.  Any proof of that incompatibility would itself refute (1).  Constructing
the function by inserting $\alpha$ into its algebraic coefficients merely
makes the forced singularity in (26) follow the construction.

The other apparent route would require two ingredients not supplied by the
reviewed literature: representations of $e^e$ and/or $e^\pi$ as
$E$-values at algebraic points, with usable Borel singularity control, and a
theorem on algebraic relations between their logarithms.  Individual
transcendence of those logarithms would not suffice.

Accordingly, the newest unconditional $E$-function results do not currently
prove that $e+\pi$ is transcendental or algebraic.  Their genuine contribution
to this investigation is the exact forced-exception theorem (26), which closes
the broad class of endpoint-fixing exponential perturbations and explains why
regular interpolation in the 2026 follow-up cannot evade the obstruction.

## 9. Primary-source versions checked

The following downloaded primary artifacts were checked locally.  Hashes are
SHA-256 of the downloaded PDF/source archive, not of extracted text.

| Primary source | Version checked | SHA-256 |
|---|---|---|
| Fischler--Rivoal, logarithms of $E$-functions | final author-hosted Math. Ann. PDF, revised 2025-11-11 | `86669c0103d2a589c9a45970734a9ebac47c737382c015fa026b546960c0301d` |
| Fischler--Rivoal, arXiv:2409.18537 | v1 TeX source | `034843f404a635b3775960b531925e8a6f9bd500c5e06f95bed22b96217f59d6` |
| Delaygue, arXiv:2210.12046 | v2 TeX source, 2025-03-07 | `900362b1c9a2682cf3362504061e5524fbe5d390a8836e633e42772b67a9eeb4` |
| Fischler--Rivoal, arXiv:2604.20332 | v1 TeX source archive | `d338d11051d85dad237b0b3aa17953c140fe5e19015c970516620a92bb96ccf2` |
| Fischler--Rivoal, arXiv:2503.20345 | v1 TeX source | `5a134dfc6dd21f129fb921dde3b3789063998862bb738970952f45195c1fd505` |
| Fischler--Rivoal, arXiv:2312.12043 | v2 TeX source, 2025-07-10 | `1e01c7b9e7c2d801f941d7d93c6cc66decc2d79570b0db62a8e3e8c9654c93c1` |
| Adamczewski--Faverjon, arXiv:2502.09999 | v1 TeX source | `7f30da6c5903fbff27197140aa3dd8b71b39178fcd616ff8ea627e62318a1c44` |
