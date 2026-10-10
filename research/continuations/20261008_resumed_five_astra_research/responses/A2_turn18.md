> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2 Turn 18 — All-precision audit and an exact recurrence for the literal one-shot residual pair

## Executive statement

The rationality or irrationality of $e+\pi$ remains unresolved.

The two new parent candidates pass the audit below, subject to their stated integral and finite-range hypotheses:

- the formal differential equation and precision-contractive rational expansion for the actual contact numbers;
- the integer numerator recursion, including the carries required modulo $16$;
- integral Hasse extraction for the actual top and arbitrary-pole bottom sources;
- the complete top and atom laws modulo $16$;
- the uniform period $12$ modulo $8$;
- the all-phase lifting to
  

$$
T_h=3\cdot2^{h-1},\qquad h\ge3.
$$



The earlier modulo-$4$ anti-period is **reused**, not claimed as a new result.

For the primary residual-pair application, this report proves a concrete follow-on lemma: an exact finite source recurrence, a factorial-paid path contraction of the actual remaining return columns, and a backward recurrence evaluating **both literal borders**, including the full constant border $-f+4\rho$. These identities preserve the actual odd pivot quotient and the entire finite forcing.

They do **not** prove a reduction to two residual directions. The full dimension remains


$$
s=\frac d2+m_d+3.
$$


An explicit full-pair height bound is obtained, but it is only $O(d^2\log d)$, not the requested


$$
\frac54d^2+O(d\log d).
$$



The common-minor lower bounds and paid integral descent in FULL17 Section 8 are awaiting their assigned different audit. I do not self-audit them here. Algebraic identities involving that descent are proved over $\mathbb Q$; their asserted integer normalization is used only under the explicit Section-8 handoff hypothesis stated below.

---

# Part I. Different audit of the new all-precision and period candidates

## 1. Original scope and reused contact identities

Throughout,


$$
\boxed{k=9^{18+32u},\quad u\ge0,\qquad d=k-1.}
$$


In particular,


$$
v_2(d)=4,\qquad d\equiv208\pmod{256},\qquad d\equiv2\pmod3.
$$



Retain


$$
a_0=1,\qquad a_n=1-na_{n-1},\qquad u_m=a_{2m},
$$


and the already proved integral contact identities


$$
\theta_r=\frac{\Delta^r u_0}{2^rr!},
\qquad
\theta_0=1,\quad\theta_1=0,\quad
\theta_{r+1}=(2r+1)\theta_r+\theta_{r-1}.
\tag{1.1}
$$


For every nonnegative physical base $m$,


$$
\boxed{
\theta_r^{(m)}
=\frac{\Delta^r u_m}{2^rr!}
=\sum_{v=0}^{m}\binom mv2^v(r+1)_v\theta_{r+v}.
}
\tag{1.2}
$$



These are reused at their proved integral scope. No factorial is inverted modulo a power of $2$.

The original return columns remain $0\le r<d$. Theta order $r=d$, when used below, is the already paid re-expression of the terminal return/border transformation, not an additional original return.

---

## 2. Formal ODE and the precision-contractive remainder

Let


$$
F(Y)=\sum_{n\ge0}\theta_nY^n\in\mathbb Z[[Y]].
$$


Summing (1.1) for $n\ge1$ gives


