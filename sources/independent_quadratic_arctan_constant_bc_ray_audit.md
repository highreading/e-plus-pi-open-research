> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the constant-(B,C) quadratic pullback ray

Date: 2026-08-26

Accepted source snapshot:

```text
9c4b35483a592857f1eab25741fc8ae5b813a5110df0f7212d77b9ed658b091a  sources/quadratic_arctan_constant_bc_ray.md
```

The initially presented snapshot was

```text
8f1a6fe45123d41a0aefd5438f0dbb2ba21112052bcad93187a20deb1d4ef4e3  sources/quadratic_arctan_constant_bc_ray.md
```

I made one local edge-case correction before acceptance: the definition
(M=\lfloor(a-1)/2\rfloor) and its common-denominator display are now stated
for (a\geq1), while (a=0) is recorded separately as
$\Pi_{p,0}=0,D_{p,0}=1$.  The original asymptotic theorem was unaffected.
No other source text was changed.

## Verdict

**Accept.**  The completely reduced endpoint form is exactly the reduced
rational approximant denominator times its error.  The denominator of the
truncated (F_p) series is at most exponential in (a), whereas the reduced
denominator of the exponential truncation is at least



$$
\exp\!\left(\frac12a\log a-O(a)\right).
$$



The elementary common-denominator lemma transfers this lower bound, up to an
exponential loss, to the completely primitive endpoint coefficient.  Finally,
the exponent-(36/5) rational-approximation consequence of the known finite
irrationality measure of $\pi$ prevents the (e)-tail from cancelling the
$F_p$-tail.  The resulting primitive form satisfies



$$
|\mathcal L_{p,a}|
 \geq\exp\!\left(\frac12a\log a-O_p(a)\right)
 \longrightarrow\infty.
$$



No sign hypothesis on the (F_p) tail and no unproved gcd estimate is hidden
in the argument.  This is a theorem only for the fixed-(B,C) ray in the
source; it has no consequence by itself for the arithmetic nature of
(e+\pi).

## 1. The endpoint primitive reduction is exact

Maximal cancellation with (B=C=1) forces



$$
A_a=-T_a(e^z+F_p(z)).
$$



Writing



$$
E_a=\sum_{k=0}^a\frac1{k!},\qquad
 \Pi_{p,a}=T_aF_p(1),\qquad
 R_{p,a}=E_a+\Pi_{p,a}=\frac{P_{p,a}}{Q_{p,a}}
$$



with $\gcd(P_{p,a},Q_{p,a})=1$, (Q_{p,a}>0), the unscaled endpoint is



$$
(e+\pi)-R_{p,a}.
$$



It is worth checking explicitly that clearing every coefficient of the
polynomial triple and then taking the endpoint gcd gives exactly the pair
$(-P_{p,a},Q_{p,a})$.  Let (L>0) clear all coefficients of (A_a).
Because (A_a(1)=-R_{p,a}), one has (LR_{p,a}\in\mathbb Z\).  Coprimality of
(P_{p,a},Q_{p,a}) implies (Q_{p,a}\mid L); write (L=hQ_{p,a}).  The raw
integer endpoint pair is then



$$
(-hP_{p,a},hQ_{p,a}),
$$



whose full coordinate gcd is exactly (h).  Hence primitive reduction gives



$$
\mathcal L_{p,a}=Q_{p,a}(e+\pi)-P_{p,a},
\qquad
 |\mathcal L_{p,a}|=Q_{p,a}|(e+\pi)-R_{p,a}|.   \tag{A1}
$$



This proves the normalization assertion without any conjectural formula for
the coefficient gcd.

## 2. Exponential upper bound for the (F_p)-truncation denominator

For fixed integer (p\geq2), direct differentiation gives



$$
F_p'(z)=
 \frac{4(p-1)(p+z^2)}
 {z^4+(p^2-4p+1)z^2+p^2}.
$$



If



$$
c_{p,0}=1,\quad c_{p,1}=-p^2+5p-1,
$$





$$
c_{p,m}=-(p^2-4p+1)c_{p,m-1}-p^2c_{p,m-2},
$$



then coefficient comparison and integration from (0) give



$$
F_p(z)=\sum_{m\geq0}
 \frac{4(p-1)c_{p,m}}
 {p^{2m+1}(2m+1)}z^{2m+1}.                     \tag{A2}
