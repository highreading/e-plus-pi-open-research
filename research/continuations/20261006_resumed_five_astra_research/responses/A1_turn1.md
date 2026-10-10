> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A1, turn 1 — Finite-cutoff verification and a uniform Cartier reduction of the complete coefficient

## Executive conclusion

The coordinator’s pole-pair reduction is correct under its stated degree and cutoff hypotheses. The proposed additional low-layer identity is also correct on the original window:


$$
\boxed{
P_0((y^H-1)F)+P_1((y^H-1)F)
=-2[y^{(H-1)/2}]F.
}
$$


The contribution at $c=3$, excluded from $P_1$, is indeed recovered at $c=1$ in $P_0$. Both copies lie within the original cutoff for precisely the inequalities checked below.

I do **not** obtain a numerical original residual coefficient or a rank theorem. I obtain instead a new, division-safe coefficient identity:

> At modulus $3^{27}$, the complete pole functional applied to $(y-1)^HF$ factors through a single Cartier section of $F$, with a universal exponent $3^{26}$, independent of the enormous original $H$.

This is stronger than a generic Hankel or Smith specification. It removes the need to compute binomial coefficients with upper index $H$, incorporates **all** $\Delta_H$ layers and their carries, and applies directly to products of the two corrected representatives. It also supplies an exact endpoint-kernel observable.

The limitation is important: the universal arithmetic still has a very large worst-case bound, and the required Cartier coefficients of the **corrected-column products** have not been evaluated. Neither an input-linear original matrix construction nor the universal bound below is presented as a feasible original computation.

All applications to the depth-$26$ Schur coefficient remain conditional on the earlier support and transfer dependencies pending A4’s audit. The elementary identities proved here do not depend on that audit.

---

## 1. Original domain and finite boundaries

Keep


$$
n=4^j+1,\qquad j>0,\qquad81\mid j,
$$




$$
H=3^{h-1},\qquad A=H-D=n-2,\qquad 0<D<H/972,
$$


and


$$
m=\frac{H-D+1}{2},\qquad d=\frac{3D}{2}-1,\qquad
\nu=\frac D2-1.
$$



The finite columns remain


$$
U_u=(y-1)^u\quad(0\le u<D),\qquad
z_i=(y-1)^Dy^i\quad(0\le i<\nu),
$$




$$
Y_b=y^b\quad(d\le b\le m).
$$


No additional residual coordinate, HIGH column, or moment beyond index $D-4$ is introduced.

The pole cutoff in the sources is exactly


$$
2v+1\le4n-3.
$$


Since $2v+1$ is odd, this is equivalent to


$$
v\le R_{\max}=2n-2=2H-2D+2.
$$



For the elementary low-layer calculation assume $D\ge486$. For the modulus-$3^{27}$ reduction below assume $h\ge27$. The retained sufficiently large depth-$26$ window satisfies this latter condition; it must not be inferred from $D/H<1/972$ alone.

Write


$$
\delta_\ell=3^{h-\ell},\qquad
r_c=\frac{c\delta_\ell-1}{2},
$$


and retain


$$
P_\ell(T)=3^\ell
\sum_{\substack{c\ge1\ {\rm odd},\ 3\nmid c\\r_c\le R_{\max}}}
\frac{T[r_c]}c .
$$



---

## 2. Independent verification of the finite pairing

Let $\deg F=B$ and suppose


$$
H+B\le R_{\max}.
$$


For $2\le\ell\le h$, put


$$
a_\ell=2\cdot3^{\ell-1}.
$$


Then


$$
r_{c+a_\ell}=r_c+H.
$$


The translation preserves oddness and being a $3$-adic unit.

Every nonzero low coefficient $F[r_c]$ has $0\le r_c\le B$, so its high copy is within the **original** cutoff. Conversely, every nonzero high-copy coefficient at $r_c$ arises from a nonnegative index $r_c-H$; its translated index $c-a_\ell$ is positive and remains an odd unit. Thus there are no omitted negative-index or upper-boundary terms.

