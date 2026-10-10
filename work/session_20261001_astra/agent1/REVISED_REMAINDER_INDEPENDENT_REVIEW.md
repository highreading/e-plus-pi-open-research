> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review: revised remainder and high-row slack

Reviewer: Agent 1. Completed from the saved sources and the verified application execution. This review distinguishes exact reference identities, valid determinant upper bounds, and the failure of particular positive bounding expressions.

## Verdicts

| Claim | Verdict |
|---|---|
| CD subtraction and both reference signs | PASS |
| v_n A_n/h_n=theta_n and relative scalar normalization | PASS |
| Bounds for alpha_n, b_n and the disk constants | PASS |
| Direct comparison of actual reference functions | PASS |
| Explicit two-sided epsilon_n estimates | PASS |
| Gaussian normalization, functional domains and complete companion ratio | PASS |
| Companion asymptotic for fixed lambda and b=floor(n/2) | PASS in that domain |
| Explicit R=n, n>=40 companion inequality | PASS; exp(26) requires no mathematical repair |
| Source-specific high-row slack and divergence of its positive bounding expression | PASS |
| Treating the source's loss condition as an attainable remaining objective with these same majorants | REQUIRES INTERPRETIVE CORRECTION |
| Divergence, shrinking or nonvanishing of the actual growing family | NOT ESTABLISHED |

The exact-rational checker repair is computational, not a repair to any of the displayed mathematical identities. All 44 recorded checks passed after that repair. The unrestricted proofs below supply the analytic and asymptotic arguments; the finite symbolic checks are supporting evidence.

## Inspected sources and scope

The reviewed inputs are:

- ../agent2/ACTUAL_PROJECTION_REMAINDER.md and ACTUAL_PROJECTION_REMAINDER_REPORT.md;
- ../agent3/GAUSSIAN_VANDERMONDE_BOUND.md;
- ../GROWING_HIGH_ROW_SLACK_DRAFT.md and GROWING_HIGH_ROW_SLACK_CHECKS.json;
- ../agent2/GROWING_CONTENT_CORRECTION_SUMMARY.md;
- ../agent4/ADDITIONAL_GROWING_REVIEW.md.

Their hashes are recorded in revised_remainder_independent_checks.json. The main-agent constants certificate identifies the same revised projection source hash as the independent certificate. Its six rational checks support constants only; they do not substitute for this analytic review.

The September identities are used as exact monic Legendre, norm, recurrence and projection identities. The fixed-degree reference normalization is checked directly below. No fixed-b determinant limit, growing-degree nonvanishing inference, prime transfer, or extrapolation from HP samples is used.

Use the source's monic p_k, signed bilinear norm h_k, U=p_(n+1), A_n=p_n(1), scalar v_n=L(p_n/(1-t)), V=K_n(t,1), and actual projection remainder W. The projection polynomial denoted H_n in that source is distinct from the arithmetic auxiliary H_n. The scalar v_n is distinct from the row of factorial functionals. Determinant statements use 1<=b<=n; the growing regime uses n>=2 and b=floor(n/2). Every quotient involving D_V assumes D_V!=0.

## 1. Exact CD subtraction and scalar normalization

The monic CD formula is

    K_n(t,z)=[U(t)p_n(z)-p_n(t)U(z)]/[h_n(t-z)].

Reproduction of constants gives L_z K_n(t,z)=1. Consequently

    W(t)=L_z K_n(t,z)[1/(1-t)-1/(1-z)].

The reciprocal difference is (t-z)/[(1-t)(1-z)], with a positive t-z numerator. Cancelling it before integration proves

    W(t)=[v_n U(t)-v_(n+1)p_n(t)]/[h_n(1-t)].

Setting z=1 in CD instead gives a denominator t-1. Thus, with r_n=p_n/U, alpha_n=v_(n+1)/v_n and b_n=A_(n+1)/A_n,

    W/U=(v_n/h_n)(1-alpha_n r_n)/(1-t),
    V/U=-(A_n/h_n)(1-b_n r_n)/(1-t).

Both signs in the revised source are correct.

