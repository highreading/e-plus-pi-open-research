> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Signed adjoint contraction of the complete forcing

New author research, not an audit. The completed directional and multirow records are preserved. No controls, scans, or earlier computations are repeated. CONTACT_INVERSE_RESEARCH.md, including its completion Section 9, was already read; its quantitative inverse estimates remain separate author inputs. Normality is used only in the accepted range stated below.

The new analytic result is a uniform bound on the complete arctangent forcing on circles approaching radius sqrt(2). It replaces the earlier n!(3/2)^n forcing factor by a polynomial multiple of n!. The adjoint contraction is written and estimated directly before the inverse input is used to eliminate its remaining coefficient norm. The resulting conditional directional envelope is

    |t-(e+pi)| <= 2 n^(8b) 2^(-n).

Uniformly on the accepted slow-growth range, its logarithm is at most -n log 2+o(n). This improves the previous -n log(4/3)+o(n) envelope. It is an upper bound, not a signed asymptotic or a nonvanishing theorem.

## 1. Fixed factorial norm, including the b=2 boundary

Assume

    n>=16, 2<=b<=n, n>=512 b^4 log n,

with natural logarithms. Put

    m=floor((b-1)/2),
    r0=n+m+1-b,
    w_j=r0!/(n+m+1-j)!, 0<=j<=b,
    W=diag(w_0^2,...,w_b^2).

The coefficient vectors are the ordinary ascending coefficients of the ACTUAL polynomial B, including its endpoint constant. The norm is exactly

    ||B||_W^2=sum_(j=0)^b [r0!/(n+m+1-j)!]^2 B_j^2.

In particular w_b=1, wmin=w_0, and wmin>=(2n)^(-b). Indeed 1/w_0 is a product of b integers at most n+m+1<=2n. The factorial weights are squared in W; there is no unsquared-weight convention here.

For b>=3 this is the completed multirow norm with the maximal allowed m. For b=2, m=0 and r0=n-1. These are the unsubtracted factorial-tail weights. No nonexistent high-row cancellation is asserted for b=2. All arguments below use the forcing integrals and apply to this boundary as well.

This B norm is positive definite on the two-dimensional solution space because its B-coefficient map is injective. It is exactly the B-only norm in the earlier directional note. Scalar multiplication of W would not change its center, but the displayed normalization is fixed throughout this note.

## 2. Actual lift and its reconstructed adjoint

Use xi as the Taylor variable and put

    q0(xi)=1-xi+xi^2/2,
    G_n(xi)=exp(xi)q0(xi)^n,
    T_ij=[xi^(n+i-j)]G_n(xi), 0<=i,j<b.

The rational forcing columns are

    (f_P)_i=[xi^(n+i)]q0^n D^n(1/(1-xi)),
    (f_Q)_i=[xi^(n+i)]q0^n D^n((exp(xi)+F(xi))/(1-xi)),
    F(xi)=4 arctan(xi/(2-xi)).

The exact contact reduction is the input supplying T and these two columns. Its normality makes T invertible in the accepted range.

Let D be differentiation on polynomials of degree less than b, in ascending coefficient coordinates. Define the finite reconstruction operator

    H=(I+D)^(-n)
      =sum_(l=0)^(b-1) (-1)^l binom(n+l-1,l)D^l.

Its entries, for 0<=i,j<b, are

    H_ij=(-1)^(j-i) binom(n+j-i-1,j-i) j!/i!  if j>=i,
    H_ij=0 otherwise.

Let D_B be multiplication by xi-1 from degree less than b to degree at most b:

    (D_B)_jl=1_(j=l+1)-1_(j=l).

Fix

    K=D_B H.

Thus K includes BOTH the finite differential reconstruction and multiplication by xi-1. It is not merely a selector of transformed coefficients. With e_0=(1,0,...,0)^T in Q^(b+1), the two actual B-lift columns are

    u=K T^(-1)f_P,
    v=e_0+K T^(-1)f_Q.

For endpoint data (P,Q), the actual B vector is Pu+Qv. In particular sum u_j=0 and sum v_j=1.

Define

    a=u^T W u>0,
    h=u^T W v,
    t=h/a,
    z=T^(-T)K^T W u.

The symbol z denotes this b-dimensional adjoint vector only. The previous directional note's transverse B vector will be denoted z_perp=v-tu to avoid confusion.

The exact adjoint normalization is

    z^T f_P=a.

Put

    lambda=z/a,
    c0=u^T W e_0/a=w_0^2 u_0/a.

Then lambda^T f_P=1. The rational center is precisely the previously specified weighted center, and its signed identity is

    t-S=c0+lambda^T(f_Q-S f_P), S=e+pi.              (1)

