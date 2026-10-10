> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2, Turn 4 — An exact endpoint current and an actual all-depth obstruction to integral contact lifting

## Executive summary

I do **not** obtain the requested all-depth relative alignment


$$
v_{29}(M-\rho_nD)\ge v_{29}(D)+1,
\qquad \rho_n=(6C_n)^{-1}.
$$


Nor do I disprove that scalar statement.

I obtain two exact results for the **actual finite reconstruction with the complete force**.

1. **An explicit integral finite-boundary current removes the component forced by the exterior $+1$ in the direction normal to the reconstruction image.** Its scalar coefficient is known independently of $D$. The construction retains the first and last high-block currents and the shorter final block.

2. **Pulling the resulting orthogonal projection back through the actual contact reconstruction can lose arbitrarily many $29$-adic digits at original indices inside the preferred cylinder.** This is not an abstract isotropic-vector example. It is caused by the actual factorial reconstruction lattice and the actual exterior $+1$; the complete exponential and logarithmic force cannot cancel the exhibited negative valuation.

More precisely, put


$$
B=410910916=687936+20\cdot29^5.
$$


On originally reachable refinements satisfying


$$
k=v_{29}(b-B)\ge9,
$$


an explicitly determined contact-lift correction has valuation


$$
\boxed{14675394-k}
$$


at the actual coordinate


$$
j=b-B-1.
$$


For $k>14675394$, the lift of the **complete projected $Q$-column** has exactly that negative valuation. Thus an integral contact-operator ansatz for this projected column fails by an unbounded, explicitly quantified amount.

This does **not** contradict the possibility of a skew-adjoint identity on the **weighted, saturated reconstruction space**. I give a concrete force-side identity which would produce such a skew-adjoint reconstruction and, consequently, the desired all-depth current. That identity remains unproved.

No tools were executed. The initializer and the pending higher-tail compression are not rerun or used to assert original units.

**The irrationality or rationality of $e+\pi$ remains unresolved.**

---

## 1. Domain, exact reconstruction, and scope of the inputs

Throughout,


$$
p=29,\qquad L=p^4=707281,
$$




$$
a=432827+682892t,\qquad t\ge0,\qquad b=3^a,\qquad n=2001b.
$$


The actual weighted coordinates are


$$
0\le j\le b,
$$


and the finite contact system has indices


$$
0\le i,j<b.
$$



The preferred cylinder is


$$
t\equiv364\pmod{841}.
\tag{1.1}
$$


There,


$$
b=687936+p^5H,\qquad H\equiv20\pmod p.
\tag{1.2}
$$



Write


$$
W_j=\binom{n+2}{j},\qquad
\omega_j=j!W_j=(n+2)_{\underline j}.
$$


The normalized columns and scalar products remain


$$
P=Z_w/p^2,\qquad Q=Y/p^3,\qquad Y=V_w/b!,
$$




$$
D=P^TP,\qquad M=P^TQ.
$$



### 1.1 The full finite reconstruction used here

Let $S$ be the upper shift on the actual $b$-dimensional contact space, and put


$$
U=(I+S)^{-n}.
$$


Because $S^b=0$, this is an exact finite matrix.

Let $\widetilde N$ be the actual finite contact matrix, let $f^0$ be the complete $P$-force, and let


$$
\mathbf r=
\frac{
h^e+h^F-\widetilde N(I+S)^n(j!)_{0\le j<b}
}{b!}.
\tag{1.3}
$$


Thus $\mathbf r$ includes the complete exponential residual, factorial boundary subtraction, and logarithmic force.

The exact divided contact coefficients are


$$
\theta=U\widetilde N^{-1}f^0,
\qquad
\psi=U\widetilde N^{-1}\mathbf r.
\tag{1.4}
$$


With


$$
\theta_{-1}=\theta_b=\psi_{-1}=\psi_b=0,
$$


the reconstruction is


$$
\boxed{
Z_{w,j}=W_j(j\theta_{j-1}-\theta_j),
}
\tag{1.5}
$$




$$
\boxed{
Y_j=W_j(j\psi_{j-1}-\psi_j)+W_b\,\mathbf1_{j=b}.
}
\tag{1.6}
$$



In particular,


$$
Z_{w,b}=W_b\,b\theta_{b-1},
\qquad
Y_b=W_b(1+b\psi_{b-1}).
\tag{1.7}
$$


The exterior $+1$ is present throughout the argument.

The complete exponential part of (1.3) is, in the source notation,


