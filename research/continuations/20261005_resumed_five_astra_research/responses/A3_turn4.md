> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A3, Turn 4 — General rational endpoint weights: exact local cancellation, height sparsity, and the remaining resonance problem

## 1. Executive summary and proof status

Let


$$
S=e+\pi,\qquad M=1+\sqrt2,\qquad b=d+1,
$$


and retain the complete original rational columns, with original coordinates $0,\ldots,b$. For an arbitrary reduced rational weight


$$
\lambda=\frac ak,\qquad a\in\mathbb Z,\quad k>0,\quad \gcd(a,k)=1,
$$


consider exactly


$$
c_\lambda=\frac ak c_0+\left(1-\frac ak\right)c_b.
$$



The main arithmetic result of this report is an exact classification at every prime satisfying


$$
p>d\ge2,\qquad p\mid n,\qquad \tau_nD_d\not\equiv0\pmod p.
$$



Write


$$
m_p=2v_p(n!),\qquad w_p=v_p(v_0),
$$


where $v_0$ here is the **actual unnormalized companion endpoint**, including its exterior $+1$. A new consequence of the complete producer is


$$
\boxed{w_p\ge v_p(n).}
$$



The classification shows:

* If $p\mid k$, the denominator contribution increases:
  

$$
\boxed{v_p(q_\lambda)=m_p+v_p(k).}
$$


* If $p\nmid k$, ordinary cancellation is limited by the $p$-part of $a-k$ and the actual valuation $w_p$.
* Cancellation through the **final shared-endpoint gcd** can occur only on the precise resonance
  

$$
\boxed{v_p(a-k)=w_p<m_p.}
$$


  Even on that resonance, additional cancellation requires a further explicit congruence. Equality of valuations alone is not enough.

For weights of height


$$
\mathcal H=\max(|a|,k),
$$


ordinary cancellation over any set of eligible primes costs at most the factor $|a-k|\le2\mathcal H$, unless $a=k=1$. Thus a subexponential-height weight cannot remove exponentially many of the eligible factorial prime powers **except through the identified resonant final gcd**.

There is also a rigorous sparsity statement: for a fixed finite set of eligible primes, only $O(n^{|\mathcal P|})$ weights of subexponential height can cancel an exponentially large selected-prime modulus. This is a uniqueness/rational-reconstruction theorem, not an exclusion of those exceptional weights.

On the analytic side, retain provisionally Turn 3’s fixed-$d$ coefficient


$$
C_d=2d-3-3\sqrt2.
$$


The exact whole-error cancellation weight is


$$
\Lambda_{n,d}=\frac{c_b-S}{c_b-c_0},
$$


and provisionally


$$
\boxed{\Lambda_{n,d}
=\frac{n^2}{d}+\frac{C_dn}{d}+O_d(1).}
$$


This yields a careful height analysis:

* Approximating the irrational coefficient is genuinely necessary for improving the first signed defect.
* Nevertheless, an extra large denominator is **not automatically necessary**: rounding the algebraic threshold to an integer already gives an $O(n^{-2})$ relative-error upper bound.
* Pell approximants have an exact additional denominator cost, stated below.
* No finite-order expansion supplies a lower bound for approximation to the **actual** threshold beyond its remainder.

Finally, an explicit polynomial-height, integer-weight family is given whose complete whole error has a proved nonzero asymptotic, conditional on the provisional third-order contrast. Its eligible factorial prime powers survive, and its actual primitive forms diverge. This is a new example illustrating the interaction between rational approximation, congruence restrictions, and the full gcd—not a favorable irrationality construction.

No tools were executed.

---

## 2. Retained objects and exact normalization

The finite contact and reconstruction ranges remain


$$
C,\mathsf T,\mathcal S:\{0,\ldots,d\}^2,
\qquad
Z:\{0,\ldots,d+1\}\times\{0,\ldots,d\}.
$$


There is no extension of a matrix inverse beyond its original finite boundary.

Let the least actual two-column clearer be $d_B$, and write


$$
U=d_Bu,\qquad V=d_Bv.
$$


Reduce the endpoint rows:


$$
r_0=\gcd(|U_0|,|V_0|),\qquad
r_b=\gcd(|U_b|,|V_b|),
$$




$$
(\widetilde u_j,\widetilde v_j)
=(U_j/r_j,V_j/r_j),\qquad j=0,b.
$$


Then put


$$
h=\gcd(|\widetilde u_0|,|\widetilde u_b|),\qquad
\widetilde u_0=hA,\quad \widetilde u_b=hB,
$$


so that $\gcd(A,B)=1$.

It is useful to distinguish two normalized endpoint products:


$$
\mathcal W=B\widetilde v_0,\qquad
\mathcal V=A\widetilde v_b.
$$


Thus


$$
J=\mathcal W-\mathcal V
=B\widetilde v_0-A\widetilde v_b,
$$


and the numerator of the weighted center is


$$
T=aJ+k\mathcal V.
$$


Equivalently,


$$
\boxed{T=(a-k)J+k\mathcal W.}
\tag{2.1}
$$



The exact center and its full primitive reduction are


$$
c_\lambda=\frac{T}{khAB},
$$




