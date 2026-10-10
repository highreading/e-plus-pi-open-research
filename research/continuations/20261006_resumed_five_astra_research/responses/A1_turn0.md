> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A1 — Complete core-layer compression and a six-digit inverse certificate

## Executive summary

The accepted Turn 13 transfer changes the next task substantially. On its stated sufficiently large original-index window, and only under all of its simultaneous hypotheses,


$$
S_c\in3^{26}M_\nu(\mathbb Z_3),
\qquad
S_{\rm act}-S_c\in3^{32}M_\nu(\mathbb Z_3).
$$


Consequently, with


$$
B_c=-S_c/3^{26},\qquad \Theta=-S_{\rm act}/3^{26},
$$


we have


$$
\Theta\equiv B_c\pmod{3^6}.
$$



This report does **not** establish the rank of $B_c\bmod3$. It advances the complete normalized-layer problem in three concrete ways.

1. **Complete first-layer compression.**  
   The whole bracket (8.1), with both corrected representatives, all lower poles and their carries, and the original cutoff, determines a Hankel matrix over $\mathbb F_3$. Thus only $2\nu-1=D-3$ complete bracket evaluations are needed, rather than $\nu^2$. An explicit finite convolution map gives its exact kernel and endpoint action. This is a target-specific finite representation, not a bounded-state or feasible-complexity theorem.

2. **A decisive six-digit certificate for the inverse bottleneck.**  
   Successive radical/complement reductions of $B_c\bmod3^6$ decide whether
   

$$
s_c<32.
$$


   More precisely, if $B_c$ is nonsingular and its largest Smith exponent is $a$, then
   

$$
s_c=26+a.
$$


   Six normalized digits certify $a\le5$ exactly when the sixth residual radical is zero. A nonzero sixth radical excludes $s_c<32$ at that particular original input, whether the exact matrix is singular or nonsingular.

3. **Endpoint-sensitive guard precision.**  
   Even when $s_c<32$, a determinant comparison alone does not protect the whole cofactor ratio. A sharper sufficient comparison uses the inverse image of the **actual endpoint channel**, rather than the worst matrix inverse loss. If
   

$$
z_c=B_c^{-1}e_c,\qquad
   u=\max\!\left(0,-\min_i v_3((z_c)_i)\right),
$$


   then, under $a<6$, the complete scalar
   

$$
\sigma_{\rm act}
   =e_{\rm act}^T\Theta^{-1}e_{\rm act}-3^{26}d_{\rm act}
   =D_1/D_0
$$


   agrees with its core counterpart to precision $3^{6-2u}$. This gives an explicit nonvanishing and relative-valuation criterion, with the complete subtraction retained.

No original-index coefficient calculation has been performed here. Therefore the assertion $s_c<32$ remains **open on the moving original family**. Neither its truth nor its failure follows from the support-certificate ceiling.

The rationality or irrationality of $e+\pi$ remains unresolved.

---

## 1. Scope, hypotheses, and the complete data

Retain


$$
n=4^j+1,\qquad j>0,\qquad81\mid j,
$$


and


$$
A=n-2=H-D,\qquad H=3^{h-1},\qquad0<D<H/972.
$$


Set


$$
x=y-1,\qquad
m=\frac{A+1}{2},\qquad
d=\frac{3D}{2}-1,\qquad
\nu=\frac D2-1.
$$



The original columns are exactly


$$
U_u=x^u\quad(0\le u<D),\qquad
z_i=x^Dy^i\quad(0\le i<\nu),
$$




$$
Y_b=y^b\quad(d\le b\le m),\qquad W=[U\ Y].
$$


In particular,


$$
2\nu-2=D-4.
$$


No residual moment with index $2\nu-1$, no HIGH column beyond $m$, and no additional exterior coordinate is introduced.

The complete functional is


$$
\mathcal M(F)=
-\frac{3^h}{4}\mathfrak f(F)
+
3^h\sum_{\substack{v\ge0\\2v+1\le4n-3}}
\frac{[y^v](F-F(-1))/(y+1)}{2v+1},
\qquad
\mathfrak f(y^r)=(2r)!.
\tag{1.1}
$$


The producer remains


$$
Q_{\rm act}=Q_c+3^6R,\qquad
Q_c=(y+1)x^A(\beta+3y),\qquad
\beta=-71-A.
\tag{1.2}
$$


The signed producer system, its complete factorial force, and its actual scalar denominator are not replaced by another producer.

