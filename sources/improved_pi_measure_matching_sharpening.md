> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Sharpening the primitive-matching barriers with the current measure of $\pi$

Date: 2026-08-26

## 1. Input and scope

Zeilberger and Zudilin proved



$$
\mu(\pi)\le
7.103205334137\ldots .
\tag{1}
$$



We use only the weaker rational exponent



$$
\tau=\frac{36}{5}=7.2.
\tag{2}
$$



This improves the numerical exponents in the already accepted
primitive-matching barriers.  It does not change their qualitative
hypotheses and does not prove any arithmetic statement about $e+\pi$.
The earlier sources remain frozen; this note records independent
corollaries of their exact matching and height lemmas.

Primary source: D. Zeilberger and W. Zudilin, “The irrationality measure
of $\pi$ is at most $7.103205334137\ldots$,” *Moscow Journal of
Combinatorics and Number Theory* 9 (2020), no. 4, 407--419,
[DOI 10.2140/moscow.2020.9.407](https://doi.org/10.2140/moscow.2020.9.407);
[arXiv:1912.06345](https://arxiv.org/abs/1912.06345).

## 2. A uniform integer-form bound

### Lemma 2.1

There is a fixed $c_\pi>0$ such that, for every
$A\in\mathbb Z$, $B\in\mathbb Z_{\ge1}$, and
$\delta\in\{1,-1\}$,



$$
|A+\delta B\pi|
\ge c_\pi B^{-31/5}.
\tag{3}
$$



### Proof

The definition of (1), together with $\tau>7.103205334137\ldots$,
gives, for all sufficiently large denominators $B$ and every integer
$p$,



$$
\left|\pi-\frac pB\right|\ge B^{-36/5}.
\tag{4}
$$



For $p=-\delta A>0$, multiplication by $B$ gives (3) with constant
one at all sufficiently large $B$.  If $p\le0$, the left side is at
least $B\pi$.  For the finitely many remaining positive denominators,
irrationality of $\pi$ gives a positive minimum after optimizing the
integer numerator.  Decreasing one fixed constant proves (3) in all
cases. $\square$

## 3. Universal minimal matching

Let



$$
E_n=q_ne-p_n>0,\qquad
\gcd(p_n,q_n)=1,
\tag{5}
$$



be the primitive exponential beta form from the accepted fixed-denominator
theorem.  For positive even $n$,



$$
q_n\ge n^n,\qquad
\frac{E_n}{q_n}\le e\,n^{-2n-1}.
\tag{6}
$$



Let



$$
L=A+\varepsilon B\pi,\qquad
\gcd(A,B)=1,\qquad B>0,
\tag{7}
$$



be any primitive nonzero integer $\pi$-form, oriented by its value.
Put



$$
d=\gcd(q_n,B),\qquad q_n=dq_0,\qquad B=dB_0.
\tag{8}
$$



The exact matching lemma in the accepted sources proves that $B_0,q_0$
are the minimal coefficient multipliers and that the final content $g$
satisfies



$$
g\mid d.
\tag{9}
$$



This includes both coefficient signs and a zero matched constant
coefficient.

If the two positive component values have the same target-coefficient
sign, (3) and (9) give



$$
|\Lambda_n^{\rm prim}|
\ge c_\pi\frac{q_n}{B^{41/5}}.
\tag{10}
$$



If their signs are opposite, the possible-cancellation ratio now obeys



$$
\frac{E_n/q_n}{|L|/B}
\le c_\pi^{-1}e\,B^{36/5}n^{-2n-1}.
\tag{11}
$$



Whenever $\log B=o(n\log n)$, this ratio tends to zero.  The same
content calculation therefore gives, for all sufficiently large indices,



$$
|\Lambda_n^{\rm prim}|
\ge\frac{c_\pi}{2}\frac{q_n}{B^{41/5}}
\tag{12}
$$



in both sign classes.

The exponent $41/5$ has the same transparent origin as the earlier
integer exponent $9$: $31/5$ powers come from the integer-form
measure (3), and at most two further powers come from minimal matching and
final content removal.

## 4. Stronger necessary escape scales

If the final primitive forms remain bounded in the same-sign case, (6)
and (10) force



$$
\log B\ge
\frac5{41}n\log n-O(1),
\qquad
B\ge n^{\,5n/41-o(n)}.
\tag{13}
$$



In the opposite-sign case, either (12) applies or the cancellation ratio
in (11) exceeds $1/2$.  The latter alternative forces



$$
B^{36/5}\gg n^{2n+1}
\tag{14}
$$



and hence



$$
\log B\ge
\frac5{18}n\log n-O(\log n),
\qquad
B\ge n^{\,5n/18-o(n)}.
\tag{15}
$$



Thus every bounded escape from a fixed-denominator/projective-height
family must at least reach the stronger scale in (13); genuine
opposite-sign cancellation requires (15).

## 5. The critical quadratic-power Fourier region

For the accepted even-$n$, $k>n$ Fourier family, the exact primitive
coefficient estimate is



$$
B_{n,k}\le64^{k-1}\gamma^n,
\qquad
\gamma=\frac{1+\sqrt2}{2}.
\tag{16}
$$



Only same-sign matching occurs.  Equations (6), (10), and (16) give



$$
\log|\Lambda_{n,k}^{\rm prim}|
\ge
n\log n
-\frac{41}{5}(k-1)\log64
-\frac{41}{5}n\log\gamma
+O(1).
\tag{17}
$$



In particular,



$$
n<k\le\frac1{35}n\log n
\tag{18}
$$



implies divergence for all sufficiently large even $n$.  To certify the
constant without decimal logarithms, use the elementary bound
$\log2<7/10$.  Then



$$
\frac{41}{5}\log64
=\frac{246}{5}\log2
<\frac{861}{25}
=34.44<35.
\tag{19}
$$



The term involving $n\log\gamma$ in (17) is $O(n)$, so the strict
margin in (19) absorbs it for sufficiently large $n$.

This improves the previously recorded explicit constant $1/40$ to
$1/35$.  It remains a barrier theorem: the region beyond this constant
is not asserted to work.