Consequently,


$$
\begin{aligned}
P_\ell((y^H-1)F)
&=3^\ell
\sum_{\substack{c\ge1\ {\rm odd},\ 3\nmid c\\0\le r_c\le B}}
\left(\frac1{c+a_\ell}-\frac1c\right)F[r_c]\\
&=-2\,3^{2\ell-1}
\sum_{\substack{c\ge1\ {\rm odd},\ 3\nmid c\\0\le r_c\le B}}
\frac{F[r_c]}{c(c+a_\ell)}.
\end{aligned}
\tag{2.1}
$$


All denominators in the last expression are units.

This proves the coordinator identity, including its finite-boundary requirement. At modulus $3^{27}$, its paired part vanishes for $\ell\ge14$.

### Both corrected columns

For


$$
\phi_i=x^D\psi_i,\qquad x=y-1,
$$


define


$$
F_{ij}=x^D(\beta+3y)\psi_i\psi_j.
$$


If both representatives satisfy $\deg\phi_i,\deg\phi_j\le m-1$, then


$$
\deg F_{ij}
\le D+1+2(m-1-D)=H-2D.
\tag{2.2}
$$


Therefore


$$
H+\deg F_{ij}\le2H-2D<R_{\max}.
$$


The pairing applies to the product of **both corrected representatives**, not just to $x^Dy^{i+j}$.

### Scope of the receipt

The supplied receipt records 90 exact layer checks, 1076 binomial-valuation checks, 7052 sparse-precision checks, and four deliberately truncated boundary checks. Its stated auxiliary scope is appropriate. It supplies no original Schur coefficient. There is no reason to rerun it for the present argument.

---

## 3. Verification of the two low layers

Set


$$
r_1=\frac{H-1}{2},\qquad r_*=\frac{3H-1}{2}.
$$



### 3.1 Layer $P_0$

Here $\delta_0=3H$. Its $c=1$ pole is within the cutoff because


$$
r_*\le R_{\max}
\iff H-4D+5\ge0,
$$


which follows from $H>972D$.

The next allowable odd unit is $c=5$, and


$$
\frac{15H-1}{2}>R_{\max}.
$$


Thus $P_0$ contains only $c=1$.

Since $\deg F\le H-2D<r_*$,


$$
F[r_*]=0,
\qquad
[(y^H-1)F][r_*]=F[r_1].
$$


Hence


$$
P_0((y^H-1)F)=F[r_1].
\tag{3.1}
$$



### 3.2 Layer $P_1$

Here $\delta_1=H$. Again $c=1$ is inside the cutoff. The candidate $c=3$ is excluded because it is not a unit.

The next allowable value, $c=5$, is outside:


$$
\frac{5H-1}{2}>2H-2D+2
\iff H+4D>5.
$$


This holds under $D\ge486$.

At $c=1$, the high copy is impossible because $r_1-H<0$. Thus


$$
P_1((y^H-1)F)=-3F[r_1].
\tag{3.2}
$$



Combining (3.1)–(3.2),


$$
\boxed{
P_0((y^H-1)F)+P_1((y^H-1)F)=-2F[r_1].
}
\tag{3.3}
$$



The proposal needs no repair. The coefficient $F[r_1]$ can itself be zero if it lies beyond the actual degree; the identity includes that case.

---

## 4. The complete surviving combination

For $h\ge27$, the factorial contribution to


$$
G_c(\phi_i,\phi_j)
=
-\frac{3^h}{4}\mathfrak f((y+1)x^HF_{ij})
+\sum_{\ell=0}^hP_\ell(x^HF_{ij})
$$


is zero modulo $3^{27}$, because its argument has integral coefficients. This is only a modulus-specific omission.

Put


$$
\Delta_H=x^H-(y^H-1).
$$


Then for every $F$ satisfying the degree hypothesis,


