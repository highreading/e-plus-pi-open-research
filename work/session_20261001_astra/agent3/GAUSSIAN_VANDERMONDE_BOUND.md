> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Gaussian Vandermonde refinement of the growing-degree absolute bound

Author: Agent 3. Status: proved analytic refinement, including all constants. This note preserves the completed b=1 certificate and growing-degree audit. It does not edit Agent 2's files or repeat the fixed-b theorem. No numerical computation or additional HP degree sample is used.

The proposed normalized Gaussian integral is correct. Replacing the old radial majorant by the actual squared Vandermonde improves the logarithm of the bounding expression, for d=b or b+1 and b=floor(n/2), by

    n^2 log(n)/8 + n^2/16 + O(n log n).

The improvement is independent of the contour radius. All asymptotic statements below concern explicit positive upper-bound expressions, not asymptotics or lower bounds for the determinants themselves.

## 1. Setup and functional domains

Use the actual system and complete-tail notation of work/session_20261001_astra/agent2/PROOF_DRAFT.md:

    ell_j(t^k)=1/(n+k+1-j)!, 0<=j<=b<=n,
    D_j=ell_(j+1)-ell_j,
    U0(t)=p_(n+1)(t),
    V(t)=K_n(t,1), W(t)=1/(1-t)-H(t),
    D_V=det[U;e;v], D_W=det[U;e;w], T=det[U;v;w].

Here the b-1 rows of U come from p_(n+1),...,p_(n+b-1), and the columns are indexed by ell_0,...,ell_b. The exact identities are Y=-D_V and Remainder(1)=D_W+T.

Respect the corrected domains throughout:

- A d-column difference determinant uses ell_0,...,ell_d, so 1<=d<=b.
- A d-column ordinary determinant uses ell_0,...,ell_(d-1), so 1<=d<=b+1.

No extension to negative factorial arguments is made. The applications use differences at d=b and ordinary functionals at d=b+1. This note applies those domains without duplicating Agent 2's source edit.

Let rho=1/20, R>20, S=d(d-1)/2, and a=2R/pi^2. Suppose P_i=U0 G_i and |G_i(t)|<=M_i on |t|<=rho, with G_i analytic on a neighborhood of the closed disk. Define

    C_G=d^(d/2) (product_i M_i) rho^d/(rho-1/R)^(d+S),

    E_n(R)=exp(R)(R+1)R^(-n-1)|U0(0)|(1+2/R)^(n+1).

These are exactly the factors already present in the audited bound. Only its Gaussian factor is changed.

## 2. Direct proof of the Gaussian integral

For a>0 define the monic Hermite polynomial

    h_j(x)=(-1)^j (2a)^(-j) exp(a x^2) (d/dx)^j exp(-a x^2), j>=0.

Repeated differentiation shows that exp(a x^2)(d/dx)^j exp(-a x^2) is a polynomial with leading coefficient (-2a)^j. Thus h_j is monic of degree j.

For any polynomial p, integration by parts j times gives

    integral_R h_j(x)p(x)exp(-a x^2) dx
      =(2a)^(-j) integral_R p^(j)(x)exp(-a x^2) dx.

All boundary terms vanish because they are polynomials times a decaying Gaussian. Consequently h_j is orthogonal to every polynomial of degree less than j, and

    integral_R h_j(x)^2 exp(-a x^2) dx
      = j!(2a)^(-j) sqrt(pi/a).                         (1)

For completeness, the one-dimensional Gaussian constant follows without a named integral evaluation. The square of its positive integral is the two-dimensional integral of exp(-a(x^2+y^2)); polar coordinates give

    [integral_R exp(-a x^2) dx]^2
      =2pi integral_0^infinity exp(-a r^2)r dr=pi/a.

Now prove the determinant integration identity used here. For finitely many functions f_i,g_j whose expanded products are integrable,

    integral ... integral det[f_i(x_k)] det[g_j(x_k)]
                          product_k w(x_k) dx_k
      =d! det[integral f_i(x)g_j(x)w(x) dx].             (2)

