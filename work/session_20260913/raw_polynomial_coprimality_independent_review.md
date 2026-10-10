> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of polynomial coprimality and modular common factors

Date: 2026-09-13. Reviewer: audit_sources. **PASS.** No correction is
required in `raw_polynomial_coprimality_and_modular_common_factor.md`.
This review also records the precise remaining room for repeated
roots of the actual cubic Wronskian.

## 1. Characteristic-zero coprimality

The use of the actual normalized endpoint, rather than only Taylor
normality, is sound. A common monic divisor (H\in\mathbb Q[z]\)
has degree (1\le d\le n\), since (B,C\ne0\) and their degrees
are at most (n\). Because (B_n(1)=1\), (H(1)\ne0\). Put
(r=\operatorname{ord}_0H\le d\) and (m=n-d\ge0\).

The divided triple is a nonzero rational triple of degree at most
(m\), preserves (C(1)=4B(1)\), and has remainder order at least



$$
3n+1-r\ge3(n-d)+1.
$$



The previously proved bordered uniqueness therefore places it on
the canonical degree-(m\) line. Its (B(1)\) is nonzero, so its
endpoint ratio equals both the degree-(n\) and degree-(m\)
ratios. Equal rational numbers have equal positive reduced
denominators. This contradicts the strictly increasing integer
sequence



$$
j+2\left\lfloor\frac{j+2}{4}\right\rfloor
=v_2(q_j).
$$



This uses the **proved all-index primitive endpoint valuation**,
not the older finite pattern or the valuation of an unnormalized
cofactor. The case (m=0\) is covered by the explicit degree-zero
triple ((-1,1,4)\) and (v_2(q_0)=0\). The argument establishes
the gcd of all three polynomials, without asserting pairwise
coprimality.

A common complex root would be algebraic because, for example,
(B\in\mathbb Q[z]\) is nonzero; its rational minimal polynomial
would divide all three polynomials. Hence the stated absence of
a common complex root follows. There is no hidden assumption that
a putative common factor is linear or already split over
$\mathbb Q$.

## 2. The degree bound is an integer polynomial identity

Let the divided triple ((a,b,c)\) have degree at most (m\), and
write (D=1+z^2\). Its numerator is the determinant



$$
N(a,b,c)=\det\begin{pmatrix}
D^2a&b&c\\
D^2a'+Dc&b+b'&c'\\
D^2a''+2Dc'-D'c&b+2b'+b''&c''
\end{pmatrix}.
$$



In the naive degree count, the only possible terms of degree
(3m+3\) combine into the high-degree part of



