> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent relative-saddle and phase-sparsity review

Status: scoped PASS. Independently examined agent2/LARGE_SELECTOR_RELATIVE_SADDLE.md Sections 2–7 and ../LARGE_SELECTOR_PHASE_SPARSITY_DRAFT.md Sections 1–4. This is a paper review; no numerical computation was performed. Older saddle analyses, normality, the completed dyadic review, and the accepted residue gate were not reopened.

## 1. Exact scaling and critical equation

Write a=(1+i)/2 to avoid confusing the endpoint with a rational exponential companion. The substitution w=a-i x/2=a(1-a x) sends the original orientation x=1 to x=0. Thus reversing its limits gives the factor i/2. Direct substitution gives V(w)=x(1-x/2)/2 and A(w)=-2i C0(x)^2. With x=lambda t, the resulting prefactor is exactly

P=[i/(2a)](2a)^(-n)(-2i)^m lambda^(n+1).

The exponent in the source retains w^(-(n+1)) through -(1+nu)log(1-a lambda t), where nu=1/n. There is no dropped amplitude depending on t.

Multiplying the logarithmic critical equation by w V(w)(2w^2-1), and using w V'(w)-V(w)=(2w^2-1)/2, gives

n(2w^2-1)^2+16m w^2 V(w)-2V(w)(2w^2-1)=0.

This multiplication is used near the displaced saddle, where its factors are nonzero; it does not identify every quartic root as a contributing saddle.

Expansion of the scaled analytic phase gives

phi(t)=log t-2t+lambda[((-1+i)/2)t^2+(i/2+nu a)t]+O(lambda^2).

Consequently

t_s=1/2+lambda[-1/8+i/4+nu a/4]+O(lambda^2),
F=phi(t_s)=-log 2-1+lambda[-1/8+3i/8+nu a/2]+O(lambda^2).

Both displayed source expansions check. In particular w_s=a-i lambda/4+O(lambda^2). The exact F, rather than any fixed truncation multiplied by n, is necessary in the relative formula.

## 2. Branches, contour and global separation

On fixed rectangles surrounding [1/16,8], t stays away from zero and all other logarithm arguments tend uniformly to one as lambda tends to zero. Compatible analytic branches therefore exist. The removable lambda=0 definition follows from the convergent expansion of log C0(lambda t)/lambda. These statements also hold uniformly for nu in [0,1].

The original integer-power integrand makes the endpoint scaling globally unambiguous. Only the central contour uses logarithms. Its horizontal translation and the two vertical connectors remain within the analytic rectangle; the corresponding w contour avoids w=0. Cauchy's theorem therefore preserves the integral with the appropriate connector orientations.

The modulus identity |A((1+iy)/2)|=(1+6y^2+y^4)/4 and convexity give |A/(-2i)|<=1-7x/8. The remaining quotient of nth powers has modulus at most one, and the extra reciprocal factor at most sqrt(2). Thus the complete real integrand is bounded by sqrt(2)t^n exp(-7nt/8).

At the small endpoint, log(1/16)<-log 2-1. At the large endpoint, log 8-7<-log 2-1. The source's two integral estimates therefore have a fixed exponential gap relative to the saddle, uniformly for sufficiently small lambda. Polynomial factors in n do not affect this gap.

For a<=u<=8 and |v|<=1/64, Re((u+iv)^(-2))>1/100 as asserted. Uniform convergence of phi'' to -1/t^2 then gives strict concavity of Re phi along the translated horizontal segment. Its stationary point is t_s, since the full complex derivative vanishes there. Integrating the second-derivative bound gives the quadratic gap. The connectors have a fixed phase gap by continuity from their real endpoints. This controls the entire deformed contour and the untouched real tails; no classification of other quartic roots is required.

## 3. Uniform relative remainder

The local root is unique in a fixed disk by the perturbation of 1/t-2 and is analytic by its simple derivative. Derivatives of the phase through the orders needed for the local expansion are uniformly bounded. Also beta=-phi''(t_s)=4+O(lambda), so Re beta is uniformly positive.