Neither the endpoint constant e_0 nor its factorial weight may be dropped.

## 3. Complete signed forcing integrals

For -1<=y<=1 write tau_y=(1+iy)/2. The complete difference quotients give

    q0^n D^n((exp(xi)-e)/(1-xi))=-E_n(xi),
    E_n(xi)=q0(xi)^n integral_0^1 s^n exp(1-s+s xi) ds,

and

    q0^n D^n((F(xi)-pi)/(1-xi))=-A_n(xi),
    A_n(xi)=n! integral_-1^1
       [tau_y q0(xi)/(1-tau_y xi)]^n
       /[(1-tau_y)(1-tau_y xi)] dy.                 (2)

These are the full functions, not first omitted Taylor terms. They are analytic for |xi|<sqrt(2). E_n is entire. The arctangent integral retains both conjugate endpoints and its original orientation. Although the outer signs in (2) are both negative, their contracted values need not be positive.

For any analytic g define the scalar adjoint coefficient functional

    C_lambda(g)=sum_(i=0)^(b-1) lambda_i [xi^(n+i)]g.

With Lambda(w)=sum_i lambda_i w^i, Cauchy's formula gives, for an admissible circle of radius rho,

    C_lambda(g)=(1/(2pi)) integral_-pi^pi
       rho^(-n) exp(-in theta)
       Lambda(rho^(-1)exp(-i theta))
       g(rho exp(i theta)) dtheta.                 (3)

Equations (1)-(3) give the complete SIGNED contraction

    t-S=c0-I_E-I_A,
    I_E=C_lambda(E_n), I_A=C_lambda(A_n).           (4)

In particular the same-circle integral may combine E_n+A_n before any absolute value. Conjugation of theta and y shows I_E,I_A are real. This does not assign either one a sign.

Equation (4) is the actual adjoint identity, not a definition of an unknown error constant. The next sections give explicit bounds for its integrals. The normalization lambda^T f_P=1 is retained throughout.

## 4. A new uniform kernel bound on the larger circle

Set R=sqrt(2). For every -1<=y<=1 and every |xi|<=R,

    |tau_y q0(xi)/(1-tau_y xi)|<=R,                 (5)

where the removable endpoint singularities are understood by continuity.

Proof. On |xi|=R, put x=Re(xi)-1. Then

    q0(xi)/xi=R cos(theta)-1=x,
    |q0(xi)|=R|x|.

The reciprocal omega=1/tau_y lies on the right semicircle

    |omega-1|=1, Re(omega)>=1.

If x<=0, horizontal separation gives

    |omega-xi|>=Re(omega)-Re(xi)>=-x.

If x>=0, then |xi-1|^2=1-2x, and the reverse triangle inequality gives

    |omega-xi|>=1-sqrt(1-2x)>=x.

The last inequality follows from sqrt(1-2x)<=1-x; here 0<=x<=R-1. Since

    tau_y q0(xi)/(1-tau_y xi)=q0(xi)/(omega-xi),

the asserted boundary bound follows. For |y|<1 the function is analytic on a neighborhood of the closed disk. For y=+1 or -1 its pole at 1/tau_y is a root of q0 and cancels, leaving a polynomial. The maximum modulus principle therefore proves (5) throughout the disk, uniformly in y. This also resolves the zero-over-zero boundary points.

The constant R cannot be decreased in this uniform modulus lemma: at y=1 and xi=-1-i, the modulus equals R; the conjugate point gives the other equality. This sharpness is about (5), not about the signed coefficient contraction.

The old radius-one majorant supplied a factor (3/2)^n. Inequality (5) permits a Cauchy circle near R; its R^n is canceled by the radius contribution for the coefficient index n+i. This is the new analytic saving.

## 5. Direct bounds on the actual adjoint contraction

Define the explicit angular norm

    N_lambda(rho)=(1/(2pi)) integral_-pi^pi
          |Lambda(rho^(-1)exp(-i theta))| dtheta.

Choose

    rho=R(1-1/n), epsilon=1-1/n.

On this circle, |tau_y|<=1/R and |1-tau_y|>=1/2, so

    |1-tau_y xi|>=1/n,
    |[(1-tau_y)(1-tau_y xi)]^(-1)|<=2n.

The y interval has length two. From (2) and (5),

    |A_n(xi)|<=4n n! R^n.

Applying (3) only after the complete y integral has been retained proves

    |I_A|<=4n n! epsilon^(-n) N_lambda(rho).         (6)

