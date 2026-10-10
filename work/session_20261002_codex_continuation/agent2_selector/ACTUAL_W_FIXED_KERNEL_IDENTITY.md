> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A fixed polynomial kernel for the actual weighted certificate

2026-10-02. Author identity supporting the parent-requested direct nonvanishing / quotient-Casoratian target. The archive and primary-paper search before pursuing this structural target is recorded in `PERIOD_CASORATIAN_TARGET.md`. This note concerns the actual W and its full contour; it does not identify the positive complete period with W and does not prove an O(1)-shift theorem.

## 1. Identity without a selector-dependent kernel

Let n=2r≥2, d=n+1, and retain the actual coefficients a_j and U from `ACTUAL_U_ROOT_GEOMETRY.md`. Set

    V(w)=w²−w+1/2,  t(w)=1−2w²,  A(w)=t(w)²,
    h_n^full(t)=V(w(t))^n/(4w(t)^(n+2)),
    D_t=−(4w)^(-1)D_w.

The branch w(t) is the one obtained from the original contour C from bar a to a; it is nonzero there. Define the fixed rational expression

    P_n(w)=−4w(1−t(w)²)^(n+1)
      Σ_(ell=0)^r [2^ell a_(n−2ell)/ell!]
           D_t^ell[t^ell h_n^full(t)]|_(t=t(w)).       (1)

Then P_n is a polynomial with real rational coefficients, independent of m. For all integers m≥0, the actual weighted certificate satisfies

    W(n,m)=i2^(n+1)∫_C A(w)^m P_n(w)dw.              (2)

For n=4k this is exactly the W of the saved weighted-difference construction, with its original normalization. In particular the actual n+1 difference has not been replaced by a lower difference or by a different rational center.

To prove (2), transform the original full moment:

    I_m=∫_C V(w)^n A(w)^m/w^(n+1)dw
       =−∫_Γ t^(2m)h_n^full(t)dt,

where Γ has endpoints 1+i and 1−i. Use

    U(n,m)t^(2m)=Σ_ell (-2)^ell a_(n−2ell)/ell!
                         ·t^ell D_t^ell t^(2m).

Taking the actual d-th difference multiplies the undifferentiated t^(2m) by (t²−1)^d. Integrating each term ell times by parts changes (-2)^ell to 2^ell; since d is odd it changes the overall sign into the (1−t²)^d in (1). Every boundary term vanishes: h_n^full has a zero of order n at each Γ endpoint because V(a)=V(bar a)=0, and its differentiated orders in a boundary term are at most ell−1≤r−1<n. The endpoint branch and powers of t are analytic and finite there. Finally substitute dt=−4w dw and multiply by the exact i2^(n+1) linking W to Δ^d(U I). This yields (1)–(2). No U value is divided out.

## 2. Uniform polynomial factorization

Every term inside the sum in (1) has poles only at w=0, of order at most n+2+2ell. Multiplication by

    (1−t²)^d=[4w²(1−w²)]^d

and the extra w removes them, with remaining w-order at least 1 since ell≤r. Differentiating V^n at most ell times leaves a factor V^(n−ell), hence every term has V^r. The factor (w²−1)^d is explicit. Therefore

    P_n(w)=w(w²−1)^(n+1)V(w)^r R_n(w),               (3)

for a real rational polynomial R_n of degree exactly 2n.

The degree bound follows because D_t lowers the power at infinity by two and t^ell adds 2ell: every inside summand has degree at infinity at most n−2, giving deg P_n≤5n+3. Its leading coefficient does not cancel. At infinity, the leading contribution of D_t^ell[t^ell h_n^full] is

    (1/4)(1/2)^ell ∏_(j=0)^(ell−1)(n+2ell−2−2j)
       ·w^(n−2),

which is positive for every ell≥0 (empty product 1). All coefficients 2^ell a_(n−2ell)/ell! are positive; the leading coefficient of −4w(1−t²)^d is positive because d is odd. Thus deg P_n=5n+3 and, after removing the degree-3n+3 factors in (3), deg R_n=2n.

The factor degrees in (3) are 1+2(n+1)+2r=3n+3; the stated residual degree follows from 5n+3−(3n+3)=2n.

At either a or bar a, R_n is nonzero. Only ell=r contributes to P_n/V^r there. Its value is

    [P_n/V^r](a)=−2^r (n)_r/r! ·(−1/4)^r
          t(a)^r V′(a)^r (1−t(a)²)^d a^(−n−r−1),  (4)

and each displayed factor is nonzero: t(a)=1−i, V′(a)=i, 1−t(a)²=1+2i, a≠0. Since a(a²−1)^d≠0, (3) gives R_n(a)≠0; conjugation gives the other endpoint. This proves exact endpoint nonvanishing uniformly in n, not nonvanishing at a moving large-selector saddle.

## 3. Euler-factor form using actual U root geometry

Let θ=tD_t, and let μ_1,…,μ_r be the positive roots of the actual U(n,m). Transfer of the Euler operator by integration gives

    Σ_ell 2^ell a_(n−2ell)/ell! ·D_t^ell[t^ell h]
      =U(n,−(θ+1)/2)h
      = [2^r/r!]∏_(j=1)^r(θ+1+2μ_j)h.              (5)

The first identity follows either from θt^(2m)=2mt^(2m) and the formal adjoint θ*=−θ−1, or from the displayed falling-factorial expansion. Its factor form uses the proved U root theorem, including its exact leading coefficient (-1)^r4^r/r! for general even n. The factors commute and their shifts 1+2μ_j are all positive.

This is an explicit product of positive-shift Euler operators applied to the exact algebraic density h_n^full. It may permit a zero-localization or Casoratian argument. Such a root-preserving property for this branched rational density has not yet been proved.

There is also an exact coefficient form. For any locally analytic density h,

    Σ_(ell≥0) u^ell/ell! ·D_t^ell[t^ell h(t)]
       =(1−u)^(-1)h(t/(1−u)).                    (6)

It follows by applying (θ+1)_ell to Taylor monomials, or by the binomial series. Since only even coefficient indices up to n contribute, the transferred density in (1) is exactly

    [x^n] (1+2x+2x²)^n (1−2x²)^(-1)
                   h_n^full(t/(1−2x²)).         (7)

All coefficient operations in (7) are formal near x=0, with w≠0. Its square-root branch is the continuation of the one at x=0. This may allow an apolarity or two-variable saddle argument, but it does not yet provide a nonvanishing inequality.

## 4. Exact two-case identification evidence

`derive_fixed_weight_kernel.py` evaluates (1) symbolically, without sampled W values, at n=4,8. Full polynomials and factorizations are saved in `fixed_weight_kernel_n4.json` / `.log` and `fixed_weight_kernel_n8.json` / `.log`. In both cases the poles cancel exactly and the factors in (3) occur with their stated orders. The residual has degree 2n. These cases establish the saved exact expressions; the uniform identity and factor statement above are proved directly by operator algebra rather than extrapolated from them.

What remains: control R_n on the relevant moving saddle, or derive a positive / regular full quotient Casoratian from (1), (3), and (5). The full actual W can still have phase cancellation between its conjugate endpoint contributions. The positive complete-period coordinate proved separately excludes only annihilation of that one period solution.
