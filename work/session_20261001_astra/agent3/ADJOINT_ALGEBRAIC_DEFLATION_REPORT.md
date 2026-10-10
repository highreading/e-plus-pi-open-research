> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Algebraic adjoint deflation report

Original author research; no independent audit or numerical evidence. The retained B-only positive-moment criteria are preserved.

The actual adjoint is primitively normalized as L=eta G, eta>0, G in Z[t], using its rational coefficient denominator and integer content explicitly. The normalization is F_n(G)=1/eta>0.

Division by psi=1-4t+2t^2 has the exact integer recurrence h_k=g_k+4h_(k-1)-2h_(k-2). Two terminal zero tests certify each successful division. Every primitive quotient remains primitive by Gauss's lemma. The maximal r is also characterized by membership of adj(T)^T Krec^T W Krec adj(T)fP in the multiplication-by-psi^r subspace. This retains the actual reconstruction equations.

For G=psi^r H, maximality gives H(a)H(A)!=0 and |H(a)|>=1/(2^deg(H)|H(A)|). The new conjugate-circle identity expresses positive forcing normalization as a weighted average of G(1+exp(i theta)/sqrt(2)), with nonnegative weight on even n. It controls an average, not H(A) directly.

An exact derivative expansion B=sum beta_(r,k)H^(k)(A)/k! isolates this loss. If beta_(r,0)!=0 and the derivative tail is at most epsilon<1 times |beta_(r,0)H(A)|, then

    |H(A)|<=B/((1-epsilon)|beta_(r,0)|),
    |H(a)|>=(1-epsilon)|beta_(r,0)|/(2^deg(H)B).

All beta coefficients are exact constant-term ratios. The missing actual-family derivative bound is explicitly stated rather than replaced with arbitrary coefficient height.

On the left positive-moment arc, even r=2s gives first surviving coefficient (-8)^s H(a) at x^s. Odd r=2s+1 gives the first possible coefficient at x^(s+1), proportional to rH(a)-H'(a)/sqrt(2). Its vanishing is equivalent to psi dividing J_r=rH+(t-1)H'. Thus rational conjugacy is retained and odd deflation exposes a secondary obstruction. A second resultant and conjugate derivative bound handle J_r when it is not divisible.

The main note combines these coefficients with the retained moment bounds, all higher derivative terms, the endpoint constant, and the full exponential estimate. Complete nonvanishing remains conditional on the displayed dominance inequality. No unbounded-family sign theorem is asserted.

Both newly written files must be read back before completion is reported.
