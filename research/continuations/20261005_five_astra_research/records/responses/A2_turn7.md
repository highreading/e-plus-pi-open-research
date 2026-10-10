> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2 turn 7: the divided cross carry factors through the leading norm sum

I obtain a symbolic formula for the next carry at the **original indices**


$$
n=2001\,3^a,\qquad b=3^a,\qquad a\ge1,\qquad m_w=1.
$$


It explains the supplied value $5$ at $a=3$, without assuming that value persists.

The two main formulas on the candidate $23$-class $a\equiv3\pmod{11}$ are


$$
\boxed{\frac{\Xi}{23}\equiv J\,\mathcal S\pmod{23},
\qquad
\mathfrak D\equiv6J^2\mathcal S\pmod{23}.}
\tag{1}
$$


Here $J$ and $\mathcal S$, defined below, depend on the higher digits of the **same** $n,b$. Thus the carry is not a fixed factorial unit.

At $29$, I prove that **none** of the constant-term digit factors vanishes. On $a\equiv3\pmod{28}$, the corresponding formulas are again


$$
\boxed{\frac{\Xi}{29}\equiv J\,\mathcal S\pmod{29},
\qquad
\mathfrak D\equiv6J^2\mathcal S\pmod{29}.}
\tag{2}
$$


The remaining first-layer obstruction at $29$ is therefore the norm sum $\mathcal S$, not $J$.

I do **not** prove that the unit conditions in (1) or (2) hold on an infinite exponent class. To address common $P$-content without a digit-distribution assumption, I also prove an unconditional logarithmic bound for the content of the entire weighted $P$-column:


$$
\boxed{
\min_j v_p(Z_{w,j})\le 2\lfloor\log_p(n+2)\rfloor,
\qquad p\in\{23,29\}.
}
\tag{3}
$$


This separates a controllable common-content loss from the still-uncontrolled primitive cross-versus-norm cancellation.

No decision concerning the irrationality of $e+\pi$ follows.

---

## 1. Setup and the precise new carry statement

I retain the actual construction and its complete residual:


$$
\lambda=\frac{(n!)^2}{2^n},\qquad
Z_w=\operatorname{diag}((n+2)_j)\,z,\qquad
V_w=\operatorname{diag}((n+2)_j)\,v,
$$




$$
\mathfrak D=Z_w^TZ_w,\qquad
\mathfrak C=Z_w^TV_w,\qquad
Y=\frac{V_w}{b!},\qquad
\Xi=\frac{\mathfrak C}{b!}=Z_w^TY.
\tag{4}
$$


The exact center is


$$
c_n=\frac{\mathfrak C}{\lambda\mathfrak D}.
$$



The previously proved local integrality and complete residual identities are reused, not claimed as new. In particular, at $p=23,29$,


$$
\widetilde N=B(n)+nC,\qquad C\in M_b(\mathbb Z),
$$


and $\widetilde N$ is a $p$-adic unit matrix. Both actual $B$-lift columns are $p$-integral, so


$$
v_p(d_B)=0.
\tag{5}
$$



Write, for either prime,


$$
n=pN,\qquad b=pB+r,\qquad 3\le r<p.
\tag{6}
$$


On the original family $p\nmid N$ and $p\nmid b$.

Define


$$
J=\operatorname{CT}(t^{-1}+2+2t)^n\pmod p,
$$




$$
A_H=\binom{2N+H}{H},\qquad
\mathcal S=\sum_{q=0}^{B}\binom Nq^2 A_{B-q}^{\,2}\pmod p.
\tag{7}
$$



For $s=0,1,2$, put


$$
L_{r,s}
=
\sum_{t=r}^{p-1}
t!\,\frac{(-1)^{t-s-1}}{t-s}
\quad\text{in }\mathbb F_p,
$$


and


$$
\eta_{p,r}=1-5L_{r,0}+6L_{r,1}-L_{r,2}.
\tag{8}
$$


All denominators in these sums are nonzero modulo $p$, since $t\ge r\ge3>s$.

### Divided-cross carry theorem

At the original indices, for $p=23$ or $29$ and $r\ge3$,


$$
\boxed{
\frac{\Xi}{p}
\equiv
\frac{-2N\,(-1)^B\,\eta_{p,r}}{r!}\,
J\,\mathcal S
\pmod p.
}
\tag{9}
$$


At the same indices,


