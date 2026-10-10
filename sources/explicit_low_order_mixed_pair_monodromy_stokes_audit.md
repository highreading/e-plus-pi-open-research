> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The explicit low-order mixed $E/G$ pair:
# monodromy, connection matrices, inverse Borel transform, and Stokes data

Date: 2026-08-27 (UTC)

## 1. Question and verdict

Assume, only in order to test this route, that


$$
({\rm H})\qquad s=e+\pi\in\overline{\mathbb Q}.        \tag{1}
$$


The two explicit realizations under examination are


$$
E(z)=e^z,\qquad A_s(z)=s-4\arctan z,                  \tag{2}
$$


and


$$
L_s(z)=s(1-e^{-z})-2\operatorname {Si}(z),\qquad
\operatorname {Si}(z)=\int_0^z\frac{\sin u}{u}\,du.   \tag{3}
$$


They satisfy


$$
E(1)=e=A_s(1),\qquad
\lim_{x\to+\infty}L_s(x)=e                            \tag{4}
$$


under (1).

Every relevant low-order invariant can be calculated explicitly. The
calculation does **not** produce a contradiction, but it gives a
stronger obstruction than the abstract statement that the
$E$-value/$G$-value intersection is unknown:

> **Explicit rank-three obstruction.** Under (1), the vector
> 

$$
> (1,e^z,s-4\arctan z)^T
>
$$


> solves a rational $3\times3$ system that is ordinary at $z=1$
> and has algebraic initial values at $z=0$. Its two nonconstant
> coordinates are algebraically independent over
> $\overline{\mathbb Q}(z)$, its differential Galois group is the
> solvable product $\mathbb G_m\times\mathbb G_a$, yet the two
> coordinates have the same value at $z=1$.

Consequently, proving a mixed Siegel--Shidlovskii specialization
theorem even for this one elementary solvable system would already
prove that $e+\pi$ is transcendental. Ordinary-point regularity,
algebraic initial data, functional algebraic independence, explicit
monodromy, and solvability of the differential Galois group do not
activate any currently proved mixed-value theorem.

The inverse-Borel route collapses exactly to the same pair:


$$
2\psi(L_s)(t)
=A_s(t)+s\,\frac{t-1}{t+1}.                           \tag{5}
$$


The correction is rational and vanishes at $t=1$. Thus the
inverse-Borel interpolant contains no new special-value information.

Finally, a completely closed $E$-system regular at $1$ exists for
$e^z,L_s$, but $\pi$ appears there only as an asymptotic
connection/Stokes constant at infinity. Beukers' theorem specializes
finite values at algebraic ordinary points; it does not compare such a
finite $E$-connection value with a Stokes constant. The full system
is block diagonal between those two sources of constants, so its
local data contain no off-diagonal coupling that could force the
missing arithmetic comparison.

No proof of the arithmetic nature of $e+\pi$ is claimed.

## 2. The elementary rank-three system

Let


$$
Y_s(z)=
\begin{pmatrix}
1\\ e^z\\ s-4\arctan z
\end{pmatrix}.
$$


Here $e^z$ is a strict $E$-function, while


$$
\arctan z=\sum_{n\ge0}\frac{(-1)^n}{2n+1}z^{2n+1}
$$


is a $G$-function: its coefficients and their common denominators
have exponential growth and it satisfies
$(1+z^2)y'=1$. Thus $A_s$ is a $G$-function whenever $s$ is
algebraic.

Then


$$
Y_s'(z)=M(z)Y_s(z),\qquad
M(z)=
\begin{pmatrix}
0&0&0\\
0&1&0\\
-\dfrac4{1+z^2}&0&0
\end{pmatrix}.                                      \tag{6}
$$


The only finite poles of $M$ are $i$ and $-i$. In particular,
$0$ and $1$ are ordinary points, and under (1)


$$
Y_s(0)=(1,1,s)^T\in\overline{\mathbb Q}^{\,3}.        \tag{7}
$$



A fundamental matrix normalized by $\Phi(0)=I_3$ is


