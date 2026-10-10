> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Atomic certificates and the compact $e+\pi$ determinant

## Research report for A3, Turn 13

### Status and principal result

The rationality or irrationality of $e+\pi$ remains unresolved.

This investigation nevertheless closes one of the outstanding analytic obligations for the **actual compact family**. It does not use a numerical sign grid, replace the factorial moments, remove the negative atom, or change the primitive normalization.

Write


$$
s_0=e+\pi,
\qquad
\Delta_k=\det[\Phi_{k,2k-1}^{T}\mid N],
$$


with the objects defined in the supplied A5 manuscript. Thus


$$
H_k(s_0)=\Lambda_k^k\Delta_k
=(-1)^{k^2}\Lambda_k^kJ_k^\nu\det T^{(k)}.
$$



The new result is:

> **Theorem.** For every integer $k\ge32$,
> 

$$
> \boxed{\det T^{(k)}>0,}
>
$$


> and, more precisely,
> 

$$
> \boxed{
> \det T^{(k)}
> \ge \gamma_k^k\,\mathfrak h_k>0,
> }
> \tag{1}
>
$$


> where
> 

$$
> \gamma_k=
> \frac4k\left(\frac{k^2-1}{144}\right)^k-1-2^k,
> \qquad
> \mathfrak h_k=
> \det\left(\frac1{i+j+1}\right)_{0\le i,j<k}
> =
> \frac{\prod_{j=0}^{k-1}(j!)^4}
> {\prod_{j=0}^{2k-1}j!}.
> \tag{2}
>
$$


> Moreover,
> 

$$
> \boxed{
> (-1)^kH_k(e+\pi)>0,
> \qquad
> (-1)^kH_{1,k}>0.
> }
> \tag{3}
>
$$



The proof gives a uniform, growing-dimension sign certificate. It retains both the overlapping positive supports and the negative atom at $-1$.

The direct support-ratio Chebyshev transfer suggested by the lattice manuscript **fails for the actual densities**: their ratio is not monotone, and it is not completely monotone. The successful replacement is a deterministic polynomial extrapolation estimate. It proves that, on the precise degree space needed by the determinant, a sufficiently distant part of the positive charge dominates every possibly negative contribution.

This is a nonvanishing theorem, not a primitive-error decay theorem. The final all-prime gcd remains unevaluated.

---

## 1. What the Family090 manuscript actually establishes, conditional on its finite arithmetic

The atomic-certificate manuscript has three logically separate components:

1. exact spectral and interpolation identities;
2. finitely many quantitative inequalities;
3. an analytic deduction from those inequalities to exact infinite interpolation and global signs.

These components should not be conflated. In particular, the assertion that a public checker succeeds is not itself an independently inspected arithmetic witness.

No source, build, or verification code was executed here.

### 1.1 Exact finite atom system

The manuscript works with


$$
b=\frac{\sqrt3}{2},\quad B=\frac43,\quad
h=\frac{17}{50},\quad H=\frac{27}{50},\quad
\eta=H-h=\frac15,
$$


and the scalar coordinate $s=b|x|^2$.

Its residue set and positive interpolation nodes are


$$
I=\{0,1,3,4,7,9,12,13,16,19,21,25,27,28,31\},
$$




$$
\mathcal N=(36\mathbb Z+I)\cap(0,\infty).
$$


The finite positive-node list is exactly


$$
f=\{1,3,4,7,9,12,13,16,19,21\},
$$


and the remaining nodes form $T=\mathcal N\setminus f$. The fixed-node list is $L=\{0\}\cup f$.

The sine product is


$$
P(s)=\prod_{a\in I}
\left(2\sin\frac{\pi(s-a)}{36}\right)^2
=\sum_{j=-15}^{15}P_je^{i\pi js/18}.
$$


It has precisely double zeros at $36\mathbb Z+I$. At such a zero,


$$
P(n+u)=Q_nu^2(1+D_nu+O(u^2)),
$$


where $Q_n>0$, and both $Q_n,D_n$ are $36$-periodic.

For $n\in L$, the undamped finite columns are


$$
A_n(s)=\kappa^2P(s)\csc^2\kappa(s-n),\qquad
B_n(s)=\kappa P(s)\cot\kappa(s-n),
\quad \kappa=\frac{\pi}{36}.
$$


They are trigonometric polynomials, not merely functions with a claimed atomic approximation.

At $t_j=j/18$, $0\le j\le15$, their folded spectral masses are


$$
M_{j;c,n}
=-4\kappa^2(2-\mathbf1_{j=0})
\sum_{l=j+1}^{15}(l-j)P_l
e^{i\pi(t_l-t_j)n},
$$




$$
M_{j;d,n}
=i\kappa(2-\mathbf1_{j=0})
\left(P_j+2\sum_{l=j+1}^{15}
P_le^{i\pi(t_l-t_j)n}\right).
$$


The constant column $P$ has folded masses


