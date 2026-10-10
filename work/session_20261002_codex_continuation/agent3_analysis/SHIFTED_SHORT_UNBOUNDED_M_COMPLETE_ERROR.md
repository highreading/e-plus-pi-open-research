> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Shifted short rectangular family: complete unbounded-shift crossover

Author theorem: Agent 3 / analysis, 2026-10-02. Gate: SHIFTED_SHORT_LARGE_M_GATE.md. The exact M26 construction and all final denominator arithmetic remain Root's interface. This note extends the preceding complete signed-error theorem; it is original analysis, not a review of finite construction data.

## 1. Actual family and a uniform complete formula

Keep the probability measure mu, the positive compact measure sigma, and the actual blocks from SHIFTED_SHORT_COMPLETE_SIGNED_ERROR.md:

    mu = pushforward of exp(-t)dt, t>=0, under y=(1-t)^2,
    dsigma(y)=g(y)y^(-1/2)dy, 0<y<1,
    g(y)=[exp(sqrt(y))+4/(1+y)]/2,
    rho_M=y^M mu-(-1)^M delta_{-1},  sigma_M=y^M sigma.

The upper block C has k rows and 2k columns, C_ij=rho_M(y^(i+j)). The complete lower block is entrywise L=eC+R+S V_M, S=e+pi, V_M,ij=(-1)^(M+i+j). Subtracting the corresponding eC upper rows is determinant preserving. Write

    Delta_(k,M)=det[C;R+S V_M]=a_(k,M)+b_(k,M)S,
    c_(k,M)=-a_(k,M)/b_(k,M),
    delta_(k,M)=S-c_(k,M).

Both the exponential and arctangent endpoints stay in g throughout. For every integer M>=0 and k>=24, the prior theorem gives nonzero a+bS and b, and

    sign(delta_(k,M))=(-1)^M.                              (1)

Set

    j=k-1,  zeta=M+1/2,  w=M+2j+1/2,
    A_j=2^j Gamma(M+j+1/2)/[Gamma(M+1/2)j!],
    R_j(M)=sum_(l=0)^j (j)_fall,l^2/[2^l l! (zeta)_rise,l],
    r=j/[2(j+M-1/2)],  a*=1/(48e^4),  g1=(e+2)/2.

**Uniform exact-crossover theorem.** If k>=1 and M>=max(100,16k), then BOTH actual determinants are nonzero, the response sign is (1), and

    delta_(k,M)=(-1)^M g1/[w A_j^2 R_j(M)^2] exp(epsilon_(k,M)),       (2)

with the explicit error-log bound

    |epsilon_(k,M)| <=16k/M+4k^2/(a* M^2)+2r^2.                     (3)

In particular (2) is a uniform relative asymptotic as M/k tends to infinity. It permits arbitrary faster growth, including exponential and superpolynomial M, and also EVERY fixed k>=1 with M tending to infinity. Its Gamma quotient and finite positive R_j are exact. No term proportional to log M is discarded in the error bound. This bounded small-k analytic extension does not duplicate Root's M27 arithmetic.

Let Q_(k,M) be the FINAL REDUCED positive denominator of the actual center. Its complete primitive form satisfies

    log|Q_(k,M)delta_(k,M)|
      =log Q_(k,M)+log g1-log w-2log A_j-2log R_j(M)+epsilon_(k,M).   (4)

Equation (4) preserves the actual evaluated gcd and all denominator primes through Q. It does not prove a growth law for Q, favorable content, or irrationality of S.

## 2. Conditional roots at the full M^2 scale

Fix any k-1 nodes x_i in [-1,1], let Q_x(y)=product_i(y-x_i), and nu_M=Q_x rho_M. The preceding all-shift theorem already establishes positive definiteness of its degree-<k moment Gram for k>=24. The present large-M bound also proves this for k=1,...,23 directly, with no finite-index computation. All atom bounds are absolute, so both M parities are covered.

For M>=max(100,k), set A=a* M^2 and I=[M^2,4M^2]. Thus A>=2. For every real polynomial p of degree <k, the elementary exterior Legendre kernel estimate gives

    integral_I p(y)^2dy >=3M^2/[k^2 16^(k-1)] L_A(p),
    L_A(p)=max(|p(-1)|^2,sup_[0,A]|p|^2).                         (5)

The affine images of the test interval stay below absolute value 2, just as in the unshifted proof; the largest exterior image is attained at -1. On I,

    y^M>=M^(2M),  Q_x(y)>=(M^2-1)^(k-1),
    dmu/dy>=exp(-2M-1)/(4M).

Consequently the positive tail in nu_M(p^2) is at least C_(M,k)L_A(p), where

    C_(M,k)=3exp(-2M-1)M^(2M+1)(M^2-1)^(k-1)
                         /[4k^2 16^(k-1)].                    (6)

