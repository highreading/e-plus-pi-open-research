> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the full integral Witt bridge and valued consequence

2026-09-13. Reviewed `witt_depth_lift_attempt.md`, Item424's exact Bockstein, the universal partial-fraction lift, Item194's complete endpoint kernel and same-row rank proof, Item197's exact residue substitution, and Item427's shifted determinantal ideal. This is a bounded continuation of the earlier independent first-Witt review.

**Verdict:** the full three-coordinate bridge is valid on the stated ordinary PNT-side rows, including j=0. It has a common invertible diagonal sign matrix, with the angular sign depending on p modulo4. Therefore Item194's same-row rank-two theorem applies to the actual integral rows, not only to their rational-log determinant. The resulting DVR ideal equality and the assertion that the full depth equals the normalized log-gcd valuation plus zero or one are sound. The aggregate equivalence is sound only on this stated cell set; the note correctly preserves that restriction and does not replace small radical mass by a bound on unbounded multiplicities.

## 1. Domain and exact Bockstein

Write a=3j+1, c=2j+1 and

    F_j=u^a/Q^c,
    omega_nu=F_j^p P_nu dx,
    P_nu=u^r Q^(2s-nu),
    p=2r+6s+3.

The domain is j>=0, s>=1, r>=1, a<p and2j+2<p, with the actual integrality condition for m. It implies the Item424 hypothesis p^2>4m+1. In particular c<p. The theorem must not be extended to the PNT-complement merely because that complement has small radical weight.

The zero-constant primitive T_nu of P_nu has coefficients in Z_(p), since its degree is at most p-2 or p-5. Define

    eta_nu=F_j^(p-1)F'_j T_nu dx.

The characteristic-zero identity

    omega_nu=d(F_j^p T_nu)-p eta_nu

has zero endpoint boundary because F_j vanishes at0 and1. Consequently

    W_nu=(R_nu,L_nu/p,E_nu/p)
        =(-pR(eta_nu),-L(eta_nu),-E(eta_nu))

is an exact equality before reduction. Its coordinates are p-integral by the rank-zero normalization. No determinant carry is used to obtain this equality.

## 2. Componentwise Cartier comparison

Work over the unramified splitting ring obtained by adjoining i; when p splits, the equivalent product splitting algebra may be used. The poles -1,i,-i and both endpoint distances are p-units apart. Partial fractions of eta_nu therefore have p-integral coefficients. There is no polynomial quotient: F_j has degree -1 at infinity, F'_j has degree at most -2, and deg T_nu<=p-2, so eta_nu is proper of order at least three.

Its finite pole orders are at most cp+1<p^2. Thus in the exact rational endpoint formula for pR(eta_nu), only pole orders ph+1 can survive modulo p. Here h<p, and the surviving terms are

    -c_(alpha,ph+1)[(1-alpha)^(-ph)-(-alpha)^(-ph)]/h.

All remaining pole orders have a p-unit primitive denominator and are multiplied by p. There is no p^2 resonance in this domain.

Let sigma be Frobenius on the residue splitting algebra. The local Cartier formula replaces a pole term of order ph+1 by one of order h+1 with coefficient sigma^(-1)(c_(alpha,ph+1)). The endpoint powers satisfy

    (b-alpha)^(-ph)=(b-sigma(alpha))^(-h) mod p,
    b=0,1.

Because eta_nu has coefficients in F_p, its partial-fraction coefficients are Frobenius-compatible. Reindexing the poles by sigma identifies the surviving endpoint sum exactly with the rational endpoint of Phi_nu=C(eta_nu). Therefore

    R(Phi_nu)=pR(eta_nu) mod p.

This is a relative rational endpoint identity. It would be wrong to replace the rational endpoint by the simple residue alone.

For the logarithmic and angular coordinates, the exact residue maps are

    L=4c_(-1,1)+2(c_(i,1)+c_(-i,1)),
    E=2i(c_(i,1)-c_(-i,1)).

Cartier applies inverse Frobenius to the residues. Put chi_p=(-1)^((p-1)/2), so sigma(i)=chi_p i. The symmetric residue combination is unchanged, while the antisymmetric combination gains chi_p. Hence

    L(Phi_nu)=L(eta_nu),
    E(Phi_nu)=chi_p E(eta_nu) mod p.

Combining with the exact Bockstein gives the complete relation

    E_j(H_nu)=(-R_nu,-L_nu/p,-chi_p E_nu/p) mod p,

or equivalently

    W_nu=diag(-1,-1,-chi_p) E_j(H_nu) mod p.

The same matrix applies to both nu and to consecutive m at fixed p,j. It is invertible. At p congruent3 modulo4 this is diag(-1,-1,+1); at p congruent1 modulo4 it is diag(-1,-1,-1). This proves the observed sign pattern without extrapolating from a single prime.

No Fermat or signed carry has been omitted at this stage. The exact Bockstein already performs the required division by p, and the Cartier comparison above is only modulo p. A claim about the next coordinate digit would need the additional terms discussed in Section6.

## 3. Same-row rank two for the actual integral rows

The relevant rank theorem is Item194 Section5, for the two differentials nu=0,1 at the same construction index. It is distinct from the new three-shift determinant theorem.

The endpoint map kernel is exactly the Frobenius direction G_j, under the displayed pole and endpoint-order bounds. Its proof extends to j=0, as verified in the preceding review. A dependence of the two projected rows would consequently give

    W=alpha T_0+beta T_1-gamma x^p,

vanishing at the four roots, with (alpha,beta) nonzero. Its derivative is

    W'=u^r Q^(2s-1)(alpha Q+beta).

