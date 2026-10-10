> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the positive derivative-kernel divergence theorem

Date: 2026-08-26

## Frozen object and verdict

I audited the current version of

**sources/positive_derivative_kernel_divergence.md**

with SHA-256

    c3b1b0493a66b781324c28014058675f92bf529ec46ff1eff87ce64af1e3965b

This is the version after the two typographical $\backslash\mathrm{quad}$
repairs mentioned in the audit request.  I did not edit it.

**Verdict: accepted.**  I independently rederived every identity and every
inequality used in the theorem.  I found no sign error, missing denominator,
uncontrolled gcd, or exceptional case.  In particular, the proof does not
assume any of the experimentally observed gcds to equal one.  The possible
case $M_n=0$ is also covered by the content argument.

The conclusion is deliberately narrow: this is a rigorous divergence
theorem for one proposed family, not a result about the arithmetic nature of
$e+\pi$.

## 1. Reduction of the interpolation ratio

Let



$$
A=13^3 239^2=125494837.
$$



Direct cancellation gives



$$
\frac{239^2\,57122}{25\,26}
 =\frac{239^2(26\cdot13^3/26)}{25}
 =\frac{A}{25}.
$$



Since $5\nmid A$, raising this reduced fraction to $m=n/2$ gives



$$
a_n=A^m,\qquad b_n=25^m=5^n,
$$



exactly as claimed.

For the linear polynomial before primitive reduction, Euclid's algorithm
gives



$$
\begin{aligned}
 &\gcd(a_n-b_n,57121a_n-25b_n)\\
 &\quad=\gcd(a_n-b_n,57096a_n)
 =\gcd(a_n-b_n,57096),
\end{aligned}
$$



because $\gcd(a_n,a_n-b_n)=\gcd(a_n,b_n)=1$.

The relevant exact factorizations are



$$
\begin{aligned}
 57096&=2^3 3^2 13\,61,\\
 A-25&=2^2 3^3 43\,61\,443,\\
 A+25&=2\,113\,555287.
\end{aligned}
$$



For $3$ and $61$, odd-prime LTE gives



$$
v_3(A^m-25^m)=3+v_3(m),\qquad
 v_{61}(A^m-25^m)=1+v_{61}(m).
$$



After truncating at the valuations in $57096$, these contribute $3^2$
and $61$ for every $m\geq1$.  The prime $13$ contributes nothing,
because $13\mid A$ and $13\nmid25$.  For the prime $2$, odd $m$
gives



$$
v_2(A^m-25^m)=v_2(A-25)=2,
$$



whereas even $m$ gives



$$
v_2(A^m-25^m)
 =v_2(A-25)+v_2(A+25)+v_2(m)-1
 =2+v_2(m)\geq3.
$$



Truncation at $v_2(57096)=3$ therefore proves



$$
\delta_n=
 \begin{cases}
  2^2 3^2 61=2196,&m\text{ odd},\\
  2^3 3^2 61=4392,&m\text{ even}.
 \end{cases}
$$



Thus $u_n=(a_n-b_n)/\delta_n$ and
$v_n=(57121a_n-25b_n)/\delta_n$ are coprime.  The factors
$x^{2n}$, $(1-x^2)^n$, and $(u_nx^2+v_n)^2$ are primitive integer
polynomials, so Gauss's lemma proves that their product $P_n$ is primitive.
For positive even $n$, every factor has nonnegative value on the real
axis after the square or even power is taken, and the polynomial is nonzero.

## 2. Exact pole interpolation

Substitution in the primitive linear factor gives



$$
\ell_n(-25)=\frac{57096a_n}{\delta_n},\qquad
 \ell_n(-57121)=\frac{57096b_n}{\delta_n}.
$$



Because $n$ is even,



$$
P_n(5i)
 =650^n\left(\frac{57096a_n}{\delta_n}\right)^2.
$$



At the second pole,



$$
P_n(239i)
 =(57121\,57122)^n
 \left(\frac{57096b_n}{\delta_n}\right)^2.
$$



The equality of these expressions is equivalent to



