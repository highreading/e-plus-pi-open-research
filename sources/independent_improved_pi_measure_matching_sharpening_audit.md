> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the improved pi-measure matching sharpening

Date: 2026-08-26

## Verdict

**ACCEPT.** The Zeilberger--Zudilin input, the uniform conversion with
$\tau=36/5$, both primitive-matching signs, the zero-constant edge
case, all four rational exponents, and the explicit Fourier constant
$1/35$ rederive correctly. I found no mathematical defect in the
standalone source.

The accepted source is
sources/improved_pi_measure_matching_sharpening.md, with SHA-256

9db7e8432631cf102d913b18e3bc74db72bfee634ab008a489dacab3bc6ff040.

The source was not modified during this audit.

## 1. Exact irrationality-measure input

Zeilberger and Zudilin define the irrationality measure $\mu(x)$ as
the least exponent $\mu$ such that, for every $\epsilon>0$,



$$
\left|x-\frac pq\right|>
\frac1{q^{\mu+\epsilon}}
$$



for all integers $p$ and all sufficiently large positive integers
$q$. Their final result is



$$
\mu(\pi)\le
7.10320533413700172750577342281\ldots .
$$



This is the exact kind of uniform quantification needed here: the
denominator threshold may depend on the chosen excess exponent, but not
on $p$.

Since



$$
\tau=\frac{36}{5}=7.2
>
7.1032053341370017\ldots,
$$



one may choose a fixed positive excess smaller than the gap to $7.2$.
It follows that, for all sufficiently large $B$ and every
$p\in\mathbb Z$,



$$
\left|\pi-\frac pB\right|>B^{-36/5}.
$$



Thus the source's use of constant one at large denominators is safe; no
unrecorded multiplicative constant from the primary theorem is required.

## 2. Uniform integer-form conversion

Let $A\in\mathbb Z$, $B\ge1$, and $\delta\in\{1,-1\}$, and put



$$
p=-\delta A.
$$



Then the exact identity



$$
|A+\delta B\pi|
=B\left|\pi-\frac pB\right|
$$



holds for either sign. If $B$ is sufficiently large, the primary
measure therefore gives



$$
|A+\delta B\pi|>B^{1-36/5}=B^{-31/5}.
$$



The source separately treats $p\le0$, where
$\pi-p/B\ge\pi$, so the form is at least $B\pi$. This is valid but
not actually necessary because the primary definition already quantifies
over every integer $p$.

For each of the finitely many remaining positive denominators,



$$
\min_{A\in\mathbb Z,\,\delta=\pm1}
|A+\delta B\pi|
=\operatorname{dist}(B\pi,\mathbb Z)>0
$$



by irrationality of $\pi$. Consequently



$$
c_\pi=
\min\left\{
1,\
\min_{1\le B<B_0}
B^{31/5}\operatorname{dist}(B\pi,\mathbb Z)
\right\}>0
$$



gives the claimed all-sign, all-numerator, all-denominator bound



$$
|A+\delta B\pi|\ge c_\pi B^{-31/5}.
$$



No coprimality hypothesis is needed. The exponent $31/5$ is exactly
$\tau-1$, because passing from rational approximation to an integer
linear form multiplies by $B$.

## 3. Minimal matching and final content

Let



$$
E_n=q_ne-p_n>0,\qquad
\gcd(p_n,q_n)=1,
$$



and let the oriented primitive pi-form be



$$
\widetilde L=\widetilde A+\delta B\pi=|L|>0,
\qquad
\gcd(\widetilde A,B)=1,\qquad B>0.
$$



Put



$$
d=\gcd(q_n,B),\qquad
q_n=dq_0,\qquad B=dB_0.
$$



Then $\gcd(q_0,B_0)=1$, and the least positive multipliers making the
two target coefficients equal are $B_0$ and $q_0$. The common
coefficient is



$$
C=dq_0B_0=\frac{q_nB}{d}.
$$



For either target sign, the matched constant has the form



$$
M=-B_0p_n\mathbin{\pm}q_0\widetilde A.
$$



If a prime $\ell$ divides $q_0$, then it divides neither $B_0$
nor $p_n$, and



$$
M\equiv-B_0p_n\not\equiv0\pmod\ell.
$$



If $\ell\mid B_0$, then it divides neither $q_0$ nor
$\widetilde A$, and



$$
M\equiv\pm q_0\widetilde A\not\equiv0\pmod\ell.
$$



Thus no prime from $q_0B_0$ divides the final content
$g=\gcd(M,C)$. Prime power by prime power, every surviving exponent in
$g$ is bounded by its exponent in $d$, so



$$
g\mid d.
$$



This proof is insensitive to the matching sign. If $M=0$, the same
congruences show that $q_0=B_0=1$; then $C=d$ and
$g=\gcd(0,d)=d$. Hence the zero matched constant is also fully covered.

Two consequences used repeatedly below are



$$
dg\le d^2\le B^2
$$



and



$$
\frac{q_0}{g}=\frac{q_n}{dg}\ge\frac{q_n}{B^2}.
$$



## 4. Same-sign lower bound and the exponent $41/5$

In the same-sign branch the raw matched value is a sum of two positive
components:



$$
W^+=B_0E_n+q_0\widetilde L.
$$



After primitive reduction,



$$
\frac{W^+}{g}
\ge\frac{q_0\widetilde L}{g}
=\frac{q_n|L|}{dg}
\ge\frac{q_n|L|}{B^2}.
$$



The integer-form measure therefore gives



$$
\left|\Lambda_n^{\rm prim}\right|
\ge c_\pi\frac{q_n}{B^{31/5+2}}
=c_\pi\frac{q_n}{B^{41/5}}.
$$



