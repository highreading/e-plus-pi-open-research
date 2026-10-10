> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2 — completed bounded $R_C$ kernels and a one-pass certificate specification

## Status

The coordinator’s two proposed contact simplifications are valid. They admit a further reduction:

- $h_A\bmod841$ has an explicit $58$-entry Newton vector given below.
- $h_Q\bmod24389$ has an explicit $58$-entry Newton vector requiring only **two contact-coefficient terms per entry**, followed by a correction at four specified entries.
- At these precisions, both positive reconstructed kernels have Laurent support contained in
  

$$
\boxed{0\le q\le30,}
$$


  rather than merely $0\le q\le58$.
- The complete exterior boundary still requires every power
  

$$
\boxed{-60\le q\le0.}
$$


- The positive coefficient arrays can be cached on $x\bmod841$. The raw unit-boundary coefficient at $q=-2$ generally cannot. The stripping units, carry counts, shapes, and harmonic coefficients also cannot be reduced to $x\bmod841$.

Thus the remaining calculation is one pass through $0\le x<29^4$, with at most $91$ Laurent positions per row and no contact inverse.

I reuse the supplied exact receipt


$$
\zeta_0=18,\qquad \zeta_1=11,\qquad \zeta=0.
$$


At the stated turn23 reconstruction dependencies, it gives


$$
\boxed{R_{29}=20K_d,\qquad \Gamma _1(d)=0\quad(0\le d\le24).}
$$



**The universal $R_C$ contraction constants have not been numerically evaluated in this report.** Consequently, this is a completion of the bounded kernel and certificate specification, not a completed mixed identity or a proof of third-depth alignment.

---

## 1. Source gate, domain, and dependency ledger

I checked the supplied archive for the finite contact operator, boundary elimination, reconstruction, moment reduction, and third-defect interface. The unrelated paired-derangement determinant construction supplies no missing $R_C$ identity and is not used here.

There is no external search facility in this interface. I therefore cannot report a fresh primary-literature search as completed. The identities proved below are elementary finite-binomial, factorial, and polynomial identities; no global novelty claim is made.

Keep the original domain


$$
p=29,\qquad b=3^a,\qquad n=2001b,\qquad
a\ge1,\quad a\equiv432827\pmod{682892}.
$$


Every contact inverse remains indexed by


$$
0\le i,j<b,
$$


and actual weighted coordinates remain indexed by


$$
0\le j\le b.
$$



The metric used here is the explicitly specified falling-factorial metric


$$
\omega_j=j!\binom{n+2}{j}=(n+2)_{\underline j},
\qquad
\Omega=\operatorname{diag}(\omega_j^2).
$$


The earlier descriptions of this same expression as “rising” cannot be retained.

Write


$$
P=\frac{Z_w}{p^2},\qquad Q=\frac{Y}{p^3},\qquad
Y=\frac{V_w}{b!},
\qquad D=P^TP,\quad M=P^TQ.
$$


Set


$$
L=p^4=707281,\qquad b_*=687936,
$$




$$
b=b_*+Lh,\qquad n=191110+LN,\qquad
N=3+pA,\qquad h=pH+d.
$$



The retained third-defect interface, on


$$
0\le d\le24,\qquad T=0,\qquad D_1=0,
$$


is


$$
\frac{M-(6C_n)^{-1}D}{p^2}
=
U\bigl(C_n\Gamma _0(d)+J_{29}\Gamma _1(d)\bigr)
\pmod p.                                                    \tag{1.1}
$$



The supplied receipt closes its second coefficient. Indeed,


$$
8\zeta_0-11=17=20\cdot11,\qquad
8\zeta_1-18=12=20\cdot18\pmod{29},
$$


so turn23’s formula gives


$$
R_{29}=20\{11(d+7-J)^2+18(3-J)^2\}=20K_d.
$$


Since $\mathcal L_d(K_d)=0$,


$$
\boxed{
\frac{M-(6C_n)^{-1}D}{p^2}
=
C_nU\,\Gamma _0(d)\pmod p
}                                                           \tag{1.2}
$$


at those reconstruction dependencies.

The exact finite receipt does not independently prove those dependencies, all-depth alignment, or an original-index nonzero-defect reachability statement.

---

# Part I. Explicit bounded Newton vectors

## 2. Audit of the proposed finite contact compression

The signed finite operator is


$$
\begin{aligned}
\mathscr L_{s,b}\binom Xr
={}&(-1)^s\binom Xs\binom{X-s}r\\
&+\sum_{v=1}^s(-1)^{s-v}\binom X{s-v}\binom nv
 \sum_{i=0}^r
 \binom{X-s+v}{r-i}\binom{v+i-1}i
 \binom{b-1-X+s}{v+i}.
