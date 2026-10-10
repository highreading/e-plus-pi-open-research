> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 243 — exact order-six actual-family closure and the all-h gauge

## 1. Result

Let $h=3n+r$, where $r\in\{1,2\}$, and let



$$
\delta_r(n)=\sum_{k=0}^3p_k(h)
 \left(\prod_{j=0}^{k-1}\rho(h+3j)\right)E_{h+3k}^*.
$$



The following statements are **PROVED EXACTLY**.

1.  For each residue $r$, the actual sequence $\delta_r(n)$ satisfies
    an order-six rational recurrence for every integer $n\geq0$.
2.  Its forward coefficient is nonzero for every such $n$.
3.  Six exact initial zeros in each residue therefore give

    

$$
\delta_r(n)=0\qquad(n\geq0).
$$



4.  Item 237's proved order-three recurrence for $c_h^*$, whose leading
    coefficient $p_3(h)$ is positive for $h\geq1$, and three separate
    exact gauge initials in each residue then give

    

$$
\boxed{c_h^*=\mathcal R_hE_h^*}
    \qquad(h\geq1,\ 3\nmid h).
$$



The two initial-value layers are logically distinct: 12 defect initials
prove the gauged $E$-recurrence, while six gauge initials transfer that
recurrence to $c_h^*=\mathcal R_hE_h^*$.

## 2. Actual-family transition and endpoints

The 15-dimensional state consists of the joint $x,u$ companion state
tensor the $v$ companion state; $y$ is recovered by the $y,v$ cross
relation.  Exact Gosper certificates prove the required $x$ and $v$
recurrences and the $x,u$ and $y,v$ cross relations in
$\mathbb Q(n,j)$.

Both telescoping endpoints were audited for both residues.  The lower
certificate numerator is divisible by $j$; the upper base coefficient
lies strictly beyond the support of
$K_e=(1-z)^{2h}(1+z)^e$.  Every displayed endpoint denominator has no
unlisted nonnegative integral zero.  The one exceptional unreduced pole,
the lower endpoint of the residue-two $v$ recurrence at $n=0$, is
replaced by a direct exact rational check



$$
\sum_{k=0}^3P_k(0)v_{2+3k}=0.
$$



Every primitive transition divisor factors into a nonzero rational scalar
and sign-normalized factors with strictly positive coefficients.  Hence all
transition divisors, all their forward shifts, the denominators of
$\rho(h)$, and $4h+3$ are nonzero throughout the actual range.

## 3. Ambient order-six identity

Write $R_j(n)\in\mathbb Q(n)^{15}$ for the defect covector at time
$n+j$, transported back to time $n$.  A structural common denominator
$B_j(n)$ clears column $j$, giving a polynomial column
$A_j=B_jR_j$.

The exact degree ledger is



$$
\deg A_j\leq206+38j.
$$



The signed cofactors of the first six coordinate rows therefore give a
seven-column relation whose every cleared coordinate has degree at most



$$
\sum_{j=0}^6(206+38j)=2240.
$$



At each of the 2241 consecutive integers $n=0,\ldots,2240$, the first
six columns are invertible and the normalized relation with last
coefficient one vanishes in all 15 coordinates.  At such a point that
normalized relation is exactly the signed-cofactor relation divided by its
nonzero last cofactor.  Thus every cleared coordinate polynomial has 2241
roots and is identically zero.  This proves the ambient relation over
$\mathbb Q(n)$, rather than extrapolating from a finite scan.

## 4. Forward cofactor

The forward cofactor $C_6$ uses columns $0,\ldots,5$, so



$$
\deg C_6\leq\sum_{j=0}^5(206+38j)=1806.
$$



For each residue, 1808 exact values were computed.  The exact forward
difference of order 1807 is zero.  Among the 1807 Newton coefficients
$\Delta^kC_6(0)$, 1804 are negative, three are zero, and none is positive.
An independent origin check gives $C_6(0)<0$ in both residues.  Therefore



$$
C_6(n)=\sum_{k=0}^{1806}\Delta^kC_6(0){n\choose k}<0
\qquad(n\geq0).
$$



The last point is essential: one-sign coefficients alone would not exclude
small zeros if the first nonzero Newton index were positive.  Here the
least nonzero index is exactly zero.

The coefficient of $\delta_r(n+6)$ is $C_6(n)B_6(n)$.  The pole audit
proves $B_6(n)\ne0$; hence forward propagation is valid at every index.

## 5. Initial propagation and gauge transfer

The exact rational initial checker proves

* $\delta_r(0)=\cdots=\delta_r(5)=0$ for $r=1,2$ (12 zeros);
* $c_{3n+r}^*=\mathcal R_{3n+r}E_{3n+r}^*$ for
  $n=0,1,2$ and $r=1,2$ (six identities).

The order-six defect recurrence proves the gauged $E$-recurrence for all
indices.  Both $c_h^*$ and $\mathcal R_hE_h^*$ then satisfy Item 237's
same order-three recurrence, and $p_3(h)>0$.  The six gauge initials prove
the displayed all-h identity.

## 6. No-go, finite evidence, and capacity

**PROVED EXACT AMBIENT NO-GO.**  The original one-step defect covector is
not the zero covector on the full 15-dimensional state space: all 15
coordinates are nonzero in both residues.  This does not contradict the
actual-family theorem; it shows why transported order-six closure is needed.

**EXACT FINITE ONLY.**  Six orbit computations modulo 1000000007, at
$n=3,17,41$ in each residue, first find order six.  They are recorded only
as finite evidence and are not used to extrapolate the theorem.

The capacity ledger does not change:



$$
\boxed{\text{new linear log rate}=0,\quad
       \text{new divisibility exponent}=0,\quad
       \text{capacity booked}=0.}
$$



The gauge theorem removes the algebraic identity barrier, but it proves no
moving-row-prime nonvanishing, no simultaneous endpoint $K_h$ theorem,
no density or radical saving, and no conclusion about the irrationality of
$e+\pi$.

## 7. Reproducibility

The canonical and replay closure JSON files are byte-identical with SHA-256

`0ec0052ea270a84828cb1934373ad05e8e5b00cbf72e0d970ff805e716078546`.

The ambient degree-grid JSON has SHA-256
`94ee7993c8869fe58f8824ba3bf3a0c061044e90d3debcc12f2ecc5f7b1329c6`.
The Newton JSON has SHA-256
`87f22eaea77a95fac34b92b227bf803766d27f934f12a59eea6e747a5c1d2af0`.

The package manifest pins every source, script, dependency, and result.
