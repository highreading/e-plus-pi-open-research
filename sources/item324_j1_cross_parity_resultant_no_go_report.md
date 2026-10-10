> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 324 — cross-parity resultant, even-overlap localization, and the selected-slice no-go

Date: 2026-08-31

## 1. Outcome and capacity first

Retain the actual Item-308 integer containers $D_{s,\epsilon}$ and
Item 321's rational normalization



$$
q_{s,\epsilon}={D_{s,\epsilon}\over9\,2^{27s+21}}.
                                                               \tag{1.1}
$$



Writing $Z_s=X_s+iY_s$, this item derives both parity quadrics in
the rational coordinates $(A_s,X_s,Y_s)$ and proves, uniformly in
$r=s\bmod4$,



$$
\boxed{
 \operatorname {Res}_{A}
 (q_{r,0},q_{r,1})
 =64(X^2+Y^2)^2=64(Z\overline Z)^2.}                       \tag{1.2}
$$



This does give one genuine arithmetic localization theorem.  If $s$
is even and an actual prime divides **both** parity containers, then
$p\equiv3\pmod4$.  Equation (1.2) forces $X=Y=0$, and either
quadric then forces $A=0$.  The first row of Item 321's actual
fundamental matrix vanishes, so its Casoratian $W_s$ vanishes.  Item
321 therefore confines every such prime to its already explicit
Casoratian exceptional support.  At fixed $M$,



$$
\boxed{
 \sum_{\substack{s\in\mathcal S_M,\ s\ {\rm even}\\
                  p_s\ {\rm prime}\\
                  p_s\mid D_{s,0},\ p_s\mid D_{s,1}}}
 \log p_s=O(\log M)=o(M).}                                 \tag{1.3}
$$



However, (1.3) is not a bound for the actual selected collision set.
On one fixed-$M$ slice, increasing $s$ by three decreases $h$
by four.  Thus $h\bmod4$, and in particular
$\epsilon=h\bmod2$, is constant on the entire slice.  The pinned
Item-308 implication supplies only



$$
p_s\mid D_{s,\epsilon_M};          \tag{1.4}
$$



it supplies no divisibility of $D_{s,1-\epsilon_M}$.  The preselected
exact row $(M,s,h,p)=(34,2,8,47)$ makes this failure concrete at the
Item-308 eliminant level:



$$
a_2+b_{2,0}w_8\equiv0,\qquad
 D_{2,0}\equiv0,\qquad D_{2,1}\equiv19\pmod {47}.          \tag{1.5}
$$



This row is not asserted to be an Item-264 full two-coordinate
collision.  Its exact role is to disprove promotion of the selected
Item-308 event to a two-parity event.

For odd $s$, the cross-parity intersection itself is not empty:
because every actual prime is $1\pmod4$, the two quadrics meet in four
nonzero projective lines.  This exact geometry produces no exclusion of
the actual pinned initial state.

Consequently the cross-parity resultant closes only a sharply defined
information class:



$$
\boxed{
 \text{gcds or resultants requiring both parity containers cannot bound}
 \ \mathcal W_D(M)\text{ or }\mathcal W_{\rm off}(M)
 \text{ without a new bridge forcing the unused parity}.} \tag{1.6}
$$



No such bridge is proved.  Hence



$$
\boxed{\text{new linear log rate}=0,\qquad
        \text{new fixed-}j=1\text{ capacity reduction}=0.} \tag{1.7}
$$



The fixed-$j=1$ ceiling remains $1/36$ per $6M$.

## 2. Exact rational-coordinate quadrics

Item 317 gives



$$
\begin{aligned}
q_{s,\epsilon}={}&A_s^2
-2\delta_s(-i)^sZ_s^2
-2\delta_si^s\overline Z_s^{\,2}\\
&\hspace{34mm}-4(-1)^\epsilon\delta_sZ_s\overline Z_s,
\qquad
\delta_s=(-1)^{s(s+1)/2+1}.                              \tag{2.1}
\end{aligned}
$$



Put $Z=X+iY$, $\overline Z=X-iY$.  Exact expansion of (2.1)
gives



$$
\begin{array}{c|cc}
r=s\bmod4&q_{r,0}&q_{r,1}\\ \hline
0&A^2+8X^2&A^2-8Y^2\\
1&A^2-4(X+Y)^2&A^2+4(X-Y)^2\\
2&A^2-8Y^2&A^2+8X^2\\
3&A^2+4(X-Y)^2&A^2-4(X+Y)^2.
\end{array}                                                \tag{2.2}
$$



For monic quadratics $A^2+u$ and $A^2+v$,



$$
\operatorname {Res}_A(A^2+u,A^2+v)
                 =(v-u)^2.                                \tag{2.3}
