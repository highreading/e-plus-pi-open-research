> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Low Legendre projection: actual recurrence and normalization divisors

Author: Child 2. Status: author-level proofs, not independently reviewed. This stage gives a smaller actual-moment recurrence and an all-degree divisor bounding its primitive-normalization loss. It does not prove a uniform upper bound or small-prime support for zeta_W, nor a denominator theorem for the actual S=e+pi.

## 1. Scope and fixed normalization

The starting report is work/parallel_batch_01/agents/e53af3d9/91945614/ACTUAL_RESIDUAL_QUOTIENT_STAGE1.md. The inherited matrix and lattice identities are in work/session_20261002_codex_continuation/agent2_selector/SHORT_STACK_COMPACT_DIAGONAL_INDEX.md and SHORT_STACK_RIGHT_BLOCK_SCHUR_CONTENT.md. Their factors are retained below. The historical ACTUAL_MOMENT_ORDER_FOUR_RECURRENCE.md concerns a different contour family also denoted W; its recurrence is not transferred here.

Fix k>=2. Put

    rho(y^r)=C_r=D_(2r)-(-1)^r,
    f(y^r)=(2r)!,
    lambda(P)=integral_0^1 P(x^2)dx,
    K(P)=-f((y+1)P)+4lambda(P),
    L=lcm(1,3,...,6k-5).

The actual W' has upper entries rho(ell_i ell_j), 0<=i<k, lower entries L K(ell_i ell_j), 0<=i<k-1, and columns 0<=j<2k, where

    ell_j(y)=4^j P_(2j)(sqrt(y)).

Assume W' has row rank 2k-1 and its right block, columns j=k-1,...,2k-1, has rank k+1. The preceding stage supplies these hypotheses for k>=24 using attributed signed-moment coercivity. Those rank proofs are not repeated. The present algebra applies at any k>=2 satisfying the hypotheses. The two bounded checks concern k=2 and k=4 only.

Let z be the primitive integer Legendre-coordinate vector in ker W'. The inherited polynomial interpretation of the wide loss is

    zeta_W=gcd(z_0,...,z_(k-2))>0.

The task here is to compute and bound the normalization of this projection through actual moments, beyond this inherited identity.

## 2. Primitive scalar moment law and the exceptional initial block

The derangement recurrence gives exactly

    D_(2r+2)=(2r+2)(2r+1)D_(2r)-(2r+1),
    f(y^(r+1))=(2r+2)(2r+1)f(y^r).

The first follows by eliminating D_(2r+1) from D_n=nD_(n-1)+(-1)^n. Every D_(2r) is odd: this holds at r=0 and follows by induction from the displayed recurrence. Thus every C_r is even, and C_1=2 shows their integer content is exactly 2. Define

    rho_0=rho/2,
    c_r=C_r/2 in Z.

This scaling does not remove the endpoint: rho_0=(mu-delta_(-1))/2, where mu is the positive pushforward of exp(-t)dt by y=(1-t)^2.

For m>=2, the leading rho moment Gram matrix has inertia (m-1,1). Indeed, it is a positive definite mu Gram matrix minus the rank-one evaluation vector at -1. Its leading 2 by 2 block is [[0,2],[2,8]], which has a negative direction. Congruence by the positive Gram square root gives I-vv^t; existence of a negative direction implies its remaining eigenvalue is strictly negative and all other eigenvalues are 1. This also proves nonsingularity for every m>=2. The same conclusion holds after division by 2.

Set

    H_m=det[c_(a+b)]_(0<=a,b<m), m>=2.

In this stage H_m is the NORMALIZED determinant. The unnormalized determinant in earlier progress notes equals 2^m H_m. All H_m are negative and nonzero. The degree-one determinant is zero, so a regular scalar orthogonal-polynomial recurrence starting at degree zero would be incorrect.

There is a unique monic p_m orthogonal for rho_0 to degrees below m, for every m>=2. Define

    U_m=H_m p_m.

