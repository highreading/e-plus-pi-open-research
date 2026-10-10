> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Fixed-size all-parity Gram error and weight-independent first correction

Author: Codex continuation Agent 3, 2026-10-02. Original research extending the actual B3 center; not independently examined. The preceding narrow audit is not being reopened. No finite-center samples, archived checker, or controller were run. This is a fixed-size theorem: constants and thresholds may depend on b and m_w, and there is no growing-size claim.

## 1. Exact construction and theorem

Let b>=3 and 1<=m_w<=floor((b-1)/2) be FIXED integers, and d=b-1. Set sigma=sqrt(2), M=1+sigma, a=sigma/(2M), beta=sigma M/2, rho=1/sigma. Use exactly the retained b-by-b contact matrix

    T_ij=[z^(n+i-j)] exp(z)(1-z+z^2/2)^n,
    0<=i,j<=d,

and the B-only factorial reconstruction and metric

    K=Z(I+Dpol)^(-n),
    w_j=(n+m_w+1-b)!/(n+m_w+1-j)!, 0<=j<=b,
    W=diag(w_j^2), G=K^T W K.

Here Dpol differentiates and Z multiplies coefficient polynomials by t-1. Define xi=T^(-1)fP, u=K xi, A=xi^T G xi, lambda=T^(-T)Gxi/A, kappa=u^TWe0/A and c_(n,b,m)=kappa+lambda^TfQ.

For every sufficiently large integer n, T is nonsingular, A>0, and the complete actual center error satisfies

    c_(n,b,m)-(e+pi)
       =(-1)^(n+1)4pi M^(-2n-b)
          [1-(b-1+sigma/8)/n+O_(b,m_w)(n^(-2))]. (1)

Both the leading term and its first correction are independent of m_w in this fixed factorial-weight family. The full inverse-power expansion exists to each fixed order, with later coefficients permitted to depend on m_w. The actual endpoint correction is

    kappa=(-1)^(n+b)
      exp(-sigma)d!/[sigma^d binom(2d,d) n! n^(2b)]
                                      [1+O_(b,m_w)(1/n)]. (2)

The limiting normalized selector coefficients are positive:

    fP_0 lambda_i ->
          binom(d,i)sigma^i/(2+sigma)^d, 0<=i<=d. (3)

Equation (1) gives eventual alternating bracketing and monotonicity on each parity for this exact fixed center. It is not a global denominator theorem or a rationality theorem for e+pi.

## 2. Fixed-size determinant, cofactors and actual metric

Put D=diag((-sigma)^i) and H=(-1)^n DTD^(-1). Its exact symbol remains

    (1+sigma cos t)^n exp(-sigma exp(it)).

The dominant maximum of its modulus is unique at zero, and its absolute tail is exponentially smaller on either parity. The fixed-size Andreief/Gaussian argument gives, for a contiguous r-by-r principal block,

    det H_r=C_r M^(rn)n^(-r^2/2)[1+O_r(1/n)],
    C_r=exp(-r sigma) product_(j=0)^(r-1) j!
           /[2^(r(r+1)/2) pi^(r/2) a^(r^2/2)].   (4)

All Gaussian constants are positive. The index-Vandermonde ratio after deleting index i from 0,...,d is binom(d,i). Thus for v_i=(-1)^i binom(d,i),

    adj H=C_d M^(dn)n^(-d^2/2)
                                [v v^T+O_b(1/n)]. (5)

The ratio

    C_d/C_b=exp(sigma)2^(d+1)sqrt(pi)a^(d+1/2)/d!

is nonzero. Therefore

    T^(-1)=(-1)^n (C_d/C_b)M^(-n)n^(d+1/2)
                                 [r l^T+O_b(1/n)], (6)
    r_i=binom(d,i)sigma^(-i), l_i=binom(d,i)sigma^i.

This handles conditioning before solving. No positivity of the finite complex symbol or inversion of a rank-one limit is used.

The exact forcing-circle formula gives

    fP_0=n!M^n/[2sqrt(pi a n)] [1+O(1/n)],
    fP_i/fP_0 -> Aplus^i, Aplus=1+rho.

The contraction l^T fstar=(2+sigma)^d=(sigma M)^d is positive. Combining with (6),

    xi_i=(-1)^n exp(sigma)(2^d/d!) n!n^d
                                      [r_i+O_b(1/n)], (7)
    xi_d=(-1)^n exp(sigma)sigma^d n!n^d/d!
                                              [1+O_b(1/n)].

