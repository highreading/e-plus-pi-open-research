> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 260 - exact punctured cohomology in the $p\equiv5\pmod 6$ phase

Checked: 2026-08-31 (Beijing time)

## 1. Scope and verdict

Retain an actual ordinary-$j=2$ row with



$$
p\equiv5\pmod 6,\qquad p=6m+2r+9,\qquad r\equiv1\pmod 6. \tag{1.1}
$$



Put



$$
q=\frac{p-5}{6},\qquad
\delta=\frac{r+2}{3},\qquad m=q-\delta,\qquad
n=\frac{p-1}{2},\qquad \epsilon=\left(\frac 2p\right). \tag{1.2}
$$



Thus $\delta$ is a positive odd integer. Item 254 reduced the target to
the punctured moment



$$
S_r=\sum_{x\in\mathbf F_p\setminus\{0,1\}}
\frac{x^{r+4}\chi\!\left(x(1-x^3/2)\right)}{1-x^3},\qquad
H_m=\epsilon(2m+r+5)-S_r. \tag{1.3}
$$



> **PROVED - exact Hermite reduction with an explicit primitive.** On
> 

$$
> E:\quad Y^2=X^3-\frac12,\qquad
> \mathcal L(R)=\left(X^3-\frac12\right)R'+\frac32X^2R, \tag{1.4}
>
$$


> define
> 

$$
> C_0=1,\qquad
> C_j=\prod_{i=0}^{j-1}\frac{6i+5}{3i+4},\qquad
> K_\delta=\sum_{j=0}^{\delta-1}C_j. \tag{1.5}
>
$$


> There is an explicit Laurent polynomial $P_\delta(X)\in\mathbf Q[X^{-1}]$
> for which
> 

$$
> \boxed{
> \frac{X^{-r-1}}{X^3-1}\frac{dX}{Y}
> =\left(\frac{X}{X^3-1}+K_\delta X\right)\frac{dX}{Y}
> -d(P_\delta Y).} \tag{1.6}
>
$$


> All poles and the primitive are retained; no endpoint has been discarded.

> **PROVED - exact finite-field endpoint correction.** For
> 

$$
> \Lambda_p(f)=\sum_{X\in\mathbf F_p^*\setminus\{1\}}
> f(X)\chi\!\left(X^3-\frac12\right), \tag{1.7}
>
$$


> and every $j\equiv1\pmod 3$ with $1\le j\le r$,
> 

$$
> \boxed{\Lambda_p\!\left(\mathcal L(X^{-j})\right)
> =\epsilon\frac{j-3}{2}.} \tag{1.8}
>
$$


> Thus the exact differential in (1.6) does **not** disappear under the
> finite-field point-sum functional. Its contribution is a fixed puncture
> term.

> **PROVED - bounded two-class normal form.** Put
> 

$$
> U_p=\Lambda_p(X),\qquad
> V_p=\Lambda_p\!\left(\frac{X}{X^3-1}\right). \tag{1.9}
>
$$


> Then
> 

$$
> \boxed{S_r=V_p+K_\delta U_p+\epsilon(K_\delta+\delta),} \tag{1.10}
>
$$


> and the two residual coordinates are exactly
> 

$$
> \boxed{U_p=h_q-\epsilon,\qquad V_p=-H_q+\frac{4\epsilon}{3}.} \tag{1.11}
>
$$


> The residual cohomological dimension for this weight family is bounded
> independently of $r$, but one residual coordinate is the original
> moving puncture period. The coordinate $U_p$ represents the
> unpunctured second-kind differential $X\,dX/Y$, not a holomorphic
> differential.

> **PROVED - recovery of the fixed-cutoff boundary formula.** Substitution
> in (1.10) gives
> 

$$
> S_r=-H_q+K_\delta h_q+\epsilon\left(\delta+\frac43\right). \tag{1.12}
>
$$


