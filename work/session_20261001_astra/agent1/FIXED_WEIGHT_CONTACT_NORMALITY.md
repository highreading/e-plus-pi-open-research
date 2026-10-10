> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Fixed-weight contact normality with the actual exceptional border

Author research proof, 2026-10-01. This note contains a new deductive proof, not an independent review or a numerical certificate. The completed fixed-weight Christoffel package is an accepted starting point but none of its Gram estimates is needed for the normality proof below. No balanced contact-normality theorem is assumed.

Throughout, log denotes the natural logarithm,

    Q(z)=1-z+z^2/2,
    alpha=1+i, beta=1-i,
    F(0)=0, F'(z)=2/Q(z).

Thus Q=(z-alpha)(z-beta)/2 and F(1)=pi. Taylor coefficients at zero are rational. Polynomial spaces and linear maps may be taken over Q; complex scalars are used for the analytic proof.

## 1. Main theorem and precise scope

Let n and b be integers satisfying

    n >= ceil(exp(32)),     1 <= b <= floor(log n),
    M=2n+b+1.

Then the square contact system

    deg A <= n,  deg B <= b-1,  deg C <= n-1,
    A+B exp(z)+C F(z)=O(z^M)

has only the zero solution.

Consequently, for the original, unselected allocation

    deg A <= n+1,  deg B <= b,  deg C <= n,
    A+B exp(z)+C F(z)=O(z^M),

the rational coefficient-endpoint map

    (A,B,C) -> (A(1),B(1),C(1))

is an isomorphism from its solution space to Q^3. In particular, imposing B(1)=C(1) gives a two-dimensional space, and its map to (X,Y)=(A(1),B(1)) is an isomorphism to Q^2.

This is a full endpoint-rank theorem for the unselected weighted allocation. It does not impose the stopped balanced-restoring selector. It establishes both independent endpoint directions simultaneously, rather than just a nonzero endpoint on a selected cofactor line. It does not assert that every individual direction has a nonzero highest A coefficient, nor does it determine the dimension of the balanced-selector slice by importing provisional balanced results.

The theorem gives neither useful coefficient heights nor primitive shrinking. The complete evaluated form remains X+Y(e+pi); its nonvanishing is a different issue.

## 2. The actual differential image

First establish a general algebraic fact. For m>=1, define

    S_m(C)=Q^m D^m(CF),     deg C <= m-1.

This is a rational-coefficient polynomial of degree at most m-1, and S_m is an isomorphism of that m-dimensional polynomial space.

Proof of polynomiality and the degree bound: write locally

    F=(2/i)(log(z-alpha)-log(z-beta))+constant.

For j<m,

    D^m((z-r)^j log(z-r))
      =(-1)^(m-j-1) j! (m-j-1)! (z-r)^(j-m).

Thus D^m(CF) is rational, with poles only at alpha and beta of orders at most m. On a sector at infinity, F has a constant plus a convergent series in z^(-1). Multiplying by C gives a polynomial part of degree at most m-1 plus negative powers. Its m-th derivative is O(z^(-m-1)). Therefore Q^m D^m(CF) is a polynomial of degree at most m-1.

For injectivity, S_m(C)=0 implies CF is a polynomial locally. If C is nonzero, F would be rational. This is impossible: F'=2/Q has nonzero simple-pole residues, whereas the derivative of a rational function has zero residue at every finite pole. Equal finite dimensions give the asserted isomorphism. All defining operations have rational coefficients.

Now use the actual number of derivatives required by the square system: m=n+1. Put

    T_n(C)=Q^(n+1) D^(n+1)(CF),    deg C<n.

The image lies in polynomials of degree at most n. It is NOT the full image of S_n and is NOT to be replaced by that image.

Let U=S_n(C). Since S_n is an isomorphism on deg<n,

    T_n(C)=L_n(U),
    L_n(U)=Q U'-n Q' U,     deg U<n.                 (2.1)

The map L_n is injective: L_n(U)=0 says D(U/Q^n)=0, hence U is a constant multiple of Q^n, which is incompatible with deg U<n unless U=0. For a nonzero U of degree d<n, the leading coefficient of L_n(U) is (d/2-n) times the leading coefficient of U, in degree d+1. In particular the image contains degree-n polynomials and has dimension n in the (n+1)-dimensional ambient space.

Here is its exact codimension-one condition. For deg P<=n define

    Lambda_n(P)=Res_(z=alpha) P(z)/Q(z)^(n+1),
    lambda_n(P)=Lambda_n(P)/Lambda_n(1).