Orthogonality applies to p_n(t)(p_n(t)-A_n)/(1-t), since its second factor is a polynomial of degree at most n-1. It proves

    A_n v_n=L(p_n(t)^2/(1-t)).

On t=(1+iu)/2, p_n(t)=i^n Leg_n(u)/binom(2n,n). The odd part of 2/(1-iu) integrates to zero against Leg_n(u)^2. Hence

    A_n v_n=2(-1)^n/binom(2n,n)^2
              * integral_(-1)^1 Leg_n(u)^2/(1+u^2) du.

Dividing by h_n proves exactly

    v_n A_n/h_n=theta_n,
    theta_n=(2n+1) integral_(-1)^1 Leg_n(u)^2/(1+u^2) du.

The ordinary Legendre norm gives 1<=theta_n<=2. The endpoint recurrence starts at A_0=1, A_1=1/2 and has positive coefficients, so A_n>0. Thus v_n is nonzero with sign (-1)^n. In particular,

    mu_n=v_n/h_n=theta_n/A_n>0,
    nu_n=A_n/|h_n|>0,
    mu_n/nu_n=epsilon_n=theta_n|h_n|/A_n^2.

This is a relative small scalar. It does not state that W/U decays absolutely.

## 2. Disk estimates and the actual reference comparison

On |t|<=1/20, let m=9/20. Starting with p_1/p_0=t-1/2, the recurrence

    p_(k+1)/p_k=t-1/2+beta_k/(p_k/p_(k-1)),
    beta_k=k^2/[4(4k^2-1)]

inductively gives analytic, nonzero ratios with real part at most -m. The reciprocal of a number with negative real part also has negative real part. This justifies the induction and yields

    Re r_n<0, |r_n|<=20/9.

The endpoint recurrence gives b_0=1/2 and b_k=1/2+beta_k/b_(k-1), whence 1/2<=b_k<=2/3 because 0<beta_k<=1/12.

For k>=1, integrating the polynomial recurrence divided by 1-t uses L(p_k)=0 and gives

    v_(k+1)=v_k/2+beta_k v_(k-1).

Apply this at k=n+1, rather than incorrectly applying the orthogonality step at k=0. Alternating signs then give

    |alpha_n|=beta_(n+1)/(1/2+|alpha_(n+1)|)<1/6,
    alpha_n<0,

for every n>=0.

Set F_W=(1-alpha_n r_n)/(1-t) and F_V=(1-b_n r_n)/(1-t). The bounds 19/20<=|1-t|<=21/20 imply

    340/567 <= |F_W| <= 740/513,
    20/21 <= |F_V| <= 1340/513.

Indeed the W numerator lies between 17/27 and 37/27 in modulus. The V numerator has real part at least 1 and modulus at most 67/27. Thus the source's special-row majorants are valid and satisfy the exact comparison

    M_W^sharp/M_V^sharp=(37/67)epsilon_n.

For the stronger comparison of actual functions, put c=-alpha_n, so 0<c<b_n. For Re r<=0,

    |1+c r|^2-|1-b_n r|^2
      =2(c+b_n)Re r+(c^2-b_n^2)|r|^2<=0.

The denominator 1-b_n r_n has positive real part, so division is legitimate. Together with the preceding numerator bounds this proves

    (17/67)epsilon_n <= |W(t)/V(t)| <= epsilon_n.

This is not division of two upper bounds. U, V and W are nonzero on this disk. No nonvanishing of their factorial determinants follows.

The exact symmetry p_k(1-t)=(-1)^k p_k(t) gives r_n(0)=-1/b_n. Therefore the normalized shapes are F_V/2 and F_W/(1+alpha_n/b_n), precisely as stated in the source. Their upper bounds are c_V/2 and 3c_W/2. Also V(0)>0 and

    W(0)/V(0)=(-1)^(n+1)epsilon_n(1+alpha_n/b_n)/2,
    epsilon_n/3 <= |W(0)|/V(0) <= epsilon_n/2,
    W(0)=(-1)^(n+1)theta_n(b_n+alpha_n).

In particular 1/3<=|W(0)|<=4/3. The sharper reference identity preserves this absolute normalization.

