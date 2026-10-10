> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# All inverse-column hook congruences and primitive endpoint units

Date: 2026-09-13. Original continuation by root. Independent review: **FULL PASS**
after the Section 3 transcription and Section 5 orientation corrections;
see raw_appell_column_endpoint_independent_review.md.
This extends the reviewed Appell full/corner congruence to every cofactor,
then uses the primitive original polynomial to transfer it to the actual
endpoint arithmetic. No saturation hypothesis is used.

Retain n>=1, a_k(x)=[z^k]e^(xz)(1+z^2)^n, and

    A(x)=(a_(n+i-j)(x))_(0<=i,j<=n),       D(x)=det A(x).

At x=1 let v(z)=sum_j (A(1)^(-1))_(j0) z^j. All exact polynomial
normalizations U,V,W,Qhat,Pe,Pa are those of the reviewed dual notes.
The Appell theorem proves that every augmented Schur polynomial below
is an integer polynomial congruent to x^(its partition size) modulo 2n.

## 1. Every inverse-column cofactor has an explicit hook ratio

Let lambda_D=(n^(n+1)). For 0<=j<=n, deleting row zero and column j,
then transposing, gives the ordinary Jacobi--Trudi determinant for

    lambda_j=((n+1)^j,n^(n-j)),       |lambda_j|=n^2+j.

Indeed its l-th row has index n+i-k_l, where k_l=l-1 for l<=j
and k_l=l for l>j; this is lambda_(j,l)-l+i. The cofactor sign is
(-1)^j. Write M_j(x)=H_j s_(lambda_j)(a(x)) and M_D=H_D D(x),
where H denotes the product of hook lengths. Then

    M_j,M_D in Z[x],       M_j(x)=x^(n^2+j) mod 2n,
    M_D(x)=x^(n(n+1)) mod 2n.                            (1)

The hook ratio is

    H_D/H_j=r_j=(2n-j)!/[j!(n-j)!].                      (2)

For a direct check, relative to the square lambda_0=(n^n), the
factorial numerator in the hook formula changes by (2n)!/(2n-j)!.
The cross-block Vandermonde changes by binom(n,j). Since
H_D/H_0=(2n)!/n!, their quotient gives (2). Equivalently the degree
set is {n,...,2n} with 2n-j omitted. Each r_j is an integer, since
r_j=binom(2n-j,n)n!/j!.

All M_j(1) and M_D(1) are congruent to one modulo 2n and nonzero.
Thus every coefficient v_j is nonzero, and exactly

    v_j=(-1)^j r_j M_j(1)/M_D(1).                        (3)

In particular for every prime p|2n,

    v_j/[(-1)^j r_j] in 1+2n Z_(p).                     (4)

This is an exact rational congruence, not a congruence applied to
unscaled rational Taylor coefficients. It also proves deg(v)=n in
every degree; the even two-function accessory K consequently has
degree exactly two.

## 2. Primitive factorial-normalized coefficients

Write U(t)=sum_(j=0)^n U_j t^j and define the integers

    b_j=U_j/(n+j)!.

Their integrality was proved by the original reversed division.
For completeness the exact formula is

    b_j=w_(2n+j)+sum_(h>=1, j+2h<=n)
       (-1)^h binom(n+h-1,h) (n+j+2h)!/(n+j)!
                    w_(2n+j+2h),                       (5)

where W(t)=t^n(t-1)^n V(t)=sum_k w_k t^k and V is primitive.
The map from V's coefficients to w_(2n),...,w_(3n) is triangular
over Z with diagonal one. The map (5) has the same property. Both
are unimodular, so

    gcd(b_0,...,b_n)=1.                                  (6)

Moreover every off-diagonal coefficient in (5) is divisible by 2n.
For h>=1, use

    binom(n+h-1,h)=(n/h)binom(n+h-1,h-1).

The product of 2h consecutive integers (n+j+1)...(n+j+2h) is
divisible by 2h. Their product with n/h is therefore an integer
multiple of 2n. This proves

    b_j=w_(2n+j) mod 2n.                                (7)

The exact dual identity q(z)=z^n U(1/z)=n!V(1)v(z), together
with (2)--(3), gives the unambiguous formula

    b_j=(-1)^(n-j) binom(n,j) V(1)
                     M_(n-j)(1)/M_D(1).                (8)

For p|2n each last quotient is a unit congruent to one modulo 2n.
Thus v_p(b_j)=v_p(V(1))+v_p(binom(n,j)). The minimum over j is
v_p(V(1)), because the endpoint binomial coefficients are one.
Equation (6) forces this minimum to be zero. Consequently

    gcd(V(1),2n)=gcd(Vlead,2n)=1.                        (9)

This is stronger than equality of their p-valuations. In particular,
no undetected common scaling survives in this step.

## 3. A polynomial monomial congruence modulo 2n

