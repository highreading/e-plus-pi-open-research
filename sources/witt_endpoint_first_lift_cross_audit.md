> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Cross-audit of the Witt endpoint first-lift formulas

Date: 2026-08-28

## Verdict

No mathematical flaw was found in equations (2.4), (4.10), or (4.13) of
`sources/witt_endpoint_first_lift.md`.  Their signs, indices, divisions, and
integrality qualifications are correct.  The claim about eventual
integrality on each fixed positive-mass item-149 band is also correct, with
the tail qualification recorded below.

## 1. Universal endpoint lift: equation (2.4)

For a pole term $c_{\alpha,d+1}(x-\alpha)^{-d-1}dx$, define



$$
\Delta_{\alpha,d}=(1-\alpha)^{-d}-(-\alpha)^{-d}.
$$



Direct integration gives



$$
\int_0^1{c_{\alpha,d+1}\,dx\over(x-\alpha)^{d+1}}
=-{c_{\alpha,d+1}\Delta_{\alpha,d}\over d}.                  \tag{1.1}
$$



Thus the minus signs in both pole sums of (2.4) are correct.  Polynomial
terms have the positive primitive $h_n/(n+1)$.

If $d=pk$, multiplication by $p$ leaves the resonant contribution
$-c\Delta/k$; hence the pole indices are



$$
j=d+1=pk+1,
$$



not $pk$.  Likewise the polynomial resonant indices are



$$
n+1=pk,\qquad n=pk-1.
$$



The hypotheses $J_\alpha\le p^2$ and polynomial degree at most
$p^2-2$ imply



$$
d\le p^2-1,qquad n+1\le p^2-1.
$$



No primitive denominator is divisible by $p^2$.  All partial-fraction
coefficients and endpoint powers are $p$-integral because the poles are
separable and avoid $0,1$.  Therefore $pR$ is integral and the split
between the modulo-$p^2$ resonant line and the $p$-multiple of the
nonresonant line in (2.4) is exact.

## 2. Rank-one determinant: equation (4.10)

Write $X_s=pR_s$, and lift the common Cartier vector as



$$
X_s=\gamma_sV_R+px_s,qquad
L_s=\gamma_sV_L+p\ell_s.                                     \tag{2.1}
$$



Equation (4.9) says



$$
\gamma_1x_0-\gamma_0x_1=B-pR(\eta),
$$





$$
\gamma_1\ell_0-\gamma_0\ell_1=-L(\eta).                     \tag{2.2}
$$



Expanding the wedge once gives



$$
\begin{aligned}
{L_1X_0-L_0X_1\over p}
&\equiv
V_L(\gamma_1x_0-\gamma_0x_1)
+V_R(\gamma_0\ell_1-\gamma_1\ell_0)\\
&=V_L\bigl(B-pR(\eta)\bigr)+V_RL(\eta)\pmod p.
\end{aligned}                                                \tag{2.3}
$$



This is exactly (4.10), including the plus sign before $V_RL(\eta)$.
No division by $\gamma_0$ or $\gamma_1$ occurs, so zero Cartier scalars
cause no singularity in the formula.

## 3. Rank-zero determinant: equation (4.13)

For $P_s=T_s'$, the identity



$$
F_s^pP_s\,dx=d(F_s^pT_s)-p\eta_s
$$



gives



$$
X_s=p\bigl(B_s-pR(\eta_s)\bigr),
\qquad L_s=p\bigl(-L(\eta_s)\bigr).                           \tag{3.1}
$$



Consequently



$$
\begin{aligned}
{L_1X_0-L_0X_1\over p^2}
\equiv{}&(-L(\eta_1))(B_0-pR(\eta_0))\\
&-(-L(\eta_0))(B_1-pR(\eta_1))\pmod p,
\end{aligned}                                                \tag{3.2}
$$



which confirms every sign in (4.13).  When $\deg P_s\le p-2$, the
primitive $T_s$ is $p$-integral because its denominators range only
from $1$ to $p-1$.

## 4. Sharp integrality boundary for $pR(\eta)$

If $F$ has pole order $h$, then



$$
\eta=F^{p-1}F'T\,dx
$$



has maximal pole order



$$
h(p-1)+(h+1)=hp+1.                                           \tag{4.1}
$$



If $h\le p-1$, then $hp+1\le p^2-p+1$, so every primitive pole
denominator is strictly below $p^2$; under the analogous polynomial-degree
bound, $pR(\eta)$ is integral.  If $h=p$, a term of order
$p^2+1$ may occur, whose primitive denominator is $p^2$.  Then
$pR(\eta)$ need not be integral.  The qualification before (4.10) is
therefore necessary and sharp at this level.

## 5. Fixed item-149 bands and the moving tail

On a fixed prime-number-theorem band of item 149, the floor values



$$
a=\left\lfloor{6m\over p}\right\rfloor,
\qquad b=\left\lfloor{4m+1\over p}\right\rfloor
$$



are fixed.  Hence the common factor



$$
F={u^a\over Q^{b+1}}
$$



has fixed pole order $h=b+1$, while $p\asymp m\to\infty$.  Thus
$h\le p-1$ eventually.  The polynomial-quotient degree of $\eta$ is
only $O(p)$, with a constant depending on that fixed band, and is
eventually below $p^2-2$.  The integrality hypothesis used in (4.10)
therefore holds uniformly for all sufficiently large primes in each fixed
band.

This statement should not be read as a uniform bound over band labels that
grow with $m$.  However, the union of item-149 bands beyond a fixed label
$J$ has total Chebyshev/PNT weight $O(m/J)$.  Any genuinely positive
logarithmic mass can therefore be captured, up to an arbitrarily small
loss, in finitely many fixed bands, where the preceding eventual argument
applies.

## Final classification

- **PROVED:** equations (2.4), (4.10), and (4.13), including signs and
  integrality conditions; eventual applicability on every fixed
  positive-mass band.
- **CAUTION:** the moving tail is controlled by truncation in total prime
  weight, not by one uniform pole-order bound over all band labels.
- **OPEN:** any positive-mass vanishing theorem for the resulting lifted
  determinant.
