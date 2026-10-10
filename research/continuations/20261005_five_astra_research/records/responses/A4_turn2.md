> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4 independent review and quantitative continuation

## Executive assessment

**A5’s moving-prime theorem passes the arithmetic review for the original falling-factorial metric**, on its stated finite domain and with the stated anisotropy condition. The CRT/Dirichlet construction genuinely supplies infinitely many applicable primes. In particular, its upper bound on norm content is justified by anisotropy—not by a large determinant or by divisibility alone.

**A1’s compact-root argument also passes.** The Stieltjes determinacy condition is the correct one, the Gaussian quadrature argument handles unbounded support, and quasi-orthogonal interlacing gives arbitrarily many roots in every fixed positive open interval. This invalidates eventual compact positivity, but does not exclude the signed determinant family.

The endpoint applications retain two important boundaries:

* finite normality is still needed to identify A5’s lattice quantities with the actual endpoint-normalized center;
* A1’s lower-block nonsingularity and dyadic denominator assertion, and A5’s proportional signed-error theorem, remain inherited dependencies rather than independently proved inputs here.

As a quantitative continuation, I prove:

1. a stronger signed stationary bound, replacing A1’s factor $1+\theta_n^{-1}$ by $\theta_n^{-1}$, with the optimal absolute-weight Christoffel quantity in place of an arbitrary test polynomial;
2. an explicit, finite-index lower bound for $\theta_n$, obtained from the **actual rational signed lower block** and a rational Cauchy determinant majorant for its absolute Gram matrix.

The second result is effective but potentially very weak. Neither result is promoted to an asymptotic denominator budget or an irrationality conclusion.

---

# I. Independent review of A5’s moving-prime arithmetic

## 1. Domain and metric

Throughout the arithmetic review, let


$$
n=p-1,\qquad b\ge5,\qquad 2b-3<p,\qquad m=1,
$$


where $p$ is an odd prime. The original weights are


$$
\omega_j=\frac{(p+1)!}{(p+1-j)!},\qquad 0\le j\le b,
$$


and


$$
\Omega=\operatorname{diag}(\omega_j^2).
$$



The comparison rising weights are not used to identify the original center.

The actual high block is


$$
R_{lj}=E_{p-1+l,l+j-1},
\qquad 1\le l\le b-2,\quad 0\le j\le b.
$$



## 2. Triangular high-row reduction: **PASS**

Put $k=p+s$, $0\le s\le b-3$. In


$$
H_k(x)=\sum_{t=0}^k k^{\underline t}[z^t](1-z+z^2/2)^k\,x^{k-t},
$$


every coefficient with $t>s$ contains a factor $p$ in $k^{\underline t}$. For $t\le s<p$, Frobenius reduction gives


$$
[z^t](1-z+z^2/2)^{p+s}
\equiv [z^t](1-z+z^2/2)^s\pmod p.
$$


Consequently,


$$
x^{p+s}H_{p+s}(x)\equiv x^{2p}x^sH_s(x)\pmod p.
$$



The derivative orders are


$$
r=s+j\le2b-3<p.
$$


All positive derivatives of $x^{2p}$ of these orders vanish modulo $p$. Thus


$$
R_{s+1,j}\equiv
\left.(x^sH_s(x))^{(s+j)}\right|_{x=1}\pmod p.
$$


Since $x^sH_s$ is monic of degree $2s$,


$$
R_{s+1,j}\equiv0\quad(j>s),\qquad
R_{s+1,s}\equiv(2s)!\ne0\pmod p.
$$



Therefore the first $b-2$ columns give an invertible triangular block modulo $p$. In particular,


$$
Rz=0,\quad z\in\mathbb Z^{b+1}
\quad\Longrightarrow\quad
z_0,\ldots,z_{b-3}\equiv0\pmod p.
$$



This establishes both the asserted rank and the kernel restriction uniformly in the growing dimension.

## 3. First two rows modulo $p^2$: **PASS**

### First row

For $1\le t<p$, the coefficient indexed by $t$ in $H_p$ contains:

* a factor $p$ from $p^{\underline t}$;
* a factor $p$ from $[z^t](1-z+z^2/2)^p$.

