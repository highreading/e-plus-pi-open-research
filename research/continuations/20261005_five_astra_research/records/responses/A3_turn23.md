> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A3 — uniform localization after rescaling, but not yet the characteristic comparison

Put


$$
\sigma=\sqrt2,\qquad M=1+\sqrt2,\qquad \rho=M^{-1},
\qquad d=b-1,\qquad c=d/n.
$$


The new estimates below apply to integers


$$
d\ge2,\qquad 0<c\le 10^{-3}.
$$


Their intended asymptotic use is $d\to\infty$, $c\to0$. They do not require a particular power relation between $d$ and $n$.

**I do not complete the assigned $O(1)$ characteristic derivative comparison.** I prove a uniform, finite-$d$, fixed-interval localization lemma for precisely the proposed rescaled unperturbed ensemble. This removes the shrinking-support and remote-tail issues at the positive-ensemble level without invoking a one-cut expansion theorem. The remaining issue is an explicitly stated uniform bias estimate on that fixed interval.

A useful feature of the calculation is that the proposed rescaled potential is not merely locally close to a Gaussian potential: it is **globally uniformly strongly convex on its entire principal domain**.

## 1. Exact rescaled ensemble

Under


$$
x=\tan(\theta/2)=\sqrt c\,u,
$$


the unperturbed positive principal ensemble has density


$$
\frac1{\mathcal Z_{d,c}}
\Delta(u)^2\exp\!\left[-d\sum_{i=1}^dW_c(u_i)\right],
\qquad |u_i|<\frac M{\sqrt c},
\tag{1}
$$


where


$$
W_c(u)=
\frac{\log(1+cu^2)-\log(1-cu^2/M^2)}c
+\log(1+cu^2).
\tag{2}
$$


No amplitude or characteristic tilt has been included in (1). Those remain separate perturbations of this exact base ensemble.

On one ordered chamber define


$$
\mathcal H_{d,c}(u)
=d\sum_iW_c(u_i)-2\sum_{i<k}\log(u_k-u_i).
\tag{3}
$$


The chamber is convex. Its density vanishes at collisions and principal endpoints.

## 2. New lemma: global uniform convexity

For every $0<c\le10^{-3}$ and every $|u|<M/\sqrt c$,


$$
\boxed{W_c''(u)\ge k,\qquad k=\frac1{16}.}
\tag{4}
$$



### Proof

Write $y=cu^2$, so $0\le y<M^2$. Differentiating (2) exactly gives


$$
W_c''(u)
=
2(1+c)\frac{1-y}{(1+y)^2}
+\frac2{M^2}\frac{1+y/M^2}{(1-y/M^2)^2}.
\tag{5}
$$



If $0\le y\le1$, the first term is nonnegative and the second is at least $2/M^2>1/3$.

If $1\le y<M^2$, use


$$
\sup_{y\ge1}\frac{y-1}{(1+y)^2}=\frac18.
$$


Consequently


$$
W_c''(u)\ge-\frac{1+c}{4}+\frac2{M^2}.
$$


Since $M^2=3+2\sqrt2<6$ and $c\le10^{-3}$,


$$
-\frac{1+c}{4}+\frac2{M^2}
>
-\frac{1001}{4000}+\frac13
>\frac1{16}.
$$


This proves (4). ∎

The pair contribution in (3) is positive semidefinite, so


$$
\boxed{\nabla^2\mathcal H_{d,c}\ge kd\,I.}
\tag{6}
$$


In particular, the classical Brascamp–Lieb estimate is available globally in the $u$-coordinates, with no localization loss:


$$
\operatorname{Var}(F)
\le\frac1{kd}\mathbb E\|\nabla F\|^2.
\tag{7}
$$



This is a direct calculation for the actual $W_c$, not an application of a varying-potential expansion theorem.

## 3. New lemma: a uniformly bounded mode

Let $a=(a_1<\cdots<a_d)$ be the minimizer of (3). Then


