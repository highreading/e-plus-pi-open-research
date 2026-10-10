> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A3 turn 8: the two endpoint laws and a generic-domain signed-rate theorem

The negative-density continuation can be proved on the entire requested interval. In addition, the positive endpoint has a **nonzero degree-four weight**, yielding a different polynomial order from either the negative endpoint or an interior negative saddle.

Together these give a complete logarithmic rate for every fixed proportional order $c>0$, apart from:

* the transition $c=c_0$;
* a **finite, explicitly defined but not yet evaluated set** of zeros of the negative interior effective amplitude;
* unrestricted approaches to the phase-switch order $c=c_{\mathrm s}$.

At $c_{\mathrm s}$, ordinary bounded integer rounding is covered: the positive endpoint wins by a factor of order $n^3$. Unrestricted approaches require care because the two phases can balance in a logarithmic transition window.

No conclusion decides irrationality of $e+\pi$.

## 1. Notation and exact quantities retained

Set


$$
b=\sqrt2,\qquad M=1+b,\qquad \rho=M^{-1},\qquad
 r=2M,\qquad p=2\rho,\qquad d=2M^3.
$$


Here $p$ denotes the positive support endpoint, not a prime.

Retain the exact compensated sequences and their filter:


$$
Z_k=H_k+(e+\pi)J_k,\qquad
\mathcal Z_{n,m}=\sum_{j=0}^{m}\binom mj5^{m-j}Z_{n+j},
\quad n\ge2,\quad m\ge0.
$$


Thus the factorial compensation is still the source’s exact one:


$$
H_k=\frac{\mathscr X_k}{(k!)^2},
\qquad J_k=\frac{\mathscr D_k}{(k!)^2}.
$$


Write $\mathcal H,\mathcal J$ for the corresponding transforms of $H,J$.

I use the accepted exact representation


$$
\mathcal Z^{\rm ar}_{n,m}
 =\sum_{h=0}^{4}\int D^h\!\left(T^n(5+T)^m\right)d\mu_h(T),
 \qquad D=T\partial_T,
\tag{1}
$$


and the accepted bound for the **entire exponential correction**


$$
\left|\mathcal Z^{\rm exp}_{n,m}\right|
\le C(N+1)^4\frac{d^n}{n!}
       \left(5+\frac d{n+1}\right)^m,
\qquad N=n+m.
\tag{2}
$$


In particular, (2) retains both exponential deficits, the adjacent truncation endpoint term, and the separate $H_{k+1}W_k$ term. If $m/n$ remains bounded, its logarithm is at most


$$
-n\log n+O(n).
\tag{3}
$$



The measure map is


$$
T=v_1v_2u(y),\quad
v_i=-1-b\cos\theta_i,\quad
u(y)=-\frac2{1+b\cosh y},\quad y\ge0.
\tag{4}
$$


The five weights $A_h$ are exactly those in A3 turn 6:


$$
\begin{aligned}
A_4&=uF,\\
A_3&=u(3F+G)-2B,\\
A_2&=u(3F+3G)-2(3B+D_0),\\
A_1&=u(F+3G)-2(3B+2D_0),\\
A_0&=uG-2(B+D_0).
\end{aligned}
\tag{5}
$$


I write $D_0$ for that report’s product weight $D$, to distinguish it from the Euler operator.

## 2. All five total densities are analytic on $(-r,-2\rho^3)$

### 2.1 Exhaustion of the nonzero critical values

Extend $y$ evenly to the whole real line and divide the resulting measure by two. This removes the boundary $y=0$.

At a point where $T\ne0$, both $v_i$ and $u$ are nonzero. Consequently


$$
\partial_{\theta_1}T=\partial_{\theta_2}T=\partial_yT=0
$$


forces


$$
\sin\theta_1=\sin\theta_2=0,\qquad y=0.
$$


Indeed, $u'(y)=0$ only at $y=0$. Thus the nonzero critical values are exactly


