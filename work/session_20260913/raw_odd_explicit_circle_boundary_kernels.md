> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Explicit circle kernels and finite boundary data for the odd rank-two reduction

Date: 2026-09-13. Original bounded continuation by audit_sources.
Independent review: PASS by audit_results; see raw_odd_circle_kernels_independent_review.md.

This continues the independently reviewed raw_odd_exact_two_mode_boundary_matrices.md. It gives the exact two boundary vectors, the rational base inverse, and the functionals entering its 2-by-2 and 3-by-3 determinants. The remaining exponential compression is retained explicitly. This is separate from the Cayley operator-limit argument in raw_odd_boundary_operator_limit.md.

All formulas hold for m>=0. No actual degree, root, prime or singular-value scan is used.

## 1. Ordinary circular binomial kernels

For integers a,M>=0 let P_M^(a) be the orthogonal projection onto polynomials of degree at most M in the scalar space with measure


$$
d\mu_a(t)=|1+t|^{2a}\frac{d\theta}{2\pi},\quad t=e^{i\theta}.
$$


Write K_M^(a)(t,zeta) for its reproducing kernel. Then


$$
\boxed{
 K_M^{(a)}(t,-1)=
 \sum_{j=0}^M(-1)^j
 \frac{(a+j)!(a+M-j)!}{(2a)!\,j!\,(M-j)!}t^j.}           \tag{1}
$$


In particular


$$
\boxed{
 H_M^{(a)}:=K_M^{(a)}(-1,-1)
 =\frac{(a!)^2(2a+M+1)!}
 {(2a)!(2a+1)!\,M!}.}                                   \tag{2}
$$



Here is a derivation. For a>=1, changing w to -t in the proved circular binomial polynomials gives


$$
\Phi_k^{(a)}(t)=
 \sum_{j=0}^k(-1)^{k-j}\binom kj
       \frac{(a)_{k-j}}{(a+j+1)_{k-j}}t^j,
 \quad
 h_k^{(a)}=\frac{k!(2a+k)!}{((a+k)!)^2},
$$




$$
\Phi_k^{(a)}(-1)=(-1)^k\frac{(2a+1)_k}{(a+1)_k}.
$$


Rising factorials are used in these expressions. Substituting into
sum_(k=0)^M Phi_k(t) conjugate(Phi_k(-1))/h_k and summing the coefficient of t^j by the binomial hockey-stick identity gives (1). For a=0 it is the ordinary Haar kernel sum_0^M(-t)^j, agreeing with the same factorial expression. Summing (1) at -1 by Vandermonde gives (2).

There is also the exact normalized beta-integral representation


$$
\frac{K_M^{(a)}(t,-1)}{H_M^{(a)}}
 =\frac1{B(a+1,a+1)}
   \int_0^1 x^a(1-x)^a[(1-x)-xt]^M\,dx.                 \tag{3}
$$


This follows by expanding the bracket and evaluating each elementary beta integral. It is not being used to assert positivity at a complex t.

## 2. The rational residual is a lower-weight endpoint kernel

Now use the rank-two space: a=m+1, scalar degree bound m. Put


$$
r(t)=\frac1{1+t},\quad h=(I-P_m^{(m+1)})r,\quad \rho=\|h\|_{\mu_{m+1}},
$$


and define


$$
H=H_{m+1}^{(m)},\quad
 R(t)=K_{m+1}^{(m)}(t,-1)/H.
$$


Then


$$
\boxed{h(t)=\frac{R(t)}{1+t},\qquad \rho^2=\frac1H.}       \tag{4}
$$


Indeed r-p has the form R_0/(1+t), where R_0 has degree at most m+1 and R_0(-1)=1. Minimizing its squared norm in mu_(m+1) is exactly minimizing ||R_0||^2 in mu_m subject to that endpoint constraint. The unique minimizer is the normalized reproducing kernel in (4), and its norm squared is 1/H. Equivalently, its orthogonality is against (1+t)P_m in the lower weight.

Let


$$
k(t)=K_m^{(m+1)}(t,-1),\quad
 \kappa=H_m^{(m+1)}.
$$


The actual evaluation map Lambda=rho(eval_-1,eval_-1) and its adjoint U therefore have the explicit form


$$
\Lambda(f_1,f_2)=\rho(f_1(-1),f_2(-1)),\quad
 U(c_1,c_2)=\rho k(t)(c_1,c_2).
$$


Their exact norm is


$$
\boxed{\|U\|^2=\|\Lambda\|^2
 =\rho^2\kappa
 =\frac{3(m+1)^2}{4(2m+1)(2m+3)}
 \le\frac14.}                                           \tag{5}
$$


It tends to 3/16. This sharpens the earlier valid but larger bound 5/4.

For later formulas, (1) gives


$$
k(0)=\frac12,\quad
 R(0)=\frac{2m+1}{(m+1)H}>0,\quad
 [t^{m+1}]R=(-1)^{m+1}R(0).                              \tag{6}
$$


The first equality also holds at m=0.

## 3. Exact rational base inverses: no hidden linear system

On the scalar polynomial space set


