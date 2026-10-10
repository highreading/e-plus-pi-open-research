> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Effective coordinate content: report

New original paper arithmetic for eligible positive b=3 coordinates at n=13^(s+1)+3, s>=5. The earlier global-content paper, exact 13-adic theorem, and all completed reviews are preserved. No scan or numerical experiment was performed.

The universal map has the explicit primitive kernel

k=((n+2)/2,-(2n+3),n+2).

A Rodrigues/adjacent-determinant calculation gives

U_0 J_1-U_1 J_0=O 2^(2n+1)/(n+1) !=0,
Delta_2(Z)=O^2 2^(2n+1)/((n+1)(n+2)).

Thus rank one cannot occur anywhere on the requested family. This is an exact identity, not a finite rank test.

The note explicitly identifies the original two transformed adjugate coordinates through a GL_2(Z) change. Their gcd is exactly the gcd of

(2n+3)(C_j)_0+((n+2)/2)(C_j)_1,
(C_j)_2-2(C_j)_0.

Removing the diagonal selector scaling contributes a two-dimensional matrix with Smith divisors 1 and h=(n+1)(n+2). The kernel scaling is separately n+1; the full determinant ledger is retained.

For the actual transformed integer matrix Nmat=Qd^T M Aplus^(-1), the relevant adjugate row is (w_0,w_1,d_2). Let nu_j be the gcd of the two third-row entries in the columns complementary to this row index. Dividing those entries by nu_j produces an explicit smaller cofactor pair (P_j,Q_j).

With kraw_j the original adjugate-row content, define

kappa_j=kraw_j/gcd(kraw_j,nu_j),
(Pbar_j,Qbar_j)=(P_j,Q_j)/kappa_j,
G_j=gcd(kraw_j,nu_j),
tau_j=gcd(G_j,Pbar_j,Qbar_j).

The exact effective-content factorization is

r_j=nu_j kappa_j tau_j epsilon_j,
tau_j | G_j, epsilon_j | (n+1)(n+2).

The formula includes an explicit expression for epsilon_j from the primitive reduced pair. Original selector content is already included and is not counted again. If the third adjugate entry d_2 vanishes, tau_j=1.

The companion denominator is also expressed using a primitive two-by-two universal map with determinant O^2 2^(2n+1). Its residual output gcd divides the corresponding normalized determinant. This supplies all-prime bounds involving nu_j and kraw_j, together with the explicit coarse uniform bound

B_j <=72 O (n+2)^5(n+3)^2 500^n ((n+2)!)^2,
log B_j<=2n log n+O(n).

This is a genuine global upper bound but does not establish the favorable rate sought for the companion budget. No new positive exponential lower rate is claimed.

The remaining undecided content is exactly simultaneous prime-power divisibility of (Pbar_j,Qbar_j), capped by G_j. If a=v_p(nu_j kappa_j), t=v_p(tau_j), and primitive inputs are needed modulo p^k, the unnormalized cofactor pair must be known modulo p^(a+t+k). Determining tau_j alone requires the reduced pair modulo p^(v_p(G_j)); saturation at that cap is conclusive. The note also states the separate precision for the polynomial basis factor and final output cancellation.

The universal determinant identities do not decide intermediate-depth common divisibility of the actual exponential Toeplitz cofactors. Consequently no subfactorial companion bound, exponential upper window, or shrinking-form result follows yet. The known 13-primary factor is preserved; other primes are not presumed units. No conclusions are transferred to Gram centers.

Deliverables are COORDINATE_EFFECTIVE_CONTENT_BOUNDS.md and this report. Both require controller readback before completion is reported.
