> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

## A3: factorial-compensated signed raw filter, with a uniform whole-error bound

I withdraw the criticism of A1’s $D_j$ bound. Its $D_j$ are derangement numbers, not the nonalternating partial-factorial sums used elsewhere. In particular, $D_2=1$, and the stated bound $D_{2r}\le (2r)!$ is valid. No repair of A1’s bound is needed.

The new filter below genuinely changes the raw scale: its weights on the original raw forms alternate in sign and compensate their factorial decay. I obtain a surviving endpoint and a uniform upper bound for the **complete evaluated error**, valid for arbitrary growing filter order. The denominator estimate remains far too large for irrationality, and complete-error nonvanishing after filtering is not proved.

### 1. Exact compensated outputs and final primitive normalization

Use the integer-$L$ raw $b=2$ normalization from the contiguous endpoint source. To avoid confusing the target constant with a determinant, write


$$
\mathcal S=e+\pi.
$$


For every integer $k\ge2$, the exact raw outputs are


$$
Y_k=s_k\mathscr D_k,\qquad
X_k=s_k\mathscr X_k,\qquad
R_k=X_k+\mathcal S Y_k,
$$


where


$$
s_k=\frac{(-1)^k}{4(k!)^4(k+1)^3},
\qquad
\mathscr X_k=Q_k+2f_kV_k.
$$


In particular, $\mathscr X_k$ contains the complete partial-exponential and second-kind contractions.

Define the additional factorial compensation


$$
J_k=\frac{Y_k}{s_k(k!)^2}
     =\frac{\mathscr D_k}{(k!)^2},
\qquad
H_k=\frac{X_k}{s_k(k!)^2}
     =\frac{\mathscr X_k}{(k!)^2},
$$


and the complete compensated remainder


$$
Z_k=H_k+\mathcal S J_k
   =\frac{R_k}{s_k(k!)^2}.
\tag{1}
$$



Fix a positive rational number $\theta=a/b$, with positive coprime integers $a,b$. For integers $n\ge2$, $m\ge0$, set


$$
w_j=\binom mj a^j b^{m-j}\qquad(0\le j\le m),
$$




$$
\mathcal H_{n,m}=\sum_{j=0}^m w_jH_{n+j},
\qquad
\mathcal J_{n,m}=\sum_{j=0}^m w_jJ_{n+j}.
$$


On $\mathcal J_{n,m}\ne0$, the new center is


$$
\boxed{c_{n,m}=-\frac{\mathcal H_{n,m}}{\mathcal J_{n,m}}.}
\tag{2}
$$



Although $w_j>0$, its weights on the **original raw forms** are


$$
\frac{w_j}{s_{n+j}((n+j)!)^2}
=
4(-1)^{n+j}w_j((n+j)!)^2(n+j+1)^3.
\tag{3}
$$


They are signed and factorially compensating. Thus this is not the previously excluded positive raw-weight construction.

Here is the final gcd, defined before any estimate. Put $N=n+m$ and


$$
L_N=2^{N+1}(2N+2)!(N!)^4.
$$


The contiguous source’s clearer shows that


$$
U=L_N\mathcal H_{n,m}\in\mathbb Z,\qquad
T=L_N\mathcal J_{n,m}\in\mathbb Z.
$$


Indeed, its clearer for $\mathscr X_k$, multiplied by $(k!)^2$, divides $L_N$ for every $k\le N$.

For $T\ne0$, let


$$
g=\gcd(|U|,|T|),
\qquad
P=-\operatorname{sgn}(T)\frac Ug,\qquad
q=\frac{|T|}{g}>0.
\tag{4}
$$


Then $c_{n,m}=P/q$ in lowest terms. In particular, $q$ is the **actual primitive denominator**, and


$$
\boxed{
q\mathcal S-P
=
q\,\frac{\sum_{j=0}^m w_jZ_{n+j}}
        {\sum_{j=0}^m w_jJ_{n+j}}.
}
\tag{5}
$$


No cross-index scalar or endpoint gcd has been discarded.

---

### 2. The compensated endpoint and remainder have different geometric scales

Let


$$
d=14+10\sqrt2,\qquad r=2+2\sqrt2.
\tag{6}
$$


I claim that the inherited $b=2$ asymptotics imply


$$
\frac{J_{k+1}}{J_k}\longrightarrow d,
\qquad
\frac{Z_{k+1}}{Z_k}\longrightarrow-r.
\tag{7}
$$



Here is the scale calculation. The raw endpoint asymptotic has the form