\end{aligned}                                               \tag{2.1}
$$


Its last binomial preserves the actual finite endpoint.

For a Newton polynomial $h$ of degree at most $28$, the proposed reductions are


$$
\boxed{
\mathscr L_{s,b}h
\equiv(-1)^s\binom Xs h(X-s)\pmod p,
\qquad 1\le s\le28,
}                                                           \tag{2.2}
$$


and


$$
\boxed{
\mathscr L_{29,b}h
\equiv-\binom X{29}h(X-29)
      +7h(X)\binom{b+28-X}{29}\pmod p.
}                                                           \tag{2.3}
$$



They are valid coefficientwise in the integral Newton representation:

- $\binom nv=0\bmod p$ for $1\le v\le28$;
- $\binom n{29}=7\bmod p$;
- for $1\le i\le28$,
  

$$
\binom{28+i}{i}=0\bmod p.
$$



Generalized binomials at negative integer arguments introduce no exception: the binomials are integer-valued, and the identities are polynomial identities before reduction.

A useful explicit version of the remaining factor is


$$
\boxed{
\binom{b+28-X}{29}
\equiv-\binom X{27}-2\binom X{28}-\binom X{29}\pmod p.
}                                                           \tag{2.4}
$$


Here $b+28\equiv26\bmod841$. Formula (2.4) follows from


$$
\binom{A-X}{r}
=\sum_{i=0}^r(-1)^i\binom{A-i}{r-i}\binom Xi.
$$



No field-value interpolation is being used.

---

## 3. Contact coefficients: a small recurrence

Define


$$
d_s=s![z^s](1-z+z^2/2)^n.
$$


For implementation, the following recurrence is simpler than repeated coefficient extraction:


$$
\boxed{
d_0=1,\qquad d_1=-n,\qquad
d_{s+1}=(s-n)d_s+s\left(n-\frac{s-1}{2}\right)d_{s-1}.
}                                                           \tag{3.1}
$$


It follows by differentiating $(1-z+z^2/2)^n$.

For all calculations of $d_s\bmod24389$, one may use


$$
\bar n=n\bmod24389=20387.
$$


Only $d_1,\ldots,d_{58}$ are needed; set $d_{59}=0\bmod24389$.

The valuation bound


$$
v_p(d_s)\ge1+v_p((s-1)!)
$$


gives


$$
d_s\in p\mathbb Z_p\quad(1\le s\le29),\qquad
d_s\in p^2\mathbb Z_p\quad(30\le s\le58).
$$



For the first layer, put $\gamma_s=d_s/p\bmod p$. Then


$$
\boxed{
\gamma_s=-7(s-1)!(21^s+9^s)\quad(1\le s\le28),
\qquad \gamma_{29}=7.
}                                                           \tag{3.2}
$$


The two roots $21,9$ satisfy


$$
1-z+z^2/2=(1-21z)(1-9z)\quad\text{in }\mathbb F_{29}[z].
$$



---

## 4. The complete explicit vector $h_A\bmod841$

Write


$$
h_A(X)=\sum_{i=0}^{57}\alpha_i\binom Xi.
$$


The following formulas specify every entry directly; there is no remaining contact operator or finite-difference reconstruction.

Define, in $\mathbb F_{29}$,


$$
a_t=\frac{7(8\cdot20^t-20\cdot8^t)}{12t},
\qquad 1\le t\le28,
$$




$$
H_i=\sum_{s=1}^i\frac1s,\qquad
E_i=\sum_{t=1}^i\binom it a_t,\qquad
V_i=\sum_{s=1}^i\frac{21^s+9^s}{s}.
$$


All three empty sums are zero.

Let $c_i=(-1)^ii!$, retaining the actual integer value in the first term of the next formula. Then


$$
\boxed{
\alpha_i
=
c_i+
29\left[
(c_i\bmod29)(7H_i+E_i+7V_i)
+\mathbf1_{i=27}-7\mathbf1_{i=28}
\right]\pmod{841},
\quad 0\le i\le28.
}                                                           \tag{4.1}
$$


The upper block is


$$
\boxed{
\alpha_{29+r}=29\cdot6(-1)^rr!\pmod{841},
\qquad 0\le r\le28.
}                                                           \tag{4.2}
$$



For clarity, its divided upper block is


$$
\boxed{
\begin{aligned}
(\alpha_{29},\ldots,\alpha_{57})/29
={}&(6,23,12,22,28,5,28,7,2,11,6,21,9,28,14,\\
&22,25,10,23,27,11,1,7,13,7,28,26,23,23)
\pmod{29}.
\end{aligned}}
$$


