> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A3: exact real moments and the proportional-order transform

Write


$$
\mathcal S=e+\pi,\qquad M=1+\sqrt2,\qquad \rho=M^{-1}=\sqrt2-1,
$$


and put


$$
r=2M,\qquad d=2M^3=14+10\sqrt2.
$$



The real-moment proposal works, with one important clarification: **the exponential deficit attached to $L_{k+1}$ uses the truncation indexed by $k$, not the truncation indexed by $k+1$**. Its integral therefore has an additional endpoint term. Keeping that term, and the separate term involving $H_{k+1}W_k$, gives a uniform factorial-small bound for the complete exponential contribution.

The resulting exact signed transform gives a substantially better upper rate than the unfiltered approximation at the same last index $N=n+m$, on an explicit range of proportional orders. It does not give a matching real lower bound or a sufficiently sharp upper bound for the actual reduced denominator.

## 1. Brief primorial audit

I reuse the established last-summand theorem, including its raw factor $k+1$, rather than reprove it. For $(a,b)=(1,5)$, every odd prime divisor of $N=n+m$ satisfies


$$
v_p(q_{n,m})\ge 2v_p(N!),
$$


where $q_{n,m}$ is the denominator **after the full cross-index endpoint gcd**.

The coordinator’s primorial consequence passes. Indeed, uniformly for $p\le N$,


$$
v_p(N!)=\frac{N}{p-1}+O\!\left(\frac{\log N}{\log p}+1\right).
$$


If $N_x$ is the product of the admissible odd primes through $x$, then


$$
\log q_{n,m}
\ge
2N_x\sum_{\substack{p\le x\\p\text{ admissible}}}
\frac{\log p}{p-1}
-O\bigl(\pi(x)\log N_x\bigr).
$$


The prime number theorem and partial summation give


$$
\log N_x\sim x,\qquad
\sum_{\substack{p\le x\\p\text{ admissible}}}\frac{\log p}{p-1}
\sim\log x.
$$


The error is $O(x^2/\log x)=o(N_x\log x)$. Consequently


$$
\boxed{\liminf_{x\to\infty}
\frac{\log q_{n,m}}{N_x\log\log N_x}\ge2.}
$$


Here the starting indices must lie in the established nonzero-endpoint domain.

This is a denominator **lower bound**. It is neither a denominator upper bound nor an exclusion of the filtered construction without a corresponding lower bound for its complete real error.

---

## 2. Exact decomposition of every component of $Z_k$

All identities in this section hold for integers $k\ge2$. Use the contiguous source’s unmodified scalars


$$
S_k,\quad C_k,\quad W_k,\quad f_k=\frac{2^k}{(k!)^2},\quad t=k+1.
$$


To avoid ambiguity in the truncation index, define


$$
T^{[k]}(Q)=\sum_u[t^u]Q(t)\,E_{k+u},
\qquad E_j=\sum_{v=0}^j\frac1{v!}.
$$


Thus the source’s $T_P,T_U$ are $T^{[k]}(L_k)$ and $T^{[k]}(L_{k+1})$.

The complete numerator and denominator are


$$
\begin{aligned}
\mathscr X_k={}&
2\bigl(w_k+T^{[k]}(L_k)\bigr)S_k\\
&-t^2\bigl(w_{k+1}+T^{[k]}(L_{k+1})\bigr)C_k
-2f_kH_{k+1}(1)W_k,\\
\mathscr D_k={}&t^2L_{k+1}(1)C_k-2L_k(1)S_k.
\end{aligned}
$$


The compensated output is


$$
Z_k=\frac{\mathscr X_k+\mathcal S\mathscr D_k}{(k!)^2}.
$$



Define the *unnormalized*, signed second-kind deficit


$$
\varepsilon_l=\pi L_l(1)-w_l,
$$


and the two exponential deficits actually needed at index $k$:


$$
\mathcal E_{k,0}=eL_k(1)-T^{[k]}(L_k),
\qquad
\mathcal E_{k,1}=eL_{k+1}(1)-T^{[k]}(L_{k+1}).
$$


Direct substitution gives the exact decomposition


$$
\boxed{Z_k=\mathcal Z_k^{\rm ar}+\mathcal Z_k^{\rm exp},}
\tag{1}
$$


where


$$
\boxed{
\mathcal Z_k^{\rm ar}
=\frac{t^2C_k\varepsilon_{k+1}-2S_k\varepsilon_k}{(k!)^2},
}
\tag{2}
$$


and


$$
\boxed{
\mathcal Z_k^{\rm exp}
=\frac{t^2C_k\mathcal E_{k,1}
-2S_k\mathcal E_{k,0}
-2f_kH_{k+1}(1)W_k}{(k!)^2}.
}
\tag{3}
$$


In particular, the last term of (3) is not part of the arctangent remainder and cannot be dropped.

### 2.1 Heine normalization and branch

Use the standard Legendre function


$$
Q_l(z)=\frac12\int_{-1}^{1}\frac{P_l(u)}{z-u}\,du,
\qquad z\notin[-1,1],
$$


with the branch obtained from its behavior at infinity. This specifies ordinary $Q_l$, not an unspecified Olver normalization.

The moment definition of $w_l$ gives


$$
\varepsilon_l
=\int_{-1}^{1}\frac{L_l((1+iu)/2)}{1-(1+iu)/2}\,du.
$$


Since


$$
L_l((1+iu)/2)=2^li^lP_l(u),
$$


we obtain


$$
\varepsilon_l=-2^{l+2}i^{l+1}Q_l(-i).
\tag{4}
$$



For ordinary $Q_l$, the Heine formula is


$$
Q_l(z)=\int_0^\infty
\bigl(z+\sqrt{z^2-1}\cosh v\bigr)^{-l-1}\,dv.
$$


Continue from $z>1$ into the lower half-plane, with


$$
\sqrt{z^2-1}\sim z\quad(z\to\infty).
$$


At $z=-i$, this means


$$
\sqrt{z^2-1}=-i\sqrt2,
$$


not $+i\sqrt2$. Inserting this into (4) proves


$$
\boxed{
\varepsilon_l
=4(-2)^l\int_0^\infty
(1+\sqrt2\cosh v)^{-l-1}\,dv.
}
\tag{5}
$$


The integral is absolutely convergent. Its sign is $(-1)^l$, agreeing with
$\varepsilon_0=\pi$ and $\varepsilon_1=2\pi-8$.

Equivalently, with


$$
u(v)=-\frac2{1+\sqrt2\cosh v},
\qquad
d\nu(v)=\frac{4\,dv}{1+\sqrt2\cosh v},
$$


we have


$$
\boxed{\varepsilon_l=\int u(v)^l\,d\nu(v),}
\tag{6}
$$


where $\nu$ is finite and positive, of total mass $\pi$, and


$$
-2\rho\le u(v)<0.
$$



### 2.2 Both exponential deficits, with the adjacent endpoint correction

Let


$$
\mathcal F_l(x)=x^lH_l(x),\qquad f_l=\frac{2^l}{(l!)^2}.
$$


The exact Rodrigues transform is


$$
f_l\mathcal F_l(x)
=\sum_u[t^u]L_l(t)\frac{x^{l+u}}{(l+u)!}.
\tag{7}
$$


Integrating against $e^{-x}$ on $[0,\infty)$ gives


$$
\boxed{
\int_0^\infty e^{-x}\mathcal F_l(x)\,dx
=(l!)^2\,2^{-l}L_l(1).
}
\tag{8}
$$



For every integer $q\ge0$,


$$
e-E_q=\frac{e}{q!}\int_0^1e^{-x}x^q\,dx.
$$


Thus (7) gives