$$
F=\gcd(|A|,|a|)\gcd(|B|,|a-k|),
\qquad
G=\gcd(k,|J|),
$$




$$
H_{\rm gcd}
=\gcd\!\left(h,\frac{|T|}{FG}\right),
$$




$$
\boxed{
q_\lambda=\frac{kh|AB|}{FGH_{\rm gcd}},
\qquad
p_\lambda=\operatorname{sgn}(AB)\frac{T}{FGH_{\rm gcd}}.
}
\tag{2.2}
$$


The usual conventions for gcd with zero apply. In particular, these formulas also cover $a=0$ and $a=k=1$.

This is the accepted endpoint decomposition, now used with general $a,k$. No raw-minor content is added to it a second time.

---

## 3. A stronger local fact about the actual companion endpoint

### Proposition 3.1 — Divisibility by the full $p$-part of $n$

Under


$$
p>d\ge2,\qquad p\mid n,
$$


the complete producer satisfies


$$
\boxed{v_p(v_0)\ge v_p(n).}
\tag{3.1}
$$



This assertion does not require the extra unit condition on $\tau_nD_d$; that condition will be used for the first-column valuations.

### Proof

Set


$$
s=v_p(n).
$$


The accepted complete producer uses


$$
Q(z)=1-z+\frac{z^2}{2},\qquad q_j=[z^j]Q(z)^n,
$$




$$
\mathcal B_K
=\sum_{j=0}^{\min(K,2n)}q_jK^{\underline j},
$$


and


$$
\mathcal W_\ell
=\ell!\sum_{r=0}^{\ell}\frac1{r!}
+\sum_{r=1}^{\ell}\frac{2\ell!\alpha_{r-1}}r
\in\mathbb Z[1/2].
$$



First, for every $j\ge1$ and $K\ge j$,


$$
\boxed{q_jK^{\underline j}\in n\mathbb Z[1/2].}
\tag{3.2}
$$


Indeed, selecting $l$ nonconstant factors, of which $r$ contribute $z^2/2$, gives $j=l+r$ and a contribution


$$
(-1)^{l-r}
\frac{n^{\underline l}}{r!(l-r)!2^r}
K^{\underline{l+r}}.
$$


Since


$$
\frac{K^{\underline{l+r}}}{r!(l-r)!}
=
\binom K{l+r}\frac{(l+r)!}{r!(l-r)!}
$$


is integral and $n\mid n^{\underline l}$, (3.2) follows term by term. Consequently,


$$
\mathcal B_K\equiv1\pmod{p^s}.
\tag{3.3}
$$



For the complete companion force,


$$
w_i
=\sum_{j=0}^{\min(2n,n+i)}
q_j(n+i)^{\underline j}\mathcal W_{2n+i-j},
$$


equation (3.2) gives


$$
w_i\equiv\mathcal W_{2n+i}\pmod{p^s}.
\tag{3.4}
$$



The logarithmic/arctangent part of $\mathcal W_\ell$ vanishes modulo $p^s$ when $\ell\ge2n$. To see this, the function


$$
v_p(\ell!)-\lfloor\log_p\ell\rfloor
$$


is nondecreasing for positive integer $\ell$. At $\ell=2p^s$,


$$
v_p((2p^s)!)-\lfloor\log_p(2p^s)\rfloor
=
2(1+p+\cdots+p^{s-1})-s
\ge s.
$$


Thus every term $2\ell!\alpha_{r-1}/r$ has valuation at least $s$.

The exponential part is


$$
\ell!\sum_{r=0}^{\ell}\frac1{r!}
=\sum_{t=0}^{\ell}\ell^{\underline t}.
$$


At $\ell=2n+i$,


$$
\sum_{t=0}^{2n+i}(2n+i)^{\underline t}
\equiv\sum_{t=0}^{i}i^{\underline t}\pmod{p^s}.
$$


Therefore


$$
w_i\equiv\sum_{t=0}^{i}i^{\underline t}\pmod{p^s}.
\tag{3.5}
$$



Meanwhile,


$$
C_{ij}=(n+i)^{\underline j}\mathcal B_{n+i-j}
\equiv i^{\underline j}\pmod{p^s}.
$$


The matrix on the right is lower triangular with unit diagonal $i!$, because $d<p$. Thus, for $y=C^{-1}w$,


$$
y_j\equiv1\pmod{p^s}\qquad(0\le j\le d).
\tag{3.6}
$$



Finally, the complete reconstruction is


$$
v_0=1-\sum_{j=0}^{d}(-1)^jn^{\overline j}y_j.
$$


All $j\ge1$ terms are divisible by $p^s$, and $y_0\equiv1\pmod{p^s}$. Hence $p^s\mid v_0$. ∎

### Scope of this improvement

The proposition supplies a lower bound, not a universal exact value. The actual valuation may be larger than $v_p(n)$, and it may reach or exceed $2v_p(n!)$.

For exact arithmetic, it is determined by the complete numerator


$$
Y_0=\det C-s^T\operatorname{adj}(C)w.
$$


Since $\det C$ is a $p$-unit,


$$
\boxed{v_p(v_0)=v_p(Y_0).}
\tag{3.7}
$$


The exterior $+1$ is exactly the $\det C$ term here.

---

## 4. Exact local classification for general $a/k$