$$
F-1
=Y(2YF'+F-1)+Y^2F.
$$


Therefore


$$
\boxed{(1-Y-Y^2)F-2Y^2F'=1-Y.}
\tag{2.1}
$$



This derivation takes place in the ring of formal series. It does not use complex convergence.

Put


$$
S=1+Y+Y^2,
\qquad
\mathcal TH=\frac{(Y+Y^2)H+Y^2H'}S,
\qquad
f_0=\frac{1+Y}{S}.
$$


Since $S(0)=1$, both $S^{-1}$ and $\mathcal TH$ have integer coefficients whenever $H$ does. Equation (2.1) is equivalent to


$$
F=f_0+2\left(\mathcal TF-\frac YS\right).
$$



A direct calculation checks the claimed inhomogeneous term. Indeed,


$$
f_0'=\frac{-2Y-Y^2}{S^2},
$$


and hence


$$
\mathcal Tf_0-\frac YS
=
\frac{Y^2-Y^3}{S^3}
=:U.
$$


Thus, with $E=F-f_0$,


$$
\boxed{E=2U+2\mathcal TE.}
\tag{2.2}
$$



There is a small point worth making explicit in the remainder argument: (2.2) first proves $E\in2\mathbb Z[[Y]]$. Iterating it $h-1$ times then gives


$$
E=\sum_{j=0}^{h-2}2^{j+1}\mathcal T^jU
  +2^{h-1}\mathcal T^{h-1}E,
$$


and the last term belongs to $2^h\mathbb Z[[Y]]$. Consequently


$$
\boxed{
F\equiv f_0+\sum_{j=0}^{h-2}2^{j+1}\mathcal T^jU
\pmod{2^h},\qquad h\ge1.
}
\tag{2.3}
$$


The sum is empty when $h=1$.

**Verdict: PASS.** The remainder is coefficientwise precision-contractive. It is not an analytic remainder.

---

## 3. Integer numerator recursion and all modulo-$16$ carries

Write


$$
\mathcal T^jU=\frac{N_j}{S^{3+2j}}.
$$


Applying $\mathcal T$ to this quotient gives


$$
\boxed{
N_{j+1}
=(Y+Y^2)N_jS+Y^2N_j'S-(3+2j)Y^2N_jS',
\qquad N_0=Y^2-Y^3.
}
\tag{3.1}
$$


Every operation is in $\mathbb Z[Y]$. In particular, this is an **integer** recursion.

The first term has degree at most $\deg N_j+4$, and the other two have degree at most $\deg N_j+3$. Therefore


$$
\deg N_j\le3+4j.
\tag{3.2}
$$



### 3.1 Independent check of $N_1$

For $N_0=Y^2-Y^3$, the three contributions in (3.1) are


$$
Y^3+Y^4-Y^6-Y^7,
$$




$$
2Y^3-Y^4-Y^5-3Y^6,
$$


and


$$
-3Y^4-3Y^5+6Y^6.
$$


Their sum is


$$
\boxed{N_1=3Y^3-3Y^4-4Y^5+2Y^6-Y^7.}
\tag{3.3}
$$



### 3.2 Independent check of $N_2\bmod2$

Modulo $2$,


$$
\overline{N_1}=Y^3+Y^4+Y^7,\qquad
\overline{N_1'}=Y^2+Y^6,
$$


and


$$
(Y+Y^2)S=Y+Y^4,\qquad S'=1.
$$


Thus


$$
\overline{N_2}
=(Y+Y^4)\overline{N_1}
 +Y^2S\overline{N_1'}
 +Y^2\overline{N_1},
$$


which simplifies to


$$
\boxed{\overline{N_2}=Y^5+Y^7+Y^8+Y^{10}+Y^{11}.}
\tag{3.4}
$$



Consequently


$$
\boxed{
\begin{aligned}
F\equiv{}&
\frac{1+Y}{S}
+\frac{2Y^2(1-Y)}{S^3}\\
&+\frac{4(3Y^3-3Y^4-4Y^5+2Y^6-Y^7)}{S^5}\\
&+\frac{8(Y^5+Y^7+Y^8+Y^{10}+Y^{11})}{S^7}
\pmod{16}.
\end{aligned}}
\tag{3.5}
$$



The coefficient-$4$ term really requires $N_1\bmod4$, not merely its parity:


$$
N_1\equiv3Y^3+Y^4+2Y^6+3Y^7\pmod4.
$$


In particular, the $2Y^6$ carry cannot be deleted.

For later use, (2.3) can be written


$$
F\equiv \frac{P_h(Y)}{S^{2h-1}}\pmod{2^h},
\qquad P_h\in\mathbb Z[Y],
\tag{3.6}
$$


with the explicit bound


$$
\boxed{\deg P_h\le4h-3=2(2h-1)-1.}
\tag{3.7}
$$


This follows by clearing the denominator in each term of (2.3).

**Verdict: PASS.** The degree bound is a formal rational-representation bound. It is not a determinant-valuation bound, nor is $S^{2h-1}$ an arithmetic least clearer or the primitive denominator $q_k$.

---

## 4. Hasse extraction and the actual physical sources

Define the Hasse derivative by


$$
F(Y+Z)=\sum_{j\ge0}Z^j\partial^{[j]}F(Y).
$$


Then


$$
\partial^{[j]}F(Y)
=\sum_{r\ge0}\binom{r+j}{r}\theta_{r+j}Y^r.
$$


Thus, for


$$
B_j(r)=\binom{r+j}{r}\theta_{r+j},
\qquad
K_b(z,r)=\sum_{t=0}^b\binom btB_{z+t}(r),
$$


one has


$$
\boxed{
\sum_{r\ge0}B_j(r)Y^r=\partial^{[j]}F(Y),
}
$$




$$
\boxed{
\sum_{r\ge0}K_b(z,r)Y^r
=[Z^{z+b}](1+Z)^bF(Y+Z).
}
\tag{4.1}
$$


The second formula follows by reversing $t$ and $b-t$ in the finite binomial sum.

These are integral coefficient-extraction identities. There is no division by $j!$.

### 4.1 Physical-base extraction

Multiplying (1.2) by $\binom{r+s}{r}$, and using


$$
\binom{r+s}{r}(r+s+1)_v
=(s+1)_v\binom{r+s+v}{r},
$$


gives


$$
\boxed{
\binom{r+s}{r}\theta_{r+s}^{(m)}
=\sum_{v=0}^m
 \binom mv2^v(s+1)_vB_{s+v}(r).
}
\tag{4.2}
$$



Let


$$
\lambda_v=v+v_2(v!)=2v-s_2(v),
\qquad
\nu(H)=\max\{v\ge0:\lambda_v<H\}.
\tag{4.3}
$$


Since $v!\mid(s+1)_v$, every term with $\lambda_v\ge H$ vanishes modulo $2^H$. Thus the physical sum may be truncated at


$$
v\le\min(m,\nu(H)).
$$


This truncation is paid by an integer divisibility statement, not by cancellation of a factorial denominator.

### 4.2 Exact top extraction

Use the already passed notation


$$
P_d(x)=\prod_{h=0}^{d-1}(2x+2h+1),\qquad
\mathcal A_dy=\Delta^d(P_dy),
$$




$$
R_j=(d+1)_j,\qquad
o_d=\frac{d!}{2^{v_2(d!)}},
\qquad
Q_\ell(a)=\prod_{t=\ell}^{d-1}(2a+2t+1).
$$


For


$$
T_j^{(a)}(r)
=\frac{\Delta^j\mathsf v_a^{(r)}}{2^jR_j},
$$


the passed exact top identity is


$$
T_j^{(a)}(r)
=o_d\sum_{\ell=0}^d
 \binom d\ell Q_\ell(a)
 \binom{d-\ell+r+j}{r}
 \theta_{d-\ell+r+j}^{(a+\ell)}.
$$


Applying (4.2) proves


$$
\boxed{
\frac{T_j^{(a)}}{o_d}
\longleftrightarrow
\sum_{\ell=0}^d\binom d\ell Q_\ell(a)
\sum_{v=0}^{a+\ell}
 \binom{a+\ell}{v}2^v(j+d-\ell+1)_v
 \partial^{[j+d-\ell+v]}F.
}
\tag{4.4}
$$



The exact admitted range is


$$
a+j\le d-1,\qquad 0\le r\le d.
$$


Every theta coefficient used on the right satisfies


$$
r+j+d-\ell+v\le r+j+d+a\le3d-1.
$$


Thus the representation does not introduce a new physical moment.

### 4.3 Arbitrary actual pole source

Let


$$
I\subseteq\{0,\ldots,d-1\},\qquad |I|=p,
$$




$$
Q_I(i)=\prod_{t\in I}(2(d+i+t)+1),
\qquad
J_\ell=\frac{\Delta^\ell Q_I(0)}{2^\ell\ell!}.
$$


The exact bottom identity, at $j=p+z$, is


$$
V_z^I(r)
=\sum_{\ell=0}^pJ_\ell
 \binom{r+j-\ell}{r}
 \theta_{r+j-\ell}^{(d+\ell)}.
$$


Hence


$$
\boxed{
V_z^I\longleftrightarrow
\sum_{\ell=0}^pJ_\ell
\sum_{v=0}^{d+\ell}
 \binom{d+\ell}{v}2^v(j-\ell+1)_v
 \partial^{[j-\ell+v]}F.
}
\tag{4.5}
$$



The physical base is literally $d+\ell$. It has not been replaced by $d$, $0$, or a free parameter.

For


$$
p\le j\le d+1,\qquad 0\le r\le d,
$$


the largest coefficient index is


$$
r+j-\ell+v\le r+j+d\le3d+1.
$$



### 4.4 An explicit all-precision pole-carry formula

The source candidate assumes the established integrality of $J_\ell$. It is useful to record a fully explicit all-precision form.

Put $x_t=d+t$, and let $e_a(x_I)$ be the elementary symmetric polynomial in the actual $x_t$, $t\in I$. Writing $Q_I$ as a polynomial in $2i$ gives


$$
J_\ell
=\sum_{q=\ell}^p2^{q-\ell}
 e_{p-q}(1+2x_I)\,S(q,\ell).
$$


Expanding the elementary symmetric coefficient yields


$$
\boxed{
J_\ell
=
\sum_{q=\ell}^p\ \sum_{a=0}^{p-q}
2^{q-\ell+a}
S(q,\ell)\binom{p-a}{q}e_a(x_I).
}
\tag{4.6}
$$


Here $S(q,\ell)$ is a Stirling number of the second kind.

At precision $2^H$, terms with $q-\ell+a\ge H$ may be omitted. All other Stirling and elementary-symmetric carries remain. Formula (4.6) applies to every actual $I$, including the endpoint cases $p=0$ and $p=d$.

**Verdict: PASS.** The Hasse, physical, top, and arbitrary-pole source claims are valid at their literal finite boundaries. The atom and the constant border are not supplied by $F$; they require their own exact formulas.

---

## 5. Complete top and atom normalization modulo $16$

The hypothesis needed here is $v_2(d)=4$, which holds on every original index.

Write $c_\ell=\binom d\ell$. For $0<\ell<d$,


$$
\ell c_\ell=d\binom{d-1}{\ell-1},
\qquad
(d-\ell)c_\ell=d\binom{d-1}{\ell}.
$$


Thus, if $t=v_2(c_\ell)\le3$, then


$$
2^{4-t}\mid\ell,\qquad 2^{4-t}\mid d-\ell.
\tag{5.1}
$$


The endpoint terms satisfy the corresponding assertions directly.

### 5.1 Removal of $Q_\ell(a)$ is weighted, not unqualified

A product of $d-\ell$ consecutive odd factors, where $2^{4-t}\mid d-\ell$, is $1$ modulo $2^{4-t}$. For modulus $4$, two complete odd-residue cycles are present; for modulus at least $8$, the product of all odd residues is already $1$.

Therefore


$$
c_\ell Q_\ell(a)\equiv c_\ell\pmod{16}.
\tag{5.2}
$$


It would be incorrect to assert $Q_\ell(a)\equiv1\pmod{16}$ for every $\ell$ without its binomial weight.

### 5.2 The physical terms $v=0,1,2$

Terms $v\ge3$ vanish modulo $16$, since $\lambda_3=4$ and $\lambda_v$ is increasing.

For $v=1$, the difference between the literal weight and its simplified weight is


$$
\begin{aligned}
&2c_\ell\bigl((a+\ell)(j+d-\ell+1)-a(j+1)\bigr)\\
&\qquad
=2c_\ell\bigl(\ell(j+1)+(a+\ell)(d-\ell)\bigr).
\end{aligned}
$$


Both $c_\ell\ell$ and $c_\ell(d-\ell)$ are divisible by $16$, so this difference vanishes modulo $16$.

For $v=2$, the factor


$$
4(j+d-\ell+1)(j+d-\ell+2)
$$


already has valuation at least $3$. Consequently only odd $c_\ell$ can contribute. In that case $\ell$ and $d-\ell$ are multiples of $16$; replacing $a+\ell$ by $a$ in $\binom{a+\ell}{2}$, and $j+d-\ell$ by $j$, preserves the required residue.

Summing the resulting integer filters gives


$$
\boxed{
\frac{T_j^{(a)}}{o_d}
\equiv
K_d(j)+2a(j+1)K_d(j+1)
+4\binom a2(j+1)(j+2)K_d(j+2)
\pmod{16}.
}
\tag{5.3}
$$



This is valid for every admitted $a,j,r$, including a literal odd base such as $a=d-p$. It does not authorize replacing that base by $0$.

### 5.3 The atom and its rising ratios

The exact $w$-atom jet is


$$
A_j^{(a)}
=(-1)^{a+j}
\sum_{\ell=0}^d
 \binom{d+j}{\ell}\frac{d!}{(d-\ell)!}Q_\ell(a).
$$


Every $\ell\ge1$ term contains $d$, hence vanishes modulo $16$. The $\ell=0$ product has length divisible by $16$, and is $1\bmod16$. Thus


$$
\boxed{A_j^{(a)}\equiv(-1)^{a+j}\pmod{16}.}
\tag{5.4}
$$



In a complete normalized source-jet row, the atom is still


$$
\frac{R_m}{R_j}\frac{A_j^{(a)}}{o_d}.
$$


Neither $R_m/R_j$ nor $o_d$ is replaced by $1$.

The formula is for the $w$-atom. For the actual $c=u-w$ atom,


$$
\frac{\mathcal A_dc}{2^d}
=
2^{\alpha-d}\mathsf v^{(0)}-\mathsf a_w,
$$


so


$$
\frac{\Delta^j(\mathcal A_dc/2^d)}{2^j}
=
2^{\alpha-d}R_jT_j^{(a)}(0)-A_j^{(a)}.
\tag{5.5}
$$


On the original domain $\alpha-d=v_2(d!)\ge4$, and hence this atom is the negative of (5.4) modulo $16$, with all subsequent rising ratios and odd local units retained.

**Verdict: PASS, with a scope clarification.** The parent formula is a $w$-atom formula. Its application to the actual $c$-atom must use (5.5). It is not a formula for the constant border $r=-f+4\rho$.

---

## 6. Uniform modulo-$8$ period: a different product calculation

Set


$$
M(n)=\begin{pmatrix}2n+1&1\\1&0\end{pmatrix},
\qquad
P_T(n)=M(n+T-1)\cdots M(n).
$$


For $n\ge1$, this carries


$$
(\theta_n,\theta_{n-1})^t
\quad\text{to}\quad
(\theta_{n+T},\theta_{n+T-1})^t.
$$



The following verifies all starting phases without repeating a finite table of products.

Put $a=2n+1$, and


$$
B(a)=M(n+1)M(n)
=
\begin{pmatrix}(a+1)^2&a+2\\a&1\end{pmatrix}.
$$


Exactly,


$$
\det B(a)=1.
$$


Modulo $8$,


$$
B(a+8)=B(a),\qquad
B(a+4)=B(a)+4J,
\quad
J=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
$$


Therefore


$$
P_6(n)\equiv B(a)^3+4B(a)JB(a)\pmod8.
$$



Modulo $2$,


$$
B(a)=\begin{pmatrix}0&1\\1&1\end{pmatrix},
\qquad
B(a)JB(a)=J.
$$


If $\tau=\operatorname{tr}B(a)=(a+1)^2+1$, Cayley–Hamilton gives


$$
B(a)^3=(\tau^2-1)B(a)-\tau I.
$$


Since $\tau$ is odd, $\tau^2\equiv1\pmod8$, and


$$
-\tau\equiv2a+1\pmod8.
$$


Thus


$$
\boxed{
P_6(n)\equiv(4n+3)I+4J\pmod8.
}
\tag{6.1}
$$



This is exactly the two-phase table in the candidate. It also proves the table for all integer phases at once.

The already established modulo-$4$ anti-period is recovered as


$$
P_6(n)\equiv-I\pmod4;
$$


it is **REUSE** here.

Since $n$ and $n+6$ have the same parity, the two six-step matrices agree modulo $8$, and their square is $I$. Hence


$$
\boxed{P_{12}(n)\equiv I\pmod8}
\tag{6.2}
$$


uniformly in $n$.

Applying the second coordinate of (6.1) at starting index $n+1$ gives, for $n\ge0$,


$$
\boxed{
\theta_{n+6}
\equiv
\{-1+4(n\bmod2)\}\theta_n+4\theta_{n+1}\pmod8.
}
\tag{6.3}
$$


This includes $\theta_0$ without introducing a negative-index state.

The resulting tables are


$$
\theta_n\bmod4=(1,0,1,1,0,1,3,0,3,3,0,3),
$$




$$
\theta_n\bmod8=(1,0,1,5,4,1,7,4,3,7,0,7).
$$



**Verdict: PASS.** Period $12$ modulo $8$ is uniform. No minimal-period assertion is made.

---

## 7. All-phase lifting to $T_h=3\cdot2^{h-1}$

For odd $a$, define the integral matrix polynomial


$$
\mathcal P_T(a)
=\prod_{j=T-1}^{0}
 \begin{pmatrix}a+2j&1\\1&0\end{pmatrix}.
$$


Modulo $2$, every factor equals


$$
A=\begin{pmatrix}1&1\\1&0\end{pmatrix},
\qquad A^3=I.
$$


With $E=\operatorname{diag}(1,0)$,


$$
\mathcal P_T'(a)
\equiv
\sum_{j=0}^{T-1}A^{T-1-j}EA^j\pmod2.
\tag{7.1}
$$


Each summand has period $3$ in $j$. If $6\mid T$, each of the three classes occurs an even number of times. Therefore


$$
\boxed{\mathcal P_T'(a)\in2M_2(\mathbb Z)}
\tag{7.2}
$$


for every odd $a$.

Suppose $h\ge3$, $T=3\cdot2^{h-1}$, and $P_T(n)\equiv I\pmod{2^h}$ for every $n$. The change $n\mapsto n+T$ changes $a$ by $2T$, of valuation $h$.

Expand each entry of the integral polynomial $\mathcal P_T(a+2T)$ by the ordinary binomial theorem. The linear term contains the extra factor $2$ from (7.2); every term of degree at least two contains $(2T)^2$. Thus


$$
P_T(n+T)\equiv P_T(n)\pmod{2^{h+1}}.
$$


No Taylor factorial is divided out.

It follows that


$$
P_{2T}(n)
=P_T(n+T)P_T(n)
\equiv P_T(n)^2
\equiv I\pmod{2^{h+1}}.
$$


The base $h=3,T=12$ is (6.2). Induction proves


$$
\boxed{
\theta_{n+3\cdot2^{h-1}}\equiv\theta_n\pmod{2^h},
\qquad h\ge3,\ n\ge0.
}
\tag{7.3}
$$



**Verdict: PASS.** The derivative cancellation and the induction are both all-phase statements. No hypothesis about a particular initial phase is missing.

---

## 8. Audit ledger

| Claim | Verdict |
|---|---|
| Exact formal ODE | **PASS** |
| Coefficientwise precision-contractive remainder | **PASS**, with $E\in2\mathbb Z[[Y]]$ explicitly used |
| Integer numerator recursion | **PASS** |
| $N_1$, $N_2\bmod2$, and modulo-$16$ carries | **PASS** |
| Denominator $S^{2h-1}$ and linear numerator-degree bound | **PASS as a representation bound only** |
| Integral Hasse extraction | **PASS** |
| Arbitrary actual pole source | **PASS**, including the literal base $d+\ell$ |
| All-precision pole carries | **Explicitly evaluated in (4.6)** |
| Top modulo-$16$ law | **PASS** under $v_2(d)=4$ and the actual top boundary |
| Atom modulo-$16$ law | **PASS**, retaining $R_m/R_j$ and $o_d$ |
| Application to the $c$-atom | **Scope repair supplied by (5.5)** |
| Modulo-$4$ anti-period | **REUSE** |
| Uniform period $12$ modulo $8$ | **PASS** |
| All-phase higher lifting | **PASS** for $h\ge3$ |
| Exact two-dimensional terminal reduction | **OPEN; not implied** |
| Full paired valuation upper | **OPEN** |

The auxiliary receipts are not used to prove any item in this table. In particular, two residual directions at precision $12$ in the three auxiliary minimal-source matrices do not establish an exact kernel, an original-index reduction, or a complete paired upper.

---

# Part II. The actual corrected pencil and the Section-8 handoff

## 9. Complete original data and finite boundaries

Retain


$$
f_n=(2n)!,\qquad w_n=(-1)^n,\qquad c_n=u_n-w_n,
$$




$$
\rho_0=0,\qquad \rho_{n+1}+\rho_n=\frac1{2n+1},
\qquad r_n=-f_n+4\rho_n.
$$


The two complete returns are


$$
\sigma_n=u_{n+1}+u_n=c_{n+1}+c_n,
$$




$$
\boxed{\tau_n=-(2n+2)!-(2n)!+\frac4{2n+1}.}
\tag{9.1}
$$


Set


$$
\Lambda_k=\operatorname{lcm}(1,3,\ldots,6k-5),
\qquad T_n=\Lambda_k\tau_n.
$$



The finite ranges are unchanged:

- top source rows $0\le a<d$;
- original return orders $0\le r<d$;
- residual rows $0\le i\le d+1$, physical row $d+i$;
- last physical row $2d+1$;
- largest moment $3d+1$;
- terminal factorial $(6k-4)!$;
- terminal odd denominator $6k-5$.

Write $\mathbf K_d$ for the forcing matrix, to distinguish it from the integer filters $K_b(z,r)$. The full top forcing is


$$
F_k=-\Lambda_kD_f\mathbf K_dD_f,
\qquad D_f=\operatorname{diag}((2a)!)_{a<d},
$$


or entrywise


$$
F_k(a,j)=
-\Lambda_k\sum_{\ell=0}^d(-1)^\ell\binom d\ell
P_d(a+\ell)b(a+\ell+j)(2(a+\ell+j))!,
$$


where


$$
b(t)=4t^2+6t+3,\qquad b(t)(2t)!=(2t+2)!+(2t)!.
$$



Retain


$$
h_d=(2d-2)!,\qquad
\beta=v_2(h_d),\qquad
\alpha=v_2((2d)!)=\beta+5,
$$




$$
N_d=(h_dD_f^{-1})\operatorname{adj}(\mathbf K_d)(h_dD_f^{-1}),
$$




$$
\eta_d^F=\det\mathbf K_d,\qquad
\delta_k=\Lambda_k\eta_d^Fh_d^2,\qquad
F_k^{-1}=-N_d/\delta_k.
$$


The established oddness statements for the relevant $\mathbf K_d$-determinants are reused.

The full bottom forcing is


$$
\boxed{
R(i,j)=
\frac{\Lambda_k}{2(d+i+j)+1}
-\frac{\Lambda_k}{4}b(d+i+j)(2(d+i+j))!.
}
\tag{9.2}
$$


Equivalently,


$$
R=R^{\rm C}-2^{\alpha-2}V.
$$


The factorial correction $V$ is not deleted.

Define


$$
\mathscr T(y)
=RN_d(\mathcal A_dy)_{\rm top}+\frac{\delta_k}{4}y_{\rm bot},
\qquad
D_r=2^rr!.
\tag{9.3}
$$


Then the complete corrected columns are


$$
x=\frac{\mathscr T(c)}{2^d},
\qquad
z^{(r)}=\frac{\mathscr T(\Delta^r\sigma)}{2^{\alpha+1}D_r},
\quad 0\le r<d,
$$




$$
\mathfrak b_0=\Lambda_k\mathscr T(r),
\qquad
\mathfrak b_1=\Lambda_k\mathscr T(w).
\tag{9.4}
$$


Thus


$$
\mathcal Q_k(s)
=[x,z^{(0)},\ldots,z^{(d-1)},\mathfrak b_0+s\mathfrak b_1].
$$



All the displayed return and atom divisions are the already paid divisions in the original corrected pencil.

---

## 10. Accepted half-size input and the pending integral handoff

The differently passed first-wrap/cofactor theorem is used as an actual input, without repeating its proof.

On infinitely many original indices satisfying


$$
\frac98\,2^{a_k}<k<\frac{17}{15}\,2^{a_k},
\qquad a_k=\lfloor\log_2k\rfloor\ \text{even},
$$


and the stated sufficiently-large threshold, it supplies an attaining block of size


$$
\boxed{q=\frac d2-m_d-1,\qquad m_d=1+\lfloor\log_2d\rfloor.}
\tag{10.1}
$$



For clarity, the payment notation is


$$
\lambda_j=j+v_2(j!),\qquad S_n=\sum_{j=0}^{n-1}\lambda_j,
$$




$$
e_n=v_2\!\left(\frac{h_d}{(2n)!}\right),\qquad
E_b=\sum_{n=d-b}^{d-1}e_n,
$$




$$
B_b=\binom b2+\sum_{j=0}^{b-2}v_2((d+1)_j),
$$




$$
f_q=F_q(p)
=(q-p)L_d+S_p+S_q+2E_p+B_p,
\qquad L_d=\alpha-12.
\tag{10.2}
$$


Here $p$ is the actual minimizing count supplied by the accepted theorem, including the equality-tie case.

Choose an actual attaining $q$-minor $A$ on the first $q$ residual rows, containing the atom and $q-1$ original return columns. Then


$$
\det A=2^{f_q}\mu_A,\qquad \mu_A\ \text{an actual odd integer}.
\tag{10.3}
$$


The full value of $\mu_A$, not merely its parity, remains in every construction.

Write the common rectangle and both bordered matrices in block form:


$$
\mathcal Q_h=
\begin{pmatrix}
A&B&u_h\\
C_0&D_0&v_h
\end{pmatrix},
\qquad h=0,1.
$$


Put


$$
t=d+1-q,\qquad s=t+1=d+2-q=\frac d2+m_d+3.
\tag{10.4}
$$



### Section-8 handoff hypothesis $\mathrm{H8}$

The assigned different audit must validate the following integral outputs:


$$
K_A=\frac{C_0\operatorname{adj}A}{2^{f_q}}\in M_{s,q}(\mathbb Z),
$$




$$
E_A=\mu_AD_0-K_AB,\qquad
e_h=\mu_Av_h-K_Au_h,
$$




$$
c=L_d+\lambda_q,\qquad
\widehat E_A=E_A/2^c\in M_{s,t}(\mathbb Z),
$$




$$
\widehat e_0=e_0/2^{d+1}\in\mathbb Z^s,\qquad
\widehat e_1=e_1/2^d\in\mathbb Z^s.
\tag{10.5}
$$



I do not prove these common-minor lower bounds or their division payments here.

Under $\mathrm{H8}$, define


$$
J_h=\det[\widehat E_A,\widehat e_h].
$$


The algebraic block identity is


$$
\boxed{
|\mu_A|^t g_{\mathcal Q,k}
=
2^{\mathcal E_q}\gcd(2|J_0|,|J_1|),
\qquad
\mathcal E_q=f_q+tc+d.
}
\tag{10.6}
$$


The reported evaluated extraction is


$$
\mathcal E_q=\frac52d^2+O(dm_d).
\tag{10.7}
$$



The remainder of this report applies the newly audited source representation to this **actual** block. It does not replace it by a minimal theta-source matrix.

---

# Part III. A proved literal-source recurrence for the actual residual pair

## 11. Exact theta-to-return identities in the original pencil

Let


$$
\mathfrak a=\alpha-d=v_2(d!),
$$




$$
v^{(r)}=\frac{\mathscr T(\Delta^ru)}{2^\alpha D_r},
\quad 0\le r\le d,
\qquad
w_*=\frac{\mathscr T(w)}{2^d}.
$$


Then


$$
\boxed{x=2^{\mathfrak a}v^{(0)}-w_*.}
\tag{11.1}
$$



Since


$$
\sigma=\Delta u+2u
$$


and


$$
D_{r+1}=2(r+1)D_r,
$$


one obtains the exact identity


$$
\boxed{z^{(r)}=v^{(r)}+(r+1)v^{(r+1)},\qquad 0\le r<d.}
\tag{11.2}
$$


This uses an integer ratio of the full return divisors. No odd factorial quotient is discarded.

The two borders remain


$$
\boxed{
\mathfrak b_0=\Lambda_k\mathscr T(-f+4\rho),
\qquad
\mathfrak b_1=\Lambda_k2^dw_*.
}
\tag{11.3}
$$



These identities are the starting point for a source-specific residual recurrence.

---

## 12. The actual one-shot row functional

Define the row operation on residual vectors by


$$
\Omega_A(y)_i
=\mu_Ay_{q+i}-\sum_{b=0}^{q-1}K_A(i,b)y_b,
\qquad 0\le i<s.
\tag{12.1}
$$


Over $\mathbb Q$, this definition and the following identities are valid for every nonzero pivot $A$. Under $\mathrm{H8}$, they are integral at the stated normalizations.

By construction,


$$
\Omega_A(A\text{-columns})=0.
\tag{12.2}
$$



Put


$$
U_{i,a}
=\mu_A(RN_d)_{q+i,a}
-\sum_{b=0}^{q-1}K_A(i,b)(RN_d)_{b,a}.
\tag{12.3}
$$


Define a finite functional


$$
\mathscr L_{A,i}(y)=\Omega_A(\mathscr T(y))_i.
$$


It has the explicit physical expansion


$$
\boxed{
\mathscr L_{A,i}(y)
=\sum_{m=0}^{2d+1}\ell_{i,m}y_m,
}
\tag{12.4}
$$


where


$$
\begin{aligned}
\ell_{i,m}={}&
P_d(m)
\sum_{\substack{0\le a<d\\0\le m-a\le d}}
U_{i,a}(-1)^{d-(m-a)}
\binom d{m-a}\\
&+\frac{\delta_k}{4}
\left(
\mu_A\,\mathbf1_{m=d+q+i}
-\sum_{b=0}^{q-1}K_A(i,b)\mathbf1_{m=d+b}
\right).
\end{aligned}
\tag{12.5}
$$



This formula is obtained simply by expanding


$$
\mathcal A_dy(a)
=\sum_{\ell=0}^d(-1)^{d-\ell}\binom d\ell
P_d(a+\ell)y_{a+\ell}.
$$


It is a finite exact formula with support at most $2d+1$.

The provenance of its coefficients still includes the full $R$, hence the physical forcing terminal $3d+1$. No part of $R^{\rm C}-2^{\alpha-2}V$, $N_d$, $\mu_A$, or $K_A$ has been replaced by a leading approximation.

Set


$$
W^{(r)}=\Omega_A(v^{(r)})\in\mathbb Q^s.
\tag{12.6}
$$


Then


$$
E_A^{(r)}=W^{(r)}+(r+1)W^{(r+1)}
\tag{12.7}
$$


on each unselected original return order $r$.

Because the pivot includes $x$, (11.1) and (12.2) imply


$$
\Omega_A(w_*)=2^{\mathfrak a}W^{(0)}.
$$


Therefore the normalized linear border has the exact form


$$
\boxed{\widehat e_1=\Lambda_k2^{\mathfrak a}W^{(0)}.}
\tag{12.8}
$$



This is an actual consequence of the selected atom pivot. It is an additional lower factor, not an upper bound for $J_1$.

---

## 13. Factorial-paid path contraction: the residual dimension is $s$, not two

Let the unselected original return orders be


$$
\mathcal R=\{r_1<\cdots<r_t\}.
$$


The selected return orders are the other $q-1$ edges of the path on vertices


$$
0,1,\ldots,d.
$$



For a selected return order $r$, (12.2) and (11.2) give


$$
W^{(r)}+(r+1)W^{(r+1)}=0.
$$


Multiplying by $r!$,


$$
r!W^{(r)}+(r+1)!W^{(r+1)}=0.
\tag{13.1}
$$


Thus


$$
(-1)^rr!W^{(r)}
$$


is constant on each connected component of the path after the unselected edges are removed.

There are exactly $t+1=s$ such components. Their initial vertices are


$$
a_0=0,\qquad a_j=r_j+1\quad(1\le j\le t).
$$


Define their actual vector values


$$
\boxed{
Z_j=(-1)^{a_j}a_j!W^{(a_j)},\qquad 0\le j\le t.
}
\tag{13.2}
$$



For an unselected edge $r_j$,


$$
\boxed{
(-1)^{r_j}r_j!E_A^{(r_j)}=Z_{j-1}-Z_j.
}
\tag{13.3}
$$


No factorial has been divided out. Every odd factorial factor remains in this identity.

Let


$$
\mathfrak F_{\mathcal R}
=\prod_{j=1}^t(-1)^{r_j}r_j!.
$$


With the remaining return columns ordered increasingly, (13.3) proves


$$
\boxed{
2^{ct}\mathfrak F_{\mathcal R}J_0
=
\det[Z_0-Z_1,\ldots,Z_{t-1}-Z_t,\widehat e_0],
}
\tag{13.4}
$$


and, using (12.8),


$$
\boxed{
2^{ct}\mathfrak F_{\mathcal R}J_1
=
\Lambda_k2^{\mathfrak a}\det[Z_0,\ldots,Z_t].
}
\tag{13.5}
$$



For (13.5), the elementary incidence determinant is


$$
\det[Z_0-Z_1,\ldots,Z_{t-1}-Z_t,Z_0]
=\det[Z_0,\ldots,Z_t].
$$


It follows either by successive column additions or by expansion in the standard basis of the $Z_j$.

Equations (13.3)–(13.5) are an exact finite compression of the **actual selected-return relations**. They do not assert that any new quotient is integral unless its divisibility has already been paid.

They also explain why a two-dimensional conclusion is unavailable: the selected edges leave $s$ components, not two. To reduce further would require additional paid pivots and a proof of their actual valuations. The auxiliary precision-$12$ receipts do not supply those pivots.

Indeed, the established nonvanishing of $I_{1,k}$, together with the exact descent identity, makes the complete residual linear-border matrix nonsingular over $\mathbb Q$. Its literal rank is $s$, not $2$. A future “two-dimensional reduction” could only mean a further **paid elimination**, not a rank-two assertion about this matrix.

---

## 14. Both complete borders have explicit backward recurrences

The constant border can be evaluated without treating it as an unexplained source symbol.

Fix a residual row $i$, put


$$
N=2d+1,
$$


and use the coefficients $\ell_{i,m}$ from (12.5).

### 14.1 Alternating reciprocal source

Define


$$
C_{i,N}=0,\qquad
C_{i,t}=\ell_{i,t+1}-C_{i,t+1},
\quad t=N-1,\ldots,0.
\tag{14.1}
$$


Then


$$
C_{i,t}
=\sum_{m=t+1}^{N}(-1)^{m-1-t}\ell_{i,m}.
$$


Since


$$
\rho_m=\sum_{t=0}^{m-1}\frac{(-1)^{m-1-t}}{2t+1},
$$


finite interchange gives


$$
\sum_{m=0}^{N}\ell_{i,m}\rho_m
=\sum_{t=0}^{N-1}\frac{C_{i,t}}{2t+1}.
\tag{14.2}
$$



To clear these reciprocals using only actual original clearers, define


$$
R_{i,N}=0,\qquad
R_{i,t}=R_{i,t+1}
+C_{i,t}\frac{\Lambda_k}{2t+1},
\quad t=N-1,\ldots,0.
\tag{14.3}
$$


Every $\Lambda_k/(2t+1)$ is an integer: the largest denominator here is $4d+1$, below the retained $6d+1=6k-5$.

Thus $R_{i,0}$ is the complete cleared reciprocal contribution. No product denominator is incorrectly asserted to divide $\Lambda_k$.

### 14.2 Factorial source

Define


$$
X_{i,N}=\ell_{i,N},
$$




$$
X_{i,m}
=\ell_{i,m}+(2m+2)(2m+1)X_{i,m+1},
\quad m=N-1,\ldots,0.
\tag{14.4}
$$


Induction gives


$$
X_{i,m}
=\sum_{n=m}^{N}\ell_{i,n}\frac{(2n)!}{(2m)!}.
$$


In particular,


$$
X_{i,0}=\sum_{n=0}^{N}\ell_{i,n}(2n)!.
\tag{14.5}
$$


This recurrence uses no factorial division in its implementation and no moment beyond $N$.

### 14.3 The complete pair

Combining the two recurrences proves


$$
\boxed{
2^{d+1}\widehat e_{0,i}
=-\Lambda_kX_{i,0}+4R_{i,0}.
}
\tag{14.6}
$$


The two terms on the right are both retained.

For the linear border,


$$
\sum_{m=0}^{N}(-1)^m\ell_{i,m}
=\ell_{i,0}-C_{i,0},
$$


so


$$
\boxed{
2^d\widehat e_{1,i}
=\Lambda_k(\ell_{i,0}-C_{i,0}).
}
\tag{14.7}
$$



Under $\mathrm{H8}$, the divisions by $2^{d+1}$ and $2^d$ in these formulas are exactly the already asserted border payments. The recurrences do not manufacture a new division.

### 14.4 Compatibility with both original returns

For each $0\le j<d$,


$$
(\mathcal A_dT_{\bullet+j})_{\rm top}=F_k(:,j),
\qquad
(T_{\bullet+j})_{\rm bot}/4=R(:,j).
$$


Consequently


$$
\mathscr T(T_{\bullet+j})
=RN_dF_k(:,j)+\delta_kR(:,j)=0.
$$


Thus $\mathscr T$, and hence $\mathscr L_A$, annihilates exactly the admitted forcing-return shifts.

Since $\tau=(\Delta+2)r$, this yields


$$
\mathscr T(\Delta^{j+1}r)=-2\mathscr T(\Delta^jr),
\qquad 0\le j<d.
$$


Because $d$ is even,


$$
\boxed{\mathscr T(\Delta^dr)=2^d\mathscr T(r).}
\tag{14.8}
$$


This recovers the literal shifted-border identity without deleting either $-f$ or $4\rho$, and without installing return order $d$.

---

## 15. New proved follow-on lemma

The preceding calculations establish the following result.

> **Literal residual source-and-path lemma.**  
> For every nonzero actual pivot block $A$, the one-shot residual admits:
> 
> 1. the finite physical functional (12.4)–(12.5);
> 2. the exact return recurrence (12.7);
> 3. the factorial-paid path contraction (13.3), with exactly $s$ component vectors;
> 4. the full paired identities (13.4)–(13.5);
> 5. the evaluated factorial and reciprocal backward recurrences (14.1)–(14.7).
> 
> These are identities over $\mathbb Q$ without any Section-8 lower-bound assumption. Under $\mathrm{H8}$, all asserted residual normalizations are integral. Every occurrence of $R,N_d,\mu_A,K_A,\Lambda_k$, both returns, and both borders is literal.

This is a source-specific finite recurrence, not a generic finite-state assertion. It advances the application beyond a named Schur determinant. It does **not**, by itself, bound the valuations of the two final determinants.

---

# Part IV. Applying the verified rational source representation, with precision and overflow paid

## 16. An integer Hasse numerator formula

Let


$$
F_H=\frac{P_H}{S^{a_H}},
\qquad a_H=2H-1,
\qquad \deg P_H\le2a_H-1.
$$


For $j\ge0$, expand


$$
S(Y+Z)=S(Y)+(1+2Y)Z+Z^2.
$$


The coefficient of $Z^j$ in $P_H(Y+Z)S(Y+Z)^{-a_H}$ is


$$
\begin{aligned}
\partial^{[j]}F_H
={}&
\sum_{b=0}^{\min(j,\deg P_H)}P_H^{[b]}(Y)\\
&\times
\sum_{\substack{u,v\ge0\\u+2v=j-b}}
(-1)^{u+v}
\binom{a_H+u+v-1}{u+v}
\binom{u+v}{v}
\frac{(1+2Y)^u}{S^{a_H+u+v}}.
\end{aligned}
\tag{16.1}
$$


All coefficients are integers.

After multiplication by $S^{a_H+j}$, every exponent of $S$ is nonnegative, and the numerator degree is at most


$$
\deg P_H+j.
\tag{16.2}
$$


Thus the Hasse extraction itself has a completely paid polynomial implementation. No derivative factorial is divided out.

---

## 17. A rational generating row for each actual residual row

For each original top base $a$, define, modulo $2^H$,


$$
\begin{aligned}
\Theta_{a,H}(Y)
={}&o_d\sum_{\ell=0}^d\binom d\ell Q_\ell(a)\\
&\times
\sum_{v=0}^{\min(a+\ell,\nu(H))}
\binom{a+\ell}{v}2^v(d-\ell+1)_v
\partial^{[d-\ell+v]}F_H.
\end{aligned}
\tag{17.1}
$$


For a physical base $m$, define


$$
\Psi_{m,H}(Y)
=
\sum_{v=0}^{\min(m,\nu(H))}
\binom mv2^vv!\,\partial^{[v]}F_H.
\tag{17.2}
$$



Let


$$
\gamma_k=\Lambda_k\eta_d^F\operatorname{odd}(h_d)^2,
\qquad L_d=\alpha-12.
$$


The exact theta-column decomposition gives the actual residual generating row


$$
\boxed{
\begin{aligned}
\mathcal W_{i,H}(Y)
={}&\sum_{a=0}^{d-1}U_{i,a}\Theta_{a,H}(Y)\\
&+2^{L_d}\gamma_k
\left(
\mu_A\Psi_{d+q+i,H}(Y)
-\sum_{b=0}^{q-1}K_A(i,b)\Psi_{d+b,H}(Y)
\right).
\end{aligned}}
\tag{17.3}
$$


Its coefficients $0\le r\le d$ are $W_i^{(r)}\bmod2^H$.

This formula retains:

- every original top source $a$;
- all product-rule shifts $\ell$;
- every physical term still visible at precision $H$;
- the full forcing matrices through $U_{i,a}$;
- the actual $\mu_A$ and $K_A$;
- the actual bottom bases.

It is therefore not a selected-source or selected-tie calculation. The original ties have already been aggregated in the actual integer entries of $A$, $K_A$, and $\mathcal Q_k$.

### 17.1 A finite denominator bound

Every Hasse order in (17.3) is at most


$$
\kappa_H=\min(2d+1,\ d+\nu(H)).
$$


Indeed, the top order is at most $d+a\le2d-1$, and the bottom order is at most $2d+1$.

Set


$$
b_H=a_H+\kappa_H.
$$


Using (16.2), all terms in (17.3) can be put over the common denominator $S^{b_H}$, with numerator degree at most $2b_H-1$:


$$
\mathcal W_{i,H}=\frac{\mathcal P_{i,H}}{S^{b_H}},
\qquad \deg\mathcal P_{i,H}\le2b_H-1.
\tag{17.4}
$$



The actual return recurrence (12.7) corresponds to


$$
\mathcal E_{i,H}(Y)
=(1+\partial_Y)\mathcal W_{i,H}(Y).
$$


Hence


$$
\boxed{
\mathcal E_{i,H}
=
\frac{
S(\mathcal P_{i,H}+\mathcal P_{i,H}')
-b_HS'\mathcal P_{i,H}
}{S^{b_H+1}},
}
\tag{17.5}
$$


whose numerator has degree at most $2b_H+1$.

This gives an explicit source-specific coefficient recurrence. If


$$
S^{b_H+1}=\sum_{j=0}^{M_H}q_jY^j,
\qquad M_H=2(b_H+1),
$$


then


$$
q_j=
\sum_v
\binom{b_H+1}{j-v}\binom{j-v}{v},
\tag{17.6}
$$


with out-of-range binomial coefficients zero. Writing the numerator of (17.5) as $\mathcal N_{i,H}$,


$$
\boxed{
\sum_{j=0}^{\min(M_H,r)}q_jE_{A,i}^{(r-j)}
\equiv[Y^r]\mathcal N_{i,H}\pmod{2^H}.
}
\tag{17.7}
$$



The recurrence is explicit. Its order is not claimed minimal.

---

## 18. The physical cutoff produces an explicit overflow, not a virtual return

Only $0\le r<d$ are original return orders. Let


$$
E_i^{<d}(Y)=\sum_{r=0}^{d-1}E_{A,i}^{(r)}Y^r,
$$


including zero coefficients at selected return orders.

Multiplication by $Q_H(Y)=S^{b_H+1}$ gives the exact finite-boundary polynomial


$$
Q_HE_i^{<d}
=
\operatorname{trunc}_{<d}\mathcal N_{i,H}
+\mathcal B_{i,H}\pmod{2^H},
\tag{18.1}
$$


where the overflow is explicitly


$$
\boxed{
\mathcal B_{i,H}(Y)
=
\sum_{r=d}^{d+M_H-1}
\left(
\sum_{\substack{0\le a<d\\0\le r-a\le M_H}}
q_{r-a}E_{A,i}^{(a)}
\right)Y^r.
}
\tag{18.2}
$$



Every coefficient in (18.2) uses an admitted original return coefficient. No coefficient at $r\ge d$ is supplied by a virtual physical return.

Under $\mathrm{H8}$, all $E_{A,i}^{(r)}$, $r<d$, are divisible by $2^c$. Thus (18.1) may be divided by $2^c$ only after being known to precision $H\ge h+c$, yielding a valid normalized identity modulo $2^h$.

This is the required finite-boundary payment. The rational generating function alone does not justify dividing an infinite continuation by $2^c$.

---

## 19. Precision required for an actual paired upper

Suppose one seeks the bound


$$
v_2\gcd(2J_0,J_1)\le B(d).
$$


A sufficient exact test is that the pair


$$
(2J_0,J_1)
$$


is not zero modulo $2^{B(d)+1}$.

Because the residual matrices are integral under $\mathrm{H8}$, knowledge of their entries modulo


$$
2^h,\qquad h=B(d)+1,
$$


is sufficient to compute their determinants modulo $2^h$. There is no extra factor of $s$ in this precision requirement.

But the entry normalizations must be paid:

- common residual entries require unnormalized entries modulo $2^{h+c}$;
- the constant border requires precision $2^{h+d+1}$;
- the linear border requires precision $2^{h+d}$.

Thus, when the actual $\mu_A,K_A$ are supplied exactly, a safe uniform source precision is


$$
\boxed{H=h+\max(c,d+1).}
\tag{19.1}
$$



If $\mu_A$ and $K_A$ themselves are to be formed from raw common-column residues, their divisions by $2^{f_q}$ require a further $f_q$ digits. A safe common-column input precision is then


$$
\boxed{H_{\rm raw}=h+\max(c,d+1)+f_q.}
\tag{19.2}
$$



These costs cannot be replaced by precision $12$.

For the requested scale


$$
B(d)=\frac54d^2+O(d\log d),
$$


one needs $H\asymp d^2$. At such precision, $\nu(H)$ exceeds every admitted physical base, so the universal physical truncation no longer removes any of the permitted $v$-terms. Also


$$
\kappa_H=2d+1,\qquad
M_H=4H+4d+2.
\tag{19.3}
$$


Thus the direct rational recurrence has order of quadratic size in $d$, whereas only $d$ original return coefficients are available.

This does not prove that a better source-specific recurrence is impossible. It proves that the presently verified denominator bound does **not** supply one.

At this precision the factorial forcing terms also cannot be dismissed as “deep.” Their elementary binary depths are of linear order in $d$, while the needed precision is quadratic. The complete $V$, the bottom corrections, and the factorial part of $r$ remain potentially visible.

---

# Part V. An explicit bound for the full residual pair, and why it misses the target

## 20. Exact original scalar and binary transfer

Retain


$$
\Omega_k=\prod_{a=0}^{d-1}P_d(a),
$$




$$
f_k=(-\Lambda_k)^d\eta_d^F
\left(\prod_{a<d}(2a)!\right)^2,
$$




$$
\lambda_d^{\rm tr}=d\alpha+4d+4,
\qquad
\mathfrak D_d=\prod_{r<d}2^rr!.
$$


The established complete scalar identity is


$$
\boxed{
\delta_k^{d+2}\Omega_kH_k(s)
=
f_k\,2^{\lambda_d^{\rm tr}}\mathfrak D_d
\det\mathcal Q_k(s),
}
\tag{20.1}
$$


up to one common sign.

For contents,


$$
\boxed{
|\delta_k|^{d+2}\Omega_kG_k
=
|f_k|\,2^{\lambda_d^{\rm tr}}\mathfrak D_d\,g_{\mathcal Q,k}.
}
\tag{20.2}
$$



Since $\Lambda_k,\Omega_k,\eta_d^F$ are odd,


$$
v_2(\delta_k)=2\alpha-10,
\qquad
v_2(f_k)=2S_d,
\qquad
v_2(\mathfrak D_d)=S_d.
$$


Therefore


$$
\boxed{
v_2(g_{\mathcal Q,k})
=
v_2(G_k)+C_d,
\qquad
C_d=(d+4)\alpha-14d-24-3S_d.
}
\tag{20.3}
$$



Under $\mathrm{H8}$, (10.6) gives the exact further relation


$$
\boxed{
v_2\gcd(2J_0,J_1)
=
v_2(G_k)+C_d-\mathcal E_q.
}
\tag{20.4}
$$



No odd factor was discarded from the all-prime identities merely because it disappears from these valuation equations.

---

## 21. A rigorous full-pair height cap

This section supplies a genuine, though inadequate, numerical upper bound for the full actual object.

Put


$$
N_\star=3d+1,\qquad F_\star=(2N_\star)!=(6k-4)!.
$$


The recurrence for $u_m$ gives


$$
u_{m+1}=(2m+1)((2m+2)u_m-1),
$$


from which $0<u_m\le(2m)!$ follows by induction. Hence


$$
|c_m|\le2F_\star
$$


through the original physical range.

The finite alternating sum defining $\rho_m$ has absolute value at most $1$, so


$$
|r_m|\le(2m)!+4\le5F_\star.
$$



In the original determinant


$$
H_k(s)=
\det[(c_{m+j})\mid(\Lambda_k(r_{m+j}+s(-1)^{m+j}))],
$$


all $s$-columns are proportional. Therefore $H_{1,k}$ is a sum of exactly $k$ determinants, each containing:

- $k$ $c$-columns;
- $k-1$ $\Lambda_kr$-columns;
- one $\Lambda_kw$-column.

Leibniz’s determinant bound gives


$$
\boxed{
|H_{1,k}|
\le
\mathcal H_d
:=
k(2k)!\,2^k5^{k-1}\Lambda_k^kF_\star^{\,2k-1}.
}
\tag{21.1}
$$


The established $H_{1,k}\ne0$ makes this an upper bound for its binary valuation. Since $G_k\mid H_{1,k}$,


$$
v_2(G_k)\le\lfloor\log_2\mathcal H_d\rfloor.
$$


Consequently the already integral original corrected pencil satisfies


$$
\boxed{
v_2(g_{\mathcal Q,k})
\le
\lfloor\log_2\mathcal H_d\rfloor+C_d.
}
\tag{21.2}
$$


Under $\mathrm{H8}$, the full actual residual pair satisfies


$$
\boxed{
v_2\gcd(2J_0,J_1)
\le
\lfloor\log_2\mathcal H_d\rfloor+C_d-\mathcal E_q.
}
\tag{21.3}
$$



This bound concerns the actual pair. It does not replace the constant border by a theta border; it merely uses the legitimate inequality $G_k\le|H_{1,k}|$.

For an elementary size estimate,


$$
\log_2\Lambda_k
\le(3d+1)\log_2(6d+1),
$$




$$
\log_2F_\star\le(6d+2)\log_2(6d+2).
$$


Thus


$$
\boxed{
v_2\gcd(2J_0,J_1)
\le15d^2\log_2d+O(d^2)
}
\tag{21.4}
$$


under the integral handoff.

This is a proved cap, but it misses the required leading allowance by a factor of order $\log d$. It does not close numerical contact.

---

## 22. Precise obstruction to the proposed terminal upper

The requested residual target is


$$
\boxed{
v_2\gcd(2J_0,J_1)
\le\frac54d^2+O(d\log d)
}
\tag{22.1}
$$


on infinitely many of the same original indices.

The verified source representation does not presently prove it, for four separate reasons.

### 22.1 Representation degree is not a valuation upper

A low-degree rational representation does not bound determinant valuation. Even a constant matrix


$$
\operatorname{diag}(1,\ldots,1,2^M)
$$


has a degree-zero representation and arbitrarily large determinant valuation. In the actual problem the coefficients are fixed, but an additional noncancellation theorem is still necessary.

### 22.2 Precision must reach a nonzero whole paired residue

The numerator recursion at a fixed precision proves only that precision. To establish (22.1) by residue evaluation, the input must be computed at the paid precision in (19.1), or (19.2) when the pivot quotient is reconstructed.

At that precision, the presently available recurrence has order $4H+O(d)$, not a useful fixed or two-dimensional order.

### 22.3 The accepted cofactor theorem does not control the remaining pivots

The accepted theorem supplies a genuine attaining $q$-minor. It does not specify a nested elimination flag for the remaining columns, nor bound the remaining invariant factors.

The path contraction makes the surviving structure explicit: it consists of $s$ actual component vectors $Z_j$. Further elimination of $s-2$ directions would need new paid pivots. Neither the full theta parity corank nor a capped auxiliary profile provides them.

### 22.4 The constant border has an independent alignment obstruction

Equations (14.6)–(14.7) evaluate both source borders, but they do not prove that their projections through the common return rectangle avoid simultaneous deep divisibility.

The factorial accumulator and the reciprocal accumulator in (14.6) may cancel. A theta-only determinant calculation does not control this cancellation. The actual odd pivot and source coefficients participate in it and cannot be replaced by $1$.

The concrete follow-on lemma proved in Sections 12–15 gives the exact object on which a new noncancellation argument must operate. The remaining open obligation is not another formal-series identity: it is a uniform valuation theorem for that fully specified finite recurrence and both of its terminal outputs.

---

# Part VI. All-prime normalization, primitive approximation, and proof status

## 23. Actual contents and least simultaneous clearer

The original all-prime quantities remain


$$
G_k=\gcd(|H_{0,k}|,|H_{1,k}|),
\qquad
d_{H,k}=\gcd(\Lambda_k^k,H_{0,k},H_{1,k}).
$$


The individual least right-column entry clearers are


$$
\Lambda_{k,j}
=\operatorname{lcm}(1,3,\ldots,4k+2j-3).
$$


The least simultaneous coefficient clearer of $H_k/\Lambda_k^k$, and the resulting content, are exactly


$$
\boxed{
\frac{\Lambda_k^k}{d_{H,k}},
\qquad
\frac{G_k}{d_{H,k}}.
}
\tag{23.1}
$$



For the original rectangles


$$
Z_k=[(c_{m+j})_{m<2k,j<k}\mid(T_{m+j})_{m<2k,j<k-1}],
$$




$$
Y_k=[(\sigma_{m+j})_{m<2k-1,j<k}\mid(T_{m+j})_{m<2k-1,j<k}],
$$


retain their actual maximal-minor contents


$$
\mathscr R_k=\delta_{2k-1}(Z_k),\qquad
\mathscr L_k=\delta_{2k-1}(Y_k),
$$


and the established relation


$$
\operatorname{lcm}(\mathscr L_k,\mathscr R_k)
\mid G_k\mid\Lambda_k\mathscr L_k\mathscr R_k.
\tag{23.2}
$$



The paid five-column normalization, including its payments $2^{13},2^{19},2^{32}$, is reused without recalculation:


$$
\boxed{
|\delta_k|^{d+2}\Omega_k|\mu_{5,k}|^{d-4}G_k
=
|f_k|\,2^{\lambda_d^{\rm tr}+d+69}
\mathfrak D_d\,g_k^{[5]}.
}
\tag{23.3}
$$


Its actual odd pivot quotients remain actual.

Under $\mathrm{H8}$, the new residual application retains the exact all-prime identity


$$
\boxed{
|\mu_A|^t|\delta_k|^{d+2}\Omega_kG_k
=
|f_k|\,2^{\lambda_d^{\rm tr}+\mathcal E_q}
\mathfrak D_d\,
\gcd(2|J_0|,|J_1|).
}
\tag{23.4}
$$



None of these gcds is replaced by its $2$-primary part.

---

## 24. Actual primitive denominator and whole same-index error

The actual primitive numerator and denominator remain


$$
q_k=\frac{|H_{1,k}|}{G_k}>0,\qquad
p_k=-\frac{(-1)^kH_{0,k}}{G_k}.
$$


The retained nonzero whole error is


$$
\boxed{
0<\ell_k=q_k(e+\pi)-p_k
=\frac{|H_k(e+\pi)|}{G_k}.
}
\tag{24.1}
$$



A binary upper such as (22.1), even if eventually proved, would not by itself establish the all-prime $G_k$, the actual growth of $q_k$, or the required decay of the whole error.

For example, an irrationality conclusion from this producer would require a same-index argument forcing $\ell_k\to0$: if $e+\pi=P/Q$ were rational, every positive $q_k(e+\pi)-p_k$ would be at least $1/Q$. No such completed whole-error argument is supplied here.

---

## 25. Proved, conditional, finite, and open ledger

| Item | Status |
|---|---|
| Formal ODE and all-precision rational expansion | **Differently proved here** |
| Integer numerator recursion and modulo-$16$ carries | **Differently proved here** |
| Integral Hasse and actual physical-source extraction | **Differently proved here** |
| Arbitrary-pole all-precision carry formula | **Explicit proved formula (4.6)** |
| Top and atom laws modulo $16$ | **PASS**, with literal bases and all ratios retained |
| Modulo-$4$ anti-period | **REUSE** |
| Uniform period $12$ modulo $8$ | **Differently proved here** |
| All-phase periods $3\cdot2^{h-1}$, $h\ge3$ | **Differently proved here** |
| Accepted first-wrap/half-size cofactor theorem | **REUSE as a paid input** |
| FULL17 Section-8 common-minor lower bounds and integral descent | **Different audit pending; used only as $\mathrm{H8}$** |
| Literal residual source functional | **New proved identity** |
| Factorial-paid path contraction of actual returns | **New proved identity** |
| Complete factorial/reciprocal border recurrences | **New proved result** |
| Finite rational recurrence and explicit boundary overflow | **New proved application**, integral under $\mathrm{H8}$ |
| Full-pair height cap | **Proved; residual version conditional on $\mathrm{H8}$** |
| Exact two-dimensional paid reduction | **OPEN** |
| Target $\frac54d^2+O(d\log d)$ residual upper | **OPEN** |
| Other-prime terminal control and final primitive error | **OPEN** |
| Rationality or irrationality of $e+\pi$ | **OPEN** |

The closed auxiliary receipts remain evidence only at their stated finite inputs and precisions. They have not been rerun or promoted to an original-index theorem.

---

## 26. Bounded exact arithmetic needed

**No new bounded arithmetic calculation is indispensable for the proofs in this report, and none is requested.**

The new identities are proved by finite algebra. No original-sized solve, prime scan, closed matrix profile, or old auxiliary receipt needs to be repeated.

A future finite test of the new residual mechanism would have to specify:

1. an actual finite corrected pencil, including both factorial returns and both borders;
2. the exact pivot block $A$, not merely its binary leading sector;
3. the complete odd quotient $\mu_A$ and the paid residue of $K_A$;
4. the precision before every division, as in (19.1)–(19.2);
5. the expected output: the full pair $(2J_0,J_1)$ at that precision, together with all division remainders and the finite overflow (18.2).

Such a calculation would establish only that finite instance. It would not prove the required same-index infinite-family upper.

---

# Final conclusion

The new parent all-precision theta/source and uniform binary-period candidates survive a different proof audit. Their exact hypotheses, integer carries, physical bases, rising ratios, and finite boundaries have been checked without complex convergence, factorial division, virtual returns, or a minimal-period claim.

The primary new result is an exact finite recurrence for the **actual one-shot residual pair**:

- the full corrected source map is retained;
- the selected-return relations contract to exactly $s$ path components;
- all factorial multipliers and odd pivot quotients are preserved;
- the constant border $-f+4\rho$ is evaluated by explicit backward recurrences;
- both bordered determinants remain coupled to the original all-prime scalar identity.

This is not a two-dimensional reduction. The full residual dimension remains


$$
\boxed{s=d/2+m_d+3.}
$$



An explicit full-pair upper of order $d^2\log d$ is proved, but the required


$$
\boxed{v_2\gcd(2J_0,J_1)\le\frac54d^2+O(d\log d)}
$$


is still unproved. The exact remaining bottleneck is uniform noncancellation of the two complete terminal outputs of the derived finite source recurrence, at the paid quadratic precision, on infinitely many of the same original indices.

The all-prime $G_k$, actual least simultaneous clearer, actual primitive denominator $q_k$, and nonzero whole error $\ell_k$ remain unchanged. No unconditional rationality or irrationality conclusion for $e+\pi$ follows.
