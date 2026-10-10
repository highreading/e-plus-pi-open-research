> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Matched $b=5$: carry-correct root-disk reduction and a constructive subfamily exclusion

The completed controls do **not** give a whole-family exclusion. They do, however, give enough prime mass for an explicit positive-density subfamily exclusion once all prime conditions are imposed on the **same indices**.

The main new local result below is more specific: on each of the two genuine disks


$$
2+7\mathbb Z_7,\qquad 3+7\mathbb Z_7,
$$


the normalized contraction has a carry-correct restricted-analytic expansion


$$
\boxed{\;
\widetilde V(r+7T)
=\widetilde V_r+7\Lambda_rT+49G_r(T),
\qquad G_r\in\mathbb Z_7\langle T\rangle .
\;}
\tag{1}
$$


The coefficient carry in the **scalar state** is generally nonzero. It disappears from (1) only because it is a common scalar rescaling and $\widetilde V_r\equiv0\pmod7$.

Thus four new prime-square evaluations—not a new prime atlas—will determine whether these two disks contain simple $7$-adic roots or instead have uniformly bounded valuation. I give the exact finite criterion and the currently unevaluated coefficients below. I do **not** claim that the existence or arithmetic nature of those roots has already been settled.

Separately, I prove a general contiguous replacement mechanism for the high rows. It removes an explicit triangular family of universal factors for each fixed matched $b$, without claiming that these exhaust all evaluated content.

Throughout, the actual approximation family is


$$
(n,5,n),\qquad\text{contact order }2n+6,\qquad n\ge5.
$$


Indices below $5$ are scalar seeds only.

---

## 1. Normalization, full evaluated content, and the actual denominator

Use the integral replacement-basis contractions from the supplied $b=5$ construction:


$$
(\widetilde\sigma_n,\widetilde\chi_n,\widetilde\kappa_n),
\qquad
\widetilde V_n
=\widetilde\sigma_n\mathcal A_n
-\widetilde\chi_n\mathcal B_n-\widetilde\kappa_n,
$$


where


$$
\mathcal B_n=\mathcal M_n+h_n-u_n.
$$



No further numerical factor is divided out on the strength of the symbolic coefficient calculation. Define the **full evaluated contraction gcd**


$$
d_n=\gcd\bigl(
|\widetilde\sigma_n|,
|\widetilde\chi_n|,
|\widetilde\kappa_n|
\bigr).
\tag{2}
$$


When the triple is nonzero, put


$$
(\sigma_n^*,\chi_n^*,\kappa_n^*)
=d_n^{-1}
(\widetilde\sigma_n,\widetilde\chi_n,\widetilde\kappa_n).
$$


In the raw convention of the supplied construction, the exact contraction gcd is therefore


$$
\boxed{
\gcd(|\sigma_n^{\rm raw}|,|\chi_n^{\rm raw}|,|\kappa_n^{\rm raw}|)
=
1152(n+3)(2n+5)(2n+7)d_n.
}
\tag{3}
$$



The completed joint-zero checks, together with the already proved normalized transfer, imply


$$
v_p(d_n)=0
\quad
(n\ge0,\ p\in\{7,11,13,17,19\}).
\tag{4}
$$


This is an infinite consequence of transfer and the supplied finite controls, not a claim that coefficient primitiveness exhausts evaluated content.

In particular,


$$
v_p(V_n^*)=v_p(\widetilde V_n)
\tag{5}
$$


at those primes. Their globally primitive residues need not be periodic; only this valuation statement is needed.

### 1.1 Complete endpoint numerator

Write $\mathsf P_j=L_j(1)$, and use the supplied second-kind endpoints $w_j$. Set


$$
\begin{aligned}
D_n^*&=(n+1)\mathsf P_{n+1}\chi_n^*
                    -2\mathsf P_n\sigma_n^*,\\
Q_n^*&=2w_n\sigma_n^*
                    -(n+1)w_{n+1}\chi_n^*,\\
V_n^*&=\sigma_n^*\mathcal A_n
                    -\chi_n^*\mathcal B_n-\kappa_n^*,\\
S_n^*&=Q_n^*+\frac{2^{n+1}}{(n!)^2}V_n^*.
\end{aligned}
\tag{6}
$$