Expand both determinants as permutation sums. Each term factors into d one-variable integrals. Grouping the two permutations by their relative permutation gives the determinant on the right, with exactly d! identical groups. This proves (2) directly. In the present application all expanded terms are polynomial-Gaussian integrals and are absolutely integrable.

Monicity implies

    det[h_(j-1)(x_k)]_(j,k=1..d)
      =det[x_k^(j-1)]_(j,k=1..d)
      =Delta(x),

where Delta(x)=product_(k<l)(x_l-x_k). Apply (2) to these polynomials and w(x)=exp(-a x^2). The Gram matrix is diagonal by (1), so

    integral_(R^d) exp(-a sum x_k^2) Delta(x)^2 dx
      =d! product_(j=0)^(d-1) [j!(2a)^(-j)sqrt(pi/a)]
      =(pi/a)^(d/2)(2a)^(-S) product_(j=1)^d j!.        (3)

The last equality uses d! product_(j=0)^(d-1) j!=product_(j=1)^d j!.

Since S+d/2=d^2/2, division by (2pi)^d gives the proposed identity, with every constant retained:

    (2pi)^(-d) integral_(R^d) exp(-a sum x_k^2)Delta(x)^2 dx
      =(2pi)^(-d/2)(2a)^(-d^2/2) product_(j=1)^d j!.    (4)

For example, (4) gives 1/(2sqrt(pi*a)) at d=1 and 1/(4pi*a^2) at d=2. These are exact consequences of the formula, not numerical checks or HP degree samples.

The positivity used in this section is solely the positivity of an auxiliary real Gaussian integral. It asserts nothing about the original complex contour integrand.

## 3. Substitution into the contour bound

The audited difference determinant identity is

    det[D_j(P_i)]
      =1/[d!(2pi i)^d] integral ... integral
         det[P_i(1/z_k)] Delta(z)
         product_k [exp(z_k)(z_k-1)z_k^(-n-2) dz_k].     (5)

For the ordinary determinant omit z_k-1. Divided differences and Hadamard give

    |det[G_i(t_k)]|<=C_G |Delta(t)|.

On z_k=R exp(i theta_k), with -pi<=theta_k<=pi,

    |Delta(z)Delta(1/z)|
      =product_(k<l)|exp(i theta_l)-exp(i theta_k)|^2
      <=product_(k<l)(theta_l-theta_k)^2
      =Delta(theta)^2.                                 (6)

Also cos(theta)<=1-2theta^2/pi^2. The reference-polynomial, contour-length, and z-1 estimates therefore extract exactly E_n(R)^d from (5). Instead of replacing (6) by (2||theta||^2)^S, retain Delta(theta)^2. The remaining nonnegative Gaussian integral over [-pi,pi]^d is bounded by its integral over all R^d. Formula (4) evaluates that enlarged integral exactly.

Define the replacement factor

    J_VdM,d(R)
      =(2pi)^(-d/2)(4R/pi^2)^(-d^2/2) product_(j=1)^d j!.
                                                               (7)

The resulting inequalities are

    |det[D_j(P_i)]| <= C_G E_n(R)^d J_VdM,d(R)/d!,
       1<=d<=b,                                         (8)

    |det[ell_j(P_i)]| <= C_G [E_n(R)/(R+1)]^d
                               J_VdM,d(R)/d!,
       1<=d<=b+1.                                       (9)

The factors 1/d! in (8)-(9) are the original contour integration factors. In particular,

    J_VdM,d(R)/d!
      =(2pi)^(-d/2)(4R/pi^2)^(-d^2/2)
                        product_(j=1)^(d-1) j!.         (10)

The d! arising in the Gaussian Gram identity must not be counted a second time or omitted. Formula (10) makes the cancellation explicit; the product is empty and equals one at d=1.

The Gaussian integral evaluation is exact. The contour estimate still contains the absolute-value step, the chord-versus-angle inequality, the cosine majorant, divided-difference/Hadamard bounds, and enlargement of the integration domain. Equality for the Gaussian integral is not equality for the determinant.

## 4. Actual endpoint upper bounds

