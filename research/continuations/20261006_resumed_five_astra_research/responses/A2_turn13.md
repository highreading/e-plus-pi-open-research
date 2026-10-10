> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2, Turn 13 — Audit of the $\Xi$ lift, and a finite exterior-forcing lemma for the complete mixed contraction

## Executive assessment

The $\Xi$ specification survives the audit, subject to the finite-normal-form hypotheses already stated in Turn 12. In particular:

1. The ratios in Turn 12, (18.1), are **absolute stripped unit ratios**. They must not be normalized by dividing by their values at $q=0$.
2. The $220/242$ upper paths have low valuation exactly two and the two stated interface prefactors.
3. The $231$ paths are exactly the **low three-digit valuation-one paths** of $V(q)$. They are not merely the $42$ digit-one transitions, and they are not, for arbitrary $t$, the complete set of full-index atoms of valuation exactly one.
4. The first-order dependence on the high factorial arguments does cancel in the whole $\gamma$ numerator. This requires a more explicit argument than “first-order reflection”: the high-dependent logarithmic correction is constant under the first-digit reflection, separately for each bridge type and each fixed middle transition.
5. The endpoint does not leave an extra derivative term. Every one of the $231$ low indices lies between $2076$ and $2774$, hence below $C\bmod29^3=20916$. All of them have exactly the same remaining finite range $0\le r\le t$.

I do **not** evaluate or predict $\Xi$. No accepted $42$-term, $135918$-atom, or original ordinary-tail calculation is requested again.

For the mixed problem, I obtain two concrete advances:

* an explicit four-scalar description of the actual first head at the precision relevant to $F\bmod29$;
* a finite exterior-response formula which would put the complete exponential second column in the **same consolidated $2n$-atom class** as the first column.

The second advance identifies a source-specific identity that must be proved before it can be applied to the actual complete second force. It cannot be inferred from the two initial charges alone. Under that explicitly stated identity, the ordinary annihilating tail does kill the complete mixed contraction through


$$
F^TQ\equiv0\pmod{29^3}
\quad\text{on }u\equiv2\pmod{29^9}.
$$


This includes the first two normalized mixed layers and their complete finite returns. It is not yet the required norm-relative mixed congruence.

Thus this report completes the requested $\Xi$-specification audit, but **does not claim completion of the assigned actual leading paid mixed evaluation**. The precise missing force identity and the next bounded coefficient certificate are given below. No actual low-prefix obstruction has been evaluated.

---

## 1. Preserved objects and accepted scope

Write


$$
p=29,\qquad D=p^3,\qquad
b=3^{249005515+574312172u}
   =410910916+p^6C,
$$




$$
n=2001b,\qquad u\ge0.
$$



The domains remain


$$
0\le j<b
$$


for contact coordinates,


$$
1\le i\le b-2
$$


for recurrence source rows, and


$$
0\le j\le b
$$


for reconstructed coordinates.

The actual columns are


$$
Z_w=\mathcal RA^{-1}f^0,\qquad
Y=\mathcal RA^{-1}\mathbf r+W_be_b,\qquad
W_j=\binom{n+2}{j},
$$


with


$$
(\mathcal Rx)_j=W_j(jx_{j-1}-x_j),\qquad x_{-1}=x_b=0.
$$


In particular,


$$
(\mathcal Rx)_b=bW_bx_{b-1}.
$$



Retain


$$
P=\frac{Z_w}{p^2}=p^cx,\qquad
Q=\frac{Y}{p^3},\qquad
F=\frac{Z_w}{p^4},
$$


and


$$
d=v_p(Z_w^TZ_w)=2c+4+\nu,\qquad
\nu=v_p(x^Tx).
$$



I reuse the independently accepted conclusion


$$
u\equiv2\pmod{p^3}
\quad\Longrightarrow\quad
Z_w\in p^4\mathbb Z_p^{b+1},\qquad d\ge9.
$$



The Turn 12 factorization and its $d\ge10$ consequence remain subject to their stated complete-column and finite-cutoff hypotheses. The audit below finds no additional defect in the $\Xi$ lift.

No exact $c$, primitive norm digit, or primitive mixed digit follows from these lower bounds.

---

# Part I. Independent audit of the $\Xi$ specification

## 2. Exact stripping: valuation and unit must remain separate

For


$$
F_p(N)=\prod_{\substack{1\le r\le N\\p\nmid r}}r,
\qquad
\mathcal P_m(N)=\prod_{i=0}^{m-1}
F_p\!\left(\left\lfloor N/p^i\right\rfloor\right),
$$


the exact identity is


$$
N!
=
p^{\sum_{i=1}^{m}\lfloor N/p^i\rfloor}
\left\lfloor N/p^m\right\rfloor!\,
\mathcal P_m(N).
\tag{2.1}
$$



For a product of the two positive binomials, with outgoing weight borrow, lower-index borrow, and addition carry $w,k,c$, this gives