$$
\begin{array}{c|c}
(v_1,v_2)&T\\ \hline
(-M,-M)&-2M=-r\\
(-M,\rho),\;(\rho,-M)&2\rho=p\\
(\rho,\rho)&-2\rho^3.
\end{array}
\tag{6}
$$


Possible critical points with a zero circle factor have $T=0$, outside the interval in question. There are therefore **no other critical values between $-r$ and $-2\rho^3$**.

### 2.2 Proper analytic fiber integration

For every compact interval


$$
I\Subset(-r,-2\rho^3),
$$


its preimage has bounded $y$, because


$$
|T|\le M^2|u(y)|\longrightarrow0\quad (|y|\to\infty).
$$


Hence the map is proper over $I$.

The original product weights, without introducing any division by circle weights, are real analytic in $(\theta_1,\theta_2,y)$. The map is a submersion over $I$. To justify analytic, rather than merely smooth, dependence of the pushforward, use the analytic vector field


$$
X=\frac{\nabla T}{|\nabla T|^2}
$$


on a neighborhood of the compact preimage of a slightly larger interval. Its analytic flow satisfies $XT=1$, and analytically identifies nearby fibers with a fixed compact fiber. In these coordinates each pushed-forward density is an integral, over that fixed fiber, of an analytic density depending analytically on $T$. Compactness gives a common local analytic neighborhood and justifies integration of its convergent parameter expansion.

It follows that the **total actual pushforward densities**


$$
d\mu_h(T)=f_h(T)\,dT
$$


are real analytic throughout


$$
\boxed{(-r,-2\rho^3),\qquad 0\le h\le4.}
\tag{7}
$$


This includes all preimages, not only the negative corner component.

Accordingly,


$$
\mathcal F(T)=\sum_{h=0}^{4}(D^*)^hf_h(T),
\qquad D^*f=-(Tf)',
\tag{8}
$$


is real analytic on the same connected interval.

The established endpoint expansion is


$$
\mathcal F(-r+s)
=-\frac34bMr^3K\,s^{-5/2}+O(s^{-3/2}),
\qquad
K=\frac{e^{-2b}}{\pi M b^{3/2}}>0.
\tag{9}
$$


Thus $\mathcal F$ is not identically zero. Its zeros in (7) are isolated.

## 3. Positive endpoint: both corners, Hessian, and all five amplitudes

The maximum $T=p$ has exactly two attaining corners:


$$
(v_1,v_2,y)=(-M,\rho,0),\qquad(\rho,-M,0).
\tag{10}
$$


Each angular coordinate is a local signed coordinate on its circle. There is no extra multiplicity from representing $0$ and $2\pi$ separately.

At the first corner,


$$
q_1=-b,\quad q_2=b,\quad h_1=h_2=b^2=2.
$$


Using the exact symmetric weights gives


$$
\begin{aligned}
F&=\tfrac12(-M-\rho)(2b)=-4,\\
G&=\tfrac12\{-M(-3+b)+\rho(-3-b)\}=1,\\
B&=-1,\qquad D_0=4.
\end{aligned}
\tag{11}
$$


In particular,


$$
\boxed{A_4=uF=8\rho>0.}
\tag{12}
$$


All five corner values, at either corner, are


$$
\boxed{
\begin{array}{c|c}
h&A_h\\ \hline
4&8\rho\\
3&22\rho+2\\
2&18\rho-2\\
1&2\rho-10\\
0&-2\rho-6.
\end{array}}
\tag{13}
$$



Take coordinates $\alpha=\theta_1$, $\beta=\theta_2-\pi$ at the first corner. Direct expansion of (4) gives


$$
p-T=b\rho^2\alpha^2+b\beta^2+b\rho^2y^2+O(|(\alpha,\beta,y)|^4).
\tag{14}
$$


Thus the Hessian of $p-T$ is


$$
\boxed{\operatorname{diag}(2b\rho^2,\,2b,\,2b\rho^2).}
\tag{15}
$$


At the other corner its first two entries are exchanged.

