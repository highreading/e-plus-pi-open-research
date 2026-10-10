> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2, Turn 6 — Complete-force displacement, evaluated terminal residues, and closure of the fixed-degree nearest-neighbor escape

## Executive conclusions

The supplied entrywise logarithmic force makes two additional reductions possible. They materially sharpen Turn 5, but they do **not** prove the desired all-depth divisibility


$$
\mathfrak v\in\mathfrak b\,\mathbb Z_{29}.
$$



The principal results are as follows.

1. **The requested first-force combination is a unit, not zero.** On every original index in the preferred cylinder,
   

$$
\boxed{
   2\theta_{b-26}-\theta_{b-25}
   \equiv-\prod_{\nu\ge0}j_{n_\nu}\not\equiv0\pmod{29},
   }
$$


   where $n=\sum_\nu n_\nu29^\nu$, and the complete, explicitly evaluated table $j_0,\ldots,j_{28}$ appears below. Thus the first matching equation alone does **not** rule out degree $27$.

2. **The complete second force has an independently evaluated terminal contact residue**
   

$$
\boxed{\psi_{b-1}\equiv0\pmod{29}.}
$$


   More generally, $\psi_j\equiv0\pmod{29}$ whenever $j\bmod29\le26$. This uses the full factorial tail and the actual logarithmic force, followed by the actual finite contact inverse.

3. **That terminal residue closes the fixed-degree nonintegral-polynomial escape on sufficiently deep original refinements.** The full nearest-neighbor identity forces
   

$$
\boxed{1-29\kappa_h\equiv8\pmod{29},}
$$


   whereas the deep contact coordinate from Turn 4 requires $1-29\kappa_h$ to acquire arbitrarily high valuation if $h$ has uniformly bounded coefficient denominators.

   Consequently:

   * integral-valued $h$ is impossible at **every original index**, not merely on deep refinements;
   * for every fixed polynomial degree $d$, integral edge coefficients do not rescue the family on sufficiently deep originally reachable refinements;
   * in particular, the degree-$27$ escape is impossible when
     

$$
v_{29}(b-B)>14675394.
$$



   This is a complete-force obstruction to the proposed operator family. It is **not** a disproof of scalar norm/mixed alignment.

4. **The logarithmic force is exactly homogeneous for the finite interior recurrence.** It is not merely negligible to a fixed precision. The complete force obeys an exact displacement identity beginning at row $i=1$, with no negative contact index:
   

$$
\boxed{
   \mathcal D A=-\mathcal V C,\qquad
   \mathcal D f^0=0,\qquad
   \mathcal D\mathbf r=\mathcal V e_b.
   }
$$


   Here every matrix and boundary is specified below. The complete logarithmic contribution survives in exactly two initial force entries.

5. **The actual unprojected weighted columns lie in an explicitly defined three-dimensional rational space.** This gives an exact three-column reduction of the norm/mixed problem. A saturated adjoint version extracts a norm-proportional contribution with an independently determined coefficient:
   

$$
\boxed{
   29^3\mathfrak v
   =
   \frac{r_0}{f^0_0}\,29^{c+2}\mathfrak b+\mathcal E_{\mathrm{force}}.
   }
$$


   The residual $\mathcal E_{\mathrm{force}}$ is evaluated in terms of two complete initial force entries, the explicit factorial boundary column, and the true exterior endpoint. No coefficient is defined from $M/D$.

The remaining local theorem is precisely


$$
\boxed{\mathcal E_{\mathrm{force}}\in29^3\mathfrak b\,\mathbb Z_{29},}
$$


followed by the unit-scale congruence retained from Turn 5. Neither is proved here.

No tools were executed. The irrationality or rationality of $e+\pi$ remains unresolved.

---

# 1. Original domain, accepted scope, and notation

Retain


$$
p=29,\qquad
a=432827+682892t,\qquad t\ge0,
$$




$$
b=3^a,\qquad n=2001b,
$$


and the preferred original cylinder


$$
t\equiv364\pmod{841}.
$$



The weighted coordinates are exactly


$$
0\le j\le b,
$$


and the contact coordinates are exactly


$$
0\le i,j<b.
$$



Write


$$
W_j=\binom{n+2}{j},\qquad
\omega_j=j!W_j,
$$


and let $C$ be the finite reconstruction matrix


$$
(Cx)_j=jx_{j-1}-x_j,\qquad x_{-1}=x_b=0.
$$


Thus


$$
\mathcal R=\operatorname{diag}(W_j)C.
$$



The actual contact system is


$$
A=\widetilde N(I+S)^n,\qquad
A\theta=f^0,\qquad A\psi=\mathbf r,
$$


with


$$
Z_w=\mathcal R\theta,\qquad
Y=\mathcal R\psi+W_be_b.
$$


The normalized columns are


$$
P=Z_w/p^2,\qquad Q=Y/p^3,
$$


and


$$
D=P^TP,\qquad M=P^TQ.
$$



The complete force is


$$
\mathbf r=
\frac{h^e+h^F-\widetilde N(I+S)^n(j!)_{0\le j<b}}{b!}.
$$


Nothing in the argument removes its factorial subtraction, logarithmic term, or exterior $+1$.

I reuse the accepted facts


$$
A,A^{-1}\in M_b(\mathbb Z_p),\qquad
\theta,\psi\in\mathbb Z_p^b,
$$


and the fixed-depth conclusions


