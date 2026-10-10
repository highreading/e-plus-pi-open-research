> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Uniform obstruction at the second divided digit, using the old sector method

9 October2026. This is a parent proof candidate for independent review.
It uses the NEW matrix evaluation of current A1turn6, whose complete
physical proof is under A3turn8 audit. It does not establish a global
proof or a primitive denominator estimate.

The generic tools are ALREADY in the archive: old A1turn7 Section4's
243-sector decomposition, old A1turn11 Sections3--5's dimension-counting
Frobenius syzygy, and old A4turn12 Section6's endpoint-restriction principle.
The parent read these proofs before this application. Their old original
rank formulas are not imported for the changed coefficient polynomial.
The new issue is their application to current A1turn6's second-divided
operator, which had an unclassified middle range. The finite diagnostic
second_divided_sector_finite_certificate.json is new and AUXILIARY only.

## 1. Original parameters and conditional physical transfer

Retain the same sufficiently large original j,n,h and fixed subwindow.
Write Pi=P/3, kappa=(Pi-1)/2 and

    delta=min{chi-1,(P+3)/2-3chi},
    D_uv=[y^(kappa-u-v)](1-y)^(2chi), 0<=u,v<delta.

A1turn6 evaluates the complete CORE radical matrix divided by3^5 as
-D modulo3. A3turn7's complete actual/core comparison in3^7 transfers
that digit in a common paid complementary frame. The accepted old H2
endpoint is evaluation at-1 on these amplitude coordinates, up to a
unit. Exact endpoint corrections differ by3 and hence do not affect
this3^5 digit. An endpoint-adapted first complement has cross in3^5,
physical inverse3^-4 and matrix return in3^6, also invisible here.

Subject to the current independent audit of A1turn6, the actual leading
endpoint-annihilating operator is therefore the restriction of-D to
the hyperplane e(a)=a(-1)=0. In adjacent-sum coordinates it is the
negative Hankel form of(1-y)^(2chi)*(1+y)^2, of dimensiondelta-1.

The old degree and parameter inequalities give .0145<chi/P<.136.
The exact original low congruence gives

    chi=243*c, c=1mod9,
    Pi=243*T, with T an odd power of3 and eventually9|T.

These are actual original parameters, not a free reindexing.

## 2. Three already classified ranges

Reuse A1turn6's exact ranks at their stated scope.

RangeI has B1=2chi+2delta-1-kappa<=0. Then D=0 and nullitydelta.
Since chi grows on the original infinite indices, delta>=242 eventually.

RangeII has 0<B1<=delta. The upper branch fordelta has positiveepsilon
and therefore cannot occur here; thusdelta=chi-1. Its exact nullity is

    delta-B1=(Pi-6chi+3)/2.

T-6c is odd and congruent3mod18. It cannot be negative here, because
243*(T-6c)+3>=0. ThusT-6c>=3 and this nullity is at least366. In
particular, the potential equalitydelta=B1 is excluded by the ORIGINAL
low digits, not assumed excluded by an asymptotic estimate.

RangeIII has epsilon=2chi+delta-Pi>0 and exact nullityepsilon.
In its lower branchdelta=chi-1,

    epsilon=243*(3c-T)-1.

The integer3c-T is positive and congruent3mod9, hence at least3. The
nullity is therefore at least728. In the upper branch,

    epsilon=(Pi+3)/2-chi
            >(1/6-.136)*P+3/2,

so it also exceeds242 for sufficiently large original indices.

## 3. The formerly unclassified middle range

Now suppose B1>delta andepsilon<=0. As in A1turn6,delta=chi-1.
The two inequalities give

    6c>T, 3c<=T.

Since6c-T is odd and congruent15mod18, positivity sharpens this to

    6c-T>=15.                                      (1)

Writec=9s+1, withs>=1 eventually. Set

    A=(T+9)/18,
    B=(8c-T+1)/18,
    C=2s,
    d0=3s.

