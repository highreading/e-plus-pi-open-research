> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Full accessory Jacobian rank, unique possible lifts, and the exact two-residual depth

Date: 2026-09-13. Original bounded arithmetic continuation by audit_sources. Independent review passed: raw_accessory_transversality_independent_review.md.

This note proves an all-degree transversality statement for the actual four accessory equations. At every common zero in characteristic $p>3d+3$, their $4$-by-$2$ Jacobian has rank 2. There is at most one common zero even over an algebraic closure, and it lies in $\mathbb F_p$. At each prime-power depth there is at most one solution.

Full Jacobian rank does not imply that the four equations lift together. Choosing any invertible pair gives a unique lift solving those two equations. The other two have residual values $\rho_0,\rho_1\in\mathbb Z_p$, and the actual extremal depth is exactly



$$
v_p(F_{d+1})=\min\{v_p(\rho_0),v_p(\rho_1)\}.
$$



Thus the result gives a precise obstruction and unique-lift structure, not an upper bound for the depth. The completed local accessory algebra is $\mathbb Z_p/(p^f)$, with $f=v_p(F_{d+1})$.

## 1. Inputs and notation

Use the four integer polynomials



$$
\mathscr F=(E_0,E_1,R_0,R_1)
$$



from raw_extremal_four_accessory_equations.md, whose full field and prime-power equivalence was independently checked in raw_extremal_four_equations_independent_review.md. Put $n=d+1$, $M=3d+4$, $p>3d+3$, and $R=\mathbb Z_p$. The formulas below are for $d\ge2$; the already excluded $d=0,1$ fibers have no common zero at their allowed primes.

The exact inputs are:

1. A common accessory zero gives a unique degree-at-most-$d$ extremal triple with the leading coefficient of $B$ equal to 1.
2. Over every residue-field extension, the actual extremal kernel has dimension at most one, and the top $B$-coefficient is injective on it.
3. Reconstruction uses only the downward exponential pivots $-1,\ldots,-d$, a unit maximal minor of $U_d$, and the unit two-by-two initial determinant. Its finite-jet induction uses $k(k-1)(k-M)$, $2\le k\le M-1$.
4. The actual constant matrix $X_n$ has full column rank in characteristic zero and at most one nonunit Smith invariant over $R$. Its valuation is $f=v_p(F_n)$.

No additional normality, root-separation, or perfect-system assumption is introduced.

## 2. The two parameters are polynomial functions of the top B coefficients

Write the monic exponential polynomial as



$$
B(z)=z^d+b_1z^{d-1}+b_2z^{d-2}+\cdots .
$$



Here $b_1,b_2$ are names for the first two lower coefficients, not coefficient indices at the origin. The coefficients of $z^{d+1}$ and $z^d$ in $L^{[1]}B=0$ are exactly



$$
-b_1+\beta-3d^2+d=0,
$$




$$
-2b_2+(\beta-3d^2+d+2)b_1+\gamma-2d-2=0.
$$



Consequently



$$
\boxed{
\beta=3d^2-d+b_1,\qquad
\gamma=2d+2+2b_2-b_1^2-2b_1.}
\tag{1}
$$



For example, the second identity follows after substituting the first into the second coefficient equation. These identities hold over every ring in which the original equations hold. They introduce no new scalar division.

In particular, the normalized triple determines its accessory pair uniquely. This remains true over a ring with nilpotents.

## 3. Reconstruction over the dual numbers

Let $K$ be any field of characteristic $p>3d+3$, and let $\bar\theta=(\bar\beta,\bar\gamma)$ be a common zero. Consider $K[\varepsilon]/(\varepsilon^2)$.

The reconstruction from the reviewed four-equation proof works over this ring. To see the precise reason, use the maximal minor of $U_d$ and the initial two-by-two determinant that are nonzero at $\bar\theta$. Their values after a dual-number perturbation remain units. Choose the same pivot columns to solve for $A_0$ and the same initial normalization. The cofactor generator $C^*$ has a unit coordinate. All polynomial divisions by $D$ are monic, and all indicial and downward pivots remain units. Therefore a dual-number zero of $\mathscr F$ produces an actual normalized extremal triple over the dual numbers.

This is a functorial algebraic reconstruction in a fixed unit chart. It is stronger than applying an existence assertion over $\mathbb F_p$ to a ring without checking its inverses.

## 4. All-degree rank-two Jacobian theorem

