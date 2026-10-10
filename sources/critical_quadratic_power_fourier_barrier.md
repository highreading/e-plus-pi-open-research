> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A critical-scale Fourier barrier for $(1+x^2)^{-k}$

Date: 2026-08-26

## 1. Theorem

For positive even $n$ and integers $k>n$, put



$$
J_{n,k}
 =
 \int_0^1
 \frac{x^n(1-x)^n}{(1+x^2)^k}\,dx.             \tag{1}
$$



The region $k>n$ is automatically log-free: $J_{n,k}$ is a rational
linear form in $1,\pi$, and its $\pi$-coefficient is positive.  The
general coordinate-height estimate gives only
$\exp(O(n+k))$, which reaches factorial scale when
$k\asymp n\log n$.  This note tracks the common Fourier denominator
through primitive reduction and obtains an explicit part of that critical
scale.

Put



$$
\gamma=\frac{1+\sqrt2}{2}.
$$



**Theorem.**  Let $n$ tend to infinity through positive even integers,
and suppose



$$
n<k=k_n\leq\frac1{40}n\log n.                  \tag{2}
$$



Primitive-normalize the $\pi$-form (1), minimally match its
$\pi$-coefficient with the primitive beta-integral $e$-form, and
remove the entire final content.  Then the resulting primitive
$e+\pi$ forms tend to $+\infty$.

More generally, divergence holds along every sequence for which



$$
9(k-1)\log64+9n\log\gamma
 \leq(1-\eta)n\log n                            \tag{3}
$$



for some fixed $\eta>0$ and all sufficiently large $n$.

The proof gives an exact formula for the primitive $\pi$-coefficient.
The large common Fourier denominator $2^{2k-2}$ cancels before
primitive matching.

This is a no-go theorem for one direct-integral construction.  It does not
prove that $e+\pi$ is irrational, algebraic, or transcendental.

## 2. An integer Laurent polynomial

Set



$$
\ell=k-n-1\geq0.
$$



With $x=\tan t$, equation (1) becomes



$$
J_{n,k}
 =
 \int_0^{\pi/4}
 H_{n,k}(t)\,dt,                                \tag{4}
$$



where



$$
H_{n,k}(t)
 =
 \sin^nt\,(\cos t-\sin t)^n
 \cos^{2\ell}t.                                 \tag{5}
$$



Because $n$ and $2\ell$ are even,



$$
H_{n,k}(t)\geq0
$$



for every real $t$, and it is not identically zero.

Put $y=e^{2it}$, $D=2k-2$, and define



$$
G_{n,k}(y)
 =
 i^{-n}(y-1)^n
 \bigl((1+i)y+1-i\bigr)^n
 (y+1)^{2\ell}.                                \tag{6}
$$



Since $n$ is even,



$$
G_{n,k}(y)\in\mathbb Z[i][y],
\qquad \deg G_{n,k}=D.
$$



Direct substitution of



$$
\sin t=\frac{e^{it}-e^{-it}}{2i},
\qquad
 \cos t=\frac{e^{it}+e^{-it}}2
$$



into (5) gives the exact Laurent identity



$$
H_{n,k}(t)
 =
 2^{-D}y^{-(k-1)}G_{n,k}(y).                    \tag{7}
$$



For $-(k-1)\leq m\leq k-1$, set



$$
C_m=[y^{\,k-1+m}]G_{n,k}(y).
$$



Reality of $H_{n,k}$ on the unit circle gives



$$
C_{-m}=\overline{C_m}.
$$



Write



$$
C_0\in\mathbb Z,\qquad
 C_m=A_m+iB_m
 \quad(1\leq m\leq k-1),
\qquad A_m,B_m\in\mathbb Z.                    \tag{8}
$$



Then (7) is the exact real Fourier expansion



$$
H_{n,k}(t)
 =
 2^{-D}
 \left[
 C_0+
 2\sum_{m=1}^{k-1}
 \bigl(A_m\cos(2mt)-B_m\sin(2mt)\bigr)
 \right].                                      \tag{9}
$$