### 1.1 Precisely what is reused

The coordinator has accepted Turn 13’s conditional transfer. I reuse it, rather than repeat its proof.

For general $P,L,p$, its hypotheses include


$$
P,L\ge7,\quad p\ge1,\quad h-1\ge P,\quad
\Omega=H/3^{P-1}>4D+2P+3,
$$


the existence of the exact terminal factorial length $\ell_{6+p}$,


$$
2v_3((A+1)!)\ge6+p,\qquad
\kappa_p=\ell_{6+p}-2,
$$


and both polynomial budgets


$$
\left\lfloor\frac{L-1}{6}\right\rfloor\kappa_p\le D,
\qquad
\frac{\Omega-4D-2P-3}{2}\ge L-6.
\tag{1.3}
$$


Its conclusion is


$$
S_{\rm act}-S_c\in
3^{\min(L+1,P+7,p+7)}M.
\tag{1.4}
$$



For the remainder of this report, the depth-$26$ statements apply on the sufficiently large retained window


$$
j\equiv81\pmod{243},\qquad
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad
C_{16}=147968\,3^{15},
\tag{1.5}
$$


with all accepted finite-support dependencies in force. Here the accepted specialization is


$$
P=25,\qquad L=31,\qquad p=25,\qquad\kappa_{25}=54.
$$



The independent A4 audit of Turn 13 is not presumed completed.

---

## 2. The complete first layer, with carries retained

Choose the accepted precision-$25$ representatives


$$
\phi_i=x^D\psi_i,\qquad
\phi_i\equiv\widehat z_i^{\,c}\pmod{3^{25}},
\qquad 0\le i<\nu.
$$


Define


$$
T_{ij}=x^{H+D}(\beta+3y)\psi_i\psi_j.
\tag{2.1}
$$


Then


$$
Q_c\phi_i\phi_j=(y+1)T_{ij}.
$$



For an integral polynomial $T$, introduce the finite bracket


$$
\begin{aligned}
\mathcal B_{27}(T)={}&
-\frac{3^h}{4}\mathfrak f((y+1)T)\\
&+\sum_{\ell=0}^{26}
\ \sum_{\substack{c\ge1\ {\rm odd},\ 3\nmid c\\
c3^{h-\ell}\le4n-3}}
3^\ell c^{-1}
[y^{(c3^{h-\ell}-1)/2}]T
\pmod{3^{27}}.
\end{aligned}
\tag{2.2}
$$


Every inverse $c^{-1}$ is taken modulo the precision needed by its term.

The accepted bracket identity gives


$$
(B_c)_{ij}\equiv
-\frac{\mathcal B_{27}(T_{ij})}{3^{26}}\pmod3.
\tag{2.3}
$$


The division means:

1. evaluate and add the entire bracket modulo $3^{27}$;
2. verify its residue modulo $3^{26}$ is zero;
3. divide the resulting multiple of $3^{26}$.

There is no termwise division by $3^{26}$.

### 2.1 A precise carry interpretation

Write the full bracket as


$$
b_0+3b_1+\cdots+3^{26}b_{26}\pmod{3^{27}},
$$


where each $b_\ell$ includes the complete coefficient sum at that pole layer, and the factorial contribution is included at its actual valuation.

Then (2.3) depends not only on $b_{26}\bmod3$, but also on the carries from all $b_0,\ldots,b_{25}$. Consequently, cancellation of one finest-pole pair does not evaluate (2.3).

Likewise, the map


$$
T\longmapsto \frac{\mathcal B_{27}(T)}{3^{26}}\pmod3
$$


is defined only on the submodule on which the complete bracket is divisible by $3^{26}$. It is not an unrestricted functional on $\mathbb F_3[y]$. Reducing $T$ modulo $3$ before forming the bracket generally destroys its value.

This is the exact obstruction to an immediate Lucas-theorem evaluation of the normalized layer.

### 2.2 The factorial term at this particular modulus

The factorial term remains part of (2.2). On the present window its omission **after valuation checking** is legitimate.

Indeed, the accepted $P=25,L=31$ upper gap gives


$$
H/3^{24}\ge4D+103.
$$


Since $D\ge486$, this implies $h>27$. The polynomial $(y+1)T$ is integral, so


$$
\frac{3^h}{4}\mathfrak f((y+1)T)\in3^{27}\mathbb Z_3.
$$


Thus it contributes zero to (2.2). This is a modulus-specific conclusion, not deletion of the factorial force from the exact construction or from higher-precision work.