$$
D^2(b+2b'+b'')(ca'-ac').
$$



For polynomials of degree at most (m\),
$\deg(ca'-ac')\le2m-2$: if both have degree (m\), the two
degree-(2m-1\) coefficients cancel exactly, and if either degree
is smaller the same bound is immediate. For (m=0\) this
expression vanishes. All other determinant terms have degree at
most (3m+2\). Thus



$$
\deg N(a,b,c)\le3m+2
$$



holds by an identity over the integers. In particular, the
cancellation does not involve division by (m\), a factorial, or
a coefficient which might vanish in characteristic (p\).

## 3. Modular truncation, the gcd bound, and the origin exception

For an arbitrary nonzero modular raw high-kernel triple, the
reviewed Vandermonde and parity-Cauchy arguments imply (B,C\ne0\)
when (p>3n\). Dividing them by a common polynomial (H\) leaves
(b,c\ne0\), so the characteristic-(p\) residue and logarithmic-
derivative lemma gives (N(a,b,c)\ne0\). This does not appeal to
the false general characteristic-(p\) Wronskian independence
criterion.

Here is an explicit justification of the truncation after
division. Work with the finite polynomials



$$
E_T=\sum_{j=0}^{3n}\frac{z^j}{j!},\qquad
F_T=\sum_{\substack{1\le j\le3n\\j\ {
m odd}}}
\frac{(-1)^{(j-1)/2}z^j}{j}
\quad\text{over }\mathbb F_p.
$$



Their coefficients exist because (p>3n\). The raw Taylor
condition says (A+BE_T+CF_T=O(z^{3n+1})\). Polynomial division
by (H\) is exact in this identity:



$$
A+BE_T+CF_T=H(a+bE_T+cF_T).
$$



Thus the divided expression has order at least
(M=3n+1-r\), without assuming that (H(0)\ne0\) or using an
infinite exponential series in characteristic (p\).

The error orders are



$$
E_T'-E_T=O(z^{3n}),\qquad E_T''-E_T=O(z^{3n-1}),
$$




$$
F_T'-D^{-1}=O(z^{3n}),\qquad
F_T''-(D^{-1})'=O(z^{3n-1}).
$$



The factor (E_T(0)=1\) is a formal unit. Substituting into the
Wronskian identity and eliminating the (F_Tc\) column changes
the rational determinant numerator only by
(O(z^{3n-1})\). Since (M-2\le3n-1\), the two derivatives of
the divided remainder give



$$
\operatorname{ord}_0N(a,b,c)\ge M-2=3n-r-1.
$$



No coefficient involving $(3n+1)!$ is needed, including when
(p=3n+1\). Comparing this order with the degree in §2 gives



$$
3n-r-1\le3(n-d)+2,
\qquad 3d-r\le3,
\qquad 2d\le3.
$$



Therefore (d\le1\). The proof begins with the gcd over
$\mathbb F_p[z]$, not a selected algebraic root. Its degree
bound consequently excludes irreducible common factors of degree
at least two, and excludes multiplicity at least two at a common
root. Any common root is in $\mathbb F_p$.

If (H=z-a\) with (a\ne0\), the quotient numerator has order
at least (3n-1\) and degree at most (3n-1\), so it is a nonzero
multiple of (z^{3n-1}\). The covariance (N(Ha,Hb,Hc)=H^3N(a,b,c)\)
then yields exactly (Q=q_3(z-a)^3\), (q_3\ne0\).

If (H=z\), its quotient numerator instead has the form



$$
N(a,b,c)=z^{3n-2}(\alpha+\beta z),
\quad(\alpha,\beta)\ne(0,0),
$$



and hence



$$
Q=z^2(\alpha+\beta z).
$$



This confirms the stated (z^2\mid Q\) origin exception and
explains why it cannot be replaced by the nonzero-root cubic
formula. The coefficient $\beta$ need not be nonzero for an
arbitrary modular kernel vector.

## 4. What actual coprimality says about repeated cubic roots

The reviewed result does **not** prove squarefreeness of the
actual characteristic-zero cubic. Some additional restrictions
can nevertheless be stated exactly.

First, because (Q_n\in\mathbb Q[z]\) has degree exactly three,
every repeated root is rational. If a repeated root had rational
minimal polynomial of degree at least two, that polynomial's
square would divide the cubic. In particular any roots at
$\pm i$ are automatically simple. This restriction follows
from rationality and cubic degree alone.

Next let $\rho\ne0,\pm i$ be a root of multiplicity (h\) of
(Q_n\). Choose any local analytic branch of arctangent. The
functions (R_n,B_ne^z,C_n\) have no common zero there: if all
three vanished, then (B_n(\rho)=C_n(\rho)=0\) and hence also
(A_n(\rho)=0\), contradicting polynomial coprimality.

Their local echelon orders therefore begin with zero, say
(0<l_1<l_2\). The characteristic-zero Vandermonde calculation of
the Wronskian gives



$$
h=l_1+l_2-3.
$$



For the possible repeated multiplicities, this leaves exactly

| Cubic-root multiplicity | Possible local echelon orders |
|---:|---|
| 2 | $(0,1,4)$ or $(0,2,3)$ |
| 3 | $(0,1,5)$ or $(0,2,4)$ |

Coprimality excludes the common-zero pattern $(1,2,3)$ for a
triple root, but it does not exclude the displayed alternatives.
These are failures of independence of certain derivative
evaluations, not common zeros of the coefficient polynomials.

At the origin the prefactor $z^{3n-1}$ must instead be retained.
The low constant equation is (A_n(0)=-B_n(0)\), so coprimality
implies that (B_n(0),C_n(0)\) are not both zero. The two analytic
solutions (B_ne^z,C_n\) have echelon orders (0,l_1\), and the
high remainder has order (M\ge3n+1\). Their two-function
Wronskian gives (l_1\le2n+1<M\), so the full orders are
(0,l_1,M\). If (h_0=\operatorname{ord}_0Q_n\), the exact ledger
becomes



$$
M+l_1=3n+2+h_0,\qquad 1\le l_1\le h_0+1\le4.
$$



This is a genuine sharpening of the origin data, but still allows
positive, including repeated, origin multiplicity for (Q_n\).

An exact illustration of the logical obstruction already occurs
in the actual degree-zero seed. For ((A,B,C)=(-1,1,4)\), whose
polynomial gcd is one, formula §2 gives



$$
N(-1,1,4)=16(D+D')=16(z+1)^2.
$$



Thus even within the same exponential/arctangent system an
ordinary Wronskian numerator can have a double root while the
three coefficient polynomials have no common root. This seed
example is not evidence for or against squarefreeness in later
canonical degrees; it shows why the proposed converse cannot be
used as a general Wronskian principle.

The remaining squarefreeness target is an actual new local-rank
or discriminant statement excluding the displayed derivative
patterns, equivalently proving $\gcd(Q_n,Q_n')=1$. Neither
polynomial coprimality nor the finite-field common-factor bound
alone supplies that statement. No additional canonical degree was
computed in this review.
