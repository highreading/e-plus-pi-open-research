> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Removing the positive slow mode from the actual half-step output

2026-10-02. Original structural continuation under parent steering. The goal is to express the remaining constant-shift determinant as a two-output Casoratian with a gauge that stays nonzero at every nonnegative index, including actual U zeros. This reduction is proved; positivity of that last Casoratian is still open.

## Search and overlap ledger

Before reading the newly supplied paper, archive search for `2604.09723`, `Shvets`, `Order.3 pi.formulas`, `Clausen functoriality`, `shifted.summation.lift`, and `Conservative Matrix Fields` over sources and the preceding session returned no hits. A follow-up search for summation lifts and right divisibility returned only unrelated coefficient sums and arithmetic lifts.

Online primary search: `Shvets 2604.09723 Order-3 pi-formulas Apery-like kernels Clausen functoriality shifted summation lift`. Opened the abstract and FULL HTML primary preprint at https://arxiv.org/abs/2604.09723 and https://arxiv.org/html/2604.09723v1. Read §3, especially Lemma 3.1 and Remark 3.2, and the surrounding operator conventions. The paper explains the standard right-factor criterion: a scalar recurrence with coefficient sum zero has a right factor S−1, and its solutions are summation lifts of lower-order kernels. It applies that criterion to three explicit printed recurrences of another family.

Overlap: the Ore-algebra summation-lift mechanism is classical and is credited here. New work below identifies a positive slow-mode gauge and the exact two-state kernel for the ACTUAL half-step W. None of that paper's printed cases or sequence scans is repeated. No claim that our kernel is a Gauss symmetric square or one of its Apéry-like sequences is made.

## 1. A uniformly positive gauge for the actual output

Write the actual output row in the rational state as

    R(h)=(F(h),G(h),H(h)),
    Y_h=R(h)X_h=W̆(n,h)/2^(n+1).

The exact fixed polynomial gives

    F(h)=∫_(-1/sqrt2)^(1/sqrt2)P_even(w)(1−2w²)^h dw / C_h,
    C_h=(1/sqrt2)B(1/2,h+1)>0.

In fact F(h)>0 for EVERY real h≥0. To identify the sign directly, put t=1−2w² and retain the positive density from `POSITIVE_COMPLETE_PERIOD_OUTPUT.md`:

    h_pos(t)=[V(−w)^n−V(w)^n]/(4w^(n+2)),
    κ_pos(t)=Σ_(ell=0)^r 2^ell a_(n−2ell)/ell!
                                      D_t^ell[t^ell h_pos(t)].

The completed density proof gives κ_pos(t)>0 for 0≤t<1 and the endpoint order which makes the following integral convergent. The full actual half-step kernel obeys

    P_even(w)=2w(1−t)^(n+1)κ_pos(t)>0,
                                         0<w<1/sqrt2.

Its even extension is positive on the corresponding negative interval as well. The numerator integral defining F is therefore strictly positive. This establishes the gauge without dividing by U_h, without presuming the ACTUAL W value positive, and without a determinant positivity assumption.

The slow homogeneous solution S_h=C_h F(h) is consequently nonzero on the whole nonnegative axis, and

    S_(h+1)/S_h=c(h)F(h+1)/F(h)>0,
    c(h)=(2h+2)/(2h+3).

The quotient F(h+1)/F(h) is rational; C carries the explicit positive hypergeometric scalar.

## 2. Exact two-state kernel and Casoratian reduction

Define an ACTUAL same-index combination

    K_h=Y_(h+1)/F(h+1)−c(h)Y_h/F(h).             (1)

This is rational at integer h. Its D-coordinate vanishes identically because the D-column of the transition is (c(h),0,0)^T. If E_h=(A_h,B_h)^T, then

    K_h=k(h)E_h,
    E_(h+1)=J E_h,
    J=[1 −1; 1 1], det J=2,

where k(h) is the last two coordinates of

    R(h+1)M(h)/F(h+1)−c(h)R(h)/F(h).             (2)

Every factor in (1),(2) is finite for h≥0. Unlike a gauge by u_n(h), this construction crosses all actual forcing zeros safely. It retains both endpoint modes explicitly.

Let

    Kmat(h)=[k(h); k(h+1)J].

Elementary lower-triangular output row operations give the exact determinant identity

    det O(h)=F(h)F(h+1)F(h+2) det Kmat(h).        (3)

Indeed divide each original row by its corresponding F, subtract c(h) times row zero from row one, and subtract c(h+1) times the original normalized row one from row two. The D-column becomes (1,0,0)^T; its endpoint minor is exactly Kmat. This also proves (3) without a scalar recurrence or an unspecified gauge choice.

Thus constant-shift ACTUAL W nonvanishing is reduced to a two-output Casoratian in the constant regular endpoint state. The prefactor in (3) is strictly positive on the entire axis. The n=4,8 exact determinant calculations transfer to this minor, but uniform minor positivity remains open.

At the sequence level, K_h=C_(h+1)Δ[Y_h/S_h]. This is the positive-gauge version of the summation-lift perspective: after normalizing by the exact slow solution S, one difference removes that mode. It does not assert that the unnormalized W has an S−1 factor. For example the newly derived order-four I recurrence has coefficient sum n(n−1), so an ungauged summation-lift conclusion would be false for n≥4.

## 3. Current implication and remaining target

The completed algebraic block theorem already proves a nonzero actual W among H,…,H+2n+4 for all n=4k and H≥0, with full errors and actual center denominators. Formula (3) improves structural understanding but has not yet shortened that theorem to a constant number of starts. A proof must control the actual rational endpoint row k and its Casoratian; positivity of F alone does not do so. No new arithmetic benefit from the rational gauge in (1) is claimed without tracking its own denominator if K is used as a separate lattice certificate.
