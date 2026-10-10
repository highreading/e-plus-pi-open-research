> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 388 — finite local digits and triple-free matching are not an exhaustive mixed-cubic ceiling

Checked: 2026-09-01 (Beijing time)

## 1. Verdict

This item defines the frozen higher-digit/matching part of the mixed-cubic
architecture and asks whether its present local information can support an
exhaustive compatible upper bound.

It cannot.

Two exact countermodel theorems close the whole proposed information class.

1. **Fresh-scalar blindness.**  Any finite package of Witt/Hasse digits on a
   declared prime support has fibers with unbounded fresh common content.
   This remains true when the precision at each declared prime grows with
   $m$, provided it is finite at each row.  Multiplication by a common
   integer congruent to one modulo the complete digit modulus preserves every
   recorded residue exactly while adding new common factors outside the
   declared support.
2. **Sharp multi-parent packing.**  The Item-201 constraints
   (triple gcd one, pair-specific edge divisibility, and the unique CRT bound
   $R\le L$) admit complete-graph integer models with
   $R=L$.  One-parent forests see an asymptotically vanishing fraction of
   their pair-specific mass.

Therefore neither adding finitely many more local digits on the same support
nor repeating triple/forest accounting can make the present class
exhaustive.  A valid Route-1 ceiling must add genuinely global actual-family
input: a support theorem and valuation bound for the complete primitive
content, or a global transfer-lcm theorem for the actual beta recurrence.

This is an information-class no-go, not a counterexample to the actual
mixed-cubic row.  The countermodels do not satisfy the period formulas or the
beta recurrence and are never promoted to actual candidates.  They prove
that the currently retained local consequences do not logically imply the
missing exhaustive bound.

No material ceiling changes.  In particular, the only unconditional global
content ceiling in the frozen package remains



$$
\limsup_{m\to\infty}\frac{\log c_m}{6m}
\le 1.99566316016\ldots>T,
\tag{1.1}
$$



and the matching bound $R\le L$ is sharp in the present information class.
Booking is zero.

## 2. The declared mixed-cubic architecture

This section fixes the scope being closed.  It is a restatement of the
master ledger and the frozen reports, not an enlargement of Route 1.

### 2.1 Core mixed-cubic row

At index $m$, put



$$
N=6m,
\qquad K_0=4m+1,
\qquad K_1=4m+2,
\tag{2.1}
$$



and retain the two rational differentials



$$
\omega_s=\frac{[x(1-x)]^N}{[(1+x)(1+x^2)]^{K_s}}\,dx.
\tag{2.2}
$$



Their endpoint coordinates are written



$$
H_s=R_s+\frac{L_s}{4}\log2+\frac{E_s}{8}\pi.
\tag{2.3}
$$



The two determinant coordinates are



$$
A_m=L_1R_0-L_0R_1,
\qquad
B_m=\frac{L_1E_0-L_0E_1}{8}.
\tag{2.4}
$$



With the frozen clearing integer $D_m^\sharp$, put



$$
X_m=D_m^\sharp A_m,
\qquad
Y_m=D_m^\sharp B_m.
\tag{2.5}
$$



The rank-zero squarefree Cartier product is



$$
G_m=\prod_{p\in\mathcal P_m}p,
\tag{2.6}
$$



and the actual primitive post-Cartier pair and content are



$$
\boxed{
U_m=\frac{X_m}{G_m},
\qquad
V_m=\frac{Y_m}{G_m},
\qquad
c_m=\gcd(U_m,V_m).}
\tag{2.7}
$$



The analytic saddle criterion needs the normalized content/matching exponent
to reach



$$
T=1.1561471519642446123307302239\ldots .
\tag{2.8}
$$



The only booked contribution is the rank-one Cartier divisor



$$
\prod_{p\in\mathcal H_m}p\mid c_m,
\qquad
r_1=0.1365141682948128184504238226\ldots .
\tag{2.9}
$$



### 2.2 Higher Witt/Hasse side

For a forced prime $p\in\mathcal H_m\cup\mathcal Z_m$, let



$$
q_p=p^e\le4m+1<p^{e+1},
\qquad
D=1+\mathbf1_{p\in\mathcal P_m}.
\tag{2.10}
$$



The exact two-minor gate uses



$$
\mathscr A=q_pA_m,
\qquad
\mathscr B=8B_m,
\qquad
p^D\mid\mathscr A,\mathscr B,
\tag{2.11}
$$



and normalized digits



$$
\frac{\mathscr A}{p^D}=\sum_{j\ge0}a_{p,j}p^j,
\qquad
\frac{\mathscr B}{p^D}=\sum_{j\ge0}b_{p,j}p^j.
\tag{2.12}
$$



