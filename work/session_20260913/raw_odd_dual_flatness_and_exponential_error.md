> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Odd dual flatness and the complete exponential-error constant

Date: 2026-09-13. Original bounded continuation by audit_results.
Independent review: FULL PASS by audit_computations; see raw_odd_dual_flatness_independent_review.md. The limiting determinant certificate has independently passed its full adversarial review.

This extends the already proved even-degree flatness theorem to odd degrees using the actual normalized inverse bound. It does not use positive accretivity of the odd signed Toeplitz matrix.

Write n=2m+1, and let v_n^lead=[t^n]V_n, the nonzero integer leading coefficient. The conclusion is

    Re_n(1)=-sqrt(e) V_n(1) n!/(2n+1)! (1+O(1/n)),        (1)

and, with beta=3sqrt(3)/4,

    lim_(n odd) n beta^(-n) Re_n(1)/v_n^lead
       =-(3/4)sqrt(e) s_infty >0.                        (2)

Here s_infty is the fixed determinant ratio certified in
raw_odd_limiting_determinant_interval_certificate.md, with
-0.47<s_infty<-0.45. The signed arctangent error and the actual endpoint gcd remain separate.

## 1. Uniform finite inverses, including the finite prefix

The exact rank-two formula and operator limit prove

    Atilde_m=T_m+U_mV_m,
    sup_m ||T_m^(-1)||<infinity,
    D2_m->D2_+,       det D2_+ !=0.

Woodbury and the uniform exterior bounds therefore bound ||Atilde_m^(-1)|| for every sufficiently large m. The passed added-column theorem proves invertibility at every finite m, including m=0. A finite collection of finite inverse norms has a finite maximum. Hence there exists a finite constant

    K_A=sup_(m>=0)||Atilde_m^(-1)||<infinity.              (3)

This is an existence statement for the uniform constant; it does not claim an effective first degree or a computed maximum of the finite prefix.

The same reasoning also bounds the actual high compression inverses. Its block-inverse identity is

    B_m^(-1)=Pi Atilde_m^(-1)Pi
       -(Pi Atilde_m^(-1)v)(v*Atilde_m^(-1)Pi)/
                         (v*Atilde_m^(-1)v).

The denominator is 1/s_m and tends to 1/s_infty!=0. The high compression is separately proved invertible at every m. Thus its inverse norms also have a finite supremum. Only (3) is needed for the coefficient estimate below.

## 2. The actual complex-weight moment coefficients

Let

    A_ij=[z^(n+i-j)]e^z(1+z^2)^n,   0<=i,j<=n,
    u=A^(-1)e_0,       u(z)=sum_j u_j z^j,
    c_m=((2m+1)!)^2/[m!(3m+2)!].

The positive metric G is the Gram matrix of

    w_+(theta)=|1+z^2|^(2m+2),       |z|=1.

It satisfies (G^(-1))_00=c_m. Since

    G^(1/2)u=Atilde_m^(-1)G^(-1/2)e_0,

equation (3) gives

    ||u||_(w_+)<=K_A sqrt(c_m).                            (4)

This follows from the inverse norm, not from a sign for the odd Hermitian part.

The actual signed complex symbol is

    f(theta)=e^z(2cos(theta))^(2m+1).

The moment equations are

    integral f u conjugate(p)=0,
       p in span{z,...,z^n},
    integral f u=1.

All integrals use normalized Haar measure. Define b_r=integral f u z^r, so b_0=1. The exact joint identity, valid in both parities, gives

    V_n(1+t)/V_n(1)
       =sum_(r=0)^n n!/(n+r)! b_r t^r.                    (5)

It is a polynomial identity without an omitted remainder.

## 3. Positive lower-weight predictions with unequal parity dimensions

Put

    w_-(theta)=|1+z^2|^(2m).

For the squared distance

    D_(m,r)=dist_(w_-)^2(z^(-r),span{z,...,z^(2m+1)}),

the two parities have DIFFERENT predictor dimensions. With s=floor(r/2), changing variable w=-z^2 gives

    r=2s:   predict 1 from w^(s+1),...,w^(s+m);
    r=2s+1: predict 1 from w^(s+1),...,w^(s+m+1),

under the positive weight |1-w|^(2m).

The previously proved circular binomial residual construction applies to arbitrary degree M in this weight. Its monic polynomial has squared norm

    h_M^(m)=M!(2m+M)!/((m+M)!)^2.

The reversed polynomial F_M has constant one and all roots outside the closed unit disk. Truncating 1/F_M through degree s gives an admissible residual at gap s. Its boundary supremum is at most binom(M+s,s), by the root-in-disk reciprocal coefficient bound. Therefore

    D_(m,2s)<=h_m^(m) binom(m+s,s)^2,
    D_(m,2s+1)<=h_(m+1)^(m) binom(m+1+s,s)^2.             (6)

For m=0 this is the Haar case, with F_M=1 and norm one, and the same upper bounds hold. A dimension-zero even predictor is also covered.

