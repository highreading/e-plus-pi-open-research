> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 179 — independent diagonal Hermite--Padé forms and the endpoint tax

Checked: 2026-08-29 (Beijing time)

## Status and outcome

Let



$$
F(z)=4\arctan\frac{z}{2-z},\qquad F(1)=\pi,
$$



and let $A,B,C\in\mathbb Q[z]$ have degrees at most $n$. This item
separates two constructions that must not be conflated:

1. the genuinely independent, maximally cancelling diagonal family;
2. the one-order-lower family in which $B(1)=C(1)$ is imposed so that the
   endpoint is an integer form in $e+\pi$.

The central result is an all-degree linear-algebra theorem.

> **PROVED — compatibility determinant identity.** In every degree $n$,
> maximal Taylor cancellation is compatible with $B(1)=C(1)$ if and only if
> one explicit square compatibility determinant vanishes. Equivalently, the
> endpoint-matched order-$(3n+1)$ family then acquires one extra zero.

The determinant is not proved nonzero in all degrees. Its certified finite
behavior is nevertheless decisive over a substantial range.

> **PROVED — finite rank obstruction.** For every $1\le n\le256$, exact
> arithmetic modulo the proved prime $65521$ shows that:
>
> - the maximal independent family is projectively unique and has exact zero
>   order $3n+2$;
> - its endpoint mismatch $B(1)-C(1)$ is nonzero;
> - the endpoint-matched family is projectively unique and has exact zero
>   order $3n+1$.
>
> Hence no maximally cancelling independent form in this range is a native
> integer form $A+B(e+\pi)$. The endpoint condition costs exactly one Taylor
> order throughout the certified range.

There is also a fully rational, primitive reconstruction through $n=30$.
After the endpoint condition and complete gcd reduction, every nondegenerate
form $2\le n\le30$ has rigorously certified absolute value greater than one.
The values lie in single certified base-ten decades, rising from decade
$10^0$ at $n=2$ to decade $10^{1421}$ at $n=30$.

> **EXPERIMENTAL INTERPRETATION.** The exact finite data show rapid growth, not
> decay, in the endpoint-matched family. This is not promoted to an
> all-degree asymptotic theorem.

> **OPEN.** Nonvanishing of the compatibility determinant for every $n$,
> an asymptotic primitive-height theorem for the endpoint-matched family, and
> all broader unequal-degree or multipoint families remain open. Nothing here
> decides the arithmetic nature of $e+\pi$.

## 1. The two high-jet systems

Write



$$
B(z)=\sum_{j=0}^n b_jz^j,\qquad
 C(z)=\sum_{j=0}^n c_jz^j,
$$



and put $\tau_k=F^{(k)}(0)$. The exact jets are



$$
\tau_k=4(k-1)!2^{-k/2}\sin\frac{k\pi}{4}\in\mathbb Z
 \quad(k\ge1),\qquad \tau_0=0.
 \tag{1}
$$



For $k>n$, the derivative-scaled high equation is



$$
h_k(B,C):=
 \sum_{j=0}^n k^{\underline j}b_j+
 \sum_{j=0}^n k^{\underline j}\tau_{k-j}c_j=0.
 \tag{2}
$$



The low equations $0\le k\le n$ reconstruct $A$ uniquely:



$$
[z^k]A=
 -\frac1{k!}\sum_{j=0}^k
 k^{\underline j}\bigl(b_j+\tau_{k-j}c_j\bigr).
 \tag{3}
$$



Thus only $B,C$ remain in the high system.

### Maximal independent family

Let $M_n$ be the $(2n+1)$-by-$(2n+2)$ matrix with rows



$$
h_{n+1},h_{n+2},\ldots,h_{3n+1}.
 \tag{4}
$$



A nonzero kernel vector gives



$$
A+Be^z+CF=O(z^{3n+2}).
 \tag{5}
$$



This is the largest generic zero order available from the $3n+3$
coefficients up to projective scale.

### Endpoint-matched family

Let



$$
\ell(B,C)=B(1)-C(1)
 =\sum_{j=0}^n b_j-\sum_{j=0}^n c_j.
 \tag{6}
$$



Let $E_n$ be the $(2n+1)$-by-$(2n+2)$ matrix with rows



$$
h_{n+1},h_{n+2},\ldots,h_{3n},\ell.
 \tag{7}
