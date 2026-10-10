> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Coordinator proposals for independent audit, 2026-10-04

These are mathematical proposals, with proof obligations explicitly identified. They do not settle e+pi.

## Full divided-coordinate support interface

Let L=3M, N=L+1, phi_d=(y+1)(y-1)^d/d!, rho=mu-delta_{-1}. The regular lattice has basis 1,phi_0,...,phi_(L-1). Its Gram E on the phi coordinates is integral and invertible at3. Eliminating E leaves the constant pivot a, a unit. Hence the FULL regular block A_reg has an integral inverse. All moments mu(phi_i phi_j)=binom(i+j,i)e_(i+j) and mu(phi_i)=t_i are integers. Therefore the full target phi_N force is integral, including its constant row.

Replace phi_L by r=sum_(D=0)^M tau_D phi_(3D), tau_D=(-1)^(M-D)binom(M,D); tau_M=1 makes this an integral unimodular divided-coordinate change. Pairings of r with phi_i, i<L, are the full residual v_i in3M Z3. Its constant coupling is mu(r)=sum tau_D t_(3D), divisible3 because every t_(3D)=2mod3 and sum tau_D=0. Thus every full regular coupling u is divisible3.

If the exceptional solution is theta/3, regular solution x=A_reg^-1(f-u*theta/3) is integral. Multiplying the original projection coefficients by3 therefore leaves only the r coordinate modulo3:
3eta_(d+1)=theta*tau_(d/3) mod3 for3|d, and0 otherwise. This proves full support, not selected tail entries, PROVIDED the phi_N target and eta coordinate normalization agree with the recorded monic expansion. That normalization is exhibited in A1turn9 and must be checked again.

For m=v3(M)>=2 this makes the last three dangerous factorial terms vanish at modulus3^(m+2): d=L-1,L-2 are off support; d=L-3 has tau_(M-1)=-M. All lower terms contain both L and L-3. With the proved raw linear jet and projected correction bounds this should complete Qloc=(y+1)(y-1)^(n-2)*(3y-71-3M) mod3^(m+2). This is for the actual locally normalized primitive polynomial.

## Complete weighted matrix at fourth depth

Use the exact all-pole functional M(F) in A4turn12/13 and the monomial basis y^a, 0<=a<=m=(A+1)/2. The endpoint-adapted basis is an integral unimodular change. Parameters A=n-2=H-D, H=3^(h-1), d=3D/2-1, nu=D/2-1. Strip only the actual unit lambda. The matrix partitions as [[3L,3X],[3X^T,E]]. Let U denote monomials0..D-1 and Z columns z_i=y^i(y-1)^D, i<nu. Ehat=E-3X_U^T L_U^-1 X_U; R=E0^-1, E0_ab=[y^(3H-1)/2](y-1)^A y^(a+b); F=(Ehat-E0)/3. Full pole cutoffs are the exact a3^r<=4n-3, not inferred nearest poles.

On27|j and D<H/108, A1turn14 provides Qcore81=(y+1)(y-1)^A(3y+10); that prior complete proof is attached. If its coordinate support proof needed repair, the previous section addresses it. The all-depth theorem alone atK3 is insufficient, but is not the only source.

Let L_ext be the SAME all lower-pole functional (divided by3) extended from LOW to index d and all HIGH indices; keep four lower layers through modulus81. The top-pole contribution is absent in pairs (U,d), (Z,d), and (d,d) by degree. Therefore X_(U,d)=L_ext(U,d), X_(Z,d)=L_ext(Z,d), and E_dd/3=L_ext(d,d) at the necessary precision. Verify these identities from the actual polynomial quotient; its endpoint-subtracted division preserves coefficients modulo81.

The extension w_nu=y^nu(y-1)^D has degree d and annihilates L_ext against every monomial through degree d modulo81 by the same four-layer half-grid gap. If L_U is the actual unit first block, eliminating U and using existing Z annihilation should yield L_ext(d,d)-L_ext(d,U)L_U^-1 L_ext(U,d)=0mod81. Thus F_dd/3=0mod3. Likewise V_d=Z^T X_d=0mod27, and K_d=0, should give J e_d=0mod3.

CORRECTION to the earlier coordinator proposal: F e_d need not be supported only at m. The TOP perturbation is explicit:
(E_top-E0)/3=[y^rstar](y-1)^A(y+3)y^(a+b) mod3.
At column d it can have an entry at m-1 as well as m. The extended lower recurrence gives its mod3 part only at m. Hence the expected full support is span(e_(m-1),e_m), sufficient for cancellation; do not assert the stronger one-edge hypothesis. R sends this two-edge span into span(e_d,e_(d+1)); K annihilates both, while all R entries among m-1,m vanish. This would imply KRF e_d=0 and (FRF)_dd=0.

The inverse orientation is explicit: R_ab=[z^(d+m-a-b)](1-z)^(-A), with negative degrees zero, modulo3. Then KRK^T=0 because its possible degree (H+3)/6+D+i+j lies strictly between D and H, where (1-z)^(-A)=(1-z)^D/(1-z^H) has zero coefficients. Each identity above needs actual-entry proof, not merely representative rank. If all pass the fourth carry is zero; final gcd only gets its justified lower bound, not an exact denominator.

## Cubic cancellation at b~kappa*n^(2/3)

A3turn16 already proves reciprocal-anchor ratio for all d=o(n). For the next critical regime, refine the true logarithmic derivative at each real anchor using Q's sharp mean in the q-tilted measure and the quadratic expansion
1/(exp(-it)+q)=1/(1+q)+it/(1+q)^2+(q-1)t^2/[2(1+q)^3]+O(|t|^3).
This predicts A_j'/A_j=d/(1+q)+(d^2/n)*c1(q)+error, c1(q)=(q-1)/(2alpha_ref(1+q)^3), alpha_ref=sigma/M. Need weighted phase estimates to show the derivative error small enough after multiplication by d/n. The principal trace contribution is O(d/n); the cubic absolute sum bound d^(5/2)/n^(3/2) multiplied by d/n tends0 at d~n^(2/3). Phase/insertion correction to Q can be bounded using VarQ and actual denominator, not a large exp(Cd^2/n) bound. Real positive tilts retain EQ=d^2/(alpha_ref*n)*(1+O(d/n)).

Use the cubic scalar saddle value formula, with a=U'(1), beta=U''(1), alpha=f''(1):
nf(r)+U(r)=nf(1)+U(1)-a^2/(2nalpha)+beta*a^2/(2n^2 alpha^2)-f'''(1)*a^3/(6n^2 alpha^3)+O(d^4/n^3).
For both scalar phases f'''(1)=-3alpha. Leading beta=-d/(1+q)^2 must be justified to error o(d), using actual differentiated integrals or holomorphic controls. With q+=M, q-=rho, a+=d/(1+M)+(d^2/n)c1(M); a-=-d/(1+rho)-(d^2/n)c1(rho).

The pure cubic saddle-value difference is -d^3/(sigma^6*M*n^2). The cross term from the first derivative corrections has difference +d^3/(2sigma^4*M*n^2). Since sigma^2=2, these are equal and opposite. Exact anchor reciprocity removes the common characteristic value correction. This suggests no surviving kappa-dependent constant at the critical2/3 scale, and possibly a further range b=o(n^(3/4)). The latter range would require stronger derivative remainder bounds; do not infer it automatically. Verify every sign, coefficient, phase denominator, whole residual and outer sector before asserting either extension.
