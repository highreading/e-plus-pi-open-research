> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Charged actual perturbations: what the finite inverse budget proves, and the missing support identity

## 1. Scope and conclusion

The objective remains an unconditional decision on the rationality or irrationality of $e+\pi$. No such decision follows from the supplied work or from the results below.

This report retains the original domain


$$
j>0,\qquad j\equiv84645\pmod{531441},
$$


with


$$
m=2^{2j-1},\quad n=4^j+1,\quad A=n-2=2m-1,\quad
H=3^{h-1},\quad D=H-A,
$$


and


$$
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15}.
$$


On the sufficiently large retained tuples,


$$
v_3(A)=v_3(D)=5,\qquad D\ge486.
$$



The finite coordinates are exactly


$$
U_u=x^u\quad(0\le u<D),\qquad
z_i=x^Dy^i\quad(0\le i<\nu),\qquad
Y_b=y^b\quad(d\le b\le m),
$$


where


$$
x=y-1,\qquad d=\frac{3D}{2}-1,\qquad \nu=\frac D2-1.
$$



The main conclusions are:

1. **The conservative six-digit charge per actual perturbation insertion is valid.** Consequently, at precision $3^{20}$, no more than three insertions can contribute.
2. **This does not establish the proposed polynomial-support invariant.** The finite insertion bound and the spatial-support claim are different statements.
3. **A new proved simplification is available:** in the next-digit formula, all actual-inverse corrections caused by the producer can be replaced by the corresponding complete core blocks. Their effect is beyond the observed precision.
4. **A new exact sensitivity formula identifies a specific unresolved higher producer layer:** a change
   

$$
\mathscr R\longmapsto\mathscr R+27P
$$


   changes the combined observed digit by an explicitly displayed complete-functional pairing. This is the precise term that a successful actual-support argument must annihilate.

The report does **not** claim that this pairing is nonzero for the actual producer. Nor does it claim its vanishing. Thus it identifies an obstruction to the proposed proof, not a counterexample to the proposed invariant.

---

## 2. Complete objects and retained results

The functional is


$$
\mathcal M(G)=
-\frac{3^h}{4}\mathfrak f(G)
+
3^h\sum_{v=0}^{2n-2}
\frac{[y^v](G-G(-1))/(y+1)}{2v+1},
\qquad
\mathfrak f(y^s)=(2s)!.
$$


Every pole through $4n-3$, endpoint subtraction, and factorial contribution remains present.

Set


$$
Q_c=(y+1)x^A(\beta+3y),\qquad \beta=-71-A,
$$




$$
W=[U\ Y],\qquad F=Z-WE_c^{-1}C_c.
$$


The $F_i$ are the complete core-orthogonal columns.

Write


$$
R_{\rm prod}=3\mathscr R,\qquad
G_{\rm act}=G_c+3^7K_{\mathscr R},
\quad
K_{\mathscr R}(f,g)=\mathcal M(\mathscr Rfg).
$$



The established theorem


$$
\mathcal Q\in243M_\nu(\mathbb Z_3)
$$


is retained at its original scope. The closed $350$- and $62$-coordinate calculations are not repeated. The optional $452$-coordinate endpoint calculation is not requested.

The stronger width-$20$ conclusions remain under review. In particular, this report does not promote


$$
S_c\in3^{21}M,\qquad \Phi_R\in3^{20}M
$$


from reviewed premises to unconditional conclusions.

For the actual blocks, use


$$
E_{\rm act}=
\begin{pmatrix}3L&3X\\3X^T&E_Y\end{pmatrix},
\qquad
\widehat E=E_Y-3X^TL^{-1}X.
$$


Define


$$
T(\mathscr R)=
\bigl(\mathcal M(\mathscr R\,wF_i)\bigr)_{w,i}
=3\binom{\alpha}{\beta_s},
$$




$$
\alpha=3a,\qquad
\widetilde\beta_s=\beta_s-X^TL^{-1}\alpha
=-\kappa e_m\tau^T+3B,
\qquad \tau=e_{\nu-1}.
$$



The complete next digit is


$$
\boxed{
K_{18}\equiv
\frac{a^TL^{-1}a}{3}+B^TRB
-\kappa\operatorname{Sym}_\tau\left(\frac{B_d}{3}-B_{d+1}\right)
-\kappa^2\frac{V_{dd}}3\,\tau\tau^T
\pmod3,
}
\tag{2.1}
$$


