> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 371 — determinant-specific compatibility test for the fixed-$j=1$ cyclic companion

Date: 2026-09-01

## 1. Outcome and capacity first

The actual selector remains



$$
p=4h+6s+3,\qquad M=3h+4s+2,\qquad
n=2h,\qquad r=2s+1.                                    \tag{1.1}
$$



Item 369 constructed the exact cyclic companion



$$
\mathcal C_{h,s}
=\begin{bmatrix}-a_{r,n}&-Q_0(h,s)\\1&0\end{bmatrix},
\qquad
\chi_{\mathcal C}(X)=X^2+a_{r,n}X+Q_0.                  \tag{1.2}
$$



Hence



$$
-\operatorname {tr}\mathcal C=a_{r,n},\qquad
\det\mathcal C=Q_0.                                      \tag{1.3}
$$



The exact determinant divisor is therefore



$$
\boxed{\mathcal D_{\det}:\quad
Q_0=2c_T-c_L=0\pmod p.}                                  \tag{1.4}
$$



This is Item 360's already forced transverse divisor.  It is not a third
condition and receives no extra codimension credit merely because it has
been placed in a determinant.

This item tests whether (1.2) can be promoted from an additive complete
moment to a genuine bounded-conductor rank-two Frobenius system or a
pointwise local Frobenius product.  Three scoped obstructions result.

1. A lisse mod-$p$ Frobenius matrix is invertible at every unramified
   point.  The actual companion is singular whenever $Q_0=0$, including
   the predeclared actual row $(h,s,p)=(10,11,109)$.  Thus no lisse
   all-row realization can have characteristic polynomial (1.2).
2. The determinant of a product of local Frobenius matrices is the product
   of their local determinants.  The target $Q_0$ is instead a selected
   additive cancellation.  A universal pointwise-separable product cannot
   equal that sum.
3. In the standard crystalline class with one fixed Tate normalization
   and unit normalized full determinant, reduction of the full determinant
   is either everywhere a unit or everywhere zero after undoing the fixed
   twist.  The actual $Q_0$ takes both nonzero and zero values.

Literal Kummer and Artin--Schreier realizations of the finite logarithm
also have conductor growing linearly with $p$.

These theorems close the direct *full determinant* architectures.  They do
not rule out a Hasse subdeterminant, a varying-slope or singular
$F$-crystal, or a different target-specific cohomological compression.

All identities reach every actual row and therefore have raw capacity



$$
{M\over6}+o(M),\qquad {1\over36}\text{ per }6M.           \tag{1.5}
$$



No asymptotic horizontal theorem is proved.  Consequently



$$
\boxed{
\text{new linear log rate}=0,\quad
\text{new fixed-}j=1\text{ capacity reduction}=0,\quad
\text{booking}=0.}                                       \tag{1.6}
$$



The $1/36$ ceiling is retained and Route 1 remains ACTIVE.

## 2. What would have to be a Frobenius determinant

Item 369's extension-field identity is



$$
\mathcal C_{h,s}
=\sum_{x\in\mathbb F_{p^2}^{\times}}
\begin{bmatrix}
x^{-n}G(x)^{p-r}&
2x^{-T}F_Q(x)-x^{-L}F_Q(x)\\
-1&0
\end{bmatrix},                                           \tag{2.1}
$$



where



$$
F_Q(x)=P_0(x)\mathscr L_p(x^2),                          \tag{2.2}
$$





$$
P_0(x)=(1-x)^{2h}(1+x)(1+x^2)^{2s},                     \tag{2.3}
$$





$$
T=2h+6s+2,\qquad L=4h+4s+2,                             \tag{2.4}
$$



and



$$
\mathscr L_p(w)={(1+w)^p-1-w^p\over p}\pmod p.           \tag{2.5}
$$



Coefficient orthogonality gives



$$
\sum_x x^{-n}G(x)^{p-r}=-a_{r,n},                        \tag{2.6}
$$





