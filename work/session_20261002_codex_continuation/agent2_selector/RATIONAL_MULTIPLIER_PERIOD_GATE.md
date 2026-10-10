> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Rational multiplier with exact elimination of extra periods

2026-10-02. Original author research under the parent's fresh rational-multiplier steering. The quartic exclusion is preserved. This note identifies a period-compatible rational class and the exact missing exponential normalization, rather than treating a new contour integral as automatically approximating e+pi.

## Search and overlap ledger

Archive search covered rational selector/multiplier, additional poles/periods, poles at w=1 or t=0, and arctan(1/3) in the preceding sessions. The archived "rational saddle selector" was read in `agent2/RATIONAL_SADDLE_SELECTOR_WORKING.md`; despite the name, its selector L is an integer polynomial, so it does not cover rational denominators in w. Existing companion transfer notes require retention of the actual rational correction and shared coefficient. No present period-compatible two-pole rational multiplier was located by this bounded search.

Primary paper search included rational integral residues/logarithms, rational approximation of pi, and Hermite reduction. Opened full texts:

- Bostan, Chyzak, Lairez, Salvy, *Generalized Hermite Reduction, Creative Telescoping and Definite Integration of D-Finite Functions*, https://arxiv.org/pdf/1805.03445, Introduction and Sections 3.1–3.2. Classical reduction modulo derivatives and residue obstructions are credited overlap.
- Lairez, *Computing periods of rational integrals*, https://arxiv.org/pdf/1404.5069. The period/creative-telescoping setting is overlap, not a claim that a general rational multiplier preserves the old two constants.

The new obligations below are the exact endpoint log ratios on this contour, their compatible pole classification, the paired e/pi residue functionals, and a rational projection matching the two target coefficients. No denominator rate or nonvanishing claim is inferred from reduction alone.

## 1. Compatible real rational poles

Let a=(1+i)/2 and C be the upward vertical path from bar(a) to a. For a real rational c off C, the exponential of the logarithmic increment is

    ρ_c=(a−c)/(bar(a)−c)∈Q(i), |ρ_c|=1.

If that increment is a rational multiple of i*pi then ρ_c is a root of unity in Q(i), hence belongs to {1,−1,i,−i}. For finite c, ρ_c=1 is impossible. The value −1 requires c=1/2, a pole on C and thus excluded. The remaining two values give c=0 and c=1. Conversely, along the prescribed continuous branches,

    ∫_C dw/w = i*pi/2,
    ∫_C dw/(w−1) = −i*pi/2.                         (1)

This is a classification of individual real rational simple-pole periods compatible with rational multiples of pi. It does not rule out deliberate cancellation between several other periods, nor more general algebraic poles. Such cancellation must be proved before claiming a target consisting only of e+pi.

In particular every F∈Q(w) with poles only at 0 and 1 has the exact Hermite reduction

    F=P'(w)+r0/w+r1/(w−1), P∈Q(w),
    ∫_C F=2i Im P(a)+i*pi*(r0−r1)/2.               (2)

The rational part Im P(a) is rational because P has real rational coefficients and Gaussian rational arguments. All higher pole depths contribute to P and introduce no additional period. Thus no uncontrolled constants arise in this two-pole class.

## 2. Exact same-kernel e and pi components

Write the partial fractions of F as

    F=p(w)+Σ_(j=1)^s a_(0,j)w^(−j)
              +Σ_(j=1)^t a_(1,j)(w−1)^(−j).

Define the rational functionals

    R(F)=a_(0,1)−a_(1,1),
    E0(F)=Σ_(j=1)^s a_(0,j)/(j−1)!,
    E1(F)=Σ_(j=1)^t a_(1,j)/(j−1)!.

A positively oriented closed contour Γ around both poles gives EXACTLY

    (1/(2*pi*i))∮_Γ exp(w)F(w)dw = E0(F)+e E1(F). (3)

This uses the finite principal parts, not an omitted series. Polynomial p has zero closed-contour integral against exp(w). If E1 and R are nonzero, then

    α(F)=−E0(F)/E1(F), β(F)=−4 Im P(a)/R(F)

are rational approximants to e and pi with COMPLETE errors (3)/E1 and −2i∫_C F/R. Their sum has coefficient one for e+pi, but generally two different endpoint denominators. A raw rational multiplier does not preserve the archived shared U.

The stronger shared-coefficient condition is

    E1(F)=R(F)=U≠0.                                (4)

