> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Deferred refinement of the proportional intrinsic height

Agent 3, 2026-10-02. This branch was deferred at the root's instruction to prioritize an actual denominator mechanism. None of the candidate constants below is being used as a theorem about a reduced denominator.

The established intrinsic identity remains

    log A_B=2 log d_B+2(n+b)log n+O(n).

A possible sharper linear term requires the adjacent positive monic norm h_d=Z_(d+1)(0)/Z_d(0), not merely the n^2-scale partition limit. The candidate is

    log h_d/n -> ell(c),
    ell(c)=(2c+1)log M-2log 2-c log(M^2+1)
            -2(c+1)log(c+1)+c log c+(c+2)log(c+2).

This comes from the Euler constant of the explicit circular equilibrium. For m/n->alpha and j/n->theta, the elementary Stirling profile of omega_j B_j is

    f(c,alpha,theta)=c H(theta/c)
      +(1+alpha)log(1+alpha)
      -(1+alpha-theta)log(1+alpha-theta)
      +(1+c-theta)log(1+c-theta)-c-c log(sqrt2).

Its maximizing theta is the smaller root of

    2theta^2-(2+alpha+2c)theta+c(1+alpha)=0.

The resulting candidate correction is 2n[-1+max f+Phi_plus(r_plus)-ell(c)]. The weighted norm theorem needed to justify the adjacent-norm limit was not completed in this branch. In particular, an n^2-scale free energy by itself does not justify differencing adjacent partition functions.

Archive queries covered chemical potential, monic norms, weighted Chebyshev, partition derivatives, linear height and the displayed formulas. Closest matches were the established adjacent-norm bounds and older fixed/growing selector heights. Primary queries were `site:arxiv.org varying weights monic orthogonal polynomial norms equilibrium measure one cut asymptotic` and `site:arxiv.org Borot Guionnet one cut partition function potential analytic parameter uniform`. Opened https://arxiv.org/pdf/1107.1167 and https://arxiv.org/pdf/0910.4223, especially Balogh--Bertola Corollary 3.1 and its smooth-potential norm hypotheses, and the Hermite--Pade record https://arxiv.org/abs/math/0302357. The divergent principal-arc boundary field still needs either a restriction argument or a directly applicable weighted Bernstein--Markov statement. These are source leads, not a claimed theorem import.
