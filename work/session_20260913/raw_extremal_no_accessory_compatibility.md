> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Two-parameter compatibility for an extremal monomial Wronskian

Date: 2026-09-13. Original bounded algebra continuation by audit_sources.
This note studies the necessary lower-degree triple in the exceptional
nullity-three scenario of `raw_large_prime_nullity_and_smith.md`.
It gives an explicit two-parameter differential compatibility system
over the residue field and excludes its two smallest degrees by exact
identities. It does not exclude the extremal shape in every degree.
Independent review is requested for the general reduction.

## 1. Setup and the characteristic-p boundary

Put (d=n-1\ge0\), (M=3d+4\), and (s=M-2=3d+2\). Work over
(K=\mathbb F_p\), with (p>3d+3=M-1\). An extremal triple consists
of polynomials of degree at most (d\), with (B,C\ne0\), satisfying



$$
A+BE_T+CF_T=O(z^M),
\tag{1}
$$



where (E_T,F_T\) are the exponential and arctangent Taylor
polynomials **through degree (M-1\)**. All their denominators are
units. The reviewed nonzero numerator and degree/order arguments give



$$
N(A,B,C)=\kappa z^s,\qquad \kappa\ne0.
\tag{2}
$$



The coefficient identity is



$$
\kappa=b_d\Xi_d,\qquad
\Xi_d=a_dc_{d-1}-a_{d-1}c_d+c_d^2,
\tag{3}
$$



with negative-index coefficients zero. Thus (b_d\ne0\) and the
two leading Laurent coefficient vectors of (C\) and (A-C/z\)
are independent. In particular their echelon degrees at infinity
are (d,d-1\).

The allowed prime can equal (M\), for example (d=1,p=7\). A
characteristic-zero argument invoking a full analytic solution
with exponent (M\), or division by (M!\), would be invalid at
this boundary. The construction below uses polynomial jets and
rational functions only.

## 2. The bounded-degree operator and its remaining parameters

Write (D=1+z^2\). The Wronskian cofactor construction applied to
(2), with its common monomial canceled, gives



$$
L=zD\,\partial^3
-\bigl[(z+s)D-4z^2\bigr]\partial^2
 +(a z^2+\beta z+\gamma)\partial+(u z+v).
\tag{4}
$$



Here the coefficients are in (K\). To justify the degrees without
infinite exponential series, use the polynomial cofactor identities
from the reviewed homogeneous-ODE construction. The numerators for
the coefficients of $\partial$ and (1\) have degree at most
(3d+3\) and (3d+2\), respectively. Their origin orders are at
least (M-3=3d+1\). Dividing by this common monomial leaves degrees
at most two and one. The truncated derivatives have error order at
least (M-3\), so the same divisibility holds even when (p=M\).
The $\partial^2$ coefficient follows directly by differentiating
the known monomial numerator, retaining the (D^{-2}\) factor.

No exponential or logarithm needs to be adjoined to define the
identities annihilated by this operator. If (L=\sum_{j=0}^3L_j
\partial^j\), define its exponential conjugate on polynomials by



$$
L^{[1]}B:=\sum_{j=0}^3L_j(\partial+1)^jB.
\tag{5}
$$



The cofactor identities say (LC=0\), (L^{[1]}B=0\), and
(LA+\mathcal T_L(C)=0\), with the last rational expression
computed in §3.

For a Laurent leading term (z^m\), the coefficient of (z^{m+1}\)
in (4) is



$$
F(m)=-m(m-1)+am+u.
$$



The two infinity degrees (d,d-1\) in (3) force



$$
F(m)=-(m-d)(m-d+1),\qquad
a=2d-2,\quad u=-d(d-1).
\tag{6}
$$



This use of infinity requires only the finite Laurent jet
(A-C/z\). Its image under (L\) differs from the exact rational
arctangent forcing by (O(z^{d-2})\), because
(D^{-1}-z^{-2}=O(z^{-4})\). Hence the coefficients at degrees
(d+1,d\) used here are valid over (K\), without asserting an
infinite Laurent solution.

For the degree-(d\) Laurent branch, its next coefficient, at
degree (d\), is



$$
d(d-1)(d-3d)+\beta d+v.
$$



The coefficient of the next input term of degree (d-1\) is
(F(d-1)=0\), so it cannot cancel this expression. Therefore



$$
v=2d^2(d-1)-d\beta.
\tag{7}
$$



The resulting operator has only **two** undetermined scalars:



$$
\boxed{\begin{aligned}
L_{d,\beta,\gamma}={}&zD\,\partial^3
-\bigl[(z+3d+2)D-4z^2\bigr]\partial^2\\
&+\bigl[(2d-2)z^2+\beta z+\gamma\bigr]\partial\\
&-d(d-1)z+2d^2(d-1)-d\beta.
\end{aligned}}
\tag{8}
$$



In particular the absence of a nonconstant accessory factor does
not mean that all scalar accessory coefficients have disappeared.

The polynomial exponential condition also gives the exact top
coefficient relation



$$
\boxed{\beta=3d^2-d+\frac{b_{d-1}}{b_d}.}
\tag{9}
$$



It follows by taking the coefficient of (z^{d+1}\) in
(L^{[1]}B\); its two contributions are
(-b_{d-1}+(\beta-3d^2+d)b_d\). Formula (9) uses the unit (b_d\)
from (3), and includes (d=0\) by the missing-coefficient convention.

## 3. A separate logarithmic pole compatibility

For the operator (8), let (f_1=D^{-1}\), (f_2=f_1'\), and
(f_3=f_1''\). Define the rational forcing, without an arctangent
function over (K\), by



$$
\mathcal T_L(C)=
(3L_3C''+2L_2C'+L_1C)f_1
 +(3L_3C'+L_2C)f_2+L_3Cf_3.
\tag{10}
$$



Direct simplification gives the particularly small expression



$$
\boxed{\begin{aligned}
\mathcal T_L(C)={}&3zC''-2(z+3d+1)C'+2dC\\
&+\frac{-2C'+[(\beta+6d+2)z+\gamma-2d]C}{D}.
\end{aligned}}
\tag{11}
$$



This identity was checked symbolically with arbitrary (C(z)\)
and symbolic (d,\beta,\gamma\); it is a rational differential
identity, not a numerical test.

Since (LA\) is a polynomial, an extremal triple necessarily
satisfies the two residue conditions encoded by



$$
\boxed{D\mid
2C'-[(\beta+6d+2)z+\gamma-2d]C.}
\tag{12}
$$



This is meaningful over (K\) whether or not (D\) splits there.
Over its splitting field, (2) and the explicit numerator formula
imply (C(\pm i)\ne0\); otherwise (N(\pm i)=0\), contrary to
(2). Thus (12) also prescribes the two logarithmic derivatives



$$
2\frac{C'(\xi)}{C(\xi)}
=(\beta+6d+2)\xi+\gamma-2d,
\qquad \xi=\pm i.
\tag{13}
$$



These conditions are additional to the local exponent lists.
The latter remain (0,1,M\) at the origin and (0,0,1\) at the
two zeros of (D\). They do not select the particular polynomial
(C\) as the logarithmic coefficient, and consequently do not
replace (12).

## 4. An exact finite-jet compatibility formulation

For (p>M-1\), existence of an extremal triple is equivalent to
the following system for some $\beta,\gamma\in K$ and
(A,B,C\in K[z]\) of degree at most (d\), with (B,C\ne0\):



$$
\begin{gathered}
LC=0,\qquad L^{[1]}B=0,\qquad LA+\mathcal T_L(C)=0,\\
A(0)+B(0)=0,\qquad
A'(0)+B'(0)+B(0)+C(0)=0.
\end{gathered}
\tag{14}
$$



The rational identity in (14) includes (12); after multiplying
by (D\), all equations are polynomial equations over (K\).
Necessity was proved above. Here is the finite-jet sufficiency.

For the finite Taylor polynomials through (M-1\),



$$
E_T^{(j)}-E_T=O(z^{M-j}),\quad 1\le j\le3,
$$



and the corresponding differences between (F_T^{(j)}\) and
(f_j\) have the same lower bounds. The leading coefficient
(L_3=zD\) has a factor (z\). Hence the polynomial identities
in (14) imply



$$
L(A+BE_T+CF_T)=O(z^{M-2}).
\tag{15}
$$



For an unknown coefficient of (z^k\), the coefficient multiplying
it at degree (z^{k-2}\) is exactly



$$
I(k)=k(k-1)(k-M).
$$



This is a unit in (K\) for every (2\le k\le M-1\), since
(p>M-1\). Starting from the two zero initial coefficients in
(14), triangular induction in (15) therefore gives (1). This
argument is valid even when (p=M\); it never divides by (M\)
or claims existence of a full exponential power series. The
nonzero numerator lemma and its degree bound then recover (2).

This equivalence does not assume generic normality or distinct
accessory roots. It is still an algebraic compatibility problem,
not an exclusion theorem.

## 5. Why the remaining parameters cannot simply be dropped

For every choice of $\beta,\gamma$, (8) maps



$$
L:\mathcal P_d\longrightarrow\mathcal P_{d-1}.
\tag{16}
$$



Indeed the raising coefficient vanishes at degrees (d,d-1\),
and (7) also removes the degree-(d\) output of the leading
degree-(d\) monomial. Dimension counting alone therefore
provides a nonzero polynomial (C\) with (LC=0\) for **every**
pair of accessory parameters. Merely finding such a polynomial,
or citing its local exponents, imposes no restriction on them.
The residue condition (12), the exponential polynomial condition,
and the remaining equations in (14) must be retained.

There is an explicit two-polynomial necessary condition from
the exponential branch. Normalize (b_d=1\). The coefficient
of (z^{m+2}\) in (L^{[1]}z^m\) is (m-d\). Consequently its
coefficients at degrees (d+1,d,\ldots,2\) recursively determine
(b_{d-1},\ldots,b_0\). The divisions are only by
(-1,\ldots,-d\), all units here. Each coefficient (b_{d-r}\)
is a polynomial in $\beta,\gamma$, over the localization
with these denominators, of total degree at most (r\).

The two remaining coefficients, at (z^1,z^0\), give explicit
polynomials



$$
E_{d,1}(\beta,\gamma)=E_{d,0}(\beta,\gamma)=0,
\qquad \deg E_{d,j}\le d+1.
\tag{17}
$$



Their degrees grow with (d\). The equations (17) alone do not
imply the separate (C\)-pole conditions or the full system (14).
No assertion that they have finitely many roots in every
characteristic, or that their resulting elimination ideal has only
small-prime content, is made here. Producing such an elimination
identity is the precise remaining arithmetic step.

## 6. Exact exclusions in the two smallest extremal degrees

For (d=0\), the numerator of any constant triple with (B,C\ne0\)
is



$$
N(A,B,C)=BC^2(D+D')=BC^2(z+1)^2.
$$



It cannot equal a nonzero multiple of (z^2\) in odd
characteristic. Thus the extremal triple is impossible for
(d=0,p>3\).

For one predeclared nonconstant check, (d=1\), **all** the
coefficient equations at (k=2,\ldots,6\) must be retained.
After multiplying the (k\)-th row by (k!\), their matrix in
((b_0,b_1,c_0,c_1)\) is



$$
\begin{pmatrix}
1&2&0&2\\
1&3&-2&0\\
1&4&0&-8\\
1&5&24&0\\
1&6&0&144
\end{pmatrix}.
\tag{18}
$$



The maximal minors from rows (k=2,3,4,5\) and
(k=2,3,4,6\) are respectively 196 and 648, and



$$
43\cdot196-13\cdot648=4.
\tag{19}
$$



Thus (18) has full column rank modulo every odd prime. Since all
row clearers are units for (p>6\), no extremal degree-one triple
exists at any allowed prime. For completeness its other three
maximal minors are 4468, 7776 and 3760; their total gcd is 4.

A preliminary subminor calculation omitted the (k=2\) row,
which would have allowed a spurious candidate prime 47. That row
is exactly the requirement that the reconstructed (A\) also
have degree at most one. Restoring it gives (18)–(19), so the
subminor observation supplies no counterexample. No prime scan
was performed, and no degree beyond this predeclared (d=1\)
check was sampled.

Consequently the exceptional minimal-degree subspace is zero for
(n=1,2\) at every (p>3n\). The reviewed nullity argument then
gives full row rank of the unbordered (H_n\) in these two
degrees. These finite-degree all-prime exclusions are not being
extrapolated to arbitrary (n\).

## 7. Remaining target

The monomial numerator leaves the two scalar accessories
$\beta,\gamma$, and their polynomial/rational compatibility is
now explicit. A useful all-degree exclusion would show that the
full system (14), or an equivalent saturated elimination ideal
using (12) and (17), has no solution in characteristic
(p>3d+3\). No such identity has been proved here.

In particular, applying characteristic-zero no-log reasoning at
the formal exponent (M\), dropping the polynomial (A\) degree
condition, or discarding the residues at $\pm i$ would each
remove a real part of the problem. The current result exposes
the remaining compatibility rather than assuming it away.