$$
D\equiv5C_n^2\mathcal T\pmod{p^4},\qquad
M-\rho_nD\equiv0\pmod{p^4},
\quad \rho_n=(6C_n)^{-1}.
$$


They are not extended to an all-depth relative statement.

A4turn13 accepts the actual projection and contact-lift loss. The coordinator’s certificate independently verifies the fixed constants. Accordingly, I reuse


$$
\ell_j=\frac{\omega_b}{\omega_j},\qquad
\mathscr S=\ell^T\ell\equiv8\pmod{29},
\qquad
\Pi=I-\frac{\ell\ell^T}{\mathscr S},
$$


and


$$
E=W_be_b-\frac{W_b}{\mathscr S}\ell=\mathcal R\xi,
$$




$$
\xi_j=\frac{j!}{b!\mathscr S}\sum_{i=0}^j\ell_i^2.
$$


For


$$
B=410910916,\qquad k=v_p(b-B)\ge9,
$$


the accepted original-coordinate formula is


$$
\boxed{
v_p(\xi_{b-B-1})=14675394-k.
}
\tag{1.1}
$$



The direct contact lift of $Q^\parallel=\Pi Q$ is $(\psi+\xi)/p^3$; the vector $\psi+\xi$ reconstructs $Y^\parallel$.

---

# 2. Entrywise evaluation of the complete logarithmic force

This section replaces the previously unevaluated symbol $h^F$ by an explicit recurrence and a valuation bound.

Put


$$
\phi(z)=1-z+\frac{z^2}{2},
\qquad
F(z)=4\arctan\frac{z}{2-z}.
$$


Direct differentiation gives


