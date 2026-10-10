> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A paired-log valuation separation lemma from the exact recurrence

2026-09-13. Auxiliary valued theorem, extending the first-Witt rank calculation to the original characteristic-zero log residues. A uniform version gives sublinear dyadic averages for every fractional depth moment of order strictly between0 and1 on the PNT-side ordinary set. It does not reach the first moment or prove uniform integrability.

## 1. Exact characteristic-zero input

Let q_nu(m)=L_nu(m), the original mixed-cubic logarithmic coordinate. At z=6m the original differentials are

    omega_nu=u^z Q^(-2z/3-1-nu) dx.

Thus the exact polynomial telescoper and contiguity from witt_exterior_recurrence_attempt.md apply with parameter z=6m over Q, before reduction modulo any prime. Taking residues kills the exact derivative identically, without an x^p ambiguity. Write c_k(z), k=0,...,3, for the archived-in-this-session nu=0 coefficients, each of degree17. Then

    sum_(k=0)^3 c_k(6m) q_0(m-k)=0,
    q_1(m)=sum_(k=0)^2 a_k(6m) q_0(m-k).             (1)

These are identities of rational numbers for sufficiently large m, outside the finite rational coefficient singularities; they do not identify the original residues with phase finite parts. Their proof is the exact rational differential identity itself.

Fix an ordinary cell prime p and divide all q values by the same p. On rows in that cell these are p-integral. Set

    S_m=(q_0(m)/p,q_0(m-1)/p,q_0(m-2)/p)^T.

The actual exterior-rank theorem and the full integral bridge show that S_m is primitive modulo p outside the sextic exceptional rows, as long as the three rows remain in the actual cell. Indeed the full three-coordinate row matrix is unimodular, so each coordinate column, including this log column, is primitive.

Let T(z) be the companion of(1), so S_(m-1)=T(6m)S_m. It has last row (-c_0/c_3,-c_1/c_3,-c_2/c_3). Its limiting matrix is

    C=[[0,1,0],[0,0,1],
       [16777216/531441,40370176/19683,26446912/729]].

For a fixed integer gap d>=1 let

    T_d(z)=T(z-6(d-1)) ... T(z-6) T(z).

Then e_1 T_d(6m) S_m=q_0(m-d)/p.

## 2. A nonzero three-row observation for every gap

The paired nu=1 observation supplies the scaled row

    h(z)=(0,z a_1(z),z a_2(z)).

Applied to S_m it equals

    z[q_1(m)/p-a_0(z)q_0(m)/p], z=6m.               (2)

The known exact limits are

    z a_1(z) -> A_1=-165139233219/3610112000<0,
    z a_2(z) -> A_2=291328083/231047168000>0.

Consider

    O_d(z)=rows(e_1,h(z),e_1 T_d(z)).

Its limiting determinant is

    A_1(C^d)_(1,3)-A_2(C^d)_(1,2),                 (3)

which is strictly negative for every d>=1. For d=1,2 this follows from e_1 C=e_2 and e_1 C^2=e_3. For d>=3, the last row of C is strictly positive, and multiplying a strictly positive row by C again gives a strictly positive row; hence e_1 C^d has both indicated entries positive. This proves symbolic nonidentity for every prescribed gap without an unresolved root-of-unity or sign condition.

## 3. An explicit integer observation polynomial

The common denominator of z a_1,z a_2 can be chosen as

    D_H(z)=40960(z-3)(2z-21)(2z-15)(2z-9)(2z-3)(2z+3)S_6(z),

where S_6 is the sextic in witt_actual_exterior_rank.md. It has degree12. Both H_i(z)=D_H(z)z a_i(z), i=1,2, are integer polynomials of degree12.

Let M(z)=c_3(z)T(z), an integer polynomial matrix of degree17. Define

    M_d(z)=M(z-6(d-1)) ... M(z),
    J_d(z)=H_1(z)(e_1 M_d(z))_3-H_2(z)(e_1 M_d(z))_2.

Then J_d is an integer polynomial and

    det O_d(z)=J_d(z)/[D_H(z) product_(h=0)^(d-1)c_3(z-6h)]. (4)

