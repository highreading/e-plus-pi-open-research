> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Extending the actual-center range by Gaussian moments

Author: Codex continuation Agent 3, 2026-10-02. Original author analysis, not independently reviewed. This improves only the uniform localization step of GROWING_B_CHARACTERISTIC_PRODUCT_ASYMPTOTIC.md. Its exact cofactors, characteristic products, endpoint, forcing decomposition, inverse normalization, K reconstruction and positive-metric convexity are retained.

The complete actual-center theorem extends to

    b=o(n^(1/3)), b>=3.                                  (1)

For ANY positive diagonal rational W_n,

    c_W-(e+pi)=(-1)^(n+1)4pi(1+sqrt(2))^(-2n-b)
       [1+O(b^3/n+b/sqrt(n)+exp(-cn+Cb^2))],              (2)

with positive absolute constants c,C, along sequences satisfying (1). The complete exponential forcing and coefficient-zero endpoint are included. Their factorial bounds from the preceding note are absorbed by the displayed error. No quantitative independent review or actual-denominator theorem is claimed.

This admits b=floor(n^theta) for every 0<theta<1/3, giving an approximation-error factor exp(-log(1+sqrt(2))n^theta+O(1)) beyond fixed b. The leading logarithmic rate divided by n remains -2log(1+sqrt(2)). The critical cubic size and proportional size are not covered by a relative 1+o(1) Gaussian theorem here.

## 1. Target checks and literature overlap

Before this refinement, narrow archive searches included b with exponent 1/3, cubic dimension correction, b^3/n, fourth trace moment and uniform Gaussian moments in the contact-normality/contact-inverse sources and the current analytic notes. No exact actual-center theorem in (1) was located by these bounded queries. This is not a global novelty claim.

Primary searches:
- site:arxiv.org Gaussian unitary ensemble fourth trace moment 2 n cubed n Wick
- site:arxiv.org Toeplitz localized determinant Gaussian ensemble perturbation varying size moments Laplace