Initial checks from (4.1) are


$$
\alpha_0=1,\qquad \alpha_1=434,\qquad \alpha_2=698
\pmod{841}.
$$



### Derivation

Let


$$
h_0(X)=\sum_{i=0}^{28}(-1)^ii!\binom Xi.
$$


For $s<29$, the coefficient of $\binom Xr$ in $\mathscr L_{s,b}h_0\bmod p$ is


$$
(-1)^r\frac{r!}{s!},\qquad s\le r\le28,
$$


and is zero for $r\ge29$.

Next,


$$
h_0(27)=16,\qquad h_0(28)=17\pmod p.
$$


Using (2.4) and the Newton product identity gives


$$
\boxed{
\mathscr L_{29,b}h_0
=
4\binom X{27}+\binom X{28}
-8\sum_{r=0}^{28}(-1)^rr!\binom X{29+r}
\pmod p.
}                                                           \tag{4.3}
$$


For example,


$$
h_0(X)\left(\binom X{27}+2\binom X{28}\right)
=
16\binom X{27}+4\binom X{28}\pmod p.
$$



The initial forcing has lower coefficients


$$
c_i\{1+p(7H_i+E_i)\}\pmod{p^2},
$$


and upper coefficients $p\,8(-1)^rr!$. Subtracting the single contact action, with (3.2) and (4.3), proves (4.1)–(4.2).

---

## 5. The complete explicit vector $h_Q\bmod24389$

### 5.1 The coordinator’s boundary-contact simplification passes

For the raw exterior coefficients


$$
c_h=\sum_{r=h}^{59}\frac{(b+r)!}{b!}\binom{2n}{r-h}\pmod{p^4},
$$


one has


$$
c_h\in p^2\mathbb Z_p\quad(h\ge2),\qquad
c_0=1-2n\pmod{p^2},\qquad c_1=-1\pmod{p^2}.
$$


Because every contact coefficient contains $p$, only $c_0,c_1$ contribute to $a_Q\bmod p^3$. Thus


$$
\begin{aligned}
a_Q(X)\equiv
\sum_{s=1}^{58}d_s(-1)^{s+1}
\sum_{v=1}^s(-1)^v\binom X{s-v}\binom nv
\bigg[
&(1-2n)\binom{b-X+s-1}{v-1}\\
&+\binom{b-X+s}{v-1}
\bigg]\pmod{p^3}.
\end{aligned}                                               \tag{5.1}
$$


This simplification concerns only the contact force. It does not remove the raw exterior boundary.

### 5.2 A further Newton contraction

For $k=s-v$, the coefficient of $\binom Xi$ in


$$
\binom Xk\binom{A-X}{v-1}
$$


is


$$
(-1)^{i-k}\binom ik\binom{A-i}{s-1-i}.
$$


After combining the signs in (5.1), Vandermonde gives


$$
\sum_v\binom i{s-v}\binom nv=\binom{n+i}s.
$$


Therefore


$$
[a_Q]_i
=
(-1)^{i+1}\sum_{s=i+1}^{58}
d_s\binom{n+i}s
\left[
(1-2n)\binom{b+s-1-i}{s-1-i}
+\binom{b+s-i}{s-1-i}
\right]\pmod{p^3}.                                         \tag{5.2}
$$



Put $k=s-1-i$. For $2\le k\le28$, the bracket is divisible by $p^2$. For $29\le k\le57$, it is divisible by $p$, while $s\ge30$ supplies $p^2$. Hence every term with $k\ge2$ vanishes.

This leaves just two terms:


$$
\boxed{
[a_Q]_i=(-1)^{i+1}
\left[
(2-2n)d_{i+1}\binom{n+i}{i+1}
+(-1+2n)d_{i+2}\binom{n+i}{i+2}
\right]\pmod{p^3}.
}                                                           \tag{5.3}
$$



The divisibility used here is an actual factorial-product divisibility. For example, $\binom{b+k}{k}$ contains $b+2$, of valuation two. For $29\le k\le57$, removing the single denominator factor $29$ still leaves at least one factor $29$.

### 5.3 The one subsequent contact is sparse

The leading contact polynomial is


$$
\boxed{
a_Q/p\equiv a(X):=9\binom X{27}+18\binom X{28}\pmod p.
}                                                           \tag{5.4}
$$


This is the degree-$28$ Newton representation of the coordinator’s two-binomial expression.

Using (2.2)–(2.4),


$$
\mathscr L_{1,b}a=9\binom X{28},\qquad
\mathscr L_{s,b}a=0\quad(2\le s\le28),
$$


and


$$
\mathscr L_{29,b}a
=
24\binom X{27}+19\binom X{28}
+15\binom X{56}+\binom X{57}\pmod p.
$$


