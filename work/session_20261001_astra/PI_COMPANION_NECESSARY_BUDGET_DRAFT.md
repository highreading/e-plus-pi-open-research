> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Necessary denominator budgets for complete rational companions

Status: main-agent author proofs, not independently reviewed. This note preserves the previously unsaved correction threshold and the inequality that does not require logarithmic dominance in advance. The external approximation input for pi has now been located and its statement and quantifiers read in the retained primary-source text. No new numerical calculation is claimed. These results concern specified approximation families and do not decide the rationality of e+pi.

## 1. Published quantitative input and exact quantifiers

Doron Zeilberger and Wadim Zudilin, The irrationality measure of pi is at most 7.103205334137..., arXiv:1912.06345v2, revised January 2020. The retained primary text is work/session_20260913/zeilberger_zudilin_1912.06345.txt; page 1 states the bound and defines the irrationality measure using every strictly larger exponent and all sufficiently large denominators. Source URL: https://arxiv.org/abs/1912.06345 .

The main has read that primary passage. This is use of a published theorem, not a fresh independent verification of its entire proof. No newer preprint is needed here.

Choose the safe rational exponent

    mu=36/5=7.2.

Since this is strictly above the published bound, there is a constant C_pi>0 such that, for every reduced rational u/v with v>=1,

    |pi-u/v|>=C_pi v^(-mu).                         (1)

Indeed the primary theorem supplies the assertion with constant one for sufficiently large v. For each of the finitely many smaller denominators, minimize over the nearest integers u to v*pi. Irrationality of pi makes every resulting distance positive. Decreasing the constant proves (1) for all denominators. No numerical value of C_pi or its denominator threshold has been computed.

The retained elementary project theorem for e supplies, for every epsilon>0, a constant C_epsilon>0 such that

    |e-u/v|>=C_epsilon v^(-nu), nu=2+epsilon,        (2)

uniformly over reduced rationals. Its previously saved proof is an input; it is not rerun here.

This resolves the source-location dependency in FINITE_MEASURE_COMPANION_TRANSFER_DRAFT.md and GENERAL_SMALL_SELECTOR_COMPLETE_EXCLUSION_DRAFT.md. Their construction-specific estimates remain author inputs with their original hypotheses; neither draft acquires independent review status from this source confirmation.

## 2. A complete inequality without a dominance premise

Let alpha and gamma be rational numbers, and define

    S=e+pi, c=alpha+gamma,
    q=den(c), B=den(gamma), R=q|c-S|.

All denominators are positive reduced denominators. Let E>0 satisfy |e-alpha|<=E. No assumption about the size, sign, or nonvanishing of c-S is made.

Since alpha=c-gamma, its reduced denominator is at most qB. Equation (2) gives

    E>=C_epsilon(qB)^(-nu),
    1/q<=C_epsilon^(-1/nu) E^(1/nu) B.             (3)

On the other hand, the complete decomposition gives

    C_pi B^(-mu)<=|pi-gamma|<=E+R/q.

Multiplying by B^mu and using (3) proves

    C_pi<=E B^mu
          +R C_epsilon^(-1/nu) E^(1/nu) B^(mu+1). (4)

Both error components remain in this inequality. It uses no contour-sign assertion, exact dyadic law, or premise that the logarithmic error dominates. It remains valid when R=0.

## 3. Necessary budget for bounded primitive errors

Let X tend to infinity along a sequence of such companions. Assume

    liminf (-log E)/X>=a>0,
    R is bounded.

Then

    liminf log B/X>=a/[2(mu+1)].                    (5)

Proof. If (5) fails, there is a subsequence and b<a/[2(mu+1)] with log B<=bX. Choose epsilon>0 so small that (mu+1)b<a/(2+epsilon). This also implies mu b<a. Allowing an arbitrarily small slack in the hypothesis on E, both terms on the right of (4) tend to zero on that subsequence, contradicting C_pi>0. This proves (5), including cases where B does not tend to infinity.

For X=n log n and a=1, equation (5) is

    liminf log B/(n log n)>=5/82.                   (6)

The condition is necessary for bounded primitive errors, not sufficient for small primitive errors.

There is also a direct divergence conclusion. If

    limsup log B/X<=b<a/[2(mu+1)],

then the reverse triangle inequality applies eventually because E is negligible compared with C_pi B^(-mu). Combining it with (3) gives

    R>=(C_pi/2) C_epsilon^(1/nu)
                     E^(-1/nu) B^(-(mu+1)).

Therefore

    liminf log R/X>=a/2-(mu+1)b>0.                 (7)

Only strict inequalities give the asserted divergence. No positive rate at the boundary is claimed.

## 4. Additional information from the actual center denominator

Suppose, in addition to the assumptions of Section 3, an established estimate gives

    liminf log q/X>=g>=0.

