> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5, turn 8 — The exact corrected Gram ideal, the visible normalization bridge, and the missing final-row identity

## Executive conclusions

The attached sources determine more of the normalization than the previous report used, but they do **not** determine the complete conversion to the prescribed final coefficient rows.

The distinction is precise.

1. The exact raw normalization is
   

$$
D_{\rm raw}=4N,\qquad E_{\rm raw}=8H,
   \qquad
   \frac{H}{N}=\frac{E_{\rm raw}}{2D_{\rm raw}}.
$$


   Moreover, the factorial subtraction and the terminal return combine to give the exact identity
   

$$
\boxed{
   b!\,Y=\mathcal R A^{-1}(h^e+h^F)+e_0.
   }
$$


   Thus the factorial normalization of the complete second column is visible. It cannot be discarded as a common row scaling.

2. The attachments do **not** specify the actual finite coefficient rows used to construct $N_{B,1},N_{B,2}$, their complete row contents, or the entries of the prescribed $\Omega$. They also do not give the equation identifying those columns with the raw columns. Consequently, the exact relation between
   

$$
\frac{E_{\rm raw}}{2D_{\rm raw}}
   \quad\text{and}\quad
   \frac{p_n}{q_n}
$$


   is not recoverable from these attachments alone. The displayed binary denominator interface does not determine the missing odd factors or exclude an affine rather than purely multiplicative conversion.

3. A new exact all-prime statement is nevertheless available. After common clearing, write the complete separated Gram pair as
   

$$
\mathcal A=S a+\Delta_A,\qquad
   \mathcal H=S h+\Delta_H.
$$


   Put $g_0=\gcd(a,|h|)$, $a=g_0a_0$, $h=g_0h_0$, and choose
   

$$
r a_0+s h_0=1.
$$


   Then
   

$$
\boxed{
   (\mathcal A,\mathcal H)
   =
   \bigl(Sg_0+r\Delta_A+s\Delta_H,\;
         a_0\Delta_H-h_0\Delta_A\bigr)
   }
$$


   as ideals in $\mathbb Z$. In particular,
   

$$
\boxed{
   \gcd(\mathcal A,|\mathcal H|)
   =
   \gcd\!\left(
      Sg_0+r\Delta_A+s\Delta_H,\,
      |a_0\Delta_H-h_0\Delta_A|
   \right).
   }
$$


   This identifies the **complete correction ideal**, not merely an unspecified odd-prime obstruction.

4. The divisor of the high norm that actually survives into the Gram gcd is exactly
   

$$
\boxed{
   J=\gcd(S,\Delta_A,\Delta_H).
   }
$$


   The corresponding lost high-norm divisor is
   

$$
\boxed{
   L_{\rm sat}=\frac{S}{J}.
   }
$$


   Finite binary congruences do not bound the odd part of $L_{\rm sat}$. They do, however, determine its binary behavior in the guarded ranges already proved.

5. Conditional on the source’s displayed binary denominator interface—or on a recovered exact normalization identity implying it—the separator theorem yields
   

$$
\boxed{
   v_2(q_n)=
   \frac{3n}{2}-v_2(b!)-s_2(n)-1
   }
$$


   whenever
   

$$
c\le22,\qquad t-c\le6,\qquad t=2c+\nu.
$$


   This is a statement about the **actual final binary denominator**, but its normalization premise must remain explicit until the missing row identity is supplied.

No accepted $u_0$ computation is repeated. No pending high-block test is treated as received. No arbitrary-precision continuation of the orders $63,62$, or of the modular factor multiplicities $134,135$, is asserted.

The irrationality or rationality of $e+\pi$ remains unresolved.

---

# 1. Preserved domain and source scope

Throughout,


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0.
$$



The physical domains remain:

- contact coordinates:
  

$$
0\le i<b;
$$


- reconstructed coordinates:
  

$$
\boxed{0\le j\le b}.
$$



Write


$$
W_j=\binom{n+2}{j},\qquad
(Cz)_j=jz_{j-1}-z_j,\qquad
\mathcal R=\operatorname{diag}(W_j)C,
$$


with the original finite conventions $z_{-1}=z_b=0$.

I use $X,Y$ for the complete raw reconstructed columns:


$$
X=\mathcal RA^{-1}f,
$$




$$
Y=\mathcal RA^{-1}r+W_be_b,
\qquad
r=\frac{h^e+h^F-A(j!)_{0\le j<b}}{b!}.
\tag{1.1}
$$



The second formula retains:

- the complete exponential force;
- the complete logarithmic force;
- the factorial subtraction;
- the actual finite inverse;
- the terminal reconstructed contribution.

The accepted precision-$32$ construction gives these complete columns at its stated local scope. It does not turn its modular short presentations into characteristic-zero identities.

Likewise, “integral Schur inverse” here means integrality over $\mathbb Z_2$. A rational matrix congruent to $I\pmod2$ can have nontrivial odd denominators in its inverse. Those denominators remain relevant to exact all-prime normalization.

---

# 2. The exact part of the normalization that is visible

## 2.1 Undoing the factorial subtraction and terminal return

Let


$$
\mathbf j!=(j!)_{0\le j<b}.
$$


At the original finite boundary,


$$
\mathcal R\mathbf j!=-e_0+b!W_be_b.
\tag{2.1}
$$



