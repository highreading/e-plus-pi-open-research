> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A3, Turn 7 — Moment–reference reduction with polynomial projection cost, and an exact binary denominator law on an infinite original subfamily

## Executive conclusions

The irrationality or rationality of $e+\pi$ remains unresolved.

This turn gives two new arithmetic results for the retained endpoint construction.

### 1. The remaining projected Wronskian content admits a moment–reference reduction with only a polynomial loss

The structural intersection is already closed and remains closed:


$$
\gcd(G_3,C_3)\mid4(n+1)^2(n+2)^2,
$$




$$
\gcd(G_0,C_0)\mid4(n+1)^2(n+2)^2(n+3).
$$


In particular,


$$
\gcd(G_j,C_j)_{>n+2}=1.
$$



Using **both actual endpoint row equations**, I obtain four explicit moment–reference residuals $\mathcal D_{j,i}$, $j=0,3$, $i=0,1$. They contain the complete inhomogeneous Wronskian


$$
\mathscr K_n=h_nb_{n+1}-h_{n+1}b_n-2(n!)^3
$$


and no factorial seed.

Define


$$
\mathfrak D_j
=
\prod_{\substack{p>n+2\\p\nmid G_j}}
p^{\min\{v_p(R_j),v_p(\mathcal D_{j,0}),v_p(\mathcal D_{j,1})\}}.
$$


Then


$$
\boxed{
\gcd(R_3,C_3)_{>n+2}
\ \mid\ \mathfrak D_3
\ \mid\
(n^2+4n+1)\gcd(R_3,C_3)_{>n+2},
}
\tag{E1}
$$


and


$$
\boxed{
\gcd(R_0,C_0)_{>n+2}
\ \mid\ \mathfrak D_0
\ \mid\
(n^2+6n+4)\gcd(R_0,C_0)_{>n+2}.
}
\tag{E2}
$$



Thus the replacement of the actual projected cancellation by these evaluated moment–reference residuals costs only $O(\log n)$, not an unbounded contact determinant or an unspecified saturation factor.

This is a genuine further reduction of the simultaneous $R,I,J$ congruences. It does **not** yet bound $\log\mathfrak D_j$ by $O(n)$ or $o(n\log n)$.

### 2. The endpoint-$0$ binary calculation can be completed on an infinite original subfamily

Every original index with $n\equiv1\pmod4$ actually satisfies $n\equiv1\pmod8$. On this scope, put


$$
t=v_2(n!),\qquad k=\frac{n-1}{2}.
$$


The actual primitive contact rows satisfy


$$
\boxed{v_2(G_0)=2,\qquad v_2(G_3)=0,}
\tag{E3}
$$


and their reference projections satisfy


$$
\boxed{v_2(R_0)=k+2,\qquad v_2(R_3)=k.}
\tag{E4}
$$


Both complete exterior-corrected exponential projections have the stronger lower bound


$$
\boxed{v_2(r_0\mathbf U)\ge3,\qquad v_2(r_3\mathbf U)\ge3.}
\tag{E5}
$$


Consequently,


$$
\boxed{
v_2(d_0)\le t+k-1,\qquad
v_2(d_3)\le t+k-3.
}
\tag{E6}
$$



On the infinite original subfamily


$$
\boxed{
n=15^{2a}\quad(a\ge1),
\qquad\text{or}\qquad
n=105^{4a}\quad(a\ge1),
}
\tag{E7}
$$


one has $n\equiv1\pmod{32}$, and all these force and denominator bounds become exact:


$$
\boxed{
v_2(r_0\mathbf U)=v_2(r_3\mathbf U)
=v_2(C_0)=v_2(C_3)=3,
}
\tag{E8}
$$




$$
\boxed{
v_2(\gamma_0)=2t-1,\qquad
v_2(\gamma_3)=2t-3,
}
\tag{E9}
$$




$$
\boxed{
v_2(d_0)=t+k-1,\qquad
v_2(d_3)=t+k-3.
}
\tag{E10}
$$



In particular, the binary part of the actual endpoint denominator imbalance is exactly $4$ on (E7). This conclusion comes from the complete numerator and the all-prime primitive denominator factorization; it is not an inference from an unnormalized reference pair.

No program was executed. No accepted producer, selected-prime extraction, or whole-form enclosure is proposed for repetition.

---

## 1. Scope, accepted results, and normalization

The original index domain is unchanged:


$$
n=15^r,\quad r\ge2,
\qquad\text{or}\qquad
n=105^r,\quad r\ge2.
$$



All arguments below retain:

- the original $3\times3$ contact matrix;
- both corrected four-coordinate reconstruction columns;
- the complete force through exactly $2n+2$;
- the terminal return;
- the exterior $+1$;
- the least clearer over all eight reconstructed entries;
- every actual reconstruction row content;
- the actual primitive endpoint rows;
- every prime in the final weighted gcd;
- the actual primitive denominator;
- the whole error at the same original index.

The logarithmic-force identity is used only at its established three-contact-row scope. No assertion about an earlier-index logarithmic recurrence is introduced.

### 1.1 Results retained from Turn 6

I retain the proved terminal normal identity


$$
q_\partial\mathbf C
=
2(n+1)(n+2)\bigl(2a_{n+1}-(n+1)a_n\bigr),
$$


the polynomial structural divisors, and their large-prime exclusion.

I also retain the complete Wronskian


$$
\mathscr K_n
=
h_nb_{n+1}-h_{n+1}b_n+2(-1)^n(n!)^3,
$$


with


$$
(n!)^3<|\mathscr K_n|<3(n!)^3.
$$


All original indices are odd, so its factorial term is $-2(n!)^3$.

