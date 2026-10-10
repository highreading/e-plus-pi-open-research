> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 274 — fixed reverse-Bessel determinants are blind to high singleton depth

Checked: 2026-08-31 (Beijing time)

## 1. Scope and verdict

Retain the beta denominator



$$
q_0=q_1=1,\qquad q_N=(4N-2)q_{N-1}+q_{N-2},             \tag{1.1}
$$



and the reverse-Bessel polynomial



$$
A_N(X)=\sum_{k=0}^N\frac{(2N-k)!}{k!(N-k)!}X^k,
\qquad q_N=A_N(-1).                                     \tag{1.2}
$$



Item 265 localized the still-uncontrolled matching mass to a prime power
supported at one block index.  A sufficient strengthening on matching
primes would be



$$
v_p(q_N)\log p=O(N),                                    \tag{1.3}
$$



uniformly in the actual family.  This item tests the reverse-Bessel
differential identity, the exponential Padé Wronskian, and every
fixed-length determinant made from their natural index shifts and jets.

> **PROVED — exact fixed-length determinant reduction.**  Fix once and
> for all a window $L$, jet order $J$, determinant size $s$, and
> polynomial coefficient degree $d$.  After one fixed common
> denominator is cleared, every $s\times s$ determinant whose entries
> are integral polynomial-coefficient linear forms in
> 

$$
> Z_{i,j}(N)=2^j A_{N+i}^{(j)}(-1),\qquad
> |i|\le L,\quad 0\le j\le J,                            \tag{1.4}
>
$$


> has the exact form
> 

$$
> \boxed{
> \mathscr D_N=\sum_{k=0}^s C_k(N)q_N^kq_{N+1}^{s-k},
> \qquad C_k\in\mathbb Z[N].}                           \tag{1.5}
>
$$


> Moreover
> 

$$
> \deg C_k\le s(d+L+J).                                 \tag{1.6}
>
$$



> **PROVED SCOPED NO-GO — singleton dichotomy.**  Let $k$ be the
> least index for which $C_k$ is not the zero polynomial.  Apart from
> the finitely many positive integer roots of $C_k$, if
> $a=v_p(q_N)>v_p(C_k(N))$, then
> 

$$
> \boxed{
> v_p(\mathscr D_N)=ka+v_p(C_k(N)),
> \qquad v_p(C_k(N))\log p=O_{\mathscr D}(\log N).}      \tag{1.7}
>
$$


> Thus $k=0$ is blind to the singleton depth, while $k\ge1$
> means that the determinant contains the formal factor $q_N^k$.
> If its integer value is nonzero,
> 

$$
> |\mathscr D_N|\ge q_N^k,
> \qquad \log|\mathscr D_N|\ge kN\log N+O_k(N).         \tag{1.8}
>
$$


> This is a no-go for obtaining (1.3) from the ordinary height of a
> fixed-length determinant.  It is not an absolute impossibility theorem
> for every use of that determinant.

> **PROVED — the Padé Wronskian is the unit branch.**  Its specialization
> is a unit modulo the full integer $q_N$; it proves argument-root
> simplicity but contains no information about $v_p(q_N)$.

The theorem handles a singleton prime power rather than hiding it in a
pairwise gcd.  It also carries Item 265's clearing overlap exactly: after
the already admitted reservoir is removed, the forced branch remains
divisible by the same power of



$$
\overline q_{m,N}=\frac{q_N}{\gcd(q_N,D_m)}.             \tag{1.9}
$$



No uniform bound (1.3), little-oh squarefull theorem, or capacity saving
follows.  The booking is zero.

## 2. The reverse-Bessel differential module

Coefficient comparison in (1.2) gives



