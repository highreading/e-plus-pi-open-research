> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A3 Turn 15: independent audits of the paid dyadic reduction and the degree-controlled source period

## 1. Executive conclusions

### First primary: A2 turn10, Sections 7–8

**PASS.** The complete-source annihilator, factorial-normalized forcing pivot, literal atom valuation, and simultaneous reduction of $H_{0,k}$, $H_{1,k}$, and their **all-prime** gcd are valid at the stated scope.

In particular:

- the row operator is a literal finite integer operator with the stated odd determinant;
- it cancels the rational forcing in **every** common return column;
- both factorial terms remain;
- the normalized forcing determinant is odd, with all factorial divisions paid;
- the contact atom $w_n=(-1)^n$ is retained and gives the claimed exact valuation;
- the Schur clearer and subsequent column divisions are valid for both affine coefficients;
- the original final row and complete remaining border are unchanged;
- the exact all-prime gcd identity and the original-domain formula for $\kappa_k$ are correct.

No repair to those mathematical identities is required. Some intermediate divisibility checks, especially for the affine border, are supplied explicitly below.

This audit does **not** prove the residual paired upper bound. In particular, neither


$$
v_2(G_k)\le \frac{13}{4}k^2+o(k^2)
\quad\text{nor}\quad
v_2(G_k)\le \frac{19}{4}k^2+o(k^2)
$$


has been established.

### Second primary: the degree-controlled source-input period

**PASS, conditional on the full precision-local producer theorem at its stated scope.**

For $M\ge4$, $1\le L\le3M$, and sufficiently large original $n$, the sufficient input exponent is indeed


$$
\boxed{E=M+\lfloor\log_3(6M-1)\rfloor.}
$$


This pays not only the transformed matrix entries, but also:

- the transformed next-column force;
- all last-$3M$ force products and their factors $(-2)^a$;
- all required top Pascal reconstructions;
- the dense known part of $h$;
- both scalar contractions;
- division of $\Xi$ and $\chi$ by $3$;
- both original affine forcing constants;
- the unit division by $n-1$;
- monic division by $x+2$.

The window is **not** shortened.

There is one necessary wording qualification: the bound $6M-1$ applies to every **$n$-dependent binomial evaluation after the stated local reduction**. It does not literally bound every lower index occurring in the fixed small Pascal tables used to construct interpolation coefficients. Those fixed computations are independent of $n$, so they impose no additional input-period payment.

For $M=33,L=72$, the operative window remains $620$, while $E=37$. Consequently, conditional on the local theorem, the actual top coefficient jet modulo $3^{32}$ is frozen on


$$
\boxed{j=84645+3^{36}t,\qquad t\ge0.}
$$


The separate real Range-III admission uses the already-paid irrational-rotation argument. The base $j=84645$ is not asserted to satisfy that real window.

### Global status

Neither audit determines the rationality or irrationality of $e+\pi$. Neither evaluates the requested actual return $\eta$, $N_{00}/3^{29}$, the full physical-seven return, an actual all-prime primitive denominator, or the whole primitive error.

---

## 2. Original objects and normalization retained throughout

### 2.1 The compact determinant producer

The original infinite domain is


$$
\mathcal K=\{K_u:u\ge0\},
\qquad
K_u=9^{18+32u}=3^{36+64u}.
$$



Retain


$$
a_0=1,\qquad a_n=1-na_{n-1},
$$




$$
u_n=a_{2n},\qquad w_n=(-1)^n,\qquad c_n=u_n-w_n,
$$


and


$$
\rho_0=0,\qquad \rho_{n+1}+\rho_n=\frac1{2n+1},
\qquad r_n=-(2n)!+4\rho_n.
$$


The complete returns are


$$
\sigma_n=c_{n+1}+c_n=u_{n+1}+u_n
$$


and


$$
\tau_n=r_{n+1}+r_n
=-(2n+2)!-(2n)!+\frac4{2n+1}.
$$



For fixed $k$, put


$$
\Lambda_k=\operatorname{lcm}(1,3,\ldots,6k-5),
\qquad T_n=\Lambda_k\tau_n.
$$


Thus


$$
T_n=-\Lambda_k\bigl((2n+2)!+(2n)!\bigr)
+\frac{4\Lambda_k}{2n+1}.
$$



The original determinant is


$$
H_k(s)=
\det\left[
(c_{m+j})_{j<k}\ \middle|\
\bigl(\Lambda_k(r_{m+j}+s(-1)^{m+j})\bigr)_{j<k}
\right]_{m<2k}
=H_{0,k}+H_{1,k}s.
$$


Its unchanged physical limits are


$$
\boxed{
\text{last row }2k-1,\quad
\text{last moment }3k-2,\quad
\text{last factorial }(6k-4)!,\quad
\text{last odd denominator }6k-5.
}
$$



The established individual original right-column entry clearers are


$$
\Lambda_{k,j}
=\operatorname{lcm}(1,3,\ldots,4k+2j-3),
\qquad 0\le j<k,
$$


and the common least entry clearer of the complete unprojected right block is $\Lambda_k$.

The final content is


$$
G_k=\gcd(|H_{0,k}|,|H_{1,k}|),
$$


with **all primes included**. If


$$
d_{H,k}=\gcd(\Lambda_k^k,H_{0,k},H_{1,k}),
$$


then the least simultaneous coefficient clearer of $H_k/\Lambda_k^k$, and the content after that clearing, are exactly


$$
\boxed{\frac{\Lambda_k^k}{d_{H,k}},\qquad \frac{G_k}{d_{H,k}}.}
$$


These formulas follow prime by prime: if $N=v_p(\Lambda_k^k)$ and
$g=\min(v_p(H_{0,k}),v_p(H_{1,k}))$, the required clearing exponent is
$\max(0,N-g)$, and the resulting content exponent is $\max(0,g-N)$.

No auxiliary Schur clearer below is substituted for this actual least clearer.

The accepted sign and nonvanishing results give, at every original index,


$$
q_k=\frac{|H_{1,k}|}{G_k}>0,\qquad
p_k=-\frac{(-1)^kH_{0,k}}{G_k},
$$


and


$$
\boxed{
\ell_k=q_k(e+\pi)-p_k
=\frac{(-1)^kH_k(e+\pi)}{G_k}
=\frac{|H_k(e+\pi)|}{G_k}>0.
}
$$


The quantity requiring control is $\ell_k$, not merely $\ell_k/q_k$.

### 2.2 Contents reused without reopening their audits

The actual rectangles remain


$$
Z_k=
\left[
(c_{m+j})_{\substack{m<2k\\j<k}}
\ \middle|\
(T_{m+j})_{\substack{m<2k\\j<k-1}}
\right],
$$




$$
Y_k=
\left[
(\sigma_{m+j})_{\substack{m<2k-1\\j<k}}
\ \middle|\
(T_{m+j})_{\substack{m<2k-1\\j<k}}
\right].
$$