$$
\mathbf r_i^e
=
\frac1{b!}
\sum_{s=0}^{\min(2n,n+i)}
\alpha_s(n,i)
\sum_{q=b}^{2n+i-s}(2n+i-s)_{\underline q},
\tag{1.8}
$$


where


$$
\alpha_s(n,i)=[z^s](1-z+z^2/2)^n\,(n+i)_{\underline s}.
$$


Empty inner sums are zero. The logarithmic contribution is exactly $h_i^F/b!$, not a truncated or deleted substitute.

The supplied complete-tail result proves


$$
\mathbf r\in\mathbb Z_p^b.
$$


The integral contact strengthening gives


$$
\widetilde N=B(n)+nC,\qquad C\in M_b(\mathbb Z),
$$


and $p\mid n$, while $B(n)$ has determinant one. Hence


$$
\widetilde N^{-1},\,U\in M_b(\mathbb Z_p).
$$


At the retained complete-force scope,


$$
\theta,\psi\in\mathbb Z_p^b.
\tag{1.9}
$$



No fixed-precision cutoff such as $117$, $88$, or $59$ is promoted to an all-depth cutoff here. Equation (1.3) is the full force.

### 1.2 What is and is not reused

The accepted absolute-precision conclusions


$$
D\equiv5C_n^2\mathcal T\pmod{p^4},
\qquad
M-\rho_nD\equiv0\pmod{p^4}
\tag{1.10}
$$


retain their stated scope. They do not establish a relative valuation at deeper norm zeros.

The new higher-tail scalar is pending independent audit and is not needed below. The conditional shifted-class calculations are not invoked. The earlier $p=23$ branch is not reopened.

---

## 2. The actual reconstruction image has an exactly evaluable normal vector

Define


$$
\ell_j=\frac{\omega_b}{\omega_j}
      =\frac{(n+2-j)!}{(n+2-b)!},
\qquad 0\le j\le b.
\tag{2.1}
$$


These are positive integers, and


$$
\ell_b=1.
$$



Equivalently, writing


$$
c=2000b+3=n+3-b,
$$


one has


$$
\ell_{b-r}=(c)^{\overline r},
\qquad 0\le r\le b.
\tag{2.2}
$$



### Proposition 1 — the exact affine charge

For the complete actual columns,


$$
\boxed{\ell^TZ_w=0,\qquad \ell^TY=W_b.}
\tag{2.3}
$$



#### Proof

Since $\ell_jW_j=\omega_b/j!$, equation (1.5) gives


$$
\ell_jZ_{w,j}
=
\omega_b\left(
\frac{\theta_{j-1}}{(j-1)!}-\frac{\theta_j}{j!}
\right),
\tag{2.4}
$$


where the first term is zero at $j=0$ and the second is zero at $j=b$.

Summing over the actual range $0\le j\le b$ telescopes to zero. The homogeneous part of (1.6) telescopes in the same way. Its exterior term contributes exactly


$$
\ell_bW_b=W_b.
$$


This proves (2.3). ∎

This identifies a genuine obstruction to a homogeneous reconstruction ansatz: $Y$ is not in the linear reconstruction image. No manipulation of the complete interior force changes that fact.

### 2.1 The normal norm is a $29$-adic unit

Put


$$
\mathscr S=\ell^T\ell
=\sum_{r=0}^{b}\bigl((2000b+3)^{\overline r}\bigr)^2.
\tag{2.5}
$$



On the original domain,


$$
b\equiv27\pmod{29},\qquad n\equiv0\pmod{29},
$$


so


$$
2000b+3\equiv5\pmod{29}.
$$


Every term with $r\ge25$ contains a factor $29$. Therefore


$$
\mathscr S\equiv
\sum_{r=0}^{24}\bigl(5^{\overline r}\bigr)^2
\pmod{29}.
\tag{2.6}
$$



The rising-factorial residues are


$$
\begin{aligned}
(5^{\overline r})_{r=0}^{24}\equiv
(&1,5,1,7,27,11,23,21,20,28,15,22,4,\\
 &10,6,27,18,1,22,13,22,28,3,23,6).
\end{aligned}
$$


Their squares sum to $8$ modulo $29$. Hence


$$
\boxed{\mathscr S\equiv8\pmod{29}.}
\tag{2.7}
$$



This is an evaluation of an actual finite-boundary quantity. Its validity for all original indices follows because all terms after the displayed finite range vanish modulo $29$, not because of sampling.

Consequently