$$
\boxed{2A_N'(X)=A_N(X)-XA_{N-1}(X).}                    \tag{2.1}
$$



Differentiating $j$ times and setting $X=-1$ gives



$$
2A_N^{(j+1)}(-1)
=A_N^{(j)}(-1)+A_{N-1}^{(j)}(-1)
-jA_{N-1}^{(j-1)}(-1).                                  \tag{2.2}
$$



With



$$
Z_{i,j}(N)=2^jA_{N+i}^{(j)}(-1),
$$



equation (2.2) becomes the integral recursion



$$
\boxed{
Z_{i,j+1}=Z_{i,j}+Z_{i-1,j}-2jZ_{i-1,j-1},
\qquad Z_{i,0}=q_{N+i}.}                                \tag{2.3}
$$



Consequently every fixed jet in (1.4) is an integral linear combination
of the fixed index window



$$
q_{N-L-J},\ldots,q_{N+L}.                               \tag{2.4}
$$



No derivative constant or infinite tail is introduced.  The factor
$2^j$ is a unit at every odd matching prime.

The first derivative already displays the blindness.  At a prime
$p\mid q_N$,



$$
2A_N'(-1)=q_N+q_{N-1}\equiv q_{N-1}\not\equiv0\pmod p, \tag{2.5}
$$



because adjacent beta denominators are coprime.  The polynomial root at
$-1$ is simple for every exponent $v_p(q_N)\ge1$.

## 3. Every fixed index window has two generators

Put formally



$$
F=q_N,\qquad G=q_{N+1}.
$$



The recurrence (1.1), read in both directions, gives polynomials
$U_i,V_i\in\mathbb Z[N]$ such that



$$
\boxed{q_{N+i}=U_i(N)F+V_i(N)G\qquad(i\in\mathbb Z).}   \tag{3.1}
$$



They begin with



$$
(U_0,V_0)=(1,0),\qquad (U_1,V_1)=(0,1),                 \tag{3.2}
$$



and satisfy



$$
\begin{aligned}
(U_{i+1},V_{i+1})
&=(4N+4i+2)(U_i,V_i)+(U_{i-1},V_{i-1}),\
(U_{i-1},V_{i-1})
&=(U_{i+1},V_{i+1})-(4N+4i+2)(U_i,V_i).
\end{aligned}                                           \tag{3.3}
$$



Induction gives



$$
\deg U_i,\deg V_i\le |i|.                              \tag{3.4}
$$



The transfer matrices have determinant $-1$; in particular the two
boundary coordinates are unimodular.  At any prime divisor of $F=q_N$,
$G=q_{N+1}$ is a unit.

Combining (2.3) and (3.1), each scaled jet has a unique reduction



$$
Z_{i,j}=\alpha_{i,j}(N)F+\beta_{i,j}(N)G,\qquad
\alpha_{i,j},\beta_{i,j}\in\mathbb Z[N],                \tag{3.5}
$$



with



$$
\deg\alpha_{i,j},\deg\beta_{i,j}\le L+J               \tag{3.6}
$$



on the window (1.4).

## 4. Exact admissible determinant class and proof of the dichotomy

Fix integers $L,J,s,d\ge0$.  An admissible fixed-length determinant is



$$
\mathscr D_N=\det(H_{ab}(N))_{1\le a,b\le s},           \tag{4.1}
$$



where



$$
H_{ab}(N)=
\sum_{|i|\le L}\sum_{0\le j\le J}
P_{ab,i,j}(N)Z_{i,j}(N),                                \tag{4.2}
$$



and the $P_{ab,i,j}$ are fixed rational polynomials of degree at most
$d$.  One common integer, fixed with the construction and independent
of $N,p$, is first used to clear every coefficient denominator.  This
only multiplies (4.1) by a fixed power.  At primes dividing that fixed
integer it changes valuations by a construction-dependent constant and
does not encode singleton depth.

Equations (3.5)–(3.6) give



$$
H_{ab}=A_{ab}(N)F+B_{ab}(N)G,\qquad
A_{ab},B_{ab}\in\mathbb Z[N],                            \tag{4.3}
$$



with degrees at most $d+L+J$.  Multilinearity of the determinant now
proves the homogeneous expansion (1.5) and degree bound (1.6).  In
particular,



$$
C_0(N)=\det(B_{ab}(N)).                                  \tag{4.4}
$$



Let $k$ be the least index with $C_k\not\equiv0$.  Then



$$
\mathscr D_N
=q_N^k\left(C_k(N)q_{N+1}^{s-k}+q_NR_N\right),
\qquad R_N\in\mathbb Z.                                 \tag{4.5}
$$



A nonzero polynomial $C_k$ has only finitely many positive integer
roots.  For every other $N$, its fixed degree and height give



$$
\log|C_k(N)|=O_{\mathscr D}(\log N).                    \tag{4.6}
$$



If $p^a\mid q_N$, $p\nmid q_{N+1}$, and
$a>v_p(C_k(N))$, the two terms in the parentheses of (4.5) have
different valuations.  Therefore no cancellation is possible and (1.7)
follows.

This proves the two branches precisely.

* If $k=0$, then for deep enough singleton exponent the determinant's
  valuation is only the fixed-polynomial value $v_p(C_0(N))$.  It is
  $O_{\mathscr D}(\log N/\log p)$ and is blind to $a$.
* If $k\ge1$, the determinant sees $a$ only because it contains the
  formal factor $q_N^k$.  If $\mathscr D_N\ne0$, equation (1.8)
  follows.  An archimedean divisibility argument therefore returns the
  existing $N\log N$ height scale, not (1.3).

If every $C_k$ is zero, the determinant vanishes identically and gives
no height inequality.  If the relevant $C_k(N)$ vanishes at one of its
finitely many integer roots, the effective first index increases at that
one $N$; these finitely many indices can be checked separately and
cannot yield an asymptotic all-index theorem.

This theorem covers ordinary fixed-length Wronskians: their rows or
columns are fixed jets and fixed shifts, so they are instances of
(4.1)–(4.2).

## 5. The exponential Padé Wronskian is maximally blind

Write



$$
Q_N(x)=\sum_{k=0}^N(-1)^k
\frac{(2N-k)!}{k!(N-k)!}x^k,\qquad
P_N(x)=Q_N(-x).                                          \tag{5.1}
$$



Then $q_N=Q_N(1)$, and the diagonal exponential Padé identity gives



$$
\boxed{
P_N'Q_N-P_NQ_N'-P_NQ_N=(-1)^{N+1}x^{2N}.}              \tag{5.2}
$$



At $x=1$, reduction modulo the full integer $q_N$ yields



$$
\boxed{P_N(1)Q_N'(1)\equiv(-1)^N\pmod{q_N}.}           \tag{5.3}
$$



Thus both factors on the left are units at every prime divisor of
$q_N$, for every exponent.  The Wronskian is exactly in the residual
unit branch of Section 4.

If $a=v_p(q_N)>0$, the unique argument root
$\xi_{N,p}\in1+p\mathbb Z_p$ satisfies



$$
v_p(1-\xi_{N,p})=a.                                     \tag{5.4}
$$



The Wronskian proves simplicity of $\xi_{N,p}$; it does not bound its
distance from the distinguished integer $1$.  The exact resultant is



$$
\operatorname{Res}_x(x-1,Q_N(x))=q_N,                  \tag{5.5}
$$



and the coefficient height is



$$
H(Q_N)=\frac{(2N)!}{N!},\qquad
\log H(Q_N)=N\log N+O(N).                              \tag{5.6}
$$



So the argument-root Padé route also pays the full forbidden scale.

## 6. Exact de-overlap with the clearing reservoir

Retain Item 265's normalized clearing divisor



$$
D_m=\frac{K_m^{(0)}}{\gcd(K_m^{(0)},c_m)},\qquad
\overline q_{m,N}=\frac{q_N}{\gcd(q_N,D_m)},             \tag{6.1}
$$



and its matching quotient



$$
J_{m,N}\mid\overline q_{m,N}^{\,2}.                     \tag{6.2}
$$



Suppose the determinant is in the forced branch



$$
\mathscr D_N=q_N^kE_N,\qquad E_N\in\mathbb Z,
\qquad \mathscr D_N\ne0.                               \tag{6.3}
$$



Define the correctly de-overlapped auxiliary



$$
\overline{\mathscr D}_{m,N}
=\frac{\mathscr D_N}
{\gcd(\mathscr D_N,D_m^k)}.                             \tag{6.4}
$$



Prime by prime, if $t=v_p(q_N)$, $r=v_p(D_m)$, and
$e=v_p(E_N)$, then



$$
v_p(\overline{\mathscr D})
=kt+e-\min(kt+e,kr)\ge k(t-r)_+.                        \tag{6.5}
$$



Therefore



$$
\boxed{
\overline q_{m,N}^{\,k}\mid
\overline{\mathscr D}_{m,N}.}                           \tag{6.6}
$$



The fixed determinant does not create fresh capacity after reservoir
overlap is removed: it still contains the same unbounded beta factor.
For $k=0$ it was already blind.  Equation (6.6) is why the forced
factor may not be booked again on top of the optimistic two-copy
reservoir.

## 7. Actual singleton and the smallest missing global input

Assume a matching-range prime power is supported at only one block index
$N$.  Then in particular



$$
p^a\mid q_N,\qquad p\nmid q_{N+1}.                       \tag{7.1}
$$



The fixed-window reduction uses only the unimodular boundary pair
$(q_N,q_{N+1})$.  Pairwise overlaps, neighboring Wronskians, argument
derivatives, and every admissible fixed determinant therefore fall under
Sections 4–5.  Increasing the singleton exponent changes none of their
unit minors.  This is an exact local-algebra blind spot, not a finite
nonoccurrence claim.

The canonical $p$-adic index interpolation makes the missing input
equally explicit.  On an ordinary root disk,



$$
v_p(q_N)=v_p(N-\rho_{p,r}).                              \tag{7.2}
$$



A successful continuation must therefore supply at least one genuinely
global ingredient, for example:

1. a uniform rational-integer approximation theorem for the specific
   zeros $\rho_{p,r}$;
2. a growing-length auxiliary whose residual coefficient is not a fixed
   polynomial in $N$, whose nonzero archimedean height is $O(N)$, and
   whose $p$-adic order reaches $v_p(q_N)$; or
3. a direct prime-power height theorem for the seeded sequence, followed
   by the overlap normalization (6.1)–(6.6).

The global initial seed $q_0=q_1=1$, over a length growing with $N$,
must enter essentially.  A fixed local differential or Wronskian module
does not use enough of it to control singleton depth.

## 8. Capacity and strict labels

### PROVED

* The integral jet recursion (2.3) and two-generator reduction (3.5).
* The admissible determinant expansion (1.5), integrality, homogeneity,
  and degree bound (1.6).
* The singleton valuation dichotomy (1.7), including the finite root
  exceptions of the residual polynomial.
* The Padé unit identity (5.3) and the argument-root distinction.
* The exact de-overlap divisibility (6.6).

### EXACT FINITE ONLY

* The portable checker replays bounded polynomial, jet, determinant,
  Padé, and overlap identities.  It does not search for exceptional
  singleton primes and does not extrapolate a valuation distribution.

### OPEN

* The uniform estimate (1.3) or any sufficient little-oh variant.
* A growing-length auxiliary with sub-main height and the required local
  order.
* Uniform approximation of the canonical zeros $\rho_{p,r}$.
* The actual moving correlation with the clearing divisor and transverse
  matching factor.
* Route 1 and every conclusion about $e+\pi$.

### BOOKING



$$
\boxed{\text{new Route-1 rate}=0,\qquad
\text{new beta capacity reduction}=0.}                  \tag{8.1}
$$


