> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Joint dual Hankel identity and an even-degree root-product theorem

Date: 2026-09-13. Original continuation by audit_computations.
Independent review passed in
`raw_joint_hankel_even_root_product_independent_review.md`.
No irrationality conclusion is claimed.

This note resolves the factorial distinction between the two Rodrigues
representations in `raw_dual_endpoint_error_integrals.md`. It derives an
exact varying Hankel functional and its Pearson identity. An accretive
Toeplitz representation gives an all-even-degree normality and root-product
theorem for the actual primitive dual polynomial. The already saved n=2
example disproves the proposed common sign cone on the integration paths.
The earlier dual-cofactor and whole-error notes were inspected first.
No positive orthogonal-polynomial theorem is imported.

## 1. The factorial distinction and the exact differential identity

Fix n>=1, retaining the reviewed definitions and cofactor signs:

    W(t)=sum_(k=n)^(3n) w_k t^k=t^n(t-1)^n V(t),
    T(t)=sum_(r=0)^(2n) (n+r)! w_(n+r) t^r,
    S(t)=(1+t^2)^n U(t),       D^n S=T,
    Borel(T)=D^n W.                                           (1)

Here V is primitive, integral, nonzero, and of degree at most n;
U is integral and nonzero, with degree at most n and (n+j)! dividing
u_j=[t^j]U. No exact degree or endpoint nonvanishing is initially assumed.

D^n S and D^n W are NOT equal in general. The joint equation is
Borel(D^n S)=D^n W. The polynomial

    S0(t)=sum_(r=0)^(2n) r! w_(n+r) t^(n+r)

satisfies deg(S-S0)<n. Consequently, for k>=n,

    [t^k]W=[t^k]S/(k-n)!.                                    (2)

Define the even polynomial and polynomial reversal

    H_n(x)=sum_(h=0)^n binom(n,h) x^(2h)/(2h)!,
    q_n(z)=z^n U(1/z)=sum_(j=0)^n u_(n-j) z^j.                (3)

Direct expansion gives W(x)=x^n sum_j u_j H_n^(n-j)(x): the
contribution from u_j binom(n,h) is exactly x^(j+2h)/(j+2h-n)!
when j+2h>=n, and zero otherwise. Equation (2) therefore proves

    q_n(D) H_n(x)=(x-1)^n V(x).                               (4)

It does not identify the two ordinary antiderivatives. Direct summation
also gives the formal generating identity

    sum_(n>=0) H_n(x) z^n
       =(1-z)^(-1) cosh(x sqrt(z/(1-z))).                     (5)

This is not a positive-measure representation for the next functional.

## 2. The actual finite Hankel functional and uniqueness

Define

    mu_n(p)=[z^(2n)] e^z(1+z^2)^n p(z),
    h_l=mu_n(z^l)=H_n^(l)(1)
       =sum_(h>=ceil(l/2))^n binom(n,h)/(2h-l)!.              (6)

The coefficient identity follows by replacing h by n-h; empty sums
are zero, so h_l=0 for l>2n. Differentiating (4) at x=1 yields

    mu_n(z^s q_n)=0,                      0<=s<n,
    mu_n(z^s q_n)=s! V^(s-n)(1)/(s-n)!,   s>=n.              (7)

Both sides vanish for s>2n. Thus q_n is in the kernel of the
n-by-(n+1) matrix (h_(s+j)), 0<=s<n, 0<=j<=n.

This kernel has dimension one. Indeed, any q in it reverses to U
and defines S=(1+t^2)^n U. Define W by (2). Then W=x^n q(D)H_n
has zeros of order n at 0 and 1. Also T=D^n S has the first n raw
Legendre moments zero, by n integrations by parts and the order-n
zeros of S at -i and i. Undoing factorials gives a left annihilator
of the original X_n. This map is injective: T=0 would force deg S<n,
impossible for nonzero U. The previously proved full column rank of
X_n proves the dimension claim. No principal-minor assumption is used.

In particular,

    mu_n(q_n^2)=n! U(0) V(1).                                (8)

All coefficients of q below degree n disappear by (7), leaving
q_(n)=U(0). This formula includes degree drops and zero values; it
does not assert positive definiteness or quasi-definiteness.

## 3. Pearson identity and the finite moment recurrence

The functional is the residue at zero against
rho_n=e^z(1+z^2)^n/z^(2n+1). Set

    sigma=z(1+z^2),       tau_n=z^3+2z^2+z-2n.

