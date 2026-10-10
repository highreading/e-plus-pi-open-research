> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 253 — the half-binomial phase diagonal and its hypergeometric increment

Checked: 2026-08-31 (Beijing time)

## 1. Scope and verdict

Retain an actual ordinary-$j=2$ row



$$
p=2r+6s+3,\qquad r\geq1\text{ odd},\qquad 3\nmid r,\qquad s\geq1,
 \tag{1.1}
$$



and put



$$
m=s-1,\qquad \delta=r+4,\qquad
 n=3m+\delta={p-1\over2}.                         \tag{1.2}
$$



Thus $p=6m+2\delta+1$, $\delta\geq5$ is odd, and
$\delta\equiv3,5\pmod6$.  Let



$$
h_k={(1/2)_k\over k!2^k},\qquad H_m=\sum_{k=0}^m h_k.             \tag{1.3}
$$



Item 252 left $H_m$ as the sole universal moving prefix.  This item
specializes it to the phase (1.2).

> **PROVED — exact phase diagonal and integer normalization.**  Define
> 

$$
> K_{\delta,m}=\sum_{k=0}^m\binom{3m+\delta}{k}
>                         \left(-{1\over2}\right)^k,              \tag{1.4}
>
$$


> 

$$
> B_{\delta,m}=2^{3m+\delta}K_{\delta,m}-1\in\mathbf Z.           \tag{1.5}
>
$$


> On every actual row,
> 

$$
> \boxed{K_{\delta,m}\equiv H_m,\qquad
> H_m\equiv\varepsilon_2(B_{\delta,m}+1)\pmod p,}                \tag{1.6}
>
$$


> where $\varepsilon_2=2^{(p-1)/2}=(2/p)\pmod p$.

> **PROVED — one hypergeometric increment.**  With
> 

$$
> Q_\delta(j)=28j^2+(21\delta+25)j+4\delta^2+9\delta+5,           \tag{1.7}
>
$$


> the exact integer increment
> $\Delta_{\delta,j}=B_{\delta,j+1}-B_{\delta,j}$ is
> 

$$
> \boxed{
> \Delta_{\delta,j}=(-1)^{j+1}2^{2j+\delta}
> \binom{3j+\delta}{j}
> {Q_\delta(j)\over(j+1)(2j+\delta+1)}.}                         \tag{1.8}
>
$$


> In particular, $B_{\delta,m}$, and hence $H_m$ on the phase,
> is one alternating incomplete hypergeometric sum.

> **PROVED — fixed-$r$ terminal-increment invariant.**  Every factor
> in (1.8) other than $Q_\delta(m)$ is a $p$-unit, and
> 

$$
> \begin{aligned}
> 2Q_\delta(m)-(2m^2-m+3)
>   &=p(4\delta+9m+7),\\
> 18Q_\delta(m)-(2\delta^2+5\delta+29)
>   &=p(35\delta+84m+61).
> \end{aligned}                                                   \tag{1.9}
>
$$


> Therefore
> 

$$
> \boxed{
> \Delta_{\delta,m}\equiv0\pmod p
> \iff p\mid 2m^2-m+3
> \iff p\mid 2r^2+21r+81.}                                      \tag{1.10}
>
$$


> For fixed $r$, terminal-increment zeros can occur only among prime
> divisors of one fixed nonzero integer.  For fixed $p$, there are at
> most two phase indices $m$; the discriminant is $-23$.

> **PROVED, SHARPLY SCOPED NO-GO — six-section values do not isolate the
> target coefficient.**  The exact Cartier polynomial in Section 6 gives
> all six residue-class sums of the $H_k$'s.  For $m\geq1$, however,
> $z^m-z^{m+6}$ has zero value at every sixth root of unity and changes
> the coefficient of $z^m$.  Thus sixth-root evaluations, or their six
> Fourier section sums, alone cannot determine $H_m$.  This is only a
> no-go for the value-only six-section ansatz; it does not rule out jets,
> a higher Hasse digit, or an additional arithmetic invariant.

