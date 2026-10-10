> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A1, turn 2 — Exact strip multiplication and finite HIGH convolution, with a growing-rank obstruction to residue-channel compression

## Executive conclusion

The fixed-window geometry gives a useful new construction, but it does **not** turn a narrow grid strip into a bounded number of scalar residue channels.

The advances in this report are:

1. **The original section cutoff has exactly two possibilities.** On the retained original window,
   

$$
\boxed{
   R'=
   \begin{cases}
   2M-2,&4D\le 3g+5,\\
   2M-3,&4D>3g+5.
   \end{cases}}
$$


   Equality belongs to the first case. No endpoint is rounded away.

2. **Each corrected quotient strip occupies at most two consecutive $g$-blocks.** Those blocks still contain a number of residue positions proportional to $g$. I give exact multiplication rules, including the carries $0,1,2$, for
   

$$
\mathcal C_g\!\left((y-1)^D(\beta+3y)\psi_i\psi_j\right).
$$


   Both corrected factors remain present.

3. **The original finite HIGH inverse admits an explicit section-convolution rule.** Its kernel is reduced modulo $3^{27}$ to
   

$$
\boxed{
   (1-t)^{-A}\equiv
   \frac{(1-t)^D}{(1-t^g)^M}\pmod{3^{27}},
   }
$$


   followed by the exact finite reflection and restrictions on $d,\ldots,m$. The resulting formula specifies every coefficient, residue carry, reflection borrow, and boundary mask. It requires no arbitrary coefficient oracle.

4. **There is a precise obstruction to the proposed support-only compression.** Even inside the initial permitted strip, the single section coefficient at $y^\rho$ induces a bilinear form whose rank grows linearly with $g$. Consequently, no bounded-dimensional **linear quotient of each factor separately**, justified only by this support geometry, can recover all corrected-product sections.

The fourth conclusion does not rule out a quotient for the **actual return-generated columns**, or for their **whole pole functional**. Those objects have additional relations, including cancellations already established by the depth-$26$ theorem. It does rule out obtaining the desired quotient merely by counting the number of $g$-blocks intersecting a strip.

Thus this report supplies constructive section rules and a rigorous obstruction to one proposed compression mechanism. It does not supply an original normalized coefficient, a rank theorem for the actual Schur matrix, or a proof concerning irrationality of $e+\pi$.

---

## 1. Scope and accepted results

Retain exactly


$$
n=4^j+1,\qquad j>0,\qquad81\mid j,
$$


and, on the sufficiently large fixed window,


$$
j\equiv81\pmod{243},\qquad
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15}.
$$


As before,


$$
H=3^{h-1},\quad A=H-D,\quad
m=\frac{H-D+1}{2},\quad
d=\frac{3D}{2}-1,\quad
\nu=\frac D2-1.
$$



The original spaces remain


$$
U_u=(y-1)^u\quad(0\le u<D),\qquad
z_i=(y-1)^Dy^i\quad(0\le i<\nu),
$$




$$
Y_b=y^b\quad(d\le b\le m).
$$



A4turn0 has now accepted, at the stated finite-support and simultaneous-hypothesis scope,


$$
S_c\in3^{26}M_\nu(\mathbb Z_3),
\qquad
S_{\rm act}-S_c\in3^{32}M_\nu(\mathbb Z_3).
$$


I reuse these results without reopening their accepted bounded checks.

I also use A4’s corrected pairing comparison. If the precision-$25$ representatives are written


$$
\Phi=WB+\widehat Z^{\,c}C,
\qquad B\in3^{25}M,\quad C-I\in3^{25}M,
$$


then


$$
G_c(\Phi,\Phi)=B^TE_cB+C^TS_cC,
$$


so


$$
G_c(\Phi,\Phi)-S_c\in3^{50}M.
$$


This is the justification for using both representative columns in the absolute modulus-$3^{27}$ calculation. It is not a coefficientwise precision-$27$ assertion about each representative.

Set


$$
g=3^{h-27},\qquad M=3^{26},\qquad
H=gM,\qquad \rho=\frac{g-1}{2},\qquad \delta=\frac Dg.
$$



All new polynomial identities below are independent of the accepted support theorem. Their application to the chosen representatives uses that theorem at its stated precision.

---

## 2. Exact integer geometry

