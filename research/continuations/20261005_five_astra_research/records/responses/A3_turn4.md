> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A3 continuation: the last-term valuation mechanism works; signed analytic gain remains unproved

Write $\mathcal S=e+\pi$. I obtain an affirmative answer to the coordinator’s last-term hypothesis **in the precise raw normalization of A3 turn 3**. It proves growth of the actual reduced denominator, and hence eventual nonvanishing of the entire filtered error, without assuming either rationality or irrationality of $\mathcal S$.

I also give an exact signed contour representation of the complete filtered remainder, retaining its cofactor amplitudes. However, I do **not** obtain the requested signed asymptotic for $m\asymp n$. I identify quantitatively why the supplied individual-index asymptotics cannot justify that asymptotic. Thus there is no irrationality decision or verified primitive shrinking result here.

## 1. Raw normalization: the factor $k+1$ must remain in this filter

Use $k\ge2$, $t=k+1$, and the notation of the supplied $b=2$ arithmetic source. In particular,


$$
f_k=\frac{2^k}{(k!)^2},
$$


and


$$
\begin{aligned}
\sigma_k&=t\,\mathsf k_k^2-\mathsf a_k\mathsf l_k,\\
C_k&=(t\mathsf k_k-\mathsf a_k)J_k^{\rm aux}
       -t(\mathsf l_k-\mathsf k_k)h_k,\\
\omega_k&=\mathsf k_kJ_k^{\rm aux}-\mathsf l_kh_k.
\end{aligned}
$$


Here the sans-serif letters distinguish the auxiliary integers from the compensated outputs below.

The exact normalized contractions are


$$
\begin{aligned}
\widetilde V_k&=\sigma_k\mathcal A_k-C_k\mathcal B_k-\mathsf a_k\omega_k,\\
\widetilde Q_k&=2w_k\sigma_k-tw_{k+1}C_k,\\
\widetilde D_k&=tL_{k+1}(1)C_k-2L_k(1)\sigma_k.
\end{aligned}
$$


The original contiguous scalars satisfy the exact identities


$$
V_k=t\widetilde V_k,\qquad
Q_k=t\widetilde Q_k,\qquad
\mathscr D_k=t\widetilde D_k.
\tag{1}
$$


These follow by substituting


$$
S_k=t\sigma_k,\qquad W_k=t\omega_k
$$


into the defining contiguous expressions. Thus no coefficient-content assertion or modular division is being used.

At the integer-$L$ raw cofactor scale,


$$
s_k=\frac{(-1)^k}{4(k!)^4(k+1)^3},
$$


and


$$
X_k=s_k\left(Q_k+2f_kV_k\right),\qquad
Y_k=s_k\mathscr D_k.
\tag{2}
$$


Consequently the compensated outputs from A3 turn 3 are exactly


$$
\boxed{
H_k=\frac{t\widetilde Q_k}{(k!)^2}
 +\frac{2^{k+1}t\widetilde V_k}{(k!)^4},
\qquad
J_k=\frac{t\widetilde D_k}{(k!)^2}.
}
\tag{3}
$$


In particular, the factorial rational term in $H_k$ has fourth-factorial depth, not second-factorial depth.

Although the factor $t$ cancels in the individual quotient $H_k/J_k$, it **cannot be canceled separately at each index inside the filter**. Formula (3) retains it.

### The residue-zero seed, calculated exactly

At the scalar seed $k=0$,


$$
(h,u,v,\mathcal A,\mathcal B)=(1,0,0,1,3).
$$


The polynomial formulas give


$$
\mathsf a=0,\quad \mathsf k=1,\quad \mathsf l=2,\quad
J^{\rm aux}=0,
$$


and hence


$$
\sigma=1,\qquad C=-1,\qquad \omega=-2.
$$


Therefore


$$
\boxed{\widetilde V_0=1-(-1)\cdot3-0=4.}
\tag{4}
$$


This is a direct seed calculation, not an inferred primitive-content normalization.

