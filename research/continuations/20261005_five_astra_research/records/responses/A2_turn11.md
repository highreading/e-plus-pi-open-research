> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2: the coefficientwise mixed projection does hold at the first normalized lift

No irrationality or rationality decision for $e+\pi$ follows.

The main new result is stronger than a scalar-contraction identity. On the assigned original class


$$
n=2001\,3^a,\qquad b=3^a,\qquad a\equiv31\pmod{812},
$$


write


$$
p=29,\qquad n=pN,\qquad b=pB+27,\qquad H=B-q,
$$


and retain the exact integers


$$
T_q=\frac1p\binom Nq\binom{2N+B-q}{B-q},
\qquad 0\le q\le B.
$$


Then the actual complete normalized $Q$-column satisfies


$$
\boxed{
\bigl(Q^{[2]}_{pq},Q^{[2]}_{pq+1},Q^{[2]}_{pq+2}\bigr)
\equiv
6(-1)^qT_q(1,2,-2)\pmod{29}.
}
\tag{1}
$$


In particular,


$$
\boxed{
-Q^{[2]}_{pq}+2Q^{[2]}_{pq+1}-Q^{[2]}_{pq+2}
\equiv(-1)^qT_q\pmod{29}.
}
\tag{2}
$$



This holds coefficientwise for every $0\le q\le B$, with unrestricted higher digits in the stated class. It is not inferred from the $b=839$ certificate.

Both factorial blocks are needed. Their boundary contributions cancel in the weighted reconstruction. The first and quadratic inverse corrections are included below and shown not to alter these three coordinates at this precision.

Consequently,


$$
\boxed{
(P^{[1]})^TQ^{[2]}
\equiv
J\sum_{q=0}^{B}T_q^2
\equiv
\frac{(P^{[1]})^TP^{[1]}}{6J}
\pmod{29}.
}
\tag{3}
$$


The remaining problem is genuinely a **relative-depth problem**: (3) gives a $29$-divisible scalar defect, not a defect divisible by the actual normalized Gram contraction. I give an exact orthogonal-decomposition formula for that next defect in §7.

---

## 1. Domain, exact columns, and the supplied finite certificate

Throughout the new proof, the original index domain is


$$
a\ge1,\qquad a\equiv31\pmod{812},\qquad
b=3^a,\qquad n=2001b,\qquad m_w=1.
\tag{4}
$$


Thus


$$
B\equiv28\pmod p,\qquad N\equiv7\pmod p,\qquad B\ \text{is even}.
\tag{5}
$$


The proof of the $Q$-projection below uses these congruences, rather than any restriction on subsequent digits.

Put


$$
W_j=\binom{n+2}{j},\qquad
(\mathcal Z\theta)_j=j\theta_{j-1}-\theta_j,
\quad \theta_{-1}=\theta_b=0.
$$


The actual complete column is


$$
Y=\frac{V_w}{b!}
=
W_be_b+\operatorname{diag}(W_j)\mathcal Z\theta,
\qquad
\theta=T(-n)\widetilde N^{-1}(\rho/b!).
\tag{6}
$$


The previously established divisibilities on (4) make


$$
P^{[1]}=Z_w/p,\qquad Q^{[2]}=Y/p^2
\tag{7}
$$


exact integral $p$-adic columns.

The complete logarithmic forcing obeys


$$
v_p(h_i^F/b!)
\ge
F_n-F_b-\lfloor\log_p(2n+b-1)\rfloor\ge3.
\tag{8}
$$


It therefore cannot change any calculation modulo $p^3$ below. This is a bound on the whole forcing coefficient, not on a selected summand.

### What the $b=839$ receipt says

For the auxiliary pair


$$
(n,b)=(1678839,839),
$$


the displayed certificate gives, by direct extraction of its triples, precisely


$$
Q^{[2]}_{29q+s}
=
6(-1)^qT_q(1,2,-2)_s\pmod{29}.
$$


For example, at $q=0$,


$$
(21,13,16)=6\cdot18(1,2,-2)\pmod{29}.
$$