### 2.1 Window bounds and minimum scale

The fixed window gives


$$
\boxed{
\alpha<\delta<2\alpha,\qquad
\alpha=\frac{177147}{295936}.
}
$$


In particular,


$$
\frac12<\alpha<\frac35,\qquad
2\alpha<\frac65.
$$



On the original window $D\ge486$. Since $D<(6/5)g$,


$$
g>405.
$$


As $g$ is a nonnegative power of $3$, this implies


$$
\boxed{g\ge729.}
$$



This lower bound makes the constant-width corrections below harmless, but they are not discarded.

### 2.2 Exact cutoff after section

The original pole cutoff is


$$
R_{\max}=2H-2D+2.
$$


Therefore


$$
\begin{aligned}
R'
&=\left\lfloor\frac{R_{\max}-\rho}{g}\right\rfloor\\
&=2M-\left\lceil
2\delta+\frac12-\frac{5}{2g}
\right\rceil.
\end{aligned}
\tag{2.1}
$$



The expression inside the ceiling is strictly greater than $1$ and strictly less than $3$. Indeed,


$$
2\delta+\frac12-\frac{5}{2g}
>
2\alpha+\frac12-\frac5{1458}>1,
$$


and


$$
2\delta+\frac12-\frac{5}{2g}
<\frac{12}{5}+\frac12<3.
$$



Thus its ceiling is $2$ or $3$. The transition is exact:


$$
2\delta+\frac12-\frac{5}{2g}\le2
\iff 4D\le3g+5.
$$


Consequently,


$$
\boxed{
R'=
\begin{cases}
2M-2,&4D\le3g+5,\\
2M-3,&4D>3g+5.
\end{cases}}
\tag{2.2}
$$



In particular, replacing $R'$ uniformly by either $2M-2$ or $2M-3$ would change some original endpoints.

### 2.3 Residual and strip widths

The actual residual indices satisfy


$$
0\le i\le\nu-1=\frac D2-2,
$$


hence


$$
\boxed{\frac ig\le\frac{\delta}{2}-\frac2g<\frac{\delta}{2}.}
\tag{2.3}
$$



At precision $25$, the accepted quotient support is contained in


$$
I_{9g}(w),\qquad
w=\nu+25=\frac D2+24.
$$


Using $D<(6/5)g$ and $g\ge729$,


$$
w<\frac35g+24<g.
\tag{2.4}
$$



A strip centered at $9ag$ is therefore contained in the two $g$-blocks


$$
[(9a-1)g,9ag-1],\qquad
[9ag,(9a+1)g-1].
$$


Negative original exponents are, as always, excluded.

**Important distinction:** this is a bound of two on the number of block positions, not a bound of two on the number of residues within those blocks.

---

## 3. Constructive multiplication of the two corrected sections

Work first over any coefficient ring. For a polynomial $P(y)$, define its full residue decomposition


$$
P(y)=\sum_{r=0}^{g-1}y^rP_r(y^g),
\qquad
P_r(z)=\sum_{q\ge0}P[gq+r]z^q.
\tag{3.1}
$$



The distinguished section from turn 1 is $P_\rho$.

### 3.1 Exact binary section multiplication

For polynomials $P,Q$,


$$
\boxed{
(PQ)_r(z)=
\sum_{a=0}^{r}P_a(z)Q_{r-a}(z)
+
z\sum_{a=r+1}^{g-1}P_a(z)Q_{r+g-a}(z).
}
\tag{3.2}
$$



The first sum has residue carry $0$; the second has carry $1$.

This follows directly by grouping the exponent identity


$$
(gp+a)+(gq+b)=g(p+q+\varepsilon)+r,
$$


where $a+b=r+\varepsilon g$.

Formula (3.2) is exact. It illustrates why knowing only $P_\rho$ and $Q_\rho$ cannot determine $(PQ)_\rho$.

### 3.2 Strip representation

For a supported quotient $\psi_i$, write


$$
\psi_i(y)=
\sum_a y^{9ag}P_{i,a}(y),
$$


where $P_{i,a}$ is a Laurent polynomial supported in $[-w,w]$, and only nonnegative total exponents are retained.

Since $w<g$, split it without ambiguity as