$$
\boxed{
\mathcal E_{k,0}
=e f_k\int_0^1e^{-x}\mathcal F_k(x)\,dx.
}
\tag{9}
$$



For the adjacent polynomial, the relevant factorial index is


$$
k+u=(k+1)+u-1.
$$


Therefore it is the derivative of (7) that occurs:


$$
\mathcal E_{k,1}
=e f_{k+1}\int_0^1e^{-x}\mathcal F_{k+1}'(x)\,dx.
$$


Since $k+1\ge1$, integration by parts gives


$$
\boxed{
\mathcal E_{k,1}
=f_{k+1}H_{k+1}(1)
+e f_{k+1}\int_0^1e^{-x}\mathcal F_{k+1}(x)\,dx.
}
\tag{10}
$$


This extra endpoint term is the necessary clarification to the proposal. Formula (9) at $l=k+1$, without this correction, would represent the wrong truncation.

---

## 3. Exact fixed-degree polynomial moments for the arctangent part

Reuse the archive’s circle identity. Put


$$
z(\theta)=-\sqrt2e^{i\theta},\qquad
v(\theta)=-1-\sqrt2\cos\theta.
$$


Then


$$
-M\le v(\theta)\le\rho
$$


and, for every fixed nonnegative integer $a$,


$$
\frac{H_k^{(a)}(1)}{k!}
=\frac1{2\pi}\int_0^{2\pi}
z(\theta)^ae^{z(\theta)}v(\theta)^k\,d\theta.
\tag{11}
$$


Because $v(\theta)$ is real and the integral is real, we may replace the complex weight by its real part.

Introduce the real moments


$$
A_a(k)=\frac1{2\pi}\int_0^{2\pi}
\Re(z^ae^z)\,v^k\,d\theta,
$$




$$
B_a(k)=\frac1{2\pi}\int_0^{2\pi}
\Re(z^ae^z)\,v^{k+1}\,d\theta.
$$


Thus


$$
H_k^{(a)}(1)=k!A_a(k),\qquad
H_{k+1}^{(a)}(1)=t!B_a(k).
$$



The contiguous contractions simplify exactly to


$$
\boxed{
\frac{S_k}{(k!)^2}
=t^2\bigl(tB_0^2+B_1^2-B_0B_2\bigr),
}
\tag{12}
$$


and


$$
\boxed{
\frac{C_k}{(k!)^2}
=t\bigl(B_0A_0+kB_0A_1-tB_1A_0+B_1A_1-B_2A_0\bigr).
}
\tag{13}
$$


For example, (12) follows by substituting


$$
J_{k+1}=t!\,(tB_0+B_1),\quad
K_{k+1}=t!\,\bigl(t(t-1)B_0+2tB_1+B_2\bigr)
$$


into $S_k=J_{k+1}^2-H_{k+1}K_{k+1}$. In (13), the coefficient of $B_0A_0$ reduces to


$$
k^2-(t^2-2t)=1,
$$


which is why the apparent higher polynomial degree cancels.

Multiplying (12)–(13) by (6) resolves (2) into a finite sum of product integrals. Each has a factor


$$
\bigl(v(\theta_1)v(\theta_2)u(v)\bigr)^k,
$$


a bounded signed weight independent of $k$, and a polynomial amplitude in $k$ of degree at most $4$. Adjacent shifts contribute only extra bounded factors $v(\theta_i)$ or $u(v)$.

Now


$$
[-M,\rho]\cdot[-M,\rho]=[-1,M^2].
$$


Multiplying by $[-2\rho,0]$ proves the proposed support:


$$
\boxed{-2M\le T\le2\rho.}
\tag{14}
$$



More precisely, pushing forward the finite product measures yields finite real signed measures $\mu_0,\ldots,\mu_4$, independent of $k$, supported on $[-2M,2\rho]$, such that


