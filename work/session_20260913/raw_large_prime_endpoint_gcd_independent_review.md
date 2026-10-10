> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the raw large-prime endpoint gcd carrier

Date: 2026-09-13. Reviewer: audit_computations.

Reviewed file: `raw_large_prime_endpoint_gcd_carrier.md`, Sections 1–7.
This is an algebraic audit of the actual coefficient-primitive raw family.
No new numerical sample, canonical degree construction, prime scan, or
inference from finite data was used.

**Verdict: all stated theorems pass.** In particular, the argument remains
valid for every prime strictly greater than (3n), for arbitrary nonzero
finite-field kernel vectors rather than only reductions of the rational
canonical vector, and when the carrier or discriminant is zero. The
result is an exact restriction on primitive endpoint cancellation. It
does not provide a quantitative gcd bound or an irrationality proof.

## 1. Cofactor content and the actual primitive triple

The matrix convention agrees with the canonical raw arithmetic matrix:
the (2n) high rows are multiplied by (k!), and the remaining row is
(C(1)-4B(1)). The three appended rows are respectively (n!A(1)),
(B(1)), and the coefficient (b_n). The first row is integral because
the low Taylor equations involve factorial and odd denominators at most
(n). Its extra (n!) is a unit at every prime used in the theorem.

Let ((\widehat A,\widehat B,\widehat C)) be primitive as a full integer
coefficient triple. For (p>n), its (B,C) coefficient vector is
(p)-primitive: the low equations express the coefficients of (A) as
(p)-integral linear combinations of those of (B,C). Thus a common
(p) factor in (B,C) would be a common factor in the whole triple.

The maximal-minor vector (w) is a rational scalar multiple of that
(B,C) vector. Its scalar has valuation exactly
(v_p(\delta_n)), since (\delta_n) is the gcd of *all* coordinates
of (w). This proves each identity (5), including the endpoint (A)
identity with its harmless unit (n!). It does not assume that the
scalar is globally an integer. Consequently the cofactor content is
removed correctly before any endpoint gcd is discussed.

Both (\delta_n\mid\Delta_B) and (\delta_n\mid\Delta_T)
hold over the integers, because their appended rows are integral.
The actual positive integer (U_n=|\Delta_B|/\delta_n) therefore
has the stated local valuations.

## 2. The positive-characteristic Wronskian argument

The determinant in (7) is a polynomial definition; no exponential or
logarithm is being introduced as a global function in characteristic
(p). Dividing the three formal function columns by (C), or directly
simplifying the determinant over the rational function field, gives



