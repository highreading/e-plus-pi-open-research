> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A3, Turn 3 — The fixed-degree endpoint defect: a corrected coefficient and actual-form divergence

Let


$$
S=e+\pi,\qquad \sigma=\sqrt2,\qquad M=1+\sqrt2,\qquad \rho=M^{-1},
\qquad d=b-1.
$$


The center is unchanged:


$$
\widehat c
=\frac{n^2}{d}c_0+\left(1-\frac{n^2}{d}\right)c_b,
\qquad c_j=\frac{v_j}{u_j}.
$$



## 1. Main conclusions

**The focused signed-defect lower bound closes.** In fact, the exact finite insertion admits a fixed-$d$ expansion that corrects the suggested coefficient.

For every fixed integer $d\ge2$, on both parities,


$$
\boxed{
\frac{c_0-S}{c_b-S}
=
1-\frac d{n^2}
+\frac{d(2d-3-3\sqrt2)}{n^3}
+O_d(n^{-4}).
}
\tag{1.1}
$$


Consequently,


$$
\boxed{
\frac{\widehat c-S}{c_b-S}
=
\frac{2d-3-3\sqrt2}{n}+O_d(n^{-2}).
}
\tag{1.2}
$$



Thus the coefficient is


$$
\boxed{C_d=2d-3-3\sqrt2,}
\tag{1.3}
$$


not $3(2d-7)/(2\sqrt2)$. In particular,


$$
\boxed{
C_2=1-3\sqrt2,
}
$$


rather than $-9/(2\sqrt2)$.

The calculation below derives this coefficient from the original finite endpoint insertion and the exact full scalar integrals. It does not use the conjectural value, a common-error coefficient from an earlier report, or a growing-parameter Jacobi theorem.

### The focused $d=2$ result

For the actual principal endpoint forces,


$$
\boxed{
\frac{F_0}{P_0}
-\left(1-\frac2{n^2}\right)\frac{F_b}{P_b}
=
\frac{F_b}{P_b}
\left[
\frac{2(1-3\sqrt2)}{n^3}+O(n^{-4})
\right].
}
\tag{1.4}
$$


Hence there is $N$ such that, for every integer $n\ge N$,


$$
\boxed{
\left|
\frac{F_0}{P_0}
-\left(1-\frac2{n^2}\right)\frac{F_b}{P_b}
\right|
\ge
\frac{3\sqrt2-1}{n^3}\left|\frac{F_b}{P_b}\right|.
}
\tag{1.5}
$$


This proves the requested lower bound with $K=3$, on a domain larger than $105\mid n$.

After restoring the **complete exponential and determinant endpoint residuals**, the whole error satisfies


$$
\boxed{
\widehat c-S
=
(-1)^n\,4\pi(3\sqrt2-1)
\frac{M^{-2n-3}}n
\left[1+O(n^{-1})\right]
\qquad(d=2).
}
\tag{1.6}
$$



Using Turn 2’s prime-survival theorem at its exact hypotheses and the actual reduced denominator,


$$
\boxed{
|\widehat qS-\widehat p|\longrightarrow\infty
\qquad(d=2,\ 105\mid n).
}
\tag{1.7}
$$


More precisely, eventually on this progression,


$$
\boxed{
|\widehat qS-\widehat p|
>
\frac{2\pi(3\sqrt2-1)}{11025\,M^3}\,
\frac{2^n}{n^7}.
}
\tag{1.8}
$$



This is an exclusion theorem for these **actual primitive forms**, not merely for a denominator multiplied by an error upper-bound scale.

It is not a proof or disproof of irrationality of $e+\pi$.

---

## 2. Scope and retained exact data

The finite matrices remain


$$
\mathsf T,C,\mathcal S:\{0,\ldots,d\}^2,
\qquad
Z:\{0,\ldots,d+1\}\times\{0,\ldots,d\}.
$$


No matrix is extended beyond its original finite boundary.

The exact insertion supplied in the sources is


$$
R_j(z)
=[t^j](t-1)(1+D_t)^{-n}
\prod_{\ell=1}^d(z_\ell+t/\sigma).
\tag{2.1}
$$


The complete scalar identities are


$$
P_j=\frac{n!}{2\pi}
\int_{-\pi}^{\pi}g_+(s)^nA_j(\sigma+e^{is})\,ds,
\tag{2.2}
$$




$$
F_j=2n!
\int_{-\pi/4}^{\pi/4}g_-(s)^nA_j(\sigma-e^{is})\,ds,
\tag{2.3}
$$


where


