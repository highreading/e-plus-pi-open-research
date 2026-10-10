> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 427 — the complete ordinary rank-zero Witt tower: a shifted determinantal ideal and an all-level gate theorem

Date: 2026-09-01  
Status: **WORK ONLY, UNAUDITED, NO CENTRAL EDIT, NO BOOKING**

## 1. Capacity-first verdict

Item 424 found the missing first integral error coordinate on an ordinary
rank-zero row.  This item settles the entire corresponding lift tower at
once.

Retain



$$
\omega_s={u^{6m}\over Q^{4m+1+s}}\,dx,
 \qquad u=x(1-x),\quad Q=(1+x)(1+x^2),\quad s=0,1,        \tag{1.1}
$$



with mixed endpoint coordinates



$$
H_s=R_s+{L_s\over4}\log2+{E_s\over8}\pi,               \tag{1.2}
$$



and determinants



$$
A_m=L_1R_0-L_0R_1,
 \qquad
 B_m={L_1E_0-L_0E_1\over8}.                              \tag{1.3}
$$



Let $p$ be an odd prime in Item 200's ordinary rank-zero set
$\mathcal P_m$, and impose the exact positive-rate hypothesis



$$
p^2>4m+1.                         \tag{1.4}
$$



Put



$$
b_{m,p}=v_p(K_m),
 \qquad
 K_m={\operatorname {lcm}(1,\ldots,4m+1)\over
            \prod_{2m<q<3m}q}.                            \tag{1.5}
$$



Then $b_{m,p}\in\{0,1\}$.  Item 424's exact Bockstein makes the
following two quantities integral:



$$
\mathcal K_{m,p}={A_m\over p}\in\mathbb Z_p,
 \qquad
 \mathcal X_{m,p}={8B_m\over p^2}\in\mathbb Z_p.          \tag{1.6}
$$



Define the shifted determinantal ideal



$$
\boxed{
 \mathfrak I_{m,p}=
 (\mathcal K_{m,p},p\mathcal X_{m,p})\subset\mathbb Z_p.} \tag{1.7}
$$



The main theorem is the all-depth identity



$$
\boxed{
 v_p(c_m)-b_{m,p}
 =v_p(\mathfrak I_{m,p})
 =\min\{v_p(\mathcal K_{m,p}),
          1+v_p(\mathcal X_{m,p})\}.}                     \tag{1.8}
$$



Thus one ideal—not a succession of newly invented local jets—captures
every post-baseline content digit on the complete ordinary rank-zero
branch.

Write the canonical base-$p$ expansions



$$
\mathcal K_{m,p}=\sum_{n\ge0}\kappa_np^n,
 \qquad
 \mathcal X_{m,p}=\sum_{n\ge0}\xi_np^n,
 \qquad0\leq\kappa_n,\xi_n<p.                             \tag{1.9}
$$



Then, for every $N\ge1$,



$$
\boxed{
 v_p(c_m)-b_{m,p}\ge N
 \iff
 \begin{cases}
 \kappa_0=\cdots=\kappa_{N-1}=0,\\
 \xi_0=\cdots=\xi_{N-2}=0.
 \end{cases}}                                             \tag{1.10}
$$



The second line is empty for $N=1$.  Equation (1.10) gives the structural
answer requested for the full tower.

* There is one forced **triangular/Jordan delay**: the
  $\mathcal X$-stream enters one level later because the second
  determinant already has one additional forced factor of $p$.
* Beyond that single shift, each level contains genuinely new paired
  digits $(\kappa_N,\xi_{N-1})$.  No further vanishing follows from the
  rank-zero/Bockstein hypotheses alone.

The second statement has two distinct scopes.  It is an actual-family
theorem that (1.8)--(1.10) are the exact gates and that successive gates
really occur on actual rows.  The stronger statement that the two infinite
digit streams may be arbitrary is proved only in an explicitly labelled
ambient endpoint-lattice model; it is not asserted for the mixed-cubic
family.

Capacity is decisive before any scan.  One complete squarefree layer of
the whole ordinary rank-zero support has ceiling



