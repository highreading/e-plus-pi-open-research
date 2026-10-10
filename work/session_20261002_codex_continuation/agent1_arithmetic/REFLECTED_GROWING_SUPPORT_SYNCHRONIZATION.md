> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Constructive growing prime support on a convergent reflected sequence

Original author arithmetic L21, 2026-10-02, at root's steering. The fresh archive/primary gate is in TARGET_LEDGER.md, L21. This note uses the exact all-prime theorem from REFLECTED_UNIVERSAL_PRIME_RESIDUE.md and the analysis agent's FIXED_CONGRUENCE_INVERSE_CRITICAL_COROLLARY.md §3. It gives an explicit index construction, not a prime atlas, prime-distribution assumption, or numerical experiment.

There is ONE sequence of actual reflected centers converging to e+pi for which log(q)/N→infinity. Every fixed finite odd support of evaluated rational correction shifts leaves this growth intact. The modulus and exponent are allowed to grow, and their cost is paid explicitly. A response-changing correction with denominator support inherited from the old q is outside the statement.

## 1. Explicit indices and the modulus cost

Let p_1,p_2,… be the odd primes in increasing order. For each j≥1 put

    S_j={p_1,…,p_j},
    A_j=lcm(4,{p(p−1):p∈S_j}),
    J_j=lcm({ord_p(2):p∈S_j}),
    b_j=bit_length(A_j+1).

Define recursively s_0=0 and

    s_j=J_j ceil(max(8(j+b_j),s_(j−1)+1)/J_j),
    N_j=2^s_j.

These definitions involve only finite integer arithmetic. In particular s_j is a multiple of every chosen 2-order, so N_j≡1 modp for every p∈S_j. The powers N_j strictly increase. Let t_j be the large positive exact root of

    Psi(t,N_j)=t^(3/2)/sqrt(N_j)−2sqrt(N_j)/sqrt(t)
               +log(sqrt(N_j)/(4t^(3/2)))=0,

and set

    n_j=A_j·nearest(t_j/A_j), h_j=N_j−n_j.

A fixed tie convention for nearest is harmless. These exact-root definitions are mathematical indices; no finite floating-point approximation is used to certify them.

As A_j+1<2^b_j and s_j≥8(j+b_j),

    (A_j+1)N_j^(−1/4)
      <2^(b_j−s_j/4)≤2^(−2j−b_j)→0.           (1)

This is stronger than the analytic requirement A_j=o(N_j^(1/4)). Analysis's explicit bound, valid on the compact quadratic critical window, therefore gives for the FULL actual center

    |c_(n_j,h_j)−(e+pi)|
      ≤C(A_j+1)N_j^(−1/4)→0.                   (2)

That bound retains the full exponential coordinate, both pole residues, determinant and both vertical endpoints. It is attributed to FIXED_CONGRUENCE_INVERSE_CRITICAL_COROLLARY.md §3, not rederived as an arithmetic estimate. In particular n_j~sqrt(2N_j), h_j~N_j. Since A_j is divisible by4 and N_j is a power of2, n_j,h_j are positive multiples of4 eventually.

Also max(S_j)=p_j≤A_j, and (1) implies eventually h_j≥p_j+1 and N_j≥2p_j. The required size hypotheses are thus uniform over the chosen set, without estimating the distribution of primes.

## 2. Uniform all-prime actual denominator equality

For every sufficiently large j and every p∈S_j,

    p|n_j,  h_j≥p+1,  N_j=1 modp,  N_j≥2p.

The L20 residue theorem gives epsilon E=−1 modp. Its COMPLETE primitive comparison is uniform in p at the stated sizes, so after the final numerator/denominator gcd,

    v_p(q_j)=v_p(N_j!)+v_p(U_j).                (3)

This is the actual reduced denominator of the full center. Since U_j is an integer, the factorial term supplies a lower bound. The power-two dyadic eligibility also holds: for 0<n_j<N_j, binom(2N_j−n_j−1,N_j) is odd, hence selector's exact result gives v_2(q_j)=N_j. This dyadic contribution is not needed to prove the unbounded odd rate.

## 3. A single sequence with log(q_j)/N_j→infinity

Put

    W_j=Σ_(p∈S_j) log(p)/(p−1).

The elementary factorial bound

    v_p(N!)≥N/(p−1)−(1+log_p N)

and (3) give

    log(q_j)≥N_j W_j−j log N_j−Σ_(p∈S_j) log p.  (4)

The product of the distinct primes in S_j divides A_j, so Σ logp≤log A_j<b_j log2 and j≤b_j. Also b_j≤s_j/8. Thus the error in (4), divided by N_j=2^s_j, is bounded by a constant times s_j²/2^s_j, which tends to0. Consequently

    log(q_j)/N_j≥W_j−o(1)→infinity.             (5)

The last step uses the classical divergence of the prime reciprocal sum: logp/(p−1)≥1/p for every odd prime. No quantitative prime number theorem is required. If desired the exact dyadic factor adds log2 to the lower rate in (5).

This upgrades L20's statement “for each fixed finite rate there is a subsequence” into ONE explicitly synchronized sequence with unbounded surviving rate. The complete numerator's forced unit is used at every chosen prime, so this is not a diagonal argument over experimental certificates or unproved good-prime supply.

## 4. Evaluated rational shifts with fixed odd support

Fix ANY finite set T of odd primes. Let delta_j be arbitrary rational numbers whose complete reduced denominators have no odd prime outside T. Their coefficients, height, degree or dyadic denominator may vary freely. At each p∈S_j\T, delta_j is p-integral while the old center has negative valuation by (3). Therefore

    v_p(q'_j)=v_p(q_j)=v_p(N_j!)+v_p(U_j)
       for q'_j=denominator(c_(n_j,h_j)+delta_j).  (6)

Deleting the finitely many terms from T changes W_j by a bounded constant. The same estimate proves

    log(q'_j)/N_j→infinity.                      (7)

If delta_j→0, the corrected centers still converge to e+pi by (2). Selector's exponentially small norm5/dyadic cancellation shifts are one example with fixed evaluated odd support {5}; their exact correction arithmetic and coefficient costs are owned by selector and are not rederived here. Removing the dyadic denominator cannot remove the odd growth in (7).

The qualifier concerns the COMPLETE evaluated shift, not the leading coefficient or norm of a pole polynomial considered in isolation. In particular selector's freshly derived response change p/q→(p+12)/(q+2) has a difference whose denominator can involve all the old q primes. It need not be p-integral at S_j\T and is not excluded by (6). Moving old prime factors to new ones need not reduce the size of q; this note makes no claim about that separate content problem.

## 5. What this proves and what remains open

Equations(2),(5),(7) are complete-center and actual-final-denominator statements. They show that increasing synchronized factorial layers survive fixed evaluated odd-support corrections, with a rigorously priced varying congruence modulus. They do not provide a lower bound for the rounded approximation error. A very large denominator and an upper error bound alone do not prove that the primitive residual grows, or even that it fails to shrink. Response changes and corrections with growing evaluated prime support remain distinct mechanisms. No irrationality statement about e+pi is established here.
