> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Leading transfer coefficients as exact two-by-two minor ratios

Date: 2026-09-13. Root proposed the leading minor formula; this note
verifies its sign and normalization, derives the next coefficient, and
isolates the two precise minor bounds needed by the new norm criterion.
No further degree sample is taken, and no bound on these ratios is claimed.

## 1. Actual normalization and notation

Use the actual canonical raw triples



$$
R_n=A_n+B_ne^z+C_n\arctan z=O(z^{3n+1}),\quad
B_n(1)=1,\quad C_n(1)=4.
\tag{1}
$$



Assume only that the current accessory polynomial Q_n has degree 3.
It may have repeated roots or vanish at any fixed singular point. The
next index need not have accessory degree 3. Write the first transfer
row from `raw_hp_rational_degree_transfer.md` as



$$
S_n=\frac{N_0+N_1\partial_z+N_2\partial_z^2}{Q_n},\qquad
\deg(N_0,N_1,N_2)\le(5,6,6),\quad \lambda_n=[z^3]Q_n.
$$



The two normalized coefficients relevant to
`raw_hp_integral_transfer_operator.md` are



$$
\Gamma_n=\frac{[z^6]N_2}{\lambda_n},\qquad
\delta_n=\frac{[z^5]N_2}{\lambda_n}.
\tag{2}
$$



Gamma here is a transfer coefficient, unrelated to the low Laurent
coefficient called gamma in `raw_accessory_scaling_and_compactness.md`.
Let



$$
\begin{array}{lll}
a=[z^n]A_n,&a_1=[z^{n-1}]A_n,&
b=[z^n]B_n,\quad b_1=[z^{n-1}]B_n,\\
c=[z^n]C_n,&c_1=[z^{n-1}]C_n,\\
d=[z^{n+1}]A_{n+1},&d_1=[z^n]A_{n+1},\\
f=[z^{n+1}]C_{n+1},&f_1=[z^n]C_{n+1}.
\end{array}
$$



Set



$$
\Xi_n=ac_1-a_1c+c^2,\qquad \beta_n=b_1/b,
\tag{3}
$$





$$
m_n^{(0)}=af-cd,\qquad
m_n^{(1)}=af_1+a_1f-cd_1-c_1d.
\tag{4}
$$



The cubic degree ledger ensures b is nonzero. Equation (5) below then
ensures Xi is nonzero, even if c=0 or the next leading coefficients
vanish. No division by c,d,f, or the mixed minor m0 is used.

## 2. Exact coefficient formulas

The identities are



$$
\boxed{\lambda_n=b\Xi_n,\qquad
[z^6]N_2=b m_n^{(0)},\qquad
[z^5]N_2=b m_n^{(1)}+b_1m_n^{(0)}.}
\tag{5}
$$



Consequently root's proposed leading sign is correct:



$$
\boxed{\Gamma_n=
\frac{A_{n,n}C_{n+1,n+1}-C_{n,n}A_{n+1,n+1}}{\Xi_n},}
\tag{6}
$$





$$
\boxed{\delta_n=
\frac{m_n^{(1)}+\beta_n m_n^{(0)}}{\Xi_n}.}
\tag{7}
$$



These are coefficients of the numerator divided by Q's leading
coefficient. They should not be confused with the first two coefficients
of the Laurent expansion of N2/Q: that expansion is



$$
\frac{N_2}{Q_n}=\Gamma_n z^3+
(\delta_n-q_2\Gamma_n)z^2+O(z),\qquad
q_2=[z^2](Q_n/\lambda_n).
\tag{8}
$$



### Proof of the leading denominator

At infinity subtract a fixed branch constant of arctangent, and put



$$
H_n=A_n-C_n\arctan(1/z).
$$



This replaces the R column by a constant linear combination of the
original columns. Its first relative coefficients and those of C are



$$
H_n=z^n\bigl(a+(a_1-c)/z+O(z^{-2})\bigr),\quad
C_n=z^n\bigl(c+c_1/z+O(z^{-2})\bigr).
$$



The first nonzero coefficient of the Wronskian of
$(H_n,e^zB_n,C_n)$ is
$b(ac_1-a_1c+c^2)e^zz^{3n-2}$. This follows either by expanding its
three rows, or by taking the wedge of the displayed two coefficient
rows. Comparing with
$e^zz^{3n-1}Q_n/(1+z^2)^2$ proves the first identity in (5).

### Proof of the two numerator coefficients

