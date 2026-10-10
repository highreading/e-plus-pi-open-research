> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of endpoint normalization and high-mode concentration

Date: 2026-09-13. Reviewer: audit_computations. Reviewed in full:
`raw_top_legendre_normalization.md` and
`raw_high_orthogonality_spectral_concentration.md`, including the
previously proved uniform interpolation input. No new degree sample
was run. Both proofs pass. Two quantitative consequences are derived
below without asserting endpoint noncancellation or coefficient bounds.

## 1. Reflected endpoint normalization

For the reflected polynomial
$P_n(t)=\sum_{j=0}^n B_{n,j}t^{n-j}/(n-j)!$, one has exactly
$P_n^{(r)}(0)=B_{n,n-r}$. Thus the functional
$\mathfrak b(P)=\sum_{r=0}^nP^{(r)}(0)$ is B_n(1), with no sign
change. The shifted Legendre derivative formula is



$$
J_l^{(r)}(0)=(-1)^{l-r}\frac{(l+r)!}{(l-r)!r!}.
$$



Reversing the derivative sum gives the stated sigma_l formula and
positive weights $z_l=\mathfrak b(\sqrt{2l+1}J_l)$. The consecutive
absolute summand ratio is



$$
\frac{l-s}{(s+1)(2l-s)}\le\frac1{2(s+1)},
$$



so $1/2\le\sigma_l\le1$ for l>=1. The claimed O(1/l) convergence
can be made uniform as follows: the relative discrepancy between
$(l)_{\underline s}/(2l)_{\underline s}$ and $2^{-s}$ is at most
$\min(1,s(s-1)/(2l))$ for s<=l, by bounding the deficit in a product
by the sum of its factor deficits. The corresponding weighted error
is summable against $2^{-s}/s!$, and the omitted tail has the same
bound. This proves the rate used in the adjacent-weight ratio.

The exact adjacent factorial quotient is
$1/[2(2l-1)]$. Combining it with the square-root factor and the
sigma ratio proves $z_{l-1}/z_l=1/(4l)+O(l^{-2})$, together with
the stated two Euclidean tail bounds. The l=0,1 values are harmless
fixed exceptions to the coarse ratio estimate, not asymptotic gaps.

Consequently the two-term top-mode relation follows by solving
$\sum_lz_la_l=1$ for a_n and applying Cauchy–Schwarz to the tail.
The mass lower bound applies after reflection as well, giving
$1/(z_n\|P_n\|_2)\le\exp(O(n))/(n!)^2$. The top-mode suppression
and the almost-orthogonality to the endpoint representer follow with
exactly the claimed scales. The angle estimate is explicitly
mass-dependent and does not imply an endpoint evaluation bound.

For the first B root sum, P_n'(0)/P_n(0) has the positive coefficient
ratio B_(n,n-1)/B_(n,n). Since J_l(0)=(-1)^l and
J_l'(0)=(-1)^(l-1)l(l+1), both the minus sign in the beta quotient and
the factor $(n-l)(n+l+1)$ in its centered version are correct. The
sufficient implication from the two endpoint-weight conditions is
valid and retains its noncancellation assumption.

## 2. Uniform inverse-Borel and imaginary-Legendre bounds

For $\phi_l=\sqrt{2l+1}J_l=\sum_j u_jx^j$, the exact coefficient
formula gives



$$
\sum_j|u_j|\le\sqrt{2l+1}\,8^l,
\quad \sup_{|u|\le1}|\mathcal B^{-1}\phi_l(iu)|
\le l!\sqrt{2l+1}\,8^l.
$$



The factor l! is essential; it is retained throughout the proof.
The raw normalization is exactly
$Q_k(iu)=i^k m_kP_k(u)$, where
$m_k=2^k/\binom{2k}{k}$. In the odd case, differentiation introduces
an additional i, so the relevant ratio in absolute value is
$|P_k'(0)|\le k$, with no missing m_k or k! factor. In the even
case the ratio is $|P_k(0)|\le1$.

Orthogonal expansion of the inverse-Borel polynomial along the
imaginary segment therefore gives



$$
\sum_{k=0}^l|a_{l,k}|
\le (l+1)^3\sqrt{2l+1}\,8^l l!
$$



in the normalized low Borel basis. The elementary sum used here is



$$
\sum_{k=0}^l(2k+1)\max(1,k)
=1+\frac{l(l+1)(4l+5)}6\le(l+1)^3.
$$



This is uniform for every 0<=l<=n. Intermediate complex coefficients
cause no problem: the final expansion is real, and the estimate only
uses their absolute values. The Legendre sup bound follows from the
displayed integral representation; no condition number of an
uncontrolled growing basis is imported.

## 3. Interpolation input, all-mode summation, and the exponent

The old interpolation estimate is uniform over every low k<=n in
both parities. Its least cancelled monomial degree is at least n-2,
including n=4, and its tail ratio is at most4/(n-1)^2<1/2. Hence the
constant $4n^2(2e^3)^n/n!$ applies at the boundaries used in the new
proof. No same-parity Chebyshev claim enters this argument.

