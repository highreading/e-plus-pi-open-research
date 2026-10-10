> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A Legendre second-kind formula for the actual associated measure

Date: 2026-09-13. Original root continuation; independent review passed in raw_associated_measure_second_kind_independent_review.md.

This makes the density in the reviewed Legendre-square identification
explicit in two ordinary Legendre solutions. It also records the exact
endpoint behavior for each fixed starting index. Uniform growing-index
bounds require additional estimates; the fixed-index limits below are
not silently used in that regime.

## 1. Exact density in standard polynomial solutions

Retain mu_a from `raw_coupled_pencil_exact_legendre_square.md`, put
m=a−1≥0, and write

    alpha_j=j/sqrt(4j²−1),
    c_m=alpha_(2m+1)alpha_(2m+2),
    kappa_l=2^(−l) binom(2l,l).

Define the second-kind function by its integral, including its branch:

    Q_l(s)=1/2 integral_(-1)^1 P_l(u)/(s−u) du,
                                      s outside [-1,1].

On −1<x<1 write mathsf Q_l(x) for its real principal-value boundary
part. Then Q_l(x+i0)=mathsf Q_l(x)−i*pi*P_l(x)/2.

The entire associated probability measure has density

    w_a(y)=sqrt(y)/[2c_m²(4m+1)|Q_(2m)(sqrt(y)+i0)|²]

          =sqrt(y)/{2c_m²(4m+1)
                 [mathsf Q_(2m)(sqrt y)²
                              +pi² P_(2m)(sqrt y)²/4]},
                         0<y<1.                         (1)

Here is an exact normalization check, rather than an appeal to an
unspecified associated-polynomial convention. The monic polynomials
for mu_0 are pi_m(y)=P_(2m)(sqrt y)/kappa_(2m), with squared norm
h_m=1/[(4m+1)kappa_(2m)²]. Put

    sigma_(m−1)(z)=integral [pi_m(z)−pi_m(y)]/(z−y) dmu_0(y),

where sigma_(-1)=0. The lower row of the stripping matrix T_(m+1)
in the preceding note is exactly

    C_(m+1)=c_m² pi_m,
    D_(m+1)=−c_m² sigma_(m−1).                           (2)

This follows either by its two-by-two product recurrence or by the
monic three-term recurrence and its second-kind recurrence, with
initial pairs (pi_0,sigma_(-1))=(1,0) and
(pi_1,sigma_0)=(z−d_0,1). Its determinant is c_m² h_m.

Further,

    pi_m(z)m_0(z)−sigma_(m−1)(z)
      =integral pi_m(y)/(z−y) dmu_0(y)
      =Q_(2m)(sqrt z)/(kappa_(2m)sqrt z).                (3)

For the last equality substitute y=u². Evenness of P_(2m) gives
integral_0^1 P_(2m)(u)/(s²−u²)du=Q_(2m)(s)/s. Inserting (2)–(3)
into the already proved density formula gives (1), including its
factor 2, the factor 4m+1, and the actual off-diagonal c_m².

## 2. Fixed-index behavior at zero

The even polynomial has

    P_(2m)(0)=(−1)^m binom(2m,m)/4^m ≠0.

The real principal-value Q_(2m) is odd, analytic near zero, and
vanishes there. These facts follow by substituting u→−u in its
integral, or from the elementary logarithm expression in the next
section. Therefore, for each fixed a,

    w_a(y)=K_a sqrt(y)[1+O_a(y)],
    K_a=2/[pi² c_m²(4m+1) P_(2m)(0)²],   y→0+.         (4)

The constants are finite and positive for every a≥1. The elementary
central-binomial asymptotic, if used, gives K_a→8/pi as a→infinity;
the exact coefficient in (4) does not depend on that asymptotic.

## 3. Fixed-index behavior at one, with the harmonic shift retained

Polynomial division in the second-kind integral gives

    mathsf Q_l(x)=1/2 P_l(x) log((1+x)/(1−x))−W_(l−1)(x),
    W_(l−1)(x)=1/2 integral_(-1)^1
                       [P_l(x)−P_l(u)]/(x−u) du.        (5)

The last expression is a polynomial, with W_(-1)=0. The recurrence
for P_l and Q_l gives, for l≥1,

    (l+1)W_l=(2l+1)x W_(l−1)−l W_(l−2),

with W_0=1. Consequently

    W_(l−1)(1)=H_l=sum_(j=1)^l 1/j,  H_0=0.            (6)

Indeed the sequence H_l has the same recurrence at x=1 and the same
two initial values. This also supplies a direct proof of (6).

For epsilon=1−y→0 and fixed l=2m, equations (5)–(6) give

    2 mathsf Q_l(sqrt(1−epsilon))
      =log(4/epsilon)−2H_l
                         +O_l(epsilon log(1/epsilon)),
    P_l(sqrt(1−epsilon))=1+O_l(epsilon).

Thus a more informative version of the edge asymptotic is

    w_a(1−epsilon)
      ~ [2/(c_m²(4m+1))]
             /{[log(4/epsilon)−2H_(2m)]²+pi²}.         (7)

In particular it is asymptotic to
2/[c_m²(4m+1)log²(4/epsilon)] at each fixed a. For a growing with
epsilon^(-1), the shift 2H_(2m) cannot be discarded: it is of order
log a. Formula (7) as stated is a fixed-index limit, not a uniform
boundary scaling theorem.

The limiting constant-coefficient Jacobi measure has semicircle
density (8/pi)sqrt(y(1−y)). Equation (7) proves that there is no
constant upper comparison of w_a to that density on the entire
interval, even for any one fixed a. Their ratio diverges as y→1.
This does not preclude uniform comparison outside a shrinking edge
interval or a small total mass for that interval. Such quantitative
estimates, with the growing index and both boundary factors retained,
are the next useful analytic step.

No mixed zero-count bound, endpoint cancellation estimate, or
irrationality conclusion follows from (1)–(7) alone.
