> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 209 — the separate second-lift digit on the moving rank-one cell

Date: 2026-08-30

## 1. Scope and verdict

This item continues the rank-one $\kappa=1$ analysis of archived
Items 172, 181, and 196, using Item 205's localized common-moving-content
theorem.  It treats the second-lift digit $A_1$ separately from the two
first gates $A_0,B_0$.  No left-factorial filter is revisited.

The conclusions are:

- **PROVED — exact quotient/carry formula.**  On every $\kappa=1$ row,
  rank one first gives an exact division by $p$.  If $A_0=0$, it gives
  a second exact division, and
  

$$
A_1\equiv {L_1X_0-L_0X_1\over p^2}\pmod p,
     \qquad X_\nu=pR_\nu.                              \tag{1.1}
$$


  The signed carry version is given in Section 3.  It remains valid when
  $A_0=B_0=0$, and it divides by no Cartier scalar.  The condition
  $B_0=0$ is part of the cubic gate but is not needed to make (1.1)
  integral.

- **PROVED — common moving content does not force $A_1$.**  The actual
  common-content row
  

$$
(s,p,j,m)=(3,19,1,17)
$$


  has $(A_0,A_1,B_0)=(0,16,0)$.  At the same $(s,p)$, the row
  $(j,m)=(3,36)$ has $(0,0,0)$.  Thus even an identically zero reduced
  moving vector does not determine the second lift.  The large exact ray
  point $(s,p,j,m)=(299,1499,1,1349)$ has $A_1=925$.

- **FINITE — the new $p=8s+7$ candidate.**  For the actual-seed point
  

$$
(s,p)=(299,2399),\qquad 2399=8s+7,
$$


  the Item 205/208 coefficient recurrence has $g_0=g_1=0\pmod p$.
  Nevertheless the $j=1,m=2249$ row has
  $(A_0,A_1,B_0)=(0,404,0)$.  This is one exact finite point; no infinite
  $p=8s+7$ content ray is claimed.

- **PROVED — automatic anchor degeneration is only a first-gate theorem.**
  Whenever
  

$$
2j+3\le p\le3j+2,                 \tag{1.2}
$$


  all fixed Cartier wedge weights in the Item 196 contractions vanish
  modulo $p$.  Hence $A_0=B_0=0$ for every admissible $s$, but
  $A_1$ is not forced: $(j,p,s,m)=(2,7,0,10)$ has $A_1=1$.

- **PROVED — zero rate.**  Every row in (1.2) satisfies $p^2\le6m$, so
  the entire automatic-anchor family has log-prime weight
  $O(\sqrt m)=o(m)$.  The exact $p=5s+4$ content ray is already
  contained in the divisors of $10m+1$.  These repackagings contribute
  **zero new Route-1 exponent**, irrespective of their $A_1$ behavior.

No global exclusion or zero-density theorem for $A_1$ is proved.  The
finite controls below are not extrapolated.

## 2. Unambiguous digit convention

For $\nu=0,1$, let $(R_\nu,L_\nu,E_\nu)$ be the two endpoint Hasse
coordinate triples and put



$$
X_\nu=pR_\nu,
 \qquad
 \mathscr A=L_1X_0-L_0X_1,
 \qquad
 \mathscr B=L_1E_0-L_0E_1.                            \tag{2.1}
$$



All statements may be made in $\mathbb Z_p$; the checker evaluates the
entries modulo $p^3$.  Write the canonical raw determinant digits as



$$
\mathscr A\equiv d^A_0+p d^A_1+p^2d^A_2\pmod {p^3},
 \qquad 0\le d^A_q<p,                                 \tag{2.2}
$$



and similarly for $\mathscr B$.  On the rank-one cell,



$$
d^A_0=d^B_0=0.               \tag{2.3}
$$



The gate names are



$$
A_0=d^A_1,
 \qquad B_0=d^B_1,
 \qquad A_1=d^A_2\quad\hbox{after }A_0=0.             \tag{2.4}
$$



