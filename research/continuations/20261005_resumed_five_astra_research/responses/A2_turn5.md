> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2, Turn 5 — A nearest-neighbor obstruction, an exact factorial-force recurrence, and a saturated norm/mixed factorization

## Executive conclusions

The complete-force identity (7.7) is **not proved**. This report establishes three concrete advances.

1. **The proposed nearest-neighbor family is impossible on sufficiently deep originally reachable branches if $h_n$ is integral-valued on the actual edge indices.** This includes every polynomial $h_n\in\mathbb Z_{29}[J]$, of any degree. More strongly, if the edge coefficients $g_j$ are integral and
   

$$
\deg h_n\le 26,
$$


   then the family is impossible even without assuming that the coefficients of $h_n$ are integral.

   The obstruction is an exact coefficient equation:
   

$$
\boxed{(1-29\kappa_h)\xi=29s_n\theta+29\eta_h-\psi.}
$$


   Here $\eta_h$ and $\kappa_h$ are explicitly constructed from the first, complete contact solution, independently of $D$. For integral-valued $h_n$, both are integral. The coefficient $1-29\kappa_h$ is then a unit and cannot absorb the actual unbounded negative valuation of $\xi$.

2. **Allowing a nonintegral polynomial $h_n$ while keeping all $g_j$ integral is a genuine escape route, not something the preceding argument rules out.** It first becomes possible at degree $27$. At that degree, a necessary first residue is explicitly
   

$$
\boxed{
   15\lambda\bigl(2\theta_{b-26}-\theta_{b-25}\bigr)=1
   \quad\text{in }\mathbb F_{29}.
   }
$$


   The coefficient $\lambda$ is the leading residue of $29h_n$, specified below. Thus the nonintegral pullback imposes a constraint on independently determined operator coefficients and actual first-force data. It cannot be bypassed by assuming an integral contact lift.

3. **There is an exact finite recurrence for the actual factorial/exponential force, and an explicit integral orthogonal transformation of the actual weighted columns giving a two-channel norm/mixed factorization.** The latter carries *all* primitive-norm cancellation:
   

$$
\boxed{
   D=29^{2c}\mathfrak a\mathfrak b,\qquad
   2M=29^c(\mathfrak a\mathfrak v+\mathfrak b\mathfrak u),
   \qquad \mathfrak a\in\mathbb Z_{29}^{\times}.
   }
$$


   Every component is explicitly evaluable from the complete finite reconstruction. No component is defined as $M/D$, and the transformation requires division only by a demonstrated unit.

This is an actual norm/mixed factorization, not an auxiliary isotropic-vector example. It yields a sharp remaining force-side divisibility problem. It does **not** establish that divisibility.

The full final gcd, actual primitive denominator, and whole evaluated error remain separate obligations. **The irrationality or rationality of $e+\pi$ remains unresolved.**

No tools were executed.

---

## 1. Scope, dependencies, and notation

Retain the original domain


$$
p=29,\qquad
a=432827+682892t,\quad t\ge0,\qquad
b=3^a,\qquad n=2001b,
$$


and the preferred cylinder


$$
t\equiv364\pmod{841}.
$$



The weighted coordinates are exactly $0\le j\le b$. The contact coordinates are exactly $0\le j<b$.

Write


$$
W_j=\binom{n+2}{j},
\qquad
\omega_j=j!W_j,
$$


and define the finite reconstruction map


$$
(\mathcal R x)_j=W_j(jx_{j-1}-x_j),
\qquad
x_{-1}=x_b=0.
$$


Thus


$$
Z_w=\mathcal R\theta,\qquad
Y=\mathcal R\psi+W_be_b,
$$


where


$$
\theta=A^{-1}f^0,\qquad
\psi=A^{-1}\mathbf r,\qquad
A=\widetilde N U^{-1}.
$$


The complete force is


$$
\mathbf r=
\frac{h^e+h^F-\widetilde N(I+S)^n(j!)_{0\le j<b}}{b!}.
$$


In particular, neither the factorial subtraction nor $h^F$ is removed.

The normalized columns and scalar products remain


$$
P=Z_w/p^2,\qquad Q=Y/p^3,\qquad
D=P^TP,\qquad M=P^TQ.
$$



I use the retained complete-force integrality


$$
\theta,\psi\in\mathbb Z_p^b
$$


and the accepted fixed-precision conclusions


$$
D\equiv5C_n^2\mathcal T\pmod{p^4},
\qquad
M-\rho_nD\equiv0\pmod{p^4},
\qquad \rho_n=(6C_n)^{-1}.
$$


They are not promoted to all-depth statements.

### 1.1 Turn 4 dependencies

I do not re-prove the normal charge or its current. The following Turn 4 formulas are the exact inputs needed here:


$$
\ell_j=\frac{\omega_b}{\omega_j},\qquad
\mathscr S=\ell^T\ell,\qquad
\Pi=I-\frac{\ell\ell^T}{\mathscr S},
$$




$$
E=W_be_b-\frac{W_b}{\mathscr S}\ell=\mathcal R\xi,
$$




$$
\xi_j=\frac{j!}{b!\mathscr S}\sum_{i=0}^j\ell_i^2,\qquad 0\le j<b,
$$


and


$$
Q^\parallel=\Pi Q,\qquad
Y^\parallel=\mathcal R\psi+E=\mathcal R(\psi+\xi).
$$



The asserted fixed arithmetic is


$$
\mathscr S\equiv8\pmod{29},
$$


and, with


$$
B=410910916,\qquad
k=v_{29}(b-B)\ge9,
$$




$$
v_{29}(\xi_{b-B-1})=14675394-k. \tag{1.1}
$$



The algebraic arguments below identify exactly where these pending-audit inputs enter. The original-index occurrence of arbitrarily large finite $k$ uses the retained finite lifting bijection, not a freely selected auxiliary $b$.

The higher-tail compression receipt and A4 audit are accepted at their stated finite and fixed-precision scope. They supply no additional all-depth force identity.

---

# Part I. An exact recurrence for the actual factorial force

## 2. A recurrence before contact inversion

The actual exponential part of the divided force is


$$
r_i^e=
\sum_{s=0}^{\min(2n,n+i)}
c_s(n+i)_{\underline s}\,
T_{2n+i-s},
\qquad
c_s=[z^s](1-z+z^2/2)^n,
\tag{2.1}
$$


where


$$
T_m=\frac1{b!}\sum_{q=b}^{m}(m)_{\underline q},
$$


and $T_m=0$ if $m<b$.

This is the complete factorial tail from the supplied reconstruction, not a fixed-precision truncation.

### Proposition 1 — exact tail recurrence

For $m\ge1$,


$$
\boxed{T_m=mT_{m-1}+\binom mb.} \tag{2.2}
$$



#### Proof

For $m\ge b$,


$$
\begin{aligned}
\sum_{q=b}^{m}(m)_{\underline q}
&=
m\sum_{q=b}^{m}(m-1)_{\underline{q-1}}\\
&=
m\sum_{q=b}^{m-1}(m-1)_{\underline q}
+(m)_{\underline b}.
\end{aligned}
$$


Divide by $b!$. The same identity holds below $b$, with both tails zero. ∎

The inhomogeneous binomial in (2.2) is the factorial boundary source. It is not discarded.

## 3. Transport through the actual quadratic kernel

Put


$$
\phi(z)=1-z+\frac{z^2}{2},
\qquad
F(z)=\sum_{\ell\ge0}T_{n+\ell}\frac{z^\ell}{\ell!},
$$


and


$$
G(z)=\sum_{\ell\ge0}\binom{n+\ell+1}{b}\frac{z^\ell}{\ell!}.
$$


Equation (2.2) gives the formal identity


$$
(1-z)F'(z)=(n+1)F(z)+G(z).
$$



Let


$$
R(z)=\phi(z)^nF(z)=\sum_{m\ge0}R_m\frac{z^m}{m!}.
$$


By construction,


$$
R_{n+i}=r_i^e.
$$



A direct differentiation gives