$$
\sum_x\bigl(2x^{-T}F_Q(x)-x^{-L}F_Q(x)\bigr)=-Q_0,       \tag{2.7}
$$



and $\sum_x(-1)=1$ in characteristic $p$.  Thus (2.1)
is exact.

But it is an **additive** global matrix moment:



$$
\mathcal C=\sum_x\mathcal K(x).                          \tag{2.8}
$$



A Frobenius representation supplies a matrix through composition or
monodromy, and a product architecture has the form



$$
\Phi=\prod_x\Phi_x.                                      \tag{2.9}
$$



The two operations behave differently under determinant:



$$
\det\!\left(\sum_x\mathcal K(x)\right)
\quad\text{has no local factorization, whereas}\quad
\det\!\left(\prod_x\Phi_x\right)=\prod_x\det\Phi_x.      \tag{2.10}
$$



The companion trick in Item 369 deliberately placed the additive scalar
$Q_0$ in the determinant of a *sum*.  Equation (2.10) is the structural
gap that a genuine realization would have to bridge.

## 3. Exact lisse obstruction

Let $\mathcal V$ be a rank-two lisse sheaf with residue coefficient
field $k$ of characteristic $p$.  At every unramified point $t$,
geometric or arithmetic Frobenius acts by an automorphism:



$$
\rho(\operatorname {Frob}_t)\in\operatorname {GL}_2(k).
\tag{3.1}
$$



Therefore



$$
\det\rho(\operatorname {Frob}_t)\ne0.                    \tag{3.2}
$$



This is independent of purity, monodromy size, or conductor estimates.
It follows immediately that no such Frobenius can have characteristic
polynomial



$$
X^2+a_{r,n}X+Q_0                                        \tag{3.3}
$$



at a row where $Q_0=0$.

The obstruction occurs on the actual tied family, not merely in an
ambient model.  The predeclared row



$$
(h,s,p)=(10,11,109)                                      \tag{3.4}
$$



has



$$
(a_{r,n},Q_0)=(70,0)\pmod{109}.                          \tag{3.5}
$$



Thus $\mathcal C$ is singular on an actual row.  Hence



$$
\boxed{
\begin{gathered}
\text{there is no rank-two lisse mod-}p\text{ system on a good locus}\\
\text{containing all actual rows whose Frobenius polynomial is (3.3).}
\end{gathered}}                                          \tag{3.6}
$$



Deleting $Q_0=0$ from the lisse locus does not solve the research
problem: it deletes exactly the determinant divisor whose weighted mass
must be controlled.

Equation (3.6) is about a literal residue-characteristic realization.
A characteristic-zero $\ell$-adic system whose chosen integral lattice
has singular reduction at $\ell=p$ is a different question; it is
addressed only within the fixed-normalization crystalline class below.

## 4. Pointwise local Frobenius products cannot create the additive divisor

Suppose local matrices $\Phi_i$ depend separately on local inputs
$t_i$.  Then



$$
\det(\Phi_1\cdots\Phi_N)
=\prod_{i=1}^N f_i(t_i),\qquad f_i=\det\Phi_i.            \tag{4.1}
$$



If all $\Phi_i$ are genuine lisse Frobenius matrices, every factor is
nonzero and the product never vanishes.  Even if singular local matrices
are admitted, the determinant-zero locus is a union of local factor-zero
loci.  By contrast, the exact transverse coordinate is a global
cancellation of the selected coefficient contributions.

There is a universal two-variable algebraic test.  For a function
$F(x,y)$, put



$$
\Delta(F)=F\,F_{xy}-F_xF_y.                              \tag{4.2}
$$



For every multiplicatively separable function



$$
F(x,y)=f(x)g(y),                                         \tag{4.3}
$$



one has



$$
\Delta(F)=0.                                             \tag{4.4}
$$



For the additive selector,



$$
F(x,y)=x+y,\qquad \Delta(F)=-1.                          \tag{4.5}
$$



