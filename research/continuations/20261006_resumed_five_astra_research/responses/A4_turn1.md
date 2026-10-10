> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4, Turn 1 — Independent audit, repaired divisor proof, and a sharper complete-row content theorem

## Executive assessment

The attached work still does **not** establish the rationality or irrationality of $e+\pi$. It does contain several valid reductions, and the outstanding divisor claim can be proved rigorously.

My principal conclusions are:

1. **A1’s whole-layer Hankel compression is valid modulo $3$**, as a consequence of the accepted whole-form normalization and the actual/core transfer. It is not a Hankel assertion about the separate pole layers, nor does it automatically extend to all six normalized digits.

2. **A1’s six-digit Smith/radical decision theorem is correct.** It decides, at a supplied original input, whether the largest core Smith exponent is at most $5$. It does not decide exact singularity when the sixth radical survives, and it supplies no unevaluated family-wide inverse bound.

3. **A1’s directional scalar guard is correct**, provided the accepted endpoint integrality and comparison hypotheses are retained. The strict inequality must concern the **whole scalar**
   

$$
e_c^TB_c^{-1}e_c-3^{26}d_c.
$$


   Matrix invertibility alone does not establish this guard.

4. **The coordinator’s finite pole pairing, cutoff condition, and binomial correction are correct.** The additional low-layer identity is also correct:
   

$$
\boxed{
   P_0((y^H-1)F)+P_1((y^H-1)F)
   =-2F[(H-1)/2].
   }
$$


   Its proof depends on keeping the excluded $c=3$ contribution in its proper layer, namely $\ell=0$.

5. **A3’s primitive correction-height comparison and complete-row content theorems survive audit**, with the nonzero-denominator and sign conventions made explicit below. Their exponential factors are justified; the specialized primitive moment heights and complete-force contents themselves remain unbounded at the desired scale.

6. **The claimed divisor is valid**, but its brief proof should be replaced by a primewise argument:
   

$$
\boxed{Z_X\mid |\Omega|Q^\Delta.}
$$


   In fact, a sharper divisor follows. If
   

$$
G_t=\gcd(t_0,t_1),\qquad
   \Omega_{\rm red}
   =\frac{|\Omega|}{\gcd(|\Omega|,G_t^2)},
$$


   then
   

$$
\boxed{Z_X\mid \Omega_{\rm red}Q^\Delta.}
$$



7. **A new complete-row refinement removes every prime factor of $t_0$ that is absent from the reference clearer $L$.** Using both Wronskian eliminations gives integers $K_j^\sharp$ satisfying
   

$$
\boxed{
   \left|v_p(|AB|)-v_p(Z_{K^\sharp})\right|
   \le v_p(LG_t),
   }
$$


   and, more importantly,
   

$$
\boxed{
   v_p(|AB|)=v_p(Z_{K^\sharp})
   \qquad(p>n+1).
   }
$$


   This is an exact statement about the actual complete, row-primitive endpoint factor, not merely a new output specification.

No code was executed. The supplied PASS receipt is treated only as reported finite corroboration. The coordinator’s planned $n=225$ complete-force/content calculation is not treated as a result.

---

# 1. Scope and retained hypotheses

The two active original domains remain separate.

### Ternary core route

Retain


$$
n=4^j+1,\qquad j>0,\qquad81\mid j,
$$




$$
A=n-2=H-D,\qquad H=3^{h-1},\qquad0<D<H/972,
$$


and


$$
m=\frac{A+1}{2},\qquad
d=\frac{3D}{2}-1,\qquad
\nu=\frac D2-1.
$$



The finite columns remain exactly


$$
U_u=x^u\quad(0\le u<D),\qquad
z_i=x^Dy^i\quad(0\le i<\nu),\qquad
Y_b=y^b\quad(d\le b\le m),
$$


where $x=y-1$.

For the six-digit conclusions, retain the sufficiently large original window


$$
j\equiv81\pmod{243},\qquad
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15},
$$


and every simultaneous support, saturation, lower-factor, and upper-degree hypothesis from the accepted transfer theorem.

The preceding independent review is retained. In particular, I reuse


$$
S_c\in3^{26}M_\nu(\mathbb Z_3),\qquad
S_{\rm act}-S_c\in3^{32}M_\nu(\mathbb Z_3).
\tag{1.1}
$$



### Complete endpoint route

Retain either


$$
n=15^r,\quad r\ge2,\quad\mathcal P=\{3,5\},
$$


or


$$
n=105^r,\quad r\ge2,\quad\mathcal P=\{3,5,7\}.
$$



Here $d=2,b=3$; contact rows and columns are $0,1,2$; reconstruction has coordinates $0,1,2,3$; and the complete force ends at exactly $2n+2$.

The accepted local theorem supplies


$$
\Delta_T\ne0,\qquad \xi_0\xi_3\ne0
\tag{1.2}
$$


on these original families. These are indispensable hypotheses for the rational endpoint formulas below.

The supplied literature gate is background about established methods and overlap, not an independently repeated literature search or a proof of a target-specific arithmetic estimate.

---

# Part I. Audit of A1 Turn 0

## 2. Whole-layer Hankel compression

Write


$$
B_c=-S_c/3^{26},\qquad
\Theta=-S_{\rm act}/3^{26}.
$$


Then (1.1) gives


$$
\Theta\equiv B_c\pmod{3^6}.
\tag{2.1}
$$



The accepted whole-form normalization is


$$
\mathsf H=\mathsf V^T\Psi\mathsf V,\qquad
\Psi=-S_{\rm act}/3^{16},\qquad
\mathsf V\equiv I\pmod3.
$$


Consequently,


$$
\mathsf H/3^{10}=\mathsf V^T\Theta\mathsf V
$$


is integral and Hankel, and


$$
B_c\equiv\Theta\equiv\mathsf H/3^{10}\pmod3.
$$


Thus


$$
\boxed{
B_c\bmod3=(\lambda_{i+j})_{0\le i,j<\nu}.
}
\tag{2.2}
$$



This establishes A1’s compression. The number of required anti-diagonal values is


$$
2\nu-1=D-3,
$$


with indices exactly


$$
0,\ldots,2\nu-2= D-4.
$$



### Important scope restriction

The proof establishes that the **complete normalized first layer** is Hankel. It does not establish any of the following:

- that each separate pole layer is Hankel;
- that one may reduce the polynomial inputs modulo $3$ before resolving the lower-layer carries;
- that $B_c\bmod3^6$ is Hankel in the same coordinates;
- that the six-digit radical calculation can be recovered from the first-layer moment values alone.

At higher precision, the coordinate transformation and the higher complete matrix data must be retained.

