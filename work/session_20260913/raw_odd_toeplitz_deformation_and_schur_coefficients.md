> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Odd Toeplitz deformation: exact Schur coefficients and a uniform local scalar bound

Date: 2026-09-13. Original bounded continuation by audit_sources.
Independent review: FULL PASS by audit_results; see raw_odd_deformation_independent_review.md.

This note treats the actual deformation


$$
a_k(x)=[z^k]e^{xz}(1+z^2)^n,\qquad
 A_n(x)=(a_{n+i-j}(x))_{i,j=0}^n,\qquad D_n(x)=\det A_n(x).
$$


It obtains an exact all-order signed coefficient formula, the first two nonconstant even coefficients, the leading inverse-corner coefficient, and a uniform local bound near x=0. It does **not** extend that bound to x=1. In particular the actual odd scalar condition log|s_m(1)|=o(m) remains open.

The source audit covered raw_joint_dual_hankel_and_even_root_product.md, raw_odd_dual_toeplitz_scalar_obstruction.md and its review, and the older centered_cosh_factorial_pascal_height_theorem.md and centered_cosh_pade_residual_quotient_theorem.md. The last two use positive Schur alphabets. The present alphabet contains both i and -i; their positivity arguments do not transfer.

## 1. Exact rectangular Schur specialization

Define the elementary specialization by


$$
E(t)=\sum_{k\ge0}e_kt^k=e^{xt}(1+t^2)^n.
$$


It consists formally of n copies of i and n copies of -i, together with the exponential specialization. Transposing the determinant and using the dual Jacobi--Trudi definition gives exactly


$$
\boxed{D_n(x)=s_{((n+1)^n)}[E].}                         \tag{1}
$$


This is an identity of finite polynomials, not an appeal to positivity or convergence of an infinite alphabet.

The total rectangular size is n(n+1). Equivalently, if A is the finite alphabet (i,...,i,-i,...,-i), expansion in the exponential specialization gives


$$
D_n(x)=\sum_{\mu\subseteq((n+1)^n)}
 s_\mu(A)\,f^{((n+1)^n)/\mu}
 \frac{x^{n(n+1)-|\mu|}}{(n(n+1)-|\mu|)!}.                 \tag{2}
$$


Here f^(lambda/mu) counts standard tableaux of the skew diagram. This formula also follows by expanding the determinant multilinearly and collecting its factorial coefficients. Since A contains signed imaginary pairs, the summands do not have a common sign.

Put J=diag(1,-1,1,-1,...). Directly,


$$
A_n(-x)=(-1)^n J A_n(x)J.
$$


As n(n+1) is even, D_n is an even polynomial. The already frozen n=1 example is D_1(x)=x^2/2-1, so the deformation is not nonvanishing in an arbitrary positive sector.

## 2. A general binomial-minor ratio

For nonnegative a,b and L>=1 let


$$
T_L(a,b)=\bigl(\binom{a+b}{a+i-j}\bigr)_{i,j=0}^{L-1},
 \qquad \Delta_L(a,b)=\det T_L(a,b).
$$


The reviewed determinant formula gives


$$
\Delta_L(a,b)=\prod_{j=0}^{L-1}
 \frac{j!(a+b+j)!}{(a+j)!(b+j)!}>0.
$$



If the ordered column indices are kappa_j=j+lambda_(L-j), with lambda a partition of length at most L, define R_lambda(a,b,L) as the ratio of this selected-column determinant to Delta_L(a,b). Then


$$
\boxed{
 R_\lambda=
 \prod_{0\le i<j<L}\frac{\kappa_j-\kappa_i}{j-i}
 \prod_{j=0}^{L-1}
 \frac{(a+L-1-j)!(b+j)!}
      {(a+L-1-\kappa_j)!(b+\kappa_j)!}.}                  \tag{3}
$$


A negative factorial denominator gives zero. Equivalently,


$$
R_\lambda=s_\lambda(1^L)
 \prod_{(i,j)\in\lambda}
 \frac{a+i-j}{b+L-i+j}.                                  \tag{4}
$$


The first factor in (4) is simply the Vandermonde ratio in (3), so (3) can be used without Schur terminology.

For completeness, factor


$$
\frac{(a+b)!}{(a+L-1-\kappa)!(b+\kappa)!}
$$


from column kappa. Its remaining row-i entry is


$$
(a+L-1-\kappa)^{\underline{L-1-i}}
 (b+\kappa)^{\underline i},
$$


a polynomial in kappa of degree at most L-1. Its evaluation determinant is a constant times the Vandermonde of the column indices. Comparison with indices 0,...,L-1 proves (3) whenever all factored factorials are nonnegative. If kappa_(L-1)>a+L-1, that entire column of the original minor is zero; this agrees with the zero rising/falling product in (4). Thus the convention covers the out-of-support cases needed here.

The three ratios used below are


$$
R_{(1)}=\frac{La}{b+L},\quad
 R_{(2)}=\frac{L(L+1)a(a-1)}{2(b+L)(b+L+1)},