Its supplied $T$-vector has


$$
\sum_qT_q^2\equiv18\pmod{29}.
$$


Therefore the certified contractions are consistent with


$$
6\cdot13^2\cdot18\equiv11,\qquad
13\cdot18\equiv2\pmod{29}.
\tag{9}
$$



This is finite evidence for (1), stronger than merely checking $11/(6\cdot13)=2$. The proof follows independently.

---

## 2. Independent paper audit of the structured inverse

I first verify the operator used in the certificate, including its finite dimension.

Let


$$
d_s=s![z^s](1-z+z^2/2)^n.
$$


For $p=29$, these coefficients are $p$-integral. In fact,


$$
\boxed{
v_p(d_s)\ge v_p(n)+v_p((s-1)!)
\quad(s\ge1).
}
\tag{10}
$$



To see this directly, write $\phi(z)=1-z+z^2/2$. Since


$$
z\phi'(z)/\phi(z)\in\mathbb Z_p[[z]],
$$


the coefficient identity obtained from


$$
z(\phi^n)'=n\phi^n\,z\phi'/\phi
$$


shows that $s[z^s]\phi^n$ is $n$ times a $p$-integral quantity. Multiplication by $(s-1)!$ gives (10).

In particular,


$$
d_s\equiv0\pmod{p^3}\qquad(s\ge59).
\tag{11}
$$


The source computation's larger cutoff $s<87$ is harmless; the additional terms $59\le s<87$ are already zero modulo $p^3$.

### 2.1 Exact Newton transform

The defining contact coefficient has


$$
\binom{n+i}{s}\binom{n+i-s}{j}
=
\binom{j+s}{s}\binom{n+i}{j+s}.
$$


The inverse Pascal transform satisfies


$$
\Delta_i^k\binom{n+i}{m}\big|_{i=0}
=\binom n{m-k}.
$$


Consequently,


$$
\boxed{
(P^{-1}\widetilde N)_{kj}
=
\sum_{s\ge0}
d_s\binom{j+s}{s}\binom n{j+s-k}.
}
\tag{12}
$$


This is an exact identity, with actual matrix indices $0\le k,j<b$.

Modulo $p^3$, define


$$
E^*_{kj}
=
\sum_{s=1}^{58}\frac{d_s}{p}
\binom{j+s}{s}\binom n{j+s-k}\pmod{p^2}.
$$


Then


$$
A:=P^{-1}\widetilde N=T(n)+pE^*\pmod{p^3}.
\tag{13}
$$


Set


$$
\mathcal E=E^*T(-n).
$$


The factorization is


$$
A=(I+p\mathcal E)T(n),
$$


so its order-sensitive inverse is


$$
A^{-1}
=
T(-n)(I-p\mathcal E+p^2\mathcal E^2)
\pmod{p^3}.
$$


Therefore


$$
\boxed{
T(-n)\widetilde N^{-1}
=
T(-2n)(I-p\mathcal E+p^2\mathcal E^2)P^{-1}
\pmod{p^3}.
}
\tag{14}
$$


This verifies the coordinator's matrix order.

### 2.2 Why the extended columns are legitimate

For a length-$b$ input $v$, computing $E^*v$ by first placing


$$
\frac{d_s}{p}\binom{j+s}{s}v_j
$$


at extended index $j+s$, and then applying the binomial coefficients
$\binom n{j+s-k}$, is exactly (12).

The extension occurs only while evaluating this operator:

* its input has indices $0,\ldots,b-1$;
* its output has indices $0,\ldots,b-1$;
* each subsequent $T(-n)$, and each application of $\mathcal E$, is again $b$-dimensional.

Thus the implementation does **not** replace the actual inverse by an inverse in a larger dimension.

With cutoff $87$, the largest extended index is


$$
(b-1)+86=b+85,
$$


so length $b+86$, as in the source, is sufficient. The stored binomial series is longer than necessary, not shorter.

Only $E^*\bmod p^2$ is needed in the linear correction, and only $E^*\bmod p$ in the quadratic correction. Dividing a representative $d_s\bmod p^3$ by $p$ determines exactly the required residue modulo $p^2$.