### Both corrected columns remain necessary

For the accepted representatives


$$
\phi_i=x^D\psi_i,\qquad
\phi_i\equiv\widehat z_i^{\,c}\pmod{3^{25}},
$$


the bracket input is


$$
T_{ij}=x^{H+D}(\beta+3y)\psi_i\psi_j.
$$


It contains both corrected representatives.

As clarified in the preceding review, the pairing error follows from the full basis decomposition, not from an overstatement of orthogonality:


$$
G_c(\Phi,\Phi)-S_c\in3^{50}M.
\tag{2.3}
$$


This comfortably supports every absolute modulus through $3^{32}$.

### Kernel and endpoint action

With


$$
L(X)=\sum_{k=0}^{2\nu-2}\lambda_kX^k,\qquad
a^\vee(X)=\sum_{j=0}^{\nu-1}a_jX^{\nu-1-j},
$$


one has


$$
[X^{\nu-1+i}]L(X)a^\vee(X)
=\sum_{j=0}^{\nu-1}\lambda_{i+j}a_j.
$$


Therefore A1’s convolution description of the kernel is exact.

The endpoint action


$$
a\longmapsto\sum_{j=0}^{\nu-1}(-1)^ja_j
$$


uses the accepted actual/core endpoint residue. It is not inferred merely from the Hankel property.

### Complete forcing and terminal return

The compression does not change the recurrence domain:


$$
\lambda_{i+\nu}
+\sum_{k=0}^{\nu-1}\bar f_k\lambda_{i+k}
=\bar b_i^{\langle26\rangle},
\qquad 0\le i\le\nu-2.
\tag{2.4}
$$


There is no moment $\lambda_{2\nu-1}$.

The terminal identity remains


$$
J^T\varepsilon+\omega
=
-\varepsilon-s\bigl(\theta e_{\nu-1}
+3^{26}b^{\langle26\rangle}\bigr).
\tag{2.5}
$$


In particular, neither the complete forcing nor $\omega_{\nu-1}$ disappears.

**Verdict:** valid new corollary of the accepted whole-form normalization; not an evaluated first-layer rank theorem.

---

## 3. The six-digit Smith/radical criterion

Let $B\in M_\nu(\mathbb Z_3)$ be symmetric. A lifted decomposition into a radical and a nondegenerate complement modulo $3$ gives a block matrix


$$
P^TBP=
\begin{pmatrix}
A&B_{KL}\\
B_{KL}^T&C
\end{pmatrix},
\qquad C\in\operatorname{GL}(\mathbb Z_3).
$$


Its residual Schur operator


$$
R=A-B_{KL}C^{-1}B_{KL}^T
$$


is divisible by $3$.

The congruence elimination is unimodular over $\mathbb Z_3$. Thus the unit complement contributes Smith exponents $0$, while replacing $R$ by $R/3$ reduces each remaining positive Smith exponent by one.

If $r_k$ is the residual dimension after $k$ stages, then


$$
r_k=\#\{\text{Smith exponents at least }k\},
\tag{3.1}
$$


with exact zero invariant factors counted as infinite exponents.

It follows that


$$
\boxed{
r_6=0
\iff
B_c\text{ is nonsingular and all its Smith exponents are }\le5.
}
\tag{3.2}
$$



When this holds, writing $a$ for the largest exponent,


$$
s_c=26+a,
$$


and


$$
v_3(\det B_c)=\sum_{k=1}^{5}r_k.
\tag{3.3}
$$



These statements are correct even when the determinant valuation is much greater than $5$. The calculation follows invariant factors rather than trying to detect the determinant from its residue modulo $3^6$.

### What a surviving sixth radical means

If $r_6>0$, six digits establish only that at least one Smith exponent is at least $6$, or is infinite. They do **not** distinguish these possibilities.

Accordingly:

- if the exact core is nonsingular, then $s_c\ge32$;
- if it is singular, $s_c$ is undefined;
- no assertion of exact singularity is justified from $r_6>0$.

### Actual/core implication

If $a\le5$, then


$$
B_c^{-1}(\Theta-B_c)\in3^{6-a}M.
$$


Hence $\Theta$ is nonsingular and


$$
\frac{\det\Theta}{\det B_c}
\in1+3^{6-a}\mathbb Z_3,
\tag{3.4}
$$




$$
\Theta^{-1}-B_c^{-1}\in3^{6-2a}M.
\tag{3.5}
$$



**Verdict:** correct finite-precision decision theorem, obtained by applying standard local linear algebra to the particular six-digit transfer interval. Its success on the moving original family remains unevaluated.

---

## 4. Directional scalar protection

Retain


$$
e_{\rm act}-e_c\in3^6\mathbb Z_3^\nu,\qquad
d_{\rm act}-d_c\in3^4\mathbb Z_3,
\tag{4.1}
$$


together with the accepted integrality of the endpoint vectors and of the scaled scalar $3^{26}d$.

Assume $a<6$, and put


$$
z_c=B_c^{-1}e_c,\qquad
u=\max\left(0,-\min_i v_3((z_c)_i)\right).
$$


Then $u\le a$.

Writing $\Delta=\Theta-B_c$, the resolvent identity gives


$$
\Theta^{-1}e_c-z_c=-\Theta^{-1}\Delta z_c
\in3^{6-a-u}\mathbb Z_3^\nu.
$$


Because $6-a>0$, both inverse endpoint vectors have valuation at least $-u$. Symmetry then gives


$$
e_c^T(\Theta^{-1}-B_c^{-1})e_c
=-z_c^T\Delta\Theta^{-1}e_c
\in3^{6-2u}\mathbb Z_3.
$$



The endpoint-vector cross terms have depth at least $6-u$, and the quadratic endpoint error has depth at least $12-a$. Both are at least $6-2u$. Finally,


$$
3^{26}(d_{\rm act}-d_c)\in3^{30}\mathbb Z_3.
$$



Therefore


$$
\boxed{
\sigma_{\rm act}-\sigma_c\in3^{6-2u}\mathbb Z_3,
}
\tag{4.2}
$$


where


$$
\sigma_c=e_c^TB_c^{-1}e_c-3^{26}d_c,
$$




$$
\sigma_{\rm act}
=e_{\rm act}^T\Theta^{-1}e_{\rm act}-3^{26}d_{\rm act}.
$$



The strict guard


$$
v_3(\sigma_c)<6-2u
\tag{4.3}
$$


therefore transfers nonvanishing and valuation.

### Whole-pair subtraction

The relevant pair is still


$$
D_0=\det\Theta,
$$




