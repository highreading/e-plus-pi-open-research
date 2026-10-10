> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Limited inverse and log(2) envelope review

Verdict: PASS WITH A TERMINOLOGY REPAIR for the precisely required inverse inequalities and their propagation in LOG_TWO_FORCING_ENVELOPE_DRAFT.md. The logarithmic residual is holomorphic in |z|<sqrt(2), not entire. Every contour used in the argument lies strictly inside that disk, so the repair changes neither the estimate nor its domain.

This completes the retained paper examination. It does not repeat the contact-normality review, the quotient audit, their checks, or the alternative log(2) proof. No new numerical computation is claimed. The examined inverse dependencies are the localization/coercivity argument, the actual positive forcing lower bound, and finite B reconstruction in agent3/CONTACT_INVERSE_RESEARCH.md Section 9. The positive forcing upper bound, older (3/2)^n residual bound, older exp(-n/8) propagation, and full-coefficient reconstruction norm are unnecessary to this verdict.

The coercive inverse inequalities hold for integers n>=16, 2<=b<=n, n>=512 b^4 log n. The center application uses b>=3 and 1<=m<=floor((b-1)/2). The new logarithmic kernel estimate itself needs only n>=2 and 1<=b<=n. Logarithms are natural. Existence and the exact Toeplitz reduction use the retained normality PASS in its stated domain.

## 1. Coercive Toeplitz inverse

Write R=sqrt(2), M=1+sqrt(2), d0=b-1, and D_R=diag((-R)^i), 0<=i<b. Let T_ij=[z^(n+i-j)] exp(z)(1-z+z^2/2)^n. The matrix H=(-1)^n D_R T D_R^(-1) has the symbol

    (1+R cos u)^n exp(-R exp(iu)).

The Toeplitz quadratic form is its normalized circle integral against the squared modulus of the coefficient polynomial. This representation retains the complex phase and the possible negative real contribution for odd n.

For a polynomial of degree at most d0, put h=1/sqrt(n) and choose one point in each interval

    I_j=[-h+2jh/b,-h+(2j+1)h/b], 0<=j<b,

by the integral mean inequality. The intervals have length h/b, and their selected values satisfy

    sum_j |p(exp(iu_j))|^2 <= (b/h) integral_(-h)^h |p(exp(iu))|^2 du.

The factor here is b/h, not b^2/h. For i<j, the selected angles differ by at least (j-i)h/b and by at most 2h<=pi. The chord inequality gives

    |exp(iu_j)-exp(iu_i)| >= (j-i)h/(2b).

The numerator coefficient l1 norm of each degree-d0 Lagrange polynomial is at most 2^d0. Its denominator is at least (h/(2b))^d0 j!(d0-j)!. Cauchy-Schwarz and sum_j binom(d0,j)^2=binom(2d0,d0) therefore prove exactly

    integral_(-h)^h |p(exp(iu))|^2 du
      >= ||coeff(p)||_2^2/[b sqrt(n) Cint],
    Cint=(16b^2 n)^d0 binom(2d0,d0)/(d0!)^2.

For all |x|<=sqrt(2), the alternating cosine bound gives cos x>=7/45. On |u|<=1/sqrt(n), Bernoulli gives (1+R cos u)^n>=M^n/2. Since exp(-R)>1/9, the real part of the symbol there is greater than M^n/128. With

    K0=2048b sqrt(n) Cint,

the normalized central quadratic contribution is at least 2M^n/K0 times the coefficient norm squared; pi<4 suffices for this comparison.

For even n all other real contributions are nonnegative. For odd n a negative real contribution requires 1+R cos u<0, and its whole magnitude is at most

    9(R-1)^n ||coeff(p)||_2^2.

The stated slow-growth domain implies n>16384, b^4<=n, Cint<=n^(2d0), and K0<=n^(2b). It also gives

    2b log n <= n/(256b^3),
    9K0 ((R-1)/M)^n < 9n^(2b)4^(-n)<1.