For a fixed weight m_w, w_j=n^(j-b)[1+O_(b,m_w)(1/n)]. The column j of W^(1/2)K is O(n^(j-d)) for j<d. Its final column tends, in rows 0,...,b, to

    (0, (-1)^d binom(d,0), (-1)^(d-1)binom(d,1),
                         ..., binom(d,d))^T.

Consequently

    G ->binom(2d,d)e_d e_d^T,
    A=binom(2d,d)exp(2sigma)2^d (n!)^2 n^(2d)/(d!)^2
                                         [1+O_(b,m_w)(1/n)]. (8)

The leading constant is nonzero. This proves (3). The first row of K has final entry
-(-1)^d(n)_d=(-1)^(d+1)n^d[1+O_b(1/n)], where (n)_d is rising factorial. Inserting it and (7)-(8) in kappa=w0^2u0/A proves (2).

## 3. A cofactor insertion formula for the first correction

Let z_l=exp(it_l). Normalize the d-particle complex circle integral with density

    product_l w_n(t_l) product_(p<q)|z_q-z_p|^2.

For each fixed n at which its normalization det H_d is nonzero, write its normalized functional as < . >_n. It need not be a positive measure. Its limiting rescaled Gaussian functional IS positive.

A Vandermonde/elementary-symmetric identity gives the exact cofactor formula

    (adj H)_(d,i)=(-1)^(d+i)det H_d
                                  <e_(d-i)(z_1^(-1),...,z_d^(-1))>_n.
                                                        (9)

To see this, the row index set in this minor is {0,...,d} without i and the column set is {0,...,d-1}. Reverse the inverse-power alternant, factor product z_l^(-d), and use the missing-power Vandermonde identity. Relative to the contiguous d determinant the remaining factor is
e_i(z)/product z=e_(d-i)(z^(-1)). Its cofactor sign is the displayed (-1)^(d+i).

Let k=d-i. Its normalized first correction is

    <e_k(z^(-1))>_n
      =binom(d,k)[1+delta_i/n+O_b(n^(-2))],
    delta_i=-(d-i)(i+1+2sigma)/(4a).               (10)

Here is a direct derivation. In the limiting Gaussian ensemble with density proportional to exp(-a sum x_l^2)Delta(x)^2, put X=sum_l x_l and Y=sum over a chosen subset of k variables. Scaling and translation give

    E[X^2]=d/(2a),
    E[x_l^2]=d/(2a),
    E[x_l x_j]=-1/(2a), l!=j.

Indeed scaling the Gaussian partition function, whose homogeneity is d^2, gives E[sum x_l^2]=d^2/(2a); the Vandermonde is invariant under simultaneous translation, so X has variance d/(2a). Symmetry supplies the stated individual moments. Hence

    E[Y^2]=k(d-k+1)/(2a),
    E[YX]=k/(2a).

The insertion exp(-iY/sqrt(n)) has first odd term -iY/sqrt(n). The actual symbol phase has first odd term -i sigma X/sqrt(n). Their product contributes -sigma E[YX]/n; the insertion's own quadratic term contributes -E[Y^2]/(2n). All common even corrections of the ensemble cancel in the normalized functional because the insertion's leading value is constant. This gives delta_i exactly. Odd terms vanish by simultaneous sign symmetry, and the next relative remainder is O_b(n^(-2)) by fixed-dimensional analytic saddle expansion.

Conjugating (9) by D shows that, up to a common scalar, the highest inverse row has positive coefficients

    a_i(n)=binom(d,i)sigma^i
                        [1+delta_i/n+O_b(n^(-2))]. (11)

This is the only first cofactor perturbation needed.

## 4. First-order cancellation of the actual metric perturbation

After extracting the common cofactor scalar, write Q=Q0+hQ1+O(h^2), Q0=r l^T and h=1/n. Also G=G0+hG1+O(h^2), G0=binom(2d,d)e_d e_d^T. In the exact quotient

    fP_0 lambda =
       Q^T G Q (fP/fP_0) /
       [(fP/fP_0)^T Q^T G Q (fP/fP_0)],

the terms involving G1 cancel at order h because Q0 has the fixed rank-one form r l^T. The remaining first coefficient is precisely that of the highest inverse row normalized by its forcing contraction. Therefore

    fP_0 lambda_i =
       a_i(n)/sum_j a_j(n)(fP_j/fP_0)+O_(b,m_w)(n^(-2)).
                                                        (12)

This is a first-order directional statement, not an exact identification with a coordinate center. It explains why m_w cannot enter the coefficient in (1).

## 5. Complete logarithmic forcing and binomial contraction

The exact all-parity logarithmic identity is

    eF_i=(-1)^(n+1)2n! integral_-pi/4^pi/4
       (sigma cos t-1)^n(1-rho exp(it))^i dt.

