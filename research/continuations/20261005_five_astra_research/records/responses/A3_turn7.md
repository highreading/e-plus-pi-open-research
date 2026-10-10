> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

## New result: a fixed-prime exclusion on a power-of-three index class

The last factorial block can be retained exactly. Its residue is a finite scalar polynomial in $N\bmod p$ and $m\bmod p$, not a single last-term residue. This gives a new quantitative consequence: **a proportional-order subfamily with**


$$
N=3^{30a}
$$


**has primitive forms growing exponentially**, provided the proportional order lies in a sufficiently small subinterval of the supplied signed-existence interval.

This is different from the established primorial exclusion. It does not exclude the full filtered family or decide irrationality of $e+\pi$.

### 1. Exact normalization of the complete cross-index numerator

Retain, without indexwise cancellation,


$$
H_k=\frac{(k+1)\widetilde Q_k}{(k!)^2}
+\frac{2^{k+1}(k+1)\widetilde V_k}{(k!)^4},
\qquad
J_k=\frac{(k+1)\widetilde D_k}{(k!)^2}.
$$


For $n\ge2,\ m\ge0,\ N=n+m$, put


$$
\mathcal H=\sum_{j=0}^{m}\binom mj5^{m-j}H_{n+j},
\qquad
\mathcal J=\sum_{j=0}^{m}\binom mj5^{m-j}J_{n+j}.
$$



Reverse the summation index by $r=m-j$, and normalize the **whole** numerator as


$$
A_{N,m}=\frac{(N!)^4}{2^{N+1}}\mathcal H.
$$


Writing $(N)_r=N!/(N-r)!$, exact substitution gives


$$
\boxed{
A_{N,m}
=
\sum_{r=0}^{m}
\binom mr\left(\frac52\right)^r
(N)_r^4(N-r+1)\widetilde V_{N-r}
+E_{N,m},
}
\tag{1}
$$


where the complete second-kind contribution is


$$
\boxed{
E_{N,m}
=
\frac1{2^{N+1}}
\sum_{r=0}^{m}
\binom mr5^r
\frac{(N!)^4}{((N-r)!)^2}
(N-r+1)\widetilde Q_{N-r}.
}
\tag{2}
$$


In particular, (1) retains $V_{\mathrm{raw},k}=(k+1)\widetilde V_k$.

Fix an odd prime $p$, and write


$$
F_N=v_p(N!),\qquad \ell_N=\lfloor\log_p(N+1)\rfloor.
$$


The exact moment bound supplied in the source gives


$$
v_p(\widetilde Q_k)\ge-\lfloor\log_p(k+1)\rfloor.
$$


Since $v_p(k!)\le F_N$ for $k\le N$, every summand of (2) has valuation at least


$$
4F_N-2v_p(k!)-\ell_N\ge2F_N-\ell_N.
$$


Thus


$$
\boxed{v_p(E_{N,m})\ge2F_N-\ell_N.}
\tag{3}
$$


For $N\ge p$, the supplied elementary inequality $2F_N>\ell_N$ makes (2) zero modulo $p$. This is a separation of the actual second-kind term, not its omission.

### 2. The exact last-$p$-block polynomial

Let


$$
s=N\bmod p,\qquad t=m\bmod p,\qquad 0\le s,t<p.
$$


For $0\le r\le s$, all factors in $(N)_r$ are $p$-units and


$$
(N)_r\equiv(s)_r\pmod p.
$$


For $r>s$, $(N)_r$ contains a multiple of $p$, so its fourth power is zero modulo $p$.

The supplied all-residue scalar transfer gives


$$
\widetilde V_{N-r}\equiv\widetilde V_{s-r}\pmod p
\qquad(0\le r\le s).
$$


Lucas's theorem, applied only to $r<p$, gives


$$
\binom mr\equiv\binom tr\pmod p.
$$


Consequently, for every odd $p$ and $N\ge p$,


$$
\boxed{
A_{N,m}\equiv B_p(s,t)\pmod p,
}
\tag{4}
$$


where


$$
\boxed{
B_p(s,t)=
\sum_{r=0}^{s}
\binom tr
\left(\frac52\right)^r
(s)_r^4(s-r+1)\widetilde V_{s-r}
\quad\text{in }\mathbb F_p.
}
\tag{5}
$$


Here $\binom tr=0$ for $r>t$. If $m<s$, the additional terms written in (5) vanish for the same reason, so no extension of the original summation changes its value.

Equation (5) resolves the entire deepest factorial block. It retains:

* every binomial weight;
* the factorial unit ratios;
* the raw factor $N-r+1$;
* the scalar transfer at every residue, including $p-1$;
* all cancellations between equal-depth terms.

**No higher digits are necessary for this first residue.** They become necessary only when $B_p(s,t)=0$.

#### Explicit scalar evaluation, without a determinant

