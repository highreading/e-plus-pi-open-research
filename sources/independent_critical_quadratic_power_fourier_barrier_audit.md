> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the critical quadratic-power Fourier barrier

Date: 2026-08-26

## Verdict

**ACCEPT.**  Every Laurent/Fourier index, the exact primitive coordinate
pair, positivity and the bound for $C_0$, the elementary LCM estimate, the
prime-power content argument, the exponent $B^9$, and the explicit
$1/40$ arithmetic rederive correctly.  The finite script and archived
summary are also internally consistent, but no finite calculation is
needed for the theorem.

The frozen artifact hashes are

* `sources/critical_quadratic_power_fourier_barrier.md`:
  `b18623356be658ad9a694498e77a2c16bffc0e4e6e0221a00d7ea149aa7a0650`;
* `scripts/critical_quadratic_power_fourier_probe.py`:
  `b348ca14b029aef921c7117381e889d56fe9333900d2e8fd6b3a42de8765edf1`;
* `results/critical_quadratic_power_fourier_probe.json`:
  `452f98814c5bc39ea939241c87c5f5665a06c261389cca299fa9a83051003d12`.

## 1. Exact Laurent and Fourier indexing

Let $n$ be positive and even, $k>n$, and

$$
\ell=k-n-1,\qquad D=2k-2,
\qquad y=e^{2it}.
$$

The substitution $x=\tan t$ gives

$$
J_{n,k}=\int_0^{\pi/4}H_{n,k}(t)\,dt,
$$

where

$$
H_{n,k}(t)=
\sin^nt\,(\cos t-\sin t)^n\cos^{2\ell}t.
$$

Using

$$
\sin t=e^{-it}\frac{y-1}{2i},\qquad
\cos t-\sin t=e^{-it}\frac{(1+i)y+1-i}{2},
\qquad
\cos t=e^{-it}\frac{y+1}{2},
$$

the total power of $2$ in the denominator is

$$
n+n+2\ell=2k-2=D,
$$

and the total exponential factor is

$$
e^{-iDt}=y^{-D/2}=y^{-(k-1)}.
$$

Thus

$$
H_{n,k}(t)
=2^{-D}y^{-(k-1)}G_{n,k}(y),
$$

with

$$
G_{n,k}(y)=i^{-n}(y-1)^n
((1+i)y+1-i)^n(y+1)^{2\ell}.
$$

The polynomial degree is
$n+n+2\ell=D$ and its coefficients are Gaussian integers.  The coefficient
of Fourier frequency $m$ is therefore exactly

$$
C_m=[y^{k-1+m}]G_{n,k}(y),
\qquad -(k-1)\le m\le k-1.
$$

Reality of $H_{n,k}$ on the unit circle gives
$C_{-m}=\overline{C_m}$.  In particular, the central coefficient is real
and, being a Gaussian integer, lies in $\mathbb Z$.  Writing
$C_m=A_m+iB_m$ for $m>0$, conjugate pairing gives

$$
C_me^{2imt}+\overline{C_m}e^{-2imt}
=2(A_m\cos(2mt)-B_m\sin(2mt)),
$$

so every sign in the real Fourier expansion (9) is correct.

Because $n$ and $2\ell$ are even, $H_{n,k}$ is nonnegative on the entire
real line and is not identically zero.  Its full-period average is
$2^{-D}C_0$, whence

$$
C_0=2^D\frac1{2\pi}\int_0^{2\pi}H_{n,k}(t)\,dt>0.
$$

This proves positivity symbolically; it is not inferred from the finite
data.

## 2. Exact rational and $\pi$ coordinates

For $m\ge1$,

$$
\int_0^{\pi/4}\cos(2mt)\,dt
=\frac{\sin(m\pi/2)}{2m},
$$

and

$$
\int_0^{\pi/4}\sin(2mt)\,dt
=\frac{1-\cos(m\pi/2)}{2m}.
$$

The sine and cosine values belong to $\{0,1,-1\}$.  Therefore, with

