> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Complete diagonal error/content threshold — Stage 1, revised derivation

Author: Child 3. Status: author proof using the inherited complete signed-product and primitive-moment interfaces; no independent review claimed. This revision preserves COMPLETE_ERROR_CONTENT_THRESHOLD_STAGE1.md and strengthens its compact-weight estimate. S denotes the actual e+pi. Its rationality remains unresolved.

## 1. Main result

For the actual family m=k and every k>=131072, let beta(T)=sum beta_j T^j be the complete physical determinant, let I_j=delta beta_j be the complete integer coefficients, and let g=gcd(I_0,...,I_k)>0. Put P(T)=sum (I_j/g)T^j and A_k=|I_k/g|. Then

    log|beta(S)/beta_k|
      =-(log 4)k^2-(1/2)k log k
         +[log(2 sqrt(pi))+2/pi]k+O(k^(4/5)).                 (1)

The constant is absolute. The proof below is elementary and gives explicit finite errors; it needs no uniform varying-weight asymptotic theorem. It uses the inherited all-index nonvanishing and exact top-coefficient identities without reauditing their arithmetic construction.

Define

    D_k=det[1/(i+j+1/2)]_(0<=i,j<k),
    kappa_k=[4^(k-1)/binom(2k-2,k-1)]^k,
    Lambda_k=log kappa_k-log D_k,
    C=192e^4,
    U_k=(e+10pi^2/3+16k^2(4/5)^k)/2,
    U=(e+10pi^2/3+1)/2.

For each positive integer v, there is an exact threshold T_k(v) such that

    |P(S)|<v^(-k)  iff  A_k<T_k(v).                          (2)

Its asymptotic expansion is

    log T_k(v)=(log 4)k^2+(1/2)k log k
                  -[log(2 sqrt(pi) v)+2/pi]k+O(k^(4/5)).    (3)

Here v enters exactly through -k log v, so the error bound is independent of v. The explicit finite interval is in Section 7. No estimate showing that the ACTUAL A_k meets (2) is proved. In particular, this is an analytic/content interface, not an irrationality proof.

## 2. Exact objects, full endpoint jets, and diagonal cancellation

The inherited sources, read in the present assignment, are the current main/BACKGROUND_MAP.md and the following paths under work/session_20261002_codex_continuation/:

- agent3_analysis/GROWING_POLE_ORDER_SHORT_COMPLETE_PRODUCT.md;
- main/GROWING_POLE_ACTUAL_NORM_CONTENT_BUDGET.md;
- agent3_analysis/GROWING_POLE_ALL_ROOT_LOCALIZATION.md;
- main/GENERAL_POLE_RANK_M_PRIMITIVE_INTERFACE.md.

Let mu be the pushforward of exp(-t)dt on t>=0 by y=(1-t)^2. Put d=k-1 and

    nu_k(f)=sum_(j=0)^d a_j f^(j)(-1),
    a_j=2^j binom(d,j)(2(d-j)-1)!!/(2d-1)!!,
    rho_k=mu-nu_k,
    c_k=4^k/binom(2k-2,k-1).

The convention (-1)!!=1 is used. Every derivative through d remains present. On [0,1],

    dgamma=y^(-1/2)dy,
    dsigma_k=[exp(sqrt(y))+c_k(1+y)^(-k)]dgamma/2.

The k-by-2k blocks are C_ij=rho_k(y^(i+j)), V_ij=nu_k(y^(i+j)), and R_ij equal to the complete rational part of c_k integral_0^1 x^(2i+2j)/(1+x^2)^k dx minus (2i+2j)!. The physical compact block is eC+R+SV, where S=e+pi. Thus beta(T)=det[C;R+TV] and beta(S)=det[C;sigma_k] by an exact row operation.

The inherited comparison for k>=131072 is

    exp(-C)F*_k det G_(sigma_k,k)
       <=|beta(S)|<=F*_k det G_(sigma_k,k),
    F*_k=det M_[mu(y+1)^k,k]>0,
    sign beta(S)=(-1)^k.                                    (4)

