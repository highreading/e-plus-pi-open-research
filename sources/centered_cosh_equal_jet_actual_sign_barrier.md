> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# An actual-secant sign barrier for the equal quadratic jets

Checked: 2026-08-27 UTC.

## 1. Exact statement

Put



$$
F(x)=\frac1{2\cosh\sqrt x}.
\tag{1}
$$



For nonnegative (L,D), let (Q_{L,D}\in\mathbb Q[x]) be the
denominator of the normal Padé pair of type ([L/D]) for (F), with



$$
Q_{L,D}(0)=1,
 \qquad
 FQ_{L,D}-P_{L,D}=O(x^{L+D+1}).
\tag{2}
$$



Write



$$
\widehat A(y)=y^{\deg A}A(1/y),\qquad
 X_M=\widehat Q_{M,M},\qquad
 Y_M=y\widehat Q_{M+1,M}.
\tag{3}
$$



For polynomials (D,N), with (D(0)\ne0), define the equal quadratic
jet determinant



$$
\Theta_m(D,N)=
 \det [y^i]
 \left\{y^jD^2,y^jDN,y^jN^2:0\le j<m\right\}_{0\le i<3m},
\tag{4}
$$



where the three blocks and the shifts inside each block occur in the
displayed order.

The genuine centered-secant determinants are not sign regular in the Padé
index, even when the block size is fixed.  Exact integer computation gives



$$
\boxed{
 \begin{array}{c|rrrr}
 M&6&7&14&15\\ \hline
 \operatorname {sgn}\Theta_6(X_M,Y_M)&+&-&-&+
 \end{array}.}
\tag{5}
$$



Moreover,



$$
\Theta_4(X_5,Y_5),\quad
 \Theta_4(X_6,Y_6),\quad
 \Theta_4(X_{13},Y_{13}),\quad
 \Theta_4(X_{14},Y_{14})
 \quad\hbox{are all positive}.                            \tag{6}
$$



Consequently the six-dimensional condensation quotients, in the fixed
normalization (2)--(4),



$$
\mathcal B_{M,6}=
 \frac{\Theta_6(X_M,Y_M)}
      {\Theta_4(X_{M-1},Y_{M-1})}                         \tag{7}
$$



have signs (+,-,-,+) at (M=6,7,14,15), respectively.

This is an actual-kernel counterexample, not a generic Markov-system
example.  In particular, a condensation proof cannot have a missing factor
which, under the normalization above, is always a positive ordinary
resultant, a positive Gram determinant, or a nonempty Cauchy--Binet sum of
nonnegative terms.  Likewise, the determinants in (5) cannot themselves be
the fixed-sign normalizing minors of a sign-regular multiple-orthogonality
system as (M) varies.

The result is deliberately narrow.  It does **not** rule out an identity
with a genuinely sign-changing prefactor, and it does not disprove or prove
the conjectured all-parameter nonvanishing.

## 2. Why primitive clearing preserves the signs

The replay clears each rational denominator independently.  More precisely,
if (q=(q_0,\ldots,q_D)), (q_0=1), is the coefficient vector of
(Q_{L,D}), it multiplies by the least common multiple of the denominators,
divides by the gcd of the resulting integers, and chooses the sign so that
the constant coefficient is positive.  Denote the resulting primitive
integer polynomial by (Q_{L,D}^{\rm prim}).

Thus



$$
Q_{L,D}^{\rm prim}=c_{L,D}Q_{L,D},\qquad c_{L,D}>0.       \tag{8}
$$



For positive (u,v), direct column scaling in (4) gives



$$
\Theta_m(uD,vN)=u^{3m}v^{3m}\Theta_m(D,N).              \tag{9}
$$



Therefore using the independently primitive diagonal and upper-adjacent
denominators changes none of the signs in (5)--(7).  This also removes any
ambiguity from rational denominator clearing.

## 3. Exact reconstruction

No decimal approximation is used.  Write



$$
F(x)=\sum_{n\ge0}f_nx^n.
$$



The identity (2F(x)\cosh\sqrt x=1) reconstructs the coefficients by



$$
f_0=\frac12,
 \qquad
 f_n=-\sum_{j=1}^n\frac{f_{n-j}}{(2j)!}\quad(n\ge1).     \tag{10}
$$



With (Q_{L,D}=1+q_1x+\cdots+q_Dx^D), the (D) equations



$$
\sum_{j=0}^Dq_jf_{n-j}=0,
 \qquad L+1\le n\le L+D,                                 \tag{11}
$$



determine the rational coefficients.  The certificate solves (11) over
(\mathbb Q), substitutes the answer back into every equation, checks the
top coefficient is nonzero, and then performs the primitive clearing in
§ 2.

It next constructs every entry of the (3m\)-square integer matrix in (4)
by exact polynomial convolution and computes its determinant over
(\mathbb Z).  The signed decimal determinant is retained in full in the
JSON certificate.  For compact cross-checking, its SHA-256 and bit length
are



$$
\begin{array}{c|c|c|c}
(M,m)&\operatorname {sgn}&\text{bit length}&
 \operatorname {SHA256}(\text{signed decimal})\\ \hline
(6,6)&+&2796&5792c404daeb671fdbdfc41abb42c586c5275e2cd4e30e88607d8699b385e265\\
(7,6)&-&3665&e161ddc7f87e00cdb5cee000dea6e0227af844778bb87da7052b389e120d2106\\
(14,6)&-&13169&2be64277f638c516f092b35d6bc9aaf839deabc23fdf78e448042b8a61940168\\
(15,6)&+&14872&2c68405788670b97b0babb816bb7de86efb3c71a8eb073fbcc6f87241c1e8c53\\
(5,4)&+&1319&fd81ceb8eda424e06e8d44b2b54fc6bcc5e3b266641eabd50de2cbaa6794c2e4\\
(6,4)&+&1804&6821927f78e8aa1e9588ab9f38f8f7350651f1dbec1dbb296748495dd00f2a91\\
(13,4)&+&7393&19d849d850fe05024526275f4a10db2d95efe61b4d04f15af1dc560464249271\\
(14,4)&+&8585&57c27af53bbe838b3449d30bdbec7888dbeaeac979c5c92e4a296e4b0181f9f9
\end{array}                                                \tag{12}
$$



The certificate also stores the complete primitive coefficient vectors,
the exact determinant integers, the reduced numerator and denominator of
each quotient (7), and canonical hashes of every input vector and jet
matrix.  Thus the signs are consequences of independently reconstructed
rational Padé systems and exact determinants; they are not copied into the
output as unsupported labels.

## 4. Logical boundary

Suppose, for example, that a proposed condensation identity had the form



$$
\mathcal B_{M,6}=c_M\sum_I w_{M,I},
 \qquad c_M>0,\quad w_{M,I}\ge0,                          \tag{13}
$$



with at least one positive summand for every (M).  Equations (5)--(7)
contradict (13).  The same argument applies to a positive resultant or Gram
factor.  It does not apply if (c_M) is allowed to carry the observed sign
changes.  Hence (5) identifies a precise limitation of positivity-based
proofs without overstating what the finite witnesses establish.

The companion files are

* `scripts/centered_cosh_equal_jet_actual_sign_barrier_certificate.py`;
* `results/centered_cosh_equal_jet_actual_sign_barrier_certificate.json`;
* `results/centered_cosh_equal_jet_actual_sign_barrier_hashes.sha256`.

This local obstruction has no standalone implication for (e+\pi).
