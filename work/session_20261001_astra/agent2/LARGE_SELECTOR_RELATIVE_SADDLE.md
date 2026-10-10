> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A relative saddle theorem for the upper endpoint integral

Status: new author analytic proof, not independently reviewed. LARGE_SELECTOR_BLOCK_NONCANCELLATION.md and its proved high-high adjacent-pair selection are preserved without replay. No numerical computations or old checks are performed. The final primitive-denominator consequence uses the separate main author arithmetic and complete-exponential results in their stated scopes.

## 1. Result and precise regime

Put

    alpha=(1+i)/2, V(w)=w^2-w+1/2,
    A(w)=(2w^2-1)^2,
    G_m(w)=V(w)^n A(w)^m/w^(n+1),
    J_m=integral_(1/2)^alpha G_m(w)dw.

The defining path is the straight segment. All powers in G_m are integer powers. Fix rho>0 and a fixed block constant C. Uniformly for integers

    n -> infinity,
    |m-rho n log n| <= C n log n/log log n,

this note proves

    log|J_m|=m log 2-n log(m/n)+O_rho,C(n),             (1)
    J_(m+1)/J_m=-2i[1+O_rho,C(1/log n)].             (2)

In particular J_m is nonzero throughout these blocks for all sufficiently large n. The analytic theorem does not require n to be dyadic. The dyadic restriction enters only when combining it with the saved parity and large-forcing selection.

A stronger relative formula, including the exact complex phase and a uniform O(1/n) relative remainder, is given below. Formula (1) is not obtained by dividing the saved absolute integral majorant by another upper bound.

## 2. Exact endpoint scaling

Set

    lambda=n/m, nu=1/n,
    w=alpha-i x/2=alpha(1-alpha x), 0<=x<=1,
    C0(x)=1-x+(1+i)x^2/4.

Direct algebra gives

    V(w)=(x/2)(1-x/2),
    2w^2-1=(i-1)C0(x),
    A(w)=(-2i)C0(x)^2.

The orientation of the original path gives the exact identity

    J_m=P_(n,m) integral_0^(1/lambda) exp(n phi(t))dt,   (3)

where

    P_(n,m)=[i/(2alpha)](2alpha)^(-n)(-2i)^m
                  lambda^(n+1),

    phi(t)=log t+(2/lambda)log C0(lambda t)
            +log(1-lambda t/2)
            -(1+nu)log(1-alpha lambda t).             (4)

Here x=lambda t. For positive t near the saddle, log t is the branch real on the positive axis. The remaining logarithms are their analytic branches equal to zero at lambda t=0. Away from that neighborhood equation (3) can always be interpreted through the original integer powers. No logarithm branch is used to change the original integral.

At lambda=0 define the removable parameter limit

    phi_0(t)=log t-2t.

The scaled saddle therefore has a finite nondegenerate limit t=1/2, even though the original saddle approaches the endpoint alpha.

## 3. The exact saddle and a correction to its earlier provisional location

For all sufficiently small positive lambda and 0<=nu<=1, the equation phi'(t)=0 has a unique solution t_s in a fixed small disk about 1/2. It is analytic in lambda and nu and satisfies

    t_s=1/2+O(lambda),
    beta=-phi''(t_s)=4+O(lambda).

All constants here and in the local analytic estimates below are uniform in nu in [0,1]. Define

    w_s=alpha-i lambda t_s/2.

This is the EXACT root near alpha of

    n V'(w)/V(w)+m A'(w)/A(w)-(n+1)/w=0.             (5)

Equivalently it solves

    n(2w^2-1)^2+16m w^2 V(w)-2V(w)(2w^2-1)=0.       (6)

The n+1 in (5) is retained in (4), through nu. It is not replaced by n in the relative formula.

In particular A'(alpha)/A(alpha)=-4i. Consequently

    w_s=alpha-i lambda/4+O(lambda^2).                (7)

The earlier provisional large-degree reduction listed alpha+1/(8kappa), kappa=m/n, as the leading displacement. That location is not a root to the asserted order. Equation (7) records the corrected leading displacement as part of the present exact-saddle analysis; the older file is preserved. No conclusion here uses its provisional root expansion.

For clarity about the phase size, expansion of the explicit analytic function gives

    t_s=1/2+lambda[-1/8+i/4+nu alpha/4]+O(lambda^2),
    phi(t_s)=-log 2-1
          +lambda[-1/8+3i/8+nu alpha/2]+O(lambda^2).  (8)

These expansions explain the scales only. In particular n Im phi(t_s) has a correction of order n lambda=n^2/m, which diverges in the requested regime. Every finite further truncation can also leave an unbounded exponent error. The theorem uses the exact t_s and exact phi(t_s), not a fixed-order replacement from (8).