For the high rows choose

    M_l=(3/4)^(l-1), 1<=l<=b-1,
    H_b=product_(l=1)^(b-1) M_l
       =(3/4)^((b-1)(b-2)/2).

The empty product convention applies when b=1. Let M_V and M_W bound V/U0 and W/U0 on the same disk. Separate the row bounds from the remaining divided-difference factor by writing

    C_d(R)=d^(d/2) rho^(-S)
                       (1-1/(rho R))^(-(d+S)),
    C_G=C_d(R) product_i M_i.

The actual full-tail endpoint determinants satisfy

    |D_V| <= B_V := C_b(R) H_b M_V E_n(R)^b
                                      J_VdM,b(R)/b!,

    |D_W| <= B_W := C_b(R) H_b M_W E_n(R)^b
                                      J_VdM,b(R)/b!,

    |T| <= B_T := C_(b+1)(R) H_b M_V M_W
                    [E_n(R)/(R+1)]^(b+1)
                    J_VdM,b+1(R)/(b+1)!.                (11)

The column-difference sign in D_V,D_W is the common factor (-1)^(b+1); it disappears from these absolute bounds. The companion T retains both V and W and uses ordinary functionals. Its extra row does not justify division by D_V or a claim that T/D_V is small.

## 5. Exact comparison with the old radial factor

Write the old factor as

    J_rad,d(R)
      =2^S a^(-S-d/2) pi^(d/2) Gamma(S+d/2)
                      /[(2pi)^d Gamma(d/2)].

Using S+d/2=d^2/2 and (4), all powers of a and pi cancel from the ratio:

    J_rad,d(R)/J_VdM,d(R)
      =2^(d(d-1)) Gamma(d^2/2)
          /[Gamma(d/2) product_(j=1)^d j!].              (12)

This exact ratio is independent of R. It equals one at d=1 and exceeds one for d>=2, since the old radial majorant is strictly larger on a set of positive measure. For example, its exact values at d=2 and d=3 are 2 and 70.

For identical choices of R, U0, and M_i, (12) is also the ratio of the old and new complete upper-bound expressions. This includes the ordinary companion bound: its unchanged factors cancel in precisely the same way.

Let P_d=product_(j=1)^d j!. The exact logarithmic improvement is

    L_d=log(B_old/B_new)
       =d(d-1)log 2 + log Gamma(d^2/2)
          -log Gamma(d/2)-log P_d.                      (13)

## 6. Justified factorial and Gamma estimates

Here elementary estimates suffice; no unevaluated dimension constant or named multiple integral is used.

For a twice differentiable real f, the trapezoidal error on consecutive unit intervals satisfies

    sum_(k=1)^m f(k)
      =integral_1^m f(x)dx + [f(1)+f(m)]/2 + E_f,
    |E_f| <= (1/8) integral_1^m |f''(x)|dx.

This follows by integrating twice against the kernel
(x-k)(k+1-x)/2 on each interval [k,k+1]. The sign of the error is the sign of f'' when f'' has constant sign.

Apply this to f=log x. For every integer m>=1,

    log(m!)=(m+1/2)log m-m+c_m, 7/8<=c_m<=1.            (14)

Apply it to f=x log x:

    sum_(k=1)^d k log k
      =(d^2/2+d/2)log d-d^2/4+1/4+E_d,
    0<=E_d<=(log d)/8.                                  (15)

Summing (14) and using (15) yields

    log P_d=(d^2/2)log d-3d^2/4+d log d+O(d).            (16)

The error here is explicitly bounded. If F_d denotes the three displayed terms on the right of (16), then

    F_d-d/8+(log d)/4+11/16
       <=log P_d<=F_d+3(log d)/8+3/4.                   (17)

These inequalities also cover d=1. Thus the error statement in (16) is uniform in dimension.

For the Gamma factors only integer and half-integer arguments occur. The recurrence from its defining integral and the one-dimensional Gaussian evaluation give

    Gamma(m+1)=m!,
    Gamma(m+1/2)=(2m)!sqrt(pi)/(4^m m!), m>=0.