$$
P_{i,a}(y)=P^+_{i,a}(y)+y^{-g}P^-_{i,a}(y),
\tag{3.3}
$$


where


$$
P^+_{i,a}(u)=\sum_{t=0}^{w}\psi_i[9ag+t]u^t,
$$




$$
P^-_{i,a}(u)=
\sum_{t=-w}^{-1}\psi_i[9ag+t]u^{g+t}.
$$


Every polynomial in (3.3) has degree below $g$.

Equivalently,


$$
\psi_i(y)=\sum_b y^{gb}B_{i,b}(y),\qquad \deg B_{i,b}<g,
\tag{3.4}
$$


with nonzero block positions restricted to $b=9a$ and $b=9a-1$. If two descriptions contribute to the same block, their coefficients are added; no independent copy of an original coefficient is introduced.

This constructs the block inputs from the actual finite-return coefficients, rather than presuming random access to a product section.

### 3.3 The prefactor and the three possible carries

Put


$$
K(y)=(y-1)^D(\beta+3y).
$$


Its coefficients are explicitly


$$
\boxed{
K[t]=
\beta(-1)^{D-t}\binom Dt
+
3(-1)^{D-t+1}\binom D{t-1},
}
\tag{3.5}
$$


where out-of-range binomial coefficients are zero.

Because $D+1<2g$, write


$$
K(y)=K_0(y)+y^gK_1(y),\qquad \deg K_e<g.
\tag{3.6}
$$



For


$$
F_{ij}=K\psi_i\psi_j,
$$


the desired section is now given constructively by


$$
\boxed{
\mathcal C_gF_{ij}(z)
=
\sum_{e=0}^{1}\sum_{b,c}\sum_{\kappa=0}^{2}
z^{e+b+c+\kappa}
[u^{\rho+\kappa g}]
K_e(u)B_{i,b}(u)B_{j,c}(u).
}
\tag{3.7}
$$



The three possible carries are precisely $\kappa=0,1,2$, because the product of three degree-$<g$ polynomials has degree at most $3g-3$.

Equation (3.7) retains:

- both corrected factors;
- every coefficient of their finite strips;
- the prefactor $(y-1)^D(\beta+3y)$;
- all residue carries;
- the actual finite upper support bounds.

For endpoint-kernel products, replace the two block families respectively by


$$
B_{i,b}+B_{i+1,b},\qquad
B_{j,c}+B_{j+1,c}.
$$


No replacement by $(1+y)y^i$ is made.

### What this construction achieves

There is now an explicit finite convolution algorithm for every required product section. The coefficients are generated by polynomial multiplication and extraction from the return blocks.

What it does **not** achieve is a bound independent of $g$ on the lengths of the polynomials $B_{i,b}$. The next two sections make that distinction precise.

---

## 4. Exact section rule for the finite HIGH inverse

The accepted finite HIGH inverse is


$$
(R_H)_{ab}
=[t^{d+m-a-b}](1-t)^{-A},
\qquad d\le a,b\le m.
\tag{4.1}
$$


Let


$$
N=d+m,
\qquad f(t)=\sum_{b=d}^{m}f_bt^b.
$$


Then its output is exactly


$$
\boxed{
(R_Hf)_a=[t^{N-a}](1-t)^{-A}f(t),
\qquad d\le a\le m.
}
\tag{4.2}
$$



Thus the finite inverse is a convolution, followed by a reflection and the original finite restriction. It is not an unrestricted infinite convolution operator on the output.

### 4.1 Reduction of the kernel exponent

The lifted Frobenius identity from turn 1 gives


$$
(1-t)^H\equiv(1-t^g)^M\pmod{3^{27}}.
$$


Both sides have constant coefficient $1$, so inversion is legitimate in the formal power-series ring. Since $A=H-D$,


$$
\boxed{
(1-t)^{-A}
\equiv
(1-t)^D(1-t^g)^{-M}
\pmod{3^{27}}.
}
\tag{4.3}
$$



Write


$$
(1-t)^D=\sum_{r=0}^{g-1}t^rA_r(t^g).
$$


The coefficients are


$$
\boxed{
A_r(z)=
\sum_{\substack{e\ge0\\ge+r\le D}}
(-1)^{ge+r}\binom D{ge+r}z^e.
}
\tag{4.4}
$$


