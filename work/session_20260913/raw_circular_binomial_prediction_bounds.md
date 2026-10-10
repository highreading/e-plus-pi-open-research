> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Circular binomial prediction at a growing gap

Date: 2026-09-13. Original bounded continuation by audit_sources.
Independent review: PASS by audit_computations; see raw_circular_prediction_independent_review.md.

This note treats only the positive base circular weight in raw_joint_dual_hankel_and_even_root_product.md. It does not transfer these estimates to the complex weight e^z; that comparison is a separate task. The inspected project material contains the binomial Toeplitz determinant and its inverse corner, but not the growing-gap prediction bound below. No new actual Hermite–Pade degree or prime scan is used, and no external theorem is needed.

Let n=2m>=2 and equip Laurent polynomials on the unit circle with


$$
\|f\|_{G_0}^2=\int_0^{2\pi}|f(e^{i\theta})|^2
 |1+e^{2i\theta}|^{2m}\,\frac{d\theta}{2\pi}.
$$


For any integer r>=0, define the **squared** prediction distance


$$
D_{m,r}=\operatorname{dist}_{G_0}^2
 \bigl(z^{-r},\operatorname{span}\{z,z^2,\ldots,z^{2m}\}\bigr).
$$


The base inverse corner and its reciprocal are


$$
c_m=\frac{((2m)!)^2}{m!(3m)!},\qquad
 H_m=\frac1{c_m}=\frac{m!(3m)!}{((2m)!)^2}.
$$



The principal bound, with s=floor(r/2), is


$$
\boxed{D_{m,2s}=D_{m,2s+1},\qquad
 \frac{D_{m,r}}{H_m}\le\binom{m+s}{s}^2.}                 \tag{1}
$$


It holds for every s>=0. For the range 0<=r<=n+1, hence s<=m, it implies


$$
\boxed{\frac{D_{m,r}}{H_m}\le
 \frac{n^{2\lfloor r/2\rfloor}}{(\lfloor r/2\rfloor!)^2}.} \tag{2}
$$


The baseline is exact: D_(m,0)=D_(m,1)=H_m. All constants are uniform in m and r in the displayed ranges.

## 1. Exact parity reduction

The circular weight is invariant under z -> -z, so its even and odd Laurent subspaces are orthogonal. A predictor of the wrong parity can only increase the squared error and is absent from the minimizing predictor.

Put w=-z^2. Pushing Haar measure forward under this map gives Haar measure once again, and the weight becomes |1-w|^(2m). For r=2s, only the even predictor powers z^2,...,z^(2m) matter. Multiplication by the unit-modulus monomial w^s converts the target and predictor to


$$
1,\quad \operatorname{span}\{w^{s+1},\ldots,w^{s+m}\}.
$$


Signs in w=-z^2 merely change predictor coefficients.

For r=2s+1, factor out the common unit-modulus z^-1. The odd predictor powers z,z^3,...,z^(2m-1) then become the same w,w^2,...,w^m. Multiplication by w^s again gives exactly the preceding problem. Thus both squared distances equal


$$
d_{m,s}=\operatorname{dist}_{|1-w|^{2m}}^2
 \bigl(1,\operatorname{span}\{w^{s+1},\ldots,w^{s+m}\}\bigr).
                                                               \tag{3}
$$


There are m predictor powers in each parity. In particular r=1 has no new loss relative to r=0.

## 2. Explicit circular binomial orthogonal polynomials

Keep m fixed. The moments for the positive measure |1-w|^(2m)dtheta/(2pi) are


$$
\mu_\ell=(-1)^\ell\binom{2m}{m+\ell},
$$


where out-of-range binomial coefficients are zero.

For every k>=0 the monic orthogonal polynomial is


$$
\boxed{\Phi_k(w)=
 \sum_{j=0}^k
 \binom{k}{j}\frac{(m)_{k-j}}{(m+j+1)_{k-j}}w^j.}          \tag{4}
