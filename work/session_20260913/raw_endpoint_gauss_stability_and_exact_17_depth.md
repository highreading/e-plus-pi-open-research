> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Gauss stability of the actual endpoint gate and an exact infinite 17-adic depth

Date: 2026-09-13. Original root continuation.
Independent review passed: raw_endpoint_gauss_stability_independent_review.md.

The new endpoint restriction reduces saturated degrees n=mp^nu to
a fixed-prime constant-term sequence. This note proves a stability
criterion at every odd prime and settles the previously open extra
17-adic depth on the infinite family n=4·17^nu, nu≥2:

    v_17(d_n^II)=1,
    v_17(Z_n)=(n−4)/16+1.                                (1)

The proof uses one predeclared exact coefficient modulo 17², followed
by an all-index congruence. It does not infer an infinite assertion
from a numerical trend, and does not identify the simultaneous
denominator d_n^II with the selected type-I denominator.

## 1. An integer constant-term form for the Legendre gate

Let Q_n be the actual monic imaginary-segment Legendre polynomial.
Define the positive integer

    A_n = sum_(j=0)^floor(n/2)
              binom(n,2j) binom(2j,j) 2^(n−j).           (2)

Then exactly

    A_n = binom(2n,n) Q_n(1)
        = CT_z [2+sqrt(2)(z+z^(-1))]^n.                (3)

For completeness, the ordinary Legendre generating identity gives
P_n(x)=CT[x+(sqrt(x²−1)/2)(z+z^(-1))]^n. It also follows by
expanding the constant term: its generating function is
(1−2xt+t²)^(-1/2), using sum binom(2j,j)v^j=(1−4v)^(-1/2).
Since Q_n(t)=i^n P_n(t/i)/kappa_n with
kappa_n=2^(−n)binom(2n,n), substitution t=1 yields (3).
The sign of the square root is irrelevant to the constant term.
Expanding the last expression in (3) gives (2), so its integrality
does not require an algebraic-number convention.

## 2. Exact Gauss congruences, including the nonsplit case

For every odd prime p, every integer m≥0 and every r≥1,

    A_(mp^r) ≡ A_(mp^(r−1))  (mod p^r).                 (4)

Work in the free quadratic Z_p-algebra R=Z_p[t]/(t²−2), and let
chi=(2/p)∈{−1,1}. The automorphism sigma(t)=chi·t fixes Z_p.
Modulo p it is the Frobenius: t^p=2^((p−1)/2)t≡chi t, and
every coefficient from Z_p has its usual Frobenius residue. Thus
for f(z)=2+t(z+z^(-1)),

    f(z)^p ≡ sigma(f(z^p))  (mod p).

In any commutative Z_p-algebra, if U≡V modulo p^s with s≥1,
the binomial theorem gives U^p≡V^p modulo p^(s+1).
Iteration, followed by the integer m-th power, therefore gives

    f(z)^(mp^r) ≡ sigma(f(z^p))^(mp^(r−1)) (mod p^r).

Taking constant terms removes the substitution z→z^p. The other
constant term is sigma(A_(mp^(r−1))), equal to that ordinary integer.
Since R is free over Z_p, divisibility by p^r of the resulting
integer in R is the same divisibility in Z_p. This proves (4),
whether 2 is a square or a nonsquare modulo p.

These are classical Gauss-type congruences. For context and terminology,
see Beukers–Houben–Straub, Section 1 and its Frobenius-lift framework:
https://arxiv.org/pdf/1710.00423.
Mellit–Vlasenko study stronger constant-term Dwork congruences under
Newton-polytope hypotheses: https://arxiv.org/pdf/1306.5811.
The elementary proof above is sufficient here; no stronger congruence
or nonvanishing theorem is imported from either paper.

## 3. A p-adic limit and finite stability certificates

For fixed m and odd p, (4) proves existence of

    A_(m,p)^infty = lim_(nu→infty) A_(mp^nu) in Z_p,

with the exact error divisibility

    A_(m,p)^infty − A_(mp^nu) ∈ p^(nu+1) Z_p.            (5)

The infinite sum of successive differences converges; every term
after index nu is divisible by p^(nu+1), which proves (5).

If at any r_0≥0 an exact finite calculation proves

    e=v_p(A_(mp^r_0)) ≤ r_0,

then (5) forces v_p(A_(m,p)^infty)=e. Every subsequent coefficient
A_(mp^nu), nu≥r_0, has the same valuation e. Thus a single sufficiently
precise certificate can prove an eventual exact depth. The existence
of such a certificate is not assumed for all (m,p).

If the limit is zero, (5) instead gives

    v_p(A_(mp^nu))≥nu+1 for every nu≥0.                  (6)

Real positivity of A_n does not exclude this p-adic possibility.
No general nonvanishing claim for the limit is proved here.

## 4. Transfer to the actual endpoint determinant

Now assume 1≤m, 3m<p and n=mp^nu with nu≥1. Use K_n, Theta_n, h_n,
Z_n and d_n^II from `raw_endpoint_scalar_cauchy_restriction.md`.
That independently reviewed theorem proves

    Theta_n,h_n are p-adic units,
    d_n^II=|K_n|/Theta_n,
    v_p(Z_n)=(n−m)/(p−1)+v_p(K_n),

