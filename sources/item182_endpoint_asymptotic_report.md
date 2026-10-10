> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 182 — endpoint remainder tails, content, and the gcd bottleneck

Checked: 2026-08-29 (Beijing time)

## Status and outcome

Continue with the endpoint-matched diagonal family of Item 179:



$$
R_n(z)=A_n(z)+B_n(z)e^z+C_n(z)F(z),\qquad
 F(z)=4\arctan\frac{z}{2-z},
$$



where all three degrees are at most $n$,



$$
R_n(z)=O(z^{3n+1}),\qquad B_n(1)=C_n(1).
$$



The desired all-large nondecay theorem was not obtained. The strongest new
analytic result is an all-degree, exact tail representation and a completely
explicit singularity bound. It isolates the missing arithmetic input.

> **PROVED — exact endpoint tail and uniform bound.** For every such triple,
> $R_n(1)$ is exactly a sum of exponential tails and two logarithmic tails
> based at the conjugate singularities $1\pm i$. If
> $H_{BC}=\max_j(|b_j|,|c_j|)$, then
> 

$$
> |R_n(1)|\le H_{BC}\Phi_n,
> \quad
> \Phi_n=(n+1)\left{
> \frac{2n+2}{(2n+1)(2n+1)!}
> +\frac{12}{(2n+1)2^n}
> \right}.
> \tag{1}
>
$$



Thus analytic cancellation supplies an exponential factor of order $2^{-n}$
relative to coefficient height. It does not control the integer scale left
after full polynomial content and the separate endpoint gcd are removed.

> **PROVED — extended finite barrier.** Exact rational elimination and rigorous
> rational intervals were extended from $n=30$ to $n=45$. For every
> $2\le n\le45$, the fully reduced integer form has absolute value greater
> than one. At $n=45$, its height has 3581 digits and its absolute value lies
> in decade $10^{3529}$. No shrinking subsequence occurs in this range.

> **EXPERIMENTAL INTERPRETATION.** The primitive endpoint height grows much
> faster than the observed relative approximation improves. This strongly
> disfavors this particular diagonal ray, but is not an asymptotic theorem.

> **OPEN.** A recurrence or sign formula for the normalized value, an
> all-degree lower bound, and adequate control of the endpoint gcd remain
> missing. Nothing here decides the arithmetic nature of $e+\pi$.

## 1. Exact singularity description

Put



$$
\alpha=\frac{1-i}{2},\qquad \bar\alpha=\frac{1+i}{2}.
$$



The two nearest singularities of $F$ are $\alpha^{-1}=1+i$ and
$\bar\alpha^{-1}=1-i$, and the power series at zero has the exact form



$$
F(z)=\frac2i\left[
 \log(1-\alpha z)-\log(1-\bar\alpha z)
 \right]
 =\sum_{q\ge1} f_qz^q,
\tag{2}
$$





$$
f_q=\frac4q\,2^{-q/2}\sin\frac{q\pi}{4}.
\tag{3}
$$



Although (3) displays radicals, every $f_q$ is rational. Define the tails



$$
E_N=\sum_{q=N}^{\infty}\frac1{q!},\qquad
 T_N(w)=\sum_{q=N}^{\infty}\frac{w^q}{q}
 =w^N\int_0^1\frac{t^{N-1}}{1-wt}\,dt.
\tag{4}
$$



### Theorem 1 (exact endpoint tail)

Let $A,B,C$ have degrees at most $n$, and suppose
$A+Be^z+CF=O(z^m)$ with $m>n$. Then



$$
R(1)=
 \sum_{j=0}^n b_jE_{m-j}
 +\frac2i\sum_{j=0}^n c_j
 \left[T_{m-j}(\bar\alpha)-T_{m-j}(\alpha)\right].
\tag{5}
$$



#### Proof

The coefficients below degree $m$ vanish, while $A$ has no coefficients
at or above degree $m$. The series for $e^z$ and (2) converge absolutely
at $z=1$. Summing the remaining coefficients of $B e^z$ and $CF$, and
then shifting each polynomial coefficient, gives (5). The integral in (4)
follows by expanding $(1-wt)^{-1}$. $\square$

Formula (5) identifies the exact analytic mechanism: apart from the
factorially small exponential part, the value is governed by conjugate
logarithmic tails from $1\pm i$. In a first-order tail expansion their
amplitudes involve values of $C_n$ near those singularities, not merely the
imposed equality at $z=1$.

## 2. A uniform all-degree bound

For the endpoint family take $m=3n+1$ and put $q_0=m-n=2n+1$. Uniformly
for $0\le j\le n$,



$$
E_{m-j}\le E_{q_0}
 \le \frac{q_0+1}{q_0q_0!}.
\tag{6}
$$



From (3),



$$
|f_q|\le \frac4{q\,2^{\lfloor q/2\rfloor}}.
\tag{7}
$$



The first odd index $q_0=2n+1$, followed by pairs $(2r,2r+1)$, gives



$$
\sum_{q=q_0}^{\infty}|f_q|
 \le \frac{12}{q_0 2^n}.
\tag{8}
$$



There are $n+1$ coefficients in each polynomial. Applying the triangle
inequality to (5), then (6) and (8), proves (1). This theorem requires no
rank, uniqueness, or finite computation.

