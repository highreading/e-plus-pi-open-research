> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the exact dual endpoint error integrals

Date: 2026-09-13. Reviewer: audit_results.

Target: raw_dual_endpoint_error_integrals.md by audit_computations.
Status: PASS for every mathematical assertion, with one requested scope clarification in the prose following (18). No new degree construction or index scan was performed.

The proof is for the actual primitive cofactor vector and its existing endpoint family. Its two signed integrals and its absolute-mass lower bound are new exact descriptions of that family; they do not settle the primitive shrinking problem.

## 1. Dependencies and normalization

I checked the target against the reviewed primitive dual polynomial/content identity and the actual endpoint integral numerator theorem. For n>=1 the vector w is primitive, W=t^n(t-1)^n V, and monic integer factorization gives V integral and primitive. The identities

    T(t)=sum_r (n+r)! w_(n+r)t^r,
    Qhat(z)=z^(2n)T(1/z)/n!,
    Borel(T)=D^n W,
    L(t^s T)=0 (s<n)

have the stated factorial conventions. Qhat, its two numerator polynomials Pe,Pa, and the endpoint Z are the previous objects. In particular Z is a nonzero integer. No new normalization of U, V, or Z is implicit.

## 2. Complete exponential error

For the term indexed by k, the Taylor truncation of e^z ends at k-n because the accompanying power of z is 3n-k. Its integral Taylor remainder therefore contributes z^(2n+1) times the corresponding coefficient of Borel(T), divided by n!. This proves the preliminary identity before (4) for the whole error.

Every derivative of W below order n vanishes at both 0 and 1. Each integration by parts replaces the derivative on W by minus the derivative of e^{z(1-t)}, producing a factor +z. There is no residual sign or boundary term. Thus (4) is an entire identity with factor z^(3n+1)/n!. The sign in (5) comes solely from (t-1)^n.

The beta integral is n!^2/(2n+1)!, so its division by n! gives exactly the coefficient e n!/(2n+1)! in (6). No bound for the actual norm of V is supplied or presumed.

## 3. Existence, uniqueness and arithmetic of U

The n-fold antiderivative based at -i has its first n jets zero there. Its j-th derivative at i, for j<n, is an integral of T times (i-t)^(n-1-j), a polynomial of degree at most n-1. All these integrals vanish by the actual orthogonality. Two such antiderivatives differ by a polynomial of degree below n with a zero of order n; hence they are equal.

Conjugation swaps the two endpoint conditions and preserves T, so uniqueness proves reality. Degree at most 3n and both order-n factors give S=(1+t^2)^n U, with degree U<=n. T is nonzero, hence U is nonzero.

For S0=sum_r r! w_(n+r)t^(n+r), differentiation n times gives T. Thus S-S0 has degree below n. Integer division of S0 by the monic polynomial (1+t^2)^n has an integer quotient and remainder of degree below 2n. Comparison with S shows that the quotient is exactly U and the remainder actually has degree below n. This establishes integrality without assuming that the complex endpoint conditions themselves form an integral linear system.

Expanding at infinity,

    (1+t^2)^(-n)=t^(-2n) sum_h (-1)^h binom(n+h-1,h)t^(-2h),

gives precisely (8): the coefficient index in w is 2n+j+2h and the factorial is (n+j+2h)!. Consequently every u_j is divisible by (n+j)!, including zero coefficients. Neither exact degree n nor primitivity of U/n! is needed.

## 4. Arctangent error and contour orientation

The identity atan(z)=z L((1-zt)^(-1)) with L=(2i)^(-1) integral from -i to i gives (10), including z^(2n+1)/n!. It holds near zero and analytically continues along the real segment to 1; that path introduces no pole in the t contour.

Using T=D^n S, the n integrations by parts give (-1)^n. The nth derivative of (1-zt)^(-1) is n!z^n(1-zt)^(-n-1), which cancels the displayed n! in (10). All boundary terms vanish by the first n endpoint jets of S. This proves the factor and sign in (11).

At z=1 the only pole is t=1. The region between the segment -i to i and the left circular arc excludes this pole. At phi=pi/4, t=1-sqrt(2)e^(i phi)=-i; at phi=-pi/4 it is i. Thus the prescribed decreasing-phi orientation is correct. The identities

    (1+t^2)/(1-t)=2sqrt(2)cos(phi)-2,
    dt/(1-t)=-i dphi

give a positive factor 1/2 after the phi limits are reversed and the factor (2i)^(-1) is applied. This verifies (12). Real coefficients of U and t(-phi)=conjugate(t(phi)) justify replacement by the real part.

