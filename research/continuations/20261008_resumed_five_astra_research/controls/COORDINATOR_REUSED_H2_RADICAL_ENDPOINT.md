> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Reuse of the accepted H2 endpoint on the current full radical

9 October2026, active continuation. This corrects an overly broad OPEN
label in current A4turn8 Section9: its leading mod3 endpoint samples are
already determined by the accepted original H2 endpoint theorem. Higher
endpoint digits, complete diagonal residues and directional solves are
different obligations and remain paid. No global e+pi conclusion follows.

## Archive and literature gate: an existing theorem is being reused

The original 7 October A1turn12 Section10, A1turn13 Sections1.2--2 and
A4turn12 Sections5--6 were read at the needed scope. A4turn15's explicit
acceptance of H2 includes its endpoint and complete diagonal consequences.
The 8 October A1turn0 already reuses them. This is NOT a new general
endpoint theorem or a fresh discovery of evaluation at-1. The relevant
H2 statement has passed independent review on the same sufficiently
large original index subwindow. It must not be reset to an arbitrary
primitive functional merely because a later report omitted the formula.

The prior primary Jacobi/binomial/finite Schur references are reused at
their hypotheses. The deduction below is elementary substitution into
the explicit already validated finite endpoint. No new literature theorem
or exhaustive novelty assertion is made.

Source paths, with scope, are:

- [Old A1turn12](../../20261007_resumed_five_astra_research/responses/A1_turn12.md), Section10;
- [Old A1turn13](../../20261007_resumed_five_astra_research/responses/A1_turn13.md), Sections1.2--2;
- [Old A4turn12](../../20261007_resumed_five_astra_research/responses/A4_turn12.md), Sections5--6;
- [Old A4turn15](../../20261007_resumed_five_astra_research/responses/A4_turn15.md), explicit H2 acceptance;
- [Current A1turn0](../responses/A1_turn0.md), accepted inputs and Section7.2;
- [Current A4turn8](../responses/A4_turn8.md), Sections7--9;
- [Current A1turn5](../responses/A1_turn5.md), full radical and saturated complement.

The spaces and original indices are unchanged. R_*= (9Q+1)/2,
K={0,...,3R}, R=b/2, P=3^(h-32), chi=P-R and

    G0 a = (y-1)^b a,
    g_s=(1-y)^(2chi)y^s,
    L_*=(P-1)/2 <= s <= L_*+delta-1.

The parent notation delta here is the current full-radical dimension.

## 1. What the old actual endpoint theorem says

For the complete ACTUAL producer after the first prefix and J reduction,

    f_act^(2) = f_act,K - 3 L_act B_act^-1 f_act,J,
    bar(f_act^(2))_u = (-1)^(R_*+u), 0<=u<=3R.       (1)

The original first-prefix and J endpoint corrections were explicitly paid
in the old independent proof; (1) is not a replacement by a model endpoint.
Since L_act,B_act^-1,f_act,J are integral, it also gives

    bar(f_act,K)_u = (-1)^(R_*+u).                    (2)

For the subsequent actual rank-b elimination, retain its FULL endpoint:

    f_act,new = G0^T f_act^(2)
                -3 M_b,act^T A_b,act^-1 f_act,b.     (3)

The established integral M_b,act and unit A_b,act^-1 make the last term
divisible by3. The stronger new M_b,act in3 from A4turn8 is unnecessary
for this mod3 deduction. Formula(3) keeps that correction for every
higher digit; it does not assert exact evaluation at-1.

Because b is even, (y-1)^b at y=-1 is1 modulo3. Thus for every amplitude
a in the actual degree<=R space,

    bar(f_act,new)(a) = (-1)^R_* a(-1) in F3.         (4)

## 2. Every displayed full-radical generator is an endpoint unit

The new explicit radical generators satisfy

    g_s(-1) = 2^(2chi)(-1)^s = (-1)^s in F3.

Combining with(4),

    bar(f_act,new)(g_s) = (-1)^(R_*+s) !=0.           (5)

This evaluates the actual leading endpoint on EVERY allowed current
radical generator, using the original accepted endpoint theorem.

Equivalently, since G0 g_s = (y-1)^(2P)y^s and P is odd,
Frobenius gives its three nonzero monomial slots s,s+P,s+2P. From(2),

    (bar f_act,K)_s+(bar f_act,K)_(s+P)
      +(bar f_act,K)_(s+2P)
      =(-1)^(R_*+s) (1-1+1)
      =(-1)^(R_*+s).                                (6)

