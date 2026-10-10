> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact column-normalization bridge for the active binary producer

The coordinator derives this algebraic interface from the complete contact excerpt and old A5turn20; no remote operational instruction is used. The formulas are exact rational identities. They do not constitute an all-depth scalar cancellation theorem.

Let Nt=Ntilde, U=(I+S)^n, A=Nt*U, Cx_j=j*x_(j-1)-x_j on0<=j<=b with x_-1=x_b=0, W_j=binom(n+2,j), Rrec=diag(W)*C. The excerpt's T=Rrec*U^-1. Set facvec=(j!)_(0<=j<b) and retain the complete h=h^e+h^F.

Old A5turn20 defines Rcentral=2^(n/2)*binom(n,n/2), X=Zw/(2Rcentral), Y=Vw/(4b!), where Zw=T*Nt^-1*f0 and Vw=e0+T*Nt^-1*h.

For the first column, therefore,

    2X=Rrec*A^-1*(f0/Rcentral).

The existing complete central formulas and first-force Newton filtration supply the normalized f0/Rcentral; computing raw Zw to precision v2(Rcentral)+M and only then dividing would require precision proportional to n. The exact loss is v2(Rcentral)=n/2+s2(n/2).

For the second column define the COMPLETE normalized force

    r=(h-A*facvec)/b!.

The exact endpoint identity Rrec*facvec=-e0+b!*W_b*e_b implies

    Vw=b!*(Rrec*A^-1*r+W_b*e_b),
    4Y=Rrec*A^-1*r+W_b*e_b.

Every factorial subtraction, logarithmic term and endpoint+1 is retained. In particular the excerpt's exterior e0 cancels against the full finite factorial reconstruction, producing the actual endpoint termW_b*e_b after division byb!. This is not a coordinate relabeling.

Thus the raw second-column recurrence in A5turn14, even if correct, needs input precisionP=v2(b!)+M to yield4Y modulo2^M. Its degree bound4P-3 then scales withb. Raw support at fixedP may be a consequence of common factorial content and does not by itself give a precision-sized algorithm for the actual normalized second column.

The exact normalized exponential force is

    r_i^e=sum_s a_s(n)*(n+i)_falling_s*T_(2n+i-s),
    T_m=(1/b!)*sum_(q=b)^m (m)_falling_q
       =sum_(t>=0) binom(m,b+t)*(b+t)!/b!,

with invalid terms zero. Since(b+t)!/b!=t!*binom(b+t,t), the t-tail beyondv2(t!)>=M vanishes modulo2^M. This leaves O(M) shift labels b+t but retains genuinely high lower-binomial indices. The logarithmic part is the supplied complete hF/b!, with any omission justified only after subtractingv2(b!).

The exact displacement/triple-column identities of A2turn6 are rational algebraic identities, potentially reusable here, though their odd-prime saturation conclusions require new binary accounting. A three-column rational Gram reduction alone does not evaluate those Gram entries or prove norm/mixed relative alignment.
