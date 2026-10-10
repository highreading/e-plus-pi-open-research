> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# General ordinary cells: a both-parity bridge and zero average for the whole common-log radical support

2026-09-13. Status: new auxiliary derivation using the archived exact Hermite/tensor certificate and the two algebraic branches. Every fixed ordinary j>=1 common-log collision support has zero normalized dyadic average. A uniformly summable raw tail extends this to the entire Item197 ordinary common-log radical support. No full valuation estimate or assertion about e+pi follows. Independent review: general_cell_independent_check.py/.json and the separate reviewer note.

## 1. Exact general-cell input and the result

Item197, equations(4.7)-(4.8), proves on every ordinary PNT row with j>=1

    4M+1=(2j+1)p-2s, 1<=s<=(p-3)/6, 3j+1<p,
    r=(p-6s-3)/2,

that the actual divided logarithmic coordinates are

    C_nu(M)/p = A_j X_nu+B_j Y_nu+C_j Y'_nu mod p,

where nu=0,1 and

    A_j=(3j+1)U_j, B_j=-(2j+1)V_j, C_j=-(2j+1)W_j,
    U_j=[y^(2j)](1-y)^(3j)/(1+y^2)^(2j+1),
    V_j=[y^(2j)](1-y)^(3j+1)/(1+y^2)^(2j+2),
    W_j=[y^(2j-1)](1-y)^(3j+1)/(1+y^2)^(2j+2).

All three constants are integers. Here C_j is a fixed coefficient, distinct from the actual sequence C_nu(M). Integrality of M forces r even when j is odd and r odd when j is even. Actual primes force r>=1 and3 does not divide r.

The following necessary gate is proved below for every fixed j, outside a fixed finite prime set depending on j:

    actual simultaneous collision
      => 2(-1)^r A_j 2^(2s) a_r+(A_j+2B_j)b_r=0 mod p.       (1)

The coefficients a_r and b_r are exactly the two branches of Items309/314, with b_r=[x^r]C_+(x). Neither a norm nor a fitted recurrence replaces the actual collision in (1). The implication need not be sufficient.

If (A_j,B_j)!=(0,0), the right side of (1), on the actual fixed-p rows, is a nontrivial constant linear combination of the two same-operator sequences already used in the Roth proof. Consequently that fixed cell has Z_j(p)=o(p), with the same quantitative exp(-c(log log p)^(1/9)) factor, and its radical collision mass has dyadic average o(X^2).

If A_j=B_j=0, Section6 proves C_j!=0. The original actual pair then forces f_0=f_1=0, so D_u=0 and hence b_r=0. This single-branch gate has the same density conclusion. Thus every fixed j>=1 is admitted, including any exceptional j where (1) itself is identically zero.

For j=3, exact coefficient extraction gives

    (U_3,V_3,W_3)=(126,30,348),
    (A_3,B_3,C_3)=42(30,-5,-58).

Thus r is even and (1) simplifies, after excluding fixed scalar primes, to

    actual ordinary j=3 collision => 3*2^(2s)a_r+b_r=0 mod p. (2)

This proves the j=3 support result. Its raw cell mass is M/35+o(M), or1/210 per6M; the retained mass has zero normalized dyadic average.

## 2. A parity-uniform version of the ordinary tail reduction

Put Q=2s, q=-(2r+3)/3, c=2^Q, and

    K_0(z)=(1-z)^r(1+z),
    K_1(z)=(1-z)^r(1+z)^4,
    P_nu(z)=K_nu(z)(1+z^2)^(Q-nu).

The original X_nu uses the low target tau_nu=p-Q+nu-1. The identities A_p(z)=-z^p A_p(1/z) and K_nu(z)=(-1)^r z^(r+1+3nu)K_nu(1/z) reflect it to T=p-r-1. For any n beyond the polynomial degree,

    [z^n]P(z)log(1-z)=-sum_k P_k/(n-k).

Reversing P's coefficients supplies a second factor (-1)^(r+1). The two signs cancel, so for both parities the original low X_nu equals

    integral_0^1 t^(Q-nu)K_nu(t)(1+t^2)^(Q-nu)dt mod p.     (3)

Every integral denominator lies between1 and T<p. This establishes the same X-tail used in Item250 for both parities, without retaining the odd-r sign convention by accident.

