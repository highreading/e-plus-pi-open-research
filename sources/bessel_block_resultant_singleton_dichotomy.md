> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Bessel blocks: unit transition minors and the singleton-resultant dichotomy

Date: 2026-08-27.

## 1. Scope and conclusion

Let



$$
q_0=q_1=1,
\qquad q_n=(4n-2)q_{n-1}+q_{n-2}\quad(n\ge2)              \tag{1}
$$



be the primitive exponential beta coefficient.  The unresolved high tail
in the critical-Fourier matching problem is governed by the largest
prime-power valuation attained in a block
$q_N,\ldots,q_{2N-1}$.  This note tests whether a block determinant,
resultant, discriminant, or subresultant can aggregate those singleton
maxima cheaply.

The outcome is an exact dichotomy.

1.  The rank-two transition matrix has adjacent minors equal to units.
    Its Smith determinantal divisor is therefore one.  These transition
    invariants detect simultaneous zeros but are blind to a prime power
    dividing only one member of the block.
2.  The first standard invariant which necessarily sees every singleton
    is the product $\prod q_n$, equivalently a resultant.  It already has
    logarithmic size

    

$$
\left({3\over2}+o(1)\right)N^2\log N.                 \tag{2}
$$



    Integral interpolation adds another $N^2\log N$ rather than saving
    anything.
3.  Discriminants see collisions, not isolated zero depth, and are even
    larger.  For a prime $p>N$ occurring at exactly one grid value, the
    resultant records its full depth, whereas the first nonzero
    subresultant is already a $p$-unit.  Descending the subresultant chain
    therefore discards precisely the singleton information being sought.

The surviving object is the smooth part of the largest Smith invariant,
after removal of the known threshold.  The identities below isolate it
exactly, but do not bound it.  Thus this is a rigorous no-go for the
standard block-resultant shortcut, not a proof about $e+\pi$.

## 2. Exact rank-two transition and Cassini identity

Define the continuants



$$
P_0(X)=0,qquad P_1(X)=1,qquad
P_{j+2}(X)=(4X+4j+6)P_{j+1}(X)+P_j(X).                   \tag{3}
$$



The recurrence gives



$$
q_{N+d}=P_d(N)q_{N+1}+P_{d-1}(N+1)q_N.                  \tag{4}
$$



Put



$$
A_t=\begin{pmatrix}4t+6&1\\1&0\end{pmatrix},
\qquad M_d(N)=A_{N+d-1}\cdots A_N.                       \tag{5}
$$



Direct induction using (3) yields



$$
\boxed{
M_d(N)=
\begin{pmatrix}
P_{d+1}(N)&P_d(N+1)\\
P_d(N)&P_{d-1}(N+1)
\end{pmatrix}.}                                          \tag{6}
$$



Since $\det A_t=-1$,



$$
\boxed{
P_{d+1}(N)P_{d-1}(N+1)-P_d(N)P_d(N+1)=(-1)^d.}           \tag{7}
$$



For row vectors



$$
r_0=(0,1),\qquad
r_d=(P_d(N),P_{d-1}(N+1))\quad(d\ge1),                  \tag{8}
$$



one has $q_{N+d}=r_d(q_{N+1},q_N)^t$.  More generally, if
$e>d$, the addition formula for continuants gives



$$
r_e=P_{e-d}(N+d)r_{d+1}
   +P_{e-d-1}(N+d+1)r_d,
$$



and therefore



$$
\boxed{\det(r_e,r_d)=(-1)^dP_{e-d}(N+d).}                \tag{9}
$$



In particular every adjacent row minor is $\pm1$.  The rank-two
determinantal divisor of the complete transition matrix is one.  No prime
power dividing a single output can be charged to this transition lattice;
only simultaneous output conditions enter its nontrivial minors.  This is
the exact rank-two source of the familiar gap polynomial.

## 3. The largest Smith invariant and the exact smooth quotient

Let



$$
D_N=\operatorname {diag}(q_N,\ldots,q_{2N-1}),
\qquad Q_N=\prod_{n=N}^{2N-1}q_n,                         \tag{10}
$$



and let $\Delta_j(D_N)$ denote the gcd of the $j$-rowed minors.
Then



$$
\Delta_N(D_N)=Q_N,
\qquad
\Delta_{N-1}(D_N)=gcd_n{Q_N\over q_n}.                  \tag{11}
$$



Prime by prime, subtracting the sum of all valuations except their maximum
shows that



$$
\boxed{
L_N:=\operatorname {lcm}(q_N,\ldots,q_{2N-1})
={\Delta_N(D_N)\over\Delta_{N-1}(D_N)}.}                 \tag{12}
$$



For a cutoff $X$, let $L_N^{(X)}$ be the $X$-smooth part of
$L_N$.  If $b_p(N)$ is the accepted threshold exponent, set



