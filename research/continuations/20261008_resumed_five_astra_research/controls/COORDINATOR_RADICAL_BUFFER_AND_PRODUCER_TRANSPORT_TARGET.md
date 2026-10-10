> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Original radical buffer and a precise actual-producer transport target

Coordinator note,8 October2026. The gap below is a proved elementary
consequence of original parameters and A1turn5's exact radical. The
transport proposal after it is NOT proved. This extends the already reused
bounded-top-support mechanism; it is not a new general producer mechanism.

## An arithmetic buffer in the exact original radical

Use P=3^(h-32),r=2 mod9, b=27P-243r,R=b/2,chi=P-R.
Then

    chi=(243r-25P)/2.

At sufficiently large original indices v3(P)>5, while r is a ternary unit.
Thus v3(chi)=5. In particular both P and8chi are divisible by243, and

    P-8chi is a NONZERO multiple of243.

It is nonzero because P is odd and8chi is even. Consequently its absolute
value is at least243. The exact radical has

    g_s=(1-y)^(2chi)*y^s,
    L*=(P-1)/2 <= s <= L*+delta-1,
    delta=min(chi-1,(P+3)/2-3chi),
    kappa=(3P-3)/2.

For two such indices s,t, the observed low-band index kappa-s-t ranges in

    [L*-2delta+2,L*].

Its lower endpoint lies above2chi by

    margin=(P+3)/2-2(delta+chi).

If delta=chi-1, then8chi<=P+5. Since P-8chi is a nonzero multiple of243,
it is at least243, and margin=(P+7-8chi)/2>=125.

If delta=(P+3)/2-3chi, then8chi>=P+5. In this branch8chi-P is a positive
multiple of243, and margin=(8chi-P-3)/2>=120.

Hence the UNIFORM integer bound is

    kappa-s-t >= 2chi+120,
    kappa-s-t <= (P-1)/2 < P.

This gives a fixed buffer of at least120 between the exact observed window
and the low band of (1-y)^(2P+2chi). The gap is not guessed from a small
auxiliary P. It follows from the original243 divisibility.

For any integral polynomial Q of degree<=30, modulo3 the product

    (1-y)^(2P+2chi)*Q
      =(1+y^P+y^(2P))*(1-y)^(2chi)*Q

has low-band degree<=2chi+30. All the above observed indices miss it,
with at least90 remaining margin. The higher P-shifted bands also miss.
This is a precise leading-digit support fact, not a whole pairing theorem.

## Actual producer transport: a possible paid route, still open

The recovered ACTUAL source support is

    R=(y+1)*x^(A-72)*q31(x) modulo3^31, deg q31<=72,
    r31(y)=beta^(-1)*sum_(k=0)^30(-3y/beta)^k,
    x=y-1.

For an actual one-lift trial with original amplitude

    x^(D+b)*g_s*y^k0*(y^(3Q)+3)*filter,

the multiplier carries x^(D+b-72)*q31*r31. Since b grows and b>=72,
it remains in x^D times an integral polynomial. Its total degree increases
by at most30. In a product with another original radical amplitude, the
finite extra factor is of the form

    x^(2P+2chi-72)*q31*r31.

The degree of its low-band part is at most2chi+30, so the PROVED gap above
is large enough for leading-digit translations of this size. The complete
reciprocal is essential; dropping it is not part of this proposed route.

This suggests a direct test of whether the complete R correction has
vanishing normalized Delta_GG on the whole radical, rather than merely a
small buffered subspace. It DOES NOT yet prove that vanishing.

## Specific debts the proposed route must pay

1. A sufficiently accurate ACTUAL corrected-column representative is needed.
   The old p20 support representative alone is insufficient. The p26
   physical overflow construction, including its deleted tail, may supply
   precision26, but the exact residual and inverse loss must be verified.

2. A substitution error3^26*Delta in the finite degree<=m space could use
   the retained mixed observation eta_M(R*F*Delta) in3, giving precision27.
   This is enough for a producer pairing needed through precision24 after
   the3^7 factor. The argument must prove Delta stays in the actual finite
   basis and use the FULL linear observation, not an unproved positivity.

3. The multiplier may have degree up to m+30. Its overflow coefficients
   require an actual uniform valuation or an evaluated physical tail.
   One cannot apply finite-basis mixed observation to degree>m vectors.
   The physically truncated complete functional remains integral, but that
   fact only helps after the overflow coefficient divisibility is proved.

4. Complete-core orthogonality can replace an admissible multiplier by its
   exact corrected lift. The paid compression/pole theorem must then be
   verified for its altered amplitude and all new LOW/HIGH extractions.
   A formal comparison Qc*L=R*trial does not by itself evaluate the pairing.

5. The mixed rank-b residue, actual endpoint and1/9 diagonal channel still
   need their own returns. Vanishing only on the radical does not prove the
   complement remains a unit, nor that the returned endpoint has a unit
   pivot. The actual Bsharp and final ALL-prime normalization remain open.

These are concrete original-object hypotheses for A4's producer/endpoint
task. The note supplies a proved support buffer and an explicit multiplier,
not a solved directional inverse or a primitive-error estimate.
