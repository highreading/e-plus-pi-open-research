> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Odd Hardy reference, exact finite moments, and reversal phase

Date: 2026-09-13. Independent derivation and normalization audit by
audit_sources. Independent review: FULL PASS by audit_computations in
raw_odd_hardy_framework_independent_review.md.
This note certifies the framework needed by the new odd
kernel and saddle calculations; their nonzero limiting amplitudes remain
separate calculations.

The inputs already have independent PASS:
raw_odd_boundary_operator_limit.md,
raw_odd_limiting_determinant_interval_certificate.md,
raw_odd_dual_flatness_and_exponential_error.md, and the circular binomial
polynomial theorem. The even Hardy argument has PASS in
raw_actual_dual_hardy_independent_review.md. No finite-operator certificate
or canonical degree is recomputed here.

## 1. The actual positive metric and reference

Put n=2m+1, m>=0, and retain the actual matrix and solution



$$
A_{ij}=[z^{n+i-j}]e^z(1+z^2)^n,\qquad
 u=A^{-1}e_0,\qquad
 u(z)=\sum_{j=0}^n u_jz^j.
$$



The actual odd signed symbol is e^z(2cos(theta))^(2m+1). The positive
metric used to normalize its accepted operator is instead



$$
w_+(z)=|1+z^2|^{2m+2},\qquad
 c_m=(G^{-1})_{00}
 =\frac{((2m+1)!)^2}{m!(3m+2)!}.
$$



Set a=m+1. Let Phi_j^a be the monic circular polynomial for
|1-w|^(2a), with the already proved formula



$$
\Phi_j^a(w)=\sum_{\ell=0}^j
 \binom j\ell\frac{(a)_{j-\ell}}{(a+\ell+1)_{j-\ell}}w^\ell,
\qquad
 h_j^a=\frac{j!(2a+j)!}{((a+j)!)^2}.
$$



All parenthesized factorials are rising. Define



$$
\boxed{\Psi_n(z)=(-1)^m z\Phi_m^a(-z^2),\qquad
 F_m(z)=(\Phi_m^a)^*(-z^2).}
 \tag{1}
$$



The first polynomial is monic of degree n; the second has degree n-1
(degree zero when m=0) and constant coefficient one. Parity and the
pushforward w=-z^2 prove that Psi_n is the monic degree-n orthogonal
polynomial for w_+. Its squared norm is



$$
\|\Psi_n\|_{w_+}^2=h_m^{m+1}
 =\frac{m!(3m+2)!}{((2m+1)!)^2}=\frac1{c_m}.
 \tag{2}
$$



Every root of Phi_m lies strictly inside the disk by the previously
proved monic minimization argument. Psi_n adds a root at zero.
Consequently F_m has no zero in the closed disk. In particular its
real values on [-1,1] are positive, since F_m(0)=1.

The exact degree-n reversal is



$$
\Psi_n(z)=z^nF_m(1/z),\qquad
 \Psi_n^*(z)=F_m(z).
 \tag{3}
$$



The lower degree of F_m is a consequence of the root zero in Psi_n;
it does not change the degree used for reversal.

## 2. Exact Bernstein--Szegő identity through degree n

The measures



$$
d\mu=w_+(z)\frac{d\theta}{2\pi},\qquad
 d\nu=\frac1{c_m}|F_m(z)|^{-2}\frac{d\theta}{2\pi}
$$



have the same Laurent moments at exponents -n,...,n. The elementary
finite-moment proof from the even note remains valid, including the
degree difference. Under nu, analyticity of 1/F gives



$$
\int\Psi_n z^{-j}\,d\nu
 =\frac1{c_m}\int\frac{z^{n-j}}{F_m(z)}\,\frac{d\theta}{2\pi}
 =0\quad(0\le j<n),
$$



and the value at j=n is 1/c_m. These are exactly the mu values,
including the norm relation (2). Conjugation supplies the reverse
equations.

For completeness, multiplication of the Laurent span by z^n gives



$$
\Psi_n\mathcal P_n+F_m\mathcal P_n.
$$



Psi_n and F_m are coprime. An element in the intersection is
Psi_n F_m h; because deg Psi_n=n and both multipliers have degree at
most n, h must be constant. Thus the intersection is one-dimensional,
even though deg F_m=n-1. The sum has dimension 2n+1 and fills
P_(2n). This checks the only new dimension issue in the odd case.

It follows that for EVERY polynomial p of degree at most n,



$$
\boxed{\displaystyle
 \|p\|_{w_+}^2=\frac1{c_m}\left\|\frac p{F_m}\right\|_{H^2}^2.}
 \tag{4}
$$



This is an exact identity. It is not an estimate comparing the signed
odd weight with its absolute value.

## 3. Uniform bounds for both actual analytic factors

Let Atilde=G^(-1/2)AG^(-1/2). The reviewed odd operator and determinant
theorems imply



$$
K_A=\sup_{m\ge0}\|\widetilde A_m^{-1}\|<\infty,\qquad
 s_m\longrightarrow s_\infty\ne0,\qquad s_m\ne0\text{ for every }m.
$$



The finitely many initial inverse norms are finite. Likewise



$$
S=\sup_{m\ge0}|s_m|<\infty.
$$



No effective numerical value for K_A or S is asserted here. From the
actual inverse equation and the scalar Schur normalization,



$$
\|u\|_{w_+}\le K_A\sqrt{c_m},\qquad
 u_0=c_m\,v_m^*\widetilde A_m^{-1}v_m=\frac{c_m}{s_m}.
 \tag{5}
$$



In particular u_0 is real and nonzero; it is negative for all sufficiently
large m. This sign must not be replaced by even-degree positivity.

All coefficients are real. Use degree n for
u^*(z)=z^n u(1/z), and define



