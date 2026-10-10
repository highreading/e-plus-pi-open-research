> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of actual branch columns and the upper-cut kernel limit

Date: 2026-09-13. Reviewer: audit_computations.

Reviewed `raw_actual_branch_column_asymptotics.md` in full.
The fixed-cut constants, unequal powers, derivative convergence,
linear condition-number limits, and prescribed high-kernel
dominance all pass. No mathematical correction is requested.
The limitations concerning growing determinants and small
scaled nodes are preserved correctly.

## 1. Exact starting rows and unequal column powers

I derived the first two rows beyond the seeds directly from
the actual symmetric recurrence. At row zero,
`b_0=1/3`, `a_1=1/sqrt(3)`, and `a_2=4/sqrt(15)`, giving

    R_2=(sqrt(5)(6x+1)/8, sqrt(15)/4).

At row one, `b_1=-3/5`; substitution of the preceding row
and both seed rows gives

    R_3=(sqrt(7)(15x+8)/24, sqrt(21)(5x+8)/36).

Inverting the exact cocycle gives its first row of sizes
`sqrt(x)` and `x^(-1/2)`, and its second row tends to
`(-sqrt(J/2),sqrt(J/2))`. Thus the first-row off-diagonal
does not vanish identically and must be retained until after
the column scaling. It causes no omitted leading term in
the two limits in (3).

For `J=1`, the first column is led by the second row, with
coefficient `3sqrt(5)/(4sqrt(2))` times `x`; the second
column is led by the first row, with coefficient `sqrt(2)`
times `sqrt(x)`. For `J=2`, the leading coefficients are
`3sqrt(5)/4` times `x^(3/2)` in the first column and
`5sqrt(21)/36` times `x` in the second column. Every other
normalized entry tends to zero. These verify both the powers
and the positions of the leading directions.

## 2. Diagonal product constants and the column matrix

Substitution of `J=1,2` into the previously reviewed gamma
product gives exactly

    D_1=diag(4sqrt(3)/(3pi),32sqrt(5)/(15pi)),
    D_2=diag(4sqrt(10)/15,12sqrt(14)/35).

Multiplying the starting limits gives

    C_even=diag(sqrt(2),sqrt(6)/3),
    C_odd=(4/pi)sigma_1 C_even.

No row radical or odd-column constant is missing. The exact
identity `F(N,cN^2)=N^(-1/2)B(c)` follows by substituting
in all three scalar, diagonal, and exponential factors.
The fixed-cut corrected matrix converges before multiplication
by the already column-scaled initial matrix, so (7) follows
without promoting an absolute matrix error to an unjustified
relative entry error.

All normalized factors are holomorphic on a fixed slightly
larger compact subset of the right half-plane once `N` is
large. The column powers have the consistent principal
logarithm. Therefore Cauchy's formula gives the asserted
first and second derivative convergence of the *fully*
normalized matrix. No derivative of an unremoved scalar
exponential has been neglected.

## 3. Condition numbers and individual singular values

After factoring the common scalar and the smaller column
power, the remaining matrix is
`(A_parity+o(1))diag(sqrt(x),1)`. Dividing it by `sqrt(x)`
gives a rank-one limit with norm `||A_parity e_0||`.
The exact determinant product then proves the smaller
singular-value limit. This argument remains valid without
any rate on the original matrix little-o.

For even parity,

    |det A_even|=(2/sqrt(3))(c+1)^(-1/2),

while the squared first-column norm is twice that scalar
factor `(c+1)^(-1/2)` times the bracket displayed in (11).
Their ratio is `sqrt(3)` times the bracket. For odd parity,
the common squared multiplier `(4/pi)^2` cancels and the
hyperbolic sine/cosine positions are reversed. Multiplication
by `sqrt(c)` gives both stated limits of `cond(P_N)/N`.
The positive-axis singular-value formulas retain the exact
lambda product and both unequal powers as required.

## 4. The mixed-node kernel and the diagonal

The Green identity and symmetry of `M_N` give exactly

    Kcal_N(x,y)=P_N(x)^T
                (M_N(x)-M_N(y))/(y-x) P_N(y).

The sign agrees with the positive diagonal `-M_N'(x)`.
Writing `M_N(cN^2)/N^2=m(c)I/16+O(1/N)` gives the
stated divided-difference limit. A derivative bound on a
slightly enlarged convex compact set makes it uniform as
`d` approaches `c`. Thus there is no unbounded division
by a vanishing `d-c`.

From `c=(q+q^(-1)-2)/4`, I checked the exact identity

    (m(c)-m(d))/(16(d-c))
       =q(c)q(d)/(1-q(c)q(d)).

The denominator is nonzero throughout the stated domain.
The transpose convention is correct for the holomorphic
kernel; a conjugate transpose would be a different object.
Column scaling on both sides cancels the exact powers in
the two branch matrices and yields (16). Local uniform
holomorphy justifies fixed-order parameter derivatives too.

## 5. The logarithmic-endpoint scalar-product sum

For a fixed starting cut `J=1` or `2`, the exact logarithm
of the lambda product is the parity-lattice sum

    2 sum_(j=J+2,J+4,...,L) asinh(sqrt(c)/(j/n)).

On the right half-plane the chosen logarithm agrees with
this expression by continuation from positive real `c`.
Write its summand function as

    log(2sqrt(c)/t)+h_c(t),
    h_c(t)=log((1+sqrt(1+t^2/c))/2).

The remainder extends smoothly through `t=0` with
`h_c(t)=O_K(t^2)` and bounded derivative on the relevant
compact interval. Its Riemann-sum error is uniformly `O(1)`.
For the term `-log t`, the parity product is evaluated using
`Gamma(L/2+1)/Gamma(J/2+1)`; Stirling's formula gives
an `O(log n)` difference from the integral. The fixed
omitted starting points also contribute only `O(log n)`.
This verifies (17) for both actual parity lattices.

Replacing the lower endpoint ratio `(n+1)/n` by one costs
only `O(1)` after multiplying by `n`. Therefore subtraction
gives (18). The real part of its integral is strictly
positive throughout the right half-plane, since
`Re asinh(sqrt(z))=-log|q(z)|/2>0`. Its compact minimum
is positive. The `O(log n)` loss is only polynomial and
is absorbed by a smaller exponential rate.

## 6. Exact upper-cut normalization and scope

The upper cut `2n` is always even. If the lower cut `n+1`
is even, its column powers equal the upper ones. If it is
odd, each power is exactly one half smaller, giving an
additional scalar `x^(-1/2)` after the upper normalization.
All remaining cut-size and power factors are polynomial.
The scalar product ratio from Section 5 therefore makes
the lower-cut kernel exponentially small, uniformly in
both parameters on compact subsets. Uniformity near the
diagonal follows from the same analytic divided-difference
argument; fixed derivatives follow by Cauchy's formula.

The total high-kernel error remains unquantified little-o,
because the accepted fixed-cut column limit has no rate.
The note states this explicitly.

For distinct positive parameters, the limiting scalar kernel
has the positive expansion `sum_(r>=1)q(c)^r q(d)^r`.
Its finite Vandermonde feature matrix proves strict positive
definiteness. The first components of both selected column
vectors are nonzero on the positive axis; their diagonal
congruence already gives a positive definite contribution,
and the second components add a positive semidefinite one.
This verifies the fixed-size selected-channel statement.

It gives no uniform lower eigenvalue bound for a growing
number of moving nodes. The note correctly leaves both
that stability problem and the excluded `c->0` nodes open,
and retains the actual spectral amplitudes. No mixed-node
determinant or irrationality claim is inferred.
