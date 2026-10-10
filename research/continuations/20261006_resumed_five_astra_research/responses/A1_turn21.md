> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A1 turn21 — Audit of the first-jet evaluator and evaluation of the next complete nonlinear digit

## Executive conclusion

The width-$350$ evaluator in turn20 survives the audit. Its finite Pascal identities, terminal support, block alignment, propagation bound, and dependence on $n\bmod 3^{11}$ are valid for the actual signed producer. One detail deserves clarification: the polynomial approximation to the moments should be constructed using integer representatives of the powers $(-2)^{-k}$ modulo $3^8$. This makes the claimed **integer-valued polynomial** literal, rather than merely a $\mathbb Z_3$-valued polynomial. The degree bound remains $41$.

No value of $c$ is inferred here. The coordinator’s pending scalar calculation remains the calculation that selects its branch, with the prescribed divisions.

The new mathematical advance is an evaluation of the **whole first digit of $\mathcal Q/9$**, including the actual HIGH inverse and LOW feedback:



$$
\boxed{\frac{\mathcal Q}{9}\equiv0\pmod3.}
$$



Thus, on the retained sufficiently large original window,



$$
\boxed{\mathcal Q\in27M_\nu(\mathbb Z_3),\qquad
S_{\rm act}\in3^{16}M_\nu(\mathbb Z_3).}
$$



This is not obtained by evaluating $c^2$ alone. The proof uses three additional facts established below:

1. **The actual second producer jet narrows to a cubic:**
   

$$
\boxed{
   R_{\rm prod}(y)\equiv
   c(y+1)x^A+
   3(y+1)x^{A-3}G(x)\pmod9,
   \qquad \deg G\le3.
   }
$$


2. **The actual HIGH inverse has the following boundary response:**
   

$$
\boxed{
   \widehat E_{\rm act}^{-1}e_{Y_m}
   \equiv4e_{Y_d}-3e_{Y_{d+1}}\pmod9.
   }
$$


3. **The next lower-edge HIGH source equals its LOW feedback**, so its contribution to the next quadratic contraction cancels.

The next endpoint numerator is also reduced substantially. Write


$$
G(x)=g_0+g_1x+g_2x^2+g_3x^3,
$$


and define


$$
\Pi_D=\sum_{a=0}^{D/2-1}\binom{3D/2-1}{a}\pmod3.
$$


Then, for every original residual index $0\le i<\nu$,


$$
\boxed{
\frac{(e_{\rm act}-e_c)_i}{3^7}
\equiv
-\mathcal E_G(i)+c\,\mathbf1_{i=\nu-1}\Pi_D
\pmod3,
}
$$


where


$$
\boxed{
\begin{array}{c|c}
i\bmod3&\mathcal E_G(i)\\ \hline
0&g_0+g_1+g_2\\
1&2g_0+2g_1+g_2\\
2&g_0+g_2
\end{array}}
$$



The three needed producer coefficients $g_0,g_1,g_2$ are bounded postprocessing outputs of the unit-matrix vectors already occurring in the pending width-$350$ calculation. They require **no new signed-producer solve and no repeated $\eta$-division**. An independent $62$-coordinate, three-term Pascal interface suffices to prove their locality.

The endpoint digit $\Pi_D$ is not replaced by a fixed residue of $n$. It has an explicit nine-state digit evaluation on the **actual** integer $D/2$. Consequently the endpoint formula is a bounded-state original-domain evaluation, not an assertion that all its values are constant on the progression.

The exact value of $\mathcal Q/9$ beyond its now-evaluated first digit, the full endpoint, the relative determinant-pair arithmetic, the all-prime gcd, and the whole nonzero primitive error remain unresolved.

---

# 1. Original domain and retained finite boundaries

Throughout, retain


$$
j>0,\qquad j\equiv84645\pmod{531441},
$$


and hence the original broader condition


$$
j\equiv81\pmod{243}.
$$


The parameters remain


$$
m=2^{2j-1},\qquad n=4^j+1,\qquad A=n-2=2m-1,
$$




$$
H=3^{h-1},\qquad D=H-A,
$$


with


$$
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15}.
$$



In particular,


$$
v_3(A)=5,\qquad v_3(D)=5
$$


for sufficiently large indices in this window.

The original spaces are unchanged:


$$
U_u=x^u\quad(0\le u<D),\qquad x=y-1,
$$




$$
z_i=x^Dy^i\quad(0\le i<\nu),
$$




$$
Y_b=y^b\quad(d\le b\le m),
$$


where


$$
d=\frac{3D}{2}-1,\qquad \nu=\frac D2-1.
$$



All statements below apply to the full residual block and therefore, in particular, to both selected original residual columns. No HIGH coordinate beyond $m$, no residual coordinate beyond $\nu-1$, and no residual moment beyond $D-4$ is introduced.

The complete functional remains


$$
\boxed{
\mathcal M(F)=
-\frac{3^h}{4}\mathfrak f(F)
+
3^h\sum_{v=0}^{2n-2}
\frac{[y^v](F-F(-1))/(y+1)}{2v+1},
\qquad
\mathfrak f(y^r)=(2r)!.
}
\tag{1.1}
$$



Its cutoff is exactly $2v+1\le4n-3$.

The accepted finite receipts retain only their stated finite scopes. None is rerun or promoted to an original-window inverse calculation.

---

# 2. Audit of the width-$350$ scalar evaluator

## 2.1 The factorial moment identity is exact

Turn5 gives