$$
\boxed{
D_1=e_{\rm act}^T\operatorname{adj}(\Theta)e_{\rm act}
-3^{26}d_{\rm act}\det\Theta.
}
\tag{4.4}
$$


Under the guard,


$$
v_3(D_1)-v_3(D_0)=v_3(\sigma_c).
$$



The radical/complement formula likewise requires the updated scalar. With $R=3T$,


$$
\eta=e_K-B_{KL}C^{-1}e_L,\qquad
\gamma=3^{26}d-e_L^TC^{-1}e_L,
$$


one has, for radical dimension $r\ge1$,


$$
D_1=(\det P)^{-2}\det C
\left(
3^{r-1}\eta^T\operatorname{adj}(T)\eta
-\gamma\,3^r\det T
\right).
\tag{4.5}
$$


This is a polynomial identity and remains valid when $T$ is singular.

**Verdict:** the directional estimate is valid. It is a conditional protection theorem, not an evaluated scalar nonvanishing result.

---

# Part II. Audit and completion of the finite pole reduction

## 5. Exact finite pairing

The original pole cutoff is


$$
2v+1\le4n-3,
$$


equivalently


$$
v\le R_{\max}=2n-2.
$$



For


$$
\delta_\ell=3^{h-\ell},\qquad
r_c=\frac{c\delta_\ell-1}{2},
$$


define


$$
P_\ell(T)
=3^\ell
\sum_{\substack{c\ge1\ {\rm odd}\\3\nmid c\\r_c\le R_{\max}}}
\frac{T[r_c]}c.
$$



For $\ell\ge2$, put


$$
a_\ell=2\cdot3^{\ell-1}.
$$


Then


$$
r_{c+a_\ell}=r_c+H,
$$


and $c\mapsto c+a_\ell$ preserves odd positive $3$-adic units.

If


$$
\deg F\le B,\qquad H+B\le R_{\max},
$$


every nonzero low-copy coefficient has its high-copy counterpart inside the original cutoff. Reindexing only those nonzero coefficients gives


$$
\begin{aligned}
P_\ell((y^H-1)F)
&=3^\ell\sum_{\substack{c\ {\rm odd},\,3\nmid c\\0\le r_c\le B}}
\left(\frac1{c+a_\ell}-\frac1c\right)F[r_c]\\
&=-2\cdot3^{2\ell-1}
\sum_{\substack{c\ {\rm odd},\,3\nmid c\\0\le r_c\le B}}
\frac{F[r_c]}{c(c+a_\ell)}.
\end{aligned}
\tag{5.1}
$$


All displayed denominators are units.

Thus


$$
P_\ell((y^H-1)F)\in3^{2\ell-1}\mathbb Z_3.
\tag{5.2}
$$



The cutoff hypothesis is essential. Without it, the omitted high-copy boundary coefficient produces precisely the sort of defect tested by the supplied code.

---

## 6. Proof of the additional low-layer identity

Assume


$$
D\ge486,\qquad D/H<1/972,
$$




$$
R_{\max}=2H-2D+2,\qquad
\deg F\le H-2D.
$$


Put


$$
r=\frac{H-1}{2},\qquad T=(y^H-1)F.
$$



### Layer $\ell=1$

Here $\delta_1=H$. The cutoff gives


$$
c\le\frac{2R_{\max}+1}{H}
=\frac{4H-4D+5}{H}<4.
$$


The positive odd possibilities are $c=1,3$, but $c=3$ is excluded by $3\nmid c$. Therefore only $c=1$ occurs:


$$
P_1(T)=3T[r].
$$


Since $r<H$,


$$
T[r]=-F[r].
$$


Hence


$$
P_1(T)=-3F[r].
\tag{6.1}
$$



### Layer $\ell=0$

Here $\delta_0=3H$. The only allowed positive odd $c$ below the cutoff is again $c=1$. Its extraction position is


$$
\frac{3H-1}{2}=r+H.
$$


This position lies inside the original cutoff because


$$
r+H\le2H-2D+2
\iff H\ge4D-5,
$$


which follows from $D/H<1/972$.

Also $\deg F<H$, so


$$
T[r+H]=F[r].
$$


Thus


$$
P_0(T)=F[r].
\tag{6.2}
$$



Combining (6.1) and (6.2),


$$
\boxed{
P_0((y^H-1)F)+P_1((y^H-1)F)
=-2F[(H-1)/2].
}
\tag{6.3}
$$



The excluded $c=3$ position at $\ell=1$ is exactly the $c=1$ position at $\ell=0$. Its weight is $1$, not $3$. This is why the answer is $-2F[r]$, rather than a cancellation to zero.

This identity is proved here under the stated window; it is not an output of the supplied finite receipt.

---

## 7. Binomial correction and application to both corrected columns

Write


$$
(y-1)^H=(y^H-1)+\Delta_H.
$$


Since $H$ is odd, the endpoint coefficients cancel, and for $1\le r<H$,


$$
\Delta_H[r]=(-1)^{H-r}\binom Hr.
$$


The identity


$$
\binom Hr=\frac Hr\binom{H-1}{r-1}
$$


and the fact that $\binom{H-1}{r-1}$ is a $3$-adic unit give


$$
\boxed{
v_3(\Delta_H[r])=h-1-v_3(r).
}
\tag{7.1}
$$



Modulo $3^q$, an interior coefficient can survive only when


$$
3^{\max(0,h-q)}\mid r.
\tag{7.2}
$$


This is a correct sparse-index restriction, not a practical state-size bound.

For the actual corrected representatives, set


$$
F_{ij}=x^D(\beta+3y)\psi_i\psi_j.
$$


If both $\deg\phi_i,\deg\phi_j\le m-1$, then


$$
\deg F_{ij}
\le D+1+2(m-1-D)
=H-2D.
\tag{7.3}
$$


Consequently,


$$
H+\deg F_{ij}\le2H-2D<R_{\max}.
$$


The finite pairing is therefore admissible.

### Complete reduced formula

The exact pairing is


$$
\begin{aligned}
G_c(\phi_i,\phi_j)
={}&-\frac{3^h}{4}
\mathfrak f\bigl((y+1)(y-1)^HF_{ij}\bigr)
-2F_{ij}[(H-1)/2]\\
&-2\sum_{\ell=2}^{h}3^{2\ell-1}
\sum_{\substack{c\ {\rm odd},\,3\nmid c\\0\le r_c\le\deg F_{ij}}}
\frac{F_{ij}[r_c]}{c(c+a_\ell)}
+\sum_{\ell=0}^{h}P_\ell(\Delta_HF_{ij}).
\end{aligned}
\tag{7.4}
$$



