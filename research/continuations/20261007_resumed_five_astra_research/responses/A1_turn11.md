> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A uniform Frobenius obstruction in the remaining adjacent window

## Abstract

The once-divided endpoint-annihilator cannot become invertible in any of the remaining original subwindows


$$
\frac19\le \frac{N_0}{P_0}<\frac15.
$$



The obstruction comes from the **original low ternary digits**, not from a generic singularity assertion for Hankel matrices. The original congruence $r\equiv2\pmod9$, together with $r$ odd, forces a common Frobenius syzygy in both kinds of equal residue-sector blocks of the complete tail matrix. There are $241$ such sectors. The one unequal sector pair supplies an additional radical direction. Consequently the complete tail matrix has nullity at least $242$, and its restriction to the prescribed endpoint-annihilator has nullity at least $241$:


$$
\boxed{\dim_{\mathbb F_3}\ker\mathcal W\ge241,\qquad
\operatorname{rank}_{\mathbb F_3}\mathcal W\le L-241.}
$$



This is a uniform obstruction throughout the remaining window, including every sufficiently large original tuple there. It explicitly includes the factor $(y+1)^2$: that factor represents restriction to the actual alternating endpoint’s kernel, and restriction can remove at most one of the $242$ radical directions constructed below.

The proof evaluates a guaranteed kernel, rather than claiming that the entire kernel has constant dimension. Additional Frobenius degeneracies can increase the nullity. No exact equality for the total nullity is needed to rule out every proposed once-divided unit window.

The result does **not** evaluate the actual higher bordered scalar. Its transport to the actual first radical digit retains precisely the turn9 mixed-divisibility hypothesis under independent review. No precision-$29$ producer transport is assumed.

---

## 1. Original objects and scope

Retain the original indices and inequalities:


$$
j>0,\qquad j\equiv84645\pmod{531441},
$$




$$
m=2^{2j-1},\qquad n=4^j+1,\qquad A=4^j-1=2m-1,
$$




$$
H=3^{h-1},\qquad D=H-A,
$$




$$
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15}.
$$



The finite coordinates remain


$$
U_u=(y-1)^u\quad(0\le u<D),
$$




$$
z_i=(y-1)^Dy^i\quad(0\le i<\nu),
\qquad \nu=\frac D2-1,
$$




$$
Y_b=y^b\quad(d\le b\le m),
\qquad d=D+\nu.
$$


In particular, the physical HIGH terminal remains $Y_m$.

The complete core functional is


$$
G_c(f,g)=\mathcal M(Q_cfg),
\qquad
Q_c=(y+1)(y-1)^A(\beta+3y),\quad \beta=-71-A,
$$


where


$$
\mathcal M(P)=
-\frac{3^h}{4}\mathfrak f(P)
+
3^h\sum_{v=0}^{2n-2}
\frac{[y^v](P-P(-1))/(y+1)}{2v+1},
\qquad
\mathfrak f(y^t)=(2t)!.
$$


The finite denominator cutoff is unchanged:


$$
2v+1\le4H-4D+5.
$$



In the adjacent window write


$$
P=3^{h-32},\qquad P_0=243P,\qquad N_0=243r,
\qquad D=P_0+N_0.
$$


The original integer $r$ is not freely chosen. In particular,


$$
r\equiv2\pmod9,\qquad r\text{ odd},
$$


and


$$
4^j=243(3^{26}-1)P-243r+1.
$$



We investigate the original tuples satisfying


$$
\frac19\le\frac rP<\frac15.
\tag{1.1}
$$


Every assertion below is restricted to original tuples satisfying all the preceding conditions. Nothing enlarges the original domain merely because the finite-field argument also works for some auxiliary tuples.

### Reused results

The completed second jet and divided-tail evaluation from turn10 are reused:


$$
F_i\equiv
(y-1)^D\left(
y^i-3\delta_{i,\nu-1}q_d
-9y^{H/3+i}
+9\delta_{i,\nu-1}q_{d+1}
\right)\pmod{27},
$$


with the actual monic quotients


$$
y^b=r_b+(y-1)^Dq_b,\qquad \deg r_b<D.
$$



The complete total-order-two contribution and all higher contributions relevant at precision $28$ have already been paid. In particular,


$$
G_c(\Delta_i,\Delta_j)\in3^{24}\mathbb Z_3,
\qquad
\Delta_i=\frac{F_i-T_i}{9}.
$$


Neither that calculation nor the ranks below $1/9$ are repeated.