The supplied coefficient-extraction transfer applies to these raw polynomial expressions over $\mathbb Z[1/2]$. For clarity, its mod-$p$ mechanism is that in


$$
H_k^{(d)}(1)=\sum_s(k)_{s+d}[z^s](1-z+z^2/2)^k,
$$


all terms with $s+d>k\bmod p$ vanish modulo an odd $p$, and the surviving coefficients transfer by Frobenius. The same argument, together with


$$
D_j=jD_{j-1}+1,
$$


transfers $\mathcal A,\mathcal B$; at the boundary residue the formula for $\mathcal B$ is used before any division by $k+1$. Thus


$$
k\equiv0\pmod p
\quad\Longrightarrow\quad
\widetilde V_k\equiv4\pmod p.
\tag{5}
$$


Since $k+1\equiv1\pmod p$, the **original raw** $V_k$ is also a unit there.

No further evaluated contraction content has been removed. Indeed, (5) itself prevents any such common content from containing $p$ at the last index under consideration.

## 2. Uniform last-summand theorem

Let $p$ be any odd prime, let $a,b$ be positive integers with $p\nmid a$, and put


$$
w_j=\binom mj a^jb^{m-j},\qquad N=n+m.
$$


Assume


$$
n\ge2,\qquad m\ge0,\qquad N\ge p,\qquad p\mid N.
\tag{6}
$$


Define


$$
\mathcal H=\sum_{j=0}^m w_jH_{n+j},
\qquad
\mathcal J=\sum_{j=0}^m w_jJ_{n+j}.
$$


For an integer $k\ge2$, write


$$
F_k=v_p(k!),\qquad \ell_k=\lfloor\log_p(k+1)\rfloor.
$$



I prove


$$
\boxed{v_p(\mathcal H)=-4F_N,\qquad
v_p(\mathcal J)\ge-2F_N.}
\tag{7}
$$


The second inequality permits $\mathcal J=0$.

### 2.1 Second-kind bounds, including small indices

The moment formula gives


$$
v_p(w_k),\ v_p(w_{k+1})\ge-\ell_k.
$$


All coefficients multiplying these quantities in $\widetilde Q_k$ are integers. Hence


$$
v_p\left(\frac{(k+1)\widetilde Q_k}{(k!)^2}\right)
\ge-2F_k-\ell_k.
\tag{8}
$$


Also $\widetilde V_k\in\mathbb Z[1/2]$, so


$$
v_p\left(\frac{2^{k+1}(k+1)\widetilde V_k}{(k!)^4}\right)
\ge-4F_k.
\tag{9}
$$



We need a bound valid even when $k<p$:


$$
\boxed{\ell_k\le2F_k+1.}
\tag{10}
$$


If $\ell_k=0$ or $1$, this is immediate. If $\ell_k=e\ge2$, then


$$
k\ge p^e-1,\qquad F_k\ge p^{e-1}-1,
$$


and


$$
2(p^{e-1}-1)+1=2p^{e-1}-1\ge e.
$$


This proves (10) throughout the required domain.

### 2.2 Every earlier summand has strictly shallower valuation

For every $k<N$, divisibility of $N$ by $p$ implies


$$
F_N-F_k
=v_p((k+1)\cdots N)\ge1.
\tag{11}
$$


Combining (8)–(11),


$$
-2F_k-\ell_k
\ge-4F_k-1
\ge-4F_N+3,
$$


and


$$
-4F_k\ge-4F_N+4.
$$


Therefore


$$
\boxed{v_p(H_k)\ge-4F_N+3>-4F_N\quad(k<N).}
\tag{12}
$$


Multiplication by the integer weight $w_{k-n}$ cannot decrease these valuations.

This proves the strict comparison with **every** earlier term, not only the immediately preceding one.

### 2.3 The last summand has exact depth

By (5) and $p\nmid N+1$,


$$
v_p\left(\frac{2^{N+1}(N+1)\widetilde V_N}{(N!)^4}\right)
=-4F_N.
\tag{13}
$$


