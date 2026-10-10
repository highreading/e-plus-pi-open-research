> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The high prime-power tail: an exact gap reduction and the surviving singleton barrier

Checked: 2026-08-27 UTC.

## 1. Verdict

Let



$$
q_0=q_1=1,\qquad q_n=(4n-2)q_{n-1}+q_{n-2}\quad(n\ge2).
\tag{1}
$$



The continuant gap polynomial gives an exact formula for every pairwise gcd:



$$
\boxed{\gcd(q_n,q_{n+d})=\gcd(q_n,P_d(n)).}
\tag{2}
$$



Consequently, if the same prime power divides two or more terms in an
interval, its repeated occurrences can be charged to explicit gap-polynomial
values.  This does **not** control the whole moving high-level valuation tail.
There is an exact decomposition into

1. one deepest occurrence for each prime, and
2. an overlap term controlled by pairwise gaps.

The first term is invisible to every argument that starts by assuming that a
prime divides two different $q_n$'s.  It is not a hypothetical artifact:
on the interval



$$
I=[1359,2717],
$$



the prime $11$ has exactly one term divisible by $11^4$, namely
$q_{1359}$, and



$$
v_{11}(q_{1359})=5.
\tag{3}
$$



The lift leading to this term has exactly one child at every level
$11,11^2,\ldots,11^6$ tested below.  In particular this contribution is
ordinary, not an all-$11$ branch.  It contributes $2\log 11$ to the
moving tail for $N=1359$, wholly inside the singleton term.

