> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5, turn 9 — The exact final normalization and a canonical ternary factorial obstruction

## Executive conclusions

The recovered source closes the RAW-to-FINAL bridge. It also makes possible a new all-prime advance: an exact evaluation at the prime $3$, valid on the entire original family.

Throughout,


$$
b=9^{18+32u}=3^{36+64u},\qquad n=4002b,\qquad u\ge0.
$$



The main conclusions are as follows.

1. **The documentary identification is correct.** The current complete normalized first force is exactly
   

$$
f=\frac{f^0}{R}.
$$


   This follows from the exact central-coefficient formula and the complete first-force construction, not from a comparison of Gram residues. The complete reconstructed columns satisfy
   

$$
X_{\rm raw}=\frac{Z_w}{R},\qquad
   Y_{\rm raw}=\frac{V_w}{b!},
$$


   including the factorial subtraction, both complete forces, the finite inverse, and the terminal $+1$.

2. **The actual prescribed final Gram forms are**
   

$$
\boxed{
   A_B=d_B^2\,4\lambda^2R^2N,\qquad
   H_B=d_B^2\,8\lambda Rb!H.
   }
$$


   Here $d_B$ is the least common denominator of every coefficient of the actual columns $u,v$. No independent row-content division is prescribed or introduced.

3. **The normalization scalar is the reciprocal of an integer.** Define
   

$$
\boxed{
   \mathscr D_n
   =\frac{\lambda R}{2b!}
   =\frac{(n!)^2\binom n{n/2}}{2^{n/2+1}b!}\in\mathbb Z_{>0}.
   }
$$


   Then
   

$$
\boxed{\frac{p_n}{q_n}=\frac1{\mathscr D_n}\frac HN.}
$$


   If $H/N=p_{\rm r}/q_{\rm r}$ is reduced, with $q_{\rm r}>0$, then the actual final denominator is
   

$$
\boxed{
   q_n=\frac{\mathscr D_n q_{\rm r}}
                {\gcd(\mathscr D_n,|p_{\rm r}|)}.
   }
$$


   This retains every odd factorial factor.

4. **The displayed final binary denominator interface is now unconditional as a normalization identity:**
   

$$
\boxed{
   v_2(q_n)=
   \max\!\left\{
   C_n+v_2(N)-v_2(H),0
   \right\},
   \quad
   C_n=\frac{3n}{2}-v_2(b!)-s_2(n)-1.
   }
$$


   Consequently, on the retained guarded separator domain
   

$$
c\le22,\qquad t-c\le6,
$$


   one obtains, without the former documentary qualification,
   

$$
\boxed{v_2(q_n)=C_n.}
$$


   This does not prove that infinitely many original parameters satisfy those guards.

5. **New exact ternary result.** For every original index,
   

$$
\boxed{
   v_3(q_n)=2v_3(n!)-v_3(b!)
           =\frac{8003b-15}{2}.
   }
$$


   The proof evaluates two complete-source coefficients:
   

$$
\boxed{
   Z_w^TZ_w\equiv6\pmod9,\qquad
   Z_w^T\!\left(\frac{V_w}{b!}\right)\equiv3\pmod9.
   }
$$


   Thus the factorial normalization does **not** disappear at $3$. Its cancellation against the primitive raw numerator is exactly $3^3$, no more.

6. **Consequence for the proposed shallow-binary route.** Combining the exact ternary denominator with the guarded binary law gives
   

$$
\log q_n\ge
   \left[
   \left(\frac32-\frac1{4002}\right)\log2
   +\left(1-\frac1{8004}\right)\log3
   \right]n+O(\log n).
$$


   The coefficient is approximately $2.13802$, exceeding the stated whole-error decay coefficient
   

$$
\beta=\left(2+\frac1{4002}\right)\log(1+\sqrt2)
   \approx1.76297.
$$


   Therefore, **under the retained whole-error theorem**, every infinite original sequence satisfying the shallow-binary guards has
   

$$
|q_n\epsilon_n|\longrightarrow\infty,
$$


   rather than tending to zero.

This is an obstruction to that particular primitive-approximation route, not a proof of rationality or irrationality of $e+\pi$.

The HIGH8 computations are accepted as completed finite corroboration at their stated scope. No accepted computation is proposed for repetition.

---

# 1. Exact finite objects and notation

Write


$$
h=\frac n2,\qquad
R=2^h\binom nh,\qquad
\lambda=\frac{(n!)^2}{2^n},
$$


and


$$
\omega_j=(n+2)_{\underline j},\qquad
W_j=\binom{n+2}{j},\qquad
\Omega=\operatorname{diag}(\omega_j^2)_{0\le j\le b}.
$$



The contact coordinates remain


$$
0\le i,r<b,
$$


and reconstructed coordinates remain


$$
\boxed{0\le j\le b.}
$$



Let


$$
\mathcal R=\operatorname{diag}(W_j)C,
\qquad
(Cz)_j=jz_{j-1}-z_j,
$$


with $z_{-1}=z_b=0$.

I use


