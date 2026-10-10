> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5 — the $P_{64}$ input transfers uniformly; the fifth discrepancy is reduced, but not completed

I can close the missing **central-forcing truncation and parameter transfer**, and the **complete finite $P_{64}$ transfer**, including the first surviving $n$-contact correction.

I do **not** obtain a proved value of


$$
\Delta _5=\frac{H-N}{32}\pmod2
$$


on the true common-zero locus. Below I give a new bounded reduction of the remaining calculation: conditional on the stipulated complete $Q_5$ transfer, **only 31 residue classes modulo $128$ can contribute**. I give explicit moment-polynomial identities for all of them, their exact ranges, and their weight-carry classification. Their remaining higher-digit bilinear convolution is not evaluated here.

In particular, I do not infer mixed terms from the unaudited next-norm calculation.

---

## 1. Scope and retained interfaces

Throughout this report,


$$
b=9^r,\qquad n=4002b,\qquad r=18+32u,\quad u\ge0,
$$


and


$$
b=128D+81,\qquad n=128C+66,\qquad C=4002D+2532.
$$


Thus


$$
D\ \text{is odd},\qquad C\equiv2\pmod4.
$$



Set


$$
a=\frac{C-2}{4},\qquad v=\left\lfloor\frac D4\right\rfloor.
$$


The assigned locus is exactly


$$
\mathcal Z=\left\{r=18+32u:\ v\mathbin{\&}(a+1)\ne0\right\}.
$$


I use the established conclusions


$$
X,Y\in2\mathbb Z_2^{b+1},\qquad H-N\in32\mathbb Z_2
$$


on the parent domain, and


$$
N,H\in32\mathbb Z_2\qquad(r\in\mathcal Z).
$$


I do not rederive the fourth-layer results.

The actual columns and metric remain


$$
h=\frac n2,\quad R=2^h\binom{2h}{h},\quad
\lambda=\frac{(n!)^2}{2^n},
$$




$$
X=\frac{Z_w}{2R},\qquad Y=\frac{V_w}{4b!},
$$




$$
W_j=\binom{n+2}{j},\qquad
\omega_j=j!W_j=(n+2)_{\underline j},\qquad
\Omega=\operatorname{diag}(\omega_j^2)_{0\le j\le b}.
$$


Write


$$
N=X^TX>0,\qquad H=X^TY,\qquad
\alpha=v_2(N),\quad\gamma=v_2(H).
$$


The retained original-family mixed nonvanishing, not a residue computation, makes $\gamma$ finite.

Every actual inverse has range $0\le i,j<b$.

---

# Part I. Closing the complete $P_{64}$ input

## 2. Central truncation and uniform transfer to $h=161$

Because $C\equiv2\pmod4$,


$$
h=64C+33\equiv161\pmod{256},\qquad
n\equiv322\pmod{512}.
$$


Because $D$ is odd,


$$
b\equiv209\pmod{256}.
$$


Only bounded forcing and operator coefficients will be transferred to these references. The actual large binomial kernels and actual inverse range will not be replaced.

### 2.1 Exact central formulas and the $r$-tail

Use the exact normalized central formulas from turn12:


$$
B^{\rm cen}_{2j}
=
\left(\prod_{t=1}^{j}(2h+2t-1)\right)
(h)_{\underline j}
\sum_{s\ge0}
\frac{2^s(s!)^2}{(2s)!}
\binom{h-j}{s}\binom{h+j}{s},
\tag{2.1}
$$




$$
B^{\rm cen}_{2j+1}
=
\left(\prod_{t=0}^{j}(2h+2t+1)\right)
(h)_{\underline{j+1}}
\sum_{s\ge0}
\frac{2^s(s!)^2}{(2s+1)!}
\binom{h-j-1}{s}\binom{h+j}{s}.
\tag{2.2}
$$



For either scalar coefficient in these sums,


$$
v_2\!\left(\frac{2^s(s!)^2}{(2s)!}\right)
=
v_2\!\left(\frac{2^s(s!)^2}{(2s+1)!}\right)
=v_2(s!).
\tag{2.3}
$$


After its power of $2$ is extracted, the denominator is odd. All binomial factors and prefactors are $2$-integral.

For $s\ge8$,


$$
v_2(s!)\ge v_2(8!)=7.
$$


Therefore every such summand vanishes modulo $64$, uniformly in every retained central index. Only


$$
0\le s\le7
\tag{2.4}
$$


is needed.

### 2.2 The entire central-index tail $\ell\ge7$

On $h\equiv1\pmod{32}$,


$$
v_2(h-1)=5,\qquad v_2(h-3)=1.
$$


