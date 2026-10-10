> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# M31 growing pole order: uniform coercivity and complete root-error product

Author: Agent 3 / analysis, 2026-10-02. Original analytic theorem, not an audit. Fresh archive and primary-literature gate: GROWING_POLE_ORDER_SHORT_GATE.md. Root supplies and owns the exact normalized arctangent response, finite rectangular rank, actual rational moment/clearer formulas, primitive polynomial content, and arithmetic transfer. The classical modified-Hankel and confluent characteristic identities are credited to the primary papers in that gate. The present uniform tail comparison and complete growing-order product estimates are the analytic contribution.

## 1. Actual full determinant and quantified theorem

Let mu be the probability pushforward of exp(-t)dt, t>=0, under y=(1-t)^2. Fix integers m>=1 and k>=m. Put d=m-1 and use Root's exact response

    c_m=4^m/binom(2m-2,m-1),
    nu_m(y^r)=(-1)^r (1/2-r)_d/(1/2)_d,
    rho_m=mu-nu_m,
    dsigma_m(y)=[exp(sqrt(y))+c_m/(1+y)^m]dy/[2sqrt(y)].

Rising factorials are denoted by (a)_d. Root's jet identity, used with attribution, is

    nu_m(f)=sum_(j=0)^d a_j f^(j)(-1),
    a_j=2^j binom(d,j)(2(d-j)-1)!!/(2d-1)!!,
    1/j! <= a_j <= 2^j/j!,   a_d=1/(1/2)_d.                 (1)

The double factorial (-1)!! is 1. In particular all terms of the actual jet functional are retained.

For 0<=i<k and 0<=j<2k, write C_ij=rho_m(y^(i+j)) and V_ij=nu_m(y^(i+j)). Root's exact moment interface gives

    L_ij=sigma_m(y^(i+j))=e C_ij+R_ij+S V_ij,
    S=e+pi,
    beta_(k,m)(s)=det[C;R+sV].                              (2)

Subtracting e times the upper rows proves beta(S)=det[C;L]. The polynomial expanded at S is the full stack with lower functional sigma_m+(s-S)nu_m. This row operation does not omit the eC term from the actual moments.

Set

    a=1/(48e^4),   k0=131072,   L0=exp(-4/a),
    kappa_m=[(m-1)!/(1/2)_(m-1)]^m.                         (3)

For EVERY k>=k0 and EVERY 1<=m<=k:

* beta has degree EXACTLY m; its value at S has sign (-1)^k and is strictly nonzero.
* Its leading coefficient beta_m has sign (-1)^[k+binom(m,2)] and is strictly nonzero.
* If s_1,...,s_m are ALL complex roots with multiplicity, the complete signed product has sign (-1)^binom(m,2), and its modulus is controlled by the ACTUAL compact m-jet inverse Gram determinant K_(sigma_m,k,m):

        L0/[kappa_m det K] <= |product_j(S-s_j)|
                                    <=1/[L0 kappa_m det K]. (4)

* The growth estimate is uniform throughout the full range 1<=m<=k:

        log|product_j(S-s_j)|
          =-4km log(1+sqrt(2))
                        +O(m^2+m log(k+1)+m log(m+1)).      (5)

Every implied constant in (5) is absolute, independent of both k and m. An explicit one-sided bound stronger than an unspecified error term is given in (24) below. In particular the geometric mean of the m root-error moduli is at most exp(-k/4) throughout this range. At least one complex root lies within that distance of S. The product estimate does NOT assert that every root is real or that every individual root converges to S.

For m=o(k), formula (5) gives the uniform geometric-mean rate

        (1/m)sum_j log|S-s_j|
                  =-4k log(1+sqrt(2))+O(m+log(k+1)).        (6)

The exact multiplier kappa_m and the actual final primitive leading coefficient are retained in Sections 4 and 7. No denominator-height estimate or irrationality conclusion is inferred from a small root-error product.

## 2. Uniform conditional Gram positivity with ALL jet terms

Fix ANY k-1 real nodes x_i in [-1,1], allowing coincidences, and put Q(y)=product_i(y-x_i), eta=Q rho_m. Let p be a nonzero real polynomial of degree <k. Define

    A=ak^2,  I=[k^2,4k^2],  L_A=sup_[-1,A]|p|^2,
    C_k=3exp(-2k-1)(k^2-1)^(k-1)/[4k16^(k-1)].

