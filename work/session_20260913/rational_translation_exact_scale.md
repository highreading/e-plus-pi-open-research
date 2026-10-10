> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact critical-scale constant for rational translates of e

2026-09-13. Status: rigorous auxiliary result. This is an elementary consequence of Euler's continued fraction and finite modular recurrences; no originality claim is made. It neither computes the corresponding constant for pi nor settles e+pi.

For irrational x, put


$$
f(t)=\frac{\log t}{\log\log t},\qquad
\mathcal C(x)=\liminf_{q\to\infty}\min_{p\in\mathbb Z}
q^2\left|x-\frac pq\right|f(q).
$$


All assertions involving f are for sufficiently large positive t. In particular f(t) tends to infinity, is eventually increasing, and f(ct)/f(t) tends to1 for every fixed c>0.

## The exact formula

Let a/b be reduced, with a an integer and b a positive integer. For k≥1 let P_k/Q_k be the Euler convergent to e with full continued-fraction index 3k−2, using index0 for the initial term2. Thus


$$
\frac{P_1}{Q_1}=\frac31,\quad
\frac{P_2}{Q_2}=\frac{19}7,\quad
\frac{P_3}{Q_3}=\frac{193}{71}.
$$


Define


$$
d_k=\gcd(aQ_k-bP_k,bQ_k),
\qquad
D=\max\{d:\ d_k=d\text{ for infinitely many }k\}.
\tag{1}
$$


The gcd is positive, allowing its first argument to be negative. Then


$$
\boxed{\mathcal C(a/b-e)=\frac{b^2}{2D^2}.}
\tag{2}
$$


Moreover every value taken by d_k recurs infinitely often, and D can be found by a terminating exact finite-state computation modulo b². A universally valid explicit bound for the number of states inspected is b⁶. No closed prime-factor formula for D is asserted here.

## Euler input, with the subsequence identified exactly

Euler's regular continued fraction satisfies


$$
a_{3j-2}=a_{3j}=1,\qquad a_{3j-1}=2j\quad(j\ge1).
$$


For its full convergents p_n/q_n,


$$
q_n^2|e-p_n/q_n|
=\frac1{[a_{n+1};a_{n+2},\ldots]+q_{n-1}/q_n},
$$


and the denominator on the right lies strictly between a_{n+1} and a_{n+1}+2.

The elementary product estimates


$$
2^j j!\le q_n\le\prod_{h=1}^{n}(a_h+1),
\qquad j=\lfloor(n+1)/3\rfloor,
$$


give log q_n=j log j+O(j), hence f(q_n)~j. On the indices n=3k−2, the next partial quotient is2k, and j=k−1. Consequently


$$
Q_k^2|e-P_k/Q_k|f(Q_k)\longrightarrow\frac12.
\tag{3}
$$


Every other sufficiently large full convergent has next partial quotient1, hence q_n²|e-p_n/q_n|>1/3. Its weighted error therefore tends to infinity along those indices.

A sequence of reduced rational approximations to e with bounded weighted error eventually consists of principal convergents: its unweighted denominator-squared error tends to zero, so Legendre's criterion applies. The preceding paragraph then shows that it eventually belongs to the exact subsequence P_k/Q_k. This establishes the exhaustion property needed for the reverse inequality in (2), not just an upper construction.

## Rational reduction and complementary gcds

The following facts hold for any reduced P/Q, not only for Euler convergents. Put


$$
N=aQ-bP,\qquad d=\gcd(N,bQ).
$$


Then d divides b². Indeed d divides bQ and bN−abQ=−b²P, so


$$
d\mid\gcd(bQ,b^2P)=b\gcd(Q,b)\mid b^2.
\tag{4}
$$


The rational number a/b−P/Q reduces to


$$
\frac pq=\frac{N/d}{bQ/d},\qquad q=\frac{bQ}{d}.
\tag{5}
$$


In particular Q/b≤q≤bQ.

Conversely, begin with reduced p/q and reduce


$$
\frac ab-\frac pq=\frac{aq-bp}{bq}=\frac PQ.
$$


Writing g=gcd(aq−bp,bq), one has g|b² and


