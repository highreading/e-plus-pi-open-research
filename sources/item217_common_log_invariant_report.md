> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 217 — retained-state common-log invariants and the two decisive cells

## 1. Outcome

This item returns to the normalized common-log obstruction of Items 197, 200,
and 203 after the forced Cartier factor has been removed.

The strongest new exact facts are:

1. The raw pair $(C_0(m),C_1(m))$ satisfies an all-$m$ contiguous
   relation linking $m$ and $m+1$.  A rational constant-term telescoper
   proves the relation, and both coefficient covectors have completely
   factored polynomial gcds and completely factored primitive resultants.
2. The actual five-coordinate Frobenius-defect vector separates as a
   $3\times4$ incidence matrix applied to a fixed $j$-vector.  In the
   convention of Item 203 the first two vectors are
   

$$
J_1=(-12,-12,6,12),\qquad
      J_2=(-245,70,315,-35).
$$


3. In the frozen Item 197 coordinates the two decisive cells simplify much
   further:
   

$$
\begin{array}{c|c}
      j=1&2Y'_0-Y_0=2Y'_1-Y_1=0,\\[2mm]
      j=2&9X_0-10Y_0+Y'_0=9X_1-10Y_1+Y'_1=0.
   \end{array}                                      \tag{1.1}
$$


   These are necessary and sufficient common-log conditions, not merely
   projective necessary conditions.
4. Both thin phase edges have zero linear logarithmic rate.  This is an
   all-prime theorem, but it gives no positive linear-rate saving.

No all-prime exclusion of either line of (1.1) was obtained.  The standard
finite-logarithm functional equations preserve nontrivial moving coefficient
moments rather than eliminating them.  The raw contiguous relation also does
not survive division by the discontinuous Cartier product $F_m$.  Thus the
normalized radical bound and every positive new rate remain **OPEN**.

There is nevertheless a sharp quantitative target.  The $j=1$ and $j=2$
cell masses are respectively $1/6$ and $2/35$ per $m$, or $1/36$
and $1/105$ per $6m$.  Proving both lines of (1.1) impossible for all
admissible primes would leave


$$
0.3370475079987658-\frac16-\frac2{35}
   =0.1132379841892420\ldots                         \tag{1.2}
$$


per $m$, hence


$$
0.0188729973648737\ldots                           \tag{1.3}
$$


per $6m$.  This is below the required gap
$0.01963298366943179388\ldots$ by
$0.0007599863045581\ldots$.  Equation (1.3) is a sufficient paired
fixed-cell target; it is not a proved exclusion.

## 2. Setup and the retained five-coordinate state

Put


$$
A(v)=1-3v+2v^2,\qquad D(v)=1-2v+2v^2,
$$


and, on an admissible PNT row,


$$
4m+1=(2j+1)p-2s,\quad
 1\le s\le\frac{p-3}{6},\quad 3j+1<p.               \tag{2.1}
$$


As in Item 203, set


$$
a=3j+1,\quad c=2j+1,\quad
 r=\frac{p-6s-3}{2},\quad q=2s-1,\quad
 P=A^rD^q,\quad L=\deg P=p-2s-5.                    \tag{2.2}
$$


For $R=A,D$, write


$$
\Delta_pR(v)=\frac{R(v)^p-R(v^p)}p.    \tag{2.3}
$$


All congruences below are modulo $p$.

Define the fixed four-vector


$$
\begin{aligned}
u_0&=[y^{c-1}]\frac{A(y)^{a-1}}{D(y)^c},&
u_1&=[y^{c-2}]\frac{A(y)^{a-1}}{D(y)^c},\\
v_0&=[y^{c-1}]\frac{A(y)^a}{D(y)^{c+1}},&
v_1&=[y^{c-2}]\frac{A(y)^a}{D(y)^{c+1}},\\
J_j&=(au_0,au_1,-cv_0,-cv_1).                       \tag{2.4}
\end{aligned}
$$


For $1\le t\le5$, define the moving row


$$
w_t=\bigl(
 [v^{L+t}]\Delta_pA\,P,
 [v^{p+L+t}]\Delta_pA\,P,
 [v^{L+t}]\Delta_pD\,P,
 [v^{p+L+t}]\Delta_pD\,P
 \bigr).                                             \tag{2.5}
$$


Only the two displayed $p$-sections can reach the target.  Directly
separating them in Item 203's defect formula gives


$$
e_{t-4}=w_tJ_j^{\mathsf T}.         \tag{2.6}
$$


