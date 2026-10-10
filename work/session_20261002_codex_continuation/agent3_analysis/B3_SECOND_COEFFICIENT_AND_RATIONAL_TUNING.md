> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Explicit B3 second coefficient and a rational positive-weight tuning

Author: Codex continuation Agent 3, 2026-10-02. Original follow-up to the fixed-size metric theorem, not independently examined. The new symbolic derivation is derive_b3_second_correction.py/.txt; it expands Gaussian saddle coefficients and contains no finite-index center sample or historical checker replay.

Fix b=3 and retain the exact B-coefficient reconstruction K. Put sigma=sqrt(2), M=1+sigma and gamma=-(2+sigma/8). Let c_j be its four actual coordinate centers, with coordinate zero's endpoint retained. The top coordinate j=3 has

    c_3-(e+pi)=(-1)^(n+1)4pi M^(-2n-3)
       [1+gamma/n+eta_top/n^2+O(n^-3)],
    eta_top=(241-100sigma)/64.                    (1)

The coordinate-spread theorem consequently gives

    eta_0=eta_1=(113-100sigma)/64<0,
    eta_2=(177-100sigma)/64>0,
    eta_3=(241-100sigma)/64>0.

The original factorial B-only Gram center therefore has the explicit further correction

    c_n-(e+pi)=(-1)^(n+1)4pi M^(-2n-3)
       [1-(2+sigma/8)/n+(177-100sigma)/(64n^2)
                                               +O(n^-3)]. (2)

This absolute second coefficient is independent of the first depth-comparison theorem; the latter needed only coordinate differences.

## 1. Reproducible saddle/cofactor algebra

Write h=1/n, a=sigma/(2M), beta=sigma M/2 and m_k=H_(i,j)/H_00 for k=j-i. To obtain the top cofactor through relative h^2, the normalized moments must be expanded through h^3. Their coefficients are:

    m_-2=1+(-4-3sigma)h+(23+17sigma)h^2/2
                                      -(424+315sigma)h^3/16+O(h^4),
    m_-1=1-(6+5sigma)h/4+(9+12sigma)h^2/16
                                      -(41+55sigma)h^3/32+O(h^4),
    m_0=1,
    m_1=1+(2+3sigma)h/4+(25+4sigma)h^2/16
                                      +(-69+25sigma)h^3/32+O(h^4),
    m_2=1+sigma h+(3-3sigma)h^2/2
                                      +(-168+9sigma)h^3/16+O(h^4).

Multiplying the final adjugate row by D_i=(-sigma)^i and the common factor 2a/h gives the positive-leading coefficient vector A_i(h):

    A_0=1-(7+3sigma)h/2+(189+107sigma)h^2/16+O(h^3),
    A_1=2sigma-(2+5sigma)h+(27+53sigma)h^2/4+O(h^3),
    A_2=2+(-1+2sigma)h+(81-sigma)h^2/8+O(h^3).

These common factors cancel in the top-coordinate selector. The complete exponential forcing and coordinate endpoints are factorially small and do not enter any displayed inverse-power coefficient.

Let f_i=fP_i/fP_0 and g_i=eF_i/eF_0. The normalized positive-circle/arc scalar expansions give

    f_0=g_0=1,
    f_1=1+sigma/2-(1+sigma)h/4+(8+9sigma)h^2/32+O(h^3),
    g_1=1-sigma/2+(-1+sigma)h/4+(8-9sigma)h^2/32+O(h^3),
    f_2=3/2+sigma-(3/2+sigma)h+(44+29sigma)h^2/16+O(h^3),
    g_2=3/2-sigma+(-3/2+sigma)h+(44-29sigma)h^2/16+O(h^3).

The scalar saddle ratio is

    eF_0/fP_0=(-1)^(n+1)4pi M^(-2n-1)
       [1-sigma h/8+(1+4sigma)h^2/64+O(h^3)].

The exact top-coordinate logarithmic contraction is
(eF_0/fP_0)(sum_i A_i g_i)/(sum_i A_i f_i).
Expanding this quotient gives 1+gamma h+eta_top h^2 relative to M^-2, proving (1).