Indeed:

- at $j=0$, reconstruction gives $-1$;
- for $1\le j<b$,
  

$$
j(j-1)!-j!=0;
$$


- at $j=b$, reconstruction gives
  

$$
b(b-1)!=b!.
$$



Substitution into (1.1) yields


$$
\begin{aligned}
b!Y
&=\mathcal RA^{-1}(h^e+h^F)
  -\mathcal R\mathbf j!+b!W_be_b\\
&=\mathcal RA^{-1}(h^e+h^F)+e_0.
\end{aligned}
$$



Therefore:

### Proposition 2.1 — Exact complete second-column normalization


$$
\boxed{
b!Y=\mathcal RA^{-1}(h^e+h^F)+e_0.
}
\tag{2.2}
$$



This is an exact identity, not a modulo-$2^{32}$ omission statement.

It also explains why neither deleting the exterior term nor adding another exterior correction is legitimate. The terminal return is exactly what converts the factorial subtraction into the $+e_0$ in (2.2).

---

## 2.2 Paying the factors $4$ and $8$

Define


$$
x=\frac X2,\qquad y=\frac Y4.
\tag{2.3}
$$


Then the supplied identities give


$$
\boxed{
N=x^Tx=\frac{D_{\rm raw}}4,\qquad
H=x^Ty=\frac{E_{\rm raw}}8.
}
\tag{2.4}
$$


Thus


$$
\boxed{
\frac HN=\frac{E_{\rm raw}}{2D_{\rm raw}}.
}
\tag{2.5}
$$



Undoing the second-column factorial normalization alone changes $y$ to $b!y$, and changes the mixed-to-norm ratio to


$$
\frac{x^T(b!y)}{x^Tx}=b!\frac HN.
\tag{2.6}
$$


There is no corresponding $b!$ in the first norm in this identity.

This is the first exact reason that one cannot infer the final ratio by saying that “the normalizations cancel.”

---

## 2.3 The primitive pair of the raw ratio, including all clearing factors

Let $e$ be the least positive integer clearing both rational columns $x,y$:


$$
U=ex\in\mathbb Z^{b+1},\qquad
V=ey\in\mathbb Z^{b+1}.
$$


This $e$ is a **raw-column clearer**, not the prescribed final clearer $d_B$.

Set


$$
A_{\rm r}=U^TU=e^2N,\qquad
H_{\rm r}=U^TV=e^2H,
$$




$$
g_{\rm r}=\gcd(A_{\rm r},|H_{\rm r}|).
$$


Then the primitive pair of the raw ratio is exactly


$$
q_{\rm r}=\frac{A_{\rm r}}{g_{\rm r}},
\qquad
p_{\rm r}=\frac{H_{\rm r}}{g_{\rm r}},
\qquad
\frac{p_{\rm r}}{q_{\rm r}}=\frac HN.
\tag{2.7}
$$



For every prime $\ell$, with $v_\ell(0)=+\infty$,


$$
v_\ell(A_{\rm r})
=
2v_\ell(e)+v_\ell(D_{\rm raw})-2\mathbf1_{\ell=2},
$$




$$
v_\ell(H_{\rm r})
=
2v_\ell(e)+v_\ell(E_{\rm raw})-3\mathbf1_{\ell=2}.
$$


Consequently,


$$
\boxed{
v_\ell(q_{\rm r})
=
\max\!\left\{
v_\ell(D_{\rm raw})-v_\ell(E_{\rm raw})
+\mathbf1_{\ell=2},\,0
\right\}.
}
\tag{2.8}
$$



Here cancellation of $e^2$ is justified because it is an explicitly identified **common Gram multiplier**. This argument does not cancel any row-dependent scaling, change $\Omega$, or identify $q_{\rm r}$ with $q_n$.

---

# 3. The exact missing source equations

The attachments repeatedly state


$$
A_B=N_{B,1}^T\Omega N_{B,1},\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B.
\tag{3.1}
$$



But none of the supplied texts defines the entries of the finite coefficient rows from which $N_{B,1},N_{B,2}$ are formed. Nor does either supplied Python source construct those rows or $\Omega$. They construct the raw operator and raw reconstructed-column presentations.

The missing data are the following.

### Missing equation A: the actual coefficient rows

An equation is needed of the form


$$
\mathcal C_{B,i}
=
\bigl(c_{i,1},\ldots,c_{i,r}\bigr),
\qquad i\in\mathcal I_B,
\tag{3.2}
$$


specifying:

- the exact original row domain $\mathcal I_B$;
- every coefficient in each row;
- all factorial, power-of-two, and odd rational prefactors;
- the terminal row, if present.

The content must be the content of the **whole prescribed coefficient row**, not just of the two entries later used in a Gram pairing.

### Missing equation B: row clearing and primitive row content

For example, if the construction first clears each row, the required equations are


$$
\ell_i=\operatorname{lcm}\{\text{reduced denominators of all }c_{i,k}\},
$$




$$
c_i=\gcd_k|\ell_i c_{i,k}|,
\qquad
\mathcal C_{B,i}^{\rm prim}
=\frac{\ell_i}{c_i}\mathcal C_{B,i}.
\tag{3.3}
$$



The actual convention may differ. What is needed is that convention, with every row entry included.

### Missing equation C: the prescribed metric

