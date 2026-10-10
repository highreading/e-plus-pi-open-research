> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# All-parity signed asymptotics and first correction for the actual factorial B3 center

Author: Codex continuation Agent 3, 2026-10-02. Original research after the narrowly completed even-index audit. This note is an author proof and has not received independent examination. It uses the retained exact contact/forcing/reconstruction identities, not a replacement center. No historical finite checker, normality review, controller, or old computation was replayed. Symbolic algebra in derive_first_correction.py expands new saddle coefficients; it does not sample centers.

## 1. Exact center and results

Fix b=3,m_w=1. Write sigma=sqrt(2), M=1+sigma, a=sigma/(2M), b0=sigma M/2, rho=1/sigma and S=e+pi. Let

    T_ij=[z^(n+i-j)] exp(z)(1-z+z^2/2)^n, 0<=i,j<=2,
    D=diag(1,-sigma,2), v=(1,-2,1)^T,
    K=Z(I+Dpol)^(-n), w_j=(n-1)!/(n+2-j)!,
    W=diag(w_j^2), G=K^T W K,
    xi=T^(-1)fP, u=K xi,
    A=xi^T G xi,
    lambda=T^(-T)G xi/A, kappa=u^T W e0/A,
    c_n=kappa+lambda^T fQ.

Dpol differentiates coefficient polynomials and Z multiplies by t-1. The exact center is rational and lambda^T fP=1. These definitions retain the endpoint e0 and the factorial B-only metric.

For all sufficiently large integers n, not only one parity, T is nonsingular and

    c_n-S=(-1)^(n+1)4pi M^(-2n-3)
               [1-(2+sigma/8)/n+O(n^(-2))].           (1)

The normalized actual selector has the more precise direction

    fP_0 lambda = L0+L1/n+O(n^(-2)),                 (2)

where

    L0=(3/2-sigma, -4+3sigma, 3-2sigma)^T,
    L1=(3/4-3sigma/4, -1+sigma/2, 1/2)^T.

All entries of lambda are positive eventually, on BOTH parities. The endpoint correction itself satisfies

    kappa=(-1)^(n+1)exp(-sigma)/(6n! n^6)
                       [1+O(1/n)].                 (3)

The complete exponential forcing remains separately retained and is factorially smaller than every fixed inverse power correction to the geometric term. There are parity-independent coefficients alpha_j with alpha_0=1, alpha_1=-(2+sigma/8), such that, for each fixed J,

    c_n-S=(-1)^(n+1)4pi M^(-2n-3)
             [sum_(j=0)^J alpha_j/n^j+O(n^(-J-1))]. (4)

No estimate of the actual reduced denominator q_n is supplied. Equations (1)-(4) do not prove rationality or irrationality of S.

## 2. All-parity determinant conditioning

The exact scaled contact relation, including its parity sign, is

    H_n=(-1)^n D T_n D^(-1),
    (H_n)_ij=(1/(2pi)) integral_-pi^pi
      (1+sigma cos t)^n exp(-sigma exp(it))
                                      exp(i(j-i)t) dt.  (5)

The local maximum of |1+sigma cos t| is unique at t=0 with value M. Away from any fixed neighborhood, its modulus is at most M(1-eta). This includes the adverse odd-index region where the real base is negative: its modulus is at most sigma-1<M. Thus the local Gaussian determinant/cofactor asymptotics have the SAME coefficients on both parities. Positivity of the complex symbol is not asserted.

Put r=D^(-1)v=(1,sigma,1/2)^T and l=Dv=(1,2sigma,2)^T. The Gaussian Vandermonde calculation gives

    det H=C3 M^(3n)n^(-9/2)[1+O(1/n)],
    adj H=C2 M^(2n)n^(-2)[v v^T+O(1/n)],

    C2=exp(-2sigma)/(8pi a^2),
    C3=exp(-3sigma)/(32pi^(3/2)a^(9/2)).
                                                        (6)

The error O(1/n) follows from Taylor expansion after t=x/sqrt(n). Terms of order n^(-1/2) are odd under simultaneous x -> -x and integrate to zero. For a rigorous expansion with an arbitrary fixed number of terms, restrict to |t|<=n^(-1/2+epsilon) for a sufficiently small epsilon depending on that number, bound Taylor remainders by a fixed polynomial times a slightly weaker Gaussian, and use exp(-c n^(2epsilon)) on the local complement. The distant region is exponentially small. The alternants supply the required coincident-variable vanishing before integration.

Consequently T is nonsingular eventually and

    T^(-1)=(-1)^n k_n [r l^T+O(1/n)],
    k_n=4sqrt(pi)exp(sigma)a^(5/2) M^(-n)n^(5/2).   (7)

This obtains the actual inverse scale by nonzero determinants and cofactors. It does not invert a rank-one entrywise limit.

The positive endpoint forcing is exactly

    fP_i=n!/(2pi) integral_-pi^pi
       (1+sigma cos t)^n (1+rho exp(it))^i dt.
                                                        (8)

