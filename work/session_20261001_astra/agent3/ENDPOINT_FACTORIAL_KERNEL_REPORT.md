> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Agent 3: factorial-kernel report

The pending Bernstein verifier executed unchanged and passed: 126 signed differences, 95 shift identities, two endpoint sums, and the original endpoint. Its JSON output and actual stdout were read back; stderr is empty and all input certificates were preserved.

The new exact kernel theorem is

    det[1/(a_i+c_j)!]
      =(-1)^(d(d-1)/2) (product e_i!)/(product X_j!)
                         det[binom(X_j,e_i)],

for strictly increasing nonnegative integer offsets, with A=max a_i, e_i=A-a_(d+1-i), and X_j=A+c_j. The last determinant counts nonintersecting lattice-path families and is strictly positive. Every factorial domain is explicit. Repeated offsets give zero.

For the actual consecutive reversed columns this becomes

    det[1/(n+m_i-j)!]=Delta(m)/product_i(n+m_i)!.

The actual endpoint E_k is a signed Cauchy–Binet sum with these positive kernel weights and all ordered Legendre coefficient minors retained. Those minors do not have a common sign: at the saved n=6 control, the two sums contain respectively 60 positive/59 negative/1 zero and 60 positive/60 negative terms.

A new exact integral representation expresses E_k as eta_k times a positive normalizer times

    integral_(0<t_1<...<t_b<1)
      det[Borel(q_i)(t_l)] Delta(t)
      product_l(1-t_l)^(n-b) dt,

where q_i are the actual rows (1-t)p_(n+1),...,(1-t)p_(n+b-1),p_k. Its normalizer is (n!)^b/product_(j=0)^(b-1)(n-j-1)!.

The integral is not pointwise positive. At the frozen nodes (1/4,1/2,3/4), both actual signed Borel determinants are strictly negative; at (1/8,1/4,3/8), both are positive. These exact counterexamples stop the pointwise-sign route. They do not contradict the positive endpoint integrals.

The new checker passed 120 relevant kernel-minor factorizations and both complete signed endpoint and beta-integral identities using only saved n=6 data. No original control was rebuilt, and no degree list was extended. The exact endpoint sums remain

    E_6=1355870278086451/73150524144312975360000,
    E_7=181648924564193/70441245472301383680000.

The remaining substantive target is a cancellation-aware inequality comparing positive and negative weighted contributions, for example a rigorously bounded simplex decomposition. Uniform dominance has not been proved. A positive-measure Hankel obstruction does not invalidate the oriented bare-kernel theorem, and that theorem does not remove the signed Legendre weights.

Saved under work/session_20261001_astra/agent3/:

- ENDPOINT_FACTORIAL_KERNEL.md — proofs, actual integral, counterexamples, residual inequality.
- ENDPOINT_FACTORIAL_KERNEL_REPORT.md — this report.
- check_endpoint_factorial_kernel.py and endpoint_factorial_kernel_checks.json — exact frozen-data checks.
- Actual stdout/stderr logs for both executed verifiers.

No unbounded endpoint or full-remainder nonvanishing theorem is claimed. Companion conditioning and the quotient audit remain with their assigned agents. No networking, installations, new HP indices, prime scans, or edits outside this directory were performed.
