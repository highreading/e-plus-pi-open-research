> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# M33 widened pole-jet border: complete uniform mixed determinant nonzero

Author: Agent 3 / analysis, 2026-10-02. Original analytic result. Fresh archive and primary-literature gate: WIDE_POLE_JET_BORDER_GATE.md. Root supplies and owns the exact reduction of the full rational border to the mixed moment matrix, endpoint normalizations, arbitrary polynomial-direction algebra, primitive content and cost. This note proves the mixed determinant's uniform sign, nonzero value and conditional comparison. No audit or main-problem conclusion is made.

## 1. Full mixed determinant and result

Let mu be the probability pushforward of exp(-t)dt, t>=0, under y=(1-t)^2. For the actual normalized arctangent pole order m>=1 use

    c_m=4^m/binom(2m-2,m-1),
    dsigma_m(y)=[exp(sqrt(y))+c_m/(1+y)^m]dy/[2sqrt(y)],
    h=y+1,
    dmu_m=h^m dmu,    dtau_m=h^m dsigma_m.

In particular the COMPLETE actual compact density after the jet-annihilating factor is

    dtau_m(y)=[(1+y)^m exp(sqrt(y))+c_m]dy/[2sqrt(y)].       (1)

Both compact contributions are retained. Define the 2k-by-2k mixed matrix with ascending monomial columns by

    W_(k,m)=[ A ; B ],
    A_(i,j)=mu(h^m y^(i+j)),
    B_(i,j)=sigma_m(h^m y^(i+j))=tau_m(y^(i+j)),
    0<=i<k, 0<=j<2k,
    Delta_(k,m)=det W_(k,m).                                (2)

**Uniform complete theorem:** for EVERY k>=24 and EVERY 1<=m<=k,

    sign Delta_(k,m)=(-1)^k,
    Delta_(k,m)!=0.                                         (3)

The analytic sign proof actually permits any integer modifier order m>=0 for the Gamma measure and any nonzero positive compact lower measure with all needed moments; the stated pole construction uses m>=1 and Root's algebraic domain m<=k. No border realization beyond that domain is inferred.

For k>=100, a=1/(48e^4), and

    F*_(k,m)=det M_[mu(y+1)^(m+k),k]>0,
    D_(tau_m,k)=det M_(tau_m,k)>0,
    L0=exp(-4/a),

one has the full determinant bounds

    L0 F*_(k,m) D_(tau_m,k)
                 <=|Delta_(k,m)|<=F*_(k,m) D_(tau_m,k).      (4)

The comparison constant is absolute and independent of m, including growing m. The full widened rational border is invertible wherever Root's stated exact nonzero-constant reduction to (2) applies. Its canonical sign includes only the additional endpoint-row normalization/sign supplied by that algebra.

## 2. Conditional positivity: the extra modifier improves tail domination

Fix ANY k-1 nodes x_i in [-1,1], with coincidences allowed, and put Q(y)=product_i(y-x_i). Let p be a nonzero real polynomial of degree <k. Define

    I=[k^2,4k^2],  L=sup_[-1,1]|p|^2,
    C_k=3exp(-2k-1)(k^2-1)^(k-1)/[4k16^(k-1)].

The inherited elementary Legendre evaluation bound is

    integral_I p(y)^2dy>=3·16^(-(k-1))L.                    (5)

Its normalization follows by mapping I to [-1,1], bounding the degree-l exterior Legendre value by4^l, and summing the k-dimensional evaluation kernel; every evaluation point in [-1,1] maps to absolute coordinate less than2 for k>=2.

The actual positive mu tail density on I is at least exp(-2k-1)/(4k). On that interval,

    Q(y)>=(k^2-1)^(k-1),  (y+1)^m>=(k^2+1)^m.

Consequently the positive tail of mu(h^m Qp^2) is at least

    (k^2+1)^m C_k L.                                       (6)

The ONLY possibly negative continuous part is y in [0,1]. There |Q(y)|<=2^(k-1), h^m<=2^m and |p|^2<=L. Because the ENTIRE mu measure has mass1, its absolute negative contribution is at most2^(k-1+m)L. No part of this compact branch is omitted.

For every k>=24 the exact elementary inequality is

    C_k/2^k
      >4/[k(k^2-1)] [(k^2-1)/288]^k
      >=4(3/2)^k/[k(k^2-1)]>1.                             (7)

The first step uses e<3; the second uses k^2-1>=432. The final threshold is certified by the integer inequality 4·3^24>2^24·24·575, and its ratio at consecutive indices is (3/2)(k-1)/(k+2)>1 for k>7.

Thus the positive/negative ratio in the conditional Gram is greater than

    2[(k^2+1)/2]^m>=2,                                    (8)