The entries of


$$
\boxed{\Omega}
\tag{3.4}
$$


must be specified. In particular, it must be known whether any row-content factors have deliberately been compensated in $\Omega$.

### Missing equation D: the final two-column map and least clearer

One needs the exact rational columns $Z_{B,1},Z_{B,2}$ before their common clearing:


$$
N_{B,a}=d_B Z_{B,a},\qquad a=1,2,
\tag{3.5}
$$


together with


$$
\boxed{
d_B=\operatorname{lcm}
\{\text{reduced denominators of every entry of both }Z_{B,1},Z_{B,2}\}.
}
\tag{3.6}
$$



Most decisively, one needs the equation expressing $Z_{B,1},Z_{B,2}$ in terms of the complete $x,y$ from (2.3), including any column mixing or additive rational term.

A pair of exact Gram identities


$$
d_B^{-2}A_B=\mathcal A_n(N,H,\ldots),
\qquad
d_B^{-2}H_B=\mathcal H_n(N,H,\ldots)
\tag{3.7}
$$


with every coefficient specified would also close this interface.

These are missing definitions, not missing numerical residues.

---

## 3.1 Why the displayed binary interface cannot fill this gap

The source gives


$$
v_2(q_n)=
\max\left\{
0,\,
C_n-(\gamma-\alpha)
\right\},
\tag{3.8}
$$


where


$$
C_n=\frac{3n}{2}-v_2(b!)-s_2(n)-1,
\quad
\alpha=v_2(N),\quad\gamma=v_2(H).
\tag{3.9}
$$



Even if (3.8) is retained as an established interface, it does not determine an exact rational conversion.

For instance, under a purely multiplicative conversion


$$
\frac{p_n}{q_n}=\lambda_n\frac HN,
$$


every scalar of the form


$$
\lambda_n=2^{-C_n}\eta_n,
\qquad v_2(\eta_n)=0,
\tag{3.10}
$$


has the same binary denominator law. Its odd numerator and denominator factors can be arbitrarily different.

More concretely, replacing $\eta_n$ by $\eta_n/\ell$, for an odd prime $\ell$ avoiding the relevant primitive numerator, changes the final denominator by $\ell$ while preserving all binary information.

Nor does a denominator valuation identity alone rule out


$$
\frac{p_n}{q_n}=\mu_n+\lambda_n\frac HN.
\tag{3.11}
$$



Thus neither the exact scalar nor the absence of an affine term can be inferred from (3.8).

---

# 4. A primewise bridge that keeps every row-content and metric factor

The following theorem gives the exact bridge once the missing row map is supplied. Its hypotheses are explicit; they are not asserted to have been established for the final source rows.

## 4.1 General common-row map with possible column mixing

Suppose the actual rational columns satisfy


$$
Z_{B,1}=\alpha Lx,
\qquad
Z_{B,2}=\beta Lx+\gamma Ly,
\tag{4.1}
$$


where $L$ is the exact rational row map, including all prescribed row-content divisions. Let


$$
M=L^T\Omega L.
\tag{4.2}
$$


Define


$$
F=x^TMx,\qquad G=x^TMy.
\tag{4.3}
$$



Then


$$
A_B=d_B^2\alpha^2F,
$$




$$
H_B=d_B^2\alpha(\beta F+\gamma G).
\tag{4.4}
$$



Therefore:

### Theorem 4.1 — Exact row-metric and primewise bridge
Under (4.1),


$$
\boxed{
\frac{p_n}{q_n}
=
\frac{\beta}{\alpha}
+
\frac{\gamma}{\alpha}\frac GF.
}
\tag{4.5}
$$



For every prime $\ell$,


$$
\boxed{
v_\ell(q_n)
=
\max\!\left\{
v_\ell(\alpha)+v_\ell(F)
-v_\ell(\beta F+\gamma G),\,0
\right\}.
}
\tag{4.6}
$$


The final gcd itself is


$$
\boxed{
v_\ell(g_B)
=
\min\!\left\{
2v_\ell(d_B)+2v_\ell(\alpha)+v_\ell(F),\,
2v_\ell(d_B)+v_\ell(\alpha)
+v_\ell(\beta F+\gamma G)
\right\}.
}
\tag{4.7}
$$



In particular, the primitive multiplier remains exactly


$$
\boxed{
\frac{d_B^2}{g_B},
}
$$


with primewise valuation


$$
2v_\ell(d_B)-v_\ell(g_B).
\tag{4.8}
$$



### Proof

Equations (4.4) follow by direct substitution into the two prescribed Gram forms. Taking their ratio proves (4.5). Taking valuations and using


$$
v_\ell(A_B/\gcd(A_B,H_B))
=\max\{v_\ell(A_B)-v_\ell(H_B),0\}
$$


proves (4.6)–(4.8). ∎

This theorem cancels only the proved common factor $d_B^2$ in the ratio. It preserves the entire effect of row normalization through $M$.

---

## 4.2 The metric defect is explicit

Set


$$
\delta_N=x^T(M-I)x,\qquad
\delta_H=x^T(M-I)y.
\tag{4.9}
$$


Then


$$
F=N+\delta_N,\qquad G=H+\delta_H,
$$


so (4.5) becomes


