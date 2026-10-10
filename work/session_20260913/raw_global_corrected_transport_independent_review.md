> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the global corrected transport

Date: 2026-09-13. Reviewer: audit_computations.

Reviewed `raw_global_corrected_transport.md` in full, using the
previously reviewed first correction and explicit cocycle. All
substantive claims pass, including the extension to unbounded
`c` and the fixed-cut positive diagonal limit. No mathematical
repair is requested. I suggested spelling out the orientation of
one pointwise similarity in Section 3 for clarity.

## 1. Uniform resolvents on the unbounded half-plane

The identity `q+q^(-1)=4c+2`, together with the branch `|q|<1`,
does give `|q(c)|<=q(a)` on `Re c>=a`. For `r=|q|`, taking
real parts first gives `(r+r^(-1))cos(theta)>=4a+2`, hence
`r+r^(-1)>=4a+2`; the function is decreasing on `(0,1)`.

The bounds

    1/(|c|+1)<=|m(c)|<=1/|c|

are valid. The lower bound follows from the square-root sum in
the denominator. For the upper bound, the distance from `c` to
the negative interval `[-1,0]` is at least `|c|` when `Re c>0`.
The same geometric observation treats every negative eigenvalue
of the embedded finite row matrix. Its positive eigenvalues are
eventually at most `a/2`; their distance to `c` is at least
`|c|-a/2>=|c|/2`. Thus the claimed actual finite resolvent bound
`2/|c|` holds uniformly on the entire unbounded half-plane.

The geometric boundary vector and each fixed polynomially
weighted version have norm `O_a(1/|c|)`. The first-correction
weighted band estimates therefore give a sandwiched linear
remainder `O_a(1/(|c|^2 j^2))`; the second resolvent term has
the additional factor `1/|c|`. Absorbing that factor using
`|c|>=a` yields equation (3). Dividing by the nonzero `m` gives
the stated relative remainder. The squared Neumann correction
also fits it because `|c|^(-2)<=a^(-1)|c|^(-1)`.

This reasoning genuinely uses unbounded-parameter estimates. It
does not import a compact-`c` error bound with an uncontrolled
constant.

## 2. Exact transfer factorization and the anisotropic entry

From `M=Gamma^T R_phys Gamma`, the exact identity is

    T=M^(-1)Gamma^T=Gamma^(-1)R_phys^(-1).

At `x=cj^2`, with `G_j=Gamma_j/j^2`, division by `lambda=4/m`
therefore gives exactly

    Q_j=(G_j^(-1)/4)(R_bd/m)^(-1).

The first factor is lower triangular. Its top-right entry is
identically zero, including its second-order remainder. Hence
the upper-right entry of `Q_j-I-A/j` can receive only the
`1/|c|`-suppressed terms from the second factor and their
products with the first diagonal entry. This proves the
special `O_a(1/(|c|j^2))` entry estimate; the unsuppressed
lower-triangular remainder cannot enter it.

The correction coefficient is the same `A=-4G_1-B/m` as in
the first-correction proof. No transpose or scale is missing.

## 3. Reference cocycle and conjugation

The explicit `F(t,x)` obeys the stated generator equation.
The estimates on `A,cA'` are uniform when `Re c>=a`. In
particular

    A_12=1/[sqrt(c)(sqrt(c+1)+sqrt(c))],
    c A_12'=-1/[2s(c)(c+1)]

both have the required `1/|c|` bound. On `[j-2,j]`, the
time derivative of the generator uses `A+2cA'` divided by
`2t^2`, so it has the same entrywise suppression.

For clarity, the pointwise similarity preserving this estimate
can be written with `B_c=diag(1/|c|,1)` as
`B_c^(-1) G(t) B_c`. Its upper-right entry is multiplied by
`|c|`, while its lower-left entry is divided by `|c|`.
Both the transformed generator and its derivative retain the
ordinary uniform bounds. Undoing the similarity gives the
suppressed upper-right error in the original coordinates. The
separate unweighted estimate bounds all the other entries.
This use of `|c|` is only a pointwise norm argument and makes
no false holomorphy assertion.

