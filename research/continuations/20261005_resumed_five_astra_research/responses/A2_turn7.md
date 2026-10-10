> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2, Turn 7 — A unit-preserving Gram transfer and an evaluated boundary-contraction law

## Executive conclusions

The all-depth complete-force norm factor is **not proved or refuted** here. In particular, I do not obtain an unconditional proof or disproof of irrationality of $e+\pi$.

This turn does, however, replace the unevaluated expressions


$$
B_0=\mathcal RA^{-1}h^{(0)},\qquad
B_1=\mathcal RA^{-1}h^{(1)},\qquad
B_*=\mathcal RA^{-1}\tau+W_be_b
$$


by a **finite-precision arithmetic transfer with explicit initial data and only demonstrated unit inversions**.

The principal new results are:

1. **A bounded-width contact-inverse reduction.**  
   At requested absolute precision $29^K$, the actual contact inverse reduces to:
   - two explicit finite binomial transforms;
   - a monic lower recurrence of order at most $29K-1$;
   - an endpoint correction of dimension at most $29K-1$;
   - a correction matrix congruent to the identity modulo $29$, whose inverse is a finite geometric sum modulo $29^K$.

   No $b\times b$ inverse remains in the evaluation formulas.

2. **An evaluable, unit-sensitive law for all six Gram entries.**  
   The three columns are reconstructed by that transfer, and their Gram matrix is accumulated over exactly $0\le j\le b$. Projection changes only its $(*,*)$-entry:
   

$$
\boxed{
   G=G^{\mathrm{raw}}-\frac{W_b^2}{\mathscr S}e_*e_*^T.
   }
$$


   The transfer retains residues, not merely valuations. It retains the exterior $+1$, all factorial weights, and the actual finite endpoint.

3. **The adjoint factorial-boundary sum is reduced to two evaluated Gram contractions.**  
   Put
   

$$
f=(f_0^0,f_1^0,0)^T,\qquad
   \alpha=\frac{r_0}{f_0^0},\qquad
   \Delta=r_1-\frac{f_1^0}{f_0^0}r_0,
$$


   and define
   

$$
\boxed{
   H_1=f_0^0G_{01}+f_1^0G_{11},\qquad
   H_*=f_0^0G_{0*}+f_1^0G_{1*}.
   }
$$


   Then
   

$$
\boxed{\chi=\Delta H_1+H_*}
$$


   is the complete residual contraction. It includes both the factorial boundary and the true exterior endpoint. The logarithmic contribution remains in the complete $r_0,r_1$.

4. **The reduced force obligation has a direct numerator test.**  
   With
   

$$
P=29^cx,\qquad x^Tx=\mathfrak a\mathfrak b,
   \qquad \mathfrak a\in\mathbb Z_{29}^{\times},
$$


   the exact force residual satisfies
   

$$
\boxed{
   \mathcal E_{\mathrm{force}}
   \in29^3\mathfrak b\,\mathbb Z_{29}
   \quad\Longleftrightarrow\quad
   \chi\in29^{c+5}\mathfrak b\,\mathbb Z_{29}.
   }
$$


   Once this divisibility is justified, the corrected unit-scale condition is equivalently the division-free congruence
   

$$
\boxed{
   \chi+\mathcal N\left(\alpha-29\rho_n\right)
   \in29^2\mathcal N\,\mathbb Z_{29},
   \qquad
   \mathcal N=f^TGf=29^{2c+4}\mathfrak a\mathfrak b.
   }
$$



These are **evaluation and equivalence theorems**, not a proof that the actual family satisfies the two final divisibilities. The remaining obstruction is now the relative valuation of two explicitly transferable scalar quantities, $\mathcal N$ and $\chi$.

No tools were executed.

---

# 1. Domain, accepted inputs, and proof scope

Throughout retain


$$
p=29,\qquad
a=432827+682892t,\quad t\ge0,
$$




$$
b=3^a,\qquad n=2001b,
$$


and the original preferred cylinder


$$
t\equiv364\pmod{841}.
$$



The actual coordinate ranges remain


$$
0\le j\le b
$$


for weighted columns and


$$
0\le i,j<b
$$


for contact vectors.

Write


$$
W_j=\binom{n+2}{j},\qquad
\omega_j=j!W_j,
$$




$$
(Cx)_j=jx_{j-1}-x_j,\qquad x_{-1}=x_b=0,
$$


and


$$
\mathcal R=\operatorname{diag}(W_j)C.
$$



The complete contact equations are


$$
A\theta=f^0,\qquad A\psi=\mathbf r,
\qquad
A=\widetilde N(I+S)^n,
$$


with


$$
Z_w=\mathcal R\theta,\qquad
Y=\mathcal R\psi+W_be_b.
$$


Thus


$$
P=\frac{Z_w}{p^2},\qquad
Q=\frac{Y}{p^3},\qquad
D=P^TP,\qquad M=P^TQ.
$$



The force is the complete one:


$$
\mathbf r=
\frac{h^e+h^F-\widetilde N(I+S)^n(j!)_{0\le j<b}}{b!}.
$$


Its factorial subtraction, logarithmic contribution, and exterior $+1$ are never removed.

I reuse at their stated scope:

- integrality of $A,A^{-1},\theta,\psi$ over $\mathbb Z_{29}$;
- the audited channel transformation and the content-corrected criteria in A4turn15;
- the proven digit product for
  

$$
J=f_0^0=[t^n](1+2t+2t^2)^n,
  \qquad J\in\mathbb Z_{29}^{\times};
$$


- the actual complete terminal residue
  

$$
\psi_{b-1}\equiv0\pmod{29};
$$


- the integral projection
  

$$
\ell_j=\frac{\omega_b}{\omega_j},\qquad
  \mathscr S=\ell^T\ell\equiv8\pmod{29},\qquad
  \Pi=I-\frac{\ell\ell^T}{\mathscr S}.
$$



No restriction is imposed on the higher base-$29$ digits of $n$ or $b$. In particular, the digit-product theorem is not replaced by a smaller cylinder.

The fixed-degree nearest-neighbor route is not reopened.

---

# 2. The finite displacement needed below

For clarity, the Turn 6 identities used in this report can be checked directly from the supplied contact formulas. Only their short algebraic verification is needed here.

Put


$$
\phi(z)=1-z+\frac{z^2}{2}.
$$


Define


$$
\alpha_i=2n+2i+1,
$$




$$
\beta_i=\frac{(n+i)(n+3i-1)}2,\qquad
\gamma_i=\frac{(n+i)(n+i-1)(1-i)}2.
$$


For exactly


$$
1\le i\le b-2,
$$


let


$$
(\mathcal Dh)_i
=h_{i+1}-\alpha_i h_i+\beta_i h_{i-1}+\gamma_i h_{i-2}.
$$


At $i=1$, $\gamma_1=0$; that row uses only $h_0,h_1,h_2$.

Define


$$
B_j^{(m)}(z)=\sum_{k=0}^j\binom m{j-k}\frac{z^k}{k!}.
$$


The contact formula is


$$
A_{ij}
=(n+i)![z^{n+i}]\phi(z)^ne^zB_j^{(n)}(z).
$$


The elementary identity


$$
(1-z)(B_j^{(n)})'-(n+z)B_j^{(n)}
=
B_j^{(n+1)}-(j+1)B_{j+1}^{(n+1)}
$$


therefore gives


$$
\boxed{\mathcal DA=-\mathcal VC,}
\tag{2.1}
$$


where


$$
\mathcal V_{ik}
=(n+i)![z^{n+i}]
\phi(z)^{n+1}e^zB_k^{(n+1)}(z),
$$


with


$$
1\le i\le b-2,\qquad 0\le k\le b.
$$



The last column $k=b$ is essential.

The complete source is


$$
\boxed{
\mathcal H_i=(\mathcal Ve_b)_i
=
\sum_s[z^s]\phi(z)^{n+1}
(n+i)_{\underline s}
\binom{2n+i-s+1}{b}.
}
\tag{2.2}
$$



For the logarithmic part, if


$$
F(z)=4\arctan\frac{z}{2-z},
$$


then


$$
\phi F'=2.
$$


Writing


$$
P_n(z)=\phi(z)^{n+1}F^{(n+1)}(z)
$$


gives


$$
P_0=2,\qquad
P_{n+1}=\phi P_n'-(n+1)\phi'P_n,
$$


hence $\deg P_n\le n$. Its coefficients in degrees $n+i$, $i\ge1$, vanish exactly. Consequently


$$
\boxed{
\mathcal Df^0=0,\qquad
\mathcal D\mathbf r=\mathcal H.
}
\tag{2.3}
$$



This confirms the displacement and the two-initial-value complete-force reduction at the finite scope used below. It does not establish a norm factor.

---

# 3. Initial data for the three actual columns

Let $h^{(0)},h^{(1)}$ solve the homogeneous recurrence with


$$
(h^{(0)}_0,h^{(0)}_1)=(1,0),\qquad
(h^{(1)}_0,h^{(1)}_1)=(0,1).
$$


Let $\tau$ solve


$$
\mathcal D\tau=\mathcal H,\qquad \tau_0=\tau_1=0.
$$



The first forward step is written separately:


$$
h_2=\alpha_1h_1-\beta_1h_0+\text{source}_1.
$$


Subsequent steps use


$$
h_{i+1}
=\alpha_i h_i-\beta_i h_{i-1}-\gamma_i h_{i-2}
+\text{source}_i,
\qquad 2\le i\le b-2.
$$


Thus there is no implicit negative initial index.

Set


$$
\mathcal B=(B_0,B_1,B_*),
$$


where the exact rational columns are


$$
B_0=\mathcal RA^{-1}h^{(0)},\qquad
B_1=\mathcal RA^{-1}h^{(1)},\qquad
B_*=\mathcal RA^{-1}\tau+W_be_b.
$$


Then


$$
Z_w=\mathcal Bf,\qquad
Y=\mathcal Br,
\tag{3.1}
$$


where


$$
f=(f_0^0,f_1^0,0)^T,\qquad
r=(r_0,r_1,1)^T.
$$



The next sections give an arithmetic evaluation of these columns and their Gram matrix, rather than leaving $A^{-1}$ in their definitions.

## 3.1 The complete initial force entries

For $i=0,1$, the input $r_i$ is


$$
r_i=
\sum_s a_s(n)(n+i)_{\underline s}
\left(T_{2n+i-s}+\frac{L_{2n+i-s}}{b!}\right),
\tag{3.2}
$$