$$



A nonzero kernel vector gives



$$
A+Be^z+CF=O(z^{3n+1}),\qquad B(1)=C(1),
 \tag{8}
$$



and therefore at $z=1$



$$
A(1)+B(1)(e+\pi).
 \tag{9}
$$



The endpoint equality is an actual extra row, not an assumption or a
post-processing identity.

## 2. The compatibility determinant theorem

Form the square matrix



$$
K_n=
 \begin{pmatrix}
 h_{n+1}\\
 \vdots\\
 h_{3n}\\
 h_{3n+1}\\
 \ell
 \end{pmatrix}.
 \tag{10}
$$



The following statement holds over any field of characteristic zero, and
over any finite field in which the displayed rows are defined.

### Theorem 1

The following conditions are equivalent:

1. the maximal independent kernel contains a nonzero vector satisfying
   $B(1)=C(1)$;
2. the endpoint-matched kernel contains a nonzero vector satisfying the
   additional equation $h_{3n+1}=0$;
3. $\det K_n=0$.

If $\det K_n\ne0$, then both $M_n$ and $E_n$ have full row rank,
their kernels are one-dimensional, and



$$
\ell(v_n^{\mathrm{max}})\ne0,\qquad
 h_{3n+1}(v_n^{\mathrm{end}})\ne0.
 \tag{11}
$$



#### Proof

The row set of $M_n$ is obtained from the first $2n$ common high rows by
adjoining $h_{3n+1}$; the row set of $E_n$ is obtained by adjoining
$\ell$. Appending the missing row to either system gives the same square
matrix $K_n$, up to row order. Thus a kernel vector of one rectangular
system also satisfies the missing equation exactly when $K_n$ is singular.
If $K_n$ is nonsingular, every proper row subset is independent, proving
the last assertion. $\square$

This identity is all-degree. Only the determinant nonvanishing below is
finite.

## 3. Exact finite rank and order through $n=256$

The certificate works over



$$
\mathbb F_p,\qquad p=65521.
$$



It proves primality by deterministic trial division and checks the jet
recurrence



$$
2\tau_{m+1}-2m\tau_m+m(m-1)\tau_{m-1}=0
 \pmod p
 \tag{12}
$$



at every used index. Since $3\cdot256+2<p$, all factorial divisions in
(2)--(3) are valid modulo $p$.

For each $n$, the program finds a nonzero maximal minor, normalizes the
omitted coordinate to one, reconstructs the kernel, and checks the full
matrix product. It then evaluates the endpoint mismatch and first free jet.
It does this separately for $M_n$ and $E_n$.

For $1\le n\le30$, the rational and modular implementations are also
cross-checked projectively: their normalized kernels, endpoint values, and
first-free jets agree modulo $65521$. The modular backend and exact runtime
versions are recorded in the JSON; all modular products are bounded strictly
inside signed 64-bit range.

### Theorem 2

For every $1\le n\le256$:



$$
\operatorname{rank}_{\mathbb Q}M_n
 =\operatorname{rank}_{\mathbb Q}E_n=2n+1,
 \tag{13}
$$





$$
h_{3n+2}(v_n^{\mathrm{max}})\ne0,\qquad
 \ell(v_n^{\mathrm{max}})\ne0,
 \tag{14}
$$



and



$$
h_{3n+1}(v_n^{\mathrm{end}})\ne0.
 \tag{15}
$$



Here the notation means evaluation of the next derivative row on the
displayed kernel vector. Nonzero residues modulo $65521$ prove the
corresponding rational quantities nonzero. Equations (13)--(15) imply



$$
\det K_n\ne0
 \quad(1\le n\le256).
 \tag{16}
$$



This is an exact finite theorem, not evidence for all $n$.

## 4. Rational normalization and endpoint gcd

For $1\le n\le30$, a second implementation uses only rational Gaussian
elimination. It makes the high kernel $(B,C)$ primitive integral, uses (3)
to reconstruct $A$, clears the exact least common denominator, and divides
the gcd of every coefficient in the full triple. This produces a primitive
integral polynomial triple whose first nonzero coefficient is positive. The
certificate records, degree by degree, the primitive $(B,C)$ vector, the
denominator cleared in reconstructing $A$, the full-triple gcd removed, and
the final endpoint denominator (one).

For the maximal family the endpoint is genuinely three-dimensional:



$$
A_n(1)+B_n(1)e+C_n(1)\pi,
 \qquad B_n(1)\ne C_n(1).
 \tag{17}
$$



No integer form in $e+\pi$ may be read from (17).

For the endpoint-matched family put



$$
X_n=A_n(1),\qquad Y_n=B_n(1)=C_n(1),\qquad
 d_n=\gcd(|X_n|,|Y_n|).
 \tag{18}
$$



The completely reduced integer form is



$$
\boxed{
 L_n=\frac{X_n}{d_n}+\frac{Y_n}{d_n}(e+\pi),\qquad
 \gcd\left(\frac{|X_n|}{d_n},\frac{|Y_n|}{d_n}\right)=1.}
 \tag{19}
$$



The full-triple gcd and endpoint-pair gcd are performed separately, and both
are recorded exactly in the certificate. Formula (19) therefore records the
actual primitive endpoint height



$$
H_n=\max\left(\frac{|X_n|}{d_n},\frac{|Y_n|}{d_n}\right).
 \tag{20}
$$



## 5. Rigorous endpoint values through $n=30$

The sign and decade of (19) are certified with rational intervals:

- $e$ is enclosed by a Taylor partial sum and an explicit factorial tail;
- $\pi$ is enclosed using
  

$$
\pi=16\arctan(1/5)-4\arctan(1/239)
$$


  and alternating rational remainders.

The interval endpoints themselves are represented exactly; the JSON stores
their hashes rather than printing multi-thousand-digit fractions.

At $n=1$, the endpoint pair is $(0,0)$. This is an endpoint-degenerate
polynomial triple, not a relation among $1,e,\pi$. For every
$2\le n\le30$, the primitive interval excludes zero and has absolute lower
endpoint greater than one.

Selected exact summaries are:

| $n$ | digits of $H_n$ | certified decade of $|L_n|$ |
|---:|---:|---:|
| 2 | 4 | $10^0$ |
| 3 | 8 | $10^4$ |
| 5 | 25 | $10^{18}$ |
| 10 | 125 | $10^{112}$ |
| 15 | 311 | $10^{293}$ |
| 20 | 591 | $10^{567}$ |
| 25 | 970 | $10^{941}$ |
| 30 | 1457 | $10^{1421}$ |

The complete certified decade sequence for $n=2,\ldots,30$ is



$$
\begin{aligned}
 0,4,10,18,31,47,65,87,112,141,174,210,249,293,339,\\
 390,444,503,567,634,704,779,857,941,1028,1122,1215,1317,1421.
 \end{aligned}
 \tag{21}
$$



Thus the first thirty exact diagonal systems supply no shrinking primitive
form. Statement (21) is finite and is not a monotonicity or asymptotic
theorem.

## 6. What is proved, experimental, and open

**PROVED**

- the all-degree compatibility determinant identity;
- complete modular rank, exact-order, and endpoint incompatibility for
  $1\le n\le256$;
- primitive rational reconstruction and exact endpoint gcds for
  $1\le n\le30$;
- rational interval signs, nonvanishing, and decades for every nondegenerate
  endpoint-matched form in that exact range.

**EXPERIMENTAL**

- the rapid growth pattern suggested by the exact finite values;
- any extrapolation of determinant nonvanishing beyond $n=256$.

**OPEN**

- an all-degree sign, recurrence, or closed product for $\det K_n$;
- an asymptotic for the primitive endpoint gcd $d_n$;
- any unequal-degree allocation producing shrinking native forms;
- the irrationality or rationality of $e+\pi$.

## 7. Portable artifacts

The certificate depends only on its sibling exact-arithmetic helper and the
bundled NumPy runtime. It does not read the research archive.

Invoked without `--output`, the certificate writes beside itself in `work/`;
after staging under `scripts/`, it writes to the sibling `results/` directory.
Passing `--output` with the replay filename produces the independently
byte-compared replay. The sibling helper is resolved from the certificate's
own directory, so invocation does not depend on the current working directory.

- sources/item179_independent_diagonal_report.md
- scripts/item179_independent_diagonal_certificate.py
- scripts/item179_independent_diagonal_exact.py
- results/item179_independent_diagonal_certificate.json
- results/item179_independent_diagonal_certificate_replay.json
- results/item179_independent_diagonal_hashes.sha256
