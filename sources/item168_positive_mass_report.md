> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 168 — complete $e=1$ cells and the small-support barrier for automatic third layers

Date: 2026-08-29

## 1. Scope and verdict

Put



$$
u=x(1-x),\qquad Q=(1+x)(1+x^2),\qquad
 \omega_s={u^{6m}\over Q^{4m+1+s}}\,dx\quad(s=0,1).
$$



For an odd prime in the top layer



$$
p\le 4m+1<p^2                                      \tag{1.1}
$$



write



$$
6m=ap+r,\qquad4m+1=bp+t,\qquad0\le r,t<p,
 \qquad \kappa=2a-3b.                                    \tag{1.2}
$$



This note classifies every $e=1$ floor cell which can enter the proved
rank-one or rank-two Cartier divisor, and asks whether the third content
layer can have positive prime-number-theorem weight.

The conclusions are deliberately scoped.

**PROVED — complete three-cell parameterization.**  Apart from the
non-forced $t=0$ boundary, every rank-at-most-two row is in exactly one
of the cells $\kappa=0,1,2$.  Explicit $(j,s)$ coordinates and all
three PNT intervals are given in Section 3.

**PROVED — a universal rank-one exact tail.**  On a $\kappa=1$ row let
$\gamma_0,\gamma_1$ be the two first Cartier scalars.  If



$$
\gamma_0=\gamma_1=0,\qquad3j+1\ge p,           \tag{1.3}
$$



then



$$
\boxed{p^3\mid c_m}.                \tag{1.4}
$$



This strictly generalizes the *mechanism* of item 164: no assumption
$p\mid10m+1$ is used in the proof.  However, every row in (1.3) satisfies



$$
p(p+1)\le6m.                         \tag{1.5}
$$



Consequently all primes accessible through this automatic degree tail have
logarithmic weight $O(\sqrt m)=o(m)$.

**PROVED — the rank-zero analogue stops one layer earlier.**  In the
$\kappa=2$ cell, if



$$
3j\ge p,\qquad2j+2\le p,                    \tag{1.6}
$$



the same second-Cartier exactness gives $p^2\mid c_m$.  It does not
formally give $p^3\mid c_m$: the rational endpoint of an exact
differential may be nonzero.  The exact normalized-minor ledger leaves the
next $A$-digit free.  Again (1.6) implies $p=O(\sqrt m)$.

**PROVED — mechanism-level small-support barrier.**  More generally, any
second-Cartier argument of the item-164 type which obtains exactness solely
by factoring a new $(u/Q)^p$ and bounding the residual polynomial degree
by $p-2$ requires $a-1\ge p$.  Hence $6m\ge p(p+1)$.  Such a fixed
depth degree-exactness argument cannot produce positive weighted prime mass.
This says nothing against non-scalar endpoint cancellation on PNT-scale
cells.

**PROVED — three-layer capacity no-go.**  The exact radical mass of the
rank-zero and rank-one cells, plus the absolute ceiling of the rank-two
cell, is



$$
C_{\le2}=1.7094487795303306\ldots\quad\hbox{per }m.       \tag{1.7}
$$



Even if every available prime in all three cells satisfied $p^3\mid c_m$,
the resulting three-layer capacity would be at most



$$
{3C_{\le2}\over6}=0.8547243897651653\ldots,              \tag{1.8}
$$



which misses the Route-1 threshold
$1.1561471519642446\ldots$ by



$$
0.3014227621990792\ldots .          \tag{1.9}
$$



**EXPERIMENTAL.**  The scalar-free item-163 replay has only five cubic
survivors among 784 forced $e=1$ rows through $m\le100$: four in
$\kappa=1$, one in $\kappa=2$, and none in the vanishing
$\kappa=0$ rows.  A separate exact scan through $p\le2000$ finds no
simultaneous rank-one scalar zero outside the balanced four-section ray.
Neither finite statement is a density theorem.

**OPEN.**  A positive-mass family could still arise from the scalar-free
digit equations on $\kappa=1,2$, or from the rank-two determinant and its
lifts on $\kappa=0$.  No theorem here excludes those cancellations.  No
new positive content exponent and no result about $e+\pi$ is claimed.