$$
\boxed{\mathfrak D\equiv6J^2\mathcal S\pmod p.}
\tag{10}
$$



The division in (9) is valid because the established first layer gives $Y\equiv0\pmod p$. The proof below keeps the contact correction, shifted inverse, factorial-block carry, actual weights, endpoint, and complete logarithmic forcing. Some contributions cancel or vanish after projection; they are not omitted by assumption.

---

## 2. Derivation of the second carry

Let


$$
\mathsf T(x)_{ij}=\binom{x}{j-i}
$$


be the finite upper-triangular binomial-shift matrix, and let $P$ be the Pascal matrix. Thus


$$
B(n)=P\mathsf T(n).
$$


The divided reconstruction before multiplication by $z-1$ is $\mathsf T(-n)$.

Set


$$
R^{\rm res}=\rho/b!,
\qquad
t=\mathsf T(-n)\widetilde N^{-1}R^{\rm res}.
\tag{11}
$$


For $j<b$,


$$
Y_j=\binom{n+2}{j}(jt_{j-1}-t_j),
\tag{12}
$$


with $t_{-1}=0$. The exact terminal term remains present at $j=b$.

### 2.1 The whole logarithmic residual is beyond the required precision

The inherited whole-coefficient bound gives


$$
v_p(h_i^F/b!)
\ge
v_p(n!)-v_p(b!)
-\lfloor\log_p(2n+b-1)\rfloor.
\tag{13}
$$


For $p=23,29$ and $b=3^a\ge3$, this is greater than $2$. For example,


$$
v_p(n!)-v_p(b!)\ge
\left\lfloor\frac{2000b}{p}\right\rfloor,
$$


which already dominates the logarithmic term.

Consequently the **complete** residual modulo $p^2$ can be evaluated using its exponential expression, with (13) certifying that the complete logarithmic part cannot change this carry.

### 2.2 The contact correction after the Pascal transform

Write


$$
a_s(n)=[z^s]\phi(z)^n,\qquad \phi(z)=1-z+z^2/2,
$$


and, for $1\le s<p$,


$$
\ell_s=[z^s]\log\phi(z)\pmod p.
$$


Then


$$
a_s(n)/p\equiv N\ell_s\pmod p,\qquad
a_p(n)\equiv-N\pmod p.
\tag{14}
$$



The Newton-difference identity


$$
\begin{aligned}
&\Delta_i^k\left((n+i)_s\binom{n+i-s}{j}\right)\bigg|_{i=0}\\
&\qquad=
\sum_{h=0}^{\min(s,k)}
\binom sh(k)_h(n)_{s-h}
\binom{n-s+h}{j-k+h}
\end{aligned}
\tag{15}
$$


follows by applying $D_z^s$ to $z^k(1+z)^n$.

Terms with $s>p$ vanish modulo $p^2$, by the established bound


$$
v_p\!\left(a_s(n)(n+i)_s\right)
\ge1+v_p((s-1)!).
$$


For $s<p$, only $h=s$ survives after division by $p$. For $s=p$, only $h=0,p$ can survive. If $k=pq+u$, then


$$
(n)_p/p\equiv-N,\qquad (k)_p/p\equiv-q\pmod p.
$$


It follows that


$$
P^{-1}\widetilde N\equiv\mathsf T(n)+pE\pmod{p^2},
\tag{16}
$$


where


$$
\boxed{
\begin{aligned}
E_{kj}={}&
N\sum_{s=1}^{p-1}\ell_s(k)_s
             \binom n{j-k+s}\\
&+Nq\binom n{j-k+p}
+N^2\binom{n-p}{j-k}
\pmod p.
\end{aligned}}
\tag{17}
$$



This is the contribution of the actual $nC$ correction; it has not been replaced by zero.

### 2.3 Why this contact correction does not survive in the supported cross carry

The leading weighted $P$-column is supported only at indices with low digit $0,1,2$. Consider rows $k$ having one of these low digits.

In (17), $(k)_s\not\equiv0\pmod p$ requires $s\le k\bmod p$. Lucas reduction then shows that every nonzero $E_{kj}$ has


$$
j\bmod p\le k\bmod p\le2.
\tag{18}
$$


Thus $E$ preserves the low-digit-$\{0,1,2\}$ row subsystem.

For the $s=0$ part of the residual, its Newton transform is


$$
R_k^0
=
\sum_{t\ge b}\frac{t!}{b!}\binom{2n}{t-k}.
\tag{19}
$$