---

## 3. A complete finite characteristic-$3$ representation

The following compression uses the accepted **whole-form** Hankel normalization. It does not assert that the separate pole layers are Hankel.

### Theorem 3.1 — Complete bracket Hankel compression

There are uniquely determined residues


$$
\lambda_0,\ldots,\lambda_{2\nu-2}\in\mathbb F_3
$$


such that


$$
B_c\bmod3=(\lambda_{i+j})_{0\le i,j<\nu}.
\tag{3.1}
$$


They can be evaluated by exactly $2\nu-1=D-3$ complete bracket evaluations:



$$
\lambda_k=
-\frac{\mathcal B_{27}(T_{0k})}{3^{26}}\pmod3,
\qquad 0\le k<\nu,
\tag{3.2}
$$


and


$$
\lambda_k=
-\frac{\mathcal B_{27}(T_{k-\nu+1,\nu-1})}{3^{26}}\pmod3,
\qquad \nu\le k\le2\nu-2.
\tag{3.3}
$$



#### Proof

The accepted actual normalization gives


$$
\mathsf H=\mathsf V^T\Psi\mathsf V,\qquad
\Psi=-S_{\rm act}/3^{16},\qquad
\mathsf V\equiv I\pmod3.
$$


Since $S_{\rm act}\in3^{26}M$,


$$
\mathsf H/3^{10}=\mathsf V^T\Theta\mathsf V
$$


is integral and Hankel. Reduction modulo $3$ gives


$$
\mathsf H/3^{10}\equiv\Theta\equiv B_c\pmod3.
$$


Hence $B_c\bmod3$ is Hankel.

The first row supplies anti-diagonals $0,\ldots,\nu-1$. The final column, starting at row $1$, supplies anti-diagonals $\nu,\ldots,2\nu-2$. Equations (3.2)–(3.3) then follow from (2.3). ∎

This gives a complete finite representation over characteristic $3$. Its input is still a carry-sensitive computation modulo $3^{27}$; the theorem does not disguise that cost.

### 3.1 Exact kernel and endpoint

Put


$$
L(X)=\sum_{k=0}^{2\nu-2}\lambda_kX^k.
$$


For $a=(a_0,\ldots,a_{\nu-1})^T$, set


$$
a^\vee(X)=\sum_{j=0}^{\nu-1}a_jX^{\nu-1-j}.
$$


Then


$$
\boxed{
a\in\ker(B_c\bmod3)
\iff
[X^{\nu-1+i}]L(X)a^\vee(X)=0
\quad(0\le i<\nu).
}
\tag{3.4}
$$



Indeed, the displayed coefficient equals


$$
\sum_{j=0}^{\nu-1}\lambda_{i+j}a_j.
$$



The actual endpoint acts on this kernel by


$$
\boxed{
a\longmapsto\sum_{j=0}^{\nu-1}(-1)^ja_j.
}
\tag{3.5}
$$


This follows from the accepted endpoint residue


$$
e_{\rm act}\equiv e_c\equiv(1,-1,\ldots,(-1)^{\nu-1})^T\pmod3.
$$



Thus (3.2)–(3.5) specify the exact first-layer rank, radical, and endpoint action once the $D-3$ whole residues have been evaluated.

### 3.2 Complete forcing and terminal return

This representation does not extend the moment sequence. Its forcing remains


$$
\lambda_{i+\nu}+\sum_{k=0}^{\nu-1}\bar f_k\lambda_{i+k}
=\bar b_i^{\langle26\rangle},
\qquad0\le i\le\nu-2.
\tag{3.6}
$$


The endpoint identity remains


$$
J^T\varepsilon+\omega
=
-\varepsilon-s\bigl(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\bigr).
\tag{3.7}
$$


Neither $\omega_{\nu-1}$ nor the terminal component of the forcing is suppressed.

Equations (3.6)–(3.7) are consistency conditions for the complete computed data; a homogeneous companion recurrence cannot replace them.

### 3.3 What has not been established

No value of $\lambda_k$, no nonzero coefficient, and no rank has been obtained here. The representation is exact but not proved small in $n$. Established finite-field extraction and rational/diagonal methods do not by themselves provide a feasible observable module for these particular carry-sensitive inputs.

---

## 4. From a first-layer rank defect to the whole pair

Suppose a lifted integral basis $P=[K\ L]$ separates the radical of $B_c\bmod3$ from a nondegenerate complement. Write, for either the exact core matrix or the actual matrix,


