> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Shifted paired recurrence compression and the actual gcd

Author theorem, 2026-10-02. The fresh archive/primary-paper gate is in `SHIFTED_RECURRENCE_COMPRESSION_PROGRESS.md`. The scalar multi-step recurrence is classical and credited there to Miska's Section4.3. The results below concern its exact substitution into the full shifted paired coefficient pair. Root owns the M23 positive complete error and M24's distinct shorter right-family wedge; neither is rederived here.

## 1. Three exact scalar states

Fix k>=2 and n=2k−1. Let M be even, X=2M, d=D_X, f=X!, and l=beta_M+f (the rational arctangent remainder). Set

    P_j(X)=product_(a=1)^j(X+a),
    Q_0=0, Q_(j+1)=(X+j+1)Q_j+(−1)^(j+1),
    h_r(X)=4 sum_(a=0)^(r−1)(−1)^(r−1−a)/(X+2a+1).

The empty h_0 is0. Direct iteration proves

    D_(X+j)=P_j d+Q_j, (X+j)!=P_j f,
    beta_(M+r)=−P_(2r)f+(−1)^r l+h_r.           (1)

This retains the entire exponential constant, rational arctangent endpoint mass and its fixed tail. All r required here lie between0 and2n−1. The tail denominators therefore divide the integer polynomial

    delta(X)=product_(a=0)^(2n−2)(X+2a+1).      (2)

Its degree is2n−1. The denominator of l is its actual reduced odd denominator, not an assumed equality with an odd lcm.

## 2. Cofactor vector and primitive normalization

In the polynomial ring Z[X,d], form the n by(n+1) matrix

    C_ij=P_(2(i+j))(X)d+Q_(2(i+j))(X)−(−1)^(i+j),
          i0,...,n−1, j0,...,n.

Let V_j be its signed maximal minor, with sign(−1)^(n+j). Then V=(V_0,...,V_n) is an integer polynomial vector of d-degree at most n and satisfies C V=0 identically. At every admissible specialization where C has full row rank, it represents the same orthogonal polynomial as root M23. Its primitive polynomial is V/g, where g is the gcd of all specialized coefficients, with sign chosen if desired.

Using V in the ENTIRE weighted matrix multiplies that matrix by g relative to the primitive polynomial. Both determinant coefficients are multiplied by g^k. Consequently g^k cancels in the final primitive pair. The formulas below may use V without guessing g, while preserving the exact primitive-center denominator. A small g is not claimed to be an independent denominator improvement.

Write

    V_minus=sum_j(−1)^j V_j,
    Gamma_s=sum_j V_j P_(2(s+j)),
    Z_s=sum_j V_j Q_(2(s+j))−(−1)^s V_minus.

The exact cofactor constraints give

    d Gamma_s+Z_s=0             (0<=s<n).       (3)

Although each V_j has d-degree at most n, equation(3) forces

    deg_d Gamma_s<=n−1.                        (4)

This is a POLYNOMIAL identity: the highest d-degree contraction vanishes. It introduces no numerical division by d, and it remains meaningful at a zero specialization of d.

Define the rational sequence

    R0_s=−f Gamma_s+sum_j V_j h_(s+j),
    R_s=R0_s+l(−1)^s V_minus.                 (5)

Then R is the exact full rational matrix part, and

    H=R0+(S+l)V_minus uu^T,
    u_i=(−1)^i, i0,...,k−1.                   (6)

## 3. The old mass denominator occurs only once

Let T0=delta R0 be the k-square integer polynomial matrix. Define

    a0=det T0,
    j0=u^T adj(T0)u,
    b0=delta V_minus j0.                      (7)

Then the COMPLETE coefficient pair from V is

    A=(a0+l b0)/delta^k,
    B=b0/delta^k.                             (8)

Thus B is independent of the old arctangent mass l, and A is affine in l. These are exact polynomial determinant identities, including singular T0; no Schur quotient or determinant inverse is used.