## 3. Two-sided epsilon estimates without fixed-b asymptotics

Put a=(1+sqrt(2))/4 and s=(sqrt(2)-1)^2. Then 16a^2=1/s and 1/(2a)+s=1.

The positive endpoint recurrence has beta_k>=1/16. Comparison with its constant-coefficient counterpart, with the same initial values, gives

    A_n>=a^n[1-(-s)^(n+1)]/(1+s)>=(1-s)a^n.

For the upper bound, x_n=A_n/a^n satisfies

    x_(k+1)=(1/(2a))x_k+s[1+1/(4k^2-1)]x_(k-1).

The unperturbed coefficients sum to one, x_0=1 and x_1=1-s. Its running maximum is therefore bounded by

    product_(k=1)^(n-1)[1+s/(4k^2-1)]<=exp(s/2),

using the telescoping sum of 1/(4k^2-1). Hence A_n<=exp(s/2)a^n.

The central-binomial inequalities

    4^n/(2sqrt(n))<=binom(2n,n)<=4^n/sqrt(3n+1), n>=1,

follow by induction. The squared margins in the lower and upper steps are respectively 1 and n. They imply

    2*16^(-n)<=|h_n|<=4*16^(-n).

Combining these inequalities with 1<=theta_n<=2 proves

    2exp(-s)s^n<=epsilon_n<=8s^n/(1-s)^2, n>=1.

Thus log epsilon_n=-tau n+O(1), where tau=-log s. The constants are independent of b. The separate amplitude inequalities in the source follow from the same bounds:

    exp(-s/2)a^(-n)<=mu_n<=[2/(1-s)]a^(-n),
    [(1-s)/4](16a)^n<=nu_n<=[exp(s/2)/2](16a)^n.

These statements concern reference scalars; they are not determinant quotient estimates.

## 4. Gaussian factor and complete companion ratio

The monic Hermite norm for weight exp(-a_G x^2) is j!(2a_G)^(-j)sqrt(pi/a_G). Determinant integration therefore gives

    (2pi)^(-d) integral exp(-a_G sum x_i^2) Delta(x)^2 dx
      =(2pi)^(-d/2)(2a_G)^(-d^2/2) product_(j=1)^d j!.

The contour formula retains its outside factor 1/d!. It is not absorbed a second time into the Gaussian evaluation. With a_G=2R/pi^2 this gives the source's J_d(R). The divided-difference, chord, cosine, and domain-enlargement steps remain inequalities. Gaussian positivity does not assert positivity of the original complex integral.

The difference applications have d=b and use ell_0 through ell_b. The ordinary companion has d=b+1 and uses the same largest functional index b. Thus 1<=b<=n is sufficient for the corrected domains. The common sign on the difference reductions is (-1)^(b+1); absolute bounds remove it. The exact identities remain Y=-D_V and Remainder(1)=D_W+T.

Write rho=1/20 and gap=1-1/(rho R). The positive bounds contain

    C_d=d^(d/2)rho^(-d(d-1)/2)gap^(-d(d+1)/2),
    H_b=(3/4)^((b-1)(b-2)/2).

Direct division of the defined positive expressions gives

    Xi=B_T^sharp/B_W^sharp
      =[(b+1)^((b+1)/2)/b^(b/2)]rho^(-b)gap^(-(b+1))
       * M_V^sharp E_n(R)/(R+1)^(b+1)
       * b!/[sqrt(2pi)(4R/pi^2)^(b+1/2)].

The last b! follows from multiplying J_(b+1)/J_b, which contributes (b+1)!, by the outside ratio b!/(b+1)!. No companion term or integration factorial is missing. Consequently

    |D_W+T|<=B_V^sharp(37/67)epsilon_n(1+Xi).

For fixed lambda>0, R=lambda n and b=floor(n/2), the contour factor has logarithm -(n+b)log n+O_lambda(n). The remaining factorial-radius combination has logarithm O_lambda(n), as do the special/reference amplitudes and the divided-difference ratio. Hence

    log Xi=-(n+b)log n+O_lambda(n)
          =-(3/2)n log n+O_lambda(n).