The exact quotient remains


$$
\boxed{\frac{X_n}{Y_n}=\frac{S_n^*}{D_n^*}},
\qquad n\ge5,\quad D_n^*\ne0.
\tag{7}
$$



In particular, $S_n^*$ retains both second-kind terms and the full $-\kappa_n^*$ contribution. With


$$
f_n=\frac{2^n}{(n!)^2},\qquad
T_P=f_n\mathcal A_n,\qquad
T_U=\frac{2f_n}{n+1}\mathcal B_n,
$$


it is equivalently


$$
S_n^*
=
2(w_n+T_P)\sigma_n^*
-(n+1)(w_{n+1}+T_U)\chi_n^*
-2f_n\kappa_n^*.
\tag{8}
$$



Take the valid clearer


$$
\lambda_n=\operatorname{lcm}\!\left(
(n!)^2,\,
2^n\operatorname{lcm}(1,\ldots,n+1)
\right).
$$


Then


$$
N_n=\lambda_n S_n^*,\qquad Z_n=\lambda_nD_n^*
$$


are integers. The **final endpoint gcd** and actual primitive center are


$$
g_n=\gcd(|N_n|,|Z_n|),
\tag{9}
$$




$$
\boxed{
c_n=-\frac{X_n}{Y_n}=\frac{p_n}{q_n},\qquad
q_n=\frac{|Z_n|}{g_n},\qquad
p_n=-\operatorname{sign}(Z_n)\frac{N_n}{g_n}.
}
\tag{10}
$$


Nothing below identifies $g_n$ with $d_n$.

---

# 2. Restricted-analytic scalar expansions, including the coefficient carry

Put


$$
\phi(z)=1-z+\frac{z^2}{2},\qquad
a_s(x)=[z^s]\phi(z)^x,
$$


where $a_s(x)$ is the rational polynomial defined by the binomial expansion. Let


$$
\mathscr D(x)=\sum_{j\ge0}(x)_j,\qquad x\in\mathbb Z_p.
$$


The scalar functions are extended by the exact sums


$$
\begin{aligned}
h(x)&=\sum_{s\ge0}(x)_sa_s(x),\\
u(x)&=\sum_{s\ge0}(x)_{s+1}a_s(x),\\
v(x)&=\sum_{s\ge0}(x)_{s+2}a_s(x),\\
\mathcal A(x)&=\sum_{s\ge0}(x)_sa_s(x)\mathscr D(2x-s),\\
\mathcal M(x)&=\sum_{s\ge0}(x)_sa_s(x)\mathscr D(2x+1-s).
\end{aligned}
\tag{11}
$$


At nonnegative integers these equal the defining scalar quantities: the falling factorial makes the support finite.

Denote this five-coordinate state by


$$
\mathbf S(x)=(h(x),u(x),v(x),\mathcal A(x),\mathcal M(x)).
$$



## 2.1 Coefficientwise convergence on a residue disk

Fix an odd prime $p$, $0\le r<p$, and write $x=r+pT$. I use the Gauss valuation on $\mathbb Q_p[T]$.

For every $j\ge0$,


$$
v_{\rm G}((r+pT)_j)\ge \left\lfloor\frac jp\right\rfloor,
\tag{12}
$$


because at least that many factors have both coefficients divisible by $p$.

Expand


$$
a_s(x)=\sum_{j=0}^s c_{s,j}\binom{x}{j},
\qquad
c_{s,j}=[z^s](\phi(z)-1)^j\in\mathbb Z_p.
$$


If $m=\lfloor s/p\rfloor$ and $j\le s$, then


$$
\begin{aligned}
v_{\rm G}\!\left((r+pT)_{s+d}\binom{r+pT}{j}\right)
&\ge
m+\left\lfloor\frac jp\right\rfloor-v_p(j!)\\
&=
m-v_p\!\left(\left\lfloor\frac jp\right\rfloor!\right)\\
&\ge m-v_p(m!).
\end{aligned}
\tag{13}
$$


This applies to $d=0,1,2$. The right side tends to infinity with $s$.

Also


$$
\mathscr D(a+pcT)
=\sum_{j\ge0}(a+pcT)_j
\in\mathbb Z_p\langle T\rangle
\tag{14}
$$


