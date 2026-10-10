> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Unequal-degree endpoint-matched Hermite–Padé continuation

Date: 2026-09-13. This note proves an all-degree obstruction for a previously
open boundary allocation and an exact small-degree projection lemma. Neither
statement decides the arithmetic nature of e+pi. Finite profiles are explicitly
separated from the proofs.

## Outcome and scope

For the original Möbius pullback



$$
F(z)=4\arctan\frac{z}{2-z},\quad D(z)=z^2-2z+2,
 \quad F'=4/D,\quad F(1)=\pi,
$$



consider independent coefficients satisfying



$$
R=A+B e^z+C F=O(z^{a+b+c+1}),\qquad B(1)=C(1),
 \quad \deg A\le a,\ \deg B\le b,\ \deg C\le c.
\tag{1}
$$



The new results are:

* For every n>=1, allocation (a,b,c)=(n,0,n) has exactly one projective
  solution. With B=1 its normalized remainder is a logarithmic Padé error
  plus a factorially small perturbation. After *complete endpoint gcd
  reduction*, its integer form L_n has a nonzero coefficient pair, is
  nonzero in value for all sufficiently large n, and satisfies
  
  

$$
\liminf_{n\to\infty}\frac{\log|L_n|}{n\log n}\ge\frac12.
  \tag{2}
$$


  Thus this entire boundary family eventually grows in absolute value.

* For (a,b,c)=(n,b,n), 1<=b<=n, the high equations reduce exactly to a
  b-row system in the b+1 coefficients of B. A Legendre projection gives
  
  

$$
\frac{\max_j|B_j|}{|B(1)|}
  \ge \frac{(n+1-b)!}{(b+1)(n+1)^2 64^{n+1}}
  \quad\text{if }B(1)\ne0.
  \tag{3}
$$


  For b=round(n/log n), the logarithm of this ratio is at least
  n log n-O(n). This is coefficient amplification relative to the
  endpoint, not a lower bound on a primitive endpoint denominator.

* The polynomial Wronskian numerator still has a cubic factor after its
  forced zero at zero for every allocation (n,b,n). Its degree and
  multiplicity bounds do not deteriorate when b is made small.

The first statement is an actual new all-index theorem for this family.
The second is an exact reduction with a proved norm bound; it leaves the
small-positive-b arithmetic problem open.

## Archive check: which failed routes are being avoided

Reviewed Items176,179,182,184; the existing endpoint/height continuation;
`high_radius_composed_integral_jet_pullback.md`;
`high_radius_composed_nondiagonal_endpoint_scan.md`; and the Machin endpoint
asymptotic note. Item176 treats A constant and B=C as the same polynomial.
The composed-family constant-coefficient theorem treats (a,0,0). The
Machin theorem treats a different logarithmic function and essentially
(N-1,1,1). None is the independent (n,0,n) family proved here.

This work does not revisit the already defeated fixed C=D^n, constant-A
softened-singularity family. The composed function
G=F(z+(z^7-z^8)/140) has a better radius, but the simple vertical-segment
moment representation used below is specific to F. The new Legendre
arguments cannot be transferred to G merely from its improved radius.

## 1. Exact linear system and the arithmetic ledger

Write M=a+b+c+1, B=sum B_j z^j, C=sum C_j z^j, and
tau_k=F^(k)(0). The archive's explicit integer jets are



$$
\tau_0=0,\qquad
 \tau_k=4(k-1)!2^{-k/2}\sin(k\pi/4)\in\mathbb Z\quad(k\ge1).
$$



The remaining rows after reconstructing A are



$$
\sum_{j=0}^{b} k^{\underline j}B_j+
 \sum_{j=0}^{c} k^{\underline j}\tau_{k-j}C_j=0,
 \quad k=a+1,\ldots,M-1,
\tag{4}
$$



with a term j>k defined to be zero, followed by
sum B_j=sum C_j. This is an integer (b+c+1)-by-(b+c+2) matrix.
For k=0,...,a, the coefficient of A is the negative of the corresponding
ordinary Taylor coefficient of Be^z+CF. Rank counting alone does not prove
that the kernel has dimension one.

For any rational solution with Y=B(1)=C(1) nonzero, put x=A(1)/Y.
Writing x=p/q in lowest terms, q>0, the final primitive endpoint form is



