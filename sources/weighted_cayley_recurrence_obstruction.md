> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Corrected weighted-residue recurrence: exact structure and a terminal no-go

Date: 2026-08-28

## 1. Scope

Let $q$ be a positive odd integer with $3\nmid q$, put



$$
P(z)=(1+z)(1+z^2),\qquad \alpha=\frac{2q-3}{3},
$$



and define the formal residue sequence



$$
J_s=\frac{P(z)^{\alpha-s}}{z^q(1-z)^q}\,dz,
 \qquad B_s=2\operatorname {Res}_0J_s+\operatorname {Res}_1J_s.
$$



For a valid fresh prime $p=6m+q>q$, the actual integral exponent is



$$
E=\frac{p+2q-3}{3},\qquad E\equiv\alpha\pmod p.
$$



The corrected Cayley calculation identifies $(B_0,B_1)$, up to explicit
nonzero powers of $2$, with the two mixed-cubic logarithmic residues.
Thus simultaneous logarithmic-residue vanishing implies $B_0=B_1=0$.

This note records two exact recurrences and then proves that neither the
order-four recurrence nor a symmetric-cube reinterpretation closes the
remaining valid-prime case.  It is a structure/no-go result, not a proof of
fresh-prime nonvanishing.

## 2. A short exact relation

Put



$$
a=-\frac{5(5q-9)}{8(q-3)},\qquad
 b=\frac{(5q-9)(5q-6)}{8(q-3)(2q-3)}.
$$



Then



$$
\boxed{B_2+aB_1+bB_0=0.} \tag{1}
$$



This is not a guessed numerical relation.  With



$$
S(z)=-\frac{3\{-5qz^3-5qz^2-5qz-3q
 +3z^4+9z^3+9z^2+9z+3\}}
 {8(q-3)(2q-3)}
$$



and $H=z(1-z)P S$, direct differentiation gives



$$
H'+H\left(-\frac qz+\frac q{1-z}
 +(\alpha-2)\frac{P'}P\right)=1+aP+bP^2. \tag{2}
$$



Multiplying (2) by $J_2$ and taking the weighted residues proves (1).
For every valid prime, the displayed denominators are units: the only
possible equality $p=2q-3$ would force $3\mid q$.  Consequently



$$
B_0=B_1=0\quad\Longrightarrow\quad B_2=0. \tag{3}
$$



Geometrically, after the Kummer substitution $w^3=x(x-1)$, (1) is the
reason the first three transformed differentials occupy a rank-two, not a
rank-three, twisted de Rham quotient.  Therefore a proposed $3\times3$
connection determinant cannot supply the missing Pochhammer obstruction.

## 3. The exact order-four recurrence

For every integer $s$,



$$
\boxed{\sum_{j=0}^4 a_j(s,q)B_{s+j}=0,} \tag{4}
$$



where



$$
\begin{aligned}
a_0={}&-81(s+1)(s+2)(3s+2)(3s+4)(3s+7)(3s+10),\\
a_1={}&-5(s+2)(3s+7)(3s+10)(5q-21s-27)\\
&\quad\cdot(5q^2-24qs-33q+45s^2+117s+72),\\
a_2={}&4(3s+10)(2q-3s-6)\\
&\quad\cdot(225q^2s^2+750q^2s+650q^2-1350qs^3-6975qs^2\\
&\qquad\quad-11550qs-6150q+2187s^4+15255s^3+38286s^2
 +40770s+15552),\\
a_3={}&-80(3s+4)(2q-3s-9)(2q-3s-6)\\
&\quad\cdot(9qs^2+39qs+37q-27s^3-180s^2-360s-207),\\
a_4={}&64(s+1)(3s+4)(3s+7)
 (2q-3s-12)(2q-3s-9)(2q-3s-6).
\end{aligned}
$$



The companion certificate re-derives (4), rather than merely substituting
sample values.  It solves the exact telescoping identity



$$
\sum_{j=0}^4\frac{a_j}{P^j}
 =H_s'+H_s\left(-\frac qz+\frac q{1-z}
 +(\alpha-s)\frac{P'}P\right)
$$



with $H_s=U_s(z)z(1-z)/P^3$, $\deg U_s\le10$, and verifies that the
symbolic residual is identically zero.

At the actual endpoint $s=E-k$, the three last factors of $a_4$ become



$$
2q-3s-12=3(k-3)-p,\quad
 2q-3s-9=3(k-2)-p,\quad
 2q-3s-6=3(k-1)-p.
$$



Thus $a_4$ has the terminal zero block $s=E-3,E-2,E-1$ modulo $p$.
This makes a forward connection argument tempting, but it is not enough.

## 4. The recurrence is not a symmetric cube

Taking the coefficient of the highest power of $s$ in
$(a_0,\ldots,a_4)$
gives



$$
(-6561,42525,-78732,58320,-15552).
$$



The Poincare characteristic polynomial is therefore



$$
-243(X-1)(4X-1)(16X^2-40X+27), \tag{5}
$$



whose roots are



$$
1,\quad\frac14,\quad\frac{5+\sqrt{-2}}4,
 \quad\frac{5-\sqrt{-2}}4. \tag{6}
$$



For a symmetric cube of a second-order recurrence, the four characteristic
roots have the form



$$
A^3,\ A^2B,\ AB^2,\ B^3.
$$



Hence they admit a pairing with equal products.  The roots (6) do not.  In
the real pairing the products are $1/4$ and $27/16$.  Either cross
pairing would require one conjugate quadratic root to be four times the
other; their sum and product then contradict $5/2$ and $27/16$.
Multiplying the sequence by any scalar gauge scales all four roots equally
and preserves this obstruction.  Thus (4) is not a symmetric cube, even up
to scalar gauge.

## 5. Exact surviving terminal modes

Start the recurrence with the hypothetical common-zero state



$$
(B_0,B_1,B_2,B_3)=(0,0,0,1). \tag{7}
$$



At a row where $a_4\ne0$, propagate forward.  At a right-singular row
$a_4=0$, test the remaining residual and, when it is zero, choose the new
free state to be zero.  This deterministic audit gives:

* $(q,p,E)=(5,11,6)$: the mode reaches $s=3$ with state window
  $(1,0,0,0)$; the residual is zero, and the rows $s=4,5$ vanish
  identically.  The Pochhammer product is $-56\equiv10\pmod {11}$, a unit.
* $(q,p,E)=(11,659,226)$: all three terminal residuals at
  $s=223,224,225$ are zero with a nonzero incoming state.  The Pochhammer
  product is again a unit modulo $659$.
* As controls, $(q,p)=(5,17)$ is killed at $s=5$ by residual $16$, and
  $(q,p)=(13,97)$ is killed at $s=37$ by residual $78$.

The first two primes are old connection-determinant candidates.  They show
that terminal compatibility can preserve nonzero modes on that candidate
locus; it therefore does not by itself impose the final Frobenius/cube
condition that excludes the actual logarithmic residues.  Any uniform proof
must use extra
information fixing the Cartier image line (equivalently, the prescribed
cube root), not just (1), (4), and their singular endpoints.

## 6. Replay

With the bundled SymPy runtime on `PYTHONPATH`, run

```
python scripts/weighted_cayley_recurrence_obstruction_certificate.py \
  --output results/weighted_cayley_recurrence_obstruction_certificate.json
```

The JSON records the exact telescoper factorization, the zero symbolic
residual in (2), the characteristic factorization (5), and every modular
terminal trace above.
