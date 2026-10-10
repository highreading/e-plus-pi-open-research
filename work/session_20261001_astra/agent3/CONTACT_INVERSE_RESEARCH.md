> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Quantitative contact inverse: endpoint forcing and reconstruction

Status: author research derivation, not independently reviewed. Contact normality and the exact contact reduction are explicitly provisional pending Child 4. Earlier certificates and proofs are preserved. No HP scan or old checker is replayed.

This note preserves the current derivation. The quantitative estimates in Sections 3–5 require final verification of their detailed constants before promotion to a completed uniform theorem. The exact forcing, reconstruction, and Gram identities are separated from that remaining verification.

## 1. Actual endpoint forcing

Let n>=16, 2<=b<=n and n>=512 b^4 log n. Write q(z)=1-z+z^2/2, S=e+pi, r=sqrt(2), M=1+r, and d=b-1. Endpoint data are (P,Q), distinct from the polynomial q.

Set

    A=P+(z-1)a, B=Q+(z-1)v, C=Q+(z-1)c,
    deg a,c<n, deg v<b,
    h=(P+Q(exp(z)+F(z)))/(1-z).

Contact O(z^(2n+b)) is equivalent to

    a+exp(z)v+F(z)c=h mod z^(2n+b).

Let G_n=exp(z)q^n and T_ij=[z^(n+i-j)]G_n for 0<=i,j<b. Under the provisional exact reduction, the TWO actual forcing columns are

    fP_i=[z^(n+i)]q^n D^n(1/(1-z)),
    fQ_i=[z^(n+i)]q^n D^n((exp(z)+F(z))/(1-z)),
    T vtilde=P fP+Q fQ, vtilde=(D+1)^n v.

Both columns are rational. Explicitly,

    fP_i=n! 2^(-n) sum_(l=0)^floor(n/2)
                         binom(n,l)binom(2n+i-2l,n+i).

For either column, writing h_m for its scalar h coefficients,

    f_i=sum_(s=0)^min(2n,n+i) [z^s]q^n
                    (2n+i-s)!/(n+i-s)! h_(2n+i-s).

Here hP_m=1 and hQ_m=sum_(j=0)^m(1/j!+[z^j]F). Every factorial argument is nonnegative.

Exact reconstruction is

    v=sum_(l=0)^d (-1)^l binom(n+l-1,l)D^l vtilde,
    p=[q^n D^n h-G_n vtilde]_(degree<n),
    c=U_n^(-1)p, U_n(c)=q^n D^n(cF),
    a=[h-exp(z)v-Fc]_(degree<n).

Thus A(1)=P and B(1)=C(1)=Q exactly. The actual B coefficients beta satisfy beta_0=Q-v_0, beta_j=v_(j-1)-v_j for 1<=j<b, and beta_b=v_(b-1).

## 2. Direction-sensitive forcing decomposition

The rational columns admit the real analytical decomposition

    fQ=S fP+eF+eE.

The residual generating functions are exactly

    q^n D^n((exp(z)-e)/(1-z))
      =-q^n integral_0^1 t^n exp(1-t)exp(tz)dt,

    q^n D^n((F(z)-pi)/(1-z))
      =-n! integral_-1^1 [t q(z)/(1-tz)]^n
                         /[(1-t)(1-tz)]du,
    t=(1+iu)/2.

These retain the complete functions and both conjugate ends of the segment. They follow by integrating the difference quotients before differentiation; compactness and analyticity near zero justify differentiation.

Put D_r=diag((-r)^j), 0<=j<b. The proposed explicit forcing estimates are

    Fminus=n!2^n/(2n+1),
    Fplus=n!sqrt(b) M^(n+b),
    E0=16sqrt(b)r^d n!(3/2)^n+27sqrt(b)M^n/(n+1),

    Fminus<=||D_r fP||_2<=Fplus,
    ||D_r(fQ-S fP)||_2<=E0.

The lower bound follows from fP_0 and binom(2n,n)>=4^n/(2n+1). The positive-sum upper bound uses radius 2-sqrt(2). The logarithmic residual is estimated on |z|=1 using |tq(z)/(1-tz)|<=3/2 and |(1-t)(1-tz)|^(-1)<8. The exponential residual is estimated on |z|=sqrt(2). The scalar identities supporting these steps were checked in contact_inverse_scalar_identity_checks.json; that check is not a verification of all inequalities.

## 3. Proposed uniform coercive inverse estimate

Define

    Cint=(16 b^2 n)^d binom(2d,d)/(d!)^2,
    K0=2048 b sqrt(n) Cint.

