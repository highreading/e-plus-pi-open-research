> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the both-parity ordinary-cell bridge

2026-09-13. Reviewer: computational audit subagent. Reviewed `general_cell_roth_attempt.md`, the original reports for Items197,250,306,309, the Item237 algebraic coefficient formulas, and the session's fixed-prime Roth and actual-cell extension notes. The large archived rational Hermite/tensor certificate is an explicit imported proof dependency; this review does not claim to have recomputed that certificate from scratch.

**Verdict:** no substantive mathematical gap found in the extension to even r, the resulting j=3 necessary gate, or the extension to any fixed j with `(A_j,B_j)!=(0,0)`. A subsequent exact closure of the remaining fixed-j case is independently verified in Section6 below. Subject to the explicitly imported archived identities and the already reviewed Roth transfer theorem, the whole ordinary radical support has the claimed averaged zero estimate. This is an auxiliary support estimate, not a proof about e+pi and not an estimate for an unbounded sum of valuations.

One sentence in the draft said that a sign both changes and remains constant on a step-six ray. I requested replacement by the exact contour prefactor below. The author confirmed that correction. It changes the explanation, not the resulting factor `16*K_even`.

## 1. Original low/high coefficient reflection

Write Q=2s and let P=P_nu have degree d=r+1+nu+2Q. Its reciprocal identity is

    P(z)=(-1)^r z^d P(1/z).

For the original truncated logarithm A_p, `A_p(z)=-z^p A_p(1/z)`. If tau=p-Q+nu-1 and T=p-r-1, then `p+d-tau=T`. Therefore the low coefficient X equals `(-1)^(r+1)[z^T]A_p P`. Since T exceeds d, the latter coefficient is the exact logarithmic tail `-sum_k P_k/(T-k)`. Reversing P's coefficients contributes another factor `(-1)^r`. The final sign is positive, and `T-d=Q-nu+1`. Thus for both parities

    X_nu = integral_0^1 t^(Q-nu)P_nu(t)dt mod p.

All denominators are positive and at most T<p. There is no inherited odd-r sign left over.

The other truncated logarithm satisfies `B_p(z)=z^(2p)B_p(1/z)`. Hence its original upper coefficient at tau+p equals `(-1)^r[z^T]B_p P`, exactly the sign in the new upper-tail formula.

## 2. Actual factorial representatives and rank-one cancellation

Let epsilon=r mod2 and h=floor(r/2). For the upper B-tail, the actual integer factorial parameters are

    R_actual=(T-epsilon)/2,
    D_actual=R_actual-Q=(r+Q+2-epsilon)/2=h+s+1.

They reduce to the displayed phase parameters because

    D_actual-(r+3-3epsilon)/6=p/6,
    R_actual+(r+1+epsilon)/2=p/2.

The common factorial period is explicitly

    mathfrak_f=(-1)^(D_actual-1) Q!(D_actual-1)!/R_actual!.

All factorial arguments lie in `[0,p-1]`, so this scalar is a p-unit. For either parity the upper f0 summation has t<=h<D_actual, and the upper f1 summation has t<=h+2<=D_actual. Thus the denominator Pochhammers terminate before their first zero. The lower tails have the same `N_actual=r+Q+1<p` for both parities. Their t-ranges are no longer than the odd-r bounds already proved in Item250.

The affine J recurrence uses ordinary pivots `3Q+k` and `Q+k` lying strictly between zero and p. The sole p-pivot is treated before reduction and contributes the terminal constant -1. Removing it would change d_nu; it does not change b_nu. I checked the displayed descending beta-coordinate formula and its adjacent sum. Pochhammer reversal then gives `d_nu=u_nu/2` term by term.

For the homogeneous coordinate, the reflected coefficient indices really are `epsilon+2(h-t)` and `epsilon+2(h+2-t)` in the two rows. Both scalar identities in Section3 have the stated initial value and successive-term quotient. The denominators are nonzero for r>0 and 3 not dividing r. Hence `a_nu=kappa_r f_nu` holds without division by a polynomial coefficient or by f_nu. Taking the determinant with f therefore removes the whole homogeneous and upper-period contribution, including C_j, and gives precisely

    A_j c D_b+(A_j/2+B_j)D_u=0.

This is a necessary condition for an actual collision. No converse is used.