$$
\boxed{\phi(z)F'(z)=2.}
\tag{2.1}
$$



Define


$$
u_m=[z^m]\phi(z)^{-1}.
$$


Then


$$
u_0=u_1=1,\qquad
u_m=u_{m-1}-\frac12u_{m-2}\quad(m\ge2).
\tag{2.2}
$$


In particular, every $u_m$ is $29$-integral.

For $q\ge1$,


$$
[z^q]F(z)=\frac{2u_{q-1}}q.
$$


Consequently, if


$$
L_m=m!\,[z^m]\frac{F(z)}{1-z},
$$


then


$$
\boxed{
L_0=0,\qquad
L_m=2m!\sum_{q=1}^m\frac{u_{q-1}}q.
}
\tag{2.3}
$$


Equivalently,


$$
L_m=mL_{m-1}+d_m,
\qquad
d_m=2(m-1)!u_{m-1}\quad(m\ge1).
\tag{2.4}
$$



Using the supplied entrywise definition, the entire divided logarithmic force is therefore


$$
\boxed{
r_i^F
=
\frac{2(n+i)!\,n!}{b!}
\sum_{s=0}^{\min(2n,n+i)}
a_s(n)
\binom{2n+i-s}{n}
\sum_{q=1}^{2n+i-s}\frac{u_{q-1}}q,
}
\tag{2.5}
$$


where $a_s(n)=[z^s]\phi(z)^n$.

This is an entrywise formula for the actual force, including every summation term.

## 2.1 A whole-force valuation bound

Let $F_m=v_p(m!)$. Equation (2.5) gives, for every actual contact row,


$$
v_p(r_i^F)
\ge
F_{n+i}+F_n-F_b-\left\lfloor\log_p(2n+i)\right\rfloor.
$$


Thus


$$
\boxed{
r^F\in p^{N_{\log}}\mathbb Z_p^b,\qquad
N_{\log}:=
2F_n-F_b-\left\lfloor\log_p(2n+b-1)\right\rfloor.
}
\tag{2.6}
$$



Here $N_{\log}>0$ throughout the original family. For example,


$$
F_n\ge n/29=69b,\qquad F_b\le b/28,
$$


whereas the logarithm grows much more slowly.

This bound justifies reducing the complete logarithmic force to zero modulo $29$ below. It does **not** justify deleting it at arbitrary precision relative to a possibly deeply cancelling primitive norm.

---

# 3. The actual first-force terminal combination

## 3.1 Reduction of the finite contact inverse

Let


$$
\mathsf P_{ij}=\binom ij,\qquad 0\le i,j<b.
$$


The supplied contact formula gives


$$
\widetilde N_{ij}
=
\sum_s a_s(n)(n+i)_{\underline s}\binom{n+i-s}{j}.
$$



Since $p\mid n$,

* $a_s(n)\equiv0\pmod p$ for $1\le s<p$;
* $(n+i)_{\underline s}\equiv0\pmod p$ for $s\ge p$.

Hence


$$
\widetilde N_{ij}\equiv\binom{n+i}{j}\pmod p.
$$


Finite Vandermonde convolution gives


$$
\left(\binom{n+i}{j}\right)_{i,j}
=
\mathsf P(I+S)^n.
$$


Therefore


$$
\boxed{
A^{-1}\equiv(I+S)^{-2n}\mathsf P^{-1}\pmod p.
}
\tag{3.1}
$$



All matrices here retain their actual $b\times b$ boundaries.

## 3.2 Reduction of the first force

Write


$$
J_i=[t^n](1+2t+2t^2)^n(1+t)^i,
\qquad
f_i^0=\frac{(n+i)!}{n!}J_i.
$$


Put $J=J_0$.

For $0\le i<p$, Frobenius and $p\mid n$ imply


$$
J_i\equiv J\pmod p.
$$


For $i\ge p$, the factorial quotient contains $n+p$, so


$$
f_i^0\equiv0\pmod p.
$$


Thus


$$
f_i^0\equiv
\begin{cases}
i!J,&0\le i<p,\\
0,&p\le i<b.
\end{cases}
\tag{3.2}
$$



Using the inverse Pascal matrix,


$$
(\mathsf P^{-1}f^0)_j
\equiv
(-1)^jJ
\sum_{r=0}^{j\bmod p}(-1)^r(j\bmod p)_{\underline r}
\pmod p.
\tag{3.3}
$$



For $b-p\le j<b$, the remaining upper-shift distance is less than $p$, and $(I+S)^{-2n}$ has no nonconstant coefficient in that range modulo $p$. Consequently (3.3) is already the actual $\theta_j$ there.

Since $b\equiv27\pmod{29}$,


$$
b-26\equiv1,\qquad b-25\equiv2\pmod{29}.
$$


The two short sums are


$$
1-1=0,\qquad 1-2+2=1.
$$


Moreover $b$ is odd, so $b-25$ is even. Therefore


$$
\boxed{
\theta_{b-26}\equiv0,\qquad
\theta_{b-25}\equiv J\pmod{29}.
}
\tag{3.4}
$$



It remains to evaluate whether $J$ is a unit.

## 3.3 Complete digit evaluation of $J\bmod29$

Define the fixed coefficients


$$
j_r=[t^r](1+2t+2t^2)^r,\qquad0\le r\le28.
$$


They satisfy


$$
j_0=1,\qquad j_1=2,
$$




$$
(r+1)j_{r+1}=2(2r+1)j_r+4rj_{r-1}.
\tag{3.5}
$$



Their complete residues are


$$
\boxed{
\begin{aligned}
(j_r)_{r=0}^{28}\equiv(
&1,2,8,3,20,12,14,2,13,24,22,21,21,20,6,\\
&7,17,19,6,16,4,2,2,18,25,14,15,14,1)
\pmod{29}.
\end{aligned}}
\tag{3.6}
$$


Every entry is nonzero.

To justify the digit product, write


$$
J=[t^0](t^{-1}+2+2t)^n.
$$


At the lowest base-$29$ digit, the exponent range is contained in $[-28,28]$. The only exponent in that range divisible by $29$ is zero. Frobenius therefore separates the constant coefficient one digit at a time:


$$
\boxed{
J\equiv\prod_{\nu\ge0}j_{n_\nu}\pmod{29},
\qquad n=\sum_{\nu\ge0}n_\nu29^\nu.
}
\tag{3.7}
$$


This proves uniformly, without selecting or sampling higher digits,


$$
J\in\mathbb Z_{29}^{\times}.
$$



Combining (3.4)–(3.7),


$$
\boxed{
2\theta_{b-26}-\theta_{b-25}
\equiv-\prod_{\nu\ge0}j_{n_\nu}
\in\mathbb F_{29}^{\times}.
}
\tag{3.8}
$$



The supplied low digits are $n_0,n_1,n_2,n_3=0,7,24,7$, whose contribution is


$$
j_0j_7j_{24}j_7=13.
$$


Thus an equivalent evaluated formula is


$$
2\theta_{b-26}-\theta_{b-25}
\equiv16\prod_{\nu\ge4}j_{n_\nu}\pmod{29}.
$$



This is an exact actual-index digit formula, not a claim that the cylinder fixes one constant residue independently of its higher digits. It decisively establishes nonvanishing.

---

# 4. The complete second force through the actual inverse

Let


$$
T_m=\frac1{b!}\sum_{q=b}^m(m)_{\underline q}.
$$


Then


$$
r_i^e=\sum_s a_s(n)(n+i)_{\underline s}T_{2n+i-s}.
$$



Each $T_m$ is integral. Modulo $29$, only $s=0$ survives, so


$$
r_i^e\equiv T_{2n+i}\pmod{29}.
$$


Also


$$
T_m=\sum_{q=b}^m\binom mq\frac{q!}{b!}.
$$


Because $b\equiv27\pmod{29}$, all terms with $q\ge b+2$ vanish modulo $29$. Hence


$$
\boxed{
r_i
\equiv
\binom{2n+i}{b}-\binom{2n+i}{b+1}
\pmod{29}.
}
\tag{4.1}
$$


The logarithmic contribution vanishes here by the proved whole-force bound (2.6), not by omission.

Lucas’s theorem shows that the right side is zero whenever


$$
i\bmod29\le26.
$$


Thus the complete force is supported modulo $29$ only on row residues $27,28$.

The inverse Pascal matrix preserves this support condition: if $j\bmod29\le26$, then


$$
\binom ji\equiv0\pmod{29}
$$


for every potentially nonzero force entry $r_i$. The remaining upper operator in (3.1) has nonzero coefficients only at offsets divisible by $29$, and therefore also preserves the low residue.

We obtain the actual complete-contact result


$$
\boxed{
\psi_j\equiv0\pmod{29}
\quad\text{whenever }j\bmod29\le26.
}
\tag{4.2}
$$


In particular,


$$
\boxed{\psi_{b-1}\equiv0\pmod{29}.}
\tag{4.3}
$$



Consequently the true exterior endpoint satisfies


$$
\boxed{
Y_b/W_b=1+b\psi_{b-1}\equiv1\pmod{29}.
}
\tag{4.4}
$$


The exterior $+1$ is essential to this residue.

---

# 5. Closure of the fixed-degree nearest-neighbor escape

Consider Turn 5’s family


$$
g_j=(j+1)(n+2-j)h(j),\qquad0\le j<b,
$$


with integral edges $g_j$, and let $\mathcal K(g)=\Pi\mathcal A(g)\Pi$.

Retain the exact definitions


$$
t_i(h)=
\mathbf1_{i<b}(n+2-i)^2h(i)q^\theta_{i+1}
-\mathbf1_{i>0}i^2h(i-1)q^\theta_{i-1},
$$




$$
q^\theta_i=i\theta_{i-1}-\theta_i,
$$




$$
\eta_{h,j}=-j!\sum_{i=0}^j\frac{t_i(h)}{i!},
\qquad
\kappa_h=\sum_{i=0}^b\frac{b!}{i!}t_i(h).
$$



Direct telescoping verifies the endpoint-exact formulas


$$
\mathcal R\eta_h=\mathcal A(g)Z_w-\kappa_hW_be_b,
$$




$$
\mathcal K(g)Z_w=\mathcal R(\eta_h+\kappa_h\xi).
$$


Thus the proposed full-force equality is equivalent to


$$
\boxed{
(1-p\kappa_h)\xi
=ps_n\theta+p\eta_h-\psi.
}
\tag{5.1}
$$



## 5.1 The terminal row forces a unit, not deep matching

At the last contact coordinate,


$$
b\eta_{h,b-1}=t_b(h)-\kappa_h,
\qquad
b\xi_{b-1}=1-\frac1{\mathscr S}.
$$


Substituting these into (5.1) gives


$$
\boxed{
1-p\kappa_h
=
\mathscr S\left(
1+b\psi_{b-1}
-ps_nb\theta_{b-1}
-pt_b(h)
\right).
}
\tag{5.2}
$$



Integral edge coefficients imply $h(b-1)\in\mathbb Z_p$, because


$$
g_{b-1}=b(n+3-b)h(b-1),
$$


and


$$
b(n+3-b)\equiv27\cdot5\not\equiv0\pmod{29}.
$$


Therefore $t_b(h)$ is integral.

For every integral $s_n$, equations (4.3) and (5.2) now give


$$
\boxed{
1-p\kappa_h\equiv\mathscr S\equiv8\pmod{29}.
}
\tag{5.3}
$$


Equivalently,


$$
\boxed{p\kappa_h\equiv22\pmod{29}.}
\tag{5.4}
$$



This conclusion comes from the actual complete force and the genuine last coordinate. It cannot be inferred from a scalar norm residue.

## 5.2 Integral-valued $h$ is impossible everywhere in the original family

If $h$ is integral-valued at every actual edge, then all $t_i(h)$ are integral and hence


$$
\kappa_h\in\mathbb Z_p.
$$


But then $1-p\kappa_h\equiv1\pmod p$, contradicting (5.3).

Therefore:

> **Theorem 1 — global original-family obstruction for integral-valued $h$.**  
> At every original index, the proposed nearest-neighbor full-force identity is impossible for integral-valued $h$ and integral $s_n$.

In particular, the degree-$\le26$ integral-edge class is impossible everywhere, since Turn 5’s unit-Vandermonde argument makes its polynomial coefficients integral.

## 5.3 Every fixed degree is impossible on sufficiently deep refinements

For a fixed degree $d$, retain the interpolation nodes and denominator bound


$$
h\in p^{-C_d}\mathbb Z_p[J],
\qquad
R_d=\max(C_d-1,0),
$$


provided the chosen nodes are actual edge indices.

Then


$$
v_p(\eta_{h,j})\ge-C_d,
$$


so the right side of (5.1) has valuation at least $-R_d$.

By (5.3), $1-p\kappa_h$ is a unit. At the actual coordinate $b-B-1$, the left side therefore has valuation


$$
14675394-k.
$$


This is less than $-R_d$ whenever


$$
k>14675394+R_d.
$$



We have proved:

> **Theorem 2 — fixed-degree integral-edge obstruction.**  
> Fix $d$. Once the interpolation nodes lie in the actual edge range, no polynomial $h\in\mathbb Q_{29}[J]$ of degree at most $d$, with all actual edges $g_j$ integral, can satisfy the full-force identity at an original index with
> 

$$
> \boxed{v_{29}(b-B)>14675394+R_d.}
>
$$


> Such refinements are originally reachable by the accepted finite lifting theorem.

The obstruction is no longer merely that high-precision matching remains unverified. The last complete-force row forces that matching to fail.

## 5.4 What happens specifically at degree $27$

For $H=ph$, Turn 5’s residue calculation gives


$$
\overline H=\lambda
\frac{J^{29}-J}{(J-2)(J+1)}
$$


and


$$
\kappa_H
\equiv15\lambda(2\theta_{b-26}-\theta_{b-25})
=-15\lambda J\pmod{29}.
$$



The deep contact coordinate would require


$$
\kappa_H\equiv1,
\qquad
\lambda\equiv27J^{-1}.
$$


The actual terminal row instead requires


$$
\kappa_H\equiv22,
\qquad
\lambda\equiv14J^{-1}.
$$


Since $J$ is a unit, these are incompatible.

Thus the requested combination is nonzero, but the complete endpoint supplies the additional contradiction:


$$
\boxed{
\deg h\le27,\quad g_j\in\mathbb Z_{29}
\quad\Longrightarrow\quad
\text{failure when }v_{29}(b-B)>14675394.
}
$$



This does not exclude arbitrary integral nearest-neighbor edges with denominator losses growing without a fixed-degree bound, nor does it exclude more general saturated skew operators.

---

# 6. An exact complete-force recurrence with only two initial entries

The supplied logarithmic definition permits a stronger recurrence statement than Turn 5.

Define


$$
V_m=T_m+\frac{L_m}{b!}.
$$


Then


$$
V_m=mV_{m-1}+\binom mb+\frac{d_m}{b!}.
\tag{6.1}
$$


The complete force is


$$
r_i=\sum_s a_s(n)(n+i)_{\underline s}V_{2n+i-s}.
\tag{6.2}
$$



Let


$$
\mathcal F_n(z)=\sum_{\ell\ge0}V_{n+\ell}\frac{z^\ell}{\ell!},
\qquad
R(z)=\phi(z)^n\mathcal F_n(z).
$$


Then $R_{n+i}=r_i$, in exponential-coefficient notation, and


$$
(1-z)\mathcal F_n'
=
(n+1)\mathcal F_n+G_n+\frac{F^{(n+1)}}{b!},
$$


where


$$
G_n(z)=\sum_{\ell\ge0}\binom{n+\ell+1}{b}\frac{z^\ell}{\ell!}.
$$



Hence


$$
\begin{aligned}
&(1-z)\phi R'
-\bigl[n(1-z)\phi'+(n+1)\phi\bigr]R\\
&\hspace{25mm}
=\phi^{n+1}G_n+
\frac{\phi^{n+1}F^{(n+1)}}{b!}.
\end{aligned}
\tag{6.3}
$$



## 6.1 Why the logarithmic interior source is exactly zero

Set


$$
P_n(z)=\phi(z)^{n+1}F^{(n+1)}(z).
$$


Equation (2.1) gives


$$
P_0=2,\qquad
P_{n+1}=\phi P_n'-(n+1)\phi'P_n.
$$


Therefore


$$
\deg P_n\le n.
$$


It follows that


$$
[z^{n+i}]P_n(z)=0\qquad(i\ge1).
$$



Thus the entire logarithmic force is homogeneous in every retained recurrence row beginning at $i=1$.

The lower boundary is not zero: for example,


$$
n![z^n]P_n(z)
=
(-1)^n2^{1-n}n!(n+1)!.
$$


This is one reason the complete initial force entries must remain.

## 6.2 The finite recurrence

Define


$$
\alpha_i=2n+2i+1,
$$




$$
\beta_i=\frac{(n+i)(n+3i-1)}2,
\qquad
\gamma_i=\frac{(n+i)(n+i-1)(1-i)}2.
$$


For every actual row


$$
1\le i\le b-2,
$$


put


$$
(\mathcal Dx)_i
=
x_{i+1}-\alpha_ix_i+\beta_ix_{i-1}+\gamma_ix_{i-2}.
\tag{6.4}
$$


At $i=1$, $\gamma_1=0$, so this definition introduces **no negative index**.

Then


$$
\boxed{
(\mathcal D\mathbf r)_i
=
\mathcal H_i,
\qquad1\le i\le b-2,
}
\tag{6.5}
$$


where


$$
\boxed{
\mathcal H_i=
\sum_s[z^s]\phi(z)^{n+1}
(n+i)_{\underline s}
\binom{2n+i-s+1}{b}.
}
\tag{6.6}
$$



The complete force is therefore determined by exactly two initial entries,


$$
r_0,\ r_1,
$$


and the full factorial boundary source $\mathcal H_i$. The logarithmic contribution to those two entries is explicitly (2.5).

---

# 7. First-force homogeneity and the actual contact displacement

## 7.1 The first force obeys the same homogeneous recurrence

The coefficient identity


$$
\boxed{
J_i
=
2^n[z^{n+i}]
\frac{\phi(z)^n}{(1-z)^{n+1}}
}
\tag{7.1}
$$


follows by expanding


$$
1+2t+2t^2=(1+t)^2+t^2
$$


and


$$
2\phi(z)=1+(1-z)^2.
$$



Thus


$$
f_i^0=
\frac{2^n}{n!}(n+i)!
[z^{n+i}]
\frac{\phi(z)^n}{(1-z)^{n+1}}.
$$


The differential operator on the left of (6.3) annihilates


$$
\phi(z)^n(1-z)^{-n-1}.
$$


Consequently,


$$
\boxed{\mathcal Df^0=0.}
\tag{7.2}
$$



Also,


$$
f_0^0=J\in\mathbb Z_{29}^{\times}.
\tag{7.3}
$$



## 7.2 Generating polynomials for the actual contact columns

Define


$$
B_j^{(m)}(z)
=
\sum_{k=0}^j\binom m{j-k}\frac{z^k}{k!}.
$$


The supplied contact formula gives the exact actual column representation


$$
\boxed{
A_{ij}
=
(n+i)![z^{n+i}]
\phi(z)^ne^zB_j^{(n)}(z).
}
\tag{7.4}
$$



Two elementary identities are


$$
(B_j^{(n)})'=B_{j-1}^{(n)},
$$


and


$$
\boxed{
(1-z)(B_j^{(n)})'-(n+z)B_j^{(n)}
=
B_j^{(n+1)}-(j+1)B_{j+1}^{(n+1)}.
}
\tag{7.5}
$$


The latter includes $j=0$, with $B_{-1}=0$.

Define the finite rectangular matrix


$$
\boxed{
\mathcal V_{ik}
=
(n+i)![z^{n+i}]
\phi(z)^{n+1}e^zB_k^{(n+1)}(z),
}
\tag{7.6}
$$


with exactly


$$
1\le i\le b-2,\qquad0\le k\le b.
$$



Applying (6.3) to each actual contact column and using (7.5) proves


$$
\boxed{\mathcal DA=-\mathcal VC.}
\tag{7.7}
$$



There is no omitted final column: $k=b$ is required when $j=b-1$.

Finally,


$$
G_n(z)=e^zB_b^{(n+1)}(z),
$$


so


$$
\boxed{\mathcal H=\mathcal Ve_b.}
\tag{7.8}
$$



Combining the complete-force equations,


$$
\boxed{
\mathcal V(C\theta)=0,\qquad
\mathcal V(C\psi+e_b)=0.
}
\tag{7.9}
$$



This is an actual finite displacement identity for both complete reconstructed columns.

---

# 8. A three-dimensional exact reduction of the actual columns

The matrix $\mathcal D$ is surjective over $\mathbb Z_{29}$: set the first two entries to zero and solve forward using the coefficient $1$ of $x_{i+1}$.

Since $A$ is invertible over $\mathbb Z_{29}$, equation (7.7) implies that $\mathcal V$ is also surjective. Therefore


$$
\operatorname{rank}\mathcal V=b-2,
\qquad
\dim_{\mathbb Q_{29}}\ker\mathcal V=3.
\tag{8.1}
$$



Let $h^{(0)},h^{(1)}$ be the homogeneous recurrence solutions with initial entries


$$
(h^{(0)}_0,h^{(0)}_1)=(1,0),
\qquad
(h^{(1)}_0,h^{(1)}_1)=(0,1).
$$


Let $\tau$ solve


$$
\mathcal D\tau=\mathcal H,\qquad \tau_0=\tau_1=0.
$$



Define the three actual weighted vectors


$$
B_0=\mathcal RA^{-1}h^{(0)},\qquad
B_1=\mathcal RA^{-1}h^{(1)},
$$




$$
B_*=\mathcal RA^{-1}\tau+W_be_b.
\tag{8.2}
$$



Then, exactly,


$$
\boxed{
Z_w=f_0^0B_0+f_1^0B_1,
}
\tag{8.3}
$$




$$
\boxed{
Y=r_0B_0+r_1B_1+B_*.
}
\tag{8.4}
$$



The first two vectors have zero charge, while $B_*$ has charge $W_b$. They are linearly independent over $\mathbb Q_{29}$. Thus they form an explicit basis of the weighted image of $\ker\mathcal V$.

After applying $\Pi$, the norm/mixed calculation reduces to the Gram matrix of


$$
B_0,\quad B_1,\quad \Pi B_*.
$$


This is an exact three-column reduction, not a truncation.

It does **not** imply that this basis is a saturated integral basis. The factorial reconstruction lattice must still be respected. Nor does a three-dimensional Gram representation by itself supply a primitive-norm factor.

---

# 9. A saturated adjoint identity for the actual transformed channel

Retain Turn 5’s unit-only factorization. Write


$$
P=p^cx,
$$


where $x$ is primitive, and choose the demonstrated unit $\mathfrak a$. The coordinate transformation gives


$$
D=p^{2c}\mathfrak a\mathfrak b,
\qquad
2M=p^c(\mathfrak a\mathfrak v+\mathfrak b\mathfrak u).
\tag{9.1}
$$


Its formulas are verified by expanding


$$
AB+\sum T_j^2
$$


under the stated hyperbolic-coordinate shear. No norm factor follows merely from this isometry.

Let $d$ be the integral coefficient vector of the linear functional defining $\mathfrak v$:


$$
\mathfrak v(y)=d^Ty.
$$


Thus


$$
d^Tx=\mathfrak b,\qquad
\mathfrak v=d^TQ^\parallel.
$$



Define the actual saturated adjoint solution


$$
\boxed{
A^Tz=\mathcal R^T\Pi d.
}
\tag{9.2}
$$


All entries of $z$ are $29$-integral.

It follows immediately that


$$
\boxed{
z^Tf^0=p^{c+2}\mathfrak b,
}
\tag{9.3}
$$


and


$$
\boxed{
p^3\mathfrak v
=
z^T\mathbf r+W_b(\Pi d)_b.
}
\tag{9.4}
$$



The endpoint term in (9.4) is retained exactly.

## 9.1 Elimination down to two initial force entries

There are unique $\lambda_1,\ldots,\lambda_{b-2}$ and $\eta_0,\eta_1$ such that


$$
z=\mathcal D^T\lambda+\eta_0e_0+\eta_1e_1.
\tag{9.5}
$$



They are obtained without nonunit division. With $\lambda_i=0$ outside $1\le i\le b-2$, solve backward for $j=b-1,\ldots,2$:


$$
\boxed{
\lambda_{j-1}
=
z_j+\alpha_j\lambda_j
-\beta_{j+1}\lambda_{j+1}
-\gamma_{j+2}\lambda_{j+2}.
}
\tag{9.6}
$$


The two true lower boundary coefficients are


$$
\boxed{
\eta_0=z_0-\beta_1\lambda_1-\gamma_2\lambda_2,
}
\tag{9.7}
$$




$$
\boxed{
\eta_1=z_1+\alpha_1\lambda_1
-\beta_2\lambda_2-\gamma_3\lambda_3.
}
\tag{9.8}
$$



Since $\mathcal Df^0=0$ and $\mathcal D\mathbf r=\mathcal H$,


$$
p^{c+2}\mathfrak b
=\eta_0f_0^0+\eta_1f_1^0,
\tag{9.9}
$$




$$
p^3\mathfrak v
=\eta_0r_0+\eta_1r_1
+\sum_{i=1}^{b-2}\lambda_i\mathcal H_i
+W_b(\Pi d)_b.
\tag{9.10}
$$



Every complete logarithmic contribution is now in the two explicitly defined entries $r_0,r_1$. Every interior factorial boundary contribution is in the displayed finite sum.

## 9.2 Extracting a norm-proportional term independently of $D$

Since $f_0^0$ is a demonstrated unit, eliminate $\eta_0$ using (9.9). This gives


$$
\boxed{
p^3\mathfrak v
=
\frac{r_0}{f_0^0}\,p^{c+2}\mathfrak b
+\mathcal E_{\mathrm{force}},
}
\tag{9.11}
$$


where


$$
\boxed{
\begin{aligned}
\mathcal E_{\mathrm{force}}
={}&
\eta_1\left(r_1-\frac{f_1^0}{f_0^0}r_0\right)\\
&+\sum_{i=1}^{b-2}\lambda_i\mathcal H_i
+W_b(\Pi d)_b.
\end{aligned}
}
\tag{9.12}
$$



The scalar $r_0/f_0^0$ is determined from the first complete force row and a proved unit. It is not $M/D$, nor a renamed defect quotient.

Equation (4.1) gives $r_0\in p\mathbb Z_p$. Therefore


$$
p^{c-1}\frac{r_0}{f_0^0}\in\mathbb Z_p.
$$


Since the actual $\mathfrak v$ is integral, (9.11) also proves


$$
\mathcal E_{\mathrm{force}}\in p^3\mathbb Z_p.
$$



Most importantly,


$$
\boxed{
\mathfrak v\in\mathfrak b\mathbb Z_p
\quad\Longleftrightarrow\quad
\mathcal E_{\mathrm{force}}\in p^3\mathfrak b\mathbb Z_p.
}
\tag{9.13}
$$



This is the new reduced force-channel obligation.

The associated adjoint displacement is also exact:


$$
\boxed{
C^T\left(
\operatorname{diag}(W_j)\Pi d+\mathcal V^T\lambda
\right)
=
A^T(\eta_0e_0+\eta_1e_1).
}
\tag{9.14}
$$


In particular, the last component of the vector in parentheses is exactly the last two terms of (9.12). Thus the factorial boundary and exterior endpoint have been combined by an actual displacement identity, not dropped.

---

# 10. What is still missing for relative alignment

The factorization retains


$$
v_p(D)=2c+v_p(\mathfrak b).
$$


Since the actual first column is nonzero and its real norm is positive,


$$
D>0,\qquad \mathfrak b\ne0.
$$


No bound on $v_p(\mathfrak b)$ follows from positivity.

The desired all-depth relative statement still requires:

1. the additional divisibility
   

$$
\mathcal E_{\mathrm{force}}\in p^3\mathfrak b\mathbb Z_p;
$$


2. after this is proved, the unit-scale congruence
   

$$
\mathfrak a\frac{\mathfrak v}{\mathfrak b}
   +\mathfrak u-2\rho_np^c\mathfrak a
   \in p^{c+1}\mathbb Z_p.
$$



The three-dimensional reduction and the adjoint recurrence make these obligations explicit. They do not establish them.

A concrete follow-on lemma is now:

> **Reduced complete-force norm-factor lemma — open.**  
> For the actual $A,\mathcal V,\theta,d,z,\lambda,\eta_1$ defined above, prove
> 

$$
> \eta_1\left(r_1-\frac{f_1^0}{f_0^0}r_0\right)
> +\sum_{i=1}^{b-2}\lambda_i\mathcal H_i
> +W_b(\Pi d)_b
> \in29^3\mathfrak b\,\mathbb Z_{29},
>
$$


> and then establish the stated unit-scale congruence. The two initial force values must be the complete values from (2.5) and (6.2).

This is narrower than a general search for a skew operator: the logarithmic interior has been eliminated exactly, the factorial source is a specified contact boundary column, and only two complete initial force entries remain.

The fixed-degree nearest-neighbor family cannot supply a uniform solution on the deep original refinements proved above.

---

# 11. Finite boundaries, content, final gcd, and whole error

No high block has been extended. If the retained block size is $L=29^4$, the terminal block remains


$$
Lh\le j\le b,
$$


rather than a full block of length $L$. The accepted normal current still has both genuine exterior currents zero. All new recurrences stop at $i=b-2$, whose leading force entry is $r_{b-1}$.

The common contents and primitive-norm cancellation remain separate. In particular,


$$
D=p^{2c}\mathfrak a\mathfrak b
$$


retains the entire primitive-norm valuation in $\mathfrak b$. The new force reduction does not replace that factor by column content.

Retain the least actual two-column clearer


$$
N_B=d_B[u,v],\qquad v_{29}(d_B)=0,
$$


and the actual integer Gram pair


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2}.
$$


The final normalization is still


$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
p_n=H_B/g_B,\qquad q_n=A_B/g_B>0.
}
$$