$$
\boxed{
\begin{aligned}
\mathcal E_{27}(F):={}&
-2F[(H-1)/2]\\
&-2\sum_{\ell=2}^{13}3^{2\ell-1}
\sum_{\substack{c\ge1\ {\rm odd},\ 3\nmid c\\0\le r_c\le\deg F}}
\frac{F[r_c]}{c(c+a_\ell)}\\
&+\sum_{\ell=0}^{26}P_\ell(\Delta_HF)
\pmod{3^{27}}.
\end{aligned}}
\tag{4.1}
$$


This is the entire surviving pole combination. In particular, no $\Delta_H$ layer has been removed merely because the corresponding paired layer vanished.

The unresolved issue is evaluation of (4.1), including its carries. The next theorem makes the correction part independent of the large binomial upper index $H$.

---

## 5. New theorem: a universal Cartier-section identity

Set


$$
g=3^{h-27},\qquad M=3^{26},\qquad H=gM,\qquad
\rho=\frac{g-1}{2}.
$$


Define the Cartier section


$$
\mathcal C_gF(z)=
\sum_{k\ge0}F[gk+\rho]z^k.
\tag{5.1}
$$


Only nonnegative original coefficient indices occur.

### Lemma 5.1 — Lifted Frobenius with an explicit precision

For every $0\le\ell\le26$,


$$
x^H
\equiv
\bigl(y^{g3^\ell}-1\bigr)^{3^{26-\ell}}
\pmod{3^{27-\ell}}.
\tag{5.2}
$$



#### Proof

For every power $u$ of $3$,


$$
(y-1)^u\equiv y^u-1\pmod3.
$$


If $A\equiv B\pmod{3^s}$, $s\ge1$, then


$$
A^3-B^3=(A-B)(A^2+AB+B^2)\in3^{s+1}\mathbb Z_3[y].
$$


Iterating $26-\ell$ times, starting with $u=g3^\ell$, proves (5.2). ∎

This proof requires no division and no binomial computation with upper index $H$.

### Theorem 5.2 — Complete coefficient compression

Let


$$
V(z)=\mathcal C_gF(z),
\qquad
R'=\left\lfloor\frac{R_{\max}-\rho}{g}\right\rfloor,
\qquad
s_{\ell,c}=\frac{c3^{27-\ell}-1}{2}.
$$


Then


$$
\boxed{
\mathcal E_{27}(F)
\equiv
\sum_{\ell=0}^{26}3^\ell
\sum_{\substack{c\ge1\ {\rm odd},\ 3\nmid c\\
g\,c3^{27-\ell}\le 2R_{\max}+1}}
\frac{[z^{s_{\ell,c}}](z-1)^MV(z)}c
\pmod{3^{27}}.
}
\tag{5.3}
$$


Equivalently, the cutoff in the inner sum is $s_{\ell,c}\le R'$.

#### Proof

Lemma 5.1 at $\ell=0$ gives


$$
x^HF\equiv(y^g-1)^MF\pmod{3^{27}}.
$$


For any polynomial $A$,


$$
\mathcal C_g\bigl(A(y^g)F(y)\bigr)
=A(z)\mathcal C_gF(z).
\tag{5.4}
$$


Moreover,


$$
r_c
=\frac{gc3^{27-\ell}-1}{2}
=g\,s_{\ell,c}+\rho.
$$


Thus each original pole coefficient equals the corresponding coefficient in (5.3), at the required precision. Its original cutoff is exactly the displayed inequality. Summing proves the result. ∎

### What this changes

The complete coefficient depends on $F$ only through one section:


$$
F\longmapsto\mathcal C_gF.
$$


Since $\deg F\le H-2D<H$,


$$
\deg V\le M-1.
\tag{5.5}
$$


Thus the functional has an $H$-independent coefficient input bound.

This is not a claim of practical smallness:


$$
M=3^{26}=2\,541\,865\,828\,329.
$$


It is nevertheless a structural elimination of the moving exponent $H$, not an input-linear request for an original matrix.

---

## 6. A multiresolution formula retaining every correction layer

For computation, (5.3) need not expand $(z-1)^M$ separately at every pole.