### 2.3 Other truncations used in the receipt

At $b=839$,


$$
b+2=841=p^2.
$$


The factorial quotient $(b+d)!/b!$ has:

* valuation $0$ for $d=0,1$;
* valuation $2$ for $2\le d\le30$;
* valuation at least $3$ from $d=31$ onward.

Hence the exclusive factorial-tail endpoint $870=b+31$ is correct.

The original $P$-forcing has a consecutive-product factor


$$
(n+i)!/n!,
$$


so $i\ge87=3p$ gives valuation at least three. Its forcing cutoff is therefore valid too.

Finally, the receipt's complete logarithmic depth


$$
59957-28-4=59925
$$


is far beyond the requested precision.

**Audit conclusion:** the structured inverse and the relevant truncations pass the paper check. This does not amount to independently executing the certificate.

---

## 3. A finite-boundary lemma that controls all contact corrections

The useful new simplification is to combine the residual correction and inverse correction **before** projecting.

Let $U=T(n)$ on finitely supported sequences indexed by nonnegative integers. Define the raising operator


$$
(D_sv)_{j+s}=\binom{j+s}{s}v_j.
$$


The Newton-transformed contact matrix is the restriction of


$$
U\sum_s d_sD_s
$$


to the actual rows and columns.

For $l\ge b>k$, put


$$
C_s(k,l)=(UD_sU^{-1})_{kl}.
$$


A generating-function calculation gives the exact formula


$$
\boxed{
C_s(k,l)=
\sum_{v=1}^{s}
\binom{k}{s-v}\binom nv
\binom{-v}{l-k+s-v}.
}
\tag{15}
$$


Indeed, its row generating function is


$$
\frac1{s!}\frac{d^s}{dz^s}\bigl(z^k(1+z)^n\bigr)(1+z)^{-n}.
$$



For $l>k$,


$$
\binom{-v}{l-k+s-v}
=
(-1)^{l-k+s-v}
\binom{l-k+s-1}{v-1}.
$$


Thus $C_s(k,l)$ is $(-1)^k$ times an integer-valued polynomial in $k$ of degree at most $s-1$.

### 3.1 The combined correction

Write


$$
b+2=p^2K,\qquad K=(B+1)/p.
\tag{16}
$$


Let $R_0$ be the Newton transform of the $s=0$ residual, including both factorial blocks, and put


$$
y_0=T(-n)R_0.
$$


Let $R$ be the Newton transform of the complete residual. The exact correction equation is


$$
A(y-y_0)=F,\qquad
F:=R-R_0-(A-T(n))y_0.
\tag{17}
$$



The nonconstant contact coefficients multiplying the second factorial block have valuation at least three. Hence, modulo $p^3$, only the two unit tails $b,b+1$ enter $F$. Their exact finite-boundary expression is


$$
\boxed{
F_k=
\sum_{s=1}^{58}d_s
\left[
\bigl(1+2n(b+1)\bigr)C_s(k,b)
+(b+1)C_s(k,b+1)
\right].
}
\tag{18}
$$


No columns beyond the actual inverse dimension have been retained as unknowns. They have been eliminated into the explicit boundary kernel (15).

Split


$$
F=pF_1+p^2F_2,
\tag{19}
$$


where $F_1$ consists of the terms $s\le p$, divided by $p$, and $F_2$ of $p<s\le2p$, divided by $p^2$.

These sequences have the following precise structure:

1. $F_1(k)=(-1)^kA(k)$, with
   

$$
A\in\mathbb Z_p[k],\qquad \deg A\le p-1.
$$


2. Modulo $p$, $F_1$ is supported only on
   

$$
k\bmod p\in\{27,28\}.
   \tag{20}
$$


3. $F_2(k)$ is $(-1)^k$ times an integer-valued polynomial of degree at most $2p-1=57$, with $p$-integral Newton coefficients.

For (20), all $s<p$ terms acquire a factor $p$ from $\binom nv$. At $s=p$, only $v=p$ can remain, and