where


$$
a_s(n)=[z^s]\phi(z)^n,
$$




$$
T_m=\frac1{b!}\sum_{q=b}^m(m)_{\underline q},
$$


and


$$
L_0=0,\qquad
L_m=mL_{m-1}+2(m-1)!u_{m-1},
$$




$$
u_0=u_1=1,\qquad
u_m=u_{m-1}-\frac12u_{m-2}.
$$



These are complete values, not only their residues modulo $29$.

The proven reduction of the full force modulo $29$ gives


$$
r_0\equiv0\pmod{29}.
$$


Since $f_0^0=J$ is a unit,


$$
\boxed{\alpha:=r_0/f_0^0\in29\mathbb Z_{29}.}
\tag{3.3}
$$



A logarithmic term may be replaced by zero at a specified precision only when its proved whole-force valuation bound exceeds that precision. Exact interior homogeneity does not make these initial terms zero.

---

# 4. A finite-precision factorization of the actual contact matrix

This is the main computational reduction.

Fix a requested absolute precision $p^K$, $K\ge1$, and put


$$
m=\min(2n,pK-1),\qquad t_0=\min(m,b).
\tag{4.1}
$$



All congruences in Sections 4–6 are modulo $p^K$.

Let


$$
\mathsf P_{ij}=\binom ij,\qquad
T_{ij}=\binom n{j-i},\qquad 0\le i,j<b.
$$


Thus


$$
T=(I+S)^n,
$$


and


$$
(T^{-1})_{ij}=\binom{-n}{j-i},\qquad
(\mathsf P^{-1})_{ij}=(-1)^{i-j}\binom ij
$$


in their respective triangular ranges.

These are exact finite matrices with integral inverses.

## 4.1 Uniform truncation by falling-factorial divisibility

For every nonnegative integer $q$,


$$
v_p\bigl((q+s)!/q!\bigr)\ge\lfloor s/p\rfloor.
$$


Likewise, any nonzero falling factorial of length $s$ has valuation at least $\lfloor s/p\rfloor$.

Since $a_s(n)\in\mathbb Z_{29}$, all terms with $s\ge pK$ vanish modulo $p^K$. This is a uniform truncation statement for the matrix entries, not a truncation inferred from a particular evaluated force.

The coefficient identity


$$
(n+i)_{\underline s}\binom{n+i-s}{j}
=\frac{(j+s)!}{j!}\binom{n+i}{j+s}
$$


and finite differences give


$$
\boxed{
(\mathsf P^{-1}\widetilde N)_{ij}
\equiv
\sum_{s=0}^{m}
a_s(n)\frac{(j+s)!}{j!}\binom n{j+s-i}.
}
\tag{4.2}
$$



## 4.2 Interior band and true endpoint correction

Define a lower triangular band matrix $H$ by


$$
H_{kj}=
\begin{cases}
a_{k-j}(n)\dfrac{k!}{j!},&0\le k-j\le m,\\
0,&\text{otherwise},
\end{cases}
\qquad 0\le k,j<b.
\tag{4.3}
$$


Its diagonal entries are $1$.

The terms with $j+s\ge b$ form the endpoint correction. Define


$$
K^{\mathrm{tail}}_{rj}=
\begin{cases}
a_{b+r-j}(n)\dfrac{(b+r)!}{j!},
&1\le b+r-j\le m,\\
0,&\text{otherwise},
\end{cases}
\tag{4.4}
$$


for


$$
0\le r<m,\qquad0\le j<b,
$$


and


$$
T^{\mathrm{tail}}_{ir}=\binom n{b+r-i}.
\tag{4.5}
$$


Then


$$
\mathsf P^{-1}\widetilde N
\equiv TH+T^{\mathrm{tail}}K^{\mathrm{tail}}.
\tag{4.6}
$$



This formula retains every term crossing the actual last contact column.

Put


$$
F=T^{-1}T^{\mathrm{tail}}.
$$


The entries of $F$ have the short endpoint formula


$$
\boxed{
F_{jr}
=
-\sum_{u=0}^{r}
\binom{-n}{b+u-j}\binom n{r-u}.
}
\tag{4.7}
$$



### Proof of (4.7)

The full coefficient convolution is


$$
\sum_{\ell=j}^{b+r}
\binom{-n}{\ell-j}\binom n{b+r-\ell}=0,
$$


because $b+r-j>0$. The actual finite matrix product stops at $\ell=b-1$. Moving the remaining terms $\ell=b,\ldots,b+r$ to the other side gives (4.7). ∎

Thus no long inverse contraction is hidden in $F$: each entry uses at most $m$ terms.

Only the last $t_0$ columns of $K^{\mathrm{tail}}$ can be nonzero. Let $E$ select those coordinates:


$$
(Ey)_v=y_{b-t_0+v},\qquad0\le v<t_0,
$$


and write


$$
K^{\mathrm{tail}}=\overline K E.
$$


Define


$$
L=F\overline K.
\tag{4.8}
$$


Combining the formulas gives the finite-precision factorization


$$
\boxed{
A\equiv\mathsf P\,T\,(H+LE)\,T.
}
\tag{4.9}
$$



The only nonbanded correction inside the middle factor has $t_0\le pK-1$ columns.