Let


$$
\mathscr R_k=\delta_{2k-1}(Z_k),\qquad
\mathscr L_k=\delta_{2k-1}(Y_k).
$$


The established interface is


$$
\operatorname{lcm}(\mathscr L_k,\mathscr R_k)
\mid G_k\mid \Lambda_k\mathscr L_k\mathscr R_k.
$$



The accepted exact ternary result is reused:


$$
v_3(\mathscr L_k)=v_3(\mathscr R_k)=E_k,
\qquad
E_k=\frac{(k-2)(k-1-2s)}2,
\quad k=3^s\in\mathcal K.
$$


It gives only


$$
\boxed{E_k\le v_3(G_k)\le 2E_k+s+1,}
$$


not an equality for $v_3(G_k)$.

The earlier exact-three content audit and canonical signed Hermite-return audit are not repeated here.

---

# Part I. Full audit of the dyadic reduction

## 3. Literal finite row operator and complete rational cancellation

Let $k\ge9$ be odd and set


$$
d=k-1.
$$


Then $d\ge8$ is even. Define


$$
P_d(x)=\prod_{h=0}^{d-1}(2x+2h+1)
$$


and


$$
(\mathcal A_d y)_n
=\sum_{i=0}^d(-1)^i\binom di P_d(n+i)y_{n+i}.
$$



On the original $2d+2$ rows, transform only rows $0,\ldots,d-1$ by this formula and leave rows $d,\ldots,2d+1$ unchanged. The resulting row matrix $\mathcal S_d$ is upper triangular. Its first $d$ diagonal entries are $P_d(n)$, and all remaining diagonal entries are $1$. Therefore


$$
\boxed{
\det\mathcal S_d=\Omega_k
=\prod_{n=0}^{d-1}P_d(n),
}
$$


which is positive and odd.

This is an exact integer determinant factor. The operation is invertible over $\mathbb Z_2$, but is not generally unimodular over $\mathbb Z$.

The greatest row index used by a transformed row is


$$
(d-1)+d=2d-1.
$$


Thus neither of the final two original rows is used as an invented continuation, and the final row $2d+1=2k-1$ remains literally unchanged.

For each common return shift $0\le j<d$,


$$
\frac{P_d(n+i)}{2(n+i+j)+1}
=
\prod_{\substack{0\le h<d\\h\ne j}}
(2(n+i+h)+1)
$$


is a polynomial in $i$ of degree $d-1$. Consequently,


$$
\sum_{i=0}^d(-1)^i\binom di
\frac{P_d(n+i)}{2(n+i+j)+1}=0.
$$


This proves cancellation for **every one** of the $d$ common return columns.

Now


$$
(2t+2)!+(2t)!
=\bigl((2t+2)(2t+1)+1\bigr)(2t)!
=b(t)(2t)!,
$$


where


$$
b(t)=4t^2+6t+3
$$


is odd. Hence


$$
\boxed{
(\mathcal A_dT_{\bullet+j})_n
=-\Lambda_k\sum_{i=0}^d(-1)^i\binom di
P_d(n+i)b(n+i+j)(2(n+i+j))!.
}
$$


The rational channel has disappeared by an exact identity. Both factorial terms are present in $b(t)(2t)!$.

This annihilation is not asserted for the remaining border $\Lambda_kr$; that complete border is retained later.

---

## 4. Exact forcing-entry valuation and the normalized Pascal pivot

### 4.1 Entry valuation

In the last sum, the $i=0$ term has valuation


$$
v_2((2(n+j))!),
$$


since $\Lambda_k$, $P_d(n)$, and $b(n+j)$ are odd.

For $i\ge1$,


$$
\frac{(2(n+i+j))!}{(2(n+j))!}
$$


is even. The binomial coefficient is integral, so every such term has strictly greater binary valuation than the $i=0$ term. Therefore


$$
\boxed{
v_2\bigl((\mathcal A_dT_{\bullet+j})_n\bigr)
=v_2((2(n+j))!).
}
$$



### 4.2 Integral factorial normalization

Let


$$
F_k(n,j)=(\mathcal A_dT_{\bullet+j})_n,
\qquad 0\le n,j<d,
$$


and


$$
D_f=\operatorname{diag}((2n)!)_{0\le n<d}.
$$


Define


$$
K_d(n,j)=
\sum_{i=0}^d(-1)^i\binom diP_d(n+i)b(n+i+j)
\frac{(2(n+i+j))!}{(2n)!(2j)!}.
$$


Each summand is integral because


$$
\frac{(2(n+i+j))!}{(2n)!(2j)!}
=
\frac{(2(n+i))!}{(2n)!}
\binom{2(n+i+j)}{2j}.
$$


Thus


$$
\boxed{F_k=-\Lambda_kD_fK_dD_f.}
$$



Modulo $2$, the $i\ge1$ summands vanish because the first factorial quotient in the preceding factorization is even. The remaining term gives


$$
K_d(n,j)\equiv \binom{2(n+j)}{2j}
\equiv \binom{n+j}{j}\pmod2.
$$


The second congruence follows by comparing coefficients in


$$
(1+x)^{2(n+j)}\equiv(1+x^2)^{n+j}\pmod2.
$$



For an independent determinant check, let


$$
C(n,j)=\binom{n+j}{j}.
$$


Apply the unit lower-triangular forward-difference matrix to its rows. The resulting entry in row $r$, column $j$, is


$$
\Delta_n^r\binom{n+j}{j}\bigg|_{n=0}
=\binom jr.
$$


This is an upper-triangular matrix with diagonal $1$. Hence


$$
\det C=1.
$$


Therefore


$$
\boxed{\eta_d:=\det K_d\equiv1\pmod2.}
$$



It follows that $F_k$ is nonsingular and


$$
f_k:=\det F_k
=(-\Lambda_k)^d\eta_d
\left(\prod_{n=0}^{d-1}(2n)!\right)^2,
$$


so


$$
\boxed{
v_2(f_k)=V_d:=2\sum_{n=0}^{d-1}v_2((2n)!).
}
$$



All odd factors, including the generally unknown odd integer $\eta_d$, remain in the exact determinant formula.

---

## 5. Contact divisibility and the literal atom

### 5.1 Finite-difference divisibilities

The moment representation


$$
u_n=\int_0^\infty e^{-t}(t-1)^{2n}\,dt
$$


is consistent with the original recurrence. It gives


$$
\Delta^ru_n
=\int_0^\infty e^{-t}(t-1)^{2n}t^r(t-2)^r\,dt.
$$



Expand $t^r(t-2)^r$ and then $(t-1)^{2n}$. A typical factorial term contains


$$
\binom rh2^{r-h}(r+h+a)!,
\qquad a\ge0.
$$


