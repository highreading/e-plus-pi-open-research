> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Growing shifted paired determinants: coercivity and complete signed error

Author theorem: Agent 3, 2026-10-02. The separate new-target archive and primary gate is GROWING_SHIFTED_DERANGEMENT_GATE.md. Root's M23 fixed-degree Gamma/Hermite limit is acknowledged prior work; the results below are uniform growing-degree statements. Root owns the integer normalization and final evaluated content. This is original mathematics, not an audit.

## Exact construction and main conclusions

Let mu be the probability pushforward of exp(-t)dt, t>=0, under y=(1-t)^2, so mu(y^r)=D_{2r}. Let M be a positive EVEN integer and set

    rho_M(f)=integral y^M f(y)dmu(y)-f(-1).

Take n=2k-1, k>=1. Whenever its degree-n moment prefix is nonsingular, let q=q_(n,M) be the monic polynomial satisfying rho_M(y^j q)=0 for 0<=j<n. A positive rational/integer scalar multiple does not alter any center below.

The ACTUAL scalar weight is x^(2M)q(x^2). Define

    H_ij=integral_0^1 x^(2M+2i+2j)q(x^2)[exp(x)+4/(1+x^2)]dx,
    lambda=q(-1),  v_i=(-1)^i, 0<=i,j<k.

The shifted orthogonality gives equal exponential and arctangent coefficients for every entry:

    H=R+S lambda vv^T,   S=e+pi,   R rational.

For its exact affine determinant det(R+s lambda vv^T)=a+b s, let c=-a/b. The theorem establishes b!=0 and c<S in the ranges below, retaining both integrals and all rational endpoint terms.

**Uniform square-root shift range.** If

    M>=24,   n<=M^2/4,   M even,                         (A)

then q exists uniquely and EVERY one of its n roots is real, simple, and greater than 1. The actual normalized matrix J=H/lambda is positive definite. In particular,

    0<S-c=1/[v^T J^(-1)v]
          <= (e+4)/[(2M+1)T_(k-1)(3)^2]
          <= 4(e+4)/(2M+1) (1+sqrt(2))^(-4k+4).          (B)

The expression is the FULL signed error of the actual rational center. Thus growing k with, for example, the least even M>=max(24,2sqrt(2k-1)) gives complete convergence with a strictly nonzero error at every index. No primitive denominator size is asserted.

**Proportional shift rate.** Uniformly for M/k in any fixed compact subinterval of (0,infinity), with even M and k tending to infinity,

    log(S-c)=-2k F(M/k)+O(log k),                        (C)

where, writing H_ent(s)=-s log s-(1-s)log(1-s),

    F(kappa)=max_{0<=s<=1} [(1+kappa)H_ent(s/(1+kappa))
                           +H_ent(s)+s log 2],
    s_kappa=2+kappa-sqrt(kappa^2+2kappa+2).

This is a two-sided logarithmic scale result for the complete positive error, not an upper bound alone. The rate is strictly increasing in kappa. At kappa=0 its continuous extension is F(0)=log(3+2sqrt(2))=2log(1+sqrt(2)); for positive kappa it improves that reference exponent.

## 1. Tail coercivity at growing degree

The tail t>=1, with u=t-1 and y=u^2, has shifted density

    d(y^M mu)_tail=exp(-1)u^(2M)exp(-u)du
                 =exp(-1)u^(2M-1)exp(-u)dy/2.

For M>=24 put U=2M-1 and I=[16,U^2]. The density as a function of u is increasing on [4,U], so on I it is at least

    w_min=exp(-5)4^(2M-1)/2.

For a polynomial p of degree <n, the Legendre evaluation kernel on I gives, simultaneously for y_0=-1 and all y_0 in [0,1],

    |p(y_0)|^2 <= n^2 Phi^(2n-2)/|I| integral_I p(y)^2dy,
    log Phi=2 asinh sqrt(17/|I|).

Indeed the affine map to [-1,1] has maximum exterior absolute value at y_0=-1, equal to (U^2+18)/(U^2-16). The standard integral representation gives |P_j(z)|<=Phi^j for real |z|>=1; the sum of 2j+1 is n^2. The same estimate is valid inside the interval. No Gram or scalar polynomial has been substituted here.