---

# 5. Why every inversion in the reduced transfer is a unit inversion

For $1\le s<p$, Frobenius and $p\mid n$ give


$$
a_s(n)\equiv0\pmod p.
$$


For $s\ge p$, the factorial quotient in (4.3) or (4.4) is divisible by $p$. Therefore


$$
\boxed{
H\equiv I\pmod p,\qquad
K^{\mathrm{tail}}\equiv0\pmod p,\qquad
L\equiv0\pmod p.
}
\tag{5.1}
$$



Let


$$
\Gamma=H^{-1}L.
$$


Then


$$
\Gamma\equiv0\pmod p.
$$


Consequently the endpoint matrix


$$
S_{\mathrm{end}}=I_{t_0}+E\Gamma
$$


satisfies


$$
\boxed{S_{\mathrm{end}}\equiv I_{t_0}\pmod p.}
\tag{5.2}
$$



Its inverse is explicitly


$$
\boxed{
S_{\mathrm{end}}^{-1}
\equiv
\sum_{q=0}^{K-1}(-E\Gamma)^q\pmod{p^K}.
}
\tag{5.3}
$$



In particular, the reduction does not divide by a contact minor that might contain part of the primitive norm.

---

# 6. Explicit transfer for the three columns and their Gram entries

For each input


$$
h\in\{h^{(0)},h^{(1)},\tau\},
$$


perform the following steps.

## 6.1 Two explicit finite binomial transforms

First set


$$
\beta_j(h)=\sum_{i=0}^{j}(-1)^{j-i}\binom ji h_i,
\tag{6.1}
$$


and then


$$
g_j(h)=\sum_{k=j}^{b-1}\binom{-n}{k-j}\beta_k(h).
\tag{6.2}
$$


These are exactly


$$
g(h)=T^{-1}\mathsf P^{-1}h.
$$



They retain their complete finite ranges. They are classical transforms, not new locality assertions.

## 6.2 A monic recurrence of order at most $pK-1$

Solve $Hv(h)=g(h)$ by


$$
\boxed{
v_j(h)
=
g_j(h)
-\sum_{s=1}^{\min(m,j)}
a_s(n)\,j_{\underline s}\,v_{j-s}(h).
}
\tag{6.3}
$$



Similarly, every column of $\Gamma=H^{-1}L$ is obtained from


$$
\boxed{
\Gamma_{jv}
=
L_{jv}
-\sum_{s=1}^{\min(m,j)}
a_s(n)\,j_{\underline s}\,\Gamma_{j-s,v}.
}
\tag{6.4}
$$



The leading coefficient is $1$. No loss of $29$-adic precision occurs in these recurrences.

## 6.3 The endpoint solve and the final transform

Set


$$
u(h)=S_{\mathrm{end}}^{-1}Ev(h),
$$




$$
y(h)=v(h)-\Gamma u(h),
$$


and


$$
\boxed{
\zeta_j(h)
=
\sum_{k=j}^{b-1}\binom{-n}{k-j}y_k(h).
}
\tag{6.5}
$$



Then (4.9) proves


$$
\boxed{\zeta(h)\equiv A^{-1}h\pmod{p^K}.}
\tag{6.6}
$$



This is an evaluable replacement for the previously unevaluated inverse definitions.

### Scope of the bounded-order claim

The lower recurrence and endpoint correction have order or dimension bounded by $pK-1$, independently of $b$. The explicit binomial transforms still range over the original finite interval. I do **not** claim that the entire computation has runtime, storage, or a single streaming state dimension bounded independently of $b$.

That stronger compression remains unavailable here.

## 6.4 Reconstruction and six-scalar Gram accumulation

Collect the three solutions in row vectors


$$
\zeta_j=
\bigl(\zeta_j(h^{(0)}),\zeta_j(h^{(1)}),\zeta_j(\tau)\bigr).
$$


Use


$$
\zeta_{-1}=\zeta_b=0
$$


only for reconstruction, and define


$$
\boxed{
\mathbf B_j
=
W_j\left(j\zeta_{j-1}-\zeta_j+\mathbf1_{j=b}e_*^T\right).
}
\tag{6.7}
$$



At the actual upper endpoint this is


$$
\boxed{
\mathbf B_b=W_b\left(b\zeta_{b-1}+e_*^T\right).
}
\tag{6.8}
$$


The complete $+1$ is visible.

Starting with $G^{(0)}=0$, accumulate


$$
\boxed{
G^{(j+1)}=G^{(j)}+\mathbf B_j^T\mathbf B_j,
\qquad 0\le j\le b.
}
\tag{6.9}
$$


Then


$$
G^{\mathrm{raw}}\equiv G^{(b+1)}
\equiv\mathcal B^T\mathcal B\pmod{p^K}.
$$



The charges are exactly


$$
\ell^TB_0=\ell^TB_1=0,\qquad
\ell^TB_*=W_b.
$$


Therefore the projected Gram matrix is


$$
\boxed{
G:=(\Pi\mathcal B)^T(\Pi\mathcal B)
=
G^{\mathrm{raw}}-\frac{W_b^2}{\mathscr S}e_*e_*^T.
}
\tag{6.10}
$$



Thus all six entries are evaluated modulo $p^K$ by the transfer. Projection requires only the demonstrated unit $\mathscr S^{-1}$.