Every $P_\ell$ in the correction retains the original cutoff. No correction term is paired away merely because the $y^H-1$ part has been paired.

### A useful precision observation

The accepted $P=25,L=31$ upper-gap condition gives


$$
3^{h-25}=H/3^{24}\ge4D+103\ge2047>3^6.
$$


Therefore


$$
h\ge32.
\tag{7.5}
$$



Thus the factorial term in (7.4) vanishes at every absolute modulus $3^K$ with $K\le32$. This omission is justified by valuation over the entire accepted six-digit interval, not only modulo $3^{27}$.

For $27\le K\le32$, formula (7.4) becomes


$$
\begin{aligned}
G_c(\phi_i,\phi_j)\equiv{}&
-2F_{ij}[(H-1)/2]\\
&-2\sum_{\ell=2}^{\lfloor K/2\rfloor}3^{2\ell-1}
\sum_{\substack{c\ {\rm odd},\,3\nmid c\\0\le r_c\le\deg F_{ij}}}
\frac{F_{ij}[r_c]}{c(c+a_\ell)}\\
&+\sum_{\ell=0}^{K-1}P_\ell(\Delta_HF_{ij})
\pmod{3^K}.
\end{aligned}
\tag{7.6}
$$



This formula must still be evaluated **as a whole before division by $3^{26}$**. The accepted depth implies a substantial cancellation between its low coefficient, paired sums, and binomial correction. None of the three pieces alone determines a normalized moment.

---

## 8. What the supplied code and receipt corroborate

Reading the code against its stated loops gives:

- $90$ exact layer-pair checks;
- $1076$ binomial-valuation checks;
- $7052$ sparse-precision checks;
- $4$ deliberately truncated boundary-defect checks.

These counts are consistent with the receipt.

The cases use $h=4,\ldots,7$, finitely many polynomials of degree at most the listed $B$, and the stated finite cutoffs. They do not evaluate:

- an original-family Schur matrix;
- a corrected representative;
- a normalized moment;
- the additional low-layer identity on the large-$D$ window;
- a determinant/cofactor valuation;
- any complete endpoint content.

The reported PASS therefore has exactly its stated finite scope. No rerun is needed or proposed.

---

# Part III. Audit of A3 Turn 0

## 9. Nonzero denominators, signs, and complete reconstruction

On the original endpoint families, (1.2) ensures


$$
u_j=\frac{n!\xi_j}{\Delta_T}\ne0,\qquad j=0,3.
$$


Thus the endpoint centers and their positive reduced denominators are well-defined.

The complete exponential numerators remain


$$
\boxed{
N_0^{\exp}=\Delta_T+R_0\widehat w^{\exp},\qquad
N_3^{\exp}=R_3\widehat w^{\exp}.
}
\tag{9.1}
$$


In particular, the exterior $+1$ is retained in $N_0^{\exp}$.

The exponential force is the complete finite sum


$$
w_i^{\exp}
=
\sum_{j=0}^{\min(2n,n+i)}
q_j(n+i)^{\underline j}
(2n+i-j)!
\sum_{r=0}^{2n+i-j}\frac1{r!}.
\tag{9.2}
$$


There is no factorial-tail deletion.

The reconstruction matrix is


$$
\mathsf I\mathcal S=
\begin{pmatrix}
-1&n&-n(n+1)\\
1&-(n+1)&n(n+3)\\
0&1&-(2n+1)\\
0&0&1
\end{pmatrix}.
\tag{9.3}
$$


The least clearer must still cover all eight entries of the two reconstructed columns. As useful consistency identities,


$$
\sum_{j=0}^3u_j=0,\qquad
\sum_{j=0}^3v_j=1.
\tag{9.4}
$$


The second identity detects loss of the exterior term.

### Primitive triples

A3’s positive scale $\sigma_j$ is well-defined because $(\alpha_j,\beta_j)\ne(0,0)$, as follows from $\xi_j\ne0$. Hence


$$
\gamma_j=\gcd(|\mathsf A_j|,|\mathsf B_j|)>0.
$$


The resulting pair


$$
(\mathfrak a_j,\mathfrak b_j)
$$


is primitive, and


$$
\gcd(\gamma_j,|\mathsf E_j|)=1.
$$



The exact representation


$$
M_j=\gamma_jX_j,\qquad
V_j=\gamma_jY_j+L\mathsf E_j
$$


satisfies


$$
(u_j,v_j)
=\frac{n!}{\sigma_jL\Delta_T}(M_j,V_j).
\tag{9.5}
$$


Because $X_j\ne0$,


$$
d_j=\frac{|M_j|}{\gcd(|M_j|,|V_j|)}
\tag{9.6}
$$


is the actual positive reduced endpoint denominator.

The common scalar in (9.5) can be negative. Therefore the original primitive row is the auxiliary primitive row multiplied by the sign of that scalar. Absolute denominators are unaffected, but the signed quantities $A,B,\widetilde v_j$ in the final weight formula must retain their original signs.

A zero $V_j$ is harmless: then $d_j=1$. A zero $X_j$ would not be harmless; it would invalidate the endpoint ratio. It is excluded here by the accepted original-family theorem.

---

## 10. Every claimed exponential factor

A3 uses


$$
L=2^{n+1}\operatorname{lcm}(1,\ldots,n+1),
$$




$$
t_0=L\tau_n,\quad t_1=L\tau_{n+1},\quad
r_0=4L\rho_n,\quad r_1=4L\rho_{n+1}.
$$


The supplied dyadic coefficient formula and convolution formula imply that all four are integers.

Moreover,


$$
\tau_n>0,
$$


so $t_0>0$, and the Wronskian gives


$$
\Omega=t_0r_1-t_1r_0
=\frac{4(-1)^nL^2}{n+1}\ne0.
\tag{10.1}
$$



The bounds used for the exponential distortion are justified:

- $\log\operatorname{lcm}(1,\ldots,n+1)=O(n)$;
- $\tau_m\le(1+\sqrt2)^m$;
- the convolution gives
  

$$
|\rho_m|\le(1+\sqrt2)^{m-1}\sum_{j=1}^{m}\frac1j.
$$



Thus


$$
\log L,\quad \log t_0,\quad \log|\Omega|=O(n).
\tag{10.2}
$$



Crucially, this argument does **not** bound


$$
\gamma_j,\quad \mathsf E_j,\quad X_j,\quad \mathcal C_j,\quad K_j
$$


by $\exp(O(n))$. Those quantities contain the unresolved specialized arithmetic.

---

## 11. Primitive correction heights

The correction formula


$$
\kappa_j=\frac{\Omega\mathfrak b_j}{t_0X_j}
\tag{11.1}
$$