## 2. Exact scalar-free third-layer gate

Let



$$
X_s=pR_s,
 \qquad \mathscr A=L_1X_0-L_0X_1,
 \qquad \mathscr B=L_1E_0-L_0E_1.                         \tag{2.1}
$$



For a forced rank-one row or a vanishing rank-two row put



$$
\epsilon={\bf1}_{p\in\mathcal P_m},\qquad D=1+\epsilon.
$$



The frozen primitive normalization gives



$$
p^D\mid\mathscr A,\mathscr B,
 \qquad
 {\mathscr A\over p^D}=\sum_{n\ge0}A_np^n,
 \qquad
 {\mathscr B\over p^D}=\sum_{n\ge0}B_np^n.              \tag{2.2}
$$



Item 163 proves, without dividing by a Cartier scalar,



$$
\boxed{
 p^3\mid c_m
 \iff A_0=A_1=B_0=0.}                                    \tag{2.3}
$$



Thus the remaining PNT-scale problem is an exact system of three lifted
equations.  In the rank-two cell it is preceded by the additional equation
$\Delta_{p,s}=0$.  Calling these equations “codimension three” or
“codimension four” is only an algebraic ledger; no independence or
equidistribution is assumed.

## 3. Complete $e=1$ cell coordinates

The identity $2(6m)=3(4m+1)-3$ gives



$$
\kappa p+2r-3t=-3.                           \tag{3.1}
$$



If $t>0$, the two Cartier-polynomial degrees are



$$
d_0=(3-\kappa)p-3,\qquad d_1=(3-\kappa)p-6.             \tag{3.2}
$$



Consequently rank at most two is equivalent to
$\kappa\in\{0,1,2\}$.  Solving (3.1) gives the following complete table.

### 3.1 Rank two: $\kappa=0$

There are integers $j\ge1$ and $s$ such that



$$
(a,b)=(3j,2j),\qquad r=3s,\qquad t=2s+1,                \tag{3.3}
$$





$$
2m=jp+s,\qquad0\le s\le{p-1\over3},\qquad s\equiv j\pmod2. \tag{3.4}
$$



The endpoint $j=1,s=0$ is omitted by the required inequality $p<2m$.
The two Cartier images have rank at most two.  A prime is forced only when
their exact determinant $\Delta_{p,s}$ vanishes.

At PNT scale the $j$-th cell is



$$
{6\over3j+1}<{p\over m}<{2\over j}.   \tag{3.5}
$$



### 3.2 Rank one: $\kappa=1$

Here



$$
(a,b)=(3j+2,2j+1),\quad p-t=2s+1,\quad r=p-3s-3,       \tag{3.6}
$$





$$
2m+1=(j+1)p-s,\qquad0\le s\le{p-3\over3},
 \qquad s\equiv j\pmod2.                                \tag{3.7}
$$



Every such row is a forced rank-one row.  Its PNT interval is



$$
{2\over j+1}<{p\over m}<{6\over3j+2}. \tag{3.8}
$$



### 3.3 Rank zero: $\kappa=2$

Here



$$
(a,b)=(3j+1,2j),\quad p-t=2s,\quad
 r={p-6s-3\over2},                                      \tag{3.9}
$$





$$
4m+1=(2j+1)p-2s,\qquad1\le s\le{p-3\over6}.           \tag{3.10}
$$



The integrality condition in (3.10) is equivalent to its right side being
$1\pmod4$.  Both first Cartier images vanish.  The old squarefree
rank-zero factor has already been removed in $c_m$, so this cell still
starts with one surviving forced layer.  Its PNT interval is



$$
{4\over2j+1}<{p\over m}<{6\over3j+1}. \tag{3.11}
$$



The deterministic certificate exhaustively reconstructs 43,630 rows in
these three parameterizations for primes through 149, with no discrepancy.

## 4. Weighted mass of the three cells

The PNT sums for the rank-zero and rank-one cells are exact:



$$
\begin{aligned}
 C_{0}
 &=\sum_{j\ge1}\left({6\over3j+1}-{4\over2j+1}\right)\\
 &=-4\log2+{\pi\over\sqrt3}+3\log3-2\\
 &=0.3370475079987658\ldots,                               \tag{4.1}
\end{aligned}
$$





$$
\begin{aligned}
 C_{1}
 &=\sum_{j\ge1}\left({6\over3j+2}-{2\over j+1}\right)\\
 &=-1-{\pi\over\sqrt3}+3\log3\\
 &=0.4820375017701113\ldots .                              \tag{4.2}
\end{aligned}
$$



For rank two, pretending optimistically that every determinant vanishes
gives the absolute ceiling



$$
\begin{aligned}
 C_{2}
 &=\sum_{j\ge1}\left({2\over j}-{6\over3j+1}\right)\\
 &=6-{\pi\over\sqrt3}-3\log3\\
 &=0.8903637697614535\ldots .                              \tag{4.3}
\end{aligned}
$$



Thus $C_{\le2}=C_0+C_1+C_2$, proving (1.7)--(1.9).  Notice that
$C_2$ is only a ceiling, whereas $C_0+C_1$ is the already proved
rank-one radical mass.  The calculation does not bound unforced primes or
higher valuations in the actual $c_m$.

## 5. Second-Cartier exact tails

Set $\mathfrak D=uQ=x(1-x^4)$.  Whenever the relevant first Cartier
coefficients of a polynomial $P_s$ vanish, let $T_s$ be its
zero-constant $p$-integral primitive.  For



$$
F={u^a\over Q^c},\qquad \omega_s=F^pP_s\,dx,             \tag{5.1}
$$



integration by parts gives



$$
\omega_s=d(F^pT_s)-p\Psi_s,
 \qquad \Psi_s=F^{p-1}F'T_s\,dx.                          \tag{5.2}
$$



Define



$$
N_s=T_s\{a u'Q-cQ'u\}.                                  \tag{5.3}
$$



The same coefficient filter as item 164 gives



$$
\mathcal C\Psi_s=\Phi_s={u^{a-1}H_s\over Q^{c+1}}\,dx. \tag{5.4}
$$



### 5.1 Rank-one cubic tail

In the $\kappa=1$ cell,



$$
a=3j+2,\qquad c=2j+2,\qquad \deg H_s\le5.               \tag{5.5}
$$



If $\gamma_0=\gamma_1=0$, both primitives in (5.2) are $p$-integral.
If $3j+1\ge p$, the complete $e=1$ range also gives $2j+3\le p$,
and



$$
\Phi_s=\left({u\over Q}\right)^p
 u^{3j+1-p}H_sQ^{p-2j-3}\,dx.                            \tag{5.6}
$$



The residual polynomial has degree



$$
2(3j+1-p)+\deg H_s+3(p-2j-3)
 =p-7+\deg H_s\le p-2.                                  \tag{5.7}
$$



Therefore $\Phi_s$ is exact in characteristic $p$.  Absolute exactness
kills its logarithmic and circular coordinates, although its rational
endpoint may survive.  Equations (5.2)--(5.4) then give



$$
p\mid X_s,\qquad p^2\mid L_s,E_s.                       \tag{5.8}
$$



Hence



$$
p^3\mid\mathscr A,\qquad p^4\mid\mathscr B.            \tag{5.9}
$$



Here $\epsilon=0,D=1$, so the exact gate (2.3) proves $p^3\mid c_m$.
Finally



$$
6m=(3j+2)p+r\ge(p+1)p,                                  \tag{5.10}
$$



which proves the small-support assertion.

### 5.2 Rank-zero tail and its sharp stopping point

In the $\kappa=2$ cell the two first Cartier coefficients vanish
automatically, and



$$
a=3j+1,\qquad c=2j+1,\qquad\deg H_s\le4.                \tag{5.11}
$$



Under (1.6),



$$
\Phi_s=\left({u\over Q}\right)^p
 u^{3j-p}H_sQ^{p-2j-2}\,dx,                              \tag{5.12}
$$



whose residual degree is



$$
p-6+\deg H_s\le p-2.                   \tag{5.13}
$$