$$
{\mathfrak C_F\over6}
 =0.3895079179997942811851475804\ldots,                    \tag{1.11}
$$



where



$$
\mathfrak C_F=-4\log2+{\pi\over\sqrt3}+3\log3.            \tag{1.12}
$$



The booked overlap has per-layer ceiling



$$
{\mathfrak C_F-2\over6}
 =0.0561745846664609478518142471\ldots .                  \tag{1.13}
$$



Against Item 418's outside-large admission residual



$$
R_{\rm out}=0.5908590983307739249345460183\ldots,          \tag{1.14}
$$



one perfectly saturated whole-support layer is insufficient and two are
already more than enough in raw capacity:



$$
R_{\rm out}-{\mathfrak C_F\over6}
 =0.2013511803309796437493984379\ldots,                    \tag{1.15}
$$





$$
{2\mathfrak C_F\over6}-R_{\rm out}
 =0.1881567376688146374357491425\ldots .                  \tag{1.16}
$$



The booked overlap alone would require eleven perfectly saturated layers
to reach (1.14).  These are admission calculations, not proved masses.
Without a depth bound or weighted-zero theorem, the infinite layer cake has
no finite ceiling obtained from support alone.  Therefore



$$
\boxed{
 \Delta C_{\leq}=\Delta r_{\rm booked}
 =\Delta C_{\rm global}=\Delta(T-r_1)=0.}                  \tag{1.17}
$$



## 2. The exact Bockstein rows

For $p\in\mathcal P_m$, write



$$
\omega_s=F_s^pP_s\,dx.                                   \tag{2.1}
$$



Rank zero means



$$
\deg P_s\leq p-2.                 \tag{2.2}
$$



Hence there is a $p$-integral primitive



$$
T_s(0)=0,
 \qquad T_s'=P_s.                                         \tag{2.3}
$$



Put



$$
\eta_s=F_s^{p-1}F_s'T_s\,dx.            \tag{2.4}
$$



Item 424 proved the exact identity



$$
\omega_s=d(F_s^pT_s)-p\eta_s.                            \tag{2.5}
$$



The numerator exponent of $F_s$ is positive, so its endpoint boundary is
zero.  Taking the three mixed coordinates gives, exactly,



$$
R_s=-pR(\eta_s),
 \qquad L_s=-pL(\eta_s),
 \qquad E_s=-pE(\eta_s).                                  \tag{2.6}
$$



In particular,



$$
\mathcal W_s=left(R_s,{L_s\over p},{E_s\over p}\right)
 =\bigl(-pR(\eta_s),-L(\eta_s),-E(\eta_s)\bigr)
 \in\mathbb Z_p^3.                                       \tag{2.7}
$$



For the all-level content problem the natural row is not $\mathcal W_s$
itself, but its one-step anisotropic rescaling



$$
\mathcal Y_s=operatorname {diag}(1,1,p)\mathcal W_s
 =\left(R_s,{L_s\over p},E_s\right)
 =\bigl(-pR(\eta_s),-L(\eta_s),-pE(\eta_s)\bigr).          \tag{2.8}
$$



The two target minors of the $2\times3$ matrix with rows
$\mathcal Y_0,\mathcal Y_1$ are



$$
\Delta_{RL}
 ={L_1\over p}R_0-{L_0\over p}R_1
 ={A_m\over p}=\mathcal K_{m,p},                           \tag{2.9}
$$



and



$$
\Delta_{LE}
 ={L_1\over p}E_0-{L_0\over p}E_1
 ={8B_m\over p}
 =p\mathcal X_{m,p}.                                      \tag{2.10}
$$



Thus (1.7) is literally the relevant determinantal ideal of the integral
Bockstein rows.  The third minor $\Delta_{RE}$ is not one of the two
determinants defining the actual $(1,e+\pi)$ approximant and is not added
as an artificial condition.

## 3. Proof of the all-depth identity

The exact normalization is



$$
U_m={D_m^\sharp A_m\over G_m},
 \qquad
 V_m={D_m^\sharp B_m\over G_m},
 \qquad
 D_m^\sharp=2^{9m+5}K_m.                                 \tag{3.1}
$$