$$
\Lambda_r=
\sum_{k=0}^r
\binom rk(-2)^{r-k}(r+k)!,
\qquad \gamma_r=\frac{\Lambda_r}{r!}.
$$


Since


$$
\frac{(r+k)!}{r!}=k!\binom{r+k}{k},
$$


one obtains exactly


$$
\boxed{
\gamma_r=
\sum_{k=0}^r
k!\binom rk\binom{r+k}{k}(-2)^{r-k}.
}
\tag{2.1}
$$



Thus turn20’s identity (5.2) has the correct factorial normalization.

## 2.2 The degree-$41$ approximation is uniform for every $r\ge0$

Let $\ell_K$ be the least integer with $v_3(\ell_K!)\ge K$. In (2.1), all $k\ge\ell_K$ terms vanish modulo $3^K$.

For a literal integer-valued polynomial construction, choose integers $a_k$ satisfying


$$
a_k\equiv(-2)^{-k}\pmod{3^K}.
$$


Then


$$
P_K(r)=
\left(\sum_{\ell=0}^{K-1}(-3)^\ell\binom r\ell\right)
\left(
\sum_{k=0}^{\ell_K-1}
a_k\,k!\binom rk\binom{r+k}{k}
\right)
\tag{2.2}
$$


is integer-valued and satisfies


$$
P_K(r)\equiv\gamma_r\pmod{3^K}
\qquad(r\ge0).
$$



For $k>r$, $\binom rk=0$, so extending the truncated sum to its fixed upper limit causes no exception at small $r$. The exponent approximation


$$
(1-3)^r\equiv
\sum_{\ell=0}^{K-1}(-3)^\ell\binom r\ell\pmod{3^K}
$$


is likewise valid for every nonnegative integer $r$.

Its degree is at most


$$
2(\ell_K-1)+K-1.
$$


At $K=8$,


$$
\ell_8=18,\qquad \deg P_8\le41.
$$



Taking finite differences at $0$ therefore proves, uniformly for all $r\ge0$,


$$
\boxed{
\gamma_r\equiv
\sum_{k=0}^{41}c_k\binom rk\pmod{3^8},
\qquad
c_k=\sum_{s=0}^k(-1)^{k-s}\binom ks\gamma_s.
}
\tag{2.3}
$$



No finite computation at $r\le41$ is being used as an empirical extrapolation. The polynomial argument establishes the uniform scope.

## 2.3 The Pascal band is a finite-matrix identity

Let


$$
\mathsf P_{ij}=\binom ij,\qquad
\mathsf B_n=\mathsf P_n^{-1}\mathsf T_n\mathsf P_n^{-T}.
$$


The generating kernel calculation gives


$$
\frac{(z+w)^k}{(1-z-w)^{k+1}}
\longmapsto
\frac{(z+w+2zw)^k}{(1-zw)^{k+1}}.
$$


Hence


$$
(\mathsf B_n)_{ij}\equiv
[z^iw^j]\sum_{k=0}^{41}
c_k\frac{(z+w+2zw)^k}{(1-zw)^{k+1}}
\pmod{3^8}.
\tag{2.4}
$$



Every numerator monomial has difference between its two exponents at most $k$; the denominator adds equal exponents. Therefore


$$
|i-j|>41\quad\Longrightarrow\quad
(\mathsf B_n)_{ij}=0\pmod{3^8}.
$$



Lower triangularity of the Pascal transformations means that this infinite-kernel calculation restricts exactly to the original finite principal matrix. It does not replace the finite boundary.

## 2.4 The unit blocks are aligned correctly

Modulo $3$, Lucas decomposition gives the finite low-digit moment block


$$
M_3=
\begin{pmatrix}
1&0&1\\
0&2&0\\
1&0&0
\end{pmatrix}.
$$


Conjugating by the $3\times3$ lower Pascal matrix gives


$$
J_3=
\begin{pmatrix}
1&2&2\\
2&0&0\\
2&0&2
\end{pmatrix}.
$$


The high-digit Pascal factors cancel the corresponding $Z$-matrices.

Thus the transformed matrix is block diagonal modulo $3$ in consecutive triples, with the terminal principal block


$$
J_2=\begin{pmatrix}1&2\\2&0\end{pmatrix}
$$


because $n\equiv2\pmod3$.

Both are unit blocks. For the proposed suffix,


$$
n_0-L=86996-350=86646\equiv0\pmod3.
$$


Its left boundary is a genuine block boundary, and its right boundary retains the original shortened $2\times2$ block.

## 2.5 Inverse Pascal preserves the terminal support of $u$

The product of any $18$ consecutive integers has $3$-adic valuation at least $v_3(18!)=8$. Consequently


$$
u_a=0\pmod{3^8}\qquad(a<n-18).
$$


Since $\mathsf P_n^{-1}$ is lower triangular,


$$
\widehat u_i=(\mathsf P_n^{-1}u)_i=0\pmod{3^8}
\qquad(i<n-18).
$$



This is the correct direction of triangularity. No initial support is being mistaken for terminal support.

## 2.6 The identities for $h$ and $u^Th$ retain the finite next column

Write the Pascal matrix at order $n+1$ in block form:


$$
\mathsf P_{n+1}=
\begin{pmatrix}
\mathsf P_n&0\\
p^T&1
\end{pmatrix},
\qquad p_i=\binom ni.
$$


If


$$
b_i=(\mathsf B_{n+1})_{i,n},
$$


then the actual next moment column equals