Consequently


$$
\sum_{s=1}^{29}\gamma_s\mathscr L_{s,b}a
=
23\binom X{27}+12\binom X{28}
+18\binom X{56}+7\binom X{57}\pmod p.                         \tag{5.5}
$$



Writing


$$
h_Q(X)=\sum_{i=0}^{57}\beta_i\binom Xi,
$$


the promised explicit vector is


$$
\boxed{
\begin{aligned}
\beta_i={}&(-1)^{i+1}
\left[
(2-2\bar n)d_{i+1}\binom{\bar n+i}{i+1}
+(-1+2\bar n)d_{i+2}\binom{\bar n+i}{i+2}
\right]\\
&-841\left(
23\mathbf1_{i=27}+12\mathbf1_{i=28}
+18\mathbf1_{i=56}+7\mathbf1_{i=57}
\right)
\pmod{24389},
\quad 0\le i\le57.
\end{aligned}}                                             \tag{5.6}
$$


Here $\bar n=20387$, and the $d_s$ are given by (3.1).

Replacing $n$ by $\bar n$ in the small-lower binomials is legitimate after multiplication by $d_s$: the possible loss of one power of $p$ in their parameter period is compensated by $p\mid d_s$.

Checks include


$$
\beta_0=9251,\qquad \beta_1=10933\pmod{24389},
$$


and


$$
\beta_{27}=29\cdot9,\qquad
\beta_{28}=29\cdot18\pmod{841},
$$


with every other $\beta_i$ zero modulo $841$.

Equations (4.1)–(4.2) and (5.6) are explicit component definitions of the requested vectors, not assertions that a separate numerical vector computation has been run.

---

# Part II. Complete Laurent coefficients and valid caching

## 6. A minimal positive-kernel formula

Let


$$
h(X)=\sum_{i=0}^{57}\eta_i\binom Xi,\qquad
S_t(x)=\sum_{i=t}^{57}\eta_i\binom{x}{i-t},
$$


and put


$$
A_t=\binom{2n+t-1}{t}.
$$


The reconstruction is


$$
\mathcal R_h(x,r)
=\sum_{t=0}^{57}A_t
\left[
r^{t+1}S_t(x)+(1+r)r^t xS_t(x-1)
\right].                                                   \tag{6.1}
$$


Thus its coefficient at $r^q$ is


$$
\boxed{
k_q(x)=
A_{q-1}\{S_{q-1}(x)+xS_{q-1}(x-1)\}
+A_qxS_q(x-1),
}                                                           \tag{6.2}
$$


where nonexistent terms are zero. In particular,


$$
k_0(x)=xS_0(x-1).
$$



At the present precisions, only $S_0,\ldots,S_{29}$ are required.

Indeed,


$$
p\mid A_t\quad(1\le t\le57,\ t\ne29).
$$


For $h_A$, every coefficient of index at least $29$ contains $p$; for $h_Q$, every such coefficient contains $p^2$. Hence the terms with $t\ge30$ vanish at their respective working precisions.

Therefore


$$
\boxed{
\operatorname{supp}\mathcal R_{h_A}\subseteq[0,30]\pmod{p^2},
\qquad
\operatorname{supp}\mathcal R_{h_Q}\subseteq[0,30]\pmod{p^3}.
}                                                           \tag{6.3}
$$


The coefficients at $31,\ldots,58$ are proved zero, not silently omitted.

---

## 7. Every negative boundary coefficient

Compute the complete raw boundary coefficients


$$
c_h=\sum_{r=h}^{59}F_r\binom{2n}{r-h}\pmod{p^4},
\qquad
F_r=\prod_{i=1}^r(b+i).
$$


Define


$$
E_k=\sum_{h=k}^{59}(-1)^hc_h\binom hk,\qquad 0\le k\le59,
$$


and set $E_{-1}=E_{60}=0$.

Because the original $b$ is odd, the full boundary is


$$
\sum_{h=0}^{59}(-1)^hc_h(1+r^{-1})^h(1+x+xr^{-1}).
$$


Its coefficient at $r^{-k}$ is exactly


$$
\boxed{
t_{-k}(x)=E_k+x(E_k+E_{k-1}),\qquad 0\le k\le60.
}                                                           \tag{7.1}
$$



Use


$$
a_q(x)=[r^q]\mathcal R_{h_A},
$$


and


$$
y_q(x)=[r^q]\mathcal R_{h_Q}+t_q(x).
$$


This supplies every actual coefficient in


$$
\boxed{-60\le q\le30.}
$$



The $q=0$ contact and boundary coefficients are added, not treated as alternative formulas.