Thus the complete real quadratic form of H is at least M^n/K0 times the coefficient norm squared. Its symbol modulus is at most exp(R)M^n<9M^n. Compression of multiplication by the symbol yields the forward norm bound, and coercivity yields the inverse bound:

    ||D_R T D_R^(-1)||_2 <= 9M^n,
    ||D_R T^(-1)f||_2 <= K0 M^(-n)||D_R f||_2.

These are actual operator bounds with no unevaluated inverse norm. The tail estimate includes the entire adverse odd-n region.

## 2. Actual forcing lower bound and finite reconstruction

Let Q0(z)=1-z+z^2/2. The actual positive endpoint forcing is

    fP_i=[z^(n+i)] Q0^n D^n(1/(1-z)).

Expanding Q0=((1-z)^2+1)/2 gives

    fP_i=n!2^(-n) sum_(l=0)^floor(n/2)
             binom(n,l)binom(2n+i-2l,n+i).

The omitted terms are polynomials of degree below the requested coefficient index. Every retained term is positive. The i=0,l=0 term alone gives

    ||D_R fP||_2 >= n!2^(-n)binom(2n,n)
                  >= n!2^n/(2n+1)=Fminus.

This is a lower bound for the actual forcing column, not a ratio of majorants.

On polynomials of degree d0, ||D^l||_2=d0!/(d0-l)!. The finite binomial expansions therefore give

    ||(D+1)^n||_2 <= (n+1)^d0=Hplus,
    ||(D+1)^(-n)||_2 <= (n+b)^d0=Hminus.

Multiplication by z-1 has norm at most 2; partial sums invert it on its image with norm at most b. These estimates retain both diagonal scalings. For the actual B lift u=Psi(1,0),

    ||u||_2 >= L,
    L=Fminus/[9b R^d0 Hplus M^n].

Writing v=Psi(0,1), S=e+pi, and D_B for multiplication by z-1, reconstruction is exactly

    v-Su=e0+D_B(D+1)^(-n)T^(-1)(fQ-SfP).

The additive e0 is the constant endpoint term in B=Q+(z-1)B'. It cannot be dropped. In particular any bound E0 for ||D_R(fQ-SfP)||_2 gives

    ||v-Su||_2 <= 1+2Hminus K0 E0/M^n.

No estimate for the full A/C coefficient norm is used here.

## 3. New kernel bound and complete coefficient envelope

The complete forcing residuals are

    H_F(z)=-n! integral_-1^1 [t Q0(z)/(1-tz)]^n
                             /[(1-t)(1-tz)] du,
    t=(1+iu)/2,
    H_E(z)=-Q0(z)^n integral_0^1 x^n exp(1-x)exp(xz) dx.

Their coefficients at n+i are eF_i and eE_i. These identities retain the complete difference quotients before differentiation. In particular fQ-SfP=eF+eE.

Set t_plus=(1+i)/2, t_minus=(1-i)/2 and alpha=(1+u)/2. Then

    (1-tz)/Q0(z)
      =alpha/(1-t_minus z)+(1-alpha)/(1-t_plus z).

For |w|<=theta<1,

    Re(1/(1-w))>=1/(1+theta).

After multiplication by the positive denominator, this is equivalent to theta+(1-theta)Re(w)-|w|^2>=0, which follows from Re(w)>=-theta and |w|^2<=theta^2. Therefore on |z|<=R theta,

    |t Q0(z)/(1-tz)| <= (1+theta)/R.

Together with |1-t|>=1/2, |1-tz|>=1-theta, and integration length two, this gives

    |H_F(z)| <= 4n![(1+theta)/R]^n/(1-theta).

Cauchy's coefficient estimate at the original index n+i, with the diagonal factor R^i retained, proves

    ||D_R eF||_2
      <=4 sqrt(b)n! theta^(-d0)[(1+theta)/(2theta)]^n/(1-theta).

Choose theta=1-1/n. Since d0<=n-1, theta^(-d0)<e<3. Also [1+1/(2(n-1))]^n<=e<3. Hence

    ||D_R eF||_2 <=36n sqrt(b)n!.

