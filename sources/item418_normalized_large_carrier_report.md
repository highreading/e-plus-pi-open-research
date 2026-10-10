> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 418 — sharp centered-circle height for the fully Cartier-normalized large carrier

Date: 2026-09-01  
Status: **CANONICAL, ROOT-AUDITED, COMPONENT CEILING REDUCED, NO BOOKING**

## 1. Verdict and capacity first

Retain the exact Item-390 residue integers



$$
\lambda_{0,m}=[y^{4m}]
 \frac{(1-y)^{6m}(1+y)}{(1+y^2)^{4m+1}},
 \qquad
 \lambda_{1,m}=[y^{4m+1}]
 \frac{(1-y)^{6m}(1+y)^4}{(1+y^2)^{4m+2}},
 \tag{1.1}
$$



and canonical Item 200's complete squarefree rank-zero Cartier product



$$
F_m=G_m\mid\lambda_{0,m},\lambda_{1,m},
 \qquad
 \log F_m=\mathfrak C_Fm+o(m),
 \tag{1.2}
$$



where



$$
\mathfrak C_F=-4\log2+\frac{\pi}{\sqrt3}+3\log3
 =2.3370475079987656871\ldots .
 \tag{1.3}
$$



Thus Item 415's normalized coordinates are



$$
\mu_{s,m}=\lambda_{s,m}/F_m\in\mathbb Z.
 \tag{1.4}
$$



Item 390 and Item 415 already prove, for every prime $p>6m$, the
all-depth identity



$$
v_p(c_m)=\min\{v_p(\mu_{0,m}),v_p(\mu_{1,m})\}.
 \tag{1.5}
$$



The new theorem is an exact optimization of the common Cauchy kernel in
(1.1).  Let $x_*$ be the unique positive root of



$$
h(x)=9x^3+3x^2+12x-4,
 \tag{1.6}
$$



put $r_*=\sqrt{x_*}$, and define



$$
\rho_*=
 \frac{2(3x_*^2+3x_*+2)^3}
 {x_*^2(9x_*^4+6x_*^3+5x_*^2-8x_*+4)^2}.
 \tag{1.7}
$$



Then



$$
r_*=0.541298719518858\ldots,
 \qquad
 \rho_*=135.5974839008548212502259703306\ldots .
 \tag{1.8}
$$



This item proves



$$
|\lambda_{0,m}|<3\rho_*^m,
 \qquad
 |\lambda_{1,m}|<21\rho_*^m
 \tag{1.9}
$$



for every $m\ge1$.  On the nonzero rows to which Item 390 applies, and
hence for every sufficiently large $m$, it follows that



$$
c_m^><\frac{21\rho_*^m}{F_m}.
 \tag{1.10}
$$



Consequently Item 415's strictly-large component ceiling improves to



$$
\boxed{
 \limsup_{m\to\infty}\frac{\log c_m^>}{6m}
 \le\frac{\log\rho_*-\mathfrak C_F}{6}
 =0.4287738853386578689457603829\ldots .}
 \tag{1.11}
$$



The previous ceiling was



$$
\frac{\log136-\mathfrak C_F}{6}
 =0.4292678962895477202317242499\ldots,
$$



so the component-ceiling decrease is



$$
\boxed{
 \frac{\log(136/\rho_*)}{6}
 =0.0004940109508898512859638670\ldots .}
 \tag{1.12}
$$



This is a positive linear-exponent **Closer** improvement, but it is small
and it is not decision-changing.  It changes neither the booked lower bound,
the global total-content ceiling, nor the frozen deficit.  Its more useful
strategic consequence is a scoped no-go: $\rho_*$ is the exact optimum of
the entire centered circular Cauchy-radius method.  Merely tuning the radius
cannot lower this exponential base any further.

## 2. The inherited exact carrier and de-overlap

Every prime in $F_m$ is at most $6m$, while the present component is



$$
c_m^>=\prod_{p>6m}p^{v_p(c_m)}.
 \tag{2.1}
$$



Therefore division by $F_m$ preserves every target valuation.  Combining
canonical Items 390 and 415 gives



$$
c_m^>=
 \left(\gcd(|\mu_{0,m}|,|\mu_{1,m}|)\right)_{p>6m}
 \tag{2.2}
$$



on every nonzero row.  No new divisor is introduced in this item.  The
Cartier product in (1.2) was already removed in the frozen normalization;
its sole role here is to remove forced height from the auxiliary global
carrier before estimating the disjoint $p>6m$ part.

## 3. The common centered-circle kernel

For $0<r<1$, Cauchy's formula applied to (1.1) gives



$$
|\lambda_{0,m}|
 \le
 \max_{|z|=r}\left|\frac{1+z}{1+z^2}\right|
 \left(
 \max_{|z|=r}
 r^{-4}\left|\frac{(1-z)^6}{(1+z^2)^4}\right|
 \right)^m,
 \tag{3.1}