$$
\text{atom}
=
p^{e_{\rm low}}L(J)H_{wkc}(J),
\tag{2.2}
$$


where $L(J)$ is a unit and


$$
H_{wkc}(J)=
(W-J)^w(A+B-J-k+1)^c
\binom WJ
\binom{A+B-J-k}{B-J-k}.
\tag{2.3}
$$



The three points important for the present audit are:

* $e_{\rm low}$ is the sum of the low outgoing weight borrows and addition carries;
* the factors in front of the upper binomials in (2.3) are indispensable;
* $L(J)$ is the absolute ratio of the stripped factorial products.

There is no extra Wilson sign to append to the ratios in Turn 12, (18.1): those signs are already in $\mathcal P_3$. Squaring removes their leading sign, but not their first-order unit contribution.

### Absolute-ratio warning

The calculation must use


$$
L_r(q)
$$


as displayed in Turn 12. Replacing it by


$$
L_r(q)/L_r(0)
$$


would destroy the branch weights and would not compute either $\alpha_\varepsilon$ or $\beta_\varepsilon$.

---

## 3. Why the first-order lift has only the stated high dependence

For $0\le r<p$,


$$
F_p(pq+r)
\equiv
((p-1)!)^q r!
\left(1+pq\,\mathsf H_r\right)
\pmod{p^2},
\tag{3.1}
$$


where


$$
\mathsf H_r=\sum_{a=1}^r a^{-1}\pmod p,\qquad
\mathsf H_0=\mathsf H_{p-1}=0.
$$



In a balanced factorial ratio, the exponents of $(p-1)!$ are fixed by the low carry data. They are not additional variable functions of the unread high index.

At a cut $p^3$, changing an upper quotient affects the factors at levels $0$ and $1$ only by multiples that are invisible modulo $p^2$. The nonconstant first-order dependence therefore comes from the last low digit.

This proves, for each fixed low path,


$$
L(J)\equiv L(0)+pJ L^{[1]}\pmod{p^2}.
\tag{3.2}
$$



This is a statement about the **low unit ratio**. It does not assert that the upper binomial factor has no lift. That distinction is essential in the $\gamma$ audit.

---

## 4. The $220/242$ paths and their prefactors

The upper parameters are


$$
W=7663+DX,\qquad
B=16848+DC,\qquad
A=15327+2DX.
$$



The low minimal indices are


$$
r=j_0+p^2j_2,
$$


with


$$
j_0\in\{0,\ldots,7\}\cup\{15,\ldots,28\}.
$$


There are $22$ choices of $j_0$.

The two branches are:

| Branch | $j_2$ | Count | Outgoing interface | Exact upper factor |
|---|---:|---:|---|---|
| I | $0,\ldots,9$ | $22\cdot10=220$ | $(0,0,1)$ | $(2X+C+1-q)V(q)$ |
| II | $10,\ldots,20$ | $22\cdot11=242$ | $(1,0,0)$ | $(X-q)V(q)$ |

Thus the interface prefactors in Turn 12 are correct:


$$
F_{\rm I}(q)=(2X+C+1-q)V(q),\qquad
F_{\rm II}(q)=(X-q)V(q).
\tag{4.1}
$$



Each path has low valuation exactly two.

All $462$ low indices satisfy


$$
r\le16848=B\bmod D.
$$


Hence the upper range is exactly


$$
0\le q\le C
$$


for every path. No branch has a shortened final $q$-range.

### A useful additional checksum

At the last low digit put $d=j_2$. In both branches, the resulting weight-remainder and addition-result digits coincide. Therefore the logarithmic slope in $q$ is


$$
\mathsf H_{20-d}-\mathsf H_d.
\tag{4.2}
$$



The leading squared unit at this digit is symmetric under


$$
d\longleftrightarrow20-d.
$$


The middle point $d=10$ has zero slope. Consequently the specification also implies


$$
\boxed{\beta_{\rm I}+\beta_{\rm II}=0\pmod p.}
\tag{4.3}
$$



This is an audit identity, not a numerical evaluation of either $\beta$, and not a prediction of $\Xi$.

---

## 5. The $231$ paths are the complete low valuation-one support

At


$$
C=20916+Dt,\qquad
X=2774+D(1716+2001t),
$$


the low triples for $X,2X,C$ are


$$
(19,8,3),\qquad (9,17,6),\qquad (7,25,24).
$$



The first digit is event-free and satisfies


$$
d_0+k_0=7+29\varepsilon,\qquad
0\le d_0,k_0\le19.
$$



The first-digit counts are:

* $\varepsilon=0$: $d_0=0,\ldots,7$, giving $8$ paths;
* $\varepsilon=1$: $d_0=17,18,19$, giving $3$ paths.

For each of these $11$ choices, the middle digit has:

* $9$ type-A possibilities;
* $12$ type-B possibilities.

The last digit is then uniquely determined. Therefore


$$
\boxed{11(9+12)=231.}
\tag{5.1}
$$



