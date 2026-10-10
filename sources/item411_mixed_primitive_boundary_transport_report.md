> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 411 — Primitive mixed-cubic boundary transport and the marked-branch target

Date: 2026-09-01  
Status: **CANONICAL, ROOT-AUDITED, NO BOOKING**

## 1. Verdict and capacity first

Let (q>0) be odd with (3\nmid q), put



$$
n=q-1,\qquad A=2n-1=2q-3,\qquad K=4^n,
$$



and retain the actual fixed-gap coefficients of Items 403 and 406.  Write



$$
u=a_n,\qquad v=a_{n-1},\qquad r=b_n,\qquad s=b_{n-1}.
$$



Item 406 proves



$$
\begin{aligned}
 C_0&=2u+v,& AC_1&=(5n-1)C_0-6u,\\
 T_0&=r+s,& AT_1&=(5n-7)T_0+6r.
\end{aligned}                                                \tag{1.1}
$$



This item proves an exact all-(q) transport of the **primitive**
Item-403 cubic factor.  In the cubic algebra with variable (Z), replace
the two actual generators by



$$
\epsilon _0=s-Zu,\qquad
 \epsilon _1=r-Z(u+v).                                      \tag{1.2}
$$



The change is invertible at every prime away from (6A).  Consequently,
after the local common content is removed, the primitive factor
(G_q^{\rm prim}) is measured exactly by



$$
\boxed{
 D=ur-s(u+v),\qquad
 V_0=s^3-Ku^3,\qquad
 V_1=r^3-K(u+v)^3.}                                        \tag{1.3}
$$



This is an equality of local Smith exponents, not merely a one-sided
radical implication.

For a compatible prime (p=6m+q), (m\ge1), (q\ge5), put



$$
k=4m+1,\qquad E=p-k=2m+q-1,\qquad X_p=2^E,
 \qquad Y_m=4^m.                                           \tag{1.4}
$$



The actual common-log collision is exactly the **marked** branch



$$
s=X_pu,\qquad r=X_p(u+v)\pmod p.                           \tag{1.5}
$$



By contrast, the unmarked support of (H_qG_q^{\rm prim}) is the union
of (1.5) with its cube-root twists



$$
s=\zeta X_pu,\qquad r=\zeta X_p(u+v),
 \qquad \zeta\in\mu _3(\mathbb F_p).                       \tag{1.6}
$$



Thus the primitive Smith carrier is exact as an **unmarked cubic
carrier**, but it is stronger than the actual target when
(q\equiv1\pmod6).  In that half, proving support for all of
(G_q^{\rm prim}) attacks three branches although only (zeta=1) is
needed.  When (q\equiv5\pmod6), cubing is bijective and the unmarked
and marked conditions coincide.

The marked branch admits an exact positive-exponent polynomial form.  Put



$$
F_{m,q}(z)=(1-z)^{6m}(1+z^2)^E,
 \qquad J_{m,q}(z)=F_{m,q}(z)(1+z)^E.                       \tag{1.7}
$$



Writing (F_j=[z^j]F_{m,q}), (J_j=[z^j]J_{m,q}), the actual collision
is exactly



$$
\boxed{
 F_{n-1}=Y_m(J_n-J_{n-1}),\qquad
 F_n=Y_m(J_n+J_{n-1})\pmod p.}                              \tag{1.8}
$$



The smallest missing actual-family lemma is now the uniform nonoccurrence
of (1.8).  Together with the already settled (q=1) row, that lemma would
give (c_m^>=1) for every (m).  Item 411 does not prove it.

The component ceiling therefore remains



$$
\frac{\log136}{6}=0.8187758142893420014168718304\ldots,    \tag{1.9}
$$



the booked deficit remains



$$
T-r_1=1.0196329836694317938803064012\ldots,                \tag{1.10}
$$



and both the booking delta and the proved total-capacity delta are zero.

## 2. PROVED — exact generator and Smith transport

In



$$
\mathcal A_\ell=\mathbb Z_\ell[Z]/(Z^3-K),
$$



let



$$
\lambda_0=C_0Z-T_0,\qquad \lambda_1=C_1Z-T_1.
$$



Using (1.1) gives the identities



$$
\lambda_0=-(\epsilon_0+\epsilon_1),                        \tag{2.1}
$$





