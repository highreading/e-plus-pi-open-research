> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the endpoint scalar Cauchy restriction

Date: 2026-09-13. Reviewer: audit_results.

Target: raw_endpoint_scalar_cauchy_restriction.md, Sections 1–6.
Dependencies checked against the exact original normalization in
raw_extremal_dual_polynomial_and_content_identity.md and the already
reviewed smooth-divisor and Cauchy-rank notes.

**Verdict: FULL PASS.** The cofactor transport preserves the actual
primitive vector and its sign; the polynomial and content identities
are global over the integers. The bordered determinant and its
Legendre evaluation have the stated signs. The saturated-family
reduction, exact prime-power endpoint valuation, normalized polynomial
reduction, and the infinite $m=4,p=17$ obstruction all follow.
No repair was needed. No degree or prime scan was performed.

## 1. Cofactor transport from the actual integer matrix

The signed cofactor convention is the same as in the original dual
note: row $k=n+t$ has position $t$, and its cofactor sign is
$(-1)^t$. For the unimodular row transformation $U$, the exterior
power identity gives $u'=U^{-T}u$, since $\det U=1$.

In the transformed matrix, cofactors from its first $n$ row positions
vanish by the deficient $B$-column rank. Its bottom position $n+r$
has cofactor


$$
(-1)^{n+r}\det V\,\det G[\widehat r].
$$


Dividing by the exact *weighted* global content formula gives


$$
w'_{n+r}=(-1)^{n+r}c_r\delta_r/h_n.
$$


The use of $h_n$, rather than the unweighted content $\Theta_n$,
is necessary and correct.

The entry of the difference row $r$ in original position $t=r+s$
is $(-1)^{n-s}\binom ns$. Thus the combined sign is


$$
(-1)^{n+r+n-(t-r)}=(-1)^t.
$$


This proves (5) exactly from $w=U^Tw'$. There is no unspecified
unit, projective rescaling or reversal of the primitive orientation.

Inserting (5) in the actual definition


$$
\widehat Q_n(z)=\sum_{t=0}^{2n}
\frac{(n+t)!}{n!}w_{n+t}z^{2n-t}
$$


and using $c_r=(2n)!/(n+r)!$ gives (6)–(7), including
$R_n=(2n)!/n!$. Every exponent is nonnegative.

## 2. Polynomial coefficient content

All coefficients of $\mathscr P_n$ are integer combinations of
the $\delta_r$. Conversely, its first $n+1$ coefficients in
descending degree have the displayed triangular coefficient matrix,
with diagonal $(-1)^t$. Every strict lower entry is an integer
because $(n+t)!/(n+r)!$ is integral for $r<t$.
This triangular matrix has an integer inverse.

Consequently its coefficient content is exactly $\Theta_n$, even
if some leading $\delta_r$ vanish. Taking positive rational contents
in $h_n\widehat Q_n=R_n\mathscr P_n$ yields


$$
c_n^Q=R_n\Theta_n/h_n.
$$


The known integrality of $\widehat Q_n$, together with
$\Theta_n\mid h_n$, then gives $h_n/\Theta_n\mid R_n$.
No unsupported equality of the two small-prime contents is used.

As a sign and scale check using the already established $n=1$
case, $L=6$, $\mathsf Z=(-6,-6)^T$,
$\Theta_1=h_1=6$, and $R_1=2$. Formula (6) gives
$\mathscr P_1=-6z^2+18z-18$, hence
$\widehat Q_1=-2z^2+6z-6$, $Z_1=-2$, $c_1^Q=2$
and $d_1^{II}=1$, exactly matching the original normalization.
This is a small normalization check, not an extrapolation.

## 3. The endpoint border and its denominator

Expansion along column $n$ of the $(n+1)$-square matrix
$[\mathsf Z\mid v]$, with zero-based indices, gives signs
$(-1)^{r+n}$. Hence $K_n=(-1)^n\det[\mathsf Z\mid v]$
as in (9).

Evaluation of the polynomial identity at one gives
$h_nZ_n=R_nK_n$.
The coefficient content $c_n^Q$ divides $Z_n$, because $Z_n$
is the sum of those integer coefficients. Therefore the least
coefficient denominator of $S_0=\widehat Q_n/Z_n$ is
$|Z_n|/c_n^Q=|K_n|/\Theta_n$, with no omitted gcd.
Nonvanishing is supplied by the previously proved actual endpoint
determinant, not by a new sign assertion for this border.

## 4. Congruence and exact Legendre determinant evaluation

The identity (10) is the integral identity already reviewed in the
Cauchy-rank note. It makes every positive-$s$ summand of
$\mathscr P_n$ divisible by $n$, giving the polynomial congruence
in (11), while $v_r\equiv1\pmod n$.

