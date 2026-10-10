> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Short paired stack: exact odd-prime Laurent and primitive content

Author theorem, 2026-10-02. The fresh archive/opened primary-paper gate is in `SHORT_STACK_LAURENT_GATE.md`. Root M24 owns the construction; analysis owns all-degree nonzero and complete signed error. Root M25's extra-column lattice is not used. Local Smith/rank methods are classical; the full projected leading complement and its actual q interface below are specific author derivations.

## 1. Complete p-integral regular part

Let k>=2 and let p be an odd prime with

    4k<p<6k−5.

Set

    h=(p+1)/2,
    t=3k−1−h,
    m=k−t,
    N=2k−t=k+m.

The nonempty strict range gives1<=t<=k−2. Keep root's exact k by2k matrices C,R,V. Throughout the actual moment range r<=3k−2, precisely one positive odd denominator is divisible by p: it is p itself. Define the integer residue matrix

    E_ij=4(−1)^(i+j−h) 1_(i+j>=h).

Then EXACTLY

    R=Rreg+E/p,                Rreg in Z_(p)^(k by2k).  (1)

Here Rreg=R−E/p retains the entire factorial term and every regular arctangent denominator; no endpoint or carry is discarded.

E is supported on the last t rows and last t columns. Its t-square nonzero block has zero entries before the anti-diagonal and value4 on that anti-diagonal. Hence it has exact rank t and determinant

    epsilon_t 4^t,
    epsilon_t=(−1)^(t(t−1)/2).                  (2)

## 2. The whole leading polynomial in S

Introduce an indeterminate z and form

    P(T,z)=det[C;Rreg+z E+T V]
          =P0(z)+T P1(z).                     (3)

The polynomial is affine in T and has z-degree at most t. Its leading coefficient is

    [z^t]P(T,z)=epsilon_t 4^t Delta_(k,m)(T),   (4)

where the FULL complement is

    Delta_(k,m)(T)=det[Csmall;Rsmall+T Vsmall]
                 =A_(k,m)+T B_(k,m),

with k top rows, m bottom rows and columns0,...,N−1. Csmall and Rsmall use the original exact moments with top row indices0,...,k−1 and bottom indices0,...,m−1. Rsmall has NO denominator p, so it equals the corresponding regular part. Indeed its largest moment index is k+2m−2=3k−2t−2<h. The top block's largest derangement index is2(h−1)=p−1.

Proof: to get z^t one must use all t supported bottom residue rows and all t supported residue columns. Their exterior determinant is(2). Deleting them leaves exactly the stated complement, and the row/column deletion signs cancel because the deleted index sets coincide. The residue rank bounds every term using more than t residue rows. This proves the entire affine leading polynomial, not just a raw pole order.

In particular BOTH constant and S coefficients can have pole order t. Replacing one of the m regular lower rows by the S response keeps every residue row available. Rank t alone cannot force the constant coefficient to have a larger pole order.

## 3. A division-free response-minor reduction

The leading S coefficient B_(k,m) has the exact determinant

    B_(k,m)=det[ Dsmall ; v ; Ksmall ],        (5)

where

    Dsmall_ij=D_(2(i+j))    (i0,...,k−1, j0,...,N−1),
    v_j=(−1)^j,
    Ksmall_ij=−(2(i+j))!−(2(i+j)+2)!+4/(2(i+j)+1),
                  i0,...,m−2, j0,...,N−1.

If m=1, the K block is empty; the strict prime range used here actually has m>=2.

Proof: transform the m lower rows to first row R_0+T v and subsequent rows(R_i+R_(i+1)), i0,...,m−2. The triangular row transformation has determinant1 and kills V in all subsequent rows. The coefficient of T replaces the first lower row by v. The scalar identity

    R_r+R_(r+1)=−(2r)!−(2r+2)!+4/(2r+1)

gives Ksmall. Finally add(−1)^i times the v row to each top C_i row; this replaces Csmall by Dsmall with no determinant change. All operations are integer and require no inverse or nonzero determinant.

Every denominator in Ksmall is strictly smaller than p. Formula(5) therefore gives a p-integral leading response minor without any old arctangent primitive sums or chosen kernel basis. Its vanishing modulo p is the actual first arithmetic obligation.

## 4. Actual primitive p-valuation, including all carries

Write

    Pi(z)=sum_(j=0)^t c_(i,j) z^j, i0,1,
    c_(i,j) in Z_(p).

At the ACTUAL matrix, z=1/p. Set

    Hi=p^t beta_i=sum_(j=0)^t c_(i,j) p^(t−j). (6)

This is the full carried integer pair locally at p. For beta1!=0 the ACTUAL reduced center denominator has depth

    v_p(q)=max(0,v_p(H1)−v_p(H0)).             (7)