The normalized common-log condition is therefore exactly


$$
\boxed{
 \begin{pmatrix}
   w_4\\ w_3-2w_1\\ w_2-2w_1
 \end{pmatrix}J_j^{\mathsf T}=0.}                   \tag{2.7}
$$


The scalar recurrence then also gives $w_5J_j^{\mathsf T}=0$.  Unlike a
local recurrence kernel, (2.7) retains the actual Frobenius-defect seed.
Evaluation of (2.4) gives


$$
J_1=(-12,-12,6,12),\qquad
 J_2=(-245,70,315,-35),                              \tag{2.8}
$$


as claimed.

Equivalently, if $h_t=w_tJ_j^{\mathsf T}$, the three conditions are
$h_2=2h_1$, $h_3=2h_1$, and $h_4=0$.  This is the exact
five-coordinate convention behind (2.7); it should not be confused
componentwise with Item 197's three frozen coefficients below.

## 3. Exact collapse of the $j=1$ and $j=2$ cells

Use Item 197's notation


$$
A_p(z)=-\sum_{k=1}^{p-1}\frac{z^k}{k},\qquad
 B_p(z)=\sum_{k=1}^{p-1}\frac{(-1)^{k-1}z^{2k}}k,    \tag{3.1}
$$




$$
\begin{aligned}
 X_\nu&=[z^{p-q_\nu-1}]A_pP_\nu,\\
 Y_\nu&=[z^{p-q_\nu-1}]B_pP_\nu,\\
 Y'_\nu&=[z^{2p-q_\nu-1}]B_pP_\nu,
 \qquad q_\nu=2s-\nu,                              \tag{3.2}
\end{aligned}
$$


where


$$
P_\nu=(1-z)^r(1+z)^{1+3\nu}(1+z^2)^{q_\nu}.       \tag{3.3}
$$


The exact quotient digit is