where


$$
\widehat E=K_0+3V,\qquad R=K_0^{-1},
$$


and


$$
\operatorname{Sym}_\tau(r)=\tau r+r^T\tau^T.
$$


All divisions in (2.1) are justified by the retained divisibilities.

---

## 3. The charged inverse-walk budget is valid

Let


$$
\Delta E=E_{\rm act}-E_c
=3^7K_{\mathscr R}(W,W).
$$


The complete functional is integral on integral polynomial inputs at the retained cutoff, and $\mathscr R$ is integral. Therefore


$$
\Delta E\in3^7M.
$$



The established eliminated-core inverse bound gives


$$
E_c^{-1}\in3^{-1}M.
$$


Consequently


$$
T=E_c^{-1}\Delta E\in3^6M.
\tag{3.1}
$$


This is the paid LOW division: the perturbation has seven digits, and multiplication by the eliminated inverse may consume one.

Since


$$
E_{\rm act}^{-1}=(I+T)^{-1}E_c^{-1},
$$


the finite geometric expansion gives


$$
(I+T)^{-1}
\equiv I-T+T^2-T^3\pmod{3^{24}}.
\tag{3.2}
$$


Thus four insertions have valuation at least $24$ before the final possible inverse loss, and at least $23$ afterward. They cannot affect precision $3^{20}$.

All products in (3.2) take place in the unchanged finite eliminated space. No coordinate beyond $Y_m$ is introduced.

### What this proves—and does not prove

Equation (3.2) proves the **number of relevant insertions**. It proves no assertion about the polynomial support of


$$
W T^\ell E_c^{-1}C_c
\quad\text{or}\quad
W T^\ell E_c^{-1}K_{\mathscr R}(W,Z).
$$



In particular,


$$
7\cdot45=315<D
$$


is useful only after proving that each insertion loses at most $45$ powers of $x$, including its LOW projection and all finite HIGH returns. The valuation budget alone supplies no such statement.

---

## 4. New result: actual-inverse perturbations are invisible to this digit

Use superscript $c$ for the corresponding complete core blocks:


$$
E_c=
\begin{pmatrix}
3L_c&3X_c\\
3X_c^T&E_{Y,c}
\end{pmatrix},
\qquad
\widehat E_c=E_{Y,c}-3X_c^TL_c^{-1}X_c.
$$



Because $\Delta E\in3^7M$,


$$
L-L_c\in3^6M,\qquad
X-X_c\in3^6M,\qquad
E_Y-E_{Y,c}\in3^7M.
\tag{4.1}
$$


Both LOW matrices are units, so


$$
L^{-1}-L_c^{-1}
=L^{-1}(L_c-L)L_c^{-1}\in3^6M.
\tag{4.2}
$$


It follows that


$$
X^TL^{-1}-X_c^TL_c^{-1}\in3^6M,
\tag{4.3}
$$


and hence


$$
\widehat E-\widehat E_c\in3^7M.
\tag{4.4}
$$



Define


$$
V_c=(\widehat E_c-K_0)/3.
$$


Then


$$
V-V_c\in3^6M.
\tag{4.5}
$$



The source $a=T(\mathscr R)_U/9$ uses the fixed core columns $F$; it does not involve the actual eliminated inverse. Define the core-feedback source


$$
B^c=
\frac{\beta_s-X_c^TL_c^{-1}\alpha+\kappa e_m\tau^T}{3}.
$$


Using $\alpha=3a$, equation (4.3) gives


$$
B-B^c\in3^6M.
\tag{4.6}
$$



### Proposition 4.1

In (2.1), one may replace


$$
L^{-1},\quad B,\quad V
$$


by


$$
L_c^{-1},\quad B^c,\quad V_c
$$


without changing $K_{18}$.

### Proof

The change in $a^TL^{-1}a/3$ belongs to $3^5M$. The change in $B_d/3$ belongs to $3^5M$; changes in $B_{d+1}$ and $B^TRB$ belong to $3^6M$. Finally, the change in $V_{dd}/3$ belongs to $3^5M$. All vanish modulo $3$. ∎

This removes **actual-inverse dependence**, not higher producer-source dependence. The complete source and its complete core feedback remain.

---

## 5. A concrete higher-jet obstruction in the combined observation

The following calculation isolates an actual coefficient-level obligation rather than another expansion of an unevaluated Gram.

