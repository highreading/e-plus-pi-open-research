> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the dual quadratic and endpoint separation

Date: 2026-09-13. Reviewer: audit_results.

Target: raw_dual_quadratic_and_endpoint_separation.md by audit_sources.
Status: PASS after correction of two signs in the explanatory expansion in Section 2. The author has applied that correction. The defining determinant and degree bound are unchanged. A subsequently identified cutoff improvement from p>3n to p>2n is also verified below; it does not extend the separate old type-I scale comparison.

This review covers Sections 1–8, including the full-depth divisors (11a) and (15a). The only computational controls use the two previously saved actual dual triples at n=1,2. No new canonical system, degree sequence, or prime scan was constructed.

## 1. Scales and the previous cubic carrier

The simultaneous triple is Q=Qhat, P=Pe, T=Pa from the previously reviewed global integral numerator theorem. In particular these are integral polynomials of degrees at most 2n, Z=Q(1) is a nonzero integer, and the actual normalized rational endpoint is -(P(1)+4T(1))/Z.

Equation (2) correctly distinguishes the current gcd G_4 from the endpoint cancellation of the primitive integral type-I triple. At p>3n the factorial n! is a unit. The reviewed identities

    Delta_B = (-1)^(n+1) F Z,
    Delta_A = (-1)^n n! F (P(1)+4T(1))

give valuation v_p(F)+v_p(G_4) for their common divisor. The earlier primitive cofactor carrier gives v_p(delta)+h_p for the same quantity. Subtraction proves (2). Thus the new simultaneous gcd cannot be substituted unchanged for h_p in the old cubic carrier.

## 2. Universal determinant, product rule and degree

The third column of the analytic Wronskian, after adding atan(z) times its first column, has entries

    T, T'-Q/D, T''-2Q'/D+QD'/D^2.

The exponential column after differentiation and multiplication by e^z is P,P'-P,P''-2P'+P. Clearing D^2 in the third column therefore gives exactly (3) and (4), with the stated signs.

