> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The mixed-extension moment kernel: adjoint reduction, local
# obstructions, and finite-pole survivors

Date: 2026-08-27 (UTC)

## 1. Question and exact verdict

Let $k=\overline{\mathbb Q}$, and put


$$
x=e^z,\qquad y=-4\arctan z,\qquad
 q=y'=-\frac{4}{1+z^2}.                              \tag{1}
$$


The non-split rank-three system studied in
`sources/explicit_nonsplit_mixed_extension_audit.md` introduces the
connection period


$$
K_r(1)=e\int_0^1e^{-t}r(t)y(t)\,dt                  \tag{2}
$$


for a rational kernel $r\in k(z)$ having no pole on $[0,1]$.  Its
relevant connection entry is $e+\pi+K_r(1)$.  The purpose of this
note is to decide whether one can make $K_r(1)$ vanish, or at least
make it algebraically cancellable, without making the extension split.

There is an exact answer at the differential/cohomological level, but
the last arithmetic condition remains open.

Define


$$
h=\frac{q'}q-1=-\frac{(z+1)^2}{z^2+1},\qquad
 L^*=(D-1)(D+h).                                    \tag{3}
$$


Then the cross extension is rationally split **if and only if**


$$
r=L^*\phi\qquad(\phi\in k(z)).                     \tag{4}
$$


For every such kernel that is regular along the integration path,


$$
K_{L^*\phi}(1)
 =-\pi\bigl(\phi'(1)-2\phi(1)\bigr)
   +2\phi(1)-4e\phi(0).                             \tag{5}
$$


The values of the right side, as $\phi$ ranges through polynomials,
are exactly


$$
V:=k+k e+k\pi.                                     \tag{6}
$$


Consequently every cancellation obtained by a closed rational
integration-by-parts certificate is a split coboundary.  In
particular, this note gives an explicit nonzero $r=L^*\phi$ for
which $K_r(1)=0$, but also gives its explicit rational splitting.
It is not the desired survivor.

Let


$$
\mathcal R=\{r\in k(z):r\text{ has no pole on }[0,1]\},
\quad
 \mathcal H_\times=\mathcal R/L^*\mathcal R,
\quad
 \mathcal H_e=\mathcal R/(D-1)\mathcal R.           \tag{7}
$$


Since $L^*\mathcal R\subseteq(D-1)\mathcal R$, there is a natural
map


$$
\rho:\mathcal H_\times\longrightarrow\mathcal H_e.\tag{8}
$$


Equation (5) makes


$$
\overline K:\mathcal H_\times\longrightarrow
 \mathbb C/V,\qquad [r]\longmapsto[K_r(1)]          \tag{9}
$$


well defined.  The exact remaining condition is


$$
\boxed{\text{find }[r]\in\ker\overline K
        \text{ with }\rho([r])\ne0.}                \tag{10}
$$


This is equivalent to finding a literal zero-moment representative
$r_0\notin(D-1)k(z)$.  Thus (10) cleanly separates genuine
non-splitting from endpoint cancellation.

For a single simple pole $r=1/(z-\alpha)$,
$\alpha\notin[0,1]$, the desired literal cancellation is impossible:


$$
K_{1/(z-\alpha)}(1)\ne0.                           \tag{11}
$$


This follows from a strict Stieltjes-transform sign argument, valid
also for nonreal $\alpha$.  Such a kernel is always outside
$(D-1)k(z)$.  What is not decided is whether its nonzero value lies
in $V$.

For any finite rational-pole family, Sections 7--9 reduce (10) to an
explicit $k$-linear relation among two fixed polynomial core periods,
a Stieltjes transform and its derivatives, and $1,e,\pi$.  No such
relation was proved or found.  The exact survivor is displayed in
(61)--(62) below.

This note does not prove any arithmetic conclusion about $e+\pi$.

## 2. The scalar operator behind the period

Set


$$
w=e^{-z}y.                                         \tag{12}
$$


Since $y'=q$,


$$
(D+1)w=e^{-z}q.                                    \tag{13}
$$


The logarithmic derivative of the right side is $h=q'/q-1$.
Therefore


$$
Lw=0,\qquad L=(D-h)(D+1).                          \tag{14}
$$


The formal adjoint of $L$ is


$$
L^*=(D+1)^*(D-h)^*
     =(-D+1)(-D-h)
     =(D-1)(D+h),                                   \tag{15}
$$


which is (3).  The factorization, rather than an expanded second-order
formula, is the useful normalization: the first factor detects the
exponential extension, while the second solves its coupling to the
logarithmic block.

In this notation


$$
K_r(1)=e\int_0^1r(t)w(t)\,dt.                     \tag{16}
$$



## 3. Exact classification of rationally split cross kernels

Consider the lower-triangular system


$$
\frac d{dz}
 \begin{pmatrix}1\\y\\u\end{pmatrix}
 =
 \begin{pmatrix}
 0&0&0\\
 q&0&0\\
 0&r&1
 \end{pmatrix}
 \begin{pmatrix}1\\y\\u\end{pmatrix}.            \tag{17}
$$


Its normalized last coordinate is


$$
u(z)=e^z\int_0^z e^{-t}r(t)y(t)\,dt,              \tag{18}
$$


so $u(1)=K_r(1)$.

### Theorem 3.1 (split if and only if adjoint-exact)

The system (17) splits over $k(z)$ if and only if there is
$\phi\in k(z)$ such that $r=L^*\phi$.

**Proof.**  A rational splitting has the form


$$
f=A y+B,\qquad A,B\in k(z),                        \tag{19}
$$


with $f'-f=r y$.  Comparing the coefficient of $y$ and the
rational part gives


$$
r=A'-A,\qquad B'-B=-qA.                            \tag{20}
$$


Put $\phi=-B/q$.  The second equation becomes


$$
A=\phi'+\left(\frac{q'}q-1\right)\phi=(D+h)\phi.  \tag{21}
$$