$$
x=\frac{X_{\rm raw}}2,\qquad
y=\frac{Y_{\rm raw}}4,
\qquad
N=x^Tx,\qquad H=x^Ty.
$$


These are exactly the quantities called $X,Y,N,H$ in the recovered PRE-resumption source.

The final columns are the prescribed $u,v$, not independently primitive versions of their rows:


$$
N_B=d_B[u,v],
$$




$$
A_B=N_{B,1}^T\Omega N_{B,1},\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
\boxed{
g_B=\gcd(A_B,|H_B|),\quad
q_n=A_B/g_B,\quad p_n=H_B/g_B.
}
$$



All gcds in this report, except explicitly prime-local statements, are ordinary all-prime integer gcds.

---

# 2. Verifying the normalized first force

The recovered exact first force is


$$
f_i^0=\frac{(n+i)!}{n!}J_i,
\qquad
J_i=[t^n](1+2t+2t^2)^n(1+t)^i.
$$



Put


$$
Q(t)=1+2t+2t^2
$$


and define exact central quantities


$$
B_\ell=
\frac{(n+\ell)!}{n!\,R}[t^{n-\ell}]Q(t)^n.
\tag{2.1}
$$



Then expansion of $(1+t)^i$ gives the exact identity


$$
\begin{aligned}
\frac{f_i^0}{R}
&=\frac{(n+i)!}{n!\,R}
  \sum_{\ell=0}^i\binom i\ell[t^{n-\ell}]Q(t)^n\\
&=\sum_{\ell=0}^i
  \binom i\ell
  \frac{(n+i)!}{(n+\ell)!}\,B_\ell.
\end{aligned}
\tag{2.2}
$$



This is precisely the first-force construction in the supplied head source:


$$
f_i=\sum_{\ell=0}^i\binom i\ell
       \left(\prod_{t=\ell+1}^i(n+t)\right)B_\ell.
$$



It remains to verify that its `central` formula computes (2.1), rather than an differently normalized central coefficient.

## 2.1 Exact central formula

Write


$$
\ell=2j+\delta,\qquad \delta\in\{0,1\}.
$$


In the multinomial expansion of $Q^{2h}$, choose


$$
h-j-\delta-s
$$


quadratic terms and $2s+\delta$ linear terms. This gives


$$
[t^{2h-\ell}]Q(t)^{2h}
=
(2h)!\,2^{h-j}
\sum_{s=0}^{h-j-\delta}
\frac{2^s}
{(h-j-\delta-s)!\,(h+j-s)!\,(2s+\delta)!}.
\tag{2.3}
$$



Since


$$
R=2^h\frac{(2h)!}{(h!)^2},
$$


equation (2.1) becomes


$$
B_{2j+\delta}
=
P_{j,\delta}
\sum_{s=0}^{h-j-\delta}
\frac{2^s(s!)^2}{(2s+\delta)!}
\binom{h-j-\delta}{s}\binom{h+j}{s},
\tag{2.4}
$$


where


$$
P_{j,0}
=
\left(\prod_{t=1}^j(2h+2t-1)\right)
h_{\underline j},
$$




$$
P_{j,1}
=
\left(\prod_{t=0}^j(2h+2t+1)\right)
h_{\underline{j+1}}.
\tag{2.5}
$$



These are exactly the two prefactors and summands in the supplied source.

Thus:

### Proposition 2.1 — Exact first-head identification


$$
\boxed{f=f^0/R.}
$$



The precision-$32$ source is a modular truncation of this exact identity. Its accepted central and first-force tail theorems justify that truncation at the stated precision; they do not make the truncated head an exact characteristic-zero force.

No head computation is needed to establish the normalization.

---

# 3. The finite contact-coordinate bridge

Let


$$
U_n=(1+S)^n
$$


on the original $b$-dimensional contact range, where $S$ is the upper shift. Its inverse is the finite triangular matrix $U_{-n}$.

The contact excerpt gives


$$
\mathcal T=\mathcal R U_{-n}.
$$


The current contact-coordinate matrix is


$$
\boxed{A=\widetilde N U_n.}
\tag{3.1}
$$


Consequently,


$$
A^{-1}=U_{-n}\widetilde N^{-1}.
$$



There is a direct coefficient check of (3.1). Put


$$
\lambda_s=s![z^s]\phi(z)^n.
$$


Then


$$
\widetilde N_{ij}
=
\sum_s\lambda_s\binom{n+i}{s}
                    \binom{n+i-s}{j},
$$


and finite Vandermonde convolution gives


$$
\boxed{
A_{ij}=
\sum_s\lambda_s\binom{n+i}{s}
                 \binom{2n+i-s}{j},
\quad 0\le i,j<b.
}
\tag{3.2}
$$


No term with intermediate column outside $0,\ldots,b-1$ enters this product: for an output column $j<b$, the upper-triangular convolution uses only intermediate indices at most $j$.

Using Proposition 2.1,


$$
X_{\rm raw}
=\mathcal R A^{-1}f
=\frac1R\mathcal R U_{-n}\widetilde N^{-1}f^0
=\boxed{\frac{Z_w}{R}}.
\tag{3.3}
$$