The primitive multiplier on the rational Gram pair remains $d_B^2/g_B$.

With


$$
\delta=v_{29}(D),\qquad\mu=v_{29}(M),
$$


the retained exact local interface is


$$
v_{29}(g_B)
=
\min\{4F_n+4+\delta,\ 2F_n+F_b+5+\mu\},
$$




$$
v_{29}(q_n)
=
\max\{0,\ 2F_n-F_b-1+\delta-\mu\}.
$$


The present report does not evaluate $\delta-\mu$ at all depths, and it supplies no all-prime bound for the actual $q_n$.

Mixed nonvanishing retains its supplied original-family dependency. A zero residue is not interpreted as a zero mixed integer.

For


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
$$


the whole evaluated error is


$$
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n.}
$$


At the retained hypotheses and proof status of the complete signed-error theorem,


$$
\epsilon_n>0\quad\text{eventually},
$$




$$
\log|\epsilon_n|
=
-\left(2+\frac1{2001}\right)n\log(1+\sqrt2)+o(n).
$$


Neither the new obstruction nor the reduced channel identity proves that the whole nonzero form tends to zero.

---

# 12. Bounded exact arithmetic for personal inspection

The accepted normal constants and Legendre receipts do not need to be repeated.

## A. First-force digit table

**Inputs**