**Theorem 1.** At every common zero $\bar\theta$ over any such field $K$,



$$
\operatorname{rank}_K
J_{\mathscr F}(\bar\theta)=2.
\tag{2}
$$



Equivalently at least one of its six two-by-two row minors is nonzero. At a root in $\mathbb F_p$, that minor is a unit in any integral lift.

**Proof.** Let $v=(u,v_2)\in K^2$ lie in the Jacobian kernel. The polynomial Taylor identity over the dual numbers gives



$$
\mathscr F(\bar\theta+\varepsilon v)=0.
$$



Section 3 reconstructs a normalized triple $T+\varepsilon\dot T$. The actual Taylor equations are linear, and their matrix $X_n$ has constant coefficients in $K$. Hence $\dot T$ belongs to the same extremal kernel over $K$. Its top $B$-coefficient is zero because the perturbed $B$ is still monic. Injectivity of that coefficient gives $\dot T=0$.

Formula (1) now forces $u=v_2=0$. Alternatively, subtracting the two exponential equations for the unchanged monic $B$ gives



$$
\bigl[(uz+v_2)(\partial+1)-du\bigr]B=0.
$$



Its coefficient of $z^{d+1}$ is $u$. Once $u=0$, its coefficient of $z^d$ is $v_2$. This proves injectivity of the Jacobian and hence (2). QED.

The proof covers a Jacobian pair involving residue equations as well as one involving exponential equations. It does not assert that the particular $2$-by-$2$ Jacobian of $E_0,E_1$ alone is always invertible.

## 5. Unique geometric point and reduced residue-field algebra

**Corollary 2.** For a fixed allowed prime $p$, either there is no common zero over $\overline{\mathbb F}_p$, or there is exactly one and it belongs to $\mathbb F_p^2$.

Indeed every common zero reconstructs a monic extremal triple. The original matrix has at most a one-dimensional kernel even over $\overline{\mathbb F}_p$. Normalization therefore gives at most one triple. Formula (1) gives at most one accessory pair. If it exists over the algebraic closure, the actual matrix already has rank loss over $\mathbb F_p$, and its monic kernel vector is defined over $\mathbb F_p$. Formula (1) then puts both parameters in $\mathbb F_p$.

There is also an ideal-theoretic version:



$$
\mathbb F_p[\beta,\gamma]/(\mathscr F)
\cong
\begin{cases}
0,& f=0,\\
\mathbb F_p,& f>0.
\end{cases}
\tag{3}
$$



For the nonempty case, the affine zero set over the algebraic closure is a single point, so the finitely generated quotient is zero-dimensional and its maximal ideal is nilpotent. Theorem 1 makes its cotangent space zero: the linear parts of the four equations span both coordinate directions. Nakayama's lemma forces the maximal ideal to be zero. Descent and Corollary 2 give (3). In the empty case the ideal is the unit ideal by the Nullstellensatz.

Thus no additional polynomial measuring a failure of rank 2 is needed at an actual zero: all six Jacobian minors cannot vanish there. Equivalently the four equations together with those six minors have no common geometric zero at any allowed prime. This assertion concerns the parameter directions, not the depth in the prime $p$.

## 6. Uniqueness at every congruence depth

**Corollary 3.** For each $h\ge1$, there is exactly one accessory solution modulo $p^h$ if $h\le f$, and none otherwise.

Existence or nonexistence is the reviewed full-depth theorem. To check uniqueness without presuming Hensel solvability, take the Smith form of the actual constant matrix $X_n$ over $R$. All but its final invariant factors are units. If $h\le f$, its kernel modulo $p^h$ is free of rank one, generated by the reduction of the final unimodular Smith column.

The top $B$-coefficient of that generator is a unit, since its residue-field reduction is a nonzero extremal triple. Requiring that coefficient to be 1 selects exactly one vector modulo $p^h$, and $A$ is then uniquely recovered from the low Taylor coefficients. Formula (1) selects exactly one parameter pair. If $h>f$, a vector in the remaining Smith coordinate must be divisible by $p$; it cannot give a monic top $B$-coefficient.

The solutions at the permitted depths are automatically compatible under reduction. This does not extend them past $h=f$.

## 7. Choose two equations and retain the other two as exact obstructions

Assume $f>0$, and let $\bar\theta$ be the unique common zero modulo $p$. Select two rows $I$ of $J_{\mathscr F}$ with unit determinant at $\bar\theta$. Denote those two polynomials by $G=(G_1,G_2)$, and the other two by $H=(H_1,H_2)$.