The arc obeys |t|^2=3-2sqrt(2)cos(phi)<=1. On the arc, double integration of cos(phi)>=cos(pi/4) gives 1-cos(phi)>=sqrt(2)phi^2/4. Hence F<=rho-phi^2<=rho exp(-phi^2/rho), with rho=2(sqrt(2)-1). Extending the Gaussian integral to the real line proves (13) with its exact factor 1/2. This is a full-error estimate, not an estimate for only the first nonzero Taylor coefficient.

## 5. Norm bound and absolute-mass lower bound

The coefficient norm of W is at most 2^n H_V. In (8), n+j+2h<=2n. For any fixed h, summing the selected w coefficients over j costs at most the full coefficient norm of W, not an extra factor n. The hockey-stick sum is binom(n+floor(n/2),floor(n/2))<=4^n. Therefore (14), with (2n)!8^n H_V, is a valid deliberately loose bound.

Let d=degree U. Its leading coefficient has magnitude at least (n+d)! by the proved divisibility. For d>=1, only the leading U term supplies the highest harmonic cos(d phi); its magnitude as a polynomial in x=cos(phi) is |u_d| 2^(3d/2-1). Lower U terms cannot cancel it. For d=0 the real polynomial is a nonzero constant.

On [c,1], the shifted ordinary Legendre polynomial of degree d has supremum at most one, leading coefficient binom(2d,d)/ell^d, and squared norm ell/(2d+1). Testing p against it removes all lower coefficients and proves (16), with absolute values valid for either sign of the leading coefficient. Using binom(2d,d)<=4^d, d<=n, and 0<ell/sqrt(2)<1 proves (17). The constant-polynomial case satisfies the same weaker bound.

On the inner arc |phi|<=pi/8, F>=rho0. Both halves of the arc contribute, and |dphi|=dx/sqrt(1-x^2)>=dx. This supplies the factor 2 that changes the denominator in (17) into the one in (18). The result is the exact factorial absolute-mass lower bound

    A_n >= n! ell/(2n+1) (rho0 ell/sqrt(2))^n,

and therefore log A_n>=n log n-O(n).

This is not a lower bound for the signed arctangent error. I requested that the sentence “A signed-cancellation factor is indispensable” be explicitly restricted to obtaining a small UNREDUCED arctangent error from this arc representation. The already stated large-gcd alternative and the primitive ledger below are essential: a large endpoint gcd could make the primitive integer form small without a small unreduced error. This is a prose clarification, not a defect in (18).

## 6. Combined form and primitive arithmetic

Because Pe,Pa are integral and Z!=0, N=Pe(1)+4Pa(1) is an integer and

    Lambda=Z(e+pi)-N=Re(1)+4Ra(1).

The factor 4 multiplying the arctangent error gives the coefficient 2 in its arc contribution in (19). The common (-1)^n sign is correct. Separate irrationality of e and pi proves nonzero separate errors, but does not prove nonzero sum; the note does not make that inference.

The previously reviewed cross-product identity gives A_canonical(1)=-N/Z. Therefore, for g=gcd(|N|,|Z|) and q=|Z|/g,

    q((e+pi)-N/Z)=sign(Z) Lambda/g.

This proves (20) with its exact sign and shows that the representation produces the same primitive endpoint form. Primitivity of w or V does not remove g. Applying (6) and four times (13), and using ||V||<=H_V, yields exactly (21).

The earlier strict distinctness of the endpoint rational approximants implies that at most one Lambda vanishes. No all-index sign theorem is required here, and no new one is claimed. Neither the large absolute mass nor the displayed crude upper bound proves nondecay of the primitive form.

## 7. Independent finite normalization checks and conclusion

I read the author's exact output restricted to the already archived n=1,2 cofactor vectors and independently checked its normalizations. For n=1, w=(-2,3,-1), V=2-t and U=3-2t. In the arc formula, F Re U=8cos^2(phi)-2sqrt(2)cos(phi)-2; its integral is pi, so the prefactor gives Ra(1)=-pi/2, agreeing with the complete Taylor error. For n=2, the recorded U=-118-972t+1176t^2 has coefficient divisibility by 2!,3!,4!, and the recorded complete errors agree with the already reviewed Qhat,Pe,Pa and endpoint values. These are controls of conventions only; the proof above is all-index.

The target passes. The exact Rodrigues polynomial, coefficientwise factorial divisibility and circular-arc mass theorem are usable additions. The remaining task is a signed-integral estimate combined with the actual endpoint gcd, or another argument controlling their product. No rationality or irrationality conclusion follows from this note.