for integral $a,c$: its $j$-th summand has Gauss valuation at least $\lfloor j/p\rfloor$.

Consequently all five sums in (11) converge in


$$
\boxed{\mathbf S(r+pT)\in\mathbb Z_p\langle T\rangle^5.}
\tag{15}
$$


This coefficientwise statement is stronger than congruence transfer on integer arguments.

It also supplies a finite, all-depth truncation rule. To compute the state modulo $p^a$ coefficientwise, it is enough to truncate the outer sum before


$$
s=p\left\lceil\frac{a(p-1)}{p-2}\right\rceil
\tag{16}
$$


and each $\mathscr D$-sum before $j=ap$. Indeed,


$$
m-v_p(m!)\ge m\frac{p-2}{p-1}.
$$


No extrapolation from a fixed collection of scalar indices is involved.

## 2.2 The first carry on disks with $2r<p$

Assume now $p\ge5$ and $2r<p$.

For $s<p$, the polynomial $a_s(x)$ has $p$-integral coefficients, so the corresponding terms admit ordinary first-order expansion at $r$.

For $p\le s<2p$, a different contribution occurs. Coefficientwise modulo $p$,


$$
[z^s]\phi(z)^{r+pT}
=
[z^s]\phi(z)^r(1-Tz^p).
\tag{17}
$$


Here is a direct polynomial justification. In the binomial expansion of $\phi(z)^{pT}$, through degree $<2p$,

* $\binom{pT}{j}$ is divisible by $p$ for $1\le j<p$;
* $\binom{pT}{p}\equiv T\pmod p$;
* $\binom{pT}{p+j}$ is divisible by $p$ for $1\le j<p$;
* $(\phi-1)^p\equiv-z^p+z^{2p}/2\pmod p$.

Since $\deg\phi^r=2r<p$, (17) gives


$$
a_{p+j}(r+pT)\equiv-T\,a_j(r)\pmod p.
\tag{18}
$$



On the other hand, Wilson’s theorem gives


$$
\frac{(r+pT)_{p+j+d}}p
\equiv
-T(r)_{j+d}\pmod p
\quad(j+d\le r).
\tag{19}
$$


If $j+d>r$, the product contains a second factor divisible by $p$, so its quotient by $p$ is zero modulo $p$.

Thus the entire range $p\le s<2p$ contributes


$$
pT^2h_r,\quad pT^2u_r,\quad pT^2v_r
$$


to the three jet coordinates modulo $p^2$.

For the integral coordinates, use additionally


$$
\mathscr D(2r+2pT-p-j)\equiv\mathscr D(2r-j)\pmod p
$$


and the analogous formula with $2r+1$. Their carry contributions are


$$
pT^2\mathcal A_r,\qquad pT^2\mathcal M_r.
$$


The terms with $s\ge2p$ vanish modulo $p^2$ by (13).

We have therefore proved the coefficientwise identity


$$
\boxed{
\mathbf S(r+pT)
=
\mathbf S_r+pT\,\mathbf L_r+pT^2\mathbf S_r
+p^2\mathbf E_r(T),
\qquad
\mathbf E_r\in\mathbb Z_p\langle T\rangle^5.
}
\tag{20}
$$



This is the missing small-depth carry. Replacing the scalar state by
$\mathbf S_r+pT\mathbf L_r$ alone is generally incorrect.

### Explicit formula for $\mathbf L_r\bmod p$

For $d=0,1,2$,


$$
(L_r)_d
=
\sum_{s=0}^{p-1}
\left.
\frac{d}{dx}\bigl((x)_{s+d}a_s(x)\bigr)
\right|_{x=r}
\pmod p.
\tag{21}
$$


Writing $w_s(x)=(x)_sa_s(x)$,


$$
\begin{aligned}
(L_r)_{\mathcal A}
&=
\sum_{s=0}^{p-1}
\left[
w_s'(r)\mathscr D(2r-s)
+2w_s(r)\mathscr D'(2r-s)
\right]\pmod p,\\
(L_r)_{\mathcal M}
&=
\sum_{s=0}^{p-1}
\left[
w_s'(r)\mathscr D(2r+1-s)
+2w_s(r)\mathscr D'(2r+1-s)
\right]\pmod p.
\end{aligned}
\tag{22}
$$


