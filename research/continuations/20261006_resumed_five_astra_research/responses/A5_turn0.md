> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5, new turn 0 — Exterior-load compression of the complete second force and a four-variable identity for the original squared-weight contractions

## Executive conclusion

The supplied endpoint Schur solve is now an input, not an outstanding calculation. I do not recompute or request it.

This report takes the **structural-identity alternative** in the assignment. It proves a reduction for the **complete original norm and mixed contraction**, not merely for a first-layer weighted kernel:

> At the original $u=0$, modulo $2^{20}$, both reconstructed columns can be represented by two hypergeometric generating-function branches. After their actual finite endpoint corrections have been applied, the complete squared-weight norm and complete exponential mixed output are coefficients of **four explicitly specified rational kernels in four variables**.

The reduction retains:

- the original contact domain $0,\ldots,b-1$;
- reconstruction through $j=b$;
- both independent contraction variables;
- all contact shifts through $76$;
- every exponential-tail label that survives at twenty bits;
- the supplied, nonidentity endpoint Schur correction;
- the complete factorial subtraction in the normalized second force;
- the exterior $+1$, through an explicit principal-part calculation;
- the additional precision required by the actual norm valuation.

The main new steps are:

1. **Complete exponential forcing as an exterior-column load.**  
   Its apparent collection of $(a,s,t)$-channels can be assembled exactly into one load on columns $b,\ldots,b+23$ of the same extended operator. Applying the finite block factorization reduces its response to at most $100$ exterior transfer columns.

2. **A bulk generating function for every required exterior transfer column.**  
   It includes its entire principal part, rather than replacing the finite transfer by an infinite one.

3. **A two-branch normal form for both actual contact responses.**  
   At twenty bits it uses four polynomials containing only $952$ residue slots in total.

4. **A common-$n$ coefficient identity for the complete squared-weight contractions.**  
   It reduces the outstanding extraction to four-variable kernels while preserving the original cutoff.

This does **not** yet evaluate $D_{\rm raw}=4N$ or $E_{\rm raw}=8H$. In particular, it does not certify their first nonzero digits, their contents, a relative-output law, or the full primitive denominator.

No tools were executed. No new numerical residues, hashes, or independently reproduced receipts are claimed.

---

## 1. Domain, inputs, and accepted scope

The original family remains


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge 0.
$$


For the requested original specialization,


$$
b=150094635296999121,\qquad
n=600678730458590482242.
$$


We work first at


$$
M=20,\qquad q=2^{20},\qquad m=76.
$$



Set


$$
B=b-1,\qquad N_0=n+2,\qquad W_j=\binom{N_0}{j}.
$$


Thus $b$ is odd and $B$ is even.

Contact vectors have coordinates $0,\ldots,B$. Reconstruction has coordinates $0,\ldots,b$:


$$
(Cx)_j=jx_{j-1}-x_j,\qquad x_{-1}=x_b=0,
$$




$$
\mathcal R=\operatorname{diag}(W_j)C.
$$


The normalized columns and outputs remain


$$
\mathsf a=\mathcal RA^{-1}f,\qquad
\mathsf b=\mathcal RA^{-1}r+W_be_b,
$$




$$
r=\frac{h^e+h^F-A(j!)_{0\le j<b}}{b!},
$$




$$
D_{\rm raw}=\mathsf a^T\mathsf a=4N,\qquad
E_{\rm raw}=\mathsf a^T\mathsf b=8H.
$$



### 1.1 Reused operator inputs

I reuse the accepted finite factorization


$$
A\equiv LUJU\pmod q,
\qquad
J=H+F_m\overline K E,
\tag{1.1}
$$


where $E$ selects $b-m,\ldots,b-1$, and $F_m$ consists of exterior transfer columns $0,\ldots,m-1$.

The band inverse coefficients satisfy


$$
(H^{-1})_{j,j-s}=c_s\binom js,\qquad 0\le s\le m.
\tag{1.2}
$$


The coefficients $\lambda_s,c_s$, their filtration, and their integral divided-power interpretation are reused at their accepted scope.

Write


$$
S=I_m+EH^{-1}F_m\overline K.
\tag{1.3}
$$


The supplied $S^{-1}\bmod 2^{20}$ is used with exactly this factor grouping.

The coordinator’s receipt reports the original $76\times76$ solve, both inverse products, and the independent padded adjoint comparison. Its scope is an operator certificate. It is not a weighted Gram certificate.

### 1.2 Complete force cutoffs

The first-force budget gives


$$
f_i\equiv0\pmod{2^{20}}\qquad(i\ge48).
$$


Accordingly put


$$
I=48.
$$


All $f_0,\ldots,f_{47}$ below are the **complete actual normalized coefficients**.

For the exponential tail define


$$
v_t=t!\binom{b+t}{t}=\frac{(b+t)!}{b!}.
\tag{1.4}
$$


Since $v_2(t!)\ge20$ for $t\ge24$, it is sufficient, without exploiting any additional cancellation, to retain


$$
0\le t\le T,\qquad T=23.
\tag{1.5}
$$


In particular, $v_0=1$.

The accepted force formula is therefore equivalently


$$
r_i^e\equiv
\sum_{t=0}^{T}v_t
\sum_{s=0}^{m}
\lambda_s
\binom{n+i}{s}
\binom{2n+i-s}{b+t}
\pmod q.
\tag{1.6}
$$


This is the complete layer sum: expanding $\lambda_s$ into its $\lambda_s^{(a)}$ recovers every surviving $(a,s,t)$-term. Terms killed by $a+v_2(t!)\ge20$ disappear through their coefficients, not through a replacement of the source.

