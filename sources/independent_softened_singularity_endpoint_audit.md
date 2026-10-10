> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the softened-singularity endpoint subfamily

Date: 2026-08-26

Audited source snapshot:

```text
1ff8ef74ebd60cc89416771a972d14ac52a235ef736808b7583217dbbf30d5ed  sources/softened_singularity_endpoint_subfamily.md
```

## Scope and verdict

This note audits the live softened-singularity construction based on



$$
F(z)=4\arctan\frac{z}{2-z},\qquad
 D(z)=z^2-2z+2,
$$



including the exact endpoint form, integrality, fixed truncation degree,
proportional degrees $b/n\to\lambda\in(0,2)$, the critical diagonals
$b=2n+d$, and the stated growing transition window above $2n$.

The claims pass, with the contour details made explicit below.  In
particular, the horizontal-cut argument really does extend the positive
saddle theorem past the branch-point radius and up to every *fixed*
$\lambda<2$.  Its exponential gap is not uniform as $\lambda\uparrow2$,
so it must not be used for an arbitrary sequence $b/n\to2$.  The separate
moving-saddle analysis covers fixed offsets and the displayed growing
window, but not the entire transition region.

All finite scans in this audit are labeled finite experiments.  None of the
results proves irrationality, algebraicity, or transcendence of $e+\pi$.

## 1. Exact endpoint form and its sign convention

Put



$$
h_n(z)=e^{-z}D(z)^nF(z)
       =\sum_{k\geq0}\eta_{n,k}\frac{z^k}{k!},
$$





$$
E_b=\sum_{k=0}^b\frac{(-1)^k}{k!},\qquad
 H_{n,b}=\sum_{k=0}^b\frac{\eta_{n,k}}{k!}.
$$



If $A$ is constant and



$$
A+B(z)e^z+D(z)^nF(z)=O(z^{b+1}),
$$



then multiplication by $e^{-z}$ forces



$$
B=-T_b(Ae^{-z}+h_n).
$$



Since $D(1)=1$, the endpoint condition $B(1)=1$ is exactly



$$
-AE_b-H_{n,b}=1,
 \qquad
 A=-\frac{1+H_{n,b}}{E_b}.
$$



The original auxiliary expression at one is $A+e+\pi$.  Therefore its
multiple by $b!E_b$ is



$$
L_{n,b}=U_b(e+\pi)-V_{n,b},
$$



where



$$
U_b=b!E_b={!b},\qquad
 V_{n,b}=b!(1+H_{n,b}).
$$



This confirms both the minus sign in front of $V_{n,b}$ and the endpoint
normalization.  For $b\geq2$, $U_b>0$.  If



$$
g_{n,b}=\gcd(U_b,V_{n,b}),
$$



then $L_{n,b}/g_{n,b}$ is exactly the primitive two-coordinate form.

For $b=2$, direct differentiation gives



$$
\eta_{n,1}=2^{n+1},\qquad
 \eta_{n,2}=-2^{n+1}(2n+1),
$$



and hence



$$
U_2=1,\qquad
 V_{n,2}=2+2^{n+1}(1-2n),
$$





$$
L_{n,2}=e+\pi-2+2^{n+1}(2n-1)>0.
$$



The gcd is one in this case.

## 2. Integrality and the fixed-degree leading term

Let $f=e^{-z}F$.  Since