$$
\Phi(z)=
\begin{pmatrix}
1&0&0\\
0&e^z&0\\
-4\arctan z&0&1
\end{pmatrix}.                                      \tag{8}
$$


Indeed, direct differentiation gives $\Phi'=M\Phi$, and


$$
Y_s(z)=\Phi(z)(1,1,s)^T.                             \tag{9}
$$


Along the real segment from $0$ to $1$,


$$
\Phi(1)=
\begin{pmatrix}
1&0&0\\
0&e&0\\
-\pi&0&1
\end{pmatrix},\qquad
Y_s(1)=(1,e,s-\pi)^T.                               \tag{10}
$$


Thus (1) is precisely the statement that the second and third
coordinates of the algebraically normalized solution (9) coincide at
the ordinary algebraic point $1$.

The system matrix is independent of $s$. The parameter occurs only
in the algebraic initial vector (7). Hence no invariant of the
differential module itself can distinguish the special choice
$s=e+\pi$ from any other algebraic initial constant.

## 3. Functional algebraic independence is maximal

It is useful to prove more than linear independence.

**Theorem 3.1.** The functions $e^z$ and $\arctan z$ are
algebraically independent over $\overline{\mathbb Q}(z)$.
Consequently, for every algebraic $s$, $e^z$ and $A_s(z)$ are
algebraically independent over $\overline{\mathbb Q}(z)$.

**Proof.** Use the germ at $0$


$$
\arctan z=\frac1{2i}
\bigl(\log(1+iz)-\log(1-iz)\bigr).                  \tag{11}
$$


Counterclockwise analytic continuation around $z=i$ fixes $e^z$
and sends


$$
\arctan z\longmapsto\arctan z+\pi.                  \tag{12}
$$



Suppose that a nonzero


$$
P(z,X,T)\in\overline{\mathbb Q}(z)[X,T]
$$


satisfies


$$
P(z,e^z,\arctan z)=0.                               \tag{13}
$$


Iterating the loop in (12) gives


$$
P(z,e^z,\arctan z+n\pi)=0\qquad(n\in\mathbb Z).      \tag{14}
$$


At any generic point $z$ in the initial domain, the left side of
(14), viewed as a polynomial in its third argument, has infinitely
many distinct roots. Therefore every coefficient in the $T$-degree
expansion vanishes:


$$
P_j(z,e^z)=0
$$


for every coefficient polynomial $P_j(z,X)$.

It remains only to recall that $e^z$ is transcendental over
$\overline{\mathbb Q}(z)$. An elementary proof suffices: after
clearing denominators, a hypothetical relation would be


$$
\sum_{k=0}^N r_k(z)e^{kz}=0,\qquad r_k\in\overline{\mathbb Q}[z],
$$


with $r_N\ne0$. Divide by $e^{Nz}$ and let $z=x\to+\infty$
on the real axis. A nonzero polynomial $r_N(x)$ cannot equal an
exponentially decaying sum of polynomials, a contradiction. Hence
every $P_j$, and then $P$, is zero. This contradicts the choice of
$P$.

The affine change $T\mapsto s-4T$ preserves algebraic
independence. $\square$

For comparison, the Wronskian of
$1,e^z,\arctan z$ is


$$
W(z)=
-\frac{(z+1)^2e^z}{(1+z^2)^2},                     \tag{15}
$$


which is not identically zero and therefore already proves their
linear independence over $\overline{\mathbb Q}(z)$.

Thus the functional transcendence degree of the two nonconstant
coordinates is $2$. Under (1), their values at $1$ have
transcendence degree $1$, since they are both equal to the
transcendental number $e$. The specialization drop is exactly one.

## 4. Differential Galois group and monodromy

After extending the constant field to $\mathbb C$, the
Picard--Vessiot group of (6) is


$$
G=
\left\{
\begin{pmatrix}
1&0&0\\
0&c&0\\
d&0&1
\end{pmatrix}
:c\in\mathbb C^\times,\ d\in\mathbb C
\right\}
\simeq\mathbb G_m\times\mathbb G_a.                 \tag{16}
$$


