> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A critical-scale approximation criterion for e + pi

Status: rigorous auxiliary reduction; does not prove the main irrationality statement. The mathematical deduction below is independently checked against Davis's theorem; no novelty claim is made.

## 1. Precise scale

For an irrational real number $x$, define



$$
\mathcal C(x)=\liminf_{q\to\infty}
\min_{p\in\mathbb Z}
q^2\left|x-\frac pq\right|\frac{\log q}{\log\log q}.
$$



Only sufficiently large $q$ enter, so both logarithms are positive. Davis's Theorem 1 states



$$
\mathcal C(e)=\frac12.
$$



Source: C. S. Davis, “Rational approximations to e,” Journal of the Australian Mathematical Society 25 (1978), 497–502, [primary PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/0A59D34AF70DE5ED9A5F3FB1E3703976/S1446788700021480a.pdf/rational_approximations_to_e.pdf), [DOI](https://doi.org/10.1017/S1446788700021480).

In particular, for every $0<c<1/2$, all sufficiently large integers $Q$ and all integers $P$ satisfy



$$
\left|e-\frac P Q\right|
\ge c\,\frac{\log\log Q}{Q^2\log Q}.
\tag{1}
$$



The all-integer quantifier matters: no unproved coprimality condition may be inserted during a rational translation.

## 2. Rational-translation lower bound

**Proposition.** If $a\in\mathbb Z$, $b\in\mathbb Z_{>0}$, and
$\alpha=a/b-e$, then



$$
\boxed{\mathcal C(\alpha)\ge\frac1{2b^2}>0.}
\tag{2}
$$



**Proof.** For every integer $p$ and positive integer $q$,



$$
\left|\alpha-\frac pq\right|
=\left|e-\frac{aq-bp}{bq}\right|.
$$



Apply (1) directly at $P=aq-bp$, $Q=bq$. Multiplying by
$q^2\log q/\log\log q$ gives a lower bound



$$
\frac c{b^2}\,
\frac{\log\log(bq)}{\log(bq)}
\frac{\log q}{\log\log q}.
$$



For fixed $b$, the product of logarithmic ratios tends to 1. Taking the
liminf, then $c\uparrow1/2$, proves (2). The fraction need not be reduced.
$\square$

**Corollary.**



$$
\boxed{\mathcal C(\pi)=0
\quad\Longrightarrow\quad e+\pi\notin\mathbb Q.}
\tag{3}
$$



Indeed, a rational equality $e+\pi=a/b$ contradicts (2).

There is a complementary upper bound. Choose Davis convergents
$P_k/Q_k$ whose normalized error tends to $1/2$. The fractions
$(aQ_k-bP_k)/(bQ_k)$ approximate $\alpha$ with exactly the same
absolute error. At the possibly unreduced denominator $bQ_k$, their
normalized error tends to $b^2/2$. Thus



$$
\boxed{\frac1{2b^2}\le\mathcal C(a/b-e)\le\frac{b^2}{2}.}
\tag{2a}
$$



Consequently $\mathcal C(\pi)=+\infty$ is another sufficient condition
for irrationality of the sum. For example, bounded partial quotients of
$\pi$ would imply that condition. Neither boundedness nor the zero
alternative has been proved for $\pi$. The endpoints in (2a) are not
asserted to be sharp for each rational translation.

The zero alternative is weaker as an approximation demand than requiring a fixed
irrationality exponent above 2 for $\pi$. It still requires an unproved
Diophantine property of that particular constant.

## 3. Exact continued-fraction equivalent

Let $x=[a_0;a_1,a_2,\ldots]$, with principal convergents $p_k/q_k$ and
complete quotient $\alpha_{k+1}=[a_{k+1};a_{k+2},\ldots]$. The standard
exact error identity is



$$
q_k^2\left|x-\frac{p_k}{q_k}\right|
=\frac1{\alpha_{k+1}+q_{k-1}/q_k},
\qquad
a_{k+1}<\alpha_{k+1}+q_{k-1}/q_k<a_{k+1}+2.
\tag{4}
$$



Consequently



$$
\boxed{
\mathcal C(x)=0
\iff
\limsup_{k\to\infty}
a_{k+1}\frac{\log\log q_k}{\log q_k}=\infty.}
\tag{5}
$$



For the forward implication, any sequence attaining normalized error
tending to zero has, eventually, error less than $1/(2q^2)$. For reduced
fractions, Legendre's criterion makes these principal convergents. Reducing
an unreduced fraction can only improve the relevant asymptotic bound;
bounded reduced denominators cannot approach the fixed irrational $x$.
Equation (4) then forces the limsup in (5). Conversely, choose convergents
along which that limsup tends to infinity and use (4).

A completely explicit sufficient remaining lemma is therefore:

> For every $C>0$, infinitely many principal convergents of $\pi$
> satisfy $a_{k+1}>C\log q_k/\log\log q_k$.

No reviewed result proves this for $\pi$. Unbounded partial quotients
alone are insufficient. An upper bound on $\mu(\pi)$, including the
September 2026 preprint, does not prove this moving-threshold lower bound.
No finite list of large partial quotients proves it either.

## 4. Independent check of the lower-bound input

The lower half of Davis's theorem also follows directly from Euler's
continued fraction, without accepting a numerical asymptotic fit.

Euler's partial quotients satisfy



$$
a_{3r-2}=a_{3r}=1,\qquad a_{3r-1}=2r.
$$



If $q_n$ is the $n$-th convergent denominator and
$k=\lfloor(n+1)/3\rfloor$, the recurrence
$q_j=a_jq_{j-1}+q_{j-2}$ gives



$$
q_n\ge\prod_{r=1}^{k}(2r)=2^k k!,
\qquad a_{n+1}\le2(k+1).
$$



Stirling's formula implies
$k\le(1+o(1))\log q_n/\log\log q_n$. Thus (4) gives



$$
\left|e-\frac{p_n}{q_n}\right|
\ge\left(\frac12-o(1)\right)
\frac{\log\log q_n}{q_n^2\log q_n}.
$$



Reduced nonconvergents have error at least $1/(2q^2)$, which is stronger
eventually. To extend to unreduced $P/Q$, reduce to $p/q$. If 

$$
q\to
\infty
$$

, the function $\log\log t/(t^2\log t)$ is decreasing for large
$t$, so the lower bound at $q\le Q$ implies the bound at $Q$. If $q$
stays bounded, the distance from $e$ to those finitely many relevant
fractions is bounded away from zero, and the bound follows eventually.
This proves (1).

For a check of the sharp constant, $q_n\le\prod_{j=1}^n(a_j+1)$ gives
$\log q_n=k\log k+O(k)$. Along the convergents immediately preceding
$a_{n+1}=2(k+1)$, (4) makes the normalized error tend to $1/2$.
Thus the lower bound has the right scale and constant.

## 5. Connection with the project's content threshold

Given an integer $\pi$-form $U_m+V_m\pi$, divide by
$c_m=\gcd(U_m,V_m)$ and put $b_m=|V_m|/c_m$. Its rational approximation
error is $|U_m+V_m\pi|/|V_m|$. If $b_m\to\infty$, (3) shows that



$$
\frac{|V_m|\,|U_m+V_m\pi|}{c_m^2}
\frac{\log b_m}{\log\log b_m}\longrightarrow0
$$



on an infinite subsequence is sufficient for irrationality of the sum.
The archive gives $\log|V_m|/(6m)\to h$ and only the upper bound
$\limsup\log|U_m+V_m\pi|/(6m)\le h-d$. These give the available upper
exponent $2h-d-2\log c_m/(6m)$, recovering the same sufficient threshold
$\log c_m/(6m)>h-d/2$. At equality, suitable lower-order savings could
still suffice; exponential exponents alone are inconclusive.

The current proved content rate is far below that threshold. This criterion
neither supplies missing content nor changes the ledger. Its value is to
state exactly what a critical-scale improvement would have to accomplish.