This domain requires fixed lambda and eventually R>20. It is not a uniform assertion for arbitrary varying lambda_n. The full ratio of positive bounds then has logarithm -tau n+O(1). Only one W row supplies the scalar saving in each remainder determinant.

Neither Xi->0 nor the direct reference comparison bounds T/D_W, D_W/D_V, or T/D_V. D_W can be zero or much smaller than its upper bound. No actual companion negligibility or full-remainder nonvanishing follows.

## 5. Separate proof of the explicit n>=40 inequality

Take R=n, n>=40 and b=floor(n/2). The exact Xi formula admits the following bounds:

    (b+1)^((b+1)/2)/b^(b/2)<=exp(1/2)sqrt(b+1),
    (1-20/n)^(-(b+1))<=exp(20+40/n)<=exp(21),
    b!/[sqrt(2pi)(4n/pi^2)^(b+1/2)]
       <=sqrt(pi/(8n))(pi^2/8)^b.

The second line uses -log(1-x)<=2x for 0<=x<=1/2. The third uses b!<=b^b and b/n<=1/2.

Symmetry gives |U(0)|=A_(n+1). The proved scalar estimates imply

    M_V^sharp |U(0)|<=c_V exp(s)a s^(-n)/2.

Finally (1+2/n)^(n+1)<=exp(41/20) and (n+1)^(-b)<=n^(-b). Substitution yields

    Xi <= K_n/n * [e/(s n)]^n [5pi^2/(2n)]^b,

where

    K_n=exp(1/2+21+41/20+s)
          * (c_V a/2) sqrt(pi(b+1)/(8n)).

There is ample exact margin: c_V<3, a<5/8, s<1/5, pi<4, and (b+1)/n<=21/40. The two factors after the exponential are each less than one. Therefore

    K_n<=exp(95/4)<exp(26).

This proves the source's displayed inequality for every n>=40 without evaluating any new index. The constant exp(26) is valid; the exact-rational programming repair does not invalidate it or the unrelated CD identities.

## 6. Source-specific high-row slack

The inspected revised source actually retains H_b=(3/4)^N_b, N_b=(b-1)(b-2)/2. The recurrence on the same disk proves

    |p_(k+1)/p_k|<=11/20+(1/12)/(9/20)=397/540<3/4.

For p_(n+l)/p_(n+1), there are l-1 adjacent ratios. Replacing only these high-row majorants gives their product (397/540)^N_b. All other factors in the endpoint bound can be left identical, including R, U, the special V row, disk, divided differences, Gaussian factor and outside factorial. Multiplicative dependence on row bounds proves

    |D_V|<=Bhat_V=(397/405)^N_b B_V^sharp.

The cases b=1,2 have N_b=0 and cause no exception.

Put c=log(405/397)>0. On D_V!=0, the actual reduced denominator satisfies q>=1, so

    delta_n^sharp=log(q B_V^sharp/|D_V|)
       >=log q+cN_b.

For even n with b=n/2, N_b=n^2/8-3n/4+1. For odd n, N_b=n^2/8-n+15/8. Thus the source's loss has a positive quadratic lower bound in the prescribed growing regime.

More directly, retain the complete positive expression

    S_bound=q(B_W^sharp+B_T^sharp)/|D_V|.

Positivity and the smaller valid endpoint upper bound give

    S_bound>=q B_W^sharp/Bhat_V
       >=(74/67)exp(-s)q exp(cN_b-tau n).

Accordingly

    log S_bound>=log q+cN_b-tau n+log(74/67)-s.

It tends to positive infinity along every unbounded nonzero-endpoint set with b=floor(n/2). The positive companion majorant is unnecessary for this lower bound on S_bound; it has not been discarded from the actual remainder or from the upper-bound formula.

The broader condition is also correct:

    liminf b(n)^2/n>2tau/c, 1<=b(n)<=n.

It forces b(n)->infinity. Since N_b/b^2->1/2, there is then a positive margin with cN_b-tau n growing at least linearly. Thus S_bound diverges on any unbounded nonzero-endpoint set satisfying that condition. This includes sqrt(n)<<b(n)<=n. No conclusion for the complementary regimes follows from this inequality alone.

