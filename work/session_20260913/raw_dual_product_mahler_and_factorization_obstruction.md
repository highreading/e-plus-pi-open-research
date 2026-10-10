> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Bounded dual product, logarithmic radial root excess, and factorization obstruction

Date: 2026-09-13. Original continuation by audit_computations.
Independent review requested. The product identity and fixed-radius
argument were proposed by root and independently verified here.
The Mahler bound and normalized comparison family are new continuations.

This note concerns the actual even-degree dual family. It controls a
root statistic beyond the fixed radius, but does not estimate the
signed arctangent connection scalar or the endpoint gcd.

## 1. Exact product and its uniformly bounded coefficients

Let n=2m>=2 and retain the normalization in
`raw_dual_arctangent_toeplitz_second_kind.md`:

    v=q/(n!V(1)),       v(0)=v_0>0,
    B(x)=sum_(r=0)^n b_r x^r,       B(0)=1,
    f(theta)=e^(e^(i theta))|1+e^(2i theta)|^(2m).

The full-circle second-kind identity, with s=1/x, gives

    P_n(x):=v(x)B(x)/v_0
      =(1/v_0) integral_circle f(theta)|v(e^(i theta))|^2
                                      /(1-xe^(i theta)).     (1)

Initially |x|<1. The left side is a polynomial of degree at most
2n with constant one, so this identity also identifies every Taylor
coefficient of the integral. All coefficients are real.

The positive Hermitian-part identity is

    integral_circle f|v|^2=v_0,
    integral_circle |f||v|^2<=v_0/cos(1).

Indeed Re f=|f|cos(sin theta)>=cos(1)|f|, and the imaginary
part integrates to zero by conjugation. Expanding (1) therefore gives

    [x^0]P_n=1,       |[x^k]P_n|<=sec(1),  1<=k<=2n.        (2)

For k>2n these moments vanish exactly, not just asymptotically.

## 2. Verified fixed-radius zero exclusion

For |x|<=cos(1) and z=e^(i theta),

    Re[e^z/(1-xz)]
      =|e^z| Re[e^(i sin theta)(1-conjugate(xz))]/|1-xz|^2
      >=|e^z|[cos(sin theta)-|x|]/|1-xz|^2.                 (3)

The denominator is nonzero since cos(1)<1. In the boundary case
|x|=cos(1), the last numerator is strictly positive apart from the
two points sin theta=+/-1. The weight is positive almost everywhere,
and v is a nonzero polynomial. Integration in (1) proves

    Re P_n(x)>0       on the CLOSED disk |x|<=cos(1).        (4)

Consequently v and B have no zeros on that disk. The reciprocal
identity q(z)=u_n product_j(1-lambda_j z), where lambda_j are all
roots of U counted with multiplicity, shows

    |lambda_j|<sec(1)       for every root of U.             (5)

Zeros of U at zero contribute constant factors to q and satisfy
this conclusion as well. No assertion of real-rootedness is used.

## 3. Polynomial Mahler control and only logarithmically many exterior roots

For a polynomial F, use the multiplicative Mahler measure

    M(F)=exp(integral_circle log|F|).

Equivalently, for leading coefficient a and roots alpha_j,
M(F)=|a| product_j max(1,|alpha_j|). The equivalence follows by
applying the circle mean identity for log|z-alpha| to each linear
factor; unit-circle zeros have integrable logarithmic singularities.
For a polynomial with constant one, this also gives
M(F)=product_j max(1,1/|alpha_j|)>=1.

Jensen's inequality and Parseval's identity applied to (2) give

    M(P_n)<=||P_n||_(L2 circle)
            <=L_n:=sqrt(1+2n sec^2(1)).                     (6)

Both F_n=v/v_0 and B have constant one, and P_n=F_n B.
Mahler measure is multiplicative. Since neither factor has Mahler
measure less than one, (6) proves

    1<=M(F_n)<=L_n,       1<=M(B)<=L_n.                     (7)