Assume henceforth


$$
p>d\ge2,\qquad p\mid n,\qquad \tau_nD_d\not\equiv0\pmod p.
\tag{4.1}
$$



Use the notation


$$
m=2v_p(n!),\qquad
w=v_p(v_0),\qquad
t=\min(m,w),
$$




$$
\kappa=v_p(k),\qquad r=v_p(a-k),
$$


with $v_p(0)=+\infty$.

The accepted local producer theorem, together with Proposition 3.1, gives


$$
v_p(u_0)=v_p(u_b)=m,\qquad
v_p(v_b)=0,\qquad w\ge v_p(n)\ge1,
$$


and $p\nmid d_B$. Therefore


$$
v_p(r_0)=t,\qquad v_p(r_b)=0,
$$




$$
v_p(h)=m-t,\qquad
v_p(A)=0,\qquad
v_p(B)=t,
$$




$$
v_p(\widetilde v_0)=w-t,\qquad
v_p(\widetilde v_b)=0.
$$


In particular,


$$
\boxed{
v_p(\mathcal W)=w,\qquad
v_p(\mathcal V)=0,\qquad
v_p(J)=0.
}
\tag{4.2}
$$



### 4.1 The coefficient denominator cannot cancel locally

Because $J$ is a unit,


$$
\boxed{v_p(G)=0}
\tag{4.3}
$$


for every rational weight.

If $\kappa>0$, coprimality of $a,k$ implies $p\nmid a$, and hence $r=0$. Equation (2.1) then makes $T$ a unit. Consequently,


$$
\boxed{
p\mid k
\quad\Longrightarrow\quad
v_p(q_\lambda)=m+\kappa.
}
\tag{4.4}
$$



Thus an eligible prime appearing in $k$ is a genuine added denominator cost, not a source of cancellation through $G$.

### 4.2 Nonresonant numerator valuations

Suppose $p\nmid k$. The two terms in


$$
T=(a-k)J+k\mathcal W
$$


have valuations $r$ and $w$.

If $r\ne w$,


$$
\boxed{v_p(T)=\min(r,w).}
\tag{4.5}
$$


Therefore


$$
\boxed{
v_p(q_\lambda)=\max\{0,m-\min(r,w)\}
\qquad(r\ne w).
}
\tag{4.6}
$$



The special weight $a=k=1$ has $T=\mathcal W$, so


$$
\boxed{
v_p(q_1)=\max(0,m-w).
}
\tag{4.7}
$$


This is simply the primitive denominator of $c_0$. It must be separated from estimates using the nonzero integer $a-k$.

### 4.3 The resonance and its additional congruence

Suppose


$$
p\nmid k,\qquad r=w<\infty.
$$


Define


$$
\chi=
v_p\!\left(
\frac{a-k}{p^w}J
+k\frac{\mathcal W}{p^w}
\right).
\tag{4.8}
$$


Both summands inside parentheses are units, so $\chi\ge0$, but $\chi$ need not be positive. Then


$$
\boxed{v_p(T)=w+\chi.}
\tag{4.9}
$$



The exact denominator valuation is


$$
\boxed{
v_p(q_\lambda)=\max(0,m-w-\chi).
}
\tag{4.10}
$$



When $w<m$, complete removal of the eligible $p$-part is therefore equivalent to


$$
\boxed{
\frac{a-k}{p^w}
\equiv
-k\,\frac{\mathcal W}{p^w}J^{-1}
\pmod{p^{m-w}}.
}
\tag{4.11}
$$



This is the precise resonant cancellation that escapes a bound based only on the ordinary size of $a-k$.

### 4.4 Which gcd performs the cancellation?

At this prime,


$$
\boxed{
v_p(F)=\min(m,w,r),\qquad v_p(G)=0.
}
\tag{4.12}
$$



Moreover,


$$
\boxed{
v_p(H_{\rm gcd})=
\begin{cases}
\min(m-w,\chi),&
p\nmid k,\ r=w<m,\\[2mm]
0,&\text{otherwise}.
\end{cases}
}
\tag{4.13}
$$



Thus the final shared gcd is locally nontrivial **only** when


$$
v_p(a-k)=v_p(v_0)<2v_p(n!)
$$


and the leading unit terms actually cancel.

Equations (4.12)–(4.13) give the compact exact classification


$$
\boxed{
v_p(q_\lambda)
=
m+\kappa-\min(m,w,r)-v_p(H_{\rm gcd}).
}
\tag{4.14}
$$



This includes the case $w\ge m$: then $h$ is a $p$-unit, so there is no final shared-factor cancellation at $p$, regardless of how large $v_p(T)$ becomes.

### 4.5 Raw-minor content is already exhausted

As in the accepted local proof,


$$
v_p(U_bV_0-U_0V_b)=m,
$$


while


$$
v_p(r_0r_bh)=t+0+(m-t)=m.
$$


Hence


$$
\boxed{v_p(J)=0.}
$$


The raw minor contributes no additional factor to $G$ or $H_{\rm gcd}$. The only new shared cancellation is the explicitly computed resonance (4.13).

---

## 5. The local cancellation target is one exact rational number

Define