For EVERY 1<=k<=M and M>=100,

    C_(M,k)/2^k
      =3M/(8e k^2) (M^2/e^2)^M [(M^2-1)/32]^(k-1)
      >1000^M/(8M)>1.

The entire compact-plus-atom loss in nu_M(p^2) is at most 2^k L_A. Thus its Gram is positive definite also for the smaller fixed indices. No archived small-k diagnostic is promoted to a proof.

The positive contribution in nu_M((y-A)p^2) is at least (M^2-A)C_(M,k)L_A. All possible negative continuous contributions lie in [0,A]. The total continuous and exterior-atom loss is at most

    [A^(M+1)(A+1)^(k-1)+(A+1)2^(k-1)]L_A
       <=3A^(M+1)(A+1)^(k-1)L_A.                             (7)

Use M^2-1>=M^2/2 and A+1<=(3/2)a* M^2. The positive-to-negative ratio in (6)--(7) is at least

    (1-a*)M/[4e a* k^2] (48e^2)^M exp(4(k-1))>1.               (8)

The last inequality holds uniformly: k<=M, (1-a*)/(4e a*)>2, and 2·48^M/M>1. Hence nu_M((y-A)p^2)>0 for every nonzero deg p<k.

The symmetric multiplication compression for this EXACT modified functional has all k eigenvalues z_i>A. Equivalently, its characteristic determinant factorization is

    det M_[nu_M(y-u),k]=det M_[nu_M,k] product_(i=1)^k(z_i-u).

This uses finite-dimensional positive Grams only; it does not assume positivity or global quasi-definiteness of rho_M. For -1<=u<=1,

    exp(-4k/A)<=F_(k,M)(x,u)/F_(k,M)(x,-1)<=1.

Replacing all k nodes successively yields

    exp(-4k^2/(a* M^2))<=F_(k,M)(x)/F_(k,M)^*<=1,              (9)
    F_(k,M)^*=det M_[y^M mu·(y+1)^k,k]>0.

The exact double-Andreief determinant and actual S-cofactor identities from the preceding theorem therefore imply

    |log(|delta_(k,M)|/Lambda_(sigma_M,k)(-1))|
                         <=4k^2/(a* M^2).                    (10)

This is complete inverse-normalization control, including the actual affine response; the unsigned tail measure is not substituted for the original determinant.

## 3. The actual compact weight concentrates at its endpoint

Let dgamma_M=y^(M-1/2)dy and a=M-1/2. Since g1=g(1), the elementary bound

    |g(y)-g1|<=g1(1-y), 0<=y<=1,                              (11)

follows from |exp(sqrt(y))-e|<=e(1-sqrt(y)) and the exact rational term. It retains both original endpoints.

The orthonormal shifted Jacobi multiplication matrix for gamma_M has diagonal and off-diagonal entries

    b_l=1/2[1+a^2/((2l+a)(2l+a+2))],
    t_l=l(l+a)/[(2l+a)sqrt((2l+a-1)(2l+a+1))],  l>=1.

These formulas follow from the classical Jacobi leading coefficients, norms, and three-term recurrence. For a>0,

    0<=1-b_l<=(2l+1)/a,  0<t_l<=l/a.

Gershgorin for the k-dimensional compression, or its row-sum norm, gives for EVERY deg p<k

    integral(1-y)p^2 dgamma_M <=(4k/a) integral p^2 dgamma_M
                             <=(8k/M) integral p^2 dgamma_M.  (12)

For M>=16k, (11)--(12) bound the full quadratic forms between g1(1-8k/M)gamma_M and g1(1+8k/M)gamma_M. Taking the true Christoffel minima, with p(-1)=1, yields

    |log(Lambda_(sigma_M,k)/(g1 Lambda_(gamma_M,k)))|<=16k/M.  (13)

No assumption about concentration of only the minimizer is needed; the estimate is uniform over the entire polynomial space.

## 4. Exact exterior Jacobi crossover and last-term domination

The exact reference minimum is

    Lambda_(gamma_M,k)(-1)
      =1/sum_(l=0)^j (2l+M+1/2)[P_l^(M-1/2,0)(3)]^2.          (14)

The positive binomial expansion is

    P_j^(a,0)(3)=sum_(m=0)^j binom(j+a,m)binom(j,m)2^m.

The m=j term is A_j. With l=j-m, the remaining exact coefficient ratio proves

    P_j^(M-1/2,0)(3)=A_j R_j(M).                              (15)

For j>=1, compare term m+1 at degree j to term m at degree j-1. Their ratio is 2j(j+a)/(m+1)^2>=2(j+a)/j. Thus

    P_(j-1)^(a,0)(3)/P_j^(a,0)(3)<=r=j/[2(j+a)].