### Coefficient generation without unsafe modular division

If desired, generate $a_s(n)$ by


$$
\boxed{
a_s(n)=(-1)^s
\sum_{v=0}^{\lfloor s/2\rfloor}
2^{-v}\binom n{s-v}\binom{s-v}{v}.
}
\tag{6.11}
$$


Only powers of $2$ occur as denominators. Binomial coefficients and factorial quotients in the transfer are evaluated as integers before reduction.

A recurrence involving division by $s+1$ must not be implemented by inverting $s+1$ modulo $29^K$ when $29\mid s+1$.

---

# 7. The lattice issue: what is saturated and what is not

The three-dimensional rational reduction does not authorize replacing the actual weighted lattice by $\mathbb Z_{29}^3$.

There is, however, a precise distinction worth recording.

## 7.1 The unweighted kernel basis is integral and saturated

Let


$$
q_0=CA^{-1}h^{(0)},\qquad
q_1=CA^{-1}h^{(1)},\qquad
q_*=CA^{-1}\tau+e_b.
$$


Then these form a $\mathbb Z_{29}$-basis of


$$
\ker(\mathcal V:\mathbb Z_{29}^{b+1}\to\mathbb Z_{29}^{b-2}).
\tag{7.1}
$$



### Proof

The square matrix $[C,e_b]$ has determinant $(-1)^b$, so every integral $q$ has a unique decomposition


$$
q=Cx+\kappa e_b,\qquad x\in\mathbb Z_{29}^b,\quad\kappa\in\mathbb Z_{29}.
$$


The equation $\mathcal Vq=0$ becomes, by (2.1),


$$
\mathcal D(Ax)=\kappa\mathcal H.
$$


The monic forward recurrence then gives uniquely


$$
Ax=\eta_0h^{(0)}+\eta_1h^{(1)}+\kappa\tau
$$


with integral $\eta_0,\eta_1$. This proves (7.1). ∎

This conclusion is justified by the actual integral maps, not merely by rational rank.

## 7.2 Weighting changes the lattice

The weighted basis is


$$
\mathcal B=\operatorname{diag}(W_j)(q_0,q_1,q_*).
$$


Its saturated coefficient lattice is


$$
\boxed{
\Lambda_{\mathrm{wt}}
=
\left\{
s\in\mathbb Q_{29}^3:
\mathbf B_js\in\mathbb Z_{29}
\text{ for every }0\le j\le b
\right\}.
}
\tag{7.2}
$$


It need not equal $\mathbb Z_{29}^3$.

Likewise, projection must be applied to the actual weighted columns; it does not justify assuming an integral contact pullback.

The transfer in Sections 4–6 never substitutes a saturated surrogate for the actual columns. It preserves every $W_j$, every factorial quotient, and every coefficient $f_0^0,f_1^0,r_0,r_1,1$.

If an integral basis change is made to study (7.2), its inverse change must also be applied to these coefficient vectors, and its Gram congruence must be retained. A Smith-form computation at one precision determines only the invariant factors visible at that precision.

---

# 8. Evaluating the adjoint boundary contraction by the Gram transfer

This is where the displacement identity advances the reduced force obligation.

Write


$$
\widehat{\mathcal B}=\Pi\mathcal B,
\qquad
\widehat B_*=\Pi B_*.
$$


The first two columns already have zero charge, so


$$
\widehat B_0=B_0,\qquad \widehat B_1=B_1.
$$



Let


$$
P=p^cx,\qquad x\ \text{primitive},
$$


and use the audited unit-only channel transformation:


$$
x^Tx=\mathfrak a\mathfrak b,\qquad
\mathfrak a\in\mathbb Z_{29}^{\times},\qquad
\mathfrak b\ne0.
$$



Let $\mathfrak u(y)=y_r+\iota y_s$, with the actual coordinate choice and sign of $\iota$ used to make $\mathfrak a$ a unit. The coefficient vector $d$ of the other channel satisfies the useful exact identity


$$
\boxed{
d=\frac{2x}{\mathfrak a}
-\frac{\mathfrak b}{\mathfrak a}\,u_{\mathrm{row}},
}
\tag{8.1}
$$


where $u_{\mathrm{row}}^Ty=\mathfrak u(y)$.

This is simply the audited polarization identity written as a linear functional:


$$
2x^Ty=\mathfrak a\,\mathfrak v(y)+\mathfrak b\,\mathfrak u(y).
$$



## 8.1 Two boundary invariants

Define


$$
H_1=f^TGe_1
=f_0^0G_{01}+f_1^0G_{11},
$$




$$
H_*=f^TGe_*
=f_0^0G_{0*}+f_1^0G_{1*}.
\tag{8.2}
$$


Since $Z_w=p^{c+2}x$,


$$
H_1=Z_w^TB_1,\qquad
H_*=Z_w^T\widehat B_*.
$$



Also define the two coordinate-channel values


$$
s_1=\mathfrak u(B_1),\qquad
s_*=\mathfrak u(\widehat B_*).
\tag{8.3}
$$


They are evaluated from the same reconstructed rows. In particular,


$$
s_*=
\mathfrak u(B_*)-\frac{W_b}{\mathscr S}\mathfrak u(\ell).
$$