$$
P=\frac{aq-bp}{g},\quad Q=\frac{bq}{g},
\quad aQ-bP=\frac{b^2p}{g},\quad bQ=\frac{b^2q}{g}.
$$


Because p/q is reduced, the forward gcd at P/Q is therefore


$$
\boxed{d=b^2/g.}
\tag{6}
$$


Thus the two reduction factors are complementary and no hidden cancellation is discarded in either direction.

For the scalar modular computation it is useful to have the stronger identity


$$
\boxed{\gcd(aQ-bP,bQ)=\gcd(aQ-bP,b^2).}
\tag{7}
$$


Here coprimality of a,b and of P,Q is essential. To verify (7), fix a prime l dividing b and write s=v_l(b), t=v_l(Q). If t<s, then v_l(N)=t, since a is a unit at l. If t>s, then P is a unit and v_l(N)=s. If t=s, then v_l(N)≥s and v_l(bQ)=2s. In each case


$$
\min\{v_l(N),s+t\}=\min\{v_l(N),2s\}.
$$


For primes not dividing b, (4) excludes a factor on the left and b² excludes it on the right. This proves (7).

## Proof of the exact critical-scale formula

First apply (5) to each sharp Euler convergent. The reduced rational p_k/q_k then approximates alpha=a/b−e with exactly the same absolute error as P_k/Q_k approximates e. Since q_k=bQ_k/d_k,


$$
q_k^2|\alpha-p_k/q_k|f(q_k)
=\frac{b^2}{d_k^2}
\left(Q_k^2|e-P_k/Q_k|f(Q_k)\right)
\frac{f(bQ_k/d_k)}{f(Q_k)}.
\tag{8}
$$


There are only finitely many possible d_k, all divisors of b². Along the infinite subsequence with d_k=D, (3) and the fixed-factor ratio of f give the limit b²/(2D²). Also q_k≥Q_k/b tends to infinity. This proves the upper bound in (2).

For the reverse bound, it suffices first to consider any sequence of *reduced* fractions p_j/q_j approximating alpha, with q_j tending to infinity and weighted error bounded. Map each fraction back to a reduced approximation P_j/Q_j to e. The denominator comparison Q_j/q_j∈[1/b,b] and eventual fixed-factor comparability of f show that the weighted errors for e are bounded as well. By the exhaustion property proved above, each sufficiently late P_j/Q_j is a sharp Euler convergent P_k/Q_k, with k tending to infinity.

Equation (6) ensures that mapping this e convergent forward recovers exactly p_j/q_j and the same d_k. Formula (8) therefore applies to every sufficiently late member of the original sequence. Any d-value occurring infinitely in that sequence is at most D; (3) then gives a liminf at least b²/(2D²). This proves the lower bound among reduced fractions.

For completeness, allowing unreduced fractions does not lower this liminf. Write an arbitrary fraction p/q in reduced form p0/q0. Along a sequence of bounded weighted errors at q tending to infinity, the errors themselves tend to zero, and hence q0 tends to infinity; otherwise bounded reduced denominators could not approach the fixed irrational alpha. Since t²f(t) is eventually increasing and q0≤q,


$$
q^2|\alpha-p/q|f(q)
\ge q_0^2|\alpha-p_0/q_0|f(q_0).
$$


Thus the reduced lower bound applies. Any sequence violating the claimed lower bound would have a subsequence with bounded weighted error, so the preceding argument rules it out. Together with the finite upper construction this completes (2).

## Pure periodicity and an explicit algorithm for every a/b

Adjoin P_0=Q_0=1. The three-step Euler recurrence gives, for k≥1,


$$
P_{k+1}=(4k+2)P_k+P_{k-1},\qquad
Q_{k+1}=(4k+2)Q_k+Q_{k-1}.
\tag{9}
$$


For k=1 this is verified directly from (P_0,Q_0)=(1,1), (P_1,Q_1)=(3,1), (P_2,Q_2)=(19,7). For subsequent indices it follows by substituting the three full-convergent recurrences with partial quotients 2k,1,1 and eliminating the intervening vectors.

