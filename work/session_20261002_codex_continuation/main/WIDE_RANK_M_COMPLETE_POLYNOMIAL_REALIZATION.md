> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# M33. Minimal-width complete response control and arbitrary primitive polynomial directions

Original author theorem, 2026-10-02. Fresh gate: WIDE_RANK_M_POLYNOMIAL_REALIZATION_GATE.md. The independent analytic part was authored by Agent3 in WIDE_POLE_JET_BORDER_COMPLETE_NONZERO.md; it is not described as a review. This construction extends M25's rank-one freedom. It does not prove e+pi rational or irrational.

## Actual complete moment and endpoint matrices

Let S=e+pi, h=y+1, mu(y^r)=D_(2r), and use the normalized pole order m from M31. Its rational functional is

    nu_m(P)=sum_(a=0)^(m-1) c_a P^(a)(-1),
    c_a=2^a binom(m-1,a)(2m-2a-3)!!/(2m-3)!!.

For the complete compact moment, write

    sigma_m(y^r)=eD_(2r)-(2r)!+alpha_(m,r)+pi nu_m(y^r).

Take k>=m, width N=2k+m, with ascending monomial columns. Define k-by-N matrices

    C_(i,j)=mu(y^(i+j))-nu_m(y^(i+j)),
    R_(i,j)=alpha_(m,i+j)-(2i+2j)!,
    V_(i,j)=nu_m(y^(i+j)),

and normalized Taylor matrix E_(a,j)=binom(j,a)(-1)^(j-a), 0<=a<m. With E_left=E[:,0:k]^T and

    J_(a,b)=(a+b)! c_(a+b) if a+b<m, and 0 otherwise,

one has EXACTLY V=E_left J E. J is invertible and has anti-triangular determinant sign(-1)^binom(m,2) times a positive rational number. All Taylor factorials are included.

The physical full moment matrix is

    sigma=eC+R+S V.

Thus on the matching kernel C Q=0 the COMPLETE integral determinant is det((R+S V)Q). Dropping the unmatched exponential rows would be invalid; the equality above is the precise elimination.

## Exact border reduction and uniform invertibility

Consider the square rational border B0=[C;R;E], size N. Add eC+S V to the middle rows, and add E_left J E to the top rows. Both are determinant-preserving operations using other row blocks. This changes the upper two blocks to [mu;sigma], while the last block remains E.

Change the monomial column basis to

    1,h,...,h^(m-1), h^m,h^m y,...,h^m y^(2k-1).

This monic degree-ordered change has determinant1. The bottom jet block is [I_m,0]; expansion across it has sign(-1)^(2km)=1. Consequently, with NO extra hidden endpoint factorial,

    det B0 = det [mu(h^m y^(i+j)); sigma_m(h^m y^(i+j))],
    0<=i<k, 0<=j<2k.                                      (1)

Agent3's new full tail/compact proof gives (1) nonzero with sign(-1)^k for every k>=24 and 1<=m<=k. It retains the signed conditional Gamma modification; it does not infer nonzero merely from two positive measures. Therefore the rational response map

    ker_Q C --> Q^k direct_sum Q^m,
    z --> (Rz,Ez)                                          (2)

is an isomorphism. Its domain and codomain both have dimension k+m.

Width2k+m is the smallest width that can make THIS ENTIRE linear response map surjective when C has row rank k. This is only a dimension statement about full response control; no minimal-width claim for polynomial directions alone is made.

## Every nonzero primitive polynomial of degree at most m can be encoded

Choose an invertible rational left-row matrix F such that

    F E_left J = U=[0_(k-m,m); I_m].                       (3)

One explicit choice starts with the left polynomial rows h^m y^i, i<k-m, followed by h^a, 0<=a<m, and multiplies the last m rows by J^(-1). Let B=[C;FR;E], which is invertible by (1).

Fix ANY primitive integer polynomial

    f(T)=a_0+a_1T+...+a_d T^d, 1<=d<=m, a_d>0.

Let Comp(f/a_d) be the ordinary rational companion matrix. Set A=diag(I_(k-d),-Comp(f/a_d)), and let Bjet be m-by-k with its last d rows and last d columns equal to I_d and all other entries zero. Solve the unique rational system

    Q=B^(-1)[0;A;Bjet].                                   (4)

Then C Q=0, FR Q=A and E Q=Bjet. The columns of Q are independent: the stacked prescribed response [A;Bjet] has rank k. Equations (3)--(4) give the COMPLETE determinant identity

    det((FR+T FV)Q)=det(A+T U Bjet)=f(T)/a_d,
    det((R+T V)Q)=f(T)/(a_d det F).                        (5)

The companion identity follows by direct expansion of TI-Comp; it is classical. Nonzero constants are also realized by prescribing Bjet=0 and any invertible constant A. This result concerns actual decomposable k-planes (4), not arbitrary vectors in an exterior coefficient module. In rank>1, Plucker constraints cannot be ignored.

## Integer lifting and FINAL primitive content

Let d_j be the least common denominator of column j of Q and Z=Q diag(d_1,...,d_k), so Z has integer entries and C Z=0. Let delta be ANY positive integer clearing the FULL R matrix; V is rational, so if needed enlarge delta to clear both R and V. The exact receipts use such a common clearer. Then the full integer polynomial is

    I(T)=det(delta(R+T V)Z)=lambda f(T),
    lambda=delta^k product_j(d_j)/(a_d det F).              (6)

Because I has integer coefficients and f is primitive, Bezout for the coefficients of f shows lambda is an integer. All actual coefficients therefore have gcd EXACTLY |lambda|. After removing it and choosing positive leading coefficient, the actual primitive polynomial is EXACTLY f.

For d=1, f(T)=qT-p with gcd(p,q)=1, q>0, the final denominator is q and the complete primitive form is qS-p. Neither the large integer right-polynomial coefficients, delta, detF nor lambda may be replaced by an untracked gain; (6) explicitly accounts for their cancellation in the final coefficients.

Thus the enlarged family can encode every rational center, every degree-m polynomial direction, and directions with nonreal roots. It supplies no theorem selecting a small NONZERO integer value at S. Preselecting such a direction would import the unresolved Diophantine task itself. The positive full-stack/root-localization results for the fixed monomial width2k do not apply to arbitrary k-planes in this larger space.

## New exact receipts

WIDE_RANK_M_POLYNOMIAL_REALIZATION_CERTIFICATE.json contains23 new exact widened-plane realizations at (m,k)=(1,2),(2,2),(2,4),(3,3),(3,5),(4,4),(4,6),(5,5). The driver checks all endpoint jets and factorials, full matching, nonzero borders, left normalization, right column denominators, integer lifting, complete determinant coefficients and final coefficient gcd. Its targets include7T-41, fresh degree-m primitive polynomials, and T^2+1. This last target proves that a real-rootedness conclusion cannot hold for all widened choices.

The integer right-polynomial heights in these receipts range from40 to727bits. These are finite lifting costs, not an infinite height bound. No finite numerical S evaluation is used to assert a proof.

## Outstanding task

Find a controlled selection of right k-planes whose COMPLETE primitive polynomial values are provably nonzero and tend to zero, with an infinite sequence and all lifting costs retained. Equations (1)--(6) make the freedom exact and also show why freedom alone does not solve e+pi.