Because $D<2g$, each $A_r$ has degree at most $1$.

Hence the kernel sections are


$$
\boxed{
\bigl((1-t)^{-A}\bigr)_r(z)
\equiv A_r(z)(1-z)^{-M}\pmod{3^{27}}.
}
\tag{4.5}
$$



The remaining universal kernel has completely specified coefficients


$$
[z^k](1-z)^{-M}=\binom{M+k-1}{k}.
\tag{4.6}
$$



### 4.2 Finite input masks

For every residue $r$, the input section is exactly


$$
f_r(z)=
\sum_{q=\lceil(d-r)/g\rceil}^{\lfloor(m-r)/g\rfloor}
f_{gq+r}z^q,
\tag{4.7}
$$


with an empty interval interpreted as zero.

There is no rounding convention beyond the displayed floor and ceiling. In particular, a coefficient at $b=d$ or $b=m$ is retained.

Define


$$
B_r(z)=
\sum_{a=0}^{r}A_a(z)f_{r-a}(z)
+
z\sum_{a=r+1}^{g-1}A_a(z)f_{r+g-a}(z).
\tag{4.8}
$$


Then, by (3.2),


$$
\boxed{
\bigl((1-t)^{-A}f(t)\bigr)_r(z)
\equiv(1-z)^{-M}B_r(z)\pmod{3^{27}}.
}
\tag{4.9}
$$



Equations (4.4), (4.6), and (4.8) specify all coefficients in this convolution.

### 4.3 Reflection borrow and output masks

Write


$$
N=gQ+s,\qquad0\le s<g.
$$


For an output index $a=gq+r$, define


$$
\epsilon_r=
\begin{cases}
0,&r\le s,\\
1,&r>s,
\end{cases}
\qquad
r^\star=s-r+\epsilon_rg.
$$


Then


$$
N-a=g(Q-q-\epsilon_r)+r^\star.
$$


Therefore


$$
\boxed{
(R_Hf)_{gq+r}
\equiv
[z^{Q-q-\epsilon_r}]
(1-z)^{-M}B_{r^\star}(z)
\pmod{3^{27}},
}
\tag{4.10}
$$


for exactly


$$
\boxed{
\left\lceil\frac{d-r}{g}\right\rceil
\le q\le
\left\lfloor\frac{m-r}{g}\right\rfloor.
}
\tag{4.11}
$$



The equality case $r=s$ has borrow $0$, not $1$.

This proves the requested finite HIGH-convolution rule. It also identifies the obstruction to commuting a single Cartier section through the finite inverse: both the residue convolution (4.8) and the residue-dependent reflection borrow (4.10) must be accounted for.

The same construction works at a lower modulus by reduction. No nonunit modular division is needed.

---

## 5. Complete forcing and precision

The preceding rule acts on the **complete** finite HIGH force. In the notation of the accepted return formula, that force is


$$
\begin{aligned}
f_b={}&
c_0[y^{r_*}]x^Hq\,y^b
+[y^{r_*}]x^Hyq\,y^b\\
&+
\sum_{\substack{0\le a\le h-1\\c\ {\rm odd},\ 3\nmid c\\
c3^a\le4n-3}}
3^{h-1-a}c^{-1}
[y^{(c3^a-1)/2}]x^H(\beta+3y)q\,y^b\\
&-\frac{3^{h-1}}4
\mathfrak f((y+1)x^H(\beta+3y)q\,y^b)
-(X^T\varepsilon)_b .
\end{aligned}
\tag{5.1}
$$


Here $q$ is the polynomial appearing in that return formula, not the final primitive denominator.

The section construction applies to the sum (5.1). It does not replace that sum by its leading extraction term.

At the accepted representative precision $25$:

- the factorial part vanishes by its stated valuation;
- the complete LOW error vanishes by the accepted support separation;
- the finite-return expansion may be stopped at the accepted precision length.

These are precision-$25$ facts. They do not license declaring the separate LOW or factorial terms zero at every higher precision.

The chosen precision-$25$ representatives may be lifted as actual supported polynomials and then used in (3.7). Their whole-pairing accuracy is supplied by the $3^{50}$ comparison in §1.

For the final absolute modulus-$3^{27}$ pairing, the factorial contribution


$$
-\frac{3^h}{4}\mathfrak f((y+1)x^HF_{ij})
$$