At this original index, all displayed small shifts are within the valid source ranges. The general zero conventions remain in force.

The logarithmic threshold is


$$
K_{\rm norm}
=
1+v_2((n/2)!)-v_2(b!)
-\lfloor\log_2(2n+b-1)\rfloor.
\tag{1.7}
$$


The accepted estimate


$$
K_{\rm norm}\ge2000b-138>20
$$


justifies omitting $h^F/b!$ for the present **absolute twenty-bit calculation**. Section 7 records the restriction at greater, norm-dependent precision.

---

# Part I. Compressing the complete second force

## 2. The exponential tail is an exterior-column load

The following identity is the first substantive new reduction.

### Theorem 1 — Exterior-load identity

Let $A^+$ denote the rectangular extension of the original operator to the finitely many columns needed below, with


$$
A^+_{i,k}
=
\sum_{s=0}^{m}
\lambda_s\binom{n+i}{s}\binom{2n+i-s}{k},
\qquad 0\le i<b.
\tag{2.1}
$$


Its first $b$ columns equal the actual $A\bmod q$. If $v$ is supported on exterior indices $0,\ldots,T$, then


$$
r^e\equiv A^+_{\mathrm{out}}v\pmod q.
\tag{2.2}
$$



Let


$$
\mathsf U_{\mathrm{out},r,t}=\binom n{t-r}
$$


in its upper-triangular range, and


$$
\mathsf H_{\mathrm{out},r,k}
=
\lambda_{r-k}\binom{b+r}{r-k}
$$


for $0\le r-k\le m$. Put


$$
u^{\mathrm{out}}_r
=
\sum_{t=r}^{T}\binom n{t-r}v_t,
\qquad 0\le r\le T,
\tag{2.3}
$$


and


$$
h^{\mathrm{out}}_r
=
\sum_{k=\max(0,r-m)}^{\min(r,T)}
\lambda_{r-k}\binom{b+r}{r-k}u^{\mathrm{out}}_k,
\qquad 0\le r\le T+m.
\tag{2.4}
$$


Then


$$
\boxed{
A^{-1}r^e
=
F_{T+1}v+
U^{-1}J^{-1}F_{T+m+1}h^{\mathrm{out}}
\pmod q.
}
\tag{2.5}
$$



Here $F_R$ means exterior transfer columns $0,\ldots,R-1$. Thus the largest exterior transfer index needed at twenty bits is $99$.

#### Proof

For the infinite triangular matrices, interpreted only on the finitely supported vectors in question,


$$
(LU)_{i,k}=\binom{n+i}{k}.
$$


Consequently


$$
(LUH)_{i,j}
=
\sum_s\lambda_s
\binom{j+s}{s}\binom{n+i}{j+s}
=
\sum_s\lambda_s
\binom{n+i}{s}\binom{n+i-s}{j}.
$$


Multiplication by the rightmost $U$, followed by Vandermonde convolution, gives (2.1).

This use of an extended operator does not replace the finite inverse: it only identifies the specified exterior source columns. Equation (1.6) now proves (2.2).

Partition the triangular factors at the original contact boundary:


$$
U_\infty=
\begin{pmatrix}
U&T_{\rm out}\\
0&\mathsf U_{\rm out}
\end{pmatrix},
\qquad
H_\infty=
\begin{pmatrix}
H&0\\
K_{\rm out}&\mathsf H_{\rm out}
\end{pmatrix}.
$$


Only the first $m$ rows of $K_{\rm out}$ can be nonzero, and


$$
K_{\rm out}= \begin{pmatrix}\overline K E\\0\end{pmatrix}.
$$


Let


$$
F_{\rm out}=U^{-1}T_{\rm out}.
$$


The upper-left block of $U_\infty H_\infty U_\infty$ is $UJU$. Its upper-right block is


$$
UJ T_{\rm out}
+
T_{\rm out}\mathsf H_{\rm out}\mathsf U_{\rm out}.
$$


Since the first $b$ rows of the leftmost $L_\infty$ involve only the original $L$,


$$
A^{-1}A^+_{\rm out}
=
U^{-1}T_{\rm out}
+
U^{-1}J^{-1}F_{\rm out}
\mathsf H_{\rm out}\mathsf U_{\rm out}.
$$


Applying this identity to $v$ gives (2.5).

The support statements follow from upper triangularity of $\mathsf U_{\rm out}$ and bandwidth $m$ of $\mathsf H_{\rm out}$. ∎

### Significance and limitation

Equation (2.5) preserves the complete inhomogeneous exponential force while avoiding separate contact inversions for its many $(a,s,t)$-labels.

The exterior indices through $b+99$ are **intermediate algebraic transfer indices**, not new solved rows or reconstructed coordinates. The finite contact system still ends at $b-1$, and reconstruction still ends at $b$.

---

## 3. Signed reversal and the full exterior-column generating function

Put


$$
t(z)=(1-z)^{-n}.
$$


For a contact vector $x$, define its signed reversed coefficients by


$$
g_k=(-1)^{B-k}x_{B-k},\qquad 0\le k\le B.
\tag{3.1}
$$


The associated generating polynomial is $\sum_{k=0}^B g_kz^k$.

Signed reversal is useful here because $U^{-1}$ becomes ordinary multiplication by $t(z)$, followed by the original finite coefficient projection.

Indeed, if $x'=U^{-1}x$, then


$$
(-1)^j x'_j
=
\sum_{r=0}^{B-j}\binom{n+r-1}{r}
\,(-1)^{j+r}x_{j+r}.
$$


Thus


