> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 379 — local primitive-gcd formula, exponential height, and selector invisibility

Checked: 2026-09-01 (Beijing time)

## 1. Verdict and capacity

Retain the actual fixed-$j=1$ family



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



Item 376 left a nonlinear step between its cleared pairs and primitive
numerators:



$$
x_h={A_x(h)\over D_x(h)}={N_x(h)\over E_x(h)},
 \qquad
 u_h={A_u(h)\over D_u(h)}={N_u(h)\over E_u(h)}.
\tag{1.2}
$$



This item resolves the part of that step that can affect the actual
collision problem.

> **PROVED — local gcd and height theorem.**  For every prime $q$, the
> exponent of $q$ in the primitive denominator, and hence in
> $\gcd(A,D)$, is given exactly by one explicit local reverse-sum
> residue.  Uniformly,
> 

$$
> E_x(h),E_u(h)\mid\operatorname {lcm}(1,2,\ldots,4h+3).
> \tag{1.3}
>
$$


> Consequently the primitive numerators have genuinely exponential,
> rather than $\exp(O(h\log h))$, height:
> 

$$
> \boxed{\log|N_x(h)|=O(h),\qquad \log|N_u(h)|=O(h).}
> \tag{1.4}
>
$$



There is also a sharper actual-family conclusion.

> **PROVED — selector invisibility.**  Every prime divisor of either
> primitive gcd is at most $4h+3$, whereas every actual selected prime
> satisfies $p\geq4h+9$.  Therefore
> 

$$
> \boxed{
> p\mid N_x(h)\iff p\mid A_x(h),
> \qquad
> p\mid N_u(h)\iff p\mid A_u(h).}
> \tag{1.5}
>
$$



Thus nonlinear primitive reduction changes no actual selected-prime
event.  A recurrence for the reduced numerators remains open, but it is
not required for the actual modular bridge: one may work with the
unreduced holonomic sequences $A_x,A_u$ from Item 376.

The improved individual height does not aggregate to a useful weighted
bound.  There are $O(M)$ relevant rows with $h=O(M)$, so summing
$O(h)$ pointwise bounds gives $O(M^2)$, not $O(M)$ and certainly
not $o(M)$.  Hence



$$
\boxed{\text{new booking}=0},
 \qquad
 \boxed{\text{new capacity reduction}=0},
 \qquad
 \boxed{\text{shared fixed-}j=1\text{ ceiling}=1/36}.
\tag{1.6}
$$



## 2. The two reverse sums in local form

For either family write



$$
o_i=2h+1+2i.
\tag{2.1}
$$



For the $x$-family put



$$
n_x=h,
 \qquad
 d^{(x)}_j=3-2h+6j,
 \qquad
 Q^{(x)}_r=\prod_{j=0}^{r-1}d^{(x)}_j.
\tag{2.2}
$$



For the $u$-family put



$$
n_u=h+2,
 \qquad
 d^{(u)}_j=-3-2h+6j,
 \qquad
 Q^{(u)}_r=\prod_{j=0}^{r-1}d^{(u)}_j.
\tag{2.3}
$$



Also define $O_r=\prod_{i=0}^{r-1}o_i$.  Item 376's exact reversed
formulas become



$$
x_h=\sum_{r=0}^{n_x}\rho^{(x)}_r,
 \qquad
 \rho^{(x)}_r
 =(-1)^rk^{(0)}_{2r}{3^rO_r\over Q^{(x)}_r},
\tag{2.4}
$$



and



$$
u_h=\sum_{r=0}^{n_u}\rho^{(u)}_r,
 \qquad
 \rho^{(u)}_r
 =(-1)^rk^{(1)}_{2r}{3^rO_r\over Q^{(u)}_r}.
\tag{2.5}
$$



The $r=0$ term is $1$, so neither local system is empty.  The
assumption $3\nmid h$ implies that all $d_j^{(*)}$ are nonzero,
odd, and prime to $3$.

## 3. Exact prime-by-prime gcd identity

Fix a prime $q$.  Ignore any zero summand and define the maximum local
term defect



$$
\lambda_{*,q}
 =\max_{0\leq r\leq n_*}
 \max\bigl(0,-v_q(\rho^{(*)}_r)\bigr).
\tag{3.1}
$$