$$
\binom{-p}{l-k}\equiv0\pmod p
$$


unless $l-k$ is divisible by $p$. The two boundary values $l=b,b+1$ give residues $27,28$.

### 3.2 The finite summation identity used for the valuation

For $L=b-1-j$,


$$
\boxed{
\begin{aligned}
&\sum_{h=0}^{L}
\binom{-2n}{h}(-1)^{j+h}\binom{j+h}{r}\\
&\quad=
(-1)^j\sum_{t=0}^{r}
\binom j{r-t}
\binom{2n+t-1}{t}
\binom{2n+L}{L-t}.
\end{aligned}}
\tag{21}
$$


Terms with invalid lower indices are zero. This is a finite identity, so its upper boundary is retained.

Take


$$
j=pq+u,\qquad u=0,1,2.
$$


If $W_j$ is a unit, Lucas implies $q\bmod p\le7$. Therefore


$$
H\bmod p=28-(q\bmod p)\ge21.
\tag{22}
$$


Also


$$
L=pH+26-u.
$$


For every $0\le t\le57$, the binomial


$$
\binom{2n+L}{L-t}
$$


vanishes modulo $p$: after its lowest digit, its lower digit is one of


$$
H_0,\ H_0-1,\ H_0-2,
$$


while the corresponding upper digit is


$$
(2N+H)\bmod p=H_0-15.
$$


The lower digit is strictly larger.

Applying (21) to $F_2$ now gives


$$
W_j(T(-2n)F_2)_j\equiv0\pmod p.
\tag{23}
$$



For $F_1$, a stronger conclusion holds:


$$
\boxed{
W_j(T(-2n)F_1)_j\equiv0\pmod{p^2},
\qquad u=0,1,2.
}
\tag{24}
$$


At a unit weight:

* the $t=0$ term has $A(j)\equiv0\pmod p$ by (20), as well as the vanishing binomial just proved;
* for $1\le t\le p-1$, the factor
  

$$
\binom{2n+t-1}{t}
$$


  is divisible by $p$, and the other binomial also vanishes modulo $p$.

At a nonunit weight, $T(-2n)F_1$ is already zero modulo $p$ in residues $0,1,2$, because the shift preserves low residues modulo $p$.

### 3.3 The inverse corrections, including the quadratic one

Using (14), (17), and (19),


$$
\boxed{
\theta-\theta_{\rm base}
=
pT(-2n)F_1+
p^2T(-2n)F_2-
p^2T(-2n)\mathcal EF_1
\pmod{p^3}.
}
\tag{25}
$$


Here


$$
\theta_{\rm base}=T(-2n)R_0.
$$



This identity is obtained from the full inverse, including its quadratic term. In this reorganized equation the term $p^2\mathcal E^2F$ is divisible by $p^3$, since $F\in p\mathbb Z_p^b$. The quadratic inverse contribution on the original right-hand side has not simply been dropped.

For a row with low digit $u\le2$, the matrix $E^*\bmod p$ uses only columns whose low digits are at most $u$. This follows directly from (12) and Lucas:

* for $s<p$, nonvanishing requires $s\le u$;
* for $s=p$, the column has the same low digit as the row;
* $s>p$ contributes zero modulo $p$.

Thus $\mathcal EF_1$ vanishes on low residues $0,1,2$, by (20). Equations (23)–(25) show that the weighted correction to $\theta_j$ is zero modulo $p^3$ there.

The predecessor at $j=pq$ must also be checked. It is multiplied by $pq$. For $q\ge1$,


$$
(T(-2n)F_1)_{pq-1}
\equiv
(-1)^{q-1}A(28)\binom{2N+H}{H}\pmod p.
\tag{26}
$$


The upper limit here is $B-1$, not $B$, because residue $28$ lies beyond $b-1$ in the last block. At a unit weight the last binomial vanishes by (22); at a nonunit weight the weight supplies the needed factor. At $q=0$, the predecessor coefficient is exactly zero.

We have proved:


$$
\boxed{
\text{The actual contact corrections change none of }
Y_{pq},Y_{pq+1},Y_{pq+2}\pmod{p^3}.
}
\tag{27}
$$



---

## 4. Both factorial blocks and their boundary cancellation

It remains to evaluate the $s=0$ base solution.

Finite convolution gives, for $j<b$,


$$
\theta_{{\rm base},j}
=
-\sum_{d\ge0}\frac{(b+d)!}{b!}
\sum_{k=0}^{d}
\binom{-2n}{b-j+k}\binom{2n}{d-k}.
\tag{28}
$$


This is the actual truncated-inverse boundary term.

Put


$$
x=-2n,\qquad j=pq,\qquad l=b-j,\qquad
f_r=\binom xr,\qquad
g=\binom{x}{l+2}.
$$



### 4.1 The unit factorial block

The terms $d=0,1$ give


$$
-\bigl(1+2n(b+1)\bigr)f_{b-j}-(b+1)f_{b-j+1}.
$$


Since $b+1=-1+p^2K$, for $u=0,1,2$,


$$
\theta_{{\rm base},pq+u}
\equiv
f_{l-u+1}-(1+x)f_{l-u}
+\text{second block}
\pmod{p^3}.
\tag{29}
$$


The omitted $p^2Kf_{l-u+1}$ term is divisible by $p^3$, since its lower index has a nonzero low digit.

### 4.2 The second factorial block

For $2\le d\le30$,


$$
\frac{(b+d)!}{p^2b!}
\equiv-K(d-2)!\pmod p.
$$


In row $pq+u$, only $d=u+2$ survives the Lucas test in (28). Hence


$$
\boxed{
\theta_{{\rm base},pq+u}
\equiv
f_{l-u+1}-(1+x)f_{l-u}
+p^2K\,u!\binom{-2N}{H+1}
\pmod{p^3}.
}
\tag{30}
$$


This is the required second-block contribution.

For the predecessor, only precision $p^2$ is needed:


$$
\theta_{{\rm base},pq-1}
\equiv g-(1+x)f_{l+1}\pmod{p^2}.
\tag{31}
$$



### 4.3 The cancellation at low digit zero

The exact binomial identity


$$
(l+2)g=(x-l-1)f_{l+1}
$$


and $j+l+2=b+2=p^2K$ give


$$
jg=p^2Kg-(x-l-1)f_{l+1}.
\tag{32}
$$


The $p^2Kg$ term in (32) cancels the second-block contribution in


$$
j\theta_{j-1}-\theta_j.
$$


Thus


$$
Y_j
\equiv
W_j\left[(1+x)f_l-
\bigl(x-l+j(1+x)\bigr)f_{l+1}\right]
\pmod{p^3}.
\tag{33}
$$



For the coordinates $j+1,j+2$, the second-block contributions cancel to the required precision because


$$
(j+1)0!-1!=j,\qquad
(j+2)1!-2!=j.
$$


Each resulting term has the additional factor $j=pq$.

This cancellation is why a calculation retaining only the first factorial block would be incorrect.

---

## 5. Evaluation of the three weighted coordinates

We need one uniform product estimate, including the cases in which the weight itself is nonunit.

Let


$$
X=-2N,\qquad A_H=\binom{2N+H}{H}.
$$


The elementary prime-block congruence


$$
\binom{pU}{pV}\equiv\binom UV\pmod{p^2}
\tag{34}
$$


holds for integer $U$ and $V\ge0$, including negative $U$. It follows by expanding


$$
(1+z)^{pU}
=
(1+z^p+pA(z))^U\pmod{p^2},
$$


where $A(z)$ has degrees $1,\ldots,p-1$; the linear term cannot contribute to a degree divisible by $p$.

Using (34) and products with unit denominators,


$$
W_jf_l
\equiv
p\,\frac{X}{27}\,
(-1)^H\binom Nq A_H
\pmod{p^3}.
\tag{35}
$$


Here all first-order unit-ratio corrections disappear because


$$
p\mid\binom Nq A_H.
$$


