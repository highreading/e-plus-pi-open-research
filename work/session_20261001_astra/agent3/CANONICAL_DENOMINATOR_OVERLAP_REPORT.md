> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Canonical denominator overlap report

Original author research, not independently reviewed. The preserved companion-transfer calculation was not repeated. All conclusions concern the actual factorial B-only Gram center c=alpha+gamma, gamma=kappa+beta.

The new exponential integer contraction Acal and the retained endpoint numerator Rcal=Delta x_0 give

    alpha=Acal/((n!)^2 dmax Dg),
    gamma=(L_N Rcal+(n!)^2 T_z)/((n!)^2 L_N Dg).

Using the common denominator Dcommon=(n!)^2 dmax L_N Dg, set

    U=L_N Acal,
    V=dmax(L_N Rcal+(n!)^2 T_z).

The note gives q,B,Q and C_overlap with every final gcd retained. In particular

    delta=gcd(Dcommon,|U+V|)/gcd(Dcommon,|U|,|V|),
    C_overlap=B/delta,
    q=lcm(Q,B)/delta,
    delta divides gcd(Q,B),
    lcm(q,B)=lcm(Q,B).

Hence B|q is exactly the condition delta=1. Loss can occur only at a prime with equal positive denominator depths v_p(Q)=v_p(B)=t. At such a prime its exact depth is

    v_p(delta)=min(t,v_p(Ared B0+Gred Q0)),

with Q=p^t Q0, B=p^t B0 and reduced companion numerators Ared,Gred. This isolates the required unit-numerator congruence.

A substantive new fixed-b result disproves eventual B|q for b=3,m=1. For every

    n=11^h+3, h>=6,

these even indices are in the retained slow-growth regime, and a determinant unit congruence proves their normality. The exact valuations are

    v_11(Q)=v_11(B)=(11^h-1)/5,
    v_11(q)=v_11(C_overlap)=(11^h-1)/5-1,
    v_11(delta)=1.

The proof uses one new exact seed at n=3, recorded in denominator_overlap_seed3.json, followed by a direct modulo-121 transfer for the actual Toeplitz matrix, positive forcing, exponential vector, reconstruction and metric. The key sum is

    S_n=Acal_n+dmax_n Delta_n x_(n,0).

Its seed is 44 modulo 121, and it transfers to 33 modulo 121 on the stated sequence. The logarithmic companion has denominator depth at most h, too small to alter the computed depths. The endpoint term is essential to this cancellation. The theorem is not finite-sample inference and uses no coordinate-center denominator theorem.

The result does not decide divisibility for growing b or for other subsequences. The one-power loss at 11 is negligible at the n log n scale, but losses at other primes remain uncontrolled.

Substituting C_overlap=B/delta into the supplied complete overlap inequality yields

    C_pi <= E B^mu
       + R C_epsilon^(-1/nu) E^(1/nu) B^mu delta,
    R=q|c-e-pi|.

With the retained factorial accuracy, a sufficient divergence condition is

    mu limsup(log B/(n log n))
       +limsup(log delta/(n log n))<1/2.

Thus the strict threshold 5/72 remains sufficient if log delta=o(n log n), using admissible pi exponents approaching the confirmed published bound 36/5. Exact B|q is sufficient but unnecessary. Neither that total-defect estimate nor a sufficient global B budget is established here.

The remaining arithmetic is the weighted sum over equal-depth primes of their normalized numerator-cancellation depths. The note specifies that sum exactly and explains the additional congruence information needed to bound it. No irrationality conclusion or global denominator exclusion is asserted.
