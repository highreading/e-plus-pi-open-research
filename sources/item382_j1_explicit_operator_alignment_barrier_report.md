> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 382 — explicit operator candidates and the fixed-$M$ alignment barrier

Checked: 2026-09-01 (Beijing time)

## 1. Verdict

Retain



$$
p=4h+6s+3,
 \qquad
 M=3h+4s+2,
 \qquad
 h,s\geq1,
 \qquad
 3\nmid h.
\tag{1.1}
$$



Item 379 proved that primitive reduction is invisible to the actual
selected prime, so the congruence problem may use the unreduced sequences
$A_x(h),A_u(h)$.  This item constructs the smallest order-three
polynomial-operator candidates found on each admissible $h\bmod3$ ray
and audits their compatibility with the actual fixed-$M$ motion.

> **EXACT FINITE ONLY — explicit operator candidates.**  Put
> 

$$
> a_n^{(*,\epsilon)}=A_*(3n+\epsilon),
> \qquad *\in\{x,u\},\quad\epsilon\in\{1,2\}.
>
$$


> The deterministic certificate supplies exact integer tables for
> 

$$
> \widehat L_{*,\epsilon}a_n
> =\sum_{j=0}^{3}P_{*,\epsilon,j}(n)a_{n+j}.
> \tag{1.2}
>
$$


> The $x$-candidates have order $3$, degree $19$; the
> $u$-candidates have order $3$, degree $23$.  They vanish on all
> declared fitting and holdout rows and are unique in the corresponding
> modular ansatz.  No symbolic creative-telescoping certificate was
> obtained, so (1.2) is **not** promoted to an all-$n$ recurrence theorem.

> **PROVED — fixed-$M$ alignment no-go.**  Every recurrence confined to
> one $h\bmod3$ ray uses shifts $h\mapsto h+3j$.  At fixed $M$, such
> a shift can be an integral parameter row only when $4\mid j$, and it is
> actual only if the shifted value of $s$ remains at least one.  Thus an
> order-three window contains no second actual fixed-$M$ row.  The first
> possible integral return is
> 

$$
> h\mapsto h+12,
> \qquad s\mapsto s-9,
> \qquad p\mapsto p-6.
> \tag{1.3}
>
$$


> and it is an actual return when $s\geq10$.  Reducing a same-ray recurrence modulo $p$ gives information modulo
> $p$, not modulo the new selected prime $p-6$.  Same-ray operators
> alone therefore provide no cross-prime propagation or resultant.

The ledger remains



$$
\boxed{\text{new booking}=0},
 \qquad
 \boxed{\text{new capacity reduction}=0},
 \qquad
 \boxed{\text{shared fixed-}j=1\text{ ceiling}=1/36}.
\tag{1.4}
$$



## 2. The four finite operators

The exact coefficient convention is



$$
P_j(n)=\sum_{k=0}^{d}c_{j,k}n^k,
\tag{2.1}
$$



with four consecutive blocks $(c_{j,0},\ldots,c_{j,d})$.  The complete
integer tables are in the replay certificate.  Their identifiers are:

| family | $h\bmod3$ | order | degree | coefficient-table SHA-256 |
|---|---:|---:|---:|---|
| $A_x$ | 1 | 3 | 19 | `de6fa1e63fd1e6c36f670af042b573ba27edcb1bb44e5f8c0eb557f58cada515` |
| $A_x$ | 2 | 3 | 19 | `69202f8cd06b6f8290613f8731a99fbbe2da58884a420b397762a98cafe9926d` |
| $A_u$ | 1 | 3 | 23 | `76ba07eb1356faf7dc25598754dc4443ec49d0b5ced42330470ca971da07de63` |
| $A_u$ | 2 | 3 | 23 | `af8df96ad77c3fe3bbd9b6aa39e71e140b294d1d0f952e61b436a8b1a09669b5` |

The $x$-tables use $88$ exact fitting rows and $12$ exact holdout
rows.  The $u$-tables use $104$ fitting rows and $12$ holdout rows.
Over $1{,}000{,}000{,}007$, each candidate matrix has nullity one.  Full
rank excludes orders $1,2$ through degree $30$, and excludes order
$3$ below degree $19$ for $x$ or $23$ for $u$, inside the
declared finite experiment.

