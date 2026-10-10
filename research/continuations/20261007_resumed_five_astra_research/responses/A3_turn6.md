> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Complete-source transfer to the saturated endpoint contacts

## Abstract and proof status

The rationality or irrationality of $e+\pi$ remains unresolved.

This report advances the source-crossing calculation in two ways.

1. **An exact complete-source transfer is proved.** The entire physical convolution, including every pre-crossing and post-crossing term, is evaluated by a finite inhomogeneous recurrence with divisions only by $1,\ldots,n+2$. Its forcing coefficients are explicit. The resulting endpoint formulas retain the actual kernel contents $h_j^K$, the exterior return at endpoint $0$, and the existing $F$-payment.

2. **The crossing calculation is specialized further at an original index.** For $n=225$, $p=449$, all four surviving post-crossing source terms and their contributions to the three physical terminal coordinates are evaluated modulo $p^2$. The lift retains $\mathcal W_{448}$, the Wilson quotient, and the half-Fermat quotient. No nonvanishing assumption is made about them.

The transfer does **not** establish contact avoidance on a positive-density prime band or a constant bound on contact lifting depth. It identifies the exact remaining obstruction: after saturation and payment, the question is the divisibility of two explicitly generated endpoint numerators. A unit crossing seed does not determine those numerators.

For primes above the physical terminal, the new lattice identities still do not imply a polynomial bound. An explicit lattice-level counterexample below shows that the identities, even with the correct exterior correction and exact row contents, permit arbitrarily deep endpoint contents. This is a limitation of that proposed inference—not a counterexample to a conjecture about the original seeded source.

No new computation is claimed. The requested bounded calculation concerns the **actual endpoint transfer and contact depths**, not the already completed crossing or frame audits.

---

## 1. Original objects, hypotheses, and reused results

The approximation domain remains exactly


$$
\boxed{n=15^r\quad\text{or}\quad n=105^r,\qquad r\ge2.}
$$


Put


$$
m=n+1,\qquad N=n+2,\qquad K=2n+2.
$$


All such $n$ are odd and at least $225$.

The source and its amplitude are unchanged:


$$
q(z)=1-z+\frac{z^2}{2},
$$




$$
\alpha_0=\alpha_1=1,\qquad
\alpha_s=\alpha_{s-1}-\frac12\alpha_{s-2},
$$




$$
\eta_s=\sum_{r=0}^s\frac1{r!}
       +2\sum_{r=1}^s\frac{\alpha_{r-1}}r,
\qquad
\mathcal W_s=s!\eta_s.
$$


Thus


$$
\boxed{\mathcal W_s=s\mathcal W_{s-1}
       +1+2(s-1)!\alpha_{s-1}.}
\tag{1.1}
$$



The physical terminal is


$$
\boxed{
\widehat w_i=
\sum_{j=0}^{n+i}q_j
\frac{\mathcal W_{2n+i-j}}{(n+i-j)!},
\qquad 0\le i\le2,
}
\tag{1.2}
$$


where $q_j=[z^j]q(z)^n$. Since $n+i\le2n$, this is precisely the supplied finite convolution. Its maximum source index is $K$.

Let


$$
c_k=[z^k]e^zq(z)^n,\qquad
T=
\begin{pmatrix}
c_n&c_{n-1}&c_{n-2}\\
c_{n+1}&c_n&c_{n-1}\\
c_{n+2}&c_{n+1}&c_n
\end{pmatrix},
\qquad J=N!T.
$$


Write $J_0,J_1,J_2$ for its columns and $\Delta=\det J$.

The reference vector is


$$
t=
\begin{pmatrix}
\tau_n\\
(\tau_n+\tau_{n+1})/2\\
\tau_{n+2}/2
\end{pmatrix},
\qquad H=N!t.
$$


The actual reference is determined, equivalently, by


$$
\tau_0=\tau_1=1,\qquad
(k+2)\tau_{k+2}=(2k+3)\tau_{k+1}+(k+1)\tau_k.
$$



We reuse the following established results at their stated scope:

- the complete terminal matching
  

$$
\boxed{N!\widehat w=J_0+E_nH+\mathbf C,}
  \qquad
  E_n=n!\sum_{r=0}^n\frac1{r!};
  \tag{1.3}
$$


- the archived primitive endpoint rows and companion normalization;
- the polynomial payments
  

$$
\kappa_3b_{c,3}\mid4m^2N^2,\qquad
  \kappa_0b_{c,0}\mid4m^2N^2(n+3);
  \tag{1.4}
$$


- the paid contact equality above $N$;
- the one-replacement formula for $D_8$, its invariant-factor interpretation, and the actual row-content formulas;
- the temporal repulsion theorem, without extending it to isolated entrances.

For contact assertions we retain


$$
\det T\ne0,\qquad F\ne0,\qquad \widehat R_j\ne0.
\tag{1.5}
$$


Here, as in the sources,


$$
\begin{gathered}
a_k(n)=k![z^k]e^zq(z)^n,\\
X=ma_n(n),\qquad Y=mn\,a_{n-1}(n),\qquad
Z=2a_{n+1}(n)-ma_n(n),\\
P=nX+Y,\qquad Q=nZ+2X-Y,\qquad
F=2m(Z-Q).
\end{gathered}
$$



