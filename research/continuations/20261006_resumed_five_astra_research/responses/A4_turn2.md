> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4, Turn 2 — Complete-force audit, a specialized moment–force Bézout identity, and corrections to the remaining computational bottlenecks

## Executive conclusions

The completed $n=225$ calculations change the finite evidence, but not the global proof status.

- The producer, whole-form enclosure, and dual-content post-processing are mutually consistent at the level of their formulas, boundaries, and normalization. I have inspected those formulas and the supplied data; **I have not executed or rerun the computations**.
- At this one original index, the reported large-prime parts
  

$$
(\gamma_0)_{>226}=(\gamma_3)_{>226}
  =(\mathcal C_0^\sharp)_{>226}=(\mathcal C_3^\sharp)_{>226}=1
$$


  are finite facts, not a support theorem.
- All five supplied primitive whole forms are certified nonzero and much larger than $1$. In particular, canceling the reference correction does **not** cancel the complete error.

The principal new symbolic result is an **actual specialized moment–force identity**, rather than another derivation of the closed generic dual-content theorem. With notation defined below, it is


$$
\boxed{
\mathcal Z\,N_j^{\exp}
=\alpha_j\mathcal P+\beta_j\mathcal Q,
\qquad j=0,3.
}
\tag{E1}
$$


Here $\mathcal P,\mathcal Q$ use the complete exponential force, and the polynomial terms in them retain the exterior $+1$.

After clearing only denominators supported on primes at most $n+1$, this identity yields integers $\mathcal B,\mathcal F$ satisfying


$$
\boxed{
\gamma_j\mid\mathcal B,
\qquad
\mathcal C_j^\sharp\mid G_t\mathcal F.
}
\tag{E2}
$$


The second divisibility comes from an explicit integer Bézout identity in the three original generators of $\mathcal C_j^\sharp$.

More precisely, at every prime


$$
p>n+1,\qquad p\nmid\mathcal B,
$$


the specialized complete-force cancellation has the exact description


$$
\boxed{
v_p(\mathcal C_j^\sharp)
=\min\{v_p(X_j),v_p(\mathcal F)\}.
}
\tag{E3}
$$


Thus the complete-force contents at both endpoints are controlled, away from an explicit moment exceptional factor, by **one common force resultant**. This is genuine progress on the requested arithmetic identity. It does not prove that the resultant or the relevant gcds have small large-prime parts.

Two other conclusions are important:

1. **A1’s Cartier reduction is valid**, provided coefficient integrality, precision, and the original cutoff are retained. An exact beta-integral formula below independently explains its section support and gives the valuations of its monomial weights.

2. **A2’s finite-binomial factorization survives inspection.** Its stated parameter bounds do not provide practical high-index evaluation. However, its discussion of accumulated nonunit losses can be sharpened decisively: the displayed first-order summand recurrence admits exact valuation/unit tracking with **no cumulative $29$-adic precision loss**. The unresolved obstruction is the original summation length and compressed high-index access, not an unavoidable factorial-sized precision guard.

No unconditional proof or disproof of the irrationality of $e+\pi$ is obtained.

---

# 1. Scope and treatment of the supplied evidence

The three original domains remain distinct.

### Ternary core

Retain


$$
n=4^j+1,\qquad j>0,\qquad81\mid j,
$$




$$
H=3^{h-1},\qquad n-2=H-D,\qquad 0<D<H/972,
$$


and the original finite LOW, residual, and HIGH columns. Applications to the depth-$26$ Schur coefficient retain all the simultaneous support, degree, saturation, and transfer hypotheses recorded in A4 Turn 1.

### Complete endpoints

Retain


$$
n=15^r,\quad r\ge2,
\qquad\text{or}\qquad
n=105^r,\quad r\ge2,
$$


with contact coordinates $0,1,2$, reconstructed coordinates $0,1,2,3$, and complete force through $2n+2$.

The accepted nonvanishing hypotheses


$$
\Delta_T\ne0,\qquad \xi_0\xi_3\ne0
$$


remain necessary.

### $29$-adic contact route

Retain exactly


$$
b=3^{249005515+574312172u},\qquad n=2001b,\qquad u\ge0,
$$


with contact coordinates $0,\ldots,b-1$, source rows $1,\ldots,b-2$, and reconstruction through $j=b$.

The supplied literature gate is used as background about established methods. It does not supply a target-specific kernel evaluator, content bound, or irrationality theorem.

---

# 2. Independent inspection of the completed $n=225$ work

## 2.1 Finite boundaries and complete forces

The producer uses


$$
n=225,\qquad 2n+2=452.
$$


Its factorial and complete-force arrays run through index $452$, inclusive. Its five moments are exactly


$$
c_{223},c_{224},c_{225},c_{226},c_{227}.
$$



For contact row $i=0,1,2$, the source loop is


$$
0\le j\le n+i.
$$


Because $n+i<2n$, this is exactly


$$
0\le j\le\min(2n,n+i).
$$


Its exponential part is therefore the complete finite expression


$$
w_i^{\exp}
=
\sum_{j=0}^{n+i}
q_j(n+i)^{\underline j}
(2n+i-j)!
\sum_{r=0}^{2n+i-j}\frac1{r!}.
\tag{2.1}
$$


No exponential tail inside this finite force is removed.

The logarithmic recurrence uses the coefficients of


$$
(1-z+z^2/2)^{-1}
$$


through the last index required by the force. The reconstructed complete numerator is checked against


$$
N_j^{\rm whole}
=
N_j^{\exp}
+4n!\bigl(\alpha_j\rho_n+\beta_j\rho_{n+1}\bigr).
\tag{2.2}
$$



At endpoint $0$,


$$
N_0^{\exp}=\Delta_T+R_0\widehat w^{\exp}.
$$


