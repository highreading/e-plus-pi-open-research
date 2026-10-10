> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

## A1 continuation: eventual compact sign changes, and a signed-error bound with an explicit spectral obstruction

The proposed quasi-orthogonality alternative is valid: **the number of roots of $Q_n$ in $(0,1)$ tends to infinity.** In particular, $Q_n>0$ on $[0,1]$ cannot hold for all sufficiently large $n$, including on the regular subfamily $n=4^j+1$.

This obstructs the positive-weight Christoffel strategy for this family. It does **not** exclude the determinant family or determine the sign, size, or nonvanishing of its complete evaluated error.

I also give an unconditional signed-error inequality involving an explicit normalized spectral gap of the rational lower block. Unlike positivity of $Q_n$, this gap is a viable quantity to study after compact sign changes begin.

The compact moment and stationary-error identities are reused from M22 and the preceding interface, not claimed as new.

---

## 1. Measures, normalization, and dependency status

Let


$$
d\mu(y)
=
\frac{e^{-1-\sqrt y}+\mathbf1_{(0,1)}(y)e^{-1+\sqrt y}}
{2\sqrt y}\,dy,\qquad y>0,
$$


so that


$$
\mu(y^r)=D_{2r}.
$$


Set


$$
\rho=\mu-\delta_{-1},
\qquad d\nu(y)=(y+1)\,d\mu(y).
$$



For every $n\ge2$, let $Q_n$ denote the positive-leading primitive integer normalization of the monic degree-$n$ polynomial orthogonal for $\rho$. I use the supplied finite-degree normalization theorem as given:

* $Q_n$ exists;
* it has one simple root below $-1$ and $n-1$ simple positive roots;
* $Q_n(-1)\ne0$.

The supplied dyadic conclusion


$$
v_2(q_n^{\mathrm{cen}})=n+2,
\qquad n\in\mathcal N:=\{4^j+1:j\ge1\},
$$


is an **inherited author theorem**, not independently re-certified here: its underlying machine states and receipts are not included in a form I can inspect. Statements below using this conclusion retain that dependency. The eventual compact-root theorem does not require the dyadic theorem.

---

## 2. Stieltjes determinacy: the relevant Carleman condition really holds

Write


$$
m_r=\int_0^\infty y^r\,d\nu(y)=D_{2r}+D_{2r+2}.
$$


For $r\ge1$,


$$
0<m_r\le (2r)!+(2r+2)!\le2(2r+2)!.
$$


Consequently,


$$
m_r^{-1/(2r)}
\ge \bigl(2(2r+2)!\bigr)^{-1/(2r)}
\ge \frac{c}{r}
$$


for some fixed $c>0$. For example, the last inequality follows immediately from Stirling’s formula. Therefore


$$
\sum_{r=1}^{\infty}m_r^{-1/(2r)}=\infty.
$$



This is exactly the **Stieltjes Carleman condition**, and it implies uniqueness of the representing measure on $[0,\infty)$.

It is important not to replace this with the Hamburger condition. The latter would use $m_{2r}^{-1/(2r)}$, for which the corresponding factorial estimate has order $r^{-2}$, not $r^{-1}$. That different series does not provide the required divergence.

Thus the determinacy input needed below is justified in the correct moment problem.

---

## 3. Gaussian quadrature measures converge weakly to $\nu$

Let $\pi_N$ be the monic degree-$N$ orthogonal polynomial for the positive measure $\nu$. Its roots


$$
0<x_{N,1}<\cdots<x_{N,N}
$$


are simple. Let


$$
\nu_N=\sum_{i=1}^N\lambda_{N,i}\delta_{x_{N,i}},
\qquad \lambda_{N,i}>0,
$$


be its Gaussian quadrature measure. Then


$$
\int y^r\,d\nu_N=m_r,\qquad 0\le r\le2N-1.
$$



Here is a direct justification of weak convergence, including the unbounded-support issue.

1. The measures have common mass $m_0$. Their common first moment, for $N\ge1$, gives
   

$$
\nu_N([R,\infty))\le \frac{m_1}{R}.
$$


   Hence they are tight.

2. Consider any weakly convergent subsequence with limit $\eta$. For each fixed integer $r\ge0$, the quadrature moments of orders $r$ and $r+1$ are eventually exact. The estimate
   

$$
\int_{y>R}y^r\,d\nu_N
   \le \frac{m_{r+1}}{R}
$$


   gives uniform integrability of $y^r$. Truncating and passing to the limit yields
   

$$
\int y^r\,d\eta=m_r.
$$



3. The limit is supported on $[0,\infty)$. Stieltjes determinacy therefore gives $\eta=\nu$.