For the second column, the retained exact finite-boundary identity is


$$
\mathcal R(j!)_{0\le j<b}=-e_0+b!W_be_b.
$$


Therefore its factorial subtraction and terminal return give


$$
b!Y_{\rm raw}
=\mathcal R A^{-1}(h^e+h^F)+e_0.
$$


The right side is exactly $V_w$, so


$$
\boxed{Y_{\rm raw}=V_w/b!.}
\tag{3.4}
$$



In particular,


$$
x=\frac{Z_w}{2R},\qquad
y=\frac{V_w}{4b!}.
$$


This closes both column identifications.

---

# 4. The actual final rows, least clearer, and Gram map

The recovered coefficient equations are


$$
\operatorname{diag}(\omega_j)u=\lambda Z_w,
\qquad
\operatorname{diag}(\omega_j)v=V_w.
$$


Equivalently,


$$
u_j=\frac{2\lambda R}{\omega_j}x_j,\qquad
v_j=\frac{4b!}{\omega_j}y_j.
\tag{4.1}
$$



The falling metric compensates these displayed factors exactly:


$$
u^T\Omega u=4\lambda^2R^2N,
$$




$$
u^T\Omega v=8\lambda Rb!H.
\tag{4.2}
$$


Hence


$$
\boxed{
A_B=d_B^2\,4\lambda^2R^2N,\qquad
H_B=d_B^2\,8\lambda Rb!H.
}
\tag{4.3}
$$



There is no affine term.

## 4.1 The actual least clearer, without a row rescaling

The definition is


$$
\boxed{
d_B=\operatorname{lcm}
\{\operatorname{den}(u_j),\operatorname{den}(v_j):0\le j\le b\}.
}
\tag{4.4}
$$


Primewise, this means


$$
\begin{aligned}
v_\ell(d_B)=\max\bigg\{0,\;&
\max_j\bigl(v_\ell(\omega_j)-v_\ell(2\lambda R)-v_\ell(x_j)\bigr),\\
&
\max_j\bigl(v_\ell(\omega_j)-v_\ell(4b!)-v_\ell(y_j)\bigr)
\bigg\}.
\end{aligned}
\tag{4.5}
$$



An entirely integral formula for this same clearer is also available.

First, the full source forces are integers. For the logarithmic force, observe


$$
F'(z)=\frac2{\phi(z)}.
$$


If $c_m=[z^m]\phi(z)^{-1}$, then


$$
c_m=c_{m-1}-\frac12c_{m-2},
\qquad
2^{\lfloor m/2\rfloor}c_m\in\mathbb Z.
$$


Thus


$$
F^{(r)}(0)=2(r-1)!c_{r-1}\in\mathbb Z,
$$


and


$$
m!\mathcal F_m
=\sum_{r=1}^m\frac{m!}{r!}F^{(r)}(0)\in\mathbb Z.
$$


Also $\lambda_s\in\mathbb Z$, so $\widetilde N,f^0,h^e,h^F$ are integral.

Set


$$
M=(b-1)!,\qquad
E=M K D_b^{-1}.
$$


This $E$ is integral, including its terminal row. Indeed,


$$
E_{jr}
=\frac{M}{j!}
\left[j\binom{-n}{r-j+1}-\binom{-n}{r-j}\right].
$$


For $j<b$, integrality follows from $j!\mid M$; at $j=b$, only $r=b-1$ survives and the entry is $1$.

Let


$$
\Delta=\det\widetilde N\ne0,\qquad
P=\operatorname{adj}(\widetilde N)f^0,\qquad
Q=\operatorname{adj}(\widetilde N)(h^e+h^F),
$$


and define


$$
L=M|\Delta|,
$$




$$
t_1=\operatorname{sgn}(\Delta)\lambda EP,
\qquad
t_2=\operatorname{sgn}(\Delta)(M\Delta e_0+EQ).
$$


On the present family $\lambda$ is an integer, so $t_1,t_2$ are integer vectors and


$$
u=t_1/L,\qquad v=t_2/L.
$$



Therefore the actual least clearer is exactly


$$
\boxed{
C=\gcd\bigl(L,\{t_{1,j},t_{2,j}:0\le j\le b\}\bigr),
\qquad
d_B=L/C.
}
\tag{4.6}
$$


The prescribed final columns are


$$
N_{B,1}=t_1/C,\qquad N_{B,2}=t_2/C.
$$



Their row contents are consequently


$$
\gcd(|t_{1,j}|,|t_{2,j}|)/C.
$$


These contents are retained. They are **not** separately divided out.

Formula (4.6) is an exact characterization, not a claim that the enormous determinant or clearer has been numerically evaluated.

---

# 5. Every factorial factor in the primitive denominator

Define


$$
\mathscr D_n=\frac{\lambda R}{2b!}
=\frac{(n!)^2\binom nh}{2^{h+1}b!}.
\tag{5.1}
$$



For every odd prime $\ell$,