This real bound is not used as a primewise exclusion.

### 1.2 Corrections and improvements retained from A4 Turn 9

For


$$
\delta_j=\gcd(|R_j|,|C_j|),\qquad
R_j^*=R_j/\delta_j,\qquad C_j^*=C_j/\delta_j,
$$


the actual endpoint denominator is


$$
\boxed{
d_j=
|R_j^*|\,
\frac{n!}{\gcd\!\left(n!,|E_nR_j^*+C_j^*|\right)}.
}
\tag{1.1}
$$


The seed-dependent multiplier is a divisor of $n!$. Consequently,


$$
\boxed{
v_p(d_j)=\bigl(v_p(R_j)-v_p(C_j)\bigr)_+
\qquad(p>n).
}
\tag{1.2}
$$



The finer $\gamma_j,\mathcal C_j^\sharp$ formulas retain their original $p>n+2$ normalization-unit scope.

I also retain A4’s extra binary factor for $n\equiv3\pmod4$:


$$
v_2(r_3\mathbf U)\ge v_2(n+1)+1,
$$


and hence


$$
v_2(\gamma_3)\le2v_2(n!)-1
$$


on both odd classes. The new binary work below strengthens a different scope, namely the original $n\equiv1\pmod8$ indices.

---

# Part I. Explicit moment–reference reduction

## 2. Terminal coordinates adapted to the endpoint equations

Put


$$
m=n+1,\qquad N=n+2,
$$


and abbreviate


$$
A=a_n,\qquad B=a_{n-1},\qquad D=a_{n+1}.
$$


Define


$$
\boxed{
X=mA,\qquad Y=mnB,\qquad Z=2D-mA.
}
\tag{2.1}
$$



Here $X,Y,Z$ are moment quantities, not reconstruction coordinates or weighted numerator variables.

For an actual primitive endpoint row


$$
r_j=(x_j,y_j,z_j),
$$


write


$$
\alpha_j=r_jv',\qquad \beta_j=r_jw',
$$


where


$$
v'=(2N,N,m)^T,\qquad
w'=(0,N,2n+3)^T.
$$


Thus


$$
G_j=\gcd(\alpha_j,\beta_j).
$$



The change of row coordinates


$$
(x_j,y_j,z_j)\longmapsto(\alpha_j,\beta_j,z_j)
$$


has determinant $2N^2$. It is therefore invertible over $\mathbb Z_p$ for every $p>n+2$.

### 2.1 The two endpoint equations, fully evaluated

For each endpoint define two triples $(P_{j,i},Q_{j,i},F_{j,i})$ by the following table:


$$
\begin{array}{c|c|c|c}
(j,i)&P_{j,i}&Q_{j,i}&F_{j,i}\\ \hline
(3,0)
&X
&Z
&Y-X-(2n+1)Z\\[2mm]
(3,1)
&Y
&2X-Y
&NY-(3n+4)X+NZ\\[2mm]
(0,0)
&nX+Y
&nZ+2X-Y
&2m\bigl(Y-2X-(n-1)Z\bigr)\\[2mm]
(0,1)
&mZ-(n^2+1)X-(n-1)Y
&mY-(n-1)X-m^2Z
&2m\bigl(mX-NY+(n^2+n+1)Z\bigr).
\end{array}
\tag{2.2}
$$



Then the **actual** endpoint rows satisfy


$$
\boxed{
P_{j,i}\alpha_j+Q_{j,i}\beta_j+F_{j,i}z_j=0,
\qquad i=0,1.
}
\tag{2.3}
$$



#### Derivation

Turn 6 gives the exact row identity


$$
2N r_j=(\alpha_j-\beta_j,2\beta_j,0)+z_jq_\partial.
$$


Applying it to a contact column $J_i$, and dividing the resulting identity by $N$, gives coefficients


$$
P_i=\frac{(J_i)_0}{N},\qquad
Q_i=\frac{2(J_i)_1-(J_i)_0}{N},\qquad
F_i=f_i.
$$



For endpoint $3$, the annihilated columns are $J_0,J_1$, immediately giving the first two rows of (2.2).

For endpoint $0$, the annihilated columns are


$$
nJ_0+J_1,\qquad -nmJ_0+J_2.
$$


Substituting the moment recurrence to eliminate $a_{n-2}$ gives the last two rows.

Thus (2.2) is an evaluated consequence of the two original endpoint kernels. It does not divide by the contact determinant.

---

## 3. Reference coordinates and the complete residual

Set


$$
h=h_n=n!\tau_n,\qquad
\ell=n!\tau_{n+1}.
\tag{3.1}
$$


Both are integers on the original domain.

For $\ell$, one may use the constant-term formula for $\tau_{n+1}$: its denominator divides $2^{\lfloor(n+1)/2\rfloor}$, while


$$
v_2(n!)\ge\left\lfloor\frac{n+1}{2}\right\rfloor
$$


for all original $n\ge225$.

The terminal reference relation is


$$
h_{n+1}=\frac m2(h+\ell).
$$


Consequently,


$$
\boxed{
\mathcal R_j:=h\alpha_j+\ell\beta_j=\frac{2R_j}{m}.
}
\tag{3.2}
$$


In particular, $\mathcal R_j$ is integral, and it has the same valuation as $R_j$ at $p>n+2$.

Retain Turn 6’s integral residual decomposition


$$
\mathbf C=S_nv'+T_nw'+mZe_2,
$$


where


$$
S_n=\frac{mb_n}{2}+2n!m!\rho_n,
$$




$$
T_n=b_{n+1}-\frac{mb_n}{2}+2n!m!\rho_{n+1}.
$$


Then