$$
(1-z)\phi R'
-\bigl[n(1-z)\phi'+(n+1)\phi\bigr]R
=\phi^{n+1}G.
$$


The two polynomial coefficients are


$$
(1-z)\phi=1-2z+\frac32z^2-\frac12z^3
$$


and


$$
n(1-z)\phi'+(n+1)\phi
=1+(n-1)z-\frac{n-1}{2}z^2.
$$



Consequently:

### Theorem 2 — exact finite-row factorial-force recurrence

For every actual interior index


$$
2\le i\le b-2,
$$


the complete exponential force satisfies


$$
\boxed{
\begin{aligned}
r_{i+1}^e
&-(2n+2i+1)r_i^e\\
&+\frac{(n+i)(n+3i-1)}2r_{i-1}^e\\
&+\frac{(n+i)(n+i-1)(1-i)}2r_{i-2}^e
=\mathcal H_i,
\end{aligned}}
\tag{3.1}
$$


where the forcing term is explicitly


$$
\boxed{
\mathcal H_i=
\sum_{s=0}^{\min(2n+2,n+i)}
[z^s]\phi(z)^{n+1}\,
(n+i)_{\underline s}
\binom{2n+i-s+1}{b}.
}
\tag{3.2}
$$



#### Proof

Extract $m![z^m]$ from the preceding differential identity and then substitute $m=n+i$. The coefficient of $R_{m-1}$ is


$$
\frac32m(m-1)-(n-1)m
=\frac{m(3m-2n-1)}2,
$$


and that of $R_{m-2}$ is


$$
-\frac12m(m-1)(m-2)
+\frac{n-1}{2}m(m-1)
=\frac{m(m-1)(n-m+1)}2.
$$


These give (3.1). The coefficient on the right gives (3.2). ∎

### 3.1 Complete logarithmic force and finite boundaries

Let $\mathcal D_n$ denote the four-term finite-row operator on the left of (3.1). For the complete force,


$$
\boxed{
(\mathcal D_n\mathbf r)_i
=\mathcal H_i+
\left(\mathcal D_n(h^F/b!)\right)_i,
\qquad 2\le i\le b-2.
}
\tag{3.3}
$$



The last term is retained **whole**. The attached text does not reproduce an entrywise formula for $h^F$ that would justify further simplification of this term.

The initial entries $r_0,r_1,r_2$ remain their complete formulas. No negative contact indices are introduced, and no equation beyond the actual last row $b-1$ is used. The exterior $+1$ remains separately in


$$
Y_b=W_b(1+b\psi_{b-1}).
$$



Thus (3.3) is an actual force law, but not yet an intertwining identity with a skew operator.

---

# Part II. The nearest-neighbor family has a precise contact obstruction

## 4. Exact decomposition of its saturated action

Consider


$$
g_j=(j+1)(n+2-j)h(j),\qquad 0\le j<b,
$$


and the finite skew matrix


$$
\mathcal A(g)_{j,j+1}=g_j,\qquad
\mathcal A(g)_{j+1,j}=-g_j.
$$


There are no edges outside $0,\ldots,b$.

Set


$$
\mathcal K(g)=\Pi\mathcal A(g)\Pi.
$$



For the actual first contact solution, write


$$
q_j^\theta=j\theta_{j-1}-\theta_j,\qquad 0\le j\le b.
$$


Define the following quantities directly from $h$ and $\theta$:


$$
\boxed{
t_j=
\mathbf1_{j<b}(n+2-j)^2h(j)q_{j+1}^\theta
-\mathbf1_{j>0}j^2h(j-1)q_{j-1}^\theta,
}
\tag{4.1}
$$




$$
\boxed{
\eta_{h,j}=-j!\sum_{i=0}^j\frac{t_i}{i!},
\qquad 0\le j<b,
}
\tag{4.2}
$$


and


$$
\boxed{
\kappa_h=\sum_{i=0}^b\frac{b!}{i!}t_i.
}
\tag{4.3}
$$



These definitions contain no $D$, $M$, or proposed defect.

The adjacent-weight ratio gives


$$
(\mathcal A(g)Z_w)_j=W_jt_j.
$$


At the true last coordinate,


$$
t_b=-b^2h(b-1)q_{b-1}^\theta;
$$


there is no artificial upper-edge term.

### Proposition 3 — endpoint-exact saturated action

One has


$$
\boxed{
\mathcal R\eta_h=\mathcal A(g)Z_w-\kappa_hW_be_b,
}
\tag{4.4}
$$


and therefore


$$
\boxed{
\mathcal K(g)Z_w=\mathcal R\eta_h+\kappa_hE
=\mathcal R(\eta_h+\kappa_h\xi).
}
\tag{4.5}
$$



#### Proof

For $j<b$, the defining partial sum in (4.2) gives


$$
j\eta_{h,j-1}-\eta_{h,j}=t_j.
$$


At $j=b$,


$$
b\eta_{h,b-1}
=-b!\sum_{i=0}^{b-1}\frac{t_i}{i!}
=t_b-\kappa_h.
$$


This proves (4.4), including the endpoint.

Also,


$$
\ell^T\mathcal A(g)Z_w
=\omega_b\sum_{i=0}^b\frac{t_i}{i!}
=W_b\kappa_h.
$$


Since $\Pi Z_w=Z_w$,


$$
\mathcal K(g)Z_w
=\mathcal A(g)Z_w-\frac{W_b\kappa_h}{\mathscr S}\ell.
$$


Combine this with (4.4) and the definition of $E$. ∎

This identity isolates exactly how the saturated operator acquires its nonintegral contact pullback.

## 5. The full-force equality forces a scalar matching of that pullback

Turn 4’s identity (7.7) is equivalent to


$$
Y^\parallel=ps_nZ_w+p\mathcal K(g)Z_w.
$$


Using (4.5) and the injectivity of $\mathcal R$, this becomes


$$
\psi+\xi=ps_n\theta+p\eta_h+p\kappa_h\xi.
$$



Hence the exact necessary and sufficient contact equation for this family is


$$
\boxed{
(1-p\kappa_h)\xi
=ps_n\theta+p\eta_h-\psi.
}
\tag{5.1}
$$



Every complete-force term remains in $\psi=A^{-1}\mathbf r$. The exterior $+1$ is exactly the source of the $\xi$-term.

### Theorem 4 — impossibility for integral-valued $h$

Suppose

* $s_n\in\rho_n+p\mathbb Z_p$;
* $h(j)\in\mathbb Z_p$ for all $0\le j<b$.

Then the full-force equality is impossible at every original index with


$$
v_p(b-B)>14675394.
$$



#### Proof

By (4.1), all $t_i$ are integral. Since $j!/i!$ and $b!/i!$ are integers in their displayed ranges,


$$
\eta_h\in\mathbb Z_p^b,\qquad \kappa_h\in\mathbb Z_p.
$$


Thus $1-p\kappa_h$ is a unit.

The right side of (5.1) is integral, because $s_n,\theta,\psi,\eta_h$ are integral. At the actual coordinate $j=b-B-1$, however, (1.1) makes the left side have valuation


$$
14675394-v_p(b-B)<0.
$$


Contradiction. ∎

This applies to **every** polynomial with coefficients in $\mathbb Z_p$, regardless of degree. In particular, constant and affine choices do not merely lack a known proof: they fail on the stated actual branches.

The proof does not replace the complete force by its leading approximation. The integrality of the complete $\psi$ is what makes the obstruction decisive.

---

## 6. Integral edge coefficients do not always imply integral $h$

It would be incorrect to conclude from Theorem 4 that every polynomial family with integral $g_j$ is impossible. A factor


$$
(j+1)(n+2-j)
$$


can absorb a denominator of $h(j)$.

The degree restriction determines when that escape first becomes available.

### Theorem 5 — degree at most $26$ is impossible even with nonintegral polynomial coefficients

Let


$$
h(J)\in\mathbb Q_p[J],\qquad \deg h\le26,
$$


and suppose that all actual $g_j$ are integral. Then $h\in\mathbb Z_p[J]$. Consequently Theorem 4 applies.

#### Proof

On the original domain $n\equiv0\pmod p$, so


$$
(j+1)(n+2-j)
$$


is a unit whenever


$$
j\not\equiv2,28\pmod{29}.
$$


There are $27$ such residues.

Choose $\deg h+1$ distinct representatives among them in $0,\ldots,27$. These are actual edge indices. Integrality of $g_j$ gives integrality of $h(j)$ at these nodes.

Their Vandermonde determinant is a $p$-adic unit. Interpolation therefore gives integral polynomial coefficients. ∎

Thus the entire bounded-degree class through degree $26$, with integral skew edges, is ruled out on the deep branches in Theorem 4.

### 6.1 A uniform coefficient bound at any fixed degree

For a general fixed degree $d$, let


$$
e_0<e_1<\cdots<e_d
$$


be the first $d+1$ nonnegative integers avoiding residues $2,28\pmod{29}$, and put


$$
C_d=
\max_{0\le r\le d}
v_p\!\left(\prod_{m\ne r}(e_r-e_m)\right).
\tag{6.1}
$$


Whenever these nodes lie in the actual edge range, Lagrange interpolation gives


$$
h\in p^{-C_d}\mathbb Z_p[J].
$$



Consequently


$$
v_p(\eta_{h,j}),\,v_p(\kappa_h)\ge-C_d.
$$


Put


$$
R_d=\max(C_d-1,0).
$$


At the deep coordinate in (1.1), equation (5.1) therefore forces


$$
\boxed{
v_p(1-p\kappa_h)
\ge
k-14675394-R_d.
}
\tag{6.2}
$$



In particular, once the right side is positive,


$$
\boxed{v_p(\kappa_h)=-1.} \tag{6.3}
$$



This is a constraint on the independently defined first-force contraction (4.3). The scalar $s_n$ cannot remove it, since $ps_n\theta$ remains integral.

For $d\le26$, $C_d=0$, recovering the contradiction. For larger fixed $d$, (6.2) demands increasingly accurate matching


$$
p\kappa_h\longrightarrow1
$$


along the deep original refinements. A fixed bound on the coefficient denominators is not, by itself, a contradiction to this matching.

---

## 7. The first possible denominator: an explicit degree-$27$ test

At degree $27$, one can take nodes with $C_{27}=1$. Thus


$$
H(J):=ph(J)\in\mathbb Z_p[J].
$$


If $h$ is not integral and all $g_j$ are integral, reduction modulo $p$ gives


$$
\overline H(J)=\lambda R(J),\qquad
\lambda\in\mathbb F_p^\times,
\tag{7.1}
$$


where


$$
\boxed{
R(J)=
\prod_{\substack{r\in\mathbb F_{29}\\r\ne2,-1}}(J-r)
=
\frac{J^{29}-J}{(J-2)(J+1)}
\in\mathbb F_{29}[J].
}
\tag{7.2}
$$


The displayed quotient is a polynomial identity.

Since $\kappa_h=\kappa_H/p$, the deep-branch condition becomes


$$
\kappa_H\equiv1\pmod p.
$$



### Proposition 6 — evaluated first matching coefficient

For an integral polynomial $H$ whose reduction vanishes away from $2,-1$,


$$
\boxed{
\kappa_H
\equiv
13H(2)\bigl(2\theta_{b-26}-\theta_{b-25}\bigr)
\pmod{29}.
}
\tag{7.3}
$$


For (7.1),


$$
\boxed{
\kappa_H
\equiv
15\lambda\bigl(2\theta_{b-26}-\theta_{b-25}\bigr)
\pmod{29}.
}
\tag{7.4}
$$



#### Proof

In


$$
\kappa_H=\sum_{i=0}^b\frac{b!}{i!}t_i(H),
$$


all terms with $i\le b-28$ vanish modulo $p$, because $b\equiv27\pmod p$.

For the remaining indices $b-27\le i\le b$, the residue of $i$ runs from $0$ to $27$.

In the upper term of $t_i(H)$, the only potentially nonzero value $H(i)$ occurs at residue $2$; its factor $(n+2-i)^2$ then vanishes modulo $p$.

In the lower term, residue $i-1=-1$ occurs at $i=0\pmod p$, where $i^2=0$. The only surviving term is therefore $i=b-24$, of residue $3$, and it equals


$$
-9H(2)q_{b-25}^\theta.
$$


Moreover,


$$
\frac{b!}{(b-24)!}
\equiv\frac{27!}{3!}\equiv\frac16=5\pmod{29}.
$$


Hence its coefficient is $-9\cdot5=13$.

Finally,


$$
R(2)=\frac{-1}{2+1}=-\frac13=19\pmod{29},
$$


so $13R(2)=15$. ∎

Therefore a degree-$27$ escape must satisfy


$$
\boxed{
15\lambda(2\theta_{b-26}-\theta_{b-25})=1
\quad\text{in }\mathbb F_{29}.
}
\tag{7.5}
$$



This gives an immediate actual obstruction if that first-force contact combination vanishes. If it is a unit, the equation uniquely fixes $\lambda$; it does **not** prove the remaining rows of the full-force identity.

The supplied material does not evaluate this actual contact combination. In particular, its value cannot be inferred from a vanishing norm residue.

### Status of the whole bounded-degree question

The rigorous conclusions are:

* Integral-valued $h$: impossible on the stated deep branches, at every degree.
* Integral $g$ and $\deg h\le26$: impossible.
* Integral $g$ and larger fixed degree, allowing nonintegral $h$: not ruled out in full. Equations (6.2) and (7.5) are necessary actual-force constraints.

Claiming impossibility for the last class would exceed the proof.

---

# Part III. A suitable saturated weighted group identity

## 8. Why a change of weighted coordinates is preferable

The preceding failure occurs in the **contact lattice**, not in the integral weighted space. The saturated projector remains integral when $\mathscr S$ is a unit, and $Q^\parallel$ remains integral.

A useful replacement must therefore:

1. operate directly on the actual weighted columns;
2. use only unit divisions;
3. retain the entire norm, including primitive cancellation;
4. expose a force component that can be tested without defining a scalar from $M/D$.

The following explicit orthogonal transformation does this.

## 9. An actual two-channel normal form

Let


$$
c=\min_{0\le j\le b}v_p(P_j),\qquad
x=P/p^c.
$$


The vector $x$ is primitive and integral.

Choose an actual coordinate $r$ with $x_r$ a unit, and choose any distinct actual coordinate $s$. Fix the Hensel root


$$
\iota^2=-1,\qquad \iota\equiv12\pmod{29}.
$$


At least one of


$$
x_r+\iota x_s,\qquad x_r-\iota x_s
$$


is a unit, since their sum is $2x_r$. Change the sign of $\iota$, if necessary, so that


$$
\mathfrak a=x_r+\iota x_s\in\mathbb Z_p^\times.
$$



Let


$$
I=\{0,\ldots,b\}\setminus\{r,s\},
\qquad
T=\sum_{j\in I}x_j^2,
$$


and define


$$
\boxed{
\mathfrak b=x_r-\iota x_s+\frac{T}{\mathfrak a}.
}
\tag{9.1}
$$



For any weighted vector $y$, define


$$
\mathfrak u(y)=y_r+\iota y_s,
$$




$$
\boxed{
\mathfrak v(y)=
y_r-\iota y_s
+\frac{2}{\mathfrak a}\sum_{j\in I}x_jy_j
-\frac{T}{\mathfrak a^2}(y_r+\iota y_s),
}
\tag{9.2}
$$


and


$$
\mathfrak w_j(y)=y_j-\frac{x_j}{\mathfrak a}\mathfrak u(y),
\qquad j\in I.
\tag{9.3}
$$



All divisions are by the demonstrated unit $\mathfrak a$.

### Theorem 7 — integral orthogonal group identity for the actual columns

For every pair of weighted vectors $y,z$,


$$
\boxed{
y^Tz=
\frac{\mathfrak u(y)\mathfrak v(z)+
      \mathfrak v(y)\mathfrak u(z)}2
+\sum_{j\in I}\mathfrak w_j(y)\mathfrak w_j(z).
}
\tag{9.4}
$$


The transformation is invertible over $\mathbb Z_p$. On the actual primitive first column,


$$
\mathfrak u(x)=\mathfrak a,\qquad
\mathfrak v(x)=\mathfrak b,\qquad
\mathfrak w_j(x)=0.
$$



#### Proof

First change the $r,s$ coordinates to


$$
A=y_r+\iota y_s,\qquad B=y_r-\iota y_s.
$$


Then


$$
y_r^2+y_s^2=AB.
$$



Put $\tau_j=x_j/\mathfrak a$. The remaining transformation is


$$
A'=A,\qquad
T'_j=T_j-\tau_jA,
$$




$$
B'=B+2\sum_j\tau_jT_j-\left(\sum_j\tau_j^2\right)A.
$$


A direct expansion gives


$$
A'B'+\sum_j(T'_j)^2=AB+\sum_jT_j^2.
$$


Its inverse is obtained by replacing each $\tau_j$ by $-\tau_j$. Polarization proves (9.4). Substitution of $y=x$ gives the asserted image of the first column. ∎

This is a transformation of the **actual** weighted vector $P$, constructed from its actual primitive coordinates. It is not an example involving independently chosen isotropic vectors.

## 10. Exact norm/mixed factorization with the complete force

Apply the transformation to


$$
y=Q^\parallel.
$$


Write


$$
\mathfrak u=\mathfrak u(Q^\parallel),\qquad
\mathfrak v=\mathfrak v(Q^\parallel).
$$



Because projection does not change $P^TQ$, Theorem 7 gives


$$
\boxed{
D=p^{2c}\mathfrak a\mathfrak b,
}
\tag{10.1}
$$




$$
\boxed{
2M=p^c(\mathfrak a\mathfrak v+\mathfrak b\mathfrak u).
}
\tag{10.2}
$$



The force components are explicitly


$$
Q^\parallel_j=
\frac1{p^3}
\left[
W_j(j\psi_{j-1}-\psi_j)
+W_b\mathbf1_{j=b}
-\frac{W_b}{\mathscr S}\ell_j
\right],
\tag{10.3}
$$


with


$$
\psi=A^{-1}
\frac{h^e+h^F-\widetilde N(I+S)^n(j!)_{0\le j<b}}{b!}.
$$


Substituting (10.3) into (9.2) is an explicit linear functional of the **complete** second force and the exterior endpoint. It requires no nonintegral contact lift of $Q^\parallel$.

Likewise, $\mathfrak a,\mathfrak b$, and every transformation coefficient are determined solely by the actual first column.

### 10.1 Primitive-norm cancellation is fully retained

Since $D>0$ as a nonzero rational norm,


$$
\mathfrak b\ne0.
$$


Set


$$
\nu=v_p(\mathfrak b).
$$


Then


$$
\boxed{v_p(D)=2c+\nu.} \tag{10.4}
$$



Thus the additional primitive-norm cancellation is **exactly** the valuation of the explicit component $\mathfrak b$. It has not been bounded, discarded, or replaced by common column content.

Also,


$$
\boxed{
v_p(M)=c+
v_p(\mathfrak a\mathfrak v+\mathfrak b\mathfrak u),
}
\tag{10.5}
$$


when $M\ne0$, and hence


$$
\boxed{
v_p(D)-v_p(M)
=
c+\nu-
v_p(\mathfrak a\mathfrak v+\mathfrak b\mathfrak u).
}
\tag{10.6}
$$



If the original $Q$-column has content $c_Q$, then $Q^\parallel$, $\mathfrak u$, and $\mathfrak v$ are divisible by $p^{c_Q}$. Accordingly, the original second-column content is still present in (10.5); projection does not erase it.

---

## 11. A sharp, evaluable reduction of the all-depth problem

Equations (10.1)–(10.2) give


$$
2(M-\rho_nD)
=
p^c\left[
\mathfrak a\mathfrak v+
\mathfrak b\mathfrak u
-2\rho_np^c\mathfrak a\mathfrak b
\right].
$$



Since $\mathfrak a$ is a unit and $\mathfrak b\ne0$, the desired relative statement is equivalent to the following two tests:


$$
\boxed{\mathfrak v\in\mathfrak b\,\mathbb Z_p,} \tag{11.1}
$$


and, after that division has been justified,


$$
\boxed{
\mathfrak a\frac{\mathfrak v}{\mathfrak b}
+\mathfrak u-2\rho_np^c\mathfrak a
\in p^{c+1}\mathbb Z_p.
}
\tag{11.2}
$$



Indeed, the desired valuation forces $\mathfrak a\mathfrak v$ to be divisible by $\mathfrak b$, because the other two terms already are. Once (11.1) holds, divide the displayed exact expression by $\mathfrak b$ to obtain (11.2).

This is more specific than introducing an unspecified skew operator:

* the coordinate transformation is explicit and proved;
* its coefficients are determined by the first force;
* $\mathfrak v$ is a specified linear functional of the full second force;
* $\mathfrak b$ contains all primitive-norm cancellation;
* no division by $D$ occurs;
* $\rho_n$ enters only in the final unit-scale congruence, not in the definitions of the channels.

Nevertheless, **(11.1) remains an unproved divisibility theorem for the actual force**. The group identity identifies the exact channel that must inherit the primitive-norm factor; it does not manufacture that factor.

This is the principal local bottleneck after the present reduction.

---

# Part IV. What the new results do and do not settle

## 12. Relationship to the failed nearest-neighbor ansatz

The two constructions fit together as follows.

* The nearest-neighbor calculation proves that a contact-compatible integral local family cannot reproduce the projected exterior term on deep actual branches.
* Nonintegral polynomial coefficients can only help by forcing the independently defined quantity $p\kappa_h$ to match $1$ to the depth prescribed in (6.2).
* The weighted group identity avoids that contact-lattice obstruction entirely. It stays in the saturated integral weighted space.
* Its remaining difficulty is different: the complete second force must supply the factor $\mathfrak b$ in one explicit transformed channel.

The exact factorial-force recurrence (3.3) is a possible input to evaluating that channel. It is not yet an identity proving its divisibility by $\mathfrak b$. An appropriate future argument would have to intertwine the finite force recurrence, the actual inverse $A^{-1}$, and the first-column transformation coefficients, including their endpoint terms.

No result from positive infinite Hankel theory, generic Schur complements, or the supplied methodological literature establishes that specialized intertwining. The standard linear-algebra ingredients above are used only at their proved finite scope.

---

## 13. Full gcd and the actual primitive denominator

Retain the actual least two-column denominator and integer Gram pair:


$$
N_B=d_B[u,v],\qquad v_{29}(d_B)=0,
$$




$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2}.
$$


The final normalization is


$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
p_n=H_B/g_B,\qquad q_n=A_B/g_B>0.
}
$$