$$
g_+(s)=1+\sigma\cos s,\qquad
g_-(s)=\sigma\cos s-1,
$$


and


$$
A_j(q)=\nu_{n,d}\!\left(
R_j(z)\prod_{\ell=1}^d(z_\ell^{-1}+q)
\right).
\tag{2.4}
$$



Up to a common normalization, which cancels in every ratio used below, the full particle functional is integration against


$$
|\Delta(e^{i\theta})|^2
\prod_{\ell=1}^d
g_+(\theta_\ell)^n e^{-\sigma e^{i\theta_\ell}}
\,d\theta_1\cdots d\theta_d,
\qquad -\pi\le\theta_\ell\le\pi.
\tag{2.5}
$$



In particular:

- the factor $e^{-\sigma e^{i\theta_\ell}}$ is retained, not replaced by its modulus;
- the full particle torus is retained;
- the plus scalar interval is $[-\pi,\pi]$;
- the minus scalar interval is exactly $[-\pi/4,\pi/4]$;
- $g_+(\theta)^n$ retains its sign on the outer particle sectors for odd $n$;
- no scalar contour is shortened to an unqualified local saddle model.

The proof is for **fixed $d$**. Constants in $O_d(\cdot)$ can depend on $d$. No uniform claim for growing $d$ is inferred.

---

## 3. The actual finite endpoint insertion

Let $e_r(z)$ denote the elementary symmetric polynomial of degree $r$, with $e_0=1$. Since the product in (2.1) has degree exactly $d$,


$$
R_b=\sigma^{-d}.
\tag{3.1}
$$


Also,


$$
R_0
=-\sum_{k=0}^d(-1)^k n^{\overline k}\sigma^{-k}e_{d-k}(z),
$$


where $n^{\overline k}=n(n+1)\cdots(n+k-1)$. Therefore


$$
\boxed{
R_0=(-1)^{d+1}n^{\overline d}\sigma^{-d}W_{n,d}(z),
}
\tag{3.2}
$$


with the exact finite polynomial


$$
\boxed{
W_{n,d}(z)
=
\sum_{r=0}^d
(-1)^r\sigma^r
\frac{n^{\overline{d-r}}}{n^{\overline d}}e_r(z).
}
\tag{3.3}
$$



For the focused case $d=2$, this is simply


$$
\boxed{
W_{n,2}
=
1-\frac{\sigma}{n+1}(z_1+z_2)
+\frac{\sigma^2}{n(n+1)}z_1z_2.
}
\tag{3.4}
$$


There is no omitted higher-degree insertion in this case.

Define $\mathbb E_\epsilon$, $\epsilon\in\{+1,-1\}$, as the normalized **full joint scalar-particle integral** with scalar variable $s$, factor


$$
g_\epsilon(s)^n
\prod_{\ell=1}^d
\bigl(e^{-i\theta_\ell}+\sigma+\epsilon e^{is}\bigr),
\tag{3.5}
$$


and particle weight (2.5). The scalar intervals are those in (2.2)–(2.3).

These are algebraic normalized complex integrals, not positive expectations. Their denominators are nonzero for sufficiently large $n$, as follows from the fixed-dimensional leading term proved below.

Equations (2.2)–(3.3) give the exact identity


$$
\boxed{
\frac{F_0/P_0}{F_b/P_b}
=
\frac{\mathbb E_-W_{n,d}}{\mathbb E_+W_{n,d}}.
}
\tag{3.6}
$$



This is the endpoint contrast that must be expanded. A common expansion of $F_j/P_j$, by itself, would not answer the assignment.

---

## 4. A controlled fixed-degree moment calculation

Set


$$
\alpha=\frac{\sigma}{M}=2-\sigma,
\qquad
a_4=\frac{\alpha}{24}-\frac{\alpha^2}{8}.
\tag{4.1}
$$


Near zero,


$$
\log g_+(\theta)
=\log M-\frac{\alpha\theta^2}{2}+a_4\theta^4+O(\theta^6).
\tag{4.2}
$$



We first hold the characteristic parameter $q$ fixed near either $M$ or $\rho$, and write


$$
p=\frac1{1+q}.
$$


Let $\mathbb E_q$ denote the normalized full particle integral with insertion
$\prod_\ell(e^{-i\theta_\ell}+q)$.

### 4.1 Conditional first and second elementary moments

The needed expansions are


$$
\mathbb E_q e_1
=d+\frac{m_1(p)}n+\frac{m_2(p)}{n^2}+O_d(n^{-3}),
\tag{4.3}
$$


and


$$
\mathbb E_q e_2
=\binom d2+\frac{h_1(p)}n+O_d(n^{-2}),
\tag{4.4}
$$


