> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Accessory pencils, Heine–Stieltjes theory, and two exact pole identities

Date: 2026-09-13. Bounded primary-source audit and original algebra by
audit_sources. This note concerns the actual extremal accessory system;
it does not prove the required bound on its prime-power content.
Independent root audit of the new algebra in Sections3–5:
raw_accessory_pole_and_pcurvature_root_review.md, PASS.

## 1. Actual system and the scope of the comparison

Use the normalization of raw_extremal_four_accessory_equations.md:


$$
D=1+z^2,\quad s=3d+2,\quad p>3d+3,
$$




$$
\begin{aligned}
L={}&zD\partial^3-[(z+s)D-4z^2]\partial^2\\
&+[(2d-2)z^2+\beta z+\gamma]\partial\\
&-d(d-1)z+2d^2(d-1)-d\beta.
\end{aligned}
\tag{1}
$$


The actual branches satisfy $LC=0$ and $L^{[1]}B=0$, where
$L^{[1]}=e^{-z}Le^z=L(\partial+1)$ is an algebraic conjugation of
operators; no full exponential series in characteristic $p$ is needed.
The monic $B$ has degree $d$. The two remaining equations say


$$
2C'-[(\beta+6d+2)z+\gamma-2d]C\equiv0\pmod D.
\tag{2}
$$


The four-equation equivalence, all prime-power depths, finite free
two-equation algebra of rank $\binom{d+2}{2}$, and full local quotient
$\mathbb Z_p/(p^f)$, $f=v_p(F_{d+1})$, have already been separately
proved and reviewed. They are dependencies, not claims established by
the external papers below.

The parameter directions are exactly


$$
L=L_{0,0}+\beta(z\partial-d)+\gamma\partial,\qquad
L^{[1]}=L^{[1]}_{0,0}
+\beta[z\partial+z-d]+\gamma[\partial+1].
\tag{3}
$$


Thus these are derivative parameters. The scalar coefficient of
$L^{[1]}$ has degree two, while its coefficients of
$\partial,\partial^2,\partial^3$ have degrees $3,3,3$.

## 2. Primary theorems and exact applicability

