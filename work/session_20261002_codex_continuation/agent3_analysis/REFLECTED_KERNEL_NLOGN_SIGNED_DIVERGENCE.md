> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Complete signed divergence of the reflected repair at depth n log n

2026-10-02. Original author theorem, Agent 3. The target/prior-art gate, queries, URLs, and method overlap are saved in `REFLECTED_KERNEL_SIGNED_ERROR_PROGRESS.md`. The exact construction, all-h positive determinant, and final-denominator arithmetic belong to Agent 2's `REFLECTION_DISTRIBUTED_POLE_REPAIR.md`. This note proves the complete analytic behavior in one growing-depth regime. It is a construction-specific theorem, not a statement about rationality of e+pi.

## Theorem

Let n=4k tend to infinity and let h/(n log n) tend to a fixed kappa in (0,infinity). Put N=n+h and R=sqrt(N/n). Use Agent 2's ACTUAL kernels and projection:

    q(w)=1-2w+2w^2,
    F0=q(w)^N/[w^(N+1)(1-w)^h], F1=wF0,
    Ri=Res0 Fi-Res1 Fi,
    Ai=Res1(e^(w-1)Fi), Bi=Res0(e^w Fi),
    T=(h-1)!, mi=T(Ai-Ri), F=m1 F0-m0 F1,
    U=T(A1R0-A0R1)>0.

Let epsilon=(-1)^h, X_l=N-2l, and define the positive quantities

    D=sum_(X_l>=0) binom(N,l) binom(X_l+n,n),
    D1=sum_(X_l>=1) binom(N,l) binom(X_l+n,n+1),
    C=sum_(X_l>=n+1) binom(N,l) binom(X_l-1,n),
    E=sum_(X_l>=n+1) binom(N,l) binom(X_l,n+1),
    B(z)=sum_(X_l>=0) binom(N,l) L_(X_l)^(n)(z),
    A=sum_(X_l>=n+1) binom(N,l) L_(X_l-n-1)^(n)(-1),
    Aplus=sum_(X_l>=n+1) binom(N,l) L_(X_l-n-1)^(n+1)(-1),
    r=D1/D.

Here L denotes the standard generalized Laguerre polynomial. Then r/R tends to 1, B(1)>0 eventually, and

    U/T = 2R D A (1+o(1)),                                      (1)
    alpha=-B(F)/U = [R/(4n)] [D/A] exp(-r) (1+o(1)) > 0,       (2)
    |pi-beta| <= exp[-n log R+O(n)],                            (3)
    c-(e+pi) = [R/(4n)] [D/A] exp(-r) (1+o(1)) -> +infinity. (4)

In particular the complete signed error satisfies

    log(c-(e+pi)) = (1+o(1)) n/R,
    [sqrt(log n)/n] log(c-(e+pi)) -> 1/sqrt(kappa).              (5)

The factors D/A and exp(-r) in (4) are retained rather than replacing their subleading, diverging logarithms by a formal expansion. This gives a complete positive leading expression with relative error tending to zero. Both actual rational primitive endpoints and both exponential poles enter the argument.

## 1. Exact finite-sum interface

At the origin write H0(w)=q(w)^N/(1-w)^h. The identity

    q(w)^N=sum_l binom(N,l) w^(2l)(1-w)^(2N-2l)

gives H0 coefficients (-1)^j times positive finite binomial sums up to degree N. At w=1+s use q(1+s)=(1+s)^2+s^2. Direct coefficient extraction gives

    Res0 F0=epsilon D, Res0 F1=-epsilon D1,
    Res1 F0=epsilon C, Res1 F1=epsilon E,
    R0=epsilon(D-C), R1=-epsilon(D1+E).

The Laguerre finite series, with the same coefficient extraction, gives EXACTLY

    B0=epsilon B(1), B1=epsilon B'(1),
    B(0)=D, B'(0)=-D1,
    A0=epsilon A, A1=epsilon Aplus.                            (6)

For example, the k-th exponential term at the origin is

    (-1)^k binom(X_l+n,n+k)/k!,

which is L_(X_l)^(n)(1). At pole 1 it is binom(X_l-1,n+k)/k!, which is L_(X_l-n-1)^(n)(-1). Multiplication by w at pole 1 changes the top to X_l, hence the parameter to n+1 without changing degree. No large circle is falsely treated as a contour around only one pole.