Define J_k=sum_(t=0)^(Q-1) binom(Q-1,t)/(Q+k+2t). Item250's exact recurrence

    (3Q+k)J_(k+2)=c-(Q+k)J_k

and its resonant terminal at k*=2r+3 give J_k*= (c-1)/(Q+k*) modulo p. The unique top summand responsible for -1 is retained. No step uses r odd. The same ascending even chain and descending odd chain yield

    X_nu=a_nu e+b_nu c+d_nu.                              (4)

These lower-case a_nu,b_nu are affine-tail coordinates, distinct from branch coefficients a_r,b_r.

The lower B-tail is a rational number u_nu=Y_nu at the phase. With N=r+q+1=r/3, and writing K_nu=sum k_(nu,l)z^l,

    u_0=C_0 sum_t k_(0,2t)(-1)^t(-N)_t/(-r)_t,
    u_1=C_1 sum_t k_(1,2t+1)(-1)^t(-N)_t/(-r-1)_t,
    C_0=(-1)^r r!/(q+1)_(r+1),
    C_1=(-1)^(r+1)(r+1)!/(q)_(r+2).                       (5)

All sums terminate before a denominator Pochhammer vanishes. For the upper tail, let epsilon=r mod2, h=floor(r/2),

    D=(r+3-3epsilon)/6, R=-(r+1+epsilon)/2, rho=-D/q.

Then

    f_0=sum_t k_(0,epsilon+2t)(-1)^t(-R)_t/(1-D)_t,
    f_1=rho sum_t k_(1,epsilon+2t)(-1)^t(-R)_t/(-D)_t,
    Y'_nu=(-1)^r f_nu mathfrak_f.                         (6)

The common factorial period mathfrak_f has p-unit denominator and numerator on an actual row. Formula(6) uses the actual parity of T, which is epsilon. Its phase values differ from Item250's odd-r values when epsilon=0.

The unit proof is the same actual-representative proof as Item250 Section7: every ordinary forward or backward pivot is strictly between0 and p, the unique resonant p-pivot is handled before reduction, and all factorial arguments are less than p. Phase denominators are reductions of those representatives. Numerator zeros in f_nu are allowed and are never inverted.

## 3. Two all-r identities remove the affine and homogeneous periods

First,

    d_nu=u_nu/2 for nu=0,1.                                (7)

Here is a termwise proof. The constant coordinate of an even J_k is zero. The constant coordinate beta_(2t+1) of an odd J is, by the descending recurrence at q=-(2r+3)/3,

    beta_(2t+1)=-(r+1-t)!/[2(t-r/3)_(r+2-t)].

Thus

    beta_(2t+1)+beta_(2t+3)
      =-(r-t)!/[2(t-r/3)_(r+1-t)].

Pochhammer reversal gives

    C_0/2=-r!/[2(-r/3)_(r+1)],
    C_1/2=-(r+1)!/[2(-r/3)_(r+2)].

Multiplying these by the two respective coefficient ratios in(5) gives exactly the preceding beta expressions. The X_0 formula sums beta_(l+1)+beta_(l+3) over even l, and X_1 sums beta_l over odd l. This proves(7) before summation and for both r parities.

Second, the homogeneous coordinates satisfy

    a_nu=kappa_r f_nu,
    kappa_r=(-1)^(r+h)(-D)_(h+2)/[rho(-R)_(h+2)].           (8)

For a direct coefficient proof put H_t=(-1)^t(q/2)_t/(3q/2)_t. The homogeneous X coordinates are

    a_0=sum_(t=0)^h k_(0,2t+1)(H_(t+1)+H_(t+2)),
    a_1=sum_(t=0)^(h+2) k_(1,2t)H_t.

Reverse the K coefficients using k_(nu,l)=(-1)^r k_(nu,r+1+3nu-l). In a_0 the reflected index is epsilon+2(h-t); in a_1 it is epsilon+2(h+2-t). The two scalar identities are

    H_t=kappa_r rho(-1)^(r+h+2-t)(-R)_(h+2-t)/(-D)_(h+2-t),

    H_(t+1)+H_(t+2)
      =kappa_r(-1)^(r+h-t)(-R)_(h-t)/(1-D)_(h-t).