**Shapiro.** *Algebro-geometric aspects of Heine–Stieltjes theory*,
[primary PDF](https://arxiv.org/pdf/0812.4193), printed pp. 3–5,
Theorems 4–6 and Proposition 1. For a fixed operator
$T=\sum_{j=1}^k Q_j\partial^j$, set
$r=\max_j(\deg Q_j-j)$. Nondegeneracy requires
$\deg Q_k=k+r$. In $TS+VS=0$, the unknown $V$ is multiplication
by a polynomial of degree at most $r$. Generic coefficients give
$\binom{n+r}{r}$ distinct solutions of degree $n$; without genericity,
the same multiplicity count for exact degree $n$ requires
$L_n\ne L_j$, $0\le j<n$, for the explicit diagonal coefficients.
Theorem 6 then gives a complete intersection.
Our derivative part has $r=2$ but $\deg Q_3=3\ne5$, and (3) is
not multiplication-only. The operator also changes with $d$.
Consequently neither its nondegenerate counting theorem nor its
nonresonance conclusion proves our result. The matching binomial
number is an analogy, not a theorem identification.

**Brändén.** *A generalization of the Heine–Stieltjes theorem*,
[primary PDF](https://arxiv.org/pdf/0907.0648), printed pp. 2–5,
Theorems 1.3, 1.5, 2.1 and Lemma 2.7. The counting, unique zero-pattern,
coprimality, and interlacing conclusions assume a nondegenerate
hyperbolicity-preserving real operator; additional common-zero
conditions yield simplicity. This is stronger root information in
its applicable class. It does not apply here: besides nondegeneracy
and parameter-direction failures, our leading polynomial
$z(1+z^2)$ is not real-rooted. Lemma 2.7 requires each nonzero
coefficient polynomial of a hyperbolicity preserver to be hyperbolic.
Thus the displayed real operator itself fails that hypothesis.
Rotating $z$ to move the poles onto the real axis changes the other
coefficients and the exponential direction; it does not supply a
positive real operator automatically.

**Scherbak.** *A theorem of Heine–Stieltjes, the Wronski map, and
Bethe vectors in the $\mathfrak{sl}_p$ Gaudin model*,
[primary PDF](https://arxiv.org/pdf/math/0211377), printed pp. 4–7,
Theorems 1–2 and the definition of a nondegenerate polynomial plane;
pp. 8–9, the polynomial-solution setup.
Theorem 1 identifies critical points with nonzero critical values
with nondegenerate planes in the specified Schubert intersection.
Theorem 2 supplies generic-configuration completeness for the stated
tensor products of symmetric powers. The solution plane is a plane
of polynomials, giving a Fuchsian equation, with further conditions
on adjacent Wronskians. Our three branches include one exponential
direction and an arctangent logarithmic direction. There is no
established rational gauge identifying this with its polynomial
plane. Generic configurations would not establish normality at
these fixed singularities, much less a uniform integral depth bound.

**Wakabayashi.** *Gaudin model modulo $p$, Tango structures, and
dormant Miura opers*, 2024 revision,
[primary PDF](https://arxiv.org/pdf/1905.03364), printed pp. 2–4,
Theorem A and condition $(*)_G$; pp. 12–17, Theorem 2.5 and
Propositions 2.8–2.9. For the specified adjoint group
($\mathrm{PGL}_r$ with $r<p$ is allowed), distinct marked/Bethe
points, admissible coweights, and the balance equality, the theorem
identifies Bethe solutions with specified generic Miura opers.
Proposition 2.9 places these in the nilpotent-$p$-curvature locus;
zero weights give the dormant specialization. These are
characteristic-$p$ correspondences, not Smith-depth estimates.
Section 5 below proves that the actual rank-three connection has
non-nilpotent projective $p$-curvature. Thus this particular
correspondence cannot apply directly even before its other
configuration requirements are considered.

**Turbiner.** *Quasi-Exactly-Solvable Differential Equations*,
[primary PDF](https://arxiv.org/pdf/hep-th/9409068), printed pp. 3–5,
Definition 2.1, Lemma 2.1 and Theorem 2.1.
An order-$k$ operator preserving the degree-$\le d$ polynomial
space, for $d>k-1$, is representable by a degree-$k$ polynomial
in the standard projective $\mathfrak{sl}_2$ generators.
The converse is immediate; for smaller $d$, the stated
qualification concerns the part acting on that finite space.
The spectral completeness theorem additionally assumes symmetry.
The preservation statement does apply to $L$, and Section 3 gives
its explicit integral expression, including the small degrees
without a classification appeal. It does not apply as such to
$L^{[1]}$, which need not preserve that space, and no symmetry
or normality of our simultaneous two-branch system follows.

All five PDFs were downloaded and their indicated theorem sections
read. This is a bounded targeted search, not an assertion that all
confluent or irregular Gaudin variants have been exhausted.

## 3. An exact integral $\mathfrak{sl}_2$ expression

Put


$$
E=\partial,\qquad H=z\partial,\qquad F=z^2\partial-dz.
$$


Then $E,H-d/2,F$ are the usual three generators up to the standard
choice of signs. Composition below acts on the rightmost factor
first. The following is an identity of polynomial differential
operators, with integer coefficients in $d,\beta,\gamma$:


$$
\boxed{\begin{aligned}
L={}&-F(H-d+1)\\
&+(H-d)\{H^2-(2d+1)H-2d(d-1)+\beta\}\\
&+E(\gamma+1-H)+E^2(H-3d-4).
\end{aligned}}
\tag{4}
$$


To verify it, apply each side to $z^m$. The only powers are
$z^{m+1},z^m,z^{m-1},z^{m-2}$, with coefficients


$$
\begin{aligned}
&-(m-d)(m-d+1),\\
&m(m-1)(m-3d)+(m-d)\beta+2d^2(d-1),\\
&m(\gamma-m+1),\\
&m(m-1)(m-3d-4),
\end{aligned}
$$


respectively, and these are exactly the coefficients from (1).
Equality on all monomials in characteristic zero proves the
integer Weyl-algebra identity, hence also every reduction.
The universal symbolic coefficient differences and the
pole-determinant remainder in (7) were also checked exactly
in accessory_pole_identity_symbolic_check.py/.json.

For $0\le m\le d$, the degree-$d+1$ coefficient vanishes,
and every degree-$d$ coefficient vanishes as well. Thus
$L:\mathcal P_d\to\mathcal P_{d-1}$, explaining the always-present
polynomial kernel and the rectangular cofactor construction.
This expression does not imply that the cofactor vector meets
(2). The two endpoint functionals in (2) are extra constraints,
not an $\mathfrak{sl}_2$-invariant subspace condition.

## 4. A content-preserving resultant identity at the actual poles

This lemma works over any commutative ring $R$ where $2$ is a
unit. It is particularly valid over $\mathbb Z/p^h\mathbb Z$,
with the actual polynomial triple and its actual normalization.
For polynomials $A,B,C$, define


$$
J=C(B'+B)-C'B
\tag{5}
$$


and the cleared gauged Wronskian


$$
N=D^2\det\begin{pmatrix}
A&B&C\\
A'+C/D&B+B'&C'\\
A''+2C'/D-CD'/D^2&B+2B'+B''&C''
\end{pmatrix}.
\tag{6}
$$


Its apparent denominators cancel, so $N\in R[z]$. Expanding the
first column modulo $D$ leaves only the term with $-CD'$ in
the last row. The cofactor has sign plus and equals
$BC'-(B+B')C=-J$. Hence


$$
\boxed{N\equiv CD'J\pmod D.}
\tag{7}
$$


For the actual extremal triple, the previously proved equality is
$N=\kappa z^s$, with $\kappa=b_d\Xi_d$ a unit modulo $p$.
Consequently in the finite free rank-two algebra $R[z]/(D)$,


$$
CJ=\frac{\kappa}{2}z^{s-1}.
\tag{8}
$$


The determinant norm of $z$ is $1$, and that of the scalar $2$
is $4$. Since $D$ is monic, the norm of $C$ is
$\operatorname{Res}(D,C)$, without a leading-coefficient factor.
Taking norms proves the exact congruence


$$
\boxed{4\,\operatorname{Res}(D,C)\operatorname{Res}(D,J)=\kappa^2.}
\tag{9}
$$


There is no division by the content of $N$, $C$, or $J$.
In particular both resultant factors are units at every actual
allowed residue-field root, and are units at every existing
prime-power lift. Their nonzero square classes agree over
$\mathbb F_p$. No value of that square class has been computed,
so this does not exclude the root.

Equation (2) additionally gives, in a splitting field and with
the roots $a_j$ of $C$ counted with multiplicity,


$$
\boxed{\begin{aligned}
\beta&=-6d-2-2\sum_j\frac1{1+a_j^2},\\
\gamma&=2d-2\sum_j\frac{a_j}{1+a_j^2}.
\end{aligned}}
\tag{10}
$$


Indeed $C'/C=\sum_j(z-a_j)^{-1}$, and the sum and difference
of (2) at $i,-i$ give (10). Equation (8) ensures that no
denominator vanishes. These formulas require no simple-root
assumption. They resemble root equilibrium equations, but their
terms are not known to have one sign.

There is a useful precise multiplicity limit, not squarefreeness.
Over characteristic $p>3d+3$, a root of $C$ away from
$0,\pm i$ has multiplicity at most two: for multiplicity
$m\ge3$, the lowest coefficient of $LC$ comes only from
$zD C'''$, with the nonzero factor $m(m-1)(m-2)$.
At $0$, the indicial factor is $m(m-1)(m-3d-4)$, so a root
has multiplicity at most one. There are no roots at $\pm i$.
Thus an argument requiring every root of $C$ to be simple
still needs a new lemma.

## 5. Direct obstruction to nilpotent-$p$-curvature methods

Let $K$ have characteristic $p>3d+3$, and suppose the actual
four equations have a root. Normalize $L$ to a monic scalar
operator over $K(z)$, and let $\mathsf A$ be its companion
matrix for the column $(y,y',y'')^T$. Define the connection
$\nabla_\partial=\partial-\mathsf A$. The following rational
columns are nonzero:


$$
w=(C,C',C'')^T,\qquad
v=(B,B+B',B+2B'+B'')^T.
$$


Their equations give


$$
\nabla_\partial w=0,\qquad \nabla_\partial v=-v.
\tag{11}
$$


This calculation uses $LC=0,L^{[1]}B=0$, not an exponential
solution in a characteristic-$p$ series ring. They are
independent: proportionality would imply
$(B/C)'/(B/C)=-1$, impossible for a nonzero rational function
because its logarithmic derivative is $O(1/z)$ at infinity.

The restricted $p$-th power of $\partial=d/dz$ on $K(z)$
is zero. One elementary proof writes
$K(z)=\bigoplus_{j=0}^{p-1}K(z^p)z^j$; $\partial^p$
annihilates every summand. Therefore the $p$-curvature is
$\Psi=\nabla_\partial^p$, and (11) implies


$$
\Psi w=0,\qquad \Psi v=-v.
\tag{12}
$$


So its eigenvalues include $0$ and $-1$. Its image modulo
scalar matrices is not nilpotent: a matrix representing a
nilpotent class in $\mathfrak{pgl}_3$, with $p>3$, has all
eigenvalues equal after adding a scalar. The two distinct
eigenvalues in (12) rule this out.

This obstruction survives any rational gauge transformation.
It excludes identification of this actual rank-three connection
with the $p$-nilpotent or dormant connection in the cited
Wakabayashi theorem. It does not exclude a different irregular
theory permitting nonzero semisimple $p$-curvature, and has no
contradiction with the existence of finite exponential jets.

For completeness, the two known branches give a rational
factorization of the monic scalar operator:


$$
\frac L{zD}=
\left(\partial-\frac sz+2\frac{D'}D+\frac{J'}J\right)
\left[\partial^2-\left(1+\frac{J'}J\right)\partial+
\frac{(1+J'/J)C'-C''}{C}\right].
\tag{13}
$$


The bracket annihilates $C$ and the formal gauged branch $B$.
Its Wronskian has logarithmic derivative $1+J'/J$.
The product has the same coefficients of $\partial^3,\partial^2$
as $L/(zD)$; their difference has order at most one and
annihilates the two independent branches. The determinant $J$
then forces that difference to vanish. This proof is algebraic
over the rational function field.

## 6. What this changes, and the next concrete lemma

The higher Heine–Stieltjes count explains why a two-parameter
finite spectral problem is a natural comparison. It supplies no
missing arithmetic normality theorem for this derivative pencil.
The project already has a stronger actual finite-free statement
over $\mathbb Z[1/d!]$ and an exact local quotient.

The new usable items are the explicit integral enveloping-algebra
identity (4), the actual-scale resultant identity (9), the root
sum constraints (10), and the gauge-invariant $p$-curvature
obstruction (12). None bounds $f=v_p(F_{d+1})$.

A bounded next arithmetic target is to express (7)–(9) in the
finite accessory algebra using its canonical cofactor $C^*$
and monic $B^*$, retaining the scalar needed to recover the
actual $C$. A useful result would be an explicit small-prime
unit or controlled-height resultant that contradicts, or bounds
the depth of, its simultaneous pole residues. Merely taking
another norm of (9) cannot do this: both resultants are already
units on the full local root algebra, while the unknown depth is
its vertical thickness. Any argument that replaces this depth
by field reducedness, generic simplicity, or a complex root
count repeats an obstruction already settled in the local
transversality review.
