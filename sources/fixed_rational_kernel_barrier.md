> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A fixed-rational-kernel barrier for symmetric beta matching

Date: 2026-08-26

## Scope and result

This note generalizes the direct $1/(1+x^2)$ calculation to a broad class
of fixed rational kernels.  Let



$$
K(x)\in\mathbb Q(x)
$$



be fixed, with no pole on $[0,1]$, and suppose that



$$
K(x)\geq\kappa>0\qquad(0\leq x\leq1).             \tag{1}
$$



For even positive integers $n$, put



$$
w_n(x)=x^n(1-x)^n,
\qquad
J_n(K)=\int_0^1w_n(x)K(x)\,dx.                   \tag{2}
$$



Assume that, for an infinite set of even $n$, the exact value has the
special form



$$
J_n(K)=r_n+\varepsilon_n c_n\pi,
\qquad
r_n,c_n\in\mathbb Q,\quad c_n>0,\quad
\varepsilon_n\in\{1,-1\}.                       \tag{3}
$$



For each such $n$, primitive-normalize (3) to an integer form and match
its $\pi$-coefficient with the $e$-coefficient furnished by
$n!^{-1}\int_0^1w_n(x)e^x\,dx$.  The theorem below proves that the final
primitive matched forms tend to infinity in absolute value.  This includes
both the same-sign and the apparently cancellative opposite-sign cases.

Thus changing $1/(1+x^2)$ to any *fixed positive rational kernel* cannot
repair the symmetric common-beta-weight construction, provided its beta
moments really contain only $1$ and $\pi$ as in (3).  The theorem does not
cover a kernel depending on $n$, a sign-changing kernel, different beta
weights for the two constants, or a nonrational kernel.

Nothing in this note proves an arithmetic statement about $e+\pi$.

## 1. The primitive exponential form

Define



$$
F_n(x)=\frac{w_n(x)}{n!},
\qquad
E_n=\int_0^1F_n(x)e^x\,dx.                       \tag{4}
$$



Repeated integration by parts gives, for even $n$,



$$
E_n=q_ne-p_n>0,                                  \tag{5}
$$



where



$$
q_n=(-1)^n\sum_{j=0}^n(-1)^j
     \frac{(n+j)!}{j!(n-j)!},
\qquad
p_n=\sum_{j=0}^n
     \frac{(n+j)!}{j!(n-j)!}.                    \tag{6}
$$



The two sequences satisfy



$$
X_n=2(2n-1)X_{n-1}+X_{n-2},                      \tag{7}
$$



with $q_0=q_1=1$ and $p_0=1,p_1=3$.  Their adjacent determinant is
$\pm2$ and all entries are odd, so



$$
\gcd(p_n,q_n)=1.                                 \tag{8}
$$



Reversing the alternating sum for $q_n$ gives strictly decreasing
absolute terms.  Its first two terms therefore imply



$$
q_n\geq\frac{n(2n-1)!}{n!}.                      \tag{9}
$$



The positivity of the integrand also gives



$$
0<E_n\leq\frac{e\,n!}{(2n+1)!}.                 \tag{10}
$$



These facts are included to make the later normalization self-contained.

## 2. Exponential arithmetic height for a fixed rational kernel

For a rational number $a/b$ in lowest terms with $b>0$, write



$$
H(a/b)=\max\{|a|,b\}.
$$



### Lemma 2.1

For the fixed rational function $K$ in (1), there is a constant
$C_K\geq1$ such that the following holds for every $n\geq1$: if



$$
J_n(K)=r+c\pi\qquad(r,c\in\mathbb Q),             \tag{11}
$$



then



$$
H(r)\leq C_K^n,
\qquad
H(c)\leq C_K^n.                                 \tag{12}
$$



The same statement holds with $c\pi$ replaced by $-c\pi$.

### Proof

Choose fixed coprime $P,Q\in\mathbb Z[x]$ with $K=P/Q$.  Because $K$
has no pole on $[0,1]$ and the representation is reduced, $Q$ has no
zero there.  Let $d=\deg Q$, and divide



$$
P(x)x^n(1-x)^n
$$