$$
\left(\frac{a_n}{b_n}\right)^2
 =\left(\frac{57121\,57122}{650}\right)^n,
$$



which follows from
$a_n/b_n=(57121\,57122/650)^{n/2}$.  Hence the common integer $T_n$
in the source is exact after primitive reduction.

## 3. Coordinate formulas and signs

Writing $y=x^2$, expansion of



$$
y^n(1-y)^n(u_ny+v_n)^2
$$



gives precisely the three binomial terms in equation (14), with degrees
$n\leq k\leq2n+2$.  For every nonnegative integer $j$, direct
integration by parts gives



$$
\int_0^1x^je^x\,dx
 =(-1)^j\bigl(!j\,e-j!\bigr).
$$



All exponents used here are even, so summing this identity proves
$I_{e,n}=q_ne-p_n$ with the stated integer coordinates.

The two moment identities



$$
j!=\int_0^\infty e^{-t}t^j\,dt,
 \qquad
 !j=\int_0^\infty e^{-t}(t-1)^j\,dt
$$



show, after termwise summation, that



$$
p_n=\int_0^\infty e^{-t}P_n(t)\,dt>0,
 \qquad
 q_n=\int_0^\infty e^{-t}P_n(t-1)\,dt>0.
$$



Strictness holds because a nonzero polynomial has only finitely many zeros.
Dividing by $\gcd(p_n,q_n)$ therefore produces a positive primitive form
$\bar q_ne-\bar p_n$, without any claim about the size of that gcd.

Now regard $P_n$ as an integer polynomial $F_n(y)$.  Since
$F_n(-s^2)=T_n$ for $s=5,239$, monic Euclidean division proves



$$
\frac{F_n(y)-T_n}{y+s^2}\in\mathbb Z[y].
$$



Coefficient comparison from the leading term downward gives exactly the
recurrence (19), including the constant check
$c_{n,0}-T_n=s^2h_{s,n,0}$.

Consequently



$$
\int_0^1\frac{P_n(x)}{x^2+s^2}\,dx
 =\sum_j\frac{h_{s,n,j}}{2j+1}
  +\frac{T_n}{s}\arctan(1/s).
$$



Multiplication by $80$ and $-956$ changes the two arctangent coefficients
to $16T_n$ and $-4T_n$.  Machin's identity therefore gives exactly



$$
I_{\pi,n}=\rho_n+T_n\pi.
$$



The maximum denominator is $4n+3$, so the lcm in equation (21) clears
every denominator.  Primitive reduction in (23) is valid even in the
hypothetical case $A_n^{(0)}=0$, under the standard convention
$\gcd(0,B)=B$.

Finally, direct combination of the two fractions in $G'$ gives



$$
G'(x)=\frac{4545780-876x^2}
 {(x^2+25)(x^2+57121)}.
$$



Its numerator is already positive at $x=1$, hence throughout
$[0,1]$.  This verifies $I_{\pi,n}>0$ and the sign of the primitive
$\pi$-form.

## 4. The exponential gcd is bypassed correctly

For a reduced rational $p/q$, Legendre's criterion splits the proof into
two cases.  If it is not forced to be a convergent of $e$, then



$$
\left|e-\frac pq\right|\geq\frac1{2q^2}.
$$



For a convergent $P_k/Q_k$, the standard continued-fraction inequalities
give



$$
\left|e-\frac{P_k}{Q_k}\right|
 >\frac1{Q_k(Q_{k+1}+Q_k)}
 >\frac1{(a_{k+1}+2)Q_k^2}.
$$



Euler's continued fraction has $a_{k+1}=O(k)$, while
$Q_k\geq F_{k+1}$, so $k=O(\log(2Q_k))$.  Decreasing one absolute
constant to absorb the finitely many initial cases proves



$$
\left|e-\frac pq\right|
 \geq\frac{c_e}{q^2\log(2q)}
 \geq\frac{c_e}{q^3}.
$$



