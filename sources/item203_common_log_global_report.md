> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 203 — cancellation-aware global transfer to the common-log line

Checked: 2026-08-30 (Beijing time)

## 1. Scope and verdict

Stay on an Item 194 prime-number-theorem row



$$
4m+1=(2j+1)p-2s,\qquad
 1\le s\le (p-3)/6,\qquad 3j+1<p,                 \tag{1.1}
$$



and retain Item 200's scalar coefficients



$$
\sum_{k\ge0}g_{m,k}v^k
 =\frac{((1-v)(1-2v))^{6m}}
        {(1-2v+2v^2)^{4m+2}}.                     \tag{1.2}
$$



Put $n=4m$.  This item attacks only the normalized common-log
condition.  It does not use the identification $F_m=G_m$, it does not
reuse the Item 149 digit, and it keeps $A_1$ completely separate.

> **PROVED — the actual state lies in the zero specialization of the
> local kernel modulo $p$.**  On every row (1.1),
> 

$$
>        g_{m,n-3}\equiv g_{m,n-2}\equiv g_{m,n-1}
>        \equiv g_{m,n}\equiv g_{m,n+1}\equiv0\pmod p.          \tag{1.3}
>
$$


> Thus Item 200's abstract local line
> $\lambda(0,2,2,1)$ has $\lambda=0$ for the actual undivided
> coefficient state modulo $p$.  The divided state in (1.5) can still
> have an arbitrary line parameter $e_{-3}$.  This is an all-row
> support theorem, not a finite
> observation.

> **PROVED — exact five-coordinate Frobenius defect.**  There are
> integral coefficients $e_d$, $-3\le d\le1$, given without a
> recurrence denominator by
> 

$$
>       g_{m,n+d}=p e_d,\qquad
>       e_d=[v^{n+d}]E_{p,j}(v)P_{p,s}(v),                         \tag{1.4}
>
$$


> where $E_{p,j}$ and $P_{p,s}$ are defined in (3.1).  Modulo $p$,
> the common-log condition is exactly
> 

$$
> \boxed{e_0=0,\qquad e_{-1}=2e_{-3},\qquad
>        e_{-2}=2e_{-3}.}                                      \tag{1.5}
>
$$


> In that case the recurrence also gives $e_1=0$.  Conversely, (1.5)
> gives both normalized common-log zeros.

> **PROVED — cancellation-aware global transfer.**  Work modulo $p^2$
> through degree $n+1<p^2$.  Any two unit-series solutions of the full
> first-order coefficient equation with constant coefficient one differ
> by
> 

$$
>                         1+pH(v^p).                              \tag{1.6}
>
$$


> Every possible term introduced by (1.6) lands in the support gap (1.3).
> Hence all five quotients $g_{m,n+d}/p\pmod p$ are independent of the
> singular choices at $k+1\equiv0\pmod p$.  The apparent
> $2^{n+1}(n+1)!$ clearing loss in naive forward transfer is therefore
> not intrinsic for this target.

> **PROVED SCOPED INFORMATION BARRIER — the transfer lands in a moving
> Frobenius-defect problem.**  The explicit transfer is driven by the two
> polynomials
> 

$$
>              \Delta_pR(v)=\frac{R(v)^p-R(v^p)}p,\qquad R=A,D.   \tag{1.7}
>
$$


> Their reductions modulo $p$ have degree at least $2p-1$, and their
> first $p-1$ coefficients are truncated logarithmic kernels; see
> (5.2)--(5.4).  Thus the global uniqueness theorem removes the recurrence
> division barrier but does not produce a bounded-degree or bounded-height
> resultant.  This is a statement about the displayed direct
> representation only; it does not rule out a different arithmetic
> representation.

> **EXACT FINITE ONLY.**  The deterministic replay checks all 701 PNT rows
> with $m\le160$, 3,505 exact defect coordinates, and 299,557 gauged
> recurrence rows.  It finds 11 separate $e_0$-zeros and no line
> membership.  No nonoccurrence, density, or asymptotic conclusion is
> inferred.

> **OPEN.**  No all-prime exclusion and no sublinear bound for the
> common-log radical $R_m$ is proved.  No additional Route-1 mass and no
> statement about $A_1$ follows.

## 2. The five-term support gap

Set



$$
A(v)=(1-v)(1-2v)=1-3v+2v^2,\qquad
 D(v)=1-2v+2v^2,                                    \tag{2.1}
$$



and abbreviate



$$
a=3j+1,\quad c=2j+1,\quad
 r=\frac{p-6s-3}{2},\quad q=2s-1.                  \tag{2.2}
$$



The row identities give



$$
6m=ap+r,qquad 4m+2=cp-q.                           \tag{2.3}
$$



Consequently the series in (1.2) factors exactly over the integers as