$$
v_\ell(\mathscr D_n)
=2v_\ell(n!)+v_\ell\binom nh-v_\ell(b!)\ge0.
$$


At $2$,


$$
v_2(\mathscr D_n)
=\frac{3n}{2}-v_2(b!)-s_2(n)-1=C_n>0.
$$


Thus $\mathscr D_n$ is an integer and


$$
\xi_n=\frac{2b!}{\lambda R}=\frac1{\mathscr D_n}.
$$



From (4.3),


$$
\boxed{
\frac{p_n}{q_n}=\frac{H}{\mathscr D_nN}.
}
\tag{5.2}
$$



If $H/N=p_{\rm r}/q_{\rm r}$ in lowest terms, then


$$
\gcd(\mathscr D_nq_{\rm r},|p_{\rm r}|)
=\gcd(\mathscr D_n,|p_{\rm r}|),
$$


so


$$
\boxed{
q_n=q_{\rm r}\,
\frac{\mathscr D_n}{\gcd(\mathscr D_n,|p_{\rm r}|)}.
}
\tag{5.3}
$$



The factor


$$
\boxed{
\mathscr D_n^{\rm def}
=\frac{\mathscr D_n}{\gcd(\mathscr D_n,|p_{\rm r}|)}
}
\tag{5.4}
$$


is a canonical factorial deficit. It is not a chosen estimate or a selected-prime normalization.

For every prime,


$$
\boxed{
v_\ell(q_n)
=
\max\{v_\ell(\mathscr D_n)+v_\ell(N)-v_\ell(H),0\}.
}
\tag{5.5}
$$



The final gcd itself remains


$$
\begin{aligned}
v_\ell(g_B)=2v_\ell(d_B)+\min\{&
v_\ell(4\lambda^2R^2)+v_\ell(N),\\
&
v_\ell(8\lambda Rb!)+v_\ell(H)\}.
\end{aligned}
\tag{5.6}
$$


This preserves the actual $d_B$, $g_B$, and primitive multiplier $d_B^2/g_B$.

## 5.1 Binary conclusion

Equation (5.5) proves the recovered binary interface:


$$
v_2(q_n)=\max\{C_n+v_2(N)-v_2(H),0\}.
$$



The retained separator theorem gives


$$
v_2(N)=v_2(H)=31+t
$$


when $c\le22$ and $t-c\le6$. Thus


$$
\boxed{v_2(q_n)=C_n}
$$


on that domain, now without the former missing-normalization premise.

The mathematical guards and original-domain occurrence issue remain unchanged.

---

# 6. Transporting the complete correction ideal through the scalar

Retain the exact cleared raw pair from turn 8:


$$
\mathcal A=e_*^2N=Sa+\Delta_A,\qquad
\mathcal H=e_*^2H=Sh+\Delta_H.
$$


Here $\Delta_A,\Delta_H$ are the complete finite corrections, including both corrected columns, unsupported rows, finite returns, and the terminal coordinate.

The integer pair governing the final ratio is now


$$
\boxed{
(\mathscr D_n\mathcal A,\mathcal H)
=
(S\mathscr D_na+\mathscr D_n\Delta_A,\;
 Sh+\Delta_H).
}
\tag{6.1}
$$



Set


$$
g_{\rm mod}=\gcd(\mathscr D_na,|h|),
$$




$$
a_{\rm mod}=\mathscr D_na/g_{\rm mod},
\qquad
h_{\rm mod}=h/g_{\rm mod},
$$


and choose


$$
r_{\rm mod}a_{\rm mod}+s_{\rm mod}h_{\rm mod}=1.
$$


The exact transported correction ideal is


$$
\boxed{
\begin{aligned}
(\mathscr D_n\mathcal A,\mathcal H)
=\bigl(&Sg_{\rm mod}
+r_{\rm mod}\mathscr D_n\Delta_A+s_{\rm mod}\Delta_H,\\
&a_{\rm mod}\Delta_H-h_{\rm mod}\mathscr D_n\Delta_A
\bigr).
\end{aligned}
}
\tag{6.2}
$$



This is the same unimodular reduction as before, now applied to the **actual scalar-normalized pair**.

Its exact high-norm saturation divisor is


$$
\boxed{
J_{\rm final}
=\gcd(S,\mathscr D_n\Delta_A,\Delta_H).
}
\tag{6.3}
$$


In particular,


$$
\gcd\!\left(S,\gcd(\mathscr D_n\mathcal A,\mathcal H)\right)
=J_{\rm final}.
$$



The actual final pair is related to (6.1) by the explicitly known common rational multiplier


$$
\rho=\frac{d_B^2(4b!)^2\mathscr D_n}{e_*^2}:
$$




$$
(A_B,H_B)=\rho(\mathscr D_n\mathcal A,\mathcal H).
\tag{6.4}
$$


Equation (6.4) is an equality of pairs and hence of fractional ideals; both final coordinates are integers. It does not introduce a new row operation.

An upper bound on the transverse generator in (6.2) is still an **upper gcd bound**, not the lower gcd bound needed to make $q_n$ small. The relevant new question is whether the complete primitive raw numerator contains the factorial divisor in (5.4).