$$
\boxed{
\mathcal Z_k^{\rm ar}
=\sum_{h=0}^{4}k^h\int_{-2M}^{2\rho}T^k\,d\mu_h(T),
\qquad k\ge2.
}
\tag{15}
$$


Equations (6), (12), and (13) are an explicit construction of these measures: expand the displayed polynomial factors in $k$, multiply their circle weights and $\nu$, include the indicated adjacent-shift factors, and push forward under $T=v_1v_2u$.

Thus (15) is an actual representation of the arctangent contribution, not a phase inferred from its leading single-index asymptotic. The measures are signed; no positivity assertion about their sum is made.

---

## 4. Uniform bound for the complete exponential contribution

Here all constants are absolute and independent of $k,n,m$.

From the circle formula, uniformly for $0\le x\le1$ and $a=0,1,2$,


$$
|H_k^{(a)}(x)|
\le k!\,(\sqrt2)^a e^{\sqrt2}M^k.
\tag{16}
$$


Consequently (9)–(10) imply


$$
|\mathcal E_{k,0}|+|\mathcal E_{k,1}|
\le C_1\frac{r^k}{k!}.
\tag{17}
$$


For example, one may take


$$
C_1=e^{\sqrt2}\bigl(e+(1+e)r\bigr).
$$



Equations (12)–(13) give


$$
\frac{|S_k|}{(k!)^2}
\le C_2t^3M^{2k},\qquad
\frac{|C_k|}{(k!)^2}
\le C_2t^2M^{2k}.
\tag{18}
$$


The remaining contraction satisfies


$$
|W_k|
=|J_{k+1}J_k-K_{k+1}H_k|
\le C_3t^3(k!)^2M^{2k+1},
\tag{19}
$$


while


$$
|H_{k+1}(1)|\le e^{\sqrt2}t\,k!M^{k+1}.
$$


Therefore the last term in (3), separately, obeys


$$
\frac{2f_k|H_{k+1}(1)W_k|}{(k!)^2}
\le C_4t^4\frac{d^k}{k!}.
\tag{20}
$$


Combining all three terms proves


$$
\boxed{
|\mathcal Z_k^{\rm exp}|
\le C_{\rm exp}(k+1)^4\frac{d^k}{k!},
\qquad k\ge2.
}
\tag{21}
$$


A deliberately loose explicit admissible constant is


$$
C_{\rm exp}=10^6e^{3\sqrt2}(1+e)M^4.
$$


No cancellation between the two deficits and the $H_{k+1}W_k$ term was needed.

For the actual weights $\binom mj5^{m-j}$, write $N=n+m$. Since


$$
(n+j)!\ge n!(n+1)^j,
$$


equation (21) gives the uniform estimate


$$
\boxed{
\left|
\sum_{j=0}^m\binom mj5^{m-j}\mathcal Z_{n+j}^{\rm exp}
\right|
\le
C_{\rm exp}(N+1)^4\frac{d^n}{n!}
\left(5+\frac d{n+1}\right)^m.
}
\tag{22}
$$


This holds for **every** $n\ge2,m\ge0$. In particular, if $m/n\to c<\infty$, its logarithm is


$$
-n\log n+O_c(n).
$$


It is therefore factorial-small even after proportional-order filtering.

---

## 5. Perform the actual binomial transform

Let


$$
\mathcal D_T=T\frac{d}{dT}.
$$


For each nonnegative integer $h$,


$$
\sum_{j=0}^m\binom mj5^{m-j}(n+j)^hT^{n+j}
=\mathcal D_T^h\!\left(T^n(5+T)^m\right).
$$


Thus (15), with no asymptotic substitution, gives


$$
\boxed{
\sum_{j=0}^m\binom mj5^{m-j}\mathcal Z_{n+j}^{\rm ar}
=
\sum_{h=0}^4\int
\mathcal D_T^h\!\left(T^n(5+T)^m\right)d\mu_h(T).
}
\tag{23}
$$