$$



In every row of (2.2), $v-u=\pm8(X^2+Y^2)$.  Equations
(2.2)--(2.3) prove (1.2) without a finite fit or a prime scan.

All reductions are legitimate on an actual row.  Item 308 proves that
the denominators of $A_s,B_s$, hence those of $X_s,Y_s$, have
rational-prime support contained in $\{2,3\}$.  Equation (1.1) only
adds powers of two and the factor $9$.  Every actual prime satisfies



$$
p=4h+6s+3\geq13,                 \tag{2.4}
$$



so every discarded scaling is a $p$-unit.

## 3. Even rows: simultaneous parity collision is thin

Modulo four,



$$
p\equiv2s+3\pmod4.               \tag{3.1}
$$



Thus even $s$ gives $p\equiv3\pmod4$.  Suppose that an actual
prime divides both $D_{s,0}$ and $D_{s,1}$.  By the unit audit it
annihilates both quadrics in (2.2).  The resultant identity gives



$$
X_s^2+Y_s^2=0\pmod p.             \tag{3.2}
$$



Since $-1$ is a nonsquare modulo a prime $3\pmod4$, (3.2) implies
$X_s=Y_s=0$.  Either row of (2.2) then gives $A_s=0$.
Consequently



$$
(A_s,Z_s,\overline Z_s)=(0,0,0)\pmod p,                 \tag{3.3}
$$



and the first row of Item 321's matrix



$$
F_s=\begin{pmatrix}
A_s&Z_s&\overline Z_s\\
A_{s+1}&Z_{s+1}&\overline Z_{s+1}\\
A_{s+2}&Z_{s+2}&\overline Z_{s+2}
\end{pmatrix}                                             \tag{3.4}
$$



vanishes.  Hence $W_s=\det F_s=0\pmod p$.

Item 321 proves on every actual row



$$
W_s=0\pmod p
 \quad\Longleftrightarrow\quad
 h=1\ \text{or}\ p\mid Q(s),
 \qquad Q(s)=660s^2+1600s+779.                            \tag{3.5}
$$



At fixed $M$, its division-free identity is



$$
\begin{aligned}
Q(s)-8(330M^2-235M+18)
={}&5(66s-132M+127)\\
&\cdot(4M+2s+1).                                         \tag{3.6}
\end{aligned}
$$



Because $4M+2s+1=3p_s$, every $h\geq2$ prime in (3.5)
divides the nonzero degree-two integer



$$
R(M)=330M^2-235M+18
=330(M-1)^2+425(M-1)+113.                                 \tag{3.7}
$$



The $h=1$ case contributes at most one fixed-$M$ row.  The map
$s\mapsto p_s$ is injective, so (3.6)--(3.7) give (1.3).
This theorem controls only the intersection of the two parity-container
zero sets.

## 4. Odd rows: exact nonzero intersection geometry

For odd $s$, equation (3.1) gives $p\equiv1\pmod4$.  The unordered
pair of quadrics in (2.2) is



$$
f=A^2-4(X+Y)^2,\qquad
 g=A^2+4(X-Y)^2.                                          \tag{4.1}
$$



Choose $j\in\mathbb F_p$ with $j^2=-1$.  For every
$u,v\in\{\pm1\}$, the nonzero point



$$
\boxed{
 (A,X,Y)=\left(2,{u-vj\over2},{u+vj\over2}\right)}        \tag{4.2}
$$



satisfies $f=g=0$.  These are the four intersections obtained by
choosing one linear factor of each quadric.  The certificate reduces
both substitutions exactly modulo $j^2+1$.

Equation (4.2) is a state-space statement, not an actual-prime witness.
It proves that the odd-row resultant geometry itself gives no
nonvanishing theorem.  Arithmetic of the actual pinned initial values
could still show that they avoid these four lines; that is open.

## 5. Fixed-$M$ parity constancy

The actual indexing is



$$
\mathcal S_M=\{s\geq1:4s\leq M-5,\ s\equiv M+1\pmod3\},
\quad
p_s={4M+2s+1\over3},
\quad
h_s={M-4s-2\over3}.                                      \tag{5.1}
$$



Consecutive elements of $\mathcal S_M$ differ by three.  Directly
from (5.1),



$$
p_{s+3}=p_s+2,\qquad h_{s+3}=h_s-4.                      \tag{5.2}
$$



Therefore one fixed-$M$ slice has a single value



$$
\epsilon_M=h_s\bmod2             \tag{5.3}
$$



for all its rows.  Item 308's actual necessary implication is exactly



$$
\text{pinned eliminant zero}
 \Longrightarrow p_s\mid D_{s,\epsilon_M}.               \tag{5.4}
