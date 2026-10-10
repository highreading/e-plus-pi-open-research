> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact audit of the 239-adic endpoint pattern

Date: 2026-08-26

This note audits the endpoint-matched Machin Hermite--Padé system implemented
in scripts/mixed_hermite_pade_probe.py.  The numerical observation through
degree 18 was



$$
v_{239}(A_{\mathrm{end}})=0,\qquad
 v_{239}(B_{\mathrm{end}})=\text{largest odd integer at most }n,
$$



after first making the polynomial coefficient vector primitive over the
integers and then dividing the two endpoint coefficients by their gcd.

The proposed all-degree pattern is false.  There is an exact counterexample
at



$$
p=239,\qquad n=65:
\qquad
 v_p(A_{\mathrm{end}})=0,\quad
 v_p(B_{\mathrm{end}})=66.
$$



This occurs while $3n=195<p$, so it is not an artifact of factorials
crossing a multiple of 239.  The cancellation is already visible in the
leading determinant modulo 239.

The independently executable exact certificate is
scripts/machin_239_counterexample.py.  It uses integer arithmetic modulo
$239$ and $239^2$, and contains assertions for every residue quoted
below.

## 1. Reduced endpoint-matched system

Write



$$
G(z)=16\arctan(z/5)-4\arctan(z/p)
    =\sum_{r\geq 0}g_rz^r,\qquad p=239.
$$



For positive odd $r$,



$$
g_r=\frac{(-1)^{(r-1)/2}}{r}
 \left(\frac{16}{5^r}-\frac{4}{p^r}\right),
$$



and $g_r=0$ for even $r$, including $g_0=0$.

Let



$$
A(z)=\sum_{j=0}^n a_jz^j,\quad
B(z)=\sum_{j=0}^n b_jz^j,\quad
C(z)=\sum_{j=0}^n c_jz^j.
$$



The conditions are



$$
A(z)+B(z)e^z+C(z)G(z)=O(z^{3n+1}),\qquad C(1)=B(1).
$$



The Taylor equations of degrees $0,\ldots,n$ determine the $a_j$.
The remaining $2n+1$ equations in the $2n+2$ variables
$(b_0,\ldots,b_n,c_0,\ldots,c_n)$ are



$$
\sum_{j=0}^n\frac{b_j}{(k-j)!}
+ \sum_{j=0}^n c_jg_{k-j}=0
\quad(n+1\leq k\leq 3n),                                      \tag{1}
$$



where a term with negative factorial index is absent, together with



$$
\sum_{j=0}^n(c_j-b_j)=0.                                      \tag{2}
$$



Call this $(2n+1)$-by-$(2n+2)$ matrix $D_n$.

After eliminating $A$, its endpoint value is the linear functional



$$
L_A=-\sum_{j=0}^nE_{n-j}b_j-\sum_{j=0}^nG_{n-j}c_j,            \tag{3}
$$



where



$$
E_m=\sum_{r=0}^m\frac1{r!},\qquad
G_m=\sum_{r=0}^m g_r.
$$



The other endpoint functional is



$$
L_B=\sum_{j=0}^n b_j.                                         \tag{4}
$$



Define the square bordered determinants



$$
\Delta_A=\det\begin{pmatrix}D_n\\L_A\end{pmatrix},\qquad
\Delta_B=\det\begin{pmatrix}D_n\\L_B\end{pmatrix}.             \tag{5}
$$



If $\Delta_A\ne0$, then $D_n$ has full row rank and its kernel is
one-dimensional.  Expansion by the last row in (5) shows that, for every
nonzero kernel vector,



$$
\frac{B(1)}{A(1)}=\frac{\Delta_B}{\Delta_A}                    \tag{6}
$$



up to a common sign, which does not affect valuations.  Thus



$$
v_p\!\left(\frac{B(1)}{A(1)}\right)
=v_p(\Delta_B)-v_p(\Delta_A).                                 \tag{7}
$$



This quotient is invariant under both normalizations performed by the
probe.

## 2. The clean range $3n<p$

When $0<r<p$ is odd,



$$
v_p(g_r)=-r,\qquad
p^rg_r\equiv
-\frac{4(-1)^{(r-1)/2}}r\pmod p.                              \tag{8}
$$



All factorials in (1) are also $p$-units when $3n<p$.
Consequently the least-valuation part of each bordered determinant can be
read from an explicit matrix over $\mathbf F_p$.

### 2.1 The leading matrix for $\Delta_B$

In the matrix defining $\Delta_B$, add the appended $L_B$ row to the
endpoint row (2).  This turns (2) into the pure $C$-endpoint row
$\sum c_j=0$.

Use the following powers of $p$:



$$
\begin{array}{c|c}
\text{object}&\text{power}\\ \hline
\text{jet row }k&\max(0,k-2n)\\
\text{pure \(C\)-endpoint row}&-n\\
\text{\(B\)-endpoint row}&0\\
b_j\text{ column}&0\\
c_j\text{ column}&2n-j.
\end{array}                                                    \tag{9}
$$



Every resulting entry is $p$-integral.  The sum of all row and column
powers is