Set


$$
R_*=\frac{P_0+1}{2},\qquad
\tau=\frac{N_0-3}{2},\qquad
L=\tau-1=\frac{N_0-5}{2},
$$


and


$$
C=\frac{P_0/3-3}{2}.
$$


The complete normalized core tail is


$$
V_{uv}=[y^{C-u-v}](y-1)^{N_0},
\qquad 0\le u,v<\tau,
\tag{1.2}
$$


and the endpoint-annihilating restriction is


$$
\mathcal W_{uv}
=[y^{C-u-v}](y+1)^2(y-1)^{N_0},
\qquad 0\le u,v<L.
\tag{1.3}
$$



The new task is therefore a finite-field rank problem for these exact finite matrices.

---

## 2. The exact $243$-sector decomposition of the tail

Put


$$
a=\frac{r-1}{2},\qquad K=\frac P3,\qquad T=\frac{K-1}{2}.
$$


Then


$$
\tau=243a+120,\qquad C=243T+120.
\tag{2.1}
$$



Over $\mathbb F_3$,


$$
(y-1)^{N_0}=(y^{243}-1)^r.
$$


Write a tail coordinate as


$$
u=243i+\alpha,\qquad 0\le\alpha<243.
$$


Its sector length is


$$
n_\alpha=
\begin{cases}
a+1,&0\le\alpha\le119,\\
a,&120\le\alpha\le242.
\end{cases}
\tag{2.2}
$$



An entry of $V$ can be nonzero only if


$$
\alpha+\beta\equiv120\pmod{243}.
$$


There are exactly two possibilities.

### Lower residue sum

For


$$
\alpha+\beta=120,
$$


the sector block is


$$
[z^{T-i-j}](z-1)^r.
\tag{2.3}
$$



The pair $0\leftrightarrow120$ is unequal, with dimensions


$$
(a+1)\times a.
$$


The remaining residues $1,\ldots,119$ give $119$ equal sectors of length $a+1$.

### Upper residue sum

For


$$
\alpha+\beta=363,
$$


the block is


$$
[z^{T-1-i-j}](z-1)^r.
\tag{2.4}
$$


These are the $122$ sectors with residues $121,\ldots,242$, all of length $a$.

Thus the complete tail consists of:

* $119$ equal sectors of size $(r+1)/2$, with coefficient index $T$;
* $122$ equal sectors of size $(r-1)/2$, with coefficient index $T-1$;
* one unequal symmetric pair of total size $2a+1$.

These counts include the shortened finite sectors. No periodic extension of the matrix has been made.

---

## 3. A common low-digit Frobenius syzygy

The essential original congruence is


$$
r=9k+2,
\tag{3.1}
$$


where $k$ is odd because $r$ is odd.

For sufficiently large original tuples, $K$ is an odd multiple of $9$. Define


$$
A_0=\frac{K-9}{18},\qquad B_0=2k-A_0,
\qquad d_0=\frac{3k-1}{2}.
\tag{3.2}
$$



The following construction uses only elementary dimension counting and Frobenius. It does not invoke a generic nonsingularity theorem.

### 3.1 Verification of the degree inequalities

From (1.1),


$$
\frac K3\le r<\frac{3K}{5}.
$$


Equality $r=K/3$ is impossible for sufficiently large tuples, since $K/3$ is divisible by $9$, whereas $r\equiv2\pmod9$. Since both are odd,


$$
r\ge\frac K3+2.
$$


Therefore


$$
K\le3r-6,
$$


which is equivalent to


$$
A_0\le d_0.
\tag{3.3}
$$



Also,


$$
B_0\le d_0
\quad\Longleftrightarrow\quad
K\ge r+16.
$$


This holds uniformly for sufficiently large tuples because $r<3K/5$. Finally,


$$
k\le d_0
$$


for $k\ge1$.

Thus $A_0,B_0,k$ are positive and no larger than $d_0$, for all sufficiently large original tuples in (1.1).

### 3.2 Existence of the syzygy

Let $X,Y$ be auxiliary homogeneous variables and put $Z=X+Y$. Consider


$$
U X^{A_0}+V_0Y^{B_0}+W_0Z^k=0
\tag{3.4}
$$


in total degree $d_0$.

The space of possible triples $(U,V_0,W_0)$ has dimension


$$
(d_0-A_0+1)+(d_0-B_0+1)+(d_0-k+1),
$$


whereas the target homogeneous space has dimension $d_0+1$. Since