The product measure’s corner weight is


$$
\frac1{\pi^2M}=\frac{\rho}{\pi^2}.
$$


For the quadratic form in (14), the half-space pushforward coefficient is


$$
\frac{\pi}{b^{3/2}\rho^2}s^{1/2}.
$$


Each corner therefore contributes


$$
\frac1{\pi b^{3/2}\rho}s^{1/2}.
$$


Adding both corners, put


$$
\boxed{K_+=\frac2{\pi b^{3/2}\rho}.}
\tag{16}
$$


Analytic Morse coordinates and compact separation from the other preimages give the total endpoint expansions


$$
f_h(p-s)=K_+A_h\,s^{1/2}+O(s^{3/2}),
\tag{17}
$$


with convergent analytic series after division by $s^{1/2}$.

For completeness, the **full Euler-filter polynomial at either corner** is specified exactly by


$$
E_0(T)=1,\qquad
E_{h+1}(T)=T E_h'(T)+
 \left(n+\frac{mT}{5+T}\right)E_h(T),
\tag{18}
$$


so that


$$
D^h\!\left(T^n(5+T)^m\right)
 =T^n(5+T)^m E_h(T).
$$


Its corner amplitude is


$$
\begin{aligned}
&(8\rho)E_4(p)+(22\rho+2)E_3(p)
 +(18\rho-2)E_2(p)\\
&\hspace{35mm} +(2\rho-10)E_1(p)-2\rho-6.
\end{aligned}
\tag{19}
$$


Thus all degrees are present. The leading order is nonzero because of (12).

## 4. The two signed endpoint Watson laws

Let $c_n=m/n\to c>0$. Define


$$
a_-(c)=1-\frac{cr}{5-r},\qquad
a_+(c)=1+\frac{cp}{5+p}.
\tag{20}
$$



### 4.1 Negative endpoint, $0<c<c_0$

Here


$$
c_0=\frac5r-1,\qquad a_-(c)>0.
$$


The phase decreases into the support from $T=-r$, with inward decay coefficient


$$
\kappa_-(c)=\frac1r-\frac c{5-r}=\frac{a_-(c)}r>0.
$$



Use the established endpoint densities


$$
f_3(-r+s)=AKs^{1/2}+O(s^{3/2}),\qquad A=-2bM,
$$




$$
f_4(-r+s)=O(s^{5/2}),\qquad
f_h(-r+s)=O(s^{1/2})\quad(h\le2).
$$


Uniformly in a fixed endpoint neighborhood,


$$
E_h(T)=n^h\left(1+\frac{c_nT}{5+T}\right)^h+O(n^{h-1}).
\tag{21}
$$


Watson scaling $s\asymp n^{-1}$ now shows:

* degree three has order $n^{3-3/2}=n^{3/2}$;
* degree four has order $n^{4-7/2}=n^{1/2}$;
* every lower degree is also smaller.

Consequently, when this endpoint is globally dominant,


$$
\boxed{
\mathcal Z_{n,m}
=(-1)^n C_-(c_n)n^{3/2}r^n(5-r)^m
 \bigl(1+O(n^{-1})\bigr),
}
\tag{22}
$$


where


$$
\boxed{
C_-(c)=AK\,\Gamma(3/2)\,r^{3/2}a_-(c)^{3/2}<0.
}
\tag{23}
$$


Section 5 below proves global dominance for every $0<c<c_0$.

This corrects the possible ambiguity about the filter factor: before endpoint integration the degree-three term contains $a_-^3$; after Watson integration the net factor is $a_-^{3/2}$. Both are positive on this domain. The sign is therefore $(-1)^{n+1}$.

### 4.2 Positive endpoint

The inward decay coefficient is


$$
\kappa_+(c)=\frac1p+\frac c{5+p}=\frac{a_+(c)}p>0.
$$


Equations (17)–(21) give a degree-four main term of order
$n^{4-3/2}=n^{5/2}$, whereas all lower degrees are smaller. When the positive endpoint is globally dominant,