Thus (5.8)--(5.9) hold again.  But now the already removed rank-zero
factor means $\epsilon=1,D=2$.  Dividing (5.9) by $p^D$ forces only



$$
A_0=0,\qquad B_0=B_1=0.                \tag{5.14}
$$



The digit $A_1$, required by (2.3), is not controlled.  The conclusion
is $p^2\mid c_m$, not $p^3\mid c_m$.  In the frozen $m\le100$
replay all eight rows satisfying (1.6) have the proved second layer and
none has a third; this finite sharpness check is not a uniform
nonvanishing theorem.

### 5.3 Mechanism-level barrier

The degree argument (5.6) or (5.12) works by extracting a fresh
$(u/Q)^p$ from (5.4).  Irrespective of the cell, this requires



$$
a-1\ge p.                   \tag{5.15}
$$



Since $6m=ap+r$, (5.15) implies $6m\ge p(p+1)$.  Chebyshev's bound
then gives



$$
\sum_{\substack{p\text{ accessible by (5.15)}}}\log p
 \le\vartheta(\sqrt{6m})=O(\sqrt m)=o(m).                \tag{5.16}
$$



This is the promised sharp scope: (5.16) rules out positive mass from
residual-degree exactness, not from the scalar-free equations (2.3).

## 6. Known rays and their thinness

On the balanced rank-one subcell



$$
p=5s+4,                     \tag{6.1}
$$



one has $r=p-t=2s+1$ and



$$
P_0=x^r(1-x^4)^r,\qquad
 P_1=x^r(1-x)(1-x^4)^{r-1}.                              \tag{6.2}
$$



The selected offset is $3s+2$.  Since a prime in (6.1) has odd $s$,
four-section support gives



$$
\gamma_0=\gamma_1=0
 \iff s\equiv3\pmod4
 \iff p\equiv19\pmod {20}.                              \tag{6.3}
$$



For $s\equiv1\pmod4$, $\gamma_0=0$ but the unique selected term in
$P_1$ is a nonzero binomial coefficient, so $\gamma_1\ne0$.
Equations (3.7) and (6.1) give



$$
(5j+4)p=10m+1.                   \tag{6.4}
$$



Thus the simultaneous-support-zero ray is exactly the item-162/164 slab
and has $O(\log m)$ weight at fixed $m$.

The three proved rank-two determinant rays similarly satisfy



$$
\begin{array}{c|c}
p=3s+4&p\mid3m+2,\\
p=5s+2&p\mid5m+1,\\
p=5s+1&p\mid10m+1.
\end{array}                                               \tag{6.5}
$$



Their combined radical has logarithm $O(\log m)$.  These rays are not
claimed to exhaust $\Delta_{p,s}=0$.

More generally, any finite collection of exact rays whose primes divide
fixed nonzero polynomials $F_i(m)\in\mathbb Z[m]$ has radical dividing
$\prod_i|F_i(m)|$, hence logarithm $O(\log m)$.  Boundedly many
additional valuation copies on such rays remain zero-rate.

## 7. The prime-square ray

Let



$$
10m+1=p^2.                       \tag{7.1}
$$



For every prime $p\ne2,5$ for which (7.1) is integral, the four residue
classes modulo 20 split exactly as follows.

If $p=5s+4$, then $j=s$ and the row is in $\kappa=1$.  Therefore



$$
\begin{array}{c|c}
p\equiv9\pmod {20}&\gamma_0=0,\ \gamma_1\ne0,\\
p\equiv19\pmod {20}&\gamma_0=\gamma_1=0.
\end{array}                                               \tag{7.2}
$$



Item 167 proves the exact uniform valuation



$$
p\equiv19\pmod {20}\Longrightarrow v_p(c_m)=3. \tag{7.3}
$$



If $p=5s+1$, then $j=s$ and the row is in $\kappa=0$.  Its two
Cartier polynomials reduce to



$$
P_0=x^{3s}(1-x^4)^{3s},\qquad
 P_1=x^{3s}(1-x)(1-x^4)^{3s-1}.                           \tag{7.4}
$$