The first equation is consequently


$$
r=(D-1)(D+h)\phi=L^*\phi.                         \tag{22}
$$


Conversely, if (22) holds, take


$$
A=(D+h)\phi,\qquad B=-q\phi.                      \tag{23}
$$


Direct differentiation gives both equations in (20), hence a rational
splitting.  $\square$

If $r$ is regular at a point of $[0,1]$, a rational $\phi$
satisfying $L^*\phi=r$ cannot have a pole there.  Indeed, at such an
ordinary point, a pole of order $m\ge1$ in $\phi$ produces an
uncancelled pole of order $m+2$ through the leading $D^2\phi$
term.  Thus all endpoint values used below exist whenever the kernel
in (22) is admissible.

Theorem 3.1 is the precise scope of the integration-by-parts no-go:
every rational coboundary that closes inside the natural span
$k(z)y+k(z)$ is exactly a split extension class.  It does not assert
that a non-exact period can never vanish numerically; that unresolved
possibility is exactly (10).

## 4. Endpoint concomitant and the cancellable field

Let $r=L^*\phi$, and define $A,B,f$ by (19) and (23).  From
$f'-f=r y$,


$$
e^{-t}r(t)y(t)=\frac d{dt}\bigl(e^{-t}f(t)\bigr).  \tag{24}
$$


Using $y(0)=0$, $y(1)=-\pi$, $q(0)=-4$, and $q(1)=-2$,