$$
A\lambda_1
 =-(5n-7)\epsilon_0-(5n-1)\epsilon_1.                     \tag{2.2}
$$



The coefficient matrix in (2.1)--(2.2) has determinant (6).  Therefore,
for every prime (ell\nmid6A), the two pairs generate the same ideal in
(mathcal A_\ell), and their (3\times6) multiplication matrices have
identical Smith invariants.

The coefficient content of the new pair is



$$
\min\{v_\ell(u),v_\ell(u+v),v_\ell(r),v_\ell(s)\}
 =\min\{v_\ell(u),v_\ell(v),v_\ell(r),v_\ell(s)\}.         \tag{2.3}
$$



Item 406 identifies this with (v_\ell(H_q)) away from (6A).  If the
four base coefficients are divided by their local common power, attach a
star to the results and define



$$
\begin{aligned}
 D^*&=u^*r^*-s^*(u^*+v^*),\\
 V_0^*&=(s^*)^3-K(u^*)^3,\\
 V_1^*&=(r^*)^3-K(u^*+v^*)^3.
\end{aligned}                                              \tag{2.4}
$$



Applying the exact DVR Smith theorem of Item 403 to the new pair and using
Smith invariance proves



$$
\boxed{
 v_\ell(G_q^{\rm prim})
 =\min\{v_\ell(D^*),v_\ell(V_0^*),v_\ell(V_1^*)\}
 \quad(\ell\nmid6A).}                                      \tag{2.5}
$$



The connection determinant also becomes especially simple:



$$
\boxed{
 A(C_0T_1-C_1T_0)=6\{ur-s(u+v)\}.}                         \tag{2.6}
$$



Equations (2.1)--(2.6) hold for the actual coefficient family for every
admissible (q).  They are not inferred from a bounded factorization.

## 3. PROVED — exact marked versus unmarked support

Let (p=6m+q) be compatible.  Then (p\nmid6A), and Fermat gives



$$
X_p^3=2^{3E}\equiv4^{q-1}=K\pmod p.                       \tag{3.1}
$$



The fixed-gap residue congruences of Item 396 and the invertible transport
(2.1)--(2.2) prove



$$
\boxed{
 p\mid\lambda_{0,m},\lambda_{1,m}
 \quad\Longleftrightarrow\quad
 s=X_pu,\ r=X_p(u+v)\pmod p.}                              \tag{3.2}
$$



This is a first-digit statement.  It does not identify higher
(p)-adic valuations of the actual residues.

Now suppose first that (p\nmid H_q).  By (2.5), the condition
(p\mid G_q^{\rm prim}) is the simultaneous vanishing of the three forms
in (2.4).  The vector ((u,u+v)) cannot be zero: otherwise (V_0=V_1=0)
would also force (s=r=0), contrary to primitivity.  The determinant
(D=0) therefore gives



$$
(s,r)=y(u,u+v)
$$



for some (y\in\mathbb F_p), and either cubic equation gives (y^3=K).
Conversely, such a (y) makes all three forms zero.  Since every root of
(Y^3-K) is (zeta X_p), this proves (1.6) when (p\nmid H_q).

If (p\mid H_q), all four raw base coefficients vanish, so (1.6) holds
trivially.  Conversely, a solution of (1.6) either has all four raw
coefficients zero, giving (p\mid H_q), or is primitive and gives
(p\mid G_q^{\rm prim}).  Hence the exact union statement is



$$
\boxed{
 p\mid H_qG_q^{\rm prim}
 \Longleftrightarrow
 \exists\zeta\in\mu_3(\mathbb F_p):
 (s,r)=\zeta X_p(u,u+v)\pmod p.}                            \tag{3.3}
$$



For (q\equiv5\pmod6), one has (p\equiv2\pmod3), so
(mu_3(\mathbb F_p)=\{1\}), and (3.2)--(3.3) coincide.  For
(q\equiv1\pmod6), there are three branches.  The replay includes an
explicit **ambient, non-actual** coefficient row over (mathbb F_{13})
on a nontrivial branch.  It proves that the unmarked forms alone do not
identify the selected power-of-two root.  It is not evidence that a false
branch occurs in the actual mixed-cubic family.

The case (q=1) is separate and already closed:



$$
C_0T_1-C_1T_0=-6,
$$



so no compatible prime (p>3) can be a common-log collision there.