For this section, all inverse blocks are the complete core blocks, as permitted by Proposition 4.1. Write them as $L,X$ for readability.

Let $P\in\mathbb Z_3[y]$, and compare two integral producers


$$
\mathscr R'=\mathscr R+27P.
\tag{5.1}
$$


This comparison is a sensitivity calculation; it does not assert that the original producer can be varied arbitrarily.

Define the complete finite sources


$$
t_U=\bigl(\mathcal M(PU_uF_i)\bigr)_{u,i},
\qquad
t_Y=\bigl(\mathcal M(PY_bF_i)\bigr)_{b,i},
$$


and


$$
c=t_Y-X^TL^{-1}t_U.
\tag{5.2}
$$



Directly from the source normalizations,


$$
a'=a+3t_U,
\qquad
B'=B+3c.
\tag{5.3}
$$


The residue $\kappa$ and its fixed lift are unchanged.

The LOW quadratic term changes by


$$
\begin{aligned}
\frac{(a+3t_U)^TL^{-1}(a+3t_U)-a^TL^{-1}a}{3}
&=
t_U^TL^{-1}a+a^TL^{-1}t_U
+3t_U^TL^{-1}t_U.
\end{aligned}
$$


Thus, modulo $3$,


$$
\delta\left(\frac{a^TL^{-1}a}{3}\right)
=
t_U^TL^{-1}a+a^TL^{-1}t_U.
\tag{5.4}
$$



Since $B'=B+3c$, the terms $B^TRB$ and $B_{d+1}$ are unchanged modulo $3$, while


$$
\delta(B_d/3)=c_d.
\tag{5.5}
$$


The inverse-dependent scalar $V_{dd}/3$ is unchanged at this precision by Proposition 4.1.

Consequently,


$$
\boxed{
\delta K_{18}
=
t_U^TL^{-1}a+a^TL^{-1}t_U
-\kappa\operatorname{Sym}_\tau(c_d)
\pmod3.
}
\tag{5.6}
$$



### Polynomial form of the obstruction

Define, for each original residual index $i$,


$$
O_i=
U L^{-1}a_i
-\kappa\tau_i\bigl(Y_d-U L^{-1}X_d\bigr).
\tag{5.7}
$$


Here $X_d$ is the actual finite column of the core mixed block indexed by $Y_d$. Every term is a polynomial in the original space of degree at most $m$.

Expanding (5.6) gives the explicit entry formula


$$
\boxed{
(\delta K_{18})_{ij}
=
\mathcal M\!\left(P(F_jO_i+F_iO_j)\right)
\pmod3.
}
\tag{5.8}
$$



This is a proved identity in the unchanged finite objects.

### Exact order of the missing information

The layer $27P$ in $\mathscr R$ is the layer $81P$ in $R_{\rm prod}$. It changes the actual form only at order


$$
3^6\cdot81=3^{10}.
$$


Nevertheless it can enter the normalized next quadratic digit through the divisions


$$
a=T(\mathscr R)_U/9,\qquad B_d/3.
$$


Equations (5.4)–(5.8) show exactly how.

Thus earlier six-row support for $a\bmod3$, and the equality $B_d\bmod3=0$, do not themselves dispose of this layer. Its opposite-edge LOW contribution and its lower-edge HIGH feedback occur in the **same combined observation**.

---

## 6. Assessment of the proposed support mechanism

The candidate is not refuted by a known nonzero original-producer term. However, the supplied arguments do not prove it.

The precise unsupported step is the transfer


$$
\text{short producer terminal width}
\quad\Longrightarrow\quad
\text{short complete projected-column width}.
$$



A successful transfer must prove that the functional pairing in (5.8) vanishes for the higher producer layers actually permitted by factorial saturation and endpoint divisibility. It must do so after:

- monic LOW remainders;
- complete LOW feedback;
- finite HIGH inverse copies;
- lower truncation;
- the physical upper terminal $m$;
- all paid divisions.

Core orthogonality alone cannot supply this conclusion: $P F_j$ is not automatically $Q_c$ times an integral polynomial of degree at most $m$.

### Concrete follow-on lemma

A sharper next target is:

> **Higher-jet observed annihilation lemma.**  
> For every higher-layer polynomial $P$ arising from the actual producer after subtracting its retained lower jets and dividing by $27$, prove
> 