In particular,


$$
v_p(W_jf_l)\ge2.
$$


Since $X\equiv-14\pmod{29}$,


$$
\boxed{
\frac{W_jf_l}{p^2}
\equiv7(-1)^HT_q\pmod{29}.
}
\tag{36}
$$



The ratios needed in (33) and its two adjacent reconstructions all have unit denominators:


$$
\frac{f_{l+1}}{f_l}\equiv-2,\qquad
\frac{f_{l-1}}{f_l}\equiv-\frac23,\qquad
\frac{f_{l-2}}{f_l}\equiv\frac12\pmod p.
\tag{37}
$$


Also


$$
\frac{W_{j+1}}{W_j}\equiv2,\qquad
\frac{W_{j+2}}{W_j}\equiv1\pmod p.
$$


Because $W_jf_l$ is already divisible by $p^2$, only these leading unit ratios are required.

The resulting three coefficients multiplying $W_jf_l$ are


$$
5,\qquad-\frac{28}{3},\qquad\frac92\pmod{29}.
$$


Multiplying by the factor $7$ in (36) gives


$$
6,\qquad12,\qquad-12.
$$


Finally, $B$ is even, so $(-1)^H=(-1)^q$. Together with (27), this proves


$$
\boxed{
\bigl(Q^{[2]}_{pq},Q^{[2]}_{pq+1},Q^{[2]}_{pq+2}\bigr)
\equiv6(-1)^qT_q(1,2,-2)\pmod{29}.
}
$$



All indices in these triples lie strictly below $b$. The endpoint $j=b$ remains in the actual column but is outside this projection. Its omission from the mixed residue is justified by the established first normalized $P$-column support—not by deleting it from the construction.

---

## 6. Elimination of $Q^{[2]}$ from the mixed contraction

The established first normalized $P$-digit is


$$
(P^{[1]}_{pq},P^{[1]}_{pq+1},P^{[1]}_{pq+2})
\equiv
J(-1)^qT_q(-1,2,-1)\pmod p,
$$


and all other $P^{[1]}$-coordinates vanish modulo $p$.

Taking the triple projection in (1),


$$
-6+2\cdot12-(-12)=30\equiv1\pmod{29}.
$$


Therefore


$$
-Q^{[2]}_{pq}+2Q^{[2]}_{pq+1}-Q^{[2]}_{pq+2}
\equiv(-1)^qT_q\pmod{29}.
$$


Substitution into the previous equation (7.6) now gives the evaluated identity


$$
\boxed{
(P^{[1]})^TQ^{[2]}
\equiv J\sum_qT_q^2\pmod{29}.
}
\tag{38}
$$


Together with the actual norm formula,


$$
\boxed{
(P^{[1]})^TP^{[1]}
\equiv6J^2\sum_qT_q^2\pmod{29},
}
\tag{39}
$$


this proves (3).

Thus:

* the coefficientwise triple-projection relation holds;
* the weighted contraction relation follows from it;
* the full vector $Q^{[2]}$ is **not** asserted proportional to $P^{[1]}$;
* no condition has been imposed on admissible higher digits.

In particular, on every original index in (4) where


$$
\sum_qT_q^2\not\equiv0\pmod{29},
$$


both evaluated normalized contractions are units. No infinite norm-unit subclass is asserted here.

---

## 7. What can be iterated, and the exact Gram-divisibility obstruction

Let


$$
C_n=\operatorname{CT}(t^{-1}+2+2t)^n
$$


as an actual integer. The supplied digit-factor theorem makes $C_n$ a $29$-adic unit. Set


$$
P=P^{[1]},\qquad Q=Q^{[2]},\qquad
D_1=P^TP,\qquad M_1=P^TQ,\qquad
c=\frac1{6C_n}.
$$


The new theorem proves


$$
\boxed{
M_1=cD_1+pE_1,\qquad E_1\in\mathbb Z_p.
}
\tag{40}
$$


Equivalently, in the original contractions,