$$
S=P_m^{(m+1)}rP_m^{(m+1)},\qquad K=I-S.
$$


These are the lower-left and upper-right blocks of A0 respectively. Polynomial division and (4) give


$$
\boxed{Sf=\frac{f-f(-1)R}{1+t},\qquad
 Kf=\frac{tf+f(-1)R}{1+t}.}                              \tag{7}
$$


If g has degree at most m, write g_m=[t^m]g. Then


$$
\boxed{
 S^{-1}g=(1+t)g-\frac{g_m}{R_{m+1}}R,\qquad
 K^{-1}g=\frac{(1+t)g-(g(0)/R(0))R}{t}.}                 \tag{8}
$$


The first expression has its degree-(m+1) coefficient canceled. The second has its constant coefficient canceled before division by t. In each case the result has degree at most m; evaluating at -1 and substituting into (7) verifies the inverse. Both denominators in (8) are nonzero by (6).

Consequently


$$
A_0^{-1}=\begin{pmatrix}0&S^{-1}\\K^{-1}&0\end{pmatrix}
$$


is fully explicit in the polynomial basis. These formulas agree with the previously proved uniform norm bound ||A0^-1||<=2; their potentially large ordinary coefficients must not be mistaken for a large weighted operator norm.

## 4. The actual endpoint vector, kept distinct from evaluation at -1

The vector v in the odd Schur complement represents the original coefficient at z^0. In the two-parity polynomial model it is


$$
v(t)=\bigl(K_m^{(m+1)}(t,0)/\sqrt{c_m},\,0\bigr),
 \quad c_m=K_m^{(m+1)}(0,0)
 =\frac{((2m+1)!)^2}{m!(3m+2)!}.
$$


Reversed orthogonality gives


$$
K_m^{(m+1)}(t,0)=\Phi_m^{(m+1),*}(t)/h_m^{(m+1)}.
$$


Thus with F=Phi_m^(m+1),*,


$$
\boxed{v(t)=(\sqrt{c_m}F(t),0),\quad \|v\|=1.}           \tag{9}
$$


For any polynomial pair f,


$$
\langle v,f\rangle=f_1(0)/\sqrt{c_m}.
$$


In particular v has not been replaced by the boundary endpoint kernel k at -1.

The three required base inputs are now explicit:


$$
b_1=(0,K^{-1}(\rho k)),\quad
 b_2=(S^{-1}(\rho k),0),\quad
 b_v=(0,K^{-1}(\sqrt{c_m}F)).                             \tag{10}
$$


They equal A0^-1Ue_1, A0^-1Ue_2 and A0^-1v. Their weighted norms are at most one, one and two respectively, by (5) and the base inverse bound.

## 5. The residual functional is a finite band of leading coefficients

Normalize the rational residual by


$$
\widehat h=h/\rho
 =\frac{K_{m+1}^{(m)}(t,-1)}{(1+t)\sqrt H}.
$$


For an analytic function g in a neighborhood of the closed disk, define


$$
\mathcal L_m(g)=\langle\widehat h,g\rangle_{\mu_{m+1}}.
$$


It has the exact lower-weight projection expression


$$
\boxed{
 \mathcal L_m(g)
 =\frac{[P_{m+1}^{(m)}((1+t)g)](-1)}{\sqrt H}.}           \tag{11}
$$


This follows by canceling one factor 1+bar(t) from the measure. It vanishes for every g of degree at most m.

There is a stronger finite-coefficient formula. Set


$$
L_v=\frac{2m+1}{m+1}\binom mv
       \frac{(3m+2)_{\underline v}}{(2m+1)_{\underline v}},
 \quad 0\le v\le m,
$$


with falling factorials. Then


$$
\boxed{
 \mathcal L_m(g)=\frac{(-1)^{m+1}}{\sqrt H}
 \sum_{v=0}^{m}L_v\,[t^{2m+1-v}]g.}                     \tag{12}
$$


Thus only coefficients of degrees m+1,...,2m+1 enter, exactly. There is no approximation of an infinite series in (12).

Here are details fixing the sign and the central zero block. Let Klow=K_(m+1)^(m)(t,-1) and


$$
\mathscr P(t)=(1+t)^{2m+1}Klow(t).
$$


Its kernel coefficients directly satisfy


$$
t(1+t)Klow''+[t-(2m+1)]Klow'-(m+1)^2Klow=0.
$$


Conjugating by (1+t)^(2m+1) gives


$$
t(1+t)\mathscr P''-[(2m+1)+(4m+1)t]\mathscr P'
                  +m(3m+2)\mathscr P=0.
$$


The coefficient recurrence is


$$
v(2m+2-v)\mathscr P_v
 =(m+1-v)(3m+3-v)\mathscr P_{v-1}.
$$


Since P_0=(2m+1)/(m+1), this proves P_v=L_v for 0<=v<=m, and P_v=0 for m+1<=v<=2m+1. The recurrence becomes resonant only at v=2m+2; no division there is made.

The symmetry of (1) gives


$$
\overline{Klow(t)}=(-1)^{m+1}t^{-(m+1)}Klow(t)
 \quad(|t|=1).