## 3. Period normalization, including the even-r sign

Put a=(r+1+epsilon)/2 and b=-2r/3. Here a>0, b is not an integer, and a+b is not an integer. The beta factors used in the proof are finite and nonzero by meromorphic continuation. The opposite parity has integer first argument `a_opp=h+1`; its beta value is the rational factorial expression obtained by Pochhammer reversal.

Expanding K_nu(iu) proves

    f_nu=2 part_epsilon(A_r,B_r)_nu/Beta(a,b),
    u_nu=2(-1)^(h+epsilon)part_(1-epsilon)(A_r,B_r)_nu.

For nu=1, the beta ratio is `(a+b-1)/(b-1)=-D/q=rho`, so no extra row-dependent beta normalization remains.

Write Omega=Im(A_r conjugate(B_r)). Directly taking the two possible real/imaginary determinants gives the parity-independent exact formula

    D_u=4(-1)^(h+1) Omega/Beta(a,b).

The six-step scalar ratio is consequently `-Beta(a,b)/Beta(a+3,b-4)`. Expanding the gamma shift yields

    K_even=64(r+6)(2r+3)(2r+9)/(27(r+1)(r+3)(r+5))

for even r, and the archived K_odd for odd r.

For D_b, use the original unscaled Item309 one-forms `phi_nu(z)X(z)^r dz`, and let I_delta be the difference of the 0-to-i and 0-to-minus-i period vectors. Let I_Gamma be the inherited infinity-to-1 period vector. Put s_r=i^(r+1). Substitution z=iu and conjugation show for both parities

    I_delta=2 i^epsilon s_r part_epsilon(A_r,B_r),
    f=I_delta/(i^epsilon s_r Beta(a,b)).

Inversion of the phase tail, with its orientation retained, gives `X_meromorphic=(-1)^(r+1)I_Gamma`. Eliminating its homogeneous f multiple gives the exact prefactor

    D_b = (-1)^(r+1) det(I_delta,I_Gamma)
          / (i^epsilon s_r 2^q Beta(a,b)).

Under r->r+6, q decreases by4 and s_r changes sign. This scalar ratio is exactly `16*K_even`, not its negative. This explicit expression resolves the draft's wording ambiguity about signs.

The Item306 cleared identities are polynomial identities over Q(r), rather than tests at odd integers. Their boundary exponents are integers plus or minus 2r/3; none is zero when 3 does not divide r. The vanishing at 0 and1 uses r>0 and is unchanged by parity. Consequently the meromorphic endpoint functional used to kill exact primitives extends to even r. The proof does not discard a divergent ordinary integral.

Finally the displayed rational functions satisfy `R_even*K_even=R_odd*K_odd` by cancellation. Thus the same archived tensor identity supplies the required recurrence for the newly normalized even determinants. The branch coefficient recurrence is a global formal differential identity and likewise has no odd-index restriction.

## 4. Exact initials, units, and nonzero states

I independently recomputed the six even-r initial determinant comparisons at r=2,8,14 and r=4,10,16. All agree with

    lambda_2=-729/98, lambda_4=59049/3025,
    16^n D_b/g_n=lambda_e a_r,
    16^n D_u/g_n=lambda_e b_r.

These computations used fresh standard-library Fraction polynomial operations, direct rational series inversion and Lagrange inversion, without importing any archived or new production checker. The initial two-coordinate branch determinants independently equal

    -4424709835/1594323,
    3604770571325/774840978.

The recurrence's forward coefficient is positive on r/2>0, as proved in Item237. The three initials therefore identify the sequences on each entire ray. Finite initials identify a sequence already proved to satisfy the recurrence; they are not the proof of recurrence membership.

In the gauge product up to r, the largest shifted factor is 2r+3, which is strictly less than the actual prime p=2r+6s+3. The fixed scalars and both initial branch determinants require excluding only finitely many primes. The global branch clearer `6^(r+3)r!` remains a p-unit. No common numerator content is divided out.

For each fixed j with `(A_j,B_j)!=(0,0)`, the coefficient pair `2(-1)^r A_j, A_j+2B_j` is nonzero outside a fixed finite prime set. Multiplication of the first coefficient by `4^s0` preserves that fact. Since the initial two-coordinate branch matrix is invertible, the actual linear combination cannot have both first values zero.