$$
N_m=A_m\sin(m\pi/2)-B_m(1-\cos(m\pi/2)),
$$

termwise integration gives exactly

$$
J_{n,k}
=2^{-D}\left(\frac{C_0}{4}\pi
+\sum_{m=1}^{k-1}\frac{N_m}{m}\right).
$$

Let

$$
L_k=\operatorname{lcm}(1,\ldots,k-1),
\qquad
T_{n,k}=\sum_{m=1}^{k-1}\frac{L_k}{m}N_m\in\mathbb Z.
$$

Then

$$
J_{n,k}
=\frac1{2^DL_k}\left(T_{n,k}+\frac{L_kC_0}{4}\pi\right).
$$

The factor $2^DL_k$ is a common rational scale and has no effect on the
primitive integer direction.  Multiplication by $4$ leaves the integer
pair

$$
(4T_{n,k},L_kC_0).
$$

Hence, with

$$
h_{n,k}=\gcd(4T_{n,k},L_kC_0),
$$

the primitive pair is exactly

$$
(A_{n,k},B_{n,k})
=\left(\frac{4T_{n,k}}{h_{n,k}},
       \frac{L_kC_0}{h_{n,k}}\right).
$$

This handles every zero case as well.  If $T_{n,k}=0$, then
$h_{n,k}=L_kC_0$ and the primitive pair is $(0,1)$.  Since $C_0>0$, the
second coordinate never vanishes.  The normalizing multiplier is positive,
and the original integral is positive, so

$$
\mathcal L_{n,k}=A_{n,k}+B_{n,k}\pi>0,
\qquad B_{n,k}>0.
$$

The source's central cancellation claim is therefore exact:
$2^D=2^{2k-2}$ disappears before coefficient matching rather than being
estimated as part of the primitive height.

## 3. Bounds for $C_0$, $L_k$, and $B_{n,k}$

The elementary identity

$$
\sin t(\cos t-\sin t)
=\frac{\sin2t+\cos2t-1}{2}
$$

and $-\sqrt2\le\sin2t+\cos2t\le\sqrt2$ give

$$
|\sin t(\cos t-\sin t)|
\le\frac{1+\sqrt2}{2}=\gamma.
$$

Since $|\cos t|\le1$,
$0\le H_{n,k}(t)\le\gamma^n$.  Averaging therefore yields

$$
0<C_0\le2^D\gamma^n.
$$

For completeness, the asserted LCM estimate also follows with all prime
powers accounted for.  Put
$\mathcal D_m=\operatorname{lcm}(1,\ldots,m)$.  If a prime power
$p^a\le2m$ already satisfies $p^a\le m$, it divides $\mathcal D_m$.  If
$m<p^a\le2m$, then $p^{a-1}\le m$ and the carry in
$\binom{2m}{m}$ supplies an additional factor $p$.  Hence

$$
\mathcal D_{2m}\mid\mathcal D_m\binom{2m}{m}
$$

and

$$
\mathcal D_{2m}\le4^m\mathcal D_m.
$$

Iteration at powers of two gives
$\mathcal D_{2^r}\le4^{2^r-1}$.  For arbitrary $m$, choose the next power
of two, which is less than $2m$; monotonicity then gives the deliberately
coarse but elementary bound

$$
\mathcal D_m\le16^m.
$$

Taking $m=k-1$, and using $h_{n,k}\ge1$, gives

$$
B_{n,k}
\le L_kC_0
\le16^{k-1}2^{2k-2}\gamma^n
=64^{k-1}\gamma^n.
$$

No untracked factorial denominator occurs.

## 4. Fully primitive matching and the $B^9$ loss

Let $q_ne-p_n>0$ be the primitive exponential beta form.  For positive
even $n$,

$$
\gcd(p_n,q_n)=1,
\qquad q_n\ge n^n.
$$

Put

$$
d=\gcd(q_n,B_{n,k}),\quad
q_n=dq_0,\quad B_{n,k}=dB_0.
$$

The minimal positive target multipliers are $B_0$ and $q_0$.  The common
coefficient is $q_nB_{n,k}/d$, and the matched constant is