The support lies strictly to the right of $-5$:


$$
5+T\ge5-2M>0.
$$


Repeated Euler differentiation therefore yields, for $0\le h\le4$,


$$
\left|\mathcal D_T^h\!\left(T^n(5+T)^m\right)\right|
\le C_h(N+1)^h|T|^n(5+T)^m
$$


throughout the support. This follows either by induction or by expanding derivatives into falling factorials and powers of $T/(5+T)$, which is uniformly bounded there.

Taking total variations in (23), and then adding (22), proves the complete uniform bound


$$
\boxed{
\begin{aligned}
\left|\sum_{j=0}^m\binom mj5^{m-j}Z_{n+j}\right|
\le{}&
C(N+1)^4
\max_{-r\le T\le2\rho}|T|^n(5+T)^m\\
&+
C_{\rm exp}(N+1)^4\frac{d^n}{n!}
\left(5+\frac d{n+1}\right)^m .
\end{aligned}}
\tag{24}
$$


It includes the entire evaluated error.

### 5.1 The interior negative saddle and positive branch

For $c>0$, set


$$
\mathcal B(c)=
\max\{\mathcal B_-(c),\mathcal B_+(c)\},
$$


where


$$
\boxed{
\mathcal B_-(c)=x_c(5-x_c)^c,\qquad
x_c=\min\left(r,\frac5{1+c}\right),
}
\tag{25}
$$


and


$$
\boxed{
\mathcal B_+(c)=2\rho(5+2\rho)^c.
}
\tag{26}
$$


Indeed,


$$
\frac{d}{dx}\log\bigl(x(5-x)^c\bigr)
=\frac1x-\frac c{5-x},
$$


so the negative branch has its interior maximum at $x=5/(1+c)$ when that point lies below $r$. The positive branch is increasing and has its maximum at $T=2\rho$.

This retains both components requested in the assignment. In particular, replacing $\mathcal B_-(c)$ by the endpoint expression $r(5-r)^c$ after the saddle moves into the interior would be incorrect.

---

## 6. Complete center-error rate and comparison at the same $N$

Let


$$
\mathcal J_{n,m}=\sum_{j=0}^m\binom mj5^{m-j}J_{n+j}.
$$


The inherited endpoint theorem gives one sign for all sufficiently large indices and


$$
J_{k+1}/J_k\longrightarrow d.
$$


Consequently, for $m/n\to c>0$,


$$
\boxed{
\log|\mathcal J_{n,m}|
=n\log d+m\log(5+d)+o(n).
}
\tag{27}
$$


For completeness, sandwich the consecutive ratios between $d-\eta$ and $d+\eta$, use the binomial theorem and the common sign, and let $\eta\downarrow0$. Also $\log|J_n|=n\log d+o(n)$.

Define


$$
c_{n,m}=-\frac{\mathcal H_{n,m}}{\mathcal J_{n,m}}.
$$


Equations (24) and (27) prove


$$
\boxed{
\limsup_{\substack{n\to\infty\\m/n\to c}}
\frac1n\log|\mathcal S-c_{n,m}|
\le
\log\mathcal B(c)-\log d-c\log(5+d).
}
\tag{28}
$$


The convention $\log0=-\infty$ is allowed. Nonvanishing on the established arithmetic subsequences is retained below, rather than inferred from this upper bound.

### Same-last-index improvement

The unfiltered complete error at $N=n+m$ has rate


$$
-2N\log M+o(N).
$$


Set


$$
\alpha=\frac{5+d}{M^2}=2M+\frac5{M^2}.
$$


Then the difference between the right side of (28) and the unfiltered exponent $-(1+c)2\log M$ is


$$
\log\frac{\mathcal B(c)}{r\alpha^c}.
\tag{29}
$$



Notice that $\alpha>5$. For every $0\le x\le r$ and every $c>0$,


$$
\frac{x(5-x)^c}{r\alpha^c}<1.
$$