$$
A_0+B_0+k=3k,\qquad 2d_0=3k-1,
$$


the difference is exactly


$$
2d_0-3k+2=1.
$$


Hence a nonzero syzygy (3.4) exists.

Moreover,


$$
W_0\ne0.
\tag{3.5}
$$


Indeed, a relation between $X^{A_0}$ and $Y^{B_0}$ alone has total degree at least


$$
A_0+B_0=2k>d_0.
$$



This is an explicit finite construction: $W_0$ is obtained from the kernel of the displayed homogeneous coefficient map. Its existence and its nonzero third component have been proved, rather than postulated.

---

## 4. The two equal-sector kernels

We now lift the same syzygy to both types of actual sectors.

### 4.1 Exact selected-map correspondence

For a signed Hankel block


$$
[z^{S-i-j}](z-1)^r,\qquad 0\le i,j<n,
$$


diagonal sign changes reduce it to the unsigned binomial block. Row reversal then identifies it with multiplication by $Z^r$:


$$
\left(\mathbb F_3[X,Y]/(X^\alpha,Y^\beta)\right)_{n-1}
\longrightarrow
\left(\mathbb F_3[X,Y]/(X^\alpha,Y^\beta)\right)_{n+r-1},
\tag{4.1}
$$


where


$$
\alpha=S+1,\qquad \beta=r+2n-\alpha.
\tag{4.2}
$$


Indeed, the surviving target $X$-exponents are precisely


$$
S-n+1,\ldots,S.
$$


This verifies both finite boundaries.

### 4.2 Sectors of length $(r+1)/2$

Here


$$
n_+=\frac{r+1}{2},\qquad S=T,
$$


so


$$
\alpha_+=\frac{K+1}{2}=9A_0+5,
\qquad
\beta_+=2r+1-\alpha_+=9B_0.
\tag{4.3}
$$



Raise (3.4) to the ninth power. Frobenius gives


$$
U^9X^{9A_0}+V_0^9Y^{9B_0}+W_0^9Z^{9k}=0.
$$


Multiplying by $X^5Z^2$ produces a syzygy of


$$
X^{\alpha_+},\quad Y^{\beta_+},\quad Z^r
$$


whose coefficient on $Z^r$ is


$$
\boxed{F_+=X^5W_0^9.}
\tag{4.4}
$$



Its total degree is


$$
9d_0+7=\frac{3r-1}{2}=n_++r-1.
$$


Consequently


$$
\deg F_+=n_+-1.
$$


Since $W_0\ne0$, this supplies a nonzero kernel vector in every one of the $119$ equal sectors of this type.

### 4.3 Sectors of length $(r-1)/2$

Now


$$
n_-=\frac{r-1}{2},\qquad S=T-1,
$$


and


$$
\alpha_-=\frac{K-1}{2}=9A_0+4,
\qquad
\beta_-=2r-1-\alpha_-=9B_0-1.
\tag{4.5}
$$



Multiply the ninth-power syzygy instead by $X^4Z^2$. Its $Y$-term remains divisible by $Y^{9B_0-1}$, and its coefficient on $Z^r$ is


$$
\boxed{F_-=X^4W_0^9.}
\tag{4.6}
$$


The total degree is


$$
9d_0+6=\frac{3r-3}{2}=n_-+r-1.
$$


Thus $F_-$ gives a nonzero kernel vector in each of the $122$ equal sectors of the second type.

These vectors are genuine finite-sector vectors. The source degree is less than both truncation exponents, so none is killed merely by passing to the source quotient.

---

## 5. Uniform rank obstruction, including the endpoint

### Theorem 5.1 — Complete tail obstruction

For every sufficiently large original tuple satisfying


$$
\frac19\le\frac{N_0}{P_0}<\frac15,
$$


the complete tail matrix (1.2) satisfies


$$
\boxed{\dim\ker V\ge242.}
\tag{5.1}
$$



#### Proof

The equal sectors supply $119+122=241$ independent radical vectors: each is supported in its own source residue sector and is killed by the only block with which that sector pairs.

The unequal pair has block form


$$
\begin{pmatrix}
0&B\\
B^T&0
\end{pmatrix},
\qquad B\in M_{a+1,a}(\mathbb F_3).
$$


Its rank is $2\operatorname{rank}B\le2a$, whereas its dimension is $2a+1$. It therefore supplies at least one further independent radical direction. ∎

### The actual endpoint restriction

The endpoint on the original tail is