Under it the rational center is

    c(F)=[−E0(F)−4 Im P(a)]/U,
    e+pi−c(F)= [ (1/(2*pi*i))∮_Γ exp(w)F dw
                         −2i∫_C F dw ]/U.           (5)

Both full integrals, their signs, and the same U appear explicitly.

## 3. Rational two-row matching projection

Take two rational kernels F0,F1 in this class and put Li=E1(Fi)−R(Fi). The new rational kernel

    F=L1 F0−L0 F1

automatically satisfies E1(F)=R(F). Its actual shared response is the determinant

    U=E1(F1)R(F0)−E1(F0)R(F1).                      (6)

If U=0 the projection does not define the desired center. If U≠0, (5) is exact. This is a linear algebra identity, not a new nonzero theorem. Extra periods are already absent before this projection; the remaining research problems are the actual determinant, complete contour bounds, and its primitive arithmetic.

## 4. A degree-at-infinity reduction and its arithmetic cost

One concrete candidate, with n=4k and h≥1, is

    F0(w)=(2V(w))^n G(w)^h/[w^(n+1)(1−w)^(4h)],
    F1(w)=w F0(w),
    V=w²−w+1/2, G=(1−2w²)(1+4w^4).

Both retain zeros at a and bar(a) of order n+h. Their finite poles are exactly 0 (order n+1) and 1 (order 4h), with integer principal-part coefficients. The degree of F0 at infinity is n+2h−1, in place of n+6h−1 for the polynomial quartic kernel. Thus this rational denominator changes the degree cost and preserves only the pi period. It also changes the e residue response and cannot be inserted into the old α formula.

Let T=(4h−1)! and form integer projection coefficients

    mi=T[ E1(Fi)−R(Fi) ],
    F=m1F0−m0F1.

They are integers because the principal parts are integral and E1 denominators divide T. Its matched U=R(F) is therefore an integer. Pole orders remain s=n+1,t=4h and the degree at infinity is at most D=n+2h.

For integral principal parts and polynomial part, choose

    L=lcm(1,...,max(s−1,t−1,D+1)),
    Q=2^(D+1)L n!.

The rational antiderivative P uses only divisors at most max(s−1,t−1,D+1). Its negative powers at a and a−1 are Gaussian INTEGERS, since a^(−1)=1−i and (a−1)^(−1)=−1−i. Only the polynomial primitive needs powers of two, bounded by 2^(D+1). Consequently

    Q E0(F)∈Z, Q·4 Im P(a)∈Z.

The EXACT final reduced denominator of (5), if U≠0, is

    q=Q|U| / gcd(Q U, Q E0(F)+Q·4 Im P(a)).          (7)

This formula includes the new factorial projection coefficients and all cancellation in the complete rational numerator. Q is merely a justified common integer multiplier; (7), not Q or U alone, is the actual denominator. At h~κ n log n the explicit odd-lcm length is roughly 4h rather than the preceding N~6h, but the projection determinant can itself contain factorial-scale size/content. No favorable primitive rate is claimed without estimating (7).

This candidate passes the extra-period gate. Its matched-response determinant and complete error remain open; the next calculation may investigate those exact quantities. The generic reduction/projection is classical in method, and no novelty for Hermite reduction is claimed.

## 5. A tempting derivative matching is exactly center-invariant

There is a simpler matching identity, but it cannot supply an arithmetic gain. Suppose F(a)=F(bar(a))=0 and A=E1(F), R=R(F) are both nonzero. Derivatives have zero ordinary residues, while integration by parts around each exponential residue gives

    R(F')=0, E0(F')=−E0(F), E1(F')=−E1(F).

Hence

    H=A F+(A−R)F'

satisfies E1(H)=R(H)=AR, without any determinant nonzero condition. Its Hermite rational primitive is A P+(A−R)F, whose endpoint imaginary part is A Im P(a) because the endpoints of F vanish. Its exponential numerator is E0(H)=R E0(F). Consequently

    α(H)=α(F), β(H)=β(F), c(H)=c(F), den(c(H))=den(c(F)).

This matching creates a shared written coefficient but preserves the EXACT rational center and its reduced denominator. It must not be credited as a denominator improvement. To change the center one needs a different kernel direction, such as the wF direction in Section 3, and must then estimate its actual determinant and final gcd. The derivative identity is an original specialization of classical integration by parts, not an audit or an external no-go claim.
