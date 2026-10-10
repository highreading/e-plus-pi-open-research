> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the factor accessories and boundary operator

Date: 2026-09-13. Reviewer: audit_sources.
Status: PASS. No mathematical correction required.

Reviewed raw_dual_factor_accessory_and_boundary_operator.md in full. The already reviewed Hardy factor theorem was used only for its exact norm identity, actual normalization, and explicit circular polynomial.

## 1. Reversal and accessories

The actual coefficients are real, so the conjugated full-degree reversal has the last coefficients written in (3). Full-degree reversal remains valid under degree loss. Equality of boundary moduli and the exact positive-measure norm replacement give the same Hardy bound for both ends.

The coefficient of $z^2$ in $F$ is $-m/2=-n/4$, directly from the explicit monic circular polynomial. I re-expanded the differential expression in (4). The top coefficient of $Cv'-C'v$ cancels, and its degree-$2n-2$ coefficient is $b_1v_n-v_{n-1}$. This gives exactly all three lines of (5), including the $-1$ and the additional $b_1$ in $K_0$. The bounds in (8) are conservative and imply the stated coefficientwise compactness. They give no nonzero limiting accessory.

## 2. Actual equation and the analytic compression

The right-hand side in (10) is exactly $c_m/v_0$, since the original Toeplitz equation pairs with the constant coefficient of the test polynomial. In the Hardy model this coefficient is evaluation at zero, represented by the constant function one. Dropping this scalar would change the actual equation; the note retains it.

The backward shift formula has numerator $p-p(0)F$, which vanishes at zero and has degree at most $n$. It therefore remains in the stated model space after division by $zF$. Orthogonal-complement shift invariance makes compression multiplicative for analytic powers. Norm convergence of the exponential series proves $T_\nu=\exp(S_b)$ and its inverse formula; neither statement assumes invariance under the forward shift. Applying the inverse to one gives $P_{S_n}e^{-z}$, as used in (13).

## 3. Finite-rank interface and all moment endpoints

The original measure and its replacement are invariant under $z\mapsto-z$. Because $n$ is even, their moments at both $n+1$ and $-n-1$ vanish. Thus these two additional moments really agree.

For $t\ge1$, a test polynomial divisible by $z^{t-1}$ makes every Laurent exponent of $e_t p\overline q$ lie between $-n$ and $n+1$. This verifies the one-sided interface and the rank $t-1$, rather than rank $t$. When the stated divisible subspace is empty, the note correctly retains only the trivial rank bound. Its orthogonal complement consists of the first coefficient-evaluation kernels because $F(0)=1$.

The two multiplication compressions each have norm bounded by the scalar supremum, in their exactly identified positive norms. The uniform factorial error bound therefore has no hidden $n$-dependent normalization. The singular-value consequence follows by using degree $t+1$ and rank at most $t$.

## 4. The first surviving correction

The original monic recurrence gives


$$
\Psi_{n+2}=z^2\Psi+(-1)^{m+1}\frac{m}{2m+1}F.
$$


Projection in the original measure therefore gives $+(-1)^m mF/(2m+1)$. In the replacement measure, $z^2\Psi\,\overline q\,d\nu$ is the boundary value of an analytic function with zero constant coefficient, so its projection is zero.

After subtracting $p_n\Psi$, the remaining polynomial has degree at most $n-1$; the extra moment agreement through $n+1$ kills its difference pairing. Consequently (16), including its sign and absence of any additional $H_m$ or $c_m$, is exact.

Finally


$$
\left\langle p/F,\Psi/F\right\rangle_{H^2}=p_n,\qquad
\|\Psi/F\|_{H^2}=1.
$$


Thus the coefficient functional has norm one and the correction norm is exactly $m/(2m+1)$. Its exponential contribution has the additional factor $1/2!$, correctly retained.

The first surviving Taylor term cannot be discarded. Its nonzero norm does not by itself lower-bound the norm of the full exponential correction, nor does local convergence of actual factors settle the moving boundary pairing. The source states these limitations correctly.