$$
\boxed{\max_i|a_i|\le\frac4{\sqrt k}=16.}
\tag{8}
$$



### Proof

The energy tends to $+\infty$ at collisions and principal endpoints. Strong convexity gives a unique interior minimizer. Evenness gives


$$
a_i=-a_{d+1-i}.
$$


Its equations are


$$
dW_c'(a_i)=2\sum_{j\ne i}\frac1{a_i-a_j}.
\tag{9}
$$



Let $v_1<\cdots<v_d$ be the Gaussian equilibrium configuration satisfying


$$
kd\,v_i=2\sum_{j\ne i}\frac1{v_i-v_j}.
\tag{10}
$$


These are the zeros of the probabilists’ Hermite polynomial scaled by $(kd)^{-1/2}$. The Hermite three-term recurrence realizes them as eigenvalues of a symmetric Jacobi matrix whose off-diagonal entries are


$$
\sqrt{\frac{i}{kd}},\qquad 1\le i<d.
$$


Its norm is at most twice its largest off-diagonal entry, hence


$$
|v_i|\le\frac2{\sqrt k}.
\tag{11}
$$



Set $R_0=2/\sqrt k$, and suppose


$$
\max_i(a_i-v_i-R_0)>0.
$$


Choose an index attaining that maximum. Then $a_i>v_i+R_0\ge0$. Also, for every $j\ne i$,


$$
a_i-a_j\ge v_i-v_j.
$$


For $j<i$, both differences are positive; for $j>i$, both are negative. Since $s\mapsto1/s$ is decreasing on each of these intervals,


$$
2\sum_{j\ne i}\frac1{a_i-a_j}
\le
2\sum_{j\ne i}\frac1{v_i-v_j}
=kd\,v_i.
\tag{12}
$$


But $W_c'(0)=0$ and (4) imply $W_c'(a_i)\ge ka_i$, so (9) gives


$$
kd\,a_i\le kd\,v_i,
$$


a contradiction.

Thus $a_i\le v_i+R_0\le4/\sqrt k$. Reflection gives the lower bound. ∎

## 4. New lemma: a uniform remote-tail estimate

For every $T>1/\sqrt k$,


$$
\boxed{
\mathbb P\!\left\{\max_i|u_i|>\frac4{\sqrt k}+T\right\}
\le
\exp\!\left[
-\frac d2\bigl(kT^2-1-\log(kT^2)\bigr)
\right].
}
\tag{13}
$$



In particular, choosing $T=2/\sqrt k=8$ gives


$$
\boxed{
\mathbb P\{\max_i|u_i|>24\}
\le e^{-\gamma d},
\qquad
\gamma=\frac{3-\log4}{2}>0.
}
\tag{14}
$$



### Proof

Translate the ordered chamber by its mode $a$. Along any admissible ray $a+r\omega$, strong convexity and $\nabla\mathcal H(a)=0$ give


$$
\frac{d}{dr}\mathcal H(a+r\omega)\ge kd\,r.
$$


Therefore


$$
r\longmapsto
\exp\!\left[
-\mathcal H(a+r\omega)+\mathcal H(a)+\frac{kd\,r^2}{2}
\right]
$$


is nonincreasing until the ray reaches the chamber boundary. Extend it by zero beyond that boundary.

After integrating over directions, the radial density of $\|u-a\|$ has the form


$$
C\,r^{d-1}e^{-kd r^2/2}A(r),
$$


where $A(r)$ is nonnegative and nonincreasing. Thus its ratio to the radial density of a $d$-dimensional centered Gaussian with covariance $(kd)^{-1}I$ is nonincreasing. The resulting one-dimensional monotone-likelihood-ratio comparison gives stochastic domination by that Gaussian radius.

Hence


$$
\mathbb P\{\|u-a\|>T\}
\le \mathbb P\{\chi_d^2>kdT^2\}.
$$


