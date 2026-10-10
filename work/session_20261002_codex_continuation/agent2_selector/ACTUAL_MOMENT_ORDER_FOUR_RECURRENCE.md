> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A regular order-four recurrence for the actual full contour moments

Date: 2026-10-02. Status: original author derivation, not independently audited. The symbolic calculation is an exact coefficient-field elimination of a displayed total derivative, not a recurrence fit. It does not yet prove O(1)-shift nonvanishing for W. Search and primary-paper context are recorded in `RECURRENCE_TARGET_PROGRESS.md`.

## 1. Actual moment and differential certificate

Let n≥1 be an integer, a=(1+i)/2, V=w²−w+1/2, A=(2w²−1)², and

    f=V^n/w^(n+1), I_m=∫_(bar a)^a f(w)A(w)^m dw,
    g=wV(2w²−1)=2w^5−2w^4+w²−w/2.

All endpoints and contour are the actual selector endpoints. The path avoids w=0. Set

    R=(8m+2n+8)w^4−(8m+6)w³+(4m−2n)w²+w+n/2,
    T_(n,m)(h)=g h′+R h.

Direct logarithmic differentiation proves the exact identity

    D_w(g h f A^m)=f A^m T_(n,m)(h).               (1)

The multiplier at either endpoint has factor V^(n+1), so the boundary value is zero for every polynomial h and every integer m≥0. Thus

    ∫_(bar a)^a f A^m T_(n,m)(h)dw=0.             (2)

For the upper half-contour J_m the lower boundary at w=1/2 does not vanish; (2) is for the full contour and is not asserted as a homogeneous recurrence for J alone.

For h=w^k, the five possible monomials in T(h) are

    (2k+8m+2n+8) w^(k+4)
    +(−2k−8m−6) w^(k+3)
    +(4m−2n) w^(k+2)
    +(k+1) w^(k+1)+(n−k)w^k/2.                    (3)

The leading factor is positive for k≥0,n≥1,m≥0. In particular T is injective on polynomials: a nonzero h of degree k has nonzero T(h) of degree k+4.

## 2. A four-dimensional exact reduction

Over the coefficient field Q(n,m), reduce any polynomial p by repeatedly subtracting its leading coefficient divided by 2k+8m+2n+8 times T(w^k), where its current degree is k+4. The resulting unique remainder b(p) has degree at most three. This constructs p=T(h_p)+b(p); uniqueness follows from injectivity and the degree-raising property.

For j=0,…,4 write the reduced coefficient column

    b_j=( [w^0]b(A^j), …, [w^3]b(A^j) )^T.

Define by signed maximal minors

    c_j=(−1)^j det(b_0,…,hat b_j,…,b_4).          (4)

Then Σc_j b_j=0, hence Σc_j A^j=T(h) for the explicitly reduced h=Σc_j h_(A^j). Integrating (2) gives

    Σ_(j=0)^4 c_j(n,m) I_(m+j)=0.                 (5)

Thus the recurrence follows from a total derivative at the actual endpoints. It neither relies on guessed numerical values nor suppresses a conjugate contribution.

The script `derive_moment_recurrence.py` implements precisely (3)–(4) over SymPy's rational-function coefficient field. It saved the entire rational coefficient vector in `moment_recurrence_coefficients.json` and its factorizations in `moment_recurrence_derivation.log`. An initial array-padding bug was corrected before the successful full symbolic run; no failed output is used as evidence.

## 3. Nonvanishing leading coefficient and complete singular ledger

The exact resulting leading coefficient factors as

    c_4=−8192 n(m+1)(2m+1) P_6(m,n) /
        ∏_(j=4)^12 (4m+n+j),                      (6)

where

    P_6=6400m^6+2880m^5 n+74080m^5
        +144m^4 n²+25824m^4 n+348832m^4
        +984m³ n²+89560m³ n+852476m³
        +2323m² n²+149229m² n+1135320m²
        +2171m n²+118241m n+776356m
        +624n²+34992n+210816.

Every coefficient of P_6 is positive. Therefore c_4≠0 for every n≥1,m≥0. The coefficient-field reduction divisions were the positive linear factors 2k+8m+2n+8, 0≤k≤12, and no denominator vanishes in this domain. The saved rational c_j denominators all factor into positive 4m+n+j with 4≤j≤16. Multiplying (5) by their positive common product gives a polynomial-coefficient recurrence whose leading coefficient is still nonzero for all such m.

