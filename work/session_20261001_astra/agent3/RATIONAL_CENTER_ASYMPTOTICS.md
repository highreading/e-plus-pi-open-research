> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Rational center from two forcing columns: exact formula and signed expansion

Status: new author research, conditional on the previously reported provisional contact inverse and reconstruction estimates. Those dependencies are accepted in their stated scope here; they are not re-audited or recomputed. The exact formulas and new error analysis below use no HP scan. A uniform nonzero leading coefficient is not established.

Throughout,

    n>=16, 2<=b<=n, n>=512 b^4 log n,
    q(z)=1-z+z^2/2, S=e+pi,
    r=sqrt(2), M=1+r, chi=r-1, d=b-1.

All logarithms are natural. The inverse result's full rational coefficient norm is used. Its weights must be fixed as rational construction data, independently of S. The canonical choice for this note is w_j=1. Every formula and bound also applies to any specified rational weights

    0<w_j<=1, wmin=min_j w_j>=(2n)^(-b).

In particular the permitted multi-row weights of Child 2 can be used, but a full-coefficient center must not be silently identified with a B-only center.

## 1. Elementary consequences, separated from the new result

Let f=Phi(1,0), g=Phi(0,1), a=<f,f>_W, h=<f,g>_W, t=h/a. The accepted provisional estimate is

    ||g-Sf||_W<=delta ||f||_W, delta=exp(-n/8).

Cauchy–Schwarz immediately gives |t-S|<=delta. Orthogonal projection gives exactly

    det Gram(f,g)/a^2
      =||g-Sf||_W^2/a-(t-S)^2,

and hence 0<det Gram(f,g)/a^2<=delta^2. Positivity follows from the injective endpoint lift. These are elementary consequences of the prior estimate, not the new asymptotic research.

The new results are: an exact rational center formula using the two forcing columns, a rational separation into exponential and logarithmic companions, and a uniform signed expansion whose unresolved coefficient is explicitly specified without using S.

## 2. Exact rational construction and center formula

Use

    G_n(z)=exp(z)q(z)^n=sum_m g_m z^m,
    T_ij=g_(n+i-j), 0<=i,j<b.

Denote the two forcing columns by u and v, reserving f and g for full triples:

    u_i=[z^(n+i)]q^n D^n(1/(1-z)),
    v_i=[z^(n+i)]q^n D^n((exp(z)+F(z))/(1-z)).

They are rational. Their finite construction is

    u_i=n! 2^(-n) sum_(l=0)^floor(n/2)
                         binom(n,l)binom(2n+i-2l,n+i),

and, for either column,

    forcing_i=sum_(s=0)^min(2n,n+i) q_s
       (2n+i-s)!/(n+i-s)! H_(2n+i-s),
    q_s=[z^s]q(z)^n,

where H_m=1 for u and

    H_m=sum_(j=0)^m (1/j!+[z^j]F)

for v. All factorial arguments are nonnegative.

Let D be differentiation on polynomials of degree less than b, and define rational matrices

    Jinv=(I+D)^(-n)
       =sum_(l=0)^d (-1)^l binom(n+l-1,l)D^l,
    Z_ij=1_(i=j+1)-1_(i=j), 0<=i<=b, 0<=j<b,
    U=Z Jinv.

Here U maps the solved transformed exponential polynomial to the coefficients of its product with z-1. Let e0=(1,0,...,0)^T in Q^(b+1). Solve exactly

    x=T^(-1)u, y=T^(-1)v.

The actual B columns are

    betaP=Ux, betaQ=e0+Uy.                              (1)

The e0 term is the actual endpoint forcing and is retained throughout.

Define a rational reconstruction map R on B coefficient vectors beta by

    C_beta^*(t)=-sum_(k=0)^n ell_beta(p_k)p_k(t)/h_k,
    C_beta(z)=z^n C_beta^*(1/z),
    A_beta=-[B_beta exp(z)+C_beta F(z)]_(degree<=n),
    R beta=(A_beta,B_beta,C_beta).

This map is defined on all B vectors. On the actual relaxed kernel it is the full reconstruction. Thus f=R Ux and g=R(e0+Uy).

