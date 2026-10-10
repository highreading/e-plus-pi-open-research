> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4, turn 16 — Joint logarithmic protection, a logarithmic first-column content bound, and the remaining relative-norm problem

## Executive conclusions

1. **The coordinator’s joint complete-logarithmic estimate is valid.** It retains every original summand and correctly combines the valuation of $\lambda_s$ with that of $\mathcal L_{2n+i-s}$ before using their complementary indices. In particular,
   

$$
v_2(h_i^F)\ge n+\left\lfloor\frac i2\right\rfloor-3\ell,
   \qquad
   \ell=\left\lfloor\log_2(2n+b-1)\right\rfloor.
$$


   After the actual division by $4b!$,
   

$$
y^F\in 2^{B_{\rm new}}\mathbb Z_2^{b+1},
   \qquad
   B_{\rm new}=n-v_2(b!)-2-3\ell.
$$


   Thus the protected scale is approximately $0.999750125\,n$, not $0.499750125\,n$.

2. **My turn-15 conclusion requiring an additional $0.04134n$ of complete-source cancellation is superseded.** That number resulted from the weaker logarithmic guard. With the new proof, logarithmic omission at gap $k$ is valid when
   

$$
B_{\rm new}\ge a+\nu+k,
$$


   with the actual first-column content $a$ and primitive norm loss $\nu$ retained. A strict inequality is needed to preserve the first nonzero digit at that target depth.

3. **There is a new unconditional content bound for the original binary family.** For
   

$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0,
$$


   write $x=2^a x_0$, with $x_0$ primitive over $\mathbb Z_2$. Then
   

$$
\boxed{
   0\le a\le
   \max_{0\le j<b}v_2\binom{n+2}{j}-1
   \le \lfloor\log_2(n+2)\rfloor-1.
   }
$$


   The proof uses the actual first force, the first two central coefficients, and the finite reconstruction. It does not assume that a reference column has the same content as the corrected column.

   Consequently, **a linearly deep first-column content is no longer an unresolved exception**. The possible exception to logarithmic omission at the denominator-relevant scale is principally the primitive norm loss $\nu$.

4. **I also derive an exact factorial-tail identity for the complete exponential residual.** At a target depth $T=a+\nu+k$, its contribution is determined modulo $2^T$ by a finite, explicitly paid factorial sum ending at
   

$$
j\le b+T+O(\log n),
$$


   rather than by the entire source length $2n+b-1$. This is a justified evaluation identity for the original finite producer—not a change of contact dimension, reconstruction boundary, or force.

5. **A5 turn 10’s integer-affine two-center obstruction passes the audit at its stated scope.** The exact full ternary-cancellation congruence, the actual all-prime gcd, and the whole affine error are correctly retained. The divergence conclusion is uniform as the lower original index tends to infinity. It does not cover arbitrary rational affine coefficients, the original one-center family without further hypotheses, or a decision about $e+\pi$.

6. **The stronger guard and the new content theorem do not yet produce an unconditional denominator dichotomy.** They reduce the exceptional range to a concrete question about the actual primitive norm:
   

$$
\nu\ \text{near or above}\ 
   \left(1-\frac1{4002}-\eta\right)n
   \approx0.45866n,
   \qquad
   \eta\approx0.54109.
$$


   No supplied proof controls $\nu$ on that scale. Even below that range, a relative exponential mixed-contraction estimate is still required.

No computation was executed. No accepted computation is proposed for repetition. The optional $b=9$, twenty-thousand-bit logarithmic diagnostic is unnecessary: its vanishing follows from the new bound.

---

## 1. Scope, retained normalization, and the new receipts

### 1.1 Original binary objects

All new binary results below stay on


$$
b=9^{18+32u}=3^{36+64u},\qquad n=4002b,\qquad u\ge0.
$$


In particular, $b$ is odd and


$$
n=2h,\qquad h=2001b
$$


is odd.

The contact matrix has exactly $b$ rows and columns. The reconstruction has exactly the coordinates


$$
0\le j\le b.
$$


Put


$$
R=2^{n/2}\binom n{n/2},\qquad
\lambda=\frac{(n!)^2}{2^n},\qquad
W_j=\binom{n+2}{j}.
$$


The actual reconstruction is


$$
(\mathcal R z)_j=W_j(jz_{j-1}-z_j),
\qquad z_{-1}=z_b=0.
$$



The complete columns remain


$$
Z_w=\mathcal R A^{-1}f^0,
\qquad
V_w=\mathcal R A^{-1}(h^e+h^F)+e_0,
$$


and


$$
x=\frac{Z_w}{2R},\qquad
y=\frac{V_w}{4b!},\qquad
N=x^Tx,\qquad H=x^Ty.
$$



The prescribed weighted columns, least simultaneous clearer, and all-prime reduction remain


