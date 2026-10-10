> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Positive spectral tail for the Borel kernel

Date: 2026-09-13. Root's convergence proof supporting the quantitative
raw-remainder continuation. All objects are those of
`raw_arctan_positive_kernel_attempt.md`.

Let Q_k be the raw monic Legendre polynomials,
h_k=L(Q_k^2), v_k=L(Q_k/(1-t)), and F_k=Borel(Q_k). Put
alpha=(1+sqrt(2))/2 and eta=sqrt(2)-1=1/(2alpha).
The exact positive tail identity is



$$
\boxed{G_N(x)=\sum_{k>N}\frac{v_k}{h_k}F_k(x),}\tag{1}
$$



with uniform absolute convergence on every compact subset of the entire
complex x-plane. In particular its summands are nonnegative on [0,1].
The convergence statement is stronger than an unproved termwise Borel
transformation of an asymptotic series.

## 1. Elementary weight bounds

The square orthogonality identity gives



$$
v_k=Q_k(1)^{-1}L\left(\frac{Q_k(t)^2}{1-t}\right).
$$



Since Q_k(iu)^2 has constant sign (-1)^k times a real square, taking real
parts shows



$$
0<\frac{v_k}{h_k}\le\frac1{Q_k(1)}.\tag{2}
$$



The ratio of the integrals on the right is a weighted mean of
1/(1+u^2), which lies between1/2 and1. Both h_k and v_k have the same
sign, so dividing them introduces no reversed inequality.

The positive recurrence Q_(k+1)(1)=Q_k(1)+beta_k Q_(k-1)(1),
beta_k>=1/4, proves Q_k(1)>=alpha^(k-1) for k>=1 by induction;
Q_0=Q_1(1)=1 starts it because alpha=1+1/(4alpha).

Let sigma be k modulo2, and let q_(k,sigma) be the lowest nonzero
coefficient of Q_k. For even k,



$$
q_{k,0}=\frac{\binom{k}{k/2}}{\binom{2k}{k}},
$$



while for odd k,



$$
q_{k,1}=\frac{k^2}{2k-1}q_{k-1,0}.
$$



The elementary bounds binom(k,k/2)<=2^k and
binom(2k,k)>=4^k/(2k+1) give the safe common estimate
q_(k,sigma)<=4(k+1)^2 2^(-k). Hence



$$
0<b_k:=\frac{v_k}{h_k}q_{k,\sigma}
\le4\alpha(k+1)^2\eta^k,\qquad k>=1.\tag{3}
$$



## 2. An actual convergent expansion before Borel transformation

The finite Christoffel–Darboux identity is



$$
\frac1{1-t}-\sum_{k=0}^N\frac{v_k}{h_k}Q_k(t)
=\frac{v_N}{h_N}\frac{Q_{N+1}(t)-a_NQ_N(t)}{1-t},
\qquad a_N=v_{N+1}/v_N.
\tag{4}
$$



Fix 0<r<1. The coefficients of Q_N are nonnegative, so its absolute
value on |t|<=r is at most Q_N(r). Choose delta>0 so that the positive
root gamma of gamma^2=r gamma+1/4+delta is smaller than alpha.
Since beta_N tends to1/4, the positive recurrence, after a fixed initial
segment, gives Q_N(r)<=C_r gamma^N. This follows by induction after
choosing C_r to dominate the two initial values. The already proved
bound |a_N|<1/3, (2), and Q_N(1)>=alpha^(N-1) therefore bound (4) by
C'_r(gamma/alpha)^N, uniformly on |t|<=r.

Thus



$$
\frac1{1-t}=\sum_{k>=0}\frac{v_k}{h_k}Q_k(t)
\tag{5}
$$



is a locally uniformly convergent analytic identity in |t|<1. Its
Taylor coefficients agree term by term. Every summand coefficient is
nonnegative, so for each degree d their sum is exactly1.

## 3. Absolute entire Borel convergence

The coefficient recurrence for Q_k, after Borel transformation and
normalization f_k=F_k/q_(k,sigma), is exactly



$$
f_k(x)=\sum_{r>=0}
\frac{\prod_{j=0}^{r-1}(k(k+1)-(2j+\sigma)(2j+\sigma+1))}
     {((2r+\sigma)!)^2}x^{2r+\sigma},\tag{6}
$$



terminating at degree k. All nonzero products are positive and are at
most(k+1)^(2r). On |x|<=R, (6) and the elementary squared-factorial
series estimate give



$$
|f_k(x)|\le C_R\exp(2\sqrt{(k+1)\max(1,R)}).\tag{7}
$$



For sigma=1 the extra factor |x| can be absorbed into C_R. The exact
constant is immaterial; it does not depend on k. Combining(3) and(7)
gives a summable bound uniform on the x-disk. Therefore the series of
Borel polynomials in(1) converges absolutely and uniformly on every
compact set. Its coefficients are those obtained from(5), so the full
sum is exp(x). Subtracting the first N+1 terms proves(1), since
G_N=Borel(1/(1-t)-H_N).

For x>=0 the same coefficient identities can alternatively be summed
by Tonelli; the total is exp(x). No conditional series rearrangement
is used in either proof.

For the real interval alone there is an even shorter proof: the exact
finite difference G_N-G_M is the sum in(1) from N+1 through M, and the
already reviewed uniform kernel estimate gives sup_[0,1]G_M->0.
That finite telescoping argument is the dependency used in the factorial
interpolation note. The argument above additionally establishes entire
compact-uniform convergence.

## 4. Application to the matched raw family

The actual factorial functional ell_B annihilates Q_(n+1),...,Q_(2n-1).
The beta/Borel identity consequently gives, for n>=1,



$$
R_n(1)=\int_0^1P_n(x)G_{2n-1}(x)\,dx.\tag{8}
$$



This is the same entire evaluated remainder as with G_n, but uses a
later positive tail. Any interpolation of f_k at the high parity nodes
may now be summed against the explicit weights b_k in(3). The
exponential weight and its polynomial prefactor justify the required
moment sums. The quantitative interpolation and its factorial norm and
cancellation bounds are proved separately in
`raw_arctan_dual_factorial_mass.md`.

Neither absolute convergence nor positivity of the tail makes P_n have
one sign. This lemma does not claim a bound for the whole primitive
remainder or a proof of irrationality.