$$
\boxed{
\mathcal Z_{n,m}
=C_+(c_n)n^{5/2}p^n(5+p)^m
 \bigl(1+O(n^{-1})\bigr),
}
\tag{24}
$$


where


$$
\boxed{
C_+(c)=8\rho K_+\Gamma(3/2)\,
       p^{3/2}a_+(c)^{5/2}>0.
}
\tag{25}
$$



Both statements concern the complete numerator: (2) is negligible. Localization away from the attaining corners is exponentially smaller by the accepted whole upper bound. No endpoint integration by parts is used.

## 5. Exact phase-switch characterization and its location

Write


$$
B_-(c)=x_c(5-x_c)^c,\quad
x_c=\min\left(r,\frac5{1+c}\right),
\qquad B_+(c)=p(5+p)^c.
$$


Let


$$
\Delta(c)=\log B_-(c)-\log B_+(c).
$$


On either side of $c_0$, differentiation at the maximizing negative point gives


$$
\Delta'(c)=\log\frac{5-x_c}{5+p}<0.
\tag{26}
$$


Also $\Delta(0)=\log(r/p)>0$, and $\Delta(c)\to-\infty$. Hence there is exactly one switch order $c_{\mathrm s}$.

It lies strictly between $1$ and $2$. Indeed,


$$
B_-(1)=25/4,\qquad B_+(1)=r<5,
$$


whereas


$$
B_-(2)=500/27,\qquad B_+(2)=2M^3>500/27.
$$


For the last inequality it suffices to use $M>12/5$.

Thus the exact specification is


$$
\boxed{
1<c_{\mathrm s}<2,\qquad
\frac5{1+c_{\mathrm s}}
 \left(\frac{5c_{\mathrm s}}{1+c_{\mathrm s}}\right)^{c_{\mathrm s}}
=p(5+p)^{c_{\mathrm s}}.
}
\tag{27}
$$


In particular:

* $B_-$ strictly dominates for $0<c<c_{\mathrm s}$;
* $B_+$ strictly dominates for $c>c_{\mathrm s}$.

Every negative-dominant interior saddle lies in the analytic interval (7). In fact, for $c_0<c<c_{\mathrm s}<2$,


$$
\frac5{1+c}>\frac53>2\rho^3.
\tag{28}
$$



## 6. All negative-dominant interior orders except finitely many zeros

Define


$$
\mathcal E=
\left\{c\in(c_0,c_{\mathrm s}):
 \mathcal F\!\left(-\frac5{1+c}\right)=0\right\}.
\tag{29}
$$


This set is not merely discrete: it is **finite**.

To see this, (9) excludes zeros for all $c$ sufficiently close to $c_0$. On the remaining closed interval up to $c_{\mathrm s}$, the saddle stays in a compact subset of (7), where the composition in (29) is analytic on a neighborhood. Infinitely many zeros there would have an accumulation point and force analytic identically-zero behavior, contradicting (9).

For fixed


$$
c_0<c<c_{\mathrm s},\qquad c\notin\mathcal E,
$$


the already-audited localization proof now applies with the global analytic densities. It gives


$$
\boxed{
\mathcal Z_{n,m}
=(-1)^n\mathcal F(T_{c_n})
 \sqrt{\frac{2\pi}{n\lambda(c_n)}}\,
 \left(\frac5{1+c_n}\right)^n
 \left(\frac{5c_n}{1+c_n}\right)^m
 (1+O(n^{-1})),
}
\tag{30}
$$


where


$$
T_c=-\frac5{1+c},\qquad
\lambda(c)=\frac{(1+c)^3}{25c}.
$$


This holds for arbitrary integer sequences $m/n\to c$. It proves eventual nonvanishing and sign


$$
(-1)^n\operatorname{sgn}\mathcal F(T_c).
$$



### What finite-order zeros do—and do not—prove

At an exceptional $c$, analyticity ensures that the zero of $\mathcal F$ has finite order. That alone does **not** ensure a surviving Laplace coefficient.