$$
\Lambda_{N,X}=\operatorname {lcm}(1,\ldots,N)
               \prod_{N<p\le X}p.                       \tag{13}
$$



Thus $v_p(\Lambda_{N,X})=b_p(N)-1$ for $p\le X$.  The
thresholded smooth largest invariant is exactly



$$
\boxed{
T_{N,X}
={L_N^{(X)}\over\gcd(L_N^{(X)},\Lambda_{N,X})}
=\prod_{p\le X}
p^{(\max_{N\le n<2N}v_p(q_n)-b_p(N)+1)_+}.}              \tag{14}
$$



Consequently the high singleton sum $S(N,X)$ in the earlier Bessel
decomposition is exactly



$$
\boxed{S(N,X)=\log T_{N,X}.}                              \tag{15}
$$



For $X\le C N\log N$, the threshold itself has only



$$
\log\Lambda_{N,X}
=\psi(N)+\vartheta(X)-\vartheta(N)=O(N\log N),            \tag{16}
$$



which is $o(N^2\log N)$.  Removing the known threshold is therefore
cheap, but (14) shows that the remaining problem is literally the smooth
part of the largest Smith invariant; no transition determinant bounds it.

## 4. The first singleton-sensitive resultant is main-scale

Let $I_N(x)$ be the unique polynomial of degree below $N$ satisfying



$$
I_N(j)=q_{N+j}\qquad(0\le j<N),                           \tag{17}
$$



and put



$$
F_N(x)=(N-1)!I_N(x),qquad
B_N(x)=\prod_{j=0}^{N-1}(x-j).                            \tag{18}
$$



The Newton interpolation formula shows that $F_N\in\mathbb Z[x]$: the
coefficient of $\binom{x}{r}$ is the integer finite difference
$\Delta^r q_N$, while $(N-1)!/r!$ clears every falling factorial
through $r<N$.  Evaluation of a resultant at the roots of $B_N$
gives the exact identity



$$
\boxed{
|\operatorname {Res}(B_N,F_N)|
=((N-1)!)^N\prod_{n=N}^{2N-1}q_n.}                       \tag{19}
$$



There is also an unpolluted product resultant.  With



$$
G_N(Y)=\prod_{n=N}^{2N-1}(Y-q_n),                         \tag{20}
$$



one has



$$
\boxed{|\operatorname {Res}_Y(Y,G_N(Y))|=Q_N.}           \tag{21}
$$



The elementary recurrence bounds



$$
\prod_{j=2}^n(4j-2)\le q_n<\prod_{j=2}^n4j              \tag{22}
$$



imply



$$
\log q_n=n\log n+O(n).                                   \tag{23}
$$



Summing (23) on the block gives



$$
\boxed{
\log Q_N={3\over2}N^2\log N+O(N^2),}                    \tag{24}
$$



whereas Stirling's formula in (19) gives



$$
\boxed{
\log|\operatorname {Res}(B_N,F_N)|
={5\over2}N^2\log N+O(N^2).}                            \tag{25}
$$



Thus the first standard invariant which necessarily records every
singleton depth is already at the full product scale.

## 5. Why discriminants and subresultants do not escape

The grid discriminant is



$$
|\operatorname {Disc}(B_N)|
=\prod_{j=1}^{N-1}(j!)^2,
\qquad
\log|\operatorname {Disc}(B_N)|
=N^2\log N+O(N^2).                                       \tag{26}
$$



It brings factorial contamination before seeing any $q_n$.  The rapid
growth $q_m\ge6q_{m-1}$ also gives



$$
\log|\operatorname {Disc}(G_N)|
={5\over3}N^3\log N+O(N^3),                              \tag{27}
$$



so the value discriminant is worse.

More decisively, discriminants encode collisions.  Suppose a prime
$p$ divides exactly one member $q_s$ of the block.  Modulo $p$,



$$
G_N'(0)\equiv(-1)^{N-1}\prod_{m\ne s}q_m\not\equiv0
\pmod p.                                                  \tag{28}
$$



The displayed relation is a congruence, not an integer equality: all other
summands in the exact derivative contain $q_s$.  Thus the singleton zero
is simple and contributes nothing to the discriminant modulo $p$.

If in addition $p>N$, the grid polynomial $B_N$ is squarefree modulo
$p$.  When exactly one value $q_{N+j}$ vanishes, the gcd of
$B_N,F_N$ modulo $p$ has degree exactly one.  Hence the resultant has



$$
v_p\operatorname {Res}(B_N,F_N)
=v_p(q_{N+j}),                                            \tag{29}
$$



because the interpolation clearing is a $p$-unit, while the first
nonzero degree-one subresultant is a $p$-unit.  Retaining the resultant
pays the full singleton depth; descending to the first nonzero
subresultant erases it.  For $p\le N$, (26) adds rather than removes
factorial valuation.

