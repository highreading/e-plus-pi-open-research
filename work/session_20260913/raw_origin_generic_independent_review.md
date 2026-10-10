> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the bounded origin jets and generic accessory update

Date: 2026-09-13. Reviewed by audit_results.

Reviewed in full:

- raw_hp_origin_finite_jets.md;
- raw_hp_generic_accessory_update.md;
- the mixed Cramer degree and endpoint-jet dependencies in raw_hp_rational_degree_transfer.md.

**Verdict:** both new arguments pass. No correction is required. The origin result is unconditional for the actual raw family, whereas the twenty-variable update has precisely the stated current-degree generic hypotheses. Neither result proves a bound on the accessory orbit, a remainder asymptotic, or a primitive denominator estimate.

## 1. Exceptional origin: valuations and the high Frobenius solution

Let the echelon orders of span(U,C) be l0<l1 and let M=ord R. The existing two-function multiplicity theorem gives l1<=2n+1<M. For three germs with distinct leading orders, the leading Wronskian coefficient is the nonzero Vandermonde in those orders times their leading coefficients. Consequently



$$
M+l_0+l_1-3=3n-1+h,\qquad h=\operatorname{ord}_0 Q.
$$



Since l0>=0 and l1>=1, this proves M<=3n+4. Since M>=3n+1, it also proves l0+l1<=h+1<=4. The high root is therefore separated from the two low roots for every n>=1.

The cofactor estimate is valid even if differentiation kills a leading monomial. For a germ of order l, its r-th derivative has order at least l-r; a negative right side merely gives a weaker valid lower bound. Every determinant summand has order at least the sum of the three germ orders minus the sum of derivative-row orders. Dividing W013,W023,W123 by W012 gives poles of order at most1,2,3. No division by Q(0) occurs in this argument.

The Euler indicial polynomial must vanish at all three distinct actual leading orders. It is monic cubic, so it is exactly



$$
I(s)=(s-l_0)(s-l_1)(s-M).
$$



Substitution of z^M sum(u_r z^r) into the Euler equation gives the displayed recurrence with denominator



$$
I(M+r)=(M+r-l_0)(M+r-l_1)r.
$$



This is nonzero for every r>=1. In particular the recurrence identifies the normalized actual high solution; no additional claim about convergence of an independently invented formal solution is being used.

For the origin-raise numerator, the last coefficient required to vanish is degree 3n+3+h. The second derivative can bring in the coefficient of R at degree 3n+5+h. Subtracting the smallest possible M=3n+1 gives relative index at most h+4<=7. Thus u0,...,u7 really suffice in every exceptional case. Earlier terms that lie below M are zero and introduce no unknowns.

## 2. All six accessory constraints are necessary and sufficient