$$
\mathsf P_n(\mathsf B_np+b).
$$


Therefore, exactly,


$$
\boxed{
h=\mathsf P_n^{-T}(p+\mathsf B_n^{-1}b),
}
\tag{2.5}
$$


and


$$
\boxed{
u^Th=\widehat u^T(p+\mathsf B_n^{-1}b).
}
\tag{2.6}
$$



These are turn20’s (6.5) and (6.7), with the finite endpoints intact.

## 2.7 The Neumann radius fits inside $350$

Let $\mathsf C$ be the aligned block-diagonal lift and


$$
\Delta=\mathsf B_n-\mathsf C\in3M.
$$


Then


$$
\mathsf B_n^{-1}\equiv
\sum_{r=0}^7(-\mathsf C^{-1}\Delta)^r\mathsf C^{-1}
\pmod{3^8}.
$$



The next-column vector $b$ has terminal width $41$. Applying $\mathsf C^{-1}$ enlarges support by at most $2$, and each subsequent $\mathsf C^{-1}\Delta$ enlarges it by at most $43$. Thus all required paths lie within terminal width


$$
41+2+7\cdot43=344.
$$



The suffix of length $350$ leaves a margin and begins at a complete block boundary. No contributing path reaches the artificial left edge.

## 2.8 The residue requirement is indeed $n\bmod3^{11}$

For $0\le k\le41$,


$$
\binom{x+3^{11}}k\equiv\binom xk\pmod{3^8}.
$$


By Vandermonde, the nonconstant terms contain $\binom{3^{11}}t$, whose valuation is at least


$$
11-\lfloor\log_3t\rfloor\ge8.
$$



All binomial lower indices in the band formula are at most $41$. The remaining terminal factors involve shorter products or binomial coefficients, and


$$
(-2)^a=(1-3)^a\bmod3^8
$$


depends only on $a\bmod3^7$.

Therefore the complete scalar evaluator depends only on


$$
n\bmod3^{11}
$$


once the original finite order exceeds the fixed interface width.

The supplied original tail gives


$$
n\equiv795584\pmod{3^{13}},
\qquad
n\equiv86996\pmod{3^{11}}.
$$



### Audit conclusion

The pending computation evaluates the actual signed-producer first scalar, not an auxiliary band model.

Its required division order remains unchanged:

1. compute $\eta,\chi$ modulo $3^8$;
2. divide both by $3$;
3. invert the resulting unit denominator modulo $3^7$;
4. assemble the whole top coefficient modulo $3^7$;
5. divide by $3^6$.

I do not infer its output.

---

# 3. A sharper actual producer jet modulo $9$

The next source calculation does not require an arbitrary eleven-coordinate jet.

Write


$$
3P_n-Q_c=\sum_{a=0}^{A+1}e_ax^a=3^6R_{\rm prod}.
$$


The exact coefficient formula is


$$
e_a=-\frac{F}{a!}(t_a+\xi_nv_a),
\qquad F=(A+1)!.
\tag{3.1}
$$



For indices below $A$,


$$
t_a=3nh_a.
$$



Turn20’s proved inverse formulas give


$$
v\equiv(z,2z,0)\pmod9,
\qquad
h\equiv(z,0,-z_{<N})\pmod3,
$$


where


$$
A=3N,\qquad v_3(N)=4,\qquad
z_i=(-1)^{N+i}\binom Ni.
$$



Consider the next terminal groups.

| Indices $a$ | $v_3(F/a!)$ | Additional established divisibility |
|---|---:|---|
| $A-1,A-2,A-3$ | $5$ | $h_a\in3\mathbb Z_3,\ v_a\in9\mathbb Z_3$ |
| $A-4,A-5,A-6$ | $6$ | $h_a\in3\mathbb Z_3,\ v_a\in9\mathbb Z_3$ |
| $A-7,A-8,A-9$ | $7$ | $v_a\in3\mathbb Z_3$ |

For the middle group, the relevant binomial is $\binom N2$, divisible by $3^4$. For the last group, the only additional case is $\binom N3$, whose valuation is $3$.

It follows that


$$
e_a\in3^8\mathbb Z_3
\qquad(a\le A-4).
\tag{3.2}
$$


Earlier indices are covered by the factorial saturation bound.

Together with the first-jet theorem and the actual endpoint divisibility, this proves:

## Theorem 3.1 — Actual cubic second jet

Choose any integral lift of $c\in\mathbb F_3$. Then there is a polynomial


$$
G(x)=g_0+g_1x+g_2x^2+g_3x^3\in\mathbb F_3[x]
$$


such that


$$
\boxed{
R_{\rm prod}(y)\equiv
c(y+1)x^A+
3(y+1)x^{A-3}G(x)\pmod9.
}
\tag{3.3}
$$



Changing the lift of $c$ changes only $g_3$. The coefficients $g_0,g_1,g_2$ are unambiguous.

This is a coefficient-value restriction for the actual producer, not merely the earlier factorial-support bound.

---

# 4. The actual HIGH inverse boundary response

Put


$$
q=m-d,
$$


and index the HIGH block by $b=d+s$, $0\le s\le q$.

Define the exact integral anti-triangular lift


$$
(K_0)_{bc}=
\begin{cases}
(-1)^{b+c-m-d}\binom A{b+c-m-d},&b+c\ge m+d,\\
0,&b+c<m+d.
\end{cases}
\tag{4.1}
$$



It has unit anti-diagonal. Its inverse is explicitly