The exact complete leading-coefficient identity at m=k is

    beta_k=(-1)^[k+binom(k,2)] kappa_k F*_k.                 (5)

The upper jet is annihilated by (y+1)^k. In the lower confluent insertion, the Vandermonde square vanishes to total order k(k-1), forcing derivative k-1 in every variable and forcing all these derivatives onto that square. This is the inherited reason that the factor kappa_k is exact. No endpoint term or Taylor factorial is discarded.

Consequently there is theta_k in [exp(-C),1] with

    beta(S)/beta_k
       =(-1)^binom(k,2) theta_k det G_(sigma_k,k)/kappa_k.   (6)

Both numerator and denominator are nonzero. This identity concerns the full product of root errors. No individual-root localization or hyperbolicity is inferred at m=k.

For exact arithmetic let B_k be the odd part of binom(2k-2,k-1), and L_n=lcm(1,...,n). The inherited complete clearer is

    E_(k,k)=B_k 2^(3k+2)L_k L_(6k),
    delta=B_k^k E_(k,k)^k,
    I_j=delta beta_j in Z,
    g=gcd(I_0,...,I_k),  P(T)=sum (I_j/g)T^j.

The complete primitive-value identity is therefore

    |P(S)|=A_k theta_k det G_(sigma_k,k)/kappa_k,
    A_k=|I_k/g|.                                            (7)

All subsequent arithmetic statements retain this final gcd of ALL coefficients.

## 3. Reference kernel and an explicit O(k) determinant bracket

Under y=x^2, dgamma=2dx on [0,1]. Its orthonormal polynomials are

    p_i(y)=sqrt((4i+1)/2) P_(2i)(sqrt(y)),
    K_k(x^2)=sum_(i<k)(2i+1/2)P_(2i)(x)^2.

Here P_n is the ordinary Legendre polynomial. Its elementary Laplace representation gives

    |P_n(x)|<=1,
    |P_n(x)|<=sqrt(pi)/sqrt(2n(1-x^2)),  n>=1, |x|<1.

Indeed, the modulus of the integrand (x+i sqrt(1-x^2)cos phi)^n is at most exp[-n(1-x^2)sin^2(phi)/2]. Symmetry and sin phi>=2phi/pi on [0,pi/2] reduce the integral to a Gaussian upper bound. Hence

    K_k(x^2)<=5pi k/6 for 0<=x<=1/2,
    K_k(x^2)<=k^2 for 0<=x<=1.                              (8)

For G=G_(gamma,k) and H=G_[gamma(1+y)^(-k),k], the relative bump trace is

    tr(G^(-1)H)=2 integral_0^1 K_k(x^2)(1+x^2)^(-k)dx.

The exact beta integral gives

    J_k=integral_0^infinity (1+x^2)^(-k)dx
       =(pi/2)binom(2k-2,k-1)/4^(k-1),
    c_k J_k=2pi.

Split the trace integral at 1/2, use (8), and use c_k<=8k. This gives

    c_k tr(G^(-1)H)<=(10pi^2/3)k+16k^3(4/5)^k.

Since exp(sqrt(y))<=e, Loewner order and AM-GM on the k eigenvalues imply

    2^(-k)D_k<=det G_(sigma_k,k)<=U_k^k D_k.                (9)

For k>=64, 16k^2(4/5)^k<=1: (4/5)^8<1/5 verifies the endpoint, and the ratio of consecutive k^2(4/5)^k terms is less than one thereafter. Thus U_k<=U on the required range. This O(k) logarithmic comparison alone proves the first two terms of (1), whereas a pointwise bound of order sqrt(k) would leave an O(k log k) ambiguity.

## 4. A sharp one-sided lower bound for the exponential baseline