$$




$$
R_{(1,1)}=\frac{L(L-1)a(a+1)}
                  {2(b+L)(b+L-1)}.                     \tag{5}
$$


A partition whose length exceeds L is absent, rather than evaluated after a formal cancellation at an inadmissible L.

## 3. All odd deformation coefficients as signed parity minors

Set n=2m+1 and L=m+1. At x=0, after grouping even rows first and odd columns first, the two nonzero blocks are


$$
T_L(m,m+1),\qquad T_L(m+1,m).
$$


They have equal determinants by transposition. Therefore


$$
\boxed{D_n(0)=(-1)^L\Delta_L(m,m+1)^2\ne0.}             \tag{6}
$$



The identity a_k'=a_(k-1) implies the following exact differentiated-column expansion:


$$
D_n^{(r)}(0)=
 \sum_{\lambda\vdash r,\ \ell(\lambda)\le2L}
 f^\lambda\,
 \det\bigl(a_{n+i-\kappa_j}(0)\bigr)_{i,j=0}^{2L-1},
 \quad \kappa_j=j+\lambda_{2L-j}.                         \tag{7}
$$


It can be proved inductively: differentiation raises one column index by one. A collision with the next column gives a zero determinant. The surviving paths to a given partition are its standard tableaux, giving f^lambda. This proves the formula without an assumption on a Schur expansion.

A selected minor in (7) is zero unless the kappa indices contain exactly L even and L odd values. In the balanced case write its even indices as 2e_0<...<2e_(L-1) and odd indices as 2o_0+1<...<2o_(L-1)+1. They determine partitions beta and alpha respectively through e_j=j+beta_(L-j), o_j=j+alpha_(L-j). Both are genuine nonnegative partitions.

Let sigma_lambda be the sign of the permutation regrouping these columns into odd indices followed by even indices, divided by the corresponding sign for the original columns 0,...,2L-1. Then


$$
\boxed{\frac{D_n^{(r)}(0)}{D_n(0)}
 =\sum_{\lambda\vdash r\ {\rm balanced}}
 f^\lambda\sigma_\lambda
 R_\alpha(m,m+1,L)R_\beta(m+1,m,L).}                     \tag{8}
$$


In a balanced term, |alpha|+|beta|=r/2. This is also a direct parity proof that odd derivatives vanish.

Formula (8) is finite, exact, and retains the signs. Bounding its positive summands independently can lose the cancellations relevant to x=1. It is not a positivity formula.

## 4. Exact second and fourth coefficients

Write B_lambda=R_lambda(m,m+1,m+1) and C_lambda=R_lambda(m+1,m,m+1). For r=2, the two partitions give


$$
D_n''(0)/D_n(0)=B_{(1)}-C_{(1)}
 =\boxed{-\frac{3m+2}{2(2m+1)}}.                         \tag{9}
$$


Thus


$$
D_n(x)/D_n(0)=1-\frac{3m+2}{4(2m+1)}x^2+O(x^4).
$$


The O symbol here is only a Taylor notation, not a uniform remainder estimate at x=1.

For m>=1, the five partitions of four give respectively


$$
\begin{array}{c|c|c}
\lambda&f^\lambda&\text{normalized selected minor}\\
(4)&1&B_{(2)}\\
(3,1)&3&-C_{(2)}\\
(2,2)&2&B_{(1)}C_{(1)}\\
(2,1,1)&3&-B_{(1,1)}\\
(1,1,1,1)&1&C_{(1,1)}.
\end{array}
$$


Substitution into (5) and simplification gives


$$
\boxed{\frac{D_n^{(4)}(0)}{D_n(0)}
 =\frac{(m+3)(3m+2)}{4(2m+1)(2m+3)}}.                    \tag{10}
$$


For m=0 the forbidden partitions must be omitted; D_1 has degree two, so its fourth derivative is zero. Formula (10) is not claimed there.

The limits in (9),(10) are -3/4 and 3/16. In particular a Gaussian approximation inferred from only the quadratic coefficient is false: it would require the fourth derivative limit 27/16. The exact fourth logarithmic derivative is


$$
-\frac{(3m+2)(4m+3)(4m+5)}
        {4(2m+1)^2(2m+3)}\longrightarrow-\frac32.
$$


No limiting special function or zero distribution is inferred from these few coefficients.

A single exact Taylor-order-four check of the explicit n=3 deformation gives D_3(0)=36, D_3''(0)/D_3(0)=-5/6 and D_3^(4)(0)/D_3(0)=1/3. This checked the finite-order partition signs only; no actual HP system was solved and no degree/prime scan was performed.

## 5. Exact inverse-corner leading term

Let C_n(x) be the n-square corner minor of A_n(x), obtained by deleting row and column zero. Translation of indices makes it the Toeplitz determinant with indices 0,...,n-1 and the same offset n.

At x=0 the parity counts are unequal, so C_n(0)=0. On differentiation, only the last column survives without a duplicate. Its two parity blocks have sizes L and L-1. Their signs give


