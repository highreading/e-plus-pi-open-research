> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of sharp exponential accretivity

Date: 2026-09-13. Reviewer: audit_sources.
Status: PASS. No correction required.

Reviewed raw_sharp_exponential_accretivity.md in full.

For $|\lambda|=1$, writing $b=|\Im\lambda|$ gives the smaller possible real part as $e^{-\sqrt{1-b^2}}\cos b$. Its logarithmic derivative on $0<b<1$ is


$$
b/\sqrt{1-b^2}-\tan b>0,
$$


since $\arcsin b>b$. Its minimum is therefore attained only at $b=0,\lambda=-1$, and equals $e^{-1}$. Continuity handles the endpoints. This proves the sharp scalar assertion and its equality case.

The spectral theorem applies to the unitary generator $K$, whose exponential is normal with eigenvalues $e^\lambda$. It gives $\Re e^K\ge e^{-1}I$ and $\|e^K\|\le e$. The same quadratic-form bound survives orthogonal compression. Applying it to the adjoint as well proves closed and dense range, hence the claimed inverse bounds, rather than only injectivity.

For the actual even scalar equation, the inverse corner $v_0$ is real and positive and the energy is $v_0$. Evaluation at zero has norm $\sqrt{c_m}$. Thus


$$
e^{-1}\|v\|_w^2\le v_0\le\sqrt{c_m}\|v\|_w
$$


indeed gives $\|v\|_w\le e\sqrt{c_m}$. Subtraction of the best predictor and Cauchy--Schwarz introduce one further factor $e$, giving the displayed $e^2\sqrt{c_mD_r}$ bound.

The preceding sector lower bound for $v_0$ can be retained independently. The sharper accretivity changes constants only; it does not replace the independently certified exceptional determinants or any arithmetic estimate.