$$
A_B=d_B^2\,4\lambda^2R^2N,\qquad
H_B=d_B^2\,8\lambda Rb!H,
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=\frac{A_B}{g_B},\qquad p_n=\frac{H_B}{g_B}.
$$


No independent row-content division is introduced.

In particular,


$$
\frac{p_n}{q_n}=\frac{H}{\mathscr D_nN},
\qquad
\mathscr D_n=\frac{\lambda R}{2b!},
$$


and, for every prime $p$,


$$
v_p(q_n)=
\max\{v_p(\mathscr D_n)+v_p(N)-v_p(H),0\}.
$$



### 1.2 What the new finite receipts establish

The accepted A1 and A2 audits need not be reopened.

- The NEW40 calculation supplies forty auxiliary full-content/sign comparisons at $m=241,\ldots,260$. Its six zero signed residues demonstrate endpoint cancellation beyond full polynomial content in those six cases. They are not six evaluations of eligible original powers.
- The new $29$-adic scalar receipt gives
  

$$
(\alpha_{\rm I},\alpha_{\rm II})=(33,837)\pmod{841},
  \quad
  (\beta_{\rm I},\beta_{\rm II})=(5,24)\pmod{29},
$$


  

$$
\gamma=22,\qquad \Xi=17\pmod{29}.
$$


  The displayed scalar arithmetic is consistent:
  

$$
\frac{33+837}{29}=30,\qquad
  4(22)+13(30)+11(5)+22(24)=1061\equiv17\pmod{29}.
$$


  The $220/242$ branch support, $231$-path support, and paid divisions remain essential. This is not an evaluation of the complete original mixed contraction.
- At $n=3375$, the new alignment calculation gives
  

$$
\gcd(F,Q\widehat h-P\widehat\ell)=128,\qquad I_{\rm ref,large}=1.
$$


  At $n=11025$, the distinct reference/moment-only calculation gives
  

$$
\gcd(F,Q\widehat h-P\widehat\ell)=8,\qquad I_{\rm ref,large}=1.
$$



The recurrence used at $11025$ is consistent with the defining differential equation. If


$$
a_k=k![z^k]\bigl(e^z\phi(z)^n\bigr),
\qquad \phi(z)=1-z+\frac{z^2}{2},
$$


then


$$
\phi A'=(\phi+n\phi')A
$$


gives


$$
a_{k+1}
=(k+1-n)a_k
+\frac{k(2n-k-1)}2a_{k-1}
+\frac{k(k-1)}2a_{k-2},
$$


exactly as used.

Neither alignment receipt proves a universal support theorem. At $11025$, no complete force, contact producer, primitive denominator, or whole error was calculated.

---

# Part I. Independent audit of the joint complete-logarithmic guard

## 2. Symbol coefficients: the valuation payment is legitimate

Let


$$
\lambda_s=s![z^s]\phi(z)^n.
$$


The finite expansion is


$$
[z^s]\phi(z)^n
=
\sum_{r=0}^{\lfloor s/2\rfloor}
(-1)^{s-2r}
\binom n{s-r}\binom{s-r}{r}2^{-r},
$$


where terms outside the polynomial support are zero.

Every binomial factor is integral. Hence


$$
v_2(\lambda_s)
\ge v_2(s!)-\lfloor s/2\rfloor
=\left\lceil\frac s2\right\rceil-s_2(s).
$$


A possibly negative lower bound is harmless: it is a valuation inequality, not a modular inversion. For $s=0$, it gives the exact value $0$.

This argument retains the factorial in $\lambda_s$; that is the factor discarded in the older estimate.

---

## 3. The complete logarithmic convolution

Let


$$
F'(z)=\frac2{\phi(z)},\qquad F(0)=0,\qquad
g_r=F^{(r)}(0).
$$


The identity


$$
\frac1{\phi(z)}
=
\frac{1+z+z^2/2}{1+z^4/4}
$$


is exact, since


$$
(1-z+z^2/2)(1+z+z^2/2)=1+z^4/4.
$$


Therefore


$$
v_2([z^k]\phi(z)^{-1})\ge-\lfloor k/2\rfloor,
$$


including the zero coefficients, and


$$
v_2(g_r)\ge
1+v_2((r-1)!)-\left\lfloor\frac{r-1}{2}\right\rfloor.
$$



The whole exponential convolution is


$$
\mathcal L_m
=m![z^m](e^zF(z))
=\sum_{r=1}^m\frac{m!}{r!}g_r.
$$


For every summand,


$$
\begin{aligned}
v_2\!\left(\frac{m!}{r!}g_r\right)
&\ge
1+v_2(m!)-v_2(r)
-\left\lfloor\frac{r-1}{2}\right\rfloor\\
&\ge
1+v_2(m!)
-\lfloor\log_2m\rfloor
-\left\lfloor\frac{m-1}{2}\right\rfloor.
\end{aligned}
$$


