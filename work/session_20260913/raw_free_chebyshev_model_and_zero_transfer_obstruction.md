> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The canonical free polynomial model and its zero-count transfer obstruction

Date: 2026-09-13. Original continuation by audit_computations; independent root review passed: raw_free_model_root_review.md.

This constructs the constant-coefficient model with its actual polynomial
forcing and both inherited boundary constraints. It proves an exact n=4
model zero bound, an all-index relation to the actual Legendre family,
and a quantitative distinction between pointwise and growing-jet
comparison. It does not prove the all-n mixed zero bound for either
family. The previously proved actual Legendre Chebyshev obstructions
remain valid.

## 1. A specified model rather than arbitrary boundary forcing

Let U_j be the Chebyshev polynomial of the second kind and put

    C_j(t)=i^(-j)U_j(it),
    f_j(x)=Borel[C_j](x)
          =sum_(h=0)^floor(j/2) binom(j-h,h)
                           (2x)^(j-2h)/(j-2h)!.                  (1)

All these polynomials are real with positive coefficients of one parity.
The ordinary recurrence is C_(j+1)=2t C_j+C_(j-1), C_0=1,C_1=2t.
Equivalently the monic family 2^(-j)C_j has the fixed coefficient 1/4.
The exact generating function after the coefficientwise Borel transform is

    sum_(j>=0) f_j(x)z^j
      =1/(1-z^2) * exp[2xz/(1-z^2)].                            (2)

