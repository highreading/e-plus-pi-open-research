> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 246 — Structure and row recurrences of the $j=2$ bulk residual

Checked: 2026-08-31 (Beijing time)

## 1. Scope and verdict

Item 244 reduced the variable character part of the actual $j=2$
carry to one old endpoint term and one canonical scalar
$\mathsf B_\nu$.  This item analyzes that scalar.

For an integer polynomial



$$
D(t)=\sum_{v=0}^{d}d_vt^v,\qquad
 N_v=2(L+v)+1,                                      \tag{1.1}
$$



define



$$
\mathcal S_L[D]=\sum_{v=0}^{d}\frac{(-1)^vd_v}{N_v}.             \tag{1.2}
$$



On the actual Item 244 parity polynomial $D_\nu$, the residual is
$\mathsf B_\nu=\mathcal B_L[D_\nu]$, where $\mathcal B_L$ is
defined below.

> **PROVED — closed rational/double-period representation.**
> 

$$
> \boxed{
> \mathcal B_L[D]
> =\sum_{0\le k<v\le d}
> \frac{(-1)^{v-k-1}d_v}{N_kN_v}.}                   \tag{1.3}
>
$$


> Equivalently, it is the exact polynomial double integral (2.4).  No
> recursively defined tail remains in this representation.

> **PROVED — exact recurrence in the row parameters.**  Multiplication
> by either row factor $1+\epsilon t$, $\epsilon=\pm1$, acts by
> 

$$
> \boxed{
> \begin{aligned}
> \mathcal S_L[(1+\epsilon t)D]
> &=\mathcal S_L[D]-\epsilon\mathcal S_{L+1}[D],\\
> \mathcal B_L[(1+\epsilon t)D]
> &=\mathcal B_L[D]+\epsilon\left(
> \mathcal B_{L+1}[D]+\frac{\mathcal S_{L+1}[D]}{2L+1}
> \right).
> \end{aligned}}                                      \tag{1.4}
>
$$


> Together with the parity-binomial seed recurrence (3.4), these
> formulas evaluate $\mathsf B_\nu$ exactly from the row parameters
> $(L,b,q,R,\delta)$, without expanding the full $P_\nu$.

> **PROVED — reciprocity is a two-pole relation, not a scalar closure.**
> Coefficient reversal gives the exact identity (4.7), but at the
> reflected pole $L^\vee=-L-d-1$.  On every actual nonempty
> projection,
> 

$$
> 0<2L+d+1<p,                                      \tag{1.5}
>
$$


> so $L^\vee\not\equiv L\pmod p$.  Reciprocity alone therefore
> introduces a second pole state and cannot eliminate
> $\mathcal B_L[D]$ as one scalar.

> **PROVED — the two $\nu$ coordinates require a companion parity.**
> If $F=P_0/(1+z^2)$, its selected parity is $A(t)$ and its opposite
> parity is $C(t)$, then
> 

$$
> D_0=(1+t)A,\qquad
> D_1=(1+3t)A+t^{1-\delta}(3+t)C.                    \tag{1.6}
>
$$


> The companion $C$ is nonzero on every admissible row.  Thus the
> pair does not close on $D_0$ alone.

> **PROVED — exact moving-prime reformulation and obstruction.**  The
> rational denominator of $\mathcal B_L[D_\nu]$ is a $p$-unit, so
> $\mathsf B_\nu=0\pmod p$ exactly when $p$ divides its reduced
> rational numerator.  A universal nonvanishing theorem is false:
> $(p,s,\nu)=(37,4,0)$ has a nonzero rational value whose numerator has
> $37$-adic valuation one, hence $\mathsf B_0=0\pmod {37}$.

> **SCOPED CONCLUSION.**  The obstruction is now a precise
> moving-prime numerator problem with a finite row-parameter recurrence.
> No Bezout eliminant, zero-rate theorem, or all-prime classification is
> proved.

> **GLOBAL INTERFACE / BOOKING.**  This scalar occurs only in the
> stronger Item 239 $p^3$ carry.  Item 246 does not strengthen the
> ordinary $p^2$ common-log gate and books no rate or capacity.

## 2. Closed coefficient and double-integral forms

Start from the terminal tails of Item 244:



$$
Q_{d+1}=0,\qquad
 Q_k=\frac{d_k}{N_k}-Q_{k+1},\qquad
 \mathcal B_L[D]=\sum_{k=0}^{d-1}\frac{Q_{k+1}}{N_k}.             \tag{2.1}
$$



Expanding the unique tail gives



$$
Q_{k+1}=\sum_{v=k+1}^{d}
 (-1)^{v-k-1}\frac{d_v}{N_v}.                        \tag{2.2}
$$



Interchanging the finite sums proves (1.3).  The inner geometric
polynomial satisfies



$$
\sum_{k=0}^{v-1}(-1)^{v-k-1}y^{2k}
 =\frac{y^{2v}-(-1)^v}{1+y^2}.                       \tag{2.3}
$$



