> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Large-prime nullity, minimal-degree defects, and Smith content

Date: 2026-09-13. Original bounded continuation by audit_computations.

This note uses the independently reviewed determinant argument in
`raw_large_prime_endpoint_gcd_carrier.md` and its explicit finite-field
bridge in `raw_large_prime_endpoint_gcd_independent_review.md`.
It strengthens the rank information for the high matrix before the
endpoint row and gives an exact local Smith description of its content.
No new degree construction or prime scan is used.

Fix (n\ge1), a prime (p>3n), and write (K=\mathbb F_p).
Let (H_n) be the (2n\)-by-((2n+2)) high coefficient matrix in
the (B,C) coordinates, with the usual integer (k!) row scaling.
Let (J_n) append the row (\ell=C(1)-4B(1)). All polynomial
spaces below include the uniquely reconstructed low polynomial (A).

## 1. A sharp bound on the minimal-degree subspace

Let (V_n=\ker_K H_n), viewed as triples of degree at most (n)
with



$$
A+BE_T+CF_T=O(z^{3n+1}),
\tag{1}
$$



where (E_T,F_T) are the Taylor polynomials through degree (3n).
The carrier review proves for every nonzero member that (B,C\ne0)
individually and that



$$
0\ne\mathcal N(A,B,C),\qquad
z^{3n-1}\mid\mathcal N(A,B,C).
\tag{2}
$$



For a triple of degree at most (d), the universal degree bound is
(\deg\mathcal N\le3d+2). Consequently no nonzero member of
(V_n) has degree at most (n-2).

Let (V_n^-\subset V_n) consist of triples of degree at most (n-1).
Then



$$
\boxed{\dim_K V_n^-\le1.}
\tag{3}
$$



Indeed, (2) and the degree bound force every nonzero such triple (T)
to satisfy



$$
\mathcal N(T)=\kappa z^{3n-1},\qquad \kappa\ne0.
\tag{4}
$$



The universal leading coefficient identity, with degree parameter
(d=n-1), reads



$$
\kappa=b_{n-1}
\bigl(a_{n-1}c_{n-2}-a_{n-2}c_{n-1}+c_{n-1}^{,2}\bigr).
\tag{5}
$$



Missing coefficients are interpreted as zero. In particular the linear
functional (b_{n-1}) is nonzero on every nonzero element of (V_n^-).
It is therefore injective on this vector space, proving (3). Such a
triple has degree exactly (n-1).

## 2. The unbordered high matrix loses at most one row rank

For any three members (T_i=(A_i,B_i,C_i)\in V_n),



$$
\det\begin{pmatrix}A_1&B_1&C_1\\A_2&B_2&C_2\\A_3&B_3&C_3\end{pmatrix}=0
\quad\text{in }K[z].
\tag{6}
$$



To prove this, replace the first column by (A_i+B_iE_T+C_iF_T).
The determinant does not change, and (1) makes it divisible by
(z^{3n+1}). Its original polynomial degree is at most (3n), so it
is zero. This is a polynomial identity and does not need formal
exponentials past the allowed truncation.

Let (\tau:V_n\to K^3) take the three degree-(n) coefficients.
Equation (6), at the leading coefficient, implies
(\operatorname{rank}\tau\le2), while (3) gives
(\dim\ker\tau\le1). Thus



$$
\boxed{2\le\dim_K V_n\le3,
\qquad \operatorname{rank}_K H_n\ge2n-1.}
\tag{7}
$$



The lower bound is ordinary dimension counting. If (\dim V_n=3),
then (V_n^-=KT) for a nonzero triple (T) of degree (n-1),
and (\operatorname{rank}\tau=2). Both (T) and (zT) belong
to (V_n): their degrees are at most (n), and multiplication by
(z) preserves the required Taylor vanishing. They are linearly
independent. Therefore



$$
\boxed{V_n=\operatorname{span}_K\{T,zT,S\}}
\tag{8}
$$



for a suitable third triple (S) of degree (n). The triple (T)
has no nonconstant common polynomial factor. Indeed, let such a
factor (f) have degree (m\ge1) and origin order (h\le m).
The divided triple has degree at most (n-1-m) and remainder order
at least (3n+1-h). The same truncated-jet argument gives its
nonzero determinant origin order at least (3n-1-h): the previously
bounded derivative errors are still of sufficient order. Its degree
is at most (3n-1-3m), which would require (3m\le h), impossible.
Nonvanishing of the determinant is preserved since division does
not make either (B) or (C) zero.