The derivative series converges locally. Modulo $p$, its value is obtained by differentiating the finite sum with $j<2p$.

---

# 3. The two $7$-adic disks: explicit scalar tangents and contraction expansion

Both $r=2$ and $r=3$ satisfy $2r<7$, so (20) applies directly.

## 3.1 The scalar tangents

The identity


$$
\mathscr D(x)=1+x\mathscr D(x-1)
$$


implies


$$
\mathscr D'(x)
=
\mathscr D(x-1)+x\mathscr D'(x-1).
\tag{23}
$$


Modulo $7$, this gives


$$
\bigl(\mathscr D'(0),\ldots,\mathscr D'(6)\bigr)
=(4,5,5,6,5,6,5).
\tag{24}
$$


For example, $\mathscr D'(0)\equiv\mathscr D(-1)\equiv\mathscr D(6)=4$.

At $r=2$, the coefficients of $\phi^2$ modulo $7$ are


$$
(1,5,2,6,2),
$$


and the derivatives $a_s'(2)$, for $1\le s\le6$, are


$$
(6,2,4,4,0,5).
$$


These follow by extracting coefficients in


$$
\phi(z)^2\log\phi(z),
$$


using


$$
([z]\log\phi,\ldots,[z^6]\log\phi)
=(6,0,6,1,6,0)\pmod7.
$$


The derivative weights $w_s'(2)$, $0\le s\le6$, are


$$
(0,3,3,5,3,0,0).
$$


Substitution in (21)–(22) yields


$$
\mathbf L_2=(0,0,2,1,0)\pmod7.
$$



Differentiating the exact five-state recurrence transfers this tangent from $2$ to $3$. The result is


$$
\boxed{
\begin{array}{c|ccccc|ccccc}
r&h&u&v&\mathcal A&\mathcal M&
L_h&L_u&L_v&L_{\mathcal A}&L_{\mathcal M}\\ \hline
2&1&5&2&0&4&0&0&2&1&0\\
3&2&5&2&2&4&5&0&5&5&0
\end{array}}
\pmod7.
\tag{25}
$$


These tangent values are new local data, not repetitions of the completed contraction table.

## 3.2 Why the carry cancels from the root contraction

Let


$$
\mathcal V(n,h,u,v,\mathcal A,\mathcal M)
$$


be the fixed rational polynomial defining $\widetilde V$. Its coefficient denominators are units at $7$.

The four high rows are linear in $(h,u,v)$. Consequently:

* $\widetilde\sigma,\widetilde\chi$ are homogeneous of degree $5$ in the scalar state;
* $\widetilde\kappa$ is homogeneous of degree $6$;
* $\mathcal V$ is homogeneous of degree $6$ in all five scalar coordinates.

Euler’s identity therefore gives


$$
\sum_i S_i\frac{\partial\mathcal V}{\partial S_i}=6\mathcal V.
\tag{26}
$$



Substitute (20) into the defining polynomial. Modulo $p^2$,


$$
\widetilde V(r+pT)
=
\widetilde V_r
+pT\Lambda_r
+6pT^2\widetilde V_r,
\tag{27}
$$


where


$$
\Lambda_r
=
\left(
\frac{\partial}{\partial n}
+\sum_i(L_r)_i\frac{\partial}{\partial S_i}
\right)\mathcal V(r,\mathbf S_r)
\pmod p.
\tag{28}
$$



At either supplied $7$-adic root residue, $7\mid\widetilde V_r$. The last term in (27) is therefore divisible by $49$, proving (1).

This cancellation uses the root condition and homogeneity. It is not an assertion that the scalar carry was absent.

## 3.3 The remaining slopes are fixed determinant derivatives

There is a small exact circuit for the two slopes. Define operators acting only on the three contraction polynomials:


$$
\partial_2=\partial_n+2\partial_v,\qquad
\partial_3=\partial_n+5\partial_h+5\partial_v.
$$


Using (25), $\mathcal B=\mathcal M+h-u$, and the supplied contractions at the two root residues,


$$
\boxed{
\Lambda_2
=
6-\partial_2\widetilde\kappa(2,1,5,2)
\pmod7,
}
\tag{29}
$$


and