$$
\boxed{
\frac{p_n}{q_n}
=
\frac{\beta}{\alpha}
+
\frac{\gamma}{\alpha}
\frac{H+\delta_H}{N+\delta_N}.
}
\tag{4.10}
$$



Thus a pure raw-ratio bridge requires, at minimum, an appropriate exact metric identity. It is not enough to identify scalar factors in the two columns.

For example, if row normalization acts by


$$
L=\operatorname{diag}(\sigma_i),
$$


then


$$
M_{ij}=\sigma_i\Omega_{ij}\sigma_j.
\tag{4.11}
$$


If $\Omega$ is diagonal,


$$
M_{ii}=\Omega_{ii}\sigma_i^2.
$$


Dividing a row by its content changes the metric unless the prescribed $\Omega$ compensates that division exactly.

This is the precise obstruction to asserting that row scaling either “cancels” or “does not matter.”

---

## 4.3 Purely multiplicative specialization, with all odd factors

Suppose the missing source identities establish


$$
\beta=0,\qquad M=I.
$$


Put


$$
\lambda=\gamma/\alpha=a/b,
\qquad \gcd(a,b)=1,\quad b>0.
$$


Using the raw primitive pair (2.7),


$$
\frac{p_n}{q_n}=\frac{a p_{\rm r}}{bq_{\rm r}}.
$$



The complete cancellation is


$$
\gcd(a p_{\rm r},bq_{\rm r})
=
\gcd(|a|,q_{\rm r})\gcd(b,|p_{\rm r}|).
$$


Consequently,


$$
\boxed{
q_n=
\frac{bq_{\rm r}}
{\gcd(|a|,q_{\rm r})\gcd(b,|p_{\rm r}|)}.
}
\tag{4.12}
$$



Equivalently, for every prime,


$$
\boxed{
v_\ell(q_n)
=
\max\!\left\{
v_\ell(D_{\rm raw})-v_\ell(E_{\rm raw})
+\mathbf1_{\ell=2}-v_\ell(\lambda),\,0
\right\}.
}
\tag{4.13}
$$



This is the requested explicit primewise bridge in the pure-scalar case. It includes every odd numerator and denominator factor of $\lambda$, and it does not substitute a selected-prime gcd for $g_B$.

If the actual conversion is affine, write


$$
\mu=A/w,\qquad\lambda=B/w
$$


using a common positive denominator. Then the exact formula instead is


$$
\boxed{
q_n=
\frac{wq_{\rm r}}
{\gcd\!\left(wq_{\rm r},\,|Aq_{\rm r}+Bp_{\rm r}|\right)}.
}
\tag{4.14}
$$


The cancellation inside $Aq_{\rm r}+Bp_{\rm r}$ must then be evaluated; it cannot be reconstructed from the valuation of $H/N$ alone.

---

# 5. The exact complete separated raw Gram ideal

I now apply the retained separator theorem to an exact integral model. This step does not require the missing final-row normalization.

Let


$$
b=b_0+2^Lh,\qquad L\ge135,\qquad h\ge1,
$$


be an original parameter satisfying the retained separator hypotheses.

Put


$$
T=103,\qquad M=2^T,\qquad m_h=2^{L-T}h.
$$


Let $H_k=H_{L,h}(k)$ be the exact high entries from turn 7, and


$$
S=\sum_{k=0}^{m_h}H_k^2.
\tag{5.1}
$$



Define the embedding


$$
\mathcal T_H:\mathbb Q^{b_0+1}\longrightarrow\mathbb Q^{b+1}
$$


by


$$
(\mathcal T_H z)_{j_0+Mk}=H_kz_{j_0}
$$


for


$$
0\le j_0\le b_0,\qquad0\le k\le m_h,
$$


and zero on the unsupported rows.

Every supported model row lies in the actual inclusive range $0\le j\le b$, including $j=b$. Moreover,


$$
\boxed{\mathcal T_H^T\mathcal T_H=S I.}
\tag{5.2}
$$



Let


$$
x_0=X_0/2,\qquad y_0=Y_0/4.
$$


The complete separator theorem gives exact residuals


$$
x=\mathcal T_Hx_0+\varepsilon_x,
\qquad
y=\mathcal T_Hy_0+\varepsilon_y,
\tag{5.3}
$$


with


$$
\varepsilon_x\in2^{31}\mathbb Z_{(2)}^{b+1},
\qquad
\varepsilon_y\in2^{30}\mathbb Z_{(2)}^{b+1}.
\tag{5.4}
$$



The different depths $31,30$ are the paid divisions by $2$ and $4$. They must not both be called $32$-bit residuals after normalization.

---

## 5.1 Common exact clearing

Let $e_*$ be the least common clearer of


$$
x,y,x_0,y_0.
$$


On the present separator domain these vectors are binary integral, so $e_*$ is odd. Define


$$
u_0=e_*x_0,\qquad v_0=e_*y_0,
$$




$$
R=e_*\varepsilon_x,\qquad T'=e_*\varepsilon_y.
$$


All four vectors are integral.

Then


$$
e_*x=\mathcal T_Hu_0+R,
\qquad
e_*y=\mathcal T_Hv_0+T'.
\tag{5.5}
$$



Set


$$
a=u_0^Tu_0,\qquad h=u_0^Tv_0.
$$


The exact cleared raw Gram pair is


