> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Roth's theorem and zero density for the actual fixed-prime determinant

Date: 2026-09-13. Status: auxiliary proof independently reviewed; the
underlying recurrence certificate is also being rechecked directly. This is not a proof of irrationality of
e+pi. It strengthens an averaged upper bound, not a divisor lower bound.

## 1. Statement and exact archived dependencies

Use the actual ordinary-j=2 rows



$$
p=2r+6s+3,\quad r=e+6n,\quad s=s_0-2n,\quad
0\le n<N_p=\left\lfloor\frac{p-2e+3}{12}\right\rfloor,
$$



where e=1 for p=5 mod6 and e=5 for p=1 mod6. The exact all-row bridge
in Item314 identifies determinant zeros with zeros modulo p of



$$
u_{p,n}=18\,4^{s_0}16^{-n}a_{e+6n}+11b_{e+6n}.
\tag{1}
$$



The branch coefficients are p-integral because Item314 clears them by
6^{r+3}r!, a p-unit on every actual row. Item309 Section6 proves that
both sequences in (1) obey the same Item237 order-three recurrence



$$
\sum_{j=0}^3P_j(h)u_{p,n+j}=0,\qquad h=e/2+3n,
\tag{2}
$$



whenever the indices involved are actual. Each P_j has degree16. These
are archived all-index identities, not recurrences fitted in this session.

The preceding session proof `fixed_prime_stepanov_attempt.md`, reviewed in
`fixed_prime_stepanov_review.md`, also proves that the state
(u_{p,n},u_{p,n+1},u_{p,n+2}) can be zero at at most five actual starting
indices, outside a fixed finite prime set. This follows from its reverse
desingularization and nonzero initial branch minors. It is the only
nonzero-state input below.

**Proposed theorem.** With



$$
Z(p)=\#\{0\le n<N_p:u_{p,n}=0\pmod p\},
$$



one has Z(p)=o(p) as p tends to infinity through the primes. More precisely,
using the quantitative progression theorem specified below,
there exists c>0 such that, for all sufficiently large primes,



$$
Z(p)\ll p\exp\left(-c(\log\log p)^{1/9}\right).
\tag{3}
$$



The implicit constants depend only on the fixed recurrence. They do not
depend on the prime-dependent initial linear combination in (1).

## 2. The limiting cubic is nondegenerate

Reading the leading coefficients from Item237's exact factorizations and
normalizing by the leading coefficient of P_3 gives, in order j=0,1,2,3,



$$
-\frac{64}{531441},\quad-\frac{9856}{19683},\quad
-\frac{413233}{729},\quad1.
$$



Thus the constant limiting companion matrix has characteristic polynomial
proportional to



$$
f(X)=531441X^3-301246857X^2-266112X-64.
\tag{4}
$$



This polynomial is irreducible over Q. Its values at 0,1,...,6 modulo7
are respectively 6,5,6,1,3,4,3, with nonzero leading coefficient modulo7.
A cubic with no root over that field is irreducible, which proves the
characteristic-zero assertion by reduction.

Its discriminant, computed by the exact cubic formula, is



$$
\mathscr D=-572058527163885303300000000<0.
\tag{5}
$$



Neither -D nor -D/3 is a square in Q (both are integers; the enclosed
integer-square check is exact). Hence the splitting field K has Galois
group S_3 and its unique quadratic subfield is neither Q(i) nor
Q(sqrt(-3)). Every cyclotomic subfield of K is abelian and therefore
lies in its maximal abelian subextension, that quadratic field. The
only roots of unity in K are consequently 1 and -1: any root of unity
of degree at most two other than these generates Q(i) or Q(sqrt(-3)).

Let lambda_1,lambda_2,lambda_3 be the distinct nonzero roots of f.
A ratio lambda_i/lambda_j which is a root of unity belongs to K and
must be ±1. The value +1 is excluded by distinctness. To exclude -1,
write the monic cubic as X^3-A X^2-B X-C, with A,B,C>0. If two roots
were lambda,-lambda, the third would be A. Factoring would give the
constant term A lambda^2; its X coefficient forces lambda^2=B, so
AB=-C, impossible. Thus



