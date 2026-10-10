> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 412 — Frobenius-marked cubic branches and the symmetric-selector boundary

Date: 2026-09-01  
Status: **WORK ONLY, UNAUDITED, NO CENTRAL EDIT, NO BOOKING**

## 1. Verdict and capacity first

Retain the actual base coefficients from Item 411,



$$
u=a_n,\qquad v=a_{n-1},\qquad r=b_n,\qquad s=b_{n-1},
$$



and its exact marked collision equations



$$
s=X_pu,\qquad r=X_p(u+v)\pmod p.                 \tag{1.1}
$$



This item settles what the mark is in the difficult class
$q\equiv1\pmod6$.  Put



$$
n=q-1,\qquad x_q=4^{n/3},\qquad
 t=\frac{p-1}{3},\qquad \chi_p(2)=2^t\pmod p.
$$



Then $K=4^n=x_q^3$, and the distinguished root is exactly



$$
\boxed{X_p=x_q\chi_p(2)\pmod p.}                 \tag{1.2}
$$



Thus the mark is not a fixed characteristic-zero factor of
$Z^3-K$.  It is the cubic Frobenius value of $2$.  Over the
Eisenstein integers, the actual collision is a diagonal incidence:
the prime must divide the coefficient branch whose label equals
$\chi_p(2)$.  The Item-403/411 Smith carrier forgets that label and sees
the union of all three branches.

This yields two exact no-go statements.

1. Any information class invariant under cyclic permutation of the three
   cube-root branches can exclude the whole unmarked orbit, but cannot
   select one nonempty member of that orbit.  Smith invariant factors,
   the unmarked radical carrier, and their valuations belong to this
   symmetric class.
2. No one proper $q$-only rational factor of $Z^3-x_q^3$ contains the
   distinguished root for every compatible prime.  Already for the same
   value $q=7$, the selected root lies in the quadratic factor at
   $p=13$, and in the linear factor at $p=31$.

These are selector-architecture no-go theorems.  They do **not** exhibit a
wrong branch in the actual coefficient family and do not rule out a global
actual-family identity excluding the entire unmarked orbit.

There is also a useful positive reduction.  On an unmarked primitive row,
let $\zeta\in\mu_3(\mathbb F_p)$ be its common branch ratio.  Then, for
two of the three residue classes modulo $18$, marked selection is an
ordinary cubic-residuosity test:



$$
\boxed{
\begin{array}{c|c}
p\bmod18&\text{marked branch condition}\ \\ \hline
7&2\zeta^{-2}\in(\mathbb F_p^\times)^3,\\
13&2\zeta^{-1}\in(\mathbb F_p^\times)^3,\\
1&\zeta=\chi_p(2)\quad\text{directly.}
\end{array}}                                             \tag{1.3}
$$



For $p\equiv1\pmod{18}$, ordinary cubic character kills every element
of $\mu_3$, so multiplying $2$ by a power of $\zeta$ cannot turn the
direct equality into a cube/noncube test.

No weighted distribution theorem for the actual moving carriers is proved.
Consequently the separate large-prime ceiling remains



$$
\frac{\log136}{6}=0.8187758142893420014168718304\ldots,   \tag{1.4}
$$



the frozen booked deficit remains



$$
T-r_1=1.0196329836694317938803064012\ldots,                \tag{1.5}
$$



and both the booking delta and proved capacity delta are zero.

## 2. PROVED — the distinguished root is a Frobenius mark

Write $q=6d+1$, so $n=6d$, and let $p=6m+q$.  Item 411 uses



$$
E=2m+q-1=2m+6d.
$$



But



$$
\frac{p-1}{3}=2(m+d),\qquad \frac{2n}{3}=4d,
$$



and hence the exact integer exponent identity



$$
E=\frac{p-1}{3}+\frac{2n}{3}                      \tag{2.1}
$$



