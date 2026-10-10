> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2, Turn 9 — The $29$-step reset is nilpotent, not a surviving rank-one channel

## Executive assessment

The restrictive reset yields a substantially stronger conclusion than a large-period Fitting bound:

> **The complete homogeneous $29$-step monodromy has zero stable image. It does not have a surviving rank-one stable image.**

At phase $i\equiv2\pmod{29}$, its reduction is the explicit square-zero matrix


$$
\boxed{
B^{[2]}=
\begin{pmatrix}
0&-2&2\\
0&-1&1\\
0&-1&1
\end{pmatrix},
\qquad (B^{[2]})^2=0.
}
$$


The exceptional phase $i\equiv1\pmod{29}$ has a rank-two, cube-zero monodromy. All other phases have rank-one, square-zero monodromy.

This has three useful consequences.

1. **Linear-in-precision forgetting.** Modulo $29^K$, every homogeneous propagator of length at least
   

$$
\boxed{58K+1}
$$


   vanishes. No period of length $29^K$ or $29^{\operatorname{poly}(K)}$ is needed for this recurrence.

2. **An explicit finite-memory formula for the complete particular solution.** The actual source is retained, with at most $58K+1$ preceding source entries contributing to any recurrence output modulo $29^K$.

3. **A rational generating-kernel closure.** The source and the recurrence-generated particular input can be represented, modulo $29^K$, using coefficient extractions of rational functions whose relevant $z$-pole order is at most $87K$. This replaces a generic recurrence-state existence argument by explicit polynomial transition weights.

The source calculation is especially revealing. Write


$$
n=29m,\qquad b=29B+27.
$$


Then, on every actual source row,


$$
\boxed{
\mathcal H_{29q+t}\equiv
\begin{cases}
\displaystyle\binom{2m+q}{B},&t=26,27,\\[2mm]
0,&t\ne26,27,
\end{cases}
\pmod{29}.
}
$$


These two adjacent impulses disappear from the phase-$2$ block-end state, but **not from the interior recurrence outputs**. Consequently, even the vanishing of the inhomogeneous block-end contribution does not imply a vanishing Gram contribution.

The remaining obstruction is therefore sharper, not removed:



$$
\boxed{
\mathcal C-29\rho_n\mathcal N
\in29^2\mathcal N\mathbb Z_{29}
}
$$


still requires an identity for the **actual contact-inverted, weighted, endpoint-sensitive outputs**, at the first nonzero digit of the actual norm.

No original normalized defect is evaluated in this report. No unconditional proof or disproof of irrationality of $e+\pi$ is obtained.

No tools were executed.

---

# 1. Scope, original indices, and source status

Throughout,


$$
p=29,
$$


and the original family remains


$$
a=432827+682892t,\qquad b=3^a,\qquad n=2001b,
$$


with


$$
t=364+841u,\qquad u\ge0.
$$


Equivalently,


$$
\boxed{
b=3^{249005515+574312172u},\qquad n=2001b.
}
$$



The finite domains are unchanged:

- contact coordinates:
  

$$
0\le i,j<b;
$$


- recurrence rows:
  

$$
1\le i\le b-2;
$$


- reconstructed coordinates:
  

$$
0\le j\le b.
$$



Retain


$$
A\theta=f^0,\qquad A\psi=\mathbf r,
$$




$$
Z_w=\mathcal R\theta,\qquad
Y=\mathcal R\psi+W_be_b,
$$


where


$$
W_j=\binom{n+2}{j},\qquad
(\mathcal Rx)_j=W_j(jx_{j-1}-x_j)
$$


with the actual first and last rows.

The normalization remains


$$
P=\frac{Z_w}{p^2},\qquad
Q=\frac{Y}{p^3},\qquad
D=P^TP,\qquad M=P^TQ,
$$


and


$$
\boxed{
\mathcal N=Z_w^TZ_w=p^4D,\qquad
\mathcal C=Z_w^TY=p^5M.
}
$$



## 1.1 What is reused

A4turn18 audits Turn 7’s:

- finite contact factorization and endpoint correction;
- unit endpoint solve;
- projection charges;
- unweighted saturation statement;
- complete-force reduction to two initial values and one source column;
- division-free norm-relative numerator criterion.

Those results are used only at those scopes.

Turn 8’s broader digit/Fitting construction remains pending independent audit. The principal results below do **not** require accepting its complete six-entry digit theorem. They follow from the displayed recurrence, the explicit source, and the already audited finite contact reconstruction.

The classical Fitting theorem is used as standard background, not as a novelty claim. The new issue here is the calculation of the **actual monodromy**, which makes its stable image zero.

---

# 2. The actual recurrence and the two-step reset

Set


$$
x_i=
\begin{pmatrix}
h_i\\h_{i-1}\\h_{i-2}
\end{pmatrix}
$$


when these coordinates are actual available coordinates. For $i\ge2$,


$$
x_{i+1}=T_i x_i+e_1\mathcal H_i,
$$


where


$$
T_i=
\begin{pmatrix}
\alpha_i&-\beta_i&-\gamma_i\\
1&0&0\\
0&1&0
\end{pmatrix},
$$




$$
\alpha_i=2n+2i+1,
$$




$$
\beta_i=\frac{(n+i)(n+3i-1)}2,
\qquad
\gamma_i=\frac{(n+i)(n+i-1)(1-i)}2.
$$



The first row is handled separately:


$$
h_2=\alpha_1h_1-\beta_1h_0+\mathcal H_1.
$$


No $h_{-1}$ is introduced into the original problem.

Modulo $p$, since $p\mid n$,


$$
\overline T_i=
\begin{pmatrix}
2i+1&-\dfrac{i(3i-1)}2&\dfrac{i(i-1)^2}2\\
1&0&0\\
0&1&0
\end{pmatrix}.
$$



At $i\equiv0\pmod p$,


$$
h_{i+1}=h_i+\mathcal H_i.
$$


At the next step,


$$
h_{i+2}=3h_{i+1}-h_i+\mathcal H_{i+1}.
$$


Thus the complete two-step reset is


$$
\boxed{
x_{i+2}
=
\begin{pmatrix}2\\1\\1\end{pmatrix}h_i
+
\begin{pmatrix}
3\mathcal H_i+\mathcal H_{i+1}\\
\mathcal H_i\\
0
\end{pmatrix}
\pmod p.
}
\tag{2.1}
$$



The homogeneous rank-one statement is correct. But the source term in (2.1) must be retained until its actual residues have been evaluated.

---

# 3. Complete homogeneous $29$-step monodromy

For a starting phase $a$, define the mod-$p$ block product


$$
\overline B^{[a]}
=
\overline T_{a+28}\cdots\overline T_a,
$$


with subscripts read modulo $29$.

These products are algebraic objects used to establish identities for actual intervals. Their definition does not extend the original contact vector beyond its endpoint.

## 3.1 Phase $0$: rank one, but square zero

After the reset at phase $0$, the homogeneous sequence is


$$
h_r=r!\,h_0\pmod p
$$


through $r=p$. This follows by substitution in the recurrence.

Wilson’s theorem gives


$$
(p-1)!\equiv-1,\qquad (p-2)!\equiv1\pmod p.
$$


Therefore


$$
(h_p,h_{p-1},h_{p-2})=(0,-h_0,h_0),
$$


so


$$
\boxed{
\overline B^{[0]}
=
\begin{pmatrix}
0&0&0\\
-1&0&0\\
1&0&0
\end{pmatrix}.
}
\tag{3.1}
$$


In particular,


$$
\operatorname{rank}\overline B^{[0]}=1,
\qquad
(\overline B^{[0]})^2=0.
$$



The image line is annihilated on the next block. It is not a stable unit-eigenvalue line.

## 3.2 Two short coefficient identities

To evaluate the other delicate phases without a $29$-entry numerical table, use


$$
\phi(z)=1-z+\frac{z^2}{2},
\qquad
\phi(z)^{-1}=\sum_{r\ge0}u_rz^r.
$$



In $\mathbb F_{29}$,


$$
\phi(z)=(1-21z)(1-9z),
$$


because


$$
21+9=1,\qquad21\cdot9=\frac12.
$$


Hence


$$
u_r=\frac{21^{r+1}-9^{r+1}}{21-9}.
$$


Fermat’s theorem yields


$$
\boxed{u_{27}=0,\qquad u_{28}=1.}
\tag{3.2}
$$



Also define the finite logarithm


$$
\mathscr L(X)=\sum_{q=1}^{28}\frac{X^q}{q}\in\mathbb F_{29}[X].
$$


The standard finite-logarithm symmetry


$$
\mathscr L(X)=\mathscr L(1-X)
$$


gives


$$
\mathscr L(21)=\mathscr L(9).
$$


Thus


$$
\boxed{
\sum_{q=1}^{28}\frac{u_{q-1}}q=0.
}
\tag{3.3}
$$



These identities determine the exceptional monodromy exactly.

## 3.3 Phase $1$: rank two and cube zero

For the $n=0$ coefficient model, a sequence satisfying the homogeneous recurrence from $i=1$ has exponential generating function


$$
H(z)
=
\frac{h_0+(h_1-h_0)\displaystyle\int_0^z\phi(t)^{-1}\,dt}
{1-z}.
$$


This follows from