$$
V_j=(2-\mathbf1_{j=0})P_j.
$$



These formulas follow from Laurent-polynomial division by $(Y-1)^2$ and $Y-1$, with $Y=e^{2i\kappa(s-n)}$. The zero-frequency mass is not doubled. That normalization is essential.

There are twenty unknown finite coordinates on each side: $c_n,d_n$ for $n\in f$. The fixed data are


$$
c_{1,0}=c_{2,0}=\frac{11}{25},\quad
d_{1,0}=d_{2,0}=0,\quad
C_1=-\frac3{500},\quad C_2=\frac3{500}.
$$


After sum-and-difference decomposition, the forty unknown coordinates reduce to the two matrices


$$
I-R,\qquad I+R,
$$


each of order twenty.

Thus the advertised “small atomic system” is an exact finite spectral construction with two $20\times20$ inversions. It is not, by itself, the full interpolation certificate.

### 1.2 The infinite correction is indispensable

For every $n\in T$, the manuscript adds the rational columns


$$
\frac{P(s)}{(s-n)^2},\qquad \frac{P(s)}{s-n},
$$


with damping $e^{-\pi hs}$.

Their folded spectral measures are absolutely continuous. On
$t\in(t_{j-1},t_j)$,


$$
\rho_{c,n}(t)
=-2\pi^2\sum_{l=j}^{15}(t_l-t)P_l
e^{i\pi(t_l-t)n},
$$




$$
\rho_{d,n}(t)
=2i\pi\sum_{l=j}^{15}P_l
e^{i\pi(t_l-t)n}.
$$


The node dependence occurs through phases of modulus one. Hence the total-variation bounds are uniform in the unbounded node index.

The stated interval-variation bounds are


$$
W_{j,c}
=2(\pi/18)^2\sum_{l=j}^{15}
(l-j+\tfrac12)|P_l|,
\qquad
W_{j,d}
=(2\pi/18)\sum_{l=j}^{15}|P_l|.
\tag{4}
$$



This is the substantive analytic reason that **unweighted** $\ell^1$ tail coefficients suffice. Gaussian waves with frequency parameter in the fixed compact interval $[-5/6,5/6]$ have uniformly bounded Schwartz seminorms. Integration against a finite spectral measure, followed by an absolutely summable column series, therefore converges in every Schwartz seminorm.

The relevant Fourier wave is exactly


$$
\widehat{e^{-\pi b(k-it)|x|^2}}
=
\frac1{b(k-it)}
\exp\left(-\frac{\pi|\xi|^2}{b(k-it)}\right).
$$


After division by $e^{-\pi vs}$, its amplitude and exponent are


$$
\lambda_k(t)=\frac{k+it}{b(k^2+t^2)},\qquad
\zeta_{k,v}(t)
=-\frac{Bt}{k^2+t^2}
+i\left(\frac{Bk}{k^2+t^2}-v\right).
$$



The four minimum extra decay exponents, before multiplication by $\pi$, are


$$
\frac{100079}{455650},\quad
\frac{8949}{455650},\quad
\frac{216419}{554650},\quad
\frac{105489}{554650}.
$$


All are positive. Consequently, the divided transformed waves used in the operator estimates really do decay.

### 1.3 Repeated finite columns and complete residual forcing

The periodic finite columns also prescribe jets at later nodes in the same residue class. They cannot be treated as columns supported only at their first node.

At $m=n+36l$, $l\ge1$, their contribution in tail coefficient coordinates is


$$
e^{-\pi\eta m}(c_n,d_n-\pi\eta c_n).
$$


It is an own-side contribution and must be subtracted from the tail target. This includes the fixed column at zero.

Its operator norm is bounded by


$$
\frac{1+\pi\eta}{e^{36\pi\eta}-1}.
\tag{5}
$$



The finite approximation retains Gaussian targets only at $1,3,4,7$, using


$$
e=(z,1,zw,w,zu,u,zp,p)^T,
$$


where


$$
w=e^{-2/z},\quad u=e^{-3/z},\quad p=e^{-6/z}.
$$


The omitted targets at $9,12,13,16,19,21$, and all tail targets, remain part of the residual forcing.

The containing polytope uses


$$
Z=.391,\quad W_*=.0061,\quad \Delta_*=.00018,\quad
U_*=.00048,\quad P_*=.0000003,
$$


with $zw=Zw-\Delta$, $0\le a\le Zu$, and the other bounds stated in the source. The enclosure of the actual parameter curve is analytically justified, including the maximum of


$$
(Z-z)e^{-2/z}.
$$



### 1.4 Finite premises needed by the infinite argument

The sufficient finite premises used by the proof are:



$$
\|(I-R)^{-1}\|_1<17,\qquad
\|(I+R)^{-1}\|_1<5,
$$




$$
\sup_{\mathcal E}\|A_ie\|_1<3,
$$




$$
\|\mathcal B\|<340,\quad
\|\mathcal D\|<3\cdot10^{-8},\quad
\|\mathcal C\|+\|\mathcal A\|<3\cdot10^{-10},
$$




