> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact minimal Gaussian-endpoint moment clearer

Root original deduction, 2026-10-02. This is an incremental research note, not stage closeout. It sharpens the deliberately nonminimal clearer in the inherited direct-selector draft. It does not establish a uniform dyadic lower bound for the complete b=3 center.

## 1. Archive and literature boundary

The archive search covered sources and work, excluding bundled libraries and this session, for minimal moment clearers and Gaussian denominator formulas. In `work/session_20261001_astra/DIRECT_SELECTOR_HEIGHT_OBSTRUCTION_DRAFT.md`, Section 3 uses `2^(N-1) lcm(1,...,N)` and explicitly makes no minimality claim. `CANONICAL_COMPANION_TRANSFER.md` imports that choice. Those proofs remain valid with their original larger integers. No earlier minimal formula for this exact moment functional was located.

Primary literature searches used Gaussian rational moments, arctangent denominators, and 2-adic Hermite valuations. Opened Jack S. Calcut, *Gaussian Integers and Arctangent Identities for pi*, American Mathematical Monthly 116 (2009), author-hosted primary PDF https://isis2.cc.oberlin.edu/faculty/jcalcut/gausspi.pdf, for the Gaussian arithmetic context; it does not supply this selector's denominator theorem. Also opened Amdeberhan and Moll, *Involutions and Their Progenies*, https://www.math.tulane.edu/~vhm/papers_html/invo-final.pdf, for valuation-method context; its Hermite/involution sequence is different from the n-dependent contact polynomial here. The calculation below is elementary and no general mathematical novelty is claimed.

## 2. Exact moments

Let a=(1+i)/2 and

    calL(f)=integral_-1^1 f((1+iu)/2) du,
    mu_j=calL(t^j), j>=0.

Integrating the monomial along the segment gives

    mu_j=4 Im((1+i)^(j+1))/(2^(j+1)(j+1)).

Consequently, with k>=0,

    mu_(2k)=(-1)^floor(k/2) 2^(1-k)/(2k+1),
    mu_(4k+1)=(-1)^k 2^(-2k)/(2k+1),
    mu_(4k+3)=0.                                      (1)

For the first line the sign pattern is +,+,-,-,+,+,...; powers of two and the odd denominator are already coprime. The first moment is mu_0=2 and mu_1=1.

## 3. Minimal universal integer

For N>=1 let O_N be the lcm of all positive odd integers at most N. Define

    e_N=max(0, floor((N-1)/2)-1, 2 floor((N-2)/4)),
    L_min(N)=2^e_N O_N.                               (2)

Then L_min(N) is exactly the smallest positive integer for which

    L_min(N) calL(P) is an integer

for every P in Z[t] of degree at most N-1.

Proof. By (1), the largest denominator power of two amongst these moments is e_N. The nonzero even moments have odd denominators 2k+1 covering all positive odd integers at most N (or N-1 when N is even, which gives the same O_N). Hence their odd denominator lcm is exactly O_N. These observations give sufficiency. Necessity follows by applying any proposed clearer to each monomial separately: its valuation at every prime must dominate the largest denominator valuation of a moment. Taking that maximum prime by prime yields precisely (2). No primitivity assumption on P is used. End of proof.

Equivalently, for sufficiently large N,

    e_N=N/2-2       if N=0 mod4,
    e_N=(N-3)/2     if N=1 or3 mod4,
    e_N=N/2-1       if N=2 mod4.

The max with zero handles N=1,2,3,4. For example L_min(4)=3, L_min(5)=30, L_min(6)=60 and L_min(7)=420.

## 4. Actual companion normalization

If the integral Rodrigues selector has forcing U!=0, kernel K in Z[t] of degree at most N, and beta=calL((K-U)/(t-1))/U, then

    den(beta) divides L_min(N) |U|.                   (3)

For the inherited canonical coefficients z and positive forcing Dg, put

    T_z,min=L_min(N) calL((K_z-Dg)/(t-1)).

This is an integer and is still divisible by the actual coefficient content g, because K_z and Dg have that factor. The exact endpoint-corrected companion formula becomes

    den(kappa+beta)
      =F L_min(N) Dg /
       gcd(F L_min(N) Dg,
           |L_min(N) Delta x0+F T_z,min|),
    F=(n!)^2.                                       (4)

The final gcd in (4) cannot be removed. Formula (4) describes the same rational number as the larger historical clearer, so it does not alone imply a smaller actual denominator. It does reduce the artificial dyadic part of the shared integer lattice by

    2^[(N-1)+floor(log_2 N)-e_N].

Odd-prime moment bounds and the new odd-prime b=3 theorem are unchanged. The global regular-factor height from the archived resultant factorization may be recomputed with this smaller L, but its unresolved factorial cancellation remains unresolved.

## 5. New full-beta data and the remaining dyadic problem

`B3_COMPLETE_TWO_ADIC_PROBE.json` records newly computed exact complete beta and complete center values for n=3,...,80. Unlike the inherited coefficient-only scans, these data use the entire Gaussian moment functional and actual rational reduction. On this finite range beta is 2-adically integral and its valuation is strictly larger than that of the endpoint-corrected factorial companion, so the center has exactly the companion's negative valuation. This is finite evidence only.

The observed factorial companion denominator rate is consistent with (3/2)n+O(log n), but no uniform bound on v_2(V_n) or all-depth proof has been obtained. A lifted dyadic zero may not be discarded on the basis of these data. The odd-only seventeen-prime theorem offers a separate arithmetic route which needs no dyadic assumption.

## 6. Status

Equations (1)-(4) are author deductions with complete elementary proofs. No independent review is claimed. The minimal clearer target is completed; a full uniform dyadic center-denominator law remains open. Neither result decides the rationality of e+pi. Research continues under the human's stated stopping conditions.
