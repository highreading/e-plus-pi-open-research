> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Actual Toeplitz hook normalization and a congruence at every prime dividing 2n

Date: 2026-09-13. Original specialization of a published Appell theorem,
by audit_sources. Independent review: **FULL PASS**, audit_results;
see raw_appell_hook_congruence_independent_review.md.

This is a direct application of Bonneux, Hamaker, Stembridge and Stevens,
*Wronskian Appell polynomials and symmetric functions*, Advances in
Applied Mathematics 111 (2019), 101932, Theorem 4.1, Proposition 4.3 and
the integer-power-sum statement in the proof of Theorem 5.8.
[Primary paper, arXiv:1812.01864v2](https://arxiv.org/pdf/1812.01864v2).
The application below is to the actual family, not to a guessed
Painlevé identification.

## 1. The actual full determinant and its actual corner

Fix an integer $n\ge1$, and define


$$
a_k^{[n]}(x)=[t^k]e^{xt}(1+t^2)^n,\qquad a_k=0\quad(k<0).
$$


Use the matrices with exactly these row and column conventions:


$$
A_n(x)=(a_{n+i-j}^{[n]}(x))_{i,j=0}^{n},\qquad
 D_n(x)=\det A_n(x),
$$




$$
B_n(x)=\det(a_{n+i-j}^{[n]}(x))_{i,j=0}^{n-1}.
$$


Deleting row zero and column zero of $A_n$, and subtracting one from
both surviving indices, gives exactly $B_n$. In particular,


$$
(A_n(1)^{-1})_{00}=B_n(1)/D_n(1)                       \tag{1}
$$


whenever the inverse exists. Neither determinant has a row factorial
already inserted.

Define the positive integer hook products


$$
H_D=\prod_{j=0}^{n}\frac{(n+j)!}{j!},\qquad
 H_B=\prod_{j=0}^{n-1}\frac{(n+j)!}{j!},\qquad
 R=\frac{H_D}{H_B}=\frac{(2n)!}{n!}.                    \tag{2}
$$


These are respectively the hook products of the rectangles
$\lambda_D=(n^{\,n+1})$ and $\lambda_B=(n^n)$.

## 2. Exact Appell specialization and integral coefficients

Let $\mathcal A_k(x)=k!a_k^{[n]}(x)$. This is a monic Appell sequence:
$\mathcal A_0=1$ and $\mathcal A_k'=k\mathcal A_{k-1}$.
In its complete-symmetric-function specialization,


$$
\varphi(h_k)=a_k^{[n]}(x),\qquad
 \sum_{k\ge0}\varphi(h_k)t^k=e^{xt}(1+t^2)^n.
$$


The logarithm gives the exact power-sum values


$$
\varphi(p_1)=x,\qquad
 \varphi(p_{2j})=2n(-1)^{j+1}\quad(j\ge1),\qquad
 \varphi(p_{2j+1})=0\quad(j\ge1).                       \tag{3}
$$


These are the cumulant ratios in Proposition 4.3 of the cited paper.

Transposition, followed by the ordinary Jacobi--Trudi formula, gives


$$
D_n=\varphi(s_{\lambda_D}),\qquad
 B_n=\varphi(s_{\lambda_B}).                            \tag{4}
$$


This complete-function partition $(n^{n+1})$ is the conjugate of the
elementary-function partition $((n+1)^n)$ used in the earlier
deformation note. Confusing the two would change the specialization.

The universal integer-coefficient identity used in the proof of
Theorem 5.8 is


$$
H(\lambda)s_\lambda
   =p_1^{|\lambda|}
     +\sum_{\substack{\mu\vdash|\lambda|\\\mu\ne(1^{|\lambda|})}}
             d_{\lambda,\mu}p_\mu,\qquad d_{\lambda,\mu}\in\mathbb Z.
                                                               \tag{5}
$$


For clarity, the coefficient of $p_1^{|\lambda|}$ is one. The
Frobenius formula gives each other coefficient as
$|\mathcal C_\mu|\chi^\lambda(\mu)/f^\lambda$, the scalar by which
the integral class sum acts in the irreducible representation indexed
by $\lambda$. It is a rational algebraic integer and hence an integer.
This also explains the integrality statement and its normalization.

Every nonleading monomial in (5), after (3), either vanishes or contains
a factor $2n$. Therefore, in the polynomial ring $\mathbb Z[x]$,


$$
\boxed{
 M_D(x):=H_DD_n(x)\in\mathbb Z[x],\qquad
 M_D(x)\equiv x^{n(n+1)}\pmod{2n},}                     \tag{6}
$$




$$
\boxed{
 M_B(x):=H_BB_n(x)\in\mathbb Z[x],\qquad
 M_B(x)\equiv x^{n^2}\pmod{2n}.}                        \tag{7}
$$


Both polynomials are monic. Equations (6)--(7) are stronger than
integrality alone and hold for every positive $n$.

## 3. Exact valuations and the inverse corner

At $x=1$, both normalized values are congruent to one modulo $2n$.
They are therefore nonzero integers relatively prime to $2n$.
Thus $A_n(1)$ is invertible, its corner is nonzero, and for every
prime $p\mid2n$,


$$
v_p(D_n(1))=-v_p(H_D),\qquad
 v_p(B_n(1))=-v_p(H_B).                                 \tag{8}
$$


Set $v_0=(A_n(1)^{-1})_{00}$. Equations (1)--(2) give the exact identity


$$
\frac{v_0}{R}=\frac{M_B(1)}{M_D(1)}.                   \tag{9}
$$


The denominator on the right is relatively prime to $2n$. Therefore,
simultaneously for every $p\mid2n$,


$$
\boxed{\frac{v_0}{R}\in1+2n\mathbb Z_{(p)},\qquad
        v_p(v_0)=v_p(R).}                              \tag{10}
$$


The first assertion has the full depth $v_p(2n)$, not just depth one.
Globally (9) lies in $1+2n\mathcal R_n$, where $\mathcal R_n$ is the
subring of rationals whose reduced denominators are relatively prime
to $2n$.

More generally, if an integer $x$ is relatively prime to $2n$, (6)--(7)
give $v_0(x)/R\equiv x^{-n}\pmod{2n\mathcal R_n}$, with
$v_0(x)=B_n(x)/D_n(x)$. Only $x=1$ is used for the actual endpoint.

## 4. Original dual-polynomial normalization

Retain the original polynomials $U_n,V_n$, with
$V_{n,\mathrm{lead}}=[t^n]V_n$.
The exact Hankel-to-Toeplitz equation in
raw_joint_dual_hankel_and_even_root_product.md is


$$
A_n(1)\,\mathbf q_n=n!V_n(1)e_0,\qquad
 q_n(0)=[t^n]U_n=(2n)!V_{n,\mathrm{lead}}.              \tag{11}
$$


Here $\mathbf q_n$ is the coefficient vector of the reversed dual
polynomial, not the positive reduced endpoint denominator. Equation
(11) is algebraic and valid in both parities; its later positivity
argument in that source was restricted to even $n$. The all-index
nonvanishing and exact normalization are also recorded in
raw_dual_endpoint_added_column_dyadic.md.

The constant coordinate of (11) yields


$$
\frac{V_n(1)}{V_{n,\mathrm{lead}}}=\frac R{v_0}
     =\frac{M_D(1)}{M_B(1)}.
$$


Consequently, for every $n\ge1$ and every prime $p\mid2n$,


$$
\boxed{
 \frac{V_n(1)}{V_{n,\mathrm{lead}}}
       \in1+2n\mathbb Z_{(p)},\qquad
 v_p(V_n(1))=v_p(V_{n,\mathrm{lead}}).}                  \tag{12}
$$


This extends the prior dyadic quotient congruence to every prime
dividing $n$, with no restriction such as $n=mp^\nu$, $3m<p$.
For the frozen $n=1$ control, $M_D=x^2-2$, $M_B=x$;
at one the quotient is $-1$, consistent with (12) modulo two.

## 5. Scope and next arithmetic question

This proves exact normalization information at the primes dividing
$2n$. It does not show that the actual reduced endpoint denominator
is a unit there, and does not control its factors at primes not dividing
$2n$. In particular, it does not transfer the scalar relation (12)
to the distinct evaluated numerator $N_n$ or denominator $Z_n$.

One useful next step is to express the exact primitive endpoint
numerator and its neighboring cofactor evaluations in the same
augmented-Schur coordinates, keeping their hook factors and integral
linear combinations. Such a representation could turn (6)--(7) into
an actual endpoint gcd statement. Merely recognizing a Schur function
or a Painlevé-like determinant does not provide that missing step.
