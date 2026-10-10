> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Metric correction and positive-weight tuning: saved original progress

Codex continuation Agent 3, 2026-10-02. Original analysis, not independently reviewed. Saved before the newly requested bounded arithmetic audit.

Target: first correction that depends on the actual reconstruction metric, and whether rational positive diagonal weights can cancel logarithmic terms or change the exponential regime. Fixed b>=3, d=b-1 throughout; no growing-b statement.

Pre-target archive searches: metric-dependent, weight/second/correction, positive weight/cancel, Gram/convex/coordinate, coordinate/first correction, first metric correction, weight/exponential regime. Closest archive overlap is the exact convex-combination identity in agent4/COORDINATE_CENTER_ARITHMETIC.md, not an asymptotic tuning theorem.

Current primary papers searched/opened:
- [Garcia-Garcia and Tierz, Toeplitz minors and specializations of skew Schur polynomials](https://arxiv.org/abs/1706.02574), full accepted paper [repository PDF](https://repositorio.iscte-iul.pt/bitstream/10071/20917/1/Toeplitz%20minors_postprint.pdf). Overlap: exact minor formulas as symmetric insertions; different symbols/asymptotic applications. The basic Schur-insertion framework is established literature, not claimed globally new.
- [Wielonsky, Asymptotics of Diagonal Hermite-Pade Approximants to e^z](https://www.i2m.univ-amu.fr/perso/franck.wielonsky/8.pdf), full author PDF now opened. Related exact HP remainders, different family.
- [Mano and Tsuda](https://arxiv.org/html/1502.06695), [Pan and Prokhorov](https://arxiv.org/abs/2407.04852). Structural overlap only.
Queries: fixed size Toeplitz minors Schur polynomial insertions asymptotic expansion saddle Gaussian; Hermite Pade weighted least squares positive metric asymptotic remainder cancellation.

## Derived progress

Let u=K T^(-1)fP and v=e0+K T^(-1)fQ. Each reconstructed coordinate u_j, 0<=j<=b, has a nonzero leading term for all sufficiently large n at fixed b. Define exact coordinate c_j=v_j/u_j. For ANY positive diagonal B-coefficient metric with rational entries, possibly depending arbitrarily on n,

    c_W=sum_j alpha_j c_j,
    alpha_j=W_jj u_j^2/sum_k W_kk u_k^2>=0,
    sum_j alpha_j=1.

Thus uniform fixed-b coordinate asymptotics transfer independently of how large the weight ratios become.

The coordinate selectors all agree through first relative order:

    c_j-S=(-1)^(n+1)4pi M^(-2n-b)
           [1-(d+sqrt2/8)/n+O_b(n^-2)],

including the actual coordinate-zero endpoint. The reason is that row j of K is led by the final inverse row, and its next inverse-row contribution has a coefficient O(1/n); all inverse rows are proportional at leading order, so normalization postpones its effect to 1/n^2.

Therefore every positive diagonal weighting has the same nonzero leading term and the same first correction, with a remainder bound independent of the weights. At fixed b, no such tuning can alter the exponential error rate or cancel the leading logarithmic term. This includes rational weights with extreme n-dependence. It does not exclude growing b, off-diagonal metrics, signed combinations or changes to the contact/reconstruction problem.

The first coordinate spread at SECOND order appears particularly simple. Let eta_b be the second relative coefficient of the final reconstructed coordinate j=b. Then

    c_j-S=sign*4pi M^(-2n-b)
        [1+gamma/n+(eta_b-s_j)/n^2+O_b(n^-3)],
    gamma=-(d+sqrt2/8),
    s_0=d, s_j=b-j for 1<=j<=b.

Derivation: relative to the d-particle cofactor insertion from the fixed-b note, the next inverse row inserts e1(z). Its first nonproportional correction against e_(d-i)(z^-1) is

    B(k)=[2k+2sqrt2*d-d^2]/(4a), k=d-i,
    a=sqrt2/[2(1+sqrt2)].

The difference comes from E[XY]+sqrt2 E[X^2]-E[sum x_l^2]/2 with X=sum all x, Y=sum k selected x. The difference of its binomial forcing contractions equals d after the inverse diagonal factor. Meanwhile the reconstruction ratio K_(j,d-1)/K_(j,d) is -s_j/(dn)+O_b(n^-2), including s_0=d. Multiplication gives the displayed -s_j shift. This coefficient still needs a coherent final write-up, not another audit.

For arbitrary positive weights the second relative coefficient is eta_b-sbar(n), where

    sbar(n)=sum_j alpha_j(n)s_j in [0,d].

Thus its potential cancellation is an explicit interval question eta_b in [0,d], not independent assignments of selector zeros. Regardless of that answer, the first two larger terms persist and the exponential regime is unchanged.

For the original fixed factorial weights, alpha_0->0 and alpha_j->binom(d,j-1)^2/binom(2d,d). Hence sbar->d/2 and the SECOND error coefficient is eta_b-d/2, independent of m_w. The first metric/weight-depth dependence within the allowed fixed factorial family is postponed at least to THIRD order. Its explicit m_w dependence is the next analytic target.

No global novelty claim, denominator estimate, primitive shrinking form, or rationality claim for e+pi is made.