$$
\mathcal A=e_*^2N,\qquad
\mathcal H=e_*^2H.
$$



Expansion of the complete finite contractions gives


$$
\boxed{
\mathcal A=Sa+\Delta_A,
}
\tag{5.6}
$$




$$
\boxed{
\mathcal H=Sh+\Delta_H,
}
\tag{5.7}
$$


where


$$
\boxed{
\Delta_A
=
2(\mathcal T_Hu_0)^TR+R^TR,
}
\tag{5.8}
$$


and


$$
\boxed{
\Delta_H
=
(\mathcal T_Hu_0)^TT'
+R^T\mathcal T_Hv_0
+R^TT'.
}
\tag{5.9}
$$



These corrections contain the whole physical discrepancy. In particular, no corrected branch, re-entering finite return, unsupported row, or terminal coordinate has been deleted.

---

# 6. A unimodular description of the complete Gram ideal

The following elementary integral reduction is useful because it separates correction **along** the model direction from correction **across** it.

### Theorem 6.1 — Complete corrected Gram ideal

Let


$$
\mathcal A=Sa+\Delta_A,\qquad
\mathcal H=Sh+\Delta_H
$$


be integers, with $a>0$. Write


$$
g_0=\gcd(a,|h|),\qquad a=g_0a_0,\qquad h=g_0h_0.
$$


Choose integers $r,s$ satisfying


$$
ra_0+sh_0=1.
$$



Define


$$
U=r\Delta_A+s\Delta_H,
\qquad
V=a_0\Delta_H-h_0\Delta_A.
\tag{6.1}
$$


Then


$$
\boxed{
(\mathcal A,\mathcal H)=(Sg_0+U,V)
}
\tag{6.2}
$$


as ideals in $\mathbb Z$. Consequently,


$$
\boxed{
g=\gcd(\mathcal A,|\mathcal H|)
=\gcd(Sg_0+U,|V|).
}
\tag{6.3}
$$



For every prime $\ell$,


$$
\boxed{
v_\ell(g)
=
\min\{v_\ell(Sg_0+U),v_\ell(V)\}.
}
\tag{6.4}
$$



### Proof

The matrix


$$
P=
\begin{pmatrix}
r&s\\
-h_0&a_0
\end{pmatrix}
$$


has determinant


$$
ra_0+sh_0=1.
$$


It is therefore unimodular. Applying it to the column $(\mathcal A,\mathcal H)^T$ gives


$$
P
\begin{pmatrix}\mathcal A\\ \mathcal H\end{pmatrix}
=
\begin{pmatrix}
Sg_0+U\\
V
\end{pmatrix}.
$$


A unimodular transformation preserves the ideal generated by the coordinates. This proves all assertions. ∎

---

## 6.1 Exact mixed alignment

The transverse correction $V$ measures the entire projective discrepancy:


$$
\boxed{
\frac{\mathcal H}{\mathcal A}-\frac{h_0}{a_0}
=
\frac{V}{a_0\mathcal A}.
}
\tag{6.5}
$$



Thus the high norm disappears from the **model direction**, but not from the actual denominator. Its cancellation in the actual primitive pair is controlled by $U,V$.

This is stronger than a statement that “there might be an odd-prime correction.” The correction is now an explicit integer:


$$
V=a_0\Delta_H-h_0\Delta_A,
$$


with $\Delta_A,\Delta_H$ given by the complete finite sums (5.8)–(5.9).

---

## 6.2 The exact saturation divisor

From (5.6)–(5.7),


$$
\gcd(S,\mathcal A,\mathcal H)
=
\gcd(S,\Delta_A,\Delta_H).
$$


Therefore


$$
\boxed{
\gcd(S,g)=J:=\gcd(S,\Delta_A,\Delta_H).
}
\tag{6.6}
$$



The part of $S$ not certified to enter the final Gram gcd is exactly


$$
\boxed{
L_{\rm sat}=\frac{S}{J}.
}
\tag{6.7}
$$



Primewise,


$$
\boxed{
v_\ell(L_{\rm sat})
=
\max\!\left\{
v_\ell(S)-\min\bigl(v_\ell(\Delta_A),v_\ell(\Delta_H)\bigr),
\,0
\right\}.
}
\tag{6.8}
$$



Equation (6.8) is an exact all-prime obstruction. A congruence at the prime $2$ supplies no information about its odd-prime terms.

---

# 7. The paid binary specialization

Write, exactly as in turn 7,


$$
c=\min_k v_2(H_k),\qquad
t=v_2(S),\qquad
S=2^{2c}\Sigma,\qquad
\nu=v_2(\Sigma),
$$


so


$$
\boxed{t=2c+\nu.}
\tag{7.1}
$$



Assume $c\le22$. Since $x_0$ has exact binary content $8$, while $y_0$ has content at least $8$, equations (5.8)–(5.9) give


$$
\boxed{
v_2(\Delta_A)\ge40+c,\qquad
v_2(\Delta_H)\ge38+c.
}
\tag{7.2}
$$



These are exactly the turn-7 budgets after dividing $D_{\rm raw}$ by $4$ and $E_{\rm raw}$ by $8$.

The accepted low pair satisfies


$$
v_2(a)=v_2(h)=31,
$$


because $e_*$ is odd. Hence


$$
v_2(g_0)=31,\qquad a_0,h_0\ \text{odd}.
\tag{7.3}
$$