The constant coefficient is the full-period mean multiplied by $2^D$.
Consequently,



$$
C_0>0.                                        \tag{10}
$$



## 3. Exact rational and $\pi$ coordinates

Define the integers



$$
s_m=\sin\frac{m\pi}{2}\in\{0,1,-1\},
\qquad
 c_m=\cos\frac{m\pi}{2}\in\{0,1,-1\},
$$



and



$$
N_m=A_ms_m-B_m(1-c_m)\in\mathbb Z.             \tag{11}
$$



Termwise integration of (9) on $[0,\pi/4]$ gives



$$
J_{n,k}
 =
 2^{-D}
 \left[
 \frac{C_0}{4}\pi+
 \sum_{m=1}^{k-1}\frac{N_m}{m}
 \right].                                      \tag{12}
$$



Put



$$
L_k=\operatorname{lcm}(1,2,\ldots,k-1)
$$



and



$$
T_{n,k}
 =
 \sum_{m=1}^{k-1}\frac{L_k}{m}N_m\in\mathbb Z.  \tag{13}
$$



Then



$$
J_{n,k}
 =
 \frac1{2^DL_k}
 \left(
 T_{n,k}+\frac{L_kC_0}{4}\pi
 \right).                                      \tag{14}
$$



Let



$$
h_{n,k}=\gcd(4T_{n,k},L_kC_0).
$$



Multiplication of (14) by $2^D4L_k/h_{n,k}$ proves that its primitive
integer normalization is exactly



$$
\mathcal L_{n,k}
 =
 A_{n,k}+B_{n,k}\pi
 =
 \frac{4T_{n,k}+L_kC_0\pi}{h_{n,k}},            \tag{15}
$$



where



$$
A_{n,k}=\frac{4T_{n,k}}{h_{n,k}},
\qquad
 B_{n,k}=\frac{L_kC_0}{h_{n,k}}>0.              \tag{16}
$$



The multiplier in (15) is positive.  Since $J_{n,k}>0$,



$$
\mathcal L_{n,k}>0.                            \tag{17}
$$



Equations (15)--(16) display the crucial cancellation: the common
denominator $2^D=2^{2k-2}$ is absent from the primitive pair.  The only
new denominator in the rational Fourier coordinate is $L_k$.

## 4. An explicit primitive-coefficient bound

The elementary identity



$$
\sin t(\cos t-\sin t)
 =
 \frac{\sin2t+\cos2t-1}{2}
$$



gives



$$
\left|\sin t(\cos t-\sin t)\right|
 \leq\gamma
$$



for every real $t$.  Since $|\cos t|\leq1$, equations (5) and (10)
give



$$
0<C_0
 =
 2^D\frac1{2\pi}\int_0^{2\pi}H_{n,k}(t)\,dt
 \leq2^D\gamma^n.                              \tag{18}
$$



The elementary least-common-multiple bound



$$
L_k\leq16^{k-1}                                \tag{19}
$$



now implies, directly from (16),



$$
B_{n,k}
 \leq L_kC_0
 \leq64^{k-1}\gamma^n.                         \tag{20}
$$



For completeness, (19) follows by writing
$\mathcal D_m=\operatorname{lcm}(1,\ldots,m)$, observing



$$
\mathcal D_{2m}\mid
 \mathcal D_m\binom{2m}{m},
$$



and using $\binom{2m}{m}\leq4^m$, followed by iteration and
monotonicity.  The constant $16$ is deliberately elementary; no prime
number theorem is used.

## 5. Fully primitive matching

For even $n$, let



$$
E_n=q_ne-p_n
 =
 \frac1{n!}\int_0^1x^n(1-x)^ne^x\,dx>0.
$$



The endpoint formulas and adjacent determinant give



$$
\gcd(p_n,q_n)=1,
\qquad
 q_n\geq n^n.                                   \tag{21}
$$



Put



$$
d=\gcd(q_n,B_{n,k}),\qquad
 q_n=dq_0,\qquad B_{n,k}=dB_0.
$$



Minimal coefficient matching gives the positive raw $e+\pi$ form