By contrast, the accepted $42$ terms are


$$
2(9+12)=42
$$


middle-digit transition weights, before multiplication by the first-digit branch weights.

These are different collections and must not be interchanged.

### Full valuation versus low valuation

For arbitrary $t$, a $231$-path low residue can be followed by a high atom with further valuation. Thus “$231$ valuation-one paths” means:

> exactly $231$ low three-digit paths with one event and zero outgoing interface.

It does not mean that the complete sum has exactly $231$ atoms of total valuation one for every $t$.

This wording correction matters at the lifted precision.

---

## 6. The endpoint is common to all $231$ paths

For type A,


$$
q_s=d_0+pd_1+p^2\cdot3.
$$


For type B,


$$
q_s=d_0+pd_1+p^2\cdot2.
$$



The ranges give


$$
\boxed{2076\le q_s\le2774<20916.}
\tag{6.1}
$$



All three outgoing interfaces are zero. Therefore


$$
q=q_s+Dr
$$


has exactly the remaining range


$$
0\le r\le t.
\tag{6.2}
$$



The high factor is exactly


$$
V_{\rm tail}(r)=
\binom{1716+2001t}{r}
\binom{3432+4002t+t-r}{t-r}.
\tag{6.3}
$$



There is no $t-1$ branch, no extra $t+1$ endpoint, and no unfinished terminal carry.

---

## 7. Full audit of the derivative-tail cancellation in $\gamma$

Let


$$
a=1716+2001t.
$$


For a surviving path, write its last low digits as


$$
d_2=
\begin{cases}
3&\text{type A},\\
2&\text{type B},
\end{cases}
\qquad
k_2=
\begin{cases}
21&\text{type A},\\
22&\text{type B}.
\end{cases}
$$


The other last digits are


$$
X_2=3,\quad (X-q)_2=0,\quad (2X)_2=6,\quad
(2X+C-q)_2=28.
$$



Using (3.1), the part of the first-order logarithmic correction that depends on the high variables is


$$
a(\mathsf H_3-2\mathsf H_6)
-t\mathsf H_{k_2}
+r(\mathsf H_{k_2}-\mathsf H_{d_2}).
\tag{7.1}
$$



The terms with $\mathsf H_0$ and $\mathsf H_{28}$ vanish.

Crucially, (7.1) depends on the bridge type, but not on which of $d_0,k_0$ is designated the first digit. It is unchanged by


$$
d_0\longleftrightarrow k_0
$$


for each fixed middle transition.

Now


$$
\Delta(q)=(X+C+1)(3X+C+1-2q)
$$


satisfies


$$
\Delta(q)\equiv15+4d_0
=4(d_0-7/2)\pmod p.
\tag{7.2}
$$


The leading squared low weight is symmetric in $d_0,k_0$, while


$$
d_0+k_0\equiv7\pmod p.
$$



It follows that the contraction against (7.2) vanishes separately for:

* each cutoff branch $\varepsilon$;
* each bridge type;
* each fixed middle transition.

Therefore the contraction kills all of:

1. the leading low coefficient;
2. the first-order $a$-dependence;
3. the first-order $t$-dependence;
4. the first-order $r$-dependence.

This accounts for all high dependence in the low unit ratio modulo $p^2$.

### What happens to the high factorial-unit lift?

It is not omitted. The exact common high factor is still $V_{\rm tail}(r)^2$. After the low contraction, its coefficient is $p\gamma\pmod{p^2}$. Consequently


$$
p\gamma\,V_{\rm tail}(r)^2\pmod{p^2}
$$


needs only the ordinary reduction of that whole high factor modulo $p$.

Thus a first-order lift of the high factorial units is multiplied by $p^2$ and disappears at this precision. This is the missing explicit justification behind the informal phrase “no derivative tail remains.”

We obtain


$$
\boxed{
\mathcal B(C)\equiv
p\gamma\sum_{r=0}^{t}V_{\rm tail}(r)^2
\pmod{p^2}.
}
\tag{7.3}
$$



---

## 8. Audited specification for the coordinator’s new calculation

The numerical specification in Turn 12 need not be replaced. It should be supplemented by the following explicit requirements.

### 8.1 Upper constants

Use the absolute ratios


$$
L_r(q)=
\frac{\mathcal P_3(W_*)}
{\mathcal P_3(r+Dq)\mathcal P_3(W_*-r-Dq)}
\frac{\mathcal P_3(A_*+B_*-r-Dq)}
{\mathcal P_3(A_*)\mathcal P_3(B_*-r-Dq)}
\pmod{p^2},
$$


with


$$
W_*=7663+19D,\quad
B_*=16848+7D,\quad
A_*=15327+38D.
$$



Then


$$
\alpha_\varepsilon=\sum_{r\in\varepsilon}L_r(0)^2\pmod{p^2},
$$




