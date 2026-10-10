> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the raw positive-kernel representation

Date: 2026-09-13. Reviewed `raw_arctan_positive_kernel_attempt.md`
Sections2–7 after independently verifying the primitive dyadic theorem.

## Verdict and one scope correction

The whole-remainder integral, positive convex mixture, uniform
exponential kernel rate, and cancellation ledger pass. The proof does
not obtain a whole-remainder asymptotic, and its explicit retention of
the varying polynomial and cancellation ratio is necessary.

The projection and integral construction must be stated for n>=1.
At n=0 the canonical triple is(-1,1,4), but there are no high moment rows.
Equation(8) would incorrectly require C=-1. This finite boundary issue
does not affect any asymptotic claim; the author was notified to state
n>=1 throughout that construction.

## 1. Exact beta/Borel identity and full remainder

For n>=1 the first n+1 high coefficient equations determine C* by
orthogonal projection, and the remaining n-1 equations give the extra
orthogonality rows. The endpoint equation has coefficient4 because this
family uses arctan(z), rather than4arctan(z).

The inverse of the coordinate change
P_B(x)=sum_j B_j(1-x)^(n-j)/(n-j)! is exactly
B_(n-k)=(-1)^k P_B^(k)(1). For each monomial t^d, the beta integral is



$$
\frac1{d!(n-j)!}\int_0^1x^d(1-x)^{n-j}\,dx
 =\frac1{(n+d+1-j)!}.
$$



Thus integrating P_B against the Borel transform reproduces every
factorial functional exactly. Subtracting all Taylor terms through
degree n gives ell_B(h-H_n), so the resulting integral represents the
entire evaluated remainder, including both tails. At the raw endpoint,
the Abel justification is legitimate, and the factorial sums are
absolutely convergent.

## 2. Positivity and exact normalization of the weights

The raw Legendre recurrence has positive coefficient beta_k and preserves
parity. Hence Q_k has positive coefficients in precisely its parity.
The Legendre-square integral gives sign(v_k)=(-1)^k, while h_k has that
same sign. Thus v_n/h_n>0 and a_n<0.

Consequently S_n=Q_(n+1)+|a_n|Q_n has strictly positive coefficients
in every degree0,...,n+1. The Borel transform of S_n/(1-t) is exactly
the sum of exponential tails with those coefficients. This proves
G_n=sum_d w_(n,d) T_d, with each weight positive.

The normalization is also exact. Applying L to K_n(t,1) gives1 because
the kernel reproduces the constant polynomial. Christoffel–Darboux
then yields



$$
v_nQ_{n+1}(1)-v_{n+1}Q_n(1)=h_n.
$$



Dividing by h_n proves sum_d w_(n,d)=1. There is no missing factor4 or
endpoint normalization. It follows that w_(n,0)e^x<=G_n(x)<=e^x on[0,1],
and the entire series is absolutely dominated there.

## 3. Uniform coefficient bounds

The backward ratio recurrence and beta_k in(1/4,1/3] give
3/16<|a_n|<1/3. The Rodrigues coefficient comparison for even degrees
has a central-binomial ratio at most1 and a factorial product with
every factor at most2k. This gives the bound(2k)^d/d! relative to the
constant coefficient. For odd degrees the analogous product has d-1
factors, giving(2k)^(d-1)/d! relative to the linear coefficient.

The two neighboring lowest-coefficient ratios in the source,
k^2/(2k-1) and2k+1, follow from the same Rodrigues coefficients and
the constant-term recurrence. Their use in the two parity cases is
valid. For even n,



$$
s_1/s_0=\frac{(n+1)^2}{(2n+1)|a_n|}<6(n+1).
$$



For odd n, the ratio is |a_n|(2n+1), which is smaller still. Combining
this with the separate even and odd coefficient estimates proves the
single uniform bound



$$
s_d/s_0\le3\,[2(n+1)]^d/d!.
$$



Since T_d(x)<=e^x x^d/d!, summing gives



$$
w_{n,0}\le G_n(x)
 \le3e\,w_{n,0}\exp(2\sqrt{2(n+1)}),\quad0\le x\le1.
$$



The auxiliary series inequality follows termwise from
binom(2d,d)<=4^d and the even part of exp(2sqrt(z)). The constant is
independent of x and n, which is the required uniformity; no pointwise
asymptotic has been promoted to a uniform one.

## 4. The kernel exponent

The backward ratio map is uniformly contractive with derivative at
most1/3. Its positive limit solves x(1+x)=1/4, giving
|a_n|->(sqrt2-1)/2. The stated finite-iteration argument does not
assume a boundary condition at an infinite index. Cesaro summation of
the logarithmic ratios gives |v_n|^(1/n)->(sqrt2-1)/2.

The norm recurrence gives |h_n|^(1/n)->1/4. The even constant
coefficients are products of alternating beta indices, so their
degree-normalized root tends to1/2. The extra |a_n| factor in one parity
does not change that limit. Thus w_(n,0)^(1/n)->sqrt2-1.

The logarithmic error supplied by the preceding uniform bound is O(sqrt n).
Therefore the supremum statement for log G_n(x)/n follows on the entire
closed interval[0,1], including x=0.

## 5. Forced sign changes and the exact remaining quantity

For n>=2 the extra row ell_B(Q_(n+1))=0 becomes an integral of P_B
against a strictly positive Borel polynomial on(0,1). Since B(1) is
nonzero, P_B is not the zero polynomial. It must therefore take both
positive and negative values. The positive kernel does not make the
whole integrand have one sign.

The negative two-by-two factorial moment determinant is computed
correctly; those moments cannot themselves come from a positive real
measure. The beta/Borel identity avoids that issue by keeping P_B
explicitly signed.

After B(1)=1 normalization, the weighted absolute integral lies between
w_(n,0)M_n and3e exp(2sqrt(2(n+1)))w_(n,0)M_n. Multiplication by the
exact cancellation ratio theta_n and by the actual reduced q_n gives



$$
\log|L_n|=\log q_n+n\log(\sqrt2-1)
 +\log M_n+\log\theta_n+o(n).
$$



The proven o(n) term is independent of the unknown sizes of M_n and
theta_n. The possibility that theta_n is extremely small has not been
excluded or absorbed into that error. Its at-most-one possible zero
follows from the independently verified distinctness theorem, while
its positive values have no quantitative bound here.

The representation and kernel asymptotic are consequently rigorous
progress. They do not supply primitive shrinkage or an irrationality
proof. The source makes that distinction correctly.