$$
\Theta_{n,d}
=-\frac{\mathcal V}{J}
=\frac{A\widetilde v_b}
{A\widetilde v_b-B\widetilde v_0}.
\tag{5.1}
$$


At every eligible prime, its denominator is a unit and


$$
\Theta_{n,d}=1-\frac{\mathcal W}{J},
\qquad
v_p(\Theta_{n,d}-1)=w.
\tag{5.2}
$$


Also


$$
\boxed{T=J(a-k\Theta_{n,d}).}
\tag{5.3}
$$



Thus the local roots are not unrelated choices at different primes: they are reductions of the same exact rational $\Theta_{n,d}$.

Its real meaning is


$$
\Theta_{n,d}=\frac{c_b}{c_b-c_0}.
$$


It is the weight making the rational center equal to zero:


$$
c_{\Theta_{n,d}}=0.
$$



It is **not** the weight making the error relative to $S$ vanish. The latter is


$$
\Lambda_{n,d}=\frac{c_b-S}{c_b-c_0}.
\tag{5.4}
$$



This distinction is central:

* the full gcd asks for $p$-adic approximation to $\Theta_{n,d}$;
* analytic cancellation asks for real approximation to $\Lambda_{n,d}$.

A successful construction must make these two requirements compatible at its actual height.

---

## 6. Height bounds outside resonance, and a rigorous exceptional-weight sparsity theorem

Let $\mathcal P$ be a finite set of eligible primes for the current original index $n$. Define


$$
Q_{\mathcal P}(n)=\prod_{p\in\mathcal P}p^{2v_p(n!)},
\qquad
k_{\mathcal P}=\prod_{p\in\mathcal P}p^{v_p(k)},
$$


and let


$$
\mathcal R_{\mathcal P}(a,k)
=\prod_{p\in\mathcal P}p^{v_p(H_{\rm gcd})}.
$$


This last quantity is exactly the selected-prime part of the final shared gcd, not an auxiliary predicted divisor.

For $a\ne k$, equations (4.12)–(4.14) imply


$$
\boxed{
q_\lambda
\ge
\frac{Q_{\mathcal P}(n)k_{\mathcal P}}
{|a-k|\,\mathcal R_{\mathcal P}(a,k)}
\ge
\frac{Q_{\mathcal P}(n)}
{2\mathcal H\,\mathcal R_{\mathcal P}(a,k)}.
}
\tag{6.1}
$$



This has an important advantage over multiplying separate bounds prime by prime: the ordinary losses combine into a divisor of the **single integer** $a-k$. There is no extra factor $\mathcal H^{|\mathcal P|}$.

### 6.1 Conditional moderate-height prime survival

For a fixed finite $\mathcal P$, put


$$
L_{\mathcal P}
=2\sum_{p\in\mathcal P}\frac{\log p}{p-1}.
$$


Legendre’s formula gives


$$
Q_{\mathcal P}(n)
=\exp\bigl(L_{\mathcal P}n-O_{\mathcal P}(\log n)\bigr).
\tag{6.2}
$$



Hence, if


$$
\log\mathcal H=o(n),
\qquad
\log\mathcal R_{\mathcal P}(a,k)=o(n),
$$


then


$$
\boxed{
q_\lambda\ge
\exp\bigl(L_{\mathcal P}n-o(n)\bigr).
}
\tag{6.3}
$$



This is rigorous. Its unproved part, when applied uniformly to arbitrary moderate-height weights, is precisely the bound on the resonant factor $\mathcal R_{\mathcal P}$.

### 6.2 Rational-reconstruction uniqueness

Let $L\mid Q_{\mathcal P}(n)$. Since $J$ is a unit modulo $L$, cancellation of $L$ is equivalent to


$$
a\equiv k\Theta_{n,d}\pmod L.
\tag{6.4}
$$


The integer pairs satisfying this congruence form a lattice of determinant $L$.

If two distinct reduced fractions $a_1/k_1$, $a_2/k_2$ satisfy (6.4), then


$$
L\mid a_1k_2-a_2k_1.
$$


For heights at most $\mathcal H$,


$$
|a_1k_2-a_2k_1|\le2\mathcal H^2.
$$


Therefore:

> **Uniqueness theorem.** If $L>2\mathcal H^2$, at most one reduced rational weight of height at most $\mathcal H$ can cancel $L$.

If the weights are restricted to an interval of width $W$ and $k_i\le K$, the sharper criterion is


$$
L>WK^2.
\tag{6.5}
$$



This is a genuine height obstruction to having two such candidates. It is not a lower bound for the height of the one possible exceptional candidate.

### 6.3 Polynomially many exponentially cancelling exceptions

For a weight, let


$$
\ell_p=\min\{2v_p(n!),v_p(T)\},
$$


and


$$
L(a,k)=\prod_{p\in\mathcal P}p^{\ell_p}.
\tag{6.6}
$$


At a prime dividing $k$, $T$ is a unit, so $\ell_p=0$. Thus $L(a,k)$ is exactly the selected-prime cancellation modulus.

Suppose $\mathcal P$ is fixed and


$$
\log\mathcal H_n=o(n).
$$


For every fixed $\varepsilon>0$, sufficiently large $n$ satisfy


$$
e^{\varepsilon n}>2\mathcal H_n^2.
$$