---

## 8. Precisely what may be cached modulo $841$

For $r<58$, Vandermonde gives


$$
\binom{x+p^2}{r}-\binom xr
\in
\begin{cases}
p^2\mathbb Z_p,&r<29,\\
p\mathbb Z_p,&29\le r<58.
\end{cases}                                                \tag{8.1}
$$



Together with the coefficient filtrations, this proves:

| Coefficient data | Working precision | Depend only on $x\bmod841$? |
|---|---:|---|
| Every $a_q(x)$ | $p^2$ | Yes |
| Every positive-contact coefficient of $y_q(x)$ | $p^3$ | Yes |
| Boundary $q=0,-1$, at their sufficient precision | $p^2$ | Yes |
| Boundary $q=-k,\ 3\le k\le31$ | $p^4$ | Yes |
| Boundary $q=-k,\ 32\le k\le60$ | $p^4$ | In fact $x\bmod p$ suffices |
| Raw boundary $q=-2$ | $p^4$ | **No, generally** |

For the last assertions, note


$$
E_k\in p^2\mathbb Z_p\quad(k\ge2),\qquad
E_k\in p^3\mathbb Z_p\quad(k\ge31),
$$


whereas


$$
E_0=2,\qquad E_1=1\pmod p.
$$



More exactly, an affine boundary coefficient $E_k+xB_k$, evaluated modulo $p^m$, has additive period


$$
p^{\max(0,m-v_p(B_k))}.
$$


This formula allows any extra cancellation in a computed $B_k=E_k+E_{k-1}$ to be used safely.

### The exceptional coefficient $q=-2$

Its slope $E_2+E_1$ is a unit. Let $c_{x,-2}$ be its four-level carry count. To compute the normalized $Q$-coefficient modulo $p^2$, its required raw precision is


$$
p^{\,5-c_{x,-2}}.
$$


Thus the necessary period can be $p^4$, $p^3$, or $p^2$, according to whether the carry count is $1,2$, or at least $3$.

This is not a merely theoretical exception. At $x=0$ and $x=p^2$, the $q=-2$ product has one low carry. Replacing $x$ by its residue modulo $p^2$ loses a contribution after the required division.

Finally, none of the following has been proved $p^2$-periodic:

- $c_{xq}$;
- the low factorial unit $u_{xq}$;
- the shape $(e,u)$;
- $r_q$;
- the harmonic coefficients.

They depend on the full four-digit low block and must still be computed on the actual $x\in[0,L)$.

---

# Part III. The universal pass

## 9. Explicit stripping and harmonic data

For each $0\le x<L$, put


$$
v=b_*-x,\qquad
e=\mathbf1_{x>191112},\qquad
u=\left\lfloor\frac{382219+v}{L}\right\rfloor,\qquad
r_q=\mathbf1_{v-q<0}.
$$


The three shapes are


$$
(e,u)=(0,1),(1,1),(1,0).
$$


Use formal variables $D,J$, and set


$$
G_{eu}(D,J)=(3-J)^e(D+7-J)^u.
$$



The six factorial arguments, specified by high and low parts, are



$$
\begin{array}{c|c|c}
 &\text{high part}&\text{low part}\\ \hline
W_{\rm top}&3&191112\\
W_{\rm bot1}&J&x\\
W_{\rm bot2}&3-J-e&191112-x+Le\\
B_{\rm top}&6+D-J+u&382219+v-Lu\\
B_{\rm bot1}&D-J-r_q&v-q+Lr_q\\
B_{\rm bot2}&6&382219+q
\end{array}                                                \tag{9.1}
$$



For an argument $z=La+t$, $0\le t<L$, let


$$
s_i(z)=\left\lfloor t/p^i\right\rfloor\bmod p,\qquad
m_i(z)=p^{3-i}a+\left\lfloor t/p^{i+1}\right\rfloor.
$$


Use numerator signs $+$ and denominator signs $-$. Then


$$
c_{xq}=\sum_{i=0}^3\sum_z\varepsilon_zm_i(z),
$$




$$
\boxed{
u_{xq}=(28!)^{c_{xq}}
\prod_{i=0}^3\prod_z(s_i(z)!)^{\varepsilon_z}\pmod{841}.
}                                                           \tag{9.2}
$$


All factorials in the product are units.

The complete first harmonic correction is


$$
\Lambda_{xq}(D,J)
=\sum_{i=0}^3\sum_z\varepsilon_zm_i(z)H_{s_i(z)}
=\lambda_0+\lambda_DD+\lambda_JJ\pmod p.                    \tag{9.3}
$$



For implementation, its two nonconstant coefficients are particularly short:


$$
\boxed{
\lambda_D=H_{s_3(B_{\rm top})}-H_{s_3(B_{\rm bot1})},
}                                                           \tag{9.4}
$$




$$
\boxed{
\lambda_J=
-H_{s_3(W_{\rm bot1})}+H_{s_3(W_{\rm bot2})}
-H_{s_3(B_{\rm top})}+H_{s_3(B_{\rm bot1})}.
}                                                           \tag{9.5}
$$


The constant coefficient is


$$
\begin{aligned}
\lambda_0={}&
\sum_{i=0}^{2}\sum_z\varepsilon_zs_{i+1}(z)H_{s_i(z)}
+3H_{s_3(W_{\rm top})}-(3-e)H_{s_3(W_{\rm bot2})}\\
&+(6+u)H_{s_3(B_{\rm top})}
+r_qH_{s_3(B_{\rm bot1})}
-6H_{s_3(B_{\rm bot2})}\pmod p.
\end{aligned}                                               \tag{9.6}
$$



These formulas retain the $D$- and $J$-harmonic terms. In particular, $28!$ is retained modulo $841$, not replaced by $-1$.

The resulting natural high multiplier is


$$
G_{eu}(D,J)(D-J)^{r_q}.
$$



---

## 10. Safe normalization before accumulation

For an $A$-coefficient, define


$$
A^{\rm raw}_{xq}=p^{c_{xq}-2}a_q(x).
$$


For a $Q$-coefficient, define


$$
Q^{\rm raw}_{xq}=p^{c_{xq}-3}y_q(x).
$$



A negative exponent here denotes an exact division of the **whole coefficient**, not inversion of $p$ modulo $841$. Before division, verify


$$
v_p(a_q(x))+c_{xq}\ge2,\qquad
v_p(y_q(x))+c_{xq}\ge3.                                    \tag{10.1}
$$


For the exceptional boundary term, this verification includes its factor $x$.

For either column, with normalized raw coefficient $z$, accumulate


$$
z\,u_{xq}(1+p\lambda_0)\pmod{p^2}
$$


into its constant slot, and


$$
(z\bmod p)(u_{xq}\bmod p)\lambda_D,\qquad
(z\bmod p)(u_{xq}\bmod p)\lambda_J
$$


into its two harmonic slots.

Group by $r_q=0,1$. This produces


$$
A_{xr}=a_{xr}+p(b_{xr,D}D+b_{xr,J}J),
$$




$$
Q_{xr}=q_{xr}+p(c_{xr,D}D+c_{xr,J}J).
$$


The natural low polynomials are


$$
A_x=G_{eu}\{A_{x0}+(D-J)A_{x1}\},
$$




$$
Q_x=G_{eu}\{Q_{x0}+(D-J)Q_{x1}\}\pmod{p^2}.                \tag{10.2}
$$



This is an implementable row kernel involving:

1. cached positive coefficients on $841$ residues;
2. the complete affine boundary (7.1), with $q=-2$ evaluated at actual $x$;
3. at most $91$ stripping records;
4. six slots per column.

---

## 11. The $27$ constants, and a stronger divisibility check

For each shape and $v=0,1,2$, retain turn23’s definitions


$$
T^{(0)}_{eu,v}
=
\sum_{\substack{x:\,\mathrm{shape}(x)=(e,u)\\r+s=v}}
\left(a_{xr}q_{xs}-\frac16a_{xr}a_{xs}\right)\pmod{p^2},
$$


and, for $Z=D,J$,


$$
\begin{aligned}
T^{(Z)}_{eu,v}
=
\sum_{\substack{x:\,\mathrm{shape}(x)=(e,u)\\r+s=v}}
\bigg[
&a_{xr}c_{xs,Z}+b_{xr,Z}q_{xs}\\
&-\frac16(a_{xr}b_{xs,Z}+b_{xr,Z}a_{xs})
\bigg]\pmod p.
\end{aligned}                                               \tag{11.1}
$$



There are nine flat and eighteen harmonic constants.

### Each flat entry is divisible by $29$ in this construction

At the retained natural leading-column identities,


$$
A_x^{(0)}=
\begin{cases}
c(x)\ell_{e(x)},&x\in\mathcal X,\\
0,&x\notin\mathcal X,
\end{cases}
\qquad
Q_x^{(0)}=\xi(x)\ell_{e(x)}\quad(x\in\mathcal X).
$$


Comparison with (10.2), as ordinary polynomials, gives


$$
a_{x1}=0\pmod p\quad\text{for every }x,
$$


and, on $\mathcal X$,


$$
a_{x0}=c(x),\qquad q_{x0}=\xi(x),\qquad q_{x1}=0\pmod p.
$$


