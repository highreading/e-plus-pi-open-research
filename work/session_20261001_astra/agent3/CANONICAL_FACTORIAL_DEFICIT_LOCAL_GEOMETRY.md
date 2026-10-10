> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Factorial deficit: local geometry and stage closeout

Child 3 author deductions, closing the currently accepted task at the user's request. No independent review, numerical scan, or repeated computation is asserted. The preceding exceptional-deficit paper and its factorization are preserved. This stage ends with a local elimination result and an unresolved global valuation bound; no further research assignment is proposed.

## 1. Exact retained normalization

Work with the SAME b=3,m=1 factorial B-only Gram center, at n>=3 with nonsingular contact matrix. Eventual analytic interpretations use the retained even slow-growth normality domain. All quantities below refer to CANONICAL_EXCEPTIONAL_DEFICIT_CONTENT.md and CANONICAL_OVERLAP_DEFICIT.md.

Put F=(n!)^2, d0=(n+1)(n+2), e=4(n+2), and L=2^(2n+1)lcm(1,...,2n+2). The positive primitive response is

    w=(P_n,P_(n+1))/t0, t0=gcd(P_n,P_(n+1)).

The primitive reconstruction matrices are Cbar=C/k_C and Rbar=Cbar[j0 j1]/k_R. Set

    Zbar=Cbar^T Omega Rbar,
    Bbar(w)=w^T Rbar^T Omega Rbar w=abar_B Q(w),

where Q is the primitive positive integral binary quadratic form. Do not confuse this Q with a rational companion denominator. Here Omega=diag(omega_j^2), omega_j=(n+2)_j, 0<=j<=3.

The integer rows, including BOTH corrections, are

    uhat=L Ecal^T Zbar,
    vhat=L(d0 Delta/k_C)e0^T Rbar+F d0 theta Zbar.

The first term of vhat is the endpoint correction; its second term is the logarithmic companion. Let shat be their joint entry content and put u0=uhat/shat, v0=vhat/shat. Thus the four entries of u0,v0 have joint gcd one. Define

    Dtilde=F d0 L t0 k_R abar_B Q(w),
    g1=gcd(Dtilde,e shat), D1=Dtilde/g1,
    h0=gcd(D1,|u0 w|,|v0 w|),
    D2=D1/h0,
    Wcancel=((u0+v0)w)/h0.

The exact target is delta_F=gcd(F,D2,|Wcancel|). The separate factors delta_exc=delta_reg delta_res remain exactly as in the preceding paper. They are not estimated anew here.

Restrict to nonzero sum row, as holds eventually from the retained convergence of the canonical center to e+pi>0. Write

    u0+v0=c_H H, H=(H0,H1), c_H>0, gcd(H0,H1)=1.

The formulas below do not drop shat or h0. Zero sum-row cases remain covered by the original gcd definition and are outside the projective chart used here.

## 2. A two-coordinate elimination retaining the final gcd

Choose an integer row J=(J0,J1) such that H0 J1-H1 J0=1. Define

    y=H w, z=J w.

Then gcd(y,z)=1 and

    w=(J1 y-H1 z,-J0 y+H0 z)^T.

There are unique integers a,b with

    u0 w=a y+b z,
    v0 w=(c_H-a)y-b z.

They are explicitly a=u0 dot (J1,-J0), b=u0 dot (-H1,H0). Unimodularity preserves joint row content, so

    gcd(a,b,c_H)=1.

In particular b is an actual integer contraction of the primitive exponential row against the kernel of the complete sum row. It is not an unspecified new numerator. It also equals det(H,u0), up to the displayed orientation.

The final gcd and corrected numerator are now exactly

    h0=gcd(D1,|a y+b z|,|c_H y|),
    Wcancel=c_H y/h0.                                      (1)

This replaces the two original evaluated rows by one primitive response coordinate y, a transverse coordinate z, and the explicitly known coefficients a,b,c_H. The identity uses the endpoint-corrected sum row throughout.

For any prime p set

    f=2v_p(n!),
    A0=v_p(d0 L t0 k_R abar_B),
    E0=v_p(e shat),
    qv=v_p(Q(w)),
    d1=max(0,f+A0+qv-E0),
    h=min(d1,v_p(a y+b z),v_p(c_H y)).

Then the exact local exponent is

    v_p(delta_F)=min(f,d1-h,v_p(c_H y)-h).                  (2)

The convention v_p(0)=infinity is used. Formula (2) specifies the final normalization rather than presuming the row values are units before h0 is removed.

## 3. Actual discriminant of the Gram form

Write Q(X,Y)=A X^2+B XY+C Y^2. Its actual discriminant is

    Disc(Q)=B^2-4AC
           =-4 det(Rbar^T Omega Rbar)/abar_B^2 <0.           (3)