The derivative of a meromorphic Laurent series has residue zero.
Applying this to sigma p rho_n proves, for every polynomial p,

    mu_n(sigma p' + tau_n p)=0.                              (9)

The constants follow from

    rho_n'/rho_n=1+2nz/(1+z^2)-(2n+1)/z,
    sigma'+sigma rho_n'/rho_n=tau_n.

Taking p=z^k gives

    h_(k+3)+(k+2)h_(k+2)+h_(k+1)+(k-2n)h_k=0,   k>=0.       (10)

This supplies a varying semiclassical structure. A polynomial ladder
that divides by neighboring Hankel minors must still verify that
those particular minors are nonzero; (9) does not do so automatically.

## 4. An even-degree accretive Toeplitz representation

Assume n=2m>=2. Put a_k=[z^k]e^z(1+z^2)^n, with a_k=0 for k<0,
and let G=(h_(i+j))_(i,j=0)^n and A=(a_(n+i-j))_(i,j=0)^n.
Reversing the rows of G gives A. Hence (7) becomes

    A q_n=n! V(1) e_0.                                      (11)

The Toeplitz symbol of A is

    f(theta)=e^(e^(i theta))(2cos theta)^n
            =e^(e^(i theta)) |1+e^(2i theta)|^(2m).

For a complex vector c and p(z)=sum c_j z^j,
c*Ac is the integral of f(theta)|p(e^(i theta))|^2/(2pi).
Write A=H+iK with H,K Hermitian. Let G0 be the Toeplitz Gram matrix
of w(theta)=|1+e^(2i theta)|^(2m). Pointwise bounds imply

    e^(-1)cos(1) G0 <= H <= e G0,
    -tan(1) H <= K <= tan(1) H.                              (12)

Since w is positive except at finitely many points, G0 and H are
positive definite. Thus A is invertible. It has real entries, and

    V(1)!=0,       q_n(0)/(n! V(1))=(A^(-1))_(0,0)>0.         (13)

Positivity of this inverse entry is also quantified below. Since
q_n(0)=u_n=(2n)!w_(3n)=(2n)![t^n]V, this proves independently of
any dyadic normality result that

    deg V=deg U=n,       V(1)[t^n]V>0,       for even n.       (14)

It does not imply an interior sign, U(0)!=0, or an arc sign. For
odd n the symbol changes sign and this accretivity argument fails.

## 5. Exact inverse comparison via a binomial Toeplitz determinant

For integers a,b>=0 and L>=1, the elementary determinant identity is

    det_(0<=i,j<L) binom(a+b,a+i-j)
      = product_(j=0)^(L-1) j!(a+b+j)!/[(a+j)!(b+j)!].        (15)

An out-of-range binomial coefficient means zero. Factor
(a+b)!/[(a+i)!(b-i+L-1)!] from row i. The remaining column j is
p_j(x)=(a+x)_j(b-x+L-1)_(L-1-j), evaluated at x=i, with falling
factorials. Each has degree at most L-1. Translating all evaluation
points to x=-a+i leaves the Vandermonde and thus this determinant
unchanged. The latter matrix is lower triangular with diagonal
i!(a+b+L-1-i)!/(a+b)!. Restoring row factors proves (15), including
the zero entries covered by falling factorials.

The even and odd coordinates of G0 decouple. Its even block contains
coordinate zero and has size m+1, with entries binom(2m,m+i-j).
Its inverse corner is the ratio of the size-m and size-(m+1)
determinants in (15), so

    c_m:=(G0^(-1))_(0,0)=((2m)!)^2/[m!(3m)!].                (16)

Set C=H^(-1/2)KH^(-1/2). Equation (12) gives ||C||<=tan(1), and

    Re(A^(-1))=H^(-1/2)(I+C^2)^(-1)H^(-1/2).

Consequently cos^2(1)H^(-1)<=Re(A^(-1))<=H^(-1). Combining
this with (12), and using that the diagonal entry is real, proves

    e^(-1)cos^2(1)c_m <= (A^(-1))_(0,0)
                       <= e/cos(1)c_m.                      (17)

These constants do not depend on m. An entrywise or determinant
approximation has not been substituted for an inverse estimate.

## 6. Actual even-degree root-product asymptotic

Write v_n=[t^n]V, and B_m=(4m)!m!(3m)!/((2m)!)^3. Equations
(13), (16)-(17) give the positive ratio bound

    e^(-1)cos(1)B_m <= V(1)/v_n
                      <= e/cos^2(1)B_m.                     (18)

For n=2m, Stirling's formula therefore gives

    log(V(1)/v_n)=n log n+((3/2)log 3-1)n+O(log n),
    (V(1)/v_n)^(1/n)/n --> 3sqrt(3)/e.                       (19)

The quotient is positive; no complex-root choice is involved. If
r_1,...,r_n are all roots of V with multiplicity, equivalently

    (product_(j=1)^n |1-r_j|)^(1/n)/n --> 3sqrt(3)/e.          (20)

In particular max_j|r_j| >= (3sqrt(3)/e+o(1))n-1. This controls
a root product, not every root or its argument; it does not exclude
roots in (0,1). Since v_n is a nonzero integer, (18) also gives an
actual factorial lower bound on |V(1)| and on ||V||_[0,1]. One
cannot justify a small exponential error by simply asserting that
this primitive polynomial has only exponential uniform height.

The even-degree normality also sharpens the previous arc-absolute-
mass lower bound. In Section 5 of the dual-integral note take d=n
and |u_n|>=(2n)! instead of d<=n and |u_d|>=n!. With that note's
exact positive constants ell and rho0, the same proof gives

    integral_(-pi/4)^(pi/4) F(phi)^n |Re U(t(phi))|dphi
      >= (2n)! ell/(2n+1)(rho0 ell/sqrt(2))^n.                (21)

The separate all-index dyadic proof of w_(3n)!=0 in
`raw_adjacent_dual_cross_and_fixed_gcd.md` has now been independently
accepted, so (21) extends immediately to all n. That extension is
not a premise of the even-degree theorem proved here.

## 7. Existing degree-two data disprove the common sign cone

Use only the already saved primitive polynomials

    V_2(t)=49t^2-64t+940,
    U_2(t)=1176t^2-972t-118,
    q_2(z)=1176-972z-118z^2.

The discriminant of V_2 is negative and its leading coefficient
positive, so V_2>0 on the real line. On the actual left arc
t=1-sqrt(2)e^(i phi), writing x=cos(phi) gives

    Re U_2(t)=4704x^2-1380sqrt(2)x-2266,
                     1/sqrt(2)<=x<=1.                       (22)

Its value at 1/sqrt(2) is -1294. Its value at 1 is
2438-1380sqrt(2)>0, since 2438^2>2*1380^2. Both signs thus
occur in the open arc, where F>0. Changing the global cofactor sign
cannot repair this. Positivity of V therefore does not supply the
previously proposed common sign of V and Re U on both paths.

The same data refute positivity of mu_n even on polynomials of
degree at most n:

    H_2(x)=1+x^2+x^4/24,
    (h_0,h_1,h_2,h_3,h_4)=(49/24,13/6,5/2,1,1),
    mu_2(q_2^2)=2!*(-118)*925=-218300<0.                      (23)

There is no conflict with the Toeplitz result: reversing Hankel
rows is not a congruence preserving quadratic-form positivity.
Also (14) involves U_n whereas (8) involves U(0); confusing those
coefficients would give an incorrect sign conclusion.

## 8. Remaining error and arithmetic targets

With Z=Qhat(1), N=Pe(1)+4Pa(1), and g=gcd(|Z|,|N|), the exact
reviewed whole-error identity remains

    Lambda_n=Z(e+pi)-N
      =(-1)^n [ (1/n!) integral_0^1
                e^(1-t)[t(1-t)]^n V(t)dt
             +2 integral_(-pi/4)^(pi/4) F(phi)^n Re U(t(phi))dphi ],
    primitive endpoint form=sign(Z)Lambda_n/g.               (24)

Equations (4), (7), and (9) constrain the two polynomials jointly.
They do not justify discarding signs or g. The degree-two example
closes the common-sign-cone argument, not a weaker integrated sign
theorem and not a possibility of primitive shrinking after a large gcd.

A concrete next analytic task is to bound this specific linear
functional of the actual Hankel kernel vector. The Pearson recurrence
gives fixed coefficient data for a ladder or second-kind equation,
but any division by adjacent Hankel minors needs proof. The even
Toeplitz inverse comparison may also control further individual
coefficient ratios. Odd n requires a different argument for the
signed symbol. Neither the factorial root product nor the absolute
mass bound excludes a sufficiently large endpoint gcd.

## 9. Bounded controls

`check_raw_joint_dual_existing.py` and
`raw_joint_dual_existing_checks.json` use only the saved n=1,2
cofactor vectors. They check (4), (7)-(10), the n=2 Toeplitz equation
and inverse entry, and the two sign-obstruction calculations. The
all-even proofs (12)-(20) are independent of these controls. No new
canonical degree was solved and no root scan was performed.