The raw digit $d^A_2$ exists even when $A_0\ne0$, but its
second-quotient interpretation is used only after $A_0=0$.  The raw
digit $d^B_2$ is not called $A_1$.  With this convention, Item 172's
cubic gate is exactly



$$
p^3\mid c_m
                  \iff A_0=A_1=B_0=0.                 \tag{2.5}
$$



## 3. Exact lift and carry theorem

Equation (2.3) first proves, before any reduction,



$$
\mathscr A\in p\mathbb Z_p,
     \qquad
     A_0\equiv {\mathscr A\over p}\pmod p.            \tag{3.1}
$$



If $A_0=0$, then $\mathscr A/p\in p\mathbb Z_p$.  Thus the second
division is exact and



$$
\mathscr A\in p^2\mathbb Z_p,
     \qquad
     A_1\equiv {\mathscr A\over p^2}\pmod p.          \tag{3.2}
$$



This proves (1.1).  Separately, $B_0=0$ says
$\mathscr B\in p^2\mathbb Z_p$.  It does not participate in the proof
of (3.2).

For the carry form, write



$$
L_\nu=\ell_{\nu,0}+p\ell_{\nu,1}+p^2\ell_{\nu,2},
 \qquad
 X_\nu=x_{\nu,0}+px_{\nu,1}+p^2x_{\nu,2}\pmod {p^3}, \tag{3.3}
$$



and set



$$
S_n=\sum_{q=0}^n
 \bigl(\ell_{1,q}x_{0,n-q}-\ell_{0,q}x_{1,n-q}\bigr). \tag{3.4}
$$



Rank one gives $p\mid S_0$, so define the integer



$$
c_0={S_0\over p}.        \tag{3.5}
$$



The first gate is



$$
A_0\equiv S_1+c_0\pmod p.    \tag{3.6}
$$



If $A_0=0$, then the numerator in



$$
c_1={S_1+c_0\over p}     \tag{3.7}
$$



is divisible by $p$ before reduction.  The second digit is therefore



$$
\boxed{A_1\equiv S_2+c_1\pmod p.} \tag{3.8}
$$



Equations (3.5) and (3.7) are the two certified exact divisions.  Signed
raw convolutions and negative carries are allowed; the final digits are
the canonical residues in $\{0,\ldots,p-1\}$.

## 4. Actual common-moving-content no-go

Use Item 205's notation



$$
k=3s+2,
 \qquad
 F_s(x)={ (1-x^4)^{2s}\over(1-x)^{5s+3}}
       =\sum_{n\ge0}A_n(s)x^n.                         \tag{4.1}
$$



The actual initial state $A_0=1$, $A_n=0$ for $n<0$, obeys



$$
(n+1)A_{n+1}
 =(5s+3)(A_n+A_{n-1}+A_{n-2})+(n-3s)A_{n-3},          \tag{4.2}
$$



and



$$
g_1=A_k,
 \qquad
 g_0=A_k+A_{k-1}+A_{k-2}+A_{k-3}.                    \tag{4.3}
$$



For an odd prime $p>k$, Item 205 proves that
$p\mid\gcd(g_0,g_1)$ is exactly common $p$-content of the reduced
three-coordinate moving vector.  It forces $A_0=B_0=0$ for every
admissible $j$, but contains no second-lift information.

The standalone checker obtains the following actual-seed terminal states.
Every row in this table is **FINITE** as a computation.



$$
\begin{array}{c|c|c|c}
s&p&(A_{k-3},A_{k-2},A_{k-1},A_k)\bmod p&(g_0,g_1)\bmod p\\ \hline
3&19&(15,4,0,0)&(0,0)\\
299&1499&(468,1031,0,0)&(0,0)\\
299&2399&(7,2392,0,0)&(0,0)
\end{array}                                             \tag{4.4}
$$



The corresponding modulo-$p^3$ Hasse replays are:



$$
\begin{array}{c|c|c|c|c|c|c}
s&p&j&m&(d^A_0,d^A_1,d^A_2)&(d^B_0,d^B_1,d^B_2)&
(A_0,A_1,B_0)\\ \hline
3&19&1&17&(0,0,16)&(0,0,14)&(0,16,0)\\
3&19&3&36&(0,0,0)&(0,0,4)&(0,0,0)\\
299&1499&1&1349&(0,0,925)&(0,0,1368)&(0,925,0)\\
299&2399&1&2249&(0,0,404)&(0,0,874)&(0,404,0)
\end{array}                                             \tag{4.5}
$$



The first two rows have the same reduced moving vector — zero — and the
same $(p,s)$, yet different $A_1$.  Hence no rule using only the
Item 196 moving vector, its common Smith content, the two first gates, or
the affine ray relation can determine $A_1$.  This is an actual-seed
obstruction, not a formal CRT countermodel.

For the proved infinite common-content ray



$$
s\equiv3\pmod4,
                   \qquad p=5s+4\text{ prime},         \tag{4.6}
$$



the $p=19$ and $p=1499$ rows in (4.5) show that the ray mechanism
does not force $A_1=0$ identically.  This does not rule out infinitely
many zero rows or an eventual pattern; no density assertion follows.

The point $p=2399=8s+7$ is also an exact nonzero second-lift witness.
Only this $s=299$ common-content point is certified.  In particular,
there is no theorem here that $p=8s+7$ is an infinite content ray.

## 5. Automatic anchor degeneration

Put



$$
A=3j+2,
                         \qquad K=2j+2.                \tag{5.1}
$$



Use the Cayley coordinate of Items 175/181,



$$
x={y-1\over y+1},
 \qquad D(y)=y(1+y^2),
 \qquad
 F_j\,dx\doteq{(1-y)^A\over D(y)^K}\,dy,             \tag{5.2}
$$



where $\doteq$ suppresses a nonzero constant.  Suppose (1.2), and set



$$
h=p-K,
                         \qquad r=A-p=j-h.             \tag{5.3}
$$



Then $1\le h\le j$.  With $H=(1-y)/D(y)$, (5.2) becomes



$$
F_j\,dx\doteq H(y)^pP_0(y)\,dy,
 \qquad P_0=(1-y)^rD^h.                               \tag{5.4}
$$



For $a\in\{-1,i,-i\}$, write



$$
{1\over x-a}={1+y\over\lambda_a(y)},
 \qquad \lambda_a(y)=(1-a)y-(1+a).                   \tag{5.5}
$$



Up to a unit, $\lambda_a$ is one of the three linear factors of
$D$.  Therefore



$$
{F_j\over x-a}\,dx
 \doteq H(y)^pP_a(y)\,dy,
 \qquad
 P_a=(1-y)^r(1+y){D^h\over\lambda_a}.                \tag{5.6}
$$



Both polynomial factors have the same degree,



$$
\deg P_0=\deg P_a=r+3h=j+2h\le2j+h=p-2.             \tag{5.7}
$$



Write either polynomial as $P=\sum_{n=0}^{p-2}c_ny^n$.  In
characteristic $p$, $d(H^p)=0$, and every $n+1$ is a unit.  Hence



$$
H^pP\,dy
 =d\left(H^p\sum_{n=0}^{p-2}{c_n\over n+1}y^{n+1}\right). \tag{5.8}
$$



Thus the base differential and every divided differential in (5.6) are
rationally exact modulo $p$.  Their logarithmic and circular coordinates
vanish; every fixed coordinate vector lies on the relative $R$-axis.
Consequently both wedges



$$
R_jL_{j,a}-L_jR_{j,a},
 \qquad E_jL_{j,a}-L_jE_{j,a}                         \tag{5.9}
$$



vanish modulo $p$.  Since $p\ge K+1$, all denominators in the
Item 196 first-gate contraction are units.  This proves



$$
\boxed{2j+3\le p\le3j+2\quad\Longrightarrow\quad
        A_0=B_0=0\text{ for every admissible }s.}      \tag{5.10}
$$