For odd $\ell\ge7$, the falling factorial in (2.2) contains both $h-1$ and $h-3$. For even $\ell\ge8$, the same holds in (2.1). Consequently their prefactors have valuation at least $6$, while the normalized sums are $2$-integral.

Thus


$$
\boxed{B^{\rm cen}_\ell\equiv0\pmod{64}\qquad(\ell\ge7).}
\tag{2.5}
$$


Indices outside the original central coefficient range have zero coefficient. This is an all-index truncation argument, not an extrapolation from the zero entries in the receipt.

### 2.3 Transfer of every retained central sum

For integer $x,\delta$ and $k\ge1$,


$$
v_2\!\left(\binom{x+\delta}{k}-\binom{x}{k}\right)
\ge v_2(\delta)-\lfloor\log_2k\rfloor.
\tag{2.6}
$$


Indeed, Vandermonde reduces the difference to terms involving $\binom{\delta}{j}$, and


$$
\binom{\delta}{j}
=\frac{\delta}{j}\binom{\delta-1}{j-1}.
$$



For $0\le\ell\le6$ and $0\le s\le7$, changing $h$ to $161$ changes each binomial factor in (2.1)–(2.2) by a multiple of


$$
2^{8-\lfloor\log_2 7\rfloor}=2^6.
$$


The prefactors are products of integral affine functions of $h$, so their changes are divisible by $2^8$. The scalar factors (2.3) are $2$-integral and cause no additional loss.

It follows that **each complete retained central sum**, not just its prefactor, agrees modulo $64$ with its $h=161$ value.

The supplied exact finite evaluation can therefore be transferred:


$$
\boxed{
(B^{\rm cen}_0,\ldots,B^{\rm cen}_6)
\equiv(2,3,3,32,0,32,32)\pmod{64}.
}
\tag{2.7}
$$



This uses the receipt only as a bounded arithmetic evaluation, after the infinite transfer and both truncations have been proved.

---

## 3. Complete normalized forcing, including its index tail

The exact forcing is


$$
\frac{f_i^0}{R}
=
\sum_{\ell=0}^{i}
\binom i\ell
\left(\prod_{t=\ell+1}^{i}(n+t)\right)
B^{\rm cen}_\ell.
\tag{3.1}
$$



For $i\le7$, all retained products are integral polynomials in $n$. Since $n-322$ is divisible by $512$, (2.7) transfers these forcing entries modulo $64$.

The tail $i\ge8$ requires a separate argument.

### 3.1 Exact factorial-product depths

For $n\equiv322\pmod{512}$, the valuations of $n+t$, $1\le t\le10$, are


$$
(0,2,0,1,0,3,0,1,0,2).
\tag{3.2}
$$


At $i=8$, the products in (3.1) consequently have these depths:


$$
\begin{array}{c|rrrrrrr}
\ell&0&1&2&3&4&5&6\\ \hline
v_2\!\left(\prod_{t=\ell+1}^{8}(n+t)\right)
&7&7&5&5&4&4&1.
\end{array}
\tag{3.3}
$$



The central coefficients have lower depths


$$
(1,0,0,5,6,5,5)
\tag{3.4}
$$


for $\ell=0,\ldots,6$. Thus every $\ell\ne2$ term in (3.1) is already zero modulo $64$ for every $i\ge8$.

For $\ell=2$, the two exceptional indices are disposed of by


$$
v_2\binom82=v_2\binom92=2.
$$


For $i\ge10$, the factorial product itself has depth at least $7$, by the last entry of (3.2).

Together with (2.5), this proves


$$
\boxed{\frac{f_i^0}{R}\equiv0\pmod{64}\qquad(i\ge8).}
\tag{3.5}
$$



No finite string of zero forcing entries is being used in place of this product argument.

### 3.2 Transferred forcing polynomial

The bounded reference values therefore give the complete forcing


$$
\boxed{
f^0/R\equiv(2,9,51,57,12,36,48,16,0,\ldots)\pmod{64}.
}
\tag{3.6}
$$


After inverse Pascal transformation, its signed Newton polynomial is


$$
\boxed{
g_{64}(z)=
2+55\binom z1+51\binom z2+7\binom z3
+12\binom z4+28\binom z5
+48\binom z6+48\binom z7
\pmod{64}.
}
\tag{3.7}
$$



This closes the previously missing independent forcing input.

---

## 4. Full finite $P_{64}$ reference transfer

### 4.1 An explicit integral polynomial operator

For $t\ge1$, define the signed suffix operator


$$
(\mathscr T_{t,b}f)(x)
=
\sum_{k=x}^{b-1}
\binom{t+k-x-1}{t-1}f(k),
\tag{4.1}
$$


interpreted by its polynomial continuation; put $\mathscr T_{0,b}f=f$.

With


$$
(c_1,c_2,c_3,c_4)=(-1,2,-3,3),
$$