$$
G_m(v)=F_j(v)^pP_{p,s}(v),qquad
 F_j(v)=\frac{A(v)^a}{D(v)^c},qquad
 P_{p,s}(v)=A(v)^rD(v)^q.                            \tag{2.4}
$$



The moving polynomial has the exact degree



$$
\deg P_{p,s}=2r+2q=p-2s-5.             \tag{2.5}
$$



Freshman's dream in $\mathbb F_p[[v]]$ changes (2.4) into



$$
G_m(v)\equiv F_j(v^p)P_{p,s}(v)\pmod p.       \tag{2.6}
$$



For $-3\le d\le1$, the exponent



$$
n+d=cp-2s-1+d                                      \tag{2.7}
$$



has residue



$$
p-2s-1+d\in
 \{p-2s-4,p-2s-3,p-2s-2,p-2s-1,p-2s\}.             \tag{2.8}
$$



Every residue in (2.8) is strictly larger than (2.5) and strictly less
than $p$.  Since every term of $F_j(v^p)P_{p,s}(v)$ has residue equal
to an exponent in the support of $P_{p,s}$, its five coefficients in
(2.7) are exactly zero.  Equation (1.3) follows.  The same proof shows
that every nonnegative shift of these exponents by a multiple of $-p$
is also in the gap whenever the shifted exponent remains nonnegative.

Finally, (1.1) implies



$$
6m<(3j+2)p\le p^2,qquad n+1<6m<p^2.               \tag{2.9}
$$



This strict height bound is what makes the gauge classification in
Section 4 exact: no $v^{p^2}$ term occurs before the target.

## 3. Denominator-free normalized coordinates

Because $F_j\in\mathbb Z[[v]]$, coefficientwise Frobenius gives an
integral series



$$
E_{p,j}(v)=\frac{F_j(v)^p-F_j(v^p)}p\in\mathbb Z[[v]].          \tag{3.1}
$$



Substitution into (2.4) is the exact identity



$$
G_m(v)=F_j(v^p)P_{p,s}(v)+pE_{p,j}(v)P_{p,s}(v).   \tag{3.2}
$$



The first term has zero coefficient at all five exponents (2.7), so
(1.4) follows over the integers, with no division by a recurrence
coefficient.

The two Item 200 target forms are



$$
C_0=g_{m,n}-2g_{m,n-1}+2g_{m,n-2},\qquad
 C_1=g_{m,n+1}.                                      \tag{3.3}
$$



Hence



$$
\frac{C_0}{p}\equiv e_0-2e_{-1}+2e_{-2},\qquad
 \frac{C_1}{p}\equiv e_1\pmod p.                   \tag{3.4}
$$



For completeness, impose the two zeros in (3.4) and use the recurrence
rows $k=n,n-1$.  On the state



$$
(e_0,e_{-1},e_{-2},e_{-3})                         \tag{3.5}
$$



the resulting three-row matrix is Item 200's



$$
\begin{pmatrix}
 1&-2&2&0\\
 -20m-8&40m+20&-40m-24&8\\
 -8m&20m-2&-40m&40m+4
 \end{pmatrix}.                                     \tag{3.6}
$$



Its first three-column minor is $-16(4m+1)$, a unit modulo $p$
because $4m+1\equiv-2s\not\equiv0\pmod p$, and its kernel is



$$
\mathbb F_p(0,2,2,1).         \tag{3.7}
$$



Equations (3.4)--(3.7) prove (1.5), including the case
$e_{-3}=0$.  Conversely, substituting (1.5) into the row $k=n$ gives
$e_1=0$, again because $n+1=4m+1$ is a unit modulo $p$.  This is the
precise normalized common-log test.  Item 197 then identifies it with
$p^2\mid C_0,C_1$; no $A_1$ coordinate is involved.

## 4. Cancellation-aware global recurrence transfer

The four-step recurrence is the coefficient form of the first-order
equation



$$
AD\,Y'=\{6mA'D-(4m+2)AD'\}Y.                       \tag{4.1}
$$



Let $Y_1,Y_2\in(\mathbb Z/p^2\mathbb Z)[[v]]$ be unit-series solutions
of (4.1) with $Y_1(0)=Y_2(0)=1$.  Since $AD$ is a unit series,



$$
\left(\frac{Y_1}{Y_2}\right)'=0\pmod {p^2}.        \tag{4.2}
$$



Write $K=Y_1/Y_2=1+\sum_{k\ge1}\kappa_kv^k$.  Through degree less
than $p^2$, equation (4.2) says



$$
\kappa_k=0\pmod {p^2}\quad(p\nmid k),\qquad
 \kappa_{hp}=0\pmod p\quad(1\le h<p).               \tag{4.3}
$$



Thus, with $H(0)=0$,



$$
K=1+pH(v^p)\pmod {p^2}      \tag{4.4}
$$