The exact projection numerator is

    B(F)/T = D1 B(1)+D B'(1)
               +Aplus B(1)-A B'(1)+E B(1)-C B'(1).             (7)

The first pair in (7) contains a cancellation that determines the sign.

## 2. Positive binomial concentration, including the variance

For X in the lattice {N,N-2,...} with X>=0, the D weights are

    p_D(X)=binom(N,(N-X)/2) product_(j=1)^n (X+j)/n!.

Their smooth logarithmic extension has derivatives in a neighborhood X~nR:

    (log p_D)'(X)=-atanh(X/N)+sum_(j=1)^n 1/(X+j)+O(1/N),
    (log p_D)''(X)=-1/[N(1-(X/N)^2)]
                    -sum_(j=1)^n 1/(X+j)^2+O(1/N^2).

The unique mode satisfies X_*=nR(1+O(1/R)); its curvature is -(2+o(1))/N. The third derivative in a fixed relative neighborhood is O(1/(NR)+1/(N nR)), and more precisely the product part is O(n/X_*^3), while the binomial part is O(X_*/N^3). Multiplied by N^(3/2), both tend to zero. The lattice spacing 2 is negligible compared with sqrt(N).

Strict concavity, the displayed derivatives, and Stirling's formula give a local Gaussian law of variance N/2 and exponentially small mass outside any fixed relative neighborhood of X_*. For the product weight, the endpoint X<=n contributes at most 2^N exp[O(n)], whereas a central term has size 2^N R^n exp[O(n)]. Thus that omitted endpoint is exponentially negligible. Tail moment estimates follow by the same concavity bound. Consequently

    E_D X = nR(1+O(1/R)),
    Var_D X = (N/2)(1+o(1)),
    E_D |X-E_D X|^j=O(N^(j/2)), j=3,4.                       (8)

These statements hold uniformly if the weights are multiplied by exp(t X/(n+1)) for bounded t. That tilt shifts the mode by O(N/n)=O(R^2), small compared with X_*, and does not change the leading curvature. They also hold for the C weights (replace X+j by X-j and restrict X>=n+1), and for the interpolation products product_(j=1)^n(X+t j), -1<=t<=1, on that restricted range. The endpoint omission remains negligible there. These observations supply the uniform Laplace claims used below.

For completeness, integrating the interpolation derivative gives a sharper response comparison without discarding a large bias:

    log(D/C)=integral_(-1)^1 E_t sum_(j=1)^n j/(X+t j) dt
             +o(1)
            =(1+o(1)) n/R.                                  (9)

Uniform concentration places X=nR(1+o(1)), so the integrand is (1+o(1)) n/(2R). The negligible D mass with X<=n cannot change (9).

## 3. Uniform Laguerre logarithmic expansion

Normalize Q_m(z)=L_m^(n)(z)/binom(m+n,n), and put mu=m/(n+1). For 0<=m<=N and |z|<=1, all its roots are positive, and the reciprocal power sums obtained from the Laguerre differential equation are

    s1=mu,
    s2=(mu^2+mu)/(n+2),
    s3=(2mu+1)(mu^2+mu)/[(n+2)(n+3)].

Since max mu=O(log n), s2=O(log^2 n/n) tends to zero. The smallest root is at least s2^(-1/2), so it is greater than 1 eventually. Expanding the product over positive roots, including two z derivatives, proves uniformly

    log Q_m(z)=-mu z-(s2/2)z^2+O(s3),
    (log Q_m)'(z)=-mu-s2 z+O(s3),
    (log Q_m)''(z)=-s2+O(s3).                              (10)

The remainder bounds follow from s_k<=s3 lambda_min^(-(k-3)) for k>=3. This argument is valid simultaneously for every m up to N and supplies eventual positivity on [0,1]. It does not use a fixed-separated-turning-point asymptotic outside its domain. The Laguerre definition, equation and positive-zero facts are standard; the fresh primary/reference readings are documented in the progress note, with the additional zero reference https://dlmf.nist.gov/18.16.