The bordered moment determinant proves U_m is an integer polynomial, and the Schur determinant identity gives

    rho_0(p_m^2)=H_(m+1)/H_m>0,
    rho_0(U_m^2)=H_m H_(m+1).                         (1)

The initial data are

    H_2=-1, H_3=-6416,
    p_2=y^2-4y-117,
    rho_0(p_2^2)=6416,
    rho_0(yp_2^2)=596592,
    p_3=(y-37287/401)p_2-6416,
    U_2=-y^2+4y+117,
    U_3=(6416y-596592)U_2+41165056.                   (2)

These formulas may be checked directly from c_0=0,c_1=1,c_2=4 and the scalar moment recurrence.

## 3. An integer three-term recurrence with every division recorded

Put A_m=rho_0(yU_m^2), an integer. For every m>=3,

    H_m^2 U_(m+1)
      =(H_m H_(m+1)y-A_m)U_m-H_(m+1)^2 U_(m-1).     (3)

For completeness, the monic recurrence is

    p_(m+1)=(y-a_m)p_m-b_m p_(m-1),
    a_m=rho_0(yp_m^2)/rho_0(p_m^2),
    b_m=H_(m+1)H_(m-1)/H_m^2.

To prove it despite the exceptional degree-one block, subtract the displayed p_(m+1) and p_m terms from yp_m. The remainder has degree at most m-1 and is orthogonal to all degrees at most m-2. That space is one-dimensional, spanned by p_(m-1), because the leading Gram of order m-1 is invertible for m>=3. Pairing with p_(m-1) determines b_m. Clearing denominators yields (3). The separate initial step (2) handles m=2.

Equation (3) is an exact coefficientwise integer division by H_m^2. Rational nonvanishing of H_m is proved, but p-adic unit status is not. No recurrence division is silently treated as unimodular.

## 4. A k-coordinate actual kernel

Form the integer (k-1) by k matrix

    E_(i,j)=L K(y^i U_j),
    0<=i<=k-2, k<=j<=2k-1.                           (4)

Here K(y^r)=-(2r)!-(2r+2)!+4/(2r+1). The greatest denominator index is 2((k-2)+(2k-1))+1=6k-5, so the original L suffices.

The polynomials U_k,...,U_(2k-1) form a rational basis of the k-dimensional upper matching kernel. They are independent by their distinct degrees, and each satisfies rho(Qa)=0 for deg a<k. The leading k by k upper Gram is nonsingular by Section 2, proving that this kernel has dimension k. Consequently E has rank k-1 under the assumed rank of W'.

Take the signed cofactor vector of E, divide it by the positive gcd of all its entries, and call the resulting primitive integer vector t=(t_k,...,t_(2k-1)). Then

    Q=sum_(j=k)^(2k-1) t_j U_j                       (5)

is a nonzero integer polynomial spanning the actual W-kernel. This cofactor gcd division is mandatory. Likewise, replacing the earlier unnormalized column U_j by the normalized column defined in this report divides that column by 2^j and requires recomputing t; retaining the old t would generally give a different polynomial.

## 5. Actual norm and endpoint divisors for primitive normalization

Let g>0 be the gcd of the monomial coefficients of Q. Define

    M(t)=gcd_(k<=j<=2k-1) |H_j H_(j+1)t_j|,
    T_j=U_j(-1),
    E_end(t)=sum_j t_j T_j=Q(-1),
    M_end(t)=gcd(M(t),|E_end(t)|).                    (6)

The gcd convention is gcd(M,0)=M. Since t is nonzero and H_j H_(j+1) is nonzero, M and M_end are positive.

**Actual normalization divisor.** For every k under the stated rank hypotheses,

    g | M_end(t) | M(t),
    M(t) | lcm_(k<=j<=2k-1) |H_j H_(j+1)|.           (7)

Proof: distinct U_j are rho_0-orthogonal, so

    rho_0(QU_j)=H_j H_(j+1)t_j.