Neither $\mathfrak b$, column content, a contact determinant, nor a projector denominator replaces this full gcd.

With


$$
F_n=v_{29}(n!),\qquad F_b=v_{29}(b!),\qquad
\delta=v_{29}(D),\qquad\mu=v_{29}(M),
$$


the retained exact interface remains


$$
\boxed{
v_{29}(g_B)
=
\min\{4F_n+4+\delta,\;2F_n+F_b+5+\mu\},
}
\tag{13.1}
$$




$$
\boxed{
v_{29}(q_n)
=
\max\{0,\;2F_n-F_b-1+\delta-\mu\}.
}
\tag{13.2}
$$



The new factorization gives the exact substitution


$$
\boxed{
\delta-\mu
=
c+v_{29}(\mathfrak b)
-v_{29}(\mathfrak a\mathfrak v+\mathfrak b\mathfrak u).
}
\tag{13.3}
$$


This retains both content and primitive-norm cancellation. It does not yet bound their difference.

If (11.1)–(11.2) were established, then


$$
v_{29}(M-\rho_nD)\ge v_{29}(D)+1,
\qquad
\mu=\delta,
$$


because $\rho_n$ is a unit. That would settle this local contribution, not the all-prime denominator.

Across all primes,


$$
\boxed{
\log q_n
=
\sum_{\ell}
\max\{v_\ell(A_B)-v_\ell(H_B),0\}\log\ell.
}
\tag{13.4}
$$


