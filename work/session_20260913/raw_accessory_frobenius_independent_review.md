> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the accessory Frobenius and trace certificate

Date: 2026-09-13. Reviewer: audit_results.

Reviewed in full: raw_accessory_frobenius_pairing_and_reducedness_certificate.md.
The all-degree proof and the single predeclared degree-two diagnostic **pass**.
No mathematical correction is required. This review establishes neither
all-degree reducedness nor a bound on the actual large-prime content.

The crucial distinction is maintained: the coefficient functional defines an
always-perfect **Frobenius pairing**, whereas the ordinary **trace pairing** is
perfect exactly when the characteristic-zero algebra is reduced. The theorem
gives an explicit normalized multiplier relating them; it does not prove that
the multiplier is invertible in every degree.

## 1. Dependencies and filtered normal forms

I re-read the leading-term and filtered-division proof in
raw_accessory_finite_algebra_and_norm_carrier.md. The base ring is exactly
$R=\mathbb Z[1/d!]$, $d\ge2$. The actual equations retain the order and
normalization


$$
E_1=d![z]L^{[1]}B^*,\qquad E_0=d![1]L^{[1]}B^*.
$$


Their leading forms are $P_{d+1}$ and $\gamma P_d$, with weights one and
two on beta and gamma. The monic leading generators


$$
G_j=\gamma^jP_{d+1-j},\qquad
 \gamma G_j-\beta G_{j+1}=(d-j)G_{j+2}
$$


use only the units $1,\ldots,d$. Their standard monomials are precisely
$\beta^a\gamma^b$, $a+b\le d$.

The highest-weight syzygy argument excludes hidden lower-weight relations.
Thus the actual quotient is free on these monomials, and reduction never
increases weight. No reducedness is used. The coefficient of $\gamma^d$
vanishes on weight below $2d$; at weight exactly $2d$, lower terms of the
actual equations cannot contribute to that coefficient.

## 2. Signed Gaussian moments and the fixed determinant

The formal identity


$$
M\!\left(e^{tX+t^2/2}e^{uX}\right)=e^{-tu-u^2/2}
$$


gives both asserted formulas


$$
M(P_r(X,1)e^{uX})=(-u)^r e^{-u^2/2},\qquad
 M(P_rP_s)=\delta_{rs}(-1)^r r!.
$$


These are coefficient identities with integer moments. They neither assume
a positive measure nor introduce further denominators into the resulting
polynomial formulas.

For $G_j$, put $r=d+1-j$. Its weight is $2d+2-r$. A multiplier bringing
it to weight $2d$ has weight $r-2$, hence beta degree at most $r-2<r$;
the moment functional annihilates it. Cases $r=0,1$ have no such multiplier.
The only standard monomial of weight $2d$ is $\gamma^d$, on which the
functional is one. This proves the exact top moments in equation (5).

The block-triangular determinant is valid despite the differing sizes of
the weight groups. A monomial of weight $w$ has beta exponent in


$$
A_w=\{a:0\le a\le\min(w,2d-w),\ a\equiv w\pmod2\}.
$$