The dependence of (1.4) on the archived moment-primitivity theorem is retained. It is not replaced by full-frame primitivity.

### Finite receipts

The supplied receipt records successful checks at $n=225$ of the three Plücker identities, $D_8$, all four actual row contents, and the omitted-column projections. It also records complete first- and second-level crossing checks at $229$ and $239$.

These are finite certificates at the stated index and primes. In particular:

- a one-digit first invariant factor does not establish a universal bound;
- an endpoint/full-frame discrepancy equal to $1$ at $225$ does not establish universal equality;
- the temporal receipt concerns only its stated finite prime interval and block.

Those closed calculations are not requested again.

---

## 2. Splitting the actual convolution at a crossing prime

Fix


$$
N<p\le K,\qquad p\ \text{prime},
$$


and put


$$
h=p-n.
$$


Since $n+i<p$, every factorial in the denominator of (1.2) is a $p$-adic unit.

Writing $l=n+i-j$, the actual split is


$$
\begin{aligned}
\widehat w_i={}&
\sum_{0\le l<h}
q_{n+i-l}\frac{\mathcal W_{n+l}}{l!}\\
&+
\sum_{h\le l\le n+i}
q_{n+i-l}\frac{\mathcal W_{n+l}}{l!},
\end{aligned}
\tag{2.1}
$$


with terms outside $0\le l\le n+i$ omitted. In the second sum put $l=h+d$. Then


$$
\boxed{
\widehat w_i^{\,\mathrm{cross}}
=
\sum_{d=0}^{2n+i-p}
q_{2n+i-p-d}\frac{\mathcal W_{p+d}}{(h+d)!}.
}
\tag{2.2}
$$


An upper limit below zero means an empty sum.

The established crossing formulas are


$$
\mathcal W_{p+d}\equiv B_d\pmod p,
\qquad
B_d=E_d-2\chi_p d!,
\tag{2.3}
$$


where


$$
E_0=1,\qquad E_d=dE_{d-1}+1,\qquad
\chi_p=\left(\frac{-1}{p}\right).
$$


For the second level,


$$
\mathcal W_{p+d}\equiv B_d+pR_d\pmod{p^2},
\tag{2.4}
$$


with


$$
R_0\equiv
\mathcal W_{p-1}
+2\chi_p\bigl(\mathfrak w_p+\varepsilon_p\mathfrak h_p\bigr)
\pmod p,
\tag{2.5}
$$




$$
R_d\equiv dR_{d-1}+B_{d-1}-2(d-1)!a_d\pmod p,
\tag{2.6}
$$


and


$$
\mathfrak w_p=\frac{(p-1)!+1}{p},\qquad
\mathfrak h_p=\frac{2^{(p-1)/2}-\varepsilon_p}{p},
\qquad \varepsilon_p=\left(\frac2p\right),
$$




$$
a_d=
\begin{cases}
\alpha_d,&\chi_p=1,\\[1mm]
\frac12\alpha_{d-2},&\chi_p=-1,
\end{cases}
\qquad \alpha_{-1}=0.
$$



Equations (2.1)–(2.6) specify the split, but by themselves they leave a long convolution. The next theorem evaluates the **whole** convolution by a different finite recurrence. It is an exact identity, not a replacement of the source.

---

## 3. An exact finite recurrence evaluating the complete physical response

Define


$$
L(z)=\int_0^z\frac{dt}{q(t)},\qquad
Y(z)=\frac{e^z+2L(z)}{1-z}.
$$


Then


$$
Y(z)=\sum_{s\ge0}\eta_s z^s.
$$


Consequently, if


$$
g(z)=q(z)^nY^{(n)}(z),
$$


then


$$
[z^{n+i}]g(z)=\widehat w_i.
\tag{3.1}
$$



This is a formal power-series identity. It does not extend the physical inverse or introduce a new approximation index.

### 3.1 The explicitly evaluated rational forcing

Put


$$
\mathcal R_n(z)=q(z)^{n+1}\frac{d^n}{dz^n}\frac1{q(z)}.
$$



**Lemma 3.1.** The polynomial $\mathcal R_n$ has degree at most $n$, and


$$
\boxed{
[z^l]\mathcal R_n
=
n!(-1)^l\binom{n+1}{l}2^{-l}\alpha_{n-l}
\quad(0\le l\le n).
}
\tag{3.2}
$$



**Proof.** Let $r_\pm=(1\pm i)/2$. Since


$$
q(z)=(1-r_+z)(1-r_-z),\qquad r_+r_-=\frac12,
$$


partial fractions give


$$
\mathcal R_n(z)=
\frac{n!}{r_+-r_-}
\left[
r_+^{n+1}(1-r_-z)^{n+1}
-r_-^{n+1}(1-r_+z)^{n+1}
\right].
$$


The coefficient of $z^{n+1}$ cancels. For $0\le l\le n$, the coefficient is


$$
n!(-1)^l\binom{n+1}{l}2^{-l}
\frac{r_+^{n+1-l}-r_-^{n+1-l}}{r_+-r_-},
$$


which is (3.2). ∎

Thus the logarithmic forcing is not left as a derivative or an unevaluated sum.

### 3.2 The complete recurrence

The equation


