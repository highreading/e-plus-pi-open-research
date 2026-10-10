> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Endpoint lattice research report

New exact all-size arithmetic, conditional on the square contact matrix J being nonsingular:

1. The actual rational endpoint lift is V=J^(-1)G, where G_(k,1)=1 and G_(k,2)=sum_(h<=k)(1/h!+f_h). This includes the correct positive sign from division by z-1. A reduced square system has size n+b; reconstruction of A' must retain its denominators.

2. Let d be the least denominator of V and W=dV. The saturated endpoint lattice is exactly {u in Z^2: Wu=0 mod d}. If t_2 is the gcd of the two-row determinants of W, its index is

I=d^2/gcd(d,t_2).

Thus d|I|d^2, and v_p(I)=2v_p(d)-min(v_p(d),v_p(t_2)). This replaces maximal-minor content of the full constraint matrix by two-column content of the actual lift. It introduces no arbitrary clearer.

3. A primitive direction u has minimal integral lifting factor m(u)=d/gcd(d,entries of Wu). The resulting coefficient triple is primitive but its endpoint gcd is m(u). For two independent primitive directions the sublattice index is m(u_1)m(u_2)|det[u_1,u_2]|/I. This distinguishes lattice index, coefficient primitivity, endpoint gcd, and reduced denominators.

4. Every primitive rational direction is available. Its primitive complete remainder is exactly the remainder of the rational lift, because radial scaling cancels against the endpoint gcd. Therefore lattice arithmetic alone cannot produce two useful approximation directions.

5. The research note gives an explicit complete exponential-plus-arctangent tail functional and a rigorous directional majorant B_n(u), with the inverse-J conditioning visible. Selecting two independent primitive directions with both majorants tending to zero is a precise sufficient target. A saturated lattice basis is unnecessary and can be unsuitable: triangular bases contain a direction whose primitive form is 1.

Remaining requirements: normality, directional bounds exploiting the actual lift and complete-tail cancellation, and an independent-pair selection theorem. No useful asymptotic estimate for d, its minor content, or the directional second minimum has yet been established. No irrationality conclusion is claimed.

Full derivations: ENDPOINT_LATTICE_RESEARCH.md in this directory. These results use paper proofs; no old audits, 907-check run, prime tables, or frozen approximation solves were repeated. Sources and completed artifacts were not edited.