Modulo $p$, only $b\le t<b+p-r$ matters, and these $t$ have low digits at least $r$. Hence


$$
R_k^0=0\pmod p
\quad\text{when }k\bmod p\le2.
\tag{20}
$$


Both $\mathsf T(-n)$ and $\mathsf T(-2n)$ preserve low digits modulo $p$.

The $s\ge1$ residual correction has exactly the expression (17) with the binomial upper arguments $n,n-p$ replaced by $2n,2n-p$, acting on the tail coefficients $t!/b!$. The same digit test makes it zero in the rows $k\bmod p\le2$.

Therefore, on these rows, the two corrections


$$
p\,\mathsf T(-2n)G,\qquad
-p\,\mathsf T(-2n)E\mathsf T(-n)R^0
$$


both vanish modulo $p^2$. In particular,


$$
\boxed{
t_k\equiv
\bigl(\mathsf T(-2n)R^0\bigr)_k\pmod{p^2},
\qquad k\bmod p\le2.
}
\tag{21}
$$



This proves the relevant disappearance of the contact and nonconstant residual corrections. It is a support-and-operator argument, not an amplitude lower bound.

### 2.4 The shifted inverse and the second factorial block

Finite binomial convolution gives, for $j<b$,


$$
\begin{aligned}
\bigl(\mathsf T(-2n)R^0\bigr)_j
={}&-\sum_{d\ge0}\frac{(b+d)!}{b!}\\
&\quad\cdot
\sum_{k=0}^{d}
\binom{-2n}{b-j+k}\binom{2n}{d-k}.
\end{aligned}
\tag{22}
$$


This is the exact boundary term from truncating the inverse shift.

Set


$$
j=pq+s,\quad s=0,1,2,\qquad H=B-q,\qquad X=-2N,
$$


and


$$
K_H=X\binom{X-1}{H}.
$$


There are two contributions modulo $p^2$:

* **First factorial block:** $0\le d<p-r$. Here $(b+d)!/b!$ is a unit. The relevant divided binomial is
  

$$
\frac1p\binom{pX}{pH+u}
  \equiv
  \frac{X(-1)^{u-1}}u\binom{X-1}{H},
  \qquad 1\le u<p.
  \tag{23}
$$



* **Second factorial block:** only $d=p+s-r$ can contribute to this row after division by $p$. Its factorial quotient is
  

$$
\frac1p\frac{(b+p+s-r)!}{b!}
  \equiv-\frac{(B+1)s!}{r!}\pmod p.
  \tag{24}
$$


  If $p\mid B+1$, this correctly becomes zero.

Equations (21)–(24) yield


$$
\boxed{
\frac{t_{pq+s}}p
\equiv
-\frac{K_H}{r!}L_{r,s}
+\frac{(B+1)s!}{r!}\binom X{H+1}
\pmod p,\qquad s=0,1,2.
}
\tag{25}
$$



The second factorial block is essential: it supplies the second term of (25).

### 2.5 Actual weighted multiplication and the cross contraction

For $r\ge3$, the leading weighted $P$-coordinates are


$$
\boxed{
(Z_{w,pq},Z_{w,pq+1},Z_{w,pq+2})
\equiv
J(-1)^q\binom Nq A_H(-1,2,-1).
}
\tag{26}
$$


The norm formula (10) follows immediately.

For the $Q$-column, one additional boundary contribution occurs at low digit zero. The established first residual layer gives


$$
t_{p(q-1)+p-1}\equiv\frac1{r!}\binom X{H+1}\pmod p.
\tag{27}
$$


Thus, writing $t_s^{(1)}=t_{pq+s}/p$, the divided unweighted multiplication terms are


$$
M_0=\frac q{r!}\binom X{H+1}-t_0^{(1)},\quad
M_1=t_0^{(1)}-t_1^{(1)},\quad
M_2=2t_1^{(1)}-t_2^{(1)}.
\tag{28}
$$



The first-order carries of the weights themselves multiply a zero zeroth-order multiplication term at these coordinates, so they contribute zero to $\Xi/p$. Outside these coordinates, $Z_w\equiv0\pmod p$, while $Y\equiv0\pmod p$; hence those coordinates also contribute zero to $\Xi/p$. The endpoint $j=b$, whose low digit is $r\ge3$, is covered by this latter statement.

The three supported coordinates contribute the combination


