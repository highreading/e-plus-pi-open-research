> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of finite accessory freeness and the norm carrier

Date: 2026-09-13. Reviewer: audit_sources.

Reviewed in full: raw_accessory_finite_algebra_and_norm_carrier.md. **All three theorems pass**, including freeness over $\mathbb Z[1/d!]$, the full local quotient $\mathbb Z_p/(p^f)$, and both inequalities for the norm-content carrier. No mathematical correction is required.

The review checks the actual normalization and prime support, rather than only the generic dimension over $\mathbb Q$. No new degree or prime scan was used.

## 1. Actual conjugation and the highest weighted forms

I independently expanded $L^{[1]}$. Its four coefficients, in descending differential order, are



$$
\begin{aligned}
&z(1+z^2),\\
&2z^3+(2-3d)z^2+2z-3d-2,\\
&z^3+(2-4d)z^2+(\beta+1)z+\gamma-6d-4,\\
&-dz^2+[\beta-d(d-1)]z
+\gamma+2d^2(d-1)-d\beta-3d-2.
\end{aligned}
$$



These agree with the displayed formula. With weights $1,2$ on $\beta,\gamma$, the downward recurrence at its highest weight is



$$
r h_r=\beta h_{r-1}+\gamma h_{r-2}.
$$



Induction shows that all other contributions have smaller weight, and the leading part of $b_{d-r}$ is $h_r$. In the first unsolved coefficient, the actual prefactor $d!$ gives



$$
d!(\beta h_d+\gamma h_{d-1})
=(d+1)!h_{d+1}=P_{d+1}.
$$



This is an identity between integer polynomials. It does not divide by $d+1$. The second unsolved coefficient has highest part $d!\gamma h_d=\gamma P_d$. Thus both leading forms have exactly the stated monic normalization; there is no missing scalar factor or an unallowed denominator.

The exponential notation defining $h_r$ is only a way to specify finite rational polynomials. The integral recurrence for $P_r$ makes sense at every prime, and its later reductions invert only numbers at most $d$.

## 2. The monic leading Gröbner basis over the localized integers

Let $A=\mathbb Z[1/d!]$. Each



$$
G_j=\gamma^jP_{d+1-j}
$$



has highest monomial $\beta^{d+1-j}\gamma^j$, of coefficient 1, for the stated weight-then-$\beta$-exponent order. The identities



$$
\gamma G_j-\beta G_{j+1}=(d-j)G_{j+2}
$$



use only the units $d,d-1,\ldots,1$ to generate all $G_j$ from $G_0,G_1$.

The telescoping formula for a nonadjacent S-pair is correct. After inserting the adjacent identity, each resulting monomial multiple of $G_{r+2}$ has the same total weight as the original least-common-multiple monomial, and $\beta$-exponent exactly two lower. Thus it is a standard representation by smaller monomials. The final adjacent pair has zero remainder. Buchberger's criterion is valid here because every divisor is monic; coefficient division by a nonunit is unnecessary.

The leading monomial ideal consists of all monomials of total ordinary degree at least $d+1$. Its standard monomials are consequently exactly



$$
\{\beta^a\gamma^b:a+b\le d\},
$$



of cardinality $D_d=(d+1)(d+2)/2$. This remains true in characteristics $d+1$ or $d+2$ when those integers are prime. Neither integer is inverted.

One can also prove the needed coprimality directly over $A$, avoiding any ambiguity about descent from $\mathbb Q$. If an irreducible element divides both $P_{d+1}$ and $\gamma P_d$, it cannot divide $\gamma$, since $P_{d+1}$ has monic top term $\beta^{d+1}$. It therefore divides $P_d$. The recurrence descends to $P_{d-1},\ldots,P_0$, using only the units $d,\ldots,1$, and gives a contradiction. A constant prime factor is likewise excluded by the monic top term.

## 3. The filtered argument really gives freeness

The possible hidden issue is a lower-weight relation in the actual ideal that is absent from its two leading generators. The note's syzygy argument excludes it over the ring $A$, not merely over its fraction field.

For $H=uE_1+vE_0$, if the two highest possible weighted contributions cancel, their homogeneous parts satisfy



$$
u_{\rm top}G_0+v_{\rm top}G_1=0.
$$



The UFD property of $A[\beta,\gamma]$ and the coprimality just checked imply



$$
(u_{\rm top},v_{\rm top})=t(G_1,-G_0)
$$



with $t\in A[\beta,\gamma]$. Since both leading generators are homogeneous for the weight, $t$ can be taken homogeneous of the required weight. Subtracting $t(E_0,-E_1)$ from the representing pair strictly lowers the largest weighted degree of its two summands. It preserves $H$, and the nonnegative integer weights ensure termination.

Hence the full weighted initial ideal is exactly $(G_0,G_1)$. The recursive lifts $F_j$ have highest weighted part $G_j$: their defining division is by the unit $d-j$, and the lower-weight errors stay strictly below the new leading weight. Monic reduction therefore spans the actual quotient by the stated standard monomials.

A nonzero $A$-linear relation among those monomials in the actual ideal would have a highest weighted part supported on standard monomials in the leading ideal. The monic Gröbner basis excludes it. This proves linear independence over $A$, including the absence of integer torsion, and thus finite freeness of rank $D_d$.

Consequently the multiplication matrices and their monic characteristic polynomials are defined over $A$. Their construction introduces only small-prime denominators. The two-equation algebra may be nonreduced; none of the argument requires simple roots.

