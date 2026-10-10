> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Uniform growing-degree Gamma/compact leading coefficient

Author theorem: Agent 3 / analysis, 2026-10-02. Fresh gate: UNIFORM_GAMMA_COMPACT_LEADING_GATE.md. Root's bounded-degree predecessor and the actual leading-homogeneous arithmetic interface are in main/SHIFTED_SHORT_FIXED_DIMENSION_TRANSCENDENCE_OBSTRUCTION.md. Root owns the polynomial-transcendence measure, coefficient height, actual evaluated gcd, and the resulting primitive-denominator consequences; those are not duplicated here.

## 1. Exact coefficient and uniform result

For real X>=0, let Gamma_X be the probability pushforward under y=u^2 of the Gamma(X+1,1) density. Set

    P_r(X)=(X+1)_(2r),
    dc_X(y)=exp(sqrt(y)-1)y^((X-1)/2)dy/2, 0<y<1,
    c_r(X)=exp(-1) integral_0^1 exp(u)u^(X+2r)du,
    V_ij=(-1)^(i+j), 0<=i<k, 0<=j<2k.

The exact leading coefficient is

    Z_k(X)=det[ P_(i+j)(X) ; c_(i+j)(X)-V_ij ].                 (1)

For even integer X, this is Root's actual leading f^k coefficient divided by its stated integer clearer factor. The equality uses the exact row operation removing c_0P from the upper recurrence block, including the block-swap/lower-row signs. The even-step integration recurrence also gives its polynomial continuation for real X>=0. No claim of generic specialization nonvanishing is substituted for (1).

Explicitly put Q_0=0 and

    Q_(r+1)=(X+2r+1)(X+2r+2)Q_r-(X+2r+1).

Integration by parts twice gives

    c_(r+1)=(X+2r+1)(X+2r+2)c_r-(X+2r+1),
    c_r-c_0P_r=Q_r.

These identities hold for every real X>=0; the intermediate integrations have positive powers at the zero endpoint. Subtracting c_0 times each corresponding upper row from the lower rows in (1) yields Z_k=det[P;Q-V], an actual integer polynomial in X. Thus proving its sign on the stated real region also proves evaluated nonzero values of the exact polynomial used by Root. Root's recurrence denotes this Q_r by Q_(2r); this is only an index convention.

Put a=1/(48e^4). The new UNIFORM conclusions are:

1. For EVERY k>=1 and X>=100, every Gamma-square conditional moment Gram with any k-1 nodes in [-1,1] is positive definite, and its k multiplication-compression roots are greater than aX^2.
2. In this range, write the exact positive integral terms from (1) as Z_k=(-1)^k(A_c-B_c). Then

       exp(-4k^2/(aX^2)) Lambda_(c_X,k)(-1)
          <= A_c/B_c <=exp(4k^2/(aX^2)) Lambda_(c_X,k)(-1),      (2)
       0<Lambda_(c_X,k)(-1)<=mass(c_X)<=1/(X+1).

3. In particular for EVERY k>=1 and X>=128k,

       Z_k(X)!=0,  sign Z_k(X)=(-1)^(k+1),
       0<A_c/B_c<=e/(X+1)<1.                                (3)

Thus (3) is an explicit growing-k leading-coefficient condition. It proves an evaluated nonzero coefficient in the actual complete arithmetic interface, not an actual-denominator growth rate by itself.

## 2. Tail coercivity with the true Gamma lower-tail mass

Fix k-1 arbitrary nodes x_i in [-1,1], let Q(y)=product_i(y-x_i), and let nu=Q Gamma_X. All estimates below may use the unnormalized Gamma-square measure

    dgamma_X(y)=y^((X-1)/2)exp(-sqrt(y))dy/2;

division by Gamma(X+1) is a common positive factor and does not affect positivity or roots.

Assume X>=100. Set I=[X^2,4X^2], A=aX^2>=2. For deg p<k, exterior Legendre evaluation on I gives

    integral_I p(y)^2dy >=3X^2/[k^2 16^(k-1)] L_A(p),
    L_A(p)=max(|p(-1)|^2,sup_[0,A]|p|^2).                     (4)

The affine images of this test set are bounded by absolute value 2, independently of k and X. On I,

    Q(y)>=(X^2-1)^(k-1),
    dgamma_X/dy>=X^X exp(-2X)/(4X).

Hence the positive tail in nu(p^2), before the common normalization, is at least C_(X,k)L_A, with

    C_(X,k)=3exp(-2X)X^(X+1)(X^2-1)^(k-1)/[4k^2 16^(k-1)].   (5)

All negative contributions to Q gamma_X(p^2) lie in [0,1]. The true mass there satisfies

    integral_0^1 u^X exp(-u)du<=1/(X+1).

Its absolute loss is therefore at most 2^(k-1)L_A/(X+1). Their ratio is

    C_(X,k)(X+1)/2^(k-1)
      =3(X+1)X/(4k^2) (X/e^2)^X [(X^2-1)/32]^(k-1)>1.         (6)

This inequality is uniform over ALL k, not just k<=X: for X>=100, (X^2-1)/32>4, and k^2<=4^(k-1). Also X/e^2>100/9. Thus the degree-<k Gamma modified Gram is positive definite.

For the shifted form nu((y-A)p^2), every possible negative continuous contribution lies in [0,A]. Its TRUE Gamma mass is bounded by

    integral_0^sqrt(A) u^X exp(-u)du
        <=A^((X+1)/2)/(X+1).                                (7)

No exterior atom belongs to this upper measure. Consequently the negative contribution is at most

    A(A+1)^(k-1) A^((X+1)/2)L_A/(X+1).                      (8)

