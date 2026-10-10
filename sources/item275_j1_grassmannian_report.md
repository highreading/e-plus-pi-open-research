> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 275 — exterior-square encoding of the full $j=1$ gate

Checked: 2026-08-31 (Beijing time)

## 1. Scope and verdict

Retain the actual fixed $j=1$ family



$$
p=4h+6s+3,\qquad h,s\ge1,\qquad M=3h+4s+2,                 \tag{1.1}
$$



and the simultaneous gate



$$
Q_0(p,h,s)=Q_1(p,h,s)=0\pmod p.                            \tag{1.2}
$$



Item 273 writes (1.2) as a two-row incidence



$$
G_{h,s}x=0,\qquad x=S_T\in\mathbb F_p^4,                  \tag{1.3}
$$



after exact invertible endpoint transport.  This item replaces the
excluded one-scalar shortcut by the natural exterior-square and
Grassmannian encoding of $\ker G_{h,s}$.

> **PROVED — fixed determinantal recognition.**  On the rank-two chart,
> the kernel is a point of $\operatorname{Gr}(2,4)\subset\mathbb P^5$.
> The collision is the fixed flag incidence $x\in\ker G$.  It has six
> Plücker coordinates, one quadratic Plücker relation, and four displayed
> bilinear incidence coordinates.  On a nonzero decomposable plane, those
> four coordinates impose only two independent conditions.

> **PROVED — exterior-square module.**  Item 273's rank-four parameter
> transport induces a rank-six exterior-square transport.  Its determinant
> is the cube of the rank-four determinant, so it has exactly the same
> fixed singular support and introduces no new exceptional prime factors.

> **PROVED — sharply scoped non-flatness.**  The natural kernel Plücker
> line is not horizontal under either exact $h$- or $s$-transport.  It
> is also non-horizontal under the actual fixed-$M$ step
> $(h,s)\mapsto(h-4,s+3)$.  Exact witnesses make the old and pulled-back
> gate planes transverse, not merely unequal.

This proves that the natural Plücker line is not a rank-one flat subobject
of the Item 273 exterior-square difference module.  It does **not** prove
that no enlarged sheaf, different connection, or finite-field-specific
incidence theorem can work.

> **BOOKING DECISION.**  The fixed flag incidence is codimension two, not
> a divisor, and no weighted distribution theorem for the moving
> arithmetic section is proved.  Item 149 already books the first
> post-Cartier copy.  Hence
>
> 

$$
> \boxed{\text{new \(j=1\) capacity reduction}=0,\qquad
>        \text{new unconditional Route-1 rate}=0.}           \tag{1.4}
>
$$



The raw fixed-$j=1$ ceiling remains $1/36$ per $6M$.  No finite rank
census is used as density evidence.

## 2. Exact kernel Plücker coordinates

Use Item 273's four-coordinate graph state and reduced gate



$$
x=S_T=(f_{T+1},f_T,f_{T-1},f_{T-2})^{\mathsf T},\qquad
 G_{h,s}=A_T+A_EP_{h,s}.                                    \tag{2.1}
$$



Write the rows of $G$ as $g_0,g_1$, and define their six maximal
minors in the order



$$
(12,13,14,23,24,34)
 \quad\text{by}\quad
 \Delta_{ij}=g_{0i}g_{1j}-g_{0j}g_{1i}.                     \tag{2.2}
$$



When $\operatorname{rank}G=2$, the kernel two-plane has the exact
Plücker vector



$$
\boxed{
 K(G)=(\Delta_{34},-\Delta_{24},\Delta_{23},
       \Delta_{14},-\Delta_{13},\Delta_{12}).}               \tag{2.3}
$$



The signs are the Hodge-dual signs for the orientation $1234$.  Direct
expansion gives the Plücker quadric



$$
K_{12}K_{34}-K_{13}K_{24}+K_{14}K_{23}=0.                  \tag{2.4}
$$



As a useful exact full subfamily, put $h=s=t$.  Then $E=T+1$, so only
one tail step occurs.  Substitution in Item 273's gate matrix gives



$$
G_{t,t}=
 \begin{pmatrix}
 0&1&0&0\\
 4t+3&22t+5&12t-3&-6t+3
 \end{pmatrix},                                             \tag{2.5}
$$



and therefore



$$
K(G_{t,t})=(0,6t-3,12t-3,0,0,-4t-3).                      \tag{2.6}
$$



Equations (2.3)--(2.6) are exact identities over $\mathbb Q$, not finite
interpolation claims.

## 3. The fixed flag incidence

Let $K=(K_{12},K_{13},K_{14},K_{23},K_{24},K_{34})$ be a nonzero
decomposable two-vector and $x=(x_1,x_2,x_3,x_4)$.  The equation
$x\wedge K=0$ has four coordinates:



$$
\begin{aligned}
 I_{123}&=x_1K_{23}-x_2K_{13}+x_3K_{12},\\
 I_{124}&=x_1K_{24}-x_2K_{14}+x_4K_{12},\\
 I_{134}&=x_1K_{34}-x_3K_{14}+x_4K_{13},\\
 I_{234}&=x_2K_{34}-x_3K_{24}+x_4K_{23}.