Because primitive reduction does not change the rational number,
$\bar p_n/\bar q_n=p_n/q_n$.  On $[0,1]$, one has
$0\leq x^{2n}(1-x^2)^n\leq1$, $e^x\leq e$, and
$0<\ell_n(x^2)\leq u_n+v_n$, hence



$$
I_{e,n}\leq e(u_n+v_n)^2.
$$



Moreover,



$$
\frac{u_n+v_n}{u_n}
 =57122+\frac{57096b_n}{a_n-b_n}<57123,
$$



because $a_n/b_n\geq A/25>57097$.

In the moment integral for $q_n$, put $x=t-1$ and restrict $x$ to
$[4n+4,4n+5]$.  There



$$
x^2-1\geq\frac{x^2}{2},\qquad
 u_nx^2+v_n\geq u_nx^2,
$$



so



$$
q_n\geq2^{-n}u_n^2e^{-(4n+6)}(4n+4)^{4n+4}.
$$



Division gives equation (31).  Applying the $q^{-3}$ lower bound to the
reduced fraction $\bar p_n/\bar q_n$ then gives equation (32) with every
power in the correct direction.  Taking logarithms yields



$$
\log\bar q_n\geq\frac43n\log n-O(n).
$$



Thus the unknown $g_{e,n}$ is genuinely eliminated rather than estimated.

## 5. Exponential upper bound for the primitive pi coefficient

Primitive reduction can only decrease $B_n$, and



$$
T_n
 =650^n\left(\frac{57096a_n}{\delta_n}\right)^2
 \leq57096^2(650A)^n,
$$



because $a_n^2=A^n$.  For completeness, the lcm estimate used in the
source has an elementary proof.  If
$\vartheta(N)=\sum_{p\leq N}\log p$, strong induction gives



$$
\vartheta(N)\leq2N\log2.
$$



Indeed, for $N=2m$, every prime in $(m,2m]$ divides
$\binom{2m}{m}<2^{2m}$, and the induction bound for
$\vartheta(m)$ completes the step.  For $N=2m+1$, every prime in
$(m+1,2m+1]$ divides $\binom{2m+1}{m}$; the two equal central
coefficients show
$\binom{2m+1}{m}<2^{2m}=2^{N-1}$, while the induction bound for
$\vartheta(m+1)$ supplies the remaining $(N+1)\log2$.  The total in
both parity cases is at most $2N\log2$.

Since


$$
\log\operatorname{lcm}(1,\ldots,N)
=\sum_{k\geq1}\vartheta(N^{1/k})
$$

, and a term with index $k$ occurs
only when $2^k\leq N$, one has
$N^{1/k}\leq N/2^{k-1}$.  Thus



$$
\log\operatorname{lcm}(1,\ldots,N)
 \leq2\log2\sum_{k\geq1}N^{1/k}
 \leq4N\log2.
$$



Exponentiation proves the claimed estimate



$$
\operatorname{lcm}(1,2,\ldots,N)\leq16^N
$$



and also shows directly why a fixed exponential base is available.
With $N=4n+3$, this gives exactly



$$
B_n\leq16^{4n+3}57096^2(650A)^n=C_0C_1^n.
$$



Only the conclusion $\log B_n=O(n)$ is used later.  No lower bound for
$B_n$ or any information about $g_{\pi,n}$ enters the argument.

## 6. Prime-power content, including the case M=0

Write



$$
\bar q_n=d_nq_{0,n},\qquad B_n=d_nB_{0,n},
 \qquad\gcd(q_{0,n},B_{0,n})=1.
$$



The least positive multipliers that make the two transcendental
coefficients equal are $B_{0,n}$ and $q_{0,n}$.  Therefore the matched
constant and coefficient are indeed



$$
M_n=-B_{0,n}\bar p_n+q_{0,n}A_n,
 \qquad C_n=d_nq_{0,n}B_{0,n}.
$$



Let $r$ be a prime divisor of $q_{0,n}$.  Since
$\gcd(q_{0,n},B_{0,n})=1$ and
$\gcd(\bar p_n,\bar q_n)=1$, reduction modulo $r$ gives



$$
M_n\equiv-B_{0,n}\bar p_n\not\equiv0\pmod r.
$$