The standard exponential-moment calculation for $\chi_d^2$ yields


$$
\mathbb P\{\chi_d^2>sd\}
\le e^{-d(s-1-\log s)/2},\qquad s>1.
$$


Finally, (8) implies that


$$
\max_i|u_i|>4/\sqrt k+T
\quad\Longrightarrow\quad
\|u-a\|>T.
$$


This proves (13). ∎

This proof controls the complete principal domain, including points approaching its moving endpoints. No tail has been discarded on equilibrium grounds alone.

## 5. Consequence: reduction to an actual fixed-domain ensemble

Let $\mathbb E_{d,c}$ denote expectation in (1), and let $\mathbb E^{[24]}_{d,c}$ denote that same ensemble conditioned on all particles lying in $[-24,24]$. For sufficiently small $c$, this interval is inside the principal domain.

If $f$ is uniformly bounded on the principal domain, then (14) gives


$$
\boxed{
\left|
\mathbb E_{d,c}\sum_i f(u_i)
-\mathbb E^{[24]}_{d,c}\sum_i f(u_i)
\right|
\le 2d\|f\|_\infty e^{-\gamma d}.
}
\tag{15}
$$


The corresponding partition functions satisfy exactly


$$
\frac{\mathcal Z^{[24]}_{d,c}}{\mathcal Z_{d,c}}
=\mathbb P\{\max_i|u_i|\le24\}
=1+O(e^{-\gamma d}).
\tag{16}
$$



For the characteristic derivative use


$$
f_{c,q}(u)=
\frac1{z(\sqrt c\,u)^{-1}+q},
\qquad
z(x)=\frac{1+ix}{1-ix}.
\tag{17}
$$


For real $q$ in fixed sufficiently small neighborhoods of $M$ and $\rho$, its denominator is uniformly separated from zero on the whole real $u$-axis. Thus (15) applies uniformly to (17).

The exact equilibrium support is contained in $[-24,24]$ for all sufficiently small $c$, since


$$
\frac{A_c^2}{c}
=\frac{M^2(c+2)}{M^2+(c+1)^2}
\longrightarrow\frac{2M^2}{M^2+1}.
\tag{18}
$$


Restricting the domain to $[-24,24]$ therefore does not change that equilibrium measure.

Moreover, on a fixed complex neighborhood of this interval, $W_c$ converges analytically to


$$
W_0(u)=(1+M^{-2})u^2.
$$


Thus the localization proposal is now justified by a finite-$d$, uniform estimate. What is **not** justified merely by this observation is a uniform expansion of its finite-$d$ mean trace.

## 6. The exact remaining comparison

Let $\widehat\mu_c$ be the pushforward of the archived equilibrium under $x=\sqrt c\,u$. Define


$$
\mathcal B_{d,c}(q)=
\mathbb E^{[24]}_{d,c}\sum_{i=1}^d f_{c,q}(u_i)
-d\int f_{c,q}(u)\,d\widehat\mu_c(u).
\tag{19}
$$


The assigned sufficient estimate is now reduced to


$$
\boxed{
\sup_{\substack{0<c\le c_*\\d\ge d_*\\q\in J_M\cup J_\rho}}
|\mathcal B_{d,c}(q)|<\infty,
}
\tag{20}
$$


with constants independent of $d,c$.

The localization error in this reduction is $O(de^{-\gamma d})$, not $d\,o(1)$.

Equation (7) does not prove (20). It controls fluctuations about the finite-$d$ mean, while (20) compares that mean with equilibrium. Indeed,


$$
\operatorname{Var}\!\left(\sum_i f(u_i)\right)
\le k^{-1}\|f'\|_\infty^2
$$


contains no estimate for the deterministic bias (19).