Thus


$$
\boxed{
v_2(\mathcal L_m)
\ge
\left\lfloor\frac m2\right\rfloor+2
-s_2(m)-\lfloor\log_2m\rfloor.
}
$$



No denominator has been treated as a binary unit without payment. This is an estimate on the complete $\mathcal L_m$, not a selected term.

---

## 4. The joint estimate and its transport

For a contact row $0\le i<b$, put


$$
m=2n+i-s.
$$


The complete force is


$$
h_i^F
=
\sum_{s=0}^{n+i}
\lambda_s\binom{n+i}{s}\mathcal L_m.
$$


Here


$$
n\le m\le2n+b-1,\qquad s+m=2n+i.
$$



Combining the two paid estimates, and retaining the integral binomial factor, gives


$$
\begin{aligned}
v_2\!\left(
\lambda_s\binom{n+i}{s}\mathcal L_m
\right)
&\ge
\left\lceil\frac s2\right\rceil
+\left\lfloor\frac m2\right\rfloor
+2-s_2(s)-s_2(m)-\lfloor\log_2m\rfloor\\
&\ge
n+\left\lfloor\frac i2\right\rfloor
+2-s_2(s)-s_2(m)-\lfloor\log_2m\rfloor.
\end{aligned}
$$


With


$$
\ell=\lfloor\log_2(2n+b-1)\rfloor,
$$


we have


$$
s_2(s),s_2(m)\le\ell+1,\qquad
\lfloor\log_2m\rfloor\le\ell.
$$


Consequently,


$$
\boxed{
v_2(h_i^F)\ge
n+\left\lfloor\frac i2\right\rfloor-3\ell.
}
$$



The outer sum is complete. Cancellation within it can only increase this lower bound.

For the retained even producer, $A^{-1}$ and $\mathcal R$ are $2$-integral. Hence


$$
y^F=\frac{\mathcal RA^{-1}h^F}{4b!}
\in2^{B_{\rm new}}\mathbb Z_2^{b+1},
$$


where


$$
\boxed{
B_{\rm new}=n-v_2(b!)-2-3\ell.
}
$$


On $n=4002b$,


$$
B_{\rm new}
=
\left(1-\frac1{4002}\right)n+O(\log n).
$$



**Audit verdict:** the coordinator’s joint proof passes.

The terminal has not been deleted: it belongs to


$$
y^E=
\frac{\mathcal RA^{-1}h^e+e_0}{4b!},
$$


not to $y^F$.

---

## 5. A modest further strengthening from the outer binomial

The same calculation can retain more of the factor
$\binom{n+i}{s}$. This improves the logarithmic loss, though not the linear coefficient.

Put $N_i=n+i$. Since


$$
\lambda_s\binom{N_i}{s}
=
\frac{N_i!}{(N_i-s)!}[z^s]\phi(z)^n,
$$


we have


$$
v_2\!\left(\lambda_s\binom{N_i}{s}\right)
\ge
v_2(N_i!)-v_2((N_i-s)!)-\lfloor s/2\rfloor.
$$


Also


$$
m=n+(N_i-s),
$$


so


$$
v_2(m!)-v_2((N_i-s)!)\ge v_2(n!).
$$


Combining this with the preceding bound for $\mathcal L_m$ gives


$$
\begin{aligned}
v_2\!\left(
\lambda_s\binom{N_i}{s}\mathcal L_m
\right)
\ge{}&
v_2(N_i!)+v_2(n!)+1-\ell\\
&-\lfloor s/2\rfloor-\lfloor(m-1)/2\rfloor.
\end{aligned}
$$


Because $s+m=2n+i$,


$$
\lfloor s/2\rfloor+\lfloor(m-1)/2\rfloor
\le n+\left\lfloor\frac{i-1}{2}\right\rfloor.
$$


Therefore


$$
\boxed{
v_2(h_i^F)
\ge
n+\left\lfloor\frac i2\right\rfloor+2
-s_2(n+i)-s_2(n)-\ell.
}
\tag{5.1}
$$



Using


$$
s_2(n+i)\le s_2(n)+s_2(i),
\qquad
s_2(i)\le\lfloor i/2\rfloor+1,
$$


we obtain the uniform bound


$$
v_2(h_i^F)\ge n+1-2s_2(n)-\ell.
$$


Thus one may use


$$
\boxed{
B_*=
n-v_2(b!)-1-2s_2(n)-\ell
}
\tag{5.2}
$$


in place of $B_{\rm new}$.

Since $s_2(n)\le\ell$, this is at least one digit stronger than $B_{\rm new}$. The important advance remains the coordinator’s joint linear coefficient; (5.2) is a further paid refinement.