$$


Parenthesized subscripts here denote rising factorials. In particular Phi_0=1 and Phi_1=w+m/(m+1).

Here is an elementary orthogonality proof, including the zeros outside the moment support. For k>=1 and 0<=ell<k, multiplication of the coefficient in (4) by mu_(j-ell) gives a fixed nonzero factor times


$$
(-1)^j\binom{k}{j}
 (m+k-j-1)^{\underline{k-\ell-1}}
 (m+j)^{\underline{\ell}}.                                \tag{5}
$$


The factor independent of j is


$$
(-1)^{-\ell}\frac{(2m)!}{(m-1)!(m+k)!}.
$$


The product of falling factorials in (5) is a polynomial in j of degree k-1. Its kth alternating finite difference is zero. If m+j-ell or m-j+ell is negative, the corresponding falling factorial has a zero factor, agreeing exactly with the vanishing out-of-range moment. Thus the same finite-difference proof covers all j, including k>m. This establishes orthogonality to 1,w,...,w^(k-1), with leading coefficient one.

The binomial Toeplitz determinant identity already proved in the joint note, or its same row-factor proof, gives the exact norm


$$
h_k=\|\Phi_k\|^2=\frac{k!(2m+k)!}{((m+k)!)^2}.             \tag{6}
$$


Indeed this is the quotient of the Gram determinant of size k+1 by that of size k. The signs in the moments are removed by conjugating the matrix by diag(1,-1,1,-1,...), so they do not change its determinant.

The reversed polynomial has the explicit coefficients


$$
\Phi_k^*(w)=w^k\overline{\Phi_k(1/\bar w)}
 =\sum_{j=0}^k
 \binom{k}{j}\frac{(m)_j}{(m+k-j+1)_j}w^j.                 \tag{7}
$$


Its constant coefficient is one. As a supplementary exact check, these polynomials obey


$$
\Phi_{k+1}=w\Phi_k+\frac{m}{m+k+1}\Phi_k^*.
$$


This recurrence follows coefficientwise from (4); it is not being used to assume the measure or its orthogonality.

## 3. Root location and the base prediction error

All roots of Phi_k lie strictly inside the unit disk. This usual extremal fact has a short proof here. A monic orthogonal polynomial uniquely minimizes its norm among monic polynomials of its degree. A root a with |a|>1 could be replaced by 1/bar(a), decreasing the norm by the strict factor 1/|a| on the unit circle. This is impossible. If |a|=1, write Phi_k=(w-a)Q. Orthogonality to Q gives


$$
a=\frac{\int w|Q|^2|1-w|^{2m}\,d\theta}
          {\int |Q|^2|1-w|^{2m}\,d\theta}.
$$


The modulus of this weighted average is strictly less than one, because the weight is positive almost everywhere and Q is nonzero. This is also impossible.

Consequently F=Phi_m^* has constant one, degree m, and no roots in the closed unit disk. Reversal of the orthogonality relations shows


$$
F\perp w,w^2,\ldots,w^m.
$$


Since 1-F belongs to this predictor span, F is the exact base residual. Its norm is


$$
\|F\|^2=h_m=H_m.
$$


This independently identifies the baseline 1/c_m with a squared distance, rather than a norm.

## 4. An explicit residual at every gap

Write the formal reciprocal


$$
\frac1{F(w)}=\sum_{j\ge0}b_jw^j,\quad b_0=1,
$$


and let B_s(w)=sum_(j=0)^s b_jw^j. Define


$$
R_s(w)=F(w)B_s(w).                                       \tag{8}
$$


It has constant one, all coefficients at degrees 1,...,s vanish, and its degree is at most m+s. Thus 1-R_s belongs to span{w^(s+1),...,w^(s+m)}, making R_s an admissible residual for (3). It need not be the minimizing residual when s>0.

If a_1,...,a_m are the roots of Phi_m with multiplicity, then