Its divisibility by $2^rr!$ follows from


$$
\frac{\binom rh2^{r-h}(r+h)!}{2^rr!}
=
\binom{r+h}{2h}(2h-1)!!\in\mathbb Z
$$


and from the integrality of $(r+h+a)!/(r+h)!$. Thus


$$
2^rr!\mid\Delta^ru_n.
$$


Since $\sigma=2u+\Delta u$,


$$
2^{r+1}r!\mid\Delta^r\sigma_n.
$$



For $0\le h\le d$,


$$
\Delta^hP_d(n)
=
2^h\frac{d!}{(d-h)!}
\prod_{r=h}^{d-1}(2n+2r+1).
$$


The finite-difference product rule


$$
\Delta^d(Py)_n
=
\sum_{h=0}^d\binom dh
(\Delta^hP)_n(\Delta^{d-h}y)_{n+h}
$$


therefore proves


$$
\boxed{
2^dd!\mid(\mathcal A_du_{\bullet+j})_n,
\qquad
2^{d+1}d!\mid(\mathcal A_d\sigma_{\bullet+j})_n.
}
$$


The possible overall sign between $\mathcal A_d$ and $\Delta^d$ is immaterial; here $d$ is even.

Put


$$
\alpha_d=v_2((2d)!)=d+v_2(d!).
$$


The two transformed-column valuations are at least $\alpha_d$ and $\alpha_d+1$, respectively.

### 5.2 Exact atom valuation

For the literal atom $w_n=(-1)^n$,


$$
(\mathcal A_dw)_n
=(-1)^n\sum_{i=0}^d\binom diP_d(n+i).
$$


Writing $E=1+\Delta$,


$$
\sum_{i=0}^d\binom diP_d(n+i)
=(1+E)^dP_d(n)=(2+\Delta)^dP_d(n).
$$


Hence


$$
(\mathcal A_dw)_n=(-1)^n2^dU_d(n),
$$


where


$$
U_d(n)=
\sum_{h=0}^d
\binom dh\frac{d!}{(d-h)!}
\prod_{r=h}^{d-1}(2n+2r+1).
$$



The $h=0$ term is odd. Every $h\ge1$ term contains the even factor $d$. Therefore


$$
U_d(n)\equiv1\pmod2
$$


and


$$
\boxed{v_2((\mathcal A_dw)_n)=d.}
$$



Because $d!$ is even,


$$
v_2((\mathcal A_du)_n)\ge d+v_2(d!)>d.
$$


Using the actual relation $c=u-w$, we obtain


$$
\boxed{v_2((\mathcal A_dc)_n)=d.}
$$



This verifies the source’s essential atom payment. Replacing $c$ by $u$ would destroy this exact valuation.

---

## 6. Complete common-column form and explicit corrected blocks

Perform the adjacent-column transformations in each original column group, using the original adjacent columns, equivalently processing from right to left:


$$
(c_0,\ldots,c_d)\longmapsto(c_0,\sigma_0,\ldots,\sigma_{d-1}),
$$




$$
(\Lambda_k(r_0+sw),\ldots)
\longmapsto
(\Lambda_k(r_0+sw),T_0,\ldots,T_{d-1}).
$$


Both transformations have determinant $1$. The parameter cancels exactly in the common return columns.

Moving the $d$ return columns to the front contributes


$$
(-1)^{d(d+2)}=1.
$$


Thus


$$
H_k(s)=\det[\mathcal T\mid\mathcal M(s)],
$$


where


$$
\mathcal T(m,j)=T_{m+j}
$$


and


$$
\mathcal M(s)
=
\left[
c_m\ \middle|\ (\sigma_{m+j})_{j<d}\ \middle|\
\Lambda_k(r_m+sw_m)
\right]_{m<2d+2}.
$$



After applying $\mathcal S_d$,


$$
\mathcal S_d[\mathcal T\mid\mathcal M(s)]
=
\begin{pmatrix}
F_k&A_0+sA_1\\
B&C_0+sC_1
\end{pmatrix}.
$$



For complete specificity, if $0\le n<d$, $0\le r<d+2$, and $m=d+r$, these blocks are


$$
A_0(n,:)=
\left[
(\mathcal A_dc)_n,\
((\mathcal A_d\sigma_{\bullet+j})_n)_{j<d},\
(\mathcal A_d(\Lambda_kr))_n
\right],
$$




$$
A_1(n,:)=
\left[0,\ldots,0,\Lambda_k(\mathcal A_dw)_n\right],
$$




$$
B(r,j)=T_{m+j},
$$




$$
C_0(r,:)=
\left[c_m,\ (\sigma_{m+j})_{j<d},\ \Lambda_kr_m\right],
$$




$$
C_1(r,:)=
\left[0,\ldots,0,\Lambda_kw_m\right].
$$



These definitions retain the full constant border, including $-\Lambda_k(2m)!$ and $4\Lambda_k\rho_m$. Only the last column depends on $s$.

---

## 7. Exact Schur clearer and every column division

### 7.1 Adjugate clearer

Set


$$
h_d=(2d-2)!,\qquad \beta_d=v_2(h_d),
$$




$$
\widehat D_f=h_dD_f^{-1},
$$




$$
N_d=\widehat D_f\,\operatorname{adj}(K_d)\,\widehat D_f,
\qquad
\delta_k=\Lambda_k\eta_dh_d^2.
$$


The matrix $\widehat D_f$ is integral, because every $(2n)!$, $n<d$, divides $h_d$. Thus $N_d$ is integral.

Direct inversion of $F_k=-\Lambda_kD_fK_dD_f$ gives


$$
\boxed{F_k^{-1}=-\frac{N_d}{\delta_k}.}
$$


In particular,


$$
v_2(\delta_k)=2\beta_d.
$$


This is an explicit valid clearer, not a claim of leastness.

Define


$$
E_i=\delta_kC_i+BN_dA_i,\qquad i=0,1.
$$


The Schur identity then gives


$$
\Omega_kH_k(s)
=f_k\det\left(C_0+sC_1+\frac{BN_d(A_0+sA_1)}{\delta_k}\right),
$$


hence


$$
\boxed{
\delta_k^{\,d+2}\Omega_kH_k(s)
=f_k\det(E_0+sE_1).
}
$$



### 7.2 Bottom-block divisibilities

All bottom row indices satisfy $m\ge d\ge8$.

First, $4\mid B(r,j)$. Indeed, both factorials in $T_{m+j}$ are divisible by $4$, and


$$
4\Lambda_k/(2(m+j)+1)
$$


is an integer multiple of $4$.

Second, every $u_m$ is odd, by the original recurrence at an even index. Hence $c_m=u_m-w_m$ and $\sigma_m=u_{m+1}+u_m$ are even.

Third, $\Lambda_k\rho_m$ is integral at every row used here: unrolling its recurrence uses odd denominators at most $2m-1\le4k-3\le6k-5$. Since $m\ge8$,


