> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Root independent review of the complete signed saddle assembly

Date: 2026-09-13. Reviewer: root. FULL MATHEMATICAL PASS.
Reviewed raw_even_dual_saddle_assembly.md against its exact contour,
base differential equation, phase certificate, and actual multiplier
normalization. A separate end-to-end dependency audit is assigned to
audit_results to check the complete chain once more.

The leading coefficient u_n is exactly (2n)!Vlead_n and exactly
n!V_n(1)v0. The integral divided by this u_n has no remaining
factorial. Formal degree-n reversal produces z^n f_m(-1/z^2)Rtilde,
and the remaining rational factor is 1/[z(z-1)]. At z=-phi this
is rho^3>0. The original upward tangent and 1/(2i) contribute the
positive factor 1/2 to the Gaussian. The sole alternating sign
(-1)^m is the independently checked actual multiplier phase.

The varying-amplitude lemma is uniform. On a fixed neighborhood of
the saddle, Hardy bounds and Cauchy's formula control the multiplier
and its derivative independently of n. The base expansion has its
own uniform analytic O(1/n) relative error, without division by that
multiplier. Comparing the analytic phase to its quadratic term gives
n|y|^3 exp(-c n y^2); its integral is O(1/n). The amplitude's
Lipschitz error integrates to O(1/n) as well. Thus the remainder in
equation (3) does not require a convergence rate for A_n.

The certified middle-arc maximum supplies a compact gap outside a
fixed saddle neighborhood. Its retained middle covers a>=1/8; the
outward certificate actually extends slightly farther, so the
independently proved endpoint tail leaves no gap. The endpoint base
sqrt(5)/8 is strictly below tau. Both discarded contributions are
absorbed in O(tau^n/n).

I independently checked the transport identity by differentiating
the chi substitution and by its origin coefficient: H(w) begins
-3w^2/32, agreeing with the exact polynomial's logarithm. At the
saddle, exp H=sqrt(3/8)/rho. This gives exactly
C_s=(rho^2/4)sqrt(3pi/h_2), including every factor of two.

The full signed result therefore follows:

    Ra_n ~ (-1)^m A_s C_s (2n)!Vlead_n tau^n/sqrt(n).

The independently controlled Re is factorially smaller, so the same
integer linear form Lambda=Re+4Ra has the stated factor 4 and is
eventually nonzero. The primitive form divides by the actual positive
gcd g_n. Its shrinking is equivalent on any chosen even subsequence
to g_n/[(2n)!|Vlead_n|tau^n/sqrt(n)] tending to infinity. No such
arithmetic assertion is proved by the analytic theorem.

This is a rigorous intermediate asymptotic theorem. It does not prove
that e+pi is rational or irrational and is not a termination condition.