This follows either from (1) or by expanding the Chebyshev generating
function. The standard source is [DLMF 18.12.10](https://dlmf.nist.gov/18.12.E10).
Formula (2) is also a local analytic identity for |z|<1 and arbitrary
fixed complex x, not only a formal coefficient identity.

Define normalized even and odd members by

    E_m^0=f_(2m),       O_m^0=f_(2m+1)/[2(m+1)].

Thus E_m^0(0)=1 and (O_m^0)'(0)=1. With empty products equal to one,

    E_m^0(x)=sum_(j=0)^m
       4^j prod_(h=0)^(j-1)[(m-h)(m+h+1)] x^(2j)/((2j)!)^2,

    O_m^0(x)=sum_(j=0)^m
       4^j prod_(h=0)^(j-1)[(m-h)(m+h+2)] x^(2j+1)/((2j+1)!)^2.
                                                                    (3)

In particular E_0^0=1 and E_1^0=1+2x^2. The even Chebyshev recurrence
and the consecutive difference identity give exactly

    (E_(m+1)^0)''-2(E_m^0)''+(E_(m-1)^0)''=4E_m^0, m>=1,
    O_m^0=[(E_(m+1)^0)'-(E_m^0)']/[4(m+1)].                    (4)

These equations and the displayed starting polynomials specify the
model. No choice of arbitrary boundary functions is made.

## 2. Both original boundary constraints survive

For the free block a<=m<=b put Evec^0=(E_a^0,...,E_b^0)^T,
H_0=L_r (diagonal 2, off-diagonal -1), M_0=4I and
B_0=[e_1,e_r]. Then

    H_0(Evec^0)''+4Evec^0
       =B_0(beta^0)'',
    beta^0=(E_(a-1)^0,E_(b+1)^0)^T,
    Evec^0(0)=1, (Evec^0)'(0)=0.                              (5)

After the alternating-sign gauge its symmetric Jacobi matrix has
diagonal 1/2 and off-diagonal 1/4. The signs and forcing in (5) are
those of gamma=1,delta=4 in the actual coupled system.

Let H_n^0=span(f_(n+1),...,f_(2n-1)). For odd n=2s+1 choose
a=s+1,b=2s+1; for even n=2s choose a=s,b=2s. Formula (4) proves

    n odd: H_n^0={p^T Evec^0+q^T(Evec^0)' : p_b=0, sum q=0},
    n even: H_n^0={p^T Evec^0+q^T(Evec^0)' :
                                      p_a=p_b=0, sum q=0}.    (6)

The coefficient 4(m+1) in (4) is positive and nonzero, so the odd
members span precisely the consecutive derivative-difference
hyperplane. These are the same two or three constraints as for the
actual family; the dimension remains n-1.

The genuine Laplace forcing also has a closed form:

    Ehat_m^0(s)=(-1)^m U_(2m)(i/s)/s,  s>0.                  (7)

It follows by integrating each polynomial coefficient in (1).
The row-sum identity H_0 1=B_0(1,1)^T again cancels the initial terms,
so Evec_hat^0=s^2(4I+s^2H_0)^(-1)B_0 beta_hat^0. The free
resolvent therefore acts on the specified polynomial boundary data,
not on independent oscillatory forcing modes.

## 3. The free scalar differential operator is different

The imaginary Chebyshev equation and the factorial coefficient
recurrence give

    L_0 f_j=j(j+2) f_j,
    L_0=x^2 D^4+4xD^3+(x^2+2)D^2+3xD
       =D^2 x^2 D^2+x^2D^2+3xD.                            (8)

For example the coefficient recurrence is

    (r+2)^2(r+1)^2 [x^(r+2)]f_j
       =[j(j+2)-r(r+2)] [x^r]f_j.

This is not the actual Legendre scalar operator, whose last term
is 2xD and whose eigenvalue is j(j+1). More strongly, no positive
scalar weight makes L_0 formally self-adjoint on an interval of
positive x. Formal self-adjointness first forces

    4x=2[(w x^2)'/w],

so w is constant. For constant weight the coefficient of D would
have to equal (x^2+2)'-(x^2)'''=2x, which disagrees with 3x.
Thus the actual scalar self-adjoint/Volterra factorization cannot
simply be imported into this free model. This does not contradict
the symmetric finite matrix pencil in (5).

## 4. An exact, bounded n=4 model theorem

This section uses only the predeclared n=4 block, without extending
the degree search. In the ordered basis (f_5,f_7,f_6), the first
Wronskian is positive on x>0, and the next two are

    W_2=32x^3/4725 *
                (2x^8+80x^6+1605x^4+4410x^2+11025),

    W_3=-32x/212625 * T(x^2),                                (9)

where

    T(y)=8y^7+60y^6+4860y^5+95400y^4-769500y^3
                       +1148175y^2+4961250y-1488375.

Both W_1=f_5 and W_2 are strictly positive on (0,1).
Also T(0)<0<T(1)=3951878 and T'>0 on [0,1]. Indeed the only
negative term in T' is -2308500y^2; combine it with 2296350y
using y^2<=y, and its possible negative remainder is only -12150y,
dominated by the positive constant 4961250. Hence W_3 has precisely
one simple interior zero.

For every f in this three-dimensional span, division by f_5 and
then division of its derivative by (f_7/f_5)' are nonsingular
operations on (0,1). Their second weighted derivative is a constant
multiple of W_3, with a nonvanishing denominator. Rolle's theorem,
including multiplicities, therefore proves

    every nonzero f in H_4^0 has at most three zeros in (0,1).  (10)

If the coefficient of f_6 is zero, the same two-function argument
gives at most one zero. Thus (10) includes that exceptional case.

The three-zero bound is sharp in the multiplicity sense. At the
simple W_3 zero, the first three evaluation-derivative rows have
rank two because W_2 is nonzero. Their kernel supplies a nonzero
combination with a triple zero. Its third derivative is nonzero:
W_3'=det(rows 0,1,3) at this point, and W_3' is nonzero. A small
perturbation within the span by a function vanishing there with
nonzero first derivative splits it into three distinct nearby
real zeros, with the appropriate sign of the perturbation.

Thus even the canonical free model fails the ordinary three-function
Chebyshev bound of two zeros in this actual high block. It nevertheless
satisfies the weaker target of at most n zeros for n=4. This is a
single-degree theorem, not evidence promoted to an all-n conclusion.

The displayed identities and the positive derivative certificate are
independently reproducible with `check_raw_free_chebyshev_fixed_n4.py`;
its exact output is `raw_free_chebyshev_fixed_n4_checks.json`. The
control is restricted to this declared block and its required lower
rows, without an expanded index search.

## 5. An exact all-index relation to the actual family

Define l_j(x)=Borel[i^(-j)P_j(it)](x), so the actual F_j differs
from l_j only by a positive degree-dependent leading normalization.
The Legendre generating function after Borel transformation is

    sum l_j(x)z^j=(1-z^2)^(-1/2) exp(u) I_0(u),
    u=xz/(1-z^2).                                            (11)

This is also the already derived formula in
`raw_borel_legendre_literature.md`. Define the normalized dilation
average

    (A f)(x)=integral_0^1 f(sx)ds/[pi sqrt(s(1-s))]
            =(1/pi)integral_0^x f(t)dt/sqrt(t(x-t)).           (12)

The elementary identity
integral_0^1 exp(2us)ds/[pi sqrt(s(1-s))]=exp(u)I_0(u)
follows from s=(1+cos(theta))/2 and the
[I_0 integral in DLMF 10.32.1](https://dlmf.nist.gov/10.32.E1).
Combining (2),(11),(12) proves exactly

    sum l_j z^j=sqrt(1-z^2) * A[sum f_j z^j],
    l_j=sum_(h=0)^floor(j/2) b_h A f_(j-2h),
    b_h=(-1)^h binom(1/2,h).                                 (13)

Here b_0=1 and EVERY b_h for h>=1 is negative. These are finite
polynomial identities for every index. In particular a high actual
row contains lower same-parity model rows, down to degree zero or
one, after the averaging map. The inverse index transformation has
the positive coefficients of (1-z^2)^(-1/2), but again introduces
all those lower rows. It does not preserve the prescribed high block.

## 6. The positive averaging map is not a variation theorem

The kernel in (12) is positive, but it is not sign-regular of order
two on its full Volterra domain. Removing its positive column factor
t^(-1/2)/pi leaves K(x,t)=(x-t)^(-1/2) for t<x and zero otherwise.

For t_1<x_1<t_2<x_2 its 2-by-2 evaluation determinant is positive
by triangularity. In contrast, for t_1<t_2<x_1<x_2,

    (x_1-t_1)(x_2-t_2)
       -(x_1-t_2)(x_2-t_1)=(x_2-x_1)(t_2-t_1)>0.

Taking reciprocal square roots shows that the corresponding
2-by-2 determinant is strictly negative. Thus the two configurations
give opposite signs without any endpoint singularity. A positive
averaging argument supplies no general variation-diminishing theorem
for A. This exact obstruction is for arbitrary inputs of the averaging
operator; it is not a counterexample to the zero count for the
specific model family. Combined with the lower-row mixing in (13),
it identifies two separate missing hypotheses in a proposed direct
transfer of a free-model Chebyshev theorem to the actual high block.

## 7. Pointwise closeness versus high-order derivative closeness

There is nevertheless a useful quantitative comparison of the actual
normalized parity members E_m,O_m and the model E_m^0,O_m^0.
Their coefficient ratios, for 0<=j<=m, are exactly

    [x^(2j)]E_m^0 / [x^(2j)]E_m
       =prod_(h=0)^(j-1) (m+h+1)/(m+h+1/2),

    [x^(2j+1)]O_m^0 / [x^(2j+1)]O_m
       =prod_(h=0)^(j-1) (m+h+2)/(m+h+3/2).                  (14)

For m>=1 both ratios lie between 1 and exp(j/(2m)). With
c=exp(1/(4m)), coefficient positivity gives

    E_m(x)<=E_m^0(x)<=E_m(cx),
    O_m(x)<=O_m^0(x)<=c^(-1)O_m(cx),   x>=0.                  (15)

For completeness, a uniform logarithmic derivative bound can be
derived directly from the same coefficients. For either actual
parity polynomial F=E_m or F=O_m, turn its positive monomial terms
at x>0 into a probability distribution on their degrees N. Their
factorial recurrence gives

    expectation[N^2(N-1)^2]<=4(m+1)^2 x^2.

Since N<=1+sqrt(N(N-1)) for every integer N>=0, Jensen/Hölder yield

    x F'(x)/F(x)<=1+sqrt(2(m+1)x).                            (16)

The recurrence's constant is 4m(m+1/2) for the actual even member,
and 4m(m+3/2) for the actual odd member, both at most 4(m+1)^2.
Integrating (16) from x to cx, subtracting log(c) for the odd
case in (15), and using c<=exp(1/4)<4/3 proves

    1<=E_m^0(x)/E_m(x)<=exp(1/sqrt(m)),
    1<=O_m^0(x)/O_m(x)<=exp(1/sqrt(m)), 0<x<=1.               (17)

For example log of the even upper ratio is at most
[1+sqrt(2(m+1)c)]/(4m)<=1/sqrt(m); the odd estimate is smaller.
This comparison is for the specified origin normalizations.

However, take j=m in (14). In either parity,

    ratio of highest nonzero derivatives tends to sqrt(2),
    rather than to one.                                     (18)

An elementary proof takes logarithms: the sum is
(1/2)sum_(h=0)^(m-1)1/(m+h+alpha)+O(1/m), with alpha=1/2
or 3/2, and this Riemann sum tends to (1/2)log(2).
Thus the relative error in the highest derivative tends to
sqrt(2)-1 even though the function-value relative error in (17)
tends uniformly to zero. No numerical sample is used in (14)-(18).

## 8. The remaining precise model and perturbation problems

The model problem is now unambiguous: prove or refute that every
nonzero f in the specific H_n^0 of (6) has at most n zeros on
(0,1). The constant matrix alone, without its two polynomial boundary
members, is insufficient. The single-degree theorem (10) does not
settle this all-index assertion.

Even an affirmative model theorem would require a quantitative
stability argument before implying the actual assertion. One exact
possible formulation uses the (n+1)-by-(n-1) Hermite divided-difference
evaluation matrix of f_(n+1),...,f_(2n-1), with positive column
normalizations fixed and ordered nodes in [0,1]. A lower singular-
value bound, uniform also as nodes coalesce, could be compared with
the corresponding actual matrix error. Function-value comparison
(17) alone does not bound that error in a growing confluent norm;
(18) explicitly prevents one from asserting that all normalized
derivatives become relatively close. The lower-row mixing and lack
of a sign-regular averaging kernel in (13) supply additional exact
obstructions to bypassing this issue by a positivity argument.

No false full-block Chebyshev statement, new high-row rank result,
primitive arithmetic conclusion, or irrationality proof is claimed.