The support has only the two shapes with $e+u=1$.

Therefore the $v=1,2$ flat entries and the middle-shape flat entry are zero modulo $p$. The remaining two reduce to


$$
g_e-\kappa_e/6=0.
$$


Hence


$$
\boxed{T^{(0)}_{eu,v}\equiv0\pmod{29}\quad\text{for all nine entries}.} \tag{11.2}
$$



This is stronger than merely checking divisibility after expanding the aggregate polynomial. It uses the natural leading reconstruction identities as well as the supplied $\kappa,g$ constants; the finite constants alone would not establish it.

Define


$$
\tau_{eu,v}=T^{(0)}_{eu,v}/29\pmod p.
$$


Then the universal polynomial is


$$
\boxed{
R_C(D,J)=
\sum_{eu,v}G_{eu}(D,J)^2(D-J)^v
\left[
\tau_{eu,v}+D\,T^{(D)}_{eu,v}+J\,T^{(J)}_{eu,v}
\right].
}                                                           \tag{11.3}
$$


Its total degree is at most seven.

No analytic identity evaluating these $27$ divided/harmonic constants has been proved here. In particular, leading norm and mixed constants do not determine the harmonic weighted contractions.

---

## 12. The resulting $\Gamma _0$ formula

For $d=0,\ldots,24$, put


$$
B_{eu,v,d}(J)=(3-J)^{2e}(d+7-J)^{2u}(d-J)^v.
$$


Let $\mathcal L_d$ be the retained ordinary-polynomial functional