The functional rho_0 maps every integer polynomial to an integer. Since every coefficient of Q is divisible by g, every displayed pairing is divisible by g. Also g divides the integer evaluation Q(-1). This proves the first divisibility. At a fixed prime, some t_j is a unit because t is primitive. The valuation of M is therefore at most the largest valuation among H_j H_(j+1), proving the lcm assertion.

These divisors concern the ACTUAL signed moment norms and endpoint. They do not come from a generic Smith identity.

The endpoint values themselves have the scalar recurrence

    H_m^2 T_(m+1)
      =-(H_m H_(m+1)+A_m)T_m-H_(m+1)^2 T_(m-1),
    T_2=112, T_3=-26371840.                          (8)

They also satisfy an exact atom-cancellation identity. Let F_m be the leading m by m determinant of the unscaled positive mu moments, and phi_m its monic orthogonal polynomial. Then

    2^m T_m=F_m phi_m(-1).                           (9)

To prove (9), multiply the m moment rows in the bordered determinant for U_m by 2, then evaluate its final row at -1. Adding (-1)^i times the final row to moment row i cancels precisely the rank-one atom. The result is the bordered determinant for mu. This cancellation is specific to this evaluation; the atom remains in H_m, U_m, E and all matching equations. No claim that E_end(t) is nonzero or a unit is needed.

### Direct integer endpoint moments and their singular primes

Define

    b_r=c_r+c_(r+1)=(D_(2r)+D_(2r+2))/2,
    B_m=det[b_(i+j)]_(0<=i,j<m).

Then the endpoint identity can be written without auxiliary positive orthogonal polynomials:

    T_m=(-1)^m B_m.                                  (9a)

Proof: evaluate the final row of the bordered determinant for U_m at -1. For j=m,m-1,...,1, add column j-1 to column j, in this descending order. The final row becomes (1,0,...,0). Expansion along that row leaves B_m with sign (-1)^m. The alternating atom cancels in c_r+c_(r+1). These are the integer moments of the positive measure (y+1)dmu/2, so B_m>0. This proves each T_m is nonzero but gives no nonvanishing or modular unit assertion for their signed combination E_end(t).

Put a_r=(2r+2)(2r+1) and A_r=a_r+1. Elimination from the actual derangement recurrence gives

    A_r b_(r+1)=a_r A_(r+1)b_r
                   -(8r^3+28r^2+32r+11),
    b_0=1.                                          (9b)

For verification, 2b_r=A_r D_(2r)-(2r+1). Substitution of the derangement recurrence at r and r+1 yields (9b). Its division by A_r is exact over the integers, but its prime factors cannot generally be omitted.

Every prime divisor of A_r is either 3 or congruent to 1 modulo 3. Also v_3(A_r)=1 if 3 divides r, and is zero otherwise. Indeed, A_r is odd and

    4A_r=(4r+3)^2+3.

For p different from 3 dividing A_r, set x=4r+3 and u=(x-1)/2 modulo p. Then u^2+u+1=0 and u is not 1, since u=1 would imply p divides 12. Thus u has multiplicative order 3, proving p=1 modulo 3. Finally, for r=3s,

    A_r=3(12s^2+6s+1),

while A_r=r^2 modulo 3. This proves the stated 3-adic valuation.

Consequently (9b) propagates b_r modulo every p-power without nonunit division whenever p=2 modulo 3. This restricts singular primes of this scalar recurrence, not prime factors of B_m, H_m, or zeta_W.

The normalization divisor in (6) becomes the completely integer moment expression

    M_end(t)=gcd(M(t), |sum_j (-1)^j t_j B_j|).        (9c)

For example, a sufficient actual-moment premise for exact valuation transfer is

    sum_j (-1)^j t_j B_j != 0 modulo p.               (9d)