The unresolved analytic constant is therefore a uniform bound for the equilibrium linear-response/loop inversion needed to convert the finite-$d$ loop residual into (20), together with control of that residual in the inversion norm. I have not derived that inversion here, nor verified all the theorem-level hypotheses and uniform constants necessary to import it from Borot–Guionnet. Analytic convergence of the potentials alone is not a substitute.

Subject to (20), the supplied positive-tilt and actual phase/insertion estimates would give


$$
(\log A_j)'(q)=dL_c'(q)+O(1),
\tag{21}
$$


uniformly in $0\le j\le b$. In that transfer the actual normalization remains


$$
N_j(q)=\mathbb E_q(S_je^{i\Phi_q}),
\qquad
\langle F\rangle_j
=\frac{\mathbb E_q(S_je^{i\Phi_q}F)}{N_j(q)}.
$$


It cannot be replaced by one before estimating centered errors.

Since the real saddle displacement is $O(c)$, (21) would cost only $O(c)$ in stationary increments. This explains precisely why the bounded bias in (20), rather than another moment coefficient, is the remaining target.

## 7. Whole-error and arithmetic scope

No new all-sublinear scalar conclusion is claimed. The original scalar contours, signed particle outer sectors, remote scalar arcs, and both minus connectors remain required.

Retain the full forces $P_j,F_j$ and


$$
E_j=\nu_{n,d}\!\left(
R_j\sum_{i=0}^d\sigma^i e_{d-i}(z^{-1})eE_i
\right),
$$


with the complete forcing


$$
eE_i=-[z^{n+i}](1-z+z^2/2)^n
\int_0^1s^n e^{1-s+sz}\,ds.
$$


For $D=\det H_b$, the actual columns remain


$$
u_j=(-1)^nP_j/D,\qquad
v_j-Su_j=\delta_{j0}+(-1)^nE_j/D-F_j/D.
$$


Whenever $P_j\ne0$, the whole real error is exactly


$$
c_j-S=
\frac{E_j}{P_j}
+(-1)^{n+1}\frac{F_j}{P_j}
+(-1)^n\delta_{j0}\frac D{P_j}.
\tag{22}
$$


For a positive diagonal metric $W$, the center remains


$$
c_W=\frac{u^TWv}{u^TWu}.
$$


Neither a different column system nor a nondiagonal metric is substituted.

For rational positive diagonal metrics, retain the least actual clearer $d_B$, an integral positive diagonal scaling $\Omega$, and


$$
N_B=d_B[u,v],\quad
A_B=N_{B,1}^T\Omega N_{B,1},\quad
H_B=N_{B,1}^T\Omega N_{B,2}.
$$


With


$$
g_B=\gcd(A_B,|H_B|),\qquad
q_B=A_B/g_B,\qquad p_B=H_B/g_B,
$$


the primitive multiplier is $d_B^2/g_B$, and


$$
q_BS-p_B
=\frac{d_B^2}{g_B}
\bigl[(u^T\Omega u)S-u^T\Omega v\bigr]
=q_B(S-c_W).
\tag{23}
$$


This report proves no new all-sublinear nonvanishing of (22) or (23), and supplies no bound for $q_B$.

## Closing ledger

1. **New result and proof status.**  
   Proved directly for the exact rescaled ensemble: global uniform convexity $W_c''\ge1/16$; a uniformly bounded mode; the remote-tail estimate (13); and fixed-domain trace and partition comparisons with exponentially small error in $d$. These are uniform finite-$d$ estimates, not empirical evidence. The assigned characteristic derivative comparison remains unproved.

2. **Exact remaining bottleneck.**  
   Prove the bounded finite-$d$ equilibrium bias (20) on the now-justified fixed interval, with a uniform loop-inversion constant or a fully verified applicable expansion theorem. After the analytic comparison, irrationality would still require same-index control of the actual reduced denominator after the final gcd, and nonzero whole primitive errors tending to zero. Neither is supplied here.

3. **Computation request.**  
   None. The outstanding assertion is a uniform analytic bias estimate; finite numerical convergence would not establish it.