$$
(K_0^{-1})_{bc}=
\begin{cases}
\displaystyle\binom{A+m+d-b-c-1}{m+d-b-c},
&b+c\le m+d,\\
0,&b+c>m+d.
\end{cases}
\tag{4.2}
$$



In particular,


$$
K_0^{-1}e_{Y_m}=e_{Y_d},
$$


and


$$
K_0^{-1}e_{Y_{m-1}}
=e_{Y_{d+1}}+Ae_{Y_d}.
\tag{4.3}
$$



Write


$$
\widehat E_{\rm act}
=E_{Y,\rm act}-3X_{\rm act}^TL_{\rm act}^{-1}X_{\rm act}
=K_0+3V.
\tag{4.4}
$$



We now evaluate the **whole column $Ve_{Y_d}$** modulo $3$.

## 4.1 LOW projection at the leading layer

Let


$$
r_b=\left(\binom ba\right)_{0\le a<D},
$$


the $x$-coefficient vector of $\operatorname{rem}_{x^D}y^b$.

The leading LOW/HIGH block satisfies


$$
\boxed{X_b\equiv Lr_b\pmod3.}
\tag{4.5}
$$



Indeed, the difference $y^b-\operatorname{rem}_{x^D}y^b$ is divisible by $x^D$. After multiplication by $x^{A+u}$, its leading-layer extraction is from $x^H$ times a polynomial of degree at most $b+u-D\le m-1<r_1$, where


$$
r_1=\frac{H-1}{2}.
$$


The extraction therefore vanishes.

This proves the actual LOW feedback identity, rather than presuming that feedback is absent.

## 4.2 Top pole, next pole, and feedback in the $d$-column

At the original finite cutoff, modulo $9$,


$$
\mathcal M(F)\equiv
[y^{r_*}]\mathcal D(F)+3[y^{r_1}]\mathcal D(F),
\qquad
r_*=\frac{3H-1}{2}.
$$



For $Q_c=(y+1)x^A(\beta+3y)$, the top-pole contribution to $E_{Y,bd}$ is:

- $0$, if $b\le m-2$;
- $3$, if $b=m-1$;
- $\beta-3A$, if $b=m$.

Since


$$
\frac{\beta-3A-1}{3}
=-24-\frac{4A}{3}\equiv0\pmod3,
$$


the divided top-pole correction is $e_{Y_{m-1}}$.

The next-pole term minus LOW feedback is


$$
[y^{r_1}]x^A
\left(y^{b+d}
-\operatorname{rem}_{x^D}y^b\,
 \operatorname{rem}_{x^D}y^d\right).
\tag{4.6}
$$


The polynomial in parentheses is divisible by $x^D$. After division its degree is at most


$$
b+d-D\le m+d-D=r_1.
$$


Equality occurs only at $b=m$, with leading coefficient $1$. Using $x^H=y^H-1$ modulo $3$, (4.6) is therefore $-\mathbf1_{b=m}$.

Consequently


$$
\boxed{
Ve_{Y_d}\equiv e_{Y_{m-1}}-e_{Y_m}\pmod3.
}
\tag{4.7}
$$



The factorial term vanishes at this evaluated precision by its factor $3^h$. The actual producer perturbation $3^6K$ also vanishes modulo $9$. Neither is removed from the exact definition of $\widehat E_{\rm act}$.

## Theorem 4.1 — Actual next HIGH boundary response

Expanding the unit inverse modulo $9$,


$$
\widehat E_{\rm act}^{-1}e_{Y_m}
\equiv
e_{Y_d}-3K_0^{-1}(e_{Y_{m-1}}-e_{Y_m}).
$$


Since $A\equiv0\pmod3$,


$$
\boxed{
\widehat E_{\rm act}^{-1}e_{Y_m}
\equiv4e_{Y_d}-3e_{Y_{d+1}}\pmod9.
}
\tag{4.8}
$$



In particular,


$$
\boxed{
(\widehat E_{\rm act}^{-1})_{mm}=0\pmod9.
}
\tag{4.9}
$$



The effective support is exactly contained in the first two HIGH coordinates at this precision. It is not obtained by truncating the original HIGH matrix.

---

# 5. The complete next mixed source

Write


$$
T_R=3T_1,\qquad T_1=\binom a b.
$$


The first-jet result gives


$$
a=3a',
\qquad
b\equiv-c\,e_{Y_m}e_{\nu-1}^T\pmod3.
$$



We evaluate $a'\bmod3$ and the lower-edge HIGH row $T_{R,Y_d}/9\bmod3$.

## 5.1 All poles needed modulo $27$

The original cutoff gives


$$
\begin{aligned}
\mathcal M(F)\equiv{}&
[y^{r_*}]\mathcal D(F)
+3[y^{r_1}]\mathcal D(F)\\
&+9\sum_{\alpha\in\{1,5,7,11\}}
\alpha^{-1}
[y^{(\alpha H/3-1)/2}]\mathcal D(F)
\pmod{27}.
\end{aligned}
\tag{5.1}
$$



The four displayed units are precisely the admissible valuation-$(h-2)$ denominators at this layer. The factorial term is zero modulo $27$ because $h$ is sufficiently large.

The complete-core columns satisfy


$$
F_i\equiv z_i-3\pi(y^d)\mathbf1_{i=\nu-1}\pmod9.
\tag{5.2}
$$



For LOW rows, the top pole is absent by the exact degree bound even with the full corrected column.

Substitute (3.3) into the other terms:

- the $c\,x^H$ contribution at the $3$-weighted pole vanishes modulo $9$, because $x^H\bmod9$ is supported on multiples of $H/3$, while the required index lies in the separated middle gap;
- the correction $-3\pi(y^d)$ contributes an $x^H$-multiple whose lower factor has degree $O(D)$, below the relevant half-grid;
- all four $9$-weighted poles miss the supports of the $c\,x^H$ terms.

Thus every factorial, pole, and corrected-column contribution has been accounted for before division.

The surviving LOW source is


$$
\boxed{
a'_{ui}\equiv
[y^{r_1-i}]x^{H-3+u}G(x)\pmod3.
}
\tag{5.3}
$$


It vanishes for $u\ge3$.

Put


$$
N_i=r_1-i.
$$


For $u=0,1,2$,


$$
\boxed{
\begin{aligned}
a'_{0i}&=
g_0\binom{N_i+2}{2}-g_1(N_i+1)+g_2,\\
a'_{1i}&=-g_0(N_i+1)+g_1,\\
a'_{2i}&=g_0
\end{aligned}
\pmod3.
}
\tag{5.4}
$$



Since $r_1\equiv1\pmod3$, these columns depend only on $i\bmod3$.

## 5.2 The possible second terminal return at $Y_d$

For the HIGH row $Y_d$, a top-pole contribution modulo $27$ could arise from the coefficient $[y^m]F_i$. It must not simply be omitted.

The retained complete-core support theorem at precision $27$ gives


$$
F_i\equiv x^D\psi_i\pmod{27},
\qquad
\operatorname{supp}\psi_i\subseteq
I_{H/243}(3D/2),
\qquad
\deg\psi_i\le m-D.
$$


But


$$
m-D=\frac{H-3D+1}{2}
$$


lies at distance at least


$$
\frac{H}{486}-\frac{3D-1}{2}
$$


from a multiple of $H/243$. The retained window makes this larger than $3D/2$. Hence


$$
\boxed{[y^m]F_i=0\pmod{27}.}
\tag{5.5}
$$



This proves the vanishing of that possible terminal return at the required precision.

The remaining pole calculation yields


$$
\frac{(T_R)_{Y_d,i}}9
\equiv
[y^{r_1-d-i}]x^{H-3}G(x)\pmod3.
\tag{5.6}
$$



On the other hand, replacing $y^d$ by its remainder modulo $x^D$ in this extraction changes it by an $x^H$-multiple with lower degree $O(D)$. Therefore


$$
\boxed{
\frac{(T_R)_{Y_d,i}}9
\equiv r_d^Ta'_i\pmod3.
}
\tag{5.7}
$$



Because $a'_i$ is supported in $0,1,2$, only


$$
(r_d)_0,(r_d)_1,(r_d)_2\equiv(1,2,1)\pmod3
$$


are used.

Equation (5.7) is the required equality of the next actual HIGH boundary source and its complete LOW feedback.

---

# 6. Evaluation of the whole first digit of $\mathcal Q/9$

Let


$$
\tau=e_{\nu-1},
$$


and write


$$
\widetilde b=b-X_{\rm act}^TL_{\rm act}^{-1}a
=-c\,e_{Y_m}\tau^T+3B.
\tag{6.1}
$$



The lower-edge row of $B$ is


$$
B_d=
\frac{(T_R)_{Y_d}}9-r_d^Ta'\equiv0\pmod3
\tag{6.2}
$$


by (5.7).

The exact nonlinear term is


$$
\mathcal Q
=
9a'^TL_{\rm act}^{-1}a'
+
3\widetilde b^T\widehat E_{\rm act}^{-1}\widetilde b.
$$



Using


$$
\widehat E_{\rm act}^{-1}
\equiv K_0^{-1}-3K_0^{-1}VK_0^{-1}\pmod9,
$$


and $K_0^{-1}e_{Y_m}=e_{Y_d}$, the completely assembled divided digit is


$$
\boxed{
\frac{\mathcal Q}{9}
\equiv
a'^TL^{-1}a'
-c\bigl(\tau B_d+B_d^T\tau^T\bigr)
-c^2V_{dd}\tau\tau^T
\pmod3.
}
\tag{6.3}
$$



This displays why the nonlinear object is not $c^2$ alone.

All three terms vanish for separate proved reasons:

1. $a'$ is supported in LOW coordinates $0,1,2$, and the actual leading LOW inverse satisfies
   

$$
(L^{-1})_{uv}=0\pmod3
   \quad(u+v<D-1).
$$


   Hence $a'^TL^{-1}a'=0$.

2. $B_d=0$ by the complete source-feedback equality (5.7).

3. $V_{dd}=0$, as follows either from (4.7) or the evaluated HIGH response.

## Theorem 6.1 — The next complete nonlinear digit vanishes

On the retained sufficiently large original family,


$$
\boxed{
\frac{\mathcal Q}{9}\equiv0\pmod3,
\qquad
\mathcal Q\in27M_\nu(\mathbb Z_3).
}
\tag{6.4}
$$



This holds for the full residual block, not only its selected $2\times2$ subblock.

It is a proof of the first digit of the exact object $\mathcal Q/9$. It is **not** an evaluation of all higher digits of that object.

## 6.1 Consequence for the actual Schur depth

The exact identity remains


$$
S_{\rm act}=S_c+3^6\Phi_R-3^{13}\mathcal Q.
$$


At the retained scope,