the signed contact operator is


$$
\boxed{
\mathscr E_{n,b}f(x)=
\sum_{s=1}^{4}\sum_{t=0}^{s}
c_s(-1)^{s-t}\binom{x}{s-t}\binom nt
(\mathscr T_{t,b}f)(x-s+t).
}
\tag{4.2}
$$


On $0\le i<b$, this is exactly


$$
E(n)\mathcal S_bf=\mathcal S_b(\mathscr E_{n,b}f).
$$


When $i<s-t$, the vanishing factor $\binom{i}{s-t}$ handles the lower boundary.

All these operators preserve integral Newton polynomials. If $\deg f\le d$, then


$$
\deg\mathscr T_{t,b}f\le d+t,\qquad
\boxed{\deg\mathscr E_{n,b}f\le d+4.}
\tag{4.3}
$$



For the parameter estimate, expand the summand in (4.1) in the Newton basis in $k$. Its degree is at most $d+t-1$, so its upper-boundary dependence uses only


$$
\binom bk,\qquad k\le d+t.
\tag{4.4}
$$


Equation (2.6) therefore controls the $b$-dependence in every iterate. This also proves coefficient congruences: integral finite differences transfer the uniform value congruences to Newton coefficients.

### 4.2 Every inverse iterate is retained at its required precision

At raw $P$-precision $64$, the established divided-power contact congruence is


$$
\phi^n\equiv1+2U\pmod{64}.
$$


Consequently the complete polynomial inverse is


$$
P_{64}
=
\sum_{\ell=0}^{5}(-2)^\ell
\mathscr E_{n,b}^{\,\ell}g_{64}
\pmod{64}.
\tag{4.5}
$$


All later iterates vanish because the operator is integral and their scalar coefficient is divisible by $64$.

For degree accounting, split


$$
g_{64}=g^{(0)}+4g^{(2)}+16g^{(4)},
$$


where the respective degree bounds are $3,5,7$. The retained iterates of these pieces have


$$
\ell\le5,\qquad \ell\le3,\qquad \ell\le1,
$$


respectively. Thus


$$
\boxed{\deg P_{64}\le23.}
\tag{4.6}
$$



This sharpens the raw degree-$27$ bound without pretending that $g_{64}$ has degree three.

### 4.3 Transfer of $b$ to $209$

Since $v_2(b-209)\ge8$, the complete weighted requirements are:



$$
\begin{array}{c|c|c|c}
\ell&
\text{largest needed }b\text{-index}&
\text{available unweighted depth}&
\text{required unweighted depth}\\ \hline
1&11&5&5\\
2&13&5&4\\
3&17&4&3\\
4&19&4&2\\
5&23&4&1
\end{array}
\tag{4.7}
$$



The index bounds use the coefficient-valued degree split above. A telescoping expansion of the difference of two iterates applies (4.4) at each possible changed operator. All other operators preserve the resulting divisibility.

Therefore every term of (4.5) transfers to $b=209$ at its weighted precision.

### 4.4 Transfer of $n$, and the correction relative to $n=2$

Because $v_2(n-322)\ge9$, for $t\le4$,


$$
v_2\!\left(\binom nt-\binom{322}{t}\right)\ge7.
$$


Thus replacing $n$ by $322$ in (4.2) is more than sufficient for every inverse term.

The $n=2$ substitution, in contrast, has a surviving correction. Modulo $32$,


$$
E(n)\equiv E(2)+16T(-4).
\tag{4.8}
$$


Only the first inverse term can retain this difference modulo $64$, giving


$$
-32\mathscr T_{4,b}g_{64}.
$$



Modulo $2$,


$$
g_{64}(x)\equiv x+\binom x2+\binom x3,
$$


the indicator of $x\not\equiv0\pmod4$. Since $b=4m+1$ with $m$ even, the suffix count in (4.1) gives


$$
\mathscr T_{4,b}g_{64}
\equiv
\binom x5+\binom x6+\binom x7\pmod2.
\tag{4.9}
$$


Indeed, the kernel is odd exactly when $k-x\equiv0\pmod4$. At $x=4s+\rho$, $\rho=1,2,3$, the number of admissible terms has parity $s$; at $\rho=0$, the forcing is zero.

Hence an alternative complete reference formula is


$$
\boxed{
P_{64}\equiv
\sum_{\ell=0}^{5}(-2\mathscr E_{2,209})^\ell g_{64}
+32\left(\binom x5+\binom x6+\binom x7\right)
\pmod{64}.
}
\tag{4.10}
$$


This explicitly retains the $n$-contact correction rather than hiding it in the reference computation.

### 4.5 Transferred result and actual reconstruction

The supplied fixed reference coefficients therefore transfer to every original index:


$$
\boxed{
(p_0,\ldots,p_{11})
=(34,31,7,5,48,12,4,4,32,8,56,8)\pmod{64},
}
\tag{4.11}
$$


with all higher coefficients zero modulo $64$.

The degree proof (4.6) is important here: the fixed zero coefficients through degree $23$ certify the whole polynomial. They are not finite samples of an unbounded-degree assertion.

The actual first solution remains


$$
\boxed{
\theta=T(-2n)\mathcal S_bP_{64}\pmod{64},
}
\tag{4.12}
$$


and


$$
\boxed{
2X_j\equiv W_j(j\theta_{j-1}-\theta_j)\pmod{64},
\qquad \theta_{-1}=\theta_b=0.
}
\tag{4.13}
$$


Neither $T(-2n)$ nor its finite range has been replaced by a reference operator.

---

# Part II. Complete fifth moment identities

## 5. The stipulated $Q_5$ input and complete forces

For the remaining mixed calculation, I take the requested $Q_5$ transfer as a **conditional input**:


$$
Q_5=
2\sum_{\ell=0}^{5}(-2\mathscr E_{2,81})^\ell a_{32}
+64\left(1+\binom x7\right)\pmod{128},
\tag{5.1}
$$


where


$$
a_{32}=10+2x+24\binom x2+15\binom x3.
$$


Thus the $64(1+\binom x7)$ correction is retained.

Its supplied coefficient vector is


$$
(q_0,\ldots,q_{11})
=(52,36,24,6,112,48,64,8,32,32,64,112)\pmod{128}.
\tag{5.2}
$$



The complete retained exterior values are


$$
(B_0,\ldots,B_6)
=(69,106,54,56,120,80,112)\pmod{128}.
\tag{5.3}
$$


They arise from all seven factorial products


$$
f_s=\prod_{t=1}^{s}(b+t),\qquad 0\le s\le6.
$$


The next product has the exact depth


$$
v_2(f_7)=1+0+2+0+1+0+3=7
$$


on $b\equiv209\pmod{256}$; all later products have at least that depth.

The whole logarithmic force is absent only because its retained estimate gives


$$
v_2(h_i^F/b!)
\ge2000b+2-2\lfloor\log_2(8005b-1)\rfloor>7.
\tag{5.4}
$$



Thus the conditional complete second solution is


$$
\eta_i\equiv
-\sum_{s=0}^{6}B_s\binom{-2n}{b+s-i}
+(T(-2n)\mathcal S_bQ_5)_i
\pmod{128}.
\tag{5.5}
$$


The reconstruction includes


$$
4Y_j\equiv W_b\mathbf1_{j=b}
+W_j(j\eta_{j-1}-\eta_j)\pmod{128}.
\tag{5.6}
$$



---

## 6. Explicit moment-polynomial coefficients for every coordinate

Put


$$
A=2n,\qquad L_j=b-1-j,\qquad
\mathcal M_s(j)=\binom{A+L_j}{L_j-s}.
\tag{6.1}
$$


All these binomials retain their actual parameters.

Define


$$
d_r=q_r-2p_r\pmod{128}.
$$


The complete vector is


$$
\boxed{
(d_0,\ldots,d_{11})
=(112,102,10,124,16,24,56,0,96,16,80,96).
}
\tag{6.2}
$$



### 6.1 Bounded moment factors may use $A=4$

Here


$$
A=4+128(2C+1).
$$


In the exact finite moment identity, the bounded factors are


$$
\binom{A+s-1}{s},\qquad 0\le s\le11.
$$


The parameter loss is at most $\lfloor\log_2s\rfloor$.

For the $P$-coefficients, the odd coefficients occur only through degree three; degrees $4$–$7$ have depth at least two, and degrees $8$–$11$ have depth at least three. Thus the replacement


$$
\binom{A+s-1}{s}\longmapsto\binom{s+3}{3}
$$


is valid in the entire $P$-moment expansion modulo $64$.

For $d$, degrees one and two have depth at least one, degree three at least two, and all larger retained degrees have enough additional factors to make the same replacement valid modulo $128$.

This replacement concerns only the bounded factors—not $\mathcal M_s(j)$.

### 6.2 Polynomial coefficients before reconstruction

For $0\le s\le11$, put


$$
F_s(x)=
\binom{s+3}{3}\sum_{r=s}^{11}p_r\binom{x}{r-s},
\tag{6.3}
$$




$$
G_s(x)=
\binom{s+3}{3}\sum_{r=s}^{11}d_r\binom{x}{r-s}.
\tag{6.4}
$$



The exact finite moment summation used is


$$
\sum_{t=0}^{L}
\binom{A+t-1}{t}\binom tv
=
\binom{A+v-1}{v}\binom{A+L}{L-v}.
\tag{6.5}
$$