uniformly in fixed complex neighborhoods of the two anchors. Their first coefficients are


$$
\boxed{
m_1(p)=\frac d\alpha\left(\sigma+p-\frac d2\right),
}
\tag{4.5}
$$




$$
\boxed{
h_1(p)
=\frac{d(d-1)}\alpha
\left(\sigma+p-\frac{d-1}{2}\right).
}
\tag{4.6}
$$



Here is an explicit derivation of the second coefficient needed for the contrast.

Put


$$
X=\sum_\ell\theta_\ell,\qquad Q_r=\sum_\ell\theta_\ell^r,
$$


and


$$
c=\sigma+p,\qquad
u=\frac{\sigma-p+p^2}{2},\qquad
v=\frac{\sigma+p-3p^2+2p^3}{6}.
\tag{4.7}
$$


The logarithm of the complete one-particle amplitude is


$$
-\sigma e^{i\theta}+\log(e^{-i\theta}+q)
=
\text{constant}-ic\theta+u\theta^2+iv\theta^3+O(\theta^4).
\tag{4.8}
$$



The circular Vandermonde correction is


$$
|\Delta(e^{i\theta})|^2
=
\Delta(\theta)^2
\left[
1-\frac{dQ_2-X^2}{12}+O_d(\|\theta\|^4)
\right].
\tag{4.9}
$$


This correction is essential at the requested order.

Use the Gaussian eigenvalue measure proportional to


$$
\Delta(\theta)^2
\exp\!\left(-\frac{\alpha n}{2}Q_2\right)d\theta.
$$


For $t=(\alpha n)^{-1}$, its exact moments are


$$
\begin{array}{c|c}
\text{quantity}&\text{value}\\ \hline
\mathbb E X^2&dt\\
\mathbb E Q_2&d^2t\\
\operatorname{Var}(X^2)&2d^2t^2\\
\operatorname{Cov}(X^2,Q_2)&2dt^2\\
\operatorname{Var}(Q_2)&2d^2t^2\\
\mathbb E(XQ_3)&3d^2t^2\\
\mathbb E Q_4&(2d^3+d)t^2\\
\operatorname{Cov}(X^2,Q_4)&12d^2t^3\\
\operatorname{Cov}(Q_2,Q_4)&4(2d^3+d)t^3.
\end{array}
\tag{4.10}
$$



These are finite Gaussian identities, not a universality assumption. For example, the three Wick pairings give
$\mathbb E\operatorname{Tr}H^4=(2d^3+d)t^2$; Gaussian integration by parts in the identity-matrix direction gives the $XQ_3$ and $X^2,Q_4$ identities; radial scaling gives the $Q_2,Q_4$ covariance.

Expand


$$
e_1=d+iX-\frac{Q_2}{2}-\frac{iQ_3}{6}+\frac{Q_4}{24}+\cdots.
\tag{4.11}
$$


With $U=u-d/12$, the normalized order-$n^{-2}$ contribution is


$$
\begin{aligned}
\frac{m_2(p)}{n^2}
={}&-\left(v+\frac c6\right)\mathbb E(XQ_3)\\
&+\left(cU-\frac1{24}+\frac{c^2}{4}\right)
  \operatorname{Cov}(X^2,Q_2)
+\frac c{12}\operatorname{Var}(X^2)
-\frac U2\operatorname{Var}(Q_2)\\
&+na_4\left[
c\,\operatorname{Cov}(X^2,Q_4)
-\frac12\operatorname{Cov}(Q_2,Q_4)
\right]
+\frac1{24}\mathbb E Q_4.
\end{aligned}
\tag{4.12}
$$


The apparent cubic term in $c$ cancels because
$\mathbb E X^4=3(\mathbb E X^2)^2$.

Substituting (4.10) yields


$$
\boxed{
\begin{aligned}
m_2(p)
={}&\frac1{\alpha^2}
\left[
-3d^2v+(2dc-d^2)u+\frac{dc^2}{2}
-\frac{cd^2}{2}+\frac{4d^3-d}{24}
\right]\\
&+\frac{a_4}{\alpha^3}
\left[12cd^2-4d^3-2d\right].
\end{aligned}
}
\tag{4.13}
$$



This retains the exponential phase, the characteristic phase, the circular Vandermonde correction, and the quartic correction to the particle saddle.

### 4.2 Why the remainder is controlled

For fixed $d$, the preceding calculation is a standard finite-dimensional Laplace expansion with an explicit domination argument:

1. Outside a fixed neighborhood of $\theta=0$,
   