holds.  Since $x_q=4^{n/3}=2^{2n/3}$, equation (2.1) gives



$$
2^E=x_q,2^{(p-1)/3}.
$$



Reduction modulo $p$ proves (1.2).  Fermat also gives



$$
\chi_p(2)^3=2^{p-1}=1,
$$



so $\chi_p(2)\in\mu_3(\mathbb F_p)$, and



$$
X_p^3=x_q^3=K\pmod p.
$$



This is an all-parameter identity.  It is not inferred from the
normalization rows in the replay.

The case $q=1$ also satisfies the exponent identity, but its connection
determinant is $-6$, so Item 411 already excludes every compatible
common collision there.  The branch-selection problem begins at
$q\ge7$.

## 3. PROVED — Eisenstein branch decomposition and diagonal incidence

Let



$$
\mathcal O=\mathbb Z[\omega],\qquad \omega^2+\omega+1=0.
$$



For $j\in\{0,1,2\}$, define the two branch residuals



$$
L_{j,0}=s-\omega^jx_qu,
 \qquad
 L_{j,1}=r-\omega^jx_q(u+v).                       \tag{3.1}
$$



Item 411's unmarked primitive forms are



$$
D=ur-s(u+v),\qquad
 V_0=s^3-Ku^3,\qquad
 V_1=r^3-K(u+v)^3.                                  \tag{3.2}
$$



Because $K=x_q^3$, one has the exact factorizations



$$
V_0=\prod_{j=0}^2L_{j,0},\qquad
 V_1=\prod_{j=0}^2L_{j,1}.                           \tag{3.3}
$$



Over any field of characteristic different from $3$, with $x_q\ne0$,



$$
D=V_0=V_1=0
 \quad\Longleftrightarrow\quad
 \exists j:\ L_{j,0}=L_{j,1}=0.                    \tag{3.4}
$$



Indeed, if $(u,u+v)\ne(0,0)$, then $D=0$ makes $(s,r)$ a scalar
multiple $y(u,u+v)$; either cubic equation gives $y^3=x_q^3$, so
$y=\omega^jx_q$.  If $(u,u+v)=(0,0)$, the cubics force
$(s,r)=(0,0)$, and all three branches meet at the origin.  This proves
(3.4), including degenerate coordinate choices.

Now let $p\equiv1\pmod3$, and choose a prime ideal
$\mathfrak p\mid p$ in $\mathcal O$.  There is a unique label
$j(\mathfrak p)$ satisfying



$$
\omega^{j(\mathfrak p)}
 \equiv 2^{(p-1)/3}\pmod{\mathfrak p}.               \tag{3.5}
$$



For a primitive row $p\nmid H_q$, Items 396 and 411 plus (1.2) give
the exact marked incidence theorem



$$
\boxed{
 p\mid\lambda_{0,m},\lambda_{1,m}
 \quad\Longleftrightarrow\quad
 L_{j(\mathfrak p),0}\equiv L_{j(\mathfrak p),1}\equiv0
 \pmod{\mathfrak p}.}                                  \tag{3.6}
$$



The unmarked Smith condition replaces the prescribed
$j(\mathfrak p)$ in (3.6) by an existential quantifier over all three
labels.  This is the precise information lost by the rational Smith
carrier.  If $p\mid H_q$, all four base coefficients vanish and the
actual collision is already present; all three branch equations meet at
zero, so there is no unique label to recover.

Equation (3.6) is the actual-family theorem produced by this item.  It
does not prove that the marked incidence is empty.

## 4. PROVED — rational linear/quadratic split and fixed-factor no-go

Over $\mathbb Q$, the cubic has the factorization



$$
Z^3-x_q^3=(Z-x_q)(Z^2+x_qZ+x_q^2).                 \tag{4.1}
$$



The quadratic factor is irreducible over $\mathbb Q$, since its
discriminant is $-3x_q^2$.  Thus these are the only two nonconstant
proper rational factors, up to units.