> **OPEN / zero booking.**  Formula (1.8) relocates the period; it does not
> sum it.  At $(p,r,s)=(43,11,3)$, $H_2=0\pmod {43}$ although every
> increment through the terminal one is nonzero.  Conversely, at
> $(127,17,15)$, the terminal increment is zero while $H_{14}=109$.
> Consequently (1.10) is not a nonvanishing theorem for the Item-251 gate.
> This item books zero rate and zero capacity reduction.

All bounded counts in the companion output are labeled **EXACT FINITE
ONLY**.

## 2. Frobenius phase diagonal

Since $n=(p-1)/2\equiv-1/2\pmod p$, for $0\leq k\leq m<p$,



$$
\binom nk\left(-{1\over2}\right)^k
 \equiv{(1/2)_k\over k!2^k}=h_k\pmod p.                          \tag{2.1}
$$



This proves the first congruence in (1.6).  The same sum is the exact
diagonal



$$
K_{\delta,m}=[x^m]{(1-x/2)^{3m+\delta}\over1-x}.                 \tag{2.2}
$$



Multiplying by $2^{3m+\delta}$ gives



$$
B_{\delta,m}=[x^m]{(2-x)^{3m+\delta}-1\over1-x}\in\mathbf Z,    \tag{2.3}
$$



including the subtracted boundary coefficient.  On the phase,
$2^{3m+\delta}=2^n=\varepsilon_2$, which proves the second
congruence in (1.6).

## 3. Elementary coefficient proof of the increment

Put $N=3j+\delta$.  Raising $j$ by one changes $N$ to $N+3$.
Using (2.3) at the common coefficient $x^{j+1}$ gives



$$
\begin{aligned}
 \Delta_{\delta,j}
  &=[x^{j+1}](2-x)^N{(2-x)^3-x\over1-x}\\
  &=[x^{j+1}](2-x)^N(x^2-5x+8),                  \tag{3.1}
 \end{aligned}
$$



because



$$
(2-x)^3-x=(1-x)(x^2-5x+8).                     \tag{3.2}
$$



The three coefficients in (3.1) give



$$
\Delta_{\delta,j}=(-1)^{j+1}2^{2j+\delta}
 \left\{4\binom N{j+1}+5\binom Nj+2\binom N{j-1}\right\},       \tag{3.3}
$$



where the first binomial in braces means $\binom N{j+1}$.
Combining the three terms over
$(j+1)(2j+\delta+1)$ yields exactly $Q_\delta(j)$, proving
(1.8).  Formula (3.1) also proves integrality without division.

The exact hypergeometric ratio is



$$
{\Delta_{\delta,j+1}\over\Delta_{\delta,j}}
 =-4{(3j+\delta+1)(3j+\delta+2)(3j+\delta+3)
          Q_\delta(j+1)
 \over
 (j+2)(2j+\delta+2)(2j+\delta+3)Q_\delta(j)}.                   \tag{3.4}
$$



Over $\mathbf Q$, $Q_\delta(j)>0$ for the present parameters, so
(3.4) is legitimate.  Modulo $p$, $Q_\delta(j)$ can vanish; the
portable certificate uses the cross-multiplied recurrence and never
inverts it.

## 4. What the reduction does and does not sum

The initial value is



$$
B_{\delta,0}=2^\delta-1.                                          \tag{4.1}
$$



Consequently



$$
B_{\delta,m}=2^\delta-1+\sum_{j=0}^{m-1}\Delta_{\delta,j},       \tag{4.2}
$$



and (1.6) becomes



$$
\boxed{
 H_m\equiv\varepsilon_2\left(
 2^\delta+\sum_{j=0}^{m-1}\Delta_{\delta,j}\right)\pmod p.}     \tag{4.3}
$$



This is an exact rank-two description: one product mode
$\Delta_{\delta,j}$ and its incomplete sum.  It is not a product
evaluation of $H_m$.

The separation is witnessed in both directions.

* At $(p,r,s,m,\delta)=(43,11,3,2,15)$, the residues of
  $Q_\delta(0),Q_\delta(1),Q_\delta(2)$ are $8,32,26$, the
  increment residues are $42,42,12$, but $H_2=0$.
* At $(127,17,15,14,21)$, $Q_{21}(14)=13970=110\cdot127$, so
  the terminal increment vanishes, but $H_{14}=109$.

Both are exact counterexamples to replacing the incomplete-sum condition
by terminal-increment nonvanishing.