The exact relation `w(j,x)^2=q(c)` gives the two bounds in
equation (10). Thus

    D_j^(-1) Delta_j D_j
       = [[Delta_11,Delta_12/w],[w Delta_21,Delta_22]]

is uniformly `O_a(j^-2)`. The upper-right term is actually
bounded by a constant times `1/(sqrt(|c|)j^2)`, hence by
`C_a/j^2`. The scalar and diagonal ratios over the two-unit
interval are bounded by their exact logarithmic derivatives.
The remaining exponentials have uniformly bounded norms and
inverses. This proves the corrected step estimate without
using an insufficient global condition bound for `F`.

## 4. Global products and parameter derivatives

For `Re x>=aN^2` and every earlier cut `j<=N`, the previous
estimates apply with `Re(x/j^2)>=a`. Casoratian separation
makes all required actual branch matrices invertible once
the starting cut is sufficiently large. The scalar lambda
factors commute, while the corrected matrices remain in their
correct ordered product.

The sum over the parity progression is at most `1/(2J)`.
The standard product norm estimate gives
`||W-I||<=exp(C_a/(2J))-1`. Once each step error is at most
one half, the inverse factor has error at most twice the
original error. This gives both inverse bounds in (13).
There is no dependence on a bounded ratio `N/J` or on an
upper bound for `|x|/J^2`.

On a fixed slightly larger compact neighborhood in `Re chi>0`,
the same bounds hold with uniform constants, and the matrices
are holomorphic. Cauchy's formula then gives (14). In
particular an arbitrarily slowly diverging initial cut is
permitted; the proof contains no hidden `J>>sqrt(N)` condition.

## 5. Fixed-cut diagonal limit and the initial head

For a fixed step `j`, the actual transfer divided by lambda
tends to `j^2 Gamma_j^(-1)/4`. Its upper-right entry is
`O_j(1/x)`. The latter estimate remains necessary even here:
conjugation by the diagonal factors of `F` multiplies that
entry by order `sqrt(x)`.

More explicitly, the entries before the bounded exponential
conjugations behave as follows:

* The top diagonal has multiplier
  `sqrt(w(j-2,x)/w(j,x)) -> sqrt((j-2)/j)`.
* The bottom diagonal has the reciprocal multiplier.
* The upper-right entry is `O_j(1/x)` divided by
  `sqrt(w(j,x)w(j-2,x))`, and tends to zero.
* The lower-left entry is bounded times
  `sqrt(w(j,x)w(j-2,x))`, and also tends to zero.

The scalar ratio tends to one and the exponential factors to
the identity. This proves exactly the two positive diagonal
limits in (15). Their deviations from one are `O(j^-2)`.

A fixed finite head therefore converges to its diagonal
product. The corrected tail is uniformly `I+O(1/L)` after
any later cut `L`, independently of the final `N`. Taking
the head limit first and then `L` to infinity proves (17).
This is a controlled ordered-product argument, not a formal
exchange of infinite limits. It also extends to any fixed
smaller `J>=1` by retaining finitely many initial steps.
The first such step is `j=J+2>=3`, so the square root
`sqrt(j/(j-2))` remains well-defined and finite.

## 6. Explicit diagonal product constants and scope

I checked the finite telescoping identity (20): the paired
denominator factors run through every `a_k`, `J+1<=k<=L`,
and the square roots telescope to `sqrt(J/L)`. The formula
for their product follows from

    a_k=k^2/[2sqrt((k-1/2)(k+1/2))].

The displayed gamma-ratio limit is `sqrt(pi/2)`, yielding
the stated expression for `d_J^+`. The finite ratio of
minus and plus products is exactly
`(L/J)a_(J+1)/a_(L+1)`; its limit is `2a_(J+1)/J`.
Thus both constants in (19) are correct and positive.

The final reconstruction preserves `F(J,x)^(-1)P_J(x)` and
the location of its matrix little-o factor. This matters
because the finite head contains different powers of `x`.
The note correctly declines to convert that matrix statement
into relative errors for individual entries that may cancel,
or into a mixed-node cofactor bound. No such conclusion is
needed for the proved global transport theorem.
