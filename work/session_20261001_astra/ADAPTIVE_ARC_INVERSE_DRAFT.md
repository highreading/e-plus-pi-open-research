> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Adaptive-arc coercivity and a larger growing-degree range

Status: new main-agent paper research, not independently reviewed. The inverse argument below is self-contained given the exact Toeplitz reduction. Center-error consequences also assume the logarithmic forcing-vector bound reported by Agent 2. This is not an irrationality theorem.

## 1. Even-index positive real part

Let n>=2 be even, 2<=b<=n, d=b-1, M=1+sqrt(2). Use the scaled Toeplitz matrix H and symbol from POSITIVE_FORCING_EVEN_NORMALITY_TAU_DRAFT.md:

    phi(u)=(1+sqrt(2)cos u)^n exp(-sqrt(2)exp(iu)).

Its real part is nonnegative everywhere and its quadratic form is strictly positive on nonzero coefficient vectors. The endpoint lift therefore exists within the new even-index author proof.

The previous localization radius n^(-1/2) is unnecessarily small when the coefficient polynomial has degree b-1. Here choose

    h=sqrt(b/n)<=1.

## 2. Localization with a variable arc

For any 0<h<=1, degree-d coefficient polynomial p, and coefficient vector x, the same explicit interpolation construction proves

    integral_-h^h |p(exp(iu))|^2 du
       >=h ||x||_2^2/[b C(h)],

where

    C(h)=(16b^2/h^2)^d binom(2d,d)/(d!)^2.           (1)

To verify constants, take I_j=[-h+2jh/b,-h+(2j+1)h/b], j=0,...,d. Select u_j in I_j with |p(exp(iu_j))|^2 at most (b/h) times its interval integral. For i<j the angle gap is at least (j-i)h/b and at most 2h<=2<pi. The chord is at least (j-i)h/(2b).

The coefficient norm of the jth Lagrange polynomial is at most

    2^d(2b/h)^d/[j!(d-j)!].

Sum their squared bounds and use the binomial-square identity. Cauchy-Schwarz and the sum of the selected value bounds yield (1). No unknown interpolation constant remains.

## 3. Optimized inverse cost

On |u|<=h=sqrt(b/n),

    (1+sqrt(2)cos u)/M>=1-u^2/2>=1-b/(2n).

Since log(1-x)>=-2x for 0<=x<=1/2,

    (1+sqrt(2)cos u)^n>=M^n exp(-b).

Also exp(-sqrt(2)cos u)>=exp(-sqrt(2)) and cos(sqrt(2)sin u)>=7/45. The normalized central contribution to the real quadratic form is therefore at least

    [7exp(-sqrt(2))/(90pi)] M^n exp(-b)
       *h ||x||_2^2/[b C(h)].

All other contributions are nonnegative for even n. Hence

    ||D_R T^(-1)D_R^(-1)||_2<=Kadapt M^(-n),       (2)

with the convenient explicit constant

    Kadapt=512 sqrt(bn) exp(b)
       (16bn)^d binom(2d,d)/(d!)^2.                  (3)

Indeed 90pi exp(sqrt(2))/7<512, using pi<4 and exp(sqrt(2))<9. Thus (3) safely bounds the exact reciprocal constant. The forward norm remains below 9M^n.

For a simpler asymptotic envelope, use binom(2d,d)<=4^d, d!>=(d/3)^d, and d>=b/2. Then

    Kadapt<=512 sqrt(bn) exp(b)(2304n/b)^(b-1),     (4)

so

    log Kadapt=O(log n+b+b log(n/b)).               (5)

In particular log Kadapt=o(n) whenever b=o(n). This is stronger dimension control than O(b log n). It concerns the inverse only; the reconstruction and factorial weights still have their own costs.

Strict positivity and the singular-value bound also give

    det J_(n,b)>=K_(n,b)(M^n/Kadapt)^b>0

for the positive prefactor in the exact reduction. This determinant estimate is not used as a substitute for (2).

## 4. Complete center propagation

Use the actual positive forcing lower bound, finite differential reconstruction, and complete forcing hypotheses from POSITIVE_FORCING_EVEN_NORMALITY_TAU_DRAFT.md, replacing Kinv by Kadapt in its formula (10).

This substitution changes no coefficient normalization or rational center. It yields an explicit conditional complete envelope for every even n>=16, 3<=b<=n, and allowed subtraction depth m. In particular, the logarithmic residual hypothesis used here is

    ||D_R eF||_2<=2sqrt(pi b/n)n!M^(-n).

The exponential residual and endpoint constant remain in the factorial part of the envelope. No cancellation between separately bounded contributions is presumed.

Let beta>0 be fixed and, along even integers n tending to infinity, set

    b=floor(beta n/log n),
    m=floor((b-1)/2).

Eventually 3<=b<=n and all weight definitions are valid. Then

    log Kadapt=o(n),
    log Hplus=beta n+o(n),
    log Hminus=beta n+o(n),
    b log(2n)=beta n+o(n).

All remaining dimension and diagonal factors have logarithm o(n). Thus the geometric term in the complete center envelope satisfies

    log deltastar <=-[2log M-3beta]n+o(n),          (6)

while the factorial terms have logarithm -n log n+O_beta(n) and are negligible. More precisely, the logarithm of the sum is bounded by the right side of (6) plus o(n), since the geometric prefactor has been explicitly retained.

Therefore any fixed

    0<beta<2log(1+sqrt(2))/3

gives a decaying author/conditional center envelope on this much larger growing-degree allocation. This range is outside the former fourth-power restriction. Its availability comes from the even-index argument and the variable localization arc, not extrapolation of a fixed-b theorem.

A sufficient arithmetic target for this selected allocation is

    q_n->infinity,
    limsup log(q_n)/n<2log(1+sqrt(2))-3beta,

where q_n is the actual reduced denominator of the same B-only rational center. No such arithmetic estimate is proved here.

## 5. Scope and next step

The new proved-within-author-scope result is (2)-(5), with every localization and dimension constant displayed. Equation (6) is a consequence conditional on the named complete forcing input and the exact reconstruction identities. The finite reconstruction estimates still cost approximately three beta n in this conservative propagation.

Improving those reconstruction losses could enlarge the useful b range further, but requires analysis of the actual two forcing columns. It cannot follow from rescaling the coefficient norm or deleting its smallest weight. Arithmetic of the final center denominator remains independent and unresolved.

No accepted result is overwritten, no numerical scan is used, and no conclusion about e+pi is claimed.