$$
\Pi=I-\frac{\ell\ell^T}{\mathscr S}
\tag{2.8}
$$


is an integral, self-adjoint idempotent over $\mathbb Z_p$. It projects onto the saturated submodule


$$
\ell^\perp\subset\mathbb Z_p^{b+1}.
$$



---

## 3. An exact integral current for the exterior normal component

Define


$$
Y^\parallel
=
Y-\frac{W_b}{\mathscr S}\ell,
\qquad
Q^\parallel
=
Q-\gamma\ell,
\qquad
\gamma=\frac{W_b}{p^3\mathscr S}.
\tag{3.1}
$$


Then


$$
\ell^TY^\parallel=0.
$$



The source’s fixed low borrows for $W_b$, equivalently the low digits


$$
b=(27,28,5,28)_{29}\pmod{29^4},
\qquad
n+2=(2,7,24,7)_{29}\pmod{29^4},
$$


give


$$
v_p(W_b)\ge3.
\tag{3.2}
$$


Thus $\gamma\in\mathbb Z_p$, and $Q^\parallel$ is integral.

By Proposition 1,


$$
\boxed{
P^TQ^\parallel=M,\qquad P^TP=D.
}
\tag{3.3}
$$


The scalar mixed product is unchanged exactly.

### 3.1 The current is explicit, not a cumulative definition of the defect

For $1\le k\le b$, put


$$
\mathfrak c_k
=
-\frac{\omega_b}{p^2}\,
\frac{\theta_{k-1}}{(k-1)!},
\qquad
\mathfrak c_0=\mathfrak c_{b+1}=0.
\tag{3.4}
$$


Then (2.4) gives the coordinate identity


$$
\boxed{
P_j\ell_j=\mathfrak c_{j+1}-\mathfrak c_j.
}
\tag{3.5}
$$



Moreover,


$$
\mathfrak c_k
=
-\frac{W_b}{p^2}\frac{b!}{(k-1)!}\theta_{k-1}
\in p\mathbb Z_p,
\tag{3.6}
$$


using (1.9) and (3.2).

It follows that


$$
\boxed{
P_j(Q_j-\rho_nP_j)
=
P_j(Q^\parallel_j-\rho_nP_j)
+\gamma(\mathfrak c_{j+1}-\mathfrak c_j).
}
\tag{3.7}
$$


The current coefficient $\gamma$ is determined independently of $D$.

### 3.2 First and last high-block currents

Retain


$$
b=687936+Lh.
$$


For $0\le J<h$, the block is


$$
LJ\le j\le L(J+1)-1,
$$


while the last block is


$$
Lh\le j\le b.
$$



Let


$$
e_J=\sum_{j\text{ in block }J}P_j(Q_j-\rho_nP_j),
$$


and define $e_J^\parallel$ with $Q^\parallel$ in place of $Q$.

Set


$$
\mathcal B_J=\gamma\mathfrak c_{LJ}
\quad(0\le J\le h),
\qquad
\mathcal B_{h+1}=\gamma\mathfrak c_{b+1}=0.
$$


Then


$$
\boxed{
e_J=e_J^\parallel+\mathcal B_{J+1}-\mathcal B_J,
\qquad 0\le J\le h,
}
\tag{3.8}
$$


and


$$
\boxed{\mathcal B_0=\mathcal B_{h+1}=0.}
\tag{3.9}
$$



There is no extension of the last block to length $L$. Both genuine exterior currents vanish.

### What this current accomplishes

It removes exactly the normal component dictated by the exterior $+1$, while retaining the full actual force in $Q^\parallel$.

It is **not yet** the desired relation


$$
e_J=\alpha_nd_J+\text{current difference}.
$$


The unresolved term is $e_J^\parallel$.

The projection and telescoping principles are standard. The actual arithmetic contributions here are the unit evaluation $\mathscr S\equiv8$, the integral current at the supplied normalization, and the contact-lattice obstruction proved next.

---

## 4. Exact contact lift of the projected exterior term

Write


$$
E=W_be_b-\frac{W_b}{\mathscr S}\ell.
\tag{4.1}
$$


This vector has zero charge and is the part added to the homogeneous reconstruction when $Y$ is replaced by $Y^\parallel$.

Let


$$
\mathscr S_j=\sum_{i=0}^{j}\ell_i^2.
\tag{4.2}
$$


Solving the finite reconstruction recurrence gives


$$
\boxed{
\xi_j=\frac{j!}{b!\,\mathscr S}\,\mathscr S_j,
\qquad 0\le j<b,
}
\tag{4.3}
$$


