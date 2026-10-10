> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Uniform Hardy control of the actual dual factor allocation

Date: 2026-09-13. Original continuation by audit_computations.
Independent review pending. The scope is every even n=2m>=2.

This note uses the actual coupled Toeplitz equations to strengthen the
previous product/Mahler estimates. It proves a uniform Hardy H^2 bound
after division by an explicit positive-weight polynomial, a constant
bound on the total outward radial excess of the actual U roots, and
bounded discrepancies of every fixed root power sum. It also isolates
an exact signed-contour functional of the remaining bounded factor.
No new canonical degree, numerical root calculation, or scan is used.

The inspected inputs were raw_circular_binomial_prediction_bounds.md,
raw_joint_dual_hankel_and_even_root_product.md,
raw_dual_product_mahler_and_factorization_obstruction.md,
raw_dual_arctangent_toeplitz_second_kind.md, and the new two-function
Padé equation. The argument below is not an inference from product
bounds: its principal identity uses the actual equation Av=e_0.

## 1. The explicit base polynomial

Keep n=2m and normalized Haar measure on the unit circle. Put

    w(z)=|1+z^2|^(2m),  f(z)=exp(z)w(z),
    c_m=((2m)!)^2/[m!(3m)!],  H_m=1/c_m,
    v=A^(-1)e_0=q/(n!V(1)),  v_0=v(0)>0.                 (1)

Let Phi_j be the monic polynomials for the positive circular measure
|1-u|^(2m). Their already proved explicit formula and norm are

    Phi_j(u)=sum_(r=0)^j binom(j,r)
                (m)_(j-r)/(m+r+1)_(j-r) u^r,
    h_j=j!(2m+j)!/(m+j)!^2.                              (2)

Rising factorials occur in (2). All their roots lie strictly inside
the unit disk. Define the degree-n monic polynomial and its reversal

    Psi(z)=(-1)^m Phi_m(-z^2),
    F(z)=Psi^*(z)=Phi_m^*(-z^2).                          (3)

Parity and the pushforward u=-z^2 show that Psi is the monic degree-n
orthogonal polynomial for w, with norm squared H_m. Its roots are
strictly inside the unit disk. Therefore F(0)=1 and F has no root
in the closed unit disk. All coefficients in (3) are real rational.

## 2. An exact positive-measure replacement through degree n

The two positive circle measures

    dmu=w(z)dtheta/(2pi),
    dnu=H_m |F(z)|^(-2)dtheta/(2pi)                      (4)

have identical Laurent moments at every exponent from -n to n.
Here is a self-contained proof of this finite moment identity.

On the circle Psi(z)=z^n conjugate(F(z)). Since 1/F is analytic
on a neighborhood of the closed disk, for 0<=j<n one has

    integral Psi(z)z^(-j)dnu
       =H_m integral z^(n-j)/F(z)=0.

Also integral |Psi|^2 dnu=H_m. Thus Psi has the same monic
orthogonality and norm under both measures. In either measure,
orthogonality and its monic leading coefficient imply
integral Psi(z)z^(-n)=H_m. The difference functional L=mu-nu
therefore annihilates Psi z^(-j), 0<=j<=n, and their conjugates.

To verify that these equations determine all the stated moments,
multiply their Laurent polynomial span by z^n. The resulting span
is Psi P_n+F P_n, where P_n denotes polynomials of degree at most n.
The polynomials Psi and F are coprime: their roots lie strictly
inside and strictly outside the unit disk, respectively. Hence
Psi P_n intersect F P_n is the one-dimensional span of Psi F.
The sum has dimension 2(n+1)-1=2n+1, exactly the dimension of
P_(2n). It is the whole of that space. This proves the moment
claim, with no assumed infinite moment identity.

In particular, for EVERY polynomial p of degree at most n,

    ||p||_w^2=H_m ||p/F||_(H^2)^2.                       (5)

The right norm is the circle Hardy norm. The quotient is analytic
past the unit circle for each fixed n. Equation (5) is exact; it
is not a bound obtained by discarding a varying weight.

## 3. Actual sector energy gives a uniform Hardy bound

The Toeplitz equation Av=e_0 gives the exact energy identity

    integral f(z)|v(z)|^2=v_0.                            (6)