For the abandoned auxiliary diagnostic,


$$
b=9,\quad n=36018,\quad s_2(n)=7,\quad \ell=16,
$$


the original new bound gives $B_{\rm new}=35961$, while (5.2) gives $B_*=35980$. Either proves the logarithmic contribution is zero modulo $2^{20000}$. No source evaluation is needed to rediscover that protected zero.

---

# Part II. A new bound for the actual first-column content

## 6. Two central coefficients give a low-valuation contact witness

This section proves a bound on the actual corrected column, not on a homogeneous reference.

Let


$$
n=2h,\qquad h\ \text{odd},
$$


and write


$$
c_k=[t^k](1+2t+2t^2)^{2h}.
$$


Recall


$$
R=2^h\binom{2h}{h}.
$$



### Lemma 6.1

For odd $h$,


$$
\boxed{
\frac{c_{2h}}R\in2\mathbb Z_2,
\qquad
\frac{c_{2h-1}}{hR}\in\mathbb Z_2^\times.
}
\tag{6.1}
$$



#### Proof

Expanding the central coefficient by the number of quadratic terms gives


$$
\frac{c_{2h}}R
=
\sum_{r=0}^{h}
\frac{2^r(h_{\underline r})^2}{(2r)!}.
$$


The $r=0$ term is $1$, and the $r=1$ term is $h^2$. For every $r$,


$$
\frac{2^r(h_{\underline r})^2}{(2r)!}
=
\frac{2^r(r!)^2}{(2r)!}\binom hr^2,
$$


and


$$
v_2\!\left(\frac{2^r(r!)^2}{(2r)!}\right)
=r-s_2(r)=v_2(r!).
$$


All terms with $r\ge2$ are therefore even. Since $h$ is odd,


$$
1+h^2\equiv0\pmod2.
$$


This proves the first assertion.

Similarly,


$$
\frac{c_{2h-1}}{hR}
=
\sum_{d=0}^{h-1}
\frac{2^d(h-1)_{\underline d}h_{\underline d}}{(2d+1)!}.
$$


The $d=0$ term is $1$. The $d=1$ term is


$$
\frac{h(h-1)}3,
$$


which is even. For $d\ge2$,


$$
\frac{2^d(h-1)_{\underline d}h_{\underline d}}{(2d+1)!}
=
\frac{2^d(d!)^2}{(2d+1)!}
\binom{h-1}{d}\binom hd,
$$


with


$$
v_2\!\left(\frac{2^d(d!)^2}{(2d+1)!}\right)
=d-s_2(d)=v_2(d!)\ge1.
$$


Thus every term except the initial $1$ is even. This proves the second assertion. ∎

The actual first-force formula is


$$
f_i^0=\frac{(n+i)!}{n!}
[t^n](1+2t+2t^2)^n(1+t)^i.
$$


Because $b\ge2$, its row $i=1$ exists and satisfies


$$
f_1^0=(n+1)(c_n+c_{n-1}).
$$


Here $n+1$ and $h$ are odd. Lemma 6.1 therefore yields the exact valuation


$$
\boxed{
v_2(f_1^0)=v_2(R).
}
\tag{6.2}
$$



This is a low-valuation witness in the **complete actual first force**.

---

## 7. Transporting that witness through the finite reconstruction

Write


$$
x=2^a x_0,
$$


where $x_0\in\mathbb Z_2^{b+1}$ is primitive. The retained normalization theorem gives $a\ge0$.

Let


$$
\xi=A^{-1}f^0,\qquad Z_w=\mathcal R\xi.
$$


For $0\le j<b$,


$$
\xi_j=j\xi_{j-1}-\frac{Z_{w,j}}{W_j},
$$


and hence, by finite iteration,


$$
\boxed{
\xi_j=-\sum_{k=0}^j\frac{j!}{k!}\frac{Z_{w,k}}{W_k}.
}
\tag{7.1}
$$


No recurrence is continued through $j=b$.

Set


$$
w_*=\max_{0\le k<b}v_2(W_k).
$$


Since


$$
Z_w=2R\,x,
$$


every term in (7.1) has valuation at least


$$
v_2(2R)+a-w_*.
$$


Therefore


$$
v_2(\xi_j)\ge v_2(2R)+a-w_*
$$


for every contact coordinate. As $A$ is integral,


$$
v_2(f_i^0)\ge v_2(2R)+a-w_*
$$


for every contact row.

Applying the exact witness (6.2),


$$
v_2(R)\ge v_2(2R)+a-w_*,
$$


so


$$
a\le w_*-1.
$$



Finally, Kummer’s carry formula gives


$$
v_2\binom{n+2}{k}\le\lfloor\log_2(n+2)\rfloor.
$$


We have proved:

### Theorem 7.1 — Actual first-column content is logarithmic