Because $p\in\mathcal P_m$, the squarefree product $G_m$ contains one
copy of $p$.  Hypothesis (1.4) implies



$$
v_p(D_m^\sharp)=v_p(K_m)=b_{m,p}\in\{0,1\}.              \tag{3.2}
$$



From (1.6),



$$
A_m=p\mathcal K_{m,p},
 \qquad
 B_m={p^2\over8}\mathcal X_{m,p}.                         \tag{3.3}
$$



Substitution into (3.1) gives the two exact valuation identities



$$
v_p(U_m)=b_{m,p}+v_p(\mathcal K_{m,p}),                   \tag{3.4}
$$





$$
v_p(V_m)=b_{m,p}+1+v_p(\mathcal X_{m,p}).                 \tag{3.5}
$$



Taking the minimum proves (1.8).  No asymptotic estimate or finite scan is
used.

Equation (3.4) also shows why the normalized log pair from Item 415 cannot
be the full small-prime carrier.  The controlling object is a determinant
of two divided Bockstein rows, not either divided log coordinate
separately.

## 4. One generating series for every lift level

For an element $x\in\mathbb Z_p$, let



$$
\operatorname {dig}_p(x)(z)=\sum_{n\ge0}d_n(x)z^n
 \in\mathbb F_p[[z]],                                     \tag{4.1}
$$



where $d_n(x)\in\{0,\ldots,p-1\}$ are its canonical base-$p$ digits.
Define the two-component error series



$$
\boxed{
 \mathscr G_{m,p}(z)
 =\operatorname {dig}_p(\mathcal K_{m,p})(z)\,\mathbf e_1
 +z\operatorname {dig}_p(\mathcal X_{m,p})(z)\,\mathbf e_2.} \tag{4.2}
$$



For a vector series, take $\operatorname {ord}_z$ to be the minimum of
the two component orders.  Multiplication by $p$ shifts base-$p$ digits
without a carry, so (1.8) is equivalent to



$$
\boxed{
 \operatorname {ord}_z\mathscr G_{m,p}
 =v_p(c_m)-b_{m,p}.}                                      \tag{4.3}
$$



The coefficient at level $n$ is



$$
[z^n]\mathscr G_{m,p}
 =\begin{cases}
   (\kappa_0,0),&n=0,\\
   (\kappa_n,\xi_{n-1}),&n\ge1.
  \end{cases}                                             \tag{4.4}
$$



Equations (4.3)--(4.4) prove (1.10) simultaneously for every $N$.

If an explicit recursion is preferred, set



$$
K^{[0]}=\mathcal K_{m,p},
 \qquad X^{[0]}=\mathcal X_{m,p},                          \tag{4.5}
$$



and define



$$
\kappa_n=K^{[n]}\pmod p,
 \qquad
 K^{[n+1]}={K^{[n]}-\kappa_n\over p},                      \tag{4.6}
$$





$$
\xi_n=X^{[n]}\pmod p,
 \qquad
 X^{[n+1]}={X^{[n]}-\xi_n\over p},                        \tag{4.7}
$$



using the representatives $0,\ldots,p-1$.  The tower terminates at the
first nonzero pair in (4.4).  This recursion is canonical and requires no
new choice of a local jet at each order.

## 5. Triangular shift versus genuinely new gates

The factor $z$ in (4.2) is the complete forced resonance.  It comes from
the exact extra factor of $p$ in the log--$\pi$ determinant:



$$
v_p(B_m)\ge2,
 \qquad v_p(A_m)\ge1.                                     \tag{5.1}
$$



There is no second forced shift in (3.4)--(3.5).  At every level after the
first, the next content digit requires both a new $\mathcal K$-digit and
the lagged new $\mathcal X$-digit.

### 5.1 Actual-family facts

The following exact rows prove that these are not merely formal labels.

1. At $(m,p)=(13,11)$,
   

$$
(\kappa_0,\kappa_1)=(0,4),
   \qquad \xi_0=8,
   \qquad v_{11}(c_{13})-b_{13,11}=1.                     \tag{5.2}
$$


   Thus the first gate $\kappa_0=0$ does not force the lagged
   $\mathcal X$-gate $\xi_0=0$.

