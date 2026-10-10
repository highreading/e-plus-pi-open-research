> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A valued first-Witt theorem and the exact obstruction to summing all depths

2026-09-13. New actual-family valuation theorem on the PNT-side ordinary cells, independently reviewed. The full Witt depth is the normalized common-log valuation plus either zero or one. Together with the new first-Witt support theorem this reduces, but does not settle, the uniform-integrability problem. No irrationality conclusion is claimed.

## 1. Exact normalization and new theorem

Use precisely Item427's ordinary row and normalization:

    4m+1=(2j+1)p-2s, p=2r+6s+3,
    j>=0, s>=1, r>=1, 3j+1<p, 2j+2<p,

    Kcal=A_m/p, Xcal=8B_m/p^2,
    d_(m,p)=v_p(c_m)-b_(m,p)=min(v_p(Kcal),1+v_p(Xcal)).

Here b_(m,p)=v_p(K_m) is exactly the already removed baseline from Item427; K_m and Kcal are different objects. The displayed inequalities include the j=0 cell and the canonical PNT-side j>=1 cells. They imply p^2>4m+1. We do not extend this theorem to the omitted band where3j+1>=p merely because its radical is small.

Let the exact integral first-error rows be

    W_nu=(R_nu, ell_nu, e_nu)
        =(R_nu,L_nu/p,E_nu/p), nu=0,1.

Then the following is an equality of ideals in Z_p, not only a first-digit congruence:

    (Kcal,Xcal)=(ell_0,ell_1).                         (1)

Consequently, with v_p(0)=infinity and

    t_(m,p)=min(v_p(ell_0),v_p(ell_1)),

we have, whenever t is finite,

    d_(m,p) in {t_(m,p),t_(m,p)+1}.                    (2)

More precisely d=t+1 exactly when v_p(Kcal)>t; otherwise d=t. This one additional copy is the precise pointwise information that the divided log pair can miss.

Item197's residue substitution is an exact rational identity and gives

    L_nu=2^(-2m-2nu) C_nu(m).

Since p is odd and F_m=G_m contains exactly one copy of every ordinary rank-zero prime,

    t_(m,p)=min(v_p(C_0(m)/F_m),v_p(C_1(m)/F_m)).       (3)

In particular d_(m,p)<=min(v_p(C_0(m)),v_p(C_1(m))). If both exact log coordinates vanish, (1) says both target determinants vanish as well; the finite-valued formulation(2) is then replaced by that exact statement. The independently verified analytic dependency core_analytic_audit.md, Sections3-4 (reviewed in saddle_independent_review.md), proves B_m!=0 at every sufficiently large m. Therefore L_0,L_1 cannot both vanish at those m, since B_m=(L_1E_0-L_0E_1)/8. All t values and normalized common-log gcds in sufficiently large dyadic blocks are consequently finite. This uses a verified eventual analytic nonvanishing theorem; no unproved all-index gcd nonvanishing is assumed.

## 2. The componentwise bridge, including rational endpoint and Frobenius sign

The first-Witt rank argument needs all three components, not merely equality of the rational-log determinant. Retain Item424's exact Bockstein identity

    omega_nu=d(F_j^p T_nu)-p eta_nu,
    eta_nu=F_j^(p-1)F'_j T_nu dx,
    F_j=u^(3j+1)/Q^(2j+1).

Its boundary is zero. Hence exactly over Q,

    (R_nu,L_nu/p,E_nu/p)
          =(-p R(eta_nu),-L(eta_nu),-E(eta_nu)).        (4)

The reduced Cartier differential is the canonical Item194 four-section form

    Phi_nu=C eta_nu=u^(3j)H_nu/Q^(2j+2) dx.

Put chi_p=(-1)^((p-1)/2). The componentwise bridge is

    E_j(H_nu)=(-R_nu,-ell_nu,-chi_p e_nu) mod p.       (5)

Here E_j on the left denotes the three-coordinate endpoint map. To check the rational coordinate in(5), work in the unramified splitting algebra Z_p[i]. All partial-fraction coefficients of eta_nu are p-integral: T_nu has unit denominators, and the differences among -1,i,-i are units. The pole orders are at most (2j+1)p+1<p^2; eta_nu is proper at infinity. Thus the only terms that survive in pR(eta_nu) modulo p have pole order hp+1, with h<p. Integration replaces their denominator hp by h after multiplication by p. Their endpoint powers satisfy

    (a-alpha)^(-hp)=(a-alpha^p)^(-h) mod p, a=0,1.