For $s\equiv2\pmod4$, equivalently $p\equiv11\pmod {20}$, both
high selected coefficients vanish and $\Delta_{p,s}=0$.  For
$s\equiv0\pmod4$, equivalently $p\equiv1\pmod {20}$,



$$
\Delta_{p,s}=
 (-1)^{s/2}{3s\choose s/2}
 \left[-(-1)^{7s/4}{3s-1\choose7s/4}\right]\ne0\pmod p. \tag{7.5}
$$



Every binomial argument in (7.5) is below $p=5s+1$, proving
nonvanishing.  Hence (7.3) is the unique *proved automatic cubic class*
on the square ray.  Uniform deeper valuations in the $p\equiv9,11$
classes remain open here.  The exact controls



$$
(p,v_p(c_m))=(11,2),(19,3),(29,2),(31,2)                \tag{7.6}
$$



are finite diagnostics consistent with this classification, not a theorem
for the (9) or (11) classes.

## 8. What remains capable of positive mass

After the preceding reductions, a positive-mass cubic theorem could only
come from one of the following genuinely unresolved systems.

1. **Rank one $\kappa=1$:** non-scalar cancellation in
   $A_0=A_1=B_0=0$ over a PNT-positive subset of (3.8).  Simultaneous
   scalar zero is sufficient for $A_0=0$, but is not necessary.
2. **Rank zero $\kappa=2$:** the two-primitive digits
   $A_0=A_1=B_0=0$ over a PNT-positive subset of (3.11).  The degree tail
   proves only $A_0=0$ and has small support.
3. **Rank two $\kappa=0$:** first
   $\Delta_{p,s}=0$, then all three lifted equations in (2.3), over a
   PNT-positive subset of (3.5).  No independence among these four
   equations is known.

The current algebra supplies neither a positive-mass family nor a theorem
that these systems have zero mass.  Moreover, even maximal cubic survival
on their entire radical support is insufficient by (1.8)--(1.9).  A
Route-1 closure would still need a fourth/fifth layer on substantial
support, new internal primes, or sequential matching gain after primitive
normalization.

## 9. Deterministic certificate

The standard-library checker

`scripts/item168_positive_mass_certificate.py`

verifies the cell identities, tail inequalities, interval sums, balanced
four-section ray, square-ray split, and the frozen scalar-free gates.  Its
default finite diagnostics are:



$$
\begin{array}{l|r}
\text{cell rows reconstructed through }p\le149&43{,}630\\
\text{rank-one scalar pairs scanned through }p\le2000&\text{all admissible }s\\
\text{simultaneous scalar zeros}&38\\
\text{off-balanced simultaneous zeros}&0\\
\text{frozen forced }e=1\text{ rows}&784\\
\text{frozen cubic survivors}&5\\
\text{rank-zero exact-tail rows}&8\\
\text{rank-zero exact-tail cubic survivors}&0.
\end{array}                                                \tag{9.1}
$$



The finite counts in (9.1) audit formulas only.  The uniform statements
are the symbolic arguments above.

## 10. Status ledger

### PROVED

- The complete $e=1$, rank-at-most-two cell parameterization.
- The exact PNT interval masses and three-layer capacity deficit.
- The conditional universal cubic tail (1.3)--(1.5).
- The rank-zero second-layer tail and its ledger-level stopping point.
- The $p=O(\sqrt m)$ barrier for residual-degree exactness.
- Thinness of every currently proved ray and the prime-square residue split.

### EXPERIMENTAL FINITE

- No off-balanced simultaneous scalar zero through $p\le2000$.
- Five cubic survivors among 784 frozen $e=1$ rows through $m\le100$.
- The four square-ray valuation controls (7.6).

### OPEN

- Positive weighted mass for any of the scalar-free systems in Section 8.
- A uniform $p^2$ theorem in the square-ray $p\equiv9,11\pmod {20}$
  classes.
- Enough fourth/fifth-layer or sequential mass to reach the saddle.
- Any conclusion about the rationality, irrationality, or transcendence of
  $e+\pi$.
**EXPERIMENTAL.**  The scalar-free item-163 replay has only five cubic