## 4. Global tails on the original segment

The following bounds control contributions away from the scaled saddle before any contour deformation. With y=1-x, 0<=x<=1, one has

    |A((1+iy)/2)|=(1+6y^2+y^4)/4.

This convex polynomial lies below its endpoint chord, so

    |A(w)/(-2i)|<=1-7x/8<=exp(-7x/8).

Also

    |(1-x/2)/(1-alpha x)|<=1,
    |1-alpha x|^(-1)<=sqrt(2).

The first follows by comparing (1-x/2)^2 with
|1-alpha x|^2=1-x+x^2/2. Thus the modulus of the integrand in (3) is at most

    sqrt(2) t^n exp(-7nt/8), 0<=t<=1/lambda.         (9)

Fix a=1/16 and B=8. For lambda small enough that B<1/lambda, the two real tails satisfy

    integral_0^a |exp(n phi(t))|dt
       <=sqrt(2) a^(n+1)/(n+1),

    integral_B^(1/lambda) |exp(n phi(t))|dt
       <=[4sqrt(2)/(3n)] exp(n(log 8-7)).            (10)

The second inequality uses the derivative bound
(d/dt)(log t-7t/8)<=-3/4 for t>=8.

Since Re phi(t_s)=-log 2-1+O(lambda), both bounds are exponentially smaller than exp(n Re phi(t_s))/sqrt(n), uniformly as lambda tends to zero. This controls the midpoint side of the path and all its distant parts. It does not rely on claiming that every stationary point of the global quartic contributes to this particular open contour.

## 5. Permissible local deformation and exclusion of competing contributions

On a fixed rectangle containing [a,B] and a small imaginary neighborhood, the logarithms in (4) are analytic when lambda is sufficiently small. Their arguments remain close to one; t stays away from zero. The corresponding w points remain near the upper part of the original segment and away from the sole pole w=0.

The following elementary uniform estimates can be imposed simultaneously by decreasing a fixed positive lambda_0:

    |t_s-1/2|<=3lambda,
    |Im t_s|<1/64,
    phi(t)=phi_0(t)+O(lambda),
    phi''(t)=-1/t^2+O(lambda),                         (11)

on the relevant compact rectangles. Derivatives through order six are uniformly bounded on a neighborhood of the small saddle disk. These statements follow directly from the polynomials and logarithms in (4), whose denominators are bounded away from zero there. They involve fixed analytic constants, not a norm of the unknown integral.

For existence and uniqueness of t_s, one may apply Rouché to phi' and 1/t-2 on |t-1/2|=1/100, then use the nonzero derivative -4 at lambda=0. Analytic dependence follows from the implicit function theorem, uniformly for nu in the compact interval [0,1].

Deform the segment [a,B] to the horizontal segment from a+i Im t_s to B+i Im t_s, with the two short vertical connectors. Cauchy's theorem applies in the rectangle just described. Under the w map this is a deformation avoiding zero, so it changes neither the original open-path homotopy class nor the integral.

Along the horizontal segment, write t=t_s+r with r real. The real part has its derivative zero at r=0. Moreover the second derivative is uniformly strictly negative. To see this quantitatively, for a<=u<=8 and |v|<=1/64,

    Re(1/(u+iv)^2)>1/100.

A slightly smaller positive constant absorbs the O(lambda) perturbation in (11). Hence, after decreasing lambda_0 if necessary, there is an absolute c>0 such that

    Re phi(t_s+r)<=Re phi(t_s)-c r^2                (12)

throughout the horizontal segment. The vertical connectors have real phase separated below Re phi(t_s) by a fixed positive gap, by continuity from phi_0 at a and B.

This proves a single dominant saddle on the deformed central contour. The real tails were already controlled by (10). Together these facts control all competing contributions for J_m. In particular neither the small roots near w=0 nor the lower conjugate endpoint can add an uncontrolled contribution to this upper-endpoint integral. No unproved global steepest-descent contour decomposition is needed.

## 6. Uniform relative saddle formula

Choose the square root beta^(1/2) continuously from beta=4, so it tends to the positive value 2. The horizontal contour has its orientation from left to right. Uniform saddle integration gives

    J_m=P_(n,m) exp(n phi(t_s))
                sqrt(2pi/n) beta^(-1/2)(1+e_(n,m)),
    |e_(n,m)|<=C_1/n,                                (13)

for n>=n_0 and 0<lambda<=lambda_0, with absolute constants C_1,n_0,lambda_0. The constants are independent of m and of nu=1/n in this domain.

