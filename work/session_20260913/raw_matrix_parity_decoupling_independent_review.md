> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of boundary parity decoupling

Date: 2026-09-13. Reviewer: audit_computations.

Reviewed `raw_matrix_resolvent_parity_decoupling.md` in full.
All identities, constants, and scope statements pass.

The decomposition (K_N=K_{0,N}-J_N) uses the compression of
(J^2-\Lambda), not (J_N^2-\Lambda_N). Parity conjugation
fixes its diagonal and distance-two entries and reverses (J_N).
Consequently (\widetilde R=\Pi R\Pi) has the same norm as (R),
and the resolvent identity is exactly



$$
R-\widetilde R=-2RJ_N\widetilde R.
$$



With (\|R\|\le2/(cN^2)), (\|J_N\|\le N), the norm of
the difference is at most (8/(c^2N^3)). Dividing by two gives
the stated (4/(c^2N^3)) parity off-block bound. The identity



$$
R^2-\widetilde R^2=(R-\widetilde R)R
+\widetilde R(R-\widetilde R)
$$



does not require commutation. It yields the stated
(16/(c^3N^5)) bound after dividing by two.

The two retained boundary coordinates have opposite parity, so these
operator bounds apply to their off-diagonal entries. For
(\Gamma=\bigl(\begin{smallmatrix}d_1&0\\\ell&d_2\end{smallmatrix}\bigr)),
the exact transformed entry is (d_1d_2R_{12}+\ell d_2R_{22}).
Using (d_1,d_2\le N^2/2), ( |\ell|\le N) gives
((c^{-2}+c^{-1})N), with no omitted cross term. Applying the
same formula to (R^2) gives ((4c^{-3}+2c^{-2})/N).

The quoted positive lower bounds on the diagonal entries follow
from the previously independently reviewed matrix CD theorem.
They give the relative estimates (5)–(6) exactly. The diagonal
normalization converts each matrix to a correlation matrix with
diagonal one, whose difference from the identity has norm equal
to the absolute normalized off-diagonal entry.

The final caution is necessary. Neither the boundary congruence
nor these entry bounds makes (P_N) nearly diagonal. Also, the
per-cut error cannot simply be declared negligible after a number
of cuts proportional to (N). The next note
`raw_two_step_channel_transport.md` supplies an additional diagonal
balance estimate and an explicit normalization of that product.