Multiplying that estimate by the coefficient sum above approximates
each phi_l by the actual high span. Pairing with an arbitrary
high-orthogonal P and summing the squared bounds for l<=d introduces
exactly the extra factor sqrt(d+1). Thus the stated bound is



$$
\frac{\|\Pi_{\le d}P\|_2}{\|P\|_2}
\le4n^2(d+1)^{7/2}\sqrt{2d+1}\,
8^d(2e^3)^n\frac{d!}{n!}.
$$



For w=ceil(A n/log(n+1)), d=n-w, the logarithm of the factorial ratio
is -w log n+O(w^2/n+w/n). The polynomial factor contributes O(log n),
and the remaining exponential cost is at most
$(\log16+3)n$. Therefore every A>log16+3 gives the asserted uniform
exponential decay. A=8 is sufficient; the positive margin is
$8-(\log16+3)$. This estimate applies to every qualifying P after
dividing out its nonzero norm once.

The absolute endpoint-weighted tail is also correct. Its denominator
is at least $\|P\|_2$, whereas Cauchy–Schwarz bounds its numerator
by $(d+1)\|\Pi_{\le d}P\|_2$. This proves concentration of the
absolute weights, with no lower bound for their signed sum. Reflection
preserves the conclusion because it changes Legendre coefficients
only by signs and commutes with the spectral projections.

## 4. A stronger centered norm criterion on the actual high-orthogonal inputs

This is an additional rigorous consequence of the reviewed theorem.
Let $\mathscr L=-[t(1-t)\partial_t]'$, so
$\mathscr L\phi_l=l(l+1)\phi_l$. Put N=n(n+1), choose the above
w_n, and let epsilon_n denote the exponential bound for the low
projection through n-w_n. Then, for every high-orthogonal P,



$$
\boxed{\| (\mathscr L-N)P\|_2
\le\{w_n(2n+1)+N\epsilon_n\}\|P\|_2.}
\tag{A}
$$



Indeed on the top band the multiplier difference is at most
w_n(2n+1), and on the low band it is at most N. Orthogonality of the
modes gives an even slightly sharper Euclidean combination of these
two bounds; their sum is enough for (A).

Use the exact centered integral operator from
`raw_hp_integral_transfer_operator.md`, equation (11), normalized by
Q3:



$$
\overline{\mathcal D}_n=
\Gamma_n(\mathscr L-N)
+\delta_n\{t(t-1)\partial_t+n(1-2t)\}
+\overline W_0+\sum_{k=1}^5\overline V_kJ^k.
$$



The old weighted derivative estimate gives



$$
\|\{t(t-1)\partial_t+n(1-2t)\}P\|_2
\le(\sqrt N/2+n)\|P\|_2.
$$



Hence a sufficient one-step bound on the actual high-orthogonal input
is



$$
\Lambda_n\left[
|\Gamma_n|\{w_n(2n+1)+N\epsilon_n\}
+|\delta_n|(\sqrt N/2+n)
+\|\overline W_0\|_\infty
+\sum_{k=1}^5\frac{\|\overline V_k\|_\infty}{k!}
\right]\le C(n+1).
\tag{B}
$$



In particular it suffices that the inverse is uniformly bounded,
$|\Gamma_n|=O(1/w_n)=O(\log n/n)$, $|\delta_n|=O(1)$, and the
combined W0/Volterra norm is O(n). If these hold for all sufficiently
large cubic indices and the remaining indices are also controlled,
iteration yields the same factorial mass upper bound. The logarithmic
relaxation of the Gamma condition uses the exact centered constant
term; it does not follow by dropping V0 from the uncentered formula.

This is a bound for the actual high-orthogonal inputs. It is not a
uniform bound on the full degree-n polynomial space. None of its
coefficient or inverse hypotheses is proved here.

## 5. A quantitative statement of the remaining endpoint obstruction

For the reflected actual polynomial let



$$
L_n=\sum_{l=0}^n\sqrt{2l+1}|a_l|,
\quad \kappa_n=|P_n(0)|/L_n,
\quad \eta_n=\frac{\sum_{l\le n-w_n}\sqrt{2l+1}|a_l|}{L_n}.
$$



When B has degree n, kappa is positive. The reviewed concentration
theorem proves eta_n<=poly(n)epsilon_n. The exact beta formula and
the split into the top band and its complement give



$$
\boxed{\left|\frac{\beta_n}{n^2}+1+\frac1n\right|
\le\frac1{\kappa_n}
\left[\frac{w_n(2n+1)}{n^2}+
\left(1+\frac1n\right)\eta_n\right].}
\tag{C}
$$



Thus the additional noncancellation condition
$\kappa_n\log n\longrightarrow\infty$ would imply
$\beta_n/n^2\to-1$. A fixed positive lower bound for kappa is more
than enough. No such lower bound is supplied by L2 concentration, by
the normalization-functional angle, or by the factorial mass estimates.
Formula (C) makes the missing signed-endpoint estimate explicit.

The audits and consequences above establish concentration and its
conditional uses only. They do not establish root bounds, endpoint
noncancellation, an accessory limit, or primitive shrinking.