The determinant term is present. At endpoint $3$,


$$
N_3^{\exp}=R_3\widehat w^{\exp}.
$$



These are the correct complete endpoint numerators.

## 2.2 Reconstruction and the least all-row clearer

The code applies the stated triangular contact transformation and then reconstructs


$$
u=(-s_x{}_0,\ s_x{}_0-s_x{}_1,\ s_x{}_1-s_x{}_2,\ s_x{}_2),
$$




$$
v=(1-s_y{}_0,\ s_y{}_0-s_y{}_1,\ s_y{}_1-s_y{}_2,\ s_y{}_2).
$$


Consequently,


$$
\sum_{j=0}^3u_j=0,\qquad
\sum_{j=0}^3v_j=1.
\tag{2.3}
$$


The post-processing explicitly checks these two identities.

The clearer is computed as the lcm of the reduced denominators of **all eight entries** of $u$ and $v$. That is the least positive common clearer of those entries—not an endpoint-only clearer.

The supplied row contents are


$$
(508500,\ 28350,\ 15525,\ 772).
\tag{2.4}
$$


Their factorizations are


$$
\begin{aligned}
508500&=2^2\,3^2\,5^3\,113,\\
28350&=2\,3^4\,5^2\,7,\\
15525&=3^3\,5^2\,23,\\
772&=2^2\,193.
\end{aligned}
$$


In particular, row reduction already involves unselected primes. Their presence must not be replaced by the selected $\{3,5\}$-part.

The content of the eight cleared entries together is $1$, consistent with—but not by itself a substitute for—the lcm construction of the least clearer.

## 2.3 Signs and primitive endpoint normalization

The supplied signed endpoint factors have


$$
A>0,\qquad B<0.
$$


The auxiliary endpoint coordinates have


$$
M_0<0,\qquad M_3>0.
$$


This is consistent with the common rational scale relating the auxiliary rows to the actual reconstructed rows being negative. It is exactly why one must distinguish:

- positive reduced denominators $d_j$;
- signed primitive first coordinates;
- the signed factors $A,B$.

The code does so. It uses


$$
q_\lambda>0,
\qquad
p_\lambda
=
\operatorname{sgn}(AB)\,
\frac{T}{F_{\rm gcd}GH_{\rm gcd}},
$$


and verifies both


$$
\frac{p_\lambda}{q_\lambda}
=
\lambda\frac{v_0}{u_0}
+(1-\lambda)\frac{v_3}{u_3}
$$


and


$$
\gcd(|p_\lambda|,q_\lambda)=1.
$$


Thus the final reduction is an **all-prime** reduction.

## 2.4 What the supplied dual-content data establish

The supplied data have


$$
g_0^*=g_3^*=L.
\tag{2.5}
$$


They also give


$$
\mathcal C_3^\sharp=G_t,\qquad
\mathcal C_0^\sharp=637\,G_t,
\qquad 637=7^2\cdot13.
\tag{2.6}
$$


At this input, the displayed single- and dual-content values coincide:


$$
\mathcal C_j^\sharp=\mathcal C_j,
$$


and consequently the supplied $Z_{K^\sharp}$ and $Z_K$ coincide.

These additional equalities are features of this finite case. They do not make the dual sharpening redundant as a theorem: the latter removes the possible large-prime loss from $t_0$ uniformly.

The receipt reports


$$
|AB|_{>226}=(Z_{K^\sharp})_{>226},
$$


with $2314$ decimal digits, and large-prime parts of $\gamma_j,\mathcal C_j^\sharp$ equal to $1$.

The accepted selected-prime values are also corroborated:


$$
\begin{array}{c|ccc}
p&v_p(d_0)&v_p(d_3)&v_p(|AB|)\\ \hline
3&218&220&2\\
5&107&110&3
\end{array}
$$


so


$$
(|AB|)_{\{3,5\}}=1125=5n.
$$



None of these facts establishes a family-wide support or growth theorem.

## 2.5 Rational enclosures of the whole forms

The enclosure code uses


$$
e_{\rm lo}=\sum_{k=0}^{N}\frac1{k!},
\qquad
e_{\rm hi}=e_{\rm lo}
+\frac{N+2}{(N+1)(N+1)!},
\qquad N=768.
$$


The upper tail is valid because


$$
\sum_{r\ge0}\frac1{(N+1+r)!}
\le
\frac1{(N+1)!}
\sum_{r\ge0}\frac1{(N+2)^r}.
$$



For each arctangent, the partial sum has an even number $N$ of terms and ends with a negative term. It is a lower bound; adding the next positive term is an upper bound. The code then uses


$$
\pi=16\arctan(1/5)-4\arctan(1/239)
$$


with the subtraction bounds in the correct order.

Finally, it forms


$$
qS_{\rm lo}-p<q(e+\pi)-p<qS_{\rm hi}-p
$$


using the already reduced positive $q$. It encloses the **whole form**, not a component of the error.

The reported conclusions are:

| Weight | Sign of $q(e+\pi)-p$ | Certified $\lfloor\log_{10}|\text{form}|\rfloor$ |
|---|---:|---:|
| endpoint $3$ | $-$ | $1815$ |
| endpoint $0$ | $-$ | $1817$ |
| $1/2$ | $-$ | $2976$ |
| $n^2/2$ | $+$ | $2974$ |
| reference-canceling | $-$ | $1290$ |

Thus all five are nonzero and have absolute value greater than $1$. The reference cancellation removes its designated reference term, not the complete same-index error.

---

# 3. A1’s universal Cartier reduction: valid scope and a whole-functional sharpening

## 3.1 Audit of the reduction

At modulus $3^{27}$, A1 assumes


$$
h\ge27,\qquad F\in\mathbb Z_3[y],\qquad
\deg F\le H-2D.
$$