$$
> \mathcal M\!\left(P(F_jO_i+F_iO_j)\right)\equiv0\pmod3
>
$$


> for every $0\le i,j<\nu$, with $O_i$ given by (5.7).  
> Supply explicit finite support bounds for these products, or explicit coefficient cancellations at every surviving pole.

This lemma is narrower than a full corrected-column support theorem, but directly addresses the combined feedback. Its hypothesis must be verified for the actual producer, not for an unrestricted formal $P$.

Even its proof would only remove the specified higher layers; the remaining lower-jet contribution and $V_{c,dd}/3$ would still require evaluation.

---

## 7. Distinguished pair and primitive arithmetic

The endpoint and diagonal remain


$$
e_{\rm act}=Z(-1)^T-C_{\rm act}^TE_{\rm act}^{-1}w,
\qquad
d_{\rm act}=w^TE_{\rm act}^{-1}w,
\qquad w=W(-1)^T,
$$


with the genuine possible loss


$$
d_{\rm act}\in3^{-1}\mathbb Z_3.
$$



Under a justified depth-$18$ normalization,


$$
\Upsilon_{18}=-S_{\rm act}/3^{18},
$$


the full distinguished pair is


$$
\mathcal D_0=\det\Upsilon_{18},
$$




$$
\mathcal D_1=
e_{\rm act}^T\operatorname{adj}(\Upsilon_{18})e_{\rm act}
-3^{18}d_{\rm act}\det\Upsilon_{18}.
$$


Neither member is evaluated here.

The original complete construction retains both exponential boundary columns, logarithmic forcing, exterior constant, and terminal closure


$$
J^T\varepsilon+\omega
=
-\varepsilon-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
$$



After the actual contents, actual multiplier, and least simultaneous clearer,


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$




$$
g_\ell=\gcd(|A_\ell|,|B_\ell|)
$$


over **all primes**. For $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell}.
$$


The whole same-index error is


$$
\boxed{
q(e+\pi)-p=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}{g_\ell}
\det H_{\rm complete}.
}
$$



These are preserved exact definitions, not estimates of the actual contents, gcd, denominator, or error.

---

## 8. Computation and proof-status ledger

No new numerical calculation is necessary to verify Propositions 4.1 and formula (5.8); their proofs are algebraic.

No bounded small-producer interface is yet proved sufficient for evaluating $K_{18}$. Accordingly, this report requests neither a speculative original-dimension computation nor a rerun of a closed receipt.

A future finite check of the annihilation lemma would require, as bounded inputs:

- one explicitly specified original tuple $(j,h)$;
- the exact actual higher-layer polynomial $P$;
- the complete core blocks and columns on the original finite intervals.

Its verifiable output would be the complete matrix


$$
\left(
\mathcal M(P(F_jO_i+F_iO_j))\bmod3
\right)_{0\le i,j<\nu}.
$$


Such an output would establish only that tuple. No computation of this kind is commissioned here because no finite-to-infinite reduction has been proved.

| Item | Status |
|---|---|
| At most three charged inverse insertions at precision $3^{20}$ | Proved |
| Actual corrected-column support after each insertion | Open |
| Actual inverse replaceable by complete core inverse in $K_{18}$ | Newly proved |
| Higher-layer sensitivity formula (5.8) | Newly proved |
| Vanishing of that sensitivity for actual producer layers | Open |
| Combined feedback evaluation and full radical of $K_{18}$ | Open |
| Stronger depth-$18$ normalization | Conditional on reviewed bounds |
| Full endpoint/diagonal distinguished pair | Retained, unevaluated |
| Actual contents, least clearer, all-prime gcd, primitive denominator | Unevaluated |
| Whole nonzero error tending to zero at the same infinite original indices | Open |

## Conclusion

The finite charged-walk count survives audit. The proposed spatial invariant has not yet been established, and $315<D$ cannot substitute for it.

The new result is a separation of the outstanding problem: **producer-induced changes in the eliminated inverse do not affect the next digit, but higher producer-source layers can affect it through the explicit pairing (5.8).** Proving the vanishing of that pairing for the actual saturated layers is a concrete remaining support obligation.

Beyond this local bottleneck remain the distinguished-cofactor problem and the all-prime, whole-error argument on the same infinite original sequence.



$$
\boxed{\text{No unconditional proof of rationality or irrationality of }e+\pi
\text{ is obtained.}}
$$


