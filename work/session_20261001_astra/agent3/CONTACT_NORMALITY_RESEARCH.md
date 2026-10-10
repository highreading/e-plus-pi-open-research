> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

Contact normality through an exact rational reduction and a concentrated circle integral

Status: proved nonvanishing on an explicit unbounded growing-b range. The proportional range b=floor(n/2) remains unresolved here. This is new contact-normality research, not an independent audit. No Bernstein checks, kernel witnesses, previous positivity investigations, or HP degree scans are repeated.

All logarithms below are natural logarithms.

The main result is the following.

THEOREM. Let n>=16 and 2<=b<=n be integers satisfying

    n >= 512 b^4 log n.                                      (1)

For the square Taylor matrix J_(n,b) in the assignment, in the stated column order, one has

    det J_(n,b)>0.                                           (2)

In particular, put

    b_*(n)=floor((n/(512 log n))^(1/4)).

For every integer n>=2^18 and every 2<=b<=b_*(n), (2) holds. This includes the explicit unbounded allocation b=b_*(n), which grows on the scale (n/log n)^(1/4). There is no parity restriction on n.

The supplied endpoint bridge therefore gives a two-dimensional relaxed matched space, whose endpoint map (A(1),B(1)) is an isomorphism onto Q^2, throughout this range.

The exact reductions below also apply to b=floor(n/2). The concentration estimate used to prove (2) does not establish nonvanishing in that proportional regime.

1. Exact reduction of the logarithmic block

Write

    Q(z)=1-z+z^2/2,
    F(z)=4 arctan(z/(2-z)),
    F'(z)=2/Q(z),
    alpha=1+i, beta=1-i, delta=alpha-beta=2i.

Both poles are retained. Since

    F'(z)=-2i[1/(z-alpha)-1/(z-beta)],

a local branch of F equals -2i log((z-alpha)/(z-beta)) plus a constant.

For C of degree less than n define

    U_n(C)=Q(z)^n D_z^n(C(z)F(z)).                         (3)

This is an invertible rational linear map from polynomials of degree less than n to themselves. In the ascending monomial basis its determinant is exactly

    det U_n=2^n (product_(j=0)^(n-1) j!)^2.                 (4)

Here is a proof including the degree bound and all complex signs. Over Q(i), use the basis

    C_j(z)=(z-alpha)^j(z-beta)^(n-1-j), 0<=j<n,
    w=(z-alpha)/(z-beta).

The differential covariance identity is

    D_z^n[(z-beta)^(n-1) f(w)]
      =delta^n (z-beta)^(-n-1) f^(n)(w).                  (5)

For the functions needed here, (5) follows directly by expanding f(1-delta/u), u=z-beta, in powers of u^(-1). Terms u^(n-1-r) with r<n differentiate to zero. For r>=n their nth derivative is

    (-1)^n r!/(r-n)! * u^(-r-1),

which gives the right side of (5). The resulting rational derivative identities continue to the germ at zero. Changing a logarithm branch adds a polynomial of degree less than n before differentiation, so it has no effect.

For 0<=j<n,

    D_w^n(w^j log w)
      =(-1)^(n-j-1) j!(n-j-1)! w^(j-n).

Since Q(z)=(z-alpha)(z-beta)/2, equations (3)-(5) give

    U_n(C_j)=lambda_j C_j,
    lambda_j=2 i^(n-1)(-1)^(n-j-1)j!(n-j-1)!.            (6)

Thus the image has degree less than n and every eigenvalue is nonzero. The operator has rational coefficients, since F'=2/Q and D_z^n C=0. Multiplying the eigenvalues gives (4): the factors i^(n(n-1)) and (-1)^(n(n-1)/2) cancel exactly.

This invertible map is the key simplification. After n derivatives, the entire logarithmic polynomial block becomes the full space

    {P(z)/Q(z)^n : degree P<n}.

No positive-minor assertion is involved.

2. A b-by-b Toeplitz determinant with an exact prefactor

Define the rational Taylor coefficients

    G_n(z)=exp(z)Q(z)^n=sum_(m>=0) g_m^(n) z^m,

