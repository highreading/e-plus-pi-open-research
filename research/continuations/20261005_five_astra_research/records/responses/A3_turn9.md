> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A3 turn 9: the bounded-rounding transition at $c_0$

The proposed boundary-Gaussian mechanism **passes**, but its sign is important: at the transition the complete numerator has sign $(-1)^n$, rather than the sign $(-1)^{n+1}$ found on the nearby fixed-order negative-endpoint and negative-interior regimes.

The resulting whole primitive error has sign $(-1)^{n+1}$. This proves the missing scoped primorial exclusion at $c_0$.

I also obtain a uniform transition profile. It has at least two real zeros, so the transition cannot be extended to arbitrary approaching orders merely by invoking its nonzero value at zero.

## 1. Exact inputs and constants

Use the actual transform and densities derived in A3 turns 5–6 and independently checked in A4 turn 7. Set


$$
b=\sqrt2,\quad M=1+b,\quad r=2M,\quad p=2/M,\quad d=2M^3,
$$


and


$$
h=5-r>0,\qquad c_0=\frac hr=\frac5r-1.
$$


Here $h$ is a constant, not a polynomial-degree index.

The complete numerator is


$$
\mathcal Z_{n,m}
=\sum_{j=0}^{m}\binom mj5^{m-j}Z_{n+j},
\qquad n\ge2,\quad m\ge0.
$$


Its arctangent part is exactly


$$
\mathcal Z^{\rm ar}_{n,m}
=\sum_{\ell=0}^{4}\int D^\ell\!\left(T^n(5+T)^m\right)d\mu_\ell(T),
\qquad D=T\partial_T.
\tag{1}
$$



Writing $T=-r+s$, the **actual total densities** near $s=0$ satisfy


$$
\begin{aligned}
f_3(-r+s)&=AKs^{1/2}+O(s^{3/2}),\\
f_2(-r+s)&=3AKs^{1/2}+O(s^{3/2}),\\
f_1(-r+s)&=3AKs^{1/2}+O(s^{3/2}),\\
f_0(-r+s)&=AKs^{1/2}+O(s^{3/2}),\\
f_4(-r+s)&=K\frac{1-2b}{15M}s^{5/2}+O(s^{7/2}),
\end{aligned}
\tag{2}
$$


where


$$
A=-2bM<0,\qquad
K=\frac{e^{-2b}}{\pi M b^{3/2}}>0.
\tag{3}
$$


The remainders in (2) are analytic after removing the indicated half-integer powers. No new positive-measure assumption is made.

The phase at the transition is


$$
\phi(T)=\log(-T)+c_0\log(5+T).
$$


It satisfies


$$
\phi'(-r)=0,\qquad
a:=-\phi''(-r)
=\frac1{r^2}+\frac{c_0}{h^2}
=\boxed{\frac5{r^2h}}>0.
\tag{4}
$$


Thus


$$
\phi(-r+s)-\phi(-r)=-\frac a2s^2+O(s^3).
\tag{5}
$$



The tools below are classical direct Laplace/Watson scaling. In particular, I do **not** integrate the singular endpoint densities by parts.

## 2. Bounded integer rounding: precise asymptotic

Fix $B<\infty$. Consider all integer pairs satisfying


$$
n\to\infty,\qquad m\ge0,\qquad
\beta=m-c_0n,\qquad |\beta|\le B.
\tag{6}
$$


Define the exact endpoint factor


$$
R_{n,m}=r^nh^m>0.
$$



Near the negative endpoint,


$$
T^n(5+T)^m
=(-1)^nR_{n,m}
 \exp\!\left(n[\phi(-r+s)-\phi(-r)]\right)
 \left(1+\frac sh\right)^\beta.
\tag{7}
$$


The rounding factor has not been absorbed into an unspecified exponential:
its value at the endpoint is already retained in $h^m$.

With $s=x/\sqrt n$, (7) becomes


$$
(-1)^nR_{n,m}
\left[e^{-ax^2/2}+O_B(n^{-1/2})\right]
\tag{8}
$$


in the usual Gaussian-weighted, polynomially weighted derivative norms needed through order four.