$$
\|\mathcal K_{T,V}\|<1.3\cdot10^{-7},
$$


and omitted-target bounds


$$
d<8.2\cdot10^{-8},\qquad d_T<10^{-26}.
$$



The source supplies stricter underlying bounds, including


$$
\|W\|<119,\quad
\|\mathcal A\|<2.5\cdot10^{-10},\quad
\|\mathcal C\|<7\cdot10^{-15}.
$$



Writing


$$
\beta=3\cdot10^{-10},\qquad \delta=3\cdot10^{-8},
$$


the two tail Schur complements are invertible because


$$
\delta+340\beta N_\varepsilon<1,
\qquad N_+=17,\quad N_-=5.
$$


Numerically, the larger of these bounds is only $1.764\cdot10^{-6}$.

The full equations are


$$
(I-\varepsilon R)u_\varepsilon
-\varepsilon\mathcal Bw_\varepsilon=r_\varepsilon,
$$




$$
(I-\varepsilon\mathcal D)w_\varepsilon
-(\varepsilon\mathcal C-\mathcal A)u_\varepsilon=s_\varepsilon.
$$


The sign of $\mathcal A$ is the same in both decompositions. This is correct: it is an own-side repetition map.

The resulting rational error estimates give, on each individual side,


$$
\|w_i\|_1<3\cdot10^{-9},\qquad
\|u_i-(A_ie)_f\|_1<10^{-5}.
\tag{6}
$$


This step is genuinely infinite-dimensional. A finite truncation of the tail would not establish it.

---

## 2. How the manuscript obtains global, rather than sampled, signs

### 2.1 Between-node control

For a $C^2$ function,