No bound for this whole sum is supplied by the present work.

---

## 14. Nonvanishing and the whole evaluated error

Norm nonvanishing follows from the nonzero first column and the positive real metric. It does not prevent $29$-adic primitive-norm cancellation.

Mixed nonvanishing retains its supplied original-family dependency. No zero residue in this report is interpreted as a zero integer mixed product.

For


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
$$


the complete same-index evaluated form is still


$$
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n.} \tag{14.1}
$$



At the retained hypotheses and proof status of the complete signed-error theorem,


$$
\epsilon_n>0\quad\text{eventually},
$$




$$
\log|\epsilon_n|
=
-\left(2+\frac1{2001}\right)n\log(1+\sqrt2)+o(n).
\tag{14.2}
$$



The complete exponential residual, logarithmic force, factorial/contact boundary, and exterior endpoint remain part of this error.

An irrationality proof by this construction still needs an infinite sequence of original indices with


$$
0<|q_n(e+\pi)-p_n|\longrightarrow0.
$$


A local force obstruction or a local norm factorization does not establish that statement.

---

# Part V. Bounded exact arithmetic for personal inspection

## 15. Required audit receipts

The following are bounded calculations, not large original-column evaluations.

### A. Turn 4 normal and tail units

**Inputs**


$$
u_0=1,\qquad u_{r+1}=(5+r)u_r
\quad\text{in }\mathbb F_{29},\quad0\le r<24.
$$



