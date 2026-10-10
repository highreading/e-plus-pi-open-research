> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 372 — the two $j=1$ boundary exact-zero strata are empty

Checked: 2026-09-01 (Beijing time)

## 1. Verdict and capacity

Retain the potentially prime fixed-$j=1$ rays



$$
p=4h+6s+3,
 \qquad
 M=3h+4s+2,
 \qquad
 h,s\geq1,
 \qquad
 3\nmid h.
\tag{1.1}
$$



Items 364 and 368 left two characteristic-zero exceptional sets,



$$
\mathcal Z_0=\{h:X_h=Y_h=0\text{ in }\mathbb Q\},
 \qquad
 \mathcal Z_1=\{h:U_h=V_h=0\text{ in }\mathbb Q\}.
\tag{1.2}
$$



This item closes them globally.

> **PROVED — terminal-term $3$-adic separation.**  For every integer
> $h\geq1$ with $3\nmid h$, the terminal summand of $X_h$ is the
> unique summand of lowest $3$-adic valuation.  The same is true of the
> terminal summand of $U_h$.  Consequently
> 

$$
> \boxed{X_h\ne0,\qquad U_h\ne0}
>
$$


> for every potentially prime ray.

It follows immediately that



$$
\boxed{\mathcal Z_0=\mathcal Z_1=\varnothing.}
\tag{1.3}
$$



This is an all-$h$ theorem, not a finite strip or a prime scan.  In
particular, the primitive large-prime carriers of Item 368 are now defined
on every potentially prime ray without an exceptional characteristic-zero
stratum.

The result removes one term from the weighted boundary target, but proves
no divisibility estimate for the remaining nonzero carriers.  Therefore



$$
\boxed{\text{new booking}=0},
 \qquad
 \boxed{\text{new capacity reduction}=0},
 \qquad
 \boxed{\text{shared fixed-}j=1\text{ ceiling remains }1/36}.
\tag{1.4}
$$



## 2. A one-line $3$-adic lemma

Write



$$
\sigma_h=-{4h+3\over6},
 \qquad
 A_h^{(0)}=\sigma_h+1={3-4h\over6},
 \qquad
 B_h^{(0)}=3\sigma_h+2={1-4h\over2}.
\tag{2.1}
$$



If $3\nmid h$, then for every integer $j$,



$$
\begin{aligned}
 6(A_h^{(0)}+j)&=3-4h+6j\equiv-h\not\equiv0\pmod3,\\
 6(\sigma_h+j)&=-4h-3+6j\equiv-h\not\equiv0\pmod3.
\end{aligned}
\tag{2.2}
$$



Hence



$$
\boxed{
 v_3(A_h^{(0)}+j)=-1,
 \qquad
 v_3(\sigma_h+j)=-1.}
\tag{2.3}
$$



On the other hand,



$$
B_h^{(0)}+j={1-4h+2j\over2},
 \qquad
 3\sigma_h+j={-4h-3+2j\over2}
\tag{2.4}
$$



have denominators prime to $3$, so



$$
\boxed{
 v_3(B_h^{(0)}+j)\geq0,
 \qquad
 v_3(3\sigma_h+j)\geq0.}
\tag{2.5}
$$



All four rational numbers in (2.2)–(2.4) are nonzero in the ranges used
below.  The two inequalities in (2.5) are allowed to be strict.

## 3. The first pair: $X_h$ is never zero

Let



$$
K_0(z)=(1-z)^{2h}(1+z)=\sum_jk^{(0)}_jz^j.
\tag{3.1}
$$



The tied phase value from Item 364 is



$$
X_h
 =\sum_{t=0}^{h}
 (-1)^t{(A_h^{(0)})_t\over(B_h^{(0)})_t}
 k^{(0)}_{2t+1}.
\tag{3.2}
$$



Call the $t$-th summand $T_t$.  Since $K_0$ has degree $2h+1$
and leading coefficient $1$,



$$
k^{(0)}_{2h+1}=1,
 \qquad
 T_h=(-1)^h{(A_h^{(0)})_h\over(B_h^{(0)})_h}\ne0.
\tag{3.3}
$$



For $0\leq t<h$, if $k^{(0)}_{2t+1}=0$, then $T_t=0$ and it can
be ignored.  Otherwise exact cancellation of the common initial
Pochhammer factors gives



$$
{T_t\over T_h}
 =(-1)^{t-h}k^{(0)}_{2t+1}
 {(B_h^{(0)}+t)_{h-t}\over
  (A_h^{(0)}+t)_{h-t}}.
\tag{3.4}
$$



The coefficient $k^{(0)}_{2t+1}$ is an integer.  Applying
(2.3)–(2.5) factor by factor gives



$$
\begin{aligned}
 v_3\!\left({T_t\over T_h}\right)
 &=v_3(k^{(0)}_{2t+1})
   +v_3((B_h^{(0)}+t)_{h-t})
   -v_3((A_h^{(0)}+t)_{h-t})\\
 &\geq 0+0+(h-t)\\
 &\geq1.
\end{aligned}
\tag{3.5}
$$



Thus every nonzero $T_t$, $t<h$, has strictly larger $3$-adic
valuation than $T_h$.  By the ultrametric inequality, a finite sum with
a unique lowest-valuation term has the valuation of that term.  Therefore