$$
n(2n+1).                                                       \tag{10}
$$



Modulo $p$, the scaled matrix is block upper triangular.  Its lower-right
block consists of the jet rows $k=2n+1,\ldots,3n$, the pure $C$-endpoint
row, and the $c_j$ columns.  The endpoint row selects $c_n$.  The
remaining matrix splits by parity into two Cauchy matrices, with entries
equal to nonzero row and column factors times



$$
\frac1{k-j}.
$$



All row parameters and column parameters are distinct modulo $p$, and
$0<k-j\leq3n<p$.  The Cauchy determinant formula therefore proves that
this high-$C$ block is nonsingular modulo $p$.

The upper-left block consists of the rows $k=n+1,\ldots,2n$, the
$B$-endpoint row, and the $b_j$ columns.  Multiplication of jet row
$k$ by the unit $k!$ gives



$$
(1,(k)_1,\ldots,(k)_n),\qquad
(k)_j=k(k-1)\cdots(k-j+1).
$$



The only degree-$n$ polynomial, up to a scalar, that vanishes at all
$k=n+1,\ldots,2n$ is



$$
Q_n(x)=\prod_{k=n+1}^{2n}(x-k)
      =\sum_{j=0}^nq_j(x)_j,                                  \tag{11}
$$



where direct finite-difference expansion gives



$$
q_j=(-1)^{n-j}\frac{(2n-j)!}{(n-j)!\,j!}.                     \tag{12}
$$



For completeness, (12) follows immediately from the falling-factorial
translation identity



$$
(x+y)_n=\sum_{j=0}^n\binom nj(x)_j(y)_{n-j}.
$$



Indeed, $Q_n(x)=(x-(n+1))_n$, and



$$
(-(n+1))_{n-j}
=(-1)^{n-j}\frac{(2n-j)!}{n!}.
$$



The final row of the block is all ones.  Hence this block is nonsingular
modulo $p$ exactly when



$$
S_n=\sum_{j=0}^nq_j\not\equiv0\pmod p.                        \tag{13}
$$



Put $T_n=(-1)^nS_n$.  Formula (12) gives



$$
T_n=\sum_{j=0}^n(-1)^j
\frac{(2n-j)!}{(n-j)!\,j!}.                                  \tag{14}
$$



Here is a direct proof of the recurrence needed below.  Define



$$
Y_n(x)=\sum_{k=0}^n
\frac{(n+k)!}{k!(n-k)!}\left(\frac{x}{2}\right)^k.
$$



Changing variables $k=n-j$ in (14) gives
$T_n=(-1)^nY_n(-2)$.  Direct comparison of the coefficient of every
power $x^k$ gives



$$
Y_{m+1}(x)=(2m+1)xY_m(x)+Y_{m-1}(x)\qquad(m\geq1).
$$



Evaluating this identity at $x=-2$ and multiplying by
$(-1)^{m+1}$ proves



$$
T_0=T_1=1,\qquad
T_{m+1}=(4m+2)T_m+T_{m-1}.                                   \tag{15}
$$



Thus the conjectured leading valuation for $\Delta_B$ silently requires
$T_n\not\equiv0\pmod{239}$.

### 2.2 The first failure

Exact iteration of (15) modulo 239 gives



$$
\begin{array}{c|rrrrrrrr}
m&58&59&60&61&62&63&64&65\\ \hline
T_m\bmod239&68&214&93&15&198&42&111&0.
\end{array}                                                    \tag{16}
$$



There are no zero residues for $1\leq m<65$.  At $n=65$, however,
the nominal least-valuation determinant vanishes modulo 239.  Therefore
the finite pattern through degree 18 cannot extend to all degrees.

Vanishing of the leading residue alone proves only an increase of at least
one in $v_p(\Delta_B)$.  To determine the exact increase, the certificate
forms the fully scaled $132$-by-$132$ matrix from (9) modulo $p^2$.
Exact elimination with unit pivots gives



$$
\operatorname{rank}_{\mathbf F_p}=131,\qquad
p^{8515}\Delta_B\equiv28919
=239\cdot121\pmod{239^2}.                                    \tag{17}
$$



Since $8515=65(2\cdot65+1)$ and $121\not\equiv0\pmod{239}$,



$$
v_p(\Delta_B)=-8515+1=-8514.                                 \tag{18}
$$



## 3. The $A$-bordered determinant at $n=65$

For odd $n$, and in particular for $n=65$, use the powers



$$
\begin{array}{c|c}
\text{object}&\text{power}\\ \hline
\text{jet row }k&\max(0,k-(2n-1))\\
\text{endpoint and \(A\)-functional rows}&0\\
b_j\text{ column}&0\\
c_j\text{ column}&2n-1-j.
\end{array}                                                    \tag{19}
$$



Their sum is



$$
2n(n+1)=8580.                                                  \tag{20}
$$



All scaled entries are $p$-integral.  At $n=65$, every scaled $C$
entry in each of the last two rows is divisible by $p$.  For the endpoint
row this is immediate from $2n-1-j\geq64$.  For the $A$-functional row,
the lowest valuation in $G_{n-j}$ comes from the largest odd index at
most $n-j$, which is still at least 64 powers smaller than
$2n-1-j$.

