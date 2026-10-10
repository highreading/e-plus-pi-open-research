> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review: all-index exclusion of a triple root

Date: 2026-09-13. Reviewer: audit_sources.

**Result: pass; the opening wording clarification was incorporated.**
The proof in `raw_all_index_triple_root_exclusion.md` establishes
the stronger all-index statement H_n=q_2^2-3q_3q_1!=0 and hence
excludes a triple root of the actual cubic Q_n for every n>=1.
The opening word “Equivalently” should be “More precisely”:
H_n!=0 is sufficient for absence of a triple root, but is not
equivalent to it for a general cubic. The author has made this
correction. It was a wording issue, not a gap in the proved
stronger statement.

The even-degree proof is independently reviewed in
`raw_even_P_moment_gates_independent_review.md`. I checked the
entire odd extension, its new dominant-term case, the n=1
normalization, and the uniform canonical Hessian valuation.

## 1. The odd central derivative supplies the missing top coefficient

For odd n, the already proved exact penultimate-C valuation is

    v_2(c_(n-1))=M0=-n-2phi(n-1).

It is an all-index dependency, as recorded with its separate
odd proof in `raw_all_index_cubic_gate.md`; it is not extrapolated
from the even C estimate. The actual moment calculation gives
v_2(u_j)>=M0 for every j<n. Since Q_n'(0) is a dyadic unit,
the exact equation U'(0)=c_(n-1) then gives v_2(u_n)>=M0.
The derivatives of all lower Q_j have dyadically integral
coefficients, so no additional negative valuation occurs.

This proves the same full-polynomial lower bound used in the
even argument. It does not divide by Q_n(0), and it does not
require an endpoint or leading-cofactor approximation.

For the quadratic coefficient, same-parity pairs i<j<=n satisfy
i<=n-2, and the polarized estimate is

    M0+phi(n)-phi(n+1+i)+v_2(j-i)-1.

Since v_2(j-i)>=1 and phi(2n)-phi(2n-1)=1 when n is odd, this
is at least K0+1, with K0=M0-n. Opposite parities contribute
zero. For the linear coefficient the same argument handles
i<=n-2, and the pair (n-1,n) has eigenvalue difference 2n of
valuation one and gives the same lower bound. The exact
exponential correction has coefficientwise bound M0>=K0+1.
Thus p_1 and p_2 both have valuation at least K0+1 in every odd
degree, including the harmless n=1 endpoint cases.

## 2. The ordinary odd class

For n=3 mod 4, v_2(p_0)=K0, so p_1/p_0 and p_2/p_0 are even.
The proved reduction B_n=z^n mod 2 makes b_n a unit and both
b_(n-1), b_(n-2) even. The two exact coefficient formulas imply
q_2/q_3 even and q_1/q_3 odd. Therefore H_n/q_3^2 is a unit.
This reasoning preserves the full canonical polynomial rather
than selecting particular terms of its coefficient determinants.

## 3. The n=1 mod 4 class has a different unique lowest term

For n>=5 in this class, let a=v_2(n-1)>=2. The independently
proved Xi valuation is K0+2, so the available moment estimate
gives only

    v_2(p_1/p_0), v_2(p_2/p_0) >= -1.

That weaker bound is sufficient. The exact B leading valuation
and its reduction modulo 2 give

    v_2(b_(n-1)/b_n)=-a.

The all-coefficient lower bound gives
v_2(b_(n-2))>=phi(n)-phi(n-2)=a, so its ratio to b_n is
integral. Thus in

    q_2/q_3 = p_1/p_0+b_(n-1)/b_n+2

the middle term is uniquely least and has valuation -a. In the
formula for q_1/q_3, each term has valuation at least -a-1:
the potentially least product is
(b_(n-1)/b_n+3)(p_1/p_0). Hence

    v_2(q_2/q_3)=-a,
    v_2(q_1/q_3)>=-a-1.

Because -2a<-a-1 for a>=2, the squared term in H_n/q_3^2
is uniquely least. This proves its exact valuation -2a. It does
not assume that either p ratio is integral in this class, and
does not incorrectly reuse the even-degree dominant term.

## 4. Degree one and the uniform canonical valuation

For the saved degree-one cubic

    -464 z^3-1746 z^2-2697 z+1403,

I checked H=1746^2-3(464)(2697)=-705708. Its valuation is 2,
whereas the leading coefficient has valuation 4, so H/q_3^2
has valuation -6. This ratio does not depend on the common
scale of this displayed cubic.

In the canonical triple scale, b_1=8 and Xi_1=-29. Together
with the all-index identity q_3=b_n Xi_n, the three classes of
normalized Hessian valuations give exactly

    v_2(H_n)=2v_2(Xi_n), n>=1.

The scale qualification in the note is necessary and correct:
under multiplying the whole HP triple by c, H scales as c^6
and Xi^2 scales as c^4. Thus the unit formulation H/Xi^2 is
an assertion in the canonical normalization; H!=0 and the
valuation of H/q_3^2 are invariant under a common cubic scale.

## 5. Consequence for the carrier and retained limitations

The degree-three theorem is already independently proved, so
H_n!=0 indeed excludes a triple root of Q_n. If Q_n(1), Q_n'(1),
and Q_n''(1)/2 all vanished, Taylor expansion at 1 would make
Q_n=q_3(z-1)^3, contradicting this result. After clearing the
rational coefficients by a nonzero integral common factor,
the gcd of these three integers is therefore nonzero.

This establishes nonvanishing of the three-integer carrier at
every index. It does not estimate its magnitude or valuations
at large primes. A double root is still possible, so neither
squarefreeness nor a nonzero discriminant follows from the
present Hessian argument. No assertion about the rationality
or irrationality of e+pi follows without the remaining analytic
and primitive-denominator estimates.

No additional canonical degrees, numerical spectra, or prime
scans were used in this review.
