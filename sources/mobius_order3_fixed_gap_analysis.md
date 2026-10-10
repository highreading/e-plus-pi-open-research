> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Möbius and order-three structure of the fixed-gap cubic obstruction

Date: 2026-08-28

## 1. Scope and conclusion

Let



$$
n=q-1,\qquad A=2q-3,\qquad \alpha=A/3,
$$



where $q$ is positive, odd, and $3\nmid q$.  This note rewrites the
fixed-gap coefficients $C_s,T_s$ as two endpoint residues of one
algebraic differential and identifies the exact contiguity between the
rows $s=0,1$.

There is a genuine order-three symmetry, but it does **not** preserve the
two endpoint poles.  The actual coefficient transform carrying the
$T_s$ endpoint to the $C_s$ endpoint is the involution $z\mapsto2/z$,
not an order-three map.  Consequently the relation
$X^3=4^{q-1}$ does not, by itself, turn the pair
$(\lambda_0,\lambda_1)$ into two eigenfunction coordinates for an
order-three PSL2 action.  A separate jet/Bezout or Cartier argument is
still required for the missing uniform Smith-divisor theorem.

## 2. The two coefficient rows are endpoint residues

For $s\ge0$, put



$$
d_s=1+3s,\qquad \beta_s=\alpha-s
$$



and consider



$$
\omega_s(t)=
 \frac{(1+t)^{d_s}(1+t^2)^{\beta_s}}
      {t^q(1-t)^q}\,dt.                                      \tag{2.1}
$$



The branch at $t=0$ is normalized by
$(1+t^2)^{\beta_s}=1+O(t^2)$.  Then the fixed-gap tail coefficient is



$$
\boxed{T_s=\operatorname {Res}_{t=0}\omega_s}.              \tag{2.2}
$$



Fix the continuation of this branch through the changes of coordinate
below, and write $a=2^\alpha$ for the resulting value, so
$a^3=2^A$.  Every occurrence of $2^{\pm\alpha}$ in (2.3)--(2.6) uses
this same choice; it is not an independently chosen cube root.

For the other endpoint, use



$$
H(z)=(1+z)(1+z+z^2/2),\qquad R(z)=z^2+2z+2,
$$



and



$$
\phi(z)=\frac z{z+2},\qquad \iota(z)=\frac2z.
$$



Direct substitution gives



$$
\phi^*\omega_s=
 2^{1+2s-q/3}
 \frac{(z+1)^{d_s}(z+2)^{\beta_s}R(z)^{\beta_s}}
      {z^q}\,dz.                                             \tag{2.3}
$$



On the other hand, the differential whose residue is $C_s$ is



$$
\gamma_s(z)=2^{-s}
 \frac{(z+2)^{d_s}H(z)^{\beta_s}}{z^q}\,dz,
 \qquad C_s=\operatorname {Res}_{z=0}\gamma_s.               \tag{2.4}
$$



Using



$$
\iota(z)+1=\frac{z+2}{z},\quad
 \iota(z)+2=\frac{2(z+1)}z,\quad
 R(\iota(z))=\frac{2R(z)}{z^2},
$$



and $3\alpha=2q-3$, all powers of two and $z$ cancel exactly:



$$
\boxed{\gamma_s=-2^{-\alpha}\,\iota^*(\phi^*\omega_s).}     \tag{2.5}
$$



Since $\iota(0)=\infty$ and $\phi(\infty)=1$, residue invariance
under a Möbius change of coordinate yields



$$
\boxed{C_s=-2^{-\alpha}\operatorname {Res}_{t=1}\omega_s.} \tag{2.6}
$$



Here and below, $2^\alpha$ denotes the branch induced by the normalized
branch of $(1+t^2)^{\beta_s}$ used in (2.1)--(2.6).  Thus the later
notation $a=2^\alpha$ is synchronized with this residue identity, rather
than chosen independently up to a cube root of unity.

Formula (2.6) is also the exact coefficient-reflection identity hidden in
the full-and-tail construction.  It is uniform in $s$; in particular it
applies to $s=0,1$.

## 3. Exact contiguous formulation of $\lambda_0,\lambda_1$

Let $X^3=4^n$, use the branch-synchronized $a=2^\alpha$ fixed above,
and put



