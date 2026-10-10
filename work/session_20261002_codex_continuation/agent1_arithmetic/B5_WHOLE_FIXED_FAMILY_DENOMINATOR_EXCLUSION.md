> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The complete fixed b5,m1 B-only Gram family has growing primitive error

Author result, target L12, 2026-10-02. This combines new exact finite inputs with the all-depth local arithmetic already derived in this directory and the separately authored fixed-b signed-error theorem of the designated analysis agent. No independent review is asserted. The conclusion concerns this specified rational-center family; no unconditional conclusion about e+pi follows.

Let c_n=p_n/q_n in lowest terms, q_n>0, be the canonical factorial B-only Gram center with b=5 and m_w=1. The definition includes the full endpoint correction kappa and the complete rational logarithmic companion beta. At normal indices its normalized representation is

    c_n = 2^n V_n / ((n!)² D_n) + beta_n,
    Y_n = adj(N_n) D0_n J_n,
    D_n = Y_n^T H_n Y_n,
    V_n = Y_n^T H_n adj(N_n) A_n + det(N_n)(K_n Y_n)_0.

The last summand is the full correction. These are the exact canonical identification and definitions of GENERAL_FIXED_B_ODD_ORIGIN.md; scaling the original diagonal metric by its common scalar gives Omega_j=(n+2)_j², 0<=j<=5, and H=K^T Omega K. This positive common scaling cancels in the center.

Set S={11,13,29,53,59,89,101,173,193,199} and

    rho_5 = sum_(p in S) 2 log(p)/(p-1).

Then every normal n>=398 satisfies the actual denominator inequality

    log q_n >= rho_5 n - 21 log n - 2 sum_(p in S) log p.       (1)

The exact rational certificate proves

    rho_5 - 2 log(1+sqrt(2)) > 1/25.                           (2)

The signed-error author theorem in ../agent3_analysis/FIXED_B_UNIVERSAL_FIRST_CORRECTION.md gives, on both parities and for all sufficiently large n,

    c_n-(e+pi) = (-1)^(n+1) 4pi (1+sqrt(2))^(-2n-5)
                   [1-(4+sqrt(2)/8)/n+O(n^-2)].              (3)

Its exact canonical cofactor/metric setup is also recorded in that agent's ALL_PARITY_B3_SIGNED_ASYMPTOTIC.md, with the general fixed-b proof in the first file. This note uses (3) as an attributed author input, and does not independently review that proof. In particular, it supplies eventual normality and a nonzero error on both parities.

Combining (1)–(3), the complete primitive linear form

    R_n = |q_n(e+pi)-p_n|

obeys

    liminf_(n to infinity) (log R_n)/n
         >= rho_5 - 2 log(1+sqrt(2)) > 1/25.                  (4)

Thus R_n tends to infinity for the entire eventual fixed b5,m1 sequence, including every subsequence. This family cannot produce shrinking primitive forms. Only the local proof inputs and the attributed signed-error theorem are used; the finite atlas is not extrapolated as a valuation experiment.

## Exact finite inputs

For each p in S, direct finite definitions modulo p evaluate all r=0,...,p-1. All P_r=J_0(r) are units, and the only V_r zeros are r=0,p-2,p-1. The origin constants are

    D_origin=497664,
    V_n/n = P_n · 331776(3C_p+32) mod p,
    C_p=sum_(j=0)^(p-1) (-1)^j j! mod p.

The two structurally null boundary disks are h=1 and h=2. The complete normalized constants of FINITE_BOUNDARY_QUOTIENT_FORMULA.md are listed below; nu includes kappa.

|p|C_p|331776(3C_p+32) mod p|delta(h1)|nu(h1)|delta(h2)|nu(h2)|
|---:|---:|---:|---:|---:|---:|---:|
|11|5|4|6|8|5|10|
|13|0|5|1|1|12|6|
|29|20|22|13|25|11|5|
|53|21|44|43|24|5|8|
|59|33|11|17|52|38|11|
|89|48|32|23|53|3|42|
|101|41|19|59|13|67|43|
|173|89|56|74|96|11|6|
|193|121|81|7|154|50|146|
|199|65|10|91|19|187|163|