$$
\boxed{
\Lambda_3
=
2\partial_3\widetilde\sigma
-\partial_3\widetilde\chi
-\partial_3\widetilde\kappa+4
\pmod7,
}
\tag{30}
$$


where the right side of (30) is evaluated at $(n,h,u,v)=(3,2,5,2)$.

I have not evaluated these last fixed determinant derivatives. Claiming numerical values for them would invent the missing computation.

---

# 4. Exact all-depth consequences and the root-classification gap

Put


$$
\beta_r=\frac{\widetilde V_r}{7}\in\mathbb Z.
$$


Equation (1) becomes


$$
\frac{\widetilde V(r+7T)}7
=
\beta_r+\Lambda_rT+7G_r(T).
\tag{31}
$$



## 4.1 Simple-root case

If $\Lambda_r\not\equiv0\pmod7$, then (31) has exactly one root $T_r\in\mathbb Z_7$. Set


$$
\nu_r=r+7T_r.
$$


Moreover,


$$
\boxed{
v_7(\widetilde V_n)=v_7(n-\nu_r)
\quad
(n\in r+7\mathbb Z_7),
}
\tag{32}
$$


with the usual value $+\infty$ at the root.

To prove the exact valuation, for $t,u\in\mathbb Z_7$ write


$$
G_r(t)-G_r(u)=(t-u)H(t,u),
\qquad H(t,u)\in\mathbb Z_7.
$$


Then


$$
\frac{\widetilde V(r+7t)-\widetilde V(r+7u)}7
=(t-u)(\Lambda_r+7H(t,u)).
$$


The last factor is a unit. This proves the isometry, and the unique root follows by ordinary digit-by-digit Hensel lifting.

Thus a nonzero slope proves an **actual infinite-depth $7$-adic root**, not merely a surviving finite residue.

By (5), the same valuation formula holds for $V_n^*$ at ordinary integer indices.

## 4.2 Other first-layer outcomes

If $\Lambda_r\equiv0\pmod7$ but $\beta_r\not\equiv0\pmod7$, then


$$
\boxed{v_7(V_n^*)=1\quad(n\equiv r\pmod7).}
\tag{33}
$$


There is no $7$-adic root in that disk.

If both are zero modulo $7$, then the entire disk has valuation at least $2$. The next coefficient polynomial must be examined. Formulae (15)–(16) give a valid finite truncation at every subsequent depth, but do not predetermine its roots.

These alternatives explain exactly why the completed mod-$7$ rows alone do not determine the root classification.

## 4.3 What is already ruled out about rational factors

The completed symbolic gcd control does imply a useful negative result. There is no nonconstant polynomial $P(n)\in\mathbb Q[n]$ dividing


$$
\mathcal V(n,h,u,v,\mathcal A,\mathcal M)
$$


as a polynomial in its independent variables.

Indeed, such a $P$ would divide the coefficient $\widetilde\sigma$ of $\mathcal A$, the coefficient $-\widetilde\chi$ of $\mathcal M$, and then also $\widetilde\kappa$. This contradicts the constant symbolic gcd.

Thus these disks are not explained by an unremoved universal polynomial factor depending only on $n$.

There is also an evaluated distinction: the all-residue unit prime $19$, combined with transfer, proves


$$
\widetilde V_n\ne0\qquad(n\ge0).
\tag{34}
$$


Consequently, if the simple roots in §4.1 exist, neither is a **nonnegative rational integer**.

This does **not** determine whether such a root could be a negative integer, a nonintegral rational number, or an irrational $7$-adic number. Nor does absence of a symbolic factor settle those questions after specialization to the scalar sequence.

## 4.4 No unjustified global-index loss bound

Even (32) would not justify


$$
v_7(V_n^*)=O(\log n)
$$


for all positive integers.

For example, choose rapidly growing integers $m_j$ and put


$$
\nu=\sum_{j\ge1}7^{m_j},\qquad
n_j=\sum_{i\le j}7^{m_i}.
$$


Then


$$
v_7(n_j-\nu)=m_{j+1},
\qquad \log n_j\asymp m_j.
$$


Arbitrarily large gaps between successive $m_j$ invalidate a general logarithmic bound.

A rational or algebraic identification of $\nu_r$ could change this conclusion, but no such identification has been proved here.

