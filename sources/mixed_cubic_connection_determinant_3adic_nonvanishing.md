> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Uniform 3-adic nonvanishing of the fixed-gap connection determinant

Date: 2026-08-28

## 1. Statement

Let $q$ be a positive odd integer with $3\nmid q$, and put



$$
n=q-1,\qquad r=\frac{q-1}{2},\qquad A=2q-3,
 \qquad D(k)=k+v_3(k!).
$$



Define the four rational coefficients



$$
\begin{aligned}
C_0(q)&=[z^n](2+z)
 \bigl((1+z)(1+z+z^2/2)\bigr)^{A/3},\\
C_1(q)&=\frac12[z^n](2+z)^4
 \bigl((1+z)(1+z+z^2/2)\bigr)^{A/3-1},\\
T_0(q)&=[z^n]\frac{(1+z)(1+z^2)^{A/3}}{(1-z)^q},\\
T_1(q)&=[z^n]\frac{(1+z)^4(1+z^2)^{A/3-1}}{(1-z)^q}.
\end{aligned}                                                    \tag{1}
$$



These are exactly the full-and-tail quantities in the fixed-gap reduction.
Their connection determinant is



$$
\mathcal R_q=C_0(q)T_1(q)-C_1(q)T_0(q).             \tag{2}
$$



Here $v_3$ is the additive 3-adic valuation on nonzero rational numbers,
normalized by $v_3(3)=1$.

**Theorem.** For every positive odd $q$ with $3\nmid q$,



$$
\boxed{v_3(\mathcal R_q)=1-D(q-1)-D((q-1)/2).}       \tag{3}
$$



In particular, $\mathcal R_q\ne0$ for every admissible fixed gap. Thus
the nonvanishing hypothesis in the fixed-gap meta-theorem is automatic.

## 2. The unique maximal 3-adic terms

Work in the localization $\mathbb Z_{(3)}$, so congruences modulo $9$
are meaningful for rationals whose denominators are prime to $3$. For
$k\ge0$, set



$$
b_k=3^{D(k)}\binom{A/3}{k}.
$$



Since $3\nmid A$,



$$
\binom{A/3}{k}
 =\frac{\prod_{j=0}^{k-1}(A-3j)}{3^k k!},
$$



and every factor in the numerator is a 3-adic unit. Consequently



$$
v_3\!\binom{A/3}{k}=-D(k),\qquad
 b_k\in\mathbb Z_{(3)}^\times.                       \tag{4}
$$



Also



$$
D(k)-D(k-1)=1+v_3(k).                               \tag{5}
$$



Write



$$
(1+z)(1+z+z^2/2)=1+u(z),\qquad
 u(z)=2z+\frac32z^2+\frac12z^3.                      \tag{6}
$$



Expanding $(1+u)^{A/3}$, the term indexed by $k$ in $C_0$ has
3-adic denominator exactly $3^{D(k)}$, up to a factor in
$\mathbb Z_{(3)}$. Because $u$ has order one in $z$, only $k\le n$
can contribute. After multiplication by $3^{D(n)}$, every term
$k\le n-2$ is therefore zero modulo $9$. The same argument in $T_0$,
where $(1+z^2)^{A/3}$ has $k\le r$, shows that after multiplication
by $3^{D(r)}$, every term $k\le r-2$ is zero modulo $9$. This is
rigorous because $D(s)-D(k)\ge s-k$.

The shifted exponent is controlled exactly by



$$
\binom{A/3-1}{k}
 =\frac{A-3k}{A}\binom{A/3}{k}.                     \tag{7}
$$



Since both $A$ and $A-3k$ are 3-adic units, the shifted binomial in
(7) has the same valuation $-D(k)$. Thus the same two-term truncation
applies to $C_1$ and $T_1$, not only to $C_0$ and $T_0$. All
remaining coefficient multipliers in (1) have denominators that are
powers of $2$, hence are 3-adically integral.

If $q\equiv1\pmod6$, then $3\mid n$ and $3\mid r$. Equation (5)
shows that even the $n-1$ and $r-1$ terms acquire at least two powers
of $3$, so only the top terms survive modulo $9$. If
$q\equiv5\pmod6$, neither $n$ nor $r$ is divisible by $3$, so the
top two terms survive and all earlier terms vanish.

## 3. The class $q\equiv1\pmod6$

Put



$$
C_s^\sharp=3^{D(n)}C_s,\qquad
 T_s^\sharp=3^{D(r)}T_s.                             \tag{8}
$$



Thus every unit factor used below is explicit: $b_n,b_r$ are the units
from (4), while $A$, $q$, $q-3$, and $2$ are also 3-adic units in
this congruence class. The top coefficients in (6), together with (7),
give modulo $9$



$$
\begin{aligned}
C_0^\sharp&\equiv 2^{n+1}b_n,
&C_1^\sharp&\equiv-2^{n+3}\frac qA b_n,\\
T_0^\sharp&\equiv b_r,
&T_1^\sharp&\equiv\frac{q-3}{2A}b_r.                \tag{9}
\end{aligned}
$$