The next section evaluates that question at $3$.

---

# 7. New complete-source theorem at the prime $3$

The proof actually works for


$$
b=3^k,\qquad n=4002b,\qquad k\ge2.
$$


The original family has $k=36+64u$, so it is entirely included.

Define


$$
D_w=Z_w^TZ_w,\qquad
C_*=
Z_w^T\left(\frac{V_w}{b!}\right).
$$



### Theorem 7.1 — Exact ternary norm and mixed depths
For every such $b$,


$$
\boxed{
D_w\equiv6\pmod9,\qquad C_*\equiv3\pmod9.
}
\tag{7.1}
$$


In particular,


$$
\boxed{v_3(D_w)=v_3(C_*)=1.}
\tag{7.2}
$$



The proof below uses the complete forces and original finite boundary.

## 7.1 Uniform divisibility of the complete operator coefficients

For $s>0$,


$$
\boxed{n\mid \lambda_s.}
\tag{7.3}
$$



To see this, write the coefficient using $a$ linear terms and $c$ quadratic terms, with $a+2c=s$:


$$
\lambda_s
=
\sum_{a+2c=s}
(-1)^a(n)_{\underline{a+c}}\,
\frac{s!}{a!\,c!\,2^c}.
$$


The last quotient counts partitions into $a$ singletons and $c$ unordered pairs, hence is an integer. Every nonconstant term contains $n$.

Since $v_3(n)=k+1$,


$$
\lambda_s\equiv0\pmod{3^{k+1}}\qquad(s>0).
$$



Consequently,


$$
\widetilde N_{ij}\equiv\binom{n+i}{j},
\qquad
A_{ij}\equiv\binom{2n+i}{j}
\pmod{3^{k+1}}.
\tag{7.4}
$$



For $j<b=3^k$, integer-valued binomial continuity gives


$$
\binom{2n+i}{j}\equiv\binom ij\pmod9,
$$


and similarly with $n+i$. Thus


$$
\boxed{
A\equiv\widetilde N\equiv P\pmod9,\qquad
P_{ij}=\binom ij.
}
\tag{7.5}
$$


In particular, both finite matrices have $3$-adic unit determinant, and their inverses are integral over $\mathbb Z_3$.

Also,


$$
U_{-n}\equiv I\pmod9.
$$



## 7.2 Only three interior weights survive modulo $9$

For $j<b$, the same continuity estimate yields


$$
W_j=\binom{n+2}{j}\equiv\binom2j\pmod9.
$$


Therefore


$$
W_0\equiv1,\qquad W_1\equiv2,\qquad W_2\equiv1\pmod9,
$$


and


$$
\boxed{W_j\equiv0\pmod9\quad(3\le j<b).}
\tag{7.6}
$$



The reconstructed endpoint is not omitted. For an integral contact vector $\theta$, its first-column endpoint is


$$
W_b\,b\theta_{b-1},
$$


which is divisible by $9$, since $k\ge2$.

## 7.3 The complete first force at the first three contacts

Let


$$
J=J_0=[t^n]Q(t)^n.
$$


If $c_r=[t^r]Q(t)^n$, differentiation gives


$$
r c_r=n[t^{r-1}]Q'(t)Q(t)^{n-1}.
$$


For $r=n-1,n-2$, the integer $r$ is a $3$-adic unit. Hence


$$
c_{n-1}\equiv c_{n-2}\equiv0\pmod9.
$$


Thus


$$
J_0\equiv J_1\equiv J_2\equiv J\pmod9,
$$


and


$$
(f_0^0,f_1^0,f_2^0)\equiv(J,J,2J)\pmod9.
\tag{7.7}
$$



Using $A^{-1}\equiv P^{-1}\pmod9$, its first three contact coordinates are


$$
(J,0,J)\pmod9.
$$


Reconstruction gives


$$
\boxed{
(Z_{w,0},Z_{w,1},Z_{w,2})
\equiv(-J,2J,-J)\pmod9.
}
\tag{7.8}
$$


Every other coordinate is divisible by $9$, including the endpoint.

It follows that


$$
D_w\equiv6J^2\pmod9.
\tag{7.9}
$$



To evaluate $J\bmod3$, write


$$
J=\operatorname{CT}(t^{-1}+2+2t)^n.
$$


The constant term modulo $3$ factors over the ternary digits of $n$. The digit factors are


$$
1,\quad2,\quad8
$$


for digits $0,1,2$, respectively. A direct reason is that at each digit the Laurent exponent lies between $-2$ and $2$, so a constant term cannot be formed by carrying a nonzero exponent through a multiple of $3$.

Now


$$
4002=(12111020)_3,
$$


which has six nonzero digits. Multiplication by $3^k$ only appends zeros. Hence


$$
\boxed{J\equiv(-1)^6=1\pmod3.}
\tag{7.10}
$$


Equation (7.9) proves


$$
\boxed{D_w\equiv6\pmod9.}
$$



## 7.4 The complete exponential residual is an exact factorial tail