Here are the relative-error details. Split the horizontal contour into a fixed small symmetric interval about t_s and its complement. Equation (12) makes the latter exponentially smaller. On the symmetric interval expand phi through fourth order. After r=u/sqrt(n), the cubic term has coefficient O(n^(-1/2)), and its first-order integral vanishes by oddness. The quartic term and the square of the cubic term have Gaussian integrals O(1/n). The uniformly bounded higher derivatives control the remaining Taylor terms. One may first restrict to |r|<=n^(-2/5), where the cubic exponent is uniformly small, and use (12) to bound the rest by exp(-c n^(1/5)). The complex Gaussian has Re beta bounded below and beta bounded away from zero, so its integral is exactly sqrt(2pi) beta^(-1/2), with the specified branch. These estimates give an absolute O(1/n) multiple of that nonzero Gaussian integral. The connectors and (10) are exponentially smaller and are absorbed into the same relative bound.

Thus (13) has a genuine relative remainder. It is not an additive enclosure on the saved absolute majorant. It proves J_m!=0 once n is sufficiently large. All phases in P_(n,m), phi(t_s), and beta^(-1/2) are specified. In particular the integer factor (-2i)^m and the exact adjusted m are retained.

Taking moduli in (13) yields the more informative exact-phase budget

    log|J_m|=m log 2+(n+1)log lambda
       -(n+1)log 2/2+n Re phi(t_s)
       +log(2pi/n)/2-log|beta|/2+O(1/n).             (14)

Since phi(t_s)=-log 2-1+O(lambda), equation (14) proves (1) uniformly in the requested blocks. The logarithms of lambda and n in the prefactor are negligible compared with the allowed O_rho,C(n) term. The exact phase remains indispensable for any particular node's imaginary part.

## 7. Consecutive m: a relative quarter turn

Keep n fixed. Write F(lambda,nu)=phi(t_s(lambda,nu);lambda,nu). Analyticity on a fixed parameter neighborhood gives uniformly bounded derivatives of F and beta with respect to lambda. For the next integer m,

    lambda'=n/(m+1)=lambda/(1+lambda/n),
    lambda'-lambda=O(lambda^2/n).