The numerator degree is at most17d+12. Equation(3) proves its leading coefficient is nonzero, since the denominator has exactly that degree and nonzero leading coefficient. Hence

    deg J_d=17d+12.                                     (5)

These definitions specify J_d exactly for every d; they do not fit or interpolate a sequence of determinants.

## 4. The valued conclusion

Assume m and m-d are actual rows of the same fixed (p,j) cell, all rows down to m-d-2 remain in that cell, the three-row state S_m is primitive, and all coefficients used in(1)-(4) have p-unit denominators along this transfer. These are explicit exceptions: for fixed d there are only O(d) forbidden starts modulo p, arising from the fixed-degree coefficient polynomials and the sextic. Exclude also the finite rational singular indices.

Put

    t_m=min(v_p(q_0(m)/p),v_p(q_1(m)/p)),
    t_(m-d)=min(v_p(q_0(m-d)/p),v_p(q_1(m-d)/p)).

If k=min(t_m,t_(m-d)), all three entries of O_d(6m)S_m are divisible by p^k. The second entry has this property by(2), because a_0(6m) is integral at p and6m is a unit on the actual row. Multiplying by the adjugate gives

    det O_d(6m) S_m in p^k Z_p^3.

Since S_m is primitive, this forces

    min(t_m,t_(m-d))<=v_p(det O_d(6m))=v_p(J_d(6m)).   (6)

The equality uses the audited unit denominators. This is an all-level valuation inequality, not only a prohibition of simultaneous first-digit zeros.

For fixed j,d and sufficiently large p, it yields the explicit degree bound

    min(t_m,t_(m-d))<=17d+12.                           (7)

Indeed6m=(3j+1)p+r<(3j+3/2)p. For H_d=||J_d||_1 and D=17d+12,

    |J_d(6m)|<=H_d[(3j+3/2)p]^D.

For p>H_d(3j+3/2)^D this is less than p^(D+1). The nonzero polynomial J_d has no sufficiently large real integer root. Enlarging the fixed threshold therefore makes its value nonzero, so its valuation is at most D. No constant in(7) is claimed uniform in growing j or d; the exact bound(6) is the primary statement.

## 5. Uniformity in the gap and all admissible cells

The following refinement makes the spacing depend on the depth. Let B_M be the maximum row sum of coefficient l1 norms of M, and let B_H=max(1,||H_1||_1,||H_2||_1). These are fixed finite constants. Polynomial translation and matrix multiplication give

    ||J_d||_1<=2 B_H B_M^d (6d+1)^(17d).             (8)

Indeed a translation by6h increases the coefficient norm of a degree17 polynomial by at most(6h+1)^17, and the chosen matrix norm is submultiplicative.

On any PNT-side ordinary row,3j+1<p and r<p/2, so z=6m<2p^2. Also every gap between two rows of the same cell has d<p. Consequently, with D=17d+12,

    log|J_d(6m)|/log p
       <=D[2+log2/log p]+17d[1+log7/log p]
                       +[log(2B_H)+d log B_M]/log p
       <=52d+25                                             (9)

for all sufficiently large p, with an absolute threshold independent of j and d. The last inequality chooses log p larger than both

    17log2+17log7+log B_M,
    12log2+log(2B_H).

There is no unproved nonzero-value assumption in(9). All last-row entries of T(z) are positive for sufficiently large real z, by their strictly positive limiting constants. Also z a_1(z)<0 and z a_2(z)>0 eventually. Throughout an actual same-cell transfer all original arguments z-6h are at least p, hence exceed that fixed real threshold when p is large. The product row e_1 T_d is e_2 for d=1, e_3 for d=2, and strictly positive for d>=3. Thus det O_d(6m)<0 by the same sign proof as(3), uniformly over all these gaps. Its denominator is a nonzero rational number, and J_d(6m) is nonzero.

Combining(6) and(9) proves the uniform separation

    min(t_m,t_(m-d))<=52d+25                            (10)

whenever the indicated transfer is regular.