$$
4\mid\Lambda_kr_m.
$$



The lower affine coefficient $\Lambda_kw_m$, however, is odd. It must be paid through $\delta_k$; it cannot be grouped with the constant border’s divisibility.

### 7.3 Required inequalities

The exact factorial relation is


$$
\alpha_d=\beta_d+1+v_2(d).
$$


Also,


$$
\beta_d\ge d-1\ge v_2(d)+3\qquad(d\ge8,\ d\ \text{even}),
$$


so


$$
\boxed{2\beta_d+1\ge\alpha_d+3.}
$$


Since $\alpha_d\ge d$, this also implies


$$
2\beta_d+1\ge d+2.
$$



The following table records the actual payments.

| Column | Lower bound from $\delta_kC_i$ | Lower bound from $BN_dA_i$ | Valid division |
|---|---:|---:|---:|
| First contact column | $2\beta_d+1$ | $d+2$ | $2^{d+2}$ |
| Each $\sigma$-column | $2\beta_d+1$ | $\alpha_d+3$ | $2^{\alpha_d+3}$ |
| Constant border | $2\beta_d+2$ | $2$ | $4$ |
| Linear border | $2\beta_d$ | at least $2$ | $4$ |

For the linear border, $2\beta_d\ge2$, and $4\mid B$ supplies the second term’s payment. Thus the same border division is valid simultaneously for $E_0$ and $E_1$.

After these column divisions, let the resulting integer pencil be $\widehat E_k(s)$, and write


$$
\det\widehat E_k(s)=J_{0,k}+J_{1,k}s.
$$


It is affine because only its last column depends on $s$.

The total removed binary factor is


$$
\lambda_d=(d+2)+d(\alpha_d+3)+2
=d\alpha_d+4d+4.
$$


Therefore


$$
\boxed{
\delta_k^{\,k+1}\Omega_kH_{i,k}
=f_k\,2^{\lambda_d}J_{i,k},
\qquad i=0,1.
}
$$



Every row, factorial, scalar, and column division has now been accounted for.

---

## 8. All-prime gcd identity, binary offset, and primitive normalization

Define the actual residual content


$$
g_k^\sharp=\gcd(|J_{0,k}|,|J_{1,k}|).
$$


Taking gcds of the two coefficient identities gives


$$
\boxed{
|\delta_k|^{\,k+1}\Omega_kG_k
=|f_k|\,2^{\lambda_d}g_k^\sharp.
}
$$


This is an identity at **all primes**. In particular, it retains the odd factors in $\Omega_k$, $\Lambda_k$, $\eta_d$, and the factorials.

At $2$,


$$
\boxed{
v_2(G_k)=\kappa_k+v_2(g_k^\sharp),
\qquad
\kappa_k=V_d+\lambda_d-2(d+2)\beta_d.
}
$$



Let


$$
S_2(d)=\sum_{n=0}^{d-1}s_2(n).
$$


Legendre’s formula gives


$$
V_d=2d(d-1)-2S_2(d),
$$




$$
\alpha_d=2d-s_2(d),\qquad
\beta_d=2d-2-s_2(d-1).
$$


Substitution first yields the useful general identity


$$
\kappa_k
=-2d+12-ds_2(d)+2(d+2)s_2(d-1)-2S_2(d).
$$


Using


$$
s_2(d-1)=s_2(d)-1+v_2(d),
$$


this becomes


$$
\boxed{
\kappa_k
=-4d+8+(d+4)s_2(d)+2(d+2)v_2(d)-2S_2(d).
}
$$


In particular, $\kappa_k=O(k\log k)$.

### Original-domain simplification

For $k\in\mathcal K$,


$$
k=81^{\,9+16u}.
$$


The exponent is odd, and $81=1+80$. In the binomial expansion of $k-1$, the first term has valuation $4$, while every later term has valuation at least $8$. Hence


$$
v_2(k-1)=4.
$$


Thus $v_2(d)=4$ and


$$
\boxed{
\kappa_k
=4d+24+(d+4)s_2(d)-2\sum_{n=0}^{d-1}s_2(n),
\qquad d=k-1,\quad k\in\mathcal K.
}
$$


This agrees with A2’s formula.

### Primitive normalization is unchanged

The two coefficient pairs are nonzero rational scalar multiples of one another. After their respective full gcds are removed,


$$
\boxed{
\frac{|J_{1,k}|}{g_k^\sharp}
=\frac{|H_{1,k}|}{G_k}=q_k,
}
$$


and


$$
\boxed{
\frac{|J_{0,k}+J_{1,k}(e+\pi)|}{g_k^\sharp}
=\frac{|H_k(e+\pi)|}{G_k}=\ell_k.
}
$$


Thus the reduction changes neither the actual primitive denominator nor the whole evaluated error.

### Boundary check

The largest bottom return index is


$$
(2d+1)+(d-1)=3d=3k-3.
$$


Its successor moment is $3k-2$, its upper factorial is $(6k-4)!$, and its odd denominator is $6k-5$.

The last row $2k-1$, all $d$ common return columns, and the complete remaining right border are present. No physical endpoint was replaced by the smaller forcing-pivot endpoint.

**Final first-primary verdict: PASS.**

---

## 9. What remains unpaid, and the sharp conditional retirement statement

The exact residual binary quantity is


$$
v_2(g_k^\sharp)
=\min\bigl(v_2(J_{0,k}),v_2(J_{1,k})\bigr).
$$


Oddness of $\det K_d$ establishes the normalized forcing pivot, not this residual pair. The corrected contact and border columns occur through


$$
E_i=\delta_kC_i+BN_dA_i,
$$


and their simultaneous determinant cancellation is not controlled by the pivot’s unit property.

That is the precise obstruction to promoting the audited reduction into a binary upper bound.

### 9.1 Reuse of the accepted analytic lower bound

Only the already-passed first spread gain is used:


$$
\log|H_k(e+\pi)|
\ge
4k^2\log k+
\left(15\log2-\frac92\log3+\frac4{85}\right)k^2
+o(k^2).
$$


The later pairwise-convexity improvement is not audited or used here.

### 9.2 Exact ternary saving in the conditional odd height

Let


$$
W_k^{\mathrm{odd}}
=
3^{2k}\Lambda_k^k
\left(\prod_{j=0}^{k-1}\operatorname{odd}(j!)\right)^4.
$$


For odd $p$, write


$$
B_p(k)=
k\bigl(2\mathbf1_{p=3}+v_p(\Lambda_k)\bigr)
+4\sum_{j=0}^{k-1}v_p(j!).
$$



Assume, on an eventual tail of the original domain, that for **every odd prime $p\ne3$**


$$
v_p(\mathscr L_k)\le B_p(k),
\qquad
v_p(\mathscr R_k)\le B_p(k).
$$