is exact.

Apply


$$
F=
\begin{pmatrix}
0&\Omega\\
t_0^2&t_0t_1
\end{pmatrix}
$$


to the primitive vector $(\mathfrak a_j,\mathfrak b_j)^T$. Its determinant is


$$
-\Omega t_0^2\ne0.
$$



If $g$ is the content of $Fv$, then


$$
g\mid|\det F|.
$$


This follows by applying the adjugate and using a Bézout relation for the primitive coordinates of $v$.

The forward and inverse norm estimates therefore give


$$
\boxed{
\log H(\kappa_j)
=
\log\max(|\mathfrak a_j|,|\mathfrak b_j|)+O(n).
}
\tag{11.2}
$$


The constants are uniform along the original families.

The same content argument gives


$$
|X_j|\mid |\Omega|t_0Q_j^\kappa,\qquad
Q_j^\kappa\mid t_0|X_j|.
\tag{11.3}
$$



### Zero correction

If $\mathfrak b_j=0$, primitivity forces $\mathfrak a_j=\pm1$. Then


$$
X_j=\pm t_0,\qquad \kappa_j=0,\qquad Q_j^\kappa=1.
$$


Both the height statement and the divisibilities remain valid under $\operatorname{den}(0)=1$.

### Direct upper bound

The clearer


$$
D_{\rm mom}=2^n(n+2)!
$$


does clear all five moments, and


$$
|c_{n+s}|\le e(5/2)^n
$$


follows by coefficientwise domination at radius $1$. Clearing the two quadratic moment expressions by


$$
2(n+2)D_{\rm mom}^2
$$


therefore yields


$$
\log H(\kappa_j)\le2n\log n+O(n).
\tag{11.4}
$$



**Verdict:** all these statements are correct. The $\exp(O(n))$ comparison factor is proved; an $\exp(O(n))$ bound for either side of (11.2) is not.

---

# 12. Repaired proof of $Z_X\mid|\Omega|Q^\Delta$

Let


$$
\mathscr D
=\mathfrak a_0\mathfrak b_3-\mathfrak b_0\mathfrak a_3.
$$


Then


$$
\kappa_0-\kappa_3
=-\frac{\Omega\mathscr D}{X_0X_3},
$$


and, with the entire evaluated numerator retained,


$$
Q^\Delta
=
\frac{|X_0X_3|}
{\gcd(|X_0X_3|,|\Omega\mathscr D|)}.
\tag{12.1}
$$



Set


$$
Z_X=\frac{|X_0X_3|}{\gcd(|X_0|,|X_3|)^2}.
$$



## 12.1 Primewise proof, including cancellation cases

Fix a prime $p$, and write


$$
x_j=v_p(X_j),\qquad
c_j=\min(v_p(X_j),v_p(Y_j)).
$$


Because the matrix


$$
\begin{pmatrix}t_0&t_1\\r_0&r_1\end{pmatrix}
$$


has determinant $\Omega$ and acts on a primitive integer vector,


$$
0\le c_j\le w:=v_p(\Omega).
\tag{12.2}
$$



The reduced denominator exponent of $Y_j/X_j$ is


$$
a_j=x_j-c_j.
$$


The difference of these two rationals is $\kappa_0-\kappa_3$.

There are three cases.

1. **$a_0>a_3$.**  
   The $p$-adic valuations of the two rationals are unequal, so their difference has reduced denominator exponent
   

$$
q=v_p(Q^\Delta)=a_0.
$$



2. **$a_3>a_0$.**  
   Similarly,
   

$$
q=a_3.
$$



3. **$a_0=a_3$.**  
   The numerator may cancel to any additional depth, including exact cancellation. Nevertheless,
   

$$
|a_0-a_3|=0\le q.
$$



In all cases,


$$
|a_0-a_3|\le q.
$$


Consequently,


$$
\begin{aligned}
v_p(Z_X)
&=|x_0-x_3|\\
&\le |a_0-a_3|+|c_0-c_3|\\
&\le q+w.
\end{aligned}
$$


Thus


$$
\boxed{Z_X\mid|\Omega|Q^\Delta.}
\tag{12.3}
$$



This argument includes $Y_j=0$, using $v_p(0)=+\infty$.

If $\mathscr D=0$, the two primitive coefficient pairs are equal up to sign. Hence $X_0=\pm X_3$, so $Z_X=1$, while $Q^\Delta=1$. The divisor remains valid; only the reference-canceling weight becomes undefined.

---

## 12.2 Sharper exact law at imbalanced primes

There is a stronger statement.

Put


$$
G_t=\gcd(t_0,t_1),\qquad s=v_p(G_t).
$$


If $x_0\ne x_3$, then


$$
\boxed{
v_p(\mathscr D)=\min(x_0,x_3)-s.
}
\tag{12.4}
$$



### Proof

The row


$$
(t_0/p^s,t_1/p^s)
$$


is primitive over $\mathbb Z_p$. Complete it to a matrix $U\in\operatorname{GL}_2(\mathbb Z_p)$.

For each primitive input vector, write its transformed coordinates as


$$
U
\binom{\mathfrak a_j}{\mathfrak b_j}
=\binom{z_j}{w_j},
\qquad z_j=X_j/p^s.
$$


The transformed vector remains primitive.

Suppose $x_0>x_3$. Then $z_0$ is divisible by $p$, so $w_0$ is a unit. In


$$
z_0w_3-w_0z_3,
$$


the second term has strictly smaller valuation than the first. Its valuation is $x_3-s$. Since multiplication by $\det U$ does not change valuation, (12.4) follows. ∎

Therefore, at every imbalanced prime,


$$
\boxed{
v_p(Q^\Delta)
=
\bigl[\max(x_0,x_3)+s-v_p(\Omega)\bigr]_+.
}
\tag{12.5}
$$



Define


$$
\Omega_{\rm red}
=\frac{|\Omega|}{\gcd(|\Omega|,G_t^2)}.
$$


Then


$$
v_p(\Omega_{\rm red})=[v_p(\Omega)-2s]_+.
$$


Using $x_j\ge s$, equation (12.5) gives


$$
|x_0-x_3|
\le v_p(Q^\Delta)+v_p(\Omega_{\rm red}).
$$


At balanced primes the left side is zero. Hence


$$
\boxed{
Z_X\mid\Omega_{\rm red}Q^\Delta.
}
\tag{12.6}
$$



This is stronger than the originally claimed divisor and is proved here, not merely restated.

---

# 13. Audit of the complete content divisibilities

Suppress the endpoint index. Let