Their successive-t quotients agree by substitution of q,D,R. The first at t=0 is the definition of kappa. For the second, divide its t=0 right side by the first identity's t=0 right side: the result is

    (-D)(h+1-D)/[rho(-R+h)(-R+h+1)]
      =q(h+1-D)/[(-R+h)(-R+h+1)]
      =-2q/[3(3q+2)]=H_1+H_2.

This proves both scalar identities and hence(8). None of their denominators vanishes when r>0 and3 does not divide r.

Substituting(7)-(8) into the actual general-j coordinates gives

    G_nu=f_nu[A_j kappa_r e+(-1)^r C_j mathfrak_f]
           +A_j b_nu c+(A_j/2+B_j)u_nu.

Take f_0G_1-f_1G_0, without division by either f coordinate. Every actual collision therefore forces

    A_j c D_b(r)+(A_j/2+B_j)D_u(r)=0 mod p,
    D_b=det(f,b), D_u=det(f,u).                            (9)

The coefficient C_j disappears by a proved rank-one cancellation, not by deleting one of the original coordinates.

## 4. The even-r branch bridge

The odd-r bridges in Items306/309 already prove D_b and D_u are unit gauges of opposite-signed a_r and b_r. Here is the missing even-r continuation.

Use the Item306 periods, now for any integer r>0 with3 not dividing r:

    A_r=FP integral_0^1 u^r(1-u^2)^(b-1)(1-iu)^r(1+iu)du,
    B_r=FP integral_0^1 u^r(1-u^2)^(b-1)(1-iu)^r
                          (1+iu)^4/(1-u^2)du,
    b=-2r/3, a=(r+1+epsilon)/2.

Let part_0 denote the real component and part_1 the imaginary component. Coefficient expansion and the beta recurrence give

    f_nu=2 part_epsilon(A_r,B_r)_nu/B(a,b),
    u_nu=2(-1)^(h+epsilon)part_(1-epsilon)(A_r,B_r)_nu.       (10)

For the first identity, B(a+t,b)/B(a,b)=(a)_t/(a+b)_t, with a=-R and a+b=1-D. For nu=1, B(a,b-1)/B(a,b)=rho, producing the common normalization.

For the second identity, reverse the K coefficients in(5). The opposite parity has a_opp=(r+2-epsilon)/2=h+1, an integer. The reversal factor is

    C_0(-1)^(r+h+epsilon)(a_opp+b)_(h+epsilon)/(a_opp)_(h+epsilon)
      =(-1)^(h+epsilon)B(a_opp,b).

The beta denominator then cancels. The nu=1 identity follows from the same reversal with b replaced by b-1 and its factorial prefactor C_1. Thus(10) is an equality of finite beta expansions. It is not a conjectural relation among periods.

More explicitly, with the period branches inherited from Item306,

    D_u=4(-1)^(h+1) Im(A_r conjugate(B_r))/B(a,b).

It follows that D_u is the same exterior period determinant as Item306, with the displayed normalization. Its six-step ratio is

    K_even(r)=64(r+6)(2r+3)(2r+9)/[27(r+1)(r+3)(r+5)]

when r is even; for odd r it is the previously proved

    K_odd(r)=64(r+3)(2r+3)(2r+9)/[27r(r+2)(r+4)].

For D_b, use the Frobenius-free meromorphic version of(4), X_nu=a_nu E+b_nu2^q. The resonant correction changes only d_nu, not b_nu. The inversion t=1/z gives the same Item309 kernel X(z)=z(1-z)/(1+z^2)^(2/3), with sign (-1)^(r+1). Let I_delta be the vector of the two original Item309 form integrals on delta=(0,i)-(0,-i), with local branch X(z)/z->1 at0, and let I_Gamma be the corresponding vector on Gamma=(infinity,1), with its branch inherited under t=1/z. Parameterization z=+/-iu gives

    I_delta=2 i^epsilon i^(r+1) part_epsilon(A_r,B_r),
    D_b=(-1)^(r+1)det(I_delta,I_Gamma)
             /[i^epsilon i^(r+1) 2^q B(a,b)].

The beta contour selecting f changes from its imaginary to real part when r is even, exactly as in(10). In the displayed prefactor, i^(r+1) changes sign under r->r+6, q decreases by4, and epsilon is unchanged. Its six-step ratio is therefore16 K_even(r). This explicitly retains the sign change in the complex phase.