Every convergent subsequence has this same limit, so


$$
\boxed{\nu_N\Longrightarrow\nu.}
$$



In particular, every nonempty open interval contained in $(0,\infty)$ eventually contains a Gaussian node: its $\nu$-mass is strictly positive, and the Portmanteau inequality applies.

More strongly, by choosing any prescribed finite number of disjoint such intervals, the number of nodes in their containing interval must eventually exceed that prescribed number.

---

## 4. Quasi-orthogonality forces arbitrarily many compact roots

For every polynomial $r$ with $\deg r\le n-2$,


$$
\int Q_n(y)r(y)\,d\nu(y)
=
\rho\bigl(Q_n(y)(y+1)r(y)\bigr)=0.
$$


The atom at $-1$ vanishes, and the tested degree is at most $n-1$.

After dividing by its positive leading coefficient, $Q_n$ consequently has an expansion


$$
\widehat Q_n=\pi_n+a_n\pi_{n-1}
$$


for some real $a_n$. This is order-one quasi-orthogonality for the positive measure $\nu$, established separately at each $n$; it does not assume global quasi-definiteness of $\rho$.

At each zero of $\pi_{n-1}$,


$$
\widehat Q_n(x_{n-1,i})=\pi_n(x_{n-1,i}).
$$


The three-term recurrence gives


$$
\pi_n(x_{n-1,i})=-b_{n-1}\pi_{n-2}(x_{n-1,i}),
\qquad b_{n-1}>0.
$$


By interlacing, these values alternate in sign. Therefore $Q_n$ has a root between every pair of consecutive roots of $\pi_{n-1}$.

### Compact-root theorem

For every $0<a<b<\infty$,


$$
\boxed{\#\{y\in(a,b):Q_n(y)=0\}\longrightarrow\infty
\quad(n\to\infty).}
$$



**Proof.** Fix an integer $L\ge1$. Choose $L+1$ pairwise disjoint nonempty open intervals inside $(a,b)$. Weak convergence of the Gaussian measures for $\nu$ shows that, for all sufficiently large $n$, $\pi_{n-1}$ has at least $L+1$ roots in $(a,b)$. The roots lying in $(a,b)$ form a consecutive block in the ordered zero list. Between adjacent members of this block, $Q_n$ has a root. Thus it has at least $L$ roots in $(a,b)$. Since $L$ was arbitrary, the claim follows. ∎

Taking $(a,b)\subset(0,1)$ proves the announced result.

### Scope of the obstruction

Because the positive roots of $Q_n$ are simple, these interior roots are genuine sign changes. Thus:

* eventual strict compact positivity is impossible;
* eventual nonnegative compact weight is also impossible;
* the positive-measure Christoffel minimization formula cannot be applied directly to $Q_n\,d\sigma$ at all large indices.

This says nothing by itself about definiteness of its **finite polynomial compression**. A signed weight can still induce a definite form on a particular finite-dimensional polynomial space. Nor does it prove that the determinant error changes sign.

The reported root-free cases $n=5,17$ are compatible with the theorem. The proof supplies no effective onset index.

---

## 5. A signed-error bound that survives the failure of positivity

Now restrict to


$$
n=2k-1\in\mathcal N,\qquad r=k-1,\qquad w=Q_n(-1)>0.
$$


Use the compact positive base measure


$$
d\sigma(y)=
\frac{e^{\sqrt y}+4/(1+y)}{2\sqrt y}\,dy,\qquad 0<y<1.
$$


Define the signed and absolute-weight functionals


$$
\mathcal J(f)=\int_0^1 Q_n(y)f(y)\,d\sigma(y),
\qquad
\mathcal M(f)=\int_0^1 |Q_n(y)|f(y)\,d\sigma(y).
$$



Let


$$
u_i(y)=y^i-(-1)^i,\qquad 1\le i\le r.
$$


Their span is precisely the degree-$\le r$ polynomials vanishing at $-1$. Put


$$
H_{ij}=\mathcal J(u_i u_j),
\qquad
G_{ij}=\mathcal M(u_i u_j).
$$


Here $H$ is the same rational lower block as in the previous bordered interface. It is nonsingular on $\mathcal N$ under the inherited arithmetic theorem. The matrix $G$ is positive definite: a nonzero polynomial cannot vanish almost everywhere on an interval, and $|Q_n|\,d\sigma$ is positive away from finitely many points.

Define


$$
C=G^{-1/2}HG^{-1/2},
\qquad
\theta_n=\min_{\lambda\in\operatorname{spec}(C)}|\lambda|.
$$


Then


$$
0<\theta_n\le1.
$$


Indeed, for every real coefficient vector $z$,