The gate for $p^r\mid c_m$ is exactly a finite simultaneous zero string
in these digits.  All complete layers reuse the same forced prime support.
The ideal radical ceiling per layer is



$$
C_{\rm rad}=0.28490812992172166432\ldots .
\tag{2.13}
$$



Four ideal complete layers have ceiling $4C_{\rm rad}<T$, while five are
the first not excluded by that support calculation.  These are certification
ceilings, not upper bounds for the complement of the forced support.

For this item, a **finite local digit package** at row $m$ means:



$$
\mathscr D_m=
\left(
U_m,V_m\pmod {p^{e_{m,p}}}:p\in S_m
\right),
\tag{2.14}
$$



possibly together with every gate/valuation statement derived from those
residues, where $S_m$ is a finite declared prime support and each
$e_{m,p}<\infty$.  The depths and $|S_m|$ may grow arbitrarily with
$m$.  Put



$$
M_m=\prod_{p\in S_m}p^{e_{m,p}}.
\tag{2.15}
$$



The present higher-digit program is contained in this class.  An all-depth
$p$-adic identity at every possible content prime would not be finite local
data and is not closed here.

### 2.3 Sequential matching side

After removing $c_m$, put



$$
b_m=\frac{|V_m|}{c_m}.
\tag{2.16}
$$



At a parity-compatible beta index $N$, the exact sequential factor is



$$
T_N=\Delta_{m,N}g_{m,N},
\qquad
\Delta_{m,N}=\gcd(b_m,q_N),
\tag{2.17}
$$



with the final transverse factor $g_{m,N}$ from the frozen equal-valuation
gate.  Primewise,



$$
T_N\mid b_m^2,
\qquad
T_N\mid q_N^2.
\tag{2.18}
$$



For two beta indices, Item 199 proves



$$
\gcd(T_N,T_{N+h})\mid C_h(N),
\tag{2.19}
$$



where $C_h(N)$ is the transfer continuant.  Item 201 organizes a portfolio
of parents $T_{n_i}$ by



$$
P=\prod_iT_{n_i},
\qquad
L=\operatorname{lcm}_iT_{n_i},
\qquad
R=\frac PL.
\tag{2.20}
$$



Here $L$ is the unique CRT modulus and $R$ is reused prime-power credit.
One-parent forests have nonpositive transfer-recycling gain.  If every triple
gcd is one, Item 201 proves



$$
R=\prod_{i<j}\gcd(T_{n_i},T_{n_j}),
\qquad
R\le L.
\tag{2.21}
$$



The unresolved multi-parent class allows one child to meet distinct parents
on disjoint pair-specific prime supports.

### 2.4 Compatibility and fresh support

Every contribution is measured primewise after removing:

1. the booked rank-one Cartier layer;
2. the deterministic clearing reservoir already present in $c_m$ or
   $b_m$;
3. repeated copies of the same prime power across higher layers or parents.

For a declared local support $S_m$, define exactly



$$
c_{m,S}=\prod_{p\in S_m}p^{v_p(c_m)},
\qquad
c_{m,\mathrm{fresh}}=\prod_{p\notin S_m}p^{v_p(c_m)}.
\tag{2.22}
$$



Then



$$
\boxed{
c_m=c_{m,S}c_{m,\mathrm{fresh}},
\qquad
\gcd(c_{m,S},c_{m,\mathrm{fresh}})=1.}
\tag{2.23}
$$



Higher digits constrain only the first factor unless a separate support
theorem proves $c_{m,\mathrm{fresh}}=1$.  Fresh single-index matching is
the analogous part of one $T_N$ not assigned to an old reservoir or an
edge reuse block.

Fixed common-log cells and their own ceilings are separate master branches;
they are not silently included in the countermodels below.

## 3. Fresh-scalar blindness theorem

Let $S$ be any finite prime set, choose finite precisions $e_p\ge1$, and
put



$$
M=\prod_{p\in S}p^{e_p}.
\tag{3.1}
$$



For integers $u,v$, define the complete recorded residue package



$$
\mathscr D_M(u,v)=(u\bmod M,v\bmod M).
\tag{3.2}
$$



For every integer $t\ge1$, set



$$
\lambda_t=1+tM,
\qquad
(u_t,v_t)=(\lambda_tu,\lambda_tv).
\tag{3.3}
$$



Then



$$
\boxed{
\mathscr D_M(u_t,v_t)=\mathscr D_M(u,v),
\qquad
\gcd(u_t,v_t)=\lambda_t\gcd(u,v),
\qquad
\gcd(\lambda_t,M)=1.}
\tag{3.4}
$$



