> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A sharper uniform accretivity constant for the exponential multiplier

Date: 2026-09-13. Original elementary continuation by root.
Independent review: PASS by audit_sources; see raw_sharp_accretivity_independent_review.md. This improves constants, not an exponent
or a missing determinant nonvanishing assertion.

For every complex number lambda on the unit circle,

    Re exp(lambda) >= exp(-1).

Proof. Write lambda=a+ib. For fixed b the smaller allowable a is
-sqrt(1-b^2). It suffices to prove

    log cos b - sqrt(1-b^2) >= -1,       |b|<=1.

The expression is even. On 0<=b<1 its derivative is
b/sqrt(1-b^2)-tan b>=0, because arcsin b>=b and tan is increasing
on [0,pi/2). Its value at zero is -1; continuity gives the endpoints.
Equality occurs only at lambda=-1.

Consequently, if K is unitary, the spectral theorem gives

    Re exp(K) >= exp(-1) I,       ||exp(K)||<=e.

For the odd boundary problem K(y)=[[0,t(y)],[1,0]] is unitary on
the real axis. Every finite compression E_m and the limiting E_+
therefore has inverse norm at most e. Surjectivity follows from the
same coercive bound for the adjoint: the range is closed and dense.
The already invertible A0 has inverse norm at most two, hence

    ||(A0 E)^(-1)|| <= 2e.

For the even scalar problem this also proves

    Re f(theta) >= e^(-1) w(theta),
    ||v||_w <= e sqrt(c_m),
    |b_r| <= e^2 sqrt(c_m D_r).

Indeed the actual coefficient equation implies
integral f|v|^2=v0. Evaluation at zero in the base metric has norm
sqrt(c_m), so e^-1||v||_w^2<=v0<=sqrt(c_m)||v||_w. The prediction
bound follows by subtracting a best base-metric predictor from the
negative monomial and using ||f/w||_infinity<=e.

The earlier sector-derived lower bound
v0>=e^-1 cos^2(1)c_m remains available; replacing it by the rough
norm/coercivity lower bound would unnecessarily weaken it.

This sharpening removes cos(1) from upper norm bounds and makes a
fixed-operator error certificate cheaper. It does not prove that the
two exceptional boundary determinants are nonzero.