These facts do not prove an all-parameter recurrence.  The missing proof
object is a rational Gosper/creative-telescoping certificate for the exact
reverse summand of Item 379.  Apparent minimality is therefore labeled
finite only.

## 3. Exact fixed-$M$ shift arithmetic

Eliminating $s,p$ from (1.1) gives



$$
s={M-3h-2\over4},
 \qquad
 p={3M-h\over2}.
\tag{3.1}
$$



A same-ray shift $h'=h+3j$ at fixed $M$ forces



$$
s'=s-{9j\over4}.
\tag{3.2}
$$



Thus $s'$ is integral precisely when



$$
\boxed{4\mid j.}
\tag{3.3}
$$



An integral return is actual precisely when, in addition, $s-9j/4\geq1$.
For $j=0,1,2,3$, only the original row is actual.  This statement is
independent of whether the finite candidates are eventually certified:
it applies to every order-three step-$3$ recurrence.

At the first possible integral return $j=4$, formula (3.1) gives (1.3);
this returned row is actual when $s\geq10$.  An integer
identity involving $A_*(h)$ and $A_*(h+12)$, reduced at the first row,
lives wholly in $\mathbb F_p$.  The collision at the returned row lives
in $\mathbb F_{p-6}$.  Rational recurrence coefficients supply no field
map or divisibility implication between them.

## 4. The actual transverse motion

Consecutive algebraic fixed-$M$ rows obey



$$
h\mapsto h+4,
 \qquad s\mapsto s-3,
 \qquad p\mapsto p-2.
\tag{4.1}
$$



This changes $h\bmod3$.  The two finite operators live separately on
the $1$- and $2$-rays and contain no cross-ray state identity.
Eliminating internal values from one operator remains on the same ray;
placing two unrelated operators side by side does not create a
cross-prime resultant.

This is a scoped no-go.  It does not exclude a new reciprocity theorem.
It proves that a recurrence over $\mathbb Q(h)$, without extra
cross-prime arithmetic, does not transfer selected divisibility between
$p$ and $p-2$ or $p-6$.

## 5. Height and capacity

Items 376 and 379 give



$$
\log|A_x(h)|,\log|A_u(h)|=O(h\log(h+2)),
\tag{5.1}
$$



and



$$
\log|N_x(h)|,\log|N_u(h)|=O(h).
\tag{5.2}
$$



Across $O(M)$ rows, the direct aggregates are only



$$
O(M^2\log M)
 \quad\text{and}\quad
 O(M^2),
\tag{5.3}
$$



respectively, not the required $o(M)$.  Fixed-degree operator
coefficients do not change the mismatch of moduli or these aggregate
bounds.  Moreover, $N_x,N_u$ remain one-coordinate overcarriers that
forget $Y,V$.  Hence



$$
\boxed{
 \Delta r_1=0,
 \qquad
 \Delta\text{capacity}=0,
 \qquad
 \text{retained shared ceiling}=1/36.}
\tag{5.4}
$$



## 6. Smallest missing arithmetic lemma

The required new input is a target-retaining cross-prime identity that
compares the $h$-state at $p$ with the $h+12$-state at $p-6$, or
directly couples the transverse $h\mapsto h+4$, $p\mapsto p-2$ rows.
It must retain the second boundary coordinate and yield an aggregate
weighted theorem.  Certifying (1.2) alone would not provide this bridge.

## 7. Strict labels

### PROVED

- the fixed-$M$ identities (3.1)–(3.3);
- no order-three same-ray window contains a second actual row;
- the first possible integral same-ray return changes $p$ to $p-6$,
  and is actual when $s\geq10$;
- same-ray recurrence identities alone do not transfer selected
  divisibility across the two primes;
- the aggregate height bounds remain too large;
- zero booking and zero capacity reduction.

### EXACT FINITE ONLY

- four explicit order-three coefficient tables;
- exact fitting and holdout equalities;
- modular rank minimality in the declared search box;
- no all-$n$ recurrence promotion, prime scan, or extrapolation.

### OPEN

- symbolic creative-telescoping certificates and true all-$n$
  minimality for the four candidates;
- a cross-prime reciprocity or common fixed-$M$ carrier;
- selector-aware weighted zero density and any strict fixed-$j=1$
  capacity reduction;
- Route 1 and every conclusion about $e+\pi$.