The quantitative target derived in the working analysis is

    ||D_r T^(-1)f||_2<=K0 M^(-n)||D_r f||_2,
    ||D_r T D_r^(-1)||_2<=9M^n.

The scaled symbol of (-1)^n D_r T D_r^(-1) is

    (1+r cos u)^n exp(-r exp(iu)).

Its Hermitian quadratic form is the integral of the real part of that symbol against the squared modulus of the coefficient polynomial. Globally cos(r sin u)>=7/45. On |u|<=1/sqrt(n), its real part is at least M^n/128, using (1+r cos u)^n>=M^n/2 and exp(-r cos u)>1/9.

The needed localization inequality is

    integral_(-1/sqrt(n))^(1/sqrt(n)) |p(exp(iu))|^2 du
       >=||coeff(p)||_2^2/[b sqrt(n) Cint], deg p<b.

It is obtained by Lagrange interpolation at b separated points selected in short disjoint subintervals. A complete write-up must specify the subinterval widths, point selection by integral means, chord lower bounds, and coefficient norms of every Lagrange polynomial to verify precisely the displayed Cint. This is the remaining detailed constant-verification step; the localization inequality must not be treated as established merely from its statement here.

With that inequality, the normalized central quadratic contribution is at least 2M^n/K0. For odd n the negative contribution can occur only where 1+r cos u<0. Its magnitude is at most 9(r-1)^n||coeff(p)||_2^2. The intended comparison uses K0<=n^(4b) and ((r-1)/M)^n<4^(-n), making this at most M^n/K0 in the stated regime. Accretivity then proves the inverse estimate directly. No Neumann series or unevaluated inverse norm is used.

The normality theorem is not independently audited by this argument. Its exact reduction remains a provisional dependency. The new coercivity argument needs its own completed quantitative proof.

## 4. Propagation through the actual B lift

Let Psi map endpoint data to the actual B coefficient vector. Write u=Psi(1,0), v=Psi(0,1), and define

    Hplus=(n+1)^d, Hminus=(n+b)^d,
    L=Fminus/[9b r^d Hplus M^n],
    U=2Hminus K0 Fplus/M^n,
    E=1+2Hminus K0 E0/M^n.

Conditional on the estimates of Sections 2–3, reconstruction gives

    L<=||u||_2<=U,
    ||v-Su||_2<=E.

The additive 1 in E is the actual constant Q in B=Q+(z-1)v. It cannot be dropped. Multiplication by z-1 costs at most 2 in Euclidean coefficient norm; division on its image costs at most b. The operator norms of (D+1)^n and its inverse on degree<b polynomials are bounded by Hplus and Hminus, respectively, using the finite derivative expansions.

The working estimate for the relative error is

    2(2n)^b E/L<=exp(-n/8).

Its proposed proof separates the logarithmic residual, proportional to (3/4)^n, from the two terms controlled by (M/2)^n/n!, bounds each prefactor by n^(10b), and uses n!>=(n/3)^n and 10b log n<=n/20. The individual prefactor comparisons must be checked explicitly together with Section 3 before this exponential relative-error statement is promoted to a theorem.

## 5. Full rational coefficient norm and reconstruction

The actual relaxed moment equations reconstruct

    Cstar=-sum_(k=0)^n ell_beta(p_k)p_k/h_k,
    A=-[B exp(z)+C F(z)]_(degree<=n).

Define positive rational constants

    c0=(b+1)(n+1)^2 64^n/[2(n+1-b)!],
    a0=3+10c0.

The coefficient estimates ||p_k||_1<=2^k and 1/|h_k|<=(2k+1)16^k/2 give

    ||C||_2<=c0||B||_2, ||A||_2<=a0||B||_2.

The constants 3 and 10 bound the full absolute coefficient sums of exp and F. Thus the reconstruction bound contains no unevaluated U_n inverse.

For positive rational weights 0<w_j<=1 and wmin=min w_j, define

    ||(A,B,C)||_W^2=(wmin/a0)^2||A||_2^2
       +sum_j w_j^2 B_j^2+(wmin/c0)^2||C||_2^2.

This is a positive definite rational full-coefficient norm. On the actual solution space,

    ||diag(w)B||_2<=||(A,B,C)||_W<=sqrt(3)||diag(w)B||_2.

Consequently, under Sections 2–4,

    ||Phi(P,Q)-(P+SQ)Phi(1,0)||_W<=sqrt(3)E|Q|,
    ||Phi(1,0)||_W>=wmin L.