Substituting (14) into these exact identities, and using
u/(1+u)<=log(1+u)<=u for u>=0, gives uniformly on this integer/half-integer set

    log Gamma(x)=(x-1/2)log x-x+O(1).                   (18)

For integer x this follows directly from log Gamma(x)=log(x!)-log x. For x=m+1/2 with m>=1, the difference from the main expression in (18) is exactly

    (1/2)log(2pi)+1/2-m log(1+1/(2m))+c_(2m)-c_m,

which is bounded independently of m. The single value x=1/2 is harmless. This justifies (18) without assuming a dimension-dependent Stirling remainder.

Insert (16) and (18) into (13). The result, including the next logarithmic term, is

    L_d=(d^2/2)log(2d)+d^2/4
                        -(3d/2)log d+O(d).             (19)

In particular the leading improvement is (d^2/2)log d, rather than merely an exponential-in-d constant.

## 7. The regime b=floor(n/2), R=lambda n

Fix lambda>0 and take n sufficiently large that R=lambda n>20. Both applications have d=n/2+O(1). Formula (19) gives

    log(B_old/B_new)
      =n^2 log n/8+n^2/16+O(n log n).                   (20)

The O(n log n) permits the parity and d=b versus d=b+1 shifts. The exact formula (13), or the finer d-form (19), retains those shifts when needed. Neither (13) nor (19) depends on lambda.

Independently, (7) and (16) give

    log J_VdM,d(R)
      =(d^2/2)log(pi^2 d/(4R))-3d^2/4
                                      +d log d+O(d),   (21)

    log[J_VdM,d(R)/d!]
      =(d^2/2)log(pi^2 d/(4R))-3d^2/4+O(d).             (22)

Thus, for either actual dimension,

    log[J_VdM,d(lambda n)/d!]
      =(n^2/8)log(pi^2/(8lambda))-3n^2/16+O_lambda(n).
                                                               (23)

Without the outside 1/d!, the right side of (23) acquires
(n/2)log n+O(n). There is no n^2 log n term in the new Gaussian factor.

For comparison, the old factor satisfies

    log J_rad,d(R)
      =(d^2/2)log(pi^2 d^2/(2R))-d^2/2
                                     -(d/2)log d+O(d), (24)

and hence

    log J_rad,d(lambda n)
      =n^2 log n/8+(n^2/8)log(pi^2/(8lambda))
                         -n^2/8+O_lambda(n log n).      (25)

Equations (20)-(25) quantify exactly which leading Gaussian loss disappears.

## 8. Complete normalization ledger

For either determinant type put eta=1 for differences and eta=0 for ordinary functionals. With positive row bounds M_i, the logarithm of the new bounding expression is exactly

    log B_new
      = [d log d/2 + sum_i log M_i
                      -S log rho-(d+S)log(1-1/(rho R))]
        + [dR-(n+1)d log R+eta*d log(R+1)]
        + d log|p_(n+1)(0)|
        + (n+1)d log(1+2/R)
        - (d/2)log(2pi)-(d^2/2)log(4R/pi^2)
        + sum_(j=1)^d log(j!) - log(d!).                (26)

The first bracket is log C_G, including every analytic row bound. The next three terms together are d log E_n for differences, or d log(E_n/(R+1)) for ordinary functionals. The Gaussian and outside factorial factors are separately visible in the last line.

For the present endpoint rows,

    sum_i log M_i=((b-1)(b-2)/2)log(3/4)
                  + log M_V,                          for D_V,

with log M_W in place of log M_V for D_W, and with log M_V+log M_W for T.

Here are fully explicit choices showing that the analytic factors hide no n^2 log n cost. The recurrence and beta_k<=1/12 give ||p_k||_1<=2^k by induction. Also

    1/|h_k| <= (2k+1)16^k/2.

Consequently, on |t|<=rho,

    |V(t)| <= (n+1)^2 64^n/2.

On the original integration segment s=(1+iu)/2, |s|<=1/sqrt(2) and |1/(1-s)|<=2. Thus

    |L(p_k/(1-t))|<=4*2^k,
    |H(t)|<=2(n+1)^2 64^n.