$$
|g_+(\theta)|\le M(1-\delta)
$$


   for some $\delta>0$. Thus all full outer sectors, including the sectors where $g_+^n$ is negative for odd $n$, contribute an exponentially small relative error after allowing for a fixed polynomial in $n$.

2. Near zero, the quotient
   

$$
\frac{|\Delta(e^{i\theta})|^2}{\Delta(\theta)^2}
$$


   is analytic, with removable collision singularities.

3. After $\theta=n^{-1/2}y$, Taylor expansion through the required order is dominated by a Gaussian times a fixed polynomial. A cutoff such as $\|y\|\le n^{1/20}$ leaves an exponentially small Gaussian tail.

4. Terms of odd total scaled degree integrate to zero. Expanding through scaled degree five therefore leaves $O_d(n^{-3})$ in (4.3).

5. The normalized particle denominator has a nonzero leading term proportional to
   

$$
e^{-\sigma d}(1+q)^dM^{nd}n^{-d^2/2}.
$$


   Division is therefore legitimate uniformly in sufficiently small complex neighborhoods of the two anchors.

This proves the stated $O_d(n^{-3})$ and $O_d(n^{-2})$ remainders, rather than merely assigning formal coefficients.

---

## 5. The scalar correction must also be retained

A fixed-anchor particle calculation alone is not enough: the scalar variable changes


$$
q(s)=\sigma+\epsilon e^{is}.
$$


Put


$$
q_\epsilon=\sigma+\epsilon,\qquad
p_\epsilon=\frac1{1+q_\epsilon},\qquad
\beta_\epsilon=\frac{\sigma}{\sigma+\epsilon}.
\tag{5.1}
$$


Thus


$$
p_-=\frac1\sigma,\qquad
p_+=\frac1{2+\sigma},\qquad
\beta_+=\alpha,\qquad
\beta_-=2+\sigma.
$$



The leading scalar amplitude from the particle integral is
$(1+q(s))^d$. Its logarithmic linear term is
$id\epsilon p_\epsilon s$. Accordingly,


$$
\langle s\rangle
=\frac{id\epsilon p_\epsilon}{\beta_\epsilon n}
+O_d(n^{-2}),
\qquad
\langle s^2\rangle
=\frac1{\beta_\epsilon n}+O_d(n^{-2}).
\tag{5.2}
$$


It follows that


$$
\left\langle q(s)-q_\epsilon\right\rangle
=
-\frac{dp_\epsilon+\epsilon/2}{\beta_\epsilon n}
+O_d(n^{-2}),
\tag{5.3}
$$




$$
\left\langle(q(s)-q_\epsilon)^2\right\rangle
=
-\frac1{\beta_\epsilon n}+O_d(n^{-2}).
\tag{5.4}
$$



Since


$$
m_1'(q)=-\frac d\alpha p^2,\qquad
m_1''(q)=\frac{2d}\alpha p^3,
$$


the scalar contribution to the coefficient of $n^{-2}$ in
$\mathbb E_\epsilon e_1$ is


$$
\boxed{
s_2(\epsilon)
=
\frac d{\alpha\beta_\epsilon}
\left[(d-1)p_\epsilon^3+\frac{\epsilon p_\epsilon^2}{2}\right].
}
\tag{5.5}
$$



The same localization argument applies on the original scalar intervals. On the minus interval, $g_-$ vanishes at the original endpoints; on the plus interval, the absolute maximum is uniquely at zero. No unaccounted connector or endpoint contribution is introduced.

Conditional particle quotients are used only near the scalar saddle, where their denominators are nonzero. Remote contributions are bounded in their original unnormalized integral form.

---

## 6. Exact simplification of the endpoint contrast

Write $\Delta f=f_- -f_+$. The elementary identities


$$
p_-+p_+=1,\qquad
\Delta p=\rho,\qquad
\Delta(p^2)=\rho,\qquad
\Delta(p^3)=\rho\,\frac{3-\sigma}{2}
\tag{6.1}
$$


make the calculation short.

### 6.1 First-order difference

From (4.5),


$$
\boxed{
\Delta m_1=\frac d\sigma.
}
\tag{6.2}
$$



### 6.2 Second-order difference

First, the conditional particle coefficient (4.13) gives


$$
\boxed{
\Delta m_2^{\rm particle}
=
\frac{dM}{4}\left[2+3\sigma+d(4\sigma-7)\right].
}
\tag{6.3}
$$


The scalar correction (5.5) gives


$$
\boxed{
\Delta s_2=\frac d4\left[(d-1)\rho-1\right].
}
\tag{6.4}
$$