Indeed, choose analytic Morse coordinates $z$ near the saddle such that


$$
\phi_c(T)=\phi_c(T_c)-z^2/2.
$$


The localized transformed integral has analytic amplitude


$$
h(z)=\mathcal F(T(z))T'(z).
$$


Its Laplace coefficients depend on the **even Taylor coefficients** of $h$. If the first nonzero even coefficient is $h_{2\ell}$, the local leading term is


$$
e^{n\phi_c(T_c)}
h_{2\ell}\Gamma(\ell+\tfrac12)
\left(\frac2n\right)^{\ell+1/2}.
\tag{31}
$$


But a nonzero analytic $h$ can be odd, in which case all these coefficients vanish. Moreover, moving saddles arising from integer rounding need separate uniform control at a zero.

Thus (31) supplies a precise bounded follow-on criterion, not an unconditional lower bound on $\mathcal E$.

## 7. Phase equality: polynomial orders and parity

Near $c_{\mathrm s}$, localize separately at the negative saddle and positive endpoint. Uniformly for $c_n$ near $c_{\mathrm s}$, their sum is


$$
\begin{aligned}
\mathcal Z_{n,m}
={}&C_+(c_n)n^{5/2}B_+(c_n)^n(1+O(n^{-1}))\\
&+(-1)^n\sqrt{\frac{2\pi}{n\lambda(c_n)}}B_-(c_n)^n
 \bigl(\mathcal F(T_{c_n})+O(n^{-1})\bigr)\\
&+\text{an exponentially smaller term}.
\end{aligned}
\tag{32}
$$


The factorial-small contribution is included in the last term.

At exact phase equality, the positive term has order $n^{5/2}$, whereas the negative term is at most order $n^{-1/2}$. Therefore positive dominance holds whenever


$$
m-c_{\mathrm s}n=O(1).
\tag{33}
$$


More generally, it holds if, for some fixed $\epsilon>0$,


$$
n\Delta(c_n)\le(3-\epsilon)\log n.
\tag{34}
$$


In particular, (24) and eventual positivity hold under (33), whether or not $\mathcal F(T_{c_{\mathrm s}})=0$.

It would be incorrect to extend that conclusion automatically to every sequence $c_n\to c_{\mathrm s}$. If $\mathcal F(T_{c_{\mathrm s}})\ne0$, the two leading terms become comparable when


$$
n\Delta(c_n)=3\log n+O(1).
\tag{35}
$$


Their signs are respectively positive and
$(-1)^n\operatorname{sgn}\mathcal F(T_{c_{\mathrm s}})$. On the opposite-sign parity, cancellation must be analyzed rather than dismissed. Formula (32) identifies the exact obstruction.

## 8. Generic-domain complete rate and the actual final gcd

Define


$$
\mathcal G=(0,c_0)\ \cup\
 \bigl((c_0,c_{\mathrm s})\setminus\mathcal E\bigr)\
 \cup\ (c_{\mathrm s},\infty).
\tag{36}
$$


For every fixed $c\in\mathcal G$ and every integer sequence
$n\to\infty,\ m\ge0,\ m/n\to c$, the complete numerator is eventually nonzero and


$$
\boxed{
\frac1n\log|\mathcal Z_{n,m}|
\longrightarrow \log\max\{B_-(c),B_+(c)\}.
}
\tag{37}
$$


The same conclusion holds at $c=c_{\mathrm s}$ under bounded rounding (33).

The inherited denominator-transform theorem gives


$$
\log|\mathcal J|
=n\log d+m\log(5+d)+o(n),
\tag{38}
$$


and $\mathcal J<0$ once the starting index exceeds its inherited threshold.

Retain the exact integral pair


$$
L_N=2^{N+1}(2N+2)!(N!)^4,\qquad
U=L_N\mathcal H,\qquad V=L_N\mathcal J,
$$


and the **final** gcd


