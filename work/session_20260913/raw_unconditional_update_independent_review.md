> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent full audit of the unconditional finite-state update

Date: 2026-09-13. Reviewed by audit_results.

Reviewed in full:

- raw_hp_unconditional_finite_state_update.md;
- raw_hp_exceptional_logpole_jets.md;
- raw_hp_all_degree_infinity_jets.md;
- the previously reviewed origin, scalar-ODE, rank, and mixed-Wronskian transfer dependencies.

**Verdict:** the unconditional construction passes. It selects the actual next normalized triple using a bounded rational state and bounded-size systems, including every accessory configuration. It does not provide a quantitative bound on that state. One terminology correction was requested and has been incorporated: the three columns attached to 1,e,pi are formal rational coefficient columns; they are not asserted to form a linearly independent basis of numbers.

## 1. Multiple ordinary accessory points

For h=ord_a Q at a away from0,±i, the actual analytic echelon orders satisfy r0+r1+r2=h+3. Since they are distinct nonnegative integers, r2<=h+2<=5. The cofactor valuation proof gives a regular-singular scalar equation even at repeated roots.

The Euler recurrence on Taylor coefficients is triangular. Away from an indicial root the next coefficient is determined. At each of the three distinct roots it introduces at most one free parameter; compatibility can only reduce the dimension. Therefore the six-coefficient kernel has dimension at most3. The actual three analytic solutions have independent six-jets because their echelon orders are at most5, so the dimension is exactly3 and their jets span that kernel.

Every later coefficient has nonzero diagonal multiplier. This proves both reconstruction and the absence of spurious finite-jet directions. No formal convergence assumption is required: every kernel vector is the jet of a linear combination of known actual germs.

A numerator with derivatives through order2 needs old Taylor coefficients only through h+1 to determine its coefficients below h. Thus the stated local pole test is exact for all multiplicities1,2,3.

## 2. Exceptional origin and the low-space test

The origin requires two separate conditions, and both are present in the final construction.

First, the recurrence through degree4 reconstructs the entire possible low jet image. If M>4, the high solution has zero truncation and the low two germs inject through degree4. There are at most two free indicial indices in that range, so the kernel has dimension exactly2. If M=4, all three actual germs inject and the kernel has dimension3. The latter case can only occur at n=1 but is correctly included.

No compatibility condition through degree4 can shrink these actual jet images, and no additional spurious direction can arise from the triangular recurrence. Later resonance at M does not change the coefficients needed for a pole test: h+1<=4. Thus requiring zero numerator coefficients below h on the low kernel removes precisely every possible origin principal part of the analytic columns.

Second, the normalized high solution has a uniquely determined relative series. The independent origin review already verified that u0,...,u7 suffice for the required high numerator order 3n+4+h. Its unknown nonzero leading constant is immaterial to a homogeneous vanishing test.

High order alone would not remove the low-column poles, but the final note does not make that error.

## 3. Logarithmic collisions: exponents, dimension, and reconstruction

The echelon reduction of the analytic part H is valid: after cancelling a leading term of order l0, its order rises above l0; a subsequent cancellation at l1 rises above l1. Thus at most two constant column operations produce an order d distinct from both analytic-plane orders.

The analytic Wronskian leading order is d+l0+l1-3. For the logarithmic contribution, differentiating the ordinary exponent Vandermonde at the repeated exponent c gives a nonzero confluent coefficient, and the leading order is c+l0+l1-3. Because d differs from c, these terms cannot cancel. Hence the exact identity



$$
\min(c,d)+l_0+l_1=h+1
$$



is sound, including H identically zero. The same column subtraction in every cofactor proves the regular-singular pole bounds. If d<c, the three indicial roots are distinct; if c<d, applying the indicial operator to x^c log x forces I'(c)=0 and gives the claimed double root.

The finite Taylor/log system has the correct local diagonal block. At index k its two equations are



$$
I(k)b_k+\text{earlier terms}=0,
$$




$$
I(k)a_k+I'(k)b_k+\text{earlier terms}=0.
$$



When I(k) is nonzero, both coefficients are fixed. A simple root contributes at most one free coefficient, while a double root contributes at most two. Since the roots, counted with multiplicity, total three and all lie between0 and4, the finite kernel has dimension at most3. The actual three solutions inject into these ten coefficients: a nonzero log coefficient has order c<=4, and the analytic plane has echelon orders at most4. Thus the dimension is exactly3.

This dimension argument alone already identifies every finite kernel vector with an actual local solution jet. The source note additionally proves formal convergence by a majorant argument; that argument is consistent, but convergence is not a hidden additional premise of the root synthesis.

For the rational raw cubic, h at either ±i is in fact at most1 because D is irreducible over Q and has degree2. The two actual-possible exceptional indicial types are {0,0,2} and {0,1,1}. The root's degree4 construction is deliberately larger and remains valid.

## 4. Principal parts and global polynomiality

For y=a+b log x, direct differentiation gives



$$
g_b=N_0b+N_1b'+N_2b'',
$$