These are exactly the rational endpoint terms of Cartier. Reindexing the poles by Frobenius matches the inverse-Frobenius action on each coefficient. Therefore

    R(Phi_nu)=pR(eta_nu) mod p.

Cartier preserves the rational residue combination giving L, while inverse Frobenius acts on i by chi_p. Thus

    L(Phi_nu)=L(eta_nu),
    E(Phi_nu)=chi_p E(eta_nu) mod p.

Combining with(4) proves(5). This derivation retains the rational pole-index band; it does not assume that the rational endpoint is an ordinary residue. It also accounts for the angular Frobenius sign.

## 3. The actual pair has rank two modulo p

The canonical dependency is Item194, Sections4.2 and5. Its proof extends unchanged to j=0 under the displayed unit hypotheses. A self-contained account of the endpoint map kernel, including j=0, is in witt_actual_exterior_rank.md, Section4:

    ker E_j=F_p G_j,
    G_j=uQ+xD_j,
    H_nu(zeta^p)=D_j(zeta)T_nu(zeta).

If the two E_j(H_nu) were proportional, the evaluation rows T_0,T_1,Frobenius would be dependent. Thus some alpha,beta,gamma, with (alpha,beta)!=(0,0), would make

    W=alpha T_0+beta T_1-gamma x^p

vanish at all fourth roots of unity. Its derivative is

    W'=u^r Q^(2s-1)(alpha Q+beta).

As in the original proof, endpoint vanishing and the local derivative orders force

    W=u^(r+1)Q^(2s)(lambda x+mu),