$$
S_c\in3^{17}M,\qquad
\Phi_R\in3^{10}M,\qquad
\mathcal Q\in3^3M.
$$


Therefore


$$
\boxed{S_{\rm act}\in3^{16}M.}
\tag{6.5}
$$



Equivalently, the exact turn20 operator


$$
\Upsilon_{15}
=\frac{\mathcal Q}{9}-\frac{\Phi_R}{3^9}
-\frac{S_c}{3^{15}}
$$


satisfies


$$
\Upsilon_{15}\in3M.
$$



The core inverse remains unprotected: even the improved absolute depth $16$ does not exceed the known core inverse loss $s_c\ge17$.

---

# 7. Evaluation of the next endpoint numerator

The exact endpoint identity is


$$
\frac{e_{\rm act}-e_c}{3^7}
=
-\left(
a'^TL_{\rm act}^{-1}w_U
+
\widetilde b^T\widehat E_{\rm act}^{-1}\widetilde w_Y
\right),
\tag{7.1}
$$


where


$$
\widetilde w_Y=w_Y-X_{\rm act}^TL_{\rm act}^{-1}w_U.
$$



## 7.1 The LOW endpoint response is terminal-local after inversion

The leading LOW matrix has the exact finite anti-Toeplitz description


$$
L_{ab}\equiv
(-1)^k\binom{r_1+k}{k},
\qquad
k=D-1-a-b\ge0,
$$


and is zero for $a+b\ge D$.

Its inverse therefore satisfies


$$
(L^{-1})_{ab}\equiv
\binom{r_1+1}{a+b-D+1}
$$


when $a+b\ge D-1$, and is zero otherwise.

Since $w_{U,b}=(-2)^b\equiv1\pmod3$,


$$
(L^{-1}w_U)_u
=
\sum_{k=0}^u\binom{r_1+1}{k}\pmod3.
$$


For the only needed coordinates,


$$
\boxed{
(L^{-1}w_U)_0=1,\qquad
(L^{-1}w_U)_1=0,\qquad
(L^{-1}w_U)_2=1.
}
\tag{7.2}
$$



Thus


$$
a_i'^TL^{-1}w_U=a'_{0i}+a'_{2i}.
$$


Using (5.4),


$$
\boxed{
a_i'^TL^{-1}w_U
=
g_0\sum_{v=0}^2\binom iv
+
g_1\sum_{v=0}^1\binom iv
+g_2
\pmod3.
}
\tag{7.3}
$$



This gives the three-row table stated in the executive conclusion.

## 7.2 The actual terminal endpoint return survives

Modulo $3$,


$$
\widetilde b=-c\,e_{Y_m}\tau^T,
\qquad
\widehat E_{\rm act}^{-1}e_{Y_m}=e_{Y_d}.
$$


Also,


$$
(\widetilde w_Y)_d
=
(-1)^d-r_d^Tw_U
=
\pi(y^d)(-1)\pmod3.
$$



Set $s=D/2$. Since $d=3s-1$,


$$
\pi(y^d)(-1)
\equiv
\sum_{a=2s}^{3s-1}\binom{3s-1}{a}
=
\sum_{a=0}^{s-1}\binom{3s-1}{a}
\pmod3.
\tag{7.4}
$$


Define this residue to be $\Pi_D$.

## Theorem 7.1 — Complete first endpoint numerator

For every retained residual index,


$$
\boxed{
\frac{(e_{\rm act}-e_c)_i}{3^7}
\equiv
-\mathcal E_G(i)
+c\,\mathbf1_{i=\nu-1}\Pi_D
\pmod3,
}
\tag{7.5}
$$


with


$$
\mathcal E_G(i)=
\begin{cases}
g_0+g_1+g_2,&i\equiv0\pmod3,\\
2g_0+2g_1+g_2,&i\equiv1\pmod3,\\
g_0+g_2,&i\equiv2\pmod3.
\end{cases}
$$



The endpoint vector is represented by three periodic values and one actual terminal return. Both selected original columns can be evaluated without constructing the vector of length $\nu$.

---

# 8. A bounded original-domain interface for the new producer coefficients

Only three new producer residues are needed:


$$
\rho_0=\frac{e_{A-3}}{3^7},\qquad
\rho_1=\frac{e_{A-2}}{3^7},\qquad
\rho_2=\frac{e_{A-1}}{3^7}
\pmod3.
\tag{8.1}
$$


They determine


$$
\boxed{
\rho_0=2g_0,\qquad
\rho_1=g_0+2g_1,\qquad
\rho_2=g_1+2g_2.
}
\tag{8.2}
$$



The coefficient $g_3$ is unnecessary for both (6.4) and (7.5).

## 8.1 The scalar signed loss is already paid

At these three indices,


$$
h_a\in3\mathbb Z_3,\qquad v_a\in9\mathbb Z_3,
\qquad \xi_n\equiv1\pmod3.
$$


Therefore


$$
3nh_a+\xi_nv_a\equiv3nh_a+v_a\pmod{27}.
$$


No new $\eta$-division is needed to obtain these particular coefficients.

On the fixed progression,


$$
n\equiv245\pmod{729},
\qquad A/3^5\equiv1\pmod3.
$$


For $a=A-3,A-2,A-1$, respectively,


$$
3^{-5}F/a!\equiv2,2,1\pmod3.
$$


Consequently


$$
\boxed{
\rho_k
=
-f_k\left(
2\,\frac{h_{A-3+k}}3+
\frac{v_{A-3+k}}9
\right)\pmod3,
\qquad
(f_0,f_1,f_2)=(2,2,1).
}
\tag{8.3}
$$