Put

    c0=(b+1)(n+1)^2 64^n/[2(n+1-b)!], a0=3+10c0,
    W=diag((wmin/a0)^2 I_A, diag(w_j^2), (wmin/c0)^2 I_C),
    H=R^T W R,
    K=U^T H U, kappa_vec=U^T H e0.

These are rational matrices. The reconstruction coefficient estimates give

    diag(w_j^2)<=H<=3 diag(w_j^2).                       (2)

The bounds use only the finite reconstruction formulas, so also apply before restricting beta to the relaxed kernel. In particular K is positive definite since U is injective.

The exact desired center is

    a=x^T Kx,
    t=(x^T Ky+x^T kappa_vec)/(x^T Kx).                  (3)

No approximation to e, pi, or S enters its definition.

An equivalent determinant formula contains no unspecified choice of pivots. Let Delta=det T, X=adj(T)u, Y=adj(T)v. Then

    t=[X^T KY+Delta X^T kappa_vec]/[X^T KX].             (4)

Normality makes Delta nonzero, and positive definiteness makes the denominator positive. This is a rational formula, not a claim about its reduced denominator.

The structured inputs have short exact recurrences. For q_s^(n)=[z^s]q^n,

    q_s^(n+1)=q_s^(n)-q_(s-1)^(n)+q_(s-2)^(n)/2.

For g_m=[z^m]G_n, with g_0=1 and g_(-1)=g_(-2)=0,

    (m+1)g_(m+1)=(m+1-n)g_m
                 +(2n-m-1)g_(m-1)/2+g_(m-2)/2.

If F(z)=sum_j F_j z^j, then F_0=0, F_1=2, and F'=2/q provides a rational second-order recurrence for its derivative coefficients. The p_k used in R have their usual rational three-term recurrence. Equations (1)–(4), together with these recurrences, give an explicit finite construction for t from the two actual forcing columns.

## 3. A single rational dual polynomial controls the signed error

Define the rational adjoint column and endpoint term

    lambda=T^(-T)Kx/a,
    kappa=x^T kappa_vec/a,
    L(z)=sum_(i=0)^d lambda_i z^i,
    Nlambda=sum_(i=0)^d |lambda_i| r^(-i).

The normalization is exact:

    lambda^T u=1,
    t=kappa+lambda^T v.                                (5)

In particular lambda is nonzero and Nlambda>0. The polynomial L and kappa are computed from rational construction data alone.

Use the two full residual columns from the inverse result:

    v=S u+e_E+e_F.

Then

    t-S=kappa+epsilon_E+epsilon_F,
    epsilon_E=lambda^T e_E, epsilon_F=lambda^T e_F.       (6)

The endpoint term kappa, the exponential contribution, and the logarithmic contribution must all be retained. Their signs are not assumed.

## 4. Exact rational companions

Define the rational polynomial

    P_E(s)=sum_i lambda_i [z^(n+i)]q(z)^n exp(sz).

It has degree at most n+b-1. The complete exponential contribution is exactly

    epsilon_E=-integral_0^1 s^n exp(1-s)P_E(s) ds.        (7)

Writing P_E(s)=sum_l p_l s^l, normalization (5) implies

    sum_l p_l(n+l)!=1.

Since

    integral_0^1 s^N exp(1-s) ds
       =N![e-sum_(j=0)^N 1/j!],

we obtain the rational exponential companion

    r_E=sum_l p_l(n+l)! sum_(j=0)^(n+l)1/j!,
    epsilon_E=r_E-e.                                    (8)

For the logarithmic part put V(z)=z^2-z+1/2 and

    P_F(z)=z^n D_z^n[V(z)^n L(z)].

This is a rational polynomial of degree at most 2n+b-1. Coefficient comparison with the forcing formula proves

    P_F(1)=lambda^T u=1.

For t_u=(1+iu)/2,

    epsilon_F=-integral_-1^1 P_F(t_u)/(1-t_u) du.         (9)

Consequently

    r_F=integral_-1^1 [1-P_F(t_u)]/(1-t_u) du

is rational: the quotient is a rational polynomial, and each segment monomial moment is rational. Explicitly,

    integral_-1^1 t_u^m du
       =2^(-m) sum_(j even,0<=j<=m)
                    2 binom(m,j)(-1)^(j/2)/(j+1).