$$



Neither (5.4) nor the original construction contains the unused
$D_{s,1-\epsilon_M}$.  Thus (1.2) can be applied to the pinned set
only after adding a new, currently unproved second-parity bridge.

The declared exact control verifies that this bridge cannot be inserted
at the Item-308 eliminant level.  At



$$
(M,s,h,p)=(34,2,8,47),\qquad \epsilon_M=0,               \tag{5.5}
$$



the canonical coefficient formulas give



$$
a_2+b_{2,0}w_8=0\pmod {47},\qquad
 (D_{2,0},D_{2,1})=(0,19)\pmod {47}.                      \tag{5.6}
$$



This is one preselected symbolic replay control, not a scan and not an
asymptotic inference.  In particular, it does not assert that (5.5) is
a full Item-264 collision.

## 6. Scoped no-go and de-overlap

The exact resultant and the even-row theorem may be summarized as



$$
\text{two-parity zero}
 \Longrightarrow
 \begin{cases}
 \text{Item-321 Casoratian support},&s\text{ even},\\
 \text{one of four nonzero lines},&s\text{ odd}.
 \end{cases}                                               \tag{6.1}
$$



But the actual fixed-$M$ gate enters (6.1) with only one parity.
Even perfect coprimality of the two parity containers would leave the
selected one-parity zero set unchanged.  The exact information class
closed here is therefore



$$
\boxed{
 \begin{gathered}
 \text{the two Item-308 parity containers at the same }s\\
 +\ \text{their algebraic resultant or gcd}\\
 \text{without an actual theorem forcing the unused parity.}
 \end{gathered}}                                           \tag{6.2}
$$



This does not close a resultant between different actual one-parity
terms, an invariant retaining the original two-coordinate gate, or an
arithmetic theorem for a selected factor sequence.

The even overlap in (1.3) lies entirely in Item 321's already thin
Casoratian exceptional support.  It neither discovers a new valuation
beyond the booked Cartier layers nor excludes any selected collision
row.  Crediting it toward $r_1$ would therefore double-count thin
support while leaving the actual capacity unchanged.

## 7. Capacity, strict labels, and remaining target

The sufficient selected-container target remains



$$
\boxed{
 \mathcal W_D(M)=
 \sum_{\substack{s\in\mathcal S_M\setminus\{2,4,6\}\\
                  p_s\ {\rm prime},\ p_s\mid D_{s,h_s\bmod2}}}
 \log p_s=o(M).}                                          \tag{7.1}
$$



The original pinned target $\mathcal W_{\rm off}(M)=o(M)$ also
remains open.  Item 324 has bounded only an unused two-parity
intersection, not either one-parity support.

- **PROVED:** the all-phase resultant (1.2); the complete rational
  quadric table (2.2); the even-row bridge to the actual Casoratian;
  the fixed-$M$ bound (1.3); the four odd-row intersection lines; and
  fixed-$M$ parity constancy.

- **SCOPED CROSS-PARITY NO-GO:** a gcd/resultant requiring both
  $D_{s,0}$ and $D_{s,1}$ cannot control the selected fixed-$M$
  gate without a new theorem forcing the unused parity.

- **EXACT FINITE ONLY:** the one declared $p=47$ replay control.  It
  is not a scan and is not promoted to a full-gate collision.

- **OPEN:** odd-row actual cross-parity arithmetic; a selected-factor
  gcd/resultant; (7.1); $\mathcal W_{\rm off}(M)=o(M)$; fixed-$j=1$
  closure; Route 1; and every conclusion about $e+\pi$.

- **NOT CLAIMED:** that the unused parity is forced by the original
  collision; that the odd projective lines are attained by actual
  values; that the $p=47$ row is a full Item-264 collision; a prime
  scan; or positive capacity.

The ledger remains



$$
\boxed{\text{capacity booked}=0,\qquad
        \text{fixed-}j=1\text{ ceiling}={1\over36}
        \text{ per }6M.}                                  \tag{7.2}
$$



No canonical, master, or status file is edited by this research package.

## 8. Deterministic replay

From the archive root, run

~~~text
python work/item324_j1_cross_parity_resultant_no_go_certificate.py --output work/item324_j1_cross_parity_resultant_no_go_certificate.replay.json
~~~

The checker pins the canonical Items 308 and 321 packages.  It derives
all eight quadrics from the exact periodic readout, computes the four
resultants symbolically, verifies the fixed-$M$ identities and
Casoratian container, reduces all four odd-row witnesses modulo
$j^2+1$, and independently reconstructs the declared $p=47$ row
from Item 308's coefficient formulas.  It performs no prime scan.