The inclusion in the displayed group follows from


$$
e^z\longmapsto c e^z,\qquad
-4\arctan z\longmapsto-4\arctan z+d.
$$


The proof of Theorem 3.1 works verbatim with coefficients in
$\mathbb C(z)$, so neither factor collapses and there is no
algebraic relation coupling the factors; hence the group is the full
product.

The analytic monodromy in the algebraically normalized fundamental
matrix (8) is also explicit. Equation (11) gives


$$
\mathcal M_i=I_3-4\pi E_{31},\qquad
\mathcal M_{-i}=I_3+4\pi E_{31},                     \tag{17}
$$


for counterclockwise loops around $i$ and $-i$, respectively.
The exponential block has trivial topological monodromy. Its
$\mathbb G_m$ factor is an irregular/exponential-torus phenomenon
at infinity; the rank-one equation itself has no nontrivial Stokes
matrix.

One can divide the logarithmic coordinate by $4\pi$ and make the
off-diagonal entries in (17) integral, but this is not an arithmetic
normalization over $\overline{\mathbb Q}$. The transformed
differential equation contains


$$
-\frac1{\pi(1+z^2)}
$$


as a coefficient. Conversely, an algebraic gauge transformation can
only multiply the nonzero $\pi$-entry by algebraic constants; it
cannot remove the period. Thus $\pi$ can be moved between the
comparison matrix and the monodromy basis, but not eliminated while
preserving the algebraic differential structure.

The connection matrix (10) simultaneously displays the two constants
of interest:

* $e$ is the finite connection entry of the exponential block from
  $0$ to $1$;
* $-\pi$ is the finite connection entry of the logarithmic block.

The direct-product differential Galois group proves functional
independence, not algebraic independence of these two connection
entries. A numerical period-map injectivity statement for this
particular direct sum would be needed to make


$$
\operatorname {trdeg}_{\overline{\mathbb Q}}\overline{\mathbb
Q}(e,\pi)=2
$$

. That statement contains the target problem.

## 5. Exact conditional failure of a mixed specialization principle

The previous calculations yield the following precise theorem.

**Theorem 5.1.** If (1) holds, then the rational system (6) has all of
the following properties:

1. it has algebraic coefficients and is ordinary at $z=0,1$;
2. it has an algebraic initial vector $Y_s(0)$;
3. its two nonconstant coordinates consist of one $E$-function and
   one $G$-function;
4. those coordinates are algebraically independent over
   $\overline{\mathbb Q}(z)$;
5. its differential Galois group is the connected solvable group
   $\mathbb G_m\times\mathbb G_a$;
6. nevertheless,
   

$$
E(1)-A_s(1)=0.                                    \tag{18}
$$



Therefore no theorem of the following form can be proved without also
disproving (1):

> Functionally independent $E/G$ components of a rational
> first-order system, with algebraic initial data and an ordinary
> algebraic evaluation point, specialize to algebraically or linearly
> independent values.

Beukers' refined Siegel--Shidlovskii theorem proves such a conclusion
when all components are $E$-functions in an admissible $E$-system.
Here $A_s$ is a nonpolynomial $G$-function with logarithmic branch
points, so that theorem does not apply. Recent $p$-adic mixed
$E/G$ functional-independence theorems do not give an archimedean
value specialization. Theorem 3.1 already supplies the functional
independence those theorems seek; the absent step is precisely the
complex-value specialization.

## 6. The scalar equation is equally blind to the value relation

For completeness, define


$$
\begin{aligned}
a(z)&=-\frac{(z-1)(z^2-3)}{(z+1)(z^2+1)},\\
b(z)&=-\frac{2(z^2+2z-1)}{(z+1)(z^2+1)}.
\end{aligned}
$$


Then


$$
\mathcal L=D^3+a(z)D^2+b(z)D                          \tag{19}
$$


annihilates $1,e^z,\arctan z$. Hence it annihilates


$$
D_s(z)=e^z-s+4\arctan z,                             \tag{20}
$$


and