Taking the ratio of the two nonzero formulas (13) gives

    J_(m+1)/J_m=(-2i)(lambda'/lambda)^(n+1)
       exp(n[F(lambda',nu)-F(lambda,nu)])
       [beta(lambda,nu)/beta(lambda',nu)]^(1/2)
       [1+O(1/n)].                                   (15)

All roots and branches are the same analytic continuations as above. Now

    n[F(lambda',nu)-F(lambda,nu)]=O(lambda^2),
    (n+1)log(lambda'/lambda)=-(1+nu)lambda+O(lambda^2/n),
    beta(lambda',nu)/beta(lambda,nu)=1+O(lambda^2/n).

Consequently

    J_(m+1)/J_m
       =-2i exp(-(1+nu)lambda+O(lambda^2+1/n))
       =-2i[1+O(lambda+1/n)].                       (16)

The O in the exponent can be complex. In particular the phase increment is -pi/2+O(lambda^2+1/n), modulo 2pi. This proves (2), uniformly even when m differs from rho n log n by the full allowed adjustment. The large absolute phase corrections in (8) have not been discarded; only their controlled adjacent difference has been used.

For all sufficiently large n, (16) implies

    |J_(m+1)+2i J_m|<=|J_m|/2.

Taking real and imaginary parts then proves

    max(|Im J_m|,|Im J_(m+1)|)>=|J_m|/2.             (17)

For example apply the Euclidean triangle inequality to
(Im J_m,Im J_(m+1)/2)=(Im J_m,-Re J_m)+(0,error/2).
This establishes adjacent noncancellation relative to the actual integral, closing the specific gap left by the absolute remainder in the preserved block note.

## 8. Combining with the preserved high-high selection

Now take n=2^s. Use exactly the eligible block and dyadic h in LARGE_SELECTOR_BLOCK_NONCANCELLATION.md. Its proved counting theorem supplies at least h(n-8) edges (m,m+1) for which BOTH nodes are parity eligible and

    |U(n,j)|>=T=(2h)^(n/2), j=m,m+1.

All these nodes satisfy the requested enlarged adjustment. The preserved uniform upper bound H_U gives

    |U(n,j)|<=H_U,
    log H_U=(n/2)log log n+O_rho(n),
    log T=(n/2)(log log n-log log log n)+O(n).         (18)

Thus both endpoints of each edge retain their established large-forcing size. Their nonvanishing and exact dyadic valuation are used in the stated author-input scope.

The complete logarithmic error of the direct forcing quotient is exactly

    beta_(n,j)-pi=(-1)^(n+1)2^(n+2) Im J_j/U(n,j).   (19)

For EVERY such high-high edge, equations (1), (17), and (18) prove that at least one endpoint has

    log|beta_(n,j)-pi|
       >=m log 2-(3n/2)log log n-O_rho(n).           (20)

The choice between m and m+1 changes m log 2 by only an absolute constant. This is a lower bound on the actual normalized logarithmic error, not on a raw numerator.

The complete exponential author input retained in the block note supplies at both high nodes

    |alpha_(n,j)-e|<=Bstar,
    log Bstar<=-n log n+(n/2)log log n
                   +(n/2)log log log n+O_rho(n).    (21)

For each fixed rho>0, the lower bound (20) tends to positive infinity at scale rho log 2 n log n, whereas (21) tends to zero. The complete exponential contribution therefore cannot cancel the large logarithmic error at the selected endpoint. In particular, for every high-high edge at least one endpoint has a complete-error lower bound of the form (20), with a changed O_rho(n) constant.

## 9. An explicit finite selection rule independent of e and pi

To make an unbounded selected sequence precise, choose the first high-high edge in the already specified block. Use the finite Gaussian-rational endpoint sums Z_j and common truncation depth from the preserved block note; their absolute errors satisfy |J_j-Z_j|<=Rstar. Choose the endpoint j with the larger rational quantity

    |Im(Z_j/U(n,j))|,

breaking ties toward the smaller integer. No such finite search is executed in this work; this defines the sequence mathematically.

The difference between each compared value and |Im(J_j/U(n,j))| is at most Rstar/T. Hence the selected endpoint's actual value is at least the maximum actual value minus 2Rstar/T. The latter error is exponentially smaller than (20). This selection therefore inherits the complete lower bound, and both its forcing size and parity remain guaranteed.

At the selected node, the upper bound (1), the lower forcing bound T, and (21) also give

    log|c_(n,j)-(e+pi)|
       <=j log 2-(3n/2)log log n
                     +(n/2)log log log n+O_rho(n).

Together with (20), this proves the scoped statement

    log|c_(n,j)-(e+pi)|
       =j log 2-(3/2+o(1))n log log n,               (22)

and in particular

    log|c_(n,j)-(e+pi)|/(n log n) -> rho log 2>0.    (23)

The exact j, including its enlarged adjustment, is retained in (22). Replacing j by rho n log n in that subleading formula would not be justified. Formula (23) permits that replacement only at its stated leading scale.

This selected rational quotient fails even to approximate e+pi: its complete error diverges. The assertion concerns the specified finite selection, and at least one endpoint of each guaranteed high-high edge. It does not assign a fixed sign or a large error to every node of the block, or to the original U-only maximizing node.

## 10. Actual primitive denominator consequence

Let q_(n,j) be the ACTUAL reduced positive denominator of the complete direct quotient. The main dyadic author theorem on eligible nodes gives

    v2(q_(n,j))=3n/2+2j-s2(n)-s2(n+4j).

Accordingly the complete primitive integer form has the lower bound

    log(q_(n,j)|c_(n,j)-(e+pi)|)
       >=3j log 2-(3n/2)log log n-O_rho(n).          (24)

The binary digit sums contribute only O(log(n+j)); the remaining linear terms are absorbed into O_rho(n). Thus

    liminf log(q_(n,j)|c_(n,j)-(e+pi)|)/(n log n)
       >=3rho log 2.                               (25)

This uses the actual compulsory dyadic denominator cost, not the size of U or a coefficient clearer. Even without that arithmetic input, q>=1 and (23) already imply divergence of the selected primitive forms. Equation (25) supplies the stronger conditional rate.

No claim about odd denominator cancellation is needed. No irrationality conclusion follows: this is a scoped failure result for the selected large-degree rational approximants, not a construction of small nonzero forms. It does not exclude all selectors, all parity-eligible nodes, or new rational combinations.

## 11. What is new and what remains outside the conclusion

The two requested targets are proved for the explicit integral: a uniform relative one-saddle formula with its exact phase, and a uniform relative adjacent quarter turn. The local deformation, original-path tails, and central Gaussian remainder control all contributions relevant to this upper-endpoint integral.

The exact saddle direction in (7) corrects an earlier provisional root location. Its full displacement and phase are retained through the implicit analytic root in (13); the growing n^2/m phase term is not ignored. No fixed-order Watson approximation is used.

Combining this theorem with the preserved high-high selection closes its previous noncancellation gap for at least one endpoint of every such edge. The full exponential residual is included, and the actual primitive denominator is used only through its separately stated author theorem. The resulting selected family has divergent complete errors and divergent primitive forms, with the scopes in (22)-(25).

No independent review or repeated computations were performed. The old block theorem and other saved records are unmodified. This file and LARGE_SELECTOR_RELATIVE_SADDLE_REPORT.md require actual read-back before completion is reported.
