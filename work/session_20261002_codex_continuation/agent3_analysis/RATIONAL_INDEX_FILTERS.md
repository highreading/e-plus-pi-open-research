> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Rational consecutive-index filters for the actual B3 Gram centers

Author: Codex continuation Agent 3, 2026-10-02. Original corollary of ALL_PARITY_B3_SIGNED_ASYMPTOTIC.md; not independently examined. The starting centers are precisely its actual factorial B-only centers, including their endpoint corrections. This is an across-index construction, not a replacement selector or an unproved comparison of different metrics.

Let M=1+sqrt(2), R=M^(-2), gamma=-(2+sqrt(2)/8), S=e+pi, and E denote the forward shift in n. The original author theorem supplies a parity-independent complete Poincare expansion

    c_n-S=(-1)^(n+1)4pi M^(-2n-3)
                   [1+gamma/n+alpha2/n^2+...].

The coefficients beyond gamma need not be evaluated to derive the filters below, but their existence and common values on both parities are essential. A mere 1+O(1/n) theorem would not determine the filtered leading coefficient.

## 1. The minimal rational quadratic filter

The signed geometric multiplier is r=-R. Its minimal polynomial over Q is

    P(x)=1+6x+x^2,
    P(r)=0, P(1)=8,
    -r P'(r)=1-R^2>0.

Consequently define the exactly rational convex combination

    d_n=(c_n+6c_(n+1)+c_(n+2))/8.                 (1)

No numerical value of S or irrational coefficient is required. The full errors, including each center's actual rational correction, satisfy

    d_n-S=(-1)^n (pi/2)(22sqrt(2)-29)
                     M^(-2n-3)n^(-2)[1+O(1/n)]. (2)

The coefficient 22sqrt(2)-29 is positive, since 968>841. Thus this filter improves the actual error by two powers of n while retaining its exponential rate; it reverses the eventual directional sign.

To derive (2), write c_n-S=-4pi M^(-3)r^n A(n), where A(n)=1+gamma/n+alpha2/n^2+O(n^(-3)). Then

    d_n-S=(-4pi M^(-3)r^n/8)
                     sum_(j=0)^2 p_j r^j A(n+j),
    (p0,p1,p2)=(1,6,1).

The constant and each common 1/n coefficient multiply P(r)=0. Expanding the shifts gives

    sum_j p_j r^j A(n+j)
       =-gamma rP'(r)/n^2+O(n^(-3))
       =gamma(1-R^2)/n^2+O(n^(-3)).

Using gamma(1-R^2)/8=-(22sqrt(2)-29)/8 yields (2). The unknown alpha2 term cancels at this order because it also multiplies P(r).

No rational linear filter a+bE with a+b=1 can annihilate r, since a+br=0 would make r rational when b!=0. Thus degree two is the smallest fixed rational shift filter that removes the geometric leading term. This statement concerns fixed rational coefficients, not adaptive rational functions of n or nonlinear transforms.

## 2. Repeated fixed filters

For every FIXED integer m>=1, define

    d_n^(m)=8^(-m)P(E)^m c_n
           =8^(-m) sum_(j=0)^(2m) a_(m,j)c_(n+j),
    a_(m,j)=[x^j](1+6x+x^2)^m.

All a_(m,j) are nonnegative integers and sum to 8^m, so these are rational convex combinations of actual centers. Repeated shift expansion gives the complete signed asymptotic

    d_n^(m)-S=(-1)^(n+1)4pi M^(-2n-3)
        gamma m![(1-M^(-4))/8]^m n^(-m-1)
                                     [1+O_m(1/n)]. (3)

For proof, if beta is fixed and B(n)=n^(-beta)[1+O(1/n)] has its full common power expansion, then

    P(E)[r^n B(n)]
      =r^n [-beta rP'(r)]n^(-beta-1)[1+O(1/n)].

The constant in A(n) is annihilated exactly at the first application. Its gamma/n term is the surviving least inverse power. Applying the identity m times gives gamma m![-rP'(r)]^m n^(-m-1). Higher terms contribute smaller inverse powers. This proves (3).

Every m>=1 has eventual sign (-1)^n because gamma<0 and 1-M^(-4)>0. Thus even filtered centers lie above S and odd filtered centers lie below it. Each filtered parity subsequence is eventually monotone toward S, and the corresponding rational bracketing intervals have asymptotic two-step shrink ratio M^(-4).

The assertion is for each fixed m. No uniform estimate for growing m, n-dependent m, or a better exponential rate is asserted.

## 3. Exact denominator and the unresolved arithmetic cost

Write c_(n+j)=p_(n+j)/q_(n+j) in lowest terms, q_(n+j)>0. Put

    L=lcm(q_n,...,q_(n+2m)),
    N=sum_(j=0)^(2m) a_(m,j)p_(n+j)L/q_(n+j).

Then the actual reduced filtered denominator is exactly

    q_n^(m)=8^m L/gcd(8^m L,N).                  (4)

This retains every prime and all cancellation from the fully combined rational sum. Neither q_n^(m) nor the primitive filtered error is identified with an individual q_(n+j).

For fixed m, (3) supplies

    log(q_n^(m)|d_n^(m)-S|)
       =log q_n^(m)-2n log M-(m+1)log n+O_m(1). (5)

The analytic gain is real, but (4) is not an upper estimate on its arithmetic cost. No subcritical exponential denominator bound follows. The rationality of e+pi remains open.

## 4. Archive and current primary-source overlap

Before selecting this filter target, rg searches included Richardson, 1+6, consecutive-index, index-filter, c_n/6c_(n+1), the displayed 22sqrt(2)-29 coefficient, and inverse-power Gram corrections across the archive. Existing Richardson results in root-unity constructions concern different families; the scalar-center contiguous note also expressly concerns a different center. No matching actual B3 across-index filter with its complete constant was found by the bounded searches. Search absence is not global novelty.

Web queries:
- Hermite-Pade extrapolation rational approximation error asymptotic
- Toeplitz fixed saddle asymptotic Pan Prokhorov

Primary papers opened for this target:
- [Pan and Prokhorov, fixed-parameter Toeplitz/Painleve asymptotics](https://onlinelibrary.wiley.com/doi/10.1111/sapm.70051), [arXiv record](https://arxiv.org/abs/2407.04852).
- [Mano and Tsuda, Hermite-Pade approximation, isomonodromic deformation and hypergeometric integral](https://arxiv.org/html/1502.06695).

Their overlap is determinant/asymptotic structure; neither result is imported to identify this center or this filter. Search also located [Homeier, Series Prediction Based on Algebraic Approximants](https://onlinelibrary.wiley.com/doi/10.5402/2011/958968) and [van der Hoeven, On asymptotic extrapolation](https://www.texmacs.org/joris/extrapolate/extrapolate.html), contextual to sequence acceleration. The filter proof is the displayed elementary shift calculation, not an assertion of a new general extrapolation principle.

Status: author proof for a new specified rational construction. No independent audit beyond the completed even-index audit was conducted, and no externally published claim or irrationality conclusion is made.