For k>=k0, A>=2. The rescaled Legendre evaluation bound on I is

    integral_I p(y)^2 dy >=3·16^(-(k-1)) L_A.                (7)

To verify its normalization, map I to [-1,1]. Every target y in [-1,A] maps to absolute coordinate at most 2. The degree-l Legendre value has modulus <4^l there. The reproducing sum is at most k^2 16^(k-1)/(3k^2), proving (7).

The mu tail density is at least exp(-2k-1)/(4k) on I, and Q(y)>=(k^2-1)^(k-1) there. Consequently the positive tail of mu(Qp^2) is at least C_k L_A.

The continuous negative contribution comes only from y in [0,1]; its absolute value is at most (A+1)^(k-1)L_A, since mu has mass 1. For the COMPLETE jet contribution apply repeated supremum Markov inequality on [-1,A] to h=Qp^2, whose degree is at most 3k. It gives

    ||h^(j)|| <=[2(3k)^2/(A+1)]^j ||h||,
    |nu_m(h)| <=exp[36k^2/(A+1)] ||h||
                  <=E(A+1)^(k-1)L_A,  E=exp(36/a).         (8)

Equation (8) sums every actual coefficient in (1). Derivatives beyond the degree vanish. There is no factor exponential in m: the positive jet coefficients are bounded by an exponential generating series, rather than by a fixed-m constant.

The total possibly negative contribution is at most 2E(A+1)^(k-1)L_A. Elementary estimates k^2-1>=k^2/2 and A+1<=3ak^2/2 give

    C_k/(A+1)^(k-1) >=3exp(2k-4)/(4ek).                    (9)

For k>=k0, using e<3,

    36/a=1728e^4<139968,
    2k-4-36/a>k/2,
    3exp(2k-4-36/a)/(8ek)>exp(k/2)/(8k)>1.

Thus eta(p^2)>0 for every nonzero deg p<k, uniformly in all node configurations and in ALL m. The exact conditional Gram is positive definite.

## 3. Conditional roots above ak^2; complete characteristic comparison

Apply the same estimate to h=(y-A)Qp^2, whose degree is at most 3k. Its supremum is at most (A+1)^k L_A. The continuous negative part on [0,A] is at most A(A+1)^(k-1)L_A. The full jet loss is at most E(A+1)^k L_A. Their sum is at most 3AE(A+1)^(k-1)L_A.

The positive tail is at least (k^2-A)C_k L_A. By (9), its ratio to this negative bound is at least

    (1-a)exp(2k-4-36/a)/(4eak)>1,  k>=k0.                 (10)

Therefore eta((y-A)p^2)>0. The exact symmetric multiplication compression in the positive k-dimensional eta Gram has ALL eigenvalues z_i>A. They are the roots of the conditional degree-k orthogonal polynomial. This argument handles the indefinite endpoint jet directly; it does not replace it by a positive derivative-mass ensemble.

For k nodes x define

    F_(k,m)(x)=det M_[rho_m product_i(y-x_i),k].

The finite characteristic identity for the final node u is

    F(x_1,...,x_(k-1),u)=det M_(eta,k) product_i(z_i-u).

It follows that F(x)>0 on [-1,1]^k. Comparing any u in [-1,1] with -1 gives

    exp(-4k/A)<=F(x,u)/F(x,-1)<=1.

Because k>=m, product_i(y+1)=(y+1)^k annihilates the ENTIRE upper jet. Thus

    F*=F(-1,...,-1)=det M_[mu(y+1)^k,k]>0,
    L0<=F(x)/F*<=1,  x in [-1,1]^k.                        (11)

The lower constant in (11) is uniform in both m and k. Each actual coordinate of the complete jet has been included before this comparison.

## 4. Full value and exact highest confluent coefficient

Finite Andreief identities applied to (2) give

    beta(S)=(-1)^k/k! integral_[0,1]^k
                        Vand(x)^2 F(x) d sigma_m^k.        (12)

The integrand is strictly positive on distinct nodes, proving its sign and nonzero value.

To retain EVERY coefficient, write b_l=[t^l]beta(S+t). Its complete finite formula is

    b_l=(-1)^k/[l!(k-l)!] integral_[0,1]^(k-l) Vand(x)^2
       ·(nu_m)_(u_1)...(nu_m)_(u_l)
         {Vand(u)^2 product_(a,i)(u_a-x_i)^2 F(x,u)}
                                             d sigma_m^(k-l). (12a)