$$
\xi=X/a.
$$



Then



$$
\boxed{\xi^3=2^{2n-A}=2.}                                  \tag{3.1}
$$



With



$$
\mathcal L_\xi(\eta)=
 \operatorname {Res}_{t=0}\eta+
 \xi\operatorname {Res}_{t=1}\eta,
$$



equations (2.2) and (2.6) give the exact identity



$$
\boxed{\lambda_s=XC_s-T_s=-\mathcal L_\xi(\omega_s).}       \tag{3.2}
$$



The two rows are contiguous because



$$
\boxed{\omega_{s+1}=g(t)\omega_s,\qquad
 g(t)=\frac{(1+t)^3}{1+t^2}.}                                \tag{3.3}
$$



Thus simultaneous vanishing is precisely



$$
\mathcal L_\xi(\omega_0)=
 \mathcal L_\xi(g\omega_0)=0,
 \qquad \xi^3=2.                                            \tag{3.4}
$$



This is a useful exact reformulation: the cubic relation has become a
constant Kummer value at the second endpoint.

Equivalently, on the elliptic Kummer curve



$$
E:\quad y^3=1+t^2,
$$



one can write



$$
\omega_s=
 \frac{(1+t)^{1+3s}y^{A-3s}}
      {t^q(1-t)^q}\,dt,
 \qquad
 g=\left(\frac{1+t}{y}\right)^3.                            \tag{3.5}
$$



This model must not be conflated with the earlier presentation
$E_Q:Y^3=Q(z)=(1+z)(1+z^2)$.  The curve in (3.5) is the Kummer model
obtained by isolating the fractional factor $(1+t^2)^{\beta_s}$ in the
fixed-gap endpoint differential.  Its branch locus on the base is
$\{i,-i,\infty\}$, with infinity essential.  The earlier $E_Q$ model
has a different base coordinate, branch presentation, and pole divisor.
The two genus-one cyclic cubic covers are birational over an algebraic
closure after a Möbius change of their three branch points, but none of
the endpoint or regularity assertions here may be transferred between the
models without also transporting the differential and its pole divisor.

The deck transformation $y\mapsto\zeta y$ acts on every
$\omega_s$ through the same character $\zeta^A$.  This is a genuine
order-three eigenspace statement.  However, $\xi$ in (3.2) is a relative
weight between two different endpoint orbits; it is not the deck
eigenvalue.

### Exact bridge to the existing inverse-cubic map

The Möbius coordinate



$$
S=\frac2{1+t}
$$



puts (3.3) into the already studied inverse-cubic normal form.  Namely, if



$$
\phi(S)=S^3-2S^2+2S=S(S^2-2S+2),
 \qquad
 A_0(S)=(S-1)(2-S),
$$



then direct substitution gives



$$
\boxed{g(t)=\frac4{\phi(S)},\qquad
 t=0,1\longleftrightarrow S=2,1.}                    \tag{3.6}
$$



The whole differential becomes



$$
\boxed{
 \omega_s=
 -2^{1+2s-q/3}
 \frac{\phi(S)^{\alpha-s}}{A_0(S)^q}\,dS.}            \tag{3.7}
$$



Consequently,



$$
\frac{\omega_{s+1}}{\omega_s}=\frac4{\phi(S)}.       \tag{3.8}
$$



Thus the Möbius/Kummer formulation lands exactly on the existing cubic
$\phi(S)=S^3-2S^2+2S$.  It is a coordinate bridge to the inverse-cubic
route, not an independent order-three closure.

## 4. Why the coefficient transform is order two

Assume in this paragraph that $q\ge5$.  After the Cayley change (2.3),
the signed local-exponent divisor of the unscaled $T_s$-differential
consists of

* $z=-1$ with multiplicity $d_s$, and
* $z=-2,-1+i,-1-i$ with multiplicity $\beta_s$,

while the $C_s$-differential has

* $z=-2$ with multiplicity $d_s$, and
* $z=-1,-1+i,-1-i$ with multiplicity $\beta_s$.