$$
D(f'+f)=4e^{-z},
$$



coefficient extraction in exponential-generating-function normalization
gives



$$
2(\eta_{0,k+1}+\eta_{0,k})
 -2k(\eta_{0,k}+\eta_{0,k-1})
 +k(k-1)(\eta_{0,k-1}+\eta_{0,k-2})=4(-1)^k.
$$



Solving for $\eta_{0,k+1}$ preserves integrality because $k(k-1)$ is
even.  Ordinary multiplication by $D$ gives



$$
\eta_{n+1,k}=2\eta_{n,k}-2k\eta_{n,k-1}
                  +k(k-1)\eta_{n,k-2},
$$



so every $\eta_{n,k}$ is an integer.  Consequently $U_b,V_{n,b}$ are
integers.

There is an independent direct formula.  If $\tau_j=F^{(j)}(0)$, then



$$
\eta_{0,k}=\sum_{j=0}^k\binom{k}{j}(-1)^{k-j}\tau_j.
$$



If $D(z)^n=\sum_\ell d_{n,\ell}z^\ell$, then



$$
\eta_{n,k}=\sum_{\ell=0}^{\min(2n,k)}
 d_{n,\ell}(k)_\ell\eta_{0,k-\ell}.
$$



These two formulas were used for the independent finite recomputation in
Section 6; they do not import the recurrences from the original probe.

For the fixed-degree asymptotic, write $D=2d$, with
$d(0)=1$, $d'(0)=-1$.  For fixed $k\geq1$, Leibniz's rule gives



$$
\eta_{n,k}=2^nP_k(n),\qquad \deg P_k\leq k-1.
$$



The unique contribution to degree $k-1$ differentiates $F$ once and
$d^n$ exactly $k-1$ times.  Its coefficient is



$$
\binom{k}{1}F'(0)(d'(0))^{k-1}
 =2k(-1)^{k-1}.
$$



Thus



$$
P_k(n)=2k(-1)^{k-1}n^{k-1}+O_k(n^{k-2}).
$$



In $V_{n,b}$, the $k=b$ summand has multiplier $b!/b!=1$, while
all lower summands have lower degree in $n$.  Therefore



$$
V_{n,b}=b!+2^nP_b^*(n),
$$



where $P_b^*$ has degree $b-1$ and leading coefficient
$2b(-1)^{b-1}$.  Since $g_{n,b}\leq U_b$ and $U_b$ is fixed, the
primitive form diverges for every fixed $b\geq2$.

## 3. The slit-contour formula and proportional saddles

Put



$$
P(w)=w^2+2w+2,\qquad
 \mathcal A(w)=\frac{e^wF(-w)}{1+w},
$$



so that



$$
H_{n,b}=(-1)^b a_{n,b},\qquad
 a_{n,b}=[w^b]\mathcal A(w)P(w)^n.
$$



Let