$$
-M_0+4M_1-M_2
=
5t_0^{(1)}-6t_1^{(1)}+t_2^{(1)}
-\frac q{r!}\binom X{H+1}.
$$


Using (25) and


$$
(H+1)\binom X{H+1}=K_H
$$


reduces this to


$$
\frac{K_H}{r!}\eta_{p,r}.
$$


Finally,


$$
K_H=-2N(-1)^H A_H,\qquad q+H=B,
$$


which proves (9).

---

## 3. The original $23$-class containing $a=3$

Take


$$
a\equiv3\pmod{11}.
$$


Then


$$
r=4,\qquad N=87b\equiv3\pmod{23},
$$


and $B$ is odd.

The finite coefficient in (8) is


$$
\eta_{23,4}=4.
\tag{29}
$$


Here is a short exact evaluation. With $a_k=(-1)^k k!$,


$$
L_{r,1}=a_{r-2}+1,\qquad
L_{r,2}=L_{r,0}+2a_{r-3}+1,
$$


so


$$
\eta_{p,r}
=
6-6L_{r,0}+6a_{r-2}-2a_{r-3}.
\tag{30}
$$


At $p=23,r=4$,


$$
L_{4,0}=\sum_{k=3}^{21}(-1)^k k!\equiv18,
\quad a_2=2,\quad a_1=-1,
$$


and (30) gives $4$.

Since $4!\equiv1\pmod{23}$, (9) becomes precisely


$$
\boxed{
\Xi/23\equiv J\mathcal S,\qquad
\mathfrak D\equiv6J^2\mathcal S\pmod{23}.
}
\tag{31}
$$



At $a=3$,


$$
N=2349,\qquad B=1,\qquad
J=10,\qquad
\mathcal S=(2N+1)^2+N^2\equiv7^2+3^2=12.
$$


Therefore


$$
\Xi/23\equiv10\cdot12=5,\qquad
\mathfrak D\equiv6\cdot10^2\cdot12=1\pmod{23},
$$


recovering the supplied direct control.

### Exact scope of the resulting quotient law

If, at an exponent in this class,


$$
J\mathcal S\ne0\pmod{23},
\tag{32}
$$


then


$$
v_{23}(\Xi)=1,\qquad v_{23}(\mathfrak D)=0,
$$


and consequently


$$
\boxed{
v_{23}(q_n)
=
2v_{23}(n!)-v_{23}(b!)-1.
}
\tag{33}
$$



But (32) is not proved on an infinite set of these exponents.

The $J$-obstruction is exact: its digit factor vanishes when the base-$23$ expansion of $2001\,3^a$ contains $7$ or $15$. Fixing $a\bmod11$, or fixing finitely many further congruences on $a$, does not control all higher digits. I do not assume an unproved distribution statement for powers of $3$.

Even when $J$ is a unit, $\mathcal S$ can be a separate obstruction. Formula (31) then proves only the balanced first-zero statement


$$
\mathfrak D\equiv0\pmod{23}
\iff
\Xi/23\equiv0\pmod{23}.
\tag{34}
$$


It does not permit subtraction of two lower valuation bounds.

---

## 4. The other fixed divisor: no zero digits at $29$

Let


$$
C_d=\operatorname{CT}(t^{-1}+2+2t)^d.
$$


The recurrence


$$
dC_d=(4d-2)C_{d-1}+4(d-1)C_{d-2}
\tag{35}
$$


gives, modulo $29$,


$$
\boxed{
(C_0,\ldots,C_{14})
=
(1,2,8,3,20,12,14,2,13,24,22,21,21,20,6).
}
\tag{36}
$$


Every entry is nonzero.

Legendre reflection, in the already used normalization, gives


$$
C_d\equiv(-4)^{d-14}C_{28-d}\pmod{29},
\qquad 15\le d\le28.
\tag{37}
$$


The multiplier is always a unit. Therefore


$$
\boxed{C_d\ne0\pmod{29}\quad\text{for every }0\le d<29.}
\tag{38}
$$



By the constant-term digit factorization,


$$
\boxed{
\operatorname{CT}(t^{-1}+2+2t)^m\ne0\pmod{29}
\quad\text{for every integer }m\ge0.
}
\tag{39}
$$


In particular, $J$ is a $29$-unit at **every original index**. This is an infinite conclusion proved by the digit factorization and the bounded recurrence, not by sampling powers of $3$.

### 4.1 A same-index $29$-carry class