It follows that


$$
v_2(U)\ge38+c,\qquad v_2(V)\ge38+c.
\tag{7.4}
$$



If


$$
t-c\le6,
$$


then


$$
31+t<38+c.
$$


The first coordinate of the transformed ideal therefore has exact depth $31+t$, while the second is deeper. Theorem 6.1 gives


$$
\boxed{
v_2(g_{\rm r})=31+t,\qquad v_2(q_{\rm r})=0.
}
\tag{7.5}
$$



This is an exact binary statement about the primitive raw ratio. It is not yet a statement about $q_n$.

---

## 7.1 The whole mixed alignment after the factors $4,8$

The retained undivided relation


$$
E_{\rm raw}-98D_{\rm raw}\in2^{41+c}\mathbb Z_{(2)}
$$


becomes


$$
\boxed{
H-49N\in2^{38+c}\mathbb Z_{(2)}.
}
\tag{7.6}
$$



When $t-c\le6$,


$$
v_2(N)=v_2(H)=31+t,
$$


and therefore


$$
\boxed{
\frac HN\equiv49\pmod{2^{\,7+c-t}}
=
49\pmod{2^{\,7-c-\nu}}.
}
\tag{7.7}
$$



Both high losses are paid:

- coordinate content contributes $c$;
- normalized norm cancellation contributes $\nu$.

The ratio guard is not a function of $\nu$ alone.

The first primitive binary norm loss remains


$$
(31+t)-2(8+c)=15+\nu.
\tag{7.8}
$$



---

## 7.2 Slightly wider denominator-only ranges

The exact mixed valuation need not be visible to constrain the raw binary denominator.

From the retained norm and mixed congruences:

- if $t-c\le7$, then
  

$$
v_2(H)\ge v_2(N),
  \qquad
  \boxed{v_2(q_{\rm r})=0};
$$


- if $t-c\le8$, then
  

$$
v_2(H)\ge v_2(N)-1,
  \qquad
  \boxed{v_2(q_{\rm r})\le1}.
$$



These are denominator-only statements. They do not supply a positive-precision unit ratio throughout those wider ranges.

No depth-one occurrence theorem on the original powers is assumed here.

---

# 8. Transporting the correction ideal through the actual row metric

The previous sections give the exact raw correction ideal. The remaining normalization problem is to identify its image under the actual final row map.

Suppose the missing source equation supplies the map (4.1). Let $M_b=L_b^T\Omega_bL_b$, and let $M_0$ be the corresponding low-model metric.

Define the **compressed metric defect**


$$
\boxed{
\mathcal D_M
=
\mathcal T_H^TM_b\mathcal T_H-SM_0.
}
\tag{8.1}
$$



Using (5.3), the normalized first norm is exactly


$$
\begin{aligned}
x^TM_bx
={}&Sx_0^TM_0x_0\\
&+x_0^T\mathcal D_Mx_0
+2x_0^T\mathcal T_H^TM_b\varepsilon_x
+\varepsilon_x^TM_b\varepsilon_x.
\end{aligned}
\tag{8.2}
$$


Similarly,


$$
\begin{aligned}
x^TM_by
={}&Sx_0^TM_0y_0\\
&+x_0^T\mathcal D_My_0
+x_0^T\mathcal T_H^TM_b\varepsilon_y\\
&+\varepsilon_x^TM_b\mathcal T_Hy_0
+\varepsilon_x^TM_b\varepsilon_y.
\end{aligned}
\tag{8.3}
$$



These formulas exhibit three distinct corrections:

1. the metric defect caused by the actual row normalization;
2. the complete first-column residual;
3. the complete second-column residual, including all returns and the terminal contribution.

Even if $\varepsilon_x,\varepsilon_y$ are highly divisible by $2$, the term $\mathcal D_M$ is not controlled until the actual row contents and $\Omega$ are known.

After inserting the exact column scalars and clearing all rational coefficients by a specified common multiplier, equations (8.2)–(8.3) become an integral pair


$$
\mathcal A=\kappa A_B=Sa+\Delta_A,
\qquad
\mathcal H=\kappa H_B=Sh+\Delta_H.
\tag{8.4}
$$


Here $\kappa$ is recorded explicitly. If the common multiplication comes from enlarging a column clearer, then it is the square of the clearer ratio.

Since


$$
\gcd(\kappa A_B,\kappa H_B)=\kappa g_B,
$$


the primitive denominator is unchanged:


$$
\frac{\mathcal A}{\gcd(\mathcal A,\mathcal H)}=q_n.
\tag{8.5}
$$



Theorem 6.1 then applies to the **actual normalized Gram ideal**, with all row contents and odd denominators included in $a,h,\Delta_A,\Delta_H,\kappa$.

This is the concrete next bridge. It requires the missing normalization equations, not another raw Gram computation.

---

# 9. What a height bound on saturation would accomplish

The exact saturation divisor gives a direct denominator inequality.

For any integral representation


$$
\mathcal A=Sa+\Delta_A,\qquad
\mathcal H=Sh+\Delta_H,
$$


let


$$
J=\gcd(S,\Delta_A,\Delta_H),\qquad L_{\rm sat}=S/J.
$$


Because $J\mid\gcd(\mathcal A,\mathcal H)$,


