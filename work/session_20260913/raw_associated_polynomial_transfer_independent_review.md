> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of associated polynomial and boundary-transfer bounds

Date: 2026-09-13. Reviewer: audit_results.

Target: raw_associated_polynomial_and_boundary_transfer_bounds.md,
Sections 1–7. The imported density estimates were checked against the
reviewed raw_associated_measure_uniform_energy_bounds.md, and the
matrix/measure normalization against the previously audited exact
Legendre-square identification.

**Verdict: FULL PASS.** All constants, index ranges, endpoint factors
and initial-data terms check. No correction was needed and no new
degree or numerical scan was performed. The conclusions remain in
their stated norms and positive-parameter range; they do not establish
the mixed zero bound or the separate high spectral row-rank problem.

## 1. Actual coefficient perturbations

The identity


$$
\alpha_j^2=\frac14\left(1+\frac1{4j^2-1}\right)
$$


gives the diagonal bound directly. For the two factors of $c_t$,
$\sqrt{(1+x)(1+y)}\le1+(x+y)/2$ follows by squaring and using
$(x-y)^2\ge0$. This gives exactly the two constants in (1).

For the full row-sum estimate, a lower off-diagonal in an interior
row has index $t-1$, but this index is still at least $a$.
Thus every present diagonal is bounded by $1/(30a^2)$ and each
off-diagonal by $1/(60a^2)$. Their sum is $1/(15a^2)$.
This verifies (2) without misapplying the pointwise $t$-bound to
a lower neighbor.

## 2. Absolute density and polynomial Gram estimates

On $1-y\ge k^{-2}$, the imported logarithmic bound is at most
$1/2$, since $m\ge1$. Multiplication by $w_{\rm free}$ gives


$$
|w_a-w_{\rm free}|
\le e^{1/2}\left(\frac1{\pi m^2}+\frac2{\pi k}\right).
$$


Here $w_{\rm free}\le4/\pi$ and
$w_{\rm free}\sqrt{y/(1-y)}=(8/\pi)y$.
Since $k/m^2\le5/2$, the displayed bound is below $3/k$.

Inside the complementary edge layer, the imported uniform estimate
is $w_a\le64/(\pi^2k)$, while $w_{\rm free}\le8/(\pi k)$.
Both densities are nonnegative, so their absolute difference is
bounded by the larger upper bound, which is below $8/k$.
This proves (3) pointwise throughout the open interval.

The change $x=2y-1$ sends the free probability measure to
$(2/\pi)\sqrt{1-x^2}\,dx$, so the $U_j(2y-1)$ really are
orthonormal with the stated normalization. Cauchy–Schwarz and
$|U_j|\le j+1$ give
$\|q\|_\infty^2\le h^3\|q\|_{\rm free}^2$, also for complex
coefficients.

At $\epsilon=1/(4h^2)$, the minimum free density on the retained
interval is at least $2\sqrt3/(\pi h)>1/h$. The retained integral
cost is therefore at most $h$; the two omitted intervals have total
length $1/(2h^2)$, giving cost at most $h/2$. This proves (4).
Combining with (3) yields exactly $12(d+1)/k$ in (5).

For $d\le r-1$, products of the tested polynomials have degree
at most $2r-2$, within the quadrature exactness range $2r-1$.
Thus the same quadratic forms give the finite Gram estimate (6).
The leading coefficient in each new Krylov column reaches coordinate
$j+1$ by a nonzero product of the tridiagonal couplings, while
bandwidth excludes later coordinates. This proves (7), and the same
bandwidth argument proves the exact blindness statement (8).

## 3. Recurrence error and the endpoint polynomial

Writing $t=a+j$, the exact perturbation coefficients are


$$
A_j(y)=(y-\tfrac12)(c_t^{-1}-4)
       -(d_t-\tfrac12)c_t^{-1},\qquad
B_j=1-c_{t-1}/c_t.
$$


Since $c_t\ge1/4$, the two terms of $A_j$ are each at most
$2/(15t^2)$ in absolute value.
The explicit $\alpha$ formula shows $c_t$ decreases with $t$.
Therefore


$$
|B_j|\le4(c_{t-1}-\tfrac14)
\le\frac1{15(t-1)^2}
\le\frac4{15t^2},
$$


using $t\ge2$. The absent $j=0$ previous-polynomial term is
zero regardless of the chosen value of that coefficient.

The free recurrence has initial polynomials $p_{-1}=0,p_0=1$
and Green sequence $U_{j-h-1}$, proving (11) with its displayed
index. After dividing by $j+1$, its summand is bounded by


$$
\frac8{15}\frac{h+1}{(a+h)^2}M_h.
$$