$$
g'\equiv P_{<b}\bigl(tg\bigr).
\tag{3.2}
$$



### 3.1 The finite inverse-band action

For an analytic series $G(z)$, define


$$
\mathscr S_sG
=
z^{-s}\bigl(G-P_{<s}G\bigr),
\tag{3.3}
$$


and


$$
\boxed{
\Psi G
=
\sum_{s=0}^{m}(-1)^sc_s
\binom{B-\theta}{s}\mathscr S_sG,
\qquad \theta=z\frac{d}{dz}.
}
\tag{3.4}
$$


The binomial operator is defined coefficientwise:


$$
\binom{B-\theta}{s}\sum_k a_kz^k
=
\sum_k\binom{B-k}{s}a_kz^k.
$$



Its coefficient at $z^k$, for $0\le k<b$, is


$$
\sum_{s=0}^{m}(-1)^sc_s
\binom{B-k}{s}g_{k+s}.
\tag{3.5}
$$


For $k+s\ge b$, the factor $\binom{B-k}{s}$ is zero. Hence an analytic extension of the input beyond degree $B$ does not introduce a false returning endpoint.

Equation (3.5) is exactly signed reversal of (1.2). Therefore $\Psi$, followed by $P_{<b}$, gives the actual finite $H^{-1}$-action.

This is not an ordinary-jet closure claim. It is a coordinate reversal of the accepted finite operator, with its vanishing endpoint factor retained.

### 3.2 Exterior transfer columns

The supplied finite transfer formula is


$$
F_{j,r}
=
-\sum_{v=0}^{r}
\binom{-n}{b+v-j}\binom n{r-v}.
\tag{3.6}
$$


For any required $r\ge0$, define


$$
P_r(z)=\sum_{a=0}^{r}(-1)^a\binom na z^a
=P_{\le r}(1-z)^n.
\tag{3.7}
$$



### Lemma 2 — Entire exterior-column generating function

For $B$ even, the signed reversed exterior column has the analytic extension


$$
\boxed{
\mathcal F_r(z)
=
(-1)^r z^{-r-1}\bigl(t(z)P_r(z)-1\bigr).
}
\tag{3.8}
$$


For $0\le k<b$,


$$
[z^k]\mathcal F_r
=
(-1)^{B-k}F_{B-k,r}.
\tag{3.9}
$$



#### Proof

From (3.6),


$$
(-1)^{B-k}F_{B-k,r}
=
\sum_{v=0}^{r}(-1)^v\binom n{r-v}
\binom{n+k+v}{k+v+1}.
$$


Thus its generating series is


$$
\sum_{v=0}^{r}(-1)^v\binom n{r-v}
z^{-v-1}\bigl(t-P_{\le v}t\bigr).
\tag{3.10}
$$


The coefficient multiplying $t$ is


$$
(-1)^r z^{-r-1}P_r(z).
$$



It remains to determine the entire negative-power correction. The coefficient of $z^{-h-1}$ in the subtracted part is


$$
-\sum_{v=h}^{r}(-1)^v
\binom n{r-v}\binom{n+v-h-1}{v-h}.
$$


After putting $k=v-h$, this equals


$$
-(-1)^h[z^{r-h}](1+z)^n(1+z)^{-n},
$$


which is zero unless $h=r$, when it equals $(-1)^{r+1}$. This proves (3.8).

Finally $tP_r=1+O(z^{r+1})$, so (3.8) is analytic at zero. ∎

For a load $\eta=(\eta_0,\ldots,\eta_{R-1})$, write


$$
\mathcal F_\eta=\sum_{r=0}^{R-1}\eta_r\mathcal F_r,
\tag{3.11}
$$


and


$$
A_\eta(z)=
\sum_{r=0}^{R-1}(-1)^r\eta_rz^{-r-1}P_r(z),
\qquad
B_\eta(z)=
\sum_{r=0}^{R-1}(-1)^r\eta_rz^{-r-1}.
\tag{3.12}
$$


Then the exact identity is


$$
\boxed{\mathcal F_\eta=tA_\eta-B_\eta.}
\tag{3.13}
$$



The term $B_\eta$ is not optional. In particular, dropping it before applying $\Psi$ would change the source and its endpoint correction.

---

## 4. Using the supplied Schur inverse on these generating functions

Define the endpoint extraction map


$$
(\mathcal EG)_t
=
(-1)^{b-m+t}[z^{m-1-t}]G,
\qquad 0\le t<m.
\tag{4.1}
$$


This is exactly the original selector $E$ after signed reversal.

For an analytic source extension $Y$, put


$$
\beta(Y)=S^{-1}\mathcal E(\Psi Y),
\qquad
\eta(Y)=\overline K\,\beta(Y),
\tag{4.2}
$$


and define


$$
\boxed{
\mathcal JY
=
\Psi Y-\Psi\mathcal F_{\eta(Y)}.
}
\tag{4.3}
$$


The load in the second term has length $m$.

By the accepted finite Woodbury identity, $P_{<b}\mathcal JY$ is signed reversal of $J^{-1}y$. Equation (4.3) uses the supplied $S^{-1}$ in its original orientation; no endpoint factors have been reordered.

### 4.1 First source

Since $L^{-1}_{j,\ell}=(-1)^{j-\ell}\binom j\ell$, the reversed signed first source before the first $U^{-1}$ has analytic extension


$$
F_f(z)=
\sum_{\ell=0}^{I-1}(-1)^\ell f_\ell
\sum_{d=0}^{\ell}(-1)^d
\binom{B-d}{\ell-d}\frac{z^d}{(1-z)^{d+1}}.
\tag{4.4}
$$