Thus the exponent $41/5$ has exactly the source's stated decomposition:
$31/5$ from the pi-form measure and at most $2$ from minimal matching
and primitive content.

If these primitive forms remain bounded and $q_n\ge n^n$, then



$$
B^{41/5}\gg n^n,
$$



so



$$
\log B\ge\frac5{41}n\log n-O(1).
$$



Equivalently,



$$
B\ge n^{\,5n/41-o(n)}.
$$



The coefficient $5/41$ is therefore correct.

## 5. Opposite-sign cancellation and the exponent $36/5$

In the opposite-sign branch,



$$
W^-=
B_0E_n-q_0\widetilde L
=\frac{q_nB}{d}
\left(\frac{E_n}{q_n}-\frac{|L|}{B}\right).
$$



Using



$$
\frac{E_n}{q_n}\le e\,n^{-2n-1}
$$



and



$$
\frac{|L|}{B}\ge c_\pi B^{-31/5-1}
=c_\pi B^{-36/5},
$$



the ratio of the exponential component to the pi-form component obeys



$$
0\le
\frac{E_n/q_n}{|L|/B}
\le c_\pi^{-1}e\,B^{36/5}n^{-2n-1}.
$$



This confirms that $36/5$, rather than $31/5$, is the cancellation
exponent: comparing component values introduces one additional division
by $B$.

If $\log B=o(n\log n)$, the logarithm of the right side is



$$
\frac{36}{5}\log B-(2n+1)\log n+O(1)\longrightarrow-\infty.
$$



The ratio is eventually at most $1/2$. The pi-form component then
dominates, and the same content calculation as in the same-sign branch
gives



$$
\left|\Lambda_n^{\rm prim}\right|
\ge\frac{c_\pi}{2}\frac{q_n}{B^{41/5}}.
$$



If genuine cancellation remains competitive, so that the component ratio
exceeds $1/2$, its upper bound forces



$$
B^{36/5}\gg n^{2n+1}.
$$



Taking logarithms gives



$$
\log B
\ge\frac5{36}(2n+1)\log n-O(1)
\ge\frac5{18}n\log n-O(\log n).
$$



Hence



$$
B\ge n^{\,5n/18-o(n)}.
$$



The necessary cancellation scale $5/18$ is correct. In particular, all
bounded branches require at least the $5/41$ scale; the stronger
$5/18$ scale is necessary only if opposite-sign cancellation itself
stays competitive.

## 6. Critical Fourier region and the constant $1/35$

In the accepted even-$n$, $k>n$ Fourier family, only same-sign
matching occurs, and the primitive pi coefficient satisfies



$$
B_{n,k}\le64^{k-1}\gamma^n,
\qquad
\gamma=\frac{1+\sqrt2}{2}.
$$



Combining this with $q_n\ge n^n$ and the $41/5$ lower bound yields



$$
\log|\Lambda_{n,k}^{\rm prim}|
\ge
n\log n
-\frac{41}{5}(k-1)\log64
-\frac{41}{5}n\log\gamma
+\log c_\pi.
$$



This is exactly equation (17) of the source, with its $O(1)$ term equal
to the fixed constant $\log c_\pi$.

The elementary estimate $\log2<7/10$ can be certified without decimal
approximation because



$$
e^{7/10}>
1+\frac7{10}+\frac{(7/10)^2}{2}
+\frac{(7/10)^3}{6}
=\frac{12013}{6000}>2.
$$



Therefore



$$
\frac{41}{5}\log64
=\frac{246}{5}\log2
<\frac{246}{5}\frac7{10}
=\frac{861}{25}
<35.
$$



If



$$
k\le\frac1{35}n\log n,
$$



then



$$
\begin{aligned}
\log|\Lambda_{n,k}^{\rm prim}|
&\ge
\left(
1-\frac{(41/5)\log64}{35}
\right)n\log n\\
&\quad-\frac{41}{5}n\log\gamma+O(1).
\end{aligned}
$$



The displayed coefficient of $n\log n$ is not merely positive; the
rational estimate above gives the explicit margin



$$
1-\frac{(41/5)\log64}{35}
>
1-\frac{861}{875}
=\frac{14}{875}.
$$



Since $\gamma$ is a fixed positive constant, the gamma loss is exactly
$O(n)$. Thus



$$
\log|\Lambda_{n,k}^{\rm prim}|
>
\frac{14}{875}n\log n
-\frac{41}{5}n\log\gamma+O(1)
\longrightarrow+\infty.
$$



This proves divergence throughout



$$
n<k\le\frac1{35}n\log n
$$



for all sufficiently large even $n$. The lower restriction $k>n$
only selects the automatic Fourier region and is compatible with the
upper restriction once $n$ is sufficiently large. No hidden
$n\log n$ contribution is present in the gamma factor.

## 7. Primary source and exact scope

The primary source checked was D. Zeilberger and W. Zudilin,
The irrationality measure of pi is at most
$7.103205334137\ldots$, Moscow Journal of Combinatorics and Number
Theory 9 (2020), 407--419:

* <https://arxiv.org/abs/1912.06345>;
* <https://doi.org/10.2140/moscow.2020.9.407>.

The paper's definition explicitly quantifies over all integer numerators,
which validates the source's sign and non-coprime-denominator conversion.
The final theorem gives the claimed numerical upper bound.

The accepted sharpening is a no-go theorem for the stated matching
families. It neither proves success beyond $k=n\log n/35$ nor proves
that $e+\pi$ is algebraic or transcendental.
