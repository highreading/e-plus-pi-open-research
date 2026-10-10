> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Uniform local flatness of the even dual polynomial and its exponential error

Date: 2026-09-13. Original continuation by root. Independent review pending.

This note controls the actual polynomial V across the real error interval,
and hence the complete exponential error relative to V(1). In the primitive
cofactor normalization this error grows at a specified exponential rate
relative to V's nonzero integer leading coefficient. The signed arctangent
error and the endpoint gcd remain separate.

## 1. Actual coefficients and the complex-weight bound

Assume n=2m>=2. Use the definitions and passed review in
raw_joint_dual_hankel_and_even_root_product.md and
raw_joint_hankel_even_root_product_independent_review.md. Put

    w(theta)=|1+exp(2i theta)|^(2m),
    f(theta)=exp(exp(i theta))w(theta),
    A_ij=[z^(n+i-j)]exp(z)(1+z^2)^n,    0<=i,j<=n,
    v=A^(-1)e0,    v(z)=sum_(j=0)^n v_j z^j,
    c_m=((2m)!)^2/[m!(3m)!].

All circle integrals use dtheta/(2pi). The vector polynomial is
v(z)=q(z)/(n! V(1)). In contrast, write v_n^lead=[t^n]V for the
nonzero integer LEADING coefficient of V. This distinguishes the two
coefficient vectors.

The proved inverse bound and Hermitian-part bound are

    e^-1 cos^2(1)c_m <= v_0 <= e/cos(1)c_m,
    H=(A+A*)/2 >= h G0,       h=e^-1 cos(1),

where G0 is the Gram matrix of w. Since Av=e0, v*Hv=v_0. Therefore

    ||v||_w <= e/cos(1) sqrt(c_m).                           (1)

The same matrix equation means

    integral f v conjugate(p)=0   for p in span{z,...,z^n},
    integral f v=1.

Define b_r=integral f v z^r, so b_0=1. The exact joint moment identity
q(D)H_n(1+t)=t^n V(1+t) gives the POLYNOMIAL identity

    V(1+t)/V(1)=sum_(r=0)^n n!/(n+r)! b_r t^r.              (2)

Indeed mu(z^(n+r)q)=integral f q z^r, the coefficient of t^(n+r)
times (n+r)! in that identity. No Taylor remainder is omitted.

Let D_(m,r) be the SQUARED distance in L2(w) from z^-r to
span{z,...,z^n}. The independently passed theorem in
raw_circular_binomial_prediction_bounds.md gives

    c_m D_(m,r)<=binom(m+s,s)^2<=n^(2s)/(s!)^2,
    s=floor(r/2),                     0<=r<=n+1.            (3)

In particular c_m D_(m,0)=c_m D_(m,1)=1. Its proof uses the positive
base circle measure, not a positivity assumption for f.

Subtract an arbitrary p in the test space from z^-r in the integral
for b_r. Since |f|<=e w, weighted Cauchy-Schwarz, (1), and the
infimum over p prove

    |b_r|<=C sqrt(c_m D_(m,r))<=C n^s/s!,
    C=e^2/cos(1),     s=floor(r/2),     1<=r<=n.             (4)

The square root of the squared prediction distance is essential.

## 2. Uniform flatness and a growing zero-free disk

Use n!/(n+r)!<=n^-r in (2), and separate r=2s and r=2s+1.
Extending the nonnegative bounding sums to infinity gives, for every
complex t,

    |V(1+t)/V(1)-1|
      <=C{exp(|t|^2/n)-1+(|t|/n)exp(|t|^2/n)}.              (5)

Thus V(1+t)/V(1)=1+O_R(1/n) uniformly on |t|<=R, for every fixed R,
along the even indices. This controls a compact complex disk, not
merely real pointwise values.

For a quantitative growing disk choose eta=log(1+1/(4C)).
At |t|<=sqrt(eta n), the first term in (5) is 1/4; the second is
at most 1/4 whenever n>=16 C^2 eta exp(2eta). Consequently

    min_(V(r)=0)|r-1|>=sqrt(eta n)                           (6)