## 4. PROVED — positive-exponent polynomial boundary form

For (q\ge5), Item 406 gives, with coefficients only through degree
(n=q-1<p),



$$
R(z)=\frac{(1-z)^{6m}}{(1+z^2)^k},\qquad
 S(z)=\frac{R(z)}{(1+z)^k}.                                \tag{4.1}
$$



In (mathbb F_p[[z]]/(z^p)), Frobenius gives



$$
(1+z^2)^{-k}=(1+z^2)^{p-k},\qquad
 (1+z)^{-k}=(1+z)^{p-k}.                                  \tag{4.2}
$$



Since (p-k=E), the coefficients of (R,S) below degree (p) equal
those of the two honest polynomials (F,J) in (1.7).  Item 406 also gives



$$
\begin{aligned}
 r&=R_n,&s&=R_{n-1},\\
 u&=2^{-n}(S_n-S_{n-1}),&
 v&=2^{1-n}S_{n-1}.
\end{aligned}                                              \tag{4.3}
$$



Finally,



$$
X_p2^{-n}=2^{E-n}=2^{2m}=4^m=Y_m.                         \tag{4.4}
$$



Substitution of (4.2)--(4.4) into the marked equations (3.2) proves the
two-boundary criterion (1.8).  More generally, the unmarked support
(3.3) is obtained by replacing (Y_m) on the right side of (1.8) by
(zeta Y_m).

This is a global reduction for every compatible parameter, not a finite
prime census.  It replaces the primitive cubics by two selected linear
boundary equations in explicit finite polynomials.

## 5. PROVED scoped no-go — the triangular transform alone cannot close the target

The special numerator in (F_{m,q}) remains essential.  To make this
precise, work over (mathbb F_p), take an arbitrary truncated polynomial



$$
R_*(z)=\sum_{j=0}^n r_jz^j,
 \qquad S_*(z)=(1+z)^{-k}R_*(z)\pmod {z^{n+1}},             \tag{5.1}
$$



and impose the two marked boundary equations with (R_*,S_*).  Write



$$
c_j=[z^j](1+z)^{-k}=(-1)^j\binom{k+j-1}{j}.                \tag{5.2}
$$



The two boundary residuals are linear functionals of the (r_j).  Their
(2\times2) coefficient minor on the variables
((r_{n-2},r_{n-3})) is



$$
\boxed{
 \frac{Y_m^2k^2(k^2-1)}6\ne0\pmod p.}                     \tag{5.3}
$$



Indeed (p>3), (0<k-1<k<k+1<p), and (Y_m\ne0).  Therefore the two
functionals have rank two even after (r_0) is fixed.  In particular, for
every compatible triple with (q\ge5), there exists a normalized ambient
row with (r_0=1) satisfying both boundary equations.

This is a uniform countermodel to the implication



$$
S_*=(1+z)^{-k}R_*+R_*(0)=1
 \quad\Longrightarrow\quad\text{marked boundary noncollision}. \tag{5.4}
$$



The countermodels are not the actual
(R=(1-z)^{6m}(1+z^2)^{-k}).  Thus (5.3) does not refute the actual
two-boundary lemma.  It proves only that lower-triangularity, invertibility,
and normalization of the reciprocal transform cannot by themselves prove
that lemma.  A successful proof must use the special first-order kernel,
its full coefficient recurrence, or an equivalent global arithmetic input.

## 6. Capacity, weighting, and de-overlap

### 6.1 What perfect success would do

If (1.8) is impossible for every compatible (p), then (3.2) excludes
every strictly large common-log prime.  Item 390 would give



$$
c_m^>=1
$$



for every (m).  This closes the separate large-prime component ceiling
((\log136)/6).  It is a Closer exclusion, not a new divisor lower bound;
the frozen booked (r_1) and deficit (1.10) do not change.

### 6.2 H/G overlap

The raw integer factors (H_q) and (G_q^{\rm prim}) need not have
disjoint prime support.  Primewise one may partition into

1. (p\mid H_q), or
2. (p\nmid H_q) and (p\mid G_q^{\rm prim}).

Equation (3.3) describes their **union** and supplies no second valuation
reservoir.  Their logarithms must not be added as independent capacity.
Moreover, in the (q\equiv1\pmod6) class, an unmarked (G)-prime may lie
on a wrong cube-root branch and is not automatically an actual common-log
prime.