$$
\mu(r)=\frac{rP'(r)}{P(r)},\qquad
 \sigma^2(r)=r\mu'(r).
$$



For $\lambda_n=b/n\in(0,2)$, there is a unique positive
$r_n$ with $\mu(r_n)=\lambda_n$.  On every compact
$K\Subset(0,2)$, the radii $r_n$ remain in a compact subinterval of
$(0,\infty)$, and $\sigma^2(r_n)$ is bounded above and away from zero.

### Exact cuts, jumps, and orientations

With $\alpha=(1+i)/2$,



$$
F(-w)=-2i\bigl(\log(1+\bar\alpha w)
                    -\log(1+\alpha w)\bigr).
$$



Choose the two logarithm branches, continued from $w=0$, with horizontal
cuts



$$
C_+:w=-1-x+i,\qquad
 C_-:w=-1-x-i,\qquad x\geq0.
$$



Using `above minus below' boundary values, the jumps are



$$
\Delta_{C_+}F(-w)=-4\pi,
 \qquad
 \Delta_{C_-}F(-w)=+4\pi.
$$



The sign follows by mapping the upper cut through $1+\alpha w$, and the
lower cut through $1+\bar\alpha w$.  Each logarithm increases by
$2\pi i$ from its lower to its upper boundary value in the stated branch
convention.

Let $I_R$ be the outer-circle contribution divided by $2\pi i$, and
let $J_{\pm,R}$ be the two positively oriented slit-boundary
contributions.  If



$$
X(R)=\max\{0,\sqrt{R^2-1}-1\},
$$



then a direct boundary orientation gives



$$
J_{\pm,R}=\frac1{2\pi i}\int_0^{X(R)}
 \Delta_{C_\pm}\!\left(
 \frac{\mathcal A(w)P(w)^n}{w^{b+1}}
 \right)dx.
$$



The pole at $w=-1$ has residue $c=\pi/e$.  Hence, away from a contour
collision,



$$
a_{n,b}=I_R+J_{+,R}+J_{-,R}
 -\mathbf1_{R>1}\,c(-1)^{b+1}.
$$



This records the minus sign of the crossed pole term.  It also makes clear
that the cuts add jump integrals; they are not residues.

### Exponential bound for the cuts

On either cut,



$$
|w|^2=x^2+2x+2,
 \qquad
 |P(w)|^2=x^2(x^2+4),
$$



and therefore



$$
|w|^4-|P(w)|^2=4(x^3+x^2+2x+1)>0.
$$



Thus $|P(w)|<|w|^2$.  If $|w|\leq r_n$, then, because
$2-\lambda_n>0$,



$$
\frac{|P(w)|^n}{|w|^b}
 \leq r_n^{(2-\lambda_n)n}.
$$



On $K\Subset(0,2)$, the cut length is uniformly bounded,
$|e^w/(1+w)|$ is uniformly bounded, and $|w|\geq\sqrt2$.  Consequently



$$
|J_{+,r_n}|+|J_{-,r_n}|
 \leq C_K r_n^{(2-\lambda_n)n}.
$$



Relative to the positive-saddle exponential
$P(r_n)^nr_n^{-b}$, this is bounded by



$$
C_K\left(\frac{r_n^2}{P(r_n)}\right)^n.
$$



The base is strictly below one.  On a compact $K\Subset(0,2)$, it is
uniformly below one.  As $\lambda\uparrow2$, however, 

$$
r(\lambda)\to
\infty
$$

 and $r^2/P(r)\to1$.  Hence this argument deliberately supplies
no uniform estimate for arbitrary approaches to the endpoint $2$.

At $x=0$, $P(w)=0$; the factor $P(w)^n$ dominates the logarithmic
endpoint singularity.  If the chosen circle passes through $-1$ or one of
the two branch points, an outward radial perturbation by $O(1/n)$, together
with a shrinking slit indent, avoids the collision.  The first radial
derivative of



$$
\log P(r)-\lambda_n\log r
$$



vanishes at $r_n$, so this perturbation changes the saddle exponential by
$1+o(1)$.  The indent and cut pieces retain the strict exponential gap.

### Local saddle and nonzero leading coefficient

Near the positive saddle,



$$
\log\frac{P(r_ne^{i\theta})}{P(r_n)}
 -ib\theta/n
 =-\frac12\sigma^2(r_n)\theta^2+O_K(\theta^3).
$$



The positive coefficients of $P$, whose support has span one, give strict
modulus loss away from $\theta=0$.  The pole and cut neighborhoods were
bounded separately above.  Standard Gaussian localization, now with all
nonanalytic contour pieces accounted for, yields uniformly on compact
$K\Subset(0,2)$,



$$
a_{n,b}\sim
 \frac{\mathcal A(r_n)P(r_n)^nr_n^{-b}}
      {\sqrt{2\pi n\sigma^2(r_n)}}.
$$



For $r>0$, $F(-r)<0$, and hence $\mathcal A(r)<0$.  The leading
coefficient is therefore nonzero.  Moreover



$$
\Phi(\lambda)=\frac{P(r(\lambda))}{r(\lambda)^\lambda}>1:
$$



if $r<1$, then $r^\lambda<1<P(r)$; if $r\geq1$, then
$r^\lambda<r^2<P(r)$.  Thus $|H_{n,b}|$ grows exponentially for every
fixed $\lambda\in(0,2)$.

Finally,



$$
g_{n,b}\leq U_b,
 \qquad
 \frac13\leq E_b\leq\frac12,
$$



so



$$
\left|\frac{L_{n,b}}{g_{n,b}}\right|
 \geq\frac{|L_{n,b}|}{U_b}
 =\left|e+\pi-\frac{1+H_{n,b}}{E_b}\right|\to\infty.
$$



This primitive-gcd step is valid and requires no unproved estimate for the
actual gcd.

## 4. The moving saddle at $b=2n+d$

For the transition regime, put



$$
\mathcal B(w)=\frac{F(-w)}{1+w},\qquad
 H_{n,b}=(-1)^b[w^b]\mathcal B(w)e^wP(w)^n.
$$



The positive saddle for $b=2n+d$ is the unique solution of



$$
2n+d=r_n+n\mu(r_n).
$$



Let $R=\sqrt{2n}$.  Direct expansion gives



$$
\mu(r)=2-\frac2r+\frac4{r^3}+O(r^{-4}),
 \qquad
 \sigma^2(r)=\frac2r-\frac{12}{r^3}+O(r^{-4}).
$$



For fixed integer $d$,



$$
r_n=R+\frac d2+O(R^{-1}),
 \qquad
 r_n+n\sigma^2(r_n)=2R+O(1).
$$



The second expression is the total angular variance: $e^w$ contributes
$r_n$, while $P(w)^n$ contributes $n\sigma^2(r_n)$.

The local angular width is $R^{-1/2}$.  Every fixed higher angular
cumulant is $O(R)$, so after this scaling the cubic and higher normalized
cumulants tend to zero.  Away from the central arc, the elementary bound



$$
\frac{|e^{r_ne^{i\theta}}|}{e^{r_n}}
 =e^{-r_n(1-\cos\theta)}
$$



already supplies the required quantitative decay; this avoids relying on a
nonuniform fixed-radius span-one gap.

On the horizontal cuts,



$$
\frac{|P(w)|^n}{|w|^{2n+d}}<|w|^{-d}.
$$



After including the remaining factors, the cut integrand is bounded by a
constant multiple of



$$
e^{-x}\frac{|w|^{-d-1}}{|1+w|}.
$$



Its integral is $O_d(1)$, including fixed negative $d$.  The pole term
is also bounded.  Both are negligible compared with the positive saddle
found below.

Now



$$
\mathcal B(r)=-\frac\pi r(1+O(r^{-1})),
$$



and



$$
\log\frac{P(r)}{r^2}
 =\frac2r-\frac4{3r^3}+O(r^{-4}).
$$



At the saddle this gives



$$
e^{r_n}P(r_n)^nr_n^{-2n-d}
 =e^{2R}R^{-d}(1+o(1)).
$$



The Gaussian denominator is



$$
\sqrt{2\pi(r_n+n\sigma^2(r_n))}
 =2\sqrt{\pi R}(1+o(1)).
$$



Therefore



$$
H_{n,2n+d}\sim
 (-1)^{d+1}\frac{\sqrt\pi}{2}
 e^{2R}R^{-d-3/2}.
$$



This confirms the sign and the nonzero constant in the claimed fixed-offset
asymptotic.

## 5. Growing nonnegative offsets

Let $d=d_n\geq0$, $d=o(R)$.  Uniform expansion of the exact saddle
equation gives



$$
r_n=R+\frac d2+O\!\left(\frac{d^2+1}{R}\right).
$$



For



$$
S(r)=r+\frac{R^2}{2}\log\!\left(1+\frac2r+\frac2{r^2}\right)-d\log r,
$$



Taylor expansion at the exact saddle gives



$$
S(r_n)=2R-d\log R-\frac{d^2}{4R}
 +O\!\left(1+\frac{d^3}{R^2}\right).
$$



The amplitude $\mathcal B(r_n)$ and Gaussian denominator add
$-\tfrac32\log R+O(1)$.  The moving-saddle localization above remains
uniform because $r_n/R\to1$ and the total variance is asymptotic to
$2R$.  For $d\geq0$, the cut integral is uniformly $O(1)$.

In any subrange where the positive-saddle expression tends to infinity, it
dominates both the bounded pole and the cut terms, and hence



$$
\log|H_{n,2n+d}|
 =2R-d\log R-\frac{d^2}{4R}-\frac32\log R
 +O\!\left(1+\frac{d^3}{R^2}\right).
$$



If, for a fixed $\delta>0$,



$$
0\leq d\leq(2-\delta)\frac{R}{\log R},
$$



then



$$
d\log R\leq(2-\delta)R,
 \qquad
 \frac{d^2}{R}=o(R),
 \qquad
 \frac{d^3}{R^2}=o(R).
$$



Thus



$$
\log|H_{n,2n+d}|\geq\delta R+o(R),
$$



uniformly in this window.  The saddle does tend to infinity there, so the
qualification preceding the logarithmic formula is satisfied.  The same
gcd-independent inequality from Section 3 eliminates the entire window.

This does not cover offsets comparable to or larger than
$2R/\log R$, nor an arbitrary approach $b/n\to2$.

## 6. Independent finite rational certificate

The original finite probe was recomputed without importing its recurrence or
its fixed-point interval code.  The independent program uses:

1. the closed residue-class formula for $F^{(j)}(0)$;
2. the direct binomial formula for the jets of $e^{-z}F$;
3. ordinary polynomial multiplication for $D^n$;
4. direct factorial sums for $U_b,V_{n,b}$; and
5. exact `Fraction` intervals for $e$ and Machin's formula for $\pi$.

It checked all 7,260 coordinate pairs with



$$
1\leq n\leq60,\qquad 2\leq b\leq4n.
$$



All independently computed $\eta_{n,k}$, $U_b$, and $V_{n,b}$ agree
with the recurrence implementation.  The independent interval has a common
denominator of 2,838 decimal digits.  It certifies:

* for every $2\leq n\leq60$, the unique global minimum in the finite
  range occurs at $b=2$;
* the $n=1$ minimum occurs at $b=3$;
* every reported global and restricted minimum is separated from all
  competitors by a strictly positive rational gap; and
* every minimizer and certification flag agrees with the original result.

The SHA-256 of the complete ordered tuple stream
$(n,b,U_b,V_{n,b},g_{n,b})$ is

```text
848369d010288873fab9869c445a52ec0e2418d75afd8e54cc738e223b287a96
```

These statements are finite exact certificates only.  They are not used to
justify any saddle asymptotic.

The independent artifacts are:

```text
47e83965ecf8dc858732b8cf32e97a3904fa6fdf8df6e9f39714179939827b03  scripts/softened_singularity_endpoint_probe.py
a5c18e1ddab42fff383a0f53899c2cb5d52c111f6423eba54d1ffdab57107c0d  results/softened_singularity_endpoint_n60.json
d874ea89a168a423ab48a64eb2f8e6e30add90ffcad16f92c14731a50f664404  scripts/softened_singularity_independent_audit.py
7a0deb5a45916667894bd1f854ac5d4c35c8a8fbfbd37ee90c2b0350d3ed3ed3  results/softened_singularity_independent_audit_n60.json
```

## 7. Accepted conclusion and limitations

The following statements have survived the audit:

1. the exact integer endpoint form and primitive-gcd convention;
2. integrality of every $\eta_{n,k}$;
3. divergence for every fixed $b\geq2$;
4. divergence on every proportional ray with fixed limiting ratio
   $0<\lambda<2$;
5. the explicit fixed-offset asymptotic at $b=2n+d$; and
6. the growing window
   $0\leq b-2n\leq(2-\delta)\sqrt{2n}/\log\sqrt{2n}$.

The proportional cut estimate degenerates as $\lambda\uparrow2$, and the
moving-saddle estimate has not been proved for the entire remaining
transition range.  No conclusion about the arithmetic nature of $e+\pi$
follows.
