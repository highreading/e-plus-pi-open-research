> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# All integer selector exponents and the half-step weighted certificate

2026-10-02. Parent-authorized distinct research target after the fixed-kernel identity. Allow the underlying exponent h=2m to be any nonnegative integer, including odd h, and take the actual weighted finite difference in h. The intended benefits are a lower-degree polynomial certificate, the exact >1 root mesh in h, and a possibly simpler three-state output determinant. All center errors and reduced denominators must be retained. No O(1)-shift theorem is claimed yet.

## Search and overlap ledger before this target

Archive search: `half.step`, `half step`, `odd.selector`, `odd selector`, `selector.*odd`, `h=2m`, and `2m.*odd` over the preceding session and sources. Hits concerning "odd arithmetic" mean odd primes rather than odd selector exponents. The exact original center/exponential formulas were read in `LARGE_SELECTOR_DYADIC_DENOMINATOR_DRAFT.md` and `LARGE_SELECTOR_EXPONENTIAL_REMAINDER_DRAFT.md`; they supply the identities below and reveal where the even-exponent dyadic argument does not transfer. No present half-step certificate was located by this bounded search.

Online primary-paper searches included "finite difference Jensen polynomials real rooted mesh falling factorial binomial shift", "mesh preserving discrete multiplier sequences Jensen polynomial positive roots finite differences", "discrete multiplier sequences mesh polynomials arxiv", and "Connecting the q-Multiplicative Convolution and the Finite Difference Convolution arxiv".

Opened primary papers:

- Petter Brändén, Ilia Krasikov, Boris Shapiro, *Elements of Pólya–Schur theory in the finite difference setting*, https://arxiv.org/pdf/1204.2963 and the published full text https://staff.math.su.se/shapiro/Articles/FiniteDifference.pdf.
- Jonathan Leake, Nick Ryder, *Connecting the q-Multiplicative Convolution and the Finite Difference Convolution*, https://arxiv.org/pdf/1712.02499. Its mesh-preserving convolution theorem requires its precise convolution; it does not state that every binomial transform of shifted samples is real-rooted.
- The opened primary Fisk falling-factorial transform source from `ACTUAL_U_ROOT_GEOMETRY.md` remains the classical overlap behind the exact selector mesh.

New obligation: the actual odd-exponent forcing sign, half-step certificate, degree/lattice and full errors are derived here. Generic discrete-root-preserving methods are classical and are not claimed novel. No binomial/Jensen real-rootedness conclusion is inferred solely from the >1 selector mesh.

## 1. Actual rational centers for odd as well as even h

Let n=4k, r=n/2, h≥0 an integer, and put

    B_h(t)=(1−2t+2t²)^n(1−4t+2t²)^h=Σ_(j=0)^N b_jt^j,
    N=2n+2h, J=N−n=n+2h,
    K_h(t)=t^n B_h^(n)(t)/n!,
    U_h=K_h(1),
    T_h=calL((K_h−U_h)/(t−1)).

Define the polynomial

    u_n(h)=[x^n](1+2x+2x²)^n(1−2x²)^h
          =Σ_(ell=0)^r (-2)^ell binom(h,ell)a_(n−2ell).

The actual endpoint forcing is

    U_h=(-1)^h u_n(h),                              (1)

because the second quadratic at t=1+x is −1+2x². The sign in (1) is essential. The polynomial u has degree r and leading coefficient 2^r/r!, since r is even, and has r positive simple roots with gaps >1 by the proved actual-U root theorem after h=2m. For every integer h, 2^r divides U_h. Individual U_h zeros are retained.

When U_h≠0 the exact rational center is

    α_h=U_h^(-1)Σ_(j=n)^N binom(j,n)b_j E_j,
    E_j=Σ_(a=0)^j 1/a!,
    β_h=T_h/U_h,
    c_h=α_h+β_h.

These formulas define the actual complete components and do not need B_h nonnegative on a real interval. The complete exponential error obeys, with Λ_h=2n+4h,

    0<|e−α_h|
       <3Λ_h^n exp(Λ_h/(n+1))/[(n+1)(n!)²|U_h|].   (2)

Indeed B_h(−t) has nonnegative coefficients for every integer h, so |b_j|≤Λ_h^j/j! by the same coefficientwise exponential majorization. The exact sum of all exponential tails then gives (2), and rationality of α with irrationality of e supplies strict nonzero error. No positivity of the odd selector itself is required.