by $Q(x)$ over $\mathbb Q$.  The dividend has degree
$2n+O_K(1)$, and the sum of the absolute values of its coefficients is
$O_K(2^n)$.

Ordinary long division takes $2n+O_K(1)$ steps.  At each step one divides
by the fixed leading coefficient of $Q$ and subtracts a fixed translate
of $Q$.  Consequently there is a constant $C_1=C_1(K)$ such that every
coefficient of the quotient and remainder has numerator and denominator at
most $C_1^n$.  More explicitly, all these coefficients have a common
denominator which is a power of the fixed leading coefficient of $Q$, with
exponent $O_K(n)$, while the $\ell^1$-norm of the corresponding
numerators grows at each division step by at most a fixed multiplicative
factor.  Hence



$$
\frac{P(x)x^n(1-x)^n}{Q(x)}
=S_n(x)+\frac{R_n(x)}{Q(x)},
\qquad \deg R_n<d,                               \tag{13}
$$



with all rational coefficients of $S_n,R_n$, on one common denominator,
of numerator and denominator size at most $C_1^n$.

The degree of $S_n$ is $O_K(n)$.  Integrating it from 0 to 1 introduces
only the denominators $1,2,\ldots,O_K(n)$.  The elementary exponential
bound for their least common multiple therefore gives



$$
H\!\left(\int_0^1S_n(x)\,dx\right)\leq C_2^n    \tag{14}
$$



for a fixed $C_2$.  Put



$$
\omega_j=\int_0^1\frac{x^j}{Q(x)}\,dx,
\qquad0\leq j<d.                                \tag{15}
$$



The finite-dimensional $\mathbb Q$-vector space



$$
V=\operatorname{span}_{\mathbb Q}
  \{1,\pi,\omega_0,\ldots,\omega_{d-1}\}
$$



contains $1$ and $\pi$ as linearly independent elements.  Extend them to
a fixed basis



$$
1,\pi,\theta_1,\ldots,\theta_t                  \tag{16}
$$



of $V$.  Every $\omega_j$ in (15) has fixed rational coordinates in this
basis.  Equation (13), followed by integration, therefore expresses every
coordinate of $J_n(K)$ in (16) as a rational linear combination, with
fixed rational coefficients, of the coefficients of $R_n$ and the rational
number in (14).  The common-denominator observation above shows that each
coordinate consequently has height at most $C_3^n$.

If (11) holds, uniqueness of coordinates in (16) says that its first two
coordinates are exactly $r,c$ and that all remaining coordinates vanish.
This proves (12) after increasing the fixed constant. $\square$

### Corollary 2.2

Let



$$
L_n=A_n+\varepsilon_nB_n\pi=m_nJ_n(K)>0          \tag{17}
$$



be the primitive integer normalization of (3), with
$B_n,m_n>0$ and $\gcd(A_n,B_n)=1$.  There is a fixed $C\geq1$ such that



$$
c_nB_n\leq C^n.                                 \tag{18}
$$



Indeed, write $r_n=a_n/b_n$ and $c_n=u_n/v_n$ in lowest terms.
Multiplication by $\operatorname{lcm}(b_n,v_n)$ produces an integer pair
whose $\pi$-coefficient is at most $b_n|u_n|$.  Primitive reduction can
only decrease it.  Lemma 2.1 bounds $b_n,|u_n|$, and $c_n$
exponentially.

## 3. Content created by coefficient matching

The following elementary point prevents a hidden final gcd from invalidating
the analytic estimate.

### Lemma 3.1

Let $(-p,q)$ and $(A,\varepsilon B)$ be primitive integer pairs with
$q,B>0$, and put



$$
d=\gcd(q,B),\qquad u=B/d,\qquad v=q/d,
\qquad C=qB/d.                                   \tag{19}
$$



The minimally coefficient-matched sum or difference has constant
coefficient



$$
M=-up\mathbin{\pm}vA                            \tag{20}
$$



and common target coefficient $C$.  Its final content satisfies



$$
\gcd(M,C)\mid d.                                 \tag{21}
$$



### Proof