For the actual U roots, the reciprocal factorization gives exactly

    M(F_n)=M(U)/|u_n|=product_j max(1,|lambda_j|).

Thus the total outward radial excess satisfies

    sum_j log^+|lambda_j| <= (1/2)log(1+2n sec^2(1)).        (8)

In particular, for each epsilon>0,

    #{j: |lambda_j|>=1+epsilon}
      <=log(1+2n sec^2(1))/[2log(1+epsilon)].                (9)

Together with (5), this says that all U roots lie in a fixed disk,
and only O(log n) lie outside any fixed larger-than-unit radius.
The constants are explicit; no limiting root distribution is assumed.

Likewise, for 0<r<1, each of F_n and B has at most
log(L_n)/log(1/r) roots in |z|<=r. This latter statement is about
inward roots of the reciprocal factors, not an additional sign or
phase estimate on a contour.

## 4. Exact place where the product enters the remaining tail

The actual Toeplitz equation also gives the exact decomposition

    e^z(1+z^2)^n v(z)=z^n B(1/z)+z^(2n+1)G_n(z),           (10)

where G_n is entire. Since v=v_0 P_n/B, it can be rewritten as

    e^z(1+z^2)^n v_0 P_n(z)
      =z^n B(z)B(1/z)+z^(2n+1)B(z)G_n(z).                  (11)

On the circle, B(z)B(1/z)=|B(z)|^2, since B has real
coefficients. Equation (11) is a coupled factorization constraint;
the order 2n+1 cancellation at zero is part of the actual system.

The exact arctangent transform can now be written

    Ra(1)/(n!V(1))
      =(v_0/(2i)) integral_(gamma_L)
         (1+z^2)^n [P_n(z)/B(z)]
                /[z^(2n+1)(z-1)^(n+1)] dz.                 (12)

Here gamma_L is the clockwise left unit semicircle from -i to i,
as proved in the preceding note. The quotient P_n/B is the
polynomial v/v_0; common zeros are interpreted by cancellation.

Equations (2), (4), and (7) do not by themselves control this
quotient. Mahler measure controls an average logarithm and the
number of roots a fixed distance inside the unit disk. It does not
give a pointwise lower bound for B or decide how the zeros of P_n
are split between its two factors. The next section demonstrates
this with a comparison that retains more than a generic product bound.

## 5. An explicit normalized factorization comparison

This section is NOT a counterexample in the actual HP family. It
shows that the already proved scalar consequences, taken without
the coupled Toeplitz equation (10), cannot bound the separate factors
subexponentially. No canonical degree is solved.

Take the unbounded subsequence n=2m with m even. Set

    c_m=((2m)!)^2/[m!(3m)!],       R_n=c_m^(-1/n).

Let zeta range over the 2m roots of 1+w^(2m). No such root has
zero real part when m is even. Exactly m lie in each open half-plane,
and each collection is closed under conjugation. Define

    F_+(w)=product_(Re zeta>0)(1-w/zeta),
    F_-(w)=product_(Re zeta<0)(1-w/zeta).

Both are real degree-m polynomials with constant and leading
coefficient one; their roots occur in nonreal conjugate pairs.
Thus F_+F_-=1+w^(2m), and each factor is positive on the real line.
Put

    v_tilde(z)=c_m F_-((z/R_n)^2),
    B_tilde(z)=F_+((z/R_n)^2).

The following identities and bounds are exact:

    v_tilde(0)=c_m,       B_tilde(0)=1,
    [z^n]B_tilde=R_n^(-n)=c_m=v_tilde(0),
    P_tilde=v_tilde B_tilde/v_tilde(0)=1+c_m^2 z^(2n).       (13)

Thus the product has uniformly bounded coefficients, is strictly
positive in real part on the closed unit disk, and has Mahler
measure one. Both factors also have Mahler measure one after
normalizing their constant coefficients. They have no root in the
unit disk, a stronger exclusion than (4).

For x in [-1,0], both factors are positive, and

    v_tilde(x)B_tilde(x)/v_tilde(0)
      =1+c_m^2 x^(2n)>=1>=1/(1-x).                         (14)