Then



$$
Z_{*,q}=q^{\lambda_{*,q}}\sum_r\rho^{(*)}_r
\tag{3.2}
$$



is $q$-integral.  Since $x_h=N_x/E_x$ and $u_h=N_u/E_u$ are
primitive fractions, direct valuation gives the exact identity



$$
\boxed{
 v_q(E_*)
 =\max\bigl(0,\lambda_{*,q}-v_q(Z_{*,q})\bigr).}
\tag{3.3}
$$



Writing $g_* =\gcd(A_*,D_*)$, it follows that



$$
\boxed{
 v_q(g_*)
 =v_q(D_*)-
  \max\bigl(0,\lambda_{*,q}-v_q(Z_{*,q})\bigr).}
\tag{3.4}
$$



Equations (3.1)–(3.4) are a complete prime-by-prime reduction.  They
separate the elementary term defects from exactly one remaining local
cancellation quantity, $v_q(Z_{*,q})$.  They are identities, not a
finite-data conjecture.

For $q=2$ or $3$, every $d_j^{(*)}$ is a unit, so



$$
\lambda_{*,2}=\lambda_{*,3}=0,
 \qquad
 \gcd(g_*,6)=1.
\tag{3.5}
$$



## 4. Uniform lcm bound for the primitive denominators

Now take $q\geq5$.  For any power $q^a$, both progressions



$$
d_j^{(*)}=c_*-2h+6j,
 \qquad
 o_j=2h+1+2j
\tag{4.1}
$$



have steps invertible modulo $q^a$.  In a prefix of the same length
$r$, the number of terms in either progression divisible by $q^a$ is
either $\lfloor r/q^a\rfloor$ or $\lceil r/q^a\rceil$.  Hence their
counts differ by at most one.

All numerator and denominator linear factors in (2.4)–(2.5) have
absolute value at most $4h+3$.  Therefore



$$
\begin{split}
 v_q(Q^{(*)}_r)-v_q(O_r)
 &=\sum_{a\geq1}
 \left(
  \#\{j<r:q^a\mid d_j^{(*)}\}
  -\#\{i<r:q^a\mid o_i\}
 \right)\\
 &\leq\#\{a\geq1:q^a\leq4h+3\}\\
 &=\lfloor\log_q(4h+3)\rfloor.
\end{split}
\tag{4.2}
$$



The integral kernel coefficient and $3^r$ can only reduce the
denominator defect.  Thus



$$
\lambda_{*,q}\leq\lfloor\log_q(4h+3)\rfloor.
\tag{4.3}
$$



Combining (3.3) and (4.3) prime by prime proves



$$
\boxed{
 E_x(h),E_u(h)\mid L_h,
 \qquad
 L_h=\operatorname {lcm}(1,2,\ldots,4h+3).}
\tag{4.4}
$$



This bound includes every cancellation pattern without assuming that the
least-valuation terms fail to cancel.

## 5. Uniform exponential height

There is also a direct Archimedean estimate specific to the reverse sums.
For fixed $*$, the absolute values



$$
|d^{(*)}_0|,|d^{(*)}_1|,\ldots,|d^{(*)}_{n_*-1}|
\tag{5.1}
$$



are distinct positive integers.  Indeed, equality with opposite signs
would force $3\mid h$, while equality with the same sign forces equal
indices.  Hence



$$
\prod_{j=0}^{r-1}|d_j^{(*)}|\geq r!.
\tag{5.2}
$$



Since $|o_i|\leq4h+3$, equations (2.4)–(2.5) give



$$
|\rho_r^{(*)}|
 \leq |k^{(*)}_{2r}|{[3(4h+3)]^r\over r!}.
\tag{5.3}
$$



The coefficient $\ell^1$-bounds for the two kernels are



$$
|k^{(0)}_j|\leq2^{2h+1},
 \qquad
 |k^{(1)}_j|\leq2^{2h+4}.
\tag{5.4}
$$



Summing the exponential series yields the explicit inequalities



$$
|x_h|\leq2^{2h+1}e^{12h+9},
 \qquad
 |u_h|\leq2^{2h+4}e^{12h+9}.
\tag{5.5}
$$



Because $|N_x|=E_x|x_h|$, $|N_u|=E_u|u_h|$, and