It gives


$$
\theta_j\equiv(-1)^j
\sum_{s=0}^{11}F_s(j)\mathcal M_s(j)\pmod{64}.
\tag{6.6}
$$



For the complete difference $\zeta=\eta-2\theta$, Vandermonde transforms the exterior force into negative moments. Its seven coefficients are


$$
\beta_k=\sum_{s=k-1}^{6}(-1)^sB_s\binom{s}{k-1},
\qquad1\le k\le7,
$$


namely


$$
\boxed{
(\beta_1,\ldots,\beta_7)
=(113,74,78,72,120,80,112)\pmod{128}.
}
\tag{6.7}
$$



Define


$$
Z_{-k}(x)=\beta_k\quad(1\le k\le7),\qquad
Z_s(x)=G_s(x)\quad(0\le s\le11),
$$


and set all other $Z_s$ to zero. Then


$$
\boxed{
\zeta_j\equiv(-1)^j
\sum_{s=-7}^{11}Z_s(j)\mathcal M_s(j)\pmod{128}.
}
\tag{6.8}
$$



### 6.3 Reconstruction coefficient identities

Set $F_s=0$ outside $0\le s\le11$, and define


$$
\boxed{
U_s(x)=F_s(x)+xF_s(x-1)+xF_{s+1}(x-1),
\quad -1\le s\le11,
}
\tag{6.9}
$$




$$
\boxed{
V_s(x)=Z_s(x)+xZ_s(x-1)+xZ_{s+1}(x-1),
\quad -8\le s\le11.
}
\tag{6.10}
$$


These formulas follow directly from


$$
\mathcal M_s(j-1)=\mathcal M_{s-1}(j)+\mathcal M_s(j).
$$



For clarity, the complete negative part of (6.10) is


$$
\begin{array}{c|l}
s&V_s(x)\pmod{128}\\ \hline
-8&112x\\
-7&112+64x\\
-6&80+72x\\
-5&120+64x\\
-4&72+22x\\
-3&78+24x\\
-2&74+59x\\
-1&113+113x+xG_0(x-1).
\end{array}
\tag{6.11}
$$


The nonnegative part is explicitly given by (6.4), (6.10), and the numerical vector (6.2). No mixed coefficient is inferred from a norm formula.

Let


$$
\mathcal F_j=\sum_{s=-1}^{11}U_s(j)\mathcal M_s(j),
\qquad
\mathcal G_j=\sum_{s=-8}^{11}V_s(j)\mathcal M_s(j).
\tag{6.12}
$$


For every $0\le j<b$,


$$
\boxed{
2X_j\equiv(-1)^{j+1}W_j\mathcal F_j\pmod{64},
}
\tag{6.13}
$$




$$
\boxed{
4(Y_j-X_j)\equiv(-1)^{j+1}W_j\mathcal G_j\pmod{128}.
}
\tag{6.14}
$$



These identities include the complete exterior force and all off-pair even and odd coordinates.

### 6.4 Coefficient periodicity, not kernel periodicity

The displayed valuations of $p_r$ give


$$
U_s(x+128)\equiv U_s(x)\pmod{64}.
\tag{6.15}
$$


For $r\le3$, translation loses at most one of the seven available bits; the higher coefficients supply the needed extra divisibility.

Likewise, (6.2) gives


$$
V_s(x+128)\equiv V_s(x)\pmod{128}.
\tag{6.16}
$$


For example, the depth-one coefficients have degree at most two, so the worst available depth is $7+1-1=7$. All higher terms have a margin. Multiplication by $x$ in reconstruction introduces a change divisible by $128$.

Thus only bounded coefficient tables $U_s(\rho)$, $V_s(\rho)$, $0\le\rho<128$, are needed. The moments $\mathcal M_s(j)$ themselves remain unbounded, actual binomials.

---

# Part III. A new bounded support and carry reduction

## 7. Every coordinate with $v_2(W_j)\ge4$ contributes zero

This statement concerns the fifth mixed discrepancy, not merely the norm.

For an interior coordinate, (6.13)–(6.14) give the raw numerator


$$
W_j^2\mathcal F_j\mathcal G_j,
\tag{7.1}
$$


which is to be evaluated modulo $512$.

If $w=v_2(W_j)\ge5$, its divisibility by $512$ is immediate. It remains to treat $w=4$.

### 7.1 The required moment parities

From (4.11),


$$
P_{64}(x)\equiv x+\binom x2+\binom x3\pmod2.
$$


Since the higher bounded moment factors are even wherever needed, (6.9) gives


$$
\mathcal F_j\equiv
\begin{cases}
0,&j\equiv0\pmod4,\\
\mathcal M_0(j),&j\equiv1,2\pmod4,\\
\mathcal M_{-1}(j),&j\equiv3\pmod4.
\end{cases}
\pmod2.
\tag{7.2}
$$


