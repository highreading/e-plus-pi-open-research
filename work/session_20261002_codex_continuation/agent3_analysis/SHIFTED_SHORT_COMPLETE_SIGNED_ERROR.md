> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Joint M26: complete analytic theorem for the shifted short rectangular family

Author: Agent 3, 2026-10-02. Root owns the exact primitive interface/cost recurrence. The fresh archive and primary gate is SHIFTED_SHORT_RECTANGULAR_GATE.md. This is the smaller-width shifted family, distinct from M23's scalar multiplier and M25's extra column.

## Precise actual center and conclusions

Let M>=0 be EVEN. Let mu and sigma be the measures from SHORT_RECTANGULAR_COMPLETE_SIGNED_ERROR.md and set

    rho_M=y^M mu-delta_{-1},    sigma_M=y^M sigma.

For 0<=i<k and 0<=j<2k define

    C_(M),ij=D_(2(M+i+j))-(-1)^(i+j),
    R_(M),ij=-(2(M+i+j))!
          +4 sum_(a=1)^(M+i+j) (-1)^(M+i+j-a)/(2a-1),
    V_ij=(-1)^(i+j).

The COMPLETE lower moment block has entries sigma_M(y^(i+j)), and ENTRYWISE it is L_M=eC_M+R_M+S V, S=e+pi. Subtracting e times upper row i from lower row i preserves the stacked determinant exactly, so det[C_M;L_M]=det[C_M;R_M+S V]. This row operation retains the full exponential endpoint; it is not an entrywise replacement of its measure. Write

    Delta_(k,M)=det[C_M;R_M+S V]=a_(k,M)+b_(k,M)S,
    c_(k,M)=-a_(k,M)/b_(k,M).

The right polynomial degree remains <=2k-1 in y; the scalar moment shift is M. All rational exponential and arctangent endpoints are present. Any integer kernel/primitive normalization is Root's exact algebra, not part of this analytic estimate.

**Uniform theorem over ALL even shifts.** For EVERY k>=24 and EVERY even M>=0,

    b_(k,M)!=0,   Delta_(k,M)!=0,
    sign b_(k,M)=sign Delta_(k,M)=(-1)^k,
    0<S-c_(k,M)=Delta_(k,M)/b_(k,M).                    (1)

For every k>=100, uniformly over ALL even M>=0, the complete error obeys

    exp(-4/a) (3/2) Lambda_(k,M-1/2)(-1)
       <=S-c_(k,M)
       <=exp(4/a) ((e+4)/2) Lambda_(k,M-1/2)(-1),       (2)

where a=1/(48e^4) and Lambda is the positive reference Christoffel minimum for y^(M-1/2)dy on [0,1], degree <k, value 1 at -1. Its EXACT normalization is

    Lambda_(k,M-1/2)(-1)
      =1/sum_(j=0)^(k-1)(2j+M+1/2)[P_j^(M-1/2,0)(3)]^2.       (3)

This two-sided comparison controls the full determinant AND actual S-cofactor. Its constants are independent of M and k. It proves complete convergence for every sequence k->infinity with arbitrary even shifts M=M_k>=0, because the reference minimum decreases as M increases.

**Proportional complete error.** Uniformly on each compact range 0<=M/k<=K, with even M and k->infinity,

    log(S-c_(k,M))=-2k F(M/k)+O_K(log k),               (4)

where

    F(kappa)=max_(0<=s<=1){(1+kappa)H_ent(s/(1+kappa))
                            +H_ent(s)+s log2},
    H_ent(s)=-s log s-(1-s)log(1-s),
    s_kappa=2+kappa-sqrt(kappa^2+2kappa+2).

In particular F(0)=2log(1+sqrt(2)) and F'(kappa)>0. The positive shift improves the n-exponential COMPLETE error within the shorter width, rather than adding a formal rational filter.

## 1. Exact insertion formulas with shifted endpoints

For x=(x_1,...,x_k), set

    Q_x(y)=product_i(y-x_i),
    F_(k,M)(x)=det M_[rho_M Q_x,k].

