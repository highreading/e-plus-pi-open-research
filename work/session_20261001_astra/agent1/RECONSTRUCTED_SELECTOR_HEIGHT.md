> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Primitive reconstructed selectors: heights and endpoint corrections

New author deductions, 2026-10-01. The direct-selector budget is taken from DIRECT_SELECTOR_HEIGHT_OBSTRUCTION_DRAFT.md as an author input, without audit. Earlier scalar gcd results and Toeplitz local arithmetic remain unchanged. No numerical controls, scans, or independent review are performed here.

## 1. Domain and exact reconstruction

The algebra below holds for integers 1<=b<=n whenever the actual rational Toeplitz matrix T is nonsingular. It does not require quantitative inverse estimates. Indices of T are 0<=i,k<b; reconstructed B coordinates have indices 0<=j<=b. Put

 T_ik=[z^(n+i-k)] exp(z)Q0(z)^n,
 Q0(z)=1-z+z^2/2.

Let R be the matrix of (D+1)^(-n) on ascending polynomial coefficients of degree less than b:

 R_(k,k+l)=(-1)^l binom(n+l-1,l)(k+l)!/k!,
 0<=l<=b-1-k.

All its entries are integers. Its inverse, the matrix of (D+1)^n, is also integral and upper unitriangular. Let D_B multiply a polynomial by z-1, and define

 K=Krec=D_B R.

Thus K is an integer (b+1)-by-b matrix. Its image is exactly the saturated lattice of integer coefficient vectors whose sum is zero. Indeed division by z-1 on that lattice and R^(-1) are integral. In particular K has an integral left inverse, and gcd(Ky)=gcd(y) for every integer vector y. Each individual row k_j of K is primitive: its first nonzero entry is -1 for j=0 and +1 in column j-1 for 1<=j<=b.

The exact retained reconstruction is

 u=K T^(-1) fP,
 v=e0+K T^(-1) fQ.

These formulas concern the actual balanced relaxed B lift. No weighted degree update is substituted.

For the factorial Gram application assume additionally b>=3 and choose an integer 1<=m<=floor((b-1)/2). Set ell=n+m+1,

 omega_j=(ell)_j, omega_0=1,
 tau=(ell-b)!/ell!,
 W=tau^2 Omega, Omega=diag(omega_j^2), 0<=j<=b.

These are precisely the retained B-only factorial weights. Formulas below also hold for any positive integral diagonal Omega, with corresponding adjustments to weight bounds. They are not statements about a full A/B/C Gram.

## 2. Fraction-free data with the uniform factorial removed

Use the proved integral row normalization from TOEPLITZ_LOCAL_ARITHMETIC:

 c0=2^n n!, d_i=(n+i)!/n!, D0=diag(d_i),
 M=c0 D0 T in Mat_b(Z), Delta=det M!=0.

Define

 J_i=2^n fP_i/n!
     =2^n [z^(n+i)]Q0(z)^n/(1-z)^(n+1) in Z,
 V=D0 J,
 C=K adj(M) D0 in Mat_(b+1,b)(Z),
 x=CJ=K adj(M)V.

The symbol C in this note is an integer matrix, not the logarithmic coefficient polynomial. The vector J is the positive integral forcing vector; in particular J_0=P_n>0. The earlier local note calls J_i its H_i.

Exactly,

 K T^(-1)=(c0/Delta) C,
 u=((n!)^2/Delta)x.                                      (1)

The latter follows from fP=(n!/2^n)J. The factor (n!)^2 belongs to the endpoint lift. It is NOT automatically a factor in primitive selector height.

All rows of C are nonzero, since the rows of K are nonzero and adj(M)D0 is invertible. Also x!=0, since fP!=0 and K is injective.

## 3. Coordinate selectors: exact heights and corrections

For row j let

 g_j=gcd_i |C_ji|>0,
 lambda^(j)_i=C_ji/g_j.

Fixing the sign of the first nonzero coefficient would make this canonical up to a unique sign; none of H,A,r depends on that sign choice. This is exactly the primitive integral representative of the rational row e_j^T K T^(-1), since its other factor c0/Delta is common to every coefficient.

The actual l1 selector height and forcing normalization are

 H_j=sum_i |C_ji|/g_j,
 U_j=2^n sum_i lambda^(j)_i fP_i/n!=x_j/g_j,
 A_j=|x_j|/g_j.                                         (2)

The coordinate center is defined precisely when x_j!=0, equivalently u_j!=0; assume this in every formula containing A_j or its logarithm. Since g_j divides x_j, A_j is a positive integer.