For $N\ge p$,


$$
2F_N>\ell_N.
\tag{14}
$$


Indeed, for $\ell_N=1$, $F_N\ge1$; for $\ell_N=e\ge2$,


$$
2F_N\ge2(p^{e-1}-1)>e.
$$


Thus the second-kind term in $H_N$ has valuation strictly greater than $-4F_N$. Equation (13) survives in the complete $H_N$.

Finally,


$$
w_m=a^m
$$


is a $p$-unit. The ultrametric inequality with a unique minimum now proves the first equality in (7).

Since $(k+1)\widetilde D_k$ is integral,


$$
v_p(J_k)\ge-2F_k\ge-2F_N.
$$


Summing proves the second assertion in (7).

## 3. Actual final gcd and whole-filter nonvanishing

Use the explicit common clearer from A3 turn 3:


$$
L_N=2^{N+1}(2N+2)!(N!)^4,
$$


and set


$$
U=L_N\mathcal H,\qquad T=L_N\mathcal J.
$$


These are integers. On $T\ne0$, put


$$
g=\gcd(|U|,|T|),\qquad
P=-\operatorname{sgn}(T)\frac Ug,\qquad
q=\frac{|T|}{g}>0.
\tag{15}
$$


Thus


$$
-\frac{\mathcal H}{\mathcal J}=\frac Pq,\qquad
\gcd(P,q)=1.
$$


This is the actual final endpoint reduction.

The rational quotient valuation, including precisely this gcd, gives


$$
v_p(q)
=\max\{0,v_p(\mathcal J)-v_p(\mathcal H)\}.
$$


Using (7),


$$
\boxed{v_p(q)\ge2v_p(N!).}
\tag{16}
$$



The inherited compensated endpoint sign is $J_k<0$ for every sufficiently large $k$. Thus there is a fixed, possibly ineffective, $n_0$ such that


$$
n\ge n_0,\quad m\ge0
\quad\Longrightarrow\quad
\mathcal J<0.
\tag{17}
$$


This establishes the quotient domain uniformly in $m$.

Define the complete compensated remainder


$$
Z_k=H_k+\mathcal S J_k.
$$


The actual primitive error is exactly


$$
\boxed{
q\mathcal S-P
=q\,\frac{\sum_{j=0}^m w_jZ_{n+j}}{\mathcal J}.
}
\tag{18}
$$



### Unconditional eventual nonvanishing

Fix $p\nmid a$ and restrict to (6), with $n\ge n_0$ and $N\to\infty$. Equation (16) implies $q\to\infty$.

* If $\mathcal S$ is irrational, the rational number $P/q$ cannot equal it.
* If $\mathcal S=A/B$ in lowest terms, equality would force $q=B$. Eventually $q>B$, so equality is again impossible.

Consequently,


$$
\boxed{\sum_{j=0}^m w_jZ_{n+j}\ne0}
\tag{19}
$$


for all sufficiently large $N$ on this domain, **unconditionally**.

This is a classical case distinction, not an assumption about the target. It proves no useful real lower bound for the error.

For the requested concrete choice $\theta=1/5$, take $a=1,b=5$. Every odd prime is admissible in the theorem. For example, the entire conclusion holds on $3\mid N$. One may also combine (16) over any fixed finite set of odd prime divisors required to divide $N$.

## 4. Exact signed contour representation of the complete error

Here is a representation that retains both tails and all varying endpoint amplitudes. It is not a normalized model integral.

For each $k\ge2$, set


$$
U_k(t)=L_{k+1}(t),\qquad
K_k^\partial(t)=K_k(t,1),
$$


and let


$$
W_k(t)=\frac1{1-t}-\operatorname{proj}_{\le k}\frac1{1-t}
$$


be the exact projection remainder for the supplied moment functional.

For a function $P$ analytic near $0$, define


$$
\mathcal C_{k,j}[P]
=\frac1{2\pi i}\int_{|z|=R}
 e^z z^{-k-2+j}P(1/z)\,dz,\qquad R>2.