The exact M24 double-Andreief derivation gives

    Delta_(k,M)=(-1)^k/k! integral_[0,1]^k Vandermonde(x)^2
                          F_(k,M)(x) d sigma_M^k,
    b_(k,M)=(-1)^k/(k-1)! integral_[0,1]^(k-1) Vandermonde(x)^2
               product_i(1+x_i)^2 F_(k,M)(x,-1) d sigma_M^(k-1). (5)

The evenness of M ensures the lower rank-one response is exactly V. The insertion at -1 cancels the upper atom, and

    F_(k,M)(x,-1)=det M_[y^M mu·(y+1)product_(i<k)(y-x_i),k].

Nothing in (5) changes the full lower compact measure into the upper tail measure.

## 2. Uniform modified-Gram positivity at k>=24

For k-1 nodes in [-1,1], put Q=product_(i<k)(y-x_i) and nu_M=Q rho_M. The exact unshifted constant is

    C_k=3exp(-2k-1)(k^2-1)^(k-1)/[4k16^(k-1)]>2^k, k>=24.

The proof of this inequality, including its explicit all-index threshold, is Section 2 of SHORT_RECTANGULAR_COMPLETE_SIGNED_ERROR.md. On the tail interval I=[k^2,4k^2], y^M>=(k^2)^M, so its positive contribution to nu_M(p^2) is at least

    (k^2)^M C_k max(|p(-1)|^2,sup_[0,1]|p|^2).

On [0,1], y^M<=1, so its compact negative bound is unchanged. The upper atom is also unchanged for even M. Consequently

    nu_M(p^2)>=[(k^2)^M C_k-2^k] max(...)>0

for EVERY nonzero deg p<k. The same extra factor improves the full k-node positivity estimate. Thus F_(k,M)(x)>0 for all x in [-1,1]^k, every k>=24, and every even M>=0. Equation (5) immediately proves (1).

The argument concerns finite modified moment matrices and does not claim the underlying signed measure is positive or globally quasi-definite.

## 3. Uniform conditional roots and inverse conditioning

Take a=1/(48e^4), A=a k^2 and k>=100. In the unshifted proof, the positive tail of nu_0((y-A)p^2) is at least

    T_0=(k^2-A)C_k L_A(p),
    L_A(p)=max(|p(-1)|^2,sup_[0,A]|p|^2),

whereas the sum of all negative bounds is

    N_0=[A(A+1)^(k-1)+(A+1)2^(k-1)]L_A(p)<T_0.

For the shifted functional, its positive tail is at least (k^2)^M T_0. On the entire negative continuous region [0,A], y^M<=A^M; its atom remains unchanged. Since A>=2, the total negative contribution is therefore bounded by A^M N_0. Hence

    positive/negative >=(k^2/A)^M(T_0/N_0)>1.           (6)

Thus nu_M((y-A)p^2)>0, uniformly over ALL M>=0 even. Together with the positive moment Gram, the multiplication compression has EVERY root greater than a k^2. The characteristic determinant ratio for one variable is

    exp(-4k/A)<=F_(k,M)(x,u)/F_(k,M)(x,-1)<=1,  -1<=u<=1.

Successively replacing all k nodes gives

    exp(-4/a)<=F_(k,M)(x)/F_(k,M)^*<=1,
    F_(k,M)^*=F_(k,M)(-1,...,-1)
              =det M_[y^M mu·(y+1)^k,k]>0,                     (7)

for every x in [-1,1]^k, k>=100, uniformly in M. This is the necessary control of actual determinant/cofactor conditioning; raw tail mass is not used as its substitute.

## 4. Complete reference comparison and proportional rate

The two positive Hankel/insertion integrals for sigma_M, together with (5) and (7), bound the COMPLETE ratio between exp(-4/a) and exp(4/a) times the ordinary sigma_M Christoffel minimum at -1. Since

    (3/2)y^(M-1/2)dy <=d sigma_M(y)
                   <=((e+4)/2)y^(M-1/2)dy,

