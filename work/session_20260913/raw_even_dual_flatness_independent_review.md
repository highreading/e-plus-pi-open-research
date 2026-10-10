> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of even-dual flatness and the full exponential error

Date: 2026-09-13. Reviewer: audit_computations.
Target: `raw_even_dual_flatness_and_exponential_error.md` by root.

**Verdict: PASS.** The actual coefficient bridge, complex-weight norm
constant, uniform all-coefficient summation, zero-free disk, full beta
error estimate, and exponential growth constants all check. No repair
is required. This is a theorem about the complete exponential error
in the specified primitive cofactor normalization; it does not bound
the combined primitive error or its endpoint gcd.

## 1. Actual moment and complex-weight normalization

The inverse vector is v=A^(-1)e_0=q/(n!V(1)), not the coefficient
vector of V. Because A is real and strictly accretive, v_0 is real
and positive. The Hermitian-part lower bound and inverse-corner upper
bound give

    ||v||_w^2 <= e v_0/cos(1)
              <= e^2 c_m/cos^2(1).

The constant in (1) is therefore correct. For a negative row,
b_r=integral f v z^r=<z^(-r),v>_f. Subtracting any polynomial in
span(z,...,z^n) preserves this integral by Av=e_0. The bound
|f|<=e w and Cauchy--Schwarz then give exactly

    |b_r|<=e^2/cos(1) sqrt(c_m D_(m,r)).

No positive-definite conclusion has been assumed for the complex
weight f itself. The base prediction distance is squared, so the
square root in this comparison is necessary and correctly present.

The factorial identity also checks directly:

    mu_n(z^(n+r)q)=integral f q z^r=n!V(1)b_r.

This is the derivative of order n+r of q(D)H_n at 1. Since
q(D)H_n(1+t)=t^nV(1+t), it yields coefficient n!b_r/(n+r)!
in the normalized V expansion. Terms with r>n vanish exactly;
there is no analytic Taylor tail in this polynomial identity.

## 2. Uniform sum and the zero-free disk

The independently audited all-r estimate has
sqrt(c_mD_(m,r))<=n^s/s!, where s=floor(r/2). Multiplication by
n!/(n+r)!<=n^(-r) gives n^(-s)/s! for r=2s and
n^(-s-1)/s! for r=2s+1. The constant term b_0=1 is exact,
so it is removed before applying the generic constant C. Summing
the two nonnegative majorants proves precisely

    |V(1+t)/V(1)-1|
      <=C[(exp(|t|^2/n)-1)+|t|exp(|t|^2/n)/n].

The estimate is valid for every complex t; the fixed-disk O(1/n)
statement and the extension to an expanding disk therefore follow
without an interchange of signed series or a fixed-index estimate.

For eta=log(1+1/(4C)) and |t|<=sqrt(eta n), the even majorant is
exactly 1/4 at the boundary. The odd majorant is at most 1/4 once
n>=16C^2 eta exp(2eta). Thus the normalized V is within 1/2 of
one throughout the closed disk. There are no zeros in that disk;
the stated weak inequality for the minimum root distance is valid
(the proof in fact excludes equality on the boundary as well).

## 3. Complete beta error, including the relative bound

For x in [0,1], the preceding estimate with t=x-1 gives a uniform
bound by 2C exp(1/n)/n, because exp(1/n)-1<=exp(1/n)/n.
There is no loss from a possible sign of V: the normalized polynomial
is written as 1+delta(x), with |delta| bounded pointwise.

The probability normalization is exactly

    B(n+1,n+1)/n!=n!/(2n+1)!.

For Y=X-1/2 under the symmetric beta distribution, the variance is
1/[4(2n+3)]. Symmetry gives E exp(-Y)=E cosh(Y). The function
(cosh y-1)/y^2 is increasing for y>=0, as is immediate from its
nonnegative power series. Its value at 1/2 gives the bound
4(cosh(1/2)-1). This proves the stated nonnegative xi_n and its
upper bound (cosh(1/2)-1)/(2n+3).

The contribution of delta is bounded in absolute value by
epsilon_n E exp(-Y). Thus the relative error is at most
xi_n+epsilon_n(1+xi_n), exactly as written. The parity sign
(-1)^n is +1 here because every statement is along even n.
The complete error therefore has the sign of V(1) for sufficiently
large even n. This sign conclusion is not inferred merely from a
finite Taylor coefficient.

## 4. Growth scale and constants

I independently cancel the factorials:

    B_m n!/(2n+1)!
       =1/[(2n+1)c_m]
       =m!(3m)!/[((2m)!)^2(4m+1)].

Stirling's formula gives
m!(3m)!/((2m)!)^2 ~ (sqrt(3)/2)(27/16)^m. With n=2m,
the full ratio is asymptotic to sqrt(3)/(4n) times
(3sqrt(3)/4)^n. Multiplying the root-product comparison constants
by exp(1/2) therefore gives exactly the stated lower limiting
constant sqrt(3)exp(-1/2)cos(1)/4 and upper limiting constant
sqrt(3)exp(3/2)/(4cos^2(1)).

The relative error factor 1+theta_n tends to one, so it does not
alter those liminf and limsup inequalities. Comparability with
beta^n/n gives the nth-root limit beta for |Re|/|v_n^lead|.
Because v_n^lead is a nonzero integer, the final lower bound on
|Re| follows. No exact asymptotic constant for the full inverse
corner, or for Re itself without dividing by v_n^lead, is asserted.

## 5. Scope and an immediate degree corollary

The target correctly keeps both the arctangent error and
gcd(|Z|,|Pe(1)+4Pa(1)|). Growth of one unreduced error does not
exclude signed cancellation or shrinking after division by that gcd.

One immediate consequence of the proved flatness, independent of
any new estimate, is V(0)/V(1)=1+O(1/n). Hence V(0)!=0 for every
sufficiently large even n. In the exact reciprocal normalization,
[z^(2n)]Qhat=w_n=(-1)^nV(0)=V(0), so Qhat then has full degree
2n and its leading coefficient has this same ratio to V(1).
This observation is optional and is not needed by the target.

No new degree solve, numerical integral, or scan was used in this
audit. Each normalization and all-index bound were checked directly.