### Bounded root-inclusive follow-on lemma

If $\Lambda_r\ne0$, choose any $j\in\{0,\ldots,6\}$ with


$$
\beta_r+\Lambda_rj\not\equiv0\pmod7.
$$


There are exactly six choices, and each gives


$$
\boxed{
v_7(V_n^*)=1
\quad(n\equiv r+7j\pmod{49}).
}
\tag{35}
$$


This gives a constructive way to use the genuine root disk without any Diophantine approximation assumption about its limiting root.

---

# 5. Enough prime mass already exists on simultaneous indices

No further all-residue unit-prime search is necessary for a constructive infinite-subfamily exclusion.

Define


$$
\mathcal T=
\left\{
n\ge0:
\begin{array}{l}
n\not\equiv2,3\pmod7,\\
n\not\equiv10\pmod{11},\\
n\not\equiv7\pmod{13}
\end{array}
\right\}.
\tag{36}
$$


There is no restriction at $19$.

The completed normalized controls and transfer imply


$$
v_p(V_n^*)=0
\quad
(n\in\mathcal T,\ p\in\{7,11,13,19\}).
\tag{37}
$$


All conditions in (36) hold on the same indices. By the Chinese remainder theorem,


$$
\operatorname{dens}(\mathcal T)
=\frac57\frac{10}{11}\frac{12}{13}
=\boxed{\frac{600}{1001}}.
\tag{38}
$$


For example, the single progression $n\equiv0\pmod{1001}$ lies inside $\mathcal T$.

## 5.1 Final-gcd valuation on this subfamily

For an odd prime $p$, write


$$
F_p=v_p(n!),\qquad \ell_p=\lfloor\log_p(n+1)\rfloor.
$$


The moment denominators give


$$
v_p(Q_n^*)\ge-\ell_p.
\tag{39}
$$


For every odd $p$ and $n\ge p$,


$$
2F_p>\ell_p.
\tag{40}
$$


Together with (37), this strictly separates the two terms of the **whole** numerator:


$$
v_p(S_n^*)=-2F_p.
$$


Therefore $S_n^*\ne0$, and reduction by the actual gcd (9) gives


$$
\boxed{
v_p(q_n)=2v_p(n!)+v_p(D_n^*)\ge2v_p(n!)
}
\tag{41}
$$


for


$$
n\in\mathcal T,\qquad n\ge19,\qquad D_n^*\ne0,
\qquad p\in\{7,11,13,19\}.
$$



Hence, with


$$
W=\frac{2\log7}{6}
+\frac{2\log11}{10}
+\frac{2\log13}{12}
+\frac{2\log19}{18},
$$


Legendre’s formula gives


$$
\boxed{
q_n\ge
\frac{\exp(Wn)}
{n^8(7\cdot11\cdot13\cdot19)^2}.
}
\tag{42}
$$



A coarse rational certificate is sufficient. The bounds


$$
\log7>\frac{1945}{1000},\quad
\log11>\frac{2397}{1000},\quad
\log13>\frac{2564}{1000},\quad
\log19>\frac{2944}{1000}
$$


follow, for example, from


$$
2\sum_{j=0}^{7}\frac{x^{2j+1}}{2j+1}
<
\log\frac{1+x}{1-x},
$$


using powers of $2$ and respectively
$x=3/11,3/19,5/21,3/35$. They give


$$
W>\frac{42349}{22500}.
$$


Using the supplied rational upper certificate


$$
\tau=2\log(1+\sqrt2)<\frac{7051}{4000},
$$


we obtain


$$
\boxed{
W-\tau>\frac{21497}{180000}>0.119.
}
\tag{43}
$$



## 5.2 Whole evaluated error and nonvanishing

The inherited theorem at the **fixed** value $b=5$ supplies eventual normality, $D_n^*\ne0$, and


$$
e+\pi-c_n
=\frac{R_n(1)}{Y_n}
=(-1)^n\epsilon_n(\sqrt2-1)^5(1+o(1)),
\tag{44}
$$


where


$$
\log\epsilon_n=-\tau n+o(n).
$$


In particular, this whole evaluated error is eventually nonzero.

Combining (42) and (44) proves the new scoped exclusion