with


$$
E_j=W_j(j\xi_{j-1}-\xi_j),
\qquad 0\le j\le b.
\tag{4.4}
$$



Indeed, for $j<b$,


$$
j\xi_{j-1}-\xi_j
=
-\frac{j!}{b!\mathscr S}\ell_j^2,
$$


and


$$
W_j\frac{j!}{b!}\ell_j^2
=
W_b\ell_j.
$$


At the endpoint,


$$
b\xi_{b-1}
=
\frac{\mathscr S-1}{\mathscr S},
$$


so (4.4) gives


$$
E_b=W_b\left(1-\frac1{\mathscr S}\right),
$$


as required.

Therefore the complete projected column has divided reconstruction coefficients


$$
\boxed{\psi^\parallel=\psi+\xi.}
\tag{4.5}
$$



Although $Y^\parallel$ is $p$-integral, the coefficients $\xi_j$ need not be. Equation (4.3) exposes the precise factorial denominator that must be tracked.

---

## 5. A genuine original-family, all-depth contact-lattice countermechanism

Take the fixed integer


$$
B=687936+20p^5=410910916.
\tag{5.1}
$$


It is compatible with the preferred cylinder because


$$
B\equiv687936+20p^5\pmod{p^6}.
$$



Let


$$
k=v_p(b-B)\ge9,
\tag{5.2}
$$


and consider the actual coordinate


$$
j=b-B-1.
\tag{5.3}
$$


All original $b$ here are vastly larger than $B+26$, so this coordinate is inside $0\le j<b$.

Define the fixed valuations


$$
F_B=v_p(B!),
$$




$$
E_B=
v_p\!\left(\frac{(2001B+3)!}{(2000B+2)!}\right).
\tag{5.4}
$$



### Theorem 2 — exact lift loss

At every original index satisfying (5.2),


$$
\boxed{
v_p(\xi_{b-B-1})=2E_B-F_B-k.
}
\tag{5.5}
$$


For the stated $B$,


$$
F_B=14675386,\qquad E_B=14675390,
$$


so


$$
\boxed{
v_p(\xi_{b-B-1})=14675394-k.
}
\tag{5.6}
$$



#### Proof

Put


$$
r=B+1,\qquad c=2000b+3.
$$


Then


$$
\ell_j=(c)^{\overline r}.
$$



Because $b\equiv B\pmod{p^k}$,


$$
(c)^{\overline r}
\equiv(2000B+3)^{\overline{B+1}}\pmod{p^k}
$$


factor by factor.

Every positive factor in the fixed product lies between


$$
2000B+3=821821832003
$$


and


$$
2001B+3=822232742919.
$$


The latter is less than


$$
p^9=14507145975869.
$$


Thus, for $k\ge9$, every factor’s valuation is less than $k$ and is unchanged by the congruence. Consequently


$$
v_p(\ell_j)=E_B.
\tag{5.7}
$$



Next,


$$
\mathscr S_j
=
\ell_j^2
\sum_{s=0}^{j}\bigl((c+r)^{\overline s}\bigr)^2.
\tag{5.8}
$$


Since $b\equiv B\equiv27\pmod p$,


$$
c+r=2000b+B+4\equiv4\pmod p.
$$


Terms with $s\ge26$ vanish modulo $p$, and


$$
\sum_{s=0}^{25}(4^{\overline s})^2
=
1+4^2\sum_{s=0}^{24}(5^{\overline s})^2
\equiv1+16\cdot8
\equiv13\pmod p.
\tag{5.9}
$$


This is a unit. Hence


$$
v_p(\mathscr S_j)=2E_B.
\tag{5.10}
$$



Finally,


$$
\frac{b!}{j!}
=(b-B)(b-B+1)\cdots b.
$$


The first factor has valuation $k$. The others are congruent modulo $p^k$ to $1,\ldots,B$, and $B<p^k$, so their valuations are unchanged. Therefore


$$
v_p(b!/j!)=k+F_B.
\tag{5.11}
$$



Substitution into (4.3), using $v_p(\mathscr S)=0$, proves (5.5). The fixed factorial valuations below give (5.6). ∎

### 5.1 The fixed factorial arithmetic

Legendre’s formula gives the following short receipt:



$$
\begin{array}{c|r|r}
m&
\left\lfloor B/p^m\right\rfloor&
\left\lfloor(2001B+3)/p^m\right\rfloor
-\left\lfloor(2000B+2)/p^m\right\rfloor\\ \hline
1&14169341&14169342\\
2&488597&488598\\
3&16848&16848\\
4&580&581\\
5&20&20\\
6&0&1\\
7&0&0\\
8&0&0
\end{array}
$$


Thus


$$
F_B=14675386,\qquad E_B=14675390.
$$



This is bounded exact arithmetic on fixed integers, not a calculation of any enormous original column.

### 5.2 Why the bad lifts occur at actual original indices

The accepted original-parameter lifting bijection applies to every finite extension of the low digits.

For every $k\ge9$, the finite condition


$$
b\equiv B+p^k\pmod{p^{k+1}}
\tag{5.12}
$$


is compatible with (1.1)–(1.2). It therefore specifies a nonempty original $t$-congruence class inside


$$
t\equiv364\pmod{841}.
$$


Every representative satisfies


$$
v_p(b-B)=k.
$$



This does not select an independent auxiliary $b$, nor prescribe an entire infinite digit word. It uses one finite original congruence for each $k$.

### 5.3 The complete force cannot cancel the negative lift

By (1.9),


$$
\psi\in\mathbb Z_p^b.
$$


Therefore, when $k>14675394$, equation (4.5) gives


$$
\boxed{
v_p\!\left(\psi^\parallel_{b-B-1}\right)
=14675394-k<0.
}
\tag{5.13}
$$



The same conclusion holds after subtracting any integral scalar multiple of the $P$-lift. In particular, for every $s\in\mathbb Z_p$,


$$
v_p\!\left(
\psi^\parallel_{b-B-1}-ps\,\theta_{b-B-1}
\right)
=14675394-k.
\tag{5.14}
$$



The complete exponential and logarithmic force is present in $\psi$. Its integrality is exactly why it cannot cancel the negative-valuation term.

### Consequence and limitation

The following natural strategy is false on arbitrarily deep original refinements:

> Remove the normal exterior component, then express the remaining $Q$-column, after an integral scalar multiple of $P$, by an integral operator acting in the original contact lattice.

The obstruction is not removed common content or a freely chosen isotropic vector. It is the exact factorial denominator in the actual finite reconstruction, and its loss is unbounded.

This does **not** disprove


$$
v_p(M-\rho_nD)\ge v_p(D)+1.
$$


A weighted skew-adjoint identity could still hold without admitting an integral pullback to the unsaturated contact lattice.

---

## 6. An exact adjoint formulation retaining the endpoint

It is useful to record the actual Gram operator before proposing the next lemma.

Let $C$ be the $(b+1)\times b$ reconstruction matrix


$$
(Cx)_j=jx_{j-1}-x_j,
$$


with the same endpoint conventions as above, and put


$$
K=C^T\operatorname{diag}(W_j^2)C.
$$


Then $K$ is the explicit tridiagonal matrix


$$
K_{jj}=W_j^2+(j+1)^2W_{j+1}^2,
\qquad 0\le j<b,
\tag{6.1}
$$




$$
K_{j,j+1}=K_{j+1,j}=-(j+1)W_{j+1}^2,
\qquad 0\le j<b-1.
\tag{6.2}
$$


In particular, $K_{b-1,b-1}$ includes $b^2W_b^2$.

The exact scalar products are


$$
\boxed{p^4D=\theta^TK\theta,}
\tag{6.3}
$$




$$
\boxed{p^5M=\theta^TK\psi+bW_b^2\theta_{b-1}.}
\tag{6.4}
$$



Thus the unprojected adjoint relation has a genuine endpoint term. Dropping it is not a finite-boundary simplification.

Let


$$
A=\widetilde N U^{-1},
\qquad A\theta=f^0,\qquad A\psi=\mathbf r,
$$


and define $z$ by the finite adjoint system


$$
A^Tz=K\theta.
$$


Then


$$
\boxed{
p^5(M-sD)
=
z^T(\mathbf r-psf^0)+bW_b^2\theta_{b-1}
}
\tag{6.5}
$$


for every scalar $s$.

This formula is exact but does not, by itself, prove alignment: its force contraction still needs evaluation. Its value is that the missing endpoint and complete force are visible in a finite adjoint identity.

The projection in Sections 2–4 replaces the explicit endpoint in (6.5) by the explicit lift $\xi$; Theorem 2 shows why the latter cannot be treated as an integral contact correction uniformly in depth.

---

## 7. A concrete follow-on lemma on the saturated weighted space