The trailing coefficient also has no zero in this domain: the successful exact factorization is −2097152 n(m+1)²(m+2)(2m+1)²(2m+3) times a polynomial with all positive coefficients, divided by ∏_(j=4)^16(4m+n+j). Thus both forward and backward propagation are regular on nonnegative integer m.

Consequently four consecutive zero actual I-values imply an identically zero forward tail. For n=4k the fixed-n endpoint asymptotic below contradicts such a tail. This is a constant-shift statement for I_m, not yet for W.

## 4. Fixed-n endpoint asymptotic

For each fixed n, set w=a−ix/2 on the upper half segment. The exact endpoint expansion gives

    J_m∼C_n (−2i)^m m^(−n−1),
    C_n=[i/(2a)](2a)^(−n) n!/2^(n+1).             (7)

It follows by Watson's lemma on the finite segment: V=(x/2)(1−x/2), A=(−2i)[1−x+(1+i)x²/4]², and the exponent has derivative −2 at x=0. A fixed positive tail x≥ε has |A|<2; the local scaled x=u/m integral converges to ∫_0^∞u^n e^(−2u)du=n!/2^(n+1). These estimates hold with n fixed; no uniformity in n is claimed or needed for zero propagation.

For n=4k, the phase of C_n is π/4 modulo π. Hence its real and imaginary parts are both nonzero; multiplication by (−i)^m only cycles these nonzero values. Since I_m=2i Im J_m, (7) shows I_m≠0 for every sufficiently large m, for each fixed n=4k. The regular recurrence therefore proves that no four consecutive I_m can vanish for any m≥0 at this fixed n.

## 5. Transfer to weighted E and actual W: current obstruction

For n=4k retain U_m, E_m=U_m(T_m−πU_m), and W_m=Δ^(n+1)E_m. Since T_m−πU_m=i2^(n+1)I_m, E differs from U_m I_m by a fixed nonzero factor. On U≠0 nodes, (5) becomes a recurrence for E by replacing c_j with c_j/U_(m+j). Clearing all U denominators gives coefficients c_j∏_(h≠j)U_(m+h). Its leading coefficient can vanish when any of U_m,…,U_(m+3) vanishes. Such zeros are real features of the forcing polynomial, not mere numerical exceptions.

There is an exact reduction of state dimension. Multiplying the moment recurrence by i2^(n+1) and substituting T_m−πU_m gives two rational-coefficient sums whose difference is π times one of them. Irrationality of π forces both sums separately to vanish. Hence U and T satisfy the same regular recurrence. The vector v_m=(U_m,…,U_(m+3))^T is a nonzero invariant solution: four zero U-values would force the nonzero polynomial U to have an identically-zero tail, which is impossible.

Let x_m=(I_m,…,I_(m+3))^T, and express W_m as a rational row a_m x_m using its exact n+2-term weighted difference and repeated moment transitions. Because Δ^(n+1)(U_m²)=0, a_m v_m=0. The four-output observability determinant is therefore identically zero; it is not a valid nonvanishing target. An earlier incremental formulation suggesting that determinant was corrected as soon as this exact annihilated mode was recognized.

The actual W output instead lives in the quotient of the four-dimensional moment state by the one-dimensional U solution. It thus admits a rational-coefficient recurrence of order at most THREE over Q(m). A concrete target is to prove rank three for the stacked output rows a_m, a_(m+1)T_m, a_(m+2)T_(m+1)T_m on this quotient at every actual nonnegative integer start (or in the required large-selector regime), with its transition minors regular. If three consecutive outputs then vanish, the moment state is proportional to v_m and the same proportionality propagates, contradicting (7), since the actual moment has exponentially growing subsequences whereas U is polynomial.

Neither positivity of c_4 nor generic holonomic closure proves that rank/minor property at every actual integer start. The row a_m depends on the actual U polynomial and the high order n+1 difference. The quotient output minors are the remaining specific O(1)-shift target; they may have apparent singular factors and must be derived or controlled rather than assumed.

The already proved O(n) nonvanishing theorem remains valid and needs none of this uncompleted transfer. The new recurrence supplies genuine constant-order actual moment structure, with a full positive-domain division ledger, but no all-start nonvanishing claim for W.

## 6. A simpler exact three-state representation after pole cancellation