Let G0=G_[exp(sqrt(y))gamma,k]. Define the exact finite sum

    zeta_k=(1/2)sum_(i=0)^(k-1)(4i+1)
                       [binom(2i,i)/4^i]^2.                (10)

The normalized Andreief integral for det G0/D_k is the expectation of exp(sum sqrt(y_j)) under the positive reference polynomial ensemble. Jensen therefore yields

    log(det G0/D_k)>=integral sqrt(y)K_k(y)dgamma(y)=zeta_k.

For the last equality, the needed Legendre integral is

    integral_0^1 x P_(2i)(x)^2 dx=P_(2i)(0)^2/2.

Here is a direct proof. For p=P_n and lambda=n(n+1), the Legendre equation gives

    [(1-x^2)^2 p'^2+lambda(1-x^2)p^2]'
       =-2lambda x p^2.

If n is positive and even, integrate from 0 to 1 and use p'(0)=0. The case n=0 follows directly. Since P_(2i)(0)=(-1)^i binom(2i,i)/4^i, (10) follows.

Elementary Stirling remainders give the following useful bounded error:

    zeta_k=2k/pi+1/2-2/pi+r_k,
    |r_k|<=Z,  Z=5pi exp(5/144)/432.                        (11)

For detail, for i>=1 write

    log binom(2i,i)=2i log2-(1/2)log(pi i)-1/(8i)+d_i,
    -1/(576i^2)<=d_i<=1/(72i^2).

The logarithm of the i-th summand in (10), divided by 2/pi, is

    log(1+1/(4i))-1/(4i)+2d_i,

whose absolute value is <=5/(144i^2). Thus the absolute difference of that summand from 2/pi is <=(2/pi)(5/144)exp(5/144)/i^2. Summation proves (11).

Set

    c0=2/pi-1/2+Z.

Since sigma_k>=exp(sqrt(y))gamma/2, we obtain

    eta_k:=log(det G_(sigma_k,k)/D_k)
       >=zeta_k-k log2
       >=(2/pi-log2)k-c0.                                  (12)

## 5. Quantified exponential-baseline asymptotic by finite matrices

In the p_i basis, multiplication by y has the symmetric tridiagonal Jacobi matrix J with

    b_i=1/2+1/[2(4i-1)(4i+3)],
    a_i=(2i+1)(2i+2)/[(4i+3)sqrt((4i+1)(4i+5))],

where b_i is diagonal and a_i connects i to i+1. These formulas follow by applying the Legendre three-term recurrence twice and inserting the orthonormal normalization. Let J_k be its k-dimensional compression. It is a positive contraction because it is compressed multiplication by y on [0,1].

Let Q_k have constant diagonal 1/2 and off-diagonal 1/4. The trace norm obeys

    ||J_k-Q_k||_1<=43/72.                                  (13)

To verify this bound, the sum of absolute diagonal differences is at most

    1/6+sum_(i>=1)1/[2(4i-1)(4i+3)]=5/24.

For s=4i+3, one has

    a_i=(1/4)(1-s^(-2))/sqrt(1-4s^(-2)),
    0<a_i-1/4<=s^(-2).

The latter inequality follows by squaring the positive sides; for t=s^(-2)<=1/9 it reduces to 6-17t-64t^2>=0. Therefore twice the off-diagonal absolute sum is at most

    2 sum_(i>=0)(4i+3)^(-2)
       <=2(1/9+integral_0^infinity (4x+3)^(-2)dx)=7/18.

The trace norm of each single symmetric off-diagonal pair is twice its entry, proving (13).

Ordered eigenvalue variation for Hermitian matrices gives sum_j|lambda_j(J_k)-lambda_j(Q_k)|<=||J_k-Q_k||_1. Using |sqrt(s)-sqrt(t)|<=sqrt(|s-t|) and Cauchy-Schwarz,

    |tr sqrt(J_k)-tr sqrt(Q_k)|<=sqrt(43k/72).

The eigenvalues of Q_k are [1+cos(jpi/(k+1))]/2 for 1<=j<=k. A monotone Riemann-sum bound for cos(pi t/2) proves

    |tr sqrt(J_k)-2k/pi|<=sqrt(43k/72)+1.                   (14)

We next compare the actual baseline determinant with tr sqrt(J_k), without assuming they are equal. For a function f on [0,1], write

    F_k(f)=[integral p_i(y)p_j(y)f(y)dgamma(y)]_(i,j<k).

Then det F_k(exp(sqrt(y)))=det G0/D_k. Let f(y)=exp(sqrt(y)) and let q_d be its degree-d Bernstein polynomial. For every d>=1,

    1<=q_d<=e,
    ||f-q_d||_infinity<=e/(sqrt(2)d^(1/4)).                 (15)

Indeed |f(s)-f(t)|<=e sqrt(|s-t|); Jensen applied to the binomial variable in the Bernstein formula bounds the error by e times the fourth root of its variance, at most e/(sqrt(2)d^(1/4)).

If 1<=d<k, the difference F_k(q_d)-q_d(J_k) is supported in the last d coordinates. To see this, expand powers of the tridiagonal J as nearest-neighbor paths. A path of length at most d starting in any earlier coordinate cannot cross the upper compression boundary. The difference is symmetric, so the same support statement holds for columns. Its rank is therefore <=d. Both matrices have spectra in [1,e], so the difference has operator norm <=e-1 and trace norm <=(e-1)d.

For positive matrices A,B>=I,

    |log det A-log det B|<=||A-B||_1,

by integrating tr[(B+t(A-B))^(-1)(A-B)]. Apply this first to F_k(f),F_k(q_d), then to the two polynomial matrices, then to q_d(J_k),f(J_k). Equations (14)-(15) give

    |log(det G0/D_k)-2k/pi|<=E_k(d),                       (16)
    E_k(d)=sqrt(2)e k d^(-1/4)+(e-1)d+sqrt(43k/72)+1.

The argument uses only the multiplication operator for the fixed reference measure, polynomial approximation, and finite matrix estimates. For d=ceil(k^(4/5)), which is <k throughout the required range, E_k(d)=O(k^(4/5)).

## 6. The normalized endpoint bump costs only o(k)

This is a separate estimate; it is not implied by the trace bound in Section 3. Set

    h=sqrt(8 log k/k),
    u=4kh=4sqrt(8k log k),
    r=ceil(4u)=ceil(16sqrt(8k log k)),
    Bump_k=r log(32k+2)+64k^(-11)+8k^(-2).                 (17)

For k>=131072, h<1/2. Work in the gamma-orthonormal basis, and set

    B=c_k F_k((1+y)^(-k)).

It is positive and B<=c_k I<=8k I. Split its integral at x=sqrt(y)=h.

Outside the short interval, log(1+h^2)>=h^2/2 gives

    (1+x^2)^(-k)<=k^(-4),
    tr B_out<=8k^(-2).                                     (18)

Inside, truncate each p_i(x^2) before its x^(2r) term and write the vector p=T+R. The vector T(x) lies in a fixed subspace of dimension <=r. The exact Legendre coefficients give

    |[x^(2j)]p_i(x^2)|<=sqrt(2k)(4k)^(2j)/(2j)!,  i<k.     (19)

For j<=i, divide the exact coefficient by |P_(2i)(0)|. The resulting factor is

    [(2i+1)...(2i+2j)] i!^2/[(i-j)!(i+j)!(2j)!],

which is <=(4k)^(2j)/(2j)!; also |P_(2i)(0)|<=1. This proves (19), including j=0. Coefficients beyond degree i vanish.

On 0<=x<=h, the tail in (19) is bounded by

    sum_(j>=r)u^(2j)/(2j)!
      <=exp(u)(eu/(2r))^(2r)
      <=exp(-7u)<=k^(-7).                                  (20)

Here 2r>=8u and log 8>2; the last inequality uses u>=log k. These inequalities hold on the stated range. Thus each component of R has modulus <=sqrt(2k)k^(-7), and the positive remainder Gram matrix

    Rg=2c_k integral_0^h R(x)R(x)^T(1+x^2)^(-k)dx

has trace <=32k^(-11). Let Tg be defined analogously with T. The pointwise inequality (T+R)(T+R)^T<=2TT^T+2RR^T gives

    B<=2Tg+2Rg+B_out.

Also T=p-R gives Tg<=2B_in+2Rg, so

    rank(2Tg)<=r,
    ||2Tg||<=32k+128k^(-11)<=32k+1.

The positive remainder 2Rg+B_out has trace <=64k^(-11)+8k^(-2). Determinant monotonicity, followed by integration of the log-determinant derivative for the remainder, proves

    0<=log det(I+B)<=Bump_k.                               (21)

Let A0=F_k(exp(sqrt(y)))>=I. The actual bump correction to the exponential baseline is

    det(A0+B)/det A0
       =det(I+B^(1/2)A0^(-1)B^(1/2))<=det(I+B).

Consequently

    0<=log(det(G0+c_k H)/det G0)<=Bump_k.                   (22)

Since sigma_k=(exp(sqrt(y))gamma+c_k(1+y)^(-k)gamma)/2, combine (12), (16), and (22) to obtain the explicit bounds

    zeta_k-k log2 <= eta_k
      <= min{k log U_k,
             (2/pi-log2)k+E_k(d)+Bump_k}.                  (23)

In particular,

    eta_k=(2/pi-log2)k+O(k^(4/5)),                          (24)

because Bump_k=O(sqrt(k)(log k)^(3/2))=o(k^(4/5)). The lower error in (24) is in fact bounded by the absolute constant c0 from Section 4. This proves the compact-weight linear coefficient without an unavailable varying-weight theorem.

## 7. Exact Cauchy reference, finite errors, and the rational target

Cauchy's determinant identity gives

    D_k=product_(i<j)(j-i)^2/product_(i,j)(i+j+1/2)
       =product_(i=0)^(k-1)
          2^(4i+1)/[(4i+1)binom(4i,2i)^2].                 (25)

The equality with the second expression also follows from the even-Legendre monic norms. In particular D_1=2.

Here are explicit reference errors, already proved in the first stage document. With H_n=sum_(i=1)^n 1/i and H_n^(2)=sum_(i=1)^n 1/i^2, for k>=2,

    log D_k=-(log4)k^2+k log(4pi)+log(2/pi)
                     -(1/8)H_(k-1)+R_D(k),
    -H_(k-1)^(2)/144<=R_D(k)<=37H_(k-1)^(2)/1152.          (26)

For n=k-1,

    log kappa_k=(k/2)log(pi n)+k/(8n)+R_kappa(k),
    -k/(72n^2)<=R_kappa(k)<=k/(576n^2).                    (27)

To verify the constants, use log(n!)=(n+1/2)log n-n+(1/2)log(2pi)+r_n with 1/(12n+1)<r_n<1/(12n). It gives

    log binom(4i,2i)=4i log2-(1/2)log(2pi i)-1/(16i)+d_i,
    -1/(2304i^2)<=d_i<=1/(288i^2).

The logarithm of the i-th factor in (25), i>=1, is then -4i log2+log pi-1/(8i)+epsilon_i, where

    -1/(144i^2)<=epsilon_i<=37/(1152i^2).

Summation proves (26), and the same calculation for binom(2n,n) proves (27). The epsilon_i sum converges with tail O(1/k), so

    Lambda_k=(log4)k^2+(1/2)k log k-k log(4sqrt(pi))
                       +(1/8)log k+C_ref+O(1/k),          (28)

where C_ref is a finite absolute constant. The exact D_k and kappa_k, rather than this asymptotic constant, are used in every finite threshold.

From (6),

    log|beta(S)/beta_k|=-Lambda_k+eta_k+log theta_k,
    -C<=log theta_k<=0.                                    (29)

Equations (23), (26)-(29) prove (1). They also give fully explicit finite bounds for it, including the inherited bounded factor and every reference error.

Define the exact rational-target threshold

    T_k(v)=kappa_k/[v^k theta_k det G_(sigma_k,k)].          (30)

Equation (7) proves the exact equivalence (2). For a practical finite interval, put

    X_k(v)=Lambda_k-k log v+(log2-2/pi)k,
    d=ceil(k^(4/5)).

Then

    X_k(v)-E_k(d)-Bump_k <= log T_k(v)
       <= X_k(v)+C+c0.                                    (31)

A sharper version retaining zeta_k and the original O(k) upper bound is

    Lambda_k-k log v
      -min{k log U_k,(2/pi-log2)k+E_k(d)+Bump_k}
       <=log T_k(v)
       <=Lambda_k-k log v+k log2-zeta_k+C.                 (32)

Thus log A_k below the left side guarantees |P(S)|<v^(-k); log A_k at least the right side prevents that strict inequality. Equations (28) and (31) prove (3).

If S=u/v in lowest terms, v^k P(u/v) is an integer. The inherited full nonvanishing gives P(S)!=0, hence |P(S)|>=v^(-k). Therefore satisfying any sufficient criterion above for the ACTUAL A_k excludes that hypothetical denominator. To prove irrationality by this route one needs enough actual arithmetic control to exclude every fixed v; no such control is supplied here.

For example, if along an unbounded subsequence

    log A_k=(log4)k^2+(1/2)k log k+d_* k+o(k),

then for fixed v the strict inequality

    d_*<-[log(2sqrt(pi)v)+2/pi]

suffices to beat its target eventually, while the reverse strict inequality prevents it eventually. Equality requires finer sublinear information. A strict saving at the k^2 scale, or at the k log k scale below coefficient 1/2 with the k^2 coefficient fixed, also suffices eventually for every fixed v.

For a direct final-content translation, |I_k|=delta kappa_k F*_k. Condition log A_k<L is exactly

    g>delta kappa_k F*_k exp(-L).

The threshold thus preserves the tail determinant, full clearer, and complete gcd. It cancels the large tail norm only in the normalized analytic ratio; it does not assume that norm cancels arithmetically.

## 8. Limits, proportional extension, and handoff

The arithmetic gap is a bound or construction for the actual A_k=|I_k/g| meeting the explicit threshold. Neither guaranteed factorial content nor a saturated right subblock establishes it. This note does not identify g, compare the whole coefficient height with A_k, or couple different polynomials by resultants.

The remaining analytic term is below the linear scale. Explicitly, eta_k-(2/pi-log2)k lies between -c0 and E_k(d)+Bump_k. The bounded log theta_k remains present. No constant term or logarithmic term of the actual compact determinant is claimed. The earlier stage's statement that the compact linear coefficient was unresolved is replaced by Sections 4-6 of this revision; its two-term theorem and finite O(k) bounds remain valid.

The short-interval bump argument also works for pole order m proportional to the compact Gram dimension: its support length is O(sqrt(log k/m)), and its effective rank is O(k sqrt(log k/m)). However, for m<k the exact top coefficient still contains a (k-m)-dimensional determinant with weight sigma_m(y)(1+y)^(2m). That twisted determinant does not cancel as it does on the diagonal. This stage does not assert a proportional-regime k^2 coefficient without analyzing that additional object. This is the next analytic interface only if arithmetic results make it useful.

The appropriate present handoff is (31)-(32) on the actual primitive leading coefficient. Main owns different-polynomial coupling, and the arithmetic children own final content. The bounded stage is complete mathematically at author-proof level, subject to artifact receipt/readback and registration. Finite reference checks supplement the identities; they do not verify the inherited all-degree arithmetic or positivity theorem. No networking, installation, historical audit, or old regime exclusion was performed.