$$
(1-z)Y'(z)-Y(z)=e^z+\frac2{q(z)}
$$


implies


$$
(1-z)Y^{(n+1)}-(n+1)Y^{(n)}
=e^z+2\left(\frac1q\right)^{(n)}.
$$


Multiplying by $q^{n+1}$ and substituting $g=q^nY^{(n)}$ gives


$$
\begin{aligned}
&(1-z)q\,g'
-\bigl(n(1-z)q'+(n+1)q\bigr)g\\
&\hspace{35mm}=q^{n+1}e^z+2\mathcal R_n(z).
\end{aligned}
\tag{3.3}
$$


Here


$$
(1-z)q=1-2z+\frac32z^2-\frac12z^3
$$


and


$$
n(1-z)q'+(n+1)q
=1+(n-1)z-\frac{n-1}{2}z^2.
$$



Let


$$
\epsilon_l=[z^l]q(z)^{n+1}e^z,\qquad
r_l=[z^l]\mathcal R_n(z),
$$


with $r_l=0$ for $l>n$. If $g_l=[z^l]g$, coefficient comparison proves


$$
\boxed{
\begin{aligned}
(l+1)g_{l+1}={}&(2l+1)g_l
+\frac{2n+1-3l}{2}g_{l-1}\\
&+\frac{l-n-1}{2}g_{l-2}
+\epsilon_l+2r_l.
\end{aligned}
}
\tag{3.4}
$$


The initial data are


$$
g_{-2}=g_{-1}=0,\qquad g_0=\mathcal W_n.
\tag{3.5}
$$



The exponential forcing is itself evaluated by


$$
\epsilon_{-2}=\epsilon_{-1}=0,\qquad \epsilon_0=1,
$$




$$
\boxed{
(l+1)\epsilon_{l+1}
=(l-n)\epsilon_l+
\left(n-\frac{l-1}{2}\right)\epsilon_{l-1}
+\frac12\epsilon_{l-2}.
}
\tag{3.6}
$$


Indeed,


$$
q(q^{n+1}e^z)'=(q+(n+1)q')q^{n+1}e^z
=\left(-n+nz+\frac12z^2\right)q^{n+1}e^z.
$$



### Theorem 3.2 — Complete finite transfer

For each original $n$, equations (3.2), (3.4)–(3.6), run only through


$$
0\le l\le n+1,
$$


evaluate


$$
\boxed{\widehat w=(g_n,g_{n+1},g_{n+2})^T}
\tag{3.7}
$$


exactly.

Every division in this evaluation is by $2$ or by an integer in $1,\ldots,N$. Hence, for every $p>N$, it also evaluates the complete physical response modulo $p^e$, for any specified finite $e$, using only unit divisions.

**Proof.** Equations (3.3)–(3.6) have been derived from the actual generating series of the complete source. The coefficient of $g_{l+1}$ is $l+1$, so the initial value determines the coefficients successively. Equation (3.1) identifies the three retained coefficients with the original convolution. Only coefficients through $N$ are used. ∎

This proves an evaluated transfer of **all surviving terms**, not just the crossed terms. It includes the original amplitude $2$ through the explicit forcing $2r_l$.

It does not yet prove an arithmetic bound on the endpoint values produced by the recurrence.

---

## 4. Removing the reference-direction seed without discarding forcing

The homogeneous solution of (3.3) with constant coefficient $1$ is


$$
A(z)=\frac{q(z)^n}{(1-z)^{n+1}}.
\tag{4.1}
$$


Its three retained coefficients are the reference vector:


$$
\begin{pmatrix}
[z^n]A\\ [z^{n+1}]A\\ [z^{n+2}]A
\end{pmatrix}
=t.
\tag{4.2}
$$


This is the retained reference identity. It can also be checked from the binomial expansion of


$$
q(z)=\frac{1+(1-z)^2}{2}
$$


and the displayed recurrence for $\tau_k$.

Define $z_l$ by the same forced recurrence (3.4), but with


$$
z_{-2}=z_{-1}=z_0=0.
\tag{4.3}
$$


Thus


$$
\begin{aligned}
(l+1)z_{l+1}={}&(2l+1)z_l
+\frac{2n+1-3l}{2}z_{l-1}\\
&+\frac{l-n-1}{2}z_{l-2}
+\epsilon_l+2r_l.
\end{aligned}
\tag{4.4}
$$


Let


$$
\mathbf Z_n=N!(z_n,z_{n+1},z_{n+2})^T.
\tag{4.5}
$$


By uniqueness,


$$
N!\widehat w=\mathcal W_nH+\mathbf Z_n.
\tag{4.6}
$$


Combining this with (1.3) gives the exact original-source identity


$$
\boxed{
\mathbf C=(\mathcal W_n-E_n)H+\mathbf Z_n-J_0.
}
\tag{4.7}
$$



The coefficient


$$
\lambda_n:=\mathcal W_n-E_n
=2n!\sum_{r=1}^n\frac{\alpha_{r-1}}r
\tag{4.8}
$$


is $p$-integral for every $p>N$.

Equation (4.7) has an important scope:

- it does not discard the logarithmic source;
- its amplitude $2$ remains in every $2r_l$ in (4.4);
- it removes only a reference-direction term when working at a contact;
- it is not a new universal rational-gauge construction.