vanishes because $h\ge27$ and its argument is integral. This is a different valuation statement from the normalized-return factorial omission.

The terminal equations remain unchanged:


$$
\lambda_{i+\nu}+
\sum_{k=0}^{\nu-1}\bar f_k\lambda_{i+k}
=\bar b_i^{\langle26\rangle},
\qquad0\le i\le\nu-2,
\tag{5.2}
$$




$$
\boxed{
J^T\varepsilon+\omega
=-\varepsilon-s\bigl(\theta e_{\nu-1}
+3^{26}b^{\langle26\rangle}\bigr).
}
\tag{5.3}
$$


No moment beyond $D-4$ is introduced, and $\omega_{\nu-1}$ is not suppressed.

---

## 6. A growing-rank obstruction inside one permitted strip

The exact rules above do not collapse to a bounded number of scalar residue channels merely because each strip occupies two blocks. The following proposition quantifies that failure.

### Proposition — No bounded separate linear quotient for all supported product sections

Let


$$
w_0=\min\left(\frac D2-2,\rho\right),
\qquad
L=\rho-w_0,
\qquad
N_0=2w_0-\rho+1.
$$


Over $\mathbb F_3$, consider the space


$$
\mathcal U=\operatorname{span}\{y^L,y^{L+1},\ldots,y^{w_0}\}.
$$


For all sufficiently large original inputs on the retained window, $N_0>0$, and the bilinear form


$$
\mathcal B(P,Q)
=[y^\rho](y-1)^D(\beta+3y)P(y)Q(y)
\pmod3
\tag{6.1}
$$


has rank exactly $N_0$ on $\mathcal U$.

Moreover $N_0$ grows at least linearly in $g$.

#### Proof

The monomials in $\mathcal U$ have degrees between $0$ and $\nu-1$, so they lie inside the initial permitted strip.

Index the basis by $y^{L+a}$, $0\le a<N_0$. The matrix entries of (6.1) are


$$
K[\rho-2L-a-b]\pmod3,
\qquad K=(y-1)^D(\beta+3y).
$$


Since


$$
\rho-2L=2w_0-\rho=N_0-1,
$$


the entries are


$$
K[N_0-1-a-b]\pmod3.
$$


They vanish whenever $a+b>N_0-1$. On the anti-diagonal $a+b=N_0-1$, they equal


$$
K[0]=(-1)^D\beta\equiv1\pmod3,
$$


because $D$ is even and $\beta\equiv1\pmod3$.

The matrix is therefore anti-triangular with unit anti-diagonal. Its determinant is a unit, proving rank $N_0$.

If $D/2-2\le\rho$, then


$$
N_0=D-\frac g2-\frac52
>
\left(\alpha-\frac12\right)g-\frac52.
$$


If $D/2-2>\rho$, then


$$
N_0=\rho+1=\frac{g+1}{2}.
$$


Since $\alpha>1/2$, both alternatives give a positive linear lower bound for sufficiently large $g$. ∎

### Consequence for observable quotients

Suppose linear maps


$$
\pi_1:\mathcal U\to V_1,\qquad
\pi_2:\mathcal U\to V_2
$$


and a bilinear pairing on $V_1\times V_2$ recover (6.1) for every $P,Q\in\mathcal U$. Then


$$
\dim V_1\ge N_0,\qquad \dim V_2\ge N_0.
\tag{6.2}
$$


Indeed, the rank of a bilinear form factoring through those maps cannot exceed either quotient dimension.

Since the constant coefficient of $\mathcal C_g(KPQ)$ is precisely (6.1), the same lower bound applies to a separate linear quotient intended to recover **all** such product sections.

### Exact scope of the obstruction

This proves an obstruction to:

> a bounded-dimensional separate linear compression derived only from the permitted strip support, valid for arbitrary coefficients in those strips.

It does **not** prove an obstruction to:

- compression restricted to the actual finite-return-generated family;
- a coupled observable that does not first compress the two factors separately;
- a quotient for the whole pole functional rather than all section coefficients;
- a fast structured convolution using the full residue polynomials;
- a special endpoint-kernel identity using the complete return equations.

In particular, this proposition is not a lower bound for the rank of $B_c\bmod3$. The whole pole functional has cancellations absent from (6.1). The already accepted common depth is itself evidence that such cancellations matter.

