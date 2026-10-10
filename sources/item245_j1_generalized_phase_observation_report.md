> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 245 — generalized $\pm i$ observations on the actual $j=1$ family

Checked: 2026-08-31 (Beijing time)

## 1. Scope and verdict

Retain the actual rows


$$
p=4h+6s+3=2r+6s+3,\qquad r=2h,\qquad h,s\geq1,               \tag{1.1}
$$


and Item 242's kernel


$$
\mathcal H_E={R_E\over(1+z^{2p})^5}.                         \tag{1.2}
$$


This item resolves the finite phase-state interface for the two actual
short convolutions $P_0,P_1$.

**PROVED — an exact family-specific dependency.**  In the target
$p$-section, write $Z=z^p$, $Q=1+Z^2$, and expand the numerator
uniquely as


$$
A_\nu\equiv c_{\nu,0}+Qc_{\nu,1}+Q^2c_{\nu,2}
                  +Q^3c_{\nu,3}+Q^4c_{\nu,4}\pmod {Q^5},
 \qquad \deg c_{\nu,j}<2.                                    \tag{1.3}
$$


The term $c_{\nu,4}/Q$ is exactly the old simple-pole
$\pm i$ pair.  On every actual row,


$$
\boxed{c_{\nu,4}=0.}                 \tag{1.4}
$$


This follows from the row relation and the exact degrees of the two
actual $P_\nu$, not from a finite rank scan.

Thus the independent simple-pole pair is absent from these target
sections.  The remaining state is the eight-dimensional generalized
quotient


$$
\mathcal R_4=\mathbb F_p[Z]/(1+Z^2)^4.     \tag{1.5}
$$


This statement does not say that the full phase orbit has no ordinary
Jordan descendants; it says there is no separately excited
$c_{\nu,4}/Q$ summand.

**PROVED — exact terminal/observation determinant.**  Let


$$
\bar A_\nu=A_\nu\bmod Q^4,\qquad
 \bar A_\nu\bmod Q=\alpha_\nu+\beta_\nu Z.                    \tag{1.6}
$$


The eight-phase terminal/Krylov matrix $\mathcal T_\nu$ of the actual
generalized state satisfies


$$
\boxed{\qquad
 \det\mathcal T_\nu=(\alpha_\nu^2+\beta_\nu^2)^4.
 \qquad}                                                       \tag{1.7}
$$


Consequently the actual coordinate excites all eight generalized
directions precisely when
$\alpha_\nu^2+\beta_\nu^2\ne0$.

**PROVED — closed finite-sum factors.**  Put


$$
q_\nu=2s-\nu,\qquad a_\nu=p-q_\nu-1,\qquad
 B_0=\sum_{k=1}^{p-1}{(-1)^{k-1}z^{2k}\over k},               \tag{1.8}
$$


and write $B_0^2P_\nu=\sum_nt_{\nu,n}z^n$.  Then


$$
\boxed{\begin{aligned}
 \alpha_\nu&=-24\sum_{j\geq0}(-1)^j
                       t_{\nu,a_\nu+2jp},\\
 \beta_\nu&=-24\sum_{j\geq0}(-1)^j
                       t_{\nu,a_\nu+(2j+1)p}.
\end{aligned}}                                                \tag{1.9}
$$


All sums are finite and every denominator in $B_0$ is a $p$-unit.
Equations (1.7)--(1.9) are an all-row determinant factorization.

**PROVED — reciprocity aligns, but does not identify, the two
coordinates.**  If $C_{\nu,a}(Z)$ is the $a$-th $p$-section of
$B_0^2P_\nu$, then


$$
C_{\nu,a_\nu}(Z)=Z^3C_{\nu,b}(Z^{-1}),
 \qquad b=p-r-1,                                               \tag{1.10}
$$


for both $\nu=0,1$.  The common residue $b$ is forced by (1.1).
The polynomials $P_0$ and $P_1$ remain different, so (1.10) is an
alignment, not a dependency between their determinant factors.

**PROVED — exact individual and joint rank classifications.**  Over an
algebraic closure, let $k_{\nu,+},k_{\nu,-}\in\{0,1,2,3,4\}$ be the
orders of $\bar A_\nu$ at the two roots of $Q$, truncated at four.
Then


$$
\operatorname {rank}\mathcal T_\nu
      =8-k_{\nu,+}-k_{\nu,-}.                                 \tag{1.11}
$$


For the two-coordinate stacked matrix,


