> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Agent 1: growing-degree arithmetic normalization

Status: paper derivation completed; 18 formal symbolic checks passed. Independent review pending. Scope: 1<=b<=n, including b=floor(n/2). No new degree or prime scan.

The candidate Rodrigues identity is verified. In Agent 2's monic system the exact high-row factor is 1/(2n+2l)!, leaving the integer derivative row E_(n+l,l+j-1). These factors cancel from every endpoint quotient.

Additional proved cancellations are: individual integer row contents; maximal-minor content of the high block; divisibility k|E_(k,r) for r>=1 (in particular a forced n+l row divisor for l>=2); the resulting adjacent derivative normalization by n+1; and the gcd of the three integer endpoint contractions.

After these cancellations, let sigma*,c*,kappa* be the primitive three contractions specified in GROWING_DEGREE_ARITHMETIC.md. The actual quotient is

    X/Y=(Q*+2^(n+1)V*/(n!)^2)/D*,
    D*=(n+1)P_(n+1)c*-2P_n sigma*,
    Q*=2w_P sigma*-(n+1)w_U c*,
    V*=sigma* Acal_n-c* Bcal_n-kappa*.

Both partial-exponential contractions and the complete second-kind terms remain present. The elementary endpoint identities are justified for every column j<=b<=n by their factorial-tail identity and the unchanged projection kernel; they are not assumed from a b=2-only calculation.

For the explicit integer Lambda in the proof, set N=Lambda(Q*+2^(n+1)V*/(n!)^2), Z=Lambda D*. On D*!=0 the actual reduced denominator is

    q=|Z|/gcd(|Z|,|N|).

This final gcd is the precisely specified unresolved arithmetic content. The clearer Lambda is not substituted for q. Growing-degree endpoint nonvanishing also remains open; no fixed-b theorem is imported to establish it.

The b=2 specialization gives exactly the completed Vtilde expression, with kappa=a omega, and recovers V_original=(n+1)Vtilde and both original endpoint factors. Completed scans were not repeated.

Files:

- GROWING_DEGREE_ARITHMETIC.md: full proof, cancellations, quotient, and final gcd gate.
- check_growing_degree_arithmetic.py: reproducible symbolic evidence.
- growing_degree_arithmetic_certificate.json: successful 18-check certificate.
- GROWING_DEGREE_REPORT.md: this concise report.

The next arithmetic problem is to bound the final gcd or the depth of V*+(n!)^2 Q*/2^(n+1) for growing-size integer minors, together with proving D*!=0 on the intended indices. No global growth estimate, shrinking conclusion, or irrationality assertion is claimed.