At a simple root a of Q away from0,±i, the old analytic solution space has echelon orders0,1,3. Thus the pairs (y(a),y'(a)) fill a two-dimensional space. Evaluation of the scalar equation gives



$$
A_2(a)=-A_3'(a)\ne0,\qquad
y''(a)=\frac{A_0(a)y(a)+A_1(a)y'(a)}{A_3'(a)}.
$$



Substituting into N0 y+N1 y'+N2 y'' shows that its vanishing for every solution is equivalent to the two displayed divisibilities modulo Q. Because Q is squarefree, vanishing at its three roots is exactly divisibility by Q. These constraints remove the entire possible simple pole of the operator image at every accessory point, not just the pole on one selected column.

This remains valid at a=1. There is no endpoint exception to the accessory argument.

## 3. Both logarithmic constraints, including the derivative sign

At a=±i the generic hypotheses give Q(a) nonzero. The Wronskian has an exact double pole, which forces C(a) nonzero: if C vanished, the log-free Wronskian contribution could have at most a simple pole.

With x=z-a and t_j=N_j/Q, the extra nonlogarithmic singular part is



$$
\gamma\big((t_1C+2t_2C')/x-t_2C/x^2\big).
$$



The x^-2 coefficient vanishes precisely when t2(a)=0. After this, the x^-1 coefficient is C(a)(t1(a)-t2'(a)). Thus the second condition is t1=t2', with the sign stated in the note. Since N2(a)=0, it becomes N1(a)=N2'(a). The two polynomial divisibilities by D are therefore both necessary and sufficient.

## 4. Origin and infinity constraints

In the generic case Q(0) is a unit, so M=3n+1. The five numerator coefficients at M-2,...,M+2 are exactly the possible terms below the required order M+3. Their highest required high-solution coefficient is u4. The polynomial-ODE denominator Q(0)(M+r)(M+r-1)r agrees with the Euler-form calculation after restoring A3=zDQ.

At infinity q=3 forces the exponential branch to have polynomial degree n, and the two Laurent echelon degrees to be n,n-1. This fact concerns their plane, not the particular degree of C.

For a Laurent branch of degree k, the highest possible image degree is k+2, coming only from N0's degree5 and N1's degree6. The branch of degree n-1 is therefore already within the target degree n+1. For the degree-n branch the excessive coefficient is proportional to a05+n a16.

For the exponential branch, the two excessive numerator powers are n+6 and n+5. The first coefficient is b_n(a16+a26). The second, after the first has been set to zero, is



$$
b_n(a_{05}+a_{15}+a_{25}+n a_{16}+2n a_{26}).
$$



The b_(n-1) term multiplies the first condition and vanishes. These are exactly the three stated infinity equations. They are necessary and sufficient and require no leading branch connection constants.

## 5. Global sufficiency and the rank18 argument

The rational expressions for Ahat,Bhat,Chat can have finite poles only at roots of Q or D. The accessory constraints remove the Q poles of all three; the logarithmic constraints remove the D poles of Ahat. This proves polynomiality.

The infinity constraints give degree Bhat,Chat<=n+1. On a chosen infinity branch, H=A+C(atan-F_infinity) belongs to the old Laurent plane, and



$$
SH=\widehat A+\widehat C(\arctan-F_\infty).
$$



The second term is O(z^n), while SH is O(z^(n+1)). Hence deg Ahat<=n+1. The origin conditions finish the next Taylor approximation requirement.

Conversely, every unmatched next triple yields a rational first-row Cramer operator with numerator degrees5,6,6. I checked the relevant degree argument and also asked the independent transfer reviewer to check this precise scope: only degree bounds and the new Taylor order enter the argument; endpoint matching is not used. Its local and infinity behavior therefore satisfies all eighteen conditions.

An order-at-most2 operator annihilating the three independent old solutions has zero coefficients, so the correspondence is injective.

For clarity, the dimension claim follows from two inequalities. The unmatched next Taylor space has at least dimension2 by its variable/equation count. Adding the single matching row leaves the independently proved one-dimensional canonical line, so the unmatched dimension is at most2. It is exactly2. The operator coefficient space has dimension20; hence the eighteen displayed homogeneous equations have rank18. This conclusion follows from an isomorphism of actual solution spaces, rather than from merely counting eighteen written equations.

## 6. Endpoint normalization, including Q(1)=0

On the unmatched two-dimensional space, the endpoint map to (Bhat(1),Chat(1)) is injective. Indeed, a vector in its kernel satisfies the matching row and hence lies on the canonical line; that line has Bhat(1) nonzero unless the vector is zero. A linear injection between two-dimensional spaces is an isomorphism. Thus imposing (1,4) selects one point and adds two independent affine conditions.

When Q(1) has a simple zero, the accessory equations have already made both endpoint numerators vanish. Their quotient values are numerator derivatives divided by Q'(1). For the exponential column, let V=sum N_j U^(j). The polynomial numerator is e^-z V. Its derivative is e^-z(V'-V). Since V(1)=0, only V'(1) remains. This verifies the stated u_(j+1) formula and explains why no additional minus-u_j term is present in the final endpoint equation.

At an ordinary endpoint the third-order equation generates higher jets from three initial values. At the present simple apparent endpoint, its local indicial roots are0,1,3; the coefficient of the r-th Taylor unknown is nonzero for r>=4. Thus the six stored jets are more than sufficient to generate the finitely many extra jets needed by the transfer. Dividing by a simple Q root costs one extra Taylor coefficient, but does not increase the state size with n.

The companion transformation and Q update follow from T=Psi_next Psi_old^-1. Their exact scaling is preserved because the endpoint equations fix the next triple's normalization. The result does not assert that the next cubic remains generic.

## 7. Fresh independent controls

The new checker check_raw_generic_independent.py uses the original Taylor/endpoint equations to construct degrees3 and4 independently. It does not replay the archived transfer output.

It verifies:

- all eight relative origin coefficients against the original degree3 remainder;
- the rank18 homogeneous system and rank20 endpoint-normalized system;
- exact agreement of the resulting first row with the original degree4 triple;
- polynomial degree and Taylor-order conditions for both independent vectors of the homogeneous nullspace.

It also checks two explicitly synthetic local controls. The first has analytic orders1,3,10 and origin Wronskian defect3; the exceptional indicial polynomial and eight recurrence coefficients agree exactly. The second has a simple apparent endpoint and verifies the analytic quotient derivative formula. Neither synthetic example is asserted to be an actual exceptional degree of the raw family.

All checks pass. Results are in raw_generic_independent_checks.json.

## 8. An additional bounded local lemma for the exceptional extension

The following observation may help replace the generic logarithmic constraints when Q vanishes at a=±i.

**Lemma.** Let h=ord_a Q and c=ord_a C for the actual raw family. If c>=1, then c<=h. In particular c<=3; when h=0, C(a) is necessarily nonzero.

**Proof.** Write x=z-a and R=H+gamma C log x with H analytic. After subtracting the logarithmic C column, the Wronskian is W(H,U,C) plus determinant terms whose first-column entries are 0, gamma C/x, gamma(2C'/x-C/x²). The analytic determinant has valuation at least c-2. The extra determinant terms have valuation at least2c-3, which is at least c-2 for c>=1. Thus ord_a W>=c-2. The exact Wronskian formula gives ord_a W=h-2, proving h>=c. Cancellation can only increase the valuation, so it does not weaken this bound. ∎

This is a local degree-independent bound. It does not by itself provide all pole-removal equations at a multiple accessory/logarithmic collision. Root is deriving that larger construction separately.
