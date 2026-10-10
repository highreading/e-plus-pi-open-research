> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 176 — a native common-polynomial reciprocal Padé ray

Checked: 2026-08-29 (Beijing time)

## Status and outcome

Let



$$
F(z)=4\arctan\frac{z}{2-z},\qquad
 S(z)=e^z+F(z),\qquad S(1)=e+\pi.
$$



This report tests a concrete coupled construction in which the exponential
and period columns have the same polynomial coefficient:



$$
R_n(z)=-1+Q_n(z)e^z+Q_n(z)F(z).
$$



The polynomial $Q_n$ is chosen for maximal cancellation at zero.
Equivalently, $1/Q_n$ is the $[0/n]$ Padé approximant to $S$.

> **PROVED.** The unique such ray satisfies
> 

$$
> R_n(z)=O(z^{n+1}),\qquad
> |R_n(1)|\asymp \rho^{-n}\longrightarrow\infty,
>
$$


> where $\rho\in(2/5,1/2)$ is the modulus of the unique zero of $S$ in
> $|z|<3/5$. After exact denominator clearing and complete endpoint gcd
> reduction, the primitive integer forms also tend to infinity. Their
> absolute values are asymptotic to $e+\pi$ times their primitive heights.

Thus this native common-polynomial Hermite--Padé ray does not merely miss a
Roth threshold: it does not approximate zero at all.

> **EXPERIMENTAL.** The real zero is
> $\rho=0.404821727032308\ldots$. This decimal is diagnostic only; the proof
> uses the exact bracket $2/5<\rho<1/2$.

> **OPEN.** This theorem does not cover the endpoint-only constraint
> $B(1)=C(1)$ with independent polynomials $B,C$, nor other unequal-degree
> or multipoint systems. It does not decide whether $e+\pi$ is rational,
> irrational, algebraic, or transcendental.

## 1. Exact construction and uniqueness

Write



$$
S(z)=\sum_{k\ge0}s_k\frac{z^k}{k!},\qquad
 H(z)=\frac1{S(z)}=\sum_{k\ge0}h_k\frac{z^k}{k!}.
 \tag{1}
$$



The Möbius arctangent jets are



$$
\tau_k=F^{(k)}(0)
 =4(k-1)!2^{-k/2}\sin\frac{k\pi}{4}\in\mathbb Z
 \quad(k\ge1),\qquad \tau_0=0.
 \tag{2}
$$



Hence $s_0=1$ and $s_k=1+\tau_k\in\mathbb Z$ for $k\ge1$.
Hurwitz convolution in $HS=1$ gives



$$
h_0=1,\qquad
 h_n=-\sum_{k=1}^n\binom nk s_kh_{n-k}\in\mathbb Z.
 \tag{3}
$$



Define



$$
Q_n(z)=\sum_{k=0}^nh_k\frac{z^k}{k!}.
 \tag{4}
$$



Then exactly



$$
Q_n(z)S(z)-1
 =-1+Q_n(z)e^z+Q_n(z)F(z)=O(z^{n+1}).
 \tag{5}
$$



This is the unique projective solution with $A$ constant,
$\deg Q\le n$, and identical exponential and period coefficients. The
constant equation fixes $A$ from $Q(0)$; the next $n$ equations give
(3). If $Q(0)=0$, triangularity makes the whole solution zero.

## 2. Exact denominator and primitive endpoint ledger

Since every $h_k$ is integral,



$$
n!Q_n(z)=\sum_{k=0}^nh_k\frac{n!}{k!}z^k\in\mathbb Z[z].
 \tag{6}
$$



Put



$$
W_n=n!Q_n(1)=\sum_{k=0}^nh_k\frac{n!}{k!}\in\mathbb Z,
 \qquad g_n=\gcd(|W_n|,n!).
 \tag{7}
$$



After complete polynomial primitivization and the separate endpoint gcd
reduction, the endpoint form is exactly



$$
\boxed{
 L_n=\frac{W_n}{g_n}(e+\pi)-\frac{n!}{g_n},\qquad
 \gcd\left(\frac{|W_n|}{g_n},\frac{n!}{g_n}\right)=1.}
 \tag{8}
$$



Indeed, any content removed from the full polynomial triple divides both
$W_n$ and $n!$, so it cancels again in (8). No cofactor content is hidden.
The real value is



$$
L_n=\frac{n!}{g_n}\bigl(S(1)Q_n(1)-1\bigr)
     =\frac{n!}{g_n}R_n(1).
 \tag{9}
$$



Since $n!/g_n\ge1$, an analytic lower bound for the raw remainder survives
every possible primitive gcd.

## 3. A unique dominant zero: exact Rouché certificate

The Taylor coefficients of $F$ have the logarithmic form



$$
[z^m]F(z)=\frac{4\operatorname{Im}(\lambda^m)}m,\qquad
 \lambda=\frac{1+i}{2},\qquad |\lambda|=2^{-1/2}.
 \tag{10}
$$



On $|z|=3/5$, compare $S(z)$ with $1+3z$. We have



$$
|1+3z|\ge \frac45,
 \tag{11}
$$



whereas



$$
\begin{aligned}
 |S(z)-(1+3z)|
 &\le e^{3/5}-1-\frac35
   +4\sum_{m\ge2}\frac{(3/(5\sqrt2))^m}{m}\\
 &<\frac7{30}+\frac{15}{28}
  =\frac{323}{420}<\frac45.
 \end{aligned}
 \tag{12}
$$



Rouché's theorem therefore gives exactly one zero, counted with
multiplicity, in $|z|<3/5$.