Extend only the **formula for a row polynomial**, not the finite inverse:


$$
A^\infty_{ij}
=\sum_s\lambda_s\binom{n+i}{s}\binom{2n+i-s}{j},
\qquad j\ge0.
$$


For $j<b$, this is exactly $A_{ij}$. Since


$$
\mathcal D_m=\sum_{j=0}^m\binom mj j!,
$$


the complete exponential force satisfies


$$
h_i^e=\sum_{j=0}^{2n+i}A^\infty_{ij}j!.
$$



Thus its residual after the actual finite subtraction is exactly


$$
\boxed{
r_i^e
=\frac{h_i^e-(A(j!))_i}{b!}
=\sum_{j=b}^{2n+i}A^\infty_{ij}\frac{j!}{b!}\in\mathbb Z.
}
\tag{7.11}
$$



This identity preserves the complete source and all terms beyond the finite contact boundary.

Using (7.3),


$$
r_i^e
\equiv
\sum_{j=b}^{2n+i}\binom{2n+i}{j}\frac{j!}{b!}
\pmod9.
$$


The sum has the exact closed form


$$
\boxed{
r_i^e\equiv
\binom{2n+i}{b}\,\mathcal D_{2n+i-b}\pmod9.
}
\tag{7.12}
$$



## 7.5 Full logarithmic-force protection

From $F'=2/\phi$, whose coefficients have only powers of $2$ in their denominators,


$$
v_3(\mathcal F_m)\ge-\lfloor\log_3m\rfloor.
$$


In every term of $h_i^F$,


$$
m=2n+i-s\ge n,
$$


and the factor $\lambda_s\binom{n+i}{s}$ is integral. Therefore


$$
\boxed{
v_3(h_i^F/b!)
\ge v_3(n!)-v_3(b!)
-\lfloor\log_3(2n+b-1)\rfloor.
}
\tag{7.13}
$$



Here


$$
v_3(n!)=2001b-4,\qquad
v_3(b!)=\frac{b-1}{2},
$$


and


$$
\lfloor\log_3(2n+b-1)\rfloor=k+8.
$$


The lower bound is far greater than $2$ for $k\ge2$. Hence


$$
\boxed{h^F/b!\equiv0\pmod9.}
\tag{7.14}
$$



This is a proved absolute congruence for the **whole logarithmic force**. It is not a deletion from the real approximation error.

## 7.6 Evaluating the residual coefficient

For $i=0,1,2$,


$$
\binom{2n+i}{b}\equiv8004\equiv3\pmod9.
\tag{7.15}
$$



For completeness, the scaling congruence used here follows from


$$
(3r+1)(3r+2)\equiv2\pmod9,
$$


which gives


$$
\binom{3A}{3B}\equiv\binom AB\pmod9.
$$


Iterating with $b=3^k$ yields


$$
\binom{8004b}{b}\equiv8004\pmod9.
$$


For $i=1,2$, the extra factorial ratios are units congruent to $1\pmod9$.

Also


$$
\mathcal D_{2n+i-b}\equiv\mathcal D_i\pmod3,
$$


and


$$
(\mathcal D_0,\mathcal D_1,\mathcal D_2)\equiv(1,2,2)\pmod3.
$$


Therefore the complete residual


$$
r=\frac{h^e+h^F-A(j!)}{b!}
$$


has


$$
\boxed{(r_0,r_1,r_2)\equiv(3,6,6)\pmod9.}
\tag{7.16}
$$



After the actual finite inverse, its first three contact coordinates are


$$
(3,3,6)\pmod9.
$$


Consequently,


$$
\boxed{
\left(\frac{V_{w,0}}{b!},
      \frac{V_{w,1}}{b!},
      \frac{V_{w,2}}{b!}\right)
\equiv(-3,0,0)\pmod9.
}
\tag{7.17}
$$



The vector $V_w/b!$ is $3$-integral by (7.11)–(7.14) and the integral finite inverse.

The remaining interior weighted coordinates are divisible by $9$. The terminal coordinate is retained, but its product with $Z_{w,b}$ vanishes modulo $9$, because $Z_{w,b}$ contains the factor $b$.

Finally,


$$
C_*\equiv(-J)(-3)=3J\equiv3\pmod9.
$$


This completes the proof of Theorem 7.1. ∎

---

# 8. The actual ternary denominator and factorial deficit

From


$$
u^T\Omega u=\lambda^2D_w,\qquad
u^T\Omega v=\lambda b!C_*,
$$


Theorem 7.1 gives


$$
\begin{aligned}
v_3(A_B)&=2v_3(d_B)+2v_3(\lambda)+1,\\
v_3(H_B)&=2v_3(d_B)+v_3(\lambda)+v_3(b!)+1.
\end{aligned}
$$


Since $v_3(\lambda)=2v_3(n!)>v_3(b!)$,


$$
\boxed{
v_3(g_B)
=2v_3(d_B)+2v_3(n!)+v_3(b!)+1,
}
\tag{8.1}
$$


and


