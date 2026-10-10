> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the extremal no-accessory compatibility reduction

Date: 2026-09-13. Root verification of
`raw_extremal_no_accessory_compatibility.md`.

**Verdict: the finite-jet equivalence and its stated remaining
two-parameter obstruction pass.** The all-degree exclusion is open.

The extremal order is M=3d+4 and the numerator monomial exponent
is s=M-2. The nonzero leading numerator coefficient supplies both
b_d!=0 and independence of the two leading Laurent coefficient
vectors. Thus the infinity echelon degrees really are d,d-1;
they are not inferred from genericity. Cofactor degree cancellations
leave degree at most two in the first-derivative coefficient and
at most one in the zeroth coefficient after division by z^(M-3).
The second-derivative coefficient follows directly from the
monomial Wronskian and its D^(-2) factor.

For an input z^m the output at degree m+1 is
-m(m-1)+a m+u. Annihilation at degrees d,d-1 therefore gives
a=2d-2 and u=-d(d-1). The next output coefficient of z^d is
-2d^2(d-1)+beta d+v; the coefficient of the next input term
vanishes because the raising polynomial also vanishes at d-1.
This fixes v as stated. The finite Laurent replacement A-C/z
has an error beginning at z^(d-3); the operator raises degree
by at most one, so it cannot affect the two leading comparisons.
The argument does not require an infinite Laurent antiderivative
in characteristic p.

The forcing formula follows from the ordinary product rule with
F'=1/D and its next two rational derivatives. Its polynomial part
and residual simple-pole numerator retain both parameters beta,
gamma. At a root of D, a zero of C would make the explicit
numerator determinant vanish, contradicting kappa z^s there.
Therefore the residue divisibility and logarithmic-derivative
form are equivalent at those roots over a splitting field.

For sufficiency, errors in finite exponential and arctangent jets
through M-1 enter L at order at least M-2: the third-derivative
term acquires one extra origin power from L3=zD. The coefficient
of an unknown remainder coefficient at order k, in output degree
k-2, is k(k-1)(k-M). It is a unit for every 2<=k<=M-1 when
p>M-1, including p=M. Induction from the two initial zero
coefficients consequently gives the required order M without
division by M or M!. This verifies the exact equivalence, rather
than a characteristic-zero heuristic carried across a resonance.

The polynomial mapping property L:P_d -> P_(d-1) is consistent
with the two leading cancellations and supplies a C solution by
dimension alone. It cannot remove the exponential branch, pole,
or initial conditions. The downward exponential recursion divides
only by -1,...,-d, retaining the last two scalar equations as
separate compatibility conditions.

For d=0 the exact numerator BC^2(z+1)^2 excludes the monomial
shape in odd characteristic. For d=1, the k=2 row is essential
because A also has degree at most one. The displayed rows follow
by multiplying the five Taylor coefficient equations by k!, and
the two reported minors satisfy 43*196-13*648=4. Thus no allowed
prime can destroy their common full rank. This is an exact
all-prime statement in two fixed degrees, and the discarded
p=47 subminor calculation is correctly identified as incomplete.

The two remaining accessory parameters and growing polynomial
compatibility equations are genuine. The note neither excludes
their simultaneous solutions in all degrees nor bounds a Smith
valuation from these equations.
