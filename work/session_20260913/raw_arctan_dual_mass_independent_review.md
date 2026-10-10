> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the raw dual factorial-mass theorem

Date: 2026-09-13. Reviewer: audit_results.
Reviewed `raw_arctan_dual_factorial_mass.md`, Sections1--7, against the
previously independently checked raw projection, positive-kernel, and
primitive dyadic normalization results.

## Verdict

The proof passes. I found no substantive gap in either



$$
M_n\ge\frac{n!}{n^2(n+1)(2n+1)(32e^3)^n}\qquad(n\ge4)
$$



or the asymptotic bound



$$
\vartheta_n\le\frac{\exp(O(n))}{n!}
$$



for the actual family normalized by B_n(1)=1 and the later kernel
G_(2n-1). The latter estimate is obtained from approximation by the
annihilated high span; it does not assume that the remainder stays
bounded and does not use the lower bound for M_n circularly.

The proof of the distance/cancellation estimate is explicitly valid for
n>=4, which is sufficient for its asymptotic formulation. The separate
later-kernel identity is valid for n>=1. No n=0 projection formula is
being used.

The results control opposite factorial scales. They do not give the
remaining exponential rate of M_n*vartheta_n or the final primitive
denominator. They therefore do not imply shrinking integer linear forms.

## 1. Coefficients, parity, and the exact normalized family

The raw monic Legendre equation is



$$
(1+t^2)Q_k''+2tQ_k'-k(k+1)Q_k=0.
$$



Writing lambda=k(k+1), its coefficient recurrence is



$$
[t^{d+2}]Q_k=
 \frac{\lambda-d(d+1)}{(d+1)(d+2)}[t^d]Q_k.
$$



Starting from d=sigma in {0,1}, then applying the Borel transform, gives
exactly the squared-factorial expansion in equation(5) of the reviewed
note. Both sigma! factors equal1. The product stays nonnegative until
it acquires its first zero factor, and remains zero afterwards; later
negative factors do not invalidate a bound on the entire zero product.

For even n, the even high nodes number n/2-1, giving first possible
error degree n-2, and the odd nodes number n/2, giving degree n+1.
For odd n both parities have (n-1)/2 nodes, giving degrees n-1 and n.
Thus every parity and endpoint in equation(6) is correct. The n>=4
restriction ensures neither interpolation set is empty.

The normalization is the actual raw one: C_n(1)=4B_n(1), B_n(1)=1.
The Borel kernel T_n therefore pairs with P_n to give -4. The high
rows are exactly the n-1 indices n+1,...,2n-1, rather than an enlarged
space of rows that the actual polynomial need not annihilate.

## 2. Interpolation error and the explicit factorial constant

For high nodes h_j spaced by2, the denominator of a Lagrange weight is
at least



$$
(4n)^{m-1}j!(m-1-j)!.
$$



The low-node numerator is at most (4n^2)^(m-1). Summing the reciprocals
of j!(m-1-j)! gives 2^(m-1)/(m-1)!, hence the bound (2n)^(m-1)/(m-1)!.
It is bounded by e^(2n) as one term of the exponential series. This
also covers m=1.

Let d=2m+sigma. The consecutive coefficient-majorant ratio is bounded
by 4/(n-1)^2 because d>=n-2. At n=4 the upper bound is4/9<1/2;
therefore the geometric-tail factor2 is valid throughout the asserted
range.

The final conversion of the first majorant to a reciprocal factorial
uses four separate valid inequalities:



$$
4^m\le2^n,\quad n^{2m}\le n^d,\quad
 \frac{n^d}{d!}\le e^n,\quad \frac{n!}{d!}\le n^2.
$$



Together with 2(1+e^(2n))<=4e^(2n), they give the stated
4n^2(2e^3)^n/n! bound. In particular the lower parity offset n-2 costs
only n^2; a factorial of n+1 has not been substituted incorrectly.

The coefficient bound for the normalization kernel is also safe:
Q_k(1)<=2^k, q_(k,sigma)<=Q_k(1), and
|h_k|^(-1)<=(2k+1)4^k give |a_k|<=(2k+1)16^k. Thus the summed
kernel approximation has the factor4n^2(n+1)(2n+1)(32e^3)^n/n!.
Pairing with P_n gives4 on the left; this cancels the leading4 and
produces the exact displayed lower bound for M_n.

## 3. The later-index remainder and primitive normalization

The finite projection identity



$$
\Psi_n-\Psi_m=\sum_{k=n+1}^m(v_k/h_k)Q_k
$$



has the stated sign. At m=2n-1 every term is annihilated by ell_B.
The beta/Borel identity therefore gives the same R_n(1) paired against
G_(2n-1), without changing B_n or P_n.

The previously proved uniform logarithmic estimate for G_m survives
this substitution: (2n-1)log eta+o(n)=2n log eta+o(n), eta=sqrt(2)-1.
Uniformity is enough to sandwich the positive integral
integral |P_n|G_(2n-1) between M_n times the minimum and maximum of G.
No bound on the changing polynomial P_n is required for that sandwich.