$$
\boxed{
v_3(q_n)=2v_3(n!)-v_3(b!)
=\frac{8003b-15}{2}.
}
\tag{8.2}
$$



The primitive multiplier is also preserved:


$$
\boxed{
v_3(d_B^2/g_B)
=-2v_3(n!)-v_3(b!)-1.
}
\tag{8.3}
$$



## 8.1 What cancels in the normalized raw pair

The ternary digit sums are


$$
s_3(4002)=8,\qquad s_3(2001)=7.
$$


Hence


$$
v_3(R)=v_3\binom n{n/2}=3.
$$



Since


$$
N=\frac{D_w}{4R^2},\qquad
H=\frac{C_*}{8R},
$$


we obtain


$$
\boxed{v_3(N)=-5,\qquad v_3(H)=-2.}
\tag{8.4}
$$


Thus the primitive raw numerator has exact depth


$$
v_3(p_{\rm r})=3,
\qquad v_3(q_{\rm r})=0.
$$



Meanwhile,


$$
v_3(\mathscr D_n)
=2v_3(n!)-v_3(b!)+3.
$$


Therefore


$$
\boxed{
v_3\gcd(\mathscr D_n,|p_{\rm r}|)=3.
}
\tag{8.5}
$$



This is the evaluated target coefficient that was missing from a generic Bezout framework: the complete raw numerator cancels only three powers of $3$ from the factorial normalization.

No binary congruence is being used to create this odd divisibility. It is proved directly from the complete contact and force equations.

---

# 9. Consequences for the whole same-index error

Retain the source’s fixed-ratio whole-error statement at its stated scope:


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
$$




$$
\log|\epsilon_n|=-\beta n+o(n),
\qquad
\beta=\left(2+\frac1{4002}\right)\log(1+\sqrt2),
$$


with eventual nonvanishing and the stated eventual sign.

The exact evaluated identity remains


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n.
}
\tag{9.1}
$$



## 9.1 The shallow-binary route has the wrong denominator scale

On the guarded separator domain,


$$
v_2(q_n)=C_n
=\left(\frac32-\frac1{4002}\right)n+O(\log n).
$$


The new theorem gives, on every original index,


$$
v_3(q_n)=\left(1-\frac1{8004}\right)n-\frac{15}{2}.
$$


Thus


$$
\log q_n\ge\kappa n+O(\log n),
$$


where


$$
\kappa=
\left(\frac32-\frac1{4002}\right)\log2
+\left(1-\frac1{8004}\right)\log3.
$$


Numerically,


$$
\kappa-\beta\approx0.37506>0.
$$



Consequently, along any infinite original sequence satisfying those binary guards,


$$
\boxed{
\log|q_n\epsilon_n|
\ge(\kappa-\beta)n+o(n)\longrightarrow+\infty.
}
\tag{9.2}
$$



This deduction uses the retained whole-error theorem; it is not a new proof of that analytic theorem. The denominator result underlying it is proved above without an error hypothesis.

## 9.2 A sharper necessary binary target

Put


$$
\delta_2=v_2(H)-v_2(N).
$$


If the present primitive approximants were to satisfy


$$
|q_n\epsilon_n|\to0
$$


on an infinite original sequence, then the $2$- and $3$-parts alone force


$$
\boxed{
\delta_2\ge
\eta n+o(n),
}
\tag{9.3}
$$


where


$$
\eta=
\frac{
\left(\frac32-\frac1{4002}\right)\log2
+\left(1-\frac1{8004}\right)\log3-\beta
}{\log2}
\approx0.541.
$$



Thus equal binary depths, or a bounded relative binary gap, cannot suffice for this family of primitive centers under the stated whole-error asymptotic. A successful use of these same centers would require an exceptionally large positive mixed-to-norm binary valuation gap, before paying any other odd primes.

This does not prove that such a gap is impossible. It replaces the previous small-depth objective by a necessary scale-compatible one.

---

# 10. Arithmetic receipts and a genuinely new bounded check

## 10.1 Completed HIGH8 status

I accept the supplied receipt as finite corroboration of:

- all $64$ complete auxiliary sums for $1\le m\le64$;
- the $32$ full-word depth-one criteria;
- the listed $g=1,2,5,32$, $h=3,11$ checks.

These results agree with the proved counter and its specified terminal condition. They do not evaluate an original high word, prove infinitely many original depth-one occurrences, or evaluate the final all-prime pair.

No rerun is proposed.

## 10.2 A new complete-source ternary check

Theorem 7.1 is a symbolic proof; no bounded computation is required for its validity. A useful independent implementation check would test its **complete-source residual**, rather than another high-block observable.

### Inputs

Use the auxiliary, non-original value


$$
b=9,\qquad n=36018.
$$


The contact matrix has exactly $9$ rows and columns, and reconstruction has exactly $10$ rows.

Compute the full source formulas modulo


$$
3^{v_3(9!)+2}=3^6=729.
$$



Required complete inputs are:

- every needed $\lambda_s=s![z^s]\phi(z)^n$;
- the full $9\times9$ $\widetilde N$ and $A=\widetilde N U_n$;
- $f^0$;
- both complete forces $h^e,h^F$;
- the finite subtraction $A(j!)_{j=0}^8$;
- the actual terminal addition.

No short binary numerator arrays enter this check.

Division-safe recurrences include


$$
\lambda_0=1,\qquad \lambda_1=-n,
$$




$$
\lambda_{s+1}
=(s-n)\lambda_s
+\frac{s(2n-s+1)}2\lambda_{s-1},
$$


and, with $g_r=F^{(r)}(0)$,


$$
g_1=g_2=2,\qquad
g_r=(r-1)g_{r-1}
-\frac{(r-1)(r-2)}2g_{r-2}.
$$


Then


$$
\mathcal D_m=m\mathcal D_{m-1}+1,
$$




$$
m!\mathcal F_m
=m\bigl((m-1)!\mathcal F_{m-1}\bigr)+g_m.
$$


Only division by $2$, a ternary unit, occurs in these recurrences.

### Expected verifiable outputs

After dividing the complete residual by $9!$ with its exact $3^4$ factor paid:



$$
A\equiv P\pmod9,
$$




$$
h^F/9!\equiv0\pmod9,
$$




$$
(r_0,r_1,r_2)\equiv(3,6,6)\pmod9,
$$




$$
V_w/9!\equiv(6,0,0,0,0,0,0,0,0,6)\pmod9,
$$


and the whole reconstructed contractions satisfy


$$
\boxed{
Z_w^TZ_w\equiv6\pmod9,\qquad
Z_w^T(V_w/9!)\equiv3\pmod9.
}
$$



This is a new, feasible complete-source check. It is specified but not executed here. Its finite output would corroborate only this auxiliary input and implementation; the original-family theorem rests on §7.

---

# 11. Proof-status ledger

| Statement | Status |
|---|---|
| Exact central normalization and $f=f^0/R$ | **Proved from the supplied formulas** |
| $X_{\rm raw}=Z_w/R$ | **Exact finite-coordinate identity** |
| $Y_{\rm raw}=V_w/b!$, including terminal return | **Exact finite-coordinate identity** |
| Prescribed $u,v,\Omega$ and absence of extra row normalization | **Recovered documentary definitions, explicitly used** |
| Actual least clearer formula | **Exact all-prime characterization; not numerically evaluated** |
| Final Gram map and final primewise denominator law | **Proved** |
| $\xi_n=1/\mathscr D_n$, with $\mathscr D_n\in\mathbb Z$ | **Proved** |
| Scalar-transported complete correction ideal and saturation divisor | **Proved** |
| Guarded final binary law $v_2(q_n)=C_n$ | **Unconditional on the retained guarded domain** |
| HIGH8 auxiliary tests | **Completed finite corroboration, accepted at stated scope** |
| Complete-source ternary contractions $6,3\bmod9$ | **Proved for $b=3^k,\ k\ge2$** |
| $v_3(q_n)=(8003b-15)/2$ | **Proved on every original index** |
| Exact cancellation $v_3\gcd(\mathscr D_n,p_{\rm r})=3$ | **Proved** |
| Failure of the shallow-binary sequence to make $q_n\epsilon_n\to0$ | **Deduction under the retained whole-error theorem** |
| Existence or impossibility of the necessary large binary gap | Open |
| Remaining odd-prime primitive denominator | Open |
| New $b=9$ complete-source check | Unevaluated specification |
| Irrationality or rationality of $e+\pi$ | Unresolved |

---

# Conclusion

The recovered source resolves the normalization issue completely:


$$
\boxed{
\frac{p_n}{q_n}
=\frac{2b!}{\lambda R}\frac HN
=\frac{H}{\mathscr D_nN},
\qquad
\mathscr D_n\in\mathbb Z_{>0}.
}
$$


The actual least clearer, prescribed rows, falling metric, final all-prime gcd, and primitive multiplier are all retained.

The new mathematical result is the complete-source ternary identity


$$
\boxed{
Z_w^TZ_w\equiv6\pmod9,\qquad
Z_w^T(V_w/b!)\equiv3\pmod9,
}
$$


which proves


$$
\boxed{
v_3(q_n)=\frac{8003b-15}{2}
}
$$


for every original index.

This is a canonical odd-factorial obstruction, not merely a failure to find a common factor. At $3$, the complete normalized raw numerator supplies exactly three powers toward cancellation of the factorial normalization; the remaining exponentially large ternary denominator survives in the actual primitive pair.

Accordingly, the prior shallow-binary denominator law, although now rigorously bridged to the final pair, does not support the desired irrationality argument. Under the stated whole-error theorem it has the opposite scale: the primitive whole error grows on every infinite sequence within that guarded regime.

The exact remaining bottleneck for these same centers is now sharper:



$$
\boxed{
\text{prove or rule out an original infinite sequence with a binary gap of order }
0.541n,
\text{ then control all remaining primes and the whole same-index error.}
}
$$



No such sequence or exclusion theorem is proved here. No conclusion about the rationality or irrationality of $e+\pi$ follows.