Adding them,


$$
\boxed{
\Delta m_2^{\rm joint}
=
2d+\frac{\sigma d(2-d)}2.
}
\tag{6.5}
$$



Thus the full joint moments satisfy


$$
\boxed{
\mathbb E_-e_1-\mathbb E_+e_1
=
\frac d{\sigma n}
+\frac{2d+\sigma d(2-d)/2}{n^2}
+O_d(n^{-3}).
}
\tag{6.6}
$$


Likewise, from (4.6),


$$
\boxed{
\mathbb E_-e_2-\mathbb E_+e_2
=
\frac{d(d-1)}{\sigma n}+O_d(n^{-2}).
}
\tag{6.7}
$$



For $d=2$, these simplify to the especially small certificate


$$
\boxed{
\mathbb E_-e_1-\mathbb E_+e_1
=\frac{\sqrt2}{n}+\frac4{n^2}+O(n^{-3}),
}
\tag{6.8}
$$




$$
\boxed{
\mathbb E_-e_2-\mathbb E_+e_2
=\frac{\sqrt2}{n}+O(n^{-2}).
}
\tag{6.9}
$$



### 6.3 Substitute into the actual finite insertion

For fixed $d$,


$$
W_{n,d}
=
1-\frac{\sigma}{n+d-1}e_1
+\frac{\sigma^2}{(n+d-2)(n+d-1)}e_2+\cdots.
\tag{6.10}
$$


For $r\ge3$, both joint expectations of $e_r$ equal
$\binom dr+O_d(n^{-1})$, so the omitted terms contribute only
$O_d(n^{-4})$ to the **difference** of the two expectations.

Equations (6.6)–(6.7) give


$$
\mathbb E_-W_{n,d}-\mathbb E_+W_{n,d}
=
-\frac d{n^2}
+\frac{d[\,2d-3+\sigma(d-3)\,]}{n^3}
+O_d(n^{-4}).
\tag{6.11}
$$


Also,


$$
\mathbb E_+W_{n,d}
=1-\frac{\sigma d}{n}+O_d(n^{-2}).
\tag{6.12}
$$


Dividing,


$$
\boxed{
\frac{\mathbb E_-W_{n,d}}{\mathbb E_+W_{n,d}}
=
1-\frac d{n^2}
+\frac{d(2d-3-3\sigma)}{n^3}
+O_d(n^{-4}).
}
\tag{6.13}
$$



Together with the exact identity (3.6), this proves the third-order principal endpoint contrast.

For $d=2$, the insertion (3.4) is exact, and the two decisive coefficients are particularly transparent:


$$
\mathbb E_-W_{n,2}-\mathbb E_+W_{n,2}
=
-\frac2{n^2}+\frac{2-2\sigma}{n^3}+O(n^{-4}),
$$


while division by


$$
\mathbb E_+W_{n,2}=1-\frac{2\sigma}{n}+O(n^{-2})
$$


changes the cubic coefficient to $2-6\sigma$. Hence


$$
\frac{F_0/P_0}{F_b/P_b}
=
1-\frac2{n^2}+\frac{2-6\sqrt2}{n^3}+O(n^{-4}).
$$



This is the requested threshold separation, not another common-error coefficient.

---

## 7. Restoring the complete whole error

The exact whole coordinate error remains


$$
e_j:=c_j-S
=
\frac{E_j}{P_j}
+(-1)^{n+1}\frac{F_j}{P_j}
+(-1)^n\delta_{j0}\frac{D}{P_j},
\qquad D=\det H_b.
\tag{7.1}
$$


The exponential force is the complete one:


$$
eE_i
=
-[z^{n+i}]Q(z)^n
\int_0^1s^ne^{1-s+sz}\,ds,
\qquad Q(z)=1-z+\frac{z^2}{2},
\tag{7.2}
$$




$$
E_j=
\nu_{n,d}\!\left(
R_j\sum_{i=0}^d\sigma^i e_{d-i}(z^{-1})eE_i
\right).
\tag{7.3}
$$



With $\lambda=n^2/d$,


$$
\boxed{
\begin{aligned}
\widehat c-S
={}&(-1)^{n+1}
\left[
\lambda\frac{F_0}{P_0}
+(1-\lambda)\frac{F_b}{P_b}
\right]\\
&+\lambda\frac{E_0}{P_0}
+(1-\lambda)\frac{E_b}{P_b}
+(-1)^n\lambda\frac{D}{P_0}.
\end{aligned}
}
\tag{7.4}
$$


In particular, coordinate zero’s exterior $+1$ has not disappeared.