$$
\boxed{
\Xi=\frac{p}{6C_n}\mathfrak D+p^4E_1.
}
\tag{41}
$$


This improves the absolute remainder depth, but does not yet prove a relative remainder bound.

### 7.1 An exact orthogonal defect formula

On each supported triple let


$$
e=(-1,2,-1)^T,\qquad \Pi_{\rm triple}=\frac{ee^T}{6}.
$$


Let $\Pi$ be the block-diagonal operator with these blocks, and zero on all other coordinates, including the endpoint. Since $6$ is a $29$-unit, $\Pi$ is an integral $p$-adic orthogonal idempotent.

Write


$$
P_\parallel=\Pi P,\qquad P_\perp=(I-\Pi)P,
$$


and similarly for $Q$.

The two coefficientwise column formulas prove


$$
P_\perp\in p\mathbb Z_p^{b+1},\qquad
Q_\parallel-cP_\parallel\in p\mathbb Z_p^{b+1}.
$$


Define the exact integral vectors


$$
U_\perp=P_\perp/p,\qquad
U_\parallel=(Q_\parallel-cP_\parallel)/p.
$$


Orthogonality then gives the exact identity


$$
\boxed{
E_1=
P_\parallel^TU_\parallel
+
U_\perp^TQ_\perp
-
pc\,U_\perp^TU_\perp.
}
\tag{42}
$$



This is a new bounded follow-on lemma: it isolates the next defect into actual parallel and orthogonal components, with no unspecified contraction discarded.

### 7.2 Why a vanishing next digit does not automatically iterate

Put


$$
\alpha=v_p(D_1),\qquad \gamma=v_p(M_1).
$$


A sufficient relative estimate is


$$
\boxed{v_p(E_1)\ge\alpha.}
\tag{43}
$$


It would imply


$$
M_1=D_1(c+p\,\text{\(p\)-integral quantity}),
$$


and hence $\gamma=\alpha$.

What is proved here is only $E_1\in\mathbb Z_p$. If the common norm/mixed digit vanishes, division of (40) by $p$ gives


$$
\frac{M_1}{p}=c\frac{D_1}{p}+E_1.
$$


The new error is no longer accompanied by an automatic factor $p$. Its residue must be evaluated.

On a whole-column-zero subclass, where $P\in p\mathbb Z_p^{b+1}$, (42) reduces to


$$
\boxed{
E_1\equiv U_\perp^TQ_\perp\pmod p.
}
\tag{44}
$$


Thus the next obstruction can come from the first subsequent $P$-digit paired with the orthogonal part of the present $Q$-digit. The fact that the supported triple projections vanish does not remove this term.

Accordingly, the remainder is now proved **$p^4$-divisible in (41)**. It is not proved **Gram-divisible**. Formula (42) identifies exactly what an iteration must control.

---

## 8. Final gcd, actual primitive denominator, and whole evaluated error

For the original family, retain the actual least two-column $B$-denominator $d_B$ and


$$
N_B=d_B[u,v],
$$




$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
p_n=H_B/g_B,\qquad q_n=A_B/g_B.
\tag{45}
$$


At $29$, the established local integrality gives $v_{29}(d_B)=0$.

With


$$
F_n=v_{29}(n!),\qquad F_b=v_{29}(b!),
$$


and $\alpha,\gamma$ as above, the exact final identities remain


$$
\boxed{
v_{29}(g_B)
=
\min\{4F_n+2+\alpha,\ 2F_n+F_b+3+\gamma\},
}
\tag{46}
$$




$$
\boxed{
v_{29}(q_n)
=
\max\{0,\ 2F_n-F_b-1+\alpha-\gamma\}.
}
\tag{47}
$$


The new theorem proves simultaneous first normalized scalar zeros. It evaluates (47) whenever their common first digit is nonzero, but does not evaluate $\alpha-\gamma$ after that digit vanishes.

For the auxiliary $b=839$ certificate, the supplied unit residues give the finite consequences


$$
\alpha=\gamma=0,
$$




$$
v_{29}(q_n)=119885,\qquad
v_{29}(g_B)=119945,
$$