$$
M=\gamma X,\qquad
V=\gamma Y+L\mathsf E,\qquad
\gcd(\gamma,|\mathsf E|)=1,
$$


and


$$
g^*=\gcd(|M|,|V|).
$$



A3’s cancellation integer satisfies


$$
\mathcal R=t_0L\mathsf E+\Omega\gamma\mathfrak b
=t_0V-r_0M.
\tag{13.1}
$$


Thus


$$
\mathcal C=\gcd(|X|,|\mathcal R|)
=\gcd(|X|,|t_0V|).
$$



Put


$$
e=\gcd(|X|,|V|).
$$


Then


$$
e\mid\mathcal C\mid t_0e.
\tag{13.2}
$$


Also


$$
g^*=e\gcd\left(\gamma,\frac{|V|}{e}\right),
$$


and


$$
\gcd(\gamma,|V|)
=\gcd(\gamma,L),
$$


because $\gcd(\gamma,|\mathsf E|)=1$. Hence


$$
e\mid g^*\mid Le.
\tag{13.3}
$$



Equations (13.2)–(13.3) prove


$$
\boxed{
g^*\mid L\mathcal C,\qquad
\mathcal C\mid t_0g^*.
}
\tag{13.4}
$$


They remain valid when $V=0$.

With


$$
K=\frac{\gamma|X|}{\mathcal C},\qquad
d=\frac{\gamma|X|}{g^*},
$$


one obtains


$$
-v_p(L)\le v_p(d)-v_p(K)\le v_p(t_0).
\tag{13.5}
$$



For the two endpoints, the reverse triangle inequality proves A3’s comparison


$$
\left|v_p(|AB|)-v_p(Z_K)\right|
\le v_p(Lt_0).
\tag{13.6}
$$



**Verdict:** the complete content divisibilities and their primewise consequence are correct. They retain the complete exponential force through $\mathsf E_j$, and the logarithmic contribution through the exact Wronskian identity. They do not estimate the remaining gcd.

---

# Part IV. New result: dual-Wronskian complete-row content reduction

## 14. Why a second elimination is useful

A3 used only


$$
t_0V-r_0M.
$$


That introduces $t_0$ as a possible comparison-loss factor, including primes coming from $\tau_n$.

The second Wronskian identity is equally exact:


$$
\boxed{
t_1V-r_1M
=t_1L\mathsf E-\Omega\gamma\mathfrak a.
}
\tag{14.1}
$$



Using both identities replaces the loss factor $t_0$ by $\gcd(t_0,t_1)$. In the present specialization, that replacement has an important support consequence.

---

## 15. Dual-content theorem

For $j=0,3$, define


$$
\mathcal R_j^{(0)}
=t_0L\mathsf E_j+\Omega\gamma_j\mathfrak b_j,
$$




$$
\mathcal R_j^{(1)}
=t_1L\mathsf E_j-\Omega\gamma_j\mathfrak a_j,
\tag{15.1}
$$


and


$$
\boxed{
\mathcal C_j^\sharp
=
\gcd\bigl(
|X_j|,\,
|\mathcal R_j^{(0)}|,\,
|\mathcal R_j^{(1)}|
\bigr).
}
\tag{15.2}
$$



Set


$$
K_j^\sharp=\frac{\gamma_j|X_j|}{\mathcal C_j^\sharp},
$$




$$
Z_{K^\sharp}
=\frac{K_0^\sharp K_3^\sharp}
{\gcd(K_0^\sharp,K_3^\sharp)^2}.
\tag{15.3}
$$



### Theorem 15.1 — Sharper complete-row content comparison

For each endpoint,


$$
\boxed{
g_j^*\mid L\mathcal C_j^\sharp,\qquad
\mathcal C_j^\sharp\mid G_tg_j^*,
}
\tag{15.4}
$$


where $G_t=\gcd(t_0,t_1)$.

Consequently,


$$
\boxed{
-v_p(L)
\le v_p(d_j)-v_p(K_j^\sharp)
\le v_p(G_t),
}
\tag{15.5}
$$


and


$$
\boxed{
\left|v_p(|AB|)-v_p(Z_{K^\sharp})\right|
\le v_p(LG_t).
}
\tag{15.6}
$$



### Proof

The two exact identities give


$$
\begin{aligned}
\mathcal C_j^\sharp
&=\gcd(|X_j|,|t_0V_j|,|t_1V_j|)\\
&=\gcd(|X_j|,|G_tV_j|).
\end{aligned}
\tag{15.7}
$$


Therefore, with $e_j=\gcd(|X_j|,|V_j|)$,


$$
e_j\mid\mathcal C_j^\sharp\mid G_te_j.
$$


The already proved relation


$$
e_j\mid g_j^*\mid Le_j
$$


then gives (15.4).

Since


$$
v_p(d_j)-v_p(K_j^\sharp)
=v_p(\mathcal C_j^\sharp)-v_p(g_j^*),
$$


equation (15.5) follows. Applying the reverse triangle inequality to the two denominator imbalances proves (15.6). ∎

Thus


$$
Z_{K^\sharp}\mid LG_t|AB|,
\qquad
|AB|\mid LG_tZ_{K^\sharp},
\tag{15.8}
$$


and


$$
\log|AB|_{\mathcal P^c}
=
\log(Z_{K^\sharp})_{\mathcal P^c}+O(n).
\tag{15.9}
$$



The exponential factor is justified because $G_t\le t_0$.

---

## 16. Exactness at every prime exceeding $n+1$

Since $G_t$ divides both $t_0$ and $t_1$,


$$
G_t\mid\Omega.
$$


But


$$
\Omega=\frac{4(-1)^nL^2}{n+1}.
$$


Every prime factor of $\Omega$, and hence of $G_t$, divides $L$.

The prime support of


$$
L=2^{n+1}\operatorname{lcm}(1,\ldots,n+1)
$$


is precisely the primes at most $n+1$. Therefore


$$
p>n+1\quad\Longrightarrow\quad p\nmid LG_t.
$$



Equation (15.5) now yields the exact result


$$
\boxed{
v_p(d_j)=v_p(K_j^\sharp)\qquad(p>n+1),
}
\tag{16.1}
$$


and hence


$$
\boxed{
|AB|_{>n+1}=(Z_{K^\sharp})_{>n+1}.
}
\tag{16.2}
$$



This is sharper than A3’s exactness condition $p\nmid Lt_0$. A large prime dividing $t_0$ is no longer exceptional.

### Structural versus complete-force cancellation

At $p>n+1$, if $p\mid\gamma_j$, then $\mathsf E_j$ is a unit and $L$ is a unit. Therefore $V_j$ is a unit, so