On every original index,


$$
\boxed{
0\le a
\le
\max_{0\le j<b}v_2\binom{n+2}{j}-1
\le\lfloor\log_2(n+2)\rfloor-1.
}
\tag{7.2}
$$



The physical row $b$ is still included in $x$, its content, and its norm. The proof merely uses the first $b$ reconstruction equations to obtain an upper bound; it does not replace the complete column by those rows.

This closes one previously unresolved part of the precision bill:


$$
\boxed{a=O(\log n)\quad\text{on all original powers}.}
$$



---

# Part III. A relative-source identity at the necessary linear scale

## 8. The same adjoint observes the norm and the complete force

Put


$$
\nu=v_2(x_0^Tx_0),\qquad
w=A^{-T}\mathcal R^Tx_0.
$$


Then $w\in\mathbb Z_2^b$, and


$$
\boxed{
w^Tf^0
=x_0^TZ_w
=2^{a+1}R\,x_0^Tx_0.
}
\tag{8.1}
$$



Thus the actual norm has the exact source-coordinate representation


$$
v_2(w^Tf^0)=a+1+v_2(R)+\nu.
$$


The same $w$ gives


$$
H=\frac{2^a}{4b!}
\left(w^T(h^e+h^F)+x_{0,0}\right).
$$


Consequently,


$$
\boxed{
\frac{p_n}{q_n}
=
\frac{w^T(h^e+h^F)+x_{0,0}}
{\lambda\,w^Tf^0}.
}
\tag{8.2}
$$



Equation (8.2) is an identity for the same rational center already reduced by the prescribed all-prime gcd. It is not a replacement primitive pair and does not authorize discarding the odd denominators in $w$.

---

## 9. Complete exponential forcing as a factorial tail

For $0\le j\le M:=2n+b-1$, define an auxiliary source column


$$
(\mathbf a_j)_i
=
\sum_{s=0}^{n+i}
\lambda_s\binom{n+i}{s}
\binom{2n+i-s}{j},
\qquad 0\le i<b.
$$


The first $b$ of these columns are exactly the columns of $A$. The remaining $\mathbf a_j$ are used only to express the force; they do **not** enlarge the contact matrix.

The recurrence


$$
\mathcal D_m=m\mathcal D_{m-1}+1,\qquad \mathcal D_0=1
$$


gives


$$
\mathcal D_m=\sum_{j=0}^m j!\binom mj.
$$


Interchanging two finite sums therefore proves


$$
\boxed{
h^e=\sum_{j=0}^{M}j!\mathbf a_j.
}
\tag{9.1}
$$


If


$$
t=(j!)_{0\le j<b},
$$


then


$$
\boxed{
h^e-At=\sum_{j=b}^{M}j!\mathbf a_j.
}
\tag{9.2}
$$



Define the integral adjoint observations


$$
\theta_j=w^T\mathbf a_j\in\mathbb Z_2.
$$


For $j<b$, the fact that $\mathbf a_j$ is the actual $j$-th column of $A$ gives


$$
\theta_j=(\mathcal R^Tx_0)_j.
$$


Explicitly,


$$
\theta_j=(j+1)W_{j+1}x_{0,j+1}-W_jx_{0,j}.
$$


Therefore


$$
\sum_{j=0}^{b-1}j!\theta_j
=-x_{0,0}+b!W_bx_{0,b}.
$$


This is exactly the finite terminal identity.

Let


$$
E=x_0^Ty^E.
$$


Combining the preceding formulas yields


$$
\boxed{
4E
=
W_bx_{0,b}
+\sum_{j=b}^{M}\frac{j!}{b!}\theta_j.
}
\tag{9.3}
$$



Every exponential-force term and the physical terminal are present. The division by $4$ is a division of the **whole bracket**. Its divisibility follows from the complete integrality of $E$, not from an unsupported termwise assertion.

---

## 10. A paid linear cutoff

Suppose $E$ is needed modulo $2^T$, with $T\ge0$. Formula (9.3) requires the bracket modulo $2^{T+2}$.

Since every $\theta_j$ is $2$-integral, all indices beyond $J$ may be omitted if


$$
v_2\!\left(\frac{(J+1)!}{b!}\right)\ge T+2.
\tag{10.1}
$$


The factorial valuation is nondecreasing in $J$, so this protects the entire remaining tail.

An explicit sufficient choice is


$$
\boxed{
J=\min\{M,\ b+T+\ell+2\}.
}
\tag{10.2}
$$


Indeed, when $j\le M$,


$$
v_2(j!/b!)
=j-b-s_2(j)+s_2(b),
$$


and $s_2(j)\le\ell+1$.

Consequently,


$$
\boxed{
4E\equiv
W_bx_{0,b}
+\sum_{j=b}^{J}\frac{j!}{b!}\theta_j
\pmod{2^{T+2}}.
}
\tag{10.3}
$$