The contact-lattice obstruction suggests working directly with the integral projector $\Pi$, not pretending that its pullback is integral.

### 7.1 Explicit skew-adjoint operators and their currents

Let $g_0,\ldots,g_{b-1}\in\mathbb Z_p$, and define the finite skew-tridiagonal matrix


$$
\mathcal A(g)_{j,j+1}=g_j,\qquad
\mathcal A(g)_{j+1,j}=-g_j.
\tag{7.1}
$$


There are no entries beyond $0,\ldots,b$.

Set


$$
\mathcal K(g)=\Pi\mathcal A(g)\Pi.
\tag{7.2}
$$


Then


$$
\mathcal K(g)^T=-\mathcal K(g),\qquad
\mathcal K(g)\ell=0,
$$


and $\mathcal K(g)$ is integral over $\mathbb Z_p$.

Because $\Pi P=P$, define


$$
\beta=\frac{\ell^T\mathcal A(g)P}{\mathscr S}\in\mathbb Z_p.
$$


Then


$$
\mathcal K(g)P=\mathcal A(g)P-\beta\ell.
\tag{7.3}
$$



Put


$$
\mathfrak f_{j+1}=g_jP_jP_{j+1}
\quad(0\le j<b),
\qquad
\mathfrak f_0=\mathfrak f_{b+1}=0.
\tag{7.4}
$$


Equations (3.5) and (7.3) give


$$
\boxed{
P_j(\mathcal K(g)P)_j
=
(\mathfrak f_{j+1}-\beta\mathfrak c_{j+1})
-(\mathfrak f_j-\beta\mathfrak c_j).
}
\tag{7.5}
$$



This is an explicit finite current for this operator family.

### 7.2 The force-side identity that would suffice

For a zero-charge weighted vector $w$, define its divided reconstruction inverse by


$$
\mathcal L(w)_j
=
-j!\sum_{i=0}^{j}\frac{w_i}{\omega_i},
\qquad 0\le j<b.
\tag{7.6}
$$


This formula retains the actual lower endpoint. Its upper compatibility condition is precisely $\ell^Tw=0$.

Theorem 2 warns that $\mathcal L(w)$ need not be integral even when $w$ is integral.

The following is a concrete sufficient lemma.

> **Saturated full-force skew-reconstruction lemma — open.**  
> Construct $s_n\in\rho_n+p\mathbb Z_p$, determined from the complete contact/force identities independently of $D$, and explicitly specified integral coefficients $g_j$, such that
> 

$$
> \boxed{
> \mathbf r+\widetilde N U^{-1}\xi
> =
> ps_nf^0+
> p\,\widetilde N U^{-1}
> \mathcal L\!\left(\mathcal K(g)Z_w\right).
> }
> \tag{7.7}
>
$$


> The rational contact-lift terms in this identity must be retained at their actual valuations. In particular, $\widetilde N U^{-1}\xi$ cannot be replaced by an integral surrogate.

Equation (7.7) is an equality of the complete $b$-entry force vectors. It is not the scalar quotient $s_n=M/D$, and it does not define a current by cumulatively summing the desired defect.

A useful initial family to test symbolically is


$$
g_j=(j+1)(n+2-j)\,h_n(j),
\tag{7.8}
$$


with an explicitly bounded-degree polynomial $h_n$. The coefficient
$(j+1)(n+2-j)$ is compatible with the exact adjacent-weight ratio


$$
\frac{W_{j+1}}{W_j}=\frac{n+2-j}{j+1}.
$$


No claim is made that a constant or affine $h_n$ already satisfies (7.7). Its adequacy is an outstanding force-identity question, not something supplied by generic orthogonality theory.

### Proposition 3 — exact consequence of the follow-on lemma

If (7.7) holds, put


$$
\alpha_n=s_n-\rho_n\in p\mathbb Z_p.
$$


Then


$$
\boxed{
Q^\parallel=s_nP+\mathcal K(g)P,
}
\tag{7.9}
$$


and therefore


$$
\boxed{
M=s_nD,\qquad
v_p(M-\rho_nD)\ge v_p(D)+1,\qquad
v_p(M)=v_p(D).
}
\tag{7.10}
$$



Moreover, the full coordinate current is


$$
\boxed{
\mathfrak J_k=
\mathfrak f_k+(\gamma-\beta)\mathfrak c_k,
}
\tag{7.11}
$$


and


