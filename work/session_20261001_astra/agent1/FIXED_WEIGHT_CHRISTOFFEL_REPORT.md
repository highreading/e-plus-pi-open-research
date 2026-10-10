> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Fixed-weight Christoffel research report

The fixed weight t admits a complete one-step transformation of the established monic Legendre system:

    Q_k=(p_(k+1)+b_k p_k)/t,
    hhat_k=b_k h_k,
    Ahat_k=2A_(k+1),
    vhat_k=v_(k+1)+b_k v_k.

Every weighted polynomial Gram determinant is nonzero. The norms retain alternating signs; no positivity of the complex bilinear form is asserted. This removes the polynomial Gram gap of the earlier changing-weight proposal without importing balanced contact normality.

The transformed mass is pi-2. Its rational second-kind endpoint is

    what_k=w_(k+1)+b_k w_k-2Ahat_k.

The actual HP endpoint quotient contains the shift -2. Omitting it changes the numerator; retaining it gives no denominator gain by itself because integer translation preserves a reduced denominator.

New uniform estimates on |t|<=1/20 include, for n>=2,

    |Q_n/Q_(n+1)|<=180/79,
    |alpha_hat_n|<5/36,
    Mhat_W=(2080/1501)vhat_n/hhat_n,
    Mhat_V=(3780/1501)Ahat_n/|hhat_n|,
    (2/7)epsilon_hat_n<=|What/Vhat|<=epsilon_hat_n.

Exactly,

    epsilon_hat_n/epsilon_n=(1+alpha_n/b_n)/2 in (1/3,1/2).

The scalar exponential rate remains s^n, s=(sqrt(2)-1)^2. A smaller scalar alone is not a primitive improvement.

The complete exponential companion is retained in two forms: an exact integral of the normalized combined Rodrigues polynomial and a conditioning-explicit bound. The new Rodrigues numerator is

    Psi_k=Pcal_(k+1)'+b_k(2k+2)(2k+1)Pcal_k.

For n>=40 and b=floor(log n), both endpoint cancellations apply. With r=n+2-b and the appropriate actual normalized vector lambda,

    (lambda dot full_U_tail)/Ahat_(n+1)
      =e/[Ahat_(n+1)(2n+4)!]
          * integral_0^1 exp(-x)x^r(1-x)G_lambda(x) dx,
    deg G_lambda<=n+b.

The vector retains the actual endpoint d or Y. No favorable uniform norm estimate for G_lambda follows automatically.

For the explicit determinant companion majorant at R=n,

    Xi_hat<=exp(26)/n^2 [e/(s n)]^n[5pi^2/(2n)]^b<1/400,

uniformly for n>=40 and b<=n/2. Its ratio to the same-index balanced companion majorant is less than 6/n. These are comparisons of positive bounds, not actual determinant quotients.

The actual primitive budget is

    |L_w|<=q_w/Delta_hat
          [epsilon_hat_n+C_hat eFhat_n/(n+2-b)!].

Here q_w is the final reduced endpoint denominator. The coefficient-norm comparison gives

    (8/11)Fbal_n<=Fhat_n<=(43/54)Fbal_n.

Thus the reference contribution improves by a factor between one third and one half, and the companion tail has one additional factorial factor, provided the same-index actual arithmetic and conditioning ratios are controlled. Those ratios remain open. The report does not infer a primitive saving from a smaller unnormalized remainder.

One natural selection is conclusively stopped: imposing ell_beta(p_(n+1))=0 restores exactly the missing lowest balanced equation. The weighted selected triples then equal the balanced triples at the same n,b and contact 2n+b+1. Their primitive forms are identical. In the respective n! and (n+1)! clearer conventions, g_w=(n+1)g_bal and q_w=q_bal. The apparent extra scale cancels in the final gcd.

The genuinely nonbalanced family remains open. Its exact remaining gap is nonvanishing and quantitative conditioning of the weighted contact determinant d after a specified selector or M+1 contact, together with the actual q_w and a normalized companion estimate. Child 3's balanced normality work is not duplicated or assumed to settle this determinant. The old coarse inverse certificate and stopped audits were not reopened.

Evidence: 41 new symbolic controls passed with exit code 0 and sandboxed=true. No HP degree sweep, prime scan, or repeated earlier control was performed.

Deliverables under work/session_20261001_astra/agent1/:

- FIXED_WEIGHT_CHRISTOFFEL_RESEARCH.md: proofs, exact endpoint formulas, uniform estimates, primitive comparison, and stopped selector.
- FIXED_WEIGHT_CHRISTOFFEL_REPORT.md: this report.
- check_fixed_weight_christoffel.py and fixed_weight_christoffel_checks.json: successful new symbolic evidence.

No primitive shrinking, actual-family exclusion, complete-remainder nonvanishing, or irrationality result is claimed.