This is a concrete reduction of the complete exponential source at the needed precision. In a regime with


$$
\nu=o(n),\qquad k=\eta n+o(n),
$$


Theorem 7.1 gives


$$
T=a+\nu+k=\eta n+o(n),
$$


and the sufficient cutoff is


$$
J=
\left(\eta+\frac1{4002}\right)n+o(n)
\approx0.54134n+o(n),
$$


well below the full source endpoint $2n+b-1$.

This does not by itself evaluate the sum. Its contribution is that the exact remaining mixed observable is now a **paid factorial tail with the original terminal**, rather than an unspecified full-force black box.

---

# Part IV. What the stronger guard does—and does not—settle

## 11. Corrected complete-source criterion

Use either $B=B_{\rm new}$ or the slightly stronger $B=B_*$. Write


$$
y^F=2^B\widetilde y^F,\qquad
L=x_0^T\widetilde y^F\in\mathbb Z_2.
$$


Then


$$
H=2^a(E+2^BL),
\qquad
v_2(N)=2a+\nu,
$$


and hence


$$
\boxed{
\delta_2=v_2(H)-v_2(N)
=v_2(E+2^BL)-a-\nu.
}
\tag{11.1}
$$



For a target gap $k$, put


$$
T=a+\nu+k.
$$



- If $T\le B$, then
  

$$
\boxed{
  \delta_2\ge k
  \iff E\equiv0\pmod{2^T}.
  }
  \tag{11.2}
$$


  The logarithmic force can be omitted for this divisibility test. If the first nonzero digit at depth $T$ is to be preserved, use $T<B$.
- If $T>B$, then
  

$$
\boxed{
  \delta_2\ge k
  \iff
  E\in2^B\mathbb Z_2
  \quad\text{and}\quad
  E/2^B+L\in2^{T-B}\mathbb Z_2.
  }
  \tag{11.3}
$$



These remain complete-source statements. Formula (10.3) supplies an explicit source evaluation for the exponential part of either test.

### Correction to turn 15

The previous additional-depth expression must be replaced by


$$
\boxed{\max\{a+\nu+k-B,\,0\}.}
$$


At $k=\eta n+o(n)$, Theorem 7.1 gives


$$
a+\nu+k-B
=
\nu-
\left(1-\frac1{4002}-\eta\right)n+o(n).
$$


There is no longer a universal additional requirement of $0.04134n$.

---

## 12. The norm threshold is genuine, but not yet controlled

Let


$$
\rho=
1-\frac1{4002}-\eta
\approx0.45866.
$$



The new results give the following useful sufficient condition:


$$
\limsup_{u\to\infty}\frac{\nu}{n}<\rho
\quad\Longrightarrow\quad
\text{the logarithmic force is omissible at }k=\eta n+o(n)
$$


with a fixed linear safety margin.

The exact finite sufficient condition, using (7.2), is


$$
\boxed{
\nu+k+\lfloor\log_2(n+2)\rfloor-1\le B.
}
\tag{12.1}
$$



If this fails because the primitive norm is sufficiently deep, a favorable gap requires the exponential contraction itself to reach the nearly $n$-deep level $B$, followed, when necessary, by the complete logarithmic matching in (11.3).

This is a sharper mathematical separation than in turn 15:

- **first-column content:** now bounded by $O(\log n)$;
- **primitive norm loss:** still potentially linear;
- **mixed cancellation:** still requires an actual relative evaluation.

It is **not yet an unconditional no-go/favorable-subsequence dichotomy**.

### Why primitiveness does not bound $\nu$

A primitive vector over $\mathbb Z_2$ can have an arbitrarily deep sum of squares once the dimension is sufficiently large. For example, by the four-square theorem one may write


$$
2^M-1=a_1^2+a_2^2+a_3^2+a_4^2.
$$


Then


$$
(1,a_1,a_2,a_3,a_4)
$$


is primitive and has norm $2^M$.

This example is not claimed to arise from the present producer. It proves that a bound for $a$, integrality, and positivity of the real norm cannot alone bound $\nu$. A target-specific property of the corrected column is indispensable.

Likewise, even a sublinear norm-loss theorem would only justify deleting the logarithmic source at the needed precision. It would not prove that the exponential contraction has a shallow valuation relative to the norm.

### Concrete next lemma

A useful next result is therefore a **target-specific primitive-norm bound**


$$
\boxed{
v_2(x_0^Tx_0)\le(\rho-\varepsilon)n
\quad\text{on all sufficiently large original powers}
}
\tag{12.2}
$$


for some $\varepsilon>0$, or a structural description of the indices where it fails.

Unlike a first-column content question, this obligation cannot now be deferred to an unspecified content factor: that factor is controlled by Theorem 7.1.