## 3. Why content and endpoint gcd are separate

Choose the rational kernel ray and clear denominators. First divide the gcd of
all coefficients of $(A,B,C)$; call the resulting triple *full primitive*.
For this triple put



$$
X=A(1),\qquad Y=B(1)=C(1),\qquad d=\gcd(|X|,|Y|).
\tag{9}
$$



The native primitive endpoint form is



$$
L=\frac Xd+\frac Yd(e+\pi)=\frac{R(1)}d.
\tag{10}
$$



Consequently (1) gives only



$$
|L|\le \frac{H_{BC}}d\Phi_n.
\tag{11}
$$



The full content is removed before $d$ is formed; they cannot be merged.
Moreover, if



$$
H_{\rm end}=\max(|X|,|Y|),
$$



then



$$
\frac{|L|}{H_{\rm end}/d}
 =\frac{|R(1)|}{H_{\rm end}}
 \le \frac{H_{BC}}{H_{\rm end}}\Phi_n.
\tag{12}
$$



The endpoint gcd cancels from the relative ratio. Absolute decay from the
analytic estimate would follow from $H_{BC}\Phi_n/d\to0$, but no estimate of
that strength is available. A lower bound proving nondecay is still harder:
(1) and (11) are upper bounds and cannot supply it.

This is the scoped barrier. Taylor order and singularity location alone do not
settle the primitive value; one needs arithmetic information about the kernel
coefficients and especially their endpoint gcd, or a sign-controlled exact
representation stronger than the triangle bound.

## 4. Exact diagnostics through degree 45

The certificate independently reconstructs the endpoint ray over
$\mathbb Q$ in every degree $1\le n\le45$. It records:

- the denominator cleared when reconstructing $A$;
- the full-triple gcd removed and final full content;
- hashes of the full triple and the primitive pre-reconstruction $(B,C)$;
- the raw endpoint pair, its separate gcd, and the primitive pair;
- polynomial, $(B,C)$, raw-endpoint, and primitive-endpoint heights;
- rigorous value and relative-value decades;
- the analytic upper bound (11), checked against the rigorous interval.

The enclosure of $e+\pi$ is fully rational: a Taylor enclosure for $e$
and alternating Machin-series enclosures for
$\pi=16\arctan(1/5)-4\arctan(1/239)$.

Selected results are:

| $n$ | endpoint-gcd digits | primitive-height digits | decade of $|L_n|$ | decade of $|L_n|/H_n$ | decade of bound (12) |
|---:|---:|---:|---:|---:|---:|
| 2  | 1  | 4    | 0    | -3  | -1 |
| 10 | 5  | 125  | 112  | -12 | 8  |
| 20 | 12 | 591  | 567  | -24 | 30 |
| 30 | 20 | 1457 | 1421 | -35 | 56 |
| 35 | 22 | 2053 | 2013 | -40 | 71 |
| 40 | 26 | 2760 | 2713 | -46 | 86 |
| 45 | 32 | 3581 | 3529 | -52 | 102 |

All displayed decades are certified using exact rational interval endpoints.
For every $2\le n\le45$, $|L_n|>1$; the value decades are strictly
increasing across this finite range. The relative ratio improves, but only by
52 decades at $n=45$, while the primitive height has 3581 digits.

The coefficient-to-raw-endpoint amplification
$H_{BC}/H_{\rm end}$ reaches decade $10^{115}$ at $n=45$. It overwhelms
the generic $2^{-n}$ factor in (12), explaining why the triangle bound has
already become non-informative. The actual relative error is much smaller than
that bound, so a sharper analysis would have to exploit cancellations between
the two conjugate tails in (5).

## 5. Classification

**PROVED**

- the all-degree exact tail identity (5);
- the all-degree singularity/triangle bound (1);
- exact full-content and endpoint-gcd diagnostics for $1\le n\le45$;
- rigorous nonzero values with $|L_n|>1$ for $2\le n\le45$.

**EXPERIMENTAL**

- extrapolation of height growth, relative-error decay, or small endpoint gcd;
- the suggestion that the diagonal endpoint ray never yields decay.

**OPEN**

- a recurrence or sign-controlled integral for $L_n$;
- asymptotics of $C_n(1\pm i)$, full coefficient height, and endpoint gcd;
- an all-large lower bound for $|L_n|$, or a shrinking subsequence;
- the arithmetic nature of $e+\pi$.

## 6. Portable artifacts

The certificate resolves the Item179 exact helper from its own directory. With
no `--output`, it writes beside itself in `work/`, or from archived `scripts/`
to the sibling `results/` directory.

The canonical digest records CPython 3.12.13 because the JSON deliberately
includes `sys.version`.  Replaying under another interpreter version changes
that metadata field (and hence the whole-file digest), while the mathematical
records remain identical; byte-identical replay uses the recorded runtime.

- sources/item182_endpoint_asymptotic_report.md
- scripts/item182_endpoint_asymptotic_certificate.py
- scripts/item179_independent_diagonal_exact.py (hashed dependency)
- results/item182_endpoint_asymptotic_certificate.json
- results/item182_endpoint_asymptotic_certificate_replay.json
- results/item182_endpoint_asymptotic_hashes.sha256