Therefore $x+y$ cannot equal a pointwise product
$f(x)g(y)$.  Restricting all but two local inputs proves the same
obstruction for any number of independently varying contributions:



$$
\boxed{
\text{a universal pointwise product of local determinant factors cannot
equal the additive transverse selector.}}               \tag{4.6}
$$



This proof works in every characteristic because $-1\ne0$.

The scope is important.  The exact values attached to the tied orbit are
not algebraically independent local variables.  A new target-specific
identity could in principle collapse their sum to a product.  None is
known or proved.  A factor allowed to depend on the entire global sum
$Q_0$ trivially escapes (4.6), but then it is no longer a pointwise local
Frobenius factor and supplies no new arithmetic theorem.

## 5. Fixed-normalization crystalline full determinants

Consider the standard integral crystalline class in which, on one
connected good locus, a single Tate normalization makes the full
rank-two Frobenius determinant a unit.  Write the unnormalized determinant
as



$$
\det\Phi=p^\mu u,\qquad u\text{ a unit},                 \tag{5.1}
$$



where the total exponent $\mu\ge0$ is fixed by the normalization.
Reduction modulo $p$ gives the dichotomy



$$
\begin{cases}
\det\Phi\ne0\pmod p\text{ at every good point},&\mu=0,\\
\det\Phi=0\pmod p\text{ at every good point},&\mu>0.
\end{cases}                                              \tag{5.2}
$$



But the declared actual rows give



$$
Q_0=9,\ 14,\ 30,\ 0                                     \tag{5.3}
$$



at $p=13,17,47,109$, respectively.  Hence $Q_0$ is neither uniformly
a unit nor uniformly zero.  It follows that



$$
\boxed{
Q_0\text{ cannot be the full Frobenius determinant in the
fixed-normalization class (5.1).}}                       \tag{5.4}
$$



This is a scoped crystalline no-go, not a theorem against all possible
$p$-adic cohomology.  Selective vanishing can occur for a Hasse
subdeterminant or a map on a graded piece even when the full Frobenius is
an isomorphism after inverting $p$.  Varying lattices, varying total
slopes, singular extensions across $Q_0=0$, and a different
target-specific $F$-crystal are also outside (5.4).  Any such proposal
must construct the subquotient and prove that its Hasse divisor is exactly
(1.4); companion notation alone does not do so.

## 6. Literal bounded-conductor realizations still fail

Item 366 proved



$$
\mathscr L_p'(w)={1-w^{p-1}\over1+w}.                    \tag{6.1}
$$



Every root of $\mathscr L_p$ has multiplicity at most two, and therefore



$$
\mathscr L_p(z^2)\text{ has at least }p-2
\text{ distinct roots}.                                 \tag{6.2}
$$



For $p\ge13$, multiplicities one and two are nonzero modulo both
$p-1$ and $p^2-1$.  A literal full-order Kummer pullback is ramified
at each root, so its finite conductor support is at least $p-2$.

The direct additive-character alternative is also unbounded.  The
polynomial has degree



$$
\deg\mathscr L_p(z^2)=2(p-1),\qquad p\nmid2(p-1).        \tag{6.3}
$$



It is already reduced with respect to Artin--Schreier $g^p-g$
subtraction at its leading term.  Thus the literal Artin--Schreier
pullback has Swan conductor



$$
2(p-1)                                                   \tag{6.4}
$$



at infinity.

Consequently



$$
\boxed{
\text{neither literal full-order Kummer nor literal Artin--Schreier
realization has bounded conductor.}}                    \tag{6.5}
$$



This does not exclude a nonliteral unipotent, Artin--Schreier--Witt, or
cohomological compression with cancellations of apparent singularities.
No such compression is presently constructed.

## 7. Declared exact controls

The deterministic certificate uses only four rows predeclared before this
item.  It performs no prime or collision scan.