Since $3$ has order $28$ modulo $29$, take


$$
a\equiv3\pmod{28}.
$$


Then


$$
r=27,\qquad N=69b\equiv7\pmod{29},
$$


and $B$ is even.

Formula (30) gives


$$
\eta_{29,27}=2.
\tag{40}
$$


For verification,


$$
L_{27,0}=a_{26}+a_{27}=14-1=13,
\quad a_{25}=24,\quad a_{24}=6,
$$


so


$$
6-6\cdot13+6\cdot24-2\cdot6\equiv2\pmod{29}.
$$


Also $27!\equiv1\pmod{29}$, and $-2N\eta\equiv-28=1$. Hence


$$
\boxed{
\Xi/29\equiv J\mathcal S,\qquad
\mathfrak D\equiv6J^2\mathcal S\pmod{29}.
}
\tag{41}
$$



Since $J$ is always a unit here, the sole first-layer condition is


$$
\mathcal S\ne0\pmod{29}.
$$


Whenever it holds,


$$
\boxed{
v_{29}(q_n)
=
2v_{29}(n!)-v_{29}(b!)-1.
}
\tag{42}
$$



I have not proved this norm-unit condition on an infinite exponent class. Whole-$P$ normalization cannot by itself turn a vanishing quadratic contraction into a unit.

### 4.2 A new prediction at the original $a=3$

At


$$
(n,b)=(54027,27),
$$


we have $B=0$, so $\mathcal S=1$. The base-$29$ digits of $n$ are


$$
(0,7,6,2)_{29}.
$$


Thus


$$
J=C_7C_6C_2\equiv2\cdot14\cdot8=21,
$$


and (41) predicts


$$
\boxed{
\mathfrak D\equiv7\pmod{29},\qquad
\Xi/29\equiv21\pmod{29}.
}
\tag{43}
$$


Since


$$
v_{29}(n!)=1863+64+2=1929,\qquad v_{29}(27!)=0,
$$


this predicts the finite actual denominator depth


$$
\boxed{v_{29}(q_{54027})=3857.}
\tag{44}
$$


An independent direct check is requested at the end.

---

## 5. A logarithmic bound robust to whole-$P$ content

The first-carry theorem does not control deeper simultaneous zeros. The following independent lemma shows that an arbitrarily deep scalar $J$-zero cannot be treated as arbitrarily deep common content of the entire weighted $P$-column.

Let


$$
\kappa_p=\min_{0\le j\le b}v_p(Z_{w,j}),
\qquad p=23\text{ or }29.
\tag{45}
$$



### Theorem
At every original index $a\ge1$,


$$
\boxed{
0\le\kappa_p
\le
\lfloor\log_p(n+1)\rfloor+
\lfloor\log_p(n+2)\rfloor.
}
\tag{46}
$$


At $29$, the stronger bound


$$
\boxed{\kappa_{29}\le\lfloor\log_{29}(n+2)\rfloor}
\tag{47}
$$


holds.

### 5.1 An adjacent constant-term Bézout identity

Choose $\delta^2=-4$. Then


$$
C_m=\delta^mP_m(2/\delta).
$$


Define the polynomial second solution


$$
R_m(x)=
\sum_{k=1}^{m}\frac1kP_{k-1}(x)P_{m-k}(x),
\qquad R_0=0,
$$


and


$$
V_m=\delta^{m-1}R_m(2/\delta).
$$


Its denominators divide


$$
\operatorname{lcm}(1,\ldots,m)
$$


up to powers of $2$. Indeed, the product in each summand has total Legendre index $m-1$; scaling by $\delta^{m-1}$ leaves an element of $\mathbb Z[1/2]$.

The generating function


$$
\sum_{m\ge0}R_m(x)t^m
=
\frac1{\sqrt{1-2xt+t^2}}
\int_0^t\frac{ds}{\sqrt{1-2xs+s^2}}
$$


shows that $R_m$ satisfies the Legendre recurrence for $m\ge2$, with $R_0=0,R_1=1$. Its Wronskian with $P_m$ is therefore


$$
P_nR_{n+1}-P_{n+1}R_n=\frac1{n+1}.
$$


After scaling,


$$
\boxed{
C_nV_{n+1}-C_{n+1}V_n=\frac{(-4)^n}{n+1}.
}
\tag{48}
$$



Because $p\mid n$, the right side is a $p$-unit. Since