This is an exact integer evaluated from the actual canonical matrix, not the discriminant of a coordinate-center form. More explicitly, with r_i the i-th row of Rbar,

    Disc(Q)=-(4/abar_B^2)
        sum_(0<=i<j<=3) omega_i^2 omega_j^2 det(r_i,r_j)^2. (4)

Cauchy-Binet proves (4); rank two proves strict negativity. The division by abar_B^2 is part of primitive normalization. The coefficients A,B,C and their discriminant are therefore fully specified by the retained integer data, without a generic quadratic form substitution.

In coordinates (y,z), write

    Q(w)=A' y^2+B' yz+C' z^2.

The unimodular substitution preserves the discriminant exactly. Its constant coefficient is

    C'=Q(-H1,H0)=Rresultant>0.                            (5)

For an odd prime p not dividing Disc(Q), the actual reduction is either split, when Disc(Q) is a nonzero square modulo p, or nonsplit, when it is a nonsquare. In the nonsplit case Q(w) is a p-adic unit for every primitive integer w: a nonzero zero of the reduced binary form would give an isotropic line and hence a square discriminant.

In the split case there are two distinct projective zero lines. In a chart with unit leading coefficient, their simple roots lift uniquely to every power of p by the elementary simple-root lifting criterion. If q(T)=A'T^2+B'T+C', a root t0 satisfies q'(t0)!=0 modulo p, because q and its derivative have no common root when the discriminant is a unit. Near a lifted root xi, v_p(q(t))=v_p(t-xi). A different chart is required when the chosen leading coefficient is not a unit; the projective statement is unchanged.

Primes dividing the discriminant are not included in that simple-root assertion. For odd such primes the primitive form reduces to rank one, and its repeated root can have different lifting behavior. The prime 2 is also treated separately by direct congruences. The identity

    4A' q(T)=(2A'T+B')^2-Disc(Q)