Thus these terms vanish modulo $p^2$. The last term, $t=p$, has coefficient divisible by $p$, and its exponent in $x^pH_p$ is $p$. Any derivative of order $1\le r<p$ supplies a second factor $p$. Hence


$$
E_{p,r}\equiv(2p)^{\underline r}\pmod{p^2},
$$


and


$$
\frac{E_{p,r}}p
\equiv2(-1)^{r-1}(r-1)!\pmod p.
$$



### Second row

The first two terms of $x^{p+1}H_{p+1}$ are


$$
x^{2p+2}-(p+1)^2x^{2p+1}.
$$



The treatment of the omitted terms is valid, but merits making the endpoint cases explicit:

* $t=2$: its coefficient is divisible by $p$, and its exponent is $2p$;
* $3\le t\le p-1$: the falling product and the coefficient of the defining power each supply a factor $p$;
* $t=p,p+1$: the coefficient contains $p$, while the exponents are $p+2,p+1$; derivatives of order $r\ge3$ include a factor $p$.

Thus for $3\le r<p$,


$$
\begin{aligned}
\frac{E_{p+1,r}}p
&\equiv
4(-1)^{r-3}(r-3)!
-2(-1)^{r-2}(r-2)!\\
&=2r(-1)^{r-3}(r-3)!\pmod p.
\end{aligned}
$$


The reductions


$$
E_{p,0}\equiv1,\qquad E_{p+1,1}\equiv1,\qquad
E_{p+1,2}\equiv2\pmod p
$$


also agree with the triangular calculation.

No modular division by a nonunit is being performed without first establishing integer divisibility.

## 4. Actual falling-metric restriction: **PASS**

Write $s=b-2$, and for the three surviving tail indices define


$$
d_j=(-1)^{j-2}(j-2)!\,z_j\pmod p,
\qquad j=s,s+1,s+2.
$$


For $j\ge2$,


$$
\frac{\omega_j}{p}\equiv(-1)^{j-2}(j-2)!\pmod p.
$$



The first row divided by $p$ gives


$$
\frac{z_0}{p}\equiv2\sum_{j=s}^{s+2}(j-1)d_j\pmod p.
$$


The second gives


$$
\frac{z_0}{p}+2\frac{z_1}{p}
+2\sum_{j=s}^{s+2}(j+1)d_j\equiv0\pmod p,
$$


so


$$
\frac{(p+1)z_1}{p}\equiv-2\sum_{j=s}^{s+2}j\,d_j\pmod p.
$$



All intermediate weighted coordinates, after division by $p$, vanish modulo $p$. Therefore, for any two integer kernel vectors,