$$
\boxed{
P_j(Q_j-\rho_nP_j)
=
\alpha_nP_j^2+\mathfrak J_{j+1}-\mathfrak J_j.
}
\tag{7.12}
$$


Both boundary currents are zero:


$$
\mathfrak J_0=\mathfrak J_{b+1}=0.
$$



#### Proof

Apply $U\widetilde N^{-1}$ to (7.7):


$$
\psi+\xi=ps_n\theta+p\mathcal L(\mathcal K(g)Z_w).
$$


Reconstruction gives


$$
Y^\parallel=ps_nZ_w+p\mathcal K(g)Z_w.
$$


Dividing by $p^3$ proves (7.9). Skew-adjointness gives


$$
P^T\mathcal K(g)P=0,
$$


so $M=s_nD$. Since $s_n\equiv\rho_n\not\equiv0\pmod p$, the valuation assertions follow.

Finally combine (3.7) and (7.5). The endpoint conventions in (3.4) and (7.4) give both zero boundary currents. Summing over the actual high blocks gives the proposed blockwise identity, including the shorter last block. ∎

What remains unproved is the force identity (7.7), including an independently determined scalar and a controlled explicit operator. The current formula and its consequence are proved.

---

## 8. Common content and primitive-norm cancellation remain separate

The projection does not lose common content in weighted coordinates.

Indeed, if $Q\in p^c\mathbb Z_p^{b+1}$, then


$$
\ell^TQ=W_b/p^3\in p^c\mathbb Z_p,
$$


so $\gamma\in p^c\mathbb Z_p$, and hence


$$
Q^\parallel\in p^c\mathbb Z_p^{b+1}.
\tag{8.1}
$$


Thus the unbounded loss in Theorem 2 belongs to the **contact lift**, not to the weighted column itself.

For exact content accounting, let


$$
c_P=\min_jv_p(P_j),\qquad
c_Q=\min_jv_p(Q_j),
$$


and write


$$
P=p^{c_P}x,\qquad Q=p^{c_Q}y,
$$


with $x,y$ primitive. Put


$$
y^\parallel=y-\frac{\ell^Ty}{\mathscr S}\ell.
$$


Then


$$
x^Ty^\parallel=x^Ty.
$$



Define


$$
\nu=v_p(x^Tx),\qquad
\chi=v_p(x^Ty^\parallel),
$$


when the mixed product is nonzero. The exact scalar valuations are


$$
\boxed{
\delta=v_p(D)=2c_P+\nu,
}
\tag{8.2}
$$




$$
\boxed{
\mu=v_p(M)=c_P+c_Q+\chi,
}
\tag{8.3}
$$


and therefore


$$
\boxed{
\delta-\mu=c_P-c_Q+\nu-\chi.
}
\tag{8.4}
$$



The endpoint projection preserves these scalar quantities exactly. It does not bound the additional primitive-norm cancellation $\nu$, or compare it with $\chi$.

If the force lemma (7.7) were proved, it would carry the entire actual norm $D$, including both its removed content and its primitive-norm cancellation. Without that lemma, no such comparison follows from the present results.

---

## 9. Final gcd, actual primitive denominator, and whole same-index error

Retain the actual least two-column denominator and integer Gram pair:


$$
N_B=d_B[u,v],\qquad v_{29}(d_B)=0,
$$




$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,
\qquad
H_B=N_{B,1}^T\Omega N_{B,2}.
$$


The final normalization is


$$
g_B=\gcd(A_B,|H_B|),
\qquad
p_n=H_B/g_B,\qquad q_n=A_B/g_B>0.
\tag{9.1}
$$



No factorial-lattice index, projector denominator, or column content replaces this full gcd.

With


$$
F_n=v_{29}(n!),\qquad F_b=v_{29}(b!),
$$


the retained exact interface is


$$
\boxed{
v_{29}(g_B)
=
\min\{4F_n+4+\delta,\;2F_n+F_b+5+\mu\},
}
\tag{9.2}
$$




$$
\boxed{
v_{29}(q_n)
=
\max\{0,\;2F_n-F_b-1+\delta-\mu\}.
}
\tag{9.3}
$$


Equivalently, using the exact content decomposition,


$$
v_{29}(q_n)
=
\max\{0,\;2F_n-F_b-1+c_P-c_Q+\nu-\chi\}.
\tag{9.4}
$$



The new current does not evaluate the last four terms. The force lemma would give $\delta=\mu$, but still only settle the local $29$-part.

The full primitive denominator remains


