> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Large selector: two endpoint contributions with controlled truncation

New author analytic research, not an independent review. The main LARGE_SELECTOR_DYADIC_DENOMINATOR_DRAFT.md has been read. Its nonvanishing, valuation, forcing-height, and actual reduced-denominator conclusions are used as provisional arithmetic inputs. Earlier saddle reductions are preserved. The small-saddle constant correction is saved separately in LARGE_DEGREE_SMALL_SADDLE_PHASE_CORRECTION.md.

## Allocation and normalization

Let n=4k, choose the power of two P satisfying k<P<=2k, and set

    m=P ceil((rho n log n+k)/P)-k,
    0<rho<1/(2 log 7).

Keep this exact integer m throughout. Put V(w)=w^2-w+1/2 and

    G(w)=V(w)^n(2w^2-1)^(2m)/w^(n+1).

The retained exact identities are

    D=n! 2^(-n)U,
    Flog=(-1)^(n+1)(2n!/i) integral_C G(w)dw,

where C runs from the lower root (1-i)/2 to the upper root (1+i)/2 on the right of zero. The main author inputs give U!=0, v2(U)=n/2, and

    log|U| <= (n/2)log log n+O_rho(n).

Thus all quotients below use an actual nonzero denominator. Write c for the rational direct-selector quotient. Its complete error is (Flog+Eexp)/D.

## An exact two-contribution construction

A moving-saddle relative asymptotic is not assumed. Instead use an explicitly convergent endpoint expansion with a growing truncation depth. This supplies an additive enclosure even when the two conjugate contributions nearly cancel.

Put alpha=(1+i)/2, c0=1/2, and h=c0-alpha=-i/2. Deform C into the two straight segments from conjugate(alpha) to c0 and from c0 to alpha. They avoid the only pole, zero. Define

    Jplus=integral_(c0)^alpha G(w)dw.

Since G has real coefficients, the lower contribution is -conjugate(Jplus). Consequently

    integral_C G=Jplus-conjugate(Jplus)=2i Im Jplus,
    Flog=(-1)^(n+1)4n! Im Jplus.                    (1)

The two contributions and their relative phase are retained exactly. Replacing either by its modulus would destroy (1).

Expand at the upper endpoint:

    G(alpha+z)=sum_(j>=n) g_j z^j.

This series has radius |alpha|=1/sqrt(2); the integration segment has length 1/2 and is strictly inside it. Its coefficients have the explicit finite formula

    g_(n+l)=alpha^(-n-1) [z^l]
      (i+z)^n [(i-1)+4alpha z+2z^2]^(2m)
      sum_(r=0)^l (-1)^r binom(n+r,r)(z/alpha)^r.   (2)

Indeed V(alpha+z)=z(i+z) and 2(alpha+z)^2-1=(i-1)+4alpha z+2z^2. Formula (2) lies in Q(i), has no asymptotic phase approximation, and retains the exact congruence-adjusted m.

For any integer K>=n define

    Z_K=-sum_(j=n)^K g_j h^(j+1)/(j+1).

Termwise integration gives

    Jplus=Z_K+r_K,
    lower contribution=-conjugate(Z_K)-conjugate(r_K). (3)

Every power h^(j+1)=2^(-j-1)exp(-i pi(j+1)/2) is retained. The additional phases in g_j are retained through (2), including (i-1)^(2m) and its higher binomial terms. An O(n) change in m is not removed from any expression.

## Uniform remainder without a fixed-order Watson assumption

Use the circle |z|=3/5 about alpha. On this circle,

    |V(alpha+z)|<=24/25,
    |alpha+z|>=1/sqrt(2)-3/5>1/10,
    |2(alpha+z)^2-1|<5.

The last inequality follows from |alpha|+3/5<4/3. Therefore the entirely explicit Cauchy bound

    |G(alpha+z)|<=Mstar,
    Mstar=10^(n+1)25^m

is valid. Cauchy's coefficient estimate gives |g_j|<=Mstar(3/5)^(-j). Along the segment, |h|/(3/5)=5/6, so

    |r_K|<=R_K,
    R_K=3 Mstar (5/6)^(K+1)/(K+2).                 (4)

This follows by summing the integrated Taylor tail, not by assuming a saddle-centered neighborhood is uniform. In particular (4) is valid for every n,m and K>=n. Its dependence on m is explicit and may be large; increasing K compensates for that dependence rigorously.