2. At $(m,p)=(24,11)$,
   

$$
(\kappa_0,\kappa_1)=(0,10),
   \qquad(\xi_0,\xi_1,\xi_2)=(0,0,8),
   \qquad v_{11}(c_{24})-b_{24,11}=1.                     \tag{5.3}
$$


   Here the first two displayed $\mathcal X$-digits vanish, but the new
   $\kappa_1$-gate stops the tower.  Hence the shifted branch does not
   absorb the next rational-log digit.

3. At $(m,p)=(89,19)$,
   

$$
(\kappa_0,\kappa_1,\kappa_2)=(0,0,6),
   \qquad(\xi_0,\xi_1,\xi_2)=(0,0,12),
   \qquad v_{19}(c_{89})-b_{89,19}=2.                     \tag{5.4}
$$


   The actual tower reaches depth two and is then stopped by the genuinely
   new $\kappa_2$-digit.

These are exact actual-family counterexamples to automatic propagation of
the displayed vanishings.  They are not density statements.

### 5.2 Ambient endpoint-lattice theorem

The stronger information-class statement is deliberately separated from
the actual family.  Let $\mathcal K,\mathcal X\in\mathbb Z_p$ be
arbitrary.  In coordinate order $(R,L/p,E)$, take



$$
\mathcal Y_0=(0,1,0),
 \qquad
 \mathcal Y_1=(-\mathcal K,1,-p\mathcal X).                \tag{5.5}
$$



These rows correspond to $L_0=L_1=p$ and
$E_0=0,E_1=-p\mathcal X$, so they satisfy exactly the rank-zero endpoint
divisibilities.  Their two target minors are



$$
\Delta_{RL}=\mathcal K,
 \qquad
 \Delta_{LE}=p\mathcal X.                                 \tag{5.6}
$$



Thus arbitrary and independent $p$-adic digit streams occur in the
ambient endpoint lattice.  No relation among higher digits can follow from
rank-zero endpoint divisibility alone.

Equations (5.5)--(5.6) do **not** claim that every such pair is realized by
the mixed-cubic differentials.  An actual-family recurrence, Frobenius
equation, or arithmetic zero-density theorem could still relate the two
streams.  None is presently proved.

## 6. Exact de-overlap and layer capacity

Define the actual ordinary rank-zero tower depth



$$
d_{m,p}=v_p(c_m)-b_{m,p}.                                 \tag{6.1}
$$



For the $q=p$ cells of Item 200's parametrization,



$$
4m+1=(2j+1)p-2s,
 \qquad1\le s\le{p-3\over6}.                              \tag{6.2}
$$



There are two cases.

* If $j=0$, then $p>4m+1$, $b_{m,p}=0$, and the first Witt layer is
  the first actual post-$G_m$ content copy at that prime.
* If $j\ge1$, then $p<2m$, $p\in\mathcal H_m$, and
  $b_{m,p}=1$.  This is exactly the Item-149 copy already booked in the
  frozen ledger.  Therefore $d_{m,p}$ begins strictly after that booked
  copy.

Thus (6.1) removes the available baseline exactly once.  It neither
rebooks $G_m=F_m$, which was divided out before $c_m$ was defined, nor
rebooks Item 149.

For $n\ge1$, put



$$
\mathcal R_n(m)=
 \prod_{\substack{p\in\mathcal P_m,\ p^2>4m+1\\d_{m,p}\ge n}}p. \tag{6.3}
$$



The exact layer-cake identity is



$$
\sum_{\substack{p\in\mathcal P_m\\p^2>4m+1}}
 d_{m,p}\log p
 =\sum_{n\ge1}\log\mathcal R_n(m).                        \tag{6.4}
$$



Every $\mathcal R_n$ is supported inside $F_m$, so Item 200 gives,
for each fixed $n$,



$$
\limsup_{m\to\infty}{\log\mathcal R_n(m)\over6m}
 \le{\mathfrak C_F\over6}.                               \tag{6.5}
$$



On the booked $j\ge1$ cells, the corresponding ceiling is
$(\mathfrak C_F-2)/6$.