Work in $\mathbb F_{29}$, with


$$
j_0=1,\quad j_1=2,
$$




$$
j_{r+1}
=
(r+1)^{-1}\bigl(2(2r+1)j_r+4rj_{r-1}\bigr),
\qquad1\le r\le27.
$$



**Expected verifiable output**

The 29-entry table (3.6), with no zero entry.

This finite calculation certifies the fixed coefficient table. The uniform original-family conclusion follows separately from the proved digit-product identity (3.7).

## B. Degree-$27$ compatibility screen

**Inputs**

* the table above;
* $R(J)=(J^{29}-J)/((J-2)(J+1))$;
* $R(2)=19$;
* the already proved coefficient
  

$$
\kappa_H=15\lambda(2\theta_{b-26}-\theta_{b-25});
$$


* the complete terminal residues
  

$$
\psi_{b-1}=0,\qquad \mathscr S=8
  \quad\text{in }\mathbb F_{29}.
$$



**Expected verifiable output**



$$
2\theta_{b-26}-\theta_{b-25}=-J,
$$




$$
\lambda_{\mathrm{deep}}=27J^{-1},
\qquad
\lambda_{\mathrm{endpoint}}=14J^{-1},
$$


which are unequal.

This checks the small arithmetic in the degree-$27$ contradiction. Reachability and the depth threshold remain supplied by the symbolic proof, not by this finite screen.

