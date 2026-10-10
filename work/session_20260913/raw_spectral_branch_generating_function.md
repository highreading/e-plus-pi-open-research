> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Spectral branch generating functions from one second-order equation

Date: 2026-09-13. Original continuation by audit_results.

This note gives an exact generating function for both polynomial
branches in the positive two-measure representation. After explicit
row normalization, the branches have rational polynomial coefficients
in the spectral parameter. Their generating functions are fixed Abel
averages of two solutions of one second-order differential equation.
The formulas are analytic for |z|<1 and every complex spectral parameter.
A uniform individual-coefficient bound is proved below; no nullspace
concentration or inverse-minor bound is inferred from it.

## 1. Normalization and the reflection convention

Let p_k^(sigma) be the branches of the symmetric row normalization E_k
in raw_positive_two_measure_reduction.md. Define rationally normalized
branches



$$
r_k^{(0)}(\xi)=\frac{p_k^{(0)}(\xi)}{\sqrt{2k+1}},
\qquad
r_k^{(1)}(\xi)=\frac{\sqrt3\,p_k^{(1)}(\xi)}{\sqrt{2k+1}}.
\tag{1}
$$



Indeed E_k=c_k sqrt(2k+1)F_k with c_k=2^(-k)binom(2k,k).
The even seed is1 and the odd seed is sqrt3(x-1/2), so (1) removes
both the varying row radical and the fixed odd seed factor. The
initial values are



$$
(r_0^{(0)},r_1^{(0)})=(1,1/2),\qquad
(r_0^{(1)},r_1^{(1)})=(0,1).
$$



All moment formulas here use the plus convention: the original
polynomial U_n(x)=sum_j B_j(1-x)^(n-j)/(n-j)! annihilates F_k(x).
For the reflected polynomial P_n(t)=U_n(1-t), the same high equations
contain a minus sign in the odd spectral branch. Reflection does not
change the branch definitions or the generating identities below.

## 2. The second-order equation and exact generating formula

For sigma=0,1, let V_sigma(w;xi) be the solution of



