> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact modal signs: the full sign cone fails, while quantitative noncancellation remains open

Date: 2026-09-13. Only saved exact polynomials are used. No new degree
was constructed, no asymptotic fit was made, and no sign pattern or
uniform lower bound is inferred from the finite data.

## 1. Inputs and conventions

The prescribed rows n=2,4,8,16 were read from
`raw_accessory_scaling_probe.json`; their B polynomials were divided
by their saved exact B(1). The already available n=3 row was read
from `raw_rational_transfer_checks.json`, and n=5 from
`raw_dual_mass_independent_checks.json`. The n=4 B coefficients in the
last file agree exactly with the normalized scaling-probe input.
No linear system or degree update was run.

For each row define the reflected polynomial and its ordinary shifted
Legendre expansion by



$$
P_n(t)=\sum_{j=0}^n B_{n,j}\frac{t^{n-j}}{(n-j)!}
=\sum_{l=0}^n p_{n,l}J_l(t),\qquad J_l(t)=P_l(2t-1).
\tag{1}
$$



The p's here multiply unnormalized J_l, not the orthonormal basis.
The endpoint weights and cancellation ratio are



$$
\omega_{n,l}=(-1)^lp_{n,l},\qquad
S_n=P_n(0)=B_{n,n}=\sum_l\omega_{n,l},\qquad
\kappa_n=\frac{|S_n|}{\sum_l|p_{n,l}|}.
\tag{2}
$$



The full sign-cone assertion would say that every nonzero omega has
the same sign as S. It would imply kappa=1. A positive lower bound
for kappa is substantially weaker and permits opposite signs.

## 2. Exact finite outcome

Every sign in the table is an exact rational sign, listed in increasing
order l=0,...,n. The decimal kappa values are rounded presentations of
exact rational numbers retained in the certificate.

| n | signs of p_(n,l) | signs of omega_(n,l) | sign of S_n | kappa_n |
|---:|---|---|:---:|---:|
| 2 | --+ | -++ | + | 0.543925233645 |
| 3 | ++-+ | +--- | - | 0.831211910573 |
| 4 | ---+- | -+--- | - | 0.716817855250 |
| 5 | ++--+- | +--+++ | + | 0.934889330844 |
| 8 | ---+--++- | -+---++-- | - | 0.920530305821 |
| 16 | ---++-++--++--++- | -+--+++--++--++-- | - | 0.958507659770 |

The respective sets of indices whose endpoint weight has the opposite
sign to S_n are



$$
\{0\},\quad\{0\},\quad\{1\},\quad\{1,2\},\quad
\{1,5,6\},\quad\{1,4,5,6,9,10,13,14\}.
$$



Thus the all-degree full sign cone is false. At n=16, l=14 has the
opposite endpoint sign while l=15,16 share the endpoint sign, so a
claim that the top three modes always lie in one such cone is also
false. These finite counterexamples do not disprove a theorem with
an unspecified eventual threshold or a more restricted subsequence.

The n=2 counterexample is especially small and independently readable:



$$
P_2(t)=\frac{3579t^2-8168t+2037}{1027}
=\frac{-1708J_0(t)-4589J_1(t)+1193J_2(t)}{2054}.
$$



Its endpoint weights are (-1708,4589,1193)/2054, with positive sum,
and $\kappa_2=291/535$. Thus no numerical rounding is involved in
the sign-cone obstruction.

All six tested kappas exceed 1/2 exactly. This is compatible with a
weaker uniform positive bound, but it does not prove one. In particular
the samples establish neither convergence to 1 nor eventual monotonicity.

## 3. Exact Rodrigues formula for every modal coefficient

The shifted Rodrigues identity is



$$
J_l(t)=\frac1{l!}\frac{d^l}{dt^l}[t^l(t-1)^l].
$$



The boundary terms vanish in l integrations by parts, so



$$
\boxed{p_{n,l}=
\frac{2l+1}{l!}\int_0^1t^l(1-t)^lP_n^{(l)}(t)\,dt.}
\tag{3}
$$



Expanding P_n and evaluating the beta integral gives the exact rational
linear functional



$$
\boxed{p_{n,l}=(2l+1)\sum_{j=0}^{n-l}
B_{n,j}\frac{(n-j)!}{(n-j-l)!(n-j+l+1)!}.}
\tag{4}
$$



All weights in (4) are positive. The B coefficients are not assumed
to have a suitable sign pattern, so this positivity alone does not
prove a modal sign assertion. Formula (3) has the same limitation:
the positive beta weight does not control the sign of the derivative
being integrated.

## 4. A positive triangular transform within parity

There is a further exact representation that may be useful for an
actual sign or signed-mass estimate. Define the centered exponential
coefficients



$$
c_{n,r}=[z^r](B_n(z)e^{z/2}).
$$