Explicitly,

    Lambda_n(P)=2^(n+1)/n! *
      [D^n(P(z)/(z-beta)^(n+1))]_(z=alpha),

and

    Lambda_n(1)=2^(n+1)(-1)^n binom(2n,n)
                 /(alpha-beta)^(2n+1) != 0.         (2.2)

Because P/Q^(n+1)=O(z^(-n-2)), its residues at alpha and beta are opposite. For rational P each is in iQ, so lambda_n is a rational linear functional, normalized by lambda_n(1)=1.

Equation (2.1) gives

    L_n(U)/Q^(n+1)=D(U/Q^n),

so both residues vanish. Dimension now proves

    im T_n = {P: deg P<=n, lambda_n(P)=0}.          (2.3)

Equivalently, apply S_(n+1) to an arbitrary C of degree at most n. The explicit local formula gives

    Res_alpha D^(n+1)(CF)=(2/i)n! [z^n]C,
    Res_beta  D^(n+1)(CF)=-(2/i)n! [z^n]C.

The missing degree-n coefficient of C is exactly the missing residue direction. Both distinct poles, and the exceptional condition they create, are retained.

## 3. The reduced b-by-b system after n+1 derivatives

For the actual square system, D^(n+1) eliminates A completely. Write

    P=(D+1)^(n+1)B,   E(z)=exp(z)Q(z)^(n+1).

The operator on B is invertible and preserves degree at most b-1. The contact condition becomes

    E P + T_n(C)=O(z^(n+b)).                       (3.1)

Consequently P must satisfy the b conditions

    [z^k](E P)=0,          k=n+1,...,n+b-1,
    lambda_n([E P]_(<=n))=0.                      (3.2)

The last line is the exceptional row. When b=1 the first group is empty, and the exceptional row remains essential. Conversely (3.2), together with (2.3), uniquely reconstructs C; integration and the lower Taylor conditions uniquely reconstruct A.

For E_k=[z^k]E, with E_k=0 for k<0, a completely explicit matrix has columns j=0,...,b-1, bulk rows

    E_(n+r-j),  r=1,...,b-1,

and exceptional row

    lambda_n(sum_(k=0)^n E_(k-j) z^k).

Its nonsingularity is equivalent to the main theorem. This establishes the actual n+1-derivative reduction before any comparison with an exp(z)Q(z)^n matrix.

## 4. An equivalent bordered exp(z)Q(z)^n determinant

For analysis it is useful to keep, rather than eliminate, the last polynomial coefficient for one intermediate step. This does NOT replace the preceding n+1-derivative reduction.

Write A_n=[z^n]A in the square system, and set

    a=n! A_n,  V=(D+1)^n B,  U=S_n(C),
    w(z)=exp(z)Q(z)^n,
    s_k=[z^k]w(z),  q_k=[z^k]Q(z)^n,

with coefficients indexed below zero equal to zero. After n derivatives,

    a Q^n + w V + U=O(z^(n+b+1)),    deg U<n.      (4.1)

The n low coefficients determine U. The remaining equations are

    sum_(j=0)^(b-1) s_(n+r-j) v_j + q_(n+r) a=0,
                       r=0,...,b.               (4.2)

Define d=b+1 and the exact bordered determinant

    D_(n,b)=det [ s_(n+r-j) | q_(n+r) ],          (4.3)
               r=0,...,b; j=0,...,b-1.

The final column is exceptional; transposing (4.3) makes it the exceptional row. It cannot be discarded or identified with an ordinary Toeplitz column.

All changes of variables above are invertible, with the explicit nonzero scalar n! on A_n. Thus D_(n,b)!=0 is equivalent to nonsingularity of the actual square system and of (3.2). For completeness, given a vector in the kernel of (4.2), put U=-[wV+aQ^n]_(<n), invert S_n and (D+1)^n to obtain C and B, and choose the lower n coefficients of A to cancel the lower n Taylor coefficients. Equation (4.1) then gives contact exactly at least M. This proves both directions without assuming any balanced normality.

There is also a finite expansion in explicit minors of the exp(z)Q(z)^n coefficient array. Since Q^n=w exp(-z),

    D_(n,b)=sum_(j=b)^(n+b) (-1)^j/j! *
       det [s_(n+r-k)]_(r=0,...,b; k=0,...,b-1,j). (4.4)

Terms j<b vanish by repeated columns. Formula (4.4) retains the entire border, not just its first minor.

## 5. Exact integral representation of the border

Take rho=sqrt(2), z_l=rho exp(i theta_l), and normalized angular measure dtheta/(2pi). Let

    V_d(theta)=product_(u<v)|exp(i theta_v)-exp(i theta_u)|^2.