If p>8k-4, this premise implies g is a p-unit and the Legendre conversion index is a p-unit, hence v_p(zeta_W)=v_p(Lambda) with Lambda as defined below. The implication holds for every such p. The additional condition p=2 modulo 3 merely makes (9b) regular modulo p-powers; it does not establish (9d). The coefficients t must still be those of the fully normalized actual reduced kernel. No uniform proof of (9d) is claimed.

## 6. Explicit Legendre propagation and the valuation bound

Let n=2k. Let B be the n by n integer matrix whose jth column contains the monomial coefficients of ell_j. Its determinant is

    Delta=Delta_(2k)=product_(j<2k) binom(4j,2j).

If u_m is the coefficient vector of U_m padded to length n, define

    w_m=adj(B)u_m in Z^n,
    v=sum_j t_j w_j=adj(B)coeff(Q),
    Lambda=gcd(v_0,...,v_(k-2)),
    G=gcd(v_0,...,v_(2k-1)).                          (10)

The right-block rank hypothesis ensures Lambda>0. The actual primitive Legendre vector is z=v/G, up to overall sign.

There is an exact tridiagonal multiplication rule

    y ell_r=a_r ell_(r+1)+b_r ell_r+c_r ell_(r-1),

where

    a_r=(2r+1)(2r+2)/[4(4r+1)(4r+3)],
    b_r=(2r+1)^2/[(4r+1)(4r+3)]
           +4r^2/[(4r+1)(4r-1)],
    c_r=8r(2r-1)/[(4r+1)(4r-1)].                    (11)

The final term is absent at r=0. Applying the classical Legendre multiplication formula twice proves (11), including the factors from ell_r=4^r P_(2r). Let J be the corresponding coefficient multiplication matrix, J_(s,r)=[ell_s](y ell_r). For 3<=m<=2k-2, (3) becomes

    H_m^2 w_(m+1)
      =(H_m H_(m+1)J-A_m I)w_m-H_(m+1)^2w_(m-1).   (12)

Although J has rational entries, Jw_m is integral in this range: it equals adj(B) applied to the integer coefficient vector of yU_m. There is no truncation loss because deg(yU_m)<2k. Individual denominators in (11) and divisions in (12) remain explicit; no p-adic unit inference is made.

Write Q=gQ_0 with Q_0 primitive in monomial coordinates. Then

    G=g theta_L, theta_L | Delta.                    (13)

Indeed theta_L is the content of adj(B)coeff(Q_0). Multiplication by B shows it divides every coefficient of Delta Q_0. Primitiveness of Q_0 implies theta_L divides Delta. The symbol theta_L is a conversion index here; it is not identified with the inherited theta_W.

Combining the actual divisor (7) with (10)-(13) proves

    zeta_W | Lambda,
    Lambda | Delta_(2k) M_end(t) zeta_W.              (14)

Equivalently, for every prime p,

    max(0,v_p Lambda-v_p Delta_(2k)-v_p M_end(t))
       <=v_p zeta_W<=v_p Lambda.                     (15)

In particular,

    v_p zeta_W=v_p Lambda
      whenever p does not divide Delta_(2k)M_end(t). (16)

Equations (3)-(12) give an explicit actual-moment calculation through k kernel coordinates; (15) bounds its primitive-normalization loss. They do more than restate the gcd of z. Their unresolved input is concrete: control the recurrence-generated Lambda and the actual norm/endpoint quantity M_end(t). A unit statement for the latter is sufficient for exact valuation transfer outside the retained basis primes, but is not proved uniformly. Equations (14)-(16) do not restrict the prime support of zeta_W itself.

## 7. A finite obstruction to unrestricted small-prime support

At k=2 the actual monomial kernel contains

    Q_0=-2015194+8115147y-4687490y^2+79961y^3.

Direct substitution gives rho(Q_0)=rho(yQ_0)=K(Q_0)=0. The exact basis identity is

    924 Q_0=-218267280 ell_0+639779668 ell_1
                 -60435570 ell_2+79961 ell_3.

