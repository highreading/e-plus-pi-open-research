> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact Jacobi endpoint normalization bridge

Coordinator proof, October 6, 2026. This note reuses the integral Jacobi definition in the October5 A1turn1 source; it repairs a missing-source uncertainty in October6 A1turn15. It makes no new claim about full polynomial content, scalar unit hypotheses or original primitive direction.

Keep the SAME parameter A=2m-1 in both Jacobi degrees. Write



$$
J_s(y)=\sum_{k=0}^s\binom{s+A}{k}\binom{s-\tfrac12}{s-k}y^k(y-1)^{s-k}.
$$



Rename the coefficient endpoints to avoid collision with the Jacobi recurrence scalars:



$$
a_m^{\mathrm{end}}=[t^m](1-t)^{3m-1}(1-2t)^{m-1/2},
$$





$$
b_m^{\mathrm{end}}=[t^{m-1}](1-t)^{3m-2}(1-2t)^{m-3/2}.
$$



Evaluating the displayed Bernstein sum at y=-1 gives



$$
J_m(-1)=(-1)^m\sum_{k=0}^m\binom{3m-1}{k}\binom{m-\tfrac12}{m-k}2^{m-k}=a_m^{\mathrm{end}}.
$$



The same calculation at degree s=m-1, without changing A, gives



$$
J_{m-1}(-1)=(-1)^{m-1}\sum_{k=0}^{m-1}\binom{3m-2}{k}\binom{m-\tfrac32}{m-1-k}2^{m-1-k}=b_m^{\mathrm{end}}.
$$



Both equalities are exact characteristic-zero identities. There is no extra scalar or change of basis. In particular, a finite evaluation of the coefficient endpoints evaluates the actual integral Jacobi endpoint pair at the same index. This does not equate the content of that pair with the content of either entire polynomial.

Let a_m^sc be the retained Christoffel evaluation scalar and beta_m^sc the retained monic recurrence coefficient. The source's notation b_m for the latter must not be confused with b_m^end above. Its exact source polynomial satisfies



$$
(3y-\eta)Z_{\mathrm{source}}(y)=(y-\beta_m^{\mathrm{sc}}-a_m^{\mathrm{sc}})J_m(y)-\rho_mJ_{m-1}(y),\qquad\eta=A+71.
$$



Consequently



$$
Z_{\mathrm{source}}(-1)=\frac{(1+\beta_m^{\mathrm{sc}}+a_m^{\mathrm{sc}})a_m^{\mathrm{end}}+\rho_m b_m^{\mathrm{end}}}{A+74},
\qquad
\rho_m=\frac{A(3A+1)}{(4A+1)(4A+3)}.
$$



On the retained original congruence A divisible by3, A+74 is a3-adic unit. On the separately proved resonant scalar branch, v3(rho_m)=4 and a_m^sc,beta_m^sc have valuation1. The endpoint map therefore has determinant rho_m/(A+74), of valuation4 on that branch. It is an exact integral map with a nonunit determinant, so inverse projective transport must pay four digits. Endpoint content and full polynomial normalization remain different quantities.

The mod9 Cartier certificate corroborates the coefficient normalization at80 new endpoint coefficients, using direct characteristic-zero sums. Those finite checks do not certify an eligible original power-of-two middle word. Scalar-branch reachability, primitive direction, complete force, all-prime normalization and the whole error remain separate obligations.