$$
R_n(z)=\frac{u(z)}{u_0F_m(z)},\qquad
 \widetilde R_n(z)=\frac{u^*(z)}{u_0F_m(z)}.
 \tag{6}
$$



The circle moduli of u and u^* agree. Applying (4)--(5) proves



$$
\boxed{\|R_n\|_{H^2},\ \|\widetilde R_n\|_{H^2}
 \le K_A|s_m|\le K_AS.}
 \tag{7}
$$



Therefore both families are locally bounded on the disk, with



$$
|R_n(z)|,\ |\widetilde R_n(z)|
 \le\frac{K_AS}{\sqrt{1-|z|^2}}.
 \tag{8}
$$



The same bounds apply to phase multiples (-1)^m of either family.
They supply Montel compactness and the usual Cauchy derivative bounds.
If the separate kernel calculation identifies a unique pointwise limit
on a real interval inside the disk, the whole analytic family converges
locally uniformly, with all fixed derivatives. No convergence rate or
nonvanishing amplitude follows from (7) alone.

R_n(0)=1, but in general Rtilde_n(0)=u_n/u_0, not one. The even
explicit constant e*sec(1) is not carried over: (7) uses the accepted
odd uniform inverse and its scalar, not a positive odd sector inequality.

## 4. Exact exterior identity and the extra factor

For |z|>1, the definitions give the exact identity



$$
\boxed{\displaystyle
 \widetilde R_n(1/z)=\frac{u(z)}{u_0\Psi_n(z)}
 =\frac{u(z)}{u_0(-1)^m z\Phi_m^{m+1}(-z^2)}.}
 \tag{9}
$$



There is an extra z relative to the even monic comparison. Dropping it
changes the exterior saddle amplitude, even though it has modulus one
on the unit circle.

In the odd Cayley representation



$$
u(z)=u_1(t)+z u_2(t),\quad t=z^2,\quad
 P_j(y)=(1-iy)^m u_j(t),\quad
 t=\frac{1+iy}{1-iy},
$$



both components have degree at most m; there is no missing-channel
constraint. The common scalar weight has exponent beta=2m+2.
The original constant coefficient is P_1(i)/2^m. The top coefficient
of z^n is P_2(-i)/2^m. These factors are positive, and the monic
reference Psi_n lies in the second component, not the first.

Consequently the exact finite exterior ratio, before phase changes, is



$$
\widetilde R_n(1/z)=
 \frac{(\ell_m^o)^*[(x_m^o)_1+z(x_m^o)_2]}
 {g_m\,z\,(\ell_m^o)^*(k_m^o)_2},
 \qquad g_m=u_0/c_m=1/s_m,
 \tag{10}
$$



where x_m^o is the normalized actual solution, k_m^o is the unit
minus-i Riesz vector in component two, and ell_m^o is the scalar
evaluation Riesz vector at the relevant exterior imaginary node.
The positive kernel magnitude and the common Cayley denominator cancel.

Reverse the scalar basis and choose



$$
x_m=i^m x_m^o,\qquad
 k_m=(-i)^m k_m^o,\qquad
 \ell_m=(-i)^m\ell_m^o.
$$



Their relative phase gives



$$
\boxed{\displaystyle
 (-1)^m\widetilde R_n(1/z)=
 \frac{\ell_m^*[(x_m)_1+z(x_m)_2]}
 {g_m\,z\,\ell_m^*(k_m)_2}.}
 \tag{11}
$$



Thus at z=-phi the denominator contains exactly -phi, in addition
to the actual possibly negative g_m. Both factors must remain in the
limiting amplitude. The interior comparison uses the plus-i reference
in component one and matching i^m phases, so it has no alternating
phase. This is a normalization identity, not a sign assertion about
the yet-to-be-certified odd amplitudes.

## 5. Distinguishing the literal absolute odd weight

If one instead chooses the positive absolute symbol weight



$$
w_{\rm abs}=|1+z^2|^{2m+1},
$$



its scalar circular parameter is a=m+1/2. It has its own monic
polynomial Phi_m^abs, reference
Psi_abs=(-1)^m z Phi_m^abs(-z^2), and reversal F_abs.
The same finite-moment proof gives (4) with its own inverse corner
c_abs. These polynomials must not be substituted into (1) or the
accepted beta=2m+2 operator coordinates.

A uniform Hardy theorem nevertheless also exists for this alternative.
The reviewed positive-weight comparison on P_n gives



$$
\|p\|_{w_-}^2\le\frac54\|p\|_{w_+}^2,\qquad
 w_-=|1+z^2|^{2m},
$$




$$
\|p\|_{w_{\rm abs}}^2
 \le\frac{\sqrt5}{2}\|p\|_{w_+}^2.
$$



Also w_+<=2w_abs pointwise, so the evaluation norms satisfy
c_abs<=2c_m. The exact finite-moment identity then yields the
uniform squared Hardy bound



$$
\left\|\frac{u}{u_0F_{\rm abs}}\right\|_{H^2}^2,
 \ \left\|\frac{u^*}{u_0F_{\rm abs}}\right\|_{H^2}^2
 \le\sqrt5\,K_A^2 S^2.
$$



This verifies that the literal absolute-weight framework is possible,
but the actual contour continuation being developed uses (1), a=m+1.

## 6. Frozen normalization control

The already saved n=1 control gives u(z)=-2+3z,
c_0=1/2, s_0=-1/4, F_0=1, Psi_1=z. Hence



$$
u_0=c_0/s_0=-2,\qquad
 R_1(z)=1-\tfrac32z,\qquad
 \widetilde R_1(z)=z-\tfrac32.
$$



Equation (9) is exact at this base degree and exhibits the essential
odd factor z. This uses a frozen control, not a new canonical solve.