For each fixed (p,j), remove the row positions where c_3, the denominators of a_0 and h, or the state sextic vanish modulo p, together with the fixed terminal band. Each defining polynomial has fixed degree and nonzero reduction for every sufficiently large p. Thus only an absolute O(1) number of positions are removed. They divide the remaining indices into O(1) consecutive regular intervals. Within such an interval every pair of indices satisfies(10), because the entire transfer path has unit denominators. This formulation avoids losing O(d) fresh positions separately at every depth.

If N_(p,j)(u) counts positions with t_m>=u, then(10) gives, for u>=50,

    N_(p,j)(u)<=C p/u+C                              (11)

with an absolute constant C. On each regular interval, two such positions must be separated by at least(u-25)/52>=u/104; the bounded removed set contributes only the additive constant.

## 6. A stronger common-log support bound by deleting short pairs

This improves the support input for t_m itself without a progression theorem. Let L be the leading matrix of M and let b_i be the leading coefficient of H_i. Take

    A=max(1,|b_1|+|b_2|),
    B=max(2,maximum absolute row sum of L).

The leading coefficient of J_d is

    b_1(e_1 L^d)_3-b_2(e_1 L^d)_2,

which is a nonzero integer by(3), with absolute value at most A B^d. Set D_p=floor(log p/(2log B)). For p>A^2, every d<=D_p satisfies

    0<|lc J_d|<=A sqrt(p)<p.

Thus each J_d remains nonzero modulo p, uniformly over these gaps, and has at most17d+12 roots.

Delete every start in the fixed-(p,j) interval with J_d(6m)=0 modulo p for some1<=d<=D_p, at cost O(D_p^2). Delete also the D_p-neighborhoods of the fixed number of singular and terminal positions, costing O(D_p). If two retained common-log zeros had gap d<=D_p, their entire transfer would be regular and (6) would force J_d(6m)=0, contradicting retention. Thus retained common-log zeros are separated by more than D_p, so their count is at most N/D_p+1. Adding back the deleted positions proves, uniformly in admissible j,

    N_(p,j)(1)<=C p/log p.                            (15)

No sign claim about finite-field values is used. Summing over the PNT-side cells, where p is between sqrt(6X) and12X and occurs in O(X/p) relevant j-cells, gives by Chebyshev

    sum_(X<=m<2X) sum_(PNT-side p:t_(m,p)>=1) log p
                                      =O(X^2/log X).  (16)

This is a common-log radical bound, not a multiplicity sum or a bound on the extra-one first-Witt component.

## 7. Every fractional depth moment below one has zero dyadic average

Fix a real exponent theta with0<theta<1. The independently established uniform first-Witt support bound is

    #{m in the fixed (p,j) cell: d_(m,p)>=1}<=p epsilon(p),
    epsilon(p)=C exp[-c(log log p)^(1/9)] ->0.

For t_m we use the stronger bound(15). In addition, the exact Cauchy coefficient estimate for C_nu(m) gives log|C_nu(m)|<=C_0m whenever that coefficient is nonzero, with an absolute C_0. One may use the contour radius1/2 directly. The verified eventual nonvanishing of B_m ensures that the two C coefficients cannot both vanish for sufficiently large m. Therefore, for X<=m<2X,

    t_m<=C_1 X/log p=:T.                              (12)

From (11), the support bound(15), and the layer-integral identity for the finite sum of t_m^theta,

    sum_m t_m^theta
       =theta integral_0^T u^(theta-1) N_(p,j)(u) du,

one obtains

    sum_m t_m^theta
       <=C_theta p/(log p)^(1-theta)+C_theta T^theta. (13)

For completeness, absorb the bounded exceptional count as C T^theta and bound the remaining count by min(Cp/log p,Cp/u). Split its integral at a constant multiple of log p. The lower part is O(p/(log p)^(1-theta)); the upper integral converges because theta-2<-1, and has the same order. Values u<50 are absorbed in the first term. If the splitting point exceeds T, the same estimate remains valid by extending the integral upper limit. Constants depend on theta and blow up as theta tends to1.

The exact valued theorem d=t+epsilon_m, epsilon_m in {0,1}, and concavity give

    d^theta<=t^theta+1_(d>=1).