For H_E, Cauchy's estimate on |z|=R uses |Q0(z)|<=RM, exp(1-x+xR)<=exp(R)<9, and integral_0^1 x^n dx=1/(n+1). It gives 9 sqrt(b)M^n/(n+1), so the draft's constant 27 is a valid weakening. Consequently

    E0_new=36n sqrt(b)n!+27 sqrt(b)M^n/(n+1)

bounds the whole forcing residual vector.

Terminology repair: H_E is entire, but H_F is generally not entire. H_F is holomorphic in |z|<sqrt(2); its representation as the differentiated logarithmic difference quotient has a removable apparent singularity at z=1. The logarithmic branch singularities at the conjugate boundary points need not disappear. The logarithmic contour radius R(1-1/n) is strictly interior. Thus no boundary analyticity or integration across a branch cut is required, and the terminology defect does not invalidate any estimate.

## 4. Propagation to the rational Gram center

For 1<=m<=floor((b-1)/2), use precisely

    w_j=(n+m+1-b)!/(n+m+1-j)!, 0<=j<=b,
    W=diag(w_j^2).

These weights satisfy 0<w_j<=1 and wmin>=(2n)^(-b). Define

    theta_G=(u^T W v)/(u^T W u),
    Enew=1+2Hminus K0 E0_new/M^n.

Weighted Cauchy-Schwarz and the lower bound on u give

    |theta_G-S| <= ||W^(1/2)(v-Su)||_2/||W^(1/2)u||_2
                 <= Enew/(wmin L)
                 <= (2n)^b Enew/L.

This is the B-only weighted Gram center. It is not the full-coefficient Gram center or an individual coordinate quotient.

The expansion of the last expression has exactly the following three factors and prefactors:

    ((M/2)^n/n!) C1,
    2^(-n) C2,
    ((M/2)^n/n!) C3,

    C1=9(2n)^b b R^d0 Hplus(2n+1),
    C2=648n(2n)^b b sqrt(b)R^d0 Hplus Hminus K0(2n+1),
    C3=486(2n)^b b sqrt(b)R^d0 Hplus Hminus K0(2n+1)/(n+1).

The constants and the extra n in C2 are correct. Each is at most n^(10b) on the stated domain. One conservative ledger uses K0<=n^(2b), (2n)^b<=n^(3b/2), Hplus,Hminus<=n^(3d0/2), R^d0<=n^(d0/2), b sqrt(b)<=n, and 2n+1<=n^2. The numerical constants are below n. Including the extra n yields exponent at most 7b+3/2<=10b in C2.

It follows that

    |theta_G-S| <= delta_n,
    delta_n=n^(10b)[2^(-n)+2(M/2)^n/n!].

The domain implies b log n/n<=512^(-1/4)(log n/n)^(3/4), tending uniformly to zero. Also M^n/n! tends to zero. Thus

    log delta_n=-n log 2+10b log n+o(1)=-n log 2+o(n).

This equality concerns the explicit positive envelope delta_n. It is not an asymptotic equality for the actual error. No sign, lower bound, nonvanishing, or nonstabilization of the rational centers has been established.

## 5. Primitive-pair implication and precise limits

If theta_G=p/q is fully reduced, q>0, the direct pair (-p,q),(x,y), with qx+py=1 and |y|<=q/2, satisfies

    |-p+qS|<=q delta_n,
    |x+yS|<=1/q+q delta_n/2.

These are bounds on complete forms. The individual integral polynomial lifting factors cancel against their own endpoint gcds. Therefore q->infinity and q delta_n->0 suffice for the paired irrationality criterion. Neither arithmetic condition follows from the inverse estimates reviewed here.

The verdict accepts only the specified new inverse/log(2) dependencies and this propagation. It does not review the alternative log(2) proof or any subsequent scalar-center draft. Failure of a sufficient denominator bound is not an exclusion of small actual forms. No conclusion about the rationality of e+pi is obtained.