These hypotheses matter separately:

- $h\ge27$ permits the stated lifted Frobenius precision and factorial omission.
- Coefficient integrality prevents multiplication by $3^h$ from concealing a coefficient denominator.
- The degree bound ensures that the **entire support** of $(y-1)^HF$ is inside the original pole cutoff.

Set


$$
g=3^{h-27},\qquad M=3^{26},\qquad \rho=(g-1)/2.
$$


The congruence


$$
(y-1)^H\equiv(y^g-1)^M\pmod{3^{27}}
$$


is correct, and


$$
\mathcal C_g(A(y^g)F)=A(z)\mathcal C_gF
$$


is an exact coefficient identity.

The pole positions satisfy


$$
\frac{gc3^{27-\ell}-1}{2}
=
g\frac{c3^{27-\ell}-1}{2}+\rho.
$$


Thus the transformed cutoff in A1 is precisely the original cutoff, not a replacement of it.

The formulas for both the complete functional and the separate $\Delta_H$ layers are consequently valid at their stated precisions.

For corrected products,


$$
F_{ij}=x^D(\beta+3y)\psi_i\psi_j,
$$


both corrected factors remain necessary. Precision-$25$ representatives are usable through the accepted whole-pairing comparison; they are not coefficientwise precision-$27$ substitutes.

The remaining obstruction is still the evaluation of the Cartier sections of these **complete corrected products through the finite return**, including the HIGH boundary restrictions.

## 3.2 New exact beta-functional formula

There is a useful independent way to see the complete section support.

Define the complete pole functional


$$
\mathscr P_H(F)
=
\sum_{\ell=0}^{h}P_\ell((y-1)^HF).
$$


Because every coefficient is inside the original cutoff and


$$
2R_{\max}+1<4H<3^{h+1},
$$


the pole layers partition the denominators exactly:


$$
\mathscr P_H(F)
=
3^h\sum_v\frac{[(y-1)^HF]_v}{2v+1}.
\tag{3.1}
$$


For $F(y)=\sum_kF_k y^k$, beta integration gives the exact rational identity


$$
\boxed{
\mathscr P_H(F)
=
\sum_k F_k\,W_{H,k},
\qquad
W_{H,k}
=
-\frac{3^h\,2^H H!}
{\displaystyle\prod_{r=0}^{H}(2k+2r+1)}.
}
\tag{3.2}
$$


Indeed,


$$
\int_0^1 t^{2k}(t^2-1)^H\,dt
=
-\frac{2^HH!}{\prod_{r=0}^{H}(2k+2r+1)},
$$


since $H$ is odd.

This formula contains all pole layers and all their cancellations at once.

### Exact valuations of the weights

For $0\le k<H$, put


$$
r_*=(H-1)/2.
$$


Counting multiples of powers of $3$ in the denominator gives


$$
\boxed{
v_3(W_{H,k})
=
h-\min\{v_3(2k+1),h-1\}
-\mathbf1_{k\ge r_*}.
}
\tag{3.3}
$$



To verify this, write $H=3^{h-1}$. For each $a\le h-1$, the $H+1$ consecutive odd terms contain


$$
H/3^a+\mathbf1_{3^a\mid 2k+1}
$$


multiples of $3^a$. At level $3^h=3H$, there is one additional multiple exactly when $k\ge r_*$. There are no higher multiples.

In particular:

- at $k=r_*$, the weight is a unit;
- below $r_*$, the valuation is $h-v_3(2k+1)$;
- above $r_*$, it is $h-1-v_3(2k+1)$.

At modulus $3^K$, $K\le h$, every surviving coefficient therefore satisfies


$$
3^{h-K}\mid 2k+1.
\tag{3.4}
$$


Below the midpoint there is the stronger necessary condition


$$
3^{h-K+1}\mid 2k+1.
$$



Equation (3.4) is exactly the Cartier residue class


$$
k\equiv \frac{3^{h-K}-1}{2}\pmod{3^{h-K}}.
$$


Thus the section dependence is also a consequence of an exact whole-functional valuation calculation.

This does **not** evaluate the required corrected section. Nor does it make the universal $3^{26}$-scale calculation small. It does, however, identify the complete monomial weights and explains why separate low-layer terms cannot be interpreted before their cancellation.

## 3.3 Unchanged finite return and endpoint obligations

The moment recurrence still ends at


$$
0\le i\le\nu-2,
$$


and no moment beyond index $D-4$ is added:


$$
\lambda_{i+\nu}
+\sum_{k=0}^{\nu-1}\bar f_k\lambda_{i+k}
=\bar b_i^{\langle26\rangle}.
$$


The terminal equation remains


$$
J^T\varepsilon+\omega
=
-\varepsilon-s\bigl(\theta e_{\nu-1}
+3^{26}b^{\langle26\rangle}\bigr).
$$


Neither the complete forcing nor $\omega_{\nu-1}$ is removed by the new coefficient formula.

---

# 4. A2’s atom reduction: audit and a decisive precision correction

## 4.1 Finite transforms and parameter bounds

The finite upper-transform identity in A2 is correct. Its subtraction over


$$
0\le\ell\le B-b
$$


is exactly the missing tail of the unrestricted Vandermonde convolution. It is essential when $B\ge b$.

The divided-power identity is also correct:


$$
\mathsf D E(A,B;r)
=
\sum_{s=0}^{M}c_s(n)\binom{r+s}{s}
E(A,B+s;r+s).
$$



The particular input is correctly written as an algebraic extension minus the head


$$
\tau=g-\eta.
$$


The condition $j\le d+1$ in $\eta$ removes precisely the nonexistent source rows. Its high-binomial table has the stated range


$$
-G\le\delta\le1.
$$



The final parameter box survives inspection. In particular, the potentially largest offsets in the particular path are bounded by