The exact scaled determinant calculation modulo 239 gives



$$
p^{8580}\Delta_A\equiv181\pmod{239}.                           \tag{21}
$$



In particular, $\Delta_A\ne0$, so $D_{65}$ has full row rank and all
uses of the determinant quotient (6) are justified.  Equation (21) also
gives



$$
v_p(\Delta_A)=-8580.                                          \tag{22}
$$



There is a smaller hand-check for the only non-Cauchy part of (21).
For



$$
Q(x)=\prod_{k=66}^{129}(x-k)=\sum_{j=0}^{64}q_j(x)_j,
$$



the correct coefficients are



$$
q_j=(-1)^{64-j}
\frac{(129-j)!}{65\,j!\,(64-j)!}.                             \tag{23}
$$



Let



$$
L(v)=\sum_jv_j,\qquad
M(v)=-\sum_{j=0}^{65}E_{65-j}v_j.
$$



For the falling-factorial coefficient vectors of $Q$ and $xQ$, exact
reduction modulo 239 gives



$$
(L(Q),M(Q),L(xQ),M(xQ))=(113,205,111,177).
$$



The associated $2$-by-$2$ determinant is



$$
113\cdot177-111\cdot205\equiv114\not\equiv0\pmod{239}.         \tag{24}
$$



Together with the nonsingular parity-Cauchy high block, this explains
structurally why the full determinant in (21) is a unit.  The full matrix
residue 181 is retained in the executable certificate to eliminate any
dependence on omitted sign or ordering conventions.

## 4. Endpoint valuation and normalization

Combining (7), (18), and (22),



$$
v_p\!\left(\frac{B(1)}{A(1)}\right)
=-8514-(-8580)=66.                                            \tag{25}
$$



Take the unique rational kernel vector, clear all coefficient denominators,
and divide all polynomial coefficients by their common integer gcd, as in
the probe.  Its endpoint values $A(1)$ and $B(1)$ are nonzero integers.
Equation (25) says that their valuations differ by 66.  Dividing those two
endpoint integers by their gcd therefore gives



$$
v_{239}(A_{\mathrm{end}})=0,\qquad
v_{239}(B_{\mathrm{end}})=66.                                 \tag{26}
$$



The largest odd integer at most 65 is 65, so (26) is an exact
counterexample to the proposed pattern.

## 5. Why this does not give an all-degree height no-go theorem

There are three distinct obstructions.

First, the claimed valuation law itself is false.  Its leading determinant
contains the arithmetic factor $T_n$, and $T_{65}\equiv0\pmod{239}$.
Finite verification through $n=18$ cannot rule out such modular
cancellations.

Second, the clean determinant reduction above stops before degree 80.
For $n\geq80$, one has $3n\geq239$, and both basic valuation rules
change:



$$
v_p(1/r!)=-v_p(r!),\qquad
v_p(g_r)=-r-v_p(r)\quad\text{for odd }r.
$$



The least-valuation matching, the parity-Cauchy blocks, and possible
leading cancellations must then be recomputed across every factorial
regime.  The calculation at $n=65$ supplies no uniform formula in those
regimes.

Third, even a uniform divisibility statement would be only a height lower
bound, not an Archimedean no-go theorem.  If coprime endpoint integers
satisfied $p^r\mid B_{\mathrm{end}}$, then



$$
|B_{\mathrm{end}}|\geq p^r.
$$



For any endpoint-normalized auxiliary coefficient vector this also implies


$$
\max_j|b_j|\geq\frac{p^r}{n+1},
$$


because $B_{\mathrm{end}}=\sum b_j$.  But a large coefficient height does
not give a lower bound for



$$
|A_{\mathrm{end}}+B_{\mathrm{end}}(e+\pi)|.
$$



The two real summands can cancel arbitrarily closely unless an independent
Diophantine or asymptotic estimate prevents it.  Similarly, a Taylor-tail
estimate proportional to coefficient height is an upper bound.  Showing
that this upper bound fails to tend to zero does not show that the actual
linear form fails to tend to zero.

Accordingly, this 239-adic analysis yields neither an all-degree height
formula nor a no-go theorem for the Machin Hermite--Padé construction.  A
genuine all-degree no-go result would require at least:

1. a uniform determinant/valuation analysis including all multiples of
   239 and all modular cancellation loci; and
2. an independent Archimedean lower bound, or a complete asymptotic formula
   with a proved nonzero leading constant, for the endpoint linear form.

Neither ingredient follows from the observed finite valuation pattern.

## 6. Reproduction

Run

    python3 scripts/machin_239_counterexample.py

from the research directory.  The exact output is

    p=239, n=65, 3n=195<p
    T_64 mod p=111, T_65 mod p=0
    scaled Delta_B: rank mod p=131, determinant mod p^2=28919=239*121
    scaled Delta_A: determinant mod p=181
    v_p(Delta_B)=-8514
    v_p(Delta_A)=-8580
    v_p(B(1)/A(1))=66
    largest odd integer <=n is 65; the proposed pattern is false.

No floating-point computation or extrapolation is used.