Here $h/3$ is extracted from $h\bmod9$, and $v/9$ from $v\bmod27$. These divisions are paid at their displayed precisions.

This does not alter the required modulus-$3^8$ division for the pending first scalar $c$.

## 8.2 Independent locality bound: $62$ coordinates

At modulus $27$,


$$
\ell_3=9,\qquad d_3=18.
$$


Thus the Pascal-transformed unit matrix has bandwidth $18$, and its inverse requires three Neumann terms:


$$
\mathsf B_n^{-1}\equiv
\sum_{r=0}^2(-\mathsf C^{-1}\Delta)^r\mathsf C^{-1}
\pmod{27}.
$$



The maximum propagation width is


$$
18+2+2(18+2)=60.
$$


A suffix of length $62$, comprising twenty complete $3\times3$ blocks and one terminal $2\times2$ block, is sufficient.

The matrix data depend only on $n\bmod3^5$; the divided factorial units in (8.3) require $n\bmod3^6$. A fixed representative is


$$
\boxed{n_*=245,\qquad L_*=62,}
$$


with suffix $183,\ldots,244$.

This representative is used only for the proved local positive-unit-matrix data. No order-six congruence for the actual small signed producer at $n=245$ is presumed.

The effective interface consists of:

- two right-hand sides;
- $62$ coordinates;
- bandwidth $18$;
- Neumann levels $0,1,2$;
- only unit $J_3,J_2$ inverses;
- top-coordinate extraction with Pascal lower indices at most $4$.

There is no original-dimension solve and no hidden nonunit inverse.

## 8.3 No additional solve is needed if the pending intermediates are retained

The pending width-$350$ calculation already produces $z_u,z_b$ to much greater precision. The required three entries are simply


$$
v_a=\sum_{j=a}^{n-1}(-1)^{j-a}\binom ja(z_u)_j,
$$




$$
h_a=\sum_{j=a}^{n-1}(-1)^{j-a}\binom ja\bigl(p_j+(z_b)_j\bigr),
$$


for $a=n-5,n-4,n-3$.

Thus the new outputs can be obtained by bounded postprocessing of those retained intermediate vectors. This is not a request to rerun the scalar calculation or any accepted producer, Jacobi, Cartier, or content control.

---

# 9. The remaining endpoint digit: an explicit nine-state evaluation

The residue


$$
\Pi_D=\sum_{a=0}^{s-1}\binom{3s-1}{a}\pmod3,
\qquad s=D/2,
$$


can depend on higher digits of the actual $s$. It must not be replaced without proof by a function of the fixed suffix of $n$.

There is nevertheless a direct bounded-state evaluation.

Let


$$
N=3s-1,\qquad B=s-1.
$$


Read their ternary digits from most significant to least significant, with leading zero padding. Maintain


$$
(T,L)\in\mathbb F_3^2,
$$


where $T$ is the accumulated weight for an equal prefix and $L$ that for a strictly smaller prefix.

For input digits $n_k,b_k$, update


$$
\boxed{
\begin{aligned}
T'&=T\binom{n_k}{b_k},\\
L'&=2^{n_k}L+
T\sum_{a=0}^{b_k-1}\binom{n_k}{a}
\end{aligned}
\pmod3.
}
\tag{9.1}
$$


Start from $(T,L)=(1,0)$, and output $T+L$.

Lucas’s theorem proves the transition directly. The state set is the explicit nine-element set $\mathbb F_3^2$. Actual inputs determine a particular path in it; no claim that every state occurs on the original power progression is needed.

This evaluation takes $O(\log H)$ digit steps and constant state storage. It does not materialize a length-$D$ vector.

### Scope

This is an exact digit interface for each actual original-window index. It is not a numerical evaluation of $\Pi_D$ on every member of the progression, nor a proof that $\Pi_D$ is constant there.

Together with the three fixed producer residues and the pending $c$, it evaluates the endpoint digit (7.5) on the same original real-window progression.

---

# 10. Precision and support ledger for the new contraction

| Object | Required data | Effective support or states | Nonunit loss |
|---|---|---|---:|
| First scalar $c$ | Existing $3^8$ evaluator | $350$ coordinates, 8 Neumann terms | $1$ for $\eta$, then $6$ for the whole coefficient |
| New $\rho_0,\rho_1,\rho_2$ | $h\bmod9,\ v\bmod27$ | $62$-coordinate proof; only top five transformed entries observed | $h/3,\ v/9$, explicitly paid |
| $a'\bmod3$ | $g_0,g_1,g_2$ | LOW rows $0,1,2$; three residual residue classes | None after the paid $T_R/9$ extraction |
| $\widehat E_{\rm act}^{-1}e_{Y_m}\bmod9$ | Complete HIGH block and LOW feedback | HIGH rows $d,d+1$ | None: normalized HIGH inverse is a unit inverse |
| Next lower-edge HIGH feedback | $r_d^Ta'$ | First three coefficients of $r_d$ | None |
| $\mathcal Q/9\bmod3$ | All preceding terms | Identically zero on the full residual block | Whole quadratic division accounted for |
| Endpoint LOW numerator | $g_0,g_1,g_2$ | Three periodic values | None |
| Endpoint terminal return | Actual $D/2$ | Nine-state ternary digit interface | None |
| Original eliminated inverse | Exact $E_{\rm act}^{-1}$ | Retained LOW/HIGH normalization | Still $1$ |
| Core residual inverse | Exact $S_c^{-1}$, if it exists | Not evaluated | At least $17$; still unprotected |