and set

    Delta_(n,b)=det[g_(n+i-j)^(n)]_(i,j=0,...,b-1).        (7)

Then, for every n>=2 and 2<=b<=n,

    det J_(n,b)
      =(-1)^(nb) K_(n,b) Delta_(n,b),                    (8)

where the prefactor is strictly positive and completely explicit:

    P_n=product_(j=0)^(n-1) j!,
    K_(n,b)=2^n P_n^3 / product_(m=n+b)^(2n+b-1) m!.     (9)

To prove this, first eliminate the polynomial columns using Taylor rows 0,...,n-1. Those columns form an identity block. The remaining rows are n,...,2n+b-1. For k=0,...,n+b-1, replacing a Taylor coefficient in row n+k by the corresponding coefficient of the nth derivative contributes the factor

    k!/(n+k)!.

The differentiated exponential block is

    D^n(exp(z)B)=exp(z)(D+1)^n B.

On polynomials of degree less than b, (D+1)^n is triangular with diagonal one. The differentiated logarithmic block is U_n(C)/Q^n. Multiplication of all remaining functions by Q^n preserves their Taylor-jet determinant, because Q(0)^n=1.

The remaining canonical columns are therefore

    z^j G_n(z), 0<=j<b;
    z^j,        0<=j<n,

with the additional column-transform determinant det U_n. Swapping these two blocks contributes (-1)^(nb). Eliminating the polynomial identity block leaves exactly (7). Finally,

    product_(k=0)^(n+b-1) k!/(n+k)!
      =P_n / product_(m=n+b)^(2n+b-1) m!,

which proves (8)-(9).

Equivalently, a kernel vector of J corresponds bijectively to a pair

    degree P<n, degree Btilde<b,
    P+G_n Btilde=O(z^(n+b)).                             (10)

The low coefficients determine P; the remaining b coefficients are the system in (7). Thus nonvanishing of (7) is exactly contact normality, with no endpoint assumption inserted.

The coefficients in (7) can be generated by a short exact recurrence. With g_0=1 and g_(-1)=g_(-2)=0,

    (m+1)g_(m+1)
      =(m+1-n)g_m+(2n-m-1)g_(m-1)/2+g_(m-2)/2,
      m>=0.                                            (11)

Indeed QG_n'=(Q+nQ')G_n. All entries of (7) use indices between n-b+1 and n+b-1, which are positive in the stated domain. Alternatively,

    g_m=sum_(s=0)^min(m,2n) [z^s]Q(z)^n/(m-s)!,

so every factorial argument is nonnegative.

3. The requested differential-annihilator representation

The same reduction can be expressed with

    L=(D-1)^b D^n.

For an initial polynomial P_0 of degree less than n, define successively

    P_(r+1)=Q P_r'-(n+r)Q'P_r-QP_r,
    r=0,...,b-1.                                       (12)

Then

    (D-1)^r(P_0/Q^n)=P_r/Q^(n+r),
    degree P_r<=n-1+2r.                                 (13)

Taking P_0=U_n(C) gives L(CF). In particular contact normality is also equivalent to invertibility of the n-by-n rational matrix

    H_(n,b)=[ [z^q]P_b^(j)(z) ]_(q,j=0,...,n-1),

where P_0^(j)=z^j and (12) generates P_b^(j).

For completeness, the reverse implication follows from the monic constant-coefficient differential equation L. Its homogeneous solution space is spanned by z^j, j<n, and z^j exp(z), j<b. These functions allow arbitrary initial jets of length n+b. If L(CF)=O(z^n), choose their linear combination to cancel the first n+b jets of CF. The differential equation then recursively forces contact through order 2n+b-1. Multiplication by Q^(n+b), a unit at zero, makes the condition exactly P_b=O(z^n).

If a_(r,m)=[z^m]P_r, the banded coefficient recurrence is

    a_(r+1,m)
      =(m+1)a_(r,m+1)+(n+r-m-1)a_(r,m)
       +((m+1)/2-n-r)a_(r,m-1)-a_(r,m-2)/2,             (14)

with out-of-range coefficients zero. Thus the reduction supplies both a rational-function jet matrix and the smaller Toeplitz determinant (7). The nonvanishing mechanism below applies to the latter.