The sharper pointwise estimate Re exp(z)>=exp(-1) holds on the
unit circle. For completeness, if b=|sin theta|, the smaller
cosine branch has logarithm

    -sqrt(1-b^2)+log cos b.

Its derivative is tan(arcsin b)-tan b>=0 for 0<=b<1, since
arcsin b>=b and tangent is increasing there. Its minimum is -1
at b=0. The other cosine branch is larger, and continuity covers
b=1. Thus (6) proves

    ||v||_w^2<=e v_0.                                    (7)

The previously passed inverse-corner lower bound is

    v_0>=e^(-1)cos^2(1)c_m.                              (8)

Combine (5), (7), and (8). The ACTUAL normalized analytic factor

    R_n(z)=v(z)/[v_0 F(z)],       R_n(0)=1                (9)

satisfies the uniform theorem

    ||R_n||_(H^2)^2
       =c_m||v||_w^2/v_0^2
       <=e c_m/v_0<=e^2 sec^2(1)=:C_*^2.                (10)

All constants are independent of n. Also, evaluation at zero in
the positive base norm has squared norm c_m. Consequently
v_0^2<=c_m||v||_w^2<=e c_m v_0, giving the additional upper bound

    v_0<=e c_m.                                          (11)

This is a true factor-allocation statement using the actual
weighted Cauchy equations. The comparison family in the earlier
product-obstruction note was not required to satisfy these equations
and therefore was not subject to (10).

The elementary Hardy evaluation bound gives, for |z|<1,

    |R_n(z)|<=C_*/sqrt(1-|z|^2).                         (12)

It also follows from the exact positive base kernel identity

    K_n(z,z)=c_m
       [|F(z)|^2-|z|^2|Phi_m(-z^2)|^2]/(1-|z|^2).

That identity can be proved by telescoping the recurrence in (2),
or directly by the even and odd polynomial decomposition. It is
not needed once the exact norm identity (5) has been established.

## 4. Constant radial root excess and finite root counts

Let lambda_1,...,lambda_n be the actual U roots, including zeros
and multiplicity. The established leading coefficient u_n is nonzero,
and

    v(z)/v_0=product_(j=1)^n(1-lambda_j z).                (13)

Since F(0)=1 and all its zeros are outside the closed unit disk,
the circle mean of log|F| is zero. Jensen's inequality, (9)-(10),
and the polynomial root formula therefore give

    sum_j log^+|lambda_j|
       =integral log|v/v_0|
       =integral log|R_n|
       <=log ||R_n||_(H^2)
       <=log C_*=1-log cos(1).                           (14)

Circle zeros cause only integrable logarithmic singularities and
do not invalidate these identities. Equivalently,

    M(U)/|u_n|<=e sec(1).                                (15)

This improves the earlier sqrt(1+2n sec^2(1)) upper bound to a
constant for the actual even family. In particular, for epsilon>0,

    #{j: |lambda_j|>=1+epsilon}
       <=[1-log cos(1)]/log(1+epsilon).                   (16)

The earlier uniform root-radius bound |lambda_j|<sec(1) remains
valid. Formula (16) does not exclude roots just outside the unit
circle, nor does it establish that all roots are real or lie on a
particular arc. If epsilon=n^(-alpha), 0<alpha<1, it gives the
explicit sublinear bound O(n^alpha), without an extra logarithm.

## 5. Fixed-disk factor and phase comparison

The previously passed product identity proves that v has no zero
on |z|<=cos(1). Since F has no disk zeros, R_n has no zero on this
same closed disk. Choose 0<r<R<cos(1) and set

    M_R=log(C_*/sqrt(1-R^2)).

There is a unique analytic log R_n with value zero at the origin.
Its real part is at most M_R on the radius-R disk by (12).
Harnack's inequality for the positive harmonic function
M_R-Re log R_n proves

    exp[-2r M_R/(R-r)]<=|R_n(z)|<=exp(M_R),  |z|<=r.       (17)

The same conclusion follows from the Poisson kernel bounds and
therefore requires no assumption about limiting coefficients.
This is a uniform two-sided comparison of the actual factor with
the explicit F on each such fixed disk.

More precisely, write log R_n=sum_(j>=1) ell_(n,j) z^j.
The positive harmonic function just used has mean M_R, so its
Fourier coefficients give the elementary bound

    |ell_(n,j)|<=2 M_R/R^j,          j>=1.                 (18)