$$
v_p(V_n),v_p(V_{n+1})
\ge-\lfloor\log_p(n+1)\rfloor,
$$


equation (48) proves


$$
\boxed{
\min\{v_p(C_n),v_p(C_{n+1})\}
\le\lfloor\log_p(n+1)\rfloor.
}
\tag{49}
$$



### 5.2 The first two actual forcing coordinates detect this pair

The actual $P$-forcing begins with


$$
f_0^0=C_n.
$$


Symmetry of the Laurent coefficients gives


$$
\operatorname{CT}\bigl(tW^n\bigr)=\frac{C_{n+1}-2C_n}{4},
$$


hence


$$
f_1^0=(n+1)\frac{C_{n+1}+2C_n}{4}.
\tag{50}
$$


At $p=23,29$, the change between $(f_0^0,f_1^0)$ and $(C_n,C_{n+1})$ is invertible over $\mathbb Z_p$. Thus the content of the entire $f^0$-column is at most the bound in (49).

Both $\widetilde N^{-1}$ and $\mathsf T(-n)$ are unimodular over $\mathbb Z_p$; consequently the divided reconstructed $P$-column has the same content as $f^0$.

Multiplication by $z-1$ in divided coordinates,


$$
a_j=jt_{j-1}-t_j,
$$


also preserves content: the recurrence


$$
t_j=-a_j+jt_{j-1}
$$


is an integral left inverse.

Finally, actual weighting multiplies $a_j$ by $\binom{n+2}{j}$. Kummer’s carry formula gives


$$
v_p\binom{n+2}{j}\le\lfloor\log_p(n+2)\rfloor.
$$


This proves (46). At $29$, $f_0^0=C_n$ is already a unit by (39), proving (47).

### What this does—and does not—normalize

Put


$$
Z_w^\circ=p^{-\kappa_p}Z_w,\qquad
\mathfrak D^\circ=(Z_w^\circ)^TZ_w^\circ,\qquad
\Xi^\circ=(Z_w^\circ)^TY.
$$


Then


$$
\mathfrak D=p^{2\kappa_p}\mathfrak D^\circ,\qquad
\Xi=p^{\kappa_p}\Xi^\circ.
$$


Consequently the exact quotient law is


$$
\boxed{
v_p(q_n)=
\max\!\left\{
0,\,
2v_p(n!)-v_p(b!)
+\kappa_p
+v_p(\mathfrak D^\circ)-v_p(\Xi^\circ)
\right\}.
}
\tag{51}
$$


The common-column contribution $\kappa_p$ is now bounded by $O(\log n)$, unconditionally.

Equivalently,


$$
v_p(\Xi)-v_p(\mathfrak D)
=
v_p(\Xi^\circ)-v_p(\mathfrak D^\circ)-\kappa_p.
\tag{52}
$$


Thus the still-missing bound is genuinely a **primitive scalar-contraction** bound. Common $P$-content alone cannot be blamed for a larger uncontrolled depth.

This does not establish


$$
v_p(\Xi^\circ)-v_p(\mathfrak D^\circ)=O(\log n).
$$


A primitive vector can have a highly divisible quadratic norm, and its cross contraction can undergo further cancellation. Neither primitivity nor a support bound prevents that.

---

## 6. Final gcd, same-index restrictions, and the whole error

To keep the final reduction explicit, set


$$
N_B=d_B[u,v],
$$




$$
B_n=A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
A_n=H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_n=\gcd(B_n,|A_n|),\qquad
p_n=A_n/g_n,\qquad
\boxed{q_n=|B_n|/g_n.}
\tag{53}
$$



For $p=23,29$, write


$$
F_n=v_p(n!),\quad F_b=v_p(b!),\quad
\delta=v_p(\mathfrak D),\quad \xi=v_p(\Xi).
$$


Then, using the actual local least-denominator fact (5),


$$
\boxed{
v_p(g_n)=
\min\{4F_n+\delta,\;2F_n+F_b+\xi\},
}
\tag{54}
$$


and


$$
\boxed{
v_p(q_n)=\max\{0,\,2F_n-F_b+\delta-\xi\}.
}
\tag{55}
$$


On the unit cases established by the carry criterion,


$$
v_p(g_n)=2F_n+F_b+1,\qquad
v_p(q_n)=2F_n-F_b-1.
\tag{56}
$$


These are final evaluated-gcd statements, not coefficient-content substitutions.