$$
G+M=116K-2<120K+4.
$$


The endpoint solve forms scalar combinations and introduces no new atom labels.

These are algebraic and finite-boundary conclusions. Their construction cost is conditional on the specified high-index scalar inputs.

## 4.2 The actual reconstructed Gram kernel is retained

For $j<b$,


$$
jE_\alpha(j-1)-E_\alpha(j)
=
(r+1)E(A,b+v+1;r+1)_j-E_\alpha(j).
$$


At $j=b$, only


$$
bE_\alpha(b-1)
$$


occurs. Thus A2 correctly retains


$$
b^2W_b^2e_\alpha e_\beta
$$


in the atom Gram matrix.

The exterior contribution is separately


$$
bW_b^2\sum_\alpha z_{f,\alpha}e_\alpha.
$$


It is not part of the contact Gram matrix and must remain in the complete defect.

The $O(K^5)$ parameter count is therefore a valid count of a sufficient scalar table. It is not an evaluation of that table.

## 4.3 New correction: cumulative denominator valuation is not necessary

A2’s literal precision budget $E_{\rm rat}$ is a valid conservative bound for a particular implementation. But it is not an intrinsic precision obstruction.

For a nonsingleton kernel, let $U_j$ denote its exact integer summand. On its nonzero range,


$$
\frac{U_{j+1}}{U_j}=\frac{N_j}{D_j},
$$


where