The coefficient integral and the determinant integration identity give

    D_(n,b)=1/d! integral V_d(theta)
       product_l [(Q(z_l)/z_l)^n exp(z_l)]
       exp(-z)[z_1,...,z_d] product_l dtheta_l/(2pi).       (5.1)

Here the bracket is the order-b divided difference. To verify normalization, the determinant of the functions

    1,z,...,z^(b-1),exp(-z)

at the nodes equals their ordinary Vandermonde times exp(-z)[z_1,...,z_d]. The other determinant is that of z_l^(-r), r=0,...,b. On the circle their Vandermonde product is precisely V_d(theta). Thus no power of rho, pole, or row is missing from (5.1).

Let nu be uniform PROBABILITY measure on the simplex

    t_l>=0, sum_l t_l=1.

Its unnormalized coordinate volume is 1/b!. The elementary simplex formula for divided differences gives

    exp(-z)[z_1,...,z_d]
       =(-1)^b/b! E_nu exp(-sum_l t_l z_l).        (5.2)

It follows by iterating the fundamental theorem of calculus for divided differences; it extends continuously to coincident nodes. In particular, on coincident negative-real nodes it has the nonzero sign (-1)^b. This is the border-specific mechanism, not a Gram-positivity assertion.

Shift theta_l=pi+x_l, x_l in [-pi,pi], and define

    H(x)=1+rho cos x,  a0=1+rho.

Since Q(z)/z=rho cos(theta)-1, formulas (5.1)-(5.2) become the exact identity

    (-1)^(nd+b) D_(n,b)
      =1/(d! b!) integral V_d(x) product_l H(x_l)^n
          E_nu exp(-rho sum_l(1-t_l)exp(i x_l))
          product_l dx_l/(2pi).                  (5.3)

The right side is real by complex conjugation. Its integrand is not globally positive: H can change sign and the exponential has a phase. The proof below controls both effects explicitly.

## 6. Border-adapted concentration, with an explicit slow range

Assume n>=ceil(exp(32)) and 1<=b<=floor(log n). Write

    t=log n,  d=b+1<=t+1,  delta=n^(-1/4).

Let the core be |x_l|<=delta for all l.

### 6.1 Phase and sign on the core

On the core, H>0. The exponential in (5.3) has imaginary exponent of absolute value at most

    rho sum_l(1-t_l)|sin x_l| <= 2d delta <= 1/2.

Indeed 2(t+1)exp(-t/4) decreases for t>=32 and is already less than 1/2 there. Its real exponent is at least -rho b>=-2d. Therefore, pointwise for every simplex point,

    Re exp(-rho sum_l(1-t_l)exp(i x_l)) >= (1/2)exp(-2d).

The real part of the entire signed integrand is nonnegative throughout the core.

### 6.2 A quantitative lower bound inside the core

For l=1,...,d take the disjoint intervals centered at

    c_l=(2l-d-1)/(d sqrt(n))

with half-width 1/(4d sqrt(n)). Every point in their Cartesian product has |x_l|<1/sqrt(n)<=delta. Distinct coordinates have separation at least 3/(2d sqrt(n)), so the corresponding circular chord is at least 1/(2d sqrt(n)). Each interval has normalized angular measure at least 1/(16d sqrt(n)).

Also, throughout this rectangle,

    H(x)/a0 >= 1-1/(2n),
    (H(x)/a0)^n >= 1/2,

the latter by Bernoulli's inequality. Thus the real part of the core integral in (5.3), before its external factor 1/(d!b!), is at least

    L=a0^(nd) exp(-2d) 2^(-(d^2+4d+1))
                  d^(-d^2) n^(-d^2/2).          (6.1)

No lower bound on an oscillating determinant has been obtained by ignoring its phase; the phase bound above is part of (6.1).

### 6.3 The complement is exponentially smaller

For |x|>=delta,

    |H(x)|/a0 <= 1-delta^2/10 <= exp(-delta^2/10). (6.2)

To prove this, when H>=0 use

    1-cos x >= 2x^2/pi^2,
    2rho/(a0 pi^2)>1/10.

When H<0, use |H|/a0 <=(rho-1)/(rho+1)<1/4, while 1-delta^2/10>=9/10. This accounts explicitly for the opposite-sign part of the circle.

At least one coordinate is outside the core. Every other |H| is at most a0; V_d<=2^(d(d-1)); and the exponential modulus is at most exp(rho b)<=exp(2d). Consequently the absolute value of the complementary integral is at most

    T=a0^(nd) 2^(d(d-1)) exp(2d-sqrt(n)/10).      (6.3)