In particular, the complete crossing lift is not an independent random parameter at the endpoint. Its contributions, together with the pre-crossing terms, must satisfy (4.7).

---

## 5. Explicit actual endpoint rows and exact saturation

Write


$$
J=
\begin{pmatrix}
a&b&c\\
d&a&b\\
e&d&a
\end{pmatrix}.
\tag{5.1}
$$


These five entries are the actual scaled moment coefficients, not free parameters.

Define


$$
\mathbf t_3=(d^2-ae,\ be-ad,\ a^2-bd)
\tag{5.2}
$$


and


$$
\begin{aligned}
\mathbf t_0={}&
-\,(a^2-bd,\ cd-ab,\ b^2-ac)\\
&+n(be-ad,\ a^2-ce,\ cd-ab)\\
&-nm(d^2-ae,\ be-ad,\ a^2-bd).
\end{aligned}
\tag{5.3}
$$


Then


$$
\mathbf t_j=\ell_j\operatorname{adj}(J),
\qquad
\ell_0=(-1,n,-nm),\quad \ell_3=(0,0,1).
\tag{5.4}
$$



The actual kernel contents are


$$
h_j^K=\gcd(|t_{j,0}|,|t_{j,1}|,|t_{j,2}|).
\tag{5.5}
$$


Up to the retained sign normalization,


$$
r_j=\sigma_j\frac{\mathbf t_j}{h_j^K},
\qquad \sigma_j\in\{1,-1\}.
\tag{5.6}
$$



Indeed, $\mathbf t_3$ is $J_0\times J_1$. For endpoint $0$,


$$
(nJ_0+J_1)\times(-nmJ_0+J_2)=-\mathbf t_0.
$$


Thus (5.5) is precisely the required saturation payment, not a substitute content.

The omitted-column projections are


$$
\boxed{\mathbf t_3J_2=\Delta,\qquad
       \mathbf t_0J_0=-\Delta.}
\tag{5.7}
$$



### Evaluated endpoint numerators

Define


$$
\Xi_j=r_j(\mathbf Z_n-J_0).
\tag{5.8}
$$


Equations (5.2)–(5.7) give


$$
\boxed{
\Xi_3=
\frac{\sigma_3}{h_3^K}
\left(
t_{3,0}N!z_n+t_{3,1}N!z_{n+1}
+t_{3,2}N!z_{n+2}
\right),
}
\tag{5.9}
$$


and


$$
\boxed{
\Xi_0=
\frac{\sigma_0}{h_0^K}
\left(
t_{0,0}N!z_n+t_{0,1}N!z_{n+1}
+t_{0,2}N!z_{n+2}+\Delta
\right).
}
\tag{5.10}
$$



The $+\Delta$ in (5.10) is essential. It is the transformed exterior return at endpoint $0$; it has not been absorbed into a homogeneous source.

Together, (3.2), (3.6), (4.4), and (5.2)–(5.10) give an explicit finite evaluation of each actual endpoint numerator. No convolution remains to be assigned a generic value.

---

## 6. The paid endpoint rank-drop criterion

Put


$$
R_j=r_jH.
$$


By the retained normalization,


$$
R_j=\frac{m!}{2L}\widehat R_j,
\qquad L=2^{(n+1)/2}.
\tag{6.1}
$$


At $p>N$, the multiplier is a unit.

Equation (4.7) gives


$$
\boxed{C_j=\lambda_nR_j+\Xi_j.}
\tag{6.2}
$$



Let


$$
r=v_p(R_j),\qquad f=v_p(F).
$$


The paid contact depth is


$$
s_j(p)=\min\{(r-f)_+,v_p(C_j)\}.
$$



### Theorem 6.1 — Complete forced endpoint criterion

For every $p>N$,


$$
\boxed{
s_j(p)=\min\{(v_p(R_j)-v_p(F))_+,v_p(\Xi_j)\}.
}
\tag{6.3}
$$



Equivalently, for an integer $u\ge1$, set $b=v_p(h_j^K)$. Then


$$
\boxed{
s_j(p)\ge u
}
$$


if and only if


$$
\boxed{
\begin{aligned}
v_p(\mathbf t_jH)&\ge b+v_p(F)+u,\\
v_p\bigl(\mathbf t_j(\mathbf Z_n-J_0)\bigr)&\ge b+u.
\end{aligned}
}
\tag{6.4}
$$



**Proof.** If $r\le f$, both sides of (6.3) are zero. Otherwise let $d=r-f>0$. Since $\lambda_n$ is $p$-integral and $r\ge d$,


$$
C_j\equiv\Xi_j\pmod{p^d}.
$$


Therefore


$$
\min(d,v_p(C_j))=\min(d,v_p(\Xi_j)).
$$


Using (5.6) proves (6.4). ∎

This is the endpoint-restricted rank criterion **after exact saturation and the existing $F$-payment**.

A modular implementation must respect the payment. If it starts from $\mathbf t_j$, rather than the already primitive $r_j$, it needs the additional $b$ digits shown in (6.4). Dividing a residue modulo $p^2$ by a nonunit $h_j^K$ is not legitimate.

### What is proved, and what is not