For completeness, the seeds in (5) can be defined entirely by finite scalar sums. Put


$$
a_j(x)=[z^j](1-z+z^2/2)^x,\qquad D_j=\sum_{u=0}^{j}(j)_u.
$$


For $x\ge0$, define


$$
h=\sum_{j\ge0}(x)_j a_j(x),\quad
u=\sum_{j\ge0}(x)_{j+1}a_j(x),\quad
v=\sum_{j\ge0}(x)_{j+2}a_j(x),
$$


with the sums ending where the falling factorial becomes zero, and


$$
\begin{aligned}
\mathcal A&=\sum_{j=0}^{x}(x)_j a_j(x)D_{2x-j},\\
\mathcal B&=2D_{2x+1}
+\sum_{j=1}^{x+1}(x)_{j-1}(2x+2-j)a_j(x+1)D_{2x+1-j}.
\end{aligned}
$$


Then set


$$
\begin{aligned}
a&=-xh+xu+v/2,\\
b&=(1-x)h+(x-1)u+v,\\
l&=(-x^2+3x+2)h+(x^2-2x-1)u+xv,\\
J&=xh+u,\\
\sigma&=(x+1)b^2-al,\\
\omega&=bJ-lh,\\
C&=((x+1)b-a)J-(x+1)(l-b)h.
\end{aligned}
$$


The exact original contraction is


$$
\boxed{\widetilde V_x=\sigma\mathcal A-C\mathcal B-a\omega.}
\tag{6}
$$


Thus (5)–(6) are an explicit scalar function of $s,t$, derived from the original Rodrigues/Legendre transfer, rather than an unevaluated determinant.

### 3. A genuine cancellation example

At $p=3$, the supplied exact seeds give


$$
\widetilde V_0\equiv\widetilde V_1\equiv\widetilde V_2\equiv1\pmod3,
\qquad 5/2\equiv1\pmod3.
$$


Formula (5) therefore becomes


$$
\boxed{
B_3(0,t)=1,\qquad
B_3(1,t)=2+t,\qquad
B_3(2,t)=2t+\binom t2.
}
\tag{7}
$$


In particular:

* $s=1,t=1$ gives cancellation of the deepest block;
* $s=2,t=0$ gives a nonunit because the surviving raw factor $s+1$ vanishes;
* $s=1,t=0$ is a unit;
* $s=2,t=1,2$ are units.

Thus a single-index unit theorem for $\widetilde V_k$ does not itself imply a filtered unit theorem. Both the raw factor and the binomial sum matter.

I make no inference that the nonunit cases in (7) have only logarithmic additional depth.

### 4. Quantitative consequence for the actual denominator

If $B_p(s,t)\ne0$, equations (3)–(5) prove


$$
v_p(A_{N,m})=0,
\qquad
\boxed{v_p(\mathcal H)=-4F_N.}
\tag{8}
$$


Independently, integrality of $(k+1)\widetilde D_k$ gives


$$
v_p(\mathcal J)\ge-2F_N.
\tag{9}
$$



Retain the actual final reduction. Set


$$
L_N=2^{N+1}(2N+2)!(N!)^4,\quad
U=L_N\mathcal H,\quad T=L_N\mathcal J,
$$


and, on $T\ne0$, define


$$
g=\gcd(|U|,|T|),\qquad
P=-\operatorname{sgn}(T)\frac Ug,\qquad q=\frac{|T|}{g}>0.
\tag{10}
$$


Then $P/q=-\mathcal H/\mathcal J$ and $\gcd(P,q)=1$. Exact rational reduction yields


$$
v_p(q)=\max\{0,v_p(\mathcal J)-v_p(\mathcal H)\}.
$$


Here one valuation is known **exactly** by (8), so (9) legitimately implies


$$
\boxed{B_p(s,t)\ne0\ \Longrightarrow\ v_p(q)\ge2v_p(N!).}
\tag{11}
$$



### 5. Simultaneous compatibility on $N=3^{30a}$

Take


$$
N_a=3^{30a},\qquad a\ge1.
$$


Then


$$
N_a\equiv0\pmod3,\qquad N_a\equiv1\pmod7,\qquad N_a\equiv1\pmod{11}.
$$


Indeed $3^6\equiv1\pmod7$ and $3^5\equiv1\pmod{11}$.

Require


$$
m_a\equiv0\pmod{77}.
$$


For $p=7,11$, this means $(s,t)=(1,0)$. In (5), all terms except $r=0$ vanish by Lucas's theorem, giving


$$
B_p(1,0)=2\widetilde V_1=32\pmod p,
$$


where $\widetilde V_1=16$ is supplied by the exact scalar formulas. This is nonzero at both primes. At $p=3$, equation (7) gives a unit for every $m_a$.

Thus all three bounds concern the **same actual $q$**:


$$
\boxed{
3^{2v_3(N_a!)}7^{2v_7(N_a!)}11^{2v_{11}(N_a!)}
\mid q.
}
\tag{12}
$$