Set


$$
N_\ell=3^{26-\ell},\qquad
d_{\ell,k}=(-1)^{N_\ell-k}\binom{N_\ell}{k}
\quad(1\le k<N_\ell).
$$


Lemma 5.1 gives


$$
\Delta_H
\equiv
\sum_{k=1}^{N_\ell-1}d_{\ell,k}y^{g3^\ell k}
\pmod{3^{27-\ell}}.
$$


Therefore


$$
\boxed{
P_\ell(\Delta_HF)
\equiv
3^\ell
\sum_{\substack{c\ge1\ {\rm odd},\ 3\nmid c\\
gc3^{27-\ell}\le2R_{\max}+1}}
\frac1c
\sum_{k=1}^{N_\ell-1}
d_{\ell,k}\,
V[s_{\ell,c}-3^\ell k]
\pmod{3^{27}}.
}
\tag{6.1}
$$


Out-of-range coefficients of $V$ are zero.

This formula includes every correction layer. At $\ell=26$, $N_\ell=1$, so the inner sum is empty: the correction vanishes modulo the one digit required at that layer. That is a proved precision omission, not a dropped carry.

The low paired coefficient becomes


$$
F[(H-1)/2]=V[(M-1)/2],
\tag{6.2}
$$


and the paired terms in (4.1) use


$$
F[r_c]=V[s_{\ell,c}].
\tag{6.3}
$$


Equations (4.1), (6.1)–(6.3) are consequently an explicit evaluation identity entirely in the section $V$.

### Division and resource budgets

1. **Coefficient precision.**  
   Correction layer $\ell$ needs $V$ and $d_{\ell,k}$ modulo $3^{27-\ell}$. The paired layer $\ell\ge2$ needs its coefficient and unit weight modulo $3^{28-2\ell}$.

2. **No nonunit denominator is introduced.**  
   Pole denominators and paired denominators are units. Binomial coefficients can be generated by tracking their $3$-adic valuation and their unit part in
   

$$
\binom Nk=\binom N{k-1}\frac{N-k+1}{k}.
$$


   Strip powers of $3$ from numerator and denominator before unit inversion. There is no division of a residue by a nonunit.

3. **Correction coefficient valuation.**
   

$$
v_3(d_{\ell,k})=26-\ell-v_3(k).
   \tag{6.4}
$$


   This is the coordinator’s valuation formula, now with upper index at most $3^{26}$.

4. **Explicit worst-case query bound.**  
   Since
   

$$
2R_{\max}+1=4H-4D+5<4H,
$$


   the number of candidate odd $c$’s is at most $2\cdot3^{\ell-1}$ for $\ell\ge1$, and is one for $\ell=0$. Ignoring the unit exclusion only enlarges the bound. Thus the double sums in (6.1), over $\ell=0,\ldots,25$, use fewer than
   

$$
M+25\cdot\frac{2M}{3}<18M
$$


   coefficient queries. Including binomial generation and paired terms, $60M$ is a conservative arithmetic-operation budget, **assuming random access to the required section coefficients**.

5. **Normalization.**  
   All terms are accumulated modulo $3^{27}$. Only after the whole result is verified divisible by $3^{26}$ may one divide once and reduce modulo $3$.

The random-access assumption is the outstanding target-specific issue. This bound does not establish that the corrected section can be produced at acceptable cost.

---

## 7. Application to corrected columns and the endpoint observable

For integral residual vectors $a,b$, write


$$
\psi_a=\sum_{i=0}^{\nu-1}a_i\psi_i,\qquad
\psi_b=\sum_{i=0}^{\nu-1}b_i\psi_i,
$$


and define


$$
V_{a,b}
=
\mathcal C_g\!\left(x^D(\beta+3y)\psi_a\psi_b\right).
\tag{7.1}
$$



Under the earlier corrected-representative and depth hypotheses,