The exact center decomposition is

 v_j/u_j=r_j+(lambda^(j) dot fQ)/(lambda^(j) dot fP),
 r_j=delta_(j,0) Delta/((n!)^2 x_j).                     (3)

For j>0, r_j=0 and den(r_j)=1. For j=0 the positive reduced correction denominator is EXACTLY

 v_r,0=(n!)^2 |x_0|/gcd((n!)^2 |x_0|,|Delta|).           (4)

This is the correction denominator, not the denominator of the complete center. Child 4's eligible-coordinate reduction remains a separate problem.

For j=0 there is the unconditional divisor

 (n!)^2/gcd((n!)^2,|Delta|) divides v_r,0.                (5)

This follows prime by prime: adding v_p(x_0)>=0 to the denominator valuation cannot decrease its reduced denominator. It identifies an actual possible factorial contribution to the budget, subject to cancellation with Delta. It does not assert Delta is coprime to n!.

The exact coordinate budget is consequently

 log H_j+log A_j+2log den(r_j)
 =log(sum_i |C_ji|)+log|x_j|-2log g_j+2log den(r_j).      (6)

For j>0 it has no correction term. Multiplying the original rational row by any nonzero rational changes neither (2) nor (6).

## 4. Gram selector: exact heights and correction

Put

 D=x^T Omega x>0,
 z=C^T Omega x in Z^b,
 gamma=gcd_i |z_i|.

The vector z is nonzero because z^T J=D>0. The rational Gram selector in the question has exactly the scale

 T^(-T) K^T W u
   =[c0 (n!)^2 tau^2/Delta^2] z.                       (7)

Remove this common rational factor and the coefficient gcd gamma. The primitive integral selector is lambda_G=z/gamma, with

 H_G=(sum_i |z_i|)/gamma,
 U_G=2^n lambda_G dot fP/n!=D/gamma,
 A_G=D/gamma>0.                                        (8)

In particular gamma divides D; it cannot be omitted from the forcing normalization. The actual Gram center satisfies

 (u^T W v)/(u^T W u)
   =r_G+(lambda_G dot fQ)/(lambda_G dot fP),
 r_G=Delta (x^T Omega e0)/[(n!)^2 D].                   (9)

For the specified factorial weights omega_0=1, so x^T Omega e0=x_0. Thus

 v_r,G=(n!)^2 D/gcd((n!)^2 D,|Delta x_0|).              (10)

The convention gcd(a,0)=a makes v_r,G=1 when x_0=0. That case must not be assigned a nontrivial correction denominator. In general,

 (n!)^2/gcd((n!)^2,|Delta x_0|) divides v_r,G.           (11)

The exact Gram budget is

 log H_G+log A_G+2log v_r,G
 =log(sum_i |z_i|)+log D-2log gamma+2log v_r,G.          (12)

Both the common weight factor tau^2 and the common forcing-lift factorial in (7) cancel from the primitive selector. Neither supplies a height gain or loss by itself.

A further useful exact content separation is available. Put y=adj(M)V and rho=gcd(y)=gcd(x)>0, the equality following from saturation of K. Write x=rho x*, and z*=C^T Omega x*. Then

 z=rho z*, gamma=rho gamma*, gamma*=gcd(z*),
 D=rho^2 D*, D*=x*^T Omega x*,
 H_G=||z*||_1/gamma*, A_G=rho D*/gamma*,
 r_G=Delta x*_0/[(n!)^2 rho D*].                       (13)

These identities do not assume gamma* and rho are coprime. They distinguish content of the actual forcing response from content of its adjoint selector.

## 5. Divisibility restrictions on the selector gcds

Let dmax=d_(b-1). Every d_i divides dmax, including b=1 with dmax=1. From the definition of C,

 C D0^(-1) M=Delta K.

Therefore for each row,

 g_j divides dmax Delta.                              (14)

Proof: multiply the identity by dmax. Its left side has all entries divisible by g_j; its right side is dmax Delta times the primitive row k_j. Bezout on that row proves (14). This result removes any unsupported generic-coprimality assumption and confines possible coordinate-selector content to an explicit integer.

For the Gram selector define the positive definite integral b-by-b reconstruction Gram

 G_K=K^T Omega K.

The identities

 M^T D0^(-1) z=Delta K^T Omega x=Delta G_K y

give

 gamma divides dmax Delta gcd(G_K y).

Since y/rho is primitive, adj(G_K) applied to G_K y and Bezout imply

 gcd(G_K y) divides rho det(G_K).

Consequently

 gamma divides dmax Delta rho det(G_K).               (15)

This does not multiply independent overlapping divisors: each statement follows sequentially from an integer matrix identity. It does not claim equality.

