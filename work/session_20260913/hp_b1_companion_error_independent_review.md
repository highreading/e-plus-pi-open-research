> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the exact degree-one companion error

Date: 2026-09-13. Reviewer: audit_computations.

**FULL PASS.** All five sections of
`hp_b1_companion_exact_error_rate.md` pass. The error identity is for the
original rational companion, the two-functional cancellation has the
claimed cubic prefactor, and the actual residual W(0) has zero
exponential rate. No correction is required. No degree calculation,
matrix scan, or new literature assumption is used in this review.

The statement proved is


$$
e-r_n^*\sim\frac{e^{-\sqrt2}W(0)}{n^3n!},\qquad
 \log|e-r_n^*|=-n\log n+n+o(n).
$$


This closes a second-factorial-order error estimate for this specific
companion. It does not supply its reduced height or an estimate of the
actual b=1 endpoint denominator.

## 1. Exact companion and sign verification

The original companion in `hp_b1_primitive_arithmetic_attempt.md` is


$$
r_n^*=E_n+
 \frac{t_0/n!+t_1g_0-t_0g_1}{\delta},\qquad
 \delta=t_1-t_0.
$$


The original elementary projection identity gives
$g_j=\ell_j(H)-\pi t_j$, so the pi terms cancel from its cross product.
Also, for h(t)=1/(1-t),


$$
e-E_n=\ell_0h,\qquad1/n!=\ell_1h-\ell_0h.
$$


Direct substitution therefore gives independently


$$
\delta(e-r_n^*)
 =t_1(\ell_0h-\ell_0H)-t_0(\ell_1h-\ell_1H)
 =t_1w_0-t_0w_1.
$$


This confirms both the target's equation (1) and its sign, without
renormalizing r_n^* or using an approximate Taylor cancellation. With
$D(P,Q)=\ell_0P\ell_1Q-\ell_1P\ell_0Q$, the numerator is exactly
-D(V,W), not D(V,W).

## 2. Actual fixed-parameter analytic inputs

The reviewed degree-two source, `hp_b2_endpoint_attempt.md`, Sections
3-4, supplies the needed facts for the same fixed Möbius parameter:

- U=p_(n+1) has reciprocal root moduli at most 2;
- U(z/n)/U(0) tends locally uniformly to exp(-sqrt(2)z);
- V/V(0)=(U/U(0))G_V and W/W(0)=(U/U(0))G_W on one fixed disk;
- G_V,G_W and their Taylor coefficients are uniformly controlled,
  G_V(0)=G_W(0)=1, and their limiting derivatives differ by exactly 1.

More precisely G_V'(0)->1+1/sqrt(2), whereas G_W'(0)->1/sqrt(2).
Thus H=G_W-G_V has H(0)=0 and H'(0)->-1. The relevant value of c is
sqrt(2); the moving-parameter result with c=1 is not reused without
this change. The original degree-two verification proves a resolvent
bound on a fixed disk, so these are uniform analytic inputs, not merely
pointwise convergence on the real line.

## 3. Exact determinant kernel and summable cancellation

The monomial weights of ell_0 and ell_1 give


$$
D(P,Q)=\sum_{k,l\ge0}
 \frac{(l-k)P_kQ_l}{(n+k+1)!(n+l+1)!}.
$$


The sign l-k follows because the first product supplies n+l+1 and the
second supplies n+k+1 after using the same denominator.

Write U/U(0)=sum u_k t^k. The root bound gives
$|u_k|\le\binom{n+1}{k}2^k\le(4n)^k/k!$ for n>=1. For each fixed k,
u_k/n^k tends to (-c)^k/k!, c=sqrt(2). For D(U,tU), put l=j+1. After
multiplication by (n!)^2 n^3/U(0)^2, the termwise limit is


$$
(j+1-k)\frac{(-c)^{j+k}}{j!k!}.
$$


The factorial-ratio bounds dominate this absolutely by a fixed multiple
of (j+k+1)4^(j+k)/(j!k!). Its full sum is exp(-2c): the j-k part cancels
by symmetry and the constant part is the product of two exponential
series. This is a cancellation evaluated under absolute domination.

For all nonnegative shifts r,s the same estimate gives


$$
\frac{(n!)^2n^3}{|U(0)|^2}|D(t^rU,t^sU)|
 \le C(r+s+1)n^{1-r-s},
$$


with C independent of r,s,n. The factor l+s-k-r is bounded by
k+l+r+s and its double factorial series has the stated bound.

The Taylor coefficients of G_V and H obey C_0 rho^(-r) and
C_0 rho^(-s) on a fixed disk. Because H(0)=0, the only term with
r+s=1 is r=0,s=1. Its coefficient tends to -1. The sum over r+s>=2
is O(1/n), since


$$
\sum_{d\ge2}(d+1)^2n^{1-d}\rho^{-d}=O(1/n)
$$


for sufficiently large n. Thus all products and infinite rearrangements
are absolutely justified, even though W itself is not a polynomial.
Its Taylor coefficients define the same factorial functionals as in the
original remainder theorem.

It follows exactly that


$$
D(V,W)\sim-rac{V(0)W(0)e^{-2\sqrt2}}{(n!)^2n^3}.
$$


No uncontrolled Taylor tail is larger than this cancellation scale.

## 4. Division by the actual endpoint and the residual size

The same fixed-shift factorial estimate yields
$\ell_1V\sim V(0)e^{-c}/n!$ and
$\ell_0V\sim V(0)e^{-c}/(n\,n!)$. Therefore
$\delta\sim V(0)e^{-c}/n!$, with a nonzero leading term.
Dividing -D(V,W) by this actual delta proves the target's equation (2).

The source's residual normalization is also exact:


$$
V(0)=\frac{2p_n(1)p_{n+1}(1)}{|h_n|},\qquad
 \frac{W(0)}{V(0)}
 =\frac{(-1)^{n+1}\epsilon_n}{2}
       (1+\alpha_n^*/b_n).
$$


This follows directly from the known second-kind Christoffel–Darboux
formula at zero and p_k(0)=(-1)^k p_k(1). The factor 1/2 is correct.
Here b_n tends to (1+sqrt(2))/4 and alpha_n^* to (1-sqrt(2))/4;
their displayed ratio makes the final factor positive and bounded away
from zero. Thus W(0) has sign (-1)^(n+1).

The endpoint recurrence and exact norm give
$\log V(0)/n\to2\log(1+\sqrt2)$, while the proved Padé error has
$\log\epsilon_n/n\to-2\log(1+\sqrt2)$. Hence
$\log|W(0)|/n\to0$. Stirling's formula, including the harmless
factor n^-3, now gives


$$
\log|e-r_n^*|=-n\log n+n+o(n).
$$


The sign follows from the same asymptotic and does not use irrationality
of e as a substitute for an evaluated nonzero limit.

## 5. Scope

The difference between this rate and -2n log n+O(n) is
n log n+O(n); therefore the latter upper bound cannot hold even along
an unbounded subsequence for this companion. This conclusion concerns
its actual error, not every possible new companion construction.
Neither an arbitrary coefficient clearer nor the real sizes of V,W
have been interpreted as the reduced endpoint denominator. The existing
b=1 arithmetic question remains the exact endpoint cancellation problem.