The excluded initial-scaling tail $p^2\le4m+1$ has radical logarithm



$$
O(\sqrt m\log m)=o(m).                                   \tag{6.6}
$$



Therefore it cannot change any fixed-layer capacity.  Equation (6.6) does
not bound arbitrarily high multiplicities on that tail; an aggregate depth
theorem would still be required.

Support alone does not allow summation of (6.5) over infinitely many
layers.  A uniform depth bound $d_{m,p}\le D$ would give at most
$D\mathfrak C_F/6$ for this component, but:

* $D=1$ fits below (1.14);
* $D=2$ already has raw ceiling
  $2\mathfrak C_F/6>R_{\rm out}$; and
* no finite $D$, weighted tail bound, or zero-density theorem is proved
  here.

The correct next target is consequently not “compute digit three.”  It is
an aggregate theorem such as



$$
\sum_{n\ge2}\log\mathcal R_n(m)=o(m),                    \tag{6.7}
$$



or an explicit upper bound for the left side small enough to matter after
combining all disjoint components.

## 7. Deterministic finite replay

Only after the all-level theorem and capacity screen are fixed does the
certificate examine finite data.  On all ordinary rank-zero rows satisfying
(1.4) for $1\le m\le100$, it reconstructs



$$
\mathcal K={U_mG_m\over D_m^\sharp p},
 \qquad
 \mathcal X={8V_mG_m\over D_m^\sharp p^2},                \tag{7.1}
$$



as exact rational numbers with $p$-unit denominators.  It verifies every
digit gate in (1.10), every valuation in (1.8), and the exact shift of the
$p\mathcal X$ digit stream.

The finite census contains 1,953 incidences.  Their tower-depth distribution
is



$$
\begin{array}{c|rrr}
 d&0&1&2\\ \hline
 \text{all ordinary rank-zero rows}&1929&23&1\\
 \text{booked overlap}&270&14&1.
 \end{array}                                               \tag{7.2}
$$



Thus the first and second layer supports have 24 and 1 rows respectively;
on the booked overlap they have 15 and 1.  These counts are exact finite
checks only and are not extrapolated.

The certificate also checks 75 ambient parameter tuples, but the proof of
(5.5)--(5.6) is symbolic and does not depend on that finite check.

## 8. Strict claim ledger

### PROVED — ACTUAL FAMILY

* The integral Bockstein rows (2.8).
* The single all-level determinantal ideal (1.7).
* The exact full-depth identity (1.8).
* The unified digit series and recursion (4.2)--(4.7).
* The exact level-$N$ criterion (1.10) for every $N$.
* A single forced Jordan delay followed by new paired gates.
* The actual successive-gate witnesses (5.2)--(5.4).
* The de-overlapped layer cake and each fixed-layer capacity ceiling.
* Zero change to every central ledger quantity.

### PROVED — AMBIENT MODEL ONLY

* Arbitrary independent $\mathcal K$- and $\mathcal X$-digit streams
  are compatible with rank-zero endpoint divisibility.
* Therefore rank-zero endpoint divisibility alone cannot force a higher
  resonance theorem.

### EXACT FINITE ONLY

* The counts and stream digest in (7.2).
* The observed absence of depth $3$ in the checked range.

### OPEN

* An actual-family relation, distribution theorem, or average bound for the
  paired digit streams.
* The aggregate higher-layer estimate (6.7).
* An exact initial scaling for the zero-rate $q>p$ tail.
* Non-rank-zero small-prime content.
* Route 1 and the irrationality of $e+\pi$.

### NOT CLAIMED

* That the ambient arbitrary-stream construction belongs to the actual
  family.
* Positive density or zero density for any Witt layer.
* A finite uniform depth bound inferred from the finite census.
* A reduced small-prime ceiling, new booked content, Route-1 closure, or an
  irrationality proof.

## 9. Replay

Run

```text
python work/item427_rankzero_witt_tower_certificate.py \
  --output work/item427_rankzero_witt_tower_certificate.replay.json \
  --replay work/item427_rankzero_witt_tower_certificate.json
```

The checker uses only the Python standard library and confines every
Item-427 artifact to `work/`.