Write l=p/a in lowest terms, a>0. If b0!=0, the actual center and its ACTUAL reduced denominator are

    c=−(a a0+p b0)/(a b0),
    q_actual=|a b0|/gcd(a a0+p b0,a b0).       (9)

Equation(9) retains the complete evaluated content. It is valid whether V is primitive or not: dividing V by g divides both a0 and b0 by g^k, which cancels exactly from the quotient.

The denominator a therefore appears only once in an explicit integer pair. Clearing each row separately by a delta would have inserted a^k; that extra factor a^(k−1) is removable by the rank-one response identity before any empirical gcd conjecture. This is an honest clearing-cost reduction. It does not claim that the remaining actual q attains its upper bound.

For an exact prime-by-prime description, first reduce a0/b0=r/s, s>0. Then c=−p/a−r/s. At any prime ell with alpha=v_ell(a), beta=v_ell(s),

- if alpha!=beta, the actual denominator depth is max(alpha,beta);
- if alpha=beta=t>0, it is max(0,t−v_ell(p(s/ell^t)+r(a/ell^t)));
- if alpha=beta=0, it is0.

This includes every tied-denominator cancellation and makes no unsupported inference from a raw factorial clearer. In particular q_actual divides lcm(a,s).

## 4. Exact factorial-degree cancellation

Give f and d degree1, while X,l and the tail coefficients have degree0. Equation(4) and(5) imply

    total_(f,d) degree R0_s <= n.

Consequently

    total_(f,d) degree a0 <= nk,
    total_(f,d) degree b0 <= nk.               (10)

Without using the exact orthogonality, the separate bound V_j degree n and the factorial multiplier f would have yielded k(n+1). The cofactor identity removes one whole large-state degree per matrix row, a formal factor-f^k cost at d comparable to f. It is a structural ceiling improvement; it is not an assertion of a multiplicative improvement between two already reduced denominators.

For each fixed k, all remaining coefficient functions have fixed polynomial height in X after delta clearing. Since D_X=Theta(X!), equations(9),(10) imply

    log q_actual <= nk log(X!)+O_k(M+log(M+2)). (11)

Indeed |b0|<=C_k (X+1)^c_k (f+d+1)^(nk); the actual l denominator divides the odd lcm through X−1. The classical Chebyshev lcm bound gives log a=O(M). No equality for a or assumption about the final gcd is used.

## 5. Uniform specialization content at k2

A meaningful SYMBOLIC computation was performed once at n3 (k2), to test whether primitive cofactor normalization itself could hide a factorial-sized factor. It uses indeterminates X,d, not a degree/prime scan or a finite-M pattern. The exact signed minors have generic polynomial gcd2. Set Z_j=V_j/2.

The two extreme cofactors are coprime in Q(X)[d]. Their exact Sylvester resultant is

    R(X)=−1024 (X+1)^6 (X+2)^6 (X+3)^2 (X+4)^2 P10(X) P27(X), (12)

where the fully expanded positive-coefficient polynomials P10,P27 are retained in `SHIFTED_COMPRESSION_SYMBOLIC_RECEIPT.json`. R has degree53 and no nonnegative real zero. The Sylvester adjugate identity supplies integer polynomial A(X,d),B(X,d) with

    A Z_0+B Z_3=R(X).

Therefore, for EVERY integer X>=0 and integer d,

    gcd_j Z_j(X,d) divides R(X).               (13)

In particular the numerical gcd after d=D_X substitution is O((X+1)^53), uniformly. There is no new factorial-sized primitive cofactor content at k2. This is an infinite-parameter result obtained from a symbolic identity; it is not inferred from numerical M examples. No analogous coprimality for every n is claimed.

The leading d³ coefficient of sum_j(−1)^j Z_j is a nonzero negative polynomial with all coefficients of the same sign, recorded in the receipt. Thus, for d=D_X and X=2M tending to infinity,

    log|q_(3,M)(−1)|=3 log(X!)+O(log M),        (14)

after the exact primitive coefficient normalization. The same leading-state estimate applies to the polynomial coefficient height. Resultant(13) cannot replace the final determinant gcd in(9).

## 6. What the complete error requires of final content