The accepted complete factorial residual bound is


$$
\begin{aligned}
|\mathcal R_{n,d}|
:={}&
\left|
\lambda\frac{E_0}{P_0}
+(1-\lambda)\frac{E_b}{P_b}
+(-1)^n\lambda\frac{D}{P_0}
\right|\\
\le{}&
C(2\lambda-1)\frac{2^d}{n!\sqrt n}
+C\lambda\frac{\sqrt n}{n!B_0},
\qquad
B_0=n^{\overline d}\sigma^{-d}.
\end{aligned}
\tag{7.5}
$$


For fixed $d\ge2$,


$$
\boxed{
|\mathcal R_{n,d}|=O_d(n^{3/2}/n!).
}
\tag{7.6}
$$


This estimate is applied **after** amplification by the signed coefficients.

### 7.1 Fixed-degree endpoint size

The same fixed-dimensional Laplace calculation gives


$$
\boxed{
\frac{F_b}{P_b}
=
4\pi M^{-2n-d-1}\left[1+O_d(n^{-1})\right].
}
\tag{7.7}
$$


Indeed:

- the scalar exponential ratio is $(\rho/M)^n=M^{-2n}$;
- the characteristic leading-amplitude ratio is
  

$$
\left(\frac{1+\rho}{1+M}\right)^d=M^{-d};
$$


- the scalar Gaussian curvature ratio is
  

$$
\sqrt{\beta_+/\beta_-}=M^{-1};
$$


- the original scalar normalization ratio is $4\pi$.

All full outer sectors are exponentially smaller for fixed $d$.

Since factorial decay beats $M^{-2n}$ times every fixed power of $n^{-1}$, the residuals in (7.1) can be absorbed into the $O_d(n^{-4})$ endpoint-ratio remainder. This proves the whole-error statements (1.1)–(1.2).

### 7.2 Full fixed-degree even/odd law

Combining (6.13), (7.4), and (7.7),


$$
\boxed{
\widehat c-S
=
(-1)^{n+1}4\pi C_d\,
\frac{M^{-2n-d-1}}n
\left[1+O_d(n^{-1})\right],
\qquad C_d=2d-3-3\sqrt2.
}
\tag{7.8}
$$


There is no zero coefficient at an integer $d$, because $\sqrt2$ is irrational.

For the actual primitive pair,


$$
\boxed{
\widehat qS-\widehat p
=
(-1)^n4\pi C_d\,\widehat q
\frac{M^{-2n-d-1}}n
\left[1+O_d(n^{-1})\right].
}
\tag{7.9}
$$



The sign transition is therefore:

| Fixed degree | $C_d$ | Eventual sign of $\widehat c-S$ |
|---|---:|---|
| $d=2$ | $1-3\sqrt2<0$ | $(-1)^n$ |
| $d=3$ | $3-3\sqrt2<0$ | $(-1)^n$ |
| $d=4$ | $5-3\sqrt2>0$ | $(-1)^{n+1}$ |
| $d\ge4$ | positive | $(-1)^{n+1}$ |

Thus the observed $d=3/d=4$ sign change is rigorous. The actual coefficient changes sign at the noninteger threshold


$$
d=\frac{3+3\sqrt2}{2},
$$


not at $d=7/2$.

---

## 8. The precise signed-threshold separation

Retain Turn 1’s notation


$$
x=\frac d{n^2},\qquad
r_{n,d}=\log(e_0/e_b)+x.
$$


From (1.1),


$$
r_{n,d}
=\frac{dC_d}{n^3}+O_d(n^{-4}).
\tag{8.1}
$$


The exact zero threshold is


$$
r_*(x)=x+\log(1-x)
=-\frac{d^2}{2n^4}+O_d(n^{-6}).
$$


Therefore


$$
\boxed{
r_{n,d}-r_*(d/n^2)
=
\frac{dC_d}{n^3}+O_d(n^{-4}).
}
\tag{8.2}
$$



For $d=2$,


$$
r_{n,2}-r_*(2/n^2)
=
-\frac{2(3\sqrt2-1)}{n^3}+O(n^{-4}).
\tag{8.3}
$$


The actual remainder is thus separated from the zero threshold by order $n^{-3}$.

This resolves the precise obstruction identified in Turns 1–2: the CSC uncertainty allowed the zero threshold, whereas the explicit fixed-degree calculation determines which side of that threshold the actual system occupies.

The earlier nonconstancy theorem is not reproved here. The new result supplies the quantitative magnitude that nonconstancy could not supply.

---