Here every bound has a short rational certificate. First,



$$
e^{3/5}<1+\frac35+
 \frac{(3/5)^2/2}{1-1/5}
 =\frac{73}{40}<\frac{11}{6},
 \tag{13}
$$



which gives the $7/30$ exponential tail. Next set
$x=3/(5\sqrt2)<3/7$. The function
$-\log(1-x)-x$ is increasing, and



$$
\log\frac74<\frac9{16}
 \tag{14}
$$



because



$$
\sum_{k=0}^3\frac{(9/16)^k}{k!}
 =\frac{14339}{8192}>\frac74.
$$



Consequently,



$$
4[-\log(1-x)-x]
 <4\left(\frac9{16}-\frac37\right)=\frac{15}{28}.
 \tag{15}
$$



The exact Rouché gap is



$$
\frac45-\frac{323}{420}=\frac{13}{420}>0.
 \tag{16}
$$



The zero is real. At the left endpoint,



$$
S(-1/2)=e^{-1/2}-4\arctan(1/5)<-\frac{46}{375}<0,
 \tag{17}
$$



because $e^{-1/2}<2/3$ and



$$
4\arctan(1/5)>
 4\left(\frac15-\frac1{3\cdot5^3}\right)=\frac{296}{375}.
$$



At the other endpoint,



$$
S(-2/5)=e^{-2/5}-4\arctan(1/6)>\frac1{291}>0.
 \tag{18}
$$



Indeed,



$$
e^{2/5}<1+\frac25+
 \frac{(2/5)^2/2}{1-2/15}=\frac{97}{65}<\frac32,
$$



so $e^{-2/5}>65/97$, while $4\arctan(1/6)<2/3$.
Thus the sole zero is



$$
r\in(-1/2,-2/5),\qquad \rho=|r|\in(2/5,1/2).
 \tag{19}
$$



It is simple because on this real interval



$$
S'(x)=e^x+\frac4{x^2-2x+2}>0.
 \tag{20}
$$



## 4. Darboux asymptotics and no decay

The only singularity of $H=1/S$ in $|z|<3/5$ is the simple pole at
$r$. The strict boundary inequality gives a radius $R$ with
$3/5<R<1$ on which subtracting this pole leaves an analytic function.
For $c_n=[z^n]H=h_n/n!$, the residue theorem and Cauchy's estimate give



$$
c_n=-\frac{r^{-n-1}}{S'(r)}+O(R^{-n}).
 \tag{21}
$$



Summing (21) through $n$, using $\rho<1/2<3/5<R$, yields



$$
\boxed{
 Q_n(1)=\frac{r^{-n-1}}{S'(r)(r-1)}(1+o(1)).}
 \tag{22}
$$



Therefore



$$
\boxed{
 R_n(1)=
 \frac{e+\pi}{S'(r)(r-1)}r^{-n-1}(1+o(1)),}
 \tag{23}
$$



and



$$
|R_n(1)|\asymp\rho^{-n}\longrightarrow\infty,\qquad
 |L_n|\ge |R_n(1)|\longrightarrow\infty.
 \tag{24}
$$



This is stronger than a height-capacity failure: the analytic Padé remainder
already diverges at the target point.

## 5. Primitive height

Let



$$
\mathcal H_n=
 \max\left(\frac{|W_n|}{g_n},\frac{n!}{g_n}\right).
 \tag{25}
$$



Since $W_n=n!Q_n(1)$, equation (22) implies



$$
\log\mathcal H_n
 =\log\frac{n!}{g_n}
  +(n+1)\log\frac1\rho
  +\log\left|\frac1{S'(r)(r-1)}\right|+o(1),
 \tag{26}
$$



and



$$
\log|L_n|
 =\log\frac{n!}{g_n}
  +(n+1)\log\frac1\rho
  +\log\left|\frac{e+\pi}{S'(r)(r-1)}\right|+o(1).
 \tag{27}
$$



The gcd appears in both formulas identically and cannot change the result.
Equivalently,



$$
\boxed{\frac{|L_n|}{\mathcal H_n}\longrightarrow e+\pi.}
 \tag{28}
$$



The primitive values are comparable to their heights, not small relative to
them.

## 6. Exact replay and relation to earlier barriers

The certificate checks through $n=200$:

- the differential recurrence for every required $\tau_k$;
- all Hurwitz inverse convolutions $HS=1$;
- integrality of every coefficient of $n!Q_n$;
- exact endpoint pairs, gcds, and primitive coordinates at selected indices;
- every rational inequality in the Rouché and real-root ledgers.

The first reciprocal jets are



$$
1,-3,15,-111,1097,-13549,\ldots.
$$



Their growth is explained by the proved pole; it is not used as evidence.
The floating root diagnostic is marked **EXPERIMENTAL** in the JSON and is
excluded from proof checks.

This ray is not one of the frozen no-go families. The constant-$B=C$
obstruction fixes both coefficients to scalars; endpoint-matched systems
impose only $B(1)=C(1)$; direct common-kernel barriers use sign-controlled
integrals. Here $B=C=Q_n$ as polynomials and both degrees grow. The theorem
therefore closes a genuine intermediate subspace, but only that subspace.

## 7. Artifacts

- sources/item176_route2_native_reciprocal_report.md
- scripts/item176_route2_native_reciprocal_certificate.py
- results/item176_route2_native_reciprocal_certificate.json
- results/item176_route2_native_reciprocal_certificate_replay.json
- results/item176_route2_native_reciprocal_hashes.sha256