$$
\begin{aligned}
 K_r(1)
 &=f(1)-e f(0)\\
 &=-\pi A(1)-q(1)\phi(1)+e q(0)\phi(0)\\
 &=-\pi\bigl(\phi'(1)-2\phi(1)\bigr)
   +2\phi(1)-4e\phi(0),
\end{aligned}                                      \tag{25}
$$


which proves (5).

The boundary map in (25) is onto $V$.  More explicitly, given


$$
v=\lambda_0+\lambda_e e+\lambda_\pi\pi,
 \qquad \lambda_0,\lambda_e,\lambda_\pi\in k,      \tag{26}
$$


prescribe


$$
\phi(0)=-\frac{\lambda_e}{4},\qquad
 \phi(1)=\frac{\lambda_0}{2},\qquad
 \phi'(1)=\lambda_0-\lambda_\pi.                  \tag{27}
$$


These three Hermite data are realized by the quadratic polynomial


$$
\phi(z)=-\frac{\lambda_e}{4}
 +\left(\lambda_\pi+\frac{\lambda_e}{2}\right)z
 +\left(\frac{\lambda_0}{2}-\lambda_\pi
          -\frac{\lambda_e}{4}\right)z^2.          \tag{28}
$$


Substitution into (25) gives $K_{L^*\phi}(1)=v$.

It follows at once that (9) is well defined.  It also proves the
equivalence claimed after (10).  If $[r]\in\ker\overline K$, write
$K_r(1)=v\in V$, choose a polynomial $\phi$ whose boundary value is
$-v$, and put


$$
r_0=r+L^*\phi.                                     \tag{29}
$$


Then


$$
K_{r_0}(1)=0,\qquad
 [r_0]=[r]\text{ in }\mathcal H_\times,\qquad
 \rho([r_0])=\rho([r]).                            \tag{30}
$$


The last equality holds because every adjoint coboundary is already
in the image of $D-1$.  Conversely, a literal zero clearly maps to
zero in $\mathbb C/V$.

Under the hypothetical relation


$$
({\rm H})\qquad e+\pi\in k,                        \tag{31}
$$


one has $V=k+k e$.  Thus any algebraic value of $K_r(1)$, and more
generally any value in $k+k e$, is cancellable by the same split
correction without changing either cohomology class in (30).

## 5. An exact zero-moment kernel that fails because it is split

The simplest systematic way to force every term in (25) to vanish is
to take a polynomial with
$\phi(0)=\phi(1)=\phi'(1)=0$.  For


$$
\phi=z^2(1-z)^2,                                   \tag{32}
$$


direct computation gives


$$
r_\phi=L^*\phi=
 \frac{
 z^8-8z^7+17z^6-24z^5+37z^4-24z^3+23z^2-16z+2
 }{(z^2+1)^2}.                                      \tag{33}
$$


This rational kernel has no pole on $[0,1]$, and (25) proves


$$
K_{r_\phi}(1)=0.                                   \tag{34}
$$


However, its splitting is explicit:


$$
\begin{aligned}
 A&=-\frac{z(z-1)(z^4-3z^3+z^2-5z+2)}{z^2+1},\\
 B&= \frac{4z^2(z-1)^2}{z^2+1},
\end{aligned}                                      \tag{35}
$$


and one verifies exactly that


$$
A'-A=r_\phi,\qquad B'-B=-qA.                      \tag{36}
$$


Therefore $r_\phi\in L^*k(z)\subset(D-1)k(z)$.
This example separates two notions that otherwise look deceptively
similar:

* endpoint cancellation is the vanishing of the concomitant (25);
* genuine non-splitting is nonvanishing of the class in
  $\mathcal H_\times$, or, in the stronger requested form,
  nonvanishing after $\rho$.

The adjoint construction guarantees the first only by destroying the
second.

## 6. A complete local test for $r\notin(D-1)k(z)$

Let $r\in k(z)$.  At a finite pole $\alpha$, write its principal
part as


$$
r(z)=\sum_{j=1}^{m_\alpha}
 \frac{c_{\alpha,j}}{(z-\alpha)^j}+O(1).            \tag{37}
$$


Define the local exponential residue


$$
\Omega_\alpha(r)=
 \sum_{j=1}^{m_\alpha}
 \frac{(-1)^{j-1}}{(j-1)!}\,c_{\alpha,j}.           \tag{38}
$$



### Proposition 6.1 (Hermite criterion for $D-1$)

One has


$$
r\in(D-1)k(z)\quad\Longleftrightarrow\quad
 \Omega_\alpha(r)=0
 \text{ for every finite pole }\alpha.             \tag{39}
$$



**Proof.**  If $r=(D-1)A$, then


$$
e^{-z}r=(e^{-z}A)'.                                \tag{40}
$$


The residue of a derivative at every finite pole is zero.  Expanding
$e^{-z}=e^{-\alpha}\sum_{n\ge0}(-1)^n(z-\alpha)^n/n!$ shows that this residue is
$e^{-\alpha}\Omega_\alpha(r)$, proving necessity.

For sufficiency, eliminate the principal parts pole by pole.  If the
highest term at $\alpha$ is $c_m(z-\alpha)^{-m}$, $m\ge2$, then
subtracting


$$
(D-1)\left(-\frac{c_m}{m-1}(z-\alpha)^{-(m-1)}\right) \tag{41}
$$


removes it and only changes lower-order terms at the same pole.
Iteration leaves precisely
$\Omega_\alpha(r)/(z-\alpha)$.  Under the assumed vanishing, every
finite principal part is removed.  The remaining polynomial belongs
to $(D-1)k[z]$, since $D-1$ is triangular with diagonal $-1$ on
the monomial basis.  This constructs a rational preimage.  $\square$

For a simple pole, $\Omega_\alpha(c/(z-\alpha))=c$.  Therefore every
nonzero sum of distinct simple partial fractions is outside
$(D-1)k(z)$, independently at each pole.  In particular
$1/(z-2)$ passes the strong non-splitting test requested here.

For the zero-moment adjoint example (33), the two obstructions at
$\alpha=i,-i$ vanish separately, as they must from (36).

## 7. Polynomial cross classes collapse to two core periods

Although every polynomial is in $(D-1)k[z]$ and hence does not meet
the strengthened condition $\rho([r])\ne0$, polynomial kernels can
still define non-split **cross** extensions.  Their quotient is exactly
two-dimensional.

Given $P\in k[z]$, let $A\in k[z]$ be the unique polynomial with


$$
A'-A=P.                                            \tag{42}
$$


By (20), the cross extension splits exactly when
$B'-B=-qA=4A/(z^2+1)$ has a rational solution.  Its only possible
poles are the simple poles at $i$ and $-i$.  Proposition 6.1 says
that a solution exists exactly when their residues vanish, namely
when


$$
A(i)=A(-i)=0
 \quad\Longleftrightarrow\quad z^2+1\mid A.         \tag{43}
$$



Reduce $A$ modulo $z^2+1$:


$$
A\equiv az+b\pmod{z^2+1}.                          \tag{44}
$$


Then, modulo $L^*k(z)$,


$$
P\equiv(D-1)(az+b)
   =-az+(a-b)=b(-1)+a(1-z).                         \tag{45}
$$


Thus the polynomial quotient is represented by the two kernels
$-1$ and $1-z$.

Put


$$
\begin{aligned}
 \kappa_0&=K_{-1}(1)
 =4e\int_0^1\frac{e^{-t}}{1+t^2}\,dt-\pi,\\
 \kappa_1&=K_{1-z}(1)
 =4e\int_0^1\frac{t e^{-t}}{1+t^2}\,dt-\pi.
\end{aligned}                                      \tag{46}
$$


Equations (25) and (45) give the exact congruence


$$
K_P(1)\equiv b\kappa_0+a\kappa_1\pmod V.          \tag{47}
$$


Consequently a nonsplit polynomial class has an algebraically
cancellable moment if and only if


$$
b\kappa_0+a\kappa_1\in V
 \quad\text{for some }(a,b)\ne(0,0).               \tag{48}
$$


This is exactly a $k$-linear relation among
$1,e,\pi,\kappa_0,\kappa_1$ with a nonzero core coefficient.
The audited mixed-value theorems do not decide this relation.

For orientation only, the certificate gives


$$
\begin{aligned}
 \kappa_0&=2.5645934990166531028380080380475608717643\ldots,\\
 \kappa_1&=-1.0503705346977063490013726825397433677479\ldots.
\end{aligned}                                      \tag{49}
$$


The unique real constant $c$ for which the linear polynomial
$r(z)=z-c$ has zero moment is


$$
c=0.5904339088824595812612908321619564634964\ldots.\tag{50}
$$


Proving that this number is algebraic would produce an exact
algebraic-coefficient cancellation, while proving it transcendental
would rule out only this one-dimensional attempt.  Its arithmetic
nature is not established here.

## 8. The one-simple-pole family: rigorous nonvanishing

Define the positive measure on $(0,1]$


$$
d\mu(t)=-e^{1-t}y(t)\,dt
         =4e^{1-t}\arctan(t)\,dt.                  \tag{51}
$$


For $\alpha\in\mathbb C\setminus[0,1]$, let


$$
F(\alpha)=K_{1/(z-\alpha)}(1)
 =\int_0^1\frac{d\mu(t)}{\alpha-t}.                \tag{52}
$$


If $\alpha>1$, the integrand in (52) is strictly positive; if
$\alpha<0$, it is strictly negative.  If
$\operatorname{Im}\alpha\ne0$, then


$$
\operatorname{Im}\frac1{\alpha-t}
 =-\frac{\operatorname{Im}\alpha}
        {(\operatorname{Re}\alpha-t)^2+
         (\operatorname{Im}\alpha)^2}              \tag{53}
$$


has one strict sign throughout the interval.  Since $\mu$ has
positive mass, all three cases prove


$$
F(\alpha)\ne0.                                     \tag{54}
$$



Together with $\Omega_\alpha(1/(z-\alpha))=1$, this proves that a
single algebraic pole off the path is genuinely $(D-1)$-nonexact but
can never give a literal zero period.  The remaining one-pole question
is the arithmetic inclusion


$$
F(\alpha)\stackrel{?}{\in}V,                       \tag{55}
$$


which positivity cannot address.

The same argument rules out many sign-constrained families.  For
example, if all real poles satisfy $\alpha_j>1$ and all real
coefficients $c_j\ge0$, not all zero, then
$\sum_jc_jF(\alpha_j)>0$.  For poles all below $0$, the analogous
sum is negative.  With opposite signs, cancellation is possible over
$\mathbb R$, but algebraic coefficients require an unproved
arithmetic statement.  For two poles, it is precisely the algebraicity
of the ratio of the two nonzero Stieltjes values.

More generally, because $e^{1-t}y(t)<0$ for $0<t\le1$, every nonzero
real rational function $r$ of constant sign on $[0,1]$ has a strictly
nonzero moment.  If $r=N/D$ is reduced, has real algebraic
coefficients, and has no pole on the interval, then $D$ has constant
sign there.  Hence a literal zero moment forces the numerator $N$ to
have a zero in $(0,1)$.  In particular, no real rational kernel with
constant nonzero numerator can work, regardless of how many real or
conjugate pole pairs occur in its denominator.  This is a rigorous
barrier for a substantially larger family than the one-pole case.

## 9. Exact finite-pole moment and kernel classification

Let $S\subset\overline{\mathbb Q}\setminus[0,1]$ be finite and write
an arbitrary rational kernel with poles in $S$ as


$$
r(z)=P(z)+\sum_{\alpha\in S}\sum_{j=1}^{m_\alpha}
       \frac{c_{\alpha,j}}{(z-\alpha)^j}.           \tag{56}
$$


Let $A'-A=P$, and let $az+b$ be the remainder of $A$ modulo
$z^2+1$, as in (44).  Differentiating (52) under the integral sign
gives the exact identity


$$
K_{1/(z-\alpha)^j}(1)
 =\frac{F^{(j-1)}(\alpha)}{(j-1)!}.                 \tag{57}
$$


Combining (47) and (57) yields


$$
K_r(1)\equiv
 b\kappa_0+a\kappa_1
 +\sum_{\alpha\in S}\sum_{j=1}^{m_\alpha}
  \frac{c_{\alpha,j}}{(j-1)!}F^{(j-1)}(\alpha)
 \pmod V.                                          \tag{58}
$$


At the same time, Proposition 6.1 gives the independent local test


$$
r\notin(D-1)k(z)\quad\Longleftrightarrow\quad
 \Omega_\alpha(r)\ne0
 \text{ for at least one }\alpha\in S,             \tag{59}
$$


where


$$
\Omega_\alpha(r)=
 \sum_{j=1}^{m_\alpha}
 \frac{(-1)^{j-1}}{(j-1)!}c_{\alpha,j}.             \tag{60}
$$



Equations (58)--(60) are the requested finite-dimensional
classification.  They show that a finite-pole family succeeds exactly
when one proves a relation


$$
b\kappa_0+a\kappa_1
 +\sum_{\alpha,j}
  \frac{c_{\alpha,j}}{(j-1)!}F^{(j-1)}(\alpha)
 \in k+k e+k\pi                                    \tag{61}
$$


whose coefficients also satisfy


$$
\exists\alpha:\quad
 \sum_j\frac{(-1)^{j-1}}{(j-1)!}c_{\alpha,j}\ne0. \tag{62}
$$


The first condition is the global arithmetic period collision; the
second is a completely decidable local certificate that the kernel is
not a disguised $(D-1)$ coboundary.

For a simple-pole-only family, (61) reduces to a $k$-linear relation
among $1,e,\pi,F(\alpha_1),\ldots,F(\alpha_N)$, and (62) merely says
that the coefficient vector is nonzero.  Thus raw coefficient-space
dimension does not force a collision: the image consists of actual
complex period values, and an algebraic relation among them is exactly
what must be proved.

The deterministic calculation evaluated the six real poles


$$
-3,-2,-1,2,3,4                                     \tag{63}
$$


to 220 decimal digits.  A PSLQ search on those six values together
with $1,e,\pi$ returned no vector up to coefficient bound $10^{20}$
at tolerance $10^{-205}$.  Likewise, PSLQ returned no relation among
$1,e,\pi,\kappa_0,\kappa_1$ up to $10^{50}$ at the same tolerance.
These are diagnostics only.  They neither prove independence nor
exclude larger or specially structured relations.

## 10. What exactly remains, and why the old machinery does not close it

The analysis leaves three sharply separated outcomes.

1. If $r=L^*\phi$, its moment is explicitly in $V$, and it can be
   made zero by endpoint interpolation.  But the cross extension is
   rationally split and $r\in(D-1)k(z)$.

2. If $r=1/(z-\alpha)$, the extension is genuinely non-split in the
   stronger $D-1$ sense and its moment is rigorously nonzero.  No
   argument here decides whether that value belongs to $V$.

3. For two or more poles, or a polynomial part plus poles, success is
   exactly the relation (61) with the local survivor condition (62).
   Neither integration by parts, monodromy, nor the differential
   Galois group supplies that numerical relation.

The earlier audit proves functional algebraic independence for the
explicit non-split system, but evaluation at $z=1$ need not preserve
that independence.  The connection-period field can therefore have
smaller transcendence degree than the Picard--Vessiot group without
contradicting any specialization theorem used in this archive.  The
mixed $E/G$ and logarithm-value theorems were separately audited in
`sources/independent_mixed_e_g_logarithm_value_audit.md` and
`sources/e_function_logarithm_exceptional_set_no_go.md`; none of their
hypotheses turns (61) into a proved independence statement.

Even a successful non-split zero kernel would not, by itself, prove
that (31) is false.  It would produce the strongest connection-matrix
configuration in this branch--a genuinely non-split module whose new
mixed connection entry contains $e+\pi$ without an extra numerical
period--but a numerical connection-period injectivity theorem would
still be needed to derive a contradiction.

The sharp survivor of this branch is therefore not a vague request for
"a clever rational kernel."  It is the explicit arithmetic problem
(61)--(62), equivalently (10).

## 11. Deterministic certificate

The script
`scripts/mixed_extension_moment_kernel_certificate.py` performs the
following checks:

* the factored scalar operator and adjoint identities;
* the exact formula (33);
* both splitting equations (36);
* the zero endpoint concomitant;
* the quadratic interpolation proving that the boundary map has image
  $k+k e+k\pi$;
* the local $D-1$ obstructions at $i,-i$, and at the pole $2$;
* the polynomial normal form through degree $12$;
* 220-digit evaluation and the explicitly non-rigorous PSLQ
  diagnostics described above.

Its byte-for-byte output is
`results/mixed_extension_moment_kernel_certificate.json`.

SHA-256:

| Artifact | SHA-256 |
|---|---|
| `scripts/mixed_extension_moment_kernel_certificate.py` | `89d66a0b702f8ca2fe58d737602a5e0c7d8f31f99c6742a86b31abba3bba834f` |
| `results/mixed_extension_moment_kernel_certificate.json` | `6f6eb2d611d9034f52261126c6a96576ea66e301794f25309c7cee28952fb20b` |

The symbolic checks certify the displayed algebra.  The analytical
nonvanishing theorem (54) and the equivalences (39), (58)--(62) are
proved in this note; the floating-point data are not used in those
proofs.