The first $n$ columns of the bordered determinant each acquire
the factor $(-1)^n$ under
$\mathsf Z\equiv(-1)^n\mathsf C\pmod n$.
Their product is $(-1)^{n^2}=(-1)^n$, cancelling the prefactor
in the formula for $K_n$. This proves (12).

Reversing the $n$ moment columns replaces $\tau_{n+r-j}$
by $\tau_{r+j+1}=\mathcal L(t^{r+j})$.
The reversed bordered determinant, after removing $L^n$, is the
transpose of the usual monic orthogonal-polynomial determinant
evaluated at one. Hence it equals
$(\prod_{j<n}h_j^{\rm Leg})Q_n(1)$.

The column reversal contributes $(-1)^{n(n-1)/2}$, while
$\prod_{j<n}h_j^{\rm Leg}$ has exactly that sign.
They cancel, proving (13) with the positive absolute norms. The
norm formula is the monic Legendre norm after $t=iu$:


$$
h_j^{\rm Leg}
=(-1)^j\frac{4^j(j!)^4}{((2j)!)^2(2j+1)}.
$$


The proof is over $\mathbb Q$; the determinant on the other side
is an integer. Thus it does not require a falsely uniform local
unimodularity statement for the Legendre basis.

The resulting congruence modulo $p^\nu\mid n$ fixes the valuation
only when the compared determinant has valuation below $\nu$.
The note explicitly retains this limitation.

## 5. Saturated-family left kernel and reciprocal polynomial

Let $n=mT$, $T=p^\nu$, $3m<p$. The previous rank theorem
proves $\delta_n$ is a unit, so both $\Theta_n$ and $h_n$
are units. Residue zero has the sole rectangular block of size
$(m+1)$-by-$m$; every other block is square and invertible.

The signed vector $((-1)^r\delta_r)_r$ is a left null vector
of $\mathsf Z$. Its entries therefore vanish modulo $p$
outside residue zero. The residue-zero block, apart from its
common nonzero scalar, has entries $\tau_{m+u-v}$.
Reversing its columns makes its left-null equations exactly


$$
\mathcal L(t^jQ(t))=0,\qquad 0\le j<m.
$$


The first $m$ rows form an invertible parity-Cauchy matrix,
so the monic solution is unique and equals $Q_m$.
All local divisions are valid because $p>3m$ exceeds every
moment denominator and nonzero Cauchy numerator factor needed here.

The coefficient at row $u=m$ is $(-1)^n\delta_n$.
This fixes the scale of the entire left null vector and proves
(16) with its displayed sign. Substituting into (11) gives


$$
\mathscr P_n(z)\equiv
(-1)^n\delta_n z^{2n}Q_m(z^{-T})\pmod p.
$$


The lowest exponent is $2n-mT=n$, with unit coefficient, so this
reciprocal expression is genuinely a polynomial.
Evaluation at one yields the asserted $K_n$ residue.

## 6. Exact valuations and normalized polynomial reduction

Since $m<p$ and $2m<p$, Legendre's factorial formula gives


$$
v_p(n!)=\frac{n-m}{p-1},\qquad
v_p((2n)!)=\frac{2(n-m)}{p-1}.
$$


Thus $v_p(R_n)=(n-m)/(p-1)$.
The units $\Theta_n,h_n$ in the exact global identities then give
all three statements in (18).

When $Q_m(1)$ is a unit, so is $K_n$. The exact rational identity
$S_0=\mathscr P_n/K_n$ makes coefficientwise reduction meaningful
and proves (19). In particular $m=1$, $Q_1(t)=t$, gives


$$
v_p(Z_{p^\nu})=\frac{p^\nu-1}{p-1},\qquad
S_0(z)\equiv z^{p^\nu}\pmod p.
$$


The simultaneous coefficient denominator is a $p$-unit.
Adding this valuation to the exact extremal-content valuation gives
(21) and (22), with the stated factor $2n+1$.

Finally,


$$
Q_4(1)=1+\frac67+\frac3{35}=\frac{68}{35}
$$


has positive $17$-valuation, while $17>3\cdot4$.
For every $n=4\cdot17^\nu$, the same actual left-kernel reduction
therefore makes $K_n$ divisible by $17$, with $\Theta_n$
still a unit. This proves the infinite-family lower bounds (23).
It does not determine the next valuation, and none is claimed.

The result concerns the actual normalized type-II cross product
$S_0=B_EC_F-C_EB_F$. It correctly avoids identifying its coefficient
denominator with the primitive rational denominator of the selected
type-I linear form. The remaining scalar and the limits above $3n$
remain explicit.