for every sufficiently large even n. One can take a strict radius
if desired; the bound by 1/2 already excludes zeros on the displayed
closed disk. Unlike the preceding root product of order n, (6)
bounds the distance of EVERY root. No precise limiting distribution
is asserted.

## 3. The complete relative exponential-error estimate

The full error identity is

    Re(1)=(-1)^n/n! integral_0^1
                        exp(1-x)[x(1-x)]^n V(x)dx.          (7)

On 0<=x<=1, take t=x-1 in (5). This gives

    sup |V(x)/V(1)-1|<=epsilon_n:=2C exp(1/n)/n.              (8)

Normalize the beta kernel: let X have density
[x(1-x)]^n/B(n+1,n+1), and put Y=X-1/2. Then Y is symmetric,
|Y|<=1/2, and E Y^2=1/[4(2n+3)]. The elementary power-series bound

    cosh(y)-1<=4(cosh(1/2)-1)y^2     (|y|<=1/2)

therefore yields

    E exp(-Y)=1+xi_n,
    0<=xi_n<=(cosh(1/2)-1)/(2n+3).                          (9)

Since B(n+1,n+1)/n!=n!/(2n+1)! and n is even, (7)-(9) give

    Re(1)=exp(1/2)V(1)n!/(2n+1)! (1+theta_n),
    |theta_n|<=xi_n+epsilon_n(1+xi_n)=O(1/n).                (10)

The error term is explicit and uniform. This estimates the entire
signed exponential integral in the actual cofactor normalization.
For all sufficiently large even n, its sign is the sign of V(1),
which is also the sign of v_n^lead.

## 4. The unreduced exponential error grows at a specified rate

The passed even root-product theorem gives

    e^-1 cos(1)B_m <= V(1)/v_n^lead <= e/cos^2(1)B_m,
    B_m=(4m)!m!(3m)!/((2m)!)^3.                             (11)

The exact remaining factorial ratio is

    B_m n!/(2n+1)!
      =m!(3m)!/[(2m)!^2(4m+1)]
      ~sqrt(3)/(4n) beta^n,
    beta=3sqrt(3)/4>1.                                     (12)

The last asymptotic follows directly from Stirling's formula:
m!(3m)!/(2m)!^2 ~sqrt(3)/2 (27/16)^m and n=2m.
Combining (10)-(12) proves that Re(1)/v_n^lead is positive and
comparable to beta^n/n, with constants independent of n. More
explicitly,

    liminf n beta^-n Re(1)/v_n^lead
       >=sqrt(3)exp(-1/2)cos(1)/4,
    limsup n beta^-n Re(1)/v_n^lead
       <=sqrt(3)exp(3/2)/(4cos^2(1)).                        (13)

In particular,

    (|Re(1)|/|v_n^lead|)^(1/n) --> beta,
    |Re(1)|>=c beta^n/n --> infinity                       (14)

along the sufficiently large even indices, for a constant c>0.
The second assertion uses the nonzero integer leading coefficient;
no conjectured coefficient height is involved.

## 5. Exact scope for the irrationality problem

This supplies quantitative control of one complete simultaneous error.
In this normalization its exponential part does not shrink, even on
the even subsequence. The target is nevertheless still

    [Re(1)+4Ra(1)]/g_n,
    g_n=gcd(|Z_n|,|Pe_n(1)+4Pa_n(1)|).

The theorem does not estimate Ra(1), its cancellation against Re(1),
or g_n. It therefore does not exclude a shrinking combined primitive
form. A strategy making Re(1)/g_n small separately needs at least
the corresponding exponential arithmetic gain, retaining the factor
|v_n^lead| too. The useful next analytic task is a signed estimate
for Ra in the same Toeplitz coordinates; the fixed-combination gcd
remains the arithmetic task.