$$



and



$$
|\lambda_{1,m}|
 \le
 \max_{|z|=r}
 \left|\frac{(1+z)^4}{r(1+z^2)^2}\right|
 \left(
 \max_{|z|=r}
 r^{-4}\left|\frac{(1-z)^6}{(1+z^2)^4}\right|
 \right)^m.
 \tag{3.2}
$$



Write $z=re^{i\theta}$, $c=\cos\theta$, and



$$
A=1+r^2-2rc,
 \qquad
 B=(1-r^2)^2+4r^2c^2.
 \tag{3.3}
$$



The exponential kernel is



$$
\Phi(r,c)=\frac{A^3}{r^4B^2},
 \qquad
 M(r)=\max_{-1\le c\le1}\Phi(r,c).
 \tag{3.4}
$$



Thus the exact centered-circle problem is to evaluate



$$
\inf_{0<r<1}M(r).
 \tag{3.5}
$$



## 4. Exact minimax theorem

Differentiation in $c$ gives



$$
\frac{\partial}{\partial c}\log\Phi(r,c)
 =-\frac{2r}{AB}f(r,c),
 \tag{4.1}
$$



where



$$
f(r,c)=3B+8rcA
 =-4r^2c^2+8r(r^2+1)c+3(r^2-1)^2.
 \tag{4.2}
$$



Its two roots are



$$
c_\pm(r)=
 \frac{1+r^2\pm\frac12\sqrt{7r^4+2r^2+7}}{r}.
 \tag{4.3}
$$



The upper root is greater than $1$.  The lower root enters the interval
at



$$
r_0=2-\sqrt3,
 \qquad c_-(r_0)=-1.
 \tag{4.4}
$$



For $0<r\le r_0$, $\Phi(r,c)$ decreases on $[-1,1]$, so



$$
M(r)=\Phi(r,-1)=\frac{(1+r)^6}{r^4(1+r^2)^4}.
 \tag{4.5}
$$



This expression decreases on that interval and at its right endpoint equals



$$
\frac{4887}{16}+\frac{5643\sqrt3}{32}
 =610.8738\ldots .
 \tag{4.6}
$$



It therefore cannot contain the global minimum.

For $r_0<r<1$, the unique angular maximum is $c_-(r)$.  Put
$x=r^2$ and $S=\sqrt{7x^2+2x+7}$.  Along this maximizing branch, the
radial derivative numerator is



$$
g=8\bigl((6x^2+5x+4)S-(15x^3+17x^2+18x+10)\bigr),
 \tag{4.7}
$$



with



$$
\operatorname{sign}M'(r)=-\operatorname{sign}g.
 \tag{4.8}
$$



The exact square-difference identity



$$
\begin{aligned}
 &(6x^2+5x+4)^2(7x^2+2x+7)\\
 &\quad -(15x^3+17x^2+18x+10)^2\\
 &=3(x-1)(x^2+1)(9x^3+3x^2+12x-4)
\end{aligned}
\tag{4.9}
$$



shows, because $0<x<1$, that



$$
\operatorname{sign}M'(r)=\operatorname{sign}h(x).
 \tag{4.10}
$$



Now



$$
h'(x)=27x^2+6x+12>0\qquad(x\ge0),
 \tag{4.11}
$$



while $h(0)=-4$ and $h(1)=20$.  Hence (1.6) has exactly one positive
root $x_*$; $M$ decreases before $r_*$ and increases after it.  This
proves



$$
\boxed{\inf_{0<r<1}M(r)=M(r_*)=\rho_*.}
 \tag{4.12}
$$



At the minimum, the maximizing angle simplifies to



$$
c_*=-\frac{r_*(3x_*+1)}4.
 \tag{4.13}
$$



Substitution into (3.4) yields exactly (1.7).

## 5. Algebraic isolation and the fixed prefactors

Eliminating $x_*$ from (1.6)--(1.7) gives



$$
262144\rho_*^3-35555328\rho_*^2
 +1259712\rho_*-531441=0.
 \tag{5.1}
$$



The discriminant of this cubic is



$$
-93433860167497364275200000000<0,
$$



so it has one real root.  Exact rational signs isolate it as



$$
135.59748<\rho_*<135.59749.
 \tag{5.2}
$$



Likewise



$$
0.2930043<x_*<0.2930044,
 \qquad r_*<0.542.
 \tag{5.3}
$$



The fixed factors in (3.1)--(3.2) satisfy



$$
\max_{|z|=r}\left|\frac{1+z}{1+z^2}\right|
 \le\frac1{1-r},
 \tag{5.4}
$$



and



$$
\max_{|z|=r}
 \left|\frac{(1+z)^4}{r(1+z^2)^2}\right|
 \le\frac{(1+r)^2}{r(1-r)^2}.
 \tag{5.5}
$$