\tag{20}
$$


All functions used here are analytic for $|t|<1$. Expanding on this contour,


$$
\mathcal C_{k,j}[P]
=\sum_{\nu\ge0}\frac{[t^\nu]P(t)}{(k+\nu+1-j)!}
=\ell_j(P),\qquad 0\le j\le2.
\tag{21}
$$


Uniform convergence on the contour justifies coefficient extraction.

Put


$$
\alpha_{k,j}=\mathcal C_{k,j}[U_k],\qquad
\beta_{k,j}=\mathcal C_{k,j}[K_k^\partial],
$$


and let


$$
\begin{aligned}
B_{k,0}&=\alpha_{k,1}(1+\beta_{k,2})
          -\alpha_{k,2}(1+\beta_{k,1}),\\
B_{k,1}&=\alpha_{k,2}(1+\beta_{k,0})
          -\alpha_{k,0}(1+\beta_{k,2}),\\
B_{k,2}&=\alpha_{k,0}(1+\beta_{k,1})
          -\alpha_{k,1}(1+\beta_{k,0}).
\end{aligned}
\tag{22}
$$


These are the actual integer-$L$ raw cofactor amplitudes.

The complete projection identity gives


$$
R_k=\sum_{\ell=0}^2 B_{k,\ell}\mathcal C_{k,\ell}[W_k].
$$


Therefore the entire signed filtered numerator in (18) is exactly


$$
\boxed{
\begin{aligned}
\sum_{j=0}^m w_jZ_{n+j}
={}&\frac1{2\pi i}\int_{|z|=R}e^z
\sum_{j=0}^m
4(-1)^{n+j}w_j((n+j)!)^2(n+j+1)^3\\
&\quad{}\times z^{-n-j-2}W_{n+j}(1/z)
\left(B_{n+j,0}+zB_{n+j,1}+z^2B_{n+j,2}\right)\,dz .
\end{aligned}}
\tag{23}
$$


Every sum here is finite except the absolutely convergent contour expansions already justified.

The exponential tail is the $1/(1-t)$ part of $W_k$; the subtracted projection is exactly the logarithmic/arctangent contribution. Thus (23) does not omit either tail or replace the cofactors by limiting constants.

What (23) does **not** yet do is sum the $j$-dependent kernel and cofactors into a phase whose steepest-descent analysis is uniform for $m\asymp n$. That is a genuine remaining analytic task.

## 5. Why the individual-index asymptotics do not prove signed gain

Let


$$
d=14+10\sqrt2,\qquad r=2+2\sqrt2.
$$


The established ratios are


$$
J_{k+1}/J_k\to d,\qquad Z_{k+1}/Z_k\to-r.
$$


For $(a,b)=(1,5)$, a purely geometric model would predict filter factors


$$
5+d\quad\text{and}\quad5-r,
$$


respectively. Since $0<5-r<1$, the predicted cancellation is severe.

The following elementary lemma quantifies a stability requirement.

### Signed-transform perturbation lemma

Suppose, on a window $n\le k\le n+m$,


$$
z_k=C(-r)^k(1+\varepsilon_k),\qquad
|\varepsilon_k|\le\delta.
$$


Then


$$
\sum_{j=0}^m\binom mj5^{m-j}z_{n+j}
=C(-r)^n(5-r)^m+E,
$$


where


$$
|E|\le |C|r^n\delta(5+r)^m.
\tag{24}
$$


This follows by expanding the sum and applying the binomial theorem separately to the main term and absolute perturbation.

Thus this route requires, at minimum,


$$
\delta\left(\frac{5+r}{5-r}\right)^m=o(1)
\tag{25}
$$


to preserve the predicted asymptotic. An $o(1)$ error, or an arbitrary fixed power saving in $n$, is inadequate when $m\asymp n$.

There is an explicit obstruction even for exponentially small individual errors. For $0<\rho<1$, define