Equations (14)-(15) yield the rigorous lower bounds

 H_j>=max(1,||C_j||_1/(dmax |Delta|)),
 H_G>=max(1,||z||_1/(dmax |Delta| rho det(G_K))).        (16)

For the factorial weights, the extra det(G_K) has no inevitable n log n scale when b is logarithmic. Indeed ||K||_2<=2(n+b)^(b-1) by the finite differential expansion and multiplication by z-1, while omega_j<=ell^b. Hence

 det(G_K)<= [4(n+b)^(2b-2) ell^(2b)]^b,
 log det(G_K)=O(b^2 log(n+b)),
 log dmax<= (b-1)log(n+b).                             (17)

For b=O(log n), both are o(n log n). The possible large remaining factors in (14)-(15) are the actual determinant Delta and, for Gram selection, the response content rho. No conclusion that they cancel is inferred from their allowed support.

## 6. Explicit all-size height ceilings

These bounds are ceilings, not estimates for reduced heights from entrywise clearers. The exact coefficient gcd remains in every formula.

Write R0=sqrt(2), M0=1+sqrt(2), and c_i=2^n(n+i)!. Cauchy's inequality on |z|=R0 gives

 |T_ik|<=exp(R0) M0^n R0^(k-i).

For b>=2, scaling a (b-1)-by-(b-1) cofactor and applying Hadamard gives

 max_(i,k)|adj(M)_ik|<=B,
 B=(b-1)^((b-1)/2) exp(R0(b-1)) M0^(n(b-1))
       *R0^(b-1) * product_(i=1)^(b-1)c_i.             (18)

The row/column geometric factor for any deleted row and column is at most R0^(b-1). The product of retained c_i is at most the displayed product because c_i increases. For b=1 set B=1, using the empty cofactor convention.

Let

 Kmax=2(n+b)^(b-1), OmegaMax=ell^(2b),
 Cmax=b Kmax B dmax,
 Jmax=2^(n+b) M0^n/sqrt(n),
 Xmax=b Cmax Jmax.

Here Jmax follows from the direct-selector positive forcing bound with i<=b-1; that bound is an author input from the budget draft. Then

 |C_ji|<=Cmax, |x_j|<=Xmax,
 H_j<=b Cmax/g_j,
 A_j<=b Cmax Jmax/g_j,
 H_G<=[b(b+1) Cmax OmegaMax Xmax]/gamma,
 A_G<=[(b+1) OmegaMax Xmax^2]/gamma.                  (19)

Alternatively, for either primitive selector the sharper universal forcing comparison is

 1<=A<=Jmax H.                                       (20)

No sign assumption is needed; it follows by taking absolute values after primitive normalization. Thus log A<=log H+O(n+b), and for b=O(log n) the two may have the same leading n log n ceiling, but no lower equality is established.

For orientation, (18) yields

 log Cmax <=(b-1)log(n!)+O(nb+b^2 log(n+b)).            (21)

At b of order log n this unnormalized ceiling is of order n(log n)^2. It is much too coarse to decide the n log n budget. Equation (19) is not a claim that primitive height attains this ceiling. Deciding the budget requires the gcd subtractions in (6) or (12) and, where applicable, the reduced correction denominator.

The b=1 boundary demonstrates that factorial height is not forced just by the reconstruction mechanism. Here K=(-1,1)^T, adj(M)=1, D0=1, C=(-1,1)^T, and J=P_n. Both coordinate selectors have H=1 and A=P_n. For any positive integral diagonal Omega, the Gram selector also has H=1 and A=P_n, after its one coefficient is made primitive. This is a structural boundary observation, not a renewed scalar small-denominator search; the scalar obstruction remains retained.

## 7. Local transfer after reconstruction and primitive normalization

Only here impose the exact domain of the retained local theorem:

 p odd, p>2b+3, p>=3b,
 n=ap+r, b<=r<=floor((p-b)/2).

The extra p>=3b remains necessary for nonemptiness of this chosen window. No dyadic or ternary extension of it is made.

The retained input is

 M(n)=2^a M(r), V(n)=2^a h_a V(r) mod p,
 J(n)=2^a h_a J(r) mod p,
 h_a=[w^a]Q0(w)^a/(1-w)^(a+1).

All d_i are p-units in the interior window and D0(n)=D0(r) mod p. The explicit reconstruction formula also gives K(n)=K(r) mod p: every derivative order l<b<p, so l! is invertible and binom(n+l-1,l) is a polynomial in n modulo p. This proof covers n crossing blocks without dividing by a multiple of p.

Thus the NEW reconstructed transfers are

 C(n)=2^(a(b-1)) C(r),
 x(n)=2^(ab) h_a x(r),
 Delta(n)=2^(ab) Delta(r) mod p.                      (22)