Then



$$
\boxed{p_{n,l}=\frac{l!}{(2l)!}
\sum_{r=0}^{\lfloor(n-l)/2\rfloor}
\frac{c_{n,n-l-2r}}
{16^r r!(l+3/2)_{\overline r}}.}
\tag{5}
$$



The rising factorial is positive. Thus this is an explicit positive
triangular transform using only one parity of the centered Taylor
coefficients.

To derive it without importing a sign theorem, write (4) as the
coefficient of B_n(z) times the exponential generating function of a
beta integral:



$$
p_{n,l}=\frac{2l+1}{l!}[z^{n-l}]
B_n(z)\int_0^1e^{zt}t^l(1-t)^l\,dt.
$$



The beta density is symmetric about 1/2. Its odd centered moments vanish,
and its normalized even moments are



$$
\mathbb E[(t-1/2)^{2r}]
=\frac1{4^r}\frac{(1/2)_{\overline r}}{(l+3/2)_{\overline r}}.
$$



Using $(2r)!=4^r r!(1/2)_{\overline r}$ gives (5). Equivalently,
the generating function is the usual Kummer/zero-F-one identity, but
the beta-moment calculation proves exactly what is needed here.

A concrete possible next lemma would bound the opposite-sign part of
the sums in (5), rather than assert that all their terms have one sign.
The observed modal counterexamples prevent importing such a universal
sign assertion without proving a weaker, quantitative statement.

## 5. Canonical bordered determinants and the precise weaker target

Use the actual homogeneous coefficient matrix $\mathcal H_n$ from
`raw_transfer_leading_minor_criterion.md`: the Taylor equations through
3n and the matching equation C(1)-4B(1)=0. For a linear functional ell,
write



$$
T_n[\ell]=\det\begin{pmatrix}\mathcal H_n\\\ell\end{pmatrix},
\qquad E_n=T_n[B(1)]\ne0.
$$



Let ell_(n,l) be the B-coefficient functional on the right of (4), and
let ell_top extract B_(n,n). Then exactly



$$
p_{n,l}=\frac{T_n[\ell_{n,l}]}{E_n},\quad
S_n=\frac{T_n[\ell_{\mathrm{top}}]}{E_n},\quad
\boxed{\kappa_n=
\frac{|T_n[\ell_{\mathrm{top}}]|}
{\sum_{l=0}^n|T_n[\ell_{n,l}]|}.}
\tag{6}
$$



The identity
$T_n[\ell_{\mathrm{top}}]=\sum_l(-1)^lT_n[\ell_{n,l}]$
is an exact last-row linearity identity. Formula (6) removes every
arbitrary common row scaling. Its numerator may still be zero at a
degree-defective index; no all-index nonvanishing assertion is made
here. All six sampled numerators are nonzero.

When S_n is nonzero, split the absolute endpoint-weighted mass into
W_plus, whose weights have the sign of S_n, and W_minus, whose weights
have the opposite sign. Then



$$
\kappa_n=\frac{W_+-W_-}{W_++W_-}
=1-\frac{2W_-}{W_++W_-}.
\tag{7}
$$



For a fixed c in (0,1), the bound kappa_n>=c is equivalent to



$$
\boxed{W_-\le\frac{1-c}{1+c}W_+.}
\tag{8}
$$



This signed-mass domination is a viable weaker target after the full
sign cone fails. In determinant form it is a comparison of the
oppositely signed bordered minors, not a claim that every such minor
has the same sign. The already proved high-mode concentration removes
an exponentially small absolute tail outside a sublinear top band;
it does not prove (8) inside that band.

The even weaker condition kappa_n log n->infinity would suffice for
the conditional first-root-sum limit derived in
`raw_legendre_concentration_independent_review.md`, equation (C).
Neither that condition nor (8) follows from the finite table.

## 6. Reproducibility and verification

`probe_raw_legendre_endpoint_signs.py` only reads the named saved files.
It computes (4) with exact fractions, reconstructs every coefficient
of P_n from the resulting J_l expansion, verifies the endpoint sum,
and independently checks the positive triangular formula (5). The
two saved n=4 sources agree exactly. It stores every rational modal
coefficient, endpoint weight, kappa, and input polynomial in
`raw_legendre_endpoint_sign_probe.json`.

All checks pass. The rigorous outcome is an exact finite counterexample
to the strong all-degree sign cone and the all-index formulas (3)–(8).
An all-index noncancellation estimate remains open.

Independent verification: audit_results checked the Rodrigues and
finite coefficient formulas, the exact beta normalization and the
16^r factor in the positive parity transform, the readable n=2
counterexample and kappa=291/535, and the bordered determinant
conventions. No substantive gap was found and no further degree was
sampled.