For wmin>=(2n)^(-b), the proposed relative-error estimate would make the correction at most exp(-n/8)||Phi(1,0)||_W |Q|. The exact endpoint covector is (1,S); the matrix Phi and its two original columns remain rational.

## 6. Gram estimates and rational orientation

Write

    Sigma=Psi^T diag(w_j^2)Psi=[[Um,Vm],[Vm,Wm]],
    Dm=det Sigma, theta=Vm/Um,
    Hw=sum_j w_j^(-2).

The B lift is injective because B=0 forces C=0 by moment reconstruction and then A=0. Hence Sigma is positive definite whenever the provisional endpoint lift exists.

Conditional on the explicit column bounds above,

    wmin^2 L^2<=Um<=U^2,
    |theta-S|<=E/(wmin L),
    1/Hw<=Dm/Um<=E^2.

The lower Schur-complement estimate is unconditional on the quantitative inverse constants: every B vector Psi(0,1)-t Psi(1,0) has coefficient sum one. Weighted Cauchy–Schwarz gives squared norm at least 1/Hw. The upper estimate chooses t=S.

There is an exact rational orthogonal decomposition

    Psi=u(1,theta)+z(0,1),
    u^T diag(w^2)z=0,
    ||diag(w)z||_2^2=Dm/Um.

Thus the center and the orthogonal residual are actual rational construction data. Comparing theta to S supplies orientation information, not the reduced denominator of theta.

For the full-coefficient Gram matrix Gfull=Phi^T W Phi,

    Sigma<=Gfull<=3Sigma.

In particular Um<=Gfull_11<=3Um and Dm<=det Gfull<=9Dm. These inequalities reconcile the full reconstruction scale with the B-only scale; the two Gram matrices need not have the same rational center.

## 7. Child 2's complete-tail interface

The current MULTIROW_REMAINDER_RESEARCH.md and its report have been read. For b>=3 choose

    1<=m<=floor((b-1)/2), k=n+m,
    rm=n+m+1-b,
    w_j=rm!/(n+m+1-j)!.

These rational weights satisfy w_b=1 and wmin>=(2n)^(-b). The actual high constraints are ell_beta(p_(n+l))=0 for l=1,...,b-2. Their multi-row subtraction gives the COMPLETE identity

    P+QS=Q v_k/p_k(1)
          +ell_beta(t^m p_k/(1-t))/p_k(1).

For b=2 there is no such available multi-row choice. Use the unsubtracted complete-tail identity, keeping the inverse and reconstruction estimates separate.

In Child 2's normalization define

    gamma=3||p_k||_1/[p_k(1)rm!],
    dk=2|h_k|/p_k(1)^2,
    Z=(b+1)(gamma/dk)^2,
    G=2[e2 e2^T+Z Sigma], eta=dk.

Then exactly

    G11=2Z Um,
    det G/G11=2(1+Z Dm/Um),
    G12/G11=theta.

The preceding bounds imply

    2Z wmin^2 L^2<=G11<=2Z U^2,
    2(1+Z/Hw)<=det G/G11<=2(1+Z E^2).

The term e2 e2^T is indispensable: it retains the full pi error. If theta=p/q in lowest terms, the center-pair quantities are exactly

    2(b+1)gamma^2 Um/q^2,
    [2dk^2+2(b+1)gamma^2 Dm/Um]q^2.

No convergence or reduced-center denominator estimate is proved here. That arithmetic belongs to Child 4. Integral lifting multipliers multiply coefficients and the endpoint gcd equally and cancel from all homogeneous estimates.

## 8. Remaining completion steps

The actual forcing columns, reconstruction, complete-tail normalization, rational norm, and Gram identities have been retained explicitly. The pending mathematical work is to complete the interpolation constant proof and verify each prefactor in the claimed exponentially small relative correction. These are next research steps, not an access or authorization obstruction.

The final uniform inverse theorem must not be marked complete until those details and the saved outputs have been verified. No new HP scan or old checker replay is needed. Contact normality remains provisional pending Child 4 throughout.


## 9. Completion of the quantitative estimates

This section completes the previously pending details. Sections 3–4 deliberately preserved their unfinished status at the time of the initial save; the proofs below supersede those qualifications. The resulting quantitative statements are author deductions conditional on the provisional exact contact reduction, not independently reviewed results. No numerical normality test is used.

### 9.1 Localization with the stated constant

Put h=1/sqrt(n), d=b-1. For j=0,...,d take

    I_j=[-h+2jh/b,-h+(2j+1)h/b].