Therefore (1.3) also equals



$$
\boxed{
\mathcal B_L[D]
=\int_0^1\!\int_0^1
x^{2L}y^{2L}
\frac{D(x^2y^2)-D(-x^2)}{1+y^2}\,dx\,dy.}           \tag{2.4}
$$



The numerator in (2.4) is divisible by $1+y^2$, so the integrand is
a polynomial over $\mathbb Z[x,y]$.  The integral is only compact
notation for termwise rational integration; no analytic choice is
involved.

For the actual $D_\nu$, Item 244 proves $1\le N_v<p$.  Hence the
reduced denominator of the rational number (1.3) is not divisible by
$p$, and



$$
\boxed{
 \mathsf B_\nu=0\pmod p
 \iff p\mid\operatorname{num}\!\left(\mathcal B_L[D_\nu]\right).}   \tag{2.5}
$$



This is the exact moving-prime numerator formulation.

## 3. Row-parameter recurrences

First note the two elementary shift identities



$$
\begin{aligned}
\mathcal S_L[tD]&=-\mathcal S_{L+1}[D],\\
\mathcal B_L[tD]&=\mathcal B_{L+1}[D]
 +\frac{\mathcal S_{L+1}[D]}{2L+1}.                  \tag{3.1}
\end{aligned}
$$



The first follows by shifting the coefficient index.  In the second,
the $k=0$ term produces the displayed endpoint correction, while
$k\ge1$ is exactly $\mathcal B_{L+1}[D]$.  Linearity gives (1.4).

Recall the exact Item 244 factorization



$$
D_\nu(t)=\sigma(1-t)^b(1+t)^qE_{R,\delta}(t),         \tag{3.2}
$$



where



$$
L=\left\lceil\frac r2\right\rceil,\quad
b=\min(r,1+3\nu),\quad q=2s-\nu,\quad
R=|r-(1+3\nu)|,\quad\delta\equiv r\pmod2.            \tag{3.3}
$$



The two parity-binomial seeds obey



$$
\boxed{
\begin{aligned}
E_{R+1,0}&=E_{R,0}+tE_{R,1},\\
E_{R+1,1}&=E_{R,0}+E_{R,1},
\end{aligned}
\qquad(E_{0,0},E_{0,1})=(1,0).}                       \tag{3.4}
$$



Equations (1.4), (3.4) are an exact finite recurrence in
$(L,b,q,R,\delta)$: generate the appropriate seed, apply the
$b$ minus-factors and $q$ plus-factors, and retain only the shifted
functional pairs $(\mathcal B_{L+j},\mathcal S_{L+j})$.  No full
coefficient convolution is required.  The checker replays this operator
calculation independently through $p\le101$.

## 4. What reciprocity gives

Besides $\mathcal B_L[D]$, define



$$
\begin{aligned}
\widehat{\mathcal B}_L[D]
&=\sum_{0\le k<v\le d}
 \frac{(-1)^{v-k-1}d_k}{N_kN_v},\\
\mathcal A_L^{(d)}
&=\sum_{k=0}^{d}\frac{(-1)^k}{N_k},\\
\mathcal J_L[D]
&=\sum_{k=0}^{d}\frac{d_k}{N_k^2}.
\end{aligned}                                         \tag{4.1}
$$



Expanding the product $\mathcal S_L[D]\mathcal A_L^{(d)}$ and
separating the diagonal gives



$$
\boxed{
\mathcal B_L[D]+\widehat{\mathcal B}_L[D]
=\mathcal J_L[D]-\mathcal S_L[D]\mathcal A_L^{(d)}.}             \tag{4.2}
$$



Let



$$
D^*(t)=t^{d}D(t^{-1}),\qquad
L^\vee=-L-d-1.                                     \tag{4.3}
$$



Then



$$
2(L^\vee+k)+1=-\{2(L+d-k)+1\}.                    \tag{4.4}
$$



Reversing $k,v$ in the triangular sum proves



$$
\mathcal B_L[D^*]=\widehat{\mathcal B}_{L^\vee}[D].               \tag{4.5}
$$



Using (4.2) at $L^\vee$ yields the exact reciprocity identity



$$
\boxed{
\mathcal B_L[D^*]
=\mathcal J_{L^\vee}[D]
-\mathcal S_{L^\vee}[D]\mathcal A_{L^\vee}^{(d)}
-\mathcal B_{L^\vee}[D].}                            \tag{4.6}
$$



If $D^*=\tau D$, $\tau=\pm1$, this becomes



$$
\boxed{
\tau\mathcal B_L[D]+\mathcal B_{L^\vee}[D]
=\mathcal J_{L^\vee}[D]
-\mathcal S_{L^\vee}[D]\mathcal A_{L^\vee}^{(d)}.}             \tag{4.7}
$$



It is a genuine two-pole relation.  Indeed the largest denominator
$N_d=2(L+d)+1$ satisfies $N_d<p$, and



$$
2L+d+1=N_d-d
 \quad\text{satisfies}\quad0<2L+d+1<p.             \tag{4.8}