$$
L=p+q(e+\pi)=q\,R(1)/Y.
\tag{5}
$$



This formula includes denominator clearing, full polynomial content, and
the separate endpoint-pair gcd. Any arbitrary scaling of the full triple
cancels from (5). If Y=0, the endpoint is rational and is irrelevant to
irrationality by this construction; no argument below divides by Y in
that case.

## 2. General Wronskian bounds

Define B_1=B'+B, B_2=B''+2B'+B and K=B C'-(B'+B)C. As checked in
`endpoint_hp_continuation.md` and its independent root review,



$$
N=D^2e^{-z}W(R,Be^z,C)
 =D^2\det\begin{pmatrix}A&B&C\\A'&B_1&C'\\A''&B_2&C''\end{pmatrix}
 +4D[-C(BC''-B_2C)+2C'K]-4D'CK.
\tag{6}
$$



The derivation subtracts **both** the Be^z column and F times the C column
from the first Wronskian column. When B,C are nonzero, logarithmic
monodromy and the fact that e^z is not rational imply N is a nonzero
polynomial. For arbitrary caps a,b,c,



$$
\deg N\le \max(a+b+c+3,\ b+2c+2),
 \quad \operatorname{ord}_0R\le\max(a+b+c+5,\ b+2c+4).
\tag{7}
$$



Indeed the polynomial determinant in (6) can be written as the ordinary
polynomial Wronskian plus
B(AC''-A''C)-(2B'+B)(AC'-A'C). Its degree is at most a+b+c-1.
Multiplication by D^2 adds four. The other terms have degree at most
b+2c+2. Finally ord_0 N>=ord_0 R-2.

If a=c=n, the leading equal-degree terms in AC'-A'C cancel, so its degree
is at most 2n-2 and that of its derivative is at most 2n-3. Consequently



$$
\deg N\le2n+b+2=M+1,\qquad \operatorname{ord}_0R\le M+3.
\tag{8}
$$



For a solution of (1), therefore



$$
N=z^{M-2}Q,\qquad \deg Q\le3.
\tag{9}
$$



All nonzero matched solutions with a=c=n>=1 and b>=0 have B,C nonzero.
If B=0, the first n logarithmic moment equations below force C^* to be a
multiple of p_n, and the endpoint condition forces that multiple to be
zero. If C=0, a nonzero A+Be^z has order at most n+b+1: differentiating
n+1 times leaves e^z times a nonzero polynomial of degree at most b.
This is smaller than M. The bound (8) also implies that the matched
solution space has dimension at most four, by imposing four further
Taylor vanishing conditions. This does not prove normality for b>=1.

## 3. Exact complex moment representation

Put t=(1+iu)/2 and introduce the complex bilinear moment functional



$$
\mathcal L(P)=\int_{-1}^1 P((1+iu)/2)\,du.
$$



Direct integration, or equality of Taylor coefficients, gives



$$
F(z)=z\int_{-1}^1\frac{du}{1-(1+iu)z/2}.
\tag{10}
$$



In particular [z^k]F=\mathcal L(t^{k-1}) for k>=1. For a=c=n and
0<=b<=n, reverse C by C^*(t)=t^n C(1/t). The high equations (4) become



$$
\mathcal L(t^q C^*)=-\ell_{n,B}(t^q),\qquad q=0,\ldots,n+b-1,
\quad
 \ell_{n,B}(t^q)=\sum_{j=0}^{b}\frac{B_j}{(n+q+1-j)!}.
\tag{11}
$$



The endpoint condition becomes C^*(1)=B(1). All factorial arguments in
(11) are positive. For other degree allocations the same simple formula
requires adjusting the power t^(a-c); (11) is deliberately restricted
to a=c=n.

Let P_k be the standard Legendre polynomial and set



$$
p_k(t)=\frac{i^kP_k(-i(2t-1))}{\binom{2k}{k}}.
\tag{12}
$$



These are monic polynomials in Q[t]. Orthogonality on [-1,1] gives



$$
\mathcal L(p_jp_k)=0\ (j\ne k),\qquad
 h_k=\mathcal L(p_k^2)=\frac{2(-1)^k}{(2k+1)\binom{2k}{k}^2}\ne0.
\tag{13}
$$



This is not an appeal to positivity of a complex measure: the nonzero
bilinear norms are explicitly alternating in sign.

The monic recurrence is



$$
p_{k+1}=(t-1/2)p_k+\frac{k^2}{4(4k^2-1)}p_{k-1}.
\tag{14}
$$



It implies the coefficient norm bound ||p_k||_1<=2^k. The explicit
Legendre expansion evaluated at t=1 has only positive summands after
the factor i^k, and its leading summand gives p_k(1)>=2^(-k)>0.
Consequently



$$
\|p_n/p_n(1)\|_1\le4^n,\qquad
 1/|h_k|\le(2k+1)16^k/2.
\tag{15}
$$



## 4. Complete boundary theorem: b=0

First take B=1 and abbreviate ell_n(t^q)=1/(n+q+1)!. The first n equations
in (11) and the nonzero norms (13) imply



$$
C^*=U_n+\kappa p_n,\qquad
 U_n=-\sum_{k=0}^{n-1}\frac{\ell_n(p_k)}{h_k}p_k.
\tag{16}
$$



Since p_n(1)>0, the endpoint equation fixes
kappa=(1-U_n(1))/p_n(1). A solution with B=0 has C^*=kappa p_n and
C^*(1)=0, hence is zero. Therefore this constructs and uniquely
normalizes the projective solution for every n.

Let C_{0,n}^*=p_n/p_n(1), and reverse it to define C_{0,n}(z). Then



$$
C=C_{0,n}+\delta C_n,\qquad
 \delta C_n^*=U_n-U_n(1)C_{0,n}^*.
$$



From (15) and |ell_n(p_k)|<=2^k/(n+1)!,



$$
\|U_n\|_1\le\frac{n^2 64^n}{(n+1)!},\qquad
 \|\delta C_n\|_1\le\frac{e^{O(n)}}{(n+1)!}.
\tag{17}
$$



All constants implicit in O(n) are absolute and independent of n.

### 4.1 A signed Padé error with an exponential lower bound

Write T_n for Taylor truncation through degree n, and put



$$
f_n=[T_n(C_{0,n}F)](1)\in\mathbb Q.
$$



Since C_{0,n}(1)=1, the exact tail identity from (10) and orthogonality
give



$$
\pi-f_n
 =\frac{1}{p_n(1)^2}\mathcal L\!\left(\frac{p_n(t)^2}{1-t}\right)
 =\frac{2(-1)^n}{\binom{2n}{n}^2p_n(1)^2}
       \int_{-1}^1\frac{P_n(u)^2}{1+u^2}\,du.
\tag{18}
$$



For the first equality, the unreduced tail is
L(p_n/(1-t))/p_n(1). Multiplying by p_n(1) and replacing it with p_n(t)
changes the integrand by p_n times a polynomial of degree <=n-1, whose
moment is zero. In the second equality the odd imaginary part integrates
to zero. Thus (18) has the strict sign (-1)^n.

Using the exact Legendre norm 2/(2n+1),



$$
\frac{2}{(2n+1)\binom{2n}{n}^2p_n(1)^2}
 \le|\pi-f_n|\le
 \frac{4}{(2n+1)\binom{2n}{n}^2p_n(1)^2}.
\tag{19}
$$



In particular the lower bound is at least 2/((2n+1)64^n), by (15).
This coarse exponential lower bound suffices for the arithmetic argument.
Also binom(2n,n)>=2^n and p_n(1)>=2^(-n), so f_n remains bounded.

### 4.2 Rational height of the logarithmic approximant

The polynomial



$$
J_n(t)=2^n i^nP_n(-i(2t-1))
 =\sum_{j=0}^{\lfloor n/2\rfloor}
   \binom nj\binom{2n-2j}{n}(2t-1)^{n-2j}
\tag{20}
$$



has integer coefficients of size e^{O(n)}, and J_n(1) is a positive
integer of size e^{O(n)}. We have C_{0,n}^*=J_n/J_n(1). The Taylor
coefficients of F through n have a common denominator dividing
2^n lcm(1,...,n)=e^{O(n)}; this follows as well from
[z^k]F=4 Im((1+i)^k)/(k2^k). Therefore the reduced denominator of f_n
is at most e^{O(n)}. Its numerator has the same bound because f_n is
bounded. This statement concerns rational height, not only real size.

### 4.3 Exponential forcing and complete primitive height

The reconstructed A equals -T_n(e^z+CF). Put E_n=sum_(k=0)^n 1/k!.
Then exactly



$$
r_n:=-A(1)-f_n=E_n+[T_n(\delta C_nF)](1)\in\mathbb Q.
\tag{21}
$$



The sum of absolute Taylor coefficients of F at z=1 is finite. Hence
(17) and the exponential tail yield



$$
0<|e-r_n|\le\frac{e^{O(n)}}{(n+1)!}
 =\exp(-n\log n+O(n)).
\tag{22}
$$



Strict positivity follows from irrationality of e. The same calculation
gives the normalized endpoint remainder



$$
R_n(1)=A(1)+e+\pi=(\pi-f_n)+(e-r_n).
\tag{23}
$$



By (19) and (22), this has sign (-1)^n for all sufficiently large n,
and |R_n(1)|>=exp(-O(n)).

Now let q_n be the reduced denominator of A(1), so the fully primitive
endpoint form is L_n=q_nR_n(1), by (5). The reduced denominator Q_n of
r_n satisfies Q_n<=q_n exp(O(n)), by the proved height bound on f_n.

Euler's continued fraction of e has partial quotients growing only
linearly in their index. Consequently, for each epsilon>0, all rational
p/q with sufficiently large reduced denominator satisfy



$$
|e-p/q|\ge q^{-(2+\epsilon)}.
\tag{24}
$$



For completeness: convergent denominators grow at least as Fibonacci
numbers, while the exact error is greater than
1/((a_(k+1)+2)q_k^2); all nonconvergents satisfy the Legendre bound
|e-p/q|>=1/(2q^2). These imply (24). The expansion itself is proved in
Henry Cohn, *A Short Proof of the Simple Continued Fraction Expansion
of e*, American Mathematical Monthly 113 (2006), 57–62,
[primary full text](https://arxiv.org/pdf/math/0601660). No conjectural
irrationality measure is used. As r_n tends to the irrational e, its
reduced denominators tend to infinity.

Applying (24) to (22), and then Q_n<=q_n exp(O(n)), gives



$$
\log q_n\ge\frac{n\log n}{2+\epsilon}-O_\epsilon(n).
\tag{25}
$$



Combining (23), its exponential lower bound, and (25) proves
log|L_n|>=n log n/(2+epsilon)-O_epsilon(n). Letting epsilon tend to zero
proves (2). Every content and endpoint cancellation has already been
included through q_n. This completes the all-degree boundary theorem.

## 5. Positive but small degree b: exact reduced problem

For 1<=b<=n, the tests in (11) include all polynomials of degree <=n.
Nondegeneracy (13) therefore fixes the entire polynomial C^*:



$$
C^*=-\sum_{k=0}^{n}\frac{\ell_{n,B}(p_k)}{h_k}p_k.
\tag{26}
$$



The remaining high equations are exactly



$$
\ell_{n,B}(p_k)=0,\quad k=n+1,\ldots,n+b-1,
\tag{27}
$$



because each of these p_k is orthogonal to every possible C^* of degree
<=n. Finally the endpoint equation is



$$
B(1)+\sum_{k=0}^{n}\frac{p_k(1)\ell_{n,B}(p_k)}{h_k}=0.
\tag{28}
$$



Equations (27)–(28) are precisely b linear equations in b+1 B-coefficients.
They are an exact reduction of the original n+b+1 rows, not a heuristic
normality assertion. For b=1 only (28) remains. Its two coefficients
are not simultaneously zero for all sufficiently large n, as proved
after the norm estimate below. Normality for the growing-b allocation
is still open.

If H_B=max_j |B_j|, then



$$
|\ell_{n,B}(p_k)|\le\frac{(b+1)H_B 2^k}{(n+1-b)!}.
$$



Substitution in (26), using (15), gives the explicit safe bound



$$
\|C\|_1\le
 \frac{(b+1)(n+1)^2 64^{n+1}}{(n+1-b)!}H_B.
\tag{29}
$$



Since |Y|=|C(1)|<=||C||_1, this proves (3). The n/log n allocation
therefore cannot treat B as a coefficient block of modest size relative
to its endpoint even though it has comparatively few coefficients.

### A second exact boundary consequence: eventual normality for b=1

For b=1 write the endpoint row (28) as
(1+t_0)B_0+(1+t_1)B_1=0, where



$$
t_j=\sum_{k=0}^{n}p_k(1)\ell_{n,z^j}(p_k)/h_k.
$$



The same estimate gives
|t_j|<=2(n+1)^2 64^(n+1)/n!, which tends to zero. In particular both
coefficients 1+t_j are nonzero for all sufficiently large n (n>=512
is a safe explicit threshold, using n!>=(n/3)^n). The reduced matrix
therefore has rank one, and the original matched matrix has full row
rank for every n>=512. Its unique projective B has B_0 nonzero and



$$
B_1/B_0=-(1+t_0)/(1+t_1)=-1+O(e^{O(n)}/n!).
\tag{29a}
$$



This proves eventual normality for (n,1,n), not primitive endpoint
nondecay. The endpoint Y/B_0=(t_1-t_0)/(1+t_1) may be much smaller
than the coefficient norm; showing it is nonzero and controlling the
rational denominator of A(1)/Y require additional information. This
explains concretely why a full-rank theorem by itself is insufficient.

### Analytic estimates must preserve the two coefficient scales

Let r=1/sqrt(2), H_C=max_j |C_j|, q_E=M-b=2n+1, and
q_F=M-n=n+b+1. Summing the exact tails after the M vanishing coefficients
gives the unconditional bound



$$
|R(1)|\le
 H_B\frac{(q_E+1)^2}{q_E^2 q_E!}
 +H_C\frac{4r^{q_F}}{q_F(1-r)^2}.
\tag{30}
$$



The factorial improvement in the first term and the geometric improvement
in the second are different. After integral normalization the useful
bound is (30) divided by the endpoint gcd, or, invariantly, q times (30)
divided by |Y| as in (5). Equation (29) can be substituted into (30), but
does not provide the missing bound on H_B divided by the endpoint gcd.
A lower bound on H_B/|Y| cannot be substituted as an upper bound, and
cannot prove nondecay by itself. This is the exact remaining arithmetic
obstruction for small positive b.

The next narrow problem is to analyze the explicit b-by-(b+1) rational
matrix (27)–(28) and its evaluated endpoint denominator when
b=round(n/log n). A useful theorem must control its rational cofactors
and the reconstructed A(1), together with the signed endpoint remainder.
Normality alone or a real coefficient norm estimate alone is insufficient.
The b=0 proof suggests checking whether a rational approximant to e with
an exponentially bounded logarithmic companion still emerges from this
reduced matrix; (26) shows that such a companion is no longer automatic.

## 6. Predeclared finite checks, not asymptotics

The exact set was n=4,8,12,16 and b in
{0,1,round(n/log n),n}. The program
`check_unequal_hp_profiles.py` uses exact rational elimination, checks
all high rows and the Legendre reconstruction independently, retains
the primitive full triple, and performs a separate endpoint gcd.
Taylor/Machin intervals certify each displayed decimal decade.
Full exact triples and gcds are in `unequal_hp_exact_profiles.json`.

| n | b | floor(log10 primitive absolute endpoint) | floor(log10 endpoint with Y=1) |
|---:|---:|---:|---:|
|4|0|1|-3|
|4|1|1|-4|
|4|3|8|-4|
|4|4|10|-5|
|8|0|5|-6|
|8|1|12|-6|
|8|4|35|-8|
|8|8|65|-10|
|12|0|12|-9|
|12|1|24|-9|
|12|5|75|-11|
|12|12|174|-14|
|16|0|19|-12|
|16|1|36|-12|
|16|6|134|-14|
|16|16|339|-18|

All sixteen sampled matrices have full row rank, and all sixteen final
primitive endpoint magnitudes exceed one. These finite statements do not
prove eventual normality or nondecay for b>=1. Independently of this table,
the preceding arguments prove all-degree normality and eventual primitive
growth for b=0, and eventual normality for b=1.

## Route priority consequence

The exact boundary (n,0,n) should be removed from the active search. The
small-positive-b family remains open, but its explicit projection shows
that reducing the exponential degree does not remove the factorial
coefficient/endpoint mismatch. Its next meaningful work is the reduced
arithmetic matrix (27)–(28), not another broad degree scan. The composed
high-radius family remains a separate candidate; neither the boundary
theorem nor this specific Legendre projection has yet been proved for it.