because the divisor has degree p-1 and deg W<=p. Differentiating gives

    alpha Q+beta
      =Q{lambda u+(r+1)u'(lambda x+mu)}
                            +2s uQ'(lambda x+mu).

The difference of its x and x^2 coefficients is (p-8s)lambda, so lambda=0. The x^4 coefficient is then -(p-1)mu, so mu=0. This contradicts (alpha,beta)!=(0,0). All cancelled local orders are below p, and the Frobenius x^p term has been explicitly retained.

Hence the E_j(H_0),E_j(H_1) rows have rank two. By the invertible diagonal bridge(5), so do the reductions of the actual integral rows W_0,W_1.

## 4. The DVR lemma and exact valued conclusion

Let two rows (R_0,ell_0,e_0),(R_1,ell_1,e_1) over Z_p have rank two modulo p. Put

    K=ell_1R_0-ell_0R_1,
    X=ell_1e_0-ell_0e_1.

If at least one ell is a unit, K and X cannot both be divisible by p: that would make the full two rows proportional modulo p. Therefore both ideals (K,X) and (ell_0,ell_1) are the unit ideal.

If both ell are divisible by p, rank two forces the R-e minor R_0e_1-R_1e_0 to be a unit. The matrix taking (ell_0,ell_1) to (K,X) is then invertible over Z_p, so it preserves the generated ideal exactly. This proves(1) in both cases. Applying the lemma to the exact rows W_nu identifies K=Kcal and X=Xcal by Item427's formulas(2.9)-(2.10), with the latter divided by its explicit extra p. There is no loss of a p factor.

Equation(1) gives min(v_p(Kcal),v_p(Xcal))=t. Taking the shifted minimum min(v_p(Kcal),1+v_p(Xcal)) proves(2). This is a valued theorem for the actual family; Item427's arbitrary ambient streams do not contradict it because its ambient examples need not have the rank-two reduction proved in Section3.

## 5. Consequence for the aggregate problem

On the stated PNT-side ordinary set, write d=t+epsilon, epsilon in {0,1}. Then

    0<=sum_p d_(m,p)log p - sum_p t_(m,p)log p
                      <=sum_(p:d_(m,p)>=1)log p.         (6)

The right side is exactly bounded by the first-Witt radical support. The newly proved support theorem therefore makes its dyadic average o(X^2). The eventual nonvanishing dependency in Section1 ensures finiteness throughout every sufficiently large dyadic block. Thus the full Witt depth mass and the normalized common-log valuation mass have the same normalized dyadic-average asymptotics.

Thus an averaged sublinear full-depth theorem is now equivalent, within this cell range, to

    sum_(X<=m<2X) sum_p
       min(v_p(C_0(m)/F_m),v_p(C_1(m)/F_m)) log p=o(X^2). (7)

The new first-Witt theorem controls the one-copy discrepancy that caused Item421's counterexample to the divided-log carrier. It does not prove(7). Equation(7) involves the full valuations of the normalized common-log gcd, not just its radical. Item200 explicitly distinguishes these objects and gives a local two-row resultant obstruction.

The small-prime/PNT-complement band remains separate. A sublinear radical bound on that band does not by itself bound its full depth contribution.

## 6. What the 26-by-26 rank theorem lifts, and what it does not

There is a useful exact integral consequence of the new rank theorem. Away from its sextic exceptional rows, the three actual nu=0 rows W_0(m),W_0(m-1),W_0(m-2) form an invertible matrix over Z_p, because their reductions form a basis by witt_actual_exterior_rank.md and the componentwise bridge(5). Thus, for any integral linear functional with coefficient vector v,

    min_(k=0,1,2) v_p(v dot W_0(m-k))
                          =min_i v_p(v_i).              (8)

This follows by multiplying by an invertible integral matrix and its integral inverse. It is an all-level valuation statement: three adjacent observations cannot acquire a common extra p factor from the transfer alone.

It does not bound a singleton valuation. The integral invertible matrix

    [[p^N,1,0],[1,0,0],[0,0,1]]

has determinant -1 for every N, although its first observation can have valuation N. This is an information-class counterexample about what unimodular rank alone implies, not a claim that these arbitrary matrices occur in the mixed-cubic family. Item276's existing primitive-Casoratian analysis makes the analogous distinction between transporting depth and bounding it.

There is also a concrete obstruction to repeating the characteristic-p multiplicity proof modulo p^2. In that proof,

    W=alpha T_0+beta T_1-gamma x^p

has derivative alpha P_0+beta P_1 modulo p. Over Z/p^2, the derivative instead includes

    -p gamma x^(p-1).

If gamma is a unit, this term has value -p gamma at x=1. Even when W(1)=0 modulo p^2, its derivative no longer has the high endpoint zero required for divisibility by u^(r+1). The same issue occurs at Q's roots. The degree-counting argument therefore does not lift unchanged.

In addition, the exact phase relation is2s+1=-2r/3+p/3, so lifting the displayed polynomial rank system adds a p uQ'A correction. The underlying coefficient matrix may remain invertible, but the lift acquires inhomogeneous endpoint and Frobenius-carry terms. An invertible matrix solves for those new terms; it does not force them to vanish. The exact Bockstein retains these terms in eta_nu, and Item194's Frobenius defect (F(x)^p-F(x^p))/p and the Hasse lower-band examples show why they cannot be omitted.

The next concrete task is consequently a valuation theorem for the normalized common-log pair in(7), or a true arithmetic bound on these inhomogeneous carry terms. The new rank argument rules out an entire zero three-state and proves(8); it does not supply the missing uniform tail of singleton valuations.

## 7. Prior work reviewed and verification scope

Read in full for this task: Items424,426,427; Item194's kernel/rank proof; Item197's exact residue bridge; Item200's normalized-gcd and local-resultant obstruction. The relevant existing lift cautions are lifted_endpoint_hasse_formula.md (the lower pole-index bands cannot be deleted), Item194 Section3 (the signed carry in the next determinant digit), and Item276 (primitive Casoratians transport rather than cap singleton depth).

The full componentwise bridge and DVR ideal argument were independently reviewed by the computations agent. The earlier 26-by-26 determinant was independently rebuilt from its coefficient stencil and verified over Z[r]. Numerical data have not been used to infer any valuation bound or averaged theorem. No aggregate estimate(7), unbounded Witt-depth bound on the omitted band, or main e+pi proof is claimed.

Subsequent extension: paired_log_valuation_separation.md lifts the original log recurrence exactly over Q, proves a uniform two-index valuation separation, and obtains sublinear dyadic averages for every fractional depth moment of order0<theta<1 on the PNT-side set. This does not reach the first-moment estimate(7); its layer integral loses convergence at theta=1. The distinction is explicit in that note.