Hence the entire negative branch, including its interior saddle, strictly improves on the same-$N$ unfiltered rate.

For the positive branch,


$$
5+2\rho=M^2,\qquad \frac{2\rho}{r}=M^{-2}.
$$


Thus


$$
\frac{\mathcal B_+(c)}{r\alpha^c}
=M^{-2}\left(\frac{M^2}{\alpha}\right)^c.
$$


Since $M^2>\alpha$, define


$$
\boxed{
c_*=
\frac{2\log M}
{\log\!\left(M^4/(5+d)\right)}.
}
\tag{30}
$$


The denominator is positive. We obtain the explicit conclusion


$$
\boxed{
0<c<c_*
\quad\Longrightarrow\quad
\text{the proved complete filtered upper rate is strictly better
than the unfiltered rate at }N=n+m.
}
\tag{31}
$$


At $c=c_*$, the positive-branch bound equals the unfiltered rate. For $c>c_*$, this particular upper bound no longer establishes same-$N$ improvement.

A simple exact example is $c=1$. Here


$$
x_c=\frac52,\qquad
\mathcal B_-(1)=\frac{25}{4},\qquad
\mathcal B_+(1)=2M<\frac{25}{4}.
$$


Therefore


$$
\boxed{
\limsup_{\substack{n\to\infty\\m/n\to1}}
\frac1n\log|\mathcal S-c_{n,m}|
\le
\log\frac{25}{4d(5+d)}.
}
\tag{32}
$$


This is a genuine signed-transform gain for the actual compensated outputs, not the geometric-model prediction $(5-r)^m$.

---

## 7. Actual primitive denominator, whole error, and nonvanishing

No new normalization is introduced.

For $N=n+m$, take the established common clearer


$$
L_N=2^{N+1}(2N+2)!(N!)^4
$$


and define


$$
U=L_N\mathcal H_{n,m},\qquad
T=L_N\mathcal J_{n,m}.
$$


For $n$ above the inherited endpoint-sign threshold, $T\ne0$ for every $m\ge0$. Put


$$
g=\gcd(|U|,|T|),
$$




$$
\boxed{
P=-\operatorname{sgn}(T)\frac Ug,\qquad
q=\frac{|T|}{g}>0.
}
\tag{33}
$$


Then $c_{n,m}=P/q$ is in lowest terms, and the complete primitive error is exactly


$$
\boxed{
q\mathcal S-P
=
q\,\frac{\displaystyle
\sum_{j=0}^m\binom mj5^{m-j}Z_{n+j}}
{\mathcal J_{n,m}}.
}
\tag{34}
$$



The established last-summand theorem applies whenever an odd prime $p\mid N$, and gives


$$
v_p(q)\ge2v_p(N!).
$$


In particular, along $3\mid N$, with $n$ above the sign threshold and $N\to\infty$, we have $q\to\infty$. The already-proved rational/irrational case distinction then gives eventual nonvanishing of (34), unconditionally. This includes proportional-order subsequences within that domain.

The new bound (28) concerns the error in (34) before multiplication by the **actual** $q$. The current general upper estimate


$$
\log q\le6N\log N+O(N)
$$


is still much too large to establish primitive shrinking. Conversely, the primorial lower bound cannot be combined with an error upper bound to prove primitive growth.

---

## 8. Secondary audit: A2’s restricted-analytic root-disk extension

**Pass for the restricted-analytic and small-carry mechanism; no independent numerical certification of the stated tangent table or unavailable determinant circuit is asserted here.**

The points requiring particular care are sound:

1. **Gauss convergence.** For $x=r+pT$,
   

$$
v_{\rm G}((x)_j)\ge\lfloor j/p\rfloor.
$$


   Combining this with the denominator of $\binom{x}{j}$ gives
   

$$
v_{\rm G}\!\left((x)_{s+d}\binom{x}{j}\right)
   \ge m-v_p(m!),\qquad m=\lfloor s/p\rfloor.