This includes primes $p>6k-5$, where the required allowance is zero.

The exact ternary result permits the replacement


$$
W_{k,\mathrm{sharp}}^{\mathrm{odd}}
=
\frac{W_k^{\mathrm{odd}}}{3^{B_3(k)-E_k}},
$$


where the reused exact excess is


$$
2(B_3(k)-E_k)=k^2+7k-2-4s.
$$


Thus


$$
\operatorname{odd}(G_k)
\mid
\Lambda_k\bigl(W_{k,\mathrm{sharp}}^{\mathrm{odd}}\bigr)^2.
$$


This is a conditional allowance bound, not a replacement for an actual content or clearer.

Using the established height of $W_k^{\mathrm{odd}}$, a further hypothesis


$$
v_2(G_k)\le Ak^2+o(k^2)
$$


gives


$$
\log G_k
\le
4k^2\log k+
\bigl(A\log2+6-4\log2-\log3\bigr)k^2+o(k^2).
$$


Therefore


$$
\boxed{
\log\ell_k
\ge
\left((19-A)\log2-\frac72\log3-\frac{506}{85}\right)k^2
+o(k^2).
}
$$



The sufficient threshold is


$$
A<A_*+\frac{\log3}{\log2}
\approx4.86435253348.
$$


For $A=19/4$, the margin is


$$
\delta_{19/4}
=\frac{57}{4}\log2-\frac72\log3-\frac{506}{85}
\approx0.07926313617>0.
$$


For example, the supplied logarithm brackets imply the coarser inequalities


$$
\log2>0.69314,\qquad \log3<1.09862,
$$


which already give the exact positive lower bound


$$
\delta_{19/4}>
\frac{269055}{3400000}>0.
$$



### 9.3 Concrete follow-on lemma

The sufficient binary obligation is now appropriately stated as follows.

> **Paid paired-valuation lemma — open.**  
> For the exact integer pencil $\widehat E_k(s)$ constructed in Sections 6–7, there exist constants $C$ and $u_0$ such that, for every $u\ge u_0$ and $k=9^{18+32u}$,
> 

$$
> \min\bigl(v_2(J_{0,k}),v_2(J_{1,k})\bigr)
> \le \frac{19}{4}k^2+Ck\log k.
>
$$



Together with the audited $\kappa_k=O(k\log k)$, this would give the required direct binary upper bound. Combined with the still-open other-odd-prime descents, it would imply


$$
\ell_k\longrightarrow+\infty
$$


along the same original domain.

This would retire this particular producer as a source of primitive whole-error decay. It would not decide whether $e+\pi$ is rational or irrational.

---

# Part II. Audit of the degree-controlled source-input period

## 10. Exact conditional hypotheses and original local producer

This part does not duplicate the full precision-local proof or its complete implementation audit, assigned separately to A4. It checks the new period implication conditional on that theorem.

To avoid confusion with the preceding return sequence $T_m$, write the ternary forcing matrix as $\mathsf T_n$:


$$
\mathsf T_n[a,b]=\binom{a+b}{a}\gamma_{a+b},
\qquad 0\le a,b<n,
$$


where


$$
\gamma_0=1,\qquad \gamma_1=0,\qquad
\gamma_{r+1}=(4r+2)\gamma_r+4\gamma_{r-1}.
$$


The original indices are


$$
n=4^j+1,\qquad j\equiv84645\pmod{3^{12}},
$$


with the separately retained real and integer admissibility conditions.

Let


$$
F_{\mathrm{fac}}=(n-1)!,
\qquad
u_a=\frac{F_{\mathrm{fac}}(-2)^a}{a!},
$$




$$
v=\mathsf T_n^{-1}u,
\qquad
k_a=\binom{n+a}{a}\gamma_{n+a},
\qquad
h=\mathsf T_n^{-1}k.
$$


The complete force is


$$
t=3nh+(b_{\mathrm{force}}+6)e_{n-1}
+\frac{2b_{\mathrm{force}}}{n-1}e_{n-2},
\qquad b_{\mathrm{force}}=-n-66.
$$



The reused scalar theorem, valid for every $n\ge5$, $n\equiv2\pmod3$, gives


$$
\Xi=F_{\mathrm{fac}}^2-u^T\mathsf T_n^{-1}u,
\qquad
\chi=u^Tt,
$$




$$
\Xi\equiv\chi\equiv3\pmod9,
\qquad
v_3(\Xi)=v_3(\chi)=1.
$$


Thus $\xi=\chi/\Xi$ is a ternary unit.

The complete-force contraction is


$$
\chi=3n\,u^Th+6u_{n-1}.
$$


Indeed,


$$
u_{n-2}=-\frac{n-1}{2}u_{n-1},
$$


so the two original affine force terms contribute


$$
(b_{\mathrm{force}}+6)u_{n-1}
+\frac{2b_{\mathrm{force}}}{n-1}u_{n-2}
=6u_{n-1}.
$$


This scalar cancellation does not authorize dropping either term from an individual $q$-coefficient.

The complete coefficient formula remains


$$
\boxed{
q_a=-\frac{F_{\mathrm{fac}}}{a!}
\left(
3nh_a+(b_{\mathrm{force}}+6)\delta_{a,n-1}
+\frac{2b_{\mathrm{force}}}{n-1}\delta_{a,n-2}
+\xi v_a
\right).
}
$$



The full precision-local theorem is assumed to supply:

1. the literal finite Pascal transform and its entry formula;
2. the weighted finite inverse locality law;
3. the aligned end window, with the actual last block;
4. the complete transformed $u$ and next-column force;
5. the exact top reconstruction formulas;
6. the stated support and factorial precision payments.

The old scalar theorem is established reuse, not a new conditional unit assertion.

---

## 11. Classical binomial period and the actual source degree

Fix


$$
M\ge4,\qquad 1\le L\le3M,\qquad H_{\deg}=6M-1,
$$


and set


$$
E=M+\lfloor\log_3H_{\deg}\rfloor.
$$



### 11.1 Sufficient-period lemma

For integers $a$, $h\ge1$, and $E>\lfloor\log_3h\rfloor$, Vandermonde gives


$$
\binom{a+3^E}{h}-\binom ah
=
\sum_{i=1}^h\binom{3^E}{i}\binom{a}{h-i}.
$$


For $1\le i\le h<3^E$,


$$
\binom{3^E}{i}
=\frac{3^E}{i}\binom{3^E-1}{i-1},
$$


so


$$
v_3\binom{3^E}{i}
\ge E-v_3(i)
\ge E-\lfloor\log_3h\rfloor.
$$


Generalized binomial coefficients with integer upper argument are integers. Therefore


$$
\binom{a+3^E}{h}\equiv\binom ah
\pmod{3^{E-\lfloor\log_3h\rfloor}}.
$$