$$
\boxed{
C_j=S_n\alpha_j+T_n\beta_j+mZz_j,
}
\tag{3.3}
$$


and the complete companion identity is


$$
\boxed{
hT_n-\ell S_n=\mathscr K_n.
}
\tag{3.4}
$$



The logarithmic contribution in (3.4) is exactly $-2(n!)^3$ at the original odd indices. It has not been omitted or replaced by an exponential-only residual.

At every $p>n+2$, $h,\ell$ generate the unit ideal in $\mathbb Z_p$, by the retained Legendre companion Wronskian and its denominator scope.

---

## 4. Four evaluated moment–reference residuals

Define


$$
M_{j,i}=Q_{j,i}h-P_{j,i}\ell,
$$


and


$$
\boxed{
\mathcal D_{j,i}
=
mZ\,M_{j,i}-F_{j,i}\mathscr K_n.
}
\tag{4.1}
$$



For example, the endpoint-$3$ pair is


$$
\boxed{
\mathcal D_{3,0}
=
mZ(Zh-X\ell)
-\bigl(Y-X-(2n+1)Z\bigr)\mathscr K_n,
}
\tag{4.2}
$$




$$
\boxed{
\mathcal D_{3,1}
=
mZ\bigl((2X-Y)h-Y\ell\bigr)
-\bigl(NY-(3n+4)X+NZ\bigr)\mathscr K_n.
}
\tag{4.3}
$$



The endpoint-$0$ pair is


$$
\boxed{
\begin{aligned}
\mathcal D_{0,0}
={}&mZ\bigl((nZ+2X-Y)h-(nX+Y)\ell\bigr)\\
&-2m\bigl(Y-2X-(n-1)Z\bigr)\mathscr K_n,
\end{aligned}}
\tag{4.4}
$$




$$
\boxed{
\begin{aligned}
\mathcal D_{0,1}
={}&mZ\Bigl(
\bigl(mY-(n-1)X-m^2Z\bigr)h\\
&\hspace{22mm}
-\bigl(mZ-(n^2+1)X-(n-1)Y\bigr)\ell
\Bigr)\\
&-2m\bigl(mX-NY+(n^2+n+1)Z\bigr)\mathscr K_n.
\end{aligned}}
\tag{4.5}
$$



These are explicit integers in the retained moment, reference, and complete residual data. They are not scalar resultants left to be evaluated.

### 4.1 Integral identities connecting them to $I_j,J_j$

In the present notation,


$$
I_j=\beta_j\mathscr K_n+mhZz_j,
$$




$$
J_j=-\alpha_j\mathscr K_n+m\ell Zz_j.
$$



Using (2.3), direct expansion proves


$$
\boxed{
\alpha_j\mathcal D_{j,i}
=
mZQ_{j,i}\mathcal R_j+F_{j,i}J_j,
}
\tag{4.6}
$$




$$
\boxed{
\beta_j\mathcal D_{j,i}
=
-mZP_{j,i}\mathcal R_j-F_{j,i}I_j,
}
\tag{4.7}
$$




$$
\boxed{
z_j\mathcal D_{j,i}
=
Q_{j,i}I_j-P_{j,i}J_j.
}
\tag{4.8}
$$



All three identities are integral. In particular, the original $m$-factor in Turn 6’s global $J_j$ identity has not been silently canceled.

---

## 5. Exact local projection law

Fix $p>n+2$ with $p\nmid G_j$. Write


$$
r=v_p(R_j),\qquad c=v_p(C_j),\qquad
f=\min_i v_p(F_{j,i}).
$$



### Theorem 5.1

At this scope,


$$
\boxed{
\min\{v_p(R_j),v_p(\mathcal D_{j,0}),v_p(\mathcal D_{j,1})\}
=
\min\{r,c+f\}.
}
\tag{5.1}
$$



This specifies the projection loss exactly: it is the common normal coefficient $F_{j,0},F_{j,1}$, rather than an ambient determinant.

### Proof

If $r=0$, both sides are zero.

Suppose $r>0$. Choose $a,b\in\mathbb Z_p$ with


$$
ah+b\ell=1,
$$


and define


$$
t_j=a\beta_j-b\alpha_j.
$$


Then


$$
\alpha_j=a\mathcal R_j-\ell t_j,\qquad
\beta_j=b\mathcal R_j+ht_j.
$$


Since $\mathcal R_j$ is divisible by $p$ and $G_j$ is a unit, $t_j$ is a unit.

Put


$$
V=aS_n+bT_n.
$$


Equations (3.3)–(3.4) become


$$
C_j=V\mathcal R_j+\mathscr K_n t_j+mZz_j.
$$


Similarly, (2.3) becomes


$$
(aP_{j,i}+bQ_{j,i})\mathcal R_j
+M_{j,i}t_j+F_{j,i}z_j=0.
$$


Eliminating $z_j$ gives the exact local identity


$$
\boxed{
t_j\mathcal D_{j,i}
=
\bigl(F_{j,i}V-mZ(aP_{j,i}+bQ_{j,i})\bigr)\mathcal R_j
-F_{j,i}C_j.
}
\tag{5.2}
$$


Because $t_j$ and $m/2$ are units,


$$
(R_j,\mathcal D_{j,0},\mathcal D_{j,1})
=
(R_j,F_{j,0}C_j,F_{j,1}C_j)
$$


as ideals in $\mathbb Z_p$. This proves (5.1). ∎

The use of a local reference Bézout pair in this proof is legitimate: the reference pair is known to generate the unit ideal at this scope. No factorial-seed unit is invoked.

---

## 6. The normal-coefficient loss is polynomial