These b intervals of length h/b are disjoint and lie in [-h,h]. Given a coefficient polynomial p of degree at most d, select u_j in I_j with

    |p(exp(iu_j))|^2 <= (b/h) integral_(I_j)|p(exp(iu))|^2 du.

Such points exist by the integral mean bound and continuity. Set x_j=exp(iu_j). For i<j, u_j-u_i>=(j-i)h/b and u_j-u_i<=2h<=pi. The chord inequality gives

    |x_j-x_i| >= (j-i)h/(2b).

The Lagrange polynomial l_j(z)=product_(i!=j)(z-x_i)/(x_j-x_i) consequently satisfies

    ||coeff(l_j)||_2
      <=2^d(2b/h)^d/[j!(d-j)!].

Here the numerator coefficient l1 norm is at most 2^d since every node has modulus one. Apply Cauchy–Schwarz to p=sum_j p(x_j)l_j:

    ||coeff(p)||_2^2
      <=sum_j |p(x_j)|^2 sum_j ||coeff(l_j)||_2^2
      <= (b/h) integral_(-h)^h |p(exp(iu))|^2du
           * (16b^2/h^2)^d binom(2d,d)/(d!)^2.

The last sum uses sum_j binom(d,j)^2=binom(2d,d). This proves exactly the localization inequality with Cint in Section 3, including the factor b rather than b^2.

### 9.2 Accretivity and the actual inverse

For all |x|<=sqrt(2), the alternating cosine expansion gives

    cos x >=1-x^2/2+x^4/24-x^6/720 >=7/45.

The last polynomial decreases on this interval as a function of x^2. Thus the cosine of the symbol's phase is globally positive. On |u|<=1/sqrt(n), Bernoulli's inequality gives (1+r cos u)^n>=M^n/2. Together with exp(-r cos u)>=exp(-r)>1/9, its real part is at least M^n/128. After the normalized angle integral and the localization estimate, the central quadratic contribution is at least

    M^n/[256pi b sqrt(n) Cint] >=2M^n/K0.

For even n every other contribution has nonnegative real part. For odd n its negative real part is restricted to 1+r cos u<0 and has absolute value at most 9(r-1)^n. Parseval bounds its entire contribution by 9(r-1)^n||coeff(p)||_2^2.

The assumed range implies n>=8192 log n>16384 and b^4<=n. Using binom(2d,d)<=4^d and d!>=1 gives

    Cint <=(64b^2 n)^d<=n^(2d),
    2048b sqrt(n)<=n^2,
    K0<=n^(2b)<=n^(4b).

The middle inequality follows from b<=n^(1/4), n>16384, and 2048<=n^(5/4). Also

    2b log n <= n/(256b^3),
    9K0 ((r-1)/M)^n < 9n^(2b)4^(-n)<1.

Therefore the complete real quadratic form of H=(-1)^n D_r T D_r^(-1) is at least M^n||x||_2^2/K0. The symbol modulus is at most exp(r)M^n<9M^n. Compression of multiplication by the symbol to the polynomial subspace gives ||H||_2<=9M^n. Cauchy–Schwarz applied to Re(x*Hx) proves

    ||D_r T^(-1)f||_2<=K0 M^(-n)||D_r f||_2.

This is a genuine uniform inverse estimate, not an estimate containing an unevaluated inverse. It applies to both actual forcing columns and arbitrary linear combinations. The proof has no Neumann-series step.

### 9.3 Details of the forcing estimates

For the P column, q=((1-z)^2+1)/2 gives the positive sum in Section 1. Terms with l>floor(n/2) are polynomials of degree at most n-1 and do not contribute to the coefficient n+i. Let rho=2-sqrt(2). Evaluating the remaining positive-coefficient generating terms at rho, and then adding the omitted positive values, bounds

    r^i fP_i
      <= n! r^i rho^(-n-i) q(rho)^n/(1-rho)^(n+1)
      =n! M^(n+1+i).

Here q(rho)=rho, (1-rho)^(-1)=M, and r/rho=M. This proves Fplus. The l=0 term of fP_0 is n!2^(-n)binom(2n,n), proving Fminus.

For the logarithmic residual let t=(1+iu)/2, x=|t|=|1-t| in [1/2,1/sqrt(2)], and v=(1-u^2)/4=1/2-x^2. The exact identity

    q(z)=(1-tz)(1-(1-t)z)+v z^2

implies on |z|=1

    |tq(z)/(1-tz)|
      <=x(1+x)+x(1/2-x^2)/(1-x)
      =x(3/2-2x^2)/(1-x)<=3/2.

