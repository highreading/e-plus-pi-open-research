> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

## Status

I reuse the completed sixth result on


$$
j>0,\qquad243\mid j,\qquad n=4^j+1,\qquad
H=3^{h-1},\qquad 0<D=H-(n-2)<H/8748.
$$


I do **not** obtain the requested uniform Schur-support induction, or an evaluated seventh saturation.

I do obtain a bounded precision improvement relevant to that induction: **the actual-polynomial remainder has one more digit of protection in the radical Schur form than the entrywise LOW-division estimate provides.** In particular, on the existing $243\mid j$ domain, the depth-seven polynomial remainder does not affect the radical Schur form modulo $3^7$. Thus increasing the divisibility of $j$ solely to remove that remainder at seventh precision is unnecessary.

This is a precision lemma for the actual form, not a claim that its remaining core contractions vanish.

## 1. Actual columns, form, and Schur normalization

Retain


$$
A=H-D,\qquad d=\frac{3D}{2}-1,\qquad
\nu=\frac D2-1,\qquad m=\frac{A+1}{2}.
$$


The columns are $1,y,\ldots,y^m$, with HIGH $d,\ldots,m$, LOW unit columns


$$
U=(1,\ldots,y^{D-1}),
$$


and radical columns


$$
Z=(z_i)_{0\le i<\nu},\qquad z_i=y^i(y-1)^D.
$$



The metric remains the complete rational functional


$$
\mathcal M(F)=
-\frac{3^h}{4}\mathfrak f(F)
+\sum_{r=0}^{h}
\sum_{\substack{c\ge1\ {\rm odd}\\3\nmid c\\c3^r\le4n-3}}
3^{h-r}c^{-1}
[y^{(c3^r-1)/2}]
\frac{F-F(-1)}{y+1},
\qquad
\mathfrak f(y^s)=(2s)!.
$$


Only the primitive unit $\lambda=L_n/3$ is stripped.

For the lemma, compare


$$
Q_c=(y+1)(y-1)^A(\beta+3y),\qquad
Q=Q_c+3^tT,\qquad T\in\mathbb Z_3[y],\quad\deg T\le n.
$$


The supplied actual polynomial has this form with $t\ge7$.

Write $\mathcal R_c,\mathcal R$ for the radical Schur forms after eliminating HIGH and $U$, **and dividing the original scale by $3$**. These are the normalization used in the sixth calculation.

## 2. New bounded lemma: radical protection of the polynomial error

### Statement

On the displayed domain, for $t\ge3$,


$$
\boxed{\mathcal R-\mathcal R_c\in
3^t\operatorname{Mat}_{\nu}(\mathbb Z_3).}
\tag{1}
$$


Here the comparison assumes the established unit-block structure and integral radical lifts, with their reductions equal to $Z\bmod3$; these hold for both forms on this domain because their block data agree at the necessary initial precisions.

In particular, for the actual $t\ge7$,


$$
\boxed{\mathcal R\equiv\mathcal R_c\pmod{3^7}.}
\tag{2}
$$



### Proof

Let $\Delta$ be the original-scale matrix perturbation,


$$
\Delta(f,g)=3^t\mathcal M(Tfg).
$$


The complete cutoff gives entrywise integrality of $\mathcal M$, hence


$$
\Delta(f,g)\in3^t\mathbb Z_3
$$


for integral actual columns.

Let $W_c$ be the exact core radical lift orthogonal to the eliminated columns. The established LOW-first formulas give


$$
W_c=Z+3N
$$


for an integral matrix of actual polynomial columns $N$. This uses the actual LOW projection: its $U$-correction is divisible by $3$, and its HIGH correction contains the explicit factor $3$.

It follows that


$$
W_c^T\Delta W_c
\equiv3^t\bigl(\mathcal M(Tz_i z_l)\bigr)_{i,l}
\pmod{3^{t+1}}.
\tag{3}
$$



We now evaluate the residue on the right, including endpoint subtraction. Modulo $3$, the functional has only its top pole:


$$
\mathcal M(F)\equiv
[y^{r_*}]\frac{F-F(-1)}{y+1}\pmod3,
\qquad r_*=\frac{3H-1}{2}.
\tag{4}
$$


Indeed $4n-3<9H=3^{h+1}$, so the top layer has only $c=1$; every lower pole has weight divisible by $3$, and the factorial term is divisible by $3^h$.

For every $0\le i,l<\nu$,


$$
\deg(Tz_i z_l)
\le n+2D+2\nu-2
=H+2D-2.
$$


Consequently


$$
\deg\frac{Tz_i z_l-T(-1)z_i(-1)z_l(-1)}{y+1}
\le H+2D-3<r_*.
\tag{5}
$$


The final inequality follows already from $H>4D-5$, far weaker than the assigned bound.

Equations (4)–(5) prove


