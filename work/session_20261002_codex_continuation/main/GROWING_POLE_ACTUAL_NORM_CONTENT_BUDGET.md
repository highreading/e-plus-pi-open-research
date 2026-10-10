> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# M32. Uniform actual norm and complete content budget for growing poles

Original Root author transfer, 2026-10-02. Scope: M31's actual short stack, EVERY1<=m<=k once k>=131072. No main irrationality or global gcd theorem. The earlier simple-pole actual response scale in agent2_selector/SHORT_STACK_ACTUAL_RESPONSE_SCALE.md is credited; the new target is the uniform growing-order specialization with the exponential-cost COMPLETE moment clearer and final polynomial content.

## Fresh target gate

A fresh archive/session search found no completed uniform growing-pole norm/content budget. M24's scalar response norm and M31's conditional-characteristic comparison are prior inputs, not rediscovered claims. Fresh online searches concerned factorial/Gamma moment Hankel norms and mixed orthogonal determinant asymptotics. Read Kuijlaars, https://arxiv.org/pdf/1004.0846, §2.1 determinant ensemble/existence condition; its positivity hypothesis is not automatically assumed for our signed upper functional. The actual positivity here is the separately proved M31 conditional-Gram theorem. NIST DLMF https://dlmf.nist.gov/18.3 supplies classical polynomial norm background; the elementary interval/Hilbert bounds below suffice without importing a general Riemann-Hilbert asymptotic. No specific published answer to this new content specialization was located in these bounded searches.

## Exact full-value comparison

Let beta=det[C;R+TV], delta=B_m^k E_(k,m)^k as in GENERAL_POLE_RANK_M_PRIMITIVE_INTERFACE.md, I_j=delta beta_j, and g=gcd(I_0,...,I_m). The final primitive polynomial P has coefficients ±I_j/g.

M31's full signed insertion theorem gives, with a=1/(48e^4),

    exp(-4/a)F*_k detG_(sigma_m,k)
      <=|beta(S)|<=F*_k detG_(sigma_m,k),
    F*_k=det M_[mu(y+1)^k,k].                           (1)

The reference F*_k is INDEPENDENT of m because k>=m annihilates every upper endpoint jet. The actual compact measure obeys

    (1/2)y^(-1/2)dy <=dsigma_m<=6m y^(-1/2)dy.          (2)

Both endpoints and all period derivatives were already included before (1). This is a complete determinant value comparison, not a raw entry bound or a coefficient-only comparison.

## Tail reference scale with elementary upper and lower bounds

The reference moments are sum_(h=0)^k binom(k,h)D_(2(i+j+h)). Factor k^(2i) from rowi, k^(2j) from columnj, and k^(2k) from each row. The total scale is

    k^(4k^2-2k).

Since i+j+h<=3k-2, D_(2n)<=(2n)! gives a residual entry bound exp(Ck) after this scaling, with an absolute C. Hadamard bounds the residual determinant by exp(C'k^2). Thus

    logF*_k <=4k^2logk+O(k^2).                          (3)

For the LOWER bound restrict the true mu tail to y in[k^2,4k^2]. Its density is >=exp(-2k-1)/(4k), and (y+1)^k>=k^(2k). Substituting y=k^2z gives the same row/column scale, a positive density factor k exp(-2k-1)/4 in each of the k rows, and the ordinary Gram on[1,4]. Its determinant is 3^(k^2) times the Hilbert Gram determinant on[0,1]. The classical Cauchy formula implies that the logarithm of the latter is O(k^2) in absolute value. Loewner order of positive Grams preserves this determinant lower bound. Therefore

    logF*_k >=4k^2logk-O(k^2),
    logF*_k =4k^2logk+O(k^2).                           (4)

This keeps the full moment degree k of the reference weight, in addition to the k-dimensional Gram. Treating it as an ordinary unweighted factorial determinant would miss half the leading scale.

For the compact reference gamma=y^(-1/2)dy, the moment Gram is[1/(i+j+1/2)]. Its diagonal upper bound gives logdet<=O(k), while gamma>=dy and the Hilbert/Cauchy lower bound give logdet>=-Ck^2. Equation (2) changes these logs by at most O(klog(m+1)+k), uniformly m<=k. Hence

    |logdetG_(sigma_m,k)|<=C'k^2.                       (5)

Combining (1),(4),(5) proves the ACTUAL full determinant scale

    log|beta_(k,m)(S)|=4k^2logk+O(k^2),                 (6)

with constants independent of m throughout1<=m<=k.

## Final evaluated content is the leading arithmetic issue

The complete Gaussian moment clearer in M31 has logdelta=O(k^2) in this range. Consequently the FINAL primitive value satisfies

    log|P_(k,m)(S)|=4k^2logk-logg+O(k^2).                (7)

Every constant in (7) is uniform in growing m. No actual gcd is replaced by its guaranteed factorial divisor.

For any fixed epsilon>0, along ANY subsequence with

    logg <=(4-epsilon)k^2logk,

the primitive values diverge in absolute value. Thus a primitive-small subsequence necessarily has

    liminf logg/(k^2logk)>=4.                           (8)

This is a necessary content budget, not a bound ruling out (8). Pole-order growth improves the normalized product error at an O(km) logarithmic scale, at most O(k^2) here; it does not remove the4k^2logk full-value scale before actual content is counted.

The full product theorem also gives log|beta(S)/beta_m|=O(k^2), uniformlym<=k. Therefore the ACTUAL leading rational coefficient has

    log|beta_m|=4k^2logk+O(k^2),
    log|I_m/g|=4k^2logk-logg+O(k^2).                    (9)

The guaranteed F_(k-m)^2 divisor in M31 yields the ceiling

    log|I_m/g| <=[4k^2-(k-m)^2]logk+O(k^2).             (10)

The Stirling remainder is uniform: n^2log(n/k)=O(k^2) for0<=n<=k, includingn=0. Formula (10) is an upper bound on the leading coefficient. It is NOT an equality, a lower bound, or a bound on the entire coefficient height without further root/middle-coefficient control.

If S were rational with denominatorv, M31 supplies P(S)!=0 and the primitive degree-m polynomial would obey |P(S)|>=v^(-m). A research construction must beat this bound with its COMPLETE primitive values. The uniform nonzero and product theorems do not yet give the required evaluated gcd. No stop condition or proof-completion claim follows from (7)–(10).
