> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Coordinate-center arithmetic completion report

The retained paper work is now supplied in LOG_TWO_INVERSE_REVIEW.md and COORDINATE_CENTER_ARITHMETIC.md. The narrow review has verdict PASS WITH A TERMINOLOGY REPAIR on n>=16, 3<=b<=n, n>=512b^4 log n, with 1<=m<=floor((b-1)/2). The inverse operator bounds themselves allow b>=2. The logarithmic residual is holomorphic inside |z|<sqrt(2), not entire; the interior contours remain valid. The log(2) rate is an upper-envelope rate, not a signed asymptotic or nonstabilization theorem.

The coordinate research proves a nonempty selection rule using rational construction data only. With u=Psi(1,0), lambda=n+m+1, omega_j=(lambda)_j, and c_lambda=sum_(j=1)^b omega_j^(-2), choose j>=1 satisfying

    b(1+c_lambda)(w_j u_j)^2 >= sum_i(w_i u_i)^2.

Such a coordinate exists because sum_i u_i=0. Its error is at most sqrt(b(1+c_lambda)) times the weighted-vector envelope. The selection factor is less than sqrt(b+1) and has subexponential size on the reviewed domain. One may minimize the actual reduced denominator within this eligible set without using a numerical value of e+pi.

The actual B lift is N/Delta, with N constructed from the smaller Toeplitz adjugate and both forcing columns, including the additive endpoint term. Each coordinate denominator is exactly

    q_j=|N_(j,1)|/gcd(|N_(j,1)|,|N_(j,2)|).

For the guaranteed coordinates j>=1, both numerators are linear bordered determinants. The common inverse denominator and the factorial weights cancel; they provide no primitive gain.

In the saturated basis Phi=K[[g1,g2t],[0,g2c]]/d, chi=g1g2c divides d. If xi,nu are the two B blocks and xi_j!=0, then

    h_j=gcd(g1|xi_j|,|g2(t xi_j+c nu_j)|),
    q_j=g1|xi_j|/h_j,
    r_j=gcd(|xi_j|,|nu_j|), h_j=r_j e_j, e_j|chi.

The coordinate approximant is the primitive endpoint direction of the actual slice B_j=0. Its primitive integral coefficient vector is K(-nu_j/r_j,xi_j/r_j), up to sign. Its endpoint gcd is d e_j/chi, which is distinct from q_j and cancels against the integral lifting factor in the primitive remainder.

Let m_ij=xi_i nu_j-xi_j nu_i, betaB=gcd|m_ij|, and M_j=gcd_i|m_ji|. Then M_j/r_j divides betaB. The actual endpoint sums give the stronger relation

    hxi|betaB|[d/(g2c)]hxi, hxi=gcd_i|xi_i|.

Consequently, at every prime outside d hxi,

    v_p(q_j)=v_p(xi_j)-v_p(M_j).

This locates the remaining ambiguity in explicit projection and endpoint contents and replaces the squared-contraction gcd with unsquared minors. It is a structural actual-family result; no random coprimality is assumed.

The weighted Gram center is an exact convex combination of the coordinate centers. The note retains the zero-first-column term in its variance identity. Neither its reduced denominator nor that of the different direct forcing ratio fQ_0/fP_0 is identified with q_j. An exact reconstruction identity compares the latter ratio with t_j; no later scalar-center proof is independently reviewed.

What remains open is useful denominator asymptotics for an analytically eligible coordinate. The sufficient conditions are q_j->infinity and q_j sqrt(b(1+c_lambda)) delta_n->0, where delta_n is the reviewed log(2) envelope. Failure of these sufficient bounds would not exclude small actual forms. No rationality or irrationality conclusion for e+pi is claimed.

All results in this delivery are retained paper deductions. The prior normality, rational-center, and quotient reviews and their successful outputs are preserved; neither the 21 nor the 907 checks are rerun. Final file readback is the remaining delivery operation after saving these documents.