Thus with d in place of t the bound is

    sum_m d_(m,p)^theta
       <=C_theta p/(log p)^(1-theta)+C_theta T^theta
                                             +p epsilon(p). (17)

The last, slower term is needed: t=0,d=1 is an actual possibility and is not counted by(15).

Now sum over ordinary PNT-side cells in the dyadic m range. Their primes satisfy sqrt(6X)<p<12X, and at each p the number of relevant j is O(X/p). The main term of(13), after multiplication by log p, sums to

    O_theta[X sum_(sqrt(6X)<p<12X) (log p)^theta]
                =O_theta[X^2/(log X)^(1-theta)]=o(X^2)

by Chebyshev's prime-count bound, since log p is comparable to log X. The extra p epsilon(p) term for d contributes o(X^2) by the first-Witt support theorem. The exceptional term is

    O_theta[X^(1+theta) sum_p (log p)^(1-theta)/p]
       =O_theta[X^(1+theta)(log X)^(1-theta)]
       =o(X^2).

The middle estimate follows from Chebyshev by partial summation; throughout this prime range log p is comparable to log X. We conclude the new fractional-moment theorem

    sum_(X<=m<2X) sum_(PNT-side ordinary p)
                    d_(m,p)^theta log p=o(X^2),
                       for every fixed0<theta<1.         (14)

The same holds with t in place of d. This is stronger than radical support sparsity, but it deliberately excludes the first-moment endpoint.

## 8. A growing clipped first moment and the remaining endpoint

Let K_X>=1 be any real sequence with K_X=o(log X). Equation(15) immediately gives

    sum_(X<=m<2X) sum_(PNT-side ordinary p)
                           min(t_(m,p),K_X)log p
                    =O(K_X X^2/log X)=o(X^2).         (18)

Since d=t+epsilon_m with epsilon_m in {0,1},

    min(d,K_X)<=min(t,K_X)+1_(d>=1).

The first-Witt support theorem proves(18) with d in place of t. This is a growing clipping level, rather than only a theorem for each fixed finite union of layers.

It extends to the entire Item427 range p^2>4m+1. On the non-PNT complement p=O(sqrt(m)); Chebyshev bounds its radical logarithm by O(sqrt(m)). Clipping therefore bounds its dyadic contribution by O(K_X X^(3/2))=o(X^2), without any unbounded multiplicity assumption.

What remains missing is the untruncated first moment.

This rules out two arbitrarily deep paired-log zeros at any prescribed regular gap. It is more information than the local two-row kernel in Item200, because it compares two different construction indices and uses the primitive three-shift state.

It still does not give a summable uniform tail for the singleton depths t_m. A lone extremely deep value is consistent with(6), provided nearby values have smaller depth. The now-proved linear separation gives the weak tail O(p/u), whose first-moment layer integral is logarithmic rather than convergent. At theta=1, both the integral used in(13) and the exceptional estimate lose the needed saving. Thus taking theta arbitrarily close to1 is not a proof of the first-moment theorem; its constants and error depend on theta. The full normalized gcd valuation mass remains the exact open target stated in witt_depth_lift_attempt.md. The PNT-complement depth mass is also outside(14).

An explicit information-class model shows the endpoint issue is real for these bounds. On an interval of length floor(p/12), put t=ceil(log p) at every ceil(log p)-th index and t=0 elsewhere. Its support is O(p/log p), its positive values satisfy the linear separation(10), its fractional theta-moment is of order p/(log p)^(1-theta), and every clipping level o(log p) has sublinear total. Its untruncated first moment is nevertheless of order p. The height upper bound(12) also permits it for fixed cells at large p. This is not asserted to be an actual residue sequence; it proves only that the estimates established here do not logically force the first-moment conclusion without new arithmetic information.

The companion check_paired_log_separation.py and paired_log_separation_checks.json verify the integer degree17 companion coefficients, the exact degree12 common denominator and numerator integrality, the signed limiting rows, the coefficient norms used in(8), and exact observation leading coefficients for gaps1,2,3. Every-gap nonvanishing and the moment estimate are proved in the text, rather than inferred from those finite symbolic checks.