Since integral_-1^1 (1-t_u)^(-1)du=pi,

    epsilon_F=r_F-pi,
    t=kappa+r_E+r_F.                                   (10)

This exact separation uses neither the unknown S nor the signed error to define either rational companion.

## 5. A uniform exponential endpoint expansion

Let

    C_j=(-1)^j [(D_s-1)^j P_E(s)]_(s=1).

These coefficients are rational. For j<b they are available directly from the solved b-dimensional data:

    C_j=sum_(l=0)^j (-1)^l binom(j,l)(Kx)_l/a.           (11)

Indeed P_E^(l)(1)=lambda^T T e_l=(Kx)_l/a when l<b. For larger j the finite coefficients q_s and g_m still define C_j exactly; no extension of a factorial to a negative argument is required.

For every positive integer J, repeated integration by parts in (7) gives

    epsilon_E=-sum_(j=0)^(J-1) C_j/(n+1)_(j+1)+R_E,J,  (12)

where (n+1)_l=(n+1)(n+2)...(n+l) is a rising factorial. The exact remainder has the derivative of order J of exp(1-s)P_E(s) under an integral. On |z|=r,

    |q(z)|<=rM, |1-z|<=M,
    exp(1-s+s Re z)<=exp(r)<9, 0<=s<=1.

Cauchy's coefficient estimate therefore gives

    sup_(0<=s<=1)|D_s^J[exp(1-s)P_E(s)]|
       <=9 Nlambda M^(n+J).

It follows that

    |R_E,J|<=9 Nlambda M^(n+J)/(n+1)_(J+1).             (13)

This remainder is uniform in n,b,J. For J<=b, all displayed coefficients in (12) use the actual columns in (11). It is an additive asymptotic expansion; no first C_j is presumed nonzero.

## 6. A new real-arc representation for the logarithmic contribution

The polynomial identity defining P_F is useful because V(t_u)=(1-u^2)/4 vanishes at both segment endpoints. Integration by parts n times in (9) has no boundary terms: derivatives through order n-1 of V^n L vanish at both endpoints. Also

    D_z^n[z^n/(1-z)]=n!/(1-z)^(n+1).

Hence

    epsilon_F=(-1)^(n+1)n! integral_-1^1
                 V(t_u)^n L(t_u)/(1-t_u)^(n+1) du.     (14)

The only pole of this rational integrand is at z=1. Deform the segment to the left circular arc

    z(theta)=1-r^(-1)exp(i theta),
    -pi/4<=theta<=pi/4.

The region between the segment and this arc excludes z=1. Keeping the direction of traversal and du=2dt/i gives exactly

    epsilon_F=(-1)^(n+1)2n! integral_(-pi/4)^(pi/4)
          [r cos theta-1]^n L(1-r^(-1)exp(i theta)) dtheta.    (15)

Indeed V(z)/(1-z)=r cos theta-1, and the transformed differential divided by 1-z contributes the factor 2. Conjugation symmetry allows L in (15) to be replaced by its real part. The scalar weight is nonnegative throughout this arc.

This identity retains both conjugate endpoints. It does not assert that the polynomial factor has a fixed sign. It concerns the dual polynomial from the actual center, not an arbitrary Borel-transformed high block from earlier investigations.

## 7. Uniform additive saddle expansion with an explicit coefficient

Put

    zstar=1-r^(-1),
    c=r/(2chi)=(2+r)/2,
    A_n=2n! chi^n sqrt(pi/(c n)).

The coefficient L(zstar) is an algebraic number obtained by evaluating the rational polynomial L. Its definition does not use S. The factor sqrt(pi) is the ordinary Gaussian integral constant, not a definition through the target error.

The following uniform estimate follows from (15):

    epsilon_F=(-1)^(n+1) A_n [L(zstar)+R_F],
    |R_F|<=(12+d^2)Nlambda/n, n>=16.                    (16)

Here are quantitative details rather than a fixed-b extrapolation. Write

    h(theta)=r cos theta-1,
    J_n=integral_(-pi/4)^(pi/4) h(theta)^n dtheta.

