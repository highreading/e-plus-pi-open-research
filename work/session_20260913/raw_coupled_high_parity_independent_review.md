> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the coupled high-parity Jacobi system

Date: 2026-09-13. Reviewer: audit_results.

Reviewed in full: raw_coupled_high_parity_jacobi_system.md, including
the corrected one-dimensional exception in Section 5. The original
parity identities are from the independently reviewed
raw_mixed_parity_volterra_and_darboux.md; the final sufficient
zero-count implication is the previously reviewed singular-endpoint
argument in raw_weaker_oscillation_and_spectral_rank.md.

**Verdict: PASS after one minor scope clarification.** The exact matrix
system, actual high-block embedding, uniform all-mode frequency
comparison, endpoint residues and polynomial cancellation all hold.
No numerical controls or new canonical degrees were constructed.
No mixed zero bound or new high-row rank conclusion follows from this
audit alone.

## 1. Elimination and symmetrization

Differentiating the first parity identity twice gives


$$
E_{m+1}''-E_m''=(4m+3)O_m'.
$$


Substitution of the second identity and of
$O_{m-1}'=(E_m''-E_{m-1}'')/(4m-1)$ gives precisely (1).
The two simplifications in (2) follow from


$$
4m^2(4m+3)-(2m+1)^2(4m-1)=1,\qquad
(4m+3)(4m+1)=4(2m+1)^2-1.
$$


They are valid for every stated $m\ge1$.

Multiplying the negative of the second-derivative part of (1) by
$\rho_m$ yields the positive diagonal of $H$. The equality
$\rho_m\gamma_m=\rho_{m-1}$, for $m>a$, makes its off-diagonal
entries symmetric. The two omitted terms have coefficients
$\rho_a\gamma_a=\gamma_a$ and $\rho_b$, giving exactly $B\beta''$
with the signs in (3).

Expansion of (4) reproduces every diagonal and off-diagonal coefficient,
including the case $r=1$, when the two boundary terms add. All its
weights are strictly positive, so $H$ is positive definite; $M$
is positive diagonal. The initial values follow from evenness and
$F_{2m}(0)=Q_{2m}(0)$.

## 2. The actual high-index constraints

For $n=2s+1$, the high indices $2s+2,\ldots,4s+1$ have even
members $E_{s+1},\ldots,E_{2s}$, and odd members
$O_{s+1},\ldots,O_{2s}$. Thus $a=s+1,b=2s+1$, with the last
even coefficient omitted. Equation (5) maps these odd members to all
consecutive differences on the $r=s+1$ derivative coordinates.
Those differences span exactly $\sum q_m=0$.

For $n=2s$, the high indices $2s+1,\ldots,4s-1$ have even
members $E_{s+1},\ldots,E_{2s-1}$, and odd members
$O_s,\ldots,O_{2s-1}$. Thus both endpoint even coefficients are
omitted, and the same derivative hyperplane occurs.

The coordinates really are independent: the $E_m$ have different
even degrees $2m$, and the $E_m'$, since $a\ge1$, have different
odd degrees $2m-1$. The even and odd spaces have zero intersection.
The two dimensions are therefore $2r-2=n-1$ and $2r-3=n-1$,
respectively. In particular $n=2$ is included, with no even member
and one odd difference. All these actual blocks have $r\ge2$.

## 3. Uniformity of the all-mode estimates

Put $t_m=((2m+1)^2(4m-1))^{-1}$. Then
$\gamma_m=1+t_m$ and


$$
e^{-S_a}\le
\rho_m=\prod_{k=a+1}^{m}(1+t_k)^{-1}\le1,
\qquad 1\le\gamma_a\le e^{S_a}.
$$


Every edge and endpoint weight in (4) lies in the stated common
interval. Also


$$
\sum_{m=a}^{\infty}t_m
\le \frac1{12a^3}+\int_a^\infty\frac{dt}{12t^3}
\le\frac1{8a^2}.
$$


This proves (8), without dependence on $b$ or the number of modes.

For clarity, write $\mu_j=4\sin^2(j\pi/(2(r+1)))$, in increasing
order, and let $\lambda_j$ be the increasing generalized eigenvalues
of $Hv=\lambda Mv$. Generalized min--max applied to (8) gives


$$
\frac{e^{-2S_a}\mu_j}{4}\le\lambda_j
\le\frac{e^{2S_a}\mu_j}{4-(2a+1)^{-2}}.
$$


