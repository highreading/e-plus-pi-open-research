> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the actual rational-parameter denominator theorem

Date: 2026-09-13. Reviewed `hp_parameter_primitive_denominator.md` against
the exact kernel and endpoint identities, including root's subsequent
prime-power strengthening. Verdict: **the identities and actual reduced
denominator bounds are correct**. No correction to the mathematical
statements is required. The scope qualifications about exceptional
primes and rational tuning are necessary and are retained below.

## 1. Christoffel–Darboux sign and the affine leading determinant

Use P_k=p_k(1), with monic polynomials and squared norms at Möbius
parameter one, and denote the second-kind values by v_k*. Their exact
Wronskian is



$$
v_n^*P_{n-1}-v_{n-1}^*P_n=-h_{n-1}.
 \tag{1}
$$



The initial value is -2=-h_0. To check propagation rather than only its
initial sign, the recurrence has the form
p_(k+1)=(t-1/2)p_k+alpha_k p_(k-1), alpha_k>0, while
h_k=-alpha_k h_(k-1). At the endpoint both P and the second-kind values
satisfy the corresponding recurrence after the initial step; their
Wronskian is multiplied by -alpha_k, which proves (1).

The rational pi Padé approximants are f_k=pi-v_k*/P_k. Consequently



$$
f_{n-1}-f_n=-h_{n-1}/(P_nP_{n-1}).
$$



Write V_1=sum p_k P_k/h_k and J_1=sum p_k P_k f_k/h_k, and let their
ordinary coefficients be v_k,j_k. Expanding the top two coefficients
gives



$$
v_nj_{n-1}-v_{n-1}j_n
 =\frac{P_nP_{n-1}}{h_nh_{n-1}}(f_{n-1}-f_n)
 =-1/h_n.
 \tag{2}
$$



The contributions from the next coefficient of the monic p_n cancel.
Thus the sign in root's formula is correct.

Set A=(beta+1)/2 and Q_k=(t-1)^k. Expanding the affine covariance about
t=1 gives V_beta=A sum vtilde_k A^k Q_k, and likewise for J. The change
from ordinary coefficients to these Taylor coefficients sends
(v_n,v_(n-1)) to (v_n,nv_n+v_(n-1)), and similarly for j; hence it
preserves the cross difference (2).

In the bilinear term t_1 ell_0(J)-t_0 ell_1(J), the pair of indices
(n,n) cancels identically. The only remaining pair with the next possible
degree is (n,n-1) together with its reverse. Therefore, with



$$
d_n=\ell_1(Q_n)\ell_0(Q_{n-1})
 -\ell_0(Q_n)\ell_1(Q_{n-1}),
$$



the coefficient of beta^(2n+1) is -d_n/(2^(2n+1)h_n). All remaining
terms linear in V or J have degree at most n+1. This is strictly smaller
than 2n+1 for **every n>=1**, including n=1, when the two degrees are 2
and 3. There is no exceptional linear contribution at n=1.

## 2. Laguerre normalization and positivity, checked independently

The exact finite sum gives



$$
\ell_j(Q_k)=(-1)^k\frac{k!}{(n+k+1-j)!}L_k^{n+1-j}(1).
 \tag{3}
$$



Indeed expanding the Laguerre polynomial on the right gives the term
(-1)^(k+l) binom(k,l)/(n+l+1-j)!, exactly the expansion of (t-1)^k under
ell_j. Thus no factorial or parameter shift is missing.

Put K=L_n^n(1), N=L_(n-1)^(n+1)(1), and M=L_(n-1)^n(1).
The ordinary contiguous identity gives L_n^(n+1)(1)=K+N. The derivative
identity x(L_n^n)'=nL_n^n-2n L_(n-1)^n, together with (L_n^n)'(1)=-N,
gives M=K/2+N/(2n). Substitution into (3) yields, independently,



$$
d_n=\frac{n!(n-1)!}{((2n)!)^2}
 \left[-KN+\frac{2n}{2n+1}(K+N)M\right]
 =\frac{(n!)^2(nK^2-nKN+N^2)}
 {n(2n+1)((2n)!)^2}.
 \tag{4}
$$



Thus with U_n=n!K, V_n=n!N and
T_n=nU_n^2-nU_nV_n+V_n^2, root's formula for d_n is exact.
U_n,V_n are integers because multiplying the finite Laguerre coefficient
formula by n! clears each coefficient denominator, including the
degree-(n-1) polynomial defining V_n.

The positivity argument is essential: the displayed quadratic form is
not positive definite for arbitrary real U,V when n is large. It is
positive for the actual Laguerre values for the stated reason. For
K(x)=L_n^n(x), its differential equation at x=1 gives
K''(1)=nN-nK, and therefore



$$
T_n/(n!)^2=K'(1)^2-K(1)K''(1).
$$



The n roots of L_n^n are distinct and real, as follows from orthogonality
for the positive weight x^n exp(-x) on (0,infinity). Away from a root,
the last expression is K(1)^2 times the strictly positive sum of squared
reciprocals of the root distances. At a root it equals the nonzero
square K'(1)^2. This handles a possible root at one instead of dividing
by its value. Hence T_n>0 for every n>=1.

