> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the actual even inverse-corner limit

Date: 2026-09-13. Reviewer: audit_sources.
Status: PASS, including an identical interval postprocessing rerun.
No mathematical correction required.

Reviewed raw_even_endpoint_inverse_corner_limit.md and
check_raw_even_limit_from_odd_witnesses.py in full, using the previously independently certified odd vectors and their full half-line errors.

## 1. Actual even geometry and its normalization

For $p(z)=u(z^2)+zh(z^2)$, the two degrees are $m$ and $m-1$. The even weight kills the cross-parity norm terms, and multiplication by $z$ has matrix $\left(\begin{smallmatrix}0&t\\1&0\end{smallmatrix}\right)$. Thus its exponential, without a rational odd factor, is the actual symbol.

With the common Cayley denominator $(1-iy)^m$, the original scalar factor $|1+t|^{2m}$, this denominator, and the angular Jacobian together give exponent $2m+1$ in $(1+y^2)^{-(2m+1)}dy$. The smaller second degree becomes


$$
H(y)=(1-iy)P(y),\qquad\deg P\le m-1.
$$


Since $1-iy$ vanishes at $y=-i$, its image is precisely the degree-$m$ space with evaluation at $-i$ set to zero. It is not deletion of a monomial or of the top orthogonal coefficient.

The original endpoint $t=0$ is $y=i$; its scalar $2^{-m}$ disappears after normalizing its Riesz vector. The squared norm of the original endpoint functional is exactly $c_m$. Therefore the original inverse corner divided by $c_m$ is the inverse quadratic form of the unit first-channel vector in the constrained positive space. This proves the exact interface (4), with no missing weight or factorial scalar.

## 2. Recurrence limit and phases

For the changed exponent $2m+1$, every required fixed neighborhood of degree $m$ has finite moments once $m$ is sufficiently large. The earlier local functional-calculus argument therefore applies. Its proof only takes fixed moment orders before passing to the limit and does not assume an infinite polynomial basis for the Cauchy weight.

The endpoint Rodrigues ratio is unchanged in form. Its minimum over $j\le m$ is bounded below by $\sqrt2$, which supplies a uniform summable tail. Its fixed-distance-from-the-top limit is $\sqrt3$.

Conjugating the evaluations and then reversing indices gives $i^r$ at $+i$, after phase $i^m$, and $(-i)^r$ at $-i$, after phase $(-i)^m$. Thus the two limiting vectors in (6) have the stated phases and normalization $\sqrt{2/3}$. The independent phases leave both the endpoint quadratic form and the removed one-dimensional subspace unchanged.

## 3. Inverse convergence and positivity

The rank-one projections converge in operator norm because their unit vectors converge in norm. The full-space extensions of $E_m$ converge strongly with uniform norm and coercivity bounds. Consequently


$$
B_m=\Pi_mE_m\Pi_m+w_mw_m^*
$$


converges strongly to its stated limit. The added rank-one term is the identity on the excluded direction; the rest remains strictly accretive. Both these operators and their adjoints have a common positive coercivity bound. This proves surjectivity and uniformly bounded inverses, so the inverse identity gives strong inverse convergence.

The limit quadratic form has positive real part: if $x=B_+^{-1}v$, then its real part equals $\Re(x^*B_+x)>0$. Its reality follows independently from the real actual corners and convergence. Therefore $g_+>0$ does not depend on numerical evidence.

The inverse-compression identity has the correct minus sign and denominator $w^*E_+^{-1}w$. This denominator also has positive real part, so the formula is legitimate.

## 4. Reuse of the exact certified odd columns

The half-line resolvent calculation


$$
(I\pm iY)^{-1}e_0=\tfrac23(\mp i/\sqrt3)^r
$$


satisfies both the first row and every interior row. It gives


$$
A_{0,+}^{-1}U_+e_1=w/\sqrt2,\qquad
A_{0,+}^{-1}U_+e_2=v/\sqrt2.
$$


Thus the first two already certified odd solutions are exactly
$E_+^{-1}w/\sqrt2$ and $E_+^{-1}v/\sqrt2$. Substitution into the inverse-compression formula gives precisely (11), including the outer factor $\sqrt2$.

The postprocessor reads the unchanged exact dyadic vectors, whose input SHA256 was recorded in raw_odd_limiting_certificate_independent_review.md. The bounds $4\cdot10^{-13}$ and $3\cdot10^{-12}$ exceed their independently certified full-space errors. Pairing with the exact unit vectors $v,w$ adds at most these errors. Finite support of the approximants means no separate unbounded endpoint tail is omitted.

I reran the identical postprocessor with

    /opt/homebrew/bin/python3.12 work/session_20260913/check_raw_even_limit_from_odd_witnesses.py

It completed PASS without any new solve or quadrature. The certified real intervals are


$$
0.91149<g_+<0.91150,\qquad
0.783<\frac{\sqrt{3e}}{4g_+}<0.784.
$$


The denominator enclosure is bounded away from zero. All complex pairings, square roots, the exponential, and the final division are performed with outward interval arithmetic. The realness of the limit is proved analytically; it is not inferred from a small imaginary interval.

## 5. Endpoint and error constants

The exact inverse-corner identity gives


$$
V_n(1)/[t^n]V_n=B_m/g_m,\qquad
B_m=(4m)!m!(3m)!/((2m)!)^3.
$$


The scalar $c_m$ has been canceled correctly here. The remaining ratio is


$$
B_m\,\frac{n!}{(2n+1)!}
=\frac{m!(3m)!}{(2m)!^2(4m+1)}
\sim\frac{\sqrt3}{4n}\left(\frac{3\sqrt3}{4}\right)^n.
$$


Together with the already proved even flatness/error theorem and $g_m\to g_+>0$, this gives the claimed positive exact even error constant.

No effective convergence rate for the inverse corner is claimed. The signed arctangent term, primitive endpoint cancellation, and the rationality of $e+\pi$ remain outside this theorem.