Both conjugate endpoints and arc orientation are retained. Put Aminus=1-rho. The forcing ratios have the expansions

    fP_i/fP_0=Aplus^i+f1_i/n+O_b(n^(-2)),
    f1_i=[-i rho Aplus^(i-1)
                  -i(i-1)rho^2 Aplus^(i-2)]/(4a),

    eF_i/eF_0=Aminus^i+g1_i/n+O_b(n^(-2)),
    g1_i=[i rho Aminus^(i-1)
                  -i(i-1)rho^2 Aminus^(i-2)]/(4beta),

with zero terms interpreted directly at i=0. The scalar saddle ratio is

    eF_0/fP_0=(-1)^(n+1)4pi M^(-2n-1)
                             [1-sigma/(8n)+O(n^(-2))]. (13)

The leading normalized contraction of (11)-(12) is

    (1+sigma Aminus)^d/(1+sigma Aplus)^d=M^(-d).

For completeness the first relative coefficient reduces to -d by elementary binomial moments. Let xplus=sigma+1, xminus=sigma-1. For the normalized binomial weights binom(d,i)x^i/(1+x)^d,

    E_x[delta_i]=-[d(d-1)x/(1+x)^2
                       +(1+2sigma)d/(1+x)]/(4a).

The relative forcing corrections average to

    Fplus=-[d/(1+xplus)+d(d-1)/(1+xplus)^2]/(4a),
    Fminus=[d/(1+xminus)-d(d-1)/(1+xminus)^2]/(4beta).

Using 1+xminus=sigma, 1+xplus=sigma M, sigma-1=1/M and beta=aM^2,

    E_xminus[delta]-E_xplus[delta]=-d(1+sigma/4),
    Fminus-Fplus=d sigma/4.

Their sum is exactly -d. Thus

    lambda^T eF=(eF_0/fP_0)M^(-d)
                              [1-d/n+O_(b,m_w)(n^(-2))].

Combining with (13) gives the displayed leading term and first correction in (1).

The retained complete exponential forcing estimate gives
lambda^T eE=O_b(1/(n!sqrt(n))). Equation (2) retains the endpoint. Both are smaller than M^(-2n) times every fixed inverse power of n. Hence the exact full identity
c-(e+pi)=kappa+lambda^T eE+lambda^T eF proves (1). The same fixed-dimensional analytic expansion gives all higher inverse-power coefficients.

## 6. Consequences and scope

Each fixed b gains a factor M^(-1) in the geometric leading constant when b increases by one, while its exponential n-rate remains -2log M. Weight choice m_w does not affect the leading term or first correction. It may affect later terms and the rational denominator.

The rational filter d_n=(c_n+6c_(n+1)+c_(n+2))/8 consequently has

    d_n-(e+pi)=(-1)^n (pi/2)(d+sigma/8)(1-M^(-4))
                     M^(-2n-b)n^(-2)[1+O_(b,m_w)(1/n)].

It retains the exact denominator cost of combining the actual centers. No favorable denominator estimate follows.

There is no growing-b, growing-m_w, uniform threshold, full-coefficient norm, arbitrary-selector, primitive-content, or irrationality conclusion.

## 7. Search and primary-source overlap record

Before starting this extension, archive rg searches included fixed-b signed errors, general Gram errors, Gram/all-parity, the fixed-size metric binomial limit, and general first-order selectors in the October 1 session, September 27 session and sources. The closest exact-center result was the b=3 EVEN-only draft; other fixed-degree error papers and Gaussian Vandermonde bounds supply related methods for different centers or bounds. No matching fixed-b all-parity complete theorem and weight-independent first correction was found by these bounded searches. This is not a global novelty claim.

Current web queries:
- Toeplitz elementary symmetric fixed determinant asymptotic Gaussian
- Hermite-Pade signed asymptotics fixed degree

Primary sources opened:
- [Pan and Prokhorov, fixed-parameter Toeplitz/Painleve asymptotics](https://onlinelibrary.wiley.com/doi/10.1111/sapm.70051). Earlier full article access succeeded; one later line-specific reopen returned an internal error. Related fixed-size Andreief/Vandermonde/saddle methodology, different symbol and objective.
- [Mano and Tsuda, Hermite-Pade approximation, isomonodromic deformation and hypergeometric integral](https://arxiv.org/html/1502.06695). Related Toeplitz/HP determinant structure, not this Gram center or its first correction.

No external theorem identifies this center; equations (4)-(13) provide the specific derivation. Author proof, awaiting independent examination.