The classes at $23$ and $29$ intersect at


$$
a\equiv3\pmod{308}.
$$


But I have not proved that the needed $23$- and $29$-norm conditions hold on an infinite subset of that intersection. No favorable aggregate is asserted.

The complete cross contraction is nonzero at every original index by the inherited exact $3$-adic theorem. Also $\mathfrak D>0$, so every valuation appearing above is finite.

At the stated dependency status of the supplied proportional signed-rate theorem, on this exact allocation,


$$
\epsilon_n=c_n-(e+\pi)\ne0\quad\text{eventually},
$$




$$
\log|\epsilon_n|
=
-\left(2+\frac1{2001}\right)\log(1+\sqrt2)\,n+o(n).
$$


The complete primitive evaluated error remains


$$
\boxed{
L_n=q_n(e+\pi)-p_n=-q_n\epsilon_n\ne0
\quad\text{eventually}.
}
\tag{57}
$$


All original $n$ are odd, so the inherited sign assertion gives $\epsilon_n>0$, and hence $L_n<0$, eventually. No exponential-only or logarithmic-only error is substituted for (57).

---

# Concluding ledger

## (1) New result and proof status

**Proved here, from the supplied exact contact construction**

1. The symbolic second divided-cross carry, including all relevant corrections:
   

$$
\frac{\Xi}{p}
   \equiv
   \frac{-2N(-1)^B\eta_{p,r}}{r!}J\mathcal S
   \pmod p,\qquad p=23,29,\ r\ge3.
$$


   The contact correction and nonconstant residual corrections vanish in the required projection for explicitly proved reasons.

2. On $a\equiv3\pmod{11}$,
   

$$
\Xi/23\equiv J\mathcal S,\qquad
   \mathfrak D\equiv6J^2\mathcal S\pmod{23}.
$$


   This derives the supplied finite value $5$ and identifies its nonconstant higher-digit dependence.

3. At $29$, there are no zero constant-term digit factors. Thus $J$ is a $29$-unit at every original index.

4. On $a\equiv3\pmod{28}$,
   

$$
\Xi/29\equiv J\mathcal S,\qquad
   \mathfrak D\equiv6J^2\mathcal S\pmod{29}.
$$



5. The unconditional whole-weighted-$P$-content bound
   

$$
\kappa_p\le2\lfloor\log_p(n+2)\rfloor,
$$


   with the sharper one-logarithm bound at $29$, and the exact normalized quotient law (51).

**Not proved**

An $O(\log n)$ bound for the primitive cross-minus-norm depth, an infinite norm-unit exponent class, a favorable aggregate final-gcd estimate, or irrationality of $e+\pi$.

## (2) Exact remaining bottleneck

After the proved logarithmic common-content removal, the local unresolved quantity is


$$
\boxed{
v_p(\Xi^\circ)-v_p(\mathfrak D^\circ),
\qquad p=23,29,
}
$$


on an explicit infinite sequence of the original indices.

At $23$, the first-layer unit criterion additionally requires the digit-sensitive $J$-unit. At $29$, that obstruction is completely removed, but the weighted norm sum $\mathcal S$ and its deeper simultaneous carries remain.

Equations (31) and (41) align the first scalar zeros; they do not control the depth of their simultaneous continuation.

## (3) One bounded exact computation request

**REQUEST: pro / max / high**

**Purpose:** independently test the newly derived $29$-carry at the same original center already controlled at $3$ and $23$.

**Inputs**


$$
n=54027,\qquad b=27,\qquad m_w=1,\qquad p=29,
$$


using the original defining coefficient sums and complete forcing, with


$$
\Xi=\mathfrak C/27!,\qquad \text{modulus }29^2=841.
$$



**Expected verifiable output**


$$
\boxed{
J\equiv21\pmod{29},\qquad
\mathfrak D\equiv7\pmod{29},\qquad
\Xi\equiv609\pmod{841}.
}
$$


Equivalently,


$$
\Xi/29\equiv21\pmod{29}.
$$



The complete logarithmic forcing has


$$
v_{29}(h_i^F/27!)\ge1929-3=1926,
$$


so its disappearance at this precision should be certified by that bound.

If the predicted residues pass, the finite, final-gcd conclusion is


$$
\boxed{
v_{29}(g_n)=3859,\qquad
v_{29}(q_n)=3857.
}
$$


This requested check would verify one newly derived carry, not prove an infinite-index law.