For a concrete depth set

    K=max(n, ceil(((n+1)log 10+m log 25
          +2n log n+2n log 2+log 12)/log(6/5))).     (5)

Then

    R_K <= (1/4) exp(-2n log n)2^(-2n).

For m=rho n log n+O(n), this depth is O_rho(n log n). No constant-order expansion has been extrapolated to a moving saddle. The price is a long explicit finite sum; no useful lower bound for its imaginary part is implied.

## Normalized logarithmic and complete errors

Define the signed rational quantity

    A_K=(-1)^(n+1) 2^(n+2) Im Z_K/U.

Equations (1)-(4) prove

    |Flog/D-A_K|<=eta_K,
    eta_K=2^(n+2) R_K/|U|.                         (6)

The arithmetic input |U|>=2^(n/2) and choice (5) give, in particular,

    eta_K<=exp(-2n log n).

This is an additive enclosure with both endpoint contributions included. It is not a relative saddle asymptotic or a proof of endpoint dominance.

The complete exponential upper bound supplied by the main selector argument is

    |Eexp/D|<=B_E,
    B_E=27(2(1+sqrt(2)))^n 7^(2m)
                      /((n+1)n!|U|).              (7)

It bounds the entire exponential residual, not its first term. On the exact allocation,

    log B_E <= -(1-2rho log 7)n log n+O_rho(n).

Thus B_E tends to zero factorially at the n log n scale in the stipulated rho range. Set Delta_K=eta_K+B_E. The complete signed enclosure is

    |c-(e+pi)-A_K|<=Delta_K.                       (8)

There is no missing reconstructed endpoint constant: this is a direct forcing quotient. All contributions of its two forcing columns are included in Flog and Eexp.

## Precise noncancellation condition

The finite data Z_K are defined explicitly without e or pi. If

    |A_K|>Delta_K,                                 (9)

then the complete error is nonzero, has the sign of A_K, and satisfies

    |c-(e+pi)| >= |A_K|-Delta_K.                    (10)

Equivalently, the two-contribution condition is

    |Im Z_K| > R_K + |U|B_E/2^(n+2).

This condition tests the signed sum of the two conjugate endpoint contributions. Neither their equal magnitudes nor their individual nonvanishing proves it. The long Taylor expansion gives an arbitrarily small certified remainder, but its finite signed sum can itself have strong cancellation.

No verification of (9) on an unbounded explicit subsequence has been obtained. In particular the dyadic congruence proving U!=0 is not a sign condition on Im Z_K. No equidistribution claim for a moving saddle phase is assumed. The exact O(n) allocation adjustment remains visible in every coefficient of Z_K.

## Actual primitive denominator cost

Use q for the positive denominator of c after full rational reduction. The provisional main arithmetic theorem gives exactly

    v2(q)=3n/2+2m-s2(n)-s2(n+4m).

Put q2=2 raised to that exponent. Then q>=q2, and (10), whenever its right side is positive, gives the genuine primitive-form lower bound

    q|c-(e+pi)| >= q2(|A_K|-Delta_K).               (11)

No coefficient clearer or unreduced height replaces q in (11). Along the allocation,

    log q2=2rho log 2 n log n+O_rho(n).

For example, an unbounded-subsequence theorem

    |A_K|-Delta_K >= exp(-sigma n log n+o(n log n)),
    sigma<2rho log 2,

would prove divergence of the primitive forms on that subsequence. Such a lower bound has not been established here. Conversely, failure to establish (9) does not prove that conjugate cancellation prevents all subsequence lower bounds.

## What this contribution establishes

The new result is the explicit two-contribution formula (2)-(3), its uniform growing-depth remainder (4)-(5), and the complete normalized enclosure (8). These address the permitted alternative when a lower bound remains open. They do not repeat the retained saddle-root derivation, nor pretend that a convergent expansion establishes moving-saddle dominance.

The remaining quantitative problem is to bound the signed finite combination Im Z_K from below on an explicit unbounded part of the congruence allocation, or to replace it by a shorter moving-saddle expression with a proved relative remainder and noncancellation. Its precise arithmetic and analytic threshold is (9), and its consequence using the actual compulsory q cost is (11).

No scans, numerical checks, or independent arithmetic review were performed. No unconditional shrinking-form, divergence, or irrationality conclusion is claimed. The companion report and this note require read-back before completion is reported.