Since W also vanishes at0 and the relevant local orders are all below p, it is divisible by `u^(r+1)Q^(2s)`, of degree p-1. Therefore W equals this divisor times `lambda x+mu`. Differentiating and comparing gives the displayed polynomial identity in the depth note.

I independently expanded its two decisive coefficients. The difference between its x and x^2 coefficients is `(p-8s)lambda`. Since p is odd and0<s<p, this forces lambda=0. The x^4 coefficient is then `-(p-1)mu`, forcing mu=0. This contradicts (alpha,beta) nonzero. The argument retains the gamma x^p term and has no omitted exceptional root or seed assumption.

Thus E_j(H_0),E_j(H_1) are independent. The common invertible diagonal comparison in Section2 proves that the actual reductions of W_0,W_1 also have rank two. This is the full rank needed for the valuation argument; equality of the kappa determinants alone would not have sufficed.

## 4. The exact DVR ideal, not just its first digit

Use the actual integral entries rho_nu=R_nu, ell_nu=L_nu/p and e_nu=E_nu/p, and put

    K=ell_1 rho_0-ell_0 rho_1=A_m/p,
    X=ell_1 e_0-ell_0 e_1=8B_m/p^2.

If at least one ell_nu is a unit, simultaneous divisibility of K and X by p would make the two full rows dependent modulo p. Hence both ideals (K,X) and (ell_0,ell_1) are the unit ideal.

If both ell_nu are divisible by p, rank two forces the rho-e minor to be a unit. The linear map from (ell_0,ell_1) to (K,X) has determinant equal, up to sign, to that minor. It is an invertible matrix over Z_p, so it preserves the generated ideal exactly.

In both cases

    (A_m/p,8B_m/p^2)=(L_0/p,L_1/p) in Z_p.

For finite `t=min(v_p(ell_0),v_p(ell_1))`, this gives `min(v_p(K),v_p(X))=t`. Item427's exact shifted ideal then implies

    d=v_p(c_m)-b_(m,p)=min(v_p(K),1+v_p(X)) in {t,t+1}.

More precisely d=t+1 exactly when v_p(K)>t. The exact rational residue substitution gives `L_nu=2^(-2m-2nu)C_nu(m)`, so powers of2 do not affect valuations. Since F_m contains one copy of p on the rank-zero set,

    t=min(v_p(C_0/F_m),v_p(C_1/F_m)),
    d<=min(v_p(C_0),v_p(C_1)).

If both exact logarithmic coordinates are zero, the ideal equality states that K=X=0; the finite-valued formulation must then be replaced by that statement. The note correctly makes this qualification.

The extra one is necessary: Item421's actual counterexamples have d=1,t=0. The new theorem does not revive the disproved stronger inequality d<=t.

## 5. Aggregate comparison and the all-level rank consequence

On exactly the stated PNT-side cell set and when the masses are finite, write d=t+epsilon with epsilon in {0,1}. If epsilon=1 then d>=1, so its prime lies in the first-Witt support. Therefore

    0<=sum_p(d-t)log p<=W_kappa(m).

The already reviewed radical-support theorem makes the difference o(X^2) after dyadic averaging. Thus the full depth mass and the full valuation mass of the normalized common-log pair have the same normalized dyadic-average asymptotics on this set. This is a legitimate reduction of the unresolved tail problem. It is not a proof that either full valuation mass is sublinear.

This comparison does not cover the omitted PNT-complement depth. Small radical weight there is insufficient to discard its multiplicities, and the note explicitly preserves that limitation.

The separate three-shift rank theorem gives an invertible matrix of actual integral nu=0 rows away from its sextic exceptions, because the diagonal bridge is common across the three rows. For a fixed integral coefficient vector v, multiplication by this matrix and its integral inverse preserves the ideal generated by its entries. Hence the minimum valuation of the three observations equals the minimum valuation of v's coefficients. This is a correct statement at every depth. It does not apply to an arbitrary observation whose coefficient vector changes between the three rows, and the note does not claim that application.

An invertible matrix may have an individual entry of arbitrarily high valuation. The displayed elementary example therefore correctly explains why the three-observation statement does not bound a singleton valuation.

## 6. Why the mod-p rank proof cannot simply be repeated modulo p^2

The proof of the mod-p dependence obstruction uses `(x^p)'=0`. Modulo p^2,

    (alpha T_0+beta T_1-gamma x^p)'
       =alpha P_0+beta P_1-p gamma x^(p-1).

When gamma is a unit, the last term is nonzero at x=1 modulo p^2, while the P_nu terms vanish there. The high endpoint multiplicity required by the divisibility argument is lost. The same problem occurs at the Q roots.

There is also the exact phase difference `2s+1=-2r/3+p/3`. Thus the lifted coefficient system has extra p-times terms even before accounting for endpoint corrections. The Hasse/Fermat defect of the local units and the endpoint-power corrections in `witt_endpoint_first_lift.md` are precisely relevant to such a lift. Higher determinant digits additionally have ordinary signed carries.

An integral matrix whose reduction is invertible remains invertible at every level, so the rank information itself persists. What does not persist is a homogeneous equation with zero right side: the lifted system solves for new inhomogeneous carry terms. The valued ideal theorem above avoids this problem by using exact integral algebra after obtaining rank two modulo p. It does not assert that the complete componentwise Cartier formula holds unchanged modulo every p^k.

## 7. Bounded exact normalization checks

The companion `witt_integral_bridge_checks.py` independently reconstructed the original rational endpoint coordinates and the small projected endpoint coordinates on four rows, covering p=11,13,17, both p modulo4 classes, j=0 and j>=1. It checked the full diagonal relation, actual rank-two minors, the exact integer residue substitution and the DVR valuation conclusion. All passed. These are normalization checks supporting the proof, not the basis for any uniform assertion. Results are in `witt_integral_bridge_checks.json`.
