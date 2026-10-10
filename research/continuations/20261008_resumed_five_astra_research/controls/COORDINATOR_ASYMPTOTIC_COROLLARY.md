> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A sharper corollary of the proposed correlated Gamma comparison

Coordinator derivation, 8 October 2026. Conditional on independent acceptance
of Sections 2–4 and 8 of COORDINATOR_UNIFORM_GAMMA_COMPARISON.md. This is an
analytic consequence for the SAME compact pencil, not a rationality proof.

Put A=17+12 sqrt(2), R_k=1/K_(k-1)^nu(-1,-1), and eps_k=e+pi-p_k/q_k.
For k>=64 define the explicit quantities

    delta_k=18/(k^2-11k+1),
    tau_k=2 e^11 4^(-k).

The existing correlated proof actually retains the sharper bounds

    ((1-delta_k)^k-tau_k)/(1+tau_k)
       <= eps_k/R_k <= (1+tau_k)/(1-tau_k).             (1)

Indeed, the exterior comparison retains (1-delta_k)^k rather than replacing
it by3/5; the full signed overlap and atom payments are tau_k times the same
positive exterior slope. Neither determinant, scalar normalization nor final
gcd has been altered.

Bernoulli and (1) imply the entirely explicit relative bounds

    1-(k delta_k+2 tau_k)/(1+tau_k)
       <= eps_k/R_k <= 1+2 tau_k/(1-tau_k).            (2)

Consequently eps_k/R_k tends to1, with a lower loss O(1/k) and an upper loss
O(4^(-k)). This refines the fixed-constant rate comparison. It does not assume
strong orthogonal-polynomial asymptotics, a determinantal-process coupling,
an adjacent-gcd recurrence, or an extra original moment. The only asymptotic
operation is on the explicit rational delta_k and exponential tau_k.

The same proof gives at each k>=64

    eps_(k+1)/eps_k
      <= (1/9) * (1+tau_(k+1))/(1-tau_(k+1))
         * (1+tau_k)/((1-delta_k)^k-tau_k).             (3)

In particular limsup eps_(k+1)/eps_k<=1/9. Equation (3) is a computable
upper bound on the actual ordinary-error ratio, not an evaluated neighboring
denominator ratio. It neither proves that this limsup is1/9 nor identifies the
more precise Christoffel ratio.

No new arithmetic claim is made: q_k eps_k is the nonzero whole error, and a
bound on the ACTUAL q_k or the ACTUAL primitive adjacent cross difference is
still required on an explicit infinite domain. The finite k32/k33 certificates
do not fall inside this k>=64 theorem and are not used in its proof.

Overlap gate: the present corollary is elementary algebra applied to the new
proposed same-pencil comparison. Classical variational and Gaussian arguments
are explicitly reused in that source. No global novelty is asserted, and no
new computation or external theorem is imported here.