$$
P^TBP=
\begin{pmatrix}
A&B_{KL}\\
B_{KL}^T&C
\end{pmatrix},
\qquad C\in\operatorname{GL}(\mathbb Z_3).
$$


Let the radical dimension be $r$. Then


$$
A,B_{KL}\in3M.
$$


Set


$$
R=A-B_{KL}C^{-1}B_{KL}^T=3T,
\tag{4.1}
$$


and transport the endpoint:


$$
P^Te=\binom{e_K}{e_L},\qquad
\eta=e_K-B_{KL}C^{-1}e_L.
\tag{4.2}
$$


For the complete pair, put


$$
c=3^{26}d,\qquad
\gamma=c-e_L^TC^{-1}e_L.
\tag{4.3}
$$



For $r\ge1$, exact block determinant identities give


$$
\det B=(\det P)^{-2}\det C\,3^r\det T,
\tag{4.4}
$$


and


$$
\boxed{
e^T\operatorname{adj}(B)e-c\det B
=
(\det P)^{-2}\det C
\left(
3^{r-1}\eta^T\operatorname{adj}(T)\eta
-\gamma\,3^r\det T
\right).
}
\tag{4.5}
$$



These are polynomial identities and do not require $T$ to be nonsingular.

### Consequences

- A first-layer nullity $r$ gives
  

$$
v_3(D_0)\ge r,\qquad v_3(D_1)\ge r-1,
$$


  but these are lower bounds, not a relative-valuation law.

- If $r=1$ and the endpoint is nonzero on the one-dimensional radical, then $D_1$ is a unit. This follows directly from (4.5), because $\eta\bmod3\ne0$ and the second summand is divisible by $3$.

- If $r\ge2$, both first determinant residues vanish. That does not establish characteristic-zero singularity.

- A rank defect must be followed by the exact Schur operator $T$, the transported endpoint $\eta$, and the updated scalar $\gamma$. Retaining only the radical matrix and discarding $\gamma$ changes the complete cofactor.

This quantifies what a first-layer calculation would actually buy.

---

## 5. A six-digit certificate for $s_c<32$

### Theorem 5.1 — Exact finite-precision decision criterion

Let


$$
B_c=-S_c/3^{26}\in M_\nu(\mathbb Z_3).
$$


Starting from $B_c\bmod3^6$, repeatedly:

1. split its reduction modulo $3$ into its radical and a nondegenerate complement;
2. eliminate the complement by its unit inverse;
3. divide the residual Schur operator by $3$;
4. continue at one fewer digit of precision.

Let $r_k$ be the residual dimension after $k$ such stages. Then:

1. $r_6=0$ if and only if $B_c$ is nonsingular with largest Smith exponent at most $5$;
2. in that case
   

$$
s_c=26+a,\qquad 0\le a\le5,
   \tag{5.1}
$$


   where $a$ is the last level at which a nonzero-dimensional residual remains;
3. if $r_6>0$, the assertion $s_c<32$ is false at this input whenever $s_c$ is defined; otherwise the exact core matrix is singular and $s_c$ is undefined.

#### Proof

Over $\mathbb Z_3$, a symmetric integral matrix admits successive unit-complement elimination because the residue characteristic is not $2$. At each stage, the unit complement accounts for Smith exponents zero at that stage. Dividing the radical Schur operator by $3$ decreases every remaining positive Smith exponent by one.

Thus $r_k$ counts the Smith exponents at least $k$, including any infinite exponents caused by exact singularity. Six digits suffice for these six stages: unit inversion loses no precision, while each normalization loses exactly one digit.

Therefore $r_6=0$ is equivalent to all Smith exponents being finite and at most $5$.

If the Smith exponents of $B_c$ are


$$
0\le a_1\le\cdots\le a_\nu=a,
$$


unimodular equivalence shows


$$
-\min_{i,j}v_3((B_c^{-1})_{ij})=a.
$$


Since $S_c=-3^{26}B_c$, equation (5.1) follows. ∎

If $r_6=0$, the determinant valuation is also certified:


$$
v_3(\det B_c)=\sum_{k=1}^{5}r_k.
\tag{5.2}
$$


This can be much larger than $5$. Nevertheless, it is recoverable from six matrix digits because the computation follows invariant factors rather than attempting to detect a large determinant valuation from $\det B_c\bmod3^6$.

### 5.1 Actual implication

Since


$$
\Theta-B_c\in3^6M,
$$