$$
\lambda_i^d\ne\lambda_j^d
\quad(i\ne j,\ d\ge1).
\tag{6}
$$



This is an all-d algebraic proof. A finite check of step sizes does not
replace it.

## 3. Every fixed-spacing observation determinant is nonzero

Define the column state S_n=(u_n,u_{n+1},u_{n+2})^t. Away from zeros
of P_3, equation(2) gives S_(n+1)=T(h)S_n, where



$$
T(h)=\begin{pmatrix}
0&1&0\\0&0&1\\-P_0/P_3&-P_1/P_3&-P_2/P_3
\end{pmatrix}.
$$



For k>=0, put



$$
T_k(h)=T(h+3(k-1))\cdots T(h),\qquad T_0=I,
$$



and let e_1=(1,0,0) be a row vector. For each d>=1, define



$$
F_d(h)=\det\begin{pmatrix}e_1\\e_1T_d(h)\\e_1T_{2d}(h)\end{pmatrix}.
\tag{7}
$$



This is a rational function in h over Q, independent of p and the
initial state. Since all P_j have the same degree, T(h) tends as
h tends to positive real infinity to the constant companion matrix C.
For fixed d, T_k(h)->C^k. The columns
(1,lambda_j,lambda_j^2)^t are eigenvectors of C. Multiplication by
their Vandermonde matrix therefore gives



$$
\lim_{h\to\infty}F_d(h)
=\frac{\det(\lambda_j^{id})_{0\le i\le2,\,1\le j\le3}}
{\det(\lambda_j^i)_{0\le i\le2,\,1\le j\le3}}\ne0
\tag{8}
$$



by(6). In particular F_d is not identically zero for every d. The real
limit is used solely to establish that rational-function identity; it
does not assert that h modulo p is close to a real limiting matrix.

## 4. Clearing the determinants uniformly

Replace all P_j by a common fixed positive integer multiple so they have
integer coefficients. This leaves T unchanged. Let H be at least one
and at least the sum of absolute coefficients of each P_j. Write



$$
M(h)=P_3(h)T(h),\quad
A_k(h)=M(h+3(k-1))\cdots M(h),\quad
D_k(h)=\prod_{t=0}^{k-1}P_3(h+3t).
$$



Then T_k=A_k/D_k. The integer polynomial



$$
J_d(h)=\det\begin{pmatrix}e_1\\e_1A_d(h)\\e_1A_{2d}(h)\end{pmatrix}
\tag{9}
$$



is nonzero by(8), and F_d=J_d/(D_d D_{2d}). Its degree is at most
16d+32d=48d.

The sum-of-absolute-coefficients norm is submultiplicative. A translate
P_j(h+3t) for 0<=t<2d has norm at most H(6d+1)^16. A matrix product
entry has at most three choices per multiplication, hence



$$
\|J_d\|_1\le2\,[3H(6d+1)^{16}]^{3d}.
\tag{10}
$$



The first row e_1 reduces the determinant to two products, explaining
the factor2. These bounds need not be sharp.

Set



$$
K_p=\left\lfloor\frac{\log p}{100\log\log p}\right\rfloor.
\tag{11}
$$



For all sufficiently large p and every 1<=d<=K_p, (10) gives
log||J_d||_1 <=(48/100+o(1))log p<log p. Since J_d is a nonzero
integer polynomial, at least one of its nonzero coefficients has absolute
value less than p; indeed they all do. Thus J_d does not become the zero
polynomial modulo p. Exclude the fixed finite prime divisors of P_3's
leading coefficient. Then D_(2d) is also nonzero modulo p, and it has
degree32d.

All these polynomials are evaluated at h=e/2+3n. For p>3 this affine
map is injective on the actual n interval, whose length is less than p.
They therefore vanish at at most 48d and 32d actual starting indices,
respectively.

## 5. Short zero progressions are few

Suppose u_n=u_(n+d)=u_(n+2d)=0 and all three indices are actual.
If D_(2d)(h) is nonzero modulo p, every transfer needed in(7) is legal
and all intermediate sequence values are p-integral. If in addition
J_d(h) is nonzero, the three observations force S_n=0. There are at
most five such zero-state starting indices by the preceding bounded-run
theorem. Hence, for 1<=d<=K_p, the number of three-zero progressions
of spacing d is at most



