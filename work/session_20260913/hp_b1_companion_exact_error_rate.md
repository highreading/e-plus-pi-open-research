> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact factorial error of the existing degree-one rational companion

Date:2026-09-13. Root continuation; independent review FULL PASS in
`hp_b1_companion_error_independent_review.md` (audit_computations).
This is a new application of the project's already proved factorial
determinant method, not a claim that the method itself is new.
It closes the faster-error escape suggested in
hp_b1_primitive_arithmetic_attempt.md, Section4. It does not bound the
actual reduced HP endpoint denominator.

## 1. Statement and existing inputs

Use exactly the original F(z)=4 arctan(z/(2-z)), the functionals
ell_j(t^k)=1/(n+k+1-j)!, j=0,1, and the previously proved objects

    U=p_(n+1), V=K_n(t,1), W=1/(1-t)-H_n(t),
    t_j=ell_j(V), w_j=ell_j(W), delta=t_1-t_0.

H_n here is the orthogonal projection of1/(1-t); it is not the special
integer polynomial also denoted H in the auxiliary-gcd notes.
Let r_n^* be EXACTLY the rational companion defined in Section4 of
hp_b1_primitive_arithmetic_attempt.md. Then

    e-r_n^* = (t_1 w_0-t_0 w_1)/delta,                         (1)

and

    e-r_n^* ~ e^(-sqrt(2)) W(0)/(n^3 n!).                    (2)

In particular its sign is (-1)^(n+1) eventually, and

    log|e-r_n^*|=-n log n+n+o(n).                            (3)

Thus an estimate exp(-2n log n+O(n)) is impossible for THIS companion
on every unbounded subsequence. This leaves the reduced companion height
and actual HP endpoint gcd as arithmetic unknowns.

All analytic inputs below are in hp_b2_endpoint_attempt.md, Sections3-5,
and its independent review. The exact two-functional determinant kernel
and its domination method are already in hp_moving_mobius_parameter.md,
Section2. Here the original fixed parameter has c=sqrt(2), not c=1.

## 2. Exact error identity with all signs

Write g_j=[T_n(C_j F)](1), E_k=sum_(r=0)^k1/r!, and
a_j=-E_(n-j)-g_j. The raw endpoint representative is

    X=(1+t_1)a_0-(1+t_0)a_1, Y=delta,
    f_n^*=(g_0-g_1+1/n!)/delta,
    r_n^*=-X/delta-f_n^*.

The elementary logarithmic tail is C_j(1)pi-g_j=-ell_j(H_n).
Since C_j(1)=-t_j, this proves

    g_j=ell_j(H_n)-pi t_j.

The factorial tail identity gives
(ell_1-ell_0)(1/(1-t))=1/n!. Hence

    f_n^*=pi+(w_1-w_0)/delta.

The raw matched remainder is

    R_raw=(1+t_1)w_0-(1+t_0)w_1
         =-(1+t_1)(w_1-w_0)+delta w_1.

Because R_raw=X+delta(e+pi), direct substitution gives

    e-r_n^*=R_raw/delta+(w_1-w_0)/delta
            =w_1-t_1(w_1-w_0)/delta,

which is(1). No approximate cancellation is used here.

## 3. Determinant asymptotic at the cancellation scale

The passed degree-two analysis proves, on a fixed disk about zero,

    U(z/n)/U(0) -> exp(-c z), c=sqrt(2),
    V/V(0)=(U/U(0))G_V, W/W(0)=(U/U(0))G_W,

where G_V,G_W are uniformly bounded analytic functions, both equal1 at
zero, and

    G_V'(0)->1+1/sqrt(2), G_W'(0)->1/sqrt(2).

The reciprocal roots of U have modulus at most2. Put H=G_W-G_V;
then H(0)=0 and H'(0)->-1. Define

    D(P,Q)=ell_0(P)ell_1(Q)-ell_1(P)ell_0(Q).

For P=sum P_k t^k,Q=sum Q_l t^l the exact identity is

    D(P,Q)=sum_(k,l>=0) (l-k)P_k Q_l /
                       ((n+k+1)!(n+l+1)!).                 (4)

Let U/U(0)=sum u_k t^k. The root bound gives
|u_k|<=binom(n+1,k)2^k, and u_k/n^k->(-c)^k/k!.
For the pair U,tU, multiplication of(4) by(n!)^2 n^3/U(0)^2
gives a summable limit with terms

    (j+1-k)(-c)^(j+k)/(j! k!).

The double sum is exp(-2c): the j-k terms cancel by symmetry.
Domination is by a fixed multiple of
(j+k+1)4^(j+k)/(j!k!), using the factorial ratios and the root bound.

For a pair t^r U,t^s U, the corresponding normalized absolute bound
is at most C(r+s+1)n^(1-r-s). Expand G_V and H in their uniformly
Cauchy-bounded Taylor coefficients. Since H(0)=0, terms with r+s>=2
sum to O(1/n), while the only r+s=1 term has r=0,s=1 and coefficient
H'(0)->-1. This also justifies all infinite interchanges, by taking
n larger than twice the inverse common analytic radius.
Consequently

    D(V,W) ~ -V(0)W(0) exp(-2c)/((n!)^2 n^3).             (5)

The first-order factorial lemma already proves

    delta ~ V(0) exp(-c)/n!.

Equation(1) is -D(V,W)/delta. Dividing(5) by the last NONZERO
asymptotic proves(2). The sign of W(0) is (-1)^(n+1), from the exact
identity cited next, so(2) proves the stated eventual sign without
using irrationality of e to assert nonvanishing.

## 4. The residual W(0) has no exponential rate

The passed reference identities give

    V(0)=2p_n(1)p_(n+1)(1)/|h_n|,
    W(0)/V(0)=(-1)^(n+1)epsilon_n(1+alpha_n^*/b_n)/2,
    b_n=p_(n+1)(1)/p_n(1)->(1+sqrt(2))/4,
    alpha_n^*->(1-sqrt(2))/4,
    log(epsilon_n)/n -> -2log(1+sqrt(2)).

The exact norm h_n=2(-1)^n/((2n+1)binom(2n,n)^2) has
log|h_n|/n->-log16. The positive recurrence ratio for p_n(1) gives
log p_n(1)/n->log((1+sqrt(2))/4). It follows that

    log V(0)/n ->2log(1+sqrt(2)),
    log|W(0)|/n ->0.

The factor1+alpha_n^*/b_n has a positive nonzero limit, so it cannot
alter either the sign or this rate. Combining with(2) and Stirling's
formula proves(3). In particular, the discrepancy between(3) and a
bound -2n log n+O(n) is n log n+O(n), which diverges even on an
arbitrary unbounded subsequence.

## 5. Scope and next step

This deduction resolves the previously open possibility that the SAME
rational companion had a hidden second factorial order. Its exact
error has first factorial order with a cubic polynomial improvement.
It does not show that another companion cannot be better, and it does
not decide q_n=den(X/delta). The coefficient-clearer obstruction was
already proved separately. A useful next arithmetic step must act on
the actual reduced endpoint gcd or construct a different companion
with its own proved error AND reduced-height estimates.