The eight Item306 Hermite identities and its three cleared tensor identities are identities over Q(r). Their endpoint proof also applies for even r: at0 and1 the exact primitives vanish to order r+1, and exponents at +/-i and infinity lie in Z-2r/3 or Z+2r/3, which contain no zero. Hence the same meromorphic finite-part functional kills every exact term. No divergent literal endpoint is discarded.

Define, for even r,

    R_even(r)=(r+3)^2(2r+9)^2(2r+15)^2
       /[78732(r+1)(r+2)^2(r+4)^2(r+5)],
    g_0=1, g_n/g_(n+1)=R_even(e+6n), e=2 or4.

It satisfies R_even K_even=R_odd K_odd, the exact weight in Item306's tensor identity. Therefore both sequences

    16^n D_u(e+6n)/g_n,
    D_b(e+6n)/g_n

satisfy Item237's P_j(r/2) recurrence. The second comparison sequence16^(-n)a_(e+6n) satisfies that same recurrence by Item309's global other-branch differential identity; this formal coefficient identity has no parity restriction. The first comparison sequence is b_(e+6n).

Three separate exact initial identities per even ray give

    16^n D_b(e+6n)/g_n=lambda_e a_(e+6n),
    16^n D_u(e+6n)/g_n=lambda_e b_(e+6n),
    lambda_2=-729/98, lambda_4=59049/3025.                  (11)

These initial identities are evaluated from the finite tail formulas, not from the recurrence. Item237's forward polynomial is positive at r/2>0, so the all-index recurrence propagates them. This completes the parity extension.

Every variable factor in g_n is an actual-row p-unit: in the product up to r, the largest shifted factor is2r+3<p, and the fixed scalar78732 is supported at2,3. The lambda_e factors require excluding only a fixed finite set of primes. The branch coefficient denominators have the global p-unit clearer6^(r+3)r! from Item314, valid for all coefficient indices. Thus(11) can be reduced modulo every sufficiently large actual prime.

Combining (9), (11), and the odd-r Item306/309 bridges proves(1).

## 5. Actual nonzero states and the fixed-j density consequence

For e=2,4 the exact first-two-coordinate determinants of the branch pair

    (16^(-n)a_(e+6n), b_(e+6n))

are respectively

    -4424709835/1594323,
    3604770571325/774840978.

They are nonzero. The odd-ray determinants e=1,5 are already recorded and proved in the j=2 note. If (A_j,B_j)!=(0,0), the two coefficients in (1) cannot both vanish modulo every sufficiently large prime; exclude the finite prime divisors of their common integer numerator content. The initial two-state is then nonzero because these determinants are units.

At fixed p, r=e+6n and s=s0-2n, so c=4^s0 16^(-n). The gate(1) is therefore a constant linear combination of the same-operator branch pair. The reverse monic recurrence excludes four consecutive zeros and bounds zero three-states by five, using p=2r+6s+3 exactly as in the preceding j=1 and j=2 proofs. All observation determinant and limiting-cubic hypotheses are unchanged. The quantitative Roth lemma applies.

For any fixed j, the additional ordinary condition3j+1<p omits only finitely many primes. The actual index map is

    M=((3j+1)p+e)/6+n.

This yields the dyadic averaged support estimate by summing Z_j(p)log p up to p=O_j(X). In particular j=3 is now admitted unconditionally from its explicit nonzero vector.

## 6. Nonvanishing of the coefficient triple and a rigorously uniform tail

The integer triple (U_j,V_j,W_j) cannot vanish simultaneously for any j>=1. To prove this set

    S(y)=(1-y)^(3j+1)/(1+y^2)^(2j+2)=sum_(k>=0) S_k y^k,
    R(y)=(1-y)^(3j)/(1+y^2)^(2j+1).

Then V_j=S_(2j), W_j=S_(2j-1), U_j=[y^(2j)]R. Direct differentiation gives

    ((1+y^2)S)'=-(3j+1)R-(4j+2)yS.

Taking coefficient y^(2j) yields

    (2j+1)S_(2j+1)=-(3j+1)U_j-3(2j+1)W_j.            (12)