$$
\frac{C_\nu(m)}p\equiv
 (3j+1)U_jX_\nu-(2j+1)(V_jY_\nu+W_jY'_\nu),        \tag{3.4}
$$


with


$$
\begin{aligned}
U_j&=[y^{2j}]\frac{(1-y)^{3j}}{(1+y^2)^{2j+1}},\\
V_j&=[y^{2j}]\frac{(1-y)^{3j+1}}{(1+y^2)^{2j+2}},\\
W_j&=[y^{2j-1}]\frac{(1-y)^{3j+1}}{(1+y^2)^{2j+2}}.
                                                               \tag{3.5}
\end{aligned}
$$


The complete integer evaluations and their primitive factorizations are


$$
\begin{array}{c|c|c}
j&(U_j,V_j,W_j)&C_\nu(m)/p\\ \hline
1&(0,2,-4)&6(2Y'_\nu-Y_\nu),\\
2&(-45,-70,7)&-35(9X_\nu-10Y_\nu+Y'_\nu).
\end{array}                                           \tag{3.6}
$$


All admissible primes in these two cells exceed $7$, so the scalar
factors are units.  Consequently (3.6) proves the two necessary and
sufficient pairs in (1.1).  This is stronger than the insufficient
projective determinant from Item 197.

The admissibility inequalities do **not** force either primitive pair into
finite prime support: after removal of $6$ and $-35$, the entries are
moving truncated-log moments for every admissible $(p,s)$.  Thus the
desired fixed-cell exclusion remains an infinite arithmetic problem.

## 4. What the finite-log functional equations do and do not remove

The degree-one finite logarithm obeys the exact polynomial identities


$$
A_p(z)=A_p(1-z),\qquad
 A_p(z)=-z^pA_p(1/z),                                \tag{4.1}
$$


and


$$
B_p(z)=A_p(-z^2)=A_p(1+z^2).                        \tag{4.2}
$$


They follow coefficientwise from
$p^{-1}\binom pk\equiv(-1)^{k-1}/k$, so no external theorem is needed.
They are also the $n=1$ instances of the finite-polylogarithm framework;
see [Besser, *Finite and p-adic polylogarithms*](https://arxiv.org/abs/math/0006051).

For the present coefficient problem, however, (4.1)--(4.2) transform the
logarithm and the moving weight simultaneously.  In particular,


$$
\frac{P_1}{P_0}=\frac{(1+z)^3}{1+z^2},        \tag{4.3}
$$


while the low and high extraction degrees in (3.2) differ by $p$.  The
maps $z\mapsto1-z$, $1/z$, and $-z^2$ do not identify those two
weighted extraction functionals.  Hence they do not turn either line of
(1.1) into a fixed polynomial in $p,s$, or into a nonzero constant.

This is a scoped no-go for the direct finite-log functional-equation
reduction only.  It does not prove that a different identity cannot exclude
the two cells.  The finite replay also contains individual moment zeros, so
proving only one coordinate nonzero is not viable: for example
$(j,p,s;C_0/p,C_1/p)=(1,29,1;3,0)$,
$(1,109,11;0,101)$, and $(2,109,8;40,0)$.

## 5. An exact all-$m$ contiguous relation

The coefficient pair has the constant-term representation


$$
R(z)=\frac{(1-z)^6}{z^4(1+z^2)^4},\quad
 f_0(z)=\frac{1+z}{1+z^2},\quad
 f_1(z)=\frac{(1+z)^4}{z(1+z^2)^2},                 \tag{5.1}
$$




$$
C_\nu(m)=\operatorname{CT}_z R(z)^m f_\nu(z). \tag{5.2}
$$


Exact creative telescoping gives


$$
\boxed{A_mC_0(m)+B_mC_0(m+1)+D_mC_1(m)+E_mC_1(m+1)=0,}        \tag{5.3}
$$


where


$$
\begin{aligned}
A_m={}&-6(3m+1)(6m+1)(6m+5)\\
 &\quad\cdot(1480100m^4+3217800m^3+2450801m^2+775695m+85874),\\
B_m={}&-32(m+1)(2m+1)(4m+1)(4m+3)\\
 &\quad\cdot(8700m^3+22100m^2+16887m+3782),\\
D_m={}&15(3m+1)(4m+1)(6m+1)(6m+5)\\
 &\quad\cdot(59204m^3+113256m^2+68461m+13149),\\
E_m={}&80(m+1)(2m+1)(4m+1)(4m+3)(4m+5)(6m+5)(58m+23).
                                                               \tag{5.4}
\end{aligned}
$$



Here is an exact certificate for all $m$, rather than a guessed finite
recurrence.  There is a polynomial $N(z,m)\in\mathbb Z[z,m]$, of degree
$13$ in $z$ and $6$ in $m$, listed coefficientwise in the checker.
Put


$$
S(z,m)=\frac{(1-z)N(z,m)}{z^5(1+z^2)^5}.       \tag{5.5}
$$


If


$$
H=A_mf_0+B_mRf_0+D_mf_1+E_mRf_1,                  \tag{5.6}
$$


then the checker verifies in $\mathbb Z[m,z]$, after clearing the common
denominator, the identity


$$
H=zS'+m\,z\frac{R'}R S.                \tag{5.7}
$$


Equivalently,


$$
R^mH=z\frac{d}{dz}(R^mS).                   \tag{5.8}
$$


The constant term of a logarithmic derivative is zero, so (5.8) proves
(5.3).  The cleared identity has degree at most $7$ in $m$; the
certificate checks its eight integer specializations $m=0,\ldots,7$,
which is an exact interpolation proof.

## 6. Factored resultants and the exact recurrence obstruction

Define


$$
\begin{aligned}
K_0&=(3m+1)(6m+1)(6m+5),\\
K_1&=(m+1)(2m+1)(4m+1)(4m+3),\\
a_4&=1480100m^4+3217800m^3+2450801m^2+775695m+85874,\\
d_3&=59204m^3+113256m^2+68461m+13149,\\
b_3&=8700m^3+22100m^2+16887m+3782,\\
e_3&=(4m+5)(6m+5)(58m+23).
                                                               \tag{6.1}
\end{aligned}
$$


After removing the polynomial and numerical gcds, the two covectors in
(5.3) are represented by


$$
(-2a_4,\;5(4m+1)d_3),\qquad (-2b_3,\;5e_3).  \tag{6.2}
$$


Their primitive polynomial resultants factor completely as


$$
\begin{aligned}
\left|\operatorname{Res}(a_4,(4m+1)d_3)\right|
 &=2^{17}3^4 5^3 7^2 19^2 41\,71\,1531\,2683,\\
\left|\operatorname{Res}(b_3,e_3)\right|
 &=2^{10}3^3 5\,11\,29\,43\,79\,1531.
                                                               \tag{6.3}
\end{aligned}
$$


Thus, outside explicit finite prime support, simultaneous degeneration of a
covector can occur only through $K_0$ or $K_1$.  On an admissible row,
(2.1) shows


$$
p\nmid K_0,\qquad p\mid K_1\Longleftrightarrow s=1. \tag{6.4}
$$


For example, modulo $p$,
$4(3m+1)=1-6s$, $2(6m+1)=-6s-1$, and
$2(6m+5)=7-6s$; the allowed range makes all three nonzero.  Similarly,
the four factors of $K_1$ reduce, after multiplying by units, to
$3-2s$, $1-2s$, $-2s$, and $2-2s$, so only the last can vanish,
at $s=1$.

This nonsingularity does not close the problem.  If the divided pair at
$m$ vanishes, (5.3), divided by $p$ along a same-prime phase chain,
places the next divided pair on one nonzero projective line.  A single
covector in a two-dimensional space always has such a kernel.  The
resultants certify that the line is usually well-defined; they do not turn
it into zero propagation.  This is the precise recurrence/resultant no-go.
The checker also has a $40\times32$ modular matrix of rank $31$, proving
that (5.3) spans the complete order-one, coefficient-degree-at-most-seven
relation ansatz over $\mathbb Q$.  Thus no second covector exists in that
bounded ansatz.  This rank statement does not exclude a higher-order or
higher-degree invariant.

Nor may (5.3) simply be applied to the normalized pair
$\bar C_\nu=C_\nu/F_m$.  The Cartier product changes with $m$.  At
$m=1$, $F_1=1$, $F_2=11$, the raw residue in (5.3) is zero, but the
same expression with $C_\nu(k)/F_k$ equals


$$
-73214064000\ne0.              \tag{6.5}
$$


Thus normalization does not survive this recurrence.

## 7. A genuine all-prime two-edge zero-rate theorem

For fixed $m$, every candidate with $s\le S$ satisfies


$$
4m+1+2s=(2j+1)p.                     \tag{7.1}
$$


Consequently the total logarithmic weight of all such primes is at most


$$
\sum_{s=1}^{S}\log(4m+1+2s)
        \le S\log(4m+1+2S).                          \tag{7.2}
$$



There is a matching statement at the upper phase edge.  Let
$s_{\max}=\lfloor(p-3)/6\rfloor$ and $t=s_{\max}-s$.  If
$p\equiv1\pmod6$, elimination of $s$ from (2.1) gives


$$
6m-2-3t=(3j+1)p,                  \tag{7.3}
$$


whereas for $p\equiv5\pmod6$,


$$
6m-1-3t=(3j+1)p.                  \tag{7.4}
$$


For $0\le t\le T$, the total logarithmic weight is therefore at most


$$
2(T+1)\log(6m).                   \tag{7.5}
$$


Equations (7.2) and (7.5) apply to all candidate primes and hence to all
common-log primes.  If $S,T=o(m/\log m)$, both edges contribute $o(m)$.

This theorem is structurally informative but books no new linear exponent:
it removes only thin phase layers.  The unresolved bulk still has the full
linear capacity relevant to (1.2).

## 8. Deterministic replay and final status

The standalone checker verifies:

1. the bivariate telescoper and 80 exact instances of (5.3);
2. both Sylvester resultants and every prime exponent in (6.3);
3. the normalization counterexample (6.5);
4. the vectors (2.8), the incidence (2.7), and the bridge back to (3.4);
5. the primitive reductions (3.6) for every replayed row;
6. the functional equations (4.1)--(4.2) by exact finite-field polynomial
   arithmetic; and
7. 329 admissible $j=1$ rows and 331 admissible $j=2$ rows through
   $p\le199$, with no simultaneous collision.

The last statement is **EXACT FINITE ONLY**.  Individual coordinate zeros
do occur.  No density, all-prime nonvanishing, radical bound, or positive
rate follows from the scan.

### PROVED

- The retained-state incidence (2.7) and the exact vectors (2.8).
- The primitive fixed-cell congruences (1.1).
- The all-$m$ contiguous relation (5.3) with rational telescoper.
- The factored degeneracy support (6.3)--(6.4).
- The two-edge zero-rate theorem (7.2), (7.5).
- The paired-cell threshold (1.2)--(1.3) as a conditional sufficient target.

### OPEN

- All-prime exclusion of the $j=1$ and $j=2$ congruences.
- Any positive linear-rate reduction of the normalized common-log radical.
- Any subexponential bound for
  $\gcd(C_0/F_m,C_1/F_m)$.

### RATE CONSEQUENCE

The unconditional new rate is zero and the new divisibility exponent is
zero.  If, and only if, both fixed cells are subsequently excluded, their
combined mass would lower the residual ceiling below the Route-1 gap by
$0.0007599863045581\ldots$ per $6m$.