$$
\boxed{
(1+w^2)V''-(w-1)^2V'+(1-w-\xi)V=0,}
\tag{2}
$$



with respective initial data



$$
(V_0(0),V_0'(0))=(1,1/2),\qquad
(V_1(0),V_1'(0))=(0,1).
\tag{3}
$$



Continue these solutions from0 into the slit plane



$$
\Omega=\mathbb C\setminus
\bigl(i[1,\infty)\cup-i[1,\infty)\bigr).
$$



This domain is simply connected, and the coefficients of the normalized
equation have no singularities there. The solutions are analytic in w
on Omega and entire in xi, locally uniformly in both variables.

Put eta=z/(1-z²). Then the exact identities are



$$
\boxed{
\mathcal P_\sigma(z;\xi):=\sum_{k\ge0}r_k^{(\sigma)}(\xi)z^k
=\frac1{\pi\sqrt{1-z^2}}
\int_0^\pi V_\sigma\bigl(\eta(1+\cos\theta);\xi\bigr)d\theta.}
\tag{4}
$$



The square root is the branch equal to1 at0. Equivalently, writing



$$
\mathcal A_\sigma(\eta;\xi)
=\frac1\pi\int_0^2
\frac{V_\sigma(\eta s;\xi)}{\sqrt{s(2-s)}}ds,
\tag{5}
$$



one has P_sigma(z;xi)=(1-z²)^(-1/2) A_sigma(z/(1-z²);xi).
The averaging kernel in (5) is fixed and positive on (0,2).
This does not assert positivity of its complex-parameter integrand
or of any growing moment determinant.

## 3. Derivation at the actual spectral points

The existing, independently derived Borel–Legendre generating function is



$$
\sum_{k\ge0}c_kF_k(x)z^k
=\frac1{\sqrt{1-z^2}}e^{x\eta}I_0(x\eta)
=\frac1{\pi\sqrt{1-z^2}}
\int_0^\pi e^{x\eta(1+\cos\theta)}d\theta.
\tag{6}
$$



It converges uniformly for x in [0,1] and z in every compact subset
of the unit disk. Projection onto a fixed psi_l is therefore valid.

Use the normalized prolate eigenfunction
y_l(u)=psi_l((u+1)/2)/sqrt2 from the reviewed finite-Fourier identity.
At c=1/2 that identity and its entire continuation give



$$
\int_0^1 e^{wx}\psi_l(x)dx
=\frac{\mu_l}{\sqrt2}e^{w/2}y_l(-iw).
\tag{7}
$$



For even l, divide by the nonzero amplitude
g_l=mu_l y_l(0)/sqrt2. For odd l, divide by
g_l=sqrt3 mu_l y_l'(0)/(sqrt2 i). Thus the projected Laplace transforms
are respectively V_0(w;xi_l) and V_1(w;xi_l)/sqrt3, where



$$
V_0=e^{w/2}\frac{y_l(-iw)}{y_l(0)},\qquad
V_1=i e^{w/2}\frac{y_l(-iw)}{y_l'(0)}.
\tag{8}
$$



The prolate equation is



$$
(1-u^2)y''-2uy'+(\xi_l-3/4-u^2/4)y=0.
$$



Substitute u=-iw and then multiply by e^(w/2). Direct differentiation
gives exactly (2) and the initial values(3). The two distinct parity
normalizations in (8) are the reason for the sqrt3 factor in (1).

Projecting (6) and using E_k=c_k sqrt(2k+1)F_k now proves (4) at
xi=xi_l of the corresponding parity. All interchanges here are on
compact z sets and a finite x interval, for a fixed eigenfunction;
no growing-l or growing-k estimate is hidden in this step.

## 4. Extension to every parameter and the full unit disk

The normalized equation(2) determines a convergent series
V_sigma(w;xi)=sum_(j>=0)v_j^(sigma)(xi)w^j near0. Its exact recurrence is



$$
\boxed{
(j+2)(j+1)v_{j+2}
=(j+1)v_{j+1}+[\xi-j(j+1)-1]v_j+jv_{j-1},}
\tag{9}
$$



where v_-1=0 and the two initial pairs are (3). Every coefficient
is a rational polynomial in xi. Induction gives degree at most
floor(j/2) in the even branch and floor((j-1)/2) in the odd branch.

The j-th moment of the averaging kernel in(5) is



$$
\frac1\pi\int_0^\pi(1+\cos\theta)^j d\theta
=2^{-j}\binom{2j}{j}=c_j.
\tag{10}
$$



Consequently each coefficient of the right side of(4) is again a
polynomial in xi with the same branch degree cap. The equality with
the independently defined r_k holds at the infinitely many distinct
xi_l of its parity. A polynomial with these infinitely many zeros
is identically zero. This proves coefficientwise equality for every
complex xi, without an accumulation-point assumption for the spectrum.

To justify the analytic domain claimed in(4), suppose |z|<1 and
eta=z/(1-z²). A useful identity is



$$
\operatorname{Re}\eta
=\frac{(1-|z|^2)\operatorname{Re}z}{|1-z^2|^2}.
$$



Thus eta can be purely imaginary only when z=iy with |y|<1; in that
case |eta|=|y|/(1+y²)<1/2. For every s in[0,2], the point s eta
therefore avoids both slit rays of Omega. For a compact subset of
the disk the whole image, including all such s, is a compact subset
of Omega. The integral in(4) is holomorphic in z and entire in xi,
locally uniformly. Its Taylor series thus converges throughout
|z|<1, establishing the asserted analytic identity there.

At an actual eigenvalue the solution of matching reflection parity
in(8) has an entire continuation. This makes no assertion about the
opposite-parity solution at that same eigenvalue. For arbitrary xi
the slit-plane specification is retained; it would be incorrect to
assume an entire continuation for both normalized solutions at every
parameter.

## 5. A scalar equation for the Abel transform itself

Let theta=eta d/deta and A=A_sigma. Applying(10) to(9) gives the
fourth-order scalar equation



$$
\boxed{\begin{aligned}
0={}&\bigl[\theta^2(\theta-1)^2
-\eta\theta^2(2\theta+1)\\
&+\eta^2(2\theta+1)(2\theta+3)
       (\theta^2+\theta+1-\xi)\\
&-\eta^3(2\theta+1)(2\theta+3)(2\theta+5)\bigr]A.
\end{aligned}}
\tag{11}
$$



Each displayed power of eta multiplies on the left; all theta factors
within that term act first. This ordering is part of the formula.

For an explicit coefficient check, write A=sum a_j eta^j, a_j=c_jv_j.
Since c_(j+1)/c_j=(2j+1)/(j+1), equation(9) becomes



$$
\begin{aligned}
0={}&(j+2)^2(j+1)^2a_{j+2}
-(j+1)^2(2j+3)a_{j+1}\\
&+(j^2+j+1-\xi)(2j+3)(2j+1)a_j\\
&-(2j+3)(2j+1)(2j-1)a_{j-1}.
\end{aligned}
\tag{12}
$$



Summing this recurrence proves(11). Its analytic solutions with the
chosen a_0,a_1 are the Abel averages in(5). The second-order equation
applies directly to V; no order-two equation for A or P_sigma is
claimed merely from the existence of this transform.

## 6. A uniform individual-branch upper bound

Fix any 0<rho<1 and set



$$
W_\rho=\frac{2\rho}{1-\rho^2},\qquad
\delta_\rho=\frac{(1-\rho)^4}{(1+\rho^2)^2},\qquad
C_\rho=W_\rho\left(1+\frac{(W_\rho+1)^2}{\delta_\rho}\right).
$$



Then for every k>=0, every complex xi and either branch,



$$
\boxed{
|r_k^{(\sigma)}(\xi)|
\le\frac{3}{2\sqrt{1-\rho^2}}\,
\rho^{-k}\exp\!\left(C_\rho\sqrt{1+|\xi|}\right).}
\tag{13}
$$



Here is a direct proof with no asymptotic spectral assumption. For
|z|<=rho and 0<=s<=2, w=s z/(1-z²) has |w|<=W_rho and



$$
1+w^2=\frac{(1-z^2+isz)(1-z^2-isz)}{(1-z^2)^2}.
$$



For each real s in[0,2], both roots of each quadratic numerator
factor lie on the unit circle, including the double-root endpoint
s=2. Therefore |1+w²|>=delta_rho. The same bound holds on the
straight segment from0 to w by replacing s with a smaller value.

Write (2) as V''=a(w)V'+b(w)V. Along these segments,



$$
|a|\le\frac{(W_\rho+1)^2}{\delta_\rho},\qquad
|b|\le\frac{|\xi|+W_\rho+1}{\delta_\rho}.
$$



Put h=sqrt(1+|xi|) and use the scaled two-component state (V,V'/h).
The induced l1 matrix norm for its first-order equation is at most



$$
h\left(1+\frac{(W_\rho+1)^2}{\delta_\rho}\right).
$$



The initial state norm is at most3/2 for either solution. Integration
along a segment of length at most W_rho and the elementary Gronwall
bound give |V|<=(3/2)exp(C_rho h). Applying(4), bounding its square-root
prefactor by(1-rho²)^(-1/2), and using Cauchy's coefficient estimate
proves(13).

In particular, if |xi|<=C(k+1)^2 with fixed C, each normalized branch
value is bounded by exp(O(k)), with constants depending on C and rho.
This is a genuine growing-index statement about individual entries.
It neither lower-bounds a mixed determinant nor controls its inverse;
those could still lose much more through cancellation.

## 7. Checks and remaining task

The closed symbolic check uses coefficients0 through6, with xi left
symbolic. It compares the generating formula to the independently
derived five-diagonal row recurrence, verifies(2) and(11), and constructs
no canonical HP triple or new spectral eigenvalue. All checks pass in
raw_spectral_branch_generating_function_checks.json.

For orientation the first coefficients are

    r^(0): 1, 1/2, (6xi+1)/8, 5xi/8+1/3, ...;
    r^(1): 0, 1, 3/4, (5xi+8)/12, ... .

The constructive next question is a uniform interpolation estimate
for these two coupled branches at the actual prolate nodes with the
actual positive weights. Formula(4) retains all cancellations before
absolute values are taken; equation(13) supplies only the individual
upper-bound side of such an estimate. Neither the analytic generating
formula nor its finite checks prove top-two concentration.