The audited small-disk reference bound |U0(t)|>=(9/20)^(n+1) therefore permits

    M_V=(20/9)^(n+1) (n+1)^2 64^n/2,
    M_W=(20/9)^(n+1) [20/19+2(n+1)^2 64^n].             (27)

Both have logarithm O(n). Only one or two such special rows occur; the other rows use the sharper adjacent-ratio product H_b. These estimates need no numerical evaluation or rationality assumption on H.

The roots of the monic U0 are (1+iu_k)/2 with |u_k|<1. Their moduli lie between 1/2 and 1/sqrt(2). In particular,

    2^(-(n+1)) <= |p_(n+1)(0)| <= 2^(-(n+1)/2).         (28)

Thus its exact contribution in (26) is of order n^2 when d is of order n, with no n^2 log n contribution.

The remaining entries of (26), for R=lambda n, have the following scales:

| Factor | Logarithmic contribution |
|---|---|
| Contour exponential and powers | -dn log n+dn(lambda-log lambda)+(eta-1)d log R+O_lambda(1) |
| Reference value | d log|p_(n+1)(0)|, bounded explicitly by (28), of order n^2 |
| Reciprocal-root correction | (n+1)d log(1+2/R)=O_lambda(n) |
| Hadamard | (d/2)log d=O(n log n) |
| Fixed disk radius | -S log rho=(n^2/8)log20+O(n) |
| Gap from contour to disk | -(d+S)log(1-1/(rho R))=O_lambda(n) |
| High analytic rows | ((b-1)(b-2)/2)log(3/4)=(n^2/8)log(3/4)+O(n) |
| Special analytic rows | log M_V, log M_W, or their sum: O(n) using (27) |
| New Gaussian | Formula (21), with no n^2 log n at d proportional to R |
| Outside integration factorial | -log(d!)=-d log d+d+O(log d) |

For the disk-gap estimate, take n large enough that x=1/(rho lambda n)<=1/2 and use x<=-log(1-x)<=x/(1-x). The fixed-radius cost rho^(-S) remains exp(O(n^2)); it has not been discarded.

With the explicit choices (27), all three positive bounding expressions in (11) consequently satisfy

    log B_new=-n^2 log n/2+O_lambda(n^2).                (29)

The old radial versions of the same expressions instead satisfy

    log B_old=-3n^2 log n/8+O_lambda(n^2).               (30)

These are cofactor-normalization absolute bounds. Their very small scale does not imply that the endpoint-normalized remainder is small.

The source of the removed loss is precise. The radial Gamma factor has
log Gamma(d^2/2)=d^2 log d+O(d^2), whereas the actual Vandermonde contributes
log P_d=(d^2/2)log d+O(d^2). When d is proportional to R, the latter cancels the Gaussian radius term -(d^2/2)log R at the n^2 log n scale. The former leaves the spurious positive n^2 log n/8 term. The factor 2^(d(d-1)) in (12) changes the n^2-scale constant, not that leading logarithmic coefficient. The reference, analytic, disk, Hadamard, and 1/d! factors have the separate scales displayed above.

## 9. Remaining gaps and stopping boundary

The new bounds improve absolute control of D_V, D_W, and T. They do not provide a lower bound for |D_V|, nonvanishing of D_V, or nonvanishing of D_W+T. They do not assert positivity of the original complex contour integrand.

For the actual positive reduced denominator q, the exact normalization still requires

    |L|=q |D_W+T|/|D_V|,

whenever D_V!=0. A sufficient shrinking criterion remains

    D_V!=0, D_W+T!=0,
    q(B_W+B_T)/|D_V| ->0

on an unbounded index set. None of the new Gaussian identities establishes those hypotheses. In particular, dividing one absolute upper bound by another cannot bound the determinant quotient. A common small cofactor scale can occur in numerator and denominator and cancel from the endpoint ratio. The actual endpoint gcd and reduced q remain separate arithmetic questions.

No additional HP degrees, prime scans, network searches, installations, or historical edits were performed. The task stops at the exact Gaussian replacement, its quantified logarithmic improvement, and these remaining normalization gaps.