$$
|z^THz|\le z^TGz.
$$


Thus all eigenvalues of $C$ lie in $[-1,1]$, and nonsingularity gives strict positivity of $\theta_n$.

### Signed stationary-error lemma

Let $F_n$ be the actual rational stationary polynomial:


$$
F_n(-1)=1,\qquad \deg F_n\le r,\qquad
\mathcal J(F_nu_i)=0.
$$


For every real polynomial $P$ satisfying


$$
P(-1)=1,\qquad \deg P\le r,
$$


one has


$$
\boxed{
|\mathcal J(F_n^2)|
\le \left(1+\frac1{\theta_n}\right)\mathcal M(P^2).
}
\tag{1}
$$



**Proof.** Let


$$
h_i=\mathcal J(Pu_i).
$$


Stationarity and nonsingularity give


$$
F_n=P-\sum_i(H^{-1}h)_i u_i,
$$


and hence the exact identity


$$
\mathcal J(F_n^2)=\mathcal J(P^2)-h^TH^{-1}h.
\tag{2}
$$


This retains the actual $F_n$; it does not replace it with a positive minimizer.

Writing $\widetilde h=G^{-1/2}h$,


$$
|h^TH^{-1}h|
=|\widetilde h^TC^{-1}\widetilde h|
\le \theta_n^{-1}h^TG^{-1}h.
$$


In the Hilbert space $L^2(|Q_n|\,d\sigma)$, the vector $h$ consists of the inner products of $\operatorname{sgn}(Q_n)P$ against $u_i$. Orthogonal projection onto their span therefore gives


$$
h^TG^{-1}h
\le \|\operatorname{sgn}(Q_n)P\|^2
=\mathcal M(P^2).
$$


Also $|\mathcal J(P^2)|\le\mathcal M(P^2)$. Combining these estimates with (2) proves (1). ∎

This is not a completed rate estimate. It replaces the false eventual positivity premise by the explicit problem of bounding how close a normalized signed compression comes to singularity.

### Consequence for the whole evaluated error

The inherited exact identity is


$$
S-c_n=\frac{\mathcal J(F_n^2)}{w}.
$$


Since


$$
\sigma([0,1])=e-1+\pi=S-1,
$$


test (1) with


$$
P(y)=\frac{T_r(2y-1)}{T_r(-3)}.
$$


It follows that


$$
\boxed{
|S-c_n|
\le
\frac{(S-1)(1+\theta_n^{-1})}
{T_r(3)^2}
\sup_{0\le y\le1}\frac{|Q_n(y)|}{w}.
}
\tag{3}
$$



Unlike the earlier positive-weight estimate, (3) is valid despite arbitrarily many compact sign changes.

---

## 6. An exact inertia description of the new spectral obstruction

Split the lower-block absolute Gram form according to the sign of $Q_n$:


$$
G=G_++G_-,
\qquad H=G_+-G_-,
$$


where


$$
(G_-)_{ij}
=\int_{\{Q_n<0\}}|Q_n(y)|u_i(y)u_j(y)\,d\sigma(y).
$$


Thus


$$
C=I-2B,\qquad B=G^{-1/2}G_-G^{-1/2},
$$


and $0\le B\le I$.

If $\eta_1,\ldots,\eta_r$ are the eigenvalues of $B$, then


$$
\boxed{
\begin{aligned}
n_+(H)&=\#\{i:\eta_i<1/2\},\\
n_-(H)&=\#\{i:\eta_i>1/2\},\\
n_0(H)&=\#\{i:\eta_i=1/2\},\\
\theta_n&=\min_i|1-2\eta_i|.
\end{aligned}}
\tag{4}
$$



This supplies a precise interpretation: the obstruction is not the mere presence of negative intervals, but a polynomial direction for which positive and negative compact masses nearly balance.

For the complete compact matrix, the bordered stationary congruence also yields


$$
\operatorname{inertia}
\begin{pmatrix}
\mathcal J(1)&\mathcal J(u)^T\\
\mathcal J(u)&H
\end{pmatrix}
=
\operatorname{inertia}(H)
+
\operatorname{inertia}\bigl(\mathcal J(F_n^2)\bigr).
\tag{5}
$$


Equation (5) identifies the complete error sign through an inertia difference, but does not assume that difference is known.

---

## 7. Actual denominator, final gcd, and nonvanishing remain indispensable

Retain the bordered integers from the preceding interface:


$$
\ell=\operatorname{lcm}(1,3,\ldots,4n-3),\quad
K=\ell H,\quad z=\ell b,\quad t=\ell a,
$$




$$
\Delta=\det K,\qquad
A=t\Delta-z^T\operatorname{adj}(K)z,\qquad
B=\ell w\Delta.
$$


