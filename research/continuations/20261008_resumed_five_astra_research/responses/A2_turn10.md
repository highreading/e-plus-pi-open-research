> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Report on the Laguerre spread refinement and a paid dyadic reduction of the original coefficient pair

## 1. Executive verdict

### 1.1 First primary task: the new Laguerre–Jensen candidate

**Verdict: PASS, at the stated scope.**

For


$$
D_k=\bigl((2k+2i+2j)!\bigr)_{0\le i,j<k},
\qquad
B_k=2^{k(k-1)}
\prod_{j=0}^{k-1}j!(3k-1+j)!,
$$


the candidate correctly proves


$$
\boxed{
\det D_k\ge B_k\exp(R_k),\qquad
R_k=\frac{k(4k-1)(k^2-1)}{85k^2-37k+6}
}
\tag{1.1}
$$


for every integer $k\ge2$. In particular,


$$
\frac{R_k}{k^2}\longrightarrow \frac4{85}.
\tag{1.2}
$$



Combining this with the already differently audited same-$H$ reference comparison gives


$$
\boxed{
(-1)^kH_k(e+\pi)
\ge
\left(\frac{3\Lambda_k}{64}\right)^k
\mathfrak h_k B_k e^{R_k}>0
\qquad(k\ge512),
}
\tag{1.3}
$$


where


$$
\mathfrak h_k=\det\left(\frac1{i+j+1}\right)_{0\le i,j<k}.
$$


Consequently,


$$
\boxed{
\log |H_k(e+\pi)|
\ge
4k^2\log k+
\left(15\log2-\frac92\log3+\frac4{85}\right)k^2
+o(k^2).
}
\tag{1.4}
$$



The new lower-bound constant is


$$
\boxed{
C_H=15\log2-\frac92\log3+\frac4{85}
\approx5.500511232922098.
}
\tag{1.5}
$$



No content upper bound follows from this analytic result.

### 1.2 Second primary task: direct binary control of the final gcd

I do **not** prove


$$
v_2(G_k)\le\frac{13}{4}k^2+o(k^2)
$$


at the original indices.

I do prove a different, source-specific dyadic result:

* an explicit integer row operator annihilates the rational part of **every common original return column**;
* the resulting complete factorial-forcing pivot has an **exactly evaluated binary determinant valuation**;
* the literal contact atom has an exactly evaluated valuation under the same operator;
* these evaluations produce an exact, fully paid reduction of **both $H_{0,k}$ and $H_{1,k}$ simultaneously** to a smaller integer affine pencil.

The unpaid binary term in that reduction is specified explicitly in Section 8. This is an evaluated source mechanism, not an assertion that an unknown Schur determinant is a unit.

### 1.3 Global objective

The rationality or irrationality of $e+\pi$ remains unresolved.

Even a successful content upper bound making the primitive whole errors diverge would retire this compact producer as a source of primitive whole-error decay. It would not prove $e+\pi$ rational.

---

## 2. Fixed original objects, boundaries, and normalization

### 2.1 Original index set

The infinite original domain remains


$$
\boxed{
\mathcal K=\{K_u:u\ge0\},
\qquad
K_u=9^{18+32u}=3^{36+64u}.
}
\tag{2.1}
$$


Every member of $\mathcal K$ exceeds $512$.

Retain


$$
a_0=1,\qquad a_n=1-na_{n-1},
$$




$$
u_n=a_{2n},\qquad f_n=(2n)!,\qquad w_n=(-1)^n,
\qquad c_n=u_n-w_n,
$$


and


$$
\rho_0=0,\qquad
\rho_{n+1}+\rho_n=\frac1{2n+1},
\qquad
r_n=-f_n+4\rho_n.
\tag{2.2}
$$



The complete returns are


$$
\sigma_n=c_{n+1}+c_n=u_{n+1}+u_n
\tag{2.3}
$$


and


$$
\boxed{
\tau_n=r_{n+1}+r_n
=-(2n+2)!-(2n)!+\frac4{2n+1}.
}
\tag{2.4}
$$


Both factorial terms and the rational forcing are retained.

Put


$$
\Lambda_k=\operatorname{lcm}(1,3,\ldots,6k-5),
\qquad
T_n=\Lambda_k\tau_n.
\tag{2.5}
$$


Thus


$$
T_n
=
-\Lambda_k\bigl((2n+2)!+(2n)!\bigr)
+\frac{4\Lambda_k}{2n+1}
\tag{2.6}
$$


is the complete integer return entry.

The original affine determinant is


$$
\boxed{
H_k(s)=
\det\left[
(c_{m+j})\
\middle|\
\bigl(\Lambda_k(r_{m+j}+s(-1)^{m+j})\bigr)
\right]
=H_{0,k}+H_{1,k}s,
}
\tag{2.7}
$$


with


$$
0\le m<2k,\qquad 0\le j<k.
$$



The largest moment index is $3k-2$. Therefore the unchanged physical boundary is


$$
\boxed{
\text{moment }3k-2,\qquad
\text{factorial }(6k-4)!,\qquad
\text{last odd denominator }6k-5.
}
\tag{2.8}
$$



### 2.2 Actual clearers, final gcd, and primitive error

The individual least original right-column entry clearers remain


$$
\Lambda_{k,j}
=
\operatorname{lcm}(1,3,\ldots,4k+2j-3),
\qquad 0\le j<k.
\tag{2.9}
$$


The common least entry clearer of the complete unprojected right block is $\Lambda_k$.

The final gcd is the **all-prime** gcd


$$
\boxed{
G_k=\gcd(|H_{0,k}|,|H_{1,k}|).
}
\tag{2.10}
$$



For the rational pair $H_k/\Lambda_k^k$, put


$$
d_{H,k}=\gcd(\Lambda_k^k,H_{0,k},H_{1,k}).
$$


Its exact least simultaneous coefficient clearer and subsequent content are


$$
\boxed{
\frac{\Lambda_k^k}{d_{H,k}},
\qquad
\frac{G_k}{d_{H,k}}.
}
\tag{2.11}
$$


Nothing below replaces either actual quantity by a lower divisor.

The established sign theorem gives


$$
(-1)^kH_{1,k}>0\qquad(k\ge64).
$$


Thus, at every original index,


$$
q_k=\frac{|H_{1,k}|}{G_k}>0,
\qquad
p_k=-\frac{(-1)^kH_{0,k}}{G_k},
\tag{2.12}
$$


and the whole evaluated error is


$$
\boxed{
\ell_k=q_k(e+\pi)-p_k
=\frac{(-1)^kH_k(e+\pi)}{G_k}
=\frac{|H_k(e+\pi)|}{G_k}>0.
}
\tag{2.13}
$$



