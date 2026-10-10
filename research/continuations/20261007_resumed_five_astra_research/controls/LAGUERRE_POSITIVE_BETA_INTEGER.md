> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The positive beta bound is an exact short charge, and an integer originally

Coordinator derivation, 7 October2026. ACTIVE. This reuses A2turn13's exact
kernel and A2turn14's coefficient-sign/Rodrigues identities, which are currently
under independent proof review. It proves no favorable final gcd or irrationality.

Retain r=sum_(k=0)^n r_k x^k, W(y)=sum_(j=0)^d w_j y^j and



$$
R=\sum_{k=0}^n |r_k|
\frac{k!(3/4)_k}{(n-k+1/4)_{k+1}}.
$$



For every k<=n, integration by parts in the exact monomial kernel gives



$$
\int_0^1 y^{-3/4}\mathcal W_{n,k}(y)\,dy
=(-1)^k\frac{k!(3/4)_k}{(n-k+1/4)_{k+1}}.
$$



All endpoint terms vanish: at0 their power is n-k+1/4>0, at1 the repeated
factor has the required order. Since (-1)^(n-k)r_k>0,



$$
\boxed{R=(-1)^n\int_0^1 y^{-3/4}W(y)\,dy
=4(-1)^n\sum_{j=0}^d\frac{w_j}{4j+1}.}
$$



Thus the n+1-term positive beta sum equals an EXACT d+1-term signed rational
charge. Equality here is algebraic; it does not infer positivity of individual
w_j or pointwise W. The positivity comes from the original coefficient sign.

Set Lambda_R=lcm(1,5,9,...,4d+1). The already proved h! divisibility of every
w_j shows that if h>=4d+1, then R is a strictly positive INTEGER, divisible
by h!/Lambda_R. Every original n=2001b index satisfies that inequality.

Therefore, on the complete original family, all F,E,T,R are integers, ell=1,
and the remaining paid comparison is



$$
R/(2g)<q(e+\pi)-p<6005 R/g,
\qquad g=\gcd(|F|,|E+T|).
$$



These facts make possible sharper exact divisibility questions. For example,
if one could PROVE g divides C R for a fixed integer C, then the nonzero positive
integer C R/g would yield a primitive-error lower bound1/(2C), obstructing this
family. No such divisibility or uniform bound is asserted. Conversely a proof
that g/R tends to infinity on an infinite original set would establish the
required decay, conditional on the independently reviewed sign theorem.

The existing raw common factors h!/Lambda_R and h!/Lambda_B are lower divisors
of separate charges. They do not automatically divide E or identify the actual
all-prime final g. There is no transfer to the older prime29 producer or the
different compact even-contact determinant.