4. An exact circle integral for the complete determinant

Put a=sqrt(2) and z=a exp(i theta). The two conjugate roots give the exact identity

    Q(z)/z=a cos(theta)-1.

Define

    w_n(theta)=exp(a exp(i theta))(a cos(theta)-1)^n.

Its kth Fourier coefficient is a^k g_(n+k). Consequently diagonal row and column scalings identify (7) with the Toeplitz determinant of these Fourier coefficients. Expanding two Vandermonde determinants and integrating term by term yields

    Delta_(n,b)
      =1/[b!(2pi)^b] integral_[-pi,pi]^b
          product_l w_n(theta_l)
          |V(exp(i theta_1),...,exp(i theta_b))|^2 dtheta.     (15)

Here V(x)=product_(i<j)(x_j-x_i). This determinant integration identity is finite-dimensional; all functions are continuous and the integration domain is compact.

The integral is for the entire function G_n, after elimination of F. No integration of a logarithm across its branch points occurs.

Center the angles at the negative real axis by writing theta=u+pi, with periodic identification. Let

    h(u)=1+a cos u,
    M=1+a.

Then

    (-1)^(nb) b! Delta_(n,b)
      =1/(2pi)^b integral_[-pi,pi]^b
          |V(exp(iu_1),...,exp(iu_b))|^2
          product_l [h(u_l)^n exp(-a cos u_l)]
          cos(a sum_l sin u_l) du.                     (16)

The imaginary part vanishes under simultaneous u_l -> -u_l. For odd n the factors h(u_l)^n may be negative. Equation (16) retains those signs. The proof will control their entire contribution outside a small central box, rather than treating the integral as positive.

5. A uniform scalar bound on the circle

For every -pi<=u<=pi,

    |h(u)| <= M exp(-u^2/16).                           (17)

If h(u)>=0, use

    h(u)/M=1-[a/(1+a)](1-cos u),
    a/(1+a)>1/2,
    1-cos u>=2u^2/pi^2,
    1-x<=exp(-x).

These imply h(u)/M<=exp(-u^2/pi^2)<=exp(-u^2/16), since pi<4.

If h(u)<0, then

    |h(u)|/M <= (a-1)/(a+1)<1/4.

Meanwhile exp(-u^2/16)>exp(-1)>1/3, using pi<4 and e<3. This proves (17) in the negative region as well. The elementary constants pi<4 and e<3 follow respectively from pi=4 integral_0^1 dt/(1+t^2) and the factorial series for e.

6. Dominant region and a quantitative lower bound

Let

    delta=1/(2b),
    G={u : |u_l|<=delta for every l}.

On G, every h(u_l) is positive, and

    |a sum_l sin u_l|<=a/2.

Since cos x>=1-x^2/2 and a^2=2,

    cos(a sum_l sin u_l)>=3/4.                          (18)

Let Z_G and Z_tail be the integrals over G and its complement of the nonnegative density

    |V(exp(iu))|^2 product_l |h(u_l)|^n exp(-a cos u_l),

including the normalization (2pi)^(-b), but not the factor 1/b!. Equation (16) implies

    (-1)^(nb) b! Delta_(n,b) >= (3/4)Z_G-Z_tail.         (19)

Assume n>=4b^2. For j=1,...,b, choose the intervals

    I_j=[-1/sqrt(n)+2(j-1)/(b sqrt(n)),
         -1/sqrt(n)+(2j-1)/(b sqrt(n))].

They have length 1/(b sqrt(n)), lie within [-1/sqrt(n),1/sqrt(n)], and have gaps of that same length. Their product is contained in G.

On these intervals,

    h(u)/M >= 1-u^2/2 >= 1-1/(2n),
    h(u)^n >= M^n/2,

where the last step is Bernoulli's inequality. Also exp(-a cos u)>=exp(-a). For angles from different intervals the chord distance is at least 1/(2b sqrt(n)): use 2 sin(|u-v|/2)>=2|u-v|/pi>=|u-v|/2.

Therefore the following explicit lower bound holds:

    Z_G >= L_(n,b),

    L_(n,b)=M^(nb) 2^(-b) exp(-ab)
              (2b sqrt(n))^(-b(b-1))
              (2pi b sqrt(n))^(-b) >0.                 (20)