The complementary group $2d-w$ has the same set. Increasing row weights
and decreasing column weights put zero blocks on one side of the
complementary blocks. Each diagonal block is $M(X^{a+a'})$.
The monic same-parity polynomials $P_a$, $a\in A_w$, make a unit
triangular change within that block, whose determinant is therefore
$\prod_{a\in A_w}(-1)^aa!$.

A fixed exponent $a$ occurs for exactly the $d-a+1$ weights
$a,a+2,\ldots,2d-a$. Multiplying gives


$$
\det G=\pm\prod_{a=0}^d(a!)^{d-a+1}.
$$


All actual lower terms occur off these diagonal blocks. This proves
perfectness over the stated ring, not merely over its fraction field.
Commutativity gives $M_a^TG=GM_a$ with the column convention. The nonzero
vector one is isotropic, so the nondegenerate real form is indefinite.

## 3. The diagonal annihilator over the ring

The stated divided-difference matrix, multiplied by the column
$(\beta-\eta,\gamma-\zeta)^T$, gives the differences of the ordered pair
$(E_1,E_0)$ between the two variable pairs. The order and signs are
correct. In the tensor quotient, its adjugate therefore shows that both
coordinate differences annihilate its determinant $\mathfrak B$.

The perfect pairing identifies $\mathscr A\otimes_R\mathscr A$ with
$\operatorname{End}_R(\mathscr A)$ by
$u\otimes v:x\mapsto u\lambda(vx)$. Under this identification,
annihilation by $\beta\otimes1-1\otimes\beta$ is exactly commutation with
$M_\beta$, and similarly for gamma. Commutation with the algebra
generators implies algebra-linearity, and an algebra-linear endomorphism
of the rank-one module $\mathscr A$ is multiplication by its value at one.
No field, point decomposition, separability, or reducedness is needed.
Consequently


$$
\mathfrak B=(k\otimes1)\mathfrak C,\qquad
 \mathfrak C=\sum_i b_i\otimes b_i^\vee,\qquad
 k=(\operatorname{id}\otimes\lambda)\mathfrak B.
$$



The total weight of $\mathfrak B$ is at most $2d$: the two column
divisions lower weights by one and two. Reductions in either tensor factor
preserve this bound. A term with positive first-factor weight has
second-factor weight below $2d$, so lambda kills it. Hence $k$ is a
scalar determined by the leading equations even though the actual algebra
is not graded.

Setting the first variables to zero in the leading determinant gives
$\eta^dP_d(\eta,\zeta)$, with a positive sign. Its functional value is


$$
M(X^dP_d(X,1))=(-1)^dd!,
$$


since $P_d$ is monic and its lower terms are orthogonal to $P_d$.
This independently fixes $k=(-1)^dd!$; no residue constant remains.

## 4. Euler, the bordered determinant, and the trace radical

Multiplication of the tensor factors sends $\mathfrak B$ to the
Jacobian of $(E_1,E_0)$ with respect to $(\beta,\gamma)$, and the
Casimir to $\mathfrak e=\sum b_ib_i^\vee$. Therefore


$$
J_E=(-1)^dd!\,\mathfrak e.
$$


The previously independently reviewed bordered identity has the same
order and normalization:
$J_E=(-1)^dd!\det W_d$. Dividing by this unit gives
$\mathfrak e=\det W_d$ in the actual quotient.

Summing the diagonal coefficients of $M_a$ gives the trace formula.
The stated matrix orientation also checks:


$$
\operatorname{Tr}(M_a)=\lambda(a\mathfrak e),\qquad H=GM_{\mathfrak e}.
$$


Thus the fixed Frobenius determinant multiplies the ordinary norm of
$\det W_d$ to give the trace determinant. This does not make the latter
norm nonzero.

Over an algebraic closure of characteristic zero, a local Artin factor of
length $m$ has multiplication trace equal to $m$ times the residue
value. Its trace radical is exactly its maximal ideal; $m\ne0$ is
essential. Descent to $\mathbb Q$ and invertibility of $G$ prove


$$
\operatorname{Nil}(\mathscr A_{\mathbb Q})
 =\ker M_{\det W_d}.
$$


The rank counts geometric points; invertibility is equivalent to
reducedness. The note correctly avoids this assertion in arbitrary
positive characteristic.

In the homogeneous comparison algebra the Euler element is homogeneous
of weight $2d$, hence a scalar multiple of $\gamma^d$. Its trace
normalization makes it $D_d\gamma^d$, which is nonzero but square-zero.
This is a valid warning against using its nonzero scalar trace to infer
invertibility.

## 5. Independent exact degree-two control

I inspected the source checker, then made a separate exact control in
accessory_frobenius_independent_degree2_checks.py/.json. It uses the four
explicit filtered monic lifts and direct weighted polynomial division,
instead of the source's Groebner reducer. All six S-pairs in this one
degree reduce to zero.

The independent calculation verifies:

- the full displayed Gram matrix and determinant two;
- the Euler normal form and $J_E=2\mathfrak e$ in the quotient;
- the actual two-copy identity $\mathfrak B=2\mathfrak C$, together with
  both diagonal-annihilator identities;
- both coordinate self-adjoint identities and $H=GM_{\mathfrak e}$;
- the trace determinant $2^{15}\cdot751\cdot318737$;
- the eliminant, the linear formula for gamma, the beta multiplication
  characteristic polynomial, and squarefreeness;
- every displayed Sturm member, including its positive rational ratio
  to the ordinary signed-remainder sequence.

The Sturm variations are four at negative infinity and two at positive
infinity. The algebra has exactly two real and four nonreal joint points
in this degree. A positive-definite real form making $M_\beta$
self-adjoint is impossible. This diagnoses that proposed positivity
shortcut, while establishing reducedness only at $d=2$.

## 6. Scope retained

The all-degree perfect Frobenius pairing, fixed small-prime determinant,
exact Euler/bordered identity, and characteristic-zero nilradical kernel
all pass. The conditional use of the trace discriminant in a
normalization-index estimate remains contingent on generic reducedness.
No all-degree reducedness, actual four-equation prime exclusion,
extremal-depth bound, or conclusion about $e+\pi$ follows from this
theorem or this audit.