Although this circle weight changes sign at odd n, its far tail is exponentially smaller. Therefore

    fP_0=n! M^n/(2sqrt(pi a n))[1+O(1/n)],
    fP/fP_0 -> fstar=(1,1+rho,(1+rho)^2)^T.

Write B0=l^T fstar=(2+sigma)^2=2M^2. Since a^2 B0=1, (7)-(8) simplify to

    xi=(-1)^n exp(sigma)n!n^2
                        [(2,2sigma,1)^T+O(1/n)].       (9)

No cancellation occurs in xi2.

The actual metric has G ->6 e2 e2^T, so

    A=6exp(2sigma)(n!)^2 n^4[1+O(1/n)].             (10)

Signs in xi and T^(-T) cancel in lambda; (7)-(10) already prove L0=l/B0 on every sufficiently large integer. In contrast kappa retains one inverse sign. Since

    u0=-xi0+n xi1-n(n+1)xi2
       =(-1)^(n+1)exp(sigma)n!n^4[1+O(1/n)]
    w0^2=n^(-6)[1+O(1/n)],

equation (3) follows from kappa=w0^2 u0/A. This explicitly retains the endpoint and improves the coarse factorial bound by one power of n.

## 3. Computing the first selector correction

Set mu_n=(H_n)_00 and h=1/n. Define the scalar normalized moments m_k=(H_n)_(i,j)/mu_n for k=j-i. Local expansion gives

    m_k=1+A(k)h+B(k)h^2+O(h^3),                   (11)

where

    A(k)=k[-(2+sigma)k+4+4sigma]/4,

    B(k)=k[(3+2sigma)k^3-(16+12sigma)k^2
                  +(14+6sigma)k+24+8sigma]/16.

Here k is one of -2,-1,0,1,2. The signs in these formulas incorporate the exp(-sigma exp(it)) phase in the actual contact symbol.

For derivation, write

    log((1+sigma cos t)/M)=-a t^2+d t^4+f t^6+O(t^8),
    d=a/12-a^2/2, f=-a/360+a^2/12-a^3/3.

With x=t/sqrt(h), the combined exponent after removing exp(-sigma) is

    -a x^2
    +sqrt(h) i(k-sigma)x
    +h[sigma x^2/2+d x^4]
    +h^(3/2) i sigma x^3/6
    +h^2[-sigma x^4/24+f x^6]+O(h^(5/2) polynomial).

The normalized Gaussian moments are E[x^(2j)]=(2j-1)!!/(2a)^j. If c2(k),c4(k) denote its integrated h,h^2 coefficients, then

    c2(k)=(sigma-(k-sigma)^2)E[x^2]/2+d E[x^4],

    c4(k)=[-sigma/24-(k-sigma)sigma/6+sigma^2/8
              -(k-sigma)^2 sigma/4+(k-sigma)^4/24]E[x^4]
          +[f+sigma d/2-(k-sigma)^2 d/2]E[x^6]
          +(d^2/2)E[x^8].

Thus A(k)=c2(k)-c2(0) and
B(k)=c4(k)-c4(0)-A(k)c2(0), yielding (11).

Let M(h)=[m_(j-i)]. Taking 2-by-2 cofactors yields

    adj M(h)=h/(2a)[v v^T+h Atilde1+O(h^2)].

After conjugating back, define

    Q(h)=2a D^(-1) adj M(h) D/h
        =Q0+h Q1+O(h^2), Q0=r l^T.                (12)

Only the last row of Q1 is needed:

    Q1_(2,*)=(-7/4-3sigma/4, -1-5sigma/2, -1/2+sigma).
                                                        (13)

These are polynomial cofactor calculations from (11), with no inversion or numerically estimated coefficient. Full matrices are recorded in derive_first_correction.txt.

The forcing ratios in (8) satisfy

    fP/fP_0=fstar+h f1+O(h^2),
    f1=(0, -(1+sigma)/4, -3/2-sigma)^T.            (14)

This uses g_i''(0)/(4a) for g_i(t)=(1+rho exp(it))^i; the normalized scalar weight correction cancels.

From the exact weights and reconstruction,

    G=G0+h G1+O(h^2),
    G0=6 e2 e2^T,
    G1=[[0,0,0],[0,0,-3],[0,-3,8]].               (15)

The determinant and the scalar mu_n^2 h/(2a) cancel EXACTLY from the normalized selector. Hence

    fP_0 lambda =
       Q(h)^T G Q(h)(fP/fP_0) /
       [(fP/fP_0)^T Q(h)^T G Q(h)(fP/fP_0)].       (16)

Write X1=Q1 fstar+Q0 f1. Since Q0 is r l^T and G0 is concentrated on the final coordinate, expansion of (16) gives

    L1=2 Q1_(2,*)^T/B0-2l (X1)_2/B0^2.           (17)

The G1 terms cancel between numerator and denominator. This is a precise first-order metric cancellation for the actual metric with limit G0; it does not identify arbitrary centers.