$$
\epsilon(\xi)
=(-1)^{R_*}\sum_{u=0}^{\tau-1}(-1)^u\xi_u.
$$


Its kernel is exactly the image of the injective adjacent-sum map


$$
H_{\rm end}:\mathbb F_3^L\longrightarrow\mathbb F_3^\tau,
\qquad
e_u\longmapsto e_u+e_{u+1}.
\tag{5.2}
$$


The complete restriction is


$$
H_{\rm end}^TVH_{\rm end}=\mathcal W.
\tag{5.3}
$$


Equation (5.3) is precisely the origin of the factor $(y+1)^2$ in (1.3).

Let $\mathcal K\subseteq\ker V$ be the $242$-dimensional subspace constructed above. Then


$$
\dim(\mathcal K\cap\ker\epsilon)\ge241.
$$


Every vector in that intersection has a unique preimage under $H_{\rm end}$, and (5.3) kills that preimage. Therefore:

### Corollary 5.2 — No remaining once-divided unit window



$$
\boxed{
\dim\ker\mathcal W\ge241,\qquad
\operatorname{rank}\mathcal W\le L-241.
}
\tag{5.4}
$$



In particular, there is **no specified infinite original subwindow** inside (1.1) on which the once-divided endpoint-annihilator is invertible.

This is not an exact formula for its entire nullity. It is an exact, constructive, uniform obstruction sufficient to settle the proposed invertibility alternative. Any further degeneracy at larger Frobenius scales only strengthens it.

Combined with the already evaluated ranges below $1/9$, the proposed one-step unit criterion has no sufficiently-large-original-tuple escape anywhere in the adjacent domain under investigation.

---

## 6. Actual transport: the precise conditional consequence

The core theorem above is independent of the producer. Its actual consequence uses, and does not strengthen, the turn9 transport package.

That package includes


$$
S_{\rm act}=S_c+3^6\Phi_R-3^{13}\mathcal Q,
\qquad
\mathcal Q\in3^{21}M,
$$


and obtains


$$
\Phi_R\in3^{22}M
$$


using the separately retained actual mixed observation


$$
T=\bigl(\mathcal M(\mathscr R\,wF_i)\bigr)\in3M.
$$


Only at that scope does it give


$$
S_{\rm act}-S_c\in3^{28}M.
$$



Partition


$$
U=-S_{\rm act}/3^{26}
=
\begin{pmatrix}
\mathsf A&\mathsf B\\
\mathsf B^T&\mathsf C
\end{pmatrix}
$$


into the unit prefix and original radical tail. Retain


$$
\mathcal R=\mathsf C-\mathsf B^T\mathsf A^{-1}\mathsf B,
$$




$$
f=e_R-\mathsf B^T\mathsf A^{-1}e_C,
\qquad
\lambda=3^{26}d_{\rm act}-e_C^T\mathsf A^{-1}e_C.
$$


The diagonal is complete.

At the stated transport scope,


$$
\overline{\mathcal R/3}=-V.
$$


The exact $f$-annihilating integral basis reduces to (5.2). Consequently its once-divided block reduces to $-\mathcal W$, and is singular by (5.4).

Thus the hypothesis


$$
M=3\mathsf W,\qquad \det\mathsf W\in\mathbb Z_3^\times
$$


of the earlier relative-cofactor lemma fails in the remaining window as well.

No precision-$29$ transport has been used or proved here.

---

## 7. Scale: what the new obstruction does and does not buy

### 7.1 The independently defined remaining scalar

If the exact endpoint-annihilating block $M$ is invertible over $\mathbb Q_3$, use the actual endpoint-adapted basis to write


$$
\mathcal R'=
\begin{pmatrix}
a_0&w^T\\
w&M
\end{pmatrix}.
$$


Define, independently of any desired valuation,


$$
\sigma=a_0-w^TM^{-1}w.
\tag{7.1}
$$


When $\sigma\ne0$, put


$$
\kappa_\sigma=v_3(\sigma).
$$



The exact determinant identities are


$$
D_0=\det\mathsf A\,\det M\,\sigma,
$$




$$
D_1=\det\mathsf A\,\det M\,(f_0^2-\lambda\sigma).
\tag{7.2}
$$


Hence


$$
v_3D_1-v_3D_0
=
v_3(f_0^2-\lambda\sigma)-v_3(\sigma).
\tag{7.3}
$$