## 4. The full finite local quotient

Fix $p>3d+3$, write $R=\mathbb Z_p$, and let $f=v_p(F_{d+1})$. The four-equation algebra $S$ is finite over $R$ by the previous theorem. It is torsion because its generic fiber has no geometric point: a characteristic-zero common zero would reconstruct a forbidden nonzero extremal triple for the full-rank actual matrix $X_n$.

For $f=0$, the residue-field equivalence gives $S/pS=0$; Nakayama's lemma gives $S=0$. For $f>0$, the unique geometric accessory point is rational over $\mathbb F_p$, by the one-dimensional actual kernel and the exact parameter recovery from the monic $B$. Thus $S$ is a local Artinian ring. This conclusion does not presume it is reduced.

The universal parameters in this local ring satisfy the four equations. The residue-field unit minor of $U_d$ and the unit initial determinant are units in $S$; the reviewed reconstruction therefore produces the universal actual triple with top $B$-coefficient 1.

Apply a fixed Smith form of $X_n$ over $R$. After its invertible coordinate change, every coordinate of this vector is zero except the final coordinate $y$, which satisfies $p^f y=0$. The top $B$-functional is $uy$, where $u\in R^\times$ because the corresponding nonzero residue-field kernel vector has unit top $B$-coefficient. Normalization fixes $y=u^{-1}$, an actual constant, and forces $p^f=0$ in $S$.

All $B,C$ coordinates are therefore constants from $R$. The exact identities



$$
\beta=3d^2-d+b_{d-1},\qquad
\gamma=2d+2+2b_{d-2}-b_{d-1}^2-2b_{d-1}
$$



make both generators of $S$ constants as well. Thus $R\to S$ is surjective with kernel containing $(p^f)$. The actual monic approximate triple modulo $p^f$, supplied by the Smith form and the reviewed necessity direction, gives an $R$-algebra map $S\to R/(p^f)$. These two maps force the kernel to equal $(p^f)$.

The resulting isomorphism $S\simeq R/(p^f)$ is a global finite-algebra statement over $R$. It does not follow merely from counting congruence solutions; the universal reconstruction and Smith argument establish it directly.

## 5. The norm polynomial is nonzero, with all multiplicities retained

The residue multiplication matrices have entries in $A$, so



$$
\mathcal N_d(t)=\det(M_{R_0}+tM_{R_1})
$$



has coefficients in $A$ and degree at most $D_d$. Over an algebraically closed characteristic-zero field, the finite algebra splits into local Artinian factors. On the maximal-ideal filtration of each factor, multiplication has the scalar value $R_0(x)+tR_1(x)$ on each composition factor. Its determinant is that scalar to the length of the factor. Hence the product formula in the note retains the correct multiplicities even at nonreduced points.

There is no common zero of both residues on the exponential locus in characteristic zero, by the actual full-rank theorem. Every linear factor in that product is therefore a nonzero polynomial in $t$, proving that the norm polynomial is not identically zero. Clearing denominators requires only primes at most $d$, so it does not change any allowed large-prime valuation.

## 6. Both directions of the norm-content comparison

Write $c=v_p(c_d)$.

For the lower inequality, when $f>0$, evaluation at the actual point modulo $p^f$ is a unital functional on the finite free exponential algebra. Its row in the monomial basis is primitive because the first basis element is 1. It left-annihilates both residue multiplication matrices modulo $p^f$. Lifting this row to $R$ and completing it to an invertible row matrix gives a first row of the entire determinant pencil divisible coefficientwise by $p^f$. Therefore $c\ge f$. When $f=0$, this inequality is immediate and needs no evaluation into the zero ring.

For the upper inequality, the exact quotient $S\simeq R/(p^f)$ gives an equality



$$
p^f=aR_0+bR_1
$$



inside the integral finite exponential algebra. Every geometric evaluation of $a,b,R_0,R_1$ over $\overline{\mathbb Q}_p$ is integral over $R$, because the algebra is finite. Thus at every geometric point $x$, including every component away from the actual residue point,



$$
0\le\min(v_p(R_0(x)),v_p(R_1(x)))\le f.
$$



The Gauss valuation of a polynomial over a valued field is additive under multiplication. Applying it to the norm factorization, with each local length $m_x$, gives



$$
c=\sum_xm_x\min(v_p(R_0(x)),v_p(R_1(x)))
\le D_df.
$$



Ramified valuations at individual points may be fractional, but the sum is the integer minimum coefficient valuation of a polynomial over $\mathbb Q_p$. The proof retains all components and nilpotent multiplicities. For $f=0$, the displayed ideal equality is $1=aR_0+bR_1$; every minimum is then zero, and the upper bound correctly gives $c=0$.

This proves both inequalities and exact agreement of large-prime support. The square-zero example in the note correctly shows why equality of exponents cannot be inferred: in $R[x]/(x^2)$, the quotient by $x,p^f$ is $R/(p^f)$, whereas the norm pencil has coefficient content $p^{2f}$.

## 7. Scope

The result gives actual finite elimination, an explicit free basis, a global scalar local quotient, and a nonzero norm-content carrier with controlled multiplicity loss. It does not bound the size of the carrier, prove that its large-prime part vanishes, or make the norm easier to compute than the original determinants. Those limitations are accurately stated in the note.

No mathematical correction is required. An optional editorial clarification is to state “for $f>0$” at the start of the lower-bound evaluation argument and treat $f=0$ by the immediate inequality, as done here.