$$
\boxed{
\liminf_{\substack{n\to\infty\\n\in\mathcal T}}
\frac1n\log|q_n(e+\pi)-p_n|
\ge W-\tau
>\frac{21497}{180000}.
}
\tag{45}
$$



Thus no unbounded-index subsequence contained in $\mathcal T$ yields shrinking primitive endpoint forms for matched $b=5$.

This is **not** a whole-family exclusion. In particular, it says nothing comparable about indices allowed to approach the unresolved root disks at increasing depth.

If (35) is certified, a root-inclusive progression can be added without changing the rate: impose


$$
n\equiv r+7j\pmod{49},\qquad n\equiv0\pmod{143}.
\tag{46}
$$


The same four primes then give (42) with an additional factor $7^{-1}$. That bounded loss does not change the exponential conclusion.

Where separation is not proved, the exact complete-numerator gate remains


$$
\mathcal R_{n,p}^*
=
V_n^*+\frac{(n!)^2}{2^{n+1}}Q_n^*,
$$




$$
\boxed{
v_p(q_n)=
\max\!\left\{
0,\,
2v_p(n!)+v_p(D_n^*)-v_p(\mathcal R_{n,p}^*)
\right\},
}
\tag{47}
$$


when the complete numerator is nonzero. It cannot be replaced by a bound on $V_n^*$ alone near the separation threshold.

---

# 6. General contiguous replacement mechanism for fixed matched $b$

This extension concerns exact row identities, not dimension-uniform denominator estimates.

Write $F_j=\mathscr F_j$, fix $k=n+1$, and use the contiguous identity


