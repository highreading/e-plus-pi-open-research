> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the closed relative spectral-matrix diagnostic

Date: 2026-09-13. Reviewer: audit_sources. **PASS**, with the exact
certification boundary retained. The analytic finite-to-infinite
cutoff bounds are rigorous. The singular values, principal angles,
and floating-point residuals remain numerical estimates, not interval
certificates. No additional degree or prime was sampled, and no
canonical HP system was solved during this audit.

Reviewed in full:

- `raw_relative_spectral_matrix_diagnostic.md`;
- `probe_relative_spectral_matrix.py`;
- `relative_spectral_matrix_probe.json`;
- the amplitude and relative-truncation theorem dependencies.

## 1. Scope and operator normalization

The source fixes exactly (n=4,8,16), Jacobi cutoff 64, and
precisions 100 and 160. The completed JSON contains precisely those
two runs and those three cases in each run.

The even parity block ends at degree 64 and the odd parity block
at degree 63. The implemented diagonal is



$$
\lambda_l+3/4+t_{l-1}^2+t_l^2,
$$



including (t_l^2) at the cutoff. Therefore it is the principal
compression of the actual operator, not the square of a truncated
multiplication matrix. The only omitted coupling for a finite
parity eigenvector extended by zero is the coupling from its last
retained coordinate (L) to (L+2).

The odd seed amplitude is one half the initial odd coordinate,
while the branch factor is $\sqrt{(2k+1)/3}$. The even factor is
$\sqrt{2k+1}$. All these factors are present in the source. The
phase is positive central coordinate, as used in the amplitude
theorem. The diagnostic matrix is the plus-convention matrix in
the relative-truncation note; it does not silently substitute the
reflected odd-row convention.

The branch/direct-polynomial comparison has an exact algebraic
basis before numerical evaluation. The polynomial identity



$$
E_k=p_k^{(0)}(T)v_0+p_k^{(1)}(T)v_1
$$



also holds with the finite compression in this diagnostic: all
intermediate polynomial degrees are at most (k\le31<64), so no
cutoff boundary is reached by the required powers. Thus its exact
finite-eigenpair projection equals the branch evaluation. This
comparison is a normalization control, distinct from estimating the
finite-to-infinite eigenvector error.

## 2. The rigorous residual and eigenvector bound

The maximum off-diagonal (t_jt_{j+1}\) is (1/(6\sqrt5)<3/40=B\).
For every tail index (j>l\) of the same parity,



$$
d_j-\widetilde\xi_l\ge\lambda_j-\lambda_l-1/4.
$$



Backward Schur elimination starts at the final row. Its next ratio
has absolute value below one, so at each earlier row its correction
to the diagonal is at most (B\). This gives precisely the
denominator $\lambda_j-\lambda_l-13/40$ in the note. Its smallest
possible unperturbed gap is 6, so all denominators are positive and
the induction that the ratios are below one is valid. Equivalently,
one may define these ratios recursively by the positive Schur
denominators first, avoiding division by an unknown eigenvector
coordinate.

Multiplying the ratios from (l+2) through (L), using central
coordinate at most one, and multiplying by the one omitted coupling
gives exactly the rational residual bound $\varepsilon_l$ in
equation (2) of the diagnostic. A finite-support vector lies in the
domain of the infinite operator, so applying the spectral theorem
to this residual is legitimate.

For every other infinite eigenvalue, its distance from the exact
finite $\widetilde\xi_l$ is at least



$$
G_l=2l-1/4\quad(l\ge1),\qquad G_0=7/4,
$$



by the disjoint min-max intervals. Thus the component orthogonal
to the indexed infinite eigenvector has norm at most
$\varepsilon_l/G_l$. With consistent sign, the normalized-vector
difference is at most $2\varepsilon_l/G_l$, as claimed.

For completeness, the phase agreement can be made explicit also
at (l=0). Write either the infinite operator or its compression
as $\Lambda+7/8+W$, $\|W\|\le1/8$. At (l=0), projecting
off the central coordinate gives a diagonal gap at least (15/8),
hence an off-central norm at most (1/15). For (l\ge1), the
already proved bound is $1/(16l-1)\le1/15$. The finite and
infinite phase choices consequently have mutual inner product at
least



$$
(1-1/225)-1/225=223/225>0.
$$



The sign in the small-residual estimate is therefore the same
positive-central phase actually used by the probe. No numerical
phase or gap assertion is needed for this step.

## 3. Tiny normalizers are explicitly controlled

The finite eigenvector obeys the same lower-principal-determinant
formula as the infinite one. Its lower block is unchanged, its
eigenvalue satisfies the same min-max interval, and the preceding
central-coordinate estimate applies to its compression. Hence the
amplitude theorem's explicit lower bound is valid for both exact
finite and infinite amplitudes.