For each possible vector $(\ell_p)_{p\in\mathcal P}$ with


$$
L(a,k)\ge e^{\varepsilon n},
$$


the uniqueness theorem allows at most one reduced weight of height at most $\mathcal H_n$. There are at most


$$
\prod_{p\in\mathcal P}\bigl(2v_p(n!)+1\bigr)
=O_{\mathcal P}(n^{|\mathcal P|})
$$


such vectors.

Consequently,


$$
\boxed{
\begin{gathered}
\text{Among all weights of subexponential height, at most }
O_{\mathcal P}(n^{|\mathcal P|})\\
\text{can cancel an exponentially large selected-prime modulus.}
\end{gathered}
}
\tag{6.7}
$$



This does not prove that the exceptional set is empty. It does reduce the unresolved moderate-height arithmetic to exceptional short rational reconstructions of a completely specified actual residue.

---

## 7. The complete whole error and its exact signed threshold

The complete coordinate error remains


$$
e_j:=c_j-S
=
\frac{E_j}{P_j}
+(-1)^{n+1}\frac{F_j}{P_j}
+(-1)^n\delta_{j0}\frac{D}{P_j}.
$$


The exponential force is still


$$
eE_i
=-[z^{n+i}]Q(z)^n
\int_0^1s^ne^{1-s+sz}\,ds,
$$




$$
E_j=
\nu_{n,d}\!\left(
R_j\sum_{i=0}^{d}\sigma^ie_{d-i}(z^{-1})eE_i
\right).
$$



For general $\lambda=a/k$, therefore,


$$
\begin{aligned}
c_\lambda-S={}&
(-1)^{n+1}
\left[
\lambda\frac{F_0}{P_0}
+(1-\lambda)\frac{F_b}{P_b}
\right]\\
&+\lambda\frac{E_0}{P_0}
+(1-\lambda)\frac{E_b}{P_b}
+(-1)^n\lambda\frac{D}{P_0}.
\end{aligned}
\tag{7.1}
$$


No force component or exterior endpoint is omitted.

The retained factorial estimates give


$$
\begin{aligned}
|\text{complete factorial residual}|
\le{}&
C\bigl(|\lambda|+|1-\lambda|\bigr)
\frac{2^d}{n!\sqrt n}\\
&+C|\lambda|\frac{\sqrt n}{n!B_0},
\qquad B_0=n^{\overline d}\sigma^{-d}.
\end{aligned}
\tag{7.2}
$$


For fixed $d\ge2$ and height $\mathcal H$, this is


$$
O_d\!\left(\frac{1+\mathcal H}{n!\sqrt n}\right).
\tag{7.3}
$$


The amplification has been included before estimating the remainder.

For sufficiently large fixed-$d$ indices, define


$$
\alpha_{n,d}=1-\frac{e_0}{e_b}.
$$


Then


$$
\Lambda_{n,d}=\alpha_{n,d}^{-1}
$$


and the following identities are exact for the **whole** errors:


$$
\boxed{
c_\lambda-S
=-e_b\alpha_{n,d}(\lambda-\Lambda_{n,d}),
}
\tag{7.4}
$$




$$
\boxed{
q_\lambda S-p_\lambda
=q_\lambda e_b\alpha_{n,d}(\lambda-\Lambda_{n,d}).
}
\tag{7.5}
$$



In particular,


$$
c_\lambda-S\ne0
\quad\Longleftrightarrow\quad
\lambda\ne\Lambda_{n,d}.
$$



### Provisional fixed-$d$ expansion

Retaining Turn 3 provisionally,


$$
\frac{e_0}{e_b}
=
1-\frac d{n^2}
+\frac{dC_d}{n^3}+O_d(n^{-4}),
\qquad C_d=2d-3-3\sqrt2.
$$


Hence


$$
\alpha_{n,d}
=\frac d{n^2}
\left(1-\frac{C_d}{n}+O_d(n^{-2})\right),
$$


and


$$
\boxed{
\Lambda_{n,d}
=\frac{n^2}{d}+\frac{C_dn}{d}+O_d(1).
}
\tag{7.6}
$$



These deductions have the same provisional analytic status as Turn 3. They make no assertion for growing $d$.

---

## 8. Height cost of approximating the irrational coefficient

Set


$$
\gamma_{n}(a,k)
=\frac{da-kn^2}{kn}.
\tag{8.1}
$$


Then


$$
\lambda=\frac{n^2}{d}+\frac n d\,\gamma_n.
$$


The exact reduced denominator of $\gamma_n$ is


$$
\boxed{
q_\gamma
=\frac{kn}{\gcd(|da-kn^2|,kn)}.
}
\tag{8.2}
$$



Define also the actual scaled threshold


$$
\gamma_n^*
=\frac{d\Lambda_{n,d}-n^2}{n}
=C_d+O_d(n^{-1}).
$$


Equation (7.4) gives


$$
\frac{c_\lambda-S}{e_b}
=
-\frac n d\,\alpha_{n,d}(\gamma_n-\gamma_n^*).
\tag{8.3}
$$


Thus, in the threshold regime,


$$
\frac{c_\lambda-S}{e_b}
=
\frac{C_d-\gamma_n}{n}
+O_d(n^{-2})
$$