### 6.3 First digit versus all depth

The Smith and boundary carriers in this item detect first-digit support.
Item 390 already owns every valuation depth of the actual strictly
large-prime common content.  No exponent of (G_q^{\rm prim}) may be
booked as a second copy.

For the same reason, a theorem only of the form



$$
\sum_{p\text{ satisfying the marked equations}}\log p=o(m)
$$



would control the radical but would not by itself prove
(\log c_m^>=o(m)): one sparse prime can occur to high (p)-adic depth.
A sufficient weighted relaxation must control the actual valuation mass



$$
\sum_{p>6m}
 \min\{v_p(\lambda_{0,m}),v_p(\lambda_{1,m})\}\log p=o(m), \tag{6.1}
$$



or combine radical density with an independent depth bound.  The mod-(p)
boundary equations alone do not provide such a lift.

### 6.4 Other branches

Every prime here satisfies (p>6m), so it is disjoint from the booked
(p<2m) Cartier support and the small-prime remainder.  Excluding common
content does not automatically exclude beta matching on the primitive
residual target.  An upper bound for this component cannot be subtracted
from an overlapping global content ceiling without an exact partition.

Therefore



$$
\boxed{\Delta r_{\rm booked}=0,\qquad
       \Delta C_{\rm total}^{\rm proved}=0.}                \tag{6.2}
$$



## 7. Strict claim ledger

### PROVED

* The exact all-(q) generator transport (2.1)--(2.2).
* The exact local primitive carrier and exponent identity (2.5) away from
  (6(2q-3)).
* The marked actual collision criterion (3.2).
* The exact unmarked cube-root decomposition (3.3), including the
  distinction between the two congruence classes.
* The positive-exponent polynomial boundary criterion (1.8).
* The uniform transform-only ambient no-go (5.3)--(5.4).
* Zero booking and zero proved capacity reduction.

### CONDITIONAL

* Uniform nonoccurrence of (1.8) would prove (c_m^>=1).
* Full unmarked support exclusion for (H_qG_q^{\rm prim}) would also
  imply that conclusion, but is stronger than necessary when
  (q\equiv1\pmod6).

### OPEN

* The selected two-boundary lemma for the actual polynomials (F,J).
* Uniform support or divisibility of (G_q^{\rm prim}) and
  (H_qG_q^{\rm prim}) by (P_q).
* A valuation-weighted (o(m)) theorem for (c_m^>).
* Any new Route-1 booking, Route-1 closure, or irrationality of (e+\pi).

No finite normalization row, ambient branch witness, or transform-only
countermodel is extrapolated to the actual family.

## 8. Replay and pinned dependencies

Run:

```text
python scripts/item411_mixed_primitive_boundary_transport_certificate.py \
  --replay results/item411_mixed_primitive_boundary_transport_certificate.json \
  --output results/item411_mixed_primitive_boundary_transport_certificate_replay.json
```

The standard-library replay:

1. verifies the exact Hermite and generator transport identities;
2. checks equality of the old and new local primitive Smith exponents on
   transparent normalization rows;
3. verifies the reciprocal and positive-exponent boundary forms in both
   admissible congruence classes;
4. constructs an ambient nontrivial cube-root branch witness;
5. verifies the closed formula (5.3) and constructs normalized
   transform-only collision countermodels; and
6. verifies every pinned dependency hash.

The finite rows normalize formulas only.  The uniform theorems rest on the
displayed algebra, Frobenius identities, and rank calculation.

Pinned dependencies:

```text
245bf2e557dd81ac88c94e9d0adc8990f203e3ab40680d23bd50f8e435240c48  sources/item403_mixed_cubic_exact_smith_and_finite_local_data_no_go_report.md
a9c33967b42f5ae09c2c0c71de1b956ca240e49c367be46f3af2878cd96cbb83  sources/item406_mixed_cubic_actual_adjacent_recurrence_report.md
5bfb3c871b12524f672df515e920236f2470145d4f68bdcd7b47f29408692f46  sources/item390_mixed_cubic_fresh_primitive_saturation_report.md
7355b6909994357583f799e627e1ff19edb230a6a9002ee845be585057726aca  sources/item396_fixed_gap_resultant_3adic_report.md
```

All Item-411 artifacts are sealed in the canonical source, script, result,
and manifest directories.