$$
48d+32d+5=80d+5.
\tag{12}
$$



Some transfer steps go two places farther than the last observation if
one insists on the full state T_(2d)S_n. Remove the last two possible
starting positions for which n+2d+2>=N_p, or equivalently add at most
two to(12). This harmless boundary correction ensures every intermediate
state used in the product lies in the actual p-integral range. Below
we use the safe bound 80d+7.

Let A_p be the set of zero indices. Remove from it the starting index
of every zero progression with 1<=d<=K_p. At most



$$
\sum_{d=1}^{K_p}(80d+7)=40K_p(K_p+1)+7K_p
\tag{13}
$$



indices are removed. The resulting A'_p has no three-term arithmetic
progression with spacing at most K_p. Partition [0,N_p) into consecutive
blocks of length K_p and one shorter final block. Every full block's
intersection with A'_p is progression-free. Thus, with r_3(K) the largest
progression-free subset of [1,K],



$$
Z(p)\le\frac{N_p}{K_p}r_3(K_p)+K_p
+40K_p(K_p+1)+7K_p.
\tag{14}
$$



Roth's theorem states r_3(K)=o(K). Since K_p->infinity and K_p^2=o(p),
equation(14) proves Z(p)=o(p). Alternatively, without any coefficient
height estimate, hold K fixed, exclude its finite exceptional prime set,
take p->infinity, then K->infinity. That separate order of limits proves
the same qualitative statement.

For(3), apply the stronger bound
r_3(K)<=K exp(-c(log K)^(1/9)). Since log K_p~log log p and the
polynomial-logarithmic error in(14) is smaller, (3) follows.

The primary source used for this quantitative input is Thomas F. Bloom
and Olof Sisask, [An improvement to the Kelley–Meka bounds on three-term
arithmetic progressions](https://arxiv.org/pdf/2309.02353), Theorem1,
September2023, PDF p.1. The qualitative result is K. F. Roth,
[On Certain Sets of Integers](https://doi.org/10.1112/jlms/s1-28.1.104),
1953, pp.104–109. This is Roth's progression theorem, not Roth's
Diophantine approximation theorem. The cited theorem statement was
checked; its full proof is an imported established result, not a newly
proved ingredient here.

## 6. Consequence for the original construction index

The actual fixed-p map is M=(7p+e)/6+n. Let W(M) be the sum of log p
over actual ordinary-j=2 collision primes. A collision implies determinant
vanishing on every chart, so



$$
\sum_{X<M\le2X}W(M)
\le\sum_{p\le12X/7+O(1)}Z(p)\log p=o(X^2).
\tag{15}
$$



For the last step, given epsilon>0, bound Z(p)<=epsilon p beyond its
fixed threshold, and use sum_(p<=Y)p log p=O(Y^2), a consequence of
Chebyshev's bound. The finitely many small primes contribute a fixed
finite amount. No independence across primes is required.

Therefore the normalized dyadic **average** upper cap for this component
is zero. Also, for every epsilon>0, all but o(X) indices M in(X,2X]
satisfy W(M)<=epsilon M, by Markov's inequality. A standard diagonal
choice supplies a density-one set along which W(M)=o(M).

This does not establish W(M)=o(M) at every M. It does not control a
sparse subsequence on which a gain could be unusually large. It supplies
no positive rate for the content/matching gain Gamma and does not alter
the booked lower rate. These distinctions are essential to the main
research objective.

## 7. Relation to previous archive results

An archive text search found no use of Roth/Szemeredi/Varnavides for this
actual sequence. Item351 already excludes three consecutive zeros of a
different, locally indexed sequence. Items349/359/382 correctly reject
using recurrence existence alone to control a changing-prime selector.
The present argument adds all fixed-spacing observation determinants,
proves their nonvanishing for every spacing, uses a dense-set theorem,
and takes an average over the original index. It does not contradict
those scoped pointwise limitations.

The actual inputs still need their stated verification: recurrence,
second branch, all-row integral bridge, and nonzero-state theorem. No
empirical collision scan, numerical eigenvalue ratio, or generic
randomness assumption is used in the proposed proof.