The common determinant depth cancels **exactly**, regardless of how large the radical dimension is. If additional hypotheses establish $\sigma\in3\mathbb Z_3$, then $f_0$ unit and $\lambda$ integral imply


$$
v_3D_1-v_3D_0=-\kappa_\sigma.
$$


But the once-divided lemma no longer supplies those hypotheses. In particular, singularity of $M/3\bmod3$ does not determine $\sigma$, its integrality, or its nonvanishing.

### 7.2 Exact primitive-denominator comparison

At the retained scope of the actual primitive-ratio identity,


$$
v_3(q)=
\max\!\left(
0,\,
h-26+v_3Q_{\rm loc}(-1)+v_3D_1-v_3D_0
\right).
\tag{7.4}
$$



Suppose a valid actual scalar calculation eventually supplied


$$
v_3D_1-v_3D_0=-k.
$$


With


$$
b=h-26+v_3Q_{\rm loc}(-1),
$$


the ternary exponent would become


$$
\max(0,b-k).
$$


Relative to $\max(0,b)$, the saving is exactly


$$
\max(0,b)-\max(0,b-k),
\tag{7.5}
$$


and is at most $k$ for $k\ge0$.

Thus a bounded number of scalar digits gives at most a bounded factor $3^k$, not a factor exponential in $\tau$. This conclusion concerns the actual denominator formula, not an informal comparison of determinant sizes.

The present theorem proves additional common divisibility. It proves **no growing bound for (7.3)**. Neither the producer seed nor an all-prime cofactor argument in the supplied material supplies such a bound.

Accordingly, the stream needs either:

1. a growing quantitative estimate for the actual endpoint-observed scalar ratio (7.3); or
2. an independent growing all-prime content/gcd mechanism; or
3. a stronger whole-error estimate sufficient without the missing primitive saving.

The new obstruction does not prove that these mechanisms are impossible. It proves that fixed-depth common-radical calculations do not furnish them.

---

## 8. The next local obligation and its payments

A concrete follow-on lemma should evaluate the next actual digit on a specified surviving subspace from Theorem 5.1, after all complementary nondegenerate directions have been eliminated.

It must include:

* the actual endpoint lift $f$;
* the complete diagonal $\lambda$;
* the prefix correction $\mathsf B^T\mathsf A^{-1}\mathsf B$;
* elimination of a first-radical block whose inverse costs $3^{-1}$;
* the producer contribution
  

$$
3^6\Phi_R,
$$


  which can contribute modulo $3^{29}$, since the retained bound is only $\Phi_R\in3^{22}M$;
* any further inverse payment required by the surviving radical.

The old payments


$$
E_c^{-1},E_{\rm act}^{-1}\in3^{-1}M
$$


do not pay these new inverses.

The useful target is not merely another matrix definition. It is a proved statement about the actual scalar, for example a nonvanishing theorem and a growing lower bound for


$$
v_3(\sigma)-v_3(f_0^2-\lambda\sigma),
$$


together with the integrality and invertibility hypotheses needed to define the displayed terms.

No such quantitative scalar lemma is established here.

---

## 9. Complete forcing and global arithmetic retained

The actual columns remain


$$
F_{\rm act}=Z-WE_{\rm act}^{-1}C_{\rm act}.
$$



The producer seed remains the recovered complete identity


$$
3P_n-Q_c=3^7\mathscr R
=\sum_{a=0}^{A+1}e_a(y-1)^a,
$$




$$
e_a=-\frac{(A+1)!}{a!}(t_a+\xi v_a),
$$


with


$$
t=3nh_{\rm vec}
+(b_{\rm force}+6)e_{n-1}
+\frac{2b_{\rm force}}{n-1}e_{n-2},
\qquad b_{\rm force}=-n-66.
$$


The upper endpoint $A+1$, the signed scalar $\xi$, and its previously paid common division are unchanged.

The complete return remains


$$
J^T\varepsilon+\omega
=
-\varepsilon-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
$$


No forcing, boundary charge, exterior constant, or physical-terminal term is omitted.

The actual column contents and least simultaneous clearer have not been reevaluated in this report. They must remain their original exact values, not substitute upper bounds. Write


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$




$$
g_\ell=\gcd(|A_\ell|,|B_\ell|)
$$


over **all primes**.

For $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},
\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell}.
$$


The whole error is


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}
{g_\ell}\det H_{\rm complete}.
}
\tag{9.1}
$$



In particular,