$$
N_j=(n+2-j)^2(B-j)(B'-j),
$$




$$
D_j=(j+1)(j+1-t)
(A-B+j+1)(A'-B'+j+1).
$$


For $j_0=t\le j<J$, none of these factors is zero.

Write


$$
N_j=p^{a_j}N_j^\times,\qquad
D_j=p^{b_j}D_j^\times,
\qquad p=29,
$$


with unit parts in $\mathbb Z_p^\times$, and write


$$
U_j=p^{v_j}u_j,\qquad u_j\in\mathbb Z_p^\times.
$$


Then the exact recurrence is


$$
\boxed{
v_{j+1}=v_j+a_j-b_j,
\qquad
u_{j+1}
=
u_jN_j^\times(D_j^\times)^{-1}.
}
\tag{4.1}
$$



This updates the unit part modulo $p^K$ using only unit inversions. There is **no accumulation of lost digits**.

A summand with $v_j\ge K$ contributes zero to the current sum, but its unit part must still be carried: later summands can return to smaller valuation. Discarding that hidden unit state would be an error.

### Initialization budget

If initialization is performed by first computing the ordinary integer $U_t$, it suffices to know it modulo


$$
p^{K+v_p(U_t)}.
$$


This is much smaller than the accumulated denominator budget.

For negative upper parameters, replace


$$
\binom{-\alpha}{k}
=
(-1)^k\binom{\alpha+k-1}{k}.
$$


Kummer’s carry formula then bounds each binomial valuation by the number of base-$p$ digits of its nonnegative upper index. If


$$
T_{\max}=\max\{n+2,\alpha+B-1,\alpha'+B'-1\},
$$


then, whenever $t\le J$,


$$
v_p(U_t)\le4\lfloor\log_p T_{\max}\rfloor.
\tag{4.2}
$$


The factor $\binom tt$ contributes no valuation. Along the range, a corresponding bound with coefficient $5$ covers the extra factor $\binom jt$.

Thus the first-order kernel recurrence has a division-safe forward evaluator with fixed unit precision and a logarithmic initialization guard.

### What remains hard

This correction does not turn the evaluator into a feasible original-index algorithm:

- it still has up to $b$ steps;
- its initial high binomials still require evaluation;
- exact valuations and unit parts of the affine factors still require suitable high-index access;
- the complete scalar combination must still be evaluated at the true norm depth.

At $u=0$,


$$
b=3^{249005515}
$$


has more than $8.1\times10^7$ base-$29$ digits. Those digits are not a short input merely because the exponent has a short description.

Fast modular exponentiation supplies $b\bmod29^s$ at a prescribed small $s$. It does not automatically provide a compressed action of an original-length kernel sum or all of its digit/carry structure.

The corrected local bottleneck is therefore:

> Prove a compressed block-summation or observable recurrence for the complete kernels, including initialization and boundaries, whose cost is controlled by the exponent description and precision—not by $b$ or an uncompressed base-$29$ expansion.

---

# 5. New specialized arithmetic: collapsing the complete exponential force

I now address the requested endpoint content problem directly.

Write


$$
\phi(z)=1-z+\frac{z^2}{2},\qquad
f(z)=e^z\phi(z)^n=\sum_{k\ge0}c_kz^k.
$$


Set


$$
\mathsf b=c_{n-1},\qquad
\mathsf c=c_n,\qquad
\mathsf d=c_{n+1}.
$$



## 5.1 A generating function for the complete exponential force

Let


$$
E_m=m!\sum_{r=0}^{m}\frac1{r!},
$$


and define


$$
A_n(z)=\sum_{k\ge0}\frac{E_{n+k}}{k!}z^k.
$$


Since


$$
E_{m+1}=(m+1)E_m+1,
$$


one has


$$
(1-z)A_n'(z)=(n+1)A_n(z)+e^z.
$$


Its initial value is $A_n(0)=E_n$, and hence


$$
\boxed{
A_n(z)
=
\frac{e^z\,n!\displaystyle\sum_{r=0}^{n}(1-z)^r/r!}
{(1-z)^{n+1}}.
}
\tag{5.1}
$$



Define


$$
W(z)=\phi(z)^nA_n(z)=\sum_{k\ge0}\omega_kz^k.
$$


The coefficient formula gives


$$
\omega_{n+i}
=
\sum_{j=0}^{n+i}
q_j\,\frac{E_{2n+i-j}}{(n+i-j)!}
=
\widehat w_i^{\exp},
\qquad i=0,1,2.
\tag{5.2}
$$


Thus $W$ represents the **complete** finite exponential force already used by the producer.

## 5.2 A force relation on exactly the three contact rows

The generating functions satisfy


$$
(1-z)\phi W'
=
\bigl(n(1-z)\phi'+(n+1)\phi\bigr)W+\phi f.
$$


Expanding the polynomial factors yields


$$
\begin{aligned}
(k+1)\omega_{k+1}
={}&(2k+1)\omega_k
+\frac{2n+1-3k}{2}\omega_{k-1}\\
&+\frac{k-n-1}{2}\omega_{k-2}
+c_k-c_{k-1}+\frac12c_{k-2}.
\end{aligned}
\tag{5.3}
$$


At $k=n+1$, the $\omega_{n-1}$ coefficient vanishes:


$$
\boxed{
(n+2)\omega_{n+2}
=
(2n+3)\omega_{n+1}
-\frac{n+2}{2}\omega_n
+\mathsf d-\mathsf c+\frac{\mathsf b}{2}.
}
\tag{5.4}
$$


This is an exact relation on the actual contact triple. No additional source row has been introduced.

The moment generating function similarly gives


$$
(k+1)c_{k+1}
=
(k+1-n)c_k
+\frac{2n-k-1}{2}c_{k-1}
+\frac12c_{k-2},
$$


so


$$
\boxed{
2(n+2)c_{n+2}
=
4\mathsf d+(n-2)\mathsf c+\mathsf b.
}
\tag{5.5}
$$



---

# 6. The specialized moment–force syzygy

Retain


$$
T=
\begin{pmatrix}
c_n&c_{n-1}&c_{n-2}\\
c_{n+1}&c_n&c_{n-1}\\
c_{n+2}&c_{n+1}&c_n
\end{pmatrix},
\qquad \Delta_T=\det T,
$$


and


$$
\ell_0=(-1,n,-n(n+1)),\qquad
\ell_3=(0,0,1),
$$




$$
R_j=\ell_j\operatorname{adj}(T).
$$



The two reference vectors are


$$
v=
\begin{pmatrix}
1\\[1mm]1/2\\[1mm](n+1)/(2(n+2))
\end{pmatrix},
\qquad
w=
\begin{pmatrix}
0\\[1mm]1/2\\[1mm](2n+3)/(2(n+2))
\end{pmatrix},
$$


with


$$
\alpha_j=R_jv,\qquad \beta_j=R_jw.
$$



Define the three specialized scalars


$$
\boxed{
\mathcal Z
=
\mathsf b+(n-3)\mathsf c-2(n-1)\mathsf d,
}
\tag{6.1}
$$




$$
\boxed{
\mathcal P
=
\mathcal Z\,\omega_n
+3\mathsf c^2-2\mathsf d(\mathsf b+\mathsf c),
}
\tag{6.2}
$$




$$
\boxed{
\mathcal Q
=
\mathcal Z(2\omega_{n+1}-\omega_n)
-(2\mathsf d-\mathsf c)^2.
}
\tag{6.3}
$$



## Theorem 6.1 — Complete endpoint moment–force identity

For $j=0,3$,


$$
\boxed{
\mathcal ZN_j^{\exp}
=
\alpha_j\mathcal P+\beta_j\mathcal Q.
}
\tag{6.4}
$$


This identity retains the exterior $+1$ in $N_0^{\exp}$.

### Proof

Let


$$
\eta=\left(\frac{n+2}{2},-(2n+3),n+2\right).
$$


Then


$$
\eta v=\eta w=0.
$$


Equations (5.4)–(5.5) give


$$
\eta\bigl(\widehat w^{\exp}-Te_0\bigr)
=(n+1)(2\mathsf d-\mathsf c),
\tag{6.5}
$$


and


$$
\eta T
\begin{pmatrix}n\\1\\0\end{pmatrix}
=(n+1)\mathcal Z.
\tag{6.6}
$$


Therefore the vector


$$
\mathcal Z(\widehat w^{\exp}-Te_0)
-(2\mathsf d-\mathsf c)\,
T\begin{pmatrix}n\\1\\0\end{pmatrix}
$$


lies in the span of $v,w$.

Its first two coordinates identify that vector exactly as


$$
\boxed{
\mathcal Z(\widehat w^{\exp}-Te_0)
-(2\mathsf d-\mathsf c)\,
T\begin{pmatrix}n\\1\\0\end{pmatrix}
=
\mathcal Pv+\mathcal Qw.
}
\tag{6.7}
$$


For both endpoints,


$$
\ell_j(n,1,0)^T=0.
$$


Also


$$
\ell_0e_0=-1,\qquad \ell_3e_0=0.
$$


Multiplication by $R_j$, using $R_jT=\Delta_T\ell_j$, turns the left side into


$$
\mathcal Z\bigl(R_j\widehat w^{\exp}
-\Delta_T\ell_je_0\bigr)
=\mathcal ZN_j^{\exp}.
$$


This proves (6.4). ∎

### Why the exterior term is substantive

The terms


$$
3\mathsf c^2-2\mathsf d(\mathsf b+\mathsf c),
\qquad
-(2\mathsf d-\mathsf c)^2
$$


are not optional corrections. They arise from the subtraction of $Te_0$, which encodes the endpoint-$0$ exterior contribution.

Dropping $+1$ would change the specialized resultant below.

## 6.1 A companion determinant identity

The same calculation gives


$$
\boxed{
\alpha_0\beta_3-\beta_0\alpha_3
=
\Delta_T\,\frac{n+1}{2(n+2)}\,\mathcal Z.
}
\tag{6.8}
$$


For example, this follows from


$$
R_0\times R_3
=
\Delta_T\,T(n,1,0)^T,
\qquad
v\times w=\frac{\eta^T}{2(n+2)}.
$$



Thus nonvanishing of the primitive two-endpoint moment determinant at $n=225$, together with $\Delta_T\ne0$, proves


$$
\mathcal Z\ne0
$$


at that finite input.

It is not necessary to assume $\mathcal Z\ne0$ to prove the polynomial identity (6.4). Nonvanishing is necessary for the effective divisor bounds that follow.

---

# 7. An explicit integer Bézout identity for $\mathcal C_j^\sharp$

## 7.1 A clearer supported only through $n+1$

Put


$$
D=2^n(n+1)!.
$$


This clears


$$
\mathsf b,\mathsf c,\mathsf d,\omega_n,\omega_{n+1}.
$$


For the force coefficients this follows directly from


$$
\omega_m
=
\sum_{j=0}^{m}q_j\frac{E_{n+m-j}}{(m-j)!},
\qquad m=n,n+1.
$$



Consequently,


$$
Z_0=D\mathcal Z,\qquad
P_0=D^2\mathcal P,\qquad
Q_0=D^2\mathcal Q
$$


are integers. Define


$$
\boxed{
\mathcal B=n!D Z_0=n!D^2\mathcal Z.
}
\tag{7.1}
$$


Every prime factor introduced by $n!D$ is at most $n+1$.

Retain the actual primitive triple


$$
\sigma_j(\alpha_j,\beta_j,N_j^{\exp}/n!)
=
(\gamma_j\mathfrak a_j,\gamma_j\mathfrak b_j,\mathsf E_j),
$$


where


$$
\gcd(\mathfrak a_j,\mathfrak b_j)=1,
\qquad
\gcd(\gamma_j,\mathsf E_j)=1.
$$



Multiplying (6.4) by the prescribed factors gives


$$
\boxed{
\mathcal B\,\mathsf E_j
=
\gamma_j(\mathfrak a_jP_0+\mathfrak b_jQ_0).
}
\tag{7.2}
$$


Therefore


$$
\boxed{\gamma_j\mid\mathcal B.}
\tag{7.3}
$$



This is a specialized structural-content divisor. It was not available from the generic dual-Wronskian identity alone.

## 7.2 The common complete-force resultant

Define


$$
U=\mathcal B r_0+LP_0,\qquad
W=\mathcal B r_1+LQ_0,
$$


and


$$
\boxed{
\mathcal F=t_0W-t_1U
=
\mathcal B\Omega+L(t_0Q_0-t_1P_0).
}
\tag{7.4}
$$


The term $\mathcal B\Omega$ is the complete logarithmic restoration.

Equivalently,


$$
\mathcal F
=
D^2L^2
\left(
\tau_n\mathcal Q-\tau_{n+1}\mathcal P
+\frac{4(-1)^nn!\mathcal Z}{n+1}
\right).
\tag{7.5}
$$



Since $\gamma_j\mid\mathcal B$, put


$$
b_j^\flat=\mathcal B/\gamma_j\in\mathbb Z.
$$


Using the complete row


$$
V_j=\gamma_jY_j+L\mathsf E_j,
$$


equation (7.2) becomes


$$
\boxed{
b_j^\flat V_j
=
\mathfrak a_jU+\mathfrak b_jW.
}
\tag{7.6}
$$


Together with


$$
X_j=\mathfrak a_jt_0+\mathfrak b_jt_1,
$$


this is a common two-column transformation for the actual specialized force.

## Theorem 7.1 — Specialized complete-force Bézout identity

For each endpoint,


$$
\boxed{
\mathcal C_j^\sharp\mid G_t\mathcal F.
}
\tag{7.7}
$$



### Explicit coefficients and proof

Choose integers $s,t$ such that


$$
st_0+tt_1=G_t,
$$


and choose integers $\lambda_j,\mu_j$ such that


$$
\lambda_j\mathfrak a_j+\mu_j\mathfrak b_j=1.
$$


Set


$$
c_j=\mu_jt_0-\lambda_jt_1.
$$


Equations (7.6) and the definition of $\mathcal F$ give


$$
(\lambda_jW-\mu_jU)X_j+c_jb_j^\flat V_j=\mathcal F.
\tag{7.8}
$$



The original cancellation generators satisfy


$$
s\mathcal R_j^{(0)}+t\mathcal R_j^{(1)}
=
G_tV_j-(sr_0+tr_1)\gamma_jX_j.
$$


Substitution into $G_t$ times (7.8) yields the integer identity


$$
\boxed{
\begin{aligned}
&\Bigl[
G_t(\lambda_jW-\mu_jU)
+c_j\mathcal B(sr_0+tr_1)
\Bigr]X_j\\
&\quad+c_jb_j^\flat s\,\mathcal R_j^{(0)}
+c_jb_j^\flat t\,\mathcal R_j^{(1)}
=G_t\mathcal F.
\end{aligned}
}
\tag{7.9}
$$


Every generator of $\mathcal C_j^\sharp$ therefore divides the right side. ∎

This is the requested form of an actual moment/force Bézout identity. Its right side is fully specified by three moments and the complete force.

---

# 8. Exact large-prime cancellation and imbalance

The new identity becomes especially transparent away from the moment exceptional factor.

## Theorem 8.1 — Exact common-resultant law

Suppose


$$
p>n+1,\qquad p\nmid\mathcal B.
$$


Then


$$
\boxed{
v_p(\mathcal C_j^\sharp)
=
\min\{v_p(X_j),v_p(\mathcal F)\}.
}
\tag{8.1}
$$



### Proof

At such a prime:

- $L,G_t,\Omega$ are units;
- $\gamma_j$ is a unit by $\gamma_j\mid\mathcal B$;
- $b_j^\flat=\mathcal B/\gamma_j$ is a unit;
- the row $(t_0,t_1)$ is primitive over $\mathbb Z_p$.

Complete $(t_0,t_1)$ to a unimodular two-row matrix. Under this transformation, the primitive vector


$$
(\mathfrak a_j,\mathfrak b_j)^T
$$


has coordinates $(X_j,z_j)^T$. If $p\mid X_j$, then $z_j$ is a unit.

The second form $\mathfrak a_jU+\mathfrak b_jW$ has, in these coordinates, the form


$$
aX_j+u\mathcal Fz_j,
\qquad u\in\mathbb Z_p^\times.
$$


Hence


$$
\min\!\left(
v_p(X_j),
v_p(\mathfrak a_jU+\mathfrak b_jW)
\right)
=
\min\{v_p(X_j),v_p(\mathcal F)\}.
$$


Equation (7.6), together with the unit status of $b_j^\flat$, identifies the second valuation with $v_p(V_j)$. Finally, the closed dual identity gives


$$
v_p(\mathcal C_j^\sharp)=\min\{v_p(X_j),v_p(V_j)\}
$$


at $p>n+1$. ∎

Writing


$$
x_j=v_p(X_j),\qquad f=v_p(\mathcal F),
$$


the actual endpoint denominator has the exact exponent


$$
\boxed{
v_p(d_j)=(x_j-f)_+.
}
\tag{8.2}
$$


Therefore


$$
\boxed{
v_p(|AB|)
=
\left|(x_0-f)_+-(x_3-f)_+\right|.
}
\tag{8.3}
$$



This is an explicit imbalance law: at these primes, complete-force cancellation applies one common truncation threshold $f$ to the two endpoint $X$-valuations.

## 8.1 Global large-prime divisor consequences

When $\mathcal B\mathcal F\ne0$,


$$
R_\gamma
=\frac{\gamma_0\gamma_3}{\gcd(\gamma_0,\gamma_3)^2}
\mid|\mathcal B|,
$$


and


$$
R_{\mathcal C^\sharp}
=
\frac{\mathcal C_0^\sharp\mathcal C_3^\sharp}
{\gcd(\mathcal C_0^\sharp,\mathcal C_3^\sharp)^2}
\mid G_t|\mathcal F|.
$$


Thus the earlier large-prime lower comparison sharpens to the fully specialized bound


$$
\boxed{
\log|AB|_{>n+1}
\ge
\log(Z_X)_{>n+1}
-\log|\mathcal B|_{>n+1}
-\log|\mathcal F|_{>n+1}.
}
\tag{8.4}
$$


Moreover,


$$
|\mathcal B|_{>n+1}=|Z_0|_{>n+1}.
$$



These identities reduce the outstanding arithmetic to a linear three-moment factor and a common complete-force resultant.

## 8.2 What this does not prove

The strong support assertion


$$
(\mathcal C_j^\sharp)_{>n+1}=1
$$


does not follow merely from (7.7). One would need to control the primes of $\mathcal F$, or prove that they do not meet the relevant $X_j$.

Indeed, away from $\mathcal B$, equation (8.1) says precisely that the support question is


$$
\gcd(X_j,\mathcal F)_{>n+1}=1.
$$


The remaining question is therefore a genuine specialized resultant-coprimality problem, not a consequence of the reference Wronskian being a unit.

A straightforward size estimate gives only


$$
\log|\mathcal B|,\ \log|\mathcal F|
\le 3n\log n+O(n)
$$


when the quantities are nonzero. For example,


$$
|\omega_n|
\le e(5/2)^n\frac{(2n)!}{n!},
$$


with an analogous bound for $\omega_{n+1}$. This is not the desired complementary-prime $O(n)$ estimate.

At $n=225$, $\mathcal Z\ne0$ follows from the supplied nonzero primitive moment determinant. Also $\mathcal F\ne0$: if it vanished, (7.6) would make the two complete endpoint centers equal. Their supplied actual reduced denominators differ, so the centers are not equal.

No family-wide nonvanishing or small-support theorem for these new scalars is asserted.

---

# 9. Concrete next lemma and genuinely new bounded arithmetic

## 9.1 The next symbolic lemma

The most focused follow-on target is now:

> **Specialized resultant-coprimality or imbalance lemma.**  
> On infinitely many retained original endpoint indices, control
> 

$$
> \gcd(X_j,\mathcal F)
>
$$


> outside the prime support of $n!D\mathcal Z$, and control the contribution at primes dividing $Z_0$.
>
> A sufficient quantitative form would bound the combined imbalance contributions of $Z_0$ and $\mathcal F$ by $\exp(O(n))$, or prove a sharper direct estimate for the actual $Z_{K^\sharp}$.

This is more specific than asking for an unspecified gcd estimate in the full exponential numerator. It supplies the precise common resultant and the exact exceptional factor.

## 9.2 New post-processing only

No accepted producer, enclosure, dual-content calculation, or auxiliary test should be rerun.

A new bounded calculation can examine the scalars introduced in §§6–8 using the archived $n=225$ producer artifact.

### Inputs

Use the existing:

- $T,\Delta_T$;
- $\alpha_j,\beta_j,N_j^{\exp}$, $j=0,3$;
- primitive triples and $\gamma_j,\mathfrak a_j,\mathfrak b_j$;
- $L,t_0,t_1,r_0,r_1$;
- original $X_j,\mathcal R_j^{(0)},\mathcal R_j^{(1)}$.

No force regeneration is needed. If $\omega_n,\omega_{n+1}$ were not stored separately, obtain $\mathcal P,\mathcal Q$ from the existing endpoint data:


$$
\mathcal P
=
\mathcal Z\,
\frac{N_0^{\exp}\beta_3-N_3^{\exp}\beta_0}
{\alpha_0\beta_3-\beta_0\alpha_3},
$$




$$
\mathcal Q
=
\mathcal Z\,
\frac{\alpha_0N_3^{\exp}-\alpha_3N_0^{\exp}}
{\alpha_0\beta_3-\beta_0\alpha_3}.
$$


These use the archived complete numerators, including the exterior term.

### Expected verifiable output

1. The new determinant residual is exactly zero:
   

$$
2(n+2)(\alpha_0\beta_3-\beta_0\alpha_3)
   -(n+1)\Delta_T\mathcal Z=0.
$$



2. $Z_0,P_0,Q_0,\mathcal B,\mathcal F$ are reported as exact integers.

3. The specialized primitive identities have zero residual:
   

$$
\mathcal B\mathsf E_j
   -\gamma_j(\mathfrak a_jP_0+\mathfrak b_jQ_0)=0.
$$



4. Extended-gcd coefficients give the explicit zero residual in (7.9).

5. Report—not predict favorable values for—
   

$$
|Z_0|_{>226},\qquad |\mathcal F|_{>226},
$$


   and their gcds with the existing $X_j$.

6. Separately report the exact contribution from primes dividing $Z_0$. Do not silently apply (8.1) there.

This is a new bounded investigation of the specialized identity. It is not a repeat of the already accepted dual-content checks. I have not performed it.

---

# 10. Final gcds, actual denominators, and whole errors remain indispensable

The new identities do not change any primitive normalization.

## 10.1 Complete endpoint weights

Retain


$$
\widetilde u_0=hA,\qquad
\widetilde u_3=hB,\qquad
\gcd(A,B)=1.
$$


For reduced $\lambda=a/k$, $k>0$, retain the complete integers


$$
J=B\widetilde v_0-A\widetilde v_3,
\qquad
T=aJ+kA\widetilde v_3,
$$


and all three gcd factors. The actual primitive pair is still


$$
q_\lambda
=
\frac{kh|AB|}{F_{\rm gcd}GH_{\rm gcd}},
\qquad
p_\lambda
=
\operatorname{sgn}(AB)
\frac{T}{F_{\rm gcd}GH_{\rm gcd}}.
$$


The relevant error remains


$$
\boxed{
q_\lambda(e+\pi)-p_\lambda
=
q_\lambda e_3\alpha_{n,2}
(\lambda-\Lambda_{n,2}).
}
$$


The $n=225$ enclosures evaluate this whole quantity and show that the five specified choices are not small.

## 10.2 Ternary determinant route

Retain the complete pair


$$
D_0=\det\Theta,
$$




$$
D_1
=
e_{\rm act}^T\operatorname{adj}(\Theta)e_{\rm act}
-3^{26}d_{\rm act}\det\Theta.
$$


The Cartier and beta-functional reductions do not establish the six-digit inverse certificate or the strict whole-scalar guard.

With the least actual clearer,


$$
g_\ell=\gcd(|A_\ell|,|B_\ell|),
$$


the primitive denominator remains


$$
q=\frac{|B_\ell|}{g_\ell},
$$


and the same-index whole error is


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}
{g_\ell}\det H_{\rm complete}.
}
$$


