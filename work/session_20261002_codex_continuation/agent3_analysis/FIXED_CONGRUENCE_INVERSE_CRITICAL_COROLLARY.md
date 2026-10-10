> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Complete inverse-critical convergence on a prescribed fixed congruence lattice

2026-10-02. Original analytic corollary by agent3, prompted by the arithmetic agent's finite-prime handoff. This note does not review that arithmetic theorem. It identifies exactly how its index congruences fit the complete reflected-center convergence theorem. All implied constants below may depend on a FIXED prescribed modulus; no uniform growing-prime atlas is asserted.

## Fresh target gate

Archive queries were `(fixed.{0,15}(modulus|A)|arbitrary.{0,15}(modulus|congruence)|finite.{0,15}prime.{0,10}set).{0,80}(inverse|critical|round)`, `inverse.{0,30}critical.{0,30}(A|modulus)`, and `rounded.{0,20}(A|modulus)`. The exact overlap is `POWER_TWO_INVERSE_CRITICAL_SUBSEQUENCE.md`, which handles modulus20. Earlier finite-prime congruences belong to different constructions. This bounded search makes no global novelty claim.

Fresh primary queries were `site:arxiv.org Hermite Pade uniform multi-index rational approximation asymptotic integer` and `site:arxiv.org saddle point asymptotic implicit inversion nearby parameter uniform`. Opened the primary papers https://arxiv.org/pdf/math/0510278 and https://arxiv.org/pdf/1705.01190 again for the uniform multi-index/saddle background. Their general asymptotic methods are overlap; no external theorem about this rounded index is imported. The argument below uses the exact critical curve and the previously derived complete uniform reflected-center formula.

## 1. Fixed-modulus rounding theorem

Fix a positive integer M divisible by4. For N=2^s let t_N be the exact real inverse-critical root from `POWER_TWO_INVERSE_CRITICAL_SUBSEQUENCE.md`:

    Psi_N(t)=t^(3/2)/sqrt(N)−2sqrt(N)/sqrt(t)
             +(1/2)log N−(3/2)log t−log4=0.        (1)

Take

    n_N=M·nearest_integer(t_N/M), h_N=N−n_N.        (2)

For all sufficiently large s, n_N is a positive multiple of4, h_N>=6, h_N is divisible by4, N=n_N+h_N, and the actual projected reflected family is defined with positive U. Its complete center satisfies

    c_(n_N,h_N)=e+pi+O_M(N^(−1/4)).               (3)

Both ordinary-exponential and vertical endpoint contributions are retained. Its actual dyadic denominator has v2(q)=N by the selector's eligible power-two case. Equation(3) does not assert a lower bound for this rounded error or a small primitive residual.

Proof. Put x=sqrt(2N). The exact curve has

    t_N=x+[sqrt(x)/(2sqrt2)]
              [(1/2)log x+log(4sqrt2)]+O(log²x),   (4)

so t_N is asymptotic to x. Its derivative is

    Psi_N′(t)=3/(2R)+R/t−3/(2t), R=sqrt(N/t),
    Psi_N′(t_N)=(2sqrt2+o(1))/sqrt(t_N).           (5)

The rounding in(2) changes t by at most M/2. Uniformly on that fixed-width interval, (5) is O(t_N^(−1/2)), giving Psi_N(n_N)=O_M(t_N^(−1/2)). Also lambda=N/n_N² tends to1/2 and R tends to infinity. The complete author formula from `REFLECTED_KERNEL_QUADRATIC_CRITICAL_WINDOW.md` is

    alpha=e exp[Psi_N(n_N)](1+O(n_N^(−1/2)))
          −exp[−R+1/4−lambda/4](1+O(n_N^(−1/2))),
    |beta−pi|<=exp[−(1/2)n_N log n_N+O(n_N)].       (6)

Hence alpha=e+O_M(n_N^(−1/2)) and beta=pi+o(n_N^(−1/2)). Since n_N is asymptotic to sqrt(2N), this proves(3). This is a fixed-N rounding argument; the fixed-n nearest-N theorem is not substituted for it.

The response is retained explicitly:

    U/T=2R D A(1+O(n_N^(−1/2)))>0, T=(h_N−1)!,    (7)

with the positive exact D,A sums from the preceding analysis notes. The endpoint estimate in(6) concerns the complete beta, and no positive-modulus ensemble replaces the actual exponential coordinate.

## 2. Compatibility with a finite set of actual prime layers

The arithmetic agent's L20 handoff asserts the following distinct arithmetic interface: for an odd prime p, on its stated domain p|n, h>=p+1, N=1 modp and N>=2p, the complete projected numerator is a p-unit and

    v_p(q)=v_p(N!)+v_p(U).                       (8)

This note neither rederives nor audits(8). Its saved author theorem is `agent1_arithmetic/REFLECTED_UNIVERSAL_PRIME_RESIDUE.md`, Sections2–5; its supporting complete-q receipt is `agent1_arithmetic/REFLECTED_UNIVERSAL_PRIME_RESIDUE_RECEIPT.json`. The author attribution is preserved here rather than presenting it as an analytic proof.

For any FIXED finite set S of odd primes, put

    M=lcm(4,{p(p−1):p in S}),
    J=lcm({ord_p(2):p in S}).                    (9)

Restrict s to positive multiples of J and use(2). Then p|n_N and N=2^s=1 modp for every p in S. The remaining size conditions hold for all sufficiently large s. Thus the complete convergence statement(3), exact actual v2(q)=N, and all the author-attributed depths(8) can coexist on one infinite subsequence. This uses a fixed M and J, with their full size retained; it does not assume primes in moving intervals or extend(8) to an unproved chart.

In particular finite prime layers may survive while a shared-prime rational correction removes the actual dyadic factor. Such a correction changes the full center only by its explicit endpoint shift; equation(3) alone does not show that the corrected primitive residual is small. For a norm5 correction with d<b5 the exact complete mesh and height obligations are in `SHARED_FIVE_COMPLETE_COEFFICIENT_MESH.md`.

## 3. Explicit modulus dependence, without a prime-distribution claim

The proof itself gives a useful quantitative condition. Uniformly while M/sqrt(t_N) tends to zero, the derivative estimate on the rounding interval and the complete formula(6) give

    |c−(e+pi)|<=C(M+1)/sqrt(t_N)
              <=C′(M+1)N^(−1/4).                (10)

The constants in this analytic statement come from the compact-lambda uniform theorem, not from a finite-prime arithmetic atlas. Thus an independently supplied varying congruence modulus satisfying M=o(N^(1/4)) would preserve convergence. Constructing a useful varying prime set with all the simultaneous arithmetic hypotheses is a separate question. No such set or uniform arithmetic rate is asserted here.

If M is comparable to N^(1/4), bounded n-rounding need not make Psi_N(n_N) tend to zero: its displacement can produce a bounded nonzero exponent in(6). This identifies the analytic modulus cost rather than silently treating an increasing congruence lattice as fixed.