Using (13)-(14), (X1)_2=-B0, and (17) reduces to the displayed vector L1. The normalization check is exact:

    L1^T fstar+L0^T f1=0.

Because its limiting denominator is B0^2 r^T G0r=(3/2)B0^2>0, (16) has an ordinary power asymptotic expansion to every fixed order. No loss from the rank-one leading Q0 is hidden.

## 4. Actual endpoints and complete logarithmic contraction

The complete forcing difference is fQ-SfP=eE+eF. The all-parity exact logarithmic identity is

    eF_i=(-1)^(n+1)2n! integral_-pi/4^pi/4
      (sigma cos t-1)^n (1-rho exp(it))^i dt.      (18)

This identity follows from n integrations by parts whose boundary terms vanish at BOTH conjugate zeros, followed by deformation to the left arc. The order of the arc reverses the original segment. Its retained factor 2 and (-1)^(n+1) therefore account for both endpoint contributions and their orientation.

Put gstar=(1,1-rho,(1-rho)^2)^T. The positive arc weight has unique maximum M^(-1) at zero and curvature b0=sigma M/2. Thus

    eF/eF_0=gstar+h g1+O(h^2),
    g1=(0,(sigma-1)/4,-3/2+sigma)^T.               (19)

The scalar weights in (8),(18) have quartic coefficients
dplus=a/12-a^2/2 and dminus=b0/12-b0^2/2. Their first relative corrections are 3dplus/(4a^2) and 3dminus/(4b0^2), so

    eF_0/fP_0=(-1)^(n+1)4pi M^(-2n-1)
                        [1-sigma/(8n)+O(n^(-2))]. (20)

Indeed their difference is (1/b0-1/a)/16=-sigma/8.

The normalized contraction coefficients are

    L0^T gstar=M^(-2),
    L1^T gstar+L0^T g1=-2M^(-2).                 (21)

Combining (2),(19)-(21) gives

    lambda^T eF=(-1)^(n+1)4pi M^(-2n-3)
                   [1-(2+sigma/8)/n+O(n^(-2))].

Finally, the retained COMPLETE exponential bound
|eE_i|<=27 M^n sigma^(-i)/(n+1), together with (2) and (8), gives
lambda^T eE=O(1/(n!sqrt(n))). Equation (3) bounds the endpoint separately. Their ratio to M^(-2n)n^(-J) tends to zero for every fixed J. The exact identity

    c_n-S=kappa+lambda^T eE+lambda^T eF

therefore proves (1), and the all-order local expansions prove (4).

## 5. Directional consequences for actual rational centers

For all sufficiently large k,

    c_(2k)<S<c_(2k+1),
    c_(2k+2)>c_(2k), c_(2k+3)<c_(2k+1).

Thus the actual rational intervals I_k=[c_(2k),c_(2k+1)] are eventually nested, contain S strictly, and shrink with

    length(I_(k+1))/length(I_k) -> M^(-4).

The adjacent error ratio tends to -M^(-2), and the two-step error ratio tends to M^(-4). These are consequences of the actual complete signed error, not just an envelope. The eventual starting index is not quantified here.

## 6. Search and overlap record

Archive queries were performed before this target: all-parity/Gram alternating, first correction/Gram, 1/n/Gram, nested intervals, selector first order, metric first order, Richardson and consecutive-index filters. The main overlap is the EVEN-only October 1 draft and the earlier arbitrary-adjoint logarithmic arc formula. Older scalar-center alternating work expressly studies a different center. No completed exact all-parity B3 center theorem or its displayed first correction was found by these searches. This is a bounded archive result, not a global novelty claim.

Web queries for this target and the first-correction extension:
- Hermite Pade Toeplitz saddle determinant first correction fixed matrix size asymptotic expansion
- Toeplitz determinant Laplace method Gaussian Vandermonde fixed n large parameter asymptotic expansion
- Hermite-Pade extrapolation rational approximation error asymptotic
- Toeplitz fixed saddle asymptotic Pan Prokhorov

Current primary papers opened:
- [Pan and Prokhorov (2025), fixed-parameter Painleve III Toeplitz asymptotics](https://onlinelibrary.wiley.com/doi/10.1111/sapm.70051), [arXiv record](https://arxiv.org/abs/2407.04852). Section 4 supplies a related Andreief/Vandermonde methodology. Its cylinder-function symbol and objective differ from (5); no theorem for this center is imported.
- [Mano and Tsuda, Hermite-Pade approximation, isomonodromic deformation and hypergeometric integral](https://arxiv.org/html/1502.06695). Its Toeplitz determinant formulas are structural overlap, not a signed factorial-Gram center result.
- Search found [Homeier, Series Prediction Based on Algebraic Approximants](https://onlinelibrary.wiley.com/doi/10.5402/2011/958968) and [van der Hoeven, On asymptotic extrapolation](https://www.texmacs.org/joris/extrapolate/extrapolate.html). These are contextual extrapolation results and are not used in the proof.

Status: original author theorem for one exact center, awaiting independent examination; no global denominator bound or resolution of e+pi.