$$
-\log|q(e+\pi)-p|
=
\log g_\ell-(m+1)\log\ell_{\rm clr}
-\log|\det H_{\rm complete}|.
\tag{9.2}
$$


A bounded additional gcd contribution changes the right side by only a bounded amount. It cannot overcome a deficit tending to infinity.

An irrationality conclusion still requires, at the **same infinite original indices**,


$$
B_\ell\ne0,\qquad \det H_{\rm complete}\ne0,
$$


and divergence of (9.2) to $+\infty$. No part of the new rank obstruction supplies these conditions. No gain is combined with a different binary or prime-$29$ family.

---

## 10. A bounded new arithmetic audit

No large original matrix or closed producer calculation is needed.

An auxiliary instance in the newly treated range is


$$
P=243,\qquad r=29.
$$


It satisfies


$$
r\equiv2\pmod9,\qquad r\text{ odd},\qquad
\frac19<\frac{29}{243}<\frac15.
$$


It is **not** asserted to arise from an original pair $(j,h)$.

The derived inputs are


$$
K=81,\quad k=3,\quad A_0=4,\quad B_0=2,\quad d_0=4.
$$


A concrete syzygy is


$$
-X^4-XY\cdot Y^2+X(X+Y)^3=0
\qquad\text{over }\mathbb F_3.
$$


Thus $W_0=X$, and the constructed kernel polynomials are


$$
F_+=X^{14},\qquad F_-=X^{13}.
$$



### Expected verifiable outputs

1. The $15\times15$ signed coefficient block
   

$$
[z^{40-i-j}](z-1)^{29}
$$


   kills the vector corresponding, after the specified sign change, to $X^{14}$.

2. The $14\times14$ block
   

$$
[z^{39-i-j}](z-1)^{29}
$$


   kills the vector corresponding to $X^{13}$.

3. The unequal $15\times14$ block has a symmetric-pair nullity of at least one.

4. The sector counts are $119$, $122$, and one unequal pair.

5. With
   

$$
N_0=7047,\qquad \tau=3522,\qquad L=3521,
$$


   the resulting complete endpoint-annihilator has
   

$$
\dim\ker\mathcal W\ge241,\qquad
   \operatorname{rank}\mathcal W\le3280.
$$



Only the two small coefficient blocks and the displayed syzygy need inspection. The large restricted matrix need not be built. No computation has been executed here; its finite result would audit only this auxiliary instance.

---

## 11. Proof-status ledger

| Statement | Status |
|---|---|
| Complete second jet and divided core-tail formula | Reused turn10 results |
| Exact finite $243$-sector decomposition in the remaining window | Proved here |
| Common original-low-digit Frobenius syzygy | Proved here by dimension counting |
| Nonzero kernel vector in each of the $241$ equal sectors | Proved here |
| Complete tail nullity at least $242$ | Proved here |
| Complete endpoint-annihilator nullity at least $241$, including $(y+1)^2$ | Proved here |
| No once-divided unit subwindow in $1/9\le N_0/P_0<1/5$ | Proved for the core; actual consequence at the stated transport scope |
| Exact total nullity beyond this guaranteed kernel | Not claimed |
| Precision-$29$ producer-aware observation | Open |
| Actual scalar noncancellation and growing relative gain | Open |
| All-prime gcd and nonzero whole-error comparison | Open |
| Rationality or irrationality of $e+\pi$ | Unresolved |

## Conclusion

The new evaluated result is the uniform obstruction


$$
\boxed{
\dim\ker\mathcal W\ge241
\quad\text{throughout}\quad
\frac19\le\frac{N_0}{P_0}<\frac15
}
$$


for every sufficiently large original tuple. It comes from an explicit common Frobenius syzygy forced by $r\equiv2\pmod9$, with all finite residue-sector boundaries and the actual endpoint restriction retained.

Therefore **none of the remaining original subwindows makes the once-divided endpoint-annihilator invertible**. Together with turn10, this closes the proposed one-step-unit escape across the adjacent window.

The exact remaining local bottleneck is a producer-aware higher-digit evaluation yielding actual scalar noncancellation or a quantitative relative-cofactor bound. The next step must pay its new inverses and retain $3^6\Phi_R$ at precision $29$.

The global bottleneck remains the same-index comparison of the **actual all-prime final gcd and primitive denominator** with the **nonzero whole evaluated determinant error**, after the unchanged actual contents and least simultaneous clearer.



$$
\boxed{\text{No unconditional proof of rationality or irrationality of }e+\pi
\text{ is obtained.}}
$$