This follows from the integer Newton identity


$$
\binom{B-k}{\ell}
=
\sum_{d=0}^{\ell}(-1)^d
\binom{B-d}{\ell-d}\binom kd.
\tag{4.5}
$$


Set


$$
Y_f=tF_f.
$$


Then the actual first contact response is represented by


$$
\boxed{G_f=t\,\mathcal JY_f.}
\tag{4.6}
$$



### 4.2 Complete exponential response

Let $h^{\rm out}$ be the complete load (2.4). Equation (2.5) gives the analytic contact-response extension


$$
G_e^{\rm an}
=
\mathcal F_v+t\,\mathcal J\mathcal F_{h^{\rm out}}.
\tag{4.7}
$$


For later reconstruction it is convenient to use the Laurent series


$$
\boxed{
G_e^*
=
tA_v+t\,\mathcal J\mathcal F_{h^{\rm out}}.
}
\tag{4.8}
$$


The precise relation is


$$
G_e^*=G_e^{\rm an}+B_v.
\tag{4.9}
$$


Therefore:

- all nonnegative coefficients of $G_e^*$ are the actual signed reversed contact coefficients;
- its complete principal part is $B_v$;
- in particular,
  

$$
[z^{-1}]G_e^*=v_0=1.
  \tag{4.10}
$$



That last coefficient will account for the exterior $+1$ exactly.

---

# Part II. A bounded two-branch normal form

## 5. Four short polynomials suffice before reconstruction

Define


$$
R=T+m+1,\qquad
L_0=R+m,\qquad
k_0=I+m.
\tag{5.1}
$$


At twenty bits,


$$
R=100,\qquad L_0=176,\qquad k_0=124.
$$



### Theorem 3 — Two-branch form for the complete responses

There exist polynomials


$$
P_{f,2},\ P_{f,1},\ P_{e,2},\ P_{e,1}
$$


over $\mathbb Z/2^{20}\mathbb Z$ such that


$$
\boxed{
G_\alpha(z)
=
z^{-L_0}
\left(
\frac{P_{\alpha,2}(z)}{(1-z)^{2n+k_0}}
+
\frac{P_{\alpha,1}(z)}{(1-z)^n}
\right),
\qquad \alpha=f,e,
}
\tag{5.2}
$$


where $G_f$ means (4.6) and $G_e$ means $G_e^*$ in (4.8).

They satisfy


$$
\deg P_{\alpha,2}<L_0+k_0,\qquad
\deg P_{\alpha,1}<L_0.
\tag{5.3}
$$


Thus the four polynomials occupy at most


$$
2(300+176)=952
$$


residue slots.

Moreover,


$$
P_{<0}G_f=0,\qquad P_{<0}G_e^*=B_v.
\tag{5.4}
$$



#### Proof: integral operator formula

For any integer Laurent exponent $r$ and any nonnegative integer $A$,


$$
\boxed{
\begin{aligned}
\binom{B-\theta}{s}
\left(z^{r-s}(1-z)^{-A}\right)
={}&
\sum_{e=0}^{s}(-1)^e
\binom{B-r+s-e}{s-e}\\
&\quad\cdot
\binom{A+e-1}{e}
z^{r-s+e}(1-z)^{-A-e}.
\end{aligned}
}
\tag{5.5}
$$


For $A=0$, the second binomial is understood through the divided derivative, so only $e=0$ survives.

To prove (5.5), move $z^{r-s}$ through the coefficientwise operator and use


$$
\binom{a-\theta}{s}
=
\sum_{e=0}^{s}(-1)^e
\binom{a-e}{s-e}z^e\partial^{[e]},
\tag{5.6}
$$


together with


$$
\partial^{[e]}(1-z)^{-A}
=
\binom{A+e-1}{e}(1-z)^{-A-e}.
$$


All coefficients are integers. In particular, (5.5) requires no inversion of $s!$ or $e!$ modulo $2^{20}$.

#### Proof: degree bounds

Equation (4.4) can be written


$$
F_f=P_f(z)(1-z)^{-I},
\qquad \deg P_f<I.
$$


Using (5.5), subtracting the required prefixes in $\mathscr S_s$, and then multiplying by the final $t$, gives


$$
t\Psi Y_f
=
z^{-m}
\left(
\frac{U_2(z)}{(1-z)^{2n+I+m}}
+
\frac{U_1(z)}{(1-z)^n}
\right),
$$


with


$$
\deg U_2\le I+2m-1,\qquad
\deg U_1\le m-1.
\tag{5.7}
$$



Similarly, for a load of length $R'$, formula (3.13) has the form