is valid at every prime, but converting it to a valuation equality must retain v_p(4A'). No generic anisotropy or simple lifting claim is made at these primes.

## 4. Simultaneous divisibility has a resultant cap

Because y,z are primitive, if p divides y then z is a unit. Equation (5) gives

    Q(w)=Rresultant z^2 modulo y.

Thus at EVERY prime, including discriminant primes and 2,

    min(v_p(Q(w)),v_p(y))<=v_p(Rresultant).                 (6)

This follows by reducing modulo the smaller prime power on the left; z is a unit whenever that power is positive. If s=v_p(y)>r_p=v_p(Rresultant), then more precisely

    v_p(Q(w))=r_p.                                        (7)

Indeed A'y^2+B'yz has valuation at least s, whereas Rresultant z^2 has valuation r_p.

Consequently the Gram form cannot provide arbitrarily deep additional denominator valuation at the same time as the primitive sum-row coordinate becomes arbitrarily divisible, unless the actual resultant has the requisite depth. Equation (6) is stronger than a statement about prime support and is applicable without any split assumption.

At a good split prime dividing Rresultant, the root lying on y=0 modulo p is the only root compatible with p|y. It is simple: when C'=0 modulo p and the discriminant is a unit, B' is a unit. At a nonsplit prime Rresultant is necessarily a unit, because (-H1,H0) is primitive. These statements link the prime classification to the actual cancellation direction.

## 5. A smaller primitive congruence at regular row primes

Call a prime regular for this row reduction if p does not divide c_H b. This is an explicit condition on the actual primitive rows; b can vanish as an integer, in which case this regular set is empty and the general formulas (1),(2) still apply.

If p divides delta_F at a regular row prime, equation (1) forces p|y. To justify this without overlooking h0, v_p(Wcancel)>0 implies v_p(y)>h>=0 since c_H is a unit. Then z is a unit and a y+b z is a unit. Therefore

    v_p(h0)=0.

Every positive-depth cancellation at such a prime reduces to the single primitive coordinate t=y/z in Z_p. Exactly,

    v_p(delta_F)
      =min(f,v_p(t),max(0,f+A0+v_p(q(t))-E0))               (8)

whenever p|y. If y is a unit the exponent is zero. The use of t is legitimate because z is a unit, and Q(w)=z^2q(t).

At regular row primes not dividing Rresultant, equations (7),(8) simplify further:

    v_p(delta_F)=min(f,v_p(y),max(0,f+A0-E0)).              (9)

Thus p^k divides delta_F, for k>=1 at such a prime, if and only if

    k<=f,
    f+A0-E0>=k,
    H0 w0+H1 w1=0 modulo p^k.                            (10)

This is a primitive linear congruence, with no quadratic evaluation left to compute and no final evaluated gcd left implicit. It is valid at nonsplit primes as well as at split primes for which Rresultant is a unit. It does not assert that the actual response satisfies the congruence.

More generally, at a regular row prime let r_p=v_p(Rresultant). If k>r_p, then p^k divides delta_F if and only if

    k<=f,
    f+A0+r_p-E0>=k,
    y=0 modulo p^k.                                      (11)

Indeed v_p(y)>=k implies (7). For the finite shallow range k<=r_p the exact polynomial q(t) and (8) retain the required information. This separates shallow local root behavior from deeper cancellation without scanning primes.

## 6. Required precision at the remaining primes

The preceding simplification deliberately excludes primes dividing c_H b. At these primes no automatic claim h0=1 locally is valid. Formula (2) remains exact and uses only the transformed quadratic, one primitive coordinate pair, and the two row coefficients.

For arbitrary p, after determining h=v_p(h0), the condition p^k|delta_F is exactly

    k<=f,
    d1>=h+k,
    c_H y=0 modulo p^(h+k).                              (12)

In the original integer numerator this last test is

    (uhat+vhat)w=0 modulo p^(v_p(shat)+h+k).              (13)

The extra precision from shat and h0 cannot be suppressed. Determining h itself requires the capped valuations of a y+b z and c_H y through d1. To determine the complete local exponent, computing these valuations and v_p(Q(w)) up to their relevant caps suffices; if a cap is reached, exact higher valuations are unnecessary.

For good split primes the simple-root description in Section 3 specifies how the quadratic valuation is lifted. At discriminant primes and 2, use the exact polynomial identity and capped congruences without assuming simple roots. No universal small bound for their contribution has been proved. Likewise no subfactorial bound for the product of primes dividing c_H b Disc(Q) Rresultant is asserted: these are per-index canonical integers, not fixed exceptional primes.

## 7. Structural obstruction to obtaining a bound from anisotropy alone

Equation (9) shows why excluding Gram-form zeros does not remove the factorial deficit. Even when Q(w) is a unit, the denominator Dtilde already contains F. If A0>=E0 at a regular prime, (9) becomes

    v_p(delta_F)=min(f,v_p(y)).

Hence nonsplitness supplies no upper bound on the depth of the remaining primitive linear congruence y=0. In the transformed local lattice, pairs with z a unit and y divisible by p^f are compatible with a unit value of Q whenever Rresultant is a unit. Their geometric constraints therefore permit the entire factorial depth.

This last observation is a limitation of the local geometry argument. It is NOT an example from the canonical recurrence and does NOT prove that the canonical response attains full depth. For the actual selector, the unresolved arithmetic is the valuation of H0 P_n+H1 P_(n+1) after division by t0, with H itself formed from both canonical companion rows. A canonical recurrence or an estimate for this particular primitive congruence is still needed to exclude the permitted deep cancellation.

The result therefore supplies a smaller exact target beyond the defining gcd: at regular primes outside the resultant it is precisely (10), and above the resultant depth it is (11). The quadratic can no longer be invoked as an independent source of unlimited extra valuation there.

## 8. Finite stage outcome and provenance

The proved author results of this task are the unimodular two-coordinate elimination (1),(2), the actual discriminant formulas (3),(4), the valuation cap (6),(7), and the primitive congruence criteria (10),(11), with full lifting precision (12),(13). They apply to the retained canonical data; no coordinate-center result is transferred.

No parameter-uniform estimate log(delta_F)=o(n log n) has been obtained. The unresolved sum is the weighted sum of the local depths in (2), or their simplified values (9) at regular primes. The external factorial factor survives even when the quadratic is nonsplit, so positivity and anisotropy alone cannot settle this sum.

The earlier exceptional factorization delta_exc=delta_reg delta_res and its O(n) bound for log(delta_reg) remain preserved, with their unresolved residual condition. Neither factor of the total deficit is now known to be subfactorial. No application of the 5/72 overlap threshold follows, and the actual e+pi problem remains OPEN.

Provenance: the definitions and normalization are from Child 3's saved CANONICAL_OVERLAP_DEFICIT.md and CANONICAL_EXCEPTIONAL_DEFICIT_CONTENT.md, whose saves and full readbacks are present in the supplied transcript. The local elimination in this note is a new bounded completion of the accepted current task. It uses no computation receipt or independent verdict. Earlier completed seed and modulo-121 work was neither rerun nor re-audited. The present paper and report supply the coherent handoff for these deductions, subject to their forthcoming actual save/readback receipts.

One textual clarification to the preserved exceptional paper: its justification of k_C|Delta uses LEFT multiplication M(adj(M)Drow)=Delta Drow. A sentence there describes multiplication by M without the correct side. The asserted divisibility and its subsequent use agree with this left-multiplication identity; the original file is preserved. This is an attributed wording amendment, not a renewed audit.

File index for this closeout: CANONICAL_FACTORIAL_DEFICIT_LOCAL_GEOMETRY.md is this paper; CANONICAL_FACTORIAL_DEFICIT_LOCAL_GEOMETRY_REPORT.md is its concise handoff. The two preceding papers and their corresponding _REPORT.md files retain the definitions, factorization and prior provenance. Original evidence remains at its existing paths. This current stage is closed mathematically with the stated gap; after saving and reading back these two files, Child 3 will stop without another task.