For the factorial Gram weights hold the same integer m fixed at n and r. Then Omega(n)=Omega(r) mod p. The inequalities on r ensure ell(r)=r+m+1<p and ell(r)>b, so every omega_j is a p-unit. Nevertheless det(G_K) or its quadratic contractions may vanish modulo p.

With that convention,

 z(n)=2^(a(2b-1)) h_a z(r),
 D(n)=2^(2ab) h_a^2 D(r) mod p.                       (23)

In (23), z(r),D(r) are formed using the same m and the seed construction. Positive definiteness over R does NOT ensure D(r)!=0 modulo p.

The prime-by-prime exact normalization is

 v_p(g_j)=min_i v_p(C_ji),
 v_p(A_j)=v_p(x_j)-v_p(g_j),
 v_p(gamma)=min_i v_p(z_i),
 v_p(A_G)=v_p(D)-v_p(gamma).                          (24)

These formulas require the corresponding nonzero forcing and selector domains already specified. They do not follow by reducing a rational selector whose denominator is nonunit.

For example, if some C_ji(r) is nonzero modulo p, (22) proves v_p(g_j)=0. If additionally h_a x_j(r)!=0, it proves v_p(A_j)=0. No assertion is made that these tests always succeed.

If Delta(r)!=0, all coordinate rows C_j(r) are nonzero modulo p: K has primitive rows modulo p, and adj(M),D0 are then invertible. Thus this sufficient condition makes every coordinate-selector gcd a p-unit. When also h_a x_0(r)!=0, coordinate zero has the exact correction law

 v_p(v_r,0)=2v_p(n!).                                (25)

For Gram selection, if Delta(r), h_a, and D(r) are all nonzero modulo p, then D(n) and gamma(n) are units, so A_G is a unit. If also x_0(r)!=0, the same exact correction law holds:

 v_p(v_r,G)=2v_p(n!).                                (26)

If x_0(r)=0, (26) is not asserted. More generally the exact local correction depths are

 v_p(v_r,0)=max(0,2v_p(n!)+v_p(x_0)-v_p(Delta)),
 v_p(v_r,G)=max(0,2v_p(n!)+v_p(D)-v_p(Delta)-v_p(x_0)), (27)

where the Gram expression is zero when x_0=0. Fixed-prime factorial valuations have only O(n) logarithmic weight. These conditional gates alone therefore do not settle an n log n height budget; one would need control over growing sets of primes or direct global contents.

When h_a or all relevant residual coefficients vanish, stop the unit argument. The needed lifts are the complete integer vectors C_j or z, their contractions x_j or D, and Delta at sufficient prime-power precision. For Gram selection, the response content rho must also be retained. A first-order zero does not give its valuation. The logarithmic second forcing has not been used to claim any final center denominator; it remains part of that separate reduction.

## 8. Budget conclusion and precise unresolved arithmetic

The degree of each primitive selector is at most b-1. Under b=O(log n), the draft's necessary condition for log den(center)=O(n) is

 liminf [log H+log A+2log den(r)]/(n log n)>=1,

subject to its stated finite-growth hypotheses. This is an author budget dependency, not newly audited here.

For reconstructed coordinate j>0 the quantity is EXACTLY the right side of (6) without a correction term. Its factorial-scale content is not the common (n!)^2 in the lift: that disappears from the primitive selector. The unresolved quantity is the actual row content g_j against ||C_j||_1 and |x_j|. Equations (14), (19), and (22) constrain it but do not determine its leading rate.

For coordinate zero, (4)-(5) show where a factorial-scale correction denominator can remain. Its cancellation is governed by Delta, not the primitive selector gcd alone.

For Gram selection, (12)-(15) separate the adjoint coefficient gcd gamma, forcing-response content rho, reconstruction-Gram determinant, and correction denominator. The small bound (17) rules out attributing an independent n log n gain to the factorial weights' common scalar or to det(G_K) at logarithmic b. It does not control Delta or rho, and does not prove either a small or a large total budget.

STOP any proposed improvement obtained solely by multiplying the entire selector by an integer, by retaining c0/Delta as selector height, by retaining the scalar in (7), or by retaining tau^2. Primitive normalization cancels each of these exactly. This stopping rule does not exclude the actual reconstructed centers.

The output is an all-size exact factorization and arithmetic interface, not an asymptotic resolution of the budget. No generic coprimality, eligible-coordinate reduced denominator theorem, shrinking claim, or conclusion about e+pi is asserted. Only the two new files are written; completed scalar and local-transfer work is preserved.
