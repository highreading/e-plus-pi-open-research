> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

## A3 continuation: a structured-residual estimate, a narrow factorization obstruction, and a rational varying filter

I do not obtain an irrationality proof for $S=e+\pi$. In particular, I do **not** obtain the requested common index-moment representation for the actual complete $b=2$ errors.

There is nevertheless a quantitative advance over the adversarial residual bound: for residuals having a specified signed Laplace-moment structure, the filtered residual is smaller than the $1/k$ model by $O((m+1)/n)$, uniformly for $m=o(n)$. This is a proved model theorem, **not** a representation theorem for the actual errors. I also prove a narrow obstruction to factoring the actual exponential-tail kernels by a single index-independent amplitude, and give a different rational varying filter with an exact whole-error identity.

### 1. Domain and retained endpoint normalization

Use the actual $b=2$ family, and write


$$
X_k=A_k(1),\qquad Y_k=B_k(1)=C_k(1),\qquad
r_k=-X_k/Y_k,\qquad E_k=S-r_k.
$$


All statements about these quotients are on


$$
k\ge2,\qquad Y_k\ne0.
$$


The supplied eventual-normality theorem gives an unspecified $N_*$ such that this holds for every $k\ge N_*$.

The exact cofactor equations remain


$$
\sum_{\ell=0}^2a_{k,\ell}B_{k,\ell}=0,\qquad
\sum_{\ell=0}^2(1+t_{k,\ell})B_{k,\ell}=0,
$$


and


$$
E_k=\frac{\ell_{B_k}(W_k)}{Y_k}.
$$


Thus neither the cofactor dependence on $k$ nor the endpoint divisor is discarded.

For arithmetic, write $r_k=p_k/q_k$ in lowest terms, $q_k>0$. Equivalently, the supplied contiguous arithmetic reduction gives


$$
q_k=
\frac{|\Lambda_k\mathscr D_k|}
{\gcd(|\Lambda_k\mathscr D_k|,|\mathscr N_k|)}.
$$


This is the actual denominator, not a coefficient clearer.

---

## 2. Quantitative structured-residual lemma

Put


$$
s=3-2\sqrt2,\qquad z=-s,\qquad a=s^2,
$$


and


$$
g(T)=1+6T+T^2,\qquad
g(T)^m=\sum_{j=0}^{2m}a_{m,j}T^j.
$$


Then


$$
g(zx)=(1-x)(1-ax).
$$



The previously supplied beta identity is reused, not claimed as new:


$$
I_{n,m}
=\frac1{8^m}\int_0^1x^{n-1}(1-x)^m(1-ax)^m\,dx>0.
$$



For integers $h\ge1$, define


$$
J_h(n,m)=\frac1{8^m}\sum_{j=0}^{2m}
\frac{a_{m,j}z^j}{(n+j)^h}.
$$


The elementary Laplace identity gives


$$
J_h(n,m)=
\frac1{8^m(h-1)!}\int_0^1
x^{n-1}(-\log x)^{h-1}(1-x)^m(1-ax)^m\,dx.
\tag{1}
$$


In particular, all these quantities are positive.

### Lemma 1 — Uniform relative bound for every inverse-power correction

For $m\ge1$, $h\ge2$, and $n>h-1$,


$$
\boxed{
0<\frac{J_h(n,m)}{I_{n,m}}
\le
\frac{(2m+1)_{h-1}}
{(h-1)!\,(n-1)(n-2)\cdots(n-h+1)}.
}
\tag{2}
$$


Here $(u)_r=u(u+1)\cdots(u+r-1)$.

In particular,


$$
\boxed{
J_2(n,m)\le \frac{2m+1}{n-1}I_{n,m}.
}
\tag{3}
$$



#### Proof

Expand


$$
(1-ax)^m=\bigl((1-a)+a(1-x)\bigr)^m
=\sum_{\ell=0}^m
\binom m\ell(1-a)^{m-\ell}a^\ell(1-x)^\ell.
$$


All coefficients are nonnegative. Consequently, the probability measure proportional to


$$
x^{n-1}(1-x)^m(1-ax)^m\,dx
$$


is a positive mixture of beta distributions with parameters


$$
(n,m+\ell+1),\qquad 0\le\ell\le m.
$$



For $0<x\le1$,


$$
-\log x\le \frac{1-x}{x}.
$$


For a beta distribution with parameters $(n,b)$, and an integer $r<n$,


$$
\mathbb E\left[\left(\frac{1-X}{X}\right)^r\right]
=\frac{B(n-r,b+r)}{B(n,b)}
=\frac{(b)_r}{(n-1)\cdots(n-r)}.
$$


Here $b=m+\ell+1\le2m+1$. Apply this with $r=h-1$, average over the positive mixture, and divide by $(h-1)!$, as prescribed by (1). ∎

This estimate controls the **filtered** residual rather than the absolute size of its individual terms. For every fixed $h$,


$$
\frac{J_h(n,m)}{I_{n,m}}
=O_h\!\left(\left(\frac{m+1}{n}\right)^{h-1}\right)
$$