> Since $2m+r+5\equiv\delta+4/3\pmod p$,
> 

$$
> \boxed{H_{q-\delta}=H_q-K_\delta h_q\pmod p.} \tag{1.13}
>
$$


> Moreover, $K_\delta=B_\delta^{(5)}$ from Item 254. Thus the exact
> cohomological reduction recovers, rather than improves, the universal
> cutoff collision $H_q/h_q=K_\delta$.

> **PROVED, SHARPLY SCOPED NO-GO - ordinary $j=0$ trace data cannot close
> the puncture.** The logarithmic differential
> 

$$
> \omega_{\log}=\frac{X}{X^3-1}\frac{dX}{Y} \tag{1.14}
>
$$


> has, at every geometric point $(\alpha,\beta)$ with
> $\alpha^3=1$ and $\beta^2=1/2$, the nonzero residue
> 

$$
> \boxed{\operatorname {Res}_{(\alpha,\beta)}\omega_{\log}
> =\frac{1}{3\alpha\beta}.} \tag{1.15}
>
$$


> Exact differentials and unpunctured regular or second-kind de Rham
> classes have zero residues. Hence $\omega_{\log}$ cannot be replaced
> by an exact differential plus ordinary unpunctured de Rham trace data.
> The zero unweighted trace of the supersingular $j=0$ curve controls a
> different class.

> **NO ALL-PRIME EXCLUSION / ZERO BOOKING.** The actual row
> 

$$
> (p,r,s,m,\delta)=(47,7,5,4,3) \tag{1.16}
>
$$


> has $H_m=0\pmod p$. A fixed-$r$ ray has only
> $O(\log M)=o(M)$ raw log-prime weight at global index $M$, but that
> zero-rate fact is already the frozen fixed-ray geometry and cannot be
> summed over the linearly many moving $r$'s. Item 260 therefore books
> 

$$
> \boxed{\text{new unconditional Route-1 rate}=0,\qquad
> \text{new \(j=2\) capacity reduction}=0.} \tag{1.17}
>
$$



Every bounded scan in the checker is **EXACT FINITE ONLY**.

## 2. Birational transport and punctures

Set $X=1/x$ and $Y=y/x^2$. Then



$$
y^2=x(1-x^3/2)\quad\longleftrightarrow\quad Y^2=X^3-\frac12. \tag{2.1}
$$



The character factors agree because



$$
x(1-x^3/2)=\frac{X^3-1/2}{X^4}. \tag{2.2}
$$



Also,



$$
\frac{x^{r+4}}{1-x^3}=\frac{X^{-r-1}}{X^3-1}. \tag{2.3}
$$



The domain $x\ne0,1$ becomes $X\in\mathbf F_p^*\setminus\{1\}$.
Because $p\equiv5\pmod 6$, the cube map is bijective, so $X=1$ is
the only rational root of $X^3-1$. Equations (2.1)-(2.3) prove



$$
S_r=\Lambda_p(w_r),\qquad w_r=\frac{X^{-r-1}}{X^3-1}. \tag{2.4}
$$



The geometric punctures of $w_r\,dX/Y$ lie above $X=0$ and
$X^3=1$. The high-order pole at $X=0$ reduces to second-kind and
regular data; the simple poles above $X^3=1$ produce the surviving
logarithmic class.

## 3. Exact Hermite reduction

For every rational function $R(X)$, differentiation on $E$ gives