For $h=0$, equality is exact. Repeated positive or negative shifts give the same conclusion whenever two upper arguments differ by a multiple of $3^E$.

Consequently, the selected $E$ determines


$$
\binom{n+c}{h}\pmod{3^M}
$$


for every fixed integer offset $c$ and every $0\le h\le H_{\deg}$.

The size of the offset $c$ incurs no additional payment.

### 11.2 Why the transformed entries really have that degree

The conditional local theorem gives, modulo $3^M$,


$$
\widehat{\mathsf T}[a,b]
=
\sum_{h=0}^{H_{\deg}}g_h
\sum_{\substack{p,q,c\ge0\\p+q+c=h\\p-q=a-b}}
\frac{h!}{p!q!c!}2^c\binom{a+q}{h},
$$


where the $g_h$ depend only on the fixed $\gamma$-recurrence.

For a fixed diagonal difference $\delta=a-b$, use


$$
\binom{a+q}{h}
=\sum_{s=0}^h\binom as\binom q{h-s}.
$$


This writes the diagonal entry as


$$
\widehat{\mathsf T}[a,a-\delta]
\equiv
\sum_{s=0}^{H_{\deg}}C_{\delta,s}\binom as
\pmod{3^M},
$$


with integer coefficients


$$
C_{\delta,s}
=
\sum_{h=s}^{H_{\deg}}g_h
\sum_{\substack{p+q+c=h\\p-q=\delta}}
\frac{h!}{p!q!c!}2^c\binom q{h-s}.
$$


These coefficients are independent of $n$.

This also validates the Newton-polynomial interpretation of the supplied implementation. Its zero extension for $a-\delta<0$ is compatible with the formula: when $0\le a<\delta$, every contributing term has


$$
h=\delta+2q+c>a+q,
$$


so $\binom{a+q}{h}=0$.

Thus every $n$-dependent transformed matrix entry uses only


$$
\binom{a}{s},\qquad s\le H_{\deg}.
$$



For the end window, $a=n-R+i$. Its matrix diagonal differences are $i-j$. The transformed next-column force has difference


$$
(n-R+i)-n=i-R.
$$


Both are fixed under a change of $n$ preserving the window type. The same degree payment therefore covers the complete matrix and the complete transformed next-column force.

### Wording qualification

The small interpolation construction uses $\gamma$-values through $3H_{\deg}$, and builds fixed Pascal tables extending beyond lower index $H_{\deg}$. These are independent of $n$.

Accordingly, the precise statement is:

> Every binomial evaluation carrying the physical input $n$, after the conditional finite local reduction, has lower index at most $6M-1$.

A literal assertion about every binomial table entry in the entire implementation would be false, but is unnecessary for the period theorem.

---

## 12. Window type, inverse, force products, and reconstruction

### 12.1 The same finite window and actual last block

The conditional theorem uses a window length at least


$$
R_0=\max\{L,6M\}+13(M-1)+4,
$$


rounded upward by at most $2$ so that $n-R$ is a multiple of $3$. Since $L\le3M$,


$$
R_0=19M-9.
$$



If $n'\equiv n\pmod{3^E}$, then $n'\equiv n\pmod3$. Hence $R$, the left-edge alignment, and the final block type are unchanged.

The entry-period proof shows that the two complete $R\times R$ matrices are equal modulo $3^M$, not merely that their reductions modulo $3$ have the same block type.

For the original $n\equiv2\pmod3$, the final block is the actual $B_2$, not an invented full $B_3$. In particular,


$$
B_2=
\begin{pmatrix}1&2\\2&0\end{pmatrix},
\qquad
B_2^{-1}\equiv
\begin{pmatrix}0&2\\2&2\end{pmatrix}\pmod3.
$$


The complete local matrix is a ternary unit matrix under the conditional theorem. If $A'\equiv A\pmod{3^M}$, then