$$
F(w)=\prod_{\nu=1}^m(1-\overline{a_\nu}w),\qquad |a_\nu|<1.
$$


Expansion of these geometric series yields


$$
|b_j|\le\binom{m+j-1}{j}.                                \tag{9}
$$


There are exactly binom(m+j-1,j) weak compositions of j into m nonnegative parts, and each corresponding product has modulus at most one. No sign property of the reciprocal coefficients is assumed.

On the unit circle,


$$
|B_s(w)|\le\sum_{j=0}^s|b_j|
 \le\sum_{j=0}^s\binom{m+j-1}{j}
 =\binom{m+s}{s}.
$$


Therefore


$$
d_{m,s}\le\|R_s\|^2
 \le \binom{m+s}{s}^2\|F\|^2,
$$


which proves (1). If s<=m, each of m+1,...,m+s is at most 2m=n, proving (2). This proof is uniform for a growing s and has no hidden fixed-gap constant.

The exact first optimal coefficients can also be computed from the finite Schur complement


$$
d_{m,s}=\mu_0-v_s^*T_m^{-1}v_s,\quad
 T_m=(\mu_{i-j})_{i,j=1}^m,\quad
 (v_s)_i=\mu_{s+i}.                                      \tag{10}
$$


The matrix T_m is positive definite. For s>=m every v_s entry is zero, and d_(m,s)=mu_0=binom(2m,m). Formula (1) still holds; the simpler factorial estimate (2) is claimed only in its stated range.

## 5. Uniform summability after the original factorial weight

For 0<=r<=n+1, put s=floor(r/2). Since


$$
\frac{n!}{(n+r)!}\le n^{-r},
$$


equation (2) gives


$$
\boxed{
 \frac{n!}{(n+r)!}\frac{D_{m,r}}{H_m}
 \le
 \begin{cases}
  1/(s!)^2,&r=2s,\\
  1/[n(s!)^2],&r=2s+1.
 \end{cases}}                                           \tag{11}
$$


In particular the sum over the actual finite degree range 0<=r<=n is bounded by e(1+1/n), independently of n. For any complex x, the corresponding absolute weighted sum is at most


$$
\sum_{r=0}^n\frac{n!}{(n+r)!}
 \frac{D_{m,r}}{H_m}|x|^r
 \le (1+|x|/n)\sum_{s\ge0}\frac{|x|^{2s}}{(s!)^2}
 \le (1+|x|/n)e^{2|x|}.                                  \tag{12}
$$


The final inequality follows by retaining the equal-index terms in
(exp|x|)^2, whose terms are nonnegative.

If an application needs norms rather than squared distances, taking square roots before applying the factorial weight is stronger:


$$
\frac{n!}{(n+r)!}\sqrt{\frac{D_{m,r}}{H_m}}
 \le \frac{n^{-\lceil r/2\rceil}}{(\lfloor r/2\rfloor)!}.
                                                               \tag{13}
$$


Consequently


$$
\sum_{r=0}^n\frac{n!}{(n+r)!}
 \sqrt{\frac{D_{m,r}}{H_m}}|x|^r
 \le (1+|x|/n)\exp(|x|^2/n).                              \tag{14}
$$


This last bound is especially useful if the actual coefficient comparison is a Cauchy–Schwarz norm estimate. Whether it applies to a given normalized actual coefficient is a separate bridge; none is asserted here.

## 6. Scope of the result

The predictions are for the positive base circular weight, for all m>=1 and a gap r growing with m. Both parities have been retained exactly. The all-gap binomial bound (1), and the factorially weighted bounds (11)–(14) in the actual finite range, are proved without numerical evidence.

The residual construction supplies an upper distance bound, not an exact general inverse-corner formula. The complex e^z perturbation, actual V coefficients, endpoint denominators and irrationality estimates require their own separately verified identities. In particular no inference from base positivity to positivity of the perturbed coefficients is made.