The corresponding ratios at smaller degrees are no greater than r, and their norm weights are smaller. Consequently

    (1-r^2)/[w P_j(3)^2]<=Lambda_(gamma_M,k)(-1)
                                      <=1/[w P_j(3)^2].       (16)

For the stated range, r^2<1/2, so the logarithmic correction in (16) is at most 2r^2. Combining (10), (13), (15), and (16) proves (2)--(3).

## 5. Poisson remainder, a uniform logarithmic rate, and the k^2 crossover

For j>=1, define lambda=j^2/(2zeta). The exact finite remainder has the form

    R_j=sum_(l=0)^j lambda^l/l! product_(r=0)^(l-1)
                                   [(1-r/j)^2/(1+r/zeta)].      (17)

Thus 1<=R_j<=exp(lambda). For lambda>=1, retain the term l=floor(lambda). In the range M>=16k, l<=j/32. The elementary inequalities log(1-z)>=-2z for 0<=z<=1/2 and log(1+z)<=z give

    log(product)>=-(2/j+1/(2zeta))l(l-1).

Stirling's elementary upper factorial bound then proves, also trivially when lambda<1,

    0<=lambda-log R_j
       <=2+(1/2)log(j+1)+j^3/M^2.                             (18)

The exact Gamma quotient in A_j is a product of j factors M+1/2+r. Therefore

    log A_j=j log(2M)-log(j!)+j^2/(2M)+O(j^3/M^2),
    lambda=j^2/(2M)+O(j^2/M^2).

With (2)--(3) and (18), this gives the uniform logarithmic formula

    log|delta_(k,M)|
      =log(e+2)+2log(j!)-(2j+1)log(2M)-2j^2/M
           +O(j^3/M^2+log(k+1)+k/M),                         (19)

for all k>=1, M>=max(100,16k), with an ABSOLUTE implicit constant. In particular the exact exponent 2j+1=2k-1 is retained even if log M vastly exceeds log k. For the primitive form, add log Q_(k,M) to the right side of (19). At j=0, the leading factor A_j and remainder R_j are both exactly 1, and the same conclusion follows immediately from (2)--(3) without using (17).

A sharper relative formula follows without Stirling loss. For every l, extend the product in (17) by zero when l>j. The elementary product inequality bounds it below by

    1-(1/j+1/(2zeta))l(l-1).

This lower bound is nonpositive when l>j and is valid there too. Taking a Poisson(lambda) expectation proves

    exp(lambda)[1-xi]<=R_j<=exp(lambda),
    xi=(1/j+1/(2zeta))lambda^2=O(j^3/M^2).                      (20)

Hence if M/k^(3/2) tends to infinity (including ANY fixed k>=1, M tending to infinity),

    delta_(k,M)=(-1)^M (e+2)(j!)^2/(2M)^(2j+1)
                    exp(-2j^2/M)[1+O(k/M+k^3/M^2)].           (21)

The constant is absolute and the error tends to zero. In particular:

- If M/k^2 tends to c in (0,infinity), the correction to the elementary endpoint-power scale tends to exp(-2/c).
- If M/k^2 tends to infinity, that correction tends to one, uniformly even for exponential or superpolynomial shifts.
- Between M/k tending to infinity and M/k^(3/2) tending to infinity, the exact finite formula (2), with (3), is still a uniform relative asymptotic; (19) additionally gives its explicit logarithmic expansion.

## 6. Scope and attribution

The previous compact-parameter theorem and (2) together cover bounded and unbounded M/k. The endpoint constant and the M^2 conditional-root bound are specific to the full short-family determinant interface. The positive binomial identity, Jacobi recurrence, and positive Christoffel interpretation are classical; the gate records their primary-literature overlap and the limited scope of the cited large-parameter expansion.

Bounded reproducibility check: shifted_short_unbounded_jacobi_checks.py writes SHIFTED_SHORT_UNBOUNDED_JACOBI_RECEIPT.json. Its 21 exact finite Jacobi expansion/norm/recurrence cases and 16 finite Poisson-remainder cases passed. These are algebraic diagnostics, not a substitute for the all-index inequalities above; they do not inspect actual Q or replay old construction receipts.

For every fixed k>=1, (21) in particular gives

    delta_(k,M)~(-1)^M (e+2)((k-1)!)^2/[2^(2k-1)M^(2k-1)].

The earlier M23 scalar construction has a different right polynomial degree; equality of this endpoint constant is not equality of its actual center or denominator. Root's M27 k=1 actual Möbius extraction and factorial-denominator lower bound remain separate. This note proves no actual Q growth, no general fixed-prime survival law, and no global obstruction. Equations (4) and (19)--(21), multiplied by the final reduced Q, are the complete analytic quantities any arithmetic argument must use.
