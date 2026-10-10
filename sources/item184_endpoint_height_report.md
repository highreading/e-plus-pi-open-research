> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 184 — reverse-polynomial endpoint tails and the projective height obstruction

Checked: 2026-08-29 (Beijing time)

## Status and outcome

Continue with the endpoint-matched diagonal family of Items 179 and 182:



$$
R_n(z)=A_n(z)+B_n(z)e^z+C_n(z)F(z),\qquad
F(z)=4\arctan\frac{z}{2-z},
$$



where all three degrees are at most $n$,



$$
R_n(z)=O(z^{3n+1}),\qquad B_n(1)=C_n(1).
\tag{1}
$$



This item sharpens the coefficient-height estimate of Item 182 and identifies
what normalization can and cannot accomplish.

> **PROVED — all-degree removal of the coefficient-count loss.** Put
> $q=2n+1$ and
> $H_{BC}=\max_j(|b_j|,|c_j|)$. Then every triple satisfying (1) obeys
> 

$$
> |R_n(1)|\le H_{BC}\Psi_n,
> \qquad
> \Psi_n=
> \frac{(q+1)^2}{q^2\,q!}
> +\frac{16+12\sqrt2}{q\,2^n}.
> \tag{2}
>
$$


> The rational majorant
> 

$$
> \Psi_n^\#=
> \frac{(q+1)^2}{q^2\,q!}+\frac{33}{q\,2^n}
> \tag{3}
>
$$


> is strictly smaller, for every $n\ge2$, than Item 182's bound
> 

$$
> \Phi_n=(n+1)\left\{
> \frac{q+1}{q\,q!}+\frac{12}{q\,2^n}
> \right\}.
> \tag{4}
>
$$



The key is an exact reverse-polynomial integral. It replaces a triangle sum
over $n+1$ logarithmic tails by one integral of the reverse polynomial.

> **PROVED — normalization obstruction.** Full-content reduction,
> endpoint-gcd reduction, and rescaling do not change either projective ratio
> $H_{BC}/H_{\rm end}$ or effective ratio $H_{BC}/d$, where
> $H_{\rm end}=\max(|A(1)|,|B(1)|)$ and
> $d=\gcd(|A(1)|,|B(1)|)$. Consequently no choice of integral
> normalization can remove the coefficient-to-endpoint height loss. A further
> advance must control the projective kernel direction itself.

> **PROVED — finite exact barrier.** For the exact primitive Item 179 rays,
> 

$$
> \frac{H_{BC}}{H_{\rm end}}\ge4^n
> \qquad(7\le n\le30).
> \tag{5}
>
$$


> Moreover $(H_{BC}/H_{\rm end})\Psi_n^\#>1$ throughout this range.
> Hence even (2), after the rational relaxation (3), cannot certify relative
> shrinking on any of these degrees.

The finite statement (5) is not extrapolated. No shrinking subsequence and no
all-large lower bound for the actual endpoint value are proved.

## 1. Exact reverse-polynomial identity

For a polynomial



$$
C(z)=\sum_{j=0}^n c_jz^j,
$$



define its reverse polynomial



$$
C^*(u)=u^nC(1/u)=\sum_{j=0}^n c_ju^{n-j}.
\tag{6}
$$



Recall the logarithmic tail from Item 182,



$$
T_N(w)=\sum_{k=N}^{\infty}\frac{w^k}{k}
=w^N\int_0^1\frac{t^{N-1}}{1-wt}\,dt.
\tag{7}
$$



### Theorem 1

For every $m>n$ and $|w|<1$,



$$
\sum_{j=0}^n c_jT_{m-j}(w)
=w^{m-n}\int_0^1
\frac{t^{m-n-1}C^*(wt)}{1-wt}\,dt.
\tag{8}
$$



#### Proof

Insert (6) in the right side of (8). Its $j$-th term is



$$
c_jw^{m-j}\int_0^1\frac{t^{m-j-1}}{1-wt}\,dt
=c_jT_{m-j}(w).
$$