using the same actual local least-denominator interface. The complete mixed contraction is nonzero there because its certified normalized residue is a unit. These are auxiliary finite conclusions, not original-power-$3$ conclusions.

On the original domain, the norm is positive and the complete mixed contraction is nonzero by the retained original $3$-adic result. At the supplied dependency status of the complete signed-rate theorem,


$$
\epsilon_n=c_n-(e+\pi)>0\quad\text{eventually},
$$




$$
\log|\epsilon_n|
=
-\left(2+\frac1{2001}\right)\log(1+\sqrt2)\,n+o(n).
$$


The actual primitive evaluated form is still


$$
\boxed{
L_n=q_n(e+\pi)-p_n=-q_n\epsilon_n<0
\quad\text{eventually}.
}
\tag{48}
$$


It uses the whole error, including the exponential residual, logarithmic forcing, and endpoint correction. Neither this one-prime refinement nor the finite auxiliary denominator evaluates the global denominator rate.

---

# Concluding ledger

## (1) New result and proof status

**Proved here**

1. The coefficientwise complete normalized $Q$-triple formula
   

$$
Q^{[2]}_{pq,pq+1,pq+2}
   \equiv6(-1)^qT_q(1,2,-2)\pmod{29}
$$


   on the stated original class, with unrestricted higher digits.

2. Hence the requested projection identity holds coefficientwise:
   

$$
-Q^{[2]}_{pq}+2Q^{[2]}_{pq+1}-Q^{[2]}_{pq+2}
   \equiv(-1)^qT_q\pmod{29}.
$$



3. The actual evaluated normalized contractions satisfy
   

$$
(P^{[1]})^TQ^{[2]}
   \equiv\frac{(P^{[1]})^TP^{[1]}}{6J}\pmod{29}.
$$



4. The proof retains both factorial blocks and all inverse corrections through $p^3$. Their cancellation is derived from the explicit finite-boundary kernel (15).

5. The coordinator's structured inverse passes the independent paper audit, including the extended-column implementation and all relevant truncations.

6. The exact next-defect identity (42) isolates the parallel and orthogonal contributions that must be controlled for an iteration.

**Not proved**

Gram-divisibility of the next remainder, an all-depth equality $\alpha=\gamma$, a favorable global final-gcd rate, or irrationality or rationality of $e+\pi$.

## (2) Exact remaining bottleneck

The local next obligation is


$$
\boxed{
v_{29}(E_1)\ge
v_{29}\bigl((P^{[1]})^TP^{[1]}\bigr),
}
$$


or another bound strong enough to control $\gamma-\alpha$, with


$$
E_1=
P_\parallel^TU_\parallel+
U_\perp^TQ_\perp-
29(6C_n)^{-1}U_\perp^TU_\perp.
$$



The new congruence improves absolute precision. It does not, by itself, supply this relative estimate. Even a successful local estimate would leave the other primes in the actual primitive denominator.

## (3) Bounded computation request

No additional computation is needed to establish the first normalized projection proved above.

A useful **next-depth diagnostic**, if the coordinator chooses to perform one, is:

**Inputs**


$$
(n,b,p)=(1678839,839,29),
$$


with the same original complete construction, now through modulus $29^4$.

**Requested verifiable outputs**

* $C_n\bmod29^2$;
* $D_1=(P^{[1]})^TP^{[1]}\bmod29^2$;
* $M_1=(P^{[1]})^TQ^{[2]}\bmod29^2$;
* the exact divided defect
  

$$
E_1=\frac{M_1-D_1/(6C_n)}{29}\pmod{29};
$$


* an independent check of the orthogonal formula (42) modulo $29$.

At precision four, the divided-coefficient cutoff can be $s\le87$, the factorial-tail endpoint is $899=b+60$, and the whole logarithmic depth remains at least $59925$. No value for the new defect is predicted.

Because this auxiliary norm is already a unit, such a computation would audit the next-defect formula; it would **not** settle Gram-divisibility at a vanishing normalized norm or prove an infinite assertion.