$$
D_s(1)=0\quad\Longleftrightarrow\quad({\rm H}).       \tag{21}
$$


The operator is independent of $s$ and is ordinary at $z=1$.
A nonzero solution of a regular linear equation may of course vanish
at an ordinary point. Its operator, local exponents, monodromy group,
and differential Galois group do not decide whether this particular
connection coefficient is zero.

Moreover, the companion audit
`sources/e_g_mixed_slope_division_no_go.md` proves that


$$
\frac{s-e^z-4\arctan z}{z-1}\notin\mathcal E+\mathcal G
$$


for every algebraic $s$. Thus even under (1), when the numerator
vanishes at $1$, division by the zero leaves the mixed class. There
is no mixed analogue of the André--Beukers zero-removal theorem
available here.

## 7. A closed regular $E$-system for $L_s$

All functions in


$$
X(z)=
\begin{pmatrix}
1\\ e^z\\ e^{-z}\\ \operatorname {Si}(z)\\ \sin z\\ \cos z
\end{pmatrix}
$$


are $E$-functions, and


$$
X'(z)=N(z)X(z),                                     \tag{22}
$$


where


$$
N(z)=
\begin{pmatrix}
0&0&0&0&0&0\\
0&1&0&0&0&0\\
0&0&-1&0&0&0\\
0&0&0&0&1/z&0\\
0&0&0&0&0&1\\
0&0&0&0&-1&0
\end{pmatrix}.                                      \tag{23}
$$


The coefficient pole at $0$ comes from
$\operatorname {Si}'(z)=\sin z/z$. It is harmless for the displayed
entire solution $X$, although the full chosen system is regular
singular there; the point $1$ is ordinary.
The function (3) is the algebraic linear combination


$$
L_s=sX_1-sX_3-2X_4.                                 \tag{24}
$$



Thus there is no difficulty closing the construction inside an
$E$-system regular at $1$. The difficulty is the location of the
desired value:


$$
e=\lim_{x\to+\infty}L_s(x),                          \tag{25}
$$


not $L_s(\alpha)$ at a finite algebraic ordinary point. Beukers'
specialization theorem has no conclusion at the irregular point
$\infty$.

The changes of variables $z=1/u$ or $z=u/(1-u)$ move infinity to
$u=0$ or $u=1$, but they do not create an $E$-function germ
there. The terms


$$
e^{-1/u},\qquad e^{-u/(1-u)},\qquad
\sin(1/u),\qquad\sin(u/(1-u))
$$


have essential singularities at the new finite point. More invariantly,
$L_s$ is a transcendental entire function: its derivative


$$
s e^{-z}-2\frac{\sin z}{z}
$$


cannot be a polynomial, for example by comparison on the negative real
axis. Hence infinity is an essential singularity of $L_s$, and
composition with any rational function having a pole at the proposed
finite endpoint produces an essential singularity there. A rational
pullback therefore cannot convert (25) into a regular finite-point
$E$-specialization.

One can conditionally interpolate the number $e$ by another
$E$-function at $1$, but $e^z$ already does so. Such
interpolation forgets the asymptotic connection to $L_s$ and adds no
mixed relation.

## 8. Exact inverse-Borel reduction

For an $E$-function


$$
F(z)=\sum_{n\ge0}\frac{a_n}{n!}z^n,
\qquad
\psi(F)(t)=\sum_{n\ge0}a_nt^n.
$$


Directly from the coefficients,


$$
\psi(1-e^{-z})(t)=\frac{t}{1+t},\qquad
\psi(\operatorname {Si})(t)=\arctan t.              \tag{26}
$$


Therefore


$$
B_s(t):=\psi(L_s)(t)
=s\frac{t}{1+t}-2\arctan t.                         \tag{27}
$$


At $t=1$,


$$
B_s(1)=\frac{s-\pi}{2},                              \tag{28}
$$


so under (1), $2B_s(1)=e$.

However,


$$
\begin{aligned}
2B_s(t)-A_s(t)
&=2s\frac{t}{1+t}-s\\
&=s\frac{t-1}{t+1}.                                 \tag{29}
\end{aligned}
$$