$$
\beta_\varepsilon=
2\sum_{r\in\varepsilon}
L_r(0)\frac{L_r(1)-L_r(0)}p\pmod p.
$$



The required checks include


$$
220,\quad242,\qquad
\alpha_{\rm I}\equiv4,\quad
\alpha_{\rm II}\equiv25\pmod p,
$$


the divisibility of every displayed difference, and optionally (4.3).

### 8.2 The whole $\gamma$ numerator

Use all $231$ low paths and


$$
C_*=20916,\qquad X_*=41854298.
$$


With their absolute stripped units $L_s$, accumulate


$$
S_\gamma=
\sum_s
(X_*+C_*+1)(3X_*+C_*+1-2q_s)L_s^2
\pmod{p^2}.
\tag{8.1}
$$



Only after this whole sum has been accumulated is the division made:


$$
\gamma=S_\gamma/p\pmod p.
\tag{8.2}
$$



Individual summands need not be divisible by $p$. A termwise division would be invalid.

Finally,


$$
\Xi=
4\gamma+
13\frac{\alpha_{\rm I}+\alpha_{\rm II}}p+
11\beta_{\rm I}+22\beta_{\rm II}\pmod p.
\tag{8.3}
$$



All divisions in this specification are now explicitly justified. No value of (8.3) is asserted here.

---

# Part II. Making the actual first-head dependence smaller

## 9. Four actual high scalars suffice for the first normalized head layer

This is a useful reduction for a future actual mixed calculation. It avoids treating the $58$ relevant head entries as unrelated unknowns.

Put


$$
\mathscr P(z)=1+2z+2z^2,\qquad m=n/p.
$$


On the original family,


$$
m\equiv7\pmod p.
$$



Define the exact integer polynomial


$$
E(z)=\frac{\mathscr P(z)^p-\mathscr P(z^p)}p.
\tag{9.1}
$$


Write $e_k=[z^k]E(z)$.

Define four actual coefficient scalars:


$$
A_m=[z^m]\mathscr P(z)^m,
$$




$$
B_m=[z^{m-1}]\mathscr P(z)^{m-1},\qquad
C_m=[z^{m-2}]\mathscr P(z)^{m-1},
$$




$$
D_m=[z^{m-1}]\mathscr P(z)^m.
\tag{9.2}
$$



For $0\le i<p$, put


$$
u_i=\sum_{a=0}^{i}\binom ia e_{p-a},\qquad
v_i=\sum_{a=0}^{i}\binom ia e_{2p-a}.
\tag{9.3}
$$



The exact expansion


$$
\mathscr P(z)^{pm}
\equiv
\mathscr P(z^p)^m+
pmE(z)\mathscr P(z^p)^{m-1}
\pmod{p^2}
$$


gives


$$
J_i\equiv
A_m+pm(u_iB_m+v_iC_m)
\pmod{p^2}
\qquad(0\le i<p).
\tag{9.4}
$$



Also,


$$
\frac{(n+i)!}{n!}
\equiv i!(1+n\mathsf H_i)\pmod{p^2}.
$$


Hence


$$
\boxed{
f_i^0\equiv
i!A_m+
pm\,i!\bigl(\mathsf H_iA_m+u_iB_m+v_iC_m\bigr)
\pmod{p^2}
}
\tag{9.5}
$$


for $0\le i<p$.

For $i=p+v$, $0\le v<p$,


$$
J_{p+v}\equiv A_m+D_m\pmod p,
$$


and


$$
\frac1p\frac{(n+p+v)!}{n!}
\equiv-(m+1)v!\pmod p.
$$


Thus


$$
\boxed{
f_{p+v}^0\equiv
-p(m+1)v!(A_m+D_m)\pmod{p^2}.
}
\tag{9.6}
$$



Finally,


$$
f_i^0\equiv0\pmod{p^2}\qquad(i\ge2p).
\tag{9.7}
$$



### Consequence

At the precision determining $F\bmod p$, the actual low first-column profile is a linear combination of **four fixed bounded head profiles**, with coefficients


$$
A_m,\ B_m,\ C_m,\ D_m\pmod p.
$$



The $p$-digit of $A_m$ multiplies the short unit head and is one physical order too deep to change $F\bmod p$, by the accepted complete saturation argument.

This does not evaluate the four actual scalars. It does replace an unspecified actual head table by four explicit original coefficient observables.

It is not a primitive-content theorem.

---

# Part III. A concrete exterior-response reduction for the second force

## 10. An exact full-row factorization

Let


$$
(T_n)_{ij}=\binom n{j-i},\qquad
(R_n)_{ij}=\binom{-n}{j-i}
$$


on nonnegative indices, with negative lower indices zero.

Let


$$
(D_+)_{ij}=a_{i-j}(n)\frac{i!}{j!},
\qquad
(D_-)_{ij}=c_{i-j}(n)\binom ij.
$$


These are inverse lower-triangular symbol matrices.

For the extended contact matrix, allowing every nonnegative column index $j$, one has