$$
\mathcal L_d(V)=
\sum_{\rm adm.\ t}w_t\{V'(t)+2r_tV(t)\}
-\frac{\beta(d)}{f(d)}\sum_{\rm adm.\ t}w_tV(t),
$$


where


$$
0\le t\le3,\qquad 0\le d-t\le22,
$$




$$
w_t=\binom3t^2\binom{d-t+6}{6}^2,
\qquad
r_t=H_{3-t}-H_t+H_{d-t}-H_{d-t+6}.
$$



After the single universal calculation,


$$
\boxed{
\begin{aligned}
\Gamma _0(d)=\sum_{eu,v}\bigg[
&\left(\tau_{eu,v}+dT^{(D)}_{eu,v}\right)
       \mathcal L_d(B_{eu,v,d})\\
&+T^{(J)}_{eu,v}\mathcal L_d(JB_{eu,v,d})
\bigg]\pmod{29}.
\end{aligned}}                                             \tag{12.1}
$$



All derivatives are ordinary derivatives. For example,


$$
\begin{aligned}
B'={}&-2e(3-J)^{2e-1}(d+7-J)^{2u}(d-J)^v\\
&-2u(3-J)^{2e}(d+7-J)^{2u-1}(d-J)^v\\
&-v(3-J)^{2e}(d+7-J)^{2u}(d-J)^{v-1},
\end{aligned}
$$


with terms of zero prefactor omitted.

There is no reduction modulo $J^{29}-J$, and no replacement of derivatives by interpolation.

A concrete follow-on lemma, sufficient but stronger than necessary, is


$$
R_C(d,J)\in\operatorname{span}_{\mathbb F_{29}}K_d(J)
\quad(0\le d\le24).
$$


The weaker, exactly targeted certificate is simply that all $25$ values in (12.1) vanish.

---

## 13. Original endpoint, higher digits, and the precision-three interface

The original finite endpoint has not been removed. The absorbed boundary continues to represent


$$
Y_b=W_b(1+b\theta^Q_{b-1}),
$$


including the $1$.

For $x>b_*$, every positive $P$-power has $r_q=1$. Thus $A_x$ contains $h-J$. Only after exhibiting that factor may the range $J\le h-1$ be extended to $J\le h$ in the contractions.

The universal specialization $N=3,h=D$ is an aggregate lifted-polynomial specialization, not a claim that each individual column is independent of higher digits modulo $p^2$. Before specialization, the leading contracted coefficients of


$$
(2N+h+1-J)^2,\qquad (N-J)^2
$$


are divisible by $p$. Altering $N,h$ by multiples of $p$ therefore changes that leading contraction only modulo $p^2$. The harmonic terms already contain $p$. This is the reason the divided residual depends only on $d$.

For the proof of the third-defect interface itself, retain the stronger precision-three reconstruction:

- boundary factorial indices through $88$;
- all negative powers through $-89$;
- the unfrozen unit-boundary correction
  

$$
\delta Y_{LJ+x}
  \equiv(-1)^{j+1}LJ\,W_jB_{-2}(j)\pmod{p^6}.
$$



That correction belongs to the second residual polynomial and is killed by its leading scalar contraction on $T=0$. It is not part of the $R_C$ calculation modulo $p^2$, but it remains necessary to justify (1.1).

The complete logarithmic force remains absent only through the whole-force bound


$$
v_p(h_i^F/b!)
\ge v_p(n!)-v_p(b!)
-\lfloor\log_p(2n+b-1)\rfloor\ge6.
$$


No selected logarithmic summands are substituted for this bound.

---

# 14. Deterministic calculation and required receipt

Use the fixed odd representative


$$
b^\circ=1395217,\qquad n^\circ=2791829217.
$$


It is a low-parameter representative, not an original power-$3$ index.

### Inputs

1. The vectors (4.1)–(4.2) and (5.6).
2. The $60$ actual boundary coefficients $c_0,\ldots,c_{59}\bmod707281$.
3. Factorials $0!,\ldots,28!\bmod841$ and harmonics $H_0,\ldots,H_{28}\bmod29$.
4. All actual $x=0,\ldots,707280$.
5. The stripping and accumulation formulas (9.1)–(11.1).

### Calculation

- Precompute the positive coefficient arrays on the $841$ residue classes.
- Compute $E_0,\ldots,E_{59}$ once.
- Make one low-coordinate pass.
- Evaluate $q=-2$ at actual $x$, not its $841$-residue.
- Accumulate the $27$ constants.
- Form (11.3) and evaluate the $25$ contractions (12.1).

### Mandatory verifiable output

1. The two explicit Newton vectors as residue lists.
2. Checks of their leading filtrations and the zero Laurent coefficients at $31,\ldots,58$.
3. Nine $T^{(0)}$ residues modulo $841$.
4. Eighteen harmonic residues modulo $29$.
5. All normalization checks (10.1), before every division.
6. The nine divisibility checks (11.2).
7. The ordinary coefficient list of $R_C(D,J)$, degree at most seven.
8. The $25$ values $\Gamma _0(0),\ldots,\Gamma _0(24)$.
9. Independent checks that the direct functional calculation agrees with (12.1), and that $\mathcal L_d(K_d)=0$.

This is a completely bounded exact calculation. Its outcome is not supplied or predicted as zero here.

---

# 15. Primitive arithmetic and whole evaluated error

Retain the actual least two-column denominator


$$
N_B=d_B[u,v],\qquad v_{29}(d_B)=0.
$$


With the actual falling metric,


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
p_n=H_B/g_B,\qquad q_n=A_B/g_B>0.
$$


The primitive multiplier is $1/g_B$ on the integer Gram pair, or $d_B^2/g_B$ on the rational pair.

For


$$
\delta=v_{29}(D),\qquad \mu=v_{29}(M),
$$


the retained arithmetic interface remains


$$
v_{29}(g_B)
=\min\{4F_n+4+\delta,\;2F_n+F_b+5+\mu\},
$$




$$
v_{29}(q_n)
=\max\{0,\;2F_n-F_b-1+\delta-\mu\}.
$$


A finite-depth result does not control $\mu-\delta$ at all depths or determine the denominator contribution of every other prime.

For the whole real error


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
$$


the exact identity is


$$
\boxed{q_n(e+\pi)-p_n=-q_n\epsilon_n.}
$$


The supplied signed-error theorem retains its dependency status. Neither a partial force nor a local denominator is substituted for this whole evaluated form.

---

## Conclusion

### New proved reduction

The complete bounded contact inputs are now specified without an unevaluated contact operator:

- an explicit $58$-entry formula for $h_A\bmod841$;
- a two-term-per-entry formula for $h_Q\bmod24389$, with a four-entry inverse correction;
- positive Laurent support reduced to $0,\ldots,30$;
- every negative boundary coefficient through $-60$ retained;
- precise valid caching rules, including the exceptional $q=-2$ coefficient;
- an explicit one-pass $27$-constant calculation and its ordinary-derivative contraction.

The supplied receipt closes


$$
R_{29}=20K_d,\qquad \Gamma _1=0
$$


at the stated reconstruction dependencies.

### Exact remaining bottleneck

The immediate missing result is the numerical evaluation of the $27$ universal $R_C$ constants, equivalently the $25$ values in (12.1). No analytic contraction eliminating that low pass has been proved here.

If all $25$ values vanish, (1.2) proves the stated third-depth alignment on $d\le24,\ T=0,\ D_1=0$. If some do not, actual power-$3$ reachability and the factor $C_nU$ still have to be examined before asserting an original-domain nonzero defect.

Even successful third-depth alignment would leave all-depth relative valuations and the actual primitive denominator unresolved. **The irrationality or rationality of $e+\pi$ remains unproved by this work.**