The same upper bound applies to the maximum defining $M_j$,
because all majorant summands are nonnegative. The discrete
Gronwall product and
$\sum_{h<j}(h+1)/(a+h)^2\le j(j+1)/(2a^2)$
give exactly the exponent $4j(j+1)/(15a^2)$ in (12).

For the reversed finite matrix, every required coupling and diagonal
still has original index at least $a$. Differences of consecutive
couplings are bounded by their common interval width. Hence the
same coefficient-error bound holds with denominator $a^2$.
Repeating the majorant argument gives the same exponent through
degree $r-1$. It does not require or assert an infinite tail
interpretation for the reversed finite matrix.

## 4. All-mode quadrature weights

The tridiagonal eigenvector recurrence gives
$v_i(j+1)=p_j(\theta_i)v_i(1)$. Endpoint nonvanishing and unit
Euclidean norm therefore give (13).

For $j\le r-1$, squaring (12) and summing yields


$$
\sum_{j=0}^{r-1}p_j(\theta_i)^2
\le r^3\exp\!\left(\frac{8r(r-1)}{15a^2}\right).
$$


The reverse recurrence proves the identical estimate for the other
endpoint. Taking the geometric mean of the two squared-weight lower
bounds gives (15), without an extra square or square root in its
constant. These inequalities include $r=1$.
They retain, rather than alter, the alternating cross-weight signs
when $r\ge2$.

## 5. Positive-parameter absolute and relative transfer bounds

For $\tau\ge0$, both positive contractions have resolvent norm at
most one, proving (16) by the resolvent identity.
The corner cofactor is exactly


$$
\frac{(-\tau)^{r-1}\prod_{t=a}^{b-1}c_t}
     {\det(I+\tau J_+)}.
$$


For $\tau>0$, its sign is nonzero and agrees with the free corner.

Weyl's inequality bounds each paired eigenvalue difference by
$1/(15a^2)$. The derivative of $\log(1+\tau x)$ on $[0,1]$
is at most $\tau$, yielding the claimed $r\tau/(15a^2)$
determinant bound. Separately,
$\log(4c_t)\le4(c_t-1/4)\le1/(15t^2)$.
Adding the two bounds gives (18), including its constant.
This argument controls a signed nonzero ratio directly; it never
divides the absolute norm error by a small corner entry.

The scalar tridiagonal determinant recurrence gives


$$
\det(I+\tau J_0)=(\tau/4)^rU_r(1+2/\tau).
$$


The endpoint and diagonal cofactors then give all of (19), with
the factor $4/\tau$ and the sign $(-1)^{r-1}$.
The hyperbolic expression for $U_r$ has positive argument for
$\tau>0$. The note correctly treats $\tau=0,r\ge2$ only as
a limiting ratio, because both corner entries vanish there.

## 6. Physical factors and initial-data cancellation

Direct multiplication of $DM^{-1/2}B$ gives


$$
\beta_L=\gamma_a/\sqrt{\delta_a},\qquad
\beta_R=(-1)^{r-1}\sqrt{\rho_b/\delta_b}.
$$


For $r\ge2$, the columns are orthogonal coordinate vectors.
The bounds $\gamma_a\le28/27$, $\delta_a\ge35/9$ and
$\rho_b\le1$ show that each squared column norm is below one.
Thus (22) follows with the stated unchanged constant.

The factors $\beta_i^2$ cancel exactly in each relative diagonal
ratio. Since $R_0\succeq(1+\tau)^{-1}I$, this yields (23).
For the physical cross entry, the gauge sign in $\beta_R$
cancels the corner-cofactor sign, giving the positive expression
(24). It does not make the separate spectral residues positive.

For the Laplace transform, the exact transformed equation is


$$
(M+s^2H)\widehat E-sH\mathbf1
=s^2B\widehat\beta-sB(1,1)^T.
$$


All first derivatives at zero vanish by parity. The row sums of
$H$ equal the two boundary coefficients, so
$H\mathbf1=B(1,1)^T$, including the additive boundary case
when $r=1$. The remaining initial terms cancel exactly.
Since the original functions are polynomials, their transforms
converge for every real $s>0$. This proves both identities (25)
without an independent-forcing assumption.

## 7. Scope

The growing Gram estimate, comparable-degree endpoint polynomial
bound, polynomial lower bounds for all endpoint weights, and relative
positive-axis corner estimate are valid in the stated regimes.
They do not supply uniform bounds near the negative poles.
Nor does a positive-axis Laplace comparison by itself control zeros
of the constrained signed inverse transform.
The target correctly retains the actual forcing, coefficient
constraints, alternating residues, and the distinction from the
separate high spectral evaluation problem.
