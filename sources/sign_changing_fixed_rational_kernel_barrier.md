> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Sign-changing fixed rational kernels: a Laplace barrier

Date: 2026-08-26

## Result

The positivity hypothesis in the fixed-rational-kernel theorem is not
essential.  Let



$$
K(x)\in\mathbb Q(x)
$$



be any fixed real rational function with no pole on $[0,1]$.  For an
infinite set of even positive integers $n$, suppose



$$
J_n(K):=\int_0^1x^n(1-x)^nK(x)\,dx
=r_n+\varepsilon_nc_n\pi,                       \tag{1}
$$



where $r_n,c_n\in\mathbb Q$, $c_n>0$, and
$\varepsilon_n\in\{1,-1\}$.  Primitive-normalize this $\pi$-form,
match its target coefficient with the primitive exponential beta form, and
finally remove any content created by the match.

**Theorem.**  The absolute values of all sufficiently large final primitive
matched forms tend to infinity along the index set in (1).

Thus no single fixed rational kernel can repair the symmetric common-beta
construction, even if the kernel changes sign and analytic cancellation is
allowed.  The remaining scope is genuinely outside this theorem: a kernel
depending on $n$, different weights for the two constants, or a
nonrational kernel.

This is a family-specific obstruction and does not prove that $e+\pi$ is
irrational, algebraic, or transcendental.

## 1. Only the symmetric part contributes

Put



$$
K_{\mathrm s}(x)=\frac{K(x)+K(1-x)}2.            \tag{2}
$$



Because $x^n(1-x)^n$ is invariant under $x\mapsto1-x$,



$$
J_n(K)=J_n(K_{\mathrm s}).                       \tag{3}
$$



If $K_{\mathrm s}\equiv0$, every value in (3) is zero.  Equation (1)
would then give a rational relation
$r_n+\varepsilon_nc_n\pi=0$ with $c_n\ne0$, contradicting the
irrationality of $\pi$.  Hence $K_{\mathrm s}$ is a nonzero rational
function.

The function $K_{\mathrm s}$ is analytic near $x=1/2$ and is even about
that point.  There are therefore a unique integer $m\geq0$ and a nonzero
real number $a$ such that



$$
K_{\mathrm s}(1/2+t)=a\,t^{2m}+O(t^{2m+2})
\qquad(t\to0).                                   \tag{4}
$$



### Lemma 1.1 (signed beta-moment asymptotic)

With $a,m$ from (4),



$$
J_n(K)=
\frac{a\,\Gamma(m+1/2)}{2\cdot4^m}\,
4^{-n}n^{-m-1/2}\left(1+O_K(n^{-1})\right).      \tag{5}
$$



In particular, there are constants $c_0>0$ and $n_0$ such that



$$
\operatorname{sgn}J_n(K)=\operatorname{sgn}a,
\qquad
|J_n(K)|\geq
c_0\,4^{-n}n^{-m-1/2}                            \tag{6}
$$



for every $n\geq n_0$.

### Proof

Set $x=1/2+t$.  Equations (3)--(4) give



$$
J_n(K)=4^{-n}\int_{-1/2}^{1/2}
(1-4t^2)^nK_{\mathrm s}(1/2+t)\,dt.              \tag{7}
$$



On a fixed small neighborhood of zero, put $y=2\sqrt n\,t$.  Then



$$
(1-4t^2)^n=(1-y^2/n)^n,\qquad
t^{2m}=\frac{y^{2m}}{4^mn^m},\qquad
dt=\frac{dy}{2\sqrt n}.                          \tag{8}
$$



For $|y|\leq\sqrt n$,



$$
0\leq(1-y^2/n)^n\leq e^{-y^2}.                  \tag{9}
$$



Dominated convergence, followed by one further Taylor term in (4) and in
$\log(1-y^2/n)$, gives



$$
\int_{-\sqrt n}^{\sqrt n}
y^{2m}(1-y^2/n)^n\,dy
=\Gamma(m+1/2)+O_m(n^{-1}).                     \tag{10}
$$



The part of (7) outside the fixed neighborhood of zero is
$O_K(4^{-n}\rho^n)$ for some $\rho<1$, because $K_{\mathrm s}$ is
bounded on $[0,1]$.  Substitution of (4), (8), and (10) into (7) proves
(5), and (6) follows. $\square$

## 2. Arithmetic complexity remains only exponential

The height lemma in sources/fixed_rational_kernel_barrier.md does not use
positivity.  For completeness, its mechanism is as follows.

Choose a reduced representation $K=P/Q$ with coprime
$P,Q\in\mathbb Z[x]$.  Since $K$ has no pole on $[0,1]$, $Q$ has
no zero there.  Fixed-denominator rational long division of
$P(x)x^n(1-x)^n$ by $Q(x)$ gives quotient and remainder coefficients on
one common denominator of exponential size.  Integrating the quotient
introduces only
$\operatorname{lcm}(1,\ldots,O_K(n))=\exp(O_K(n))$.