On this interval |theta|<1 and h/chi<=exp(-theta^2). For |theta|<=1/2, let y=(r/chi)(1-cos theta). Then y<=2theta^2<=1/2 and

    |log(h/chi)+c theta^2|<=5theta^4.

This follows from |y-c theta^2|<theta^4/6 and

    0<=-log(1-y)-y<=y^2/[2(1-y)]<=4theta^4.

Both h^n/chi^n and exp(-cn theta^2) are at most exp(-n theta^2). Their difference on the central interval is therefore at most 5n theta^4 exp(-n theta^2). Integrating and bounding both outer Gaussian tails gives

    |J_n/[chi^n sqrt(pi/(cn))]-1|<=10/n.                (17)

For example, the central relative error is at most 15sqrt(c)/(4n)<6/n. The outer relative error is at most 4exp(-n/4)/sqrt(n)<=4/n for n>=16. These estimates prove (17) directly.

Along the arc, |z(theta)|<=r^(-1). Differentiating L(z(theta)) twice gives the bound

    |D_theta^2 L(z(theta))|<=d^2 Nlambda.

Its first derivative at zero is purely imaginary. Thus

    |Re L(z(theta))-L(zstar)|<=d^2 Nlambda theta^2/2.

Using h^n<=chi^n exp(-n theta^2), the integral of this difference, divided by chi^n sqrt(pi/(cn)), is at most

    d^2 Nlambda sqrt(c)/(4n)<d^2 Nlambda/(2n).

Together with |L(zstar)|<=Nlambda and (17), this proves the weaker, convenient constant in (16). No estimate differentiates a growing-degree polynomial while hiding its degree dependence; it is explicitly d^2/n.

The asymptotic assertion is on the common additive scale A_n Nlambda. It becomes a relative asymptotic with a nonzero leading term only after an additional lower bound for |L(zstar)|/Nlambda has been proved.

## 8. Combining both components, including their cancellation

Equations (6), (12), and (16) give, for every J>=1,

    t-S=kappa+(-1)^(n+1)A_n L(zstar)
          -sum_(j=0)^(J-1) C_j/(n+1)_(j+1)+R_J,

    |R_J|<=A_n(12+d^2)Nlambda/n
               +9Nlambda M^(n+J)/(n+1)_(J+1).          (18)

This is a rigorous two-sided additive enclosure for the signed error. The first three displayed terms are explicitly computable without S. It retains cancellation of the actual endpoint term, the exponential contribution, and the logarithmic contribution. A short exponential truncation is not assumed to determine the sign.

A useful stronger comparison shows that kappa and the entire exponential contribution are factorially smaller than the logarithmic envelope A_n Nlambda in the slow-growth range. Let zK=K^(-1)kappa_vec. The vector U zK is the H-orthogonal projection of e0 onto range U. From (2),

    ||U zK||_H<=||e0||_H<=sqrt(3)w_0,
    ||U zK||_2<=sqrt(3)/wmin.

The accepted finite reconstruction bounds give

    ||D_r zK||_2<=sqrt(3)b r^d(n+1)^d/wmin.

Since lambda^T T=x^T K/a,

    kappa=lambda^T T zK,
    |kappa|<=18b r^d(n+1)^d M^n Nlambda/wmin.            (19)

The inverse result's forward scaled norm bound, rather than a new inverse estimate, is used here. Formula (7) and the same Cauchy bound as above give

    |epsilon_E|<=9Nlambda M^n/(n+1).                    (20)

Consequently

    |kappa+epsilon_E|<=A_n Nlambda rho_(n,b),

    rho_(n,b)=[18b r^d(n+1)^d/wmin+9/(n+1)] M^n/A_n.   (21)

This explicit positive expression is preferable when selecting parameters. It also satisfies the convenient uniform bound

    rho_(n,b)<=exp(-n).                                 (22)

To see this, M/chi=M^2<6 and sqrt(cn/pi)/2<=sqrt(n). The prefactor in (21), using wmin^(-1)<=(2n)^b and d=b-1, is at most n^(4b+3) throughout the assumed range. Thus

    rho_(n,b)<=n^(4b+3)(18/n)^n.