The proof is immediate: $\lambda_t\equiv1\pmod M$, and common scaling
multiplies the gcd by $\lambda_t$.  Every prime factor of $\lambda_t$ is
outside $S$.  Since $t$ is arbitrary, the fresh content is unbounded on
one exact finite-digit fiber.

This statement is stronger than invariance of valuation gates.  It preserves
the actual recorded residues, hence every zero/nonzero digit and every carry
deducible through the declared precision.  If only gate status is retained,
the congruence $\lambda_t\equiv1\pmod M$ is unnecessary: every common
multiplier coprime to $M$ preserves all $S$-valuations.

There is an exact height-compatible version.  Suppose an information class
allows



$$
\max(|u|,|v|)\le B
\tag{3.5}
$$



and $B\ge2(1+M)$.  The pairs



$$
(1,2),
\qquad
(1+M,2(1+M))
\tag{3.6}
$$



both satisfy (3.5), have identical complete residues modulo $M$, and have
contents $1$ and $1+M$.  Thus local data plus that height box cannot
give a content ceiling below $\log(1+M)$.

Applied to (2.14), this proves:

> **FINITE-LOCAL-DIGIT NONEXHAUSTION.**  No theorem depending only on
> finitely many Witt/Hasse digits at the declared support can upper-bound
> the fresh complement in (2.23).  Increasing the number of digits to any
> other finite depth does not repair the logical gap.

The actual period formulas can, in principle, exclude these scalar fibers.
Doing so would be new global input and is exactly what the theorem says is
missing.

## 4. Numerical capacity boundary of the digit-only class

The ideal complete-layer ceilings are



$$
\begin{array}{c|c}
k&kC_{\rm rad}\\ \hline
4&1.13963251968688665728\ldots\\
5&1.42454064960860832160\ldots\\
6&1.70944877953032998592\ldots\\
7&1.99435690945205165024\ldots\\
8&2.27926503937377331456\ldots .
\end{array}
\tag{4.1}
$$



The frozen actual-content height ceiling is



$$
H_c=1.99566316016\ldots .
\tag{4.2}
$$



The near equality



$$
H_c-7C_{\rm rad}=0.00130625070794834976\ldots>0
\tag{4.3}
$$



is only a capacity observation, but it clarifies the management issue:
even seven ideal complete local layers remain numerically compatible with
the old global content-height box.  The eighth layer's ceiling exceeding
$H_c$ is not an upper-bound theorem; a ceiling can exceed an actual value.

More fundamentally, (3.4) shows that no finite $k$ constrains
$c_{m,\mathrm{fresh}}$.  Hence the exhaustive upper bound supplied by
local-digit data alone remains (4.2), which is above the irrationality
threshold.  The five-layer crossing in the Builder ledger is a possible
lower-bound certification capacity, not a Closer theorem.

## 5. Sharp multi-parent packing countermodel

Fix $r\ge3$.  For every edge $1\le i<j\le r$, choose pairwise coprime
odd integers $\ell_{ij}>1$, and define parent integers



$$
P_i=\prod_{j\ne i}\ell_{\min(i,j),\max(i,j)}.
\tag{5.1}
$$



Then, exactly,



$$
\boxed{
\gcd(P_i,P_j)=\ell_{ij},
\qquad
\gcd(P_i,P_j,P_k)=1\quad(i,j,k\text{ distinct}).}
\tag{5.2}
$$



Moreover,



$$
\prod_{i=1}^{r}P_i
=\prod_{i<j}\ell_{ij}^{2},
\qquad
\operatorname{lcm}_{i}P_i
=\prod_{i<j}\ell_{ij}.
\tag{5.3}
$$



Therefore the exact reuse credit is



$$
\boxed{
R=\frac{\prod_iP_i}{\operatorname{lcm}_iP_i}
=\prod_{i<j}\ell_{ij}
=L.}
\tag{5.4}
$$



This saturates Item 201's global triple-free bound $R\le L$.  It also
satisfies the three-edge transfer-capacity gcd/lcm pattern with common gcd
$H=1$: in every triangle the three edge labels are pairwise coprime and
their lcm is their product.

A one-parent forest contains at most $r-1$ of the
$\binom r2$ edge labels.  To make the logarithmic comparison sharp, for
each $r$ choose the labels as distinct primes in an interval $[X,2X]$,
with $X$ sufficiently large.  The prime number theorem supplies at least
$\binom r2$ such primes.  Then



$$
\frac{\text{mass on any forest}}
     {\log R}
\le
\frac{(r-1)\log(2X)}{\binom r2\log X}
=\frac2r\left(1+\frac{\log2}{\log X}\right).
\tag{5.5}
$$