$$
C_n'(0)=(-1)^m
 \Delta_{m+1}(m,m+1)\Delta_m(m+1,m).
$$


Consequently


$$
\boxed{\frac{C_n'(0)}{D_n(0)}
 =-\frac{(2m+1)!(2m)!}{m!(3m+1)!}.}                     \tag{11}
$$



Keep the exact positive metric from the odd scalar theorem,


$$
c_m=(G^{-1})_{00}
 =\frac{((2m+1)!)^2}{m!(3m+2)!}.
$$


Where A_n(x) is invertible, define


$$
g_m(x)=\frac{(A_n(x)^{-1})_{00}}{c_m}.
$$


It is an odd holomorphic function near zero, and (11) gives


$$
\boxed{g_m(0)=0,\qquad
 g_m'(0)=-\frac{3m+2}{2m+1}\in[-2,-3/2).}               \tag{12}
$$


The actual scalar at x=1 is s_m=1/g_m(1), with exactly the normalization in raw_odd_dual_toeplitz_scalar_obstruction.md. At x=0 the full matrix is invertible but this inverse corner is zero. Therefore a full-determinant estimate alone does not control the scalar compression.

## 6. Uniform complex zero-free disk for the full determinant

Let Atilde_n(x)=G^(-1/2)A_n(x)G^(-1/2), with the same fixed positive G as above. At x=0 this is Hermitian. In the G-orthogonal subspaces


$$
P_\pm=\{(1\pm z)u(z^2):\deg u\le m\},
$$


its diagonal blocks are **exactly** +(1/2)I and -(1/2)I. This follows by pairing theta and theta+pi in the undeformed symbol; the corresponding quadratic forms are +/-I_(m+1)(u), whereas the G norm is 2I_(m+1)(u).

Thus in an orthonormal basis


$$
\widetilde A_n(0)=
 \begin{pmatrix}\tfrac12 I&X\\X^*&-\tfrac12 I\end{pmatrix},
 \quad
 \widetilde A_n(0)^2=
 \begin{pmatrix}\tfrac14I+XX^*&0\\0&\tfrac14I+X^*X\end{pmatrix}.
$$


In particular its inverse norm is at most two, uniformly in m.

The already proved positive-weight comparison, now applied to
|e^(xz)-1|<=e^|x|-1 on the unit circle, gives


$$
\|\widetilde A_n(x)-\widetilde A_n(0)\|
 \le\sqrt{5/4}(e^{|x|}-1).
$$


Hence


$$
\boxed{D_n(x)\ne0\quad\text{if}\quad
 |x|<\rho_0:=\log(1+1/\sqrt5).}                          \tag{13}
$$


More precisely, on |x|<=R<rho_0,


$$
\|\widetilde A_n(x)^{-1}\|
 \le \frac{2}{1-\sqrt5(e^R-1)}.                          \tag{14}
$$


This is a full complex-disk estimate, not a continuation inferred from real inequalities. Its radius is fixed and less than one, so it does not settle x=1 or provide the desired growing zero-free radius.

## 7. A uniform local bound for the normalized scalar

Take R=1/4. The elementary bound e^(1/4)<9/7 and sqrt5<9/4 makes the right side of (14) less than six. Therefore |g_m(x)|<=6 on |x|<=1/4 for every m.

The oddness of g_m and Cauchy's coefficient estimate imply


$$
|g_m(x)-g_m'(0)x|
 \le 6\frac{(|x|/R)^3}{1-(|x|/R)^2}.
$$


For |x|<=1/32, division by |x| bounds this remainder by 8/21. Combining with (12) proves


$$
\boxed{|x|\le|g_m(x)|\le(5/2)|x|,
 \qquad 0<|x|\le1/32,\quad m\ge0.}                      \tag{15}
$$


In particular the normalized high compression is invertible on this punctured disk: its determinant is the full determinant times the nonzero normalized inverse corner. Its Schur scalar s_m(x)=1/g_m(x) obeys


$$
\boxed{\frac{2}{5|x|}\le|s_m(x)|\le\frac1{|x|}.}         \tag{16}
$$


This is a genuine uniform quantitative scalar theorem for a restricted deformation range. It does not include the actual point x=1.

## 8. Exact remaining obstruction

The actual required estimate remains log|s_m(1)|=o(m). The new all-index dyadic theorem already excludes s_m(1)=0; it does not lower-bound its real absolute value.

The exact coefficient formula (8) supplies a concrete possible next step: control the signed parity-minor sum uniformly in both its partition size and m, or prove a continued nonzero inverse-corner bound from the local disk to x=1. The positive-alphabet Schur estimates in the archive do not do either. Absolute bounds on individual terms of (8) discard cancellations already essential in (9) and (10). The full determinant and the corner minor must both be controlled, since the corner vanishes at x=0 while the full determinant does not.

No asymptotic root claim, extension of (13) to a growing radius, or estimate at x=1 is asserted.