$$
\mathcal F_\eta
=
z^{-R'}\bigl(A(z)(1-z)^{-n}+B(z)\bigr),
$$


where both polynomials have degree less than $R'$. The same calculation gives


$$
t\Psi\mathcal F_\eta
=
z^{-(R'+m)}
\left(
\frac{V_2(z)}{(1-z)^{2n+m}}
+
\frac{V_1(z)}{(1-z)^n}
\right),
\tag{5.8}
$$


with


$$
\deg V_2\le R'+2m-1,\qquad
\deg V_1\le R'+m-1.
$$



These bounds apply both to the complete exterior source of length $R=100$ and to the Schur correction loads of length $m=76$.

Bring all terms to the common Laurent shift $z^{-L_0}$ and common first-branch exponent $2n+k_0$. Equations (5.7)–(5.8) give precisely (5.3). The direct term $tA_v$ contributes only to the $(1-z)^{-n}$-branch and also satisfies the bound.

Finally, (5.4) follows from the analyticity statements in Sections 3–4. ∎

### What has been controlled

The normal form is for the **complete two actual responses at this precision**, including the supplied finite Schur correction. It is not a closure theorem under arbitrary repeated weight multiplication.

No original-length coefficient vector is needed to construct its four polynomials.

---

## 6. Reconstruction, the exterior endpoint, and the four-variable contraction identity

### 6.1 Reconstruction on a signed reversed series

Define


$$
\mathfrak C_b=\theta-b-z.
\tag{6.1}
$$


For an analytic contact extension $G=\sum g_kz^k$,


$$
[z^k]\mathfrak C_bG
=-(b-k)g_k-g_{k-1},
\tag{6.2}
$$


with $g_{-1}=0$.

For $0\le k\le b$, this is signed reversal of $Cx$ at $j=b-k$. At the two endpoints:

- $k=0$, corresponding to $j=b$, gives $-bg_0$;
- $k=b$, corresponding to $j=0$, gives $-g_{b-1}$, because the coefficient of the unneeded $g_b$ is zero.

Thus the finite row and reconstruction boundaries are both preserved.

Set


$$
\widehat G_f=\mathfrak C_bG_f,\qquad
\widehat G_e=\mathfrak C_bG_e^*.
\tag{6.3}
$$


For the second series, (4.10) gives


$$
[z^0]\widehat G_e
=-b[z^0]G_e^{\rm an}-1.
\tag{6.4}
$$


Since $(-1)^b=-1$, the last $-1$ is exactly the signed reversal of the exterior $+1$ in $\mathsf b$.

Consequently, for every original reconstructed index $0\le j\le b$,


$$
\boxed{
\mathsf a_j
=
(-1)^jW_j[z^{b-j}]\widehat G_f,
\qquad
\mathsf b_j
=
(-1)^jW_j[z^{b-j}]\widehat G_e
\pmod q.
}
\tag{6.5}
$$


The second equality includes the entire exponential force and the exterior term; its logarithmic qualification is still (1.7).

In particular, the physical endpoint contribution has not been declared zero. It remains


$$
W_b\mathsf a_b=bW_b^2(A^{-1}f)_{b-1}.
$$


Equation (6.4) merely incorporates it into the generating-function formula.

### 6.2 Reconstructed polynomial coefficients

Put


$$
\delta_1=0,\qquad \delta_2=k_0.
$$


For $\alpha=f,e$ and $\rho=1,2$, define


$$
\boxed{
\widehat P_{\alpha,\rho}
=
(1-z)\left(
zP'_{\alpha,\rho}-(b+L_0+z)P_{\alpha,\rho}
\right)
+
(\rho n+\delta_\rho)zP_{\alpha,\rho}.
}
\tag{6.6}
$$


Then


$$
\widehat G_\alpha
=
z^{-L_0}
\sum_{\rho=1}^{2}
\frac{\widehat P_{\alpha,\rho}(z)}
{(1-z)^{\rho n+\delta_\rho+1}}.
\tag{6.7}
$$


At twenty bits,


$$
\deg\widehat P_{\alpha,2}\le301,\qquad
\deg\widehat P_{\alpha,1}\le177.
\tag{6.8}
$$


The four reconstructed polynomials therefore occupy at most $960$ residue slots.

### 6.3 The actual squared-weight gluing identity

The elementary identity


$$
\boxed{
[u^{N_0}](1+u)^{N_0}(u+xy)^{N_0}
=
\sum_{j=0}^{N_0}\binom{N_0}{j}^{\!2}(xy)^j
}
\tag{6.9}
$$


is useful only after the two independent matrix variables $x,y$ have been retained.

It follows by expanding $(u+xy)^{N_0}$: its $j$-th term requires $u^j$ from $(1+u)^{N_0}$, giving the second binomial coefficient.

This is **not** a substitution identifying two weight variables. It is an exact elimination after summing the common metric index.

Because $\widehat G_f$ is analytic,


$$
\begin{aligned}
D_{\rm raw}
&=[x^by^bu^{N_0}]
\widehat G_f(x)\widehat G_f(y)
(1+u)^{N_0}(u+xy)^{N_0},\\
E_{\rm raw}
&=[x^by^bu^{N_0}]
\widehat G_f(x)\widehat G_e(y)
(1+u)^{N_0}(u+xy)^{N_0}.
\end{aligned}
\tag{6.10}
$$



The apparent full weight polynomial in (6.9) does not replace the cutoff. For $j>b$, the $x$-coefficient required from the complete $\widehat G_f(x)$ is negative and hence zero. Thus the surviving range is exactly $0\le j\le b$.

For a branchwise implementation, those cancellations must be retained by summing **all** first-column branches. A branch alone may have a principal part and may not be assigned the same cutoff without its correction.

Expanding (6.5) also recovers the actual reconstruction metric:


$$
(Q_{\rm rec})_{ii}=W_i^2+(i+1)^2W_{i+1}^2,
$$




$$
(Q_{\rm rec})_{i,i+1}=-(i+1)W_{i+1}^2,
$$


including


$$
(Q_{\rm rec})_{b-1,b-1}=W_{b-1}^2+b^2W_b^2.
$$



### 6.4 A common-$n$ marker

For $\rho,\sigma\in\{1,2\}$, put


$$
\boxed{
Q_{\rho,\sigma}
=
(1-x)^\rho(1-y)^\sigma
-d(1+u)(u+xy).
}
\tag{6.11}
$$


Define the four rational kernels


$$
\boxed{
\mathcal K_{\rho,\sigma}
=
\frac{(1+u)^2(u+xy)^2}
{(1-x)^{(k_0-1)\mathbf1_{\rho=2}}
 (1-y)^{(k_0-1)\mathbf1_{\sigma=2}}
 Q_{\rho,\sigma}}.
}
\tag{6.12}
$$


All expansions are ordinary power-series expansions at the origin. Every denominator has constant term $1$.

Let


$$
\mathcal T=
[x^{b+L_0}y^{b+L_0}u^{n+2}d^n].
\tag{6.13}
$$



### Theorem 4 — Complete four-variable output identity

At the original $u=0$, modulo $2^{20}$,


$$
\boxed{
D_{\rm raw}
=
\sum_{\rho,\sigma=1}^{2}
\mathcal T\!
\left(
\widehat P_{f,\rho}(x)
\widehat P_{f,\sigma}(y)
\mathcal K_{\rho,\sigma}
\right),
}
\tag{6.14}
$$


and


$$
\boxed{
E_{\rm raw}
=
\sum_{\rho,\sigma=1}^{2}
\mathcal T\!
\left(
\widehat P_{f,\rho}(x)
\widehat P_{e,\sigma}(y)
\mathcal K_{\rho,\sigma}
\right).
}
\tag{6.15}
$$



#### Proof

Write


$$
H(x,y,u)=(1+u)(u+xy),\qquad
F_{\rho,\sigma}=(1-x)^\rho(1-y)^\sigma.
$$


Then


$$
[d^n]\frac1{F_{\rho,\sigma}-dH}
=
\frac{H^n}{F_{\rho,\sigma}^{\,n+1}}.
$$


Multiplying by the numerator and the two additional pole factors in (6.12) gives


$$
[d^n]\mathcal K_{\rho,\sigma}
=
\frac{H^{n+2}}
{(1-x)^{\rho n+\delta_\rho+1}
 (1-y)^{\sigma n+\delta_\sigma+1}}.
\tag{6.16}
$$


Substitute (6.7) into (6.10), clear the two Laurent shifts $x^{-L_0}y^{-L_0}$, and apply (6.16). This proves both formulas. ∎

### Exact targets and shifts

At twenty bits the target is


$$
[x^{b+176}y^{b+176}u^{n+2}d^n].
$$


These are full integers, not their low twenty-bit residues.

A monomial $x^r y^s$ in the two numerator polynomials changes the targets independently to


$$
b+176-r,\qquad b+176-s.
$$


The shifts are not combined into $r+s$, and $x$ and $y$ are never identified.

The constant-degree core denominators have data


$$
\begin{array}{c|c|c}
(\rho,\sigma)&
\deg_{x,y,u,d}Q_{\rho,\sigma}&
\deg Q_{\rho,\sigma}\\ \hline
(1,1)&(1,1,2,1)&4\\
(1,2)&(1,2,2,1)&4\\
(2,1)&(2,1,2,1)&4\\
(2,2)&(2,2,2,1)&4.
\end{array}
$$


The additional pole exponent is $k_0-1=123$, depending on precision, not on the original $b$ or $n$.

This is the promised structural reduction of the complete outputs.

---

# Part III. Precision, feasibility, and the remaining local obligation

## 7. Content cancellation and guard digits

No row or column has been divided by a guessed content. The polynomials above encode the original reconstructed columns modulo the working modulus.

Let


$$
a=\min_jv_2(\mathsf a_j),\qquad
c=\min_jv_2(\mathsf b_j),
$$


and


$$
d_0=v_2(D_{\rm raw}),\qquad e_0=v_2(E_{\rm raw}).
$$


Then


$$
D_{\rm raw}=2^{2a}D_{\rm prim},\qquad
E_{\rm raw}=2^{a+c}E_{\rm prim},
$$


but $D_{\rm prim}$ need not be odd. The extra norm and mixed losses are


$$
\nu=d_0-2a,\qquad \xi=e_0-a-c.
$$



The ratio is


$$
\frac HN=\frac{E_{\rm raw}}{2D_{\rm raw}}.
\tag{7.1}
$$


Suppose $D_{\rm raw}$ and $E_{\rm raw}$ are known to depths $M_D,M_E$, with their valuations certified below those depths. A difference-of-quotients calculation gives ratio-error depth at least


$$
\min\{M_E-d_0-1,\ M_D+e_0-2d_0-1\}.
$$


Thus sufficient conditions for accuracy modulo $2^s$ are


$$
\boxed{
M_E\ge s+d_0+1,\qquad
M_D\ge s+2d_0+1-e_0,
}
\tag{7.2}
$$


together with $M_E>e_0$, $M_D>d_0$.

A zero residue modulo $2^{20}$ would give only a valuation lower bound. It would not permit content cancellation or a relative-output assertion.

### 7.1 Internal arithmetic

The construction uses integral binomial identities, divided derivatives, additions, multiplications, and the supplied unit inverse $S^{-1}$. It introduces no factorial-denominator precision loss.

The accepted layer rule remains:


$$
\text{a term carrying }2^a\text{ needs only precision }M-a.
$$


It applies to the $\lambda_s$-layers, inverse-band layers, and exterior factorial loads. It does not remove the norm-dependent loss in (7.2).

For a first-column replacement with coordinate error depth $T_0$, the distinct accepted budgets remain


$$
\min(T_0+a+1,2T_0)
$$


for a squared approximate norm,


$$
T_0+a
$$


for a one-sided norm contraction against the exact force, and


$$
T_0+c
$$


for the mixed contraction against the exact second column.

### 7.2 Greater precision and the logarithmic force

The same structural proof applies at other working precisions, with the corresponding $I_M,T_M,m_M$, whenever the stated small-shift ranges remain valid.

However, if norm cancellation requires more than twenty bits, every ingredient must be known at that greater precision. The supplied twenty-bit Schur inverse cannot simply be treated as an exact $2$-adic inverse.

If the eventual required precision exceeds $K_{\rm norm}$, the exact additional term is


$$
\boxed{
E_F=\sum_{i=0}^{b-1}w_i\,\frac{h_i^F}{b!},
\qquad
w=A^{-T}\mathcal R^T\mathsf a.
}
\tag{7.3}
$$


The two-branch exponential identity does not authorize deleting it.

No new endpoint solve or lift is requested in this report.

---

## 8. What is now practical, and what is not yet established

The **construction of the four polynomial numerators** is practical at the original index. It uses only precision-sized arrays and small-lower-index binomials.

The remaining four-variable coefficient extraction has not been shown here to have a small reachable or observable module.

This distinction matters. The constant-degree core $Q_{\rho,\sigma}$ is substantially simpler than the earlier seven-variable upper kernel, and the complete descendants have now been assembled explicitly. Nevertheless:

- the numerator polynomials have degrees up to $301$;
- some branches have extra poles of order $123$;
- their exact prime-power carries remain;
- the final answer requires the combined branches, including their principal-part cancellations.

Putting all factors into a single generic denominator and quoting automaticity is not a practical cost proof. Conversely, a large dense box for that representation would not rule out factorized or observable compression.

### Exact new bottleneck

A sufficient next lemma is now considerably narrower:

> **Four-variable complete-output extraction lemma.**  
> For the four kernels (6.12), the four actual reconstructed numerator polynomials (6.6), and the common full target (6.13), construct an exact sparse, factorized, or observable prime-power extraction scheme. Prove resource bounds for the two complete sums (6.14)–(6.15), preserving the branch cancellations and all independent numerator shifts. Then evaluate to depths satisfying (7.2).

Unlike the previous open lemma, this one does not have to discover closure under unspecified finite-Schur or complete-force descendants. Those descendants are already reduced to explicit short polynomials.

---

## 9. Relation to the supplied literature and obstructions

The following distinctions remain essential.

- The fixed rational lifts and their common weight-marker simplification are accepted inputs. The additional reduction here uses the **same $n$** in both contact branches and the weight polynomial, after the complete finite inversion has been assembled.
- Rational/diagonal prime-power extraction and Cartier methods are established background. They do not by themselves establish a feasible module for (6.14)–(6.15).
- The squared-binomial metric here has not been identified with a standard full Hahn measure. The cutoff is enforced by the actual analytic first column and the coefficient target.
- Creative-telescoping existence and order bounds do not evaluate these original high coefficients or pay their prime-power singularities.
- Item 216 proves a first-order Gosper obstruction for its particular phase-dependent summand. It neither proves nor disproves a telescoper or modular quotient for the four kernels above.
- Item 232’s incomplete-binomial identities are valid at their stated parameter and endpoint scopes. They do not supply a neighboring-index condition or a relative norm law for the present family.

No exhaustive novelty or literature-search claim is made.

---

# Part IV. A bounded exact calculation for the coordinator

## 10. Numerator-construction and finite-gluing certificate

The following is a new bounded calculation. It does **not** redo the completed Schur calculation.

### 10.1 Inputs

1. The exact original $b,n$, with $M=20$, $m=76$.
2. The supplied $\lambda_s,c_s$ and the supplied $S^{-1}$.
3. The original $\overline K$, or its already defined bounded-entry formula.
4. The complete actual residues
   

$$
f_0,\ldots,f_{47}\pmod{2^{20}}.
$$


   These must come from the accepted complete first-force producer. They cannot be inferred from the four thirteen-bit initial pairs in A5turn16.
5. The factorial loads
   

$$
v_t=\prod_{h=1}^t(b+h),\qquad0\le t\le23.
$$



### 10.2 Exact mathematical specification

Perform the following operations over $\mathbb Z/2^{20}\mathbb Z$.

1. Form $u^{\rm out}$ and $h^{\rm out}$ by (2.3)–(2.4).
2. Form the short polynomials $P_r=P_{\le r}(1-z)^n$ for $0\le r\le99$.
3. Construct $F_f$ by (4.4).
4. Implement $\Psi$ using:
   - the exact prefix subtraction (3.3);
   - the integral action (5.5);
   - polynomial accumulation by the resulting exponent of $1-z$.
5. Apply the supplied $S^{-1}$ to the two endpoint right-hand sides in (4.2).
6. Assemble $G_f,G_e^*$ by (4.6) and (4.8).
7. Normalize them to (5.2), producing all four complete polynomial coefficient lists.
8. Form all four reconstructed polynomials by (6.6).
9. Independently verify the first $152$ nonnegative coefficients of the constructed responses using the finite convolution definitions and the same supplied Schur action.
10. Verify every principal-part coefficient:
    

$$
P_{<0}G_f=0,\qquad
    P_{<0}G_e^*=B_v.
$$


11. Verify the reconstructed endpoint identities, including
    

$$
[z^0]\widehat G_e
    =-b[z^0]G_e^{\rm an}-1.
$$



No $b$-row array is needed.

### 10.3 Resource bounds

For the symbolic band action,


$$
\sum_{s=0}^{76}(s+1)=3003.
$$


The four required band applications have first-branch polynomial lengths bounded respectively by


$$
48,\quad76,\quad100,\quad76.
$$


Thus formula (5.5) generates at most


$$
3003(48+76+100+76)=900900
$$


first-branch term contributions before collecting powers of $1-z$.

Collecting first by derivative exponent and then multiplying by the bounded powers of $1-z$ avoids expanding a new polynomial for each contribution.

A conservative direct implementation fits within:

- $10^8$ modular additions and multiplications;
- fewer than $10^6$ stored residue slots;
- no linear operation in $b$;
- no integer factorial of order $n$ or $b$.

For the stated independent prefix check, all binomial lower indices can be bounded by


$$
L_0+(2m-1)=176+151=327.
$$


An exact streamed small-lower-index recurrence therefore needs temporary integers of fewer than approximately $24{,}000$ bits, not original-size factorials. A valuation/odd-unit implementation is also possible.

These are bounds for the **numerator-construction certificate**, not for the remaining high coefficient extraction.

### 10.4 Expected verifiable output

The receipt should include:

- the complete four contact polynomials, within the degree bounds (5.3);
- the complete four reconstructed polynomials, within (6.8);
- the two endpoint right-hand sides and their products with the supplied $S^{-1}$;
- all zero residuals for the newly generated source-response prefixes;
- all zero principal-part residuals;
- the explicit exterior-endpoint identity;
- the four rational-kernel records and their full coefficient target.

It should state plainly:


$$
\texttt{original\_weighted\_Gram\_pair\_computed = false}
$$


unless (6.14) and (6.15) have actually also been evaluated.

No particular value or nonzero residue for either Gram output is predicted here.

---

# Part V. Global arithmetic and proof status

## 11. The full gcd and the actual primitive denominator remain unchanged

Nothing in the compression divides out an actual row content or replaces the final gcd by its binary part.

Retain the least actual two-column clearer $d_B$, the complete integer columns $N_{B,1},N_{B,2}$, and


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2}.
$$


The final reduction is still


$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
q_n=\frac{A_B}{g_B},\qquad
p_n=\frac{H_B}{g_B}.
}
\tag{11.1}
$$


The primitive multiplier is


$$
\frac{d_B^2}{g_B}.
$$


Every prime in $g_B$ matters.

The retained binary denominator interface is


$$
v_2(q_n)=
\max\left\{
0,\frac{3n}{2}-v_2(b!)-s_2(n)-1-(\gamma-\alpha)
\right\}.
$$


If the actual raw valuations are eventually certified, then


$$
\alpha=d_0-2,\qquad \gamma=e_0-3,
$$


so


$$
\gamma-\alpha=e_0-d_0-1.
$$


This is an interface, not an evaluated original-family law.

### 11.1 Whole evaluated error

Under the accepted complete signed-error theorem,


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi)<0
$$