$$
\log q_n
=
\sum_{\ell}
\max\{v_\ell(A_B)-v_\ell(H_B),0\}\log\ell.
\tag{9.5}
$$


No all-prime estimate for this quantity is established.

For


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
$$


the complete same-index evaluated form remains


$$
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n.}
\tag{9.6}
$$


At the retained hypotheses and proof status of the complete signed-error theorem,


$$
\epsilon_n>0\quad\text{eventually},
$$




$$
\log|\epsilon_n|
=
-\left(2+\frac1{2001}\right)n\log(1+\sqrt2)+o(n).
\tag{9.7}
$$



Norm nonvanishing follows from the nonzero first column and the positive real metric. Mixed nonvanishing retains its supplied original-family dependency. Eventual nonvanishing of (9.6) retains the complete signed-error theorem’s status.

The present results neither prove that the whole nonzero form tends to zero nor provide a rationality argument.

---

## 10. Bounded exact arithmetic for personal inspection

No new initializer, auxiliary recurrence, or large original-column calculation is requested.

Two small receipts suffice to audit the new numerical constants.

### A. Normal-vector unit and tail unit

**Inputs**

Work in $\mathbb F_{29}$. Set


$$
u_0=1,\qquad u_{r+1}=(5+r)u_r,
\qquad 0\le r<24.
$$



**Expected verifiable output**


$$
\boxed{\sum_{r=0}^{24}u_r^2=8\pmod{29},}
$$


and consequently


$$
\boxed{
1+16\sum_{r=0}^{24}u_r^2=13\pmod{29}.
}
$$



These certify the actual normal norm as a unit and the exact valuation of the partial normal norm used in Theorem 2.

### B. Fixed factorial-lift loss

**Inputs**


$$
B=410910916,
$$




$$
U=2001B+3=822232742919,
\qquad
V=2000B+2=821821832002.
$$



Evaluate only


$$
\sum_{m=1}^{8}\left\lfloor B/29^m\right\rfloor
$$


and


$$
\sum_{m=1}^{8}
\left(
\left\lfloor U/29^m\right\rfloor-
\left\lfloor V/29^m\right\rfloor
\right).
$$



**Expected verifiable output**


$$
\boxed{F_B=14675386,\qquad E_B=14675390,}
$$




$$
\boxed{2E_B-F_B=14675394.}
$$



No factorials themselves need to be constructed. No original $3^a$ needs to be expanded. These finite receipts verify fixed arithmetic in a proof whose original-index quantifiers come from the accepted finite lifting bijection.

---

# Conclusion and proof-status ledger

## New proved results

1. The complete actual reconstruction has affine charge
   

$$
\ell^TZ_w=0,\qquad \ell^TY=W_b.
$$



2. Its normal vector has independently evaluated norm
   

$$
\ell^T\ell\equiv8\pmod{29}.
$$


   Therefore orthogonal projection onto the saturated weighted reconstruction space is integral at $29$.

3. The exterior normal component admits an explicit integral current, with the genuine first and last high-block currents both zero. The shorter final block is retained.

4. The projected exterior term has exact divided lift
   

$$
\xi_j=\frac{j!}{b!\,\ell^T\ell}\sum_{i=0}^j\ell_i^2.
$$



5. At originally reachable preferred-cylinder refinements,
   

$$
v_{29}(\xi_{b-B-1})
   =14675394-v_{29}(b-B).
$$


   This produces arbitrarily deep negative contact-lift valuations. Once negative, the complete actual force cannot cancel them.

6. An explicit saturated weighted skew-operator family has a finite current with zero endpoints. The full-force identity (7.7), if proved with an independently determined scalar, would give the desired all-depth relative alignment and its actual block current.

## Exact remaining local bottleneck

The endpoint-normal current is now explicit. The unresolved part is:

> Prove, or genuinely refute for the complete actual force, the saturated weighted force identity (7.7), or another identity that controls $M-\rho_nD$ relative to the full actual norm after primitive-norm cancellation.

An integral pullback through the original contact lattice cannot simply be assumed: Theorem 2 gives a genuine actual obstruction and quantifies its unbounded loss.

## Global bottleneck

Even an affirmative all-depth $29$-adic alignment theorem would leave the full final gcd and the actual primitive denominator across all primes unresolved. Those must still be compared with the whole same-index error


$$
-q_n\epsilon_n.
$$



Accordingly, this report provides an exact partial current and an actual all-depth reconstruction obstruction, but **not an unconditional proof or disproof of irrationality of $e+\pi$**.