For completeness the moment algebra comes from

    log((1+sigma cos t)/M)
       =-a t^2+d t^4+f t^6+g t^8+O(t^10),

    d=a/12-a^2/2,
    f=-a/360+a^2/12-a^3/3,
    g=a/20160-a^2/160+a^3/12-a^4/4.

After t=sqrt(h)x, the contact exponent has coefficients delta_j in sqrt(h):

    delta1=i(k-sigma)x,
    delta2=sigma x^2/2+d x^4,
    delta3=i sigma x^3/6,
    delta4=-sigma x^4/24+f x^6,
    delta5=-i sigma x^5/120,
    delta6=sigma x^6/720+g x^8.

The formal exponential coefficients obey E_0=1,
E_m=(1/m)sum_(j=1)^m j delta_j E_(m-j).
Integrate E_(2r) against the normalized Gaussian using
E[x^(2l)]=(2l-1)!!/(2a)^l and discard odd moments. Divide by the k=0 series before taking the cofactors. This gives every displayed coefficient with exact rational/sqrt(2) arithmetic; fixed-size Gaussian localization controls the remainder.

## 2. What positive rational tuning can and cannot cancel

At b=3, 0<eta_top<2. Hence the second-coefficient interval criterion is nonempty: changing the positive coordinate mean can remove THIS inverse-power correction. The original leading term and gamma/n remain universal and nonzero, so the exponential regime remains unchanged.

A particularly simple change retains the original factorial weights except that row j=1 receives a squared-weight multiplier R>0:

    W_R=diag(w0^2,R w1^2,w2^2,w3^2).

The limiting coordinate probabilities are proportional to (R,4,1) on j=1,2,3. Thus its second relative coefficient is

    eta(R)=eta_top-(2R+4)/(R+5).                  (3)

The exact positive root is

    Rstar=(5eta_top-4)/(2-eta_top)
         =(7237+38400sigma)/7231.

No FIXED rational R can make (3) vanish, since eta_top is irrational while (2R+4)/(R+5) is rational. There is, however, a fully specified n-dependent rational choice:

    z_n=floor(sqrt(2n^2)),
    R_n=(7237n+38400z_n)/(7231n)>0.                (4)

It is computed from integer square roots and rational arithmetic without e+pi. Since R_n-Rstar=O(1/n), the resulting actual rational weighted center has

    c_(W_Rn)-(e+pi)=(-1)^(n+1)4pi M^(-2n-3)
                    [1+gamma/n+O(n^-3)].         (5)

This follows from the coordinate expansion and exact convexity; weight-dependent O(1/n) deviations of the probabilities move the canceled n^-2 coefficient only at order n^-3. The floor sequence need not have a common third asymptotic coefficient, so none is asserted.

The metric (4) adds a rational multiplier with numerator and denominator O(n) to the existing exact Gram construction. Its new clearing cost is polynomial, but the ACTUAL reduced denominator can change through its own combined gcd. No polynomial ratio of reduced denominators, inheritance of the canonical prime atlas, or primitive-error improvement follows. It cancels a subleading correction and cannot remove either larger term in (5).

Therefore positive rational metric tuning can modify and cancel this second correction, but cannot produce the exponential improvement sought at fixed b. The original permitted factorial-depth family is even more rigid: its second coefficient is fixed, and its first depth-dependent change occurs only at third order.

## 3. Search and attribution

Before computing this target, archive rg queries included second relative coefficient, eta_b, second signed Gram error, canonical second coefficient and quadratic correction center. No matching explicit B3 coefficient was found by these bounded searches. This is not a global novelty claim.

Current primary-source queries:
- fixed size Toeplitz moment determinant higher order saddle asymptotic expansion Schur insertion
- Hermite Pade approximant remainder second order asymptotic correction

Opened [Garcia-Garcia and Tierz](https://arxiv.org/abs/1706.02574) and [Mano and Tsuda](https://arxiv.org/html/1502.06695); the full Garcia-Garcia/Tierz and Wielonsky author PDFs were already opened for this same metric phase. Their overlap is the established determinant/Schur and HP asymptotic methodology, not this specific center coefficient or rational multiplier.

No new independent audit, external publication, growing-b assertion, denominator estimate or rationality claim for e+pi is made.