This is a rational function with algebraic coefficients, and it
vanishes at $t=1$. Thus the inverse-Borel G-function
$2B_s$ is rationally gauge-equivalent, at the target point, to the
original G-function $A_s$. In particular, its extra Borel origin
does not create a new arithmetic constraint.

Its finite singularities and local data are equally explicit:


$$
\operatorname {Sing}(B_s)=\{-1,i,-i\},               \tag{30}
$$




$$
\operatorname {Res}_{t=-1}B_s=-s,                   \tag{31}
$$


and counterclockwise continuation gives


$$
\Delta_i B_s=-2\pi,\qquad
\Delta_{-i}B_s=2\pi.                                \tag{32}
$$


The pole at $-1$ comes from the algebraic coefficient $s$; the
logarithmic jumps at $\pm i$ are the same period data already
present in $A_s$. Equation (29) makes this identity exact.

The function $B_s$ cannot be appended as a component of an
all-$E$ system: it has a pole and logarithmic branch points, whereas
every $E$-function is entire. Appending it returns to a mixed
$E/G$ system and loses the hypothesis of Beukers' theorem.

## 9. The Laplace identity contains the same equality

For positive real $t$, the inverse-Borel/Laplace relation is


$$
\psi(F)(t)=\frac1t\int_0^\infty
F(x)e^{-x/t}\,dx                                    \tag{33}
$$


whenever the integral converges. At $t=1$,


$$
\int_0^\infty e^{-x}(1-e^{-x})\,dx=\frac12.          \tag{34}
$$


Integration by parts gives


$$
\begin{aligned}
\int_0^\infty e^{-x}\operatorname {Si}(x)\,dx
&=\int_0^\infty e^{-x}\frac{\sin x}{x}\,dx\\
&=\arctan(1)=\frac\pi4.                              \tag{35}
\end{aligned}
$$


For the second equality, differentiate
$\int_0^\infty e^{-x}\sin(ax)/x\,dx$ with respect to $a$;
the derivative is $1/(1+a^2)$, and the value at $a=0$ is zero.

Consequently,


$$
\int_0^\infty e^{-x}L_s(x)\,dx
=\frac{s-\pi}{2}=B_s(1).                            \tag{36}
$$


Under (1), (36) is $e/2$. It is an explicit exponential-period
integral representation of the same conditional equality, not an
independent relation.

## 10. Where $\pi$ occurs in the Stokes/connection data

Diagonalize the trigonometric block by


$$
u_\pm(z)=e^{\pm iz}.
$$


Then


$$
\operatorname {Si}'(z)
=\frac{u_+(z)-u_-(z)}{2iz}.                          \tag{37}
$$


Sectorial primitives of $u_\pm(z)/z$ are exponential-integral
functions. When two integration paths differ by a positive loop around
$0$, their difference is


$$
\oint\frac{e^{\pm iz}}z\,dz
=2\pi i\operatorname {Res}_{z=0}
\frac{e^{\pm iz}}z
=2\pi i.                                            \tag{38}
$$


After multiplication by $1/(2i)$, the corresponding
connection/Stokes jump is a rational multiple of $\pi$. Depending
on the standard lateral-sector convention, signs and allocation
between the $+$ and $-$ columns change, but the nonzero period
class is exactly the $\pi$ already seen in (32) and


$$
\lim_{x\to+\infty}\operatorname {Si}(x)=\frac\pi2.   \tag{39}
$$



This is consistent with Fischler--Rivoal's arithmetic theory of
$E$-operators: finite connection constants are expressed using
$E$-values, while Stokes constants at infinity involve
$G$-values and Gamma values or derivatives. Their theorem classifies
the arithmetic rings in which these constants lie; it does not prove
algebraic independence between a finite connection constant and a
Stokes constant.

The block structure in (23) is decisive:

* the $e^z$ block has the finite connection coefficient $e$;
* the $e^{-z}$ block used in $L_s$ is rank one and has trivial
  Stokes matrices;