Only one ordered product of intervals is used; no missing permutation factor is implicit in this bound.

7. The complete tail is smaller

Outside G, sum_l u_l^2>=delta^2=1/(4b^2). Equation (17), the chord bound |exp(iu)-exp(iv)|<=2, and exp(-a cos u)<=exp(a) give

    Z_tail <= U_(n,b),

    U_(n,b)=M^(nb) exp(ab) 4^(b(b-1)/2)
                         exp(-n/(64b^2)).              (21)

The normalized volume of the full angle cube is one. Dividing (21) by (20) gives the exact bounding ratio

    U_(n,b)/L_(n,b)
      =exp(-n/(64b^2))
         (4b sqrt(n))^(b^2) (pi exp(2a))^b.             (22)

All dimension-dependent factors are retained.

Under (1), with n>=16 and b>=2, one has n>=4b^2. Hence

    log(4b sqrt(n))<=log(2n)<=2 log n.

Also log pi+2a<5, b<=b^2/2, and log n>2. It follows that

    b^2 log(4b sqrt(n))+b(log pi+2a)<4b^2 log n.

Since n/(64b^2)>=8b^2 log n, (22) implies

    U_(n,b)/L_(n,b) <= n^(-4b^2)<1/4.                  (23)

Combining (19), (20), and (23) proves

    (-1)^(nb) Delta_(n,b) >= L_(n,b)/(2b!)>0.            (24)

This proves nonvanishing of the complete determinant, including all phases and all odd-n signs. It is not an inference from entrywise signs, mixed-minor positivity, or finitely many determinants.

Equations (8) and (24) prove the theorem and give the explicit lower bound

    det J_(n,b) >= K_(n,b)L_(n,b)/(2b!)>0.               (25)

8. The explicit unbounded allocation

For n>=2^18, the function n/log n is increasing. At n=2^18, log n=18 log 2<18 and

    2^18 > 512 * 2^4 * 18.

Thus n/(512 log n)>16 throughout this range, so b_*(n)>=2. Its definition implies (1), and b_*(n)<=n. Therefore

    b=b_*(n)=floor((n/(512 log n))^(1/4)), n>=2^18,

is an explicit unbounded growing-b set covered by the theorem.

The requested initial allocation b=floor(n/2) remains represented exactly by (7), (11), and (12)-(14). It does not satisfy the sufficient concentration condition for large n. Failure of that condition is only a limitation of this proof; it does not imply a zero determinant in the proportional regime.

9. Endpoint-rank consequence and scope

Let S_(n,b) be the rational space of triples with degree caps (n,b,n), contact O(z^(2n+b)), and B(1)=C(1). There are 2n+b+3 coefficients and at most 2n+b+1 linear constraints, so its dimension is at least two.

If its endpoint map (A(1),B(1)) has a zero vector in the kernel, all three polynomials vanish at one. Division componentwise by z-1 produces caps (n-1,b-1,n-1), preserves contact at zero, and gives a vector in ker J_(n,b). The theorem makes that vector zero. Thus the endpoint map is injective. The dimension count then proves

    dim_Q S_(n,b)=2,
    (A,B,C) -> (A(1),B(1)) is an isomorphism S_(n,b) -> Q^2.

This uses the supplied elementary bridge in its stated relaxed-contact scope. It does not claim uniqueness of the stronger-contact projective approximant, full evaluated-remainder nonvanishing, or shrinking of primitive forms. It gives no reduced-denominator estimate and does not alter the earlier obstruction for the chosen absolute shrinking bounds.

The new mathematical ingredients are the invertible logarithmic derivative transform (3)-(6), the exact smaller determinant (7)-(9), and a uniform dominant-arc estimate for its complete complex integral. No numerical sample is used in the proof. Necessary supporting identities are proved symbolically in this note; no computational scan is required.

The proportional growing-b question left open by this note is precisely nonvanishing of Delta_(n,floor(n/2)) in (7), whose scalar coefficients obey (11). The present theorem establishes contact normality and endpoint rank on the slower explicit growing range above.