Therefore standard determinants and subresultants offer no intermediate
invariant which both sees every isolated maximum and has a proved
sub-main-scale size.  A successful aggregate theorem must estimate
$T_{N,X}$ in (14) directly, using the arithmetic of the recurrence and
its lift trees.

## 6. Exact central reflection is tautological

There is one especially natural reflection value which at first appears to
offer a new divisor bound.  It instead factors into the two primitive
solutions of the same recurrence.  Define



$$
p_0=1,\quad p_1=3,\qquad
 p_n=(4n-2)p_{n-1}+p_{n-2},                              \tag{30}
$$



and retain the sequence $q_n$ from (1).  Put



$$
C(t)=\begin{pmatrix}t&1\\1&0\end{pmatrix},\qquad
 a_k=4k-2,\qquad
 U_n=C(a_n)C(a_{n-1})\cdots C(a_1),
 \qquad D=\operatorname {diag}(1,-1).
$$



The $2n$ transition coefficients in $P_{2n+1}(-n-1)$, in product
order, are $a_n,\ldots,a_1,-a_1,\ldots,-a_n$.  Since



$$
C(-t)=-DC(t)D,\qquad C(t)^t=C(t),
$$



their product is



$$
C(a_n)\cdots C(a_1)C(-a_1)\cdots C(-a_n)
   =(-1)^nU_nDU_n^tD.                                   \tag{31}
$$



If the first row of $U_n$ is $(A_n,B_n)$, multiplication by
$(1,1)^t$ and $(1,-1)^t$ gives



$$
A_n+B_n=p_n,\qquad A_n-B_n=q_n.
$$



Taking the upper-left entry in (31) therefore proves the exact
factorization



$$
\boxed{P_{2n+1}(-n-1)=(-1)^n(A_n^2-B_n^2)
                         =(-1)^np_nq_n.}                 \tag{32}
$$



The Wronskian identity



$$
p_nq_{n-1}-p_{n-1}q_n=2(-1)^{n-1}                      \tag{33}
$$



follows immediately from the determinant of the transition product.
Both sequences are odd, so (33) implies $\gcd(p_n,q_n)=1$.  Thus



$$
v_\ell(P_{2n+1}(-n-1))=v_\ell(p_n)+v_\ell(q_n)
$$



for every odd prime $\ell$.  In particular, on the primes supported by
$q_n$, coprimality gives



$$
v_\ell(P_{2n+1}(-n-1))=v_\ell(q_n).
$$



Thus the most symmetric reflection modulus reproduces the unknown prime
power of $q_n$ exactly; it does not upper-bound it by a cheaper external
integer.

## 7. A sharp sufficient prime-power-height lemma

For fixed $C>0$, define



$$
V_N(C)=\max\{v_p(q_n)\log p:
        N\le n<2N,\ p\le C N\log N,\ p\text{ odd prime}\}. \tag{34}
$$



Since every summand in (15) is at most $V_N(C)$, while
$\pi(CN\log N)=O_C(N)$, one has the rigorous bound



$$
\boxed{S(N,CN\log N)\le \pi(CN\log N)V_N(C)
                         =O_C(N)V_N(C).}                 \tag{35}
$$



Consequently



$$
V_N(C)=o(N\log N)
 \quad\Longrightarrow\quad
 S(N,CN\log N)=o(N^2\log N).
$$



In particular, a uniform polynomial prime-power-height estimate



$$
p^{v_p(q_n)}\le (2N)^A
$$



for all primes and indices occurring in (34) would give
$S(N,CN\log N)=O_{A,C}(N\log N)$.  This is the precise missing
statement: a lower bound for the largest prime factor is insufficient;
one needs an upper bound for every relevant prime-power divisor.

The need is not merely formal.  For $p=11$, the compatible zero classes
of $q_n$ modulo successive powers can be represented by



$$
6\pmod {11},\quad 28\pmod {11^2},\quad 28\pmod {11^3},
 \quad1359\pmod {11^4},\quad1359\pmod {11^5}.
$$



In particular, $v_{11}(q_{1359})=5$.  The index $1359$ belongs to the
block $[680,1360)$, where $b_{11}(680)=3$, so this one entry has excess
depth $5-3+1=3$.  This exact finite example demonstrates that lift depth
can genuinely exceed the accepted threshold; it is not evidence for or
against an asymptotic bound such as (35).

## 8. Diagnostic boundary

Exact checks of (6)--(9), (19), and (26) were made for the indicated small
blocks during the audit.  Direct gcd-only calculations gave



$$
{\log\operatorname {lcm}(q_N,\ldots,q_{2N-1})\over
 \log\prod_{n=N}^{2N-1}q_n}
=0.990945,0.996565,0.997972,0.998865                     \tag{36}
$$



at $N=40,80,160,320$, respectively.  These figures are finite
diagnostics only.  In particular they do not bound the
$X$-smooth part: large unique primes can dominate the unrestricted
product.  The proved content of this note is (6)--(29), not an
extrapolation from (30).