All are integers. Equation(1) givesA<=3s. The inequalityT>=3c and
c>=7 givesT>=2c+7, henceB<=3s. AlsoC<=3s. All three exponents are
positive, and

    A+B+C=6s+1, A+B=4s+1>d0.

Use the old dimension-counting construction, now with these changed
exponents. In total degreed0, the coefficient triples in

    U X^A+V Y^B+W(Y-X)^C=0

have dimension

    (d0-A+1)+(d0-B+1)+(d0-C+1)=d0+2,

while the target homogeneous space has dimensiond0+1. A nonzero
syzygy therefore exists. ItsW component cannot be zero: a relation
betweenX^A andY^B alone has degree at leastA+B>d0.

Raise this relation to the ninth power in characteristic3 and multiply
by(Y-X)^2. Its nonzero third coefficient is

    F=W^9, degree9s=c-1.                           (2)

For the two equal sector forms of currentD, the exponent triples are

    a_low=(T+1)/2=9A-4,
    b_low=4c-a_low=9B-1,
    a_high=(T-1)/2=9A-5,
    b_high=4c-a_high=9B,
    r=2c=9C+2.

The first ninth-powered term is divisible by BOTH requiredX powers;
the second is divisible by BOTH requiredY powers; the last isF(Y-X)^r.
Thus(2) is a kernel coefficient for BOTH selected finite sector maps
in total degree3c-1. Their source degree isc-1 and their surviving
target exponents are exactly[(T-1)/2-c+1,(T-1)/2] for the low block,
and the one-step-lower interval for the high block. Their truncation
exponents exceedc-1 by the inequalities already paid. ThereforeF is
a nonzero source vector in each actual selected map.

Diagonal sign changes translate this homogeneous statement to the
signed coefficient sequence(1-z)^(2c); they are units and do not
alter its nonzero kernel dimension. No Han--Monsky formula or a
characteristic-zero determinant is extrapolated here.

## 4. Exact sector count and uniform conclusion

Apply the old243-sector decomposition with the NEW current exponent
2chi=486c and coefficient indexkappa=243*(T-1)/2+121.

The sector lengths arec for residues0..241 andc-1 for residue242.
Only residue sums121 and364 survive. There are122 equal sectors of
the low type,119 equal sectors of the high type, and the unequal pair
122<->242 of dimensionsc andc-1. The shared kernel above supplies
241 independent vectors in the equal sectors. The unequal symmetric
pair has rank at most2(c-1) in dimension2c-1, and supplies at least
one more independent kernel vector. Hence in the middle range

    nullityD>=242.                                 (3)

Together with Section2, this holds uniformly on ALL sufficiently
large original indices of the retained fixed subwindow.

For ANY endpoint functional, the242-dimensional subspace inkerD
meets its annihilator in dimension at least241. Each such vector
is also in the radical of the restricted form. Consequently

    nullity(D restricted to the actual endpoint annihilator)>=241.

This last inequality does not require an unproved assertion thatW
evaluates nonzero at-1. The accepted endpoint unit on the FIRST full
radical gives the valid local adaptation; the intersection bound works
whether its observation on this SECOND radical is zero or nonzero.

## 5. Meaning and limits

This candidate would CLOSE the proposed possibility of an immediately
nonsingular second-divided endpoint-annihilator anywhere in the retained
original subwindow. It does not rule out paid singular-layer directional
alignment, further growing arithmetic cancellation, or other routes.
It provides neither an actual directional solve nor primitive error
decay. The complete forcing, earlier1/3 and1/9 returns, full diagonal,
least clearer, ALL-prime gcd and actual finalq remain required.

The finiteT=81,c=19 receipt reports nullity242 and annihilator nullity241,
consistent with this proof; it is NOT its justification. T=81,c=10 and28
match the already classified neighboring ranges. Maximum computed block
size28; no original dense matrix was generated. The admitted A1turn7
andA3turn8 packets predate this new parent candidate, and are immutable.
Supply this note and oldA1turn11's proof on their next adaptive review.
