> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A positive representation of the unchanged beta charge

Status: coordinator-derived identity; not a proof of a favorable comparison.
The original domain has n=2001b, d=b-1 even, h=n-d, and the primitive
r(x)=a(x-1)^d p_h(x) has all roots positive. Write
P(z)=p_h(z)/p_h(0)=product_i(1-z/rho_i). Then



$$
\sum_{j=0}^{n}|r_j|z^j=|r_0|(1+z)^dP(-z).
$$



For every 0<=j<=n the positive beta weight is exactly



$$
c_{n,j}=\frac{j!(3/4)_j}{(n-j+1/4)_{j+1}}
=(3/4)_j B(j+1,n-j+1/4).
$$



Use Euler's beta integral and the gamma moment
(3/4)_j = integral_0^infinity u^(j-1/4)e^(-u)du/Gamma(3/4).
Expanding the finite coefficient polynomial and applying Tonelli gives



$$
\frac R{|r_0|}=
\frac1{\Gamma(3/4)}\int_0^1\int_0^\infty
t^{n-3/4}u^{-1/4}e^{-u}
\left(1+\frac{u(1-t)}t\right)^d
P\!\left(-\frac{u(1-t)}t\right)\,du\,dt.
$$



Every factor in this representation is nonnegative. The endpoints are
integrable term by term: the worst t power is -3/4, the u power at zero is
-1/4, and at infinity there is only a polynomial of degree n times e^(-u).
It is a representation of the actual integer R, with no rescaling or removal
of the final all-prime gcd. It does not contradict the sign change in the
different reciprocal-moment comparison kernel in A2turn17.

This identity alone proves only positivity already established elsewhere.
The open purpose is to compare it with the complete positive representation
of |F|/|r_0| in A2turn17, preserving tail contributions and the original
orthogonality measure. It gives no pointwise bound between those two measures.

Literature/overlap gate: the parent read the full A2turn17, which derives a
different signed ratio representation; it does not derive this double integral.
This is a classical application of Euler's beta identity, not a new special
function theorem. The primary identity and its positive-parameter hypotheses
were checked in [NIST DLMF 5.12.1](https://dlmf.nist.gov/5.12.E1) on 2026-10-07.
The gamma moment is its defining integral. No literature novelty is claimed.