for all modifier orders m>=0. Every k-dimensional conditional Gram M_[mu h^m Q,k] is positive definite. This is not deduced from positivity of mu_m alone: its node-product modification has a signed compact part, and (6)--(8) control it explicitly.

For a FULL k-node configuration x in [-1,1]^k, put Q_x=product_(i=1)^k(y-x_i). Its positive tail gains an additional factor k^2-1, and its compact negative bound is at most2^(k+m)L. Therefore

    mu(h^m Q_x p^2)
      >=[(k^2-1)(k^2+1)^m C_k-2^(k+m)]L>0,
    F_(k,m)(x):=det M_[mu h^m Q_x,k]>0.                    (9)

All node configurations, including coincident nodes, are covered. This proves the exact positivity needed inside the final compact-node integral.

## 3. Full Andreief sign and nonzero

Finite double Andreief gives the EXACT mixed determinant identity

    Delta_(k,m)=(-1)^k/k! integral_[0,1]^k
                   Vand(x)^2 F_(k,m)(x) d tau_m^k.         (10)

The sign comes from orienting the cross product as product_(i,j)(y_i-x_j): the k-by-k crossing has sign(-1)^(k^2)=(-1)^k. The normalization is1/k!, since the inner k-by-k Gamma Hankel determinant already contains its own1/k! Andreief factor.

By (9), F is strictly positive, and tau_m has a strictly positive density on(0,1). Vand(x)^2 is positive away from its usual coincident-node diagonals. Thus the integral is strictly positive. This proves (3), and hence the stated widened-border invertibility through Root's exact reduction.

Positivity of two measures would not suffice for this conclusion: if the upper and lower measures coincided, the two row blocks in (2) would be identical and the determinant would vanish. The actual overlapping Gamma/compact pair is controlled by (6)--(9), not assumed to form a disjoint-support Angelesco or AT system.

## 4. Uniform conditional roots and determinant comparison for growing m

Keep k-1 nodes in [-1,1] and let eta=mu h^m Q. Its degree<k Gram is positive by Section2. For k>=100 set

    A=ak^2,  a=1/(48e^4),  L_A=sup_[-1,A]|p|^2.

Here A>=2 and A<k^2. The Legendre estimate (5) holds for this larger test interval as well; its most exterior mapped point is still -1. The positive tail of eta((y-A)p^2) is at least

    (k^2-A)(k^2+1)^m C_k L_A.

Its entire negative part lies in[0,A], with absolute bound

    A(A+1)^(k-1+m)L_A.

Thus the positive/negative ratio is at least

    (k^2-A)C_k/[A(A+1)^(k-1)]
                           ·[(k^2+1)/(A+1)]^m
      >=3(1-a)exp(2k-4)/(4eak)
                           ·[(k^2+1)/(A+1)]^m>1.          (11)

For the second inequality use k^2-1>=k^2/2, A+1<=3ak^2/2 and1/(48a)=e^4, as in the inherited conditional-root calculation. The final inequality holds for k>=100: the m factor is at least1, and the preceding positive factor already exceeds1. This proves eta((y-A)p^2)>0 with a constant independent of m.

The exact symmetric multiplication compression in this positive conditional Gram therefore has ALL roots z_j>A. The final-node characteristic identity is

    F_(k,m)(x,u)=det M_(eta,k) product_(j=1)^k(z_j-u).

For u in[-1,1],

    exp(-4k/A)<=F(x,u)/F(x,-1)<=1.

Replacing the k nodes successively by -1 gives

    L0<=F_(k,m)(x)/F*_(k,m)<=1,
    F*_(k,m)=det M_[mu(y+1)^(m+k),k].                      (12)

Equation (12) is uniform in growing m. Substituting it in the FULL integral (10), and using1/k! integral Vand^2 d tau_m^k=D_(tau_m,k), proves (4).

## 5. Algebraic/arithmetic handoff and limits

Root's widened square border consists of k matching rows C, k rational rows R and m endpoint Taylor rows, on width2k+m. After the exact full moment row additions and annihilation by(y+1)^m, Root reduces it to (2) up to a specified nonzero normalization. The theorem above supplies its missing all-index analytic nonzero input, already at k>=24 for EVERY1<=m<=k. The constants and sign of the mixed determinant are explicit; any raw-versus-normalized Taylor factorial belongs to the border algebra and must be retained there.

The compact density (1), full Gamma branch, complete conditional Gram and determinant comparison all refer to the actual period construction. The original matching jet was eliminated by the exact algebraic factor, rather than dropped analytically. The proof makes no assertion that an arbitrary chosen degree-m polynomial direction has small coefficient height after final gcd. Primitive arithmetic, coefficient-selection costs and any approximation criterion remain separate. No conclusion about the rationality of e+pi follows from the freedom or nonzero border alone.