The key remaining step in the projection reduction is to bound $f$. Both endpoint equations are needed here.

Define


$$
\boxed{
\Pi_3(n)=n^2+4n+1,\qquad
\Pi_0(n)=n^2+6n+4.
}
\tag{6.1}
$$



### Theorem 6.1

For $p>n+2$ with $p\nmid G_j$,


$$
\boxed{
\min_i v_p(F_{j,i})\le v_p(\Pi_j(n)).
}
\tag{6.2}
$$



### 6.1 Moment primitivity in the present coordinates

At $p>n+2$,


$$
\min\{v_p(X),v_p(Y),v_p(Z)\}=0.
\tag{6.3}
$$


Indeed, common divisibility of $X,Y,Z$ would imply common divisibility of $a_n,a_{n-1},a_{n+1}$; the retained moment recurrence would then also make $a_{n+2}$ divisible by $p$, contradicting the closed primitivity theorem for the consecutive terminal moment triple.

All divisions used here are by units at the stated scope.

### 6.2 Endpoint $3$

Suppose $f>0$. Modulo $p^f$, the two equations $F_{3,0}=F_{3,1}=0$ give


$$
X\equiv NZ,\qquad Y\equiv3mZ.
\tag{6.4}
$$


By (6.3), $Z$ is a unit.

Let


$$
\Delta_3=P_{3,0}Q_{3,1}-P_{3,1}Q_{3,0}.
$$


Its fully evaluated form is


$$
\Delta_3=2X^2-XY-YZ.
$$


Substituting (6.4),


$$
\boxed{
\Delta_3\equiv-\Pi_3(n)Z^2\pmod{p^f}.
}
\tag{6.5}
$$



On the other hand, eliminating $\alpha_3$ or $\beta_3$ between the two actual row equations shows


$$
p^f\mid\Delta_3\alpha_3,\qquad
p^f\mid\Delta_3\beta_3.
$$


Because $G_3$ is a unit, $p^f\mid\Delta_3$.

Equation (6.5), with $Z$ a unit, gives $f\le v_p(\Pi_3(n))$.

### 6.3 Endpoint $0$

Again suppose $f>0$. The two normal equations give


$$
Y\equiv2X+(n-1)Z,
$$




$$
(n+3)X\equiv3Z
\pmod{p^f}.
$$


Here $n+3$ is a unit: since $n$ is odd, every prime divisor of $n+3$ is at most $(n+3)/2<n+2$.

Thus


$$
X\equiv\frac{3Z}{n+3},\qquad
Y\equiv\frac{n^2+2n+3}{n+3}Z
\pmod{p^f},
\tag{6.6}
$$


and $Z$ is a unit by (6.3).

Substitution into


$$
\Delta_0=P_{0,0}Q_{0,1}-P_{0,1}Q_{0,0}
$$


gives


$$
\boxed{
\Delta_0\equiv
-\frac{n\Pi_0(n)}{n+3}Z^2
\pmod{p^f}.
}
\tag{6.7}
$$


For clarity, under (6.6) the coefficients reduce to


$$
P_{0,0}\equiv\frac{n^2+5n+3}{n+3}Z,\qquad
Q_{0,0}\equiv Z,
$$




$$
P_{0,1}\equiv
\frac{-n^3-3n^2+3n+3}{n+3}Z,\qquad
Q_{0,1}\equiv(1-2n)Z.
$$


These give (6.7) directly.

The two actual row equations and $p\nmid G_0$ again imply $p^f\mid\Delta_0$, proving


$$
f\le v_p(\Pi_0(n)).
$$


∎

This theorem bounds the **additional projection cost**. It does not reopen the already eliminated $G_j$-residual intersection.

---

## 7. Global consequence and the precise remaining content problem

Let


$$
\delta_j^{>}
=\gcd(R_j,C_j)_{>n+2}.
$$


The closed structural exclusion says that every prime dividing $\delta_j^{>}$ is prime to $G_j$.

Combining Theorems 5.1 and 6.1 gives


$$
\boxed{
\delta_j^{>}\mid\mathfrak D_j\mid\Pi_j(n)\delta_j^{>}.
}
\tag{7.1}
$$


In logarithmic form,


$$
\boxed{
0\le\log\mathfrak D_j-\log\delta_j^{>}
\le\log\Pi_j(n)=O(\log n).
}
\tag{7.2}
$$



Thus, up to $O(\log n)$, the outstanding large-prime cancellation is exactly the content of the explicit moment–reference residuals (4.2)–(4.5), together with the actual reference projection.

### 7.1 The complete factorial term and the evaluated remainder

Write


$$
w_n=h_nb_{n+1}-h_{n+1}b_n.
$$


Since the original indices are odd,


$$
\boxed{
\mathcal D_{j,i}
=
2F_{j,i}(n!)^3
+
\underbrace{\bigl(mZ M_{j,i}-F_{j,i}w_n\bigr)}_{\mathcal E_{j,i}}.
}
\tag{7.3}
$$



This is the fully evaluated decomposition. It retains the complete logarithmic contribution, the zero-seeded exponential residual, and the exterior subtraction inside $b_k=g_k-a_k$.

The obstruction is now exact:

> A prime can divide the actual reference projection and both integers in (7.3) through congruential cancellation between $2F_{j,i}(n!)^3$ and $\mathcal E_{j,i}$. The fact that $-2(n!)^3$ is a unit at $p>n$, or dominates $w_n$ in the real absolute value, does not exclude this cancellation.

I make no uniform support claim for these integers. Therefore no counterexample built from free triples is being substituted for the actual recurrence. The remaining assertion is an unproved bound for the actual recurrence-generated content.

### 7.2 Sharpened follow-on lemma