Thus (4) also yields the signed-error interval

    c0-I_E-BA <= t-S <= c0-I_E+BA,
    BA=4n n! epsilon^(-n)N_lambda(rho).              (7)

No dominance of c0-I_E over BA is asserted. I_E still has its complete integral in (2)-(3).

For a completely explicit scalar norm, put

    J_lambda^2=sum_(i=0)^(b-1) 2^(-i)lambda_i^2.

This square is rational. Parseval and Cauchy-Schwarz give

    N_lambda(R)<=J_lambda,
    N_lambda(rho)<=epsilon^(-(b-1))J_lambda.

Since b-1<=n-1 and (1-1/n)^(-n)<=4 for n>=2,

    epsilon^(-(n+b-1))<=16.

Consequently

    |I_A|<=64n n! J_lambda.                         (8)

This estimate is for the contracted adjoint polynomial. It is not obtained by taking absolute values of each forcing coefficient and then inserting the previous operator bound.

For E_n use the radius R directly. The elementary bounds

    |q0(xi)|<=2+R=R(1+R),
    |exp(1-s+s xi)|<=exp(R)<9,
    integral_0^1 s^n ds=1/(n+1)

give, with M0=1+R,

    |I_E|<=9 M0^n J_lambda/(n+1).                   (9)

Both forcing contributions and their signs were displayed in (4) before these estimates. Combining them only now gives the unconditional adjoint-level inequality

    |t-S|<=|c0|
       +[64n n!+9M0^n/(n+1)]J_lambda.              (10)

It is conditional only on the exact lift and forcing identities, not on a quantitative inverse estimate. The sharper signed form (7) remains available. The new factor in (8) is polynomial in n, in place of the earlier exponential arctangent forcing factor.

## 6. Separately propagating the author inverse input

This section uses Child 3's quantitative inverse estimate as a separate author input. It is not reproved here. Set d=b-1 and retain its explicit constants

    Cint=(16 b^2 n)^d binom(2d,d)/(d!)^2,
    K0=2048 b sqrt(n) Cint,
    Hplus=(n+1)^d, Hminus=(n+b)^d,
    Fminus=n!2^n/(2n+1),
    L=Fminus/[9b R^d Hplus M0^n].

With D_R=diag((-R)^i), i=0,...,b-1, the author estimates are

    ||D_R T^(-1)D_R^(-1)||_2<=K0 M0^(-n),
    ||u||_2>=L,
    ||H||_2<=Hminus.

They imply sqrt(a)>=wmin L. Multiplication by xi-1 has norm at most two, hence ||K||_2<=2Hminus.

The adjoint scaling is exact:

    D_R^(-1)z
       =(D_R T D_R^(-1))^(-T)D_R^(-1)K^T W u.

Since ||D_R^(-1)||_2=1 and ||W u||_2<=sqrt(a), it follows that

    J_lambda=||D_R^(-1)z||_2/a
       <=2Hminus K0/[M0^n sqrt(a)].                (11)

Also

    |c0|<=w_0/sqrt(a).

Inserting (11) into the NEW contraction estimate (10), rather than the previous forcing majorant, proves

    |t-S|<=Bactual,
    Bactual=[w_0+128n Hminus K0 n!/M0^n
                   +18Hminus K0/(n+1)]/sqrt(a).   (12)

All quantities in (12) are explicit coefficient or author-inverse data. This is an analytic upper bound, not |S-t| renamed. The denominator sqrt(a) is the actual norm of the reconstructed first column.

For a bound independent of that column, define

    C=9b R^d Hplus(2n+1)/wmin.

Using the valid LOWER bound sqrt(a)>=wmin L yields

    |t-S|<=Bexplicit,
    Bexplicit=C {128n Hminus K0 2^(-n)
       +[w_0+18Hminus K0/(n+1)](M0/2)^n/n!}.       (13)

Every dependence on b, the factorial weights, diagonal scaling, and finite reconstruction is retained. The endpoint constant contributes the w_0 term. The exponential integral contributes the term with 18/(n+1). The arctangent integral contributes the 128n term. None is discarded.

The use of the inverse norm in (11) is a final propagation step. The substantive new estimate is the direct complete-kernel and adjoint bound (5)-(8); merely inserting the old forcing norm into (11) would not prove (12)-(13).

## 7. Uniform exponent ledger on the accepted range

The accepted range implies n>16384 and b<=n^(1/4). Child 3's completed author bounds include K0<=n^(2b). The following deliberately coarse ledger suffices to simplify (13).

First,

    9b(2n+1)<=n^2,
    R^d Hplus<=(4n)^d<=n^(2d),
    wmin^(-1)<=(2n)^b<=n^(3b/2).