Using h_n=2(-1)^n/((2n+1)binom(2n,n)^2) in (4) proves



$$
\boxed{[\beta^{2n+1}]X
 =\frac{(-1)^{n+1}T_n}{n2^{2n+2}(n!)^4}\ne0.}
 \tag{5}
$$



For normalization checks, n=1 gives U=V=T=1 and leading coefficient
1/16. At n=2, U=5,V=6,T=26, giving -13/1024, which agrees with the
independently established full symbolic numerator
X=-(13beta^5+beta^4+2562beta^3-382beta^2-191beta+3277)/1024.
These finite checks are separate from the all-n derivation above.

## 3. Actual reduced valuations, including the stronger prime-power form

The previously reviewed polynomial ledger implies that all coefficients
of X and Y are integral at every prime p>2n+1. Let beta=r/s in lowest
terms, let Y(beta) be nonzero, and put



$$
v=v_p(s)>0,\qquad a=v_p(T_n).
$$



Formula (5) has p-adic valuation exactly a, since its denominator is a
p-unit. If v>a, the leading term of X(r/s) has valuation
a-(2n+1)v, strictly below every lower-degree term: their valuations are
at least -2nv. There is therefore no leading cancellation, and



$$
v_p(X(r/s))=a-(2n+1)v,\qquad
 v_p(Y(r/s))\ge-(n+1)v.
 \tag{6}
$$



For the actual reduced denominator q=den(X/Y), this gives



$$
\boxed{v_p(q)\ge nv-a\quad\text{if }v>a.}
 \tag{7}
$$



This is a statement about the ratio's valuation after every common
endpoint factor cancels. It does not merely count a factor in a chosen
clearer. If v<=a, this leading-term argument makes no corresponding
positive claim; the trivial lower bound zero is used.

Define the full prime-power parts



$$
s_>=\prod_{p>2n+1}p^{v_p(s)},\qquad
 g_n=\gcd(s_>,T_n),\qquad
 (r+s)_>=\prod_{p>2n+1}p^{v_p(r+s)}.
$$



At a prime in s_>, the quotient s_>/g_n has exponent max(v-a,0).
For v>a, (7) is at least n(v-a); for v<=a this latter number is zero.
Thus the convenient global consequence is



$$
(s_>/g_n)^n\mid q.
 \tag{8}
$$



The local bound (7) is stronger than (8) when n>1 and a>0, so it should
not be forgotten if a particular candidate denominator is studied.
The original s_good^n divisor is the special case a=0. In particular,
large powers of a prime dividing T_n can still impose an actual cost
once their exponent in s exceeds the exponent in T_n.

For the second divisor, the polynomial identities at beta=-1 give
V=J=0, Y=0, and X=-1/n!. This is legitimate evaluation of the
polynomial endpoint continuation; it does not assert that the original
Möbius formula is defined at beta=-1. If p>2n+1 divides r+s, then s is a
p-unit. Factoring beta+1 from the p-integral polynomial Y proves
v_p(Y(r/s))>=v_p(r+s). Also X(r/s)-X(-1) is divisible by beta+1, while
X(-1) is a p-unit, so v_p(X(r/s))=0. Therefore



$$
v_p(q)\ge v_p(r+s).
 \tag{9}
$$



The supports in (8) and (9) are disjoint because gcd(r,s)=1. Combining
them gives the verified actual denominator divisor



$$
\boxed{\left(\frac{s_>}{\gcd(s_>,T_n)}\right)^n
 (r+s)_>\ \mid\ q_{n,r/s}.}
 \tag{10}
$$



No estimate for the size of this divisor relative to the full s or r+s
has been proved. Small primes are excluded, and the coefficient integer
T_n depends on n. Those restrictions cannot be removed from (10).

## 4. Connection to the critical zero, with the direction of implication explicit

The independently proved critical-window comparison is



$$
|R/Y|\asymp\epsilon_n|r/s-b_n^*|.
$$



For rational parameters in a fixed critical interval and different
from its unique real zero, the primitive forms shrink exactly when
q epsilon_n |r/s-b_n^*| tends to zero. Hence (10) yields the **necessary**
condition



$$
\left(\frac{s_>}{\gcd(s_>,T_n)}\right)^n
 (r+s)_>\,\epsilon_n|r/s-b_n^*|\longrightarrow0.
 \tag{11}
$$



It is not sufficient: other factors of the reduced q can survive.
An exactly rational zero is a separate unproved possibility that would
give rationality of e+pi directly; it is excluded from the nonzero-form
criterion.

A standard continued-fraction guarantee |r/s-b_n^*|<1/s^2 is only an
upper-error guarantee. It neither proves that the distance is of order
1/s^2 from below nor excludes unexpectedly accurate approximations.
Accordingly, the correct conclusion is that such a generic guarantee
alone does not resolve the growing-power condition (11). One must not
infer a lower bound for a particular zero's rational approximation from
this theorem.

This review finds no mathematical correction necessary. The new actual
divisors make a real arithmetic restriction on rational tuning, while
the main rationality question and the joint tuning/gcd problem remain
open.
