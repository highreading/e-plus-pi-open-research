> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

## Result: the interior density survives, and the specified primorial subfamily is excluded

The proposed degree-three amplitude is correct. After moving **all** Euler derivatives onto the actual local densities, it produces a nonzero term of order $(T+r)^{-5/2}$. The degree-four contribution has only order $(T+r)^{-3/2}$, so it cannot cancel that term. The lower polynomial degrees cannot cancel it either.

This gives a complete signed Laplace asymptotic for an existence interval of proportional orders immediately above


$$
c_0=\frac5r-1,\qquad r=2(1+\sqrt2).
$$


Combined with the accepted actual-denominator lower bound, it excludes the corresponding odd-primorial subfamily as a source of shrinking primitive forms. It does not decide irrationality of $e+\pi$.

### 1. Actual polynomial weights, including every degree

Write


$$
b=\sqrt2,\quad M=1+b,\quad \rho=M^{-1},\quad r=2M.
$$


I reuse the exact moment construction and complete exponential decomposition from A3 turn 5.

For a circle variable $\theta$, put


$$
v=-1-b\cos\theta,\qquad z=-be^{i\theta},\qquad
w_a(v)=\Re(z^ae^z),\quad a=0,1,2.
$$


The weights are well-defined as functions of $v$, since the two corresponding circle points are conjugate. Near $v=-M$, $w_0>0$. Define there


$$
q(v)=\frac{w_1(v)}{w_0(v)},\qquad h(v)=\frac{w_2(v)}{w_0(v)}.
$$


Use the positive local product measure


$$
d\lambda=
w_0(v_1)w_0(v_2)
\frac{d\theta_1d\theta_2}{(2\pi)^2}\,
\frac{4\,dy}{1+b\cosh y},
\qquad y\ge0,
$$


and the pushforward map


$$
T=v_1v_2u(y),\qquad u(y)=-\frac2{1+b\cosh y}.
$$



Here and below angular neighborhoods of zero are understood on the circle, so their local coordinates are signed.

Introduce the following symmetric weights:


$$
\begin{aligned}
F&=\frac12(v_1-v_2)(q_2-q_1),\\
G&=\frac12\left[
v_1(1-q_1+q_1q_2-h_1)
+v_2(1-q_2+q_1q_2-h_2)\right],\\
B&=v_1v_2,\\
D&=v_1v_2\left(q_1q_2-\frac{h_1+h_2}{2}\right).
\end{aligned}
\tag{1}
$$


Symmetrization is legitimate because both $T$ and $d\lambda$ are invariant under exchanging the circle variables.

In the notation of the proposal, $F$ represents $F_0$, $G$ represents $G_0$, $B$ represents $B_0^2$, and $D$ represents $B_1^2-B_0B_2$. The exact polynomial expansions are


$$
\frac{C_k}{(k!)^2}=(k+1)(kF_0+G_0),
$$


and


$$
\frac{S_k}{(k!)^2}=(k+1)^2\bigl((k+1)B_0^2+
B_1^2-B_0B_2\bigr).
$$


Consequently the weights of the five actual measures $\mu_j$, relative to $d\lambda$, are


$$
\begin{array}{c|l}
j&A_j\\ \hline
4&uF\\
3&u(3F+G)-2B\\
2&u(3F+3G)-2(3B+D)\\
1&u(F+3G)-2(3B+2D)\\
0&uG-2(B+D).
\end{array}
\tag{2}
$$


These formulas check both the degree-three/four coefficients and every lower degree. In particular, no lower-degree amplitude is being discarded before integration by parts.

The local density $f_j(T)$ below is precisely the pushforward of $A_j\,d\lambda$, not a density selected to match an individual-index asymptotic.

### 2. The corner, its Hessian, and analytic pushforward densities

The unique point attaining $T=-r$ is


$$
\theta_1=\theta_2=y=0.
$$


Indeed, this requires the maximum positive product $v_1v_2=M^2$ and the minimum $u=-2/M$.

At this corner,


$$
\begin{aligned}
v_i&=-M+\frac b2\theta_i^2+O(\theta_i^4),\\
u(y)&=-\frac2M+\frac b{M^2}y^2+O(y^4).
\end{aligned}
$$


Therefore