For example, the factor $2^{n+3}$ is the constant coefficient $8$
of $(2+z)^4/2$, multiplied by $[z^n]u^n=2^n$. Since
$n\equiv0\pmod6$, one has $2^n\equiv1\pmod9$. From (9),



$$
\begin{aligned}
C_0^\sharp T_1^\sharp-C_1^\sharp T_0^\sharp
&\equiv b_nb_r\frac{2^n}{A}\bigl((q-3)+8q\bigr)\\
&=3b_nb_r\frac{2^n(3q-1)}A\pmod9.                  \tag{10}
\end{aligned}
$$



Now $A\equiv2\pmod3$ and $3q-1\equiv2\pmod3$. Hence



$$
b_nb_r\,\frac{2^n(3q-1)}A\in\mathbb Z_{(3)}^\times
$$



is an explicitly displayed unit. The normalized determinant in (10) has
valuation exactly one. The same computation includes $q=1$
($n=r=0$); in that case it gives the exact value
$\mathcal R_1=-6$.

## 4. The class $q\equiv5\pmod6$

Here $n\equiv4\pmod6$, $r\equiv2\pmod3$, and the adjacent-binomial
ratios are



$$
\frac{\binom{A/3}{n-1}}{\binom{A/3}{n}}
 =-\frac{3n}{q-3},\qquad
 \frac{\binom{A/3}{r-1}}{\binom{A/3}{r}}
 =\frac{3(q-1)}{q+3}.                               \tag{11}
$$



The required top and next-to-top polynomial coefficients are



$$
\begin{array}{c|cc}
 &k=n&k=n-1\\ \hline
(2+z)u^k&2^{n+1}&2^{n-2}(3n-1)\\
\frac12(2+z)^4u^k&2^{n+3}&2^n(3n+5),
\end{array}                                         \tag{12}
$$



and



$$
\begin{aligned}
[z^0](1+z)(1-z)^{-q}&=1,&
[z^2](1+z)(1-z)^{-q}&=\frac{q(q+3)}2,\\
[z^0](1+z)^4(1-z)^{-q}&=1,&
[z^2](1+z)^4(1-z)^{-q}&=\frac{q^2+9q+12}2.          \tag{13}
\end{aligned}
$$



Using (7), (11)--(13), and dividing only by the explicit units $b_n,b_r$,
gives the complete two-term reductions modulo $9$:



$$
\begin{aligned}
\frac{C_0^\sharp}{b_n}
&\equiv2^{n+1}-\frac{3n\,2^{n-2}(3q-4)}{q-3},\\
\frac{C_1^\sharp}{b_n}
&\equiv-\frac{2^{n+3}q}{A}
 +\frac{3n\,2^n(3q+2)}A,\\
\frac{T_0^\sharp}{b_r}
&\equiv1+\frac{3q(q-1)}2,\\
\frac{T_1^\sharp}{b_r}
&\equiv\frac{q-3}{2A}
 +\frac{3(q-1)(q^2+9q+12)}{4A}.                    \tag{14}
\end{aligned}
$$



Because $2^n\equiv7\pmod9$, these simplify without any subdivision by
$q\pmod9$:



$$
\boxed{
 \frac{C_0^\sharp}{b_n}\equiv2,\qquad
 \frac{C_1^\sharp}{b_n}\equiv2,\qquad
 \frac{T_0^\sharp}{b_r}\equiv4,\qquad
 \frac{T_1^\sharp}{b_r}\equiv7\pmod9.}              \tag{15}
$$



For completeness, the second congruence follows after combining its two
terms:



$$
\frac{2^n}{A}\{-8q+3(q-1)(3q+2)\}
 \equiv\frac{4(q+3)}A\equiv2\pmod9,
$$



because $4(q+3)-2A=18$. For the fourth, the numerator over $4A$ is



$$
2(q-3)+3(q-1)(q^2+9q+12)\equiv A\pmod9,
$$



so its value is $1/4\equiv7\pmod9$. The first and third congruences
follow directly from $q\equiv2\pmod3$ and $n\equiv1\pmod3$ in the
terms already carrying a factor $3$.

It follows from (15) that



$$
C_0^\sharp T_1^\sharp-C_1^\sharp T_0^\sharp
 \equiv b_nb_r(2\cdot7-2\cdot4)
 =6b_nb_r\pmod9.                                   \tag{16}
$$



Here $b_nb_r$ is again an explicit 3-adic unit, so the normalized
determinant has valuation exactly one.

Combining (10) and (16), and undoing the two normalizing factors, proves
(3).

## 5. Consequence and boundary

The theorem settles the characteristic-zero connection-determinant
obstruction uniformly: no admissible $\mathcal R_q$ is zero. It does
not say that the numerator of $\mathcal R_q$ has only small prime
divisors, nor does it replace the final power-of-two congruence at a prime
dividing that numerator. What it supplies is exactly the missing premise
of the fixed-gap meta-theorem, now for every positive gap coprime to $6$.

The accompanying standard-library script
work/verify_mixed_cubic_connection_determinant_3adic_nonvanishing.py
is a finite exact diagnostic of (1)--(3), (9), and (15). Its finite range
is not used in the proof above.