uniformly when $m=o(n)$.

### Corollary — Signed density residuals

Suppose a sequence has the exact representation


$$
E_k=Cz^k\left(1+\frac{A}{k}
+\int_0^1x^{k-1}f(x)\,dx\right),
\tag{4}
$$


where $C,A$ are fixed, and


$$
|f(x)|\le M(-\log x)\qquad(0<x<1).
\tag{5}
$$


Then, for every $n>1,m\ge1$,


$$
\boxed{
\left|
\frac{8^{-m}\sum_j a_{m,j}E_{n+j}}{Cz^n}
-AI_{n,m}
\right|
\le
M\frac{2m+1}{n-1}I_{n,m}.
}
\tag{6}
$$



Indeed, finite summation can be passed inside the integral in (4); its multiplier is exactly $g(zx)^m/8^m$, which is nonnegative on $[0,1]$. Equations (5) and (3) then prove (6).

If $CA\ne0$ and


$$
M(2m+1)<|A|(n-1),
\tag{7}
$$


the whole filtered error is nonzero and has sign


$$
\operatorname{sign}(CA)(-1)^n.
$$



**What is gained:** under the explicitly specified structure, a uniform sublinear window follows from an ordinary $O(-\log x)$ density bound. One does not need an exponentially accurate pointwise bound on the residual sequence.

**What is not gained:** no supplied source establishes (4)–(5) for the actual $b=2$ errors. Even the existence of a suitable exact common signed density remains open here.

---

## 3. Narrow obstruction: the exponential-tail amplitude is not index-independent

The full error contains the exponential-tail contribution


$$
E_k^{\exp}
=\int_0^1 e^x(1-x)^{2k}P_k(1-x)\,dx,
$$


where


$$
P_k(t)=
\frac1{Y_k}
\left(
\frac{B_{k,2}}{(2k)!}
+\frac{B_{k,1}}{(2k+1)!}t
+\frac{B_{k,0}}{(2k+2)!}t^2
\right).
\tag{8}
$$


The logarithmic-tail contribution must still be added to obtain $E_k$.

A tempting factorization is


$$
P_k(t)=P(t)
\quad\text{for all sufficiently large }k,
\tag{9}
$$


which would let an index filter act directly on the power $(1-x)^{2k}$. This particular factorization is false.

### Lemma 2 — Failure of the fixed-amplitude exponential-tail factorization

For the actual eventually normalized $b=2$ family, the coefficient


$$
P_k(0)=\frac{B_{k,2}}{Y_k(2k)!}
$$


is nonzero eventually and tends to zero. Hence (9) cannot hold.

#### Proof

Normalize $B_{k,0}=1$. The supplied factorial-functional asymptotics and the raw cross product imply


$$
B_{k,2}\sim \frac1k.
$$


Indeed, in raw scale,


$$
B_{k,2}=a_0(1+t_1)-a_1(1+t_0)
\sim-\frac{U(0)e^{-\sqrt2}}{k!},
$$


whereas


$$
B_{k,0}\sim-\frac{kU(0)e^{-\sqrt2}}{k!}.
$$



The supplied endpoint asymptotic is


$$
Y_k\sim
-\left(1+\frac1{\sqrt2}\right)
\frac{e^{-\sqrt2}V_k(0)}{k^2k!}.
$$


The exact Christoffel–Darboux endpoint expression and the endpoint-ratio limits in that source give


$$
\log V_k(0)=O(k).
$$


Therefore


$$
\log\left|\frac{B_{k,2}}{Y_k(2k)!}\right|
=\log(k!)-\log((2k)!)+O(k+\log k)
=-k\log k+O(k).
$$


It tends to $-\infty$, while all factors are nonzero eventually. Thus $P_k(0)$ cannot equal one fixed constant for all sufficiently large $k$. ∎

This is deliberately narrow. It excludes a **pointwise common amplitude for the separate exponential-tail kernels**. It does not exclude a common representation obtained after combining both tails, changing variables, or introducing additional signed measures.

The endpoint divisor $Y_k$ is essential in this obstruction.

---

## 4. A different rational varying filter

A useful alternative to merely repeating $g(E)/8$ is to attach an index polynomial before filtering.

For $m\ge1$, put


$$
D_{n,m}=\sum_{j=0}^{2m}a_{m,j}(n+j)^{m-1}>0,
$$


and define


$$
\boxed{
\widetilde c_{n,m}
=\frac1{D_{n,m}}
\sum_{j=0}^{2m}a_{m,j}(n+j)^{m-1}r_{n+j}.
}
\tag{10}
$$


These are rational convex combinations, with coefficients varying rationally with $n$.

Their exact whole-error identity is


$$
\boxed{
S-\widetilde c_{n,m}
=\frac1{D_{n,m}}\sum_{j=0}^{2m}
a_{m,j}(n+j)^{m-1}
\frac{\ell_{B_{n+j}}(W_{n+j})}{Y_{n+j}}.
}
\tag{11}
$$


Every $Y_{n+j}$ remains present, and both complete tails are included through $\ell_B(W)$.