$$
\frac{z^T\Omega z'}{p^2}
\equiv d(z)^TM_s d(z')\pmod p,
$$


where


$$
M_s=I+4aa^T+4bb^T,\qquad
a=(s-1,s,s+1)^T,\quad b=(s,s+1,s+2)^T.
$$



This is a restriction of the actual factorial metric. It does not substitute an unrelated norm.

## 5. Binary restriction and the explicit polynomial: **PASS**

If additionally $\mathbf ez=0$, then


$$
s(s-1)d_s-sd_{s+1}+d_{s+2}=0.
$$


The displayed basis


$$
v=(1,0,-s(s-1))^T,\qquad w=(0,1,s)^T
$$


is valid.

Here is an independent expansion of the determinant. Let


$$
e=(s(s-1),-s,1)^T.
$$


The cross products are


$$
a\times e=
\begin{pmatrix}
s^2+2s\\
s^3-2s+1\\
-s^3+s
\end{pmatrix},
\qquad
b\times e=
\begin{pmatrix}
s^2+3s+1\\
s^3+s^2-3s\\
-s^3-s^2+s
\end{pmatrix}.
$$


Their squared norms are


$$
\|a\times e\|^2
=2s^6-5s^4+6s^3+9s^2-4s+1,
$$




$$
\|b\times e\|^2
=2s^6+4s^5-5s^4-2s^3+21s^2+6s+1.
$$


Also,


$$
\|e\|^2=s^4-2s^3+2s^2+1,
$$


and


$$
((a\times b)\cdot e)^2=(s^2+s+1)^2.
$$


Cauchy–Binet therefore gives


$$
\boxed{
D_-(s)=16s^6+16s^5-23s^4+46s^3+170s^2+40s+25.
}
$$



For a binary form with symmetric matrix determinant $D\ne0$, isotropy over $\mathbb F_p$ is equivalent to $-D$ being a square. Thus A5’s anisotropy criterion is correct.

If $z$ is primitive, its tail $d(z)$ cannot vanish: otherwise the triangular restriction makes every coordinate divisible by $p$. Consequently


$$
\left(\frac{-D_-(s)}p\right)=-1
\quad\Longrightarrow\quad
v_p(z^T\Omega z)=2.
$$



This is the decisive **upper valuation bound**. The preceding divisibility statements alone would not establish it.

For the actual adapted vectors, whenever finite normality supplies their interpretation,


$$
v_p(T)=2,\qquad v_p(V_0)\ge2,
$$


and hence


$$
\boxed{v_p(\delta)=v_p(\gcd(T,|V_0|))=2.}
$$



## 6. CRT and the infinite progression: **PASS**

The shifted polynomial identity is


$$
D_-(-2-t)
=401+1144t+1902t^2+1690t^3+777t^4+176t^5+16t^6.
$$


It verifies A5’s $J_-$. Similarly,


$$
K^4D_+(-2-1/K)=K^4+2K^2+2K+1.
$$



For $K=2001$,


$$
J_+\equiv1\pmod K,\qquad J_-\equiv16\pmod K,
$$


so


$$
\gcd(K,4J_+J_-)=1.
$$


The simultaneous conditions


$$
p\equiv1\pmod K,\qquad p\equiv-1\pmod{4J_+J_-}
$$


therefore define a reduced residue class. Dirichlet’s theorem yields infinitely many primes in it.

For completeness, if $\ell$ is an odd prime divisor of a positive integer $J$, then under $p\equiv-1\pmod{4J}$,


$$
\left(\frac{\ell}{p}\right)
=
\left(\frac{p}{\ell}\right)
(-1)^{(\ell-1)/2}
=
\left(\frac{-1}{\ell}\right)(-1)^{(\ell-1)/2}=1.
$$


If $2\mid J$, the same progression has $p\equiv7\pmod8$, so $(2/p)=1$. Thus


$$
(J/p)=1,\qquad (-J/p)=-1.
$$



This verifies the infinite implication without relying on finite residue evidence.

## 7. Saturation and weighted Plücker content: **PASS**

A basis matrix of a saturated rank-two sublattice of $\mathbb Z^{b+1}$ has rank two modulo every prime. Equivalently, its maximal minors have gcd one; this follows from Smith normal form.

For the falling metric, every weighted kernel vector is divisible by $p$. After division by $p$, the tail coordinate map is diagonal with unit entries modulo $p$. Since all unweighted rank is already in the three tail coordinates, some weighted two-by-two minor divided by $p^2$ is a unit. Hence


$$
v_p(C_\Omega)=2.
$$



This proof requires saturation, not merely linear independence over $\mathbb Q$.

It does **not** give


$$
v_p(TU_0-V_0^2)=4.
$$


A5 correctly refrains from that assertion: the sum of squares of normalized minors can cancel modulo $p$.

## 8. Final-$q$ localization: **PASS, conditional on the endpoint lattice setup**

Retain the actual final-gcd formula


$$
g_B=k\delta\alpha\gcd(k,|r|),
\qquad
q=\frac t\alpha\,\frac{k}{\gcd(k,|r|)},
$$


where


$$
t=T/\delta,\qquad \alpha=\gcd(t,|a'|).
$$


The proved equality $v_p(T)=v_p(\delta)$ gives


$$
v_p(t)=v_p(\alpha)=0.
$$


Therefore


$$
\boxed{v_p(q)=\max\{0,v_p(k)-v_p(r)\}.}
$$



This fully resolves the norm channel at that one prime, but not the scalar channel. It supplies no linear-in-$n$ budget. In particular, the information gained per index remains of logarithmic scale.

The rising-metric comparison also passes its separate modular calculation, but is not an assertion about the original metric.

---

# II. Independent review of A1’s compact roots and signed inequality

## 9. Stieltjes determinacy: **PASS**

For


$$
d\nu=(y+1)d\mu,\qquad m_r=D_{2r}+D_{2r+2},
$$


the bound


$$
m_r\le2(2r+2)!
$$


implies


$$
m_r^{-1/(2r)}\ge c/r
$$


for a fixed $c>0$. Thus the Stieltjes Carleman series diverges.

A1 correctly distinguishes this from the Hamburger Carleman series. Only uniqueness on $[0,\infty)$ is needed.

## 10. Gaussian weak convergence and uniform integrability: **PASS**

The quadrature measures have common mass and first moment, hence are tight. For any fixed $r$, eventual exactness of the $(r+1)$-st moment gives


$$
\int_{y>R}y^r\,d\nu_N\le m_{r+1}/R.
$$


This is sufficient for uniform integrability and passage of every fixed moment to a subsequential weak limit.

The limiting measure remains supported on $[0,\infty)$, so Stieltjes determinacy identifies it with $\nu$. Hence the entire sequence converges weakly.

For any fixed positive open interval $I$, Portmanteau gives


$$
\liminf_N\nu_N(I)\ge\nu(I)>0.
$$


Thus $I$ eventually contains a node. Applying this simultaneously to finitely many disjoint intervals is valid.

## 11. Quasi-orthogonal interlacing: **PASS**

The identity


$$
\int Q_n r\,d\nu=0,\qquad \deg r\le n-2,
$$


implies, after monic normalization,


$$
\widehat Q_n=\pi_n+a_n\pi_{n-1}.
$$


At consecutive zeros of $\pi_{n-1}$, the values of $\pi_n$ alternate in sign, by the positive-measure three-term recurrence. The same is therefore true of $\widehat Q_n$.

Consequently every block of $L+1$ Gaussian nodes in $(a,b)$ produces at least $L$ roots of $Q_n$ there. It follows that


$$
\#\{Q_n\text{ roots in }(a,b)\}\longrightarrow\infty
$$


for every fixed $0<a<b<\infty$.

The conclusion about eventual positivity is sound. The warning about finite-dimensional compression is also essential: a sign-changing weight does not alone determine the inertia of its polynomial Gram compression.

## 12. A1’s signed stationary inequality: **PASS**

With


$$
C=G^{-1/2}HG^{-1/2},\qquad
\theta=\min|\operatorname{spec}C|>0,
$$


the identity


$$
\mathcal J(F^2)=\mathcal J(P^2)-h^TH^{-1}h
$$


and the Hilbert-space projection bound


$$
h^TG^{-1}h\le\mathcal M(P^2)
$$


give exactly


$$
|\mathcal J(F^2)|\le(1+\theta^{-1})\mathcal M(P^2).
$$



The proof is valid for signed weights. Nonsingularity of $H$ remains an explicit premise.

The later dyadic nonvanishing argument is also logically correct **if** the inherited exact two-adic denominator theorem holds: different reduced denominator two-depths force different rational centers, so at most one center can equal $S=e+\pi$. Nothing here independently verifies that arithmetic dependency.

---

# III. Quantitative extension: a stronger signed bound and an effective spectral floor

## 13. Improved signed stationary theorem

Let


$$
\mathcal V=\{P:\deg P\le r,\ P(-1)=0\}
$$


and let $\mathcal M$ and $\mathcal J$ be A1’s absolute and signed functionals. Assume the restriction of $\mathcal J$ to $\mathcal V$ is nonsingular.

Define the positive absolute-weight Christoffel quantity


$$
\lambda_{\mathcal M}
=
\min_{\substack{\deg P\le r\\P(-1)=1}}\mathcal M(P^2)>0.
$$



Then the actual signed stationary polynomial $F$ satisfies


$$
\boxed{
|\mathcal J(F^2)|\le\frac{\lambda_{\mathcal M}}{\theta}.
}
\tag{13.1}
$$


In particular, for every admissible test polynomial $P$,


$$
\boxed{
|\mathcal J(F^2)|\le\theta^{-1}\mathcal M(P^2).
}
\tag{13.2}
$$



### Proof

Let $P_*$ be the unique absolute-weight minimizer. It is $\mathcal M$-orthogonal to $\mathcal V$. Normalize


$$
e_0=P_*/\sqrt{\lambda_{\mathcal M}},
$$


and choose an $\mathcal M$-orthonormal basis of $\mathcal V$.

In this orthonormal basis, the signed form has matrix


$$
A=
\begin{pmatrix}
a&h^T\\
h&C
\end{pmatrix}.
$$


Because $\mathcal J$ is integration against the sign of $Q_n$ times the positive measure defining $\mathcal M$, this compression is a symmetric contraction:


$$
\|A\|\le1.
$$


Therefore $I-A^2$ is positive semidefinite. Its lower principal block gives


$$
hh^T+C^2\le I.
$$


Congruence by $C^{-1}$ yields


$$
C^{-1}hh^TC^{-1}\le C^{-2}-I.
$$


Since every eigenvalue of $C$ has absolute value at least $\theta$,


$$
\|C^{-1}h\|^2\le\theta^{-2}-1.
$$



Put


$$
x=\binom{1}{-C^{-1}h}.
$$


Then


$$
Ax=\binom{a-h^TC^{-1}h}{0},
$$


so


$$
|a-h^TC^{-1}h|
=\|Ax\|
\le\|x\|
\le\theta^{-1}.
$$



The normalized stationary vector is precisely $x$; rescaling to endpoint value one gives


$$
\mathcal J(F^2)
=\lambda_{\mathcal M}(a-h^TC^{-1}h).
$$


This proves (13.1), and the minimizing property proves (13.2). ∎

This improves A1’s bound without requiring positivity of $Q_n$, and without assuming that the stationary value is nonzero.

For the Chebyshev test polynomial, it gives


$$
\boxed{
|S-c_n|
\le
\frac{S-1}{\theta_n T_r(3)^2}
\sup_{[0,1]}\frac{|Q_n|}{Q_n(-1)}.
}
\tag{13.3}
$$



## 14. An explicit effective lower bound for the signed spectral gap

This next result applies at every finite index where the actual rational block $H$ is nonsingular.

Write


$$
Q_n(y)=\sum_j c_jy^j,\qquad
C_n=\sum_j|c_j|>0.
$$


Let $L$ be any positive integer for which


$$
K=LH
$$


is an integer matrix. We retain the actual determinant $\det K$, rather than substituting a row denominator for it.

Since the eigenvalues of $C=G^{-1/2}HG^{-1/2}$ all lie in $[-1,1]$,


$$
|\det C|\le\theta.
$$


Thus


$$
\boxed{
\theta\ge\frac{|\det H|}{\det G}
=\frac{|\det K|}{L^r\det G}.
}
\tag{14.1}
$$



We now bound $\det G$ by an explicit rational expression.

On $0<y<1$,


$$
|Q_n(y)|\le C_n,\qquad
e^{\sqrt y}+\frac4{1+y}<7.
$$


Consequently


$$
G\le7C_n W,
\qquad
W_{ij}=\int_0^1u_i(y)u_j(y)\frac{dy}{2\sqrt y}.
$$



Every $u_i$ is divisible by $y+1$. The polynomials


$$
u_i(y)/(y+1),\qquad 1\le i\le r,
$$


form a monic triangular basis of degrees $0,\ldots,r-1$, with transition determinant one. Since $(y+1)^2\le4$ on $[0,1]$, determinant monotonicity gives


$$
\det W\le4^r\det\mathsf H_r,
$$


where


$$
(\mathsf H_r)_{ij}=\frac1{2i+2j+1},
\qquad 0\le i,j<r.
$$


The Cauchy determinant is exactly


$$
\boxed{
\det\mathsf H_r
=
\frac{\displaystyle\prod_{0\le i<j<r}4(j-i)^2}
{\displaystyle\prod_{i,j=0}^{r-1}(2i+2j+1)}.
}
\tag{14.2}
$$


Therefore


$$
\det G\le(28C_n)^r\det\mathsf H_r.
$$


Substitution in (14.1) proves


$$
\boxed{
\theta_n
\ge
\frac{|\det(LH)|}
{(28LC_n)^r\det\mathsf H_r}
\ge
\frac1{(28LC_n)^r\det\mathsf H_r}.
}
\tag{14.3}
$$



The last inequality uses only the proved nonvanishing of the integer determinant. This is a lower bound for a spectral gap, not an upper bound for any gcd.

### Scope and usefulness

Equation (14.3) is an **effective finite-index signed spectral estimate**. It uses:

* the actual rational signed lower block;
* an exact integer determinant;
* ordinary integer coefficient height;
* an explicit rational Cauchy determinant.

It requires no numerical eigenvalue certification and remains valid after compact sign changes begin.

It may be far too weak for asymptotic purposes. In particular, it can lose enormous information by replacing $|Q_n|$ with $C_n$, and by replacing the actual $\det(LH)$ with one. I make no assertion that its logarithm is $o(n)$, or even $O(n)$.

Nevertheless, it provides a rigorous quantitative floor where the previous interface only named an unknown positive gap.

## 15. Complete error, actual primitive denominator, and nonvanishing

Let the actual rational center be $c_n=p_n/q_n$, with the final reduction performed:


$$
g=\gcd(|A|,|B|),\qquad
p_n=-\frac{\operatorname{sgn}(B)A}{g},\qquad
q_n=\frac{|B|}{g}>0.
$$


Then, with $w=Q_n(-1)>0$,


$$
\boxed{
q_nS-p_n=\frac{q_n}{w}\mathcal J(F_n^2).
}
\tag{15.1}
$$


The improved bound is


$$
\boxed{
|q_nS-p_n|
\le
\frac{q_n}{w\theta_n}\lambda_{\mathcal M}
\le
\frac{q_n(S-1)}
{\theta_n T_r(3)^2}
\sup_{[0,1]}\frac{|Q_n|}{w}.
}
\tag{15.2}
$$



On the regular dyadic domain, **conditional on the inherited denominator theorem**, one may substitute


$$
q_n=2^{n+2}o_n.
$$


The whole error is eventually nonzero by the distinct-center argument discussed above. Without that dependency, neither (13.1) nor (14.3) alone proves nonvanishing of $\mathcal J(F_n^2)$.

Likewise, for A5’s proportional family the retained identity is


$$
q_nS-p_n=-q_n\epsilon_n,
\qquad
q_n=\frac t\alpha\,\frac{k}{\gcd(k,|r|)}.
$$


Its signed nonvanishing and exponential error rate remain conditional on the supplied proportional analytic theorem. The moving-prime audit does not change that status.

---

# Concluding ledger

## (1) New result and proof status

**Independent review completed:**

* A5’s triangular high-row rank, first two rows modulo $p^2$, falling-metric restriction, binary anisotropy, explicit $D_-$, CRT/Dirichlet progression, saturated weighted Plücker content, and final-$q$ localization all pass on their stated domains.
* A1’s Stieltjes Carleman argument, Gaussian weak convergence, uniform-integrability step, quasi-orthogonal interlacing, and signed stationary inequality pass.
* Endpoint normality, the proportional whole-error theorem, and the dyadic arithmetic theorem retain their inherited status.

**New quantitative deductions proved here:**


$$
|\mathcal J(F_n^2)|\le\theta_n^{-1}\lambda_{\mathcal M},
$$


and, whenever $LH$ is integral and nonsingular,


$$
\theta_n\ge
\frac{|\det(LH)|}
{(28LC_n)^r\det\mathsf H_r}.
$$


These are exact finite-index results, not asymptotic conclusions.

## (2) Exact remaining bottleneck

For A5, the reviewed theorem controls one moving prime and leaves


$$
v_p(q_n)=\max(0,v_p(k)-v_p(r)).
$$


It does not control the aggregate logarithmic denominator budget.

For A1, the remaining sufficient target is still a quantitative bound on the **whole product**


$$
\frac{q_n}{w\theta_n}\lambda_{\mathcal M},
$$


or on its Chebyshev majorant, along an unbounded nonsingular sequence with nonzero whole error. The new spectral floor is explicit, but no useful asymptotic rate for it, the absolute Christoffel quantity, or the actual odd denominator has been proved.

The arithmetic nature of $e+\pi$ remains undecided; neither reviewed route is closed by these results.

## (3) Computation request

**None required.** The polynomial expansions, congruences, and quantitative spectral inequalities above have explicit algebraic proofs. No repetition of the closed eight-prime certificate, and no finite root or eigenvalue scan, is requested.