Correspondingly, put



$$
\begin{aligned}
 \ell_0&=s-x_qu,&\ell_1&=r-x_q(u+v),\\
 Q_0&=s^2+x_qsu+x_q^2u^2,&
 Q_1&=r^2+x_qr(u+v)+x_q^2(u+v)^2.
\end{aligned}                                           \tag{4.2}
$$



Then



$$
V_0=\ell_0Q_0,\qquad V_1=\ell_1Q_1.               \tag{4.3}
$$



On a primitive unmarked row:

* the rational linear stratum is $\ell_0=\ell_1=0$;
* the rational quadratic stratum is $D=Q_0=Q_1=0$, and contains the
  two conjugate nontrivial branches.

By (1.2), the selected root lies in the linear stratum exactly when
$\chi_p(2)=1$, i.e. exactly when $2$ is a cube modulo $p$.  Otherwise
it lies in the quadratic stratum, with its orientation still determined by
the value of $\chi_p(2)$.

This rational stratum is not constant even with $q$ fixed.  For
$q=7$, one has $x_q=16$.  At $p=13$,



$$
\chi_{13}(2)=2^4=3,qquad X_{13}=9\pmod {13},
$$



so $X_{13}$ lies in the quadratic factor.  At $p=31$,



$$
\chi_{31}(2)=2^{10}=1,qquad X_{31}=16\pmod {31},
$$



so $X_{31}$ lies in the linear factor.  Both primes are compatible with
the same $q=7$, with $m=1$ and $m=4$, respectively.

Therefore no one proper $q$-only rational factor in (4.1) can represent
the distinguished root for every compatible prime.  These two rows concern
the root mark only.  They do **not** assert that either prime divides the
actual unmarked carrier at $q=7$.

## 5. PROVED — ordinary cubic-residue selector in two classes

Assume a primitive unmarked row.  At least one member of
$(u,u+v)$ is nonzero.  Choose such a member $a$, let $b$ be the
corresponding member of $(s,r)$, and define



$$
\zeta=\frac{b}{x_qa}\in\mu_3(\mathbb F_p).          \tag{5.1}
$$



The determinant $D=0$ makes (5.1) independent of which nonzero
coordinate is chosen.  Equation (3.6) becomes simply



$$
\zeta=\chi_p(2).                                    \tag{5.2}
$$



For $a\in\mathbb F_p^\times$, write



$$
\chi_p(a)=a^{(p-1)/3}.
$$



When $p\equiv7\pmod {18}$, one has
$t=(p-1)/3\equiv2\pmod3$, so



$$
\chi_p(\zeta^2)=\zeta.
$$



Hence



$$
\zeta=\chi_p(2)
 \Longleftrightarrow
 \chi_p(2\zeta^{-2})=1
 \Longleftrightarrow
 2\zeta^{-2}\in(\mathbb F_p^\times)^3.              \tag{5.3}
$$



When $p\equiv13\pmod {18}$, one has $t\equiv1\pmod3$, and the
same argument gives



$$
\zeta=\chi_p(2)
 \Longleftrightarrow
 2\zeta^{-1}\in(\mathbb F_p^\times)^3.               \tag{5.4}
$$



When $p\equiv1\pmod {18}$, one has $t\equiv0\pmod3$, so



$$
\chi_p(\zeta^e)=1\qquad(e\in\mathbb Z).
$$



Thus no expression $2\zeta^{-e}$ changes the ordinary cubic character
of $2$; (5.2) must be retained directly or replaced by a genuinely
finer Kummer/Frobenius invariant.  This is a no-go only for that ordinary
cubic-residue manipulation, not for every possible invariant.

Equations (5.3)--(5.4) provide a concrete next arithmetic target: a
cubic-reciprocity or Frobenius-distribution theorem for the **actual moving
ratio** (5.1), with valuation weights audited separately.  This item does
not prove such a theorem.