These four Legendre coefficients have gcd 1. The finite right-block rank is 3. Hence

    zeta_W=218267280=2^4*3^2*5*7*11*31*127.

Thus a claim that zeta_W has prime support at most 8k-4 for EVERY k>=2 is false. This example says nothing decisive about a claim restricted to k>=24. No prime atlas or broad degree scan is used.

## 8. Exact inherited lattice interface remains intact

For the full-rank wide branch, retain the positive Smith pivots e_1|...|e_(k+1), delta_W=product e_i, and the residual (k-2) by (k-1) matrix S_W. The exact content formulas remain

    h'_W=delta_W h(S_W)/zeta_W,
    zeta_W | e_(k+1),
    h_W=delta_W h(S_W)/
          [zeta_W Delta_k Delta_(k-1) theta_W],
    theta_W | Delta_(2k).

The largest-pivot loss is retained. The normalization bound does not make delta_W or h(S_W) units.

The tall factors remain

    h_N=delta_N h(S_N)/[Delta_(2k-1)theta_N],
    theta_N | Delta_k^2.

The actual physical pair still satisfies

    lcm(h_N,h_W) | G_actual | L h_N h_W,
    q=L|B_res|/gcd(A_res,L B_res).

Here A_res,B_res denote the inherited tall residual determinant pair, avoiding collision with the basis matrix B used above. No final-pair gcd estimate follows from this stage. Final short-pair odd content is Child 1's task; cross-polynomial resultant coupling is Main's task.

## 9. Evidence, limits and next interface

The first attempted finite calculation failed with an insufficient moment-table length before producing a receipt. It is not evidence. The corrected saved check_low_projection.py subsequently executed successfully, with exit code 0 and no false flags. Its LOW_PROJECTION_IDENTITY_RECEIPT.json verifies the unnormalized integer recurrence through degree 7, the Legendre multiplication identities through r=6, and actual kernel/normalization reconstruction at exactly k=2 and k=4. It confirms the displayed k=2 primitive vector and factorization. The k=4 projection gcd is 561632400; this is a finite identity check, not a growth or prime-support law.

The supplementary check_normalized_endpoint.py subsequently executed successfully with exit code 0 and no false flags. Its LOW_PROJECTION_NORMALIZED_ENDPOINT_RECEIPT.json verifies the normalized rho_0 columns, recomputed primitive t, scalar endpoint recurrence, atom cancellation, and strengthened divisor (14), with the same two kernel instances k=2 and k=4. At k=4, the measured M/g is 4718592 and M_end/g is 576: the endpoint strictly sharpens this finite normalization bound. At k=2 both ratios are 16. These are bounded identity checks, not asymptotic evidence.

The same successful execution additionally checked (9a)-(9b) directly against the generated moments. LOW_PROJECTION_ENDPOINT_MOMENT_RECEIPT.json records all five flags as true: the endpoint moment identity, initial moment, integrality, scalar recurrence for 0<=r<15, and endpoint Hankel identity for 2<=m<=7. The prime-divisor statement following (9b) is proved algebraically above; no prime scan was performed.

The three receipts and two saved verification scripts are in this report's directory. Their successful execution verifies the stated finite identities only; it is not independent review of the all-degree proofs.

This stage supplies an all-degree normalized recurrence and an actual norm/endpoint divisor for conversion to primitive Legendre coordinates. It leaves open a useful uniform estimate for Lambda or M_end(t), a restricted prime-support law in the large-k range, and a final primitive denominator estimate. Rational regularity and real positivity cannot supply the missing modular unit claims.

The next useful interface is the joint arithmetic of the explicitly normalized reduced matrix E and the scalar sequence T_j: can actual moment recurrences bound gcd(M(t),sum t_j T_j), or prove a unit condition for the low recurrence output at specified primes without computing the full W' Smith form? Any such assertion must recompute t after column rescaling and retain (13)-(16). A generic Smith restatement or positivity-to-modular-rank transfer would not advance this interface.
