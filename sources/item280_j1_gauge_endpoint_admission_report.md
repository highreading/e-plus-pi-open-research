> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 280 — actual $j=1$ gauge-to-endpoint admission

Checked: 2026-08-31 (Beijing time)

## 1. Verdict

Retain an actual $j=1$ row



$$
p=4h+6s+3,\qquad h,s\geq1,\qquad p\text{ prime}.
$$



Primality forces $3\nmid h$.  Let $E_h^*$ be Item 222's phase
eliminant, let $c_h^*$ be the common lower/upper Gosper residual of
Items 229 and 236, and let $K_h$ be Item 231's natural endpoint scalar.

> **PROVED — exact simultaneous arithmetic localization.**  Every
> original common-log collision on an actual row satisfies
> 

$$
> E_h^*\equiv K_h\equiv0\pmod p.                    \tag{1.1}
>
$$


> Every denominator in (1.1) is a $p$-unit.  Consequently, if
> $N_E(h)$ and $N_K(h)$ are the reduced integer numerators, then
> 

$$
> \boxed{p\mid \gcd\bigl(N_E(h),N_K(h)\bigr).}       \tag{1.2}
>
$$



The proof uses Item 243's all-$h$ gauge



$$
c_h^*=\mathcal R_hE_h^*,                              \tag{1.3}
$$



whose factor $\mathcal R_h$ is an actual-row unit.  It then eliminates
the two endpoint equations without dividing by either endpoint
coefficient.

> **OPEN — arithmetic codimension.**  Equation (1.2) is the smallest
> exact integer restatement furnished by the gauge.  No all-$h$
> localized gcd/resultant theorem proves that $K_h$ is redundant after
> $E_h^*=0$, and no theorem proves that it supplies an independent
> codimension.  The attractive finite gcd pattern remains
> **EXACT FINITE ONLY**.

The inherited individual-height estimate sums to
$O(H^2\log H)$ over $h\leq H$, not $o(H)$.  Hence there is no
weighted-prime-mass saving and



$$
\boxed{\text{new Route-1 booking}=0.}                 \tag{1.4}
$$



## 2. Division-free endpoint elimination

Put



$$
s_*=-\frac{4h+3}{6}.
$$



Items 222 and 243 give, on every collision,



$$
E_h^*\equiv0,\qquad c_h^*=\mathcal R_hE_h^*\equiv0\pmod p. \tag{2.1}
$$



Item 236 identifies the lower and upper residuals at the phase, so both
incomplete-binomial reductions have the common coefficient $c_h^*$.
Write their two collision equations as



$$
\begin{aligned}
\Theta&=c_h^*S+tL_h-2d_h=0,\\
\Xi&=c_h^*T+\eta_h tU_h-F_h+3d_h=0,              \tag{2.2}
\end{aligned}
$$



where $t=t_{s+1}$, $d_h=\Delta_-(h,s_*)$, and Item 231 proves



$$
\eta_h=\frac{t_J}{t_{s+1}}
=(-1)^{h+1}\frac{(3s_*+1)_{h+1}}{(s_*+2)_{h+1}}\pmod p.     \tag{2.3}
$$



Define



$$
K_h=2d_h\eta_hU_h-L_h(F_h-3d_h).                   \tag{2.4}
$$



In the polynomial ring on the displayed symbols,



$$
\eta_hU_h\Theta-L_h\Xi
=c_h^*(\eta_hU_hS-L_hT)-K_h.                       \tag{2.5}
$$



This identity is checked monomial by monomial in the certificate.  It
uses no division by $L_h,U_h,d_h$, or $t$.  Equations (2.1)--(2.2)
therefore imply $K_h\equiv0\pmod p$, proving (1.1).

Notice the precise scope.  Equation (2.5) proves $K_h=0$ on an original
collision after the gauge has killed the common residual.  It does not
prove $K_h\equiv0$ for every prime satisfying $E_h^*\equiv0$; that
stronger assertion is exactly the missing localized gcd theorem.

## 3. Denominator and unit audit

Item 222 gives



$$
E_h^*=\frac{A_h}{2(4h+3)D_xD_yD_uD_v},             \tag{3.1}
$$



and every factor in its denominator has absolute value at most
$4h+3<p$.  Item 243 proves that the numerator and denominator factors
of $\mathcal R_h$ are nonzero units on every actual row.

It remains to audit (2.4).  The lower and upper polynomials are generalized
binomial polynomials of degree $2h$, so their coefficient denominators
divide $(2h)!$.  The Gosper operator has leading action