$$
\phi(z)\bigl((1-z)H'(z)-H(z)\bigr)=h_1-h_0.
$$



Equations (3.2)–(3.3) give


$$
h_{29}=h_0-h_1,\qquad h_{28}=-h_0.
$$


The next reset gives $h_{30}=h_{29}$. Consequently,


$$
\boxed{
\overline B^{[1]}
=
\begin{pmatrix}
-1&1&0\\
-1&1&0\\
0&-1&0
\end{pmatrix}.
}
\tag{3.4}
$$


It satisfies


$$
(\overline B^{[1]})^2
=
\begin{pmatrix}
0&0&0\\
0&0&0\\
1&-1&0
\end{pmatrix},
\qquad
(\overline B^{[1]})^3=0.
$$



Thus the phase split matters: not every $29$-step block has rank one.

## 3.4 Phase $2$: the actual initial-state phase

For arbitrary initial $x_2=(h_2,h_1,h_0)^T$, the same $n=0$ generating-function calculation has


$$
\phi(z)\bigl((1-z)H'(z)-H(z)\bigr)
=k_0+k_1z,
$$


where


$$
k_0=h_1-h_0,\qquad
k_1=h_2-3h_1+h_0.
$$


At coefficient $h_{29}$, only the denominator $29$ in the integral contributes modulo $29$. By (3.2),


$$
h_{29}=-k_0u_{28}-k_1u_{27}=h_0-h_1.
$$


The two following reset steps give


$$
(h_{31},h_{30},h_{29})
=(2,1,1)(h_0-h_1).
$$


Therefore


$$
\boxed{
\overline B^{[2]}
=v\,w,
\qquad
v=
\begin{pmatrix}2\\1\\1\end{pmatrix},
\quad
w=(0,-1,1).
}
\tag{3.5}
$$


Since $wv=0$,


$$
\boxed{(\overline B^{[2]})^2=0.}
$$



This is the relevant complete monodromy for the original two-initial-value recurrence.

## 3.5 All remaining phases

For $2\le a\le28$, put


$$
U_a=\overline T_{a-1}\cdots\overline T_2,
\qquad U_2=I.
$$


Every factor is invertible: the only singular phases modulo $29$ are $0$ and $1$.

Hence


$$
\boxed{
\overline B^{[a]}
=
U_a\overline B^{[2]}U_a^{-1}.
}
\tag{3.6}
$$


Its image vector is


$$
U_av=
\begin{pmatrix}
a!\\(a-1)!\\(a-2)!
\end{pmatrix}.
$$


Thus every phase other than $1$ has rank-one, square-zero monodromy.

### Conclusion of the monodromy calculation



$$
\boxed{
\begin{array}{c|c|c}
\text{starting phase}&\text{rank}&\text{nilpotence index}\\ \hline
1&2&3\\
0,2,3,\ldots,28&1&2
\end{array}
}
\tag{3.7}
$$



This is stronger, and structurally different, from a power-period bound.

---

# 4. The actual source, including higher-digit dependence

The complete source is


$$
\mathcal H_i
=
\sum_s a_s(n+1)(n+i)_{\underline s}
\binom{2n+i-s+1}{b},
$$


where


$$
a_s(n+1)=[z^s]\phi(z)^{n+1}.
$$



Modulo $29$, the terms $s\ge29$ vanish by falling-factorial divisibility. Since $n\equiv0\pmod{29}$, the only remaining coefficient terms are


$$
a_0=1,\qquad a_1=-1,\qquad a_2=\frac12.
$$


Therefore


$$
\boxed{
\mathcal H_i
\equiv
\binom{2n+i+1}{b}
-i\binom{2n+i}{b}
+\frac{i(i-1)}2\binom{2n+i-1}{b}
\pmod{29}.
}
\tag{4.1}
$$



Write


$$
n=29m,\qquad b=29B+27,\qquad i=29q+t.
$$


Lucas’s theorem, applied to all three terms, gives


$$
\boxed{
\mathcal H_{29q+t}
\equiv
\begin{cases}
\kappa_q,&t=26,27,\\
0,&t\ne26,27,
\end{cases}
\qquad
\kappa_q=\binom{2m+q}{B}\pmod{29}.
}
\tag{4.2}
$$



At $t=28$, the last two surviving contributions cancel. This cancellation is essential.

## 4.1 The actual low digits sharpen, but do not finish, this evaluation

The retained digits


$$
n_0,n_1,n_2,n_3=0,7,24,7
$$


and $n=2001b=29\cdot69b$ imply


$$
b_0,b_1,b_2=27,28,5.
$$


In particular,


$$
n\equiv203\pmod{29^2},
\qquad
b\equiv839=-2\pmod{29^2}.
$$



Since $m_0=7$ and $B_0=28$, equation (4.2) gives


$$
\boxed{
\kappa_q=0\pmod{29}
\quad\text{unless}\quad q\equiv14\pmod{29}.
}
\tag{4.3}
$$


For $q=29r+14$,


$$
\kappa_q
=
\binom{2\lfloor m/29\rfloor+r}{\lfloor B/29\rfloor}
\pmod{29}.
$$



This still depends on the actual higher digits. It is not a constant determined by the displayed prefix.

Those digits must come from


$$
b=3^{249005515+574312172u},
$$


not from an arbitrarily completed $29$-adic cylinder.

---

# 5. Complete affine monodromy and the true terminal phase

## 5.1 Phase $0$

Within a phase-$0$ block, the only source impulses modulo $29$ occur at phases $26,27$, with equal value $\kappa_q$.

Their contribution to the block-end state is


$$
(0,-2\kappa_q,\kappa_q)^T.
$$


Thus, whenever the whole block lies in the actual recurrence range,


$$
\boxed{
x_{29(q+1)}
=
\overline B^{[0]}x_{29q}
+
\begin{pmatrix}0\\-2\kappa_q\\\kappa_q\end{pmatrix}
\pmod{29}.
}
\tag{5.1}
$$



## 5.2 Phase $2$

The same two impulses produce


$$
(h_{29q+29},h_{29q+28},h_{29q+27})
=(0,-2\kappa_q,\kappa_q)
$$


for the source-only response. The next two reset steps annihilate that state.

Therefore the complete phase-$2$ block law is


$$
\boxed{
x_{29q+31}
=
\overline B^{[2]}x_{29q+2}
\pmod{29},
}
\tag{5.2}
$$


with **zero block-end source contribution**.

This is an actual evaluated source cancellation. It does not say that the source response is zero inside the block.

For example, the source-only response has


$$
h_{29q+27}=\kappa_q,\qquad
h_{29q+28}=-2\kappa_q
\pmod{29}.
$$


These entries can be detected by subsequent contact inversion and weighted Gram evaluation.

## 5.3 Actual initial values

For the first force,


$$
f_1^0\equiv f_0^0=J\pmod{29}.
$$


Its first state is therefore


$$
x_2(f^0)\equiv J(2,1,1)^T,
$$


which lies in the kernel of $\overline B^{[2]}$.

For the complete second force,


$$
r_0\equiv r_1\equiv0\pmod{29},
\qquad \mathcal H_1\equiv0,
$$


so its first state is zero modulo $29$.

These facts explain the vanishing actual phase-$2$ block-end states modulo $29$. They do not eliminate the interior source impulses or their reconstructed outputs.

## 5.4 The shortened final recurrence block

Because


$$
b=29B+27,
$$


the recurrence rows end at


$$
b-2=29B+25.
$$


After the separate first step $i=1$, the interval $i=2,\ldots,b-2$ has length


$$
b-3=29B+24.
$$


It therefore consists of:

- exactly $B$ complete phase-$2$ blocks;
- exactly $24$ remaining steps.

The last recurrence state ends at $h_{b-1}$. No additional recurrence step is inserted.

The reconstructed coordinate $j=b$ remains separate:


$$
\boxed{Y_b=W_b(b\psi_{b-1}+1).}
\tag{5.3}
$$



---

# 6. Higher precision: the genuine finite-ring stable image is zero

Let


$$
R_K=\mathbb Z/29^K\mathbb Z.
$$


For actual phase-$2$ blocks, define


$$
B_q=T_{29q+30}\cdots T_{29q+2}.
$$


Every $B_q$ reduces to the same square-zero matrix $B^{[2]}$.

Choose its displayed integer lift, which is itself square zero, and write


$$
B_q=B^{[2]}+29E_q.
$$


Here $E_q$ is the actual integral quotient, not a division performed without guard digits in $R_K$.

Then


$$
\boxed{
B_{q+1}B_q
=
29\left(
B^{[2]}E_q+E_{q+1}B^{[2]}
+29E_{q+1}E_q
\right).
}
\tag{6.1}
$$


This gives the actual pair-transition weight after extracting the demonstrated factor $29$.

Consequently, every product of $2K$ consecutive phase-$2$ blocks is zero modulo $29^K$.

## Theorem 1 — Linear-precision forgetting

For every $K\ge1$, every homogeneous recurrence propagator of length at least


$$
\boxed{H_K=58K+1}
\tag{6.2}
$$


vanishes modulo $29^K$, provided the interval is inside the actual recurrence range.

### Proof

If the starting phase is not $1$, its mod-$29$ block monodromy is square zero. Pairing consecutive $29$-step blocks therefore supplies one factor of $29$ per pair. After $K$ pairs, the product is zero modulo $29^K$.

If the starting phase is $1$, take its first step separately. The remaining interval starts at phase $2$, so the preceding argument applies after another $58K$ steps. ∎

For the original homogeneous inputs, whose genuine three-state initialization is at $i=2$, the sharper aligned bound is


$$
\boxed{
h_j^{(0)}\equiv h_j^{(1)}\equiv0\pmod{29^K}
\qquad(j\ge2+58K).
}
\tag{6.3}
$$



## 6.1 Fitting projectors

For any fixed $29$-step block matrix over $R_K$, its mod-$29$ reduction is nilpotent. Therefore the matrix itself is nilpotent:

- exponent at most $2K$ away from phase $1$;
- exponent at most $3K$ at phase $1$.

Its genuine Fitting decomposition is consequently


$$
\boxed{
\text{stable image}=0,\qquad
\text{nilpotent component}=R_K^3,
}
$$


and its stable-image projector is


$$
\boxed{E_{\mathrm{st}}=0.}
\tag{6.4}
$$



For the genuinely periodic coefficient system modulo $29^K$, the coefficient period is $29^K$. If $K\ge2$,


$$
29^K\ge58K+1.
$$


Thus an entire coefficient-period monodromy is already the zero matrix in $R_K$.

This is the appropriate application of finite-ring Fitting theory. A surviving rank-one quotient would be incorrect.

## 6.2 What this says about conserved bilinear forms

Suppose a periodic homogeneous bilinear form were represented by $J$ and satisfied


$$
B^TJB=J
$$


for one complete coefficient-period monodromy. Iteration gives


$$
J=(B^r)^TJB^r=0
$$


once $B^r=0$.

Thus:



$$
\boxed{
\text{There is no nonzero periodic conserved homogeneous bilinear form
on this full recurrence state over }R_K.
}
\tag{6.5}
$$



This does not rule out:

- inhomogeneous identities with source charges;
- finite-terminal adjoint identities;
- identities for the nonlocal contact-inverted outputs.

It does rule out obtaining the desired Gram alignment from a purported nonzero stable rank-one homogeneous channel.

---

# 7. Explicit finite-memory input/output weights

Define


$$
q_0(j)=1,
$$


and, for $d\ge1$,


$$
q_d(j)
=
e_1^TT_{j-1}\cdots T_{j-d}e_1.
$$


These are actual impulse-response weights.

They can be generated without matrix periods:


$$
\boxed{
q_d(j)
=
\alpha_{j-1}q_{d-1}(j-1)
-\beta_{j-1}q_{d-2}(j-2)
-\gamma_{j-1}q_{d-3}(j-3),
}
\tag{7.1}
$$


with negative-subscript terms zero.

For example,


$$
q_1(j)=\alpha_{j-1},
$$




$$
q_2(j)=\alpha_{j-1}\alpha_{j-2}-\beta_{j-1}.
$$


Induction shows


$$
q_d(j)\in\mathbb Z[1/2][n,j],
\qquad
\deg q_d\le d.
$$



The complete particular solution therefore has the finite-memory formula


$$
\boxed{
\tau_j
\equiv
\sum_{\ell=\max(1,j-H_K)}^{j-1}
q_{j-\ell-1}(j)\,\mathcal H_\ell
\pmod{29^K},
\qquad 2\le j<b.
}
\tag{7.2}
$$


Only actual rows $\ell\le b-2$ occur.

The complete force remains


$$
\boxed{
r_j=r_0h_j^{(0)}+r_1h_j^{(1)}+\tau_j.
}
\tag{7.3}
$$


The values $r_0,r_1$ here are the complete initial values, including the logarithmic contribution.

### Scope

Equations (6.3) and (7.2) give a precision-sized input/output description of the **internal recurrence**:

- an initial transient of length $O(K)$;
- a source memory of length $O(K)$;
- explicitly generated polynomial transition weights.

They do not yet give an output-compatible quotient for the actual Gram calculation after $A^{-1}$, $\mathcal R$, projection, and summation.

---

# 8. A simpler rational generating-kernel closure

The finite-memory description admits an algebraic closure substantially smaller than a full $29^K$-phase table.

Let


$$
s_{\max}=\min(2n+2,29K-1),
$$


and define, for $s\ge0$,


$$
R_s(t)
=
\sum_{k=0}^s
\binom n{s-k}\frac{t^k}{(1-t)^{k+1}}.
$$


Vandermonde’s identity and


$$
\sum_{i\ge0}\binom ikt^i=\frac{t^k}{(1-t)^{k+1}}
$$


give


$$
\sum_{i\ge0}\binom{n+i}s t^i=R_s(t).
$$



## 8.1 Source kernel

The extended coefficient formula for the source has generating function


$$
\boxed{
\sum_{i\ge0}\mathcal H_i z^i
\equiv
[X^b]\sum_{s=0}^{s_{\max}}
a_s(n+1)s!(1+X)^{2n+1-s}
R_s\bigl(z(1+X)\bigr)
\pmod{29^K}.
}
\tag{8.1}
$$



This is a coefficient extraction of an explicitly displayed rational function. Its $z$-poles have order at most $29K$.

The extension is used only to describe coefficients. The original particular input is still restricted to $0\le j<b$, and its source rows remain $1,\ldots,b-2$.

## 8.2 Particular-input kernel

Let


$$
\Theta=z\frac{d}{dz},
\qquad
\mathscr H_+(z)=\sum_{\ell\ge1}\mathcal H_\ell z^\ell.
$$


Equation (7.2) becomes


$$
\boxed{
\sum_{j\ge0}\tau_jz^j
\equiv
\sum_{d=0}^{H_K-1}
z^{d+1}q_d(\Theta+d+1)\mathscr H_+(z)
\pmod{29^K},
}
\tag{8.2}
$$


followed by retention of only $j<b$.

Since $\deg q_d\le d$, applying the largest differential operator raises the relevant pole order by at most


$$
H_K-1=58K.
$$


Thus the resulting rational coefficient kernel has $z$-pole order at most


$$
\boxed{29K+58K=87K.}
\tag{8.3}
$$



No coefficient-period table of size $29^K$ is needed.

## 8.3 The actual contact kernel

Finite Vandermonde convolution gives, for the actual entries $i,j<b$,


$$
A_{ij}
=
\sum_s a_s(n)s!\binom{n+i}s
\binom{2n+i-s}{j}.
$$


Consequently,


$$
\boxed{
\sum_{i,j\ge0}A_{ij}z^iX^j
\equiv
\sum_{s=0}^{\min(2n,29K-1)}
a_s(n)s!(1+X)^{2n-s}
R_s\bigl(z(1+X)\bigr)
\pmod{29^K}.
}
\tag{8.4}
$$



This is a simple rational generating kernel for the matrix entries.

**Important limitation:** the original $b\times b$ truncation must be made before taking the finite inverse. Inverting an infinite generating kernel and then truncating is not justified. The accepted endpoint correction, or the finite inverse word expansion, is still necessary.

Thus (8.1)–(8.4) provide an explicit algebraic closure of the recurrence and entry kernels, but not a new identity for the inverse Gram outputs.

---

# 9. Actual Gram weights, projection, and boundary charges

The remaining output issue can be displayed without any ambiguity about weights or endpoints.

Set


$$
L=\mathcal R^T\mathcal R.
$$


It is the actual $b\times b$ tridiagonal matrix


$$
\boxed{
L_{jj}=W_j^2+(j+1)^2W_{j+1}^2,
\qquad0\le j<b,
}
\tag{9.1}
$$




$$
\boxed{
L_{j,j+1}=L_{j+1,j}=-(j+1)W_{j+1}^2,
\qquad0\le j<b-1.
}
\tag{9.2}
$$


In particular, its last diagonal entry includes $b^2W_b^2$.

The exterior mixed charge is


$$
\boxed{
\mathcal R^T(W_be_b)=bW_b^2e_{b-1}.
}
\tag{9.3}
$$



Define


$$
\Gamma=A^{-T}LA^{-1},
\qquad
\eta=bW_b^2A^{-T}e_{b-1}.
$$


Then the two actual contractions are exactly


$$
\boxed{
\mathcal N=(f^0)^T\Gamma f^0,
}
\tag{9.4}
$$




$$
\boxed{
\mathcal C=(f^0)^T\Gamma\mathbf r+(f^0)^T\eta.
}
\tag{9.5}
$$



Equation (9.5) makes the exterior $+1$ a separate, nonoptional output charge.

## 9.1 Three-column Gram formula

Let


$$
\mathsf H=(h^{(0)},h^{(1)},\tau).
$$


Then


$$
\boxed{
G^{\mathrm{raw}}
=
\mathsf H^T\Gamma\mathsf H
+(\mathsf H^T\eta)e_*^T
+e_*(\eta^T\mathsf H)
+W_b^2e_*e_*^T.
}
\tag{9.6}
$$



This is the actual six-entry Gram law. It is not a norm of the internal three-state recurrence.

## 9.2 Projection charges

Retain


$$
\ell_j=\frac{\omega_b}{\omega_j},
\qquad
\mathscr S=\ell^T\ell,
\qquad
\Pi=I-\frac{\ell\ell^T}{\mathscr S}.
$$


Because


$$
\ell_jW_j=\frac{\omega_b}{j!},
$$


the complete finite reconstruction telescopes:


$$
\ell^T\mathcal Rx=0.
$$


Also $\ell_b=1$. Therefore


$$
\boxed{
\ell^TB_0=\ell^TB_1=0,\qquad
\ell^TB_*=W_b.
}
\tag{9.7}
$$


Hence


$$
\boxed{
G
=
G^{\mathrm{raw}}
-\frac{W_b^2}{\mathscr S}e_*e_*^T.
}
\tag{9.8}
$$



The original-family unit $\mathscr S\equiv8\pmod{29}$ is used only at its accepted scope.

No weighted saturation is inferred from the unweighted recurrence basis. Every $W_j$ remains in (9.1)–(9.8).

---

# 10. Why nilpotent recurrence reset still does not prove Gram alignment

There are two distinct obstructions.

## 10.1 The source can be invisible at block ends and visible in outputs

Equation (5.2) shows that the actual mod-$29$ source contributes zero to a phase-$2$ block-end state.

Nevertheless, the same block contains the nonzero potential entries


$$
\tau_{29q+27}=\kappa_q,\qquad
\tau_{29q+28}=-2\kappa_q.
$$


The map


$$
h\longmapsto\mathcal RA^{-1}h
$$


is not determined by block-end recurrence states. It acts on the entire finite input vector.

Discarding these interior entries because their block-end state is zero would discard actual forcing.

## 10.2 The finite inverse is nonlocal

The recurrence has short memory modulo $29^K$, but $A^{-1}$ is not shown to preserve that locality.

For example, (9.5) involves


$$
\sum_{i,j=0}^{b-1}f_i^0\,\Gamma_{ij}r_j.
$$


A short source-memory formula for $r_j$ does not make the kernel $\Gamma_{ij}$ local.

The rational kernels in §8, combined with the accepted finite inverse expansion, give a route to evaluation. They do not identify the mixed output functional with $29\rho_n$ times the norm output functional.

This is the precise obstruction to promoting the reset into the desired relative law.

---

# 11. A more concrete remaining output-kernel lemma

The reset does reduce the number of first-force input rows that can matter at a requested absolute precision.

Since


$$
f_i^0=\frac{(n+i)!}{n!}J_i,
\qquad J_i\in\mathbb Z,
$$


one has


$$
\boxed{f_i^0\equiv0\pmod{29^K}\qquad(i\ge29K).}
\tag{11.1}
$$


Put


$$
m_K=\min(b,29K).
$$



Thus, modulo $29^K$,


$$
\mathcal N
=
\sum_{i,j<m_K}f_i^0\Gamma_{ij}f_j^0.
$$



Define the actual head-to-source output kernel


$$
\boxed{
\Psi_\ell
=
\sum_{d=0}^{\min(H_K-1,b-\ell-2)}
q_d(\ell+d+1)
\sum_{i<m_K}f_i^0\Gamma_{i,\ell+d+1}.
}
\tag{11.2}
$$


Also set


$$
A_0=(f^0)^T\Gamma h^{(0)},\qquad
A_1=(f^0)^T\Gamma h^{(1)},\qquad
E_{\mathrm{out}}=(f^0)^T\eta.
$$


Then


$$
\boxed{
\mathcal C
\equiv
r_0A_0+r_1A_1
+\sum_{\ell=1}^{b-2}\mathcal H_\ell\Psi_\ell
+E_{\mathrm{out}}
\pmod{29^K},
}
\tag{11.3}
$$


and


$$
\boxed{
\mathcal N=f_0^0A_0+f_1^0A_1.
}
\tag{11.4}
$$



These identities retain:

- the complete $r_0,r_1$;
- every actual source row;
- the shortened final lag range in (11.2);
- the exterior charge $E_{\mathrm{out}}$;
- the actual finite inverse and weights.

### Follow-on lemma — open

On the original orbit, at


$$
K=v_{29}(\mathcal N)+2,
$$


prove


$$
\boxed{
\begin{aligned}
&\sum_{\ell=1}^{b-2}\mathcal H_\ell\Psi_\ell+E_{\mathrm{out}}\\
&\quad +(r_0-29\rho_nf_0^0)A_0
+(r_1-29\rho_nf_1^0)A_1
\equiv0\pmod{29^K}.
\end{aligned}
}
\tag{11.5}
$$



A useful next advance would be a rational-kernel or adjoint telescoping identity for the **specific** kernel (11.2), including the finite-inverse endpoint correction. A recurrence-state Fitting theorem cannot supply (11.5), because its stable image is zero and its block-end outputs omit the relevant interior source response.

---

# 12. Complete initial force and logarithmic protection

The complete initial values remain


$$
\boxed{
r_i=
\sum_s a_s(n)(n+i)_{\underline s}
\left(
T_{2n+i-s}+\frac{L_{2n+i-s}}{b!}
\right),
\qquad i=0,1,
}
\tag{12.1}
$$


where


$$
T_m=\frac1{b!}\sum_{q=b}^m(m)_{\underline q},
$$




$$
L_0=0,\qquad
L_m=mL_{m-1}+2(m-1)!u_{m-1}.
$$



Exact interior logarithmic homogeneity does not make these initial values zero.

The retained whole-force bound is


$$
r^F\in29^{N_{\log}}\mathbb Z_{29}^b,
$$




$$
N_{\log}
=
2v_{29}(n!)-v_{29}(b!)
-\lfloor\log_{29}(2n+b-1)\rfloor.
$$



Write


$$
P=29^cx,\qquad x\ \text{primitive},\qquad
\nu=v_{29}(x^Tx).
$$


Then


$$
v_{29}(\mathcal N)=2c+4+\nu.
$$


The relative logarithmic-protection estimate remains


$$
\boxed{
v_{29}\!\left(\frac MD-\frac{M^{(e)}}D\right)
\ge N_{\log}-c-3-\nu.
}
\tag{12.2}
$$


Thus logarithmic omission in the normalized ratio modulo $29$ requires


$$
\boxed{N_{\log}\ge c+4+\nu.}
\tag{12.3}
$$



The entire primitive-norm loss $\nu$ is still paid. The reset theorem supplies no bound on $\nu$.

---

# 13. Testing at the true first nonzero norm digit

The norm is nonzero over $\mathbb Q$:

- $f_0^0=J\ne0$;
- $A$ is invertible;
- the finite reconstruction is injective on contact vectors;
- its real squared norm is positive.

Thus


$$
\mathcal N>0,
\qquad
d:=v_{29}(\mathcal N)<\infty.
$$



This does not bound $d$. A nonzero vector can have a deeply cancelling $29$-adic sum of squares.

To test the desired law, one needs


$$
\mathcal N\bmod29^{d+1},
\qquad
\mathcal C\bmod29^{d+2}.
$$



If


$$
v_{29}(\mathcal C)<d+1,
$$


alignment fails.

Otherwise define


$$
\boxed{
\delta_{\mathrm{act}}
=
\left(\frac{\mathcal C}{29^{d+1}}\right)
\left(\frac{\mathcal N}{29^d}\right)^{-1}
-\rho_n
\pmod{29}.
}
\tag{13.1}
$$


Only the demonstrated unit $\mathcal N/29^d$ is inverted. Then


$$
\boxed{
\delta_{\mathrm{act}}=0
\iff
\mathcal C-29\rho_n\mathcal N
\in29^2\mathcal N\mathbb Z_{29}.
}
\tag{13.2}
$$



No such actual certificate has been computed here.

The attached material retains $\rho_n=(6C_n)^{-1}$ as an independently established unit, but does not reproduce a complete definition/evaluator for $C_n$. A numerical certificate must therefore include that independently obtained residue; it must not define $\rho_n$ from $M/D$.

---

# 14. Size and practicality

The recurrence improvement is substantial:


$$
H_K=58K+1.
$$


For example,


$$
H_8=465,
$$


whereas


$$
29^8=500246412961.
$$


Thus the recurrence no longer requires even one complete $29^K$-phase table.

This does **not** make the whole original Gram computation small.

- The finite contact inverse remains nonlocal.
- A direct digit-word construction can still have a state set of size $29^{\operatorname{poly}(K)}$.
- Such a bound is an existence statement and can be impractical even at modest $K$.
- The rational kernels in §8 have precision-sized pole orders, but their parameter exponents and coefficient extraction indices remain the actual $n,b$.

Even at $u=0$, the base-$29$ input length is


$$
1+\left\lfloor249005515\log_{29}3\right\rfloor.
$$


Using $3^3<29<3^4$, it lies between roughly $62$ million and $83$ million digits. A complete input scan is itself substantial.

No claim of a practical original Gram implementation is made.

---

# 15. Bounded exact arithmetic proposed for inspection

The following calculations are proposed, not executed.

## A. A new higher-precision reset audit on the actual coefficient prefix

Use


$$
K=2,\qquad n\equiv203\pmod{841},
$$


which is the actual original-family coefficient residue.

Form $T_i$ modulo $841$ for


$$
2\le i\le117,
$$


and the four phase-$2$ blocks


$$
B_q=T_{29q+30}\cdots T_{29q+2},
\qquad q=0,1,2,3.
$$



**Expected verifiable output:**


$$
B_q\bmod29=
\begin{pmatrix}
0&-2&2\\
0&-1&1\\
0&-1&1
\end{pmatrix}
\quad(q=0,1,2,3),
$$


and


$$
\boxed{B_3B_2B_1B_0=0\pmod{841}.}
$$



The receipt should also list the actual pair products modulo $841$, rather than replacing them by zero merely because they vanish modulo $29$.

This uses the actual $n\bmod841$ for transition coefficients only. It must **not** substitute $n=203,b=839$ into high-index source binomials.

This is an implementation audit; Theorem 1 is proved symbolically above.

## B. Rational-kernel coefficient audit

A bounded auxiliary choice such as


$$
n=29,\qquad b=57,\qquad K=2
$$


can compare:

1. source entries obtained from the original finite sum;
2. coefficients from (8.1);
3. $\tau_j$ from direct recurrence;
4. coefficients from (8.2);

for exactly $0\le j<57$.

**Expected verifiable output:** zero discrepancies modulo $841$, with $\tau_0=\tau_1=0$ and source rows ending at $55$.

This checks the new rational-kernel implementation only. It is not an original-family norm calculation.

## C. A bounded original normalized-defect calculation

A declared bounded attempt may use


$$
u=0,\qquad K_{\max}=12.
$$


Its exact inputs are:

- $b=3^{249005515}$, $n=2001b$, with their actual digit streams;
- the complete finite contact system;
- complete initial $r_0,r_1$, or a certified logarithmic omission budget;
- the separate exterior endpoint;
- the independently retained $\rho_n\bmod29$.

Its receipt must report


$$
\mathcal N,\mathcal C\bmod29^{12}.
$$



There are three legitimate output types:

1. **Certified defect:** a nonzero norm digit at $d\le10$, followed by (13.1), or the lower-valuation failure case.
2. **Certified agreement at that one input:** a nonzero norm digit at $d\le10$ and $\delta_{\mathrm{act}}=0$.
3. **Inconclusive precision:** for example,
   

$$
\mathcal N\equiv0\pmod{29^{12}},
$$


   which proves only $d\ge12$.

No expected numerical value of the original defect is asserted. This calculation may remain impractical without a substantially smaller implementation of the actual output kernels.

---

# 16. Final gcd, primitive denominator, and whole error

The least actual two-column clearer remains $d_B$, and the actual integer Gram pair remains


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,
\qquad
H_B=N_{B,1}^T\Omega N_{B,2}.
$$


The final reduction is unchanged:


$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
p_n=\frac{H_B}{g_B},\qquad
q_n=\frac{A_B}{g_B}>0.
}
\tag{16.1}
$$


The primitive multiplier remains $d_B^2/g_B$.

With


$$
\delta=v_{29}(D),\qquad \mu=v_{29}(M),
$$


retain


$$
v_{29}(g_B)
=
\min\{4F_n+4+\delta,\ 2F_n+F_b+5+\mu\},
$$




$$
\boxed{
v_{29}(q_n)
=
\max\{0,\ 2F_n-F_b-1+\delta-\mu\}.
}
\tag{16.2}
$$



A proof of the open relative law would give $\delta=\mu$, because $\rho_n$ is a unit. It would settle only the $29$-part of this denominator accounting.

The full denominator still requires


$$
\boxed{
\log q_n
=
\sum_{\ell}
\max\{v_\ell(A_B)-v_\ell(H_B),0\}\log\ell.
}
\tag{16.3}
$$



For


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
$$


the whole evaluated error remains


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n.
}
\tag{16.4}
$$