## 6. PROVED scoped no-go — symmetric data cannot recover a nonempty label

Over $\mathcal O$, consider the cyclic action



$$
\tau:(u,v,r,s)\longmapsto(u,v,\omega r,\omega s).    \tag{6.1}
$$



It satisfies



$$
D\longmapsto\omega D,qquad
 V_0\longmapsto V_0,qquad
 V_1\longmapsto V_1,                                  \tag{6.2}
$$



while it cyclically permutes the branch pairs in (3.1).  Consequently:

* the vanishing of $(D,V_0,V_1)$ is invariant;
* the local valuations used in the primitive Smith exponent are invariant,
  since $\omega$ is a unit;
* every invariant obtained only from the unmarked orbit is unchanged;
* the label $j$ is cyclically permuted.

Therefore unmarked orbit data cannot identify one branch inside a
nonempty orbit.  It can still prove that the entire orbit is empty, which
would be sufficient for Route 1.  It can also be combined with the
nonsymmetric input $\chi_p(2)$.  What it cannot do is manufacture the
missing mark from symmetric data alone.

The action (6.1) is an Eisenstein ambient action; it does not preserve the
rational actual coefficient family.  Accordingly, this theorem is an
information-class no-go, not an actual wrong-branch counterexample.

## 7. Capacity, weighting, and overlap audit

For the $q\equiv1\pmod6$ part of a fixed row, the actual valuation mass
may be partitioned by the Frobenius mark:



$$
\Gamma_{1}(m)=\Gamma_{1,0}(m)+\Gamma_{1,1}(m)+
 \Gamma_{1,2}(m),                                      \tag{7.1}
$$



where each term sums



$$
v_p(c_m)\log p
$$



over actual common-content primes whose selected Eisenstein label is the
corresponding value of $\chi_p(2)$, after choosing one prime
$\mathfrak p\mid p$ for each rational $p$.  Eisenstein conjugation
swaps the last two labels and leaves their sum unchanged.  The labels may
equivalently be grouped rationally into the cubic-residue and nonresidue
strata.

With only nonnegativity and the inherited total ceiling, proving that one
fixed branch contributes zero gives no numerical upper-bound reduction:
all remaining allowed mass may concentrate in the other branches.  It may
also concentrate in the untouched $q\equiv5\pmod6$ class.  A density
statement for ambient primes in cubic Frobenius classes does not change
this conclusion; the primes dividing the moving coefficient carriers are
a correlated weighted subset, and no equidistribution theorem for that
subset has been proved.

Moreover, (3.6) is a first-digit criterion.  Item 390 owns all valuation
depth through



$$
\log c_m^>
 =\sum_{p>6m}\min\{v_p(\lambda_{0,m}),v_p(\lambda_{1,m})\}\log p.
                                                               \tag{7.2}
$$



Therefore radical zero density in one or all Frobenius bins does not by
itself imply $o(m)$ in (7.2); it needs an independent depth bound.  A
sufficient Closer theorem is a direct $o(m)$ bound for the weighted
selected incidence in (7.2), or radical control plus a proved uniform
depth estimate.

The de-overlap rules remain:

1. Every prime in this item is $p>6m$, disjoint from the booked
   $p<2m$ Cartier support.
2. $H_q$ and $G_q^{\rm prim}$ describe one union of primewise support;
   their logarithms are not independent reservoirs.
3. Item 390 already includes every valuation depth; no Smith exponent is a
   second booking.
4. Excluding common content does not automatically exclude beta matching
   on the primitive residual target.

Hence



$$
\boxed{\Delta r_{\rm booked}=0,\qquad
        \Delta C_{\rm total}^{\rm proved}=0.}          \tag{7.3}
$$



## 8. Strict claim ledger

### PROVED

* The exact Frobenius mark identity (1.2) for every
  $q\equiv1\pmod6$ and compatible prime.