## C. Optional exact implementation check of the displacement

For an implementation check only, use $n=6,b=4$, form the complete rational matrices and force entries from the supplied formulas, and verify


$$
\mathcal DA=-\mathcal VC,\qquad
\mathcal Df^0=0,\qquad
\mathcal D\mathbf r=\mathcal Ve_b
$$


in rows $i=1,2$.

The expected output is exact zero for all three residuals, with the logarithmic coefficients generated from (2.2)–(2.3). This is a bounded check of formulas, **not** evidence about an original-family norm factor. The all-$n,b$ identities are established symbolically above.

---

# Final proof-status ledger

## New results proved from the complete finite reconstruction

1. The actual first-force combination is explicitly evaluated and is always a unit:
   

$$
2\theta_{b-26}-\theta_{b-25}
   \equiv-\prod_\nu j_{n_\nu}\ne0\pmod{29}.
$$



2. The complete second force, passed through the actual finite inverse, satisfies
   

$$
\psi_j\equiv0\pmod{29}\quad(j\bmod29\le26),
$$


   in particular at $j=b-1$.

3. The complete terminal row forces
   

$$
1-29\kappa_h\equiv8\pmod{29}.
$$


   This rules out integral-valued $h$ at every original index and every fixed-degree integral-edge polynomial family on the stated deep original refinements.