$$
z_k=(-r)^k+r^k\rho^k
=(-r)^k\bigl(1+(-1)^k\rho^k\bigr).
$$


Then $z_{k+1}/z_k\to-r$, with exponentially small relative error, but exactly


$$
\sum_{j=0}^m\binom mj5^{m-j}z_{n+j}
=(-r)^n(5-r)^m+(r\rho)^n(5+r\rho)^m.
\tag{26}
$$


For $m=\lfloor cn\rfloor$, the second contribution dominates whenever


$$
\rho\left(\frac{5+r\rho}{5-r}\right)^c>1.
\tag{27}
$$


For every fixed $c>0$, this holds for $\rho<1$ sufficiently close to $1$.

This example is **not** a claim about the actual $Z_k$. It proves that even strong-looking individual asymptotics do not, by themselves, resolve the actual signed binomial transform. The missing information is the full set of analytic components and their transform growth, including components negligible before filtering.

## 6. Comparison at the same last index $N$

The previously proved absolute-value estimate remains


$$
|\mathcal S-P/q|
\le \exp(-\tau n+o(n))
 \left(\frac{5+r+o(1)}{5+d-o(1)}\right)^m,
\qquad
\tau=2\log(1+\sqrt2).
$$


Because


$$
\frac{5+r}{5+d}>\frac rd=e^{-\tau},
$$


this bound still does not beat the unfiltered error at $N=n+m$.

Nor does the new denominator result fix that comparison. We now know, for example on $3\mid N$,


$$
q\ge3^{2v_3(N!)}=\exp(N\log3+O(\log N)),
$$


but this is a **lower** bound for the actual denominator. The available upper bound remains


$$
\log q\le6N\log N+O(N).
$$


Neither bound identifies the final gcd in (15) sufficiently sharply for primitive shrinking.

The decisive quantity remains the whole expression


$$
\left|
q\,\frac{\sum_jw_jZ_{n+j}}{\sum_jw_jJ_{n+j}}
\right|,
$$


with the same $N$, the actual $q$, and the now-proved eventual nonvanishing.

## Deliverables

### (1) New result and proof status

**Proved, using the supplied exact $b=2$ identities:**

* The raw-scale residue-zero contraction is a unit at every odd prime: $\widetilde V_N\equiv4\pmod p$ when $p\mid N$.
* For $n\ge2$, $N=n+m\ge p$, $p\mid N$, and $p\nmid a$,
  

$$
v_p(\mathcal H)=-4v_p(N!),\qquad
  v_p(\mathcal J)\ge-2v_p(N!).
$$


* On the nonzero endpoint domain, the actual final reduced denominator satisfies
  

$$
v_p(q)\ge2v_p(N!).
$$


* With $n$ beyond the inherited endpoint-sign threshold, this proves unconditional eventual nonvanishing of the complete filtered error along the stated domain.
* Equation (23) is an exact signed contour representation with both tails and actual cofactor amplitudes retained.
* Equations (24)–(27) prove a quantitative obstruction to deriving a proportional-order signed asymptotic from the supplied individual-index asymptotics.

**Not proved:** a genuine signed gain for the actual filter, a favorable same-$N$ primitive-error estimate, or irrationality of $e+\pi$.

### (2) Exact remaining bottleneck

The analytic bottleneck is a uniform analysis of (23) for $m\asymp n$, resolving all components that survive the signed binomial transform—not merely the leading individual-index component.

The independent arithmetic bottleneck is a sufficiently sharp estimate of


$$
\gcd\!\left(
\left|L_N\sum_jw_jH_{n+j}\right|,
\left|L_N\sum_jw_jJ_{n+j}\right|
\right).
$$


The new valuation theorem controls certain local depths of this final reduction, but does not supply its required global upper bound.

### (3) Computation request

**None.** The valuation and nonvanishing results above are paper proofs. A finite scan of signed errors or endpoint gcds would not resolve the remaining proportional-order asymptotic or the infinite primitive-balance assertion.