$$
\boxed{
T+r=b(\theta_1^2+\theta_2^2+y^2)+O\!\left(
(\theta_1^2+\theta_2^2+y^2)^2\right).
}
\tag{3}
$$


The quadratic Hessian is $2bI_3$, positive definite.

All weights and the map are real analytic and even in each corner coordinate. Extend the integrand evenly to negative $y$, use half the resulting integral, and apply the analytic Morse lemma to (3). In analytic Morse coordinates, the pushforward is a radial integral over spheres. The spherical average of an analytic amplitude has a convergent expansion in the squared radius: odd homogeneous terms integrate to zero. Thus, for some $\epsilon>0$,


$$
f_j(-r+s)=s^{1/2}a_j(s),\qquad 0<s<\epsilon,
\tag{4}
$$


where every $a_j$ is real analytic at $s=0$.

There are no other preimages contributing sufficiently close to this endpoint. To see this, first bound $y$ for $T$ close to $-r$, using $u(y)\to0$. On the remaining compact domain, uniqueness of the minimum separates the complement of any corner neighborhood from $-r$. Hence (4) describes the **entire actual density** near the endpoint.

In particular, the densities are real analytic on the open interval $(-r,-r+\epsilon)$, and their endpoint expansions may be differentiated to any fixed order.

The pushforward density of $d\lambda$ itself has leading coefficient


$$
K=\frac{e^{-2b}}{\pi M b^{3/2}}>0.
\tag{5}
$$


Indeed, the corner weight is


$$
\frac{e^{-2b}}{\pi^2M},
$$


while the pushforward of Lebesgue measure on the half-space $y\ge0$ under $s=b|\boldsymbol\theta|^2$ has density


$$
\frac{\pi}{b^{3/2}}s^{1/2}.
$$



### 3. Fourth-order vanishing and the nonzero degree-three amplitude

Set $a=v+1$ and $\beta^2=2-a^2$. Near the corner,


$$
q(v)=a-\beta\tan\beta.
$$


This is analytic there because $\beta\tan\beta$ is analytic in $\beta^2$. At $v=-M$,


$$
q=-b,\qquad h=b^2,\qquad q'=1-2b.
\tag{6}
$$


The last identity follows from


$$
\beta\tan\beta=(2-a^2)+O((2-a^2)^2).
$$



Consequently,