**Expected verifiable outputs**


$$
\sum_{r=0}^{24}u_r^2=8,
\qquad
1+16\sum_{r=0}^{24}u_r^2=13
\quad\text{in }\mathbb F_{29}.
$$



These support the unit projector and the partial-normal-norm valuation used in the Turn 4 lift formula.

### B. Turn 4 fixed factorial loss

**Inputs**


$$
B=410910916,\quad
U=822232742919,\quad
V=821821832002.
$$


Evaluate


$$
\sum_{m=1}^{8}\left\lfloor B/29^m\right\rfloor,
$$




$$
\sum_{m=1}^{8}
\left(\left\lfloor U/29^m\right\rfloor-
      \left\lfloor V/29^m\right\rfloor\right).
$$



**Expected verifiable outputs**


$$
F_B=14675386,\qquad E_B=14675390,
$$




$$
2E_B-F_B=14675394.
$$



No factorial itself or original $3^a$ needs to be expanded.

### C. New degree-$27$ obstruction coefficient

This is a finite symbolic calculation over $\mathbb F_{29}$, not a request to reconstruct an original column.

**Inputs**

1. The polynomial
   

$$
R(J)=\frac{J^{29}-J}{(J-2)(J+1)}.
$$


2. Formal variables $\lambda,\Theta_0,\Theta_1$.
3. The endpoint residues $n=0,\ b=27$.
4. The definitions (4.1)–(4.3), restricted to the last $28$ terms modulo $29$, with $H=\lambda R$.