Use the original inequality C_pi B^(-mu)<=E+R/q, without replacing q by (3). Bounded R and the two lower exponential rates imply

    liminf log B/X>=min(a,g)/mu.

Combining this with (5) gives the necessary condition

    liminf log B/X
      >=max{a/[2(mu+1)], min(a,g)/mu}.              (8)

For a=1 and mu=36/5 this becomes

    liminf log B/X
      >=max{5/82, (5/36)min(1,g)}.                 (9)

The estimate for q must concern the same fully reduced center and the same indices. A coefficient clearer or lift index cannot supply g.

For the saved large-selector family with corrections of subfactorial denominator, DYADIC_CORRECTION_COMPANION_TRANSFER_DRAFT.md would supply g=2rho log 2 if the pending complete dyadic theorem is established. That application of (9) remains conditional on that theorem. Equations (4)-(7) do not depend on it.

## 5. Rational corrections in the general small-selector class

Retain precisely the construction and hypotheses of GENERAL_SMALL_SELECTOR_COMPLETE_EXCLUSION_DRAFT.md: primitive integer selectors of degree d and coefficient height H, nonzero integer forcing U, and

    d+log H=o(n log n).

Its saved companion and height estimates give

    -log E=n log n+o(n log n),
    log den(beta)=o(n log n).

Let r be any rational correction and put gamma=beta+r. Since

    den(gamma)<=den(beta) den(r),

bounded complete primitive errors necessarily imply

    liminf log den(r)/(n log n)>=5/82.             (10)

Thus corrections with subfactorial reduced denominator cannot rescue this selector class. Numerator size of r is not restricted by this argument. The denominator in (10) is reduced; no separate factorial clearer is substituted for it.

Without such a correction, or with log den(r)=o(n log n), the same estimates give the stronger divergence rate

    liminf log(q|c-S|)/(n log n)>=1/2.

This is an author deduction using the published pi theorem and the retained selector estimates. It does not assert that every canonical reconstructed selector satisfies the small-height hypotheses.

## 6. Large-selector small-rho consequence

Consider the saved large-selector construction with n=4k, U!=0, and

    m=rho n log n+o(n log n), rho>0 fixed.

The saved factorial exponential bound and forcing bounds give a=1 at scale X=n log n. The logarithmic companion bound gives

    limsup log den(beta)/X<=4rho log 4.

The newer author refinement den(beta) divides O_J|U|/2, J=n+4m, supplies the same leading upper rate. Its exact content factorization does not by itself improve that rate.

Taking gamma=beta in (7) proves, under these retained construction estimates,

    liminf log(q|c-S|)/(n log n)
       >=1/2-(164/5)rho log 4>0

whenever

    0<rho<5/(328 log 4).                           (11)

The conclusion holds on every admitted nonzero-forcing sequence in this domain. No weighted-difference certificate or exact dyadic denominator theorem is needed for (11). Larger rho remains outside this particular argument.

## 7. Extension for a prescribed shrinking rate

A further consequence of (4) records the cost of requesting faster shrinking. Suppose

    liminf (-log E)/X>=a>0,
    R<=exp(-sigma X+o(X)), sigma>=0.

The same subsequence contradiction, followed by epsilon decreasing to zero, proves

    liminf log B/X
      >=min{a/mu, (a/2+sigma)/(mu+1)}.              (12)

To verify this, any subsequence strictly below both thresholds makes the first term of (4) decay with exponent -a+mu b and the second with exponent -sigma-a/nu+(mu+1)b. Choosing nu sufficiently close to two makes both exponents negative. This argument also accommodates R=0, since only an upper bound for R is used.

If the actual center denominator additionally has lower rate g, then the original complete inequality gives

    liminf log B/X>=min(a,g+sigma)/mu.              (13)

The maximum of the right sides of (12) and (13) is therefore necessary. These are lower requirements for companion denominator growth, not constructions meeting those requirements.

## 8. Canonical bridge and remaining status

Child 3 reports a saved exact canonical expression B=D_joint/G_joint, retaining the endpoint correction, and factorial exponential accuracy in its stated slow-growth domain. The main has not yet inspected that full new bridge at the time this note is requested for preservation. No uninspected canonical formula is used in the proofs above.

Once that bridge and its hypotheses are checked, (6) says bounded primitive errors require liminf (log D_joint-log G_joint)/(n log n)>=5/82. A proved upper bound below 5/82 would instead give a branch exclusion. Failure to establish such a gcd estimate proves neither small errors nor noncancellation.

Pending work includes the main inspection of the canonical bridge, the sole designated independent examination of new decisive claims when appropriate, and actual denominator/content estimates on useful unbounded families. The published pi source no longer needs to be located. No completed calculation has been repeated, and no claim about the irrationality of e+pi is made.