A concrete next target is now:

> **Moment–reference residual content lemma.**  
> On an infinite subsequence of $n=15^r$ or $n=105^r$, prove
> 

$$
> \log\mathfrak D_0+\log\mathfrak D_3=O(n)
>
$$


> or, more generally,
> 

$$
> \log\mathfrak D_0+\log\mathfrak D_3=o(n\log n),
>
$$


> with $\mathfrak D_j$ formed from the explicit integers (4.2)–(4.5).

By (7.2), this is equivalent, up to $O(\log n)$, to the desired estimate for the remaining actual large-prime endpoint cancellation. There is no further unknown determinant saturation cost in passing between the two formulations.

The estimate itself remains open.

---

# Part II. Binary endpoint-$0$ normalization and actual denominators

## 8. The relevant original binary classes

On the original domain:

- $15^r\equiv1\pmod8$ when $r$ is even;
- $15^r\equiv7\pmod8$ when $r$ is odd;
- $105^r\equiv1\pmod8$ for every $r$.

Thus every original $n\equiv1\pmod4$ lies in the more restrictive class $n\equiv1\pmod8$. That restriction materially strengthens the binary calculation.

In this part assume


$$
n\equiv1\pmod8,\qquad
m=n+1,\qquad N=n+2,\qquad
t=v_2(n!),\qquad k=\frac{n-1}{2}.
\tag{8.1}
$$


Then $v_2(m)=1$, and $k\equiv0\pmod4$.

---

## 9. Actual primitive endpoint rows

Use


$$
A=a_n,\quad B=a_{n-1},\quad C=a_{n-2},\quad
D=a_{n+1},\quad E=a_{n+2},
$$


and the retained integer contact matrix


$$
J=
\begin{pmatrix}
mNA&nmNB&n(n-1)mNC\\
ND&mNA&nmNB\\
E&ND&mNA
\end{pmatrix}.
$$



Let


$$
\mathscr R_0=(-1,n,-nm)\operatorname{adj}(J).
$$


Its coordinates are divisible by $mN$. Put


$$
\mathscr R_0=mN(X_0,Y_0,Z_0).
$$


Direct expansion gives


$$
\begin{aligned}
X_0={}&-mNA^2+nNBD+n^2BE-nNAD-nND^2+nmAE,\\
Y_0={}&n\bigl(-(n-1)NCD+mNAB+mNA^2\\
&\hspace{20mm}-n(n-1)CE-nmBE+mNAD\bigr),\\
Z_0={}&nN\bigl(-nmB^2+(n-1)mAC+n(n-1)CD\\
&\hspace{20mm}-nmAB-m^2A^2+nmBD\bigr).
\end{aligned}
\tag{9.1}
$$



### 9.1 Exact modular data

The moment polynomial integrality and the binary index period give the following reductions:


$$
\begin{array}{c|ccccc}
n\bmod16&C&B&A&D&E\\ \hline
1&3&1&0&0&1\\
9&7&5&4&4&5
\end{array}
\pmod8.
\tag{9.2}
$$



For completeness, the moment index period modulo $2^s$ is $2^{s+1}$, by the same derivative argument used for the retained force period: in


$$
D^{2^{s+1}}(e^zq(z)^n),
$$


every positive derivative of $q^n$, after factorial normalization and multiplication by its binomial coefficient, is divisible by $2^s$. This uses the already proved coefficient valuation bound and does not require a period $2^s$.

Since $n\equiv1\pmod8$, coefficientwise parameter reduction is to $n=1$, where


$$
a_j(1)=\frac{(j-1)(j-2)}2.
$$


Evaluating this polynomial at the indicated residues yields (9.2).

Substituting into (9.1),


$$
\boxed{
(X_0,Y_0,Z_0)\equiv
\begin{cases}
(1,6,2),&n\equiv1\pmod{16},\\
(5,6,2),&n\equiv9\pmod{16},
\end{cases}
\pmod8.
}
\tag{9.3}
$$



In particular, the raw row content has exactly one factor of $2$. Passing to the actual primitive row divides $(X_0,Y_0,Z_0)$ only by an odd integer, up to sign.

Its reference projections satisfy


$$
\alpha_0\equiv\beta_0\equiv4\pmod8
$$


up to a common odd unit. Hence


$$
\boxed{v_2(G_0)=2.}
\tag{9.4}
$$



### 9.2 Endpoint $3$

The retained raw row is


$$
\mathscr R_3=
\left(
N^2D^2-mNAE,\;
m(nNBE-N^2AD),\;
m(mN^2A^2-nN^2BD)
\right).
$$


Its binary content is exactly $2$. After that division,


$$
\boxed{
\frac{\mathscr R_3}{2}\equiv
\begin{cases}
(0,3,0),&n\equiv1\pmod{16},\\
(4,7,4),&n\equiv9\pmod{16},
\end{cases}
\pmod8.
}
\tag{9.5}
$$


Thus both reference projections are odd:


$$
\boxed{v_2(G_3)=0.}
\tag{9.6}
$$



These are calculations with the actual primitive contact rows. The actual reconstruction row contents are separate quantities and have not been replaced.

---

## 10. Exact binary reference depths

The constant-term formula gives


$$
\tau_{2a}
=
\sum_{j=0}^{a}
\frac{(2a)!}{j!^2(2a-2j)!\,2^j},
$$




$$
\tau_{2a+1}
=
\sum_{j=0}^{a}
\frac{(2a+1)!}{j!^2(2a+1-2j)!\,2^j}.
$$



### 10.1 Odd index $n=2k+1$, with $k$ even

Relative to the terminal summand $j=k$, the summand $j=k-r$ has ratio