Each functional in (12a) includes the entire sum (1). No middle coefficient is assigned a positivity sign. For l>m, Vand(u)^2 vanishes at the common point -1 to total order l(l-1), which is greater than the available total derivative order l(m-1); thus b_l=0. This also proves degree(beta)<=m directly from the exact coefficient formula.

For the highest coefficient insert m lower variables u_1,...,u_m in (12a). The integrand contains Vand(u)^2, which vanishes at their common point -1 to total order m(m-1). Each variable permits derivative order at most d=m-1. Consequently ONLY the highest derivative d in every nu_m survives, and all of these derivatives must fall on Vand(u)^2. No derivative of another factor contributes to this highest coefficient.

The coefficient of product_i(u_i+1)^d in Vand(u)^2 is (-1)^binom(m,2)m!, the standard confluent Vandermonde coefficient. Therefore the full derivative factor is (-1)^binom(m,2)m!(d!)^m a_d^m. Including the exact expansion factor 1/[m!(k-m)!] gives

    beta_m=(-1)^[k+binom(m,2)] kappa_m/(k-m)!
       ·integral_[0,1]^(k-m) Vand(x)^2
                 product_i(1+x_i)^(2m) F(x,(-1)^m)
                                         d sigma_m^(k-m).  (13)

Here F(x,(-1)^m)=det M_[mu(y+1)^m product_i(y-x_i),k], because the m-fold insertion kills every upper jet derivative. Its positive value follows also from (11). Thus beta_m is nonzero, and beta has degree EXACTLY m. For m=k the compact integral has zero variables and equals F*.

The exact multiplier is

    kappa_m=[4^(m-1)/binom(2m-2,m-1)]^m,
    1<=kappa_m<=(2m-1)^m,
    log kappa_m=(m/2)log m+O(m).                            (14)

The last bound follows from the elementary central-binomial estimates; the exact expression is used throughout. This is a genuine growing-order factor, not an ignored fixed-m normalization.

## 5. Full jet inverse conditioning via an exact successive-value identity

For ANY positive compact measure w, let G_(w,k) be the monomial moment Gram for degrees <k and let V be the k-by-m normalized Taylor-jet evaluation matrix

    V_(i,j)=binom(i,j)(-1)^(i-j),  0<=j<m, 0<=i<k.

Thus V^T gives derivatives divided by j!. Put K_(w,k,m)=V^T G_(w,k)^(-1)V. The positive characteristic-product identity is

    det G_(w,k) det K_(w,k,m)
       =det G_[w(y+1)^(2m),k-m]
       =1/(k-m)! integral Vand(x)^2
                         product_i(1+x_i)^(2m) dw^(k-m).   (15)

Its normalization is fixed by the Taylor factorials: for m=k the square matrix V has determinant 1, and both sides equal 1. Equation (15) is classical confluent modified-Hankel algebra; it is not a positivity claim about rho_m.

Let K_(w,n)(-1) denote the ordinary VALUE kernel for degrees <n. Telescoping (15) through consecutive single insertions yields the EXACT factorization

    det K_(w,k,m)
            =product_(r=0)^(m-1) K_[w(y+1)^(2r),k-r](-1).  (16)

This avoids an unproved growing-order exterior Wronskian estimate. For dgamma=y^(-1/2)dy on [0,1], the elementary bounds 1<=(1+y)^(2r)<=4^r give

    4^[-m(m-1)/2] product_(r=0)^(m-1) K_(gamma,k-r)(-1)
       <=det K_(gamma,k,m)
       <=product_(r=0)^(m-1) K_(gamma,k-r)(-1).             (17)

The ACTUAL compact measure obeys

    (1/2)dgamma<=dsigma_m<=6m dgamma.                       (18)

Indeed c_m<=4(2m-1)<=8m, e<3, and exp(sqrt(y))>=1. Inverse-Gram Loewner comparison on the full m-channel evaluation matrix therefore gives

    (6m)^(-m) det K_(gamma,k,m)
       <=det K_(sigma_m,k,m)<=2^m det K_(gamma,k,m).        (19)

Every conditioning loss in (17)--(19) is explicit for growing m.

## 6. Quantified complete product scale throughout 1<=m<=k

Set lambda=3+2sqrt(2) and ell=log(1+sqrt(2)), so log lambda=2ell. The exact reference value kernel is

    K_(gamma,n)(-1)=sum_(l=0)^(n-1)
                       (2l+1/2)[P_l^(-1/2,0)(3)]^2.