Similarly, if $r\mid B_{0,n}$, then primitivity of $(A_n,B_n)$ gives



$$
M_n\equiv q_{0,n}A_n\not\equiv0\pmod r.
$$



Hence



$$
\gcd(M_n,q_{0,n}B_{0,n})=1.
$$



This also handles $M_n=0$: in that case the displayed gcd forces
$q_{0,n}B_{0,n}=1$.  It is therefore not legitimate to regard zero as an
exception to the proof.

For each prime, either it divides $q_{0,n}B_{0,n}$, in which case it does
not divide $M_n$, or its valuation in $C_n$ is at most its valuation in
$d_n$.  Consequently the full content, with prime powers retained,
satisfies



$$
g_n=\gcd(|M_n|,C_n)\mid d_n.
$$



No square-free shortcut and no empirical gcd assertion is being used.

## 7. Final lower bound and exponent audit

Both addends in the matched form are positive.  Since
$q_{0,n}=\bar q_n/d_n$, $g_n\leq d_n$, and $d_n\leq B_n$,



$$
\frac{q_{0,n}}{g_n}
 =\frac{\bar q_n}{d_ng_n}
 \geq\frac{\bar q_n}{d_n^2}
 \geq\frac{\bar q_n}{B_n^2}.
$$



Salikhov's bound $\mu(\pi)<8$ implies, after choosing exponent $8$ and
absorbing finitely many denominators into one positive constant,



$$
|A+B\pi|\geq c_\pi B^{-7}
 \qquad(A\in\mathbb Z,\ B\geq1).
$$



This remains valid when $A/B$ is not reduced: reduction only replaces
$B$ by a denominator no larger than $B$.  Applying the inequality to
the primitive positive form $L_{\pi,n}$ gives



$$
\frac{\mathcal W_n}{g_n}
 \geq\frac{q_{0,n}L_{\pi,n}}{g_n}
 \geq c_\pi\frac{\bar q_n}{B_n^9}.
$$



Combining
$\log\bar q_n\geq(4/3)n\log n-O(n)$ with
$\log B_n=O(n)$ proves



$$
\frac{\mathcal W_n}{g_n}
 \geq c\exp\left(\frac43n\log n-Cn\right)
$$



for constants independent of positive even $n$.  The claimed divergence
follows.

## 8. Independent exact finite reproduction

I also wrote a separate exact implementation:

**scripts/independent_positive_derivative_kernel_audit.py**

It constructs $F_n(y)$ by SymPy symbolic expansion and obtains both
quadratic quotients by SymPy Euclidean polynomial division.  This is
independent of the hand-coded coefficient convolution and synthetic
division used by the primary script.  It then recomputes the factorial and
derangement coordinates, both primitive reductions, minimal matching, and
final content with exact integers and rationals.  No numerical values of
$e$ or $\pi$ are used.

For every even $n=2,4,\ldots,20$, all exact coordinate digests agree with
the primary result.  The independently recovered matching gcds are $29$
at $n=8$, $53$ at $n=18$, and $1$ in the other eight cases.  All ten
final contents are $1$.  These checks corroborate the formulas but are not
used to prove the all-$n$ theorem.

The independent result is stored in

**results/independent_positive_derivative_kernel_audit.json**.

## Artifact hashes at audit completion

- Audited theorem source:
  c3b1b0493a66b781324c28014058675f92bf529ec46ff1eff87ce64af1e3965b
- Primary probe script:
  3048f8264ded1ffb9f2cbdf9cf5512b3ba5524dc64b28c62feb30c37f7191cb7
- Primary probe result:
  dbf8ed56a73e82edf534e6f7d34b2d776b22a69a890921543429e0a14e181965
- Independent audit script:
  ae7c56a46371e636224a32088bdf8e7f2d5acbb1b9ed0bfde979e8d66308317a
- Independent audit result:
  c1544c2ca8b09188221c21a47e400f3005b9aa87a240922e6f6866ed8e7804d4

The audit-note hash is intentionally omitted from its own body and is
reported separately after validation.