Equations (1), (7), and (8) imply at every p|2n, to full depth v_p(2n),

    w_(2n+j)=(-1)^(n-j)binom(n,j)V(1) mod p^(v_p(2n)).

The right side is exactly the high-coefficient vector of
t^(2n)(t-1)^n V(1), corresponding to V(t)=V(1)t^n.
Inverting the same unimodular
triangular map from V coefficients and combining the prime powers
proves the global integer-polynomial congruence

    V(t)=V(1)t^n mod 2n.                                (10)

In particular Vlead=V(1) mod 2n and every lower coefficient of V
is divisible by 2n. This retains every prime power in that modulus.

## 4. Exact local content of U and a divisor of Qhat

For p|2n, equations (3) and q=n!V(1)v imply

    v_p(U_(n-j))=v_p(n!)+v_p(r_j).

All r_j are integers and r_n=1. Therefore

    v_p(content U)=v_p(n!),       p|2n.                 (11)

Multiplication by (1+t^2)^n preserves integer content by Gauss's
lemma, or directly by its monic primitive triangular coefficients.
Put S(t)=(1+t^2)^n U(t). The actual reconstruction says

    Qhat(z)=z^(2n) S^(n)(1/z)/n!.

Its coefficient from S_k is binom(k,n)S_k. Thus content U divides
content Qhat globally, and (11) proves

    v_p(content Qhat)>=v_p(n!),
    v_p(Z)>=v_p(n!),       Z=Qhat(1),       p|2n.         (12)

There is no assumption here that a derivative preserves content:
the division by n! has been accounted for by the integer binomial.

## 5. The exponential endpoint is a unit at these primes

The reviewed integer endpoint border is, in terms of the actual
primitive V coefficients,

    Pe(1)=sum_(r=0)^n V_r D_(n,r),
    D_(n,r)=sum_(j=0)^(n+r) binom(n+j,j)(n+r)_j.          (13)

This is the same signed cofactor identity from
raw_fixed_prime_primitive_denominator_gate.md, with V_r=(-1)^(n+r)
c_r delta_r/h in that note's primitive orientation. Changing the
common orientation changes both sides together.

The sign also follows without the difference-matrix coordinates:
Pe(1)=(1/n!) integral_0^infty e^(-t) W^(n)(1+t) dt.
Integrating by parts n times, using the order-n zero of W at 1,
gives (1/n!) integral_0^infty e^(-t)t^n(1+t)^n V(1+t) dt.
The integrations introduce no minus sign. Expanding V gives (13).

Every nonconstant term of D_(n,n) contains the factor 2n. Hence
D_(n,n)=1 mod 2n. Using (10) in (13) gives

    Pe(1)=V(1) mod 2n.                                  (14)

It is therefore a p-unit for every p|2n. No positivity or absence
of cancellation in a general weighted border has been assumed.

## 6. Consequences for the ACTUAL reduced denominator

Since Pa=[Qhat atan]_(<=2n), its rational Taylor denominators divide
lcm(1,...,2n). Equation (12) implies

    v_p(Pa(1))>=v_p(n!)-floor(log_p(2n)),       p|2n.

If v_p(n!)>floor(log_p(2n)), this is positive. Combining with the
unit (14), the actual N=Pe(1)+4Pa(1) is a p-unit. Therefore

    v_p(q)=v_p(Z)>=v_p(n!)                              (15)

for every p|2n satisfying that inequality, where
q=|Z|/gcd(|Z|,|N|). At p=2 the threshold is unnecessary:
Pe(1) is odd and Pa(1) is an integer, so N is odd for every n,
and v_2(q)=v_2(Z)>=v_2(n!) holds in every degree.
For every fixed prime p, the inequality holds
for all sufficiently large n; consequently along the degrees p|n,

    v_p(q_n)>=n/(p-1)-O_p(log n).                        (16)

This is a proved factorial-depth lower bound on the specified prime-
dividing-degree families. It is not a theorem at primes not dividing
2n. In the sufficient gate of the preceding arithmetic note, the
endpoint excess may compensate for a large weighted-minor loss;
the present proof does not require that loss to be logarithmic.

For illustration, fix degrees divisible by 2*3*5*7*11=2310. The
existing exact dyadic rate and (16) for 3,5,7,11 imply

    liminf log(q_n)/n >= (3/2)log 2
                        +log3/2+log5/4+log7/6+log11/10
                      >5log(phi),       phi=(1+sqrt5)/2.

Thus the already proved error criterion rules out shrinking primitive
forms along this particular divisible-degree family; in fact their
absolute values tend to infinity there. Therefore the complete
sequence over all even degrees cannot tend to zero. A sufficiently
large fixed prime set yields analogous stronger exclusions. This
does not rule out other even subsequences and does not decide e+pi.

The main remaining arithmetic work concerns primes not dividing the
degree, or a direct estimate for the reduced denominator on a
promising subsequence. The separate family n=3^nu-1 is of that kind.
