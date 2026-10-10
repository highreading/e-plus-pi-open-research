> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A large-prime cofactor-content identity and cubic carrier for the raw endpoint gcd

Date: 2026-09-13. Original bounded arithmetic continuation by
audit_sources. The statements below concern the actual raw family and
its primitive endpoint denominator. They provide an exact additional
minor identity and a constant-degree necessary carrier. They do not
bound the size of that carrier or prove shrinking integer forms.

## 1. Archive audit and exact normalization

The searched raw-family sources already contain the exact pair
`sources/raw_arctan_endpoint_arithmetic.md` and its independent audit.
The new session proves the dyadic endpoint valuation in
`raw_arctan_endpoint_dyadic_attempt.md`; that theorem retains the
endpoint gcd. The all-index leading-
(B) and cubic-degree results are indexed in
`raw_all_index_cubic_gate.md`. I found no previous large-prime gcd
theorem for this raw endpoint pair in the searched raw-family notes.
The fixed-parameter Möbius (H/J) identities and the different mixed
integral families are not being reused as statements about this pair.

Fix (n\ge1), let (N=2n+2), and use exactly the integer
((N-1)\)-by-(N) matrix (J_n) from the canonical arithmetic note.
Its first (2n) rows are (k!) times the high coefficient
functionals, (n+1\le k\le3n), and its last row is
(C(1)-4B(1)). Let (w_n\in\mathbb Z^N) be its signed maximal-minor
vector, with the common sign chosen so that appending a row (u)
gives (u(w_n)). Define



$$
\delta_n=\gcd_i |(w_n)_i|>0.
\tag{1}
$$



This is the full maximal-minor content, not an endpoint gcd. Let



$$
\Delta_A=\det[J_n;u_A],\quad
\Delta_B=\det[J_n;u_B],\quad
\Delta_T=\det[J_n;u_T],
\tag{2}
$$



where (u_A=n!A(1)), (u_B=B(1)), and (u_T=b_n), the coefficient
of (z^n) in (B). Thus $\Delta_T$ is exactly the previously
studied leading-(B) determinant (B_\star\), with its coordinate
border, not an endpoint border.

Take the actual triple



$$
(\widehat A,\widehat B,\widehat C)\in\mathbb Z[z]^3,
\quad \gcd\{\text{all its coefficients}\}=1,
\tag{3}
$$



on the canonical solution line. It satisfies degree at most (n),
$\widehat C(1)=4\widehat B(1)$, and the order-(3n+1) Taylor
condition. Its common sign is immaterial. It is not normalized by
$B(1)=1$. Put



$$
h_p=\min\{v_p(\widehat A(1)),v_p(\widehat B(1))\}.
\tag{4}
$$



For every (p>n), the (B,C) coefficient pair in (3) is already
(p)-primitive. Indeed the low equations express every coefficient
of (A) as a $\mathbb Z_p$-linear combination of those of (B,C):
all factorial and odd Taylor denominators are at most (n). If all
coefficients of (B,C) were divisible by (p), so would those of
(A), contradicting (3). Consequently the cofactor scale from
((\widehat B,\widehat C)) to (w_n) has valuation exactly
(v_p(\delta_n)), and



$$
\begin{aligned}
v_p(\Delta_A)&=v_p(\delta_n)+v_p(\widehat A(1)),\\
v_p(\Delta_B)&=v_p(\delta_n)+v_p(\widehat B(1)),\\
v_p(\Delta_T)&=v_p(\delta_n)+v_p(\widehat b_n).
\end{aligned}
\tag{5}
$$



The omitted (n!) in the first valuation is a unit for these primes.
In particular



$$
v_p\gcd(\Delta_A,\Delta_B)=v_p(\delta_n)+h_p.
\tag{6}
$$



Raw common factors of the two augmented determinants therefore
include an entire content factor which must be removed before
discussing endpoint cancellation.

## 2. A nonzero Wronskian numerator over every odd characteristic

Let (K_0) be any field of characteristic different from two, and
let (A,B,C\in K_0[z]) with (B,C\ne0). Put (D=1+z^2) and form
the polynomial



$$
\mathcal N(A,B,C)=
\det\begin{pmatrix}
D^2A&B&C\\
D^2A'+DC&B+B'&C'\\
D^2A''+2DC'-D'C&B+2B'+B''&C''
\end{pmatrix}.
\tag{7}
$$



In characteristic zero it is exactly
(D^2e^{-z}W(A+Be^z+C\arctan z,Be^z,C)), after subtracting the
logarithmic column contribution. Formula (7), not the transcendental
notation, defines the polynomial in positive characteristic.

**Lemma 1.** The polynomial $\mathcal N(A,B,C)$ is nonzero.

**Proof.** In (K_0(z)) put



$$
K=(A/C)'+1/D,\qquad L=(B/C)'+B/C.
$$



An exact determinant simplification gives