After (12.2), the mixed problem is the explicitly bounded factorial observation (10.3), compared with the norm observation (8.1). A proof controlling their relative valuation must use their actual common adjoint $w$, actual source columns $\mathbf a_j$, and terminal. A generic resultant or an abstract recurrence-existence theorem does not supply that estimate.

---

## 13. The denominator and whole-error budget are unchanged

The historical ternary theorem remains


$$
\boxed{
v_3(q_n)=\frac{8003b-15}{2}.
}
$$


At $2$,


$$
v_2(q_n)=\max\{C_n-\delta_2,0\},
$$


where


$$
C_n=\frac{3n}{2}-v_2(b!)-s_2(n)-1.
$$



Let


$$
\mathcal O_n=\sum_{p\ne2,3}v_p(q_n)\log p\ge0.
$$


Under the retained whole-error theorem


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
\qquad
\log|\epsilon_n|=-\beta n+o(n),
$$


the complete same-index budget is


$$
\boxed{
\log|q_n\epsilon_n|
=
(\kappa-\beta)n
-\min(\delta_2,C_n)\log2
+\mathcal O_n+o(n).
}
\tag{13.1}
$$



Thus $\delta_2\ge\eta n+o(n)$ remains necessary for a decaying primitive error, and is not sufficient. Every surviving other-prime contribution must still be paid.

The strengthened logarithmic guard changes neither the real error nor the actual primitive denominator. It changes which complete-source terms must be evaluated at a specified binary precision.

---

# Part V. Independent audit of A5’s two-center no-go theorem

## 14. Exact cancellation uses the actual primitive pair

Let $i<j$ be original indices and


$$
c_i=\frac{p_i}{q_i},\qquad c_j=\frac{p_j}{q_j}
$$


their actual primitive centers. For


$$
A\in\mathbb Z\setminus\{0,1\},
$$


put


$$
P_A=(1-A)p_iq_j+A p_jq_i,\qquad Q_A=q_iq_j,
$$




$$
g_A=\gcd(Q_A,|P_A|),\qquad
q_A=Q_A/g_A,\qquad p_A=P_A/g_A.
$$


This is the correct all-prime reduction.

Write


$$
q_i=3^{d_i}s_i,\qquad q_j=3^{d_j}s_j,\qquad
D=d_j-d_i>0,
$$


with $3\nmid s_is_jp_ip_j$. Then


$$
P_A
=
3^{d_i}
\left(3^Dp_is_j+A U\right),
\qquad
U=p_js_i-3^Dp_is_j,
$$


and $U$ is a ternary unit.

Since $v_3(Q_A)=d_i+d_j$, complete ternary cancellation occurs exactly when


$$
\boxed{
A\equiv-3^Dp_is_jU^{-1}\pmod{3^{d_j}}.
}
\tag{14.1}
$$


Because $D<d_j$, every such representative has


$$
v_3(A)=D,\qquad |A|\ge3^D.
$$


A5’s congruence is therefore correct at full cancellation depth.

---

## 15. The coefficient/denominator tradeoff survives every other prime

If $a_3=v_3(A)<D$, then the two terms inside the parentheses have different valuations, so


$$
v_3(P_A)=d_i+a_3,\qquad
v_3(q_A)=d_j-a_3.
$$


Using


$$
|A-1|\ge|A|/2\ge3^{a_3}/2,
$$


we get


$$
q_A|A-1|\ge3^{d_j}/2.
$$



If $a_3\ge D$, then


$$
|A-1|\ge3^D/2,\qquad q_A\ge1.
$$


Thus, in all cases,


$$
\boxed{
q_A|A-1|\ge\frac12\,3^D.
}
\tag{15.1}
$$



The proof uses a lower bound for the actual primitive denominator, not the unreduced product $q_iq_j$. Cancellation at other primes cannot invalidate it.

---

## 16. Whole-error consequence and exact scope

The whole affine error is


$$
\epsilon_A=(1-A)\epsilon_i+A\epsilon_j.
$$


The original spacing is


$$
\frac{n(j)}{n(i)}=9^{32(j-i)}.
$$


The retained whole-error theorem implies


$$
\left|\frac{\epsilon_j}{\epsilon_i}\right|\to0
$$


uniformly for $j>i$ as $i\to\infty$. Since $|A|\le2|A-1|$, eventually


$$
|\epsilon_A|\ge\frac12|A-1||\epsilon_i|.
$$


Together with (15.1),


$$
|q_A\epsilon_A|
\ge\frac14\,3^D|\epsilon_i|.
$$



The exact ternary denominator law gives


$$
D=\left(1-\frac1{8004}\right)(n(j)-n(i)).
$$


Consequently,


$$
\log|q_A\epsilon_A|
\ge
\tau_3(n(j)-n(i))-\beta n(i)+o(n(i))-\log4,
$$