The theorem closes an exact transfer obligation: it specifies the actual endpoint numerator, every forcing coefficient used to generate it, and every division.

It does **not** prove that the two conditions in (6.4) cannot hold. In particular, it does not establish:

- a positive-density band of nonresonant primes;
- a constant upper bound on $s_j(p)$;
- a subfactorial bound for the aggregate contact loss.

Those are separate arithmetic obligations about the evaluated sequence in (4.4).

---

## 7. A fully evaluated short crossing at $n=225,\ p=449$

This section gives an additional exact calculation by hand at an original index. It is not the previously completed $229/239$ audit.

Here


$$
n=225,\quad m=226,\quad N=227,\quad K=452,\quad p=449.
$$


The number $449$ is prime: trial division by $2,3,5,7,11,13,17,19$ suffices. Also


$$
\chi_{449}=\varepsilon_{449}=1.
$$



Only the four source positions $449,450,451,452$ can occur in the crossed part. Define


$$
\rho\equiv
\mathcal W_{448}
+2\left(
\frac{448!+1}{449}
+\frac{2^{224}-1}{449}
\right)\pmod{449}.
\tag{7.1}
$$


No assumption is made that $\rho$ is nonzero.

Since


$$
B_0=-1,\quad B_1=0,\quad B_2=1,\quad B_3=4
$$


and


$$
\alpha_1=1,\quad\alpha_2=\frac12,\quad\alpha_3=0,
$$


the lifting recurrence evaluates to


$$
\boxed{
\begin{aligned}
\mathcal W_{449}&\equiv-1+p\rho,\\
\mathcal W_{450}&\equiv p(\rho-3),\\
\mathcal W_{451}&\equiv1+p(2\rho-7),\\
\mathcal W_{452}&\equiv4+p(6\rho-20)
\end{aligned}
\pmod{p^2}.
}
\tag{7.2}
$$


In particular, an actual complete source coefficient immediately following the unit crossing seed vanishes modulo $449$:


$$
\mathcal W_{449}\equiv-1,\qquad
\mathcal W_{450}\equiv0.
\tag{7.3}
$$


This is a finite original-source cancellation, not a variable-amplitude example.

Let


$$
q_1=-n,\qquad q_2=\frac{n^2}{2},\qquad
q_3=-\frac{n(n^2-1)}6,
\qquad T_*=nmN.
$$


Multiplying the crossed part by $N!$, every surviving term is


$$
\begin{aligned}
P^{\rm cross}_0&=T_*q_1\mathcal W_{449}
                  +mN\mathcal W_{450},\\
P^{\rm cross}_1&=T_*q_2\mathcal W_{449}
                  +mNq_1\mathcal W_{450}
                  +N\mathcal W_{451},\\
P^{\rm cross}_2&=T_*q_3\mathcal W_{449}
                  +mNq_2\mathcal W_{450}
                  +Nq_1\mathcal W_{451}
                  +\mathcal W_{452}.
\end{aligned}
\tag{7.4}
$$


Thus


$$
\boxed{
P^{\rm cross}\equiv
\mathbf B+p(\rho\,\mathbf A+\mathbf L)\pmod{p^2},
}
\tag{7.5}
$$


where the following are exact rational expressions, in fact integral at this index:


$$
\mathbf B=
\begin{pmatrix}
-T_*q_1\\
-T_*q_2+N\\
-T_*q_3+Nq_1+4
\end{pmatrix},
$$




$$
\mathbf A=
\begin{pmatrix}
T_*q_1+mN\\
T_*q_2+mNq_1+2N\\
T_*q_3+mNq_2+2Nq_1+6
\end{pmatrix},
$$




$$
\mathbf L=
\begin{pmatrix}
-3mN\\
-3mNq_1-7N\\
-3mNq_2-7Nq_1-20
\end{pmatrix}.
\tag{7.6}
$$



Because $n\equiv1/2\pmod{449}$, these vectors reduce to


$$
\boxed{
\mathbf B\equiv
\begin{pmatrix}
15/16\\145/64\\337/128
\end{pmatrix},\qquad
\mathbf A\equiv
\begin{pmatrix}
45/16\\215/64\\523/128
\end{pmatrix},\qquad
\mathbf L\equiv
\begin{pmatrix}
-45/4\\-95/8\\-405/32
\end{pmatrix}
\pmod{449}.
}
\tag{7.7}
$$


The exact versions in (7.6), not merely their reductions in (7.7), are used in (7.5).

### Endpoint projection and the obstruction to a unit argument

Let $P^{\rm low}=N!\widehat w-P^{\rm cross}$. For either actual endpoint,


$$
\boxed{
C_j\equiv
r_j\bigl(P^{\rm low}+\mathbf B-J_0-E_nH\bigr)
+p\,r_j(\rho\mathbf A+\mathbf L)
\pmod{p^2}.
}
\tag{7.8}
$$



This formula retains:

- every crossed contribution;
- the entire pre-crossing vector;
- the actual primitive endpoint row;
- the exterior term through $-J_0$;
- $\mathcal W_{448}$, Wilson, and half-Fermat data.

The first term in (7.8) is not known to vanish or to be a unit. Nor are


$$
r_j\mathbf A,\qquad r_j\mathbf B,\qquad r_j\mathbf L
$$