$$
U_m[\varphi](v)
=
\frac{\varphi(m+v)-\varphi(m)-v\varphi'(m)}{v^2}
=
\int_0^1(1-t)\varphi''(m+tv)\,dt.
\tag{7}
$$


The exact interpolation equations therefore reduce signs to comparisons of deleted-jet remainders.

The finite Taylor polynomials have degree twenty. Their signs are checked through Bernstein coefficients on entire half-cells and on the entire parameter polytope—not at sample points.

The source’s ordinary lower bounds are:

| Half-cell | Polynomial | Lower bound |
|---|---|---:|
| $m=1,y=-1$ | $T_2$ | .174 |
| $m=1,y=-1$ | $Q_1/(2Z)-T_1$ | .057 |
| $m=1,y=1$ | $T_2$ | .011 |
| $m=3$, either side | $.8Q_1w-T_1$ | .00055 |
| $m=3$, either side | $T_2$ | .00097 |
| $m=4$, either side | $-T_1$ | .00047 |
| $m=4$, either side | $T_2$ | .00097 |
| $m=7$, either side | $-T_1,T_2$ | .0028 |
| $m=9$, either side | $-T_1,T_2$ | .0039 |
| $m=12,13$, either side | $-T_1,T_2$ | .0020 |

The infinite correction and Taylor remainders together contribute less than


$$
.018,\quad .003,\quad .00016
$$


on, respectively, the first left half-cell, first right half-cell, and every later tested half-cell.

These bounds follow from (6), the curvature envelopes


$$
\begin{array}{c|rrrrr}
s_0&0&1&2&14.5&23\\ \hline
\mathcal L(s_0)&1510&46&14&.00465&.000023\\
\mathcal T(s_0)&26500&1160&800&800&800,
\end{array}
$$


and Taylor errors below $.002$ at $m=1$ and $10^{-5}$ elsewhere.

The right half-cell at $m=1$ requires a separate argument. The exact Gaussian remainder has the lower bound


$$
U_m[G](v)\ge Q_1e^{(1-m)/z}
\frac{3z+v}{6z^2+4zv+v^2},
\qquad v\ge0.
$$


After multiplication by the positive denominator, the comparison is cubic in $z/Z$. Its four Bernstein coefficients are the four exceptional tests in the source, with lower bounds


$$
.046,\quad .056,\quad .024,\quad .027.
$$


The curvature error decreases the relevant coefficients by at most


$$
.003\cdot3.5=.0105.
$$


The exceptional comparison therefore has a genuine positive margin.

This is a valid whole-cell mechanism, conditional on the finite coefficient inequalities.

### 2.2 Unbounded-range control

The manuscript does not extrapolate its finite sign tests to infinity. It uses a different barrier there.

For a nearest zero $m$, the quotient


$$
\frac{P(s)}{(s-m)^2}
$$


is positive and log-concave on each half-gap. Indeed, after removing the double zero, its logarithmic second derivative is a sum of nonpositive terms; the divided factor contributes


$$
2\left((s-m)^{-2}
-\kappa^2\csc^2(\kappa(s-m))\right)\le0.
$$


Consequently, endpoint and midpoint bounds control the entire half-gap.

The finite node premises are


$$
Q_m>.157,\qquad |D_m|<2.83,
$$


and the fifteen midpoint quotient bounds are


$$
.165,.120,.054,.482,.656,1.11,.337,
3.13,9.26,8.19,19.08,2.34,.706,6.80,14.1.
$$


They imply


$$
P(s)>.054(s-m)^2
$$


throughout every period. On $[14.5,23]$, the stronger relevant bounds imply


$$
P(s)>3(s-m)^2.
$$



Writing $J_i=C_iP+J_i^0$, the remaining curvature is bounded by


$$
K=
3.01q+800(3\cdot10^{-9})+.006(.002),
$$


where $q=.00465$ on $[14.5,23]$ and $q=.000023$ above $23$. Thus


$$
K=.0140109<.006\cdot3,
$$


and


$$
K=.00008363<.006\cdot.054.
$$


Exact jets, the integral identity (7), and convexity of the Gaussian complete the signs on the whole half-line.

The constants $\pm.006P$, the small tail norm, and the periodic lower barrier are all essential. None has an automatic counterpart in the compact $e+\pi$ determinant.

### 2.3 Audit conclusion for Family090

The analytic passage


$$
\text{finite inequalities}
\Longrightarrow
\text{exact infinite interpolation}
\Longrightarrow
\text{global signs}
$$


is coherent at the stated hypotheses. The source gives sound algebraic recipes for outward interval evaluation, including the $659$ Bernstein-row minima.

However, this report has not independently evaluated those $659$ inequalities, the two interval inverses, or the other finite enclosures. Their successful numerical evaluation remains a **finite computational premise** in this audit.

The downstream energy deduction—reciprocal Gaussian parameters, density-only Fourier comparison, positive Laplace mixtures, and Fatou/Tonelli passage—is separate and valid under the Gaussian-minorant input. It supplies no theorem about $e+\pi$.

The bibliography likewise does not enlarge any result’s scope: classical Fourier interpolation, Bernstein representation, and lattice-restricted optimality results do not authorize the missing finite arithmetic or a transfer to a different signed moment problem.

---

## 3. The actual compact measures and the first failed transfer hypothesis

We now return to the exact A5 objects.

### 3.1 Recovering the charge density

The recurrence


$$
a_0=1,\qquad a_d=1-da_{d-1}
$$


has the integral realization


$$
a_d=\int_0^\infty(1-t)^d e^{-t}\,dt.
\tag{8}
$$


Integration by parts proves the recurrence directly.

Hence the positive measure $\mu$ may be realized as the pushforward of $e^{-t}dt$ under $x=(1-t)^2$. Its mass is one, and


$$
\int x^n\,d\mu(x)=a_{2n}.
$$


Its density is


$$
\frac{d\mu}{dx}=
\begin{cases}
\displaystyle
\frac{e^{-1}\cosh\sqrt x}{\sqrt x},
&0<x<1,\\[6pt]
\displaystyle
\frac{e^{-1}e^{-\sqrt x}}{2\sqrt x},
&x>1.
\end{cases}
\tag{9}
$$



The compact measure is


$$
\frac{d\nu}{dx}
=
\frac{e^{\sqrt x}+4/(1+x)}{2\sqrt x},
\qquad 0<x<1.
\tag{10}
$$


The contact functional remains


$$
L(f)=\int f\,d\mu-f(-1).
\tag{11}
$$



All arguments below concern polynomial integrals, so (8) also verifies their compatibility with the original moment recurrence.

### 3.2 The density ratio is not monotone

On the overlap, put $t=\sqrt x$. Then


$$
R(t)=\frac{d\mu}{d\nu}(t^2)
=e^{-1}\frac{e^t+e^{-t}}{e^t+4/(1+t^2)}.
\tag{12}
$$


At zero,


$$
R'(0)=-\frac{2}{25e}<0.
$$


At $t=1$, the numerator of its derivative, apart from the positive factor $e^{-1}$, is


$$
(e-e^{-1})(e+2)-(e+e^{-1})(e-2)
=4e-2>0.
$$


Thus the ratio decreases initially and increases near the other endpoint.

It follows that:

* the pair $\{1,d\mu/d\nu\}$ is not a two-function Chebyshev system on the overlap;
* $d\mu/d\nu$, viewed as a function of $x$, is not completely monotone;
* its reciprocal is not monotone either.

For the Chebyshev assertion, the initial decrease and subsequent increase produce a horizontal level met at two distinct interior points. The corresponding nontrivial linear combination of $1$ and the ratio has two zeros.

This is the first precise failure of the proposed support-ratio transfer. The Gaussian complete-monotonicity used by Family090 cannot simply be assigned to these densities.

There is nevertheless useful structure:


$$
d\mu-e^{-1}d\nu
=
\frac{e^{-1}}{2\sqrt x}
\left(e^{-\sqrt x}-\frac4{1+x}\right)dx<0
\quad(0<x<1).
$$


But that observation alone does not establish a growing-dimension determinant sign. We use a quantitative alternative.

---

## 4. A uniform polynomial domination lemma

The following lemma is the new deterministic ingredient.

### Lemma 1: exterior norm controls all compact evaluations

Let $k\ge2$, and let $p$ be a real polynomial of degree at most $k-1$. Set


$$
M(p)=\max_{-1\le x\le1}|p(x)|.
$$


Then


$$
\boxed{
\int_{k^2}^{4k^2}p(x)^2\,dx
\ge
\frac{3}{16^{k-1}}M(p)^2.
}
\tag{13}
$$



#### Proof

Let $\mathcal P_j$ denote the ordinary Legendre polynomial, normalized by $\mathcal P_j(1)=1$. An orthonormal basis on $[k^2,4k^2]$ is


$$
\varphi_j(x)=
\sqrt{\frac{2j+1}{3k^2}}\,
\mathcal P_j\left(\frac{2x-5k^2}{3k^2}\right).
$$


For $x\in[-1,1]$ and $k\ge2$,


$$
\left|\frac{2x-5k^2}{3k^2}\right|
\le\frac{11}{6}.
$$



For $u\ge1$, the classical integral representation


$$
\mathcal P_j(u)
=\frac1\pi\int_0^\pi
\left(u+\sqrt{u^2-1}\cos\theta\right)^j\,d\theta
$$


gives


$$
|\mathcal P_j(u)|
\le \left(u+\sqrt{u^2-1}\right)^j.
$$


The representation itself follows by summing its generating series and obtaining
$(1-2uz+z^2)^{-1/2}$. Parity handles negative $u$.

Since


$$
\frac{11+\sqrt{85}}6<4,
$$


we obtain $|\mathcal P_j(u)|\le4^j$ throughout the required range.

Expand $p=\sum_{j=0}^{k-1}\alpha_j\varphi_j$. Cauchy–Schwarz gives


$$
|p(x)|^2
\le
\left(\int_{k^2}^{4k^2}p^2\right)
\frac1{3k^2}\sum_{j=0}^{k-1}(2j+1)16^j.
$$


Using


$$
\sum_{j=0}^{k-1}(2j+1)=k^2
$$


bounds the last factor by $16^{k-1}/3$. Taking the maximum over $[-1,1]$ proves (13). ∎

### Lemma 2: domination for every compact root tuple

For $y=(y_1,\ldots,y_k)\in[0,1]^k$, define


$$
Q_y(x)=\prod_{j=1}^k(x-y_j).
$$


Put


$$
A_k=\frac4k\left(\frac{k^2-1}{144}\right)^k,
\qquad
\gamma_k=A_k-1-2^k.
\tag{14}
$$


Then, for every polynomial $p$ of degree at most $k-1$,


$$
\boxed{
L(p^2Q_y)\ge\gamma_k M(p)^2.
}
\tag{15}
$$



For $k\ge32$, $\gamma_k>0$.

#### Proof

On $x>1$, $Q_y(x)\ge0$. On the particular interval $[k^2,4k^2]$,


$$
Q_y(x)\ge(k^2-1)^k.
$$


By (9),


$$
\frac{d\mu}{dx}
\ge \frac{e^{-1-2k}}{4k}
\quad(k^2\le x\le4k^2).
$$


Therefore (13) yields


$$
\int_{k^2}^{4k^2}p^2Q_y\,d\mu
\ge
\frac{12}{ek}
\left(\frac{k^2-1}{16e^2}\right)^kM(p)^2.
$$


Since $e<3$, this is at least $A_kM(p)^2$.

On the overlap,


$$
|Q_y(x)|\le1\qquad(0\le x\le1),
$$


and $\mu([0,1])\le1$, so its possibly negative contribution is bounded below by $-M(p)^2$.

The atom is retained:


$$
-p(-1)^2Q_y(-1)
\ge-2^kM(p)^2,
$$


because


$$
|Q_y(-1)|=\prod_j(1+y_j)\le2^k.
$$


The remaining exterior integral is nonnegative. Combining these estimates gives (15).

For $k\ge32$,


$$
\frac{k^2-1}{288}>3.
$$


Thus


$$
A_k
=\frac4k\,2^k
\left(\frac{k^2-1}{288}\right)^k
>
\frac4k\,2^k3^k
\ge4\cdot2^k.
$$


Consequently,


$$
\gamma_k>3\cdot2^k-1>0.
$$


∎

This is not a claim that $Q_yL$ is a positive measure. It need not be. It is positivity of its quadratic form on the **exact finite-degree space** required below, uniformly in $y$ and uniformly for all $k\ge32$.

---

## 5. Exact signed-integral transfer to the residual determinant

### 5.1 Conditional integration of the whole determinant

The exact two-measure determinant identity is


$$
\Delta_k
=
\frac1{k!^2}
\int
V(x)^2V(y)^2
\prod_{i,j}(y_j-x_i)\,
dL^k(x)\,d\nu^k(y).
\tag{16}
$$


It follows by expanding determinants and integrating termwise. All measures have the required finite polynomial moments; $L$ is a finite signed measure.

For fixed $y$, let


$$
M_y=
\bigl(L(x^{a+b}Q_y(x))\bigr)_{0\le a,b<k}.
\tag{17}
$$


Since


$$
\prod_{i,j}(y_j-x_i)
=(-1)^{k^2}\prod_iQ_y(x_i),
$$


a second application of the determinant integration identity gives


$$
\boxed{
(-1)^{k^2}\Delta_k
=
\frac1{k!}\int_{[0,1]^k}
V(y)^2\det M_y\,d\nu^k(y).
}
\tag{18}
$$



This retains the full signed functional inside $M_y$.

### 5.2 Positive definiteness with an explicit matrix lower bound

For $p(x)=\sum_{a=0}^{k-1}v_ax^a$, Lemma 2 gives


$$
v^TM_yv=L(p^2Q_y)
\ge\gamma_k M(p)^2
\ge\gamma_k\int_0^1p(x)^2\,dx.
$$


Therefore, in positive-semidefinite order,


$$
M_y\succeq
\gamma_k
\left(\frac1{a+b+1}\right)_{a,b<k}.
\tag{19}
$$


For $k\ge32$, both matrices are positive definite. Determinant monotonicity yields


$$
\det M_y\ge\gamma_k^k\mathfrak h_k>0.
\tag{20}
$$



Substituting into (18), and using


$$
\frac1{k!}\int V(y)^2\,d\nu^k(y)=J_k^\nu,
$$


gives


$$
\boxed{
(-1)^k\Delta_k
\ge\gamma_k^k\mathfrak h_kJ_k^\nu>0.
}
\tag{21}
$$



Finally, reuse A5’s exact compression,


$$
\Delta_k=(-1)^{k^2}J_k^\nu\det T^{(k)}.
$$


Because $J_k^\nu>0$, division proves (1).

### 5.3 Relation to the supplied $\mathcal I_k-\mathcal J_k$

Expanding $L=\mu-\delta_{-1}$ in (16) gives exactly


$$
\Delta_k=\mathcal I_k-\mathcal J_k.
$$


Terms containing two negative atoms vanish through $V(x)^2$. A single atom contributes the complete factors


$$
\prod_i(x_i+1)^2\prod_j(y_j+1)
$$


and the coefficient $1/((k-1)!k!)$.

Thus the new result also states


$$
\boxed{
(-1)^k(\mathcal I_k-\mathcal J_k)>0
\qquad(k\ge32).
}
\tag{22}
$$



It does **not** assert that $\mathcal I_k$ and $\mathcal J_k$ are separately positive. Their overlapping-support sign changes remain present. The proof controls their whole difference by a finite-degree quadratic-form identity.

### 5.4 Exact moment boundaries

The entries of (17) involve degree at most


$$
(k-1)+(k-1)+k=3k-2.
$$


That is exactly the largest moment index in the original block matrix:


$$
m+j\le(2k-1)+(k-1)=3k-2.
$$



No extra contact equations, extended row range, or fictitious endpoint moments have been introduced.

---

## 6. The affine coefficient is also nonzero

The same mechanism proves the second assertion in (3).

For every real $s$, the exact mixed-moment identity permits the real column operation


$$
H_k(s)
=
\Lambda_k^k
\det\left[
\Phi^T\ \middle|\ N+(s-s_0)wv^T
\right].
\tag{23}
$$


The right block is the moment block for


$$
\nu+(s-s_0)\delta_{-1}.
$$


This is an identity for the already defined affine polynomial; it does not alter its arithmetic coefficients.

Differentiate the double-integral formula at $s=s_0$. Exactly one compact variable is placed at $-1$. If an $L$-variable is also at $-1$, the cross Vandermonde vanishes. Thus the derivative’s charge variables use $\mu$, not a modified or discarded version of $L$.

For $y=(y_1,\ldots,y_{k-1})$, define


$$
\widetilde Q_y(x)=(x+1)\prod_{j=1}^{k-1}(x-y_j),
$$


and


$$
\widetilde M_y
=
\left(\int x^{a+b}\widetilde Q_y(x)\,d\mu(x)\right)_{a,b<k}.
$$


Tracking all signs gives


$$
\boxed{
\frac{(-1)^kH_{1,k}}{\Lambda_k^k}
=
\frac1{(k-1)!}
\int
V(y)^2\prod_{j=1}^{k-1}(1+y_j)^2
\det\widetilde M_y\,d\nu^{k-1}(y).
}
\tag{24}
$$



On $[k^2,4k^2]$,


$$
\widetilde Q_y(x)
\ge(k^2+1)(k^2-1)^{k-1}
\ge(k^2-1)^k.
$$


On $[0,1]$,


$$
|\widetilde Q_y(x)|\le2.
$$


There is no atom in this conditional charge integral. The proof of Lemma 2 therefore gives


$$
\widetilde M_y
\succeq
(A_k-2)
\left(\frac1{a+b+1}\right)_{a,b<k}.
$$


Since $A_k-2>0$ for $k\ge32$, (24) proves


$$
(-1)^kH_{1,k}>0.
$$



A quantitative form is


$$
\frac{(-1)^kH_{1,k}}{\Lambda_k^k}
\ge
(A_k-2)^k\mathfrak h_k
J_{k-1}^{(1+x)^2\nu}>0,
\tag{25}
$$


where the last factor is the positive Hankel determinant of the measure
$(1+x)^2d\nu(x)$.

This is another all-size statement, not a finite coefficient sign observation.

---

## 7. What this does—and does not—do to the arithmetic ledger

### 7.1 The compact construction is unchanged

The original compact ranges remain


$$
k\ge2,\qquad 0\le m<2k,\qquad 0\le j<k.
$$


The complete recurrences remain


$$
a_0=1,\quad a_d=1-da_{d-1},\quad
c_n=a_{2n}-(-1)^n,
$$




$$
\rho_0=0,\quad
\rho_{n+1}+\rho_n=\frac1{2n+1},
\qquad
r_n=-(2n)!+4\rho_n.
$$


The factorial term and the rational arctangent correction are both retained.

The original integer polynomial remains


$$
H_k(s)=
\det\left[
\Phi^T\ \middle|\
\Lambda_k\mathcal R+s\Lambda_kwv^T
\right],
$$


where


$$
\Lambda_k=\operatorname{lcm}(1,3,\ldots,6k-5).
$$



The new proof is an analytic estimate of this exact object. It introduces no rational replacement of its moments and no new arithmetic row normalization.

### 7.2 Paid divisions, contents, and clearers are not reidentified

The established saturation payment remains


$$
\prod_{m=k}^{2k-1}e_{k,m}
=
\frac{|\det C_k|}{\delta_{k,2k-1}}.
$$


For a saturated integer kernel basis $X$, the actual entry clearer remains


$$
L_X=
\frac{\Lambda_k}
{\gcd\!\left(\Lambda_k,\{\Lambda_kB_{rj}\}_{r,j}\right)},
\qquad
B_{rj}=\sum_mX_{rm}r_{m+j}.
$$


If


$$
L_X^k\det\mathcal M_X(s)=A_0+A_1s,
$$


the least simultaneous coefficient clearer is


$$
\frac{L_X^k}{\gcd(L_X^k,A_0,A_1)},
$$


and the remaining content after that clearing is


$$
\frac{\gcd(A_0,A_1)}
{\gcd(L_X^k,A_0,A_1)}.
$$



None of these quantities is evaluated or changed by the present real-variable proof. In particular, the rational constant $\gamma_k$ is a bound, not a denominator payment imposed on the original integer linear form.

### 7.3 The actual primitive pair and whole error

Let


$$
G_k=\gcd(|H_{0,k}|,|H_{1,k}|)
$$


be the final gcd over **all primes**.

For $k\ge32$, $H_{1,k}\ne0$, so define the actual primitive pair by


$$
q_k=\frac{|H_{1,k}|}{G_k},
\qquad
p_k=-\frac{\operatorname{sgn}(H_{1,k})H_{0,k}}{G_k}.
$$


Then


$$
\gcd(p_k,q_k)=1,
$$


and the new sign theorem gives


$$
\boxed{
q_k(e+\pi)-p_k
=
\frac{|H_k(e+\pi)|}{G_k}>0.
}
\tag{26}
$$


Thus these actual primitive rational approximants lie below $e+\pi$.

The established A5 upper bound remains


$$
0<q_k(e+\pi)-p_k
\le
\frac{F_k^\perp}{G_k},
$$


where


$$
F_k^\perp
=
\Lambda_k^k21^kk!h_k
\prod_{r=0}^{k-1}(2k+4r)!.
\tag{27}
$$



The parent divisor


$$
D_{k-1}=\prod_{r=0}^{k-2}(r!)^2
\mid G_k
$$


is still only a lower divisor, not the final gcd. Using it alone leaves the previously established upper-bound scale


$$
\log(F_k^\perp/D_{k-1})
=
3k^2\log k+O(k^2).
$$


No decay follows.

The new lower bound also makes clear that the raw determinant is not being shown small:


$$
|H_k(e+\pi)|
\ge
\Lambda_k^kJ_k^\nu\gamma_k^k\mathfrak h_k.
$$


This says nothing conclusive about primitive decay without the actual $G_k$.

---

## 8. Original binary indices and reconstruction boundaries

The separate original binary construction remains on


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0.
$$


Its contact range is $0,\ldots,b-1$, while physical reconstruction runs through $0,\ldots,b$, with


$$
z_b=0.
$$



Its complete corrected columns remain


$$
x=\frac12RA^{-1}f,
\qquad
y=\frac{RA^{-1}(h^e+h^F)+e_0}{4b!},
\qquad
x=2^ax_0.
$$


Neither $h^F$ nor $e_0$ is removed.

The full-return quantity is still


$$
S=\sum_{j<b}(n+1-j)\binom{n+2}{j}z_j^f.
$$


After the paid division, the accepted conclusion remains


$$
v_2\!\left(\frac{S}{2^{a+1}}\right)\ge\chi-a,
\qquad
\chi=v_2\binom{n+b-1}{b-1}.
$$


The subtraction of $a$ is not recoverable merely by renaming the primitive column.

No compact estimate evaluates the original $Q=x_0^Tx_0$, corrected-column contents, least simultaneous clearer, or final all-prime gcd. Nor is the binary valuation


$$
v_3(q)=n-\frac{b+15}{2}
$$


transferred to the compact family.

The new compact theorem does hold on the explicit infinite set


$$
k=9^{18+32u},\qquad u\ge0,
$$


because every such $k$ exceeds $32$. On those same compact indices it proves both $H_{1,k}\ne0$ and whole-error nonvanishing. This is not an identity between the compact and binary primitive pairs.

---

## 9. Proof status, remaining lemma, and bounded arithmetic

### 9.1 Newly proved statements

The derivations above prove, without finite numerical sign tests:

1. the actual overlap ratio fails the proposed monotone-ratio and completely-monotone hypotheses;
2. the uniform polynomial domination inequality (15);
3. $\det T^{(k)}>0$ for every $k\ge32$;
4. $(-1)^kH_k(e+\pi)>0$ and $(-1)^kH_{1,k}>0$ on that same infinite domain;
5. positivity of the actual primitive whole error in (26).

The determinant nonvanishing obligation is therefore no longer open for this compact family at $k\ge32$.

### 9.2 Exact remaining bottleneck

A sufficient next lemma is now:

> **Primitive-decay lemma.** On an explicitly specified infinite set of integers $k\ge32$, prove
> 

$$
> \frac{F_k^\perp}{G_k}\longrightarrow0,
>
$$


> or prove the weaker, directly relevant assertion
> 

$$
> \frac{\Lambda_k^kJ_k^\nu\det T^{(k)}}{G_k}
> \longrightarrow0.
> \tag{28}
>
$$



Nonvanishing of the numerator and of $H_{1,k}$ is already established there.

If $e+\pi=A/B$ were rational, every nonzero primitive error would satisfy


$$
|q_k(e+\pi)-p_k|\ge\frac1B.
$$


Thus (28) would prove irrationality. At present, neither version of (28) has been established.

The remaining obstruction is therefore genuinely arithmetic-and-asymptotic: sufficient control of the **final all-prime gcd relative to the whole evaluated determinant**, not an unevaluated determinant sign.

### 9.3 Bounded exact-arithmetic receipt

No new Smith calculation, parent $k=3$ computation, or finite sign grid is needed for the proof.

A small optional receipt can audit the threshold constant at $k=32$.

**Inputs**


$$
k=32,\qquad
A_{32}=\frac18\left(\frac{341}{48}\right)^{32},
$$




$$
N=341^{32}-8(1+2^{32})48^{32}.
$$



**Expected verifiable outputs**


$$
N>0,
\qquad
\gamma_{32}=\frac{N}{8\cdot48^{32}}>0,
$$


and


$$
\gcd(N,8\cdot48^{32})=1.
$$


The gcd assertion follows already from parity and reduction modulo $3$; the denominator has no other prime factors. The all-$k$ extension is supplied by the analytic inequalities in Lemma 2, not by checking further values.

This receipt concerns only the explicit bound constant. It is not a computation of $G_{32}$.

Separately, adoption of Family090’s claimed global theorem would require independent inspection of its finite interval outputs: two order-twenty inverses, the stated envelope bounds, and the $659$ Bernstein-row minima. Those are bounded finite premises with explicit mathematical inputs and thresholds. They are not needed for the new compact theorem proved here.

---

## Conclusion

The atomic manuscript’s transferable lesson is not “a finite sign grid proves a global theorem.” Its real mechanism is:

* exact interpolation identities;
* a complete infinite correction with uniform operator bounds;
* deleted-jet control on bounded cells;
* an explicit barrier dominating the remainder on the unbounded range.

The proposed density-ratio version of that mechanism fails for the actual compact measures. Their ratio is nonmonotone.

A different exact barrier does succeed. Polynomial extrapolation from $[k^2,4k^2]$ shows that the positive exterior charge dominates both the overlapping-support contribution and the negative atom on the precise degree space of the conditional moment determinant. This proves


$$
\boxed{
\det T^{(k)}>0,\quad
H_{1,k}\ne0,\quad
H_k(e+\pi)\ne0
\qquad(k\ge32).
}
$$



The global objective remains open. What is now missing is not whole-error nonvanishing for this compact family, but primitive decay after the **actual final all-prime gcd** on the same infinite indices.