$$
g_a=N_0a+N_1a'+N_2a''
       +N_1b/x+N_2(2b'/x-b/x^2).
$$



Writing Q=x^h q with q a unit, the forbidden terms are exactly the negative powers of g_a/(x^h q) and g_b/(x^h q). Their lowest possible degree is -h-2, and their highest needed input coefficient has degree h+1. The ordinary unit division may mix lower principal coefficients but requires only a bounded Taylor prefix.

Applying this condition to the entire finite kernel removes every forbidden pole, not merely those of a chosen solution. On the analytic columns no logarithm is introduced. On R, the logarithmic coefficient after applying S is exactly the old residue times SC. Therefore subtracting Chat*atan removes that logarithm and leaves an analytic rational part.

The rational expressions Ahat,Bhat,Chat have no possible finite poles outside Q-roots and±i. The ordinary, origin, and logarithmic conditions cover all of them. Rational functions without finite poles are polynomials. There is no missing collision between the categories: 0 and±i are treated separately, and 1 belongs to the ordinary accessory category.

## 5. All infinity degree types

I independently checked the transformed operator indices, including their left-to-right ordering. For y=z^n F(1/z),



$$
\partial_z^j y=z^{n-j}(n-\theta)_{\underline j}F.
$$



Thus the exponent q+1+j-k in the Laurent equation is correct. Every exponent is nonnegative by the established coefficient degree bounds. The constant Euler polynomial is the displayed quadratic with roots n-c,n-d. The two roots are distinct and at most4, so the five-coefficient kernel is exactly the actual Laurent plane by the same upper-dimension and actual-injection argument.

After the exponential gauge, the constant Euler polynomial is qlead*(n-b-s). Its single root lies between0 and3, giving the one-dimensional exponential kernel. The cancellation in the degree of tilde A0 follows from the two leading coefficients A3 and A2; the next coefficient is fixed by the actual polynomial solution of degree b.

For a numerator of maximum degree n+6, the forbidden powers are strictly above n+q+1. The smallest forbidden power is n+q+2. An input coefficient at relative index r can contribute only when r<=4-q, hence certainly only among the first five coefficients. Division by Q changes no part of this criterion: a numerator has growth at most n+q+1 exactly when its quotient has growth at most n+1.

These conditions bound the full Laurent plane, not only C. Consequently they bound Ahat too after subtracting Chat*(atan-F_infinity), whose degree at infinity is one lower.

## 6. Rational descent, endpoint closure, and uniqueness

At an algebraic accessory root, all coefficient equations lie in its finite algebraic coefficient field and are invariant under conjugation. One may avoid any unbounded integer-factorization issue by using squarefree multiplicity strata, computed with fixed-degree polynomial gcds, and finite quotient algebras. Nonunit pivots can be split by another polynomial gcd. All algebra dimensions and possible splits are bounded by deg Q<=3. Equating rational coordinates gives a bounded rational linear system.

At z=1, the three actual analytic echelon orders sum to3+ord_1 Q<=6, and the maximum is at most5. The six carried jets therefore determine every later jet. If h=ord_1 Q, computing a transferred derivative of order at most5 requires numerator coefficients through h+5, hence old solution derivatives through h+7<=10. The stated five additional recurrence steps suffice. The stored u-jet list divides by the constant endpoint value e, so it obeys the original local differential equation, as required.

The endpoint quotient formulas are linear in the unknown N coefficients because all old jets are given. Pole removal guarantees the quotient limits exist before those normalization equations are evaluated.

Global polynomiality, the degree conditions, the high origin order, and the two endpoint values put the output exactly in the already proved canonical next-degree class. Existence is supplied by the genuine mixed-Wronskian transfer. If two N vectors satisfied the system, their difference would annihilate the three independent old solutions with an operator of order at most2, hence would vanish identically. Therefore the system has rank21 and a unique rational solution.

Differentiation and the companion identity then update the full transfer and the scalar coefficients. The Wronskian identity fixes Q_next's scale. The actual all-degree degree bounds apply to the result, so temporary uncancelled rational expressions do not enlarge the retained state.

The uniformity claim concerns the number of coefficients, equations, and rational operations. It contains no uniform lower bound on a pivot, root separation, bit length, or matrix condition number. Those missing quantitative controls remain essential.

## 7. Synthetic independent collision controls

The new checker check_raw_unconditional_local_independent.py verifies eight predeclared local examples. It derives each scalar equation directly from the chosen germs, then constructs its finite Euler kernel.

The cases are:

- ordinary double and triple accessory roots, with echelon orders(0,1,4) and(0,1,5);
- origin orders(1,3,4) and(1,3,10), checking respectively a three-dimensional and a two-dimensional degree4 kernel;
- both rational-raw-compatible exceptional log types, with indicial multisets{0,0,2} and{0,1,1};
- two deliberately more general synthetic log cases, including distinct indicial roots{0,1,2} with a later resonant logarithm, and{0,0,4}.

Every kernel equals the span of the actual synthetic germ jets. Every principal-part cutoff through h+1 is checked by subtracting the truncated germs and proving that the operator remainder has nonnegative valuation for every derivative order0,1,2; multiplication by a polynomial N cannot lower it.

All eight checks pass in raw_unconditional_local_independent_checks.json. These are local identity controls, not claims that those exceptions occur in the canonical raw orbit.

## 8. A new exact bridge toward the missing factorial norm estimate

The next task should use the finite transfer quantitatively rather than re-prove its existence. The following exact transform places its exponential branch directly in the norm problem already isolated by the project.

Use the reversed variable t=1-x and define



$$
P_n(t)=\sum_{k=0}^n B_{n,k}\frac{t^{n-k}}{(n-k)!},
\quad (Jf)(t)=\int_0^t f(s)\,ds,\quad \theta=t\partial_t.
$$



This is the same actual polynomial as the earlier P_B after reflection of [0,1], so its L1 and L2 norms are unchanged. Let



$$
\widetilde N_j=\sum_{k=j}^2\binom{k}{j}N_k,\qquad
Q(z)=\sum_{d=0}^q Q_d z^d.
$$



The actual exponential transfer is



$$
Q B_{n+1}=\sum_{j=0}^2\widetilde N_j B_n^{(j)}.
$$



Applying the reversal/factorial transform with common reference degree n+6 gives the exact fixed-order integral identity



$$
\boxed{
\sum_{d=0}^q Q_d J^{5-d}P_{n+1}
=
\sum_{j=0}^2\sum_{d=0}^6
\widetilde N_{j,d}J^{6+j-d}
(n-\theta)_{\underline j}P_n.}
\tag{1}
$$



Every displayed integral power is nonnegative. There is no degree or genericity exception.

**Coefficient proof.** A term B_k z^k becomes B_k t^(n-k)/(n-k)!. Applying (n-theta)_j multiplies it by (k)_j. Multiplication by z^d after j derivatives gives z^(k-j+d). At reference degree n+6 its transformed term is



$$
(k)_j B_k\,t^{n-k+6+j-d}/(n-k+6+j-d)!,
$$



which is exactly J^(6+j-d)(n-theta)_j applied to the original term. On the left the change from reference degree n+1 to n+6 yields J^(5-d). Summing proves(1). The normalization B_n(1)=1 has not been altered.

There is also a useful exact inverse formulation. Set



$$
\mathcal W_n=
\sum_{j,d}\widetilde N_{j,d}J^{6+j-d}
(n-\theta)_{\underline j},
\qquad
H_n=I+\sum_{\ell=1}^q\frac{Q_{q-\ell}}{Q_q}J^\ell.
$$



Since J is injective on polynomials, applying derivative order5-q to(1) gives



$$
H_nP_{n+1}=Q_q^{-1}\partial_t^{5-q}\mathcal W_nP_n.
\tag{2}
$$



For each fixed n, H_n has a bounded inverse on L2(0,1). Indeed, if
sigma_n=sum_(ell=1)^q |Q_(q-ell)/Q_q|, the Volterra powers obey
||J^m||<=1/m! by the convolution bound. Writing H_n=I+V_n gives
||V_n^r||<=sigma_n^r/r!, so the Neumann inverse converges in operator
norm and



$$
\|H_n^{-1}\|_{2\to2}\le e^{\sigma_n}.
\tag{3}
$$



This is an exact existence bound, not a useful uniform estimate when sigma_n grows. It displays explicitly where an unconditional finite-state theorem can still lose the desired asymptotic scale.

## 9. A concrete next asymptotic intermediate and its limits

A sufficient next lemma is the following estimate for the actual normalized orbit:



$$
\boxed{\|P_{n+1}\|_2\le C(n+1)\|P_n\|_2
\quad(n\ge n_0),}
\tag{4}
$$



with an absolute C independent of n. In terms of the now explicit operators, this asks for an estimate of



$$
Q_q^{-1}H_n^{-1}\partial_t^{5-q}\mathcal W_n
$$



on the actual selected P_n. It need not hold on every polynomial of degree n. Proving it on the whole polynomial space would be a stronger sufficient result.

Iterating(4) would give ||P_n||2<=n! exp(O(n)), hence the missing upper bound M_n=||P_n||1<=n! exp(O(n)). Equivalently it would prove the desired lower bound exp(-O(n))/n! for the exact inverse-norm residual delta_n. A two-step version with C²(n+1)(n+2) would suffice if parity prevents a one-step bound.

Equation(1) is new exact structure; inequality(4) is not proved. Crude differentiation inequalities can lose several powers of n per step, and the generic Volterra inverse bound(3) can lose exp(sigma_n). Neither loss is acceptable without sharper information about the actual coefficients and selected solution. Thus no norm upper bound is inferred from fixed operator order or denominator nonvanishing.

Even the desired factorial norm upper bound would not determine the exponential cancellation rate in the endpoint integral or control the primitive endpoint denominator. It is a concrete analytic intermediate, not an irrationality criterion by itself.