The normalized angular measure of the whole domain is one, so no additional volume factor is needed.

Combining (6.1)-(6.3),

    log(T/L) <= -exp(t/2)/10 + E(t,d),

where

    E(t,d)=d^2 t/2+d^2 log d
             +(2d^2+3d+1)log 2+4d.

For t>=32 and d<=t+1, elementary inequalities give E(t,d)<=2t^3. For example use d<=(33/32)t, log d<=t/4, and log 2<1 in the displayed expression. Also

    exp(t/2)/10 >= 4t^3,      t>=32.

The ratio exp(t/2)/t^3 is increasing for t>6. At t=32, the last inequality follows already from e>8/3, hence e^4>50 and e^16>50^4>40*32^3. Therefore

    T/L <= exp(-2t^3)<1/2.                       (6.4)

### 6.4 Nonvanishing and an explicit sign

The positive real core contribution strictly dominates the absolute complementary contribution. Thus

    sign D_(n,b)=(-1)^(n(b+1)+b),

and, with d=b+1,

    |D_(n,b)| >= a0^(nd) exp(-2d)
       /[d! b! 2^(d^2+4d+2) d^(d^2) n^(d^2/2)] >0.     (6.5)

This proves the main square contact-normality theorem. The cutoff is intentionally conservative; no finite-degree computation is used to improve it.

The special border does not destroy concentration here. Equation (5.2) changes the exponential factor exp(sum z_l) into an average of exp(sum(1-t_l)z_l). Its phase is still uniformly small on the same local region, and its real value at the dominant saddle is nonzero. This exact fact is what permits the proof. Replacing the border by an uncontrolled signed sum of minors would conceal it.

## 7. Full endpoint-rank consequence

Let H_full be the rational contact space for caps (n+1,b,n) and contact M. Its coefficient count is M+3, so dim H_full>=3.

If a member has A(1)=B(1)=C(1)=0, all three coefficient polynomials are divisible by z-1. Dividing them by z-1 gives caps (n,b-1,n-1). Since z-1 is a unit at zero, contact M is unchanged. The square theorem forces the divided triple, and therefore the original triple, to be zero.

The coefficient-endpoint map H_full -> Q^3 is consequently injective. The dimension bound makes it an isomorphism. This also proves independence of the original M contact rows.

The plane of endpoint triples (X,Y,Y) has dimension two. Its inverse image is exactly the matched weighted family. Therefore for every rational pair (X,Y) there is a unique matched triple with those endpoints. In particular there are independent rational solutions with endpoint pairs (1,0) and (0,1), and the family has nonzero-Y directions without imposing any restoring selector.

This argument addresses the whole endpoint map, not only a particular determinant representative. It does not divide by an unproved cofactor and remains independent of the pending balanced audit. A claim about the exact highest-degree coefficient on a particular endpoint direction would require its own minor; that is not needed for full endpoint rank and is not asserted here.

## 8. What this proof does and does not settle

Proved in this note:

1. The exact image, injectivity, degree bound and codimension-one residue condition for the actual n+1-derivative transform.
2. Its explicit exceptional-row b-by-b reduction and equivalent bordered exp(z)Q(z)^n determinant, with both poles retained.
3. A complete simplex/divided-difference integral for that border.
4. Nonvanishing, sign and a quantitative determinant lower bound for every integer n>=ceil(exp(32)), 1<=b<=floor(log n).
5. Full coefficient-endpoint rank three before matching, and rank two after matching, for the unselected weighted allocation.

Not established:

- Normality below the stated cutoff, or in faster growth ranges.
- An optimal cutoff or determinant asymptotic.
- Bounds for the coefficient height of the solution associated with prescribed endpoints.
- A controlled genuinely nonbalanced selected direction with an advantageous primitive normalization.
- Bounds on the actual endpoint denominator q, separation Delta, or normalized complete companion beyond what was already proved in the Christoffel package.
- Nonvanishing or shrinking of X+Y(e+pi), or any conclusion about rationality of e+pi.

The next quantitative problem is to estimate the relevant inverse entries or endpoint interpolation minors for this actual border, retaining the final rational endpoint gcd. Formula (5.3), rather than an unbordered determinant or signed Gram norm, is the appropriate starting representation.

No scans, prior symbolic controls, or independent-review calculations were performed for this note. The proof is self-contained apart from elementary coefficient integration, determinant multilinearity, and the divided-difference formula, whose use and normalization were specified above.