Consequently |log R_n(z)|<=2M_R r/(R-r) for |z|<=r. Thus the
analytic argument, normalized at zero, is bounded as well as
the modulus on these fixed disks. No phase bound on the unit
semicircle is inferred by taking R up to one in this statement.

## 6. Actual root power sums match an explicit symmetric comparison

Let alpha_1,...,alpha_m be the roots of Phi_m, and define a
multiset of n comparison numbers mu_j by

    F(z)=product_(j=1)^n(1-mu_j z).

In pairs they satisfy mu_(2j-1)^2=mu_(2j)^2=-conjugate(alpha_j)
and mu_(2j)=-mu_(2j-1). All have modulus less than one. By
comparing logarithmic Taylor coefficients in (9), (13), and F,

    |sum lambda_j^s-sum mu_j^s|
       <=2s M_R/R^s,          s>=1, R<cos(1).             (19)

For each fixed s this is O_s(1), uniformly in n, rather than
an O(n) estimate obtained from bounded individual root radii.
In particular all odd comparison sums vanish, hence

    sum_j lambda_j^(2r+1)=O_r(1).                         (20)

From (2), [u]Phi_m^*=m/2, so [z^2]F=-m/2. Thus

    sum_j lambda_j^2=m+O(1)=n/2+O(1).                    (21)

For reference, the next coefficient gives

    sum_j mu_j^4=-m(m-2)/[2(2m-1)],
    sum_j lambda_j^4=-n/8+O(1).                          (22)

These are complex power sums with multiplicity. They must not
be interpreted as sums of absolute powers. They are compatible
with nonreal conjugate roots and do not by themselves determine
a planar root distribution.

## 7. Exact signed-contour reduction to a uniformly bounded multiplier

The known exact representation uses the clockwise left unit
semicircle gamma_L from -i to i:

    Ra(1)/(n!V(1))=(1/(2i)) integral_gamma_L
       D(z)^n v(z)/[z^(2n+1)(z-1)^(n+1)] dz.

Substituting the proved factorization (9), and parametrizing with
increasing theta on the LEFT half-circle (therefore reversing the
clockwise orientation), gives

    Ra(1)/(n!V(1)v_0)=integral_circle k_n(theta)R_n(z),
    k_n(theta)=-pi 1_[pi/2,3pi/2](theta)
       D(z)^n F(z)/[z^(2n)(z-1)^(n+1)],   z=e^(i theta).    (23)

The density k_n is an explicitly known L^2 function: its denominator
does not vanish on the left half-circle and its numerator vanishes
at both endpoints. Write

    a_(n,j)=integral_circle k_n(theta)z^j,  j>=0,
    R_n(z)=sum_(j>=0)r_(n,j)z^j,  r_(n,0)=1.

These coefficients are real by conjugation symmetry. Hardy/L^2
duality and Parseval justify the convergent exact pairing

    Ra(1)/(n!V(1)v_0)=sum_(j>=0)a_(n,j)r_(n,j),
    sum_j |r_(n,j)|^2<=C_*^2.                             (24)

In particular there is a rigorous signed interval

    |Ra(1)/(n!V(1)v_0)-a_(n,0)|
       <=sqrt(C_*^2-1) [sum_(j>=1)|a_(n,j)|^2]^(1/2).      (25)

This states precisely what is gained: the unknown factor now lies
in a fixed Hardy ball, has constant coefficient one, and satisfies
the additional actual Padé differential constraints. It does not
replace the unknown factor by a free positive scalar. Neither
smallness of the explicit tail norm in (25) relative to a_(n,0),
nor a sharper signed alignment of the actual coefficient vectors,
has been proved here. Consequently no sign of Ra is claimed.

The earlier connection scalar, denoted a_n without a second index,
remains

    a_n=(2n+1)! Ra(1)/(n!V(1))
       =(2n+1)!v_0 sum_j a_(n,j)r_(n,j).                 (26)

The actual endpoint sum is n!V(1)/(2n+1)! times
{exp(1/2)[1+O(1/n)]+4a_n}. Its primitive version still divides
by g=gcd(|Qhat(1)|,|Pe(1)+4Pa(1)|). Uniform factor allocation
does not remove this arithmetic normalization or establish the
required cancellation in (26).