The projection endpoint is not omitted.

## 8.2 Identification with the adjoint invariants

Retain the actual adjoint decomposition


$$
A^Tz=\mathcal R^T\Pi d,
\qquad
z=\mathcal D^T\lambda+\eta_0e_0+\eta_1e_1.
$$


Because $h^{(1)}$ is homogeneous and has initial data $(0,1)$,


$$
z^Th^{(1)}=\eta_1.
$$


The adjoint equation also gives


$$
z^Th^{(1)}=d^TB_1.
$$


Using (8.1),


$$
\boxed{
\eta_1
=
\frac{2H_1}{p^{c+2}\mathfrak a}
-\frac{\mathfrak b}{\mathfrak a}s_1.
}
\tag{8.4}
$$



Similarly, $\tau_0=\tau_1=0$ and $\mathcal D\tau=\mathcal H$ imply


$$
z^T\tau=\lambda^T\mathcal H.
$$


Consequently


$$
\lambda^T\mathcal H+W_b(\Pi d)_b
=d^T\widehat B_*,
$$


and hence


$$
\boxed{
\sum_{i=1}^{b-2}\lambda_i\mathcal H_i
+W_b(\Pi d)_b
=
\frac{2H_*}{p^{c+2}\mathfrak a}
-\frac{\mathfrak b}{\mathfrak a}s_*.
}
\tag{8.5}
$$



Equations (8.4)–(8.5) are the requested boundary contraction. Their right sides are evaluated by the bounded-width transfer and Gram accumulation; they no longer require solving the adjoint system or summing its factorial boundary force.

Although the right sides display a power of $p$ in a denominator, their equality to integral quantities is proved. Computation at a finite precision must retain the corresponding guard digits.

---

# 9. The complete reduced force in two scalar contractions

Put


$$
\alpha=\frac{r_0}{f_0^0},\qquad
\Delta=r_1-\frac{f_1^0}{f_0^0}r_0.
$$


Then the full residual vector is


$$
U:=Y^\parallel-\alpha Z_w
=\Delta B_1+\widehat B_*.
\tag{9.1}
$$


Define


$$
\boxed{
\chi:=Z_w^TU=\Delta H_1+H_*,
}
\tag{9.2}
$$


and


$$
s_U:=\mathfrak u(U)=\Delta s_1+s_*.
\tag{9.3}
$$



The Turn 6 residual is therefore exactly


$$
\boxed{
\mathcal E_{\mathrm{force}}
=
\frac{2\chi}{p^{c+2}\mathfrak a}
-\frac{\mathfrak b}{\mathfrak a}s_U.
}
\tag{9.4}
$$



This identity combines the complete initial mismatch, factorial-boundary sum, and exterior endpoint. Its coefficient $\alpha$ is still the independently determined initial-force ratio, not $M/D$.

## 9.1 A divisibility that is already justified

We have


$$
Y^\parallel\in p^3\mathbb Z_p^{b+1},
\qquad
Z_w\in p^{c+2}\mathbb Z_p^{b+1},
\qquad
\alpha\in p\mathbb Z_p.
$$


Therefore


$$
\boxed{U\in p^3\mathbb Z_p^{b+1},\qquad s_U\in p^3\mathbb Z_p.}
\tag{9.5}
$$



It follows that the second term in (9.4) already belongs to


$$
p^3\mathfrak b\,\mathbb Z_p.
$$


Since $2/\mathfrak a$ is a unit,


$$
\boxed{
\mathcal E_{\mathrm{force}}
\in p^3\mathfrak b\,\mathbb Z_p
\iff
\chi\in p^{c+5}\mathfrak b\,\mathbb Z_p.
}
\tag{9.6}
$$



Thus the outstanding norm factor is now a test on the evaluated Gram contraction $\Delta H_1+H_*$.

The factor $\mathfrak b$ is still the entire primitive-norm factor. It has not been replaced by a basis determinant or by common column content.

---

# 10. The corrected unit-scale congruence

Let


$$
\mathcal N:=f^TGf=Z_w^TZ_w
=p^{2c+4}\mathfrak a\mathfrak b.
\tag{10.1}
$$


Then


$$
\chi
=Z_w^T(Y^\parallel-\alpha Z_w)
=p^5M-\alpha p^4D.
\tag{10.2}
$$



The full channel identity is


$$
p^3\mathfrak v
=\alpha p^{c+2}\mathfrak b+\mathcal E_{\mathrm{force}}.
$$


After (9.6) has justified the division by $\mathfrak b$,


$$
\frac{\mathfrak v}{\mathfrak b}
=
\alpha p^{c-1}
+\frac{2\chi}{p^{c+5}\mathfrak a\mathfrak b}
-\frac{s_U}{p^3\mathfrak a}.
$$


Also


$$
\mathfrak u(Q^\parallel)
=\alpha p^{c-1}\mathfrak a+\frac{s_U}{p^3}.
$$


The coordinate-channel terms cancel in the unit-scale condition. Hence the audited condition


$$
\mathfrak a\frac{\mathfrak v}{\mathfrak b}
+\mathfrak u(Q^\parallel)
-2\rho_np^c\mathfrak a
\in p^{c+1}\mathbb Z_p
$$


is equivalent to