$$
\mathcal L_s(j^d)=-2j^{d+1}+O(j^d),
$$



so its triangular inversion adds only powers of $2$.  Substitution of
$s_*$ and the two phase endpoints adds only powers of $2$ and $3$.
The remaining denominator factors in (2.3) are among



$$
6i-4h+9,\qquad 0\leq i\leq h.                       \tag{3.2}
$$



They are odd, hence nonzero, and their absolute values are less than
$4h+9\leq p$.  All factorial factors are smaller still.  Thus every
denominator in $L_h,d_h,U_h,F_h,\eta_h$, and therefore in $K_h$, is a
$p$-unit.  Reducing (1.1) is legitimate on every actual row, including
rows where an endpoint coefficient itself is zero.

## 4. The smallest arithmetic condition and its limitation

Because the two rational denominators are units, (1.1) is equivalent to



$$
p\mid N_E(h),\qquad p\mid N_K(h),                   \tag{4.1}
$$



which is exactly (1.2).  Passing to the gcd loses no information and is
the smallest one-integer divisibility statement obtained from these two
scalars.

There are two different possible future outcomes:

1. A localized divisibility theorem could show that every moving prime
   divisor of $N_E(h)$ already divides $N_K(h)$.  Then $K_h$ merely
   rephrases the old gate.
2. A collective gcd or resultant theorem could show that the common
   moving-prime divisors have small weighted mass.  Then $K_h$ supplies
   useful arithmetic codimension.

Neither statement follows from (1.3) or (2.5).  The exact replay through
$h\leq40$ finds that every prime in



$$
\frac{|N_E(h)|}{\gcd(|N_E(h)|,|N_K(h)|)}
$$



is at most $4h+3$, and that the reduced denominator of $K_h/c_h^*$
has no prime as large as the least possible actual row prime.  These are
**EXACT FINITE ONLY** observations and are not used to choose between the
two outcomes.

## 5. Divisor, height, and weighted-mass admission

For fixed $h$, every surviving collision prime divides the integer gcd
in (1.2).  Item 222's explicit clearing gives



$$
M_h=(h+3)2^{2h+4}(21h)^{h+2},\qquad
|A_h|\leq47hM_h^4.                                  \tag{5.1}
$$



When $A_h\ne0$, the reduced numerator $N_E(h)$ divides $A_h$, so



$$
\log\gcd(|N_E(h)|,|N_K(h)|)
\leq\log|A_h|=O(h\log h).                           \tag{5.2}
$$



Summing this individual estimate gives



$$
\sum_{h\leq H}O(h\log h)=O(H^2\log H),             \tag{5.3}
$$



which is far larger than the required $o(H)$ prime-log mass.  If some
$A_h$ vanishes as an integer, the individual $E$-height argument gives
no restriction at that $h$ and a separate theorem for $K_h$ is still
needed.  As in Item 222, the strip $h=o(H/\log H)$ has zero linear
weight, but the unbounded-$h$ range remains uncontrolled.

Thus the gauge supplies an exact two-scalar localization but no collective
radical estimate, no weighted-density theorem, and no positive capacity
admission.  The conditional $j=1$ cell remains



$$
\frac16\text{ per }m=\frac1{36}\text{ per }6m,
\qquad\text{new booked part }=0.                    \tag{5.4}
$$



## 6. Strict claim ledger

### PROVED

* The division-free identity (2.5).
* Every original actual $j=1$ collision satisfies (1.1)--(1.2).
* Every denominator used in that implication is an actual $p$-unit.
* The individual-height estimate (5.2) does not yield a sublinear summed
  bound.

### EXACT FINITE ONLY

* The replay of the lower/upper residual equality and the Item 243 gauge
  for the 27 admissible values $h\leq40$.
* The bounded gcd-quotient and $K_h/c_h^*$ denominator patterns described
  in Section 4.

### OPEN

* Whether $K_h$ is redundant after $E_h^*=0$ on every moving prime.
* Whether the pair has useful arithmetic codimension.
* A unit-localized all-$h$ gcd/resultant or collective radical theorem.
* A weighted prime-log-mass saving, Route 1, and every conclusion about
  $e+\pi$.

### BOOKING



$$
\boxed{\text{new linear log rate}=0,\quad
       \text{new divisibility exponent}=0,\quad
       \text{capacity booked}=0.}
$$



## 7. Reproducibility

The deterministic standard-library checker pins Items 222, 229, 231,
236, and 243; expands (2.5) exactly; audits the declared dependency hashes;
and produces byte-identical canonical and replay JSON files.  The bounded
replay is kept separate from the all-parameter proof.