$$


Using mu_m=t^-m(1+t)^(2m)dtheta/(2pi) in (11), constant-term extraction selects P_(2m+1-k) from a monomial t^k. The central zero block eliminates k<=m; negative coefficient indices eliminate k>2m+1. This proves (12), including its sign. All assertions also hold at m=0, where Klow=1-t and P=1-t^2.

The coefficients L_v are positive, but this does not imply a sign for L_m(Ef) because f is not known to have coefficients of one sign.

## 6. Explicit entries of the two boundary determinants

Retain


$$
E(t)=\begin{pmatrix}c(t)&ts(t)\\s(t)&c(t)\end{pmatrix},
 \qquad E_0=P_m E P_m.
$$


Its inverse is uniformly bounded by e/cos(1). This is the one remaining finite polynomial operator in the formulas; it is not set equal to the exponential of a compressed shift.

Solve the three well-conditioned equations


$$
f_1=E_0^{-1}b_1,\quad f_2=E_0^{-1}b_2,\quad
 f_v=E_0^{-1}b_v,                                       \tag{13}
$$


where the right sides are the explicit polynomials (10). The ordinary binomial reproducing kernels give E0 itself as a finite projection integral if desired.

Define the two-component functional


$$
\mathfrak b(f)=J_0^*
 \begin{pmatrix}\mathcal L_m((Ef)_1)\\
                 \mathcal L_m((Ef)_2)\end{pmatrix},
 \quad J_0=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
$$


Every L_m entry can be evaluated by the finite band (12). The actual boundary matrices from the rank-two theorem are exactly


$$
\boxed{
 D_2=I_2+\bigl[\mathfrak b(f_1)\ \mathfrak b(f_2)\bigr],}
$$




$$
\boxed{
 D_3=\begin{pmatrix}
 D_2&\mathfrak b(f_v)\\
 (f_{1,1}(0),f_{2,1}(0))/\sqrt{c_m}
                    &f_{v,1}(0)/\sqrt{c_m}
 \end{pmatrix}.}                                       \tag{14}
$$


The bottom row in the block display has its first two entries under D2 and its last entry under the final column. Formula (14) preserves exactly the signs and normalization of s_m=det D2/det D3.

Thus both rational boundary inputs and all boundary testing functionals are explicit. This is more than a count of two exceptional modes. The remaining difficulty is the asymptotic action of E0^-1 on these inputs and, ultimately, lower bounds or nonzero limits for the small determinants.

## 7. Exact localization of the base kernel vectors near the top degree

Let phi_k^(a)=Phi_k^(a)/sqrt(h_k^(a)). The unit endpoint kernel


$$
e_M^{(a)}=K_M^(a)(t,-1)/\sqrt{H_M^(a)}
$$


has squared norm in degrees <=M-r exactly


$$
\boxed{
 \|\operatorname{Proj}_{\le M-r}e_M^{(a)}\|^2
 =\frac{H_{M-r}^{(a)}}{H_M^{(a)}}
 =\prod_{j=0}^{r-1}\frac{M-j}{2a+M+1-j}.}                \tag{15}
$$


For the upper kernel (a,M)=(m+1,m), this is at most 3^-r. For the lower kernel (a,M)=(m,m+1), it is at most 2^-r. Both bounds are uniform in their permitted ranges 0<=r<=M.

After reversing the orthonormal coefficient order and multiplying by (-1)^M, both endpoint-kernel profiles converge in l2 to


$$
\boxed{\xi_r=(-1)^r\sqrt{2/3}\,3^{-r/2},\quad r\ge0.}    \tag{16}
$$


For each fixed r this follows from (1),(2) and the norm formula: the top squared coefficient is (2a+1)/(2a+M+1), and each fixed step backward has asymptotic squared ratio 1/3. The uniform geometric tails in (15) justify l2 convergence, not merely coordinatewise convergence.

The actual origin-coordinate vector v has a different profile in this circular basis. Its squared tail is


$$
\frac{K_{m-r}^{(m+1)}(0,0)}{K_m^{(m+1)}(0,0)}
 =\frac{h_m^{(m+1)}}{h_{m-r}^{(m+1)}}
 \le(3/4)^r.
$$


Its reversed, phase-adjusted profile converges in l2 to


$$
\boxed{\zeta_r=\tfrac12(-\sqrt3/2)^r,\quad r\ge0.}        \tag{17}
$$


The top squared coefficient tends to 1/4 and the successive squared tail ratio tends to 3/4. These profiles are expressed in different circular orthonormal bases as m changes; they are coefficient-profile limits. No convergence of multiplication operators or of E0^-1 is inferred from them alone.

## 8. Scope and next step

The note supplies exact finite kernels, exact residual normalization, explicit rational base inverse formulas, a finite leading-coefficient functional, and uniformly localized boundary input profiles. These are actual m-dependent objects from the rank-two factorization.

The small determinants are still not proved bounded away from zero. The separate Cayley operator-limit route must justify any replacement of E0^-1 and the projections by limiting operators. Even convergence of D2,D3 would require checking the limiting determinants are nonzero before implying log|s_m|=o(m).