Consequently, with L(p)=max(|p(-1)|^2,sup_[0,1]|p|^2),

    integral_I y^M p^2 dmu >= C_(M,n) L(p),
    C_(M,n)=w_min |I|/[n^2 Phi^(2n-2)].                 (1)

For M>=12, |I|=4M^2-4M-15>=(57/16)M^2. Under n<=M^2/4,

    C_(M,n) >= 57/(8e^5 M^2)
               exp[M(2log4-4sqrt(17/57))]
             > exp(7M/15)/(35M^2)>1  (M>=24).          (2)

The elementary estimates are log4>4/3, sqrt(17/57)<11/20, and e<3. The last function is increasing for M>=24; at M=24 it exceeds 1 because exp(11)>(8/3)^11>35*24^2. These inequalities provide an explicit all-degree threshold rather than a fixed-degree limit.

Since the remaining shifted measure is nonnegative,

    rho_M(p^2)>=(C_(M,n)-1)L(p)>0.                     (3)

For the multiplication shift, the exterior atom contributes +2p(-1)^2. Its only negative continuous part is 0<=y<1, whose absolute contribution is at most L(p), because mu has mass 1 and y^M(1-y)<=1 there. The tail I contributes at least 15C_(M,n)L(p). Thus

    rho_M((y-1)p^2)>=(15C_(M,n)-1)L(p)>0.              (4)

These statements hold for EVERY nonzero polynomial deg p<n.

## 2. Root placement and the actual determinant sign

The degree-n moment matrix for rho_M is positive definite by (3); hence q exists uniquely. The compression of multiplication by y to degrees <n is a real symmetric matrix in its orthonormal basis. Its characteristic polynomial is q, by the finite three-term recurrence. The positive consecutive norms make its off-diagonal entries nonzero, so its eigenvalues are simple. Equation (4) makes this matrix minus the identity positive definite. Therefore every root z_j of q is greater than 1.

For n odd, lambda=q(-1)<0, and on 0<=y<=1

    0<q(y)/lambda=product_{j=1}^n (z_j-y)/(z_j+1)<=1.  (5)

After the change y=x^2, the ACTUAL normalized matrix is the positive Gram matrix for

    dnu_(n,M)(y)=y^M[q(y)/lambda]
                  [exp(sqrt(y))+4/(1+y)]dy/[2sqrt(y)].

In particular J is positive definite. Rank-one differentiation of det H gives

    b=lambda^k det(J)[v^T J^(-1)v],
    det H=lambda^k det(J).

Both have sign (-1)^k. Their quotient is positive and yields exactly

    S-c=1/[v^T J^(-1)v]
       =min_{deg p<k,p(-1)=1} integral p(y)^2 dnu_(n,M)(y).   (6)

Thus determinant/cofactor nonvanishing and the complete sign are established for the actual endpoints. There is no use of an oscillatory or unsigned replacement ensemble.

Testing p(y)=T_(k-1)(2y-1)/T_(k-1)(-3), and using (5), gives

    S-c <= 1/T_(k-1)(3)^2
            integral_0^1 x^(2M)[exp(x)+4/(1+x^2)]dx
          <= (e+4)/[(2M+1)T_(k-1)(3)^2].

The closed Chebyshev formula gives (B). The constant e+4 is deliberately a uniform bound for the COMPLETE mixed weight, not an asymptotic endpoint constant.

## 3. Scalar flattening uniformly when n/M is bounded

A second tail estimate places every scalar root a distance of order M^2 from the compact interval. Fix B>0 and assume n<=BM. On I_1=[M^2,4M^2], M>=2, the tail density is at least exp(-1)M^(2M-1)exp(-2M)/2. For y_0=-1 or any y_0 in [0,M^2], the Legendre evaluation bound has Phi<4. Therefore

    integral_(I_1) y^M p^2 dmu >= C_1 max(|p(-1)|^2,sup_[0,A]|p|^2),
    C_1=3 M^(2M+1)exp(-2M)/[2e n^2 16^(n-1)],

for any A<M^2. Define

    a_B=exp(-4)16^(-B),    A=a_B M^2.