$$
\frac{F_{j+1}''}{j+1}
=(2j+1)(2F_j-F_j')+j^3F_{j-1}.
\tag{48}
$$



The raw high-row functions, after the already justified degree divisions, are


$$
R_0(k)=F_k,\qquad
R_m(k)=\frac{F_{k+m}^{(m)}}{k+m}\quad(m\ge1).
\tag{49}
$$


For matched $b$, the high block uses $m=0,\ldots,b-2$.

Define the contiguous replacement sequence


$$
\boxed{
W_{2j}(k)=F_{k+j},\qquad
W_{2j+1}(k)=\frac{F_{k+j+1}'}{k+j+1}.
}
\tag{50}
$$


Every $W_m(k)$ is an integer polynomial at nonnegative scalar indices.

## 6.1 Triangularity and its diagonal factors

The first rows satisfy


$$
R_0=W_0,\qquad R_1=W_1,
$$


and


$$
R_2=(k+1)^3W_0-(k+1)(2k+3)W_1+2(2k+3)W_2.
\tag{51}
$$



For $m\ge3$, differentiate (48) $m-2$ times at $j=k+m-1$. This gives


$$
\begin{aligned}
R_m(k)
={}&2(k+m-1)(2k+2m-1)R_{m-2}(k+1)\\
&-(k+m-1)(2k+2m-1)R_{m-1}(k)\\
&+(k+m-1)^3(k+m-2)R_{m-2}(k).
\end{aligned}
\tag{52}
$$


Since


$$
W_j(k+1)=W_{j+2}(k),
$$


induction proves that $R_m(k)$ is an integral linear combination of


$$
W_0(k),\ldots,W_m(k).
$$



Its diagonal coefficient is determined explicitly by


$$
c_0(k)=c_1(k)=1,\qquad c_2(k)=2(2k+3),
$$




$$
\boxed{
c_m(k)=2(k+m-1)(2k+2m-1)c_{m-2}(k+1)
\quad(m\ge3).
}
\tag{53}
$$


All these coefficients are nonzero for $k\ge1$. Therefore


$$
\det(R_0,\ldots,R_{b-2})
$$


in any common derivative-column realization acquires the universal triangular factor


$$
\prod_{m=0}^{b-2}c_m(k).
$$



## 6.2 Integral factorial-column normalization

After successive column differences, the $b$ tail columns are derivatives of orders $0,\ldots,b-1$ of integer polynomials. Dividing them by their respective factorials is integral.

Thus the raw contractions have the exact common factor


$$
\boxed{
K_{n,b}
=
\left(\prod_{m=0}^{b-2}c_m(n+1)\right)
\left(\prod_{j=0}^{b-1}j!\right),
}
\tag{54}
$$


and the quotient contractions are obtained directly from the integral rows (50), followed by coefficient extraction at $1+t$.

This is a root-safe construction: at a modular zero of one of the factors in (54), the quotient is evaluated through the replacement rows, not by modular division.

The recurrence reproduces the supplied $b=5$ triangular factor, but (52)–(54) apply to every fixed finite $b$.

**Limit of the claim.** This mechanism removes the entire displayed contiguous triangular factor and factorial-column content. It does not prove that the remaining contractions have constant symbolic gcd for every $b$, nor that their evaluated content is exhausted. Polynomial dependence and integral replacement do not supply uniform arithmetic estimates as $b$ grows.

---

# Concluding ledger

## (1) New result and proof status

**Proved here, with explicit derivations:**

1. Restricted-analytic scalar interpolation on each odd-prime residue disk, with a coefficientwise all-depth truncation bound.
2. The small-depth scalar carry
   

$$
\mathbf S(r+pT)
   =\mathbf S_r+pT\mathbf L_r+pT^2\mathbf S_r
   \pmod{p^2}
   \quad(2r<p).
$$


3. Its cancellation in the genuine $b=5$, $7$-adic root disks, yielding the all-depth form (1).
4. The explicit scalar tangents (25), and the exact finite determinant formulas (29)–(30) for the two unresolved slopes.
5. A precise simple-root criterion, with exact valuation
   $v_7(V_n^*)=v_7(n-\nu_r)$ when the slope is a unit; and a bounded-loss root-inclusive progression criterion.
6. A general integral contiguous replacement mechanism, equations (50)–(54).

**Certificate-backed new consequence:**

The completed controls, normalized transfer, final-gcd valuation, and inherited fixed-$b=5$ whole-error theorem imply the positive-density matched-$b=5$ exclusion (45), on the explicitly simultaneous set $\mathcal T$ of density $600/1001$.

**Not proved:**

* existence of a $7$-adic root in either of the two disks;
* rationality or irrationality of any such $7$-adic root;
* a whole-family matched-$b=5$ exclusion;
* any decision on irrationality of $e+\pi$.

## (2) Exact remaining bottleneck

For the assigned two root disks, the immediate finite bottleneck is


$$
\left(\frac{\widetilde V_2}{7},\Lambda_2\right)\pmod7,
\qquad
\left(\frac{\widetilde V_3}{7},\Lambda_3\right)\pmod7.
$$



If a slope is a unit, the infinite local root theorem is already proved above. What would remain for a **whole-family** denominator lower bound is quantitative control of integer approximation to that root—or a different argument using $D_n^*$ and the complete expression (47). No $O(\log n)$ loss bound follows merely from Hensel lifting.

The main irrationality problem remains open.

## (3) Bounded exact computation request

No further prime selection or all-residue unit certificate is requested.

For the coordinator’s consideration, request exactly **four new normalized prime-square rows**:


$$
\boxed{p=7,\qquad n\in\{2,9,3,10\},\qquad\text{modulus }49.}
$$



**Inputs:** the existing integral $b=5$ replacement-basis determinant circuit and exact scalar recurrence.

**Expected verifiable output:**

1. For each of the four indices,
   

$$
(\widetilde\sigma_n,\widetilde\chi_n,
     \widetilde\kappa_n,\widetilde V_n)\pmod{49}.
$$


2. The four residues
   

$$
\beta_2=\widetilde V_2/7,\quad
   \beta_3=\widetilde V_3/7,\quad
   \Lambda_2=(\widetilde V_9-\widetilde V_2)/7,\quad
   \Lambda_3=(\widetilde V_{10}-\widetilde V_3)/7
   \pmod7.
$$


3. Independent agreement of the slopes with the tangent circuits (29)–(30).
4. For each unit slope, the unique surviving lift
   

$$
j_r\equiv-\beta_r\Lambda_r^{-1}\pmod7,
$$


   and the six complementary lifts having exact primitive valuation $1$.
5. If a slope and intercept both vanish, return that degeneracy explicitly; do not label the disk a simple root.

These four rows would complete the first root classification step. Their infinite force comes from the coefficientwise expansion proved above, not from the finite evaluations alone.