$$
\boxed{\mathsf P_-A_{\rm ext}=T_nD_+T_n.}
\tag{10.1}
$$



A direct proof uses the row generating polynomial. With $y=1+x$,


$$
\sum_j A_{ij}x^j
=
y^n\phi(\partial_y)^n y^{n+i}.
$$


Taking the finite difference in $i$ gives


$$
y^n\phi(\partial_x)^n\bigl(x^k(1+x)^n\bigr),
$$


which is precisely row $k$ of $T_nD_+T_n$.

Its full inverse is


$$
\mathcal C_\infty=R_nD_-R_n.
\tag{10.2}
$$



At every fixed $p$-adic precision, this is well-defined by symbol truncation. It is not an unrestricted replacement of the finite inverse.

---

## 11. Explicit exterior-to-interior atoms

The entries of (10.2) have the finite-precision formula


$$
\boxed{
(\mathcal C_\infty)_{jk}
\equiv
\sum_{s=0}^{pK-1}c_s(n)
\sum_{a=0}^{s}
\binom j{s-a}\binom{-n}{a}
\binom{-2n-a}{k+s-a-j}
\pmod{p^K}.
}
\tag{11.1}
$$



This follows from Vandermonde after expanding


$$
\binom{j+t}s=\sum_{a=0}^s\binom j{s-a}\binom ta.
$$



The importance of (11.1) is that it contains only consolidated $2n$-atoms. There are no residual $n$-atoms in this **full exterior-response kernel**.

Split the indices into


$$
I=\{0,\ldots,b-1\},\qquad E=\{b,b+1,\ldots\}.
$$



For a finitely supported exterior vector $z$, solve


$$
(\mathcal C_\infty)_{EE}v=z.
\tag{11.2}
$$


Then


$$
\boxed{
\theta=-\,(\mathcal C_\infty)_{IE}v
}
\tag{11.3}
$$


is the actual finite solution of


$$
A_{II}\theta=A_{IE}z.
\tag{11.4}
$$



Indeed, the full vector $\mathcal C_\infty(0,v)$ has exterior part $z$, and applying the full operator gives zero on the interior. This proves (11.4), including the finite boundary.

Equation (11.3) is therefore a finite-boundary identity, not an infinite-inverse substitution.

---

## 12. The exponential exterior vector is short at fixed precision

The exponential part suggested by the complete initial formulas has exterior entries


$$
z_h=\frac{(b+h)!}{b!},\qquad h\ge0.
\tag{12.1}
$$



Because


$$
v_p(z_h)\ge\lfloor h/p\rfloor,
$$


it is enough modulo $p^K$ to retain


$$
0\le h\le pK-1.
$$



Moreover,


$$
c_s(n)\in p\mathbb Z_p\qquad(s\ge1).
$$


For $s<p$, this follows from Frobenius applied to $\phi(z)^{-n}$; for $s\ge p$, it follows from the factorial in $c_s$.

A term of coefficient valuation $v\ge1$ can have lower displacement at most


$$
s\le(2p-1)v=57v.
$$


A Neumann solve of (11.2) therefore needs exterior indices only through


$$
\boxed{H_K=pK-1+57(K-1)=86K-58.}
\tag{12.2}
$$



At $K=6$,


$$
H_6=458,\qquad s\le173.
$$


After reconstruction, all resulting atoms have


$$
0\le a\le173,\qquad 0\le v\le632,
\tag{12.3}
$$


and row-binomial indices at most $174<841$.

These bounds preserve all the physical digit triples used in the Turn 12 uniform $p^3$-atom bound. They also satisfy the required row-factor periodicity modulo $p^2$.

This is a small, explicit alternative to carrying the uncombined $\sigma=0,1,2$ particular-source atoms.

---

## 13. The source-specific identity that is still required

Here is the crucial limitation.

Turn 0 explicitly gives the factorial/logarithmic formula for the two initial values $r_0,r_1$, and it gives the complete recurrence source $\mathcal H_i$. The displayed packet does not separately prove that the same factorial expression, extended to every row, equals the recurrence-defined $\mathbf r$.

Define the proposed full exponential row vector


$$
\widehat r_i^{(e)}
=
\sum_{h\ge0}\frac{(b+h)!}{b!}\,
A_{{\rm ext},\,i,b+h},
\qquad 0\le i<b.
\tag{13.1}
$$


The sum is finite for each row. It agrees with the exponential parts of the two supplied initial charges, because


$$
\sum_{j=b}^{m}\frac{j!}{b!}\binom mj
=
\frac1{b!}\sum_{j=b}^{m}(m)_{\underline j}
=T_m.
$$



But agreement at $i=0,1$ alone does not prove agreement at all rows.

The missing identity is:

> **Complete exterior-forcing identity $\mathbf{EF}_K$.**  
> Modulo $p^K$, the vector (13.1), together with the retained logarithmic row contribution, satisfies the exact same finite recurrence as $\mathbf r$, with
> 