More explicitly, the exponent correction on bounded $x$-sets is


$$
n^{-1/2}
\left(\frac{\phi'''(-r)}6x^3+\frac{\beta}{h}x\right)
+O_B\!\left(n^{-1}(x^4+x^2)\right).
\tag{9}
$$


This verifies that bounded rounding affects the first correction, not the leading constant.

### Euler terms and all measure orders

The exact operator identity is


$$
D^\ell
=\sum_{j=0}^{\ell}
\left\{\!\begin{matrix}\ell\\j\end{matrix}\!\right\}
T^j\partial_s^j,
\tag{10}
$$


where the braces are Stirling numbers of the second kind. After scaling,


$$
D^\ell
=n^{\ell/2}(-r)^\ell\partial_x^\ell
+\text{terms smaller by at least }n^{-1/2}.
\tag{11}
$$



For a density beginning with $s^\alpha$, its leading contribution has order


$$
n^{\ell/2-(\alpha+1)/2}.
\tag{12}
$$


Consequently:

| Degree $\ell$ | Density order | Maximum contribution, divided by $R_{n,m}$ |
|---|---:|---:|
| $3$ | $s^{1/2}$ | $n^{3/4}$ |
| $4$ | $s^{5/2}$ | $n^{1/4}$ |
| $2$ | $s^{1/2}$ | $n^{1/4}$ |
| $1$ | $s^{1/2}$ | $n^{-1/4}$ |
| $0$ | $s^{1/2}$ | $n^{-3/4}$ |

The next density term in $f_3$, the variation of $T^3$, the lower derivatives in $D^3$, and the exponent and rounding corrections in (9) all contribute $O_B(n^{1/4}R_{n,m})$. Thus every lower Euler and measure term is controlled at the claimed relative order.

For rigor beyond bounded $x$-sets, choose a sufficiently small fixed endpoint interval. There,


$$
\phi(-r+s)-\phi(-r)\le-\kappa s^2
$$


for some $\kappa>0$. Differentiating the exact exponential through order four produces polynomial bounds in $x$ times a Gaussian majorant. Taylor’s theorem, followed by Gaussian integration, gives the same $O_B(n^{-1/2})$ relative scale. This supplies an integrable majorant and justifies the asymptotic integration.

### The leading integral is positive

Direct differentiation gives


$$
\partial_x^3e^{-ax^2/2}
=(3a^2x-a^3x^3)e^{-ax^2/2}.
$$


Therefore


$$
I_0:=\int_0^\infty x^{1/2}\partial_x^3e^{-ax^2/2}\,dx
=3a^2M_{3/2}-a^3M_{7/2},
$$


where


$$
M_\gamma=\int_0^\infty x^\gamma e^{-ax^2/2}\,dx.
$$


The Gaussian moment recurrence gives


$$
M_{7/2}=\frac{5}{2a}M_{3/2}.
$$


Hence


$$
I_0=\frac{a^2}{2}M_{3/2}
=2^{-3/4}a^{3/4}\Gamma(5/4)>0.
\tag{13}
$$


This calculation uses convergent Gaussian moments, not endpoint integration by parts against $s^{1/2}$.

Since both $A$ and $(-r)^3$ are negative, the final coefficient


$$
\boxed{
C_0=(-r)^3AK\,I_0
=2bMr^3K\,2^{-3/4}a^{3/4}\Gamma(5/4)>0
}
\tag{14}
$$


is positive.

## 3. Both global gaps and the complete exponential correction

There are two separate global issues.

* On the negative branch, $\phi$ has its unique maximum at $-r$. Outside any fixed endpoint neighborhood, its maximum is strictly smaller. The same gap persists uniformly under (6).
* The positive-support maximum is strictly below the negative endpoint value at $c_0$, as established by the exact inequalities in A3 turn 6. Continuity preserves that gap for $m/n=c_0+O(n^{-1})$.

Using the finite total variations of the original measures and the polynomial Euler bound, all these outside contributions are


$$
O_B\!\left(R_{n,m}n^4e^{-\eta n}\right)
\tag{15}
$$


for some $\eta>0$.

The **entire** exponential correction satisfies the supplied exact bound


$$
|\mathcal Z^{\rm exp}_{n,m}|
\le C(N+1)^4\frac{d^n}{n!}
       \left(5+\frac d{n+1}\right)^m,\qquad N=n+m.
\tag{16}
$$


Its logarithm is at most $-n\log n+O_B(n)$, whereas
$\log R_{n,m}=O_B(n)$. It is negligible here. Bound (16) includes both exponential deficits, the adjacent truncation endpoint correction, and the separate $H_{k+1}W_k$ term.

Combining these facts proves the complete law


$$
\boxed{
\mathcal Z_{n,m}
=(-1)^n C_0\,n^{3/4}r^n(5-r)^m
\left(1+O_B(n^{-1/2})\right).
}
\tag{17}
$$


It holds uniformly on (6), and proves eventual nonvanishing there.

## 4. Actual denominator, final gcd, and primitive-error sign

Retain the actual rational transforms $\mathcal H,\mathcal J$, not an auxiliary denominator. Their inherited theorem gives


$$
\mathcal J_{n,m}<0
$$


once $n$ exceeds the endpoint-sign threshold, for every $m\ge0$, and


$$
\log|\mathcal J_{n,m}|
=n\log d+m\log(5+d)+o(n)
\tag{18}
$$


on the present domain.

Put


$$
L_N=2^{N+1}(2N+2)!(N!)^4,\quad
U=L_N\mathcal H_{n,m},\quad V=L_N\mathcal J_{n,m},
$$




$$
g=\gcd(|U|,|V|),\qquad
P=-\operatorname{sgn}(V)\frac Ug,\qquad
q=\frac{|V|}{g}>0.
\tag{19}
$$


Then $\gcd(P,q)=1$, and the whole evaluated primitive error is exactly


$$
\boxed{
q(e+\pi)-P=q\,\frac{\mathcal Z_{n,m}}{\mathcal J_{n,m}}.
}
\tag{20}
$$


Thus, uniformly for bounded rounding at $c_0$,


$$
\boxed{\operatorname{sgn}\bigl(q(e+\pi)-P\bigr)=(-1)^{n+1}}
\tag{21}
$$


eventually. In particular, this error is nonzero without assuming anything about the rationality of $e+\pi$.

The matching center-error rate is


$$
\boxed{
\frac1n\log\left|e+\pi-\frac Pq\right|
\longrightarrow
\log r+c_0\log(5-r)-\log d-c_0\log(5+d).
}
\tag{22}
$$



For the specified odd primorial $N_x$, take


$$
n_x=\left\lfloor\frac{N_x}{1+c_0}\right\rfloor,\qquad
m_x=N_x-n_x.
$$


Then


$$
0\le m_x-c_0n_x<1+c_0,
$$


so (17) applies. Combining (22) with the accepted lower bound for the **same reduced denominator** in (19) yields


$$
\boxed{
\liminf_{x\to\infty}
\frac{\log|q(e+\pi)-P|}
 {N_x\log\log N_x}\ge2.
}
\tag{23}
$$


This adds $c_0$ to the scoped primorial exclusion.

## 5. Uniform transition profile—and genuine zeros

For a broader transition let


$$
\tau_n=\frac{m-c_0n}{h\sqrt n}
$$


remain in a fixed compact real set. The same direct argument gives the absolute uniform expansion


$$
\boxed{
\mathcal Z_{n,m}
=(-1)^nr^nh^mn^{3/4}
\left[\Psi(\tau_n)+O(n^{-1/2})\right],
}
\tag{24}
$$


where


$$
\boxed{
\Psi(\tau)=(-r)^3AK
\int_0^\infty x^{1/2}
\partial_x^3e^{-ax^2/2+\tau x}\,dx.
}
\tag{25}
$$


The error in (24) is absolute, not relative near a zero.

This real-analytic profile satisfies


$$
\Psi(0)=C_0>0.
$$


It also takes negative values on both sufficiently distant sides.

Indeed, writing $I(\tau)$ for the integral in (25), endpoint scaling at $\tau=-L$ gives


$$
I(-L)\sim-\Gamma(3/2)L^{3/2}\qquad(L\to+\infty).
\tag{26}
$$


For $\tau=L$, localize near the interior Gaussian center $x=L/a$. Integration by parts is legitimate on this **interior localization**. Since


$$
(x^{1/2})'''=\frac38x^{-5/2},
$$


the saddle contribution is


$$
I(L)\sim
-\frac38\left(\frac La\right)^{-5/2}
\sqrt{\frac{2\pi}{a}}\,e^{L^2/(2a)}<0.
\tag{27}
$$


Cutoff and endpoint pieces are exponentially smaller than this saddle contribution. As $(-r)^3AK>0$, (26)–(27) imply:



$$
\boxed{\Psi\text{ has at least one negative and at least one positive real zero.}}
\tag{28}
$$



These are cancellations within the negative-endpoint transition contribution itself. Parity multiplies the entire profile by $(-1)^n$; it does not remove its zeros. The positive support branch remains exponentially separated in this window.

Near a profile zero, integer changes in $m$ alter $\tau_n$ by $1/(h\sqrt n)$, precisely the scale of the first omitted term in (24). A lower bound there therefore needs higher uniform coefficients together with control of the integer lattice’s proximity to the corrected zero. Formula (24) alone does not settle arbitrary integer sequences approaching such a zero.

## 6. Separate finite-$\mathcal E$ question: a structural obstruction to complete odd cancellation

I do not have an unconditional resolution for every point of the finite exceptional set $\mathcal E$. The following criterion uses the actual endpoint singularity and gives more than analyticity alone.

Fix a negative interior saddle $T_c$. Let $\iota_c$ be the phase-preserving involution between its two sides:


$$
\phi_c(\iota_c(T))=\phi_c(T).
$$


If every even Morse coefficient of
$\mathcal F(T(z))T'(z)$ vanishes, that analytic amplitude is odd. Since


$$
\phi_c'(T(z))T'(z)=-z,
$$


this forces the exact identity


$$
\boxed{
\frac{\mathcal F(T)}{\phi_c'(T)}
=
\frac{\mathcal F(\iota_c(T))}
     {\phi_c'(\iota_c(T))}
}
\tag{29}
$$


near the saddle and wherever analytic continuation of the two branches is valid.

Suppose the right-side point paired with $T=-r$ lies strictly in the density-analytic interval $(-r,-2\rho^3)$. Then (29) is impossible: the left side diverges like a nonzero multiple of $(T+r)^{-5/2}$, because


$$
\phi_c'(-r)=-\frac1r+\frac c{5-r}\ne0,
$$


while the right side remains finite at a regular nonsaddle point. Thus:

> **If the phase-paired right branch reaches the level $\phi_c(-r)$ before leaving the known density-analytic interval, some even Morse coefficient must survive.**

This is a proved conditional criterion based on the actual nonzero endpoint singularity. It does not cover exceptional orders whose paired right branch crosses the next critical value first. Resolving that case requires further information about the actual continued densities or their differential identities, not merely the fact that $\mathcal F$ is analytic and nonzero.

## Closing ledger

### (1) New result and proof status

**Proved:** the complete bounded-rounding transition law (17), its explicit positive constant, all lower Euler/measure error orders, both global phase gaps, eventual nonvanishing, actual primitive-error sign, and the extension (23) of the scoped primorial exclusion to $c_0$.

**Also proved:** the uniform profile (24)–(25), existence of real profile zeros on both sides of zero, and the conditional structural criterion (29) excluding complete odd-Morse cancellation when the paired branch stays in the known analytic interval.

### (2) Exact remaining bottleneck

Arbitrary transition sequences near profile zeros require higher uniform coefficients and integer-lattice proximity control. The finite-$\mathcal E$ problem remains unresolved where the phase-paired branch encounters another density critical value. Independently, none of these exclusion results supplies a route proving irrationality or rationality of $e+\pi$.

### (3) Computation request

**None.** The first required transition result is established analytically. A finite plot of the profile or the effective density would not resolve either remaining infinite-sequence cancellation problem.