determined by the unit $\mathcal W_{449}$.

The complete finite recurrence in Sections 3–5 evaluates the first term together with the crossed terms. It gives (6.3), not a nonvanishing theorem.

This is the precise limitation of the attempted transfer:

> The unit crossing seed does not become a unit endpoint numerator. The actual transfer contains pre-crossing terms, endpoint projection, and saturation; at the second level it contains the fixed residue (7.1). None of these may be declared generic.

Equation (7.3) is an actual source-level counterexample to propagation of the unit property even one step beyond the crossing. It is **not** asserted to be a counterexample to endpoint nonresonance.

---

## 8. Why the first crossing lift cannot be treated as an independent endpoint parameter

There is a further exact original-source obstruction.

From (4.7),


$$
C_j=\lambda_nR_j+\Xi_j.
$$


At every paid level $u\le v_p(R_j)-v_p(F)$, the entire term


$$
\lambda_nR_j
$$


vanishes modulo $p^u$.

Thus the initial-value part of the complete response lies exactly in the reference direction and disappears at the paid contact. The endpoint decision is made by the forced response $\Xi_j$, not by assigning a favorable value to an individual source seed.

This is an identity in the original objects. It explains why a proof based only on “the crossing seed is a unit” cannot close the endpoint obligation.

It does **not** imply that the forcing has become homogeneous. The explicit term


$$
2n!(-1)^l\binom{n+1}{l}2^{-l}\alpha_{n-l}
$$


remains in (4.4), including the terminal nonzero coefficient


$$
2r_n=2n!(-1)^n(n+1)2^{-n}.
$$


Dropping it would change the actual source.

A possible improvement must therefore estimate the arithmetic of this **specific forced recurrence**, rather than the arithmetic of freely chosen crossing residues.

---

## 9. Primes above $K$: what the lattice identities can and cannot do

For $p>K$, no physical source index crosses $p$. The exact transfer (3.2)–(6.4) still applies, but the crossing unit theorem supplies no additional information.

Retain


$$
A_{\rm src}=n!H,\qquad
B_{\rm src}=\mathbf C+E_nH,
$$


and


$$
a^\#=\operatorname{adj}(J)A_{\rm src},\qquad
b^\#=\operatorname{adj}(J)B_{\rm src}.
$$


With


$$
B_\partial=
\begin{pmatrix}
-1&n&-nm\\
1&-n-1&nm+2n\\
0&1&-2n-1\\
0&0&1
\end{pmatrix},
$$


the complete corrected columns are


$$
u=B_\partial J^{-1}A_{\rm src},\qquad
v=e_1+B_\partial J^{-1}B_{\rm src}.
\tag{9.1}
$$


The exterior $e_1=(0,1,0,0)^T$ is retained.

Let


$$
U=B_\partial a^\#,\qquad
V=\Delta e_1+B_\partial b^\#.
$$


The established formulas are


$$
D_8=\frac{|\Delta|}{d_{\rm one}},
\qquad
g_j^{(8)}=\frac{\gcd(|U_j|,|V_j|)}{d_{\rm one}},
\tag{9.2}
$$


and


$$
d_{\rm all}\mid d_{\rm one}\mid|\Delta|,
\qquad
d_{\rm one}^2\mid|\Delta|d_{\rm all}.
\tag{9.3}
$$



At endpoints $0,3$, the transformed exterior correction is zero. Therefore, for $p>N$,


$$
\boxed{
v_p(g_j^{(8)})
=
v_p(h_j^K)
+\min\{v_p(R_j),v_p(C_j)\}
-v_p(d_{\rm one}).
}
\tag{9.4}
$$


This follows directly from


$$
U_j=\pm h_j^K n!R_j,\qquad
V_j=\pm h_j^K(C_j+E_nR_j).
$$


It is an exact accounting identity. It is not an upper bound.

### A checkable limitation of a polynomial-bound inference

The following example is deliberately restricted to the lattice identities. It is not substituted for the original moments or source.

Fix an original $n$, a prime $p>K$, and an integer $E\ge1$. Set


$$
J=I_3,\qquad
H=(n,1,p^E)^T,\qquad
\mathbf C=(2n,2,3p^E)^T.
\tag{9.5}
$$


Use the same $B_\partial$, the same endpoint rows $\ell_0,\ell_3$, and the same exterior correction in (9.1).

Then


$$
\Delta=d_{\rm one}=d_{\rm all}=D_8=1,
\qquad h_0^K=h_3^K=1.
$$


All one-replacement and Plücker identities hold. Nevertheless,


$$
\ell_3H=p^E,\qquad \ell_3\mathbf C=3p^E,
$$


and


$$
\ell_0H=-nm\,p^E,\qquad
\ell_0\mathbf C=-3nm\,p^E.
$$


Since $p>K$, $nm$ is a unit. Both endpoint contents have arbitrarily large $p$-adic depth. Taking a unit payment in this lattice model does not remove it.

This proves:

> The one-replacement identities, full-frame primitivity, the correct exterior correction, and exact retention of row contents do not by themselves impose a pointwise polynomial bound on endpoint contents.

The missing ingredient is an upper bound for the **actual seeded** row contents or the equivalent forced endpoint numerators. Merely defining those contents again does not supply one.