## 3. What the endpoint row adds, and what is not excluded

Since (J_n) adds one row,



$$
\dim\ker J_n=\dim V_n-operatorname{rank}(\ell|_{V_n})\le3.
\tag{9}
$$



This agrees with the bound supplied by the three-row augmented full
rank theorem. The unbordered estimate (7) is additional information.

The only remaining route to nullity three for (J_n) is completely
explicit: (8) must hold and



$$
\ell(T)=0,\qquad \ell(S)=0.
\tag{10}
$$



Since (z=1) at the endpoint, (\ell(zT)=\ell(T)); hence (10)
is equivalent to the endpoint row vanishing on all of (V_n).
The carrier theorem alone does not exclude these two conditions.
They are conditions on a *linear combination* (C(1)-4B(1)), not
the simultaneous vanishing of all three polynomial endpoints.

For example, if (10) holds then ((z-1)T\in\ker J_n) has all
three endpoints zero, and its nonzero top (B) coefficient in (5)
is exactly consistent with the carrier theorem. It is not a
contradiction. Nor does (T\in\ker J_n) have zero endpoints:
that would force a common factor (z-1) in (T), which (4) rules
out. Thus the available arguments do not reduce (9) to a universal
bound of two. This note does not assert that nullity three actually
occurs; an exclusion theorem or a counterexample remains open here.

## 4. At most two nonunit Smith invariants, with an exact local form

The characteristic-zero high matrix has full row rank (2n), since
the reviewed characteristic-zero bordered matrix (J_n) has rank
(2n+1). Over (\mathbb Z_p), (7) says that at most one Smith
invariant of (H_n) is a nonunit. Let its valuation be (e\ge0),
where (e=0) includes the case in which all invariants are units.

After invertible integral row and column operations, (H_n) has
an identity block of size (2n-1) and the final row
((p^e,0,0)) in its three remaining columns; a unit factor has been
absorbed. Apply the same column operations to the endpoint row and
eliminate its first (2n-1) coordinates using the identity rows.
The entire nonunit part of (J_n) is then the explicit matrix



$$
\boxed{\begin{pmatrix}p^e&0&0\\a&b&c\end{pmatrix}.}
\tag{11}
$$



Here (a,b,c\in\mathbb Z_p), and (b,c) are not both zero
because the characteristic-zero bordered matrix has full row rank.
Put (s=\min\{v_p(b),v_p(c)\}\ge0). Its two Smith invariant
valuations are



$$
\boxed{r=\min\{e,v_p(a),v_p(b),v_p(c)\},
\qquad e+s-r.}
\tag{12}
$$



This follows by taking respectively the gcd of entries and the gcd
of its (2\)-by-(2) minors. The latter minors are (p^eb,p^ec,0).
Consequently the full maximal-minor content in the carrier note obeys



$$
\boxed{v_p(\delta_n)=e+s.}
\tag{13}
$$



Here (e) is exactly the valuation of the gcd of the maximal minors
of the *unbordered* high matrix. The quantity (s) is the content of
the endpoint functional restricted to the integral free kernel of
that high matrix, in a primitive basis. It does not depend on the
torsion-coupling entry (a), though (a) affects how the total
valuation is distributed between the two Smith invariants.

In particular, at (p>3n):

- (H_n) has at most one nonunit Smith invariant;
- (J_n) has at most two;
- if (H_n) has full row rank modulo (p), then (J_n) has at
  most one nonunit Smith invariant;
- nullity three for (J_n) is equivalent in (11) to
  (e\ge1) and (a,b,c\in p\mathbb Z_p).

The entry (a) is why merely knowing that the endpoint vanishes on
the two-dimensional *integral* kernel is insufficient to diagnose
the rank in the exceptional reduction: a new modular kernel
direction appears when (e\ge1).

## 5. Exact next arithmetic question

The content has been reduced to one unbordered Smith valuation and
one endpoint restriction valuation. Nothing in the finite-field rank
theorem bounds their sizes: the ranks detect only which invariant
valuations are positive. The next precise alternatives are to prove
that (10) cannot occur for the exceptional minimal-degree triple and
its complementary solution, or to obtain a prime-power bound for
(e+s) in (13). A count of at most two nonunit factors is not a bound
on their exponents and is not an upper estimate for the endpoint gcd.