The exact normalizing ratios are

    c_m h_m^(m)=(2m+1)^2/[(3m+1)(3m+2)]<=1,
    c_m h_(m+1)^(m)=(m+1)/(3m+2)<=1.                     (7)

For 1<=r<=n, both relevant factorial products in the binomial coefficients have factors at most n. Thus

    sqrt(c_m D_(m,r))<=n^s/s!,
    s=floor(r/2),             1<=r<=n.                    (8)

The square root in (8) is essential.

Pointwise,

    |f|<=e sqrt(w_+ w_-).

Subtracting any predictor from z^(-r), then applying weighted Cauchy--Schwarz and (4), proves

    |b_r|<=C sqrt(c_m D_(m,r))<=C n^s/s!,
    C=e K_A,     s=floor(r/2),     1<=r<=n.                (9)

No positive-sector inequality for f or A has been used.

## 4. Uniform flatness and a growing zero-free disk

Since n!/(n+r)!<=n^(-r), inserting (9) into (5) and summing the two parity bounds yields, for every complex t,

    |V_n(1+t)/V_n(1)-1|
       <=C{exp(|t|^2/n)-1
               +( |t|/n )exp(|t|^2/n)}.                  (10)

In particular

    V_n(1+t)/V_n(1)=1+O_R(1/n)

uniformly on every fixed complex disk |t|<=R, along all odd degrees.

There is also a constant eta>0 giving a zero-free disk of radius sqrt(eta n) for all sufficiently large odd n. For example choose

    eta=log(1+1/(4C)).

The right side of (10) is at most 1/2 on that disk once
n>=16 C^2 eta exp(2eta). The existence of C is proved, although its finite-prefix maximum has not been explicitly evaluated.

## 5. The complete signed exponential integral

The already reviewed exact error identity is

    Re_n(1)=(-1)^n/n! integral_0^1
                      e^(1-x)[x(1-x)]^n V_n(x)dx.         (11)

On this interval, (10) gives

    sup |V_n(x)/V_n(1)-1|
       <=epsilon_n:=2C exp(1/n)/n.

For X with beta density proportional to [x(1-x)]^n, Y=X-1/2 is symmetric and

    E Y^2=1/[4(2n+3)].

The elementary inequality
cosh(y)-1<=4(cosh(1/2)-1)y^2 for |y|<=1/2 gives

    E exp(-Y)=1+xi_n,
    0<=xi_n<=(cosh(1/2)-1)/(2n+3).

Since B(n+1,n+1)/n!=n!/(2n+1)!, equation (11), with odd n, becomes exactly

    Re_n(1)=-sqrt(e) V_n(1)n!/(2n+1)! (1+theta_n),
    |theta_n|<=xi_n+epsilon_n(1+xi_n)=O(1/n).              (12)

This estimates the entire signed exponential error in the actual cofactor normalization, rather than its first Taylor coefficient or an absolute-integral upper bound.

## 6. Exact factorial constant and eventual sign

The odd scalar identity is

    V_n(1)/v_n^lead=B_m^odd s_m,
    B_m^odd=(4m+2)!m!(3m+2)!/((2m+1)!)^3,
    s_m->s_infty<0.

Retaining the error factorials gives exactly

    B_m^odd n!/(2n+1)!
       =m!(3m+2)!/[(2m+1)!^2(4m+3)]
       ~ (3/(4n)) beta^n,
    beta=3sqrt(3)/4.                                     (13)

For example, divide the numerator factorial ratio by its even counterpart at 2m. The extra factor is
(3m+1)(3m+2)/(2m+1)^2 ->9/4; after the index shift n=2m+1, Stirling's factor becomes exactly 3/4 in (13), not the even factor sqrt(3)/4.

Equations (12)-(13) prove (2). In particular its limiting positive constant lies in

    ((27/80)sqrt(e), (141/400)sqrt(e)).

For every sufficiently large odd n, Re_n(1)/v_n^lead is positive: the minus sign in (12) cancels the negative sign of s_m. The estimate does not infer an all-degree real sign from dyadic nonvanishing.

Thus

    (|Re_n(1)|/|v_n^lead|)^(1/n)->beta

along odd degrees, and |Re_n(1)|>=c beta^n/n tends to infinity there, using the nonzero integer leading coefficient. Combined with the passed even theorem, these root-rate and eventual exponential lower-bound statements hold along all degrees.

## 7. Scope

This proves uniform odd flatness, an odd growing zero-free disk, the complete relative exponential-error asymptotic, and its exact positive leading-coefficient-normalized limit. It preserves all factorials and the sign of s_infty.

The target combined primitive error is still

    sign(Z_n)[Re_n(1)+4Ra_n(1)]/g_n,
    g_n=gcd(|Z_n|,|Pe_n(1)+4Pa_n(1)|).

Neither cancellation with Ra_n nor the endpoint gcd is estimated here. Growth of the unreduced exponential contribution does not rule out a shrinking combined primitive form.

No new canonical degree, root, prime, or singular-value scan was performed.