The range implies n>16384, 4b+3<=6b, and 6b log n<=n/20; also log(n/18)>2. These inequalities imply (22), with considerable slack.

Combining (16) and (21) yields the particularly simple signed enclosure

    |(-1)^(n+1)(t-S)/A_n-L(zstar)|
      <=Nlambda[(12+(b-1)^2)/n+rho_(n,b)]
      <=Nlambda[(12+(b-1)^2)/n+exp(-n)].                (23)

This is sharper structural information than |t-S|<=exp(-n/8): it identifies a computable signed coefficient, its natural scale, and a uniform additive remainder. It does not automatically improve a numerical absolute bound when L(zstar) nearly cancels; the earlier exp(-n/8) bound remains independently available from the provisional inverse result.

## 9. Exact remaining sign condition and analytic choice of b

Let

    mu_(n,b,w)=|L(zstar)|/Nlambda,
    eps_(n,b)=(12+(b-1)^2)/n+rho_(n,b).

If mu_(n,b,w)>eps_(n,b), (23) proves

    sign(t-S)=(-1)^(n+1)sign L(zstar),

and the rigorous two-sided nonzero bound

    A_n[|L(zstar)|-Nlambda eps_(n,b)]
       <=|t-S|<=A_n[|L(zstar)|+Nlambda eps_(n,b)].        (24)

The inequality is a condition on explicitly rational/algebraic construction data, not on the unknown value S. It can be checked without computing S. No such check is performed in this task.

For example, a proved lower bound mu_(n,b,w)>=mu0>0 on a chosen family would allow b to be selected analytically by

    12+(b-1)^2<=mu0 n/2,
    rho_(n,b)<=mu0/4,
    n>=512b^4 log n.

It would give a relative error at most 3/4 in the leading term, and a relative asymptotic if b^2/n=o(mu_(n,b,w)). In the maximum permitted slow range,

    (b-1)^2/n<=1/sqrt(512 n log n),

so the additive remainder in (23) tends to zero uniformly on its Nlambda scale. This does not prove that mu stays above that remainder.

The exact algebraic zero condition is also explicit. Since zstar has minimal polynomial 2z^2-4z+1,

    L(zstar)=0 iff 2z^2-4z+1 divides L(z) in Q[z].

For b=2, L has degree at most one and lambda^T u=1, so L(zstar) cannot vanish. Even there, nonzero at each n is not a uniform lower bound relative to Nlambda. For b>=3 no exclusion of this divisibility, and no adequate quantitative separation from zero, is proved here.

Accretivity of the earlier Toeplitz operator does not by itself imply positivity of this adjoint polynomial at zstar. It is not a quadratic form of the operator. No entrywise sign theorem or positivity-preserving signed transform is assumed.

This is the stopping boundary: a first uniformly nonzero signed asymptotic term has not been established on an unbounded growing-b set. Higher saddle terms should not be promoted until the algebraic coefficient or the appropriately combined coefficients have a proved lower bound and a uniform remainder budget. Fixed-b expansions cannot replace that requirement.

## 10. Coordination and scope

For Child 4, equation (4) is the exact rational center formula in the specified full-coefficient norm. The formula defines the arithmetic object before any denominator reduction; this note does not infer its reduced denominator from its size or error. The adjoint coefficients and the test L(zstar) are rational/algebraic data independent of S.

For Child 2, the full lift, the reconstruction map R, and W are retained. Its B-only complete-bound center uses H=diag(w_j^2) in place of R^T W R. All formulas above work with that replacement, but the resulting center generally differs from the full-coefficient center. No equality of those centers is implied by constant-factor Gram comparability. The complete pi-error term in Child 2's bound remains indispensable.

The new findings are the exact center and companion formulas (3)–(10), the forcing-column derivative identity (11), the uniform exponential remainder (13), the conjugate-endpoint arc identity (15), and the signed additive saddle enclosure (18), (23). Their leading coefficient is not defined through S.

No old checker was rerun, no new HP index was constructed, and no numerical evidence is asserted. No independent audit or irrationality claim is made. The original provisional inverse remains a stated dependency. All new records are confined to work/session_20261001_astra/agent3/.