Now B(z)=D E_D Q_X(z). The measure tilted by Q_X(z) remains a positive measure. Equation (10) writes its tilt as exp[-zX/(n+1)] times a uniformly exp[O(log^2 n/n)] factor; on the central neighborhood its smooth quadratic perturbation has curvature O(n^-3), negligible beside N^-1. The Gaussian concentration calculation in (8), with moment bounds, therefore holds uniformly for z in [0,1]. In particular

    Var_z(X/(n+1)) = R^2/(2n)(1+o(1)),
    E_z s2(X/(n+1)) = R^2/n(1+o(1)).

For a logarithm of a positive mixture, the second derivative equals the expected component second derivative plus the variance of component first derivatives. Applying (10) gives

    (log B)''(z)=-R^2/(2n)(1+o(1))                          (11)

uniformly on [0,1]. The s3 bound is O(log^3 n/n^2), which is o(R^2/n). Replacing the first derivatives by -mu changes their variance by o(R^2/n), by the central moment bounds and the extra factor 1/n in s2. Thus (11) retains the variance contribution; ignoring it would give a factor-of-two error.

Since (log B)'(0)=-D1/D=-r, integration also gives

    B(1)=D exp(-r)(1+o(1)),
    D1 B(1)+D B'(1)
       =D B(1)[(log B)'(1)-(log B)'(0)]
       =-D B(1) R^2/(2n)(1+o(1)).                         (12)

The last equality establishes the negative sign of the projected exponential numerator.

## 4. Actual normalization and negligible terms

The positive coefficient expansion at pole 1 shows A>=C. It also bounds A/C by exp[O(N/n)]=exp[O(log n)]. Equations (9) and n/R >> log n give

    log(D/A)=(1+o(1))n/R,
    (A+C)/D = exp[-(1+o(1))n/R].                         (13)

Furthermore Aplus/A=R(1+o(1)). One exact way to see this is to retain the positive joint (X,k) sum defining A: its corresponding Aplus term divided by the A term is X/(n+1+k). The factorial series has k=O(log n) in its moment bounds, and its positive tilt preserves X/(nR)->1. Together with D1/D=R(1+o(1)) and E/C=R(1+o(1)), the exact determinant becomes

    U/T=Aplus(D-C)+A(D1+E)=2R D A(1+o(1)).                (14)

Every term of (7) after the first pair is bounded by O(R(A+C)B(1)). Relative to the magnitude D B(1) R^2/n in (12), this is O((n/R)(A+C)/D)=o(1). Equations (7), (12) and (14) prove (2).

## 5. Both primitive endpoints and the complete signed error

Let J_i=-2i integral_(bar a)^a Fi(w)dw, along the entire upward vertical segment. Put

    K(w)=2V/[w(1-w)], V=w^2-w+1/2.

On that segment, w=1/2+iy, |y|<=1/2, one has |2V/w|<=1 and 0<=K(w)<=2. Hence

    F0=(2V/w)^n K(w)^h/w,
    |J0|<=4*2^h, |J1|<=2*2^h.                            (15)

Both vanishing endpoints are present in this bound. The exact logarithmic-period identity is

    pi-beta=J(F)/U=(m1J0-m0J1)/U.                        (16)

By (13)-(14), |mi|/T=O(RD). A single central C term and Stirling's formula give

    log C=N log 2+n log R+O(n).

Using A>=C in (15)-(16) proves

    |pi-beta|<=O(2^h/A)<=exp[-n log R+O(n)].               (17)

The exponential contour about both poles is likewise retained exactly: its value for the projected kernel is B(F)+e A(F)=B(F)+e U. Thus

    e+pi-c=e-alpha+pi-beta.

Equations (2), (13), and (17) show alpha tends to positive infinity, beta tends to pi, and (4)-(5) follow. Parity h only changes the signs of the unprojected residues; it cancels from the actual determinant and projected numerator.

## Scope and next possible regime

This closes the intended reflected repair with h~kappa n log n: the actual centers diverge upwards. It does not close every h/n growth law. A depth of order n^2 changes the competition because n/R and R become comparable; the Laguerre mixture then has a different exponential scale and cannot be handled by the small-curvature approximation (11). Agent 2's compulsory final-q dyadic growth is a separate arithmetic result, with N! replacing n!. Any next phase analysis must preserve that denominator interface and both endpoint terms.
