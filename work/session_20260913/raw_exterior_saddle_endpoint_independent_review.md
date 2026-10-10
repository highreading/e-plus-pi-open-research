> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the exterior saddle and endpoint control

Date: 2026-09-13. Reviewer: audit_sources.
Status: PASS. No mathematical correction required.

Reviewed raw_dual_exterior_saddle_and_endpoint_control.md in full. Its global middle-arc inequality and its actual multiplier hypothesis remain conditional in that source; they are not consequences of this review.

## 1. Reversal, phase, and the closed primitive

The exact reversal produces $z^n f_m(-1/z^2)\widetilde R_n(1/z)$. After division by the original denominator, its nth-power rational factor is $D/[z(z-1)]$, and the remaining factor is $1/[z(z-1)]$. For even $n$, the real-normalized exterior logarithms reproduce this expression with the stated sign. Differentiating gives (4), including $+z^{-3}L'(-z^{-2})$.

Writing $\chi=1/[1-w+\sqrt{1-w+w^2}]$ gives


$$
w=\frac{2\chi-1}{\chi(2-\chi)},\qquad
L'(w)=\frac{\chi(2-\chi)}{1+\chi}.
$$


Their product differential is
$d\chi[1/\chi+1/(2-\chi)-2/(1+\chi)]$, proving the primitive. Its multiplicative constant gives value one at $\chi=1/2$. The chosen Schur branch has no zero in the disk and cannot take the values $2,-1$, so the analytic continuation is legitimate.

I independently checked the exact saddle identities:


$$
\mathcal H'(-\phi)=0,\quad
\mathcal H''(-\phi)=\frac{25-11\sqrt5}{4}>0,\quad
e^{2\mathcal H(-\phi)}=\frac{27}{4}\rho^5.
$$


Direct symbolic reductions of the derivative, curvature, primitive differential and exponential value all gave zero residuals. On the interior sheet the derivative at $-\phi$ is instead $2-2/\sqrt5>0$, while it vanishes at $\rho$. This verifies the warning about the extraneous sheet.

## 2. The residue and its original scalar

With $S(t)=(1+t^2)^nU(t)$,


$$
D(z)^n v(z)=z^{3n}S(1/z)/(n!V(1)).
$$


Since $n+1$ is odd, replacing $(z-1)^{-n-1}$ by $-(1-z)^{-n-1}$ gives


$$
\operatorname{Res}_0 I
=-\frac1{n!V(1)}\sum_{k=n}^{3n}[t^k]S\,\binom{k}{n}.
$$


The sum is $S^{(n)}(1)/n!=\widehat Q(1)=Z$. Therefore the residue is exactly $-Z/(n!V(1))$, without another factorial.

If $\gamma_R-\gamma_L$ winds once counterclockwise around zero, its integral difference is $2\pi i$ times that residue. Multiplication by the original $n!V(1)/(2i)$ gives
$I_R-R_a=-\pi Z$, hence $R_a=I_R+\pi Z$. Both the sign and the $\pi$ factor check.

## 3. Contour and endpoints

The left circle arc is oriented clockwise from $-i$ to $i$, and its tangent at $-\phi$ points upward. Its region of deformation from the left unit semicircle lies entirely in the left half-plane and crosses neither pole. The endpoints are zeros of $D^n$, not new poles.

The circle equation gives exactly


$$
|z|^2=1+a,\quad |D|=\sqrt5\,a,\quad |z-1|^2=2+3a,
\quad(\Im z)^2=1+a-a^2.
$$


The polynomial root bound and the Hardy evaluation inequality then give precisely the nth-power expression in (11). Its comparison with $(\sqrt5a)^n$ follows by squaring: the required difference is $6a+8a^2+3a^3\ge0$.

On $0\le a\le1/8$, the arclength derivative is below two, the rational prefactor is at most $1/\sqrt2$, and the Hardy loss is at most $C_*\sqrt{(1+a)/a}$. Integrating $a^{n-1/2}$ proves (12) with its safe constant four. This accounts for both endpoints and the original factor $1/(2i)$. The endpoint exponential base $\sqrt5/8$ is strictly below $\tau$.

## 4. The conditional middle and local saddle calculation

The expression $E(a)$ is exactly $e^{2\Re\mathcal H}$: the rational modulus contributes $5a^2/[(1+a)(2+3a)]$, and the base factor contributes the modulus of the closed primitive. Local curvature does not prove its strict global maximum; the source correctly keeps that inequality open.

Conditional on the global phase gap and a suitable nonzero actual multiplier limit, the Gaussian prefactor in (15) is correct. At the saddle,
$z(z-1)=\phi^3$, and $dz=i\,dy$ along the upward tangent. Combined with $1/(2i)$, this produces $\rho^3/2$, followed by the stated Gaussian factor.

The subsequently derived actual multiplier has an explicit parity factor; its use must replace the source's hypothetical single signed limit when the final saddle theorem is assembled. Nothing in the present contour proof removes that factor.

The note retains the original $u_n=(2n)![t^n]V_n$ normalization and does not convert an estimate relative to $u_n$ into a primitive irrationality form. All these scope distinctions are correct.