$$



But $L^\vee\equiv L\pmod p$ would force
$2L+d+1\equiv0\pmod p$, contradicting (4.8).  Thus even a
self-reciprocal actual projection does not close $\mathcal B_L$ at
one pole.

## 5. What the pair $\nu=0,1$ gives

Put



$$
F(z)=\frac{P_0(z)}{1+z^2}
=(1-z)^r(1+z)(1+z^2)^{2s-1}.                         \tag{5.1}
$$



Write its parity decomposition as



$$
F(z)=A(z^2)+zC(z^2)                                  \tag{5.2}
$$



when $\delta=0$, and interchange the names $A,C$ when
$\delta=1$, so that $A$ always denotes the selected parity and
$C$ the companion parity.  Since



$$
P_0=(1+z^2)F,\qquad P_1=(1+z)^3F,                    \tag{5.3}
$$



parity projection gives (1.6):



$$
\boxed{
D_0=(1+t)A,\qquad
D_1=(1+3t)A+t^{1-\delta}(3+t)C.}                    \tag{5.4}
$$



The companion projection $C$ is never zero.  The zero criterion from
Item 244 applied to the opposite parity would require
$|r-1|<1-\delta$; for $\delta=0$ this would give $r=1$, a parity
contradiction, and for $\delta=1$ the inequality is impossible.

Thus the pair $(D_0,D_1)$ necessarily introduces a nonzero companion
state.  The explicit factorization also shows the common polynomial
divisor



$$
(1-t)^{\min(r,1)}(1+t)^{2s-1}.                      \tag{5.5}
$$



However (1.4) shows that multiplication by this divisor acts through
shifted $L$-states; it does not factor out of $\mathcal B_L$ as a
scalar.  Hence neither the $\nu$-pair nor the visible common factor
alone supplies an eliminant.

## 6. Exact witnesses and finite evidence

The exact rational values at two actual rows are



$$
\begin{array}{c|c|c|c}
(p,s,\nu)&\operatorname{num}(\mathcal B_L)
&\operatorname{den}(\mathcal B_L)&\mathsf B_\nu\pmod p\\ \hline
(17,2,1)&13504&45045&9\\
(37,4,0)&-140105504768&121628516625&0.
\end{array}                                           \tag{6.1}
$$



The second numerator has $37$-adic valuation exactly one, while its
rational value is nonzero.  Therefore an all-row modular nonvanishing
theorem for $\mathsf B_\nu$ is false.

The finite modular census through $p\le401$ has 1,115 rows, 2,230
coordinates, 2,192 nonempty projections, and six separate zeros of
$\mathsf B_\nu$.  None of those six occur simultaneously in both
coordinates.  Of the nonempty projections, 1,111 are self-reciprocal,
but none has a reflected-pole collision.  The companion parity is
nonzero on every row.  These counts are exact finite evidence only.

The rational replay through $p\le101$ covers 148 coordinates.  It
separates the automatic zero projections from the nonempty numerators
divisible by their moving prime; no asymptotic conclusion is drawn.

## 7. Replay, status, and booking

The standard-library checker `item246_j2_bulk_residual_structure_certificate.py`:

1. verifies the coefficient and exact rational representations;
2. replays the row-factor and parity-seed recurrences;
3. verifies the reflected-pole reciprocity identity and pole separation;
4. verifies the exact $\nu$-pair companion relation;
5. reduces exact rational numerators modulo their moving primes; and
6. produces the strictly finite censuses and witnesses.

From the archive root, run:

    python scripts/item246_j2_bulk_residual_structure_certificate.py --output results/item246_j2_bulk_residual_structure_certificate.json
    python scripts/item246_j2_bulk_residual_structure_certificate.py --output results/item246_j2_bulk_residual_structure_certificate_replay.json

Canonical and replay outputs are byte-identical and contain no host path,
timestamp, random seed, or elapsed time.

### Status ledger

**PROVED**

- the coefficient and polynomial double-integral forms (1.3), (2.4);
- the exact row-parameter recurrences (1.4), (3.4);
- the reciprocity relation and distinct reflected-pole theorem;
- the exact two-coordinate companion-parity relation; and
- the moving-prime numerator reformulation and witnesses (6.1).

**EXACT FINITE ONLY**

- the modular census through $p\le401$;
- the operator recurrence replay through $p\le101$; and
- the exact rational numerator replay through $p\le101$.

**OPEN**

- a larger-state eliminant using the reflected pole or companion parity;
- an all-prime classification of moving-prime numerator divisibility;
- an all-prime classification of simultaneous $j=2$ common-log zeros;
  and
- any Route-1 rate or capacity improvement.

The booking is



$$
\boxed{
\text{new unconditional log rate}=0,\qquad
\text{new divisibility exponent}=0,\qquad
\text{capacity reduction}=0.}                        \tag{7.1}
$$



Item 246 proves no statement about the arithmetic nature of $e+\pi$.