---

## 10. A quantitatively relevant next lemma

The forced recurrence gives a more concrete target than a generic gcd reformulation.

For a fixed $C>0$, consider the statement:

> **Forced endpoint depth lemma.** On an infinite subset of one original family, for every $N<p\le K$ and $j\in\{0,3\}$,
> 

$$
> \min\{(v_p(R_j)-v_p(F))_+,v_p(\Xi_j)\}\le C,
> \tag{10.1}
>
$$


> where $\Xi_j$ is evaluated by (3.2), (3.6), (4.4), and (5.9)–(5.10).

This is not proved here. It is quantitatively useful: if true, then


$$
\log\operatorname{lcm}_{j=0,3}
\gcd(D_j,C_j)_{\{N<p\le K\}}
\le C\sum_{p\le K}\log p=O(n).
\tag{10.2}
$$


Thus a constant depth bound throughout the crossing band would be subfactorial even without contact avoidance at every prime.

A weaker sufficient version would allow exceptional primes, provided their total paid depth weight is $o(n\log n)$.

A separate above-terminal lemma is still required:


$$
\sum_{p>K}\max_{j=0,3}s_j(p)\log p=o(n\log n),
\tag{10.3}
$$


or a stronger polynomial bound. Neither (9.2) nor (9.3) proves (10.3).

These are **upper bounds for contact loss**. They must not be confused with the useful-acquisition problem, which requires a **lower bound**.

---

## 11. Acquisition, physical returns, and final arithmetic remain unchanged

The physical returns remain


$$
N_0=\det T+R_0^{\rm raw}\widehat w,\qquad
N_3=R_3^{\rm raw}\widehat w.
\tag{11.1}
$$


The physical source still ends at $K$, and the coefficient $1$ of the terminal force $\mathfrak f_K$ in $b_{K+1}$ remains present. The differential calculation above is a coefficient identity for the given source, not an extension of the physical inverse.

The actual least simultaneous clearer and primitive rows are


$$
D_8=\operatorname{lcm}_{0\le j\le3}
\bigl(\operatorname{den}(u_j),\operatorname{den}(v_j)\bigr),
$$




$$
g_j^{(8)}=\gcd(|D_8u_j|,|D_8v_j|),
$$




$$
\widetilde u_j=\frac{D_8u_j}{g_j^{(8)}},\qquad
\widetilde v_j=\frac{D_8v_j}{g_j^{(8)}}.
\tag{11.2}
$$


For a nonzero endpoint, the actual primitive endpoint denominator is


$$
|\widetilde u_j|,
$$


not $D_j$, $D_8$, or a selected-prime part.

For an original block $t=bn$, $b\in\{15,105\}$, retain


$$
\boxed{
\mathcal I_t=
\frac{\mathcal I_n c^{\min}_{n,t}}
{\mathcal M_{n,t}\mathcal L_{n,t}},
}
\tag{11.3}
$$


where


$$
\mathcal M_{n,t}
=
\prod_{n+2<p\le t+2}
p^{\min(v_p(F_n),v_p(M_n))}
$$


and


$$
\mathcal L_{n,t}
=
\prod_{p>t+2}p^{(a_n(p)-a_t(p))_+}.
$$


Neither loss has been cancelled. Useful growth requires a sufficiently strong **lower bound** for $\log c^{\min}_{n,t}$.

For nonzero endpoints, put


$$
h_{\rm end}=\gcd(|\widetilde u_0|,|\widetilde u_3|),
\quad
\widetilde u_0=h_{\rm end}A_{\rm wt},\quad
\widetilde u_3=h_{\rm end}B_{\rm wt}.
$$


For a reduced weight $\lambda=a/k_{\rm wt}$, $k_{\rm wt}>0$, retain


$$
J_{\rm wt}
=B_{\rm wt}\widetilde v_0-A_{\rm wt}\widetilde v_3,
$$




$$
T_{\rm wt}=aJ_{\rm wt}
+k_{\rm wt}A_{\rm wt}\widetilde v_3,
$$




$$
F_{\rm gcd}
=\gcd(|A_{\rm wt}|,|a|)
 \gcd(|B_{\rm wt}|,|a-k_{\rm wt}|),
$$




$$
G_{\rm wt}=\gcd(k_{\rm wt},|J_{\rm wt}|),
$$




$$
H_{\rm gcd}
=\gcd\!\left(
h_{\rm end},
\frac{|T_{\rm wt}|}{F_{\rm gcd}G_{\rm wt}}
\right).
$$


The actual primitive fraction is


$$
\boxed{
q_\lambda=
\frac{k_{\rm wt}h_{\rm end}|A_{\rm wt}B_{\rm wt}|}
{F_{\rm gcd}G_{\rm wt}H_{\rm gcd}},
}
$$




$$
\boxed{
p_\lambda=
\operatorname{sgn}(A_{\rm wt}B_{\rm wt})
\frac{T_{\rm wt}}
{F_{\rm gcd}G_{\rm wt}H_{\rm gcd}}.
}
\tag{11.4}
$$


Every gcd here is all-prime.

The required error is the whole expression