$$
\operatorname {rank}
 \begin{pmatrix}\mathcal T_0\\\mathcal T_1\end{pmatrix}
 =8-\min(k_{0,+},k_{1,+})-\min(k_{0,-},k_{1,-}).              \tag{1.12}
$$


Thus the two coordinates jointly retain full generalized
observability exactly when they have no common root factor of $Q$.

**EXACT FINITE ONLY.**  Through $p\leq601$, all 2,435 actual rows
give 4,851 rank-eight coordinate matrices, 18 rank-seven matrices, and
one rank-six matrix.  No row has a joint rank drop.  These counts are
not extrapolated.

**OPEN.**  It is not proved that at least one of the two factors in
(1.7) is nonzero on every actual row.  Therefore Item 245 supplies no
all-prime common-log exclusion or Route-1 rate.

## 2. The target $p$-sections

The two actual polynomials and targets are


$$
\begin{aligned}
 P_0&=(1-z)^r(1+z)(1+z^2)^{2s},&
 N_0&=3p-2s-1,\\
 P_1&=(1-z)^r(1+z)^4(1+z^2)^{2s-1},&
 N_1&=3p-2s.                                                   \tag{2.1}
\end{aligned}
$$


Equivalently,


$$
P_0=(1+z)(1+z^2)W,\qquad
 P_1=(1+z)^4W,                                                \tag{2.2}
$$


where $W=(1-z)^r(1+z^2)^{2s-1}$.

Their degrees are


$$
d_\nu=r+4s+1+\nu,\qquad
 N_\nu=a_\nu+2p,\qquad a_\nu=p-q_\nu-1.                       \tag{2.3}
$$


Set


$$
S_\nu(z)=R_E(z)P_\nu(z)
         =\sum_{a=0}^{p-1}z^aA_{\nu,a}(Z),\qquad Z=z^p,        \tag{2.4}
$$


and abbreviate $A_\nu=A_{\nu,a_\nu}$.  The phase-shifted coordinate
at target residue $a_\nu$ is the coefficient sequence of


$$
{A_\nu(Z)\over Q(Z)^5}.          \tag{2.5}
$$


The actual target begins at phase two because of (2.3).  Translating
the phase origin is an invertible operation and will not affect any
rank or determinant below.

## 3. Why the independent old pair vanishes

Item 242 gives


$$
\deg R_E\leq8p-1.                   \tag{3.1}
$$


If $A_\nu$ has a term $Z^m$, then


$$
\begin{aligned}
 a_\nu+mp
 &\leq\deg(R_EP_\nu)\\
 &\leq8p-1+d_\nu.
\end{aligned}                                                  \tag{3.2}
$$


Therefore


$$
mp\leq7p+d_\nu+q_\nu.                                       \tag{3.3}
$$


But the row relation gives


$$
d_\nu+q_\nu=r+6s+1=p-r-2<p.                                 \tag{3.4}
$$


Equations (3.3)--(3.4) imply $m\leq7$, hence


$$
\deg A_\nu\leq7.                 \tag{3.5}
$$


Since $Q^4$ has degree eight, the fifth digit in (1.3) must vanish.
This proves (1.4) for both actual short convolutions on every row.

Dividing (1.3) by $Q^5$ clarifies the meaning:


$$
{A_\nu\over Q^5}
 ={c_{\nu,0}\over Q^5}+{c_{\nu,1}\over Q^4}
  +{c_{\nu,2}\over Q^3}+{c_{\nu,3}\over Q^2}
  +{c_{\nu,4}\over Q}.                                       \tag{3.6}
$$


The last summand is the old semisimple $\pm i$ pair from Item 233.
There is no $q_0$ eigenmode in this $Q$-primary kernel.  Applying
one factor $Q(S_p)=S_p^2+1$ kills the simple pair and identifies the
remaining quotient with $\mathcal R_4$.  Equation (1.4) shows that,
for the actual target sections, this quotient contains all independent
input digits.

## 4. The universal eight-phase observation matrix

Use the monomial basis


$$
1,Z,\ldots,Z^7
\quad\text{of}\quad
                 \mathcal R_4=\mathbb F_p[Z]/Q^4.             \tag{4.1}
$$


For a numerator $Z^j$, the normalized generalized sequence has
generating function $Z^j/Q^4$.  Let $\mathcal B$ record its first
eight phase coefficients:


$$
\mathcal B_{m,j}=[Z^m]{Z^j\over(1+Z^2)^4},
 \qquad 0\leq m,j\leq7.                                      \tag{4.2}
$$


Explicitly,


$$
\mathcal B_{m,j}=
 \begin{cases}
  (-1)^k\binom{k+3}{3},&m-j=2k\geq0,\\
  0,&\text{otherwise}.
 \end{cases}                                                   \tag{4.3}
$$


This matrix is lower triangular with diagonal entries one:


$$
\det\mathcal B=1.               \tag{4.4}
$$


Thus eight consecutive phase observations recover every generalized
state.  Beginning the window at the actual target phase, or after the
one-$Q$ quotient, merely composes $\mathcal B$ with an invertible
phase translation.

Now let $\mathcal K_\nu$ be the Krylov matrix whose columns are


$$
\bar A_\nu,\ Z\bar A_\nu,\ldots,Z^7\bar A_\nu
 \quad\text{in }\mathcal R_4.                                \tag{4.5}
$$


Define the actual terminal/observation matrix by


$$
\mathcal T_\nu=\mathcal B\mathcal K_\nu.
                                                                  \tag{4.6}
$$


This normalization is intrinsic to the generalized $Q$-primary
module.  It is not obtained by assuming that Item 233's $3\times3$
matrix $N$ already lifts.

## 5. Determinant and rank factorization

The matrix $\mathcal K_\nu$ is multiplication by $\bar A_\nu$ in
$\mathcal R_4$.  Its determinant is the norm, equivalently the
resultant:


$$
\begin{aligned}
 \det\mathcal K_\nu
 &=\operatorname {Res}(Q^4,\bar A_\nu)\\
 &=\operatorname {Res}(Q,\alpha_\nu+\beta_\nu Z)^4\\
 &=(\alpha_\nu^2+\beta_\nu^2)^4.                              \tag{5.1}
\end{aligned}
$$


Equation (4.4) then proves (1.7).

Over an algebraic closure,


$$
Q=(Z-\iota)(Z+\iota),\qquad \iota^2=-1,                     \tag{5.2}
$$


and the Chinese remainder theorem splits $\mathcal R_4$ into two
local rings of length four.  Multiplication by an element of root order
$k$ has rank $4-k$ on that local component.  This proves (1.11).

For the stacked map, the kernel is the intersection of the two
multiplication kernels.  On either root component its dimension is the
minimum of the two root orders.  This proves (1.12).

At the leading-digit level, a common root of the two coordinates is
equivalent to


$$
\begin{aligned}
 \alpha_0^2+\beta_0^2&=0,\\
 \alpha_1^2+\beta_1^2&=0,\\
 \alpha_0\beta_1-\alpha_1\beta_0&=0.                          \tag{5.3}
\end{aligned}
$$


Higher root orders in (1.12) are then read from the subsequent
$Q$-adic digits.

If $p\equiv3\pmod4$, $Q$ is irreducible and the two root orders are
equal.  Individual ranks are then $8,6,4,2,0$.  If
$p\equiv1\pmod4$, the roots split and odd ranks can occur.

## 6. Closed leading pair and reciprocity

Modulo $V=1+z^{2p}$, Item 242's numerator satisfies


$$
R_E\equiv6U^4B_0^2,\qquad U=1-z^p.   \tag{6.1}
$$


In the $p$-section ring, $U=1-Z$, and modulo $Q=1+Z^2$,


$$
6(1-Z)^4\equiv-24.                  \tag{6.2}
$$


Consequently


$$
\alpha_\nu+\beta_\nu Z
 \equiv-24\,C_{\nu,a_\nu}(Z)\pmod Q,                          \tag{6.3}
$$


where $C_{\nu,a}$ is the $a$-th $p$-section of $B_0^2P_\nu$.
Separating even and odd section indices in (6.3) gives exactly (1.9).

There is also an exact reciprocity normalization.  Direct reindexing
gives


$$
z^{2p}B_0(1/z)=B_0(z).                 \tag{6.4}
$$


Because $r$ is even, $P_\nu$ is reciprocal of degree $d_\nu$.
Thus $B_0^2P_\nu$ is reciprocal about degree $4p+d_\nu$.

The row equation produces the common reflected residue:


$$
\begin{aligned}
 d_\nu-a_\nu
 &=r+6s+2-p\\
 &=-r-1=(p-r-1)-p.                                           \tag{6.5}
\end{aligned}
$$