$$
F=-\frac{q'(-M)}2(v_1-v_2)^2
+O\!\left((|v_1+M|+|v_2+M|)^3\right).
\tag{7}
$$


Since $v_i+M=O(\theta_i^2)$, this is fourth-order, not second-order, angular vanishing.

More explicitly, spherical averaging gives


$$
\boxed{
f_4(-r+s)
=K\,\frac{1-2b}{15M}s^{5/2}+O(s^{7/2}).
}
\tag{8}
$$


For the coefficient, use


$$
(v_1-v_2)^2=\frac{b^2}{4}(\theta_1^2-\theta_2^2)^2+O(|\boldsymbol\theta|^6),
$$


and, on the unit sphere,


$$
\operatorname{avg}(\omega_1^2-\omega_2^2)^2=\frac4{15}.
$$


The same average holds on the hemisphere because the integrand is even in its third coordinate.

At the corner, (1) gives


$$
F=0,\qquad G=-M^2,\qquad B=M^2,\qquad D=0.
$$


Thus the degree-three weight is


$$
A_3=\left(-\frac2M\right)(-M^2)-2M^2
=2M-2M^2=-2bM.
\tag{9}
$$


This verifies the proposal’s nonzero candidate.

Let


$$
A=-2bM<0.
$$


Equations (2) also check all lower-degree corner values:


$$
(A_0,A_1,A_2,A_3)=(A,3A,3A,A).
$$


Therefore


$$
\boxed{
\begin{aligned}
f_3(-r+s)&=AKs^{1/2}+O(s^{3/2}),\\
f_2(-r+s)&=3AKs^{1/2}+O(s^{3/2}),\\
f_1(-r+s)&=3AKs^{1/2}+O(s^{3/2}),\\
f_0(-r+s)&=AKs^{1/2}+O(s^{3/2}).
\end{aligned}}
\tag{10}
$$


All remainders here have the analytic structure established in (4).

### 4. The total adjoint-Euler density

With respect to Lebesgue measure,


$$
D=T\frac d{dT},\qquad D^*f=-(Tf)'.
$$


Writing $T=-r+s$,


$$
D^*=(r-s)\frac d{ds}-1.
\tag{11}
$$


Define on the open endpoint interval


$$
\mathcal F(T)=\sum_{j=0}^4(D^*)^jf_j(T).
$$



The leading contribution from $j=3$ is


$$
r^3 AK\,\frac d{ds}^{\,3}s^{1/2}
=\frac38r^3AKs^{-5/2}.
$$


The fourth derivative of (8) is only $O(s^{-3/2})$. The entire $j=2$ contribution is also $O(s^{-3/2})$; those for $j=1,0$ are smaller. The lower derivative terms in each power of (11) likewise have smaller singular order.

It follows that the **total** effective density satisfies


$$
\boxed{
\mathcal F(-r+s)
=-\frac34\,bMr^3K\,s^{-5/2}
+O(s^{-3/2}).
}
\tag{12}
$$


This establishes the required noncancellation, including all polynomial degrees and all derivatives.

In particular, after decreasing $\epsilon$ if necessary,


$$
\mathcal F(T)<0\qquad(-r<T<-r+\epsilon).
\tag{13}
$$


No global integration of the singular expression (12) is asserted or needed.

### 5. An existence interval of orders with a strict global gap

For $c>c_0=5/r-1$, the negative-branch phase


$$
\phi_c(T)=\log(-T)+c\log(5+T)
$$


has its unique maximum at


$$
T_c=-\frac5{1+c}.
$$


As $c\downarrow c_0$,


$$
T_c+r\downarrow0.
$$


Hence $T_c$ lies in the interval (13) for all sufficiently small positive $c-c_0$.

The negative branch also strictly dominates the positive branch at $c_0$. Here is a rational-bound verification, avoiding a numerical interval. We have


$$
0<c_0<\frac1{20},\qquad 5-r>\frac16,\qquad r>4,
$$


and


$$
2\rho<1,\qquad 5+2\rho<6.
$$


Therefore


$$
r(5-r)^{c_0}>4\,6^{-1/20}>2,
$$


whereas


$$
2\rho(5+2\rho)^{c_0}<6^{1/20}<2.
$$


The strict inequalities $6^{1/20}<2$ follow from $6<2^{20}$.

By continuity, there exists $\delta>0$ such that for


$$
\boxed{c_0<c<c_0+\delta}
\tag{14}
$$


the saddle lies in (13) and its value strictly exceeds the maximum on the positive support. This is a proved existence interval, not an unverified numerical interval.

### 6. Complete signed Laplace asymptotic

Fix $c$ in (14), and let integers $n\to\infty$, $m\ge0$ satisfy


$$
c_n=\frac mn\longrightarrow c.
$$


Choose an interior smooth cutoff $\chi$ equal to one near $T_c$, supported in (13). It also equals one near $T_{c_n}$ eventually.

Using the accepted exact transform,


$$
\sum_j\binom mj5^{m-j}\mathcal Z_{n+j}^{\rm ar}
=\sum_{h=0}^4\int D^h\!\left(T^n(5+T)^m\right)d\mu_h(T),
$$


integration by parts in the localized integrals gives


$$
\sum_h\int \chi f_h D^h g
=\int g\sum_h(D^*)^h(\chi f_h).
$$


Where $\chi=1$, the density is exactly $\mathcal F$. Every cutoff-derivative term is supported away from the saddle.

The unique negative maximizer and the positive-branch inequality give a strict exponential gap on the complement of a fixed saddle neighborhood. On that complement, the original moment integrals are bounded using their finite total variations and the accepted polynomial Euler-derivative bound. Thus both the cutoff terms and **all outside components** are exponentially smaller than the saddle contribution.

The curvature is


$$
\lambda(c)=-\phi_c''(T_c)
=\frac{(1+c)^3}{25c}>0.
$$


Ordinary interior Laplace expansion, uniformly for $c_n$ near $c$, now gives


$$
\boxed{
\begin{aligned}
\mathcal Z_{n,m}
&:=\sum_{j=0}^m\binom mj5^{m-j}Z_{n+j}\\
&=(-1)^n\mathcal F(T_{c_n})
\sqrt{\frac{2\pi}{n\lambda(c_n)}}\,
\left(\frac5{1+c_n}\right)^n
\left(\frac{5c_n}{1+c_n}\right)^m
(1+o(1)).
\end{aligned}}
\tag{15}
$$


This is for the **complete** numerator: the accepted bound for its exponential part is


$$
\exp(-n\log n+O_c(n)),
$$


which is negligible relative to (15). In particular, that bound includes the adjacent exponential endpoint correction and the separate $H_{k+1}W_k$ contribution.

Since $\mathcal F(T_{c_n})<0$, (15) proves eventual nonvanishing and


$$
\operatorname{sgn}\mathcal Z_{n,m}=(-1)^{n+1}.
\tag{16}
$$


It also handles arbitrary integer rounding with $m/n\to c$, rather than only exact proportional orders.

### 7. Final gcd, primitive error, and the primorial exclusion

Retain exactly the earlier rational pair. Set $N=n+m$,


$$
L_N=2^{N+1}(2N+2)!(N!)^4,
$$




$$
U=L_N\mathcal H_{n,m},\qquad V=L_N\mathcal J_{n,m},
\qquad g=\gcd(|U|,|V|),
$$


and


$$
P=-\operatorname{sgn}(V)\frac Ug,\qquad
q=\frac{|V|}{g}>0.
\tag{17}
$$


For $n$ beyond the inherited endpoint-sign threshold, $\mathcal J_{n,m}<0$ for every $m\ge0$, so this domain is valid. We have $\gcd(P,q)=1$, and the entire evaluated primitive error is


$$
\boxed{
q(e+\pi)-P=q\,\frac{\mathcal Z_{n,m}}{\mathcal J_{n,m}}.
}
\tag{18}
$$


Equations (15)–(16) prove its eventual nonvanishing and sign $(-1)^n$.

The accepted denominator-transform rate and (15) give the matching center-error rate


$$
\frac1n\log\left|e+\pi-\frac Pq\right|
\longrightarrow
\log\!\left[\frac5{1+c}
\left(\frac{5c}{1+c}\right)^c\right]
-\log d-c\log(5+d),
\quad d=2M^3.
\tag{19}
$$


In particular this is a finite real number.

Now let $N_x$ be the product of all odd primes at most $x$, and choose


$$
n_x=\left\lfloor\frac{N_x}{1+c}\right\rfloor,\qquad
m_x=N_x-n_x
$$


for a fixed $c$ in (14). Then $m_x/n_x\to c$, and the endpoint domain holds eventually. The audited bound concerns exactly the $q$ in (17):


$$
\liminf_{x\to\infty}
\frac{\log q}{N_x\log\log N_x}\ge2.
$$


Since (19) contributes only $O(N_x)$ to the logarithm of (18), we obtain


$$
\boxed{
\liminf_{x\to\infty}
\frac{\log|q(e+\pi)-P|}
{N_x\log\log N_x}\ge2.
}
\tag{20}
$$


Thus these primitive forms grow rather than shrink.

## Deliverables

### (1) New result and proof status

**Proved**, reusing the accepted exact transform and exponential bound:

- Actual analytic pushforward densities on an open interval to the right of $-r$.
- Corner Hessian $2\sqrt2 I_3$.
- All five polynomial-degree weights.
- Fourth-order vanishing of the degree-four weight.
- The nonzero total effective-density expansion (12).
- A complete signed Laplace asymptotic, including parity, integer rounding, cutoff gaps, outside components, and the factorial-small exponential part.
- Exclusion of the specified proportional-order odd-primorial subfamily, with the actual final gcd and primitive denominator retained.

### (2) Exact remaining bottleneck

For this scoped primorial subfamily, the requested lower-rate bottleneck is resolved. Nothing here determines a signed lower rate for every proportional order, excludes every filtered index family, or supplies the global final-gcd upper control needed by a different primitive-shrinking route. Irrationality of $e+\pi$ remains undecided.

### (3) Computation request

**None.** The endpoint coefficients, density survival, existence interval, and asymptotic exclusion above follow by exact algebra and local analytic arguments; no finite scan is used to establish an infinite assertion.