$$



For (a\geq1), put (M=\lfloor(a-1)/2\rfloor).  Every term retained in
$\Pi_{p,a}$ has (m\leq M).  Its denominator divides



$$
p^{2m+1}(2m+1),
$$



and each such integer divides



$$
H_{p,a}:=p^{2M+1}\operatorname{lcm}(1,2,\ldots,2M+1). \tag{A3}
$$



Therefore the reduced denominator (D_{p,a}) of (Pi_{p,a}) divides
(H_{p,a}).  Since (2M+1\leq a) and the elementary Chebyshev bound is



$$
\log\operatorname{lcm}(1,\ldots,n)=O(n),
$$



one obtains



$$
\log D_{p,a}leq(2M+1)\log p+O(M)=O_p(a).      \tag{A4}
$$



The argument needs only divisibility by a common denominator; possible
cancellation inside individual terms or in their sum can only decrease
(D_{p,a}).  At (a=0), (D_{p,0}=1), consistent with (A4) after treating
that single case separately.

## 3. Continued fractions force a large denominator for (E_a)

The rational-approximation input for (e) can be proved directly from
Euler's continued fraction



$$
e=[2;1,2,1,1,4,1,1,6,1,\ldots].
$$



There is an absolute (c_e>0) such that every reduced (r/q), (q\geq1),
satisfies



$$
\left|e-\frac rq\right|
 \geq\frac{c_e}{q^2\log(2q)}.                  \tag{A5}
$$



Here is the full short proof.  If
$|e-r/q|\geq1/(2q^2)$, (A5) follows after decreasing the absolute constant.
Otherwise Legendre's criterion makes (r/q=P_k/Q_k) a continued-fraction
convergent of (e).  The standard lower estimate for a convergent is



$$
\left|e-\frac{P_k}{Q_k}\right|
 >\frac1{Q_k(Q_{k+1}+Q_k)}
 >\frac1{(a_{k+1}+2)Q_k^2}.                    \tag{A6}
$$



Euler's pattern gives (a_{k+1}=O(k)).  Since every partial quotient is at
least one, (Q_k\geq F_{k+1}), so (k=O(\log(2Q_k))\).  Equations (A5)--(A6)
follow, with finitely many initial denominators absorbed into (c_e).

Now reduce



$$
E_a=\frac{r_a}{q_a}.
$$



The Taylor tail obeys



$$
\frac1{(a+1)!}<e-E_a<\frac2{(a+1)!}.          \tag{A7}
$$



Also (q_a\mid a!\), hence (q_a\leq a!\).  Applying (A5) to (E_a) and
using (A7) gives



$$
\frac{c_e}{q_a^2\log(2q_a)}<\frac2{(a+1)!}.
$$



Replacing (log(2q_a)) by the upper bound (log(2a!)) yields



$$
q_a^2>
 \frac{c_e(a+1)!}{2\log(2a!)}.
$$



Consequently



$$
\log q_a
 \geq\frac12\log((a+1)!)-\frac12\log\log(2a!)-O(1)
 =\frac12a\log a-O(a).                         \tag{A8}
$$



This proves the claimed superexponential lower bound.  Notice that the
trivial upper bound (q_a\leq a!\) is used only inside a logarithm; no exact
formula for (q_a) is assumed.

## 4. The denominator-transfer lemma

Write the two other reduced fractions as



$$
\Pi_{p,a}=\frac{u_{p,a}}{D_{p,a}},\qquad
 R_{p,a}=\frac{P_{p,a}}{Q_{p,a}}.
$$



Because



$$
E_a=R_{p,a}-\Pi_{p,a},
$$



the right side can be written over



$$
L=\operatorname{lcm}(Q_{p,a},D_{p,a}).
$$



After reducing that fraction, its denominator (q_a) must divide (L).
Thus, without any coprimality assumption between (Q_{p,a}) and (D_{p,a}),



$$
q_a\mid\operatorname{lcm}(Q_{p,a},D_{p,a}),
 \qquad
 q_a\leq Q_{p,a}D_{p,a}.                       \tag{A9}
$$



Combining (A4), (A8), and (A9) gives



$$
\log Q_{p,a}
 \geq\log q_a-\log D_{p,a}
 \geq\frac12a\log a-O_p(a).                   \tag{A10}