The prior reverse monic recurrence argument then applies verbatim. A four-zero block permits propagation one step backward at s>=9; a three-zero state has its preceding recurrence at s>=7. The same denominator bounds and quintic leading factor apply with h=r/2. Thus there are at most five zero three-states, with no assumed generic nonvanishing. This is the required hypothesis for the already reviewed Roth observation argument.

The fixed-prime indexing `r=e+6n, s=s0-2n` gives `M=((3j+1)p+e)/6+n`. This verifies that the density theorem is being summed over actual construction indices while keeping the characteristic fixed.

## 5. Independent actual-row checks and scope

The independent checker also reconstructed the original integer coefficient C_nu(M), divided it by p, and compared the two resulting values with Item197's three truncated-log moments. It checked both parities on twelve actual rows, seven in j=3 and five odd-r controls in j=2. It separately checked the low-tail integral, lower rational u, upper factorial-period f, the affine X decomposition, and the determinant elimination. All passed exactly. These checks address possible normalization and phase-sign errors; they are not prime-density evidence.

Saved reproducible records:

- `general_cell_independent_check.py`
- `general_cell_independent_check.json`

The j=3 vector `(U,V,W)=(126,30,348)` therefore gives the claimed necessary gate `3*2^(2s)a_r+b_r=0` after fixed-prime exclusions, and admits the auxiliary averaged support theorem.

For the raw all-j tail, the defining inequality gives `p<=6M/(3J+4)` when j>J. Item197's uniqueness of the actual cell for a pair (M,p), followed by Chebyshev's estimate, gives a uniform O(M/J) bound. This step does not require a uniform PNT remainder. The initial reviewed draft left whole-family admission conditional on resolving a coefficient question or treating the pure upper-period exceptional case. The author's subsequent argument in Section6 below resolves that case. No unbounded valuation sum, pointwise content reduction at every M, or statement about the irrationality of e+pi follows from the present result.

## 6. Subsequent all-j closure, independently verified

The author supplied the following elementary argument after the initial review. I independently differentiated both rational functions and verified the recurrence and descent.

For j>=1 put

    S(y)=(1-y)^(3j+1)/(1+y^2)^(2j+2),
    R(y)=(1-y)^(3j)/(1+y^2)^(2j+1).

Then `V_j=S_(2j)` and `W_j=S_(2j-1)`. Differentiating `F=(1+y^2)S` gives

    F'=-(3j+1)R-(4j+2)yS.

Its coefficient of y^(2j) is exactly

    (2j+1)S_(2j+1)=-(3j+1)U_j-3(2j+1)W_j.

Thus U_j=V_j=W_j=0 would force S_(2j-1),S_(2j),S_(2j+1) all to be zero. The logarithmic derivative of S gives the exact polynomial differential equation

    (1-y)(1+y^2)S'
      +[(3j+1)+(4j+4)y-(j+3)y^2]S=0.

At coefficient y^k this is

    (k+1)S_(k+1)+(3j+1-k)S_k
      +(k+4j+3)S_(k-1)-(k+j+1)S_(k-2)=0.

Starting at k=2j and descending to k=2, the last coefficient is always nonzero. The alleged three zeros force each preceding coefficient to vanish, eventually S_0=0, contradicting S_0=1. Therefore the triple (U_j,V_j,W_j) is nonzero for every integer j>=1. This does not assert the stronger, unnecessary statement that U_j,V_j alone never vanish simultaneously.

If A_j=B_j=0, then C_j is nonzero. Outside its fixed finite prime divisors, an actual collision forces both upper moments to vanish. The already audited factorial period is a p-unit, so f_0=f_1=0. Consequently D_u=0 and the proved unit branch bridge forces b_r=0. The single b branch is covered by the same Roth observation theorem: invertibility of the initial two-branch minor ensures that its first two values cannot both vanish, and the reverse recurrence gives the same zero-state control.

Every fixed j is therefore admitted, either by the two-branch gate or by this single-branch exceptional case. For any fixed J, sum the finitely many admitted cell estimates. Bound the remaining raw support by O(M/J). Taking the construction scale to infinity first and then J to infinity proves the whole ordinary radical support has zero normalized dyadic average. The dependence of the excluded finite prime set on j causes no difficulty in this ordered-limit argument. The conclusion remains about radical support; no valuation-tail assertion is introduced.