## 9. The actual primitive denominator and divergence on $105\mid n$

Nothing in the analytic calculation changes the rational center or its primitive normalization.

Let $d_B$ be the least actual two-column clearer and


$$
U=d_Bu,\qquad V=d_Bv.
$$


Reduce the two endpoint rows:


$$
r_0=\gcd(|U_0|,|V_0|),\qquad
r_b=\gcd(|U_b|,|V_b|),
$$




$$
(\widetilde u_j,\widetilde v_j)=(U_j/r_j,V_j/r_j).
$$


Set


$$
h=\gcd(|\widetilde u_0|,|\widetilde u_b|),
\qquad
\widetilde u_0=hA,\quad \widetilde u_b=hB,
$$


and


$$
g=\gcd(n^2,d),\qquad a=n^2/g,\qquad k=d/g,
$$




$$
J=B\widetilde v_0-A\widetilde v_b,\qquad
T=aJ+kA\widetilde v_b.
$$


The complete cancellation factors remain


$$
F=\gcd(|A|,a)\gcd(|B|,a-k),\qquad
G=\gcd(k,|J|),
$$




$$
H_{\rm gcd}=\gcd\!\left(h,\frac{|T|}{FG}\right).
$$


The audited exact primitive formula is


$$
\boxed{
\widehat q=\frac{kh|AB|}{FGH_{\rm gcd}},
\qquad
\widehat p=\operatorname{sgn}(AB)\frac{T}{FGH_{\rm gcd}}.
}
\tag{9.1}
$$



At $d=2$, both coefficient normalizations occur:


$$
(a,k)=
\begin{cases}
(n^2/2,1),&n\ \text{even},\\
(n^2,2),&n\ \text{odd}.
\end{cases}
\tag{9.2}
$$


Neither parity is discarded.

### 9.1 Exact scope of prime-survival reuse

Turn 2’s theorem assumes


$$
p>d,\qquad p\mid n,\qquad \tau_nD_d\not\equiv0\pmod p.
$$


Its proof uses the complete force to obtain a unit companion entry at $b$, a divisible companion entry at $0$, and unit normalized quantities $J,T$. Thus it explicitly accounts for the final shared-content gcd; it is not an inference from the empirical size of $H_{\rm gcd}$.

For $d=2$, $D_2=1$, and the proved digit transfers make $p=3,5,7$ available at every multiple of $105$. Consequently,


$$
\boxed{
v_p(\widehat q)=2v_p(n!)\qquad(p=3,5,7;\ 105\mid n).
}
\tag{9.3}
$$


The resulting lower bound is


$$
\widehat q\ge
\frac{\exp(L_2n)}{11025\,n^6},
\qquad
L_2=\log3+\frac12\log5+\frac13\log7.
\tag{9.4}
$$


As proved in Turn 2,


$$
\boxed{
\frac{\widehat qM^{-2n-3}}n
>
\frac{2^n}{11025\,M^3n^7}.
}
\tag{9.5}
$$



### 9.2 Whole primitive-form divergence

Equation (1.6), including the complete residual, implies eventually


$$
|\widehat c-S|
\ge
2\pi(3\sqrt2-1)\frac{M^{-2n-3}}n.
$$


Multiplication by the actual denominator (9.1), followed by (9.5), proves (1.8).

The parity-resolved conclusion is


$$
\boxed{
\begin{aligned}
\widehat qS-\widehat p&\longrightarrow-\infty
&&\text{through even multiples of }105,\\
\widehat qS-\widehat p&\longrightarrow+\infty
&&\text{through odd multiples of }105.
\end{aligned}
}
\tag{9.6}
$$



This is stronger than Turn 2’s denominator-budget obstruction: it concerns the whole evaluated actual primitive forms.

The same fixed-degree law also combines with Turn 2’s $385\mid n$ denominator lower bound to give


$$
|\widehat qS-\widehat p|\to\infty
\qquad(d=3,4,\ 385\mid n).
$$


That is a corollary, not needed for the focused $d=2$ closure.

---

## 10. What the finite receipt does—and does not—establish

The receipt’s exact fraction and gcd comparisons retain their stated finite scope. Its decimal error ratios are not used in the proof.

For comparison only, the newly derived limit at $d=2$ is


$$
1-3\sqrt2\approx-3.242640687,
$$


whereas the proposed value was approximately $-3.181980515$. The displayed finite scaled ratios need not equal either limit; the rigorous error term in (1.2) is $O_d(n^{-2})$, so their products with $n$ have an $O_d(n^{-1})$ correction.

The specialized coefficient follows from Sections 3–6, not from extrapolating those finitely many ratios.

