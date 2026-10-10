> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Coordinate logarithmic depth report

New result: for b=3, weight parameter m=1, n=13^(s+1)+3 with s>=5, every rationally eligible positive coordinate satisfies

v_13(L_j)=2v_13(n!)-(s+1),
v_13(B_j)=s+1,
v_13(gcd(q_j,B_j))=s+1.

Here alpha_j=E_j/((n!)^2 X_j), gamma_j=L_j/((n!)^2 X_j), t_j=alpha_j+gamma_j, B_j=den(gamma_j), and q_j=den(t_j). The correction is zero because j>=1. The actual denominators are reduced after addition or division as appropriate.

The deciding new lift is stronger than a valuation statement. With P=13^(s+1),

P L_j/(n!)^2 = 4X_j mod 13,
P gamma_j = 4 mod 13.

To prove it, use the integral adjugate selector C_j and its polynomial K_j with K_j(1)=X_j. Scaling the complete logarithmic moment by P leaves only indices k=P and 2P; their moment residues are respectively 2 and 1. Frobenius and Lucas give

K_j(t)=(-2t^P+4t^(2P))H_j(t) mod 13.

The two relevant tail sums are 2H_j(1) and 4H_j(1), while X_j=2H_j(1). Their weighted sum is therefore 4X_j. The previously accepted unit property of X_j makes this residue nonzero and proves the exact logarithmic depth.

The full overlap can be written gcd(q_j,B_j)=13^(s+1)gcd(q_j^*,B_j^*), where the starred factors are prime to 13. Its non-13 part remains unresolved. No assertion about other primes, Gram centers, or global denominator growth is made.

The companion analytic review is LARGE_SELECTOR_RELATIVE_SADDLE_REVIEW.md. Its scoped PASS covers the new relative saddle formula, adjacent signed phase drift, and phase sparsity. Complete-error deductions retain their separately stated forcing and exponential estimates as dependencies.

Evidence: these are paper proofs, with no repeated old computation or new numerical experiment. The accepted residue gate is used only as a retained theorem dependency. New deliverables require controller readback before delivery is reported complete.
