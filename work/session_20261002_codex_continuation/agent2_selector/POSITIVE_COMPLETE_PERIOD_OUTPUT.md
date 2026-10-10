> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A uniform positive complete-period coordinate of the actual weighted output

2026-10-02. Author theorem in the parent-requested constant-shift recurrence problem. The exact actual-W quotient has three coordinates. This note proves that its complete beta-period coordinate is strictly positive for every even n and every real m≥0. It does not yet prove that three consecutive actual output rows have rank three.

The archive and opened primary-literature search preceding this subtarget is recorded in `PERIOD_CASORATIAN_TARGET.md`. The beta-integral and orthogonal-polynomial/Casoratian mechanisms are classical; the project-specific result is the identity below for its actual U and its actual order-n+1 weighted difference. No generic-method novelty is claimed.

## 1. Exact definitions

Let n=2r≥2, d=n+1=2r+1, and retain

    V(w)=w²−w+1/2,
    a_j=[x^j](1+2x+2x²)^n,
    U(n,m)=Σ_(ell=0)^r (-2)^ell a_(n−2ell)(2m)_ell/ell!.

The factorial (2m)_ell here is falling. Define the symmetric complete period by its beta analytic continuation

    Z_n(m)=Σ_(k=0)^(n−1) b_(2k+1) 2^(r−k−1/2)
               B(k−r+1/2,2m+1),
    b_j=[w^j]V(w)^n.

All the half-integer first arguments avoid poles of Γ; the gamma ratio defining B is regular for m≥0. Set

    C_m=2^(−1/2)B(1/2,2m+1)>0,
    F_n(m)=C_m^(−1) Δ_m^d[U(n,m)Z_n(m)].

This agrees exactly with the H and F coordinate formulas in `PERIOD_CASORATIAN_TARGET.md`: Z_n=C_m H_n. Thus it is the actual U-weighted output applied to the complete homogeneous period solution of the original moment module. It is a coordinate of the actual W output, not the value W itself.

## 2. Positive density and its derivative signs

On 0≤t<1 put w=√((1−t)/2) and define

    h_n(t)=[V(−w)^n−V(w)^n]/(4w^(n+2)).

It is strictly positive. Expanding the odd binomial powers in the numerator yields the exact finite sum

    h_n(t)=Σ_(s=0)^(r−1) binom(n,2s+1) 2^(r−s−1/2)
             (1−t/2)^(2(r−s)−1)/(1−t)^(r−s+1/2).   (1)

For integer z≥1, the factor in a summand is

    (1−t/2)^(2z−1)/(1−t)^(z+1/2)
      =(1−t)^(-1) [1−(t/(2−t))²]^(-z+1/2).       (2)

Every Taylor coefficient at t=0 of the right side is nonnegative: both (1−t)^(-1) and t/(2−t) have nonnegative coefficients, and the binomial expansion of (1−u²)^(-z+1/2) has positive coefficients since z−1/2>0. These expansions converge for 0≤t<1. Consequently h_n and all its derivatives are nonnegative there; h_n itself is strictly positive.

Leibniz's rule also gives, for every ell≥0,

    D^ell[t^ell h_n(t)]>0,  0≤t<1.               (3)

The derivative term differentiating t^ell exactly ell times is ell!h_n>0; all other terms are nonnegative.

The endpoint bounds needed below follow directly from the finite sum (1): for fixed n and each derivative order k,

    h_n^(k)(t)=O_n,k((1−t)^(-r−1/2−k)) as t↑1,

and h_n is analytic at t=0.

## 3. Removal of finite parts by the actual difference

The complete beta period equals

    Z_n(m)=−FP∫_0^1 t^(2m)h_n(t)dt.              (4)

Here FP denotes the finite-part / beta analytic-continuation functional. To see the constants, pair the positive and negative real w-intervals in the symmetric original period. Their numerator becomes V(w)^n−V(−w)^n, and dw=−dt/(4w). Expanding V^n reproduces the beta sum defining Z_n.

The exact U formula gives

    U(n,m)t^(2m)
      =Σ_(ell=0)^r (-2)^ell a_(n−2ell)/ell!
           ·t^ell D^ell[t^(2m)].

After the d-th difference, the factor t^(2m) becomes

    f_m(t)=t^(2m)(t²−1)^d.

Therefore

    Δ^d[U Z_n]
      =−Σ_(ell=0)^r (-2)^ell a_(n−2ell)/ell!
         ∫_0^1 h_n(t)t^ell D^ell f_m(t)dt.        (5)

These are ordinary convergent integrals. Near t=1 their integrands have order O((1−t)^(d−ell−r−1/2)), whose exponent is r+1/2−ell≥1/2. Near t=0, powers in t^ell D^ell t^(2m) are bounded by a constant times t^(2m); every term is integrable for m≥0. In passing from (4) to (5), finite-part regularization has disappeared because the combined test functions vanish to sufficient order at t=1. Equivalently, the same identity follows by analytic continuation of the beta integrals after the finite difference is combined, followed by convergence of the combined expression.

Integrate each summand ell times by parts. At t=1 every boundary term has a factor bounded by

    (1−t)^(d−ell+1−r−1/2)
      =(1−t)^(r+3/2−ell),

which tends to zero, uniformly across the finite list 0≤ell≤r. At t=0, derivatives of t^ell h_n of order k≤ell−1 vanish at least to order ell−k; multiplying derivatives of f_m of order ell−1−k gives a bound O(t^(2m+1)), also tending to zero. When a derivative coefficient vanishes for an integer 2m, the bound only improves. This argument covers real m≥0 and involves no division by U or by a possibly zero error.

The ell signs from integration by parts cancel those in (-2)^ell. Since d is odd, (t²−1)^d=−(1−t²)^d. Formula (5) becomes the positive identity

    C_m F_n(m)
      =∫_0^1 t^(2m)(1−t²)^(n+1)
          Σ_(ell=0)^r [2^ell a_(n−2ell)/ell!]
               D^ell[t^ell h_n(t)] dt.          (6)

All coefficients a_(n−2ell) are strictly positive. The integrand is strictly positive on (0,1), by (3), and integrable at both endpoints by the preceding bounds. Hence

    F_n(m)>0 for every even n≥2 and real m≥0.    (7)

## 4. Scope for the remaining Casoratian problem

The exact n=4,8 symbolic period outputs previously obtained have positive numerator coefficients; identity (6) proves their functional positivity uniformly for all even n, without extrapolating that coefficient pattern. It also proves that the actual weighted-difference output does not annihilate the complete period solution anywhere on the positive real axis.

This removes one possible degeneracy of the three-state quotient. It does not imply that the three consecutive output rows are independent: two endpoint modes remain, and the corresponding output coefficients can interact with the complete-period coordinate. A uniform proof for their full Casoratian / τ_n is still required for an O(1)-shift selection theorem for W. The existing O(n) actual-W block theorem remains the currently proved nonvanishing result.