Only $\beta_1$ is odd in (6.7), and all $d_r$ are even. Hence


$$
\mathcal G_j\equiv
\begin{cases}
\mathcal M_{-1}(j),&j\ \text{even},\\
\mathcal M_{-2}(j),&j\ \text{odd}
\end{cases}
\pmod2.
\tag{7.3}
$$



For even $j$, $L_j+1$ and $A-1$ are both odd. Thus


$$
\mathcal M_{-1}(j)=\binom{A+L_j}{L_j+1}
$$


is even by Kummer. This kills (7.1) when $w=4$.

For $j\equiv3\pmod4$, $L_j+2\equiv3\pmod4$, while $A-2\equiv2\pmod4$. Therefore $\mathcal M_{-2}(j)$ is even, again killing (7.1).

### 7.2 The remaining odd class

Write


$$
j=4k+1,\qquad
m=\frac{b-1}{4},\qquad M=\frac{n+2}{4},\qquad
\ell=m-k.
$$


The exact weight depth is


$$
v_2(W_j)=2+v_2\binom{M-1}{k}.
\tag{7.4}
$$


Here $v_2(M-1)=4$. If $k$ were odd, the identity


$$
\binom{M-1}{k}
=\frac{M-1}{k}\binom{M-2}{k-1}
$$


would force $v_2(W_j)\ge6$. Thus $w=4$ requires $k$ even.

Since $m$ is even, $\ell$ is then even. Lucas gives


$$
\mathcal M_0(j)
=\binom{4(h+\ell)-1}{4\ell-1}
\equiv\binom{h+\ell-1}{\ell-1}=0\pmod2,
$$


because $h+\ell-1$ is even and $\ell-1$ is odd.

This finishes the proof:


$$
\boxed{
v_2(W_j)\ge4
\quad\Longrightarrow\quad
X_j(Y_j-X_j)\equiv0\pmod{64}
\qquad(0\le j<b).
}
\tag{7.5}
$$



This is a new precision-specific mixed support reduction.

---

## 8. Exact classification of the remaining 31 residue classes

Write


$$
j=128t+\rho,\qquad0\le\rho<128.
$$


Since


$$
n+2=128C+68,
$$


the low-block subtraction gives an exact weight-depth split.

### 8.1 Residues $0\le\rho\le68$

Put


$$
\eta_t=v_2\binom Ct,\qquad
\beta_\rho=v_2\binom{68}{\rho}.
$$


Then


$$
\boxed{v_2(W_{128t+\rho})=\beta_\rho+\eta_t.}
\tag{8.1}
$$



The residues with $\beta_\rho\le3$ are exactly:



$$
\begin{array}{c|l}
\beta_\rho&\rho\\ \hline
0&0,4,64,68\\
1&2,32,36,66\\
2&1,3,16,20,34,48,52,65,67\\
3&8,12,18,24,28,33,35,40,44,50,56,60.
\end{array}
\tag{8.2}
$$



For example,


$$
v_2\binom{68}{4k}=v_2\binom{17}{k}.
$$


For $2\le k\le16$,


$$
v_2\binom{17}{k}=4-v_2(k)-v_2(k-1),
$$


with the endpoint values handled directly. Similarly,


$$
v_2\binom{68}{4k+2}
=
\begin{cases}
1,&k=0,16,\\
5-v_2(k),&1\le k\le15,
\end{cases}
$$


and for the odd positions,


$$
v_2\binom{68}{4k+1}
=
v_2\binom{68}{4k+3}
=2+v_2\binom{16}{k}.
$$


These identities prove the exhaustive table (8.2), rather than merely checking selected residues.

All classes in (8.2) have the actual range


$$
0\le t\le D.
$$


By (7.5), a term remains only when


$$
\eta_t\le3-\beta_\rho.
\tag{8.3}
$$



### 8.2 Residues $\rho>68$

Put


$$
\zeta_t=v_2\!\left((C-t)\binom Ct\right).
$$


The borrow across the low block gives


$$
\boxed{
v_2(W_{128t+\rho})
=
v_2\binom{196}{\rho}+\zeta_t.
}
\tag{8.4}
$$


Also,


$$
(C-t)\binom Ct=C\binom{C-1}{t},
$$


so, because $v_2(C)=1$,


$$
\zeta_t=1+v_2\binom{C-1}{t}\ge1.
\tag{8.5}
$$



Among $69\le\rho\le127$, the only residues with


$$
v_2\binom{196}{\rho}\le2
$$


are


$$
\boxed{\rho=96,\ 100,}
$$


and both have depth two. Consequently these classes survive only if