$$
\boxed{
a^T(B_c\bmod3)b
=
-\frac{\mathcal E_{27}\!\left(x^D(\beta+3y)\psi_a\psi_b\right)}
{3^{26}}\pmod3.
}
\tag{7.2}
$$


The right side is now evaluated by the universal formulas above.

No substitution $\psi_i=y^i$ has occurred. The precision-$25$ representative accuracy is used only through the source’s whole-pairing comparison with the exact Schur entry; it is not used to declare a precision-$27$ coefficientwise approximation.

### Endpoint-kernel restriction

The accepted endpoint residue is


$$
\bar e=(1,-1,\ldots,(-1)^{\nu-1})^T.
$$


A basis of its kernel over $\mathbb F_3$ is


$$
u_i=e_i+e_{i+1},\qquad0\le i\le\nu-2.
$$


Hence the first-layer endpoint-kernel Gram entries are given directly by (7.2), with


$$
\boxed{
V^\partial_{ij}
=
\mathcal C_g\!\left[
x^D(\beta+3y)
(\psi_i+\psi_{i+1})(\psi_j+\psi_{j+1})
\right].
}
\tag{7.3}
$$


This is an actual complete-coefficient observable, not an endpoint replacement by a terminal channel.

It does **not** justify replacing the parenthesized factors by
$(1+y)y^i$ at precision $3^{27}$. Nor does this residue-level kernel basis replace the exact transported endpoint at higher precision.

---

## 8. Where the finite return data enter—and what is not yet proved

The supplied finite return formula contains:

- both leading extraction terms;
- every original lower pole;
- the factorial force;
- the LOW subtraction $-(X^T\varepsilon)_b$;
- the finite HIGH inverse on $d,\ldots,m$.

These data determine the corrected $\psi_i$, conditionally on the earlier construction and audit. The new identity identifies exactly which output of that construction is needed: the sections (7.1), or the endpoint sections (7.3).

What is still missing is a proved closure rule for those **products of corrected outputs** under the finite return operations. The support statement alone does not give their coefficient values. Moreover, the finite HIGH inverse is a convolution followed by boundary restrictions; one cannot commute it through $\mathcal C_g$ without accounting for those restrictions.

This is the named obstruction now isolated:



$$
\boxed{
\text{Evaluate the Cartier sections of the complete corrected-column products,
with the finite return boundaries retained.}
}
$$



A concrete follow-on lemma is:

> **Finite-return Cartier-observable lemma.**  
> At precision $3^{27}$, construct a division-safe recurrence for (7.1), or directly for (7.3), from the complete finite core return data. The recurrence must preserve LOW indices $0,\ldots,D-1$, HIGH indices $d,\ldots,m$, both corrected factors, all forcing, and the terminal return. Its cost must be proved sublinear in the enormous original $H$, with a substantially smaller reachable-observable bound than the universal worst-case budget above.

This is a narrower problem than reconstructing the original Schur matrix. It has not been solved here.

The complete moment forcing and terminal equation remain


$$
\lambda_{i+\nu}+\sum_{k=0}^{\nu-1}\bar f_k\lambda_{i+k}
=\bar b_i^{\langle26\rangle},
\qquad0\le i\le\nu-2,
$$




$$
J^T\varepsilon+\omega
=-\varepsilon-s\bigl(\theta e_{\nu-1}
+3^{26}b^{\langle26\rangle}\bigr).
$$


In particular, neither the terminal forcing nor $\omega_{\nu-1}$ has been set to zero.

---

## 9. Actual scalar guard and global normalization remain unchanged

Retain


$$
\Theta=-S_{\rm act}/3^{26},\qquad
D_0=\det\Theta,
$$




$$
D_1=e_{\rm act}^T\operatorname{adj}(\Theta)e_{\rm act}
-3^{26}d_{\rm act}\det\Theta.
$$



If the conditional six-digit inverse certificate succeeds, with largest core Smith exponent $a<6$, put


$$
u=\max\left(0,-\min_i v_3((B_c^{-1}e_c)_i)\right),
$$




$$
\sigma_c=e_c^TB_c^{-1}e_c-3^{26}d_c.
$$