$$
\boxed{v_3(X_h)=v_3(T_h)<\infty,
 \qquad X_h\ne0.}
\tag{3.6}
$$



This already proves $(X_h,Y_h)\ne(0,0)$; no information about $Y_h$
is needed.

## 4. The second pair: $U_h$ is never zero

Let



$$
K_1(z)=(1-z)^{2h}(1+z)^4=\sum_jk^{(1)}_jz^j.
\tag{4.1}
$$



The tied phase value is



$$
U_h
 =\sum_{t=0}^{h+2}
 (-1)^t{(\sigma_h)_t\over(3\sigma_h)_t}
 k^{(1)}_{2t}.
\tag{4.2}
$$



Write $S_t$ for its $t$-th summand and $n=h+2$.  The polynomial
$K_1$ has degree $2h+4=2n$ and leading coefficient $1$, so



$$
k^{(1)}_{2n}=1,
 \qquad
 S_n=(-1)^n{(\sigma_h)_n\over(3\sigma_h)_n}\ne0.
\tag{4.3}
$$



For $0\leq t<n$, every nonzero earlier summand satisfies



$$
{S_t\over S_n}
 =(-1)^{t-n}k^{(1)}_{2t}
 {(3\sigma_h+t)_{n-t}\over
  (\sigma_h+t)_{n-t}}.
\tag{4.4}
$$



Again $k^{(1)}_{2t}\in\mathbb Z$, and (2.3)–(2.5) yield



$$
\boxed{
 v_3\!\left({S_t\over S_n}\right)
 \geq n-t\geq1.}
\tag{4.5}
$$



The terminal summand is therefore uniquely lowest, whence



$$
\boxed{v_3(U_h)=v_3(S_n)<\infty,
 \qquad U_h\ne0.}
\tag{4.6}
$$



This proves $(U_h,V_h)\ne(0,0)$ globally.  It also subsumes the
characteristic-zero part of the $h=2$ degeneracy: $V_2=0$, but
$U_2\ne0$.

## 5. Exact classification and the sharpened carrier target

Combining (3.6) and (4.6) gives the complete classification



$$
\boxed{
 \mathcal Z_0=\mathcal Z_1=\varnothing
 \quad\text{for every }h\geq1\text{ with }3\nmid h.}
\tag{5.1}
$$



Thus the Item 364 numerator gcds are always nonzero:



$$
G_h^{(0)}\ne0,
 \qquad
 G_h^{(1)}\ne0.
\tag{5.2}
$$



Equivalently, the primitive large-prime radicals
$\mathfrak G_0(h),\mathfrak G_1(h)$ of Item 368 require no exceptional
definition.  The exact remaining weighted theorem becomes



$$
\boxed{
 \sum_{\substack{h\text{ actual at }M\\p_h=(3M-h)/2\text{ prime}}}
 (\log p_h)
 1_{p_h\mid\mathfrak G_0(h)\mathfrak G_1(h)}
 =o(M).}
\tag{5.3}
$$



Item 372 proves only that the characteristic-zero indicator in the former
target vanishes identically.  It does not estimate the divisibility
indicator in (5.3).  Therefore the weighted boundary problem remains
open, but it is now a pure nonzero-carrier problem.

## 6. Capacity and overlap audit

The two boundaries are not separate ledger cells.  They and the
nonboundary chart all lie inside the one fixed-$j=1$ full gate.  Hence
the exact-zero classification cannot be credited as an additive gain.

No positive or zero-rate Chebyshev-mass theorem is obtained for
$p_h\mid\mathfrak G_0(h)\mathfrak G_1(h)$.  The correct ledger entry is



$$
\boxed{
 \Delta r_1=0,
 \qquad
 \Delta\text{capacity}=0,
 \qquad
 \text{retained shared ceiling}=1/36.}
\tag{6.1}
$$



The strategic gain is that one entire exceptional mechanism has been
removed globally: no actual ray can make either boundary automatic over
$\mathbb Q$.

## 7. Strict labels

### PROVED

- the valuation lemma (2.3)–(2.5) for every $3\nmid h$;
- unique terminal-term $3$-adic minimality for $X_h$;
- unique terminal-term $3$-adic minimality for $U_h$;
- $X_h\ne0$ and $U_h\ne0$ on every potentially prime ray;
- $\mathcal Z_0=\mathcal Z_1=\varnothing$;
- global nonzero definition of both primitive boundary carriers;
- the sharpened pure-divisibility target (5.3);
- zero booking and retention of the shared $1/36$ ceiling.

### EXACT FINITE ONLY

- eight predeclared exact summand controls in the deterministic replay;
- no prime scan, boundary census, or extrapolation.

### OPEN

- weighted zero density or an average-gcd theorem for the nonzero
  primitive carriers in (5.3);
- occurrence or nonoccurrence of either modular boundary for unbounded
  $h$;
- the nonboundary full-gate chart;
- any strict fixed-$j=1$ capacity reduction, Route 1, and every conclusion
  about $e+\pi$.

The theorem is purely characteristic zero.  It must not be read as
prime-by-prime nonvanishing of $X_h,U_h$ modulo an actual tied prime.
