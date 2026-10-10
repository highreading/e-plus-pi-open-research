> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the shifted spectral-branch positivity theorem

Date: 2026-09-13. Reviewer: audit_sources. Status: **PASS** for the
all-index theorem and its logarithmic-derivative and node-ratio
consequences. No correction is required.

Reviewed in full: `raw_branch_shifted_positivity_theorem.md` and
`raw_spectral_branch_generating_function.md`. Independently checked the
normalization against §7 of `raw_boundary_free_moment_intertwiner.md`
and the polynomial interpretation in
`raw_positive_two_measure_reduction.md`. The finite diagnostic through
index 12 is not an input to this review or to the proof.

## 1. The exact normalized row and both seeds

The original symmetric row is



$$
\xi p_k=a_{k+1}a_{k+2}p_{k+2}-a_{k+1}p_{k+1}
 +(a_k^2+a_{k+1}^2-k(k+1))p_k-a_kp_{k-1}
 +a_ka_{k-1}p_{k-2},
\quad a_k=\frac{k^2}{\sqrt{(2k-1)(2k+1)}}.
$$



Substituting either (p_k=\sqrt{2k+1}\,r_k) or
(p_k=\sqrt{2k+1}\,r_k/\sqrt3) gives exactly the displayed
(U_k,u_k,v_k,w_k,d_k) in the reviewed theorem. In particular, both
the negative (w_k r_{k-2}) term and the row-dependent square-root
factors have been retained. The initial pairs become exactly
((1,1/2)) and ((0,1)). The degree caps follow from the previously
proved polynomial decomposition and do not require coefficient
positivity.

These are the plus-convention branches attached to (F_k(x)). The
reflection of the actual unknown polynomial changes its odd high-row
sign as recorded in the convention bridge; it does not change this
definition of the branch polynomials.

## 2. Elimination of the negative term

I independently simplified the two rational identities



$$
d_k+\frac{k w_k}{k-1}+\frac{(k+1)U_k}{k+2}=1,
\qquad \frac{k u_k}{k+1}+v_k=k
$$



for symbolic (k), and separately checked the resulting multipliers
(A_k,B_k,C_k). All five rational residuals vanish identically.
These identities apply to the derivation for (k\ge2); cancellation
of the algebraic factor (k-1) is not used as a substitute for a
small-index argument.

For arbitrary initial symbols (r_0,r_1), the original first two
rows give directly



$$
D_2=\frac32 r_1+\frac32(\xi-1)r_0,
\qquad
D_3=\frac56D_2+\frac54\bigl((\xi-1)r_1+r_0\bigr).
$$



Thus the same (D)-recurrence holds at (k=0,1), with
(D_0=0,D_1=r_1,r_{-1}=0), without evaluating a division by zero.
These two identities were also checked symbolically with arbitrary
seeds, not merely with the two numerical seed pairs.

For (k\ge2), (B_k>0); (B_0=B_1=0); and (A_k,C_k>0) for all
(k\ge0). Consequently every term in the new recurrence preserves
coefficient nonnegativity in (y=\xi-1). Recovering



$$
r_{k+2}=\frac{D_{k+2}+(k+1)r_k}{k+2}
$$



closes a simultaneous induction. Both seeds have (D_1>0) as a
constant, so the (A_kD_{k+1}) term supplies a positive constant
coefficient for every later (D), and hence for every (r_k) with
(k\ge1). This also handles strict positivity at (y=0), which
would not follow merely from nonzeroness and coefficient
nonnegativity. The exceptional zero polynomial (r_0^{(1)}) is
explicitly excluded from all quotients and logarithms.

## 3. The quantitative consequences and their quantifiers

For a nonzero degree-(d) polynomial
(r(\xi)=\sum_{j=0}^d a_j(\xi-1)^j), (a_j\ge0), and
(\xi>1), the quantity ((\xi-1)r'/r) is the weighted average of
the integers (0,\ldots,d). This proves exactly



$$
0\le r'(\xi)/r(\xi)\le d/(\xi-1).
$$



Its integral proves the branch ratio bound for (1<x\le y). At the
actual spectral nodes, the previously proved min-max enclosure



$$
\ell(\ell+1)+3/4\le\xi_\ell\le\ell(\ell+1)+1
$$



gives the theorem's denominator
(\ell(\ell+1)-1/4>0) for every $\ell\ge1$. The nodes used in the
ratio are strictly ordered. The formula is valid for evaluating
either branch at either parity of node; such an evaluation is a
polynomial evaluation, not an assertion that its seed amplitude is
the physical amplitude at the other parity.

For fixed positive integer (h),



$$
\log\frac{(\ell+h)(\ell+h+1)}{\ell(\ell+1)-1/4}
 =\frac{2h}{\ell}+O_h(\ell^{-2}).
$$



Combining this with (d_{k,\sigma}\le k/2) proves the stated
(\limsup\le e^{h\tau}) when (k/\ell\to\tau<\infty), and the
ratio tends to one if (k/\ell\to0). For (k\le C\ell), the
logarithmic derivative on the entire corresponding interval is
(O_C(1/\ell)). These statements allow (k) to grow with $\ell$;
no interchange of a spectral sum with a growing index is involved.

The subsequently added complex corollaries (11)–(12) also pass. For
degree (d\ge1), multiplying the positive-coefficient sum at
(1+Re^{i\theta}) by (e^{-id\theta/2}) places all its summands in
the sector of half-angle (d|\theta|/2<\pi/2). Taking real parts
proves (11). In the disk $|z-x|\le(x-1)/(4d)$, the elementary
geometry gives $|\arg(z-1)|\le\arcsin(1/(4d))\le1/(2d)$.
The radial ratio lies between $1-1/(4d)$ and $1+1/(4d)$.
Bernoulli's inequality and the exponential upper bound then give
exactly $(3/4)\cos(1/4)\le |r(z)|/r(x)\le e^{1/4}$.
The restriction (d\ge1) is explicit; a nonzero constant branch
has the corresponding trivial global comparison. This proves a
zero-free neighborhood for an individual branch, with no implication
for zeros of mixed determinants.

## 4. Scope retained

The proof establishes nonnegative coefficients in **(\xi-1)**.
It does not prove nonnegative coefficients in (\xi), real-rootedness,
positivity of a mixed determinant, or a cofactor-conditioning bound.
The stated first three even monic branch polynomials do force a
negative scalar Favard coefficient (-131/180), so that particular
positive scalar-orthogonality shortcut is unavailable.

The scalar ratio estimate is suitable input for a separately proved
relative truncation bound. It cannot by itself justify dropping the
spectral tail in the actual mixed high constraints or excluding
cancellation between the two branch contributions. No irrationality
conclusion follows from this auxiliary theorem alone.