This is the quantity requiring asymptotic control. The smaller-looking approximation error


$$
\left|e+\pi-\frac{p_k}{q_k}\right|=\frac{\ell_k}{q_k}
$$


is not a substitute for it.

### 2.3 Reused content interface

The actual rectangles remain


$$
Z_k=
\left[
(c_{m+j})_{\substack{m<2k\\j<k}}
\ \middle|\
(T_{m+j})_{\substack{m<2k\\j<k-1}}
\right],
\tag{2.14}
$$




$$
Y_k=
\left[
(\sigma_{m+j})_{\substack{m<2k-1\\j<k}}
\ \middle|\
(T_{m+j})_{\substack{m<2k-1\\j<k}}
\right].
\tag{2.15}
$$


Write


$$
\mathscr R_k=\delta_{2k-1}(Z_k),
\qquad
\mathscr L_k=\delta_{2k-1}(Y_k).
$$


The established exact interface is


$$
\boxed{
\operatorname{lcm}(\mathscr L_k,\mathscr R_k)
\mid G_k
\mid \Lambda_k\mathscr L_k\mathscr R_k.
}
\tag{2.16}
$$



The differently audited ternary theorem is reused, not reproved:


$$
v_3(\mathscr L_k)=v_3(\mathscr R_k)=E_k,
\qquad
E_k=\frac{(k-2)(k-1-2s)}2
\quad(k=3^s\in\mathcal K).
\tag{2.17}
$$


It yields only


$$
\boxed{
E_k\le v_3(G_k)\le2E_k+s+1,
}
\tag{2.18}
$$


not an equality for $v_3(G_k)$.

---

## 3. Exact relative integral and Wishart normalization

### 3.1 The same reference determinant, before AM–GM

The reference determinant has the exact Gram representation


$$
\det D_k
=
\frac1{k!}
\int_{(0,\infty)^k}
V(z_1^2,\ldots,z_k^2)^2
\prod_{i=1}^k z_i^{2k}e^{-z_i}\,dz_i.
\tag{3.1}
$$


Since


$$
V(z^2)^2
=
V(z)^2\prod_{i<j}(z_i+z_j)^2,
$$


define


$$
g_{ij}=\frac{(z_i+z_j)^2}{4z_iz_j}.
$$


Then, exactly,


$$
V(z^2)^2\prod_i z_i^{2k}
=
2^{k(k-1)}
V(z)^2\prod_i z_i^{3k-1}
\prod_{i<j}g_{ij}.
\tag{3.2}
$$



The Laguerre normalizing integral is


$$
Z_k
=
\int_{(0,\infty)^k}
V(z)^2\prod_i z_i^{3k-1}e^{-z_i}\,dz_i
=
k!\prod_{j=0}^{k-1}j!(3k-1+j)!.
\tag{3.3}
$$


This is the previously established monic-Laguerre norm product, with the remaining $k!$ coming from determinant integration.

Consequently,


$$
\boxed{
\det D_k
=
B_k\,
\mathbb E\!\left[\prod_{i<j}g_{ij}\right],
}
\tag{3.4}
$$


where the expectation has normalized density


$$
\frac1{Z_k}
V(z)^2\prod_i z_i^{3k-1}e^{-z_i}.
\tag{3.5}
$$



This is an equality for the same $D_k$, before the old AM–GM estimate. No matrix entries, terminal factorials, or arithmetic normalizations have changed.

### 3.2 Correct complex Wishart convention

Let $X$ have $k$ rows and $m$ columns, with independent complex Gaussian entries of density


$$
\pi^{-1}e^{-|x|^2}.
$$


Thus


$$
\mathbb E|X_{ia}|^2=1.
$$


Set


$$
W=XX^*.
\tag{3.6}
$$



For $m\ge k$, the unordered eigenvalues of $W$ have density proportional to


$$
V(z)^2\prod_i z_i^{m-k}e^{-z_i}.
\tag{3.7}
$$


The Vandermonde exponent is $2$, because this is the **complex**, not real, Wishart law.

The required exponent $m-k=3k-1$ gives


$$
\boxed{m=4k-1.}
\tag{3.8}
$$



All traces below are unnormalized:


$$
T_j=\operatorname{Tr}(W^j),\qquad T_0=k.
$$


There is no factor $1/k$ in $W$ or in the trace. If one starts with a convention using $W/k$, its eigenvalues must be multiplied by $k$ to recover (3.7).

The exact normalizing constant in this convention is


$$
k!\prod_{j=0}^{k-1}j!\,\Gamma(j+m-k+1),
$$


which becomes (3.3) when $m=4k-1$.

**Normalization verdict: PASS.**

---

## 4. Uniform derivation of the order-two and order-four moments

The supplied permutation and polynomial-integral receipt is corroboration. The following derivation is uniform in the matrix dimensions and does not rerun the $2!$ or $4!$ enumeration.

### 4.1 Complex Gaussian contraction

For a standard complex Gaussian variable,


$$
\mathbb E[X F]=\mathbb E\!\left[\frac{\partial F}{\partial\overline X}\right]
\tag{4.1}
$$


for every polynomial $F$ in the Gaussian variables and their conjugates.

Equivalently, expanding trace products and pairing unbarred entries with barred entries gives