Opened [Haagerup and Thorbjornsen, Asymptotic expansions for the Gaussian Unitary Ensemble](https://arxiv.org/abs/1004.3479), including its [full paper](https://arxiv.org/pdf/1004.3479). Its trace-moment/expansion methodology is established literature. The Gaussian moments below are rederived at the exact normalization needed here; its general asymptotic theorem is not imported. The primary Toeplitz/HP papers and archive overlap for the characteristic-product target were already searched/opened and are logged in the preceding note.

## 2. Gaussian identities at the actual normalization

Let the r-variable positive Gaussian ensemble have density proportional to

    exp(-A sum_l t_l^2) Delta(t)^2, A>0.

It is the eigenvalue density of a Hermitian matrix X with density exp(-A tr X^2). Its entry covariance is

    E[X_ij X_kl]=(1/(2A)) delta_(i,l)delta_(j,k).

Differentiating its partition function, or using this covariance, gives

    E sum t_l^2=r^2/(2A),
    E (sum t_l)^2=r/(2A),
    E sum t_l^4=r(2r^2+1)/(4A^2).                         (3)

For the last identity expand tr X^4 and apply the three Wick pairings. Two pairings leave three free indices and one leaves one free index; each contributes (2A)^(-2). Thus the numerator is 2r^3+r. No limit or matrix-size asymptotic is required.

The labeled eigenvalue density is exchangeable. From (3),

    E t_l^2=r/(2A), E[t_l t_k]=-1/(2A), l!=k.

Therefore the sum Y of any k selected labeled eigenvalues satisfies

    E Y^2=k(r-k+1)/(2A)<=C r^2/A.                         (4)

These identities are also valid after any fixed additive shift of A. An independent scalar s with Gaussian curvature B has E s^2=1/(2B), E s^4=3/(4B^2).

## 3. A fixed local cube with a negative quartic correction

Keep sigma,M,a,beta,d and the exact characteristic products from the preceding note. The quartic logarithmic coefficients are

    a/12-a^2/2<0, beta/12-beta^2/2<0.

Consequently there is a FIXED sufficiently small delta>0 such that on |t|,|s|<=delta,

    -C t^4<=log((1+sigma cos t)/M)+a t^2<=0,
    -C s^4<=log(M(sigma cos s-1))+beta s^2<=0.            (5)

This sign avoids a large comparison cost from decreasing the Gaussian curvature by a fixed fraction. The absolute symbol amplitude divided by its value exp(-r sigma) has bound exp(C sum t_l^2). The circle/real Vandermonde ratio V lies in [0,1], and

    0<=1-V<=C r sum t_l^2.                               (6)

The normalized elementary insertion is an average of exp(iY), so its modulus is at most one and its difference from one is bounded by the corresponding average of |Y|.

Let Pplus/Pminus denote the product factors in the preceding note, normalized by their values (2+sigma)^d and sigma^d at zero. Since each factor is analytic and nonzero on this fixed cube,

    log Pplus= i[-sum t_l+d s]/(2+sigma)
                      +O(sum t_l^2+d s^2),
    log Pminus= i[-sum t_l-d s]/sigma
                      +O(sum t_l^2+d s^2).               (7)

The remainders are bounded in complex modulus with an absolute constant. In particular their real parts are at most C(sum t_l^2+b s^2). The symbol phase similarly has linear term -i sigma sum t_l and remainder O(sum t_l^2). This retains the actual complex phase.

## 4. Relative integral errors, with no dimension-dependent supremum

Write the exact local integrand divided by its Gaussian leading integrand as the product of:
- the nonpositive exponent correction in (5),
- the Vandermonde ratio in (6),
- the analytic symbol amplitude and phase,
- the elementary insertion, if present,
- the normalized characteristic product, if present.

Apply a telescoping product difference. For the first two factors use 1-exp(-x)<=x and (6). For the analytic factors use

    |exp(z)-1|<=|z| max(1,exp(Re z)).

For the characteristic products, separate the displayed imaginary linear term in (7) from the quadratic remainder, using |exp(iu)-1|<=|u|. All multiplying absolute factors are bounded by exp(C sum t_l^2+Cb s^2), with C enlarged a finite number of times.

Thus one bounds the INTEGRATED relative error by expectations of

    C[n sum t_l^4+n s^4+b sum t_l^2+sum t_l^2+b s^2
        +|sum t_l|+b|s|+the average selected |Y|]
       times exp(C sum t_l^2+Cb s^2).                     (8)

The absent scalar/insertion terms are omitted for plain determinants/cofactors. In (8), the Gaussian curvatures are A=an and B=an for the plus forcing or B=beta n for the minus forcing. Multiplication by the final exponential changes them only to A-C and B-Cb. For b=o(n), these remain positive. Homogeneous scaling gives the changed partition-function ratio

    (A/(A-C))^(r^2/2) (B/(B-Cb))^(1/2)
       =exp(O(b^2/n+b/n)).                               (9)

It is bounded and tends to one under (1). The moments (3),(4), Cauchy-Schwarz, and the scalar moments therefore bound (8) by

    O(b^3/n+b/sqrt(n)).                                  (10)

In particular n E sum t_l^4=O(b^3/n), and the Vandermonde error has the same order. The forcing phase b s has mean absolute size O(b/sqrt(n)); the trace term has the smaller size O(sqrt(b/n)). The selected-sum insertion is O(b/sqrt(n)) uniformly in its index. This establishes a relative estimate simultaneously for all cofactors and both forced contractions.

## 5. Original-domain and Gaussian tails

Outside the fixed cube, at least one variable has magnitude greater than delta, so Q=sum t_l^2+s^2>=delta^2. Use the global bounds from the preceding note:

    |1+sigma cos t|<=M exp(-c0 t^2),
    sigma cos s-1<=M^(-1)exp(-c0 s^2),
    |exp(it_q)-exp(it_p)|<=|t_q-t_p|.

All normalized insertions have modulus at most one, except for the minus characteristic product which has the harmless global bound M^d. The symbol amplitude adds exp(O(b)). Comparing the global absolute tail to the target Gaussian normalization, and splitting exp(-c0 nQ) into two equal halves, gives

    relative absolute tail<=exp(-c n+Cb^2).               (11)

The Gaussian extension tail has the same bound. The scaling cost is exp(O(b^2)), with no hidden n-dependent factorial or binomial loss. Since b=o(n^(1/3)), the bound (11) tends to zero exponentially. The negative-base part of the full circle for odd n is included here.

Equations (10),(11) replace the earlier radial supremum estimate everywhere. They prove the same determinant/cofactor/forcing relative asymptotics, now with error O(b^3/n+b/sqrt(n)+exp(-cn+Cb^2)). The determinant has a positive nonzero leading Gaussian constant on both parities.

The EXACT reconstruction step has additional O(b/n) error by top-column dominance, which is absorbed in (10). The inherited uniform complete-eE estimate gives coordinate contribution at most C[2/(2+sigma)]^d/(n!sqrt(n)); the endpoint is at most C d!/[sigma^d n!n^(2d)]. Both are negligible relative to M^(-2n-b) throughout (1). Finally exact coordinate convexity propagates the same relative bound to every positive diagonal W_n. This proves (2).

## 6. Remaining scope

This moment argument is sufficient for a relative Gaussian approximation when b^3/n tends to zero. It does not identify the critical-size law at b~lambda n^(1/3), where the common determinant perturbation need not be small, or a proportional-size equilibrium problem. The actual reduced rational denominator has not been compared across varying b or metrics. The fixed-b prime atlas is not extended by this calculation, and no rationality or irrationality claim for e+pi is made.