$$
W_{n,k}
 =
 B_0E_n+q_0\mathcal L_{n,k}.                    \tag{22}
$$



Its constant coefficient is



$$
-B_0p_n+q_0A_{n,k},
$$



and its common $e,\pi$-coefficient is



$$
\frac{q_nB_{n,k}}d.
$$



Let $g_{n,k}$ be their full common content.  If a prime divides $q_0$,
then $B_0p_n$ is a unit modulo that prime.  If a prime divides $B_0$,
then $q_0A_{n,k}$ is a unit modulo that prime.  Hence



$$
\gcd(-B_0p_n+q_0A_{n,k},q_0B_0)=1
$$



and, prime-power by prime-power,



$$
g_{n,k}\mid d.                                \tag{23}
$$



Salikhov's irrationality-measure estimate for $\pi$, weakened to the
integer exponent $8$, gives a constant $c_\pi>0$ such that



$$
|A+B\pi|\geq c_\pi B^{-7}
$$



for every $A\in\mathbb Z$ and $B\in\mathbb Z_{>0}$.  Therefore



$$
\begin{aligned}
 \frac{W_{n,k}}{g_{n,k}}
 &\geq
 \frac{q_0\mathcal L_{n,k}}{g_{n,k}}\\
 &\geq
 \frac{q_n|\mathcal L_{n,k}|}{B_{n,k}^2}\\
 &\geq
 c_\pi\frac{q_n}{B_{n,k}^9}.                   \tag{24}
 \end{aligned}
$$



The exponent $9$ is correct: the irrationality estimate contributes
$B^{-7}$, while minimal matching and the worst possible final content
contribute another $B^{-2}$.

Combining (20), (21), and (24) gives



$$
\log\frac{W_{n,k}}{g_{n,k}}
 \geq
 n\log n
 -9(k-1)\log64
 -9n\log\gamma
 +\log c_\pi.                                   \tag{25}
$$



Condition (3) makes the right side at least



$$
\eta n\log n+O(n),
$$



which tends to $+\infty$.  This proves the general criterion.

Finally, $9\log64<40$.  Under (2), equation (25) becomes



$$
\log\frac{W_{n,k}}{g_{n,k}}
 \geq
 \left(1-\frac{9\log64}{40}\right)n\log n
 -9n\log\gamma+O(1),
$$



and the positive $n\log n$ coefficient proves the displayed theorem.

Reference for the irrationality estimate: V. Kh. Salikhov, “On the
irrationality measure of $\pi$,” Russian Mathematical Surveys 63:3
(2008), 570–572,
[DOI 10.1070/RM2008v063n03ABEH004543](https://doi.org/10.1070/RM2008v063n03ABEH004543).

## 6. Finite computational validation

The script

    scripts/critical_quadratic_power_fourier_probe.py

constructs $G_{n,k}$ with exact Gaussian-integer arithmetic, checks the
conjugate Fourier symmetry, computes $C_0,T_{n,k},h_{n,k},B_{n,k}$,
tests the two bounds in (18)--(20), and compares (12) with independent
70-digit quadrature.  The frozen summary is

    results/critical_quadratic_power_fourier_probe.json

All 37 tested cases, with even $2\leq n\leq20$ and four representative
orders between $n+1$ and $2n$, passed.  This is validation only; no
finite computation is used in the proof.

## 7. Limitations

The theorem reaches a fixed positive fraction of the critical
$n\log n$ scale, but not all of it.  Its losses are explicit:

1. the elementary estimate $L_k\leq16^{k-1}$;
2. the coefficient bound $C_0\leq2^{2k-2}\gamma^n$;
3. the deliberately rounded irrationality exponent $8$;
4. the worst-case primitive-content loss $B_{n,k}^2$.

Additional divisibility of $C_0,T_{n,k}$, a sharper least-common-multiple
estimate, or a direct gcd theorem could enlarge the constant in (2).
Nothing here proves that larger $k$ succeeds.  The region



$$
\frac1{40}n\log n<k
$$



remains outside this particular quantitative obstruction.