### Exact cancellation property

If $0\le h\le m-1$, then


$$
\sum_{j=0}^{2m}
a_{m,j}z^j(n+j)^{m-1-h}=0.
\tag{12}
$$


This follows because $z$ is a root of multiplicity $m$ of $g(T)^m$. Equivalently, the weighted power sums


$$
\sum_j a_{m,j}z^j j^\ell
$$


vanish for $0\le\ell<m$.

Thus this filter annihilates **exactly**, without a shift expansion, all model terms


$$
z^k,\ \frac{z^k}{k},\ldots,\frac{z^k}{k^{m-1}}.
$$


This differs from the fixed filter: its coefficients have been chosen to remove a finite inverse-power block algebraically.

It still requires a structured, uniformly controlled remainder before this cancellation can be applied asymptotically to the actual errors.

### Actual final gcd

Set


$$
L=\operatorname{lcm}_{0\le j\le2m}q_{n+j},
\qquad
N=\sum_{j=0}^{2m}
a_{m,j}(n+j)^{m-1}p_{n+j}\frac{L}{q_{n+j}}.
$$


Then


$$
G=\gcd(|N|,D_{n,m}L)
$$


gives


$$
\boxed{
\widetilde P_{n,m}=N/G,\qquad
\widetilde Q_{n,m}=D_{n,m}L/G.
}
\tag{13}
$$


In particular,


$$
\widetilde Q_{n,m}S-\widetilde P_{n,m}
=\widetilde Q_{n,m}(S-\widetilde c_{n,m}).
$$


No infinite nonvanishing assertion for (11), or useful growth estimate for (13), has been proved.

---

## 5. Independent audit of A1

### Bordered equations: correct

With A1’s notation, the unimodular basis change gives


$$
U^T(R+Swvv^T)U=
\begin{pmatrix}a+Sw&b^T\\b&H\end{pmatrix}.
$$


If $K=\ell H$, $z=\ell b$, $t=\ell a$, and $r=k-1$, then


$$
\det R
=\frac{t\det K-z^T\operatorname{adj}(K)z}{\ell^k},
$$


and


$$
w\det H=\frac{\ell w\det K}{\ell^k}.
$$


The powers of $\ell$ in A1’s endpoint pair are therefore correct. Its final gcd and center sign are also correct.

The corank-one survival argument is valid, including when the lower block has size one. It is a conditional local criterion, not a proof that the coupling hypothesis holds at an infinite set of primes or indices.

### Constrained integral: correct, conditional on invertibility

Taking $d=H^{-1}b$ and


$$
F(y)=1-\sum_i d_i u_i(y)
$$


gives


$$
\mathcal J(F^2)=a+Sw-b^TH^{-1}b.
$$


Hence


$$
S-c_n=\mathcal J(F^2)/w.
$$


There is no missing factor of $\det H$ or sign.

The formulation is stationary, not automatically minimizing: the weight contains $Q(x^2)$, whose sign has not been established.

### What was already in M22

The complete compact moment identity is explicitly equation (3)–(4) of the supplied M22 source. The isolation of the rank-one response and the associated constrained quadratic/Christoffel interface are standard consequences of the same matrix. These should be credited as reused interfaces, not new quantitative analysis.

### Qualification on A1’s “unconditional” nonvanishing

The supplied M22 document does **not** prove the dyadic depth theorem or the claimed regular-subfamily invertibility theorem. A1 explicitly takes them as inherited results.

Conditional on the stated exact dyadic depth


$$
v_2(q_n^{\rm cen})=n+2,
$$


its at-most-one-zero argument is correct and does not assume irrationality. Relative to the complete documents supplied in this turn, however, that depth is an **inherited assertion not independently verified here**. The bordered algebra and constrained identity do not themselves establish it.

---

## 6. Handoff

### (1) New result and proof status

**Proved here:**

- The uniform inverse-power response bound (2), and the signed-density residual estimate (6), valid for growing multiplicity.
- A narrow failure theorem for an index-independent amplitude in the actual normalized exponential-tail kernels.
- A rational varying filter that annihilates a finite inverse-power block exactly, together with its whole-error identity and actual final endpoint gcd.
- Independent verification of A1’s bordered scalings, endpoint signs, local corank-one argument, and constrained integral equation.

**Not proved:** the signed-density hypothesis for the complete actual $b=2$ errors, uniform nonvanishing of either actual growing filter, or an irrationality result.

### (2) Exact remaining bottleneck

The principal analytic question is now concrete: does the exact complete normalized error admit a representation of the form (4), or a comparably controlled signed-moment representation, with a density satisfying a bound such as (5)?

The fixed-$b$ theorem does not answer this. The separate-tail fixed-amplitude route fails by Lemma 2. Even a successful combined representation must then be paired with a bound on the **fully reduced** filtered denominator, including the gcd in (13).

### (3) Computation request

**None.** A finite scan cannot establish the missing common-density representation or its uniform bounds. The filter identities and the structured-residual estimates above have direct exact proofs.