$$
g=\gcd(|U|,|V|),\qquad
P=-\operatorname{sgn}(V)\frac Ug,\qquad
q=\frac{|V|}{g}>0.
\tag{39}
$$


Then $\gcd(P,q)=1$, and the whole evaluated primitive error is exactly


$$
\boxed{
q(e+\pi)-P=q\,\frac{\mathcal Z_{n,m}}{\mathcal J}.
}
\tag{40}
$$


Consequently, on the stated domains,


$$
\boxed{
\frac1n\log\left|e+\pi-\frac Pq\right|
\longrightarrow
\log\max\{B_-(c),B_+(c)\}
-\log d-c\log(5+d).
}
\tag{41}
$$


This is a matching rate, not merely the previously proved upper bound. Nonvanishing follows from (22), (24), or (30), rather than from an assumption about $e+\pi$.

### New scope of the primorial exclusion

For every fixed $c\in\mathcal G$, choose


$$
N_x=\prod_{\substack{\ell\le x\\\ell\ {\rm odd\ prime}}}\ell,\qquad
n_x=\left\lfloor\frac{N_x}{1+c}\right\rfloor,\qquad
m_x=N_x-n_x.
$$


The accepted arithmetic lower bound applies to exactly the $q$ in (39). Equation (41) contributes only $O(N_x)$ to the logarithm of (40), so


$$
\boxed{
\liminf_{x\to\infty}
\frac{\log|q(e+\pi)-P|}
 {N_x\log\log N_x}\ge2.
}
\tag{42}
$$


The same extension includes $c=c_{\mathrm s}$: this rounding gives
$m_x-c_{\mathrm s}n_x=O(1)$.

Thus the primorial exclusion now covers all positive proportional orders except $c_0$ and the finite set $\mathcal E$. This is still a scoped exclusion, not a statement about arbitrary filtered indices.

For any independently proved fixed-prime lower bound
$\log q\ge WN-o(N)$, the corresponding exact sufficient exclusion condition is


$$
W>
\frac{\log d+c\log(5+d)
-\log\max\{B_-(c),B_+(c)\}}{1+c}.
\tag{43}
$$


No new fixed-prime denominator claim is inferred from the analytic theorem.

## Closing ledger

### (1) New result and proof status

**Proved from the supplied exact representation and accepted estimates:**

* The nonzero critical-value list (6), and absence of intervening negative critical values.
* Real analyticity of all five **total** densities and their total adjoint amplitude on $(-r,-2\rho^3)$.
* Finiteness of the possible amplitude-zero exceptions in the negative-dominant interior range.
* Both positive attaining corners, their multiplicities, Hessians, all five corner weights, and the nonzero full Euler-filter leading amplitude.
* Complete negative- and positive-endpoint Watson laws.
* The unique phase-switch characterization $1<c_{\mathrm s}<2$.
* The generic-domain matching rate (41), with eventual nonvanishing, complete exponential correction, exact factorial compensation, and final gcd retained.
* The enlarged primorial exclusion (42).

The finite-order-zero criterion (31) is proved as a local conditional test; it does not resolve the exceptional zeros.

### (2) Exact remaining bottleneck

The remaining analytic exceptions are sharply localized:

1. The endpoint/interior transition $c=c_0$.
2. Evaluation of the finite set $\mathcal E$, or proof of a surviving even Morse-amplitude coefficient at each of its elements with appropriate rounding control.
3. Possible cancellation in the phase-switch window (35) for unrestricted approaches to $c_{\mathrm s}$.

Independently, an irrationality argument still lacks the necessary control of the **actual primitive denominator** or another route producing nonzero primitive forms tending to zero. The expanded exclusion proves growth on specified subfamilies, not irrationality or rationality of $e+\pi$.

### (3) Computation request

**None.** The new domain theorem and endpoint constants follow from exact calculations and analytic arguments. A finite numerical graph of $\mathcal F$ would not certify the absence of its exceptional zeros or settle the infinite arithmetic bottleneck.