when $\gamma_n$ remains bounded.

### 8.1 A quadratic irrationality bound

Put $c=2d-3$, so $C_d=c-3\sqrt2$, with conjugate $C_d'=c+3\sqrt2$. For a reduced rational $P/Q$,


$$
\left(\frac PQ-C_d\right)
\left(\frac PQ-C_d'\right)
=
\frac{P^2-2cPQ+(c^2-18)Q^2}{Q^2}.
$$


The integer numerator is nonzero. For $P/Q$ in a fixed bounded neighborhood of $C_d$,


$$
\boxed{
\left|\frac PQ-C_d\right|
\ge \frac{c_d}{Q^2}
}
\tag{8.4}
$$


for some $c_d>0$.

Therefore, approximation to $C_d$ with accuracy $\varepsilon$ requires


$$
Q\gg_d\varepsilon^{-1/2}.
\tag{8.5}
$$



For an $O(n^{-2})$ relative signed error, the available expansion requires approximation to $C_d$ at scale $O(n^{-1})$, so necessarily


$$
q_\gamma\gg_d\sqrt n.
$$


But this does **not** imply $k\gg\sqrt n$: $q_\gamma$ already contains the factor $n$.

Indeed, integer rounding of


$$
\frac{n^2+C_dn}{d}
$$


has $k=1$, height $O_d(n^2)$, and changes $\gamma_n$ by only $O_d(n^{-1})$. Thus:



$$
\boxed{
\text{The irrational cubic coefficient does not force an extra growing weight denominator
for a one-order analytic gain.}
}
$$



It does force genuine approximation; it cannot be replaced by an exact rational coefficient.

### 8.2 What Pell approximation actually costs

Let $P/Q$ be a reduced rational approximation to $C_d$, and take an integer offset $L$. The natural weight is


$$
\lambda
=\frac{n^2+nP/Q+L}{d}
=\frac{Q(n^2+L)+nP}{dQ}.
$$


Its exact coefficient reduction is


$$
g_\lambda=\gcd\bigl(|Q(n^2+L)+nP|,dQ\bigr),
$$




$$
\boxed{
a=\frac{Q(n^2+L)+nP}{g_\lambda},
\qquad
k=\frac{dQ}{g_\lambda}.
}
\tag{8.6}
$$


Since $\gcd(P,Q)=1$,


$$
g_\lambda\le d\,\gcd(n,Q),
$$


and hence


$$
\boxed{k\ge \frac{Q}{\gcd(n,Q)}.}
\tag{8.7}
$$



Pell approximation gives the classical $O(Q^{-2})$ coefficient error, but its denominator cost is therefore real unless it is canceled by the displayed actual gcd. After that reduction, the endpoint factors $F,G,H_{\rm gcd}$ must still be computed.

In particular, at an eligible prime dividing $k$, equation (4.4) applies: the additional coefficient denominator survives.

Finite-order Richardson methods have the same normalization obligation. A method using several original indices would require a new cross-index denominator analysis; the present within-index theorem cannot be transferred to it automatically.

### 8.3 The crucial limit of the coefficient argument

The available expansion gives only


$$
\gamma_n^*=C_d+O_d(n^{-1}).
$$


Consequently, a very small value of $|\gamma_n-C_d|$ does not prove a very small—or a nonzero—value of $|\gamma_n-\gamma_n^*|$.

Beyond the $n^{-2}$ relative-error scale, the unknown higher-order threshold displacement can dominate the coefficient approximation. A quadratic irrationality bound for $C_d$ is not a Diophantine bound for the whole threshold $\Lambda_{n,d}$.

---

## 9. A concrete moderate-height family with analytic gain and proved primitive-form divergence

This example is deliberately nonresonant. It shows that polynomial-height threshold approximation is possible while the actual factorial denominator obstruction remains.

Take


$$
d=2,\qquad n\in15\mathbb Z_{>0}.
$$


The accepted digit transfers make $p=3,5$ eligible for every such $n$.

Let


$$
C_2=1-3\sqrt2,\qquad
L_n=\lfloor\log_2 n\rfloor,
$$


and define the integer weight


$$
\boxed{
a_n
=
15\left\lceil\frac{n^2+C_2n}{30}\right\rceil
+15L_n,
\qquad k_n=1.
}
\tag{9.1}
$$


This uses only $n$ and a quadratic irrational with exact algebraic comparisons. It does not use $S$.

Its height is


$$
a_n=\frac{n^2}{2}+O(n),
\qquad \mathcal H_n=O(n^2).
$$


Moreover,


$$
a_n-\Lambda_{n,2}=15L_n+O(1),
$$


so it is positive for all sufficiently large $n$.

Using the provisional fixed-$d$ whole-error law,


$$
e_b=(-1)^{n+1}4\pi M^{-2n-3}(1+O(n^{-1})),
$$


and $\alpha_{n,2}=2n^{-2}(1+O(n^{-1}))$, equation (7.4) gives


$$
\boxed{
c_{a_n}-S
=
(-1)^n\,120\pi\,
\frac{L_n}{n^2}M^{-2n-3}
\left(1+O(L_n^{-1})+O(n^{-1})\right).
}
\tag{9.2}
$$


This is a whole-error statement. In particular, it proves eventual nonvanishing.

The relative improvement is $O(\log n/n^2)$. Replacing $L_n$ by a sufficiently large fixed integer gives two-sided order $n^{-2}$, once a valid bound for the $O(1)$ threshold remainder is specified.

### Actual primitive denominator

Since $15\mid a_n$, both $a_n-1$ and $k_n$ are units at $3,5$. Thus the general local classification gives


$$
\boxed{
v_3(q_{a_n})=2v_3(n!),\qquad
v_5(q_{a_n})=2v_5(n!).
}
\tag{9.3}
$$


These are valuations after the full gcd in (2.2).

Legendre’s formula yields


$$
q_{a_n}\ge
\frac{\exp(L_{35}n)}{225n^4},
\qquad
L_{35}=\log3+\frac12\log5.
$$


Also


$$
\frac{e^{L_{35}}}{M^2}
=\frac{3\sqrt5}{3+2\sqrt2}
>\frac{11}{10}.
$$


Combining this with the nonzero whole error,


$$
\boxed{
|q_{a_n}S-p_{a_n}|
\ge c\,\frac{L_n}{n^6}\left(\frac{11}{10}\right)^n
\longrightarrow\infty
}
\tag{9.4}
$$


for some $c>0$, eventually on this original-index family.

This example is not the closed weight $n^2/d$. It demonstrates that even a better polynomial-height signed approximation can remain arithmetically unfavorable after its actual primitive reduction.

The analytic part of this example is conditional on the provisionally retained Turn 3 expansion; the denominator calculation is unconditional from the accepted producer arithmetic.

---

## 10. A valid whole-form obstruction—and why it is not yet general

Suppose $d$ and $\mathcal P$ are fixed, every prime in $\mathcal P$ is eligible along an infinite original-index sequence, and


$$
L_{\mathcal P}>2\log M.
$$


Let the weights satisfy


$$
a\ne k,\qquad
\log\mathcal H=o(n),\qquad
\log\mathcal R_{\mathcal P}(a,k)=o(n),
$$


and also


$$
|\lambda-\Lambda_{n,d}|\ge e^{-o(n)}.
\tag{10.1}
$$



Then the actual denominator bound and exact whole-error identity give


$$
|q_\lambda S-p_\lambda|
\ge
\exp\bigl((L_{\mathcal P}-2\log M)n-o(n)\bigr),
$$


so


$$
\boxed{|q_\lambda S-p_\lambda|\longrightarrow\infty.}
\tag{10.2}
$$



This is a genuine evaluated-form theorem: the distance hypothesis supplies nonvanishing and a lower bound for the whole error. It does not multiply a denominator lower bound by an error upper bound.

There are two distinct ways a general moderate-height family can escape the theorem:

1. **Arithmetic escape:** exponentially large resonant cancellation in $H_{\rm gcd}$.
2. **Analytic escape:** exceptionally close real approximation to the actual threshold $\Lambda_{n,d}$.

The quadratic coefficient $C_d$, by itself, rules out neither escape uniformly.

---

## 11. The precise next arithmetic lemma

The new local classification identifies a concrete problem rather than an unspecified “large gcd.”

For fixed $d$, a fixed eligible prime set $\mathcal P$, and a height bound $\mathcal H_n$, form the actual residues


$$
\Theta_{n,d}\equiv-\mathcal VJ^{-1}
\pmod{\prod_{p\in\mathcal P}p^{\ell_p}},
\qquad
0\le\ell_p\le2v_p(n!).
$$



A useful next lemma is:

> **Moderate-height resonant reconstruction lemma sought.**  
> For a specified infinite original-index family and specified $\mathcal H_n$ of polynomial or subexponential size, control all reduced solutions
> 

$$
> a\equiv k\Theta_{n,d}\pmod L,\qquad
> \max(|a|,k)\le\mathcal H_n,
>
$$


> where $L\mid Q_{\mathcal P}(n)$ is exponentially large. Prove either:
> 
> 1. a subexponential upper bound for their actual resonant factor
>    

$$
>    \mathcal R_{\mathcal P}(a,k);
>
$$


>    or
> 2. an explicit classification of the exceptional rational reconstructions, including their actual $F,G,H_{\rm gcd}$ and their location relative to the signed threshold.

For $L>2\mathcal H_n^2$, each modulus has at most one such reconstruction. The unresolved task is to control its **existence and identity along the original indices**, not to prove uniqueness again.

At one prime, the genuinely new digits are precisely


$$
\frac{\mathcal W}{p^{w_p}}J^{-1}
\pmod{p^{\,2v_p(n!)-w_p}},
$$


on the branch $w_p<2v_p(n!)$. The resonance equation is


$$
\frac{a-k}{p^{w_p}}
\equiv
-k\frac{\mathcal W}{p^{w_p}}J^{-1}
\pmod{p^{\,2v_p(n!)-w_p}}.
$$


A useful original-index transfer theorem must retain this complete companion residue. A theorem only about the raw endpoint minor, or only about $v_p(v_0)\ge1$, would not address the remaining cancellation.

Even a successful arithmetic lemma must then be paired with a whole-error statement. An exceptional candidate cannot be declared favorable or unfavorable from its denominator budget alone.

---

## 12. Bounded exact arithmetic for personal inspection

No finite computation is needed for the proofs in Sections 3–6. The following bounded calculation would check the new classification, including branches not covered by the old fixed weight.

### 12.1 Inputs

Use the complete producer at


$$
(n,d)=(9,2),(15,2),(25,2),(30,2),(25,3).
$$


All contact matrices have size at most $4\times4$, and the largest complete force index is at most $62$.

Retain:

* every coefficient through the actual force endpoint $2n+d$;
* the complete exponential and logarithmic/arctangent force;
* $v_0=1-s^Ty$;
* the actual least $d_B$;
* both row contents;
* $h,A,B,\widetilde v_0,\widetilde v_b,J$;
* the final $F,G,H_{\rm gcd}$.

Eligible local checks include


$$
\begin{array}{c|c|c}
(n,d)&p&m_p=2v_p(n!)\\ \hline
(9,2)&3&8\\
(15,2)&3&12\\
(15,2)&5&6\\
(25,2)&5&12\\
(30,2)&3&28\\
(30,2)&5&14\\
(25,3)&5&12
\end{array}
$$



### 12.2 Required endpoint outputs

For each eligible pair, return the exact value


$$
w_p=v_p(v_0),
$$


not merely the statement $w_p\ge1$, and verify


$$
w_p\ge v_p(n),
$$




$$
v_p(h)=m_p-\min(m_p,w_p),
\qquad
v_p(B)=\min(m_p,w_p),
\qquad
v_p(A)=v_p(J)=0.
$$



### 12.3 Weight probes

For each record and prime, inspect:

1. $a=0,k=1$, predicting $v_p(q_\lambda)=m_p$.
2. $a=1,k=p^2$, predicting $v_p(q_\lambda)=m_p+2$.
3. $a=k=1$, predicting
   

$$
v_p(q_\lambda)=\max(0,m_p-w_p).
$$


4. Weights $k=1,\ a=1+p^r u$, with $u$ a unit and $r<w_p$ or $r>w_p$, predicting the nonresonant formula.
5. When $w_p<m_p$, construct resonant probes by solving
   

$$
a\equiv\Theta_{n,d}\pmod{p^\ell}
$$


   at $\ell=w_p+1,m_p-1,m_p$, whenever these are distinct meaningful levels. Inspect the next digit to distinguish exact valuation from a lower bound.

For every probe, compare:

* direct single-gcd reduction of the rational center;
* formula (2.2);
* the predicted local $F,G,H_{\rm gcd}$ valuations.

No factorization of the large endpoint integers is required—only exact gcds, modular inverses of units, and repeated division by the selected prime.

### 12.4 Optional whole-error certificates

For any selected probe, use rational bounds obtained from the factorial series for $e$ and Machin’s formula


$$
\pi=16\arctan(1/5)-4\arctan(1/239)
$$


to return intervals for


$$
c_\lambda-S,\qquad q_\lambda S-p_\lambda.
$$


An interval containing zero remains inconclusive at that precision.

These are finite checks only. They do not establish a moderate-height reconstruction theorem along infinitely many original indices.

---

## 13. Final ledger

### New results proved from the accepted complete producer

1. The stronger actual companion divisibility
   

$$
v_p(v_0)\ge v_p(n).
$$



2. The complete local classification for every reduced rational weight $a/k$, including:
   * denominator primes $p\mid k$;
   * the actual $v_p(v_0)$;
   * nonresonant $a-k$;
   * the precise resonance;
   * the further unit cancellation in $T$;
   * the exact local final shared gcd.

3. The fact that eligible-prime final shared cancellation occurs only when
   

$$
v_p(a-k)=v_p(v_0)<2v_p(n!),
$$


   followed by the explicit congruence (4.11).

4. A global selected-prime height bound in which ordinary cancellation costs only $|a-k|$, not a separate height factor at every prime.

5. Rational-reconstruction uniqueness and polynomial sparsity of exponentially cancelling moderate-height weights.

### Analytic deductions retained provisionally

1. The exact threshold expansion
   

$$
\Lambda_{n,d}
   =\frac{n^2}{d}+\frac{(2d-3-3\sqrt2)n}{d}+O_d(1).
$$



2. A height analysis that distinguishes the reduced slope denominator from the actual weight denominator.

3. An explicit height-$O(n^2)$ integer-weight family with whole error of order
   

$$
\frac{\log n}{n^2}M^{-2n-3},
$$


   eventual nonvanishing, and actual primitive-form divergence.

### Exact remaining bottleneck

A universal moderate-height denominator theorem has not been proved. The obstruction is now localized: exceptional short rational reconstructions of the actual residue $-\mathcal V/J$, on the branch where the complete $v_0$-valuation resonates with $a-k$, can cancel the final shared denominator.

Nor has a universal real-approximation lower bound for the whole signed threshold been proved. The irrational cubic coefficient does not by itself supply one beyond the expansion’s remainder.

No family of nonzero whole primitive forms tending to zero has been constructed, and no favorable full-gcd regime with a sufficient analytic gain has been established.



$$
\boxed{\text{The irrationality or rationality of }e+\pi\text{ remains unresolved.}}
$$