Write $q=dq_0$, $B=dB_0$, with $\gcd(q_0,B_0)=1$.  Then



$$
M=-B_0p\mathbin{\pm}q_0A,
\qquad C=dq_0B_0.                                \tag{22}
$$



Because $\gcd(p,q)=1$, the reduction of $M$ modulo every prime divisor
of $q_0$ is a unit.  Because $\gcd(A,B)=1$, the same is true modulo every
prime divisor of $B_0$.  Hence
$\gcd(M,q_0B_0)=1$, which proves (21), including prime powers.
$\square$

In particular, the final content is at most $B$.

## 4. The matched-form barrier

From (1)--(2),



$$
J_n(K)\geq\kappa\int_0^1x^n(1-x)^n\,dx
=\kappa\frac{(n!)^2}{(2n+1)!}.                  \tag{23}
$$



Combining (9) and (23) gives



$$
q_nJ_n(K)\geq\frac{\kappa n!}{2(2n+1)}.         \tag{24}
$$



### Theorem 4.1

Under (1)--(3), let (5) and (17) be separately primitive, let their target
coefficients be matched with the minimal positive integer multipliers, and
then remove the full content of the resulting integer pair.

If $\varepsilon_n=1$, the matched form is a positive sum.  Its final
primitive value satisfies



$$
|\Lambda_n^{\mathrm{prim}}|
\geq\frac{q_nJ_n(K)}{c_nB_n}
\geq\frac{\kappa n!}{2(2n+1)c_nB_n}.             \tag{25}
$$



If $\varepsilon_n=-1$, then for all sufficiently large $n$ the matched
difference has a fixed negative sign and



$$
|\Lambda_n^{\mathrm{prim}}|
\geq\frac{q_nJ_n(K)}{2c_nB_n}
\geq\frac{\kappa n!}{4(2n+1)c_nB_n}.             \tag{26}
$$



In both cases the right side tends to infinity along the index set in (3).

### Proof

First suppose $\varepsilon_n=1$.  If $d_n=\gcd(q_n,B_n)$, the minimal
matched form is



$$
\frac{B_n}{d_n}E_n+\frac{q_n}{d_n}L_n.
$$



Since $L_n/B_n=J_n(K)/c_n$ and $B_n/d_n\geq1$, its positive value is at
least $q_nJ_n(K)/c_n$.  Lemma 3.1 says that final primitive reduction
divides by at most $B_n$, proving (25).

Now suppose $\varepsilon_n=-1$.  Per unit of common coefficient, the
matched difference has value



$$
\frac{E_n}{q_n}-\frac{J_n(K)}{c_n}.              \tag{27}
$$



Equations (9), (10), and (23) give



$$
\frac{E_n/q_n}{J_n(K)/c_n}
\leq\frac{e\,c_n}{\kappa n(2n-1)!}.              \tag{28}
$$



Lemma 2.1 makes $c_n$ at most exponential, so (28) is below $1/2$ for
all sufficiently large $n$.  Thus (27) is negative with absolute value at
least $J_n(K)/(2c_n)$.  The least common coefficient is at least $q_n$,
and Lemma 3.1 again bounds the final content by $B_n$.  This proves (26).

Finally, Corollary 2.2 gives $c_nB_n\leq C^n$.  Since



$$
\frac{n!}{(2n+1)C^n}\longrightarrow\infty,
$$



both (25) and (26) diverge. $\square$

## 5. Exact residual scope

The proof uses all of the following hypotheses:

1. the same symmetric beta weight $x^n(1-x)^n$ is used for both constants;
2. $K$ is a single fixed rational function, independent of $n$;
3. $K$ has a positive lower bound on $[0,1]$;
4. the relevant moments contain no constants other than $1$ and $\pi$;
5. the construction matches the two component coefficients by integer
   cross-multiplication.

A variable kernel may have superexponential arithmetic complexity, a
sign-changing kernel may support genuine cancellation, and different beta
indices need not share the comparison (23).  None of those possibilities is
excluded here.  The theorem is a rigorous obstruction for the stated fixed
rational common-kernel class, not a universal impossibility theorem.