the certificate $r_6=0$ also protects the actual inverse. If $a\le5$,


$$
\frac{\det\Theta}{\det B_c}\in1+3^{6-a}\mathbb Z_3,
\tag{5.3}
$$


and


$$
\Theta^{-1}-B_c^{-1}\in3^{6-2a}M.
\tag{5.4}
$$



This is a useful conditional conclusion. No such certificate has yet been evaluated on the original family.

---

## 6. Endpoint-sensitive guard precision for $D_1/D_0$

The whole scalar is


$$
\sigma_c=e_c^TB_c^{-1}e_c-3^{26}d_c,
$$




$$
\sigma_{\rm act}
=e_{\rm act}^T\Theta^{-1}e_{\rm act}-3^{26}d_{\rm act}.
\tag{6.1}
$$


When $D_0\ne0$,


$$
\sigma_{\rm act}=D_1/D_0.
$$



### Theorem 6.1 — Directional scalar protection

Assume the certificate of Theorem 5.1 gives $a<6$. Put


$$
z_c=B_c^{-1}e_c,\qquad
u=\max\!\left(0,-\min_i v_3((z_c)_i)\right).
$$


Then $u\le a$, and


$$
\boxed{\sigma_{\rm act}-\sigma_c\in3^{6-2u}\mathbb Z_3.}
\tag{6.2}
$$



Consequently, if


$$
v_3(\sigma_c)<6-2u,
\tag{6.3}
$$


then both scalars are nonzero and


$$
v_3(D_1)-v_3(D_0)=v_3(\sigma_c).
\tag{6.4}
$$



#### Proof

Write $\Delta=\Theta-B_c\in3^6M$. Since $a<6$, the relative inverse exists and


$$
\Theta^{-1}e_c-z_c=-\Theta^{-1}\Delta z_c
\in3^{6-a-u}\mathbb Z_3^\nu.
$$


Because $6-a>0$, both inverse endpoint vectors have valuation at least $-u$. The resolvent identity therefore gives


$$
e_c^T(\Theta^{-1}-B_c^{-1})e_c
=-z_c^T\Delta\Theta^{-1}e_c
\in3^{6-2u}\mathbb Z_3.
$$



The accepted endpoint comparison is


$$
e_{\rm act}-e_c\in3^6\mathbb Z_3^\nu.
$$


Its cross terms with $\Theta^{-1}e_c$ have valuation at least $6-u$, and its quadratic term has valuation at least $12-a$. Both are at least $6-2u$.

Finally,


$$
d_{\rm act}-d_c\in3^4\mathbb Z_3,
$$


so the difference of the subtractions in (6.1) belongs to $3^{30}\mathbb Z_3$. This proves (6.2). The strict inequality (6.3) prevents cancellation of the leading core scalar digit. ∎

This theorem is stronger than applying the worst inverse loss indiscriminately. It still requires an evaluated whole core scalar. A primitive endpoint alone does not imply (6.3).

---

## 7. Relation to the actual denominator and whole error

Retain exactly


$$
D_0=\det\Theta,
$$




$$
D_1=e_{\rm act}^T\operatorname{adj}(\Theta)e_{\rm act}
-3^{26}d_{\rm act}\det\Theta.
\tag{7.1}
$$


With


$$
F=(n-1)!,\qquad Q_{\rm act}(-1)=-F^2\xi_n,\qquad
\xi_n\in1+3\mathbb Z_3,
$$


the accepted ratio is


$$
\frac{\beta_1}{\beta_0}
=\frac{3^{h-26}F^2\xi_n}{4}\frac{D_1}{D_0}.
\tag{7.2}
$$


Thus, when both members are nonzero,


$$
\boxed{
v_3(q)=
\max\left\{
0,\ h-26+2v_3(F)+v_3(D_1)-v_3(D_0)
\right\}.
}
\tag{7.3}
$$


Under Theorem 6.1’s strict scalar guard, the final difference in (7.3) equals $v_3(\sigma_c)$. Otherwise it remains unresolved.

No common matrix depth contributes a dimension-multiplied denominator gain.

For the original least clearing integer $\ell_{\rm clr}$, preserve


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$




$$
g_\ell=\gcd(|A_\ell|,|B_\ell|),
$$


and


$$
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell}.
\tag{7.4}
$$


All original row contents and every prime in the final gcd remain part of this normalization. This report computes none of them and cancels none of them provisionally.

The same-index whole evaluated error remains


