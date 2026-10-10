> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Preconditioned reconstruction report

New author paper result, conditional on the main positive-forcing/even-normality and adaptive-arc inverse drafts. Existing logarithmic forcing and directional files are preserved. No computations or audits were repeated.

The same factorially weighted rational B-only center is retained. Put N=n+m+1, r=N-b, d=b-1, m=floor((b-1)/2), and w_j=r!/(N-j)!.

In compatible weighted coordinates, both H=(I+D)^(-n) and H^(-1) have norm at most

    C_H=b[1+(n+d)/(r+1)]^d.

The proof cancels their exact derivative factorials against w_i/w_j before absolute values. For b=o(n), log C_H=O(b+log b). Multiplication by z-1 has weighted norm at most N+1, and its inverse on its image has weighted norm at most 1/r, using reverse cumulative sums.

The two actual reconstructed columns satisfy

    u=K T^(-1)f_P,
    v-Su=e_0+K T^(-1)(e_F+e_E).

A forward estimate supplies a genuine lower bound for ||S_B u||. Together with the residual-column estimate this yields the complete explicit envelope in equation (9) of the research note. It retains the endpoint constant and both complete residuals.

The remaining coordinate-conversion cost is exactly

    C_w=N!/[(N-d)! (sqrt(2))^d].

Diagonal conjugation of the available Toeplitz inverse estimate reproduces this factor rather than eliminating it. No claim is made that the actual inverse necessarily attains that loss.

For even n and b=floor(beta n/log n), all factors included, the new envelope is

    |t-(e+pi)|<=exp(-[2log(1+sqrt(2))-beta]n+o(n)).

Thus every fixed 0<beta<2log(1+sqrt(2)) gives decay within the named author dependencies. This reduces the previous conservative loss from 3 beta n to beta n without changing the center or its denominator. Endpoint and exponential terms are factorially smaller; the research note displays them explicitly.

For the actual reduced center t=p/q, the primitive pair still has bounds q B_rec and 1/q+q B_rec/2. Each radial lift factor cancels against its own endpoint gcd. No useful bound on q, sign of the full error, or shrinking-pair theorem is established.

The remaining analytic target is a direction-sensitive estimate across the Toeplitz coordinate conversion that improves C_w. A further rescaling alone does not do so. The full propagation cost exp(O(b log(n/b))) remains unproved even though the compatible finite reconstruction itself has cost exp(O(b)).

Full constants and proofs: PRECONDITIONED_RECONSTRUCTION.md. Both files require read-back before completion is reported.