The polynomial-integral identity for W permits a direct three-state representation without quotient coordinates or division by U. This makes the actual transformed-minor target concrete in a second way.

Put q(w)=2w²−1 and define the polynomial full-contour moments and boundary terms

    L_l=∫_(bar a)^a q(w)^l dw,
    B_l=a q(a)^l−bar a q(bar a)^l,
    q(a)=−1+i, q(bar a)=−1−i.

Integrating D(w q^l)=(2l+1)q^l+2l q^(l−1) gives, for l≥1,

    (2l+1)L_l+2l L_(l−1)=B_l.                     (8)

Eliminating L_(2m−1) from two consecutive equations gives, for m≥1,

    (4m+1)(4m−1)L_(2m)−4m(4m−2)L_(2m−2)
      =(4m−1)B_(2m)−4m B_(2m−1).                 (9)

The boundary terms are explicit combinations of (−2i)^m and (2i)^m. Thus the state consisting of L_(2m) and these two endpoint powers has dimension three, with a regular forward transition on m≥0 after (9) is shifted to m+1.

Retain the exact polynomial

    R_(n,m)(w)=w V(w)^n(w²−1)^(r+1)Q_(n,m)(q(w)²),
    W(n,m)=i2^(2n+3)∫_(bar a)^a q(w)^(2m)R_(n,m)(w)dw.

All coefficients of R are polynomials in m over Q for each fixed n. Split it into even and odd monomials. Each even monomial has the exact reduction

    ∫w^(2h)q^(2m)dw=2^(−h)Σ_(j=0)^h binom(h,j)L_(2m+j),

and each odd monomial has the exact endpoint evaluation

    ∫w^(2h+1)q^(2m)dw
      =2^(−h−2)Σ_(j=0)^h binom(h,j)
          [q(a)^(2m+j+1)−q(bar a)^(2m+j+1)]/(2m+j+1). (10)

Set D_m=iL_(2m), which is rational by conjugate Gaussian-rational endpoint evaluation of the polynomial primitive. Equations (8), (10) therefore express the actual W as

    W(n,m)=F_n(m)D_m+G_n(m)(−2i)^m+H_n(m)(2i)^m, (11)

with explicit rational functions F_n∈Q(m), G_n,H_n∈Q(i)(m), including the common i2^(2n+3) factor. The reductions introduce only positive linear denominators 2m+j+1 and 4m+2j+1, plus powers of two; there is no U denominator. Endpoint conjugacy ensures the final expression is rational, as already known from the primitive formula.

Formula (11) is an exact three-state representation of the actual pole-cancelled certificate for every fixed n=4k and integer m≥0. It is not merely a holonomic-existence statement. Its three-output determinant still requires a uniform nonvanishing proof: regularity of this base state does not by itself give observability of the particular coefficient row (F_n,G_n,H_n). This representation may offer a more direct positivity or recurrence-in-n route than the quotient of the four-state original moment.

## 7. The actual W tail is nonzero for each fixed n

For fixed n=4k, the polynomial U has leading term u_n m^r with u_n=4^r/r!>0. Combining (7) with E_m=−2^(n+2)U_m Im J_m, then taking the fixed-order d=n+1 difference, gives

    W(n,m)=−2^(n+2)u_n m^(−r−1)
       Im[C_n(−2i)^m(−1−2i)^d]+O_n(2^m m^(−r−2)). (12)

Every shift j=0,…,d is fixed when n is fixed, so its polynomial/power factors admit relative O_n(1/m) expansions. The binomial factor sums exactly to (−2i−1)^d; this retains the actual weighted difference rather than a single summand.

The leading imaginary part is nonzero in every integer residue class of m modulo four. Indeed C_n is a nonzero real multiple of 1+i, while G=(−1−2i)^d=X+iY is a Gaussian integer with X²+Y²=5^d, an odd integer. If X=Y or X=−Y, this norm would be even. Thus X+Y and X−Y are both nonzero; the four quarter-turn imaginary parts are real nonzero multiples of these two integers and their negatives.

It follows from (12) that, for each fixed n=4k, W(n,m)≠0 for every sufficiently large m. No uniform threshold in n is asserted. This supplies exactly the fixed-n nonzero-tail ingredient of the Prellberg propagation mechanism if the particular three-output determinant can be proved regular at the required starts. It does not replace that determinant obligation in the scaling m≈ρn log n.