$$
d(RY)=\left\{\left(X^3-\frac12\right)R'+\frac32X^2R\right\}\frac{dX}{Y}
=\mathcal L(R)\frac{dX}{Y}. \tag{3.1}
$$



The weight has the exact partial-fraction expansion



$$
w_r=\frac{X}{X^3-1}-\sum_{j=0}^{\delta-1}X^{-(3j+2)},
\qquad r+1=3\delta-1. \tag{3.2}
$$



Indeed, multiplication of (3.2) by $X^{3\delta-1}(X^3-1)$ makes the
sum telescope and leaves one.

For $N\equiv2\pmod 3$ and $N\ge5$, direct substitution in (3.1)
yields



$$
X^{-N}-\frac{2N-5}{N-1}X^{-(N-3)}
=\frac{2}{N-1}\mathcal L(X^{-(N-1)}). \tag{3.3}
$$



The terminal identity is



$$
X^{-2}+X=2\mathcal L(X^{-1}). \tag{3.4}
$$



Define $A_2=0$, $C_0=1$, and, for $N=3j+2$, recursively



$$
\begin{aligned}
C_j&=\frac{2N-5}{N-1}C_{j-1},\\
A_N&=\frac{2}{N-1}X^{-(N-1)}+\frac{2N-5}{N-1}A_{N-3}.
\end{aligned} \tag{3.5}
$$



Then



$$
X^{-N}-C_jX^{-2}=\mathcal L(A_N). \tag{3.6}
$$



Summing (3.6), using (3.4), and putting



$$
P_\delta=\sum_{j=0}^{\delta-1}A_{3j+2}+2K_\delta X^{-1} \tag{3.7}
$$



gives



$$
\mathcal L(P_\delta)=\sum_{j=0}^{\delta-1}X^{-(3j+2)}+K_\delta X. \tag{3.8}
$$



Equations (3.1), (3.2), and (3.8) prove (1.6) coefficientwise over
$\mathbf Q$. No finite-field sampling enters this proof.

The recurrence in (3.5) gives



$$
C_j=\prod_{i=0}^{j-1}\frac{6i+5}{3i+4}, \tag{3.9}
$$



so $K_\delta$ is exactly Item 254's $B_\delta^{(5)}$. Every denominator
in (3.3)-(3.9) is at most $r<p$, and every numerator factor in (3.9)
is at most $2r-3<p$. Hence all reductions use $p$-units.

## 4. Why exact differentials contribute to the finite sum

Let $g=X^3-1/2$. Since $n=(p-1)/2$,



$$
\mathcal L(X^{-j})g^n=\frac{d}{dX}\left\{X^{-j}g^{n+1}\right\}. \tag{4.1}
$$



For every integer $e$,



$$
\sum_{X\in\mathbf F_p^*\setminus\{1\}}X^e
=-1-\mathbf1_{p-1\mid e}. \tag{4.2}
$$



Expand the derivative in (4.1). If $j\equiv1\pmod 3$, the exponent
zero never occurs. In the phase range $1\le j\le r<(p-1)/2$, the only
possible nonzero resonant exponent is $p-1$, at $3t=p+j$; its
derivative coefficient is $3t-j=p=0$ in $\mathbf F_p$. No exponent
$-(p-1)$ or $2(p-1)$ lies in the range.

Thus (4.2) leaves only minus the value of (4.1) at $X=1$. Since
$g(1)^n=\epsilon$,



$$
\left.\frac{d}{dX}\left\{X^{-j}g^{n+1}\right\}\right|_{X=1}
=\epsilon\frac{3-j}{2}, \tag{4.3}
$$



which proves (1.8). This calculation retains both omitted finite-field
points: $X=0$ is accounted for by summing Laurent powers on
$\mathbf F_p^*$, and $X=1$ supplies (4.3).

Put



$$
T_N=\Lambda_p(X^{-N}). \tag{4.4}
$$



Equations (3.3) and (1.8) give



$$
T_N=\frac{2N-5}{N-1}T_{N-3}+\epsilon\frac{N-4}{N-1}. \tag{4.5}
$$



If $E_0=0$ and its inhomogeneous recurrence is read from (4.5), then



$$
E_j=C_j-1. \tag{4.6}
$$



Indeed, the induction step is



$$
\frac{2N-5}{N-1}(C_{j-1}-1)+\frac{N-4}{N-1}=C_j-1. \tag{4.7}
$$



The terminal equation (3.4), together with (1.8) at $j=1$, gives



$$
T_2=-U_p-2\epsilon. \tag{4.8}
$$



Therefore



$$
T_{3j+2}=C_jT_2+\epsilon(C_j-1),\qquad
\sum_{j<\delta}T_{3j+2}=K_\delta T_2+\epsilon(K_\delta-\delta). \tag{4.9}
$$



Substitution of (4.9) into (3.2), followed by (4.8), gives (1.10). The
term $\epsilon(K_\delta+\delta)$ is the exact summed endpoint. Dropping
it would confuse de Rham exactness with annihilation by $\Lambda_p$.

## 5. Evaluation of the two residual coordinates

### 5.1. The second-kind coordinate

Expand $g^n$ in



$$
U_p=\sum_{X\ne0,1}Xg(X)^n. \tag{5.1}
$$



On $\mathbf F_p^*$, the unique exponent divisible by $p-1$ satisfies



$$
3t+1=p-1,\qquad t=\frac{p-2}{3}. \tag{5.2}
$$



The complementary binomial index is $q+1$, so the power-sum rule gives



$$
U_p=-h_{q+1}-\epsilon. \tag{5.3}
$$



At $p=6q+5$,



$$
\frac{h_{q+1}}{h_q}=\frac{2q+1}{4q+4}\equiv-1\pmod p, \tag{5.4}
$$



and hence $U_p=h_q-\epsilon$.

### 5.2. The logarithmic puncture coordinate

The cube map is a bijection. Let



$$
e=\frac{2p-1}{3},\qquad 3e\equiv1\pmod{p-1},\qquad
F(y)=y^e(y-1/2)^n. \tag{5.5}
$$



Then



$$
V_p=\sum_{y\ne0,1}\frac{F(y)}{y-1}. \tag{5.6}
$$



Write



$$
Q(y)=\frac{F(y)-F(1)}{y-1}. \tag{5.7}
$$



Here $F(0)=0$, $F(1)=\epsilon$, and



$$
\sum_{y\ne0,1}\frac1{y-1}=1. \tag{5.8}
$$



The degree of $Q$ is below $2(p-1)$, so its full finite-field sum
sees only $[y^{p-1}]Q$. Removing $y=0,1$ and restoring (5.8) gives



$$
V_p=-[y^{p-1}]Q-F'(1). \tag{5.9}
$$



Now



$$
F'(1)=\epsilon(e+2n)=-\frac{4\epsilon}{3}, \tag{5.10}
$$



while



$$
\begin{aligned}
[y^{p-1}]Q
&=\sum_{t=(p+1)/3}^{n}\binom nt(-1/2)^{n-t}\\
&=\sum_{u=0}^{q}\binom nu(-1/2)^u
=H_q\pmod p.
\end{aligned} \tag{5.11}
$$



Equations (5.9)-(5.11) prove the second identity in (1.11).

Finally, (1.10)-(1.11) give (1.12). Since $r=3\delta-2$ and
$m=q-\delta$,



$$
2m+r+5=2q+\delta+3\equiv\delta+\frac43\pmod p, \tag{5.12}
$$



and (1.13) follows.

## 6. The surviving logarithmic class

Let $\alpha^3=1$ and $\beta^2=1/2$. The local parameter
$X-\alpha$ is valid at $(\alpha,\beta)$, and



$$
X^3-1=3\alpha^2(X-\alpha)+O\!\left((X-\alpha)^2\right). \tag{6.1}
$$



Therefore



$$
\operatorname {Res}_{(\alpha,\beta)}
\frac{X}{X^3-1}\frac{dX}{Y}
=\frac{\alpha}{3\alpha^2\beta}
=\frac{1}{3\alpha\beta}\ne0. \tag{6.2}
$$



Every exact differential on a smooth curve has zero residue. Unpunctured
regular and second-kind de Rham representatives also have zero residue at
these six points. This proves the scoped obstruction in (1.15).

The unweighted trace



$$
\sum_X\chi\!\left(X^3-\frac12\right)=0 \tag{6.3}
$$



uses weight $1$. It neither evaluates the unpunctured second-kind
coordinate $U_p$ in (1.9) nor the nonzero-residue class $V_p$.
Equation (5.11) shows exactly what the latter contains: the moving prefix
$H_q$.

This does not prove that every possible punctured Frobenius or $p$-adic
method must fail. It proves that ordinary unpunctured trace data and
Hermite exactness alone cannot remove the remaining coordinate.

## 7. Recurrences, zeros, and rate

Normalize the base puncture period by



$$
Z_q=\frac{H_q}{h_q}. \tag{7.1}
$$



The elementary prefix recurrence gives



$$
\boxed{Z_{q+1}=1+\frac{4q+4}{2q+1}Z_q,\qquad Z_0=1.} \tag{7.2}
$$



Also, if $c_0=1$,



$$
c_{j+1}=c_j\frac{6j+5}{3j+4},\qquad K_{\delta+1}=K_\delta+c_\delta. \tag{7.3}
$$



Thus the $r$-dependence is fixed-order hypergeometric, and every actual
zero is the fixed-rational collision



$$
Z_q=K_\delta\pmod p. \tag{7.4}
$$



But successive $q$'s in (7.2) use different row primes $p=6q+5$.
The recurrence does not propagate a modular nonzero value from one prime
to the next. The exact collision (1.16), where



$$
K_3=\frac{59}{14}, \tag{7.5}
$$



rules out a uniform all-prime theorem for all fixed $r$'s.

For the global Item-219 index $M$, fixed $r$ gives



$$
2M=5r+14s+7. \tag{7.6}
$$



Hence at most one fixed-$r$ row occurs at each $M$, with log-prime
weight $O(\log M)=o(M)$. This fixed-ray zero rate was already available
before the cohomological reduction. Since the positive-mass cell contains
linearly many $r$'s, (7.6) cannot be summed as a new capacity saving.

No all-prime exclusion, uniform zero-density theorem, or positive-mass
weighted theorem follows from (7.2)-(7.4). The booking remains zero.

## 8. Exact replay and strict labels

The standard-library checker performs:

- 67 coefficientwise rational Hermite reductions, including the explicit
  Laurent primitives, telescopic partial fraction, $K_\delta$, and every
  endpoint inhomogeneity;
- all $p\equiv5\pmod 6$ prime-level coordinate identities through
  $p\le401$;
- 1,191 endpoint summation-by-parts identities;
- 605 actual rows and 2,420 localized row equalities;
- an exact finite zero census, finding only (1.16) in that bound.

### PROVED

- the birational transport and complete puncture set;
- the exact Hermite identity (1.6) and all unit bounds;
- the endpoint lemma (1.8) and corrected finite functional (1.10);
- the residual evaluations (1.11) and final normal form (1.13);
- the nonzero-residue obstruction (1.15);
- the recurrence statements and zero booking.

### EXACT FINITE ONLY

- every bounded row count, zero count, digest, and sample in the checker.

### OPEN

- all-prime or weighted control of $Z_q=H_q/h_q$;
- a genuinely arithmetic punctured-Frobenius theorem beyond ordinary trace;
- a uniform theorem when $r$ moves through the positive-mass cell;
- any new Route-1 capacity or conclusion about $e+\pi$.

## 9. Reproduction

From the portable archive root:

```text
python scripts/item260_p5_punctured_cohomology_certificate.py \
  --output results/item260_p5_punctured_cohomology_certificate.json
python scripts/item260_p5_punctured_cohomology_certificate.py \
  --output results/item260_p5_punctured_cohomology_certificate_replay.json
```

The checker uses only Python's standard library and the frozen Item-254
report hash. It contains no timestamp, random seed, elapsed time, or host
path.