Every prime remains in $g_\ell$.

## 10.3 The $29$-adic weighted route

Retain


$$
g_B=\gcd(A_B,|H_B|),\qquad
p_n=\frac{H_B}{g_B},\qquad
q_n=\frac{A_B}{g_B}>0.
$$


In particular,


$$
\log q_n
=
\sum_\ell
\max\{v_\ell(A_B)-v_\ell(H_B),0\}\log\ell.
$$


The kernel precision correction does not evaluate this all-prime sum.

The local alignment target is still at


$$
K=v_{29}(\mathcal N)+2,
$$


not at an arbitrarily chosen small precision. Until the norm-relative logarithmic protection inequality is established, both complete logarithmic initial charges remain in the calculation.

The relevant whole form is


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n.
}
$$



---

# 11. Final assessment

The two supplied symbolic advances survive audit at their exact algebraic scopes:

- A1 gives a correct finite-cutoff Cartier reduction of the complete coefficient, not an evaluated corrected section or rank theorem.
- A2 gives a correct finite-boundary atom reduction and reconstructed Gram kernel, not a practical original-index evaluator.

The new results in this report are:

1. An exact beta-functional expression and monomial valuation law for the complete ternary pole functional.
2. A division-safe valuation/unit evaluator for A2’s summand recurrence, eliminating cumulative nonunit precision loss while leaving the original-length summation problem open.
3. The specialized complete moment–force identity
   

$$
\mathcal ZN_j^{\exp}=\alpha_j\mathcal P+\beta_j\mathcal Q.
$$


4. An explicit integer Bézout identity proving
   

$$
\gamma_j\mid\mathcal B,\qquad
   \mathcal C_j^\sharp\mid G_t\mathcal F.
$$


5. The exact large-prime cancellation law
   

$$
v_p(\mathcal C_j^\sharp)
   =\min\{v_p(X_j),v_p(\mathcal F)\}
   \quad
   (p>n+1,\ p\nmid\mathcal B).
$$



The principal new endpoint bottleneck is now sharply identified: **specialized coprimality or imbalance control for the common complete-force resultant $\mathcal F$, with the explicit moment exceptional factor $Z_0$**.

The completed $n=225$ evidence is consistent with favorable content support at that one index, but it also certifies that all five tested primitive whole forms are very large. Neither conclusion extends automatically to the family.

An irrationality proof still requires infinitely many retained original indices with actual primitive integers $p,q$ such that


$$
0<|q(e+\pi)-p|\longrightarrow0.
$$


The present work does not establish that comparison after the final all-prime gcd.



$$
\boxed{\text{The irrationality of }e+\pi\text{ remains unresolved.}}
$$