Every displayed nu and origin coefficient is a unit. There are exactly920 seed evaluations and20 normalized charts. B5_NORMALIZED_PRIME_ATLAS_199.json retains all bounded atlas results, including unsuccessful primes; B5_NORMALIZED_PRIME_CERTIFICATE.json retains the selected complete seed vectors and the finite quotient matrices/solves, their defining script hashes, primality checks, and exact rational logarithm intervals. b5_compact_certificate.py recomputes the twenty finite charts used by this theorem and checks the exact rate comparison. No n=p²-h reference or finite-depth extrapolation is needed.

For the logarithm comparison,24 rational atanh terms are used after writing each argument as2^k times a rational in[1,2). For z=(x-1)/(x+1), the positive omitted series is bounded above by

    2 z^49 / (49(1-z²)).

The rational bounds1414213562373095/10^15<sqrt(2)<1414213562373096/10^15 have their squared inequalities checked exactly. The displayed values rho_5≈1.803426302971729 and tau≈1.762747174039086 are explanatory decimal displays; (2) uses only rational inequalities.

## Why these finite inputs imply the all-depth actual-q bound

All endpoint digits being units makes P_n a p-unit for every n by the exact all-residue Lucas transfer. GENERAL_FIXED_B_ODD_ORIGIN.md proves the origin expansion at every k=v_p(n)>=1, including the extra depth-one Frobenius term and its cancellation. The two origin units give

    v_p(D_n)=0, v_p(V_n)=v_p(n) when p|n.

At nonzero seed residues outside p-1,p-2, the exact seed transfer gives v_p(V_n)=0. Even if D_n has positive valuation, the factorial summand has valuation -2v_p(n!)-v_p(D_n).

For either boundary h=1,2, ALL_STRUCTURAL_BOUNDARY_CHARTS.md proves, for every k=v_p(n+h)>=1,

    D_n/((n+h)² P_n²)=delta_h mod p,
    V_n/((n+h)² P_n)=nu_h mod p.

Only a unit triangular lower block is inverted. The backward Dcal ambiguity and the carried endpoint source both lie in e^(-z)Pol_(h-1); the reconstruction (I+partial_z)^h annihilates them. This resolves all depths and the actual carry, including depth one. Since nu_h is a unit, v_p(V_n)=2k and v_p(D_n)>=2k. The derivation permits deeper raw Gram content; it never identifies that content with q_n.

The complete beta bound is

    v_p(beta_n)>=-v_p(D_n)-floor(log_p(2n+4))

outside the structural disks, and the stronger

    v_p(beta_n)>=k-v_p(D_n)-floor(log_p(2n+4))

inside either boundary disk. For n>=2p the factorial summand is strictly deeper than beta in each case, by the explicit factorial/log inequalities of the cited origin and structural chart proofs. Its valuation therefore survives the full rational sum and its evaluated gcd. In particular,

    v_p(q_n)=2v_p(n!)-v_p(n)                       if p|n,
    v_p(q_n)=2v_p(n!)+v_p(D_n)                    at ordinary unit residues,
    v_p(q_n)=2v_p(n!)+v_p(D_n)-2v_p(n+h)          at a boundary h.

The latter two are at least2v_p(n!). Hence every selected prime gives v_p(q_n)>=2v_p(n!)-v_p(n) for every normal n>=2p, with full beta and kappa retained.

Finally, Legendre's formula and the digit bound give v_p(n!)>=n/(p-1)-log_p(n)-1. Summing these ten bounds and using sum_(p in S)v_p(n)log p<=log n proves (1). This is a same-index full-sequence estimate; no limsup analytic radius or finite numerator content is substituted for it.

## Scope

This is a distinct fixed b5,m1 family exclusion. It does not assert a criterion for all primes, other metric choices, growing b, or arbitrary Hermite–Padé constructions. The finite certificate, local all-depth proof and signed-error theorem currently have author status; independent review belongs to the designated analysis agent if root requests it. The all-depth mathematics is a separate proof dependency, clearly exposed above, and is not replaced by the920 finite rows.