Thus the explicit epsilon_s of A4turn8(9.6) are already known units.
There is no remaining open question about their mod3 nonvanishing.
All three slots remain within the original finite K coordinates by
the already proved support range.

## 3. Exact leading endpoint-annihilator inside the full radical

The full radical is

    (1-y)^(2chi)y^L_* F3[y]_(degree<=delta-1).

Its actual leading endpoint is nonzero evaluation at-1, up to the fixed
unit sign in(4). Its kernel is therefore EXACTLY

    (1-y)^(2chi)y^L_*(y+1)
          F3[y]_(degree<=delta-2),                   (7)

of dimension delta-1 when delta>=1, with the zero-dimensional interpretation
at delta=1. An explicit basis is g_s+g_(s+1),
L_*<=s<=L_*+delta-2. This is a statement about the actual leading
functional, not merely about an arbitrary hyperplane of possible endpoints.

For the exact 3-adic endpoint, choose v0=g_L_* and normalize

    v = v0 / f_act,new(v0).

The denominator is a ternary unit by(5), so this is an admissible local
basis operation. For h_s=g_s+g_(s+1), set

    h_s^exact = h_s - v*f_act,new(h_s).               (8)

Then its exact endpoint vanishes. Since f_act,new(h_s) is in3Z3,
h_s^exact-h_s is in3 times the amplitude lattice. Formula(8) retains
the actual higher endpoint rather than asserting it equals its reduction.
The resulting endpoint-adapted local basis is invertible over Z3.
This is not a redefinition of global integer columns or their ALL-prime
contents and least clearers.

If the latest unit complement has already been eliminated, its radical
lift differs by3 times the integral lattice: the physical cross in3^5
and complement inverse in3^-4 pay that statement. Therefore(5) remains
valid on those lifted radical generators. Its leading annihilator is
still(7); the exact lifts must use the correspondingly returned endpoint.

## 4. Reuse the old endpoint-adapted complement lemma

Old A1turn13 Theorem2.1 proves the following, with a complete proof:
for T in3^k Mat(Z3), a unit-normalized leading complement, and an endpoint
nonzero on the leading radical, choose the complement INSIDE the exact
endpoint kernel by subtracting multiples of an endpoint-unit radical lift.
This preserves the leading complement form and uses only unit divisions.
Its cross is in3^(k+1), inverse costs3^-k and matrix return is in3^(k+2).
Because the eliminated endpoint coordinates are exactly zero, this new
elimination makes no endpoint or complete-diagonal Schur correction.

Apply this at k=4 to the current actual T_act,red in81Mat, provided the
A4turn8 actual/core comparison has passed its independent audit. Formula(5)
supplies the needed endpoint-unit hypothesis, rather than leaving it open.
The leading matrix is the known -H_kappa; the current full radical and
unit complement are retained. Thus one can preserve the COMPLETE current
lambda while eliminating this latest complement, and put the exact
retained endpoint in coordinates(1,0,...,0). The matrix return starts
at3^6, so the first divided radical matrix digit at3^5 is unaffected.

This statement preserves whatever prefix/J/rank-b diagonal returns have
ALREADY entered that complete lambda. It does not erase their1/3 or1/9
terms, claim their individual residues are known, or import an exact
comparison at unproved higher precision. An exact older endpoint-adapted
rank-b basis can also preserve lambda^(2), as the old theorem states;
its relation to a chosen unadapted higher-layer frame needs the appropriate
unit congruence and return payments before their entries are interchanged.

## 5. What still remains and how the assignments should change

The LOWEST mod3 endpoint pivot is closed by reuse. A4turn9 was admitted
before this source recovery and its request is preserved unchanged. Its
return must be read before the next adaptive packet; the provider request
is not retrospectively edited or asserted to have received these sources.

The useful remaining tasks are higher exact endpoint lifts, the actual
returned diagonal where its residue genuinely enters a directional scalar,
and the paid endpoint-annihilator solve through further singular layers.
The current core/actual common divided matrix still must be evaluated
and its actual direction paid. A large radical of dimension delta does
not prove a primitive-denominator saving. Neither(5) nor an adapted basis
establishes the final cofactor ratio, all-prime gcd, least clearer,
nonzero complete error, or irrationality of e+pi.