$$


   This tends to infinity and establishes restricted-analytic convergence of the stated scalar sums. The proposed all-depth truncation is conservative and valid.

2. **The $pT^2$ carry is real.** For $2r<p$, $p\le s<2p$, the coefficient contribution is
   

$$
a_{p+j}(r+pT)\equiv-T a_j(r)\pmod p,
$$


   while the falling-factorial contribution divided by $p$ is
   

$$
-T(r)_{j+d}\pmod p
$$


   in its nonzero range. Their product produces $pT^2$, not merely a linear $pT$ term. Terms $s\ge2p$ vanish modulo $p^2$ for the claimed $p\ge5$ domain.

3. **The auxiliary $\mathscr D$-factors do not introduce an omitted quadratic term at this order.** Their defining falling-factorial polynomials have integral coefficients. Modulo $p^2$, their residue-disk expansions are linear in the displacement $pT$; sufficiently long terms vanish in Gauss valuation. In the $p\le s<2p$ carry range, only their mod-$p$ values are needed.

4. **Degree-six homogeneity has exactly the asserted effect.** If the normalized contraction polynomial is homogeneous of degree six in the five scalar-state variables, then a common perturbation $pT^2\mathbf S_r$ contributes
   

$$
pT^2\sum_iS_i\partial_{S_i}\mathcal V
   =6pT^2\mathcal V_r.
$$


   On a root residue $p\mid\mathcal V_r$, that term vanishes modulo $p^2$. The surviving first-order slope includes the explicit $n$-derivative as well as the scalar tangent.

Thus the claimed root-disk form follows from the stated homogeneous determinant construction. Its simple-root/isometry consequence is also correct. Numerical slopes still require the specified finite determinant evaluations; homogeneity alone does not determine them.

---

## (1) New result and proof status

**Proved from the supplied exact endpoint identities and standard Legendre integral formulas:**

- The signed Heine representation (5), with ordinary $Q_l$ normalization and the correct lower-half-plane branch.
- The complete decomposition (1)–(3), retaining both exponential deficits and the term $-2f_kH_{k+1}W_k$.
- The adjacent exponential-deficit correction (10).
- The exact degree-at-most-four signed moment representation (15), supported on
  

$$
[-2M,2/M].
$$


- The complete factorial-small exponential bound (22), uniform for all $n\ge2,m\ge0$.
- The actual $(1,5)$ binomial transform (23), its complete bound (24), and the proportional-order rate (28), retaining the interior negative saddle and positive branch.
- Strict improvement of that upper rate over the unfiltered error at the same $N=n+m$, for $0<c<c_*$.

**Audited:** the primorial consequence as a denominator lower bound, and A2’s analytic carry/homogeneity mechanism within its stated structural scope.

**Not proved:** a matching signed asymptotic or real lower bound for the transformed numerator, primitive shrinking, primitive growth on primorial indices, or irrationality of $e+\pi$.

## (2) Exact remaining bottleneck

The analytic representation is no longer missing. The next concrete analytic obligation is to determine whether the signed measures in (15) have a nonzero surviving amplitude at the maximizing negative saddle or positive endpoint after their degree-four Euler combination. That requires analyzing the explicit product weights from (12)–(13), not assuming positivity of $\mu_h$ or replacing the support maximum by an attained lower bound.

Independently, a primitive shrinking argument still needs a sufficiently sharp upper estimate for


$$
\frac{|L_N\mathcal J_{n,m}|}
{\gcd(|L_N\mathcal H_{n,m}|,\ |L_N\mathcal J_{n,m}|)}.
$$


The new analytic gain does not determine this final gcd.

## (3) Computation request

**None for the results proved above.** Their infinite statements follow from exact identities and uniform bounds. No finite error or gcd scan would resolve the remaining signed-amplitude or primitive-denominator bottleneck.