$$
A'^{-1}-A^{-1}=A'^{-1}(A-A')A^{-1}
\equiv0\pmod{3^M}.
$$


Thus the local inverse is determined at the same precision, with no extra scalar division.

This argument preserves the actual finite size and boundary. It does not replace the original dimension $n$ by its residue.

### 12.2 Complete raw force products

For $1\le r\le3M$,


$$
u_{n-r}
=\left(\prod_{j=1}^{r-1}(n-j)\right)(-2)^{n-r}.
$$


The finite product is an integer polynomial in $n$, so $n\bmod3^M$ determines it modulo $3^M$.

For the power, $ -2=1-3$. If


$$
v_3(z-1)=a\ge1,
$$


then


$$
v_3(z^3-1)=a+1,
$$


because $z^2+z+1$ has valuation exactly $1$. Induction gives


$$
v_3\bigl((-2)^{3^s}-1\bigr)=s+1.
$$


Hence $(-2)^a\bmod3^M$ has exponent period dividing $3^{M-1}$. Since $E\ge M$, the complete force factor is unchanged.

Coordinates deeper than the last $3M$ are omitted only through the conditional theorem’s support payment. Indeed, their factorial quotients contain at least $3M$ consecutive integers and hence at least $M$ factors divisible by $3$.

### 12.3 Every required top Pascal coefficient

Put


$$
L'=\max(L,3M)=3M.
$$


The relevant dependencies are:

| Operation | $n$-dependent binomial | Largest lower index |
|---|---|---:|
| Transformed matrix and next column | $\binom{n-R+i}{s}$ | $6M-1$ |
| $u\mapsto\widehat u$ on its end support | $\binom{n-R+b}{b-i}$ | $3M-1$ |
| Top $v,h$ reconstruction | $\binom{n-R+b}{b-i}$ | $L'-1=3M-1$ |
| Dense known part of $h_{n-r}$ | $\binom nr$ | $L'=3M$ |

All these lower indices are at most $6M-1$.

The dense known part merits an explicit check. The finite embedding gives


$$
h=P_n^{-T}r+P_n^{-T}\widehat{\mathsf T}_n^{-1}\widehat k,
\qquad r_b=\binom nb.
$$


For $a=n-r$,


$$
(P_n^{-T}r)_a
=\sum_{b=a}^{n-1}(-1)^{b-a}\binom ba\binom nb
=(-1)^{r-1}\binom nr.
$$


The sign depends on the offset $r$, not on a separately chosen parity representative for $n$.

This pays all last-$3M$ coordinates needed for $\chi$, even if the requested coefficient length $L$ is smaller.

---

## 13. Scalars, affine constants, and monic source quotient

### 13.1 Complete scalar contractions and division by $3$

The preceding steps determine, modulo $3^M$,

- $\widehat u$;
- both local solved vectors;
- all needed raw $v$ and $h$;
- the complete contractions
  

$$
\Xi=F_{\mathrm{fac}}^2-\widehat u^T
  \widehat{\mathsf T}_n^{-1}\widehat u,
$$


  

$$
\chi=3n\,u^Th+6u_{n-1}.
$$



The factorial term $F_{\mathrm{fac}}^2$ is zero **at this precision**, under the original size hypothesis. It is not set equal to zero as an integer or rational quantity.

Since the reused theorem gives $v_3(\Xi)=v_3(\chi)=1$, knowledge modulo $3^M$ gives


$$
\Xi/3,\ \chi/3\pmod{3^{M-1}}.
$$


The first is a unit. Thus


$$
\boxed{
\xi=\frac{\chi/3}{\Xi/3}\pmod{3^{M-1}}
}
$$


is determined with exactly one digit of precision loss, already budgeted.

No residual parameter $\chi_{\mathrm{range}}$ is involved in this scalar calculation.

### 13.2 Both original affine constants

For $a=n-r$, the original coefficient is


$$
q_{n-r}
=
-\left(\prod_{j=1}^{r-1}(n-j)\right)
\left[
3nh_{n-r}
+(-n-66+6)\mathbf1_{r=1}
+\frac{2(-n-66)}{n-1}\mathbf1_{r=2}
+\xi v_{n-r}
\right].
$$


Every displayed ingredient is determined modulo $3^{M-1}$. Moreover,


$$
n-1\equiv1\pmod3,
$$


so its inverse is a unit inverse and causes no further precision loss.

Both affine constants remain. Their earlier cancellation inside $u^Tt$ is not used to remove either one here.

Therefore all $L$ requested top coefficients are determined modulo $3^{M-1}$.

### 13.3 Monic quotient and remainder

Define the normalized top polynomial


$$
Q_{n,L}(x)=\sum_{b=0}^{L-1}q_{n-L+b}x^b.
$$


Over any coefficient ring, monic division gives


$$
Q_{n,L}(x)=(x+2)V_{n,L}(x)+Q_{n,L}(-2),
$$


where


$$
V_{n,L}(x)=\sum_{b=0}^{L-2}v_bx^b,
$$




$$
v_b=\sum_{r=b+1}^{L-1}(-2)^{r-b-1}q_{n-L+r}.
$$


These are integer-linear combinations of the top coefficients. Thus both quotient and remainder have the same period modulo $3^{M-1}$, without an additional division.

For arbitrary $L$, this statement does not assert that the remainder is zero. A zero remainder is retained only where its endpoint or truncation payment has separately been established. In particular, the saved $72$-coefficient receipt reports zero remainder modulo $3^{32}$; that is not an assertion of an exact zero endpoint.

The original nonzero endpoint


$$
Q_n^{\mathrm{loc}}(-1)=-F_{\mathrm{fac}}^2\xi
$$


is not replaced by the zero endpoint of an uncorrected core.

### Conditional period theorem

The audited implication is therefore:

> Assume the full precision-local theorem for the original finite producer, retain its aligned window and complete forces, and assume $n$ is large enough for its support and factorial payments. For $M\ge4$, $1\le L\le3M$, the residue
> 

$$
> n\bmod3^{M+\lfloor\log_3(6M-1)\rfloor}
>
$$


> determines $\Xi,\chi\bmod3^M$, $\xi\bmod3^{M-1}$, all $L$ requested top coefficients modulo $3^{M-1}$, and their monic quotient and remainder at $x=-2$.

This is a sufficient period, not a claim of minimality.

The mathematical corollary for general $M,L$ also does not enlarge the supplied program’s implementation guard $M\le33,L\le72$. The requested specialization lies inside that guard.

---

## 14. The $M=33,L=72,E=37$ specialization

Here


$$
3M=99,\qquad H_{\deg}=197,
$$


and


$$
81=3^4\le197<3^5=243.
$$


Therefore


$$
\boxed{E=33+4=37.}
$$



The unrounded window length is


$$
R_0=198+13\cdot32+4=618.
$$


Since $n\equiv2\pmod3$, alignment adds $2$:


$$
\boxed{R=620.}
$$


Its final block is $B_2$: $620=3\cdot206+2$. No $620$-row solve is repeated.

The fixed interpolation endpoint $591=3\cdot197$ is a bounded input for constructing the entry polynomials. It does not replace the physical moment endpoint $2n-2$ of $\mathsf T_n$, the endpoint $2n-1$ of the next-column force above its last coordinate, or the downstream HIGH terminal.

### 14.1 Exact residue reduction

The supplied old input residue is


$$
2\,323\,594\,735\,168\,358\,765\pmod{3^{39}}.
$$


Since


$$
3^{37}=450\,283\,905\,890\,997\,363
$$


and


$$
\begin{aligned}
2\,323\,594\,735\,168\,358\,765
&=5\cdot450\,283\,905\,890\,997\,363\\
&\quad+72\,175\,205\,713\,371\,950,
\end{aligned}
$$


its reduced residue is exactly


$$
\boxed{72\,175\,205\,713\,371\,950\pmod{3^{37}}.}
$$



This is a scalar residue reduction, not a recomputation of the saved coefficient array. The old receipt remains a receipt produced under the old conservative input exponent $39$; the new theorem supplies a later sufficiency deduction.

### 14.2 The actual frozen subfamily

Take


$$
j_t=84645+3^{36}t,\qquad t\ge0.
$$


It remains inside the original arithmetic progression because $3^{12}\mid3^{36}$.

LTE gives


$$
v_3(4^{3^{36}}-1)=v_3(4-1)+36=37.
$$


Thus


$$
4^{j_t}+1\equiv4^{84645}+1\pmod{3^{37}}
$$


for every $t\ge0$.

All these $n$ satisfy $n\equiv2\pmod3$, $n\ge5$, and the required size conditions. At $M=33$, even the crude bound $4^{84645}+1>620$ is more than sufficient for the window and factorial payments.

Consequently, conditional on the local theorem, the actual $72$-coefficient jet modulo $3^{32}$, its degree-at-most-$70$ monic quotient, and the corresponding scalar residues are the same throughout this subfamily.

The earlier family with step $3^{38}$ is contained in this family. Before imposing the real window, the new family has nine times its density within the original arithmetic progression:


$$
\frac{3^{-24}}{3^{-26}}=9.
$$



This freezes a fixed-precision coefficient jet. It does not freeze the complete source polynomial, its varying monomial exponents, the actual $W$-return, or the physical-seven return.

### 14.3 Separate Range-III admission

Let


$$
\alpha=\log_3 4.
$$


It is irrational: a rational equality $\alpha=a/b$ would imply $4^b=3^a$, contrary to unique prime factorization.

The step


$$
3^{36}\alpha
$$


is also irrational. Therefore the fractional parts of


$$
(84645+3^{36}t)\alpha
$$


visit every nonempty open phase interval infinitely often.

The passage from such a strict interior phase interval to the original Range-III window is the separately paid argument using


$$
\frac DH
=1-3^{\{j\alpha\}-1}+\frac1H.
$$


On a closed subinterval strictly inside the admitted phase interval, the inequalities have positive margin, while $1/H\to0$. Hence infinitely many members of the new progression meet


$$
\frac3{25}<\frac{\chi_{\mathrm{range}}}{P}<\frac{31}{250}.
$$



Here $\chi_{\mathrm{range}}$ is the original residual range parameter. It is not the producer scalar


$$
\chi=3n\,u^Th+6u_{n-1}.
$$


The base $j=84645$ is not claimed to meet the real window.

---

## 15. Finite evidence, unperformed calculations, and untouched obligations

### 15.1 Scope of the supplied receipts

The compatibility receipt reports:

- $1188=6\cdot198$ binomial congruences at six specified offsets;
- six unit-power checks;
- $99$ finite force-product checks;
- no recomputation of the complete matrix or original coefficient array.

These checks have only their stated finite scope. They do not prove the uniform period theorem. The proof of that theorem is the degree and precision argument above, conditional on the local theorem.

Likewise, the saved top-$72$ array is one finite candidate-derived original-index receipt. This audit neither reruns it nor independently passes the entire underlying implementation. Conditional periodicity freezes the **actual** jet; identification of the displayed numerical array with that jet retains the original receipt’s local-theorem and implementation dependencies.

Capped depths equal to $32$ mean divisibility by $3^{32}$, not exact vanishing or exact valuation $32$. No uniform $56$-coefficient width theorem is inferred.

### 15.2 No physical return or primitive normalization is evaluated

Neither audit evaluates


$$
\frac{
M(\delta Q\,\widehat F_i\widehat F_j)
-b_i^TE_{\mathrm{act}}^{-1}b_j
}{3^{29}}\pmod3.
$$


In particular, neither evaluates the requested actual $\eta$, $N_{00}/3^{29}$, the full physical-seven form, or its HIGH terminal.

The dyadic pivot notation $\eta_d=\det K_d$ is unrelated to treating such an actual return as evaluated. Likewise, the implementation variable named `eta` represents $\Xi$, not a new evaluation of the outstanding physical return.

No conclusion is drawn about an actual all-prime clearer or primitive denominator from ternary integrality alone.

Earlier source-$81$, fourth-linear, and $J_7$-transport claims remain awaiting their different audits. This report does not silently pass them. The separate binary producer and its complete corrected columns and physical terminal are not changed or used as an arithmetic shortcut.

### 15.3 Bounded arithmetic needed

No new matrix computation, coefficient solve, determinant scan, repeated finite array, or capped Smith experiment is needed for either proof audit.

The bounded scalar arithmetic used for the specialization is fully specified:

| Inputs | Expected verifiable output | Scope |
|---|---|---|
| $M=33,L=72$ | $H_{\deg}=197$, $E=37$, $R_0=618$, $R=620$ | Degree and alignment |
| $3^{37}$ and the supplied old residue | Quotient $5$, remainder $72\,175\,205\,713\,371\,950$ | Input-residue reduction |
| Supplied logarithm brackets | $\delta_{19/4}>269055/3400000>0$ | Conditional asymptotic margin |

If the saved residue’s attribution to the actual $j=84645$ is not already admitted as finite input evidence, the only additional numerical authentication needed for that attribution is the bounded modular exponentiation


$$
(4^{84645}+1)\bmod3^{37}.
$$


Its expected output is


$$
72\,175\,205\,713\,371\,950.
$$


That check would authenticate only the input residue. It would not be a coefficient solve or a verification of any physical return.

---

## 16. Compact proof-status ledger

| Claim | Status after this report |
|---|---|
| First Laguerre spread gain $4/85$, uniform trace formulas | **Established reuse; not repeated** |
| Later pairwise-convexity improvement | **Not audited here** |
| Exact ternary contents and canonical signed Hermite returns | **Established reuse; not repeated** |
| Literal dyadic row operator and odd determinant | **PASS, proved above** |
| Rational cancellation in every common return column | **PASS, both factorial terms retained** |
| Exact normalized forcing-pivot valuation | **PASS** |
| Literal atom and $c=u-w$ valuation | **PASS** |
| Adjugate clearer and all column divisions | **PASS, simultaneous for both coefficients** |
| Exact all-prime gcd identity and original-domain $\kappa_k$ | **PASS** |
| Residual paired upper bound with coefficient $19/4$ | **Open** |
| Other odd-prime descents, including primes above $6k-5$ | **Open** |
| Sharp $19/4$ retirement implication | **Proved conditional implication** |
| Degree-controlled input exponent $E=M+\lfloor\log_3(6M-1)\rfloor$ | **PASS conditional on full local theorem** |
| $M=33,L=72,E=37,R=620$ specialization | **Verified deduction at that conditional scope** |
| Frozen family $j=84645+3^{36}t$ | **New source-specific conditional deduction** |
| Real Range-III infinite admission | **Paid rotation argument reused; new step remains irrational** |
| Full precision-local theorem and full implementation | **Different audit still pending elsewhere** |
| Uniform $56$-coefficient representative | **Not passed here** |
| Older source-$81$, fourth-linear, $J_7$-transport claims | **Still awaiting different audit** |
| Actual $\eta$, $N_{00}/3^{29}$, $W$, full physical seven | **Not evaluated** |
| Actual primitive whole-error decay or divergence | **Not established unconditionally** |
| Rationality or irrationality of $e+\pi$ | **Unresolved** |

## 17. Final conclusion

The first new audited result is the fully paid identity


$$
\boxed{
v_2(G_k)=\kappa_k+
\min\bigl(v_2(J_{0,k}),v_2(J_{1,k})\bigr),
\qquad \kappa_k=O(k\log k),
}
$$


with the complete original columns, literal atom, original final row, physical factorial boundary, and all-prime normalization retained.

The exact remaining arithmetic bottleneck for that producer is a uniform upper bound for the **joint valuation of the corrected residual pair**, together with the other-odd-prime descents. The target $19/4$ is sufficient after the exact ternary saving, but remains unproved.

The second audited result is the conditional source-input period


$$
\boxed{3^{\,M+\lfloor\log_3(6M-1)\rfloor},}
$$


including every reconstruction, forcing, scalar, and quotient payment. At target precision $32$, it freezes the actual local jet on the original arithmetic subfamily


$$
\boxed{j=84645+3^{36}t.}
$$


It does not evaluate the varying physical returns or their primitive normalization.

Finally, for a rational number $A/B$, any nonzero integer linear error satisfies


$$
\left|q\frac AB-p\right|\ge\frac1B.
$$


Thus a valid irrationality proof would require an appropriate sequence of nonzero **whole** primitive errors tending to zero, or another unconditional argument. Neither audited construction presently supplies that conclusion. The global problem for $e+\pi$ remains open.