The actual scalar guard remains


$$
\boxed{v_3(\sigma_c)<6-2u.}
$$


Only under that strict inequality does the transfer identify the nonzero actual scalar valuation


$$
v_3(D_1)-v_3(D_0)=v_3(\sigma_c).
$$


Nothing in the Cartier reduction proves this inequality or $a<6$.

With $F_{\rm fact}=(n-1)!$, the primitive denominator law, when the required pair is nonzero, remains


$$
v_3(q)=
\max\left\{
0,\,
h-26+2v_3(F_{\rm fact})
+v_3(D_1)-v_3(D_0)
\right\}.
$$



All original row contents and the least actual clearing integer remain unchanged. Explicitly,


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


Every prime remains in $g_\ell$. The same-index whole error is still


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}{g_\ell}
\det H_{\rm complete}.
}
$$


No row-content, all-prime gcd, denominator-growth, or whole-error claim is established by the new local identity.

---

## 10. Bounded arithmetic needed and proof status

No computation is needed for the proofs in §§2–6, and no accepted bounded computation should be regenerated.

A new, limited check of the Cartier identity—not an original Schur computation—could use:

- $K=4$, $h=6$, hence $H=243$, $g=9$, $M=27$;
- cutoff $R=2H-2D+2$, with an explicitly chosen auxiliary $D$;
- several explicitly listed integral $F$ with $\deg F\le H-2D$;
- direct finite pole summation modulo $3^4$;
- the section $\mathcal C_9F$, and the $K=4$ versions of (5.3) and (6.1).

The expected verifiable output is equality of the **whole** residues, including the original cutoff and every correction layer. Such a check would corroborate only this new auxiliary identity. It would not supply an original corrected section or normalized residual coefficient. I have not executed it.

For an original coefficient, the indispensable inputs are instead:

1. a certified original tuple satisfying all depth-$26$ hypotheses;
2. the audited complete finite return data;
3. one explicitly evaluated section $V_{a,b}$ or $V^\partial_{ij}$, with its coefficient precision certificate.

The verifiable output would be the complete residue modulo $3^{27}$, its lower-$26$-digit divisibility check, and its normalized digit. No nonzero output is predicted.

### Final ledger

| Claim | Status |
|---|---|
| Coordinator finite pole pairing | Independently proved at its exact cutoff scope |
| Proposed $P_0+P_1$ identity | Proved, with all inequalities checked |
| Both corrected representatives satisfy the pairing degree budget | Proved from their stated degree bounds |
| All paired layers $\ell\ge14$ vanish at $K=27$ | Proved |
| Complete $\Delta_H$ contribution | Retained and reduced by (6.1) |
| Universal Cartier-section identity | Proved independently of the support audit |
| Explicit resource and division budgets | Proved, conditional on section-coefficient access |
| Original corrected section values | Not evaluated |
| Original normalized coefficient, rank, or endpoint-radical action | Not evaluated |
| Earlier support and actual/core transfer | Conditional pending the stipulated audit |
| Actual $D_0,D_1$ guard, all-prime gcd, whole-error decay | Unresolved |

## Conclusion

The new result is the complete, finite-cutoff identity


$$
\boxed{
\mathcal E_{27}(F)
\text{ factors through }
\mathcal C_{3^{h-27}}F,
\text{ with universal binomial exponent }3^{26}.
}
$$


Together with the verified low-layer cancellation, this removes the moving-$H$ binomial obstruction while retaining both corrected columns, all correction layers, and all carries.

The exact remaining local bottleneck is evaluation of the Cartier sections of the **complete corrected-column products through the bounded finite return**. The present report does not turn that specification into an original coefficient value or a feasible family algorithm.

Beyond it remain the actual determinant/cofactor scalar guard, the final all-prime primitive normalization, and the same-index nonzero whole-error estimate.



$$
\boxed{\text{No unconditional proof or disproof of irrationality of }e+\pi
\text{ has been obtained.}}
$$