No Christoffel inversion is used in this new calculation. Its separate four-digit loss has not been removed.

---

# 11. Determinant ratio, primitive normalization, and whole error

The depth-$15$ determinant pair from turn20 remains an exact pair:


$$
\mathcal D_{0,15}=\det\Upsilon_{15},
$$




$$
\mathcal D_{1,15}
=
e_{\rm act}^T\operatorname{adj}(\Upsilon_{15})e_{\rm act}
-3^{15}d_{\rm act}\det\Upsilon_{15}.
$$



The new result proves $\Upsilon_{15}\in3M$, but does not determine its inverse, determinant, or distinguished cofactor.

If one extracts the additional common residual factor, its effect in the determinant ratio is again **one factor**, not a gain proportional to $\nu$. No scalar-core comparison follows: the guaranteed absolute depth is now $16$, still not greater than the core inverse loss $s_c\ge17$.

Both original residual columns remain primitive, and


$$
(e_{\rm act})_i\equiv(-1)^i\pmod3.
$$


Growing raw Jacobi content therefore still cannot be used to divide those columns or their endpoint integrally.

After the actual row contents, actual multiplier, and least actual clearer, retain


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
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell},
$$


and


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}{g_\ell}
\det H_{\rm complete}.
}
\tag{11.1}
$$



For the weighted producer, the separate actual normalization remains


$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B,
$$




$$
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n.}
\tag{11.2}
$$



Nothing in the new local cancellation evaluates either all-prime gcd, establishes the required distinguished-cofactor nonvanishing, or bounds the whole nonzero primitive error along an infinite original sequence.

---

# 12. Genuinely new arithmetic output and exact remaining bottleneck

No numerical output is claimed in this report.

The pending scalar calculation remains responsible for $c$. Its accepted or planned checks are not requested again.

The only additional bounded arithmetic needed for the newly derived endpoint table is:

### Inputs

Retain from that calculation the top entries of $z_u,z_b$, and use


$$
a=n-5,n-4,n-3.
$$



### New postprocessing outputs

1. $h_a\bmod9$, each necessarily divisible by $3$;
2. $v_a\bmod27$, each necessarily divisible by $9$;
3. the three residues $\rho_k$ from (8.3);
4. $g_0,g_1,g_2$ from (8.2);
5. the three endpoint LOW values
   

$$
g_0+g_1+g_2,\qquad
   2g_0+2g_1+g_2,\qquad
   g_0+g_2.
$$



For any specified actual original index, the remaining input is the ternary digit stream of $s=D/2$; the nine-state recurrence outputs $\Pi_D$, and (7.5) then gives both selected endpoint digits.

No arithmetic calculation is needed to establish the newly proved vanishing


$$
\mathcal Q/9\equiv0\pmod3.
$$



### Exact next mathematical bottleneck

The local task is now to go beyond the first digit just evaluated:

- determine the next complete contraction $\mathcal Q/27$, including the next LOW quadratic layer and the next HIGH boundary response;
- determine the higher transported endpoint, not only (7.5);
- control the relative arithmetic and nonvanishing of the exact determinant/cofactor pair.

At that stage, a fixed-depth cancellation still cannot substitute for an actual inverse-loss or relative-pair theorem.

---

# 13. Proof-status ledger

| Statement | Status |
|---|---|
| Width-$350$, band-$41$ evaluator and original residue dependence | Audited and valid |
| Numerical first scalar $c$ | Pending coordinator calculation; not inferred |
| Actual cubic producer jet modulo $9$ | Proved |
| Actual HIGH inverse response $4e_{Y_d}-3e_{Y_{d+1}}\pmod9$ | Proved |
| Next LOW source supported in rows $0,1,2$ | Proved |
| Complete lower-edge HIGH source equals LOW feedback | Proved |
| $\mathcal Q/9\equiv0\pmod3$ | Proved for the full actual residual block |
| $S_{\rm act}\in3^{16}M$ | Proved on the retained window |
| Explicit three-periodic-plus-terminal endpoint formula | Proved |
| Three new producer residues | Bounded postprocessing specified; not numerically evaluated |
| Nine-state evaluation of the actual terminal endpoint digit | Explicit algorithm proved; no original input run claimed |
| Full exact $\mathcal Q/9$, higher endpoint, actual residual inverse | Unresolved |
| Distinguished-cofactor nonvanishing, all-prime gcd, whole error decay | Unresolved |

## Conclusion

The first-jet evaluator is mathematically attached to the actual signed producer at the retained finite endpoints. Its pending numerical scalar must still be received before selecting the $c$-branch.

Independently of that branch, the next complete nonlinear calculation now yields


$$
\boxed{
\mathcal Q\in27M,\qquad S_{\rm act}\in3^{16}M.
}
$$


The proof includes the actual HIGH inverse boundary response, the next LOW force, its HIGH feedback, the higher producer jet, and the possible second terminal return.

The endpoint numerator is reduced to three fixed producer residues, a three-periodic observation, and one explicit original-domain ternary digit observable. It is no longer an unevaluated contraction through an original-dimension inverse.

The remaining global obligation is unchanged: prove suitable nonvanishing and arithmetic control for the actual primitive pair and the **whole same-index error** on an infinite original sequence.



$$
\boxed{\text{The irrationality or rationality of }e+\pi\text{ remains unresolved.}}
$$