$$
\log L_h=\psi(4h+3)=O(h)
\tag{5.6}
$$



by the standard Chebyshev bound, (4.4) and (5.5) prove



$$
\boxed{
 |N_x(h)|
 \leq L_h\,2^{2h+1}e^{12h+9},
 \qquad
 |N_u(h)|
 \leq L_h\,2^{2h+4}e^{12h+9}.}
\tag{5.7}
$$



This is the promised uniform exponential height theorem (1.4).

## 6. Primitive reduction is invisible to the actual selector

The full product classification of $g_x,g_u$ is unnecessary for the
actual collision implication.  Since $g_*(h)\mid D_*(h)$, every prime
divisor of $g_*(h)$ divides one of the displayed linear factors.  Thus



$$
\boxed{q\mid g_x(h)g_u(h)\Longrightarrow q\leq4h+3.}
\tag{6.1}
$$



On an actual row,



$$
p=4h+6s+3\geq4h+9.
\tag{6.2}
$$



Therefore $p\nmid g_xg_u$.  From $A_x=g_xN_x$ and
$A_u=g_uN_u$,



$$
N_x\equiv g_x^{-1}A_x\pmod p,
 \qquad
 N_u\equiv g_u^{-1}A_u\pmod p,
\tag{6.3}
$$



which proves (1.5).  In particular, the nonlinear gcd operation can be
removed from every actual selected-prime divisibility test.  The
unreduced sequences are already holonomic by Item 376; their earlier
moving-modulus obstruction remains, but primitive reduction is not an
additional obstruction.

## 7. Smallest missing local lemma

The remaining exact product-formula problem is now sharply isolated.
For primes $q\leq4h+3$, determine



$$
v_q(Z_{x,q}),
 \qquad
 v_q(Z_{u,q}),
\tag{7.1}
$$



where $Z_{*,q}$ is the explicit finite hypergeometric residue in
(3.2).  Equivalently, one must control cancellation among precisely the
reverse-sum terms of least $q$-adic valuation.  Termwise progression
counts alone determine $\lambda_{*,q}$ but cannot determine this final
residue.

This is the smallest missing local lemma for a closed product formula or
a recurrence for $N_x,N_u$.  It concerns only primes below the actual
selector cutoff, so solving it may simplify the characteristic-zero
sequences but cannot by itself remove or create an actual collision
prime.

## 8. Capacity audit

The exponential height improvement is pointwise:



$$
\log|N_*(h)|=O(h).
\tag{8.1}
$$



Across $O(M)$ actual rows with $h=O(M)$, its direct aggregate is only



$$
\sum_h O(h)=O(M^2).
\tag{8.2}
$$



The required weighted exceptional mass is $o(M)$.  Thus (8.2) is not a
capacity theorem, and no part of the comparison or gcd support may be
booked.  The boundary charts remain inside the one shared fixed-$j=1$
gate:



$$
\boxed{
 \Delta r_1=0,
 \qquad
 \Delta\text{capacity}=0,
 \qquad
 \text{retained shared ceiling}=1/36.}
\tag{8.3}
$$



## 9. Strict labels

### PROVED

- the exact local identities (3.3) and (3.4) for every prime;
- $\gcd(g_xg_u,6)=1$;
- the uniform defect bound (4.3);
- $E_x,E_u\mid\operatorname {lcm}(1,\ldots,4h+3)$;
- the explicit exponential bounds (5.7), hence
  $\log|N_x|,\log|N_u|=O(h)$;
- primitive-gcd selector invisibility and the equivalences (1.5);
- zero booking, zero capacity reduction, and retention of the shared
  $1/36$ ceiling.

### EXACT FINITE ONLY

- ten predeclared $h$-controls for the local identities and four
  predeclared actual-row controls in the deterministic replay;
- no prime scan, collision census, recurrence guess, or extrapolation.

### OPEN

- uniform evaluation of the local residues $Z_{*,q}$ for
  $q\leq4h+3$;
- a closed product formula for the full primitive gcd;
- a fixed-order polynomial recurrence for the primitive reduced
  numerators;
- selector-aware weighted zero density for the actual paired gates;
- any strict fixed-$j=1$ capacity reduction, Route 1, and every
  conclusion about $e+\pi$.