4. The complete logarithmic force is exactly homogeneous for the finite recurrence in rows $1,\ldots,b-2$. Its full contribution remains in two initial entries.

5. The exact contact displacement
   

$$
\mathcal DA=-\mathcal VC,\qquad
   \mathcal Df^0=0,\qquad
   \mathcal D\mathbf r=\mathcal Ve_b
$$


   gives a three-dimensional actual-column reduction.

6. The saturated adjoint reduction extracts a norm-proportional channel term with coefficient $r_0/f_0^0$, determined independently of $D$, and leaves the fully specified residual (9.12).

## Exact remaining local bottleneck

Prove or genuinely refute


$$
\boxed{\mathcal E_{\mathrm{force}}\in29^3\mathfrak b\,\mathbb Z_{29}}
$$


for the actual complete force, and then prove the retained unit-scale congruence.

The coordinate isometry alone does not imply this divisibility. The fixed-degree nearest-neighbor family is now rigorously unavailable as a uniform mechanism on the deep refinements.

## Global status

Even an affirmative solution of the local channel lemma would leave the full all-prime gcd, the actual primitive denominator, and the whole nonzero same-index error to be compared.



$$
\boxed{
\text{No unconditional proof or disproof of irrationality of }e+\pi
\text{ is obtained.}
}
$$