$$
Y_k\sim
C\frac{L_{k+1}(0)K_k(0,1)}{k(k!)^2},
\qquad C>0.
$$


The supplied Legendre and kernel formulas give


$$
\frac{L_{k+2}(0)}{L_{k+1}(0)}
\longrightarrow -(2+2\sqrt2),
$$




$$
\frac{K_{k+1}(0,1)}{K_k(0,1)}
\longrightarrow 3+2\sqrt2.
$$


Consequently


$$
k^2\frac{Y_{k+1}}{Y_k}\longrightarrow-d.
$$


On the other hand,


$$
\frac{s_{k+1}}{s_k}
=-\frac1{(k+1)(k+2)^3},
$$


so


$$
\frac{s_k(k!)^2}{s_{k+1}((k+1)!)^2}
=-\frac{(k+2)^3}{k+1}.
$$


This proves the first limit in (7).

The whole-error theorem gives


$$
\frac{R_k}{Y_k}\sim(-1)^k(\sqrt2-1)^2\epsilon_k,
\qquad
\frac{\epsilon_{k+1}}{\epsilon_k}\longrightarrow3-2\sqrt2.
$$


Since $Z_k/J_k=R_k/Y_k$, the second limit follows from


$$
d(3-2\sqrt2)=r.
$$



The eventual signs are also important:


$$
J_k<0,\qquad \operatorname{sgn}(Z_k)=(-1)^{k+1}
\tag{8}
$$


for all sufficiently large $k$. These statements use the complete raw remainder, not a first-tail model.

---

### 3. Uniform complete-error estimate for every filter order

Choose


$$
0<\eta<\frac{d-r}{2}.
$$


By (7), there exists an integer $N_\eta$ such that, for every $k\ge N_\eta$,


$$
J_k<0,\qquad
\frac{|J_{k+1}|}{|J_k|}\ge d-\eta,
\qquad
\frac{|Z_{k+1}|}{|Z_k|}\le r+\eta.
\tag{9}
$$


The inherited nonvanishing theorem permits choosing this threshold so that every $Z_k$ is nonzero as well.

For every $n\ge N_\eta$, every $m\ge0$, and every $0\le j\le m$,


$$
|J_{n+j}|\ge |J_n|(d-\eta)^j,
\qquad
|Z_{n+j}|\le |Z_n|(r+\eta)^j.
$$


All terms in the endpoint sum have one sign. Therefore


$$
|\mathcal J_{n,m}|
\ge |J_n|\bigl(b+a(d-\eta)\bigr)^m>0,
\tag{10}
$$


whereas


$$
\left|\sum_jw_jZ_{n+j}\right|
\le |Z_n|\bigl(b+a(r+\eta)\bigr)^m.
\tag{11}
$$



Thus the center is defined throughout this entire growing-order domain, and


$$
\boxed{
|\mathcal S-c_{n,m}|
\le
\left|\frac{R_n}{Y_n}\right|
\left(
\frac{1+\theta(r+\eta)}
     {1+\theta(d-\eta)}
\right)^m.
}
\tag{12}
$$



This estimate is uniform in **all** $m\ge0$. It includes both complete tails and every varying cofactor amplitude through the exact $Z_k$.

For example, when $m=\lfloor cn\rfloor$, $c>0$ fixed,


$$
\limsup_{n\to\infty}
\frac1n\log|\mathcal S-c_{n,\lfloor cn\rfloor}|
\le
-\tau+
c\log\frac{1+\theta r}{1+\theta d},
\qquad
\tau=2\log(1+\sqrt2).
\tag{13}
$$


Here $\log0=-\infty$; no nonvanishing is implicit in this assertion.

The additional exponent is strictly negative. This proves a genuine whole-error improvement relative to the starting index $n$. It does **not** prove improvement relative to the best individual approximant at the last index $n+m$: indeed


$$
\frac{1+\theta r}{1+\theta d}>\frac rd=3-2\sqrt2.
$$


Nor does (12) exploit the alternating cancellation of the $Z_k$; it is a robust upper bound obtained without assuming such cancellation.

---

### 4. Quantitative actual-denominator bound—and its limitation

The final gcd (4) immediately gives the explicit bound


$$
\boxed{
q\le
L_N\sum_{j=0}^m
\binom mj a^jb^{m-j}
\frac{|\mathscr D_{n+j}|}{((n+j)!)^2}.
}
\tag{14}
$$


This is a bound for the actual denominator, not an identification of it with the clearer.

One can make its growth scale explicit without a state recurrence. For the auxiliary polynomial