$$
\boxed{
q(e+\pi)-p=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}{g_\ell}
\det H_{\rm complete}.
}
\tag{7.5}
$$


Neither its nonvanishing nor its decay has been established.

---

## 8. The smallest useful new bounded calculation

No accepted producer or saturation receipt needs regeneration.

### Stage A: the complete first layer

**Inputs**

- One coordinator-certified original tuple $(j,n,H,D,h)$ satisfying all hypotheses in §1.
- The accepted finite core return data, preserving LOW indices $0,\ldots,D-1$ and HIGH indices $d,\ldots,m$.
- Precision-$25$ corrected representatives $\phi_i=x^D\psi_i$.

**Calculation**

Evaluate only the $D-3$ brackets in (3.2)–(3.3), modulo $3^{27}$, with:

- both corrected representatives;
- every pole $\ell=0,\ldots,26$;
- the original finite $c$-cutoff;
- factorial contribution retained until its valuation is checked;
- whole-bracket divisibility checked before division.

Then compute the finite convolution kernel (3.4) and endpoint restriction (3.5).

**Verifiable output**

1. All $D-3$ normalized residues $\lambda_k$.
2. Zero lower-$26$-digit remainder for each complete bracket.
3. Exact rank and a kernel basis over $\mathbb F_3$.
4. Endpoint values on that basis.
5. Complete forcing consistency, including the actual terminal return.

No nonzero output is predicted. This is the smallest generic moment description supplied here; it is not proved complexity-optimal.

### Stage B: only if the first layer is singular

Lift the **remaining radical operator**, its endpoint, and its scalar subtraction, using at most the six normalized core digits already covered by forgetting.

Expected output is the sequence $r_1,\ldots,r_6$, together with certified unit pivots and transported data. It must report one of:

- $r_6=0$: a certificate of $s_c<32$, its exact value, and the determinant valuation;
- $r_6>0$: a certificate that $s_c<32$ cannot hold at this input if the core is nonsingular;
- insufficient or unverified input precision: no conclusion.

If $r_6=0$, evaluate the whole scalar to the guard in §6. A zero residue at the guard is inconclusive, not scalar vanishing.

One original input has only that finite scope. A family theorem requires a uniform evaluation or structural control of these outputs.

---

## 9. Proof-status ledger

| Claim | Status |
|---|---|
| Turn 13 depth $26$ and actual/core agreement through depth $32$ | Reused under every simultaneous hypothesis and accepted finite-support dependency |
| Complete bracket formula | Reused with both corrected representatives and whole carries |
| Factorial term vanishes modulo $3^{27}$ on this window | Proved by its actual coefficient valuation |
| First normalized core layer is Hankel over $\mathbb F_3$ | Proved from the accepted whole-form normalization |
| $D-3$ complete brackets determine the entire first layer | Proved |
| Finite convolution kernel and actual endpoint action | Explicit and proved |
| Numerical first-layer rank or a surviving moment | Not evaluated |
| Exact radical/complement determinant–cofactor recursion | Proved with the complete scalar subtraction |
| Six-digit criterion for $s_c<32$ | Proved |
| $s_c<32$ on the moving original family | Open |
| Endpoint-sensitive scalar guard | Proved conditionally on inverse certification |
| Actual $D_0,D_1$ nonvanishing and relative valuation | Open unless the specified certificates succeed |
| Original row contents, least clearer, final all-prime gcd | Not evaluated |
| Same-index whole nonzero error tending to zero | Open |
| Rationality or irrationality of $e+\pi$ | Unresolved |

## Conclusion

The new result is not another common-divisibility increment. It is an exact reduction of the **whole normalized core layer** to $D-3$ carry-sensitive bracket values, followed by a six-digit criterion that genuinely decides the inverse threshold at a certified original input.

The immediate mathematical bottleneck is now concrete:


$$
\boxed{
\text{Evaluate the complete moment polynomial }L(X)
\text{ and, if necessary, its successive radical Schur operators.}
}
$$


A support collision does not supply a nonzero coefficient. A first-layer rank defect does not determine the complete pair. Six digits protect the inverse only when the sixth radical disappears; even then, the endpoint scalar must pass its own strict guard.

Beyond this local bottleneck remain the actual all-prime primitive normalization and the whole same-index error (7.5). None is replaced by a raw determinant, a reference quantity, or an isolated pole contribution.



$$
\boxed{\text{No unconditional proof of rationality or irrationality of }e+\pi
\text{ has been obtained.}}
$$