$$
\frac{2^r(k)_r^2}{(2r+1)!}.
$$


Its valuation is


$$
2v_2((k)_r)-r+s_2(r).
$$


For $r=1$, this is $2v_2(k)\ge2$. For $r\ge2$, integrality of $\binom{k}{r}$ gives the lower bound


$$
r-s_2(r)\ge1.
$$


Therefore the terminal summand is uniquely of lowest valuation, and


$$
\boxed{v_2(\tau_n)=-v_2(k!).}
\tag{10.1}
$$



### 10.2 Even index $n+1=2(k+1)$, with $k+1\equiv1\pmod4$

Put $a=k+1$. Relative to its terminal summand, the even-index ratios are


$$
\frac{2^r(a)_r^2}{(2r)!}.
$$


The first two summands combine with multiplier


$$
1+a^2,
$$


which has valuation exactly $1$.

For $r=2,3$, the remaining ratios have valuation at least $3$, because $4\mid a-1$. For $r\ge4$, the bound


$$
r-s_2(r)\ge3
$$


suffices. Consequently,


$$
\boxed{
v_2(\tau_{n+1})=-v_2((k+1)!)+1
=-v_2(k!)+1.
}
\tag{10.2}
$$



At both endpoints, the two primitive reference coefficients


$$
\alpha_j/G_j,\qquad\beta_j/G_j
$$


are odd. Since (10.1) and (10.2) differ by exactly one,


$$
v_2(\xi_j)=-v_2(k!).
$$


Using


$$
R_j=\frac{m\,n!}{2}G_j\xi_j
$$


and


$$
v_2(n!)-v_2(k!)=k,
$$


we obtain


$$
\boxed{
v_2(R_0)=k+2,\qquad v_2(R_3)=k.
}
\tag{10.3}
$$



No binary unit assumption about $\tau_n$ has been made.

---

## 11. Complete exponential force and complete residual

For parameter $n=1$, the actual exponential-force coefficients satisfy


$$
u_0(1)=2,
$$


and, for $j\ge1$,


$$
\boxed{
u_j(1)=\frac{j(j+1)}2E_{j-1}+2.
}
\tag{11.1}
$$


This follows directly from the retained force coefficient formula and


$$
E_j=jE_{j-1}+1.
$$



Parameter reduction modulo $8$, together with the valid index period $16$, gives


$$
\begin{array}{c|ccc}
n\bmod16&u_n&u_{n+1}&u_{n+2}\\ \hline
1&3&0&0\\
9&7&0&4
\end{array}
\pmod8.
$$


Hence the complete exterior-corrected exponential vector


$$
\mathbf U=
\bigl(mN(u_n-A),\ N(u_{n+1}-D),\ u_{n+2}-E\bigr)^T
$$


satisfies


$$
\boxed{
\mathbf U\equiv
\begin{cases}
(2,0,7),&n\equiv1\pmod{16},\\
(2,4,7),&n\equiv9\pmod{16},
\end{cases}
\pmod8.
}
\tag{11.2}
$$



Combining (9.3), (9.5), and (11.2),


$$
\boxed{
v_2(r_0\mathbf U)\ge3,\qquad
v_2(r_3\mathbf U)\ge3.
}
\tag{11.3}
$$



For example, the endpoint-$3$ dot products modulo $8$ are


$$
(0,3,0)\cdot(2,0,7)=0,
$$




$$
(4,7,4)\cdot(2,4,7)=64\equiv0.
$$


The endpoint-$0$ dot products are $16$ and $48$, also zero modulo $8$.

### 11.1 Restoring the seed term and the complete logarithmic force

The complete residual is


$$
C_j=r_j\mathbf U-E_nR_j+r_j\mathbf Q.
$$


Since $v_2(R_j)\ge k\ge112$, the seed term is divisible by $16$.

The retained clearer


$$
L=2^{n+1}\operatorname{lcm}(1,\ldots,m)
$$


clears $4\rho_n,4\rho_{n+1}$. If


$$
e=\lfloor\log_2m\rfloor,
$$


then


$$
v_2(\rho_n),v_2(\rho_{n+1})\ge-(n+3+e).
$$


Using


$$
r_j\mathbf Q
=
2n!m!(\alpha_j\rho_n+\beta_j\rho_{n+1}),
$$


we obtain


$$
v_2(r_j\mathbf Q)\ge2t+v_2(G_j)-n-1-e>3
$$


for every original $n\ge225$.

Therefore


$$
\boxed{v_2(C_0)\ge3,\qquad v_2(C_3)\ge3.}
\tag{11.4}
$$


Moreover, whenever $v_2(r_j\mathbf U)=3$, the complete residual also has valuation exactly $3$.

Thus the passage to $C_j$ has included, rather than discarded, the seed subtraction and the complete logarithmic force.

---

## 12. Actual denominator bounds, and exact laws when $n\equiv1\pmod{32}$

From the all-prime factorization (1.1), if $r=v_2(R_j)$ and $c=v_2(C_j)$, then:

- if $c<r$, $v_2(d_j)=t+r-c$;
- if $c\ge r$, $v_2(d_j)\le t$.

Equations (10.3) and (11.4) consequently give


$$
\boxed{
v_2(d_0)\le t+k-1,\qquad
v_2(d_3)\le t+k-3.
}
\tag{12.1}
$$


The exact primitive-triple formula also gives


$$
\boxed{
v_2(\gamma_0)\le2t-1,\qquad
v_2(\gamma_3)\le2t-3
}
\tag{12.2}
$$


on the original $n\equiv1\pmod8$ scope.

### 12.1 Exact force valuation on $n\equiv1\pmod{32}$