Letting first $X\to\infty$ and then $r\to\infty$, the forest fraction
tends to zero while all triple gcds remain one and $R=L$.

This proves:

> **TRIPLE/FOREST NONEXHAUSTION.**  Pairwise transfer divisibility,
> triple-gcd-one, and all one-parent forest bounds do not imply any strict
> aggregate saving below the unique CRT modulus.  Their sharp compatible
> ceiling is $R=L$.

The displayed parents are abstract integers, not actual beta denominators.
An actual recurrence-specific theorem could prevent this incidence graph;
the present local constraints do not.

## 6. Exhaustiveness decision

The current local architecture has two independent blind spots:



$$
\begin{array}{c|c|c}
\text{blind spot}&\text{sharp countermodel}&\text{new input required}\\ \hline
\text{fresh primitive content}&
\lambda\equiv1\pmod M&
\text{global support/height or actual period identity}\\
\text{pair-specific multi-parent reuse}&
P_i=\prod_{j\ne i}\ell_{ij},\ R=L&
\text{actual transfer-lcm/gcd distribution theorem}
\end{array}
\tag{6.1}
$$



Accordingly, the following entire strategy class is closed:

* add another finite Witt/Hasse digit on the same forced support and infer
  that the full content is now exhausted;
* combine local triple coprimality with one-parent forest bounds and infer a
  strict global multi-parent saving;
* add the higher-digit ceiling and matching ceiling without a primewise
  overlap theorem.

A future exhaustive ceiling must prove at least one statement outside this
class, for example:



$$
p\mid c_m\Longrightarrow p\in S_m
\quad\text{together with a uniform bound on }v_p(c_m),
\tag{6.2}
$$



or



$$
\log\operatorname{lcm}_{i<j}
\operatorname{odd}C_{n_j-n_i}(n_i)
\le(1-\eta)\times\text{the compatible displacement budget}
\tag{6.3}
$$



for the actual moving portfolio and some $\eta>0$, after all old factors
are removed.  Neither theorem is presently available.

Thus Item 388 changes the research decision but not a numerical ledger:
finite local digits and current matching-incidence axioms are now closed as
an exhaustiveness route.  The branch remains live only through genuinely
global actual-family arithmetic.

## 7. Strict labels

### PROVED

* The precise architecture and de-overlap decomposition (2.1)--(2.23).
* The fresh-scalar fiber theorem (3.3)--(3.4), at arbitrary row-dependent
  finite precision.
* The height-compatible two-realization theorem (3.5)--(3.6).
* The exact complete-graph multi-parent construction (5.1)--(5.4).
* Sharpness of $R\le L$ and the vanishing forest fraction (5.5).
* The exhaustiveness decision in Section 6.
* Zero booking.

### PROVED GLOBAL SCOPED INFORMATION-CLASS NO-GO

* Finite local Witt/Hasse digits on a declared support do not bound fresh
  common content outside that support.
* Adding any finite number of further digits does not change this conclusion.
* Triple-gcd-one and one-parent forest theorems do not give a strict
  multi-parent ceiling; the existing $R\le L$ bound is sharp.
* Combining these local data cannot make the mixed-cubic architecture
  exhaustive.

### EXACT FINITE ONLY

* The deterministic replay's declared moduli, scalar fibers, capacity
  arithmetic, complete-graph parents, gcds, lcms, and forest controls.
* Its primes and parents instantiate the algebraic constructions only; they
  are not actual mixed-cubic or beta rows and provide no density evidence.

### OPEN

* A complete actual support theorem and uniform excess-valuation bound for
  $c_m$.
* An all-depth actual arithmetic theorem strong enough to control the fresh
  complement, rather than another finite local digit formula.
* An actual recurrence-specific multi-parent lcm/gcd bound.
* Compatible overlap with booked Cartier and clearing content.
* Every still-live common-log cell, Route 1, and $e+\pi$.

### BOOKING



$$
\boxed{
\text{new beta capacity reduction}=0,
\qquad
\text{new mixed-cubic content ceiling}=0,
\qquad
\text{new Route-1 rate}=0.}
\tag{7.1}
$$



Here “new ceiling $=0$” means no numerical ceiling change, not that the
content ceiling is zero.

No canonical, master, status, checkpoint, research-log, or root-audit file is
edited by this work package.

## 8. Deterministic replay

From the archive root:

~~~text
python work/item388_mixed_cubic_local_data_nonexhaustion_certificate.py ^
  --output work/item388_mixed_cubic_local_data_nonexhaustion_certificate.replay.json
~~~

The checker uses only the Python standard library and exact integer or
decimal arithmetic.  It performs no actual target search, exceptional-prime
search, factor census, or asymptotic extrapolation.