With the **final** gcd


$$
g=\gcd(|A|,|B|),
$$


the actual primitive pair is


$$
p_n^{\mathrm{cen}}=-\frac{\operatorname{sgn}(B)A}{g},
\qquad
q_n^{\mathrm{cen}}=\frac{|B|}{g}.
$$


On the inherited dyadic domain,


$$
q_n^{\mathrm{cen}}=2^{n+2}o_n,\qquad o_n\ \text{positive and odd}.
$$



The whole primitive error is exactly


$$
q_n^{\mathrm{cen}}S-p_n^{\mathrm{cen}}
=\frac{2^{n+2}o_n}{w}\,\mathcal J(F_n^2).
$$


In particular, (3) gives the sufficient estimate


$$
\boxed{
|q_n^{\mathrm{cen}}S-p_n^{\mathrm{cen}}|
\le
\frac{2^{n+2}o_n(S-1)(1+\theta_n^{-1})}
{T_r(3)^2}
\sup_{[0,1]}\frac{|Q_n|}{w}.
}
\tag{6}
$$



No factor on the right is a substitute for the final reduced denominator.

The earlier eventual-nonvanishing deduction is correct, conditional on the supplied dyadic theorem: two distinct regular indices have different reduced denominator $2$-depths, so their rational centers are different. Consequently at most one can equal $S$. This gives eventual nonvanishing without assuming irrationality, but not an effective exceptional-index bound.

---

## 8. Secondary audit: A5’s lattice/gcd factorization is correct as finite algebra

I independently checked A5 §§5–8, assuming its stated saturated rank-two lattice and endpoint isomorphism. I find **no algebraic error in that factorization**.

The potentially delicate assertions check out:

1. Saturation ensures that the integer basis matrix $[z_0,z_1]$ has an integer left inverse. Thus multiplication by it preserves joint entry content.

2. From
   

$$
\gcd(D_0,a,b_{\rm end})=1
$$


   one really gets
   

$$
\gcd(hD_0,a,b_{\rm end})
   =\gcd(h,a,b_{\rm end})=\gamma.
$$


   Prime by prime, whenever a prime divides both endpoint numerators, it cannot divide $D_0$.

3. The crucial coprimality in §7 is valid. Since
   

$$
\alpha=\gcd(t,|a'|),
   \qquad
   r=\frac{a'}{\alpha}v_0-b'\frac t\alpha,
$$


   and
   

$$
\gcd(t/\alpha,a'/\alpha)=1,\qquad \gcd(t,v_0)=1,
$$


   one obtains
   

$$
\gcd(t/\alpha,r)=1.
$$


   Hence the final cancellation is exactly
   

$$
g_B=k\delta\alpha\gcd(k,|r|),
   \qquad
   q=\frac t\alpha\,\frac{k}{\gcd(k,|r|)}.
$$



This confirms the finite lattice theorem, not its missing growing-dimensional arithmetic estimates. It also does not independently validate A5’s proportional analytic theorem or its Rodrigues reconstruction: those underlying source documents are not supplied here.

---

## Handoff

### (1) New result and proof status

**Proved here, using standard Stieltjes determinacy and Gaussian quadrature with their hypotheses checked:**


$$
\#\{Q_n\text{ roots in }(a,b)\}\to\infty
$$


for every fixed $0<a<b<\infty$. Eventual compact positivity is therefore impossible.

**Proved here as a signed follow-on bound:** equations (1)–(4), giving a whole-error upper bound through the absolute compact weight and a normalized signed spectral gap. Its application to the regular primitive pair retains the inherited lower-block nonsingularity and dyadic theorem.

**Independently confirmed:** A5’s saturated-lattice final-gcd factorization, conditional on its finite endpoint hypotheses.

### (2) Exact remaining bottleneck

For the same regular indices, a sufficient quantitative target is


$$
\frac{2^{n+2}o_n(1+\theta_n^{-1})}{T_{(n-1)/2}(3)^2}
\sup_{[0,1]}\frac{|Q_n|}{Q_n(-1)}
\longrightarrow0.
$$


None of the required aggregate control of the actual odd denominator, normalized polynomial amplitude, and signed spectral gap has been proved.

The failure of compact positivity is a scoped obstruction—not a whole-family exclusion. The irrationality of $e+\pi$ remains unresolved.

### (3) Computation request

**None required for these proofs.** A finite root search cannot establish an onset rate or the necessary spectral-gap bound. The next substantive analytic task is to obtain an effective bound for $\theta_n$ or an alternative cancellation estimate for the actual stationary integral, not to extrapolate the root-free small indices.