There is a unique $\theta_\infty\in R^2$ reducing to $\bar\theta$ for which $G(\theta_\infty)=0$. One can prove this directly, without assuming that the remaining equations lift: given a solution of $G$ modulo $p^h$, solve the two linear congruences



$$
J_G(\bar\theta)\delta
=-p^{-h}G(\theta_h)\pmod p.
$$



The unit determinant gives a unique correction $p^h\delta$. The quadratic Taylor terms are zero modulo $p^{h+1}$, since $2h\ge h+1$. These corrections give a coherent sequence and hence the asserted $p$-adic limit. Uniqueness follows at each step.

Define the two exact residuals



$$
\rho_1=H_1(\theta_\infty),\qquad
\rho_2=H_2(\theta_\infty).
$$



They are in $pR$. A solution of all four equations modulo $p^h$ must solve $G$ and therefore must be the reduction of $\theta_\infty$. Conversely that reduction solves all four precisely when $p^h$ divides both residuals. Thus



$$
\boxed{
f=\min\{v_p(\rho_1),v_p(\rho_2)\}.}
\tag{4}
$$



Here $v_p(0)=+\infty$; at least one residual is nonzero because the actual $X_n$ has full characteristic-zero column rank. The minimum is independent of the chosen invertible row pair, even though the two residuals themselves need not be.

For an explicit one-step test, suppose $\theta_h$ already solves all four modulo $p^h$. Put



$$
r=p^{-h}\mathscr F(\theta_h)\pmod p,
\qquad
\omega_h=r_H-J_H(\bar\theta)J_G(\bar\theta)^{-1}r_G.
\tag{5}
$$



Then a lift to depth $h+1$ exists if and only if $\omega_h=0$. When it exists, it is unique. Changing the chosen representative of $\theta_h$ adds a vector in the image of $J_{\mathscr F}$ to $r$, which leaves $\omega_h$ unchanged. Intrinsically the obstruction is the class of $r$ in the two-dimensional cokernel of the full Jacobian.

Equation (5) is a test, not an all-degree nonvanishing result. Nothing proved here ensures that $\omega_1$, or any fixed later $\omega_h$, is nonzero.

## 8. The completed local algebra

The exact local algebra can be identified using the same unit Jacobian pair. Center the variables at $\theta_\infty$, writing $u=\beta-\beta_\infty$, $v=\gamma-\gamma_\infty$. In $R[[u,v]]$, $G_1,G_2$ have zero constant term and an invertible linear coefficient matrix. Successive comparison of homogeneous degrees gives an invertible formal change of coordinates from $(u,v)$ to $(G_1,G_2)$; it divides only by that unit matrix.

Consequently



$$
\begin{aligned}
\widehat{\mathcal A}_{\bar\theta}
&:=R[[u,v]]/(E_0,E_1,R_0,R_1)\\
&\cong R/(\rho_1,\rho_2)
\cong R/(p^f).
\end{aligned}
\tag{6}
$$



This is the completed local quotient at the unique residue point. The proof derives the isomorphism from actual formal coordinates, not merely from a count of congruence solutions. A separate finite-algebra result for the exponential pair can promote it to a global finite $R$-algebra statement; that result is being established independently.

The simple model



$$
(u,v,p^a)\subset R[u,v]
$$



has full parameter Jacobian rank at its residue point but completed quotient $R/(p^a)$, for any $a\ge1$. It illustrates the distinction relevant here: parameter transversality is compatible with arbitrarily large prime-power thickness. Therefore neither (2) nor (6) alone bounds $f$.

## 9. Consequences and next arithmetic target

The actual accessory point, if present, is rigid: there are no extra geometric branches, no nilpotent parameter direction modulo $p$, and no ambiguity among possible congruence lifts. The only unresolved information is how many successive obstruction vectors (5) vanish, equivalently the valuation of the two residuals in (4).

This gives a well-defined local target for an actual recurrence, dual-pairing, or resultant calculation. It also permits unit pivot selection using the full four-row Jacobian without requiring the exponential pair itself to be nonsingular. The independently developed finite-free exponential algebra and norm carrier must retain that distinction.

No bound for the primitive endpoint denominator, no shrinking integer form, and no proof about the rationality of $e+\pi$ follows from this transversality theorem alone.