Since $\omega_j=\lambda_j^{-1/2}$, this is exactly (9).
The tridiagonal matrix $M^{-1/2}HM^{-1/2}$ has all subdiagonals
strictly negative and hence simple eigenvalues (also immediate from
the eigenvector recurrence and the one-dimensional first-coordinate
initial datum). Thus the strict ordering used in the note is justified.
The relative $O(a^{-2})$ bound is simultaneous in every $j,r$;
it does not result from an asymptotic taken at fixed mode index.

## 4. Endpoint normalizations, poles and signs

Let $V$ have columns $v_j$, normalized by $V^THV=I$. Then
$V^TMV=\operatorname{diag}(\omega_j^2)$, and direct matrix inversion
gives


$$
(M+\tau H)^{-1}
=V\operatorname{diag}((\tau+\omega_j^2)^{-1})V^T.
$$


Consequently (11) has the exact residue vectors $B^Tv_j$; there is
no missing mass or frequency factor.

Under the positive diagonal change from $v_j$ to an eigenvector of
$J=M^{-1/2}HM^{-1/2}$, neither endpoint signs nor endpoint
nonvanishing changes. A zero endpoint of an eigenvector of an
irreducible tridiagonal matrix forces all its coordinates to vanish.
Thus both coordinates of every residue vector are nonzero.

For a check of the sign convention, if the off-diagonal magnitudes of
$J$ are $c_1,\ldots,c_{r-1}>0$, then


$$
[(J-tI)^{-1}]_{1r}=\frac{\prod c_i}{\prod_i(\lambda_i-t)}.
$$


Its residue at $t=\lambda_j$ has sign $(-1)^j$. The spectral
term is $u_j(1)u_j(r)/(\lambda_j-t)$, whose residue is the negative
of its numerator. Hence the endpoint product has sign
$(-1)^{j-1}$, as claimed. The frequency order is the reciprocal of
the increasing $\lambda_j$ order, exactly as in (9).

There is one global edge case: when $r=1$, $B$ has rank one and
the sole cross residue is positive. The author has explicitly
restricted the alternating-sign obstruction to a positive scalar
cross measure to $r\ge2$, and recorded the $r=1$ exception.
All actual high blocks satisfy that restriction. For $r\ge2$, the
distinct-pole cross residues have both signs, so uniqueness of scalar
Stieltjes residues excludes a positive scalar representing measure.
The matrix-valued measure remains positive semidefinite in every case.

## 5. Finite polynomial cancellation

Equation (3) is equivalent to


$$
Evec=M^{-1}B\beta''-M^{-1}HEvec''.
$$


All matrices are constant in the polynomial argument. Iterating $b+1$
times leaves
$(-M^{-1}H)^{b+1}Evec^{(2b+2)}=0$, because every component has degree
at most $2b$. This proves (12), including the multiplication order.
The highest forcing component has degree $2b+2$, so its derivative
in the last displayed summand need not vanish.

The representation therefore retains the special polynomial solution
and its exact initial values. The modal representation of an arbitrary
forced solution would also contain homogeneous oscillations; they
cannot be independently added to this actual polynomial family.
The zero-count target is properly confined to the constrained
observables (6),(7).

## 6. Cross-check of the parent's additional Jacobi identification

This is an algebraic normalization check, not an audit of any later
spectral extension. Let


$$
a_j=\frac{j}{\sqrt{(2j-1)(2j+1)}}.
$$


The entries above give exactly


$$
J_{mm}=\frac{1+\gamma_m}{\delta_m}
=a_{2m}^2+a_{2m+1}^2,\qquad
J_{m,m+1}=-\sqrt{\frac{\gamma_{m+1}}{\delta_m\delta_{m+1}}}
=-a_{2m+1}a_{2m+2}.
$$


These equalities follow by cancelling the displayed linear factors;
the positive square roots fix the off-diagonal sign.
Thus $J$ is the alternating-sign gauge of the compression of
multiplication by $u^2$ to the orthonormal ordinary Legendre degrees
$2a,2a+2,\ldots,2b$. In particular it is the compression of
multiplication by $u^2$, not the square of the compressed
multiplication-by-$u$ operator. The distinction preserves both
diagonal boundary contributions.

Any further quadrature interpretation or zero-count consequence
requires its own proof. No such consequence was needed for the passing
audit above.