Now assume $n\equiv1\pmod{32}$. Modulo $16$, parameter and index reduction give


$$
(C,B,A,D,E)\equiv(3,1,0,0,1),
$$




$$
(u_n,u_{n+1},u_{n+2})\equiv(3,8,0).
$$


The normalized rows and force vector are


$$
(X_0,Y_0,Z_0)\equiv(1,14,10)\pmod{16},
$$




$$
\frac{\mathscr R_3}{2}\equiv(0,3,0)\pmod{16},
$$




$$
\mathbf U\equiv(2,8,15)\pmod{16}.
$$


Their dot products are


$$
1\cdot2+14\cdot8+10\cdot15\equiv8\pmod{16},
$$




$$
0\cdot2+3\cdot8+0\cdot15\equiv8\pmod{16}.
$$


Odd primitive-row divisions preserve these exact valuations. Hence


$$
\boxed{
v_2(r_0\mathbf U)=v_2(r_3\mathbf U)=3.
}
\tag{12.3}
$$



By §11.1,


$$
v_2(C_0)=v_2(C_3)=3.
$$


Since $3<k$, the exact denominator threshold law applies:


$$
\boxed{
v_2(d_0)=t+k-1,\qquad
v_2(d_3)=t+k-3.
}
\tag{12.4}
$$


Similarly,


$$
\boxed{
v_2(\gamma_0)=2t-1,\qquad
v_2(\gamma_3)=2t-3.
}
\tag{12.5}
$$



### 12.2 Infinite original scope

Because


$$
15^2\equiv1\pmod{32},\qquad
105^4\equiv1\pmod{32},
$$


the exact laws hold on


$$
n=15^{2a},\quad a\ge1,
\qquad\text{and}\qquad
n=105^{4a},\quad a\ge1.
$$



If $h_{\rm end}=\gcd(d_0,d_3)$, then


$$
\boxed{
v_2\!\left(\frac{d_0d_3}{h_{\rm end}^2}\right)=2.
}
\tag{12.6}
$$


Thus the binary contribution to the actual endpoint imbalance is exactly $4$.

This is not a claim about the final weighted gcd: a chosen weight can still interact with the retained weight-dependent factors.

The full endpoint-$0$ binary classification for the remaining original class $n=15^{2a+1}\equiv7\pmod8$ is not completed here. A4’s accepted endpoint-$3$ improvement remains valid there.

---

# Part III. Complete reconstruction, final gcd, and whole error

## 13. Both four-coordinate columns remain unchanged

With


$$
x=T^{-1}(n!t),\qquad y=T^{-1}\widehat w,
$$


and


$$
S=
\begin{pmatrix}
1&-n&n(n+1)\\
0&1&-2n\\
0&0&1
\end{pmatrix},
$$


write $sx=Sx$, $sy=Sy$. The retained columns are


$$
u=
\bigl(-sx_0,\ sx_0-sx_1,\ sx_1-sx_2,\ sx_2\bigr),
$$




$$
v=
\bigl(1-sy_0,\ sy_0-sy_1,\ sy_1-sy_2,\ sy_2\bigr).
$$


The exterior $+1$ remains in the first coordinate of the second column.

The least clearer is still taken over all eight entries, and each reconstructed row is reduced by its actual two-entry content.

At $n=3375$, the accepted actual row contents remain


$$
(113940000,\ 9780750,\ 10125,\ 1).
$$


No new endpoint identity changes them.

## 14. The final all-prime weighted normalization

For a reduced weight $\lambda=a/k_{\rm wt}$, retain the original notation


$$
J_{\rm wt}=B_{\rm wt}\widetilde v_0-A_{\rm wt}\widetilde v_3,
$$




$$
T_{\rm wt}=aJ_{\rm wt}+k_{\rm wt}A_{\rm wt}\widetilde v_3,
$$




$$
F_{\rm gcd}
=
\gcd(|A_{\rm wt}|,|a|)
\gcd(|B_{\rm wt}|,|a-k_{\rm wt}|),
$$




$$
G_{\rm wt}=\gcd(k_{\rm wt},|J_{\rm wt}|),
$$




$$
H_{\rm gcd}
=
\gcd\!\left(
h_{\rm end},
\frac{|T_{\rm wt}|}{F_{\rm gcd}G_{\rm wt}}
\right).
$$


Then


$$
\boxed{
q_\lambda=
\frac{k_{\rm wt}h_{\rm end}|A_{\rm wt}B_{\rm wt}|}
{F_{\rm gcd}G_{\rm wt}H_{\rm gcd}},
\qquad
p_\lambda=
\operatorname{sgn}(A_{\rm wt}B_{\rm wt})
\frac{T_{\rm wt}}{F_{\rm gcd}G_{\rm wt}H_{\rm gcd}}.
}
\tag{14.1}
$$



Every prime remains in this normalization.

The whole same-index error is still


$$
\boxed{
q_\lambda(e+\pi)-p_\lambda
=
q_\lambda e_3\alpha_{n,2}(\lambda-\Lambda_{n,2}).
}
\tag{14.2}
$$



The accepted five whole-form enclosures at $3375$ remain finite evidence: all five forms are nonzero and have absolute value greater than $1$. They are neither repeated nor promoted to an infinite-family conclusion.

---

# Part IV. Bounded exact arithmetic and proof status

## 15. New checks available from the archived $3375$ entries

No computation is needed for the symbolic theorems above.

If the coordinator wants a new bounded certificate for Part I, it can use the existing $3375$ artifact without regenerating the producer or any force.

### Inputs