Cramer's rule for entry (0,2) replaces old derivative row 2 by new row
0, leaving the ordered rows old0, old1, new0. In the polynomial gauge
K from the rational-transfer note its determinant is



$$
(1+z^2)^2 M(z)-(1+z^2)C_n(B_nC_{n+1}-C_nB_{n+1}),
\tag{9}
$$



where



$$
M=\det\begin{pmatrix}
A_n&B_n&C_n\\
A_n'&B_n+B_n'&C_n'\\
A_{n+1}&B_{n+1}&C_{n+1}
\end{pmatrix}.
$$



The second term in (9) has degree at most 3n+3, so it contributes
nothing to the two coefficients of degrees 3n+5 and 3n+4. Expanding M
in its middle row gives



$$
\begin{aligned}
M={}&(B_n+B_n')(A_nC_{n+1}-C_nA_{n+1})\\
&+B_n(-A_n'C_{n+1}+C_n'A_{n+1})\\
&+B_{n+1}(-A_nC_n'+C_nA_n').
\end{aligned}
\tag{10}
$$



The middle-row, middle-column cofactor has **positive** sign. The first
line contributes b m0 at degree 3n+1 and b m1+(b1+nb)m0 at degree 3n.
The second line contributes -nb m0 at degree 3n, cancelling that extra
derivative term. The last line has degree at most 3n-1: its apparent
highest A,C coefficient cancels. Therefore



$$
[z^{3n+1}]M=bm_0,\qquad [z^{3n}]M=bm_1+b_1m_0.
$$



The factor $(1+z^2)^2$ contributes no relative z^-1 correction.
Dividing (9) by the exact origin factor z^(3n-1) proves the other two
identities in (5). The proof includes all degree drops mentioned above.

## 3. A two-dimensional leading connection

For row vectors in two dimensions write $v\wedge w=\det(v;w)$.
Define



$$
v_n=(a,c),\quad w_n=(a_1-c,c_1),\qquad
v_{n+1}=(d,f),\quad w_{n+1}=(d_1-f,f_1).
\tag{11}
$$



They are the first two relative Laurent coefficient rows of the pair
$(H_n,C_n)$, with the reference degree raised from n to n+1. Then



$$
\Xi_n=v_n\wedge w_n,\quad
m_n^{(0)}=v_n\wedge v_{n+1},\quad
m_n^{(1)}=w_n\wedge v_{n+1}+v_n\wedge w_{n+1}.
\tag{12}
$$



Since Xi is nonzero, the actual two-by-two matrix



$$
\mathsf T_n^\infty=
\begin{pmatrix}v_{n+1}\\w_{n+1}\end{pmatrix}
\begin{pmatrix}v_n\\w_n\end{pmatrix}^{-1}
=\begin{pmatrix}\sigma_n&\Gamma_n\\\rho_n&\tau_n\end{pmatrix}
\tag{13}
$$



is well defined, even if the next matrix has rank below two. Equations
(6)–(7) become



$$
\boxed{\delta_n=\tau_n-\sigma_n+\beta_n\Gamma_n.}
\tag{14}
$$



When the next index is also cubic, this leading connection has the
exact determinant



$$
\det\mathsf T_n^\infty=
\frac{\Xi_{n+1}}{\Xi_n}=
\frac{\lambda_{n+1}}{\lambda_n}
\frac{B_{n,n}}{B_{n+1,n+1}}.
$$



This agrees with the full transfer determinant: the exponential line
contributes the additional leading factor
z B_(n+1,n+1)/B_(n,n), and the two Laurent reference degrees each rise
by one. Their product is z^3 lambda_(n+1)/lambda_n. If the next index
has a degree defect, (13) still exists but this nonzero determinant
description is not assumed.

Thus Gamma is exactly the off-diagonal coefficient that mixes the old
second Laurent coefficient into the next leading coefficient. Delta
is a particular centered difference of diagonal coefficients, not an
arbitrary raw coefficient of this two-dimensional matrix.

This representation makes the required cancellation explicit. Even if
$\Gamma_n=O(1/n)$ and $\beta_n=O(n^2)$, the separate term
beta Gamma can have order n. Bounded delta requires its cancellation
against tau-sigma. Separate O(n) bounds for those terms do not suffice.

## 4. Canonical bordered determinant formulas, with the endpoint factor retained

For a normalization-independent specification of the raw linear
algebra, let $\mathcal H_n$ be the matrix of the following homogeneous equations
in the 3n+3 coefficient variables of (A,B,C): Taylor coefficients
0,...,3n of A+B exp+C arctan vanish, and C(1)-4B(1)=0. It has 3n+2
rows and a one-dimensional kernel. For any coefficient functional ell
define the bordered determinant



$$
T_n[\ell]=\det\begin{pmatrix}\mathcal H_n\\\ell\end{pmatrix},\qquad
E_n=T_n[\ell_B],\quad \ell_B(A,B,C)=B(1).
\tag{15}
$$



The established actual endpoint-normality theorem gives E_n nonzero.
The signed maximal minors of $\mathcal H_n$ form a kernel vector, so every
canonical coefficient is exactly



$$
\ell(A_n,B_n,C_n)=T_n[\ell]/E_n.
\tag{16}
$$



Use tildes for leading coefficients taken from these bordered
determinants before dividing by E_n. Define Xi-tilde and m0-tilde,
m1-tilde by the same quadratic or cross-index formulas (3)–(4), with
the respective current and next tilded coefficients. Then



$$
\boxed{\Gamma_n=
\frac{E_n}{E_{n+1}}\frac{\widetilde m_n^{(0)}}{\widetilde\Xi_n},}
\tag{17}
$$





$$
\boxed{\delta_n=
\frac{E_n}{E_{n+1}}
\frac{\widetilde b_n\widetilde m_n^{(1)}+
\widetilde b_{1,n}\widetilde m_n^{(0)}}
{\widetilde b_n\widetilde\Xi_n}.}
\tag{18}
$$



All row-scaling factors in $\mathcal H_n$ cancel in these complete expressions.
In particular, one must retain E_n/E_(n+1). Omitting it would study a
different degree-by-degree normalization, even though the monic scalar
accessories and all polynomial roots would remain unchanged.

## 5. The precise minor bounds for the norm criterion

The two derivative-coefficient estimates required in the integral
operator note are equivalent, on the cubic stratum, to the existence
of constants G,D independent of n such that



$$
\boxed{(n+1)|m_n^{(0)}|\le G|\Xi_n|,\qquad
|m_n^{(1)}+\beta_n m_n^{(0)}|\le D|\Xi_n|.}
\tag{19}
$$



Equivalently, in actual bordered determinant form,



$$
(n+1)|E_n\widetilde m_n^{(0)}|
\le G|E_{n+1}\widetilde\Xi_n|,
\tag{20}
$$





$$
|E_n(\widetilde b_n\widetilde m_n^{(1)}+
\widetilde b_{1,n}\widetilde m_n^{(0)})|
\le D|E_{n+1}\widetilde b_n\widetilde\Xi_n|.
\tag{21}
$$



These are two concrete leading-minor problems, involving only two
Laurent coefficient rows at adjacent indices and one B root sum.
They neither replace nor imply the remaining combined Volterra
coefficient bounds or the uniform inverse bound in that note. If all sufficiently large indices are cubic and
those remaining hypotheses and (19) hold there, its proved operator
criterion yields
$\|P_{n+1}\|_2\le C(n+1)\|P_n\|_2$, hence
$\|P_n\|_1\le n!\exp(O(n))$.

The exact obstruction to deriving (19) from outer accessory limits
alone is normalization: multiplying each triple by a nonzero number
s_n preserves its monic scalar equation and every root, but multiplies
Gamma, delta, and the matrix (13) by s_(n+1)/s_n. The actual condition
B_n(1)=1 fixes this freedom globally. Formulas (17)–(18) identify the
endpoint factor through which it enters. A proof must therefore bound
these actual ratios or equivalent connection data; scale-invariant
outer root or accessory estimates cannot silently supply that step.

## 6. Verification and scope

`check_raw_transfer_leading_minors.py` verifies (5) symbolically with
free n and free leading coefficients, using the Laurent Wronskian and
mixed determinant. It then checks the formulas against the already
saved exact n=1-to-2 and n=2-to-3 triples in
`raw_rational_transfer_checks.json`. It constructs no new degree row.
All checks pass; the certificate is
`raw_transfer_leading_minors_checks.json`.

The contribution here is an exact formula and a precise small-minor
target. The minor inequalities, the required norm estimate, and the
endpoint remainder asymptotics remain open.

Independent review: audit_results checked Sections 1–3 and the norm
criterion's normalization. The positive middle cofactor, cancellation
of the B' term, distinction between numerator and Laurent coefficients,
and the wedge identities all passed. No additional sample was run.