the variational comparison proves (2). The shifted Jacobi squared norms are 1/(2j+M+1/2), establishing (3) with the exact factor. Both actual components remain in the comparison constants.

For compact 0<=M/k<=K, the exterior values have the positive finite sum

    P_j^(M-1/2,0)(3)
        =sum_(m=0)^j binom(j+M-1/2,m)binom(j,m)2^m.

All terms are positive, including M=0. The values increase with j. Their uniform Stirling maximum-term estimate at j=k-1 is

    log P_(k-1)^(M-1/2,0)(3)=k F(M/k)+O_K(log k).

The unique maximizer satisfies s^2=2(1+kappa-s)(1-s), giving the stated s_kappa. Bounding (3)'s sum by its last term and k times that term proves (4) from (2).

As M increases, y^(M-1/2) decreases pointwise on [0,1], so its positive Christoffel minimum also decreases. Thus (2) additionally proves uniform complete convergence for arbitrary even shift sequences, without imposing a proportional range. Formula (3) retains other M/k regimes exactly; no compact-parameter estimate is promoted to a uniform asymptotic when M/k is unbounded.

For M=o(k), the smooth envelope expansion yields the more explicit sublinear-shift scale

    log(S-c_(k,M))
       =-4k log(1+sqrt(2))-2M log(1+sqrt(2))
          +O(M^2/k+log k).                              (8)

Indeed F'(0)=log(1+sqrt(2)). This is a complete-center rate statement; the effect of the shift on the actual arithmetic cost is not omitted.

## 5. Final primitive interface and distinct scope

Let Q_(k,M) be the final reduced denominator of the actual rational c_(k,M), after all endpoint clearers and evaluated gcd. Equation (4) gives

    log|Q_(k,M)(S-c_(k,M))|
        =log Q_(k,M)-2kF(M/k)+O_K(log k).                (9)

If M/k->kappa and log Q_(k,M)/k->gamma, the primitive form's exponential rate is gamma-2F(kappa). Neither gamma nor favorable content is proved here. Both the degree/shift cost and every actual denominator prime remain Root's arithmetic task.

The scalar M23 construction has a different right degree and a separately owned fixed-k large-M asymptotic. M25 has an extra column and a coefficient lattice; it is not replaced by this width-2k family. No basis change, rationality theorem, or global construction exclusion is inferred.

## 6. Actual odd-shift directional corollary

The proof extends, with an explicit response sign, to EVERY integer M>=0. Define

    rho_M=y^M mu-(-1)^M delta_{-1},
    C_(M),ij=D_(2(M+i+j))-(-1)^(M+i+j),
    V_(M),ij=(-1)^(M+i+j)=(-1)^M V_ij.

The actual lower block is L_M=eC_M+R_M+S V_M, so the same determinant-preserving upper-row subtraction applies. In the S-cofactor identity (5), the inserted lower atom now has coefficient (-1)^M. Thus the exact identities become

    Delta_(k,M)=(-1)^k/k! integral Vandermonde^2 F_(k,M) d sigma_M^k,
    b_(k,M)=(-1)^(k+M)/(k-1)! integral Vandermonde^2
                 product_i(1+x_i)^2 F_(k,M)(x,-1) d sigma_M^(k-1).

All moment coercivity estimates used ABSOLUTE exterior-atom losses, so they remain unchanged. The inserted factor y+1 still annihilates that atom for either parity, and the positive reference F_(k,M)^* is unchanged. Therefore for every k>=24 and every integer M>=0,

    sign Delta_(k,M)=(-1)^k,
    sign b_(k,M)=(-1)^(k+M),
    sign(S-c_(k,M))=(-1)^M.                            (10)

Both determinants are nonzero. The bounds (2)--(4), (8)--(9) hold with ABSOLUTE value of S-c when M is odd, and the error is strictly signed. Thus even shifts converge from below and odd shifts from above, with the same complete exponential scale and actual denominator need. This is a full endpoint/determinant parity statement; it does not import an even-only arithmetic theorem to odd M.