$$
> \mathcal D\widehat{\mathbf r}=\mathcal H
> \quad\text{on every row }1,\ldots,b-2,
>
$$


> and with the two actual initial charges.

Equivalently, after the logarithmic contribution has been legitimately protected,


$$
\boxed{
\mathbf r\equiv A_{IE}z\pmod{p^K}
}
\tag{13.2}
$$


must be proved as a complete vector identity.

This is not a cosmetic hypothesis. If the source residual


$$
\mathcal E_i=\mathcal H_i-(\mathcal D\widehat{\mathbf r})_i
$$


is nonzero, then the actual solution contains


$$
A^{-1}\sum_{i=1}^{b-2}\mathcal E_i g^{(i)}.
$$


That residual can contain precisely the different upper kernels that the squared-kernel radical does not annihilate.

I do not delete it.

---

## 14. Logarithmic protection at the fixed layer

For the fixed precision used here, the logarithmic contribution has a direct valuation bound independent of an unknown exact $d$.

From


$$
L_m/m!=2\sum_{h=1}^{m}\frac{u_{h-1}}h
$$


and $u_r\in\mathbb Z[1/2]$,


$$
v_p(L_m)\ge v_p(m!)-\lfloor\log_p m\rfloor.
$$



Consequently the displayed row expression has logarithmic valuation at least


$$
N_{\log}
=
2v_p(n!)-v_p(b!)
-\lfloor\log_p(2n+b-1)\rfloor.
\tag{14.1}
$$



For these original indices this is far larger than $6$. Thus logarithmic omission in a **proved full-row identity modulo $p^6$** would be paid.

This does not establish the required norm-relative protection


$$
N_{\log}\ge d-c.
$$


That budget remains unchanged and must still be verified at the actual final depth.

---

# Part IV. What the exterior-forcing lemma would prove for the mixed observable

## 15. Conditional complete second-column saturation

Assume $\mathbf{EF}_6$.

Modulo $p$, the exterior vector (12.1) is


$$
z_0=1,\qquad z_1=-1,\qquad z_h=0\quad(h\ge2),
$$


because $b\equiv27\pmod p$.

Also


$$
(\mathcal C_\infty)_{EE}\equiv R_{2n}\pmod p,
$$


so its inverse is $T_{2n}$. Since $p\mid2n$, the unit coefficient sector of $v$ is again


$$
v_0=1,\qquad v_1=-1.
$$



Thus the unit-order contact sector is


$$
-\binom{-2n}{b-j}
+\binom{-2n}{b+1-j}.
$$


Its reconstructed interior sector is


$$
W_j\left[
\binom{-2n}{b-j}
-(j+1)\binom{-2n}{b+1-j}
+j\binom{-2n}{b+2-j}
\right].
\tag{15.1}
$$



Every positive-order coefficient receives the uniform three physical events and hence contributes to $p^4Y$-content.

For the first two terms of (15.1), the low residues


$$
(n+2)\bmod p^2=205,\quad
(2n-1)\bmod p^2=405,
$$




$$
b\bmod p^2=839,\quad
(b+1)\bmod p^2=840
$$


force a low event.

For the last term, if digit zero had no weight-borrow or addition-carry event, the lower digit for $b+2-j$ would have to be zero, forcing


$$
j\equiv0\pmod p.
$$


Its row factor $j$ then supplies the missing $p$.

The actual endpoint is


$$
Y_b=W_b(b\psi_{b-1}+1)\in p^6\mathbb Z_p.
$$



Therefore:

### Proposition 15.1 — Conditional complete second-column saturation
Under $\mathbf{EF}_6$,


$$
\boxed{
u\equiv2\pmod{p^3}\Longrightarrow Y\in p^4\mathbb Z_p^{b+1}.
}
\tag{15.2}
$$



This is a column-content argument, not an isotropy argument.

---

## 16. The first two normalized mixed corrections

Under the same hypothesis put


$$
G=Y/p^4,\qquad Q=pG.
$$



The zero-interface argument used for $F$ now applies to $G$: every term entering $G\bmod p$ has coefficient order plus low-event count exactly one and exits the low block with interface $000$.

At the next order the complete $G$-column has the same eight-interface form as Turn 12, (8.1), with its own complete low coefficients. Its finite shift box is (12.3), not an assumed reuse of the first-column box.

Consequently the cross-interface radical applies to the **bilinear** pairing as well. If