With B_n(1)=1, R_n(1)=A_n(1)+e+pi. If q_n is the positive reduced
denominator of A_n(1), the primitive integer form is q_n R_n(1).
This is the correct evaluated denominator, not a common coefficient
clearer or a raw determinant. The logarithmic identity is used only
when the evaluated form is nonzero. The cancellation inequality itself
remains valid when the form vanishes, with vartheta_n=0.

## 4. Infinite positive expansion and its coefficient bounds

The identity G_N-G_M=sum_(k=N+1)^M(v_k/h_k)F_k is finite and exact.
The already established uniform convergence G_M->0 on [0,1] proves
the infinite representation in equation(13). This avoids any unstated
infinite orthogonal-polynomial expansion theorem.

For the raw square identity, the quotient of
L(Q_k^2/(1-t)) by h_k is a positive average of 1/(1+u^2), so
0<v_k/h_k<=1/Q_k(1). The recurrence lower bound
Q_k(1)>=alpha^(k-1), alpha=(1+sqrt(2))/2, starts correctly at k=0,1
and propagates from beta_k>=1/4.

The constant and linear coefficients are exactly



$$
q_{k,0}=\binom{k}{k/2}/\binom{2k}{k}\quad(k\text{ even}),
 \qquad q_{k,1}=\frac{k^2}{2k-1}q_{k-1,0}\quad(k\text{ odd}).
$$



The central-binomial lower bound 4^k/(2k+1) supplies the polynomial
factor in q. These facts give the safe common estimate
0<b_k<=4alpha(k+1)^2 eta^k. No sign cancellation is used to obtain
this bound.

For k>=2n, the high-node numerator in a Lagrange weight is at most
(k+1)^2, giving equation(15). The two terms of the coefficient bound
(16) respectively bound the original degree-k polynomial and its
interpolant. Exact cancellation of all lower coefficients still follows
from interpolation of the monic spectral polynomials p_r.

## 5. Infinite-tail estimates and all convergence passages

Equation(17) has a direct valid proof even though x^s e^(-cx) need
not be monotone. On [k+1,k+2],



$$
x^s e^{-cx}\ge(k+1)^s e^{-c(k+2)}.
$$



Integrating each such interval, multiplying by e^(2c), and summing
proves the claimed comparison with the complete gamma integral.

The first contribution in(16), after weighting by b_k, thus has moment
order2r+2 and denominator ((2r+sigma)!)^2. In both parities



$$
\frac{(2r+2)!}{((2r+\sigma)!)^2}
 \le\frac{(2r+2)^2}{(2r)!}.
$$



The exponential-series tail estimate used in (18) is valid uniformly
in its starting index D. One elementary proof bounds
(D+l+2)^2/(D+2)^2 by(l+1)^2 and D!/(D+l)! by1/l!, then sums the
convergent series sum_(l>=0)(l+1)^2 A^l/l!. Since 2m>=n-2, changing
(2m)! to n! loses only a polynomial factor. The result is exp(O(n))/n!.

For the second contribution, multiplying L(k) by b_k produces moment
order2m, exactly as in(19). There are m+1 factors in
(2m)!/(m-1)!, so it is at most (2m)^(m+1)<=n^(m+1). Division by
(2n)^(m-1) leaves at most n^2/2^(m-1). The c-powers are exponential
in n. This proves the exp(O(n)) bound claimed for sum b_k L(k).
Multiplying by the already proved reciprocal-factorial coefficient
tail finishes the second contribution.

All sums rearranged in these estimates are nonnegative majorants.
Their finiteness proves absolute convergence of sum b_k E_k in sup
norm. Also sum b_k L(k)<infinity proves absolute convergence of every
coefficient of sum b_k I_k in the fixed finite high basis. Thus the
approximant is an actual member of that high span, and its pairing with
P_n vanishes exactly. These are the required convergence and membership
justifications for the infinite interpolation step.

## 6. Cancellation and limits on the conclusion

The distance estimate gives



$$
|R_n(1)|\le M_n\exp(O(n))/n!.
$$



Dividing this by integral |P_n|G_(2n-1), which is at least
M_n min G_(2n-1), cancels M_n. The reciprocal minimum is exp(O(n))
by the uniform kernel theorem. This proves the upper bound for
vartheta_n, with constants independent of n. Both quantities divided
by are strictly positive, since P_n is nonzero and the kernel is positive.

This is an upper bound for cancellation, not a lower bound on it.
The paired estimates M_n>=n!exp(-O(n)) and
vartheta_n<=exp(O(n))/n! cannot be multiplied to obtain a bound for
their product, since their inequality directions differ. The reviewed
note expressly retains that missing product estimate, which is correct.

## 7. Fresh exact controls

`check_raw_dual_mass_independent.py` uses direct rational arithmetic and
the raw three-term recurrence, without importing the author's checker
or an archived certificate. For the two predeclared degrees n=4,5 it
constructs the actual normalized B polynomial from the high moment
rows, the -4 kernel row, and B(1)=1. It then independently integrates
the resulting P against all high Borel polynomials and the normalization
kernel, and checks every low-index parity interpolant.

Both controls pass. They verify the four parity offsets2,5,4,5, the
actual endpoint normalization, and all required high-row vanishings.
Results are in `raw_dual_mass_independent_checks.json`. They are
normalization controls only; the all-degree verdict above rests on
the audited algebraic and analytic proof.