* the $(1,\operatorname {Si},\sin,\cos)$ block carries the
  $\pi$-connection/Stokes constant;
* there is no off-diagonal differential coupling between the
  exponential block and the sine-integral block.

The algebraic scalar $s$ in (24) chooses a linear combination across
the blocks but does not change their monodromy or Stokes matrices.
Under (1), the numerical relation


$$
e+\pi=s
$$


is therefore a relation between a finite $E$-connection entry and a
Stokes/$G$-period entry of an explicit block-diagonal $E$-system.
No current comparison theorem separates those two blocks
arithmetically.

## 11. Why the strongest existing theorems stop exactly here

### 11.1 Beukers

Beukers' refined Siegel--Shidlovskii theorem lifts relations among
finite algebraic-point values of components of an $E$-system regular
at that point. It applies to (22) at $1$, but $\pi$ occurs in
(39), not as one of the finite values $X_j(1)$. It does not apply to
the $G$-function $B_s$.

### 11.2 Arithmetic $E$-operator connection and Stokes constants

The arithmetic theory identifies the types of constants appearing in
the two comparison problems. In the present example those constants
are already exactly $e$ and $\pi$. Membership in the respective
rings is not a nonvanishing or independence theorem for their sum.

### 11.3 $G$-values as finite $E$-limits

Fischler--Rivoal prove that finite directional limits of
$E$-functions are precisely $G$-values. Equation (25) is the
lowest-order concrete instance. This theorem proves that the limit is
a $G$-value; it does not say that a transcendental $E$-value
cannot equal that limit. Such a statement would imply the conjectural
intersection
$\mathbf E\cap\mathbf G=\overline{\mathbb Q}$.

### 11.4 Exponential-period comparison

The connection matrix (10) is an explicit two-period comparison
containing an exponential period $e$ and an ordinary period
$\pi$. The exponential period conjecture would separate them; its
injectivity assertion is not proved. Monodromy, Stokes matrices, and
the differential Galois group calculate the formal and functional
symmetries, but do not supply that numerical injectivity.

## 12. Sharp survivor

The weakest theorem exposed by this audit that would settle the target
is the following single-system statement:

> **Explicit mixed connection conjecture.** For
> 

$$
> M(z)=
> \begin{pmatrix}
> 0&0&0\\
> 0&1&0\\
> -4/(1+z^2)&0&0
> \end{pmatrix},
> \quad
> \Phi(0)=I_3,
>
$$


> the two entries
> 

$$
> \Phi_{22}(1)=e,\qquad \Phi_{31}(1)=-\pi
>
$$


> are algebraically independent over $\overline{\mathbb Q}$.

Even the weaker assertion


$$
\Phi_{22}(1)-\Phi_{31}(1)
=e+\pi\notin\overline{\mathbb Q}                     \tag{40}
$$


solves the original problem. Everything on the functional side of
this conjecture is already established explicitly:

* $M$ is rational and regular at the endpoints;
* its fundamental matrix is (8);
* its differential Galois group is
  $\mathbb G_m\times\mathbb G_a$;
* the two functions are algebraically independent;
* the monodromy is (17).

The missing hypothesis is solely an archimedean numerical
specialization/period-injectivity theorem mixing the exponential and
logarithmic blocks.

Equivalently, on the $L_s$ side, one needs a theorem excluding an
algebraic relation between the finite connection value $e^1$ and the
Stokes/limit constant $2\lim_{x\to\infty}\operatorname {Si}(x)$.
Neither a different closure of the system nor the inverse-Borel
transform changes that requirement.

## 13. Replayable exact certificate

The deterministic symbolic certificate is:

* `scripts/explicit_low_order_mixed_pair_certificate.py`;
* `results/explicit_low_order_mixed_pair_certificate.json`.

It verifies:

1. $\Phi'=M\Phi$, $\Phi(0)=I_3$, and (6);
2. the scalar order-three annihilator (19);
3. the closed $E$-system (22)--(24);
4. the inverse-Borel coefficients through degree $30$;
5. the exact rational identity (29);
6. $B_s(1)=(s-\pi)/2$ and
   $\operatorname {Res}_{-1}B_s=-s$;