$$
\boxed{
q_\lambda(e+\pi)-p_\lambda
=
q_\lambda\left[
(e+\pi)
-\lambda\frac{\widetilde v_0}{\widetilde u_0}
-(1-\lambda)\frac{\widetilde v_3}{\widetilde u_3}
\right].
}
\tag{11.5}
$$


An irrationality proof still requires


$$
\boxed{
0<|q_\lambda(e+\pi)-p_\lambda|\longrightarrow0
}
\tag{11.6}
$$


on the **same infinite original indices** carrying the arithmetic estimates.

Neither endpoint nonvanishing alone nor a bound for a separate summand proves (11.6).

---

## 12. A bounded calculation deciding the new endpoint object

No calculation has been executed in this report.

The following request is new: it decides actual endpoint contact depths and verifies the complete forced transfer. It does not repeat the passing $229/239$ crossing audit, the old producer, the companion, or the frame-content calculation.

### Inputs

Use only


$$
\boxed{n=225,\quad N=227,\quad K=452.}
$$


Reuse the preserved exact data


$$
J,\ H,\ \mathbf C,\ F,\ r_0,\ r_3,\ h_0^K,\ h_3^K,
$$


together with the already retained actual corrected columns and contents.

Compute the new recurrence data:

1. $\alpha_l$ for $0\le l\le225$;
2. $\epsilon_l$ by (3.6), through $l=226$;
3. $r_l$ by (3.2);
4. $z_l$ by (4.4), through $l=227$;
5. $\mathbf Z_{225}$, $\Xi_0$, and $\Xi_3$.

These are bounded rational calculations with explicit recurrences and terminal indices.

### Expected verifiable output

Return:

1. zero residuals in
   

$$
\mathbf C=(\mathcal W_{225}-E_{225})H
                +\mathbf Z_{225}-J_0;
$$


   the scalar $\mathcal W_{225}-E_{225}$ may be evaluated directly by (4.8);

2. zero residuals in the two explicit endpoint formulas (5.9)–(5.10), including the $+\Delta$ term at endpoint $0$;

3. for every prime
   

$$
\boxed{227<p\le452},
$$


   the exact integers
   

$$
v_p(h_j^K),\quad v_p(F),\quad
   v_p(R_j),\quad v_p(C_j),\quad v_p(\Xi_j),
$$


   and
   

$$
s_j(p)=\min\{(v_p(R_j)-v_p(F))_+,v_p(C_j)\};
$$



4. verification of (6.3) at both endpoints for every prime in that finite band;

5. the exact finite contact-loss product
   

$$
\boxed{
   \prod_{227<p\le452}
   p^{\max(s_0(p),s_3(p))}.
   }
   \tag{12.1}
$$



Exact division of known integers determines these valuations; no depth clipping is necessary.

### Optional focused second-level output at $449$

If the preserved source data include $\mathcal W_{448}$, additionally evaluate (7.1) and return the actual residues


$$
r_jP^{\rm low},\quad r_j\mathbf B,\quad
r_j\mathbf A,\quad r_j\mathbf L
$$


at the precisions required by the **already saturated** rows. Verify (7.8) modulo $449^2$.

This evaluates a new endpoint cancellation, not merely the individual source-crossing identities.

Any nonresonance or resonance found establishes only its stated finite scope. In particular, a product (12.1) equal to $1$ must be reported as a finite absence of crossing-band contact—not as an infinite theorem.

---

## 13. Conclusion and exact remaining bottleneck

The main new proved statement is the complete forced transfer


$$
\boxed{
C_j=(\mathcal W_n-E_n)R_j+\Xi_j,
}
$$


where $\Xi_j$ is explicitly evaluated by the finite recurrences and endpoint formulas above. Consequently,


$$
\boxed{
v_p\gcd(D_j,C_j)
=
\min\{(v_p(R_j)-v_p(F))_+,v_p(\Xi_j)\}
\qquad(p>N).
}
$$


The evaluation retains the actual amplitude $2$, all forcing, the physical terminal, the endpoint-$0$ exterior return, and the exact kernel saturation.

The $n=225,\ p=449$ calculation evaluates every surviving crossed term through $p^2$. It exhibits the actual cancellation


$$
\mathcal W_{449}\not\equiv0,\qquad
\mathcal W_{450}\equiv0\pmod{449},
$$


and retains the complete lift seed involving $\mathcal W_{448}$, Wilson, and half-Fermat quotients. It does not establish endpoint resonance or nonresonance without evaluating the actual rows and pre-crossing contribution.

The precise remaining arithmetic bottlenecks are:

1. a quantitative upper bound for the paid divisibility of the forced endpoint values $\Xi_j$ in the crossing band;
2. separate control of primes above $K$, where there is no crossing mechanism;
3. a useful acquisition **lower** bound paying both retained moving-prime losses;
4. transport through the actual all-prime row contents and final weight gcd;
5. a nonzero whole-error estimate at the same infinite original indices.

The lattice identities alone cannot supply the second item, and the unit crossing seed alone cannot supply the first.

Finally, if $e+\pi=a/d$ were rational, every nonzero integer linear form $q(e+\pi)-p$ would have absolute value at least $1/d$. Therefore (11.6) would prove irrationality. No theorem established here supplies that final chain.



$$
\boxed{\text{The unconditional rationality or irrationality of }e+\pi\text{ remains unresolved.}}
$$


