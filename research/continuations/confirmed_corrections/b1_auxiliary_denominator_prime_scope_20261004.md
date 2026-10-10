> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Local correction to the prime-support scope of auxiliary denominators at b=1

Reviewer: main Codex. Date: 2026-10-04. This page reuses an erratum already confirmed by the main agent, identifying the exact version and affected scope. Original manuscript bytes are preserved.

Source: [hp_b1_primitive_arithmetic_attempt.md](../../../work/session_20260913/hp_b1_primitive_arithmetic_attempt.md). The error is at lines 23–25 and 121–125: prime factors of the reduced denominators of the listed auxiliary projection polynomials and rational endpoint quantities were unconditionally described as “at most n.”

**Correction: the uniform support bound is max(n,2).** The original conclusion holds for n≥2; the prime 2 must be retained at n=1. This amendment concerns only the listed auxiliary quantities and makes no claim about prime support of the final reduced denominator q.

Under the source definitions, at n=1,



$$
K_1(t,s)=-1+3t+3s-6ts,
 \qquad\ell_0(s^j)=\frac1{(j+2)!},
 \quad\ell_1(s^j)=\frac1{(j+1)!}.
$$



Therefore,



$$
C_0^*(t)=-\ell_0^{(s)}K_1(t,s)=-t/2,
 \qquad C_1^*(t)=-\ell_1^{(s)}K_1(t,s)=-1/2.
$$



The original polynomials follow from C_j(z)=zC_j^*(1/z), giving C_0(z)=-1/2 and C_1(z)=-z/2. Their reduced denominators contain the prime 2, with 2>n=1. This is an exact counterexample to the original unconditional wording.

The original folding argument already eliminates every odd prime p>n, while the kernel coefficients also contain dyadic factors. Combining the fixed prime 2 with that folding result gives the support bound ≤max(n,2). The folding lemma, first-order lift formula at odd primes, and conclusions for n≥2 need no change.

Lines 127–128 of the source already explicitly state that this conclusion does not restrict the final q: division by the rational endpoint difference can introduce prime factors from its numerator. That observation remains valid. This wording error does not invalidate the analytic endpoint theorem, large-prime local-divisibility propositions, or subsequent exclusion of the coefficient-clearing objective as a whole.

This page does not reapprove other unreviewed parent inputs of the source. To use other propositions, consult their exact scopes in the main review register (historical reference; see the publication coverage notes). See the [formal errata register](../../../reviews/ERRATA_AND_SCOPE.md) for the source SHA and correction locations.