To check the last inequality, 2x^3-3x+3/2 decreases on the stated interval and its terminal value is 3/2-sqrt(2)>0. Also

    |(1-t)(1-tz)|^(-1)
      <=2/(1-1/sqrt(2))<8.

The integration interval has length two. Cauchy's coefficient bound therefore gives |(eF)_i|<=16 n!(3/2)^n. Multiplying by r^i and summing squares proves the first term of E0.

For the exponential residual use |z|=r. Then |q(z)|<=2+r=rM and exp(1-t+tr)<=exp(r)<9 for 0<=t<=1. The integral of t^n is 1/(n+1). Cauchy's bound for coefficient n+i, multiplied by r^i, is at most 9M^n/(n+1). The stated constant 27 is a permissible weakening. Both bounds concern the full residual functions, not their first Taylor terms.

### 9.4 Finite differential operators and reconstruction losses

On polynomials of degree d, ||D^l||_2=d!/(d-l)!. Since binom(n,l)l!<=n^l, the finite binomial expansion gives

    ||(D+1)^n||_2<=sum_l binom(d,l)n^l=(n+1)^d.

Similarly binom(n+l-1,l)l!<=(n+d)^l gives

    ||(D+1)^(-n)||_2<=(n+d+1)^d=(n+b)^d.

If B=(z-1)v, partial sums of its coefficients recover v, so ||v||_2<=b||B||_2. Multiplication by z-1 has norm at most two. Since ||D_r||_2=r^d and ||D_r^(-1)||_2=1, the upper and lower bounds L,U and the residual bound E in Section 4 follow. In particular the lower bound uses the forward estimate

    Fminus<=||D_r fP||_2<=9M^n r^d Hplus b||Psi(1,0)||_2.

This retains both diagonal scalings and all polynomial-reconstruction losses.

### 9.5 Explicit relative correction

Expanding 2(2n)^b E/L gives three positive terms. Their respective exponential factors are

    (M/2)^n/n!, (3/4)^n, (M/2)^n/n!.

Their prefactors, in the same order, are

    A1=18(2n)^b b r^d Hplus(2n+1),
    A2=576(2n)^b b sqrt(b) r^(2d)
                       Hplus Hminus K0(2n+1),
    A3=972(2n)^b b sqrt(b) r^d
                       Hplus Hminus K0(2n+1)/(n+1).

Each is at most n^(10b) on the stated range. One explicit exponent ledger is as follows: constants 18,576,972 are at most n; b sqrt(b)<=n; 2n+1<=n^2; (2n)^b<=n^(3b/2); Hplus,Hminus<=n^(3d/2); r^(2d)<=n^(d/2); and K0<=n^(2b). For A2 and A3 these give exponent at most 7b+1/2<=10b, even on discarding the denominator n+1 in A3. A1 has fewer factors and satisfies the same bound.

The slow-growth assumption gives

    10b log n<=n/20.

Also log(3/4)<=-1/4. The elementary integral bound log(n!)>=n log n-n gives n!>=(n/3)^n. Since M/2<3/2 and n>=16,

    (M/2)^n/n! <=(9/(2n))^n<=exp(-n).

Thus each of the three terms is at most exp(-n/5), and

    2(2n)^b E/L<=3exp(-n/5)<=exp(-n/8).

This completes the uniform relative-error estimate, including all b dependence. Consequently the full-coefficient rank-one bound in Section 5 holds with the stated exp(-n/8) correction for every allowed weight system wmin>=(2n)^(-b).

## 10. Completed outcome and limitations

Conditional on the explicitly provisional exact contact reduction, the estimates of Sections 2–7 now have complete uniform proofs in n>=16, 2<=b<=n, n>=512b^4 log n. The two actual endpoint forcing columns, diagonal scaling, finite derivative inverse, and reconstruction of all three polynomials are included. The lift is within the stated exponentially small relative correction of a rank-one map oriented along (1,e+pi).

This result does not assert favorable center-pair limits. In particular, the correction is small relative to an enormous first column; its absolute bound E need not be small. The exact rational center, its reduced denominator, the complete pi-error term, and the Schur complement remain essential. No denominator estimate is inferred from the orientation bound. Child 4 retains that arithmetic and the independent examination of contact normality.

The existing interface file labels its estimates as planned; this completed note supplies their proof. Child 2's multi-row complete functional can use the actual B lift and the precise Sigma/G normalization in Section 7. For b=2 the multi-row subtraction is unavailable and is not assumed. No new HP indices or checker replays are needed for these paper arguments.