**Expected verifiable output**


$$
R(2)=19,\qquad \frac{27!}{3!}=5,
$$


and


$$
\boxed{
\kappa_H
=
15\lambda(2\Theta_0-\Theta_1)
\quad\text{in }\mathbb F_{29},
}
$$


where


$$
\Theta_0=\theta_{b-26},\qquad
\Theta_1=\theta_{b-25}.
$$



This certifies the coefficient in the actual necessary condition (7.5). It does **not** assign numerical values to those original contact entries.

No repetition of the higher-tail initializer or the 435 bounded auxiliary comparisons is needed.

---

# Conclusion and proof-status ledger

## New results proved here

Subject to the explicitly identified complete-reconstruction inputs and the Turn 4 fixed arithmetic audit:

1. **Exact actual factorial-force recurrence.**  
   Equations (3.1)–(3.3) give a finite-row recurrence with the full factorial boundary source and complete logarithmic remainder retained.

2. **Exact endpoint decomposition of the nearest-neighbor action.**
   

$$
\mathcal K(g)Z_w=\mathcal R\eta_h+\kappa_hE.
$$


   The last finite edge and exterior endpoint are included.

3. **Actual impossibility theorem.**  
   Integral-valued $h$, and in particular every integral-edge polynomial family of degree at most $26$, cannot satisfy the full force equality on the specified deep originally reachable branches.

