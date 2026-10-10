> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Constant-shift recurrence target: incremental author notes

2026-10-02, root-requested continuation after the block theorem. The new target is to shrink the nonzero-certificate selection from O(n) starts to O(1) starts by deriving a constant-order recurrence for the actual moments and weighted difference. This is original research, not an audit, and no O(1)-shift theorem is claimed yet.

Archive search before this goal: `Prellberg`, `2609.06895`, `holonomic`, `creative telescop`, `four-term`, `recurrence.*W`, and `residual.*recurrence` over the prior session and sources. Relevant overlap: `agent1/LOGARITHMIC_RESIDUAL_RECURRENCE.md` proves a fourth-order modular recurrence for a different n-index auxiliary residual in a special prime strip; it does not provide m-contiguity for the present W. The archive also contains generic cautions that holonomicity alone does not control primitive arithmetic or selected contractions. The prior recurrence text was read through its derivation and division ledger.

Online primary-paper search/read: root supplied Thomas Prellberg, *Three Irrationality Results for the Dilogarithm: Rhin–Viola and Viola–Zudilin Constructions at −1/4, 1/5, and −1/3*, dated 7 September 2026, arXiv:2609.06895. Opened abstract, full HTML https://arxiv.org/html/2609.06895v1 and primary PDF https://arxiv.org/pdf/2609.06895. Full-text sections 2.5 and 3.4 are being read for the recurrence mechanism. Its bounded-shift strategy uses a recurrence with nonzero leading coefficient to propagate a zero block into an impossible fixed-n identically-zero tail. This is the mechanism to adapt, not a new generic method.

Concrete original setup: f(w)=V(w)^n/w^(n+1), A(w)=(2w²−1)², with the full contour moment I_m=∫_(bar a)^a f(w)A(w)^m dw. Its multiplier g(w)=w V(w)(2w²−1) cancels all rational logarithmic derivative denominators. For a polynomial h,

    D(g h f A^m)/(f A^m)
      =g h′+[g′+n g V′/V−(n+1)g/w+8m w g/(2w²−1)]h.

The bracket is a degree-at-most-four polynomial R_(n,m)(w). Searching a polynomial h of degree at most 4s−4 and coefficients c_0,…,c_s such that

    g h′+R_(n,m)h=Σ_(j=0)^s c_j A(w)^j

is a finite exact symbolic linear problem. At s=4 the unknown count exceeds the polynomial coefficient constraints by one; this supplies a telescoper of order at most four by dimension, subject to proving that its c-vector is nonzero and its leading coefficient is nonsingular in the m~ρnlogn domain. Boundary flux vanishes at both endpoints because V^(n+1) occurs in g f. This construction is specific to the actual integral; no recurrence fitting is proposed.

Outstanding: derive/factor the actual coefficient vector, assess singular m, transfer through polynomial weighting U and Δ^(n+1), and prove fixed-n W tail is nonzero with an appropriate exact or asymptotic argument. A generic recurrence-existence statement alone is insufficient for O(1)-shift nonvanishing.

Auxiliary structural progress: `ACTUAL_U_ROOT_GEOMETRY.md` gives a self-contained proof, for every positive even n=2r, that the exact U polynomial has r positive simple roots with successive m-gaps >1/2. The proof identifies U with the falling-factorial transform of a positive-root polynomial obtained from the negative-root even coefficient polynomial E_n. Its archive/literature ledger explicitly credits the classical transform mechanisms in the opened primary Fisk monograph. This controls the known selector solution but does not prove the three-output scalar τ nonzero, and it does not authorize division by every integer U value.

Current outcomes: the actual recurrence was derived and its leading/trailing factors proved nonzero for n≥1,m≥0; the precise coefficients and scripts are saved. The actual fixed-n W tail was proved nonzero in every residue class, using a Gaussian norm parity argument. The π mode U is annihilated by W, so the correct output quotient has dimension three. Two exact whole-axis transformed-minor tests, n=4,8, show no nonnegative zeros. A proposed proof by positive Newton coefficients fails at n=8. The general positive-domain quotient-output minor remains the O(1)-shift obligation; the proved O(n) block theorem is unaffected.