Consequently,


$$
\boxed{
\log q\ge WN_a-O(\log N_a),\qquad
W=\log3+\frac{\log7}{3}+\frac{\log11}{5}.
}
\tag{13}
$$



Compatibility with any fixed proportional order $c>0$ is explicit. Choose


$$
m_a=77\left\lfloor\frac{cN_a}{77(1+c)}\right\rfloor,\qquad
n_a=N_a-m_a.
\tag{14}
$$


Then


$$
m_a/n_a\longrightarrow c,\qquad n_a\longrightarrow\infty.
$$


No assumption that general binomial weights are units has been used.

### 6. Comparison with the complete signed center decay

Retain the supplied signed-existence interval exactly as an inherited result:


$$
I=(c_0,c_0+\delta),\qquad
c_0=\frac5r-1,\quad r=2(1+\sqrt2),
$$


where $\delta>0$ is the existence constant from A3 turn 6. I do not reprove its density or saddle analysis.

Write


$$
d=2(1+\sqrt2)^3.
$$


On this interval the supplied complete signed theorem gives


$$
\log\left|e+\pi-\frac Pq\right|
=-\Gamma(c)N+o(N),
$$


where


$$
\Gamma(c)=
\frac{\log d+c\log(5+d)
-\log\!\left[\frac5{1+c}
\left(\frac{5c}{1+c}\right)^c\right]}{1+c}.
\tag{15}
$$



There is a rigorous strict margin at the left endpoint:


$$
\boxed{\Gamma(c_0)<\log9<W.}
\tag{16}
$$


Here is an elementary verification. Put $\tau=2\log(1+\sqrt2)$. Then


$$
\Gamma(c_0)
=\frac{\tau+c_0\log((5+d)/(5-r))}{1+c_0}.
$$


The rational bounds already used in the source, together with $d<31$, give


$$
c_0<\frac1{20},\quad 5-r>\frac16,\quad
\tau<\log(25/4),\quad \frac{5+d}{5-r}<216.
$$


Hence


$$
\Gamma(c_0)<\log(25/4)+\frac1{20}\log216<\log9.
$$


For the last inequality, $(36/25)^5>6$, so


$$
(36/25)^{20}>1296>216.
$$


Finally,


$$
7^{1/3}>\frac{19}{10},\qquad
11^{1/5}>\frac85,
$$


and therefore


$$
e^W>3\cdot\frac{19}{10}\cdot\frac85>9.
$$



By continuity, there exists $0<\eta\le\delta$ such that


$$
c_0<c<c_0+\eta\quad\Longrightarrow\quad \Gamma(c)<W.
\tag{17}
$$


This is a subinterval of the original existence interval, not a newly asserted numerical replacement for it.

Fix such a $c$, and use (14). The endpoint-sign theorem ensures $\mathcal J\ne0$ eventually. The supplied complete signed asymptotic ensures nonvanishing of


$$
\mathcal Z=\sum_{j=0}^{m}\binom mj5^{m-j}
\bigl(H_{n+j}+(e+\pi)J_{n+j}\bigr).
$$


The exact primitive error remains


$$
\boxed{
q(e+\pi)-P=q\,\frac{\mathcal Z}{\mathcal J}.
}
\tag{18}
$$


Combining (13), (15), and (17) proves


$$
\boxed{
\liminf_{a\to\infty}
\frac{\log|q(e+\pi)-P|}{N_a}
\ge W-\Gamma(c)>0.
}
\tag{19}
$$


The complete evaluated errors on this explicit power-of-three subfamily therefore grow exponentially.

## Concluding ledger

### (1) New result and proof status

**Proved from the supplied exact arithmetic identities:**

* The normalized whole last-block residue (5), with no omitted equal-depth terms.
* Its explicit scalar evaluation without determinants or higher-digit assumptions.
* The actual-denominator implication (11).
* Simultaneous fixed-prime compatibility at $3,7,11$ on $N=3^{30a}$, with $m/n\to c$.
* The quantitative denominator rate (13).

**Using the supplied signed interior theorem as an analytic dependency:** the new power-of-three subfamily exclusion (19), on a proved existence subinterval of its original interval.

### (2) Exact remaining bottleneck

When $B_p(s,t)=0$, this work does not control the higher carry depth of the complete numerator. In particular, it proves neither a uniform factorial-content estimate across all $N,m$ nor an $O(\log N)$ loss after first-digit cancellation.

The full filtered family remains open. The new subfamily exclusion supplies no irrationality decision for $e+\pi$.

### (3) Computation request

**None.** The selected residue conditions reduce exactly to $\widetilde V_0=4$ and $\widetilde V_1=16$, and simultaneous compatibility follows from the displayed congruences and rounding construction. No finite scan is needed for the asserted infinite subfamily theorem.