$$
\boxed{\binom{C-1}{t}\ \text{is odd}.}
\tag{8.6}
$$


Their actual range is


$$
\boxed{0\le t\le D-1.}
\tag{8.7}
$$



For completeness, the exclusion of the other residues follows by dividing into $\rho=4k,4k+2,4k+1,4k+3$. In the first case,


$$
v_2\binom{196}{4k}=v_2\binom{49}{k};
$$


for $18\le k\le31$, only $k=24,25$ have depth at most two. The $4k+2$ depths are at least three, and the odd depths at least four. Thus no additional overflow residue is missing.

Equations (8.2), (8.6) give exactly $29+2=31$ potential residue classes.

### 8.3 The actual endpoint

The endpoint is retained as


$$
X_b=\frac{W_b\,b\theta_{b-1}}2,\qquad
Y_b=\frac{W_b(1+b\eta_{b-1})}{4}.
$$


The established $v_2(W_b)\ge6$ implies


$$
v_2(X_b)\ge5,\qquad v_2(Y_b)\ge4.
$$


Hence


$$
X_b(Y_b-X_b)\in2^9\mathbb Z_2.
\tag{8.8}
$$


The endpoint therefore contributes zero to the fifth discrepancy, after its $+1$ has been retained.

---

## 9. The exact remaining scalar—not an evaluated fifth digit

Here is a precise expression for what remains.

Put


$$
\kappa=2C+1,\qquad d=D-t.
$$


For each surviving residue, define the actual moments


$$
M_s(\rho,t)
=
\binom{128(\kappa+d)+84-\rho}
      {128d+80-\rho-s},
\tag{9.1}
$$


and


$$
F_\rho(t)=\sum_{s=-1}^{11}U_s(\rho)M_s(\rho,t),
\qquad
G_\rho(t)=\sum_{s=-8}^{11}V_s(\rho)M_s(\rho,t).
\tag{9.2}
$$


Also put


$$
W_{\rho,t}=\binom{128C+68}{128t+\rho}.
$$



Let $\mathcal R_\beta$ denote the four rows of (8.2). Then the complete raw scalar is


$$
\begin{aligned}
\mathscr S\equiv{}&
\sum_{\beta=0}^{3}\ \sum_{\rho\in\mathcal R_\beta}
\ \sum_{\substack{0\le t\le D\\
v_2\binom Ct\le3-\beta}}
W_{\rho,t}^{\,2}F_\rho(t)G_\rho(t)\\
&+
\sum_{\rho\in\{96,100\}}
\ \sum_{\substack{0\le t\le D-1\\
\binom{C-1}{t}\ {\rm odd}}}
W_{\rho,t}^{\,2}F_\rho(t)G_\rho(t)
\pmod{512}.
\end{aligned}
\tag{9.3}
$$



The reconstruction proves


$$
\boxed{\mathscr S\equiv8(H-N)\pmod{512}.}
\tag{9.4}
$$


Thus, on the true common-zero locus—and in fact wherever the established fourth discrepancy applies—


$$
\boxed{\Delta _5\equiv\frac{\mathscr S}{256}\pmod2.}
\tag{9.5}
$$



The precision is sufficient. Changing $\mathcal F_j$ by $64$ changes the raw product by a multiple of $512$, because


$$
W_j\mathcal G_j\equiv4(Y_j-X_j)\in8\mathbb Z_2.
$$


Changing $\mathcal G_j$ by $128$ is also harmless, because


$$
W_j\mathcal F_j\equiv2X_j\in4\mathbb Z_2.
$$


The division in (9.5) is performed only after the complete sum. Individual paired terms need not be divisible by $256$.

**What has not been done:** I have not evaluated (9.3) as a function of the actual higher digits of $C,D$, nor proved it zero on


$$
v\mathbin{\&}(a+1)\ne0.
$$


The weight classification alone does not classify the normalized units of the products in (9.3). Those units matter at the fifth digit.

In particular, the off-pair norm support cannot eliminate these mixed terms. Coordinates with


$$
v_2(X_j)=3,\qquad v_2(Y_j)=2
$$


have zero square modulo $64$, but may contribute $32$ to $X_jY_j$. Equations (6.9)–(9.3) retain precisely that possibility.

I have neither used nor audited the next-norm formula from turn19. Even if its conclusion on $r=50+128w$ is retained, it gives only


$$
\alpha\ge6,\qquad\gamma\ge5,
$$


not relative alignment or a value of $\Delta _5$.

---

## 10. Actual primitive arithmetic and whole real error

The center and metric are unchanged:


$$
c_n=\frac{2b!}{\lambda R}\frac HN.
$$



Let $d_B$ be the least common denominator of the actual two-column lift, and put


$$
N_B=d_B[u,v].
$$