$$
v_p(g_j^*)=v_p(\mathcal C_j^\sharp)=0.
$$


The structural factor survives completely:


$$
v_p(d_j)=v_p(\gamma_j)+v_p(X_j).
\tag{16.3}
$$



If $p\nmid\gamma_j$, the exact cancellation is measured by


$$
v_p(\mathcal C_j^\sharp)
=
\min\left(
v_p(X_j),
v_p(\mathcal R_j^{(0)}),
v_p(\mathcal R_j^{(1)})
\right).
\tag{16.4}
$$



Because $\Omega$ is a unit at these primes, the two reference columns form an invertible local transformation. Thus complete-force cancellation at a large prime cannot be blamed on a singular reference normalization. It is a genuine congruence involving the specialized complete exponential numerator.

That is the useful sharper consequence of the new theorem.

---

## 17. The remaining specialized identity is now explicit

Define


$$
R_\gamma
=\frac{\gamma_0\gamma_3}{\gcd(\gamma_0,\gamma_3)^2},
$$




$$
R_{\mathcal C^\sharp}
=
\frac{\mathcal C_0^\sharp\mathcal C_3^\sharp}
{\gcd(\mathcal C_0^\sharp,\mathcal C_3^\sharp)^2}.
$$


At primes $p>n+1$, the exact formula gives


$$
\boxed{
\log|AB|_{>n+1}
\ge
\log(Z_X)_{>n+1}
-\log(R_\gamma)_{>n+1}
-\log(R_{\mathcal C^\sharp})_{>n+1}.
}
\tag{17.1}
$$


There is no comparison-error term here.

For the full complementary part, the corresponding estimate loses only


$$
\log(LG_t)=O(n).
$$



### Highest-value missing identity

The new result makes the complete-force cancellation target concrete:

> After substituting the actual five-moment expressions and the full finite exponential force, find a uniform arithmetic identity controlling
> 

$$
> \gcd\!\left(
> X_j,\,
> t_0L\mathsf E_j+\Omega\gamma_j\mathfrak b_j,\,
> t_1L\mathsf E_j-\Omega\gamma_j\mathfrak a_j
> \right),
>
$$


> or directly controlling the imbalance of these gcds between $j=0$ and $j=3$.

A particularly decisive sufficient identity would be an integer Bézout relation


$$
\begin{aligned}
U_{j,n}X_j
&+V_{j,n}
\bigl(t_0L\mathsf E_j+\Omega\gamma_j\mathfrak b_j\bigr)\\
&+W_{j,n}
\bigl(t_1L\mathsf E_j-\Omega\gamma_j\mathfrak a_j\bigr)
=B_{j,n}\ne0,
\end{aligned}
\tag{17.2}
$$


with a proved suitably small complementary-prime part of $B_{j,n}$, for example


$$
\log |B_{j,n}|_{\mathcal P^c}=O(n).
$$



Such an identity would bound $\mathcal C_j^\sharp$ after complete-force cancellation. It is **not proved here**, and its existence is not assumed. A useful endpoint-factor growth theorem would additionally need control of the structural-content imbalance $R_\gamma$, or a direct argument for $Z_{K^\sharp}$.

The exterior contribution in $\mathsf E_0$ is part of every term in this target. Removing it would produce a different gcd problem.

---

# Part V. Primitive normalization and whole errors

## 18. Ternary determinant route

The actual pair remains


$$
D_0=\det\Theta,\qquad
D_1=e_{\rm act}^T\operatorname{adj}(\Theta)e_{\rm act}
-3^{26}d_{\rm act}\det\Theta.
$$


When both are nonzero,


$$
v_3(q)
=
\max\left\{
0,\,
h-26+2v_3((n-1)!)
+v_3(D_1)-v_3(D_0)
\right\}.
\tag{18.1}
$$



Neither common matrix depth nor a determinant valuation alone replaces the complete relative pair.

With the least actual clearer,


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$




$$
g_\ell=\gcd(|A_\ell|,|B_\ell|),
$$


the primitive pair, when $B_\ell\ne0$, is


$$
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell}.
$$


Every prime remains in $g_\ell$.

The same-index whole error is


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}
{g_\ell}\det H_{\rm complete}.
}
\tag{18.2}
$$



If $B_\ell=0$, this positive-denominator construction does not apply. A local matrix certificate must not silently exclude or reinterpret that case.

---

## 19. Complete endpoint-weight route

After reducing the actual complete endpoint rows, retain


$$
\widetilde u_0=hA,\qquad
\widetilde u_3=hB,\qquad
\gcd(A,B)=1.
$$


Their absolute values give


$$
|AB|=\frac{d_0d_3}{\gcd(d_0,d_3)^2}.
$$



For reduced $\lambda=a/k$, $k>0$, retain


$$
J=B\widetilde v_0-A\widetilde v_3,\qquad
T=aJ+kA\widetilde v_3,
$$




$$
F_{\rm gcd}
=\gcd(|A|,|a|)\gcd(|B|,|a-k|),
$$




$$
G=\gcd(k,|J|),\qquad
H_{\rm gcd}
=\gcd\left(h,\frac{|T|}{F_{\rm gcd}G}\right).
$$



The actual primitive pair is


$$
\boxed{
q_\lambda
=\frac{kh|AB|}{F_{\rm gcd}GH_{\rm gcd}},\qquad
p_\lambda
=\operatorname{sgn}(AB)
\frac{T}{F_{\rm gcd}GH_{\rm gcd}}.
}
\tag{19.1}
$$


The formulas retain the final all-prime gcd. The usual $\gcd(m,0)=m$ convention covers a zero center; the lower bounds that divide by $|a|\,|a-k|$ must exclude $\lambda=0,1$.

The accepted selected-prime law remains


$$
(|AB|)_{\mathcal P}=5n.
\tag{19.2}
$$


The new content theorem does not extend this law to unselected primes.

The whole moving residue still includes


$$
F(n)=\sum_{t=0}^{n}n^{\underline t}
$$


and the full logarithmic restoration.

Finally,


$$
\boxed{
q_\lambda(e+\pi)-p_\lambda
=
q_\lambda e_3\alpha_{n,2}
(\lambda-\Lambda_{n,2}).
}
\tag{19.3}
$$



Neither transformation noncollapse, the repaired divisor, nor the new content comparison proves that the right side is nonzero or tends to zero.

---

# 20. Bounded arithmetic: additions to the planned $n=225$ calculation

No accepted computation should be regenerated. The coordinator’s personally authored $n=225$ complete-force/content calculation is still pending.

The new results require only **post-processing of that planned calculation’s exact data**, not a second producer construction.

