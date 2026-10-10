> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Multi-row remainder report

New author paper deductions; not independently reviewed. Earlier two-row results are preserved, and their reported factor 101/[9(n+3-b)] is not used as a premise. No controls or numerical scans were recomputed.

For the relaxed balanced construction, choose

    1<=m<=floor((b-1)/2), k=n+m.

The 2m-1 retained high rows from p_(n+1) through p_(n+2m-1) annihilate every t^r p_k for 0<=r<m. Thus

    ell_x(p_k/(1-t))=ell_x(t^m p_k/(1-t)).

The subtraction polynomial is explicitly Q_m=p_k(1+t+...+t^(m-1)). Its high-basis coefficients obey

    c_(0,l)=1_(l=k),
    c_(r+1,l)=c_(r,l-1)+c_(r,l)/2-beta_(l+1)c_(r,l+1).

Their total absolute mass is at most (12/7)[(19/12)^m-1]. Nevertheless the combined subtraction has ordinary coefficient norm at most m L_k, and its exact residual numerator t^m p_k has norm exactly L_k=||p_k||_1. The coefficient amplification is therefore fully accounted for before the residual is bounded.

One further subtraction introduces the exact boundary terms

    (-1)^m product_(l=n+1)^(n+m) beta_l * ell_x(p_n)
      +1_(2m=b-1) ell_x(p_(n+2m)).

They are not assumed to vanish. The guaranteed scheme stops at the stated m.

Put A_k=p_k(1) and d_k=2|h_k|/A_k^2. Both are rational and d_k>0. The complete remainder satisfies

    |R(1)|<=B_m(x),
    B_m(x)=d_k |Y|
       +3(L_k/A_k) sum_j |x_j|/(n+m+1-j)!.

This retains the pi error as well as the complete exponential companion. Their exact signed relation is R/Y=E_k+(-1)^k epsilon_k when Y!=0; possible cancellation is not excluded.

Including the changing reference norm and endpoint normalization gives

    B_m(x)<=c_m B_1(x),
    c_m=max{3^(-(m-1)),[28/(9(n+3-b))]^(m-1)}.

For n-b>=7 this is at most 3^(-(m-1)). The comparison uses identical coefficient data and compares explicit weights, not actual quotients through upper bounds. The slow-growth choice b=floor((n/(1024 log n))^(1/4)), m=floor((b-1)/2) is eventually compatible with n>=512 b^4 log n and gives an unbounded number of subtractions.

Assume separately that the actual normality matrix J is nonsingular. Let Phi be the rational B-coefficient endpoint lift, x=Phi(P,Q)^T. The note specifies Phi exactly through the primed-coordinate inverse J^(-1)F0, without assuming an estimate for it. Define

    r=n+m+1-b,
    w_j=r!/(n+m+1-j)!,
    gamma=3 L_k/(A_k r!),
    Sigma=Phi^T diag(w_j^2) Phi=[[U,V0],[V0,W]],
    Delta=UW-V0^2>0,
    Z=(b+1)(gamma/d_k)^2.

Then the rational positive definite matrix and scalar

    G=2[e_2 e_2^T+Z Sigma], eta=d_k

satisfy the complete uniform bound

    |P+Q(e+pi)|<=eta sqrt((P,Q)G(P,Q)^T).

The e_2 e_2^T term retains the full pi-error envelope. The complete matrices eta_m^2 G_m also improve by at least 3^(-2(m-1)) relative to m=1 when n-b>=7, for fixed n,b and the same lift.

The rational center is exactly V0/U=p/q in lowest terms. The main criterion's two targets become

    E=2(b+1) gamma^2 U/q^2,
    F=[2 d_k^2+2(b+1) gamma^2 Delta/U]q^2.

Neither tends-to-zero statement is proved. The explicit conditioning is

    U=sum_j w_j^2 Phi_(j,1)^2,
    Delta=sum_(i<j) w_i^2 w_j^2 det(Phi_[i,j])^2.

The lift of (1,0) supplies the necessary check (b+1)gamma^2 U>=1. Thus a factorial scalar saving cannot be promoted to endpoint smallness without controlling the actual inverse and the reduced center denominator. The retained term 2 d_k^2 q^2 in F is also indispensable.

For every integer triple, divide by its own endpoint gcd g: x/g=Phi(P,Q)^T and R/g=P+Q(e+pi). Minimal radial lifting multiplies coefficients and that endpoint gcd by the same factor, which cancels. Neither a coefficient clearer nor a lattice index replaces q.

The substantive result is a controlled multi-row scheme with a net full-majorant gain and an explicit rational quadratic certificate. Its usefulness for shrinking primitive pairs remains conditional on the unresolved inverse and center-denominator estimates. Normality is not reproved or independently accepted here, and no irrationality conclusion is claimed.

Full derivations and boundary formulas: MULTIROW_REMAINDER_RESEARCH.md. Both deliverables require read-back before completion is reported.