Hence N_k=aQ_k−bP_k obeys the scalar recurrence


$$
N_0=a-b,\quad N_1=a-3b,\quad
N_{k+1}=(4k+2)N_k+N_{k-1}.
\tag{10}
$$


Set m=b². Its augmented state is


$$
S_k=(N_k\bmod m,N_{k-1}\bmod m,k\bmod m).
$$


The update map on (Z/mZ)³ is


$$
T(u,v,t)=((4t+2)u+v,u,t+1).
$$


It is a permutation, with explicit inverse


$$
T^{-1}(u',v',t')
=(v',u'-(4(t'-1)+2)v',t'-1).
$$


Consequently the orbit starting at S_1 is purely periodic, with a period at most m³=b⁶. By (7), d_k=gcd(N_k,m) depends only on S_k. Every d-value in this finite orbit therefore occurs infinitely often, proving the recurrence assertion following (2).

An exact algorithm is now immediate: iterate T from


$$
((a-3b)\bmod m,(a-b)\bmod m,1\bmod m)
$$


until this state first returns; take D to be the maximum of gcd(u,m) along the orbit. The bound b⁶ guarantees termination; the algorithm does not assume any experimentally observed smaller period. Translating a/b by an integer leaves each d_k unchanged, since it adds a multiple of bQ_k to the first argument of the gcd in (1).

## Exact finite examples and one infinite family

The companion `rational_translation_exact_scale.py` performs only integer modular arithmetic, verifies the inverse update at every step, checks return to the initial state, and records the complete list of distinct gcd-values in `rational_translation_exact_scale_examples.json`. The listed periods are proved finite cycles by exhaustive exact traversal, not extrapolated numerical patterns.

| a/b | Certified state period | D | Exact C(a/b−e) |
|---|---:|---:|---:|
| 0/1 | 1 | 1 | 1/2 |
| 1/2 | 4 | 1 | 2 |
| 1/3 | 18 | 1 | 9/2 |
| 1/5 | 50 | 1 | 25/2 |
| 1/7 | 98 | 49 | 1/98 |
| 2/7 | 98 | 49 | 1/98 |
| 1/11 | 242 | 121 | 1/242 |
| 1/14 | 196 | 49 | 2/49 |
| 1/17 | 578 | 1 | 289/2 |
| 1/49 | 4802 | 2401 | 1/4802 |

In particular, neither D=b nor D=b² is a valid universal simplification. The cycles for a=1,b=7 and a=2,b=7 first attain D=49 at k=23 and k=51 respectively; equality of their maxima does not assert that their gcd sequences agree.

There is also a short symbolic infinite-family consequence. All Q_k are odd by (9). Modulo3, the successive Q_k for k≥0 have the repeating block


$$
1,1,1,2,2,2.
$$


This can be verified from the recurrence and return of the augmented state (Q_k,Q_{k-1},k mod3) at k=7 to its value at k=1. No Q_k is divisible by2 or3. Therefore, if b=2^u3^v and gcd(a,b)=1, every N_k=aQ_k−bP_k is coprime to b, so D=1 and


$$
\boxed{\mathcal C(a/b-e)=b^2/2\qquad(b=2^u3^v).}
\tag{11}
$$



## Consequence for the research target, and its limitation

If e+pi=a/b were rational in lowest terms, (2) would force


$$
\mathcal C(\pi)=\frac{b^2}{2D^2},\qquad D\mid b^2.
$$


In particular


$$
\boxed{e+\pi\in\mathbb Q\Longrightarrow
2\mathcal C(\pi)\text{ is a nonzero square in }\mathbb Q.}
\tag{12}
$$


This sharpens the previous necessary condition that C(pi) be finite and positive. It also gives an exact denominator-sensitive obstruction if one could independently determine C(pi). No such value, or contrary property, is established here. Numerical continued fractions of pi cannot prove the required infinite statement.

The most useful additional original-math questions in this narrow branch are whether D admits a simpler prime-power characterization, and whether pi-specific information can rule out the resulting critical-scale constants. The former concerns rational translates of e and by itself will not decide the latter.