$$
\boxed{
q_n\le
\frac{\mathcal A}{J}
=
L_{\rm sat}\left(a+\frac{\Delta_A}{S}\right),
}
\tag{9.1}
$$


when $\mathcal A>0$.

Thus a useful global follow-on lemma is now sharply formulated.

### Complete normalized saturation lemma — outstanding target

On an infinite sequence of original indices, construct the exact representation (8.4) and prove


$$
\log L_{\rm sat}\le \eta n+o(n),
\tag{9.2}
$$


together with


$$
\log\left|a+\frac{\Delta_A}{S}\right|
\le \theta n+o(n),
\tag{9.3}
$$


where


$$
\eta+\theta<
\left(2+\frac1{4002}\right)\log(1+\sqrt2).
\tag{9.4}
$$



Then (9.1), combined with the whole-error theorem at its established scope and with nonvanishing, would give the required denominator-versus-error comparison.

Every normalization factor must occur in the representation used for (9.2)–(9.3). In particular, one cannot prove these bounds for the raw pair and silently transfer them to the final pair.

---

## 9.1 What correction height does—and does not—prove

For the raw integral corrections of §5, ordinary Cauchy–Schwarz gives


$$
|\Delta_A|
\le
2\sqrt{Sa}\,\|R\|+\|R\|^2,
\tag{9.5}
$$


and


