> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Arithmetic bypass: new deductions and working ledger

Author deductions in the current assignment, not an independent review. Existing phase and saddle files are preserved. No computations or scans have been performed.

Work from n=2^s>=4 and an adjacent pair m,m+1 both eligible, with m in the fixed-rho padded block. Put T=n log n and a_rho=rho log 2. The exact slow parity roots remain r_(epsilon,k)=psi_n^(-1)(epsilon*pi/2+k*pi). The earlier necessary distance is exp(-min(3a_rho,1+a_rho)T+o(T)).

New endpoint identity: write P(w)=V(w)^n A(w)^m=sum p_j w^j, N=2n+4m, alpha=(1+i)/2. Then p_n=U/2^n for even n, and

J=R_complex+(U/2^n)Log(1+i),
R_complex=sum_(j!=n) p_j (alpha^(j-n)-(1/2)^(j-n))/(j-n) in Q(i).

Thus Im J=r+U*pi/2^(n+2), r in Q. The complete logarithmic companion is beta=-2^(n+2)r/U, so beta-pi=-2^(n+2)Im J/U. Eligible U!=0 and irrationality of pi imply Im J!=0. Exact integer coincidences with the matching parity crossing set are excluded. Quantitative separation is not implied.

For j=0,1, let U_j be the forcing, X_j=U_j alpha_j and Y_j=U_j beta_j the complete rational companion numerators, T_j=X_j+Y_j. Let E_j=X_j-e U_j, F_j=Y_j-pi U_j=-2^(n+2)Im J_j, R_j=T_j-(e+pi)U_j=E_j+F_j. All combinations below retain both residuals.

Primitive integer pair a,b (gcd(a,b)=1) gives L=L_m(a+b L_1), L_1=4t^4-16t^3+20t^2-8t+1. Its exact polynomial content is c=gcd(a+b,4) in {1,2,4}. Forcing U_ab=aU_0+bU_1 must be nonzero; the primitive selector forcing is U_ab/c. Opposite parity of a,b guarantees U_ab!=0, v2(U_ab)=n/2, and c=1. With h=max(|a|,|b|), the primitive coefficient l1 height has logarithm 2m log7+log h-log c+O(log(m+1)); a proof using evaluations at -1 and -(1-1/(m+1)) will appear in the final note.

Let Jfac=n+4m, N=2n+4m, t_0=N/2-v2(n!)-v2(Jfac!). The existing exact raw exponential valuation and v2(Y_j)>=1 imply v2(T_0)=t_0 and v2(T_1)=t_1=t_0-d, where d=v2(Jfac+4)-1>=1. Hence Delta=U_0 T_1-U_1 T_0!=0 and v2(Delta)=n/2+t_1 on an eligible adjacent pair. This is exact complete-companion noncollinearity, not a claim about the logarithmic-only determinant.

The actual combined denominator satisfies v2(q_ab)=[v2(U_ab)-v2(aT_0+bT_1)]_+. Unless v2(b)=v2(a)+d, the numerator valuation is the smaller of v2(a)+t_0 and v2(b)+t_1. For primitive a,b, the tie is possible only when a is odd and v2(b)=d. Only that tie can lower the individual m dyadic denominator floor. It needs its own high-order congruence calculation; the individual exact law cannot simply be inherited.

Set N_1=N+4, J_1=Jfac+4, O=lcm of odd positive integers<=N_1, D=n! J_1! O. Then A_j=D T_j are integers. For any primitive a,b with U_ab!=0,

g=gcd(aA_0+bA_1,D U_ab),
q_ab=D|U_ab|/g,
q_ab |c_ab-S|=D|aR_0+bR_1|/g.

The endpoint matrix with columns (A_j,D U_j) has nonzero integer determinant -D^2 Delta. Thus g divides |D^2 Delta|. For each prescribed reduced rational p/q, integer coefficients a=qA_1-pD U_1, b=pD U_0-qA_0 realize center p/q; their own gcd must then be removed. This proves rational surjectivity, not an approximation theorem for S.

Quantitative ledger to complete: G=2^(n+2)(|J_0|+|J_1|)=exp(a_rho T+o(T)), U_*=|U_0|+|U_1|=exp(o(T)), and E_* bounds |E_0|+|E_1| with E_*=exp(-T+o(T)). For tau=|aF_0+bF_1|/(hG) and eta=|U_ab|/(hU_*), bounded primitive errors imply tau<=H eta U_*/(qG)+E_*/G. Away from the dyadic tie, this requires tau<=exp(-min(3a_rho,1+a_rho)T+o(T)). A sufficient budget using q<=exp(d_q T+o(T)) and eta>=exp(-ell T+o(T)) requires tau decaying faster than exp(-(d_q+ell+a_rho)T), and d_q+ell<1 to discard the full exponential residual. Otherwise the complete residual itself must be cancelled with a certified bound.

The logarithmic slope determinant Delta_F=U_0Y_1-U_1Y_0 is rational but is not yet proved nonzero. If zero, all combinations have the same beta and logarithmic cancellation cannot improve the normalized companion. If nonzero, its denominator divides O and |Delta_F|>=1/O, giving only a coarse transversality bound. For the complete slope, Delta!=0; the slope is a nonconstant rational fractional-linear transform of S. Its rationality is equivalent to that of S wherever the chosen residual denominator is nonzero. This identifies the extra arithmetic, rather than claiming it has been supplied.