Set $b=p-r-1$.  If $a_\nu+mp$ is reflected about
$4p+d_\nu$, its partner is


$$
b+(3-m)p.                                                    \tag{6.6}
$$


Summing (6.6) proves (1.10).  Modulo $Q$, inversion sends
$Z^{-1}$ to $-Z$, so reciprocity preserves
$\alpha_\nu^2+\beta_\nu^2$.

The key limitation is now explicit: (1.10) sends both coordinates to
the same residue $b$, but the two polynomials


$$
P_0=(1+z)(1+z^2)W,\qquad P_1=(1+z)^4W                       \tag{6.7}
$$


remain distinct.  Reciprocity alone supplies no equality between their
leading pairs.

## 7. Deterministic replay and finite census

The standard-library checker
work/item245_j1_generalized_phase_observation_certificate.py verifies
on every actual row through $p\leq151$:

- the five-digit $Q$-adic decomposition and the all-zero
  $c_{\nu,4}$;
- the full numerator leading pair against the independent short formula
  (1.9);
- the reciprocity identity (1.10);
- $\det\mathcal B=1$ and the determinant formula (1.7);
- the exact ranks of the two $8\times8$ matrices.

For the sample row $(p,h,s)=(29,5,1)$,


$$
\begin{array}{c|c|c|c|c}
\nu&(\alpha_\nu,\beta_\nu)&
\alpha_\nu^2+\beta_\nu^2&
\det\mathcal T_\nu&\operatorname {rank}\mathcal T_\nu\\ \hline
0&(26,17)&8&7&8\\
1&(1,16)&25&24&8.
\end{array}                                                     \tag{7.1}
$$


The two terminal-matrix SHA-256 values are


$$
\begin{aligned}
\nu=0:\quad&
\texttt{c1e4fa3e4bbe3dca988b698f8bb42035ba5466520819a7cdcd04bdc61c7ed7ca},\\
\nu=1:\quad&
\texttt{0bb90a2095993ab011056ec5f27be9a7b8f8dcee050d8934d84a3aea0aa4b528}.
                                                                  \tag{7.2}
\end{aligned}
$$



The separate exact census through $p\leq601$ contains


$$
\begin{array}{c|rrrrrrrrr}
\operatorname {rank}&0&1&2&3&4&5&6&7&8\\ \hline
\text{coordinate count}&0&0&0&0&0&0&1&18&4851.
\end{array}                                                     \tag{7.3}
$$


The unique rank-six coordinate is


$$
(p,h,s,\nu)=(59,2,8,1).               \tag{7.4}
$$


The companion certificate lists all 18 rank-seven records.  None of
the 2,435 rows has a joint rank drop.

Everything in (7.1)--(7.4), including the absence of a joint drop, is
**EXACT FINITE ONLY**.  It is not evidence promoted to an all-row
nonvanishing statement.

## 8. Consequence for the $p^3$ branch

Item 242 showed that the $p^3$ equations observe two new kernel
coordinates not universally determined by the $u/v$ denominator
tower.  Item 245 now sharpens the internal structure:

- the separately excited old $\pm i$ digit is absent identically;
- the actual observations live in the eight-dimensional generalized
  quotient;
- each coordinate is fully observable exactly off its explicit norm
  factor in (1.7);
- the two coordinates are jointly observable exactly off the common
  root locus classified by (1.12).

This does not yet turn the two $p^3$ equations into an all-row scalar
obstruction.  The generalized initial state is arithmetically fixed by
the binomial kernel, but no theorem here excludes its joint exceptional
locus for every prime.

## 9. Final ledger

### PROVED

- The actual-family dependency $c_{\nu,4}=0$.
- The eight-dimensional generalized $Q$-primary state and universal
  phase observation matrix.
- The determinant factorization (1.7) and finite-sum factors (1.9).
- The individual and joint root-valuation rank formulas
  (1.11)--(1.12).
- The reciprocity alignment (1.10), with a common reflected residue.

### EXACT FINITE ONLY

- Every bounded row count, rank count, exceptional record, sample
  matrix, and digest in the certificate.
- No joint rank drop through $p\leq601$.

### OPEN

- All-row nonvanishing of at least one of the two norm factors.
- An exact family-specific identity excluding the joint root locus.
- An all-row $p^3$ terminal obstruction after the generalized state is
  coupled to the divided moment.
- Any all-prime common-log exclusion, density theorem, Route-1
  exponent, or conclusion about $e+\pi$.