$$
a_\ell=F\text{'s complete low coefficient},\qquad
g_\ell=G\text{'s complete low coefficient},
$$


define


$$
\mathscr L_{FG}=\sum_{\ell=0}^{D-1}a_\ell g_\ell\pmod p.
$$



Polarizing the complete calculation—not merely the leading atom square—gives


$$
\boxed{
F^TG\equiv
\left(\sum_\ell\widetilde a_\ell\widetilde g_\ell\right)
\sum_{J=0}^{B}K(J)^2
\pmod{p^2}.
}
\tag{16.1}
$$



Here:

* all first-order corrections in both columns are retained;
* their cross-interface contractions vanish by the proved radical;
* the differing interior cutoffs are completed only because $K(B)^2\in p^2\mathbb Z_p$;
* the two actual terminal coordinates are separately zero at this precision.

It follows that


$$
F^TQ=pF^TG\in p^2\mathbb Z_p,
$$


and the first possibly nonzero normalized correction is


$$
\boxed{
\frac{F^TQ}{p^2}
=
\mathscr L_{FG}\,\Xi\,\mathcal H(t)\pmod p.
}
\tag{16.2}
$$



Thus the ordinary tail would annihilate the complete mixed contraction at this layer:


$$
\boxed{
\mathbf{EF}_6,\quad u\equiv2\pmod{p^9}
\Longrightarrow F^TQ\in p^3\mathbb Z_p.
}
\tag{16.3}
$$



This conclusion does not require evaluating $\mathscr L_{FG}$, because the accepted original tail row is zero for every continuation.

### Scope

Equation (16.2) is a small ordinary-tail functional, but its application to the actual second force remains conditional on $\mathbf{EF}_6$.

It is not an unconditional evaluation of the requested complete mixed observable. Nor does it evaluate the first surviving paid correction after (16.3).

---

## 17. Why this still does not settle the mixed target

The exact target is


$$
F^TQ-p^2\rho_nF^TF
\equiv0\pmod{p^{d-5}}.
\tag{17.1}
$$



On the reviewed $d\ge10$ cylinder, the modulus is at least $p^5$.

Even if (16.3) is established for the actual force, it gives only


$$
F^TQ\in p^3.
$$


The norm term satisfies


$$
p^2F^TF\in p^4
$$


when $d\ge10$.

Therefore two genuinely new questions remain:

1. Does the complete paid mixed coefficient at order $p^3$ vanish?
2. At the following order, does it align with the independently defined $\rho_n$ times the complete norm?

The ordinary six-digit annihilator does not answer these questions. At that precision, one must retain further valuation support, higher unit corrections, row-factor lifts, and the complete finite source response.

A nonzero row in a larger paid transport would also not, by itself, prove a nonzero actual final value. An obstruction must include the actual terminal acceptance, or a proof of nonvanishing for every admissible continuation.

No such obstruction is asserted here.

---

# Part V. Exact remaining certificate and arithmetic scope

## 18. The next source-specific lemma is finite and concrete

The most economical next lemma is not an arbitrary adjoint calculation:

> **Finite complete exterior-forcing lemma.**  
> Prove $\mathbf{EF}_6$ by comparing the exact Turn 0 source decomposition with the exterior vector (13.1), retaining:
> * both exponential initial charges;
> * every source row $1,\ldots,b-2$;
> * the explicit indicator-removal head $\eta$;
> * the actual endpoint solve;
> * the separate reconstructed exterior at $b$.

There are two acceptable proof routes.

### Route A: recurrence identity

Derive directly


$$
\mathcal D\widehat{\mathbf r}=\mathcal H
$$


on every source row, with the actual recurrence coefficients. Together with the two matching initial values, this proves the full vector identity.

### Route B: finite atom certificate

Use Turn 0’s exact finite identities to expand both sides modulo $p^6$, including the head correction. A zero coefficient array in a common atom list is a sufficient certificate of equality.

Because the atom list is redundant, a nonzero coefficient array is not by itself a disproof. Any claimed failure must be converted into a nonzero evaluated residual or an independent exact identity.

### Required inputs

The new certificate needs:

1. the actual recurrence coefficients, or the accepted $q_d(j)$ and homogeneous-head data;
2. the Turn 0 source polynomial coefficients;
3. $K=6$, with $M=173$ and the actual finite memory;
4. the exterior vector $z_h=(b+h)!/b!$, truncated at $h=173$;
5. the bounded exterior solve through $h=458$;
6. the original low parameter residues, with paid small-binomial guards.

### Expected verifiable output

Either:

* a symbolic recurrence identity plus the two initial-value checks; or
* a complete zero finite-atom difference certificate, with the head correction and terminal terms separately displayed.

No accepted bounded producer needs to be rerun.

---

## 19. What a subsequent actual mixed calculation must output

If $\mathbf{EF}_6$ is closed, the four head profiles from §9 reduce the leading low mixed coupling to four bounded contractions. Their inputs are fully specified by (9.1)–(9.6), the finite inverse, and the exterior solve.

That calculation must return the four actual low coupling constants, not merely a declaration that coefficients exist.

For the next paid layer after the ordinary tail zero, a valid certificate must additionally provide:

* the explicit ordinary/paid transition functional for the whole mixed pairing;
* all new coefficient and row-factor corrections;
* the same original low-prefix digits already supplied by the accepted residue;
* a terminal-zero conclusion for every continuation, or an actual completed nonzero terminal evaluation.

The accepted ordinary-tail residue should be reused. There is no reason to regenerate its modular exponentiation merely to feed a different, newly derived paid observable.

At present that paid functional has not been evaluated.

---

## 20. Precision budgets and the impossible target remain unchanged

The sufficient budgets are still


$$
\boxed{K_Z^{\rm norm}\ge d-c-1,}
$$




$$
\boxed{
K_Z^{\rm mixed}\ge d-1,\qquad
K_Y^{\rm mixed}\ge d-c,\qquad
N_{\log}\ge d-c.
}
$$



Neither $d\ge9$ nor $d\ge10$ is a final precision choice.

The accepted unbounded-content theorem also remains decisive: no nonempty full original arithmetic cylinder can have a fixed finite exact $c$. Nothing here seeks such a cylinder.

The original power is not replaced by a short-period digit word. Any future subsequence statement must retain exponent-to-digit compatibility.

---

# Part VI. Global arithmetic and proof status

## 21. Final gcd, actual primitive denominator, and whole error

No row content, row metric, or least two-column clearer has been changed.

Retain


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=\frac{A_B}{g_B},\qquad
p_n=\frac{H_B}{g_B}.
$$



The gcd is over all primes. The primitive multiplier remains


$$
d_B^2/g_B,
$$


and


$$
\log q_n=
\sum_\ell
\max\{v_\ell(A_B)-v_\ell(H_B),0\}\log\ell.
$$



For the same original index,


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
$$


and the relevant whole evaluated error is


$$
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n.}
$$



At the retained scope of the signed-error theorem,


$$
\epsilon_n>0\quad\text{eventually},
$$




$$
\log|\epsilon_n|
=
-\left(2+\frac1{2001}\right)n\log(1+\sqrt2)+o(n).
$$



No result in this report supplies the all-prime denominator bound needed to make the whole nonzero same-index expression tend to zero.

---

## 22. Proof-status ledger

| Statement | Status |
|---|---|
| Actual unit-head recovery and $c\ge2,d\ge9$ on $u\equiv2\pmod{24389}$ | Reused as accepted |
| Absolute unit ratios in the $\Xi$ specification | Audited |
| $220/242$ path counts and interface prefactors | Proved explicitly |
| $231$ complete low valuation-one paths versus $42$ middle transitions | Distinguished and proved |
| Common finite endpoint for all $231$ paths | Proved |
| Cancellation of every first-order high-dependent low-unit correction | Proved explicitly |
| No omitted high-factorial derivative tail in $\gamma$ | Proved at the stated precision |
| Numerical $\Xi$ | Not evaluated or predicted |
| Four-scalar actual first-head reduction modulo $p^2$ | Proved |
| Full-row factorization $ \mathsf P_-A_{\rm ext}=T_nD_+T_n $ | Proved |
| Bounded consolidated exterior-response atoms | Proved |
| Identification of that exterior response with the complete recurrence-defined second force | **Open source-specific lemma $\mathbf{EF}_6$** |
| $Y\in p^4$ and mixed factorization (16.2) | Conditional on $\mathbf{EF}_6$ |
| Actual complete paid mixed coefficient after the ordinary tail zero | Not evaluated |
| Actual original low-prefix obstruction | Not obtained |
| Exact content and primitive norm digit | Open |
| Norm-relative mixed alignment | Open |
| All-prime denominator versus whole same-index error | Open |
| Irrationality or rationality of $e+\pi$ | Unresolved |

---

## Conclusion

The new unconditional result is the detailed validation of the $\Xi$ lift: the absolute units, carry payments, $220/242$ interfaces, full $231$-path support, high-unit dependence, and finite endpoint all fit the proposed whole-numerator specification. In particular, the feared unretained first-order derivative tail does not occur.

For the mixed problem, the report supplies a concrete finite exterior-response mechanism and an explicit four-scalar actual-head reduction. These are more specific than a generic adjoint or an all-depth existence representation.

However, the complete second force cannot yet be replaced by the exterior response merely because its two initial charges match. The exact outstanding local lemma is


$$
\boxed{
\text{the complete recurrence source equals the exterior-forcing source
on every row }1,\ldots,b-2.
}
$$


Once proved, it gives a complete same-kernel mixed reduction through $F^TQ\bmod29^3$, including the first normalized corrections. The next paid mixed layer and its alignment with the independent $\rho_n$ remain separate obligations.

Accordingly, the assigned complete actual mixed evaluation is **not closed in this turn**. The bounded new certificate needed next is the finite source/exterior identity described in §18, with an explicit zero residual as its expected verifiable output. The coordinator’s $\Xi$ calculation remains a different, already specified new task; no accepted computation is proposed for repetition.

Finally, the actual all-prime primitive denominator has still not been compared with the whole nonzero same-index error on an infinite original sequence. An unconditional proof or disproof of the irrationality of $e+\pi$ remains unresolved.