$$
\mathcal M(Tz_i z_l)\equiv0\pmod3.
$$


Thus (3) is divisible by $3^{t+1}$.

It remains to check the change in the eliminating columns, rather than identifying the first variation with the full answer. In the core-orthogonal basis, the perturbed matrix has the block shape


$$
\begin{pmatrix}
A_c+\Delta_{AA}&\Delta_{AW}\\
\Delta_{WA}&3\mathcal R_c+\Delta_{WW}
\end{pmatrix}.
$$


The eliminated block consists, after integral congruence, of a HIGH unit block and $3$ times a LOW unit block. Therefore


$$
(A_c+\Delta_{AA})^{-1}\in
3^{-1}\operatorname{Mat}(\mathbb Z_3).
$$


The exact additional Schur correction is


$$
-\Delta_{WA}(A_c+\Delta_{AA})^{-1}\Delta_{AW}.
$$


Its valuation is at least $2t-1$. After the radical normalization by $3$, its valuation is at least $2t-2\ge t$.

The linear perturbation has valuation at least $t+1$ before that division, by (3)–(5). Both contributions therefore lie in $3^t$ afterwards, proving (1). ∎

This argument retains the original finite column space throughout. It introduces neither unbounded HIGH convolutions nor geometric replacement columns.

## 3. What this settles—and what it does not

The seventh-precision calculation can use the core polynomial on the existing $243\mid j$ domain without an unidentified contribution from its depth-seven remainder. The factorial force can likewise be removed at that precision only after its stated bound is applied: here $H>8748D$, $D\ge6$, implies $h-1\ge10$, so the first LOW division leaves ample factorial precision.

The unresolved part is therefore the **core Schur contraction**, not the actual-polynomial error.

I have not proved that the proposed support modules are closed under repeated application of the actual


$$
F=(E-E_0)/3-X_U^TL_U^{-1}X_U.
$$


In particular, the known calculations for $X_Up_i$ do not establish a uniform assertion for all integer-grid polynomials produced by subsequent inverse bands and finite HIGH truncation. One must prove that each such polynomial either:

* remains a complete $(y-1)^D$-multiple with a quantified support margin, or
* has a boundary remainder whose LOW projection and coefficient valuation are explicitly controlled.

Without that statement, another use of $F$ is not justified merely by the parity of its unprojected coefficient support.

This is a precise missing closure assertion, **not an exhibited nonzero offending band**. I therefore do not claim that the all-depth mechanism fails, and I have not fulfilled the alternative task of evaluating a first failing depth. No $C_r$ for new saturation depths is established here.

## 4. Endpoint and primitive arithmetic retained

The perturbation changes the transported radical columns by a vector divisible by $3^{t-1}$. Their endpoint residue is therefore unchanged:


$$
W(-1)\equiv W_c(-1)\equiv
\bigl((-1)^i\bigr)_{0\le i<\nu}\ne0\pmod3.
$$


This preserves the known endpoint residue; it does not identify its image under an unevaluated higher divided form.

Restoring $\lambda$ preserves (1)–(2). For the actual integer pair, retain


$$
g=\gcd(|A_{\rm det}|,|B_{\rm det}|).
$$


When $B_{\rm det}\ne0$,


$$
q=\frac{|B_{\rm det}|}{g},\qquad
p=-\frac{\operatorname{sgn}(B_{\rm det})A_{\rm det}}g,
$$


and


$$
q(e+\pi)-p
=\frac{\operatorname{sgn}(B_{\rm det})\ell^{(n+1)/2}}g
\det H_{\rm complete}.
$$


The primitive multiplier is $\ell^{(n+1)/2}/g$, not merely the clearer.

The required relative arithmetic quantity remains


$$
v_3(q)=\max\!\left\{0,\,
h+2v_3((n-1)!)-1+
v_3(\operatorname{adj}(S_{\rm LOW})_{\rm endpoint})
-v_3(\det S_{\rm LOW})\right\},
$$


where the terms and inherited normalization identity are defined. No new estimate of this difference, response nonvanishing, or whole-error nonvanishing follows from the precision lemma.

### Closing ledger

1. **New result and proof status.** Proved: the actual-polynomial remainder changes the normalized radical Schur form only at depth $t$, rather than the entrywise bound $t-1$. Thus the depth-seven remainder is absent modulo $3^7$ on the existing domain. The requested uniform saturation theorem remains unproved.

2. **Exact remaining bottleneck.** Quantified closure under the actual LOW-projected $F$, including truncated HIGH boundary remainders, is missing. Neither a first offending band nor the seventh radical form has been evaluated. Actual relative cofactor/determinant control and nonzero whole primitive errors tending to zero remain necessary for irrationality.

3. **Computation request.** None. The new precision result is symbolic; a finite rank scan would not settle the missing uniform closure assertion.