No automaticity-to-Hankel-rank inference is used.

---

## 7. Recombination with the complete pole observable

With


$$
V_{ij}(z)=\mathcal C_gF_{ij}(z),
$$


constructed by (3.7), turn 1’s universal identity gives


$$
\boxed{
\mathcal E_{27}(F_{ij})
\equiv
\sum_{\ell=0}^{26}3^\ell
\sum_{\substack{c\ge1\ {\rm odd},\,3\nmid c\\
s_{\ell,c}\le R'}}
c^{-1}[z^{s_{\ell,c}}](z-1)^MV_{ij}(z)
\pmod{3^{27}},
}
\tag{7.1}
$$


where


$$
s_{\ell,c}=\frac{c3^{27-\ell}-1}{2},
$$


and $R'$ is exactly (2.2).

The final digit is


$$
(B_c)_{ij}\equiv
-\frac{\mathcal E_{27}(F_{ij})}{3^{26}}\pmod3,
\tag{7.2}
$$


only after the whole residue has been accumulated and its lower $26$ digits verified zero.

Equations (3.7), (4.10), and (7.1) now form an explicit finite construction:



$$
\text{complete finite forces}
\longrightarrow
\text{finite HIGH section convolutions}
\longrightarrow
\text{two corrected block families}
\longrightarrow
\text{product section}
\longrightarrow
\text{whole pole residue}.
$$



The arbitrary coefficient oracle is replaced by specified finite convolutions. The unresolved issue is their **compression or efficient structured evaluation** on the actual return-generated inputs. A dense implementation still has residue-polynomial lengths proportional to $g$.

That remaining complexity is substantive, not hidden by the fixed value of $M$.

---

## 8. The narrower follow-on target

The rank obstruction determines what a useful next lemma must exploit.

It cannot merely assert that strips intersect a bounded number of $g$-blocks. That is proved already and is insufficient.

A concrete next target is instead:

> **Return-relation annihilator lemma.** Form the actual finite-return block polynomials $B_{i,b}(u)$, using (4.8)–(4.11) and the complete force (5.1). Prove explicit linear identities among their residue coefficients that are preserved by the finite input masks, the reflection borrow, and the terminal return. Show that, after contraction with the complete weights in (7.1), these identities annihilate all but a bounded collection of residue-polynomial observables.

The distinction from the earlier missing lemma is operational:

- the multiplication map is now (3.7);
- the HIGH transition is now (4.10);
- its coefficients are (4.4) and (4.6);
- its masks are (4.7) and (4.11);
- the obstruction to support-only closure is the invertible matrix in §6.

Thus a candidate annihilator can be checked directly against explicit transition maps. It must use actual return relations or whole-functional cancellation, not just support.

No such annihilator is proved here.

---

## 9. Actual pair, inverse guard, and global normalization

Nothing above changes the complete pair


$$
D_0=\det\Theta,\qquad
D_1=e_{\rm act}^T\operatorname{adj}(\Theta)e_{\rm act}
-3^{26}d_{\rm act}\det\Theta,
\qquad
\Theta=-S_{\rm act}/3^{26}.
$$



A4’s direct six-digit transfer remains available:


$$
D_{0,\rm act}\equiv D_{0,c}\pmod{3^6},
\qquad
D_{1,\rm act}\equiv D_{1,c}\pmod{3^6}.
$$


It gives actual valuations when the corresponding core residues are nonzero before depth $6$; it does not predict that event.

For the inverse-based alternative, retain both conditions:

- the largest core Smith exponent satisfies $a<6$;
- with
  

$$
u=\max\left(0,-\min_i v_3((B_c^{-1}e_c)_i)\right),
$$


  and
  

$$
\sigma_c=e_c^TB_c^{-1}e_c-3^{26}d_c,
$$


  the strict guard is
  

$$
\boxed{v_3(\sigma_c)<6-2u.}
$$



The full cofactor subtraction is retained throughout.

When the required members are nonzero, the primitive denominator law remains


$$
v_3(q)=
\max\left\{
0,\,
h-26+2v_3((n-1)!)
+v_3(D_1)-v_3(D_0)
\right\}.
$$



All original row contents and the least actual clearing integer remain unchanged:


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$




$$
g_\ell=\gcd(|A_\ell|,|B_\ell|),
\qquad
q=\frac{|B_\ell|}{g_\ell},
\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell}.
$$


The gcd includes every prime.

The same-index whole error is still


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}{g_\ell}
\det H_{\rm complete}.
}
\tag{9.1}
$$