$$
M=-B_0p_n+q_0A_{n,k}.
$$

If a prime divides $q_0$, it divides neither $B_0$ nor $p_n$, so it cannot
divide $M$.  If it divides $B_0$, it divides neither $q_0$ nor
$A_{n,k}$, so again it cannot divide $M$.  Thus the full final content
$g$ satisfies, prime-power by prime-power,

$$
g\mid d.
$$

If $M=0$, the same congruences force $q_0B_0=1$, in which case the common
coefficient is $d$ and $g=d$; the conclusion still holds.

Both input forms are positive and both target coefficients are positive,
so the raw matched value is the positive sum

$$
W=B_0E_n+q_0\mathcal L_{n,k}.
$$

The uniform integer-form consequence of Salikhov's irrationality measure
is

$$
|A+B\pi|\ge c_\pi B^{-7}.
$$

Since $dg\le B_{n,k}^2$, it follows that

$$
\frac Wg
\ge\frac{q_n|\mathcal L_{n,k}|}{B_{n,k}^2}
\ge c_\pi\frac{q_n}{B_{n,k}^9}.
$$

Seven powers of $B$ come from the weakened irrationality exponent and
exactly two from the worst possible minimal-matching/content loss.  There
is no opposite-sign cancellation branch in this automatic region.

## 5. General criterion and the explicit $1/40$

Substitution of the coefficient bound and $q_n\ge n^n$ gives

$$
\log\frac Wg
\ge n\log n-9(k-1)\log64-9n\log\gamma+\log c_\pi.
$$

Thus condition

$$
9(k-1)\log64+9n\log\gamma
\le(1-\eta)n\log n
$$

makes the right side at least
$\eta n\log n+\log c_\pi$, which tends to infinity.  This proves the
general criterion without any suppressed dependence on the index density.

The numerical inequality used for the displayed $1/40$ can be certified
without floating point.  The positive exponential series gives

$$
e^{7/10}>
1+\frac7{10}+\frac{(7/10)^2}{2}
+\frac{(7/10)^3}{6}
=\frac{12013}{6000}>2.
$$

Hence $\log2<7/10$, and therefore

$$
9\log64=54\log2
<\frac{189}{5}=37.8<40.
$$

If $k\le n\log n/40$, then

$$
\log\frac Wg
\ge
\left(1-\frac{9\log64}{40}\right)n\log n
-9n\log\gamma+O(1).
$$

The coefficient of $n\log n$ is strictly positive, while the remaining
loss is only linear in $n$.  Therefore the positive primitive forms tend
to $+\infty$.

## 6. Independent computation and artifact validation

I reran all 37 archived script cases.  The exact sample values of
$C_0,L_k,T,h$, and primitive $B$ match the summary, and the largest
observed relative quadrature error is again
`5.2637792e-57`.  The archived JSON is intentionally a compact summary,
not the script's full printed case list; the source describes it accurately
as a frozen summary.

As a separate exact check, independent Gaussian-rational code compared the
Fourier coordinates with the local Laurent/antiderivative coordinates for
28 cases with even $2\le n\le14$ and
$n+1\le k\le n+4$.  In every case it verified

$$
-\frac{v_{n,k}}2=\frac{C_0}{2^D4},
\qquad
R_{n,k}=\frac{T_{n,k}}{2^DL_k},
$$

and reproduced the primitive pair.  The exact exponential-series
calculation above independently checked the $1/40$ margin.

The source, script, and result are strict UTF-8 and LF-only, with no
forbidden C0 controls or replacement characters.  The source has 47
ordered display pairs, 73 ordered inline pairs, and the complete sequential
tag list 1 through 25.  The script parses as Python, the result parses as
strict integer-valued JSON, and a Pandoc render of the source exits
successfully.

The accepted conclusion is only a no-go result for this Fourier-integral
construction through the stated positive fraction of the critical
$n\log n$ scale.  It neither proves success beyond that scale nor makes an
unconditional arithmetic assertion about $e+\pi$.