Summing gives (8). All sums are finite before integration. $\square$

This identity is the analytic gain: the old factor $n+1$ came from bounding
each shifted tail separately, whereas (8) retains their polynomial structure.

## 2. Improved all-degree endpoint bound

Let



$$
\alpha=\frac{1-i}{2},\qquad \bar\alpha=\frac{1+i}{2},
\qquad r=|\alpha|=2^{-1/2}.
$$



Item 182's exact endpoint formula, with $m=3n+1$, is



$$
R_n(1)=
\sum_{j=0}^n b_jE_{m-j}
+\frac2i\sum_{j=0}^n c_j
\left[T_{m-j}(\bar\alpha)-T_{m-j}(\alpha)\right],
\tag{9}
$$



where $E_N=\sum_{k=N}^{\infty}1/k!$. Put $q=m-n=2n+1$.

### 2.1 Exponential part

For $N\ge1$,



$$
E_N\le\frac{N+1}{NN!}.
\tag{10}
$$



Writing $m-j=q+(n-j)$, (10) gives, for $s\ge0$,



$$
E_{q+s}
\le \frac{q+1}{q q!(q+1)^s}.
\tag{11}
$$



Therefore



$$
\left|\sum_{j=0}^n b_jE_{m-j}\right|
\le H_{BC}\frac{(q+1)^2}{q^2\,q!}.
\tag{12}
$$



Here the finite geometric sum was enlarged to the corresponding infinite
sum. Compared with the exponential term in (4), the multiplier is smaller
by the exact factor $2/q$.

### 2.2 Logarithmic part

On either radial segment $w=\alpha$ or $w=\bar\alpha$,



$$
|C^*(wt)|
\le H_{BC}\sum_{s=0}^n(rt)^s
\le\frac{H_{BC}}{1-r},
\qquad
|1-wt|\ge1-r.
\tag{13}
$$



Using (8) and $\int_0^1t^{q-1}\,dt=1/q$, each conjugate integral is at
most



$$
\frac{H_{BC}r^q}{q(1-r)^2}.
\tag{14}
$$



The factor $2/i$ and the difference of the two integrals yield



$$
|\text{logarithmic part}|
\le\frac{4H_{BC}r^q}{q(1-r)^2}
=H_{BC}\frac{16+12\sqrt2}{q\,2^n}.
\tag{15}
$$



Equations (12) and (15) prove (2).

Finally, $\sqrt2<17/12$ because $289>288$, so
$16+12\sqrt2<33$. For $n\ge2$, the exponential part of (3) is smaller
than its counterpart in (4) by $2/q<1$, while
$33<12(n+1)$. This proves the strict all-degree comparison
$\Psi_n<\Psi_n^\#<\Phi_n$.

## 3. What normalization cannot improve

Let an integral representative of a rational kernel ray have full coefficient
content $g$. Set



$$
X=A(1),\qquad Y=B(1)=C(1),\qquad
d=\gcd(|X|,|Y|),
\tag{16}
$$



and let



$$
H_{\rm end}=\max(|X|,|Y|).
$$



Because $g$ divides every coefficient, it divides both $X$ and $Y$,
and hence $g\mid d$. After full-content reduction,



$$
H_{BC,0}=\frac{H_{BC}}g,
\quad
H_{{\rm end},0}=\frac{H_{\rm end}}g,
\quad
d_0=\frac dg.
\tag{17}
$$



Thus



$$
\frac{H_{BC,0}}{d_0}=\frac{H_{BC}}d,
\qquad
\frac{H_{BC,0}}{H_{{\rm end},0}}
=\frac{H_{BC}}{H_{\rm end}}.
\tag{18}
$$



Multiplying the whole ray by any nonzero integer $k$ multiplies
$g,d,H_{BC},H_{\rm end}$ by $|k|$, leaving both ratios in (18)
unchanged. Endpoint-gcd reduction changes the integer endpoint pair but
again leaves the relative ratio