* The exact Eisenstein branch decomposition and marked diagonal incidence
  (3.3)--(3.6).
* The rational linear/quadratic split and the fixed-rational-factor no-go.
* The ordinary cubic-residue selector (5.3)--(5.4) in the
  $p\equiv7,13\pmod {18}$ classes.
* The sharply scoped $\mu_3$-symmetric information no-go.
* Zero booking and zero proved capacity reduction.

### CONDITIONAL

* Uniform exclusion of the selected Frobenius incidence, together with the
  already bijective $q\equiv5\pmod6$ class, would prove $c_m^>=1$.
* A valuation-weighted $o(m)$ theorem for all selected incidences would
  reduce the strictly large-prime component to zero rate.

### OPEN

* Nonoccurrence of the selected branch in the actual coefficient family.
* Carrier-weighted distribution across the Frobenius-labelled branch
  ideals.
* A useful refinement in the $p\equiv1\pmod {18}$ class.
* Uniform support of $H_qG_q^{\rm prim}$ in $P_q$.
* Valuation-weighted $o(m)$ control of $c_m^>$.
* Any positive Route-1 booking, Route-1 closure, or irrationality of
  $e+\pi$.

No actual wrong-root prime, Chebotarev law for moving carrier divisors,
finite extrapolation, or all-depth conclusion from a mod-$p$ selector is
claimed.

## 9. Replay and pinned dependencies

Run:

```text
python work/item412_marked_cubic_frobenius_selector_boundary_certificate.py \
  --output work/item412_marked_cubic_frobenius_selector_boundary_certificate.replay.json \
  --replay work/item412_marked_cubic_frobenius_selector_boundary_certificate.json
```

The standard-library replay:

1. verifies every pinned dependency hash;
2. checks the exact exponent and root identities on transparent
   normalization rows;
3. symbolically expands the rational linear/quadratic factorization;
4. exhaustively verifies the unmarked three-branch decomposition and cyclic
   action over $\mathbb F_7$ and $\mathbb F_{13}$;
5. checks (5.3)--(5.4) for every cubic-root label at every prime below
   $250$ with $p\equiv1\pmod3$; and
6. records the exact $(q,p)=(7,13),(7,31)$ fixed-factor witnesses.

The finite rows normalize formulas and counterexamples only.  The uniform
claims rest on the displayed exponent identity, factorization, field
argument, and cyclic action.

Pinned dependencies:

```text
b44cc15d1a846d5298d61b9e53539116b31bbab0338dbc6e320fb0a875b0d0a0  sources/mixed_cubic_cube_smith_reduction.md
5bfb3c871b12524f672df515e920236f2470145d4f68bdcd7b47f29408692f46  sources/item390_mixed_cubic_fresh_primitive_saturation_report.md
7355b6909994357583f799e627e1ff19edb230a6a9002ee845be585057726aca  sources/item396_fixed_gap_resultant_3adic_report.md
245bf2e557dd81ac88c94e9d0adc8990f203e3ab40680d23bd50f8e435240c48  sources/item403_mixed_cubic_exact_smith_and_finite_local_data_no_go_report.md
a9c33967b42f5ae09c2c0c71de1b956ca240e49c367be46f3af2878cd96cbb83  sources/item406_mixed_cubic_actual_adjacent_recurrence_report.md
1399357c4dbbf49ea685c356e34efde4fa5566fe31db14f7dd0ce252a3f35168  work/item411_mixed_primitive_boundary_transport_report.md
5f7c48924d650dc5b5078ef86eaef9a0ea5ce32b3de3268229218d50f7eb7407  work/item411_mixed_primitive_boundary_transport_certificate.json
0d1cdbc73a4b6d0570af6d00895250e76f4d1d3ba7a590aa0c0209b2450ee96d  work/item411_mixed_primitive_boundary_transport_manifest.json
```

All Item-412 artifacts remain in `work/`.  No canonical or central file is
modified.