If beta0=0, use v_p(H0)=infinity and q has p-depth0. Common rational scale and every kernel-basis multiplier cancel in(7). It is equivalent to root's full global final gcd, not a row-clearing estimate.

Its first residues are, from(4),

    H0=epsilon_t4^t A_(k,m) modp,
    H1=epsilon_t4^t B_(k,m) modp.              (8)

Thus the following ALL-DEGREE implications hold:

- If B_(k,m) is a p-unit, then v_p(q)=0, regardless of A_(k,m). The entire apparent denominator prime disappears in the full primitive pair.
- If A_(k,m) is a p-unit and B_(k,m)=0 modp, then v_p(q)=v_p(H1)>=1. The constant coefficient has pole order t while the S coefficient has smaller actual pole order; higher carries in(6) decide the exact surviving depth.
- If both leading minors vanish modulo p, both complete H values and their final difference of valuations in(7) must be retained. A rank or first-residue argument alone gives no surviving-q conclusion.

For any desired precision b, formula(6) requires exactly the terms with t−j<b and each corresponding c_(i,j) modulo p^(b−t+j). Since all c coefficients are p-integral, this is a complete finite Laurent carry procedure. It retains regular determinant terms and cannot be replaced by repeatedly reading only the leading residue.

## 5. A single exact structural normalization witness

A bounded receipt used k4,p17,t2,m2,N6, to test whether the residue staircase itself forces a denominator prime. It computes the two complement minors and obtains

    A_(4,2)=10 mod17,
    B_(4,2)=4 mod17.

Both are units, hence both ACTUAL beta coefficients have pole order2, but v17(q)=0. Root's exact full primitive denominator at k4 confirms that17 does not divide q. The witness is recorded in `SHORT_STACK_LAURENT_RECEIPT.json`; it is one structurally selected normalization test, not a degree/prime atlas or an infinite nonvanishing claim.

## 6. What remains open

The arithmetic question is now an explicit p-integral complementary determinant, especially(5). A uniform theorem showing its vanishing, its unit property, or its exceptional-prime density is not proved here. The residue staircase does not itself force actual prime survival, and odd denominators in the input cannot be counted as prime mass in the reduced q. Formula(7) is the required exact final interface for any further theorem.

No global denominator rate, primitive-small-form result or irrationality claim follows from this conditional unit/nonunit classification. Analysis's complete nonzero/error theorem and the actual arithmetic need to be combined only after this remaining minor problem is solved.

## 7. Guaranteed shared content over the ENTIRE upper prime interval

The pole-rank theorem already gives a uniform positive common factor, even before deciding any leading minor. Let

    L_k=lcm(1,3,...,6k−5),
    I_k={primes p:4k<p<6k−5},
    W_k=product_(p in I_k) p^(k−t_p),
    t_p=3k−1−(p+1)/2.

For every p in I_k, v_p(L_k)=1 and equations(3),(6) give

    v_p(L_k^k beta_i)>=k−t_p, i0,1.

Consequently the integer W_k divides BOTH complete coefficients

    L_k^k beta0 and L_k^k beta1.              (9)

This is a guaranteed common factor of the ACTUAL full integer pair, not a claim that L_k^k is the reduced denominator. If beta1!=0, it yields the honest actual-q ceiling

    q <= |L_k^k beta1|/W_k.                   (10)

The exponent k−t_p=(p−4k+3)/2 is explicit at every prime. Higher shared content and the final gcd still remain in force. In particular the leading-response-unit theorem can eliminate the entire remaining p-cost; it is not assumed in(9).

Thus the full upper interval supplies a proved clearing-content improvement, even though the residue staircase alone cannot force surviving actual denominator mass. The exact logarithmic saving is

    log W_k=sum_(p in I_k) ((p−4k+3)/2)log p. (11)

Its asymptotic evaluation is a classical prime-distribution refinement, separate from the new determinant-content identity(9). It cannot by itself replace the global primitive denominator theorem.

For the classical evaluation in(11), use theta(x)=x+o(x), previously read in the original Rosser–Schoenfeld paper, equation(2.29), https://denisevellachemla.eu/Rosser-Schoenfeld-1962.pdf; the exact earlier archive/primary gate is retained in `WEIGHTED_DIFFERENCE_BLOCK_NONVANISHING.md` Section9. This is credited classical refinement, not new prime-distribution work. Partial summation gives

    log W_k = (1/2)[(6k−4k)theta(6k)
                     −integral_(4k)^(6k) theta(x)dx]+o(k²)
            =k²+o(k²).

Strict endpoint adjustments and the additive3/2 prime weight cost O(k log k), hence do not affect the leading k². The new all-degree determinant result is the divisibility(9); PNT only evaluates its proved exact factor.