All-degree coefficient divisibility gives v_2(b_j)≥ceil(j/2), and the saved moment formula gives v_2(T_h)≥1. Hence, for every nonzero U_h,

    den(β_h) divides O_N |U_h|/2,                  (3)

where O_N is the odd lcm through N. This is an actual reduced-component denominator upper bound, without a congruence allocation.

The previous exact dyadic formula for the final reduced center cannot simply be transferred to odd h. Then J=n+2h is 2 modulo 4, and the old lower bound on v_2((J)_ell) already fails at ell=2: its valuation is 1, rather than the asserted lower bound 2. The final center denominator will instead be constrained by (2), (3), and the irrationality-measure bound for e, unless a separate exact odd-h valuation theorem is proved.

## 2. Half-step certificate and lower-degree lattice

Set d=n+1 and form the actual entirely rational certificate

    W̆(n,h)=Δ_h^d(U_h T_h).

Since U_h²=u_n(h)² has degree n,

    W̆(n,h)=Σ_(j=0)^d(-1)^(d−j)binom(d,j)
                 U_(h+j)(T_(h+j)−πU_(h+j)).       (4)

The exact full-contour identity remains

    T_h−πU_h=i2^(n+1)∫_C V(w)^n q(w)^h/w^(n+1)dw,
    q(w)=2w²−1.

Define z(w)=−q(w)=1−2w² and

    P̆_(n,h)(z)=Σ_(j=0)^d(-1)^(d−j)binom(d,j)u_n(h+j)z^j
               =(z−1)^(r+1)Q̆_(n,h)(z),
    Q̆_(n,h)∈Z[z], deg Q̆≤r.

The factor follows from the same degree argument used in the archived certificate and does not divide by a forcing value. Inserting the actual sign (1) into (4) gives

    W̆(n,h)=i2^(n+1)(−2)^(r+1)
          ∫_C w V(w)^n z(w)^h Q̆_(n,h)(z(w))dw.    (5)

Its integrand is a polynomial of degree at most 3n+2h+1. The relevant primitive degree is

    L̆=3n+2h+2,                                   (6)

instead of the original even-step value 5n+2h+4. Rational Gaussian endpoint evaluation proves that the odd part of the denominator of W̆ divides O_L̆. Every summand U T has dyadic valuation ≥r+1, including zero summands. Thus

    O_L̆ W̆(n,h)∈2^(r+1)Z,
    W̆(n,h)≠0 ⇒ |W̆(n,h)|≥2^(r+1)/O_L̆.           (7)

If A_h=max_(0≤j≤d)|U_(h+j)|, then A_h>0 and a nonzero certificate yields some actual nonzero-forcing node s in [h,h+d] with

    |β_s−π|≥1/[2^r O_L̆ A_h²].                    (8)

Combining (8) with the full exponential bound at that very same s is necessary before making any complete-error conclusion. No witness is selected from a different family.

## 3. Relation to the completed fixed-kernel identity

The adjoint density is the same κ_n(t) as in `ACTUAL_W_FIXED_KERNEL_IDENTITY.md`, but the step-one h difference contributes (1−t)^(n+1) rather than (1−t²)^(n+1). Consequently the exact fixed kernel is

    P̆_n(w)=P_n(w)/[2(1−w²)]^(n+1)
           =−2^(−n−1) w V(w)^r R_n(w),            (9)
    W̆(n,h)=i2^(n+1)∫_C z(w)^h P̆_n(w)dw.         (10)

The quotient in (9) is a polynomial, of degree exactly 3n+1, by the proved old fixed-kernel factorization and odd n+1. The exact nonzero R_n(a) and R_n(bar a) factors carry over. This is an exact identity for the actual odd/even selector family, not an assumption that the positive period output is the actual W̆ value.

The corresponding complete-period output is also strictly positive: the same proof gives the convergent positive integral with t^h(1−t)^(n+1)κ_n^positive(t) instead of t^(2m)(1−t²)^(n+1)κ_n^positive(t). The two remaining endpoint modes must still be controlled.

Outstanding: derive the exact three-state output determinant for z^h, assess its singularities uniformly, establish bounded-shift or controlled block nonvanishing, and then quantify (8) with the actual reduced q and all errors. No old even-h dyadic equality is being carried over to odd h.