Retain the integer contractions


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$


and the final gcd


$$
g_B=\gcd(A_B,|H_B|).
$$


Then


$$
p_n=\frac{H_B}{g_B},\qquad q_n=\frac{A_B}{g_B}>0,
\qquad c_n=\frac{p_n}{q_n}.
$$


The primitive multiplier relative to the uncleared quadratic pair is


$$
\frac{d_B^2}{g_B}.
$$



With $s=s_2(n)$, the retained exact binary interface is


$$
v_2(g_B)=
\min\left\{
3n-2s+2+\alpha,\,
\frac{3n}{2}-s+v_2(b!)+3+\gamma
\right\},
$$




$$
\boxed{
v_2(q_n)=
\max\left\{
0,\frac{3n}{2}-v_2(b!)-s-1-(\gamma-\alpha)
\right\}.
}
\tag{10.1}
$$


Neither the new forcing transfer nor the 31-class reduction bounds $\gamma-\alpha$.

Within the retained complete signed-error theorem,


$$
\epsilon_n=c_n-(e+\pi)<0
\quad\text{eventually},
$$




$$
\log|\epsilon_n|
=-\left(2+\frac1{4002}\right)n\log(1+\sqrt2)+o(n).
$$


The whole primitive evaluated form is


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n>0
}
\quad\text{eventually}.
\tag{10.2}
$$


This retains the complete real error, actual denominator, final gcd, and eventual nonvanishing. No irrationality or rationality conclusion follows.

---

# Concluding ledger

## (1) New result and proof status

**Proved from the exact central formulas and supplied fixed arithmetic evaluations:**

- The complete central truncations $s\le7$, $\ell\le6$ modulo $64$.
- Uniform transfer of every retained central sum from $h\equiv161\pmod{256}$ to $h=161$.
- The complete forcing cutoff $i\le7$, with exact factorial-product depths for the entire tail.
- The full forcing polynomial $g_{64}$.
- Uniform finite $P_{64}$ transfer to $n=322,b=209$, including every inverse iterate, weighted $b$-loss, and degree bound.
- The explicit surviving correction relative to $n=2$, equation (4.10).
- The complete raw first column $2X\bmod64$.

**Derived conditionally on the stipulated complete $Q_5$ transfer:**

- Explicit moment-polynomial coefficient identities for the whole reconstructed difference, including all seven exterior forces.
- Coefficient periodicity modulo $128$ in the coordinate, without replacing the actual large kernels.
- Vanishing of every fifth-defect contribution with $v_2(W_j)\ge4$.
- An exhaustive 31-residue carry reduction, with exact finite ranges and the actual endpoint.
- The complete remaining scalar (9.3).

**Not proved:** a value of the fifth discrepancy on the true common-zero locus, an unrestricted relative-valuation bound, or irrationality of $e+\pi$.

## (2) Exact remaining bottleneck

The immediate bottleneck is the higher-digit, unit-sensitive bilinear convolution (9.3). It must be evaluated on the actual relation


$$
C=4002D+2532,\qquad
D=\frac{9^r-81}{128},
\qquad
v\mathbin{\&}(a+1)\ne0.
$$


The 31-class support and low weight-carry classification do not evaluate that convolution.

Beyond this digit, the arithmetic bottleneck remains control of the actual reduced denominator after the final gcd, including a justified unrestricted-depth estimate on $\gamma-\alpha$.

## (3) Bounded computation request

A useful next independent control is a **fixed moment-coefficient certificate**, not a growing-index sample.

**Inputs**

- The vectors $p,d,\beta$ in (4.11), (6.2), (6.7).
- The definitions (6.3), (6.4), (6.9), (6.10).
- The 31 residues listed in (8.2), together with $96,100$.
- Raw coefficient moduli $64$ for $U$, $128$ for $V$.

**Expected verifiable outputs**

1. The complete vectors
   

$$
(U_s(\rho))_{-1\le s\le11}\pmod{64},\qquad
   (V_s(\rho))_{-8\le s\le11}\pmod{128}
$$


   for those 31 residues.
2. Newton-coefficient certificates for
   

$$
U_s(128z+\rho)-U_s(\rho)\equiv0\pmod{64},
$$


   

$$
V_s(128z+\rho)-V_s(\rho)\equiv0\pmod{128}.
$$


   Degree at most $12$ suffices for each certificate.
3. A direct comparison with the finite moment expansion using the bounded factor
   

$$
\binom{644+s-1}{s},
$$


   certifying its agreement with the factor $\binom{s+3}{3}$ at the stated coefficient precisions.

These are bounded polynomial checks. Even a passing receipt would **not** prove an infinite value for (9.3); its unbounded carry convolution would still require an explicit mathematical evaluation.