The positive tail is at least (X^2-A)C_(X,k)L_A. Using X^2-1>=X^2/2 and A+1<=(3/2)aX^2 gives a positive-to-negative ratio of at least

    3(1-a)(X+1)/(4a^(3/2)k^2) (sqrt(48))^X exp(4(k-1))>1.   (9)

Indeed exp(4(k-1))/k^2>=1 for all k>=1, and the remaining factor exceeds 1 already at X=100. This calculation is the essential improvement over a coarse unit-mass bound for the lower Gamma tail; such a bound would lose the growing-X gain.

It follows that nu((y-A)p^2)>0 for every nonzero deg p<k. Its symmetric multiplication compression therefore has EVERY eigenvalue z_i>A. These are the conditional roots used in the exact determinant insertion; no classical Laguerre zero theorem or a globally positive signed measure has been assumed.

## 3. Full leading determinant and its single-atom decomposition

For k nodes x in [-1,1], define

    F_Gamma(x)=det M_[Gamma_X product_i(y-x_i),k].

For a final node u, the exact finite characteristic identity is

    F_Gamma(x_1,...,x_(k-1),u)
      =det M_(nu,k) product_(i=1)^k(z_i-u).

The positive Gram and z_i>A>=2 prove F_Gamma(x)>0 for EVERY k-node configuration. They also give

    exp(-4k/A)<=F_Gamma(x,u)/F_Gamma(x,-1)<=1,
                   -1<=u<=1.

Replacing the k nodes successively yields

    exp(-4k^2/(aX^2))<=F_Gamma(x)/F_Gamma^*<=1,
    F_Gamma^*=det M_[Gamma_X(y+1)^k,k]>0.                     (10)

Apply the exact mixed Andreief identity to (1). The compact lower functional is c_X-delta_-1. Configurations containing two lower exterior atoms vanish by the squared Vandermonde. Therefore

    Z_k(X)=(-1)^k(A_c-B_c),                                 (11)

    A_c=1/k! integral_[0,1]^k Vandermonde(x)^2
                                    F_Gamma(x) dc_X^k,
    B_c=1/(k-1)! integral_[0,1]^(k-1) Vandermonde(x)^2
                   product_i(1+x_i)^2 F_Gamma(x,-1) dc_X^(k-1).

Both A_c and B_c are strictly positive. Their normalization is the actual leading block, not a replacement by an unsigned modulus ensemble. Using (10), their ratio differs by at most exp(±4k^2/(aX^2)) from the positive compact Christoffel minimum. This proves (2).

The constant polynomial is an admissible test, and exp(u-1)<=1 on [0,1], proving Lambda<=1/(X+1). If X>=128k, then

    4k^2/(aX^2)<=4/(a·128^2)<1,

because e^4<81. Hence A_c/B_c<=e/(X+1)<1, and (11) proves (3), with the complete leading coefficient sign.

## 4. Explicit very-large-degree extension

There is also a distinct uniform k-root floor, inherited from the direct tail proof of SHORT_RECTANGULAR_COMPLETE_SIGNED_ERROR.md, not from Root's fixed-degree Hermite limit. For EVERY X>=0 and k>=100, replace its base pushforward measure by the Gamma(1) square pushforward and use the power y^(X/2). Its tail density on [k^2,4k^2] is larger by e than the old tail lower bound, the possible negative compact mass is no larger, and the upper exterior atom is absent. The same finite inequalities therefore give all conditional roots >ak^2.

This proves F_Gamma>0 and (11) in this range, together with

    A_c/B_c<=exp(4/a)Lambda_(c_X,k).

The polynomial p(y)=((1-y)/2)^(k-1) has p(-1)=1. Its pointwise square is at most 4^(-(k-1)) on [0,1]. Thus

    A_c/B_c<=exp(4/a)4^(-(k-1))/(X+1).                       (12)

Consequently define the explicit integer

    K0=2+ceil(4/(a log 4)).

For EVERY k>=K0 and EVERY X>=0, (12) is strictly less than 1. Hence Z_k(X) is nonzero with sign (-1)^(k+1) even without a large-X requirement. No small k enumeration or sign-polynomial extrapolation is involved.

More generally, if X>=100 and k>=100, the two conditional-root floors combine to give

    A_c/B_c<=exp[4k^2/(a max(X,k)^2)] Lambda_(c_X,k),

with the reciprocal exponential lower bound too. Equations (2), (3), and (12) identify explicit nonzero regions; they do not optimize the intentionally coarse constant a.

## 5. Reference-scale option and actual arithmetic scope

For X/k tending to infinity, (2) implies A_c/B_c=[1+O(k^2/X^2)]Lambda_(c_X,k). The compact weight has endpoint factor 1/2:

    dc_X=(1/2)exp(sqrt(y)-1)y^((X-1)/2)dy.

The uniform Jacobi quadratic-form concentration argument in SHIFTED_SHORT_UNBOUNDED_M_COMPLETE_ERROR.md applies with M=X/2. Therefore it can retain the exact finite exterior Jacobi remainder and give A_c/B_c=(1/2)Lambda_(gamma_(X/2),k)[1+O(k/X+k^2/X^2)]. This is a leading-coefficient ratio, not a replacement for the separately proved complete S-c formula.

In Root's actual leading-homogeneous polynomial, the f^k coefficient is its exact integer clearer factor times Z_k(X). Statement (3) makes this evaluated coefficient nonzero whenever X>=128k, and (12) covers all sufficiently large k irrespective of X. Any extraction at 1/e must still retain the actual rational center, final gcd, coefficient height, and the primary polynomial-transcendence theorem's growing-degree hypotheses. Root owns that transfer. No irrationality theorem or actual primitive-denominator rate is inferred from this analytic lemma alone.