No tools, files, endpoints, or credentials were accessed. The supplied code was treated as mathematical source data.

---

## 11. Bounded exact arithmetic for independent inspection

No numerical computation is required to complete the proof above. A small exact symbolic certificate would nevertheless be useful for independent review.

### 11.1 Primary coefficient certificate

**Inputs**

Work in $\mathbb Q(\sigma)$, with


$$
\sigma^2=2,\qquad \sigma>0,
$$


and use


$$
\alpha=2-\sigma,\quad
a_4=\alpha/24-\alpha^2/8,
$$




$$
p_-=\sigma/2,\quad p_+=(2-\sigma)/2,\quad
\beta_-=2+\sigma,\quad\beta_+=2-\sigma.
$$


Take $d=2$. Use $m_1,m_2,h_1,s_2$ from
(4.5), (4.13), (4.6), and (5.5).

**Expected exact output**


$$
m_1(p_-)-m_1(p_+)=\sigma,
$$




$$
[m_2(p_-)+s_2(-)]-[m_2(p_+)+s_2(+)]=4,
$$




$$
h_1(p_-)-h_1(p_+)=\sigma.
$$


Then substitute these into the exact insertion


$$
1-\frac{\sigma e_1}{n+1}
+\frac{2e_2}{n(n+1)}.
$$



The expected endpoint-ratio coefficients are


$$
\boxed{
[n^{-2}]=-2,\qquad [n^{-3}]=2-6\sigma,
}
$$


and the extrapolated relative coefficient is


$$
\boxed{1-3\sigma.}
$$



An optional symbolic-$d$ check should return


$$
\Delta m_2^{\rm joint}=2d+\frac{\sigma d(2-d)}2,
\qquad
[n^{-3}]\frac{\mathbb E_-W}{\mathbb E_+W}
=d(2d-3-3\sigma).
$$



This certificate checks finite algebra. The localization argument in Section 4.2, not the symbolic calculation alone, establishes the asymptotic remainder.

### 11.2 Optional actual-pair check on the requested progression

Use the complete finite producer at


$$
(n,d)=(105,2),\qquad(210,2).
$$


Retain the exterior $+1$, all force coefficients through $2n+d$, the least actual clearer, both row contents, and the full final gcd.

The expected exact denominator-valuation outputs are


$$
\begin{array}{c|ccc}
n&v_3(\widehat q)&v_5(\widehat q)&v_7(\widehat q)\\ \hline
105&100&50&34\\
210&204&102&68.
\end{array}
$$


Also compare direct single-gcd fraction reduction with (9.1).

If desired, use the prescribed 512-term rational bounds for $e$ and Machin’s formula for $\pi$ to return rational intervals for


$$
\widehat c-S,\qquad
\widehat qS-\widehat p,\qquad
n\,\frac{\widehat c-S}{c_b-S}.
$$


Those intervals certify only the two chosen finite records. They are not needed to infer the eventual theorem, and an interval containing zero must remain inconclusive.

---

## 12. Final proof ledger

### New results proved

1. **A controlled fixed-degree third-order endpoint contrast**
   

$$
\frac{c_0-S}{c_b-S}
   =
   1-\frac d{n^2}
   +\frac{d(2d-3-3\sqrt2)}{n^3}
   +O_d(n^{-4}).
$$



2. **Correction of the suggested coefficient**
   

$$
n\frac{\widehat c-S}{c_b-S}
   \longrightarrow 2d-3-3\sqrt2.
$$



3. **The focused $d=2$ signed-defect lower bound**, with $K=3$, retaining the exact finite endpoint insertion.

4. **The complete even/odd whole-error law**, including the amplified exponential force and determinant endpoint residual.

5. **Actual primitive-form divergence**
   

$$
|\widehat qS-\widehat p|\to\infty
   \qquad(d=2,\ 105\mid n),
$$


   using the actual denominator after every gcd cancellation.

6. **A rigorous explanation of the $d=3/d=4$ sign change.**

### Exact remaining mathematical bottleneck

The signed-defect bottleneck for $d=2$ on $105\mid n$ is now closed. On that progression, the construction produces whole primitive forms that diverge, not forms that tend to zero.

The global irrationality objective still requires a different infinite original-index family, or a different construction, producing


$$
0<|q(e+\pi)-p|\longrightarrow0,
$$


with its actual primitive denominator and complete evaluated error controlled. The present divergence theorem does not exclude all other allocations or all other constructions.



$$
\boxed{
\text{The irrationality or rationality of }e+\pi\text{ remains unresolved.}
}
$$