\end{aligned}                                               \tag{3.1}
$$



On the Plücker quadric with $K\ne0$, these four displayed equations have
rank two and are equivalent to $x$ lying in the represented two-plane.
Thus (1.3) is equivalent to



$$
K=K(G),\qquad I_{123}=I_{124}=I_{134}=I_{234}=0             \tag{3.2}
$$



on the rank-two chart.

Projectively, this is the fixed flag variety



$$
\mathcal I=\{([K],[x])\in\operatorname{Gr}(2,4)\times
 \mathbb P^3:x\in K\}.                                      \tag{3.3}
$$



It has dimension $4+1=5$ in an ambient variety of dimension $4+3=7$,
so its codimension is two.  The exterior-square construction therefore
provides a fixed determinantal incidence of uniform algebraic complexity,
but not one hypersurface divisor.

The affine cone in (3.1) includes $x=0$.  Projectivizing the state would
discard that branch, and no all-prime theorem here proves $x\ne0$.

## 4. Exterior-square transport

Let $U$ be either Item 273 state transport



$$
U_h(h,s):S_T(h,s)\longmapsto S_T(h+1,s),\qquad
 U_s(h,s):S_T(h,s)\longmapsto S_T(h,s+1).                   \tag{4.1}
$$



In the ordered basis (2.2), its exterior square is the exact $6\times6$
matrix



$$
(\wedge^2U)_{ij,ab}=U_{ia}U_{jb}-U_{ib}U_{ja}.              \tag{4.2}
$$



For every invertible $4\times4$ matrix,



$$
\det(\wedge^2U)=(\det U)^3.                                \tag{4.3}
$$



This follows either from the six pairwise eigenvalue products or directly
from (4.2).  Hence the exterior-square module has rank six and exactly the
same zero and pole support as Item 273's rank-four module, with
multiplicities tripled.

If $K_{h,s}=K(G_{h,s})$, horizontality of the natural kernel line under a
shift $U$ would mean



$$
[K_{\mathrm{new}}]=[(\wedge^2U)K_{h,s}].                   \tag{4.4}
$$



Equivalently, after pulling the new gate back to the old state frame,



$$
\operatorname{row}(G_{\mathrm{new}}U)
 =\operatorname{row}(G_{h,s}).                              \tag{4.5}
$$



This is invariant under a simultaneous gauge change of the state
connection and the kernel line.  A single exact failure disproves the
existence of that natural horizontal rank-one subobject.

## 5. Exact $h$- and $s$-nonhorizontality

At $(h,s)=(1,1)$,



$$
G_{1,1}=
 \begin{pmatrix}0&1&0&0\\7&27&9&-3\end{pmatrix},\qquad
 K_{1,1}=(0,3,9,0,0,-7).                                   \tag{5.1}
$$



Pull the next gates back through the exact Item 273 state shifts:



$$
\widetilde G_h=G_{2,1}U_h(1,1),\qquad
 \widetilde G_s=G_{1,2}U_s(1,1).                            \tag{5.2}
$$



Their primitive kernel Plücker vectors are



$$
\begin{aligned}
 K(\widetilde G_h)
   &=(1565,-5870,-17959,-12915,-42296,10439),\\
 K(\widetilde G_s)
   &=(595,-427,1090,812,-1475,-429).
\end{aligned}                                               \tag{5.3}
$$



Neither vector is proportional to (5.1).  More strongly, stacking the
old and pulled-back row planes gives



$$
\det\begin{pmatrix}G_{1,1}\\ \widetilde G_h\end{pmatrix}
 ={604\over1365}\ne0,\qquad
 \det\begin{pmatrix}G_{1,1}\\ \widetilde G_s\end{pmatrix}
 =-{7568\over1365}\ne0.                                     \tag{5.4}
$$



Thus both pairs of row planes span the full dual state space.  Their
kernel planes are transverse, so (4.4) fails for both generators.

The checker separately verifies the correct exterior law: transporting
the *old* kernel by $\wedge^2U$ agrees with the kernel of the transported
old covectors $G_{1,1}U^{-1}$.  The failure in (5.3)--(5.4) is therefore
motion of the gate observation, not an orientation or Hodge-sign error.

## 6. Exact failure on the actual fixed-$M$ ray

The adjacent fixed-$M$ parameter step is



$$
(h,s)\longmapsto(h-4,s+3).                                 \tag{6.1}
$$



Where defined, its exact state transport is



$$
\begin{aligned}
 W_{h,s}={}&U_s(h-4,s+2)U_s(h-4,s+1)U_s(h-4,s)\\
 &\cdot U_h(h-4,s)^{-1}U_h(h-3,s)^{-1}
        U_h(h-2,s)^{-1}U_h(h-1,s)^{-1}.
\end{aligned}                                               \tag{6.2}
$$



The smallest clean actual-prime witness is



$$
(h,s,p,M)=(5,1,29,21)
 \longmapsto(1,4,31,21).                                    \tag{6.3}
$$



The primitive old and pulled-back kernel Plücker vectors are