The remainder integral lies in the fixed finite-dimensional
$\mathbb Q$-space spanned by



$$
1,\quad\pi,\quad
\int_0^1\frac{x^j}{Q(x)}\,dx
\quad(0\leq j<\deg Q).                           \tag{11}
$$



Extend $1,\pi$ to a basis of this space.  Whenever all other coordinates
cancel as in (1), uniqueness of coordinates shows that



$$
H(r_n)\leq C_1^n,\qquad H(c_n)\leq C_1^n          \tag{12}
$$



for a fixed $C_1$.

Let



$$
L_n=A_n+\varepsilon_nB_n\pi=\mu_nJ_n(K)          \tag{13}
$$



be the primitive integer normalization, with $B_n,\mu_n>0$.
Writing $r_n=a_n/b_n$, $c_n=u_n/v_n$ in lowest terms and clearing the
two denominators gives, after increasing the fixed constant,



$$
c_nB_n\leq C_2^n.                                \tag{14}
$$



No sign hypothesis on $K$ entered this argument.

## 3. Primitive matching and final content

For even $n$, put



$$
E_n=\frac1{n!}\int_0^1x^n(1-x)^ne^x\,dx
=q_ne-p_n>0.                                     \tag{15}
$$



The coefficient pair is primitive and



$$
q_n\geq\frac{n(2n-1)!}{n!}.                      \tag{16}
$$



Let $\sigma=\operatorname{sgn}a$.  By (6), the primitive form



$$
\widetilde L_n=\sigma L_n>0                     \tag{17}
$$



has $\pi$-coefficient



$$
\delta_nB_n,\qquad\delta_n=\sigma\varepsilon_n\in\{1,-1\},
$$



and the primitive-invariant value-to-coefficient ratio is



$$
\frac{\widetilde L_n}{B_n}=\frac{|J_n(K)|}{c_n}. \tag{18}
$$



If two primitive pairs $(-p,q)$ and $(A,\delta B)$ are minimally
coefficient-matched, the content acquired by the resulting pair divides
$\gcd(q,B)$.  Indeed, with
$d=\gcd(q,B)$, $q=dq_0$, and $B=dB_0$, the matched constant is



$$
-B_0p\mathbin{\pm}q_0A,
$$



which is coprime to $q_0B_0$.  Thus final primitive reduction divides the
raw value by at most $B$.

## 4. Divergence in both sign classes

If $\delta_n=1$, the minimally matched form is a positive sum.  Equations
(18) and the final-content lemma give



$$
|\Lambda_n^{\mathrm{prim}}|
\geq\frac{q_n|J_n(K)|}{c_nB_n}.                  \tag{19}
$$



If $\delta_n=-1$, the matched value per common coefficient is



$$
\frac{E_n}{q_n}-\frac{|J_n(K)|}{c_n}.            \tag{20}
$$



The elementary bound



$$
E_n\leq\frac{e\,n!}{(2n+1)!}                    \tag{21}
$$



together with (6) and $c_n\leq C_1^n$ gives



$$
0\leq
\frac{E_n/q_n}{|J_n(K)|/c_n}
\leq
C_3^n n^{m+1/2}\frac{n!}{(2n+1)!}
\longrightarrow0.                               \tag{22}
$$



Here it is enough to use $q_n\geq1$ and
$(2n+1)!/n!\geq(n+1)^{n+1}$.  Hence (20) is negative for all sufficiently
large $n$, with absolute value at least
$|J_n(K)|/(2c_n)$.  Matching and final primitive reduction therefore give



$$
|\Lambda_n^{\mathrm{prim}}|
\geq\frac{q_n|J_n(K)|}{2c_nB_n}.                 \tag{23}
$$



Finally, (6), (14), and (16) imply in either sign class



$$
|\Lambda_n^{\mathrm{prim}}|
\geq
c_4\,
\frac{n(2n-1)!}{n!}\,
\frac{4^{-n}n^{-m-1/2}}{C_2^n}.                 \tag{24}
$$



Since



$$
\frac{n(2n-1)!}{n!}
=n\prod_{k=n+1}^{2n-1}k
\geq n^n,                                       \tag{25}
$$



the right side of (24) tends to infinity.  This proves the theorem.

## 5. Residual scope

The proof now covers every fixed rational $K$ with no pole on the
integration interval, regardless of sign.  It still relies on:

1. one fixed kernel, rather than $K=K_n$;
2. the common symmetric beta weight $x^n(1-x)^n$;
3. exact moments in $\mathbb Q+\mathbb Q\pi$;
4. coefficient synchronization by integer cross-multiplication.

An $n$-dependent kernel can have superexponential arithmetic complexity,
and two different weights need not share the Laplace asymptotic used here.
Those are the precise surviving direct-integral directions.