This report establishes no new bound for its nonvanishing or decay.

---

## 10. New bounded arithmetic, if a finite implementation check is desired

No computation is needed to prove the identities or the obstruction above. No accepted computation should be rerun.

A genuinely new auxiliary check would test the **finite HIGH reflection and residue carries**, not the previously checked universal pole identity.

### Inputs

Use


$$
g=9,\quad M=27,\quad H=243,\quad D=10,\quad A=233,
$$


so


$$
d=14,\qquad m=117,\qquad N=131,
$$


at modulus $3^4=81$.

These are auxiliary polynomial parameters, not an original-family tuple.

Use the two explicit finite input vectors


$$
f^{(1)}_b=\mathbf1_{b=14}+\mathbf1_{b=117},
$$




$$
f^{(2)}_b=(-1)^b(b+1),\qquad14\le b\le117.
$$



### Calculation

Compare, for every original HIGH output $14\le a\le117$,

1. the direct finite sum
   

$$
\sum_{b=14}^{117}
   f_b\binom{A+N-a-b-1}{N-a-b},
$$


   with terms of negative lower index interpreted as zero;

2. the section convolution and reflection formula (4.10), using
   

$$
(1-t)^{-233}\equiv
   (1-t)^{10}(1-t^9)^{-27}\pmod{81}.
$$



### Expected verifiable output

- zero discrepancy for all $208$ output comparisons;
- the explicit input and output section intervals;
- correct handling of the borrow transition at $r=s$;
- retention of both endpoint inputs $b=14,117$;
- no output outside $14,\ldots,117$.

This would corroborate only that finite auxiliary implementation. It would not evaluate an original corrected column or establish a family complexity bound.

No such calculation has been executed here.

---

## 11. Proof-status ledger and conclusion

| Statement | Status |
|---|---|
| Accepted finite support and weighted actual/core transfer | Reused at A4’s exact dependency scope |
| Corrected whole-pairing accuracy | Reused with A4’s basis-decomposition proof |
| Exact two-case section cutoff | Proved |
| Two $g$-blocks per corrected quotient strip | Proved |
| Explicit two-factor product-section construction | Proved, with all three carries |
| Finite HIGH kernel reduction | Proved modulo $3^{27}$ |
| Finite HIGH section convolution, reflection borrow, and masks | Proved |
| LOW and factorial omissions at representative precision | Used only at their accepted precision scope |
| Complete forcing and terminal return | Retained |
| Bounded-dimensional support-only separate quotient | Excluded by the growing-rank proposition |
| Small quotient on actual return-generated columns | Unresolved |
| Original normalized coefficient or Schur rank | Not evaluated |
| Actual inverse/scalar guard | Not established |
| All-prime primitive normalization and whole-error decay | Unresolved |

### New result

The new constructive result is the exact composition of:



$$
\boxed{\text{strip product rule (3.7)}}
\qquad\text{and}\qquad
\boxed{\text{finite HIGH section rule (4.10)}},
$$


with the exact cutoff transition (2.2).

The new obstruction is equally specific:



$$
\boxed{
\text{Two block positions per strip do not imply a bounded scalar
observable quotient for products.}
}
$$



A single coefficient of the product section already has rank proportional to $g$ on an allowed initial-strip subspace. Therefore any successful small observable for the original mechanism must exploit the **actual finite-return relations or cancellation in the whole pole functional**.

### Remaining bottleneck

The immediate local bottleneck is now to find and prove such return-specific annihilators for the explicit finite transition maps, while preserving their masks, carries, complete force, and terminal equation.

Beyond that remain the actual determinant/cofactor nonvanishing and relative valuation, the final all-prime gcd and primitive denominator, and the same-index estimate


$$
0<|q(e+\pi)-p|\longrightarrow0
$$


on infinitely many original indices.



$$
\boxed{\text{No unconditional proof or disproof of irrationality of }e+\pi
\text{ has been obtained.}}
$$


