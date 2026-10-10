> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the exact local endpoint-cancellation criterion

Date: 2026-09-13. Root verification of
`raw_large_prime_endpoint_local_classification.md`.

**Verdict: the prime-power criterion and valuation formulas pass.**
The proof does not estimate the resulting gcd as n grows.

The local first column A+C F_loc follows from subtracting B exp(z)
and the constant atan(1) times C from the original remainder column.
Rescaling the second column by exp(-1) yields B exp(t). Thus the
Wronskian in (7) has the factor exp(t), and its endpoint cofactor
E=-8 W123 is exactly the primitive homogeneous coefficient A_0(1),
not a cofactor at a different normalization. Direct differentiation
of F'=1/(1+z^2) gives F'(1)=1/2, F''(1)=-1/2,
F'''(1)=1/2, confirming every row in (6). Only the first column
has denominators at most two; E is integral.

Differentiating row determinants gives successively W013,
W023+W014, and W123+2W024+W015. A cubic endpoint factor in Q
annuls the first three quantities and makes the last equal to
6q3/4=3q3/2 modulo p^h. Powers of two are the only denominators
in this finite jet calculation; differentiation identities hold
over the required prime-power rings by polynomial identity.

For necessity, common endpoint divisibility means J0=0 modulo p^h.
The last identity then gives E=-12q3. The previously proved
p-primitivity of Q makes q3 a unit under the cubic congruence, and
p>3n>=3 makes 12 a unit. No converse about Wronskian order is
assumed in this step.

For sufficiency, W123 a unit makes J1,J2,J3 a basis over the whole
local ring, even when h>1. In J0=aJ1+bJ2+cJ3, W012=0 first kills
c, W013=0 kills b, and W023+W014=0 then kills a. Every division
is by the same unit W123. This verifies the exact prime-power
statement, rather than only a residue-field implication followed
by an unproved lift.

Applying that equivalence for every h gives the stated valuation
classification. The G=0 case is correctly treated over Q: a
nonzero E would force J0=0 and contradict actual B(1)!=0. Thus
G=0 implies E=0, and necessity excludes all large-prime endpoint
cancellation in that case. The formula for the reduced denominator
keeps the separately proved full cofactor content removed.

For the local order classification, p>=7 makes all factorials
through five and all differences between distinct orders <=5
units. The nonzero third Wronskian derivative ensures rank three
among these finite jets. Echelonization and the leading Vandermonde
then give the three and only three strictly increasing nonnegative
triples with sum six: (0,1,5), (0,2,4), (1,2,3). Terms beyond the
fifth Taylor degree cannot alter Wronskian coefficients through
degree three. Only the last order triple has J0=0, exactly as the
cofactor proof requires. This is a classification of possible
local types, not a claim that each occurs globally.

The n=1 exact triple has the stated endpoint relation and primitive
normalization; its leading coefficient b1 Xi is -1856, consistent
with the displayed cubic. The source's phrase that the equations
give a line must include the endpoint matching row: the high rows
alone give a two-dimensional space. This wording clarification was
sent to the author; it does not alter the proof for the actual family.

A further immediate corollary, sent for development, is that the
four-integer gcd

    F=gcd(Q(1),Q'(1),Q''(1)/2,E+12q3)

is nonzero and has v_p(F)=h_p for every p>3n. The source already
proves equivalence with these four congruences. Nonvanishing follows
because G=0 forces E=0 whereas q3 is nonzero. This avoids a separate
prime-support saturation in the exact large-prime carrier.

## Review of the subsequently added finite Bezout certificate

The source has now incorporated the four-integer corollary and fixed
the n=1 wording. I also checked its added Section 8. Expanding J0
in J1,J2,J3 without division gives
V J0=W023 J1-W013 J2+W012 J3. Taking a determinant with J1,J4
gives V W014=W013 W124-W012 W134, with exactly these signs.
Substitution therefore yields the displayed quadratic vector
identity. The triangular change from the first three Q jets to
W,W',W'' has unit diagonal over every odd Z_p. Thus
v_p(G)<=h_p+2v_p(E) follows by choosing a coordinate of J0 with
the minimal endpoint valuation, whenever this bound is finite.

When p divides E, the already proved h_p=0 makes the entire
false-carrier valuation at most 2v_p(E). When p does not divide E,
the endpoint valuation equals v_p(G). This proves the ordinary-gcd
formula G_(>3n)/gcd(G,E^2)_(>3n) for nonzero G, including E=0.
Finally multiplying the vector identity by 64 produces E^2 J0
in the three-jet ideal, and
E^2-(E-12q3)(E+12q3)=144q3^2 proves the four-jet ideal certificate.
No growing-degree resultant, nonunit inversion, or unproved bound
on the actual coefficients enters. These additional identities pass
review; their lack of an Archimedean height bound remains explicit.