$$



This is exactly the denominator lemma and its intended use.  An unexpectedly
large gcd in the initially cleared endpoint triple has already been removed
in (A1), and cannot invalidate (A10).

## 5. The two analytic tails cannot cancel

Zeilberger and Zudilin proved



$$
\mu(\pi)\leq7.1032053341370017\ldots .
$$



The chosen exponent



$$
\tau=\frac{36}{5}=7.2
$$



is strictly larger.  By the definition of an upper bound for the
irrationality measure, for every sufficiently large denominator (D) and
every integer (u),



$$
\left|\pi-\frac uD\right|>D^{-36/5}.
$$



The finitely many smaller (D)'s can be absorbed into a positive constant:
for each fixed (D), irrationality of $\pi$ makes
$\operatorname{dist}(D\pi,\mathbb Z)>0$.  Hence there is a uniform
(c_\pi>0) such that every reduced (u/D) satisfies



$$
\left|\pi-\frac uD\right|\geq c_\pi D^{-36/5}. \tag{A11}
$$



This implication and the numerical gap (7.103205\ldots<7.2) were already
audited independently in
`sources/independent_improved_pi_measure_matching_sharpening_audit.md`.
The primary reference is D. Zeilberger and W. Zudilin,
[*The Irrationality Measure of Pi is at most
7.103205334137...*](https://arxiv.org/abs/1912.06345).

Apply (A11) to the reduced rational (Pi_{p,a}).  By (A4), there is a
constant (C_p>0) such that



$$
|\pi-\Pi_{p,a}|
 \geq c_\pi D_{p,a}^{-36/5}
 \geq\exp(-C_pa).                               \tag{A12}
$$



On the other hand, (A7) and Stirling's formula give



$$
0<e-E_a=\exp(-a\log a+O(a)).                  \tag{A13}
$$



In particular, for all sufficiently large (a),



$$
|e-E_a|\leq\frac12\exp(-C_pa)
 \leq\frac12|\pi-\Pi_{p,a}|.
$$



The reverse triangle inequality, with no sign assumption on either tail,
then yields



$$
\begin{aligned}
 |(e+\pi)-R_{p,a}|
 &=|(e-E_a)+(\pi-\Pi_{p,a})|\\
 &\geq|\pi-\Pi_{p,a}|-|e-E_a|\\
 &\geq\exp(-O_p(a)).                            \tag{A14}
 \end{aligned}
$$



The factor (1/2) has merely been absorbed into the (O_p(a)) term.  Finally,
(A1), (A10), and (A14) prove



$$
|\mathcal L_{p,a}|
 \geq
 \exp\!\left(\frac12a\log a-O_p(a)\right)
 \longrightarrow\infty.
$$



This verifies the cancellation step and completes the independent proof.

## 6. Finite exact implementation check

A separate program, not used in the proof, recomputed (E_a),
\(Pi_{p,a}), and (R_{p,a}) directly with `Fraction` arithmetic for



$$
p=2,3,4,5,\qquad0\leq a\leq100.
$$



For all 404 records it checked exactly that



$$
D_{p,a}\mid H_{p,a}\quad(a\geq1),
\qquad
 q_a\mid\operatorname{lcm}(Q_{p,a},D_{p,a}),
\qquad
 q_a\leq Q_{p,a}D_{p,a}.
$$



These checks are finite diagnostics only.  The all-degree theorem is supplied
by Sections 1--5.

Independent artifacts:

```text
9cbb4ea5d5571406b70ae8b9aa6cea1badb644bd0d26496759ac8921d23420e1  scripts/quadratic_arctan_constant_bc_independent_audit.py
de96a55d12bc72c6da24b4838cc4fd53f4c86bc65d8e2f0dffc17c4109e5b58e  results/quadratic_arctan_constant_bc_independent_audit_a100.json
```

Relevant earlier independent inputs, frozen at audit time:

```text
4a38783099572a27934b5794cb52b4f9d072873a8dbe961cb5870e08f67c1eb2  sources/independent_positive_derivative_kernel_divergence_audit.md
197abd5ceebd5314eb1ab7ed1c6463f11b6dcb5b934c733e5e88abfcbb9f2d22  sources/independent_improved_pi_measure_matching_sharpening_audit.md
```