Thus C<=n^(4b). Also

    Hminus<=(2n)^d<=n^(2d),
    128n<=n^2.

The coefficient of 2^(-n) in (13) is therefore at most

    n^(4b) n^(2b-2) n^(2b) n^2=n^(8b).

Since w_0<=1 and Hminus K0>=1,

    C[w_0+18Hminus K0/(n+1)]
       <=19 C Hminus K0<=n^(8b).

Finally n!>=(n/3)^n, M0/2<3/2, and n>=16 give

    (M0/2)^n/n! <=(9/(2n))^n<=2^(-n).

Consequently the new conditional uniform bound is

    |t-(e+pi)|<=2 n^(8b) 2^(-n).                   (14)

Here the bound is uniform in all admissible b, including b=2. More precisely,

    8b log n/n
      <=(8/512^(1/4))(log n/n)^(3/4) ->0

uniformly over the accepted range. Hence

    |t-(e+pi)|<=exp(-n log 2+o(n)).                 (15)

As an explicit finite-range weakening, the same assumptions give

    8b log n<=n/(64b^3)<=n/512,

so the right side of (14) is at most

    2 exp(-(log 2-1/512)n).

This improves the previous exp(-log(4/3)n+o(n)) envelope by an exponential factor at the upper-bound level. The improvement originates in the complete arctangent kernel, with all b-dependent amplification already included. It does not establish that the actual error has this rate or a definite sign.

## 8. What remains unresolved about signs and leading terms

The exact signed quantity remains

    c0-C_lambda(E_n)-C_lambda(A_n).                 (16)

The proof above controls it quantitatively by a new envelope; it does not prove a nonzero signed leading coefficient. The real contractions C_lambda(E_n) and C_lambda(A_n) need not have the signs of their outer integral prefactors.

A possible boundary expansion of the arctangent contraction would have to control the adjoint polynomial at the two conjugate modulus-maximizing points xi=-1+i and xi=-1-i. Its coefficient factor contains

    Lambda((-1-i)/2), Lambda((-1+i)/2),

respectively, together with their real oscillatory combination. The normalization lambda^T f_P=1 supplies no lower bound on either evaluation or on their signed sum. Higher Taylor terms could dominate if these evaluations vanish or nearly cancel. The same issue remains for comparison against c0-I_E.

No leading-term expansion is promoted: a uniform relative remainder requires a lower bound for that actual signed leading combination, which has not been proved. The exact unresolved functional is (16), or equivalently the arctangent integral in (2)-(3) after retaining its actual Lambda factor and the other two signed terms. This is a precise stopping boundary for a signed asymptotic, not a replacement of the new upper bound by an unknown constant.

The contour kernel bound (5) is sharp as a uniform modulus statement. An improvement beyond the present coefficient envelope would need information about the adjoint polynomial, the signed y/theta integral, or both. Optimizing a discarded high-row product is not involved.

## 9. Complete directional form and primitive-pair interface

Keeping the exact longitudinal coefficient gives, for every real P,Q,

    |P+Q(e+pi)|<=|P+tQ|+Bexplicit |Q|,

and the same statement with the larger elementary envelope in (14). This is a COMPLETE form estimate: both exponential and arctangent residual forcing, and the endpoint constant, enter its derivation.

If the rational center is t=p/q in lowest terms and qx+py=1 with |y|<=q/2, the earlier center pair retains

    |q(e+pi-t)|<=q Bexplicit,
    |1/q+y(e+pi-t)|<=1/q+(q/2)Bexplicit.

No estimate for this actual reduced q is made here; that arithmetic belongs to Child 4. No recurrence for the center is developed; that belongs to Child 3. These formulas only identify the unchanged interface with the new analytic budget.

Each integral lift multiplies its rational coefficients, full remainder, and its own endpoint gcd by the same radial factor. Primitive reduction cancels that factor separately for each direction. No lift denominator, coefficient clearer, or endpoint-lattice index is substituted for q.

## 10. Status and scope

New unconditional analytic deductions from the exact forcing setup: the kernel lemma (5), the signed adjoint integral (4), and the direct scalar contraction bounds (6)-(10). New conclusions conditional on the separate author inverse input: (12)-(15), with an improved uniform exponential envelope and all b dependence displayed.

There is no scan, old-check replay, independent review, new center recurrence, or denominator computation. Earlier directional and multirow results are preserved. No shrinking primitive pair, full-error nonvanishing, or irrationality conclusion is claimed.

The companion file is SIGNED_ADJOINT_REMAINDER_REPORT.md. Completion requires reading back both saved deliverables.