The exact final prediction-coefficient relation b_n=v_0 is retained.
Also, odd coefficients of B_tilde vanish and its coefficient of
z^(2s) has absolute value at most binom(m,s)R_n^(-2s), hence
at most binom(m+s,s). These satisfy the proved all-r prediction
bounds (even with constant one).

Defining a comparison V by the same factorial coefficient map
V(1+t)/V(1)=sum n!b_r t^r/(n+r)! gives precisely

    V(1)/[t^n]V=(2n)!/(n!c_m)=B_m.

So the proved even root-product scale is retained as well. These
explicit comparison factors have real algebraic coefficients, not
necessarily rational coefficients. They are not asserted to obey
the actual joint Hankel equation.

Despite all these properties, the factors vary exponentially in
opposite directions even at a fixed interior real point. Fix 0<r<1.
Each conjugate pair in F_- at the positive argument
w=(r/R_n)^2 contributes more than 1+w^2. Consequently

    v_tilde(-r)/v_tilde(0)
       >=[1+(r/R_n)^4]^(m/2).

The product formula c_m=product_(j=1)^m (m+j)/(2m+j)
gives c_m>=2^(-m), hence R_n<=sqrt(2). Therefore, writing
kappa_r=(1/4)log(1+r^4/4)>0,

    v_tilde(-r)/v_tilde(0)>=exp(kappa_r n),
    0<B_tilde(-r)<=2exp(-kappa_r n).                        (15)

All coefficient, sign, root-excess, and normalization properties
listed above coexist with this exponential compensation.

The obstruction can also be made rational without assuming a height
bound. Keep the constant coefficient one, the degree-n coefficient
c_m, and all odd coefficients of BOTH normalized factors fixed.
Approximate their remaining real coefficients by rationals closely
enough. The original roots are outside the unit disk with a positive
margin, so Rouche's theorem on the unit circle preserves that exclusion.
The prediction-coefficient bounds have strict slack at every unfixed
coefficient. Both factors have positive minima on [-1,0], so the
approximations can retain positivity and change their values by factors
between 1/2 and 3/2 throughout that interval. The product's unfixed
coefficients can be kept with total absolute change at most 1/4;
it remains even and has unchanged constant term. Thus at x=-t,
0<=t<=1, its value is at least 1-t^2/4>=1/(1+t), preserving (14).
Choosing the perturbation still smaller keeps every product coefficient
bounded by one and its real part positive on the closed unit disk.
There are only finitely many such strict requirements for each n,
so rational density supplies them simultaneously. The comparison
V from the factorial map then has rational coefficients and can be
rescaled to primitive integral coefficients. The exact relation
b_n=v_0=c_m and the root-product scale remain unchanged. The
exponential inequalities (15) hold with constants 1/2 and 3 instead
of 1 and 2. No bound on the required rational denominators is claimed.

The comparison does not retain the precise weighted Cauchy identity
(1) with the SAME v_tilde, or the high-order matching in (10).
Accordingly it refutes no desired theorem about the actual v and B.
It proves the limited but important point that a successful estimate
must use this remaining coupled structure, rather than only the
bounded product, its zero-free disk, Mahler bounds, and previously
proved prediction consequences.

## 6. What remains for the signed arctangent connection

The actual new theorem is (8)-(9), together with the verified product
bounds (1)-(5). They sharply limit radial root escape but do not
control allocation of the product factors on gamma_L.

A useful further target is a modulus AND phase estimate for the
actual polynomial quotient P_n/B=v/v_0 on the contour in (12),
derived from the high-order coupled equation (10)-(11). A signed
estimate for its weighted integral, or for the equivalent partial
Cauchy derivative J_n^(n)(1), would control the dimensionless scalar
a_n from the preceding note. A bound for the product alone cannot
replace this step, as the normalized comparison shows.

The final form is still sign(Z)[Re(1)+4Ra(1)]/g. None of the
root or factorization estimates removes the actual endpoint gcd.