$$
\frac{H_{BC}/d}{H_{\rm end}/d}
=\frac{H_{BC}}{H_{\rm end}}
\tag{19}
$$



unchanged. This proves the normalization obstruction.

Combining (2) with the endpoint normalization gives only



$$
\left|\frac{R_n(1)}d\right|
\le\frac{H_{BC}}d\Psi_n,
\qquad
\frac{|R_n(1)|}{H_{\rm end}}
\le\frac{H_{BC}}{H_{\rm end}}\Psi_n.
\tag{20}
$$



Accordingly, a shrinking theorem still needs a genuine bound on the
projective kernel direction, not a different choice of representative.

## 4. Exact finite obstruction

The certificate reads the exact rational endpoint-matched rays of Item 179
for $1\le n\le30$, reconstructs all three coefficient blocks and the
endpoint pair, and verifies that the stored triples are full primitive. It
also performs a deterministic rescaling check in every degree.

For every $7\le n\le30$, exact integer comparison proves (5), and exact
rational arithmetic proves



$$
\frac{H_{BC}}{H_{\rm end}}\Psi_n^\#>1.
\tag{21}
$$



Selected base-ten floors are:

| $n$ | $\lfloor\log_{10}(H_{BC}/H_{\rm end})\rfloor$ | $\lfloor\log_{10}((H_{BC}/H_{\rm end})\Psi_n^\#)\rfloor$ |
|---:|---:|---:|
| 7  | 6  | 4  |
| 10 | 10 | 8  |
| 15 | 22 | 18 |
| 20 | 35 | 29 |
| 25 | 50 | 42 |
| 30 | 65 | 55 |

This is a theorem only in the displayed finite range. The exact Item 182
extension through $n=45$ is consistent with the same obstruction, but no
asymptotic conclusion is drawn here.

## 5. Structural meaning

Endpoint matching controls the single scalar



$$
C^*(1)=C(1)=B(1).
$$



In contrast, (8) probes $C^*(wt)$ along the two complex radial segments
from zero to $\alpha$ and $\bar\alpha$. A value at the real endpoint does
not, by itself, control this singular-ray norm. The exact reverse-polynomial
identity therefore both improves the triangle bound and isolates the missing
input: one needs high-jet information about the particular kernel polynomial,
or a sign/cancellation formula coupling the two conjugate integrals.

## 6. Classification

**PROVED**

- the reverse-polynomial identity (8) for every $m>n$;
- the all-degree endpoint bound (2) and strict improvement (3)--(4) for every
  $n\ge2$;
- invariance of $H_{BC}/d$ and $H_{BC}/H_{\rm end}$ under scaling,
  full-content reduction, and endpoint-gcd normalization;
- the exact amplification and failed-bound barrier (5), (21) for
  $7\le n\le30$.

**EXPERIMENTAL**

- continued growth of $H_{BC}/H_{\rm end}$ beyond the exact range used by
  this certificate;
- the suggestion that the endpoint-matched diagonal ray never shrinks.

**OPEN**

- an all-degree coefficient-to-endpoint or singular-ray comparison for the
  actual kernel direction;
- a provable shrinking subsequence or an all-large nondecay theorem;
- an exact sign/cancellation formula for the pair of conjugate integrals;
- the arithmetic nature of $e+\pi$.

## 7. Portable artifacts and replay

The certificate resolves the pinned Item 179 JSON from its own directory.
With no output argument it writes beside itself in work, or from archived
scripts to the sibling results directory.

- sources/item184_endpoint_height_report.md
- scripts/item184_endpoint_height_certificate.py
- results/item184_endpoint_height_certificate.json
- results/item184_endpoint_height_certificate_replay.json
- results/item184_endpoint_height_hashes.sha256

Replay from the archive root:

    python scripts/item184_endpoint_height_certificate.py \
      --output results/item184_endpoint_height_certificate_replay.json

The manifest pins the Item 179 exact input and the Item 182 report and
certificate on which the analytic setup depends.