$$
\mathfrak a p^{c-1}(\alpha-p\rho_n)
+\frac{\chi}{p^{c+5}\mathfrak b}
\in p^{c+1}\mathbb Z_p.
$$



Multiplying by the justified denominator gives the safer numerator formulation:


$$
\boxed{
\chi+\mathcal N(\alpha-p\rho_n)
\in p^2\mathcal N\,\mathbb Z_p.
}
\tag{10.3}
$$



This retains the unit information. A valuation comparison alone would not establish (10.3).

Indeed,


$$
\chi+\mathcal N(\alpha-p\rho_n)
=p^5(M-\rho_nD),
$$


so (10.3) has exactly the desired relative precision.

## 10.1 Arbitrary second-column content removal

No second-column content was removed in deriving (9.6)–(10.3). Thus these statements use the original normalization $Q^\parallel$.

If instead


$$
Q^\parallel=p^dy,\qquad y\in\mathbb Z_p^{b+1},
$$


the channel tests must be rescaled exactly as in A4turn15:

- if $d\le c$, use the factor $p^{c-d}$ in the unit-scale condition;
- if $d>c$, first require $v_p(\mathfrak b)\ge d-c$, then divide the norm factor by $p^{d-c}$.

The numerator identity (10.3), when evaluated using the original columns, automatically preserves all such content. It is not altered by choosing a different bookkeeping normalization for $y$.

---

# 11. Precision requirements and the remaining local lemma

Let


$$
\nu=v_p(\mathfrak b).
$$


Then


$$
v_p(\mathcal N)=2c+4+\nu.
$$



For a fixed original index, once $c$ and $\nu$ have been determined from nonzero digits, the two local questions are:

1. **Norm factor**
   

$$
\boxed{
   \chi\equiv0\pmod{p^{c+5+\nu}}.
   }
   \tag{11.1}
$$



2. **Relative unit**
   

$$
\boxed{
   \chi+\mathcal N(\alpha-p\rho_n)
   \equiv0\pmod{p^{2c+6+\nu}}.
   }
   \tag{11.2}
$$



Thus an absolute Gram computation through


$$
\boxed{K=2c+6+\nu}
\tag{11.3}
$$


suffices for the numerator tests, provided all initial inputs are supplied at the needed precision.

Using (11.2) directly avoids unnecessary precision loss from separately computing normalized channel quotients.

There is no uniform bound on $\nu$ in the supplied work. Accordingly, a fixed $K$ cannot settle every original index.

## Concrete follow-on lemma

> **Actual endpoint-sensitive Gram congruence lemma — open.**  
> For every original index in the preferred cylinder, evaluate $G$ by Sections 4–6, retain the complete initial data $\alpha,\Delta$, and prove
> 

$$
> \Delta H_1+H_*
> \in p^{c+5}\mathfrak b\,\mathbb Z_p,
>
$$


> followed by
> 

$$
> \Delta H_1+H_*+\mathcal N(\alpha-p\rho_n)
> \in p^2\mathcal N\,\mathbb Z_p.
>
$$



This is non-tautological as an evaluation problem: $H_1,H_*,\mathcal N$ are obtained without $A^{-1}$, without the adjoint factorial sum, and without defining a coefficient from $M/D$.

It remains unproved as a uniform congruence theorem.

### Precise obstruction to claiming more

The transfer proves that the Gram entries can be evaluated to any prescribed absolute precision. It does not prove that the residual contraction vanishes to a precision tied to the *first nonzero digit of the actual primitive norm*.

Neither:

- the rank-three rational reduction;
- the saturated unweighted kernel basis;
- the unit endpoint solve;
- nor the channel isometry

forces


$$
v_p(\chi)\ge c+5+\nu.
$$



A successful next proof must exploit additional structure in the transferred Gram entries or in their dependence on the original exponential parameter. Merely increasing a common zero depth does not supply that relative statement.

---

# 12. Bounded exact arithmetic for personal inspection

No original-column calculation has been executed. The following bounded check tests the new transfer itself, not the original-family norm factor.

## 12.1 Auxiliary implementation check of the Gram transfer

Use


$$
p=29,\qquad n=29,\qquad b=4,\qquad K=2.
$$



This is deliberately **not** an original-family index. Its role is to inspect a finite algebraic identity with nontrivial precision and finite boundaries.

### Inputs

1. Form the exact $4\times4$ matrix
   

$$
A_{ij}
   =(29+i)![z^{29+i}]
   \phi(z)^{29}e^zB_j^{(29)}(z).
$$



2. Form $h^{(0)},h^{(1)},\tau$ from the recurrence in Section 3, with the complete source $\mathcal H_1,\mathcal H_2$.

3. Run Sections 4–6 modulo $29^2$. Here
   

$$
m=57,\qquad t_0=4.
$$



4. Independently compute the three contact solutions over $\mathbb Q$, reconstruct the three weighted columns, and form their exact Gram matrix.

5. For projection use the actual auxiliary normal vector
   

$$
\ell_j=\frac{(31-j)!}{27!};
$$


   do not substitute the original-family residue $\mathscr S\equiv8$. Here $\mathscr S\equiv2\pmod{29}$.

### Expected verifiable outputs

- Exact zero modulo $29^2$ for
  

$$
A-\mathsf P\,T(H+LE)T.
$$



- Exact zero modulo $29^2$ for all three residuals
  