It does not prove $A_1=0$.  The smallest admissible exact control is



$$
(j,p,s,m)=(2,7,0,10),
 \quad(d^A_0,d^A_1,d^A_2)=(0,0,1),
 \quad(d^B_0,d^B_1,d^B_2)=(0,0,0).                   \tag{5.11}
$$



### Zero-rate bound

The cell equation and admissibility give



$$
\begin{aligned}
 6m
 &=3(j+1)p-3s-3\\
 &\ge3(j+1)p-(p-3)-3\\
 &=(3j+2)p\\
 &\ge p^2.
\end{aligned}                                         \tag{5.12}
$$



Therefore every automatic-anchor prime is at most $\sqrt{6m}$, and



$$
\sum_{\text{automatic-anchor }p}\log p
 \le\vartheta(\sqrt{6m})=O(\sqrt m)=o(m).             \tag{5.13}
$$



Even a hypothetical identity $A_1=0$ on all these rows would therefore
add zero normalized Route-1 exponent.

## 6. Finite audit and rate ledger

The checker evaluates every admissible row with



$$
1\le j\le12,
 \qquad 2j+3\le p\le3j+2.                             \tag{6.1}
$$



This **FINITE** box contains 77 rows.  All 77 have $A_0=B_0=0$, as
predicted by (5.10); 8 have $A_1=0$, and 69 have $A_1\ne0$.  These
counts audit the exact formula and display both possibilities.  They are
not an estimate of an asymptotic frequency.

The deterministic thin-family ledger is:

1. On $p=5s+4$, the cell relation gives
   

$$
10m+1=(5j+4)p.             \tag{6.2}
$$


   Thus the fixed-$m$ log weight is $O(\log m)$.

2. If the isolated relation $p=8s+7$ were ever promoted to a family,
   it would satisfy
   

$$
16m+1=(8j+7)p,             \tag{6.3}
$$


   and would again have only $O(\log m)$ fixed-$m$ log weight.

3. The whole automatic-anchor interval has the $O(\sqrt m)$ bound
   (5.13).

Accordingly, the content/anchor repackaging by itself contributes **zero
new exponent**.  A positive-rate advance would require genuinely moving
information outside these thin mechanisms.

## 7. Deterministic portable package

The standard-library checker

    work/item209_second_lift_digit_certificate.py

is standalone.  It includes the local Gaussian Hasse recurrence with its
factorial-valuation precision reserve, so it has no archive-path or
third-party dependency.  It performs the following exact tasks:

1. reconstructs $(L_\nu,X_\nu=pR_\nu,E_\nu)\bmod p^3$;
2. forms both raw determinants and independently reconstructs their three
   digits from signed convolutions and carries;
3. verifies both exact divisions in (3.5) and (3.7) before reducing;
4. replays the actual coefficient recurrence (4.2) at the three
   common-content points in (4.4);
5. reproduces all five distinguished Hasse controls, including the
   $p=1499$ and $p=2399$ rows;
6. audits (5.7), (5.10), and (5.12) in the finite box (6.1).

Canonical and replay JSON are required to be byte-identical.  The portable
manifest pins the report, checker, and both JSON files.  No archive metadata
is edited.

## 8. Status ledger

### PROVED

- the all-row exact quotient and carry formula (3.1)--(3.8);
- the actual-seed nonzero no-go witnesses in (4.5);
- the automatic-anchor first-gate theorem (5.10);
- the zero-rate bounds (5.13), (6.2), and conditional identity (6.3).

### FINITE

- the exact $p=1499$ and $p=2399$ Hasse computations;
- the actual-seed terminal states in (4.4);
- the complete $j\le12$ automatic-anchor audit.

### OPEN

- any global exclusion or zero-rate theorem for $A_1=0$ outside the
  thin mechanisms isolated here;
- any asymptotic density statement for the joint gate
  $A_0=A_1=B_0=0$;
- any infinite common-content theorem for $p=8s+7$;
- any new Route-1 exponent or conclusion about $e+\pi$.