This slack argument permits any common R>20 at each index: its compared factors cancel exactly. It needs neither the fixed-lambda companion asymptotic nor the n>=40 estimate.

## 7. Required interpretation and content correction

For fixed lambda and b=floor(n/2), the source correctly derives

    log S_bound=delta_n^sharp-tau n+O(1).

Thus delta_n^sharp-tau n->-infinity is equivalent to this particular positive bounding expression tending to zero. The interpretive repair is that it cannot occur with the source's retained high-row majorants. Its proposed linear sufficient bound on delta is likewise unattainable in this regime. The source's Sections 7–8 and report should describe that as an obstruction to the selected estimates, rather than an unresolved feasible target for the same expressions.

The sharper reference identities and all audited upper inequalities remain valid. The former factor-four comparison does not apply to these revised special rows. The new quadratic slack is a separate obstruction in their common high-row factors.

In the previously audited monic arithmetic scale,

    q/|D_V|=M/g,
    delta_n^sharp=log(M B_V^sharp/g),
    g<=M|D_V|<=M Bhat_V=M B_V^sharp exp(-cN_b).

Here g includes row, minor and contraction contents and the final endpoint gcd in precisely that scale. They must not be added again. The standard leading bound log B_V^sharp=-n^2 log n/2+O_lambda(n^2), together with log M=(5/4)n^2 log n+O(n^2), still gives the ceiling 3/4 for log g/(n^2 log n). Subtracting log(A_b^2)=n^2 log n/4+O(n^2) gives the residual ceiling 1/2.

The stale strict residual target above 1/2 in ADDITIONAL_GROWING_CONTENT.md and ADDITIONAL_GROWING_REPORT.md therefore must be withdrawn, as required by Agent 4's ADDITIONAL_GROWING_REVIEW.md and Agent 2's completed GROWING_CONTENT_CORRECTION_SUMMARY.md. The valid identity g/A_b^2=gamma*d*g0 and the structural recurrences and minor formulas are unaffected. Agent 4's structural verdict is PASS WITH DOCUMENTATION REPAIR; no repetition of its computations is needed.

This is not a divergence or nonvanishing theorem for actual forms. A divergent upper-bound expression is compatible with small or zero actual forms. It neither excludes the growing family nor all estimates rebuilt with different normalization or joint determinant information. Merely changing the high-row constant removes the particular slack exhibited here; it does not prove that the rebuilt bound succeeds. Actual endpoint and full-remainder nonvanishing, and useful control of an actual normalized quotient, remain separate research questions.

## 8. Actual verification and repair record

The inspected current checker already contained the correction

    Original: 20/8 == rat(5,2)
    Corrected: rat(20,8) == rat(5,2).

The original expression evaluated the left side as a Python float, which failed the intended exact symbolic comparison. A later guarded attempt to replace the old text stopped at `Expected exactly one original comparison` because the repair was already present; that attempt made no changes. Inspection confirmed the corrected line before verification.

The numeric audit found no float literals or wholly numeric Python divisions remaining. Other divisions use symbolic or exact-rational operands. Every assertion was preserved. The corrected checker was executed through the application runtime and returned exit code 0, sandboxed=true, with PASS_INDEPENDENT_SYMBOLIC_AND_CONSTANT_CHECKS and 44 passing checks. The saved stdout, certificate and repair record were read back successfully.

Evidence in this directory:

- check_revised_remainder_review.py;
- revised_remainder_independent_checks.json;
- revised_remainder_independent_stdout.txt;
- REVISED_REMAINDER_CHECKER_REPAIR.md;
- revised_remainder_checks_before_verification.json, preserving the pre-existing certificate.

The certificate hashes the seven inputs and the corrected checker. No new HP indices, prime scans, numerical quadrature, network access, installations or historical-link restoration were used. This review and the documentation amendments are confined to Agent 1's directory. Finite checks corroborate algebra and constants; they do not replace the all-index proofs or assert actual-family behavior.