$$
\mathbf H_k(x)=k![z^k]e^{xz}(1-z+z^2/2)^k,
$$


the sum of absolute coefficients is at most


$$
k!\sum_{s=0}^k\frac{(5/2)^k}{(k-s)!}
\le e\,k!(5/2)^k.
$$


Derivatives of order at most two cost at most a polynomial in $k$. Hence the integer quantities $H_k,J_k,K_k$ occurring in the contiguous formula have size


$$
k!\exp(O(k))\,k^{O(1)}.
$$


The Legendre endpoints have size $\exp(O(k))$. Substituting into


$$
\mathscr D_k=(k+1)^2L_{k+1}(1)C_k-2L_k(1)S_k
$$


therefore gives


$$
\frac{|\mathscr D_k|}{(k!)^2}=\exp(O(k)).
\tag{15}
$$


Polynomial factors are absorbed into the exponential bound.

For fixed $a,b$, (14)–(15) yield


$$
\boxed{
\log q\le 6N\log N+O(N),\qquad N=n+m.
}
\tag{16}
$$


The coefficient $6$ comes from $(2N+2)!(N!)^4$.

This is quantitative but not remotely sharp enough. For $m\asymp n$, the proved analytic bound is exponential in $n$, while (16) still allows factorial-scale denominator growth. Nothing here proves primitive shrinking.

There is a second independent gap: although the endpoint is nonzero uniformly, the alternating sum


$$
\sum_jw_jZ_{n+j}
\tag{17}
$$


has not been proved nonzero. Consequently (5) must presently be retained without a nonvanishing assertion.

---

### 5. Secondary review: A5’s endpoint integrality above $n$

I find A5’s Proposition 9.1 correct, with a useful clarification of the reflection range.

For $p\ge n+2$, $k\in\{n,n+1\}$ satisfies $k<p$, and every factorial index in $T_j(L_k)$ is at most


$$
n+k-j\le2n+1<2p.
$$


Thus every factorial pole has order at most one.

A coefficient of degree $u$ needs cancellation only when


$$
n+u-j\ge p.
\tag{18}
$$


If any such degree exists, then $n+k-j\ge p$, which places $k$ in the upper half of $0,\ldots,p-1$. The reflection congruence is therefore applicable with $r=p-1-k$:


$$
L_k(y)\equiv\varepsilon(-4)^{-r}L_r(y)\pmod p.
$$


For $k=n$, the surviving degree is at most $p-1-n$, giving


$$
n+u-j\le p-1-j<p.
$$


For $k=n+1$, it is at most $p-2-n$, giving an even smaller index. Thus every coefficient whose partial sum can have a factorial pole is divisible by $p$, canceling that pole.

The second-kind moments have degree at most $n$; their denominators divide powers of $2$ times integers at most $n+1<p$. Also $G$ is a $p$-unit. This proves integrality of both complete endpoint rows.

For $p=n+1$, the separate pole-aware proof is necessary: $G$ and $w_U$ are not units. A5’s Section 2 correctly keeps those poles, and its cancellation argument for $t_j,x_j$ passes this review.

**Scope:** this verifies endpoint integrality, not the entire moving-prime norm calculation or a global denominator theorem.

---

## (1) New result and proof status

**Proved:** the factorial-compensated signed raw filter (2) has a nonzero endpoint for every $n\ge N_\eta$ and every $m\ge0$, and satisfies the uniform complete-error bound (12). Its exact final gcd and actual denominator are (4), with the quantitative upper bounds (14) and (16).

**Independently reviewed:** A5’s global endpoint-integrality proposition, including the reflection range and factorial-pole cancellations.

**Not proved:** filtered whole-error nonvanishing, primitive shrinking, or irrationality of $e+\pi$.

## (2) Exact remaining bottleneck

For this specified construction, the two missing estimates are now explicit:

1. Prove nonvanishing—or a signed asymptotic—for the complete alternating sum (17), uniformly for $m\asymp n$.
2. Control the final gcd
   

$$
\gcd\!\left(
   \left|L_N\sum_jw_jH_{n+j}\right|,
   \left|L_N\sum_jw_jJ_{n+j}\right|
   \right)
$$


   sharply enough to replace the factorial-scale denominator bound by a favorable exponential one.

The common annihilator does not resolve either issue: annihilating both outputs would destroy the endpoint.

## (3) Computation request

None. The present estimates and the integrality audit have direct proofs. A finite scan of filtered errors or gcds would not establish either missing uniform assertion.