### Inputs

Use its retained original input


$$
n=225=15^2,
$$


with:

- contact rows and columns $0,1,2$;
- all reconstructed coordinates $0,1,2,3$;
- complete force through $452$;
- moments through $227$;
- $\tau,\rho$ through $226$;
- the actual least two-column clearer and all row contents;
- the primitive triples and complete exponential numerators.

### New exact quantities to append

Compute


$$
G_t=\gcd(t_0,t_1),\qquad
\Omega_{\rm red}
=\frac{|\Omega|}{\gcd(|\Omega|,G_t^2)},
$$


and, for $j=0,3$,


$$
\mathcal R_j^{(1)}
=t_1L\mathsf E_j-\Omega\gamma_j\mathfrak a_j,
$$




$$
\mathcal C_j^\sharp,\qquad K_j^\sharp,\qquad Z_{K^\sharp}.
$$



### Expected verifiable outputs

The following are proved identity targets, not predicted favorable sizes:

1. Exact zero residuals:
   

$$
t_0V_j-r_0M_j-\mathcal R_j^{(0)}=0,
$$


   

$$
t_1V_j-r_1M_j-\mathcal R_j^{(1)}=0.
$$



2. Exact gcd identity:
   

$$
\mathcal C_j^\sharp=\gcd(|X_j|,|G_tV_j|).
$$



3. Exact divisibility checks:
   

$$
Z_X\mid\Omega_{\rm red}Q^\Delta,
$$


   

$$
g_j^*\mid L\mathcal C_j^\sharp,\qquad
   \mathcal C_j^\sharp\mid G_tg_j^*,
$$


   

$$
Z_{K^\sharp}\mid LG_t|AB|,\qquad
   |AB|\mid LG_tZ_{K^\sharp}.
$$



4. After removing every prime at most $226$,
   

$$
\boxed{
   |AB|_{>226}=(Z_{K^\sharp})_{>226}.
   }
$$


   This requires only division by the finitely many small primes, not complete factorization of the remaining large integer.

5. Reconstruction checks:
   

$$
\sum u_j=0,\qquad \sum v_j=1.
$$



The already accepted local theorem predicts


$$
\begin{array}{c|rrr}
p&v_p(d_0)&v_p(d_3)&v_p(|AB|)\\ \hline
3&218&220&2\\
5&107&110&3
\end{array}
$$


and selected part $1125$. These are predictions from the retained theorem, not outputs of a computation performed here.

If $\mathscr D=0$ at this particular finite input, report that fact and do not construct the reference-canceling weight. If it is nonzero, its weight and final primitive center must still be fully reduced.

Any error enclosure must evaluate the complete center against the complete $e+\pi$. An interval containing zero is inconclusive.

---

# 21. Proof-status ledger

| Statement | Status after this audit |
|---|---|
| Accepted depth $26$, actual/core agreement through depth $32$ | Reused under all original simultaneous hypotheses |
| A1 whole-layer Hankel compression modulo $3$ | Valid consequence of accepted whole-form normalization |
| Hankel compression at all six normalized digits | Not established in the same coordinates |
| A1 finite convolution kernel and endpoint action | Valid |
| A1 six-digit Smith/radical decision theorem | Valid |
| Family-wide $s_c<32$ | Open |
| A1 directional scalar guard | Valid conditional theorem |
| Evaluated whole core scalar passing the guard | Open |
| Coordinator exact finite pole pairing | Valid |
| Coordinator binomial valuation and sparse restriction | Valid |
| Supplied PASS receipt | Finite corroboration only; not rerun |
| Low-layer identity $P_0+P_1=-2F[(H-1)/2]$ | Proved here under the stated finite cutoff and degree bounds |
| Complete reduction through absolute precision $32$ | Derived here, with factorial omission justified by $h\ge32$ |
| A3 primitive correction-height comparison | Valid, including zero correction |
| Exponential bound for primitive moment-pair height | Open |
| A3 complete row-content divisibilities | Valid |
| A3 primewise $Lt_0$ comparison | Valid |
| $Z_X\mid|\Omega|Q^\Delta$ | Proved here with all primewise cancellation cases |
| Sharper $Z_X\mid\Omega_{\rm red}Q^\Delta$ | Proved here |
| Dual-Wronskian content theorem with factor $LG_t$ | Proved here |
| Exact complete endpoint factor comparison for $p>n+1$ | Proved here |
| Uniform specialized complete-force content bound | Open |
| Planned $n=225$ complete-force/content computation | Not yet a reported result |
| Same-index nonzero whole primitive errors tending to zero | Open |
| Rationality or irrationality of $e+\pi$ | Unresolved |

---

# 22. Conclusion

The central claims in A1 and A3 survive independent audit at their exact scopes. The important qualifications are not cosmetic:

- the Hankel compression is a **whole first-layer** statement;
- six matrix digits do not decide exact singularity when the sixth radical survives;
- the scalar guard must protect the **complete subtraction**;
- correction heights must be measured after primitive reduction;
- endpoint factors must be formed after both **complete rows** are reduced;
- the complete exponential force, including the exterior $+1$, remains inside the cancellation integers.

The main new arithmetic result is


$$
\boxed{
\left|v_p(|AB|)-v_p(Z_{K^\sharp})\right|
\le v_p(LG_t),
\qquad
|AB|_{>n+1}=(Z_{K^\sharp})_{>n+1}.
}
$$


It removes spurious large-prime exceptions arising from $t_0$ and isolates genuine complete-force cancellation.

The previously brief divisor argument is now closed, with the stronger result


$$
\boxed{
Z_X\mid
\frac{|\Omega|}{\gcd(|\Omega|,\gcd(t_0,t_1)^2)}
\,Q^\Delta.
}
$$



On the ternary side, the exact low-layer identity sharpens the complete core coefficient target to (7.6), but no normalized moment or endpoint-sensitive rank has yet been evaluated.

The highest-value remaining arithmetic identity is a specialized control of the **dual complete-force gcd** in (15.2), after substituting the actual finite force. The corresponding local core bottleneck remains the evaluated complete moment/radical problem and its whole endpoint scalar.

Globally, an irrationality proof still requires infinitely many original indices with actual primitive integers $p,q$ satisfying


$$
\boxed{0<|q(e+\pi)-p|\longrightarrow0.}
$$


That demands same-index control of the complete force, all row contents, the final all-prime gcd, the actual primitive denominator, and the whole evaluated error. None is supplied by the current reductions alone.



$$
\boxed{\text{No unconditional proof or disproof of irrationality of }e+\pi
\text{ has been obtained.}}
$$