## 5. Phase arithmetic and denominator audit

The identities in (1.9) follow by direct expansion using
$p=6m+2\delta+1$.  Since $\delta=r+4$,



$$
2\delta^2+5\delta+29=2r^2+21r+81.                \tag{5.1}
$$



All divisions used in the phase theorem are by units:



$$
0\leq m\leq n={p-1\over2}<p,                    \tag{5.2}
$$



so the factorials in $\binom nm$ are $p$-units.  Also



$$
\begin{aligned}
 0&<m+1<p,\\
 0&<2m+\delta+1<p,\\
 0&<m+2<p,\\
 0&<2m+\delta+2<2m+\delta+3<p.
 \end{aligned}                                                   \tag{5.3}
$$



For the final strict inequality,
$p-(2m+\delta+3)=4m+\delta-2\geq3$.  Powers of two and the
constants $2,3,6,18$ are units because $p\geq11$.  No
$Q_\delta(j)$ is inverted modulo $p$.

Thus (1.10) is an all-prime theorem.  It gives at most two terminal-zero
indices for a fixed $p$, and only finitely many for fixed $r$.  It
does not control the partial sum in (4.3), so no Route-1 mass is booked.

## 6. Exact Cartier polynomial and the six-section barrier

For $0\leq k\leq n$, define $H_k$ as in (1.3), and put



$$
C_p(z)=\sum_{k=0}^nH_kz^k\in\mathbf F_p[z].                       \tag{6.1}
$$



Taking first differences coefficientwise gives



$$
\boxed{
 (1-z)C_p(z)=(1-z/2)^n-\varepsilon_2z^{n+1}.}                    \tag{6.2}
$$



The right side and its derivative both vanish at $z=1$; the derivative
uses $2n+1=p$.  Hence



$$
C_p(1)=\sum_{k=0}^nH_k=0.                                      \tag{6.3}
$$



Over $\overline{\mathbf F}_p$, let $\mu_6$ be the sixth roots of
unity and define



$$
S_a=\sum_{\substack{0\leq k\leq n\\k\equiv a\ (6)}}H_k.
$$



Fourier inversion and (6.2) give the exact six-section relation



$$
6S_a=\sum_{\substack{\zeta\in\mu_6\\\zeta\ne1}}
 \zeta^{-a}{(1-\zeta/2)^n-\varepsilon_2\zeta^{n+1}\over1-\zeta},
 \tag{6.4}
$$



where the omitted $\zeta=1$ term is (6.3).  This holds whether or not
the primitive sixth roots lie in $\mathbf F_p$.

Equation (6.4) is genuine phase/Cartier information, but it gives a sum
over an entire residue class.  For every actual row with $m\geq1$,
$m+6\leq n$, and



$$
E(z)=z^m-z^{m+6}                                                     \tag{6.5}
$$



vanishes at all of $\mu_6$, including $1$, while changing the
coefficient of $z^m$.  Therefore value-only six-section data cannot
isolate $H_m$.  The statement is deliberately ambient and scoped: it
does not perturb the actual polynomial identity (6.2), and it does not
exclude derivative jets or other structure.

## 7. Strict labels and booking

### PROVED

* the phase diagonal (1.4)--(1.6);
* the integer coefficient identity (3.1) and closed increment (1.8);
* the hypergeometric ratio, used division-free modulo $p$;
* the all-prime terminal-zero criterion (1.10) and unit ranges;
* the Cartier polynomial (6.2), total-sum identity (6.3), six-section
  formula (6.4), and the scoped value-only barrier (6.5).

### EXACT FINITE ONLY

* all row counts and zero counts emitted by the checker;
* the bounded census of intermediate $Q_\delta(j)$-zeros;
* the bounded census of $H_m$-zeros.

### OPEN

* an evaluation or sufficiently strong zero theorem for the incomplete
  sum (4.3);
* a link from terminal-increment control to the Item-251 collision gate;
* a derivative/Hasse-jet invariant that determines the residual period;
* any new divisibility exponent, rate, capacity reduction, or conclusion
  about $e+\pi$.

Accordingly,



$$
\boxed{\text{new unconditional linear-log rate}=0,\qquad
        \text{capacity reduction}=0.}                            \tag{7.1}
$$