and the exact congruence

    K_n ≡ L_(3n)^n (prod_(j=0)^(n−1)|h_j^Leg|)
                                  Q_n(1)  (mod p^nu).  (7)

The prefactor in (7) is a p-adic unit. Indeed it is exactly the
determinant of the first n Cauchy rows after its column-reversal
sign is accounted for; those rows are invertible modulo p by the
saturated block theorem. This is a statement about their full
product, not an assertion that each Legendre norm is a unit.

Also binom(2n,n) is a p-adic unit: because 2m<p, Legendre's formula
gives v_p((2n)!)=2v_p(n!). Thus (3),(7) give

    K_n ≡ U_n A_(mp^nu)  (mod p^nu),
                           U_n∈Z_p^times.              (8)

The unit U_n may depend on n; only its valuation is used.
It follows that if A_(m,p)^infty is nonzero with valuation e,
then for every nu>e,

    v_p(d_n^II)=v_p(K_n)=e,
    v_p(Z_n)=(n−m)/(p−1)+e.                             (9)

In fact (5) already fixes v_p(A_(mp^nu))=e when nu≥e; the
strict inequality nu>e in (9) is needed to resolve (8).
If the limit vanishes, the rigorous alternative is only

    v_p(d_n^II)≥nu,
    v_p(Z_n)≥(n−m)/(p−1)+nu.                            (10)

Congruence (8) supplies no corresponding upper bound in this case.
This dichotomy controls an explicit fixed-prime endpoint quantity;
it is not a distribution theorem over changing primes or degrees.

## 5. One exact certificate closes the infinite 17-adic example

Take m=4 and p=17. The already computed small polynomial has
Q_4(1)=68/35 and A_4=136, but this alone only fixes the first
congruence layer. The single additional coefficient predeclared
for this argument is A_68 modulo 289. Its exact sum (2) gives

    A_68 ≡136=8·17  (mod 289).                          (11)

For a short independently reproducible certificate, the 35 summands
in (2), in j=0,...,34 order, reduce modulo 289 to

    288,34,170,221,272,68,136,187,221,
    0,0,0,0,0,0,0,0,
    164,102,221,85,238,204,119,272,85,
    0,0,0,0,0,0,0,0,228.

Their sum is 136 modulo 289. The complete machine-readable exact
certificate is `endpoint_gauss_17_single_certificate.json`. These
are modular integer calculations, not floating approximations or
a Hermite–Padé solve. No neighboring degree or prime was scanned.

Here r_0=e=1, so (5),(11) imply that the p-adic limit has valuation
exactly one. Equation (9) therefore proves, for every nu≥2,

    v_17(d_(4·17^nu)^II)=1,
    v_17(Z_(4·17^nu))=(4·17^nu−4)/16+1.                (12)

It also gives the endpoint determinant valuation

    v_17(Ecal_n)=(2n+1)(n−4)/16−2nu n+1,
                                  n=4·17^nu, nu≥2.    (13)

The original nu=1 endpoint K_68 is still only known here to have
valuation at least one: the congruence modulo 17 cannot resolve
its next digit. The seed A_68 in (11) does not remove the factorial
correction terms from K_68. Equations (12)–(13) deliberately exclude
that boundary index.

The next arithmetic target is to describe or prove nonvanishing of
the explicit limits A_(m,p)^infty, or to obtain uniform control
when m and p both vary. Even such information would still need
the reviewed bridge from the simultaneous endpoint polynomial to
the individual normalized type-I approximation. No irrationality
claim follows from this fixed-prime result.

## 6. Independent-review addendum: an integer Laurent form and exact truncated depths

The reviewer obtained a direct integer-coefficient version of (3):

    A_n=[t^n](t²+2t+2)^n
       =CT_t(2+t+2/t)^n.                               (14)

Indeed the actual Rodrigues formula is
Q_n(x)=n!/(2n)! times the n-th derivative of (1+x²)^n.
Multiplying by binom(2n,n) and evaluating at x=1 gives
1/n! times that derivative, which is exactly the coefficient of t^n
in (1+(1+t)²)^n. This proves (14) without a complex normalization.
The change t=sqrt(2)z gives the symmetric form in (3).

With f(t)=2+t+2/t, the elementary integer congruence
f(t)^p≡f(t^p) modulo p can be raised to m p^(r−1), using the
same binomial lifting step as in Section 2. Taking constant terms
then proves (4) directly in Z_p[t,t^(-1)]. This is an alternative
proof; the quadratic Frobenius proof above is also valid.

There is a useful exact sharpening of the stability formulation.
For fixed 1≤m, 3m<p, set

    h=v_p(A_(m,p)^infty), allowing h=infinity.

For EVERY nu≥1, one has

    min(v_p(d_(mp^nu)^II),nu)=min(h,nu).                (15)

To prove it, (8) and the unit U_n imply
min(v_p(K_n),nu)=min(v_p(A_(mp^nu)),nu). Equation (5)
identifies the latter with min(h,nu), and Theta_n is a unit.
This gives (15) without assuming that the limit is nonzero.

For the 17-adic family h=1. At nu≥2, (15) forces exact depth one.
At nu=1, it says only min(v_17(d_68^II),1)=1, so the boundary
index remains unresolved beyond its first factor of 17.