Consequently a zero triple would force S_(2j-1)=S_(2j)=S_(2j+1)=0. But the first-order rational differential equation for S is

    (1-y)(1+y^2)S'=[-(3j+1)-(4j+4)y+(j+3)y^2]S,

so for each k>=2 its coefficients satisfy

    (k+1)S_(k+1)+(3j+1-k)S_k+(k+4j+3)S_(k-1)
                          -(k+j+1)S_(k-2)=0.          (13)

Starting at k=2j and descending to2, the coefficient k+j+1 is always a nonzero positive integer. Three consecutive zeros therefore propagate backward to S_0=0, contradicting S_0=1. This proves the triple nonvanishing over the rational numbers for every j, without a finite-index search.

For the only case not admitted by (1), namely A_j=B_j=0, this lemma gives C_j!=0. Outside its finite prime divisors, the original pair is

    G_nu=C_j(-1)^r mathfrak_f f_nu.

The factorial mathfrak_f is an actual-row unit, so a collision forces both f coordinates zero. In particular D_u=det(f,u)=0. The parity-specific p-unit bridge proved in Section4 and Items306/309 then gives b_r=0. The single b sequence has nonzero initial state (the two-branch initial determinant is already a unit) and exactly the same forward observation and reverse-state bounds. Thus the Roth conclusion applies in this case as well. We have now admitted every fixed j>=1.

For a fixed cell, the raw prime interval has endpoints

    p=4M/(2j+1)+O(1), p=6M/(3j+1)+O(1),

so its PNT mass is

    [6/(3j+1)-4/(2j+1)]M+o(M)
      =2M/[(3j+1)(2j+1)]+o(M).

These fixed-j caps are summable. More usefully, no uniform PNT error is needed for the tail. If j>J, the defining row inequality gives

    p<=6M/(3J+4).

There is at most one actual cell per pair (M,p), as proved in Item197. Hence Chebyshev's estimate bounds the logarithmic mass of the whole raw ordinary tail by O(M/J), uniformly in M and J>=1. The possible r=0 endpoint has no prime p>3, and any separately omitted small-prime/ordinary boundary only reduces this support bound.

Let R_M be the product of the distinct primes in the Item197 ordinary j>=1 cells at M for which both actual logarithmic coordinates vanish. For each fixed J, the preceding fixed-cell theorem gives

    sum_(X<=M<2X) sum_(1<=j<=J) log R_(M,j)=o_J(X^2).

The tail contributes O(X^2/J), with an absolute implied constant independent of J. Consequently

    limsup_(X->infinity) X^(-2) sum_(X<=M<2X) log R_M=O(1/J)

for every fixed J. Letting J tend to infinity proves

    sum_(X<=M<2X) log R_M=o(X^2).                       (14)

Thus the **whole Item197 ordinary common-log radical support** has zero normalized dyadic average. Equivalently log R_M=o(M) on a set of construction indices of natural density one. This is the Item197 common-log support, not the larger first-Witt determinant locus of Item426; the two loci have different defining conditions. Equation(14) is not asserted pointwise on every M and carries no unbounded valuation multiplicity.

## 7. Scope and verification

The proof imports Item197's exact actual bridge; Item250's recurrence/terminal and unit arguments, whose parity changes were explicitly derived above; Item306's rational Hermite/tensor identity and meromorphic endpoint theorem; and Item309/314's two formal algebraic branches. The new algebra is the both-parity affine identity, both-parity rank-one formula, even beta normalization/gauge, exact even initials and actual-state determinants, the all-j coefficient-triple lemma and exceptional-branch handling, and the uniform raw-tail estimate.

The companion `check_general_cell_extension.py` checks the new rational identities, the gauge-weight equality, all six even bridge initials, both initial determinants, and the exact j=3 coefficient vector. These are initial-value and identity checks supporting the all-index proof. They are not a prime-density experiment. The large archived tensor certificate is an explicit imported proof dependency; it was not recomputed from scratch here.

No unbounded valuation sum is controlled. Each fixed deeper gate contained in one admitted ordinary collision support inherits the support estimate, as does any fixed finite union of such layers. Passing to all valuation depths still requires a uniform tail estimate for multiplicities. A sparse exceptional sequence of construction indices also remains possible despite the density-one/averaged statements.