$$
\mathbb E\prod_{c\text{ cycle of }\gamma}T_{|c|}
=
\sum_{\sigma\in S_q}
m^{\#\operatorname{cycles}(\sigma)}
k^{\#\operatorname{cycles}(\gamma\sigma)}.
\tag{4.2}
$$


The column identifications contribute the powers of $m$, and the row identifications contribute the powers of $k$.

For the required evaluations, integration by parts provides a shorter algebraic derivation than enumerating permutations.

### 4.2 A trace recursion

Expanding one copy of $W=XX^*$ in $T_q$ and applying (4.1) gives


$$
\mathbb E T_q
=
m\,\mathbb E T_{q-1}
+
\sum_{r=0}^{q-2}
\mathbb E(T_rT_{q-1-r})
\qquad(q\ge2).
\tag{4.3}
$$



More generally, when an additional factor $T_p$ is present, differentiating that factor contributes


$$
p\,\mathbb E T_{q+p-1}.
\tag{4.4}
$$


Indeed,


$$
\frac{\partial T_p}{\partial\overline X_{ia}}
=
p(W^{p-1}X)_{ia},
$$


and contraction with the expanded $T_q$ yields $pT_{q+p-1}$.

All these integrations by parts are justified by Gaussian decay and polynomial integrands.

First,


$$
\mathbb E T_1=km.
\tag{4.5}
$$


Taking $q=1$ with an extra $T_p$ gives the useful identity


$$
\mathbb E(T_1T_p)=(km+p)\mathbb E T_p.
\tag{4.6}
$$



### 4.3 Second moments

Equation (4.3) at $q=2$ gives


$$
\boxed{
\mathbb E T_2=(m+k)km.
}
\tag{4.7}
$$


Equation (4.6) at $p=1$ gives


$$
\boxed{
\mathbb E T_1^2=km(km+1).
}
\tag{4.8}
$$



At $q=3$,


$$
\begin{aligned}
\mathbb E T_3
&=(m+k)\mathbb E T_2+\mathbb E T_1^2\\
&=km\bigl((m+k)^2+km+1\bigr).
\end{aligned}
\tag{4.9}
$$



### 4.4 Fourth-order formulas

At $q=4$,


$$
\mathbb E T_4
=
(m+k)\mathbb E T_3+2\mathbb E(T_1T_2).
$$


By (4.6),


$$
\mathbb E(T_1T_2)=(km+2)\mathbb E T_2.
$$


Substitution gives


$$
\begin{aligned}
\mathbb E T_4
&=km(m+k)\bigl((m+k)^2+3km+5\bigr)\\
&=
\boxed{
km\bigl[k^3+6k^2m+6km^2+m^3+5k+5m\bigr].
}
\end{aligned}
\tag{4.10}
$$



For $T_2^2$, use (4.3) with the extra factor $T_2$. The extra derivative contribution is $2T_3$, so


$$
\mathbb E T_2^2
=
(m+k)\mathbb E(T_1T_2)+2\mathbb E T_3.
$$


Hence


$$
\begin{aligned}
\mathbb E T_2^2
&=km\bigl[(km+4)(m+k)^2+2km+2\bigr]\\
&=
\boxed{
km\bigl[km(k+m)^2+4k^2+10km+4m^2+2\bigr].
}
\end{aligned}
\tag{4.11}
$$



These are precisely the four required unnormalized-trace formulas.

**Moment verdict: PASS by a uniform proof.**

---

## 5. Deterministic spread inequality, both Cauchy–Schwarz steps, and Jensen

For positive $z_1,\ldots,z_k$, define


$$
A=\sum_{i<j}(z_i-z_j)^2
=k\sum_i z_i^2-\left(\sum_i z_i\right)^2,
\tag{5.1}
$$




$$
B=\sum_{i<j}(z_i^2-z_j^2)^2
=k\sum_i z_i^4-\left(\sum_i z_i^2\right)^2.
\tag{5.2}
$$


Thus


$$
\boxed{B=k\operatorname{Tr}(W^4)-(\operatorname{Tr}(W^2))^2.}
\tag{5.3}
$$


The square on the second trace is essential.

### 5.1 Pairwise inequality

Put


$$
r_{ij}=\frac{z_i-z_j}{z_i+z_j}.
$$


Then $|r_{ij}|<1$, and


$$
g_{ij}=\frac1{1-r_{ij}^2}.
$$


Therefore


$$
\boxed{
\log g_{ij}=-\log(1-r_{ij}^2)\ge r_{ij}^2.
}
\tag{5.4}
$$



### 5.2 First Cauchy–Schwarz: the finite pair sum

Apply Cauchy–Schwarz to


$$
\frac{|z_i-z_j|}{z_i+z_j},
\qquad
|z_i-z_j|(z_i+z_j).
$$


It gives


$$
A^2
\le
\left(\sum_{i<j}r_{ij}^2\right)B.
$$


Hence, when $B>0$,


$$
\boxed{
\sum_{i<j}r_{ij}^2\ge\frac{A^2}{B}.
}
\tag{5.5}
$$



If all $z_i$ coincide, then $A=B=0$; define $A^2/B=0$ there. This makes the statement valid everywhere. Under the continuous Laguerre law, that exceptional set has probability zero.

Also,


$$
0\le\frac{A^2}{B}
\le \sum_{i<j}r_{ij}^2
\le \binom{k}{2}.
\tag{5.6}
$$



### 5.3 Second Cauchy–Schwarz: expectation

Since


$$
A=\frac{A}{\sqrt B}\sqrt B
$$


almost surely,


$$
(\mathbb EA)^2
\le
\mathbb E\!\left[\frac{A^2}{B}\right]\mathbb EB.
$$


Thus


$$
\boxed{
\mathbb E\!\left[\frac{A^2}{B}\right]
\ge
\frac{(\mathbb EA)^2}{\mathbb EB}.
}
\tag{5.7}
$$


Here $\mathbb EB>0$ for $k\ge2$.

### 5.4 Integrability and Jensen direction

Let


$$
P=\prod_{i<j}g_{ij},
\qquad S=\log P.
$$


Then $P\ge1$, $S\ge0$, and the exact relative integral (3.4) gives


$$
\mathbb EP=\frac{\det D_k}{B_k}<\infty.
$$


The factorial Gram integral is finite, so this is not an unproved tail assertion.

Moreover,


$$
0\le S\le P,
$$


and (5.6) bounds the intermediate ratio. All needed expectations are therefore finite.

Concavity of $\log$, or equivalently convexity of the exponential, gives


$$
\log\mathbb EP\ge\mathbb E\log P.
$$


Combining the inequalities,


$$
\boxed{
\log\mathbb E P
\ge
\mathbb E\sum_{i<j}\log g_{ij}
\ge
\mathbb E\frac{A^2}{B}
\ge
\frac{(\mathbb EA)^2}{\mathbb EB}.
}
\tag{5.8}
$$



The Jensen direction is correct.

### 5.5 Evaluation of the gain

Using the moments from Section 4,


$$
\begin{aligned}
\mathbb EA
&=k\,\mathbb ET_2-\mathbb ET_1^2\\
&=\boxed{km(k^2-1)}.
\end{aligned}
\tag{5.9}
$$



Likewise,


$$
\begin{aligned}
\mathbb EB
&=k\,\mathbb ET_4-\mathbb ET_2^2\\
&=\boxed{
km(k^2-1)(k^2+5km+4m^2+2).
}
\end{aligned}
\tag{5.10}
$$


For example, the polynomial inside the factor $km$, before factoring, is


$$
k^4+5k^3m+4k^2m^2+k^2-5km-4m^2-2,
$$


which equals


$$
(k^2-1)(k^2+5km+4m^2+2).
$$



Therefore


$$
\frac{(\mathbb EA)^2}{\mathbb EB}
=
\frac{km(k^2-1)}{k^2+5km+4m^2+2}.
\tag{5.11}
$$


Substituting $m=4k-1$,


$$
k^2+5km+4m^2+2=85k^2-37k+6,
$$


and hence


$$
\boxed{
R_k=
\frac{k(4k-1)(k^2-1)}{85k^2-37k+6}.
}
\tag{5.12}
$$



It is positive for $k\ge2$, and its leading quotient is $4k^2/85$.

At $k=1$, the relative product is empty and $\det D_1=B_1$. One may set $R_1=0$, but the intermediate division by $\mathbb EB$ must not be used at that endpoint.

**Spread/Jensen verdict: PASS, including integrability and finite endpoints.**

---

## 6. Same-$H$ consequence and conditional arithmetic threshold

### 6.1 Reuse of the audited base comparison

The base comparison is established reuse. Its exact hypotheses and objects are:

* $L=\mu-\delta_{-1}$, with the atom of mass $-1$ retained;
* $\mu$ is the pushforward of $e^{-t}\,dt$ under $x=(t-1)^2$;
* the complete compact measure has density
  

$$
\frac{e^{\sqrt x}+4/(1+x)}{2\sqrt x}\qquad(0<x<1);
$$


* for $Q_y(x)=\prod_{r=1}^k(x-y_r)$,
  

$$
M_y(i,j)=L(x^{i+j}Q_y(x));
$$


* for $k\ge512$,
  

$$
M_y\succeq D_k/32
  \qquad\text{for every }y\in[0,1]^k;
$$


* the exact signed conditional identity is
  

$$
(-1)^kH_k(e+\pi)
  =
  \frac{\Lambda_k^k}{k!}
  \int_{[0,1]^k}V(y)^2\det M_y\,d\nu^k(y).
$$



The complete overlap, the reference interval below $k$, and the atom payment are already included in that theorem. They are not re-audited here.

Since $d\nu/dx\ge3/2$, the new determinant estimate gives (1.3). The highest reference factorial remains


$$
(6k-4)!.
$$



### 6.2 The new $k^2$-constant

Reuse the established asymptotics


$$
\log B_k
=
4k^2\log k+
\left(17\log2-\frac92\log3-6\right)k^2
+O(k\log k),
$$




$$
\log\mathfrak h_k=-2(\log2)k^2+O(k\log k),
\qquad
\log\Lambda_k=6k+o(k).
$$


Together with $R_k=(4/85)k^2+O(k)$, they give (1.4).

This is a lower-bound constant. It is not a claim that the actual next asymptotic coefficient of $\log|H_k(e+\pi)|$ equals $C_H$.

### 6.3 Precisely conditional odd-content hypothesis

Define


$$
W_k^{\mathrm{odd}}
=
3^{2k}\Lambda_k^k
\left(\prod_{j=0}^{k-1}\operatorname{odd}(j!)\right)^4.
\tag{6.1}
$$


The conventional sufficient odd hypotheses are


$$
\operatorname{odd}(\mathscr L_k)\mid W_k^{\mathrm{odd}},
\qquad
\operatorname{odd}(\mathscr R_k)\mid W_k^{\mathrm{odd}}.
\tag{6.2}
$$



Their $3$-parts are now established by reuse. Their parts at every other odd prime remain unproved.

For an odd prime $p$, the allowance is


$$
B_p(k)=
k\bigl(2\mathbf1_{p=3}+v_p(\Lambda_k)\bigr)
+4\sum_{j=0}^{k-1}v_p(j!).
\tag{6.3}
$$


In particular, $B_p(k)=0$ when $p>6k-5$. Those primes remain part of the obligation.

Under (6.2), the all-prime interface yields


$$
\log G_k
\le
v_2(G_k)\log2+\log\Lambda_k+2\log W_k^{\mathrm{odd}}.
\tag{6.4}
$$


The paid height is


$$
\log W_k^{\mathrm{odd}}
=
2k^2\log k+(3-2\log2)k^2+o(k^2).
\tag{6.5}
$$



If, additionally and conditionally, at the same original indices


$$
v_2(G_k)\le Ak^2+o(k^2),
\tag{6.6}
$$


then


$$
\log G_k
\le
4k^2\log k+
(A\log2+6-4\log2)k^2+o(k^2).
\tag{6.7}
$$



Subtracting from (1.4),


$$
\boxed{
\log\ell_k
\ge
\left((19-A)\log2-\frac92\log3-\frac{506}{85}\right)k^2
+o(k^2).
}
\tag{6.8}
$$



The requested conventional threshold is therefore


$$
\boxed{
A<
A_*=
\frac{19\log2-\frac92\log3-\frac{506}{85}}{\log2}
\approx3.279390032756968.
}
\tag{6.9}
$$



For the research target $A=13/4$, the margin is


$$
\boxed{
\delta_{13/4}
=
\frac{63}{4}\log2-\frac92\log3-\frac{506}{85}
\approx0.020371618342057>0.
}
\tag{6.10}
$$



Thus $A=13/4$, **if actually proved for $G_k$** and combined with the remaining odd hypotheses, would force $\ell_k\to+\infty$.

### 6.4 Why the sum-of-contents route is unavailable

The established binary lower asymptotic for each separate content is $3k^2$. Hence


$$
v_2(\mathscr L_k)+v_2(\mathscr R_k)
\ge6k^2+o(k^2).
\tag{6.11}
$$


An upper bound for that sum with coefficient below $3.2794$ is impossible.

The relevant target is directly $v_2(G_k)$, not the sum in (6.11). The subsequent reduction respects this distinction.

### 6.5 A sharper conditional odd payment available from the exact ternary result

There is a useful additional consequence of the established ternary contents, without assuming equality in (2.18).

At $k=3^s$,


$$
B_3(k)=k^2+(2-s)k,
$$


and


$$
2(B_3(k)-E_k)=k^2+7k-2-4s.
\tag{6.12}
$$


Therefore, if the descent hypotheses are proved at the odd primes other than $3$, one can replace $W_k^{\mathrm{odd}}$ by the smaller integer


$$
W_{k,\mathrm{sharp}}^{\mathrm{odd}}
=
\frac{W_k^{\mathrm{odd}}}{3^{B_3(k)-E_k}}.
\tag{6.13}
$$


Then


$$
\operatorname{odd}(G_k)
\mid
\Lambda_k\bigl(W_{k,\mathrm{sharp}}^{\mathrm{odd}}\bigr)^2.
$$


This saves $(\log3)k^2+o(k^2)$ in the conditional upper height for $G_k$.

Accordingly, exact ternary reuse permits the larger conditional threshold


$$
A<A_*+\frac{\log3}{\log2}.
\tag{6.14}
$$


This observation does not prove any binary upper bound. The requested $13/4$ target is already sufficient under the more conservative threshold (6.9).

---

## 7. A newly evaluated source-specific dyadic forcing pivot

This section begins the second primary task.

The theorem below applies to every odd $k\ge9$, and therefore to every original index. It does not replace the original domain by those auxiliary indices.

Put


$$
d=k-1.
$$


Thus $d$ is even and $d\ge8$.

### 7.1 An integer row operator tailored to the complete returns

Define


$$
P_d(x)=\prod_{h=0}^{d-1}(2x+2h+1).
\tag{7.1}
$$


For a sequence $y$, define


$$
(\mathcal A_d y)_n
=
\sum_{i=0}^{d}
(-1)^i\binom di P_d(n+i)y_{n+i}.
\tag{7.2}
$$



For the original $2k=2d+2$ rows, apply this operator only to rows


$$
0\le n<d,
$$


and leave rows $d,\ldots,2d+1$ unchanged. Let the resulting square row matrix be $\mathcal S_d$.

It is upper triangular, with diagonal entries $P_d(n)$ for $n<d$, and $1$ thereafter. Thus


$$
\boxed{
\det\mathcal S_d=\Omega_k
:=\prod_{n=0}^{d-1}P_d(n),
\qquad \Omega_k\text{ is odd}.
}
\tag{7.3}
$$


It is not silently treated as unimodular over $\mathbb Z$; the exact factor $\Omega_k$ will be paid.

The largest row used in a transformed row is


$$
(d-1)+d=2d-1<2d+2.
$$


No new row is introduced.

### 7.2 Exact annihilation of the rational return channel

For every $0\le j<d$,


$$
\frac{P_d(n+i)}{2(n+i+j)+1}
=
\prod_{\substack{0\le h<d\\h\ne j}}
(2(n+i+h)+1)
$$


is a polynomial of degree $d-1$ in $i$. Its $d$-th finite difference vanishes. Consequently,


$$
\boxed{
\sum_{i=0}^d
(-1)^i\binom di
\frac{P_d(n+i)}{2(n+i+j)+1}=0.
}
\tag{7.4}
$$



Apply this to the **complete** return (2.6). Since


$$
(2t+2)!+(2t)!
=
\bigl(4t^2+6t+3\bigr)(2t)!,
$$


put


$$
b(t)=4t^2+6t+3,
$$


which is odd for every integer $t$. Then


$$
\boxed{
(\mathcal A_d T_{\bullet+j})_n
=
-\Lambda_k
\sum_{i=0}^d
(-1)^i\binom di
P_d(n+i)b(n+i+j)(2(n+i+j))!.
}
\tag{7.5}
$$



Thus the rational forcing has been canceled by an exact integer row identity. Neither factorial term has been dropped.

### 7.3 Exact valuation of every transformed forcing entry

In the sum in (7.5), the $i=0$ term has valuation


$$
v_2((2(n+j))!),
$$


because $P_d(n)b(n+j)$ is odd.

Every $i\ge1$ term has strictly larger valuation: the factorial ratio


$$
\frac{(2(n+i+j))!}{(2(n+j))!}
$$


is even. Therefore


$$
\boxed{
v_2\bigl((\mathcal A_d T_{\bullet+j})_n\bigr)
=
v_2((2(n+j))!).
}
\tag{7.6}
$$



This is already an evaluated complete-source identity, not merely a lower divisor.

### 7.4 A factorial-normalized forcing matrix is a dyadic unit

Let $F_k$ be the $d\times d$ matrix of these transformed common return entries:


$$
F_k(n,j)=(\mathcal A_d T_{\bullet+j})_n,
\qquad 0\le n,j<d.
\tag{7.7}
$$


Define


$$
D_f=\operatorname{diag}((2n)!)_{0\le n<d}
$$


and the integer matrix


$$
K_d(n,j)=
\sum_{i=0}^d
(-1)^i\binom di P_d(n+i)b(n+i+j)
\frac{(2(n+i+j))!}{(2n)!(2j)!}.
\tag{7.8}
$$


Every summand is integral, since


$$
\frac{(2(n+i+j))!}{(2n)!(2j)!}
=
\frac{(2(n+i))!}{(2n)!}
\binom{2(n+i+j)}{2j}.
$$


Thus


$$
\boxed{F_k=-\Lambda_kD_fK_dD_f.}
\tag{7.9}
$$



Modulo $2$, all terms with $i\ge1$ vanish. The $i=0$ term gives


$$
K_d(n,j)\equiv
\binom{2(n+j)}{2j}
\equiv
\binom{n+j}{j}\pmod2.
\tag{7.10}
$$


The latter matrix has determinant $1$: over the integers,


$$
\binom{n+j}{j}
=
\sum_h\binom nh\binom jh,
$$


so it is the product of a unit lower-triangular Pascal matrix and its transpose.

Hence


$$
\boxed{
\eta_d:=\det K_d\equiv1\pmod2.
}
\tag{7.11}
$$


In particular, $F_k\ne0$, and its exact determinant is


$$
f_k:=\det F_k
=
(-\Lambda_k)^d\eta_d
\left(\prod_{n=0}^{d-1}(2n)!\right)^2.
\tag{7.12}
$$


Therefore


$$
\boxed{
v_2(f_k)
=
V_d:=2\sum_{n=0}^{d-1}v_2((2n)!).
}
\tag{7.13}
$$



The full forcing pivot has now been evaluated at $2$. The unknown odd integer $\eta_d$ is retained in every all-prime identity below.

---

## 8. Literal atom evaluation and the paid simultaneous reduction of $H_0,H_1$

### 8.1 Contact divisibility under the same row operator

The established finite-difference divisibilities are


$$
2^r r!\mid\Delta^r u_n,
\qquad
2^{r+1}r!\mid\Delta^r\sigma_n.
\tag{8.1}
$$


They hold for the original sequences and all nonnegative $n,r$.

For clarity, they follow from


$$
u_n=\int_0^\infty e^{-t}(t-1)^{2n}\,dt
$$


and


$$
\Delta^r u_n
=
\int_0^\infty
e^{-t}(t-1)^{2n}t^r(t-2)^r\,dt.
$$


The factorial quotient appearing after expansion contains


$$
\frac{\binom rh2^{r-h}(r+h)!}{2^rr!}
=
\binom{r+h}{2h}(2h-1)!!\in\mathbb Z.
$$


The assertion for $\sigma$ follows from $\sigma=2u+\Delta u$.

For $0\le h\le d$,


$$
\Delta^hP_d(n)
=
2^h\frac{d!}{(d-h)!}
\prod_{r=h}^{d-1}(2n+2r+1).
\tag{8.2}
$$


The finite-difference product rule, together with (8.1), therefore gives


$$
\boxed{
2^dd!\mid(\mathcal A_d u_{\bullet+j})_n,
\qquad
2^{d+1}d!\mid(\mathcal A_d\sigma_{\bullet+j})_n.
}
\tag{8.3}
$$



Let


$$
\alpha_d=v_2((2d)!).
$$


Since


$$
(2d)!=2^dd!(2d-1)!!,
$$


the two valuations in (8.3) are at least $\alpha_d$ and $\alpha_d+1$, respectively.

### 8.2 Exact evaluation of the contact atom

For $w_n=(-1)^n$,


$$
(\mathcal A_dw)_n
=
(-1)^n\sum_{i=0}^d\binom diP_d(n+i).
$$


Using the shift operator $E=1+\Delta$,


$$
\sum_{i=0}^d\binom diP_d(n+i)
=(1+E)^dP_d(n)
=(2+\Delta)^dP_d(n).
$$


Substituting (8.2),


$$
(\mathcal A_dw)_n
=
(-1)^n2^d U_d(n),
\tag{8.4}
$$


where


$$
U_d(n)=
\sum_{h=0}^d
\binom dh\frac{d!}{(d-h)!}
\prod_{r=h}^{d-1}(2n+2r+1).
\tag{8.5}
$$



This expression has an evaluated parity. Its $h=0$ term is odd. Every $h\ge1$ term contains the even factor $d$. Hence


$$
\boxed{U_d(n)\equiv1\pmod2.}
\tag{8.6}
$$


Consequently,


$$
\boxed{
v_2((\mathcal A_dw)_n)=d.
}
\tag{8.7}
$$



Since $d\ge2$, $v_2(d!)\ge1$. Equations (8.3) and $c=u-w$ now give


$$
\boxed{
v_2((\mathcal A_dc)_n)=d.
}
\tag{8.8}
$$



Thus the literal atom dominates the transformed first contact column at this dyadic scale. Replacing $c$ by $u$ would be mathematically incorrect: it would erase the exact valuation in (8.8).

### 8.3 The complete common-column form of $H_k(s)$

Make determinant-one adjacent-column transformations in both original column groups:


$$
(c_0,\ldots,c_{k-1})
\longmapsto(c_0,\sigma_0,\ldots,\sigma_{d-1}),
$$




$$
(r_0+sw,\ldots,r_{k-1}+s(-1)^{k-1}w)
\longmapsto(r_0+sw,\tau_0,\ldots,\tau_{d-1}).
$$


Here each displayed column is understood with the original row shifts.

The parameter cancels in the $d$ return columns. Define


$$
\mathcal T=(T_{m+j})_{\substack{0\le m<2d+2\\0\le j<d}},
$$


and


$$
\mathcal M(s)
=
\left[
(c_m)\
\middle|\
(\sigma_{m+j})_{j<d}\
\middle|\
\Lambda_k(r_m+sw_m)
\right]_{m<2d+2}.
\tag{8.9}
$$



Moving the $d$ return columns to the front has sign


$$
(-1)^{d(d+2)}=1,
$$


because $d$ is even. Therefore


$$
\boxed{H_k(s)=\det[\mathcal T\mid\mathcal M(s)].}
\tag{8.10}
$$



All $k$ original right columns are still present: $d$ common return columns and the complete remaining border column.

Apply $\mathcal S_d$ and partition after the first $d$ rows:


$$
\mathcal S_d[\mathcal T\mid\mathcal M(s)]
=
\begin{pmatrix}
F_k&A_0+sA_1\\
B&C_0+sC_1
\end{pmatrix}.
\tag{8.11}
$$


The lower block has $d+2=k+1$ rows.

Only the last column of $A_1,C_1$ is nonzero. Its entries are the transformed and untransformed copies of $\Lambda_kw$. The constant border retains the complete $\Lambda_kr$.

### 8.4 An explicit integer clearer for the Schur correction

Put


$$
h_d=(2d-2)!,
\qquad
\beta_d=v_2(h_d),
$$




$$
\widehat D_f=h_dD_f^{-1}.
$$


This is an integer diagonal matrix.

Define


$$
N_d=\widehat D_f\,\operatorname{adj}(K_d)\,\widehat D_f,
\qquad
\delta_k=\Lambda_k\eta_d h_d^2.
\tag{8.12}
$$


Then $N_d$ is integral and


$$
\boxed{F_k^{-1}=-\frac{N_d}{\delta_k}.}
\tag{8.13}
$$


Every denominator is displayed. In particular,


$$
v_2(\delta_k)=2\beta_d,
$$


while the odd factors $\Lambda_k\eta_d$ remain in the exact formula.

Set


$$
E_i=\delta_k C_i+BN_dA_i,\qquad i=0,1.
\tag{8.14}
$$


These are integer matrices. The Schur determinant identity gives


$$
\boxed{
\delta_k^{\,k+1}\Omega_k H_k(s)
=
f_k\det(E_0+sE_1).
}
\tag{8.15}
$$



This is a simultaneous identity for the complete constant and linear coefficients, not two unrelated minor estimates.

### 8.5 Further proved integer column divisions

The bottom rows in (8.11) have indices $m\ge d\ge8$. Hence:

* every entry of $B$ is divisible by $4$;
* the bottom contact entries $c_m,\sigma_{m+j}$ are even;
* the constant bottom border $\Lambda_kr_m$ is divisible by $4$.

The top first contact column is divisible by $2^d$, by (8.8). Each top $\sigma$-column is divisible by $2^{\alpha_d+1}$, by (8.3).

For $d\ge8$,


$$
\alpha_d=\beta_d+1+v_2(d),
\qquad
\beta_d\ge v_2(d)+3,
$$


so


$$
2\beta_d+1\ge\alpha_d+3.
\tag{8.16}
$$


It follows from (8.14) that the following divisions are integral:

* divide the first contact column by $2^{d+2}$;
* divide each of the $d$ $\sigma$-columns by $2^{\alpha_d+3}$;
* divide the last, affine border column by $4$.

Apply these same divisions to the pencil $E_0+sE_1$, and denote the resulting integer pencil by


$$
\widehat E_k(s).
$$


Its determinant is affine:


$$
\det\widehat E_k(s)=J_{0,k}+J_{1,k}s.
\tag{8.17}
$$



The total paid binary column factor is


$$
\boxed{
\lambda_d
=(d+2)+d(\alpha_d+3)+2
=d\alpha_d+4d+4.
}
\tag{8.18}
$$


Thus


$$
\boxed{
\delta_k^{\,k+1}\Omega_k H_{i,k}
=
f_k\,2^{\lambda_d}J_{i,k},
\qquad i=0,1.
}
\tag{8.19}
$$



No division by a nonunit has been declared free.

### 8.6 Exact all-prime and binary gcd identities

Let


$$
g_k^\sharp=\gcd(|J_{0,k}|,|J_{1,k}|).
$$


Taking gcds in (8.19) gives the exact all-prime identity


$$
\boxed{
|\delta_k|^{\,k+1}\Omega_k G_k
=
|f_k|\,2^{\lambda_d}g_k^\sharp.
}
\tag{8.20}
$$


The odd factors in $\Omega_k,\eta_d,\Lambda_k$, and the factorials have not been discarded.

At $2$, this becomes


$$
\boxed{
v_2(G_k)
=
\kappa_k+v_2(g_k^\sharp),
\qquad
\kappa_k=V_d+\lambda_d-2(k+1)\beta_d.
}
\tag{8.21}
$$



The known offset is only lower order:


$$
\kappa_k=O(k\log k).
\tag{8.22}
$$


Indeed, writing $s_2(n)$ for binary digit sum,


$$
V_d=2d(d-1)-2\sum_{n=0}^{d-1}s_2(n),
$$


and


$$
\beta_d=2d-2-s_2(d-1).
$$



There is a further exact simplification on the **original** domain. Since


$$
k=81^{\,9+16u},
$$


the binomial theorem shows


$$
v_2(k-1)=4.
\tag{8.23}
$$


Thus $v_2(d)=4$, $s_2(d-1)=s_2(d)+3$, and


$$
\boxed{
\kappa_k
=
4d+24+(d+4)s_2(d)
-2\sum_{n=0}^{d-1}s_2(n),
\qquad d=k-1,\quad k\in\mathcal K.
}
\tag{8.24}
$$



This is an explicitly evaluated payment, not an unspecified determinant valuation.

### 8.7 Precise unpaid binary term and follow-on lemma

The remaining binary term is exactly


$$
\boxed{
v_2(g_k^\sharp)
=
\min\bigl(v_2(J_{0,k}),v_2(J_{1,k})\bigr),
}
\tag{8.25}
$$


for the complete corrected integer pencil defined in (8.9)–(8.18).

A concrete sufficient next lemma is:

> **Paid reduced paired-valuation lemma — open.**  
> On an eventual tail of
> 

$$
> k=9^{18+32u},
>
$$


> the explicitly defined pair $J_{0,k},J_{1,k}$ satisfies
> 

$$
> \min\bigl(v_2(J_{0,k}),v_2(J_{1,k})\bigr)
> \le
> \frac{13}{4}k^2+O(k\log k).
> \tag{8.26}
>
$$



Together with (8.21)–(8.24), this would prove the desired direct bound for $v_2(G_k)$.

What has been newly evaluated is the complete forcing pivot, its exact factorial normalization, the transformed literal atom, and every transfer payment. What remains open is the joint binary depth of the corrected residual pair.

The fact that $K_d$ is a dyadic unit does **not** make the residual pair a unit. The factorial diagonal divisions and the interaction of the remaining contact and border columns can create substantial common binary depth. That is the precise obstruction to promoting this reduction into the requested upper bound.

### 8.8 Boundary audit for the new reduction

Every entry remains within the original physical arrays.

* Transformed rows use only indices through $2d-1<2k$.
* All bottom rows, including the original last row $2k-1=2d+1$, remain.
* The largest return index is
  

$$
(2d+1)+(d-1)=3d=3k-3.
$$


* Its successor moment is $3k-2$, with factorial $(6k-4)!$.
* All $d$ common return columns and the complete remaining right border are retained.
* The rational forcing is canceled only by the exact identity (7.4), not by a truncation.
* The atom is retained and explicitly detected by (8.8).

---

## 9. What the new binary result does—and does not—establish

The evaluated pivot is a genuine source-specific advance:

1. The row operator is determined by the actual odd denominators in the original return columns.
2. Its determinant is explicitly odd, with its full integer value $\Omega_k$ paid.
3. The complete forcing matrix, including both factorial terms, becomes factorial-normalized Pascal data modulo $2$.
4. Its determinant valuation is evaluated exactly, rather than bounded by a generic matrix-size estimate.
5. The actual atom produces the exact valuation $d$, preventing an invalid replacement of $c$ by $u$.
6. Both $H_0$ and $H_1$ pass through one common reduction and one exact gcd identity.

Nevertheless, the reduction does not prove (8.26). In particular:

* it supplies no upper bound for the uncapped residual binary content;
* it does not transfer the ternary unit argument to $2$;
* it does not bound $v_2(\mathscr L_k)+v_2(\mathscr R_k)$ by an impossible coefficient;
* it does not exclude other odd primes in $G_k$;
* it does not determine the actual primitive denominator.

The primitive pair is still the original pair divided by $G_k$. Indeed, (8.19) shows that the two coefficient pairs are rational scalar multiples, and (8.20) pays that scalar exactly. Thus, after their respective full gcds are removed,


$$
\frac{|J_{1,k}|}{g_k^\sharp}
=
\frac{|H_{1,k}|}{G_k},
\qquad
\frac{|J_{0,k}+J_{1,k}(e+\pi)|}{g_k^\sharp}
=
\frac{|H_k(e+\pi)|}{G_k}.
\tag{9.1}
$$


This is an identity of primitive normalization, not an evaluation of $g_k^\sharp$.

---

## 10. Other established payments and distinct producers

No finite-jet or contact-frame transfer is used to claim an arithmetic shortcut.

If those alternative compact representations are used, their actual corrections remain


$$
\mathscr R_k
=
\frac{\Lambda_k^{k-1}\mathscr C_{Z,k}\zeta_{Z,k}}{t_Z},
\qquad
\mathscr L_k
=
\frac{\Lambda_k^{k-1}\mathscr C_{Y,k}\chi_{Y,k}}{t_Y},
\tag{10.1}
$$


with


$$
t_Z=\prod_{m=0}^{2k-1}(2m+1)_{2k-3},
\qquad
t_Y=\prod_{m=0}^{2k-2}(2m+1)_{2k-1}.
$$


The actual cofactor-dependent factor $\zeta_{Z,k}$ and actual minor-type correction $\chi_{Y,k}$ are not assigned the value $1$. Their contents remain the actual contents of the stated transformed arrays, not substitutes for $\mathscr L_k,\mathscr R_k$.

Likewise, the separate binary producer is not altered. Its data remain


$$
b=9^{18+32u},\qquad n=4002b,
$$


with contact indices $0,\ldots,b-1$, physical reconstruction indices $0,\ldots,b$, and $z_b=0$. Its complete corrected columns remain


$$
x=\frac12RA^{-1}f,
\qquad
y=\frac{RA^{-1}(h^e+h^F)+e_0}{4b!},
\qquad x=2^ax_0,
$$


and its complete return is


$$
S=\sum_{j<b}(n+1-j)\binom{n+2}{j}z_j^f.
$$


Only the established paid statement


$$
v_2\!\left(\frac{S}{2^{a+1}}\right)\ge\chi-a,
\qquad
\chi=v_2\binom{n+b-1}{b-1},
$$


is retained. Its norm $x_0^Tx_0$, corrected-column contents, actual least simultaneous clearer, actual primitive denominator, and final all-prime gcd remain separate.

---

## 11. Numerical precision and finite arithmetic scope

### 11.1 Exact brackets for the new constants

Reuse the already certified rational logarithm bounds


$$
\frac{69\,314\,718\,055\,994}{10^{14}}
<\log2<
\frac{69\,314\,718\,055\,995}{10^{14}},
$$




$$
\frac{109\,861\,228\,866\,810}{10^{14}}
<\log3<
\frac{109\,861\,228\,866\,812}{10^{14}}.
\tag{11.1}
$$


They imply


$$
\boxed{
5.50051123292197<C_H<5.50051123292222,
}
\tag{11.2}
$$


and


$$
\boxed{
0.0203716183419<\delta_{13/4}<0.0203716183422.
}
\tag{11.3}
$$



For the threshold, let


$$
a_-=3.27939003275,\qquad a_+=3.27939003277.
$$


Using the lower $\log2$ and upper $\log3$ bounds, the numerator of


$$
(19-a_-)\log2-\frac92\log3-\frac{506}{85}
$$


after multiplication by $170\cdot10^{25}$ is bounded below by


$$
\boxed{7\,989\,940\,105\,340\,500>0.}
\tag{11.4}
$$


Using the opposite logarithm bounds for $a_+$, the corresponding upper numerator is


$$
\boxed{-15\,156\,813\,664\,254\,550<0.}
\tag{11.5}
$$


Thus


$$
\boxed{
3.27939003275<A_*<3.27939003277.
}
\tag{11.6}
$$



These are bounded rational cross-multiplications, not content calculations.

### 11.2 Existing receipts are not rerun

The following are reused only at their established scopes:

* the original reference-Gram audit;
* the exact ternary-content theorem and its different audit;
* the supplied order-two/order-four Wishart receipt;
* the $k=2,3,4$ polynomial-integral corroborations;
* the finite $k=32,33$ final-gcd data.

No $2!$ or $4!$ enumeration, Laguerre polynomial integral, original determinant scan, adjacent scan, or capped Smith calculation is repeated.

The finite values


$$
v_2(G_{32})=3375,\qquad v_2(G_{33})=3602
$$


do not prove an asymptotic at $\mathcal K$. Nor does the finite contraction of approximation errors control the whole primitive error when the primitive denominators grow dramatically.

### 11.3 Bounded arithmetic needed for checking this report

No further matrix computation is needed for either the Jensen proof or the evaluated forcing-pivot theorem.

The only small exact arithmetic needed to inspect the displayed new decimal cutoffs is:

* **Inputs:** the four rational logarithm bounds in (11.1), $4/85$, $13/4$, and the two decimal rationals $a_-,a_+$.
* **Expected outputs:** the brackets (11.2), (11.3), (11.6), and the signed residuals (11.4), (11.5).
* **Scope:** certification of constants only.

I do not propose a new finite gcd scan as a substitute for the uniform unpaid lemma (8.26).

---

## 12. Proof-status ledger

| Statement | Status and scope |
|---|---|
| Earlier same-$H$ reference comparison | **Established reuse**, $k\ge512$ |
| Exact same-$D$ relative Laguerre factor | **Audited and proved** |
| Complex Wishart normalization with $k$ rows, $m=4k-1$ columns | **PASS**, unscaled variance-one convention |
| Order-two/order-four trace formulas | **Uniformly derived**, without rerunning permutation enumeration |
| Pairwise logarithmic inequality | **Proved** |
| Both Cauchy–Schwarz steps | **Proved**, with denominators and integrability checked |
| Jensen direction and finite endpoints | **PASS** |
| Exact $R_k$ and gain $4/85$ | **Proved** |
| New same-$H$ lower constant $C_H$ | **Proved lower-bound constant** |
| Conditional retirement threshold $A_*$ | **Proved conditional implication** |
| Exact ternary contents of $\mathscr L_k,\mathscr R_k$ | **Established reuse**, not reproved |
| Equality for $v_3(G_k)$ | **Not asserted**; only the retained range is available |
| Complete-source dyadic forcing annihilator | **New proved identity** |
| Exact binary valuation of its forcing pivot | **New evaluated theorem** |
| Exact transformed atom valuation | **New evaluated theorem** |
| Simultaneous paid reduction of $H_0,H_1$ and final gcd | **New proved identity** |
| Direct $v_2(G_k)\le(13/4)k^2+o(k^2)$ | **Open** |
| Other odd-content descents, including primes $>6k-5$ | **Open** |
| Actual primitive whole-error decay or divergence | **Not established unconditionally** |
| Rationality or irrationality of $e+\pi$ | **Unresolved** |

## Final conclusion

The complete new Laguerre spread/Jensen candidate passes the independent proof audit. It yields the unconditional same-$H$ lower bound


$$
\boxed{
\log |H_k(e+\pi)|
\ge
4k^2\log k+
\left(15\log2-\frac92\log3+\frac4{85}\right)k^2
+o(k^2),
}
$$


with the original factorial $(6k-4)!$, complete measures, forcing terms, contact atom, and original index set retained.

The new arithmetic result is an evaluated source-specific dyadic elimination. Its complete forcing pivot has exact valuation


$$
2\sum_{n=0}^{k-2}v_2((2n)!),
$$


and the same operator detects the literal atom with exact valuation $k-1$. After every factorial, scalar, row, and column payment, it gives


$$
\boxed{
v_2(G_k)=\kappa_k+
\min\bigl(v_2(J_{0,k}),v_2(J_{1,k})\bigr),
\qquad
\kappa_k=O(k\log k),
}
$$


for a fully specified corrected integer pencil using the original complete columns.

The exact remaining binary bottleneck is the uniform paired upper bound (8.26). The other odd-prime descents remain separate obligations. Even after those are settled, the conclusion must be drawn for the actual primitive denominator $|H_{1,k}|/G_k$ and the nonzero whole error $|H_k(e+\pi)|/G_k$ at the same infinite original indices.

No unconditional rationality or irrationality conclusion for $e+\pi$ has been obtained.