$$
\begin{aligned}
 K_{\mathrm{old}}
  ={}&(966875,-83743035,-928364750,8571696,84169225,940218807),\\
 K_{\mathrm{pull}}
  ={}&(1162220187,411657489,-1265521434,-8518535856,
       9022899625,-6079782117).
\end{aligned}                                               \tag{6.4}
$$



They lie on the Plücker quadric, but are not proportional.  In fact,



$$
\det\begin{pmatrix}
 G_{5,1}\\ G_{1,4}W_{5,1}
 \end{pmatrix}
 =-{585482135072\over1165539375}\ne0.                       \tag{6.5}
$$



Thus the natural kernel line is non-horizontal even along the actual
prime-tied fixed-$M$ direction.

The step (6.3) changes the characteristic from $29$ to $31$.  The
rational transport (6.2) is an exact comparison over $\mathbb Q$, but
the two collision congruences live in different finite fields.  Therefore
the transversality in (6.5) does not itself exclude either individual
prime collision or give a prime-density bound.

## 7. Rank-drop and zero-state strata

The Plücker line only exists on $\operatorname{rank}G=2$.  The complete
stratification is



$$
\begin{array}{c|c|c}
\operatorname{rank}G&K(G)&\ker G\\ \hline
2&\text{nonzero decomposable two-vector}&\text{dimension }2\\
1&0&\text{dimension }3\\
0&0&\text{dimension }4.
\end{array}                                                  \tag{7.1}
$$



Hence rank one and rank zero both collapse to the same Plücker-cone apex
$K=0$.  The exterior-square coordinate alone cannot distinguish the
rank-one hyperplane gate from the rank-zero all-state gate.  They must be
retained as separate determinantal strata using the original row frame.

Likewise, $x=0$ is an automatic affine collision and is absent from the
projective flag variety.  No universal state nonvanishing is assumed.

Consequently the natural Grassmannian encoding is exact on its rank-two,
nonzero-state chart, while the all-branch object is a fixed *stratified*
determinantal incidence.  That stratification is only a repackaging of
the original two gate equations; it does not add codimension.

## 8. Lisse/Frobenius scope

Item 273 supplies a rational translation-difference connection with fixed
singular support.  A lisse $\ell$-adic sheaf or a Frobenius trace law
would require additional arithmetic data: a fixed étale family, a
Frobenius action, bounded conductor, and a theorem connecting the actual
state section to its trace functions.  None is produced merely by (4.1).

The exact failures (5.4) and (6.5) prove something narrower and concrete:
the natural kernel Plücker line is not a flat line inside the exact
exterior-square difference module.  Therefore it is not, by this
construction, a fixed Frobenius eigenline or a fixed divisor hit.

An enlarged module could adjoin the moving gate frame, and an unrelated
geometric construction could conceivably yield a lisse sheaf.  Those
possibilities remain **OPEN**.  This item proves no global nonexistence
theorem for them.

## 9. Weighted admission and de-overlap

Item 264's fixed-$j=1$ prime interval has raw logarithmic weight
$M/6+o(M)$, or $1/36$ per $6M$.  Item 149 already books the first
post-Cartier copy on every such row.

By (4.3), exterior-square transport introduces no singular factors beyond
Item 273.  Every fixed window still has exceptional weight



$$
O_L(\log M)=o(M).                                           \tag{9.1}
$$



Outside that zero-mass set, the event is a moving codimension-two flag
incidence.  No estimate



$$
\sum_{p:\,Q_0=Q_1=0}\log p\le cM+o(M),
 \qquad c<{1\over6},                                        \tag{9.2}
$$



is proved.  In particular, geometric codimension is not promoted to
probabilistic $p^{-2}$ behavior without a uniform distribution theorem.
The full $1/36$ ceiling and zero booking remain.

## 10. Replay and proof labels

The standard-library checker verifies:

* the exact formulas (2.3)--(2.6) and the Plücker relation;
* the four incidence coordinates on a basis and a nonincident vector;
* the exterior-square transformation and determinant laws;
* both local nonhorizontal witnesses (5.3)--(5.4);
* the actual fixed-$M$ witness (6.3)--(6.5);
* the collapse of the rank-one and rank-zero strata to $K=0$.

These are exact rational identities and declared witnesses.  They are not
a collision census and support no asymptotic inference.

### PROVED

* The fixed rank-two Grassmannian/flag incidence of uniform complexity.
* The six-coordinate Plücker formula, quadric, and four-coordinate
  incidence with only two independent conditions.
* The rank-six exterior-square module and unchanged singular support.
* Nonhorizontality under both parameter generators and the actual
  fixed-$M$ step.
* The rank-drop and $x=0$ branch audit.
* Item 149 de-overlap, unchanged $1/36$ ceiling, and zero booking.

### OPEN

* A larger flat or lisse sheaf containing both the state and moving gate
  frame.
* Any Frobenius/trace interpretation with bounded conductor for the
  prime-tied arithmetic section.
* A weighted incidence theorem implying (9.2).
* Any positive $j=1$ capacity reduction or new Route-1 rate.