On a symmetric horizontal neighborhood, put r=u/sqrt(n). The cubic first-order term integrates to zero against the even complex Gaussian. The quartic contribution and the square of the cubic contribute O(1/n). Taylor remainders are controlled using uniform derivative bounds and Gaussian moments; restriction to |r|<=n^(-2/5) makes expansion of the exponential uniform, and strict concavity controls the complement by exp(-c n^(1/5)).

The Gaussian integral is sqrt(2pi) beta^(-1/2), with the branch continued from beta=4. Its modulus is bounded away from zero. Hence the absolute local estimate is also a relative O(1/n) estimate. The connectors and global tails are exponentially smaller relative to this same nonzero scale.

This validates the source's uniform relative formula, including its orientation, phase, and nonvanishing conclusion for sufficiently large n and sufficiently small positive lambda. The stated block regime eventually lies in this domain. The modulus of P is 2^(-(n+1)/2) 2^m lambda^(n+1), confirming the logarithmic prefactor in equation (14).

## 4. Adjacent ratio and signed phase drift

For fixed n, lambda'-lambda=-lambda^2/n+O(lambda^3/n^2). Analytic dependence gives bounded derivatives of F and beta. The positive real lambda prefactor contributes no phase. The factor (-2i)^m gives the exact quarter turn. Using the two separate relative-remainder bounds contributes O(1/n) to the adjacent logarithmic ratio without differentiating those remainders.

Thus the relative ratio in agent2 Section 7 is valid. The sharper imaginary expansion follows from Im F_lambda=3/8+O(lambda+nu):

theta_(m+1)-theta_m=-pi/2-3lambda^2/8+O(lambda^3+1/n).

The beta factor contributes O(lambda^2/n), already absorbed. In the specified blocks, 1/n=o(lambda^2) and lambda^3=o(lambda^2), uniformly. The signed positive drift and both sets of bounds in main Section 2 follow. Compatible phase lifts exist because each adjacent ratio remains near -2i.

The relative adjacent noncancellation statement also follows with the source's constants: if |J_(m+1)+2iJ_m|<=|J_m|/2, the Euclidean norm of (Im J_m, Im J_(m+1)/2) is at least 3|J_m|/4. Both imaginary parts cannot then be less than |J_m|/2.

## 5. Sparsity and precise accepted scope

For L=floor(rho^2(log n)^2/8), accumulation of the drift over fewer than L steps is between zero and 1/8. For an even separation, at least two increments accumulate, giving distance from pi Z at least 1/(4rho^2(log n)^2). For an odd separation, the distance is at least pi/2-1/8. Both exceed twice delta=1/(100rho^2(log n)^2). Therefore an L-node interval entirely within the saddle domain contains at most one exceptional phase. Partitioning any longer interval proves the ceiling(k/L) count. This is a proved phase-sparsity implication, not identification of exceptional integer nodes.

Main Section 4 follows algebraically from the newly reviewed analytic result together with its stated external inputs: the exact normalized logarithmic residual identity, the upper bound log|U_m|<=(n/2)log log n+O(n), the nonzero-forcing domain, and the complete exponential residual bound. These external inputs were not independently re-audited here. Under them, |sin theta_m|>=2delta/pi at nonexceptional nodes yields its complete logarithmic-error lower bound. The exponential term is negligible and the reverse triangle inequality yields the complete-error bound. Combining with the separately accepted dyadic denominator identity yields the primitive-error bound, with binary digit sums absorbed into O(n).

Accordingly: unconditional scoped PASS for the explicit integral's Sections 2–7 and the resulting phase drift and sparsity in main Sections 1–3; PASS for the deductions in main Section 4 relative to its explicitly retained external identities and bounds. No new unresolved repair was found within this scope. No explicit finite threshold is supplied by this asymptotic proof.

The review does not exclude isolated exceptional-node sequences, resolve exponentially accurate phase alignment, extend to all selectors or coordinate centers, or prove any irrationality statement. Sections 8 onward of agent2 and Section 5 onward of the main draft are outside this examination.