Both have their two endpoint poles at $0,\infty$.  The fractional
labels $\beta_s$ are interpreted as integral multiplicities after
pullback to the Kummer cover.  For admissible $q\ge5$ and $s=0,1$,
one has $d_s\ne\beta_s$, so the distinguished zero is intrinsic.  A
Möbius map carrying one divisor pattern to the other must
preserve the set $\{0,\infty\}$, send $-1$ to $-2$, and carry the
remaining three-point set to its counterpart.  The unique such map is



$$
\boxed{\iota(z)=2/z,\qquad
 \begin{pmatrix}0&2\\1&0\end{pmatrix}^{\!2}=2I.}             \tag{4.1}
$$



It is projectively an involution.  This proves directly, at the divisor
level, that the actual $C_s\leftrightarrow T_s$ transform is not an
order-three PSL2 action for $q\ge5$.  The algebraic pullback identity
(2.5) remains valid at $q=1$; only this positive-multiplicity divisor
argument was restricted.

## 5. The genuine base order-three automorphism moves the poles

The branch locus of $E:y^3=1+t^2$ on the $t$-line is
$\{i,-i,\infty\}$.  The two nontrivial order-three elements of the
Möbius group preserving this branch set are inverse to one another.  One
of them is



$$
\sigma(t)=\frac{it+3}{t+i},\qquad
 M_\sigma=\begin{pmatrix}i&3\\1&i\end{pmatrix},
 \qquad M_\sigma^3=8iI.                                    \tag{5.1}
$$



It cycles



$$
i\longmapsto-i\longmapsto\infty\longmapsto i
$$



and satisfies



$$
1+\sigma(t)^2=
 \frac{8i(1+t^2)}{(t+i)^3}.                                \tag{5.2}
$$



Thus it lifts to the Kummer curve after choosing a cube root of $8i$.
But its two endpoint orbits are



$$
\{0,-3i,3i\},\qquad
 \{1,2-i,2+i\}.                                           \tag{5.3}
$$



In particular the pole set $\{0,1\}$ of (2.1) is not invariant.  Since
every nonidentity order-three Möbius symmetry of the branch set is one of
$\sigma^{\pm1}$, no order-three base symmetry preserves both the Kummer
curve and the two-residue problem.  Closing the residue problem under the
full $\sigma$-orbit introduces four new endpoints, so the two equations
(3.4) do not form a closed eigenvector system under this action.

## 6. The exact nonresonance supplied by $P_q$

The proposed Smith bound uses



$$
P_q=\prod_{j=0}^{q-2}(A-3j)
    =3^n n!\binom\alpha n.                                  \tag{6.1}
$$



If a prime $\ell\nmid6P_q$, then necessarily $\ell>n$.  Indeed, if
$\ell\le n$, the range $0\le j\le n-1$ contains a representative of
$\alpha\pmod\ell$, making one factor $A-3j$ zero modulo $\ell$.
Consequently, away from $6P_q$, both $n!$ and every
$\alpha-j$ for $0\le j<n$ are units.  This is the basic Pochhammer
nonresonance condition necessary for a length-$n$ coefficient or jet
reduction; it is not itself such a reduction and does not prove that the
backward process closes.

The Möbius analysis does not supply that backward reduction: it only
separates the two endpoint residues and shows why the tempting
order-three closure is absent.  A proof of $d_3(q)\mid P_q$ still needs
an explicit Bezout identity in the length-$n$ jet module, or an
equivalent Cartier/primitive argument that controls the two distinct
endpoint orbits.

## 7. Status

The theorem-grade identities established here are (2.2), (2.5)--(2.6),
(3.1)--(3.8), (4.1), (5.1)--(5.3), and the nonresonance observation
(6.1).  They give an exact contiguous/Kummer formulation and a rigorous
structural obstruction to the proposed order-three PSL2 shortcut.  They
do not prove the missing uniform divisibility $d_3(q)\mid P_q$.

The standard-library checker
`work/mobius_order3_fixed_gap_certificate.py` independently audits the
endpoint reflection for $s=0,1$, all exponent cancellations in (2.5),
the identity (6.1), the Gaussian matrix cube in (5.1), the cross-multiplied
identity (5.2), and the two endpoint orbits (5.3).  Its default exact run
checks every admissible $q\le301$.  This finite run is a control for the
hand algebra; the uniform assertions rest on the displayed symbolic
identities, not on the checked range.