$$
|\Delta_H|
\le
\sqrt S\bigl(\|u_0\|\|T'\|+\|v_0\|\|R\|\bigr)
+\|R\|\|T'\|.
\tag{9.6}
$$


Hence


$$
|V|
\le |a_0|\,|\Delta_H|+|h_0|\,|\Delta_A|.
\tag{9.7}
$$



These are rigorous height bounds in terms of the actual residual norms. They are not uniform original-family estimates.

There is also an important directional warning. If $V\ne0$, then


$$
g\le |V|,
\qquad
q\ge \frac{\mathcal A}{|V|}.
\tag{9.8}
$$


Thus an upper bound on the transverse correction can give a **lower** denominator bound. It does not by itself prove the upper denominator bound required for irrationality.

For an upper bound, one needs large exact common divisibility—such as control of $L_{\rm sat}$—not merely small residuals or a finite-rank endpoint description.

---

# 10. Conditional conversion to the actual final binary denominator

The displayed source interface is


$$
v_2(q_n)=\max\{0,C_n-(\gamma-\alpha)\},
$$


with $C_n$ from (3.9).

It would follow, for example, from an exact pure-scalar bridge satisfying


$$
v_2(\lambda_n)=-C_n.
$$


It can also have other derivations from the original coefficient rows. Those rows are not supplied here, so I distinguish the following deduction from a newly proved normalization theorem.

### Conditional Corollary 10.1

Assume the source’s binary denominator interface holds for the actual final pair. On an original separator parameter with


$$
c\le22,\qquad t-c\le6,
$$


the complete raw transfer gives


$$
\alpha=v_2(N)=31+t,\qquad
\gamma=v_2(H)=31+t.
$$


Therefore


$$
\boxed{
v_2(q_n)=C_n
=
\frac{3n}{2}-v_2(b!)-s_2(n)-1.
}
\tag{10.1}
$$



In the wider ranges,


$$
t-c\le7\quad\Longrightarrow\quad v_2(q_n)\le C_n,
\tag{10.2}
$$


and


$$
t-c\le8\quad\Longrightarrow\quad v_2(q_n)\le C_n+1.
\tag{10.3}
$$



These conclusions preserve the actual final denominator interface; they do not identify it with the raw denominator.

---

## 10.1 The resulting odd-prime budget

Using


$$
v_2(b!)=b-s_2(b),\qquad b=n/4002,
$$


we have


$$
C_n=
\left(\frac32-\frac1{4002}\right)n
+s_2(b)-s_2(n)-1.
\tag{10.4}
$$


Thus


$$
C_n\log2
=
\left(\frac32-\frac1{4002}\right)n\log2
+O(\log n).
$$



On a sequence where (10.1) holds, write


$$
q_n=2^{C_n}q_{n,\rm odd}.
$$


Under the source’s whole-error asymptotic


$$
\log|\epsilon_n|
=
-\beta n+o(n),
\qquad
\beta=
\left(2+\frac1{4002}\right)\log(1+\sqrt2),
\tag{10.5}
$$


a sufficient remaining estimate is


$$
\boxed{
\log q_{n,\rm odd}
\le
\left[
\beta-
\left(\frac32-\frac1{4002}\right)\log2
-\delta
\right]n
}
\tag{10.6}
$$


for some $\delta>0$.

The available exponential margin is approximately $0.7234n$.

This converts the local binary information into a concrete global target. It does not prove that target: the actual odd normalization factors and their saturation remain to be established.

---

# 11. Precision-uniform scope

I do not claim the second, all-$K$ target in this report.

The retained divided-power filtration does support the familiar operator bandwidth


$$
m(K)=4(K-1)
$$


for an operator calculation modulo $2^K$. But that observation alone does not prove a complete all-$K$ producer-and-separator theorem.

Such a theorem must also specify and prove:

- central and first-force tail cutoffs;
- full exterior-load length;
- both finite-return lengths;
- the complete Laurent principal parts;
- reconstruction precision;
- the logarithmic-force threshold or its explicit inclusion;
- low-argument bounds for every retained atom;
- separator length and parameter guard;
- the representation of both branches before any modular branch disappearance.

In particular, the precision-$32$ orders $63,62$ and factor counts $134,135$ cannot be inserted into an all-$K$ statement.

The present advance instead addresses the first requested target: the exact Gram-ideal interface and its normalization obstruction.

---

# 12. Arithmetic status and a bounded check of the new ideal reduction

No new original-index arithmetic is needed to prove Theorem 6.1. It is an integral unimodular identity.

The coordinator’s pending high-block tests remain separate. I assume no receipt for them, and propose no rerun of the accepted $u_0$ pipeline.

If a bounded implementation check of the **new saturation reduction** is desired, the following small input tests a case where a binary correction congruence creates no odd high-norm divisibility.

### Inputs


$$
S=15,\qquad a=6,\qquad h=10,\qquad
\Delta_A=16,\qquad\Delta_H=32.
$$


Then


$$
g_0=2,\quad a_0=3,\quad h_0=5,\quad r=2,\quad s=-1.
$$



### Expected verifiable output


$$
\mathcal A=106,\qquad \mathcal H=182,
$$




$$
U=2\cdot16-32=0,\qquad
V=3\cdot32-5\cdot16=16,
$$




$$
\gcd(106,182)=\gcd(30,16)=2,
$$




$$
q=53,\qquad p=91,
$$




$$
J=\gcd(15,16,32)=1,\qquad L_{\rm sat}=15.
$$



This is only a small exact test of the new ideal formulas. It is not a high-block evaluation, not an original-family example, and not evidence about the missing normalization.

For the actual bridge, the next required input is documentary and mathematical: equations (3.2)–(3.7). No bounded numerical calculation can infer those definitions from the raw residues.

---

# 13. Proof-status ledger

| Statement | Status |
|---|---|
| Original finite domains and complete corrected raw columns | Preserved |
| Operator guard $39$, downstream guard $40$, hence $41$ | Reused at retained symbolic scope |
| Complete inclusive-row separator transfer | Reused at retained symbolic scope |
| $D_{\rm raw}=4N,\ E_{\rm raw}=8H$ | Exact source identities, explicitly paid |
| $b!Y=\mathcal RA^{-1}(h^e+h^F)+e_0$ | **Proved here from the finite reconstruction identity** |
| All-prime primitive denominator of the raw ratio | **Derived exactly** |
| Actual final row definitions, row contents, and $\Omega$ | Missing from the attachments |
| Exact raw-to-final scalar or affine conversion | Not determined |
| General row-metric primewise bridge | **Proved under explicit map hypotheses** |
| Exact complete raw corrections $\Delta_A,\Delta_H$ | **Derived** |
| Unimodular corrected Gram-ideal identity | **Proved over $\mathbb Z$, all primes** |
| Exact saturation divisor $S/\gcd(S,\Delta_A,\Delta_H)$ | **Proved** |
| Metric-defect correction for normalized rows | **Explicit exact formula** |
| Paid binary raw denominator and mixed alignment | **Derived from retained transfer** |
| Actual final binary denominator $v_2(q_n)=C_n$ | Conditional on the displayed final normalization interface |
| Infinitely many original depth-one high blocks | Not proved; not assumed |
| Precision-uniform complete all-$K$ producer/separator theorem | Not claimed |
| Small saturation implementation check | Bounded specification; no execution receipt claimed |
| Actual all-prime denominator versus whole same-index error | Open |
| Irrationality or rationality of $e+\pi$ | Unresolved |

---

# Conclusion

The new result is an exact description of the complete corrected Gram ideal:


$$
\boxed{
(Sa+\Delta_A,\;Sh+\Delta_H)
=
\bigl(Sg_0+r\Delta_A+s\Delta_H,\;
a_0\Delta_H-h_0\Delta_A\bigr).
}
$$



It identifies both:

- the transverse mixed-alignment correction;
- the exact saturation divisor governing how much of the high norm survives into the gcd.

The visible normalization has also been advanced:


$$
\boxed{
N=X^TX/4,\qquad H=X^TY/8,\qquad
b!Y=\mathcal RA^{-1}(h^e+h^F)+e_0.
}
$$


All powers of two in this visible bridge are accounted for, and the complete factorial subtraction and terminal return are retained.

The precise obstruction to completing the requested final bridge is not an unevaluated raw contraction. It is the absence, in the supplied attachments, of the actual coefficient-row normalization equation and prescribed metric. Without those equations, the odd factors—and even the distinction between a scalar and affine ratio conversion—are mathematically underdetermined.

Once that source identity is supplied, the next concrete target is


$$
\boxed{
\text{bound the complete normalized saturation loss }
L_{\rm sat}
\text{ and the cleared model height on an infinite original sequence}.
}
$$


That bound must use the actual $g_B$, actual $d_B$, and actual primitive $q_n$.

Finally, the decisive real identity remains


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n,
}
$$


with the whole nonzero evaluated error at the same original index. No local omission or Gram congruence removes a term from this identity.

The present work supplies an exact all-prime correction-ideal framework and a conditional final binary denominator constraint. It does not yet establish the global denominator-versus-whole-error inequality needed to resolve the irrationality of $e+\pi$.
