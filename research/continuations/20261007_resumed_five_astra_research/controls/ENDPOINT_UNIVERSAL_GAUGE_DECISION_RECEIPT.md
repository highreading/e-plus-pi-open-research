> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact decision of the displayed rational endpoint tensor gauge

This receipt concerns only



$$
\ell(n+1)(U_n\otimes R_n)+(n+1)^2\ell(n)=\gamma(n).
$$



The parent pole-orbit argument and A4 turn5 audit establish that every rational
solution has denominator dividing $D_*=(n+1)^2(n+2)$. Over the algebraic
closure, a leftmost solution pole is one to the right of a pole of the forward
matrix; a rightmost pole is a pole of its inverse. Both endpoints force poles
only at -2 and -1. Simple forward poles give orders at most one and two.

For the infinity bound, scale the third moment coordinate by n. The scaled
moment transfer divided by n^2 tends to



$$
U_\infty=\begin{pmatrix}0&1&1/2\\0&-1&-1/2\\0&1&1/2\end{pmatrix},
\quad R_\infty=\begin{pmatrix}0&1\\1&2\end{pmatrix}.
$$



The parent independently verifies
$\det(I+U_\infty\otimes R_\infty)=-1/4$ and that the scaled forcing
has degree at most two. A positive degree d for the scaled rational row would
produce a nonzero term of degree d+2 on the left and no matching term on the
right. Thus numerators have degrees at most 3,3,3,3,2,2 over D_*.

The resulting 22-unknown coefficient system has 64 nontrivial equations.
The seed equation is **not used**. Exact rational elimination gives



$$
\operatorname{rank}A=22,\qquad\operatorname{rank}(A\mid b)=23.
$$



The accompanying certificate records all coefficients, equation labels and
an exact vector w with $w^TA=0$, $w^Tb=1$. This decides nonexistence of
every rational gauge of the displayed tensor type, conditional only on the
now-proved universal denominator and degree arguments. It does not decide
other endpoint representations, resonance/acquisition growth, the actual
primitive denominator, or rationality of e+pi.

Certificate: `endpoint_universal_gauge_certificate.json`.
Personally authored bounded calculation: `endpoint_universal_gauge_audit.py`.
The calculation ran with network and credential access denied. Historical
42-variable limited-class certificate remains unchanged.
