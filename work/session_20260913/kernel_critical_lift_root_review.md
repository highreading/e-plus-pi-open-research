> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Root review: raw positive kernel, critical parameter, and unit gcd lift

Date: 2026-09-13. This is a proof review of the complete three named
notes, not a final research report. It identifies their implications
and limits separately.

## Raw-arctangent positive kernel

Reviewed `raw_arctan_positive_kernel_attempt.md` in full. The exact
projection uses the raw moment functional with total mass1 and the
matching condition C(1)=4B(1); no factor from the beta=1 Möbius moment
normalization has been imported. The high rows leave exactly the stated
orthogonalities k=n+1,...,2n-1.

The beta integral has the correct factorial indices. Its Borel transform
converts ell_B(Psi) into the entire evaluated remainder. The raw endpoint
arctangent series may be evaluated by the indicated Abel passage, while
the original moment denominator 1-iu has no singularity. After Borel
transformation the relevant series are absolutely and uniformly
convergent on [0,1].

The sign of v_k follows from Q_k(iu)^2=(-1)^k times a positive constant
times the square of an ordinary real Legendre polynomial. Taking the
real part of 1/(1-iu) preserves that sign in its integral. Hence the
second-kind ratio is negative and every coefficient of S_n is positive.
The Christoffel–Darboux endpoint Wronskian gives sum_d w_(n,d)=1 exactly.
This is the correct normalization for the exponential-tail mixture.

I checked the coefficient comparisons separately by parity. The odd
linear coefficient relative to its adjacent even constant has the
stated ratios k^2/(2k-1) and 2k+1. Together with
3/16<|a_n|<1/3 these give the stated safe factor3 in the bound for s_d/s_0.
The factorial tail inequality and the central-binomial estimate then
give a uniform logarithmic loss O(sqrt n). The backward ratio recurrence
is contractive on the stated bounded interval, so its limit is valid
without specifying an artificial terminal value. All root limits in the
kernel exponent follow.

The polynomial P_B must change sign for n>=2, since it is nonzero and
orthogonal to a strictly positive continuous weight on (0,1). The
negative factorial Hankel determinant is computed correctly. Neither
fact is an asymptotic bound on the signed integral. Formula(28) retains
both its L1 norm and its cancellation ratio, as well as the actual
reduced q. It is a correct decomposition with a proved o(n) term; it
does not yet establish primitive shrinkage.

## Critical moving parameter

Reviewed `hp_moving_mobius_parameter.md` and
`hp_critical_parameter_zero.md` in full. The two-functional determinant
has the correct exact kernel l-k and normalization n^3. Factoring
G_W-G_V before estimating the determinant retains its factor of size
1/b; this is essential when b is proportional to n. The resulting
cancellation occurs at t_1 of order b n^3, not at t_1 of order1.
The kernel prefactor therefore yields the logarithmic displacement
(7/2)kappa* log n.

For the holomorphic extension the complex Jacobi matrix bound, rather
than a real Hermitian-part argument, controls the resolvent. Its distance
from the identity is O(1/n), uniformly on bounded complex x-disks. Root
products and factorial domination are absolute-value estimates and
extend to this setting. The signed replacements for |p_n(0)| and |h_n|
restore the complex kernel identity. The nonzero uniform leading terms
for Delta(V) and 1+t_1 exclude poles on every fixed disk eventually.
Cauchy's formula can therefore be used for derivative convergence.

The limiting derivative is strictly negative on every fixed real
critical interval. This proves a unique simple real zero there and a
distance comparison valid arbitrarily close to it. It does not prove
that any zero is rational, or that rational parameters have small
endpoint denominators. The Weyl argument with a slowly varying logarithm
is valid; an o(1) perturbation is harmless after Cesaro averaging. Its
conclusion is density only, and does not exclude favorable sparse
subsequences.

I requested one criterion wording correction: the favorable liminf must
be restricted to nonzero-distance indices. Merely requiring infinitely
many nonzero forms would not prevent separate zero indices from attaining
a liminf of minus infinity. The author has now made that restriction
explicit. No correction to the analytic theorem was needed.

## Exact unit lift of the special gcd

Reviewed `hp_special_gcd_unit_lift.md` in full. Both differential
identities follow from the displayed formal coefficient equation, so
there is no unresolved integration constant. At x=1 their combination
is exactly J_(n+1)=(n+1)(H_n''+(n-1)(H_n'-H_n)).

For derivative order2 the coefficient summand has falling-factorial
length R at least s+2. The proof correctly separates R>=p^a+2, where
two factors divisible by p^a occur, from R<=p^a+1. In the latter range
the exact valuations of the other offsets equal their small-offset
valuations; s is at most p^a-1. The factor (R-2)! supplies at least
v_p(s(s-1)), cancelling the potentially lost binomial valuation.
The zero falling-factorial case is explicitly harmless.

Thus all s>=2 terms have valuation at least2a. The three remaining terms
give 3(n-1) modulo p^(a+1), with only powers of2 in their denominators.
This works for every odd p, including3. Substitution into the exact
raising identity gives coefficient8, a p-unit. The common valuation is
therefore exactly v_p(n-1), using the previously proved congruence lower
bound for H_n.

The root-tree conclusion is valid, with the residue1 itself treated by
the exact zeros H_1=J_2=0 and other representatives by the new valuation
formula. It removes additional lifts of this branch. It gives no
information about the original large-prime endpoint gate p>2n+2, whose
primes cannot divide n-1. This restriction is correctly stated.

All three reviewed results pass at the stated scopes. None decides the
rationality of e+pi.