$$
A\zeta(h)-h.
$$



- Exact zero modulo $29^2$ for the difference between the transferred and directly formed projected Gram matrices.

- The common reduction modulo $29$ is
  

$$
\boxed{
  G\equiv
  \begin{pmatrix}
  21&19&0\\
  19&5&0\\
  0&0&0
  \end{pmatrix}
  \pmod{29}.
  }
  \tag{12.1}
$$



For example, modulo $29$, the first two weighted columns in this check are


$$
B_0=(-1,4,-2,0,0)^T,\qquad
B_1=(0,-2,1,0,0)^T,
$$


while $B_*\equiv0$. These give (12.1).

This check cannot establish (11.1) or (11.2) on any original index.

## 12.2 Optional complete-force check in the same bounded example

Generate $u_m,L_m,T_m$ through $m=59$, using their exact recurrences, and form the complete $r_0,r_1$ from (3.2). Then verify


$$
Y=r_0B_0+r_1B_1+B_*
$$


against direct reconstruction from the complete force.

The expected output is exact zero. This specifically checks that the logarithmic initial data and factorial subtraction have not been lost.

Again, it is a finite formula check only.

---

# 13. Finite endpoints, full content, final gcd, and whole error

The new transfer uses exactly $b$ contact entries and $b+1$ weighted entries. It does not extend a terminal block. If the original high-block size is $29^4$, the final block is still shortened at $j=b$.

The endpoint correction in Section 4 is caused by terms crossing the actual contact boundary. It is not an artificial completion of the last block.

The primitive norm remains


$$
D=p^{2c}\mathfrak a\mathfrak b,
$$


so all additional primitive cancellation remains in $\mathfrak b$.

Retain the least actual two-column clearer


$$
N_B=d_B[u,v],\qquad v_{29}(d_B)=0,
$$


and the actual integer pair


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2}.
$$


The final normalization is unchanged:


$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
p_n=H_B/g_B,\qquad q_n=A_B/g_B>0.
}
\tag{13.1}
$$



With


$$
\delta=v_{29}(D),\qquad \mu=v_{29}(M),
$$


the retained local interface is


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
\tag{13.2}
$$



The present transfer does not establish $\delta=\mu$ uniformly. Even if the open Gram congruence lemma were proved, it would settle only this local contribution.

The full denominator is still governed by


$$
\boxed{
\log q_n
=
\sum_{\ell}
\max\{v_\ell(A_B)-v_\ell(H_B),0\}\log\ell.
}
\tag{13.3}
$$


No all-prime bound for this sum is obtained here.

Norm nonvanishing follows from the nonzero first column and its positive real norm. Mixed nonvanishing retains its supplied original-family dependency.

For


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
$$


the whole evaluated error remains


$$
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n.}
\tag{13.4}
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



No individual exponential, logarithmic, or endpoint component is substituted for this whole error.

---

# Final proof-status ledger

| Statement | Status in this report |
|---|---|
| Finite displacement $\mathcal DA=-\mathcal VC$, with $k=b$ retained | Algebraically checked from the supplied contact formula |
| Complete recurrence with two initial values | Checked at the actual finite range |
| $J=f_0^0$ unit and actual $\psi_{b-1}$ residue | Reused at their proven scope |
| Contact inverse modulo $29^K$ reduced to band recurrence plus bounded endpoint correction | Proved |
| Endpoint correction matrix is a unit, with finite geometric inverse | Proved |
| All six projected Gram entries evaluable by explicit finite arithmetic | Proved as a transfer law |
| Saturated unweighted kernel basis | Proved |
| Weighted coefficient lattice equals $\mathbb Z_{29}^3$ | Not asserted |
| Adjoint factorial-boundary sum reduced to $H_1,H_*$ and two coordinate channels | Proved |
| $\mathcal E_{\mathrm{force}}\in29^3\mathfrak b\mathbb Z_{29}$ iff $\chi\in29^{c+5}\mathfrak b\mathbb Z_{29}$ | Proved |
| Corrected unit-scale condition as the numerator congruence (10.3) | Proved |
| Actual family satisfies these two divisibilities | Open |
| Full all-prime gcd and primitive-denominator comparison | Open |
| Whole nonzero evaluated form tends to zero | Open |

## Conclusion

The new result is an **endpoint-exact, unit-sensitive finite-precision Gram transfer**, together with a boundary-contraction law that replaces the adjoint factorial sum by two evaluable Gram invariants:


$$
H_1,\qquad H_*.
$$



The exact local bottleneck is now


$$
\boxed{
\chi=\Delta H_1+H_*
\in29^{c+5}\mathfrak b\,\mathbb Z_{29},
}
$$


followed by


$$
\boxed{
\chi+\mathcal N(\alpha-29\rho_n)
\in29^2\mathcal N\,\mathbb Z_{29}.
}
$$



The transfer evaluates these quantities at any prescribed absolute precision, but no uniform theorem yet compares their first nonzero digits. That relative comparison—not another fixed-degree skew-operator search—is the next mathematical obligation.

Even its affirmative resolution would leave the all-prime primitive denominator and the whole same-index error to be compared.



$$
\boxed{
\text{An unconditional proof or disproof of irrationality of }e+\pi
\text{ remains unresolved.}
}
$$