Thus excluding all-$p$ branching would be useful for root-density estimates,
but it would not by itself settle the high tail.  One also needs a uniform or
average estimate for the depth of isolated ordinary lifts (equivalently, for
the large squarefull part of individual $q_n$'s).  No such asymptotic
estimate is proved here.

## 2. The exact continuant identity

Define



$$
P_0(X)=0,\qquad P_1(X)=1,
\tag{4}
$$



and, for $j\ge0$,



$$
P_{j+2}(X)=(4X+4j+6)P_{j+1}(X)+P_j(X).
\tag{5}
$$



For $d\ge1$, induction in the recurrence (1) gives



$$
\boxed{
 q_{n+d}=P_d(n)q_{n+1}+P_{d-1}(n+1)q_n.}
\tag{6}
$$



Indeed, (6) is immediate for $d=1$.  If it holds at two consecutive
values, then the recurrence at index $n+d+1$, whose coefficient is
$4n+4d+2$, gives exactly (5) for the coefficient of $q_{n+1}$, and the
same shifted recurrence for the coefficient of $q_n$.

Consecutive terms are coprime.  More precisely,



$$
\gcd(q_n,q_{n+1})
 =\gcd(q_n,q_{n-1})
 =\cdots=\gcd(q_1,q_0)=1,
\tag{7}
$$



where each equality follows by subtracting the appropriate multiple in
(1).  Reducing (6) modulo $q_n$, and using that $q_{n+1}$ is invertible
modulo $q_n$, now proves (2).

This is stronger than the one-way implication commonly used in the zero-gap
argument: it identifies the pairwise gcd exactly, not merely a multiple that
it divides.

## 3. A cluster bound valid even with branching

All $P_d(n)$ are positive for $n\ge0,d\ge1$.  They also satisfy



$$
P_d(n)\le \{4(n+d)\}^{d-1}.
\tag{8}
$$



To prove this, note first that $P_0(n)\le P_1(n)$, and (5) inductively
implies $P_{r-1}(n)\le P_r(n)$.  Hence, for $r\ge1$,



$$
\begin{aligned}
 P_{r+1}(n)
 &=(4n+4r+2)P_r(n)+P_{r-1}(n)\\
 &\le(4n+4r+3)P_r(n)
 \le4(n+r+1)P_r(n).
 \end{aligned}
$$



Multiplication from $r=1$ to $d-1$ proves (8).

Now let $M>1$ divide



$$
q_{n_1},q_{n_2},\ldots,q_{n_k},
 \qquad
 N\le n_1<\cdots<n_k<N+L.
\tag{9}
$$



Put $d_i=n_{i+1}-n_i$.  Equation (2) gives



$$
M\mid P_{d_i}(n_i)\qquad(1\le i<k),
$$



and therefore



$$
M^{k-1}\mid\prod_{i=1}^{k-1}P_{d_i}(n_i).
\tag{10}
$$



Since $n_i+d_i=n_{i+1}<N+L$, (8) and the telescoping gap sum give



$$
\begin{aligned}
 M^{k-1}
 &\le\{4(N+L)\}^{\sum_i(d_i-1)}\\
 &\le\{4(N+L)\}^{L-k}.
 \end{aligned}
\tag{11}
$$



Writing $B=4(N+L)$, we obtain the unconditional bound



$$
\boxed{
 k\le1+\frac{(L-1)\log B}{\log M+\log B}.}
\tag{12}
$$



No Hensel-simplicity assumption was used.  Thus (12) remains valid even if a
root has all $p$ children at one or more levels.  For $M>L$, however, its
order of magnitude is still $L$, so it is far too weak to close the
required average estimate.

## 4. Exact separation of the moving high tail

Fix $N\ge2$, $X\ge3$, and put



$$
I_N=\{N,N+1,\ldots,2N-1\}.
$$



For each odd prime $p$, let



$$
b_p(N)=\min\{a\ge2:p^a>N\},
\tag{13}
$$



and define



$$
h_{p,n}=\bigl(v_p(q_n)-b_p(N)+1\bigr)_+.
\tag{14}
$$



The unresolved high tail is exactly



$$
H(N,X)=\sum_{p\le X}\sum_{n\in I_N}h_{p,n}\log p.
\tag{15}
$$



For every $p$, select $n_p\in I_N$ at which $h_{p,n}$ is maximal, and
write



$$
S(N,X)=\sum_{p\le X}h_{p,n_p}\log p.
\tag{16}
$$



This is the **singleton-max term**: one deepest high-level occurrence is
retained for each prime.  For $n\ne n_p$, maximality gives the exact
identity



$$
h_{p,n}
 =
 \left(
 v_p(\gcd(q_n,q_{n_p}))-b_p(N)+1
 \right)_+.
\tag{17}
$$



Indeed, both sides vanish when $h_{p,n}=0$; otherwise
$v_p(q_n)=b_p(N)-1+h_{p,n}$ and
$v_p(q_{n_p})\ge v_p(q_n)$.

For two indices define the truncated high gcd



$$
G_{N,X}(n,m)=
 \prod_{p\le X}
 p^{
 \left(v_p(\gcd(q_n,q_m))-b_p(N)+1\right)_+
 }.
\tag{18}
$$



Summing (17), then allowing all unordered pairs rather than only the
$p$-dependent star pairs, yields



$$
\boxed{
 S(N,X)\le H(N,X)
 \le S(N,X)+
 \sum_{N\le n<m<2N}\log G_{N,X}(n,m).}
\tag{19}
$$



Equations (2) and (18) give



$$
G_{N,X}(n,n+d)
 \mid\gcd(q_n,q_{n+d})
 =\gcd(q_n,P_d(n)),
\tag{20}
$$



so every term after $S(N,X)$ is controlled by a gap polynomial.
Conversely, no gap polynomial appears in $S(N,X)$: it can be large even
when every relevant prime occurs at only one index of the interval.

For scale, the most direct use of (8) in (19) gives only



$$
\begin{aligned}
 \sum_{N\le n<m<2N}\log G_{N,X}(n,m)
 &\le
 \sum_{d=1}^{N-1}(N-d)(d-1)\log(8N)\\
 &=\frac{N(N-1)(N-2)}6\log(8N).
 \end{aligned}
\tag{21}
$$



The target total is $o(N^2\log N)$, so (21) loses a full factor of $N$.
More importantly, even a sharp treatment of the overlap term would still
leave $S(N,X)$.

The only unconditional size bound for the latter obtained from the present
information is



$$
S(N,X)\le H(N,X)
 \le\sum_{n=N}^{2N-1}\log q_n=O(N^2\log N),
\tag{22}
$$



which has exactly the forbidden main scale.  Replacing the last big-oh by a
little-oh requires new arithmetic input about isolated prime-power
divisibility, not another pairwise gap estimate.

## 5. A certified ordinary singleton

Take



$$
p=11,\qquad n=1359.
$$



Exact modular recurrence gives



$$
q_{1359}\equiv3\cdot11^5\pmod {11^6},
\tag{23}
$$



and hence (3).  The successive root representatives and their unique child
digits are



$$
\begin{array}{c|c|c|c}
a&11^a&r_a=n\bmod 11^a&
 t\in\{0,\ldots,10\}:\ 11^{a+1}\mid q_{r_a+t11^a}\\ \hline
1&11&6&2\\
2&121&28&0\\
3&1331&28&1\\
4&14641&1359&0\\
5&161051&1359&8
\end{array}
\tag{24}
$$



At every displayed level there is exactly one child.  At the first level,



$$
q_6\equiv22,\qquad q_{17}\equiv110\pmod {121},
$$



so the affine first-lift slope is



$$
\delta_{11}(6)=\frac{-q_{17}-q_6}{11}\equiv10\not\equiv0\pmod {11}.
\tag{25}
$$



This independently confirms that the branch is ordinary from its first
step.

Now set $N=1359$.  Since



$$
11^3=1331\le N<11^4=14641,
$$



we have $b_{11}(N)=4$.  Exhaustive modular recurrence on
$[1359,2717]$ gives



$$
\{n\in I_N:11^4\mid q_n\}=\{1359\}.
\tag{26}
$$



Thus the two high levels $11^4,11^5$ contribute



$$
h_{11,1359}\log11=2\log11
$$



to both $H(N,X)$ and $S(N,X)$ for every $X\ge11$, and contribute
nothing to the overlap term in (19).

There is also a smaller ordinary-square example:



$$
q_8=312129649,\qquad v_{13}(q_8)=2,\qquad
 \delta_{13}(8)\equiv1\pmod {13}.
\tag{27}
$$



These finite examples do not prove that the singleton term is asymptotically
large.  Their rigorous role is narrower and important: they show that
ordinary unique lifts really do enter the moving high tail, so eliminating
all-$p$ branching alone cannot be presented as a solution.

## 6. What remains

The gap-polynomial strategy has two logically separate outstanding tasks:

1. improve the aggregate overlap estimate in (19) from the cubic bound
   (21) to $o(N^2\log N)$; and
2. prove independently that



$$
S(N,X)=o(N^2\log N)
\tag{28}
$$



in the moving range $X\asymp N\log N$.

The second is a large-squarefull-part problem for the individual Bessel
denominators.  Prime-power periodicity, first-lift branching, and pairwise
gcds do not currently imply (28).  Therefore this route remains incomplete
and does not classify $e+\pi$.

## 7. Exact certificate

The companion script

`scripts/bessel_denominator_high_tail_gap_singleton_certificate.py`

checks, with exact integer arithmetic:

1. (6), (2), (7), and (8) on a finite rectangular audit range;
2. $v_{11}(q_{1359})=5$ via the nonzero residue modulo $11^6$;
3. every one of the eleven children at each level in (24);
4. the nonzero slopes in (25) and (27); and
5. the exhaustive singleton assertion (26).

The all-$n,d,N$ claims are proved above; the finite calculation is an
independent regression certificate, not a replacement for those proofs.