4. **Explicit constraint on possible nonintegral coefficients.**
   

$$
v_{29}(1-29\kappa_h)
   \ge k-14675394-R_d.
$$


   At the first possible degree $27$, the necessary first residue is (7.5).

5. **An integral weighted orthogonal group identity for the actual columns.**  
   It gives the exact factorization
   

$$
D=29^{2c}\mathfrak a\mathfrak b,\qquad
   2M=29^c(\mathfrak a\mathfrak v+\mathfrak b\mathfrak u),
$$


   with unit-only divisions and all primitive-norm cancellation retained.

## Exact remaining local bottleneck

There are now two sharply distinguished questions.

* For the larger-degree nearest-neighbor escape, the actual first-force data and polynomial coefficients must satisfy the high-precision matching (6.2), and then every remaining complete-force row. This has not been proved or disproved.

* In the saturated weighted reduction, the central missing theorem is
  

$$
\mathfrak v\in\mathfrak b\,\mathbb Z_{29},
$$


  followed by the explicit unit-scale congruence (11.2). Here $\mathfrak v$ is a known complete-force channel and $\mathfrak b$ is the actual primitive-norm factor.

The second is a concrete norm/mixed divisibility problem, not a scalar defined from the desired defect.

## Global proof status

Even a solution of that local problem would leave the full final gcd and actual primitive denominator across all primes to be compared with the whole nonzero error


$$
-q_n\epsilon_n.
$$



Accordingly, this turn supplies an actual skew-family obstruction, a complete factorial-force law, and a division-safe norm/mixed factorization. It does **not** give an unconditional proof or disproof of irrationality of $e+\pi$.