- archived $T$, giving the actual primitive contact rows;
- archived terminal moment coefficients;
- archived $\tau_n,\tau_{n+1},\rho_n,\rho_{n+1}$;
- archived $E_n$ and exponential-force coefficients;
- the complete terminal columns.

Recover


$$
a_s=s!\,\texttt{moment}_s,\qquad
u_s=s!\,\texttt{omega}_s,
$$


and


$$
b_s=u_s-E_nh_s-a_s,\qquad s=n,n+1.
$$


This is exact subtraction from archived entries, not force regeneration.

### Expected verifiable outputs

1. **Four zero endpoint-equation residuals**
   

$$
P_{j,i}\alpha_j+Q_{j,i}\beta_j+F_{j,i}z_j=0.
$$



2. **Zero residuals in the new integral identities**
   

$$
\alpha_j\mathcal D_{j,i}
   -mZQ_{j,i}\mathcal R_j-F_{j,i}J_j=0,
$$


   

$$
\beta_j\mathcal D_{j,i}
   +mZP_{j,i}\mathcal R_j+F_{j,i}I_j=0,
$$


   

$$
z_j\mathcal D_{j,i}
   -Q_{j,i}I_j+P_{j,i}J_j=0.
$$



3. **The new polynomial projection-cost divisibilities**, after retaining only primes $p>3377$ not dividing $G_j$:
   

$$
\gcd(F_{3,0},F_{3,1})_{\rm retained}
   \mid 11\,404\,126,
$$


   

$$
\gcd(F_{0,0},F_{0,1})_{\rm retained}
   \mid 11\,410\,879.
$$



4. The new $\mathfrak D_j$ values, or exact divisor certificates for them.

   The already accepted large-prime $\gamma_j,\mathcal C_j^\sharp$ data, together with the closed structural theorem, imply
   

$$
\gcd(R_j,C_j)_{>3377}=1
$$


   at this finite index. Therefore the new outputs must satisfy
   

$$
\boxed{
   \mathfrak D_3\mid11\,404\,126,\qquad
   \mathfrak D_0\mid11\,410\,879.
   }
$$


   No claim that either new integer equals $1$ is made before evaluation.

These are new identity and gcd postprocessings. They do not repeat the accepted selected valuations, actual denominator calculation, or whole-form enclosures.

The binary theorems in Part II are symbolic. They require no new original-index producer and no repetition of the accepted $225$ calculation.

---

## 16. Status ledger

| Statement | Status |
|---|---|
| Complete terminal normal residual | Retained proved theorem |
| Polynomial divisors for $\gcd(G_j,C_j)$ | Retained proved theorem |
| Large-prime structural residual exclusion | Retained proved theorem |
| Complete inhomogeneous $\mathscr K_n$ and its real bound | Retained proved theorem |
| All-prime primitive endpoint denominator factorization | Retained audited theorem |
| Seed-free denominator law at every $p>n$ | Retained exact scope improvement |
| A4’s extra binary endpoint-$3$ factor on $n\equiv3\pmod4$ | Retained theorem |
| Evaluated endpoint equations (2.2)–(2.3) | **New proof** |
| Four moment–reference residuals and integral projection identities | **New proof** |
| Exact local law (5.1) | **New theorem** |
| Polynomial projection costs $\Pi_3,\Pi_0$ | **New theorem** |
| Comparison $\delta_j^{>}\mid\mathfrak D_j\mid\Pi_j\delta_j^{>}$ | **New theorem** |
| $O(n)$ or $o(n\log n)$ bound for $\log\mathfrak D_0+\log\mathfrak D_3$ | Open |
| Endpoint-$0$ binary row and reference depths on original $n\equiv1\pmod8$ | **New exact theorem** |
| Complete force lower bounds and actual binary denominator bounds there | **New theorem** |
| Exact binary denominator laws on $n=15^{2a}$, $105^{4a}$ | **New infinite-family theorem** |
| Full endpoint-$0$ binary classification on original $n\equiv7\pmod8$ | Open |
| Infinite all-prime denominator versus whole-error comparison | Open |
| Irrationality or rationality of $e+\pi$ | Unresolved |

---

## Conclusion

The remaining projected content has now been reduced beyond Turn 6’s $R,I,J$ formulation.

The two actual endpoint equations produce four explicitly evaluated moment–reference residuals. Their projection loss is controlled by the small polynomials


$$
n^2+4n+1,\qquad n^2+6n+4:
$$




$$
\boxed{
\gcd(R_j,C_j)_{>n+2}
\mid\mathfrak D_j
\mid\Pi_j(n)\gcd(R_j,C_j)_{>n+2}.
}
$$


Thus the residual-content problem has been transferred with an $O(\log n)$ cost, not with an unknown determinant or row-saturation loss.

There is also an unconditional infinite-family binary denominator result:


$$
\boxed{
v_2(d_0)=v_2(n!)+\frac{n-3}{2},\qquad
v_2(d_3)=v_2(n!)+\frac{n-7}{2}
}
$$


for


$$
n=15^{2a}\quad\text{or}\quad n=105^{4a}.
$$


These formulas use the actual primitive rows, exact reference depths, complete force valuation, and actual all-prime endpoint denominator.

The exact remaining arithmetic bottleneck is a sufficiently small infinite-family bound for the recurrence-generated moment–reference content $\mathfrak D_0\mathfrak D_3$. Its factorial term and smaller real remainder can still cancel modulo large primes; neither dominance nor nonvanishing excludes that event.

After that content problem is resolved, one must still combine the uncovered local costs and all weight-dependent gcd factors with the whole nonzero same-index error in (14.2).



$$
\boxed{\text{No unconditional proof or disproof of the irrationality of }e+\pi
\text{ has been obtained.}}
$$