At the retained scope of the complete signed-error theorem,


$$
\epsilon_n>0\quad\text{eventually},
$$


and


$$
\log|\epsilon_n|
=
-\left(2+\frac1{2001}\right)n\log(1+\sqrt2)+o(n).
$$



Neither the recurrence reset nor the rational-kernel closure bounds the full primitive denominator sufficiently to show that this whole nonzero evaluated form tends to zero.

---

# Proof-status ledger

| Statement | Status |
|---|---|
| Complete homogeneous $29$-step monodromy, including exceptional phase $1$ | Proved here |
| Actual mod-$29$ source support and equal impulses at phases $26,27$ | Proved here |
| Vanishing phase-$2$ block-end source contribution | Proved here |
| Genuine finite-ring stable image | Proved to be zero |
| Uniform recurrence forgetting after $58K+1$ steps | Proved here |
| Explicit polynomial impulse weights and finite-memory formula | Proved here |
| Rational source/contact kernels and $87K$ particular-input pole bound | Proved here |
| Nonzero conserved periodic homogeneous bilinear form from the reset | Ruled out on the full recurrence state |
| Actual weighted output formulas and endpoint charges | Exact identities |
| Rank-one reset implies Gram alignment | False as an inference; interior and nonlocal output contributions remain |
| Original norm-relative congruence at its true first nonzero norm digit | Open |
| Original nonzero normalized defect | Not computed |
| Full all-prime primitive-denominator/whole-error comparison | Open |

## Conclusion

The new result is not a stable rank-one recurrence channel. It is the opposite:



$$
\boxed{
\text{The actual homogeneous block monodromy is nilpotent,
and its finite-ring stable image is zero.}
}
$$



This yields a useful linear-in-precision finite-memory law and a simpler rational generating-kernel description. It also identifies why the proposed reset cannot, by itself, force the norm/mixed relation: the complete source can vanish at block ends while remaining visible in the interior, and the actual contact inverse transfers those interior entries nonlocally into the weighted outputs.

The exact remaining local bottleneck is the endpoint-sensitive output-kernel identity (11.5), equivalently


$$
\boxed{
\mathcal C-29\rho_n\mathcal N
\in29^2\mathcal N\mathbb Z_{29}
}
$$


at the true first nonzero digit of the original norm.

Even its affirmative resolution would leave the full gcd, actual primitive denominator, and whole same-index error comparison.



$$
\boxed{
\text{An unconditional proof or disproof of irrationality of }e+\pi
\text{ remains unresolved.}
}
$$


