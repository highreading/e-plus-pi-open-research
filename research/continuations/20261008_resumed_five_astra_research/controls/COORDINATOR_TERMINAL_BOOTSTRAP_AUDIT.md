> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Terminal bootstrap: coordinator audit of A4 turn3

8 October2026. The full1493-line public report was read. A4 independently
accepted the original A1turn0/1 pole and sparse-filter arithmetic. Its new
terminal bootstrap is locally accepted by the coordinator at the stated
fixed precision. A1 will receive the full proof for an additional independent
audit. No growing cofactor saving or decision on e+pi follows from it.

## The physical exceptional pole in the p25 raw lemma

Retain the original subwindow, Q=3^(h-29), D=10Q-b with
.064<b/Q<.073, N=3^24, L=27*3Q=81Q=3^(h-25).
For deg B<2D, c=2s+1<4D<40Q<L/2. Thus v3(c)<=h-26.
The only c with v3(c)=h-26 in this interval is c=27Q=L/3:
the next positive odd multiple is81Q=L, outside the interval.
The physical odd denominator is at most4H-4D+5<3^(h+1),
so the only physical odd d_v with v3(d_v)=h is3^h.
This checks the uniqueness assertion in the report, without discarding a
physical boundary term or replacing the truncated sum by an infinite one.

The logarithmic scalar is2h-1-v3(k)-v3(d_v). Unequal valuations
of k and c have the previously paid bounds; below26 only the unique
balanced pair survives. Its coefficient is
2*3^25*B_s*sum_(q<=q0)a_q, q0=(3N-1)/2.
Since (Y-1)^N R_N(Y)^2=Y^N-1 modulo3 and N<=q0<2N,
the partial sum is zero modulo3. This pays the last digit.
The report retains the full degree and physical logarithmic cutoff.

## Stationary identity and exact inverse payments

The exceptional residual is r_T=3*t_unit*e_Ym+3^25*r, t_unit a
ternary unit. E_P^(-1) belongs to3^(-1)M, so q_T=E_P^(-1)r_T
is integral. It need not belong to3^24M. Exact stationarity gives
raw_TT=S_P,TT+q_T^T r_T. Both raw_TT and S_P,TT belong to3^26.
Reducing modulo3^25 yields(q_T)_Ym in3^24. The trial has degree<m;
therefore the actual last physical coefficient is in3^24.

For a nonterminal column q_i belongs to3^24M. The mixed raw identity,
its3^26 bound and the exceptional residual leave
3*t_unit*(q_i)_Ym in3^26; the remainder is in3^49.
Thus the nonterminal physical coefficients belong to3^25.
Column transfer costs3^(h-1), safely beyond the used fixed precision.

The same q_T equation yields(E_P^(-1))_Ym,Ym in3^23, because
the residual remainder multiplied by E_P^(-1) is in3^24.
The resolvent transfer costs3^(h-2), so this also holds for E_c.
These are actual LOW/HIGH projection statements, not changes of W.

## Finer radical-terminal coupling

The evaluated mixed-pairing formula in the report retains the exceptional
physical correction. At the d27 pole the shifted4Q coefficient contributes
binom(10Q,4Q)/3=1 modulo3; all stated nonzero offset coefficients have
the paid additional depth. This gives the boundary delta contribution.
The existing corrected middle-terminal divisibility then gives
[y^m]mathcal F_a in3^27, and

    gamma_a=-delta_(a,b/2)-[y^m]mathcal F_a/3^27 modulo3.

The right-hand coefficient at the next precision is still unknown. The
vanishing of the original normalized terminal vector at3^20 does not
evaluate this3^27 quotient. No unsupported p26 filter extension is used.

## Fully returned pivot

For actual T=[[a,z^T],[z,C]] in81M and lambda=eta/3, eta a unit,
u=1-lambda*a belongs to1+27Z3. The explicit inverse of the first two
bordered coordinates has one-digit loss. Their Schur return is
Csharp=C+(lambda/u)zz^T and Csharp-C belongs to3^7M.
The determinant sign was checked: D1=u*det(Csharp).
If C=81B,z=81w, this gives D1/81^r=det(B) modulo27.

No inverse of C was assumed. An actual solution of
(B+(27eta/u)ww^T)v=w with v in3^(-1) would imply the paid directional
bound, but its existence remains unproved. The generic counterexample in
the report correctly defeats an inference from T in81M alone and is not
asserted to occur in the original family.

The new vanishing of the normalized physical terminal vector simplifies
producer returns before the rank-b elimination. The1/9 diagonal return
can expose finer differences; no propagation after it is assumed.
All final column contents, least clearer, ALL-prime gcd, primitive q and
nonzero whole-error conditions remain in the original global ledger.