where


$$
\tau_3=\left(1-\frac1{8004}\right)\log3.
$$


This tends to $+\infty$, uniformly over the allowed integers $A$, as the lower index tends to infinity.

**Audit verdict:** the symbolic arithmetic theorem is proved, and the whole-error conclusion is a correct deduction from the retained analytic theorem.

Its limits matter:

- the theorem concerns nontrivial **integer affine** combinations;
- its asymptotic statement lets the lower original index tend to infinity;
- it does not establish an unrestricted theorem for rational coefficients;
- it does not exclude all original one-center approximations;
- it does not decide whether $e+\pi$ is irrational.

For coefficients satisfying (14.1), the same proof makes the unmultiplied whole error diverge.

---

# Part VI. Final status and arithmetic requirements

## 17. Proof ledger

| Statement | Status |
|---|---|
| NEW40 full-content/sign comparisons | Accepted finite corroboration at $m=241,\ldots,260$ |
| $29$-adic $\Xi=17$, with complete classified support | Accepted finite scalar evaluation at its stated normal-form scope |
| Alignment gcds $128$ at $3375$, $8$ at $11025$ | Accepted finite reference-alignment results |
| Universal reference-alignment support theorem | Not proved |
| Coordinator joint complete-logarithmic bound | **Independently proved above** |
| Refined guard $B_*$ | **Proved above** |
| Actual first-column content $a=O(\log n)$ | **New unconditional theorem on every original binary index** |
| Complete factorial-tail identity and paid linear cutoff | **New exact identities and bound** |
| Primitive norm loss $\nu<(\rho-\varepsilon)n$ | Open |
| Required relative exponential mixed-to-norm estimate | Open |
| All integer-affine two-center arithmetic tradeoff | Proof verified |
| Divergence of their whole primitive errors | Correct deduction from retained whole-error theorem |
| Favorable original one-center sequence with whole primitive error tending to zero | Not established |
| Irrationality or rationality of $e+\pi$ | Unresolved |

## 18. Bounded exact arithmetic needed

**No new bounded computation is required to verify the proofs in this report.**

In particular:

- do not rerun NEW40;
- do not rerun the $29$-adic lift or its older sums;
- do not regenerate either completed reference-alignment calculation;
- do not execute the optional $b=9$, twenty-thousand-bit logarithmic diagnostic.

The last calculation has a verifiable output already forced by proof:


$$
y^F\equiv0\pmod{2^{20000}},
$$


and hence its corresponding logarithmic mixed contribution vanishes at that precision. Computing the entire force would add no information about an unprotected digit.

Any future exact-arithmetic investigation of the remaining binary problem must specify an actual original index, determine the actual $\nu$, and pay the precision


$$
T=a+\nu+k
$$


together with the $2$-bit division in (10.3). Without those inputs, a proposed computation is only an unevaluated specification—not a certificate of a denominator-relevant gap. No such job is commissioned here.

---

## Conclusion

The coordinator’s joint estimate removes the principal precision objection raised in my turn 15. The complete logarithmic source is protected to approximately $0.99975n$ after the actual normalization, so the earlier unconditional demand for an additional $0.04134n$ of source cancellation must be withdrawn.

The principal new theorem of this turn is


$$
\boxed{
a\le\lfloor\log_2(n+2)\rfloor-1
}
$$


for the content of the **actual corrected first binary column on every original power**. Its proof supplies an exact low-valuation witness in the first force and transports that witness through the original finite reconstruction. This is not a reference-content inference.

The second advance is the complete relative-source representation


$$
w^Tf^0=2^{a+1}R\,x_0^Tx_0,
$$


together with the paid factorial-tail formula


$$
4x_0^Ty^E
=
W_bx_{0,b}
+\sum_{j=b}^{2n+b-1}\frac{j!}{b!}\,w^T\mathbf a_j.
$$


At target depth $T$, the latter admits the justified cutoff $j\le b+T+O(\log n)$, with its terminal and whole division retained.

The exact remaining bottleneck is therefore more narrowly identified:



$$
\boxed{
\begin{gathered}
\text{control the actual primitive norm loss }\nu
\text{ at the }0.45866n\text{ scale},\\
\text{and evaluate the relative factorial-tail contraction at }
a+\nu+0.54109n+o(n),\\
\text{including the complete logarithmic matching whenever that depth exceeds }B,\\
\text{then control all other primes in the actual primitive denominator.}
\end{gathered}}
$$



Neither the stronger logarithmic guard nor the new content bound alone resolves that relative-norm problem. A5’s valid two-center theorem rules out its precisely specified integer-affine modification, not arbitrary rational modifications or the irrationality question itself.

**No unconditional proof or disproof of the irrationality of $e+\pi$ follows.**
