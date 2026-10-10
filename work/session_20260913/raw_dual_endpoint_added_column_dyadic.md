> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The added exponential column proves the primitive-dual endpoint is nonzero

Date: 2026-09-13. Original bounded arithmetic continuation by audit_sources.
Independent review: FULL PASS by audit_results; see raw_dual_added_column_independent_review.md.

This note independently verifies the proposed added-column argument from the original integer matrix. It proves V_n(1)!=0 for every n>=1, including odd degrees. It also proves the exact dyadic comparison


$$
\boxed{\frac{V_n(1)}{[z^n]V_n(z)}
 \in 1+2^{v_2(2n)}\mathbb Z_2.}                           \tag{1}
$$


The denominator in (1) is nonzero by the already reviewed deleted-last-row determinant theorem. No positivity, generic normality, or numerical inference is used. The congruence is dyadic; it is not an Archimedean bound on this ratio.

The inspected predecessors are raw_extremal_dual_polynomial_and_content_identity.md, raw_adjacent_dual_cross_and_fixed_gcd.md and its independent review, and raw_joint_dual_hankel_and_even_root_product.md. Those supply the actual normalization, the deleted-row determinant, and the finite Hankel uniqueness bridge.

## 1. Original matrix, signs and endpoint factor

Use rows k=n,...,3n and the actual integer matrix


$$
(X_n)_{k,B_j}=(k)_{\underline j},\quad
 (X_n)_{k,C_j}=k!\tau_{k-j},\quad 0\le j<n,
$$


where tau_s=[z^s]arctan z. Put


$$
u_k=(-1)^{k-n}\det X_n[\widehat k],\quad
 F_n=\gcd_k|u_k|>0,\quad w_k=u_k/F_n,
$$




$$
W_n(z)=\sum_{k=n}^{3n}w_kz^k=z^n(z-1)^nV_n(z).
$$


The sign is fixed by the displayed cofactor orientation. F_n is positive.

Let M_n have the same rows and the columns in this exact order:


$$
B_0,\ldots,B_n,C_0,\ldots,C_{n-1}.
$$


The added entry in column B_n is (k)_(underline n). If it were appended after all the old columns, expansion of that last column would give


$$
\det[X_n,B_n]=\sum_{k=n}^{3n}(k)_{\underline n}u_k
             =F_n W_n^{(n)}(1)=F_n n!V_n(1).
$$


Moving the appended column left across the n C columns gives


$$
\boxed{\det M_n=(-1)^n F_n n!V_n(1).}                    \tag{2}
$$


There is no additional n! from the row normalization; it appears only through the displayed derivative at 1.

Write


$$
\phi(k)=v_2(k!),\quad S(n)=\sum_{j=0}^{n-1}\phi(j).
$$


We prove


$$
\boxed{v_2(\det M_n)=3S(n)+\phi(n)+
                 \sum_{k=n}^{2n-1}\phi(k).}              \tag{3}
$$


In particular det M_n and V_n(1) are nonzero.

## 2. Uniform dyadic bounds for both kinds of minor

Divide each row k by k!, and perform a Laplace expansion by the first n+1, exponential, columns. If E is the selected set of n+1 B rows, their minor has entries


$$
\frac{(k)_{\underline j}}{k!}
 =\frac{j!}{k!}\binom{k}{j},\quad 0\le j\le n.
$$


Consequently


$$
v_2(\det B_E)\ge S(n+1)-\sum_{k\in E}\phi(k).             \tag{4}
$$


The remaining binomial determinant is an integer. If the n+1 rows are consecutive, its determinant is one: the polynomial degrees 0,...,n have leading coefficients 1/j!, and the consecutive-node Vandermonde cancels the product of these denominators. Hence equality holds in (4) for E={2n,...,3n}.

The complementary C minor has n rows. Reversing its columns turns its entries into


$$
\tau_{k-n+1+j}=\mathcal L(t^{k-n+j}),\quad 0\le j<n,
 \qquad \mathcal L(t^a)=\tau_{a+1}.
$$


All row exponents k-n are nonnegative; no negative moment is present.

The monic raw Legendre polynomials Q_j form an orthogonal basis for L. Their coefficients are dyadically integral and their squared norms satisfy


$$
v_2(\mathcal L(Q_j^2))=2\phi(j).
$$


For precision, the coefficient of t^(j-2a) in Q_j is


$$
\frac{(j!)^2(2j-2a)!}
 {(2j)!a!(j-a)!(j-2a)!};
$$


its valuation is exactly v_2 binom(j,2a)>=0, using phi(2b)=b+phi(b). The inverse monic triangular change of basis is integral as well. The norm formula is


$$
\mathcal L(Q_j^2)
 =(-1)^j\frac{2^{2j}(j!)^4}{(2j)!(2j+1)!},
$$


whose valuation is 2phi(j).

After expressing the row monomials in this basis and the columns in the first n orthogonal polynomials, every C minor is an integral matrix times the diagonal norms. Thus


$$
v_2(\det C)\ge2S(n).                                     \tag{5}
$$


This holds for arbitrary complementary row sets, even if that minor vanishes. For rows k=n,...,2n-1, the row exponents are 0,...,n-1; the transition is triangular with unit diagonal. Equality then holds in (5).

## 3. The unique least Laplace term

The distinguished B row set E_0={2n,...,3n} attains equality in both (4) and (5). Every other n+1-element B row set replaces at least one row k>=2n by a row k<=2n-1. Since phi is nondecreasing, its factorial-sum loss is at least


$$
g_n=\phi(2n)-\phi(2n-1)=v_2(2n)>0.                       \tag{6}
$$