through every required degree.  Conversely, every factor (4.4) has zero
derivative modulo $p^2$, so this describes the full recurrence gauge.

For a target exponent $n+d$, multiplication by (4.4) changes its
coefficient by



$$
p\sum_{h\ge1}H_h\,[v^{n+d-hp}]Y_2\pmod {p^2}.      \tag{4.5}
$$



Every coefficient in (4.5) is zero modulo $p$ by the shifted support
gap after (2.8).  Therefore (4.5) vanishes modulo $p^2$.  All five
normalized coordinates are globally well defined by $g_{m,0}=1$ and
the recurrence even though individual resonant coefficients are not.

This is the cancellation that the naive cleared transfer misses.  It
removes the earlier $\Theta(m\log m)$ factorial-height objection for
these five coordinates.  It does not evaluate the coordinates or prove
that (1.5) is empty.

## 5. Where the global transfer lands

For $R=A,D$, define the integral polynomial



$$
\Delta_pR=\frac{R(v)^p-R(v^p)}p.  \tag{5.1}
$$



Expanding $A(v)^p=A(v^p)+p\Delta_pA$ and the analogous identity for
$D$ in (3.1) gives the recurrence-division-free congruence



$$
\boxed{
 E_{p,j}\equiv
 a\frac{A(v^p)^{a-1}}{D(v^p)^c}\Delta_pA
 -c\frac{A(v^p)^a}{D(v^p)^{c+1}}\Delta_pD
 \pmod p.}                                          \tag{5.2}
$$



This formula, multiplied by $P_{p,s}$, computes all five $e_d$
without dividing by any $k+1$.

The input is nevertheless not bounded-degree.  The next-to-leading
coefficients give, for every admissible $p\ge11$,



$$
[v^{2p-1}]\Delta_pA=-3\cdot2^{p-1}\equiv-3\pmod p,
 \qquad
 [v^{2p-1}]\Delta_pD=-2^p\equiv-2\pmod p.           \tag{5.3}
$$



Thus each displayed defect polynomial has degree at least $2p-1$ over
$\mathbb F_p$.  Its lower section is an explicit truncated logarithm:
for $1\le k<p$,



$$
[v^k]\Delta_pA=-\frac{1+2^k}{k},qquad
 [v^k]\Delta_pD=-\frac{\tau_k}{k}\pmod p,           \tag{5.4}
$$



where



$$
\tau_0=\tau_1=2,qquad
 \tau_k=2\tau_{k-1}-2\tau_{k-2}.                   \tag{5.5}
$$



For (5.4), factor $A=(1-v)(1-2v)$; for $D$, use roots whose sum and
product are both two.  The standard congruence
$p^{-1}\binom pk\equiv(-1)^{k-1}/k\pmod p$ gives the formulas.

Equations (5.2)--(5.5) precisely locate the remaining arithmetic issue:
the actual, globally normalized state is a five-coefficient projection of
two moving truncated-log defects.  A direct elimination of (1.5) from
(5.2) therefore has input degree proportional to $p$, not bounded
degree.  This proves neither that a different bounded-degree transform is
impossible nor that common zeros exist.  It is the scoped information
barrier left after the global recurrence ambiguity has been removed.

## 6. Deterministic replay and final status

The self-contained standard-library checker

`scripts/item203_common_log_global_certificate.py`

performs the following exact tasks.

1. It verifies the row factorization (2.3)--(2.5) and the five-term
   support gap.
2. It computes (5.2) independently from $\Delta_pA,\Delta_pD$ and checks
   all five normalized quotients in (1.4) modulo $p$.
3. It checks the equivalence between the two common-log zeros and the
   three line equations (1.5).
4. It applies the nontrivial gauge $1+pv^p$, checks every recurrence row
   modulo $p^2$, and verifies all five target coordinates are unchanged.
5. It verifies every truncated-log coefficient (5.4) and the degree
   witnesses (5.3) for every prime occurring in the finite replay.

The canonical and replay JSON are required to be byte-identical.  The
checker contains no host path, time field, floating-point identity, or
external numeric backend.  The manifest uses archive-relative
`sources/`, `scripts/`, and `results/` keys.

### PROVED

- The actual five-term support gap (1.3).
- The integral five-coordinate defect formula (1.4) and the exact line
  test (1.5).
- Global recurrence-gauge classification and target uniqueness through
  degree $n+1<p^2$.
- The recurrence-division-free defect formula (5.2), truncated-log identities,
  and linear degree growth of its direct kernels.

### EXACT FINITE ONLY

- The 701-row nonoccurrence result through $m\le160$, all listed counts,
  and the row digest in the canonical replay.

### OPEN

- Uniform exclusion or a sublinear weighted bound for the common-log
  locus.
- A bounded-degree or bounded-height alternative to the direct defect
  system.
- Any $A_1$ theorem, additional Route-1 mass, or conclusion about
  $e+\pi$.
