> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Actual selector polynomial: positive simple roots and a strict mesh bound

2026-10-02. Incremental author theorem within the constant-shift recurrence target. This note proves a uniform structural property of the actual U polynomial. It does not prove the quotient-output minor nonzero, and it does not establish three-shift nonvanishing of W.

## Search and overlap ledger

Before pursuing this subtarget, the prior session and sources were searched for `U.*real.root`, `real.root.*U`, `falling.factorial`, `Jensen.*polynomial`, and `Hermite.Biehler`. Relevant archive overlap consists of the exact coefficient formula and degree of U in `LARGE_SELECTOR_SELECTION_DRAFT.md`, and many unrelated uses of falling factorials in arithmetic contractions. No actual-U real-root or mesh theorem was located by that search. This is a bounded search statement, not a claim that no such theorem exists elsewhere.

Online paper searches used "falling factorial transform polynomial positive roots mesh real roots theorem", "Steve Fisk Polynomials roots interlacing arxiv 0612833 falling factorial", and "Jensen polynomials Polya Schur multiplier falling factorial real roots". The primary full text opened was Steve Fisk, *Polynomials, roots, and interlacing*, arXiv:math/0612833, https://arxiv.org/abs/math/0612833 and https://arxiv.org/pdf/math/0612833. Its Section 7.6, Proposition 7.31, printed page 182 / PDF page 194, treats the classical falling-factorial transform preserving positive real roots. The monograph also treats differential root preservers and even/odd parts. The generic root-preservation mechanisms are classical. What is supplied here is their explicit application and strict mesh proof for the exact U of this project. No novelty for the generic methods is asserted.

The proof below is self-contained and uses no numerical root experiments.

## Theorem

Let n=2r be a positive even integer, and define the actual polynomial extension in real m by

    a_j=[x^j](1+2x+2x²)^n,
    U(n,m)=Σ_(ell=0)^r (-2)^ell binom(2m,ell) a_(2r−2ell).

Then U(n,m) has exactly r distinct roots on (0,∞). If they are

    0<μ_1<⋯<μ_r,

then

    μ_(j+1)−μ_j>1/2,  1≤j<r.

For n=4k, its leading coefficient is the positive value 4^r/r!. This is the exact U from the archived large-selector construction, with no redefinition of its normalization.

## 1. The full even coefficient polynomial has negative simple roots

Put

    E_n(y)=Σ_(j=0)^n a_(2j)y^j.

For t>0,

    E_n(−t²)=Re(1+2it−2t²)^n.

Write the continuous argument of 1−2t²+2it as θ(t). It lies in (0,π), tends to 0 as t↓0 and to π as t→∞, and

    θ′(t)=(2+4t²)/[(1−2t²)²+4t²]>0.

The n values θ=(j+1/2)π/n, j=0,…,n−1, therefore give exactly n distinct t>0 for which E_n(−t²)=0. Each zero is simple because θ′ is strictly positive and the derivative of cos(nθ) there is nonzero. Since E_n has degree n, these are all its roots. Its constant term is 1, so

    E_n(y)=∏_(j=1)^n (1+c_j y),  c_j>0.

## 2. A differential transform produces a positive-root input

Define

    H_r(x)=E_n(D)x^r
          =Σ_(j=0)^r a_(2j)(r)_j x^(r−j),
    G_r(t)=(-1/2)^r H_r(−2t)
          =Σ_(j=0)^r a_(2j)(r)_j(-1/2)^j t^(r−j),

where (r)_j is the falling factorial and (r)_0=1. Both are monic of degree r.

Every factor 1+c_jD preserves the property "all roots are real and nonpositive". For completeness, if f has simple real roots β_1<⋯<β_s≤0, then

    (f+c f′)/f=1+cΣ_j 1/(x−β_j),  c>0.

On (−∞,β_1) this decreases from 1 to −∞ and has one zero. On every (β_j,β_(j+1)) it decreases from +∞ to −∞ and has one zero. These s intervals provide all roots, all nonpositive. Repeated roots follow by approximating the root multiset by distinct nonpositive roots and taking a coefficient limit; a repeated root can also be retained directly by factoring its multiplicity. The degree and leading coefficient do not change in that limit.

Starting from x^r and applying E_n(D)=∏(1+c_jD) consequently proves that all roots of H_r are real and nonpositive. Its constant term is a_(2r)r!>0, so zero is not a root. Thus all its roots are strictly negative, and all roots of G_r are strictly positive. Simplicity of these intermediate roots is unnecessary.

## 3. A strict mesh statement for the falling-factorial transform

Let T be the linear map T(t^s)=(x)_s. The elementary identity

    T(tp)(x)=x(Tp)(x−1)

shows that

    T((t−λ)p)(x)=x f(x−1)−λ f(x),  f=Tp.

Claim: if p has all positive real roots, counted with multiplicity, then Tp has positive simple roots with successive gaps strictly greater than 1.

Factor p(t)=∏_(j=1)^s(t−λ_j), λ_j>0, and argue one factor at a time. The degree-one case is x−λ_1. Suppose f is monic, has simple positive roots α_1<⋯<α_s, and α_(j+1)−α_j>1. Let

    g(x)=x f(x−1)−λ f(x),  λ>0.

There is a sign change between 0 and α_1: g(0)=−λf(0) has sign (−1)^(s+1), while g(α_1)=α_1f(α_1−1) has sign (−1)^s. For each j<s there is a sign change on (α_j+1,α_(j+1)): at its left endpoint g=−λf(α_j+1), of sign (−1)^(s−j+1), while at its right endpoint g=α_(j+1)f(α_(j+1)−1), of sign (−1)^(s−j). Finally g(α_s+1)<0 and g(x)>0 for large positive x. Hence g has a root in each of the s+1 disjoint intervals

    (0,α_1),
    (α_j+1,α_(j+1))  (1≤j<s),
    (α_s+1,∞).

Since its degree is s+1, these are all its roots and every one is simple. If ordered as γ_1<⋯<γ_(s+1), the intervals show γ_j<α_j and γ_(j+1)>α_j+1, so γ_(j+1)−γ_j>1. This proves the induction even when some original λ_j coincide.

## 4. Exact identification with U

Reindexing the archived coefficient formula by j=r−ell gives the polynomial identity

    U(n,m)=(-2)^r/r! · [T G_r](2m).

Indeed its j-th term is

    (-2)^r/r! · a_(2j)(r)_j(-1/2)^j (2m)_(r−j)
      =(-2)^(r−j) a_(2j) binom(2m,r−j).

Section 2 gives all-positive roots of G_r; Section 3 gives positive simple roots of TG_r with gaps >1. Evaluating at 2m divides those root locations and gaps by 2, proving the theorem.

## Consequences and limits for the recurrence problem

The signed selector mode in the four-state moment recurrence is now controlled by an explicit simple real-root geometry. In particular an interval in m of length at most 1/2 contains at most one U root. For n=4k, U is positive above its largest root and below its smallest root, with alternating sign between successive roots.

The three-output cofactor vector remains τ_n(m)(U_m,…,U_(m+3)). The theorem does not show τ_n(m)≠0: it controls the known kernel vector, not the rank of the three actual output rows. It also does not assert U(n,m)≠0 for every nonnegative integer m, and the step-one support can cross multiple roots. No division by a possibly zero individual U value is justified by this theorem.
