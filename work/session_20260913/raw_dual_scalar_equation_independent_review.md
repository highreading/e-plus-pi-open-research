> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the dual origin defects and scalar equation

Date: 2026-09-13. Reviewer: audit_computations.
Target: `raw_dual_origin_defects_and_scalar_equation.md` by root.

**Verdict: PASS.** The origin order argument, exact cofactor divisions,
exponential sign, infinity degree ledger, and local multiplicity claims
are correct. No substantive correction is required. The proof uses the
already independently accepted nonzero constant coefficient of Qhat and
the separate reviewed dual quadratic; it does not require generic
perfectness or an unproved degree assumption on the three polynomials.

## 1. Inputs and exact origin ledger

I checked the quadratic's defining convention against
`raw_dual_quadratic_and_endpoint_separation.md` and its independent
review. With y=(Q,P exp(-z),T-Q atan(z)), the identity is exactly

    W_012=exp(-z)z^(6n)K/(1+z^2)^2.

Subtracting the first column from the second gives g=-exp(-z)Re;
the third is h=-Ra. This is a constant column operation and therefore
preserves every derivative-row minor, not only W_012.

The nonzero Wronskian ensures that Q,g,h are independent. Echelonizing
g,h by constant combinations gives distinct finite orders a<b. The
orders 0,a,b are distinct, so their leading Wronskian determinant is
the nonzero Vandermonde in those orders. Its exponent is a+b-3.
This proves a+b-3=6n+ord_0K without a hidden leading cancellation.

If both coefficients at z^M of Re and Ra vanished, their orders
would be at least M+1. Multiplication of all three polynomials by z^2
would give degree at most 2(n+1), with both errors of order at least
M+3=3(n+1)+1. Its numerator polynomials are indeed the required Taylor
truncations, since no lower error term remains. The one-dimensional
simultaneous solution space at n+1 would force its Q to be proportional
to z^2Q_n, contrary to Q_(n+1)(0)!=0. Hence a=M and

    b=M+1+ord_0K.

The resulting unique projective exceptional combination is a constant
combination of exp(-z)Re and Ra. It cannot be applied directly to the
ungauged Re+4Ra, as the target correctly emphasizes.

The fallback ledger before using Q(0)!=0 is also exact: if ell=ord Q,
a=M+t, and b=M+t+1+s, then ell+a+b-3=6n+ell+2t+s, giving
ell+2t+s=ord_0K. Distinctness holds because ell<=2n<M.

## 2. Polynomial cofactor normalization and origin division

After differentiating the functions, addition of atan(z) times the
first column to the third leaves in row r

    T^(r)-sum_(j=1)^r binom(r,j)Q^(r-j)atan^(j).

For r<=3 all denominators divide D^3. There is only one such column
in each determinant, so multiplying the determinant by D^3 suffices;
one does not need to multiply all three rows separately by D^3.
Factoring exp(-z) from its single exponential column leaves
(partial-1)^rP. These operations prove that D^3 exp(z)W_ijk is a
polynomial. In fact its coefficients are integral for the actual
integral input, slightly stronger than the claimed rationality.

For the row sets 023 and 123, the two error columns have distinct
orders at least M,M+1. Their lowest possible total order arises when
they take derivative rows 2 and 3, giving 2M+1-5=6n-2. The remaining
Q derivative is analytic, so contributes no negative order. Every
determinant term has at least this order. Thus division by z^(6n-2)
is exact in both A1 and A0. Multiplication by exp(z) and D^3 does
not change the order at zero.

The alternating signs from expansion of the four-by-four Wronskian
are W_012, -W_013, W_023, -W_123, in derivative order 3,2,1,0.
The common multiplier D^3 exp(z)/z^(6n-2) gives A3=z^2DK exactly.
Since W_013=W_012', it gives

    A2/A3=1-6n/z+2D'/D-K'/K.

In particular the +1 sign is correct for exp(-z). All three original
functions solve the equation, and on an ordinary local domain the
nonzero Wronskian makes them its full three-dimensional solution space.

## 3. Infinity ledger and the two remaining signs

P is nonzero because P(0)=Q(0)!=0. The Laurent pair consisting of Q
and T-Q(atan-atan(infinity)) is also independent: otherwise atan
would be rational. Its derivative 1/(1+z^2) has nonzero simple-pole
residues, which a derivative of a rational function cannot have.

Keep Q as the first Laurent member, c=deg Q, and cancel its highest
power in the second member if necessary. This gives a distinct
integer highest power d. Both are at most 2n, as is b=deg P.
In the leading Wronskian term the exponential column occupies row 2
and the Laurent columns occupy rows 0,1. Its power is
exp(-z)z^(b+c+d-1), with a nonzero multiple of d-c. Comparison with
the quadratic identity therefore gives

    b+c+d=6n+deg K-3.

Each deficit from 2n is nonnegative, and their sum is 3-deg K.
This validates all degree-defect claims even when one Laurent power
is negative. For deg K=2, distinctness forces the Laurent deficits
to be 0 and 1 and the exponential deficit to be 0.

Writing leading Laurent functions as z^c,z^d and the exponential
as exp(-z)z^b recovers both remaining signs directly:

    W_023/W_012=-(c+d-1)/z+O(z^-2),
    -W_123/W_012=cd/z^2+O(z^-3).

In the first expression, derivative row 3 of the exponential supplies
-1, while the Laurent 0,2 determinant supplies (d-c)(c+d-1).
In the second, the Laurent 1,2 determinant supplies cd(d-c).
The cofactor signs then give the displayed formulas. They remain
valid when their leading coefficients vanish.

Since A3 has exact degree deg K+4, these asymptotics prove the
claimed degree bounds and the two leading-coefficient formulas.
They imply no convergence of the bounded-degree coefficient tuple.

## 4. Indicial equation and local multiplicity restrictions

If K(0)!=0, divide by A3. The equation is regular singular at zero.
The three known orders 0,M,M+1 determine its monic indicial polynomial.
Alternatively, substitution of z^r gives

    r[(r-1)(r-2)-6n(r-1)+A1(0)/K(0)].

Matching this with r(r-M)(r-M-1) yields precisely
A1(0)=3n(3n+1)K(0). A0 contributes at the next power and does not
alter this indicial calculation. The target appropriately avoids
using this generic coefficient formula when K(0)=0.

At a point away from 0 and the poles +/-i, all three functions are
analytic. If h=ord_aK, their three distinct echelon orders sum to
h+3. The largest is at most h+2, since the other two distinct
nonnegative orders sum to at least 1. Thus every nonzero local
combination has order at most 2+h<=4. For h=1 the only possible
triple is (0,1,3), giving an apparent singularity. This is a local
multiplicity result, not a count of distinct zeros across an interval.

## 5. Bounded independent normalization controls

`check_raw_dual_scalar_equation_existing.py` reads only the frozen
n=1,2 polynomials from the existing dual-error JSON. It constructs
the cleared derivative rows independently through order three,
forms all four minors, and checks their exact origin divisions.
It verifies all three equations after clearing the universal
exponential and logarithm, the origin echelon order, the K(0)
coefficient, the infinity ledger, and the leading signs.

All assertions pass; results are saved in
`raw_dual_scalar_equation_existing_checks.json`. Both controls have
origin orders (0,3n+1,3n+2), infinity degrees (2n,2n,2n-1), and
coefficient degrees (6,6,5,4). No new canonical degree was solved.
The all-index proof above does not depend on these two controls.

No correction or missing bridge was found. The target properly
leaves connection estimates and the primitive endpoint gcd unresolved.