For every l, the positive binomial sum is between P_l(3)/(2l+1) and P_l(3), where P_l is the ordinary Legendre polynomial. This follows by comparing binom(l-1/2,j)/binom(l,j): it decreases with j, and its minimum binom(l-1/2,l)=binom(2l,l)/4^l is at least 1/(2l+1).

The elementary Legendre integral representation gives

    lambda^l/[2pi sqrt(l+1)]<=P_l(3)<=lambda^l.

For the lower bound integrate only 0<=theta<=1/sqrt(l+1), use cos(theta)>=1-theta^2/2 and Bernoulli's inequality. Summing the upper estimate and keeping the final term for the lower estimate proves the deliberately coarse but uniform bounds

    lambda^(2n)/[32pi^2 lambda^2 n^2]
             <=K_(gamma,n)(-1)<=n^2 lambda^(2n).            (20)

Define C0=log(32pi^2 lambda^2) and

    T=mk-m(m-1)/2=sum_(r=0)^(m-1)(k-r).

Combining (17)--(20) yields the EXPLICIT bounds

    4ell T -m(m-1)log2 -2m log k -C0 m -m log(6m)
         <=log det K_(sigma_m,k,m)
         <=4ell T +2m log k +m log2.                       (21)

Meanwhile (11)--(15) prove the complete product formula

    sum_j log|S-s_j|=-log kappa_m
                     -log det K_(sigma_m,k,m)+epsilon,
    |epsilon|<=4/a.                                        (22)

In particular its uniform one-sided upper bound is

    (1/m)sum_j log|S-s_j|
       <=-4ell k +(2ell+log2)(m-1)+2log k+log(6m)+C0
                                   +4/(am)-(log kappa_m)/m. (23)

Together with the other side of (21), equation (22) proves (5). For m=o(k) it proves (6), with no hidden m-dependent error constant.

For completeness, even the ENTIRE linear range admits a positive geometric-mean exponent. As m<=k and kappa_m>=1, (23) gives

    (1/m)sum_j log|S-s_j|
       <=-(2ell-log2)k+3log k+C0+log6+4/a.                 (24)

Here 2ell-log2=log[(3+2sqrt(2))/2]>log2>1/2. The rough inequalities e<3, pi<4, lambda<6 imply 4/a<15552, C0<15, log6<3. Since log k<=sqrt(k), the remaining positive terms are less than k/4 for k>=131072: at that endpoint 15570+3sqrt(k)<k/4, and the difference increases thereafter. Thus (24) is at most -k/4. This proves the announced bound exp(-k/4) for the geometric mean throughout 1<=m<=k, without claiming each individual error has that bound.

The SIGNED product is exactly beta(S)/beta_m; hence its sign is (-1)^binom(m,2). Complex roots occur in conjugate pairs because beta has rational real coefficients. This sign and the complete modulus formula do not impose real-rootedness for m>2.

## 7. Actual primitive polynomial interface and scope

Let Pi_(k,m)(s)=A_0+...+A_m s^m be Root's FINAL primitive integer polynomial proportional to beta, with every rational clearer and final common content included. Then A_m!=0, Pi(S)!=0, and the COMPLETE formula is

    log|Pi(S)|=log|A_m|-log kappa_m
                      -log det K_(sigma_m,k,m)+epsilon,
    |epsilon|<=4/a.                                        (25)

Its exact uniform bounds follow by adding log|A_m|-log kappa_m to the negative of (21). Its coefficient height H(Pi) remains the actual arithmetic quantity. The analysis does not establish H comparable to |A_m| for growing m, because the root product does not control every individual root. In particular (25) may not replace |A_m| by a conjectural raw-height scale or drop primitive common content.

The result supplies a genuine quantified growing-order range, indeed all 1<=m<=k at an explicit threshold. It proves conditional positivity, the complete degree-m determinant's nonzero value and leading coefficient, its signed product of ALL root errors, and explicit inverse conditioning. It does not supply a rational approximation center, universal real-rootedness, favorable primitive height, or a proof concerning the rationality of e+pi.

Bounded own normalization receipt: growing_pole_reference_identities.py produced GROWING_POLE_REFERENCE_IDENTITIES_RECEIPT.json. Thirty-six exact classical reference jet/successive-value identities and eight exact confluent factors for an unrelated toy positive measure passed. These checks supplement the proofs of the normalization, not the all-index estimates, and do not recheck Root's actual moment/content certificates.