7. the exact Laplace integrals (34)--(36);
8. the Wronskian (15) and the monodromy jump data.

The replay was byte-identical to the archived JSON.

## 14. Primary sources and provenance

1. F. Beukers, *A refined version of the Siegel--Shidlovskii theorem*,
   Ann. of Math. **163** (2006), 369--379,
   [arXiv:math/0405549](https://arxiv.org/abs/math/0405549).
2. S. Fischler and T. Rivoal, *Arithmetic theory of
   $E$-operators*, J. Éc. polytech. Math. **3** (2016), 31--65,
   [arXiv:1406.5995](https://arxiv.org/abs/1406.5995).
3. S. Fischler and T. Rivoal, *Relations between values of arithmetic
   Gevrey series, and applications to values of the Gamma function*,
   J. Number Theory **261** (2024), 36--54,
   [arXiv:2301.13518](https://arxiv.org/abs/2301.13518).
4. J. Fresán and P. Jossen, *Exponential motives*, especially the
   exponential period conjecture and Proposition 12.1.4,
   [author PDF](https://javier.fresan.perso.math.cnrs.fr/expmot.pdf).
5. B. Snodgrass, *Periods of $E$-operators*,
   [arXiv:2608.06005v2](https://arxiv.org/abs/2608.06005).

Exact primary artifacts used in this and the immediately preceding
audit have the following SHA-256 hashes:

| Artifact | SHA-256 |
|---|---|
| Beukers arXiv source | `3023c4190ccb9b1640b668d0d7ca975cd4d1551e7ba70531bfde1efa97642ad2` |
| Fischler--Rivoal arithmetic $E$-operator source | `ff0443e91c8ff6b98ea9534cb8309a9b6d5b0ad4b86c7469bc619c19d096fb98` |
| Fischler--Rivoal arithmetic-Gevrey source | `304cd713f3488b89768a3bca26858b6197725133ba05d51c7ec19cb48bd67d1b` |
| Snodgrass $E$-period source v2 | `65b4c87421674293c6bc8984eecb52894dddc76f0d1ced70dcad8056daa6e3b5` |
| Companion mixed-division audit | `9e1d933e6c3ec5778ce8d446dbd3cc2fd039e9f664ca8fc024e102e0122a5b30` |
| Independent mixed-value theorem audit | `8bbcd71ffba7076ea09b39849fca825c957e33886703fac3bd7530d62f06ed56` |
| Symbolic certificate script | `44d54f11d2662665ff90acc2ab786b2d87154771da6e4cefb606f838a6bb3b33` |
| Symbolic certificate result | `b834488e904487ea09fe0de80ecdc5364afb18337dcc59d1df4cc6be8988403a` |

## 15. Final conclusion

The explicit low-order branch does not hide an applicable special-case
theorem. Instead, it exposes the missing theorem in its smallest
natural form:



$$
\boxed{
\begin{array}{c}
\text{a rational \(3\times3\) system, ordinary at \(0,1\),}\\
\text{with algebraic initial data and differential Galois group
\(\mathbb G_m\times\mathbb G_a\),}\\
\text{has functionally algebraically independent exponential and
logarithmic coordinates,}\\
\text{but under \(e+\pi\in\overline{\mathbb Q}\) those coordinates
coincide at \(1\).}
\end{array}}
$$



The monodromy matrices place $\pi$ in the logarithmic comparison
block; the finite connection matrix places $e$ in the exponential
block. The $L_s$ construction moves the same $\pi$ into an
asymptotic/Stokes constant, and its inverse-Borel transform differs
from the original arctangent interpolant only by a rational function
vanishing at the target point. No computed invariant couples the two
blocks.

Accordingly, the exact survivor is an archimedean mixed
connection-period injectivity theorem for this explicit system. Such a
theorem would prove the desired transcendence, but none of the audited
monodromy, differential-Galois, $E$-operator, inverse-Borel, or
existing specialization results supplies it.