Root's authored M23 positive fixed-k theorem supplies the COMPLETE error

    S−c ~ (e+2)((k−1)!)²/[2^(2k−1) M^(2k−1)].

At k2, its normalized response coefficient has the exact positive integral

    B/q_(3,M)(−1)^2 = integral_0^1 x^(2M)(1+x²)^2
                         [q_(3,M)(x²)/q_(3,M)(−1)]
                         [e^x+4/(1+x²)] dx
                    ~ 2(e+2)/M.

This is the response-reduced2-by2 formula, and all endpoints are retained. Combining it with(14) gives

    log|B|=6 log(X!)+O(log M).                 (15)

For the least positive common denominator C of the PRIMITIVE-polynomial coefficient pair A,B, log C=O(M); hence

    log(C|B|)=6 log(X!)+O(M).

If the full primitive form q_actual(S−c) is to tend to0, then with G=gcd(CA,CB) it is necessary and sufficient that

    C|B|/(G M³) -> 0.                         (16)

Thus the needed final content would be factorial-sized: its logarithm must approach6 log(X!) up to O(M+log M) costs. The polynomial cofactor content(13) does not establish that final cancellation. Conversely(13) does not rule it out, because the remaining output gcd depends on the complete evaluated exponential/arctangent coefficient pair.

## 7. Scope

The compression, degree cancellation, single old-mass denominator, full tied-prime formula and actual final-q identity hold at every fixed k and admissible even M. The explicit polynomial specialization-content bound is proved uniformly at k2 only. The general cofactor resultant/coprimality problem and the final output gcd rate remain open. No shrinking primitive form, global denominator lower bound, or irrationality claim follows from these upper bounds or the fixed-k complete-error theorem.

## 8. A uniform tail-denominator factor in BOTH output entries

There is a further exact all-k clearing reduction. Define

    T_k(X)=product_(a=3k−2)^(4k−4)
                    (X+2a+1)^(a−3k+3).          (17)

Its degree is k(k−1)/2. Then, as integer polynomial identities,

    T_k divides a0 and T_k divides b0.           (18)

Proof: fix a in the stated range and ell_a=X+2a+1. Let e=a−3k+3, so1<=e<=k−1. In row i<e of R0, every h_(i+j+t) has index

    i+j+t <= (e−1)+(k−1)+n < a+1.

Hence the denominator ell_a is absent from that entire row. Multiplication by delta forces every entry of row i<e in T0 to contain ell_a as a polynomial factor. The determinant a0 contains ell_a^e. Every(k−1)-minor of T0 loses at most one of these e rows, so it contains ell_a^(e−1). The extra delta factor in b0 supplies one more ell_a. Thus ell_a^e divides both entries. Distinct primitive linear polynomials are coprime in the polynomial UFD, so their product(17) divides both, proving(18).

At the actual X=2M this is an integer divisor of the COMPLETE pair in(9). It may be removed before the final numerical gcd, giving the rigorous ceiling

    q_actual <= a |b0|/T_k(X).                  (19)

This uses the raw cofactor vector and its full shared content; any primitive-polynomial normalization is still canceled exactly in(9). There is no multiplication of two possibly overlapping specialization-content gains. The logarithmic reduction at fixed k is[k(k−1)/2]log X+O_k(1). It does not change the leading factorial degree in(11).

At k2, T_k=X+9. The single symbolic pair computation gives the stronger COMPLETE generic polynomial gcd

    gcd_Z[X,d,f](a0,b0)=16(X+9)

when using the cofactors Z=V/2 from Section5. In particular no common polynomial in d or f remains after that exact factor is removed. The receipt `SHIFTED_COMPRESSION_PAIR_RECEIPT.json` retains the symbolic degree checks and generic gcd; one existing M8 root receipt was used solely to check the entire actual-q normalization. The exact formula matched the root's full primitive q. The old mass was explicitly normalized as l=beta_M+(2M)! throughout that check.

A generic polynomial gcd is not the gcd after the large integer specialization d=D_(2M),f=(2M)!. The latter remains the final obligation in(9),(16).