The correction found in review was limited to the displayed expansion of the part with third column D^2(T,T',T''). After division by D^2, the correct expression is

    W(Q,P,T)
      - P(QT''-Q''T)
      - (P-2P')(QT'-Q'T).

Both additional terms have minus signs. Their degrees are the same with either sign, so the bound in (5) was unaffected. The author corrected the display. The two remaining determinant contributions in the target have their correct positive cofactor signs.

For input degrees at most m, QT'-Q'T has degree at most 2m-2: when both degrees are m the leading coefficient cancels, while otherwise the degree bound follows directly. The ordinary Wronskian has degree at most 3m-3, and QT''-Q''T has degree at most 2m-2. Consequently the D^2 part has degree at most 3m+2. The two remaining parts have degrees at most 3m+2 and 3m+1. Vanishing polynomials, including the low-degree boundary cases, cause no exception.

The common-factor identity (6) has a direct proof over any commutative ring. Replacing Q,P,T by fQ,fP,fT changes the row matrix by the lower triangular multiplier

    [ f   0   0 ]
    [ f'  f   0 ]
    [ f'' 2f' f ],

so its determinant is multiplied by f^3. This proof uses no characteristic-zero exponential, no division, and no reducedness assumption. It justifies use over both fields and Z/dZ.

## 3. The actual origin factor

The high simultaneous equations give two errors of order at least M=3n+1. In (4), subtracting the first function column from the second turns it into -e^(-z)(Qe^z-P), and the third is -(Q atan(z)-T). Thus both last function columns have order at least M.

In the Wronskian of q,g,h, the potentially lowest term q(g'h''-g''h') has candidate order 2M-3. Its coefficient cancels because both products have coefficient M^2(M-1)g_M h_M. The other terms already have order at least 2M-2. This also covers a higher order of either error or of q.

Multiplication by the characteristic-zero units D^2e^z preserves that order. With the degree bound at m=2n, the integral polynomial determinant is therefore z^(6n) times an integral polynomial K of degree at most two. No division by a factorial or by 6n occurs. The identity can subsequently be reduced modulo any integer, regardless of whether its characteristic-zero series proof would make sense there.

## 4. Rational nonvanishing in odd characteristic

I independently obtained (9) directly by applying the product rule with common rational factor Q and then evaluating the determinant on (1,a,b). With L=a'-a and H=b'-1/D, this gives

    Wcal = D^2 Q^3 [ L H' - (L'-L) H ].

If Q and P are nonzero, then a=P/Q is nonzero. Its logarithmic derivative is O(1/z) at infinity in every characteristic; hence a'=a is impossible. Thus L is nonzero.

Over an algebraic closure of a field of characteristic different from two, 1/(1+z^2) has nonzero simple-pole residues at its two distinct roots. The derivative of a rational function has residue zero at every finite point, also in positive characteristic, as seen from its Laurent expansion. Hence H cannot vanish.

If the bracket were zero, the nonzero rational function H/L would have logarithmic derivative -1. Its logarithmic derivative is again O(1/z) at infinity, a contradiction. This proves (10) without requiring T nonzero and without using finite-characteristic exponentials or logarithms.

The cutoff can be sharpened to p>2n using the globally reviewed endpoint-scalar content identity: c_Q=R Theta/h, where R=(2n)!/n! and h/Theta divides R. Thus c_Q divides R, so Q is nonzero modulo every p>2n. The low Taylor relation with the exponential unit modulo z^(2n+1) then prevents P from being zero modulo p; its denominators involve only factorials through 2n. Consequently Wcal is nonzero, and the exact monomial identity makes K p-primitive. This also proves that K is nonzero over Q and its positive content has no prime above 2n. This improved argument replaces the initial sufficient p>3n argument using individual k!/n! multipliers. The old type-I scale comparison in Section 1 remains restricted to p>3n.

## 5. Common roots and all prime-power depths

At a common nonzero root a modulo p>2n, all three polynomials contain z-a. The universal product identity forces a cube factor in Wcal. Since z^(6n) is coprime to z-a, the same cube divides the nonzero quadratic K, which is impossible. This argument remains valid at a=+i or -i because the determinant identity is polynomial.

The full integer refinement (11a) is valid over rings with zero divisors as well. If d divides all three endpoint values, monic division gives a common factor z-1 in (Z/dZ)[z]. In the quotient by (z-1)^3, the element z=1+(z-1), and hence z^(6n), is a unit with an integral truncated binomial inverse. Thus K vanishes in that quotient. A degree-at-most-two polynomial has zero remainder only when all its coefficients vanish. Therefore

    gcd(|Z|,|P(1)|,|T(1)|) divides content(K)

with every prime-power depth retained. No division by two or three is hidden here.

The additional leading-coordinate consequence also follows: if all three coefficients of degree 2n vanished modulo p>2n, the universal bound with m=2n-1 would give degree at most 6n-1, contradicting a nonzero multiple of z^(6n). This does not force Q alone to have full degree or nonzero constant coefficient, as the target explicitly states.

## 6. Endpoint parameters and the remaining fixed target

If p>2n divides G_lambda, T(1) must be a p-unit, since otherwise Q(1),P(1),T(1) would have a common zero. If lambda is a unit, P(1) is also a unit. Thus the ratio in (13) is well-defined at every cancellation prime for lambda=4, and multiplication by T(1) proves its full valuation identity.

Subtracting two combinations gives (lambda-mu)T(1), proving (14). Distinct integer parameters in an interval of length at most 2n have differences prime to every p>2n. Their large-prime gcds are therefore pairwise coprime, and each contributes at most v_p(Z), proving the product divisibility (15) with full exponents.

At an arbitrary prime, if g is the common valuation of the two gcds and a=v_p(lambda-mu), subtraction forces v_p(T(1))>=g-a; then v_p(P(1))>=g-a and v_p(Z)>=g. For g>=a, applying (11a) proves g<=a+v_p(content K); for g<a this inequality is immediate. This verifies (15a), including small primes.

The limitations in Sections 6 and 8 are necessary and correctly retained. Changing lambda changes the number approximated to e+lambda*pi/4. Neither the pairwise separation nor the absence of a common triple endpoint zero gives a bound for the fixed parameter 4. The illustrative arbitrary endpoint data are correctly labeled as an algebraic limitation, not actual HP examples.

## 7. Frozen exact controls

The independent output raw_dual_quadratic_independent_controls.json uses only Qhat,Pe,Pa from the earlier saved n=1,2 integral-error controls. It reconstructs the defining determinant, checks the corrected universal expansion and rational identity, divides by z^(6n), and obtains

    K_1=-20z^2+88z-44, content 4;
    K_2=-6623355200z^2+10006152832z+2216151616, content 64.

Both endpoint triple gcds are 1. These calculations check signs and normalization only; they are not the proof of the all-index statements.

The new result is a valid all-index large-prime saturation theorem for the common simultaneous endpoint divisor, and an exact all-prime carrier for its full depth. The unresolved target is the single unit ratio P(1)/T(1) near -4 at primes dividing Z, together with the size of the resulting cancellation. No irrationality conclusion has been obtained.