eventually, and


$$
\log|\epsilon_n|
=
-\left(2+\frac1{4002}\right)n\log(1+\sqrt2)+o(n).
$$


The relevant quantity remains the whole same-index form


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n>0
}
\tag{11.2}
$$


eventually.

For this route to prove irrationality, one still needs an infinite original subsequence on which the **actual primitive denominator** makes (11.2) tend to zero. For example, a bound


$$
\log q_n
\le
\left(
\left(2+\frac1{4002}\right)\log(1+\sqrt2)-\delta
\right)n
$$


with some $\delta>0$ would suffice together with the accepted whole-error theorem and nonvanishing. No such all-prime denominator bound is proved here.

---

## 12. Proof-status ledger

| Item | Status |
|---|---|
| Original $u=0$, twenty-bit endpoint Schur matrix and inverse | Supplied finite certificate; reused, not recomputed |
| Earlier fixed rational lifts and common weight marker | Accepted inputs |
| Complete exponential force as an exterior-column load of the same operator | **Proved here** |
| Exact bulk generating function (3.8), including its entire principal part | **Proved here** |
| Finite signed-reversal band action with all shifts and endpoint zeros | **Proved here from the accepted band inverse** |
| Application of the supplied Schur inverse to the complete producers | Exact specification given |
| Two-branch normal form for both complete contact responses | **Proved here** |
| Explicit preservation of the reconstructed $j=b$ exterior term | **Proved here** |
| Four-variable identities for the actual squared-weight norm and complete exponential mixed output | **Proved here** |
| Bounded construction of all numerator polynomials | Exact specification and resource bounds given; not executed |
| Practical sparse/factorized/observable extraction of the original high coefficients | Open |
| Original $D_{\rm raw},E_{\rm raw}$ residues and first nonzero digits | Not computed |
| Actual contents and norm-relative output after guard digits | Not certified |
| Original-family relative-output law | Not proved |
| Full gcd, actual primitive denominator, and whole-error comparison | Open |
| Unconditional rationality or irrationality of $e+\pi$ | Unresolved |

---

## Conclusion

The new result is an exact reduction of the **complete original weighted-output problem**, rather than another operator-only certificate.

The complete exponential second force is first compressed to an exterior load of width $24$, whose finite response needs exterior transfers only through index $99$. The supplied Schur inverse then produces two contact generating functions in a common two-branch form. Their actual reconstruction—including the exterior $+1$—leads to the explicit four-variable contraction identities (6.14)–(6.15).

The immediate mathematical bottleneck is now:



$$
\boxed{
\text{Evaluate those four-variable complete-output coefficients
at the true norm-sensitive precision.}
}
$$



The bounded calculation presently warranted is the construction and independent finite verification of the complete numerator polynomials specified in Section 10. It uses the already supplied endpoint inverse and does not reopen that completed task.

Even a successful original twenty-bit Gram evaluation would leave two further obligations: a family-level relative theorem where needed, and all-prime control of the actual primitive denominator against the same-index whole nonzero error.



$$
\boxed{\text{The rationality or irrationality of }e+\pi
\text{ remains unconditionally unresolved.}}
$$