For the anchors (l=n-1=3,7,15\), all indices are in the theorem's
(l\ge2\) range. The rational weakening in equation (4) is in the
correct direction: replace $\sqrt3$ by 1, $\sqrt{2l+1}$ by
(2l+1\) in the denominator, $\sqrt{1-x}$ by (1-x\), and
$e^{-\eta_l}$ by (1-\eta_l>0\). The resulting factors are
positive for all three anchors, as also checked exactly in the
source.

Shifted branch positivity applies because every anchor eigenvalue
is larger than one. It gives the same rational row-denominator
lower bound for the exact finite and infinite rows. The extra
factor (1/2\) in the odd branch safely underestimates
(1/\sqrt3\), while dropping $\sqrt{2k+1}$ also weakens the
bound in the correct direction.

Let (a,\widetilde a\in\mathbb R^{n+1}\) be the unnormalized row
vectors and let (d,\widetilde d\) be their last-two-coordinate
norms. The proof uses



$$
\|a-\widetilde a\|\le N_k E_{\rm all},\quad
|d-\widetilde d|\le N_k E_{\rm top},\quad
d,\widetilde d\ge d_k^{\rm low},\quad
\|\widetilde a\|\le N_k.
$$



The last inequality is Bessel's inequality for the finite
orthonormal eigenvectors. Subtracting (a/d\) and
$\widetilde a/\widetilde d$ proves exactly



$$
\left\|\frac a d-\frac{\widetilde a}{\widetilde d}\right\|
\le \frac{N_kE_{\rm all}}{d_k^{\rm low}}
 +\frac{N_k^2E_{\rm top}}{(d_k^{\rm low})^2}.
$$



Both inverse powers of the potentially tiny normalizer have
therefore been retained. Summing these row bounds dominates the
matrix Frobenius norm and hence its operator norm. There is no
unjustified claim that the small eigenvector error remains small
without this amplification calculation.

## 4. Exact source/JSON reproduction checks

I recomputed the rational-only preparation and cutoff functions
from the probe without executing either numerical diagonalization
or SVD loop. For each of (n=4,8,16\):

- the recomputed exact Fraction equals the saved rational matrix
  error bound in **both** precision runs;
- the claimed displayed upper bounds are valid strict upper bounds
  by exact rational comparison: (1.54\cdot10^{-114}\),
  (4.26\cdot10^{-95}\), and (7.29\cdot10^{-49}\);
- the complete saved 55-digit singular-value, principal-sine, and
  principal-angle strings are identical between the two runs.

As an independent norm check, for all 25 predeclared test rows I
integrated the square of the exact monomial polynomial directly.
The result agrees exactly with the probe's Legendre-moment sum for
$\|E_k\|_2^2$. The integer ceiling of its square root is
implemented exactly using integer arithmetic and Fraction
comparisons.

I also checked the JSON's completion, degree and precision fields,
and all the reported upper inequalities for the saved numerical
reconstruction, kernel, and branch/projection residuals. These
checks verify what the saved numerical data report; they do not
turn those floating-point residuals into interval bounds.

The reviewed hashes are:

```text
5432b8d8d906fc85018404584c0f691b27dde8751efac6efa501f909ece22e46  raw_relative_spectral_matrix_diagnostic.md
059e1d4b33a004f92e0f706db6fefdadb8e9632087f2bfbe060dc61473a511db  probe_relative_spectral_matrix.py
ce76f089108995cb047844f15404817e85070debe9cf806b90f273681044407b  relative_spectral_matrix_probe.json
```

## 5. Numerical linear algebra and the retained limitation

The code obtains a full right singular-vector matrix. Its final
two rows, transposed, form the numerical right kernel. The first
(n-1\) coordinate rows of that basis have a (2\)-by-(2\) Gram
matrix whose eigenvalues are the squares of the two principal
sines relative to the last-two-coordinate plane. This is the
correct principal-angle construction. The rectangular SVD
reconstruction and the reported nonzero condition number use the
correct dimensions and singular-value ordering.

However, `mpmath.eigsy` and `mpmath.svd` are ordinary
multiple-precision floating-point computations here. No interval
enclosures or certified rounding errors are supplied. Agreement
at two precisions and small computed residuals are useful numerical
checks; they do not prove that all displayed digits are correct,
that the exact finite matrices have the reported rank, or that the
exact smallest singular values have a certified positive lower
bound. In particular, comparing the analytic cutoff bound to an
estimated singular value is explicitly a diagnostic comparison.

The note correctly preserves this distinction throughout. No
claim requires repair. To turn the displayed finite cases into
certified exact-matrix statements would require a separate
rigorous finite eigensystem/SVD enclosure, or a verified residual
and invertibility certificate with controlled arithmetic. Neither
that finite certification nor an all-index lower bound is inferred
from the three cases. The present audit adds no sample beyond
(n=4,8,16\).