| $(h,s,p)$ | $M$ | $a_{r,n}$ | $Q_0=\det\mathcal C$ | companion invertible | roots of $\mathscr L_p$ |
|---|---:|---:|---:|---|---:|
| $(1,1,13)$ | $9$ | $0$ | $9$ | yes | $10$ |
| $(2,1,17)$ | $12$ | $8$ | $14$ | yes | $16$ |
| $(8,2,47)$ | $34$ | $0$ | $30$ | yes | $46$ |
| $(10,11,109)$ | $76$ | $70$ | $0$ | no | $106$ |

For every row the certificate independently reconstructs $a_{r,n}$,
the finite-log coefficients $c_T,c_L$, $Q_0=2c_T-c_L$, the companion
determinant, and the exact algebraic-closure root count.

These are structural controls only.  The determinant-zero row is not a
full collision, and no displayed row is used as asymptotic evidence.

## 8. Capacity and the viable theorem that remains

Define



$$
\mathcal W_{\det,\operatorname {tr}}(M)
=\sum_{\substack{s\in\mathcal S_M,\ p_s\ \mathrm{prime}\\
\operatorname {tr}\mathcal C_{h_s,s}=0\ (\mathrm{mod}\ p_s)\\
\det\mathcal C_{h_s,s}=0\ (\mathrm{mod}\ p_s)}}
\log p_s.                                                \tag{8.1}
$$



Equations (1.2)--(1.4) give



$$
\mathcal W_{\det,\operatorname {tr}}(M)
=\mathcal W_{H,Q}(M),\qquad
\mathcal W_{\rm full}(M)
\leq\mathcal W_{\det,\operatorname {tr}}(M).             \tag{8.2}
$$



The viable ledger theorem is still



$$
\boxed{\mathcal W_{\det,\operatorname {tr}}(M)=o(M).}    \tag{8.3}
$$



If (8.3) were proved, it would remove the full $1/36$ fixed-$j=1$
ceiling.  A strict bound below $M/6$ would already yield a partial
saving.

The direct lisse, fixed-normalization full crystalline determinant,
pointwise product, and literal bounded-support routes above do not supply
(8.3).  The remaining determinant-specific options require genuinely new
structure:

- a Hasse subdeterminant with an exact actual-family bridge;
- a nonliteral bounded-conductor $F$-crystal or cohomological
  compression;
- horizontal zero-density for the exact integer determinant carrier; or
- an average-gcd theorem coupling that carrier to the Hasse trace carrier.

No such theorem is proved here, so no mass is booked.

## 9. Strict decision

### PROVED

- the exact determinant divisor is the existing transverse condition
  $Q_0=0$;
- the lisse mod-$p$ invertibility obstruction (3.6);
- the universal pointwise local-product separability obstruction (4.6);
- the fixed-normalization full crystalline determinant obstruction (5.4);
- literal Kummer and Artin--Schreier conductor growth (6.5);
- zero booking.

### EXACT FINITE ONLY

- four predeclared controls with both zero and nonzero determinant values;
- no collision scan, full-collision claim, or density inference.

### OPEN

- a Hasse subdeterminant or varying-slope $F$-crystal realization;
- a target-specific nonlocal identity or bounded-conductor compression;
- horizontal determinant-trace nonconcentration or an average-gcd theorem;
- weighted joint-zero density, any strict fixed-$j=1$ ceiling reduction,
  Route 1, and every conclusion about $e+\pi$.

## 10. Ledger consequence



$$
\begin{array}{c|c}
\text{quantity}&\text{Item 371 value}\\ \hline
\text{actual rows reached}&\text{all}\\
\text{new determinant divisor}&0\\
\text{new proved excluded log mass}&0\\
\text{new fixed-}j=1\text{ capacity reduction}&0\\
\text{retained fixed-}j=1\text{ ceiling per }6M&1/36
\end{array}                                               \tag{10.1}
$$



Item 371 shows that determinant notation does not turn an additive
coefficient cancellation into multiplicative Frobenius arithmetic.  A
ledger gain now requires a genuinely constructed Hasse subdeterminant or
another horizontal arithmetic theorem.