$$
\mathcal N=D^2C^3\{K(L+L')-K'L\}.
\tag{8}
$$



There is no nonzero rational function (H) with (H'/H=1) or
(H'/H=-1): its logarithmic derivative is (O(1/z)) at infinity
in every characteristic. Hence (L\ne0). Also (K\ne0): after
extending the constant field if necessary, (1/D) has nonzero
simple-pole residues at (z=\pm i), whereas the derivative of a
rational function has zero residue at every finite point, in every
characteristic. If (8) vanished, the nonzero rational function
(K/L) would satisfy ((K/L)'/(K/L)=1), a contradiction. □

The residue and infinity arguments are valid in positive
characteristic even though there are additional rational constants
such as (z^p); those constants do not have logarithmic derivative
(\pm1).

## 3. The actual integral cubic is primitive at every prime above (3n)

Define from the primitive integral triple (3)



$$
\widehat Q_n(z)=
\frac{\mathcal N(\widehat A,\widehat B,\widehat C)}{z^{3n-1}}.
\tag{9}
$$



The reviewed Wronskian degree and origin identities show that this
is an **integral** polynomial of degree at most three. Its leading
coefficient is



$$
q_3=\widehat b_n\widehat\Xi_n,\qquad
\widehat\Xi_n=
\widehat a_n\widehat c_{n-1}
-\widehat a_{n-1}\widehat c_n+\widehat c_n^2.
\tag{10}
$$



The all-index dyadic work proves that (10) is nonzero over
$\mathbb Q$; no division by it, or by the content of (9), is
performed here.

**Lemma 2.** For every prime (p>3n), $\widehat Q_n$ is
(p)-primitive: at least one of its four coefficients is a unit.

**Proof.** Reduce the primitive coefficient triple modulo (p).
It is nonzero, and its (B,C) pair is nonzero by §1. We show that
neither individual polynomial (B) nor (C) can vanish.

If (C=0), the (2n) high rows imply that the degree-at-most-(n)
polynomial



$$
H(X)=\sum_{j=0}^n b_j(X)_j
$$



vanishes at all (X=n+1,\ldots,3n\). These are (2n>n) distinct
elements of the field. Thus (H=0), then (B=0), a contradiction.

If (B=0), the (C) high-row block, after multiplication by units,
has entries (0) when (k-j) is even and signed entries
(1/(k-j)) when (k-j) is odd. Separate the two column parities
and the opposite row parities. Each set of row parities contains
(n) rows, whereas either column-parity block has at most
$\lceil(n+1)/2\rceil\le n$ columns. Choose that many rows in
each block. Every resulting square Cauchy determinant is a unit:
the differences (k-j\) lie in $[1,3n]$, all row and column
differences are nonzero modulo (p>3n), and the signs factor by
row and column. Thus the (C) block has full column rank, again
forcing (C=0), a contradiction.

Lemma 1 now implies that the reduction of (7) is nonzero. Since
division by the monomial in (9) merely removes identically zero
initial coefficients, its quotient is nonzero modulo (p). □

The same argument applies to every nonzero solution of the raw
high equations over $\mathbb F_p$, not just the reduction of the
canonical rational solution. For that version, the origin
divisibility in (9) follows by using the Taylor expansions through
degree (3n); all their denominators are units for (p>3n).

## 4. Endpoint divisibility forces a cubic power, including its unit leading coefficient

**Theorem 3.** Let (p>3n) and (h=h_p\ge1). Then



$$
\boxed{\widehat Q_n(z)\equiv q_3(z-1)^3\pmod{p^h},
\qquad v_p(q_3)=0.}
\tag{11}
$$



In particular (\widehat b_n\) and (\widehat\Xi_n\) are units
at every such cancellation prime.

**Proof.** Modulo (p^h), all three polynomials
$\widehat A,\widehat B,\widehat C$ are divisible by (z-1),
because their endpoint values vanish; here
$\widehat C(1)=4\widehat B(1)$. For three functions or formal
columns the Wronskian identity



$$
W(fy_1,fy_2,fy_3)=f^3W(y_1,y_2,y_3)
$$



is an identity over the integers, hence remains valid over
$\mathbb Z/p^h\mathbb Z$. Equivalently it follows directly
from (7). Thus $(z-1)^3$ divides $\mathcal N$ modulo
(p^h). The factor (z^{3n-1}) is a unit modulo $(z-1)^3$,
so $(z-1)^3$ also divides $\widehat Q_n$ modulo $p^h$.
Since $\deg\widehat Q_n\le3$, the congruence in (11) follows.
If (q_3\) were divisible by (p), the whole cubic would vanish
modulo (p), contradicting Lemma 2. Formula (10) proves the final
unit assertions. □

Writing $\widehat Q_n=q_3z^3+q_2z^2+q_1z+q_0$, (11) is
equivalently the three necessary congruences



$$
q_2+3q_3\equiv q_1-3q_3\equiv q_0+q_3\equiv0\pmod{p^h}.
\tag{12}
$$



One must not replace the integral cubic by an arbitrarily scaled
monic cubic before applying this statement. The proof itself shows
that monic normalization is legitimate at a cancellation prime,
because the actual (q_3) is then a unit.

## 5. An exact three-cofactor gcd identity

For an integer (m\ne0\), let (m_{>3n}\) denote its full positive
prime-power part supported on primes greater than (3n).

**Theorem 4.** The actual augmented determinants satisfy



$$
\boxed{
\gcd(|\Delta_A|,|\Delta_B|,|\Delta_T|)_{>3n}
 =(\delta_n)_{>3n}.}
\tag{13}
$$



**Proof.** Fix (p>3n). Subtract (v_p(\delta_n)) from each of
the three valuations using (5). If the two endpoint valuations
are not both positive, their minimum is already zero. If they are
both positive, Theorem 3 says (v_p(\widehat b_n)=0\). The
minimum of all three is therefore zero in either case. □

Thus the **additional coordinate minor** $\Delta_T$ removes
every large-prime common factor beyond the unavoidable full
cofactor content. This is not a claim that the two endpoint
determinants themselves have no large common factors.

There is also a direct finite-field rank formulation. Appending all
three rows (u_A,u_B,u_T\) to (J_n\) gives a matrix with full
column rank modulo every (p>3n). For if a nonzero kernel vector
existed, its reconstructed triple would have all three endpoint
values zero and (b_n=0\). Lemmas 1–2 and the endpoint factorization
would force a nonzero cubic with unit leading coefficient, contrary
to (10). This statement retains the possibility that (J_n\) by
itself loses row rank modulo such a prime.

## 6. A constant-degree carrier and an actual primitive-denominator divisor

Put



$$
G_n=\gcd\left(
|\widehat Q_n(1)|,
|\widehat Q_n'(1)|,
|\widehat Q_n''(1)/2|
\right),
\tag{14}
$$



with $\gcd(0,0,0)=0$. The quotient in (14) is integral.
Theorem 3 proves, for every (p>3n),



$$
h_p\le v_p(G_n),\qquad
\min\{h_p,v_p(\widehat b_n)\}=0.
\tag{15}
$$



The derivative triple in (14) and the coefficient triple in (12)
generate the same ideal over the integers. Indeed translating
the variable gives
$t_2=q_2+3q_3$,
$t_1=(q_1-3q_3)+2t_2$, and
$t_0=(q_0+q_3)+(q_1-3q_3)+t_2$.

Let (q_n>0\) be the actual reduced denominator of
$\widehat A(1)/\widehat B(1)$, so the primitive endpoint form
is (q_n R_n(1)\) after canonical (B(1)=1\) normalization. Set
(U_n=|\Delta_B|/\delta_n\), an integer. From (5),



$$
v_p(q_n)=v_p(U_n)-h_p\qquad(p>3n).
\tag{16}
$$



Consequently an exact useful divisor statement is



$$
\boxed{
\frac{(U_n)_{>3n}}{\gcd((U_n)_{>3n},G_n)}\ \mid\ q_n.}
\tag{17}
$$



If (G_n=0\), this version is simply the trivial divisor (1\),
not an unstated nonvanishing claim. Another consequence of (13)
is that the entire prime-power part of (U_n\) supported on
primes (p>3n\) dividing $\Delta_T/\delta_n$ survives in
(q_n\): at those primes there can be no endpoint cancellation.

Finally the integral discriminant satisfies



$$
\boxed{v_p\operatorname{Disc}(\widehat Q_n)\ge2h_p
\quad(p>3n).}
\tag{18}
$$



To check this, write the cubic at (z=1+x\). Its coefficients of
(x^0,x^1,x^2\) are all divisible by (p^{h_p}\), and every term
of the cubic discriminant contains at least two of them, counted
with multiplicity. Explicitly the five terms are
(t_2^2t_1^2-4q_3t_1^3-4t_2^3t_0-27q_3^2t_0^2
+18q_3t_2t_1t_0\). This also covers a zero discriminant under
the usual infinite-valuation convention; no all-index
squarefreeness is assumed.

## 7. Exact remaining obstruction

The common endpoint factor is now localized in three explicit
integer values of the primitive cubic. The leading coefficient is
a unit at every large cancellation prime, and the extra leading-
(B\) coordinate minor gives the exact content identity (13).
These are genuine restrictions on the primitive arithmetic,
stronger than a coefficient-denominator bound.

What is still missing is a quantitative upper bound for the
large-prime part of (G_n\), or a relation estimating its common
factors with (U_n\). The all-index nonzero leading coefficients
give no such bound on their Archimedean sizes or on the numerators
of the translated cubic coefficients. The rational finite-state
update likewise does not by itself bound these gcds. The
discriminant may vanish; (G_n\) has not been proved nonzero in
every degree; and the necessary cubic-power condition has not
been promoted to a sufficient endpoint-cancellation criterion.

The next concrete arithmetic target is therefore the actual
three-integer carrier (12), with the full cofactor content
$\delta_n$ removed from (U_n\), rather than the unsaturated
pair $(\Delta_A,\Delta_B)$. No prime scan, conjectural
normality theorem, or inference from numerical positivity enters
the proofs above.
