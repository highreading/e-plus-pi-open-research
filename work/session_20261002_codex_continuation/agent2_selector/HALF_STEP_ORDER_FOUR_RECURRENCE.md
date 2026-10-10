> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A quadratic-coefficient order-four recurrence for all integer selectors

2026-10-02. Original exact derivation in the half-step target. The archive/literature search preceding the recurrence structural target is recorded in `HALF_STEP_CHRISTOFFEL_TARGET.md`. The simpler recurrence is not inferred from generic holonomic closure.

Let n≥1 and h≥0 be integers, and set

    I_h=∫_(bar a)^a f_n(w)z(w)^h dw,
    f_n=V(w)^n/w^(n+1), V=w²−w+1/2, z=1−2w².

Then the exact full-contour moments satisfy

    8(h+1)(h+3) I_h
    −4(6h²+29h+32) I_(h+1)
    +4(7h²+2hn+40h+6n+56) I_(h+2)
    −2(8h²+6hn+53h+20n+88) I_(h+3)
    +(2h+n+7)(2h+n+8) I_(h+4)=0.                (1)

The leading and trailing coefficients are strictly positive throughout n≥1,h≥0, so (1) is forward and backward regular there.

For the derivation put g(w)=w V(w)(2w²−1). The polynomial total derivative is

    D_w[g(w)H(w)f_n(w)z(w)^h]
       =f_n(w)z(w)^h T_(n,h)H(w),

with its action on monomials

    T(w^k)=(2k+4h+2n+8)w^(k+4)
       +(−2k−4h−6)w^(k+3)+(2h−2n)w^(k+2)
       +(k+1)w^(k+1)+(n−k)w^k/2.                (2)

Its leading coefficient is positive. Reducing z^j, j=0,…,4, by (2) to the quotient basis 1,w,w²,w³ and taking signed 4×4 cofactors gives their exact dependence. The resulting coefficients share the nonzero factor

    −64n(h+1)(h+2)/∏_(j=4)^8(2h+n+j).

After cancelling it, the five coefficients are precisely those in (1). The full symbolic reduction and its signed cofactors are saved in `derive_half_step_moment_recurrence.py`, `half_step_moment_recurrence.json` and the log. No sampled numerical recurrence fit is used.

The cofactor dependence says that the recurrence polynomial Σ C_j z^j belongs to the image of T, so its full-contour integral is a boundary flux. That flux vanishes at both endpoints because it contains V^(n+1); w,z are nonzero there. The integration path avoids w=0. This proves the recurrence for the ACTUAL full moment, without an omitted inhomogeneous endpoint term.

For n=4k, the actual identity

    i2^(n+1)I_h=(−1)^h T_h−πu_n(h)

and irrationality of π show separately that u_n(h) and (−1)^hT_h solve (1) at all nonnegative integer starts. Their rationality suffices, so no forcing nonzero assumption is required. The old even-step π mode was U(n,m); its half-step counterpart is the polynomial u_n(h), not the alternating actual endpoint forcing U_h.

At large h, the leading quadratic recurrence symbol factors as

    4(E−1)²(E²−2E+2).

This identifies the slow double mode and the two conjugate endpoint modes at the leading level only. It is not an exact factorization of the variable-coefficient recurrence. The proved all-start actual-W block theorem is instead in `HALF_STEP_ALGEBRAIC_BLOCK_THEOREM.md`; constant-order recurrence regularity by itself is not promoted to constant-shift weighted-output nonvanishing.