Several replacements cannot reduce this lower bound. Combining (4) and (5), every other Laplace term has valuation at least g_n above the distinguished one. This is a strict inequality even when factorial valuations have plateaus away from the cutoff.

The distinguished term therefore cannot cancel. Restoring the divided row factorials gives


$$
S(n+1)+2S(n)+\sum_{k=n}^{2n-1}\phi(k)
 =3S(n)+\phi(n)+\sum_{k=n}^{2n-1}\phi(k),
$$


which proves (3).

Combining (2) and (3) yields the exact endpoint valuation


$$
\boxed{v_2(V_n(1))
 =3S(n)+\sum_{k=n}^{2n-1}\phi(k)-v_2(F_n).}               \tag{7}
$$


The integer V_n(1) is nonzero in every degree. In particular W_n has a zero of exactly order n at 1.

## 4. Comparison with the deleted-last-row determinant

Let


$$
\Delta_n^0=\det X_n[\text{rows }n,\ldots,3n-1].
$$


The previously reviewed proof gives


$$
v_2(\Delta_n^0)=3S(n)+\sum_{k=n}^{2n-1}\phi(k),\quad
 \Delta_n^0\ne0.
$$


Its cofactor sign is (+1), so


$$
v_n:=[z^n]V_n=w_{3n}=\Delta_n^0/F_n\ne0.                \tag{8}
$$


Equations (7) and (8) already prove v_2(V_n(1))=v_2(v_n).

The full congruence (1) follows by comparing distinguished terms, not merely valuations. In the original unscaled matrices, both distinguished terms contain exactly the same C minor on rows n,...,2n-1. The consecutive exponential minors are


$$
\prod_{j=0}^{n}j!\quad\text{for }M_n,\qquad
 \prod_{j=0}^{n-1}j!\quad\text{for }\Delta_n^0.
$$


With row and column positions starting at zero, the M_n Laplace sign is


$$
(-1)^{\sum_{i=n}^{2n}i+\sum_{j=0}^{n}j}=+1,
$$


whereas the Delta_n^0 sign is


$$
(-1)^{\sum_{i=n}^{2n-1}i+\sum_{j=0}^{n-1}j}=(-1)^n.
$$


Therefore the M_n distinguished term is exactly (-1)^n n! times the Delta_n^0 distinguished term.

Every non-distinguished term of either determinant is at least g_n powers of two deeper: the deleted-row proof has the same cutoff 2n-1 versus 2n. If L_n is the nonzero distinguished term of Delta_n^0, write


$$
\Delta_n^0=L_n(1+\epsilon_n),\quad
 \det M_n=(-1)^n n!L_n(1+\eta_n),
 \qquad \epsilon_n,\eta_n\in2^{g_n}\mathbb Z_2.
$$


Taking the quotient and using (2),(8) gives exactly


$$
\frac{V_n(1)}{v_n}
 =\frac{1+\eta_n}{1+\epsilon_n}
 \in1+2^{g_n}\mathbb Z_2.
$$


This remains meaningful even if the common valuation in (7) is positive. Equivalently,


$$
v_2(V_n(1)-v_n)\ge v_2(v_n)+v_2(2n).                    \tag{9}
$$



## 5. Consequences for the actual joint Hankel matrix

Retain the actual moment functional and polynomial from the joint note:


$$
\mu_n(p)=[z^{2n}]e^z(1+z^2)^n p(z),\quad
 h_\ell=\mu_n(z^\ell),\quad q_n(z)=z^nU_n(1/z).
$$


That note proves that the n-by-(n+1) matrix


$$
(h_{s+j})_{0\le s<n,\ 0\le j\le n}
$$


has rank n, with kernel spanned by q_n, and that


$$
\sum_{j=0}^n h_{n+j}[z^j]q_n=n!V_n(1).
$$


The newly proved nonzero right side implies that adjoining this last row makes the full (n+1)-square Hankel matrix invertible. Hence its row reversal, the actual Toeplitz matrix


$$
A_n=(a_{n+i-j})_{0\le i,j\le n},
 \qquad a_k=[z^k]e^z(1+z^2)^n,
$$


is invertible for **every** n>=1, not only the even degrees.

The exact equation A_n q_n=n!V_n(1)e_0 and
q_n(0)=(2n)!v_n then imply


$$
(A_n^{-1})_{00}
 =\frac{(2n)!}{n!}\frac{v_n}{V_n(1)}\ne0,
 \qquad
 \boxed{v_2((A_n^{-1})_{00})=n.}                          \tag{10}
$$


The last equality uses phi(2n)-phi(n)=n.

For odd n the Toeplitz symbol is signed. Invertibility and the nonzero inverse corner in (10) do not supply the even-degree accretivity bounds, an Archimedean size estimate, or a sign of the inverse corner. Those remain separate analytic requirements.

Also the actual exponential simultaneous numerator has leading coefficient V_n(1), by the previously reviewed translated-factorial formula. It therefore has degree exactly 2n in every degree n>=1.

## 6. Normalization check and scope

The frozen n=1 cofactor polynomial is W=-2z+3z^2-z^3, so V=2-z, F_1=1. The added-column determinant is


$$
\det\begin{pmatrix}1&1&1\\1&2&0\\1&3&-2\end{pmatrix}=-1.
$$


Equation (2) gives (-1)^1 F_1 1!V(1)=-1, and Delta_1^0=-1. The ratio V(1)/v_1=-1 is congruent to 1 modulo 2, as (1) requires. This is only the previously saved n=1 control, not evidence for the all-index claim.

The result is an exact nonvanishing and dyadic-normalization theorem. It neither bounds the odd inverse corner in the real absolute value nor controls the fixed endpoint cancellation gcd(Z,P_e(1)+4P_a(1)).