$$
\mathcal N=D^2C^3\{K(L+L')-K'L\},\qquad
K=(A/C)'+1/D,\quad L=(B/C)'+B/C.
$$



Every step is an identity of rational functions and remains valid in
odd characteristic.

For any nonzero rational (H=P/Q), its logarithmic derivative satisfies
(H'/H=O(1/z)) at infinity. In positive characteristic the leading
coefficient can disappear, which only improves this decay. Hence it
cannot equal either (1) or (-1), and (L\ne0).

After a constant-field extension, (D=1+z^2) has distinct roots
(\pm i). Its reciprocal has a nonzero residue at both roots. A
rational derivative has zero residue in every characteristic: the
coefficient of (t^{-1}) in a differentiated Laurent series would
come from the constant term and is therefore zero. Thus (K\ne0).

If the displayed determinant vanished, division by the nonzero
(K,L) would give



$$
\frac{(K/L)'}{K/L}=1,
$$



again impossible at infinity. This is stronger and more suitable here
than an appeal to a general Wronskian independence criterion. The
presence of extra differential constants such as (z^p) causes no
problem for this proof.

## 3. Nonzero (B,C) and the arbitrary-kernel finite-field bridge

For (p>3n), all high-row scaling factors and Taylor denominators
through degree (3n) are units. If (C=0), the polynomial
(\sum_j b_j(X)_j), of degree at most (n), vanishes at the (2n)
distinct points (n+1,\ldots,3n). Since (n\ge1), this forces
(B=0). The falling-factorial basis is triangular with diagonal one,
so no additional characteristic restriction is hidden here.

If (B=0), the opposite-parity blocks of the arctangent high matrix
are signed Cauchy matrices. There are (n) available rows of each
parity and at most (\lceil(n+1)/2\rceil\le n) columns in either
block. The row and column differences are nonzero modulo (p), and
every denominator (k-j\in[1,3n]) is a unit. Thus the selected square
minors are units and (C=0). This establishes that both polynomials
are individually nonzero for every nonzero finite-field kernel vector.

The final paragraph of Section 3 can be made fully explicit as follows.
This is a clarification of its valid argument, not an added hypothesis.
For an arbitrary high-row solution over (\mathbb F_p), reconstruct
(A) from the low rows and let



$$
E_T(z)=\sum_{j=0}^{3n}\frac{z^j}{j!},\qquad
F_T(z)=\sum_{2j+1\le3n}\frac{(-1)^jz^{2j+1}}{2j+1}.
$$



Then (R_T=A+BE_T+CF_T=O(z^{3n+1})), and



$$
\begin{aligned}
E_T'-E_T&=O(z^{3n}),& E_T''-E_T&=O(z^{3n-1}),\\
F_T'-1/D&=O(z^{3n}),& F_T''+D'/D^2&=O(z^{3n-1}).
\end{aligned}
$$



Write (K_{mat}) for the polynomial matrix in (7). The jet matrix
of ((R_T,BE_T,C)), with rows of derivative orders (0,1,2), agrees
with



$$
K_{mat}\operatorname{diag}(D^{-2},1,1)
\begin{pmatrix}1&0&0\\E_T&E_T&0\\F_T&0&1\end{pmatrix}
$$



in row zero, differs by (O(z^{3n})) in row one, and differs by
(O(z^{3n-1})) in row two. The last two matrices have unit
determinants as formal power series. The jet determinant itself is
divisible by (z^{3n-1}), since its first column has orders at least
(3n+1,3n,3n-1). The error orders show that the same divisibility
holds for (\mathcal N).

This argument needs no coefficient with denominator ((3n+1)!).
In particular, it covers the boundary possibility (p=3n+1).
Differentiation can annihilate a leading coefficient in characteristic
(p), but this only increases an order of vanishing.

The degree bound (\deg\mathcal N\le3n+2) is also a universal
polynomial identity. The potential degree-(3n+3) term cancels between
the equal top degrees of (A,C); all remaining terms have degree at
most (3n+2). Thus division by the origin monomial gives a polynomial
of degree at most three for arbitrary finite-field kernel vectors.
Its leading coefficient is the same polynomial identity (b_n\Xi_n).

For the actual primitive integer triple, origin division is integral:
it simply removes identically zero initial coefficients. Reducing it
modulo (p) is compatible with the determinant definition. Lemma 1
and the individual nonvanishing of (B,C) consequently prove that
this integral cubic is (p)-primitive.

## 4. Endpoint factorization over prime-power rings

The endpoint argument is valid over (\mathbb Z/p^h\mathbb Z),
which has zero divisors. A direct polynomial covariance identity
makes this especially transparent. If (f) is a polynomial, then



$$
K_{mat}(fA,fB,fC)=
\begin{pmatrix}f&0&0\\f'&f&0\\f''&2f'&f\end{pmatrix}
K_{mat}(A,B,C),
$$



so (\mathcal N(fA,fB,fC)=f^3\mathcal N(A,B,C)) over every
commutative coefficient ring. There is no need for a formal
exponential in the prime-power ring.

If (h_p\ge1), all three endpoint values vanish modulo (p^{h_p}),
using (C(1)=4B(1)). Hence (f=z-1) divides all three polynomials,
and (f^3\mid\mathcal N). Since (z^{3n-1}) is a unit modulo
((z-1)^3), it follows that ((z-1)^3\mid\widehat Q_n) over the
same ring. Monic division by ((z-1)^3), together with degree at most
three, gives



$$
\widehat Q_n\equiv q_3(z-1)^3\pmod{p^{h_p}}.
$$



If (q_3) were zero modulo (p), the entire cubic would be zero,
contradicting its proved (p)-primitivity. Thus both factors in
(q_3=\widehat b_n\widehat\Xi_n) are units. The use of a unit
leading coefficient is a conclusion here, not a hidden monic
normalization assumption.

The direct finite-field rank claim follows as written. A nonzero
kernel vector for all three appended rows would have (A(1)=B(1)=
C(1)=0) and (b_n=0). The arbitrary-kernel bridge above gives a
nonzero cubic, while endpoint factorization and (q_3=b_n\Xi_n)
would make that cubic zero. This contradiction proves full column
rank of the augmented matrix. It does **not** establish full row
rank of (J_n) alone; the note correctly retains possible content
(\delta_n) at these primes.

## 5. Exact gcd identity and reduced-denominator divisor

After subtracting (v_p(\delta_n)) from the three determinant
valuations, their minimum is



$$
\min\{v_p\widehat A(1),v_p\widehat B(1),v_p\widehat b_n\}.
$$



It is zero if an endpoint is a unit. If both endpoints are divisible
by (p), the preceding theorem makes (\widehat b_n) a unit.
This proves the three-cofactor gcd identity (13) with all prime
powers, not only its radical. It does not eliminate cancellation
between the two endpoint minors without the third coordinate minor.

The translated Taylor coefficients are related to the three
coefficient deviations in (12) by an integral triangular change
of basis with determinant one. Their gcd ideals are therefore
exactly equal. Thus (h_p\le v_p(G_n)).

For the actual reduced endpoint denominator,



$$
v_p(q_n)=v_p(\widehat B(1))-h_p=v_p(U_n)-h_p.
$$



Combining this with (0\le h_p\le\min(v_p(U_n),v_p(G_n)))
gives precisely the divisor (17). In particular, it is a statement
about the reduced denominator, not a displayed coefficient clearer.
If a prime divides (\Delta_T/\delta_n), then
(v_p\widehat b_n>0), so (h_p=0) and the full local power of
(U_n) survives. These conclusions use the actual integral cubic;
an arbitrary scalar normalization would invalidate the carrier
valuation interpretation.

## 6. Degenerate cases and the remaining obstruction

The convention (G_n=0) is handled correctly. Then
(v_p(G_n)=+\infty), the upper bound on (h_p) is vacuous, and
(\gcd((U_n)_{>3n},0)=(U_n)_{>3n}), so (17) supplies the divisor
one. There is no implicit assertion that the cubic has nonzero
Taylor data of order below three at the endpoint.

For the discriminant, writing the translated cubic as
(q_3x^3+t_2x^2+t_1x+t_0) gives



$$
t_2^2t_1^2-4q_3t_1^3-4t_2^3t_0-27q_3^2t_0^2
+18q_3t_2t_1t_0.
$$



Every term has valuation at least (2h_p). A zero discriminant
has infinite valuation, so the inequality remains valid without
squarefreeness or a nonzero-discriminant hypothesis.

The proof yields a necessary cubic-power congruence, a saturated
three-minor gcd identity, and an actual reduced-denominator divisor.
It does not bound the size of (G_n), its common factors with (U_n),
or the endpoint cancellation exponent from above by an effective
asymptotic quantity. The note's final obstruction statement is
therefore correctly scoped.

One purely verbal clarification was sent to the author: in the
endpoint proof, say explicitly that ((z-1)^3) divides (Q) after
removing the unit (z^{3n-1}), avoiding an ambiguous pronoun. No
mathematical correction was required.