The negative continuous contribution to rho_M((y-A)p^2) is at most A^(M+1)sup_[0,A]|p|^2, while its exterior atom contributes +(1+A)p(-1)^2. Its positive I_1 contribution is at least (M^2-A)C_1 times the same supremum. Their ratio satisfies

    (M^2-A)C_1/A^(M+1)
        >= 3(1-a_B) exp(2M)/[2e a_B B^2 M] -> infinity.   (7)

Here -2-log(a_B)-B log16=2; omitting the extra factor 16 weakens the bound. Hence, uniformly for n<=BM and sufficiently large M depending only on B, rho_M((y-A)p^2)>0 and every root z_j>A. The moment positivity already follows from (A) for these large parameters.

Equation (5) now gives the UNIFORM scalar estimate

    exp[-4n/(a_B M^2)] <= q(y)/q(-1) <=1,  0<=y<=1,   (8)

once A>=3. In particular q(y)/q(-1)=1+O_B(1/M) when n<=BM. This growing-degree flattening uses coercivity rather than Root's fixed-degree Hermite limit.

## 4. Jacobi comparison and complete proportional rate

Put a=M-1/2 and let Lambda_(k,a)(-1) be the Christoffel minimum for the positive reference measure y^a dy on [0,1], with deg p<k and p(-1)=1. Since

    3 <= exp(sqrt(y))+4/(1+y) <=e+4,

the variational identity and (8) give

    (3/2)exp[-4n/(a_B M^2)] Lambda_(k,a)(-1)
       <= S-c <= ((e+4)/2) Lambda_(k,a)(-1).            (9)

This is a TWO-SIDED estimate for the COMPLETE actual center. The exponential and arctangent pieces have remained together throughout.

The shifted Jacobi polynomial P_j^(0,a)(2y-1) has squared norm 1/(2j+a+1) under y^a dy. Its exterior value is (-1)^j P_j^(a,0)(3), and the latter is the positive finite sum

    P_j^(a,0)(3)=sum_{m=0}^j binom(j+a,m)binom(j,m)2^m. (10)

Consequently

    Lambda_(k,a)(-1)=1/sum_{j=0}^{k-1}(2j+a+1)[P_j^(a,0)(3)]^2.

For a>=0 the exterior values increase with j, as follows termwise from (10). With j=k-1 this gives

    1/[k(2k+a+1)P_(k-1)^(a,0)(3)^2]
       <=Lambda_(k,a)(-1)
       <=1/[(2k+a-1)P_(k-1)^(a,0)(3)^2].              (11)

Uniform Stirling bounds in the positive sum (10), using its largest term for the lower bound and k times that term for the upper bound, give

    log P_(k-1)^(M-1/2,0)(3)=k F(M/k)+O(log k)

uniformly on compact positive ranges of M/k. The half-integer and k-1 shifts change this by O(log k). The unique maximizing term fraction solves

    s^2=2(1+kappa-s)(1-s),

which gives s_kappa stated above. Equations (9)--(11) prove (C). This direct positive-sum argument needs no import of the interior oscillatory Jacobi regime in Szehr--Zarouf.

The envelope derivative is

    F'(kappa)=log[(1+kappa)/(1+kappa-s_kappa)]>0.

The continuous endpoint F(0)=log(3+2sqrt(2)) follows either from the saddle or the Legendre exterior value. Thus this mechanism improves the n-exponential complete error rate when M is proportional to k; it does not merely multiply a formal correction filter.

## 5. Exact primitive-denominator need and scope

Let Q_(k,M) be the FINAL REDUCED denominator of the actual rational c=-a/b, after every rational clearer and gcd. All the analytic results are invariant under positive scalar normalization of q. Their primitive complete form is exactly

    Q_(k,M)(S-c).

For M/k in a compact positive range, (C) gives

    log|Q_(k,M)(S-c)|=log Q_(k,M)-2kF(M/k)+O(log k).     (12)

If M/k->kappa and log Q_(k,M)/k->gamma, this primitive form has exponential rate gamma-2F(kappa). A strictly smaller gamma would make it tend to zero, while a strictly larger gamma would make it diverge. Equality needs finer information. No estimate for gamma, favorable common content, or distribution of denominator primes is proved here.

In particular scalar projection normality, raw Gamma mass, positive determinant sign, and complete center convergence are not a proof about the rationality of e+pi. Root's fixed-k, M->infinity asymptotic remains a different regime; it is neither assumed uniform nor re-proved as this theorem.
