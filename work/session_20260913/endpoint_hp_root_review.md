> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Root review of the new endpoint Hermite–Padé Wronskian lemma

Read the complete `endpoint_hp_continuation.md`. The proof passes the
following independent symbolic and logical checks. This review concerns
the all-index lemma and its evaluated representation; it does not certify
shrinking integer forms or full normality.

1. The convention W(f,g,h) uses derivative rows0,1,2. Subtracting the
   columns Be^z and F C from the R column leaves
   (A,A'+CF',A''+2C'F'+CF''). The omitted subtraction of Be^z in the
   prose is implicit in the displayed column; the explicit formula is
   correct. Expanding yields precisely equation(2), including the sign
   of the -4D' C K term.
2. For degree bounds, AC'-A'C has degree at most2n-2, including unequal
   actual degrees beneath the common degree cap. Its derivative is
   AC''-A''C. The polynomial determinant therefore has degree at most
   3n-2; the remaining rational-derivative terms give at most3n+2 after
   D^2 clearing. The n=0 case is handled separately.
3. When B,C are nonzero, analytic continuation around1+i changes R by
   a nonzero constant times C. A constant linear dependence of
   R,Be^z,C would therefore have zero R coefficient. The remaining
   rational/exponential dependence is impossible. This proves the
   Wronskian is not identically zero. The two omitted coefficient cases
   have the separately stated stronger two-function bounds.
4. If ord_0 R=M, the Wronskian has order at leastM-2, because each
   determinant term contains at most the second derivative of R.
   Clearing by D^2e^{-z} preserves order at0. Thus M<=3n+4. The four
   residual Taylor coefficients provide an injective linear map from
   the matched high-order space, proving dimension at most four.
5. For n>=1 the stronger two-function bound rules out B=0 or C=0
   in a nonzero form of order at least3n+1. The numerator is a nonzero
   integer polynomial of degree at most3n+2 and order at least3n-1.
   Dividing by z^{3n-1} therefore leaves an integer cubic or lower.
6. Expanding the three-function Wronskian gives the stated second-order
   inhomogeneous differential equation. With W(U,V)=e^zK, its Green
   factor is (V(z)U(t)-U(z)V(t))/W(t). Multiplication by the forcing
   N/(D^2K) gives exactly equation(6). The sign is correct and its
   derivative jump at z=t is one. Initial data and paths avoiding K=0
   are necessary, as the report states.
7. K's opposite endpoint signs at n=2 disprove the proposed universally
   nonsingular real-integral route. A complex continuation formula is
   not automatically a positive integral. Under common scalar
   multiplication, K scales quadratically and Q cubically; the
   normalized integral is invariant. The primitive endpoint coefficient
   Y/d still has to be controlled independently.

No mathematical correction is needed. One prose clarification is useful:
the Wronskian column operation removes both Be^z and F C, not merely
F C. No global mathematical novelty is asserted for this use of a
Wronskian zero estimate; its role is an explicit all-index result for
the project's family.