The second right side is increasing for
$r>\sqrt5-2$, because its logarithmic derivative has numerator
$r^2+4r-1$.  Since $r_*>r_0>\sqrt5-2$, (5.3) gives the exact rational
bounds



$$
\frac1{1-r_*}<\frac{500}{229}<3,
 \tag{5.6}
$$





$$
\frac{(1+r_*)^2}{r_*(1-r_*)^2}
 <\frac{297220500}{14211511}<21.
 \tag{5.7}
$$



Equations (3.1)--(3.2), (4.12), and (5.6)--(5.7) prove (1.9).

## 6. Capacity audit and the sharp method boundary

Using (1.2) in (1.10) proves (1.11).  The exact ledger effect is:

1. **Booked lower bound:** no change.
2. **Strictly-large component ceiling:** decreases by (1.12).
3. **Global total-content ceiling:** unchanged.  As Item 393 explains, an
   upper bound for one disjoint factor cannot be subtracted from an upper
   bound for the full product.
4. **Frozen deficit:** unchanged at
   $1.0196329836694317938803064012\ldots$.

As an admission comparison only, even crediting the strictly-large branch
at its entire new component ceiling leaves



$$
(T-r_1)-\frac{\log\rho_*-\mathfrak C_F}{6}
 =0.5908590983307739249345460183\ldots
 \tag{6.1}
$$



to be supplied outside this component.  Equation (6.1) is **not** a global
ceiling reduction or an additive de-overlap theorem for the other branches;
it merely quantifies how far this one component remains from filling the
frozen deficit by itself.

The component was already too small to fill the frozen deficit on its own.
Thus the numerical decrease is rigorous but not strategically decisive.
The theorem does, however, close a natural method class:

> Any argument that keeps the centered circle $|z|=r$, takes absolute
> values on that circle, and changes only the radius has exponential base at
> least $\rho_*$.

This statement is deliberately scoped.  It does not exclude a noncircular
steepest-descent contour, cancellation between saddle contributions, an
arithmetic resultant, a recurrence transfer, or a genuine weighted-zero
theorem for the pair $(\mu_{0,m},\mu_{1,m})$.

For an independent fully rational witness, take



$$
r=\frac{5413}{10000},
 \qquad C=\frac{678}{5}=135.6.
 \tag{6.2}
$$



The replay constructs



$$
P(c)=Cr^4\bigl((1-r^2)^2+4r^2c^2\bigr)^2
 -(1+r^2-2rc)^3.
 \tag{6.3}
$$



Its rational Sturm sequence has degrees $4,3,2,1,0$, with two sign
variations at both endpoints.  The values at $-1,0,1$ are positive, so
$P>0$ on $[-1,1]$.  This proves directly



$$
M(5413/10000)<678/5.
 \tag{6.4}
$$



The corresponding rational ceiling is



$$
0.4287769779179215846138273394\ldots,
$$



only



$$
0.0000030925792637156680669565\ldots
$$



above the exact circular optimum.  Increasing decimal precision in the
radius is therefore exhausted as a meaningful research direction.

## 7. Strict claim ledger

### PROVED

* The exact minimax theorem (4.12) for the common centered-circle kernel.
* The algebraic constant (1.7), its cubic (5.1), and the isolations
  (5.2)--(5.3).
* The uniform bounds (1.9).
* The fully Cartier-normalized all-depth component ceiling (1.11).
* The component-ceiling decrease (1.12), with zero booking and no global
  total-ceiling subtraction.
* The independent rational Sturm witness (6.2)--(6.4).

### SCOPED NO-GO

* Centered circular Cauchy bounds optimized only over the radius cannot have
  exponential base below $\rho_*$.

### OPEN

* $\log c_m^>=o(m)$, or $c_m^>=1$.
* A noncircular or cancellation-aware global height improvement.
* A recurrence, resultant, or Frobenius theorem for the actual normalized
  pair.
* Any new booked Route-1 mass, Route-1 completion, or irrationality of
  $e+\pi$.

### NOT CLAIMED

* That the circular bound is the true size of the gcd.
* That finite noncollision rows imply a support theorem.
* That $F_m$ is a new divisor of normalized content.
* Any proof of the irrationality of $e+\pi$.

## 8. Deterministic replay

Run

```text
python scripts/item418_normalized_large_carrier_certificate.py \
  --output results/item418_normalized_large_carrier_certificate_replay.json \
  --replay results/item418_normalized_large_carrier_certificate.json
```

The standard-library replay:

1. pins canonical Items 200, 390, and 415 by SHA-256;
2. verifies the exact radial sign identity (4.9);
3. verifies the algebraic relation (5.1) by polynomial reduction modulo
   (1.6);
4. checks exact rational isolating signs for $x_*$ and $\rho_*$;
5. proves the nearby rational inequality (6.4) by a complete Sturm
   sequence; and
6. records the de-overlapped component-ceiling arithmetic.

The canonical artifacts are stored in `sources/`, `scripts/`, `results/`,
and `manifests/`.
